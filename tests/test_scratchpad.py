"""Unit tests for AgentScratchpad."""
import unittest
from agent_scratchpad_lru.scratchpad import AgentScratchpad

class TestAgentScratchpad(unittest.TestCase):
    def test_lru_eviction(self):
        sp = AgentScratchpad(max_entries=2)
        sp.set("k1", "val1")
        sp.set("k2", "val2")
        sp.set("k3", "val3")
        self.assertIsNone(sp.get("k1"))
        self.assertEqual(sp.get("k2"), "val2")
        self.assertEqual(sp.get("k3"), "val3")

    def test_pinned_never_evicted(self):
        sp = AgentScratchpad(max_entries=2)
        sp.set("pinned_key", "must_keep", pinned=True)
        sp.set("k2", "val2")
        sp.set("k3", "val3")
        self.assertEqual(sp.get("pinned_key"), "must_keep")

if __name__ == "__main__":
    unittest.main()
