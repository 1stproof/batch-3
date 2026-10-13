"""Explicit-browsing, subscription-only Codex transport for host-owned campaigns.

This module only defines infrastructure.  Importing it does not start Codex or a
probe.  ``call_stage`` sends the supplied prompt and any fixed scoped-tool guidance on stdin, preserves the
raw event stream, and fails a response closed if Codex reports a tool item.

Authentication, session persistence, and model transport belong to the Codex
host process.  They are deliberately not presented to the worker as tools.  A
fresh worker can see only its stdin prompt; a resumed worker additionally has
the selected Codex conversation.  Stage working directories are otherwise
empty and are separate from the artifact directory.
"""

from __future__ import annotations

import asyncio
import datetime as _datetime
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import stat
import sys
import time
import uuid
from typing import Any, Mapping


def authentication_mode() -> str:
    """Explicit nonsecret selector; a saved ChatGPT run never opts into API by fallback."""
    mode = os.environ.get("MERLEAN_CODEX_AUTH", "chatgpt")
    if mode not in {"chatgpt", "api"}:
        raise ValueError("MERLEAN_CODEX_AUTH must be chatgpt or api")
    return mode


def paper_workspace_files(workspace: Path) -> dict[str, str]:
    """Bind a completed writer's actual files, never link targets or file bodies."""
    workspace = Path(workspace)
    if workspace.resolve(strict=True) != workspace or not workspace.is_dir():
        raise ValueError('paper workspace is not canonical')
    result = {}
    for path in sorted(workspace.rglob('*')):
        info = path.lstat()
        if stat.S_ISDIR(info.st_mode):
            continue
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ValueError('paper workspace contains a link or nonregular member')
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        try:
            before = os.fstat(descriptor)
            with os.fdopen(descriptor, 'rb', closefd=False) as stream:
                digest = hashlib.file_digest(stream, 'sha256').hexdigest()
            after = os.fstat(descriptor)
            current = path.lstat()
            identity = lambda value: (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_nlink)
            if identity(info) != identity(before) or identity(before) != identity(after) or identity(after) != identity(current):
                raise ValueError('paper workspace changed during completion binding')
            result[path.relative_to(workspace).as_posix()] = digest
        finally:
            os.close(descriptor)
    return result


def subscription_environment() -> dict[str, str]:
    """Authentication stays in Codex; no API/provider or parent-thread overrides."""
    allowed = {"HOME", "PATH", "USER", "LOGNAME", "TMPDIR", "LANG", "LC_ALL", "CODEX_HOME", "MERLEAN_CODEX_AUTH"}
    return {key: value for key, value in os.environ.items() if key in allowed}


def subscription_preflight(codex_binary: str = "codex") -> dict[str, str]:
    import subprocess
    env = subscription_environment()
    mode = authentication_mode()
    result = subprocess.run([codex_binary, "login", "status"], env=env, capture_output=True, text=True, timeout=5)
    status = (result.stdout + result.stderr).strip()
    valid = status == "Logged in using ChatGPT" if mode == "chatgpt" else sum(line.startswith("Logged in using an API key") for line in status.splitlines()) == 1
    if result.returncode or not valid:
        # Never include login output: API status may contain a credential prefix.
        raise RuntimeError("Codex selected authentication is unavailable; account fallback is disabled")
    version = subprocess.run([codex_binary, "--version"], env=env, capture_output=True, text=True, check=True, timeout=5).stdout.strip()
    if version not in {"codex-cli 0.153.0", "codex-cli 0.157.1", "codex-cli 0.159.2"}:
        raise RuntimeError("This experimental transport requires a new boundary audit for CLI " + version)
    return {"authentication": mode, "cli_version": version}


# Disable every current model-facing execution, retrieval, app, image, memory,
# delegation, permission-request, and extension surface relevant to this run.
# The list intentionally includes deprecated aliases used by the frozen runner;
# Codex may report those as harmless error items, which are preserved in events.
DISABLED_FEATURES = (
    "apps",
    "plugins",
    "remote_plugin",
    "skill_search",
    "skill_mcp_dependency_install",
    "browser_use",
    "browser_use_external",
    "browser_use_full_cdp_access",
    "computer_use",
    "image_generation",
    "multi_agent",
    "multi_agent_v2",
    "multi_agent_mode",
    "enable_fanout",
    "collaboration_modes",
    "shell_tool",
    "unified_exec",
    "code_mode",
    "code_mode_host",
    "js_repl",
    "artifact",
    "view_image",
    "memories",
    "hooks",
    "goals",
    "sleep_tool",
    "standalone_web_search",
    "web_search_request",
    "web_search_cached",
    "enable_mcp_apps",
    "plugin_sharing",
    "tool_suggest",
    "recommended_plugins",
    "workspace_dependencies",
    "request_permissions_tool",
    "tool_call_mcp_elicitation",
    "auth_elicitation",
    "executor_capability_discovery",
    "deferred_executor",
    "default_mode_request_user_input",
    "send_async_message",
    "in_app_browser",
    "in_app_chat",
    "shell_snapshot",
    "chronicle",
    "external_agent_memory_import",
    "apply_patch_freeform",
    "in_app_local_automation",
)

PASSIVE_ITEM_TYPES = {
    "agent_message",
    "reasoning",
    "error",
    "plan",
    "todo_list",
}
SAFE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")


def utc_now() -> str:
    return _datetime.datetime.now(_datetime.timezone.utc).isoformat()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def _atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".next")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _valid_name(name: str) -> str:
    if not isinstance(name, str) or SAFE_NAME.fullmatch(name) is None:
        raise ValueError("stage name must use only letters, digits, '.', '_', '-', and '/'")
    parts = name.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ValueError("stage name must not contain empty, '.' or '..' path segments")
    return name


def _stage_paths(root: Path, name: str) -> tuple[Path, Path]:
    directory = (root / "runtime").joinpath(*_valid_name(name).split("/"))
    return directory, directory / "stage"


def _request_id(
    name: str, prompt_hash: str, model: str, resume_session: str | None,
    internet_browse: bool = True, reasoning_effort: str = "high",
) -> str:
    identity = {
        "schema": "codex-stage-request-v2",
        "internet_browse": internet_browse,
        "reasoning_effort": reasoning_effort,
        "name": name,
        "prompt_sha256": prompt_hash,
        "model_requested": model,
        "resume_session": resume_session,
    }
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode()
    return "b2l-" + sha256_bytes(encoded)


DOCUMENT_CAPABILITY_PROFILE = {
    'tool_mode': 'direct',
    'supports_search_tool': False,
    'multi_agent_version': None,
    'apply_patch_tool_type': None,
    'experimental_supported_tools': [],
}


def _document_model_catalog(artifact_dir: Path, model: str, *, internet_browse=False, codex_binary="codex") -> dict:
    """Freeze actual model metadata, changing only explicit host tool capabilities.

    Model metadata overrides several CLI feature switches in 0.157.1. A scoped
    document stage therefore needs a direct, undeferred, non-delegating profile.
    Never replace missing real metadata with the CLI's permissive fallback model.
    """
    from pilot_document_tools import regular_bytes
    env = subscription_environment()
    home = Path(env.get('CODEX_HOME', str(Path(env.get('HOME', str(Path.home()))) / '.codex')))
    cache_path = (home / 'models_cache.json').resolve()
    source_kind = 'codex-model-cache'
    if not cache_path.exists() and authentication_mode() == 'api':
        import subprocess
        bundled = subprocess.run([codex_binary, 'debug', 'models', '--bundled'],
            env=env, capture_output=True, timeout=10, check=False)
        if bundled.returncode:
            raise ValueError('bundled API model metadata unavailable')
        data = bundled.stdout
        source_kind = 'cli-bundled-metadata-not-provider-entitlement'
    else:
        data = regular_bytes(cache_path)
    try:
        cache = json.loads(data)
    except (ValueError, UnicodeError) as error:
        raise ValueError('invalid model metadata cache') from error
    if (type(cache) is not dict or type(cache.get('models')) is not list
            or any(type(item) is not dict for item in cache['models'])):
        raise ValueError('invalid model metadata catalog')
    matches = [item for item in cache['models'] if item.get('slug') == model]
    if len(matches) != 1:
        raise ValueError('document stage requires exactly one actual requested model metadata record')
    original = matches[0]
    if (not set(DOCUMENT_CAPABILITY_PROFILE).issubset(original)
            or original['tool_mode'] not in ('direct', 'code_mode_only')
            or type(original['supports_search_tool']) is not bool
            or original['multi_agent_version'] not in (None, 'v1', 'v2')
            or original['apply_patch_tool_type'] not in (None, 'freeform', 'function')
            or type(original['experimental_supported_tools']) is not list
            or any(type(value) is not str for value in original['experimental_supported_tools'])):
        raise ValueError('unknown model capability metadata requires a new transport audit')
    # This field controls deferred tool discovery, not native web search.
    # Enabling it hides direct MCP schemas even with tool_mode='direct'.
    # Browsing remains controlled independently by the command's web flags.
    profile = dict(DOCUMENT_CAPABILITY_PROFILE)
    derived = {**original, **profile}
    artifacts = {}
    for name, value in [('document-model-source.json', original), ('document-model-catalog.json', derived)]:
        body = (json.dumps({'models': [value]}, ensure_ascii=False, indent=2) + '\n').encode()
        path = artifact_dir / name
        with path.open('xb') as stream:
            stream.write(body); stream.flush(); os.fsync(stream.fileno())
        artifacts[name] = {'path': str(path.resolve()), 'sha256': sha256_bytes(body)}
    return {'schema_version': 1, 'model': model, 'source_cache_path': str(cache_path),
            'source_cache_sha256': sha256_bytes(data), 'source_cache_client_version': cache.get('client_version'),
            'source_kind': source_kind, 'provider_availability_verified': False,
            'source': artifacts['document-model-source.json'], 'catalog': artifacts['document-model-catalog.json'],
            'capability_overrides': json.loads(json.dumps(profile)),
            'unchanged_non_capability_metadata': True}


def _command(
    model: str, reasoning_effort: str, resume_session: str | None, *, internet_browse: bool = True, codex_binary: str = "codex", document_capability: dict | None = None,
    document_runtime: dict | None = None, document_output_budget: int | None = None, document_model_catalog: dict | None = None, paper_profile: str | None = None, paper_capability: dict | None = None
) -> list[str]:
    if paper_profile not in (None, "author", "review"):
        raise ValueError("unknown paper tool profile")
    command = [codex_binary, "exec"]
    if resume_session:
        command.append("resume")
    command.extend(
        [
            "--ignore-user-config",
            "--ignore-rules",
            "--skip-git-repo-check",
            "-m",
            model,
            "--json",
            "-c",
            "model_reasoning_effort=" + json.dumps(reasoning_effort),
            "-c",
            'web_search="live"' if internet_browse else 'web_search="disabled"',
            "-c", 'forced_login_method=' + json.dumps(authentication_mode()),
            "-c", 'model_provider="openai"',
            "--enable", "skip_host_skill_discovery",
            "-c",
            "project_doc_max_bytes=0",
            "-c",
            'approval_policy="never"',
            "-c",
            'sandbox_mode=' + json.dumps('read-only'),
            "-c",
            "experimental_use_unified_exec_tool=" + "false",
            "-c",
            "tools.experimental_request_user_input.enabled=false",
            "-c",
            "tools.update_plan.enabled=false",
            "-c",
            "include_collaboration_mode_instructions=false",
            "-c",
            "agents.enabled=false",
            "-c",
            "agents.max_concurrent_threads_per_session=1",
            "-c",
            "agents.max_depth=0",
        ]
    )
    for feature in DISABLED_FEATURES:
        if internet_browse and feature in {"standalone_web_search", "code_mode", "code_mode_host"}:
            continue
        command.extend(["--disable", feature])
    if paper_capability is not None:
        from pilot_paper_tools import config
        command.extend(['-c', config(paper_capability)])
    if internet_browse:
        # This CLI exposes web through Code Mode. Do not specify both enable and
        # disable: CLI feature precedence is not command-line-order precedence.
        for feature in ("standalone_web_search", "code_mode", "code_mode_host"):
            command.extend(["--enable", feature])
    if document_model_catalog is not None:
        command.extend(['-c', 'model_catalog_json=' + json.dumps(document_model_catalog['catalog']['path'])])
    if document_capability is not None:
        # This sole local server enforces fixed document identities itself. Global
        # shell/exec remains disabled; no user-configured MCP server is inherited.
        from pilot_document_startup import server_config
        if document_runtime is None:
            raise ValueError('document capability requires a copied verified runtime')
        config = server_config(document_capability, document_runtime)
        command.extend(['-c', config])
        if document_output_budget is not None:
            command.extend(['-c', 'tool_output_token_limit=' + str(document_output_budget)])
    if resume_session:
        command.extend([resume_session, "-"])
    else:
        command.append("-")
    return command


def _tool_event(event: Mapping[str, Any]) -> bool:
    """Return true for any CLI item or top-level event that represents a tool."""
    event_type = event.get("type")
    if isinstance(event_type, str) and (
        "tool" in event_type.lower()
        or event_type.endswith("_call")
        or event_type in {"command_execution", "file_change", "mcp_call", "web_search"}
    ):
        return True
    item = event.get("item")
    if not isinstance(item, Mapping):
        return False
    item_type = item.get("type")
    return isinstance(item_type, str) and item_type not in PASSIVE_ITEM_TYPES


def _paper_discovery_arguments(arguments):
    """Only inventory discovery for the sole explicitly installed paper server."""
    from pilot_paper_tools import SERVER
    return isinstance(arguments, dict) and (arguments == {} or arguments == {'server': SERVER})


def _allowed_paper_discovery_event(event, *, resources_only=False):
    item = event.get('item', {})
    return (event.get('type') in ('item.started', 'item.updated', 'item.completed')
            and isinstance(item, dict) and item.get('type') == 'mcp_tool_call'
            and (item.get('server') == 'codex' or (not resources_only
                 and item.get('server') == 'merlean_paper'
                 and item.get('tool') in {'list_mcp_resources', 'list_mcp_resource_templates'}
                 and item.get('arguments') == {'server': 'merlean_paper'}))
            and item.get('tool') in ({'list_mcp_resources'} if resources_only else {'list_mcp_resources', 'list_mcp_resource_templates'})
            and _paper_discovery_arguments(item.get('arguments')))


def _allowed_persisted_paper_discovery(event, *, resources_only=False):
    from pilot_paper_tools import SERVER
    hashes = {sha256_text(json.dumps(args, ensure_ascii=False, separators=(',', ':'), allow_nan=False))
              for args in ({}, {'server': SERVER})}
    return (event.get('rollout_event_type') == 'response_item'
            and event.get('payload_type') == 'function_call' and event.get('namespace') is None
            and event.get('name') in ({'list_mcp_resources'} if resources_only else {'list_mcp_resources', 'list_mcp_resource_templates'})
            and event.get('arguments_canonical_sha256') in hashes)


def only_benign_paper_discovery_violation(meta):
    """Authenticate the rejected transport category; never marks it completed.

    A recovery caller must separately authenticate saved files, ownership, the
    original session and a single explicit corrective admission.
    """
    live = meta.get('tool_events') or []
    persisted = meta.get('persisted_tool_events') or []
    return (meta.get('status') == 'invalid_tool_attempt'
            and meta.get('module') == 'paper-light-author'
            and meta.get('model_verified') is True
            and (meta.get('persisted_rollout_audit') or {}).get('status') == 'verified'
            and not meta.get('protocol_errors') and not meta.get('failure_codes')
            and bool(live) and bool(persisted)
            and all(_allowed_paper_discovery_event(item.get('event', {}), resources_only=True) for item in live)
            and all(_allowed_persisted_paper_discovery(item, resources_only=True) for item in persisted))


def _allowed_paper_event(event, profile):
    from pilot_paper_tools import TOOLS, SERVER
    if profile not in ('author', 'review'): return False
    if _allowed_paper_discovery_event(event): return True
    item=event.get('item',{})
    return (event.get('type') in ('item.started','item.updated','item.completed')
            and item.get('type')=='mcp_tool_call' and item.get('server')==SERVER
            and item.get('tool') in TOOLS and (profile=='author' or item.get('tool') not in ('write_file','compile_paper')))


def _allowed_persisted_paper_event(event,profile):
    from pilot_paper_tools import NAMESPACE, TOOLS
    if profile not in ('author', 'review'): return False
    if _allowed_persisted_paper_discovery(event): return True
    return (event.get('rollout_event_type')=='response_item' and event.get('payload_type')=='function_call'
        and event.get('namespace')==NAMESPACE and event.get('name') in TOOLS
        and (profile=='author' or event.get('name') not in ('write_file','compile_paper')))


def _allowed_web_event(event: Mapping[str, Any]) -> bool:
    """Allow only known CLI web item envelopes; never a generic tool wrapper."""
    item = event.get("item")
    return (event.get("type") in {"item.started", "item.updated", "item.completed"}
            and isinstance(item, Mapping) and item.get("type") == "web_search")


def _literal_web_bridge(payload: Mapping[str, Any]) -> bool:
    """Recognize one literal web call, never general JavaScript execution.

    Accept exactly text(await tools.web__run(JSON_OBJECT));. JSON decoding
    rejects expressions, function bodies, interpolation, comments and trailing
    statements. Keep this grammar deliberately narrow and independent of the
    model's own account of what it did. Other tool calls remain violations.
    """
    if (payload.get("type") != "custom_tool_call" or payload.get("name") != "exec"
            or payload.get("namespace") not in {None, "functions"}):
        return False
    source = payload.get("input")
    if not isinstance(source, str):
        return False
    match = re.fullmatch(r"\s*text\(await tools\.web__run\((.*)\)\);?\s*", source, re.DOTALL)
    if not match:
        return False
    return _web_request_json(match.group(1))


def _web_request_json(source: object) -> bool:
    """Apply the same narrow request envelope to native and bridged web calls."""
    if not isinstance(source, str):
        return False
    try:
        request = json.loads(source, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (ValueError, RecursionError):
        return False
    operations = {"search_query", "open", "click", "find", "screenshot", "image_query"}
    return (isinstance(request, dict) and bool(operations.intersection(request))
            and not (request.keys() - operations - {"response_length"}))


def _native_web_call(payload: Mapping[str, Any]) -> bool:
    """Recognize the pinned CLI's direct web.run from the actual rollout payload."""
    return (payload.get("type") == "function_call"
            and payload.get("namespace") == "web" and payload.get("name") == "run"
            and _web_request_json(payload.get("arguments")))


def _allowed_persisted_web_event(event: Mapping[str, Any]) -> bool:
    return (event.get("payload_type") == "web_search_call"
            or event.get("verified_web_bridge") == "literal-web-run-v1"
            or (event.get("verified_native_web") == "native-web-run-v1"
                and event.get("payload_type") == "function_call"
                and event.get("namespace") == "web" and event.get("name") == "run"))


def _tool_output_part(text):
    """Hash actual model-visible text and the pinned CLI's explicit clipping form."""
    result = {'sha256': sha256_text(text), 'characters': len(text), 'clippings': [],
              'wall_time_framing': re.fullmatch(r'Wall time: [0-9]+(?:\.[0-9]+)? seconds\nOutput:', text) is not None}
    for match in re.finditer(r'…([0-9]+) chars truncated…', text):
        prefix, suffix = text[:match.start()], text[match.end():]
        result['clippings'].append({'prefix_characters': len(prefix), 'suffix_characters': len(suffix),
            'removed_characters': int(match.group(1)), 'prefix_sha256': sha256_text(prefix),
            'suffix_sha256': sha256_text(suffix)})
    return result


def _persisted_tool_audit(session_id: str | None, start_utc: str) -> dict[str, Any]:
    """Find host tool calls omitted from ``codex exec --json``.

    The exact stage start filters earlier turns when a session is resumed. Tool
    arguments are hashed rather than copied into the receipt.
    """
    if not session_id:
        return {"status": "unavailable", "reason": "missing_session_id", "tool_events": []}
    try:
        start = _datetime.datetime.fromisoformat(start_utc.replace("Z", "+00:00"))
    except ValueError:
        return {"status": "unavailable", "reason": "invalid_start_utc", "tool_events": []}
    session_root = Path(subscription_environment().get("CODEX_HOME", str(Path.home() / ".codex"))) / "sessions"
    paths: list[Path] = []
    for _attempt in range(6):
        paths = []
        for delta in (-1, 0, 1):
            day = (start + _datetime.timedelta(days=delta)).date()
            folder = session_root / f"{day.year:04d}" / f"{day.month:02d}" / f"{day.day:02d}"
            if folder.is_dir():
                paths.extend(folder.glob(f"*{session_id}.jsonl"))
        if paths:
            break
        time.sleep(0.2)
    if not paths:
        paths = list(session_root.glob(f"*/*/*/*{session_id}.jsonl"))
    if not paths:
        return {"status": "unavailable", "reason": "rollout_not_found", "tool_events": []}
    findings: list[dict[str, Any]] = []
    turn_contexts: list[dict[str, Any]] = []
    read_errors: list[str] = []
    response_usage_records: list[dict[str, Any]] = []
    tool_output_receipts: list[dict[str, Any]] = []
    context_models: dict[str, set[str | None]] = {}
    tool_types = {
        "function_call", "custom_tool_call", "tool_search_call",
        "local_shell_call", "mcp_tool_call", "image_generation_call", "web_search_call",
    }
    for path in sorted(set(paths)):
        try:
            stream = path.open(encoding="utf-8")
        except OSError as error:
            read_errors.append(type(error).__name__ + ": " + str(error))
            continue
        with stream:
            for line in stream:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    read_errors.append("malformed rollout JSON")
                    continue
                if not isinstance(event, dict):
                    read_errors.append("non-object rollout event")
                    continue
                timestamp = event.get("timestamp")
                try:
                    when = _datetime.datetime.fromisoformat(
                        str(timestamp).replace("Z", "+00:00")
                    )
                except ValueError:
                    read_errors.append("invalid rollout timestamp")
                    continue
                if when.tzinfo is None:
                    read_errors.append("timezone missing in rollout timestamp")
                    continue
                payload = event.get("payload", {})
                if event.get("type") == "turn_context" and isinstance(payload, Mapping):
                    turn_id = payload.get("turn_id")
                    host_model = payload.get("model")
                    if isinstance(turn_id, str) and turn_id:
                        # Keep every identity, including an invalid/missing model.
                        # Conflicting contexts must never become last-write-wins.
                        context_models.setdefault(turn_id, set()).add(
                            host_model if isinstance(host_model, str) and host_model.strip() else None
                        )
                if when < start:
                    continue
                if event.get("type") == "token_usage_record" and isinstance(payload, Mapping):
                    response_usage_records.append({"timestamp": timestamp, "payload": dict(payload),
                                                   "model": None})
                if event.get("type") == "turn_context" and isinstance(payload, Mapping):
                    turn_contexts.append({"model": payload.get("model"), "turn_id": payload.get("turn_id")})
                if event.get("type") == "response_item" and isinstance(payload, Mapping):
                    payload_type = payload.get("type")
                    if payload_type == 'function_call_output':
                        output = payload.get('output')
                        texts = ([output] if isinstance(output, str) else
                                 [part['text'] for part in output if isinstance(part, dict)
                                  and part.get('type') in ('input_text', 'text') and isinstance(part.get('text'), str)]
                                 if isinstance(output, list) else [])
                        tool_output_receipts.append({'call_id': payload.get('call_id'),
                            'text_sha256': [sha256_text(text) for text in texts],
                            'output_format': 'list' if isinstance(output, list) else 'other',
                            'text_parts': [({**_tool_output_part(part['text']), 'type': part.get('type'), 'keys': sorted(part)}
                                if isinstance(part, dict) and isinstance(part.get('text'), str)
                                else {'type': None, 'keys': []}) for part in output] if isinstance(output, list) else [],
                            'output_sha256': sha256_text(json.dumps(output, ensure_ascii=False, separators=(',', ':')))})
                    if payload_type in tool_types or (isinstance(payload_type, str) and payload_type.endswith("_call")):
                        arguments = payload.get("arguments", payload.get("input", ""))
                        canonical_arguments = None
                        try:
                            parsed_arguments = json.loads(arguments) if isinstance(arguments, str) else arguments
                            if isinstance(parsed_arguments, dict):
                                canonical_arguments = sha256_text(json.dumps(parsed_arguments, ensure_ascii=False, separators=(',', ':'), allow_nan=False))
                        except (ValueError, TypeError):
                            pass
                        findings.append({
                            "timestamp": timestamp,
                            "rollout_event_type": "response_item",
                            "payload_type": payload_type,
                            "namespace": payload.get("namespace"),
                            "name": payload.get("name"),
                            "call_id": payload.get("call_id"),
                            "arguments_sha256": sha256_text(str(arguments)),
                            "arguments_canonical_sha256": canonical_arguments,
                            "verified_web_bridge": "literal-web-run-v1" if _literal_web_bridge(payload) else None,
                            "verified_native_web": "native-web-run-v1" if _native_web_call(payload) else None,
                        })
                if event.get("type") == "event_msg" and isinstance(payload, Mapping):
                    item = payload.get("item", {})
                    if (
                        payload.get("type") == "item_completed"
                        and isinstance(item, Mapping)
                        and item.get("type") == "SubAgentActivity"
                    ):
                        findings.append({
                            "timestamp": timestamp,
                            "rollout_event_type": "subagent_activity",
                            "kind": item.get("kind"),
                            "agent_thread_id": item.get("agent_thread_id"),
                            "agent_path": item.get("agent_path"),
                        })
    # Usage may precede its turn_context (notably a compaction response).
    # Resolve only after every context has been inspected, by exact turn ID.
    # This is the host-reported turn model, not independent backend-model proof.
    for record in response_usage_records:
        turn_id = record["payload"].get("turn_id")
        models = context_models.get(turn_id, set()) if isinstance(turn_id, str) else set()
        record["model"] = next(iter(models)) if len(models) == 1 and None not in models else None
    attribution = "unique exact turn_context model; backend response model not independently verified"
    if read_errors:
        return {
            "status": "unavailable",
            "reason": "rollout_read_error",
            "read_errors": read_errors,
            "response_usage_records": response_usage_records,
        "tool_output_receipts": tool_output_receipts,
            "usage_model_attribution": attribution,
            "turn_contexts": turn_contexts,
            "tool_events": findings,
        }
    return {
        "status": "verified",
        "rollout_paths": [str(path) for path in sorted(set(paths))],
        "tool_events": findings,
        "turn_contexts": turn_contexts,
        "response_usage_records": response_usage_records,
        "tool_output_receipts": tool_output_receipts,
        "usage_model_attribution": attribution,
    }


def extract_answer(text: str) -> tuple[object | None, str | None, str | None]:
    """Extract a whole-response JSON value and useful Markdown, without rewriting it.

    Returns ``(json_value, markdown, parse_error)``.  A Markdown fence around one
    JSON value is accepted.  If the JSON object contains ``proof_markdown`` or
    ``markdown``, that exact string is extracted; otherwise non-JSON text is
    treated as Markdown.
    """
    stripped = text.strip()
    candidate = stripped
    if stripped.startswith("```") and stripped.endswith("```"):
        first_newline = stripped.find("\n")
        if first_newline >= 0:
            candidate = stripped[first_newline + 1 : -3].strip()
    try:
        value = json.loads(candidate)
    except json.JSONDecodeError as error:
        markdown = text if text else None
        return None, markdown, f"{error.msg} at line {error.lineno} column {error.colno}"
    markdown = None
    if isinstance(value, Mapping):
        for key in ("proof_markdown", "markdown"):
            field = value.get(key)
            if isinstance(field, str):
                markdown = field
                break
    return value, markdown, None


def _paper_image_inputs(paths, artifact_dir: Path) -> list[dict]:
    """Copy host-rendered PNG pages; reject aliases and bind exact reviewed bytes."""
    records = []
    seen = set()
    for index, value in enumerate(paths):
        path = Path(value).absolute()
        if any(part.is_symlink() for part in (path, *path.parents)):
            raise ValueError("paper image inputs cannot contain symlinks")
        info = path.stat()
        identity = (info.st_dev, info.st_ino)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or identity in seen:
            raise ValueError("paper image inputs must be distinct regular single-link files")
        seen.add(identity)
        data = path.read_bytes()
        if path.suffix.lower() != '.png' or not data.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError("paper visual review accepts rendered PNG pages only")
        target = artifact_dir / f'page-{index + 1:03d}.png'
        with target.open('xb') as handle:
            handle.write(data)
        target.chmod(0o444)
        records.append({'source': str(path), 'path': str(target), 'sha256': sha256_bytes(data)})
    if not records:
        raise ValueError("paper image input list must not be empty")
    return records


def _paper_images_unchanged(records: list[dict]) -> bool:
    try:
        return all(not Path(item[key]).is_symlink()
                   and sha256_bytes(Path(item[key]).read_bytes()) == item['sha256']
                   for item in records for key in ('source', 'path'))
    except OSError:
        return False


async def call_stage(
    root: Path,
    name: str,
    prompt: str,
    model: str,
    timeout: float,
    resume_session: str | None = None,
    *,
    internet_browse: bool = True,
    codex_binary: str = "codex",
    module: str | None = None,
    reasoning_effort: str = "high",
    accounting_price_card: Path | None = None,
    accounting_context: dict[str, str] | None = None,
    document_scope: dict | None = None,
    document_recovery_from: dict | None = None,
    image_paths: list[Path] | None = None,
    paper_workspace: Path | None = None,
    paper_evidence_root: Path | None = None,
) -> tuple[dict[str, Any], object]:
    """Run one isolated Codex turn and return its metadata and extracted answer.

    This function is the only model-launching entry point in this module.  It
    refuses to overwrite a prior stage.  Passing ``resume_session`` performs a
    real ``codex exec resume``; omitting it creates a fresh Codex conversation.
    """
    config_path = Path(root).resolve().parent/'host-config.json'
    inherited = json.loads(config_path.read_text()).get('reconciled_document_helpers', {}) if config_path.is_file() else {}
    for receipt in (Path(root).resolve()/'runtime').glob('*/*/document-startup.json'):
        record = json.loads(receipt.read_text())
        if (record.get('cleanup') or {}).get('status') == 'UNKNOWN':
            key = str(receipt.relative_to(Path(root).resolve()))
            if inherited.get(key) == sha256_bytes(receipt.read_bytes()):
                continue  # Exact historical helper already covered by native stopped-process reconciliation.
            raise RuntimeError('unresolved document helper ownership blocks further model dispatch; reconcile externally')
    if not isinstance(internet_browse, bool):
        raise TypeError("internet_browse must be boolean")
    if accounting_context is not None:
        if (type(accounting_context) is not dict
                or set(accounting_context) != {'phase', 'segment_id', 'purpose'}
                or any(not isinstance(value, str) or not value.strip() for value in accounting_context.values())):
            raise ValueError('invalid host accounting context')
        accounting_context = dict(accounting_context)
    if paper_evidence_root is not None and paper_workspace is None:
        raise ValueError("paper evidence requires explicit paper workspace")
    paper_profile = None
    if paper_workspace is not None:
        if module not in {"paper-light-author", "paper-light-review"} or document_scope is not None or image_paths is not None or document_recovery_from is not None:
            raise ValueError("paper workspace requires an exclusive light author/reviewer profile")
        workspace = Path(paper_workspace)
        if not workspace.is_absolute() or workspace.resolve(strict=True) != workspace or not workspace.is_dir():
            raise ValueError("paper workspace must be an existing canonical directory")
        problem_id = _valid_name(name).split('/')[0]
        paper_root = Path(root).resolve().parent/'exam'/'papers'/problem_id
        if not workspace.is_relative_to(paper_root) or workspace == paper_root:
            raise ValueError('paper workspace must be inside the owned problem paper directory')
        if model != "gpt-6-astra":
            raise ValueError("light paper author/reviewer requires Astra")
        if paper_evidence_root is not None:
            paper_evidence_root=Path(paper_evidence_root)
            if paper_evidence_root.resolve(strict=True)!=paper_evidence_root or not paper_evidence_root.is_relative_to(paper_root) or paper_evidence_root==paper_root:
                raise ValueError('paper evidence root must be canonical own paper snapshot')
        paper_profile = "author" if module == "paper-light-author" else "review"
    call_deadline = time.monotonic() + timeout
    preflight_start = time.monotonic()
    authentication = await asyncio.to_thread(subscription_preflight, codex_binary)
    if config_path.is_file():
        saved_auth = json.loads(config_path.read_text()).get('auth', {}).get('authentication', 'chatgpt')
        if saved_auth != authentication['authentication']:
            raise ValueError('saved campaign authentication cannot change')
    timeout -= time.monotonic() - preflight_start
    name = _valid_name(name)
    if not isinstance(prompt, str):
        raise TypeError("prompt must be text")
    if not isinstance(model, str) or not model.strip():
        raise ValueError("model must be nonempty text")
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    if resume_session is not None and (
        not isinstance(resume_session, str) or not resume_session.strip()
    ):
        raise ValueError("resume_session must be a nonempty session id or None")
    if resume_session is not None:
        uuid.UUID(resume_session)
    if module is None:
        module = "solving/" + name
    if not isinstance(module, str) or not module.strip():
        raise ValueError("module must be nonempty text")

    if image_paths is not None and (module != "paper-visual-review" or model != "gpt-6-astra"
            or resume_session is not None or internet_browse or document_scope is not None):
        raise ValueError("images require a fresh offline Astra paper-visual-review without document tools")
    root = Path(root).resolve()
    artifact_dir, prefix = _stage_paths(root, name)
    meta_path = prefix.with_suffix(".meta.json")
    if artifact_dir.exists() or meta_path.exists():
        raise FileExistsError("refusing to overwrite campaign stage: " + str(artifact_dir))
    artifact_dir.mkdir(parents=True, exist_ok=False)

    if document_scope is not None:
        from pilot_document_tools import document_prompt
        prompt = document_prompt(prompt, document_scope.get('mode'), internet_browse)
    paper_images = _paper_image_inputs(image_paths, artifact_dir) if image_paths is not None else []
    if paper_images:
        prompt += "\nHOST IMAGE MANIFEST (ordered PDF pages):\n" + json.dumps(paper_images, sort_keys=True)
    prompt_bytes = prompt.encode("utf-8")
    prompt_hash = sha256_bytes(prompt_bytes)
    request_id = _request_id(name, prompt_hash, model, resume_session, internet_browse, reasoning_effort)
    context_dir = root / "contexts" / request_id
    context_dir.mkdir(parents=True, exist_ok=False)
    prefix.with_suffix(".prompt.txt").write_bytes(prompt_bytes)
    capability = None
    document_output_budget = None
    document_model_catalog = None
    document_recovery = None
    document_runtime = None
    document_startup = None
    paper_capability = None
    if document_recovery_from is not None and document_scope is None:
        raise ValueError('document recovery requires an explicit review scope')
    preflight_meta = {'schema_version':1, 'name':name, 'module':module,
        'request_id':request_id, 'model_requested':model, 'reasoning_effort':reasoning_effort,
        'internet_browse':internet_browse, 'authentication':authentication['authentication'],
        'cli_version':authentication['cli_version'], 'start_utc':utc_now(),
        'prompt_sha256':prompt_hash, 'prompt_bytes':len(prompt_bytes), 'timeout_seconds':timeout,
        'resume_session':resume_session, 'fresh_session':resume_session is None,
        'session_id':None, 'pid':None, 'process_identity':None, 'usage':None,
        'accounting_context':accounting_context, 'status':'document_preflight_running',
        'context_directory':str(context_dir.relative_to(root)),
        'artifact_directory':str(artifact_dir.relative_to(root)), 'model_dispatched':False}
    if document_scope is not None:
        _atomic_json(meta_path, preflight_meta)
    try:
        if document_scope is not None:
            if authentication['cli_version'] not in {'codex-cli 0.157.1', 'codex-cli 0.159.2'}:
                raise ValueError('document tools require audited CLI 0.157.1 or 0.159.2')
            from pilot_document_tools import prepare_scope, output_capacity
            document_scope, capability = prepare_scope(document_scope, artifact_dir,
                {'stage': name, 'request_id': request_id, 'session_id': resume_session}, internet_browse=internet_browse)
            from pilot_document_startup import prepare_runtime, startup_preflight
            document_runtime = prepare_runtime(artifact_dir)
            document_startup = await startup_preflight(codex_binary, capability, document_runtime,
                document_scope['mode'], cwd=context_dir, env=subscription_environment(), timeout=min(15, call_deadline-time.monotonic()), public_sources=internet_browse)
            _atomic_json(artifact_dir/'document-startup.json', document_startup)
            if call_deadline <= time.monotonic():
                raise TimeoutError('stage deadline exhausted by document startup preflight')
            document_output_budget = output_capacity(document_scope)
            document_model_catalog = _document_model_catalog(artifact_dir, model, internet_browse=internet_browse, codex_binary=codex_binary)
            if document_recovery_from is not None:
                from pilot_document_recovery import verify_recovery
                document_recovery = verify_recovery(root, document_recovery_from, name=name, module=module,
                    model=model, resume_session=resume_session, prompt=prompt, scope=document_scope)
        if paper_profile:
            from pilot_paper_tools import prepare
            paper_capability = prepare(workspace,paper_profile,artifact_dir,internet_browse,paper_evidence_root,paper_root)
            document_model_catalog = _document_model_catalog(artifact_dir,model,internet_browse=internet_browse,codex_binary=codex_binary)
        command = _command(model, reasoning_effort, resume_session, internet_browse=internet_browse,
                           codex_binary=codex_binary, document_capability=capability, document_runtime=document_runtime, document_output_budget=document_output_budget, document_model_catalog=document_model_catalog, paper_profile=paper_profile, paper_capability=paper_capability)
    except BaseException as error:
        preflight_meta.update(status='process_launch_failed', end_utc=utc_now(),
            elapsed_s=time.monotonic()-preflight_start, document_capability=capability,
            document_runtime=document_runtime, startup_failure={'type':type(error).__name__})
        from codex_accounting import account_stage
        preflight_meta['accounting'] = account_stage(root, preflight_meta, {}, price_card=accounting_price_card)
        _atomic_json(meta_path, preflight_meta)
        _atomic_json(artifact_dir/'document-startup.json', {'status':'FAIL',
            'error_type':type(error).__name__, 'model_calls':0, 'runtime':document_runtime,
            'cleanup':getattr(error,'cleanup',None)})
        raise
    timeout = call_deadline - time.monotonic()
    if paper_images:
        command[-1:-1] = [argument for item in paper_images for argument in ('--image', item['path'])]
    meta: dict[str, Any] = {
        "schema_version": 1,
        "internet_browse": internet_browse,
        "authentication": authentication["authentication"],
        "cli_version": authentication["cli_version"],
        "request_id": request_id,
        "name": name,
        "module": module,
        "accounting_context": accounting_context,
        "model_requested": model,
        "reasoning_effort": reasoning_effort,
        "start_utc": utc_now(),
        "prompt_bytes": len(prompt_bytes),
        "prompt_sha256": prompt_hash,
        "timeout_seconds": timeout,
        "deadline_utc": (_datetime.datetime.now(_datetime.timezone.utc) + _datetime.timedelta(seconds=timeout)).isoformat(),
        "resume_session": resume_session,
        "fresh_session": resume_session is None,
        "context_directory": str(context_dir.relative_to(root)),
        "artifact_directory": str(artifact_dir.relative_to(root)),
        "worker_visible_inputs": [
            "exact stdin prompt",
            "Codex host system/runtime controls containing no campaign corpus",
            *(["selected resumed Codex conversation"] if resume_session else []),
        ],
        "worker_tools": ("native web and literal Code Mode web bridge; non-web execution features disabled"
                         if internet_browse else "execution features disabled; platform namespace may still be advertised"),
        "host_only_capabilities": ["Codex authentication", "model transport", "session persistence"],
        "tool_audit": ("only native web and audited literal-web-run-v1 bridges are permitted"
                       if internet_browse else "every non-passive item or tool-shaped event invalidates the stage"),
        "command": command,
        "usage": None,
        "status": "launching",
    }
    if paper_profile:
        meta['paper_capability'] = paper_capability
        meta['paper_workspace'] = str(workspace)
        meta['paper_tool_profile'] = paper_profile
        meta['worker_tools'] = 'host-scoped paper file/compile/public-source MCP; no shell or delegation; web according to internet_browse'
        meta['tool_audit'] = 'fixed paper capability: immutable evidence reads, author-only paper.tex/references writes; confined compiler'
    if paper_images:
        meta['paper_image_inputs'] = paper_images
        meta['worker_visible_inputs'].append('hash-bound host-rendered PDF page images')
    if capability is not None:
        meta['document_capability'] = capability
        meta['document_model_profile'] = document_model_catalog
        if document_recovery is not None:
            meta['document_recovery'] = document_recovery
        meta['document_tool_output_capacity'] = {'tokens': document_output_budget,
            'derivation': 'UTF-8 serialized known response and capability sizes; capacity reservation, not a prompt rejection cap'}
        meta['worker_visible_inputs'].append('fixed document capability; exact reads and main-only draft saves')
        meta['worker_tools'] += '; scoped merlean_documents MCP tools'
        meta['tool_audit'] += '; exact document calls reconciled with durable host operation receipts'
    from codex_accounting import account_stage
    meta["accounting"] = account_stage(root, meta, {}, price_card=accounting_price_card)
    _atomic_json(meta_path, meta)
    timeout = call_deadline - time.monotonic()
    if timeout <= 0:
        meta.update(status='process_launch_failed', model_dispatched=False, end_utc=utc_now(),
                    startup_failure={'type':'DeadlineExceeded'})
        _atomic_json(meta_path, meta)
        raise TimeoutError('stage deadline exhausted before model dispatch')
    start = time.monotonic()
    launch_task = asyncio.create_task(asyncio.create_subprocess_exec(
            *command,
            cwd=str(workspace if paper_profile else context_dir),
            env=subscription_environment(),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            start_new_session=True,
            limit=4 * 1024 * 1024,
        ))
    try:
        process = await asyncio.shield(launch_task)
    except asyncio.CancelledError:
        # Resolve a possibly successful OS spawn before releasing host ownership.
        # A shielded launch retains the process handle even when its caller stops.
        try:
            process = await launch_task
        except Exception as error:
            meta['launch_error'] = {'type': type(error).__name__, 'message': str(error)}
        else:
            if process.returncode is None:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                await process.communicate()
            meta['pid'] = process.pid
            meta['exit_code'] = process.returncode
        meta.update(status='cancelled', end_utc=utc_now(), elapsed_s=time.monotonic() - start)
        meta['accounting'] = account_stage(root, meta, {}, price_card=accounting_price_card)
        _atomic_json(meta_path, meta)
        raise
    except Exception as error:
        meta.update(
            status="process_launch_failed",
            end_utc=utc_now(),
            elapsed_s=time.monotonic() - start,
            launch_error={"type": type(error).__name__, "message": str(error)},
        )
        # This branch is reached only when the awaited OS spawn itself failed.
        # Never infer non-dispatch from a provider message or a cancelled spawn.
        if isinstance(error, OSError) and error.errno in (__import__('errno').EAGAIN, __import__('errno').ENOMEM):
            meta['model_dispatched'] = False
            meta['local_spawn_failure'] = {'schema_version': 1, 'errno': error.errno,
                'boundary': 'await_create_subprocess_exec', 'model_dispatched': False}
        meta["accounting"] = account_stage(root, meta, {}, price_card=accounting_price_card)
        _atomic_json(meta_path, meta)
        if meta.get('local_spawn_failure'):
            error.pilot_stage_failure = {'name': name, 'request_id': request_id,
                'meta_sha256': hashlib.sha256(meta_path.read_bytes()).hexdigest(),
                'local_spawn_failure': meta['local_spawn_failure']}
        raise

    assert process.stdin is not None
    assert process.stdout is not None
    assert process.stderr is not None
    from campaign_watchdog import capture_process_identity
    meta.update(status="running", pid=process.pid, process_identity=capture_process_identity(process.pid))
    _atomic_json(meta_path, meta)
    messages: list[dict[str, Any]] = []
    tool_events: list[dict[str, Any]] = []
    document_events: list[dict[str, Any]] = []
    protocol_errors: list[str] = []
    turn_completed = False

    async def read_stdout() -> None:
        nonlocal turn_completed
        with prefix.with_suffix(".events.jsonl").open("w", encoding="utf-8") as stream:
            while True:
                line = await process.stdout.readline()
                if not line:
                    break
                raw = line.decode("utf-8", errors="replace").rstrip("\r\n")
                elapsed = time.monotonic() - start
                try:
                    event: dict[str, Any] = json.loads(raw)
                    if not isinstance(event, dict):
                        event = {"unparsed_json_value": event}
                        protocol_errors.append("non-object event")
                except json.JSONDecodeError:
                    event = {"unparsed": raw}
                    protocol_errors.append("non-JSON event")
                if not isinstance(event.get("type"), str):
                    protocol_errors.append("missing event type")
                envelope = {"elapsed_s": elapsed, "utc": utc_now(), "event": event}
                stream.write(json.dumps(envelope, ensure_ascii=False) + "\n")
                stream.flush()
                if event.get("type") == "thread.started":
                    if meta.get("session_id") and meta["session_id"] != event.get("thread_id"):
                        protocol_errors.append("multiple session identities")
                    meta["session_id"] = event.get("thread_id")
                    meta["process_identity"] = capture_process_identity(process.pid)
                    _atomic_json(meta_path, meta)
                if event.get("type") == "turn.failed":
                    protocol_errors.append("turn.failed")
                if event.get("type") == "turn.completed":
                    turn_completed = True
                    meta["usage"] = event.get("usage")
                item = event.get("item")
                if (
                    event.get("type") == "item.completed"
                    and isinstance(item, Mapping)
                    and item.get("type") == "agent_message"
                ):
                    if isinstance(item.get("text"), str):
                        messages.append({"elapsed_s": elapsed, "text": item["text"]})
                    else:
                        protocol_errors.append("non-text agent message")
                allowed_document = False
                if document_scope is not None:
                    from pilot_document_tools import allowed_event
                    allowed_document = allowed_event(event, document_scope)
                    if allowed_document:
                        document_events.append(event)
                if _tool_event(event) and not allowed_document and not (internet_browse and _allowed_web_event(event)) and not (paper_profile and _allowed_paper_event(event, paper_profile)):
                    tool_events.append(envelope)
                    if process.returncode is None:
                        try:
                            os.killpg(process.pid, signal.SIGTERM)
                        except ProcessLookupError:
                            pass

    async def stop_process() -> None:
        if process.returncode is None:
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                await asyncio.wait_for(process.wait(), 5)
            except asyncio.TimeoutError:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                await process.wait()

    async def send_prompt() -> None:
        process.stdin.write(prompt_bytes)
        await process.stdin.drain()
        process.stdin.close()

    stdout_task = asyncio.create_task(read_stdout())
    stderr_task = asyncio.create_task(process.stderr.read())
    send_task = asyncio.create_task(send_prompt())
    wait_task = asyncio.create_task(process.wait())
    cancellation = None
    try:
        # gather propagates reader failures immediately, before pipe backpressure can hang a child.
        await asyncio.wait_for(asyncio.gather(send_task, stdout_task, stderr_task, wait_task), max(0, timeout - (time.monotonic() - start)))
        meta["status"] = "completed" if process.returncode == 0 else "process_failed"
    except asyncio.TimeoutError:
        meta["status"] = "timeout_censored"
        await stop_process()
    except asyncio.CancelledError as error:
        meta["status"] = "cancelled"
        cancellation = error
        await stop_process()
    except Exception as error:
        meta["status"] = "transport_io_failed"
        protocol_errors.append(type(error).__name__ + ": " + str(error))
        await stop_process()
    finally:
        for task in (send_task, stdout_task, stderr_task, wait_task):
            if not task.done():
                task.cancel()
        await asyncio.gather(send_task, stdout_task, stderr_task, wait_task, return_exceptions=True)
        stderr = stderr_task.result() if not stderr_task.cancelled() and stderr_task.exception() is None else b""
        prefix.with_suffix(".stderr.txt").write_bytes(stderr)

    answer_text = messages[-1]["text"] if messages else ""
    answer_bytes = answer_text.encode("utf-8")
    prefix.with_suffix(".answer.txt").write_bytes(answer_bytes)
    _atomic_json(prefix.with_suffix(".messages.json"), messages)
    json_answer, markdown_answer, parse_error = extract_answer(answer_text)
    if json_answer is not None:
        _atomic_json(prefix.with_suffix(".answer.json"), json_answer)
        answer: object = json_answer
    else:
        answer = {"raw_answer": answer_text, "parse_error": parse_error}
    if markdown_answer is not None:
        prefix.with_suffix(".answer.md").write_text(markdown_answer, encoding="utf-8")

    meta.update(
        end_utc=utc_now(),
        elapsed_s=time.monotonic() - start,
        exit_code=process.returncode,
        answer_bytes=len(answer_bytes),
        answer_sha256=sha256_bytes(answer_bytes),
        answer_json_extracted=json_answer is not None,
        answer_markdown_extracted=markdown_answer is not None,
        answer_parse_error=parse_error,
        tool_event_count=len(tool_events),
        tool_events=tool_events,
    )
    persisted_audit = _persisted_tool_audit(
        meta.get("session_id"), meta["start_utc"]
    )
    persisted_tool_events = [event for event in persisted_audit["tool_events"]
                             if not (internet_browse and _allowed_persisted_web_event(event))
                             and not (paper_profile and _allowed_persisted_paper_event(event, paper_profile))]
    if document_scope is not None:
        from pilot_document_tools import audit_operations, NAMESPACE, TOOLS
        try:
            document_audit = audit_operations(document_scope, document_events, persisted_audit['tool_events'], meta.get('session_id'), persisted_audit.get('tool_output_receipts', []))
            if document_recovery is not None:
                from pilot_document_recovery import inherit_coverage
                document_audit = inherit_coverage(document_audit, document_recovery, scope=document_scope, actual_session=meta.get('session_id'))
        except (ValueError, OSError, KeyError, TypeError) as error:
            document_audit = {'status': 'FAIL', 'errors': [type(error).__name__],
                              'required_material_delivered': False}
        meta['document_audit'] = document_audit
        meta['document_events'] = document_events
        if document_audit['status'] == 'PASS':
            persisted_tool_events = [event for event in persisted_tool_events
                if not (event.get('namespace') == NAMESPACE and event.get('name') in TOOLS)]
        elif meta['status'] == 'completed':
            meta['status'] = 'invalid_document_tool_audit'
    contexts = persisted_audit.get("turn_contexts", [])
    meta["model_actual"] = contexts[-1].get("model") if contexts else None
    meta["model_verified"] = bool(contexts) and all(c.get("model") == model for c in contexts)
    meta["persisted_rollout_audit"] = persisted_audit
    meta["persisted_tool_event_count"] = len(persisted_tool_events)
    meta["persisted_tool_events"] = persisted_tool_events
    if persisted_audit["status"] != "verified":
        meta["status"] = "unverifiable_rollout_audit"
    elif tool_events or persisted_tool_events:
        meta["status"] = "invalid_tool_attempt"
    meta["turn_completed"] = turn_completed
    meta["protocol_errors"] = protocol_errors
    if meta["status"] == "completed" and (not turn_completed or protocol_errors or not answer_text.strip()):
        meta["status"] = "invalid_transport_completion"
    if meta["status"] == "completed" and not meta["model_verified"]:
        meta["status"] = "model_identity_unverified"
    if paper_images and not _paper_images_unchanged(paper_images):
        meta["status"] = "invalid_paper_image_inputs"
    if resume_session and meta.get("session_id") != resume_session:
        meta["status"] = "resume_identity_mismatch"
    if paper_profile and meta['status'] == 'completed':
        try:
            meta['paper_workspace_files'] = paper_workspace_files(workspace)
        except (ValueError, OSError) as error:
            meta['status'] = 'invalid_paper_workspace_completion'
            meta['paper_workspace_error'] = type(error).__name__
    meta["accounting"] = account_stage(root, meta, persisted_audit, price_card=accounting_price_card)
    _atomic_json(meta_path, meta)
    if cancellation is not None:
        raise cancellation
    return meta, answer
