from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


SUBMISSION_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SUBMISSION_ROOT))

from src import kimi_responses_proxy as proxy


class TranslationTests(unittest.TestCase):
    def test_responses_request_becomes_serial_kimi_chat_request(self) -> None:
        payload = {
            "model": "moonshotai/Kimi-k3",
            "instructions": "Prove the claim.",
            "input": [
                {
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": "Begin."}],
                }
            ],
            "tools": [
                {
                    "type": "function",
                    "name": "read_file",
                    "description": "Read a file",
                    "parameters": {
                        "type": "object",
                        "properties": {"path": {"type": "string"}},
                        "required": ["path"],
                    },
                }
            ],
            "reasoning": {"effort": "max"},
            "max_output_tokens": 2048,
        }

        translated, custom_names = proxy.responses_to_chat(payload)

        self.assertEqual(translated["model"], "moonshotai/Kimi-k3")
        self.assertEqual(translated["messages"][0]["role"], "system")
        self.assertEqual(translated["messages"][1]["content"], "Begin.")
        self.assertFalse(translated["parallel_tool_calls"])
        self.assertEqual(translated["reasoning_effort"], "max")
        self.assertEqual(translated["max_tokens"], 2048)
        self.assertEqual(translated["tools"][0]["function"]["name"], "read_file")
        self.assertEqual(custom_names, set())

    def test_chat_response_preserves_tool_call_and_usage_in_responses_events(self) -> None:
        chat = {
            "id": "chatcmpl-test",
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": "",
                        "tool_calls": [
                            {
                                "id": "call-1",
                                "type": "function",
                                "function": {
                                    "name": "read_file",
                                    "arguments": '{"path":"solution.tex"}',
                                },
                            }
                        ],
                    }
                }
            ],
            "usage": {
                "prompt_tokens": 101,
                "completion_tokens": 17,
                "total_tokens": 118,
                "prompt_tokens_details": {"cached_tokens": 23},
                "completion_tokens_details": {"reasoning_tokens": 11},
            },
        }

        body = proxy.chat_to_responses_sse(
            chat, "moonshotai/Kimi-k3", custom_names=set()
        )
        records = [
            json.loads(line.removeprefix("data: "))
            for line in body.decode().splitlines()
            if line.startswith("data: ")
        ]
        completed = next(
            record for record in records if record["type"] == "response.completed"
        )["response"]

        self.assertEqual(completed["model"], "moonshotai/Kimi-k3")
        self.assertFalse(completed["parallel_tool_calls"])
        self.assertEqual(completed["output"][0]["type"], "function_call")
        self.assertEqual(completed["output"][0]["name"], "read_file")
        self.assertEqual(completed["usage"]["input_tokens"], 101)
        self.assertEqual(
            completed["usage"]["input_tokens_details"]["cached_tokens"], 23
        )
        self.assertEqual(
            completed["usage"]["output_tokens_details"]["reasoning_tokens"], 11
        )


if __name__ == "__main__":
    unittest.main()
