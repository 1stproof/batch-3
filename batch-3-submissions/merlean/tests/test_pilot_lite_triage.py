from contextlib import nullcontext
"""Behavioral checks for independent Lite selection, execution and grade boundaries."""
import asyncio
import copy
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, Mock
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot


class LiteTriageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.p = pilot.Problem.__new__(pilot.Problem)
        self.p.folder = Path(self.temp.name)
        self.p.current = {'proof_markdown': 'A complete mathematical inference.', 'ledger': {'rows': [
            {'id': 'S1', 'claim': 'claim', 'uses': [], 'class': 'NOVEL', 'triaged': False}]}}
        self.p.active_triage = None
        self.p.triage_history = []
        self.p.findings = []
        self.p.dossier = {'original': 'Exact original'}
        self.p.execution_history = []
        self.p.counter = 1
        self.p.status = Mock()
        self.p.pilot = SimpleNamespace(config={'lean_executable': '/unusable'}, policy=lambda _: 'FULL L3')
        self.p.calls = []
        self.p.review_receipt = lambda meta: dict(meta)

        self.p.pilot.drain = SimpleNamespace(check=lambda: None, admission=lambda *args: nullcontext())
        self.p.pilot.drain_stage_names = set()
        self.p.pilot.drain_probes = {}
        self.p.ident = 'test'

    def review(self, selected=True):
        return {'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [], 'unresolved_findings': [], 'resolved_ids': [],
                'triaged_rows': ['S1'] if selected else [], 'triage_decisions': [{'row_id': 'S1',
                'selected': selected, 'trigger': 'theorem_crux' if selected else 'none',
                'reason': 'Independent inference analysis', 'goal_relevance': 'Direct goal consumer',
                'inference_ready': True}]}

    def authorize(self):
        self.p.active_triage = {'candidate_binding': pilot.triage_binding(self.p.current),
            'selected_rows': ['S1'], 'review_mode': 'focused', 'receipt': {'session_id': 'fresh'}}

    def test_main_label_never_authorizes_and_stale_math_revokes(self):
        self.p.current['ledger']['rows'][0]['triaged'] = True
        self.assertFalse(self.p.lean_authorized(['S1']))
        self.authorize()
        self.assertTrue(self.p.lean_authorized(['S1']))
        self.p.current['ledger']['rows'][0]['claim'] = 'Changed statement'
        self.assertFalse(self.p.lean_authorized(['S1']))

    def test_historical_extra_rows_report_exact_current_scope(self):
        review = self.review(False)
        review['triage_decisions'].append(dict(review['triage_decisions'][0], row_id='old-row'))
        with self.assertRaisesRegex(ValueError, 'expected CURRENT candidate IDs=') as error:
            pilot.checked_triage(self.p.current, review, [])
        self.assertIn('["S1"]', str(error.exception))
        self.assertIn('["S1", "old-row"]', str(error.exception))
        self.assertIn('Historical-only rows', str(error.exception))

    def test_probe_without_selection_or_wrong_rows_never_launches(self):
        for rows in (['S1'], ['unknown'], []):
            result = asyncio.run(self.p.probe({'lean_probe': 'theorem x : True := by trivial',
                                              'lean_probe_rows': rows}, 'not-launched'))
            self.assertEqual(result['lean']['status'], 'deferred')
        self.assertFalse((self.p.folder / 'probes').exists())
        self.authorize()
        result = asyncio.run(self.p.probe({'lean_probe': 'code', 'lean_probe_rows': ['S1']},
                                         'worker', allowed_rows=[]))
        self.assertEqual(result['lean']['status'], 'deferred')

    def test_formal_worker_deferred_but_research_worker_can_run(self):
        task = {k: 'bounded' for k in ('task', 'context', 'hypotheses', 'advisory_hints',
                                      'owned_scope', 'acceptance_checks')}
        self.p.current['sol_tasks'] = [dict(task, kind='lean', row_ids=['S1'])]
        self.p.call = AsyncMock(return_value=({'session_id': 'worker'}, {'findings': 'experiment'}))
        result = asyncio.run(self.p.execution())
        self.p.call.assert_not_awaited()
        self.assertEqual(result['workers'][0]['output']['status'], 'deferred')
        self.p.current['sol_tasks'] = [dict(task, kind='research')]
        asyncio.run(self.p.execution())
        self.p.call.assert_not_awaited()  # A research label cannot bypass independent approval.
        self.authorize()
        self.p.active_triage['review_mode'] = 'assumptions'
        self.p.active_triage['selected_rows'] = []  # L0 never authorizes Lean.
        self.p.active_triage['approved_research_task_hashes'] = self.p.approved_task_hashes(
            {'approved_research_tasks': [0]})
        asyncio.run(self.p.execution())
        self.p.call.assert_awaited_once()

    def test_reassessment_preserves_findings_and_audit_history(self):
        self.authorize()
        prior = self.review()['triage_decisions']
        self.p.triage_history = [{'decisions': prior}]
        review = self.review(False)
        with self.assertRaisesRegex(ValueError, 'reassessment'):
            pilot.checked_triage(self.p.current, review, prior)
        review['triage_decisions'][0]['reassessment_reason'] = 'Routine application; not a crux'
        self.p.findings = [{'id': 'gap', 'severity': 'gap', 'finding': 'Missing construction',
                            'what_would_resolve': 'Construct intended object'}]
        self.p.call = AsyncMock(return_value=({'session_id': 'fresh'}, review))
        _, effective = asyncio.run(self.p.review_candidate('focused'))
        self.assertEqual(effective['unresolved_findings'][0]['id'], 'gap')
        self.assertEqual(self.p.active_triage['selected_rows'], [])
        self.assertFalse(self.p.lean_authorized(['S1']))
        self.assertEqual(len(self.p.triage_history), 2)
        self.assertTrue(self.p.triage_history[0]['decisions'][0]['selected'])

    def test_no_hard_three_row_cap_and_no_recursive_cited_selection(self):
        review = self.review()
        self.p.current['ledger']['rows'] *= 0
        review['triage_decisions'] = []
        review['triaged_rows'] = []
        for n in range(5):
            ident = str(n)
            self.p.current['ledger']['rows'].append({'id': ident, 'class': 'NOVEL'})
            review['triage_decisions'].append(dict(self.review()['triage_decisions'][0], row_id=ident))
            review['triaged_rows'].append(ident)
        self.assertEqual(len(pilot.checked_triage(self.p.current, review, [])), 5)
        self.p.current['ledger']['rows'][0]['class'] = 'CITED'
        with self.assertRaisesRegex(ValueError, 'L3 trigger'):
            pilot.checked_triage(self.p.current, review, [])

    def test_focused_or_stale_review_cannot_reach_grade_dispatch(self):
        self.authorize()
        self.p.call = AsyncMock()
        review = dict(self.review(), review_mode='focused')
        with self.assertRaisesRegex(ValueError, 'comprehensive'):
            asyncio.run(self.p.validate_candidate({'session_id': 'fresh'}, review))
        review['review_mode'] = 'comprehensive'
        self.p.active_triage['review_mode'] = 'comprehensive'
        self.p.current['proof_markdown'] += ' Revised.'
        with self.assertRaisesRegex(ValueError, 'comprehensive'):
            asyncio.run(self.p.validate_candidate({'session_id': 'fresh'}, review))
        self.p.call.assert_not_awaited()
        self.assertEqual(list(self.p.folder.iterdir()), [])

    def test_missing_core_is_research_gap_not_certificate(self):
        review = self.review()
        review['triage_decisions'][0]['inference_ready'] = False
        with self.assertRaisesRegex(ValueError, 'research gap'):
            pilot.checked_triage(self.p.current, review, [])
        review = self.review(False)
        review['triage_decisions'][0]['trigger'] = 'research_gap'
        self.p.call = AsyncMock(return_value=({'session_id': 'fresh'}, review))
        with self.assertRaisesRegex(ValueError, 'research gap'):
            asyncio.run(self.p.review_candidate('focused'))

    def test_evidence_and_premise_changes_revoke_authorization(self):
        for field in ('evidence', 'premise_manifest_data', 'intended_interface'):
            self.authorize()
            self.p.current['ledger']['rows'][0][field] = 'Changed evidence'
            self.assertFalse(self.p.lean_authorized(['S1']))

    def test_partial_milestone_executes_while_broader_research_gap_blocks_grade(self):
        review = self.review()
        review['verdict'] = 'INCOMPLETE'
        review['gaps'] = ['Original question still open beyond local milestone']
        review['unresolved_findings'] = [{'id': 'broader', 'step': 'S2', 'severity': 'gap',
            'finding': 'Broader construction missing', 'what_would_resolve': 'Construct it'}]
        self.p.call = AsyncMock(return_value=({'session_id': 'fresh'}, review))
        _, effective = asyncio.run(self.p.review_candidate('focused'))
        self.assertTrue(self.p.lean_authorized(['S1']))
        self.assertFalse(pilot.proof_pass(effective))
        with self.assertRaisesRegex(ValueError, 'comprehensive'):
            asyncio.run(self.p.validate_candidate({'session_id': 'fresh'}, effective))

    def test_deferred_retry_does_not_replay_completed_research_or_python(self):
        task = {k: 'bounded' for k in ('task', 'context', 'hypotheses', 'advisory_hints',
                                      'owned_scope', 'acceptance_checks')}
        research, lean = dict(task, kind='research'), dict(task, kind='lean', row_ids=['S1'])
        self.p.current.update(sol_tasks=[research, lean], python_probe='already executed',
                              lean_probe='selected code', lean_probe_rows=['S1'])
        self.authorize()
        self.p.active_triage['approved_lean_task_hashes'] = [pilot.sha(pilot.encoded(lean))]
        self.p.call = AsyncMock(return_value=({'session_id': 'worker'}, {}))
        self.p.probe = AsyncMock(return_value={'status': 'not_requested'})
        prior = {'workers': [{'task': research, 'output': {'findings': 'done'}},
                             {'task': lean, 'output': {'status': 'deferred'}}],
                 'main_probe': {'python': {'status': 'completed'}, 'lean': {'status': 'deferred'}}}
        asyncio.run(self.p.execution(deferred_from=prior))
        self.p.call.assert_awaited_once()
        self.assertNotIn('python_probe', self.p.probe.call_args.args[0])
        self.assertEqual(self.p.probe.call_args.args[0]['lean_probe'], 'selected code')

    def test_unselected_missing_inference_cannot_hide_behind_none_trigger(self):
        review = self.review(False)
        review['triage_decisions'][0]['inference_ready'] = False
        self.p.call = AsyncMock(return_value=({'session_id': 'fresh'}, review))
        with self.assertRaisesRegex(ValueError, 'research gap'):
            asyncio.run(self.p.review_candidate('focused'))

    def test_selected_row_does_not_authorize_unreviewed_or_changed_worker_scope(self):
        task = {k: 'bounded' for k in ('task', 'context', 'hypotheses', 'advisory_hints',
                                      'owned_scope', 'acceptance_checks')}
        lean = dict(task, kind='lean', row_ids=['S1'])
        self.p.current['sol_tasks'] = [lean]
        self.authorize()
        self.p.call = AsyncMock(return_value=({'session_id': 'worker'}, {}))
        asyncio.run(self.p.execution())
        self.p.call.assert_not_awaited()
        self.p.active_triage['approved_lean_task_hashes'] = [pilot.sha(pilot.encoded(lean))]
        lean['task'] = 'Formalize every premise and unrelated infrastructure'
        asyncio.run(self.p.execution())
        self.p.call.assert_not_awaited()

    def test_completed_certificates_do_not_silently_authorize_new_lean(self):
        # Reproduce the six-row completed-certificate/trigger:none failure without
        # importing any private research artifacts into the release fixture.
        self.p.current['ledger']['rows'] = [
            {'id': f'S{i}', 'class': 'NOVEL', 'triaged': True,
             'certificate': {'path': f'certificate-{i}.lean', 'sha256': str(i)},
             'evidence': 'Completed host certificate; no new execution requested'}
            for i in range(6)]
        invalid = self.review()
        invalid['triaged_rows'] = [r['id'] for r in self.p.current['ledger']['rows']]
        invalid['triage_decisions'] = [dict(self.review()['triage_decisions'][0],
            row_id=r['id'], trigger='none') for r in self.p.current['ledger']['rows']]
        self.p.triage_history = [{'decisions': copy.deepcopy(invalid['triage_decisions'])}]
        corrected = copy.deepcopy(invalid)
        corrected['triaged_rows'] = []
        for d in corrected['triage_decisions']:
            d.update(selected=False, reassessment_reason='Completed evidence retained; no current L3 selection justified')
        before = copy.deepcopy(self.p.current)
        self.p.session = 'main'
        self.p.implementers = ['main']
        def receipt(session):
            return {'session_id': session, 'name': 'q/' + session, 'status': 'completed',
                    'model_actual': pilot.ASTRA, 'model_verified': True}
        self.p.call = AsyncMock(side_effect=[(receipt('invalid'), invalid),
                                             (receipt('fresh'), corrected)])
        _, review = asyncio.run(self.p.review_candidate('comprehensive'))
        self.assertEqual(self.p.call.await_count, 2)
        first, second = [c.args[1] for c in self.p.call.call_args_list]
        header = first.split('\nEXACT REVIEW INPUTS (lossless supplied-text bindings):\n', 1)[0]
        self.assertTrue(second.startswith(header))
        self.assertIn('INVALID, is NOT authority', second)
        self.assertIn('Lean selection needs an L3 trigger', second)
        self.assertIn(pilot.REVIEW_FIELDS, second)
        self.assertEqual(self.p.current, before)
        self.assertEqual(len(self.p.triage_history), 2)
        self.assertEqual(review['triaged_rows'], [])
        self.assertFalse(self.p.lean_authorized(['S0']))
        self.assertEqual(self.p.active_triage['receipt']['session_id'], 'fresh')
        self.assertEqual(len(list(self.p.folder.glob('*-invalid-*.json'))), 1)

    def test_repeated_invalid_approval_never_publishes_partial_authority(self):
        self.p.findings = [{'id': 'old', 'severity': 'gap', 'finding': 'Still open',
                            'what_would_resolve': 'Actual independent resolution'}]
        before_findings = copy.deepcopy(self.p.findings)
        invalid = self.review()
        invalid.update(resolved_ids=['old'], approved_lean_tasks=[0])
        self.p.call = AsyncMock(return_value=({'session_id': 'invalid'}, invalid))
        with self.assertRaisesRegex(ValueError, 'invalid independent lean task approval'):
            asyncio.run(self.p.review_candidate('focused'))
        self.assertEqual(self.p.call.await_count, 2)
        self.assertEqual(self.p.findings, before_findings)
        self.assertEqual(self.p.triage_history, [])
        self.assertIsNone(self.p.active_triage)
        self.assertFalse(self.p.lean_authorized(['S1']))
        self.assertEqual(len(list(self.p.folder.glob('*-invalid-*.json'))), 2)
        self.assertEqual(list(self.p.folder.glob('*-effective.json')), [])

    def test_nonobject_review_gets_one_protocol_retry(self):
        self.p.call = AsyncMock(side_effect=[({'session_id': 'invalid'}, []),
            ({'session_id': 'fresh'}, self.review(False))])
        asyncio.run(self.p.review_candidate('focused'))
        self.assertEqual(self.p.call.await_count, 2)
        self.assertEqual(self.p.active_triage['selected_rows'], [])

    def test_transport_failure_is_not_protocol_retry(self):
        for error in (TimeoutError('deadline'), ValueError('predispatch_prompt_too_large')):
            with self.subTest(error=type(error).__name__):
                self.p.call = AsyncMock(side_effect=error)
                with self.assertRaises(type(error)):
                    asyncio.run(self.p.review_candidate('focused'))
                self.p.call.assert_awaited_once()
                self.assertIsNone(self.p.active_triage)
