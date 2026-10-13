import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as pilot
import pilot_assessment_handoff as handoff
import pilot_assessment_delivery_resolution as resolution
import pilot_review_history_delivery as delivery
import pilot_operational_handoff as operational
import test_pilot_assessment_handoff as fixture

class ReviewHistoryDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.fixture=fixture.AssessmentHandoffTests();self.fixture.setUp();self.addCleanup(self.fixture.doCleanups)
        self.x=self.fixture.x;self.root=self.fixture.f.root
        target=self.root/'campaign/problems/example';target.parent.mkdir(parents=True)
        shutil.move(self.x.folder,target);self.x.folder=target;self.fixture.f.folder=target
        self.x.ident='example';self.x.pilot=SimpleNamespace(root=self.root,config={})
        review=self.fixture.review;stage=self.root/'host/runtime'/review['name']
        cap=json.dumps({'problem_id':'example','main_session':'original','readonly_artifacts':{}}).encode()
        (stage/'document-capability.json').write_bytes(cap);review['document_capability']['sha256']=pilot.sha(cap)
        (stage/'document-operations.jsonl').write_bytes(b'')
        review['document_audit']={'status':'PASS','required_material_delivered':True,'receipt_sha256':pilot.sha(b'')}
        (stage/'stage.meta.json').write_text(json.dumps(review))
        (target/'002-proof-review.json').write_bytes((stage/'stage.answer.txt').read_bytes())
        self.fixture.raw['assessment_ids']=handoff.capability(self.x)['assessment_ids']
        self.fixture.write_main(self.fixture.raw,resume_session='original')
        main_stage=self.fixture.f.stage;main_cap=b'{"readonly_artifacts":{}}'
        (main_stage/'document-capability.json').write_bytes(main_cap)
        self.fixture.f.meta['document_capability']['sha256']=pilot.sha(main_cap)
        (main_stage/'stage.meta.json').write_text(json.dumps(self.fixture.f.meta))
        with self.assertRaises(operational.OperationalHandoff):handoff.commit(self.x,self.fixture.raw,self.fixture.f.meta)
        self.receipt=json.loads((target/handoff.FILE).read_text())
        self.external=tempfile.TemporaryDirectory();self.addCleanup(self.external.cleanup)
        self.auth=Path(self.external.name).resolve()/'authorization';self.auth.write_text('Explicit synthetic supervisor delivery repair authorization')
        (self.root/'host-config.json').write_text('{}')
        (target/'host-progress.json').write_text(json.dumps({'route_scout_history':[]}))
        self.saved={'calls':self.x.calls,'main_session':'original','current':self.x.current,
            'implementers':['original'],'execution_history':self.x.execution_history,
            'final_assessment_history':self.x.final_assessment_history,'findings':self.x.findings,
            'local_verification_modules':[]}

    def proposal(self,target=None):
        target=target or Path(self.external.name).resolve()/'successor'
        req=resolution.make_request(self.root,target,'example',self.auth)
        path=Path(self.external.name).resolve()/'request.json';path.write_text(json.dumps(req))
        pending=resolution.request(path,self.root,target)
        record=resolution.validate_new(pending,self.root,req['parent_manifest_sha256'],{'example':self.saved})
        return target,req,record

    def copy_successor(self,target,record):
        shutil.copytree(self.root,target)
        data=json.dumps({resolution.KEY:[record]}).encode();(target/'continuation-checkpoint.json').write_bytes(data)
        config={resolution.VERSION_KEY:1,'historical_review_delivery_version':1,
                'continuation_checkpoint':{'path':'continuation-checkpoint.json','sha256':pilot.sha(data)}}
        return config

    def test_full_raw_report_and_public_catalog_exposed_without_acceptance(self):
        b=delivery.for_problem(self.x);self.assertEqual(len(b['reports']),1)
        self.assertEqual(b['reports'][0]['raw_response'],(self.root/'host/runtime/example/002-proof-review/stage.answer.txt').read_text())
        scope={'readonly_artifacts':{},'required_artifact_ids':[]}
        attached,text=delivery.attach(self.x,scope,'task')
        self.assertIn('historical-review:002-proof-review',attached['readonly_artifacts'])
        self.assertIn('historical-review-index',attached['required_artifact_ids'])
        self.assertIn('never current approval',text)
        self.assertEqual(scope,{'readonly_artifacts':{},'required_artifact_ids':[]})

    def test_tampered_raw_copy_capability_and_receipts_fail_closed(self):
        stage=self.root/'host/runtime/example/002-proof-review'
        for p in [stage/'stage.answer.txt',stage/'document-capability.json',stage/'document-operations.jsonl',self.x.folder/'002-proof-review.json']:
            data=p.read_bytes();p.write_text('{}')
            with self.subTest(path=p),self.assertRaises(ValueError):delivery.for_problem(self.x)
            p.write_bytes(data)

    def test_public_packet_native_hash_verification_and_online_tools(self):
        import pilot_public_sources as public
        import pilot_document_tools as tools
        url='https://example.com/public.txt';sid=public.digest(url.encode());folder=self.x.folder/'public-sources'/sid;folder.mkdir(parents=True)
        body=b'Public synthetic reference text';(folder/'raw').write_bytes(body);(folder/'source.txt').write_bytes(body)
        receipt={'source_id':sid,'requested_url':url,'status':'downloaded','raw_sha256':public.digest(body),
                 'members':[{'member':'source.txt','sha256':public.digest(body)}]}
        (folder/'receipt.json').write_text(json.dumps(receipt))
        bundle=delivery.for_problem(self.x);self.assertEqual(bundle['public_sources'][0]['source_id'],sid)
        verified=public.verify_public_source(folder.parent,sid)
        def mutate_after_verification(*args,**kwargs):
            (folder/'source.txt').write_bytes(b'changed after verification')
            return verified
        with patch.object(public,'verify_public_source',side_effect=mutate_after_verification):
            with self.assertRaisesRegex(ValueError,'changed during registration'):
                delivery.register(bundle,self.x.folder/'race-artifacts',folder.parent)
        (folder/'source.txt').write_bytes(body)
        attached,_=delivery.attach(self.x,{'readonly_artifacts':{},'required_artifact_ids':[]},'offline task')
        member=attached['readonly_artifacts']['historical-source:'+sid+':source.txt']
        self.assertEqual(Path(member['path']).read_bytes(),body)
        self.assertNotIn('read_public_source',{x['name'] for x in tools.tool_definitions('review',False)})
        scope={**attached,'schema_version':1,'mode':'review','problem_id':'example',
            'original_sha256':'a'*64,'main_session':'original','store_root':str(self.x.folder),
            'inline_artifact_ids':[],'producer':{'stage':'example/004-proof-review','request_id':'offline','session_id':'fresh'},
            'receipt_path':str(self.root/'offline-operations.jsonl')}
        server=tools.DocumentTools(scope)
        read=server.call('read_artifact',{'artifact_id':'historical-source:'+sid+':source.txt'},1,{'callId':'c1','sessionId':'fresh'})
        self.assertFalse(read['isError']);self.assertEqual(json.loads(read['content'][0]['text'])['text'],body.decode())
        Path(member['path']).write_bytes(b'tampered copy')
        denied=server.call('read_artifact',{'artifact_id':'historical-source:'+sid+':source.txt'},2,{'callId':'c2','sessionId':'fresh'})
        self.assertTrue(denied['isError']);Path(member['path']).write_bytes(body)
        self.assertIn('read_public_source',{x['name'] for x in tools.tool_definitions('review',True)})
        for p in [folder/'raw',folder/'source.txt']:
            p.write_bytes(b'changed')
            with self.assertRaises(ValueError):delivery.for_problem(self.x)
            p.write_bytes(body)

    def test_native_execution_presentation_requires_exact_authenticated_original(self):
        import pilot_execution_identity as identity
        producer={'name':'example/001-sol-execution','request_id':'worker-request','answer_sha256':'a'*64}
        output={'status':'completed','result':'synthetic worker evidence'}
        original=[{'workers':[{'task_id':'worker','output':output,'execution_receipt':producer}],
                   'main_probe':{'python':{'status':'not_requested'}}}]
        restored=[{'historical_stage':producer['name'],'session_id':'worker','status':'completed',
                   'output':output,'execution_receipt':producer}]
        stage=self.root/'host/runtime/example/002-proof-review'
        artifact=self.x.folder/'review-evidence/execution.json';artifact.parent.mkdir();artifact.write_text(json.dumps(original))
        cap=json.loads((stage/'document-capability.json').read_text())
        cap.update(store_root=str(self.x.folder),readonly_artifacts={'actual_execution_evidence':{
            'path':str(artifact),'sha256':pilot.sha(artifact.read_bytes())}})
        data=json.dumps(cap).encode();(stage/'document-capability.json').write_bytes(data)
        calls=copy.deepcopy(self.saved['calls']);calls[0]['document_capability']['sha256']=pilot.sha(data)
        saved={**self.saved,'calls':calls,'execution_history':restored}
        assessments=[{'review_stage':calls[0]['name']}];recorded=identity.digest(original)
        check=lambda:resolution.preserved_execution_digest(self.root,'example',saved,assessments,recorded)
        self.assertNotEqual(recorded,identity.digest(restored));self.assertEqual(check(),recorded)
        with self.assertRaisesRegex(ValueError,'unavailable'):
            resolution.preserved_execution_digest(self.root,'example',saved,[],recorded)
        raw=artifact.read_bytes();artifact.write_bytes(b'[]')
        with self.assertRaisesRegex(ValueError,'artifact changed'):check()
        artifact.write_bytes(raw)
        saved['execution_history']=copy.deepcopy(restored);saved['execution_history'][0]['output']['result']='different actual evidence'
        with self.assertRaisesRegex(ValueError,'differs from restored producers'):check()
        saved['execution_history']=restored
        (stage/'document-capability.json').write_bytes(b'{}')
        with self.assertRaisesRegex(ValueError,'capability changed'):check()

    def test_resolution_preserves_history_and_only_reenters_original_main(self):
        before=copy.deepcopy((self.x.current,self.x.findings,self.x.final_assessment_history,self.x.execution_history))
        target,req,record=self.proposal();config=self.copy_successor(target,record)
        self.x.folder=target/'campaign/problems/example';self.x.pilot=SimpleNamespace(root=target,config=config)
        handoff.guard(self.x,role='main-repair')
        with self.assertRaisesRegex(ValueError,'original-main'):handoff.guard(self.x,role='proof-review')
        self.assertEqual(before,(self.x.current,self.x.findings,self.x.final_assessment_history,self.x.execution_history))
        self.assertEqual(pilot.assessment_key(self.x.current,self.x.execution_history),self.x.final_assessment_history[0]['binding_key'])
        self.assertFalse(pilot.proof_pass({'verdict':'INCOMPLETE','mathematically_ready':True}))

    def test_two_copied_generations_preserve_exact_metadata_and_resolution(self):
        target,req,record=self.proposal();config=self.copy_successor(target,record)
        self.assertEqual(resolution.records(target,config),[record])
        second=Path(self.external.name).resolve()/'second';shutil.copytree(target,second)
        record2={**record,'lineage':[str(target),str(second)]}
        data=json.dumps({resolution.KEY:[record2]}).encode();(second/'continuation-checkpoint.json').write_bytes(data)
        config2={**config,'continuation_checkpoint':{'path':'continuation-checkpoint.json','sha256':pilot.sha(data)}}
        self.assertEqual(resolution.records(second,config2),[record2])
        stage='host/runtime/example/002-proof-review/stage.meta.json'
        self.assertEqual((self.root/stage).read_bytes(),(second/stage).read_bytes())

    def test_stale_candidate_parent_session_and_repeat_format_rejected(self):
        target,req,record=self.proposal();path=Path(self.external.name).resolve()/'request.json'
        for field,value in [('candidate_sha256','a'*64),('original_main_session','other'),('parent_manifest_sha256','b'*64)]:
            changed={**req,field:value};path.write_text(json.dumps(changed));pending=resolution.request(path,self.root,target)
            with self.subTest(field=field),self.assertRaises(ValueError):resolution.validate_new(pending,self.root,req['parent_manifest_sha256'],{'example':self.saved})
        (self.root/'host-config.json').write_text(json.dumps({'historical_review_delivery_version':1}))
        path.write_text(json.dumps(req));pending=resolution.request(path,self.root,target)
        with self.assertRaisesRegex(ValueError,'same delivery format'):resolution.validate_new(pending,self.root,req['parent_manifest_sha256'],{'example':self.saved})

    def test_failed_first_main_and_retry_do_not_authorize_new_handoff(self):
        target,req,record=self.proposal();config=self.copy_successor(target,record)
        self.x.folder=target/'campaign/problems/example';self.x.pilot=SimpleNamespace(root=target,config=config)
        self.x.calls.append({'name':'example/004-main-repair','module':'main-repair','status':'process_failed','resume_session':'original'})
        self.assertTrue(resolution.allows(self.x,self.receipt,role='main-repair'))
        self.x.calls[-1]['resume_session']='other'
        with self.assertRaises(ValueError):resolution.allows(self.x,self.receipt)
        self.assertFalse(resolution.covers([record],'example',receipt={**self.receipt,'source_stage':'example/005-main-repair'}))

    def test_blind_scope_context_never_attaches_historical_verdicts(self):
        import test_pilot_dual_scope as dual
        f=dual.DualScopeTests();f.setUp();self.addCleanup(f.doCleanups)
        f.f.campaign.status.return_value={'problems':{'q':{'successful_complete':True}}}
        with patch.object(delivery,'attach',side_effect=AssertionError('blind scope must not attach historical verdicts')),patch('original_scope.audit_original_scope',return_value=[]):
            f.run_panel()
        for role,prompt,kwargs in f.prompts[:2]:
            self.assertEqual(role,'scope-review');self.assertNotIn('historical-review',prompt)
            self.assertFalse(any(k.startswith('historical-review') for k in (kwargs.get('document_scope') or {}).get('readonly_artifacts',{})))

    def test_native_prepare_and_second_validation_preserve_resolution(self):
        import subprocess
        import pilot_continuation as native
        original=b'Synthetic original question';(self.x.folder/'input.txt').write_bytes(original)
        initial={'name':'example/001-main-dossier','module':'main-dossier','session_id':'original','status':'completed','request_id':'initial','pid':900001}
        stage=self.root/'host/runtime'/initial['name'];stage.mkdir();raw=json.dumps(self.x.current).encode()
        (stage/'stage.answer.txt').write_bytes(raw);initial['answer_sha256']=pilot.sha(raw)
        (stage/'stage.meta.json').write_text(json.dumps(initial));(self.x.folder/'001-main-dossier.json').write_bytes(raw)
        self.x.calls.insert(0,initial)
        registry={'mode':'lite','problems':{'example':{'sha256':pilot.sha(original)}}}
        (self.root/'campaign/registry.json').write_text(json.dumps(registry))
        (self.root/'campaign/state.json').write_text(json.dumps({'sealed':True,'problems':{'example':{'status':'partial'}},'registry_sha256':pilot.sha((self.root/'campaign/registry.json').read_bytes())}))
        config={'problems':['example'],'mode':'lite','codex_binary':'synthetic','model_concurrency':1,'internet_browse':False,'original_scope_review_count':2,'source_url':'https://example.invalid/original','policy_hashes':{}}
        (self.root/'host-config.json').write_text(json.dumps(config));(self.root/'pilot-result.json').write_text(json.dumps({'end_utc':'2026-01-01T00:45:01Z','results':[{'problem':'example','status':'partial'}]}))
        (self.x.folder/'current-candidate.json').write_text(json.dumps(self.x.current))
        (self.x.folder/'host-progress.json').write_text(json.dumps({'main_session':'original','calls':self.x.calls,'open_findings':self.x.findings,'final_assessment_history':self.x.final_assessment_history,'route_scout_history':[]}))
        recon=Path(self.external.name).resolve()/'reconciliation.json'
        def reconcile(root):
            recon.write_text(json.dumps({'schema_version':1,'source_root':str(root),'checked_utc':'2026-01-01T00:46:00Z','host_pid':900000,'owned_pids':[900000,900001], 'descendants_checked':True,'launch_records_checked':True,'probe_records_checked':True,'evidence':[str(root/'pilot-result.json')]}))
        target=Path(self.external.name).resolve()/'native-successor';req=resolution.make_request(self.root,target,'example',self.auth)
        request=Path(self.external.name).resolve()/'native-request.json';request.write_text(json.dumps(req));reconcile(self.root)
        with patch.object(native.os,'kill',side_effect=ProcessLookupError),patch.object(native.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')),patch.object(pilot,'subscription_preflight',return_value={}):
            result=pilot.prepare_continuation(self.root,target,recon,assessment_delivery_resolution=request)
            saved=json.loads((target/'continuation-checkpoint.json').read_text())
            self.assertEqual(saved['problems']['example']['main_session'],'original')
            self.assertEqual(saved['problems']['example']['final_assessment_history'],self.x.final_assessment_history)
            (target/'pilot-result.json').write_text(json.dumps({'end_utc':'2026-01-01T00:45:01Z','results':[{'problem':'example','status':'partial'}]}))
            state=json.loads((target/'campaign/state.json').read_text());state['sealed']=True;(target/'campaign/state.json').write_text(json.dumps(state))
            preserved_meta=(self.root/'host/runtime/example/002-proof-review/stage.meta.json').read_bytes()
            shutil.move(self.root,str(self.root)+'-removed-parent')
            reconcile(target)
            restored=native.validate_and_load(target,reconciliation=recon)
            self.assertEqual(len(restored[resolution.KEY]),1)
            self.assertEqual(restored['problems']['example']['counter'],3)
            second=Path(self.external.name).resolve()/'native-second'
            second_config=pilot.prepare_continuation(target,second,recon)
            inherited=resolution.records(second,second_config)
            self.assertEqual(inherited[0]['lineage'],[str(target),str(second)])
            self.assertEqual(preserved_meta,(second/'host/runtime/example/002-proof-review/stage.meta.json').read_bytes())
            self.x.folder=second/'campaign/problems/example';self.x.pilot=SimpleNamespace(root=second,config=second_config)
            handoff.guard(self.x,role='main-repair')
