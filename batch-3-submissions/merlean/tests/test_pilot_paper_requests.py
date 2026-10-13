"""Request-only continuation uses actual scoped receipts and fake dispatch only."""
import copy
import unittest
from unittest.mock import patch

import test_pilot_paper_read_delivery as fixtures
import pilot_document_tools as tools
import pilot_paper as paper
import pilot_paper_requests as requests


class RequestTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixtures.PaperReadDeliveryTests.setUp
    scope = fixtures.PaperReadDeliveryTests.scope
    receipt = fixtures.PaperReadDeliveryTests.receipt
    async def test_unrecorded_proof_request_keeps_exact_external_scope_and_budget(self):
        external = self.engine.root.parent/'scoped-author-transport.json'
        external.write_text('{"author_observation":"fixed evidence"}')
        self.artifacts['literature-transport:1'] = {'path':str(external),
            'sha256':tools.digest(external.read_bytes()), 'media_type':'application/json'}
        self.engine.ledger['stage'] = 'proof-audit'
        meta = self.receipt(16, self.scope(['stage-input','literature-transport:1']), [],
            {'evidence_requests':['article/paper.pdf']}, fresh=True, stage='proof-audit')
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'], 'stage':'proof-audit','resume_session':None}],
            retrieval_progress={'stage':'proof-audit','session':None,'turns':1,'writer':False},
            initial_review_request={'preserved_old_raw_audit':'not_this_review'})
        before = external.read_bytes()
        self.engine.restore_retrieval('proof-audit', writer=False)
        self.assertEqual(self.engine.ledger['retrieval_progress'],
            {'stage':'proof-audit','session':'reviewer','turns':1,'writer':False})
        self.assertEqual(self.engine.request_only_unavailable, ['article/paper.pdf'])
        ref = self.engine.request_only_scope['readonly_artifacts']['literature-transport:1']
        self.assertEqual(ref['path'], str(external))
        self.assertEqual(external.read_bytes(), before)
        self.assertFalse(meta['document_audit']['required_material_delivered'])
        external.write_text('changed scoped evidence')
        with self.assertRaises(ValueError):
            requests.authenticate(self.engine, meta, 'proof-audit', False)

    async def test_binary_frozen_request_is_explicitly_unavailable_to_text_reader(self):
        import json
        binary = b'%PDF-synthetic-ascii-container'
        path = self.engine.snapshot/'synthetic.pdf'
        path.write_bytes(binary)
        manifest_path = self.engine.snapshot/'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        manifest['files']['synthetic.pdf'] = tools.digest(binary)
        manifest_path.chmod(0o600)
        manifest_path.write_text(json.dumps(manifest))
        meta = self.receipt(3, self.scope(['stage-input']), [],
            {'evidence_requests':['synthetic.pdf']}, fresh=True)
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'],'stage':'raw-audit','resume_session':None}],
            retrieval_progress={'stage':'raw-audit','session':None,'turns':1,'writer':False})
        requests.record(self.engine, 'raw-audit', False)
        self.assertEqual(self.engine.request_only_unavailable, ['synthetic.pdf'])
        self.assertNotIn('archive:synthetic.pdf', self.engine.request_only_scope['readonly_artifacts'])
    async def test_saved_writer_repair_rereads_exact_failed_audit(self):
        diagnostic = '{"verdict":"FAIL","findings":"Missing hypothesis must be restored."}'
        (self.engine.work/'raw-audit.json').write_text(diagnostic)
        meta = self.receipt(5, self.scope(['stage-input', 'archive:a']), [],
            {'evidence_requests':['article/work/00-raw-audit.json']}, session='writer', stage='repair-raw-audit')
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'], 'stage':'repair-raw-audit', 'resume_session':'writer'}],
            retrieval_progress={'stage':'repair-raw-audit','session':'writer','turns':1,'writer':True})
        self.assertTrue(requests.restore(self.engine, 'repair-raw-audit', True))
        self.assertEqual(self.engine.request_only_unavailable, ['article/work/00-raw-audit.json'])
        key = 'repair-diagnostic:raw-audit.json'
        self.assertIn(key, self.engine.request_only_scope['required_artifact_ids'])
        async def fake(host, name, prompt, model, timeout, resume, **kw):
            self.assertEqual(resume, 'writer')
            ref = kw['document_scope']['readonly_artifacts'][key]
            self.assertEqual(tools.digest(diagnostic.encode()), ref['sha256'])
            answer = {'revision_summary':'The missing hypothesis is restored in the author metadata.'}
            meta = self.receipt(6, kw['document_scope'], kw['document_scope']['required_artifact_ids'], answer,
                session='writer', stage='repair-raw-audit',
                prompt=tools.document_prompt(prompt,'review',public_sources=False))
            return meta, answer
        with patch('pilot_paper.call_stage', side_effect=fake) as dispatch:
            await self.engine.call('repair-raw-audit','Repair exact failure',{},resume='writer',writer=True)
        self.assertEqual(dispatch.call_count, 1)
        self.assertNotIn('retrieval_progress', self.engine.ledger)
    async def test_format_neutral_scoped_md_tex_json_requests(self):
        from pathlib import Path
        names = ['note.md', 'draft.tex', 'diagnostic.json']
        for name, content in zip(names, ['# Note\nActual prose', '\\section{Proof}\nActual proof', '{"verdict":"FAIL"}']):
            path = self.engine.root/name
            path.write_text(content)
            self.artifacts[name] = {'path':str(path), 'sha256':tools.digest(path.read_bytes()), 'media_type':'text/plain'}
        meta = self.receipt(3, self.scope(['stage-input', *names]), [],
                            {'evidence_requests':names}, fresh=True)
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'], 'stage':'raw-audit', 'resume_session':None}],
            retrieval_progress={'stage':'raw-audit','session':None,'turns':1,'writer':False})
        requests.record(self.engine, 'raw-audit', False)
        self.assertEqual(self.engine.request_only_unavailable, [])
        for name in names:
            ref = self.engine.request_only_scope['readonly_artifacts']['archive:'+name]
            self.assertEqual(Path(ref['path']).read_bytes(), (self.engine.root/name).read_bytes())
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'], 1)
    async def test_request_before_coverage_then_same_session_full_answer(self):
        seen = []
        async def fake(host, name, prompt, model, timeout, resume, **kw):
            seen.append(resume)
            if len(seen) == 1:
                answer = {'evidence_requests':['missing-optional-reference.md']}
                scope = kw['document_scope']
                ids = []
            else:
                self.assertIn('missing-optional-reference.md', prompt)
                self.assertEqual(resume, 'new-reader')
                answer = {'verdict':'FAIL', 'findings':'Missing optional source remains unresolved.'}
                scope = kw['document_scope']; ids = scope['required_artifact_ids']
            meta = self.receipt(int(name.split('paper-')[1].split('-')[0]), scope, ids, answer,
                session='new-reader', fresh=resume is None,
                prompt=tools.document_prompt(prompt, scope['mode'], public_sources=False))
            return meta, answer
        with patch('pilot_paper.call_stage', side_effect=fake):
            identity, answer = await self.engine.call('raw-audit', 'Audit', {})
        self.assertEqual(seen, [None, 'new-reader'])
        self.assertEqual(identity, 'new-reader')
        self.assertEqual(answer['verdict'], 'FAIL')
        first = self.engine.ledger['calls'][0]
        self.assertFalse(first['document_audit']['required_material_delivered'])
        self.assertNotIn('retrieval_progress', self.engine.ledger)

    async def test_mixed_answer_and_changed_transport_rejected(self):
        meta = self.receipt(3, self.scope(['stage-input']), [],
                            {'evidence_requests':['a'], 'verdict':'PASS'}, fresh=True)
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'], 'stage':'raw-audit', 'resume_session':None}],
            retrieval_progress={'stage':'raw-audit','session':None,'turns':1,'writer':False})
        with self.assertRaisesRegex(ValueError, 'solely evidence requests'):
            requests.record(self.engine, 'raw-audit', False)
        self.assertNotIn('request_only_turns', self.engine.ledger)

    async def test_saved_request_preserves_budget_and_substantive_underread_fails(self):
        meta = self.receipt(3, self.scope(['stage-input','archive:a']), [],
                            {'evidence_requests':['a']}, fresh=True)
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'], 'stage':'raw-audit', 'resume_session':None}],
            retrieval_progress={'stage':'raw-audit','session':None,'turns':1,'writer':False})
        requests.record(self.engine, 'raw-audit', False)
        before = copy.deepcopy(self.engine.ledger['retrieval_progress'])
        self.assertTrue(requests.restore(self.engine, 'raw-audit', False))
        self.assertEqual(before, self.engine.ledger['retrieval_progress'])
        async def fake(host, name, prompt, model, timeout, resume, **kw):
            meta = self.receipt(4, kw['document_scope'], [], {'verdict':'PASS'},
                prompt=tools.document_prompt(prompt,'review',public_sources=False))
            return meta, {'verdict':'PASS'}
        with patch('pilot_paper.call_stage', side_effect=fake):
            with self.assertRaises(paper.delivery.DeliveryRecoveryRequired):
                await self.engine.call('raw-audit','Audit',{})
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'], 2)


if __name__ == '__main__': unittest.main()
