import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_document_tools as t
import pilot_proof_document as store
from codex_transport import _tool_output_part
from pilot_reviewer_inputs import build_review_inputs


class DocumentToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name).resolve()
        self.identity = {'problem_id': 'p1', 'original_sha256': 'a'*64, 'main_session': 'main-original'}
        self.producer = {'stage': 'p1/main', 'request_id': 'request', 'session_id': 'main-original'}
        self.candidate = {'proof_markdown': '# Proof\n\nStill incomplete.\n', 'ledger': {'rows': []}}
        self.saved = store.submit(self.root, **self.identity, expected_revision=None, candidate=self.candidate, producer=self.producer)
        self.evidence = self.root/'evidence.json'; self.evidence.write_text('{"failed":true,"unicode":"漢字\\r\\n"}\n')
        self.spec = {'schema_version':1, 'mode':'main', **self.identity, 'store_root':str(self.root),
                     'readonly_artifacts':{'e1':{'path':str(self.evidence),'sha256':t.digest(self.evidence.read_bytes()),'media_type':'application/json'}},
                     'required_artifact_ids':['e1'], 'inline_artifact_ids':[]}
        self.scope, _ = t.prepare_scope(self.spec,self.root,self.producer)
        self.server = t.DocumentTools(self.scope)

    def tearDown(self): self.temp.cleanup()
    def call(self, tool, args, i=1):
        return self.server.call(tool,args,i,{'callId':f'call-{i}','sessionId':'main-original'})

    def test_id_only_read_resolves_and_verifies_saved_version(self):
        result=self.call('read_artifact',{'artifact_id':'e1'})
        self.assertFalse(result['isError'])
        self.assertEqual(json.loads(result['content'][0]['text'])['text'],self.evidence.read_text())
        ranged=self.call('read_artifact',{'artifact_id':'e1','start':0,'end':5},2)
        self.assertEqual(json.loads(ranged['content'][0]['text'])['text'],self.evidence.read_text()[:5])
        self.evidence.write_text('changed saved version')
        self.assertTrue(self.call('read_artifact',{'artifact_id':'e1'},3)['isError'])
        schema=t.tool_definitions('review')[0]['inputSchema']
        self.assertEqual(schema['required'],['artifact_id'])

    def test_host_selected_refs_cache_retains_document_store_and_fails_closed(self):
        target = str(self.root / 'refs/public-sources')
        selected = {**self.spec, 'public_source_store': target}
        destination = self.root / 'selected-stage'
        destination.mkdir()
        online, _ = t.prepare_scope(selected, destination, self.producer, internet_browse=True)
        self.assertEqual(online['store_root'], str(self.root))
        self.assertEqual(online['public_source_store'], target)
        with self.assertRaisesRegex(ValueError, 'offline stage'):
            t.prepare_scope(selected, self.root, self.producer, internet_browse=False)
        for invalid in (str(self.root / 'arbitrary-cache'), str(self.root.parent / 'public-sources')):
            with self.assertRaisesRegex(ValueError, 'host-derived'):
                t.prepare_scope({**selected, 'public_source_store': invalid}, self.root, self.producer, internet_browse=True)
        actual = self.root / 'external'
        actual.mkdir()
        (self.root / 'refs').symlink_to(actual, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            t.prepare_scope(selected, self.root, self.producer, internet_browse=True)

    def test_save_during_turn_is_draft_and_compact_ack(self):
        response=self.call('save_proof_revision',{'expected_revision':self.saved['revision'],'proof_markdown':'# New\n\nGap retained.\n'})
        self.assertFalse(response['isError']); result=json.loads(response['content'][0]['text'])
        self.assertNotIn('proof_markdown',result); self.assertEqual(result['status'],'draft')
        self.assertEqual(store.read_current(self.root,**self.identity)['proof_markdown'],'# New\n\nGap retained.\n')
        self.assertTrue((self.root/'document-operations.jsonl').is_file())
        stale=self.call('save_proof_revision',{'expected_revision':self.saved['revision'],'proof_markdown':'stale'},2)
        self.assertTrue(stale['isError']); self.assertNotEqual(store.read_current(self.root,**self.identity)['proof_markdown'],'stale')
        receipts=[json.loads(line) for line in (self.root/'document-operations.jsonl').read_text().splitlines()]
        current=store.read_current(self.root,**self.identity)
        self.assertEqual(receipts[0]['saved_revision'], {k:current[k] for k in ('revision','manifest_sha256','proof_sha256','status')})
        self.assertIsNone(receipts[1]['saved_revision'])

    def test_known_bad_arguments_are_refused_without_extra_authority(self):
        for i,args in enumerate(({'path':'/etc/passwd'}, {'artifact_id':'../../controller.key','sha256':'a'*64},
                                 {'artifact_id':'e1','sha256':'b'*64}, {'artifact_id':'e1','sha256':self.spec['readonly_artifacts']['e1']['sha256'],'start':True,'end':2}),1):
            response=self.call('read_artifact',args,i); self.assertTrue(response['isError'])
            event={'type':'item.completed','item':{'type':'mcp_tool_call','server':t.SERVER,'tool':'read_artifact','arguments':args}}
            self.assertTrue(t.allowed_event(event,self.scope))
        self.assertEqual(store.read_current(self.root,**self.identity)['revision'],self.saved['revision'])

    def test_role_and_session_cannot_be_overridden(self):
        self.server.scope['mode']='review'
        response=self.call('save_proof_revision',{'expected_revision':self.saved['revision'],'proof_markdown':'forbidden'})
        self.assertTrue(response['isError'])
        self.assertEqual([x['name'] for x in t.tool_definitions('review')],['read_artifact', 'read_required_evidence'])
        self.server.scope['mode']='main'
        response=self.server.call('read_current_proof',{},2,{'callId':'cross','sessionId':'another'})
        self.assertTrue(response['isError'])

    def test_exact_chunk_coverage_and_native_receipt_audit(self):
        text=self.evidence.read_text();events=[];persisted=[];outputs=[]
        for i,(start,end) in enumerate(((0,7),(7,len(text))),1):
            args={'artifact_id':'e1','sha256':self.spec['readonly_artifacts']['e1']['sha256'],'start':start,'end':end}
            result=self.call('read_artifact',args,i)
            native={'content':result['content'],'structured_content':None}
            events.append({'type':'item.completed','item':{'tool':'read_artifact','arguments':args,'result':native,'error':None,'status':'completed'}})
            outputs.append({'call_id':f'call-{i}','output_format':'list','text_parts':[{**_tool_output_part(text),'type':'input_text','keys':['text','type']} for text in ['Wall time: 0.001 seconds\nOutput:',result['content'][0]['text']]]})
            persisted.append({'namespace':t.NAMESPACE,'name':'read_artifact','call_id':f'call-{i}',
                              'arguments_canonical_sha256':t.digest(t.encoded(args).encode())})
        audit=t.audit_operations(self.scope,events,persisted,'main-original',outputs)
        self.assertEqual(audit['status'],'PASS');self.assertTrue(audit['required_material_delivered'])
        events[-1]['item']['result']['content'][0]['text']='truncated'
        diagnostic=t.audit_operations(self.scope,events,persisted,'main-original',outputs)
        self.assertEqual(diagnostic['status'],'PASS');self.assertTrue(diagnostic['required_material_delivered'])
        self.assertFalse(diagnostic['native_diagnostics'][-1]['native_result_matches_receipt'])

    def test_no_hash_only_coverage_and_changed_file_refusal(self):
        self.evidence.write_text('changed')
        result=self.call('read_artifact',{'artifact_id':'e1','sha256':self.spec['readonly_artifacts']['e1']['sha256']})
        self.assertTrue(result['isError'])
        self.assertFalse(t.audit_operations(self.scope,[],[],'main-original',[])['required_material_delivered'])

    def test_symlink_and_fifo_refused_without_blocking(self):
        link=self.root/'link';link.symlink_to(self.evidence)
        with self.assertRaises(ValueError):t.regular_bytes(link)
        fifo=self.root/'fifo';os.mkfifo(fifo)
        with self.assertRaises(ValueError):t.regular_bytes(fifo)

    def test_duplicate_call_never_repeats_mutation(self):
        args={'expected_revision':self.saved['revision'],'proof_markdown':'# Saved once'}
        self.assertFalse(self.call('save_proof_revision',args)['isError'])
        current=store.read_current(self.root,**self.identity)
        self.assertTrue(self.call('save_proof_revision',{'expected_revision':current['revision'],'proof_markdown':'twice'})['isError'])
        self.assertEqual(store.read_current(self.root,**self.identity)['revision'],current['revision'])

    def test_proof_builder_preserves_all_history_and_plain_current_obligations(self):
        packet={'exact_candidate':self.candidate,'exact_dossier':copy.deepcopy(self.candidate),
                'prior_findings':[{'id':'old-gap','finding':'Unresolved contradiction'}],
                'actual_execution_evidence':[{'historical_stage':'old-failure','status':'failed','output':'exact\r\n'}, {'status':'completed','output':'old PASS not authority'}],
                'finding_history':[{'finding':{'id':'old-gap','finding':'older exact variant'}}]}
        before=t.encoded(packet)
        built=build_review_inputs(packet,proof_revision=self.saved['revision'],proof_path=self.saved['proof_path'],artifact_root=self.root/'archive',required_artifact_ids=['actual_execution_evidence'])
        self.assertEqual(t.encoded(packet),before);self.assertEqual(built['text'].count(self.candidate['proof_markdown']),1)
        self.assertIn('Unresolved contradiction',built['text']);self.assertNotIn('old PASS not authority',built['text'])
        collection=built['readonly_artifacts']['actual_execution_evidence']
        self.assertEqual(json.loads(Path(collection['path']).read_text()),packet['actual_execution_evidence'])
        self.assertIn('actual_execution_evidence:1',built['readonly_artifacts']);self.assertEqual(built['inline_artifact_ids'],['proof'])

    def delivered_fixture(self, call_number=1):
        args={'artifact_id':'e1','sha256':self.spec['readonly_artifacts']['e1']['sha256']}
        result=self.call('read_artifact',args,call_number)
        event={'type':'item.completed','item':{'tool':'read_artifact','arguments':args,
               'result':{'content':result['content'],'structured_content':None},'error':None,'status':'completed'}}
        persisted={'namespace':t.NAMESPACE,'name':'read_artifact','call_id':f'call-{call_number}',
                   'arguments_canonical_sha256':t.digest(t.encoded(args).encode())}
        output={'call_id':f'call-{call_number}','output_format':'list','text_parts':[
            {**_tool_output_part(text),'type':'input_text','keys':['text','type']}
            for text in ['Wall time: 0.001 seconds\nOutput:',result['content'][0]['text']]]}
        return event,persisted,output

    def test_large_evidence_chunk_index_preserves_unicode_and_required_collection(self):
        packet = {'exact_candidate': self.candidate,
                  'actual_execution_evidence': [{'output': 'α漢字\r\n' * 15000, 'status': 'failed'}]}
        built = build_review_inputs(packet, proof_revision=self.saved['revision'],
            proof_path=self.saved['proof_path'], artifact_root=self.root/'chunks',
            required_artifact_ids=['actual_execution_evidence'])
        entries = built['readonly_artifacts']
        index = json.loads(Path(entries['actual_execution_evidence::chunks']['path']).read_text())
        parent = Path(entries['actual_execution_evidence']['path']).read_bytes().decode()
        reconstructed = ''.join(Path(entries[c['artifact_id']]['path']).read_bytes().decode()
                                for c in index['chunks'])
        self.assertEqual(parent, reconstructed)
        self.assertEqual(json.loads(reconstructed), packet['actual_execution_evidence'])
        self.assertEqual(built['required_artifact_ids'], ['actual_execution_evidence'])
        scope = {**self.scope, 'readonly_artifacts': entries,
                 'required_artifact_ids': built['required_artifact_ids']}
        t.validate_scope(scope)
        coverage = {k: False for k in entries}
        coverage['actual_execution_evidence::chunks'] = True
        self.assertFalse(t.expand_chunk_coverage(scope, coverage)['actual_execution_evidence'])
        for chunk in index['chunks'][:-1]:
            coverage[chunk['artifact_id']] = True
        self.assertFalse(t.expand_chunk_coverage(scope, coverage)['actual_execution_evidence'])
        coverage[index['chunks'][-1]['artifact_id']] = True
        self.assertTrue(t.expand_chunk_coverage(scope, coverage)['actual_execution_evidence'])
        bad = copy.deepcopy(scope)
        first = index['chunks'][0]['artifact_id']
        bad['readonly_artifacts'][first] = entries[index['chunks'][1]['artifact_id']]
        with self.assertRaises(ValueError):
            t.validate_scope(bad)

    def test_known_cli_clipping_is_not_full_delivery_and_can_be_recovered(self):
        event,call,output=self.delivered_fixture()
        full=event['item']['result']['content'][0]['text']
        clipped=full[:20]+'…'+str(len(full)-40)+' chars truncated…'+full[-20:]
        output['text_parts'][1]={**_tool_output_part(clipped),'type':'input_text','keys':['text','type']}
        audit=t.audit_operations(self.scope,[event],[call],'main-original',[output])
        self.assertEqual(audit['status'],'PASS');self.assertFalse(audit['required_material_delivered'])
        self.assertTrue(audit['delivery_errors'])
        second,call2,output2=self.delivered_fixture(2)
        recovered=t.audit_operations(self.scope,[event,second],[call,call2],'main-original',[output,output2])
        self.assertEqual(recovered['status'],'PASS');self.assertTrue(recovered['required_material_delivered'])
        self.assertTrue(recovered['delivery_errors'])

    def test_unknown_output_change_added_block_and_native_failure_fail_audit(self):
        event,call,output=self.delivered_fixture()
        for change in ('alter','extra','reorder','status','error'):
            e,o=copy.deepcopy(event),copy.deepcopy(output)
            if change=='alter':o['text_parts'][1]=_tool_output_part('injected')
            if change=='extra':o['text_parts'].append(copy.deepcopy(o['text_parts'][1]))
            if change=='reorder':o['text_parts'].reverse()
            if change=='status':e['item']['status']='failed'
            if change=='error':e['item']['error']={'message':'not delivered'}
            with self.subTest(change=change):
                self.assertEqual(t.audit_operations(self.scope,[e],[call],'main-original',[o])['status'],'FAIL')

    def test_native_preview_never_substitutes_for_exact_model_delivery(self):
        event,call,output=self.delivered_fixture()
        event['item']['result']['content'][0]['text']='native diagnostic preview only'
        audit=t.audit_operations(self.scope,[event],[call],'main-original',[output])
        self.assertEqual(audit['status'],'PASS');self.assertTrue(audit['required_material_delivered'])
        self.assertFalse(audit['native_diagnostics'][0]['native_result_matches_receipt'])
        for changed in ('altered model text', 'prefix…3 chars truncated…suffix'):
            output['text_parts'][1]={**_tool_output_part(changed),'type':'input_text','keys':['text','type']}
            audit=t.audit_operations(self.scope,[event],[call],'main-original',[output])
            self.assertEqual(audit['status'],'FAIL');self.assertFalse(audit['required_material_delivered'])

    def test_large_draft_has_no_old_prompt_threshold(self):
        text='# Honest partial draft\n'+('α漢字 gap remains.\n'*100000)
        response=self.call('save_proof_revision',{'expected_revision':self.saved['revision'],'proof_markdown':text})
        self.assertFalse(response['isError'])
        self.assertEqual(store.read_current(self.root,**self.identity)['proof_markdown'],text)
        self.assertLess(len(response['content'][0]['text']),1000)
        self.assertGreater(t.output_capacity(self.scope),len(text.encode()))


class ArtifactInterfaceTests(unittest.TestCase):
    """Use the real server and generic dispatcher, without a provider call."""
    setUp = DocumentToolTests.setUp
    tearDown = DocumentToolTests.tearDown
    call = DocumentToolTests.call
    def test_independent_range_defaults_match_advertised_schema(self):
        text=self.evidence.read_text();size=len(text)
        schema=t.tool_definitions('review')[0]['inputSchema']
        self.assertEqual(schema['required'],['artifact_id'])
        self.assertEqual(set(schema['properties']),{'artifact_id','sha256','start','end'})
        cases=[({},text),({'start':4},text[4:]),({'end':7},text[:7]),
               ({'start':4,'end':7},text[4:7]),({'start':size},''),({'end':0},'')]
        for i,(bounds,expected) in enumerate(cases,1):
            args={'artifact_id':'e1',**bounds}
            self.assertTrue(t.valid_arguments('read_artifact',args,'main'))
            reply=self.call('read_artifact',args,i)
            self.assertFalse(reply['isError']);value=json.loads(reply['content'][0]['text'])
            self.assertEqual(value['text'],expected)
            self.assertEqual(value['start'],bounds.get('start',0))
            self.assertEqual(value['end'],bounds.get('end',size))
        self.assertIn('omitted start is 0 and omitted end is the text length',t.tool_definitions('review')[0]['description'])

    def test_invalid_range_and_legacy_hash_never_get_read_receipt(self):
        size=len(self.evidence.read_text())
        bad=[{'start':size+1},{'end':size+1},{'start':8,'end':2}, {'start':-1}, {'end':-1},
             {'start':True},{'end':False},{'start':1.5},{'end':'4'}, {'extra':1},
             {'sha256':''},{'sha256':'b'*64},{'sha256':None}]
        for i,fields in enumerate(bad,1):
            with self.subTest(fields=fields):
                self.assertTrue(self.call('read_artifact',{'artifact_id':'e1',**fields},i)['isError'])
        receipts=[json.loads(line) for line in Path(self.scope['receipt_path']).read_text().splitlines()]
        self.assertTrue(all(receipt['read'] is None and receipt['is_error'] for receipt in receipts))
        correct={'artifact_id':'e1','sha256':self.spec['readonly_artifacts']['e1']['sha256'],'start':2}
        self.assertFalse(self.call('read_artifact',correct,len(bad)+1)['isError'])

    def test_actual_generic_review_dispatch_has_consistent_effective_tool_guidance(self):
        import asyncio
        from contextlib import nullcontext
        from types import SimpleNamespace
        from unittest.mock import Mock, patch
        import codex_pilot as pilot
        packet={'exact_candidate':self.candidate,'actual_execution_evidence':[{'status':'synthetic'}]}
        built=build_review_inputs(packet,proof_revision=self.saved['revision'],proof_path=self.saved['proof_path'],
                                  artifact_root=self.root/'review-inputs',required_artifact_ids=['actual_execution_evidence'])
        spec={**self.spec,'mode':'review',**{key:built[key] for key in
              ('readonly_artifacts','required_artifact_ids','inline_artifact_ids')}}
        problem=pilot.Problem.__new__(pilot.Problem)
        problem.folder=self.root;problem.ident='p1';problem.statement='Synthetic input';problem.session='main-original'
        problem.counter=0;problem.calls=[];problem.errors=[];problem.implementers=['main-original'];problem.current=self.candidate
        problem.status=Mock();problem.consecutive_failures=0
        problem.pilot=SimpleNamespace(host=self.root,root=self.root,config={'internet_browse':False,
            'codex_binary':'synthetic','proof_document_version':1},semaphore=asyncio.Semaphore(1),
            drain=SimpleNamespace(check=lambda:None,admission=lambda *args:nullcontext()),drain_stage_names=set(),
            remaining=lambda:1000,policy=lambda name:(pilot.REPO/name).read_text())
        seen=[]
        async def transport(root,name,prompt,model,timeout,resume,**kwargs):
            effective=t.document_prompt(prompt,kwargs['document_scope']['mode'])
            seen.append(effective)
            self.assertIn('read_artifact and read_required_evidence document MCP tools',effective)
            self.assertIn('read_required_evidence({"page": 0})',effective)
            self.assertIn('read_artifact({"artifact_id": "an exact indexed ID"})',effective)
            self.assertIn('no hash is needed',effective)
            self.assertNotIn('by artifact_id and sha256',effective)
            self.assertNotIn('Only the explicitly provided read_artifact document MCP tool',effective)
            self.assertEqual({tool['name'] for tool in t.tool_definitions(kwargs['document_scope']['mode'])},
                             {'read_artifact','read_required_evidence'})
            return {'status':'completed','session_id':'fresh-reviewer','module':'proof-review'}, {'status':'synthetic'}
        with patch.object(pilot,'call_stage',transport):
            asyncio.run(problem.call('proof-review',built['text'],document_scope=spec))
        self.assertEqual(len(seen),1)

if __name__=='__main__': unittest.main()
