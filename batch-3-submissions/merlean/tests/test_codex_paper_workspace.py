"""Explicit paper tools and API selection leave legacy/auth boundaries unchanged."""
import asyncio
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import codex_transport as t
import pilot_operations as ops

class PaperWorkspaceTests(unittest.TestCase):
    def test_api_selector_persisted_environment_never_contains_keys(self):
        with patch.dict(os.environ,{'MERLEAN_CODEX_AUTH':'api','OPENAI_API_KEY':'synthetic-secret','CODEX_API_KEY':'synthetic-second'},clear=True):
            env=t.subscription_environment()
            self.assertEqual(env,{'MERLEAN_CODEX_AUTH':'api'})
            for command in (t._command('gpt-6-astra','high',None),ops.command('codex',None)):
                self.assertIn('forced_login_method="api"',command)
                self.assertNotIn('synthetic-secret',' '.join(command))
        with patch.dict(os.environ,{},clear=True):
            self.assertEqual(t.authentication_mode(),'chatgpt')
            self.assertIn('forced_login_method="chatgpt"',t._command('gpt-6-astra','high',None))

    def test_api_preflight_no_fallback_or_credential_error_output(self):
        def result(text,code=0):return subprocess.CompletedProcess([],code,text,'')
        with patch.dict(os.environ,{'MERLEAN_CODEX_AUTH':'api'},clear=True):
            with patch('subprocess.run',side_effect=[result('Logged in using an API key - synthetic-secret'),result('codex-cli 0.159.2')]):
                self.assertEqual(t.subscription_preflight()['authentication'],'api')
            with patch('subprocess.run',return_value=result('Logged in using ChatGPT')) as run:
                with self.assertRaises(RuntimeError) as error:t.subscription_preflight()
                self.assertNotIn('synthetic-secret',str(error.exception));self.assertEqual(run.call_count,1)
        with patch.dict(os.environ,{},clear=True),patch('subprocess.run',return_value=result('Logged in using an API key - synthetic-secret')):
            with self.assertRaises(RuntimeError) as error:t.subscription_preflight()
            self.assertNotIn('synthetic-secret',str(error.exception))

    def test_profiles_keep_delegation_disabled_and_correct_write_policy(self):
        for profile,sandbox in [('author','read-only'),('review','read-only')]:
            cmd=t._command('gpt-6-astra','high',None,paper_profile=profile,internet_browse=False)
            self.assertIn('sandbox_mode='+json.dumps(sandbox),cmd)
            self.assertIn('agents.enabled=false',cmd)
            self.assertIn('web_search="disabled"',cmd)
            self.assertTrue(any(cmd[i:i+2]==['--disable','shell_tool'] for i in range(len(cmd))))
            self.assertTrue(any(cmd[i:i+2]==['--disable','multi_agent'] for i in range(len(cmd))))
        self.assertFalse(t._allowed_paper_event({'type':'item.completed','item':{'type':'file_change'}},'review'))
        self.assertFalse(t._allowed_paper_event({'type':'item.completed','item':{'type':'file_change'}},'author'))
        for name in ['spawn_agent','send_message','mcp_call']:
            self.assertFalse(t._allowed_persisted_paper_event({'rollout_event_type':'response_item','payload_type':'function_call','name':name},'author'))

    def test_workspace_rejected_before_preflight_for_wrong_role_or_scope(self):
        with tempfile.TemporaryDirectory() as folder,patch.object(t,'subscription_preflight',side_effect=AssertionError('must not preflight')):
            for kwargs in [{'module':'main'},{'module':'paper-light-author','document_scope':{}},{'module':'paper-light-author','image_paths':[]}]:
                with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):
                    asyncio.run(t.call_stage(Path(folder)/'host','P1/paper-001-light','x','gpt-6-astra',60,paper_workspace=Path(folder),**kwargs))

    def test_completed_workspace_binding_regular_files_only(self):
        import hashlib
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();(root/'paper.tex').write_text('synthetic')
            (root/'references').mkdir();(root/'references/ref.txt').write_text('reference')
            expected={'paper.tex':hashlib.sha256(b'synthetic').hexdigest(),
                      'references/ref.txt':hashlib.sha256(b'reference').hexdigest()}
            self.assertEqual(t.paper_workspace_files(root),expected)
            (root/'link').symlink_to(root/'paper.tex')
            with self.assertRaises(ValueError):t.paper_workspace_files(root)
            (root/'link').unlink();os.link(root/'paper.tex',root/'hardlink')
            with self.assertRaises(ValueError):t.paper_workspace_files(root)

    def test_unknown_profile_rejected(self):
        with self.assertRaises(ValueError):t._command('gpt-6-astra','high',None,paper_profile='anything')

    def test_api_bundled_metadata_is_offline_and_not_entitlement(self):
        source={'slug':'gpt-6-astra',**t.DOCUMENT_CAPABILITY_PROFILE}
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();stage=root/'stage';stage.mkdir()
            with patch.dict(os.environ,{'MERLEAN_CODEX_AUTH':'api','CODEX_HOME':str(root/'empty')},clear=True),patch('subprocess.run',return_value=subprocess.CompletedProcess([],0,json.dumps({'models':[source]}).encode(),b'')) as run:
                result=t._document_model_catalog(stage,'gpt-6-astra',codex_binary='/pinned/codex')
                self.assertEqual(run.call_args.args[0],['/pinned/codex','debug','models','--bundled'])
                self.assertEqual(result['source_kind'],'cli-bundled-metadata-not-provider-entitlement')
                self.assertFalse(result['provider_availability_verified'])
                self.assertFalse((root/'empty/models_cache.json').exists())
            other=root/'other';other.mkdir()
            with patch.dict(os.environ,{'CODEX_HOME':str(root/'empty')},clear=True),patch('subprocess.run') as run:
                with self.assertRaises((ValueError,OSError)):t._document_model_catalog(other,'gpt-6-astra')
                run.assert_not_called()

    def test_scoped_tools_write_boundaries_and_readonly(self):
        from pilot_paper_tools import PaperTools
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();paper=root/'paper';paper.mkdir()
            (paper/'selected-evidence.json').write_text('{}')
            scope={'workspace':str(paper),'role':'author','receipt_path':str(root/'receipt'),'online':False,'public_store':str(root/'cache')}
            tool=PaperTools(scope)
            self.assertNotIn('isError',tool.call('write_file',{'path':'paper.tex','text':'synthetic'},1))
            for name in ('../controller.json','selected-evidence.json','/tmp/outside'):
                self.assertTrue(tool.call('write_file',{'path':name,'text':'changed'},2)['isError'])
            (paper/'references').symlink_to(root,target_is_directory=True)
            self.assertTrue(tool.call('write_file',{'path':'references/escape','text':'x'},3)['isError'])
            reviewer=PaperTools({**scope,'role':'review'})
            self.assertTrue(reviewer.call('write_file',{'path':'paper.tex','text':'changed'},4)['isError'])
            self.assertEqual((paper/'paper.tex').read_text(),'synthetic')
            self.assertTrue(tool.call('fetch_public_source',{'url':'https://example.org'},5)['isError'])

    def test_evidence_is_hash_bound_and_exports_are_not_control_json(self):
        from pilot_paper_tools import prepare,PaperTools
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();workspace=root/'author';workspace.mkdir();evidence=root/'snapshot';evidence.mkdir();artifact=root/'stage';artifact.mkdir()
            (evidence/'source.txt').write_text('bound')
            cap=prepare(workspace,'author',artifact,evidence_root=evidence,paper_root=root)
            scope=json.loads(Path(cap['path']).read_text());tool=PaperTools(scope)
            self.assertEqual(scope['public_store'],str(root/'public-sources'))
            self.assertNotIn('isError',tool.call('read_file',{'path':'evidence/source.txt'},1))
            self.assertTrue(tool.call('write_file',{'path':'evidence/source.txt','text':'x'},2)['isError'])
            (evidence/'source.txt').write_text('changed')
            self.assertTrue(tool.call('read_file',{'path':'evidence/source.txt'},3)['isError'])
            self.assertTrue(tool.call('write_file',{'path':'references/raw.json','text':'not json'},4)['isError'])
            self.assertNotIn('isError',tool.call('write_file',{'path':'references/source.bib','text':'synthetic'},5))

    def test_compile_failure_is_bounded_tool_error(self):
        import pilot_paper_tools as pt
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();(root/'paper.tex').write_text('synthetic')
            tool=pt.PaperTools({'workspace':str(root),'role':'author','receipt_path':str(root/'receipt')})
            with patch.object(pt,'compile_paper',side_effect=subprocess.TimeoutExpired('fixed compiler',60)):
                self.assertTrue(tool.call('compile_paper',{},1)['isError'])
            with patch.object(pt,'compile_paper',side_effect=OSError('sandbox unavailable')):
                self.assertTrue(tool.call('compile_paper',{},2)['isError'])

    def test_malicious_tex_is_rejected_before_compiler(self):
        from pilot_paper_tools import compile_paper
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'paper.tex'
            for body in (r'\input{/run/secrets/auth}',r'\openin1=/etc/passwd',r'\openout1=../controller'):
                path.write_text(r'\documentclass{article}\begin{document}'+body+r'\end{document}')
                with self.subTest(body=body),patch('subprocess.run') as run:
                    with self.assertRaises(ValueError):compile_paper(path)
                    run.assert_not_called()

    @unittest.skipUnless(__import__('sys').platform=='linux','native Linux compiler boundary')
    def test_native_compiler_denies_host_read_and_write(self):
        import pilot_paper_tools as pt
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);protected=root/'controller.txt';protected.write_text('PRIVATE_SYNTHETIC_CANARY_927')
            path=root/'paper.tex'
            for operation in (r'\input{'+str(protected)+'}',r'\immediate\openout1='+str(protected)+r'\immediate\write1{changed}'):
                path.write_text(r'\documentclass{article}\begin{document}'+operation+r'\end{document}')
                # Deliberately bypass lexical filter to exercise the independent
                # compiler filesystem boundary with adversarial TeX.
                with patch('pilot_paper._validate_tex',side_effect=lambda text:text):report=pt.compile_paper(path)
                self.assertFalse(report['pass'])
                self.assertNotIn('PRIVATE_SYNTHETIC_CANARY_927',report['diagnostic'])
                self.assertEqual(protected.read_text(),'PRIVATE_SYNTHETIC_CANARY_927')

    def test_public_cache_contract_uses_host_store_and_no_arbitrary_member_path(self):
        from pilot_paper_tools import PaperTools
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve();workspace=root/'author';workspace.mkdir();store=root/'public-sources'
            tool=PaperTools({'workspace':str(workspace),'role':'author','receipt_path':str(root/'receipt'),'online':True,'public_store':str(store)})
            with patch('pilot_public_sources.fetch_public_source',return_value={'status':'downloaded','source_id':'synthetic'}) as fetch:
                self.assertNotIn('isError',tool.call('fetch_public_source',{'url':'https://arxiv.org/abs/0000.00000'},1))
                fetch.assert_called_once_with(str(store),'https://arxiv.org/abs/0000.00000')
            with patch('pilot_public_sources.read_public_source',side_effect=ValueError('unknown member')) as read:
                self.assertTrue(tool.call('read_public_source',{'source_id':'synthetic','member':'../controller'},2)['isError'])
                read.assert_called_once_with(str(store),source_id='synthetic',member='../controller')

    def test_quota_metadata_child_uses_same_auth_selector_without_fallback(self):
        import pilot_quota_recheck as quota
        from unittest.mock import AsyncMock
        with tempfile.TemporaryDirectory() as folder,patch.dict(os.environ,{'MERLEAN_CODEX_AUTH':'api','CODEX_HOME':folder},clear=True),patch('pilot_supervisor.sha',return_value='synthetic-unchanged'),patch('asyncio.create_subprocess_exec',new=AsyncMock(side_effect=OSError('synthetic spawn failure'))) as spawn:
            asyncio.run(quota.query({'codex_home':folder,'codex_binary':'codex','environment':t.subscription_environment()},Path(folder)))
            self.assertIn('forced_login_method="api"',spawn.call_args.args)
            self.assertEqual(spawn.call_args.kwargs['env'],{'MERLEAN_CODEX_AUTH':'api','CODEX_HOME':folder})
            self.assertEqual(spawn.await_count,1)
