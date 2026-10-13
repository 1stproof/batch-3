# Optional Codex subscription pilot

`scripts/merlean-codex-pilot` is an opt-in host adapter for a Lite research
pilot. Ordinary MerLean single-project behavior and the metadata-only selector
remain unchanged. This adapter is separate from a competition delivery container.
Fresh `--problems` runs default to exam mode, using the shared 22.75-hour research / 24-hour delivery clock
and separate automatic paper workflow described in [exam mode](exam-mode.md).
Use `--no-exam` on a fresh run to opt out of the clock and automatic paper workflow.
Existing runs and reconciled continuations inherit their saved mode and original clock;
neither `--exam` nor `--no-exam` may change them.
Paper status never changes research acceptance, and an honest partial manuscript is
not a completed original proof.

## New run

Prepare a JSON mapping from problem IDs to UTF-8 LF text files, relative to the
mapping file. Supply only original problem statements, never reference solutions.

```sh
scripts/merlean-codex-pilot /outside/tool/tree/pilot \
  --problems /outside/tool/tree/originals.json \
  --internet-browse on \
  --codex /absolute/path/to/audited/codex
```

The pilot directory must not exist. The run freezes original bytes, workflow
snapshots, host configuration and a source-code snapshot, then initializes the
existing campaign table with a controller key outside the campaign subtree.
Two or more registered problems run concurrently, with at most 30 live model
calls across the entire fresh pilot. This is a ceiling, not a utilization target;
unused capacity never requires extra agents. Each main may optionally select two, three or
four genuinely distinct advisory Astra scouts, within the shared capacity, or omit
exploration when one route suffices. General exploration permission does not bypass
convergence: a promising skeleton focuses work on its necessary gaps. Saved runs
inherit their existing concurrency and route width; missing legacy route settings
remain disabled. Every problem retains its own Astra main conversation and mathematical
plan. All registered problem loops are started independently; the shared limit applies to
active model calls (mains, scouts, workers, reviews and paper stages), not the number of
problem loops. The outer controller/keeper handles lifecycle, clock, status and emergencies;
its normal work is deterministic, with optional event-driven Astra supervision/diagnosis.
It does not replace the problem mains or select their mathematical routes. Main-owned bounded
execution requests default to `gpt-6.1-sol`; explicit `--execution-model gpt-6-sol`
remains supported. Saved model selections and legacy saved runs without an execution-model
field retain their original model; new defaults do not migrate them. Substantive reviewers use fresh
`gpt-6-astra` contexts. The explicit per-run `--execution-model gpt-6-astra` option
is for a user-approved override, not an automatic fallback.

## Browsing and authentication

New runs default to `--internet-browse on`. Explicit `--internet-browse off`
disables cached as well as live web search. CLI features for file, shell,
connector, plugin, interactive browser and delegation execution stay disabled.
The host performs numerical and Lean work and supplies exact results. In proof-document
version 1, an explicitly configured local document channel also permits confined proof
draft updates and immutable evidence reads; it does not grant general file execution.

ON enables native web plus the Code Mode host required by CLI versions that expose
web through `functions.exec`. The only accepted bridge source is exactly
`text(await tools.web__run(JSON_OBJECT));`, with a literal JSON request and no
other statements or expressions. The saved-rollout audit parses the actual call
source; a model's claimed web-only marker is never trusted. This is a tool-use
audit, not a promise of preventing arbitrary JavaScript before execution. Other
tool attempts and broader bridge programs invalidate the stage. OFF rejects this
bridge too. Both live CLI events and saved rollout records are checked, including
hidden calls omitted from the CLI stream. Missing audits fail closed. Run live
search/open and same-session continuation checks against the installed CLI before
relying on ON for an evaluation.

The adapter currently supports audited CLI 0.153.0, 0.157.1, and 0.159.2.
Scoped document tools require 0.157.1 or 0.159.2. Pin its absolute executable;
it does not install or downgrade Codex. It ignores user configuration/rules and
host skill discovery, pins OpenAI plus ChatGPT authentication, and excludes API
keys and provider overrides from the child environment. Authentication remains
in the existing Codex host; no credentials are copied into artifacts. An
unsupported model or subscription limit is a real failure, never permission to
switch models/accounts or use API billing. If only the optional execution model
is explicitly unsupported, its failed task is returned to the existing main as
unavailable; the main may continue its own research using host probes. The host
does not silently dispatch that worker task to a different model or repeat the
known unsupported request. Main/reviewer failures and rate/quota failures retain
their stopping rules. Tokens are host-reported telemetry. Exact response records feed the shared
accounting ledger automatically; optional frozen prices provide comparisons only.

## Numerical and Lean checks

On supported macOS hosts, numerical Python probes execute in a deny-default
kernel sandbox with a sanitized environment, no project/home reads, writes,
network or child-process creation, and bounded CPU, wall time and output. An
optional preinstalled Lean/Mathlib runtime can be configured explicitly:

```sh
  --lean-executable /pinned/toolchain/bin/lean \
  --lean-library /pinned/mathlib/.lake/build/lib/lean
```

Repeat the library option for already-built dependency libraries. Only the
pinned runtime/library roots and exact temporary source file are readable.
No Lake/Elan download or build occurs. The host retains source and diagnostics;
compilation alone never awards Silver or Gold. Faithful statements, explicit
axiom reports, closed premise manifests and independent review remain required.
macOS provides no hard resident-memory bound in this adapter. Unsupported hosts
fail probe execution closed and keep the research obligation unresolved.

## Feedback, limits and recovery

Sol/probe results return to the same main before acceptance. Intermediate candidate
revisions receive fresh focused proof review, carrying every known mathematical finding.
The existing focused review also selects useful local certificate work and approves bounded
research tasks; there is no additional review dispatch solely for execution authorization.
An independently established local inference may be selected while other research gaps
remain open. Those gaps still block final acceptance. Newly authorized work returns to
main for reconciliation; the final candidate receives
a fresh comprehensive proof review, two independent final original-scope reviews and a separate Silver
review. The existing controller validates hashed evidence.
Rejected controller findings return to the same main with stable ticket IDs and
fingerprints; authority tokens are recursively removed. A completed real turn
records delivery, while only current validation resolves findings. A scope pass
alone cannot mark the selected-grade task successful.

### Candidate and certificate handoff

The independent reviewer supplies `triage_decisions` for every ledger row: `row_id`, `selected`, `trigger`,
`reason`, `goal_relevance` and `inference_ready`. Trigger values are `exhausted_debate`,
`theorem_crux`, `sampled_computation`, `none` or `research_gap`. Removing an earlier selection
also needs the reviewer's `reassessment_reason`; main's
own selection flag cannot authorize Lean or erase the earlier selection history.
These fields expose a mathematical decision for review;
a trigger label or importance to the goal alone does not justify Lean. Select local work
only after a viable NL inference exists. A row with `inference_ready: false` must be marked
`research_gap` and belongs in mathematical development; any such gap blocks a proof pass.
Zero to three certificates is typical, never an enforced maximum or a proof criterion.

The host lists the exact current ledger IDs in the review prompt and reports expected
and received IDs on a mismatch. Historical-only rows remain evidence and findings;
they are not extra entries in the current triage array. Missing dependencies still
require substantive findings, and an incremental ledger cannot establish full completion
merely by passing checks on its current rows.
Preserving a completed certificate does not require a new selection. A selected row still
requires a current L3 trigger; `selected: true` with `trigger: none` is invalid. A reviewer
may independently unselect a formerly selected row with an explicit reassessment reason,
while retaining its certificate and all historical evidence.

An invalid proof-review protocol response is saved with its exact error and candidate
binding, marked invalid and without authority. The host requests at most one fresh reviewer
retry for that same candidate with the full policy and the labeled invalid response. It
never repairs a review by changing its selection or trigger. Findings, triage history and
execution approvals change only after the complete replacement review and both task
approval lists validate. A second invalid response propagates the failure to the ordinary
honest partial checkpoint; infrastructure and budget failures are not protocol retries.

Main proposes bounded `sol_tasks` with `kind: research` or `kind: lean`; Lean tasks identify
their `row_ids`. Host Lean probes identify `lean_probe_rows`. The reviewer returns
`approved_research_tasks` and `approved_lean_tasks`, indices of the exact proposed tasks
it independently judges useful and within scope. Each Lean task must also reference only
selected rows. Calling formalization a research task does not bypass L3; research
workers must return no Lean code. Unapproved research tasks and Lean requests without
current independent selection are deferred, not dispatched. The reviewer need not approve
any task. Initial direction research uses the existing L0 assumption review for approval;
intermediate work uses the existing focused review. Retrying deferred requests does not
replay previously completed research tasks or Python probes.

The host binds authorization to the candidate's substantive fields, including the exact
proof, answer, ledger claims and dependencies, evidence, assumptions and remaining gaps.
Execution requests and public notes are excluded from that candidate binding; approved
research and Lean tasks are additionally bound to their exact task content. Changed substantive
inputs require fresh review. Restored work retains history but invalidates execution
authorization pending fresh review. The reviewer receives the full Lite workflow and
actual execution evidence to assess substantive reasons and prior findings.
On upgrade, verified historical reviewer selections are retained even if the old main's
row flags differ. The resumed main receives the complete current Lite policy, explicitly
superseding historical allocation instructions while preserving all mathematical evidence.

Reviews keep mathematical gaps separate from typed certificate findings; certificate
findings identify their `row_id`. `mathematically_ready` describes whether all mathematical
inferences are established, but does not itself grant a grade. A mathematically open row
cannot be authorized as certificate work. Selection of a sound local inference does not
require a complete solution to the original question: remaining mathematical gaps survive
and block final grading until comprehensive review and the other gates pass.

Keep routine justified facts, independently checked exhaustive exact computations and exact
audited cited results in the NL ledger unless a particular inference warrants certification.
Preserve previous selections, failed attempts and all unresolved findings when retriaging.
Encoding cost can leave an honest certification gap and BRONZE result; it never closes a
research gap or silently waives the Silver requirement. These are mathematical judgments
for main and independent review, not conclusions inferred by the host from field names.

Main must reconsider the route when successive auxiliary repairs leave the same novel crux
open without useful evidence. Before another auxiliary task, record what now makes that
work relevant to the crux or choose a concrete research move. This workflow allocation
rule does not claim that the adapter automatically detects mathematical stagnation. No
arbitrary workload cutoff is treated as proof, refutation or completion.

Fresh runs default to the exam clock. A fresh `--no-exam` run has no overall
wall-clock cap unless `--minutes N` supplies a total allowance covering model turns
and probes. `--minutes` requires explicit `--no-exam`; it cannot override an exam
clock. Fresh formal exam model calls use the remaining original research/paper
phase allowance, with the existing cleanup reserve; they have no separate test
cutoff. Optional `--exam-model-time-policy test-cap` with
`--exam-test-call-timeout-seconds N` explicitly caps every model role for testing.
Legacy saved runs retain their recorded policy until an explicit continuation
change. See `docs/exam-mode.md`. Auth checks and process cleanup have short bounded
grace periods. Explicit model-capacity failures retry after
ten seconds within the remaining allowance; rate/quota errors and integrity
failures do not use that loop. At limits or operational failures, the pilot banks
an honest partial checkpoint and all prompts/results/history. No result is
accepted just because the allowance ended.

A `HOST-STARTED` marker prevents blind whole-run restarts. Crash recovery is
currently supervised: inspect recorded PIDs, reconcile stopped jobs through the
campaign controller, and resume the existing model conversation and artifacts.
Explicit reconciled continuation is supported below; do not remove the marker to
reset an attempt. `host-progress.json`, immutable stage directories, the campaign
`project-table.md`, and `pilot-result.json` are the monitoring outputs.


## Deterministic internal watchdog

Fresh exam campaigns enable the internal watchdog by default. Fresh `--no-exam`
campaigns leave it off unless `--watchdog` is supplied; continuations preserve the saved
setting. Use `--watchdog-interval 300` to select the observation interval when creating
a campaign. This in-process watchdog does not start the independent outer keeper;
use the explicit supervisor entry or separately install its generated recipe as described
in `pilot-supervisor.md`. It has no effect on ordinary single-project MerLean.
It runs deterministic checks inside the host; it needs neither a desktop heartbeat
nor a permanent model conversation. The interval is configurable and is not a
universal threshold for stuck reasoning.

The host writes `host/watchdog.json`, including current incidents and deduplicated
history, bound to the campaign registry hash and original deadline. Checks cover
owned process identity/liveness, hard deadlines, stale ownership, pending feedback
and repeated infrastructure failures. Capacity waits and quota limits are distinct.
Quiet model reasoning within its deadline is healthy. Explicit substantive
stagnation evidence can request supervisor review through the core's optional
incident callback; this adapter does not automatically dispatch a supervisor.

For a dead child or expired owned stage the host cancels its retained task,
drains its child process group, and saves an honest partial checkpoint. It never
signals an arbitrary PID copied from a status file or starts another attempt.
Cancellation during process creation is reconciled before ownership is released.
Controller feedback remains on the existing exact-fingerprint main-agent delivery
path; a watchdog observation does not acknowledge or resolve a finding.

After a host crash, inspect with:

```sh
scripts/merlean-codex-pilot /outside/tool/tree/pilot --inspect-watchdog
```

This command authenticates controller ownership and writes
`host/watchdog-reconciliation.json`. It makes no model calls, launches no jobs,
and never releases claims. Missing launch records or process identity remain
reconciliation obligations. Whole-host crash recovery still needs supervision;
`HOST-STARTED` must never be removed to reset the allowance. New runs validate the
frozen source snapshot and executing source, problem set, and registry deadline.
Historical runs lacking process fingerprints have limited diagnostic evidence.

## Automatic per-agent accounting

Every transport stage registers its metering state and ingests exact
`token_usage_record.payload.usage` records into `host/accounting/usage.sqlite3`.
`host/accounting/summary.json` groups by model and problem/role/session module;
each response also retains its stage, turn and actual model. Raw response evidence
is saved beside stage metadata in `stage.response-usage.json`. Response IDs are
idempotent keys. Resumed-thread totals are never added as new response usage, and
reasoning/cache subsets are not counted twice.

Failures, cancellation, partial counters and missing records remain explicitly
unmetered while preserving observed subtotals. Check the top-level
`metering_complete` and `pending_or_unmetered_stages`; ledger totals alone cover
only observed responses. Scope excludes setup, development audits, chat and
external monitors.

By default, tokens are unpriced. Supply `--accounting-price-card /verified/card.json`
to copy and hash an explicit verified price card at run creation. These prices
produce API-equivalent scenarios, never actual subscription charges. Accounting
is part of the normal adapter even when the optional watchdog is disabled.


## Continue saved work without a total time cap

For explicit `--no-exam` runs, the default overall deadline is JSON `null`, not a
distant artificial date. Non-exam model calls and probes keep finite hang-protection
timeouts. Formal exam models instead use their original phase clock; the following
single-call recovery policy applies to non-exam and explicitly capped legacy/test calls. A timed-out call may resume its
existing session once after its child has stopped; another timeout without a
completed checkpoint requests supervision. Quota/authentication/integrity failures
still stop for diagnosis. There is no automatic model/account substitution.

To continue a sealed stopped segment, explicitly reconcile its host, stage,
probe and descendant processes. Then supply a receipt to:

```sh
scripts/merlean-codex-pilot /outside/tool/tree/continuation \
  --continue-from /outside/tool/tree/previous-segment \
  --reconciliation /outside/tool/tree/stopped-processes.json \
  --internet-browse on \
  --watchdog
```

The receipt binds the source path, checked UTC timestamp, host PID and complete
owned-PID census, descendant/launch/probe checks, and existing evidence files.
The helper checks process absence again, frozen original/code/policy hashes,
sealed registry, actual completed responses, main identity, reviewer independence,
and the last substantive candidate. A durable exclusive parent reservation blocks
competing continuations of the same main sessions. Failed preparation keeps that
reservation for explicit reconciliation; it is never deleted automatically.

The new segment preserves the old directory unchanged. It carries all prior
stage/probe files, resumes each original main, preserves findings and implementer
identities, advances stage numbering, and returns saved diagnostics before further
work. Initial scouting and already executed tasks are not replayed automatically.
Omitting `--internet-browse` on continuation inherits the parent's setting;
explicit `on` or `off` changes it in the new segment and records old/new values
in its configuration and reservation. The parent policy is never rewritten.
Review commissioning and acceptance are separate. A focused assessment can
commission bounded, candidate-bound comprehensive and original-scope assessments
before every later workflow receipt exists. Readiness and assessment dispatch do
not confer acceptance. Comprehensive review accounts independently for carried
findings, preserves their history and explains any current applicability change.
Unknown applicability and active mathematical or certificate gaps remain blocking.
Actual current comprehensive proof acceptance, original-scope evidence and Silver
checks still govern completion. Safe host provenance accompanies review feedback.

Historical accounting is copied separately and included by hash in the new host
summary. Its ledger is explicitly segment-scoped, with the complete parent report
linked alongside it; segments are not blindly summed. A legacy external passive
ledger may be selected with `--history-accounting /previous/accounting`. Missing or
censored historical usage remains unknown across continuation. Watchdog enablement
is inherited unless explicitly enabled for the continuation.

## Cooperative checkpoint and drain

For hosts containing the cooperative drain implementation, a supervisor can write
`host/drain-request.json` with `schema_version: 1`, `action: "drain"`, a nonempty
`request_id`, and a nonempty `reason`. This is a host operation, never a model
instruction or proof artifact. Request-file creation is not an acknowledgement.

The host observes the request at dispatch admission, closes admission to new
model stages, retries and probes, and lets already admitted work finish. Returned
answers, current candidates and exact available usage are saved before the
problem checkpoints. `drain-admission-closed.json` reports admission closure;
only `drain-ack.json` records committed checkpoints, a terminal host result and
reconciled owned children. A drained partial result is not research completion.
An invalid request fails closed without cancelling already admitted calls.

This mechanism does not retrofit older running hosts. An old host without the
hook requires a natural stopped boundary or a separately authorized supervised
interruption with honest cancellation and accounting records. In every case,
continuation still requires the independent stopped-process reconciliation above.

## Two final original-scope reviewers

The final original-question conformity gate defaults to **two independent reviewers**.
Commission two fresh review contexts on the same immutable original source, current final
answer, theorem interfaces, definitions and evidence. Neither reviewer sees the other's
report or conclusion before returning its own. They must be distinct from each other,
the submitter, every implementer, and the proof and grade reviewers. Both reports must
individually return `PASS_FULL_SCOPE` with complete current bindings and no gaps or extra
premises. A missing, repeated, stale, failing or uncertain report blocks completion; do not
choose the favorable opinion or turn disagreement into a majority/aggregate pass. Preserve
both reports and route all findings to the responsible main. A relevant candidate change
requires a new independent pair for that version. Single-review advisory or preacceptance
scope checks are advice only and cannot satisfy this final gate.


## Candidate updates and blocked checkpoints

A main response explicitly declares `response_type: candidate_update` or
`response_type: blocked_checkpoint`. A candidate update supplies the complete
proof and dependency ledger. A blocked checkpoint selects a previously supplied,
host-owned candidate by its exact hash; natural-language references to an earlier
revision do not select an artifact. The host delivers the selected full candidate
and ledger to subsequent reviewers and saves the raw checkpoint separately.
Availability in this catalog establishes artifact identity, not mathematical
completeness, correctness, or acceptance.

Checkpoint metadata contains a reason only. Proposed work, unreviewed findings,
and the requested review are separate, explicit fields. New proposals replace old
work requests and invalidate prior execution authorization; they cannot inherit
approval merely because their rows were selected historically. Probe requests in
a checkpoint must use exact proposed worker tasks and pass independent task review.
The resulting candidate, including these proposals and findings, receives its own
binding while the selected source artifact remains preserved unchanged.

A checkpoint with no actionable work saves an honest partial result. Repeating the
same checkpoint request with the same substantive execution evidence also stops
partial instead of generating another review cycle. No-op execution bookkeeping
is not new evidence. Substantive candidate fields remain included in their hashes;
a checkpoint cannot hide a changed proof or claim that a procedural receipt closes
a mathematical finding. A malformed typed response receives at most one correction
in the same original main session. Its raw response remains preserved without
candidate authority. Continuations distinguish explicitly recorded legacy stages
from new typed stages and replay only valid selections.

## Final review protocol and prompt representation

The host states the canonical final scope report schema explicitly and validates
report structure and evidence bindings before commissioning the Silver review.
A structural protocol failure permits at most one replacement pair of fresh,
independent reviewers. Both replacements receive identical frozen inputs and the
same schema-only correction; neither sees a prior substantive report. All original
and replacement reports are preserved. An explicit substantive failure, uncertainty,
extra premise, or failed coverage blocks this recovery path. A passing report from
one attempt cannot be combined with a favorable report from another.

Large review packets may encode repeated object-key layouts in ordered schema
tables, in addition to the existing supplied-text, paragraph and line dictionaries.
The prompt supplies every key and literal value with explicit reconstruction rules.
Encoding preserves JSON types, field order, array order, Unicode and whitespace,
and is selected only when the complete UTF-8 representation is smaller. Durable
artifact hashes retain their original serialization. The unchanged predispatch
size guard rejects oversized mandatory evidence without sending a model request
or truncating content; historical evidence is never replaced by an inaccessible
reference to make a prompt fit.

### Audited infrastructure notice on continuation

A supervised continuation may supply `--infrastructure-notice <receipt.json>` to explain
an infrastructure repair to the existing main session. This optional typed receipt binds
the stopped parent manifest, exact successor source and policy manifests, runtime policy,
and copied audit/preflight evidence. The host validates it during preparation, startup,
continuation replay and delivery; malformed present evidence fails closed. Evidence paths
must be confined relative paths, with matching byte hashes. External files are copied so
later edits cannot change the frozen handoff.

The receipt chooses only supported infrastructure-change identifiers; the host supplies
their exact descriptions and acceptance predicates. It does not confer mathematical
validity, repair an earlier report, clear a substantive finding, authorize execution or
schedule a review. The original main may request useful fresh independent review or return
an honest no-action checkpoint. Inherited notices are not automatically active in a changed
successor; their files remain preserved in its history.

Historical preflight evidence is identified as historical and cannot certify unseen future
prompts. Current launch preflights bind the final configuration and delivered notice in a
separate external receipt. They are not embedded back into the notice, avoiding a circular
configuration/notice/preflight hash dependency. Independent proof,
original-scope and grade gates remain mandatory.

An unchanged typed reassessment request remains bounded. After a validated stopped
continuation, it may resume an exact host-recorded `commissioned` or `scope_returned`
assessment only when the candidate and execution binding still match, no final validation
exists, and the existing recovery attempt remains. This one-use admission resumes the
pending assessment directly; it does not dispatch workers or repeat focused review. The
host persists the consumed attempt before dispatch. Completed, rejected, altered or
exhausted assessments do not qualify, and fresh comprehensive and final acceptance gates
remain mandatory. The infrastructure notice identifier `interrupted_assessment_resume`
describes this prospective recovery without changing any historical verdict.


## Exact archived evidence retrieval

After a validated continuation, the original main may return a versioned
`archive_request` for one item marked `archive_retrievable:true` in its continuation
history manifest. The request supplies `schema_version:1`, the exact
`checkpoint_sha256`, `checkpoint_pointer`, `evidence_sha256`, and a nonempty `reason`.
The host reads only its fixed, hash-bound continuation snapshot, checks the exact
original question and main session, and returns the entire indexed item with its
historical identity. A saved `current` item is the checkpoint's old candidate, never
a replacement for the live one. Unknown entries, cross-problem requests, modified
snapshots, noncanonical pointers and items containing controller authority fields
are refused. There is no arbitrary filesystem or network access and no current-run
raw-runtime lookup. Complete delivery never truncates evidence. Actual provider or transport
limits are reported as failures; the pilot adds no artificial prompt byte cap.

One retrieval round is available per main turn. Main then returns an ordinary
`candidate_update` or `blocked_checkpoint`; a repeated retrieval request enters
only the existing bounded structural correction. Raw requests, refusals and exact
results remain in separate operational receipts copied with continuation history.
They do not enter the scientific candidate or execution evidence, renew an
assessment, approve a task, resolve a finding, or award a grade. Historical verdicts
retain their old artifact applicability and never replace current independent gates.

For exploratory reasoning that does not change the stored candidate or introduce
new findings or work requests, use the existing no-action `blocked_checkpoint` and
optional `research_work`. Changed proof, ledger or assumptions still require a full
`candidate_update`. Do not hide substantive changes or new gaps to avoid review.


Review prompt packing also considers one additional candidate using the existing
v4 positive-reference byte costs and dense short word spans. It retains every
previous candidate and decoder and selects by the size of the complete packet,
including instructions and tables. This changes representation only. It neither
omits historical evidence nor changes the prompt cap or any research gate; future
history growth can still require supervised lossless packaging.

## Selected rows in independent review responses

`triage_decisions` accounts for every current ledger row exactly once. `triaged_rows`
contains exactly the unique `row_id` values whose independent decisions have
`selected: true`. It is `[]` when all decisions are unselected; it is not the census
of reviewed rows. Removing a prior selection still requires a substantive independent
`reassessment_reason`, and every selected row still needs a valid L3 trigger and an
established inference.

The host rejects mismatches with the expected selected IDs and received field. Its
existing single fresh structural correction retains the complete invalid report and
diagnostic. A second invalid response stops partial without authorization. The host
never fixes reviewer fields itself, revives rejected reports, or adds a retry.


## Canonical proof documents and immutable submissions

`proof_document_version:1` keeps the original main's standalone `proof.md` separate
from call logs and attempted routes. During an established main session,
`read_current_proof` and `save_proof_revision` support actual in-turn drafting.
Every save requires the exact expected revision; simultaneous or stale saves fail
without overwriting a newer draft. The first dossier of a brand-new run establishes
the real main session before these tools become available. Migrated continuations
have their validated prior proof store prepared before the resumed call.

A revision stores exact Markdown and, on submission, the complete structured candidate.
One atomic `proof-current.json` pointer publishes it. The readable `proof.md` and
legacy `current-candidate.*` files are derived views, never competing authorities.
A view-refresh failure after publication reports the committed revision as requiring
repair; it does not claim the draft was lost or silently create another revision.
Incomplete orphan revisions remain preserved after an interrupted prepublication write.

Draft saves do not dispatch paid reviewers. A `candidate_update` is explicit submission:
when a draft exists, it must provide its current `proof_revision`, exact complete
`proof_markdown` and consistent full ledger, assumptions and findings. The operational
revision identifier does not enter scientific candidate hashes. A stale final body
cannot replace a newer in-turn draft. A save-only `draft_checkpoint` has exactly `response_type`, the current
`proof_revision`, and a nonempty `reason`. It preserves the submitted candidate and
its old proposals unchanged, requests no review or execution, and continues the same main. Newly identified scientific obligations require a
consistent full submission; do not hide them in draft-only notes. Both cases preserve
the current draft, all historical findings and the same original main session.

Independent review reads a pinned submitted revision, with the full plain Markdown
once and its complete current sidecars and obligations. All historical evidence is
kept in an exact indexed archive. Required current support and independently relied-on
material must actually be delivered in full, as verified by tool receipts; an index or
hash is not evidence of its contents. Unknown needed evidence blocks a pass. Where
legacy execution records cannot establish precise current dependencies, one readable
full execution-history file is required rather than separate ritual reads of every
entry. `relied_on_artifact_ids` and `needed_artifact_ids` retain the reviewer's evidence
accountability. Current comprehensive review, two fresh blind scope reviews, Silver and
controller acceptance remain unchanged. New drafts do not retroactively invalidate old
reviews on their original snapshots, but those reviews cannot approve a new draft.

The pilot-specific 1,000,000-byte prompt and 700,000-byte resume guards are removed.
There is no replacement local size threshold or evidence truncation. Actual provider
errors, quota failures, bounded call timeouts and unknown interrupted usage remain
visible. Draft writes themselves add no model usage; accounting still records only
exact response usage with response-ID deduplication and explicit unknowns.

After controller acceptance, `paper-source-handoff.json` identifies that same immutable
Markdown revision, candidate, original and accepted evidence. Paper composition retains
it as source evidence, reconstructs a distinct `paper-raw.tex`, and runs the existing
critical-path, source-fidelity and independent raw-translation checks. The handoff is not
a paper grade, a TeX freeze, or permission to bypass paper gates. Unaccepted drafts remain
research artifacts with explicit gaps, not accepted paper sources.

### Direct document tool exposure

Document-enabled stages bind a stage-local copy of the exact configured model record
and record both original and adjusted hashes. Only five tool-capability fields are
downscoped: direct tool dispatch, no deferred tool search, no internal agents, no patch
tool, and no experimental tools. Online stages retain native web search through the
separate web-search configuration; `supports_search_tool` remains false to expose the
document schemas directly. The supported native `agents.enabled=false` setting also closes
internal delegation for resumed sessions. Every other metadata field, the selected model,
authentication and original session remain unchanged; the shared model cache is never rewritten. Missing
or incompatible model metadata fails before process spawn.

The model must call the advertised document MCP tools directly. It must not search for
them through an execution wrapper. Existing shell, code-mode, worker-delegation and
editing restrictions remain in place; unsupported tool attempts remain failures even
when their prose describes an intended legitimate document operation. A prior invalid
response gains no authority from this prospective repair.

### Evidence coverage across the existing timeout recovery

Large historical collections now also have deterministic immutable chunk artifacts
and a chunk index. Each chunk carries exact Unicode character bounds and its own
hash; the host verifies its bytes against the complete parent artifact. The default
chunk size is a read size, not a retained-evidence cap. Full collections and every
original record remain available unchanged. Reading only the index earns no coverage.

All complete verified chunks together can establish delivery of their exact parent.
The existing same-reviewer recovery may retain those complete chunk receipts; it
does not merge partial responses, inherit another reviewer's verdict, or treat a
partially delivered chunk as complete. Fresh reviewers establish their own coverage.
Required material remains mandatory even when its full delivery is expensive.

When the existing single timeout recovery resumes the same independent reviewer,
its already verified full document reads may remain part of that logical review.
The host rechecks the timed-out stage metadata, capability, immutable artifact bytes,
prompt and durable tool evidence. The resumed call must use the same actual session
and model and identical review scope. Its prompt must reconstruct exactly from the
prior instruction, the existing host recovery suffix, and unchanged document guidance
in the dispatcher's actual order. Its own tool audit must also succeed.

Only full delivery proved by those bound receipts carries forward. A fresh reviewer,
changed artifact or scope, different prompt lineage, other failure category or altered
receipt cannot inherit coverage. This neither adds another retry nor supplies a
mathematical verdict; required and relied-on evidence still needs complete verified
delivery. Earlier rejected reviews remain raw historical evidence with no revived
authority. Interrupted usage remains unknown beyond exact recorded response usage.

### Explicit reviewer metadata contract

A reviewer deselecting a row must provide an independent, nonempty
`reassessment_reason` whenever the latest independent decision selected it **or**
the current candidate ledger marks it `triaged: true`. The host supplies the exact
currently applicable row IDs using the same predicate as validation. An earlier
independent deselection does not remove the reason requirement while the current
candidate remains triaged. The reviewer still decides whether deselection is justified.

Finding-disposition `rationale` and `evidence` fields are nonempty strings. A list of
evidence strings does not satisfy that existing field contract. Deterministic feedback
identifies invalid fields for each finding so the independent reviewer and original
main can understand why accountability remains incomplete. Structural diagnostics do
not establish the truth or adequacy of evidence, and the host never writes a reason,
joins an evidence array, drops an unresolved finding, or repairs a raw review into
authority. Existing bounded corrections and all scientific acceptance gates remain.

An unchanged completed assessment remains deduplicated after this interface upgrade.
A raw positive verdict cannot override failed accountability checks, even when a
disposition names no current consumer. Historical reports retain their original
authority status; the notice alone does not reopen a review or grant another attempt.

### Exact sharing in main feedback delivery

Document-enabled main turns preserve the complete original task in the immutable
`main-task-original` artifact. Before chunking, the host may share byte-identical
JSON objects or arrays from `LATEST FEEDBACK` when the complete representation is
smaller. The required `main-task` then contains readable shared definitions, every
original occurrence path, explicit reference bindings, and the remaining root.
Bindings belong to a separate protocol envelope; ordinary user keys never become
references. Key and array order, Unicode, statuses, provenance and every distinct
finding version remain exact. Finding IDs are never a deduplication key.

The host verifies inverse reconstruction against the original task hash before
publishing the document scope. The index and locator bind both hashes and the
representation kind. Unsupported JSON formatting and inputs without a net saving
retain their exact original representation and the same complete-read gate. An
error after factoring starts prevents dispatch. Chunk size remains transport
framing, not an evidence limit. Main reads every unique definition, root and binding
in the required representation; it can use shared content directly at the listed
source locations without manually rebuilding JSON. Reading only an original copy,
a reference, index, partial chunk or prior-session memory does not satisfy the
required representation's delivery audit. Draft saves remain possible, but candidate
application, checkpoints, archive responses and controller acknowledgement still
require complete current-stage delivery. This optimization does not make history
optional, change source authority or alter any scientific acceptance gate.

Continuation process reconciliation recognizes historical reviewer text chunks
whose filenames end in `.json` only through their persisted review capability,
exact stage/request binding, content-addressed local evidence paths, immutable
hashes and verified parent substring boundaries. These authenticated slices are
opaque evidence, not independent process metadata. The complete JSON parent still
enters the full PID census, including when a chunk equals its entire parent. All
other JSON remains strictly parsed; malformed process/control metadata or unbound
raw evidence blocks continuation. Every evidence file remains in the parent hash
manifest. This compatibility repair changes no process liveness or lineage checks.

### Registered local-module lineage and historical evidence

Local-verification reviewers receive a closed list of the latest registered module
IDs. A task link's `prior_module_id` must be an exact current ID, or JSON `null`
with `relation: "new_claim"` for a first registered lineage. This label describes
registry bookkeeping; it does not claim mathematical novelty, erase historical
work, authorize repeated work or reset an existing budget. Historical probe paths,
worker labels and older module generations remain evidence and cannot substitute
for a current module ID. Reviewers must independently address that history and may
decline approval when its relationship or the proposed new value is unresolved.
An empty registry requires empty module reassessments and null parent links for
any independently approved tasks; it never requires a task to be approved.

Unknown/stale IDs and missing reasons remain protocol errors. The same single
fresh correction opportunity applies, with every invalid response preserved and
no execution authority granted. All scientific selection, task admission and final
acceptance gates remain unchanged.


### Required evidence pages and truthful verification deficits

Document-enabled Codex reviews expose `read_required_evidence({"page": 0})`.
Follow its deterministic `next_page` across all required collections. Each page
contains at most 64,000 Unicode characters from the exact immutable parent; the
final page can be shorter. This is transport framing, not a total evidence limit.
All historical files, item reads and 16,000-character chunk fallback reads remain
available. The host audits persisted model-visible output hashes; sending a page
or reading a catalog never establishes its delivery. Verified parent intervals
can cover their exact authenticated chunks, and only complete chunks/collections
survive the existing same-reviewer timeout recovery. Its prompt identifies missing
pages; a fresh reviewer receives no inherited credit. No additional retry or
deadline is introduced.

For a particular document, call `read_artifact({"artifact_id": "listed-id"})`.
The host resolves the scoped file and verifies its saved version; no caller hash
is needed. Optional `start` and `end` are Unicode character offsets, defaulting
independently to 0 and the complete text length. A supplied legacy hash must still
match. These reads grant no access to arbitrary filesystem paths.

A valid incomplete review may preserve negative findings without full delivery.
The effective report explicitly withholds its positive claims: no finding
resolution, certificate deselection, task approval or global readiness is applied.
Its original raw response and hash remain preserved. Delivery stays open in the
convergence state, separately from mathematical, certification and scope deficits.
This is executable Codex-pilot behavior; the shared workflow states the generic
policy for the other providers without claiming their transport was modified.

The existing completed-assessment dispatch key and its no-execution deduplication
are unchanged, preserving compatibility with inherited assessment records. Exact
candidate/receipt applicability and all raw history remain intact. Delivery progress
does not transfer a verdict to a different candidate or reviewer.

### Select only checks with a concrete verification benefit

Before approving a new Lite Lean task, identify the exact unresolved uncertainty after
natural-language development and independent review, the evidence already available,
the actual intended objects and use-site map, and the noncircular accepted premise
boundary. State what a faithful certificate would newly establish, how its encoding
can fit the proposed local bounds, and why that value warrants the expected cost.
Novelty, importance, dependency fan-out, or a wish to accumulate certificates alone
is not selection evidence. Zero new Lean tasks is valid when independently justified.
This does not retire existing obligations: preserve their failed attempts and require
substantive independent reassessment before replacement or deselection. No automatic
retriage, retrospective approval, downgrade, or change to Silver requirements follows.

### Coherent execution inside an approved local module

An unchanged independently approved local task may run a bounded worker/source → host
compiler → implementation-repair cycle before returning for scientific acceptance.
In the host protocol, `compile_pending` explicitly requests that cycle and supplies
source, the exact selected row, `implementation_complete` and a concrete `next_step`.
It need not claim uncertainty reduction before receiving its first real diagnostic.
`implementation_complete` is the worker's coverage claim, not acceptance: a clean
compile of a full implementation stops for independent premise, intended-object and
certificate assessment. A failed compile or compiled incomplete implementation can
receive the next bounded repair with all exact prior source and diagnostics.
Generic `local_evidence` alone does not request repeated implementation. Identical
source resubmission supplies no new diagnostic work and stops the cycle.

Keep the same immutable task, claim, actual-object interface, premise closure, owned
scope, candidate and independent approval binding throughout that cycle. Count every
worker call and probe against the original cumulative module limits. Retain every
attempt and failure; replacement generations inherit consumed counters, never a new
allowance merely for changed wording. Every dispatch and compiler invocation must
revalidate those bindings and respect the host's drain, deadline and resource controls.
Where workers cannot invoke Lean directly, returned source is a request to the host,
not a failed compilation. Reconstructed worker contexts must receive the full retained
implementation evidence with continuity loss disclosed.

Goal/premise/interface/scope/budget changes, material mathematical counterissues,
encoding infeasibility, no-value evidence, missing host execution, and exhausted bounds
return to main under the existing independent reassessment rule. Terminal historical
reports, including `returned_to_main`, remain terminal; protocol migration does not
relabel them as pending or authorize replay. No scientific reviewer is required merely
between source and its first authorized compiler diagnostic. Independent acceptance
after the resulting certificate, comprehensive full-proof review, two fresh original-
scope reviews and all selected-grade gates remain unchanged.

## NL capability

For a fresh Lite campaign, `--nl` disables Lean workers, local-module admission, inventory and probes. The frozen `nl_only` flag is immutable across continuations. Existing triage, budgets, full proof review, two fresh original-scope reviews and Silver gates remain unchanged. See [NL mode](nl-mode.md).

### Exhausted independent review

A document-backed proof review that times out and consumes its one same-reviewer
recovery remains exhausted across continuations. The host authenticates both raw
stage records, immutable task scope, and delivery receipts. These records carry
operational facts only: timed-out commentary is never a verdict, a resolved
finding, or task approval. Original deadlines and consumed calls remain unchanged.

The original main receives the operational failure and can continue research.
Neither a different reviewer/model/lens nor metadata, row order, whitespace,
status, or a retry request renews the same scientific material. A fresh review
requires changed proof text, answer statement, or ledger claims accepted from a
later completed turn of the same original main, with a recorded content difference
and main receipt. Evidence-only churn does not reopen admission. This is a
conservative changed-content check, not a machine judgment that the mathematics
improved or that differently worded arguments are semantically different. All
independent task, readiness, original-scope, Silver, and paper gates still apply.
The exhausted reviewer session cannot be reused.

### Save-only draft response

When proof documents are enabled, a turn that only saves the current unsubmitted
draft returns exactly three fields:

```json
{"response_type":"draft_checkpoint","proof_revision":"<current revision>","reason":"<nonempty operational reason>"}
```

Read the current revision with `read_current_proof`. Its returned `proof_sha256`
and other receipt fields are not extra response fields. A draft checkpoint does
not submit scientific work, publish a new candidate, approve execution or review,
or change an acceptance gate. Submitting a changed proof still requires the full
`candidate_update`, its exact current revision and body, and consistent sidecars.
A pending draft cannot be bypassed using `blocked_checkpoint`.

The same exact contract is included in the ordinary main task, document-tool
instructions, and the existing single structural correction. Rejection diagnostics
identify missing and unexpected fields without deleting, interpreting, or accepting
model content. A second malformed response still stops the bounded correction;
historical rejected responses remain rejected after an infrastructure upgrade.

### Compile-pending field placement

For host-managed local Lean modules, `implementation_complete` (boolean) and
`next_step` (nonempty string) belong **inside `local_module_result`**, alongside
its module ID, outcome, scope, uncertainty and evidence fields. The exact source
`lean_probe`, singleton approved `lean_probe_rows`, and empty `python_probe`
remain at the response root. Root-level completion or next-step fields do not
satisfy the nested contract. Shape diagnostics retain the original return and
do not repair it, grant retries, execute code or certify a claim. Historical
returns retain their original interpretation and consumed budgets.

### Explicit CLI upgrade during continuation

`--continue-from PARENT --continuation-codex /absolute/canonical/codex`
selects an explicitly audited executable for the successor. The binary must be a
regular executable at its canonical absolute path. The host checks its hash
before and after subscription preflight and records the old path/version and new
path/hash/version in the continuation policy receipt before reserving the
successor. This option cannot be combined with initial-main recovery.

The original sessions, exam clock, history, paper progress, and admission budgets
remain subject to normal continuation validation. CLI selection does not resolve
an assessment handoff or authorize a retry. Historical model-unavailability
records remain intact; a failure carrying a different known CLI version does not
establish that the model is unavailable under the newly selected CLI. A missing
version remains conservative. This mechanism neither probes model availability
nor changes the configured model or account.
