"""Finite exact evidence delivery and negative-only incomplete reviews."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, Mock
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_document_tools as d
import pilot_document_recovery as recovery
import pilot_convergence as convergence
import codex_pilot as p
from codex_transport import _tool_output_part


class RequiredDeliveryTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        self.texts = {'first': ('α漢字\r\n' * 30000) + 'last', 'second': 'small exact record\n'}
        entries = {}
        for ident, text in self.texts.items():
            path = self.root / (ident + '.txt'); path.write_bytes(text.encode())
            entries[ident] = {'path': str(path), 'sha256': d.digest(path.read_bytes()), 'media_type': 'text/plain'}
            if len(text) > 16000:
                for start in range(0, len(text), 16000):
                    end = min(start + 16000, len(text)); chunk = text[start:end]
                    path = self.root / f'{ident}-{start}.txt'; path.write_bytes(chunk.encode())
                    entries[f'{ident}::chunk:{start}:{end}'] = {'path': str(path), 'sha256': d.digest(path.read_bytes()), 'media_type': 'text/plain'}
        self.scope = {'schema_version': 1, 'mode': 'review', 'problem_id': 'p', 'original_sha256': 'a'*64,
            'main_session': 'main', 'store_root': str(self.root), 'readonly_artifacts': entries,
            'required_artifact_ids': list(self.texts), 'inline_artifact_ids': [],
            'producer': {'stage': 'p/1', 'request_id': 'req', 'session_id': None},
            'receipt_path': str(self.root / 'operations.jsonl')}
        self.server = d.DocumentTools(self.scope)
        self.events = []; self.calls = []; self.outputs = []

    def page(self, index, clipped=False):
        args = {'page': index}; call = 'call-' + str(len(self.calls))
        result = self.server.call('read_required_evidence', args, len(self.calls), {'callId': call, 'sessionId': 'reviewer'})
        self.assertFalse(result['isError'])
        text = result['content'][0]['text']; visible = text
        if clipped:
            visible = text[:20] + '…' + str(len(text)-40) + ' chars truncated…' + text[-20:]
        self.events.append({'type': 'item.completed', 'item': {'type': 'mcp_tool_call', 'server': d.SERVER,
            'tool': 'read_required_evidence', 'arguments': args, 'result': {'content': result['content'], 'structured_content': None},
            'error': None, 'status': 'completed'}})
        self.calls.append({'namespace': d.NAMESPACE, 'name': 'read_required_evidence', 'call_id': call,
            'arguments_canonical_sha256': d.digest(d.encoded(args).encode())})
        self.outputs.append({'call_id': call, 'output_format': 'list', 'text_parts': [
            {**_tool_output_part(t), 'type': 'input_text', 'keys': ['text', 'type']}
            for t in ['Wall time: 0.01 seconds\nOutput:', visible]]})
        return json.loads(text)

    def audit(self):
        return d.audit_operations(self.scope, self.events, self.calls, 'reviewer', self.outputs)

    def test_all_pages_reconstruct_exact_order_unicode_and_short_final_page(self):
        plan = d.required_read_plan(self.scope); parts = {k: [] for k in self.texts}
        self.assertEqual(len(plan), 4)
        for index in range(len(plan)):
            value = self.page(index)
            self.assertEqual(value['required_page']['page'], index)
            self.assertEqual(value['required_page']['next_page'], index+1 if index+1 < len(plan) else None)
            parts[value['artifact_id']].append(value['text'])
            self.assertLessEqual(len(value['text']), 64000)
        self.assertEqual({k: ''.join(v) for k, v in parts.items()}, self.texts)
        audit = self.audit(); self.assertEqual(audit['status'], 'PASS'); self.assertTrue(audit['required_material_delivered'])
        self.assertEqual(d.required_read_progress(self.scope, audit['artifact_coverage'])['missing_pages'], [])
        self.assertTrue(all(audit['artifact_coverage'].values()))

    def test_skipped_middle_page_stays_missing_despite_terminal_pointer(self):
        for page in (0, 2, 3): self.page(page)
        audit = self.audit()
        self.assertEqual(audit['status'], 'PASS'); self.assertFalse(audit['required_material_delivered'])
        self.assertEqual(d.required_read_progress(self.scope, audit['artifact_coverage'])['missing_pages'], [1])
        self.assertFalse(audit['artifact_coverage']['first::chunk:64000:80000'])
        self.assertTrue(audit['artifact_coverage']['first::chunk:0:16000'])

    def test_clipped_or_altered_page_never_credits_parent_or_children(self):
        self.page(0, clipped=True)
        audit = self.audit(); self.assertEqual(audit['status'], 'PASS')
        self.assertTrue(audit['delivery_errors']); self.assertFalse(any(audit['artifact_coverage'].values()))
        self.outputs[0]['text_parts'][1]['sha256'] = 'f'*64
        self.outputs[0]['text_parts'][1]['clippings'] = []
        self.assertEqual(self.audit()['status'], 'FAIL')

    def test_duplicate_page_does_not_cover_unseen_text_and_fresh_has_zero_credit(self):
        self.page(0); self.page(0)
        audit = self.audit(); self.assertFalse(audit['required_material_delivered'])
        self.assertEqual(d.required_read_progress(self.scope, audit['artifact_coverage'])['missing_pages'], [1, 2, 3])
        fresh = {**self.scope, 'receipt_path': str(self.root / 'fresh.jsonl')}
        self.assertFalse(any(d.audit_operations(fresh, [], [], 'new-reviewer', [])['artifact_coverage'].values()))

    def test_invalid_page_or_main_role_cannot_expand_scope(self):
        for i, args in enumerate(({'page': True}, {'page': -1}, {'page': 4}, {'page': 0, 'path': '/etc/passwd'})):
            result = self.server.call('read_required_evidence', args, i, {'callId': str(i), 'sessionId': 'reviewer'})
            self.assertTrue(result['isError'])
        self.assertFalse(d.valid_arguments('read_required_evidence', {'page': 0}, 'main'))
        self.assertNotIn('read_required_evidence', [t['name'] for t in d.tool_definitions('main')])

    def test_changed_parent_or_chunk_cannot_be_delivered(self):
        entry = self.scope['readonly_artifacts']['first::chunk:0:16000']
        Path(entry['path']).write_text('forged')
        with self.assertRaises(ValueError): d.required_read_plan(self.scope)
        result = self.server.call('read_required_evidence', {'page': 0}, 1, {'callId': 'x', 'sessionId': 'reviewer'})
        self.assertTrue(result['isError'])

    def test_empty_plan_and_empty_required_artifact_are_distinct(self):
        self.assertEqual(d.required_read_plan({**self.scope, 'required_artifact_ids': []}), [])
        path = self.root/'empty'; path.write_bytes(b'')
        scope = {**self.scope, 'readonly_artifacts': {'empty': {'path': str(path), 'sha256': d.digest(b''), 'media_type': 'text/plain'}}, 'required_artifact_ids': ['empty']}
        self.assertEqual(len(d.required_read_plan(scope)), 1)
        self.assertEqual(d.required_read_progress(scope, {})['missing_pages'], [0])

    def test_recovery_carries_complete_chunks_from_page_only_same_session(self):
        self.page(0); audit = self.audit()
        inherited = {'session_id': 'reviewer', 'full_artifact_ids': [k for k,v in audit['artifact_coverage'].items() if v]}
        fresh = {**self.scope, 'receipt_path': str(self.root/'recovery.jsonl')}
        empty = d.audit_operations(fresh, [], [], 'reviewer', [])
        merged = recovery.inherit_coverage(empty, inherited, scope=fresh, actual_session='reviewer')
        self.assertEqual(d.required_read_progress(fresh, merged['artifact_coverage'])['missing_pages'], [1,2,3])
        self.assertFalse(merged['required_material_delivered'])
        with self.assertRaises(ValueError): recovery.inherit_coverage(empty, inherited, scope=fresh, actual_session='fresh')


class ReviewAuthorityTests(unittest.TestCase):
    def test_missing_delivery_is_not_convergence_success_or_math_gap(self):
        x = p.Problem.__new__(p.Problem); x.documents_enabled = lambda: True
        x.record_convergence_observation = Mock()
        review = {'verdict': 'INCOMPLETE', 'relied_on_artifact_ids': [], 'needed_artifact_ids': []}
        audit = {'status': 'PASS', 'required_material_delivered': False, 'artifact_coverage': {'all': False}, 'required_artifact_coverage': {'all': False}}
        x.check_review_delivery({'document_audit': audit}, review)
        observation = x.record_convergence_observation.call_args.args[1]
        self.assertFalse(observation['passed'])
        self.assertEqual(observation['deficits'][0]['kind'], 'required_evidence_not_delivered')
        review['verdict'] = 'PASS_COMPLETE_PROOF'
        with self.assertRaises(ValueError): x.check_review_delivery({'document_audit': audit}, review)

    def test_negative_effective_report_preserves_old_objection_and_raw_positive_claims(self):
        prior = [{'id': 'old', 'severity': 'gap', 'kind': 'certificate', 'finding': 'actual object certificate missing', 'what_would_resolve': 'exact certificate'}]
        raw = {'verdict': 'INCOMPLETE', 'gaps': [], 'resolved_ids': ['old'], 'unresolved_findings': [],
            'mathematically_ready': True, 'approved_research_tasks': [0], 'approved_lean_tasks': [1],
            'triage_decisions': [{'row_id': 'r', 'selected': False}], 'finding_dispositions': [{'id': 'old', 'status': 'resolved'}]}
        original = copy.deepcopy(raw)
        effective = p.negative_delivery_review(prior, raw, {'required_artifact_coverage': {'all': False}})
        self.assertEqual(raw, original); self.assertEqual(effective['unresolved_findings'], prior)
        for field in ('resolved_ids', 'approved_research_tasks', 'approved_lean_tasks', 'finding_dispositions', 'triage_decisions'):
            self.assertEqual(effective[field], [])
        self.assertFalse(effective['mathematically_ready']); self.assertFalse(effective['positive_authority'])
        self.assertEqual(effective['delivery_deficit']['raw_review_sha256'], p.sha(p.encoded(raw)))
        collision = {**raw, 'resolved_ids': [], 'unresolved_findings': [{**prior[0], 'severity': 'nitpick', 'kind': 'host_gate', 'finding': 'downgrade'}]}
        preserved = p.negative_delivery_review(prior, collision, {'required_artifact_coverage': {'all': False}})
        self.assertEqual(preserved['unresolved_findings'], prior)
        self.assertEqual(preserved['unapplied_finding_observations'], collision['unresolved_findings'])
        for change in ({'row_id': 'other'}, {'finding': 'weaker statement'}, {'kind': 'certificate'}, {'severity': 'nitpick'}):
            variant = {**raw, 'resolved_ids': [], 'unresolved_findings': [{**prior[0], **change}]}
            self.assertEqual(p.negative_delivery_review(prior, variant, {'required_artifact_coverage': {'all': False}})['unresolved_findings'], prior)
        claimed = {**raw, 'positive_authority': False, 'review_mode': 'comprehensive'}
        self.assertNotEqual(convergence._review_deficits(claimed, 'receipt')[0]['status'], 'closed')

    def test_real_review_publication_withholds_authority_without_retry_or_triage_erasure(self):
        import test_pilot_final_progression as fixtures
        f = fixtures.FinalProgressionTests(); f.setUp(); self.addCleanup(f.doCleanups); x = f.x
        x.pilot.root = x.folder.resolve(); x.ident = 'q'
        x.folder = x.pilot.root / 'campaign/problems/q'; x.folder.mkdir(parents=True)
        x.documents_enabled = lambda: True; x.document_submission = lambda: {}
        x.document_current = lambda: {'status': 'submitted'}
        x.review_context = lambda packet: ('exact immutable inputs', {})
        raw = f.review(verdict='INCOMPLETE', gaps=[], mathematically_ready=True, approved_research_tasks=[999])
        raw.update(relied_on_artifact_ids=[], needed_artifact_ids=['all'])
        meta = {**f.meta('fresh'), 'document_audit': {'status': 'PASS', 'required_material_delivered': False,
            'required_artifact_coverage': {'all': False}, 'artifact_coverage': {'all': False}}}
        x.call = AsyncMock(return_value=(meta, raw)); x.triage_history = [{'decisions': [{'row_id': 'composition', 'selected': True}]}]
        before = copy.deepcopy(x.triage_history)
        _, effective = asyncio.run(x.review_candidate('focused'))
        x.call.assert_awaited_once(); self.assertEqual(x.triage_history, before); self.assertIsNone(x.active_triage)
        self.assertFalse(effective['positive_authority']); self.assertTrue(list(x.folder.glob('*effective.json')))
        self.assertIsNone(asyncio.run(x.commission_final_assessment(effective)))

    def test_delivery_omission_preserves_banked_domains_but_new_adverse_finding_reopens(self):
        import test_pilot_convergence as fixtures
        f = fixtures.ConvergenceTests(); f.setUp()
        review = {**f.review, 'triage_decisions': []}
        state = f.update(review=f.observed(review, 1), certification=f.observed({'passed': True, 'deficits': []}))
        key = convergence.digest(f.candidate)
        old = copy.deepcopy(state['candidates'][key]['deficits'])
        partial = {**review, 'verdict': 'INCOMPLETE', 'positive_authority': False, 'mathematically_ready': False}
        updated = f.update(state, review=f.observed(partial, 1), delivery=f.observed({'passed': False, 'deficits': ['unread exact evidence']}))
        record = updated['candidates'][key]
        self.assertEqual(record['deficits']['mathematical'], old['mathematical'])
        self.assertEqual(record['deficits']['certification'], old['certification'])
        self.assertEqual(record['deficits']['delivery']['status'], 'open')
        self.assertEqual(convergence.compact_context(updated)['next_eligible_action'], 'complete_required_evidence_delivery')
        adverse = {**partial, 'unresolved_findings': [{'id': 'new', 'kind': 'mathematical', 'severity': 'gap', 'finding': 'new independently evidenced defect'}]}
        changed = f.update(updated, review=f.observed(adverse, 1))
        self.assertEqual(changed['candidates'][key]['deficits']['mathematical']['status'], 'open')

    def test_existing_noop_dispatch_identity_preserves_actual_failed_execution(self):
        candidate = {'proof_markdown': 'exact', 'ledger': {'rows': [{'id': 'r', 'uses': []}]}, 'revision': 1}
        original = copy.deepcopy(candidate)
        none = {'workers': [{'task': {'kind': 'lean'}, 'output': {'status': 'deferred'}, 'probe': {'status': 'not_requested'}}],
                'main_probe': {'status': 'not_requested'}}
        unchanged = {**candidate, 'revision': 2, 'notes': 'bookkeeping', 'sol_tasks': []}
        key = p.assessment_key(candidate, [])
        self.assertEqual(key, p.assessment_key(unchanged, [none, none]))
        actual = {'workers': [], 'main_probe': {'python': {'status': 'failed', 'stderr': 'new diagnostics', 'source':'x', 'source_ref':{'path':'probes/one-python/source.py','sha256':p.sha('x')}}}}
        self.assertNotEqual(key, p.assessment_key(candidate, [actual]))
        self.assertNotEqual(p.assessment_key(candidate, [actual]), p.assessment_key(candidate, [{'workers':[], 'main_probe':{'python':{**actual['main_probe']['python'], 'stderr':'genuinely different execution result'}}}]))
        for field, value in [('proof_markdown', 'changed'), ('assumptions', ['new']), ('answer_statement', 'changed')]:
            self.assertNotEqual(key, p.assessment_key({**candidate, field: value}, []))
        self.assertEqual(candidate, original); self.assertEqual(none['main_probe']['status'], 'not_requested')


if __name__ == '__main__': unittest.main()
