"""Shared review values preserve every byte represented by the JSON value."""
import copy
import json
import math
import random
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from pilot_review_inputs import optimize_review_packet, restore_review_packet, efficient_review_inputs
from review_packet_codec import schema_inputs, restore_schema_inputs


def exact(value):
    return json.dumps(value,ensure_ascii=False,separators=(',',':'),allow_nan=False)


def decode(packet):
    if 'review_packet_codec' in packet:
        return restore_review_packet(packet)
    return restore_schema_inputs(packet)


class EfficientReviewInputsTests(unittest.TestCase):
    def fixture(self):
        sentence = 'The exact unchanged diagnostic remains a recorded failure with no acceptance authority. '
        return {'history':[{'actor':'independent reviewer', 'diagnostic':f'Attempt {i}. '+sentence*3,
            'receipt':{'status':'invalid_not_authority','candidate_sha256':'c'*64,'actual_prompt_sha256':'p'*64},
            'findings':[{'id':'finding-α','severity':'gap','finding':sentence,'resolved':False}],
            'source':'theorem exact : True := by trivial\r\n'} for i in range(90)],
            'invalid_prior_response_not_authority':{'verdict':'PASS','shape':'invalid','raw':'  \n漢字\t😀'}}

    def test_exact_roundtrip_all_records_and_no_input_mutation(self):
        value=self.fixture();before=copy.deepcopy(value)
        packed=efficient_review_inputs(value)
        self.assertEqual(exact(decode(packed)),exact(value))
        self.assertEqual(value,before)
        self.assertLess(len(exact(packed).encode()),len(exact(schema_inputs(value)).encode()))
        self.assertEqual(decode(packed)['invalid_prior_response_not_authority'],value['invalid_prior_response_not_authority'])

    def test_containers_reference_markers_and_mixed_scalar_types_are_literal(self):
        value=self.fixture()
        value['literal']=[['ref',0],['text',['ref',1]], [None,[1]], {'review_packet_codec':'literal'},
                          None,True,False,1,1.0,-0.0,10**80,{},[], '', '\x00\r\n café e\u0301',
                          {'a':1,'b':2},{'b':2,'a':1}]
        restored=decode(efficient_review_inputs(value))
        self.assertEqual(exact(restored),exact(value))
        self.assertEqual(list(restored['literal'][-1]),['b','a'])
        self.assertIs(type(restored['literal'][8]),float)

    def test_dictionary_copies_do_not_alias_independent_original_values(self):
        value=self.fixture();restored=decode(efficient_review_inputs(value))
        restored['history'][0]['receipt']['status']='changed in decoder result'
        self.assertEqual(restored['history'][1]['receipt']['status'],'invalid_not_authority')
        self.assertEqual(value['history'][0]['receipt']['status'],'invalid_not_authority')

    def test_small_packet_falls_back_and_total_size_never_regresses(self):
        for value in (None,0,'text',[],{}, {'x':[True,3.0]}):
            self.assertIs(optimize_review_packet(value),value)
            self.assertLessEqual(len(exact(efficient_review_inputs(value)).encode()),len(exact(schema_inputs(value)).encode()))

    def test_forward_reference_cycle_bad_schema_and_text_type_fail_closed(self):
        packet=optimize_review_packet(self.fixture())
        for mutate in (
            lambda p:p.update(tree=['ref',True]),
            lambda p:p.update(tree=['text',[123]]),
            lambda p:p.update(shared_values=[['ref',0]],tree=['ref',0]),
            lambda p:p.update(tree=[-2,[]]),
            lambda p:p.update(schemas=[['x','x']]),
        ):
            altered=copy.deepcopy(packet);mutate(altered)
            with self.assertRaises(ValueError):restore_review_packet(altered)

    def test_non_json_values_are_not_coerced(self):
        for value in ({2:'key'},(1,2),float('inf'),float('nan')):
            with self.assertRaises((TypeError,ValueError)):efficient_review_inputs(value)

    def test_exact_split_terminators_and_sentences_preserved(self):
        text='First repeated complete diagnostic remains invalid. \r\nSecond sentence remains unresolved!\t Next?  end;\n'
        value={'history':[{'text':text+str(i),'other':'Prefix. '+text} for i in range(70)]}
        self.assertEqual(exact(decode(efficient_review_inputs(value))),exact(value))

    def test_literal_two_element_markers_and_random_nested_json(self):
        from pilot_review_inputs import _candidate
        rng=random.Random(64)
        atoms=[None,True,False,0,1,-0.0,1.25,'ref','text','', 'α\r\n\x00']
        def item(depth):
            if depth==0 or rng.randrange(3)==0:return copy.deepcopy(rng.choice(atoms))
            if rng.randrange(2):return [item(depth-1) for _ in range(rng.randrange(5))]
            return {str(i):item(depth-1) for i in range(rng.randrange(5))}
        values=[['ref',None],['ref',0],['ref','ref'],['text',None],['text',['ref',0]]]
        values += [item(5) for _ in range(500)]
        for value in values:
            packed=_candidate(value,24)
            self.assertEqual(exact(restore_review_packet(packed)),exact(value))
            selected=efficient_review_inputs(value)
            if selected is value:restored=value
            elif type(selected) is dict and 'review_packet_codec' in selected:restored=restore_review_packet(selected)
            else:restored=restore_schema_inputs(selected)
            self.assertEqual(exact(restored),exact(value))
            self.assertLessEqual(len(exact(selected).encode()),len(exact(schema_inputs(value)).encode()))

    def test_math_decimals_abbreviations_and_control_boundaries_exact(self):
        text='For all x ∈ ℝ, x² ≥ 0; e.g. Dr. A computes 3.14159.  Equation a.b is exact!\r\n' + 'Tab\tand null\x00 preserve every character in this deliberately long repeated fragment.\n'
        value={'history':[{'raw':text+str(i),'again':'prefix? '+text} for i in range(80)]}
        self.assertEqual(exact(decode(efficient_review_inputs(value))),exact(value))

    def test_compact_tags_and_legacy_packets_roundtrip_with_literal_collisions(self):
        from pilot_review_inputs import _candidate, compact_packet, COMPACT_FORMAT
        value=self.fixture()
        value['literal_compact_tags']=[[-1],[-2],[-1,[]],[-1,[123]],[None,[-1]],True,-1,1.0]
        legacy=_candidate(value,24)
        compact=compact_packet(legacy)
        self.assertEqual(compact['review_packet_codec'],COMPACT_FORMAT)
        self.assertEqual(exact(restore_review_packet(legacy)),exact(value))
        self.assertEqual(exact(restore_review_packet(compact)),exact(value))
        self.assertLess(len(exact(compact).encode()),len(exact(legacy).encode()))
        for tree in ([0],[True],[-1.0],[-999999],[-1,[123]],[-2,[]],['ref',0],[],[1,2,3]):
            malformed=copy.deepcopy(compact);malformed['tree']=tree
            with self.subTest(tree=tree),self.assertRaises(ValueError):restore_review_packet(malformed)
        malformed=copy.deepcopy(compact);malformed['shared_values']=[[-1]];malformed['tree']=[-1]
        with self.assertRaises(ValueError):restore_review_packet(malformed)

    def test_clause_split_exact_whitespace_and_old_size_bound(self):
        from pilot_review_inputs import _candidate
        common=' A literal repeated clause carries its exact spaces, punctuation and Unicode αβγ'
        value={'rows':[{'text':f'Unique prefix {i},'+common+': '+str(i)+'; suffix'} for i in range(150)]}
        clause=_candidate(value,24,clause_boundaries=True)
        self.assertEqual(exact(restore_review_packet(clause)),exact(value))
        selected=optimize_review_packet(value)
        self.assertLessEqual(len(exact(selected).encode()),len(exact(_candidate(value,24)).encode()))

    def test_variable_word_spans_preserve_every_boundary_and_original_fallback(self):
        from pilot_review_inputs import _candidate, compact_packet
        for whitespace in (' ', '\t', '\r\n', '\r', '\u2003', '\u2028', '  \t'):
            phrase=whitespace.join(['Literal', 'unresolved', 'diagnostic', 'retains', 'precise', 'Unicodeα', 'and', 'all', 'delimiters']*8)
            value={'rows':[{'text':whitespace+'unique'+str(i)+whitespace+phrase+whitespace+'tail'+str(i)+'\x00\u200b'} for i in range(8)]}
            packed=_candidate(value,24,phrase_words=(4,8,12,16,24,32,48,64,96))
            self.assertEqual(exact(restore_review_packet(packed)),exact(value))
            self.assertEqual(exact(restore_review_packet(compact_packet(packed))),exact(value))
            selected=optimize_review_packet(value)
            self.assertLessEqual(len(exact(selected).encode()),len(exact(_candidate(value,24)).encode()))

    def test_short_literal_spans_preserve_long_words_and_all_whitespace(self):
        from pilot_review_inputs import _candidate, compact_packet
        for whitespace in (' ', '\t', '\r\n', '\r', '\u2003', '\u2028', '  \t'):
            longword='exact_UNBROKEN_identifier_αβγ_1234567890'
            value={'text':[whitespace+str(i)+whitespace+longword+whitespace+'short phrase retained exactly'+whitespace+'\x00\u200b'+str(i) for i in range(20)]}
            new=_candidate(value,24,phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),minimum_chunk=24)
            self.assertEqual(exact(restore_review_packet(new)),exact(value))
            self.assertEqual(exact(restore_review_packet(compact_packet(new))),exact(value))
            old=compact_packet(_candidate(value,24,phrase_words=(4,8,12,16,24,32,48,64,96)))
            chosen=optimize_review_packet(value)
            self.assertLessEqual(len(exact(chosen).encode()),len(exact(old).encode()))

    def test_flat_wire_all_scalar_and_container_collisions(self):
        from pilot_review_inputs import _candidate, flat_packet
        value={'negative':[-1,-2,-999,-1.0,-0.0], 'scalars':[None,True,False,0,1,0.0],
               'containers':[[],{},[-1],[-2,-1],[None],{'':'','-1':'α'}],
               'shared':['repeated literal string with enough length for sharing']*12}
        packet=flat_packet(_candidate(value,24))
        self.assertEqual(exact(restore_review_packet(packet)),exact(value))
        for tree in ([],[-2],[-2,True],[-2,-1.0],[-2,0],[-2,-1,0],[-3],[-1,42],[True],[False],[1.0],-999999):
            corrupt=copy.deepcopy(packet);corrupt['tree']=tree
            with self.subTest(tree=tree),self.assertRaises(ValueError):restore_review_packet(corrupt)
        corrupt=copy.deepcopy(packet);corrupt['shared_values']=[-1];corrupt['tree']=-1
        with self.assertRaises(ValueError):restore_review_packet(corrupt)

    def test_storage_selected_spans_preserve_overlaps_and_boundaries(self):
        from pilot_review_inputs import _candidate,flat_packet,compact_packet
        for whitespace in (' ','\t','\r\n','\u2028','\u2003','\x00'):
            phrase='α_identifier'+whitespace+'x.y=\"z\";'+whitespace+'nested:[-2,-1]'+whitespace
            value={'history':[{'text':whitespace+phrase*(i+2)+'unique'+str(i)+whitespace+phrase*3+'\u200b'} for i in range(8)]}
            for lexical in (False,True):
                candidate=_candidate(value,24,phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),minimum_chunk=24,unique_strings=True,lexical_words=lexical,savings_selection=True)
                self.assertEqual(exact(restore_review_packet(flat_packet(candidate))),exact(value))
            prior=compact_packet(_candidate(value,24,phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),minimum_chunk=24))
            self.assertLessEqual(len(exact(optimize_review_packet(value)).encode()),len(exact(prior).encode()))

    def test_flat_cost_short_spans_keep_all_types_boundaries_and_old_minimum(self):
        from pilot_review_inputs import _candidate,flat_packet,compact_packet
        for separator in (' ', '\t', '\r\n', '\u2003', '\u2028', '\x00', '\u200b'):
            phrase=separator.join(['longer','shared','words','αβγ','x.y','[-2,-1]','\"quoted\"'])
            value={'history':[{'text':separator+phrase+separator+str(i)+separator+phrase*3} for i in range(15)],
                   'literals':[-1,-2,True,False,-0.0,[],{},[None],{'ref':-1}]}
            original=exact(value)
            prior=_candidate(value,24,phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),minimum_chunk=24,unique_strings=True,lexical_words=True,savings_selection=True)
            for lexical,minimum,cost in ((False,4,2),(True,8,3)):
                current=_candidate(value,4 if not lexical else 24,phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),minimum_chunk=minimum,unique_strings=True,lexical_words=lexical,savings_selection=True,reference_cost=cost,flat_costs=True)
                for packet in (current,compact_packet(current),flat_packet(current)):
                    self.assertEqual(exact(restore_review_packet(packet)),original)
            self.assertEqual(exact(value),original)
            self.assertLessEqual(len(exact(optimize_review_packet(value)).encode()),len(exact(flat_packet(prior)).encode()))

class PositiveReferenceTests(unittest.TestCase):
    def test_all_literal_collisions_and_dictionary_reordering(self):
        from pilot_review_inputs import _candidate,positive_packet,frequency_order_packet,flat_packet
        values=[0,1,10**80,-1,-2,True,False,0.0,-0.0,-3.5,None,[],{},[-2,0],[0,1],[-1,'x'],
                {'z':0,'a':True,'b':-0.0},'\x00\r\n e\u0301 漢字 😀']
        values += [{'payload':copy.deepcopy(values),'repeat':'shared literal '*20} for _ in range(12)]
        before=exact(values);base=_candidate(values,4)
        for packet in (base,frequency_order_packet(base)):
            encoded=positive_packet(packet)
            self.assertEqual(exact(restore_review_packet(encoded)),before)
            self.assertEqual(exact(restore_review_packet(flat_packet(packet))),before)
        self.assertEqual(exact(values),before)
        self.assertEqual(frequency_order_packet(base),frequency_order_packet(base))
    def test_positive_bad_reference_escapes_and_instruction_mismatch(self):
        from pilot_review_inputs import _candidate,positive_packet,FLAT_INSTRUCTIONS
        base=positive_packet(_candidate({'literal':0},4))
        for change in ({'tree':0},{'tree':[-2,-1]},{'tree':[-2,False]},{'tree':[-2,0.0]},
                       {'shared_values':[0],'tree':0},{'tree':[-1,False]},
                       {'decode':FLAT_INSTRUCTIONS},{'tree':[True,0]}):
            packet=copy.deepcopy(base);packet.update(change)
            with self.assertRaises(ValueError):restore_review_packet(packet)
    def test_topological_diamond_exact_and_invalid_cycle_rejected(self):
        from pilot_review_inputs import FORMAT,INSTRUCTIONS,frequency_order_packet,positive_packet
        packet={'review_packet_codec':FORMAT,'decode':INSTRUCTIONS,'schemas':[],
                'shared_values':['a','b',['text',[['ref',0],['ref',1]]],['text',[['ref',2],['ref',1]]]],
                'tree':[None,[['ref',3],['ref',2],['ref',1],['ref',1],['ref',1]]]}
        expected=restore_review_packet(packet);ordered=frequency_order_packet(packet)
        self.assertEqual(restore_review_packet(positive_packet(ordered)),expected)
        bad=copy.deepcopy(packet);bad['shared_values'][0]=['ref',3]
        with self.assertRaises(ValueError):frequency_order_packet(bad)

class PositiveCostSelectionTests(unittest.TestCase):
    def test_wire_estimator_matches_supported_representations_exactly(self):
        from pilot_review_inputs import _wire_size, _candidate, flat_packet, positive_packet
        # Includes literal integer collisions, bools (not integers), float spelling,
        # negative zero, every container tag, text joins and multi-digit references.
        nodes=[None,True,False,0,1,10000,-1,-200,0.0,-0.0,1.5,'\x00\r\n 漢字 α',
               ['ref',0],['ref',12345],['text',['a',['ref',4],' b']],
               [None,[]],[0,[]],[None,[0,-1,True,-0.0,['ref',123]]]]
        for node in nodes:
            packet={'schemas':[],'shared_values':[],'tree':node}
            for positive,transform in [(False,flat_packet),(True,positive_packet)]:
                with self.subTest(node=node,positive=positive):
                    expected=len(exact(transform(packet)['tree']).encode())
                    self.assertEqual(_wire_size(node,flat_costs=True,positive_costs=positive),expected)
            self.assertEqual(_wire_size(node),len(exact(node).encode()))

    def test_new_candidate_roundtrip_all_boundaries_containers_and_no_mutation(self):
        from pilot_review_inputs import _candidate,positive_packet,flat_packet,compact_packet,frequency_order_packet
        for whitespace in [' ','\r\n','\t','\u2003','\u2028','\x00','\u200b']:
            phrase=whitespace.join(['a','b','literal','old','failed','diagnostic','αβ','x.y','[-2,0]'])
            value={'history':[{'raw':phrase*(i+2)+str(i)+whitespace,'invalid':True} for i in range(9)],
                   'literal':[0,1,-1,False,0.0,-0.0,[-2,0],{'z':2,'a':1},{'a':1,'z':2}]}
            before=exact(value)
            packet=_candidate(value,2,phrase_words=tuple(range(1,17))+(24,32,48,64,96),
                minimum_chunk=2,unique_strings=True,savings_selection=True,reference_cost=1,
                flat_costs=True,positive_costs=True)
            for ordered in [packet,frequency_order_packet(packet)]:
                for transformed in [ordered,compact_packet(ordered),flat_packet(ordered),positive_packet(ordered)]:
                    self.assertEqual(exact(restore_review_packet(transformed)),before)
            self.assertEqual(exact(value),before)

    def test_prior_eleven_candidates_remain_exact_and_complete_minimum_does_not_regress(self):
        from unittest.mock import patch
        import pilot_review_inputs as module
        actual=module._candidate;calls=[]
        value={'history':[{'text':str(i)+' literal old finding retains exact short word spans '*5} for i in range(10)]}
        def record(*args,**kwargs):
            packet=actual(*args,**kwargs);calls.append((args[1:],copy.deepcopy(kwargs),packet));return packet
        with patch.object(module,'_candidate',side_effect=record):chosen=module.optimize_review_packet(value)
        self.assertEqual(len(calls),12)
        self.assertTrue(all('positive_costs' not in options for _,options,_ in calls[:11]))
        self.assertEqual(calls[-1][1]['positive_costs'],True)
        self.assertEqual([args[0] for args,_,_ in calls[:11]],[24]*9+[4,24])
        for args,options,packet in calls[:11]:
            self.assertEqual(exact(packet),exact(actual(value,*args,**options,positive_costs=False)))
            ordered=module.frequency_order_packet(packet)
            for alternative in [packet,ordered]+[f(x) for x in [packet,ordered]
                    for f in [module.compact_packet,module.flat_packet,module.positive_packet]]:
                self.assertLessEqual(len(exact(chosen).encode()),len(exact(alternative).encode()))
        self.assertEqual(exact(restore_review_packet(chosen)),exact(value))
