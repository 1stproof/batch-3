# test-dummy

Reference submission for the First Proof shared compute pipeline.

Reads `/data/input/input.json` (a list of LaTeX math problems), sends each problem to an LLM via OpenRouter (model set by the `MODEL` constant in `src/run.py`, currently `openai/gpt-4o-mini`), and writes `.tex` files to `/data/output/` with the LLM response wrapped in a verbatim block so the output always compiles.

Also writes `token_usage.json` to `/data/output/` recording per-problem and total token counts (prompt, completion, reasoning, total).

Note: the token-logging code reads the **OpenAI response layout** (`usage.prompt_tokens`, `usage.completion_tokens`, `usage.completion_tokens_details.reasoning_tokens`). If your submission uses a non-OpenAI provider, capture the counts — including reasoning tokens — from wherever your provider reports them instead. See "log all token usage" in the top-level README.

Requires `OPENROUTER_API_KEY` in the secrets file. Runs on `r7i.2xlarge`.
