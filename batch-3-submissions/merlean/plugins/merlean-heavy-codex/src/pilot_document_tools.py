"""Fixed-document MCP bridge. Model arguments never name a filesystem path.

The host creates one immutable per-stage capability. Main may save only its own
proof draft; reviewers can read only the immutable artifacts in their capability.
Online capabilities add bounded public HTTPS source fetch/read; no arbitrary execution,
controller mutation, submission or acceptance tool exists.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

SERVER = 'merlean_documents'
NAMESPACE = 'mcp__' + SERVER
PUBLIC_TOOLS = ('fetch_public_source', 'read_public_source')
TOOLS = ('read_current_proof', 'save_proof_revision', 'read_artifact', 'read_required_evidence', *PUBLIC_TOOLS)
CHUNK_ID = re.compile(r'(.+)::chunk:(0|[1-9][0-9]*):(0|[1-9][0-9]*)\Z')


def encoded(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def regular_bytes(path):
    path = Path(path)
    if not path.is_absolute() or path.resolve() != path:
        raise ValueError('artifact path must be canonical and cannot contain symlinks')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise ValueError('artifact must be a regular file')
        with os.fdopen(fd, 'rb', closefd=False) as stream:
            return stream.read()
    finally:
        os.close(fd)


def validate_scope(scope):
    fields = {'schema_version', 'mode', 'problem_id', 'original_sha256', 'main_session',
              'store_root', 'readonly_artifacts', 'required_artifact_ids', 'inline_artifact_ids', 'producer', 'receipt_path'}
    if type(scope) is not dict or set(scope) - {'public_source_store'} != fields or (type(scope['schema_version']) is not int or scope['schema_version'] != 1):
        raise ValueError('invalid document capability schema')
    if scope['mode'] not in ('main', 'review'):
        raise ValueError('invalid document capability mode')
    for key in ('problem_id', 'original_sha256', 'main_session'):
        if type(scope[key]) is not str or not scope[key]:
            raise ValueError('invalid document identity')
    if type(scope['producer']) is not dict or set(scope['producer']) != {'stage', 'request_id', 'session_id'}:
        raise ValueError('invalid document producer')
    if scope['mode'] == 'main' and scope['producer']['session_id'] != scope['main_session']:
        raise ValueError('only the original main can edit its proof')
    for key in ('store_root', 'receipt_path'):
        path = Path(scope[key])
        if not path.is_absolute() or path.resolve() != path:
            raise ValueError('document capability paths must be canonical')
    if 'public_source_store' in scope:
        allowed_stores = {str(Path(scope['store_root']) / 'public-sources'),
                          str(Path(scope['store_root']) / 'refs' / 'public-sources')}
        if scope['public_source_store'] not in allowed_stores:
            raise ValueError('public source store must be host-derived from the document store')
        public_path = Path(scope['public_source_store'])
        if public_path.resolve() != public_path:
            raise ValueError('public source store cannot contain symlinks')
    artifacts = scope['readonly_artifacts']
    if type(artifacts) is not dict:
        raise ValueError('invalid artifact capability map')
    for ident, entry in artifacts.items():
        if type(ident) is not str or not ident or type(entry) is not dict or set(entry) != {'path', 'sha256', 'media_type'}:
            raise ValueError('invalid fixed artifact entry')
        if entry['media_type'] not in ('text/plain', 'text/markdown', 'application/json'):
            raise ValueError('unsupported artifact media type')
        if type(entry['sha256']) is not str or len(entry['sha256']) != 64:
            raise ValueError('invalid artifact hash')
        data = regular_bytes(entry['path'])
        if digest(data) != entry['sha256']:
            raise ValueError('artifact changed before capability creation')
        data.decode('utf-8')
    # A complete chunk can count toward its parent only after its exact contents,
    # character bounds and both immutable hashes have been independently checked.
    chunk_bindings(scope)
    inline = scope['inline_artifact_ids']
    if type(inline) is not list or any(type(k) is not str or k not in artifacts for k in inline):
        raise ValueError('inline artifact not in capability')
    required = scope['required_artifact_ids']
    if type(required) is not list or any(type(k) is not str or k not in artifacts for k in required):
        raise ValueError('required artifact not in capability')
    return scope


def chunk_bindings(scope):
    artifacts = scope['readonly_artifacts']
    result, texts = {}, {}
    def text(ident):
        if ident not in texts:
            entry = artifacts[ident]
            data = regular_bytes(entry['path'])
            if digest(data) != entry['sha256']:
                raise ValueError('immutable chunk or parent artifact changed')
            texts[ident] = data.decode('utf-8')
        return texts[ident]
    for ident in artifacts:
        match = CHUNK_ID.fullmatch(ident)
        if match is None:
            continue
        parent, start, end = match[1], int(match[2]), int(match[3])
        if parent not in artifacts or CHUNK_ID.fullmatch(parent):
            raise ValueError('chunk must bind an existing non-chunk parent')
        complete = text(parent)
        if not 0 <= start < end <= len(complete) or text(ident) != complete[start:end]:
            raise ValueError('chunk bounds or exact parent content differ')
        result[ident] = (parent, start, end, len(complete))
    return result


def expand_chunk_coverage(scope, coverage):
    """Union only COMPLETE delivered immutable chunks; never combine verdicts.

    Partial chunk reads cannot transfer between attempts. The same-reviewer
    recovery may retain fully delivered chunk artifacts under its existing checks.
    """
    result = dict(coverage)
    spans = {}
    for ident, (parent, start, end, length) in chunk_bindings(scope).items():
        if result.get(ident) is True:
            spans.setdefault(parent, []).append((start, end, length))
    for parent, parts in spans.items():
        end = 0
        for left, right, length in sorted(parts):
            if left <= end:
                end = max(end, right)
        if end == parts[0][2]:
            result[parent] = True
    return result


REQUIRED_PAGE_CHARACTERS = 64000  # Transport framing, never a total evidence cap.


def required_read_plan(scope):
    """Deterministic finite pages over all required bytes, without relevance filtering."""
    pages = []
    bindings = chunk_bindings(scope)
    for ident in scope['required_artifact_ids']:
        entry = scope['readonly_artifacts'][ident]
        data = regular_bytes(entry['path'])
        if digest(data) != entry['sha256']:
            raise ValueError('required immutable artifact changed')
        text = data.decode('utf-8')
        for start in range(0, max(1, len(text)), REQUIRED_PAGE_CHARACTERS):
            end = min(start + REQUIRED_PAGE_CHARACTERS, len(text))
            pages.append({'page': len(pages), 'artifact_id': ident, 'sha256': entry['sha256'],
                'start': start, 'end': end, 'characters': len(text),
                'chunk_ids': [key for key, (parent, left, right, _) in bindings.items()
                              if parent == ident and start <= left < right <= end]})
    return pages


def required_read_progress(scope, coverage):
    pages = required_read_plan(scope)
    missing = []
    bindings = chunk_bindings(scope)
    for page in pages:
        complete = coverage.get(page['artifact_id']) is True
        end = page['start']
        for ident in sorted(page['chunk_ids'], key=lambda key: bindings[key][1]):
            _, left, right, _ = bindings[ident]
            if coverage.get(ident) is True and left <= end:
                end = max(end, right)
        complete = complete or (bool(page['chunk_ids']) and end == page['end'])
        if not complete:
            missing.append(page['page'])
    return {'page_count': len(pages), 'missing_pages': missing,
            'next_page': missing[0] if missing else None,
            'required_artifact_ids': list(scope['required_artifact_ids']),
            'authority': 'verified complete delivery only; no mathematical acceptance'}


def valid_arguments(tool, arguments, mode):
    if type(arguments) is not dict or tool not in TOOLS:
        return False
    if tool == 'fetch_public_source':
        return set(arguments) == {'url'} and type(arguments['url']) is str
    if tool == 'read_public_source':
        return ('source_id' in arguments and set(arguments) <= {'source_id','member','start','end'}
                and type(arguments['source_id']) is str
                and ('member' not in arguments or type(arguments['member']) is str)
                and all(type(arguments[k]) is int and arguments[k] >= 0 for k in ('start','end') if k in arguments))
    if tool == 'read_required_evidence':
        return mode == 'review' and set(arguments) == {'page'} and type(arguments['page']) is int and arguments['page'] >= 0
    if tool == 'read_current_proof':
        return mode == 'main' and not arguments
    if tool == 'save_proof_revision':
        return (mode == 'main' and set(arguments) == {'expected_revision', 'proof_markdown'}
                and all(type(arguments[k]) is str for k in arguments))
    return ('artifact_id' in arguments and set(arguments) <= {'artifact_id', 'sha256', 'start', 'end'}
            and type(arguments['artifact_id']) is str and ('sha256' not in arguments or type(arguments['sha256']) is str)
            and all(type(arguments[key]) is int and arguments[key] >= 0 for key in ('start', 'end') if key in arguments)
            and not ('start' in arguments and 'end' in arguments and arguments['start'] > arguments['end']))


def invocation_guidance(mode, public_sources=False):
    if mode not in ('main', 'review'):
        raise ValueError('unknown scoped document role')
    allowed = ('read_current_proof({}), save_proof_revision({"expected_revision": "the exact current revision", '
               '"proof_markdown": "the complete new draft"}), read_artifact({"artifact_id": "an exact indexed ID"'
               '})') if mode == 'main' else (
               'read_required_evidence({"page": 0}), read_artifact({"artifact_id": "an exact indexed ID"})')
    from pilot_candidate_contract import DRAFT_CHECKPOINT_GUIDANCE
    network = (' Public web search is permitted only when useful; use the native web tool or exactly text(await tools.web__run(JSON_OBJECT)); in functions.exec. JSON_OBJECT must be strict JSON with double-quoted property names and strings, not a JavaScript object literal. For example: text(await tools.web__run({"search_query":[{"q":"public source title"}],"response_length":"short"})); Do not add const/let assignments, comments, extra statements, or functions.wait; those are not admitted web bridges. Public source downloads use direct fetch_public_source({\"url\":\"https://...\"}) and read_public_source({\"source_id\":\"returned ID\",\"member\":\"indexed member\"}) calls. These are untrusted literature, never original required evidence. Fetch attempts/time/bytes are bounded and failures cached; do not repeat unchanged failures or wait for a human. Never seek benchmark answers, private resources or novelty searches. Preserve known credit and disclose unresolved essential dependencies while continuing useful work.' if public_sources else '')
    return (('SAVE-ONLY RESPONSE CONTRACT: ' + DRAFT_CHECKPOINT_GUIDANCE + '\n' if mode == 'main' else '') + 'SCOPED DOCUMENT TOOL INVOCATION: The tools are advertised directly in the mcp__merlean_documents namespace. '
            'Use a direct tool call with its JSON arguments: ' + allowed + '. '
            'Do not discover or invoke these tools through functions.exec, ALL_TOOLS, JavaScript, tool_search, shell, '
            'resource listing, patch tools, or subagents. Those calls are outside this stage contract. '
            'Read every declared required evidence page before positive review authority; optional documents remain need-driven. If a declared tool is unavailable, '
            'report that infrastructure limitation within the existing response contract; do not probe other tool surfaces.' + network)


def document_prompt(prompt, mode, public_sources=False):
    """Exact document-only transport suffix, shared with durable admissions."""
    return prompt + '\n' + invocation_guidance(mode, public_sources)


def tool_definitions(mode, public_sources=False):
    def tool(name, description, properties, required):
        return {'name': name, 'description': description,
                'inputSchema': {'type': 'object', 'properties': properties,
                                'required': required, 'additionalProperties': False}}
    string = {'type': 'string'}
    result = [tool('read_artifact', 'Read an approved immutable artifact by ID. The host verifies its saved version; no hash is needed. Optional legacy SHA-256 must match. '
                   'Optional start/end are Unicode character offsets: omitted start is 0 and omitted end is the text length. '
                   'Omit both for the complete text. '
                   'A partial read is explicitly labeled and does not supply the remainder.',
                   {'artifact_id': string, 'sha256': string, 'start': {'type': 'integer', 'minimum': 0},
                    'end': {'type': 'integer', 'minimum': 0}}, ['artifact_id'])]
    if mode == 'review':
        result.append(tool('read_required_evidence', 'Read one deterministic exact page of mandatory evidence. Start at page 0 and follow next_page; all pages are required. A sent response is not verified delivery or proof acceptance.', {'page': {'type': 'integer', 'minimum': 0}}, ['page']))
    if mode == 'main':
        result.extend((tool('read_current_proof', 'Read your complete current proof draft and exact revision. '
                            'A saved draft is not a submitted or accepted proof.', {}, []),
                       tool('save_proof_revision', 'Atomically save your complete proof.md during this turn. '
                            'Supply the current expected_revision; stale saves fail. Honest partial proofs are allowed. '
                            'This saves a draft only and never commissions review or approves mathematics.',
                            {'expected_revision': string, 'proof_markdown': string},
                            ['expected_revision', 'proof_markdown'])))
    if public_sources:
        result.extend((tool('fetch_public_source', 'Fetch a needed unauthenticated public HTTPS source with finite time/byte/URL budgets and a durable no-retry cache. Saves exact bytes and indexes readable TeX/BibTeX/text/PDF extraction. Does not verify claims. Never seek benchmark solutions.', {'url': string}, ['url']),
            tool('read_public_source', 'Read a saved public source member by returned ID and member name. At most 16000 characters; next_start gives continuation. Never counts as original evidence delivery.', {'source_id': string, 'member': string, 'start': {'type':'integer','minimum':0}, 'end': {'type':'integer','minimum':0}}, ['source_id'])))
    return result


def available_tools(scope):
    return {item['name'] for item in tool_definitions(scope['mode'], 'public_source_store' in scope)}


class DocumentTools:
    def __init__(self, scope):
        self.scope = validate_scope(scope)
        self.sequence = 0
        self.seen_requests = set()
        self.seen_calls = set()
        self.cli_session = None

    def call(self, tool, arguments, request_id, metadata):
        read = None
        saved_revision = None
        public_source = None
        call_id = metadata.get('callId') if type(metadata) is dict else None
        session_id = metadata.get('sessionId') if type(metadata) is dict else None
        try:
            if not isinstance(call_id, str) or not call_id or not isinstance(session_id, str) or not session_id:
                raise ValueError('missing CLI call or session identity')
            if self.cli_session is not None and session_id != self.cli_session:
                raise ValueError('document capability cannot cross CLI sessions')
            if self.scope['mode'] == 'main' and session_id != self.scope['main_session']:
                raise ValueError('document editor differs from original main')
            if call_id in self.seen_calls:
                raise ValueError('duplicate CLI document call id')
            self.seen_calls.add(call_id)
            self.cli_session = session_id
            request_key = encoded(request_id)
            if request_key in self.seen_requests:
                raise ValueError('duplicate document request id')
            self.seen_requests.add(request_key)
            if tool not in available_tools(self.scope) or not valid_arguments(tool, arguments, self.scope['mode']):
                raise ValueError('tool or argument fields are outside this document capability')
            if tool in PUBLIC_TOOLS:
                from pilot_public_sources import fetch_public_source, read_public_source
                operation = fetch_public_source if tool == 'fetch_public_source' else read_public_source
                value = operation(Path(self.scope['public_source_store']), **arguments)
                public_source = {k: value[k] for k in ('source_id','status','receipt_sha256','member','sha256','start','end') if k in value}
            elif tool in ('read_artifact', 'read_required_evidence'):
                page = None
                read_arguments = arguments
                if tool == 'read_required_evidence':
                    pages = required_read_plan(self.scope)
                    if arguments['page'] >= len(pages):
                        raise ValueError('required evidence page outside finite plan')
                    page = pages[arguments['page']]
                    read_arguments = page
                ident = read_arguments['artifact_id']
                entry = self.scope['readonly_artifacts'].get(ident)
                if entry is None or read_arguments.get('sha256', entry['sha256']) != entry['sha256']:
                    raise ValueError('unknown artifact or mismatched exact hash')
                data = regular_bytes(entry['path'])
                if digest(data) != entry['sha256']:
                    raise ValueError('immutable artifact changed')
                text = data.decode('utf-8')
                start, end = read_arguments.get('start', 0), read_arguments.get('end', len(text))
                if not 0 <= start <= end <= len(text):
                    raise ValueError('artifact range must be within complete text with start <= end')
                read = {'artifact_id': ident, 'sha256': entry['sha256'], 'start': start, 'end': end, 'characters': len(text)}
                value = {**read, 'complete': start == 0 and end == len(text), 'text': text[start:end],
                         'authority': 'exact historical material only; no current proof acceptance'}
                if page is not None:
                    value['required_page'] = {**page, 'page_count': len(pages),
                        'next_page': page['page'] + 1 if page['page'] + 1 < len(pages) else None,
                        'authority': 'navigation only; final persisted output audit determines delivered coverage'}
            else:
                import pilot_proof_document as store
                identity = {k: self.scope[k] for k in ('problem_id', 'original_sha256', 'main_session')}
                if tool == 'read_current_proof':
                    current = store.read_current(self.scope['store_root'], **identity)
                else:
                    current = store.save_draft(self.scope['store_root'], **identity, **arguments,
                                               producer=self.scope['producer'])
                    saved_revision = {k: current[k] for k in ('revision', 'manifest_sha256', 'proof_sha256', 'status')}
                fields = ('revision', 'proof_sha256', 'proof_markdown', 'status') if tool == 'read_current_proof' else ('revision', 'proof_sha256', 'status')
                value = {k: current[k] for k in fields}
                if 'view_status' in current:
                    value['view_status'] = current['view_status']
                value['authority'] = 'draft document only; submission and acceptance are separate'
            result = {'content': [{'type': 'text', 'text': encoded(value)}], 'isError': False}
        except (ValueError, OSError, UnicodeError) as error:
            # Only controlled backend diagnostics; never echo rejected contents.
            message = str(error) if isinstance(error, ValueError) else type(error).__name__
            result = {'content': [{'type': 'text', 'text': 'Document operation refused: ' + message}], 'isError': True}
        self.sequence += 1
        receipt = {'sequence': self.sequence, 'rpc_id': request_id, 'call_id': call_id, 'session_id': session_id, 'tool': tool,
                   'arguments_sha256': digest(encoded(arguments).encode()),
                   'result_sha256': digest(encoded(result).encode()),
                   'native_result_sha256': digest(encoded({'content': result['content'], 'structured_content': None}).encode()),
                   'content_text_sha256': [digest(part['text'].encode()) for part in result['content']], 'is_error': result['isError'],
                   'read': read if not result['isError'] else None,
                   'saved_revision': saved_revision if not result['isError'] else None, 'producer': self.scope['producer'],
                   'public_source': public_source if not result['isError'] else None}
        # Receipt is durable before acknowledging a tool result. Draft store has its
        # own atomic publication; an interrupted response never erases a saved draft.
        fd = os.open(self.scope['receipt_path'], os.O_WRONLY | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW, 0o600)
        try:
            os.write(fd, (encoded(receipt) + '\n').encode()); os.fsync(fd)
        finally:
            os.close(fd)
        return result


def main():
    import pilot_proof_document  # Verify the copied dependency before MCP startup.
    parser = argparse.ArgumentParser(); parser.add_argument('--scope', required=True); parser.add_argument('--sha256', required=True)
    args = parser.parse_args(); data = regular_bytes(args.scope)
    if digest(data) != args.sha256:
        raise ValueError('document capability changed')
    server = DocumentTools(json.loads(data))
    for line in sys.stdin:
        request = json.loads(line)
        if 'id' not in request:
            continue
        method, ident = request.get('method'), request['id']
        if method == 'initialize':
            result = {'protocolVersion': '2025-06-18', 'capabilities': {'tools': {}},
                      'serverInfo': {'name': SERVER, 'version': '1'}}
        elif method == 'tools/list': result = {'tools': tool_definitions(server.scope['mode'], 'public_source_store' in server.scope)}
        elif method == 'tools/call':
            params = request.get('params', {})
            result = server.call(params.get('name'), params.get('arguments', {}), ident, params.get('_meta', {}))
        elif method == 'ping': result = {}
        else:
            print(encoded({'jsonrpc': '2.0', 'id': ident, 'error': {'code': -32601, 'message': 'Unsupported fixed document method'}}), flush=True)
            continue
        print(encoded({'jsonrpc': '2.0', 'id': ident, 'result': result}), flush=True)



def output_capacity(scope):
    """Reserve CLI tool history space from actual complete allowed response sizes.

    This is not an evidence rejection threshold. No content is removed. Pinned
    CLI requires a numeric setting; persisted output checks remain authoritative
    if a future mutable draft exceeds this initial capacity or CLI behavior changes.
    """
    sizes = [len(encoded(scope).encode())]
    if 'public_source_store' in scope:
        sizes.append(128000)  # Complete bounded source chunks and member manifests.
    for ident, entry in scope['readonly_artifacts'].items():
        text = regular_bytes(entry['path']).decode('utf-8')
        sizes.append(len(encoded({'artifact_id': ident, 'sha256': entry['sha256'],
            'start': 0, 'end': len(text), 'characters': len(text), 'complete': True, 'text': text,
            'authority': 'exact historical material only; no current proof acceptance'}).encode()))
    if scope['mode'] == 'main':
        import pilot_proof_document as store
        current = store.read_current(scope['store_root'], **{k:scope[k] for k in ('problem_id','original_sha256','main_session')})
        sizes.append(len(encoded({k: current[k] for k in ('revision','proof_sha256','proof_markdown','status')}).encode()))
    # The capability size covers response labels/framing; UTF-8 byte count is a
    # deliberately conservative numeric history reservation for the pinned CLI.
    return max(sizes) + sizes[0]


def _known_clipping(full_text, parts):
    for part in parts:
        for clip in part.get('clippings', []):
            left, right = clip['prefix_characters'], clip['suffix_characters']
            if (left + right + clip['removed_characters'] == len(full_text)
                    and digest(full_text[:left].encode()) == clip['prefix_sha256']
                    and digest((full_text[len(full_text)-right:] if right else '').encode()) == clip['suffix_sha256']):
                return True
    return False


def prepare_scope(spec, artifact_dir, producer, *, internet_browse=False):
    """Freeze a host-only stage capability; no model-provided scope is accepted."""
    scope = {**spec, 'producer': producer, 'receipt_path': str((Path(artifact_dir) / 'document-operations.jsonl').resolve())}
    if internet_browse:
        scope.setdefault('public_source_store', str(Path(scope['store_root']) / 'public-sources'))
    elif 'public_source_store' in scope:
        raise ValueError('offline stage cannot inherit a public-source capability')
    scope.setdefault('inline_artifact_ids', [])
    validate_scope(scope)
    data = encoded(scope).encode()
    path = Path(artifact_dir) / 'document-capability.json'
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(data); stream.flush(); os.fsync(stream.fileno())
    return scope, {'path': str(path.resolve()), 'sha256': digest(data)}


def allowed_event(event, scope):
    item = event.get('item')
    return (event.get('type') in ('item.started', 'item.updated', 'item.completed')
            and type(item) is dict and item.get('type') == 'mcp_tool_call'
            and item.get('server') == SERVER
            and item.get('tool') in available_tools(scope)
            and type(item.get('arguments')) is dict)


def audit_operations(scope, events, persisted, actual_session, output_receipts):
    """Reconcile native results and persisted calls with server operation receipts.

    Delivery coverage is mechanical, not evidence of mathematical comprehension.
    Missing or failed delivery never becomes a successful read receipt.
    """
    path = Path(scope['receipt_path'])
    receipts = [json.loads(line) for line in regular_bytes(path).decode().splitlines()] if path.exists() else []
    expected = Counter((r['tool'], r['arguments_sha256']) for r in receipts)
    completed = [e['item'] for e in events if e.get('type') == 'item.completed']
    actual = Counter((e['tool'], digest(encoded(e['arguments']).encode())) for e in completed)
    errors = []
    if expected != actual:
        errors.append('native calls and durable document receipts differ')
    for index, receipt in enumerate(receipts):
        if receipt['tool'] not in available_tools(scope):
            errors.append('receipt tool exceeds scoped capability')
        if (receipt['sequence'] != index + 1 or receipt['producer'] != scope['producer']
                or receipt.get('session_id') != actual_session):
            errors.append('document receipt sequence or producing stage differs')
    pending = list(receipts)
    delivered = set()
    delivery_errors = []
    native_diagnostics = []
    for event in completed:
        key = (event['tool'], digest(encoded(event['arguments']).encode()))
        match = next((r for r in pending if (r['tool'], r['arguments_sha256']) == key), None)
        if match is None:
            continue
        pending.remove(match)
        native_matches = (event.get('result') is not None
                          and digest(encoded(event['result']).encode()) == match['native_result_sha256'])
        native_diagnostics.append({'call_id': match['call_id'], 'native_result_matches_receipt': native_matches})
        # Large native CLI events can contain a shortened diagnostic while the
        # model receives the full result. Content authority is the durable server
        # receipt matched to persisted model-visible blocks, never this preview.
        if event.get('error') is not None or event.get('status') != ('failed' if match['is_error'] else 'completed'):
            errors.append('CLI document status differs from acknowledged server result')
            continue
        outputs = [r for r in output_receipts if r.get('call_id') == match['call_id']]
        if len(outputs) != 1:
            errors.append('document call has no unique model-visible output receipt')
        else:
            parts = outputs[0].get('text_parts', [])
            content_hashes = match['content_text_sha256']
            if (outputs[0].get('output_format') != 'list' or len(parts) != len(content_hashes) + 1
                    or not parts[0].get('wall_time_framing')
                    or any(p.get('type') != 'input_text' or p.get('keys') != ['text', 'type'] for p in parts)):
                errors.append('unexpected model-visible document output framing or blocks')
                continue
            complete = True
            for index, (expected_hash, actual) in enumerate(zip(content_hashes, parts[1:])):
                if actual.get('sha256') == expected_hash:
                    continue
                complete = False
                if not native_matches or not _known_clipping(event['result']['content'][index]['text'], [actual]):
                    errors.append('unrecognized alteration of model-visible document output')
            if complete:
                delivered.add(match['sequence'])
            else:
                delivery_errors.append({'call_id': match['call_id'], 'tool': match['tool'],
                    'reason': 'exact complete tool content not retained in model-visible history'})
    saved_calls = [r for r in persisted if r.get('namespace') == NAMESPACE and r.get('name') in TOOLS]
    receipt_calls = Counter((r.get('call_id'), r['tool'], r['arguments_sha256']) for r in receipts)
    if len({r.get('call_id') for r in receipts}) != len(receipts):
        errors.append('duplicate document model call identity')
    if Counter((r.get('call_id'), r['name'], r.get('arguments_canonical_sha256')) for r in saved_calls) != receipt_calls:
        errors.append('persisted document calls differ from durable receipts')
    coverage = {}
    for ident in scope['readonly_artifacts']:
        reads = [r['read'] for r in receipts if r['sequence'] in delivered and not r['is_error'] and r.get('read') and r['read']['artifact_id'] == ident]
        end = 0
        for read in sorted(reads, key=lambda r: (r['start'], r['end'])):
            if read['start'] <= end:
                end = max(end, read['end'])
        coverage[ident] = ident in scope['inline_artifact_ids'] or (bool(reads) and end == reads[0]['characters'])
    # Exact parent ranges also deliver any wholly contained authenticated chunks.
    # This enables bounded required pages without carrying partial chunks.
    for ident, (parent, left, right, _) in chunk_bindings(scope).items():
        ranges = sorted((r['read']['start'], r['read']['end']) for r in receipts
            if r['sequence'] in delivered and not r['is_error'] and r.get('read')
            and r['read']['artifact_id'] == parent)
        end = left
        for start, stop in ranges:
            if start <= end:
                end = max(end, stop)
        if end >= right:
            coverage[ident] = True
    coverage = expand_chunk_coverage(scope, coverage)
    return {'status': 'PASS' if not errors else 'FAIL', 'errors': errors, 'delivery_errors': delivery_errors,
            'complete_tool_outputs_delivered': not delivery_errors and not errors,
            'native_diagnostics': native_diagnostics,
            'public_source_operations': [{**r['public_source'], 'delivered': r['sequence'] in delivered} for r in receipts if r.get('public_source')],
            'receipt_count': len(receipts), 'receipt_sha256': digest(regular_bytes(path)) if path.exists() else None,
            'artifact_coverage': coverage,
            'required_artifact_coverage': {k: coverage[k] for k in scope['required_artifact_ids']},
            'required_material_delivered': all(coverage[k] for k in scope['required_artifact_ids']),
            'authority': 'delivery identity only; no mathematical comprehension or acceptance'}


if __name__ == '__main__':
    main()
