"""Lossless immutable main-task delivery through the existing document capability.

The original root retains exact task bytes; the required delivery root may share
byte-identical objects through an exactly reversible, fully required envelope.
Chunks are transport partitions, never summaries, evidence selection or a total cap.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from pilot_document_tools import regular_bytes
from pilot_main_feedback_sharing import optimize_main_instruction, restore_main_instruction

READ_CHUNK_CHARACTERS = 16000
TASK_ID = 'main-task'
INDEX_ID = 'main-task-index'
ORIGINAL_ID = 'main-task-original'


def _freeze(root, text, media_type='text/plain'):
    data = text.encode('utf-8')
    sha = hashlib.sha256(data).hexdigest()
    path = root / (sha + '.txt')
    if path.exists():
        if regular_bytes(path) != data:
            raise ValueError('immutable main input changed')
    else:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    return {'path': str(path), 'sha256': sha, 'media_type': media_type}


def build_main_inputs(instruction, *, artifact_root):
    """Archive the complete exact instruction and expose a constant-size locator.

    All chunks and their hashes remain in the host-created scope. The model reads
    the index and complete chunks, or the complete root. Only actual full delivery
    of the root (including verified chunk coverage) can admit the returned answer.
    """
    if not isinstance(instruction, str) or not instruction:
        raise ValueError('main task must be nonempty exact text')
    root = Path(artifact_root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    original = instruction
    instruction, representation = optimize_main_instruction(original)
    original_sha = hashlib.sha256(original.encode('utf-8')).hexdigest()
    if restore_main_instruction(instruction, expected_original_sha256=original_sha) != original:
        raise ValueError('main feedback representation does not reconstruct exact original task')
    artifacts = {ORIGINAL_ID: _freeze(root, original), TASK_ID: _freeze(root, instruction)}
    original_binding = {'artifact_id': ORIGINAL_ID, 'sha256': original_sha,
                        'characters': len(original), 'utf8_bytes': len(original.encode('utf-8'))}
    chunks = []
    for start in range(0, len(instruction), READ_CHUNK_CHARACTERS):
        end = min(start + READ_CHUNK_CHARACTERS, len(instruction))
        ident = f'{TASK_ID}::chunk:{start}:{end}'
        artifacts[ident] = _freeze(root, instruction[start:end])
        chunks.append({'artifact_id': ident, 'sha256': artifacts[ident]['sha256'],
                       'start': start, 'end': end})
    index = {'parent_artifact_id': TASK_ID, 'parent_sha256': artifacts[TASK_ID]['sha256'],
             'characters': len(instruction), 'utf8_bytes': len(instruction.encode('utf-8')),
             'chunks': chunks, 'representation': representation, 'original': original_binding,
             'authority': 'complete lossless task representation; no proof acceptance'}
    artifacts[INDEX_ID] = _freeze(root, json.dumps(index, ensure_ascii=False, indent=2) + '\n',
                                 'application/json')
    locator = {'artifact_id': TASK_ID, 'sha256': artifacts[TASK_ID]['sha256'],
               'characters': index['characters'], 'utf8_bytes': index['utf8_bytes'],
               'chunk_index': {'artifact_id': INDEX_ID, 'sha256': artifacts[INDEX_ID]['sha256']},
               'chunk_count': len(chunks), 'representation': representation, 'original': original_binding}
    text = ('COMPLETE EXACT MAIN TASK AND FEEDBACK — REQUIRED DOCUMENT INPUT\n'
            'The full task instruction, response contract, exact feedback and obligations are preserved '
            'in the immutable main-task representation. Any shared objects appear once with readable names, '
            'complete original source paths and envelope-owned bindings. Read their full contents as applying '
            'at every listed original location; the host has verified exact reconstruction of main-task-original. '
            'Every distinct value, finding version, order and status remains; sharing adds no scientific authority. '
            'The original artifact is available for exact comparison, but does not replace required main-task '
            'delivery. Use the directly advertised read_artifact tool to read '
            'main-task-index by artifact_id, then read EVERY listed immutable chunk completely '
            'by its listed ID. No hash is needed; the host verifies each exact saved version. Read chunks '
            'in order. You may instead read the complete main-task root. A hash, index, prior-session '
            'memory, partial read or summary does not deliver the required task. These chunks partition '
            'every Unicode character; their size is a transport read size, never a total evidence cap. '
            'Read all required material before returning any response, including candidate_update, '
            'blocked_checkpoint, draft_checkpoint or archive_request. Follow the complete task instructions. '
            'The host rejects every response without verified complete delivery in this stage; this does '
            'not imply comprehension or mathematical acceptance. Existing proof draft read/save tools '
            'remain available. If a read fails, report the infrastructure limitation; do not claim delivery.\n'
            + json.dumps(locator, ensure_ascii=False, indent=2))
    return {'text': text, 'readonly_artifacts': artifacts,
            'required_artifact_ids': [TASK_ID], 'inline_artifact_ids': [],
            'input_sha256': artifacts[TASK_ID]['sha256'], 'original_input_sha256': original_sha,
            'representation': representation}


def require_main_delivery(scope, meta):
    """Fail closed before main response application or controller acknowledgment."""
    required = scope['required_artifact_ids']
    audit = meta.get('document_audit', {})
    if (meta.get('status') != 'completed' or audit.get('status') != 'PASS'
            or audit.get('required_material_delivered') is not True
            or any(audit.get('required_artifact_coverage', {}).get(key) is not True for key in required)):
        raise ValueError('main response withheld: exact required task/feedback delivery is incomplete or unverified')
