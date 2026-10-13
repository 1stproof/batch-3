# Deterministic campaign coordination

`scripts/merlean-campaign` explicitly enables an optional outer controller; it is off during ordinary MerLean use. It is a local lifecycle API/CLI for a host coordinating independent problems. It does not launch models, automatically claim work, stop processes at a deadline, or complete a campaign by itself. Each problem main owns its own mathematical plan. An optional Astra supervisor may read compact status summaries and suggest bounded resource changes; it need not receive ten proof histories and cannot override frozen inputs or completion gates.

The host calls `init`, explicitly claims a problem before dispatch, and retains its claim token. A filesystem lock serializes cooperating CLI writers. Registration copies exact source bytes into separate `problems/ID/input.txt` directories and freezes their hashes, the global timezone-qualified deadline, and the concurrency limit. A state-pinned registry hash detects subsequent accidental changes. This is integrity bookkeeping, not protection against an adversary able to rewrite all local evidence.

```sh
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key init --problems /path/to/problems.json --deadline 2027-01-01T00:00:00Z --concurrency 2
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key claim q01 --owner host-session-1
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key release q01 --token CLAIM_TOKEN
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key finish q01 --partial partial.md
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key status
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key seal
```

`problems.json` is an object mapping unique problem IDs to input file paths, relative to that JSON file. The campaign directory must not already exist. Answer, manifest and partial paths are relative to that problem's directory. No automatic retry or fresh attempt is created by any command.

## Recovery and limits

A claim is persisted before the host launches work. Running and reconciliation-required claims both consume capacity. Normal `release` is the host's assertion that its job stopped. `release --interrupted` retains an unresolved claim. After a host crash, even a still-`running` claim requires explicit `reconcile ID --token TOKEN --evidence 'Host verified process exit and retained its artifacts.'` before reuse. The host must inspect the actual process/session first. Unknown launches never become free slots just because time passed. Tokens prevent stale hosts from releasing a newer claim.

The deadline rejects new claims. Already-running process cancellation and per-call deadlines remain the dispatch host's responsibility. The coordinator can record completed or partial artifacts after the deadline. It enforces claim concurrency, not real-time process count or token/dollar limits: a host that launches without claiming violates the contract. The host must keep actual usage accounting and distinguish provider rate limits from transient model capacity failures. This layer does not implement either retry policy.

These claims coordinate one logical attempt per registered problem. Continuing work after release preserves that problem's history; it does not reset an external budget. A new exam or attempt needs a new explicit campaign directory. Keep reference answers outside blind solving contexts until submissions are sealed.

## Completing and sealing

`finish ID --manifest manifest.json` requires all of:

- `audit_original_scope(manifest, base, required=True, require_final_answer=True)` passes. Use the original-scope schema for natural-language or Lean answers.
- The pinned original descriptor's source bytes match this problem's registered input hash.
- `final_answer: {path, sha256}` points to the current answer within this problem directory.
- `final_proof_review: {path, sha256}` pins a JSON review containing `verdict: "PASS_COMPLETE_PROOF"`, `gaps: []`, `final_answer_sha256`, a nonempty `reviewer`, and `implementers` exactly matching the manifest's full implementer census. The reviewer differs from every implementer and `manifest_author`.
- That proof review pins `reviewer_provenance: {path, sha256}` relative to the review file. The provenance contains the same reviewer, `role: "final_proof_review"`, nonempty real host-issued `task_id`, `model`, and `provider`, and the same `final_answer_sha256`.

The final proof reviewer uses the required model for the manifest's provider: Codex requires
`gpt-6-astra`, and provenance must name the matching provider. A different model or provider
cannot satisfy this gate merely by supplying nonempty provenance fields.

The host must supply genuine dispatch provenance and the complete implementer census. Structural validation cannot authenticate identities or prove that a model actually reviewed the mathematics. A scope pass alone does not establish proof correctness. The separate proof-review receipt records an independent judgment, not a Lean kernel certificate or automatic research grade. Existing grade gates still apply.

Use `finish ID --partial partial.md` to retain unfinished work without any completion claim. `seal` requires every problem to be complete or explicitly partial, rereads complete manifests and their current pinned evidence, and rechecks partial hashes. Sealed runs reject claims and lifecycle edits. A seal records this inspection; it does not make the filesystem physically immutable, and downstream consumers must revalidate current evidence before publication. No paper export is performed.

## Controller-owned project table

Initialization requires a new `--owner-key` path outside the entire campaign tree.
The controller creates a private random key file there and freezes its digest in the
registry. Every API or CLI mutation must present that key. A reopened API uses
`Campaign(root, owner_key=key_path)`. A read-only `status` needs no key and recomputes
observations against current evidence without rewriting the table or state.
Keep the key path and file private to the dispatch host. Never put them in worker
prompts, worker directories, bundles, or logs.

This API ownership check prevents accidental or unauthorized cooperating writers.
A filesystem lock serializes those writers. Neither the key nor file permissions can
stop arbitrary code running with the same OS identity from reading host files or
rewriting the registry and state. For enforced exclusivity, the host must expose the
campaign registry, state and table read-only to workers, keep the key inaccessible,
and grant workers write access only to their own problem directories using a sandbox,
mount boundary, or separate OS identity. Do not describe chmod alone as isolation.

`state.json` is the authoritative project table, with a derived problem count, rows,
validation timestamp, observations, and `successful_complete`. `project-table.md` is
its generated readable view. Only controller mutations regenerate that file. It is
a timestamped snapshot, not a certificate; use `status` or authenticated `refresh`
to inspect current evidence. Problem mains continue to own their own mathematical
plans and submit evidence files, never table status flags.

The frozen initialization settings are `--mode lite` (default) or `--mode heavy`,
`--require-paper` (default false), and optional positive `--max-pages`. Explicit
host adapters can select these flags for their own submission policy.

```sh
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key observe q01 --manifest manifest.json --paper-state paper/workflow-state.json
scripts/merlean-campaign /path/to/new-run --owner-key /private/controller.key refresh
scripts/merlean-campaign /path/to/new-run status
```

`observe` pins a research manifest and optional paper state within the problem's
own directory. Re-observe after intentionally updating evidence; stale hashes never
silently authorize a new result. `finish --manifest` also registers that manifest.
There are no setters for solved, Silver, Gold, or paper-complete booleans.

The columns are independent:

- **Original solved:** the existing frozen-original scope and independent final proof
  review gates pass for the finished current answer. A local grade does not set it.
- **Silver review:** `review_recorded` means a current, independent, hash-bound review
  of the Lite ledger, certificates and trust roots was recorded. This is an explicit
  review attestation, not a deterministic mathematical or kernel certificate.
  A bare Silver label in plan metadata is insufficient.
- **Gold:** Heavy can show `verified` only through the existing live kernel and
  semantic grade audit. Lite shows `not_applicable`. Local or conditional Gold retains
  its scope and does not imply the original problem was solved.
- **Paper:** `complete` requires the full existing paper release audit, including its
  compile, reader and preservation checks, and binding to the current final answer.
  Optional page limits are checked against the compiled output.

Each observation includes its current validation details. Changes to registered
files invalidate their observation; failures after an accepted observation become
`stale`. A fresh failing review shows `failed`; missing evidence remains `pending`.
Refresh rechecks evidence instead of trusting saved green statuses.

## Host feedback and same-attempt repair

The controller retains durable feedback tickets for unmet required gates, including rejected
`finish` and `seal` checks. Authenticated `refresh` synchronizes tickets with current evidence.
The read-only API `feedback(ident=None)` and CLI `feedback [problem]` expose these packets;
reading them does not deliver work or launch models. The generated table shows open-ticket
and pending-delivery counts. The host must refresh and drain this
feedback after validation failures and relevant artifact changes, then deliver each actionable
packet to the owning problem main through its existing task context.

```sh
scripts/merlean-campaign /path/to/run --owner-key /private/controller.key refresh
scripts/merlean-campaign /path/to/run feedback q01
scripts/merlean-campaign /path/to/run --owner-key /private/controller.key acknowledge q01 --ticket TICKET_ID --fingerprint DELIVERED_FINGERPRINT --task-id REAL_HOST_TASK_ID --receipt 'Delivered to the owning problem main.'
scripts/merlean-campaign /path/to/run --owner-key /private/controller.key reopen q01 --reason 'Continue repair of the recorded gate findings.'
```

`acknowledge(ident, ticket_id, fingerprint=..., task_id=..., receipt=...)` is an owner-only
delivery receipt, not resolution or proof of repair. Copy the fingerprint from the packet
actually delivered and record the real host task identity and delivery evidence. An outdated
fingerprint is rejected. Changed ticket content sets `needs_delivery` again; an earlier
acknowledgment cannot suppress delivery of the new version. Feedback includes historical
resolved tickets, so use current status and delivery needs when draining it.
The problem main routes findings under `workflows/common.md`: scope and proof defects return
to mathematical design; bounded implementation returns to an owned Sol task; paper defects
return to the paper lead, with mathematical gaps returned to the research main. The handoff
includes the exact affected evidence/version, remaining obligation, unresolved history,
advisory hints, file boundaries and acceptance checks. Designing main reviews worker returns;
required independent Astra reviewers then assess current repaired evidence. A delivery receipt,
successful compile, local grade or paper pass cannot substitute for another required gate.

For a stopped terminal result or recorded rejected submission that needs further work,
owner-only `reopen(ident, reason=...)`
returns it to `released` and records a repair round in the same logical attempt. Claim it
normally before launching work. Preserve frozen inputs, mode, deadline, budgets and history;
reopening does not start a fresh attempt. Never relaunch an active or uncertain job: inspect
the real host job and reconcile it first. Sealed campaigns and expired deadlines do not
permit relaunch through reopening. The host owns cancellation, capacity/rate-limit handling
and actual dispatch; this API neither dispatches models nor messages people.

After repair, obtain current independent scope/proof and selected-mode/paper evidence as
required, re-observe intentionally changed artifacts, repeat `finish`, and refresh the table.
Do not mark a ticket resolved merely because a worker reports success; current gate validation
must establish closure. `seal` rejects complete rows whose required gates do not all pass.
Explicit partial sealing remains available for honest unfinished outcomes at authorized limits;
it is not successful completion. Continue useful authorized repair while work and resources
remain, preserving partial progress when a genuine stopping condition applies.

Successful completion also requires grade/paper evidence to bind the same current
answer path and hash as the completed original manifest. An unrelated local result
can be displayed but cannot satisfy project completion.

Successful completion requires original solved plus the selected mode's grade
(Silver review for Lite, Gold for Heavy), and paper complete when required. A sealed
run may contain explicit partial results and then has `successful_complete: false`.
Sealing freezes lifecycle/evidence registration but authenticated refresh can still
record subsequent evidence invalidation. Owner-authorized delivery receipts may also be
recorded for post-seal findings, without reopening the run or changing its accepted evidence.
No grade or paper gate upgrades original
completion, and no original completion silently upgrades a grade.

## Optional subscription pilot host

The opt-in host adapter and explicit browsing switch are documented in
`docs/codex-pilot.md`. It connects Codex conversations to this controller for
bounded Lite pilots; it is not the final competition container or paper exporter.


## Portable host monitoring

The optional Codex pilot can enable the deterministic campaign watchdog with
`--watchdog`; it is disabled by default. The core in `src/campaign_watchdog.py`
requires controller authority and writes diagnostics outside the problem tree.
It never changes a grade, acknowledges feedback, signals a recorded PID or resets
a run. Host integration cancels only retained owned tasks and preserves partial
artifacts. For configurable intervals, forensic restart inspection, automatic
per-agent accounting and current recovery limits, see [Codex pilot](codex-pilot.md).
