"""Deterministic quota handoff gates; no provider or research calls."""
import asyncio
from datetime import datetime,timezone,timedelta
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch,AsyncMock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import pilot_supervisor as outer
import pilot_quota_recheck as quota
from pilot_continuation_reservation import base_reservation

class QuotaTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name).resolve();self.root=self.base/'run';self.root.mkdir()
        self.state=self.base/'keeper';self.state.mkdir();self.home=self.base/'home';self.home.mkdir()
        self.binary=self.base/'codex';self.binary.write_text('synthetic wrapper')
        outer.save(self.home/'auth.json',{'tokens':{'account_id':'same-account'}})
        outer.save(self.root/'host-config.json',{'codex_binary':str(self.binary),'problems':['p'],
            'exam':{'submission_deadline_utc':(datetime.now(timezone.utc)+timedelta(hours=1)).isoformat()}})
        started=(datetime.now(timezone.utc)-timedelta(minutes=2)).isoformat()
        outer.save(self.state/'attempt.json',{'root':str(self.root),'created_utc':started})
        self.launch={'pid':987654,'process_identity':'owned','operation_started_utc':started,'attempt_sha256':outer.sha(self.state/'attempt.json')}
        outer.save(self.state/'launch.json',self.launch)
        outer.save(self.state/'status.json',{'status':'quota_paused','needs_attention':False,'exit_code':0})
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[{'problem':'p','status':'partial','operational_failure':'quota'}]})
        self.stage=self.root/'host/runtime/p/008-main';self.stage.mkdir(parents=True)
        outer.save(self.stage/'stage.meta.json',{'start_utc':outer.now(),'status':'process_failed'})
        (self.stage/'stage.events.jsonl').write_text(json.dumps({'event':{'type':'turn.failed','error':{'message':'usage limit reached'}}})+'\n')
        self.reconciliation=self.base/'reconciled.json'
        outer.save(self.reconciliation,{'host_pid':987654,'active_children':[],'pending_launches':[],'all_owned_children_stopped':True})
        self.route_path=self.base/'route.json'
        self.route={'schema_version':1,'authority':'explicit_operator_verified_selected_route','root':str(self.root),
            'attempt_sha256':outer.sha(self.state/'attempt.json'),'host_config_sha256':outer.sha(self.root/'host-config.json'),
            'codex_binary':str(self.binary),'codex_binary_sha256':outer.sha(self.binary),'codex_home':str(self.home),
            'auth_source':str(self.home/'auth.json'),'account_id':'same-account','environment':{'HOME':os.environ['HOME'],'CODEX_HOME':str(self.home)},
            'reconciliation':{'path':str(self.reconciliation),'sha256':outer.sha(self.reconciliation)}}
        self.reseal()
    def reseal(self):
        self.route['terminal_files']={str(p.relative_to(self.root)):outer.sha(p) for p in self.root.rglob('*') if p.is_file()}
        outer.save(self.route_path,self.route)
    def snapshot(self,used=0):
        return {'account_id':'same-account','limits_account_id':'same-account','account_type':'chatgpt','auth_unchanged':True,
            'cleanup':'exited_after_stdin_close','buckets':{'codex':{'primary':{'usedPercent':used,'windowDurationMins':10080,'resetsAt':2000000000},'secondary':None,
            'rateLimitReachedType':None,'spendControlReached':False,'individualLimitPresent':False}}}
    def check(self,value=None):
        with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}), \
             patch('pilot_continuation.validate_process_reconciliation'), \
             patch.object(quota,'query',new=AsyncMock(return_value=value or self.snapshot())) as query:
            result=quota.recheck(self.state,self.route_path)
        return result,query
    def assert_blocked(self):
        with patch.object(outer,'probe_process',return_value={'alive':False,'identity_match':None}), \
             patch('pilot_continuation.validate_process_reconciliation'),patch.object(quota,'query',new=AsyncMock()) as query:
            with self.assertRaises((ValueError,KeyError)):quota.recheck(self.state,self.route_path)
            query.assert_not_awaited()
        self.assertFalse((self.state/'quota-recheck-last-attempt.json').exists())
    def test_zero_is_observed_not_missing_and_never_model_availability(self):
        self.assertEqual(quota.classify(self.snapshot(0),'same-account'),'metadata_no_limit_observed')
        bad=self.snapshot();bad['buckets']['codex']['primary']={}
        self.assertEqual(quota.classify(bad,'same-account'),'unknown_incomplete_limits')
        result,query=self.check();self.assertEqual(query.await_count,1)
        self.assertEqual(result['status'],'saved_state_review_required');self.assertEqual(result['model_availability'],'UNKNOWN')
        self.assertTrue(result['needs_attention']);self.assertFalse(result['automatic_restart'])
        self.assertEqual(outer.read(self.state/'status.json')['status'],'quota_paused')
    def test_limits_mismatch_null_and_individual_cap_are_not_available(self):
        self.assertEqual(quota.classify(self.snapshot(100),'same-account'),'limit_reported')
        for change,expected in [('account','unknown_account_mismatch'),('null','unknown_incomplete_limits'),('individual','unknown_incomplete_limits')]:
            value=self.snapshot()
            if change=='account':value['account_id']='other'
            elif change=='null':value['buckets']['codex']['primary']=None
            else:value['buckets']['codex']['individualLimitPresent']=True
            self.assertEqual(quota.classify(value,'same-account'),expected)
    def test_throttle_and_unknown_cleanup_never_repeat_rpc(self):
        self.check()
        result,query=self.check();self.assertEqual(result['status'],'throttled');query.assert_not_awaited()
        record=outer.read(self.state/'quota-recheck-last-attempt.json');record['cleanup_unknown']=True
        outer.save(self.state/'quota-recheck-last-attempt.json',record)
        with self.assertRaises(ValueError):self.check()
    def test_healthy_status_and_live_or_unknown_host_block_before_attempt(self):
        for alive in [True,None]:
            with patch.object(outer,'probe_process',return_value={'alive':alive,'identity_match':True}),patch.object(quota,'query',new=AsyncMock()) as query:
                with self.assertRaises(ValueError):quota.recheck(self.state,self.route_path)
                query.assert_not_awaited()
        outer.save(self.state/'status.json',{'status':'running'});self.assert_blocked()
    def test_running_and_admitted_child_stages_block_even_with_dead_host(self):
        for state in ['running','admitted','launching','pending']:
            outer.save(self.stage/'stage.meta.json',{'start_utc':outer.now(),'status':state});self.reseal();self.assert_blocked()
    def test_native_descendant_or_probe_unknown_blocks_rpc(self):
        for reason in ['owned descendant remains','unknown document helper','unreconciled probe']:
            with patch.object(outer,'probe_process',return_value={'alive':False}), \
                 patch('pilot_continuation.validate_process_reconciliation',side_effect=ValueError(reason)),patch.object(quota,'query',new=AsyncMock()) as query:
                with self.assertRaises(ValueError):quota.recheck(self.state,self.route_path)
                query.assert_not_awaited()
            self.assertFalse((self.state/'quota-recheck-last-attempt.json').exists())
    def test_pending_review_launch_without_pid_blocks_rpc(self):
        receipt=outer.read(self.reconciliation);receipt['pending_launches']=['admitted-review'];outer.save(self.reconciliation,receipt)
        self.route['reconciliation']['sha256']=outer.sha(self.reconciliation);self.reseal();self.assert_blocked()
    def test_historical_quota_and_recovered_success_are_excluded(self):
        outer.save(self.stage/'stage.meta.json',{'start_utc':'2000-01-01T00:00:00+00:00','status':'process_failed'});self.reseal();self.assert_blocked()
        outer.save(self.stage/'stage.meta.json',{'start_utc':outer.now(),'status':'process_failed'})
        config=outer.read(self.root/'host-config.json');config.pop('exam');outer.save(self.root/'host-config.json',config)
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[{'problem':'p','status':'complete'}]});self.reseal();self.assert_blocked()
    def test_successor_reservation_disables_historical_recheck(self):
        p=base_reservation(self.root);p.parent.mkdir();p.write_text('prepared successor')
        self.assert_blocked()
    def test_changed_route_or_terminal_tree_blocks_rpc(self):
        self.binary.write_text('changed');self.assert_blocked()
        self.route['codex_binary_sha256']=outer.sha(self.binary);self.reseal()
        (self.root/'new-evidence').write_text('new lower activity');self.assert_blocked()
    def test_owner_lock_prevents_concurrent_query(self):
        with outer.owner(self.state),patch.object(quota,'query',new=AsyncMock()) as query:
            with self.assertRaises(RuntimeError):quota.recheck(self.state,self.route_path)
            query.assert_not_awaited()
    def test_terminal_watch_reentry_corrects_attention_without_rpc(self):
        with patch.object(quota,'query',new=AsyncMock()) as query:
            report=outer.watch(self.state,once=True)
            self.assertTrue(report['needs_attention']);self.assertEqual(report['status'],'quota_paused');query.assert_not_awaited()
    def test_diagnosis_needs_whole_stack_and_never_runs_when_healthy(self):
        for status in ['running','quota_paused']:
            with patch.object(outer,'watch',return_value={'status':status}),patch.object(outer,'diagnostic_quiescence') as guard:
                with self.assertRaises(ValueError):outer.diagnostic_packet(self.state)
                guard.assert_not_called()
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[{'problem':'p','status':'partial','operational_failure':'infrastructure'}]});self.reseal()
        with patch.object(outer,'probe_process',return_value={'alive':False}):
            with self.assertRaises(FileNotFoundError):outer.diagnostic_quiescence(self.state)
        outer.save(self.state/'diagnostic-reconciliation.json',{'reconciliation':self.route['reconciliation'],'terminal_files':self.route['terminal_files']})
        with patch.object(outer,'probe_process',return_value={'alive':False}),patch('pilot_continuation.validate_process_reconciliation') as validate:
            outer.diagnostic_quiescence(self.state);validate.assert_called_once()
        config=outer.read(self.root/'host-config.json');config.pop('exam');outer.save(self.root/'host-config.json',config)
        outer.save(self.root/'pilot-result.json',{'end_utc':outer.now(),'results':[{'problem':'p','status':'complete'}]});self.reseal()
        outer.save(self.state/'diagnostic-reconciliation.json',{'reconciliation':self.route['reconciliation'],'terminal_files':self.route['terminal_files']})
        with patch.object(outer,'probe_process',return_value={'alive':False}),patch('pilot_continuation.validate_process_reconciliation') as validate:
            with self.assertRaisesRegex(ValueError,'current operation'):outer.diagnostic_quiescence(self.state)
            validate.assert_not_called()
    def test_recipe_is_opt_in_bound_and_scheduled_healthy_gate_has_no_rpc(self):
        with patch.object(outer,'probe_process',return_value={'alive':False}),patch('pilot_continuation.validate_process_reconciliation'):
            result=quota.recipe(self.state,self.route_path)
        self.assertEqual(result['status'],'recipe_created_not_installed')
        outer.save(self.state/'status.json',{'status':'running'})
        with patch.object(quota,'query',new=AsyncMock()) as query:
            with self.assertRaises(ValueError):quota.scheduled(self.state)
            query.assert_not_awaited()
    def test_crash_without_current_result_is_new_failure_even_without_old_stage_error(self):
        (self.root/'pilot-result.json').unlink()
        (self.stage/'stage.events.jsonl').write_text(json.dumps({'event':{'type':'turn.failed','error':{'message':'connection closed'}}})+'\n')
        self.reseal()
        outer.save(self.state/'diagnostic-reconciliation.json',{'reconciliation':self.route['reconciliation'],'terminal_files':self.route['terminal_files']})
        with patch.object(outer,'probe_process',return_value={'alive':False}),patch('pilot_continuation.validate_process_reconciliation') as validate:
            outer.diagnostic_quiescence(self.state);validate.assert_called_once()
        outer.save(self.stage/'stage.meta.json',{'start_utc':'2000-01-01T00:00:00+00:00','status':'process_failed'});self.reseal()
        outer.save(self.state/'diagnostic-reconciliation.json',{'reconciliation':self.route['reconciliation'],'terminal_files':self.route['terminal_files']})
        with patch.object(outer,'probe_process',return_value={'alive':False}),patch('pilot_continuation.validate_process_reconciliation') as validate:
            outer.diagnostic_quiescence(self.state);validate.assert_called_once()
            self.assertEqual(outer.failure_evidence(self.root,since=self.launch['operation_started_utc']),[])
    def test_expired_exam_does_not_query_or_extend_clock(self):
        config=outer.read(self.root/'host-config.json');config['exam']['submission_deadline_utc']=(datetime.now(timezone.utc)-timedelta(minutes=1)).isoformat()
        outer.save(self.root/'host-config.json',config);self.route['host_config_sha256']=outer.sha(self.root/'host-config.json');self.reseal()
        result,query=self.check();self.assertEqual(result['status'],'exam_deadline_passed');query.assert_not_awaited()
        self.assertEqual(outer.read(self.root/'host-config.json'),config)
    def test_missing_reset_or_duration_is_unknown(self):
        for field in ['windowDurationMins','resetsAt']:
            value=self.snapshot();del value['buckets']['codex']['primary'][field]
            self.assertEqual(quota.classify(value,'same-account'),'unknown_incomplete_limits')
    def test_rpc_actual_subprocess_sends_only_allowlisted_methods(self):
        fake=self.base/'fake';fake.write_text('#!'+sys.executable+'\n'+'''import sys,json
for line in sys.stdin:
 q=json.loads(line)
 if 'id' not in q:continue
 assert q['method'] in ['initialize','account/read','account/rateLimits/read']
 if q['id']==1:r={}
 elif q['id']==2:r={'account':{'type':'chatgpt'},'workspaceRouting':{'chatgptAccountId':'same-account'}}
 else:r={'accountId':'same-account','rateLimits':{'primary':{'usedPercent':0,'windowDurationMins':10080,'resetsAt':2000000000},'secondary':None,'rateLimitReachedType':None,'spendControlReached':False,'individualLimit':None}}
 print(json.dumps({'id':q['id'],'result':r}),flush=True)
''');fake.chmod(0o755)
        result=asyncio.run(quota.query({**self.route,'codex_binary':str(fake)},self.base))
        self.assertEqual(quota.classify(result,'same-account'),'metadata_no_limit_observed')
        self.assertEqual(result['rpc_methods'],['initialize','account/read','account/rateLimits/read'])
        self.assertEqual(result['model_calls'],0);self.assertEqual(result['cleanup'],'exited_after_stdin_close')
    def test_rpc_timeout_reaps_owned_process(self):
        fake=self.base/'fake';fake.write_text('#!'+sys.executable+'\nimport time\ntime.sleep(60)\n');fake.chmod(0o755)
        with patch.object(quota,'RPC_TIMEOUT_SECONDS',0.05):result=asyncio.run(quota.query({**self.route,'codex_binary':str(fake)},self.base))
        self.assertEqual(result['error_type'],'TimeoutError');self.assertEqual(result['cleanup'],'owned_group_killed_and_reaped')
        with self.assertRaises(ProcessLookupError):os.kill(result['helper_pid'],0)
