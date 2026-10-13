# `smoke/` — cheap end-to-end smoke for the First Proof harness

This directory is a self-contained "fake First Proof run" for the
ProofCouncil container. The idea: instead of waiting on a real 24-hour
batch with Pro / Opus / Gemini-Pro to discover that a single config
knob is wrong, run `scripts/firstproof_entrypoint.py` end-to-end
on a list of eight fake problems with the cheapest models that
still exercise the production code paths.

A successful smoke confirms:

- the container builds and the adapter starts
- `/data/input/input.json` is parsed and per-problem `.tex` files
  appear in `/data/output/`
- the AC loop runs to completion in the limited budget
- the Council fanout fires (at least for some problems)
- empty / malformed input is handled gracefully (no crashed batch)
- `solutions.json`, `run_summary.json`, `token_usage.jsonl` are all
  written
- per-call token / cost rows accumulate end-to-end

It does **not** confirm:

- Pro / Opus correctness (mini models substituted)
- 24-hour wallclock behaviour
- Codex CLI Compute Worker path; the public smoke keeps Compute disabled

## Files

- `input.json` — eight fake "problems"; see "What each problem tests".
- `run_local.sh` — single-command launcher that runs the adapter on
  the host (no Docker), pointed at the cheap workflow.
- `run_container.sh` — builds & launches the production Docker image
  to also exercise the container path.
- `secrets.env.example` — env-var template (copy to `smoke/secrets.env`
  and fill).

The cheap workflow preset lives one level up at:

- `configs/workflows/firstproof_smoke_fast.yaml` — Author/Critic on
  gpt-5.4-mini, Council on (mini/sonnet/gemini), Compute **off**.

## What each problem tests

| ID | Path exercised | Expected status |
|----|----------------|------------------|
| `smoke-001-trivial-arithmetic` | Minimum-cost Author→Critic→ship loop. | `ok` |
| `smoke-002-sqrt2-classic` | Short classic proof; Critic should accept after 1–2 rounds. | `ok` |
| `smoke-003-compute-trigger` | Worded like a computation-heavy problem. The Author may emit `<compute_agent>`, and `firstproof_smoke_fast` should ignore it cleanly because `enable_compute: false`. | `ok` |
| `smoke-004-council-trigger` | Explicit "consult external advisors" → `<council>` block → parallel Council fanout. | `ok` |
| `smoke-005-references-test` | Asks for genuine bibliographic references in `references.bib`, exercises the embed-or-ship bibliography helper. | `ok` |
| `smoke-006-empty-input` | `latex: ""` → entrypoint hits `_problem_text` "empty" branch → `_fallback_tex` → status `input_error`. **Workflow is not invoked.** | `input_error` |
| `smoke-007-malformed-latex` | No `\documentclass` / `\begin{document}` / `\end{document}`. Author should still write a real solution; `_ensure_complete_latex` then wraps the output in 12pt article. | `ok` |
| `smoke-008-rh-cannot-solve` | Genuinely unsolved. Author should *not* declare `<ready>true</ready>` and should emit a "Remaining open issues" section. Solution still ships. | `ok` (final round) |

If any of these come back with status `adapter_error` or
`workflow_error`, something on the production path broke and is worth
investigating *before* the real run.

## Smoke runtime / cost expectations

The runner scripts export `FIRSTPROOF_N_ROUNDS=2` and
`FIRSTPROOF_PAGE_LIMIT=8` so the production entrypoint's
documented defaults (10 / 12) don't override the smoke preset's
intended cheap values. Per-problem budget cap is `$5` / `30 min`
for the fast workflow.

Observed in dev (with the 2-round / 8-page overrides):

- problem 1 / 2: ≈ 30s, ≈ $0.02 each
- problems 3 / 4 / 5: 1–2 min, ≈ $0.05 each
- problem 6: instant (no workflow)
- problem 7 / 8: 1–2 min, ≈ $0.05 each

Total expected cost for the fast smoke: **well under $0.50** for all
eight problems combined.

> **Without the env-var overrides** (e.g. running the entrypoint directly
> without the runner scripts), the entrypoint pins ``n_rounds=10`` and
> ``page_limit=12`` and the smoke ends up running the production-sized
> configuration. Useful when you want a realistic load test, but expect
> ~5× the runtime / cost.

## Launching locally (no Docker)

```bash
cp smoke/secrets.env.example smoke/secrets.env
# fill in OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY at minimum

./smoke/run_local.sh
```

This writes output under `smoke/output/` rather than `/data/output/`
(via the `FIRSTPROOF_OUTPUT_DIR` env var the adapter already honours).

## Launching via Docker (mimics the AWS path)

```bash
docker build -t proofcouncil-smoke .
./smoke/run_container.sh
```

The script mounts `smoke/input.json` read-only at
`/data/input/input.json` and `smoke/output_container/` at
`/data/output/`, the same way `run.sh` from the First Proof harness
will do on EC2.

## After a smoke run, what to inspect

```bash
ls smoke/output/                                  # *.tex per problem
jq '.per_problem[] | {id, status, returncode, duration_seconds}' \
    smoke/output/run_summary.json
jq '.totals' smoke/output/run_summary.json
head -n 20 smoke/output/token_usage.jsonl
```

Then spot-check one or two of the `.tex` outputs to make sure they
compile on Overleaf without modification (the spec requires
"compile cleanly on Overleaf without modification" — mini models can
produce mildly-invalid TeX so this is worth confirming on the smoke).
