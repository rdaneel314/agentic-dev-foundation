"""Disposable negative test for the live M1 required-check gate; never merge."""
import unittest


class GovernanceProbe(unittest.TestCase):
    def test_intentional_failure_blocks_merge(self):
        self.fail("Intentional M1 governance probe: this branch must not merge.")
