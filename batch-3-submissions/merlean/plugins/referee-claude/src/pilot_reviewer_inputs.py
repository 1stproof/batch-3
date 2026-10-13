"""Readable submitted proof plus exact current obligations and archived evidence.

The builder performs no mathematical relevance selection. Host-required evidence
IDs are explicit; every historical item remains in an immutable, readable catalog.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
from pilot_document_tools import regular_bytes, required_read_plan

HISTORY_FIELDS = ('finding_history', 'prior_triage_reassess_independently',
                  'actual_execution_evidence', 'advisory_route_portfolios', 'advisory_scope_history')
READ_CHUNK_CHARACTERS = 16000  # A read size, not a cap on retained/delivered evidence.


def exact_json(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n'


def _artifact(root, data, media_type='application/json'):
    sha = hashlib.sha256(data).hexdigest()
    path = root / (sha + '.json')
    if path.exists():
        if regular_bytes(path) != data:
            raise ValueError('immutable review evidence changed')
    else:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
    return {'path': str(path), 'sha256': sha, 'media_type': media_type}


def build_review_inputs(packet, *, proof_revision, proof_path, artifact_root, required_artifact_ids=()):
    """Return plain proof text, fixed artifact map and an explicit evidence census.

    All current candidate metadata, carried findings, premise/module obligations and
    current assessments are supplied. Historical data are archived without last-N
    selection. A required artifact must be delivered, never accepted from its hash.
    """
    candidate = packet['exact_candidate']
    proof = regular_bytes(Path(proof_path).resolve())
    if proof.decode('utf-8') != candidate['proof_markdown']:
        raise ValueError('review snapshot and current candidate proof differ')
    root = Path(artifact_root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    artifacts = {'proof': {'path': str(Path(proof_path).resolve()),
                           'sha256': hashlib.sha256(proof).hexdigest(), 'media_type': 'text/markdown'}}
    metadata = {key: value for key, value in packet.items() if key not in HISTORY_FIELDS}
    metadata['exact_candidate'] = {key: value for key, value in candidate.items() if key != 'proof_markdown'}
    # The earlier dossier's proof text is preserved as a separate historical
    # artifact; it must not masquerade as a second current proof narrative.
    dossier = metadata.get('exact_dossier')
    if isinstance(dossier, dict) and 'proof_markdown' in dossier:
        artifacts['original-dossier'] = _artifact(root, exact_json(dossier).encode())
        metadata['exact_dossier'] = {key: value for key, value in dossier.items() if key != 'proof_markdown'}
    catalog, chunk_indexes = [], {}
    for field in HISTORY_FIELDS:
        items = packet.get(field, [])
        if not isinstance(items, list):
            raise ValueError('review history must be a complete ordered list')
        if not items:
            continue
        # One full readable collection permits an efficient complete read when
        # dependency ambiguity requires it. Individual items remain addressable.
        collection_text = exact_json(items)
        artifacts[field] = _artifact(root, collection_text.encode())
        if len(collection_text) > READ_CHUNK_CHARACTERS:
            chunks = []
            for start in range(0, len(collection_text), READ_CHUNK_CHARACTERS):
                end = min(start + READ_CHUNK_CHARACTERS, len(collection_text))
                chunk_id = f'{field}::chunk:{start}:{end}'
                artifacts[chunk_id] = _artifact(root, collection_text[start:end].encode(), 'text/plain')
                chunks.append({'artifact_id': chunk_id, 'sha256': artifacts[chunk_id]['sha256'],
                               'start': start, 'end': end})
            index_id = field + '::chunks'
            artifacts[index_id] = _artifact(root, exact_json({
                'parent_artifact_id': field, 'parent_sha256': artifacts[field]['sha256'],
                'characters': len(collection_text), 'chunks': chunks,
                'authority': 'exact partition only; every needed chunk must actually be read'}).encode())
            chunk_indexes[field] = {'artifact_id': index_id, 'sha256': artifacts[index_id]['sha256'],
                                    'characters': len(collection_text), 'chunk_count': len(chunks)}
        for index, item in enumerate(items):
            ident = field + ':' + str(index)
            artifacts[ident] = _artifact(root, exact_json(item).encode())
            entry = {'artifact_id': ident, 'sha256': artifacts[ident]['sha256'],
                     'collection': field, 'index': index}
            if isinstance(item, dict):
                for key in ('historical_stage', 'historical_probe', 'session_id', 'status', 'candidate_sha256'):
                    if key in item:
                        entry[key] = item[key]
            catalog.append(entry)
    required = list(required_artifact_ids)
    if len(required) != len(set(required)) or any(key not in artifacts for key in required):
        raise ValueError('required review evidence must be in the complete artifact map')
    index = {'proof_revision': proof_revision, 'proof_sha256': artifacts['proof']['sha256'],
             'required_artifact_ids': required, 'collections': {key: value['sha256'] for key, value in artifacts.items() if ':' not in key},
             'entries': catalog,
             'chunk_indexes': chunk_indexes,
             'authority': 'historical identity only; old outputs and verdicts do not certify the submitted proof'}
    index_ref = _artifact(root, exact_json(index).encode())
    artifacts['history-index'] = index_ref
    pages = required_read_plan({'readonly_artifacts': artifacts, 'required_artifact_ids': required})
    delivery_plan = {'page_count': len(pages), 'first_call': {'tool': 'read_required_evidence', 'arguments': {'page': 0}} if pages else None, 'required_artifact_ids': required, 'characters': sum(p['end'] - p['start'] for p in pages)}
    text = ('\nREQUIRED EVIDENCE DELIVERY PLAN — COMPLETE FINITE SEQUENCE\n' + exact_json(delivery_plan) +
            'When page_count is positive, before catalog browsing read each required page directly with read_required_evidence. Start with page 0 and follow next_page until null. No hash lookup or chunk index is needed. Every page remains required; repeat an output if it was clipped. A final audit, not the next-page pointer, verifies delivery. Missing delivery permits negative findings, never positive readiness, finding resolution, certificate deselection or task approval.\n' +
            '\nSUBMITTED PROOF — COMPLETE EXACT MARKDOWN\n'
            'Revision: ' + str(proof_revision) + '\nSHA-256: ' + artifacts['proof']['sha256'] + '\n\n'
            + proof.decode('utf-8') + '\nEND OF SUBMITTED PROOF\n'
            '\nCURRENT CANDIDATE, PREMISES AND COMPLETE REQUIRED FINDINGS\n' + exact_json(metadata)
            + '\nEXACT HISTORICAL EVIDENCE ACCESS\n'
            'Use read_artifact with a listed artifact_id; no hash is needed. The host verifies the exact saved file version. It never reads arbitrary paths. '
            'Read history-index for the complete item catalog, or a full named collection below. All raw records are preserved. '
            'Required IDs must be read completely. Independently read any additional evidence needed for the proof or a finding; '
            'a hash, index or earlier favorable verdict is not evidence. Missing needed material means INCOMPLETE. '
            'Report relied-on IDs and any missing evidence; receipts establish delivery, never mathematical comprehension.\n'
            'For optional additional collections or a page-tool fallback, read the chunk index and exact immutable chunks. '
            'Complete verified chunks jointly deliver the exact collection; reading an index alone does not. '
            'These bounded reads retain every character and are not summaries or a new total evidence cap. '
            'Existing same-reviewer recovery may retain complete chunk reads, never unseen text or another reviewer verdict.\n'
            + exact_json({'history_index': {'artifact_id': 'history-index', 'sha256': index_ref['sha256']},
                          'collections': index['collections'], 'chunk_indexes': chunk_indexes,
                          'required_artifact_ids': required}))
    return {'text': text, 'readonly_artifacts': artifacts, 'required_artifact_ids': required, 'inline_artifact_ids': ['proof'],
            'proof_revision': proof_revision, 'proof_sha256': artifacts['proof']['sha256'],
            'history_index_sha256': index_ref['sha256'], 'input_sha256': hashlib.sha256(text.encode()).hexdigest()}
