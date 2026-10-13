"""Synthetic first-writer evidence transitions; no provider or research calls."""
import asyncio
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import pilot_paper as paper
import pilot_paper_recovery as recovery
from pilot_document_tools import prepare_scope
from pilot_exam import ExamRuntime, new_config, rebase_copied_paper_state


class PaperRecoveryTests(unittest.IsolatedAsyncioTestCase):
    def write(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name).resolve()
        self.source, self.target = base/'parent', base/'successor'
        self.source.mkdir()
        self.config = {'exam': new_config(self.source), 'internet_browse': False}
        self.runtime = ExamRuntime(self.config['exam'])
        self.folder = self.source/'campaign/problems/P1'
        self.folder.mkdir(parents=True)
        (self.folder/'input.txt').write_text('Exact synthetic question')
        self.write(self.folder/'proof-current.json', {'revision': 'old'})
        self.write(self.folder/'current-candidate.json', {'proof_markdown': 'old unresolved sketch'})
        (self.folder/'proof.md').write_text('old unresolved sketch')
        self.state = {'problems': {'P1': {'status': 'partial', 'successful_complete': False}}}
        self.pilot = SimpleNamespace(root=self.source, host=self.source/'host', config=self.config,
            semaphore=asyncio.Semaphore(1), campaign=SimpleNamespace(status=lambda: self.state))
        self.problem = SimpleNamespace(ident='P1', folder=self.folder, original_bytes=(self.folder/'input.txt').read_bytes(),
            pilot=self.pilot, current={'proof_markdown': 'old unresolved sketch'}, dossier={}, findings=[], errors=[],
            execution_history=[], final_assessment_history=[], advisory_scope_history=[], calls=[])
        self.snapshot = self.runtime.snapshot(self.problem)
        self.engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        _, scope = self.engine.scoped_payload('reconstruct', {'status': 'historical unresolved input'})
        self.answer = {'tex': paper.baseline_tex('P1'), 'artifacts': {}, 'selected_results': ['unresolved'],
            'evidence_assessment': 'Synthetic current evidence remains explicitly qualified.',
            'reconstruction_map': 'Synthetic reconstruction preserves the current exact scope.'}
        self.name = 'P1/paper-001-reconstruct'
        meta = self.receipt(self.name, scope, 'original prompt', delivered=False, fresh=True)
        self.engine.ledger.update(calls=[meta], admissions=[{'name': self.name, 'resume_session': None}],
            retrieval_progress={'stage': 'reconstruct', 'session': None, 'turns': 1, 'writer': True},
            errors=[{'type': 'DeliveryRecoveryRequired', 'message': 'original rejection'}])
        self.engine.save()
        self.old_ledger = copy.deepcopy(self.engine.ledger)
        self.write(self.folder/'proof-current.json', {'revision': 'new'})
        self.current = {'proof_markdown': 'new genuinely changed synthetic evidence'}
        self.write(self.folder/'current-candidate.json', self.current)
        (self.folder/'proof.md').write_text(self.current['proof_markdown'])
        self.write(self.source/'campaign/state.json', self.state)
        self.saved = dict(main_session='main', implementers=['main'], calls=[{'session_id': 'main'}],
            proof_document={'status': 'submitted'}, current=self.current, dossier={}, findings=[], errors=[],
            execution_history=[], final_assessment_history=[], advisory_scope_history=[])
        self.checkpoint = {'config': self.config, 'problems': {'P1': self.saved},
            'parent': {'source_root': str(self.source), 'manifest_sha256': 'a'*64,
                       'files': {'campaign/state.json': recovery.delivery.digest(self.source/'campaign/state.json')}}}

    def receipt(self, name, scope, prompt, *, delivered, fresh=False):
        stage = self.pilot.host/'runtime'/name
        stage.mkdir(parents=True)
        scope, cap = prepare_scope(scope, stage, {'stage': name, 'request_id': name+'-request',
                                                'session_id': None if fresh else 'actual-writer'})
        raw = json.dumps(self.answer)
        (stage/'stage.answer.txt').write_text(raw)
        self.write(stage/'stage.answer.json', self.answer)
        (stage/'stage.prompt.txt').write_text(prompt)
        meta = {'name': name, 'module': 'paper-reconstruct', 'status': 'completed',
            'session_id': 'actual-writer', 'resume_session': None if fresh else 'actual-writer',
            'fresh_session': fresh, 'request_id': name+'-request', 'model_actual': paper.ASTRA,
            'model_verified': True, 'turn_completed': True, 'pid': 990123, 'exit_code': 0,
            'start_utc': '2026-01-01T00:00:00+00:00', 'end_utc': '2026-01-01T00:00:01+00:00',
            'answer_sha256': hashlib.sha256(raw.encode()).hexdigest(),
            'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(), 'document_capability': cap,
            'persisted_rollout_audit': {'status': 'verified'},
            'document_audit': {'status': 'PASS', 'required_material_delivered': delivered,
                'complete_tool_outputs_delivered': True, 'errors': [], 'delivery_errors': [],
                'required_artifact_coverage': {key: delivered for key in scope['required_artifact_ids']}}}
        self.write(stage/'stage.meta.json', meta)
        return meta

    def request(self):
        return recovery.request_from_checkpoint(self.source, self.target, self.checkpoint, ['P1'],
                                                authority='Explicit synthetic recovery authorization')

    def install(self, request=None):
        request = request or self.request()
        shutil.copytree(self.source, self.target)
        rebase_copied_paper_state(self.source/'exam', self.target/'exam')
        self.write(self.target/recovery.FILE, request)
        config = {**self.config, 'exam': {**self.config['exam'], 'state_root': str(self.target/'exam')},
                  'paper_recovery': {'path': recovery.FILE, 'sha256': recovery.delivery.digest(self.target/recovery.FILE)}}
        # Original clock copied into successor must only change its storage pointer.
        self.write(self.target/'exam/clock.json', config['exam'])
        recovery.install(self.target, config, self.checkpoint, self.pilot.campaign)
        self.pilot = SimpleNamespace(root=self.target, host=self.target/'host', config=config,
                                     semaphore=asyncio.Semaphore(1))
        self.problem = SimpleNamespace(ident='P1', pilot=self.pilot)
        runtime = ExamRuntime(config['exam'])
        snapshot = runtime.snapshot(self.problem)
        return paper.PaperEngine(self.problem, snapshot, runtime)

    async def corrected(self, host, name, prompt, model, timeout, resume=None, **kwargs):
        self.assertEqual(name, 'P1/paper-002-reconstruct')
        self.assertEqual(resume, 'actual-writer')
        ledger = recovery.delivery.read(self.target/'exam/papers/P1/paper-ledger.json')
        self.assertEqual(ledger['retrieval_progress'], {**self.old_ledger['retrieval_progress'], 'turns': 2})
        self.assertEqual(ledger['paper_recovery_admissions'][0]['original_retrieval_progress'],
                         self.old_ledger['retrieval_progress'])
        scope = kwargs['document_scope']
        self.assertIn('current:snapshot.json', scope['required_artifact_ids'])
        self.assertIn('current:evidence/proof.md', scope['required_artifact_ids'])
        self.assertIn('historical:stage-input', scope['required_artifact_ids'])
        self.assertIn('unaccepted-draft', scope['required_artifact_ids'])
        self.assertIn('CURRENT stage-input', prompt)
        return self.receipt(name, scope, paper.document_prompt(prompt, scope['mode'], public_sources=False), delivered=True), self.answer

    async def test_current_snapshot_same_writer_and_existing_budget(self):
        old = {str(p.relative_to(self.source)): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        engine = self.install()
        self.assertNotEqual(engine.snapshot.name, 'snapshot')
        self.assertEqual(recovery.delivery.read(engine.snapshot/'snapshot.json')['research_status'], self.state['problems']['P1'])
        before = engine.output.read_bytes()
        with patch.object(paper, 'call_stage', side_effect=self.corrected) as dispatch:
            identity, answer = await engine.call('reconstruct', 'Synthetic reconstruct', {'evidence': engine.evidence()}, writer=True)
        self.assertEqual(dispatch.await_count, 1)
        self.assertEqual(identity, 'actual-writer')
        self.assertEqual(engine.output.read_bytes(), before)
        self.assertEqual(engine.ledger['calls'][0], self.old_ledger['calls'][0])
        self.assertEqual(engine.ledger['errors'], self.old_ledger['errors'])
        self.assertEqual(engine.ledger['retrieval_history'][0]['turns'], 2)
        self.assertEqual(old, {str(p.relative_to(self.source)): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})
        self.assertIsNone(recovery.delivery.read(self.target/'host/runtime'/self.name/'document-capability.json')['producer']['session_id'])

    async def test_crash_after_admission_reconciles_without_dispatch(self):
        engine = self.install()
        async def crash(*args, **kwargs):
            await self.corrected(*args, **kwargs)
            raise asyncio.CancelledError()
        payload = {'evidence': engine.evidence()}
        with patch.object(paper, 'call_stage', side_effect=crash):
            with self.assertRaises(asyncio.CancelledError):
                await engine.call('reconstruct', 'Synthetic reconstruct', payload, writer=True)
        resumed = paper.PaperEngine(self.problem, engine.snapshot, engine.runtime)
        # New public-source/catalog feedback must not regenerate admitted input.
        with patch.object(paper, 'call_stage', new_callable=AsyncMock) as dispatch:
            await resumed.call('reconstruct', 'Synthetic reconstruct', {'changed_live_catalog': 'new source'}, writer=True)
        dispatch.assert_not_awaited()
        self.assertEqual(resumed.ledger['retrieval_history'][0]['turns'], 2)
        self.assertEqual(len(resumed.ledger['paper_recovery_admissions']), 1)
        with patch.object(paper, 'call_stage', new_callable=AsyncMock) as dispatch:
            await resumed.call('reconstruct', 'Synthetic reconstruct', {}, writer=True)
        dispatch.assert_not_awaited()
        closure = copy.deepcopy(resumed.ledger['retrieval_history'])
        for bad in [[], closure+closure, [{**closure[0], 'turns': 1}]]:
            resumed.ledger['retrieval_history'] = bad
            with patch.object(paper, 'call_stage', new_callable=AsyncMock) as dispatch:
                with self.assertRaisesRegex(ValueError, 'consumed paper turn history'):
                    await resumed.call('reconstruct', 'Synthetic reconstruct', {}, writer=True)
            dispatch.assert_not_awaited()

    async def test_missing_corrective_delivery_consumes_turn_and_cannot_retry(self):
        engine = self.install()
        async def bad(*args, **kwargs):
            meta, answer = await self.corrected(*args, **kwargs)
            meta['document_audit']['required_material_delivered'] = False
            self.write(self.pilot.host/'runtime'/meta['name']/'stage.meta.json', meta)
            return meta, answer
        with patch.object(paper, 'call_stage', side_effect=bad):
            with self.assertRaises(RuntimeError):
                await engine.call('reconstruct', 'Synthetic reconstruct', {}, writer=True)
        with patch.object(paper, 'call_stage', new_callable=AsyncMock) as dispatch:
            with self.assertRaises(RuntimeError):
                await engine.call('reconstruct', 'Synthetic reconstruct', {}, writer=True)
        dispatch.assert_not_awaited()
        self.assertEqual(engine.ledger['retrieval_progress']['turns'], 2)

    def test_rejects_identity_budget_and_unchanged_evidence(self):
        for field, value in [('fresh_session', False), ('resume_session', 'other'), ('model_verified', False),
                             ('turn_completed', False), ('session_id', 'main')]:
            path = self.source/'host/runtime'/self.name/'stage.meta.json'
            original = path.read_bytes()
            meta = json.loads(original); meta[field] = value; self.write(path, meta)
            with self.assertRaises(ValueError): self.request()
            path.write_bytes(original)
        progress = self.engine.ledger['retrieval_progress']
        progress['turns'] = 0; self.engine.save()
        with self.assertRaises(ValueError): self.request()
        progress['turns'] = 1; self.engine.save()
        self.saved['current'] = {'proof_markdown': 'old unresolved sketch'}
        with self.assertRaisesRegex(ValueError, 'unchanged research'): self.request()
        self.saved['current']['notes'] = 'metadata only'
        self.saved['current']['sol_tasks'] = [{'task': 'operational request only'}]
        with self.assertRaisesRegex(ValueError, 'unchanged research'): self.request()

    def test_stale_proof_and_transition_tampering_fail_closed(self):
        engine = self.install()
        pointer = self.target/'campaign/problems/P1/proof-current.json'
        old = pointer.read_bytes(); self.write(pointer, {'revision': 'later'})
        with self.assertRaisesRegex(ValueError, 'transition changed'):
            engine.runtime.snapshot(self.problem)
        pointer.write_bytes(old)
        ledger = engine.root/'paper-ledger.json'
        saved = ledger.read_bytes(); data = json.loads(saved)
        data['paper_recovery_transition']['new_manifest_sha256'] = '0'*64
        self.write(ledger, data)
        with self.assertRaisesRegex(ValueError, 'receipt differs'):
            engine.runtime.snapshot(self.problem)
        ledger.write_bytes(saved)
        transition = self.target/self.pilot.config['paper_recovery_transitions']['P1']['path']
        transition.chmod(0o644); transition.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'receipt changed'):
            engine.runtime.snapshot(self.problem)

    def test_duplicate_unknown_or_changed_parent_target_rejected(self):
        for problems in [['P1', 'P1'], ['other']]:
            with self.assertRaises(ValueError):
                recovery.request_from_checkpoint(self.source, self.target, self.checkpoint, problems, authority='test')
        for key in ['parent_manifest_sha256', 'target_root']:
            request = self.request(); request[key] = 'changed'
            with self.assertRaises(ValueError):
                recovery.validate_request(request, self.source, self.target, self.checkpoint)

    def test_inherited_rejection_paths_and_second_continuation_snapshot(self):
        # Move/copy twice without rewriting the original capability paths.
        inherited = self.source.parent/'inherited'
        shutil.copytree(self.source, inherited)
        rebase_copied_paper_state(self.source/'exam', inherited/'exam')
        first = recovery.binding(self.source, 'P1', self.saved)
        second = recovery.binding(inherited, 'P1', self.saved)
        self.assertEqual(first['files'], second['files'])
        self.assertEqual(first['original_artifacts'], second['original_artifacts'])
        engine = self.install()
        next_root = self.source.parent/'next'
        shutil.copytree(self.target, next_root)
        rebase_copied_paper_state(self.target/'exam', next_root/'exam')
        config = copy.deepcopy(self.pilot.config); config['exam']['state_root'] = str(next_root/'exam')
        self.write(next_root/'exam/clock.json', config['exam'])
        problem = SimpleNamespace(ident='P1', pilot=SimpleNamespace(root=next_root, config=config))
        snapshot = ExamRuntime(config['exam']).snapshot(problem)
        self.assertEqual(snapshot.name, engine.snapshot.name)

    def test_accepted_state_requires_native_carry_and_is_preserved(self):
        self.state['problems']['P1'] = {'status': 'complete', 'successful_complete': True, 'manifest': 'accepted.json'}
        self.write(self.folder/'accepted.json', {'synthetic': 'native manifest'})
        self.write(self.source/'campaign/state.json', self.state)
        self.checkpoint['parent']['files']['campaign/state.json'] = recovery.delivery.digest(self.source/'campaign/state.json')
        engine = self.install()
        snapshot = recovery.delivery.read(engine.snapshot/'snapshot.json')
        self.assertEqual(snapshot['research_status'], self.state['problems']['P1'])
        self.assertEqual(snapshot['current'], self.current)

    def test_disjoint_later_authorization_preserves_old_transition(self):
        engine = self.install()
        config = self.pilot.config
        original = dict(config['paper_recovery'])
        archived = {'path': 'paper-recovery-history/'+original['sha256']+'.json', 'sha256': original['sha256']}
        (self.target/archived['path']).parent.mkdir()
        shutil.copyfile(self.target/recovery.FILE, self.target/archived['path'])
        newer = copy.deepcopy(recovery.load(self.target, config))
        newer['problems'] = {'P2': {**newer['problems']['P1'], 'problem': 'P2'}}
        self.write(self.target/recovery.FILE, newer)
        config['paper_recovery_history'] = [archived]
        config['paper_recovery'] = {'path': recovery.FILE, 'sha256': recovery.delivery.digest(self.target/recovery.FILE)}
        self.assertEqual(engine.runtime.snapshot(self.problem), engine.snapshot)
        self.assertEqual(recovery.authorization(self.target, config, 'P1'), original['sha256'])
        newer['problems']['P1'] = newer['problems']['P2']
        self.write(self.target/recovery.FILE, newer)
        config['paper_recovery']['sha256'] = recovery.delivery.digest(self.target/recovery.FILE)
        with self.assertRaisesRegex(ValueError, 'duplicate problem'):
            recovery.all_requests(self.target, config)

    def test_native_prepare_validates_and_installs_without_launch(self):
        import codex_pilot as pilot
        import pilot_continuation as native
        import pilot_proof_document as documents
        self.current['ledger'] = {'rows': []}
        main_name = 'P1/001-main-dossier'
        main = {'name': main_name, 'module': 'main-dossier', 'status': 'completed',
                'session_id': 'main', 'request_id': 'main-request', 'pid': 990124}
        self.write(self.folder/'001-main-dossier.json', self.current)
        answer = (self.folder/'001-main-dossier.json').read_bytes()
        main['answer_sha256'] = hashlib.sha256(answer).hexdigest()
        self.write(self.source/'host/runtime'/main_name/'stage.meta.json', main)
        (self.source/'host/runtime'/main_name/'stage.answer.txt').write_bytes(answer)
        self.write(self.folder/'paper-001-reconstruct.json', self.answer)
        (self.folder/'proof-current.json').unlink()
        original = recovery.delivery.digest(self.folder/'input.txt')
        documents.submit(self.folder, problem_id='P1', original_sha256=original,
            main_session='main', expected_revision=None, candidate=self.current,
            producer={'stage': main_name, 'request_id': 'main-request', 'session_id': 'main'})
        self.write(self.folder/'current-candidate.json', self.current)
        self.write(self.folder/'host-progress.json', {'main_session': 'main', 'calls': [main], 'open_findings': [], 'errors': []})
        config = {**self.config, 'problems': ['P1'], 'mode': 'lite', 'policy_hashes': {},
            'deadline_utc': self.config['exam']['submission_deadline_utc'], 'proof_document_version': 1,
            'codex_binary': 'synthetic', 'model_concurrency': 1, 'source_url': 'https://example.invalid',
            'original_scope_review_count': 2}
        self.write(self.source/'host-config.json', config)
        self.write(self.source/'campaign/registry.json', {'mode': 'lite', 'deadline_utc': config['deadline_utc'],
                    'problems': {'P1': {'sha256': original}}})
        self.write(self.source/'campaign/state.json', {**self.state, 'sealed': True,
                    'registry_sha256': recovery.delivery.digest(self.source/'campaign/registry.json')})
        self.write(self.source/'pilot-result.json', {'end_utc': '2026-01-01T00:00:02+00:00'})
        receipt = self.source.parent/'reconciliation.json'
        self.write(receipt, {'schema_version': 1, 'source_root': str(self.source),
            'checked_utc': '2026-01-01T00:00:03+00:00', 'host_pid': 990120,
            'owned_pids': [990120, 990123, 990124], 'descendants_checked': True,
            'launch_records_checked': True, 'probe_records_checked': True,
            'evidence': [str(self.source/'pilot-result.json')]})
        before = {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        with patch.object(native.os, 'kill', side_effect=ProcessLookupError), \
             patch.object(native.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '', '')), \
             patch.object(pilot, 'subscription_preflight', return_value={'authentication': 'chatgpt'}):
            request = recovery.make_request(self.source, self.target, receipt, ['P1'], authority='Synthetic explicit authorization')
            path = self.source.parent/'request.json'; self.write(path, request)
            prepared = pilot.prepare_continuation(self.source, self.target, receipt, paper_recovery=path)
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})
        self.assertIn('pilot_paper_recovery.py', prepared['code_hashes'])
        self.assertEqual((self.target/'code/pilot_paper_recovery.py').read_bytes(), Path(recovery.__file__).read_bytes())
        self.assertEqual(prepared['exam']['start_utc'], config['exam']['start_utc'])
        self.assertFalse((self.target/'HOST-STARTED').exists())
        snapshot = recovery.active_snapshot(SimpleNamespace(ident='P1', pilot=SimpleNamespace(root=self.target, config=prepared)),
                                             ExamRuntime(prepared['exam']))
        self.assertEqual(recovery.delivery.read(snapshot/'snapshot.json')['research_status'], self.state['problems']['P1'])
        self.assertEqual(recovery.delivery.read(self.target/'exam/papers/P1/paper-ledger.json')['retrieval_progress']['turns'], 1)


class NativeVersionedSnapshotTests(unittest.TestCase):
    def test_native_continuation_preserves_opaque_versioned_snapshot_and_process_aliases(self):
        import test_pilot_continuation as fixtures
        import pilot_continuation as native
        fixture = fixtures.ContinuationTests(); fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        _, chunk, old, alias = fixture.snapshot_chunk_fixture()
        source = fixture.source
        item = {'old_snapshot_sha256': recovery.delivery.digest(old/'manifest.json'),
                'proof_pointer_sha256': hashlib.sha256(b'{"revision":"new"}').hexdigest()}
        request = {'rule': recovery.RULE, 'existing_turn_limit': 4, 'maximum_admissions_per_problem': 1,
                   'problems': {'problem': item}}
        fixture.write(source/recovery.FILE, request)
        auth = recovery.delivery.digest(source/recovery.FILE)
        name = 'snapshot-recovery-'+auth[:24]
        new = old.with_name(name); shutil.copytree(old, new)
        (new/'evidence/proof-current.json').write_bytes(b'{"revision":"new"}')
        fixture.write(new/'snapshot.json', {'calls': fixture.calls})
        files = {str(p.relative_to(new)): recovery.delivery.digest(p) for p in new.rglob('*') if p.is_file() and p.name != 'manifest.json'}
        fixture.write(new/'manifest.json', {'files': files})
        fixture.write(new.parent/(name+'-receipt.json'), {'manifest_sha256': recovery.delivery.digest(new/'manifest.json')})
        transition = {'rule': recovery.RULE, 'authorization_sha256': auth, 'old_manifest_sha256': item['old_snapshot_sha256'],
            'new_snapshot': name, 'new_manifest_sha256': recovery.delivery.digest(new/'manifest.json')}
        fixture.write(old.parent/'paper-ledger.json', {'paper_recovery_transition': transition})
        receipt = old.parent/('recovery-transition-'+auth[:24]+'.json'); fixture.write(receipt, transition)
        config = recovery.delivery.read(source/'host-config.json')
        config.update(paper_recovery={'path': recovery.FILE, 'sha256': auth}, paper_recovery_transitions={
            'problem': {'path': str(receipt.relative_to(source)), 'sha256': recovery.delivery.digest(receipt)}})
        fixture.write(source/'host-config.json', config)
        new_alias = new/alias.relative_to(old)
        self.assertIn(new_alias, native._opaque_review_chunks(source))
        restored = fixture.load()
        self.assertIn(str(new_alias.relative_to(source)), restored['parent']['files'])
        # Another history copy has the same authenticated alias set, not arbitrary glob exclusions.
        shutil.copytree(source/'exam', source/'history/prior-exam')
        fixture.load()
        rogue = old.with_name('snapshot-recovery-'+'0'*24); shutil.copytree(new, rogue)
        with self.assertRaises(json.JSONDecodeError):
            fixture.load()
