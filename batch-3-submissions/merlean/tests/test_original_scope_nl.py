"""Pure NL answers and exact final-deliverable scope bindings."""
import unittest
import test_original_scope as legacy
from original_scope import audit_original_scope, node_scope_errors


class NaturalLanguageScopeTests(unittest.TestCase):
    digest = staticmethod(legacy.OriginalScopeTests.digest)
    write = legacy.OriginalScopeTests.write
    refresh = legacy.OriginalScopeTests.refresh
    tearDown = legacy.OriginalScopeTests.tearDown

    def setUp(self):
        legacy.OriginalScopeTests.setUp(self)
        self.answer = 'No. The natural number one is not zero, so the universal assertion is false.'
        self.manifest['candidate_kind'] = 'natural_language'
        self.manifest['final_answer'] = self.write('answer.md', self.answer)
        self.report['candidate_kind'] = 'natural_language'
        self.report['final_answer_sha256'] = self.manifest['final_answer']['sha256']
        self.report['roots'] = [{'name': 'answer', 'statement': self.answer,
                                 'answer_passage': {'start': 0, 'end': len(self.answer), 'text': self.answer}}]
        self.target = {'target_statement': self.answer, 'plan_statement_id': 'answer'}
        self.bind_target()

    def bind_target(self):
        self.manifest['target_contract'] = self.write('target.json', self.target)
        self.report['target_contract_sha256'] = self.manifest['target_contract']['sha256']

    def errors(self, **kwargs):
        self.refresh()
        return audit_original_scope(self.manifest, self.base, **kwargs)

    def test_nl_complete_answer_without_lean(self):
        self.assertEqual(self.errors(required=True, require_final_answer=True), [])

    def test_nl_plan_anchor_binds_statement_and_manifest(self):
        self.refresh()
        node = {'question_status': 'settled', 'id': 'answer', 'anchor': self.answer,
                'original_scope_manifest': {**self.manifest_ref,
                                           'path': str(self.base / 'manifest.json')}}
        self.assertEqual(node_scope_errors(node), [])
        node['anchor'] = 'A different claim.'
        self.assertTrue(node_scope_errors(node))

    def test_passage_offsets_are_unicode_characters(self):
        prefix = '结论：\n'
        self.manifest['final_answer'] = self.write('answer.md', prefix + self.answer)
        self.report['final_answer_sha256'] = self.manifest['final_answer']['sha256']
        self.report['roots'][0]['answer_passage'].update(start=len(prefix), end=len(prefix + self.answer))
        self.assertEqual(self.errors(), [])

    def test_edited_final_file_invalidates_review(self):
        (self.base / 'answer.md').write_text(self.answer + ' Every number is zero.')
        self.assertTrue(self.errors())

    def test_updated_answer_hash_requires_new_report_binding(self):
        self.manifest['final_answer'] = self.write('answer.md', self.answer + '\n')
        self.assertTrue(any('FINAL_ANSWER' in e for e in self.errors()))

    def test_missing_final_answer_blocked(self):
        del self.manifest['final_answer']
        self.assertTrue(self.errors())

    def test_invented_or_mislocated_passage_blocked(self):
        for update in ({'text': 'Invented conclusion.'}, {'start': 1}, {'end': 999}, {'start': True}):
            with self.subTest(update=update):
                self.report['roots'][0]['answer_passage'] = {'start': 0, 'end': len(self.answer), 'text': self.answer, **update}
                self.assertTrue(any('PASSAGE' in e for e in self.errors()))

    def test_target_mismatch_blocked(self):
        self.target['target_statement'] = 'An easier and different result.'
        self.bind_target()
        self.assertTrue(any('TARGET' in e for e in self.errors()))

    def test_original_binding_and_clause_coverage_still_required(self):
        self.report['original_problem_sha256'] = '0' * 64
        self.report['coverage'] = []
        errors = self.errors()
        self.assertTrue(any('STALE' in e for e in errors))
        self.assertTrue(any('COVERAGE' in e for e in errors))

    def test_independence_and_dispatch_checks_preserved(self):
        self.report['reviewer'] = 'proof-worker'
        self.assertTrue(any('INDEPENDENCE' in e for e in self.errors()))
        self.report['reviewer'] = 'independent-reviewer'
        self.provenance['model'] = 'gpt-5.6-sol'
        self.report['reviewer_provenance'] = self.write('dispatch.json', self.provenance)
        self.assertTrue(any('REVIEWER_MODEL' in e for e in self.errors()))

    def test_cannot_use_nl_branch_for_gold_or_lean_original(self):
        self.manifest['grade'] = 'GOLD'
        self.assertTrue(any('CANDIDATE' in e for e in self.errors()))
        self.manifest['grade'] = 'SILVER'
        for kind in ('lean', 'mixed'):
            self.original['input_kind'] = kind
            self.manifest['original_problem'] = self.write('original.json', self.original)
            self.report['original_problem_sha256'] = self.manifest['original_problem']['sha256']
            self.assertTrue(any('CANDIDATE' in e for e in self.errors()))

    def test_required_final_binding_cannot_be_skipped_by_partial_status(self):
        self.manifest['question_status'] = 'partial'
        del self.manifest['final_answer']
        self.assertTrue(self.errors(require_final_answer=True))

    def test_legacy_lean_optional_final_answer(self):
        self.tmp.cleanup()
        legacy.OriginalScopeTests.setUp(self)
        self.assertEqual(self.errors(), [])
        self.assertTrue(self.errors(require_final_answer=True))
        self.manifest['final_answer'] = self.write('answer.md', 'One refutes the universal assertion.')
        self.report['final_answer_sha256'] = self.manifest['final_answer']['sha256']
        self.assertEqual(self.errors(require_final_answer=True), [])
        (self.base / 'answer.md').write_text('A different answer.')
        self.assertTrue(self.errors(require_final_answer=True))


if __name__ == '__main__':
    unittest.main()
