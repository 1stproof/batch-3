"""Schema packing roundtrips full JSON without marker/type/order collisions."""
import copy
import json
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from review_packet_codec import schema_inputs, restore_schema_inputs


def serialized(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


class ReviewPacketCodecTests(unittest.TestCase):
    def records(self):
        return [{'long_repeated_evidence_field_name': i,
                 'long_repeated_exact_diagnostic_field_name': 'failed diagnostic ' + str(i),
                 'long_repeated_original_scope_field_name': 'unknown',
                 'long_repeated_independent_reviewer_field_name': 'actor' + str(i)} for i in range(200)]

    def test_large_distinct_history_exact_ordered_serialization_roundtrip(self):
        value = {'history': self.records(), 'findings': self.records(),
                 'invalid_prior_response_not_authority': {'status': 'invalid_not_authority',
                    'diagnostic': 'keep every character\r\n α漢字 😀  ', 'response': self.records()}}
        before = copy.deepcopy(value)
        packed = schema_inputs(value)
        restored = restore_schema_inputs(json.loads(serialized(packed)))
        self.assertEqual(serialized(restored), serialized(value))
        self.assertEqual(before, value)
        self.assertLess(len(serialized(packed).encode()), len(serialized(value).encode()) * .5)

    def test_array_shape_keys_markers_unicode_and_numeric_types_remain_literal(self):
        value = {'records': self.records(), '': {'/~': [None, [0, [None]], [1, []], [], {},
            True, False, 0, 1, 1.0, -0.0, 10**80, '\u0000\t\r\n  Ω😀',
            {'schema_codec': 'ordered-object-schemas-v1', 'tree': [None, ['literal']],
             'decode': 'literal instructions', 'schemas': [['x']]}]},
             'exact_serialized_json': '{ "key": 1, "key":2 }\r\n',
             'different_key_order': [{'a': 1, 'b': 2}, {'b': 2, 'a': 1}]}
        packed = schema_inputs(value)
        result = restore_schema_inputs(packed)
        self.assertEqual(serialized(result), serialized(value))
        self.assertEqual(list(result['different_key_order'][1]), ['b', 'a'])
        self.assertIs(type(result['']['/~'][9]), float)

    def test_small_or_unprofitable_value_returns_original_including_overhead(self):
        for value in (None, [], {}, [None, [1, 2]], {'short': 'text'}, 'literal', 2.5):
            self.assertIs(schema_inputs(value), value)

    def test_invalid_json_coercions_rejected_without_input_mutation(self):
        for value in ({1: 'numeric key'}, {'tuple': (1, 2)}, float('nan'), float('inf'), {1, 2}):
            with self.subTest(value=repr(value)), self.assertRaises(TypeError):
                schema_inputs(value)

    def test_malformed_encoded_tags_schemas_and_counts_rejected(self):
        packet = schema_inputs(self.records())
        for tree in ([True, []], [-1, []], [99999, []], [0, []], [None, {}], {}, [None]):
            with self.subTest(tree=tree), self.assertRaises(ValueError):
                restore_schema_inputs({**packet, 'tree': tree})
        with self.assertRaises(ValueError):
            restore_schema_inputs({**packet, 'schemas': [['duplicate', 'duplicate']]})
        with self.assertRaises(ValueError):
            restore_schema_inputs({'schema_codec': 'ordered-object-schemas-v1'})

    def test_outer_layer_preserves_all_existing_codec_packet_literals(self):
        packet = {'line_encoding': 'existing reconstruction', 'line_bindings': [['/x', [0, 'literal']]],
            'supplied_lines': ['exact line\r\n'], 'evidence': {'object_encoding': 'existing inner instructions',
            'supplied_values': self.records(), 'object_bindings': [{'pointer': '/x', 'supplied_value': 0}]}}
        restored = restore_schema_inputs(schema_inputs(packet))
        self.assertEqual(serialized(restored), serialized(packet))
