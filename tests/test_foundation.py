"""Negative-path tests for portable validation and synthetic contracts."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


foundation = load("check_foundation")
contract = load("validate_contract")


class FoundationTests(unittest.TestCase):
    def test_missing_continuity_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            messages = foundation.verify(Path(tmp))
        for name in ("AGENTS.md", "PROJECT_STATUS.md", "DECISIONS.md", "ROADMAP.md"):
            self.assertTrue(any(name in message for message in messages))

    def test_escaping_and_missing_links_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "page.md"
            page.write_text("ok")
            self.assertEqual(foundation.link_issues(page, root, "[ok](page.md) [a](#heading)"), [])
            self.assertEqual(len(foundation.link_issues(page, root, "[bad](missing.md) [out](../outside.md)")), 2)

    def test_warning_does_not_echo_credential(self):
        fake = "AKIA" + "X" * 16
        messages = foundation.content_issues("synthetic", fake)
        self.assertTrue(messages)
        self.assertNotIn(fake, str(messages))

    def test_user_paths_rejected_relative_paths_allowed(self):
        self.assertTrue(foundation.content_issues("x", "C:" + "\\Users\\someone\\project"))
        self.assertEqual(foundation.content_issues("x", "docs/setup/NEW_COMPUTER.md"), [])

    def test_private_environment_is_rejected_without_reading_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".env").write_text("SYNTHETIC_PRIVATE_VALUE")
            messages = foundation.verify(root)
        self.assertTrue(any("private/config" in m for m in messages))
        self.assertNotIn("SYNTHETIC_PRIVATE_VALUE", str(messages))

    def test_optimized_python_still_rejects_missing_foundation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            shutil.copy2(ROOT / "scripts/check_foundation.py", root / "scripts/check_foundation.py")
            result = subprocess.run([sys.executable, "-B", "-O", str(root / "scripts/check_foundation.py")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Missing required file", result.stdout)

    def test_optimized_python_still_rejects_invalid_scanner_output(self):
        script = ROOT / "scripts/scan_secrets.py"
        code = "import runpy,subprocess; from unittest.mock import patch; "
        code += "\nwith patch('subprocess.run',return_value=subprocess.CompletedProcess([],0,'{}')):\n runpy.run_path(" + repr(str(script)) + ",run_name='__main__')"
        result = subprocess.run([sys.executable, "-B", "-O", "-c", code], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Invalid secret-scan output", result.stderr)


class ContractTests(unittest.TestCase):
    def example(self, name):
        return json.loads((ROOT / "workflows/examples" / (name + ".json")).read_text())

    def test_synthetic_examples_validate(self):
        for name in ("task", "finding"):
            contract.check_record(name, self.example(name))

    def test_missing_unknown_and_wrong_typed_task_fields_block(self):
        for change in ("missing", "unknown", "boolean-timeout"):
            task = self.example("task")
            if change == "missing":
                task.pop("authorization_ref")
            elif change == "unknown":
                task["grant_admin"] = True
            else:
                task["timeout_seconds"] = True
            with self.subTest(change=change), self.assertRaises(ValueError):
                contract.check_record("task", task)

    def test_task_cannot_escape_or_grant_external_effects(self):
        for raw in ("../private", "/absolute", "C:/machine", "docs\\other"):
            task = self.example("task")
            task["allowed_paths"] = [raw]
            with self.subTest(path=raw), self.assertRaises(ValueError):
                contract.check_record("task", task)
        task["allowed_paths"] = ["docs"]
        task["external_effects"] = "deploy"
        with self.assertRaises(ValueError):
            contract.check_record("task", task)

    def test_high_findings_cannot_hide_blocker(self):
        finding = self.example("finding")
        finding.update(severity="high", blocking=False)
        with self.assertRaises(ValueError):
            contract.check_record("finding", finding)

    def test_finding_cannot_self_resolve_or_omit_disposition(self):
        finding = self.example("finding")
        finding.update(status="resolved", verified_by=finding["reporter_id"], disposition="synthetic-fixed")
        with self.assertRaises(ValueError):
            contract.check_record("finding", finding)
        finding.update(verified_by="separate-synthetic-reviewer", disposition="")
        with self.assertRaises(ValueError):
            contract.check_record("finding", finding)
        finding["disposition"] = "independent-synthetic-evidence"
        contract.check_record("finding", finding)

    def test_unsupported_schema_does_not_silently_pass(self):
        with self.assertRaises(ValueError):
            contract.validate({}, {"type": "object", "unsupported": True})


if __name__ == "__main__":
    unittest.main()
