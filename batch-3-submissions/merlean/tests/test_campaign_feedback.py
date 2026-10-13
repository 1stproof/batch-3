"""Durable return paths retain failures without treating delivery as acceptance."""
from datetime import timedelta
from unittest.mock import patch
import unittest

from test_campaign import CampaignTests
from campaign import Campaign, deadline


class CampaignFeedbackTests(unittest.TestCase):
    setUp = CampaignTests.setUp
    tearDown = CampaignTests.tearDown
    write = CampaignTests.write
    fixture = CampaignTests.fixture

    def tickets(self, gate=None):
        values = self.c.feedback('q1')['problems']['q1']['feedback']
        return [t for t in values if gate is None or t['gate'] == gate]

    def result(self, manifest, silver='review_recorded'):
        return {'answer': manifest['final_answer'], 'silver': {'status': silver},
                'gold': {'status': 'not_applicable'}, 'paper': {'status': 'pending'}}

    def test_failed_finish_repair_and_current_acceptance_resolves(self):
        manifest = self.fixture()
        frozen = (self.c.root / 'registry.json').read_bytes()
        with patch('campaign.audit_original_scope', return_value=['scope clause missing']):
            with self.assertRaisesRegex(ValueError, 'scope clause missing'):
                self.c.finish('q1', manifest='manifest.json')
        ticket = self.tickets('submission')[0]
        self.assertEqual(ticket['artifacts']['candidate']['path'], 'manifest.json')
        self.assertEqual(ticket['errors'], ['scope clause missing'])
        self.assertEqual(ticket['recipient'], 'problem_main')
        self.c.acknowledge('q1', ticket['id'], task_id='main-task', receipt='Host delivered exact packet',
                           fingerprint=ticket['fingerprint'])
        self.assertEqual(self.tickets('submission')[0]['status'], 'open')
        self.c.reopen('q1', reason='Resume exact candidate with the scope finding')
        token = self.c.claim('q1', 'same-main')
        self.c.release('q1', token)
        with patch('campaign.audit_original_scope', return_value=[]), patch(
                'campaign_evidence.assess_evidence', return_value=self.result(manifest)):
            self.c.finish('q1', manifest='manifest.json')
            self.assertTrue(self.c.status()['problems']['q1']['successful_complete'])
        self.assertEqual(self.tickets('submission')[0]['status'], 'resolved')
        self.assertEqual((self.c.root / 'registry.json').read_bytes(), frozen)
        self.assertEqual(self.c.feedback('q1')['problems']['q1']['repair_round'], 1)

    def test_regression_dedup_version_ack_and_revalidation(self):
        manifest = self.fixture()
        result = self.result(manifest)
        with patch('campaign.audit_original_scope', return_value=[]), patch(
                'campaign_evidence.assess_evidence', return_value=result):
            self.c.finish('q1', manifest='manifest.json')
            result['silver'] = {'status': 'failed', 'details': ['First gap']}
            self.c.refresh()
            ticket = self.tickets('silver')[0]
            self.c.acknowledge('q1', ticket['id'], task_id='main-task', receipt='Delivered first gap',
                               fingerprint=ticket['fingerprint'])
            self.c.refresh()
            self.assertEqual(len(self.tickets('silver')), 1)
            self.assertFalse(self.tickets('silver')[0]['needs_delivery'])
            result['silver']['details'] = ['Second gap']
            self.c.refresh()
            current = self.tickets('silver')[0]
            self.assertTrue(current['needs_delivery'])
            self.assertEqual(len(current['history']), 1)
            with self.assertRaisesRegex(ValueError, 'feedback changed'):
                self.c.acknowledge('q1', ticket['id'], task_id='main-task', receipt='Old packet',
                                   fingerprint=ticket['fingerprint'])
            result['silver'] = {'status': 'review_recorded'}
            self.c.refresh()
            self.assertEqual(self.tickets('silver')[0]['status'], 'resolved')
            result['silver'] = {'status': 'pending'}
            self.c.refresh()
            self.assertEqual(len(self.tickets('silver')), 2)
            self.assertEqual(self.tickets('silver')[1]['status'], 'open')

    def test_unrelated_answer_does_not_resolve_grade_ticket(self):
        manifest = self.fixture()
        result = self.result(manifest, 'failed')
        with patch('campaign.audit_original_scope', return_value=[]), patch(
                'campaign_evidence.assess_evidence', return_value=result):
            self.c.finish('q1', manifest='manifest.json')
            other = dict(manifest, final_answer=self.write('other.md', 'Different result'))
            self.write('other.json', other)
            result.update(self.result(other))
            self.c.observe('q1', manifest='other.json')
            self.assertEqual(self.tickets('silver')[0]['status'], 'open')
            self.assertEqual(self.tickets('answer_binding')[0]['status'], 'open')

    def test_missing_and_malformed_submission_persist_exact_attempt(self):
        self.fixture()
        with patch('campaign.audit_original_scope', return_value=['scope failure']):
            with self.assertRaises(ValueError):
                self.c.finish('q1', manifest='manifest.json')
        with self.assertRaises(ValueError):
            self.c.finish('q1', manifest='missing.json')
        self.assertEqual(self.tickets('submission')[0]['artifacts']['candidate'],
                         {'path': 'missing.json', 'sha256': None})
        manifest = self.fixture()
        manifest['final_proof_review'] = self.write('proof-list.json', '[]')
        self.write('manifest.json', manifest)
        with patch('campaign.audit_original_scope', return_value=[]):
            with self.assertRaises(ValueError):
                self.c.finish('q1', manifest='manifest.json')
        self.assertIn('get', self.tickets('submission')[0]['errors'][0])

    def test_reopen_restrictions_and_infrastructure_reconciliation(self):
        with self.assertRaises(ValueError):
            self.c.reopen('q1', reason='No submitted candidate')
        token = self.c.claim('q1', 'main')
        with self.assertRaises(ValueError):
            self.c.reopen('q1', reason='Still running')
        self.c.release('q1', token, interrupted=True)
        ticket = self.tickets('infrastructure')[0]
        self.assertEqual(ticket['recipient'], 'host')
        self.c.acknowledge('q1', ticket['id'], task_id='host-task', receipt='Host investigating',
                           fingerprint=ticket['fingerprint'])
        with self.assertRaises(ValueError):
            self.c.reopen('q1', reason='Uncertain process')
        self.assertEqual(self.tickets('infrastructure')[0]['status'], 'open')
        self.c.reconcile('q1', token, 'Host confirmed the process has exited.')
        self.assertEqual(self.tickets('infrastructure')[0]['status'], 'resolved')
        self.write('partial.md', 'Unresolved')
        self.c.finish('q1', partial='partial.md')
        with patch('campaign.now', return_value=deadline(self.c.status()['deadline_utc']) + timedelta(seconds=1)):
            with self.assertRaisesRegex(ValueError, 'deadline'):
                self.c.reopen('q1', reason='Expired repair')

    def test_seal_blocks_missing_gate_and_persists_feedback(self):
        self.fixture()
        with patch('campaign.audit_original_scope', return_value=[]):
            self.c.finish('q1', manifest='manifest.json')
            (self.c.root / 'problems/q2/partial.md').write_text('Partial')
            self.c.finish('q2', partial='partial.md')
            with self.assertRaisesRegex(ValueError, 'configured completion gates'):
                self.c.seal()
            self.assertFalse(self.c.status()['sealed'])
        self.assertEqual(self.tickets('silver')[0]['status'], 'open')
        self.c.reopen('q1', reason='Retain honestly partial outcome')
        self.write('partial.md', 'Partial')
        self.c.finish('q1', partial='partial.md')
        self.c.seal()
        self.assertFalse(self.c.status()['successful_complete'])
        with self.assertRaisesRegex(ValueError, 'sealed'):
            self.c.reopen('q1', reason='Already sealed')

    def test_status_is_read_only_owner_required_and_partial_recovery(self):
        for ident in ('q1', 'q2'):
            (self.c.root / 'problems' / ident / 'partial.md').write_text('Partial')
            self.c.finish(ident, partial='partial.md')
        self.write('partial.md', 'Changed')
        with self.assertRaises(ValueError):
            self.c.seal()
        self.write('partial.md', 'Partial')
        reader = Campaign(self.c.root)
        before = (self.c.root / 'state.json').read_bytes()
        reader.status()
        packet = reader.feedback('q1')
        self.assertFalse(packet['delivery_automatic'])
        self.assertEqual(before, (self.c.root / 'state.json').read_bytes())
        ticket = self.tickets()[0]
        for action in (lambda: reader.reopen('q1', reason='Repair'),
                       lambda: reader.acknowledge('q1', ticket['id'], task_id='task', receipt='Delivered',
                                                  fingerprint=ticket['fingerprint'])):
            with self.assertRaisesRegex(ValueError, 'owner key'):
                action()
        self.c.seal()
        self.assertEqual(self.tickets('partial_artifact')[0]['status'], 'resolved')

    def test_final_proof_review_requires_matching_provider_and_astra(self):
        manifest = self.fixture()
        for provider, model, message in [('claude', 'gpt-6-astra', 'provider'),
                                          ('codex', 'gpt-6-sol', 'Astra')]:
            ref = self.write('dispatch.json', {'reviewer': 'reviewer', 'role': 'final_proof_review',
                'task_id': 'real-task', 'model': model, 'provider': provider,
                'final_answer_sha256': manifest['final_answer']['sha256']})
            review = self.write('proof.json', {'reviewer': 'reviewer', 'implementers': ['worker'],
                'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [],
                'final_answer_sha256': manifest['final_answer']['sha256'], 'reviewer_provenance': ref})
            manifest['final_proof_review'] = review
            self.write('manifest.json', manifest)
            with patch('campaign.audit_original_scope', return_value=[]):
                with self.assertRaisesRegex(ValueError, message):
                    self.c.finish('q1', manifest='manifest.json')

    def test_postseal_staleness_can_be_delivered_without_reopening(self):
        manifest = self.fixture()
        with patch('campaign.audit_original_scope', return_value=[]), patch(
                'campaign_evidence.assess_evidence', return_value=self.result(manifest)):
            self.c.finish('q1', manifest='manifest.json')
            (self.c.root / 'problems/q2/partial.md').write_text('Partial')
            self.c.finish('q2', partial='partial.md')
            self.c.seal()
            self.write('answer.md', 'Edited after seal')
            self.c.refresh()
            ticket = self.tickets('original')[0]
            self.c.acknowledge('q1', ticket['id'], task_id='persistent-main',
                               receipt='Host delivered postseal invalidation', fingerprint=ticket['fingerprint'])
            state = self.c.status()
            self.assertTrue(state['sealed'])
            self.assertFalse(state['successful_complete'])
            self.assertEqual(self.tickets('original')[0]['status'], 'open')
            self.assertFalse(self.tickets('original')[0]['needs_delivery'])
            with self.assertRaisesRegex(ValueError, 'sealed'):
                self.c.reopen('q1', reason='Cannot change sealed attempt')
