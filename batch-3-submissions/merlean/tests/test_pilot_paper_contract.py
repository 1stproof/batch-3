"""Real document-server receipts exercise exact zero-admission reconciliation."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock, patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_paper as paper
import pilot_paper_delivery as delivery
import pilot_paper_contract as contract
import pilot_document_tools as documents
from codex_transport import _tool_output_part
import test_pilot_paper_delivery as fixtures


class ContractTests(unittest.IsolatedAsyncioTestCase):
    setUp=fixtures.DeliveryTests.setUp
    retrieval_fixture=fixtures.DeliveryTests.retrieval_fixture
    fixture=fixtures.DeliveryTests.fixture
    receipt=fixtures.DeliveryTests.receipt

    def delivered(self, scope, *, pages=False, omit=None, preview=False, bad_output=False, failed_artifact=None):
        server=documents.DocumentTools(scope);events=[];persisted=[];outputs=[]
        plan=documents.required_read_plan(scope) if pages else [
            {'artifact_id':ident,'sha256':scope['readonly_artifacts'][ident]['sha256']}
            for ident in scope['required_artifact_ids'] if ident != omit]
        for i,item in enumerate(plan):
            tool='read_required_evidence' if pages else 'read_artifact'
            args={'page':item['page']} if pages else item
            result=server.call(tool,args,i,{'callId':f'call-{i}','sessionId':'saved-writer'})
            self.assertFalse(result['isError'])
            event={'type':'item.completed','item':{'type':'mcp_tool_call','server':documents.SERVER,
                'tool':tool,'arguments':args,'result':{'content':copy.deepcopy(result['content']),'structured_content':None},
                'error':None,'status':'completed'}}
            if preview:event['item']['result']['content'][0]['text']='short native preview'
            events.append(event)
            persisted.append({'namespace':documents.NAMESPACE,'name':tool,'call_id':f'call-{i}',
                'arguments_canonical_sha256':documents.digest(documents.encoded(args).encode())})
            text=result['content'][0]['text'] if not bad_output else 'altered persisted content'
            outputs.append({'call_id':f'call-{i}','output_format':'list','text_parts':[
                {**_tool_output_part(t),'type':'input_text','keys':['text','type']}
                for t in ['Wall time: 0.001 seconds\nOutput:',text]]})
        if failed_artifact is not None:
            i=len(plan);args={'artifact_id':failed_artifact,'sha256':'','start':0,'end':16000}
            result=server.call('read_artifact',args,i,{'callId':f'call-{i}','sessionId':'saved-writer'})
            self.assertTrue(result['isError'])
            events.append({'type':'item.completed','item':{'type':'mcp_tool_call','server':documents.SERVER,
                'tool':'read_artifact','arguments':args,'result':{'content':result['content'],'structured_content':None},
                'error':None,'status':'failed'}})
            persisted.append({'namespace':documents.NAMESPACE,'name':'read_artifact','call_id':f'call-{i}',
                'arguments_canonical_sha256':documents.digest(documents.encoded(args).encode())})
            outputs.append({'call_id':f'call-{i}','output_format':'list','text_parts':[
                {**_tool_output_part(t),'type':'input_text','keys':['text','type']}
                for t in ['Wall time: 0.001 seconds\nOutput:',result['content'][0]['text']]]})
        audit=documents.audit_operations(scope,events,persisted,'saved-writer',outputs)
        return events,{'status':'verified','tool_events':persisted,'tool_output_receipts':outputs},audit

    def completed_fixture(self, *, preview=False, omit='unaccepted-draft', bad_output=False, extras=None, failed_artifact=None):
        engine=self.fixture();scope=delivery.prepare(engine,self.request)
        if extras is not None:self.answer={**self.answer,'artifacts':extras}
        self.name6='P1/paper-006-reconstruct'
        base=paper.BASE.replace('No tools, external files, web searches, delegated agents,',
            'Only the explicitly provided read_artifact tool is permitted. No other tools, web searches, delegated agents,')+'\nTASK:\nRead all required IDs including unaccepted-draft\nINPUT:\n'+json.dumps({'required_artifact_ids':scope['required_artifact_ids']})
        self.effective=base+'\n'+contract.LEGACY_GUIDANCE
        meta=self.receipt(self.name6,scope,self.answer,delivered=False,prompt=self.effective)
        self.stage=self.problem.pilot.host/'runtime'/self.name6
        actual=paper._json(self.stage/'document-capability.json')
        events,persisted,audit=self.delivered(actual,preview=preview,omit=omit,bad_output=bad_output,failed_artifact=failed_artifact)
        meta.update(document_events=events,persisted_rollout_audit=persisted,document_audit=audit)
        paper._write(self.stage/'stage.meta.json',meta)
        (self.stage/'stage.events.jsonl').write_text(''.join(json.dumps({'event':e})+'\n' for e in events))
        paths=['paper.tex','raw-source.tex','work/evidence_assessment.md','work/reconstruction_map.md',*['work/'+n for n in paper.WRITER_FILES]]
        engine.ledger['calls'].append(meta)
        engine.ledger['delivery_remediation_admissions']=[{'name':self.name6,'status':'admitted',
            'authorization_sha256':self.problem.pilot.config['paper_delivery_remediation']['sha256'],
            'resume_session':'saved-writer','original_retrieval_progress':copy.deepcopy(engine.ledger['retrieval_progress']),
            'scope_sha256':delivery.scope_binding(scope),'prompt_sha256':hashlib.sha256(base.encode()).hexdigest(),
            'before_files':{p:delivery.digest(engine.root/p) if (engine.root/p).is_file() else None for p in paths}}]
        engine.ledger['errors'].append({'type':'DeliveryRecoveryRequired','error':'historical rejection'})
        engine.save()
        self.problem.pilot.config['code_hashes']=contract.LEGACY_CODE.copy()
        paper._write(self.root/'host-config.json',self.problem.pilot.config)
        return engine

    def authorize(self):
        request=contract.make_request(self.root,'P1',self.name6,'a'*64,authority='Explicit exact prospective contract amendment')
        path=self.root/contract.FILE;paper._write(path,request)
        self.problem.pilot.config['paper_delivery_contract_reconciliation']={'path':contract.FILE,'sha256':delivery.digest(path)}
        paper._write(self.root/'host-config.json',self.problem.pilot.config)
        return request

    async def test_real_receipts_reconcile_candidate_without_reconstruction_dispatch(self):
        engine=self.completed_fixture();request=self.authorize();before=copy.deepcopy(engine.ledger)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as launch:
            identity,answer=await engine.call('reconstruct','Task',{},writer=True)
        launch.assert_not_awaited();self.assertEqual(identity,'saved-writer');self.assertEqual(answer,self.answer)
        self.assertEqual(engine.ledger['calls'],before['calls']);self.assertEqual(engine.ledger['errors'],before['errors'])
        self.assertEqual(engine.ledger['delivery_remediation_admissions'],before['delivery_remediation_admissions'])
        self.assertEqual(engine.ledger['retrieval_history'][0]['turns'],4)
        self.assertFalse(engine.ledger['calls'][-1]['document_audit']['required_material_delivered'])
        self.assertEqual(engine.ledger['delivery_contract_reconciliation']['model_admissions'],0)
        self.assertEqual(request['binding']['excluded_provenance']['sha256'],self.request['binding']['files']['raw_answer'])

    async def test_crash_after_reconciliation_and_partial_application_does_not_redispatch(self):
        engine=self.completed_fixture();self.authorize()
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as launch:
            _,answer=await engine.call('reconstruct','Task',{},writer=True)
            engine.writer_result(answer);paper._write(engine.work/'evidence_assessment.md',answer['evidence_assessment'])
            engine.ledger['writer_session']='saved-writer';engine.save()
            resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
            await resumed.call('reconstruct','Task',{},writer=True)
        launch.assert_not_awaited();self.assertEqual(len(resumed.ledger['retrieval_history']),1)
        self.assertEqual(len(resumed.ledger['delivery_remediation_admissions']),1)

    async def test_preview_mismatch_is_informational_with_full_persisted_delivery(self):
        engine=self.completed_fixture(preview=True);self.authorize()
        self.assertTrue(all(x['native_result_matches_receipt'] is False for x in engine.ledger['calls'][-1]['document_audit']['native_diagnostics']))
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as launch:
            await engine.call('reconstruct','Task',{},writer=True)
        launch.assert_not_awaited()

    def test_altered_persisted_outputs_cannot_be_reclassified_as_preview(self):
        self.completed_fixture(preview=True,bad_output=True)
        with self.assertRaisesRegex(ValueError,'original source'):self.authorize()

    def test_missing_original_artifact_never_qualifies(self):
        self.completed_fixture(omit='stage-input')
        with self.assertRaisesRegex(ValueError,'original source'):self.authorize()

    def test_unknown_extra_mandatory_artifact_is_not_optionalized(self):
        engine=self.completed_fixture()
        path=self.stage/'document-capability.json';scope=paper._json(path)
        scope['required_artifact_ids'].append('archive-index');paper._write(path,scope)
        meta=paper._json(self.stage/'stage.meta.json');meta['document_capability']['sha256']=delivery.digest(path)
        paper._write(self.stage/'stage.meta.json',meta)
        engine.ledger['delivery_remediation_admissions'][0]['scope_sha256']=delivery.scope_binding(scope);engine.save()
        with self.assertRaisesRegex(ValueError,'exact scope'):self.authorize()

    def test_exact_legacy_prompt_transform_and_producer_required(self):
        self.completed_fixture();meta=paper._json(self.stage/'stage.meta.json');path=self.stage/'stage.prompt.txt'
        path.write_text(self.effective+'extra');meta['prompt_sha256']=delivery.digest(path);paper._write(self.stage/'stage.meta.json',meta)
        with self.assertRaisesRegex(ValueError,'legacy contract'):self.authorize()
        path.write_text(self.effective);meta['prompt_sha256']=delivery.digest(path);paper._write(self.stage/'stage.meta.json',meta)
        config=paper._json(self.root/'host-config.json');config['code_hashes']['codex_transport.py']='0'*64;paper._write(self.root/'host-config.json',config)
        with self.assertRaisesRegex(ValueError,'legacy producer'):self.authorize()

    async def test_bound_history_writer_raw_and_quarantine_tamper_fail(self):
        engine=self.completed_fixture();request=self.authorize()
        mutations=[(engine.root/'unaccepted-reconstruction/draft.json','changed'),
            (self.stage/'stage.answer.txt','changed'),(self.stage/'stage.prompt.txt','changed')]
        for path,text in mutations:
            before=path.read_bytes();path.write_text(text)
            with self.subTest(path=path.name),self.assertRaises(ValueError):contract.reconcile(engine,request)
            path.write_bytes(before)
        ledger=copy.deepcopy(engine.ledger);engine.ledger['calls'][0]['status']='changed';engine.save()
        with self.assertRaises(ValueError):contract.reconcile(engine,request)
        engine.ledger=ledger;engine.save()
        meta=paper._json(self.stage/'stage.meta.json');meta['resume_session']='other';paper._write(self.stage/'stage.meta.json',meta)
        with self.assertRaises(ValueError):contract.reconcile(engine,request)

    async def test_divergent_application_blocks_completed_candidate(self):
        engine=self.completed_fixture();request=self.authorize()
        (engine.work/'reconstruction_map.md').write_text('Unrelated change')
        with self.assertRaises(delivery.DeliveryRecoveryRequired):contract.reconcile(engine,request)

    def test_real_required_page_pipeline_covers_quarantined_draft_and_all_sources(self):
        engine=self.fixture();scope=delivery.prepare(engine,self.request)
        stage=self.problem.pilot.host/'runtime/P1/new-page-test';stage.mkdir()
        actual,_=documents.prepare_scope(scope,stage,{'stage':'P1/new-page-test','request_id':'page-test','session_id':'saved-writer'})
        visible=contract.visible_contract(scope)
        self.assertEqual({p['artifact_id'] for p in visible['mandatory_read_plan']},set(scope['required_artifact_ids']))
        self.assertTrue(all('sha256' not in page for page in visible['mandatory_read_plan']))
        _,_,audit=self.delivered(actual,pages=True)
        self.assertTrue(audit['required_material_delivered']);self.assertTrue(audit['native_diagnostics'])
        self.assertFalse(audit['errors']);self.assertFalse(audit['delivery_errors'])

    async def test_future_admission_hash_matches_real_transport_suffix_and_prompt_tools(self):
        engine=self.fixture()
        async def completed(host,name,prompt,model,timeout,resume=None,**kw):
            self.assertIn('read_artifact and read_required_evidence tools are permitted',prompt)
            self.assertIn('starting at page 0',prompt)
            scope=kw['document_scope'];self.assertIn('no hash is needed',prompt)
            meta=self.receipt(name,scope,self.answer,delivered=True,internet_browse=kw['internet_browse'],
                prompt=documents.document_prompt(prompt,scope['mode'],public_sources=kw['internet_browse']))
            actual=paper._json(self.problem.pilot.host/'runtime'/name/'document-capability.json')
            events,persisted,audit=self.delivered(actual,pages=True)
            meta.update(document_events=events,persisted_rollout_audit=persisted,document_audit=audit)
            paper._write(self.problem.pilot.host/'runtime'/name/'stage.meta.json',meta)
            self.assertEqual(engine.ledger['delivery_remediation_admissions'][0]['prompt_sha256'],meta['prompt_sha256'])
            return meta,self.answer
        with patch.object(paper,'call_stage',side_effect=completed):await engine.call('reconstruct','Task',{},writer=True)
        self.assertEqual(engine.ledger['delivery_remediation_admissions'][0]['status'],'completed-reconciled')

    def test_only_exact_missing_draft_hash_refusal_is_eligible(self):
        self.completed_fixture(failed_artifact='stage-input')
        with self.assertRaisesRegex(ValueError,'errored document'):self.authorize()

    async def test_unknown_artifacts_are_losslessly_inert_and_fidelity_visible(self):
        extras={'../../controller.key':'untrusted path-shaped label','manifest.json':{'claim':'unverified'},
            'delivery-status.txt':'author claim'}
        engine=self.completed_fixture(extras=extras,failed_artifact='unaccepted-draft');self.authorize()
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as launch:
            _,answer=await engine.call('reconstruct','Task',{},writer=True)
        launch.assert_not_awaited();self.assertEqual(answer['artifacts'],{})
        visible=contract.raw_fidelity_material(engine)
        self.assertEqual(json.loads(visible['original_response'])['artifacts'],extras)
        self.assertEqual(len(visible['attachments']),3)
        self.assertFalse((self.root/'controller.key').exists())
        self.assertFalse((engine.work/'delivery-status.txt').exists())
        self.assertTrue(all('/' not in p.name for p in (engine.root/'untrusted-author-attachments').iterdir()))
        self.assertEqual(visible,contract.raw_fidelity_material(engine))

    async def test_attachment_symlink_or_changed_content_blocks_application(self):
        engine=self.completed_fixture(extras={'extra.md':'untrusted'})
        request=self.authorize();directory=engine.root/'untrusted-author-attachments'
        outside=self.root/'outside';outside.mkdir();directory.symlink_to(outside,target_is_directory=True)
        with self.assertRaises(delivery.DeliveryRecoveryRequired):contract.reconcile(engine,request)
        directory.unlink();contract.reconcile(engine,request)
        attachment=next(directory.glob('attachment-*.txt'));attachment.write_text('changed')
        with self.assertRaises(delivery.DeliveryRecoveryRequired):contract.raw_fidelity_material(engine)

    async def test_partial_projection_and_writer_application_resume_before_fresh_raw_audit(self):
        engine=self.completed_fixture(extras={'extra.md':'untrusted'});self.authorize()
        original=copy.deepcopy(engine.ledger)
        original_writer=engine.writer_result
        def crash(answer):
            original_writer(answer)
            raise OSError('synthetic interruption after writer files')
        with patch.object(engine,'writer_result',side_effect=crash),patch.object(paper,'call_stage',new_callable=AsyncMock) as launch:
            with self.assertRaisesRegex(OSError,'synthetic interruption'):await engine.run()
        launch.assert_not_awaited()
        resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        # raw_inventory requires canonical non-symlink ancestors on macOS.
        resumed.root=resumed.root.resolve();resumed.output=resumed.output.resolve();resumed.work=resumed.work.resolve()
        async def intercept(host,name,prompt,model,timeout,resume=None,**kwargs):
            self.assertEqual(name,'P1/paper-007-raw-audit');self.assertIsNone(resume)
            self.assertEqual(resumed.ledger['calls'][:6],original['calls'])
            self.assertEqual(resumed.ledger['delivery_remediation_admissions'],original['delivery_remediation_admissions'])
            self.assertEqual(len(resumed.ledger['retrieval_history']),1)
            material=json.loads(Path(kwargs['document_scope']['readonly_artifacts']['stage-input']['path']).read_text())
            self.assertEqual(json.loads(material['untrusted_author_attachments']['original_response'])['artifacts'],{'extra.md':'untrusted'})
            raise asyncio.CancelledError()
        import asyncio
        with patch.object(paper,'call_stage',side_effect=intercept):
            with self.assertRaises(asyncio.CancelledError):await resumed.run()

    def test_request_exact_parent_and_no_budget_extension(self):
        self.completed_fixture();r=self.authorize();parent={'source_root':str(self.root),'manifest_sha256':'a'*64}
        self.assertEqual(contract.validate_request(r,self.root,parent),r)
        changed={**r,'model_admissions':1}
        with self.assertRaises(ValueError):contract.validate_request(changed,self.root,parent)
        with self.assertRaises(ValueError):contract.validate_request(r,self.root,{**parent,'manifest_sha256':'b'*64})

if __name__=='__main__':unittest.main()
