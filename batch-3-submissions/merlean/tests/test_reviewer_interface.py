"""Explicit existing review predicates; synthetic protocol shapes, no research content."""
import asyncio
import copy
import json
import unittest
import test_pilot_final_progression as fixtures
import codex_pilot as p


class ReviewerInterfaceTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.FinalProgressionTests(); self.f.setUp()
        self.addCleanup(self.f.doCleanups); self.x = self.f.x

    def test_array_evidence_remains_blocking_with_exact_field_diagnostic(self):
        findings = [self.f.finding('old-' + str(i)) for i in range(3)]
        dispositions = [self.f.disposition(f['id'], evidence=['Independent observation'] * 4,
                        validation_errors=['forged success']) for f in findings]
        raw = self.f.review(finding_dispositions=dispositions)
        before = copy.deepcopy((findings, raw, self.x.current))
        result = p.finding_projection(findings, raw, self.x.current, {})
        self.assertFalse(p.proof_pass(result))
        self.assertEqual(result['unresolved_findings'], findings)
        self.assertFalse(result['finding_accountability']['complete'])
        self.assertEqual((findings, raw, self.x.current), before)
        for d in result['finding_accountability']['dispositions']:
            self.assertFalse(d['accounted']); self.assertFalse(d['effective_nonblocking'])
            self.assertIsInstance(d['evidence'], list)
            self.assertEqual(d['validation_errors'], [{'field': 'evidence',
                'expected': 'nonempty string', 'actual_type': 'list',
                'error': 'missing_wrong_type_or_empty'}])

    def test_field_diagnostics_do_not_echo_or_coerce_invalid_values(self):
        for field in ('rationale', 'evidence'):
            for value in (None, [], {}, 42, True, '', ' \n'):
                with self.subTest(field=field, value=value):
                    d = self.f.disposition(**{field: value})
                    result = self.f.projection([self.f.finding()], [d])
                    self.assertFalse(result['finding_accountability']['complete'])
                    errors = result['finding_accountability']['dispositions'][0]['validation_errors']
                    self.assertIn(field, [e['field'] for e in errors])
                    self.assertNotIn('actual_value', errors[0])

    def test_valid_and_active_dispositions_keep_authority_unchanged(self):
        for status in ('inactive_historical', 'resolved', 'active'):
            result = self.f.projection([self.f.finding()], [self.f.disposition(status=status,
                                       validation_errors=['forged'])])
            d = result['finding_accountability']['dispositions'][0]
            self.assertTrue(d['accounted'])
            self.assertEqual(d['effective_nonblocking'], status != 'active')
            self.assertEqual(p.proof_pass(result), status != 'active')
            self.assertNotIn('validation_errors', d)
            self.assertEqual(result['finding_accountability']['original_findings'], [self.f.finding()])

    def test_binding_and_semantic_failures_still_block(self):
        cases = [({'candidate_sha256': 'stale'}, 'candidate_sha256'),
                 ({'direct_consumers': ['composition']}, 'status_conditions'),
                 ({'transitive_consumers': ['composition']}, 'status_conditions'),
                 ({'no_reuse_without_reassessment': False}, 'status_conditions')]
        for fields, diagnostic in cases:
            with self.subTest(fields=fields):
                result = self.f.projection([self.f.finding()], [self.f.disposition(**fields)])
                self.assertFalse(p.proof_pass(result))
                self.assertFalse(result['finding_accountability']['complete'])
                self.assertEqual(result['finding_accountability']['dispositions'][0]
                                 ['validation_errors'][0]['field'], diagnostic)

    def triage_fixture(self):
        self.x.current['ledger']['rows'] = [dict(id='R%02d' % i, triaged=True, uses=[],
                                                **{'class': 'NOVEL'}) for i in range(1, 14)]
        review = self.f.review()
        base = review['triage_decisions'][0]
        review['triage_decisions'] = [dict(base, row_id=r['id']) for r in self.x.current['ledger']['rows']]
        return review

    def test_all_or_partial_missing_reasons_report_exact_ids_without_mutation(self):
        for supplied in ([], ['R04', 'R08', 'R11']):
            review = self.triage_fixture()
            for d in review['triage_decisions']:
                if d['row_id'] in supplied: d['reassessment_reason'] = 'Independent reassessment'
            previous = [dict(d, selected=False) for d in review['triage_decisions']]
            before = copy.deepcopy((self.x.current, review, previous))
            missing = [d['row_id'] for d in review['triage_decisions'] if d['row_id'] not in supplied]
            with self.assertRaisesRegex(ValueError, 'independent reassessment reason') as error:
                p.checked_triage(self.x.current, review, previous)
            self.assertIn('IDs=' + json.dumps(missing), str(error.exception))
            self.assertEqual((self.x.current, review, previous), before)
            for d in review['triage_decisions']: d['reassessment_reason'] = 'Independent reassessment'
            self.assertEqual(p.checked_triage(self.x.current, review, previous), review['triage_decisions'])

    def test_exact_legacy_truthiness_and_current_true_semantics(self):
        self.x.current['ledger']['rows'] = [{'id': 'a', 'triaged': 1}, {'id': 'b', 'triaged': True},
                                           {'id': 'c', 'triaged': False}, {'id': 'd'}]
        previous = [{'row_id': 'a', 'selected': False}, {'row_id': 'c', 'selected': 'legacy-truthy'},
                    {'row_id': 'historical', 'selected': True}]
        self.assertEqual(p.reassessment_required_rows(self.x.current, previous), ['b', 'c'])
        review = self.triage_fixture()
        # Preserve the existing reason truthiness check; do not add a new acceptance predicate.
        for d in review['triage_decisions']: d['reassessment_reason'] = ['legacy truthy']
        p.checked_triage(self.x.current, review, [])

    def test_prompt_scope_types_and_existing_bounded_correction(self):
        first = self.triage_fixture(); second = copy.deepcopy(first)
        for d in second['triage_decisions']: d['reassessment_reason'] = 'Independent current reassessment'
        prompts = []
        async def call(role, instruction, **kwargs):
            prompts.append(instruction)
            return self.f.meta('fresh-' + str(len(prompts))), (first if len(prompts) == 1 else second)
        self.x.call = call
        asyncio.run(self.x.review_candidate('focused'))
        self.assertEqual(len(prompts), 2)
        ids = [r['id'] for r in self.x.current['ledger']['rows']]
        for prompt in prompts:
            self.assertIn('rationale:nonempty string and evidence:nonempty string', prompt)
            section = prompt.split('REASSESSMENT_REASON REQUIRED IF DESELECTED (exact current row IDs):\n')[1]
            self.assertTrue(section.startswith(p.encoded(ids)))
            self.assertIn('not an instruction to select or deselect', section)
        self.assertEqual(first['triage_decisions'][0].get('reassessment_reason'), None)
        self.assertEqual(len(list(self.x.folder.glob('*invalid-*.json'))), 1)


if __name__ == '__main__': unittest.main()
