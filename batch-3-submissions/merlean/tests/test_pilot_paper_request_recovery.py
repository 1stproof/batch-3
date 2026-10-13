"""Saved writer request routing preserves rejection, gates and original budget."""
import asyncio
import copy
import json
from pathlib import Path
import shutil
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import test_pilot_paper_read_delivery as fixtures
import pilot_document_tools as tools
import pilot_paper as paper
import pilot_paper_requests as requests
from pilot_exam import ExamRuntime

class RequestRecoveryTests(unittest.IsolatedAsyncioTestCase):
    setUp=fixtures.PaperReadDeliveryTests.setUp
    scope=fixtures.PaperReadDeliveryTests.scope
    receipt=fixtures.PaperReadDeliveryTests.receipt

    def stopped(self, *, fresh=False, public_cache=False):
        content='{"verdict":"FAIL","missing":["synthetic unresolved gate"]}'
        ref=self.artifacts['stage-input'];path=Path(ref['path'])
        path.write_text(json.dumps({'artifacts':{'08-literature-audit.json':content}}))
        ref['sha256']=tools.digest(path.read_bytes())
        self.engine.ledger.update(stage='release-audit',errors=[{'stage':'release-audit','type':'ValueError','message':'12 synthetic failed gates'}])
        scope=self.scope(['stage-input'])
        if public_cache:
            self.config['internet_browse']=True
            scope['public_source_store']=str(self.engine.root/'public-sources')
        meta=self.receipt(16,scope,['stage-input'],
            {'evidence_requests':['work/08-literature-audit.json']},session='writer',fresh=fresh,stage='repair-release-audit')
        self.engine.ledger.update(calls=[meta],admissions=[{'name':meta['name'],'stage':'repair-release-audit','resume_session':None if fresh else 'writer'}],
            retrieval_progress={'stage':'repair-release-audit','session':'writer','turns':1,'writer':True})
        self.engine.save();self.engine.restored_ledger=True
        return content,meta

    async def test_native_paper_entry_reaches_same_writer_next_admission_without_accepting_old_request(self):
        content,meta=self.stopped();old=copy.deepcopy(self.engine.ledger)
        (self.engine.work/'08-literature-audit.json').write_text('UNTRUSTED LATER LIVE FILE')
        class Boundary(BaseException):pass
        async def stop(host,name,prompt,model,timeout,resume,**kw):
            self.assertEqual(name,'P1/paper-017-repair-release-audit');self.assertEqual(resume,'writer')
            ledger=json.loads(self.engine.ledger_path.read_text())
            self.assertEqual(ledger['retrieval_progress']['turns'],2)
            self.assertEqual(ledger['calls'][0],meta)
            self.assertEqual(ledger['errors'],old['errors'])
            self.assertEqual(ledger['completed'],old['completed'])
            ref=kw['document_scope']['readonly_artifacts']['archive:work/08-literature-audit.json']
            self.assertEqual(Path(ref['path']).read_text(),content)
            self.assertIn('archive:work/08-literature-audit.json',kw['document_scope']['required_artifact_ids'])
            raise Boundary()
        with patch('pilot_paper.call_stage',side_effect=stop):
            with self.assertRaises(Boundary):
                await paper.run_exam_paper(self.problem,self.engine.snapshot,self.runtime)

    async def test_two_copied_continuations_rebase_immutable_scope_and_are_idempotent(self):
        content,meta=self.stopped()
        for index in (1,2):
            oldroot=self.pilot.root;target=oldroot.parent/f'copy-{index}'
            shutil.copytree(oldroot,target);shutil.rmtree(oldroot)
            paperroot=target/'exam/papers/P1'
            # Mirrors native copied paper pointers while preserving raw capability bytes.
            self.pilot.root=target;self.pilot.host=target/'host'
            self.engine.root=paperroot;self.engine.work=paperroot/'work'
            self.engine.snapshot=paperroot/'snapshot';self.engine.ledger_path=paperroot/'paper-ledger.json'
            self.engine.ledger=json.loads(self.engine.ledger_path.read_text())
            self.assertTrue(requests.restore(self.engine,'repair-release-audit',True))
            first=copy.deepcopy(self.engine.ledger)
            self.assertTrue(requests.restore(self.engine,'repair-release-audit',True))
            self.assertEqual(self.engine.ledger,first)
            self.assertEqual(self.engine.ledger['retrieval_progress']['turns'],1)
            self.assertEqual(self.engine.ledger['calls'][0],meta)
            ref=self.engine.request_only_scope['readonly_artifacts']['archive:work/08-literature-audit.json']
            self.assertEqual(Path(ref['path']).read_text(),content)

    async def test_absent_optional_cache_does_not_block_fixed_writer_alias(self):
        content,_=self.stopped(public_cache=True)
        cache=self.engine.root/'public-sources'
        if cache.exists(): shutil.rmtree(cache)
        self.assertTrue(requests.restore(self.engine,'repair-release-audit',True))
        ref=self.engine.request_only_scope['readonly_artifacts']['archive:work/08-literature-audit.json']
        self.assertEqual(Path(ref['path']).read_text(),content)
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'],1)
        self.assertFalse(cache.exists())

    async def test_shared_initial_scope_missing_cache_stays_unavailable_and_wrong_path_rejected(self):
        import pilot_paper_initial_review as initial
        scope=self.scope(['stage-input'])
        scope.update(public_source_store=str(self.engine.root/'public-sources'),producer={},receipt_path='')
        scope['readonly_artifacts']['archive:snapshot-entry']=scope['readonly_artifacts']['stage-input']
        result,missing=initial.requested_scope(scope,['snapshot-entry'])
        self.assertEqual(missing,[])
        self.assertIn('archive:snapshot-entry',result['required_artifact_ids'])
        with self.assertRaisesRegex(ValueError,'requested cache source is unavailable'):
            initial.requested_scope(scope,['public-sources/'+'a'*64+'/raw'])
        scope['public_source_store']=str(self.engine.root.parent/'public-sources')
        with self.assertRaisesRegex(ValueError,'outside the preserved host scope'):
            initial.requested_scope(scope,['snapshot-entry'])

    async def test_changed_bound_embedded_bytes_fail_before_reconciliation(self):
        self.stopped();before=copy.deepcopy(self.engine.ledger)
        Path(self.artifacts['stage-input']['path']).write_text('{"artifacts":{"08-literature-audit.json":"PASS"}}')
        with self.assertRaisesRegex(ValueError,'scoped bytes changed'):
            requests.restore(self.engine,'repair-release-audit',True)
        self.assertEqual(self.engine.ledger,before)

    async def test_absent_embedded_value_stays_unavailable_never_reads_live_work(self):
        self.stopped()
        # A different immutable request is authenticated before dispatch.
        ref=self.artifacts['stage-input'];path=Path(ref['path']);path.write_text('{"artifacts":{}}');ref['sha256']=tools.digest(path.read_bytes())
        shutil.rmtree(self.pilot.host/'runtime/P1/paper-016-repair-release-audit')
        meta=self.receipt(16,self.scope(['stage-input']),['stage-input'],{'evidence_requests':['work/08-literature-audit.json']},session='writer',stage='repair-release-audit')
        self.engine.ledger['calls']=[meta]
        (self.engine.work/'08-literature-audit.json').write_text('must never expose live bytes')
        self.assertTrue(requests.restore(self.engine,'repair-release-audit',True))
        self.assertEqual(self.engine.request_only_unavailable,['work/08-literature-audit.json'])
        self.assertNotIn('archive:work/08-literature-audit.json',self.engine.request_only_scope['readonly_artifacts'])

    async def test_wrong_stage_fresh_writer_tampered_producer_and_exhaustion_reject(self):
        for kind in ('stage','fresh','producer','budget'):
            other=RequestRecoveryTests('test_changed_bound_embedded_bytes_fail_before_reconciliation');other.setUp()
            try:
                _,meta=other.stopped(fresh=kind=='fresh');before=copy.deepcopy(other.engine.ledger)
                if kind=='stage':other.engine.ledger['stage']='proof-audit';before=copy.deepcopy(other.engine.ledger)
                if kind=='producer':
                    p=other.pilot.host/'runtime'/meta['name']/'document-capability.json';obj=json.loads(p.read_text());obj['producer']['request_id']='forged';p.write_text(json.dumps(obj))
                if kind=='budget':other.engine.ledger['retrieval_progress']['turns']=4;before=copy.deepcopy(other.engine.ledger)
                with self.assertRaises(ValueError):requests.restore(other.engine,'repair-release-audit',True)
                self.assertEqual(other.engine.ledger,before)
            finally:other.temp.cleanup()

    async def test_completed_corrective_answer_crash_never_redispatches_or_reaccepts(self):
        self.stopped()
        requests.restore(self.engine,'repair-release-audit',True)
        scope=copy.deepcopy(self.engine.request_only_scope)
        meta=self.receipt(17,scope,scope['required_artifact_ids'],
            {'revision_summary':'Synthetic author correction requires ordinary downstream validation.'},
            session='writer',stage='repair-release-audit')
        self.engine.ledger['calls'].append(meta)
        self.engine.ledger['admissions'].append({'name':meta['name'],'stage':'repair-release-audit','resume_session':'writer'})
        self.engine.ledger['retrieval_progress']['turns']=2
        self.engine.save()
        self.engine=paper.PaperEngine(self.problem,self.engine.snapshot,self.runtime)
        before=copy.deepcopy(self.engine.ledger)
        with patch('pilot_paper.call_stage') as dispatch:
            with self.assertRaises(paper.PaperRecoveryRequired):
                await self.engine.call('repair-release-audit','Repair',{},resume='writer',writer=True)
        dispatch.assert_not_called()
        self.assertEqual(self.engine.ledger,before)

    async def test_exact_stage_does_not_confuse_repair_with_release_audit(self):
        self.stopped()
        self.assertFalse(requests.exact_stage(self.engine,self.engine.ledger['calls'][0],'release-audit'))
        self.assertTrue(requests.exact_stage(self.engine,self.engine.ledger['calls'][0],'repair-release-audit'))
