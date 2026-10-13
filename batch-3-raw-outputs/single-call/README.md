# Single-call runs: GPT 5.2 Pro, GPT 5.4 Pro, GPT 5.5 Pro

- `<model>/with-search/`, `<model>/no-search/` — one run folder each, containing:
  - `prob-NNN.tex` — answer
  - `prob-NNN.pdf` and build files — typesetting output, where present
  - `prob-NNN_response.json` — API response
  - `prob-NNN_trace.md` — readable trace
  - `submitted.json`, `token_usage.jsonl` — calls and token counts
  - `problem-10/` — the same two files for Problem 10

A = answer; N = call without answer; - = no call.

| Run | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Answers |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `gpt-5.2-pro/with-search` | A | A | A | A | A | A | A | A | A | A | 10 |
| `gpt-5.2-pro/no-search` | A | A | A | A | N | A | A | A | N | N | 7 |
| `gpt-5.4-pro/with-search` | A | A | N | A | A | A | N | - | - | N | 5 |
| `gpt-5.4-pro/no-search` | A | A | A | A | A | A | A | A | A | A | 10 |
| `gpt-5.5-pro/with-search` | A | A | A | A | A | A | A | A | A | N | 9 |
| `gpt-5.5-pro/no-search` | A | A | A | A | A | A | A | A | A | A | 10 |
