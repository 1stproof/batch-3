"""Copied, hash-bound document runtime and no-model Codex-boundary startup probe."""
from __future__ import annotations
import asyncio
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import subprocess
import time
import tomllib

RUNTIME_FILES = ('pilot_document_tools.py', 'pilot_proof_document.py', 'pilot_public_sources.py',
                 'paper_writing_codex/__init__.py', 'paper_writing_codex/safe_extract.py', 'paper_writing_codex/versioning.py')
# MCP inventory/schema notifications can exceed asyncio's default 64 KiB.
# Keep a finite per-frame bound, independent of model/context budgets.
MCP_RPC_LINE_LIMIT = 4 * 1024 * 1024

def digest(data): return hashlib.sha256(data).hexdigest()

def prepare_runtime(artifact_dir):
    folder = Path(artifact_dir).resolve() / 'document-runtime'
    folder.mkdir(exist_ok=False)
    files = {}
    for name in RUNTIME_FILES:
        data = (Path(__file__).parent/name).read_bytes()
        (folder/name).parent.mkdir(parents=True, exist_ok=True)
        with (folder/name).open('xb') as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
        files[name] = digest(data)
    return {'path': str(folder/'pilot_document_tools.py'), 'files': files}

def verify_runtime(runtime):
    from pilot_document_tools import regular_bytes
    server = Path(runtime['path'])
    if server.name != RUNTIME_FILES[0] or set(runtime['files']) != set(RUNTIME_FILES):
        raise ValueError('unexpected document runtime')
    for name, expected in runtime['files'].items():
        if digest(regular_bytes(server.parent/name)) != expected:
            raise ValueError('document runtime changed')
    return server

def server_config(capability, runtime):
    server = verify_runtime(runtime)
    return ('mcp_servers={merlean_documents={command=' + json.dumps(sys.executable)
            + ',args=' + json.dumps(['-B', str(server), '--scope', capability['path'],
                                    '--sha256', capability['sha256']])
            + ',required=true,default_tools_approval_mode="approve"}}')

def configured_mcp_names(env):
    """Read names only from the ordinary selected user configuration."""
    folder = Path(env.get('CODEX_HOME') or (Path(env.get('HOME') or Path.home()) / '.codex'))
    path = folder / 'config.toml'
    config = tomllib.loads(path.read_text()) if path.exists() else {}
    servers = config.get('mcp_servers', {})
    if not isinstance(servers, dict) or any(not isinstance(name, str) or not name for name in servers):
        raise RuntimeError('invalid configured MCP server names')
    if 'merlean_documents' in servers:
        raise RuntimeError('reserved document MCP server already configured')
    return sorted(servers)

def startup_command(codex_binary, capability, runtime, *, disabled_names=()):
    # Empty app/plugin configuration does not disable account-backed connectors.
    # Use the same audited feature boundary as the offline paid transport.
    from codex_transport import DISABLED_FEATURES
    config = server_config(capability, runtime)
    # Whole inline-table replacement uses literal quoted TOML keys. Dotted CLI
    # overrides do not reliably quote key components in the selected CLI.
    inert = '{command=' + json.dumps(sys.executable) + ',args=["-c","raise SystemExit(1)"],enabled=false}'
    if disabled_names:
        config = config[:-1] + ',' + ','.join(json.dumps(name)+'='+inert for name in disabled_names) + '}'
    command = [codex_binary, 'app-server', '-c', config,
               '-c', 'apps={}', '-c', 'plugins={}', '-c', 'web_search="disabled"']
    for feature in DISABLED_FEATURES:
        command.extend(['--disable', feature])
    return command

class StartupOwnershipError(RuntimeError):
    def __init__(self, pid, identity, reason):
        super().__init__(reason)
        self.cleanup = {'status':'UNKNOWN','pid':pid,'process_identity':identity,'reason':reason}

def helper_identity(pid):
    # Birth identity survives a wrapper's exec into the selected Codex binary.
    try: result = subprocess.run(['ps','-p',str(pid),'-o','lstart='],capture_output=True,text=True,timeout=2)
    except (OSError,subprocess.TimeoutExpired): return None
    return digest((str(pid)+':'+result.stdout.strip()).encode()) if result.returncode == 0 and result.stdout.strip() else None


async def startup_preflight(codex_binary, capability, runtime, mode, *, cwd, env, timeout=15, public_sources=False):
    """Exercise the actual CLI wrapper's inherited OS boundary without any turn.

    Only initialize and MCP inventory RPCs are permitted. Scope tools are never
    invoked, so the probe creates no document-operation/delivery receipts.
    """
    from pilot_document_tools import tool_definitions
    started = time.monotonic()
    disabled_names = configured_mcp_names(env)
    command = startup_command(codex_binary, capability, runtime, disabled_names=disabled_names)
    process = None
    launch_task = None
    process_identity = None
    try:
        async with asyncio.timeout(timeout):
            launch_task = asyncio.create_task(asyncio.create_subprocess_exec(*command, cwd=cwd, env=env,
                stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.DEVNULL, start_new_session=True, limit=MCP_RPC_LINE_LIMIT))
            process = await asyncio.shield(launch_task)
            process_identity = helper_identity(process.pid)
            async def rpc(ident, method, params):
                process.stdin.write((json.dumps({'id':ident,'method':method,'params':params})+'\n').encode())
                await process.stdin.drain()
                while True:
                    try: line = await process.stdout.readline()
                    except (ValueError, asyncio.LimitOverrunError) as error:
                        raise RuntimeError('document startup RPC frame exceeds bounded line limit') from error
                    if len(line) > MCP_RPC_LINE_LIMIT:
                        raise RuntimeError('document startup RPC frame exceeds bounded line limit')
                    if not line: raise RuntimeError('document startup CLI exited before RPC response')
                    response = json.loads(line)
                    if response.get('id') == ident:
                        if 'error' in response: raise RuntimeError('document startup RPC failed')
                        return response['result']
            await rpc(1, 'initialize', {'clientInfo':{'name':'merlean-document-preflight','version':'1'}})
            process.stdin.write((json.dumps({'method':'initialized','params':{}})+'\n').encode())
            await process.stdin.drain()
            response = await rpc(2, 'mcpServerStatus/list', {'limit':100, 'detail':'full'})
            servers = response.get('data', [])
            names = [server.get('name') for server in servers]
            if (names.count('merlean_documents') != 1 or len(set(names)) != len(names)
                    or response.get('nextCursor')):
                raise RuntimeError('unexpected document MCP inventory')
            for extra in servers:
                if extra.get('name') == 'merlean_documents':
                    continue
                if (extra.get('name') not in disabled_names
                        or extra.get('tools') != {} or extra.get('resources') != []
                        or extra.get('resourceTemplates') != [] or extra.get('serverInfo') is not None
                        or ('enabled' in extra and extra['enabled'] is not False)
                        or any(value is not None for key, value in extra.items() if key.endswith('Error'))):
                    raise RuntimeError('unexpected document MCP inventory')
            server = next(item for item in servers if item['name'] == 'merlean_documents')
            expected = {item['name']:item for item in tool_definitions(mode, public_sources)}
            if (server.get('name') != 'merlean_documents' or server.get('tools') != expected
                    or (server.get('serverInfo') or {}).get('name') != 'merlean_documents'
                    or (server.get('serverInfo') or {}).get('version') != '1'
                    or server.get('toolsError') is not None):
                raise RuntimeError('document MCP startup or exact tool inventory failed')
            verify_runtime(runtime)
            return {'status':'PASS', 'boundary':'selected_codex_binary_app_server',
                    'model_calls':0, 'thread_requests':0, 'turn_requests':0,
                    'tools': sorted(expected), 'capability_sha256':capability['sha256'],
                    'disabled_mcp_servers':disabled_names, 'active_mcp_servers':['merlean_documents'],
                    'runtime':runtime, 'elapsed_seconds':time.monotonic()-started}
    finally:
        if process is None and launch_task is not None:
            # Resolve a shielded in-flight OS launch before releasing ownership.
            try:
                process = await launch_task
                process_identity = helper_identity(process.pid)
            except Exception: pass
        if process is not None:
            # Signal only a currently verified owned leader. If the leader
            # vanished before its children were reconciled, do not guess that a
            # recycled numeric process group still belongs to this operation.
            live_identity = helper_identity(process.pid)
            if process.returncode is not None or not process_identity or live_identity != process_identity:
                raise StartupOwnershipError(process.pid,process_identity,'startup helper ownership unknown; descendant reconciliation required')
            try: os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError: pass
            try: await asyncio.wait_for(process.wait(), 2)
            except asyncio.TimeoutError:
                raise StartupOwnershipError(process.pid,process_identity,'startup helper reap timeout')
