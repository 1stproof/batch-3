"""Continuation lifecycle integration without model calls."""
import asyncio
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as pilot
import pilot_continuation as continuation
import test_pilot_continuation as fixtures


def expected_legacy_migration_changes():
    # Frozen protocol additions are explicitly disclosed; no unrelated policy changes.
    return {
        'proof_document_version': {'old': None, 'old_field_present': False, 'new': 1},
        'lite_local_verification_version': {'old': None, 'old_field_present': False, 'new': 1},
        'main_response_contract_version': {'old': None, 'old_field_present': False, 'new': 1},
        'parallel_route_scouts': {'old': None, 'old_field_present': False,
                                  'new': {'enabled': False, 'width': 2, 'user_requested': False}},
        'assessment_protocol_epoch': {'old': None, 'old_field_present': False,
                                      'new': 'progress-aware-admission-v1'},
        'campaign_phase': {'old': None, 'old_field_present': False, 'new': 'phase1'},
    }


class ContinuationRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.fixture=fixtures.ContinuationTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        config=json.loads((self.fixture.source/'host-config.json').read_text())
        config.update(codex_binary='synthetic', model_concurrency=1, internet_browse=False,
                      original_scope_review_count=2,
                      source_url='https://example.invalid/original')
        self.fixture.write(self.fixture.source/'host-config.json',config)
        self.root=self.fixture.base/'continued'

    def prepare(self, root=None, **kwargs):
        with patch.object(continuation.os,'kill',side_effect=ProcessLookupError), \
             patch.object(continuation.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')), \
             patch.object(pilot,'subscription_preflight',return_value={}):
            return pilot.prepare_continuation(self.fixture.source, root or self.root,self.fixture.receipt, **kwargs)

    def test_preserves_parent_and_blocks_competing_continuation(self):
        before={str(p):p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()}
        config=self.prepare()
        self.assertIsNone(config['deadline_utc'])
        self.assertFalse(config['internet_browse'])
        self.assertEqual(config['explicit_policy_changes'], expected_legacy_migration_changes())
        self.assertIsNone(json.loads((self.root/'campaign/registry.json').read_text())['deadline_utc'])
        self.assertTrue((self.root/'host/runtime/problem/004-main-repair/stage.meta.json').is_file())
        self.assertEqual(before,{str(p):p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()})
        with self.assertRaises(FileExistsError):
            self.prepare(self.fixture.base/'competing')

    def test_explicit_browsing_change_preserves_parent_and_main(self):
        before = {str(p): p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()}
        config = self.prepare(internet_browse=True)
        self.assertTrue(config['internet_browse'])
        self.assertEqual(config['explicit_policy_changes'], {**expected_legacy_migration_changes(), 'internet_browse': {'old': False, 'new': True}})
        saved = json.loads((self.root/'continuation-checkpoint.json').read_text())
        self.assertEqual(saved['problems']['problem']['main_session'], 'main-session')
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.fixture.source.rglob('*') if p.is_file()})

    def test_preserves_triage_history_for_fresh_reassessment(self):
        progress_path = self.fixture.source / 'campaign/problems/problem/host-progress.json'
        progress = json.loads(progress_path.read_text())
        history = [{'stage': 'legacy-review', 'selected_rows': ['S1'],
                    'reason': 'Retain evidence; fresh selection is required after continuation.'}]
        progress['triage_history'] = history
        self.fixture.write(progress_path, progress)
        self.prepare()
        saved = json.loads((self.root / 'continuation-checkpoint.json').read_text())
        self.assertEqual(saved['problems']['problem']['triage_history'], history)

    def test_resumes_main_and_diagnostics_without_replaying_initial_tasks(self):
        self.prepare()
        async def scenario():
            runner=pilot.Pilot(self.root)
            seen=[]
            async def main(problem,instruction,dossier=False, purpose=None):
                seen.append(instruction)
                self.assertFalse(dossier)
                self.assertEqual(problem.session,'main-session')
                self.assertEqual(problem.counter,4)
                self.assertIn('actual failed compiler diagnostic',instruction)
                self.assertIn('## Phase L3', instruction)
                self.assertIn('supersedes historical allocation instructions', instruction)
                self.assertIn('open core constructions remain research gaps', instruction)
                self.assertIsNone(problem.active_triage)
                self.assertIn('worker-session',problem.implementers)
                raise RuntimeError('synthetic stop after restored dispatch')
            with patch.object(pilot,'subscription_preflight',return_value={}), \
                 patch.object(pilot.Problem,'main_turn',main), \
                 patch.object(pilot.Problem,'execution',side_effect=AssertionError('old execution replayed')):
                result=await runner.run()
            self.assertEqual(len(seen),1)
            self.assertEqual(result[0]['status'],'partial')
            self.assertIsNone(json.loads((self.root/'campaign/problems/problem/host-progress.json').read_text())['remaining_wall_seconds'])
        asyncio.run(scenario())

    def test_main_feedback_compacts_syntax_without_changing_exact_evidence(self):
        self.prepare()
        evidence = {'rows': [{'id': 'R' + str(i), 'value': [True, None, i], 'text': '  α\n\t  '}
                             for i in range(11000)]}
        canonical = pilot.encoded(evidence)
        restore = pilot.Problem.restore_checkpoint
        seen = []
        def restored(problem):
            value = restore(problem)
            value['exact_large_evidence'] = evidence
            return value
        async def capture(problem, instruction, dossier=False, purpose=None):
            payload = instruction.split('LATEST FEEDBACK:\n', 1)[1]
            parsed = json.loads(payload)
            self.assertEqual(parsed['continuation']['exact_large_evidence'], evidence)
            self.assertEqual(payload, pilot.prompt_encoded(parsed))
            self.assertGreater(len(pilot.encoded(parsed)), 1_048_576)
            self.assertLess(len(instruction), 1_048_576)
            self.assertEqual(pilot.encoded(evidence), canonical)
            self.assertEqual(pilot.sha(pilot.encoded(evidence)), pilot.sha(canonical))
            seen.append(payload)
            raise RuntimeError('synthetic stop before model dispatch')
        runner = pilot.Pilot(self.root)
        with patch.object(pilot, 'subscription_preflight', return_value={}), \
             patch.object(pilot.Problem, 'restore_checkpoint', restored), \
             patch.object(pilot.Problem, 'main_turn', capture):
            result = asyncio.run(runner.run())
        self.assertEqual(len(seen), 1)
        self.assertEqual(result[0]['status'], 'partial')

    def test_single_call_timeout_recovers_same_session_without_total_deadline(self):
        self.prepare()
        async def scenario():
            runner=pilot.Pilot(self.root);problem=pilot.Problem(runner,'problem')
            seen=[]
            async def stage(*args,**kwargs):
                seen.append(kwargs.get('resume_override'))
                if len(seen)==1:
                    raise pilot.StageFailure({'name':'problem/009-main-repair','status':'timeout_censored','session_id':'same-session'},[])
                return {'status':'completed'}, {'checkpoint':'preserved'}
            with patch.object(problem,'_call_once',side_effect=stage):
                result=await problem.call('main-repair','Continue saved work',resume=True)
            self.assertEqual(seen,[None,'same-session'])
            self.assertEqual(result[1]['checkpoint'],'preserved')
        asyncio.run(scenario())

    def test_repeated_call_timeouts_require_supervision_instead_of_busy_loop(self):
        self.prepare()
        async def scenario():
            runner=pilot.Pilot(self.root);problem=pilot.Problem(runner,'problem')
            error=pilot.StageFailure({'name':'problem/009-main-repair','status':'timeout_censored','session_id':'same-session'},[])
            with patch.object(problem,'_call_once',side_effect=error) as stage:
                with self.assertRaises(pilot.StageFailure):
                    await problem.call('main-repair','Continue saved work',resume=True)
                self.assertEqual(stage.call_count,2)
            self.assertEqual(problem.errors[-1]['type'],'supervisor_needed')
        asyncio.run(scenario())

if __name__ == '__main__': unittest.main()
