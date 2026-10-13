"""Initial request recovery uses real scoped transport receipts and no models."""
from pathlib import Path
import json
import unittest
from unittest.mock import patch

import test_pilot_paper_read_delivery as fixtures
import pilot_document_tools as tools
import pilot_paper as paper
import pilot_paper_initial_review as initial
import pilot_paper_read_delivery as reads


class InitialReviewTests(unittest.IsolatedAsyncioTestCase):
    setUp = fixtures.PaperReadDeliveryTests.setUp
    scope = fixtures.PaperReadDeliveryTests.scope
    receipt = fixtures.PaperReadDeliveryTests.receipt
    rewrite = fixtures.PaperReadDeliveryTests.rewrite

    def pending(self, answer=None):
        meta = self.receipt(3, self.scope(['stage-input', 'archive:a']), ['stage-input'],
                            answer or {'evidence_requests':['a', 'references.md']}, fresh=True)
        self.engine.ledger.update(calls=[meta], admissions=[{'name':meta['name'], 'stage':'raw-audit',
            'resume_session':None}], reader_ids=[], retrieval_progress={'stage':'raw-audit',
            'session':None, 'turns':1, 'writer':False})
        self.engine.save()
        self.engine.restored_ledger = True
        return meta

    async def test_same_reviewer_full_reread_preserves_history_and_turns(self):
        prior = self.pending()
        before = (self.pilot.host/'runtime'/prior['name']/'stage.meta.json').read_bytes()
        self.engine.restore_retrieval('raw-audit', writer=False)
        self.assertEqual(self.engine.ledger['retrieval_progress']['session'], 'reviewer')
        self.assertEqual(self.engine.initial_review_unavailable, ['references.md'])
        self.assertFalse(reads.delivered(self.engine, prior))
        self.engine.restored_ledger = True
        self.engine.restore_retrieval('raw-audit', writer=False)
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'], 1)
        self.config['internet_browse'] = True
        async def fake(host, name, prompt, model, timeout, resume, **kw):
            self.assertEqual(resume, 'reviewer')
            self.assertFalse(kw['internet_browse'])
            self.assertNotIn('public_source_store', kw['document_scope'])
            self.config['internet_browse'] = False  # Synthetic receipt uses this flag too.
            self.assertEqual(set(kw['document_scope']['required_artifact_ids']), {'stage-input','archive:a'})
            meta = self.receipt(4, kw['document_scope'], kw['document_scope']['required_artifact_ids'],
                {'verdict':'FAIL','findings':[]}, prompt=tools.document_prompt(prompt,'review',public_sources=False))
            return meta, {'verdict':'FAIL','findings':[]}
        with patch('pilot_paper.call_stage', side_effect=fake):
            result = await self.engine.call('raw-audit', 'Return audit', {})
        self.assertEqual(result[0], 'reviewer')
        self.assertNotIn('retrieval_progress', self.engine.ledger)
        self.assertFalse(hasattr(self.engine, 'initial_review_scope'))
        self.assertEqual(before, (self.pilot.host/'runtime'/prior['name']/'stage.meta.json').read_bytes())
        self.assertFalse((self.pilot.host/'runtime'/prior['name']/reads.FILE).exists())

    async def test_substantive_and_wrong_identity_rejected(self):
        self.pending({'verdict':'PASS'})
        with self.assertRaisesRegex(paper.PaperRecoveryRequired, 'solely evidence requests'):
            self.engine.restore_retrieval('raw-audit', writer=False)
        # Independent identity is checked before any state update.
        self.temp.cleanup(); self.setUp()
        self.pending()
        self.engine.ledger['writer_ids'].append('reviewer')
        with self.assertRaisesRegex(paper.PaperRecoveryRequired, 'not independent'):
            self.engine.restore_retrieval('raw-audit', writer=False)

    async def test_changed_bytes_and_exhausted_progress_rejected(self):
        self.pending()
        Path(self.artifacts['archive:a']['path']).write_text('changed')
        with self.assertRaises(paper.PaperRecoveryRequired):
            self.engine.restore_retrieval('raw-audit', writer=False)
        self.temp.cleanup(); self.setUp()
        self.pending()
        self.engine.ledger['retrieval_progress']['turns'] = 4
        with self.assertRaises(paper.PaperRecoveryRequired):
            self.engine.restore_retrieval('raw-audit', writer=False)

    async def test_traversal_absolute_and_symlink_cache_refused(self):
        scope = self.scope(['stage-input'])
        scope.update(producer={}, receipt_path=str(self.engine.root/'unused'))
        for path in ('../secret', '/tmp/secret', 'a/../secret'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                initial.requested_scope(scope, [path])
        cache = self.engine.root/'refs/public-sources'
        cache.parent.mkdir()
        cache.symlink_to(self.root)
        scope['public_source_store'] = str(cache)
        with self.assertRaises(ValueError):
            initial.requested_scope(scope, ['refs/public-sources/'+'a'*64+'/raw'])

    async def test_partial_successor_never_accepted_or_retried(self):
        self.pending()
        async def fake(host, name, prompt, model, timeout, resume, **kw):
            meta = self.receipt(4, kw['document_scope'], ['stage-input'], {'verdict':'PASS'},
                prompt=tools.document_prompt(prompt,'review',public_sources=False))
            return meta, {'verdict':'PASS'}
        with patch('pilot_paper.call_stage', side_effect=fake) as dispatch:
            with self.assertRaises(paper.delivery.DeliveryRecoveryRequired):
                await self.engine.call('raw-audit','Audit',{})
            self.engine.restored_ledger = True
            with self.assertRaises(paper.PaperRecoveryRequired):
                await self.engine.call('raw-audit','Audit',{})
        self.assertEqual(dispatch.call_count, 1)
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'], 2)

    async def test_cached_raw_resolves_verified_text_and_changed_hash_fails(self):
        scope = self.scope(['stage-input'])
        scope.update(producer={}, receipt_path=str(self.engine.root/'unused'))
        cache = self.engine.root/'refs/public-sources'
        cache.mkdir(parents=True)
        scope['public_source_store'] = str(cache)
        url = 'https://example.invalid/source'
        source_id = tools.digest(url.encode())
        folder = cache/source_id
        folder.mkdir()
        (folder/'raw').write_bytes(b'%PDF-synthetic')
        (folder/'source.txt').write_text('Verified extracted source text')
        digest = tools.digest((folder/'source.txt').read_bytes())
        (folder/'receipt.json').write_text(json.dumps({'source_id':source_id,'requested_url':url,
            'status':'downloaded','raw_sha256':tools.digest((folder/'raw').read_bytes()),
            'content_files':[], 'members':[{'member':'source.txt','sha256':digest}]}))
        result, missing = initial.requested_scope(scope, ['refs/public-sources/'+source_id+'/raw'])
        self.assertEqual(missing, [])
        self.assertNotIn('public_source_store', result)
        key = 'requested-cache:refs/public-sources/'+source_id+'/source.txt'
        self.assertEqual(result['readonly_artifacts'][key]['sha256'], digest)
        self.assertFalse(any(k.endswith('/raw') for k in result['readonly_artifacts']))
        (folder/'source.txt').write_text('Changed source text')
        with self.assertRaises(ValueError):
            initial.requested_scope(scope, ['refs/public-sources/'+source_id+'/raw'])


if __name__ == '__main__':
    unittest.main()
