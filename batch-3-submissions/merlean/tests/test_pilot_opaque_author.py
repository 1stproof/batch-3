"""Typed legacy author artifacts never exempt arbitrary JSON controls."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import pilot_continuation as native


class OpaqueAuthorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve() / 'parent'
        self.folder = self.root / 'exam/papers/p'
        self.stage = self.root / 'host/runtime/p/paper-020-repair-release-audit'
        self.stage.mkdir(parents=True)
        self.folder.mkdir(parents=True)
        from pilot_reviewer_inputs import _artifact
        (self.folder / 'input-artifacts').mkdir()
        self.entry = _artifact(self.folder / 'input-artifacts', b'\\documentclass{article}\n')
        self.cap = self.stage / 'document-capability.json'
        self.scope = dict(schema_version=1, mode='review', problem_id='p', original_sha256='a'*64,
                          main_session='main', store_root=str(self.folder),
                          receipt_path=str(self.stage/'document-operations.jsonl'),
                          producer=dict(stage='p/'+self.stage.name, request_id='request', session_id='writer'),
                          readonly_artifacts={'preserved-author:raw': self.entry},
                          required_artifact_ids=[], inline_artifact_ids=[])
        self.meta = dict(name='p/'+self.stage.name, module='paper-repair-release-audit',
                         request_id='request', session_id='writer')
        self.save()

    def save(self):
        self.cap.write_text(json.dumps(self.scope))
        self.meta['document_capability'] = {'sha256': native._hash(self.cap)}
        (self.stage/'stage.meta.json').write_text(json.dumps(self.meta))

    def test_legacy_and_correct_mime_only_typed_artifacts(self):
        for mime in ('application/json', 'text/plain'):
            self.entry['media_type'] = mime; self.save()
            self.assertEqual(native._opaque_review_chunks(self.root), {Path(self.entry['path'])})
        self.scope['readonly_artifacts'] = {'ordinary-control': self.entry}; self.save()
        self.assertEqual(native._opaque_review_chunks(self.root), set())
        with self.assertRaises(json.JSONDecodeError): json.loads(Path(self.entry['path']).read_text())

    def test_tamper_rejected(self):
        original_scope=json.loads(json.dumps(self.scope)); original_meta=dict(self.meta)
        cases = ('mime','module','session','path','cap','bytes')
        for case in cases:
            with self.subTest(case=case):
                self.scope=json.loads(json.dumps(original_scope));self.meta=dict(original_meta)
                entry=self.scope['readonly_artifacts']['preserved-author:raw']
                Path(self.entry['path']).write_bytes(b'\\documentclass{article}\n')
                if case=='mime': entry['media_type']='text/markdown'
                if case=='module': self.meta['module']='proof-review'
                if case=='session': self.meta['session_id']='different'
                if case=='path':
                    rogue=self.folder/'other.json';shutil.copyfile(entry['path'],rogue);entry['path']=str(rogue)
                self.save()
                if case=='cap': self.cap.write_text(self.cap.read_text()+' ')
                if case=='bytes': Path(entry['path']).write_text('changed')
                with self.assertRaises(ValueError): native._opaque_review_chunks(self.root)

    def test_inherited_exact_copy_and_tampered_seal(self):
        files={str(p.relative_to(self.root)):native._hash(p) for p in self.root.rglob('*') if p.is_file()}
        child=self.root.parent/'child';shutil.copytree(self.root,child)
        receipt={'files':files,'manifest_sha256':hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
        (child/'continuation-parent.json').write_text(json.dumps(receipt))
        path=child/Path(self.entry['path']).relative_to(self.root)
        self.assertEqual(native._opaque_review_chunks(child),{path})
        receipt['manifest_sha256']='0'*64
        (child/'continuation-parent.json').write_text(json.dumps(receipt))
        with self.assertRaisesRegex(ValueError,'parent manifest'):native._opaque_review_chunks(child)
