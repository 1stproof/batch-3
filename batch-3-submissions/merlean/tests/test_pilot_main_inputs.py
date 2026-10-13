"""Exact main feedback survives provider-sized inputs; incomplete reads never submit."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import pilot_document_tools as documents
import pilot_main_inputs as inputs
import pilot_proof_document as store
from codex_transport import _tool_output_part
import test_pilot_review_handoff as fixtures
import test_pilot_continuation as continuation_fixtures


def delivery(server, scope, ids, *, session='actual-main', call_prefix='call'):
    events, persisted, outputs, texts = [], [], [], []
    for number, ident in enumerate(ids, 1):
        args = {'artifact_id': ident, 'sha256': scope['readonly_artifacts'][ident]['sha256']}
        result = server.call('read_artifact', args, f'{call_prefix}-request-{number}',
                             {'callId': f'{call_prefix}-{number}', 'sessionId': session})
        if result['isError']:
            raise AssertionError(result)
        texts.append(json.loads(result['content'][0]['text'])['text'])
        events.append({'type': 'item.completed', 'item': {'tool': 'read_artifact', 'arguments': args,
            'result': {'content': result['content'], 'structured_content': None}, 'error': None, 'status': 'completed'}})
        persisted.append({'namespace': documents.NAMESPACE, 'name': 'read_artifact',
            'call_id': f'{call_prefix}-{number}', 'arguments_canonical_sha256': documents.digest(documents.encoded(args).encode())})
        outputs.append({'call_id': f'{call_prefix}-{number}', 'output_format': 'list', 'text_parts': [
            {**_tool_output_part(text), 'type': 'input_text', 'keys': ['text', 'type']}
            for text in ['Wall time: 0.001 seconds\nOutput:', result['content'][0]['text']]]})
    return documents.audit_operations(scope, events, persisted, session, outputs), texts, (events, persisted, outputs)


def deliver_main_scope(spec, stage_root, name, session):
    """Run real scoped reads/audits while test transport replaces provider calls."""
    stage_root.mkdir(parents=True, exist_ok=True)
    scope, _ = documents.prepare_scope(spec, stage_root,
        {'stage': name, 'request_id': 'synthetic-request', 'session_id': session})
    server = documents.DocumentTools(scope)
    ids = [key for key in scope['readonly_artifacts'] if '::chunk:' in key]
    audit, _, _ = delivery(server, scope, ids, session=session)
    return audit


class MainInputTests(unittest.TestCase):
    def setUp(self):
        fixture = fixtures.ReviewHandoffTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.fixture = fixture
        self.problem = problem = fixture.problem
        problem.pilot.root = fixture.folder.resolve()
        problem.folder = fixture.folder = problem.pilot.root / 'campaign/problems/q'
        problem.folder.mkdir(parents=True)
        (problem.pilot.root / 'original.json').rename(problem.folder / 'original.json')
        problem.implementers = ['actual-main']  # This fixture has no execution worker.
        problem.consecutive_failures = 0
        problem.original_bytes = b'Exact original question'
        problem.statement = problem.original_bytes.decode()
        problem.status = Mock()
        problem.findings = []
        problem.dossier = {}
        problem.pilot.semaphore = asyncio.Semaphore(1)
        problem.pilot.remaining = lambda: 1800
        problem.pilot.config = {'internet_browse': False, 'codex_binary': 'unused', 'proof_document_version': 1}
        problem.pilot.host = fixture.folder / 'host'
        problem.pilot.policy = lambda path: (pilot.REPO / path).read_text()
        self.saved = problem.publish_document(problem.current, fixture.meta('actual-main'))

    def scope(self, text, stage=""):
        built = inputs.build_main_inputs(text, artifact_root=self.fixture.folder / 'artifacts')
        spec = {**self.problem.document_scope(),
                **{key: built[key] for key in ('readonly_artifacts', 'required_artifact_ids', 'inline_artifact_ids')}}
        stage_root = self.fixture.folder / stage
        stage_root.mkdir(parents=True, exist_ok=True)
        scope, _ = documents.prepare_scope(spec, stage_root,
            {'stage': 'q/test', 'request_id': 'test-request', 'session_id': 'actual-main'})
        return built, scope, documents.DocumentTools(scope)

    def test_large_unicode_task_exact_root_and_all_chunks_reconstruct_every_byte(self):
        original = 'Instructions and full required feedback\r\n' + 'α漢字\r\n"duplicate"\\' * 90000
        built, scope, server = self.scope(original)
        self.assertIn('No hash is needed; the host verifies each exact saved version', built['text'])
        self.assertNotIn('with its exact hash below', built['text'])
        root = documents.regular_bytes(scope['readonly_artifacts'][inputs.TASK_ID]['path'])
        self.assertEqual(root, original.encode('utf-8'))
        index = json.loads(documents.regular_bytes(scope['readonly_artifacts'][inputs.INDEX_ID]['path']))
        ids = [chunk['artifact_id'] for chunk in index['chunks']]
        audit, texts, _ = delivery(server, scope, ids)
        self.assertEqual(''.join(texts).encode('utf-8'), root)
        self.assertEqual(documents.digest(root), built['input_sha256'])
        self.assertTrue(all(len(text) <= inputs.READ_CHUNK_CHARACTERS for text in texts))
        inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': audit})
        self.assertLess(len(built['text']), 3000)
        self.assertGreater(len(root), 1_048_576)

    def test_shared_complete_scope_requires_unique_contents_and_exact_inverse(self):
        review = {'status': 'rejected', 'findings': [{'id': 'same', 'version': index,
                  'finding': ('Unique finding %s α漢字 ' % index) * 200} for index in range(12)]}
        feedback = {'latest_review': review, 'history': [copy.deepcopy(review)],
                    'distinct_status': {'status': 'open', 'findings': []}}
        original = 'Exact task\r\nLATEST FEEDBACK:\n' + json.dumps(feedback, ensure_ascii=False,
                    separators=(',', ':')) + '\nExact response contract'
        built, scope, server = self.scope(original)
        delivered = documents.regular_bytes(scope['readonly_artifacts'][inputs.TASK_ID]['path']).decode()
        self.assertNotEqual(delivered, original)
        self.assertEqual(documents.regular_bytes(scope['readonly_artifacts'][inputs.ORIGINAL_ID]['path']), original.encode())
        self.assertEqual(inputs.restore_main_instruction(delivered,
                         expected_original_sha256=built['original_input_sha256']), original)
        index = json.loads(documents.regular_bytes(scope['readonly_artifacts'][inputs.INDEX_ID]['path']))
        self.assertEqual(index['original']['sha256'], built['original_input_sha256'])
        self.assertEqual(index['representation'], built['representation'])
        ids = [chunk['artifact_id'] for chunk in index['chunks']]
        # Reading the original alone cannot bypass required shared-source maps.
        audit, _, _ = delivery(server, scope, [inputs.ORIGINAL_ID])
        with self.assertRaisesRegex(ValueError, 'withheld'):
            inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': audit})
        # Missing a chunk containing distinct shared evidence also cannot submit.
        _, scope, server = self.scope(original, stage="partial")
        audit, _, _ = delivery(server, scope, ids[1:], call_prefix="partial")
        with self.assertRaisesRegex(ValueError, 'withheld'):
            inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': audit})
        _, scope, server = self.scope(original, stage='complete')
        audit, texts, _ = delivery(server, scope, ids, call_prefix='complete')
        self.assertEqual(''.join(texts), delivered)
        inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': audit})

    def test_inverse_failure_prevents_scope_publication_and_dispatch(self):
        with patch.object(inputs, 'restore_main_instruction', side_effect=ValueError('bad inverse')):
            with patch.object(pilot, 'call_stage', new=AsyncMock()) as dispatch:
                with self.assertRaisesRegex(ValueError, 'bad inverse'):
                    asyncio.run(self.problem._call_once('main-repair', 'required feedback',
                                model=pilot.ASTRA, resume=True, timeout=1800))
                dispatch.assert_not_called()

    def test_index_or_missing_final_chunk_cannot_authorize_response(self):
        _, scope, server = self.scope('required exact evidence ' * 2000)
        index = json.loads(documents.regular_bytes(scope['readonly_artifacts'][inputs.INDEX_ID]['path']))
        ids = [inputs.INDEX_ID] + [chunk['artifact_id'] for chunk in index['chunks'][:-1]]
        audit, _, _ = delivery(server, scope, ids)
        self.assertEqual(audit['status'], 'PASS')
        self.assertFalse(audit['required_material_delivered'])
        with self.assertRaisesRegex(ValueError, 'withheld'):
            inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': audit})

    def test_clipped_output_and_timeout_never_satisfy_gate(self):
        _, scope, server = self.scope('complete exact feedback ' * 900)
        ids = [key for key in scope['readonly_artifacts'] if '::chunk:' in key]
        audit, _, (events, persisted, outputs) = delivery(server, scope, ids)
        self.assertTrue(audit['required_material_delivered'])
        with self.assertRaisesRegex(ValueError, 'withheld'):
            inputs.require_main_delivery(scope, {'status': 'timeout_censored', 'document_audit': audit})
        outputs[-1]['text_parts'][-1] = {**_tool_output_part('clipped'), 'type': 'input_text', 'keys': ['text', 'type']}
        altered = documents.audit_operations(scope, events, persisted, 'actual-main', outputs)
        with self.assertRaisesRegex(ValueError, 'withheld'):
            inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': altered})

    def test_wrong_hash_and_changed_chunk_fail_closed(self):
        built, scope, server = self.scope('preserve exact main feedback')
        result = server.call('read_artifact', {'artifact_id': inputs.TASK_ID, 'sha256': '0' * 64}, 1,
                             {'callId': 'wrong-hash', 'sessionId': 'actual-main'})
        self.assertTrue(result['isError'])
        root = Path(built['readonly_artifacts'][inputs.TASK_ID]['path'])
        root.write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'changed'):
            documents.validate_scope(scope)

    def test_dispatch_externalizes_exact_instruction_and_preserves_session(self):
        original = 'Task including feedback and response contract.\r\n' + '必 exact ' * 180000
        async def dispatch(*args, **kwargs):
            prompt, session = args[2], args[5]
            scope = kwargs['document_scope']
            self.assertNotIn(original, prompt)
            self.assertLess(len(prompt), 1_048_576)
            self.assertIn(self.problem.statement, prompt)
            self.assertIn('SHARED WORKFLOW REQUIREMENTS', prompt)
            self.assertEqual(session, 'actual-main')
            self.assertEqual(documents.regular_bytes(scope['readonly_artifacts'][inputs.TASK_ID]['path']), original.encode())
            self.assertEqual(scope['main_session'], session)
            meta = self.fixture.meta(session)
            meta['document_audit'] = {'status': 'PASS', 'required_material_delivered': True,
                                      'required_artifact_coverage': {inputs.TASK_ID: True}}
            return meta, {'response_type': 'draft_checkpoint'}
        with patch.object(pilot, 'call_stage', new=AsyncMock(side_effect=dispatch)):
            asyncio.run(self.problem._call_once('main-repair', original, model=pilot.ASTRA,
                                               resume=True, timeout=1800))

    def test_missing_resumed_proof_store_refuses_inline_fallback(self):
        (self.problem.folder / 'proof-current.json').unlink()
        with patch.object(pilot, 'call_stage', new=AsyncMock()) as dispatch:
            with self.assertRaisesRegex(ValueError, 'refusing inline fallback'):
                asyncio.run(self.problem._call_once('main-repair', 'required feedback',
                                                   model=pilot.ASTRA, resume=True, timeout=1800))
            dispatch.assert_not_called()

    def test_all_response_types_require_delivery_before_acknowledgment_or_application(self):
        self.problem.pilot.campaign.feedback.return_value = {'problems': {'q': {'feedback': [
            {'id': 'required-feedback', 'fingerprint': 'exact-fingerprint', 'status': 'open',
             'needs_delivery': True, 'recipient': 'problem_main', 'finding': 'Exact required finding'}]}}}
        for response in ('candidate_update', 'blocked_checkpoint', 'draft_checkpoint', 'archive_request'):
            with self.subTest(response=response):
                meta = self.fixture.meta('actual-main')
                meta['document_audit'] = {'status': 'PASS', 'required_material_delivered': False,
                                         'required_artifact_coverage': {inputs.TASK_ID: False}}
                before = copy.deepcopy(self.problem.current)
                self.problem.calls = []
                self.problem.pilot.campaign.acknowledge.reset_mock()
                self.problem.apply_authored_response = Mock()
                self.problem.publish_document = Mock()
                with patch.object(pilot, 'call_stage', new=AsyncMock(return_value=(meta, {'response_type': response}))):
                    with self.assertRaisesRegex(ValueError, 'withheld'):
                        asyncio.run(self.problem.main_turn('Complete exact task'))
                self.problem.apply_authored_response.assert_not_called()
                self.problem.publish_document.assert_not_called()
                self.problem.pilot.campaign.acknowledge.assert_not_called()
                self.assertEqual(self.problem.current, before)
                rejected = json.loads((self.problem.folder / f'main-{self.problem.counter}-invalid-contract.json').read_text())
                self.assertEqual(rejected['kind'], 'main_input_delivery_rejection')
                self.assertEqual(rejected['raw_response'], {'response_type': response})
                self.assertEqual(rejected['stage_binding']['session_id'], 'actual-main')
                self.assertFalse(rejected['acceptance_authority'])

    def test_main_can_save_draft_without_acquiring_submission_authority(self):
        _, scope, server = self.scope('required unread task')
        response = server.call('save_proof_revision', {'expected_revision': self.saved['revision'],
            'proof_markdown': '# Current draft\nGap retained.'}, 1,
            {'callId': 'save-draft', 'sessionId': 'actual-main'})
        self.assertFalse(response['isError'])
        current = self.problem.document_current()
        self.assertEqual(current['status'], 'draft')
        self.assertEqual(current['proof_markdown'], '# Current draft\nGap retained.')
        self.assertEqual(store.read_submission(self.problem.folder, **self.problem.document_identity())['candidate'], self.problem.current)
        with self.assertRaises(ValueError):
            inputs.require_main_delivery(scope, {'status': 'completed', 'document_audit': {}})

    def test_same_session_retry_repackages_complete_input_without_inheriting_partial_reads(self):
        attempts = []
        async def dispatch(*args, **kwargs):
            scope = kwargs['document_scope']
            attempts.append((args[5], documents.regular_bytes(scope['readonly_artifacts'][inputs.TASK_ID]['path'])))
            self.assertNotIn('document_recovery_from', kwargs)
            meta = self.fixture.meta('actual-main')
            meta['status'] = 'timeout_censored' if len(attempts) == 1 else 'completed'
            meta['document_audit'] = {'status': 'PASS', 'required_material_delivered': False,
                                     'required_artifact_coverage': {inputs.TASK_ID: False}}
            return meta, {}
        with patch.object(pilot, 'call_stage', new=AsyncMock(side_effect=dispatch)):
            with self.assertRaisesRegex(ValueError, 'withheld'):
                asyncio.run(self.problem.call('main-repair', 'Original required input', resume=True))
        self.assertEqual(len(attempts), 2)
        self.assertEqual([value[0] for value in attempts], ['actual-main', 'actual-main'])
        self.assertEqual(attempts[0][1], b'Original required input')
        self.assertTrue(attempts[1][1].startswith(attempts[0][1]))
        self.assertEqual(self.problem.session, 'actual-main')

    def test_delivery_rejected_response_is_not_in_next_main_candidate_catalog(self):
        raw = {'response_type': 'candidate_update', 'proof_markdown': 'REJECTED FUTURE CANDIDATE', 'ledger': {'rows': []}}
        self.problem.calls = [{'name': 'q/008-main-repair', 'module': 'main-repair', 'status': 'completed'}]
        pilot.write(self.problem.folder / '008-main-repair.json', raw)
        pilot.write(self.problem.folder / 'main-8-invalid-contract.json',
                    {'kind': 'main_input_delivery_rejection', 'raw_response': raw, 'acceptance_authority': False})
        async def capture(role, instruction, **kwargs):
            self.assertNotIn(pilot.candidate_hash(raw), instruction)
            self.assertIn(pilot.candidate_hash(self.problem.current), instruction)
            raise RuntimeError('captured after catalog reconstruction')
        with patch.object(self.problem, 'call', side_effect=capture):
            with self.assertRaisesRegex(RuntimeError, 'captured'):
                asyncio.run(self.problem.main_turn('Next main task'))

    def test_continuation_excludes_rejected_repair_and_refuses_rejected_dossier(self):
        fixture = continuation_fixtures.ContinuationTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        call = fixture.calls[-1]
        raw = {'response_type': 'candidate_update', 'proof_markdown': 'UNDELIVERED RESPONSE', 'ledger': {'rows': []}}
        data = json.dumps(raw).encode()
        call.update(status='completed', answer_sha256=pilot.sha(data))
        stage = fixture.source / 'host/runtime' / call['name']
        (stage / 'stage.answer.txt').write_bytes(data)
        fixture.write(stage / 'stage.meta.json', call)
        fixture.write(fixture.folder / '004-main-repair.json', raw)
        fixture.write(fixture.folder / 'main-4-invalid-contract.json',
                      {'kind': 'main_input_delivery_rejection', 'raw_response': raw, 'acceptance_authority': False})
        restored = fixture.load()['problems']['problem']
        self.assertEqual(restored['current']['proof_markdown'], 'latest valid candidate')
        self.assertIn(call, restored['calls'])
        accepted_path = fixture.folder / 'accepted-dossier.json'
        fixture.write(accepted_path, {'source_stage': call['name'], 'raw_response_sha256': call['answer_sha256'],
                      'effective_candidate': pilot.apply_main_response(raw, {})[0]})
        with self.assertRaisesRegex(ValueError, 'accepted dossier source was rejected'):
            fixture.load()
        accepted_path.unlink()
        dossier = json.loads((fixture.folder / '001-main-dossier.json').read_text())
        fixture.write(fixture.folder / 'main-1-invalid-contract.json',
                      {'kind': 'main_input_delivery_rejection', 'raw_response': dossier, 'acceptance_authority': False})
        with self.assertRaisesRegex(ValueError, 'dossier source was rejected'):
            fixture.load()

    def test_continuation_excludes_rejected_checkpoint_findings_and_tasks(self):
        fixture = continuation_fixtures.ContinuationTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        original = json.loads((fixture.folder / '001-main-dossier.json').read_text())
        raw = {'response_type': 'blocked_checkpoint', 'selected_candidate_sha256': pilot.candidate_hash(original),
               'checkpoint_metadata': {'reason': 'Rejected delivery must not add obligations'},
               'proposed_work': {'sol_tasks': [], 'python_probe': '', 'lean_probe': '', 'lean_probe_rows': []},
               'unreviewed_findings': [{'id': 'undelivered', 'severity': 'gap', 'kind': 'mathematical',
                                       'finding': 'This rejected checkpoint cannot enter the scientific state'}],
               'review_request': 'substantive_reassessment'}
        effective, checkpoint = pilot.apply_main_response(raw, {pilot.candidate_hash(original): original})
        self.assertTrue(checkpoint['actionable'])
        self.assertNotEqual(effective, original)
        call = fixture.calls[-1]
        data = json.dumps(raw).encode()
        call.update(status='completed', answer_sha256=pilot.sha(data))
        stage = fixture.source / 'host/runtime' / call['name']
        (stage / 'stage.answer.txt').write_bytes(data)
        fixture.write(stage / 'stage.meta.json', call)
        fixture.write(fixture.folder / '004-main-repair.json', raw)
        fixture.write(fixture.folder / 'main-4-invalid-contract.json',
                      {'kind': 'main_input_delivery_rejection', 'raw_response': raw, 'acceptance_authority': False})
        restored = fixture.load()['problems']['problem']
        self.assertEqual(restored['current'], original)
        self.assertEqual(restored['findings'], [{'id': 'open-finding'}])
        self.assertEqual(restored['finding_history'], [])


if __name__ == '__main__':
    unittest.main()
