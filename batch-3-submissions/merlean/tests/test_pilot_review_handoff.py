from contextlib import nullcontext
"""Reviewer handoffs carry host metadata without manufacturing semantic approval."""
import asyncio
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot


def scope_report(verdict='PASS_FULL_SCOPE', gaps=None):
    return {'verdict': verdict, 'answer_kind': 'proof', 'coverage': [],
            'extra_assumptions': [], 'gaps': gaps or [],
            'findings': {key: 'Independent substantive assessment: ' + key
                         for key in pilot.SCOPE_FINDING_KEYS}}


class ReviewHandoffTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)
        self.problem = pilot.Problem.__new__(pilot.Problem)
        self.problem.folder = self.folder
        self.problem.session = 'actual-main'
        self.problem.implementers = ['actual-main', 'actual-sol']
        self.problem.counter = 7
        self.problem.ident = 'q'
        self.problem.token = 'SECRET-CLAIM-TOKEN'
        self.problem.errors = []
        self.problem.calls = []
        self.problem.execution_history = []
        self.problem.current = {'proof_markdown': 'Exact answer. Full proof.',
                                'answer_statement': 'Exact answer.', 'ledger': {'rows': []}}
        pilot.write(self.folder / 'original.json', {'statement': 'Exact source',
                    'source': {'path': 'input.txt', 'sha256': pilot.sha('Exact source')}})
        self.campaign = Mock()
        self.campaign.status.return_value = {'problems': {'q': {'successful_complete': False}}}
        self.campaign.feedback.return_value = {'problems': {'q': {'feedback': []}}}
        self.problem.pilot = SimpleNamespace(campaign=self.campaign, remaining=lambda: 0,
                                            policy=lambda path: 'POLICY ' + path)

        self.problem.pilot.drain = SimpleNamespace(check=lambda: None, admission=lambda *args: nullcontext())
        self.problem.pilot.drain_stage_names = set()
        self.problem.pilot.drain_probes = {}

    def meta(self, session):
        return {'status': 'completed', 'session_id': session, 'model_actual': pilot.ASTRA,
                'model_verified': True, 'fresh_session': True, 'resume_session': None,
                'prompt_sha256': pilot.sha('identical actual prompt'), 'answer_sha256': 'raw-answer-hash',
                'request_id': 'request-' + session, 'name': 'q/' + session,
                'claim_token': 'SHOULD-NOT-BE-PUBLIC', 'owner_key': 'SECRET'}

    def test_exact_artifact_and_actor_metadata_precedes_review_no_verdict_rewrite(self):
        prompts = {}
        scope_calls = []
        async def call(role, instruction, **kwargs):
            prompts[role] = instruction
            if role == 'scope-review':
                scope_calls.append(instruction)
            return self.meta(role + str(len(scope_calls)) if role == 'scope-review' else role), (scope_report('unknown', ['Substantive uncertainty']) if role == 'scope-review'
                                     else {'verdict': 'INCOMPLETE', 'gaps': ['Open mathematical issue']})
        self.problem.call = call
        self.problem.active_triage = {'candidate_binding': pilot.triage_binding(self.problem.current),
            'review_mode': 'comprehensive', 'selected_rows': [], 'receipt': {'session_id': 'proof-review'}}
        raw_review = {'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [], 'self_provenance': 'unknown', 'review_mode': 'comprehensive'}
        success, feedback = asyncio.run(self.problem.validate_candidate(self.meta('proof-review'), raw_review))
        self.assertFalse(success)
        self.assertEqual(feedback['scope']['verdict'], 'unknown')
        self.assertEqual(feedback['silver']['status'], 'not_dispatched')
        self.assertEqual(feedback['scope']['gaps'], ['Substantive uncertainty'])
        for role, prompt in prompts.items():
            metadata = json.loads(prompt.split('EXACT FINAL REVIEW INPUTS (lossless supplied-text bindings):\n', 1)[1])['host_metadata']
            self.assertEqual(metadata['manifest_author'], 'actual-main')
            self.assertEqual(metadata['implementers'], ['actual-main', 'actual-sol'])
            for key in ('original_problem', 'target_contract', 'final_answer'):
                ref = metadata['artifact_references'][key]
                self.assertEqual(pilot.sha((self.folder / ref['path']).read_bytes()), ref['sha256'])
                self.assertEqual(metadata[key + '_sha256'], ref['sha256'])
            self.assertEqual(metadata['prior_proof_host_receipt']['model_actual'], pilot.ASTRA)
            self.assertTrue(metadata['prior_proof_host_receipt']['model_verified'])
            self.assertEqual(metadata['prior_proof_dispatch']['reviewer'], 'proof-review')
            self.assertIn('cannot convert fail/unknown into pass', prompt)
            self.assertIn('Do not invent IDs', prompt)
            self.assertNotIn('SECRET', prompt)
            self.assertNotIn('SHOULD-NOT-BE-PUBLIC', prompt)
            self.assertIn('self_provenance', prompt)
        receipts = feedback['host_review_receipts']
        self.assertEqual(receipts['scope']['session_id'], 'scope-review1')
        self.assertEqual(len(receipts['scopes']), 2)
        self.assertEqual(scope_calls[0], scope_calls[1])
        self.assertEqual(receipts['proof']['session_id'], 'proof-review')
        self.assertNotIn('claim_token', json.dumps(receipts))
        manifest = json.loads((self.folder / 'revision-007-manifest.json').read_text())
        self.assertEqual(manifest['grade'], 'BRONZE')

    def test_host_rejects_unverified_wrong_model_or_implementer_provenance(self):
        for changes in ({'model_actual': pilot.SOL}, {'model_verified': False},
                        {'model_verified': None}, {'session_id': 'actual-sol'},
                        {'session_id': 'actual-main'}, {'status': 'process_failed'}):
            with self.subTest(changes=changes):
                meta = self.meta('reviewer') | changes
                with self.assertRaisesRegex(ValueError, 'independent actual Astra'):
                    self.problem.provenance(meta, 'original_scope_review', 'invalid')
        self.assertFalse((self.folder / 'invalid-dispatch.json').exists())

    def test_shared_policy_contents_have_actual_repository_path_labels(self):
        async def run():
            self.problem.pilot.semaphore = asyncio.Semaphore(1)
            self.problem.pilot.remaining = lambda: 600
            self.problem.pilot.config = {'internet_browse': False, 'codex_binary': 'unused'}
            self.problem.pilot.host = self.folder / 'host'
            self.problem.statement = 'Exact original'
            self.problem.status = Mock()
            self.problem.calls = []
            with patch.object(pilot, 'call_stage', new=AsyncMock(return_value=(self.meta('reviewer'), {}))) as dispatch:
                await self.problem._call_once('scope-review', 'Review', model=pilot.ASTRA, resume=False, timeout=300)
                return dispatch.call_args.args[2]
        prompt = asyncio.run(run())
        for path in ('workflows/common.md', 'ports/codex.md', 'docs/trust-and-instantiation-gates.md'):
            self.assertIn('POLICY FILE: ' + path + '\nPOLICY ' + path, prompt)
