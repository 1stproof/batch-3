"""NL is a persisted execution capability, not a changed proof grade."""
import asyncio
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import lean_capability as c
import offline_probe
import codex_pilot as p
import research_grade
import shared_workspace
from plan_store import prove, lean_sync
from plan_store.offline_store import OfflinePlanGraph
import test_pilot_local_compile_cycle as fixture

class NLCapability(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve()

    def test_ancestor_policy_cannot_be_shadowed_and_malformed_fails_closed(self):
        c.initialize(self.root,True)
        child=self.root/'child';child.mkdir()
        (child/c.MARKER).write_text(json.dumps({'schema_version':1,'nl_only':False}))
        self.assertTrue(c.nl_only(child,config={'nl_only':False}))
        for value in [None,1,'true',{},[]]:
            (child/c.MARKER).write_text(json.dumps({'schema_version':1,'nl_only':value}))
            with self.subTest(value=value),self.assertRaises(ValueError):c.nl_only(child)

    def test_lexical_symlink_and_host_config_preserve_capability(self):
        c.initialize(self.root,True)
        with tempfile.TemporaryDirectory() as other:
            link=self.root/'link';link.symlink_to(other,target_is_directory=True)
            self.assertTrue(c.nl_only(link/'new-file'))
            (Path(other)/'host-config.json').write_text(json.dumps({'nl_only':True}))
            self.assertTrue(c.nl_only(other))
            with self.assertRaises(ValueError):c.require_lean(other)

    def test_existing_research_cannot_migrate_or_reset_grade_history(self):
        plan=self.root/'statements.json';plan.write_text('{"retained":"history"}')
        before=plan.read_bytes()
        with self.assertRaises(ValueError):c.initialize(self.root,True)
        self.assertEqual(before,plan.read_bytes());self.assertFalse((self.root/c.MARKER).exists())

    def test_inherited_nl_persists_across_external_data_and_cwd_change(self):
        project=self.root/'project';c.initialize(project,True)
        data=self.root/'outside_data'
        args=[sys.executable,str(ROOT/'src/offline_cli.py'),'--data',str(data)]
        first=subprocess.run([*args,'list'],cwd=project,text=True,capture_output=True)
        self.assertEqual(first.returncode,0,first.stderr)
        self.assertTrue((data/c.MARKER).is_file())
        second=subprocess.run([*args,'sync-lean',str(self.root)],cwd=self.root,text=True,capture_output=True)
        self.assertNotEqual(second.returncode,0);self.assertIn('NL mode',second.stderr)
        existing=self.root/'old_data';existing.mkdir();(existing/'statements.json').write_text('{"statements":[]}')
        before=(existing/'statements.json').read_bytes()
        denied=subprocess.run([sys.executable,str(ROOT/'src/offline_cli.py'),'--data',str(existing),'list'],cwd=project,text=True,capture_output=True)
        self.assertNotEqual(denied.returncode,0);self.assertFalse((existing/c.MARKER).exists())
        self.assertEqual(before,(existing/'statements.json').read_bytes())

    def test_continuation_inherits_exact_boolean(self):
        self.assertFalse(c.continuation_nl({}))
        self.assertTrue(c.continuation_nl({'nl_only':True}))
        for old,new in [({},True),({'nl_only':True},False),({'nl_only':'true'},None)]:
            with self.subTest(old=old,new=new),self.assertRaises(ValueError):c.continuation_nl(old,new)

    def test_direct_lean_apis_reject_before_file_or_subprocess_changes(self):
        c.initialize(self.root,True);graph=OfflinePlanGraph(self.root/'plan_data')
        before={str(f):f.read_bytes() for f in self.root.rglob('*') if f.is_file()}
        actions=[lambda:prove.seed_sorry_file(graph,self.root/'Main.lean',self.root),
            lambda:lean_sync.sync_edges_from_lean(graph,self.root),
            lambda:lean_sync.reconcile_status_from_lean(graph,self.root,build=True),
            lambda:lean_sync._module_builds({},self.root),
            lambda:shared_workspace.run_project(self.root,'build',[]),
            lambda:shared_workspace.init_project(self.root/'new',self.root,'p','new'),
            lambda:offline_probe.run_lean_probe('example : True := by trivial','/lean',[],policy_root=self.root),
            lambda:research_grade.verify_kernel_runtime({'grade':'GOLD','schema_version':2},self.root),
            lambda:research_grade.record_audited_gold({},self.root,self.root/'m.json',b'{}',self.root,'r')]
        with patch('subprocess.run') as run:
            for action in actions:
                with self.subTest(action=action),self.assertRaises(ValueError):action()
            run.assert_not_called()
        self.assertEqual(before,{str(f):f.read_bytes() for f in self.root.rglob('*') if f.is_file()})
        self.assertEqual(research_grade.verify_kernel_runtime({'grade':'SILVER'},self.root),[])

    def test_pilot_approved_restored_module_and_inventory_cannot_dispatch(self):
        f=fixture.CompileCycle();x,task,seen,proc=f.fixture(self.root,[],[])
        module,_=x.admit_local_module(task)
        x.pilot.config['nl_only']=True
        before=copy.deepcopy(x.local_verification_modules)
        with patch('asyncio.create_subprocess_exec',AsyncMock()) as run:
            result=asyncio.run(x.execution())
            x.call.assert_not_called();run.assert_not_called()
            self.assertEqual(result['workers'][0]['output']['status'],'deferred')
            for label,output in [('restored',{'lean_probe':'example : True := by trivial','lean_probe_rows':['r']}),
                                 ('inventory',{'lean_probe':'#check Nat','lean_probe_rows':['r']})]:
                r=asyncio.run(x.probe(output,label,local_module=module))
                self.assertEqual(r['lean']['status'],'disabled')
            run.assert_not_called()
        self.assertEqual(before,x.local_verification_modules)
        self.assertEqual(x.admit_local_module(task),(None,c.NOTICE))
        self.assertFalse(list(self.root.rglob('source.lean')))

    def test_direct_worker_api_requires_current_approved_research_task(self):
        f=fixture.CompileCycle();x,task,_,_=f.fixture(self.root,[],[]);x.pilot.config['nl_only']=True
        for role,t in [('sol-execution',None),('sol-execution',task),('lean-inventory',None)]:
            with self.subTest(role=role),self.assertRaises(ValueError):x.execution_capability(role,t)
        with self.assertRaises(ValueError):
            asyncio.run(p.Problem._call_once(x,'sol-execution','forged',model='model',resume=False,timeout=1))
        research={**task,'kind':'research'}
        with patch.object(x,'research_authorized',return_value=True):x.execution_capability('sol-execution',research)
        x.execution_capability('proof-review',None)

    def test_probe_helper_isolation_sees_nl_host_config(self):
        (self.root/'host-config.json').write_text(json.dumps({'nl_only':True}))
        request={'kind':'lean','code':'#check Nat','executable':'/nonexistent/lean','library_paths':[]}
        run=subprocess.run([sys.executable,'-I',str(ROOT/'src/offline_probe.py')],input=json.dumps(request),
                           text=True,capture_output=True,cwd=self.root)
        self.assertIn('NL mode',run.stdout);self.assertNotIn('ModuleNotFoundError',run.stderr)

    def test_nl_python_probe_and_approved_research_worker_remain_available(self):
        f=fixture.CompileCycle();x,task,_,proc=f.fixture(self.root,[],[])
        x.pilot.config['nl_only']=True
        task['kind']='research';task.pop('local_module')
        x.active_triage.update(candidate_binding=p.triage_binding(x.current),
            approved_research_task_hashes=[p.sha(p.encoded(task))])
        x.call=AsyncMock(return_value=({'session_id':'research-worker'}, {'findings':['NL derivation'],'lean_probe':''}))
        with patch('asyncio.create_subprocess_exec',AsyncMock()) as launch:
            result=asyncio.run(x.execution())
            self.assertEqual(x.call.await_count,1);launch.assert_not_called()
            self.assertEqual(result['workers'][0]['output']['findings'],['NL derivation'])
        proc.communicate=AsyncMock(return_value=(json.dumps({'status':'completed','exit_code':0,'stdout':'2'}).encode(),b''))
        with patch('asyncio.create_subprocess_exec',AsyncMock(return_value=proc)) as launch:
            result=asyncio.run(x.probe({'python_probe':'print(1+1)'},'nl-python'))
            self.assertEqual(result['python']['status'],'completed');self.assertEqual(launch.await_count,1)
        self.assertFalse(list(self.root.rglob('source.lean')))

    def test_nl_keeps_zero_selected_silver_and_blocks_selected_missing_certificate(self):
        import test_campaign_evidence as fixtures
        f=fixtures.CampaignEvidenceTests();f.setUp();self.addCleanup(f.doCleanups)
        c.initialize(f.base,True)
        f.test_silver_empty_census_only_matches_no_selected_rows()
        f.silver()
        ledger={'rows':[{'id':'S1','closed':True,'triaged':True,'status':'needs-lean'}]}
        f.data['ledger']=f.write('ledger.json',ledger);f.report['ledger']=f.data['ledger']
        provenance=json.loads((f.base/'dispatch.json').read_text());provenance['ledger_sha256']=f.data['ledger']['sha256']
        f.report['reviewer_provenance']=f.write('dispatch.json',provenance);f.update_report()
        self.assertNotEqual(f.assess()['silver']['status'],'review_recorded')
        self.assertEqual(json.loads((f.base/'ledger.json').read_text()),ledger)

    def test_nl_setup_skips_lean_files_and_inherits_without_extra_flag(self):
        import test_setup as fixtures
        f=fixtures.SetupTests();f.setUp();self.addCleanup(f.doCleanups)
        env=f.fake_lake()
        result=f.run_setup('--nl',skip_mathlib=False,extra_env=env)
        self.assertEqual(result.returncode,0,result.stderr)
        for name in ['.mcp.json','lakefile.toml','lean-toolchain','MerLeanExperiment.lean','.merlean-setup-pending']:
            self.assertFalse((f.project/name).exists(),name)
        self.assertFalse((f.base/'lake.log').exists())
        (f.project/'.merlean-workspace.json').write_text('{}')
        result=f.run_setup(skip_mathlib=False,extra_env=env)
        self.assertEqual(result.returncode,0,result.stderr);self.assertFalse((f.base/'lake.log').exists())

    def test_nl_setup_preserves_existing_files_and_uses_nonlean_requirements(self):
        import test_setup as fixtures
        f=fixtures.SetupTests();f.setUp();self.addCleanup(f.doCleanups)
        f.project.mkdir()
        names=['.mcp.json','lakefile.toml','lean-toolchain','MerLeanExperiment.lean']
        for name in names:(f.project/name).write_text('preserve '+name)
        interpreter=f.runtime/'.venv/bin/python';interpreter.parent.mkdir(parents=True)
        log=f.base/'pip.log'
        interpreter.write_text('#!/bin/sh\nif [ "$1" = -m ] && [ "$2" = pip ] && [ "$3" = install ]; then printf "%s\\n" "$*" >> "'+str(log)+'"; fi\nexit 0\n')
        interpreter.chmod(0o755)
        result=f.run_setup('-NL',skip_venv=False,skip_mathlib=False)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('requirements-nl.txt',log.read_text())
        for name in names:self.assertEqual((f.project/name).read_text(),'preserve '+name)
        requirements=(ROOT/'src/requirements-nl.txt').read_text()
        self.assertNotIn('leanclient==',requirements);self.assertNotIn('lean-lsp-mcp==',requirements)
        self.assertEqual(requirements.splitlines()[1:],(ROOT/'src/requirements.txt').read_text().split('# lean-lsp-mcp')[0].splitlines())

    def test_selector_aliases_conflicts_and_resume_unknown(self):
        for args in [('-NL',),('--nl',),('-lite','-NL')]:
            run=subprocess.run([str(ROOT/'scripts/merlean-agent'),*args],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr);data=json.loads(run.stdout)
            self.assertTrue(data['nl_only']);self.assertEqual(data['grade_target'],'SILVER')
            self.assertEqual(data['agent'],'merlean-lite')
        for args in [('-heavy','--nl'),('--task','formalize','--nl'),('--paper-writing','--nl')]:
            self.assertNotEqual(subprocess.run([str(ROOT/'scripts/merlean-agent'),*args],capture_output=True).returncode,0)
        data=json.loads(subprocess.check_output([str(ROOT/'scripts/merlean-agent'),'--resume-mode','lite']))
        self.assertIsNone(data['lean_enabled']);self.assertEqual(data['capability_policy'],'inherit_persisted')

    def test_offline_cli_policy_inherits_and_reset_retains(self):
        data=self.root/'plan_data'
        args=[sys.executable,str(ROOT/'src/offline_cli.py'),'--data',str(data)]
        result=subprocess.run([*args,'--nl','list'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        for command in [['seed-sorries',str(self.root/'missing.lean'),'--lib-dir',str(self.root)],['sync-lean',str(self.root)],['reconcile',str(self.root),'--build']]:
            result=subprocess.run([*args,*command],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0);self.assertIn('NL mode',result.stderr)
        graph=OfflinePlanGraph(data)
        graph.add({'id':'r','type':'Lemma','name':'R','content':'Retained NL statement','dependencies':[],'hierarchy_level':0})
        graph.close()
        result=subprocess.run([*args,'reset'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr);self.assertTrue(c.nl_only(data))

    def test_setup_preserves_lexical_nl_when_project_path_is_symlink_routed(self):
        project=self.root/'nl';c.initialize(project,True)
        outside=self.root/'outside';outside.mkdir();link=project/'link';link.symlink_to(outside,target_is_directory=True)
        result=subprocess.run(['/bin/bash',str(ROOT/'scripts/setup.sh'),'--project',str(link/'new'),
            '--runtime',str(self.root/'runtime'),'--skip-venv'],cwd=self.root,text=True,capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue(c.nl_only(outside/'new'));self.assertFalse((outside/'new/lakefile.toml').exists())

    def test_setup_without_python_cannot_bypass_ancestor_policy(self):
        project=self.root/'nl';c.initialize(project,True)
        child=project/'child';tools=self.root/'tools';tools.mkdir()
        for name in ['dirname','mkdir','bash']:
            import shutil
            (tools/name).symlink_to(shutil.which(name))
        python=tools/'python3';python.write_text('#!/bin/sh\nexit 1\n');python.chmod(0o755)
        uv=tools/'uv';uv.write_text('#!/bin/sh\ntouch "'+str(self.root/'uv-ran')+'"\n');uv.chmod(0o755)
        result=subprocess.run(['/bin/bash',str(ROOT/'scripts/setup.sh'),'--project',str(child),'--runtime',str(self.root/'runtime')],
                              env={**os.environ,'PATH':str(tools)},cwd=self.root,text=True,capture_output=True)
        self.assertNotEqual(result.returncode,0);self.assertIn('validate inherited capability',result.stderr)
        self.assertFalse((self.root/'uv-ran').exists());self.assertFalse((child/'lakefile.toml').exists())

    def test_pilot_lexical_symlink_policy_rejected_before_new_or_continued_writes(self):
        project=self.root/'nl';c.initialize(project,True)
        outside=self.root/'outside';outside.mkdir();link=project/'link';link.symlink_to(outside,target_is_directory=True)
        target=link/'new'
        with patch.object(sys,'argv',['pilot',str(target),'--problems','missing.json','--lean-executable','/lean']):
            with self.assertRaises(SystemExit):p.main()
        self.assertFalse(target.exists())
        import test_pilot_continuation_runtime as fixtures
        f=fixtures.ContinuationRuntimeTests();f.setUp();self.addCleanup(f.doCleanups)
        with self.assertRaises(ValueError):f.prepare(root=target)
        self.assertFalse(target.exists())

    def test_new_pilot_persists_nl_before_any_worker_runs(self):
        original=self.root/'original.txt';original.write_text('Synthetic original task')
        mapping=self.root/'problems.json';mapping.write_text(json.dumps({'synthetic':str(original)}))
        target=self.root/'new-run'
        runner=SimpleNamespace(run=AsyncMock(return_value={'status':'not_launched'}))
        with patch.object(sys,'argv',['pilot',str(target),'--problems',str(mapping),'--nl']),\
             patch.object(p,'subscription_preflight',return_value={}),patch.object(p,'Pilot',return_value=runner):
            p.main()
        config=json.loads((target/'host-config.json').read_text())
        self.assertTrue(config['nl_only']);self.assertEqual(config['mode'],'lite')
        self.assertIsNone(config['lean_executable']);self.assertTrue(c.nl_only(target))
        self.assertEqual(config['original_scope_review_count'],2)

    def test_runtime_continuation_inherits_and_rejects_change_without_mutating_parent(self):
        import test_pilot_continuation_runtime as fixtures
        f=fixtures.ContinuationRuntimeTests();f.setUp();self.addCleanup(f.doCleanups)
        config=json.loads((f.fixture.source/'host-config.json').read_text());config['nl_only']=True
        f.fixture.write(f.fixture.source/'host-config.json',config)
        before={str(path):path.read_bytes() for path in f.fixture.source.rglob('*') if path.is_file()}
        with self.assertRaises(ValueError):f.prepare(nl_only_requested=False)
        self.assertFalse(f.root.exists())
        restored=f.prepare()
        self.assertTrue(restored['nl_only'])
        self.assertEqual(before,{str(path):path.read_bytes() for path in f.fixture.source.rglob('*') if path.is_file()})
        self.assertEqual(restored['original_scope_review_count'],2)

    def test_existing_pilot_toggle_rejects_before_runtime(self):
        (self.root/'host-config.json').write_text(json.dumps({'nl_only':False}))
        before=(self.root/'host-config.json').read_bytes()
        with patch.object(sys,'argv',['pilot',str(self.root),'--nl']),patch.object(p,'Pilot') as pilot:
            with self.assertRaises(ValueError):p.main()
            pilot.assert_not_called()
        self.assertEqual(before,(self.root/'host-config.json').read_bytes())

    def test_new_pilot_nl_conflict_rejects_before_preflight_or_create(self):
        c.initialize(self.root,True);target=self.root/'new'
        with patch.object(sys,'argv',['pilot',str(target),'--problems','missing.json','--lean-executable','/lean']),patch.object(p,'Pilot') as pilot:
            with self.assertRaises(SystemExit):p.main()
            pilot.assert_not_called()
        self.assertFalse(target.exists())

if __name__=='__main__':unittest.main()
