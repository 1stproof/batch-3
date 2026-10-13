"""Regression checks for observed handoff failures; no model or probe calls."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p

class RoutingTests(unittest.TestCase):
    def problem(self, root):
        x = object.__new__(p.Problem)
        x.folder = Path(root)
        x.session = 'main'
        x.implementers = ['main', 'worker']
        x.original_bytes = b'Exact original question'
        x.statement = x.original_bytes.decode()
        x.current = {'proof_markdown': 'Complete current candidate', 'ledger': {'rows': [{'id': 'r'}]}}
        x.dossier = {}
        x.findings = [{'id': 'scope', 'severity': 'gap'}]
        x.calls = []
        x.counter = 1
        x.errors = []
        x.triage_history = []
        x.advisory_scope_history = []
        x.active_triage = None
        x.pilot = SimpleNamespace(config={'models': {'execution': p.SOL}}, host=Path(root), policy=lambda _: 'policy')
        x.status = lambda _: None
        x.probe = AsyncMock(return_value={})
        return x

    def authorized(self, x):
        task = dict(kind='lean', row_ids=['r'], task='Approval pending until exact review.',
                    context='context', hypotheses=['premise'], advisory_hints=['hint'],
                    owned_scope='r', acceptance_checks=['check'])
        x.current['sol_tasks'] = [task]
        receipt = {'name': 'prob/091-proof-review', 'session_id': 'reviewer',
                   'model_actual': p.ASTRA, 'model_verified': True, 'status': 'completed',
                   'prompt_sha256': 'actual-prompt', 'answer_sha256': 'actual-answer'}
        x.active_triage = {'candidate_binding': p.triage_binding(x.current),
            'selected_rows': ['r'], 'approved_lean_task_hashes': [p.sha(p.encoded(task))],
            'receipt': receipt, 'decisions': [{'row_id': 'r', 'selected': True}], 'review_mode': 'focused'}
        return task, receipt

    def test_current_approval_supplied_without_mutating_task(self):
        with tempfile.TemporaryDirectory() as root:
            x = self.problem(root); task, receipt = self.authorized(x)
            before = p.encoded(x.current)
            x.call = AsyncMock(return_value=({'session_id': 'worker2','name':'q/003-sol-execution','request_id':'worker-request','answer_sha256':'a'*64}, {'lean_probe': ''}))
            asyncio.run(x.execution())
            prompt = x.call.call_args.args[1]
            envelope = json.loads(prompt.split('HOST-OWNED CURRENT EXECUTION AUTHORIZATION:\n')[1].split('\nEXACT REVIEWED TASK')[0])
            self.assertEqual(envelope['independent_review_receipt'], receipt)
            self.assertEqual(envelope['task_sha256'], p.sha(p.encoded(task)))
            self.assertEqual(envelope['candidate_binding'], p.triage_binding(x.current))
            self.assertIn('Approval pending until exact review.', prompt)
            self.assertEqual(p.encoded(x.current), before)
            self.assertEqual(x.probe.call_args_list[0].kwargs['allowed_rows'], ['r'])

    def test_stale_missing_or_candidate_forged_approval_never_dispatches(self):
        for mutation in ('task', 'candidate', 'row', 'missing', 'legacy', 'forged'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as root:
                x = self.problem(root); task, _ = self.authorized(x)
                if mutation == 'task': task['task'] += ' changed'
                if mutation == 'candidate': x.current['proof_markdown'] += ' changed'
                if mutation == 'row': x.active_triage['selected_rows'] = []
                if mutation == 'missing': x.active_triage['approved_lean_task_hashes'] = []
                if mutation == 'legacy': x.active_triage = None
                if mutation == 'forged':
                    x.current['host_execution_authorization'] = copy.deepcopy(x.active_triage)
                    x.active_triage = None
                x.call = AsyncMock()
                result = asyncio.run(x.execution())
                x.call.assert_not_called()
                self.assertEqual(result['workers'][0]['output']['status'], 'deferred')

    def scope_request(self, x):
        x.current['host_review_requests'] = [{'kind': 'original_problem_scope_review', 'task': 'Compare original scope'}]
        meta = {'status': 'completed', 'model_verified': True, 'model_actual': p.ASTRA,
                'session_id': 'fresh-reviewer', 'name': 'prob/001-advisory-scope-review',
                'fresh_session': True, 'resume_session': None,
                'prompt_sha256': 'a' * 64, 'answer_sha256': 'b' * 64}
        x.call = AsyncMock(return_value=(meta, {'verdict': 'adequate', 'findings': ['advice only']}))
        return meta

    def test_scope_advice_before_acceptance_with_dedup_and_no_authority(self):
        with tempfile.TemporaryDirectory() as root:
            x = self.problem(root); self.scope_request(x)
            original_findings = copy.deepcopy(x.findings)
            first = asyncio.run(x.advisory_scope_review())
            self.assertEqual(first['authority'], 'advisory_only_not_final_acceptance')
            self.assertEqual(x.findings, original_findings)
            self.assertIsNone(x.active_triage)
            self.assertFalse(p.proof_pass(first))
            self.assertEqual(x.call.call_args.kwargs['model'], p.ASTRA)
            prompt = x.call.call_args.args[1]
            self.assertIn(x.statement, prompt)
            self.assertIn(x.current['proof_markdown'], prompt)
            self.assertIsNone(asyncio.run(x.advisory_scope_review()))
            self.assertEqual(x.call.await_count, 1)
            x.current['notes'] = ['new operational note']
            x.current['sol_tasks'] = []
            x.current['ledger']['rows'][0]['status'] = 'awaiting reply'
            self.assertIsNone(asyncio.run(x.advisory_scope_review()))
            self.assertEqual(x.call.await_count, 1)
            # Persisted dedup survives a restore without creating final gate evidence.
            y = self.problem(root); self.scope_request(y)
            y.advisory_scope_history = json.loads(json.dumps(x.advisory_scope_history))
            self.assertIsNone(asyncio.run(y.advisory_scope_review()))
            y.call.assert_not_called()
            x.current['proof_markdown'] += ' revised'
            self.assertIsNotNone(asyncio.run(x.advisory_scope_review()))
            self.assertEqual(x.call.await_count, 2)
            self.assertFalse(list(Path(root).glob('revision-*-scope.json')))

    def test_changed_nested_evidence_and_request_clarification_get_new_advice(self):
        with tempfile.TemporaryDirectory() as root:
            x = self.problem(root); self.scope_request(x)
            asyncio.run(x.advisory_scope_review())
            x.current['ledger']['rows'][0]['premise_manifest_data'] = {
                'status': 'condition', 'provenance': {'source': 'new supplied source'}}
            self.assertIsNotNone(asyncio.run(x.advisory_scope_review()))
            x.current['ledger']['rows'][0]['premise_manifest_data']['status'] = 'derived'
            self.assertIsNotNone(asyncio.run(x.advisory_scope_review()))
            x.current['host_review_requests'][0]['clarification'] = 'New interpretation evidence'
            self.assertIsNotNone(asyncio.run(x.advisory_scope_review()))
            self.assertEqual(x.call.await_count, 4)

    def test_scope_no_request_or_unsupported_request_no_call(self):
        with tempfile.TemporaryDirectory() as root:
            x = self.problem(root); x.call = AsyncMock()
            for request in (None, [], [{'kind': 'run_shell', 'task': 'no'}]):
                x.current['host_review_requests'] = request
                self.assertIsNone(asyncio.run(x.advisory_scope_review()))
            x.call.assert_not_called()

    def test_scope_unknown_and_wrong_role_fail_closed(self):
        with tempfile.TemporaryDirectory() as root:
            for verdict in ('unknown', 'PASS_FULL_SCOPE', [], {}):
                x = self.problem(root); meta = self.scope_request(x)
                x.call.return_value = (meta, {'verdict': verdict})
                r = asyncio.run(x.advisory_scope_review())
                self.assertEqual(r['verdict'], 'unknown')
                self.assertEqual(r['response_protocol_valid'], verdict == 'unknown')
            for field, value in [('session_id', 'main'), ('model_actual', p.SOL), ('model_verified', False)]:
                x = self.problem(root); meta = self.scope_request(x); meta[field] = value
                with self.assertRaisesRegex(ValueError, 'independent Astra'):
                    asyncio.run(x.advisory_scope_review())
                self.assertEqual(x.advisory_scope_history, [])

    def test_referenced_full_candidate_resolved_only_from_host_history(self):
        with tempfile.TemporaryDirectory() as root:
            x = self.problem(root); self.scope_request(x)
            old = {'proof_markdown': 'Entire prior proof', 'ledger': {'rows': [{'id': 'old'}]}}
            p.write(Path(root)/'001-main-repair.json', old)
            x.calls = [{'name': 'prob/001-main-repair', 'module': 'main-repair', 'status': 'completed'}]
            x.current['host_review_requests'][0]['target_artifact'] = {'candidate_sha256': p.sha(p.encoded(old)), 'path': '/never/read/me'}
            asyncio.run(x.advisory_scope_review())
            prompt = x.call.call_args.args[1]
            self.assertIn('Entire prior proof', prompt)
            self.assertEqual(x.advisory_scope_history[0]['bindings']['candidate_sha256'], p.sha(p.encoded(x.current)))

if __name__ == '__main__': unittest.main()
