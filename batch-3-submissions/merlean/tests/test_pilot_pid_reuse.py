"""Numeric PID reuse never substitutes for identity-bound stopped ownership."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch
import test_pilot_continuation as fixtures
import pilot_continuation as p
import campaign_watchdog

class PidReuseTests(unittest.TestCase):
    def setUp(self):
        self.f=fixtures.ContinuationTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        self.pid=900003
        self.path=self.f.source/'host/runtime/problem/003-proof-review/stage.meta.json'
        self.stage=json.loads(self.path.read_text())
        self.stage.update(exit_code=0,process_identity='a'*64,start_utc='2026-01-01T00:01:00Z',end_utc='2026-01-01T00:02:00Z')
        self.f.write(self.path,self.stage)
        progress=json.loads((self.f.folder/'host-progress.json').read_text())
        progress['calls'][2]=copy.deepcopy(self.stage)
        self.f.write(self.f.folder/'host-progress.json',progress)
        self.line='Fri Jan  2 12:00:00 2026 /unrelated/browser'
        self.fingerprint=hashlib.sha256(self.line.encode()).hexdigest()
        self.receipt=json.loads(self.f.receipt.read_text())
        self.receipt['checked_utc']='2026-01-03T00:00:00Z'
        self.receipt['reused_pids']=[{'pid':self.pid,'current_process_identity':self.fingerprint,
            'observed_utc':'2026-01-02T23:00:00Z','stage_receipts':[
                {'path':str(self.path.relative_to(self.f.source)),'sha256':p._hash(self.path)}]}]
        self.table=f'{self.pid} 1 {self.pid} {self.line}\n'
        self.second_identity=self.fingerprint
        self.kill_error=None

    def kill(self,pid,signal):
        self.assertEqual(signal,0)
        if pid==self.pid:
            if self.kill_error:raise self.kill_error
            return
        raise ProcessLookupError()

    def ps(self,args,**kwargs):
        if args[:2]==['ps','-p']:return subprocess.CompletedProcess(args,0,self.line+'\n','')
        if args==['ps','-axo','pid=,args=']:return subprocess.CompletedProcess(args,0,f'{self.pid} /unrelated/browser\n','')
        if args==['ps','-axo','pid=,ppid=,pgid=,lstart=,args=']:return subprocess.CompletedProcess(args,0,self.table,'')
        raise AssertionError(args)

    def check(self,full=False):
        with patch.object(p.os,'kill',side_effect=self.kill),patch.object(p.subprocess,'run',side_effect=self.ps),\
             patch.object(campaign_watchdog,'capture_process_identity',return_value=self.second_identity):
            if full:
                self.f.write(self.f.receipt,self.receipt)
                return p.validate_and_load(self.f.source,reconciliation=self.f.receipt)
            return p.validate_process_reconciliation(self.f.source,self.receipt)

    def test_actual_later_identity_reconciles_without_changing_parent(self):
        before={str(f):f.read_bytes() for f in self.f.source.rglob('*') if f.is_file()}
        observations=self.check()
        self.assertEqual(observations[0]['pid'],self.pid)
        self.assertEqual(observations[0]['current_process_identity'],self.fingerprint)
        restored=self.check(full=True)
        self.assertEqual(restored['problems']['problem']['main_session'],'main-session')
        self.assertEqual(before,{str(f):f.read_bytes() for f in self.f.source.rglob('*') if f.is_file()})

    def snapshot_alias(self, relative='exam/papers/problem/snapshot', record=None):
        folder=self.f.source/relative
        self.f.write(folder/'snapshot.json', {'calls':[self.stage if record is None else record]})
        self.f.write(folder/'manifest.json', {'schema_version':1,
            'files':{'snapshot.json':p._hash(folder/'snapshot.json')}})
        self.f.write(folder.parent/'snapshot-receipt.json',
            {'manifest_sha256':p._hash(folder/'manifest.json')})
        return folder

    def test_exact_bound_native_snapshot_aliases_are_not_new_owners(self):
        for root in ('exam','history/prior-exam'):
            self.snapshot_alias(root+'/papers/problem/snapshot')
        self.assertEqual(self.check()[0]['pid'],self.pid)

    def test_snapshot_alias_changed_fields_and_extra_ownership_fail_closed(self):
        for change in ({'status':'running'}, {'session_id':'different'}, {'probe_pid':self.pid}):
            self.snapshot_alias(record={**self.stage,**change})
            with self.subTest(change=change),self.assertRaisesRegex(ValueError,'non-stage ownership'):
                self.check()

    def test_snapshot_alias_wrong_path_or_problem_is_not_a_native_copy(self):
        for relative in ('unrecognized/snapshot', 'exam/papers/other/snapshot', 'history/superseded-exam/papers/problem/snapshot'):
            folder=self.snapshot_alias(relative)
            with self.subTest(relative=relative),self.assertRaisesRegex(ValueError,'non-stage ownership'):
                self.check()
            import shutil
            shutil.rmtree(folder.parent)

    def test_snapshot_alias_requires_unchanged_manifest_and_receipt(self):
        folder=self.snapshot_alias()
        self.f.write(folder/'snapshot.json',{'calls':[self.stage],'extra':'changed'})
        with self.assertRaisesRegex(ValueError,'snapshot evidence changed'):self.check()
        self.snapshot_alias()
        self.f.write(folder.parent/'snapshot-receipt.json',{'manifest_sha256':'0'*64})
        with self.assertRaisesRegex(ValueError,'bound manifest'):self.check()

    def test_no_receipt_or_same_identity_or_changed_again_never_bypasses(self):
        original=copy.deepcopy(self.receipt)
        for change in ('missing','same','changed','unknown'):
            self.receipt=copy.deepcopy(original);self.second_identity=self.fingerprint
            if change=='missing':self.receipt.pop('reused_pids')
            if change=='same':
                self.stage['process_identity']=self.fingerprint;self.f.write(self.path,self.stage)
                self.receipt['reused_pids'][0]['stage_receipts'][0]['sha256']=p._hash(self.path)
            if change=='changed':self.second_identity='b'*64
            if change=='unknown':self.second_identity=None
            with self.subTest(change=change),self.assertRaises(ValueError):self.check()
            self.stage['process_identity']='a'*64;self.f.write(self.path,self.stage)

    def test_missing_historical_identity_nonterminal_and_stale_hash_reject(self):
        original=copy.deepcopy(self.stage)
        for change in ('identity','running','hash','timestamps','exit_code'):
            self.stage=copy.deepcopy(original)
            if change=='identity':self.stage.pop('process_identity')
            if change=='exit_code':self.stage.pop('exit_code')
            if change=='running':self.stage['status']='running'
            if change=='timestamps':self.stage['end_utc']='2026-01-03T00:00:00Z'
            self.f.write(self.path,self.stage)
            self.receipt['reused_pids'][0]['stage_receipts'][0]['sha256']=p._hash(self.path) if change!='hash' else '0'*64
            with self.subTest(change=change),self.assertRaises(ValueError):self.check()

    def test_all_historical_incarnations_must_be_bound_and_terminal(self):
        extra=self.path.parent.parent/'005-proof-review/stage.meta.json'
        self.f.write(extra,{**self.stage,'name':'problem/005-proof-review','status':'running'})
        with self.assertRaisesRegex(ValueError,'every historical'):self.check()
        self.receipt['reused_pids'][0]['stage_receipts'].append({'path':str(extra.relative_to(self.f.source)),'sha256':p._hash(extra)})
        with self.assertRaisesRegex(ValueError,'not terminal'):self.check()

    def test_command_change_without_later_birth_and_unavailable_birth_reject(self):
        for line in ('Thu Jan  1 00:00:00 2026 /changed-command','birth-unknown /browser'):
            self.line=line;self.fingerprint=hashlib.sha256(line.encode()).hexdigest()
            self.receipt['reused_pids'][0]['current_process_identity']=self.fingerprint
            with self.subTest(line=line),self.assertRaises(ValueError):self.check()

    def test_owned_lineage_group_and_parentpath_remain_blocking(self):
        for table in (f'{self.pid} 900001 {self.pid} {self.line}\n',
                      f'{self.pid} 1 900001 {self.line}\n',
                      f'{self.pid} 1 {self.pid} Thu Jan  1 00:00:00 2026 /old-member\n',
                      f'{self.pid} 1 {self.pid} {self.line} {self.f.source}\n'):
            self.table=table
            with self.subTest(table=table),self.assertRaises(ValueError):self.check()

    def test_missing_current_identity_wrong_receipt_and_permission_fail_closed(self):
        self.receipt['reused_pids'][0]['current_process_identity']=None
        with self.assertRaises(ValueError):self.check()
        self.receipt['reused_pids'][0]['current_process_identity']='b'*64
        with self.assertRaises(ValueError):self.check()
        self.receipt['reused_pids'][0]['current_process_identity']=self.fingerprint
        self.kill_error=PermissionError()
        self.assertEqual(self.check()[0]['pid'], self.pid)
        self.second_identity=None
        with self.assertRaisesRegex(ValueError,'cannot establish'):self.check()

    def test_unterminated_probe_incarnation_with_same_number_is_not_stage_copy(self):
        self.f.write(self.f.folder/'probes/later/launch.json', {'pid': self.pid, 'status': 'running'})
        with self.assertRaisesRegex(ValueError, 'non-stage ownership'):
            self.check()

    def test_nested_probe_inside_stage_meta_is_not_the_stage_incarnation(self):
        self.stage['probe_launch']={'probe_pid':self.pid,'status':'running'}
        self.f.write(self.path,self.stage)
        self.receipt['reused_pids'][0]['stage_receipts'][0]['sha256']=p._hash(self.path)
        with self.assertRaisesRegex(ValueError, 'non-stage ownership'):
            self.check()

    def test_absent_leader_does_not_hide_surviving_process_group(self):
        self.kill_error=ProcessLookupError()
        self.table=f'900100 1 {self.pid} {self.line}\n'
        with self.assertRaisesRegex(ValueError, 'process group'):
            self.check()

    def test_process_exit_is_allowed_but_missing_ps_with_live_pid_is_not(self):
        self.kill_error=ProcessLookupError()
        self.table=''
        self.assertEqual(self.check(),[])
        self.kill_error=None;self.line=''
        with self.assertRaises(ValueError):self.check()

if __name__=='__main__':unittest.main()
