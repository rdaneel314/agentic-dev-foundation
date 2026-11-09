"""Parse prepared CI and reject regressions; not hosted workflow execution."""
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


class UniqueLoader(yaml.BaseLoader):
    pass


def unique_mapping(loader, node):
    result = {}
    for key, value in node.value:
        key = loader.construct_object(key)
        if key in result:
            raise ValueError("Duplicate YAML key")
        result[key] = loader.construct_object(value)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def validate(text):
    d = yaml.load(text, Loader=UniqueLoader)
    if not isinstance(d, dict) or set(d.get("on", {})) != {"pull_request", "push"}:
        raise ValueError("Unexpected workflow trigger")
    if d.get("permissions") != {"contents": "read"}:
        raise ValueError("Workflow must have read-only contents permission")
    jobs = d.get("jobs", {})
    if set(jobs) != {"foundation-checks"}:
        raise ValueError("Unexpected jobs; review policy changes explicitly")
    job = jobs["foundation-checks"]
    if job.get("timeout-minutes") != "10" or job.get("runs-on") != "${{ matrix.os }}":
        raise ValueError("Expected bounded OS matrix")
    if set(job["strategy"]["matrix"]["os"]) != {"ubuntu-24.04", "windows-latest"}:
        raise ValueError("Both Windows and Ubuntu checks required")
    if any(k in job for k in ("permissions", "continue-on-error", "if", "container", "services")):
        raise ValueError("Job override needs independent policy review")
    actions, commands = [], []
    for step in job["steps"]:
        if any(k in step for k in ("continue-on-error", "if", "env")):
            raise ValueError("Checks must not be conditional or weakened")
        if "uses" in step:
            action = step["uses"]
            if not re.fullmatch(r"actions/(?:checkout|setup-python)@[0-9a-f]{40}", action):
                raise ValueError("Only full-SHA-pinned official setup actions expected")
            actions.append(action.split("@")[0])
            if action.startswith("actions/checkout@") and step.get("with", {}).get("persist-credentials") != "false":
                raise ValueError("Checkout must not persist credentials")
            if action.startswith("actions/setup-python@") and step.get("with", {}).get("python-version") != "3.13":
                raise ValueError("Python baseline mismatch")
        commands.append(step.get("run", ""))
    if sorted(actions) != ["actions/checkout", "actions/setup-python"]:
        raise ValueError("Expected checkout and Python setup")
    expected = ["python -m pip install --only-binary=:all: --require-hashes -r requirements-ci.lock",
                "python scripts/check_foundation.py", "python -m unittest discover -s tests -v",
                "python scripts/check_yaml.py", "python scripts/check_dependencies.py",
                "python scripts/scan_secrets.py", "python -m pip check",
                "python -m pip_audit --strict --disable-pip --no-deps -r requirements-ci.lock"]
    if sorted(c for c in commands if c) != sorted(expected):
        raise ValueError("Unexpected/missing mandatory command; no failure suppression allowed")
    if any(v in text for v in ("${{ secrets.", "self-hosted", "pull_request_target", "id-token: write")):
        raise ValueError("Privileged CI reference")


if __name__ == "__main__":
    files = list((ROOT / ".github/workflows").glob("*.yml"))
    if len(files) != 1:
        raise SystemExit("FAIL: expected one reviewed workflow")
    validate(files[0].read_text(encoding="utf-8"))
    print("PASS: YAML syntax, duplicate keys, matrix and mandatory CI boundaries")
