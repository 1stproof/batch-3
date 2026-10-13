"""Real synthetic scoped-read receipts; no model or external process calls."""
import asyncio
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import codex_transport as transport
import pilot_document_tools as tools
import pilot_paper as paper
import pilot_paper_read_delivery as reads
import pilot_paper_review_recovery as recovery
from pilot_exam import ExamRuntime, new_config


class PaperReadDeliveryTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()/'parent'; self.root.mkdir()
        self.target = self.root.parent/'successor'
        self.config = {'exam': new_config(self.root), 'internet_browse': False}
        self.runtime = ExamRuntime(self.config['exam'])
        self.folder = self.root/'campaign/problems/P1'; self.folder.mkdir(parents=True)
        (self.folder/'input.txt').write_text('Synthetic original question')
        self.pilot = SimpleNamespace(root=self.root, host=self.root/'host', config=self.config,
            semaphore=asyncio.Semaphore(1), campaign=SimpleNamespace(status=lambda: {'problems': {'P1': {'status': 'partial'}}}))
        self.problem = SimpleNamespace(ident='P1', folder=self.folder, original_bytes=(self.folder/'input.txt').read_bytes(),
            pilot=self.pilot, current={}, dossier={}, findings=[], errors=[], execution_history=[], final_assessment_history=[],
            advisory_scope_history=[], calls=[])
        snapshot = self.runtime.snapshot(self.problem)
        self.engine = paper.PaperEngine(self.problem, snapshot, self.runtime)
        self.engine.ledger.update(stage='raw-audit', completed=['reconstruct'], writer_ids=['writer'], writer_session='writer', reader_ids=['reviewer'])
        self.artifacts = {}
        for key in ('stage-input','archive:a','archive:b','archive:c'):
            path = self.engine.root/(key.replace(':','-')+'.txt'); path.write_text('Synthetic evidence '+key+'\n')
            self.artifacts[key] = {'path': str(path), 'sha256': tools.digest(path.read_bytes()), 'media_type': 'text/plain'}
        self.saved = {'implementers': ['main'], 'calls': [{'session_id': 'main'}]}
        self.checkpoint = {'config': self.config, 'problems': {'P1': self.saved},
            'parent': {'source_root': str(self.root), 'manifest_sha256': 'a'*64}}

    def scope(self, keys):
        return {'schema_version':1, 'mode':'review','problem_id':'P1',
            'original_sha256': tools.digest((self.folder/'input.txt').read_bytes()), 'main_session':'writer',
            'store_root':str(self.engine.root), 'readonly_artifacts': {k:self.artifacts[k] for k in keys},
            'required_artifact_ids':list(keys), 'inline_artifact_ids':[]}

    def receipt(self, number, scope, ids, answer, *, session='reviewer', fresh=False, prompt='Synthetic task', partial=None, stage='raw-audit'):
        name = f'P1/paper-{number:03d}-{stage}'
        directory = self.pilot.host/'runtime'/name; directory.mkdir(parents=True)
        scope, cap = tools.prepare_scope(scope,directory,{'stage':name,'request_id':name+'-request','session_id':None if fresh else session}, internet_browse=self.config['internet_browse'])
        server = tools.DocumentTools(scope)
        events, persisted, outputs = [], [], []
        for i,key in enumerate(ids):
            args = {'artifact_id':key}
            if partial and key in partial: args.update(partial[key])
            callid = 'read'+str(i)
            response = server.call('read_artifact',args,i+1,{'callId':callid,'sessionId':session})
            events.append({'type':'item.completed','item':{'type':'mcp_tool_call','server':tools.SERVER,'tool':'read_artifact',
                'arguments':args,'result':{'content':response['content'],'structured_content':None},'error':None,'status':'completed'}})
            persisted.append({'namespace':tools.NAMESPACE,'name':'read_artifact','call_id':callid,
                'arguments_canonical_sha256':tools.digest(tools.encoded(args).encode())})
            outputs.append({'call_id':callid,'output_format':'list','text_parts':[
                {**transport._tool_output_part(text),'type':'input_text','keys':['text','type']}
                for text in ['Wall time: 0.01 seconds\nOutput:',response['content'][0]['text']]]})
        if not ids: (directory/'document-operations.jsonl').write_text('')
        audit = tools.audit_operations(scope,events,persisted,session,outputs)
        (directory/'stage.events.jsonl').write_text(''.join(json.dumps({'event':e})+'\n' for e in events))
        raw = json.dumps(answer)
        (directory/'stage.answer.txt').write_text(raw); (directory/'stage.answer.json').write_text(raw)
        (directory/'stage.prompt.txt').write_text(prompt)
        meta = {'name':name,'module':'paper-'+stage,'status':'completed','session_id':session,
            'resume_session':None if fresh else session,'fresh_session':fresh,'request_id':name+'-request',
            'model_actual':paper.ASTRA,'model_verified':True,'turn_completed':True,'pid':990123,'exit_code':0,
            'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00',
            'answer_sha256':tools.digest(raw.encode()),'prompt_sha256':tools.digest(prompt.encode()),
            'document_capability':cap,'document_events':events,'document_audit':audit,
            'persisted_rollout_audit':{'status':'verified','tool_events':persisted,'tool_output_receipts':outputs}}
        (directory/'stage.meta.json').write_text(json.dumps(meta))
        return meta

    def chain(self, *, partial=False, final_request=False):
        first = self.receipt(3,self.scope(['stage-input','archive:a']),['stage-input','archive:a'],{'evidence_requests':['b']},fresh=True,
            partial={'archive:a':{'start':0,'end':3}} if partial else None)
        second = self.receipt(4,self.scope(['stage-input','archive:a','archive:b']),['archive:b'],
            {'evidence_requests':['c']} if final_request else {'verdict':'revise','findings':[]})
        self.engine.ledger.update(calls=[first,second],admissions=[{'name':first['name'],'resume_session':None},
            {'name':second['name'],'resume_session':'reviewer'}], evidence_requests={'raw-audit':['b']},
            retrieval_progress={'stage':'raw-audit','session':'reviewer','turns':2,'writer':False})
        self.engine.save()
        return first,second

    def rewrite(self, meta):
        (self.pilot.host/'runtime'/meta['name']/'stage.meta.json').write_text(json.dumps(meta))

    async def test_public_cache_rebase_accepts_only_two_confined_host_layouts(self):
        self.config['internet_browse'] = True
        for number, relative in enumerate(('public-sources', 'refs/public-sources'), 20):
            with self.subTest(relative=relative):
                scope = self.scope(['stage-input'])
                scope['public_source_store'] = str(self.engine.root / relative)
                meta = self.receipt(number, scope, ['stage-input'], {'verdict': 'FAIL'}, fresh=True)
                saved_root = self.root.parent / f'copied-{number}'
                shutil.copytree(self.root, saved_root)
                copied_paper = saved_root / self.engine.root.relative_to(self.root)
                _, _, restored, _ = reads.authenticated(saved_root, copied_paper, meta['name'])
                self.assertEqual(restored['store_root'], str(copied_paper))
                self.assertEqual(restored['public_source_store'], str(copied_paper / relative))
        scope = self.scope(['stage-input'])
        meta = self.receipt(22, scope, ['stage-input'], {'verdict': 'FAIL'}, fresh=True)
        capability = self.pilot.host / 'runtime' / meta['name'] / 'document-capability.json'
        tampered = json.loads(capability.read_text())
        tampered['public_source_store'] = str(self.engine.root.parent / 'public-sources')
        capability.write_text(json.dumps(tampered))
        meta['document_capability']['sha256'] = tools.digest(capability.read_bytes())
        self.rewrite(meta)
        with self.assertRaisesRegex(ValueError, 'public source store changed'):
            reads.authenticated(self.root, self.engine.root, meta['name'])

    async def test_prospective_incremental_read_and_historical_nonacceptance(self):
        first,second=self.chain()
        self.assertFalse(reads.delivered(self.engine,second))
        before=(self.pilot.host/'runtime'/second['name']/'stage.meta.json').read_bytes()
        self.assertTrue(reads.record(self.engine,second['name']))
        receipt=json.loads((self.pilot.host/'runtime'/second['name']/reads.FILE).read_text())
        self.assertEqual(receipt['inherited_complete'],['archive:a','stage-input'])
        self.assertEqual(receipt['current_complete'],['archive:b'])
        self.assertTrue(reads.delivered(self.engine,second))
        self.assertEqual(before,(self.pilot.host/'runtime'/second['name']/'stage.meta.json').read_bytes())

    async def test_three_turn_chain_reaudits_receipts_and_restores(self):
        first,second=self.chain(final_request=True)
        reads.record(self.engine,second['name'])
        third=self.receipt(5,self.scope(list(self.artifacts)),['archive:c'],{'evidence_requests':['d']})
        self.engine.ledger['calls'].append(third)
        self.engine.ledger['admissions'].append({'name':third['name'],'resume_session':'reviewer'})
        self.engine.ledger['evidence_requests']['raw-audit']=['b','c','d']
        self.engine.ledger['retrieval_progress']['turns']=3
        reads.record(self.engine,third['name'])
        self.assertTrue(reads.delivered(self.engine,third))
        self.engine.restored_ledger=True
        self.engine.restore_retrieval('raw-audit',writer=False)
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'],3)
        prior=self.pilot.host/'runtime'/second['name']/reads.FILE
        data=json.loads(prior.read_text());data['inherited_complete']=[];prior.write_text(json.dumps(data))
        with self.assertRaises(ValueError): reads.delivered(self.engine,third)

    async def test_partial_old_reads_never_stitch(self):
        _,second=self.chain(partial=True)
        with self.assertRaises(ValueError): reads.record(self.engine,second['name'])

    async def test_fresh_reviewer_changed_scope_and_tampered_raw_fail(self):
        first,second=self.chain()
        second['resume_session']='another';self.rewrite(second)
        with self.assertRaises(ValueError): reads.record(self.engine,second['name'])
        second['resume_session']='reviewer';self.rewrite(second)
        Path(self.artifacts['archive:a']['path']).write_text('changed')
        with self.assertRaises(ValueError): reads.record(self.engine,second['name'])

    async def test_forged_coverage_does_not_replace_receipts(self):
        first,second=self.chain()
        second['document_audit']['required_artifact_coverage']['archive:a']=True;self.rewrite(second)
        with self.assertRaises(ValueError): reads.record(self.engine,second['name'])

    async def test_substantive_predecessor_cannot_authorize_chain(self):
        first,second=self.chain()
        path=self.pilot.host/'runtime'/first['name'];answer={'verdict':'revise'};raw=json.dumps(answer)
        (path/'stage.answer.txt').write_text(raw);(path/'stage.answer.json').write_text(raw)
        first['answer_sha256']=tools.digest(raw.encode());self.rewrite(first)
        with self.assertRaises(ValueError): reads.record(self.engine,second['name'])

    def authorize(self):
        request=recovery.request_from_checkpoint(self.root,self.target,self.checkpoint,['P1'],authority='Explicit synthetic correction')
        path=self.root/recovery.FILE;path.write_text(json.dumps(request))
        self.config['paper_review_recovery']={'path':recovery.FILE,'sha256':tools.digest(path.read_bytes())}
        return request

    async def test_one_correction_full_reread_and_completed_replay(self):
        first,second=self.chain();request=self.authorize()
        rejected=(self.pilot.host/'runtime'/second['name']/'stage.meta.json').read_bytes()
        calls=[]
        async def fake(host,name,prompt,model,timeout,resume,**kw):
            calls.append(name)
            meta=self.receipt(int(name.split('paper-')[1].split('-')[0]),kw['document_scope'],
                kw['document_scope']['required_artifact_ids'],{'verdict':'revise','findings':[]},
                prompt=tools.document_prompt(prompt,'review',public_sources=False))
            return meta, {'verdict':'revise','findings':[]}
        with patch('pilot_paper.call_stage',side_effect=fake):
            result=await self.engine.call('raw-audit','Return full review',{})
            again=await self.engine.call('raw-audit','Return full review',{})
        self.assertEqual(result,again);self.assertEqual(len(calls),1)
        self.assertEqual(self.engine.ledger['retrieval_history'][0]['turns'],3)
        self.assertNotIn('retrieval_progress',self.engine.ledger)
        self.assertEqual(rejected,(self.pilot.host/'runtime'/second['name']/'stage.meta.json').read_bytes())
        self.assertFalse(reads.delivered(self.engine,second))
        self.engine.ledger['retrieval_history'][0]['turns']=2
        with self.assertRaises(ValueError): await recovery.resume(self.engine,request,'same task')

    async def test_failed_correction_consumes_admission_without_retry(self):
        self.chain();self.authorize();calls=[]
        async def fake(host,name,prompt,model,timeout,resume,**kw):
            calls.append(name)
            return self.receipt(5,kw['document_scope'],['unaccepted-review'],{'verdict':'revise'},
                prompt=tools.document_prompt(prompt,'review',public_sources=False)), {'verdict':'revise'}
        with patch('pilot_paper.call_stage',side_effect=fake):
            with self.assertRaises(paper.delivery.DeliveryRecoveryRequired): await self.engine.call('raw-audit','Review',{})
            with self.assertRaises(paper.delivery.DeliveryRecoveryRequired): await self.engine.call('raw-audit','Review',{})
        self.assertEqual(len(calls),1);self.assertEqual(self.engine.ledger['retrieval_progress']['turns'],3)

    async def test_request_refuses_budget_identity_and_already_accepted(self):
        first,second=self.chain()
        self.engine.ledger['retrieval_progress']['turns']=4;self.engine.save()
        with self.assertRaises(ValueError): self.authorize()
        self.engine.ledger['retrieval_progress']['turns']=2;self.engine.save()
        self.saved['implementers'].append('reviewer')
        with self.assertRaises(ValueError): self.authorize()
        self.saved['implementers'].remove('reviewer')
        reads.record(self.engine,second['name'])
        with self.assertRaises(ValueError): self.authorize()

    async def test_crash_after_transport_reuses_exact_admission(self):
        self.chain();self.authorize();calls=[]
        async def fake(host,name,prompt,model,timeout,resume,**kw):
            calls.append(name)
            self.receipt(5,kw['document_scope'],kw['document_scope']['required_artifact_ids'],{'verdict':'revise'},
                prompt=tools.document_prompt(prompt,'review',public_sources=False))
            raise RuntimeError('synthetic host crash after durable transport')
        with patch('pilot_paper.call_stage',side_effect=fake):
            with self.assertRaises(RuntimeError): await self.engine.call('raw-audit','Review',{})
        restored=paper.PaperEngine(self.problem,self.engine.snapshot,self.runtime)
        with patch('pilot_paper.call_stage',side_effect=AssertionError('must not redispatch')):
            session,answer=await restored.call('raw-audit','Review',{})
        self.assertEqual(session,'reviewer');self.assertEqual(answer,{'verdict':'revise'})
        self.assertEqual(restored.ledger['retrieval_history'][0]['turns'],3)
        self.assertEqual(len(calls),1)

    async def test_native_prepare_and_normal_entry_preserve_history_and_clock(self):
        import codex_pilot as pilot
        import pilot_continuation as native
        import pilot_proof_document as proof
        import subprocess
        self.config['internet_browse']=True
        self.chain()
        self.engine.ledger.update(operational_failure='delivery',recovery_required='preserved rejection')
        self.engine.save()
        def write(path,value):
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value))
        current={'proof_markdown':'Synthetic unresolved candidate','ledger':{'rows':[]}}
        main_name='P1/001-main-dossier'
        main={'name':main_name,'module':'main-dossier','status':'completed','session_id':'main','request_id':'main-request','pid':990124}
        write(self.folder/'001-main-dossier.json',current)
        answer=(self.folder/'001-main-dossier.json').read_bytes();main['answer_sha256']=tools.digest(answer)
        write(self.root/'host/runtime'/main_name/'stage.meta.json',main)
        (self.root/'host/runtime'/main_name/'stage.answer.txt').write_bytes(answer)
        for call in self.engine.ledger['calls']:
            shutil.copyfile(self.pilot.host/'runtime'/call['name']/'stage.answer.json',self.folder/(call['name'].split('/')[-1]+'.json'))
        original=tools.digest((self.folder/'input.txt').read_bytes())
        proof.submit(self.folder,problem_id='P1',original_sha256=original,main_session='main',expected_revision=None,
            candidate=current,producer={'stage':main_name,'request_id':'main-request','session_id':'main'})
        write(self.folder/'current-candidate.json',current)
        write(self.folder/'host-progress.json',{'main_session':'main','calls':[main],'open_findings':[],'errors':[]})
        config={**self.config,'problems':['P1'],'mode':'lite','policy_hashes':{},
            'deadline_utc':self.config['exam']['submission_deadline_utc'],'proof_document_version':1,
            'codex_binary':'synthetic','model_concurrency':1,'source_url':'https://example.invalid','original_scope_review_count':2}
        write(self.root/'host-config.json',config)
        write(self.root/'campaign/registry.json',{'mode':'lite','deadline_utc':config['deadline_utc'],'problems':{'P1':{'sha256':original}}})
        write(self.root/'campaign/state.json',{'problems':{'P1':{'status':'partial','successful_complete':False}},'sealed':True,
            'registry_sha256':recovery.delivery.digest(self.root/'campaign/registry.json')})
        write(self.root/'pilot-result.json',{'end_utc':'2026-01-01T00:00:02+00:00'})
        receipt=self.root.parent/'reconciliation.json'
        write(receipt,{'schema_version':1,'source_root':str(self.root),'checked_utc':'2026-01-01T00:00:03+00:00',
            'host_pid':990120,'owned_pids':[990120,990123,990124],'descendants_checked':True,
            'launch_records_checked':True,'probe_records_checked':True,'evidence':[str(self.root/'pilot-result.json')]})
        before={str(p):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        with patch.object(native.os,'kill',side_effect=ProcessLookupError), \
             patch.object(native.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')), \
             patch.object(pilot,'subscription_preflight',return_value={'authentication':'chatgpt'}):
            request=recovery.make_request(self.root,self.target,receipt,['P1'],authority='Synthetic explicit authorization')
            requestpath=self.root.parent/'request.json';write(requestpath,request)
            prepared=pilot.prepare_continuation(self.root,self.target,receipt,paper_review_recovery=requestpath)
        self.assertEqual(before,{str(p):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        self.assertEqual(prepared['exam']['start_utc'],config['exam']['start_utc'])
        for module in ('pilot_paper_read_delivery.py','pilot_paper_review_recovery.py'):
            self.assertEqual((self.target/'code'/module).read_bytes(),(Path(recovery.__file__).parent/module).read_bytes())
        self.pilot.root=self.target;self.pilot.host=self.target/'host';self.pilot.config=prepared
        self.problem.folder=self.target/'campaign/problems/P1'
        self.runtime=ExamRuntime(prepared['exam'])
        snapshot=self.runtime.paper_dir('P1')/'snapshot'
        self.engine=paper.PaperEngine(self.problem,snapshot,self.runtime)
        async def fake(host,name,prompt,model,timeout,resume,**kw):
            meta=self.receipt(5,kw['document_scope'],kw['document_scope']['required_artifact_ids'],{'verdict':'revise'},
                prompt=tools.document_prompt(prompt,'review',public_sources=True))
            return meta,{'verdict':'revise'}
        async def entry(engine):
            # Keep real run_exam_paper setup and real call/admission/transport guards;
            # stop at the scientific-review application boundary in this synthetic test.
            result=await engine.call('raw-audit','Review synthetic fixed scope',{})
            return {'result':result,'turns':engine.ledger['retrieval_history'][-1]['turns']}
        with patch.object(paper.PaperEngine,'run',entry),patch('pilot_paper.call_stage',side_effect=fake):
            result=await paper.run_exam_paper(self.problem,snapshot,self.runtime)
        self.assertEqual(result['turns'],3)
        self.assertEqual(result['result'],('reviewer',{'verdict':'revise'}))
        self.assertFalse((self.target/'HOST-STARTED').exists())

    async def test_repaired_manuscript_requires_new_reviewer_after_correction(self):
        self.chain();self.authorize()
        async def corrected(host,name,prompt,model,timeout,resume,**kw):
            return self.receipt(5,kw['document_scope'],kw['document_scope']['required_artifact_ids'],{'verdict':'FAIL'},
                prompt=tools.document_prompt(prompt,'review',public_sources=False)), {'verdict':'FAIL'}
        with patch('pilot_paper.call_stage',side_effect=corrected):
            await self.engine.call('raw-audit','Review',{})
        # A legitimate contextual writer repair is a later call and changes the manuscript.
        repaired=copy.deepcopy(self.engine.ledger['calls'][-1])
        repaired.update(name='P1/paper-006-repair-raw-audit',module='paper-repair-raw-audit',session_id='writer')
        directory=self.pilot.host/'runtime'/repaired['name'];directory.mkdir()
        (directory/'stage.meta.json').write_text(json.dumps(repaired))
        self.engine.ledger['calls'].append(repaired)
        self.engine.output.write_text(paper.baseline_tex('P1')+'\n% revised synthetic manuscript')
        self.engine.save();self.engine.restored_ledger=True
        async def fresh(host,name,prompt,model,timeout,resume,**kw):
            self.assertIsNone(resume)
            return self.receipt(7,kw['document_scope'],kw['document_scope']['required_artifact_ids'],{'verdict':'FAIL'},
                session='fresh-reviewer',fresh=True,prompt=tools.document_prompt(prompt,'review',public_sources=False)), {'verdict':'FAIL'}
        with patch('pilot_paper.call_stage',side_effect=fresh):
            identity,_=await self.engine.call('raw-audit','New review',{'raw':'revised'})
        self.assertEqual(identity,'fresh-reviewer')
        self.assertEqual(len(self.engine.ledger['paper_review_recovery_admissions']),1)
        # Preserve a later fresh reviewer's explicit request at a native interruption.
        call=self.engine.ledger['calls'][-1];answer={'evidence_requests':['new-source']};raw=json.dumps(answer)
        directory=self.pilot.host/'runtime'/call['name']
        (directory/'stage.answer.txt').write_text(raw);(directory/'stage.answer.json').write_text(raw)
        call['answer_sha256']=tools.digest(raw.encode());self.rewrite(call)
        self.engine.ledger['evidence_requests']['raw-audit']=['new-source']
        self.engine.ledger['retrieval_progress']={'stage':'raw-audit','session':'fresh-reviewer','turns':1,'writer':False}
        self.engine.save()
        restored=paper.PaperEngine(self.problem,self.engine.snapshot,self.runtime)
        restored.restore_retrieval('raw-audit',writer=False)
        self.assertEqual(restored.ledger['retrieval_progress']['session'],'fresh-reviewer')
        self.assertEqual(restored.ledger['retrieval_progress']['turns'],1)

    async def test_changed_manuscript_cannot_replay_pending_correction(self):
        self.chain();request=self.authorize()
        async def fake(host,name,prompt,model,timeout,resume,**kw):
            self.receipt(5,kw['document_scope'],kw['document_scope']['required_artifact_ids'],{'verdict':'FAIL'},
                prompt=tools.document_prompt(prompt,'review',public_sources=False))
            raise RuntimeError('crash')
        with patch('pilot_paper.call_stage',side_effect=fake):
            with self.assertRaises(RuntimeError): await self.engine.call('raw-audit','Review',{})
        self.engine.output.write_text('Changed manuscript')
        with self.assertRaisesRegex(ValueError,'manuscript'): await recovery.resume(self.engine,request,'Review')

    async def test_research_identity_cannot_inherit_reviewer_reads(self):
        _,second=self.chain()
        self.problem.implementers=['reviewer']
        with self.assertRaisesRegex(ValueError,'research identity'): reads.record(self.engine,second['name'])
