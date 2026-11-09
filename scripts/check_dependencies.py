"""Check exact tool lock, official hash provenance, installed versions and closure."""
from importlib import metadata
import json
from pathlib import Path
import re

from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.utils import canonicalize_name

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT, installed=True):
    text = (root / "requirements-ci.lock").read_text()
    records = {}
    for entry in text.replace("\\\n", " ").splitlines():
        if not entry.strip() or entry.startswith("#"):
            continue
        parts = entry.split()
        req = Requirement(parts[0])
        name = canonicalize_name(req.name)
        if not re.fullmatch(r"[\w.-]+==[\w.+-]+", parts[0]) or name in records:
            raise ValueError("Duplicate/unpinned lock entry")
        hashes = {p.removeprefix("--hash=sha256:") for p in parts[1:]}
        if not hashes or any(not re.fullmatch(r"[0-9a-f]{64}", h) for h in hashes):
            raise ValueError("Missing/invalid wheel hashes")
        records[name] = (str(next(iter(req.specifier))).removeprefix("=="), hashes)
    provenance = json.loads((root / "docs/dependency-provenance.json").read_text())
    if set(records) != set(provenance):
        raise ValueError("Lock/provenance package mismatch")
    for name, (version, hashes) in records.items():
        info = provenance[name]
        if info["version"] != version or info["source"] != f"https://pypi.org/pypi/{name}/{version}/json":
            raise ValueError("Version/source provenance mismatch")
        if hashes != {f["sha256"] for f in info["wheels"]}:
            raise ValueError("Hash provenance mismatch")
        if not SpecifierSet(info["requires_python"] or "").contains("3.13.5"):
            raise ValueError("Package does not support baseline Python")
        if installed and metadata.version(name) != version:
            raise ValueError(f"Installed tool version differs from lock: {name}")
    roots = [Requirement(s) for s in (root / "requirements-ci.txt").read_text().splitlines() if s.strip() and not s.startswith("#")]
    queue, seen, reached = list(roots), set(), set()
    while queue:
        req = queue.pop()
        name = canonicalize_name(req.name)
        if name not in records or not req.specifier.contains(records[name][0]):
            raise ValueError(f"Unsatisfied transitive constraint: {name}")
        reached.add(name)
        for extra in {"", *req.extras}:
            if (name, extra) in seen:
                continue
            seen.add((name, extra))
            for raw in provenance[name]["requires_dist"]:
                child = Requirement(raw)
                for platform, os_name, system in [("win32", "nt", "Windows"), ("linux", "posix", "Linux"), ("darwin", "posix", "Darwin")]:
                    env = dict(default_environment(), python_version="3.13", python_full_version="3.13.5", sys_platform=platform, os_name=os_name, platform_system=system, extra=extra)
                    if child.marker is None or child.marker.evaluate(env):
                        queue.append(child)
                        break
    if reached != set(records):
        raise ValueError("Lock includes unrelated environment packages")
    return len(records)


if __name__ == "__main__":
    print(f"PASS: {check()} exact versions, wheel hashes and dependency closure (three OS marker contexts)")
