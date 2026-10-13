import copy
import asyncio
import json
import sys
import tempfile
import unittest
from types import SimpleNamespace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_convergence as c


class ConvergenceTests(unittest.TestCase):
    def setUp(self):
        self.original = 'a' * 64
        self.candidate = {'proof_markdown': 'Exact original answer and proof.',
            'answer_statement': 'Exact original answer', 'ledger': {'rows': [
                {'id': 'local', 'uses': []}, {'id': 'answer', 'uses': ['local']}]}}
        self.review = {'verdict': 'PASS_COMPLETE_PROOF', 'review_mode': 'comprehensive',
            'gaps': [], 'unresolved_findings': [], 'resolved_ids': [],
            'finding_accountability': {'complete': True}, 'triage_decisions': [
                {'row_id': 'local', 'selected': True, 'reason': 'fragile local inference'}]}
        self.panel = {'passed': True, 'errors': [], 'reports': [
            {'verdict': 'PASS_FULL_SCOPE', 'gaps': [], 'extra_assumptions': [],
             'coverage': [{'clause_id': 'c', 'result': 'covered'}]} for _ in range(2)]}

    def observed(self, evidence, count=0, candidate=None):
        candidate = candidate or self.candidate
        return c.observation(candidate, evidence, original_sha256=self.original,
            validated=True, receipts=[{'status': 'completed', 'model_verified': True,
                'fresh_session': True, 'resume_session': None, 'session_id': 'reviewer-' + str(i),
                'reviewed_candidate_sha256': c.digest(candidate), 'prompt_sha256': 'b'*64,
                'answer_sha256': 'c'*64} for i in range(count)])

    def update(self, previous=None, **kw):
        return c.update_convergence(previous, original_sha256=self.original,
            candidate=kw.pop('candidate', self.candidate), **kw)

    def complete(self):
        return self.update(review=self.observed(self.review, 1), scope=self.observed(self.panel, 2))

    def test_math_complete_certificate_open_and_grade_never_awarded(self):
        state = self.complete()
        record = state['candidates'][c.digest(self.candidate)]
        self.assertEqual(record['deficits']['mathematical']['status'], 'closed')
        self.assertEqual(record['deficits']['certification']['status'], 'open')
        self.assertEqual(record['deficits']['delivery']['status'], 'unknown')
        self.assertEqual(state['best_reviewed_original_candidate'], c.digest(self.candidate))
        self.assertNotIn('grade', state)

    def test_nonadverse_focused_review_retains_banked_comprehensive_evidence(self):
        state = self.complete()
        key = state['best_reviewed_mathematical_candidate']
        previous_math = copy.deepcopy(state['candidates'][key]['deficits']['mathematical'])
        state = self.update(state, review=self.observed({**self.review, 'review_mode': 'focused'}, 1))
        self.assertEqual(state['best_reviewed_mathematical_candidate'], key)
        self.assertEqual(state['candidates'][key]['deficits']['mathematical'], previous_math)
        self.assertEqual(state['candidates'][key]['observation_refs']['comprehensive_review'],
                         previous_math['evidence_sha256'])
        adverse = {**self.review, 'review_mode': 'focused', 'verdict': 'INCOMPLETE',
            'unresolved_findings': [{'id': 'counterexample', 'kind': 'mathematical',
                                    'severity': 'fatal', 'finding': 'Composition fails'}]}
        state = self.update(state, review=self.observed(adverse, 1))
        self.assertIsNone(state['best_reviewed_mathematical_candidate'])
        self.assertIsNone(state['best_reviewed_original_candidate'])

    def test_generalization_does_not_replace_best_original(self):
        previous = self.complete()
        alternate = copy.deepcopy(self.candidate)
        alternate['proof_markdown'] = 'A conditional result under a stronger premise.'
        alternate['assumptions'] = ['Extra H']
        state = self.update(previous, candidate=alternate)
        self.assertEqual(state['best_reviewed_original_candidate'], c.digest(self.candidate))
        self.assertEqual(state['candidates'][c.digest(alternate)]['deficits']['original_scope']['status'], 'unknown')
        self.assertEqual(len(state['candidates']), 2)

    def test_self_claimed_reviews_are_never_authority(self):
        candidate = {**self.candidate, 'grade': 'SILVER', 'complete_claim': True,
                     'scope': self.panel, 'review': self.review}
        state = self.update(candidate=candidate)
        self.assertIsNone(state['best_reviewed_original_candidate'])
        self.assertTrue(all(d['status'] == 'unknown' for d in state['candidates'][c.digest(candidate)]['deficits'].values()))
        with self.assertRaises(ValueError):
            c.observation(candidate, self.review, original_sha256=self.original)

    def test_binding_and_receipt_failures_rejected(self):
        base = self.observed(self.review, 1)
        for mutation in [lambda o: o.update(candidate_sha256='d'*64),
                         lambda o: o.update(original_sha256='d'*64),
                         lambda o: o['evidence'].update(gaps=['new gap']),
                         lambda o: o['receipts'][0].update(fresh_session=False),
                         lambda o: o['receipts'][0].update(model_verified=False),
                         lambda o: o['receipts'][0].update(reviewed_candidate_sha256='d'*64)]:
            obs = copy.deepcopy(base); mutation(obs)
            with self.assertRaises(ValueError): self.update(review=obs)
        obs = self.observed(self.panel, 2)
        obs['receipts'][1]['session_id'] = obs['receipts'][0]['session_id']
        with self.assertRaises(ValueError): self.update(scope=obs)

    def test_verified_same_reviewer_recovery_is_scheduling_evidence_not_fresh_scope(self):
        report = {**self.review, 'review_mode': 'focused', 'verdict': 'INCOMPLETE',
                  'unresolved_findings': [{'id': 'bridge', 'kind': 'mathematical', 'severity': 'fatal',
                                           'finding': 'Counterexample'}]}
        obs = self.observed(report, 1)
        receipt = obs['receipts'][0]
        origin = {**receipt, 'name': 'p/001-proof-review', 'status': 'timeout_censored',
                  'model_actual': 'gpt-6-astra'}
        receipt.update(name='p/002-proof-review', fresh_session=False,
                       resume_session=receipt['session_id'], independent_recovery_origin=origin)
        state = self.update(review=obs)
        self.assertEqual(state['phase']['name'], 'reconsidering')
        self.assertIsNone(state['best_reviewed_mathematical_candidate'])
        receipt['resume_session'] = 'different-reviewer'
        with self.assertRaises(ValueError): self.update(review=obs)

    def test_scope_stable_until_changed_evidence_and_reopening_retained(self):
        state = self.complete()
        obs = self.observed(self.panel, 2)
        obs['receipts'][0]['answer_sha256'] = 'd'*64
        repeated = self.update(state, scope=obs)
        self.assertEqual(len(repeated['scope_decisions']), 1)
        self.assertNotIn('independent_evidence_changed', repeated['triggers'])
        failed = copy.deepcopy(self.panel)
        failed.update(passed=False, errors=['Original clause omitted'])
        failed['reports'][0].update(verdict='fail', gaps=['Original clause omitted'])
        reopened = self.update(repeated, scope=self.observed(failed, 2))
        self.assertIsNone(reopened['best_reviewed_original_candidate'])
        self.assertEqual(len(reopened['scope_decisions']), 2)
        self.assertEqual(reopened['scope_decisions'][-1]['reopening_basis'], 'changed_exact_independent_evidence')
        self.assertGreater(len(reopened['observations']), len(state['observations']))

    def test_scope_pass_cannot_hide_substantive_failure(self):
        for key, bad in [('gaps', ['gap']), ('extra_assumptions', ['H']), ('verdict', 'unknown')]:
            panel = copy.deepcopy(self.panel); panel['reports'][1][key] = bad
            with self.assertRaises(ValueError): self.update(scope=self.observed(panel, 2))

    def test_focused_pass_and_research_gap_never_close_math(self):
        review = copy.deepcopy(self.review); review['review_mode'] = 'focused'
        state = self.update(review=self.observed(review, 1), scope=self.observed(self.panel, 2))
        self.assertIsNone(state['best_reviewed_original_candidate'])
        review = copy.deepcopy(self.review)
        review['triage_decisions'] = [{'row_id': 'local', 'selected': False, 'trigger': 'research_gap', 'reason': 'Novel inference missing'}]
        state = self.update(review=self.observed(review, 1))
        self.assertEqual(state['candidates'][c.digest(self.candidate)]['deficits']['mathematical']['status'], 'open')

    def test_negative_research_survives_without_fabricated_progress(self):
        work = {'objective': 'Resolve crux', 'approach': 'Test representation',
            'work_performed': 'Derived an obstruction to this route',
            'result': 'This auxiliary lemma does not imply the crux',
            'next_step': 'Reconsider the bridge', 'failed_approaches': ['Auxiliary implication invalid']}
        state = self.update(research_work=work)
        for _ in range(150): state = self.update(state, research_work=work)
        self.assertEqual(len(state['research_archive']), 1)
        self.assertIn('research_recorded_without_claiming_gap_closure', state['triggers'])
        self.assertNotIn('stop', state)

    def test_auxiliary_consumers_and_unchanged_crux_trigger(self):
        work = {'work_id': 'aux-1', 'consumers': [{'domain': 'mathematical', 'id': 'gap-1'}],
                'expected_contribution': 'Prove the missing implication'}
        state = self.update(auxiliary_work=work)
        state = self.update(state, auxiliary_work={**work, 'work_id': 'aux-2'})
        self.assertIn('auxiliary_crux_unchanged_reconsider_value', state['triggers'])
        state = self.update(state, auxiliary_work={**work, 'work_id': 'aux-3', 'new_value': 'A counterexample now discriminates the representation'})
        self.assertNotIn('auxiliary_crux_unchanged_reconsider_value', state['triggers'])
        with self.assertRaises(ValueError): self.update(auxiliary_work={**work, 'consumers': []})
        self.assertEqual(len(state['auxiliary_archive']), 3)

    def test_cost_retriage_retains_open_obligation_and_actual_module_shape(self):
        module = {'module_id': 'm1', 'lineage_id': 'l1', 'row_id': 'local',
            'state': 'returned_to_main', 'exit_reason': 'encoding_infeasible',
            'brief': 'Check local inference', 'reentry_disposition': None, 'returns': [{'diagnostics': 'failed encoding'}]}
        context = c.compact_context(self.complete(), modules=[module])
        self.assertFalse(context['certificate_retriage'][0]['obligation_waived'])
        self.assertEqual(context['deficits']['certification']['status'], 'open')
        mapped = c.module_consumers(self.candidate, [module])[0]
        self.assertEqual(mapped['ledger_consumers'], ['answer'])
        self.assertEqual(mapped['module_evidence_sha256'], c.digest(module))
        self.assertEqual(module['returns'], [{'diagnostics': 'failed encoding'}])

    def test_host_certificate_result_does_not_close_math_or_original_scope(self):
        observation = self.observed({'passed': True, 'deficits': []})
        state = self.update(certification=observation)
        deficits = state['candidates'][c.digest(self.candidate)]['deficits']
        self.assertEqual(deficits['certification']['status'], 'closed')
        self.assertEqual(deficits['mathematical']['status'], 'unknown')
        self.assertEqual(deficits['original_scope']['status'], 'unknown')
        with self.assertRaises(ValueError): self.update(certification=self.observed({'passed': True, 'deficits': ['still required']}))

    def test_store_restore_tamper_detection_and_small_context(self):
        with tempfile.TemporaryDirectory() as folder:
            store = c.ConvergenceStore(folder)
            state = self.complete(); ref = store.save(state)
            self.assertEqual(store.load(), state)
            alternative = {**self.candidate, 'proof_markdown': 'Long alternate argument' * 10000}
            next_state = self.update(state, candidate=alternative)
            store.save(next_state)
            self.assertTrue((Path(folder) / ref['path']).exists())
            self.assertLess(len(json.dumps(c.compact_context(next_state))), 3000)
            pointer = json.loads(store.path.read_text())
            (store.archive / (pointer['state_sha256'] + '.json')).write_text('{}')
            with self.assertRaises(ValueError): store.load()

    def test_runtime_hook_persists_actual_candidate(self):
        from codex_pilot import Problem
        with tempfile.TemporaryDirectory() as folder:
            problem = Problem.__new__(Problem)
            problem.folder = Path(folder)
            problem.current = self.candidate
            problem.original_bytes = b'Frozen source'
            problem.local_verification_modules = []
            problem.record_convergence()
            saved = c.ConvergenceStore(folder).load()
            self.assertEqual(saved['current_candidate_sha256'], c.digest(self.candidate))
            self.assertIsNone(saved['best_reviewed_original_candidate'])

    def test_reviewed_nl_answer_banked_before_certification_and_final_scope(self):
        review = copy.deepcopy(self.review)
        review.update(verdict='INCOMPLETE', mathematically_ready=True,
            unresolved_findings=[{'id': 'cert', 'severity': 'gap', 'kind': 'certificate',
                                 'finding': 'Selected local certificate encoding unfinished'}],
            finding_accountability={'complete': False})
        advice = {'verdict': 'adequate', 'rationale': 'Declared premises match the original interpretation',
                  'findings': [], 'missing_evidence': []}
        state = self.update(review=self.observed(review, 1), advisory_scope=self.observed(advice, 1))
        self.assertEqual(state['best_reviewed_mathematical_candidate'], c.digest(self.candidate))
        self.assertIsNone(state['best_reviewed_original_candidate'])
        self.assertEqual(c.compact_context(state)['best_mathematical_scope_qualification'], 'advisory_adequate_not_final')
        alternate = {**self.candidate, 'proof_markdown': 'Broader conditional research'}
        state = self.update(state, candidate=alternate)
        self.assertEqual(state['best_reviewed_mathematical_candidate'], c.digest(self.candidate))
        self.assertEqual(state['candidates'][c.digest(self.candidate)]['deficits']['certification']['status'], 'open')
        self.assertEqual(state['observations'][state['candidates'][c.digest(self.candidate)]['observation_refs']['review']]['evidence']['verdict'], 'INCOMPLETE')

    def test_promising_skeleton_pauses_nonessential_routes_before_complete_proof(self):
        candidate = {**self.candidate, 'convergence_outline': {'skeleton': 'Reduce the claim to a local bridge then compose',
            'why_promising': 'The representation supplies every other step', 'open_gap_ids': ['bridge']}}
        state = self.update(candidate=candidate)
        self.assertEqual(state['phase']['name'], 'converging')
        self.assertIsNone(state['best_reviewed_mathematical_candidate'])
        broad = {'context': 'Explore another representation', 'obstruction_ids': []}
        necessary = {'context': 'Discriminate the unproved bridge of this skeleton', 'obstruction_ids': ['bridge']}
        self.assertFalse(c.scout_admission(state, [broad])['allowed'])
        self.assertTrue(c.scout_admission(state, [necessary])['allowed'])
        for kind in ('gap_closure', 'scope', 'validation', 'writeup'):
            self.assertTrue(c.work_admission(state, kind=kind)['allowed'])
        # Candidate churn and a new description do not reset convergence.
        state = self.update(state, candidate={**self.candidate, 'proof_markdown': 'Another proposal'})
        self.assertEqual(state['phase']['name'], 'converging')
        self.assertFalse(c.scout_admission(state, [broad])['allowed'])

    def test_independent_key_bridge_failure_reopens_without_lifetime_limits(self):
        candidate = {**self.candidate, 'convergence_outline': {'skeleton': 'Promising bridge',
            'why_promising': 'Other steps available', 'open_gap_ids': ['bridge']}}
        state = self.update(candidate=candidate)
        failed = {**self.review, 'verdict': 'INCOMPLETE', 'unresolved_findings': [
            {'id': 'bridge', 'severity': 'fatal', 'kind': 'mathematical', 'finding': 'Counterexample to key bridge'}]}
        state = self.update(state, candidate=candidate, review=self.observed(failed, 1, candidate))
        self.assertEqual(state['phase']['name'], 'reconsidering')
        state = self.update(state, candidate=candidate)
        self.assertEqual(state['phase']['name'], 'reconsidering')
        self.assertTrue(c.work_admission(state, kind='route_exploration')['allowed'])

    def test_focused_fatal_objection_reopens_without_claiming_comprehensive_closure(self):
        candidate = {**self.candidate, 'convergence_outline': {'skeleton': 'Bridge and composition',
            'why_promising': 'All other steps accounted for', 'open_gap_ids': ['bridge']}}
        state = self.update(candidate=candidate)
        review = {**self.review, 'review_mode': 'focused', 'verdict': 'INCOMPLETE',
            'unresolved_findings': [{'id': 'bridge', 'severity': 'fatal', 'kind': 'mathematical',
                                    'finding': 'The key bridge has a counterexample'}]}
        state = self.update(state, candidate=candidate, review=self.observed(review, 1, candidate))
        self.assertEqual(state['phase']['name'], 'reconsidering')
        self.assertIsNone(state['best_reviewed_mathematical_candidate'])

    def test_approved_sol_alternative_cannot_bypass_convergence(self):
        from codex_pilot import Problem
        from unittest.mock import AsyncMock
        task = {'kind': 'research', 'task': 'Find an unrelated alternative', 'context': 'Different generalization',
                'hypotheses': ['original'], 'advisory_hints': 'explore', 'owned_scope': 'notes',
                'acceptance_checks': ['report'], 'consumer_ids': []}
        candidate = {**self.candidate, 'sol_tasks': [task], 'convergence_outline':
                     {'skeleton': 'Existing promising route', 'why_promising': 'One bridge remains', 'open_gap_ids': ['bridge']}}
        with tempfile.TemporaryDirectory() as folder:
            problem = Problem.__new__(Problem)
            problem.folder, problem.current, problem.counter = Path(folder), candidate, 1
            problem.convergence_state = self.update(candidate=candidate)
            problem.research_authorized = lambda task: True
            problem.call, problem.probe = AsyncMock(), AsyncMock(return_value={'status': 'not_requested'})
            result = asyncio.run(problem.execution())
            problem.call.assert_not_awaited()
            self.assertEqual(result['workers'][0]['output']['status'], 'deferred')
            self.assertFalse(c.ConvergenceStore(folder).load()['last_execution_admission']['allowed'])

    def test_store_does_not_duplicate_large_candidate_body_per_observation(self):
        candidate = {**self.candidate, 'proof_markdown': 'A' * 100000}
        with tempfile.TemporaryDirectory() as folder:
            store = c.ConvergenceStore(folder)
            state = self.update(candidate=candidate); store.save(state)
            for index in range(10):
                state = self.update(state, candidate=candidate, delivery=self.observed(
                    {'passed': False, 'deficits': ['missing artifact ' + str(index)]}, candidate=candidate))
                store.save(state)
            total = sum(p.stat().st_size for p in store.archive.rglob('*.json'))
            self.assertLess(total, 220000)
            self.assertEqual(store.load(), state)

    def test_nonexam_runtime_pauses_unrequested_routes_for_early_incomplete_skeleton(self):
        from codex_pilot import Problem
        candidate = {**self.candidate, 'convergence_outline': {'skeleton': 'Local bridge then composition',
            'why_promising': 'Only one necessary bridge is unresolved', 'open_gap_ids': ['bridge']},
            'route_scout_tasks': [{'angle': angle, 'task': 'Develop ' + angle,
                'context': 'Try an unrelated broad approach', 'purpose': 'scientific_alternative',
                'target_row_ids': ['local'], 'obstruction_ids': []} for angle in ('spectral', 'combinatorial')]}
        with tempfile.TemporaryDirectory() as folder:
            problem = Problem.__new__(Problem)
            problem.folder = Path(folder)
            problem.pilot = SimpleNamespace(config={'parallel_route_scouts': {
                'enabled': True, 'width': 2, 'user_requested': False}})
            problem.current = candidate
            problem.convergence_state = self.update(candidate=candidate)
            # No scope, proof or grade has passed, and no exam config exists.
            result = asyncio.run(problem.route_scouts())
            self.assertEqual(result['status'], 'not_dispatched')
            self.assertFalse(result['convergence_admission']['allowed'])
            restored = c.ConvergenceStore(folder).load()
            self.assertFalse(restored['last_scout_admission']['allowed'])
            self.assertEqual(restored['phase']['name'], 'converging')


if __name__ == '__main__': unittest.main()
