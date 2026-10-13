# Single-call runs: open weight models

| Folder | Model (OpenRouter id) |
|---|---|
| `kimi-k3/` | moonshotai/kimi-k3 |
| `deepseek-v4-pro/` | deepseek/deepseek-v4-pro |
| `deepseek-v4.1-flash/` | deepseek/deepseek-v4.1-flash |
| `glm-5.3/` | z-ai/glm-5.3 |
| `qwen-3.8-2.4t/` | qwen/qwen3.8-2.4t-a95b |

Each has `with-search/` and `no-search/`, containing:

- `prob-NNN.tex` — answer
- `prob-NNN_response.json` — API request and response
- `prob-NNN_trace.md` — readable trace
- `submitted.json`, `token_usage.jsonl` — calls and token counts
- `problem-10/` — the same two files for Problem 10
