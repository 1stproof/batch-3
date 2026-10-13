# First Proof — Batch 3

This repository contains everything you need to prepare a submission for the First Proof Batch 3 benchmark.

First Proof provides a common input file of LaTeX math problems. Each submitter provides code that processes those problems inside a Docker container. First Proof runs the code on AWS, collects the output, and delivers results.

This README covers the repository layout, what your submission must contain, and the `hardware.json` field reference. For the security model, turnaround, and First Proof's responsibilities, see [first-proof-benchmarking-protocol.md](first-proof-benchmarking-protocol.md).

## Key dates

- **Source code and API keys due:** October 1, 2026
- **Testing window:** first week of October 2026
- **Results published:** October 14, 2026

## Repository structure

```
├── input/input.json                     # Common input file (LaTeX problems)
├── run.sh                               # First Proof's run script (reference only)
├── run-config.env.example               # Template for First Proof's AWS config
├── allowed-instances.txt                # Approved EC2 instance types
├── first-proof-benchmarking-protocol.md # Full protocol
├── submissions/
│   └── test-dummy/                      # Reference submission (working example)
├── secrets/                             # Submitter API keys (gitignored)
└── results/                             # Run output per submitter (gitignored)
```

`run.sh` is the script First Proof uses to launch an instance, build and run your container, collect results, and terminate the instance. You do not run it — it is included so you can see exactly how your container is invoked.

## What a submission must contain

Deliver a private GitHub repository with at least:

```
├── Dockerfile
├── hardware.json
├── README.md          # what your approach is, what secrets it needs, any review context
├── src/               # your code
└── (anything else your Dockerfile needs)
```

First Proof clones your repository into `submissions/<submitter-id>/` and runs it from there.

### The container contract

Your Dockerfile must produce an image whose `CMD` reads the input and writes output. First Proof launches it as:

```bash
docker run --rm \
  -v input.json:/data/input/input.json:ro \
  -v output-dir:/data/output \
  --env-file secrets.env \    # only if env_vars is true
  your-image
```

Your code must:
- Read the problems from `/data/input/input.json` (read-only).
- Write all output — solutions, logs, token usage — to `/data/output/`.

Your code receives all problems in a single input file and may process them however you like — sequentially or in parallel — within your one container. The timeout is wall-clock for the whole container, not per problem: running all problems in parallel does not multiply your time budget.

Each AI solution may be **up to 16 pages** when typeset.

### hardware.json

```json
{
  "instance_type": "r7i.2xlarge",
  "env_vars": true,
  "rationale": "Brief explanation of why this hardware is needed."
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `instance_type` | yes | EC2 instance type. Must be on the approved list in `allowed-instances.txt`. |
| `rationale` | yes | Why this instance type is needed. |
| `env_vars` | when needed | Set to `true` if your code needs environment variables from a secrets file. |
| `timeout_minutes` | no | Maximum wall-clock minutes for your container. Defaults to **1440 (24 hours)** if omitted. |
| `storage_gb` | no | Size of the EBS root volume in GB (gp3). Defaults to **100** if omitted. Increase for large model weights, datasets, or scratch space. |
| `ami` | no | Custom AMI ID. Omit to use the default (Ubuntu 24.04 LTS). |

Set `timeout_minutes` and `storage_gb` explicitly if you have a specific requirement; otherwise you get the defaults above.

### Secrets

If your code needs API keys, set `"env_vars": true` and deliver a `secrets.env` file to First Proof through a secure out-of-band channel (encrypted message, one-time link). One `KEY=value` per line; values are injected as environment variables at runtime. Never commit secrets to your repository.

## Required: log all token usage

Your code must write a detailed log of all tokens produced and consumed at each step — model inputs, model outputs, and **all hidden reasoning/thinking tokens** — to `/data/output/` as a structured file (JSON, JSONL, or plaintext).

**Token-usage fields vary by provider.** The `test-dummy` example reads the OpenAI response layout (`usage.prompt_tokens`, `usage.completion_tokens`, `usage.completion_tokens_details.reasoning_tokens`). If you use a non-OpenAI provider, do not assume that layout — capture the counts, including reasoning tokens, from wherever your provider reports them in its response. Reasoning tokens are easy to miss and are often the largest component of spend.

## Recommended: write a progress heartbeat

A run can last up to 24 hours. So that First Proof can confirm your run is making progress (and catch a silent stall early), we strongly recommend writing a small heartbeat file to `/data/output/progress.json` and overwriting it at least every 15 minutes. The exact contents are up to you, but include a timestamp and a short status, e.g.:

```json
{"timestamp_utc": "2026-10-03T14:32:00Z", "status": "3/10 solutions written, 7 in progress"}
```

An advancing timestamp is all First Proof needs to see that the run is alive; a frozen one is the signal to look closer. This is a recommendation, not a validity requirement — omitting it will not fail your submission.

## Input format

`input/input.json` contains an array of LaTeX math problems:

```json
{
  "problems": [
    { "id": "prob-001", "latex": "\\textbf{Problem 1.} ...\n" }
  ]
}
```

Each entry has an `id` (string) and `latex` (the problem statement).

## Testing locally

```bash
docker build -t my-submission .

docker run --rm \
  -v $(pwd)/input/input.json:/data/input/input.json:ro \
  -v $(pwd)/my-output:/data/output \
  --env-file my-secrets.env \
  my-submission

ls my-output/
```

## Reference submission

`submissions/test-dummy/` is a complete working example: it reads each problem, calls an LLM via OpenRouter, writes `.tex` files to `/data/output/`, and logs token usage. Use it as a structural reference. Note that its token-logging code assumes the OpenAI response layout — adapt it to your provider (see "log all token usage" above).

## Approved instance types

See `allowed-instances.txt` for the current list (which now includes `r7i.2xlarge` — 8 vCPU / 64 GB RAM). Requests for unlisted types are returned for revision. First Proof may update the list and will notify submitters of changes.
