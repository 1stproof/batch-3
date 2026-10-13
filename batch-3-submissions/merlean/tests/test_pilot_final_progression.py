"""Final assessment commissioning is separate from mathematical acceptance."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p

class AdmittedMock(AsyncMock):
    """Simulate the real transport's concrete admission callback before dispatch."""
    async def _execute_mock_call(self, *args, **kwargs):
        callback = kwargs.get('on_admitted')
        if callback:
            callback()
        return await super()._execute_mock_call(*args, **kwargs)



class FinalProgressionTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.x = x = object.__new__(p.Problem)
        x.folder = Path(tmp.name); x.session = 'main'; x.implementers = ['main']
        x.calls = []; x.counter = 1; x.findings = []; x.finding_history = []
        x.execution_history = []; x.triage_history = []; x.final_assessment_history = []
        x.advisory_scope_history = []; x.dossier = {}; x.statement = 'Every requested case'
        x.current = {'proof_markdown': 'Exact candidate', 'ledger': {'rows': [
            {'id': 'composition', 'uses': [], 'class': 'NOVEL'}]}}
        x.status = Mock(); x.pilot = SimpleNamespace(policy=lambda _: 'POLICY', config={})
        x.active_triage = None

    def meta(self, role):
        return {'name': 'q/' + role, 'session_id': role, 'status': 'completed',
                'model_actual': p.ASTRA, 'model_verified': True, 'fresh_session': True,
                'resume_session': None, 'prompt_sha256': 'actual-prompt',
                'answer_sha256': 'actual-answer', 'request_id': 'actual-request'}

    def finding(self, ident='old', **extra):
        return {'id': ident, 'severity': 'gap', 'kind': 'mathematical',
                'finding': 'Historical route obligation', 'what_would_resolve': 'Establish it', **extra}

    def review(self, **extra):
        return {'verdict': 'PASS_COMPLETE_PROOF', 'gaps': [], 'unresolved_findings': [],
                'resolved_ids': [], 'triaged_rows': [], 'triage_decisions': [
                    {'row_id': 'composition', 'selected': False, 'trigger': 'none',
                     'reason': 'No L3 trigger', 'goal_relevance': 'Composition', 'inference_ready': True}], **extra}

    def disposition(self, ident='old', status='inactive_historical', **extra):
        return {'id': ident, 'candidate_sha256': p.sha(p.encoded(self.x.current)),
                'status': status, 'rationale': 'Independent current-candidate analysis',
                'evidence': 'Old construction replaced; every current dependency checked',
                'direct_consumers': [], 'transitive_consumers': [],
                'no_reuse_without_reassessment': True, **extra}

    def projection(self, findings, dispositions, **review):
        return p.finding_projection(findings, self.review(finding_dispositions=dispositions, **review),
                                    self.x.current, {})

    def test_readiness_commissions_scope_and_comprehensive_but_cannot_accept(self):
        x = self.x
        focused = self.review(verdict='INCOMPLETE', mathematically_ready=True,
            gaps=['Future final audits'], unresolved_findings=[self.finding(kind='certificate')])
        x.call = AdmittedMock(return_value=(self.meta('scope'), {'verdict': 'unknown', 'gaps': ['Check coverage']}))
        x.review_candidate = AsyncMock(return_value=(self.meta('proof'), focused))
        result = asyncio.run(x.commission_final_assessment(focused))
        self.assertFalse(p.proof_pass(result[1]))
        x.review_candidate.assert_awaited_once_with('comprehensive')
        self.assertIn('BEFORE proof acceptance', x.call.call_args.args[1])
        self.assertEqual(x.final_assessment_history[0]['scope']['verdict'], 'unknown')
        self.assertIsNone(asyncio.run(x.commission_final_assessment(focused)))
        x.current['notes'] = 'New display note'
        self.assertIsNone(asyncio.run(x.commission_final_assessment(focused)))
        # Exact receipt still describes the originally supplied bytes.
        self.assertNotEqual(x.final_assessment_history[0]['candidate_sha256'], p.sha(p.encoded(x.current)))
        restored = json.loads(json.dumps(x.final_assessment_history))
        x.final_assessment_history = restored
        self.assertIsNone(asyncio.run(x.commission_final_assessment(focused)))
        x.current['proof_markdown'] += ' Substantive repair'
        self.assertIsNotNone(asyncio.run(x.commission_final_assessment(focused)))

    def test_failed_commission_is_reserved_before_dispatch(self):
        x = self.x; x.call = AdmittedMock(side_effect=RuntimeError('transport failed'))
        with self.assertRaises(RuntimeError):
            asyncio.run(x.commission_final_assessment({'mathematically_ready': True}))
        self.assertEqual(x.final_assessment_history[0]['status'], 'commissioned')
        self.assertIsNone(asyncio.run(x.commission_final_assessment({'mathematically_ready': True})))
        x.call.assert_awaited_once()

    def test_unready_and_truthy_string_never_commission(self):
        self.x.call = AdmittedMock()
        for value in (False, 'true', 1, None):
            self.assertIsNone(asyncio.run(self.x.commission_final_assessment({'mathematically_ready': value})))
        self.x.call.assert_not_awaited()

    def test_all_historical_ids_preserved_and_unknown_missing_fail_closed(self):
        findings = [self.finding('inactive'), self.finding('missing'), self.finding('unknown')]
        result = self.projection(findings, [self.disposition('inactive'), self.disposition('unknown', 'unknown')],
                                 resolved_ids=['missing'])
        self.assertFalse(p.proof_pass(result))
        self.assertEqual({f['id'] for f in result['unresolved_findings']}, {'missing', 'unknown'})
        account = result['finding_accountability']
        self.assertEqual(account['original_findings'], findings)
        self.assertEqual(account['history_sha256'], p.sha(p.encoded(findings)))

    def test_inactive_needs_justification_no_consumer_and_no_reuse(self):
        for change in ({'evidence': ''}, {'rationale': ''}, {'direct_consumers': ['composition']},
                       {'transitive_consumers': ['composition']}, {'no_reuse_without_reassessment': False},
                       {'candidate_sha256': 'stale'}):
            with self.subTest(change=change):
                self.assertFalse(p.proof_pass(self.projection([self.finding()], [self.disposition(**change)])))
        for finding in (self.finding(row_id='composition'), self.finding(step='composition')):
            self.assertFalse(p.proof_pass(self.projection([finding], [self.disposition()])))
        self.x.current['ledger']['rows'][0]['uses'] = ['old']
        self.assertFalse(p.proof_pass(self.projection([self.finding()], [self.disposition()])))

    def test_real_shape_legacy_certificates_workflow_only_and_actual_receipts(self):
        # Original certificate kinds and composition row tags mirror the observed
        # circular prerequisite, without carrying private mathematics into fixtures.
        findings = [self.finding(g, kind='certificate', row_id='composition') for g in
                    ('provenance', 'scope', 'grade', 'completion')]
        ds = [self.disposition(ident, 'pending_host_gate' if ident in ('scope', 'provenance') else 'downstream_obligation',
                gate=gate, no_mathematical_or_certificate_claim=True,
                row_association_explanation='Composition location tag; this finding asks only for the named host audit')
              for ident, gate in [('provenance', 'proof_review_dispatch'), ('scope', 'original_scope_assessment'),
                                  ('grade', 'silver_acceptance'), ('completion', 'campaign_completion')]]
        raw = self.review(finding_dispositions=ds)
        receipt = self.x.review_receipt(self.meta('actual-independent'))
        blocked = p.finding_projection(findings, raw, self.x.current, {})
        self.assertFalse(p.proof_pass(blocked))
        # Candidate-supplied fake evidence cannot discharge host obligations.
        raw['host_receipts'] = {'original_scope_assessment': receipt, 'proof_review_dispatch': receipt}
        self.assertFalse(p.proof_pass(p.finding_projection(findings, raw, self.x.current, {})))
        result = p.finding_projection(findings, raw, self.x.current,
            {'original_scope_assessment': receipt, 'proof_review_dispatch': receipt})
        self.assertTrue(p.proof_pass(result))
        self.assertEqual(result['resolved_ids'], [])
        self.assertEqual(result['finding_accountability']['original_findings'], findings)
        self.assertIn('still_required', result['finding_accountability']['dispositions'][2]['authority'])
        self.x.current['proof_markdown'] += ' changed'
        self.assertFalse(p.proof_pass(p.finding_projection(findings, raw, self.x.current,
            {'original_scope_assessment': receipt, 'proof_review_dispatch': receipt})))

    def test_active_math_cannot_hide_as_gate_and_selected_certificates_still_block(self):
        for status, gate in [('pending_host_gate', 'proof_review_dispatch'),
                             ('downstream_obligation', 'silver_acceptance')]:
            ds = self.disposition(status=status, gate=gate, no_mathematical_or_certificate_claim=True,
                row_association_explanation='Attempted relabel')
            result = p.finding_projection([self.finding(row_id='composition')],
                self.review(finding_dispositions=[ds]), self.x.current,
                {'proof_review_dispatch': self.x.review_receipt(self.meta('actual'))})
            self.assertFalse(p.proof_pass(result))
        # An actual missing certificate is not a procedural claim: no semantic waiver.
        ds = self.disposition(status='downstream_obligation', gate='silver_acceptance',
            no_mathematical_or_certificate_claim=False, row_association_explanation='Lean evidence required')
        self.assertFalse(p.proof_pass(self.projection([self.finding(kind='certificate')], [ds])))

    def test_incomplete_never_promoted_by_projection(self):
        result = self.projection([self.finding()], [self.disposition()], verdict='INCOMPLETE')
        self.assertFalse(p.proof_pass(result))
        result = self.projection([self.finding()], [self.disposition()], gaps=['Real mathematical gap'])
        self.assertFalse(p.proof_pass(result))

    def test_effective_history_and_independence_and_mutation(self):
        x = self.x; x.findings = [self.finding()]
        x.call = AdmittedMock(return_value=(self.meta('reviewer'), self.review(finding_dispositions=[self.disposition()])))
        meta, result = asyncio.run(x.review_candidate('comprehensive'))
        self.assertTrue(p.proof_pass(result)); self.assertEqual(x.findings, [self.finding()])
        self.assertEqual(x.finding_history[0]['finding'], self.finding())
        self.assertIn('finding_accountability', json.loads(next(x.folder.glob('*effective.json')).read_text()))
        x.current['notes'] = 'Even exact input notes changed'
        with self.assertRaisesRegex(ValueError, 'comprehensive'):
            asyncio.run(x.validate_candidate(meta, result))
        x.call = AdmittedMock(return_value=(self.meta('main'), self.review(finding_dispositions=[self.disposition()])))
        with self.assertRaisesRegex(ValueError, 'independent Astra'):
            asyncio.run(x.review_candidate('comprehensive'))

    def test_unknown_nitpick_keeps_severity_but_blocks_protocol_acceptance(self):
        finding = self.finding(severity='nitpick')
        for dispositions in ([], [self.disposition(status='unknown')],
                             [self.disposition(status='active', candidate_sha256='stale')]):
            result = self.projection([finding], dispositions)
            self.assertTrue(p.proof_pass(result))  # Original mathematical predicate unchanged.
            self.assertEqual(result['unresolved_findings'], [finding])
            self.assertFalse(result['finding_accountability']['complete'])
            result['review_mode'] = 'comprehensive'
            self.x.active_triage = {'candidate_binding': p.triage_binding(self.x.current),
                'review_mode': 'comprehensive', 'receipt': {'session_id': 'proof'}}
            self.x.call = AdmittedMock()
            with self.assertRaisesRegex(ValueError, 'comprehensive'):
                asyncio.run(self.x.validate_candidate(self.meta('proof'), result))
            self.x.call.assert_not_awaited()
        result = self.projection([finding], [self.disposition(status='active')])
        self.assertTrue(result['finding_accountability']['complete'])
        self.assertTrue(p.proof_pass(result))
        self.assertEqual(result['unresolved_findings'], [finding])

    def test_same_id_fresh_fatal_never_downgraded_to_historical_nitpick(self):
        old = self.finding(severity='nitpick')
        fresh = self.finding(severity='fatal', finding='New fatal mathematical objection')
        result = self.projection([old], [self.disposition(status='active')],
                                 unresolved_findings=[fresh])
        self.assertFalse(p.proof_pass(result))
        self.assertEqual(result['unresolved_findings'], [fresh])
        self.assertEqual(result['finding_accountability']['original_findings'], [old, fresh])
        old['severity'] = 'gap'; fresh['severity'] = 'gap'
        result = self.projection([old], [self.disposition(status='unknown')], unresolved_findings=[fresh])
        self.assertEqual(result['unresolved_findings'], [fresh])

    def test_rewriting_row_reference_cannot_make_live_finding_inactive(self):
        old = self.finding(row_id='composition')
        fresh = self.finding()
        result = self.projection([old], [self.disposition()], unresolved_findings=[fresh])
        self.assertFalse(p.proof_pass(result))
        self.assertEqual(result['finding_accountability']['original_findings'], [old, fresh])

    def test_same_id_math_cannot_be_rewritten_as_procedural_certificate(self):
        old = self.finding(kind='mathematical', row_id='composition')
        fresh = self.finding(kind='certificate', row_id='composition')
        disposition = self.disposition(status='downstream_obligation', gate='silver_acceptance',
            no_mathematical_or_certificate_claim=True, row_association_explanation='Forged relabel')
        result = self.projection([old], [disposition], unresolved_findings=[fresh])
        self.assertFalse(p.proof_pass(result))
        self.assertEqual(result['finding_accountability']['original_findings'], [old, fresh])

    def test_host_gate_cannot_use_generic_inactive_or_resolved(self):
        for status in ('inactive_historical', 'resolved'):
            result = self.projection([self.finding(kind='host_gate', gate='proof_review_dispatch')],
                                     [self.disposition(status=status)])
            self.assertFalse(p.proof_pass(result))

    def test_stopped_continuation_retains_attempts_without_lifetime_lockout(self):
        x = self.x
        key = p.assessment_key(x.current, [])
        history = [{'binding_key': key, 'execution_identity_version':2, 'candidate_sha256': p.sha(p.encoded(x.current)),
                    'status': 'commissioned', 'attempts': 1}]
        saved = {'current': x.current, 'findings': [], 'main_session': 'main',
                 'original_sha256': p.sha(b'original'), 'implementers': ['main'], 'calls': [],
                 'errors': [], 'dossier': {}, 'counter': 1, 'execution_history': [],
                 'final_assessment_history': history}
        checkpoint = x.folder / 'continuation-checkpoint.json'
        ref = p.write(checkpoint, {'problems': {'q': saved}})
        x.ident = 'q'; x.original_bytes = b'original'
        x.pilot.root = x.folder; x.pilot.config = {'continuation_checkpoint': ref}
        x.restore_checkpoint()
        self.assertTrue(x.final_assessment_history[0]['retry_after_reconciliation'])
        x.call = AdmittedMock(return_value=(self.meta('scope'), {'verdict': 'unknown'}))
        x.review_candidate = AsyncMock(side_effect=RuntimeError('second interrupted attempt'))
        with self.assertRaises(RuntimeError):
            asyncio.run(x.commission_final_assessment({'mathematically_ready': True}))
        self.assertEqual(x.final_assessment_history[0]['attempts'], 2)
        saved['final_assessment_history'] = x.final_assessment_history
        x.pilot.config['continuation_checkpoint'] = p.write(checkpoint, {'problems': {'q': saved}})
        x.restore_checkpoint()
        with self.assertRaisesRegex(RuntimeError, 'second interrupted attempt'):
            asyncio.run(x.commission_final_assessment({'mathematically_ready': True}))
        self.assertEqual(x.final_assessment_history[0]['attempts'], 3)
        self.assertEqual(x.call.await_count, 2)

    def test_scope_receipt_and_readiness_never_bypass_final_proof_gate(self):
        self.x.call = AdmittedMock()
        self.x.active_triage = {'candidate_binding': p.triage_binding(self.x.current),
            'review_mode': 'comprehensive', 'receipt': {'session_id': 'proof'}}
        for review in (self.review(verdict='INCOMPLETE', mathematically_ready=True, review_mode='comprehensive'),
                       self.review(review_mode='focused')):
            with self.assertRaisesRegex(ValueError, 'comprehensive'):
                asyncio.run(self.x.validate_candidate(self.meta('proof'), review))
        self.x.call.assert_not_awaited()


if __name__ == '__main__': unittest.main()
