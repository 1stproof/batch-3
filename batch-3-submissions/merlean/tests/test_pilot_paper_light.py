"""Native lightweight stage flow using fake model transport, no paid calls."""
import asyncio
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import uuid
from datetime import datetime, timezone, timedelta
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_paper_light as light

TEX=r'\documentclass{article}\begin{document}A complete synthetic test.\end{document}'

def save(p,v):
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(v))

class LightTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.paper=self.root/'exam/papers/prob-001';self.paper.mkdir(parents=True)
        snapshot=self.paper/'snapshot';snapshot.mkdir();save(snapshot/'manifest.json',{'files':{}})
        save(snapshot/'snapshot.json',{'current':{'proof':'synthetic'},'dossier':{},'findings':[], 'research_status':{'successful_complete':True}})
        (snapshot/'input.txt').write_text('Prove the exact synthetic proposition.')
        save(snapshot/'manifest.json',{'files':{p.name:light.sha(p) for p in snapshot.iterdir() if p.name!='manifest.json'}})
        self.runtime=SimpleNamespace(paper_dir=lambda ident:self.paper,verify_snapshot=lambda p:None,
            paper_timeout=lambda n:min(n,900), config={'page_limit':16},
            now=lambda:datetime.now(timezone.utc),research_close=datetime.now(timezone.utc)+timedelta(hours=1))
        self.pilot=SimpleNamespace(root=self.root,host=self.root/'host',config={},semaphore=asyncio.Semaphore(1))
        self.cell={'successful_complete':True,'observations':{'original':{'status':'verified'}},
            'evidence_matches_original_answer':True,'answer_sha256':hashlib.sha256(b'synthetic').hexdigest(),'sha256':'bound-native-manifest'}
        self.pilot.campaign=SimpleNamespace(refresh=lambda:{'problems':{'prob-001':self.cell}})
        self.problem=SimpleNamespace(current={'proof_markdown':'synthetic'},original_bytes=b'Prove the exact synthetic proposition.',ident='prob-001',pilot=self.pilot,folder=self.root/'campaign/prob-001',calls=[],status=lambda x:None)
        self.engine=light.LightPaper(self.problem,snapshot,self.runtime)
        self.seen=[];self.scope_fail=False;self.final_scope_fail=False;self.fail_verify=False

    async def transport(self,root,name,prompt,model,timeout,resume=None,**kw):
        self.seen.append((name,prompt,resume,kw))
        stage=name.split('-light-')[-1];sid=resume or str(uuid.uuid4())
        answer={'verdict':'PASS','findings':[],'assessment':'Inspected every synthetic claim.'}
        if stage=='scope': answer={'verdict':'FAIL' if self.scope_fail else 'PASS','assessment':'Original objects and conclusion compared.'}
        if kw.get('module')=='paper-light-author':
            (kw['paper_workspace']/'paper.tex').write_text(TEX)
            answer={'summary':'Preserved exact proof; addressed feedback without unnecessary changes.'}
        if stage=='final-review': answer.update(original_scope_verdict='FAIL' if self.final_scope_fail else 'PASS',scope_assessment='Exact original statement verified.')
        if stage=='verify-2' and self.fail_verify: answer.update(verdict='FAIL',findings=[{'location':'section1','issue':'missing bridge','required_change':'restore bridge'}])
        folder=root/'runtime'/name;folder.mkdir(parents=True)
        raw=json.dumps(answer);(folder/'stage.answer.txt').write_text(raw);save(folder/'stage.answer.json',answer)
        (folder/'stage.prompt.txt').write_text(prompt)
        meta={'name':name,'module':kw['module'],'status':'completed','model_actual':model,'model_verified':True,
            'session_id':sid,'resume_session':resume,'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),
            'answer_sha256':hashlib.sha256(raw.encode()).hexdigest()}
        if 'paper_workspace' in kw:
            meta['paper_workspace_files']={str(p.relative_to(kw['paper_workspace'])):light.sha(p) for p in kw['paper_workspace'].rglob('*') if p.is_file()}
        if 'image_paths' in kw: meta['paper_image_inputs']=[{'sha256':light.sha(p)} for p in kw['image_paths']]
        save(folder/'stage.meta.json',meta)
        return meta,answer

    async def compile(self,source,label):
        (self.paper/'final.pdf').write_bytes(b'synthetic-pdf');return {'pass':True,'pdf_pages':1}
    async def command(self,args,timeout):
        Path(args[-1]+'-1.png').write_bytes(b'synthetic-image');return 0,'',''

    async def run_engine(self):
        with patch.object(light,'call_stage',self.transport),patch.object(self.engine,'compile',self.compile),patch.object(self.engine,'command',self.command):
            return await self.engine.run()

    async def test_complete_flow_short_context_and_real_order(self):
        result=await self.run_engine();self.assertEqual(result['status'],'polished')
        self.assertEqual([n.split('-light-')[-1] for n,_,_,_ in self.seen],['draft','reader-1','revise-1','reader-2','revise-2','verify-2','final-review','visual'])
        before={str(p):light.sha(p) for p in self.paper.rglob('*') if p.is_file()}
        self.assertEqual(light.verify_completed(self.paper,self.pilot.host)['status'],'PASS')
        self.assertEqual(before,{str(p):light.sha(p) for p in self.paper.rglob('*') if p.is_file()})
        import pilot_supervisor as supervisor
        report=supervisor.completion_summary(self.root,{'problems':['prob-001'],'exam':{'paper_engine':'lightweight-v1','page_limit':16}},
            [{'problem':'prob-001','status':'complete','paper':result}],datetime.now(timezone.utc).isoformat())
        self.assertEqual(report['status'],'exited')
        self.assertEqual(report['issues'],[])
        readers=[row for row in self.seen if row[0].endswith(('reader-1','reader-2'))]
        for _,prompt,resume,kw in readers:
            self.assertIsNone(resume);self.assertNotIn('paper_workspace',kw)
            self.assertNotIn('Original objects and conclusion compared.',prompt)
        self.assertNotIn('finalize-ledgers',' '.join(n for n,_,_,_ in self.seen))
        self.assertLess(max(len(p) for _,p,_,_ in self.seen),50000)
        (self.paper/'final.pdf').write_bytes(b'tampered')
        with self.assertRaises(ValueError):light.verify_completed(self.paper,self.pilot.host)

    async def test_original_mismatch_blocks_author(self):
        self.cell['successful_complete']=False
        with self.assertRaisesRegex(ValueError,'early paper handoff'):
            light.LightPaper(self.problem,self.paper/'snapshot',self.runtime)
        self.assertEqual(len(self.seen),0)

    async def test_deadline_partial_is_honest_without_new_scope_call(self):
        self.cell['successful_complete']=False
        self.runtime.research_close=self.runtime.now()-timedelta(seconds=1)
        engine=light.LightPaper(self.problem,self.paper/'snapshot',self.runtime)
        self.assertEqual(engine.state['scope']['kind'],'deadline-partial')
        self.assertIn('NOT complete',engine.evidence['handoff']['instruction'])

    async def test_final_original_mismatch_cannot_publish(self):
        self.final_scope_fail=True;result=await self.run_engine()
        self.assertEqual(result['status'],'original-scope-mismatch');self.assertFalse((self.paper/'final.pdf').exists())

    async def test_repeated_fail_preserves_four_repair_cap(self):
        self.fail_verify=True
        with self.assertRaisesRegex(RuntimeError,'four contextual'):await self.run_engine()
        self.assertEqual(self.engine.state['repairs'],4)
        self.assertEqual(sum(n.endswith('-repair') for n,_,_,_ in self.seen),4)

    async def test_completed_author_reconciles_without_dispatch_and_tamper_rejects(self):
        self.engine.state['stage']='draft';self.engine.save()
        with patch.object(light,'call_stage',self.transport):await self.engine.author_turn('draft')
        self.engine.save();count=len(self.seen)
        # Restore exact pre-application writer state for the completed pending call.
        self.engine.state['writer']=None;self.engine.save()
        restored=light.LightPaper(self.problem,self.paper/'snapshot',self.runtime)
        with patch.object(light,'call_stage',side_effect=AssertionError('duplicate model call')):
            await restored.author_turn('draft')
        self.assertEqual(len(self.seen),count)
        restored.output.write_text(TEX+'%changed')
        restored.state['writer']=None
        with self.assertRaisesRegex(ValueError,'workspace differs'):
            await restored.author_turn('draft')

    async def test_rejected_transport_is_not_reported_as_workspace_drift(self):
        async def rejected(*args, **kwargs):
            meta, answer = await self.transport(*args, **kwargs)
            meta['status'] = 'invalid_tool_attempt'
            meta.pop('paper_workspace_files')
            save(self.pilot.host/'runtime'/meta['name']/'stage.meta.json', meta)
            return meta, answer
        with patch.object(light, 'call_stage', rejected):
            with self.assertRaisesRegex(ValueError, 'transport did not complete: invalid_tool_attempt'):
                await self.engine.call('draft', 'Write the paper.', workspace=self.engine.author)
        pending = json.loads(json.dumps(self.engine.state['pending']))
        with patch.object(light, 'call_stage', side_effect=AssertionError('must not redispatch')):
            with self.assertRaisesRegex(ValueError, 'transport did not complete: invalid_tool_attempt'):
                await self.engine.call('draft', 'Write the paper.', workspace=self.engine.author)
        self.assertEqual(self.engine.state['pending'], pending)
        self.assertEqual(len(self.seen), 1)

    async def test_completed_review_raw_tampering_rejected(self):
        with patch.object(light,'call_stage',self.transport):await self.engine.call('scope','test')
        self.engine.save();pending=self.engine.state['pending'];folder=self.pilot.host/'runtime'/pending['name']
        save(folder/'stage.answer.json',{'verdict':'PASS','assessment':'forged'})
        with self.assertRaisesRegex(ValueError,'answer changed'):await self.engine.call('scope','test')

    async def test_legacy_ledger_never_migrates(self):
        save(self.paper/'paper-ledger.json',{'stage':'draft'})
        with self.assertRaisesRegex(ValueError,'legacy'):light.LightPaper(self.problem,self.paper/'snapshot',self.runtime)

    async def test_missing_frozen_version_is_not_recreated(self):
        await self.run_engine()
        path=self.engine.work/(light.sha(self.engine.output)+'.tex');path.unlink()
        with self.assertRaises(ValueError):light.verify_completed(self.paper,self.pilot.host)
        self.assertFalse(path.exists())

    async def test_real_compilation_and_rendering(self):
        import shutil
        if sys.platform != 'linux' or not shutil.which('pdflatex') or not shutil.which('pdftoppm'):
            self.skipTest('real TeX/Poppler tools unavailable')
        self.engine.output.write_text(TEX)
        report=await self.engine.compile(self.engine.output,'final')
        self.assertTrue(report['pass']);self.assertGreater(report['pdf_pages'],0)
        prefix=self.engine.work/'real-page'
        code,_,error=await self.engine.command(['pdftoppm','-png','-r','40',str(self.paper/'final.pdf'),str(prefix)],120)
        self.assertEqual(code,0,error)
        self.assertEqual(len(list(self.engine.work.glob('real-page-*.png'))),report['pdf_pages'])

    async def test_fresh_reviewer_cannot_reuse_writer(self):
        await self.run_engine()
        self.engine.state['pending']=None
        writer=self.engine.state['writer']
        async def reused(*args,**kwargs):
            meta,answer=await self.transport(*args,**kwargs)
            meta['session_id']=writer
            return meta,answer
        with patch.object(light,'call_stage',reused):
            with self.assertRaisesRegex(ValueError,'reused'):await self.engine.review('reader-1')

    async def test_manuscript_mutation_during_review_rejected(self):
        self.engine.output.write_text(TEX)
        async def mutate(*args,**kwargs):
            result=await self.transport(*args,**kwargs)
            self.engine.output.write_text(TEX+'%mutated')
            return result
        with patch.object(light,'call_stage',mutate):
            with self.assertRaisesRegex(ValueError,'input changed'):await self.engine.review('reader-1')

    async def test_copied_root_completed_validation_does_not_need_old_paths(self):
        await self.run_engine()
        import shutil
        destination=self.root.parent/(self.root.name+'-successor')
        self.addCleanup(shutil.rmtree,destination,True)
        shutil.copytree(self.root,destination)
        shutil.rmtree(self.root)
        self.assertEqual(light.verify_completed(destination/'exam/papers/prob-001',destination/'host')['status'],'PASS')

    async def test_current_proof_mismatch_cannot_enter_early(self):
        self.problem.current['proof_markdown']='different proposition'
        with self.assertRaisesRegex(ValueError,'early paper handoff'):
            light.LightPaper(self.problem,self.paper/'snapshot',self.runtime)

import test_campaign_scope_integration as native_fixture

class NativeHandoffTests(unittest.TestCase):
    setUp=native_fixture.CampaignScopeIntegrationTests.setUp
    tearDown=native_fixture.CampaignScopeIntegrationTests.tearDown
    digest=staticmethod(native_fixture.CampaignScopeIntegrationTests.digest)
    write=native_fixture.CampaignScopeIntegrationTests.write
    refresh=native_fixture.CampaignScopeIntegrationTests.refresh
    bind_target=native_fixture.CampaignScopeIntegrationTests.bind_target
    bind_original=native_fixture.CampaignScopeIntegrationTests.bind_original
    bind_silver=native_fixture.CampaignScopeIntegrationTests.bind_silver

    def test_native_original_proof_and_silver_gates_control_handoff(self):
        self.campaign.finish('problem',manifest='manifest.json')
        problem=SimpleNamespace(ident='problem',pilot=SimpleNamespace(campaign=self.campaign),
            original_bytes=(self.base/'input.txt').read_bytes(),current={'proof_markdown':self.answer})
        runtime=SimpleNamespace(now=lambda:datetime.now(timezone.utc),research_close=datetime.now(timezone.utc)+timedelta(hours=1))
        receipt=light.research_handoff(problem,runtime)
        self.assertEqual(receipt['kind'],'accepted-original-research')
        # Authentic stale source review must invalidate early handoff, not merely a mocked flag.
        (self.base/'answer.md').write_text(self.answer+' Unsupported extension.')
        with self.assertRaisesRegex(ValueError,'early paper handoff'):light.research_handoff(problem,runtime)
        runtime.research_close=runtime.now()-timedelta(seconds=1)
        self.assertEqual(light.research_handoff(problem,runtime)['kind'],'deadline-partial')

class NativeLightContinuationTests(unittest.IsolatedAsyncioTestCase):
    setUp=LightTests.setUp
    transport=LightTests.transport
    compile=LightTests.compile
    command=LightTests.command
    run_engine=LightTests.run_engine
    # Only this additional integration is collected; inherited focused tests run above.
    async def test_native_prepare_preserves_completed_light_paper(self):
        import test_pilot_continuation_runtime as fixtures
        import codex_pilot as pilot
        import pilot_exam
        import shutil
        self.problem.ident='problem'
        await self.run_engine()
        fixture=fixtures.ContinuationRuntimeTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        source=fixture.fixture.source
        config=light.read(source/'host-config.json')
        config['exam']=pilot_exam.new_config(source,start=pilot.now()-timedelta(hours=23))
        config['exam']['paper_engine']='lightweight-v1'
        config['deadline_utc']=config['exam']['submission_deadline_utc']
        pilot_exam.ExamRuntime(config['exam'])
        save(source/'host-config.json',config)
        registry=light.read(source/'campaign/registry.json');registry['deadline_utc']=config['deadline_utc'];save(source/'campaign/registry.json',registry)
        state=light.read(source/'campaign/state.json');state['registry_sha256']=light.sha(source/'campaign/registry.json');save(source/'campaign/state.json',state)
        shutil.copytree(self.paper,source/'exam/papers/problem')
        for meta in self.engine.state['calls']:
            shutil.copytree(self.pilot.host/'runtime'/meta['name'],source/'host/runtime'/meta['name'])
            shutil.copyfile(self.problem.folder/(meta['name'].split('/')[-1]+'.json'),fixture.fixture.folder/(meta['name'].split('/')[-1]+'.json'))
        progress=light.read(fixture.fixture.folder/'host-progress.json');progress['calls']+=self.engine.state['calls'];save(fixture.fixture.folder/'host-progress.json',progress)
        before=(source/'exam/papers/problem/light-paper-ledger.json').read_bytes()
        successor=fixture.prepare()
        self.assertEqual(successor['exam']['paper_engine'],'lightweight-v1')
        self.assertEqual(before,(fixture.root/'exam/papers/problem/light-paper-ledger.json').read_bytes())
        shutil.rmtree(source)
        self.assertEqual(light.verify_completed(fixture.root/'exam/papers/problem',fixture.root/'host')['status'],'PASS')

    async def test_native_pending_author_replay_after_parent_removed(self):
        import test_pilot_continuation_runtime as fixtures
        import codex_pilot as pilot
        import pilot_exam
        import shutil
        self.problem.ident='problem'
        with patch.object(light,'call_stage',self.transport):await self.engine.author_turn('draft')
        self.engine.state['writer']=None  # Crash before stage application/checkpoint.
        self.engine.save()
        fixture=fixtures.ContinuationRuntimeTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        source=fixture.fixture.source
        config=light.read(source/'host-config.json')
        config['exam']=pilot_exam.new_config(source,start=pilot.now()-timedelta(hours=23))
        config['exam']['paper_engine']='lightweight-v1'
        config['deadline_utc']=config['exam']['submission_deadline_utc'];pilot_exam.ExamRuntime(config['exam'])
        save(source/'host-config.json',config)
        registry=light.read(source/'campaign/registry.json');registry['deadline_utc']=config['deadline_utc'];save(source/'campaign/registry.json',registry)
        state=light.read(source/'campaign/state.json');state['registry_sha256']=light.sha(source/'campaign/registry.json');save(source/'campaign/state.json',state)
        shutil.copytree(self.paper,source/'exam/papers/problem')
        save(source/'exam/papers/problem/snapshot-receipt.json',{'manifest_sha256':light.sha(self.paper/'snapshot/manifest.json')})
        meta=self.engine.state['pending']['meta']
        shutil.copytree(self.pilot.host/'runtime'/meta['name'],source/'host/runtime'/meta['name'])
        # Real completed raw transport remains discoverable before its host application.
        shutil.copyfile(self.pilot.host/'runtime'/meta['name']/'stage.answer.json',fixture.fixture.folder/(meta['name'].split('/')[-1]+'.json'))
        progress=light.read(fixture.fixture.folder/'host-progress.json');progress['calls'].append(meta);save(fixture.fixture.folder/'host-progress.json',progress)
        config=fixture.prepare();shutil.rmtree(source)
        runtime=pilot_exam.ExamRuntime(config['exam'])
        self.problem.pilot.root=fixture.root;self.problem.pilot.host=fixture.root/'host'
        self.problem.pilot.config=config
        self.problem.folder=fixture.root/'campaign/problems/problem'
        snapshot=runtime.snapshot(self.problem)
        self.problem.pilot.campaign=SimpleNamespace(refresh=lambda:{'problems':{'problem':self.cell}})
        restored=light.LightPaper(self.problem,snapshot,runtime)
        with patch.object(light,'call_stage',side_effect=AssertionError('completed author must not redispatch')):
            await restored.author_turn('draft')
        restored.advance('reader-1')
        self.assertEqual(restored.state['writer'],meta['session_id'])
        self.assertEqual(len(restored.state['calls']),1)
        self.assertEqual(restored.state['stage'],'reader-1')
