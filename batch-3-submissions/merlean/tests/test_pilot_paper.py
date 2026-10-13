from __future__ import annotations

import asyncio
import hashlib
import json
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import AsyncMock, patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_paper as paper
from codex_transport import _paper_image_inputs, _paper_images_unchanged
from paper_writing_codex.reader_rounds import reader_round_errors
from paper_writing_codex.raw import raw_errors


class Runtime:
    def __init__(self, root):
        self.root, self.seconds = root, 3600
    def paper_dir(self, ident):
        return self.root / 'papers' / ident
    def remaining(self):
        return self.seconds
    def paper_timeout(self, requested):
        if self.seconds <= 0:
            raise TimeoutError('exam deadline')
        return min(requested, self.seconds)


class PaperTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.runtime = Runtime(self.root)
        pilot = types.SimpleNamespace(root=self.root, host=self.root / 'host', config={},
                                      semaphore=asyncio.Semaphore(1))
        self.problem = types.SimpleNamespace(ident='P1', pilot=pilot)
        self.snapshot = self.root / 'snapshot'
        self.snapshot.mkdir()
        (self.snapshot / 'input.txt').write_text('Synthetic test question, no accepted proof.')
        (self.snapshot / 'snapshot.json').write_text(json.dumps({'current': {'status': 'unverified',
                                                       'gap': 'ESSENTIAL_RESEARCH_GAP'}, 'research_status': 'RUNNING'}))
        manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in self.snapshot.iterdir()}
        (self.snapshot / 'manifest.json').write_text(json.dumps({'schema_version': 1, 'files': manifest}))
        self.tex = paper.baseline_tex('P1')
        self.requests = []
        self.session_count = 0

    async def transport(self, root, name, prompt, model, timeout, resume=None, **kwargs):
        stage = kwargs['module'].removeprefix('paper-')
        self.requests.append((stage, prompt, resume, kwargs))
        self.session_count += 1
        identity = resume or f'actual-session-{self.session_count}'
        answer = {}
        if stage in ('reconstruct', 'draft', 'polish'):
            answer = {'tex': self.tex, 'artifacts': {}, 'selected_results': ['unresolved'],
                'evidence_assessment': 'The only supplied argument has an essential unresolved research gap.',
                'reconstruction_map': 'The raw answer explicitly states unresolved status and makes no proof claim.',
                'semantic_justification': 'The already short unresolved answer must retain its explicit honest qualifications.'}
            if stage == 'draft':
                answer['literature_search'] = {'schema_version': 1, 'status': 'constrained', 'queries': [], 'candidates': [],
                    'findings': 'This synthetic test transport made no actual reference search and cannot claim completion.'}
        elif stage == 'raw-audit':
            answer = {'verdict': 'PASS', 'unresolved_fidelity_issues': [], 'research_gaps': ['essential gap'],
                      'findings': 'The synthetic raw answer explicitly retains unresolved status and claims no theorem.'}
            answer['scientific_source_findings'] = {name: 'The synthetic reviewer read this frozen input and found no named external credit.'
                for name in paper._json(self.snapshot / 'manifest.json')['files'] if not name.startswith('evidence/public-sources/')}
            answer['input_credit_census'] = {'schema_version': 1, 'verdict': 'PASS', 'credits': [],
                'findings': 'The synthetic original inputs contain no citation or named external credit.'}
        elif stage.startswith('reader-'):
            answer = {'findings': 'The synthetic manuscript consistently explains that the answer remains unresolved.',
                      'issues': [], 'verdict': 'PASS', 'unresolved_findings': []}
            answer['axes'] = {axis: {'verdict': 'PASS', 'unresolved_findings': [],
                'findings': 'The synthetic unresolved answer supplies no unsupported claim on this axis.'}
                for axis in ('exposition', 'attribution')}
        elif stage.startswith('revise-'):
            answer = {'tex': self.tex, 'artifacts': {}, 'responses': [],
                'revision_summary': 'The reader identified no changes; the unresolved status remains clearly stated.',
                'no_change_reason': 'No reader issue was identified and removing the qualification would misrepresent evidence.'}
        elif stage == 'verify-2':
            answer = {'verdict': 'PASS', 'unresolved_substantive_issues': [],
                'findings': 'Both no-change dispositions are supported by the clear unchanged unresolved manuscript.',
                'legacy': {'verdict': 'PASS', 'unresolved_findings': [],
                           'findings': 'The final unresolved manuscript retains its accurate qualification and clear reading order.'}}
            answer['axes'] = {axis: {'verdict': 'PASS', 'unresolved_findings': [],
                'findings': 'The synthetic final unchanged unresolved answer has no defect on this axis.'}
                for axis in ('exposition', 'attribution')}
        return {'name': name, 'status': 'completed', 'model_actual': model, 'model_verified': True,
                'session_id': identity, 'module': kwargs['module'],
                'document_audit': {'required_material_delivered': True}}, answer

    def retrieval_fixture(self, interrupted_count=1):
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        session='saved-writer'
        engine.ledger['writer_ids']=[session]
        engine.ledger['evidence_requests']={'reconstruct':['input.txt']}
        def receipt(number,status,answer,**extra):
            name=f'P1/paper-{number:03d}-reconstruct'
            path=self.problem.pilot.host/'runtime'/name;path.mkdir(parents=True)
            (path/'stage.answer.txt').write_text(answer)
            meta={'name':name,'module':'paper-reconstruct','status':status,'pid':800000+number,
                  'exit_code':0 if status=='completed' else -15,
                  'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00',
                  'answer_sha256':hashlib.sha256(answer.encode()).hexdigest(),**extra}
            paper._write(path/'stage.meta.json',meta)
            engine.ledger['calls'].append(meta if status=='completed' else {'name':name,'stage':'reconstruct','status':'admitted'})
        receipt(1,'unverifiable_rollout_audit','',session_id=None,resume_session=None)
        receipt(2,'completed',json.dumps({'evidence_requests':['input.txt']}),session_id=session,
                resume_session=None,fresh_session=True,model_actual=paper.ASTRA,model_verified=True,
                turn_completed=True,document_audit={'required_material_delivered':True})
        for n in range(interrupted_count):
            receipt(n+3,'cancelled','Reading required material.',session_id=session,resume_session=session,
                    model_actual=paper.ASTRA,model_verified=True,turn_completed=False,answer_json_extracted=False,
                    answer_parse_error='not JSON')
        engine.save()
        return paper.PaperEngine(self.problem,self.snapshot,self.runtime)

    async def test_no_model_startup_failure_preserves_consumed_admission(self):
        import pilot_document_startup as startup
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        name='P1/paper-001-reconstruct';directory=self.problem.pilot.host/'runtime'/name
        directory.mkdir(parents=True)
        cap=directory/'document-capability.json';cap.write_text(json.dumps({'producer':{'stage':name,'request_id':'synthetic','session_id':None}}))
        runtime=startup.prepare_runtime(directory)
        allocation={'granted_seconds':60}
        engine.ledger['calls']=[{'name':name,'stage':'reconstruct','status':'admitted','timeout_allocation':allocation}]
        engine.ledger['admissions']=[{'name':name,'stage':'reconstruct','resume_session':None,'timeout_allocation':allocation}]
        progress={'stage':'reconstruct','session':None,'turns':1,'writer':True}
        engine.ledger['retrieval_progress']=progress.copy()
        meta={'name':name,'module':'paper-reconstruct','status':'process_launch_failed','model_dispatched':False,
              'session_id':None,'resume_session':None,'pid':None,'process_identity':None,'fresh_session':True,
              'startup_failure':'synthetic startup failure','request_id':'synthetic','start_utc':'2026-01-01T00:00:00+00:00',
              'end_utc':'2026-01-01T00:00:01+00:00','document_runtime':runtime,
              'document_capability':{'path':str(cap),'sha256':hashlib.sha256(cap.read_bytes()).hexdigest()}}
        paper._write(directory/'stage.meta.json',meta)
        paper._write(directory/'document-startup.json',{'status':'FAIL','model_calls':0,'cleanup':None,'runtime':runtime})
        engine.save();engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        engine.restore_retrieval('reconstruct',writer=True)
        self.assertEqual(engine.ledger['retrieval_progress'],progress)
        self.assertEqual(engine.next_call_number(),2)
        second='P1/paper-002-reconstruct';path=self.problem.pilot.host/'runtime'/second;path.mkdir()
        answer=json.dumps({'evidence_requests':['input.txt']});(path/'stage.answer.txt').write_text(answer)
        completed={'name':second,'module':'paper-reconstruct','status':'completed','pid':800002,'exit_code':0,
                   'start_utc':meta['start_utc'],'end_utc':meta['end_utc'],'session_id':'new-writer','resume_session':None,
                   'fresh_session':True,'model_actual':paper.ASTRA,'model_verified':True,'turn_completed':True,
                   'document_audit':{'required_material_delivered':True},'answer_sha256':hashlib.sha256(answer.encode()).hexdigest()}
        paper._write(path/'stage.meta.json',completed);engine.ledger['calls'].append(completed)
        engine.ledger['writer_ids']=['new-writer'];engine.ledger['evidence_requests']={'reconstruct':['input.txt']}
        engine.ledger['retrieval_progress']={'stage':'reconstruct','session':'new-writer','turns':2,'writer':True}
        engine.restored_ledger=True;engine.restore_retrieval('reconstruct',writer=True)
        self.assertEqual(engine.ledger['retrieval_progress']['turns'],2)
        self.assertEqual(engine.ledger['retrieval_progress']['session'],'new-writer')
        for changes in ({'model_dispatched':True},{'session_id':'unexpected'},{'pid':123}):
            paper._write(directory/'stage.meta.json',{**meta,**changes})
            engine.restored_ledger=True
            with self.assertRaises(paper.PaperRecoveryRequired):engine.restore_retrieval('reconstruct',writer=True)

    async def test_interrupted_retrieval_resumes_same_writer_with_consumed_turns(self):
        engine=self.retrieval_fixture()
        before={p:str(p.stat().st_mtime_ns) for p in (self.problem.pilot.host/'runtime').rglob('*') if p.is_file()}
        async def dispatch(root,name,prompt,model,timeout,resume=None,**kwargs):
            self.assertEqual(name,'P1/paper-004-reconstruct')
            self.assertEqual(resume,'saved-writer')
            self.assertEqual(engine.ledger['retrieval_progress']['turns'],3)
            self.assertIn('archive:input.txt',kwargs['document_scope']['required_artifact_ids'])
            return await self.transport(root,name,prompt,model,timeout,resume,**kwargs)
        with patch.object(paper,'call_stage',dispatch):
            identity,answer=await engine.call('reconstruct','synthetic',{},writer=True)
        self.assertEqual(identity,'saved-writer');self.assertIn('tex',answer)
        self.assertEqual(engine.ledger['evidence_requests']['reconstruct'],['input.txt'])
        self.assertNotIn('retrieval_progress',engine.ledger)
        self.assertTrue(all(str(Path(p).stat().st_mtime_ns)==stamp for p,stamp in before.items()))
        self.assertEqual(len(self.requests),1)

    async def test_interrupted_retrieval_cannot_renew_four_turn_budget(self):
        engine=self.retrieval_fixture(interrupted_count=3)
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
            with self.assertRaisesRegex(ValueError,'four bounded turns'):
                await engine.call('reconstruct','synthetic',{},writer=True)
        dispatch.assert_not_awaited()
        self.assertEqual(engine.ledger['retrieval_progress']['turns'],4)

    async def test_retrieval_rejects_same_resume_but_changed_returned_session(self):
        engine=self.retrieval_fixture()
        path=self.problem.pilot.host/'runtime/P1/paper-003-reconstruct'
        answer=json.dumps({'evidence_requests':['snapshot.json']})
        (path/'stage.answer.txt').write_text(answer)
        meta=json.loads((path/'stage.meta.json').read_text())
        meta.update(status='completed',session_id='different-returned-session',resume_session='saved-writer',
            turn_completed=True,answer_sha256=hashlib.sha256(answer.encode()).hexdigest(),
            document_audit={'required_material_delivered':True})
        paper._write(path/'stage.meta.json',meta)
        engine.ledger['calls'][-1]=meta
        engine.ledger['writer_ids'].append('different-returned-session')
        engine.ledger['evidence_requests']['reconstruct'].append('snapshot.json')
        with self.assertRaisesRegex(paper.PaperRecoveryRequired,'changed saved session'):
            engine.restore_retrieval('reconstruct',writer=True)

    async def test_retrieval_rejects_changed_session_model_hash_and_completed_answer(self):
        engine=self.retrieval_fixture()
        path=self.problem.pilot.host/'runtime/P1/paper-003-reconstruct/stage.meta.json'
        original=json.loads(path.read_text())
        for changes in ({'session_id':'different'},{'model_actual':'different'},
                        {'answer_sha256':'wrong'},{'turn_completed':True},{'answer_json_extracted':True}):
            with self.subTest(changes=changes):
                paper._write(path,{**original,**changes})
                with patch.object(paper,'call_stage',new_callable=AsyncMock) as dispatch:
                    with self.assertRaises(paper.PaperRecoveryRequired):
                        await engine.call('reconstruct','synthetic',{},writer=True)
                dispatch.assert_not_awaited()
        paper._write(path,original)
        (path.parent/'stage.answer.json').write_text('{}')
        with self.assertRaises(paper.PaperRecoveryRequired):
            engine.restore_retrieval('reconstruct',writer=True)

    async def test_deadline_still_creates_honest_baseline_without_dispatch(self):
        self.runtime.seconds = 0
        with patch.object(paper, 'call_stage', new_callable=AsyncMock) as call:
            result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertTrue(result['terminal'])
        self.assertFalse(result['polishing_complete'])
        self.assertIn('Unresolved answer', Path(result['best_available_tex']).read_text())
        call.assert_not_awaited()

    async def test_inherited_failed_namespace_does_not_collide_or_replay_completed_steps(self):
        import shutil
        parent=self.root/'parent-paper-001';parent.mkdir()
        paper._write(parent/'stage.meta.json',{'name':'P1/paper-001-reconstruct','module':'paper-reconstruct','status':'unverifiable_rollout_audit','pid':900001,'exit_code':1,'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00'})
        (parent/'stage.answer.txt').write_bytes(b'')
        inherited=self.problem.pilot.host/'runtime/P1/paper-001-reconstruct'
        shutil.copytree(parent,inherited)
        before={p.name:p.read_bytes() for p in inherited.iterdir()}
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        engine.ledger.update(stage='polish',completed=['reconstruct','raw-audit','draft','freeze-shrink'],writer_session='saved-writer',writer_ids=['saved-writer'])
        engine.ledger['calls']=[{'name':'P1/paper-007-draft','status':'completed','session_id':'saved-writer'}]
        engine.save()
        resumed=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',side_effect=self.transport) as call:
            identity,_=await resumed._call_once('polish','continue saved stage',{},resume='saved-writer',writer=True)
        self.assertEqual(call.call_args.args[1],'P1/paper-008-polish')
        self.assertEqual(identity,'saved-writer');self.assertEqual([r[0] for r in self.requests],['polish'])
        self.assertEqual(resumed.ledger['completed'],engine.ledger['completed'])
        self.assertEqual(before,{p.name:p.read_bytes() for p in inherited.iterdir()})
        self.assertEqual(before,{p.name:p.read_bytes() for p in parent.iterdir()})

    async def test_actual_empty_ledger_inherited_failed_paper001_uses002(self):
        stage=self.problem.pilot.host/'runtime/P1/paper-001-reconstruct';stage.mkdir(parents=True)
        paper._write(stage/'stage.meta.json',{'name':'P1/paper-001-reconstruct','module':'paper-reconstruct','status':'unverifiable_rollout_audit','pid':900001,'exit_code':1,'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00'})
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        with patch.object(paper,'call_stage',side_effect=self.transport) as call:
            await engine._call_once('reconstruct','synthetic',{},writer=True)
        self.assertEqual(call.call_args.args[1],'P1/paper-002-reconstruct')

    async def test_completed_transport_with_admitted_ledger_requires_reconciliation(self):
        stage=self.problem.pilot.host/'runtime/P1/paper-001-reconstruct';stage.mkdir(parents=True)
        meta={'name':'P1/paper-001-reconstruct','module':'paper-reconstruct','status':'completed','session_id':'saved','answer_sha256':'a'*64,'pid':900001,'exit_code':0,'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00'}
        paper._write(stage/'stage.meta.json',meta)
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        engine.ledger['calls']=[{'name':meta['name'],'status':'admitted'}];engine.save()
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as call,patch.object(paper.PaperEngine,'repair',new_callable=AsyncMock) as repair:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        self.assertEqual(result['operational_failure'],'infrastructure');call.assert_not_awaited();repair.assert_not_awaited()
        self.assertEqual(result['calls'][0]['status'],'admitted')

    async def test_completed_response_before_checkpoint_advance_is_not_replayed(self):
        stage=self.problem.pilot.host/'runtime/P1/paper-001-reconstruct';stage.mkdir(parents=True)
        meta={'name':'P1/paper-001-reconstruct','module':'paper-reconstruct','status':'completed','session_id':'saved','answer_sha256':'a'*64,'pid':900001,'exit_code':0,'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00'}
        paper._write(stage/'stage.meta.json',meta)
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime);engine.ledger['calls']=[meta];engine.save()
        with patch.object(paper,'call_stage',new_callable=AsyncMock) as call:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        self.assertEqual(result['operational_failure'],'infrastructure');call.assert_not_awaited()

    async def test_storage_error_is_current_infrastructure_not_paid_content_repair(self):
        with patch.object(paper.PaperEngine,'run',new=AsyncMock(side_effect=FileExistsError('preserved namespace'))), \
             patch.object(paper.PaperEngine,'repair',new_callable=AsyncMock) as repair:
            result=await paper.run_exam_paper(self.problem,self.snapshot,self.runtime)
        self.assertEqual(result['status'],'incomplete');self.assertEqual(result['operational_failure'],'infrastructure');repair.assert_not_awaited()

    async def test_ambiguous_paper_namespace_never_dispatches(self):
        stage=self.problem.pilot.host/'runtime/P1/paper-001-reconstruct';stage.mkdir(parents=True)
        valid={'name':'P1/paper-001-reconstruct','module':'paper-reconstruct','status':'process_failed','pid':900001,'exit_code':1,
            'start_utc':'2026-01-01T00:00:00+00:00','end_utc':'2026-01-01T00:00:01+00:00'}
        for field,value in [('status',None),('status','unknown'),('end_utc',None),('exit_code',None),('pid',None),('name','P1/paper-999-other')]:
            with self.subTest(field=field,value=value):
                paper._write(stage/'stage.meta.json',{**valid,field:value})
                engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
                with patch.object(paper,'call_stage',new_callable=AsyncMock) as call:
                    with self.assertRaises(paper.PaperRecoveryRequired):await engine._call_once('reconstruct','test',{})
                    call.assert_not_awaited()

    async def test_unresolved_admission_or_duplicate_names_never_dispatch(self):
        engine=paper.PaperEngine(self.problem,self.snapshot,self.runtime)
        admission={'name':'P1/paper-001-reconstruct','status':'admitted'}
        for calls in [[admission],[admission,admission]]:
            engine.ledger['calls']=calls
            with patch.object(paper,'call_stage',new_callable=AsyncMock) as call:
                with self.assertRaises(paper.PaperRecoveryRequired):await engine._call_once('reconstruct','test',{})
                call.assert_not_awaited()

    async def test_real_paper_deadline_becomes_terminal_partial(self):
        from pilot_exam import PaperDeadline
        def expired(requested):
            raise PaperDeadline('real original exam deadline reached')
        self.runtime.paper_timeout = expired
        result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertTrue(result['terminal'])
        self.assertEqual(result['status'], 'deadline-partial')
        self.assertTrue(Path(result['best_available_tex']).is_file())

    async def test_historical_transport_text_is_not_in_inline_paper_input(self):
        evidence = self.snapshot / 'evidence'
        evidence.mkdir()
        history = evidence / 'historical-transport.json'
        history.write_text('HISTORICAL_SENTINEL' * 10000)
        manifest = paper._json(self.snapshot / 'manifest.json')
        manifest['files']['evidence/historical-transport.json'] = paper.sha256_file(history)
        paper._write(self.snapshot / 'manifest.json', manifest)
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        selected = engine.evidence()
        self.assertNotIn('HISTORICAL_SENTINEL', json.dumps(selected))
        visible, scope = engine.scoped_payload('reconstruct', {'evidence': selected})
        self.assertLess(len(visible), 2000)
        index = json.loads(Path(scope['readonly_artifacts']['archive-index']['path']).read_text())
        self.assertTrue(any(item['path'] == 'evidence/historical-transport.json' for item in index))
        self.assertFalse(any(item['path'] == str(history) for item in scope['readonly_artifacts'].values()))
        self.assertEqual(scope['required_artifact_ids'], ['stage-input'])

    async def test_banked_candidate_loads_actual_convergence_pointer_store(self):
        from pilot_convergence import ConvergenceStore
        evidence = self.snapshot / 'evidence'
        evidence.mkdir()
        state = {'candidates': {'banked': {'candidate': {'proof_markdown': 'BANKED_COMPLETE_PROOF'},
                    'scope_qualification': 'audited_original_scope', 'deficits': {}, 'observation_refs': {}}},
                 'observations': {}, 'research_archive': {}, 'auxiliary_archive': {},
                 'best_reviewed_original_candidate': 'banked', 'best_reviewed_mathematical_candidate': None}
        ConvergenceStore(evidence).save(state)
        manifest = paper._json(self.snapshot / 'manifest.json')
        for path in evidence.rglob('*'):
            if path.is_file():
                manifest['files'][str(path.relative_to(self.snapshot))] = paper.sha256_file(path)
        paper._write(self.snapshot / 'manifest.json', manifest)
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        packet = engine.evidence()
        self.assertEqual(packet['selected_candidate']['proof_markdown'], 'BANKED_COMPLETE_PROOF')
        self.assertEqual(packet['selection_qualification'], 'audited_original_scope')

    async def test_relative_dependency_required_and_stale_reference_explicit(self):
        evidence = self.snapshot / 'evidence'
        evidence.mkdir()
        dependency = evidence / 'dep.json'
        dependency.write_text('{"verified": false}')
        manifest = paper._json(self.snapshot / 'manifest.json')
        manifest['files']['evidence/dep.json'] = paper.sha256_file(dependency)
        paper._write(self.snapshot / 'manifest.json', manifest)
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        reference = {'path': 'dep.json', 'sha256': paper.sha256_file(dependency)}
        _, scope = engine.scoped_payload('proof-audit', {'candidate': reference})
        self.assertIn('archive:evidence/dep.json', scope['required_artifact_ids'])
        self.assertEqual(engine.unresolved_dependencies(reference), [])
        self.assertTrue(engine.unresolved_dependencies({**reference, 'sha256': '0' * 64}))
        self.assertEqual(len(engine.unresolved_dependencies({'path': 'missing.json', 'sha256': 'f' * 64, 'nested': reference})), 1)

    async def test_large_reader_payload_gets_no_research_archive(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        payload = {'manuscript': '\\begin{document}' + 'Mathematics. ' * 10000 + '\\end{document}',
                   'guideline': paper.READER_RUBRIC}
        visible, scope = engine.scoped_payload('reader-1', payload)
        self.assertEqual(set(scope['readonly_artifacts']), {'stage-input'})
        self.assertEqual(json.loads(Path(scope['readonly_artifacts']['stage-input']['path']).read_text()), payload)

    async def test_baseline_before_snapshot_exists(self):
        result = paper.prepare_exam_fallback(self.problem, self.runtime)
        self.assertIn('A complete solution is not established', Path(result['tex']).read_text())
        self.assertFalse(result['polishing_complete'])

    async def test_actual_dispatch_raw_freeze_and_no_research_upgrade(self):
        before = (self.snapshot / 'snapshot.json').read_bytes()
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        with patch.object(paper, 'call_stage', side_effect=self.transport), patch.object(
                engine, 'compile', side_effect=RuntimeError('missing compiler')):
            try:
                await engine.run()
            except RuntimeError:
                pass
        self.assertEqual([p[0] for p in self.requests], ['reconstruct', 'raw-audit', 'draft'])
        self.assertEqual(raw_errors(paper._json(engine.state_path), required=True, lineage=True), [])
        self.assertFalse(engine.ledger['research_acceptance_changed'])
        self.assertEqual((self.snapshot / 'snapshot.json').read_bytes(), before)
        self.assertEqual(Path(engine.ledger['best_available_tex']).name, 'raw-source.tex')

    async def test_full_two_distinct_readers_are_unprimed_and_second_verifies(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.output.write_text(self.tex)
        engine.ledger.update(stage='reader-1', writer_session='writer', writer_ids=['writer'])
        async def stop_compile(*args):
            raise RuntimeError('stop after real reader rounds')
        with patch.object(paper, 'call_stage', side_effect=self.transport), patch.object(engine, 'compile', side_effect=stop_compile):
            with self.assertRaises(RuntimeError):
                await engine.run()
        self.assertEqual([p[0] for p in self.requests], ['reader-1', 'revise-1', 'reader-2', 'revise-2', 'verify-2'])
        for stage, prompt, resume, _ in self.requests:
            if stage in ('reader-1', 'reader-2'):
                payload = json.loads(prompt.split('\nINPUT:\n')[1])
                self.assertEqual(set(payload), {'manuscript', 'guideline'})
                self.assertNotIn('ESSENTIAL_RESEARCH_GAP', prompt)
                self.assertIn('assigned independent Astra manuscript reader', prompt)
                self.assertNotIn('The exam is ten problems', prompt)
                self.assertNotIn('source inspection, locators or BibTeX from memory', prompt)
                self.assertIsNone(resume)
        self.assertNotEqual(engine.ledger['reader_1'], engine.ledger['reader_2'])
        self.assertEqual(self.requests[-1][2], engine.ledger['reader_2'])
        self.assertEqual(reader_round_errors(paper._json(engine.state_path), required=True), [])
        self.assertEqual(paper._json(engine.work / '08-reader-rounds.json')['schema_version'], 2)
        self.assertEqual(set(paper._json(engine.work / '08-round-1-reader.json')['axes']),
                         {'exposition', 'attribution'})
        self.assertNotIn('SOURCE', self.requests[0][1])

    async def test_reader_material_boundary_rejects_context_and_omitted_sources(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        for extra in ({'author_map': 'private rationale'}, {'prior_report': 'old findings'}):
            with self.assertRaisesRegex(ValueError, 'unauthorized context'):
                engine.scoped_payload('reader-1', {'manuscript': self.tex, 'guideline': paper.READER_RUBRIC, **extra})
        with self.assertRaisesRegex(ValueError, 'external or dynamic'):
            engine.scoped_payload('reader-1', {'manuscript': self.tex.replace('\\end{document}',
                '\\input{omitted}\\end{document}'), 'guideline': paper.READER_RUBRIC})

    async def test_restored_legacy_reader_contract_stays_legacy(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.ledger.pop('reader_contract')
        engine.save()
        restored = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        self.assertFalse(restored.isolated_readers())

    async def test_reference_cache_scope_and_legacy_layout_are_frozen(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        self.assertEqual(engine.reference_store(), engine.root / 'refs/public-sources')
        _, scope = engine.scoped_payload('draft', {})
        self.assertEqual(scope['store_root'], str(engine.root))
        engine.ledger.pop('literature_contract')
        engine.ledger.pop('reference_cache')
        engine.save()
        restored = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        self.assertFalse(restored.literature_enabled())
        self.assertEqual(restored.reference_store(), restored.root / 'public-sources')

    async def test_new_recovery_scope_cache_selector_preserves_bound_evidence_and_legacy(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        _, scope = engine.scoped_payload('reconstruct', {})
        binding = paper.delivery.scope_binding(scope)
        engine.bind_reference_cache(scope, online=True)
        self.assertEqual(scope['public_source_store'], str(engine.root / 'refs/public-sources'))
        self.assertEqual(paper.delivery.scope_binding(scope), binding)
        explicit = {**scope, 'public_source_store': str(engine.root / 'public-sources')}
        original = json.loads(json.dumps(explicit))
        engine.bind_reference_cache(explicit, online=True)
        self.assertEqual(explicit, original)
        engine.ledger.pop('literature_contract')
        absent = {key: value for key, value in scope.items() if key != 'public_source_store'}
        engine.bind_reference_cache(absent, online=True)
        self.assertNotIn('public_source_store', absent)
        engine.ledger['literature_contract'] = 'search-read-v1'
        engine.bind_reference_cache(absent, online=False)
        self.assertNotIn('public_source_store', absent)

    async def test_input_census_material_covers_frozen_scientific_inputs(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        _, scope = engine.scoped_payload('raw-audit', {})
        self.assertIn('archive:input.txt', scope['required_artifact_ids'])
        self.assertIn('archive:snapshot.json', scope['required_artifact_ids'])
        with self.assertRaisesRegex(ValueError, 'actual read findings'):
            engine.scientific_source_records({})

    async def test_missing_census_does_not_freeze_raw_checkpoint(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        async def missing_census(*args, **kwargs):
            meta, answer = await self.transport(*args, **kwargs)
            if kwargs['module'] == 'paper-raw-audit':
                answer.pop('input_credit_census')
            return meta, answer
        with patch.object(paper, 'call_stage', side_effect=missing_census):
            with self.assertRaisesRegex(ValueError, 'before freezing'):
                await engine.run()
        self.assertNotIn('raw_checkpoint', paper._json(engine.state_path))
        self.assertEqual(engine.ledger['stage'], 'raw-audit')

    async def test_declared_search_cannot_create_execution_or_approval(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.output.write_text(self.tex)
        record = {'schema_version': 1, 'status': 'constrained', 'queries': [], 'candidates': [],
                  'findings': 'No real search was available in this synthetic test and completion is not asserted.'}
        engine.store_literature_search({'literature_search': record, 'search_records': [
            {'query': 'synthetic query', 'execution': 'network-search', 'candidate_ids': [],
             'findings': 'This is an unsupported declaration, with no actual transport receipt.'}]})
        saved = paper._json(engine.work / '03-search-query-1.json')
        self.assertNotIn('host_call', saved)
        self.assertEqual(paper._json(engine.work / '03-literature-search.json')['status'], 'constrained')
        self.assertTrue(paper.literature_search_errors(paper._json(engine.state_path), required=True))

    async def test_source_observation_binds_only_read_window_containing_actual_excerpt(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        source = engine.work / 'source.txt'
        source.write_text('Intro. ' * 800 + 'The exact cited claim appears here.' + ' Tail.' * 50)
        digest = paper.sha256_file(source)
        excerpt = 'The exact cited claim appears here.'
        offset = source.read_text().index(excerpt)
        name = 'P1/paper-001-draft'
        folder = self.problem.pilot.host / 'runtime' / name
        folder.mkdir(parents=True)
        rollout = folder / 'synthetic-rollout.jsonl'
        rollout.write_text('')
        meta = {'session_id': 'writer', 'module': 'paper-draft', 'persisted_rollout_audit': {
            'rollout_paths': [str(rollout)], 'tool_events': [{'call_id': 'early'}, {'call_id': 'claim'}]}}
        paper._write(folder / 'stage.meta.json', meta)
        operations = folder / 'document-operations.jsonl'
        def operation(call_id, start, end):
            return {'call_id': call_id, 'session_id': 'writer', 'tool': 'read_public_source', 'is_error': False,
                    'public_source': {'status': 'read', 'sha256': digest, 'start': start, 'end': end}}
        early = operation('early', 0, 10)
        claim = operation('claim', offset, offset + len(excerpt))
        operations.write_text(json.dumps(early) + '\n' + json.dumps(claim) + '\n')
        engine.ledger['calls'].append({'name': name, 'module': 'paper-draft'})
        record = {'source_path': str(source), 'source_sha256': digest, 'excerpt': excerpt,
                  'excerpt_sha256': hashlib.sha256(excerpt.encode()).hexdigest()}
        bound = engine.bind_literature_observation(record, reading=True)
        self.assertEqual(bound['host_call'], {'session_id': 'writer', 'call_id': 'claim'})
        operations.write_text(json.dumps(early) + '\n')
        self.assertNotIn('host_call', engine.bind_literature_observation(record, reading=True))
        # Public read offsets and excerpts describe the exact raw source text,
        # including TeX comments; stripping comments changes the observed text.
        commented = engine.work / 'commented-source.tex'
        comment_excerpt = 'Claim text. % Exact source comment\nProof text.'
        commented.write_text('% Introductory source comment\n' + comment_excerpt)
        digest = paper.sha256_file(commented)
        start = commented.read_text().index(comment_excerpt)
        operations.write_text(json.dumps(operation('claim', start, start + len(comment_excerpt))) + '\n')
        comment_record = {'source_path': str(commented), 'source_sha256': digest, 'excerpt': comment_excerpt,
                          'excerpt_sha256': hashlib.sha256(comment_excerpt.encode()).hexdigest()}
        self.assertEqual(engine.bind_literature_observation(comment_record, reading=True)['host_call']['call_id'], 'claim')

    async def test_query_observation_binds_only_actual_structured_search(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        name = 'P1/paper-001-draft'
        folder = self.problem.pilot.host / 'runtime' / name
        folder.mkdir(parents=True)
        rollout = folder / 'synthetic-rollout.jsonl'
        (folder / 'document-operations.jsonl').write_text('')
        query = 'a specific relevance query'
        def payload(arguments):
            return {'type': 'response_item', 'payload': {'type': 'function_call', 'namespace': 'web',
                'name': 'run', 'call_id': 'native', 'arguments': json.dumps(arguments)}}
        paper._write(folder / 'stage.meta.json', {'session_id': 'writer', 'module': 'paper-draft',
            'persisted_rollout_audit': {'rollout_paths': [str(rollout)], 'tool_events': [{
                'call_id': 'native', 'verified_native_web': 'native-web-run-v1'}]}})
        engine.ledger['calls'].append({'name': name, 'module': 'paper-draft'})
        for request in ({'open': [{'ref_id': query}]}, {'find': [{'ref_id': 'url', 'pattern': query}]},
                        {'search_query': [{'q': 'different query', 'note': query}]}):
            rollout.write_text(json.dumps(payload(request)) + '\n')
            self.assertNotIn('host_call', engine.bind_literature_observation({'query': query}, reading=False))
        rollout.write_text(json.dumps(payload({'search_query': [{'q': query}]})) + '\n')
        self.assertEqual(engine.bind_literature_observation({'query': query}, reading=False)['host_call'],
                         {'session_id': 'writer', 'call_id': 'native'})

    async def test_custom_and_local_shadow_packages_fail_reader_dispatch(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        custom = self.tex.replace('\\begin{document}', '\\usepackage{local-results}\\begin{document}')
        with self.assertRaisesRegex(ValueError, 'custom or locally shadowed'):
            engine.reader_payload('reader-1', custom)
        (engine.root / 'geometry.sty').write_text('A project-local scientific macro package.')
        with self.assertRaisesRegex(ValueError, 'custom or locally shadowed'):
            engine.reader_payload('reader-1', self.tex)

    async def test_final_attribution_needs_distinct_actual_auditor_and_reports(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.output.write_text(self.tex)
        census_path = engine.work / '08-input-credit-census.json'
        paper._write(census_path, {'reviewer_id': 'raw-reader'})
        state = paper._json(engine.state_path)
        state['input_credit_census'] = paper._ref(census_path)
        paper._write(engine.state_path, state)
        with self.assertRaisesRegex(ValueError, 'independent of writers and input census'):
            engine.store_audits('raw-reader', {})
        with self.assertRaisesRegex(ValueError, 'actual attribution and search/read audits'):
            engine.store_audits('new-proof-auditor', {})

    async def test_unverified_transport_cannot_write_draft(self):
        async def failed(*args, **kwargs):
            return {'status': 'completed', 'model_actual': 'other', 'model_verified': True,
                    'session_id': 'false'}, {'tex': '\\documentclass{article}\\begin{document}FAKE PROOF\\end{document}'}
        with patch.object(paper, 'call_stage', side_effect=failed):
            result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertFalse(result['polishing_complete'])
        self.assertIn('Unresolved answer', Path(result['best_available_tex']).read_text())

    async def test_snapshot_tamper_blocks_dispatch(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        (self.snapshot / 'input.txt').write_text('changed question')
        with patch.object(paper, 'call_stage', new_callable=AsyncMock) as call:
            with self.assertRaisesRegex(ValueError, 'contents changed'):
                await engine.run()
        call.assert_not_awaited()

    async def test_writer_cannot_author_audit_or_state(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        for name in ('07-reader-audit.json', '../escape', '00-run-state.json', '08-reader-rounds.json'):
            with self.assertRaises(ValueError):
                engine.writer_result({'artifacts': {name: {'verdict': 'PASS'}}}, edit=False)

    async def test_failed_raw_audit_never_releases_the_candidate(self):
        original = self.transport
        async def transport(*args, **kwargs):
            meta, answer = await original(*args, **kwargs)
            if kwargs['module'] == 'paper-raw-audit':
                answer['verdict'] = 'FAIL'
                answer['unresolved_fidelity_issues'] = ['Claim is stronger than supplied evidence.']
            return meta, answer
        with patch.object(paper, 'call_stage', side_effect=transport):
            result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertFalse(result['polishing_complete'])
        self.assertEqual(Path(result['best_available_tex']).name, 'unresolved.tex')
        self.assertEqual(result['stage'], 'raw-audit')

    async def test_compile_uses_portable_module_and_saved_pdf(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        mock = AsyncMock(return_value=(0, json.dumps({'pass': True, 'pdf_pages': 1}), ''))
        with patch.object(engine, 'command', mock):
            await engine.compile(engine.output, 'test')
        args = mock.call_args.args[0]
        self.assertEqual(args[:3], [sys.executable, '-m', 'paper_writing_codex.cli'])
        self.assertIn('--pdf-output', args)

    async def test_page_limit_blocks_release(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.ledger['stage'] = 'final-compile'
        with patch.object(engine, 'compile', AsyncMock(return_value={'pdf_pages': 17})):
            with self.assertRaisesRegex(ValueError, '16-page'):
                await engine.run()
        self.assertFalse(engine.ledger['polishing_complete'])

    async def test_existing_validators_reject_fake_complete_claim(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.ledger['stage'] = 'release-audit'
        engine.output.write_text(self.tex)
        with self.assertRaises(ValueError):
            await engine.run()
        self.assertFalse(engine.ledger['polishing_complete'])

    async def test_complete_pipeline_passes_real_paperctl_audit(self):
        import shutil
        if not all(shutil.which(name) for name in ('pdflatex', 'pdftoppm', 'pdfinfo')):
            self.skipTest('portable TeX/Poppler integration dependencies unavailable')
        self.tex = r"""\documentclass[11pt]{article}
\usepackage{amsmath,amsthm}
\newtheorem{theorem}{Theorem}
\begin{document}
\section{Setup}
A natural number is a nonnegative integer.
\begin{theorem}\label{thm:reflexivity}
For every natural number $n$, one has $n=n$.
\end{theorem}
\begin{proof}
Equality is reflexive, so every object equals itself. Apply this to $n$.
\end{proof}
\end{document}
"""
        base = self.transport
        async def completed_transport(*args, **kwargs):
            meta, answer = await base(*args, **kwargs)
            stage = kwargs['module'].removeprefix('paper-')
            root = self.runtime.paper_dir('P1')
            work = root / 'work'
            if stage == 'draft' and getattr(self, 'exercise_compile_repair', False):
                answer['tex'] = self.tex.replace(r'\end{document}', r'\undefinedSyntheticCommand\end{document}')
            elif stage == 'repair-freeze-shrink':
                repair_payload = Path(kwargs['document_scope']['readonly_artifacts']['stage-input']['path']).read_text()
                self.assertIn('undefinedSyntheticCommand', repair_payload)
                self.assertIn('source_sha256', repair_payload)
                self.assertIsNotNone(args[5])
                answer = {'tex': self.tex, 'artifacts': {},
                    'revision_summary': 'Removed the undefined synthetic command identified by the actual TeX compiler diagnostics.'}
            elif stage == 'visual-review':
                answer = {'verdict': 'PASS', 'unresolved_findings': [],
                    'findings': 'Synthetic layout reviewer inspected every actual rendered page attachment.',
                    'page_findings': [{'page': i + 1, 'findings': 'Synthetic page check is readable with no clipping.'}
                                      for i in range(len(kwargs['image_paths']))]}
            elif stage == 'proof-audit':
                inv = paper.inventory_tex(root / 'paper.tex')
                proof = next(u for u in inv['units'] if u['kind'] == 'proof')
                definition = next(u for u in inv['units'] if 'A natural number' in u.get('normalized_text', ''))
                findings = 'The synthetic reflexivity proof preserves the exact hypothesis and conclusion without omitted steps.'
                answer = {'proof_audit': {'verdict': 'PASS', 'unresolved_findings': [], 'findings': findings},
                    'raw_preservation': {'verdict': 'PASS', 'unresolved_fidelity_issues': [],
                        **{key: findings for key in ('hypotheses', 'proof_bridges', 'research_status', 'omissions_and_relocations')}},
                    'reader_sidecar': {'verdict': 'PASS',
                        'findings': {key: findings for key in ('sequential_read', 'proof_bridges', 'terminology')},
                        'proofs': [{'unit_id': proof['id'], 'bridges': [],
                                   'no_bridges_reason': 'Reflexivity applies directly to the quantified number, with no auxiliary inference.'}],
                        'proof_preservation': [],
                        'terminology': [{'concept': 'natural number', 'term': 'natural number', 'status': 'standard',
                            'defining_unit_id': definition['id'], 'rejected_variants': [],
                            'evidence': {**paper._ref(root / 'raw-source.tex'),
                                         'locator': 'Synthetic setup paragraph defines natural number as a nonnegative integer.'}}]},
                    'literature_audit': {'verdict': 'PASS', 'result_ids': ['reflexivity'],
                        'priority_claims_absent': True, 'unresolved_proof_dependencies': [],
                        'unresolved_attribution_issues': [], 'findings': findings,
                        'overlap_disposition': 'Elementary reflexivity has no priority claim and uses no external proof dependency.'}}
            elif stage == 'finalize-ledgers':
                from paper_writing_codex.coverage import MATHEMATICAL_KINDS
                inv = paper.inventory_tex(root / 'paper.tex')
                theorem = next(u for u in inv['units'] if u.get('label') == 'thm:reflexivity')
                answer = {'artifacts': {
                    '03-main-results.json': {'main_results': [{'result_id': 'reflexivity',
                        'candidate_label': 'thm:reflexivity', 'normalized_sha256': theorem['normalized_sha256'],
                        'hypothesis_surface': 'n is a natural number.', 'novelty_status': 'NOT_REQUESTED',
                        'priority_claim': False, 'novelty_evidence': 'No novelty claim is requested for this exam answer.',
                        'novelty_limitations': 'Elementary reflexivity is known; no novelty or priority claim is made.',
                        'literature_audit': paper._ref(work / '08-literature-audit.json')}]},
                    '04-compression-ledger.json': {'entries': [{'unit_id': u['id'], 'classification': 'CORE_INLINE'}
                        for u in inv['units'] if u['kind'] in MATHEMATICAL_KINDS]}}}
            return meta, answer
        # This integration fixture covers preserved campaigns predating the
        # mandatory discovery contract. Dedicated tests below exercise new gates.
        legacy = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        legacy.ledger.pop('literature_contract')
        legacy.ledger.pop('reference_cache')
        legacy.save()
        state = paper._json(legacy.state_path)
        state.pop('attribution_policy', None)
        state.pop('literature_search_policy', None)
        paper._write(legacy.state_path, state)
        with patch.object(paper, 'call_stage', side_effect=completed_transport):
            result = await paper.run_exam_paper(self.problem, self.snapshot, self.runtime)
        self.assertTrue(result['polishing_complete'], json.dumps(result.get('errors'), indent=2))
        self.assertTrue(result['terminal'])
        self.assertEqual(result['status'], 'polished')
        self.assertFalse(result['research_acceptance_changed'])
        work = self.runtime.paper_dir('P1') / 'work'
        self.assertTrue(paper._json(work / 'release-audit.json')['pass'])
        self.assertEqual(set(paper._json(work / 'release-audit.json')['gate_status'].values()), {'pass'})
        self.assertTrue(Path(result['best_available_pdf']).is_file())

    async def test_contextual_compile_repair_reaches_real_full_release(self):
        self.exercise_compile_repair = True
        await self.test_complete_pipeline_passes_real_paperctl_audit()
        ledger = paper._json(self.runtime.paper_dir('P1') / 'paper-ledger.json')
        self.assertEqual(len(ledger['repairs']), 1)
        self.assertEqual(ledger['repairs'][0]['failed_stage'], 'freeze-shrink')
        self.assertTrue(ledger['repairs'][0]['source_changed'])

    async def test_empty_repair_never_blindly_retries_failed_stage(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        engine.ledger.update(stage='freeze-shrink', writer_session='writer', writer_ids=['writer'])
        with patch.object(engine, 'call', AsyncMock(return_value=('writer', {}))):
            with self.assertRaisesRegex(ValueError, 'revision summary'):
                await engine.repair(ValueError('actual compiler diagnostic'))
        self.assertEqual(engine.ledger['stage'], 'freeze-shrink')
        self.assertEqual(engine.ledger['repairs'], [])

    async def test_command_timeout_reaps_child(self):
        engine = paper.PaperEngine(self.problem, self.snapshot, self.runtime)
        with self.assertRaises(asyncio.TimeoutError):
            await engine.command([sys.executable, '-c', 'import time; time.sleep(30)'], timeout=0.02)


class ImageInputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / 'rendered.png'
        self.source.write_bytes(b'\x89PNG\r\n\x1a\nsynthetic-rendered-page')
        self.dest = self.root / 'stage'
        self.dest.mkdir()

    def test_exact_image_binding_and_mutation_detection(self):
        records = _paper_image_inputs([self.source], self.dest)
        self.assertTrue(_paper_images_unchanged(records))
        self.assertEqual(Path(records[0]['path']).read_bytes(), self.source.read_bytes())
        self.source.write_bytes(b'\x89PNG\r\n\x1a\nchanged')
        self.assertFalse(_paper_images_unchanged(records))

    def test_reject_source_alias_and_symlink(self):
        with self.assertRaises(ValueError):
            _paper_image_inputs([self.source, self.source], self.dest)
        other = self.root / 'other'
        other.mkdir()
        link = self.root / 'alias.png'
        link.symlink_to(self.source)
        with self.assertRaises(ValueError):
            _paper_image_inputs([link], other)

    def test_reject_non_png(self):
        self.source.write_text('not a rendered PNG')
        with self.assertRaises(ValueError):
            _paper_image_inputs([self.source], self.dest)
