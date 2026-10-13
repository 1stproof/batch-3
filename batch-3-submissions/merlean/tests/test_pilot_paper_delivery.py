"""Quarantined reconstruction delivery repair: one admission, no acceptance shortcut."""
import asyncio
import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import AsyncMock, patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_paper as paper
import pilot_paper_delivery as delivery
from pilot_document_tools import prepare_scope
import test_pilot_paper as fixtures


class DeliveryTests(unittest.IsolatedAsyncioTestCase):
    setUp=fixtures.PaperTests.setUp
    retrieval_fixture=fixtures.PaperTests.retrieval_fixture

    def fixture(self):
        self.runtime=fixtures.Runtime(self.root/'exam')
        target=self.runtime.paper_dir('P1')/'snapshot';target.parent.mkdir(parents=True)
        shutil.copytree(self.snapshot,target);self.snapshot=target
        engine=self.retrieval_fixture(interrupted_count=2)
        self.answer={'tex':self.tex,'artifacts':{},'selected_results':['unresolved'],
            'evidence_assessment':'The full synthetic evidence remains explicitly unresolved.',
            'reconstruction_map':'The synthetic draft preserves the exact unresolved question.'}
        self.name='P1/paper-005-reconstruct'
        _,scope=engine.scoped_payload('reconstruct',{})
        meta=self.receipt(self.name,scope,self.answer,delivered=False,prompt='Original synthetic prompt')
        engine.ledger['calls'].append(meta)
        engine.ledger['retrieval_progress']={'stage':'reconstruct','session':'saved-writer','turns':4,'writer':True}
        engine.save()
        self.request=delivery.make_request(self.root,'P1',self.name,'a'*64,authority='User explicitly authorizes this exact single delivery remediation.')
        request_path=self.root/'paper-delivery-remediation.json';paper._write(request_path,self.request)
        self.problem.pilot.config.update(exam=True,exam_model_time_policy='formal-clock',
            paper_delivery_remediation={'path':request_path.name,'sha256':delivery.digest(request_path)})
        return paper.PaperEngine(self.problem,self.snapshot,self.runtime)

    def receipt(self,name,scope,answer,*,delivered,prompt,internet_browse=False):
        path=self.problem.pilot.host/'runtime'/name;path.mkdir(parents=True)
        scope,cap=prepare_scope(scope,path,{'stage':name,'request_id':name+'-request','session_id':'saved-writer'},
                                internet_browse=internet_browse)
        raw=json.dumps(answer);(path/'stage.answer.txt').write_text(raw)
        paper._write(path/'stage.answer.json',answer);(path/'stage.prompt.txt').write_text(prompt)
        meta={'name':name,'module':'paper-reconstruct','status':'completed','session_id':'saved-writer',
            'resume_session':'saved-writer','request_id':name+'-request','model_actual':paper.ASTRA,'model_verified':True,
            'turn_completed':True,'pid':900123,'exit_code':0,'start_utc':'2026-01-01T00:00:00+00:00',
            'end_utc':'2026-01-01T00:00:01+00:00','answer_sha256':hashlib.sha256(raw.encode()).hexdigest(),
            'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'document_capability':cap,
            'document_audit':{'status':'PASS','required_material_delivered':delivered,
                'complete_tool_outputs_delivered':True,'errors':[],'delivery_errors':[],'native_diagnostics':[],
                'required_artifact_coverage':{ident:delivered for ident in scope['required_artifact_ids']}}}
        paper._write(path/'stage.meta.json',meta)
        return meta

    async def complete(self,host,name,prompt,model,timeout,resume=None,**kw):
        self.assertEqual(name,'P1/paper-006-reconstruct');self.assertEqual(resume,'saved-writer')
        ledger=paper._json(self.runtime.paper_dir('P1')/'paper-ledger.json')
        self.assertEqual(ledger['retrieval_progress']['turns'],4)
        self.assertEqual(len(ledger['delivery_remediation_admissions']),1)
        self.assertNotIn('writer_session',ledger)
        scope=kw['document_scope']
        self.assertEqual(set(scope['required_artifact_ids']),set(self.request['binding']['required_artifacts'])|{'unaccepted-draft'})
        for ident,digest in self.request['binding']['required_artifacts'].items():
            self.assertEqual(scope['readonly_artifacts'][ident]['sha256'],digest)
        self.assertIn('Before any confirmation or revision',prompt)
        self.assertEqual(timeout,3600)
        return self.receipt(name,scope,self.answer,delivered=True,internet_browse=kw['internet_browse'],
            prompt=paper.document_prompt(prompt,scope['mode'],public_sources=kw['internet_browse'])),self.answer

    async def test_same_writer_reads_original_evidence_and_quarantined_draft(self):
        engine=self.fixture()
        before=engine.output.read_bytes();history=json.loads(json.dumps(engine.ledger['calls']))
        with patch.object(paper,'call_stage',side_effect=self.complete) as dispatch:
            writer,answer=await engine.call('reconstruct','Original reconstruction task',{},writer=True)
        self.assertEqual(writer,'saved-writer');self.assertEqual(answer,self.answer)
        self.assertEqual(engine.output.read_bytes(),before)  # Normal writer_result still owns application.
        self.assertEqual(engine.ledger['calls'][:5],history)
        self.assertEqual(engine.ledger['retrieval_history'][0]['turns'],4)
        self.assertEqual(engine.ledger['unaccepted_reconstruction']['status'],'UNACCEPTED')
        self.assertEqual(dispatch.await_count,1)
        self.assertEqual(engine.ledger['stage'],'reconstruct')

    async def test_completed_response_before_ledger_acceptance_reconciles_without_dispatch(self):
        engine=self.fixture()
        async def crash(*args,**kw):
            await self.complete(*args,**kw)
            raise asyncio.CancelledError()
        with patch.object(paper,'call_stage',side_effect=crash):
            with self.assertRaises(asyncio.CancelledError):await engine.call('reconstruct','Task',{},writer=True)
        self.assertEqual(engine.ledger['calls'][-1]['status'],'admitted')
        resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            writer,answer=await resumed.call('reconstruct','Task',{},writer=True)
        dispatch.assert_not_awaited();self.assertEqual(answer,self.answer)
        self.assertEqual(resumed.ledger['retrieval_history'][0]['turns'],4)
        self.assertEqual(len(resumed.ledger['delivery_remediation_admissions']),1)

    async def test_accepted_response_partial_application_reconciles_exact_output(self):
        engine=self.fixture()
        with patch.object(paper,'call_stage',side_effect=self.complete):
            _,answer=await engine.call('reconstruct','Task',{},writer=True)
        engine.writer_result(answer)
        engine.ledger['writer_session']='saved-writer';engine.save()
        paper._write(engine.root/'raw-source.tex',answer['tex'])
        paper._write(engine.work/'evidence_assessment.md',answer['evidence_assessment'])
        resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            _,reconciled=await resumed.call('reconstruct','Task',{},writer=True)
        dispatch.assert_not_awaited();self.assertEqual(reconciled,answer)
        self.assertEqual(len(resumed.ledger['retrieval_history']),1)

    async def test_divergent_application_fails_closed(self):
        engine=self.fixture()
        with patch.object(paper,'call_stage',side_effect=self.complete):
            await engine.call('reconstruct','Task',{},writer=True)
        (engine.work/'reconstruction_map.md').write_text('Unrelated modification')
        resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            with self.assertRaisesRegex(delivery.DeliveryRecoveryRequired,'outside interrupted'):
                await resumed.call('reconstruct','Task',{},writer=True)
        dispatch.assert_not_awaited()

    async def test_failed_delivery_consumes_one_and_never_calls_content_repair(self):
        engine=self.fixture()
        async def missing(host,name,prompt,model,timeout,resume=None,**kw):
            return self.receipt(name,kw['document_scope'],self.answer,delivered=False,prompt=prompt,
                                internet_browse=kw['internet_browse']),self.answer
        with patch.object(paper,'call_stage',side_effect=missing) as dispatch,patch.object(paper.PaperEngine,'repair',new_callable=AsyncMock) as repair:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        self.assertEqual(result['operational_failure'],'delivery');self.assertEqual(result['retrieval_progress']['turns'],4)
        self.assertEqual(len(result['delivery_remediation_admissions']),1);self.assertNotIn('writer_session',result)
        self.assertEqual(dispatch.await_count,1);repair.assert_not_awaited()
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        dispatch.assert_not_awaited();self.assertEqual(result['operational_failure'],'delivery')

    async def test_timeout_consumes_one_and_no_duplicate_after_resume(self):
        engine=self.fixture()
        with patch.object(paper,'call_stage',new=AsyncMock(side_effect=TimeoutError('synthetic cutoff'))):
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        self.assertEqual(result['operational_failure'],'timeout');self.assertEqual(len(result['delivery_remediation_admissions']),1)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        dispatch.assert_not_awaited()

    async def test_changed_authorization_history_and_wrong_stage_cannot_dispatch(self):
        engine=self.fixture();original=json.loads(json.dumps(engine.ledger))
        for mutate in [lambda e:e.ledger['retrieval_progress'].update(turns=3),
                       lambda e:e.ledger['calls'][0].update(status='changed'),
                       lambda e:e.ledger.update(stage='draft')]:
            engine.ledger=json.loads(json.dumps(original));mutate(engine);engine.save()
            with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
                with self.assertRaises(delivery.DeliveryRecoveryRequired):await engine.remediate_delivery(self.request,'Task')
            dispatch.assert_not_awaited()

    async def test_rejected_binding_negatives(self):
        engine=self.fixture();path=self.problem.pilot.host/'runtime'/self.name/'stage.meta.json';original=paper._json(path)
        for change in [{'session_id':'other'},{'model_actual':'other'},{'answer_sha256':'0'*64},
                       {'document_audit':{**original['document_audit'],'required_material_delivered':True}}]:
            paper._write(path,{**original,**change})
            with self.assertRaises(ValueError):delivery.make_request(self.root,'P1',self.name,'a'*64,authority='Explicit user')
        paper._write(path,original)
        with self.assertRaises(ValueError):delivery.make_request(self.root,'P1','P1/paper-005-reader-1','a'*64,authority='Explicit user')
        engine.ledger['delivery_remediation_admissions']=[{'status':'admitted'}];engine.save()
        with self.assertRaises(ValueError):delivery.make_request(self.root,'P1',self.name,'a'*64,authority='Explicit user')

    async def test_completed_correction_integrity_and_prompt_fail_closed(self):
        engine=self.fixture()
        with patch.object(paper,'call_stage',side_effect=self.complete):await engine.call('reconstruct','Task',{},writer=True)
        path=self.problem.pilot.host/'runtime/P1/paper-006-reconstruct/stage.meta.json';original=paper._json(path)
        for change in [{'document_audit':{**original['document_audit'],'delivery_errors':['bad']}},
                       {'prompt_sha256':'0'*64},{'resume_session':'other'}]:
            paper._write(path,{**original,**change})
            resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
            with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
                with self.assertRaises(delivery.DeliveryRecoveryRequired):await resumed.call('reconstruct','Task',{},writer=True)
            dispatch.assert_not_awaited()

    async def test_request_binds_parent_manifest_and_has_no_implicit_authority(self):
        self.fixture()
        parent={'source_root':str(self.root),'manifest_sha256':'a'*64}
        self.assertEqual(delivery.validate_request(self.request,self.root,parent),self.request)
        with self.assertRaises(ValueError):delivery.validate_request(self.request,self.root,{**parent,'manifest_sha256':'b'*64})
        self.problem.pilot.config.pop('paper_delivery_remediation')
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            with self.assertRaises(paper.PaperRecoveryRequired):await engine.call('reconstruct','Task',{},writer=True)
        dispatch.assert_not_awaited()
