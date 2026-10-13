import asyncio
import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as pilot
import codex_transport as transport
from codex_transport import _tool_output_part
import pilot_document_tools as tools
import pilot_document_recovery as recovery


class DocumentRecoveryTests(unittest.TestCase):
    def setUp(self): self.temps = []
    def tearDown(self):
        for temp in self.temps: temp.cleanup()

    def build(self, partial=False, chunked=False, page_read=False):
        temp=tempfile.TemporaryDirectory();self.temps.append(temp);root=Path(temp.name).resolve()
        previous=root/'runtime/p/001-proof-review';previous.mkdir(parents=True)
        current=root/'runtime/p/002-proof-review';current.mkdir()
        artifact=root/'evidence.txt';artifact.write_text('Exact Unicode 漢字\nUnresolved evidence.\n')
        spec={'schema_version':1,'mode':'review','problem_id':'p','original_sha256':'a'*64,
              'main_session':'original-main','store_root':str(root),
              'readonly_artifacts':{'e1':{'path':str(artifact),'sha256':tools.digest(artifact.read_bytes()),'media_type':'text/plain'}},
              'required_artifact_ids':['e1'],'inline_artifact_ids':[]}
        if chunked:
            text = artifact.read_text()
            for start, end in [(0, 5), (5, len(text))]:
                path = root / f'chunk-{start}.txt'
                path.write_text(text[start:end])
                spec['readonly_artifacts'][f'e1::chunk:{start}:{end}'] = {
                    'path': str(path), 'sha256': tools.digest(path.read_bytes()), 'media_type': 'text/plain'}
        session='00000000-0000-0000-0000-000000000001'
        scope,cap=tools.prepare_scope(spec,previous,{'stage':'p/001-proof-review','request_id':'prior-request','session_id':None})
        server=tools.DocumentTools(scope);args={'artifact_id':'e1','sha256':spec['readonly_artifacts']['e1']['sha256']}
        if chunked:
            args = {'artifact_id': 'e1::chunk:0:5',
                    'sha256': spec['readonly_artifacts']['e1::chunk:0:5']['sha256']}
        if partial:args.update(start=0,end=5)
        tool = 'read_required_evidence' if page_read else 'read_artifact'
        if page_read: args = {'page': 0}
        response=server.call(tool,args,1,{'callId':'read1','sessionId':session})
        event={'type':'item.completed','item':{'type':'mcp_tool_call','server':tools.SERVER,'tool':tool,
               'arguments':args,'result':{'content':response['content'],'structured_content':None},'error':None,'status':'completed'}}
        saved={'status':'verified','tool_events':[{'namespace':tools.NAMESPACE,'name':tool,'call_id':'read1',
               'arguments_canonical_sha256':tools.digest(tools.encoded(args).encode())}],
               'tool_output_receipts':[{'call_id':'read1','output_format':'list','text_parts':[
                   {**_tool_output_part(text),'type':'input_text','keys':['text','type']}
                   for text in ['Wall time: 0.01 seconds\nOutput:',response['content'][0]['text']]]}]}
        (previous/'stage.events.jsonl').write_text(json.dumps({'event':event})+'\n')
        audit=tools.audit_operations(scope,[event],saved['tool_events'],session,saved['tool_output_receipts'])
        prompt='Exact review task\n'+tools.invocation_guidance('review')
        (previous/'stage.prompt.txt').write_text(prompt)
        meta={'name':'p/001-proof-review','module':'proof-review','status':'timeout_censored','session_id':session,
              'resume_session':None,'request_id':'prior-request','model_requested':'gpt-6-astra','model_actual':'gpt-6-astra',
              'model_verified':True,'internet_browse':False,'tool_event_count':0,'tool_events':[],
              'persisted_tool_event_count':0,'persisted_tool_events':[],'document_capability':cap,
              'prompt_sha256':tools.digest(prompt.encode()),'prompt_bytes':len(prompt.encode()),
              'persisted_rollout_audit':saved,'document_events':[event],'document_audit':audit}
        (previous/'stage.meta.json').write_text(json.dumps(meta,sort_keys=True))
        current_scope,_=tools.prepare_scope(spec,current,{'stage':'p/002-proof-review','request_id':'next-request','session_id':session})
        kwargs={'name':'p/002-proof-review','module':'proof-review','model':'gpt-6-astra','resume_session':session,
                'prompt':'Exact review task'+recovery.TIMEOUT_RECOVERY_GUIDANCE+'\n'+tools.invocation_guidance('review'),
                'scope':current_scope}
        return root,previous,meta,kwargs

    def verify(self, fixture):
        root,previous,meta,kwargs=fixture
        reference=recovery.recovery_reference(root,meta)
        return recovery.verify_recovery(root,reference,**kwargs)

    def rewrite(self, fixture):
        _,previous,meta,_=fixture;(previous/'stage.meta.json').write_text(json.dumps(meta,sort_keys=True))

    def test_full_prior_delivery_survives_no_read_recovery_without_acceptance(self):
        fixture=self.build();root,_,_,kwargs=fixture;verified=self.verify(fixture)
        current=tools.audit_operations(kwargs['scope'],[],[],kwargs['resume_session'],[])
        self.assertFalse(current['required_material_delivered'])
        inherited=recovery.inherit_coverage(current,verified,scope=kwargs['scope'],actual_session=kwargs['resume_session'])
        self.assertTrue(inherited['required_material_delivered']);self.assertFalse(inherited['current_attempt_artifact_coverage']['e1'])
        self.assertEqual(inherited['receipt_count'],0);self.assertEqual(verified['full_artifact_ids'],['e1'])
        problem=pilot.Problem.__new__(pilot.Problem);problem.documents_enabled=lambda:True
        with self.assertRaisesRegex(ValueError,'needed missing evidence'):
            problem.check_review_delivery({'document_audit':inherited},{'verdict':'PASS_COMPLETE_PROOF',
                'relied_on_artifact_ids':['e1'],'needed_artifact_ids':['unresolved-required-material']})

    def test_page_receipts_and_missing_guidance_are_independently_authenticated(self):
        fixture = self.build(chunked=True, page_read=True)
        kwargs = fixture[3]
        guidance = recovery.recovery_delivery_guidance(kwargs['scope'], fixture[2]['document_audit'])
        suffix = '\n' + tools.invocation_guidance('review')
        kwargs['prompt'] = kwargs['prompt'][:-len(suffix)] + guidance + suffix
        verified = self.verify(fixture)
        self.assertIn('e1', verified['full_artifact_ids'])
        self.assertIn('"missing_pages":[]', guidance)
        kwargs['prompt'] = kwargs['prompt'].replace('"missing_pages":[]', '"missing_pages":[0]')
        with self.assertRaisesRegex(ValueError, 'exact same logical prompt'):
            self.verify(fixture)

    def test_partial_read_never_combines_or_becomes_full(self):
        fixture=self.build(partial=True);verified=self.verify(fixture);kwargs=fixture[3]
        self.assertEqual(verified['full_artifact_ids'],[])
        current=tools.audit_operations(kwargs['scope'],[],[],kwargs['resume_session'],[])
        inherited=recovery.inherit_coverage(current,verified,scope=kwargs['scope'],actual_session=kwargs['resume_session'])
        self.assertFalse(inherited['required_material_delivered'])

    def test_complete_verified_chunks_resume_same_review_and_cover_exact_parent(self):
        fixture = self.build(chunked=True)
        verified = self.verify(fixture)
        kwargs = fixture[3]
        self.assertEqual(verified['full_artifact_ids'], ['e1::chunk:0:5'])
        scope = kwargs['scope']
        second = next(k for k in scope['readonly_artifacts'] if k.startswith('e1::chunk:5:'))
        args = {'artifact_id': second, 'sha256': scope['readonly_artifacts'][second]['sha256']}
        result = tools.DocumentTools(scope).call('read_artifact', args, 1,
            {'callId': 'second-chunk', 'sessionId': kwargs['resume_session']})
        event = {'type': 'item.completed', 'item': {'tool': 'read_artifact', 'arguments': args,
                 'result': {'content': result['content'], 'structured_content': None},
                 'error': None, 'status': 'completed'}}
        calls = [{'namespace': tools.NAMESPACE, 'name': 'read_artifact', 'call_id': 'second-chunk',
                  'arguments_canonical_sha256': tools.digest(tools.encoded(args).encode())}]
        outputs = [{'call_id': 'second-chunk', 'output_format': 'list', 'text_parts': [
            {**_tool_output_part(text), 'type': 'input_text', 'keys': ['text', 'type']}
            for text in ['Wall time: 0.01 seconds\nOutput:', result['content'][0]['text']]]}]
        current = tools.audit_operations(scope, [event], calls, kwargs['resume_session'], outputs)
        self.assertFalse(current['required_material_delivered'])
        inherited = recovery.inherit_coverage(current, verified, scope=scope,
                                               actual_session=kwargs['resume_session'])
        self.assertTrue(inherited['required_material_delivered'])
        self.assertFalse(inherited['current_attempt_artifact_coverage']['e1'])
        self.assertEqual(inherited['receipt_count'], 1)
        with self.assertRaises(ValueError):
            recovery.inherit_coverage(current, verified, scope=scope, actual_session='different-reviewer')

    def test_changed_chunk_is_not_a_complete_parent_receipt(self):
        fixture = self.build(chunked=True)
        (fixture[0] / 'chunk-0.txt').write_text('forged')
        with self.assertRaises(ValueError):
            self.verify(fixture)

    def test_current_failure_or_different_actual_session_cannot_inherit(self):
        fixture=self.build();verified=self.verify(fixture);kwargs=fixture[3];failed={'status':'FAIL'}
        self.assertIs(recovery.inherit_coverage(failed,verified,scope=kwargs['scope'],actual_session=kwargs['resume_session']),failed)
        with self.assertRaises(ValueError):recovery.inherit_coverage({'status':'PASS'},verified,scope=kwargs['scope'],actual_session='fresh')

    def test_wrong_session_model_role_prompt_scope_or_required_sets_rejected(self):
        changes=[('resume_session',None),('resume_session','fresh'),('model','gpt-6-sol'),('module','scope-review'),
                 ('name','other/002-proof-review'),('prompt','other task')]
        for key,value in changes:
            with self.subTest(key=key,value=value):
                fixture=self.build();fixture[3][key]=value
                with self.assertRaises(ValueError):self.verify(fixture)
        for key,value in [('original_sha256','b'*64),('main_session','other'),('required_artifact_ids',[]),
                          ('inline_artifact_ids',['e1']),('mode','main')]:
            with self.subTest(scope=key):
                fixture=self.build();fixture[3]['scope'][key]=value
                with self.assertRaises(ValueError):self.verify(fixture)

    def test_changed_artifact_receipt_capability_and_prompt_are_refused(self):
        for target in ['evidence.txt','document-operations.jsonl','document-capability.json','stage.prompt.txt']:
            with self.subTest(target=target):
                fixture=self.build();root,previous,_,_=fixture
                path=root/target if target=='evidence.txt' else previous/target
                path.write_text(path.read_text()+' ')
                with self.assertRaises((ValueError,KeyError)):self.verify(fixture)

    def test_metadata_hash_and_forged_or_ineligible_prior_audits_refused(self):
        fixture=self.build();reference=recovery.recovery_reference(fixture[0],fixture[2]);self.rewrite(fixture)
        (fixture[1]/'stage.meta.json').write_text((fixture[1]/'stage.meta.json').read_text()+' ')
        with self.assertRaises(ValueError):recovery.verify_recovery(fixture[0],reference,**fixture[3])
        changes=[('status','completed'),('status','invalid_tool_attempt'),('model_verified',False),
                 ('document_recovery',{'prior':'chain'}),('tool_event_count',1),('persisted_tool_event_count',1)]
        for key,value in changes:
            with self.subTest(key=key,value=value):
                fixture=self.build();fixture[2][key]=value;self.rewrite(fixture)
                with self.assertRaises(ValueError):self.verify(fixture)
        for mutation in ['forbidden','raw_forbidden','missing_outputs','forged_coverage','output_changed']:
            with self.subTest(mutation=mutation):
                fixture=self.build();meta=fixture[2]
                if mutation=='forbidden':meta['persisted_rollout_audit']['tool_events'].append({'namespace':'functions','name':'exec'})
                if mutation=='raw_forbidden':
                    with (fixture[1]/'stage.events.jsonl').open('a') as stream:stream.write(json.dumps({'event':{'type':'item.completed','item':{'type':'command_execution','command':'forbidden'}}})+'\n')
                if mutation=='missing_outputs':del meta['persisted_rollout_audit']['tool_output_receipts']
                if mutation=='forged_coverage':meta['document_audit']['artifact_coverage']['e1']=False
                if mutation=='output_changed':meta['persisted_rollout_audit']['tool_output_receipts'][0]['text_parts'][1]['sha256']='c'*64
                self.rewrite(fixture)
                with self.assertRaises(ValueError):self.verify(fixture)

    def test_actual_transport_merges_verified_prior_delivery_and_keeps_raw_stage(self):
        fixture=self.build();root,previous,meta,kwargs=fixture
        before={str(p):p.read_bytes() for p in previous.iterdir() if p.is_file()}
        reference=recovery.recovery_reference(root,meta)
        scope={k:v for k,v in kwargs['scope'].items() if k not in ('producer','receipt_path')}
        final={'verdict':'INCOMPLETE','relied_on_artifact_ids':['e1'],'needed_artifact_ids':[]}
        events=[{'type':'thread.started','thread_id':kwargs['resume_session']},
                {'type':'item.completed','item':{'type':'agent_message','text':json.dumps(final)}},
                {'type':'turn.completed','usage':{}}]
        program=root/'fake.py';program.write_text('import sys\nsys.stdin.read()\n'+'\n'.join('print('+repr(json.dumps(e))+', flush=True)' for e in events))
        saved={'status':'verified','tool_events':[],'tool_output_receipts':[], 'turn_contexts':[{'model':'gpt-6-astra'}]}
        with patch('pilot_document_startup.startup_preflight',return_value={'status':'PASS'}), patch.object(transport,'subscription_preflight',return_value={'authentication':'chatgpt','cli_version':'codex-cli 0.157.1'}), patch.object(transport,'_document_model_catalog',return_value={'model':'gpt-6-astra'}), patch.object(transport,'_command',return_value=[sys.executable,str(program)]), patch.object(transport,'_persisted_tool_audit',return_value=saved):
            actual,answer=asyncio.run(transport.call_stage(root,'p/003-proof-review',
                'Exact review task'+recovery.TIMEOUT_RECOVERY_GUIDANCE,'gpt-6-astra',5,
                resume_session=kwargs['resume_session'],internet_browse=False,module='proof-review',
                document_scope=scope,document_recovery_from=reference))
        self.assertEqual(actual['status'],'completed');self.assertEqual(answer,final)
        self.assertTrue(actual['document_audit']['required_material_delivered'])
        self.assertFalse(actual['document_audit']['current_attempt_artifact_coverage']['e1'])
        self.assertEqual(actual['document_audit']['receipt_count'],0)
        self.assertEqual(actual['document_recovery']['source'],reference)
        for path,data in before.items():self.assertEqual(Path(path).read_bytes(),data)
        problem=pilot.Problem.__new__(pilot.Problem);problem.documents_enabled=lambda:True
        problem.check_review_delivery(actual,answer)

    def test_existing_timeout_loop_forwards_once_and_fresh_call_forgets(self):
        fixture=self.build();root,_,meta,kwargs=fixture;problem=pilot.Problem.__new__(pilot.Problem)
        problem.pilot=SimpleNamespace(host=root,drain=SimpleNamespace(check=lambda:None),remaining=lambda:1000,policy=lambda _: '')
        problem.errors=[];problem.consecutive_failures=0;problem.status=Mock();seen=[]
        async def stage(*args,**options):
            seen.append((args,options))
            if len(seen)==1:raise pilot.StageFailure(meta,[])
            return {'status':'completed'},{'checkpoint':'synthetic'}
        problem._call_once=stage
        async def run():
            await problem.call('proof-review','Exact task',document_scope=kwargs['scope'])
            await problem.call('proof-review','Fresh task',document_scope=kwargs['scope'])
        asyncio.run(run())
        self.assertIsNone(seen[0][1]['document_recovery_from'])
        self.assertEqual(seen[1][1]['document_recovery_from'],recovery.recovery_reference(root,meta))
        self.assertEqual(seen[1][1]['resume_override'],kwargs['resume_session'])
        self.assertIn(recovery.TIMEOUT_RECOVERY_GUIDANCE, seen[1][0][1])
        self.assertIn('VERIFIED SAME-REVIEWER REQUIRED DELIVERY PROGRESS', seen[1][0][1])
        self.assertIsNone(seen[2][1]['document_recovery_from']);self.assertIsNone(seen[2][1]['resume_override'])

if __name__=='__main__':unittest.main()
