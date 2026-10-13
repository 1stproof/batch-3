"""Recovery packing preserves exact evidence and never changes review authority."""
import asyncio
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import AsyncMock
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import codex_pilot as p
import test_pilot_final_progression as fixtures


def replace_pointer(target, pointer, value):
    keys = [k.replace('~1', '/').replace('~0', '~') for k in pointer.split('/')[1:]]
    for key in keys[:-1]:
        target = target[int(key)] if isinstance(target, list) else target[key]
    target[int(keys[-1]) if isinstance(target, list) else keys[-1]] = copy.deepcopy(value)


def restore_packet(packet):
    packet = copy.deepcopy(packet)
    from pilot_review_inputs import restore_review_packet
    from review_packet_codec import restore_schema_inputs
    if isinstance(packet, dict) and 'review_packet_codec' in packet:
        packet = restore_review_packet(packet)
    if isinstance(packet, dict) and 'schema_codec' in packet:
        packet = restore_schema_inputs(packet)
    if 'line_encoding' in packet:
        result = packet['evidence']
        for pointer, parts in packet['line_bindings']:
            text = ''.join(part if isinstance(part, str) else packet['supplied_lines'][part] for part in parts)
            replace_pointer(result, pointer, text)
        packet = result
    if 'paragraph_encoding' in packet:
        result = packet['evidence']
        for binding in packet['paragraph_bindings']:
            text = ''.join(part if isinstance(part, str) else packet['supplied_paragraphs'][part]
                           for part in binding['parts'])
            replace_pointer(result, binding['pointer'], text)
        packet = result
    if 'object_encoding' in packet:
        result = packet['evidence']
        for binding in packet['object_bindings']:
            replace_pointer(result, binding['pointer'], packet['supplied_values'][binding['supplied_value']])
        packet = result
    if 'encoding' in packet and 'supplied_texts' in packet:
        result = packet['evidence']
        for binding in packet['bindings']:
            replace_pointer(result, binding['pointer'], packet['supplied_texts'][binding['supplied_text']])
        packet = result
    if 'serialization_encoding' in packet:
        result = packet['review_inputs']
        for binding in packet['serialization_bindings']:
            spec = packet['serializations'][binding['serialization_index']]
            replace_pointer(result, binding['pointer'], json.dumps(spec['json_value'],
                ensure_ascii=spec['ensure_ascii'], indent=spec['indent']) + spec['trailing_text'])
        packet = result
    return packet


class RecoveryPackingTests(unittest.TestCase):
    def test_exact_structured_roundtrip_and_literal_markers(self):
        repeated = {'rows': [{'k/~': 'Unicode α  spaces\\n', 'sequence': list(range(100)),
                              'literal': '[Exact supplied JSON value 0]'}]}
        value = {'a': [repeated, repeated], 'b/~': copy.deepcopy(repeated),
                 'canonical_json': p.encoded({'duplicated': repeated, 'again': repeated}),
                 'duplicate_key_json': '{"x": 1, "x": 2}',
                 'marker_object': {'object_encoding': 'literal', 'evidence': 'unchanged'},
                 'unknowns': [None, False, 1, 1.25, ''],
                 'invalid_prior_response_not_authority': {'status': 'invalid_not_authority', 'invalid_review': repeated}}
        before = copy.deepcopy(value)
        packet = p.recovery_inputs(value)
        self.assertIn('object_bindings', packet)
        self.assertEqual(restore_packet(packet), value)
        self.assertEqual(value, before)
        self.assertLess(len(p.prompt_encoded(packet)), len(p.prompt_encoded(value)))

    def test_selected_paragraph_layer_preserves_whitespace_markers_and_unicode(self):
        paragraph = 'A complete shared paragraph: αβ漢字 ' + ' mathematical prose ' * 20 + '\n\n'
        crlf = 'CRLF complete paragraph ' * 20 + '\r\n\r\n'
        value = {'a/~': '\n\n' + paragraph + 'tail A\n',
                 'nested': [paragraph + '\n\n' + crlf + 'tail B',
                            '[Exact supplied paragraph sequence]\n\n' + paragraph + 'tail C\n\n',
                            crlf + 'tail D'],
                 'literal': {'paragraph_encoding': 'literal marker', 'parts': [0, '0']},
                 'short': 'small\r\n', 'empty': ''}
        before = copy.deepcopy(value)
        packed = p.paragraph_inputs(value)
        self.assertIn('paragraph_encoding', packed)
        self.assertTrue(packed['paragraph_bindings'])
        self.assertIn(paragraph, packed['supplied_paragraphs'])
        self.assertEqual(restore_packet(packed), value)
        self.assertEqual(value, before)
        self.assertLess(len(p.prompt_encoded(packed).encode()), len(p.prompt_encoded(value).encode()))
        self.assertEqual(p.paragraph_inputs({'unique': 'word ' * 100}), {'unique': 'word ' * 100})

    def test_selected_whole_line_layer_roundtrips_terminators_and_typed_literals(self):
        lines = [('Exact shared whole line α é 漢字 ' + str(n) + ' ' + 'proof text ' * 12 + end)
                 for n, end in enumerate(('\n', '\r\n', '\r', '\u2028', ''))]
        value = {'a/~': 'unique start A\n' + ''.join(lines),
                 'list': ['unique start B\n' + ''.join(lines), 'prefix C\n' + ''.join(lines)],
                 'literal': [None, False, 0, '[Exact supplied paragraph sequence]',
                             {'line_encoding': 'literal', 'line_bindings': [[0, 1]]}],
                 'empty': '', 'last': 'unterminated'}
        before = copy.deepcopy(value)
        packed = p.line_inputs(value)
        self.assertIn('line_encoding', packed)
        self.assertEqual(restore_packet(packed), before)
        self.assertEqual(value, before)
        for line in packed['supplied_lines']:
            self.assertIn(line, lines)
        self.assertLess(len(p.prompt_encoded(packed).encode()), len(p.prompt_encoded(value).encode()))
        small = {'only': lines[0]}
        self.assertEqual(p.line_inputs(small), small)

    def test_line_dictionary_prunes_unused_entries_and_remaps_refs(self):
        unused = 'Unprofitable short line ' * 4 + '\n'
        used = 'Useful complete line α ' * 20 + '\n'
        value = {'x' * 1000: unused, 'y' * 1000: unused,
                 'a': 'a\n' + used * 5, 'b': 'b\n' + used * 5}
        packed = p.line_inputs(value)
        self.assertIn('line_encoding', packed)
        self.assertNotIn(unused, packed['supplied_lines'])
        self.assertEqual(packed['supplied_lines'], [used])
        self.assertEqual(restore_packet(packed), value)
        self.assertTrue(all(part == 0 for _, parts in packed['line_bindings']
                            for part in parts if type(part) is int))

    def test_no_savings_keeps_original_exact_packet(self):
        value = {'unique': ['one', 1, False, None]}
        self.assertEqual(p.recovery_inputs(value), p.review_inputs(value))

    def test_recovery_carries_identical_inputs_and_complete_invalid_response(self):
        fixture = fixtures.FinalProgressionTests(); fixture.setUp(); self.addCleanup(fixture.doCleanups)
        x = fixture.x
        x.findings = [fixture.finding('required')]
        raw = fixture.review(finding_dispositions=[fixture.disposition('historical-only')])
        prompts = []
        class Captured(Exception): pass
        async def call(role, instruction, **kwargs):
            prompts.append(instruction)
            if len(prompts) == 2: raise Captured()
            return fixture.meta('reviewer'), raw
        x.call = call
        with self.assertRaises(Captured): asyncio.run(x.review_candidate('comprehensive'))
        marker = 'EXACT REVIEW INPUTS (lossless supplied-text bindings):\n'
        original = restore_packet(json.loads(prompts[0].split(marker)[1]))
        recovery = restore_packet(json.loads(prompts[1].split(marker)[1]))
        diagnostic = recovery.pop('invalid_prior_response_not_authority')
        self.assertEqual(original, recovery)
        self.assertEqual(diagnostic['invalid_review'], raw)
        self.assertEqual(diagnostic['status'], 'invalid_not_authority')
        self.assertEqual(diagnostic['error'], 'finding disposition has unknown ID')
        self.assertIn('REQUIRED PRIOR FINDING IDS', prompts[0])
        self.assertIn('Use these exact stable IDs', prompts[0])
        self.assertIn('INVALID, is NOT authority', prompts[1])
        self.assertIsNone(x.active_triage)
        self.assertEqual(x.findings, [fixture.finding('required')])
        self.assertEqual(json.loads(next(x.folder.glob('*invalid-1.json')).read_text()), diagnostic)

if __name__ == '__main__': unittest.main()
