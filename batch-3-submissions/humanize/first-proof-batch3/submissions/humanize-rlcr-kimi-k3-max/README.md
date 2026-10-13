# Humanize RLCR — Kimi K3/max

First Proof Batch 3 submission harness based on the Humanize Ralph Loop with
Codex Review (RLCR). Each problem receives one independent, fully autonomous
attempt. A `moonshotai/Kimi-k3` worker writes a proof while separate Kimi K3
review calls gate every RLCR round and the final code-review phase. Both
worker and reviewer use `max` reasoning effort and make tool calls serially.

The harness is adapted from the web-disabled First Proof Second Batch
experiment. It does not use web search, browser tools, plugins, apps,
subagents, sibling attempts, or external mathematical sources.

Codex normally speaks the Responses protocol, while the supplied Kimi endpoint
speaks Chat Completions. The container therefore runs a loopback-only
compatibility bridge that translates requests and responses, including tool
calls and provider-reported token usage. The bridge sends every model request
to the exact `moonshotai/Kimi-k3` model. It is infrastructure only: Kimi remains
the model doing both the proof work and the review work.

## Container contract

The image reads `/data/input/input.json` and writes to `/data/output/`:

- `<problem-id>.tex`: a standalone LaTeX solution that has passed an actual
  PDF build and the 16-page limit;
- `token_usage.json`: response-level input, cached-input, output, and hidden
  reasoning token counts for worker and reviewer calls;
- `progress.json`: a heartbeat updated once per minute;
- `run_manifest.json`: per-problem status, output-name mapping, and assigned
  serving node;
- `logs/<problem-id>/`: Codex event streams and stderr;
- `logs/transport/node-{1,2}/`: per-node loopback bridge request metadata and
  transport errors;
- `humanize/<problem-id>/`: RLCR prompts, summaries, reviews, and lifecycle
  state for audit.

At finalization, the harness compiles the latest `solution.tex` to a stable PDF
with `latexmk`/`pdflatex` and
`-no-shell-escape`, then reads the final page count from PDF metadata. A proof
is submitted only when the build succeeds and reports at most 16 pages. The
compiler transcript is retained as
`logs/<problem-id>/solution-validation.log`. If RLCR has not reached an
accepted terminal state by the shared deadline, the latest worker-generated
`solution.tex` is still submitted as `incomplete-submitted` when it compiles
and fits the page limit. An explicit blank is used only when the latest file is
not standalone LaTeX, does not compile, or exceeds 16 pages.
The image includes the TeX Live base, recommended, extra, pictures, science,
and recommended-font collections used by the worker's documented package set.

All ten problems are launched concurrently by default. Input problems 1--5 use
serving node 1 and problems 6--10 use serving node 2. Each node has its own
loopback compatibility bridge, Codex configuration, credential selection, and
session store; token accounting combines both stores in the final report. A
transport interruption may restart the Codex process up to two times, but it
continues the same Git workspace and the same Humanize state; it never resets
or starts a second mathematical attempt. The container handles termination by
stopping every live worker process group and both compatibility bridges before
exiting.

## Secrets and endpoint

Supply the Kimi credentials to First Proof out of band in `secrets.env`:

```bash
KIMI_API_KEY_1=<node-1-key>
KIMI_API_KEY_2=<node-2-key>
KIMI_UPSTREAM_URLS=http://38.9.57.183:30000,http://38.9.57.184:30000
```

If both endpoints use the same credential, a single `KIMI_API_KEY=<shared-key>`
may replace the two numbered key variables. Do not repeat the same environment
variable twice: standard env files keep only one effective value. Do not commit
`secrets.env`. Credentials remain in the process environment; the harness does
not write them into Codex homes, workspaces, logs, or output artifacts.

The two endpoints default to `http://38.9.57.183:30000` and
`http://38.9.57.184:30000`. Override them with either the comma-separated
`KIMI_UPSTREAM_URLS` variable or both `KIMI_UPSTREAM_URL_1` and
`KIMI_UPSTREAM_URL_2`. The legacy `KIMI_UPSTREAM_URL` name is accepted only
when its value contains both comma-separated origins. Endpoints on `rust.cat`
are rejected. `KIMI_PROXY_PORT` sets node 1's loopback port and node 2 uses the
next port (defaults: `18770` and `18771`); use `KIMI_PROXY_PORT_1` and
`KIMI_PROXY_PORT_2` for independent overrides.

## Reproducibility

The image pins:

- OpenAI Codex CLI `0.157.1`;
- PolyArch Humanize commit
  `fc0e0bec143cad1ff3325b2b4d17cc2722827028`.

A small deterministic compatibility patch allows slash-qualified provider
model identifiers such as `moonshotai/Kimi-k3` throughout Humanize, makes the
review phase use the configured `max` effort, and carries the container sandbox
bypass into the final diff reviewer. The image build runs both the harness unit
tests and a real Humanize setup test using `moonshotai/Kimi-k3:max`.

## Local smoke test

```bash
docker build -t first-proof-humanize-kimi .

docker run --rm \
  -v "$(pwd)/input.json:/data/input/input.json:ro" \
  -v "$(pwd)/output:/data/output" \
  --env-file secrets.env \
  first-proof-humanize-kimi
```

For a no-model structural check, set `HARNESS_VALIDATE_ONLY=1`. It validates
the input, authentication environment, Codex and LaTeX installations,
Humanize runtime, and output directory, then exits without making API calls.
