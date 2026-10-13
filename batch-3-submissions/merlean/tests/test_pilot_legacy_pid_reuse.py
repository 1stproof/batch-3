"""Legacy receipts corroborate absence; never invent a missing identity."""
import copy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import test_pilot_pid_reuse as strict
import pilot_continuation as p


class LegacyPidReuseTests(strict.PidReuseTests):
    def setUp(self):
        super().setUp()
        self.f.source=self.f.source.resolve()
        self.f.folder=self.f.folder.resolve()
        self.path=self.path.resolve()
        self.receipt['source_root']=str(self.f.source)
        self.stage.pop('process_identity')
        self.stage.update(command=['/original/codex', 'resume', 'historical-session'],
                          session_id='historical-session', resume_session='historical-session')
        self.write_stage()
        self.external = self.f.source.parent / 'absence'
        self.external.mkdir()
        self.census_time = '2026-01-01T12:00:00Z'
        self.raw = self.external / 'ps.txt'
        self.raw.write_text('1 0 1 Thu Jan  1 00:00:00 2026 /sbin/launchd\n')
        self.census = {'checked_utc':self.census_time, 'blockers':[], 'owned_pid_count':len(self.receipt['owned_pids']),
                       'host_absent':True, 'process_count':1, 'recorded_present_pids':[], 'census_file':self.ref(self.raw)}
        self.prior = {k:copy.deepcopy(v) for k,v in self.receipt.items() if k!='reused_pids'}
        self.prior.update(all_owned_children_stopped=True, owned_process_groups_checked=True, document_mcp_segment_path_census_checked=True, active_children=[], pending_launches=[])
        self.seal = {'source_root':str(self.f.source), 'files':[dict(self.receipt['reused_pids'][0]['stage_receipts'][0])]}
        self.terminal = {'source_root':str(self.f.source), 'status':'PASS', 'campaign_sealed':True,'host_absent_both_censuses':True,'live_owned_processes':[]}
        self.save_evidence()

    def ps(self,args,**kwargs):
        if args[-1]=='comm=':
            import subprocess
            return subprocess.CompletedProcess(args,0,self.line.split(None,5)[-1].split()[0]+'\n','')
        return super().ps(args,**kwargs)

    def ref(self,path):
        return {'path':str(path), 'sha256':p._hash(path)}

    def write_stage(self):
        self.f.write(self.path,self.stage)
        progress=json.loads((self.f.folder/'host-progress.json').read_text())
        progress['calls'][2]=copy.deepcopy(self.stage)
        self.f.write(self.f.folder/'host-progress.json',progress)
        self.receipt['reused_pids'][0]['stage_receipts'][0]['sha256']=p._hash(self.path)

    def save_evidence(self):
        refs={}
        for key,value in [('census',self.census),('reconciliation',self.prior),('sealed_files',self.seal)]:
            path=self.external/(key+'.json');self.f.write(path,value);refs[key]=self.ref(path)
        self.terminal.update(reconciliation=refs['reconciliation'],sealed_files=refs['sealed_files'])
        path=self.external/'terminal.json';self.f.write(path,self.terminal);refs['terminal']=self.ref(path)
        refs['raw_census']=self.ref(self.raw)
        self.witness={'schema_version':1,'source_root':str(self.f.source),'checked_utc':self.census_time,
            'owned_pids':self.prior['owned_pids'],'recorded_present_pids':[], 'blockers':[],
            'complete_process_census':True,**refs}
        self.write_witness()

    def write_witness(self):
        path=self.external/'witness.json';self.f.write(path,self.witness)
        self.audit={'status':'PASS','auditor':'independent','source_root':str(self.f.source),
            'checked_utc':'2026-01-03T00:00:00Z','witness_sha256':p._hash(path),
            'artifacts':{ref['path']:ref['sha256'] for ref in [self.ref(path),*[self.witness[k] for k in ('census','raw_census','reconciliation','terminal','sealed_files')]]}}
        audit_path=self.external/'audit.json';self.f.write(audit_path,self.audit)
        self.receipt['reused_pids'][0].update(evidence_kind='legacy_terminal_receipt',
            prior_absence_receipt=self.ref(path),prior_absence_audit=self.ref(audit_path),current_executable='/unrelated/browser')

    # Inherit relevant strict-route negatives, but strict-specific positive cases
    # are separately exercised by PidReuseTests without this fixture override.
    def test_actual_later_identity_reconciles_without_changing_parent(self):
        before={str(f):f.read_bytes() for f in self.f.source.rglob('*') if f.is_file()}
        self.assertEqual(self.check()[0]['pid'],self.pid)
        self.assertEqual(before,{str(f):f.read_bytes() for f in self.f.source.rglob('*') if f.is_file()})
        self.assertNotIn('process_identity',json.loads(self.path.read_text()))

    def test_missing_historical_identity_nonterminal_and_stale_hash_reject(self):
        original=copy.deepcopy(self.stage)
        for key,value in [('process_identity','broken'),('process_identity','a'*64),('status','running'),
                          ('exit_code',None),('start_utc',None),('end_utc',None),('command',[]),
                          ('command','codex'),('session_id',None),('resume_session','wrong'),('name','')]:
            self.stage=copy.deepcopy(original);self.stage[key]=value;self.write_stage()
            self.seal['files']=[dict(self.receipt['reused_pids'][0]['stage_receipts'][0])];self.save_evidence()
            with self.subTest(key=key,value=value),self.assertRaises(ValueError):self.check()

    def test_nested_receipt_drift_rejected(self):
        progress=json.loads((self.f.folder/'host-progress.json').read_text())
        progress['calls'][2]['command']=['/different/codex']
        self.f.write(self.f.folder/'host-progress.json',progress)
        with self.assertRaisesRegex(ValueError,'non-stage'):self.check()

    def test_original_executable_and_ownership_markers_rejected(self):
        for command in ['/original/codex','/other/bin historical-session','/other/bin pilot_document_tools','/other/bin mcp']:
            self.line='Fri Jan  2 12:00:00 2026 '+command
            self.receipt['reused_pids'][0]['current_process_identity']=hashlib.sha256(self.line.encode()).hexdigest()
            self.receipt['reused_pids'][0]['current_executable']=command.split()[0]
            with self.subTest(command=command),self.assertRaisesRegex(ValueError,'ownership'):self.check()

    def test_bound_absence_receipt_and_audit_required(self):
        entry=self.receipt['reused_pids'][0]
        for key in ('prior_absence_receipt','prior_absence_audit'):
            original=entry.pop(key)
            with self.subTest(key=key),self.assertRaises(ValueError):self.check()
            entry[key]=original
        path=self.external/'audit.json';self.audit['artifacts']={};self.f.write(path,self.audit)
        entry['prior_absence_audit']=self.ref(path)
        with self.assertRaisesRegex(ValueError,'independently'):self.check()

    def test_absence_raw_and_summary_coverage_required(self):
        self.raw.write_text(f'{self.pid} 1 {self.pid} Thu Jan  1 00:00:00 2026 /original/codex\n')
        self.census['census_file']=self.ref(self.raw);self.save_evidence()
        with self.assertRaisesRegex(ValueError,'absence'):self.check()

    def test_absence_temporal_order_and_missing_seal_reject(self):
        for value in ['2026-01-01T00:01:00Z','2026-01-03T00:00:00Z']:
            self.census_time=value;self.census['checked_utc']=value;self.save_evidence()
            with self.subTest(value=value),self.assertRaisesRegex(ValueError,'intervene'):self.check()
        self.census_time='2026-01-01T12:00:00Z';self.census['checked_utc']=self.census_time
        self.seal['files']=[];self.save_evidence()
        with self.assertRaisesRegex(ValueError,'prior seal'):self.check()

    def test_bound_path_symlink_hash_and_escape_reject(self):
        entry=self.receipt['reused_pids'][0]
        original=copy.deepcopy(entry)
        entry['stage_receipts'][0]['path']='../outside.json'
        with self.assertRaises(ValueError):self.check()
        self.receipt['reused_pids'][0]=copy.deepcopy(original)
        entry=self.receipt['reused_pids'][0];entry['prior_absence_receipt']['sha256']='0'*64
        with self.assertRaises(ValueError):self.check()
        link=self.external/'link.json';link.symlink_to(self.external/'witness.json')
        entry['prior_absence_receipt']=self.ref(link)
        with self.assertRaises(ValueError):self.check()

    def test_prior_incomplete_flags_and_ownership_reject(self):
        original=copy.deepcopy(self.prior)
        for key,value in [('descendants_checked',False),('all_owned_children_stopped',False),
                          ('owned_process_groups_checked',False),('document_mcp_segment_path_census_checked',False),
                          ('pending_launches',[1]),('active_children',[1]),('owned_pids',[]),('source_root','/wrong')]:
            self.prior=copy.deepcopy(original);self.prior[key]=value;self.save_evidence()
            with self.subTest(key=key),self.assertRaises(ValueError):self.check()

    def test_current_executable_must_be_independently_measured(self):
        self.receipt['reused_pids'][0]['current_executable']='/forged/browser'
        with self.assertRaisesRegex(ValueError,'executable'):self.check()

    def test_recorded_groups_and_session_descendants_reject(self):
        self.prior['recorded_group_ids']=[812345];self.save_evidence()
        self.table+=f'812346 1 812345 {self.line}\n'
        with self.assertRaisesRegex(ValueError,'recorded process group'):self.check()
        self.prior['recorded_group_ids']=[];self.save_evidence()
        self.table=f'{self.pid} 1 {self.pid} {self.line}\n812346 1 812346 Fri Jan  2 12:00:00 2026 /worker historical-session\n'
        with self.assertRaisesRegex(ValueError,'references parent'):self.check()

    def test_raw_census_incomplete_and_false_summary_reject(self):
        original=self.raw.read_text()
        for raw in ['', 'bad row\n', original+original]:
            self.raw.write_text(raw);self.census['census_file']=self.ref(self.raw);self.save_evidence()
            with self.subTest(raw=raw),self.assertRaises(ValueError):self.check()
        self.raw.write_text(original);self.census['census_file']=self.ref(self.raw)
        self.census['recorded_present_pids']=[self.pid];self.save_evidence()
        with self.assertRaises(ValueError):self.check()

    def test_current_birth_after_observation_and_wrong_weekday_reject(self):
        for line in ['Sun Jan  4 12:00:00 2026 /unrelated/browser','Thu Jan  2 12:00:00 2026 /unrelated/browser']:
            self.line=line;self.receipt['reused_pids'][0]['current_process_identity']=hashlib.sha256(line.encode()).hexdigest()
            with self.subTest(line=line),self.assertRaises(ValueError):self.check()

    def test_ambiguous_time_rejected(self):
        with patch.object(p.time,'mktime',side_effect=[1,2]),patch.object(p.time,'localtime',return_value=(2026,1,2,12,0,0,4,2,0)):
            with self.assertRaisesRegex(ValueError,'ambiguous'):p._unambiguous_birth('Fri Jan 2 12:00:00 2026')

if __name__=='__main__':unittest.main()
