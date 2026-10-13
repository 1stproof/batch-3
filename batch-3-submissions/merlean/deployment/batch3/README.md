# First Proof Batch 3 submission

The repository-root `Dockerfile` and `hardware.json` implement the organizer's
container contract. The image runs an online Lite exam with optional Lean,
Astra problem mains and substantive reviewers, configured Sol execution workers,
and an event-driven tool-capable Astra operations agent. Normal health checks
do not call a model. Each problem starts once; recovery preserves saved progress.

## Runtime contract

- Read `/data/input/input.json`, with `{"problems":[{"id":"prob-001","latex":"..."}]}`.
- Write papers, research artifacts, logs and structured usage evidence under
  `/data/output`. `progress.json` updates every few seconds. `solution-status.json`
  distinguishes drafts from accepted papers; a file named `final.pdf` is not by
  itself an acceptance record.
- One container-wide 24-hour clock starts before login or campaign initialization.
  Research closes at 22.75 hours and pending problems enter writing with their
  best supported results. Completed research can enter writing earlier. Missing
  proofs remain explicitly incomplete; writing does not manufacture acceptance.
- The image includes Python/scientific libraries, Lean/Mathlib, LaTeX/TikZ,
  PDF tools and Codex CLI 0.159.2. Public-source browsing is enabled when useful.
- Optional scouts are selected by each main, with a global ceiling of 30 concurrent model
  calls; this is not a utilization target or a monetary budget.

## Authentication: no server endpoint required

Supply `OPENAI_API_KEY` through the organizer's `--env-file`. The image signs in
with an API key, never a ChatGPT subscription or numbered account wrapper. The
key is sent on stdin and its cache stays outside collected output. Neither
credentials nor prior problem attempts are baked into the image.

Create a file **outside the repository**, for example `merlean-secrets.env`:

```text
OPENAI_API_KEY=YOUR_RUNTIME_KEY
```

Do not commit it. Send real secrets through the organizer's agreed secure channel.
If organizers supply sponsored credits, ask them to inject the credential attached
to that allocation. Running our container with a submitter-owned key does not
automatically transfer billing to an organizer-owned account. No inbound API
endpoint or submitter-hosted service is part of this contract.

## Commands

From the repository root:

```sh
docker build -t merlean-batch3 .
mkdir -p output
docker run --rm \
  --env-file /absolute/path/to/merlean-secrets.env \
  -v /absolute/path/to/input.json:/data/input/input.json:ro \
  -v /absolute/path/to/output:/data/output \
  merlean-batch3
```

No Docker socket, privileged mode, host filesystem mounts, extra Linux
capabilities, or inbound network access are required by the launcher. A fresh
output directory is required; an existing run is never silently overwritten.

For a free schema check, with no credentials or model calls:

```sh
docker run --rm \
  -v /absolute/path/to/input.json:/data/input/input.json:ro \
  merlean-batch3 /opt/python/bin/python -B \
  /opt/merlean/src/batch3_submission.py --validate-input
```

The organizer's approximately 30-minute smoke test is an external test timeout,
not the formal research deadline. Do not hardcode that test duration into the
24-hour exam. A real authentication/model smoke test spends API credits and must
use a credential with access to the configured models.

## Usage and completion

Raw per-stage events and `stage.response-usage.json` files preserve provider
usage, including reported reasoning tokens, under the run's runtime artifacts.
Native accounting deduplicates authenticated response IDs. Missing provider
usage remains UNKNOWN, not zero; cached tokens and reasoning tokens are subsets
of input and output respectively. Operations event logs are also retained.

Source tests and a dependency/container check cannot establish API entitlement,
API billing completeness, or the quality of a future proof. Review the actual
smoke-test results before the scored run. The upstream models must meet the
organizer's public-availability cutoff.
