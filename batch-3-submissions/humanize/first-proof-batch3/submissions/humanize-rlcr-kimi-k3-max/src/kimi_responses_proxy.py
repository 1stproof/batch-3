#!/usr/bin/env python3
"""Bridge Codex Responses requests to the Kimi Chat Completions endpoint."""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


HOP_HEADERS = {
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailers",
    "transfer-encoding",
    "upgrade",
}
TOOL_CALL_TYPES = {"function_call", "custom_tool_call", "local_shell_call"}
TOOL_OUTPUT_TYPES = {
    "function_call_output",
    "custom_tool_call_output",
    "local_shell_call_output",
}


class CompatibilityState:
    def __init__(self, log_path: Path | None) -> None:
        self.call_names: dict[str, str] = {}
        self.call_responses: dict[str, str] = {}
        self.lock = threading.Lock()
        self.log_path = log_path
        self.log_lock = threading.Lock()

    def remember(self, item: object) -> None:
        if not isinstance(item, dict):
            return
        kind = item.get("type")
        if not isinstance(kind, str) or kind not in TOOL_CALL_TYPES:
            return
        call_id = item.get("call_id") or item.get("id")
        name = item.get("name") or item.get("tool")
        if isinstance(call_id, str) and isinstance(name, str):
            with self.lock:
                self.call_names[call_id] = name

    def tool_name(self, call_id: object) -> str | None:
        if not isinstance(call_id, str):
            return None
        with self.lock:
            return self.call_names.get(call_id)

    def remember_response(self, call_ids: list[str], response_id: str) -> None:
        with self.lock:
            for call_id in call_ids:
                self.call_responses[call_id] = response_id

    def response_id(self, call_id: object) -> str | None:
        if not isinstance(call_id, str):
            return None
        with self.lock:
            return self.call_responses.get(call_id)

    def log(self, record: dict[str, object]) -> None:
        if self.log_path is None:
            return
        line = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
        with self.log_lock:
            with self.log_path.open("a", encoding="utf-8") as stream:
                stream.write(line)


def iter_dicts(value: object):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_dicts(child)


def patch_tool_outputs(payload: object, state: CompatibilityState) -> int:
    patched = 0
    for item in iter_dicts(payload):
        state.remember(item)
        kind = item.get("type")
        if isinstance(kind, str) and kind in TOOL_CALL_TYPES:
            name = item.get("name")
            if isinstance(name, str) and not isinstance(item.get("tool"), dict):
                item["tool"] = {"name": name}
                patched += 1
            if "role" not in item:
                item["role"] = "assistant"
                patched += 1
        if not isinstance(kind, str) or kind not in TOOL_OUTPUT_TYPES:
            continue
        if isinstance(item.get("name"), str) or isinstance(item.get("tool"), str):
            continue
        name = state.tool_name(item.get("call_id"))
        if name is not None:
            item["name"] = name
            item["tool"] = {"name": name}
            item["role"] = "tool"
            patched += 1
    return patched


def event_metadata(payload: object) -> dict[str, object] | None:
    if not isinstance(payload, dict):
        return None
    item = payload.get("item")
    response = payload.get("response")
    result: dict[str, object] = {"event": payload.get("type", "unknown")}
    if isinstance(item, dict):
        result.update(
            item_type=item.get("type"),
            call_id=item.get("call_id") or item.get("id"),
            name=item.get("name") or item.get("tool"),
        )
    if isinstance(response, dict):
        result["response_id"] = response.get("id")
    return result


def content_for_chat(content: object) -> object:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return str(content) if content is not None else ""
    converted = []
    for part in content:
        if not isinstance(part, dict):
            converted.append({"type": "text", "text": str(part)})
            continue
        kind = part.get("type")
        if kind in {"input_text", "output_text", "text"}:
            converted.append({"type": "text", "text": str(part.get("text", ""))})
        elif kind in {"input_image", "image_url"}:
            image_url = part.get("image_url") or part.get("url")
            if isinstance(image_url, dict):
                image_url = image_url.get("url")
            if isinstance(image_url, str):
                converted.append({"type": "image_url", "image_url": {"url": image_url}})
    if not converted:
        return ""
    if all(part.get("type") == "text" for part in converted):
        return "\n".join(str(part.get("text", "")) for part in converted)
    return converted


def responses_to_chat(payload: dict[str, object]) -> tuple[dict[str, object], set[str]]:
    messages: list[dict[str, object]] = []
    instructions = payload.get("instructions")
    if isinstance(instructions, str) and instructions:
        messages.append({"role": "system", "content": instructions})

    call_names: dict[str, str] = {}
    custom_names: set[str] = set()
    raw_input = payload.get("input")
    if isinstance(raw_input, str):
        messages.append({"role": "user", "content": raw_input})
    elif isinstance(raw_input, list):
        for item in raw_input:
            if not isinstance(item, dict):
                continue
            kind = item.get("type")
            if kind == "message":
                role = str(item.get("role", "user"))
                if role == "developer":
                    role = "system"
                if role not in {"system", "user", "assistant", "tool"}:
                    role = "user"
                message: dict[str, object] = {
                    "role": role,
                    "content": content_for_chat(item.get("content")),
                }
                if role == "tool":
                    for key in ("name", "tool_call_id"):
                        if item.get(key) is not None:
                            message[key] = item[key]
                messages.append(message)
            elif kind in TOOL_CALL_TYPES:
                call_id = str(item.get("call_id") or item.get("id") or uuid.uuid4().hex)
                name = str(item.get("name") or item.get("tool") or "tool")
                tool_value = item.get("tool")
                if isinstance(tool_value, dict) and isinstance(tool_value.get("name"), str):
                    name = tool_value["name"]
                call_names[call_id] = name
                arguments = item.get("arguments")
                if arguments is None and "input" in item:
                    arguments = json.dumps({"input": item.get("input")})
                if not isinstance(arguments, str):
                    arguments = json.dumps(arguments or {})
                tool_call = {
                    "id": call_id,
                    "type": "function",
                    "function": {"name": name, "arguments": arguments},
                }
                if messages and messages[-1].get("role") == "assistant" and not messages[-1].get("tool_calls"):
                    messages[-1]["tool_calls"] = [tool_call]
                else:
                    messages.append({"role": "assistant", "content": "", "tool_calls": [tool_call]})
            elif kind in TOOL_OUTPUT_TYPES:
                call_id = str(item.get("call_id") or item.get("tool_call_id") or "")
                name = item.get("name") or call_names.get(call_id)
                tool_value = item.get("tool")
                if isinstance(tool_value, dict) and isinstance(tool_value.get("name"), str):
                    name = tool_value["name"]
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call_id,
                        "name": str(name or "tool"),
                        "content": content_for_chat(item.get("output")),
                    }
                )

    chat_tools = []
    raw_tools = payload.get("tools")
    if isinstance(raw_tools, list):
        for tool in raw_tools:
            if not isinstance(tool, dict):
                continue
            kind = tool.get("type")
            if kind == "function":
                function = {
                    "name": tool.get("name"),
                    "description": tool.get("description", ""),
                    "parameters": tool.get("parameters") or {"type": "object", "properties": {}},
                }
            else:
                name = str(tool.get("name") or kind or "tool")
                custom_names.add(name)
                function = {
                    "name": name,
                    "description": tool.get("description", ""),
                    "parameters": {
                        "type": "object",
                        "properties": {"input": {"type": "string"}},
                        "required": ["input"],
                        "additionalProperties": False,
                    },
                }
            chat_tools.append({"type": "function", "function": function})

    chat_payload: dict[str, object] = {
        "model": payload.get("model", "moonshotai/Kimi-k3"),
        "messages": messages,
        "stream": False,
    }
    if chat_tools:
        chat_payload["tools"] = chat_tools
        chat_payload["parallel_tool_calls"] = False
        tool_choice = payload.get("tool_choice")
        if tool_choice in {"none", "auto", "required"}:
            chat_payload["tool_choice"] = tool_choice
    for source, target in (
        ("temperature", "temperature"),
        ("top_p", "top_p"),
        ("max_output_tokens", "max_tokens"),
    ):
        if source in payload:
            chat_payload[target] = payload[source]
    reasoning = payload.get("reasoning")
    if isinstance(reasoning, dict) and reasoning.get("effort") is not None:
        chat_payload["reasoning_effort"] = reasoning["effort"]
    return chat_payload, custom_names


def chat_to_responses_sse(
    chat: dict[str, object], model: str, custom_names: set[str]
) -> bytes:
    response_id = str(chat.get("id") or f"resp_{uuid.uuid4().hex}")
    choice = {}
    choices = chat.get("choices")
    if isinstance(choices, list) and choices and isinstance(choices[0], dict):
        choice = choices[0]
    message = choice.get("message") if isinstance(choice.get("message"), dict) else {}
    assert isinstance(message, dict)
    output: list[dict[str, object]] = []
    reasoning_text = message.get("reasoning_content")
    if isinstance(reasoning_text, str) and reasoning_text:
        output.append(
            {
                "id": f"rs_{uuid.uuid4().hex[:8]}",
                "type": "reasoning",
                "summary": [{"type": "summary_text", "text": reasoning_text}],
            }
        )
    content = message.get("content")
    if isinstance(content, str) and content:
        output.append(
            {
                "id": f"msg_{uuid.uuid4().hex[:8]}",
                "type": "message",
                "status": "completed",
                "role": "assistant",
                "content": [{"type": "output_text", "text": content, "annotations": []}],
            }
        )
    tool_calls = message.get("tool_calls")
    if isinstance(tool_calls, list):
        for call in tool_calls:
            if not isinstance(call, dict):
                continue
            function = call.get("function") if isinstance(call.get("function"), dict) else {}
            assert isinstance(function, dict)
            name = str(function.get("name") or "tool")
            call_id = str(call.get("id") or f"call_{uuid.uuid4().hex}")
            arguments = function.get("arguments")
            if not isinstance(arguments, str):
                arguments = json.dumps(arguments or {})
            if name in custom_names:
                try:
                    parsed = json.loads(arguments)
                    custom_input = parsed.get("input", arguments) if isinstance(parsed, dict) else arguments
                except json.JSONDecodeError:
                    custom_input = arguments
                output.append(
                    {
                        "id": call_id,
                        "call_id": call_id,
                        "type": "custom_tool_call",
                        "name": name,
                        "input": str(custom_input),
                    }
                )
            else:
                output.append(
                    {
                        "id": call_id,
                        "call_id": call_id,
                        "type": "function_call",
                        "name": name,
                        "arguments": arguments,
                        "status": "completed",
                    }
                )

    usage = chat.get("usage") if isinstance(chat.get("usage"), dict) else {}
    assert isinstance(usage, dict)
    completion_details = (
        usage.get("completion_tokens_details")
        if isinstance(usage.get("completion_tokens_details"), dict)
        else {}
    )
    prompt_details = (
        usage.get("prompt_tokens_details")
        if isinstance(usage.get("prompt_tokens_details"), dict)
        else {}
    )
    response_usage = {
        "input_tokens": int(usage.get("prompt_tokens") or 0),
        "input_tokens_details": {"cached_tokens": int(prompt_details.get("cached_tokens") or 0)},
        "output_tokens": int(usage.get("completion_tokens") or 0),
        "output_tokens_details": {
            "reasoning_tokens": int(completion_details.get("reasoning_tokens") or 0)
        },
        "total_tokens": int(usage.get("total_tokens") or 0),
    }
    base = {
        "id": response_id,
        "object": "response",
        "created_at": int(time.time()),
        "status": "completed",
        "model": model,
        "output": output,
        "parallel_tool_calls": False,
        "usage": response_usage,
    }
    events: list[dict[str, object]] = []
    sequence = 0

    def add(kind: str, **values: object) -> None:
        nonlocal sequence
        events.append({"type": kind, "sequence_number": sequence, **values})
        sequence += 1

    add("response.created", response={**base, "status": "in_progress", "output": []})
    add("response.in_progress", response={**base, "status": "in_progress", "output": []})
    for index, item in enumerate(output):
        kind = item["type"]
        if kind == "reasoning":
            initial = {**item, "summary": []}
        elif kind == "message":
            initial = {**item, "status": "in_progress", "content": []}
        elif kind == "function_call":
            initial = {**item, "status": "in_progress", "arguments": ""}
        else:
            initial = {**item, "input": ""}
        add("response.output_item.added", output_index=index, item=initial)
        if kind == "reasoning":
            text = str(item["summary"][0]["text"])  # type: ignore[index]
            add("response.reasoning_summary_text.delta", output_index=index, summary_index=0, delta=text)
            add("response.reasoning_summary_text.done", output_index=index, summary_index=0, text=text)
        elif kind == "message":
            text = str(item["content"][0]["text"])  # type: ignore[index]
            add(
                "response.content_part.added",
                output_index=index,
                content_index=0,
                item_id=item["id"],
                part={"type": "output_text", "text": "", "annotations": []},
            )
            add(
                "response.output_text.delta",
                output_index=index,
                content_index=0,
                item_id=item["id"],
                delta=text,
            )
            add(
                "response.output_text.done",
                output_index=index,
                content_index=0,
                item_id=item["id"],
                text=text,
            )
            add(
                "response.content_part.done",
                output_index=index,
                content_index=0,
                item_id=item["id"],
                part=item["content"][0],  # type: ignore[index]
            )
        elif kind == "function_call":
            arguments = str(item.get("arguments", ""))
            add("response.function_call_arguments.delta", output_index=index, item_id=item["id"], delta=arguments)
            add("response.function_call_arguments.done", output_index=index, item_id=item["id"], arguments=arguments)
        elif kind == "custom_tool_call":
            custom_input = str(item.get("input", ""))
            add("response.custom_tool_call_input.delta", output_index=index, item_id=item["id"], delta=custom_input)
            add("response.custom_tool_call_input.done", output_index=index, item_id=item["id"], input=custom_input)
        add("response.output_item.done", output_index=index, item=item)
    add("response.completed", response=base)
    return b"".join(
        b"event: " + str(event["type"]).encode() + b"\n"
        + b"data: " + json.dumps(event, separators=(",", ":")).encode() + b"\n\n"
        for event in events
    )


class ProxyHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "KimiResponsesCompatibility/1.0"

    @property
    def proxy(self) -> "ProxyServer":
        return self.server  # type: ignore[return-value]

    def log_message(self, format_string: str, *args: object) -> None:
        self.proxy.state.log({"http": format_string % args})

    def do_GET(self) -> None:
        self._forward(None)

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        if self.path.rstrip("/").endswith("/responses"):
            self._responses_via_chat(body)
            return
        try:
            payload = json.loads(body)
        except (UnicodeDecodeError, json.JSONDecodeError):
            payload = None
        if payload is not None:
            patched = patch_tool_outputs(payload, self.proxy.state)
            if isinstance(payload, dict) and isinstance(payload.get("input"), list):
                outputs = [
                    item
                    for item in payload["input"]
                    if isinstance(item, dict) and item.get("type") in TOOL_OUTPUT_TYPES
                ]
                response_ids = {
                    response_id
                    for item in outputs
                    if (response_id := self.proxy.state.response_id(item.get("call_id")))
                }
                if outputs and len(response_ids) == 1:
                    payload["previous_response_id"] = next(iter(response_ids))
                    payload["input"] = [
                        {
                            "type": "message",
                            "role": "tool",
                            "name": item.get("name"),
                            "tool": item.get("tool"),
                            "tool_call_id": item.get("call_id"),
                            "call_id": item.get("call_id"),
                            "content": item.get("output", ""),
                        }
                        for item in outputs
                    ]
                    patched += 1
            body = json.dumps(payload, separators=(",", ":")).encode()
            tool_shapes = []
            for item in iter_dicts(payload):
                kind = item.get("type")
                if isinstance(kind, str) and kind in TOOL_CALL_TYPES | TOOL_OUTPUT_TYPES:
                    tool_shapes.append(
                        {
                            "type": item.get("type"),
                            "call_id": item.get("call_id") or item.get("id"),
                            "name": item.get("name") or item.get("tool"),
                        }
                    )
            input_shapes = []
            raw_input = payload.get("input") if isinstance(payload, dict) else None
            if isinstance(raw_input, list):
                for item in raw_input:
                    if not isinstance(item, dict):
                        input_shapes.append({"python_type": type(item).__name__})
                        continue
                    shape: dict[str, object] = {
                        key: item.get(key)
                        for key in ("type", "role", "call_id", "id", "name", "tool")
                        if key in item
                    }
                    output = item.get("output")
                    if isinstance(output, list):
                        shape["output_shapes"] = [
                            sorted(child) if isinstance(child, dict) else type(child).__name__
                            for child in output
                        ]
                    else:
                        shape["output_type"] = type(output).__name__
                    input_shapes.append(shape)
            self.proxy.state.log(
                {
                    "request": self.path,
                    "patched": patched,
                    "tool_items": tool_shapes,
                    "input_shapes": input_shapes,
                    "previous_response_id": payload.get("previous_response_id")
                    if isinstance(payload, dict)
                    else None,
                    "header_names": sorted(name.lower() for name in self.headers),
                }
            )
        self._forward(body)

    def _responses_via_chat(self, body: bytes) -> None:
        try:
            responses_payload = json.loads(body)
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_error(400, "invalid JSON")
            return
        if not isinstance(responses_payload, dict):
            self.send_error(400, "request must be an object")
            return
        chat_payload, custom_names = responses_to_chat(responses_payload)
        chat_body = json.dumps(chat_payload, separators=(",", ":")).encode()
        header_lines = []
        for name, value in self.headers.items():
            lowered = name.lower()
            if lowered in HOP_HEADERS | {"host", "content-length", "accept-encoding"}:
                continue
            header_lines.append(f"{name}: {value}\n")
        target = self.proxy.upstream.rstrip("/") + "/v1/chat/completions"
        try:
            with (
                tempfile.NamedTemporaryFile("w", encoding="utf-8") as header_input,
                tempfile.NamedTemporaryFile("wb") as body_input,
                tempfile.NamedTemporaryFile("w+b") as header_output,
            ):
                header_input.writelines(header_lines)
                header_input.flush()
                body_input.write(chat_body)
                body_input.flush()
                status = 502
                raw_headers = ""
                for upstream_attempt in range(1, 9):
                    header_output.seek(0)
                    header_output.truncate(0)
                    header_output.flush()
                    completed = subprocess.run(
                        [
                            "curl",
                            "--silent",
                            "--show-error",
                            "--http2",
                            "--request",
                            "POST",
                            "--header",
                            f"@{header_input.name}",
                            "--dump-header",
                            header_output.name,
                            "--max-time",
                            str(self.proxy.timeout),
                            "--data-binary",
                            f"@{body_input.name}",
                            target,
                        ],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=False,
                    )
                    header_output.seek(0)
                    raw_headers = header_output.read().decode("iso-8859-1", "replace")
                    blocks = [block for block in raw_headers.split("\r\n\r\n") if block]
                    final_headers = blocks[-1].splitlines() if blocks else []
                    status = 502
                    if final_headers and final_headers[0].startswith("HTTP/"):
                        parts = final_headers[0].split(" ", 2)
                        if len(parts) >= 2 and parts[1].isdigit():
                            status = int(parts[1])
                    if completed.returncode != 0 or status != 429 or upstream_attempt == 8:
                        break
                    retry_after = None
                    for line in final_headers[1:]:
                        if ":" not in line:
                            continue
                        name, value = line.split(":", 1)
                        if name.lower() == "retry-after":
                            try:
                                retry_after = max(1, int(value.strip()))
                            except ValueError:
                                pass
                    delay = retry_after or min(15 * upstream_attempt, 120)
                    self.proxy.state.log(
                        {
                            "translated_retry": upstream_attempt,
                            "status": status,
                            "retry_in_seconds": delay,
                            "message_count": len(chat_payload.get("messages", [])),
                            "upstream_error": completed.stdout.decode(
                                "utf-8", "replace"
                            )[:1024],
                        }
                    )
                    time.sleep(delay)
        except OSError as error:
            self.proxy.state.log({"chat_proxy_error": type(error).__name__, "detail": str(error)})
            self.send_error(502, "chat transport failed")
            return

        blocks = [block for block in raw_headers.split("\r\n\r\n") if block]
        final_headers = blocks[-1].splitlines() if blocks else []
        self.proxy.state.log(
            {
                "translated": "/v1/responses->/v1/chat/completions",
                "status": status,
                "message_count": len(chat_payload.get("messages", [])),
                "tool_count": len(chat_payload.get("tools", [])),
            }
        )
        if completed.returncode != 0:
            self.proxy.state.log(
                {
                    "curl_exit": completed.returncode,
                    "curl_error": completed.stderr.decode("utf-8", "replace")[:4096],
                }
            )
            self.send_error(502, "chat transport failed")
            return
        if status >= 400:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(completed.stdout)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(completed.stdout)
            self.close_connection = True
            return
        try:
            chat_response = json.loads(completed.stdout)
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_error(502, "invalid chat response")
            return
        if not isinstance(chat_response, dict):
            self.send_error(502, "invalid chat response")
            return
        response_body = chat_to_responses_sse(
            chat_response,
            str(responses_payload.get("model", "moonshotai/Kimi-k3")),
            custom_names,
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Content-Length", str(len(response_body)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(response_body)
        self.wfile.flush()
        self.close_connection = True

    def _forward(self, body: bytes | None) -> None:
        headers = []
        for name, value in self.headers.items():
            lowered = name.lower()
            if lowered in HOP_HEADERS | {"host", "content-length", "accept-encoding"}:
                continue
            headers.append(f"{name}: {value}\n")
        target = self.proxy.upstream.rstrip("/") + "/" + self.path.lstrip("/")
        try:
            with (
                tempfile.NamedTemporaryFile("w", encoding="utf-8") as header_input,
                tempfile.NamedTemporaryFile("wb") as body_input,
                tempfile.NamedTemporaryFile("w+b") as header_output,
            ):
                header_input.writelines(headers)
                header_input.flush()
                if body is not None:
                    body_input.write(body)
                    body_input.flush()
                command = [
                    "curl",
                    "--silent",
                    "--show-error",
                    "--http2",
                    "--request",
                    self.command,
                    "--header",
                    f"@{header_input.name}",
                    "--dump-header",
                    header_output.name,
                    "--max-time",
                    str(self.proxy.timeout),
                ]
                if body is not None:
                    command.extend(["--data-binary", f"@{body_input.name}"])
                command.append(target)
                completed = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=False,
                )
                header_output.seek(0)
                raw_headers = header_output.read().decode("iso-8859-1", "replace")

            blocks = [block for block in raw_headers.split("\r\n\r\n") if block]
            final_headers = blocks[-1].splitlines() if blocks else []
            status = 502
            reason = "Bad Gateway"
            if final_headers and final_headers[0].startswith("HTTP/"):
                parts = final_headers[0].split(" ", 2)
                if len(parts) >= 2 and parts[1].isdigit():
                    status = int(parts[1])
                    reason = parts[2] if len(parts) == 3 else ""
            if completed.returncode != 0:
                status = 502
                reason = "Bad Gateway"
                self.proxy.state.log(
                    {
                        "curl_exit": completed.returncode,
                        "curl_error": completed.stderr.decode("utf-8", "replace")[:4096],
                    }
                )

            response_body = completed.stdout
            self.send_response(status, reason)
            for line in final_headers[1:]:
                if ":" not in line:
                    continue
                name, value = line.split(":", 1)
                if name.lower() not in HOP_HEADERS | {"content-length"}:
                    self.send_header(name, value.strip())
            self.send_header("Content-Length", str(len(response_body)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(response_body)
            self.wfile.flush()

            response_id = None
            response_calls: list[str] = []
            for line in response_body.splitlines():
                if not line.startswith(b"data:"):
                    continue
                raw = line[5:].strip()
                if not raw or raw == b"[DONE]":
                    continue
                try:
                    event = json.loads(raw)
                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
                for item in iter_dicts(event):
                    self.proxy.state.remember(item)
                    if isinstance(item, dict) and item.get("type") in TOOL_CALL_TYPES:
                        call_id = item.get("call_id") or item.get("id")
                        if isinstance(call_id, str):
                            response_calls.append(call_id)
                response = event.get("response") if isinstance(event, dict) else None
                if isinstance(response, dict) and isinstance(response.get("id"), str):
                    response_id = response["id"]
                metadata = event_metadata(event)
                if metadata is not None:
                    self.proxy.state.log(metadata)
            if response_id is not None and response_calls:
                self.proxy.state.remember_response(response_calls, response_id)
            if status >= 400 and response_body:
                self.proxy.state.log(
                    {
                        "upstream_status": status,
                        "upstream_error": response_body.decode("utf-8", "replace")[:4096],
                    }
                )
        except (BrokenPipeError, ConnectionError, OSError) as error:
            self.proxy.state.log({"proxy_error": type(error).__name__, "detail": str(error)})
        finally:
            self.close_connection = True


class ProxyServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(
        self,
        address: tuple[str, int],
        upstream: str,
        timeout: int,
        state: CompatibilityState,
    ) -> None:
        super().__init__(address, ProxyHandler)
        self.upstream = upstream
        self.timeout = timeout
        self.state = state


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=18765)
    parser.add_argument("--upstream", default="http://38.9.57.183:30000")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    state = CompatibilityState(args.log)
    server = ProxyServer((args.listen, args.port), args.upstream, args.timeout, state)
    state.log({"listening": f"{args.listen}:{args.port}", "upstream": args.upstream})
    try:
        server.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
