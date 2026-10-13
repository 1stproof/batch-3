"""Exact readable sharing codec tests; no model calls."""
import copy,json,unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import pilot_main_feedback_sharing as s

class ExactSharingTests(unittest.TestCase):
    def fixture(self):
        value={'id':'same','finding':'α漢字 e\u0301\r\nfirst version','status':'rejected',
               'evidence':{'~root/path':[True,1,1.0,-0.0,None]},
               'bindings':[{'pointer':'/ordinary-user-data','object_id':'not-a-reference','expanded_sha256':'literal'}]}
        root={'z':copy.deepcopy(value),'a':copy.deepcopy(value),
              'distinct_version':{**value,'finding':'Second version','status':'open'},
              'null_original':None,'$ref':{'id':'ordinary-user-key'},'format':'ordinary-data'}
        original=('Prefix\r\n'+s.MARKER+s.encode(root)+'\nSuffix Unicode λ\r\n').encode()
        packet,envelope=s.factor_document(original,{'shared_finding':'/z'})
        return original,packet,envelope,root
    def test_unicode_order_types_collision_keys_and_distinct_versions_roundtrip(self):
        original,packet,envelope,root=self.fixture()
        self.assertEqual(s.expand_document(packet,expected_document_sha256=s.sha(original)),original)
        text=s.expand_envelope(envelope,expected_feedback_sha256=s.sha(s.encode(root)))
        result=json.loads(text)
        self.assertEqual(list(result),list(root))
        self.assertEqual(result,root)
        self.assertEqual(result['distinct_version']['finding'],'Second version')
        self.assertEqual(result['z']['bindings'][0]['object_id'],'not-a-reference')
        self.assertIn('-0.0',text)
        self.assertEqual(envelope['shared_objects'][0]['original_occurrences'],['/z','/a'])
    def test_nested_aliases_expand_every_original_path(self):
        review={'id':'review','status':'invalid','findings':[{'id':'g','finding':'v1'},{'id':'g','finding':'v2'}]}
        scientific={'comprehensive_review':review,'other':None}
        value={'first':scientific,'second':copy.deepcopy(scientific),'third':copy.deepcopy(review)}
        original=(s.MARKER+s.encode(value)+'\n').encode()
        packet,envelope=s.factor_document(original,{'review':'/third','scientific':'/first'})
        self.assertEqual(s.expand_document(packet,expected_document_sha256=s.sha(original)),original)
        self.assertEqual(envelope['shared_objects'][0]['original_occurrences'],['/first/comprehensive_review','/second/comprehensive_review','/third'])
        self.assertEqual(envelope['shared_objects'][1]['bindings'][0]['object_id'],'review')
    def test_escaped_pointer_keys_and_array_order(self):
        item={'finding':'exact','status':'unknown'}
        value={'a/b~c':[item,copy.deepcopy(item)],'user_empty_key':{'':None}}
        original=(s.MARKER+s.encode(value)).encode()
        packet,envelope=s.factor_document(original,{'item':'/a~1b~0c/0'})
        self.assertEqual(s.expand_document(packet,expected_document_sha256=s.sha(original)),original)
        self.assertEqual(envelope['shared_objects'][0]['original_occurrences'],['/a~1b~0c/0','/a~1b~0c/1'])
    def test_unknown_reference_cycle_hash_tamper_and_path_tamper_fail_closed(self):
        original,packet,envelope,root=self.fixture()
        for kind in ('unknown','cycle','value','hash','path','overlap','census','required','external_hash'):
            bad=copy.deepcopy(envelope)
            if kind=='unknown':bad['root']['bindings'][0]['object_id']='absent'
            elif kind=='cycle':
                definition=bad['shared_objects'][0]
                definition['value']['evidence']=None
                definition['bindings']=[{'pointer':'/evidence','object_id':definition['id'],'expanded_sha256':definition['expanded_sha256']}]
            elif kind=='value':bad['shared_objects'][0]['value']['finding']='changed'
            elif kind=='hash':bad['root']['bindings'][0]['expanded_sha256']='0'*64
            elif kind=='path':bad['root']['bindings'][0]['pointer']='/null_original'
            elif kind=='overlap':bad['root']['bindings'].append(copy.deepcopy(bad['root']['bindings'][0]))
            elif kind=='census':bad['shared_objects'][0]['original_occurrences'].pop()
            elif kind=='required':bad['required_objects']=[]
            with self.subTest(kind=kind),self.assertRaises(ValueError):
                s.expand_envelope(bad,expected_feedback_sha256='0'*64 if kind=='external_hash' else s.sha(s.encode(root)))
    def test_outer_framing_and_external_original_digest_are_required(self):
        original,packet,envelope,root=self.fixture()
        with self.assertRaises(ValueError):s.expand_document(b'changed'+packet,expected_document_sha256=s.sha(original))
        with self.assertRaises(ValueError):s.expand_document(packet,expected_document_sha256='0'*64)
        # Rebinding all internal document hashes cannot override the external expected hash.
        envelope['original_document']['sha256']='1'*64
        prefix,_,suffix,_=s.partition_document(packet)
        forged=(prefix+s.encode(envelope)+suffix).encode()
        with self.assertRaises(ValueError):s.expand_document(forged,expected_document_sha256=s.sha(original))
    def test_unsupported_duplicate_keys_noncanonical_or_nonduplicate_are_refused(self):
        for text in ('{"a":1,"a":2}','{ "a":1 }','{"a":NaN}'):
            with self.subTest(text=text),self.assertRaises(ValueError):s.factor_document((s.MARKER+text).encode(),{})
        with self.assertRaises(ValueError):s.factor_document((s.MARKER+'{"a":{"x":1}}').encode(),{'item':'/a'})
    def test_deterministic_packet_and_no_input_mutation(self):
        original,packet,envelope,root=self.fixture()
        self.assertEqual(s.factor_document(original,{'shared_finding':'/z'})[0],packet)
        before=s.encode(envelope)
        s.expand_envelope(envelope,expected_feedback_sha256=s.sha(s.encode(root)))
        self.assertEqual(s.encode(envelope),before)

class AutomaticSharingTests(unittest.TestCase):
    def test_nested_duplicate_selection_preserves_distinct_versions(self):
        review = {'status':'invalid', 'findings':[{'id':'same', 'text':'old '*2000},
                                                {'id':'same', 'text':'new '*2000}]}
        feedback = {'comprehensive_review':review, 'other':'payload '*1000}
        root = {'first':feedback, 'second':copy.deepcopy(feedback), 'third':copy.deepcopy(review)}
        original = 'prefix\n'+s.MARKER+s.encode(root)+'\nsuffix'
        shared, kind = s.optimize_main_instruction(original)
        self.assertEqual(kind, s.FORMAT)
        _, _, _, envelope = s.partition_document(shared.encode())
        self.assertEqual(len(envelope['shared_objects']), 2)
        self.assertLess(len(shared), len(original))
        self.assertEqual(s.restore_main_instruction(shared, expected_original_sha256=s.sha(original)), original)
        self.assertEqual(s.optimize_main_instruction(original), (shared, kind))

    def test_noncanonical_no_duplicate_or_unprofitable_input_keeps_exact_required_text(self):
        for original in ('plain correction task', s.MARKER+'{ "x": 1 }',
                         s.MARKER+'{"a":{"x":1},"b":{"x":1}}',
                         s.MARKER+'{"a":1,"a":2}', s.MARKER+'{"a":NaN}'):
            with self.subTest(original=original):
                self.assertEqual(s.optimize_main_instruction(original), (original, 'original'))
                self.assertEqual(s.restore_main_instruction(original, expected_original_sha256=s.sha(original)), original)
                with self.assertRaises(ValueError):
                    s.restore_main_instruction(original, expected_original_sha256='0'*64)

    def test_literal_protocol_shaped_json_is_not_implicitly_expanded(self):
        original = s.MARKER+s.encode({'format':s.FORMAT, 'bindings':[], 'root':None})
        self.assertEqual(s.restore_main_instruction(original, expected_original_sha256=s.sha(original)), original)

if __name__=='__main__':unittest.main()
