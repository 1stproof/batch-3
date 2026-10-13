"""Campaign delivery gates exercised with real NL scope evidence, without mocks."""
from datetime import datetime, timedelta, timezone
import shutil
import unittest

import test_original_scope_nl as nl_fixture
from campaign import Campaign
from campaign_evidence import SILVER_CHECKS
from original_scope import audit_original_scope


class CampaignScopeIntegrationTests(unittest.TestCase):
    digest = staticmethod(nl_fixture.NaturalLanguageScopeTests.digest)
    write = nl_fixture.NaturalLanguageScopeTests.write
    refresh = nl_fixture.NaturalLanguageScopeTests.refresh
    bind_target = nl_fixture.NaturalLanguageScopeTests.bind_target
    tearDown = nl_fixture.NaturalLanguageScopeTests.tearDown

    def setUp(self):
        nl_fixture.NaturalLanguageScopeTests.setUp(self)
        fixture_base = self.base
        self.campaign = Campaign.initialize(
            fixture_base / 'campaign', {'problem': fixture_base / 'request.txt'},
            deadline_utc=(datetime.now(timezone.utc) + timedelta(days=1)).isoformat(),
            concurrency=1, owner_key=fixture_base.parent / (fixture_base.name + '-controller.key'),
        )
        self.addCleanup(self.campaign.owner_key.unlink, missing_ok=True)
        folder = self.campaign.root / 'problems' / 'problem'
        for path in fixture_base.iterdir():
            if path.is_file():
                shutil.copyfile(path, folder / path.name)
        self.base = folder
        self.original['source'] = {
            'path': 'input.txt', 'sha256': self.digest((folder / 'input.txt').read_text())}
        self.bind_original()
        provenance = {
            'reviewer': 'independent-proof-reviewer', 'role': 'final_proof_review',
            'task_id': 'fresh-final-proof-task', 'model': 'gpt-6-astra',
            'provider': 'codex', 'final_answer_sha256': self.manifest['final_answer']['sha256'],
        }
        self.proof_review = {
            'reviewer': 'independent-proof-reviewer', 'implementers': ['proof-worker'],
            'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [],
            'final_answer_sha256': self.manifest['final_answer']['sha256'],
            'reviewer_provenance': self.write('proof-dispatch.json', provenance),
        }
        self.manifest['final_proof_review'] = self.write('proof-review.json', self.proof_review)
        self.bind_silver()
        self.refresh()

    def bind_silver(self):
        # This fixture uses a counterexample with no selected Lean triage rows.
        self.manifest['ledger'] = self.write('ledger.json', {
            'rows': [{'id': 'counterexample', 'closed': True, 'triaged': False}]})
        self.manifest['assumption_census'] = self.write('census.txt', 'No extra premises.')
        provenance = {
            'reviewer': 'silver-reviewer', 'role': 'lite_grade_review',
            'task_id': 'fresh-silver-task', 'model': 'gpt-6-astra', 'model_family': 'astra',
            'provider': 'codex', 'final_answer_sha256': self.manifest['final_answer']['sha256'],
            'ledger_sha256': self.manifest['ledger']['sha256'],
        }
        silver = {
            'reviewer': 'silver-reviewer', 'implementers': self.manifest['implementers'],
            'verdict': 'SILVER', 'review_mode': 'comprehensive', 'triaged_rows': [],
            'final_answer': self.manifest['final_answer'],
            'checks': {name: {'pass': True, 'rationale': 'The counterexample and its full inference are checked.'}
                       for name in SILVER_CHECKS},
            'reviewer_provenance': self.write('silver-dispatch.json', provenance),
        }
        for field in ('ledger', 'assumption_census', 'target_contract'):
            silver[field] = self.manifest[field]
        self.manifest['silver_review'] = self.write('silver-review.json', silver)

    def bind_original(self):
        self.manifest['original_problem'] = self.write('original.json', self.original)
        self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']

    def assert_scope_passes(self):
        self.assertEqual(audit_original_scope(
            self.manifest, self.base, required=True, require_final_answer=True), [])

    def test_real_nl_scope_finish_and_seal(self):
        self.assert_scope_passes()
        token = self.campaign.claim('problem', 'main')
        self.campaign.release('problem', token)
        self.campaign.finish('problem', manifest='manifest.json')
        self.campaign.seal()
        status = self.campaign.status()
        self.assertTrue(status['sealed'])
        self.assertEqual(status['problems']['problem']['status'], 'complete')
        self.assertEqual(status['problems']['problem']['answer_sha256'],
                         self.manifest['final_answer']['sha256'])

    def test_final_answer_edit_after_finish_blocks_seal(self):
        self.campaign.finish('problem', manifest='manifest.json')
        (self.base / 'answer.md').write_text(self.answer + '\nThe opposite conclusion holds.')
        with self.assertRaisesRegex(ValueError, 'stale hash'):
            self.campaign.seal()
        self.assertFalse(self.campaign.status()['sealed'])

    def test_different_self_consistent_original_does_not_match_campaign(self):
        # This remains valid scope evidence in isolation, but is not the frozen input.
        self.original['source'] = self.write(
            'other-request.txt', 'A different request context.\n' + self.original['statement'])
        self.bind_original()
        self.refresh()
        self.assert_scope_passes()
        with self.assertRaisesRegex(ValueError, 'different registered original'):
            self.campaign.finish('problem', manifest='manifest.json')
        self.assertEqual(self.campaign.status()['problems']['problem']['status'], 'pending')

    def test_passing_scope_without_proof_review_cannot_complete(self):
        del self.manifest['final_proof_review']
        self.refresh()
        self.assert_scope_passes()
        with self.assertRaisesRegex(ValueError, 'missing pinned evidence'):
            self.campaign.finish('problem', manifest='manifest.json')
        self.assertFalse(self.campaign.status()['sealed'])
        self.assertEqual(self.campaign.status()['problems']['problem']['status'], 'pending')


if __name__ == '__main__':
    unittest.main()
