"""Real scope/Silver evidence through durable rejection, repair, and acceptance."""
import unittest
import test_campaign_scope_integration as fixtures
from campaign import Campaign


class FeedbackIntegrationTests(unittest.TestCase):
    setUp = fixtures.CampaignScopeIntegrationTests.setUp
    tearDown = fixtures.CampaignScopeIntegrationTests.tearDown
    digest = staticmethod(fixtures.CampaignScopeIntegrationTests.digest)
    write = fixtures.CampaignScopeIntegrationTests.write
    refresh = fixtures.CampaignScopeIntegrationTests.refresh
    bind_target = fixtures.CampaignScopeIntegrationTests.bind_target
    bind_original = fixtures.CampaignScopeIntegrationTests.bind_original
    bind_silver = fixtures.CampaignScopeIntegrationTests.bind_silver

    def tickets(self):
        return self.campaign.feedback('problem')['problems']['problem']['feedback']

    def test_rejected_scope_returns_to_main_and_closes_only_after_revalidation(self):
        self.report['gaps'] = ['Missing original obligation.']
        self.refresh()
        with self.assertRaisesRegex(ValueError, 'ORIGINAL_SCOPE_INCOMPLETE'):
            self.campaign.finish('problem', manifest='manifest.json')
        ticket = self.tickets()[0]
        self.assertEqual(ticket['status'], 'open')
        self.assertTrue(ticket['needs_delivery'])
        self.assertIn('ORIGINAL_SCOPE_INCOMPLETE', str(ticket['errors']))
        self.campaign = Campaign(self.campaign.root, owner_key=self.campaign.owner_key)
        self.campaign.acknowledge('problem', ticket['id'], fingerprint=ticket['fingerprint'], task_id='resumed-main',
                                  receipt='Host delivered the exact rejected revision and diagnostics.')
        self.assertEqual(self.tickets()[0]['status'], 'open')
        registry = (self.campaign.root / 'registry.json').read_bytes()
        self.campaign.reopen('problem', reason='Repair the original obligation in the same attempt.')
        self.assertEqual(self.tickets()[0]['status'], 'open')
        token = self.campaign.claim('problem', 'resumed-main')
        self.report['gaps'] = []
        self.provenance['task_id'] = 'fresh-scope-review-after-repair'
        self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
        self.refresh()
        self.campaign.release('problem', token)
        self.campaign.finish('problem', manifest='manifest.json')
        self.assertTrue(all(t['status'] == 'resolved' for t in self.tickets()))
        self.campaign.seal()
        self.assertTrue(self.campaign.status()['successful_complete'])
        self.assertEqual((self.campaign.root / 'registry.json').read_bytes(), registry)

    def test_changed_answer_must_return_through_new_scope_proof_and_silver_evidence(self):
        self.campaign.finish('problem', manifest='manifest.json')
        self.answer += ' In particular, the witness is a permitted natural number.'
        (self.base / 'answer.md').write_text(self.answer)
        with self.assertRaises(ValueError):
            self.campaign.seal()
        self.assertTrue(any(t['gate'] == 'original' and t['status'] == 'open' for t in self.tickets()))
        self.campaign.reopen('problem', reason='Repair stale final-answer evidence without resetting the attempt.')
        token = self.campaign.claim('problem', 'original-main')
        self.manifest['final_answer'] = self.write('answer.md', self.answer)
        self.report['final_answer_sha256'] = self.manifest['final_answer']['sha256']
        self.report['roots'] = [{'name': 'answer', 'statement': self.answer,
                                'answer_passage': {'start': 0, 'end': len(self.answer), 'text': self.answer}}]
        self.target['target_statement'] = self.answer
        self.bind_target()
        self.provenance['task_id'] = 'scope-new-answer'
        self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
        self.refresh()
        self.campaign.release('problem', token)
        # Scope repaired alone cannot reuse the old independent proof receipt.
        with self.assertRaises(ValueError):
            self.campaign.finish('problem', manifest='manifest.json')
        self.proof_review['final_answer_sha256'] = self.manifest['final_answer']['sha256']
        self.proof_review['reviewer_provenance'] = self.write('proof-dispatch.json', {
            'reviewer': 'independent-proof-reviewer', 'role': 'final_proof_review',
            'task_id': 'fresh-proof-new-answer', 'model': 'gpt-6-astra', 'provider': 'codex',
            'final_answer_sha256': self.manifest['final_answer']['sha256']})
        self.manifest['final_proof_review'] = self.write('proof-review.json', self.proof_review)
        self.bind_silver()
        self.refresh()
        self.campaign.finish('problem', manifest='manifest.json')
        self.campaign.seal()
        state = self.campaign.status()
        self.assertTrue(state['successful_complete'])
        self.assertEqual(state['problems']['problem']['repair_round'], 1)
        self.assertTrue(all(t['status'] == 'resolved' for t in self.tickets()))


if __name__ == '__main__':
    unittest.main()
