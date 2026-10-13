"""Every final scope reviewer must pass; duplication cannot create independence."""
import copy
import json
import unittest
import test_original_scope as fixtures
from original_scope import audit_original_scope


class OriginalScopePanelTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.OriginalScopeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.base = self.fixture.base
        self.manifest = self.fixture.manifest

    def errors(self):
        return audit_original_scope(self.manifest, self.base, required=True)

    def second(self, changes=None, receipt_changes=None):
        ref = self.manifest['original_scope_audits'][1]
        report = json.loads((self.base/ref['path']).read_text())
        if receipt_changes:
            receipt = json.loads((self.base/report['reviewer_provenance']['path']).read_text())
            receipt.update(receipt_changes)
            report['reviewer_provenance'] = self.fixture.write('second-dispatch.json', receipt)
        report.update(changes or {})
        self.manifest['original_scope_audits'][1] = self.fixture.write('second-review.json', report)

    def test_two_pass_and_alias_optional_single_historical_insufficient(self):
        self.assertEqual(self.errors(), [])
        self.manifest.pop('original_scope_audit')
        self.assertEqual(self.errors(), [])
        self.manifest['original_scope_audit'] = self.manifest['original_scope_audits'][0]
        self.manifest.pop('original_scope_audits')
        self.assertTrue(any('legacy single' in error for error in self.errors()))

    def test_second_failed_unknown_missing_or_stale_blocks(self):
        before = copy.deepcopy(self.manifest)
        for verdict in ('fail', 'unknown', None):
            self.second({'verdict': verdict})
            self.assertTrue(any('NOT_PASSED' in error for error in self.errors()))
        self.second({'verdict': 'PASS_FULL_SCOPE', 'coverage': []})
        self.assertTrue(any('COVERAGE' in error for error in self.errors()))
        self.manifest = before
        (self.base/'second-review.json').write_text('{}')
        self.assertTrue(any('stale' in error for error in self.errors()))
        (self.base/'second-review.json').unlink()
        self.assertTrue(self.errors())

    def test_duplicate_actor_and_genuine_dispatch_identity_block(self):
        self.second({'reviewer': ' INDEPENDENT-REVIEWER '}, {'reviewer': ' INDEPENDENT-REVIEWER '})
        self.assertTrue(any('PANEL_INDEPENDENCE' in error for error in self.errors()))
        self.second({'reviewer': 'second-independent-reviewer'}, {'reviewer': 'second-independent-reviewer', 'task_id': 'review-task'})
        self.assertTrue(any('PANEL_INDEPENDENCE' in error for error in self.errors()))
        self.second(receipt_changes={'task_id': 'unique-task', 'session_id': 'review-task'})
        self.assertTrue(any('PANEL_INDEPENDENCE' in error for error in self.errors()))

    def test_same_target_but_different_complete_roots_snapshot_blocks(self):
        report = json.loads((self.base/'second-review.json').read_text())
        roots = copy.deepcopy(report['roots'])
        roots.append(dict(roots[0], name='different'))
        snapshot = self.fixture.digest(json.dumps(roots, sort_keys=True, separators=(',', ':')))
        self.second({'roots': roots, 'proof_snapshot_sha256': snapshot})
        self.assertTrue(any('PANEL_STALE' in error for error in self.errors()))

    def test_alias_count_and_added_third_failure_not_majority_vote(self):
        self.manifest['original_scope_audit'] = self.manifest['original_scope_audits'][1]
        self.assertTrue(any('primary alias' in error for error in self.errors()))
        self.manifest['original_scope_audit'] = self.manifest['original_scope_audits'][0]
        self.manifest['original_scope_review_count'] = 1
        self.assertTrue(any('review count' in error for error in self.errors()))
        self.manifest.pop('original_scope_review_count')
        third = copy.deepcopy(self.fixture.report)
        third.update(reviewer='third-reviewer', verdict='unknown')
        third['reviewer_provenance'] = self.fixture.write('third-dispatch.json', dict(self.fixture.provenance,
            reviewer='third-reviewer', task_id='third-dispatch'))
        self.manifest['original_scope_audits'].append(self.fixture.write('third-review.json', third))
        self.assertTrue(any('NOT_PASSED' in error for error in self.errors()))

    def test_scope_reviewer_cannot_reuse_proof_or_grade_session(self):
        for field in ('final_proof_review', 'silver_review'):
            self.manifest[field] = self.fixture.write(field + '.json', {
                'reviewer': 'separate-actor', 'reviewer_provenance': self.fixture.write(field + '-dispatch.json',
                    {'task_id': 'second-review-task', 'reviewer': 'separate-actor'})})
            self.assertTrue(any('PANEL_INDEPENDENCE' in error for error in self.errors()))
            self.manifest.pop(field)

    def test_mixed_review_input_version_blocks(self):
        self.second({'review_input_sha256': 'a' * 64})
        self.assertTrue(any('PANEL_STALE' in error for error in self.errors()))

    def test_missing_shared_input_and_dispatch_prompt_mismatch_block(self):
        self.second({'review_input_sha256': None}, {'review_input_sha256': None})
        self.assertTrue(any('immutable review input' in e for e in self.errors()))
        self.second({'review_input_sha256': self.fixture.report['review_input_sha256']},
                    {'review_input_sha256': 'c' * 64})
        self.assertTrue(any('immutable review input' in e for e in self.errors()))
        self.second(receipt_changes={'review_input_sha256': self.fixture.report['review_input_sha256'],
                                     'prompt_sha256': 'd' * 64})
        self.assertTrue(any('identical actual prompts' in e for e in self.errors()))
