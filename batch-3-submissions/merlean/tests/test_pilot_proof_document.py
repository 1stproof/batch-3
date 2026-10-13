"""Atomic authored drafts, explicit submissions and immutable downstream bindings."""
import asyncio
import concurrent.futures
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import pilot_proof_document as d
import codex_pilot as p
from pilot_candidate_contract import apply_main_response


class ProofDocumentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.identity = dict(problem_id='p', original_sha256='a'*64, main_session='main')
        self.producer = dict(stage='p/001-main', request_id='request', session_id='main')
        self.candidate = dict(proof_markdown='## Proof\nUnfinished; gap G remains.\n', ledger={'rows':[]}, sol_tasks=[],python_probe='',lean_probe='',lean_probe_rows=[])
        self.first = d.submit(self.root, **self.identity, expected_revision=None, candidate=self.candidate, producer=self.producer)

    def save(self, text, revision=None):
        return d.save_draft(self.root, **self.identity, expected_revision=revision or self.first['revision'], proof_markdown=text, producer=self.producer)

    def test_save_is_draft_and_submission_preserves_exact_text_and_sidecar(self):
        draft = self.save('New full proof — gap G remains.\n')
        self.assertEqual(d.read_submission(self.root, **self.identity)['candidate'], self.candidate)
        with self.assertRaisesRegex(d.ProofRevisionConflict, 'exact current'):
            d.submit(self.root, **self.identity, expected_revision=draft['revision'], candidate=self.candidate, producer=self.producer)
        changed = dict(self.candidate, proof_markdown=draft['proof_markdown'])
        submitted = d.submit(self.root, **self.identity, expected_revision=draft['revision'], candidate=changed, producer=self.producer)
        self.assertEqual(submitted['status'], 'submitted')
        old = d.read_revision(self.root, {k:self.first[k] for k in ('revision','manifest_sha256')}, **self.identity)
        self.assertEqual(old['candidate'], self.candidate)
        self.assertEqual((self.root/'proof.md').read_text(), changed['proof_markdown'])

    def test_concurrent_saves_have_exactly_one_winner(self):
        def attempt(text):
            try:return self.save(text)['revision']
            except d.ProofRevisionConflict:return None
        with concurrent.futures.ThreadPoolExecutor(2) as pool:
            outcomes=list(pool.map(attempt, ['draft one', 'draft two']))
        self.assertEqual(sum(x is not None for x in outcomes), 1)
        current=d.read_current(self.root, **self.identity)
        with self.assertRaises(d.ProofRevisionConflict):self.save('stale')
        self.assertEqual(self.save(current['proof_markdown'],current['revision'])['revision'], current['revision'])

    def test_failure_before_pointer_leaves_previous_authority(self):
        original=d._atomic
        def failing(path,data):
            if path.name=='proof-current.json':raise OSError('before publish')
            return original(path,data)
        with patch.object(d,'_atomic',side_effect=failing), self.assertRaises(OSError):self.save('orphan preserved')
        self.assertEqual(d.read_current(self.root, **self.identity)['revision'],self.first['revision'])
        self.assertEqual(len(list((self.root/'proof-revisions').iterdir())),2)

    def test_failure_after_pointer_is_committed_and_retry_idempotent(self):
        original=d._atomic
        def failing(path,data):
            if path.name=='proof.md':raise OSError('view unavailable')
            return original(path,data)
        with patch.object(d,'_atomic',side_effect=failing):saved=self.save('saved despite failed view')
        self.assertEqual(saved['view_status'],'repair_required')
        self.assertEqual(d.read_current(self.root, **self.identity)['revision'], saved['revision'])
        repaired=self.save(saved['proof_markdown'],saved['revision'])
        self.assertEqual(repaired['revision'],saved['revision']);self.assertEqual(repaired['view_status'],'current')

    def test_postrename_fsync_failure_recovers_published_revision(self):
        original=d._atomic
        def failing(path,data):
            original(path,data)
            if path.name=='proof-current.json':raise OSError('after rename')
        with patch.object(d,'_atomic',side_effect=failing):saved=self.save('published')
        self.assertIn('publication_warning',saved)
        self.assertEqual(d.read_current(self.root, **self.identity)['revision'], saved['revision'])

    def test_tamper_wrong_identity_and_draft_paper_handoff_rejected(self):
        draft=self.save('incomplete')
        ref={k:draft[k] for k in ('revision','manifest_sha256')}
        with self.assertRaisesRegex(ValueError,'submitted'):d.paper_handoff(self.root,ref,**self.identity,acceptance={})
        ref={k:self.first[k] for k in ('revision','manifest_sha256')}
        with self.assertRaisesRegex(ValueError,'acceptance'):d.paper_handoff(self.root,ref,**self.identity,acceptance={'successful_complete':True})
        state=dict(status='complete',successful_complete=True,answer_sha256=self.first['proof_sha256'],manifest='accepted.json',sha256='b'*64)
        handoff=d.paper_handoff(self.root,ref,**self.identity,acceptance=state)
        self.assertEqual(handoff['proof']['sha256'],self.first['proof_sha256'])
        Path(self.first['proof_path']).write_text('tampered')
        with self.assertRaisesRegex(ValueError,'content changed'):d.read_revision(self.root,ref,**self.identity)

    def test_markdown_handoff_is_existing_paper_evidence_not_a_tex_freeze(self):
        from test_paper_raw import evidence_fixture
        from paper_writing_codex.raw import _evidence
        raw=self.root/'paper-raw.tex';raw.write_text(r'\documentclass{article}\begin{document}Synthetic reconstruction.\end{document}')
        evidence=evidence_fixture(self.root/'paper-state.json',raw)
        ref={k:self.first[k] for k in ('revision','manifest_sha256')}
        acceptance=dict(status='complete',successful_complete=True,answer_sha256=self.first['proof_sha256'],manifest='accepted.json',sha256='b'*64)
        handoff=d.paper_handoff(self.root,ref,**self.identity,acceptance=acceptance)
        record=json.loads(evidence.read_text())
        record['source_records']=[dict(handoff['proof'],kind='natural-language',findings='Synthetic bridge preserves the authored source and its explicit gaps.')]
        evidence.write_text(json.dumps(record))
        _,dependencies=_evidence({},raw,evidence)
        self.assertIn(Path(handoff['proof']['path']),dependencies)
        with self.assertRaisesRegex(ValueError,'acceptance'):
            d.paper_handoff(self.root,ref,**self.identity,acceptance=dict(acceptance,answer_sha256='c'*64))
        Path(handoff['proof']['path']).write_text('changed after binding')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):_evidence({},raw,evidence)

    def test_pilot_stale_final_and_draft_only_noaction(self):
        x=p.Problem.__new__(p.Problem);x.pilot=type('Pilot',(),{'config':{'proof_document_version':1}})()
        x.folder=self.root;x.ident='p';x.session='main';x.original_bytes=b'original'
        x.document_identity=lambda:self.identity;x.current=copy.deepcopy(self.candidate)
        saved=self.save('new draft')
        raw=dict(response_type='candidate_update',**self.candidate)
        effective, checkpoint=apply_main_response(raw,{})
        with self.assertRaisesRegex(ValueError,'explicitly bind'):x.validate_document_response(raw,effective,checkpoint)
        raw.update(proof_revision=saved['revision'],proof_markdown=saved['proof_markdown'])
        effective,checkpoint=apply_main_response(raw,{})
        x.validate_document_response(raw,effective,checkpoint)
        self.assertNotIn('proof_revision',effective)
        self.candidate['sol_tasks']=[{'task':'already completed historical proposal'}]
        x.current=copy.deepcopy(self.candidate)
        raw={'response_type':'draft_checkpoint','proof_revision':saved['revision'],'reason':'Continue working on saved draft.'}
        effective,checkpoint=x.apply_authored_response(raw,{})
        self.assertEqual(effective,x.current)
        self.assertTrue(checkpoint['operational_draft_checkpoint'])
        self.assertFalse(checkpoint['actionable'])
        self.assertEqual(d.read_current(self.root,**self.identity)['revision'],saved['revision'])
        with self.assertRaisesRegex(ValueError,'exactly'):
            x.apply_authored_response(dict(raw,unreviewed_findings=[{'id':'new'}]),{})
        with self.assertRaisesRegex(ValueError,'stale'):
            x.apply_authored_response(dict(raw,proof_revision=self.first['revision']),{})

    def test_delivery_is_not_inferred_from_favorable_review(self):
        x=p.Problem.__new__(p.Problem);x.pilot=type('Pilot',(),{'config':{'proof_document_version':1}})()
        review={'verdict':'PASS_COMPLETE_PROOF','relied_on_artifact_ids':['e'],'needed_artifact_ids':[]}
        meta={'document_audit':{'status':'PASS','required_material_delivered':True,'artifact_coverage':{'e':False}}}
        with self.assertRaisesRegex(ValueError,'complete verified'):x.check_review_delivery(meta,review)
        meta['document_audit']['artifact_coverage']['e']=True;x.check_review_delivery(meta,review)
        review['needed_artifact_ids']=['unknown-required']
        with self.assertRaisesRegex(ValueError,'blocks'):x.check_review_delivery(meta,review)
        review['verdict']='INCOMPLETE';x.check_review_delivery(meta,review)


class ProofPilotIntegrationTests(unittest.TestCase):
    def setUp(self):
        import test_pilot_final_progression as fixtures
        self.f=fixtures.FinalProgressionTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        self.x=x=self.f.x;x.ident='q';x.original_bytes=x.statement.encode()
        x.pilot.config['proof_document_version']=1;x.packet=lambda:{'feedback':[]}
        x.publish_document(x.current,self.f.meta('001-main'))

    def test_save_only_main_turn_never_submits_old_tasks_over_draft(self):
        x=self.x
        x.current['sol_tasks']=[{'task':'old task'}]
        x.publish_document(x.current,self.f.meta('002-main'))
        saved=d.save_draft(x.folder,**x.document_identity(),expected_revision=x.document_current()['revision'],
            proof_markdown='Draft with explicit gap',producer={'stage':'q/003-main','request_id':'req','session_id':'main'})
        before=p.encoded(x.current);calls=[]
        async def call(role,instruction,**kwargs):
            calls.append(role);x.counter+=1
            return self.f.meta('003-main'),dict(response_type='draft_checkpoint',proof_revision=saved['revision'],reason='Continue draft')
        x.call=call
        asyncio.run(x.main_turn('Continue'))
        self.assertEqual(calls,['main-repair']);self.assertEqual(p.encoded(x.current),before)
        self.assertEqual(x.document_current()['revision'],saved['revision'])
        self.assertEqual(x.document_submission()['candidate'],x.current)
        self.assertFalse(x.last_main_checkpoint['actionable'])
        self.assertTrue(list(x.folder.glob('*-draft-checkpoint.json')))

    def test_stale_final_body_receives_only_existing_correction_and_keeps_draft(self):
        x=self.x;saved=d.save_draft(x.folder,**x.document_identity(),expected_revision=x.document_current()['revision'],
            proof_markdown='New draft',producer={'stage':'q/002-main','request_id':'req','session_id':'main'})
        before=p.encoded(x.current);prompts=[]
        raw=dict(x.current,response_type='candidate_update')
        async def call(role,instruction,**kwargs):
            prompts.append(instruction);x.counter+=1
            return self.f.meta(str(x.counter)+'-main'),copy.deepcopy(raw)
        x.call=call
        with self.assertRaisesRegex(ValueError,'explicitly bind'):asyncio.run(x.main_turn('Continue'))
        self.assertEqual(len(prompts),2);self.assertIn(p.encoded(raw),prompts[1])
        self.assertEqual(p.encoded(x.current),before);self.assertEqual(x.document_current()['revision'],saved['revision'])
        failures=[json.loads(v.read_text()) for v in x.folder.glob('*invalid-contract.json')]
        self.assertEqual(len(failures),2);self.assertTrue(any(v.get('recovery_exhausted') for v in failures))

    def test_plain_packet_and_exact_execution_archive_with_no_hash_only_pass(self):
        x=self.x;x.execution_history=[{'status':'failed','output':{'diagnostic':'complete exact diagnostic'}}]
        packet={'exact_candidate':x.current,'exact_dossier':x.current,'prior_findings':[self.f.finding()],
                'actual_execution_evidence':x.execution_history,'finding_history':[]}
        text,scope=x.review_context(packet)
        self.assertIn('SUBMITTED PROOF — COMPLETE EXACT MARKDOWN',text)
        self.assertEqual(text.count('Exact candidate'),1)
        self.assertEqual(scope['required_artifact_ids'],['actual_execution_evidence'])
        ref=scope['readonly_artifacts']['actual_execution_evidence']
        self.assertEqual(Path(ref['path']).read_text(),p.encoded(x.execution_history))
        self.assertEqual(p.sha(Path(ref['path']).read_bytes()),ref['sha256'])



class ProofMigrationTests(unittest.TestCase):
    def setUp(self):
        import test_pilot_continuation as fixtures
        self.f=fixtures.ContinuationTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        path=self.f.source/'host-config.json';config=json.loads(path.read_text());config['proof_document_version']=1;self.f.write(path,config)
        self.identity=dict(problem_id='problem',original_sha256=p.sha((self.f.folder/'input.txt').read_bytes()),main_session='main-session')
        self.candidate=json.loads((self.f.folder/'current-candidate.json').read_text())
        call=self.f.calls[0]
        self.submitted=d.submit(self.f.folder,**self.identity,expected_revision=None,candidate=self.candidate,
            producer={'stage':call['name'],'request_id':call['request_id'],'session_id':'main-session'})

    def test_canonical_submission_restores_despite_stale_derived_view(self):
        (self.f.folder/'current-candidate.json').write_text(p.encoded(dict(self.candidate,proof_markdown='stale derived view')))
        restored=self.f.load()['problems']['problem']
        self.assertEqual(restored['current'],self.candidate)
        self.assertEqual(restored['proof_document']['revision'],self.submitted['revision'])

    def test_acknowledged_draft_survives_timeout_but_missing_receipt_blocks_without_deletion(self):
        call=self.f.calls[3]
        producer={'stage':call['name'],'request_id':call['request_id'],'session_id':'main-session'}
        draft=d.save_draft(self.f.folder,**self.identity,expected_revision=self.submitted['revision'],proof_markdown='Preserved incomplete work',producer=producer)
        with self.assertRaisesRegex(ValueError,'durable save acknowledgment'):self.f.load()
        self.assertEqual(d.read_current(self.f.folder,**self.identity)['revision'],draft['revision'])
        receipt={'tool':'save_proof_revision','is_error':False,'producer':producer,'session_id':'main-session',
                 'saved_revision':{k:draft[k] for k in ('revision','manifest_sha256','proof_sha256','status')}}
        (self.f.source/'host/runtime'/call['name']/'document-operations.jsonl').write_text(json.dumps(receipt)+'\n')
        restored=self.f.load()['problems']['problem']
        self.assertEqual(restored['current'],self.candidate)
        self.assertEqual(restored['proof_document']['revision'],draft['revision'])
        self.assertEqual(restored['calls'][-1]['status'],'timeout_censored')

    def test_missing_canonical_pointer_never_adopts_legacy_mirror(self):
        pointer=self.f.folder/'proof-current.json'
        original=pointer.read_bytes();pointer.unlink()
        with self.assertRaisesRegex(ValueError,'missing canonical proof pointer'):self.f.load()
        self.assertTrue((self.f.folder/'proof-revisions'/self.submitted['revision']/'manifest.json').is_file())
        pointer.write_bytes(original)
        self.assertEqual(self.f.load()['problems']['problem']['current'],self.candidate)

    def test_published_checkpoint_recovers_unrecorded_findings_without_reopening_archived_versions(self):
        from pilot_candidate_contract import candidate_hash
        finding={'id':'new-obligation','severity':'gap','kind':'mathematical','finding':'Exact new unresolved obligation'}
        raw={'response_type':'blocked_checkpoint','selected_candidate_sha256':candidate_hash(self.candidate),
             'checkpoint_metadata':{'reason':'Preserve complete artifact and new gap'},
             'proposed_work':{'sol_tasks':[],'python_probe':'','lean_probe':'','lean_probe_rows':[]},
             'unreviewed_findings':[finding],'review_request':'none'}
        effective,_=apply_main_response(raw,{candidate_hash(self.candidate):self.candidate})
        call=self.f.calls[3];call.update(status='completed',answer_sha256=p.sha(p.encoded(raw)))
        stage=self.f.source/'host/runtime'/call['name']
        (stage/'stage.answer.txt').write_text(p.encoded(raw));self.f.write(stage/'stage.meta.json',call)
        self.f.write(self.f.folder/(call['name'].split('/')[-1]+'.json'),raw)
        d.submit(self.f.folder,**self.identity,expected_revision=self.submitted['revision'],candidate=effective,
                 producer={'stage':call['name'],'request_id':call['request_id'],'session_id':'main-session'})
        # Exact publication occurred, but old derived progress still lacks its obligations.
        restored=self.f.load()['problems']['problem']
        self.assertEqual(restored['current'],effective)
        self.assertEqual(restored['findings'],[{'id':'open-finding'},finding])
        version={'sha256':p.sha(p.encoded(finding)),'finding':finding}
        self.assertIn(version,restored['finding_history'])
        # A subsequent review archived this exact version; restoration must not reopen it.
        progress_path=self.f.folder/'host-progress.json';progress=json.loads(progress_path.read_text())
        progress['finding_history']=[version];self.f.write(progress_path,progress)
        restored=self.f.load()['problems']['problem']
        self.assertEqual(restored['findings'],[{'id':'open-finding'}])
        self.assertEqual(restored['finding_history'],[version])

    def test_wrong_producer_cannot_claim_another_verified_main_artifact(self):
        # Host creation API is not review authority; continuation independently checks producer receipts.
        d.submit(self.f.folder,**self.identity,expected_revision=self.submitted['revision'],
            candidate=dict(self.candidate,proof_markdown='different'),
            producer={'stage':self.f.calls[0]['name'],'request_id':'wrong','session_id':'main-session'})
        with self.assertRaisesRegex(ValueError,'provenance'):self.f.load()



if __name__=='__main__':unittest.main()
