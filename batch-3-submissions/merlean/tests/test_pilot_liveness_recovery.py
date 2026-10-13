"""Explicit advisory reachability and append-only supervisor resolution."""
import asyncio
import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import codex_pilot as p
import pilot_handoff_resolution as r
import pilot_operational_handoff as h
import pilot_convergence as c
import pilot_route_scouts as routes
import test_pilot_operational_handoff as handoff_fixture
import test_pilot_parallel_routes as route_fixture

class ResolutionTests(unittest.TestCase):
    def setUp(self):
        f=handoff_fixture.OperationalHandoffTests();f.setUp();self.addCleanup(f.doCleanups)
        self.f=f;self.root=f.root;self.folder=self.root/'campaign/problems/example';self.folder.parent.mkdir(parents=True)
        shutil.move(str(f.folder),self.folder);f.folder=self.folder;f.problem.folder=self.folder;f.problem.ident='example'
        with self.assertRaises(h.OperationalHandoff):h.commit(f.problem,f.raw,f.meta)
        self.receipt=json.loads((self.folder/h.FILE).read_text());self.target=self.root.parent/(self.root.name+'-successor')
        auth=self.root.parent/(self.root.name+'-authorization.json');auth.write_text('{"explicit_user_resume":true}');self.addCleanup(auth.unlink)
        self.req={'schema_version':1,'authority':r.AUTHORITY,'source_root':str(self.root),'target_root':str(self.target),
            'parent_manifest_sha256':'c'*64,'problem_id':'example','handoff_sha256':r.sha((self.folder/h.FILE).read_bytes()),
            'source_stage':f.meta['name'],'source_answer_sha256':f.meta['answer_sha256'],'original_main_session':'original',
            'candidate_sha256':self.receipt['candidate_sha256'],'proof_document':self.receipt['proof_document'],
            'exhaustion_ids':self.receipt['exhaustion_ids'],'authorization_evidence':{'path':str(auth),'sha256':r.sha(auth.read_bytes())}}
        self.request_path=self.root.parent/(self.root.name+'-resolution.json');self.addCleanup(lambda:self.request_path.unlink(missing_ok=True))
        self.saved={'calls':f.problem.calls,'main_session':'original','current':f.candidate,
            'proof_document':self.receipt['proof_document'],'execution_history':f.problem.execution_history,
            'local_verification_modules':[]}
        (self.folder/'host-progress.json').write_text(json.dumps({'open_findings':f.problem.findings,'route_scout_history':[]}))

    def pending(self):
        self.request_path.write_text(json.dumps(self.req));return r.request(self.request_path,self.root,self.target)

    def validated(self):
        with patch.object(r.exhaustion,'derive',return_value=[self.f.record]):
            return r.validate_new(self.pending(),self.root,'c'*64,{'example':self.saved})

    def install(self,value,root=None):
        root=root or self.root
        # Simulate the constructor's preserved payload and hash-bound host config.
        value=copy.deepcopy(value);value['lineage'][-1]=str(root)
        value['request']['target_root']=str(root)
        import base64
        raw=json.dumps(value['request']).encode();value['request_bytes']=base64.b64encode(raw).decode();value['request_sha256']=r.sha(raw)
        payload={'operational_handoff_resolutions':[value]};data=json.dumps(payload).encode()
        (root/'continuation-checkpoint.json').write_bytes(data)
        config={'operational_handoff_resolution_version':1,'continuation_checkpoint':{'path':'continuation-checkpoint.json','sha256':r.sha(data)}}
        self.f.problem.pilot=SimpleNamespace(root=root,config=config)
        return value,config

    def test_explicit_resolution_preserves_old_receipt_and_allows_changed_state(self):
        before=(self.folder/h.FILE).read_bytes();value=self.validated();self.install(value)
        h.guard(self.f.problem);self.assertFalse(self.f.problem.operational_handoff_pending)
        self.f.problem.current['proof_markdown']='New main-owned scientific work'
        self.f.problem.calls.append({'module':'main-repair','name':'example/004-main-repair','status':'running'})
        h.guard(self.f.problem);self.assertEqual((self.folder/h.FILE).read_bytes(),before)

    def test_wrong_binding_and_noncanonical_handoff_reject_without_side_effect(self):
        for field,bad in [('original_main_session','foreign'),('candidate_sha256','0'*64),('exhaustion_ids',[]),('parent_manifest_sha256','0'*64),('source_stage','example/999-main')]:
            original=self.req[field];self.req[field]=bad
            with self.subTest(field=field),self.assertRaises(ValueError):self.validated()
            self.req[field]=original
        self.f.raw['no_new_scientific_work']=1;self.f.write_stage(self.f.raw)
        with self.assertRaises(ValueError):self.validated()
        self.assertFalse(self.target.exists())

    def test_external_authority_and_exact_destination_required(self):
        self.req['target_root']=str(self.root.parent/'other')
        with self.assertRaises(ValueError):self.pending()
        self.req['target_root']=str(self.target)
        self.req['schema_version']=True
        with self.assertRaises(ValueError):self.pending()
        self.req['schema_version']=1
        self.req['authorization_evidence']['path']=str(self.folder/'main-auth.json')
        with self.assertRaises(ValueError):self.pending()
        self.request_path.write_text(json.dumps(self.req));self.request_path.unlink();self.request_path.symlink_to(self.folder/h.FILE)
        with self.assertRaises(ValueError):r.request(self.request_path,self.root,self.target)

    def test_tampered_resolution_blocks_direct_guard_and_paper_flag(self):
        value=self.validated();_,config=self.install(value)
        path=self.root/'continuation-checkpoint.json';path.write_text('{}')
        self.f.problem.operational_handoff_pending=False
        with self.assertRaises(ValueError):h.guard(self.f.problem)
        self.assertTrue(self.f.problem.operational_handoff_pending)
        from unittest.mock import AsyncMock
        x=p.Problem.__new__(p.Problem);x.__dict__.update(self.f.problem.__dict__)
        paper=AsyncMock();x.pilot.exam=SimpleNamespace(dispatch=paper,research_timeout=lambda n:n)
        x.pilot.drain=SimpleNamespace(poll=lambda:False)
        x.pilot.campaign=SimpleNamespace(status=lambda:{'problems':{'example':{'status':'released'}}},finish=lambda *a,**kw:None)
        x.carried_completion=lambda:None;x.restore_checkpoint=lambda:h.guard(x);x.status=lambda phase:None
        x.token=None;x.errors=[];x.operational_handoff_pending=False
        result=asyncio.run(x.run());self.assertEqual(result['status'],'partial');paper.assert_not_awaited()

    def test_three_descendants_keep_original_authority_and_later_handoff_blocks(self):
        value=self.validated();value,config=self.install(value)
        original_target=value['request']['target_root'];prior=self.root
        roots=[]
        try:
            for i in range(3):
                nxt=self.root.parent/(self.root.name+'-generation'+str(i));shutil.copytree(prior,nxt);roots.append(nxt)
                data=json.loads((nxt/'continuation-checkpoint.json').read_text());data['operational_handoff_resolutions'][0]['lineage'].append(str(nxt))
                raw=json.dumps(data).encode();(nxt/'continuation-checkpoint.json').write_bytes(raw)
                config={'operational_handoff_resolution_version':1,'continuation_checkpoint':{'path':'continuation-checkpoint.json','sha256':r.sha(raw)}}
                values=r.records(nxt,config);self.assertEqual(values[0]['request']['target_root'],original_target)
                prior=nxt
            self.f.problem.pilot=SimpleNamespace(root=self.root,config=self.install(value)[1])
            new=copy.deepcopy(self.receipt);new['source_stage']='example/004-main-repair'
            (self.folder/'operational-handoff-004-main-repair.json').write_text(json.dumps(new))
            with self.assertRaises(ValueError):h.guard(self.f.problem)
        finally:
            for path in roots:shutil.rmtree(path)

    def test_embedded_authorization_request_and_lineage_tampering_reject(self):
        value=self.validated();value,config=self.install(value)
        for key,bad in [('authorization_bytes','e30='),('request_bytes','e30='),('lineage',['foreign'])]:
            modified=copy.deepcopy(value);modified[key]=bad
            data=json.dumps({'operational_handoff_resolutions':[modified]}).encode()
            (self.root/'continuation-checkpoint.json').write_bytes(data)
            forged={**config,'continuation_checkpoint':{'path':'continuation-checkpoint.json','sha256':r.sha(data)}}
            with self.subTest(key=key),self.assertRaises(ValueError):r.records(self.root,forged)

class RequestedRouteTests(unittest.TestCase):
    def setUp(self):
        f=route_fixture.ParallelRouteTests();f.setUp();self.addCleanup(f.doCleanups);self.f=f;self.x=f.x
        self.x.folder=self.x.folder.resolve();self.x.pilot.root=self.x.folder;self.x.pilot.host=self.x.folder/'host'
        self.x.triage_history=[]
        for task in self.x.current['route_scout_tasks']:task['purpose']='scientific_alternative'
        self.x.convergence_state={'phase':{'name':'converging','consumer_ids':[]},
            'candidates':{},'observations':{},'research_archive':{},'auxiliary_archive':{}}

    def test_explicit_two_fresh_tasks_dispatch_then_dedup_without_fake_gap(self):
        self.x.convergence_state['phase']['name']='exploring'
        self.x.current['ledger']['rows'].append({'id':'other','claim':'Another retained claim'})
        calls=[]
        async def transport(host,name,prompt,model,timeout,resume,**kwargs):
            calls.append((name,model,timeout,resume));meta=self.f.f.meta('fresh-'+name);meta.update(name=name)
            return meta,{'representation':'advisory','remaining_obligations':['all']}
        with patch.object(p,'call_stage',side_effect=transport):
            result=asyncio.run(self.x.route_scouts())
            self.assertEqual(result['status'],'returned_advisory');self.assertEqual(len(calls),2)
            self.assertTrue(all(v[1:]==(p.ASTRA,300,None) for v in calls))
            self.assertEqual(asyncio.run(self.x.route_scouts())['status'],'already_assessed')
            for task in self.x.current['route_scout_tasks']:
                task['target_row_ids']=['other'];task['task']+=' rephrased'
            self.assertEqual(asyncio.run(self.x.route_scouts())['status'],'already_assessed')
            self.assertEqual(len(calls),2)
        self.assertEqual(self.x.findings,[])
        self.assertTrue(result['obstructions']['user_requested_advisory_exploration'])

    def test_default_certificate_invalid_ids_and_missing_rows_remain_blocked(self):
        tasks=self.x.current['route_scout_tasks'];candidate=self.x.current
        self.assertFalse(c.scout_admission(self.x.convergence_state,tasks)['allowed'])
        with self.assertRaises(ValueError):routes.eligible_obstructions(tasks,candidate,{})
        for mutate in ['certificate','missing_row','invented_finding']:
            modified=copy.deepcopy(tasks)
            if mutate=='certificate':modified[0]['purpose']='certificate_strategy'
            elif mutate=='missing_row':modified[0]['target_row_ids']=['absent']
            else:modified[0]['obstruction_ids']=['invented']
            with self.subTest(mutate=mutate),self.assertRaises(ValueError):routes.eligible_obstructions(modified,candidate,{},user_requested=True)

    def test_real_outer_loop_main_checkpoint_dispatch_and_synthesis(self):
        self.x.convergence_state['phase']['name']='exploring'
        x=self.x;initial=copy.deepcopy(x.current);initial.pop('route_scout_tasks',None);x.current=initial
        tasks=copy.deepcopy(self.f.x.tasks)
        for task in tasks:task['purpose']='scientific_alternative'
        raw={'response_type':'blocked_checkpoint','selected_candidate_sha256':p.candidate_hash(initial),
            'checkpoint_metadata':{'reason':'Explicitly requested alternative questions, not a discovered gap'},
            'proposed_work':{'sol_tasks':[],'python_probe':'','lean_probe':'','lean_probe_rows':[],'route_scout_tasks':tasks},
            'unreviewed_findings':[],'review_request':'route_exploration'}
        x.carried_completion=lambda:None;x.restore_checkpoint=lambda:{'restored':True};x.packet=lambda:{'feedback':[]}
        x.record_convergence=lambda **kw:None;x.local_modules_enabled=lambda:False;x.documents_enabled=lambda:False
        x.pilot.remaining=lambda:100;x.pilot.policy=lambda path:'Generic policy';x.pilot.exam=None
        x.pilot.campaign.claim=lambda *a:'claim';x.pilot.campaign.release=lambda *a:None
        x.pilot.campaign.status=lambda:{'problems':{'q':{'status':'released'}}};x.pilot.campaign.finish=lambda *a,**kw:None
        seen=[]
        async def transport(host,name,prompt,model,timeout,resume,**kw):
            seen.append(name)
            if 'main-repair' in name:
                if sum('main-repair' in n for n in seen)>1:
                    self.assertIn('Main must independently compare, synthesize or reject every advisory route',prompt)
                    raise RuntimeError('Synthetic stop after main receives both advisory results')
                meta=self.f.f.meta(x.session);meta.update(name=name,module='main-repair',fresh_session=False,resume_session=x.session)
                return meta,raw
            meta=self.f.f.meta('fresh-'+name);meta.update(name=name)
            return meta,{'representation':'bounded advisory','remaining_obligations':['all']}
        with patch.object(p,'call_stage',side_effect=transport),patch.object(p,'feedback_notice',return_value={}),patch.object(c,'compact_context',return_value={}):
            result=asyncio.run(x._run_research())
        self.assertEqual(result['status'],'partial')
        self.assertEqual(sum('route-scout-' in n for n in seen),2,result)
        self.assertEqual(sum('main-repair' in n for n in seen),2)
        self.assertFalse(any('proof-review' in n for n in seen))
        self.assertEqual(x.current['proof_markdown'],initial['proof_markdown']);self.assertEqual(x.findings,[])

class ConstructorResolutionTests(unittest.TestCase):
    def test_real_loader_constructor_restore_and_exclusive_successor(self):
        import test_pilot_continuation_runtime as fixtures
        import pilot_continuation as loader
        import subprocess
        f=fixtures.ContinuationRuntimeTests();f.setUp();self.addCleanup(f.doCleanups)
        # Give the existing dossier a complete scientific statement before first publication.
        original={'proof_markdown':'latest valid candidate','answer_statement':'Exact synthetic claim','ledger':{'rows':[]}}
        base=f.fixture.source;stage0=base/'host/runtime/problem/001-main-dossier'
        p.write(f.fixture.folder/'001-main-dossier.json',original);p.write(f.fixture.folder/'current-candidate.json',original)
        answer0=json.dumps(original).encode();(stage0/'stage.answer.txt').write_bytes(answer0)
        meta0=json.loads((stage0/'stage.meta.json').read_text());meta0['answer_sha256']=r.sha(answer0);p.write(stage0/'stage.meta.json',meta0)
        f.prepare();source=f.root.resolve();runner=p.Pilot(source);problem=p.Problem(runner,'problem')
        problem.restore_checkpoint()
        import pilot_review_exhaustion as exhaustion
        record={'id':'b'*64,'binding':{'scientific':exhaustion.projection(problem.current)},
            'required_material_delivered':True,'end_utc':'2026-01-01T00:20:00+00:00'}
        raw={'response_type':h.KIND,'selected_candidate_sha256':p.candidate_hash(problem.current),
            'exhaustion_ids':['b'*64],'reason':'Operational supervisor request','no_new_scientific_work':True}
        stage=source/'host/runtime/problem/005-main-repair';stage.mkdir(parents=True)
        cap=b'{"readonly_artifacts":{}}';prompt=b'Generic task';answer=json.dumps(raw).encode()
        for name,data in [('document-capability.json',cap),('stage.prompt.txt',prompt),('stage.answer.txt',answer),('stage.answer.json',answer)]:
            (stage/name).write_bytes(data)
        meta={'name':'problem/005-main-repair','module':'main-repair','status':'completed','session_id':problem.session,
            'model_verified':True,'turn_completed':True,'document_audit':{'required_material_delivered':True},
            'start_utc':'2026-01-01T00:21:00+00:00','end_utc':'2026-01-01T00:22:00+00:00',
            'document_capability':{'path':str(stage/'document-capability.json'),'sha256':r.sha(cap)},
            'prompt_sha256':r.sha(prompt),'answer_sha256':r.sha(answer)}
        p.write(stage/'stage.meta.json',meta);p.write(problem.folder/'005-main-repair.json',raw)
        problem.calls.append(meta);problem.counter=5
        with patch.object(exhaustion,'synchronize',return_value=[record]):
            with self.assertRaises(h.OperationalHandoff):h.commit(problem,raw,meta)
        problem.status('supervisor-needed')
        state_path=source/'campaign/state.json';state=json.loads(state_path.read_text());state['sealed']=True;p.write(state_path,state)
        p.write(source/'pilot-result.json',{'end_utc':'2026-01-01T00:23:00+00:00','results':[{'problem':'problem','status':'partial'}]})
        receipt=json.loads((problem.folder/h.FILE).read_text());target=source.parent/'recovered'
        files={str(x.relative_to(source)):r.sha(x.read_bytes()) for x in sorted(source.rglob('*')) if x.is_file()}
        manifest=r.sha(json.dumps(files,sort_keys=True,separators=(',',':')).encode())
        auth=source.parent/'supervisor.json';auth.write_text('{"resume":true}')
        req={'schema_version':1,'authority':r.AUTHORITY,'source_root':str(source),'target_root':str(target),
            'parent_manifest_sha256':manifest,'problem_id':'problem','handoff_sha256':r.sha((problem.folder/h.FILE).read_bytes()),
            'source_stage':meta['name'],'source_answer_sha256':meta['answer_sha256'],'original_main_session':problem.session,
            'candidate_sha256':receipt['candidate_sha256'],'proof_document':receipt['proof_document'],
            'exhaustion_ids':receipt['exhaustion_ids'],'authorization_evidence':{'path':str(auth),'sha256':r.sha(auth.read_bytes())}}
        request_path=source.parent/'resolution.json';p.write(request_path,req)
        reconciliation=source.parent/'reconciliation-new.json';p.write(reconciliation,{
            'schema_version':1,'source_root':str(source),'checked_utc':'2026-01-01T00:46:00Z','host_pid':900000,
            'owned_pids':[900000,900001,900002,900003,900004],'descendants_checked':True,'launch_records_checked':True,
            'probe_records_checked':True,'evidence':[str(source/'pilot-result.json')]})
        before=(problem.folder/h.FILE).read_bytes()
        with patch.object(loader.os,'kill',side_effect=ProcessLookupError),patch.object(loader.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')),patch.object(p,'subscription_preflight',return_value={}),patch.object(exhaustion,'derive',return_value=[record]),patch.object(exhaustion,'synchronize',return_value=[record]):
            with self.assertRaisesRegex(ValueError,'pending operational handoff'):
                loader.validate_and_load(source,reconciliation=reconciliation)
            config=p.prepare_continuation(source,target,reconciliation,operational_handoff_resolution=request_path)
            restored=p.Problem(p.Pilot(target),'problem');restored.restore_checkpoint()
            self.assertEqual(restored.session,problem.session);self.assertEqual(restored.counter,5)
            self.assertEqual(restored.current,problem.current);h.guard(restored)
            self.assertFalse(restored.operational_handoff_pending)
            with self.assertRaises(ValueError):p.prepare_continuation(source,target,reconciliation,operational_handoff_resolution=request_path)
        self.assertEqual(before,(problem.folder/h.FILE).read_bytes())
        self.assertEqual(before,(target/'campaign/problems/problem'/h.FILE).read_bytes())
        self.assertEqual(len(r.records(target,config)),1)
        original_target=str(target)
        for generation in range(3):
            current=target;next_target=source.parent/('descendant-'+str(generation))
            state_path=current/'campaign/state.json';state=json.loads(state_path.read_text());state['sealed']=True;p.write(state_path,state)
            p.write(current/'pilot-result.json',{'end_utc':'2026-01-01T00:30:00+00:00','results':[{'problem':'problem','status':'partial'}]})
            rec=json.loads(reconciliation.read_text());rec['source_root']=str(current);rec['evidence']=[str(current/'pilot-result.json')]
            recpath=source.parent/('descendant-reconciliation-'+str(generation)+'.json');p.write(recpath,rec)
            with patch.object(loader.os,'kill',side_effect=ProcessLookupError),patch.object(loader.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'','')),patch.object(p,'subscription_preflight',return_value={}),patch.object(exhaustion,'synchronize',return_value=[record]):
                config=p.prepare_continuation(current,next_target,recpath)
                restored=p.Problem(p.Pilot(next_target),'problem');restored.restore_checkpoint()
            self.assertEqual(restored.session,problem.session);self.assertEqual(restored.counter,5)
            self.assertEqual(r.records(next_target,config)[0]['request']['target_root'],original_target)
            self.assertEqual(before,(next_target/'campaign/problems/problem'/h.FILE).read_bytes())
            target=next_target
        # A genuinely new authenticated handoff is not covered by historical resolution.
        newstage=target/'host/runtime/problem/006-main-repair';newstage.mkdir(parents=True)
        newmeta={**meta,'name':'problem/006-main-repair','start_utc':'2026-01-01T00:31:00+00:00','end_utc':'2026-01-01T00:32:00+00:00',
            'document_capability':{'path':str(newstage/'document-capability.json'),'sha256':r.sha(cap)}}
        for name,data in [('document-capability.json',cap),('stage.prompt.txt',prompt),('stage.answer.txt',answer),('stage.answer.json',answer)]:
            (newstage/name).write_bytes(data)
        p.write(newstage/'stage.meta.json',newmeta);p.write(restored.folder/'006-main-repair.json',raw)
        restored.calls.append(newmeta);restored.counter=6
        with patch.object(exhaustion,'synchronize',return_value=[record]):
            with self.assertRaises(h.OperationalHandoff):h.commit(restored,raw,newmeta)
            self.assertTrue((restored.folder/'operational-handoff-006-main-repair.json').is_file())
            from unittest.mock import AsyncMock
            paper=AsyncMock();restored.pilot.exam=SimpleNamespace(dispatch=paper,research_timeout=lambda n:n)
            restored.restore_checkpoint=lambda:h.guard(restored)
            result=asyncio.run(restored.run())
            self.assertEqual(result['status'],'partial');paper.assert_not_awaited()
        self.assertEqual(before,(restored.folder/h.FILE).read_bytes());self.assertEqual(restored.counter,6)
