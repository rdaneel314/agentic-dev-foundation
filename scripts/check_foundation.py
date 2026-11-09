"""Offline structural/link and disclosure heuristics; not a security audit."""
from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "PROJECT_STATUS.md", "ROADMAP.md", "DECISIONS.md",
    "SECURITY.md", "CONTRIBUTING.md", "pyproject.toml", ".python-version", ".env.example",
    ".gitignore", ".gitattributes", "requirements-ci.txt", "requirements-ci.lock",
    "docs/backlog.md", "docs/governance.md", "docs/architecture.md", "docs/verification.md",
    "docs/ci.md", "docs/DEPENDENCIES.md", "docs/dependency-provenance.json",
    "docs/setup/NEW_COMPUTER.md", "docs/setup/SWITCHING_COMPUTERS.md",
    "docs/PUBLIC_DISCLOSURE_CHECKLIST.md", "docs/LICENSE_DECISION.md",
    "docs/CROSS_AGENT_REPORTING.md", "docs/records/0001-m0-foundation.md",
    "agents/README.md", "agents/TASK_TEMPLATE.md", "policies/AUTHORIZATION.md",
    "policies/SECURITY.md", "workflows/schemas/task.schema.json",
    "workflows/schemas/finding.schema.json", "workflows/README.md",
    ".github/workflows/ci.yml", ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/task.md", "scripts/check_yaml.py", "scripts/scan_secrets.py",
    "scripts/check_dependencies.py", "scripts/validate_contract.py", "tests/test_foundation.py",
)
SKIP = {".git", ".venv", "__pycache__", ".pytest_cache"}
PRIVATE = {"private", "private-planning", ".aws", ".ssh", "secrets", "credentials"}
MACHINE_PATH = re.compile(r"[A-Za-z]:[\\/]Users[\\/]|/(?:home|Users)/[^/\s]+/")
KEY = re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|\bgh[pousr]_[A-Za-z0-9]{30,}\b|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
TEXT = {".md", ".py", ".toml", ".yml", ".json", ".txt", ".lock"}


def content_issues(name, text):
    issues = []
    for number, line in enumerate(text.splitlines(), 1):
        if MACHINE_PATH.search(line):
            issues.append(f"{name}:{number}: machine-specific user path")
        if KEY.search(line):
            issues.append(f"{name}:{number}: credential candidate; inspect privately")
    return issues


def link_issues(path, root, text):
    issues = []
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = unquote(raw.split("#")[0])
        if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        destination = (path.parent / target).resolve()
        if not destination.is_relative_to(root.resolve()) or not destination.is_file():
            issues.append(f"{path.relative_to(root)}: missing or escaping document link")
    return issues


def verify(root=ROOT):
    root = root.resolve()
    issues = [f"Missing required file: {name}" for name in REQUIRED if not (root / name).is_file()]
    seen = set()
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        parts = {p.casefold() for p in relative.parts}
        if parts & SKIP:
            continue
        if path.is_symlink():
            issues.append(f"{relative}: symbolic link requires removal/review")
            continue
        if parts & PRIVATE:
            issues.append(f"{relative}: private location inside public payload")
        if not path.is_file():
            continue
        folded = relative.as_posix().casefold()
        if folded in seen:
            issues.append(f"{relative}: case-colliding path")
        seen.add(folded)
        if (path.name.startswith(".env") and path.name != ".env.example") or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx", ".zip"}:
            issues.append(f"{relative}: private/config/archive file in public tree")
            continue
        if path.suffix in TEXT or path.name.startswith("."):
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeError, OSError):
                issues.append(f"{relative}: unreadable text")
                continue
            issues.extend(content_issues(relative, text))
            if path.suffix == ".md":
                issues.extend(link_issues(path, root, text))
    try:
        project = tomllib.loads((root / "pyproject.toml").read_text())["project"]
        if project["requires-python"] != ">=3.13,<3.14" or project["dependencies"] != []:
            issues.append("Unexpected runtime dependency/Python baseline")
        if (root / ".python-version").read_text().strip() != "3.13":
            issues.append("Python version file disagrees with baseline")
    except (OSError, KeyError, tomllib.TOMLDecodeError):
        issues.append("Invalid project metadata")
    if not list((root / "tests").glob("test_*.py")):
        issues.append("No test modules found")
    return issues


def main():
    if sys.version_info[:2] != (3, 13):
        print("FAIL: use Python 3.13.x")
        return 1
    issues = verify()
    for issue in issues:
        print("FAIL:", issue)
    if not issues:
        print(f"PASS: {len(REQUIRED)} required files, local links, metadata and public-boundary heuristics")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
