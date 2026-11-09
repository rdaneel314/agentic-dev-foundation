import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.approval_policy import ready_for_human


class ReadinessTests(unittest.TestCase):
    def result(self, **changes):
        data = dict(author="engineer", reviewer="reviewer", reviewed_commit="abc",
                    current_commit="abc", tests_passed=True, security_passed=True,
                    qa_identity="qa", security_identity="security", qa_commit="abc", security_commit="abc")
        data.update(changes)
        return ready_for_human(**data)

    def test_independent_current_verified_work_is_ready(self):
        self.assertTrue(self.result())

    def test_self_review_is_blocked_case_insensitively(self):
        self.assertFalse(self.result(reviewer="ENGINEER"))

    def test_new_commit_invalidates_review(self):
        self.assertFalse(self.result(current_commit="def"))

    def test_failed_or_unavailable_verification_blocks(self):
        for field in ("tests_passed", "security_passed"):
            for value in (False, None, "passed", 1):
                with self.subTest(field=field, value=value):
                    self.assertFalse(self.result(**{field: value}))

    def test_missing_identity_or_commit_blocks(self):
        for field in ("author", "reviewer", "current_commit", "reviewed_commit"):
            self.assertFalse(self.result(**{field: ""}))

    def test_unresolved_or_invalid_findings_block(self):
        for value in (1, -1, None, False):
            self.assertFalse(self.result(findings_open=value))

    def test_qa_and_security_must_be_distinct_and_current(self):
        for change in ({"qa_identity": "ENGINEER"}, {"security_identity": "reviewer"},
                       {"security_identity": "qa"}, {"qa_identity": None},
                       {"qa_commit": "old"}, {"security_commit": None}):
            with self.subTest(change=change):
                self.assertFalse(self.result(**change))


if __name__ == "__main__":
    unittest.main()
