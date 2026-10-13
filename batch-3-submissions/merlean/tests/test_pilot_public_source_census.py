"""External archive JSON must never become pilot process ownership evidence."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import pilot_continuation as continuation
import pilot_public_sources as sources
import test_pilot_continuation as fixtures


class PublicSourceCensusTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ContinuationTests('test_list_module_registry_restores_exact_terminal_history')
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.source.resolve()
        self.store = self.root/'campaign/problems/problem/public-sources'
        self.url = 'https://example.org/source'
        self.ident = sources.digest(self.url.encode())

    def payload(self, *, failed=False, body=b'{"pid": 12345678}'):
        def worker(url, folder):
            (folder/'raw').write_bytes(b'archive fixture')
            (folder/'extracted').mkdir()
            (folder/'extracted/data.json').write_bytes(body)
            if failed:
                raise TimeoutError('bounded fixture')
            return {'content_type':'application/x-tar', 'raw_sha256':sources.digest(b'archive fixture'),
                    'members':[], 'read_error':'binary preserved only'}
        with patch.object(sources, '_run_worker', side_effect=worker):
            sources.fetch_public_source(self.store, self.url)
        return self.store/self.ident

    def test_external_pid_and_malformed_json_do_not_join_host_census(self):
        for body in (b'{"pid":12345678}', b'\xffinvalid JSON'):
            with self.subTest(body=body):
                if not self.store.exists():
                    folder=self.payload(body=body)
                else:
                    (folder/'extracted/data.json').write_bytes(body)
                    receipt=json.loads((folder/'receipt.json').read_text())
                    receipt['content_files']=sources.source_content_files(folder)
                    (folder/'receipt.json').write_text(json.dumps(receipt))
                self.assertIn(folder/'extracted/data.json', continuation._opaque_public_source_files(self.root))
                self.fixture.load()  # Entire normal stopped-process validation.

    def test_failed_optional_download_retains_opaque_partial_data(self):
        folder=self.payload(failed=True, body=b'{')
        self.assertEqual(sources.verify_public_source(self.store,self.ident)['status'],'unavailable')
        self.fixture.load()
        self.assertEqual(sources.read_public_source(self.store,self.ident)['status'],'unavailable')

    def test_host_helper_pids_remain_mandatory(self):
        folder=self.payload()
        (folder/'helper-lifetime.json').write_text(json.dumps({'pid':12345678}))
        with self.assertRaisesRegex(ValueError,'persisted process missing'):
            self.fixture.load()

    def test_tampered_and_unlisted_payloads_are_rejected(self):
        folder=self.payload()
        (folder/'extracted/data.json').write_text('changed')
        with self.assertRaises(ValueError):continuation._opaque_public_source_files(self.root)
        (folder/'extracted/data.json').write_text('{"pid": 12345678}')
        (folder/'extracted/unlisted.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'payload census'):continuation._opaque_public_source_files(self.root)

    def test_control_file_cannot_be_claimed_as_payload(self):
        folder=self.payload();receipt=json.loads((folder/'receipt.json').read_text())
        receipt['content_files'].append({'path':'admission.json','sha256':sources.digest((folder/'admission.json').read_bytes())})
        (folder/'receipt.json').write_text(json.dumps(receipt))
        with self.assertRaises(ValueError):continuation._opaque_public_source_files(self.root)

    def test_symlink_and_unknown_root_payload_are_rejected(self):
        folder=self.payload()
        (folder/'extracted/link.json').symlink_to(folder/'raw')
        with self.assertRaises(ValueError):continuation._opaque_public_source_files(self.root)
        (folder/'extracted/link.json').unlink()
        (folder/'unknown.json').write_text('{}')
        with self.assertRaises(ValueError):continuation._opaque_public_source_files(self.root)

    def test_interrupted_payload_requires_bound_admission_and_stays_unavailable(self):
        folder=self.payload(failed=True)
        (folder/'receipt.json').unlink()
        with self.assertRaises((ValueError,FileNotFoundError)):continuation._opaque_public_source_files(self.root)
        (folder/'helper-lifetime.json').write_text(json.dumps({'pid':900001,
            'admission_sha256':sources.digest((folder/'admission.json').read_bytes())}))
        self.fixture.load()
        with patch.object(sources,'_run_worker') as worker:
            self.assertEqual(sources.fetch_public_source(self.store,self.url)['status'],'unavailable')
            worker.assert_not_called()
        admission=json.loads((folder/'admission.json').read_text());admission['source_id']='wrong'
        (folder/'admission.json').write_text(json.dumps(admission))
        with self.assertRaises(ValueError):continuation._opaque_public_source_files(self.root)

    def test_snapshot_source_payload_requires_exact_native_snapshot(self):
        import shutil
        folder=self.payload()
        snap=self.root/'exam/papers/problem/snapshot'
        shutil.copytree(self.store,snap/'evidence/public-sources')
        manifest={'files':{str(p.relative_to(snap)):sources.digest(p.read_bytes()) for p in snap.rglob('*') if p.is_file()}}
        (snap/'manifest.json').write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError,'native receipt binding'):continuation._opaque_public_source_files(self.root)
        (snap.parent/'snapshot-receipt.json').write_text(json.dumps({'manifest_sha256':sources.digest((snap/'manifest.json').read_bytes())}))
        files=continuation._opaque_public_source_files(self.root)
        self.assertIn(snap/'evidence/public-sources'/self.ident/'extracted/data.json',files)
        (snap/'evidence/public-sources'/self.ident/'extracted/data.json').write_text('changed')
        with self.assertRaisesRegex(ValueError,'snapshot evidence changed'):continuation._opaque_public_source_files(self.root)
        manifest['files']['evidence/public-sources/'+self.ident+'/extracted/data.json']=sources.digest(b'changed')
        (snap/'manifest.json').write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError,'native receipt binding'):continuation._opaque_public_source_files(self.root)
