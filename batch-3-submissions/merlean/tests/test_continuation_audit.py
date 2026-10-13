"""Independent regression audit: acceptance gates must not depend on self-acceptance."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import test_codex_pilot as fixtures


class ContinuationAcceptanceAudit(unittest.TestCase):
    def scenario(self, *, fail_grade=False):
        original_main_turn = pilot.Problem.main_turn
        observed = []

        async def cautious_main(problem, instruction, *, dossier=False, purpose=None):
            answer = await original_main_turn(problem, instruction, dossier=dossier, purpose=purpose)
            answer['complete_claim'] = False
            answer['remaining_gaps'] = ['Separate original-target review and selected grade acceptance remain pending.']
            pilot.write(problem.folder / 'current-candidate.json', answer)
            observed.append(problem.counter)
            return answer

        fixture = fixtures.PilotIntegrationTests()
        with patch.object(pilot.Problem, 'main_turn', cautious_main):
            fixture.run_scenario(fail_grade=fail_grade)
        self.assertTrue(observed)

    def test_current_proof_pass_schedules_scope_despite_cautious_main(self):
        self.scenario()

    def test_scope_scheduling_does_not_waive_failed_grade(self):
        self.scenario(fail_grade=True)


if __name__ == '__main__':
    unittest.main()
