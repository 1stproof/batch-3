"""Exact read-only retrieval from a validated continuation snapshot; no science authority."""
import copy
import hashlib
import json
import os
import re
import stat

FIELDS = frozenset({'current', 'dossier', 'findings', 'finding_history', 'execution_history',
    'reviewer_history', 'triage_history', 'advisory_scope_history', 'final_assessment_history',
    'local_verification_modules', 'route_scout_history'})
AUTHORITY_KEYS = frozenset({'claim_token', 'owner_key', 'token'})
KEYS = frozenset({'response_type', 'schema_version', 'checkpoint_sha256', 'checkpoint_pointer',
    'evidence_sha256', 'reason'})
GUIDANCE = '''ARCHIVE RETRIEVAL v1 (original main only): If an exact older item omitted from your
continuation packet is needed, return ONLY {response_type:"archive_request",schema_version:1,
checkpoint_sha256:"exact history_manifest.checkpoint.sha256",checkpoint_pointer:"exact indexed pointer",
evidence_sha256:"exact indexed sha256",reason:"why this existing evidence is needed"}.
Only entries marked archive_retrievable:true in the continuation history_manifest are eligible.
This reads one complete immutable historical item, never a file path, network source, current verdict,
or new candidate. Historical saved current/dossier means that checkpoint's old artifact, not today's candidate.
One retrieval round is available per main turn, followed by an ordinary candidate_update or blocked_checkpoint.
A refusal leaves all work and obligations unchanged; do not repeatedly request unavailable evidence.
Retrieval grants no task approval, review eligibility, resolved finding, Lean certificate or acceptance.
Do not hide changed proof/ledger/assumptions or new findings in a retrieval reason. No history is rewritten.'''


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def digest(value):
    return hashlib.sha256(encoded(value).encode('utf-8')).hexdigest()


def has_authority(value):
    if isinstance(value, dict):
        return any(k in AUTHORITY_KEYS or has_authority(v) for k, v in value.items())
    if isinstance(value, list):
        return any(has_authority(v) for v in value)
    return False


def entries(saved, ident):
    """Enumerate literal identities; callers never parse user-supplied JSON pointers."""
    result = []
    for field, value in saved.items():
        values = enumerate(value) if isinstance(value, list) else [(None, value)]
        for number, item in values:
            pointer = '/problems/' + ident + '/' + field + (('/' + str(number)) if number is not None else '')
            result.append({'checkpoint_pointer': pointer, 'sha256': digest(item),
                'encoded_bytes': len(encoded(item).encode('utf-8')),
                'archive_retrievable': field in FIELDS and not has_authority(item)})
    return result


def _no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('archive checkpoint contains duplicate JSON keys')
        result[key] = value
    return result


def retrieve(root, ref, ident, original_sha256, main_session, request):
    """Return a full exact item or raise a refusal; never follow model-provided paths."""
    if (not isinstance(request, dict) or set(request) != KEYS
            or request.get('response_type') != 'archive_request'
            or type(request.get('schema_version')) is not int or request['schema_version'] != 1
            or any(not isinstance(request.get(k), str) or not request[k].strip()
                   for k in KEYS - {'schema_version'})):
        raise ValueError('archive_request requires exactly the documented v1 fields')
    if (not isinstance(ref, dict) or ref.get('path') != 'continuation-checkpoint.json'
            or not isinstance(ref.get('sha256'), str)
            or request['checkpoint_sha256'] != ref['sha256']):
        raise ValueError('archive request does not bind this continuation checkpoint')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', ident):
        raise ValueError('archive problem identity is invalid')
    # The runtime root is host-owned. O_NOFOLLOW blocks replacement of its fixed file
    # by a symlink; the content hash authenticates exactly the bytes read from this fd.
    with os.fdopen(os.open(root / 'continuation-checkpoint.json', os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK), 'rb') as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise ValueError('archive checkpoint must be a regular file')
        raw = stream.read()
    if hashlib.sha256(raw).hexdigest() != ref['sha256']:
        raise ValueError('archive checkpoint bytes changed')
    checkpoint = json.loads(raw.decode('utf-8'), object_pairs_hook=_no_duplicates)
    if not isinstance(checkpoint, dict) or not isinstance(checkpoint.get('problems'), dict):
        raise ValueError('archive checkpoint requires a problem mapping')
    saved = checkpoint['problems'].get(ident)
    if (not isinstance(saved, dict) or saved.get('original_sha256') != original_sha256
            or not main_session or saved.get('main_session') != main_session):
        raise ValueError('archive original problem or original main session differs')
    manifest = {entry['checkpoint_pointer']: entry for entry in entries(saved, ident)}
    entry = manifest.get(request['checkpoint_pointer'])
    if not entry or not entry['archive_retrievable'] or entry['sha256'] != request['evidence_sha256']:
        raise ValueError('archive item is absent, unavailable, or has a different evidence hash')
    # Exact enumerated membership only: no pointer decoding, prefix matching, aliases,
    # negative indexes, nested paths, or fallback to another host file.
    for field in FIELDS:
        if field not in saved:
            continue
        values = enumerate(saved[field]) if isinstance(saved[field], list) else [(None, saved[field])]
        for number, item in values:
            pointer = '/problems/' + ident + '/' + field + (('/' + str(number)) if number is not None else '')
            if pointer != request['checkpoint_pointer']:
                continue
            if digest(item) != entry['sha256'] or len(encoded(item).encode('utf-8')) != entry['encoded_bytes']:
                raise ValueError('archive item differs from its exact manifest binding')
            return {'schema_version': 1, 'status': 'retrieved', 'problem': ident,
                'original_sha256': original_sha256, 'main_session': main_session,
                'checkpoint': copy.deepcopy(ref), 'entry': entry, 'content': copy.deepcopy(item),
                'authority': 'historical_evidence_only_no_current_candidate_or_acceptance_authority',
                'provenance': 'Exact saved ' + field + '; reports retain their historical stage/artifact applicability. '
                    'The saved current/dossier is historical, never a replacement for the live candidate. '
                    'Existing current task, finding, proof, original-scope and grade gates remain required.'}
    raise ValueError('archive manifest entry is unavailable')
