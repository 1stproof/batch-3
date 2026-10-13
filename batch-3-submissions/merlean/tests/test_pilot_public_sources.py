import gzip
import asyncio
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch, Mock
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import pilot_public_sources as sources
import pilot_document_tools as docs
import codex_transport as transport


class PublicSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.store = self.root/'public-sources'
    def tearDown(self): self.temp.cleanup()

    def fetch_fixture(self, url='https://example.org/source.tex', body=b'\\section{Claim}\nVerified content is still a human/model judgment.\n'):
        def worker(url, folder):
            (folder/'raw').write_bytes(body)
            return {'final_url':url,'content_type':'text/plain','bytes':len(body),
                    'raw_sha256':sources.digest(body),'members':sources._members(folder,'text/plain'),'read_error':None}
        with patch.object(sources,'_run_worker',side_effect=worker) as call:
            receipt=sources.fetch_public_source(self.store,url)
        self.assertEqual(call.call_count,1)
        return receipt

    def test_credential_private_and_signed_urls_refused(self):
        for url in ['http://example.org/a','https://localhost/a','https://127.0.0.1/a','https://[::1]/a',
                    'https://a:b@example.org/x','https://example.org:8443/x','https://example.org/x?token=secret',
                    'https://example.org/x?X-Amz-Signature=secret','https://example.org/x\nBad:1']:
            with self.subTest(url=url), self.assertRaises(ValueError): sources.validate_url(url)
        with patch.object(sources.socket,'getaddrinfo',return_value=[(2,1,6,'',('93.184.216.34',443)),(2,1,6,'',('10.0.0.1',443))]):
            with self.assertRaises(ValueError):sources.public_addresses('example.org')

    def test_download_pins_validated_ip_and_refuses_redirect_to_private(self):
        response=Mock(status=302)
        response.getheader.side_effect=lambda name,default=None:'https://127.0.0.1/private' if name=='Location' else default
        connection=Mock(); connection.getresponse.return_value=response
        with patch.object(sources,'public_addresses',return_value=['93.184.216.34']), patch.object(sources,'_PinnedHTTPS',return_value=connection) as pinned:
            with self.assertRaises(ValueError): sources.download('https://example.org/source',self.root/'raw')
        self.assertEqual(pinned.call_args.args[:2],('example.org','93.184.216.34'))
        self.assertEqual(connection.request.call_args.args[:2],('GET','/source'))
        self.assertNotIn('Cookie',connection.request.call_args.kwargs['headers'])
        connection.close.assert_called_once()

    def test_download_exact_bytes_and_finite_size(self):
        response=Mock(status=200)
        response.getheader.side_effect=lambda name,default=None: {'Content-Type':'application/x-bibtex'}.get(name,default)
        response.read.side_effect=[b'@misc{a, title={Exact}}',b'']
        connection=Mock(); connection.getresponse.return_value=response
        with patch.object(sources,'public_addresses',return_value=['93.184.216.34']),patch.object(sources,'_PinnedHTTPS',return_value=connection):
            meta=sources.download('https://example.org/bib',self.root/'raw')
        self.assertEqual((self.root/'raw').read_bytes(),b'@misc{a, title={Exact}}')
        self.assertEqual(meta['bytes'],len(b'@misc{a, title={Exact}}'))
        response.read.side_effect=[b'12345']
        with patch.object(sources,'MAX_BYTES',4),patch.object(sources,'public_addresses',return_value=['93.184.216.34']),patch.object(sources,'_PinnedHTTPS',return_value=connection):
            with self.assertRaises(ValueError):sources.download('https://example.org/large',self.root/'large')

    def test_cache_preserves_exact_export_and_fails_closed_on_mutation(self):
        body=b'@article{Key,\n title = {Exact export},\n}\n'
        receipt=self.fetch_fixture('https://arxiv.org/bibtex/0000.00000',body)
        with patch.object(sources,'_run_worker') as worker:
            self.assertEqual(sources.fetch_public_source(self.store,receipt['requested_url'])['raw_sha256'],sources.digest(body))
            worker.assert_not_called()
        read=sources.read_public_source(self.store,receipt['source_id'])
        self.assertEqual(read['text'].encode(),body)
        self.assertIsNone(read['next_start'])
        Path(receipt['source_path']).write_bytes(b'changed')
        with self.assertRaises(ValueError):sources.read_public_source(self.store,receipt['source_id'])

    def test_failure_and_interruption_never_reset_retry_budget(self):
        with patch.object(sources,'_run_worker',side_effect=TimeoutError('fixture timeout')) as worker:
            # TimeoutError is OSError; failed attempt remains explicit and cached.
            first=sources.fetch_public_source(self.store,'https://example.org/blocked')
            second=sources.fetch_public_source(self.store,'https://example.org/blocked')
        self.assertEqual(worker.call_count,1);self.assertEqual(first['status'],'unavailable');self.assertEqual(first,second)
        ident=sources.digest(b'https://example.org/interrupted');folder=self.store/ident;folder.mkdir()
        (folder/'admission.json').write_text('{}')
        with patch.object(sources,'_run_worker') as worker:
            result=sources.fetch_public_source(self.store,'https://example.org/interrupted')
            worker.assert_not_called()
        self.assertIn('interrupted',result['error'])

    def test_caps_and_chunk_read(self):
        receipt=self.fetch_fixture(body=b'x'*(sources.READ_CHARS+4))
        first=sources.read_public_source(self.store,receipt['source_id'])
        self.assertEqual(first['next_start'],sources.READ_CHARS)
        self.assertEqual(sources.read_public_source(self.store,receipt['source_id'],start=first['next_start'])['text'],'xxxx')
        with self.assertRaises(ValueError):sources.read_public_source(self.store,receipt['source_id'],member='../../secret')
        with patch.object(sources,'MAX_URLS',1),patch.object(sources,'_run_worker') as worker:
            self.assertEqual(sources.fetch_public_source(self.store,'https://example.org/another')['status'],'unavailable')
            worker.assert_not_called()

    def test_gzip_and_tar_full_source_members_and_copied_runtime(self):
        from pilot_document_startup import prepare_runtime,verify_runtime
        stage=self.root/'stage';stage.mkdir();runtime=prepare_runtime(stage);server=verify_runtime(runtime)
        for kind in ('gzip','tar'):
            folder=self.root/kind;folder.mkdir()
            if kind=='gzip': body=gzip.compress(b'\\section{A} Exact claim')
            else:
                buffer=io.BytesIO()
                with tarfile.open(fileobj=buffer,mode='w:gz') as archive:
                    for name,data in [('main.tex',b'\\input{lemma}'),('lemma.tex',b'Exact source statement'),('ref.bib',b'@misc{k}')]:
                        info=tarfile.TarInfo(name);info.size=len(data);archive.addfile(info,io.BytesIO(data))
                body=buffer.getvalue()
            (folder/'raw').write_bytes(body)
            code='import json,sys;from pathlib import Path;import pilot_public_sources as p;print(json.dumps(p._members(Path(sys.argv[1]),"application/gzip")))'
            result=subprocess.run([sys.executable,'-c',code,str(folder)],cwd=server.parent,capture_output=True,text=True,timeout=10)
            self.assertEqual(result.returncode,0,result.stderr)
            members=json.loads(result.stdout)
            self.assertTrue(any(item['member'].endswith('.tex') for item in members))
            if kind=='tar':self.assertEqual(len(members),3)
        self.assertIn('paper_writing_codex/safe_extract.py',runtime['files'])

    def test_archive_traversal_rejected(self):
        folder=self.root/'archive';folder.mkdir();buffer=io.BytesIO()
        with tarfile.open(fileobj=buffer,mode='w:gz') as archive:
            info=tarfile.TarInfo('../escape.tex');info.size=1;archive.addfile(info,io.BytesIO(b'x'))
        (folder/'raw').write_bytes(buffer.getvalue())
        with self.assertRaises(ValueError):sources._members(folder,'application/gzip')
        self.assertFalse((self.root/'escape.tex').exists())

    def test_timeout_kills_single_direct_worker_and_reaps(self):
        process=Mock(pid=12345)
        process.communicate.side_effect=[subprocess.TimeoutExpired('fixture',30),(b'',None)]
        with patch.object(sources.subprocess,'Popen',return_value=process) as popen:
            with self.assertRaises(subprocess.TimeoutExpired):sources._run_worker('https://example.org/a',self.root)
        self.assertNotIn('start_new_session',popen.call_args.kwargs);process.kill.assert_called_once()
        self.assertEqual(process.communicate.call_count,2)

    def test_helper_lifetime_is_armed_before_work_and_owns_its_group(self):
        folder=self.root/'helper';folder.mkdir();(folder/'admission.json').write_text('{}')
        timer=Mock()
        def work(url, path):
            timer.start.assert_called_once()
            self.assertTrue((folder/'helper-lifetime.json').exists())
            return {'fixture':True}
        with patch.object(sources.os,'getpid',return_value=4321),patch.object(sources.os,'getpgrp',return_value=4321),patch.object(sources.threading,'Timer',return_value=timer) as factory,patch.object(sources,'_worker',side_effect=work):
            self.assertEqual(sources._helper_main('https://example.org/a',folder),{'fixture':True})
        factory.assert_called_once_with(sources.FETCH_SECONDS,sources._hard_lifetime,args=(4321,))
        timer.cancel.assert_called_once()
        with patch.object(sources.os,'getpid',return_value=4321),patch.object(sources.os,'getpgrp',return_value=4321),patch.object(sources.os,'kill') as kill:
            sources._hard_lifetime(4321)
        kill.assert_called_once_with(4321,sources.signal.SIGKILL)

    def test_pdf_extraction_has_disk_time_and_stderr_bounds(self):
        folder=self.root/'pdf';folder.mkdir();(folder/'raw').write_bytes(b'%PDF-fixture')
        process=Mock(pid=12345);process.wait.return_value=0
        def convert(*args,**kwargs):
            self.assertIs(kwargs['preexec_fn'],sources._pdf_limits)
            self.assertNotIn('start_new_session',kwargs)
            self.assertEqual(kwargs['stderr'],subprocess.DEVNULL);(folder/'source.txt').write_text('Page 1 exact extracted text')
            return process
        with patch.object(sources.shutil,'which',return_value='/fixture/pdftotext'),patch.object(sources.subprocess,'Popen',side_effect=convert):
            self.assertEqual(sources._members(folder,'application/pdf')[0]['member'],'source.txt')
        process.wait.assert_called_once_with(timeout=8)
        self.assertEqual(json.loads((folder/'converter-lifetime.json').read_text())['pid'],12345)
        with patch.object(sources.resource,'setrlimit') as limit:sources._pdf_limits()
        limit.assert_called_once_with(sources.resource.RLIMIT_FSIZE,(sources.MAX_TEXT_BYTES,sources.MAX_TEXT_BYTES))

    def test_research_snapshot_paper_handoff_and_failed_cache(self):
        receipt=self.fetch_fixture()
        with patch.object(sources,'_run_worker',side_effect=ValueError('unavailable')):
            failure=sources.fetch_public_source(self.store,'https://example.org/missing')
        snapshot=self.root/'snapshot'/'evidence'/'public-sources'
        shutil.copytree(self.store,snapshot)  # Same file-preserving semantics as ExamRuntime.snapshot.
        target=self.root/'paper'/'public-sources'
        catalog=sources.seed_public_sources(snapshot,target)
        self.assertEqual(len(catalog),2)
        read=sources.read_public_source(target,receipt['source_id'])
        self.assertIn('Verified content',read['text']);self.assertTrue(read['source_path'].startswith(str(target)))
        with patch.object(sources,'_run_worker') as worker:
            self.assertEqual(sources.fetch_public_source(target,failure['requested_url'])['status'],'unavailable');worker.assert_not_called()

    def test_online_document_tools_never_count_as_original_delivery(self):
        artifact=self.root/'original.txt';artifact.write_text('original evidence')
        spec={'schema_version':1,'mode':'review','problem_id':'p','original_sha256':'a'*64,'main_session':'main',
              'store_root':str(self.root),'readonly_artifacts':{'original':{'path':str(artifact),'sha256':sources.digest(artifact.read_bytes()),'media_type':'text/plain'}},'required_artifact_ids':['original'],'inline_artifact_ids':[]}
        scope,_=docs.prepare_scope(spec,self.root,{'stage':'p/review','request_id':'r','session_id':None},internet_browse=True)
        server=docs.DocumentTools(scope)
        with patch.object(sources,'fetch_public_source',return_value={'status':'unavailable','source_id':'b'*64,'error':'limit'}):
            result=server.call('fetch_public_source',{'url':'https://example.org/a'},1,{'callId':'c','sessionId':'reviewer'})
        self.assertFalse(result['isError'])
        receipt=json.loads(Path(scope['receipt_path']).read_text())
        self.assertIsNone(receipt['read']);self.assertIsNotNone(receipt['public_source'])
        self.assertIn('fetch_public_source',docs.available_tools(scope))
        offline={k:v for k,v in scope.items() if k!='public_source_store'}
        self.assertNotIn('fetch_public_source',docs.available_tools(offline))
        self.assertFalse(docs.allowed_event({'type':'item.started','item':{'type':'mcp_tool_call','server':docs.SERVER,'tool':'fetch_public_source','arguments':{}}},offline))

    def test_failed_partial_archive_is_hashed_but_never_read_authority(self):
        def partial(url,folder):
            target=folder/'extracted'/'data.json';target.parent.mkdir();target.write_text('not even JSON')
            raise ValueError('bounded extraction failure')
        with patch.object(sources,'_run_worker',side_effect=partial):
            receipt=sources.fetch_public_source(self.store,'https://example.org/partial')
        self.assertEqual(receipt['status'],'unavailable')
        self.assertEqual(receipt['content_files'][0]['path'],'extracted/data.json')
        target=self.root/'paper-cache';sources.seed_public_sources(self.store,target)
        self.assertEqual(sources.read_public_source(target,receipt['source_id'])['status'],'unavailable')
        (target/receipt['source_id']/'extracted'/'data.json').write_text('changed')
        with self.assertRaises(ValueError):sources.verify_public_source(target,receipt['source_id'])

    def test_online_operation_receipt_cannot_satisfy_original_evidence(self):
        artifact=self.root/'proof.txt';artifact.write_text('original proof')
        spec={'schema_version':1,'mode':'review','problem_id':'p','original_sha256':'a'*64,'main_session':'main','store_root':str(self.root),
              'readonly_artifacts':{'proof':{'path':str(artifact),'sha256':sources.digest(artifact.read_bytes()),'media_type':'text/plain'}},
              'required_artifact_ids':['proof'],'inline_artifact_ids':[]}
        scope,_=docs.prepare_scope(spec,self.root,{'stage':'p/review','request_id':'r','session_id':None},internet_browse=True)
        server=docs.DocumentTools(scope);args={'url':'https://example.org/ref'}
        with patch.object(sources,'fetch_public_source',return_value={'status':'unavailable','source_id':'b'*64,'error':'finite budget'}):
            result=server.call('fetch_public_source',args,1,{'callId':'public-1','sessionId':'reviewer'})
        event={'type':'item.completed','item':{'tool':'fetch_public_source','arguments':args,'result':{'content':result['content'],'structured_content':None},'error':None,'status':'completed'}}
        persisted={'namespace':docs.NAMESPACE,'name':'fetch_public_source','call_id':'public-1','arguments_canonical_sha256':docs.digest(docs.encoded(args).encode())}
        output={'call_id':'public-1','output_format':'list','text_parts':[{**transport._tool_output_part(text),'type':'input_text','keys':['text','type']} for text in ['Wall time: 0.001 seconds\nOutput:',result['content'][0]['text']]]}
        audit=docs.audit_operations(scope,[event],[persisted],'reviewer',[output])
        self.assertEqual(audit['status'],'PASS');self.assertFalse(audit['required_material_delivered'])
        self.assertFalse(audit['required_artifact_coverage']['proof'])
        self.assertEqual(audit['public_source_operations'][0]['status'],'unavailable')

    def test_combined_online_scoped_transport_dispatch_fixture(self):
        from test_codex_transport import TransportTests
        home=self.root/'home';home.mkdir()
        (home/'models_cache.json').write_text(json.dumps({'models':[{'slug':'gpt-6-astra',**transport.DOCUMENT_CAPABILITY_PROFILE}]}))
        program=self.root/'fixture.py'
        program.write_text('import sys\nsys.stdin.read()\n'+'\n'.join('print('+repr(line)+',flush=True)' for line in TransportTests().normal_lines()))
        spec={'schema_version':1,'mode':'review','problem_id':'p','original_sha256':'a'*64,'main_session':'main','store_root':str(self.root),'readonly_artifacts':{},'required_artifact_ids':[],'inline_artifact_ids':[]}
        audit={'status':'verified','tool_events':[{'payload_type':'web_search_call'}],'tool_output_receipts':[],'turn_contexts':[{'model':'gpt-6-astra'}]}
        with patch('pilot_document_startup.startup_preflight',return_value={'status':'PASS'}) as startup,patch.object(transport,'subscription_environment',return_value={'CODEX_HOME':str(home)}),patch.object(transport,'subscription_preflight',return_value={'authentication':'chatgpt','cli_version':'codex-cli 0.157.1'}),patch.object(transport,'_command',return_value=[sys.executable,str(program)]),patch.object(transport,'_persisted_tool_audit',return_value=audit):
            meta,_=asyncio.run(transport.call_stage(self.root,'online','fixture','gpt-6-astra',5,internet_browse=True,document_scope=spec))
        self.assertEqual(meta['status'],'completed');self.assertEqual(meta['persisted_tool_event_count'],0)
        self.assertTrue(startup.call_args.kwargs['public_sources'])
        self.assertFalse(meta['document_model_profile']['capability_overrides']['supports_search_tool'])
        self.assertIn('fetch_public_source',(self.root/'runtime'/'online'/'stage.prompt.txt').read_text())

    def test_online_catalog_preserves_model_without_deferred_tool_search(self):
        home=self.root/'home';home.mkdir();stage=self.root/'stage';stage.mkdir()
        original={'slug':'gpt-6-astra',**transport.DOCUMENT_CAPABILITY_PROFILE,
                  'supports_search_tool':True,'context_window':99999}
        (home/'models_cache.json').write_text(json.dumps({'models':[original]}))
        with patch.object(transport,'subscription_environment',return_value={'CODEX_HOME':str(home)}):
            receipt=transport._document_model_catalog(stage,'gpt-6-astra',internet_browse=True)
        derived=json.loads(Path(receipt['catalog']['path']).read_text())['models'][0]
        self.assertFalse(derived['supports_search_tool']);self.assertEqual(derived['tool_mode'],'direct')
        self.assertEqual(derived['slug'],original['slug']);self.assertEqual(derived['context_window'],99999)
        self.assertEqual(json.loads((home/'models_cache.json').read_text())['models'][0],original)
        self.assertIn('fetch_public_source',docs.document_prompt('P','review',True))


if __name__=='__main__': unittest.main()
