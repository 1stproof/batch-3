"""Exact selected-row guidance preserves independent triage and bounded recovery."""
import asyncio
import copy
import json
import unittest
from unittest.mock import AsyncMock
import test_pilot_final_progression as fixtures
from test_pilot_review_recovery import restore_packet
import codex_pilot as p


class TriageGuidanceTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.FinalProgressionTests(); self.f.setUp()
        self.addCleanup(self.f.doCleanups); self.x = self.f.x

    def test_empty_selection_valid_but_every_ledger_row_still_required(self):
        review = self.f.review()
        self.assertEqual(p.checked_triage(self.x.current, review, []), review['triage_decisions'])
        review['triage_decisions'] = []
        with self.assertRaisesRegex(ValueError, 'every ledger row exactly once'):
            p.checked_triage(self.x.current, review, [])

    def test_selected_subset_exact_and_diagnostic_does_not_repair_response(self):
        self.x.current['ledger']['rows'].append({'id': 'routine', 'uses': [], 'class': 'NOVEL'})
        review = self.f.review(triaged_rows=['composition'])
        review['triage_decisions'][0].update(selected=True, trigger='theorem_crux')
        review['triage_decisions'].append(dict(review['triage_decisions'][0], row_id='routine', selected=False, trigger='none'))
        p.checked_triage(self.x.current, review, [])
        for bad in ([], ['routine'], ['composition', 'composition'], ['composition', 'routine'], None, 'composition'):
            malformed = copy.deepcopy(review); malformed['triaged_rows'] = bad
            before = copy.deepcopy(malformed)
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, 'expected selected=true IDs=') as error:
                p.checked_triage(self.x.current, malformed, [])
            self.assertIn('expected selected=true IDs=["composition"]', str(error.exception))
            self.assertIn('received triaged_rows=' + json.dumps(bad), str(error.exception))
            self.assertEqual(malformed, before)

    def test_empty_array_does_not_bypass_independent_reassessment(self):
        self.x.current['ledger']['rows'][0]['triaged'] = True
        review = self.f.review()
        with self.assertRaisesRegex(ValueError, 'independent reassessment reason'):
            p.checked_triage(self.x.current, review, [])
        review['triage_decisions'][0]['reassessment_reason'] = 'Independent current evidence removes the earlier local selection.'
        p.checked_triage(self.x.current, review, [])

    def test_empty_array_cannot_hide_selected_or_unestablished_inference(self):
        review = self.f.review()
        review['triage_decisions'][0].update(selected=True, trigger='theorem_crux')
        with self.assertRaisesRegex(ValueError, 'expected selected=true IDs='):
            p.checked_triage(self.x.current, review, [])
        review['triaged_rows'] = ['composition']
        review['triage_decisions'][0].update(inference_ready=False, trigger='research_gap')
        with self.assertRaisesRegex(ValueError, 'existing inference'):
            p.checked_triage(self.x.current, review, [])

    def test_exhausted_correction_keeps_both_invalid_reports_without_authority(self):
        self.x.current['ledger']['rows'][0]['triaged'] = True
        first = self.f.review(verdict='INCOMPLETE', gaps=['Unfinished synthetic proof'], triaged_rows=['composition'])
        second = copy.deepcopy(first)
        second['triage_decisions'][0]['reassessment_reason'] = 'Independent evidence does not select this local check.'
        originals = copy.deepcopy([first, second]); prompts = []
        candidate = copy.deepcopy(self.x.current)
        self.x.execution = AsyncMock(side_effect=AssertionError('no execution from invalid review'))
        self.x.probe = AsyncMock(side_effect=AssertionError('no probe from invalid review'))
        async def call(role, instruction, **kwargs):
            self.assertEqual(role, 'proof-review'); prompts.append(instruction)
            return self.f.meta('fresh-' + str(len(prompts))), [first, second][len(prompts)-1]
        self.x.call = call
        with self.assertRaisesRegex(ValueError, 'expected selected=true IDs=\\[\\]'):
            asyncio.run(self.x.review_candidate('focused'))
        self.assertEqual(len(prompts), 2)
        for prompt in prompts:
            self.assertIn('exactly the unique row_id values', prompt)
            self.assertIn('use [] when all decisions have selected:false', prompt)
        packet = restore_packet(json.loads(prompts[1].split('EXACT REVIEW INPUTS (lossless supplied-text bindings):\n')[1]))
        self.assertEqual(p.encoded(packet['exact_candidate']), p.encoded(candidate))
        diagnostic = packet['invalid_prior_response_not_authority']
        self.assertEqual(diagnostic['invalid_review'], first)
        self.assertIn('independent reassessment reason', diagnostic['error'])
        saved = [json.loads(path.read_text()) for path in sorted(self.x.folder.glob('*invalid-*.json'))]
        self.assertEqual([item['invalid_review'] for item in saved], originals)
        self.assertEqual([item['retry_remaining'] for item in saved], [True, False])
        self.assertIn('received triaged_rows=["composition"]', saved[1]['error'])
        self.assertIsNone(self.x.active_triage); self.assertEqual(self.x.triage_history, [])
        self.assertEqual(self.x.current, candidate); self.assertEqual([first, second], originals)
        self.assertFalse(list(self.x.folder.glob('*effective.json')))
        self.x.execution.assert_not_awaited(); self.x.probe.assert_not_awaited()

    def local_lineage_review(self):
        self.x.pilot.config['lite_local_verification_version'] = 1
        self.x.local_verification_modules = []
        self.x.current['sol_tasks'] = [{'kind':'lean', 'row_ids':['composition'], 'owned_scope':'bounded local file',
            'local_module':{'brief':'Existing synthetic local inference only', 'max_worker_calls':1, 'max_probe_runs':1}}]
        review = self.f.review(verdict='INCOMPLETE', gaps=['Other synthetic obligation retained'],
            triaged_rows=['composition'], approved_lean_tasks=[0], local_module_reassessments=[],
            local_module_task_links=[{'task_index':0,'prior_module_id':'probes/legacy-worker-lean',
                                     'relation':'same_claim','reason':'Historical evidence remains relevant'}])
        review['triage_decisions'][0].update(selected=True, trigger='theorem_crux',
            verification_uncertainty='high', local_check_reason='Independent bounded uncertainty assessment',
            local_check={k:'Independent substantive '+k for k in ('uncertainty','intended_objects','premise_boundary','feasibility','expected_value')})
        return review

    def test_distinct_invalid_triage_then_unknown_lineage_exhausts_existing_retry(self):
        second = self.local_lineage_review(); first = copy.deepcopy(second)
        first['triage_decisions'][0]['inference_ready'] = False
        originals = copy.deepcopy([first, second]); prompts = []
        before = copy.deepcopy(self.x.current)
        async def call(role, instruction, **kwargs):
            prompts.append(instruction)
            return self.f.meta('fresh-'+str(len(prompts))), [first, second][len(prompts)-1]
        self.x.call = call
        with self.assertRaisesRegex(ValueError, 'exact current module IDs='):
            asyncio.run(self.x.review_candidate('focused'))
        self.assertEqual(len(prompts), 2)
        for prompt in prompts:
            self.assertIn('closed allowed non-null prior_module_id census):\n[]\n', prompt)
            self.assertIn('not mathematical novelty', prompt)
        saved = [json.loads(path.read_text()) for path in sorted(self.x.folder.glob('*invalid-*.json'))]
        self.assertEqual([item['invalid_review'] for item in saved], originals)
        self.assertIn('explicit research gap', saved[0]['error'])
        self.assertIn('exact current module IDs=[]', saved[1]['error'])
        self.assertEqual([item['retry_remaining'] for item in saved], [True, False])
        self.assertIsNone(self.x.active_triage)
        self.assertEqual(self.x.triage_history, [])
        self.assertEqual(self.x.current, before)
        self.assertEqual(self.x.local_verification_modules, [])
        self.assertFalse(list(self.x.folder.glob('*effective.json')))

    def test_independently_corrected_null_link_preserves_invalid_history(self):
        first = self.local_lineage_review(); corrected = copy.deepcopy(first)
        corrected['local_module_task_links'][0].update(prior_module_id=None, relation='new_claim',
            reason='First registered lineage; prior experiment retained and independently assessed')
        self.x.call = AsyncMock(side_effect=[(self.f.meta('fresh-1'), first), (self.f.meta('fresh-2'), corrected)])
        _, effective = asyncio.run(self.x.review_candidate('focused'))
        self.assertEqual(self.x.call.await_count, 2)
        self.assertEqual(self.x.triage_history[-1]['receipt']['session_id'], 'fresh-2')
        self.assertEqual(self.x.triage_history[-1]['local_module_links'][p.sha(p.encoded(self.x.current['sol_tasks'][0]))]['prior_module_id'], None)
        self.assertEqual(effective['verdict'], 'INCOMPLETE')
        self.assertEqual(self.x.local_verification_modules, [])  # Review itself dispatches no worker or module.
        diagnostic = json.loads(next(self.x.folder.glob('*invalid-1.json')).read_text())
        self.assertEqual(diagnostic['invalid_review'], first)
        self.assertEqual(diagnostic['status'], 'invalid_not_authority')


if __name__ == '__main__': unittest.main()
