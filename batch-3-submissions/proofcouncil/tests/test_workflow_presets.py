from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from proofstack.registry import load_preset  # noqa: E402


class WorkflowPresetTests(unittest.TestCase):
    def test_conditional_repeat_keeps_solution_when_improver_is_skipped(self) -> None:
        preset = load_preset("conditional_repeat_screenshot")

        state_updates = preset.raw["dag"]["nodes"][1]["body"]["state_updates"]

        self.assertEqual(
            state_updates["solution"],
            {"coalesce": ["$node.improve_draft.solution", "$state.solution"]},
        )


if __name__ == "__main__":
    unittest.main()
