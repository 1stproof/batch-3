"""Lossless in-prompt sharing of repeated review structures and scalar text.

No evidence selection, summarization, authority or durable hash changes. The
outer layer is decoded before existing inner evidence-codec instructions. Candidate
segmentations use literal punctuation or repeated spans of regex-delimited words.
Every span is sliced from the original string by character offsets; whitespace,
delimiters, Unicode and scalar types are preserved without normalization. The
smallest complete representation wins, including all tables and instructions.
Optional dynamic programming estimates shared span storage before that exact
comparison; both word and lexical tokenizations retain original character offsets.
"""
import json
import heapq
import math
import re

FORMAT = 'ordered-schema-shared-values-v1'
INSTRUCTIONS = (
    'Decode this outer layer FIRST. Decode tree recursively: a JSON scalar is literal; '
    '[null,items] is an array of decoded items; [integer,items] is an object whose ordered '
    'keys are schemas[integer] and whose corresponding values are decoded items. '
    '["text",items] is the exact concatenation (no separator) of decoded string items. '
    '["ref",integer] supplies the exact decoded shared_values[integer]. Decode dictionary '
    'entries in index order: a dictionary entry may refer only to earlier entries. '
    'All original containers are explicitly tagged, including arrays that resemble these '
    'tags; schema keys and scalar strings are always literal. Preserve every type, key '
    'order, array order, Unicode character and whitespace character. All distinct evidence '
    'is present here; no file access or missing historical context is required. After '
    'reconstructing the complete original packet, follow any existing inner codec instructions. '
    'These representations neither summarize evidence nor grant any research acceptance.'
)


def _json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def _wire_size(node, *, flat_costs=False, positive_costs=False):
    """Price existing v1/v3/v4 syntax exactly; this is not another wire format."""
    if not flat_costs:
        return len(_json(node).encode())
    def flatten(item):
        if type(item) is list:
            tag, values = item
            if tag == 'ref':
                return values if positive_costs else -values-1
            return [-1 if tag == 'text' else tag, *[flatten(child) for child in values]]
        if type(item) is int and (item >= 0 if positive_costs else item < 0):
            return [-2,item]
        return item
    return len(_json(flatten(node)).encode())


def _candidate(value, threshold, *, clause_boundaries=False, phrase_words=None, minimum_chunk=48, unique_strings=False, lexical_words=False, savings_selection=False, reference_cost=7, flat_costs=False, positive_costs=False):
    # Score proposed text/intern substitutions using their eventual wire syntax.
    # The final complete packet comparison still accounts for every table/tag.
    def wire_size(node):
        return _wire_size(node, flat_costs=flat_costs, positive_costs=positive_costs)
    counts, chunks = {}, {}
    phrases, split_cache = {}, {}
    phrase_sizes = sorted(phrase_words if isinstance(phrase_words, tuple) else (phrase_words,), reverse=True) if phrase_words is not None else []
    if phrase_words is not None:
        seen_text = set()
        def count_phrases(item):
            if type(item) is str:
                if unique_strings and item in seen_text:
                    return
                seen_text.add(item)
                words = list(re.finditer(r'\w+|[^\w]+' if lexical_words else r'\S+\s*', item))
                for size in phrase_sizes:
                    for i in range(len(words) - size + 1):
                        phrase = item[words[i].start():words[i + size - 1].end()]
                        if len(phrase) >= minimum_chunk:
                            phrases[phrase] = phrases.get(phrase, 0) + 1
            elif type(item) is dict:
                for child in item.values(): count_phrases(child)
            elif type(item) is list:
                for child in item: count_phrases(child)
        count_phrases(value)
    def split_text(text):
        if phrase_words is not None:
            if text in split_cache:
                return split_cache[text]
            words = list(re.finditer(r'\w+|[^\w]+' if lexical_words else r'\S+\s*', text))
            result, end, i = [], 0, 0
            if savings_selection:
                costs = [0.0]*(len(words)+1); choices = [1]*len(words)
                for index in range(len(words)-1,-1,-1):
                    costs[index] = len(_json(words[index].group()).encode())-2 + costs[index+1]
                    for span in phrase_sizes:
                        if index+span>len(words): continue
                        literal = text[words[index].start():words[index+span-1].end()]
                        count = phrases.get(literal,0)
                        if count<2: continue
                        cost = (len(_json(literal).encode())+1)/count + reference_cost + costs[index+span]
                        if cost<costs[index]: costs[index],choices[index]=cost,span
                while i<len(words):
                    stop=words[i+choices[i]-1].end();start=words[i].start()
                    if start>end: result.append(text[end:start])
                    result.append(text[start:stop]);end=stop;i+=choices[i]
                if end<len(text): result.append(text[end:])
                split_cache[text]=result
                return result
            while i + min(phrase_sizes) <= len(words):
                size = next((size for size in phrase_sizes if i + size <= len(words)
                    and phrases.get(text[words[i].start():words[i + size - 1].end()], 0) > 1), None)
                if size is not None:
                    start, stop = words[i].start(), words[i + size - 1].end()
                    if start > end:
                        result.append(text[end:start])
                    result.append(text[start:stop])
                    end, i = stop, i + size
                else:
                    i += 1
            if end < len(text):
                result.append(text[end:])
            split_cache[text] = result
            return result

        return re.split(r'(?<=[.!?;,:])(?=\s)|(?<=\n)' if clause_boundaries else r'(?<=[.!?;])(?=\s)|(?<=\n)', text)
    def count_chunks(item):
        if type(item) is str:
            for chunk in split_text(item):
                if len(chunk) >= minimum_chunk:
                    chunks[chunk] = chunks.get(chunk, 0) + 1
        elif type(item) is dict:
            for child in item.values(): count_chunks(child)
        elif type(item) is list:
            for child in item: count_chunks(child)
    count_chunks(value)
    def census(item):
        if type(item) is dict:
            if any(type(key) is not str for key in item):
                raise TypeError('review packing requires string object keys')
            for child in item.values():
                census(child)
        elif type(item) is list:
            for child in item:
                census(child)
        elif not (item is None or type(item) in (str, int, bool)
                  or (type(item) is float and math.isfinite(item))):
            raise TypeError('review packing requires finite JSON values without coercion')
        if type(item) in (dict, list, str):
            key = _json(item)
            if len(key.encode('utf-8')) >= threshold:
                counts[key] = counts.get(key, 0) + 1
    census(value)
    schemas, schema_ids, shared, shared_ids = [], {}, [], {}
    def encode(item):
        key = _json(item) if type(item) in (dict, list, str) else None
        repeated = counts.get(key, 0) > 1
        if repeated and key in shared_ids:
            return ['ref', shared_ids[key]]
        if type(item) is dict:
            keys = tuple(item)
            if keys not in schema_ids:
                schema_ids[keys] = len(schemas)
                schemas.append(list(keys))
            result = [schema_ids[keys], [encode(child) for child in item.values()]]
        elif type(item) is list:
            result = [None, [encode(child) for child in item]]
        elif type(item) is str:
            parts = []
            for chunk in split_text(item):
                if chunks.get(chunk, 0) > 1:
                    chunk_key = ('chunk', chunk)
                    if chunk_key not in shared_ids:
                        shared_ids[chunk_key] = len(shared)
                        shared.append(chunk)
                    parts.append(['ref', shared_ids[chunk_key]])
                elif parts and type(parts[-1]) is str:
                    parts[-1] += chunk
                else:
                    parts.append(chunk)
            candidate = ['text', parts]
            result = candidate if wire_size(candidate) < wire_size(item) else item
        else:
            result = item
        if repeated:
            # Count table storage and all references, rather than sharing tiny
            # values just because they occur often. Children already shared.
            reference = ['ref', len(shared)]
            occurrences = counts[key]
            if wire_size(result) * (occurrences - 1) > wire_size(reference) * occurrences + 1:
                shared_ids[key] = len(shared)
                shared.append(result)
                return reference
        return result
    tree = encode(value)
    used = set()
    def collect(node):
        if type(node) is list:
            if len(node) == 2 and node[0] == 'ref':
                index = node[1]
                if index not in used:
                    used.add(index)
                    collect(shared[index])
            else:
                for child in node[1]: collect(child)
    collect(tree)
    ordered = sorted(used)
    remap = {old: new for new, old in enumerate(ordered)}
    def renumber(node):
        if type(node) is list:
            if len(node) == 2 and node[0] == 'ref':
                return ['ref', remap[node[1]]]
            return [node[0], [renumber(child) for child in node[1]]]
        return node
    tree = renumber(tree)
    shared = [renumber(shared[index]) for index in ordered]
    return {'review_packet_codec': FORMAT, 'decode': INSTRUCTIONS,
            'schemas': schemas, 'shared_values': shared, 'tree': tree}


COMPACT_FORMAT = 'ordered-schema-shared-values-v2'
COMPACT_INSTRUCTIONS = (
    'Decode this outer layer FIRST. A JSON scalar is literal. A one-item array [n] with '
    'negative integer n is the exact decoded shared_values[-n-1]. A two-item array '
    '[-1,items] concatenates decoded string items with NO separator. [null,items] is '
    'an array of decoded items. [nonnegative_integer,items] is an object pairing the '
    'ordered schemas[integer] keys with decoded items. Decode shared_values in index '
    'order; references may point only to earlier decoded entries. All original '
    'containers are explicitly wrapped, including arrays resembling tags. Schema keys '
    'and scalar strings are literal. Preserve every type, key order, array order, '
    'Unicode and whitespace character. Every distinct value is supplied here. After '
    'exact reconstruction, follow any inner codec instructions. No evidence is omitted '
    'or summarized and no research or acceptance authority is granted.'
)


def compact_packet(packet):
    """Only shorten unambiguous container tags; every literal and table is retained."""
    def transform(node):
        if type(node) is list:
            tag, items = node
            if tag == 'ref':
                return [-items - 1]
            return [-1 if tag == 'text' else tag, [transform(child) for child in items]]
        return node
    return {'review_packet_codec': COMPACT_FORMAT, 'decode': COMPACT_INSTRUCTIONS,
            'schemas': packet['schemas'], 'shared_values': [transform(v) for v in packet['shared_values']],
            'tree': transform(packet['tree'])}


FLAT_FORMAT = 'ordered-schema-shared-values-v3'
FLAT_INSTRUCTIONS = (
    'Decode this outer layer FIRST. A negative INTEGER n references the exact decoded '
    'shared_values[-n-1]. The two-item array [-2,n] escapes a literal negative INTEGER. '
    'All other JSON scalars are literal, including negative floats and -0.0. '
    'Every other array is tagged: [null,...items] is an array of decoded items; '
    '[nonnegative_integer,...items] is an object pairing ordered schemas[integer] keys '
    'with decoded items; [-1,...items] concatenates decoded STRING items with NO separator. '
    'Decode shared_values in index order; references may only use earlier decoded entries. '
    'All original containers are tagged, even empty arrays and arrays resembling tags. '
    'Schema keys are literal. Preserve exact types, key order, array order, Unicode and '
    'whitespace. All distinct values are supplied. Reconstruct fully before following '
    'inner codec instructions. No omission, summary or research acceptance is implied.'
)


def flat_packet(packet):
    """Flatten tags and escape the only scalar class reserved for references."""
    def transform(node):
        if type(node) is list:
            tag, items = node
            if tag == 'ref':
                return -items - 1
            return [-1 if tag == 'text' else tag, *[transform(child) for child in items]]
        if type(node) is int and node < 0:
            return [-2, node]
        return node
    return {'review_packet_codec': FLAT_FORMAT, 'decode': FLAT_INSTRUCTIONS,
            'schemas': packet['schemas'], 'shared_values': [transform(v) for v in packet['shared_values']],
            'tree': transform(packet['tree'])}


POSITIVE_FORMAT = 'ordered-schema-shared-values-v4'
POSITIVE_INSTRUCTIONS = (
    'Decode this outer layer FIRST. A nonnegative INTEGER n references the exact decoded '
    'shared_values[n]. The two-item array [-2,n] escapes a literal nonnegative INTEGER. '
    'All other JSON scalars are literal, including negative integers, all floats and booleans. '
    'Every other array is tagged: [null,...items] is an array of decoded items; '
    '[nonnegative_integer,...items] is an object pairing ordered schemas[integer] keys '
    'with decoded items; [-1,...items] concatenates decoded STRING items with NO separator. '
    'Decode shared_values in index order; references may only use earlier decoded entries. '
    'All original containers are tagged, even empty arrays and arrays resembling tags. '
    'Schema keys are literal. Preserve exact types, key order, array order, Unicode and '
    'whitespace. All distinct values are supplied. Reconstruct fully before following '
    'inner codec instructions. No omission, summary or research acceptance is implied.'
)


def positive_packet(packet):
    """Alternative reference polarity; every colliding literal integer is escaped."""
    def transform(node):
        if type(node) is list:
            tag, items = node
            if tag == 'ref':
                return items
            return [-1 if tag == 'text' else tag, *[transform(child) for child in items]]
        if type(node) is int and node >= 0:
            return [-2, node]
        return node
    return {'review_packet_codec': POSITIVE_FORMAT, 'decode': POSITIVE_INSTRUCTIONS,
            'schemas': packet['schemas'], 'shared_values': [transform(v) for v in packet['shared_values']],
            'tree': transform(packet['tree'])}


def frequency_order_packet(packet):
    """Reindex a validated v1 dictionary without changing its dependency order.

    Smaller indices go to frequently spelled references among currently available
    entries. The original index breaks ties deterministically. This is only an
    alternative representation; complete packet byte counts decide whether to use it.
    """
    if type(packet) is not dict or packet.get('review_packet_codec') != FORMAT:
        raise ValueError('frequency ordering requires a v1 packet')
    restore_review_packet(packet)
    shared = packet['shared_values']
    counts = [0] * len(shared)
    dependencies = [set() for _ in shared]
    users = [[] for _ in shared]
    def references(node):
        if type(node) is list:
            if node[0] == 'ref':
                yield node[1]
            else:
                for child in node[1]:
                    yield from references(child)
    for i, entry in enumerate(shared):
        for j in references(entry):
            counts[j] += 1
            dependencies[i].add(j)
    for j in references(packet['tree']):
        counts[j] += 1
    for i, entries in enumerate(dependencies):
        for j in entries:
            users[j].append(i)
    pending = [len(entries) for entries in dependencies]
    ready = [(-counts[i], i) for i, count in enumerate(pending) if count == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        _, i = heapq.heappop(ready)
        order.append(i)
        for user in users[i]:
            pending[user] -= 1
            if pending[user] == 0:
                heapq.heappush(ready, (-counts[user], user))
    if len(order) != len(shared):
        raise ValueError('cyclic shared dictionary')
    indices = {old: new for new, old in enumerate(order)}
    def remap(node):
        if type(node) is not list:
            return node
        if node[0] == 'ref':
            return ['ref', indices[node[1]]]
        return [node[0], [remap(child) for child in node[1]]]
    return {**packet, 'shared_values': [remap(shared[i]) for i in order], 'tree': remap(packet['tree'])}


def optimize_review_packet(value):
    """Choose smaller total UTF-8 JSON, including all dictionaries/instructions.

    Packing does not promise model-token savings; those must be measured with
    the actual tokenizer separately. Original values are never mutated.
    """
    original = len(_json(value).encode('utf-8'))
    candidates = [_candidate(value, 24), _candidate(value, 24, clause_boundaries=True),
                  _candidate(value, 24, phrase_words=4), _candidate(value, 24, phrase_words=8),
                  _candidate(value, 24, phrase_words=16),
                  _candidate(value, 24, phrase_words=(4,8,12,16,24,32,48,64,96)),
                  _candidate(value, 24, phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96), minimum_chunk=24),
                  _candidate(value, 24, phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),
                             minimum_chunk=24, unique_strings=True, savings_selection=True),
                  _candidate(value, 24, phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),
                             minimum_chunk=24, unique_strings=True, lexical_words=True, savings_selection=True),
                  _candidate(value, 4, phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),
                             minimum_chunk=4, unique_strings=True, savings_selection=True,
                             reference_cost=2, flat_costs=True),
                  _candidate(value, 24, phrase_words=(1,2,3,4,6,8,12,16,24,32,48,64,96),
                             minimum_chunk=8, unique_strings=True, lexical_words=True, savings_selection=True,
                             reference_cost=3, flat_costs=True),
                  # Additional alternative only: preserve every prior candidate. Dense
                  # short spans use the existing exact word-offset reconstruction;
                  # positive-reference pricing matches the already supported v4 wire.
                  _candidate(value, 2, phrase_words=tuple(range(1,17))+(24,32,48,64,96),
                             minimum_chunk=2, unique_strings=True, savings_selection=True,
                             reference_cost=1, flat_costs=True, positive_costs=True)]
    candidates += [frequency_order_packet(item) for item in candidates]
    candidates += ([compact_packet(item) for item in candidates] + [flat_packet(item) for item in candidates]
                   + [positive_packet(item) for item in candidates])
    candidate = min(candidates, key=lambda item: len(_json(item).encode('utf-8')))
    return candidate if len(_json(candidate).encode('utf-8')) < original else value


def restore_review_packet(packet):
    """Decode an explicitly known encoded packet; never sniff literal input."""
    if (type(packet) is not dict or set(packet) != {'review_packet_codec', 'decode', 'schemas', 'shared_values', 'tree'}
            or (packet['review_packet_codec'], packet['decode']) not in
                ((FORMAT, INSTRUCTIONS), (COMPACT_FORMAT, COMPACT_INSTRUCTIONS), (FLAT_FORMAT, FLAT_INSTRUCTIONS),
                 (POSITIVE_FORMAT, POSITIVE_INSTRUCTIONS))):
        raise ValueError('invalid shared review packet')
    compact = packet['review_packet_codec'] == COMPACT_FORMAT
    positive = packet['review_packet_codec'] == POSITIVE_FORMAT
    flat = packet['review_packet_codec'] in (FLAT_FORMAT, POSITIVE_FORMAT)
    schemas, shared = packet['schemas'], packet['shared_values']
    if (type(schemas) is not list or type(shared) is not list
            or any(type(keys) is not list or any(type(key) is not str for key in keys)
                   or len(set(keys)) != len(keys) for keys in schemas)):
        raise ValueError('invalid schema or shared dictionary')
    restored = []
    def decode(item):
        if flat and type(item) is int and ((item >= 0) if positive else (item < 0)):
            index = item if positive else -item - 1
            if not 0 <= index < len(restored):
                raise ValueError('forward, cyclic or invalid shared reference')
            return json.loads(_json(restored[index]))
        if type(item) is list:
            if flat:
                if not item:
                    raise ValueError('empty tagged container')
                tag, values = item[0], item[1:]
                if type(tag) is int and tag == -2:
                    if len(values) != 1 or type(values[0]) is not int or ((values[0] < 0) if positive else (values[0] >= 0)):
                        raise ValueError('invalid escaped integer')
                    return values[0]
                if type(tag) is int and tag == -1:
                    tag = 'text'
                elif tag is not None and (type(tag) is not int or tag < 0):
                    raise ValueError('invalid flat container tag')
            elif compact and len(item) == 1:
                if type(item[0]) is not int or item[0] >= 0:
                    raise ValueError('invalid compact reference')
                tag, values = 'ref', -item[0] - 1
            elif len(item) == 2:
                tag, values = item
                if compact:
                    if type(tag) is int and tag == -1:
                        tag = 'text'
                    elif tag is not None and (type(tag) is not int or tag < 0):
                        raise ValueError('invalid compact container tag')
            else:
                raise ValueError('invalid tagged container')
            if tag == 'ref':
                if type(values) is not int or not 0 <= values < len(restored):
                    raise ValueError('forward, cyclic or invalid shared reference')
                # Avoid aliasing independent input objects after reconstruction.
                return json.loads(_json(restored[values]))
            if type(values) is not list:
                raise ValueError('container values must be an array')
            if tag == 'text':
                parts = [decode(child) for child in values]
                if any(type(part) is not str for part in parts):
                    raise ValueError('text sequence must contain strings')
                return ''.join(parts)
            if tag is None:
                return [decode(child) for child in values]
            if type(tag) is not int or not 0 <= tag < len(schemas) or len(schemas[tag]) != len(values):
                raise ValueError('invalid schema tag or value count')
            return {key: decode(child) for key, child in zip(schemas[tag], values)}
        if item is None or type(item) in (str, int, bool) or (type(item) is float and math.isfinite(item)):
            return item
        raise ValueError('invalid JSON scalar')
    for value in shared:
        restored.append(decode(value))
    return decode(packet['tree'])


def efficient_review_inputs(value):
    """Keep the existing schema representation unless the new layer is smaller."""
    from review_packet_codec import schema_inputs
    legacy = schema_inputs(value)
    improved = optimize_review_packet(value)
    return improved if len(_json(improved).encode('utf-8')) < len(_json(legacy).encode('utf-8')) else legacy
