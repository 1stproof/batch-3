"""Checkpoint selection is explicit; malformed scope pairs never purchase Silver."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p
from pilot_candidate_contract import apply_main_response, candidate_hash, replay_main_responses, checkpoint_finding_diagnostics, CHECKPOINT_FINDING_GUIDANCE
import test_pilot_dual_scope as fixtures
import test_pilot_review_handoff as handoff

class CheckpointContractTests(unittest.TestCase):
    def setUp(self):
        self.candidate = {'proof_markdown': 'Entire proof with every paragraph.', 'ledger': {'rows': [{'id': 'r'}]},
                          'assumption_census': 'All assumptions', 'answer_statement': 'Entire proof',
                          'substantive_sha256': 'must remain', 'sol_tasks': [{'old': 'old task'}]}
        self.binding = candidate_hash(self.candidate)
        self.raw = {'response_type': 'blocked_checkpoint', 'selected_candidate_sha256': self.binding,
                    'checkpoint_metadata': {'reason': 'Need independent exact-task approval'},
                    'proposed_work': {'sol_tasks': [], 'python_probe': '', 'lean_probe': '', 'lean_probe_rows': []},
                    'unreviewed_findings': [], 'review_request': 'none'}

    def test_full_artifact_preserved_no_action_and_unknown_bindings_rejected(self):
        current, receipt = apply_main_response(self.raw, {self.binding: self.candidate})
        for key in ('proof_markdown', 'ledger', 'assumption_census', 'substantive_sha256'):
            self.assertEqual(current[key], self.candidate[key])
        self.assertEqual(current['sol_tasks'], [])
        self.assertFalse(receipt['actionable'])
        self.assertEqual(receipt['raw_checkpoint'], self.raw)
        with self.assertRaises(ValueError):
            apply_main_response(self.raw, {})
        bad = copy.deepcopy(self.raw); bad['ledger'] = {'rows': []}
        with self.assertRaises(ValueError):
            apply_main_response(bad, {self.binding: self.candidate})

    def test_exact_new_task_retained_as_new_candidate_without_approval(self):
        task = {'kind': 'lean', 'task': 'Exact inspection only', 'context': 'bounded', 'hypotheses': [],
                'owned_scope': 'one module', 'advisory_hints': 'none', 'acceptance_checks': 'actual diagnostics'}
        self.raw['proposed_work']['sol_tasks'] = [task]
        current, receipt = apply_main_response(self.raw, {self.binding: self.candidate})
        self.assertTrue(receipt['actionable'])
        self.assertEqual(current['sol_tasks'], [task])
        self.assertNotEqual(candidate_hash(current), self.binding)
        self.assertNotIn('approval', receipt)
        self.raw['proposed_work']['python_probe'] = 'print(1)'
        with self.assertRaisesRegex(ValueError, 'independent task approval'):
            apply_main_response(self.raw, {self.binding: self.candidate})

    def test_replay_keeps_legacy_but_never_promotes_new_untyped_response(self):
        rejected = dict(self.candidate, proof_markdown='Short replacement masquerading as full')
        current, known = replay_main_responses([self.candidate, rejected, self.raw], legacy_indices=[0])
        expected, _ = apply_main_response(self.raw, {self.binding: self.candidate})
        self.assertEqual(current, expected)
        self.assertNotIn(candidate_hash(rejected), known)
        current, _ = replay_main_responses([dict(self.candidate, response_type='candidate_update')])
        self.assertEqual(current, self.candidate)

    def test_repeated_checkpoint_ignores_deferred_rounds_but_tracks_actual_execution(self):
        self.raw['review_request'] = 'substantive_reassessment'
        _, checkpoint = apply_main_response(self.raw, {self.binding: self.candidate})
        key = p.checkpoint_request_key(checkpoint, [])
        deferred = {'workers': [{'output': {'status': 'deferred'}}],
                    'main_probe': {'lean': {'status': 'deferred'}}}
        self.assertEqual(key, p.checkpoint_request_key(checkpoint, [deferred, deferred]))
        actual = {'workers': [{'task_id':'worker','execution_receipt':{'name':'q/003-sol-execution','request_id':'worker','answer_sha256':'a'*64},'output': {'status': 'completed', 'findings': 'actual evidence'}}],
                  'main_probe': {'status': 'not_requested'}}
        self.assertNotEqual(key, p.checkpoint_request_key(checkpoint, [actual]))
        self.assertEqual(p.checkpoint_request_key(checkpoint, [actual]),
                         p.checkpoint_request_key(checkpoint, [actual, actual, deferred]))

    def test_substantive_metadata_and_malformed_findings_rejected(self):
        self.raw['checkpoint_metadata']['ledger'] = {'rows': []}
        with self.assertRaises(ValueError):
            apply_main_response(self.raw, {self.binding: self.candidate})
        del self.raw['checkpoint_metadata']['ledger']
        self.raw['unreviewed_findings'] = ['hidden untyped gap']
        with self.assertRaises(ValueError):
            apply_main_response(self.raw, {self.binding: self.candidate})

class MainCheckpointRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.f = handoff.ReviewHandoffTests(); self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.x = self.f.problem
        self.x.pilot.config = {}
        self.x.findings = [{'id': 'old', 'finding': 'still open'}]
        self.x.active_triage = {'old': 'must not authorize new task'}
        self.x.current.update(sol_tasks=[], python_probe='', lean_probe='', lean_probe_rows=[])
        self.raw = {'response_type': 'blocked_checkpoint',
            'selected_candidate_sha256': candidate_hash(self.x.current),
            'checkpoint_metadata': {'reason': 'Preserve full proof and wait for infrastructure'},
            'proposed_work': {'sol_tasks': [], 'python_probe': '', 'lean_probe': '', 'lean_probe_rows': []},
            'unreviewed_findings': [], 'review_request': 'none'}

    def test_main_preserves_full_artifact_and_stores_metadata_separately(self):
        before = copy.deepcopy(self.x.current)
        async def call(*args, **kwargs): return self.f.meta('actual-main'), copy.deepcopy(self.raw)
        self.x.call = call
        asyncio.run(self.x.main_turn('Continue'))
        self.assertEqual(self.x.current['proof_markdown'], before['proof_markdown'])
        self.assertEqual(self.x.current['ledger'], before['ledger'])
        self.assertNotIn('checkpoint_metadata', self.x.current)
        self.assertIsNone(self.x.active_triage)
        self.assertFalse(self.x.last_main_checkpoint['actionable'])
        self.assertEqual(self.x.findings, [{'id': 'old', 'finding': 'still open'}])
        self.assertTrue((self.x.folder / 'main-7-checkpoint.json').exists())

    def test_invalid_selection_corrected_once_in_same_main_then_noop_dedup(self):
        self.raw['review_request'] = 'substantive_reassessment'
        bad = dict(self.raw, selected_candidate_sha256='invalid')
        responses = iter([bad, copy.deepcopy(self.raw), copy.deepcopy(self.raw)])
        calls = []
        async def call(role, instruction, **kwargs):
            calls.append(kwargs)
            return self.f.meta('actual-main'), next(responses)
        self.x.call = call
        asyncio.run(self.x.main_turn('Continue'))
        self.assertEqual(len(calls), 2); self.assertTrue(calls[1]['resume'])
        self.assertTrue(self.x.last_main_checkpoint['actionable'])
        self.x.execution_history.append({'workers': [], 'main_probe': {'status': 'not_requested'}})
        asyncio.run(self.x.main_turn('Continue'))
        self.assertFalse(self.x.last_main_checkpoint['actionable'])


    def test_actionable_schema_and_exhausted_response_preserved_without_mutation(self):
        first=copy.deepcopy(self.raw)
        first['unreviewed_findings']=[{'id':'science','severity':'gap','kind':'mathematical','finding':'exact claim'},
            {'id':'workflow','severity':'gap','kind':'host_gate','finding':'retain administrative history'}]
        second=copy.deepcopy(first)
        for item in second['unreviewed_findings']:item['text']=item.pop('finding')
        before=copy.deepcopy(self.x.current);old_findings=copy.deepcopy(self.x.findings)
        responses=iter([first,second]);calls=[]
        async def call(role,instruction,**kwargs):
            self.x.counter+=1;calls.append((instruction,kwargs))
            return self.f.meta('main'),next(responses)
        self.x.call=call
        with self.assertRaisesRegex(ValueError,r'unreviewed_findings\[0\].finding'):
            asyncio.run(self.x.main_turn('Continue'))
        self.assertEqual(len(calls),2);self.assertTrue(calls[1][1]['resume'])
        self.assertIn(CHECKPOINT_FINDING_GUIDANCE,calls[0][0]);self.assertIn(CHECKPOINT_FINDING_GUIDANCE,calls[1][0])
        self.assertIn('unreviewed_findings[1].kind',calls[1][0])
        self.assertIn(p.encoded(first),calls[1][0])
        diagnostics=[json.loads(path.read_text()) for path in sorted(self.x.folder.glob('main-*-invalid-contract.json'))]
        self.assertEqual(len(diagnostics),2)
        self.assertEqual(diagnostics[0]['raw_response'],first);self.assertEqual(diagnostics[1]['raw_response'],second)
        self.assertTrue(diagnostics[1]['recovery_exhausted'])
        self.assertEqual(self.x.current,before);self.assertEqual(self.x.findings,old_findings)
        self.assertFalse((self.x.folder/'current-candidate.json').exists())

    def test_diagnostics_preserve_previous_acceptance_language(self):
        import itertools
        def old_valid(f):
            return isinstance(f,dict) and isinstance(f.get('id'),str) and bool(f['id']) and f.get('severity') in ('fatal','gap','nitpick') and f.get('kind') in ('mathematical','certificate') and isinstance(f.get('finding'),str) and bool(f['finding'])
        good={'id':'f','severity':'gap','kind':'mathematical','finding':'exact'}
        examples=[None,[],True,'finding',good,{**good,'extra':{'unchanged':'retained'}},{**good,'id':' ','finding':' \r\n'}]
        for field in good:
            missing=copy.deepcopy(good);del missing[field];examples.append(missing)
            for value in (None,[],{},True,1,1.0,'','unknown'):
                examples.append({**good,field:value})
        for example in examples:
            self.assertEqual(not checkpoint_finding_diagnostics([example]),bool(old_valid(example)),repr(example))

    def test_finding_diagnostics_are_literal_no_alias_or_classification(self):
        findings=[{'id':'f','severity':'gap','kind':'host_gate','text':'exact original whitespace \r\n'}]
        before=copy.deepcopy(findings);errors=checkpoint_finding_diagnostics(findings)
        self.assertEqual([e['path'] for e in errors],['unreviewed_findings[0].kind','unreviewed_findings[0].finding'])
        self.assertEqual(errors[0]['actual'],'host_gate');self.assertFalse(errors[1]['present'])
        self.assertEqual(findings,before)
        self.assertEqual(checkpoint_finding_diagnostics([{'id':'f','severity':'gap','kind':'certificate','finding':'text'}]),[])


class ScopeProtocolTests(fixtures.DualScopeTests):
    def run_reports(self, reports):
        self.prompts = []
        reports = iter(reports)
        async def call(role, instruction, **kwargs):
            self.prompts.append((role, instruction))
            meta = self.f.meta('review-' + str(len(self.prompts)))
            meta['prompt_sha256'] = p.sha(instruction)
            return meta, next(reports)
        self.x.call = call
        return asyncio.run(self.x.validate_candidate(self.f.meta('proof'), self.review))

    def test_actual_extra_findings_key_retries_entire_blind_pair_before_silver(self):
        invalid = handoff.scope_report(); invalid['findings']['verification_language'] = 'not in schema'
        with patch('original_scope.audit_original_scope', return_value=[]), patch('original_scope._audit_original_scope', return_value=[]):
            _, feedback = self.run_reports([invalid, handoff.scope_report(), handoff.scope_report(),
                                           handoff.scope_report(), {'verdict': 'SILVER', 'gaps': []}])
        self.assertEqual([role for role, _ in self.prompts], ['scope-review'] * 4 + ['silver-review'])
        self.assertEqual(self.prompts[0][1], self.prompts[1][1])
        self.assertEqual(self.prompts[2][1], self.prompts[3][1])
        self.assertNotIn('not in schema', self.prompts[2][1])
        raw = json.loads((self.x.folder / 'revision-007-scope-1-raw.json').read_text())
        self.assertEqual(raw['report'], invalid)
        self.assertFalse(raw['acceptance_authority'])
        self.assertEqual(feedback['host_review_receipts']['scopes'][0]['session_id'], 'review-3')

    def test_valid_substantive_rejection_with_malformed_peer_never_retries(self):
        _, feedback = self.run_reports([handoff.scope_report('fail', ['real missing clause']), []])
        self.assertEqual(len(self.prompts), 2)
        self.assertEqual(feedback['scopes'][0]['gaps'], ['real missing clause'])
        self.assertEqual(feedback['silver']['status'], 'not_dispatched')

    def test_coverage_failure_or_explicit_malformed_dissent_never_retries(self):
        gap = handoff.scope_report()
        gap['coverage'] = [{'clause_id': 'c', 'root': 'answer', 'result': 'gap',
                            'explanation': 'A substantive clause remains unproved.'}]
        _, feedback = self.run_reports([gap, []])
        self.assertEqual(len(self.prompts), 2)
        self.assertEqual(feedback['silver']['status'], 'not_dispatched')
        gap['findings']['extra_key'] = 'structural defect must not erase coverage gap'
        _, feedback = self.run_reports([gap, []])
        self.assertEqual(len(self.prompts), 2)
        dissent = handoff.scope_report('unknown'); dissent['extra_field'] = 'schema defect too'
        _, feedback = self.run_reports([dissent, []])
        self.assertEqual(len(self.prompts), 2)

    def test_second_malformed_pair_stops_and_preserves_all_four(self):
        self.x.final_assessment_history = [{'candidate_sha256': p.sha(p.encoded(self.x.current))}]
        _, feedback = self.run_reports([[], {}, [], {}])
        self.assertEqual(len(self.prompts), 4)
        self.assertTrue(feedback['blocked_checkpoint_required'])
        self.assertTrue(self.x.final_assessment_history[0]['final_validation']['scope_protocol_exhausted'])
        self.assertEqual(len(list(self.x.folder.glob('*scope-*-raw.json'))), 4)
