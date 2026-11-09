"""Block current-file candidates/errors without printing values; no online verification."""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]


def scan(path, exclude=None):
    path = path.resolve()  # Normalize Windows short-name temp paths before scanning.
    args = [sys.executable, "-m", "detect_secrets", "scan", "--all-files", "--no-verify"]
    if exclude:
        args += ["--exclude-files", exclude]
    # detect-secrets ignores paths outside its working directory. Anchor each scan
    # to the actual target so relocated trees and temporary metadata are covered.
    cwd = path if path.is_dir() else path.parent
    target = "." if path.is_dir() else path.name
    result = subprocess.run(args + [target], cwd=cwd, capture_output=True, text=True, timeout=120, check=True)
    report = json.loads(result.stdout)
    if not isinstance(report, dict) or not isinstance(report.get("results"), dict):
        raise ValueError("Invalid secret-scan output")
    if report["results"]:
        print("Potential secrets found; inspect privately before publication:")
        for filename, entries in report["results"].items():
            print(f"{Path(filename).name}: {len(entries)} finding(s)")
        raise SystemExit(1)


# Official wheel digests are not secrets. Validate the complete metadata file's
# digest fields against the reviewed lock, then scan all its other fields in a
# temporary view. No blanket high-entropy filter or exclusion of metadata content.
metadata = json.loads((root / "docs/dependency-provenance.json").read_text())
allowed = set(re.findall(r"--hash=sha256:([0-9a-f]{64})", (root / "requirements-ci.lock").read_text()))
for info in metadata.values():
    for wheel in info["wheels"]:
        if wheel["sha256"] not in allowed:
            raise ValueError("Unreviewed wheel digest in dependency metadata")
        wheel["sha256"] = "REVIEWED_WHEEL_DIGEST"

scan(root, r"(^|[/\\])(\.git|\.venv|__pycache__)([/\\]|$)|(^|[/\\])docs[/\\]dependency-provenance\.json$")
with tempfile.TemporaryDirectory() as folder:
    view = Path(folder) / "dependency-provenance-view.json"
    view.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    scan(view)
print("PASS: no current-file candidates; reviewed wheel digests normalized, metadata otherwise scanned")
