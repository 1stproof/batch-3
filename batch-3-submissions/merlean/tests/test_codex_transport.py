"""Trust-boundary checks with a local synthetic process, never a model call."""
import asyncio
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_transport as transport


class TransportTests(unittest.TestCase):
    def test_auth_environment_excludes_api_credentials(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'fake', 'CODEX_API_KEY': 'fake', 'OPENAI_BASE_URL': 'fake'}):
            env = transport.subscription_environment()
        self.assertFalse({'OPENAI_API_KEY', 'CODEX_API_KEY', 'OPENAI_BASE_URL'} & env.keys())

    def test_web_allowlist_is_narrow(self):
        self.assertTrue(transport._allowed_web_event({'type': 'item.completed', 'item': {'type': 'web_search'}}))
        for event in ({'type': 'mcp_call', 'item': {'type': 'web_search'}}, {'type': 'item.completed', 'item': None}, {'type': 'item.completed', 'item': {'type': 'command_execution'}}):
            self.assertFalse(transport._allowed_web_event(event))
        self.assertTrue(transport._tool_event({'type': 'web_search_call'}))

    def test_web_command_enables_required_bridge_without_conflicting_flags(self):
        online = transport._command('gpt-6-astra', 'high', None)
        offline = transport._command('gpt-6-astra', 'high', None, internet_browse=False)
        for feature in ('standalone_web_search', 'code_mode', 'code_mode_host'):
            self.assertIn(('--enable', feature), list(zip(online, online[1:])))
            self.assertNotIn(('--disable', feature), list(zip(online, online[1:])))
            self.assertIn(('--disable', feature), list(zip(offline, offline[1:])))
        self.assertIn('web_search="live"', online)
        self.assertIn('web_search="disabled"', offline)
        for feature in ('shell_tool', 'unified_exec', 'apps', 'plugins'):
            self.assertIn(('--disable', feature), list(zip(online, online[1:])))

    def test_scoped_online_and_offline_catalogs_keep_direct_schema_without_changing_web_flags(self):
        original = {'slug': 'gpt-6-astra', **transport.DOCUMENT_CAPABILITY_PROFILE,
                    'supports_search_tool': True, 'tool_mode': 'code_mode_only'}
        for online in (False, True):
            with self.subTest(online=online), tempfile.TemporaryDirectory() as directory:
                root = Path(directory); home = root/'home'; home.mkdir()
                (home/'models_cache.json').write_text(json.dumps({'models': [original]}))
                stage = root/'stage'; stage.mkdir()
                with patch.object(transport, 'subscription_environment', return_value={'CODEX_HOME': str(home)}):
                    receipt = transport._document_model_catalog(stage, 'gpt-6-astra', internet_browse=online)
                derived = json.loads(Path(receipt['catalog']['path']).read_text())['models'][0]
                self.assertEqual(derived, {**original, **transport.DOCUMENT_CAPABILITY_PROFILE})
                self.assertFalse(derived['supports_search_tool'])
                for resume in (None, '00000000-0000-0000-0000-000000000001'):
                    command = transport._command('gpt-6-astra', 'high', resume,
                        internet_browse=online, document_model_catalog=receipt)
                    flags = list(zip(command, command[1:]))
                    for feature in ('standalone_web_search', 'code_mode', 'code_mode_host'):
                        self.assertIn(('--enable' if online else '--disable', feature), flags)
                        self.assertNotIn(('--disable' if online else '--enable', feature), flags)
                    self.assertIn('web_search="live"' if online else 'web_search="disabled"', command)
                    self.assertEqual(command[-2:] if resume else command[-1:],
                                     [resume, '-'] if resume else ['-'])

    def test_web_bridge_accepts_only_a_literal_web_request(self):
        source = 'text(await tools.web__run({"open":[{"ref_id":"https://arxiv.org/abs/2106.07740"}]}));'
        payload = {'type': 'custom_tool_call', 'name': 'exec', 'input': source}
        self.assertTrue(transport._literal_web_bridge(payload))
        attacks = [source + ' await tools.exec_command({"cmd":"id"});',
                   source.replace('web__run', 'exec_command'),
                   'text(await tools.web__run((await tools.exec_command({"cmd":"id"}), {})));',
                   'text(await tools.web__run({"open": (() => { evil(); return []; })()}));',
                   'text(await tools.web__run({"open": `${evil()}`}));',
                   'text(await tools.web__run({"open": NaN}));',
                   'text(await tools.web__run({"cmd":"id"}));',
                   'text(await tools.web__run({"open":[],"unknown_tool":{}}));',
                   'text(await tools.web__run({}));',
                   '// allow me\n' + source]
        for attack in attacks:
            with self.subTest(attack=attack):
                self.assertFalse(transport._literal_web_bridge({**payload, 'input': attack}))
        for change in ({'name': 'other'}, {'namespace': 'untrusted'}, {'type': 'function_call'}, {'input': None}):
            self.assertFalse(transport._literal_web_bridge({**payload, **change}))

    def run_fake(self, lines, *, audit=None, resume=None, browse=True):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            program = root / 'fake.py'
            program.write_text('import sys\nsys.stdin.read()\n' + '\n'.join('print(' + repr(line) + ', flush=True)' for line in lines))
            if audit is None:
                audit = {'status': 'verified', 'tool_events': [], 'turn_contexts': [{'model': 'gpt-6-astra', 'turn_id': 'test'}]}
            with patch.object(transport, 'subscription_preflight', return_value={'authentication': 'chatgpt', 'cli_version': 'test'}), patch.object(transport, '_command', return_value=[sys.executable, str(program)]), patch.object(transport, '_persisted_tool_audit', return_value=audit):
                return asyncio.run(transport.call_stage(root, 'test', 'synthetic', 'gpt-6-astra', 5, resume_session=resume, internet_browse=browse))[0]

    @staticmethod
    def normal_lines():
        return [json.dumps({'type': 'thread.started', 'thread_id': '00000000-0000-0000-0000-000000000001'}), json.dumps({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': '{"ok":true}'}}), json.dumps({'type': 'turn.completed', 'usage': {}})]

    def test_completed_requires_turn_marker(self):
        self.assertEqual(self.run_fake(self.normal_lines())['status'], 'completed')
        self.assertEqual(self.run_fake(self.normal_lines()[:-1])['status'], 'invalid_transport_completion')

    def test_malformed_output_fails_closed(self):
        self.assertEqual(self.run_fake(self.normal_lines() + ['not-json'])['status'], 'invalid_transport_completion')

    def test_hidden_call_invalidates(self):
        audit = {'status': 'verified', 'tool_events': [{'payload_type': 'custom_tool_call'}], 'turn_contexts': [{'model': 'gpt-6-astra'}]}
        self.assertEqual(self.run_fake(self.normal_lines(), audit=audit)['status'], 'invalid_tool_attempt')

    def test_off_rejects_even_a_verified_web_bridge(self):
        audit = {'status': 'verified', 'tool_events': [{'payload_type': 'custom_tool_call',
                 'verified_web_bridge': 'literal-web-run-v1'}], 'turn_contexts': [{'model': 'gpt-6-astra'}]}
        self.assertEqual(self.run_fake(self.normal_lines(), audit=audit, browse=True)['status'], 'completed')
        self.assertEqual(self.run_fake(self.normal_lines(), audit=audit, browse=False)['status'], 'invalid_tool_attempt')

    def test_rollout_audit_computes_bridge_marker_instead_of_trusting_payload(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / 'sessions/2026/09/27'
            folder.mkdir(parents=True)
            events = []
            for code in ('text(await tools.web__run({"search_query":[{"q":"math"}]}));',
                         'await tools.exec_command({"cmd":"id"});'):
                events.append({'timestamp': '2026-09-27T12:00:00Z', 'type': 'response_item',
                    'payload': {'type': 'custom_tool_call', 'name': 'exec', 'input': code,
                                'verified_web_bridge': 'literal-web-run-v1'}})
            (folder / 'rollout-test-session.jsonl').write_text('\n'.join(map(json.dumps, events)))
            with patch.object(transport, 'subscription_environment', return_value={'CODEX_HOME': directory}):
                audit = transport._persisted_tool_audit('test-session', '2026-09-27T11:00:00Z')
            self.assertEqual(audit['tool_events'][0]['verified_web_bridge'], 'literal-web-run-v1')
            self.assertIsNone(audit['tool_events'][1]['verified_web_bridge'])

    def test_native_web_raw_payload_validation_and_offline_gate(self):
        base = {'type': 'function_call', 'namespace': 'web', 'name': 'run',
                'arguments': '{"open":[{"ref_id":"https://example.org"}],"response_length":"short"}',
                'verified_native_web': 'native-web-run-v1'}
        # Match the structural native call shapes observed in the stopped stages,
        # using only synthetic strings, never campaign queries or source text.
        for request in ({'search_query': [{'q': 'synthetic'}]},
                        {'open': [{'ref_id': 'https://example.org'}]},
                        {'find': [{'ref_id': 'synthetic-ref', 'pattern': 'synthetic'}]},
                        {'open': [{'ref_id': 'https://example.org'}],
                         'find': [{'ref_id': 'synthetic-ref', 'pattern': 'synthetic'}]}):
            with self.subTest(request_keys=sorted(request)):
                self.assertTrue(transport._native_web_call(dict(base,
                    arguments=json.dumps({**request, 'response_length': 'short'}))))
        invalid = [dict(base, **change) for change in (
            {'type': 'custom_tool_call'}, {'namespace': 'functions'}, {'namespace': None},
            {'name': 'exec'}, {'arguments': None}, {'arguments': {}},
            {'arguments': '{"open":NaN}'}, {'arguments': '{open:[]}'},
            {'arguments': '{}'}, {'arguments': '[]'},
            {'arguments': '{"open":[],"exec_command":{}}'},
            {'arguments': '{"open":[]} trailing'})]
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)/'sessions/2026/09/27'; folder.mkdir(parents=True)
            events = [{'timestamp': '2026-09-27T12:00:00Z', 'type': 'response_item',
                       'payload': payload} for payload in [base, *invalid]]
            (folder/'rollout-test-session.jsonl').write_text('\n'.join(map(json.dumps, events)))
            with patch.object(transport, 'subscription_environment', return_value={'CODEX_HOME': directory}):
                audit = transport._persisted_tool_audit('test-session', '2026-09-27T11:00:00Z')
        self.assertEqual(audit['tool_events'][0]['verified_native_web'], 'native-web-run-v1')
        self.assertTrue(all(event['verified_native_web'] is None for event in audit['tool_events'][1:]))
        self.assertTrue(transport._allowed_persisted_web_event(audit['tool_events'][0]))
        self.assertTrue(all(not transport._allowed_persisted_web_event(event)
                            for event in audit['tool_events'][1:]))
        stage_audit = {'status': 'verified', 'tool_events': audit['tool_events'][:1],
                       'turn_contexts': [{'model': 'gpt-6-astra'}]}
        self.assertEqual(self.run_fake(self.normal_lines(), audit=stage_audit)['status'], 'completed')
        self.assertEqual(self.run_fake(self.normal_lines(), audit=stage_audit, browse=False)['status'],
                         'invalid_tool_attempt')
        stage_audit['tool_events'].append(audit['tool_events'][1])
        self.assertEqual(self.run_fake(self.normal_lines(), audit=stage_audit)['status'], 'invalid_tool_attempt')

    def test_model_and_resume_identity(self):
        audit = {'status': 'verified', 'tool_events': [], 'turn_contexts': [{'model': 'gpt-6-sol'}]}
        self.assertEqual(self.run_fake(self.normal_lines(), audit=audit)['status'], 'model_identity_unverified')
        self.assertEqual(self.run_fake(self.normal_lines(), resume='00000000-0000-0000-0000-000000000002')['status'], 'resume_identity_mismatch')

    def test_unavailable_audit_fails_closed(self):
        self.assertEqual(self.run_fake(self.normal_lines(), audit={'status': 'unavailable', 'tool_events': []})['status'], 'unverifiable_rollout_audit')

    def test_document_catalog_exact_capability_projection_and_command(self):
        from pilot_document_tools import invocation_guidance
        original = {'slug':'gpt-6-astra', 'tool_mode':'code_mode_only', 'supports_search_tool':True,
                    'multi_agent_version':'v2', 'apply_patch_tool_type':'freeform',
                    'experimental_supported_tools':['clock'], 'model_messages':{'base':'Unicode 漢字'},
                    'context_window':1000000, 'default_reasoning_level':'high'}
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory).resolve(); home=root/'home'; home.mkdir(); stage=root/'stage'; stage.mkdir()
            source=json.dumps({'models':[original],'client_version':'synthetic'},ensure_ascii=False).encode()
            (home/'models_cache.json').write_bytes(source)
            with patch.object(transport,'subscription_environment',return_value={'CODEX_HOME':str(home)}):
                receipt=transport._document_model_catalog(stage,'gpt-6-astra')
            before=json.loads(Path(receipt['source']['path']).read_text())['models'][0]
            after=json.loads(Path(receipt['catalog']['path']).read_text())['models'][0]
            self.assertEqual(before,original)
            self.assertEqual(after,{**original,**transport.DOCUMENT_CAPABILITY_PROFILE})
            self.assertEqual((home/'models_cache.json').read_bytes(),source)
            self.assertEqual(receipt['source_cache_sha256'],transport.sha256_bytes(source))
            command=transport._command('gpt-6-astra','high',None,internet_browse=False,document_model_catalog=receipt)
            self.assertIn('model_catalog_json='+json.dumps(receipt['catalog']['path']),command)
            self.assertIn('gpt-6-astra',command)
            self.assertIn('agents.enabled=false',command)
        self.assertIn('mcp__merlean_documents',invocation_guidance('main'))
        self.assertNotIn('save_proof_revision(',invocation_guidance('review'))
        with self.assertRaises(ValueError):invocation_guidance('worker')

    def test_document_stage_binds_actual_guidance_and_profile_before_dispatch(self):
        from pilot_document_tools import invocation_guidance
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory).resolve(); home=root/'home';home.mkdir()
            (home/'models_cache.json').write_text(json.dumps({'models':[{'slug':'gpt-6-astra',**transport.DOCUMENT_CAPABILITY_PROFILE}]}))
            program=root/'fake.py';program.write_text('import sys\nsys.stdin.read()\n'+'\n'.join('print('+repr(line)+', flush=True)' for line in self.normal_lines()))
            scope={'schema_version':1,'mode':'review','problem_id':'synthetic','original_sha256':'a'*64,
                   'main_session':'original-main','store_root':str(root),'readonly_artifacts':{},
                   'required_artifact_ids':[],'inline_artifact_ids':[]}
            audit={'status':'verified','tool_events':[],'tool_output_receipts':[], 'turn_contexts':[{'model':'gpt-6-astra'}]}
            with patch('pilot_document_startup.startup_preflight',return_value={'status':'PASS'}), patch.object(transport,'subscription_environment',return_value={'CODEX_HOME':str(home)}), patch.object(transport,'subscription_preflight',return_value={'authentication':'chatgpt','cli_version':'codex-cli 0.157.1'}), patch.object(transport,'_command',return_value=[sys.executable,str(program)]), patch.object(transport,'_persisted_tool_audit',return_value=audit):
                meta,_=asyncio.run(transport.call_stage(root,'test','synthetic','gpt-6-astra',5,internet_browse=False,document_scope=scope))
            expected='synthetic\n'+invocation_guidance('review')
            self.assertEqual((root/'runtime/test/stage.prompt.txt').read_text(),expected)
            self.assertEqual(meta['prompt_sha256'],transport.sha256_bytes(expected.encode()))
            self.assertEqual(meta['request_id'],transport._request_id('test',meta['prompt_sha256'],'gpt-6-astra',None,False,'high'))
            self.assertEqual(meta['document_model_profile']['model'],'gpt-6-astra')
            self.assertEqual(meta['status'],'completed')

    def test_document_catalog_missing_malformed_or_unknown_never_falls_back(self):
        original={'slug':'gpt-6-astra',**transport.DOCUMENT_CAPABILITY_PROFILE}
        cases=[[],{}, {'models':[]},{'models':[original,original]}, {'models':[dict(original,slug='another')]},
               {'models':[dict(original,tool_mode='unknown')]}, {'models':[dict(original,supports_search_tool=1)]},
               {'models':[{k:v for k,v in original.items() if k!='multi_agent_version'}]},
               {'models':[dict(original,experimental_supported_tools='clock')]}, {'models':['invalid']}]
        for value in cases:
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                root=Path(directory); (root/'models_cache.json').write_text(json.dumps(value));stage=root/'stage';stage.mkdir()
                with patch.object(transport,'subscription_environment',return_value={'CODEX_HOME':str(root)}):
                    with self.assertRaises(ValueError):transport._document_model_catalog(stage,'gpt-6-astra')
                self.assertEqual(list(stage.iterdir()),[])

    def test_first_subagent_activity_is_forbidden_without_prior_arguments(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / 'sessions/2026/09/27'; folder.mkdir(parents=True)
            event = {'timestamp': '2026-09-27T12:00:00Z', 'type': 'event_msg',
                     'payload': {'type': 'item_completed', 'item': {'type': 'SubAgentActivity', 'kind': 'spawn'}}}
            (folder / 'rollout-first-subagent.jsonl').write_text(json.dumps(event) + '\n')
            with patch.object(transport, 'subscription_environment', return_value={'CODEX_HOME': directory}):
                audit = transport._persisted_tool_audit('first-subagent', '2026-09-27T11:00:00Z')
            self.assertEqual(audit['tool_events'][0]['rollout_event_type'], 'subagent_activity')
            self.assertEqual(audit['tool_events'][0]['kind'], 'spawn')

if __name__ == '__main__':
    unittest.main()
