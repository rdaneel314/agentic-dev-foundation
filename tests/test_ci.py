"""CI and lock regression tests; full suite requires documented CI tools."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


@unittest.skipUnless(importlib.util.find_spec("yaml"), "Full CI tools required for YAML checks")
class WorkflowTests(unittest.TestCase):
    def setUp(self):
        import check_yaml
        self.check = check_yaml.validate
        self.text = (ROOT / ".github/workflows/ci.yml").read_text()

    def test_valid_prepared_workflow(self):
        self.check(self.text)

    def test_unsafe_or_weakened_workflows_rejected(self):
        variants = [self.text.replace("contents: read", "contents: write"),
                    self.text.replace("--require-hashes", "--no-deps"),
                    self.text.replace("windows-latest", "self-hosted"),
                    self.text.replace("  pull_request:", "  pull_request_target:"),
                    self.text + "\npermissions:\n  contents: read\n",
                    self.text.replace("        run: python scripts/scan_secrets.py", "        continue-on-error: true\n        run: python scripts/scan_secrets.py")]
        for text in variants:
            with self.subTest(variant=variants.index(text)), self.assertRaises(ValueError):
                self.check(text)

    def test_optimized_python_still_rejects_unsafe_yaml(self):
        code = "import sys; sys.path.insert(0," + repr(str(ROOT / "scripts")) + "); import check_yaml; check_yaml.validate(" + repr(self.text.replace("contents: read", "contents: write")) + ")"
        result = subprocess.run([sys.executable, "-B", "-O", "-c", code], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)


@unittest.skipUnless(importlib.util.find_spec("packaging"), "Full CI tools required for lock checks")
class LockTests(unittest.TestCase):
    def test_complete_lock_and_installed_versions(self):
        import check_dependencies
        self.assertGreater(check_dependencies.check(), 4)

    def test_removed_dependency_or_forged_hash_blocks(self):
        import check_dependencies
        for mode in ("missing", "hash"):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "docs").mkdir()
                for name in ("requirements-ci.txt", "requirements-ci.lock", "docs/dependency-provenance.json"):
                    shutil.copy2(ROOT / name, root / name)
                provenance = json.loads((root / "docs/dependency-provenance.json").read_text())
                if mode == "missing":
                    provenance.pop(next(iter(provenance)))
                else:
                    provenance[next(iter(provenance))]["wheels"][0]["sha256"] = "0" * 64
                (root / "docs/dependency-provenance.json").write_text(json.dumps(provenance))
                with self.subTest(mode=mode), self.assertRaises(ValueError):
                    check_dependencies.check(root, installed=False)


if __name__ == "__main__":
    unittest.main()
