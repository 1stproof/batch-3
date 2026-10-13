# Event-driven Astra operations

`pilot_operations.py` is an opt-in operational sidecar. It checks native supervisor status without model calls while the exam is healthy. An actionable terminal infrastructure failure wakes one persistent Astra operations conversation through the ordinary Codex CLI with its tools enabled. The operator diagnoses the problem, requests independent review, and uses native continuation when justified.

This is operational delegation. It does not make model-written repairs automatically safe, award scientific acceptance, or authorize resetting clocks, review allowances, paper turns, sessions, or saved work. The English mandate is in `pilot-operations-prompt.md`.

## Start

Use the same Python environment, ordinary Codex account, and PID namespace as the supervised exam. Keep sidecar state and its writable working directory outside every exam root.

```bash
python3 src/pilot_operations.py init /work/operations-state \
  --operation /work/supervisor \
  --codex /opt/codex/bin/codex \
  --workspace /work/operations-work
python3 src/pilot_operations.py watch /work/operations-state --once
python3 src/pilot_operations.py watch /work/operations-state
```

Initialization and a healthy observation make no provider request. Use the installed, explicitly selected Codex binary; the example path is not a version override. State binds that executable and the mandate. The launcher uses `--ignore-user-config` and `--ignore-rules` so research-specific tool restrictions are not inherited; authentication still uses the normal `CODEX_HOME`. It launches `gpt-6-astra` with high reasoning effort and workspace-write tools, without interactive approval prompts. Explicit `init --container-tools` enables full unsandboxed tools only in an externally confined task container. Run this only in the authorized operations environment.

The foreground watcher can be run under an existing service manager. Reentry uses the same state directory and process ownership checks. An ambiguous prior launch or uncertain process identity requires attention and must not be treated as permission to launch a second operator. Keep the existing namespace keeper alive when the exam depends on it. No Docker socket or privileged container is required to attach a sidecar within that container.

For an image whose `/opt` source is read-only, stage the sidecar and its mandate outside the exam roots and import the trusted installed runtime helpers. Proposed repairs belong in a separate writable source copy. Do not patch a running exam's frozen source.

## Follow native continuation

After an actual descendant is running, publish its native supervisor operation:

```bash
python3 src/pilot_operations.py route /work/operations-state \
  --operation /work/supervisor-next
```

The original deadline and models remain binding. Update external status consumers to follow the sidecar's route; the route does not itself launch or restart an exam. Preserve all old operations, results, and process evidence.

## Evidence and limits

The sidecar stores compact observations, per-incident prompts and JSONL events, the operator session ID, process identity, and durable incident deduplication. A new incident may wake the same conversation after cooldown. Provider quota errors pause operator dispatch; an unresolved incident permits at most three cooldown-separated turns in the same operations conversation; a recorded blocked or quota disposition with a reason suppresses further dispatch. A self-reported resolution cannot hide native unfinished work. The original exam deadline prevents new operations calls and requests termination of the exactly identified operations process, never research processes.

Tests use real local fake-CLI subprocesses with native supervisor observation. They establish launch, ownership, session, and state behavior without provider calls. They do not establish that an arbitrary future model repair is correct. Independent review and post-continuation verification remain required operational work. Never collect authentication files or session-home archives as diagnostic evidence.

## Protocol repair versus scientific correction

A rejected writer response is not automatically a permanent scientific blocker. The operator may investigate a generic checkpoint or protocol defect that prevents the original writer from correcting its own response within the remaining existing allowance. Any recovery must bind the exact rejected response, original session and consumed counters, retain the rejection, pass independent software review and tests, and use native continuation. The operator cannot supply corrected manuscript content, invent evidence, accept the rejected response, relax release gates, or reset allowances. A valid protocol response may still fail scientific or release checks.

Updating the mandate does not clear an existing blocked disposition, create a new incident, or replenish the three-turn operations circuit breaker. Historical decisions and all research and paper budgets remain intact. Deployment or a specifically authorized new recovery requires its own evidence and lifecycle checks.
