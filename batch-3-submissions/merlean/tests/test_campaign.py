import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from campaign import Campaign, digest


class CampaignTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        source = self.base / 'source.txt'
        source.write_text('The immutable original question.')
        self.owner_key = self.base / 'controller.key'
        self.c = Campaign.initialize(self.base / 'run', {'q1': source, 'q2': source},
            deadline_utc=(datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(), concurrency=1, owner_key=self.owner_key)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, value):
        folder = self.c.root / 'problems/q1'
        path = folder / name
        payload = json.dumps(value).encode() if isinstance(value, dict) else value.encode()
        path.write_bytes(payload)
        return {'path': name, 'sha256': digest(payload)}

    def fixture(self):
        answer = self.write('answer.md', 'The complete answer and proof.')
        original = self.write('original.json', {'source': {'path': 'input.txt', 'sha256': digest((self.c.root / 'problems/q1/input.txt').read_bytes())}})
        provenance = self.write('dispatch.json', {'reviewer': 'reviewer', 'role': 'final_proof_review', 'task_id': 'task-2', 'model': 'gpt-6-astra', 'provider': 'codex', 'final_answer_sha256': answer['sha256']})
        review = self.write('proof.json', {'reviewer': 'reviewer', 'implementers': ['worker'], 'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [], 'final_answer_sha256': answer['sha256'], 'reviewer_provenance': provenance})
        manifest = {'provider': 'codex', 'original_problem': original, 'final_answer': answer, 'final_proof_review': review, 'implementers': ['worker'], 'manifest_author': 'main'}
        self.write('manifest.json', manifest)
        return manifest

    def test_claim_survives_restart_and_prevents_duplicate_and_overallocation(self):
        token = self.c.claim('q1', 'host')
        restarted = Campaign(self.c.root, owner_key=self.owner_key)
        for ident in ('q1', 'q2'):
            with self.assertRaises(ValueError):
                restarted.claim(ident, 'host')
        restarted.release('q1', token, interrupted=True)
        with self.assertRaises(ValueError):
            restarted.claim('q2', 'host')
        restarted.reconcile('q1', token, 'Host confirmed process exited.')
        self.assertTrue(restarted.claim('q2', 'host'))

    def test_parallel_claims_admit_only_one_and_stale_token_cannot_release(self):
        from concurrent.futures import ThreadPoolExecutor
        def attempt(ident):
            try:
                return ident, Campaign(self.c.root, owner_key=self.owner_key).claim(ident, 'host')
            except ValueError:
                return ident, None
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(attempt, ['q1', 'q2']))
        admitted = [(ident, token) for ident, token in results if token]
        self.assertEqual(len(admitted), 1)
        ident, token = admitted[0]
        self.c.release(ident, token)
        newer = self.c.claim(ident, 'host')
        with self.assertRaises(ValueError):
            self.c.release(ident, token)
        self.c.release(ident, newer)

    def test_history_retains_each_owner_claim_and_reconciliation(self):
        first = self.c.claim('q1', 'first-host')
        self.c.release('q1', first, interrupted=True)
        self.c.reconcile('q1', first, 'First host confirmed its process exited.')
        second = self.c.claim('q1', 'second-host')
        self.assertNotIn('reconciliation', self.c.status()['problems']['q1'])
        self.c.reconcile('q1', second, 'Second host confirmed its process exited.')
        events = self.c.status()['events']
        claims = [e for e in events if e['action'] == 'claim']
        self.assertEqual([(e['owner'], e['claim_token']) for e in claims],
                         [('first-host', first), ('second-host', second)])
        reconciliations = [e for e in events if e['action'] == 'reconcile_stopped']
        self.assertEqual([e['evidence'] for e in reconciliations],
                         ['First host confirmed its process exited.',
                          'Second host confirmed its process exited.'])
        self.assertEqual([e['claim_token'] for e in reconciliations], [first, second])
        self.assertEqual(events[1]['owner'], 'first-host')
        self.assertEqual(events[1]['claim_token'], first)

    def test_status_does_not_rewrite_state(self):
        path = self.c.root / 'state.json'
        before = path.stat().st_mtime_ns
        self.c.status()
        self.assertEqual(path.stat().st_mtime_ns, before)

    def test_deadline_rejects_claim_but_allows_recording_partial(self):
        from campaign import deadline
        when = self.c.status()['deadline_utc']
        with patch('campaign.now', return_value=deadline(when) + timedelta(seconds=1)):
            with self.assertRaises(ValueError):
                self.c.claim('q1', 'host')
            self.write('partial.md', 'Unresolved work.')
            self.c.finish('q1', partial='partial.md')

    def test_registry_and_source_tamper_fail_closed(self):
        path = self.c.root / 'problems/q1/input.txt'
        path.write_text('Another question')
        with self.assertRaises(ValueError):
            self.c.claim('q1', 'host')

    def test_scope_gate_and_answer_are_required(self):
        self.fixture()
        with patch('campaign.audit_original_scope', return_value=['scope failed']) as gate:
            with self.assertRaises(ValueError):
                self.c.finish('q1', manifest='manifest.json')
            self.assertEqual(gate.call_args.kwargs, {'required': True, 'require_final_answer': True})

    def test_scope_pass_does_not_replace_independent_proof_review(self):
        manifest = self.fixture()
        manifest.pop('final_proof_review')
        self.write('manifest.json', manifest)
        with patch('campaign.audit_original_scope', return_value=[]):
            with self.assertRaises(ValueError):
                self.c.finish('q1', manifest='manifest.json')

    def test_original_input_binding_and_implementer_independence(self):
        manifest = self.fixture()
        manifest['original_problem'] = self.write('other-original.json', {'source': self.write('other.txt', 'Wrong original question.')})
        self.write('manifest.json', manifest)
        with patch('campaign.audit_original_scope', return_value=[]):
            with self.assertRaises(ValueError):
                self.c.finish('q1', manifest='manifest.json')
        manifest = self.fixture()
        manifest['implementers'] = ['reviewer']
        self.write('manifest.json', manifest)
        with patch('campaign.audit_original_scope', return_value=[]):
            with self.assertRaises(ValueError):
                self.c.finish('q1', manifest='manifest.json')

    def test_sealing_rechecks_current_evidence_and_keeps_partial_distinct(self):
        manifest = self.fixture()
        observed = {'answer': manifest['final_answer'], 'silver': {'status': 'review_recorded'},
                    'gold': {'status': 'not_applicable'}, 'paper': {'status': 'pending'}}
        with patch('campaign.audit_original_scope', return_value=[]), \
                patch('campaign_evidence.assess_evidence', return_value=observed):
            self.c.finish('q1', manifest='manifest.json')
            (self.c.root / 'problems/q2/partial.md').write_text('Unsolved')
            self.c.finish('q2', partial='partial.md')
            self.c.seal()
            state = self.c.status()
            self.assertTrue(state['sealed'])
            self.assertEqual(state['problems']['q2']['status'], 'partial')
            self.write('answer.md', 'Changed after review.')
            with self.assertRaises(ValueError):
                self.c.seal()

    def test_unknown_running_cannot_be_finished_or_reclaimed(self):
        self.c.claim('q1', 'host')
        self.write('partial.md', 'Partial')
        with self.assertRaises(ValueError):
            self.c.finish('q1', partial='partial.md')
        with self.assertRaises(ValueError):
            self.c.seal()


if __name__ == '__main__':
    unittest.main()
