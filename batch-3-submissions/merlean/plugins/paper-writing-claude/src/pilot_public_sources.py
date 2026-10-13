"""Bounded, unauthenticated public HTTPS retrieval; never mathematical verification.

The host chooses the store. Model arguments are URLs, source IDs and indexed members,
never writable paths. A durable admission is also the retry boundary after interruption.
"""
from __future__ import annotations
import hashlib
import fcntl
import http.client
import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import signal
import resource
import socket
import ssl
import subprocess
import sys
import time
import threading
import urllib.parse

MAX_URLS = 16
MAX_BYTES = 16 * 1024 * 1024
MAX_STORE_BYTES = 64 * 1024 * 1024
MAX_TEXT_BYTES = 24 * 1024 * 1024
MAX_MEMBERS = 256
READ_CHARS = 16000
FETCH_SECONDS = 30
MAX_REDIRECTS = 4
HEX = re.compile(r'[a-f0-9]{64}\Z')
TEXT_SUFFIXES = {'.tex', '.bib', '.txt', '.md', '.html', '.htm', '.xml', '.json', '.sty', '.cls'}


def digest(data): return hashlib.sha256(data).hexdigest()
def encoded(value): return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()

def _write(path, data):
    with Path(path).open('xb') as stream:
        stream.write(data); stream.flush(); os.fsync(stream.fileno())


def _file(root, name):
    root = Path(root)
    if root.resolve() != root:
        raise ValueError('source directory cannot contain symlinks')
    path = root / name
    if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError('source is not an immutable confined regular file')
    return path


def _root(store):
    store = Path(store)
    if not store.is_absolute() or store.resolve() != store:
        raise ValueError('public source store must be a canonical host path')
    store.mkdir(parents=True, exist_ok=True)
    return store


def validate_url(url):
    if type(url) is not str or len(url) > 4096 or any(ord(c) < 33 or ord(c) == 127 for c in url):
        raise ValueError('invalid public HTTPS URL')
    try:
        parts = urllib.parse.urlsplit(url)
        if (parts.scheme != 'https' or not parts.hostname or parts.username is not None
                or parts.password is not None or parts.port not in (None, 443) or parts.fragment):
            raise ValueError('only credential-free public HTTPS on port 443 is allowed')
        host = parts.hostname.encode('idna').decode('ascii')
    except (ValueError, UnicodeError) as error:
        raise ValueError('invalid public HTTPS authority') from error
    if host.lower() in {'localhost', 'metadata.google.internal'} or host.endswith(('.localhost', '.local', '.internal')):
        raise ValueError('nonpublic host refused')
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    if address is not None and (not address.is_global or address.is_multicast or address.is_reserved):
        raise ValueError('nonpublic IP refused')
    # Sensitive URLs, cookies and signed/private download links are outside this tool.
    query_keys = {k.lower() for k, _ in urllib.parse.parse_qsl(parts.query)}
    if any(k in {'token', 'access_token', 'api_key', 'apikey', 'key', 'password', 'signature', 'sig'}
           or k.startswith(('x-amz-', 'x-goog-')) for k in query_keys):
        raise ValueError('authenticated or signed URL refused')
    return parts, host


def public_addresses(host):
    values = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    addresses = list(dict.fromkeys(item[4][0] for item in values))
    if not addresses or any(not ipaddress.ip_address(a).is_global or ipaddress.ip_address(a).is_multicast or ipaddress.ip_address(a).is_reserved for a in addresses):
        raise ValueError('DNS resolved to a nonpublic address')
    return addresses


class _PinnedHTTPS(http.client.HTTPSConnection):
    def __init__(self, host, address, timeout):
        super().__init__(host, timeout=timeout, context=ssl.create_default_context())
        self.address = address

    def connect(self):
        # Pin the validated IP while retaining hostname TLS verification and SNI.
        sock = socket.create_connection((self.address, 443), self.timeout)
        try: self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
        except BaseException:
            sock.close(); raise


def download(url, raw_path):
    """Runs only in a killable helper, bounding DNS, TLS and slow body transfer."""
    deadline = time.monotonic() + FETCH_SECONDS - 2
    current = url
    for redirect in range(MAX_REDIRECTS + 1):
        parts, host = validate_url(current)
        address = public_addresses(host)[0]
        remaining = deadline - time.monotonic()
        if remaining <= 0: raise TimeoutError('public fetch time limit')
        connection = _PinnedHTTPS(host, address, min(5, remaining))
        try:
            path = urllib.parse.urlunsplit(('', '', parts.path or '/', parts.query, ''))
            connection.request('GET', path, headers={'User-Agent': 'MerLean-public-source/1.0',
                'Accept': '*/*', 'Accept-Encoding': 'identity'})
            response = connection.getresponse()
            if response.status in (301, 302, 303, 307, 308):
                location = response.getheader('Location')
                if not location or redirect == MAX_REDIRECTS:
                    raise ValueError('public redirect limit or missing target')
                current = urllib.parse.urljoin(current, location)
                validate_url(current)
                continue
            if response.status != 200: raise ValueError('public HTTP status ' + str(response.status))
            length = response.getheader('Content-Length')
            if length is not None and (not length.isdigit() or int(length) > MAX_BYTES):
                raise ValueError('public source exceeds byte limit')
            if response.getheader('Content-Encoding', 'identity').lower() != 'identity':
                raise ValueError('compressed HTTP transfer unsupported')
            total = 0
            with Path(raw_path).open('xb') as stream:
                while True:
                    if time.monotonic() >= deadline: raise TimeoutError('public fetch time limit')
                    chunk = response.read(min(65536, MAX_BYTES - total + 1))
                    if not chunk: break
                    total += len(chunk)
                    if total > MAX_BYTES: raise ValueError('public source exceeds byte limit')
                    stream.write(chunk)
                stream.flush(); os.fsync(stream.fileno())
            return {'final_url': current, 'content_type': response.getheader('Content-Type', ''), 'bytes': total}
        finally: connection.close()
    raise ValueError('public redirect limit')


def _pdf_limits():
    resource.setrlimit(resource.RLIMIT_FSIZE, (MAX_TEXT_BYTES, MAX_TEXT_BYTES))


def _members(folder, content_type, *, allow_pdf=True, pdf_timeout=8):
    raw = folder / 'raw'
    data = raw.read_bytes()
    paths = []
    if data.startswith(b'%PDF-'):
        if not allow_pdf: raise ValueError('PDF awaiting bounded parent extraction')
        binary = shutil.which('pdftotext')
        if not binary: raise ValueError('PDF saved, but pdftotext is unavailable')
        process = subprocess.Popen([binary, '-layout', str(raw), str(folder/'source.txt')],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, preexec_fn=_pdf_limits)
        try:
            _write(folder/'converter-lifetime.json', encoded({'pid':process.pid, 'process_group':os.getpgrp(),
                'maximum_lifetime_seconds':pdf_timeout, 'authority':'bounded direct-child PDF extraction only'}))
            code = process.wait(timeout=pdf_timeout)
        except BaseException:
            process.kill(); process.wait(timeout=2)
            raise
        if code: raise ValueError('PDF saved, but text extraction failed')
        paths = [folder / 'source.txt']
    elif data.startswith((b'\x1f\x8b', b'PK\x03\x04')) or (len(data) > 262 and data[257:262] == b'ustar'):
        from paper_writing_codex import safe_extract as extractor
        # Tight source-retrieval limits; do not change the general extractor policy.
        extractor.MAX_MEMBERS = MAX_MEMBERS
        extractor.MAX_FILE_BYTES = MAX_BYTES
        extractor.MAX_TOTAL_BYTES = MAX_TEXT_BYTES
        extractor.MAX_ARCHIVE_BYTES = MAX_BYTES
        archive = raw
        if data.startswith(b'\x1f\x8b'):
            archive = folder/'source.gz'
            _write(archive, data)
        extractor.safe_extract(archive, folder/'extracted')
        paths = [p for p in sorted((folder/'extracted').rglob('*'))
                 if p.is_file() and (p.suffix.lower() in TEXT_SUFFIXES or p.name == 'source.tex')]
    else:
        data.decode('utf-8')
        paths = [raw]
    members, total = [], 0
    for path in paths:
        body = path.read_bytes()
        total += len(body)
        if total > MAX_TEXT_BYTES or len(members) >= MAX_MEMBERS:
            raise ValueError('source text exceeds extraction limit')
        try: text = body.decode('utf-8')
        except UnicodeError: continue
        name = str(path.relative_to(folder))
        members.append({'member': name, 'sha256': digest(body), 'characters': len(text), 'bytes': len(body)})
    if not members: raise ValueError('download has no readable source text')
    return members


def _worker(url, folder):
    metadata = download(url, folder/'raw')
    try:
        members = _members(folder, metadata['content_type'], allow_pdf=False)
        error = None
    except (ValueError, OSError, UnicodeError, subprocess.TimeoutExpired) as exc:
        members, error = [], str(exc)[:240]
    raw = (folder/'raw').read_bytes()
    return {**metadata, 'raw_sha256': digest(raw), 'members': members, 'read_error': error}


def verify_public_source(store, source_id):
    store = _root(store)
    if type(source_id) is not str or HEX.fullmatch(source_id) is None:
        raise ValueError('invalid public source ID')
    folder = store / source_id
    receipt_path = _file(folder, 'receipt.json')
    receipt = json.loads(receipt_path.read_bytes())
    if receipt.get('source_id') != source_id or digest(receipt['requested_url'].encode()) != source_id:
        raise ValueError('source receipt identity mismatch')
    for record in receipt.get('content_files', []):
        if digest(_file(folder, record['path']).read_bytes()) != record['sha256']:
            raise ValueError('public source content inventory changed')
    if receipt['status'] == 'downloaded':
        raw = _file(folder, 'raw').read_bytes()
        if digest(raw) != receipt['raw_sha256']: raise ValueError('downloaded source hash changed')
        for member in receipt['members']:
            body = _file(folder, member['member']).read_bytes()
            if digest(body) != member['sha256']: raise ValueError('source text hash changed')
    return {**receipt, 'receipt_sha256': digest(receipt_path.read_bytes()),
            'source_path': str(folder/'raw'), 'receipt_path': str(receipt_path)}


def _run_worker(url, folder):
    process = subprocess.Popen([sys.executable, '-B', str(Path(__file__).resolve()), '--fetch', url, str(folder)],
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    try:
        output, _ = process.communicate(timeout=FETCH_SECONDS)
    except BaseException:
        # No nested child: the retained process handle kills/reaps the single worker.
        # It shares the stage group, so transport cancellation also terminates it.
        process.kill()
        process.communicate(timeout=2)
        raise
    if process.returncode:
        raise ValueError('public source fetch failed: ' + output.decode('utf-8', errors='replace')[:240])
    return json.loads(output)


def _fetch_public_source_locked(store, url):
    store = _root(store)
    if type(url) is not str: raise ValueError('URL must be text')
    source_id = digest(url.encode())
    folder = store / source_id
    if folder.exists():
        if (folder/'receipt.json').exists(): return verify_public_source(store, source_id)
        return {'status': 'unavailable', 'source_id': source_id,
                'error': 'earlier admission interrupted; no automatic retry', 'retryable': False}
    existing = [p for p in store.iterdir() if p.is_dir() and HEX.fullmatch(p.name)]
    if len(existing) >= MAX_URLS:
        return {'status': 'unavailable', 'source_id': source_id, 'error': 'public source URL budget exhausted', 'retryable': False}
    total = sum((p/'raw').stat().st_size for p in existing if (p/'raw').is_file())
    if total + MAX_BYTES > MAX_STORE_BYTES:
        return {'status': 'unavailable', 'source_id': source_id, 'error': 'public source store byte budget exhausted', 'retryable': False}
    folder.mkdir(exist_ok=False)
    _write(folder/'admission.json', encoded({'requested_url': url, 'source_id': source_id, 'attempt': 1}))
    receipt = {'status': 'unavailable', 'source_id': source_id, 'requested_url': url,
               'retryable': False, 'authority': 'untrusted public source; no source claim verification or research acceptance'}
    try:
        started = time.monotonic()
        validate_url(url)
        metadata = _run_worker(url, folder)
        if (folder/'raw').read_bytes().startswith(b'%PDF-'):
            remaining = FETCH_SECONDS - (time.monotonic() - started)
            if remaining > 0:
                try:
                    metadata['members'] = _members(folder, metadata['content_type'], pdf_timeout=min(8, remaining))
                    metadata['read_error'] = None
                except (ValueError, OSError, UnicodeError, subprocess.TimeoutExpired) as error:
                    metadata['read_error'] = type(error).__name__ + ': ' + str(error)[:240]
        metadata['content_files'] = source_content_files(folder)
        receipt.update(metadata, status='downloaded')
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        receipt['error'] = type(error).__name__ + ': ' + str(error)[:240]
    receipt['content_files'] = source_content_files(folder)
    _write(folder/'receipt.json', encoded(receipt))
    return verify_public_source(store, source_id)


def fetch_public_source(store, url):
    store = _root(store)
    fd = os.open(store/'.admission-lock', os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    try:
        try: fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return {'status':'unavailable', 'error':'another bounded source fetch is active; continue other work', 'retryable':False}
        return _fetch_public_source_locked(store, url)
    finally: os.close(fd)


def read_public_source(store, source_id, member=None, start=0, end=None):
    receipt = verify_public_source(store, source_id)
    if receipt['status'] != 'downloaded':
        return {'status': 'unavailable', 'source_id': source_id, 'error': receipt.get('error', 'source unavailable')}
    members = receipt['members']
    if member is None:
        if len(members) != 1: raise ValueError('choose an exact member from the source receipt')
        member = members[0]['member']
    entry = next((v for v in members if v['member'] == member), None)
    if entry is None: raise ValueError('unknown public source member')
    if type(start) is not int or start < 0 or (end is not None and type(end) is not int):
        raise ValueError('invalid source character range')
    text = _file(Path(store)/source_id, member).read_text()
    end = min(start + READ_CHARS, len(text)) if end is None else end
    if not 0 <= start <= end <= len(text) or end - start > READ_CHARS:
        raise ValueError('source read range exceeds finite chunk')
    return {'status': 'read', 'source_id': source_id, 'member': member, 'sha256': entry['sha256'],
            'source_path': str(Path(store)/source_id/member), 'start': start, 'end': end,
            'characters': len(text), 'next_start': end if end < len(text) else None, 'text': text[start:end],
            'receipt_sha256': receipt['receipt_sha256'],
            'authority': 'public source text only; never original-evidence delivery or mathematical approval'}


def source_content_files(folder):
    files = []
    for path in sorted(Path(folder).rglob('*')):
        if path.is_symlink(): raise ValueError('source content contains symlink')
        if not path.is_file(): continue
        name = str(path.relative_to(folder))
        if name in {'admission.json','receipt.json','helper-lifetime.json','converter-lifetime.json','partial-content.json'}: continue
        files.append({'path':name,'sha256':digest(path.read_bytes())})
    return files


def public_source_catalog(store):
    store = Path(store)
    if not store.exists(): return []
    store = _root(store)
    catalog = []
    for folder in sorted(store.iterdir()):
        if folder.is_dir() and not folder.is_symlink() and HEX.fullmatch(folder.name) and (folder/'receipt.json').is_file():
            receipt = verify_public_source(store, folder.name)
            catalog.append({k: receipt[k] for k in ('source_id','status','requested_url','source_path','receipt_path','receipt_sha256','members','error','read_error') if k in receipt})
    if len(catalog) > MAX_URLS: raise ValueError('public source catalog exceeds bounded admission budget')
    return catalog


def seed_public_sources(source_store, target_store):
    """Copy only immutable retrieval evidence, never research opinions or review verdicts."""
    source_store, target_store = Path(source_store), Path(target_store)
    if not source_store.exists(): return []
    source_store, target_store = _root(source_store), _root(target_store)
    for folder in sorted(source_store.iterdir()):
        if not folder.is_dir() or folder.is_symlink() or not HEX.fullmatch(folder.name): continue
        destination = target_store/folder.name
        if destination.exists():
            # A locally completed retrieval is retained; source hashes still verified independently.
            if (folder/'receipt.json').exists(): verify_public_source(source_store, folder.name)
            continue
        if len([p for p in target_store.iterdir() if HEX.fullmatch(p.name)]) >= MAX_URLS:
            raise ValueError('source handoff exceeds bounded admission budget')
        if not (folder/'receipt.json').exists():
            # Retain interrupted admission too, so a stage change does not reset its retry boundary.
            destination.mkdir()
            _write(destination/'admission.json', _file(folder,'admission.json').read_bytes())
            continue
        receipt = verify_public_source(source_store, folder.name)
        destination.mkdir()
        names = {'admission.json','receipt.json'}
        names.update(m['path'] for m in receipt.get('content_files', []))
        if receipt['status'] == 'downloaded':
            names.add('raw')
            names.update(m['member'] for m in receipt['members'])
            names.update(m['path'] for m in receipt.get('content_files', []))
        for name in sorted(names):
            source = _file(folder,name)
            target = destination/name
            target.parent.mkdir(parents=True, exist_ok=True)
            _write(target, source.read_bytes())
        verify_public_source(target_store, folder.name)
    return public_source_catalog(target_store)


def _hard_lifetime(pid):
    # The watchdog can signal only itself, which is still in the owned stage group.
    if pid != os.getpid(): os._exit(2)
    os.kill(pid, signal.SIGKILL)


def _helper_main(url, folder):
    pid, group = os.getpid(), os.getpgrp()
    _write(folder/'helper-lifetime.json', encoded({'pid':pid, 'process_group':group,
        'parent_pid':os.getppid(), 'maximum_lifetime_seconds':FETCH_SECONDS,
        'admission_sha256':digest((folder/'admission.json').read_bytes()),
        'authority':'bounded retrieval helper only; never campaign controller'}))
    timer = threading.Timer(FETCH_SECONDS, _hard_lifetime, args=(pid,))
    timer.daemon = True
    timer.start()  # Before DNS: remains alive and bounded even if the MCP parent is killed.
    try: return _worker(url, folder)
    finally: timer.cancel()


if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[1] != '--fetch': raise SystemExit(2)
    try: print(json.dumps(_helper_main(sys.argv[2], Path(sys.argv[3]))))
    except Exception as error:
        print(type(error).__name__ + ': ' + str(error)[:240]); raise SystemExit(1)
