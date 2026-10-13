"""Exact duplicate context sharing cannot replace, alter or accept evidence."""
import copy
import json
import unittest
from pilot_paper_efficiency import compact_artifacts, artifact_text, revision_edits, digest


class EfficiencyTests(unittest.TestCase):
    def test_lossless_inventory_aliases_leave_distinct_scientific_evidence_intact(self):
        inventory=json.dumps({'units':[{'text':'full hypothesis and argument '*300}]})
        payload={'manuscript':'full manuscript','evidence':{'unresolved':['keep this']},
                 'artifacts':{'round-1':inventory,'round-2':inventory,'baseline':inventory+'\n',
                              'review':'FAIL: preserve independent finding'}}
        before=copy.deepcopy(payload);result=compact_artifacts(payload)
        self.assertEqual(payload,before)
        self.assertEqual(compact_artifacts(result),result)
        self.assertEqual({k:artifact_text(result,k) for k in payload['artifacts']},payload['artifacts'])
        self.assertEqual(result['evidence'],payload['evidence'])
        self.assertEqual(result['manuscript'],payload['manuscript'])
        self.assertEqual(set(result['artifact_aliases']),{'round-2'})
        self.assertLess(len(json.dumps(result)),len(json.dumps(payload)))

    def test_alias_tamper_missing_target_chain_and_conflict_fail_closed(self):
        original=compact_artifacts({'artifacts':{'a':'x'*5000,'b':'x'*5000}})
        for mode in ['changed','missing','chain','conflict','unhashable']:
            value=copy.deepcopy(original)
            if mode=='changed':value['artifacts']['a']+='changed'
            elif mode=='missing':del value['artifacts']['a']
            elif mode=='chain':value['artifact_aliases']['a']=value['artifact_aliases']['b']
            elif mode=='conflict':value['artifacts']['b']='forged'
            else:value['artifact_aliases']['b']['artifact']=[]
            with self.subTest(mode=mode),self.assertRaises(ValueError):artifact_text(value,'b')
            with self.assertRaises(ValueError):compact_artifacts(value)
        self.assertIsNone(artifact_text(original,'not-present'))

    def test_noop_is_explicit_hash_bound_author_response_not_automatic_acceptance(self):
        text='complete unchanged manuscript'
        answer={'unchanged_manuscript_sha256':digest(text),'revision_summary':'Existing findings do not require changes.',
                'no_change_reason':'The recorded evidence supports retaining the exact current manuscript.', 'responses':[]}
        self.assertFalse(revision_edits(answer,text))
        self.assertTrue(revision_edits({'tex':text},text))
        for bad in [{**answer,'tex':text},{**answer,'unchanged_manuscript_sha256':'0'*64},
                    {**answer,'no_change_reason':''},{**answer,'responses':None}]:
            with self.assertRaises(ValueError):revision_edits(bad,text)

    def test_distinct_inputs_never_disappear_even_if_no_alias_savings(self):
        data={'artifacts':{'a':'first','b':'second'},'unresolved_diagnostics':[{'type':'FAIL'}]}
        self.assertEqual(compact_artifacts(data),data)

class FrozenAliasRequestTests(unittest.IsolatedAsyncioTestCase):
    from test_pilot_paper_request_recovery import RequestRecoveryTests as Fixture
    setUp=Fixture.setUp
    scope=Fixture.scope
    receipt=Fixture.receipt
    stopped=Fixture.stopped

    async def test_requested_alias_resolves_exact_saved_bytes_after_native_copy(self):
        import shutil
        from pathlib import Path
        import pilot_paper_requests as requests
        self.stopped()
        text='full archived inventory evidence '*200
        payload=compact_artifacts({'artifacts':{'original.json':text,'08-literature-audit.json':text}})
        ref=self.artifacts['stage-input'];Path(ref['path']).write_text(json.dumps(payload));ref['sha256']=digest(Path(ref['path']).read_text())
        shutil.rmtree(self.pilot.host/'runtime/P1/paper-016-repair-release-audit')
        meta=self.receipt(16,self.scope(['stage-input']),['stage-input'],
            {'evidence_requests':['work/08-literature-audit.json']},session='writer',stage='repair-release-audit')
        self.engine.ledger['calls']=[meta];self.engine.save()
        oldroot=self.pilot.root;target=oldroot.parent/'alias-copy';shutil.copytree(oldroot,target);shutil.rmtree(oldroot)
        self.pilot.root=target;self.pilot.host=target/'host'
        self.engine.root=target/'exam/papers/P1';self.engine.work=self.engine.root/'work'
        self.engine.snapshot=self.engine.root/'snapshot';self.engine.ledger_path=self.engine.root/'paper-ledger.json'
        self.assertTrue(requests.restore(self.engine,'repair-release-audit',True))
        actual=self.engine.request_only_scope['readonly_artifacts']['archive:work/08-literature-audit.json']
        self.assertEqual(Path(actual['path']).read_text(),text)
        self.assertEqual(self.engine.ledger['retrieval_progress']['turns'],1)
        self.assertEqual(self.engine.ledger['calls'],[meta])

    async def test_restoration_is_optional_frozen_author_only_and_hash_bound(self):
        from pathlib import Path
        import pilot_paper as paper
        from pilot_paper_efficiency import author_sources
        import pilot_document_tools as documents
        root=self.engine.root;body=b'detailed supported earlier argument'
        raw=root/'raw-source.tex';raw.write_bytes(body)
        manifest=root/'raw-manifest.json'
        manifest.write_text(json.dumps({'source':str(raw),'files':[{'kind':'manuscript','source':str(raw),'sha256':documents.digest(body)}]}))
        manifest_bytes=manifest.read_bytes()
        checkpoint={'manifest':str(manifest),'manifest_sha256':documents.digest(manifest.read_bytes())}
        sources,missing=author_sources(root,checkpoint)
        self.assertEqual(sources['preserved-author:raw'],body)
        self.assertIn('preserved-author:pre-shrink',missing)
        before=root/'work/05-pre-shrink-inventory.json';before.write_text(json.dumps({'source_sha256':documents.digest(body)}))
        (root/'draft-001.tex').write_bytes(body)
        state=json.loads(self.engine.state_path.read_text());state['raw_checkpoint']=checkpoint
        self.engine.state_path.write_text(json.dumps(state))
        text,scope=self.engine.scoped_payload('revise-1',{'manuscript':'current'})
        self.assertIn('preserved-author:raw',scope['readonly_artifacts'])
        self.assertNotIn('preserved-author:raw',scope['required_artifact_ids'])
        snapshot=Path(scope['readonly_artifacts']['preserved-author:raw']['path'])
        self.assertNotEqual(snapshot,raw)
        self.assertEqual(snapshot.read_bytes(),body)
        _,blind=self.engine.scoped_payload('reader-1',self.engine.reader_payload('reader-1',paper.baseline_tex('P1')),force_scope=True)
        self.assertFalse(any(k.startswith('preserved-author:') for k in blind['readonly_artifacts']))
        raw.write_text('changed raw argument')
        self.assertEqual(snapshot.read_bytes(),body)
        with self.assertRaisesRegex(ValueError,'raw author source changed'):author_sources(root,checkpoint)
        raw.write_bytes(body);manifest.write_text('{}')
        with self.assertRaisesRegex(ValueError,'raw manifest changed'):author_sources(root,checkpoint)
        manifest.write_bytes(manifest_bytes);raw.unlink();raw.symlink_to(root/'draft-001.tex')
        with self.assertRaises(ValueError):author_sources(root,checkpoint)
        self.assertNotIn('05-pre-shrink-inventory.json',paper.WRITER_FILES)
