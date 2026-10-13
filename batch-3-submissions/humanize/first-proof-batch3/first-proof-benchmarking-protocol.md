# First Proof Benchmarking Protocol — Batch 3

## Overview

Multiple submitters each provide code that processes a common input file of LaTeX math problems. Each submitter specifies their own hardware requirements. First Proof provides the input data, runs each submitter's code on the requested hardware, and collects the results.

First Proof's per-submitter work is: clone a repo, run a script. The input file stays on First Proof's machine and is copied to a temporary cloud instance only at run time. The instance is destroyed after results are retrieved.

See [README.md](README.md) for the repository structure, submission requirements, the `hardware.json` field reference, and how to test locally. Requirements on the LaTeX solutions themselves (length, format) are in the Batch 3 call for submissions.

## Eligibility and rules

- Each system must be an **open-source harness that calls publicly available models via API**. "Publicly available" means accessible to any member of the public as of October 7, 2026 (one week before results are published). A single prompt counts as a harness.
- Each system gets **one shot per problem** — a single autonomous attempt per problem, with no human interaction during the run. (Problems may be worked sequentially or in parallel; "one shot" refers to no second attempt or human iteration, not to processing order.)
- Each AI solution may be **at most 16 pages** when typeset.

Full benchmark details are in the Batch 3 call for submissions.

## Definitions

| Term | Meaning |
|------|---------|
| First Proof | Owns the AWS account, provides the input data, runs the infrastructure. Full visibility into all stages of execution. |
| Submitter | Provides code, a hardware spec, and API keys. Receives the final output. |
| Input file | A JSON file (~1 MB) that First Proof provides. Common schema across all submitters. |
| Results | Output files the submitter's code writes to `/data/output/`. |

## What First Proof provides

1. **Input file** — `input/input.json`, the common set of LaTeX math problems every submission processes.
2. **Run infrastructure** — an AWS account, ephemeral EC2 instances, and the run script ([`run.sh`](run.sh)) that automates the full lifecycle. First Proof's own AWS configuration lives in a gitignored `run-config.env`; see [`run-config.env.example`](run-config.env.example).
3. **Approved instance types** — the list submissions may request, in [`allowed-instances.txt`](allowed-instances.txt).
4. **Secrets handling** — submitter API keys are placed at `secrets/<submitter-id>.env` and injected at container launch via `docker run --env-file`. Keys are stored only on First Proof's machine.

## What each submitter provides

1. An invitation to a private GitHub repository with the submission code (see [README.md](README.md) for structure). **Source code and API keys are due October 1, 2026.**
2. A `hardware.json` file specifying the instance type and any other requirements (full field reference in [README.md](README.md); `instance_type` and `rationale` are required, and the instance type must be on the approved list).
3. **Comprehensive token logging** — a structured log, written to `/data/output/`, of all tokens produced and consumed at each step: model inputs, outputs, and hidden reasoning tokens. Token fields vary by provider; capture them from wherever your provider reports them, not by assuming the OpenAI layout. See [README.md](README.md).
4. If `env_vars` is `true`, a `secrets.env` file delivered through a secure out-of-band channel.

## How a run works

First Proof launches a fresh EC2 instance of the requested type, uploads the code and the input file, builds the Docker image, and runs the container. The container sees `/data/input/input.json` (read-only) and `/data/output/` (where it writes results). After the container exits or the timeout is reached, First Proof retrieves the output and logs, records run metadata, and terminates the instance. The full implementation is in [`run.sh`](run.sh).

### Pre-run check (smoke test)

Before each full run, First Proof does a short pre-test: it builds and briefly runs the submission — on a **different set of problems** with a **~30-minute timeout** — to confirm the image builds and the code starts and authenticates cleanly. This runs your real code against your API account, so **it draws real API spend** (see "API accounts and limits" below). If the pre-test surfaces a build or startup failure, First Proof notifies the submitter to fix and resubmit before the full run.

### Monitoring during the run

During the full run, First Proof periodically checks that the run is making progress (for example, by inspecting `/data/output/`, including the recommended `progress.json` heartbeat, and log growth). This is a health check, not intervention: First Proof does not modify a running submission. See [README.md](README.md) for the heartbeat recommendation.

### Run metadata

Each run produces `results/<submitter-id>/run-metadata.json`:

```json
{
  "submitter_id": "alice",
  "timestamp_utc": "2026-10-03T14:32:00Z",
  "git_commit": "a1b2c3d4...",
  "instance_type": "r7i.2xlarge",
  "instance_id": "i-0abc1234def56789",
  "storage_gb": 100,
  "exit_code": 0,
  "runtime_seconds": 1847,
  "timeout_minutes": 1440,
  "timeout_overridden": false,
  "output_files": 10,
  "failed": false
}
```

## API accounts and limits

Submitters supply their own API keys, and all model usage is billed to the submitter's own account. Because of this:

- **Provision enough headroom — credits and rate limits — for the pre-run check and the full run.** There is a single scored run, so a run that fails partway (for example, by exhausting credits or hitting a rate cap mid-execution) is a failed result with no second attempt. Give your account enough margin, on both balance and rate limits, to complete the full run comfortably.

- **Rate limits and other provider-side limits depend on your account and your code.** First Proof runs your submission as written, so provider-side behavior — tokens-per-minute limits, quota caps, and the throughput or cost that result — comes down to your account's tier and how your harness makes its calls, rather than First Proof's infrastructure. For example, a harness that issues many large model calls in parallel may exceed its account's tokens-per-minute limit and start receiving `429 rate_limit_exceeded` responses, which slows the run. First Proof will surface any such errors in the logs it returns so you can see what happened, but the fix (requesting a higher limit, lowering concurrency, or adding credit) is on the submitter's side. It's worth checking your account's rate limits, not just its balance, before your run.

## Visibility

**First Proof** sees: the complete source code, the Dockerfile and every dependency, all stdout/stderr, everything written to `/data/output/`, and the hardware used, runtime, exit code, and git commit.

**Submitter** sees: this protocol and the [README](README.md), and the contents of `/data/output/`, delivered by First Proof.

Note that after grading, First Proof publishes the source code of all tested systems, the AI solutions, the referee reports, and the scores. Prepare your submission on the understanding that it will become public.

## Security

- **Input file.** Lives on First Proof's machine. Copied to the instance at run time, mounted read-only, destroyed when the instance is terminated.
- **Ephemeral instances.** Each run uses a fresh EC2 instance, terminated after results are retrieved. No data persists in the cloud between runs.
- **Network.** Outbound HTTPS is allowed (for LLM API calls to publicly available models and access to public websites, including web search). Inbound is limited to SSH from First Proof's IP.
- **API keys.** Injected as environment variables at container launch. Stored only on First Proof's machine.
- **Timeout.** Container execution is limited to at most 24 hours of wall-clock time (or the submission's `timeout_minutes`, whichever is smaller). The clock begins when the container starts executing, not when instance provisioning begins; AWS capacity delays do not count against it. The instance is always terminated when the script exits.
- **Code review.** Before running any submission, a First Proof team member does a lightweight review (15–30 minutes) of the Dockerfile and `src/`: that the code is structurally sound, declared dependencies match what the code imports, and the hardware request matches the rationale. It is not a line-by-line audit. No run is scheduled until the review passes.
- **Instance type allowlist.** Only types in [`allowed-instances.txt`](allowed-instances.txt) may be requested. Unlisted requests are returned for revision.

## Grading

Human graders provide a detailed review of each solution and assign **separate scores for correctness, exposition, and attribution**. Scoring is **negative for wrong solutions** on the correctness axis — a wrong proof scores worse than a blank one, so submitting a confidently incorrect solution is worse than declining to answer. Full details are in the Batch 3 call for submissions.

## Turnaround and communication

- **Turnaround.** Results are published on October 14, 2026. A submission is valid when: (1) the repository is accessible, (2) `hardware.json` is well-formed and the instance type is approved, (3) any required secrets have been received, and (4) the code review has passed.
- **Validation feedback.** If any validity condition is unmet, First Proof notifies the submitter with a specific description of what to correct.
- **Run failures.** If a run fails (non-zero exit, timeout, or empty output), First Proof notifies the submitter promptly with the exit code, runtime, and available stdout/stderr. First Proof provides all available logs but is not responsible for debugging submitter code.
- **AWS instance availability.** If AWS returns `InsufficientInstanceCapacity`, First Proof retries in another Availability Zone and then another region. This is outside First Proof's control, but First Proof will make best efforts to obtain capacity.
