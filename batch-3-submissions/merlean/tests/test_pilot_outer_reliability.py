"""Synthetic ownership, provider pause and copied MCP startup regressions."""
import asyncio
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_supervisor as outer
import pilot_document_startup as startup
import pilot_document_tools as documents
import codex_transport as transport

class ReliabilityTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name).resolve()
 def scope(self):
  stage=self.root/'stage';stage.mkdir()
  spec={'schema_version':1,'mode':'review','problem_id':'synthetic','original_sha256':'a'*64,
    'main_session':'main','store_root':str(self.root),'readonly_artifacts':{},'required_artifact_ids':[],'inline_artifact_ids':[]}
  scope,cap=documents.prepare_scope(spec,stage,{'stage':'test','request_id':'synthetic','session_id':None})
  return scope,cap,startup.prepare_runtime(stage)
 def test_copy_runs_without_source_path_and_checks_dependency(self):
  scope,cap,runtime=self.scope()
  requests='\n'.join(json.dumps({'jsonrpc':'2.0','id':i,'method':m,'params':{}}) for i,m in [(1,'initialize'),(2,'tools/list')])+'\n'
  result=subprocess.run([sys.executable,'-B',runtime['path'],'--scope',cap['path'],'--sha256',cap['sha256']],input=requests,text=True,capture_output=True,env={'PATH':os.environ['PATH']},cwd=self.root,timeout=5)
  self.assertEqual(result.returncode,0,result.stderr)
  output=[json.loads(l) for l in result.stdout.splitlines()]
  self.assertEqual(output[1]['result']['tools'],documents.tool_definitions('review'))
  self.assertFalse(Path(scope['receipt_path']).exists())
  Path(runtime['path']).with_name('pilot_proof_document.py').write_text('# changed')
  with self.assertRaises(ValueError):startup.verify_runtime(runtime)
 def test_actual_cli_boundary_inventory_without_model(self):
  scope,cap,runtime=self.scope()
  script=self.root/'fake-codex'
  script.write_text('#!'+sys.executable+'\n'+'''import json,sys,subprocess,tomllib
assert sys.argv[1]=='app-server'
disabled={sys.argv[i+1] for i,arg in enumerate(sys.argv[:-1]) if arg=='--disable'}
assert {'apps','plugins','enable_mcp_apps','remote_plugin','plugin_sharing'} <= disabled
cfg=tomllib.loads(sys.argv[sys.argv.index('-c')+1])['mcp_servers']['merlean_documents']
for line in sys.stdin:
 q=json.loads(line)
 assert q['method'] in ('initialize','initialized','mcpServerStatus/list')
 if q['method']=='initialized': continue
 if q['method']=='initialize': result={}
 else:
  data=''.join(json.dumps({'id':i,'method':m,'params':{}})+'\\n' for i,m in [(1,'initialize'),(2,'tools/list')])
  child=subprocess.run([cfg['command'],*cfg['args']],input=data,text=True,capture_output=True,check=True)
  responses=[json.loads(l)['result'] for l in child.stdout.splitlines()]
  result={'data':[{'name':'merlean_documents','serverInfo':responses[0]['serverInfo'],'tools':{x['name']:x for x in responses[1]['tools']}}]}
 print(json.dumps({'id':q['id'],'result':result}),flush=True)
''');script.chmod(0o755)
  value=asyncio.run(startup.startup_preflight(str(script),cap,runtime,'review',cwd=self.root,env={'PATH':os.environ['PATH']},timeout=5))
  self.assertEqual(value['model_calls'],0);self.assertEqual(value['turn_requests'],0);self.assertEqual(value['status'],'PASS')
 def rpc_frame_program(self, payload):
  response=self.root/'rpc-response.json';response.write_text(json.dumps(payload))
  script=self.root/'framed-codex'
  script.write_text('#!'+sys.executable+'\n'+"import json,sys,os\nfrom pathlib import Path\nPath("+repr(str(self.root/'rpc-child.pid'))+").write_text(str(os.getpid()))\nfor line in sys.stdin:\n q=json.loads(line)\n if q['method']=='initialized': continue\n if q['id']==1: print(json.dumps({'id':1,'result':{}}),flush=True)\n else: print(Path("+repr(str(response))+").read_text(),flush=True)\n")
  script.chmod(0o755);return script
 def test_startup_uses_paid_offline_feature_boundary(self):
  _,cap,runtime=self.scope()
  command=startup.startup_command('codex',cap,runtime)
  disabled=[command[i+1] for i,item in enumerate(command[:-1]) if item=='--disable']
  self.assertEqual(disabled,list(transport.DISABLED_FEATURES))
 def test_configured_names_literal_keys_and_reserved_rejection(self):
  import tomllib
  _,cap,runtime=self.scope()
  config=self.root/'config.toml'
  config.write_text('[mcp_servers."a.b"]\ncommand="DO NOT EXECUTE"\n')
  names=startup.configured_mcp_names({'CODEX_HOME':str(self.root)})
  self.assertEqual(names,['a.b'])
  command=startup.startup_command('codex',cap,runtime,disabled_names=names)
  servers=tomllib.loads(command[command.index('-c')+1])['mcp_servers']
  self.assertEqual(servers['a.b']['enabled'],False)
  self.assertNotIn('DO NOT EXECUTE',str(command))
  config.write_text('[mcp_servers.merlean_documents]\ncommand="ignored"\n')
  with self.assertRaisesRegex(RuntimeError,'reserved'):startup.configured_mcp_names({'CODEX_HOME':str(self.root)})
 def test_only_explicitly_disabled_fully_inert_servers_tolerated(self):
  _,cap,runtime=self.scope()
  (self.root/'config.toml').write_text('[mcp_servers."a.b"]\ncommand="ignored"\n')
  target={'name':'merlean_documents','serverInfo':{'name':'merlean_documents','version':'1'},'tools':{item['name']:item for item in documents.tool_definitions('review')}}
  inert={'name':'a.b','tools':{},'resources':[],'resourceTemplates':[],'serverInfo':None,'enabled':False}
  env={'PATH':os.environ['PATH'],'CODEX_HOME':str(self.root)}
  script=self.rpc_frame_program({'id':2,'result':{'data':[target,inert]}})
  value=asyncio.run(startup.startup_preflight(str(script),cap,runtime,'review',cwd=self.root,env=env,timeout=5))
  self.assertEqual(value['disabled_mcp_servers'],['a.b'])
  for changes in ({'name':'unknown'},{'tools':{'x':{}}},{'resources':[{}]},{'resourceTemplates':[{}]},{'serverInfo':{}},{'enabled':True},{'toolsError':'failed'}):
   with self.subTest(changes=changes):
    script=self.rpc_frame_program({'id':2,'result':{'data':[target,{**inert,**changes}]}})
    with self.assertRaisesRegex(RuntimeError,'unexpected document MCP inventory'):
     asyncio.run(startup.startup_preflight(str(script),cap,runtime,'review',cwd=self.root,env=env,timeout=5))
 def test_unexpected_server_still_fails_closed_and_reaps(self):
  _,cap,runtime=self.scope()
  target={'name':'merlean_documents','serverInfo':{'name':'merlean_documents','version':'1'},
   'tools':{item['name']:item for item in documents.tool_definitions('review')}}
  script=self.rpc_frame_program({'id':2,'result':{'data':[target,{'name':'codex_apps','tools':{}}]}})
  with self.assertRaisesRegex(RuntimeError,'unexpected document MCP inventory'):
   asyncio.run(startup.startup_preflight(str(script),cap,runtime,'review',cwd=self.root,env={'PATH':os.environ['PATH']},timeout=5))
  pid=int((self.root/'rpc-child.pid').read_text())
  with self.assertRaises(ProcessLookupError):os.kill(pid,0)
 def test_inventory_schema_frame_over_64k_succeeds_without_model(self):
  scope,cap,runtime=self.scope();definitions=documents.tool_definitions('review')
  # Real fixed tool schemas plus a permitted large MCP server description.
  server={'name':'merlean_documents','serverInfo':{'name':'merlean_documents','version':'1',
   'description':json.dumps(definitions)*100},'tools':{item['name']:item for item in definitions}}
  payload={'id':2,'result':{'data':[server]}}
  self.assertGreater(len(json.dumps(payload).encode()),65536)
  script=self.rpc_frame_program(payload)
  value=asyncio.run(startup.startup_preflight(str(script),cap,runtime,'review',cwd=self.root,env={'PATH':os.environ['PATH']},timeout=5))
  self.assertEqual(value['status'],'PASS');self.assertEqual(value['model_calls'],0)
  pid=int((self.root/'rpc-child.pid').read_text())
  with self.assertRaises(ProcessLookupError):os.kill(pid,0)
 def test_over_limit_inventory_fails_and_reaps_owned_cli(self):
  scope,cap,runtime=self.scope()
  script=self.rpc_frame_program({'id':2,'result':{'oversized':'x'*(startup.MCP_RPC_LINE_LIMIT+1)}})
  with self.assertRaisesRegex(RuntimeError,'frame exceeds bounded line limit'):
   asyncio.run(startup.startup_preflight(str(script),cap,runtime,'review',cwd=self.root,env={'PATH':os.environ['PATH']},timeout=5))
  pid=int((self.root/'rpc-child.pid').read_text())
  with self.assertRaises(ProcessLookupError):os.kill(pid,0)
 def test_document_preflight_failure_has_terminal_receipt(self):
  scope,_,_=self.scope();spec={k:v for k,v in scope.items() if k not in {'producer','receipt_path'}}
  with patch.object(transport,'subscription_preflight',return_value={'authentication':'chatgpt','cli_version':'codex-cli 0.157.1'}),patch('pilot_document_startup.startup_preflight',side_effect=TimeoutError('synthetic')),patch.object(transport,'_command') as paid:
   with self.assertRaises(TimeoutError):asyncio.run(transport.call_stage(self.root/'host','p/001-main','synthetic','gpt-6-astra',5,internet_browse=False,document_scope=spec))
  meta=json.loads((self.root/'host/runtime/p/001-main/stage.meta.json').read_text())
  self.assertEqual(meta['status'],'process_launch_failed');self.assertFalse(meta['model_dispatched']);self.assertIsNone(meta['session_id']);paid.assert_not_called()
 def test_unresolved_helper_blocks_next_stage_before_any_subprocess(self):
  host=self.root/'host';receipt=host/'runtime/p/001-main/document-startup.json';receipt.parent.mkdir(parents=True)
  receipt.write_text(json.dumps({'status':'FAIL','cleanup':{'status':'UNKNOWN','pid':123}}))
  with patch.object(transport,'subscription_preflight') as authentication,patch.object(transport.asyncio,'create_subprocess_exec') as spawn:
   with self.assertRaises(RuntimeError):asyncio.run(transport.call_stage(host,'p/002-main','synthetic','gpt-6-astra',5,internet_browse=False))
  authentication.assert_not_called();spawn.assert_not_called()
 def test_unknown_helper_identity_returns_without_signal_or_unbounded_wait(self):
  scope,cap,runtime=self.scope()
  fake=Mock();fake.pid=123;fake.returncode=None;fake.stdin.write=Mock();fake.stdin.drain=AsyncMock()
  fake.stdout.readline=AsyncMock(side_effect=[b'{"id":1,"result":{}}\n',b'{"id":2,"result":{"data":[]}}\n'])
  fake.wait=AsyncMock()
  with patch.object(startup.asyncio,'create_subprocess_exec',new=AsyncMock(return_value=fake)),patch.object(startup,'helper_identity',return_value=None),patch.object(startup.os,'killpg') as kill:
   with self.assertRaises(startup.StartupOwnershipError):asyncio.run(startup.startup_preflight('synthetic',cap,runtime,'review',cwd=self.root,env={},timeout=1))
  kill.assert_not_called();fake.wait.assert_not_awaited()
 def test_health_within_deadline_and_overdue_stale_watchdog(self):
  root=self.root/'run';p=root/'host/runtime/p/001-main';p.mkdir(parents=True)
  now=datetime.now(timezone.utc)
  meta={'status':'running','start_utc':(now-timedelta(minutes=10)).isoformat(),'deadline_utc':(now+timedelta(minutes=10)).isoformat()}
  (p/'stage.meta.json').write_text(json.dumps(meta));cfg={'watchdog_enabled':True,'watchdog_interval_seconds':300}
  self.assertEqual(outer.health_observations(root,cfg,(now-timedelta(hours=1)).isoformat()),[])
  meta['deadline_utc']=(now-timedelta(minutes=1)).isoformat();(p/'stage.meta.json').write_text(json.dumps(meta))
  findings=outer.health_observations(root,cfg,(now-timedelta(hours=1)).isoformat())
  self.assertEqual({x['kind'] for x in findings},{'stage_deadline_overdue','watchdog_stale_or_missing'})
  self.assertTrue(all(x['automatic_action'] is False for x in findings))
 def test_interrupted_paper_rebases_live_storage_preserving_work_and_reviews(self):
  import shutil
  from pilot_exam import rebase_copied_paper_state
  from paper_writing_codex.workflow import init_compose,verify_output
  old=self.root/'old-exam';paper=old/'papers/p';paper.mkdir(parents=True)
  output=paper/'paper.tex';work=paper/'work';init_compose(output,work,profile='exam')
  output.write_text('preserved working manuscript')
  snapshot=paper/'snapshot';snapshot.mkdir();(snapshot/'manifest.json').write_text('{"files":{}}')
  (paper/'review-1.json').write_text('{"finding":"unresolved"}')
  ledger={'snapshot':str(snapshot),'snapshot_manifest':{'path':str(snapshot/'manifest.json'),'sha256':outer.sha(snapshot/'manifest.json')},'best_available_tex':str(output),'stage':'reader-2','completed':['reconstruct','reader-1'],'writer_session':'saved-writer','reader_1':'saved-reviewer','calls':[{'name':'p/paper-001-reconstruct'}]}
  (paper/'paper-ledger.json').write_text(json.dumps(ledger))
  before={str(p.relative_to(old)):outer.sha(p) for p in old.rglob('*') if p.is_file()}
  new=self.root/'new-exam';shutil.copytree(old,new);rebase_copied_paper_state(old,new)
  moved=outer.read(new/'papers/p/paper-ledger.json');state=outer.read(new/'papers/p/work/00-run-state.json')
  self.assertEqual(moved['stage'],'reader-2');self.assertEqual(moved['completed'],ledger['completed']);self.assertEqual(moved['writer_session'],'saved-writer');self.assertEqual(moved['calls'],ledger['calls'])
  self.assertEqual(Path(state['output']),new/'papers/p/paper.tex');self.assertEqual(Path(state['work_dir']),new/'papers/p/work');verify_output(state,require_reservation=True)
  self.assertEqual((new/'papers/p/paper.tex').read_text(),'preserved working manuscript');self.assertEqual((new/'papers/p/review-1.json').read_bytes(),(paper/'review-1.json').read_bytes())
  self.assertEqual(before,{str(p.relative_to(old)):outer.sha(p) for p in old.rglob('*') if p.is_file()})
 def test_identity_waits_until_postexec_fingerprint_settles(self):
  child=Mock();child.pid=123;child.poll.return_value=None
  with patch.object(outer,'capture_process_identity',side_effect=['launcher','runtime','runtime']),patch.object(outer.time,'sleep'):
   self.assertEqual(outer.settled_identity(child),'runtime')
 def test_cancel_during_spawn_retains_and_cleans_owned_handle(self):
  scope,cap,runtime=self.scope();fake=Mock();fake.pid=123;fake.returncode=None;fake.wait=AsyncMock(return_value=-9)
  async def scenario():
   began=asyncio.Event();finish=asyncio.Event()
   async def spawn(*args,**kwargs):began.set();await finish.wait();return fake
   with patch.object(startup.asyncio,'create_subprocess_exec',side_effect=spawn),patch.object(startup,'helper_identity',return_value='owned'),patch.object(startup.os,'killpg') as kill:
    task=asyncio.create_task(startup.startup_preflight('synthetic',cap,runtime,'review',cwd=self.root,env={},timeout=5))
    await began.wait();task.cancel();finish.set()
    with self.assertRaises(asyncio.CancelledError):await task
    kill.assert_called_once_with(123,signal.SIGKILL);fake.wait.assert_awaited_once()
  asyncio.run(scenario())
 def test_diagnosis_request_is_small_once_and_usage_not_invented(self):
  state=self.root/'state';state.mkdir();outer.save(state/'attempt.json',{'root':str(self.root/'run')});outer.save(state/'status.json',{'status':'infrastructure_failed','exit_code':1})
  report={'status':'infrastructure_failed','exit_code':1,'evidence':[],'process':{'alive':False,'identity_match':None}}
  with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnostic_quiescence'):
   packet=outer.diagnostic_packet(state)
   self.assertTrue(all('excerpt' in v and v['complete_file'] is False for v in packet['source'].values()))
   answer={'kind':'infrastructure_repair_proposal','diagnosis':'need more infrastructure evidence','evidence_sha256':outer.digest(json.dumps(packet,sort_keys=True).encode()),'patches':[],'tests':[]}
   with patch.object(transport,'call_stage',new=AsyncMock(return_value=({'status':'completed','usage':None},answer))) as call:
    result=outer.diagnose(state)
    self.assertLessEqual(len(call.call_args.args[2].encode()),24576);self.assertEqual(call.call_args.args[4],60);self.assertEqual(call.call_args.kwargs['reasoning_effort'],'low')
    self.assertEqual(result['metering'],'UNKNOWN');self.assertFalse(result['verified_billed_token_cap'])
    with self.assertRaises(FileExistsError):outer.diagnose(state)
    self.assertEqual(call.await_count,1)
 def test_successful_terminal_and_scientific_partial_suppress_recovered_fault_debug(self):
  self.stage('2026-03-01T00:00:00+00:00',{'type':'turn.failed','error':{'message':'usage limit reached'}})
  root=self.root/'run';outer.save(root/'host-config.json',{'problems':['p']})
  launch={'pid':123,'process_identity':'owned','operation_started_utc':'2026-02-01T00:00:00+00:00'}
  state=self.root/'keeper';state.mkdir();outer.save(state/'keeper-plan.json',{'root':str(root),'pilot_arguments':[],'diagnose_on_failure':True});outer.save(state/'attempt.json',{})
  for status in ('complete','partial'):
   outer.save(root/'pilot-result.json',{'end_utc':datetime.now(timezone.utc).isoformat(),'results':[{'problem':'p','status':status,'errors':[{'type':'transient_capacity'}]}]})
   with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):
    report=outer.observation(root,launch,exit_code=0)
   self.assertEqual(report['status'],'exited')
   with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnose') as diagnose:
    outer.keep(state)
   diagnose.assert_not_called()
 def test_current_terminal_infrastructure_or_quota_failure_remains_actionable(self):
  root=self.root/'run';root.mkdir();outer.save(root/'host-config.json',{'problems':['p']})
  launch={'pid':123,'process_identity':'owned','operation_started_utc':'2026-02-01T00:00:00+00:00'}
  for kind,expected in [('infrastructure','infrastructure_failed'),('quota','quota_paused')]:
   outer.save(root/'pilot-result.json',{'end_utc':datetime.now(timezone.utc).isoformat(),'results':[{'problem':'p','status':'partial','operational_failure':kind}]})
   with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):
    self.assertEqual(outer.observation(root,launch,exit_code=0)['status'],expected)
 def test_paper_incomplete_is_attention_without_automatic_diagnosis(self):
  root=self.root/'run';root.mkdir();outer.save(root/'host-config.json',{'problems':['p']})
  launch={'pid':123,'process_identity':'owned','operation_started_utc':'2026-02-01T00:00:00+00:00'}
  paper_root=root/'exam/papers/p';paper_root.mkdir(parents=True)
  (paper_root/'paper.tex').write_text('synthetic paper');(paper_root/'final.pdf').write_bytes(b'%PDF-synthetic')
  for paper_status,expected in [({'status':'incomplete','terminal':False},'paper_incomplete'),
    ({'status':'incomplete','terminal':False,'operational_failure':'infrastructure'},'infrastructure_failed'),
    ({'status':'polished','terminal':True,'polishing_complete':True,'best_available_tex':str(paper_root/'paper.tex'),'best_available_pdf':str(paper_root/'final.pdf'),'errors':[{'type':'FileExistsError'}]},'exited')]:
   outer.save(root/'pilot-result.json',{'end_utc':datetime.now(timezone.utc).isoformat(),'results':[{'problem':'p','status':'complete','paper':paper_status}]})
   with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):report=outer.observation(root,launch,exit_code=0)
   self.assertEqual(report['status'],expected);self.assertEqual(report['needs_attention'],expected!='exited')
   if expected=='paper_incomplete':
    state=self.root/'state';state.mkdir();outer.save(state/'keeper-plan.json',{'diagnose_on_failure':True});outer.save(state/'attempt.json',{})
    with patch.object(outer,'watch',return_value=report),patch.object(outer,'diagnose') as diagnose:
     outer.keep(state);diagnose.assert_not_called()
 def test_lock_and_durable_claim_cannot_be_reused(self):
  state=self.root/'state'
  with outer.owner(state):
   with self.assertRaises(RuntimeError):
    with outer.owner(state):pass
   outer.save(state/'attempt.json',{'one':True},exclusive=True)
   with self.assertRaises(FileExistsError):outer.save(state/'attempt.json',{},exclusive=True)
 def test_missing_launch_receipt_never_dispatches(self):
  state=self.root/'state';state.mkdir();outer.save(state/'attempt.json',{'root':str(self.root/'run')})
  with patch.object(outer.subprocess,'Popen') as launch:
   result=outer.watch(state,once=True)
  launch.assert_not_called();self.assertEqual(result['status'],'launch_uncertain')
 def test_reused_pid_does_not_signal_or_restart(self):
  root=self.root/'run';root.mkdir()
  with patch.object(outer,'probe_process',return_value={'alive':True,'identity_match':False}),patch.object(outer.os,'killpg') as kill:
   result=outer.observation(root,{'pid':123,'process_identity':'old','operation_started_utc':'2026-01-01T00:00:00+00:00'})
  self.assertEqual(result['status'],'reconciliation_required');kill.assert_not_called()
 def stage(self, start, event, name='001-main'):
  p=self.root/'run/host/runtime/p'/name;p.mkdir(parents=True)
  (p/'stage.meta.json').write_text(json.dumps({'start_utc':start,'status':'process_failed','exit_code':1}))
  (p/'stage.events.jsonl').write_text(json.dumps({'event':event})+'\n'+ '{truncated')
  return p
 def test_historical_quota_excluded_and_partial_json_safe(self):
  self.stage('2026-01-01T00:00:00+00:00',{'type':'turn.failed','error':{'message':'usage limit reached'}})
  launch={'pid':123,'process_identity':'owned','operation_started_utc':'2026-02-01T00:00:00+00:00'}
  with patch.object(outer,'probe_process',return_value={'alive':True,'identity_match':True}):
   self.assertEqual(outer.observation(self.root/'run',launch)['status'],'running')
  self.stage('2026-03-01T00:00:00+00:00',{'type':'turn.failed','error':{'message':'usage limit reached'}},'002-main')
  with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}):
   self.assertEqual(outer.observation(self.root/'run',launch)['status'],'quota_paused')
 def test_model_prose_cannot_trigger_quota(self):
  self.stage('2026-03-01T00:00:00+00:00',{'type':'item.completed','item':{'type':'agent_message','text':'quota exceeded'}})
  values=outer.failure_evidence(self.root/'run');self.assertEqual(values[0]['failure_codes'],[])
 def test_quota_diagnosis_blocks_before_reservation_or_model(self):
  state=self.root/'state';state.mkdir()
  with patch.object(outer,'watch',return_value={'status':'quota_paused'}),patch.object(transport,'call_stage') as call:
   with self.assertRaises(ValueError):outer.diagnose(state)
  call.assert_not_called();self.assertFalse((state/'diagnostic-attempt.json').exists())
 def test_proposal_cannot_target_scientific_files_or_changed_source(self):
  packet={'source':{'pilot_supervisor.py':{'sha256':'a'*64}}}
  answer={'kind':'infrastructure_repair_proposal','diagnosis':'synthetic','evidence_sha256':outer.digest(json.dumps(packet,sort_keys=True).encode()),'patches':[{'path':'pilot_supervisor.py','base_sha256':'a'*64,'unified_diff':'synthetic'}],'tests':[]}
  self.assertEqual(outer.validate_proposal(answer,packet),answer)
  answer['patches'][0]['path']='codex_pilot.py'
  with self.assertRaises(ValueError):outer.validate_proposal(answer,packet)
 def test_keeper_reentry_only_watches_and_does_not_repeat_diagnosis(self):
  state=self.root/'state';state.mkdir();outer.save(state/'keeper-plan.json',{'root':str(self.root/'run'),'pilot_arguments':['--problems','synthetic'],'diagnose_on_failure':True});outer.save(state/'attempt.json',{})
  outer.save(state/'diagnostic-attempt.json',{})
  with patch.object(outer,'watch',return_value={'status':'infrastructure_failed'}),patch.object(outer,'run') as run,patch.object(outer,'diagnose') as diagnose:
   outer.keep(state)
  run.assert_not_called();diagnose.assert_not_called()
 def test_recipe_binds_environment_without_installing(self):
  import plistlib
  state=self.root/'state';result=outer.recipe(state,self.root/'run',['--problems','synthetic'])
  plan=outer.read(state/'keeper-plan.json');plist=plistlib.loads((state/'keeper.plist').read_bytes())
  self.assertEqual(plist['EnvironmentVariables'],plan['environment']);self.assertEqual(plist['WorkingDirectory'],str(self.root));self.assertEqual(plist['KeepAlive'],{'SuccessfulExit':False});self.assertEqual(result['status'],'recipe_created_not_installed')
if __name__=='__main__':unittest.main()
