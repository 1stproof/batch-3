"""Continuation reconstruction uses synthetic immutable parent evidence."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_continuation as continuation


class ContinuationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.source = self.base / 'parent'
        self.folder = self.source / 'campaign/problems/problem'
        self.folder.mkdir(parents=True)
        self.write(self.source / 'host-config.json', dict(problems=['problem'], deadline_utc='2026-01-01T00:45:00Z', mode='lite', policy_hashes={}))
        self.write(self.source / 'pilot-result.json', dict(end_utc='2026-01-01T00:45:01Z', results=[dict(problem='problem', status='partial')]))
        original = b'Exact original question\n'
        (self.folder / 'input.txt').write_bytes(original)
        self.write(self.source / 'campaign/registry.json', dict(deadline_utc='2026-01-01T00:45:00Z', mode='lite', problems={'problem':dict(sha256=hashlib.sha256(original).hexdigest())}))
        self.write(self.source / 'campaign/state.json', dict(sealed=True, problems={'problem':{'status':'partial'}}, registry_sha256=hashlib.sha256((self.source/'campaign/registry.json').read_bytes()).hexdigest()))
        self.calls = []
        for number, role, sid, status in ((1,'main-dossier','main-session','completed'), (2,'sol-execution','worker-session','completed'), (3,'proof-review','reviewer-session','completed'), (4,'main-repair','main-session','timeout_censored')):
            name = 'problem/' + str(number).zfill(3) + '-' + role
            call = dict(name=name, request_id='request-'+str(number), module=role, session_id=sid, pid=900000+number, status=status)
            self.calls.append(call)
            self.write(self.source / 'host/runtime' / name / 'stage.meta.json', call)
            self.write(self.folder / (name.split('/')[-1]+'.json'), {'proof_markdown':'latest valid candidate', 'ledger':{'rows':[]}} if number == 1 else {'status':status})
            if status == 'completed':
                answer = (self.folder / (name.split('/')[-1]+'.json')).read_bytes()
                stage = self.source / 'host/runtime' / name
                (stage/'stage.answer.txt').write_bytes(answer)
                call['answer_sha256'] = hashlib.sha256(answer).hexdigest()
                self.write(stage/'stage.meta.json', call)
        self.write(self.folder / 'host-progress.json', dict(main_session='main-session', calls=self.calls, open_findings=[{'id':'open-finding'}], errors=[{'error':'deadline'}]))
        self.write(self.folder / 'current-candidate.json', {'proof_markdown':'latest valid candidate', 'ledger':{'rows':[]}})
        self.write(self.folder / 'probes/main-3-lean/result.json', {'status':'failed','stderr':'actual failed compiler diagnostic'})
        (self.folder / 'probes/main-3-lean/source.lean').write_text('theorem example : True := by trivial\n')
        self.receipt = self.base / 'reconciliation.json'
        self.write(self.receipt, dict(schema_version=1, source_root=str(self.source), checked_utc='2026-01-01T00:46:00Z', host_pid=900000, owned_pids=[900000,900001,900002,900003,900004], descendants_checked=True, launch_records_checked=True, probe_records_checked=True, evidence=[str(self.source/'pilot-result.json')]))

    @staticmethod
    def write(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def load(self):
        with patch.object(continuation.os, 'kill', side_effect=ProcessLookupError), patch.object(continuation.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '', '')):
            return continuation.validate_and_load(self.source, reconciliation=self.receipt)

    def local_registry(self):
        import pilot_local_verification as local
        task={'kind':'lean','row_ids':['r'],'owned_scope':'local file',
              'local_module':{'brief':'Synthetic unchanged claim','max_worker_calls':2,'max_probe_runs':2}}
        candidate={'ledger':{'rows':[{'id':'r','statement':'synthetic claim','uses':[]}]}}
        approval={'receipt':{'name':'independent-review'},
                  'local_module_links':{local.digest(task):{'prior_module_id':None,'relation':'new_claim'}}}
        modules=[]
        module,error=local.admit(modules,candidate,task,'a'*64,approval)
        self.assertIsNone(error)
        module['state']='returned_to_main';module['worker_calls']=1
        module['returns']=[{'output':{'lean_probe':'retained uncompiled source'},'receipt':{'name':'synthetic-stage'}}]
        return modules

    def save_registry(self, modules):
        self.write(self.folder/'local-verification-modules.json',modules)
        progress=json.loads((self.folder/'host-progress.json').read_text())
        progress['local_verification_modules']=modules
        self.write(self.folder/'host-progress.json',progress)
        if isinstance(modules,list):
            for module in modules:
                if isinstance(module,dict) and isinstance(module.get('artifact_root'),str) and '..' not in module['artifact_root']:
                    self.write(self.folder/module['artifact_root']/'module.json',module)

    def test_list_module_registry_restores_exact_terminal_history(self):
        modules=self.local_registry();self.save_registry(modules)
        before=(self.folder/'local-verification-modules.json').read_bytes()
        restored=self.load()['problems']['problem']['local_verification_modules']
        self.assertEqual(restored,modules)
        self.assertEqual((self.folder/'local-verification-modules.json').read_bytes(),before)
        self.assertEqual(restored[0]['state'],'returned_to_main')
        self.assertEqual((restored[0]['worker_calls'],restored[0]['probe_runs']),(1,0))

    def test_module_registry_rejects_wrong_root_and_nonobject_entries(self):
        for value in ({},None,'registry',[1],[[]],[None]):
            with self.subTest(value=value):
                self.save_registry(value)
                with self.assertRaisesRegex(ValueError,'JSON array of objects'):self.load()
        self.save_registry([])
        self.assertEqual(self.load()['problems']['problem']['local_verification_modules'],[])

    def test_module_registry_checkpoint_and_artifact_must_match(self):
        modules=self.local_registry();self.save_registry(modules)
        progress=json.loads((self.folder/'host-progress.json').read_text())
        progress['local_verification_modules'][0]['probe_runs']=1
        self.write(self.folder/'host-progress.json',progress)
        with self.assertRaisesRegex(ValueError,'differs from terminal checkpoint'):self.load()
        self.save_registry(modules)
        self.write(self.folder/modules[0]['artifact_root']/'module.json',{})
        with self.assertRaisesRegex(ValueError,'artifact differs'):self.load()
        self.save_registry(modules)
        (self.folder/'local-verification-modules.json').unlink()
        with self.assertRaisesRegex(ValueError,'differs from terminal checkpoint'):self.load()

    def test_module_registry_rejects_malformed_identity_budget_lineage_and_scope(self):
        import copy
        original=self.local_registry()
        changes=[('module_id','other'),('generation',True),('parent_module_id','absent'),
                 ('inherited_counters_from','absent'),('worker_calls',True),('probe_runs',-1),
                 ('state','certified'),('claim_sha256','not-hash'),('artifact_root','../escape'),
                 ('limits',{'max_worker_calls':0,'max_probe_runs':1}),('approval_receipt',[]),
                 ('returns',['not-object']),('counter_semantics','reset')]
        for key,value in changes:
            with self.subTest(key=key):
                modules=copy.deepcopy(original);modules[0][key]=value;self.save_registry(modules)
                with self.assertRaises(ValueError):self.load()
        self.save_registry(original+copy.deepcopy(original))
        with self.assertRaisesRegex(ValueError,'duplicate'):self.load()

    def test_object_reader_stays_object_only(self):
        path=self.base/'control.json';self.write(path,[])
        with self.assertRaisesRegex(ValueError,'expected JSON object'):continuation._json(path)

    def test_typed_dossier_correction_and_malformed_scope_preserve_exact_history(self):
        candidate = {'proof_markdown': 'Full corrected dossier', 'ledger': {'rows': []}}
        for index, value in ((0, ['malformed main']), (2, ['malformed scope']),
                             (3, dict(candidate, response_type='candidate_update'))):
            call = self.calls[index]
            call['status'] = 'completed'
            if index == 2:
                call['module'] = 'scope-review'
            raw = json.dumps(value).encode()
            call['answer_sha256'] = hashlib.sha256(raw).hexdigest()
            stage = self.source / 'host/runtime' / call['name']
            (stage / 'stage.answer.txt').write_bytes(raw)
            self.write(stage / 'stage.meta.json', call)
            self.write(self.folder / (call['name'].split('/')[-1] + '.json'), value)
        config = json.loads((self.source / 'host-config.json').read_text())
        config.update(main_response_contract_version=1, legacy_main_stages=[])
        self.write(self.source / 'host-config.json', config)
        self.write(self.folder / 'current-candidate.json', candidate)
        self.write(self.folder / 'accepted-dossier.json', {'source_stage': self.calls[3]['name'],
            'raw_response_sha256': self.calls[3]['answer_sha256'], 'effective_candidate': candidate})
        restored = self.load()['problems']['problem']
        self.assertEqual(restored['current'], candidate)
        self.assertEqual(restored['dossier'], candidate)
        self.assertEqual(restored['reviewer_history'][0]['output'], ['malformed scope'])
        self.assertEqual(json.loads((self.folder / '001-main-dossier.json').read_text()), ['malformed main'])

    def test_main_and_scope_null_or_plaintext_transport_wrappers_survive(self):
        from codex_transport import extract_answer
        for module, index in [('main-repair', 3), ('scope-review', 2)]:
            for raw in ('null', 'not JSON at all'):
                with self.subTest(module=module, raw=raw):
                    call = self.calls[index]
                    call.update(module=module, status='completed')
                    parsed, _, error = extract_answer(raw)
                    value = parsed if parsed is not None else {'raw_answer': raw, 'parse_error': error}
                    call['answer_sha256'] = hashlib.sha256(raw.encode()).hexdigest()
                    stage = self.source / 'host/runtime' / call['name']
                    (stage / 'stage.answer.txt').write_text(raw)
                    self.write(stage / 'stage.meta.json', call)
                    self.write(self.folder / (call['name'].split('/')[-1] + '.json'), value)
                    restored = self.load()['problems']['problem']
                    self.assertEqual(restored['current']['proof_markdown'], 'latest valid candidate')
                    self.assertEqual(json.loads((self.folder / (call['name'].split('/')[-1] + '.json')).read_text()), value)

    def test_nonobject_invalid_proof_review_is_preserved_without_authority(self):
        call = self.calls[2]
        value = ['invalid review', {'unresolved': 'retain exactly'}]
        answer = json.dumps(value).encode()
        stage = self.source / 'host/runtime' / call['name']
        (stage / 'stage.answer.txt').write_bytes(answer)
        call['answer_sha256'] = hashlib.sha256(answer).hexdigest()
        self.write(stage / 'stage.meta.json', call)
        self.write(self.folder / '003-proof-review.json', value)
        restored = self.load()['problems']['problem']
        self.assertEqual(restored['reviewer_history'][0]['output'], value)
        self.assertEqual(restored['triage_history'], [])
        self.assertEqual(restored['findings'], [{'id': 'open-finding'}])

    def test_invalid_scalar_null_and_text_reviews_roundtrip_transport_value(self):
        from codex_transport import extract_answer
        for raw in ('"invalid review"', 'null', 'not valid JSON', '42', 'false'):
            with self.subTest(raw=raw):
                call = self.calls[2]
                parsed, _, error = extract_answer(raw)
                saved = parsed if parsed is not None else {'raw_answer': raw, 'parse_error': error}
                stage = self.source / 'host/runtime' / call['name']
                (stage / 'stage.answer.txt').write_text(raw)
                call['answer_sha256'] = hashlib.sha256(raw.encode()).hexdigest()
                self.write(stage / 'stage.meta.json', call)
                self.write(self.folder / '003-proof-review.json', saved)
                restored = self.load()['problems']['problem']
                self.assertEqual(restored['reviewer_history'][0]['output'], saved)
                self.assertEqual(restored['triage_history'], [])
                self.assertEqual(restored['findings'], [{'id': 'open-finding'}])

    def test_preserves_state_and_diagnostics_without_mutating_parent(self):
        before = {str(p):p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        restored = self.load()
        state = restored['problems']['problem']
        self.assertEqual(state['main_session'], 'main-session')
        self.assertEqual(state['counter'], 4)
        self.assertEqual(state['current']['proof_markdown'], 'latest valid candidate')
        self.assertEqual(state['findings'], [{'id':'open-finding'}])
        self.assertEqual(state['implementers'], ['main-session','worker-session'])
        self.assertEqual(state['reviewer_history'][0]['session_id'], 'reviewer-session')
        self.assertEqual(state['execution_history'][1]['result']['stderr'], 'actual failed compiler diagnostic')
        self.assertEqual(restored['parent']['prior_deadline_utc'], '2026-01-01T00:45:00Z')
        self.assertEqual(before, {str(p):p.read_bytes() for p in self.source.rglob('*') if p.is_file()})
        self.assertEqual(restored['parent']['manifest_sha256'], self.load()['parent']['manifest_sha256'])

    def test_sealed_registry_and_candidate_binding_enforced(self):
        registry_path = self.source/'campaign/registry.json'
        registry = json.loads(registry_path.read_text())
        registry['mode'] = 'heavy'
        self.write(registry_path, registry)
        with self.assertRaisesRegex(ValueError, 'sealed against its registry'):
            self.load()
        registry['mode'] = 'lite'
        self.write(registry_path, registry)
        self.write(self.folder/'current-candidate.json', {'proof_markdown':'fabricated candidate', 'ledger':{'rows':[]}})
        with self.assertRaisesRegex(ValueError, 'latest valid completed main'):
            self.load()

    def test_completed_response_hash_binding(self):
        path = self.source/'host/runtime/problem/001-main-dossier/stage.meta.json'
        answer = (self.folder/'001-main-dossier.json').read_bytes()
        path.with_name('stage.answer.txt').write_bytes(answer)
        meta = json.loads(path.read_text())
        meta['answer_sha256'] = hashlib.sha256(answer).hexdigest()
        self.write(path, meta)
        self.load()
        path.with_name('stage.answer.txt').write_bytes(b'changed answer')
        with self.assertRaisesRegex(ValueError, 'answer hash mismatch'):
            self.load()

    def test_legacy_independent_triage_survives_without_main_flags(self):
        stage = self.source / 'host/runtime/problem/003-proof-review'
        answer = {'triaged_rows': ['S1'], 'triage_rationale': 'Check the fragile inference.'}
        self.write(self.folder / '003-proof-review.json', answer)
        raw = json.dumps(answer).encode()
        (stage / 'stage.answer.txt').write_bytes(raw)
        meta = json.loads((stage / 'stage.meta.json').read_text())
        meta['answer_sha256'] = hashlib.sha256(raw).hexdigest()
        self.write(stage / 'stage.meta.json', meta)
        restored = self.load()['problems']['problem']
        history = restored['triage_history']
        self.assertEqual(history[-1]['selected_rows'], ['S1'])
        self.assertEqual(history[-1]['decisions'][0]['row_id'], 'S1')
        self.assertFalse(history[-1]['authorization'])
        self.assertNotIn('candidate_binding', history[-1])
        self.assertEqual(history[-1]['sources'][0]['answer_sha256'], meta['answer_sha256'])

    def rejected_review(self):
        from pilot_candidate_contract import candidate_hash
        call = self.calls[2]
        value = {'verdict': 'PASS_COMPLETE_PROOF', 'triaged_rows': ['S1'], 'approved': True}
        raw = json.dumps(value).encode()
        call.update(answer_sha256=hashlib.sha256(raw).hexdigest(), prompt_sha256='a' * 64)
        stage = self.source / 'host/runtime' / call['name']
        (stage / 'stage.answer.txt').write_bytes(raw)
        self.write(stage / 'stage.meta.json', call)
        self.write(self.folder / '003-proof-review.json', value)
        candidate = json.loads((self.folder / 'current-candidate.json').read_text())
        binding = candidate_hash(candidate)
        diagnostic = {'status': 'invalid_not_authority', 'error': 'research gap cannot pass proof review',
                      'candidate_sha256': binding, 'invalid_review': value,
                      'receipt': dict(call, reviewed_candidate_sha256=binding)}
        path = self.folder / 'review-003-invalid-1.json'
        self.write(path, diagnostic)
        return path, diagnostic

    def test_rejected_review_preserves_exact_receipt_and_cannot_supply_legacy_triage(self):
        path, diagnostic = self.rejected_review()
        before = {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        restored = self.load()['problems']['problem']
        review = restored['reviewer_history'][0]
        self.assertEqual(review['protocol_status'], 'invalid_not_authority')
        self.assertEqual(review['output'], diagnostic['invalid_review'])
        self.assertEqual(review['invalid_protocol_diagnostics'], [{
            'path': str(path.relative_to(self.source)),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'diagnostic': diagnostic}])
        self.assertEqual(restored['triage_history'], [])
        self.assertEqual(restored['findings'], [{'id': 'open-finding'}])
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})

    def test_absent_rejection_receipt_never_marks_transport_accepted(self):
        path, _ = self.rejected_review()
        path.unlink()
        review = self.load()['problems']['problem']['reviewer_history'][0]
        self.assertEqual(review['protocol_status'], 'not_revalidated')
        self.assertNotIn('invalid_protocol_diagnostics', review)

    def test_rejection_binding_tampering_fails_closed(self):
        import copy
        path, original = self.rejected_review()
        for field in ('name', 'session_id', 'answer_sha256', 'prompt_sha256', 'request_id',
                      'reviewed_candidate_sha256'):
            with self.subTest(receipt=field):
                value = copy.deepcopy(original)
                value['receipt'][field] = 'stale'
                self.write(path, value)
                with self.assertRaisesRegex(ValueError, 'historical review diagnostic binding'):
                    self.load()
        for change in ('status', 'error', 'candidate', 'unknown_candidate', 'raw', 'typed_raw', 'receipt', 'scalar'):
            with self.subTest(change=change):
                value = copy.deepcopy(original)
                if change == 'status': value['status'] = 'accepted'
                if change == 'error': value['error'] = ' '
                if change == 'candidate': value['candidate_sha256'] = 'b' * 64
                if change == 'unknown_candidate':
                    value['candidate_sha256'] = value['receipt']['reviewed_candidate_sha256'] = 'b' * 64
                if change == 'raw': value['invalid_review']['verdict'] = 'INCOMPLETE'
                if change == 'typed_raw': value['invalid_review']['approved'] = 1
                if change == 'receipt': value['receipt'] = []
                if change == 'scalar': value = []
                self.write(path, value)
                with self.assertRaisesRegex(ValueError, 'historical review diagnostic binding'):
                    self.load()

    def test_missing_identity_on_both_receipts_does_not_bind(self):
        path, value = self.rejected_review()
        del value['receipt']['prompt_sha256']
        self.write(path, value)
        call = dict(self.calls[2]); del call['prompt_sha256']
        self.write(self.source / 'host/runtime' / call['name'] / 'stage.meta.json', call)
        with self.assertRaisesRegex(ValueError, 'historical review diagnostic binding'):
            self.load()

    def test_stage_order_remains_numeric_after_999(self):
        for number in (999, 1000):
            name = 'problem/' + str(number) + '-main-repair'
            answer = {'proof_markdown': 'candidate ' + str(number), 'ledger': {'rows': []}}
            encoded = json.dumps(answer).encode()
            self.write(self.folder / (name.split('/')[-1] + '.json'), answer)
            call = dict(name=name, module='main-repair', session_id='main-session', status='completed',
                        answer_sha256=hashlib.sha256(encoded).hexdigest())
            stage = self.source / 'host/runtime' / name
            self.write(stage / 'stage.meta.json', call)
            (stage / 'stage.answer.txt').write_bytes(encoded)
        self.write(self.folder / 'current-candidate.json', answer)
        state = self.load()['problems']['problem']
        self.assertEqual(state['counter'], 1000)
        self.assertEqual(state['calls'][-1]['name'], 'problem/1000-main-repair')
        self.assertEqual(state['current']['proof_markdown'], 'candidate 1000')

    def review_chunk_fixture(self, *, whole=False, pid=900004):
        self.base = self.base.resolve()
        self.source = self.source.resolve()
        self.folder = self.folder.resolve()
        text = json.dumps({'text': 'Exact Unicode α evidence ' * 20, 'pid': pid})
        root = self.folder / 'review-evidence'; root.mkdir(exist_ok=True)
        def artifact(raw, media):
            digest = hashlib.sha256(raw.encode()).hexdigest()
            path = root / (digest + '.json'); path.write_text(raw)
            return {'path': str(path), 'sha256': digest, 'media_type': media}
        parent = artifact(text, 'application/json')
        end = len(text) if whole else len(text) // 2
        chunk = artifact(text[:end], 'text/plain')
        chunk_id = 'history::chunk:0:' + str(end)
        stage = self.source / 'host/runtime' / self.calls[2]['name']
        cap = stage / 'document-capability.json'
        scope = {'schema_version': 1, 'mode': 'review', 'problem_id': 'problem',
                 'original_sha256': 'a'*64, 'main_session': 'main-session',
                 'store_root': str(self.folder), 'receipt_path': str(stage/'document-operations.jsonl'),
                 'producer': {'stage': self.calls[2]['name'], 'request_id': self.calls[2]['request_id'], 'session_id': None},
                 'readonly_artifacts': {'history': parent, chunk_id: chunk},
                 'required_artifact_ids': ['history'], 'inline_artifact_ids': []}
        self.write(cap, scope)
        return cap, scope, Path(parent['path']), Path(chunk['path']), chunk_id

    def historical_text_fixture(self):
        from pilot_review_history_delivery import register
        from pilot_public_sources import verify_public_source
        cap, scope, _, _, _ = self.review_chunk_fixture()
        url = 'https://example.org/public-source'
        sid = hashlib.sha256(url.encode()).hexdigest()
        store = self.folder/'public-sources'; folder = store/sid; folder.mkdir(parents=True)
        body = b'not JSON; exact public text'
        (folder/'raw').write_bytes(body); (folder/'text.txt').write_bytes(body)
        member = {'member':'text.txt','sha256':hashlib.sha256(body).hexdigest()}
        self.write(folder/'receipt.json', {'source_id':sid,'requested_url':url,'status':'downloaded',
                   'raw_sha256':member['sha256'],'members':[member],'content_files':[]})
        checked = verify_public_source(store,sid)
        bundle = {'reports':[],'public_sources':[{'source_id':sid,'receipt_sha256':checked['receipt_sha256'],'members':[member]}]}
        scope['readonly_artifacts'] = register(bundle,self.folder/'historical-review-artifacts',store)
        scope['required_artifact_ids'] = ['historical-review-index']
        self.write(cap,scope)
        meta = json.loads(cap.with_name('stage.meta.json').read_text())
        meta['document_capability'] = {'sha256':hashlib.sha256(cap.read_bytes()).hexdigest()}
        self.write(cap.with_name('stage.meta.json'),meta)
        ident = 'historical-source:'+sid+':text.txt'
        return cap,scope,Path(scope['readonly_artifacts'][ident]['path']),folder,ident

    def test_historical_source_text_is_authenticated_opaque_not_metadata(self):
        cap,scope,text,folder,ident = self.historical_text_fixture()
        self.assertEqual(continuation._opaque_review_chunks(self.source),{text})
        rogue=self.folder/'control.json'; rogue.write_text('not JSON')
        self.assertNotIn(rogue,continuation._opaque_review_chunks(self.source))
        with patch.object(continuation, '_opaque_public_source_files', return_value=set()):
            with self.assertRaises(json.JSONDecodeError): self.load()

    def test_historical_source_rejects_forged_capability_index_or_source(self):
        cap,scope,text,folder,ident = self.historical_text_fixture()
        originals={p:p.read_bytes() for p in [cap,cap.with_name('stage.meta.json'),folder/'text.txt',
                   Path(scope['readonly_artifacts']['historical-review-index']['path']),text]}
        for target in originals:
            with self.subTest(target=target.name):
                if target.name == 'stage.meta.json':
                    value=json.loads(originals[target]); value['request_id']='forged'; self.write(target,value)
                else:
                    target.write_bytes(originals[target]+b' ')
                with self.assertRaises((ValueError,KeyError)):continuation._opaque_review_chunks(self.source)
                target.write_bytes(originals[target])

    def test_historical_source_snapshot_and_inherited_aliases_remain_bound(self):
        import shutil
        cap,scope,text,folder,ident = self.historical_text_fixture()
        snapshot=self.source/'exam/papers/problem/snapshot'
        alias=snapshot/'evidence/historical-review-artifacts'/text.name
        alias.parent.mkdir(parents=True);alias.write_bytes(text.read_bytes())
        self.write(snapshot/'snapshot.json',{'schema_version':1})
        files={str(p.relative_to(snapshot)):hashlib.sha256(p.read_bytes()).hexdigest() for p in snapshot.rglob('*') if p.is_file()}
        self.write(snapshot/'manifest.json',{'files':files})
        self.assertEqual(continuation._opaque_review_chunks(self.source),{text,alias})
        alias.write_bytes(b'forged source')
        files[str(alias.relative_to(snapshot))]=hashlib.sha256(alias.read_bytes()).hexdigest()
        self.write(snapshot/'manifest.json',{'files':files})
        with self.assertRaisesRegex(ValueError,'authenticated original'):continuation._opaque_review_chunks(self.source)
        alias.write_bytes(text.read_bytes());files[str(alias.relative_to(snapshot))]=hashlib.sha256(alias.read_bytes()).hexdigest()
        self.write(snapshot/'manifest.json',{'files':files})
        files={str(p.relative_to(self.source)):hashlib.sha256(p.read_bytes()).hexdigest() for p in self.source.rglob('*') if p.is_file()}
        child=self.base/'historical-child';shutil.copytree(self.source,child)
        self.write(child/'continuation-parent.json',{'source_root':str(self.source),'files':files,
                   'manifest_sha256':hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
        expected={child/text.relative_to(self.source),child/alias.relative_to(self.source)}
        shutil.rmtree(self.source)
        self.assertEqual(continuation._opaque_review_chunks(child),expected)

    def test_authenticated_opaque_review_chunks_preserve_parent_hashes_and_census(self):
        cap, scope, parent, chunk, ident = self.review_chunk_fixture()
        with self.assertRaises(json.JSONDecodeError):
            json.loads(chunk.read_text())
        restored = self.load()
        files = restored['parent']['files']
        for path in (cap, parent, chunk):
            self.assertEqual(files[str(path.relative_to(self.source))], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(continuation._opaque_review_chunks(self.source), {chunk})
        # The full parent remains metadata for the conservative nested PID census.
        receipt = json.loads(self.receipt.read_text()); receipt['owned_pids'].remove(900004)
        self.write(self.receipt, receipt)
        with self.assertRaisesRegex(ValueError, 'missing from reconciliation'):
            self.load()

    def test_opaque_chunk_wrong_hash_bounds_namespace_or_stage_binding_rejected(self):
        cap, scope, parent, chunk, ident = self.review_chunk_fixture()
        original = chunk.read_bytes()
        chunk.write_bytes(original + b'changed')
        with self.assertRaisesRegex(ValueError, 'artifact changed'):
            self.load()
        chunk.write_bytes(original)
        for mutation in ('hash', 'bounds', 'stage', 'namespace'):
            altered = json.loads(json.dumps(scope))
            if mutation == 'hash': altered['readonly_artifacts'][ident]['sha256'] = '0'*64
            elif mutation == 'bounds':
                entry = altered['readonly_artifacts'].pop(ident)
                altered['readonly_artifacts']['history::chunk:0:1'] = entry
            elif mutation == 'stage': altered['producer']['request_id'] = 'unbound-request'
            else: altered['readonly_artifacts'][ident]['path'] = str(parent)
            self.write(cap, altered)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                self.load()
        self.write(cap, scope)

    def test_unbound_raw_chunks_and_corrupt_control_json_still_block(self):
        cap, scope, parent, chunk, ident = self.review_chunk_fixture()
        cap.unlink()
        with self.assertRaises(json.JSONDecodeError):
            self.load()
        self.write(cap, scope)
        for name in ('host/launch.json', 'host/runtime/problem/004-main-repair/stage.meta.json'):
            path = self.source/name
            old = path.read_bytes() if path.exists() else None
            path.parent.mkdir(parents=True, exist_ok=True); path.write_text('corrupt process metadata')
            with self.subTest(name=name), self.assertRaises(json.JSONDecodeError):
                self.load()
            if old is None: path.unlink()
            else: path.write_bytes(old)

    def snapshot_chunk_fixture(self):
        cap,scope,parent,chunk,ident=self.review_chunk_fixture()
        snapshot=self.source/'exam/papers/problem/snapshot'
        alias=snapshot/'evidence/review-evidence'/chunk.name
        alias.parent.mkdir(parents=True);alias.write_bytes(chunk.read_bytes())
        self.write(snapshot/'snapshot.json',{'schema_version':1})
        files={str(p.relative_to(snapshot)):hashlib.sha256(p.read_bytes()).hexdigest() for p in snapshot.rglob('*') if p.is_file()}
        self.write(snapshot/'manifest.json',{'files':files})
        return cap,chunk,snapshot,alias

    def test_snapshot_opaque_alias_is_exact_capability_bound_copy(self):
        cap,chunk,snapshot,alias=self.snapshot_chunk_fixture()
        self.assertEqual(continuation._opaque_review_chunks(self.source),{chunk,alias})
        self.load()

    def test_snapshot_alias_manifest_or_bytes_tampering_is_rejected(self):
        cap,chunk,snapshot,alias=self.snapshot_chunk_fixture()
        original=alias.read_bytes();alias.write_bytes(original+b'changed')
        with self.assertRaises(ValueError):continuation._opaque_review_chunks(self.source)
        manifest=json.loads((snapshot/'manifest.json').read_text())
        manifest['files'][str(alias.relative_to(snapshot))]=hashlib.sha256(alias.read_bytes()).hexdigest()
        self.write(snapshot/'manifest.json',manifest)
        with self.assertRaisesRegex(ValueError,'authenticated original'):continuation._opaque_review_chunks(self.source)

    def test_unbound_snapshot_namespace_and_control_json_remain_strict(self):
        import shutil
        cap,chunk,snapshot,alias=self.snapshot_chunk_fixture()
        rogue=self.source/'other/snapshot';shutil.copytree(snapshot,rogue)
        self.assertNotIn(rogue/'evidence/review-evidence'/chunk.name,continuation._opaque_review_chunks(self.source))
        with self.assertRaises(json.JSONDecodeError):self.load()
        shutil.rmtree(self.source/'other')
        (snapshot/'snapshot.json').write_text('malformed control JSON')
        manifest=json.loads((snapshot/'manifest.json').read_text());manifest['files']['snapshot.json']=hashlib.sha256((snapshot/'snapshot.json').read_bytes()).hexdigest();self.write(snapshot/'manifest.json',manifest)
        with self.assertRaises(json.JSONDecodeError):self.load()

    def test_missing_authenticated_original_never_exempts_snapshot_copy(self):
        cap,chunk,snapshot,alias=self.snapshot_chunk_fixture();chunk.unlink()
        with self.assertRaises((ValueError,FileNotFoundError)):continuation._opaque_review_chunks(self.source)

    def test_whole_parent_chunk_never_suppresses_json_pid_census(self):
        cap, scope, parent, chunk, ident = self.review_chunk_fixture(whole=True, pid=900077)
        self.assertEqual(parent, chunk)
        self.assertEqual(continuation._opaque_review_chunks(self.source), set())
        with self.assertRaisesRegex(ValueError, 'missing from reconciliation'):
            self.load()

    def test_inherited_chunk_copy_requires_exact_manifest_and_local_bytes(self):
        import shutil
        cap, scope, parent, chunk, ident = self.review_chunk_fixture(pid=900077)
        files = {str(p.relative_to(self.source)): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in self.source.rglob('*') if p.is_file()}
        child = self.base/'child'; shutil.copytree(self.source, child)
        self.write(child/'continuation-parent.json', {'source_root':str(self.source), 'files':files,
            'manifest_sha256':hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',', ':')).encode()).hexdigest()})
        child_chunk = child/chunk.relative_to(self.source)
        # Historical absolute paths stay unchanged; validation uses authenticated local copies.
        shutil.rmtree(self.source)
        self.assertEqual(continuation._opaque_review_chunks(child), {child_chunk})
        receipt = json.loads(self.receipt.read_text()); receipt['source_root'] = str(child)
        with patch.object(continuation.os, 'kill', side_effect=ProcessLookupError), patch.object(continuation.subprocess, 'run', return_value=subprocess.CompletedProcess([],0,'','')):
            with self.assertRaisesRegex(ValueError, 'missing from reconciliation'):
                continuation.validate_process_reconciliation(child, receipt)
        child_chunk.write_bytes(b'changed local copy')
        with self.assertRaisesRegex(ValueError, 'differs from parent manifest'):
            continuation._opaque_review_chunks(child)

    def test_inherited_online_chunk_store_rebases_only_exact_namespace(self):
        import shutil
        cap, scope, parent, chunk, ident = self.review_chunk_fixture()
        scope['public_source_store'] = str(self.folder/'public-sources')
        self.write(cap, scope)
        files = {str(p.relative_to(self.source)): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in self.source.rglob('*') if p.is_file()}
        child = self.base/'online-child'; shutil.copytree(self.source, child)
        def manifest():
            self.write(child/'continuation-parent.json', {'source_root':str(self.source), 'files':files,
                'manifest_sha256':hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',', ':')).encode()).hexdigest()})
        manifest()
        copied_cap=child/cap.relative_to(self.source)
        raw=copied_cap.read_bytes()
        shutil.rmtree(self.source)
        self.assertEqual(continuation._opaque_review_chunks(child), {child/chunk.relative_to(self.source)})
        self.assertEqual(copied_cap.read_bytes(),raw)
        # Even a manifest-bound malformed historical namespace must fail closed.
        scope['public_source_store'] = str(self.base/'unrelated-public-sources')
        self.write(copied_cap,scope)
        files[str(cap.relative_to(self.source))]=hashlib.sha256(copied_cap.read_bytes()).hexdigest()
        manifest()
        with self.assertRaisesRegex(ValueError,'historical namespace'):
            continuation._opaque_review_chunks(child)

    def test_live_owned_pid_blocks(self):
        with patch.object(continuation.os, 'kill', return_value=None):
            with self.assertRaisesRegex(ValueError, 'still exists'):
                continuation.validate_and_load(self.source, reconciliation=self.receipt)

    def test_unregistered_live_descendant_blocks(self):
        with patch.object(continuation.os, 'kill', side_effect=ProcessLookupError), patch.object(continuation.subprocess, 'run', return_value=subprocess.CompletedProcess([],0,'999999 python '+str(self.source.resolve())+'/code/offline_probe.py\n','')):
            with self.assertRaisesRegex(ValueError, 'still references'):
                continuation.validate_and_load(self.source, reconciliation=self.receipt)

    def test_missing_process_or_receipt_evidence_blocks(self):
        receipt = json.loads(self.receipt.read_text())
        receipt['owned_pids'].remove(900004)
        self.write(self.receipt, receipt)
        with self.assertRaisesRegex(ValueError, 'missing from reconciliation'):
            self.load()
        receipt['owned_pids'].append(900004)
        receipt['descendants_checked'] = False
        self.write(self.receipt, receipt)
        with self.assertRaisesRegex(ValueError, 'missing reconciliation evidence'):
            self.load()

    def test_original_and_frozen_policy_hashes_enforced(self):
        (self.folder / 'input.txt').write_text('different question')
        with self.assertRaisesRegex(ValueError, 'original question hash'):
            self.load()
        config = json.loads((self.source/'host-config.json').read_text())
        config['policy_hashes'] = {'policy.md':'not-the-hash'}
        self.write(self.source/'host-config.json', config)
        (self.source/'policy').mkdir()
        (self.source/'policy/policy.md').write_text('policy')
        with self.assertRaisesRegex(ValueError, 'frozen artifact hash'):
            self.load()

    def test_missing_probe_result_is_preserved_unknown(self):
        (self.folder/'probes/main-3-lean/result.json').unlink()
        state = self.load()['problems']['problem']
        self.assertEqual(state['execution_history'][1]['result']['status'], 'unknown')
        self.assertIn('probes/main-3-lean/source.lean', state['execution_history'][1]['artifacts'])

    def test_inconsistent_main_or_reviewer_identity_blocks(self):
        path = self.source/'host/runtime/problem/003-proof-review/stage.meta.json'
        call = json.loads(path.read_text())
        call['session_id'] = 'main-session'
        self.write(path, call)
        with self.assertRaisesRegex(ValueError, 'reviewer identity'):
            self.load()


if __name__ == '__main__':
    unittest.main()
