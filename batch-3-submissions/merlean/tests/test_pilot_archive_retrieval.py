"""Immutable historical reads stay separate from scientific and execution authority."""
import asyncio
import copy
import json
import os
import subprocess
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, Mock, patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p
import pilot_archive_retrieval as archive
from pilot_candidate_contract import candidate_hash, replay_main_responses
import test_pilot_checkpoint_scope_contract as fixtures


class ArchiveLookupTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.original = b'Exact original\n'
        self.saved = {'original_sha256': p.sha(self.original), 'main_session': 'original-main',
            'current': {'proof_markdown': 'Historical proof, not live replacement', 'ledger': {'rows': []}},
            'execution_history': [{'historical_stage': 'q/001-sol', 'status': 'completed',
                'output': {'text': 'Exact whitespace\n  λ → α\n', 'verdict': 'PASS', 'triaged_rows': ['old']}},
                {'historical_stage': 'q/002-sol', 'status': 'failed', 'output': {'error': 'keep failed route'}}],
            'reviewer_history': [{'stage': 'q/003-proof-review', 'answer_sha256': 'old-answer',
                'output': {'verdict': 'PASS_COMPLETE_PROOF', 'gaps': []}}],
            'findings': [], 'calls': [{'owner_key': 'PRIVATE'}], 'errors': ['operational failure']}
        self.save()
        self.request = {'response_type': 'archive_request', 'schema_version': 1,
            'checkpoint_sha256': self.ref['sha256'], 'checkpoint_pointer': '/problems/q/execution_history/0',
            'evidence_sha256': archive.digest(self.saved['execution_history'][0]), 'reason': 'Need old exact diagnostic'}

    def save(self):
        self.ref = p.write(self.root / 'continuation-checkpoint.json', {'problems': {'q': self.saved,
            'other': {**self.saved, 'original_sha256': 'different'}}})

    def retrieve(self, request=None, **kwargs):
        return archive.retrieve(self.root, kwargs.get('ref', self.ref), 'q',
            kwargs.get('original', p.sha(self.original)), kwargs.get('session', 'original-main'),
            self.request if request is None else request)

    def test_exact_full_content_unicode_and_original_historical_provenance(self):
        result = self.retrieve()
        self.assertEqual(result['content'], self.saved['execution_history'][0])
        self.assertEqual(result['entry']['encoded_bytes'], len(p.encoded(result['content']).encode()))
        self.assertEqual(result['entry']['sha256'], archive.digest(result['content']))
        self.assertIn('no_current_candidate', result['authority'])
        self.assertEqual(result, self.retrieve())
        current = dict(self.request, checkpoint_pointer='/problems/q/current',
            evidence_sha256=archive.digest(self.saved['current']))
        self.assertIn('historical', self.retrieve(current)['provenance'])

    def test_wrong_hash_original_session_checkpoint_and_schema_refused(self):
        for request in [dict(self.request, checkpoint_sha256='0'*64), dict(self.request, evidence_sha256='1'*64),
                        dict(self.request, schema_version=True), dict(self.request, path='/etc/passwd'),
                        dict(self.request, reason=''), dict(self.request, schema_version=2)]:
            with self.subTest(request=request), self.assertRaises(ValueError): self.retrieve(request)
        for kwargs in [{'original': p.sha(b'Exact original')}, {'session': 'new-main'},
                       {'ref': {'path': '../continuation-checkpoint.json', 'sha256': self.ref['sha256']}}]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError): self.retrieve(**kwargs)
        (self.root/'continuation-checkpoint.json').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'bytes changed'): self.retrieve()

    def test_only_canonical_exact_whitelisted_members_no_path_alias_or_cross_problem(self):
        for pointer in ['/problems/other/execution_history/0', '/problems/q/execution_history/-1',
                '/problems/q/execution_history/00', '/problems/q/execution_history/0/output',
                '/problems/q/execution_history/0/', '/problems/q/execution_history/../current',
                '/problems/q/%63urrent', '/problems/q/calls/0', '/problems/q/route_scout_history/0',
                'file:///etc/passwd', 'https://example.com', '/problems/q/errors/0']:
            with self.subTest(pointer=pointer), self.assertRaises(ValueError):
                self.retrieve(dict(self.request, checkpoint_pointer=pointer))

    def test_authority_fields_are_unavailable_without_filtering_or_echo(self):
        self.saved['execution_history'][0]['output']['owner_key'] = 'SECRET'
        self.save(); self.request.update(checkpoint_sha256=self.ref['sha256'],
            evidence_sha256=archive.digest(self.saved['execution_history'][0]))
        entry = next(e for e in archive.entries(self.saved,'q') if e['checkpoint_pointer']==self.request['checkpoint_pointer'])
        self.assertFalse(entry['archive_retrievable'])
        with self.assertRaises(ValueError) as caught: self.retrieve()
        self.assertNotIn('SECRET', str(caught.exception))
        self.assertEqual(self.saved['execution_history'][0]['output']['owner_key'], 'SECRET')

    def test_fixed_file_symlink_missing_and_duplicate_json_refused(self):
        fixed = self.root/'continuation-checkpoint.json'; other=self.root/'other.json'
        fixed.rename(other); fixed.symlink_to(other)
        with self.assertRaises(OSError): self.retrieve()
        fixed.unlink()
        with self.assertRaises(OSError): self.retrieve()
        raw='{"problems":{},"problems":{}}'; fixed.write_text(raw)
        self.ref['sha256']=p.sha(raw); self.request['checkpoint_sha256']=self.ref['sha256']
        with self.assertRaisesRegex(ValueError,'duplicate'): self.retrieve()

    def test_fifo_refused_without_waiting_for_writer(self):
        fixed=self.root/'continuation-checkpoint.json';fixed.unlink();os.mkfifo(fixed)
        code = ('import sys;sys.path.insert(0,' + repr(str(Path(archive.__file__).parent)) + ');'
                'import pilot_archive_retrieval as a;from pathlib import Path;'
                'a.retrieve(Path(' + repr(str(self.root)) + '),' + repr(self.ref) +
                ',"q",' + repr(p.sha(self.original)) + ',"original-main",' + repr(self.request) + ')')
        completed=subprocess.run([sys.executable,'-c',code],capture_output=True,text=True,timeout=3)
        self.assertNotEqual(completed.returncode,0);self.assertIn('regular file',completed.stderr)

    def test_hash_bound_malformed_root_mapping_is_safe_refusal(self):
        for value in [[], {'problems':[]}, {'problems':{'q':[]}}]:
            self.ref=p.write(self.root/'continuation-checkpoint.json',value)
            self.request['checkpoint_sha256']=self.ref['sha256']
            with self.assertRaises(ValueError):self.retrieve()

    def test_migration_rebinds_snapshot_but_preserves_exact_item_and_no_latest_alias(self):
        before=self.retrieve(); old_request=copy.deepcopy(self.request)
        self.saved['execution_history'].append({'new':'later result'})
        self.save()
        with self.assertRaisesRegex(ValueError,'bind this continuation'): self.retrieve(old_request)
        self.request['checkpoint_sha256']=self.ref['sha256']
        after=self.retrieve()
        self.assertEqual(before['content'],after['content']); self.assertEqual(before['entry'],after['entry'])

    def test_manifest_marks_only_existing_exact_science_items(self):
        packet = p.continuation_context(self.saved,self.ref,'q')
        self.assertEqual(packet['history_manifest']['entries'], archive.entries(self.saved,'q'))
        self.assertNotIn('/problems/q/route_scout_history/0',p.encoded(packet['history_manifest']['entries']))
        self.assertIn('archive_request v1', packet['history_manifest']['omissions'])


class ArchiveRuntimeTests(unittest.TestCase):
    def setUp(self):
        f=fixtures.MainCheckpointRuntimeTests();f.setUp();self.addCleanup(f.doCleanups)
        self.f=f; self.x=f.x; self.x.pilot.root=self.x.folder
        self.x.original_bytes=b'Original exactly\n'; self.x.statement=self.x.original_bytes.decode()
        self.x.original_sha256=p.sha(self.x.original_bytes)
        self.x.execution_history=[]; self.x.final_assessment_history=[]
        self.saved={'original_sha256':p.sha(self.x.original_bytes),'main_session':self.x.session,
            'current':copy.deepcopy(self.x.current), 'execution_history':[{'old':'complete source\n  λ',
            'verdict':'PASS_COMPLETE_PROOF','triaged_rows':['old'],'status':'completed'}]}
        self.ref=p.write(self.x.folder/'continuation-checkpoint.json',{'problems':{self.x.ident:self.saved}})
        self.x.pilot.config['continuation_checkpoint']=self.ref
        self.request={'response_type':'archive_request','schema_version':1,'checkpoint_sha256':self.ref['sha256'],
            'checkpoint_pointer':'/problems/'+self.x.ident+'/execution_history/0',
            'evidence_sha256':archive.digest(self.saved['execution_history'][0]),'reason':'Inspect exact old evidence'}
        self.responses=[];self.prompts=[]

    def calls(self, responses):
        async def call(role,prompt,**kwargs):
            self.x.counter+=1;self.prompts.append((role,prompt,kwargs));answer=copy.deepcopy(responses.pop(0))
            self.responses.append(answer)
            return self.f.f.meta(self.x.session),answer
        self.x.call=call

    def test_retrieval_same_main_no_scientific_state_mutation_before_reply_no_authority(self):
        before=copy.deepcopy(self.x.current);findings=copy.deepcopy(self.x.findings)
        key=p.assessment_key(before,self.x.execution_history);triage=copy.deepcopy(self.x.active_triage)
        async def call(role,prompt,**kwargs):
            self.x.counter+=1; self.prompts.append((role,prompt,kwargs))
            self.assertEqual(self.x.current,before);self.assertEqual(self.x.findings,findings)
            self.assertEqual(self.x.active_triage,triage);self.assertEqual(self.x.execution_history,[])
            self.assertEqual(p.assessment_key(self.x.current,self.x.execution_history),key)
            return self.f.f.meta(self.x.session),copy.deepcopy(self.request if len(self.prompts)==1 else self.f.raw)
        self.x.call=call
        asyncio.run(self.x.main_turn('Keep developing the current proof'))
        self.assertEqual(len(self.prompts),2);self.assertTrue(self.prompts[1][2]['resume'])
        self.assertIn(p.prompt_encoded(self.saved['execution_history'][0]).strip()[1:-1],self.prompts[1][1])
        self.assertEqual(self.x.current,before);self.assertEqual(self.x.findings,findings)
        self.assertFalse(self.x.last_main_checkpoint['actionable']);self.assertIsNone(self.x.active_triage)
        self.assertEqual(self.x.execution_history,[]);self.assertEqual(self.x.final_assessment_history,[])
        receipt=json.loads(next(self.x.folder.glob('archive-retrieval-*.json')).read_text())
        self.assertEqual(receipt['result']['content'],self.saved['execution_history'][0])
        self.assertEqual(receipt['delivery'],'completed_same_main');self.assertFalse(receipt['acceptance_authority'])
        replayed,_=replay_main_responses([dict(before,response_type='candidate_update'),self.request,self.f.raw])
        self.assertEqual(replayed,before)

    def test_refused_lookup_returns_reason_without_archived_private_contents(self):
        self.saved['execution_history'][0]['token']='ARCHIVE-SECRET'
        self.ref=p.write(self.x.folder/'continuation-checkpoint.json',{'problems':{self.x.ident:self.saved}})
        self.x.pilot.config['continuation_checkpoint']=self.ref
        self.request.update(checkpoint_sha256=self.ref['sha256'],evidence_sha256=archive.digest(self.saved['execution_history'][0]))
        self.calls([self.request,self.f.raw]);asyncio.run(self.x.main_turn('Keep researching'))
        self.assertIn('"status":"refused"',self.prompts[1][1]);self.assertNotIn('ARCHIVE-SECRET',self.prompts[1][1])
        self.assertEqual(self.x.execution_history,[])

    def test_second_request_gets_existing_one_correction_then_third_fails_preserving_state(self):
        before=copy.deepcopy(self.x.current);findings=copy.deepcopy(self.x.findings)
        self.calls([self.request,self.request,self.request])
        with self.assertRaises(ValueError):asyncio.run(self.x.main_turn('Develop'))
        self.assertEqual(len(self.prompts),3)
        self.assertIn('archive retrieval round already consumed',self.prompts[2][1])
        self.assertEqual(self.x.current,before);self.assertEqual(self.x.findings,findings)
        self.assertEqual(self.x.execution_history,[]);self.assertEqual(self.x.final_assessment_history,[])
        self.assertEqual(len(list(self.x.folder.glob('archive-retrieval-*.json'))),1)
        failures=[json.loads(path.read_text()) for path in self.x.folder.glob('*-invalid-contract.json')]
        self.assertTrue(any(item.get('recovery_exhausted') for item in failures))
        self.assertTrue(all(item['raw_response']==self.request for item in failures))

    def test_repeated_request_correction_can_return_honest_checkpoint(self):
        self.calls([self.request,self.request,self.f.raw])
        asyncio.run(self.x.main_turn('Develop'))
        self.assertEqual(len(self.prompts),3);self.assertFalse(self.x.last_main_checkpoint['actionable'])

    def test_complete_large_retrieval_reaches_transport_without_local_cap(self):
        large='x'*1_000_100
        self.saved['execution_history'][0]['source']=large
        self.ref=p.write(self.x.folder/'continuation-checkpoint.json',{'problems':{self.x.ident:self.saved}})
        self.x.pilot.config.update(continuation_checkpoint=self.ref,internet_browse=False,codex_binary='unused')
        self.request.update(checkpoint_sha256=self.ref['sha256'],evidence_sha256=archive.digest(self.saved['execution_history'][0]))
        self.x.pilot.remaining=lambda:600;self.x.pilot.semaphore=asyncio.Semaphore(1)
        self.x.pilot.host=self.x.folder/'host';self.x.status=Mock()
        self.x.execution_unavailability=Mock(return_value=None)
        before=copy.deepcopy(self.x.current);calls=[]
        async def call(role,prompt,**kwargs):
            calls.append(role)
            if len(calls)==1:
                self.x.counter+=1;return self.f.f.meta(self.x.session),copy.deepcopy(self.request)
            return await self.x._call_once(role,prompt,model=p.ASTRA,resume=True,timeout=600)
        self.x.call=call
        with patch.object(p,'call_stage',new=AsyncMock(side_effect=OSError('actual provider failure'))) as dispatch:
            with self.assertRaisesRegex(OSError,'actual provider failure'):
                asyncio.run(self.x.main_turn('Develop'))
            dispatch.assert_awaited_once()
            self.assertIn(large,dispatch.call_args.args[2])
        self.assertEqual(self.x.current,before)
        receipt=json.loads(next(self.x.folder.glob('archive-retrieval-*.json')).read_text())
        self.assertEqual(receipt['result']['content']['source'],large)
        self.assertEqual(receipt['delivery'],'not_completed')
        self.assertFalse(hasattr(p,'MAX_PROMPT_BYTES'))

    def test_operational_receipt_copy_does_not_make_replay_authority(self):
        self.calls([self.request,self.f.raw]);asyncio.run(self.x.main_turn('Develop'))
        with tempfile.TemporaryDirectory() as directory:
            copied=Path(directory)/'problem';shutil.copytree(self.x.folder,copied)
            original=next(self.x.folder.glob('archive-retrieval-*.json'))
            self.assertEqual(original.read_bytes(),(copied/original.name).read_bytes())
        current,_=replay_main_responses([dict(self.x.current,response_type='candidate_update'),self.request])
        self.assertEqual(current,self.x.current)


if __name__=='__main__':unittest.main()


class ContinuationPhaseTests(unittest.TestCase):
    def test_preserves_parent_named_phase_and_prior_phase_behavior(self):
        self.assertEqual(p.continuation_phase('p7-phase1'),'p7-phase1')
        self.assertEqual(p.continuation_phase('p7-phase1','p7-phase1'),'p7-phase1')
        self.assertEqual(p.continuation_phase('phase1','phase2'),'phase2')
        self.assertEqual(p.continuation_phase('phase1'),'phase1')

    def test_cannot_introduce_or_rename_named_phase_or_accept_unsafe_labels(self):
        for old,requested in [('phase1','p7-phase1'),('p7-phase1','p8-phase1'),('p7-phase1','p7-phase2'),
                ('p7-phase1','p7-phase1 '),('p7-phase1','../p7-phase1'),('phase1',True),
                (True,None),('p0-phase1',None),('p7-phase0',None),('other',None)]:
            with self.subTest(old=old,requested=requested),self.assertRaises(ValueError):
                p.continuation_phase(old,requested)
