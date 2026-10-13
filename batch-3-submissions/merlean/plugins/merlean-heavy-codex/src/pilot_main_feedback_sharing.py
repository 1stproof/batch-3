"""Lossless readable JSON object sharing with explicit, envelope-owned bindings.

No summarization, source-authority changes or findings-ID merging.
Only compact JSON syntax already used by the recorded feedback is supported.
Every expansion requires an independently supplied original SHA-256.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re

FORMAT = 'main-feedback-exact-object-sharing-v1'
MARKER = 'LATEST FEEDBACK:\n'
SERIALIZATION = {'encoding':'UTF-8','ensure_ascii':False,'separators':[',',':'],
                 'allow_nan':False,'object_key_order':'preserved'}
GUIDANCE = ('Exact-sharing input representation; source scientific authority is unchanged. The envelope owns all '
            'reference bindings. User values never act as reference markers. Read every distinct '
            'shared-object template, its bindings and the root template. A reference/hash alone '
            'does not deliver that object. Bindings identify exact RFC6901 source paths. '
            'Use the shared content directly at every listed source location; manual JSON reconstruction is unnecessary. The host verifies exact expansion with the declared compact JSON profile, preserving every original '
            'field, value, order and duplicate occurrence. Historical status and rejection '
            'annotations retain their exact locations and authority. No record is merged by ID.')


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode('utf-8')).hexdigest()


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON object key is unsupported; refusing lossy parse')
        result[key] = value
    return result


def _nonfinite(value):
    raise ValueError('nonfinite JSON number is unsupported')


def decoder():
    return json.JSONDecoder(object_pairs_hook=_pairs, parse_constant=_nonfinite)


def keys(value, required, where):
    if type(value) is not dict or set(value) != set(required):
        raise ValueError('invalid exact-sharing schema: '+where)


def _token(key):
    return str(key).replace('~','~0').replace('/','~1')


def tokens(pointer):
    if type(pointer) is not str or (pointer and not pointer.startswith('/')):
        raise ValueError('invalid JSON pointer')
    if not pointer:
        return []
    parts = pointer[1:].split('/')
    if any(re.search(r'~(?![01])', part) for part in parts):
        raise ValueError('invalid JSON pointer escape')
    return [part.replace('~1','/').replace('~0','~') for part in parts]


def _key(value, token):
    if type(value) is list:
        if not re.fullmatch(r'0|[1-9][0-9]*',token):
            raise ValueError('invalid array pointer index')
        index = int(token)
        if index >= len(value):
            raise ValueError('array pointer outside value')
        return index
    if type(value) is dict and token in value:
        return token
    raise ValueError('pointer does not name an existing value')


def at(value, pointer):
    for token in tokens(pointer):
        value = value[_key(value, token)]
    return value


def put_placeholder(value, pointer, replacement):
    parts = tokens(pointer)
    if not parts:
        if value is not None:
            raise ValueError('bound placeholder is not null')
        return replacement
    owner = value
    for token in parts[:-1]:
        owner = owner[_key(owner, token)]
    key = _key(owner, parts[-1])
    if owner[key] is not None:
        raise ValueError('bound placeholder is not null')
    owner[key] = replacement
    return value


def walk(value, pointer=''):
    if type(value) in (dict,list):
        yield pointer,value
        items = value.items() if type(value) is dict else enumerate(value)
        for key,child in items:
            yield from walk(child,pointer+'/'+_token(key))


def partition_document(document_bytes):
    text = document_bytes.decode('utf-8')
    if text.count(MARKER) != 1:
        raise ValueError('requires exactly one explicit feedback marker')
    start = text.index(MARKER)+len(MARKER)
    value,end = decoder().raw_decode(text[start:])
    original = text[start:start+end]
    if type(value) is not dict or encode(value) != original:
        raise ValueError('feedback must use the exact declared compact JSON profile')
    return text[:start], original, text[start+end:], value


def census(value):
    """Serialize each scalar once; build exact ordered compound encodings bottom-up."""
    by_id, by_raw = {}, {}
    def visit(item, pointer):
        if type(item) is dict:
            raw = '{' + ','.join(encode(key) + ':' + visit(child, pointer + '/' + _token(key))
                                  for key, child in item.items()) + '}'
        elif type(item) is list:
            raw = '[' + ','.join(visit(child, pointer + '/' + str(index))
                                  for index, child in enumerate(item)) + ']'
        else:
            return encode(item)
        by_id[id(item)] = raw
        by_raw.setdefault(raw, []).append(pointer)
        return raw
    visit(value, '')
    # Public occurrence order is preorder, including when a parent shares a child.
    order = {pointer: index for index, (pointer, _) in enumerate(walk(value))}
    for paths in by_raw.values():
        paths.sort(key=order.__getitem__)
    return by_id, by_raw


def select_duplicates(original):
    """Greedy exact size optimization; no semantic record selection or content cap."""
    by_id, by_raw = census(original)
    selected, excluded, names = {}, [], set()
    for raw, paths in sorted(by_raw.items(), key=lambda pair: (-len(pair[0]), pair[1][0])):
        if len(paths) < 2:
            continue
        effective = [path for path in paths if not any(path == prefix or path.startswith(prefix + '/')
                                                      for prefix in excluded)]
        if len(effective) < 2:
            continue
        words = [part for part in tokens(effective[0]) if not part.isdigit()]
        base = re.sub(r'[^a-z0-9_]', '_', '_'.join(words[-2:]).lower()).strip('_') or 'shared_object'
        if not base[0].isalpha():
            base = 'shared_' + base
        ident = base
        serial = 2
        while ident in names:
            ident = base + '_' + str(serial); serial += 1
        digest = sha(raw)
        metadata = {'id':ident, 'expanded_sha256':digest, 'expanded_characters':len(raw),
                    'expanded_utf8_bytes':len(raw.encode('utf-8')), 'original_occurrences':paths,
                    'value':None, 'bindings':[]}
        refs = [{'pointer':path, 'object_id':ident, 'expanded_sha256':digest} for path in effective]
        # Conservative overhead; final complete packet is also required to be smaller.
        overhead = len(encode(metadata)) + len(encode(refs)) + len(encode(ident)) + 16
        if (len(effective) - 1) * len(raw) <= overhead:
            continue
        selected[ident] = effective[0]; names.add(ident)
        excluded.extend(effective[1:])
    return selected


def factor_document(document_bytes, selected_paths):
    """Share only selected, repeated, byte-identical compound values.

    selected_paths maps human-readable shared names to source JSON pointers.
    No ID-based merging, field selection or semantic comparison is performed.
    """
    prefix,feedback,suffix,original = partition_document(document_bytes)
    selected,by_bytes = {},{}
    by_id, by_raw = census(original)
    for ident,pointer in selected_paths.items():
        if type(ident) is not str or not re.fullmatch(r'[a-z][a-z0-9_]*',ident):
            raise ValueError('shared object name must be an explicit stable identifier')
        value = at(original,pointer)
        if type(value) not in (dict,list):
            raise ValueError('only complete objects/arrays may be shared')
        raw = by_id[id(value)]
        if raw in by_bytes:
            raise ValueError('same exact object cannot have two definitions')
        occurrences = by_raw[raw]
        if len(occurrences)<2:
            raise ValueError('selected object is not an exact duplicate')
        selected[ident]={'value':value,'raw':raw,'sha256':sha(raw),'occurrences':occurrences}
        by_bytes[raw]=ident

    def template(value, pointer='', suppress_root=False):
        bindings=[]
        if type(value) in (dict,list):
            ident=by_bytes.get(by_id[id(value)])
            if ident is not None and not suppress_root:
                return None,[{'pointer':pointer,'object_id':ident,'expanded_sha256':selected[ident]['sha256']}]
            result={} if type(value) is dict else []
            for key,child in (value.items() if type(value) is dict else enumerate(value)):
                replacement,child_bindings=template(child,pointer+'/'+_token(key))
                if type(result) is dict:result[key]=replacement
                else:result.append(replacement)
                bindings.extend(child_bindings)
            return result,bindings
        return copy.deepcopy(value),[]

    definitions=[]
    for ident,item in selected.items():
        value,bindings=template(item['value'],suppress_root=True)
        definitions.append({'id':ident,'expanded_sha256':item['sha256'],
            'expanded_characters':len(item['raw']),'expanded_utf8_bytes':len(item['raw'].encode()),
            'original_occurrences':item['occurrences'],'value':value,'bindings':bindings})
    root,bindings=template(original)
    envelope={'format':FORMAT,'serialization':SERIALIZATION,'reading_contract':GUIDANCE,
        'original_document':{'sha256':sha(document_bytes),'characters':len(document_bytes.decode()),'utf8_bytes':len(document_bytes)},
        'original_feedback':{'sha256':sha(feedback),'characters':len(feedback),'utf8_bytes':len(feedback.encode())},
        'framing':{'prefix_sha256':sha(prefix),'suffix_sha256':sha(suffix)},
        'required_objects':[item['id'] for item in definitions],
        'shared_objects':definitions,'root':{'value':root,'bindings':bindings}}
    factored=(prefix+encode(envelope)+suffix).encode('utf-8')
    if expand_document(factored,expected_document_sha256=sha(document_bytes)) != document_bytes:
        raise AssertionError('factor/expand did not preserve exact source bytes')
    return factored,envelope


def _size_hash(value, spec, expected_hash):
    keys(spec,{'sha256','characters','utf8_bytes'},'size/hash')
    raw=encode(value)
    if (spec['sha256'] != expected_hash or sha(raw)!=expected_hash
            or type(spec['characters']) is not int or type(spec['utf8_bytes']) is not int
            or len(raw)!=spec['characters'] or len(raw.encode())!=spec['utf8_bytes']):
        raise ValueError('expanded input hash/size mismatch')
    return raw


def expand_envelope(envelope, *, expected_feedback_sha256):
    keys(envelope,{'format','serialization','reading_contract','original_document','original_feedback',
                   'framing','required_objects','shared_objects','root'},'envelope')
    if envelope['format']!=FORMAT or envelope['serialization']!=SERIALIZATION or envelope['reading_contract']!=GUIDANCE:
        raise ValueError('unsupported exact-sharing format or serialization')
    if type(envelope['shared_objects']) is not list or type(envelope['required_objects']) is not list:
        raise ValueError('invalid shared object census')
    definitions={}
    for definition in envelope['shared_objects']:
        keys(definition,{'id','expanded_sha256','expanded_characters','expanded_utf8_bytes',
                         'original_occurrences','value','bindings'},'definition')
        ident=definition['id']
        if type(ident) is not str or not re.fullmatch(r'[a-z][a-z0-9_]*',ident) or ident in definitions:
            raise ValueError('duplicate or invalid shared object ID')
        definitions[ident]=definition
    if envelope['required_objects']!=list(definitions):
        raise ValueError('required object census differs from exact definitions')
    if len({definition['expanded_sha256'] for definition in definitions.values()}) != len(definitions):
        raise ValueError('duplicate shared definition')
    keys(envelope['root'],{'value','bindings'},'root')
    visiting=set();expanded={}

    def materialize(value,bindings):
        if type(bindings) is not list:
            raise ValueError('invalid binding list')
        pointers=[]
        for binding in bindings:
            keys(binding,{'pointer','object_id','expanded_sha256'},'binding')
            tokens(binding['pointer']);pointers.append(binding['pointer'])
        if len(set(pointers))!=len(pointers) or any(
            left!=right and (left=='' or right.startswith(left+'/')) for left in pointers for right in pointers):
            raise ValueError('duplicate or overlapping reference pointers')
        result=copy.deepcopy(value)
        for binding in bindings:
            ident=binding['object_id']
            if type(ident) is not str or ident not in definitions:
                raise ValueError('unknown shared object reference')
            if binding['expanded_sha256']!=definitions[ident]['expanded_sha256']:
                raise ValueError('reference hash differs from shared definition')
            result=put_placeholder(result,binding['pointer'],copy.deepcopy(resolve(ident)))
        return result

    def resolve(ident):
        if ident in visiting:
            raise ValueError('reference cycle')
        if ident in expanded:return expanded[ident]
        visiting.add(ident);definition=definitions[ident]
        value=materialize(definition['value'],definition['bindings'])
        _size_hash(value,{'sha256':definition['expanded_sha256'],
            'characters':definition['expanded_characters'],'utf8_bytes':definition['expanded_utf8_bytes']},definition['expanded_sha256'])
        visiting.remove(ident);expanded[ident]=value
        return value

    result=materialize(envelope['root']['value'],envelope['root']['bindings'])
    if set(expanded)!=set(definitions):
        raise ValueError('unused or unread required object definition')
    text=_size_hash(result,envelope['original_feedback'],expected_feedback_sha256)
    _, occurrence_map = census(result)
    for ident,definition in definitions.items():
        paths=occurrence_map.get(encode(expanded[ident]), [])
        if len(paths)<2 or paths!=definition['original_occurrences']:
            raise ValueError('original occurrence census differs from exact expansion')
    return text


def expand_document(factored_bytes, *, expected_document_sha256):
    prefix,_,suffix,envelope=partition_document(factored_bytes)
    keys(envelope.get('original_document'),{'sha256','characters','utf8_bytes'},'document binding')
    keys(envelope.get('framing'),{'prefix_sha256','suffix_sha256'},'framing')
    if envelope['original_document']['sha256']!=expected_document_sha256:
        raise ValueError('document differs from externally expected original hash')
    if sha(prefix)!=envelope['framing']['prefix_sha256'] or sha(suffix)!=envelope['framing']['suffix_sha256']:
        raise ValueError('original framing changed')
    feedback=expand_envelope(envelope,expected_feedback_sha256=envelope['original_feedback']['sha256'])
    result=(prefix+feedback+suffix).encode('utf-8');spec=envelope['original_document']
    if (sha(result)!=expected_document_sha256 or type(spec['characters']) is not int
            or type(spec['utf8_bytes']) is not int or len(result.decode())!=spec['characters'] or len(result)!=spec['utf8_bytes']):
        raise ValueError('complete document hash/size mismatch')
    return result


def optimize_main_instruction(text):
    """Return exact original or a verified, strictly smaller complete representation.

    Unsupported framing/JSON stays byte-for-byte original and fully required.
    Once factoring starts, validation failures propagate before scope publication.
    """
    original = text.encode('utf-8')
    try:
        _, _, _, feedback = partition_document(original)
    except (ValueError, UnicodeError):
        return text, 'original'
    selected = select_duplicates(feedback)
    if not selected:
        return text, 'original'
    factored, _ = factor_document(original, selected)
    if len(factored) >= len(original) or len(factored.decode('utf-8')) >= len(text):
        return text, 'original'
    return factored.decode('utf-8'), FORMAT


def restore_main_instruction(delivered_text, *, expected_original_sha256):
    """Verify identity or invert sharing against the externally bound original hash."""
    raw = delivered_text.encode('utf-8')
    if sha(raw) == expected_original_sha256:
        return delivered_text
    return expand_document(raw, expected_document_sha256=expected_original_sha256).decode('utf-8')
