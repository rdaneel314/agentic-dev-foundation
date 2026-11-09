"""Verify unavailable scanners and detected findings cannot become green checks."""
import contextlib
import io
import json
from pathlib import Path
import runpy
import subprocess
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_secrets.py"


class SecretGateTests(unittest.TestCase):
    def invoke(self, output):
        with patch("subprocess.run", return_value=subprocess.CompletedProcess([], 0, output)):
            with contextlib.redirect_stdout(io.StringIO()):
                runpy.run_path(str(SCRIPT), run_name="__main__")

    def test_empty_valid_report_passes(self):
        self.invoke(json.dumps({"results": {}}))

    def test_candidate_fails_without_printing_value(self):
        captured = io.StringIO()
        report = json.dumps({"results": {"sample.txt": [{"hashed_secret": "redacted"}]}})
        with contextlib.redirect_stdout(captured):
            with self.assertRaises(SystemExit) as failure:
                self.invoke(report)
        self.assertEqual(failure.exception.code, 1)
        self.assertNotIn("hashed_secret", captured.getvalue())

    def test_invalid_report_blocks(self):
        for output in ("not json", "{}", '{"results": []}'):
            with self.subTest(output=output):
                with self.assertRaises((ValueError, AssertionError)):
                    self.invoke(output)

    def test_scanner_execution_failure_blocks(self):
        with patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "scanner")):
            with self.assertRaises(subprocess.CalledProcessError):
                runpy.run_path(str(SCRIPT), run_name="__main__")


if __name__ == "__main__":
    unittest.main()
