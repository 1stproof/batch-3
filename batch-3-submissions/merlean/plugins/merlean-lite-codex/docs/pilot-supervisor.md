# Outer pilot supervision

The outer keeper runs independently of the prover and the pilot's internal
watchdog. New exam campaigns enable the internal watchdog by default. The keeper
adds durable launch ownership, process-identity observation, optional narrow
automatic continuation, and an optional bounded Astra infrastructure diagnosis. It never treats a checkpoint as success.

## Start and observe

Use the maintained checkout. Plain `codex` and its normal login are the defaults.
For research isolation, an explicitly configured task home may link only that
normal account's authentication; do not inherit unrelated sessions or settings.
Never substitute a numbered account or silently switch models or billing.

```sh
scripts/merlean-pilot-supervisor run /absolute/supervision /absolute/new-run -- \
  --problems /absolute/inputs/problems.json --exam --internet-browse on
```

The supervisor state directory is separate from the campaign. An exclusive
reservation precedes process creation; the operating-system lock prevents two
keepers for one operation. Source and policy hashes are bound before dispatch.
The supervisor remains active while the recorded child identity is alive and
writes atomic status observations. A repeated command cannot replay the launch.

After a keeper interruption:

```sh
scripts/merlean-pilot-supervisor watch /absolute/supervision
```

This observes the saved child identity only. Unknown ownership, a reused PID, or a
missing launch receipt requires reconciliation. The keeper does not kill an
unverified process, reset an exam clock, unseal a campaign, clear a reservation,
or launch a replacement on a timer. Historical failures copied into a successor
are excluded from its current provider-availability status.

## Optional independent keeper

On macOS, `recipe` generates a task-scoped launchd plist without installing it:

```sh
scripts/merlean-pilot-supervisor recipe --recover-on-failure \
  /absolute/supervision /absolute/new-run -- \
  --problems /absolute/inputs/problems.json --exam --internet-browse on
```

The generated recipe binds the sanitized runtime environment, working directory,
maintained source and requested command. `KeepAlive.SuccessfulExit=false` restarts
a crashed keeper. With `--recover-on-failure`, the recipe also schedules a
600-second wakeup. Healthy monitoring and scheduled reentry consume zero model
calls. A completed or blocked incident returns its durable result; it does not
repeat a census, diagnosis, or launch. Installing or loading the recipe is a
separate explicit host operation. Creating this file does not install a service.

### Narrow automatic continuation

`--recover-on-failure` is prospective opt-in for fresh campaigns. It handles only
a host-recorded local `EAGAIN` or `ENOMEM` failure at the model-process creation
boundary, with explicit `model_dispatched: false` and exact terminal stage binding.
It does not classify provider prose, generic infrastructure errors, quota pauses,
paper failures, or arbitrary host crashes as safe retries.

The guardian records each generation in `guardian-state.json` and keeps its
individual launch receipts under `generations/`. Keeper reentry watches that
generation's saved process identity. A **new native continuation** is allowed only
when the parent has a committed terminal result, sealed campaign, exact saved
responses and submitted proof checkpoint, and a consistent existing main session.
The guardian automatically constructs a stopped-process census outside the parent
and runs the existing native validators. Any live, reused, permission-hidden or
unknown process, pending launch, unfinished execution, unsubmitted draft,
exhausted review or unresolved handoff blocks recovery. It never signals processes.

The successor preserves the original exam start and deadlines, main session,
completed work, review/execution history, counters, model selections and selected
binary/environment route. Frozen code, policies and protocol settings must match
maintained source exactly; no implicit migration or policy change is allowed.
This preserves a route, not a claim of independently verified account identity;
the guardian makes no account RPC. Native launch preflight remains unchanged.
A new main-owned scientific checkpoint is required before another automatic
recovery. New request IDs, duplicate answers, timestamps, file paths, whitespace
and a different transient errno cannot reset that brake. Existing native
successor reservations and per-generation launch reservations enforce at most one
successor; an interrupted launch without its durable identity is never replayed.

Recovery resumes the main with the preserved context; it does not blindly repeat
the failed role. Starting a child is not proof that research progressed or that
an exam is complete. Ordinary research calls resume only after native checks pass.
All guardian monitoring, census, eligibility and continuation decisions are
zero-model operations. `--diagnose-on-failure` may be added separately for the
existing bounded event diagnosis after safe continuation is unavailable; it has
no automatic patch or scientific authority.

Only an armed, matching guardian generation defers exam paper admission after
this exact pre-dispatch failure. The existing `unresolved.tex` fallback remains;
the result explicitly reports pending delivery and no PDF. The guardian does not
freeze an early research snapshot. If recovery is blocked or the original clock
closes, missing paper/PDF delivery stays an attention item. Ordinary exam launches
retain their existing paper behavior. A hard crash without the terminal result
and seal remains blocked rather than receiving a fabricated completion receipt.

## Failure diagnosis and repair

With `--diagnose-on-failure`, a current infrastructure failure, unexpected stop,
or unfinished paper at an unexpected terminal boundary can trigger
one independent offline `gpt-6-astra` diagnosis **after whole-stack stopped-process
reconciliation**. A dead host alone is insufficient: lower reviews, tools, probes,
or a pending launch may still be active. Healthy observation uses zero
model calls. The default diagnosis has a 60-second timeout, low reasoning effort,
a 24 KiB total UTF-8 request bound and an 8 KiB accepted response bound. These
are time/input/acceptance bounds, not a verified hard billed-token cap; missing
usage remains UNKNOWN. Source excerpts replace whole-file/history dumps. The same operation cannot repeat
that paid diagnostic call. A provider quota failure pauses further model dispatch,
including exam paper writing and automatic diagnosis; it retains the original
exam deadline. Successful completion and uncertain process ownership do not
trigger automatic diagnosis.

For ordinary supervision, the operator must supply `diagnostic-reconciliation.json`
in the supervisor state directory. An armed guardian can supply the same receipt
for its current generation after its absent-only census succeeds. It contains `reconciliation: {path, sha256}` referencing the native
terminal process-census receipt and `terminal_files`, the complete relative-path
to SHA-256 map of the stopped campaign. The receipt must affirm empty
`active_children` and `pending_launches`, and `all_owned_children_stopped: true`.
The native process validator rechecks persisted PIDs, descendants, process groups,
launches and probes. Missing evidence, active work, changed terminal files or a
successor reservation blocks diagnosis. The keeper reports that reconciliation
is required when the automatic guardian census is unavailable or fails.

The diagnosis is also available explicitly:

```sh
scripts/merlean-pilot-supervisor diagnose /absolute/supervision
```

Its input contains allowlisted runtime metadata, source hashes and maintained
infrastructure code. It excludes problem statements, prompts, answers, proofs,
credentials and model-generated mathematical feedback. Its transport has no tools
or internet access. The result is a schema-checked, evidence-bound repair proposal
with proposed diffs and verification steps. It is stored outside the campaign and
has no execution or scientific authority. Apply a proposed repair only to the
maintained checkout after independent review and relevant tests. Never patch an
active or historical frozen runtime.

When an exam is interrupted, resume its existing work. Never invoke a new
`--problems --exam` campaign to recover that exam. Recovery uses the existing
explicit native continuation interface with a fresh successor directory, a stopped-process reconciliation receipt and immutable parent history.
The narrow `--initial-main-recovery` option additionally permits one explicitly
authorized initial provider failure that returned no scientific output. It binds
the old failed session, exact stage/input/clock, selected binary and authorized
account route. It records whether the new conversation preserves or replaces the
failed session; it never invents session continuity or renews the exam clock.
Neither the keeper nor an Astra proposal is authorization to bypass these gates.

### Explicit paper recovery after new research

`--paper-recovery /absolute/request.json` is a continuation-only native route for
an exact first-writer reconstruction that completed but lacked required evidence
delivery. Construct its request with
`pilot_paper_recovery.make_request(parent, successor, reconciliation, problem_ids,
authority=...)` only after the whole parent is stopped and reconciled. The native
constructor validates the parent and binds its manifest, fixed successor, original
writer session, rejected response, consumed turn and genuinely changed submitted
research. It cannot replace a successful paper or reuse an existing recovery for
the same problem. Explicit disjoint problem requests can be added in later
successors while prior requests and transitions remain hash-bound history.

Preparation preserves the old snapshot and rejected response, freezes current
research in a separate immutable snapshot, and pins a transition receipt. Accepted
research must pass ordinary native carry validation; partial work stays partial.
The same writer must actually read both the mandatory historical evidence and
current research sources. The corrective call consumes an existing retrieval turn
(the first rejected turn remains spent); it grants no additional allowance, retry
loop, acceptance or grade. A completed interrupted correction is reconciled from
its exact admitted scope without another dispatch. All normal paper review and
delivery gates still apply.

If research changes again after the revised snapshot, paper dispatch fails closed
instead of publishing stale evidence. Prefer authorizing a completed problem when
its evidence is settled. This route does not mutate an active or historical run,
refresh every paper automatically, or modify the separate historical
`--paper-delivery-contract-reconciliation` exception. The original exam clock,
model choices and account route remain unchanged.

## Recheck a quota pause without model tokens

A real provider refusal pauses research, paper writing and paid diagnosis. A later
subscription upgrade or quota reset does not restart that stopped campaign.
Operational pauses now report `needs_attention: true`, including saved terminal
observations read after a keeper restart.

Research completion and paper completion are separate. An unfinished paper
reports `paper_incomplete` with attention required. The opt-in keeper can request
a bounded diagnosis only after the entire lower stack has been reconciled as stopped. A current paper storage/transport-reconciliation
failure is recorded explicitly as infrastructure failure. Historical paper
errors do not override a subsequently polished, terminal paper result. Every
diagnostic still requires the whole lower stack to be stopped and reconciled.

After independently reconciling the whole lower stack, an operator can request a
bounded account-metadata recheck:

```sh
scripts/merlean-pilot-supervisor recheck-quota /absolute/supervision \
  --route /absolute/reviewed-account-route.json
```

The reviewed route is a JSON object with these bindings:

- `schema_version: 1`, `authority: "explicit_operator_verified_selected_route"`.
- `root`, `attempt_sha256`, and `host_config_sha256` identify the stopped operation.
- `codex_binary` exactly matches its saved selection; `codex_binary_sha256` pins
  that binary or wrapper. No shell command strings are evaluated.
- `codex_home`, `auth_source` (the resolved authentication file) and `account_id`
  identify the selected account. Do not place credentials in this file.
- `environment` records only the selected route's `HOME`, `PATH`, `USER`,
  `LOGNAME`, `TMPDIR`, `LANG`, `LC_ALL` and `CODEX_HOME` as applicable. `CODEX_HOME`
  must match the route; originator, provider and API credential overrides are refused.
- `reconciliation: {path, sha256}` and `terminal_files` carry the same complete
  stopped-stack evidence described above. Do not manufacture a census from the
  host's exit code or copy a receipt from another operation.

The recheck requires a current-operation terminal quota failure, a freshly absent
host, unchanged stopped-state evidence, no active/admitted stage and no native
successor reservation. The full native process validator must also pass. These
gates run before account RPCs or query-attempt reservation. Healthy or uncertain
lower work never triggers a recheck, diagnosis, repair or restart. Once a successor
is reserved, the historical parent's rechecks stop, even if its old status still
says `quota_paused`.

Only initialize, account-read and rate-limit-read RPCs are sent. MCP/app surfaces
are disabled; there are no threads, turns, tools, model calls or authentication
refresh requests. Each invocation has a 20-second RPC deadline and bounded cleanup;
durable throttling allows at most one query per ten minutes. A crash or unknown
helper ownership blocks another query until explicitly reconciled. The original
exam deadline is retained, and expired exams are not queried.

An immutable `quota-recheck-*.json` receipt records the result. The separate
`quota-recovery-handoff.json` can report `saved_state_review_required`; this means
only that the returned account metadata showed no limit. Global quota percentages
do not establish Astra, long-context or resumed-turn availability. Missing/null
windows and account mismatches remain unknown. The historical campaign remains
paused; this command never dispatches research or changes acceptance.

For optional deterministic monitoring, `quota-recheck-recipe STATE --route ROUTE`
generates a source- and route-bound launchd plist with a ten-minute interval. It
does not install or load it. Its `quota-recheck-scheduled` entrypoint uses the same
gates and zero model calls. Without explicit invocation or installation of this
recipe, upgrades are not detected automatically.

Detection, an infrastructure diagnosis proposal, a reviewed source fix, and an
audited saved-state continuation are separate steps. The supervisor does not
automatically apply patches or reconcile unknown processes. Automatic research
continuation is limited to the explicitly armed pre-dispatch route described above.

## Document startup check

Each scoped document stage copies and hashes its small Python runtime into the
stage directory. Before paid model dispatch, the selected Codex binary (including
its configured OS wrapper) starts the MCP server through app-server inventory
RPCs. No thread, turn or document tool operation is requested. The exact server
identity and tool inventory must match. Startup failure leaves a terminal
no-model-dispatch receipt. The probe consumes the stage's existing absolute time
budget; failure or unknown child ownership blocks the paid call.


## Terminal obligations and healthy work

The native pilot writes `operational_attention` in `pilot-result.json`, even when
launched directly without the outer keeper. Each finished problem also gets a
small terminal summary in `host/task-state.json` while sibling problems continue.
A problem can need attention while other owned work remains healthy; the summary
never cancels those siblings. Observational write failures are recorded when
possible and do not cancel research tasks.

A zero process exit is not completion evidence. The current result must cover the
selected problems. A polished paper must declare regular, nonempty `paper.tex`
and `final.pdf` files in that problem's paper output directory, without symlinks.
This is an operational delivery check, not a scientific or PDF-content verdict.
Non-exam research does not acquire a paper obligation merely by using this keeper.
An exam's early partial result remains visible even if a paper was produced.

An owned live host takes precedence over earlier recovered quota failures. Missing
PDF output during active writing is normal. Silence alone never proves a stuck
model. Existing stage deadlines and current owner-matching watchdog faults remain
observable; no new model timer is introduced. An owner-bound snapshot with an
explicitly unscheduled pending problem is an attention signal, not permission to
probe, cancel or diagnose the live stack. Startup and finalizing transitions are
excluded. Historical watchdog incidents are not new alerts.

The outer keeper saves deduplicated `attention-events/` records, and rechecks the
terminal contract on saved-exit reentry. Event keys exclude polling timestamps.
Authenticated manual drain, explicit host-recorded handoff, provider quota and the
original exam deadline retain distinct outcomes. Deadline classification uses the
recorded completion time; observing an old early stop after the deadline does not
make it an expected deadline stop. A dead host without a final result has unknown
completion timing and requires attention. Missing deliverables remain visible even
at an expected deadline, without triggering a paid infrastructure diagnosis.

The native notice does not automatically invoke Astra. The separately opted-in
keeper still requires `diagnostic-reconciliation.json`, unchanged terminal files,
no active/unknown lower work and no successor reservation. Until then it durably
records `blocked_pending_whole_stack_reconciliation`. It can make at most the
existing one bounded diagnostic attempt; no automatic restart, migration, patch
application or budget renewal is added.

### Public sources and explicit offline runs

Fresh research permits public web browsing when it answers a concrete useful question. It is optional, not a mandatory phase. `--internet-browse off` remains an explicit offline opt-out; a saved run retains its recorded policy unless an authorized continuation changes it. Starting a new prospective default never modifies a running campaign. Online scoped stages can fetch and inspect exact public source bytes through the bounded source tools described in `public-source-retrieval.md`. Fresh manuscript-only readers and visual reviewers keep their narrow inputs.

### Source-review delivery continuation

Paper raw and proof audits may request additional immutable evidence in the same
reviewer session. The host can carry **complete artifact reads** along that exact
bounded evidence-request chain when identity and bytes remain unchanged. It
reaudits native events, saved capability hashes, operation receipts, and persisted
model-visible outputs. Partial reads from different turns are not stitched into
coverage. A fresh reviewer or a later writer repair starts a separate chain.
The per-call transport audit remains unchanged; prospective combined coverage is
recorded separately in `paper-delivery.json`. A historical underdelivered response
without that receipt remains rejected during restoration.

A stopped exam may explicitly authorize one full reread for a completed,
underdelivered source review using
`pilot_paper_review_recovery.make_request(source, target, reconciliation,
problems, authority=...)`, then `codex_pilot --continue-from SOURCE
--reconciliation RECEIPT --paper-review-recovery REQUEST TARGET` (with the normal
continuation arguments). The constructor requires native stopped-checkpoint
validation. It binds the exact reviewer, rejected response, immutable scope, and
consumed retrieval turns. The correction reads the full original scope plus a
quarantined copy of the unaccepted review; it consumes the next original turn
within the existing four-turn limit. It cannot request another evidence loop,
reset the clock, or accept the historical response. The original research,
writer-recovery authorizations, raw transport records, and rejection history stay
intact. A durable completed correction can be reconciled after a host crash
without redispatch, while a failed correction cannot automatically retry. Any
later writer dispatch ends this correction's application window; revised
manuscripts require a new independent review.
