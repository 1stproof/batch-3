"""Controller authority and evidence-derived project table tests."""
import json
from pathlib import Path
from unittest.mock import patch
import unittest
from test_campaign import CampaignTests
from campaign import Campaign


class CampaignTableTests(unittest.TestCase):
    setUp = CampaignTests.setUp
    tearDown = CampaignTests.tearDown
    write = CampaignTests.write
    fixture = CampaignTests.fixture

    def test_controller_key_is_required_for_every_reopened_writer(self):
        reader = Campaign(self.c.root)
        self.assertEqual(reader.status()['problem_count'], 2)
        for operation in (lambda: reader.claim('q1', 'worker'), reader.refresh, reader.seal,
                          lambda: reader.observe('q1', manifest='manifest.json')):
            with self.assertRaisesRegex(ValueError, 'owner key'):
                operation()
        wrong = self.base / 'wrong.key'
        wrong.write_text('wrong')
        with self.assertRaisesRegex(ValueError, 'owner key'):
            Campaign(self.c.root, owner_key=wrong).refresh()

    def test_owner_key_cannot_be_inside_worker_tree(self):
        with self.assertRaisesRegex(ValueError, 'outside'):
            Campaign.initialize(self.base / 'other', {'p': self.base / 'source.txt'},
                deadline_utc=self.c.status()['deadline_utc'], concurrency=1,
                owner_key=self.base / 'other/probs/key')

    def test_grade_and_original_are_independent_and_evidence_edits_invalidate(self):
        manifest = self.fixture()
        result = {'answer': manifest['final_answer'], 'silver': {'status': 'review_recorded'},
                  'gold': {'status': 'not_applicable'}, 'paper': {'status': 'complete'}}
        with patch('campaign_evidence.assess_evidence', return_value=result), patch('campaign.audit_original_scope', return_value=[]):
            self.c.observe('q1', manifest='manifest.json')
            row = self.c.status()['problems']['q1']
            self.assertEqual(row['observations']['silver']['status'], 'review_recorded')
            self.assertEqual(row['observations']['original']['status'], 'pending')
            self.assertFalse(row['successful_complete'])
            self.c.finish('q1', manifest='manifest.json')
            self.assertTrue(self.c.status()['problems']['q1']['successful_complete'])
            self.write('manifest.json', {'edited': True})
            row = Campaign(self.c.root).status()['problems']['q1']
            self.assertEqual(row['observations']['silver']['status'], 'stale')
            self.assertEqual(row['observations']['original']['status'], 'stale')
            self.assertFalse(row['successful_complete'])
            self.c.refresh()
        table = (self.c.root / 'project-table.md').read_text()
        self.assertIn('Problems: 2', table)
        self.assertIn('stale', table)

    def test_unrelated_answer_cannot_satisfy_project_completion(self):
        manifest = self.fixture()
        result = {'answer': manifest['final_answer'],
                  'silver': {'status': 'review_recorded'},
                  'gold': {'status': 'not_applicable'}, 'paper': {'status': 'complete'}}
        with patch('campaign_evidence.assess_evidence', return_value=result), patch('campaign.audit_original_scope', return_value=[]):
            self.c.finish('q1', manifest='manifest.json')
            self.assertTrue(self.c.status()['problems']['q1']['successful_complete'])
            other_answer = self.write('other-answer.md', 'A different local result.')
            other_manifest = dict(manifest, final_answer=other_answer)
            self.write('other-manifest.json', other_manifest)
            result['answer'] = other_answer
            self.c.observe('q1', manifest='other-manifest.json')
            row = self.c.status()['problems']['q1']
            self.assertEqual(row['observations']['original']['status'], 'verified')
            self.assertEqual(row['observations']['paper']['status'], 'complete')
            self.assertFalse(row['evidence_matches_original_answer'])
            self.assertFalse(row['successful_complete'])

    def test_sealed_partial_is_never_success(self):
        for ident in ('q1', 'q2'):
            (self.c.root / 'problems' / ident / 'partial.md').write_text('Unresolved')
            self.c.finish(ident, partial='partial.md')
        self.c.seal()
        self.assertTrue(self.c.status()['sealed'])
        self.assertFalse(self.c.status()['successful_complete'])
        with self.assertRaisesRegex(ValueError, 'sealed'):
            self.c.observe('q1', manifest='partial.md')

    def test_table_read_does_not_mutate_snapshot(self):
        table = self.c.root / 'project-table.md'
        before = table.read_bytes(), table.stat().st_mtime_ns
        Campaign(self.c.root).status()
        self.assertEqual(before, (table.read_bytes(), table.stat().st_mtime_ns))


if __name__ == '__main__':
    unittest.main()
