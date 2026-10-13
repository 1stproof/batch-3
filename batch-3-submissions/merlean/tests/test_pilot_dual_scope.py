"""Final original-question conformity requires two blind independent judgments."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p

class AdmittedMock(AsyncMock):
    """Simulate the real transport's concrete admission callback before dispatch."""
    async def _execute_mock_call(self, *args, **kwargs):
        callback = kwargs.get('on_admitted')
        if callback:
            callback()
        return await super()._execute_mock_call(*args, **kwargs)

import test_pilot_review_handoff as fixtures

class DualScopeTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.ReviewHandoffTests(); self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.x = self.f.problem
        self.x.calls = []
        self.x.active_triage = {'candidate_binding': p.triage_binding(self.x.current),
            'review_mode': 'comprehensive', 'selected_rows': [], 'receipt': {'session_id': 'proof'}}
        self.review = {'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [], 'review_mode': 'comprehensive'}

    def run_panel(self, second='PASS_FULL_SCOPE', sessions=None):
        self.prompts = []; sessions = iter(sessions or ['scope1', 'scope2', 'grade'])
        async def call(role, instruction, **kwargs):
            sid = next(sessions)
            self.prompts.append((role, instruction, kwargs))
            verdict = ('PASS_FULL_SCOPE' if len(self.prompts) == 1 else second) if role == 'scope-review' else 'SILVER'
            return self.f.meta(sid), (dict(fixtures.scope_report(verdict, [] if verdict == 'PASS_FULL_SCOPE' else ['Exact dissent']),
                findings={k: 'PRIVATE-' + sid for k in p.SCOPE_FINDING_KEYS}) if role == 'scope-review'
                else {'verdict': verdict, 'gaps': []})
        self.x.call = call
        return asyncio.run(self.x.validate_candidate(self.f.meta('proof'), self.review))

    def test_same_input_blind_pair_both_preserved_with_independent_receipts(self):
        self.f.campaign.status.return_value = {'problems': {'q': {'successful_complete': True}}}
        with patch('original_scope.audit_original_scope', return_value=[]):
            success, feedback = self.run_panel()
        self.assertTrue(success)
        self.assertEqual(self.prompts[0][1], self.prompts[1][1])
        self.assertEqual(self.prompts[0][2]['model'], p.ASTRA)
        self.assertNotIn('PRIVATE-scope1', self.prompts[1][1])
        self.assertIn('PRIVATE-scope1', self.prompts[2][1])
        self.assertIn('PRIVATE-scope2', self.prompts[2][1])
        manifest = json.loads((self.x.folder / 'revision-007-manifest.json').read_text())
        self.assertEqual(manifest['original_scope_review_count'], 2)
        self.assertEqual(len(manifest['original_scope_audits']), 2)
        self.assertEqual(manifest['original_scope_audit'], manifest['original_scope_audits'][0])
        hashes = []
        for ref in manifest['original_scope_audits']:
            self.assertEqual(ref['sha256'], p.sha((self.x.folder / ref['path']).read_bytes()))
            report = json.loads((self.x.folder / ref['path']).read_text())
            hashes.append(report['review_input_sha256'])
            dispatch = json.loads((self.x.folder / report['reviewer_provenance']['path']).read_text())
            self.assertEqual(dispatch['review_input_sha256'], hashes[-1])
        self.assertEqual(hashes[0], hashes[1])
        self.assertEqual([r['session_id'] for r in feedback['host_review_receipts']['scopes']], ['scope1', 'scope2'])

    def test_fail_or_unknown_preserved_and_blocks_even_if_grade_claims_silver(self):
        self.f.campaign.status.return_value = {'problems': {'q': {'successful_complete': True}}}
        for verdict in ('fail', 'unknown'):
            with self.subTest(verdict=verdict):
                success, feedback = self.run_panel(second=verdict)
                self.assertFalse(success)
                self.assertEqual(feedback['scopes'][1]['verdict'], verdict)
                self.assertEqual(feedback['scopes'][1]['gaps'], ['Exact dissent'])
                self.assertEqual(feedback['scopes'][0]['verdict'], 'PASS_FULL_SCOPE')
                manifest = json.loads((self.x.folder / 'revision-007-manifest.json').read_text())
                self.assertEqual(manifest['grade'], 'BRONZE')

    def test_missing_duplicate_and_reused_sessions_never_reach_acceptance(self):
        for sessions in (['scope1', 'scope1', 'grade'], ['proof', 'scope2', 'grade'],
                         ['actual-main', 'scope2', 'grade'], ['scope1', 'actual-sol', 'grade'],
                         ['scope1', 'scope2', 'scope1'], ['', 'scope2', 'grade']):
            with self.subTest(sessions=sessions), self.assertRaisesRegex(ValueError, 'independent'):
                with patch('original_scope.audit_original_scope', return_value=[]):
                    self.run_panel(sessions=sessions)
        self.f.campaign.finish.assert_not_called()

    def test_first_report_saved_if_second_dispatch_interrupted(self):
        first = {'verdict': 'PASS_FULL_SCOPE', 'gaps': []}
        self.x.call = AdmittedMock(side_effect=[(self.f.meta('scope1'), first), RuntimeError('drain checkpoint')])
        with self.assertRaisesRegex(RuntimeError, 'drain checkpoint'):
            asyncio.run(self.x.validate_candidate(self.f.meta('proof'), self.review))
        report = json.loads((self.x.folder / 'revision-007-scope-1.json').read_text())
        self.assertEqual(report['verdict'], 'PASS_FULL_SCOPE')
        self.assertFalse((self.x.folder / 'revision-007-manifest.json').exists())
        self.f.campaign.finish.assert_not_called()

    def test_nonfresh_or_changed_actual_prompt_is_rejected(self):
        for mutation in ({'fresh_session': False}, {'fresh_session': None},
                         {'resume_session': 'scope1'}, {'prompt_sha256': p.sha('different input')}):
            first = self.f.meta('scope1'); second = self.f.meta('scope2') | mutation
            self.x.call = AdmittedMock(side_effect=[(first, {'verdict': 'PASS_FULL_SCOPE', 'gaps': []}),
                                                (second, {'verdict': 'PASS_FULL_SCOPE', 'gaps': []})])
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                asyncio.run(self.x.validate_candidate(self.f.meta('proof'), self.review))
        self.f.campaign.finish.assert_not_called()

    def test_drained_completed_assessment_cannot_repeat_or_become_authority(self):
        x = self.x
        x.status = lambda _: None
        x.ident = 'q'; x.original_bytes = b'original'; x.statement = 'original'
        x.pilot.root = x.folder
        for tail in ('after-proof', 'between-scopes', 'before-silver'):
            history = [{'execution_identity_version':2,'binding_key': p.assessment_key(x.current, []),
                'candidate_sha256': p.sha(p.encoded(x.current)), 'status': 'reviewed', 'attempts': 1,
                'proof_receipt': {'session_id': 'preserved-proof'}, 'tail': tail}]
            saved = {'current': copy.deepcopy(x.current), 'findings': [], 'main_session': 'actual-main',
                'original_sha256': p.sha(b'original'), 'implementers': ['actual-main'], 'calls': [],
                'errors': [{'type': 'CooperativeDrain'}], 'dossier': {}, 'counter': 1,
                'execution_history': [], 'final_assessment_history': history}
            ref = p.write(x.folder / 'continuation-checkpoint.json', {'problems': {'q': saved}})
            x.pilot.config = {'continuation_checkpoint': ref}
            x.restore_checkpoint()
            self.assertIsNone(x.active_triage)
            self.assertFalse(x.final_assessment_history[0].get('retry_after_reconciliation', False))
            x.call = AdmittedMock(side_effect=AssertionError('completed review replay'))
            x.review_candidate = AsyncMock(side_effect=AssertionError('completed review replay'))
            self.assertIsNone(asyncio.run(x.commission_final_assessment({'mathematically_ready': True})))
            self.assertEqual(x.final_assessment_history, history)
            x.call.assert_not_awaited()

    def test_runtime_rejects_single_review_configuration(self):
        p.write(self.x.folder / 'host-config.json', {'original_scope_review_count': 1})
        with self.assertRaisesRegex(ValueError, 'exactly two'):
            p.Pilot(self.x.folder)

    def test_continuation_upgrades_explicit_single_review_with_policy_receipt(self):
        import test_pilot_continuation_runtime as continuation_fixtures
        fixture = continuation_fixtures.ContinuationRuntimeTests()
        fixture.setUp(); self.addCleanup(fixture.doCleanups)
        path = fixture.fixture.source / 'host-config.json'
        config = json.loads(path.read_text()); config['original_scope_review_count'] = 1
        fixture.fixture.write(path, config)
        prepared = fixture.prepare()
        self.assertEqual(prepared['original_scope_review_count'], 2)
        self.assertEqual(prepared['explicit_policy_changes']['original_scope_review_count'], {'old': 1, 'new': 2})
        self.assertEqual(json.loads(path.read_text())['original_scope_review_count'], 1)

    def test_missing_scope_count_migration_receipt_in_config_and_reservation(self):
        import test_pilot_continuation_runtime as continuation_fixtures
        fixture = continuation_fixtures.ContinuationRuntimeTests()
        fixture.setUp(); self.addCleanup(fixture.doCleanups)
        path = fixture.fixture.source / 'host-config.json'
        config = json.loads(path.read_text()); config.pop('original_scope_review_count', None)
        fixture.fixture.write(path, config)
        parent_bytes = path.read_bytes()
        prepared = fixture.prepare()
        expected = {'old': None, 'old_field_present': False, 'new': 2}
        self.assertEqual(prepared['original_scope_review_count'], 2)
        self.assertEqual(prepared['explicit_policy_changes']['original_scope_review_count'], expected)
        reservation = json.loads(Path(prepared['continuation_reservation']).read_text())
        self.assertEqual(reservation['explicit_policy_changes']['original_scope_review_count'], expected)
        self.assertEqual(path.read_bytes(), parent_bytes)
        self.assertNotIn('original_scope_review_count', json.loads(path.read_text()))

    def test_candidate_mutation_between_reviewers_rejected(self):
        async def call(*args, **kwargs):
            self.x.current['proof_markdown'] += ' mutated'
            return self.f.meta('scope1'), {'verdict': 'PASS_FULL_SCOPE', 'gaps': []}
        self.x.call = call
        with self.assertRaisesRegex(ValueError, 'unchanged candidate'):
            asyncio.run(self.x.validate_candidate(self.f.meta('proof'), self.review))
        self.f.campaign.finish.assert_not_called()

if __name__ == '__main__': unittest.main()
