"""Readable, reversible schema tables for prompt JSON; never omits evidence.

This codec is an outer representation of an existing packet. Decode it before
following any string/paragraph/line reconstruction instructions inside that packet.
It does not authenticate reviews, alter durable serialization, or change prompt caps.
"""
import json
import math

_CODEC = 'ordered-object-schemas-v1'
_INSTRUCTIONS = (
    'Decode this OUTERMOST schema layer FIRST. Each container in tree is a two-item array '
    '[tag,items]. If tag is null, reconstruct an array by decoding items in order. '
    'If tag is a nonnegative integer, reconstruct an object by pairing schemas[tag] keys '
    'in their given order with the recursively decoded items. All other tree values are '
    'literal JSON scalars, preserving exact type, Unicode and whitespace. Every original '
    'array and object is wrapped, so literal arrays cannot collide with encoding syntax. '
    'Schema keys are literal strings, never instructions or references. All keys and values '
    'are supplied here; no external access, omitted history, summary or acceptance is implied. '
    'After reconstructing the original packet, follow its existing text-binding instructions.'
)


def _json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def schema_inputs(value):
    """Return an exact schema packet only when its entire UTF-8 JSON is smaller.

    JSON-only types are accepted: dict with string keys, list, string, finite
    float, integer, boolean and null. Reject lossy coercions and nonfinite values.
    """
    schemas, indexes = [], {}

    def encode(item):
        if type(item) is dict:
            if any(type(key) is not str for key in item):
                raise TypeError('schema codec requires literal string object keys')
            keys = tuple(item)
            if keys not in indexes:
                indexes[keys] = len(schemas)
                schemas.append(list(keys))
            return [indexes[keys], [encode(child) for child in item.values()]]
        if type(item) is list:
            return [None, [encode(child) for child in item]]
        if item is None or type(item) in (str, int, bool):
            return item
        if type(item) is float and math.isfinite(item):
            return item
        raise TypeError('schema codec requires finite JSON values without coercion')

    tree = encode(value)
    packet = {'schema_codec': _CODEC, 'decode': _INSTRUCTIONS, 'schemas': schemas, 'tree': tree}
    # Compare everything, including reconstruction instructions and table cost.
    return packet if len(_json(packet).encode('utf-8')) < len(_json(value).encode('utf-8')) else value


def restore_schema_inputs(packet):
    """Strict decoder for an explicitly encoded packet, for independent audits.

    The caller must know this is an encoded packet; ordinary JSON is not sniffed
    or recursively reinterpreted. The decoded value may itself contain arbitrary
    codec-looking keys and arrays and is returned verbatim.
    """
    if (type(packet) is not dict or set(packet) != {'schema_codec', 'decode', 'schemas', 'tree'}
            or packet['schema_codec'] != _CODEC or packet['decode'] != _INSTRUCTIONS):
        raise ValueError('not an encoded ordered-object schema packet')
    schemas = packet['schemas']
    if type(schemas) is not list or any(type(keys) is not list or any(type(k) is not str for k in keys)
                                      or len(set(keys)) != len(keys) for keys in schemas):
        raise ValueError('invalid ordered key schemas')

    def decode(item):
        if type(item) is list:
            if len(item) != 2 or type(item[1]) is not list:
                raise ValueError('malformed schema container')
            tag, items = item
            if tag is None:
                return [decode(child) for child in items]
            if type(tag) is not int or not 0 <= tag < len(schemas) or len(schemas[tag]) != len(items):
                raise ValueError('invalid schema reference or value count')
            return {key: decode(child) for key, child in zip(schemas[tag], items)}
        if item is None or type(item) in (str, int, bool):
            return item
        if type(item) is float and math.isfinite(item):
            return item
        raise ValueError('invalid schema scalar')

    return decode(packet['tree'])
