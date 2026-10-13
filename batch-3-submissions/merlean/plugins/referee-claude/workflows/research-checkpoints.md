# Optional offline research checkpoints

Read `common.md` and the selected Lite/Heavy workflow first. This procedure adds durable
bookkeeping to a research campaign; it is not a new public agent, proof verifier, scheduler,
or replacement for the step ledger, failure log, plan graph, or research-grade auditor.
Main is the sole writer of both the plan and checkpoint sidecar. Workers return artifacts
and findings for main to inspect and record.

## When to use it

Use this procedure only with an explicitly offline plan (`PLAN_OFFLINE=1`). Existing online
campaigns retain their existing workflow; do not switch backends, copy their state, or create
an offline replacement automatically to obtain checkpoints. The sidecar commands do not
migrate a campaign. Flat-file Lite work can continue without them.

The research question may generate conjectures, competing routes, counterexamples and
revised obligations. Freeze each version while proving or reviewing it. A proposed revision
records its reason and effect on consumers; it does not silently change the plan, authorize
new assumptions, or inherit the earlier version's acceptance. Apply the existing scope and
pivot gates before deliberately updating an obligation. Preserve the prior evidence and
record how the revised result serves the research question.

## Record and inspect

Use `<PLUGIN_ROOT>/scripts/merlean` with the campaign's existing offline data directory:

```text
PLAN_OFFLINE=1 <PLUGIN_ROOT>/scripts/merlean --data PATH research-snapshot SID
PLAN_OFFLINE=1 <PLUGIN_ROOT>/scripts/merlean --data PATH research-checkpoint SID --evidence-root ROOT --json PAYLOAD
PLAN_OFFLINE=1 <PLUGIN_ROOT>/scripts/merlean --data PATH research-checkpoints --sid SID --evidence-root ROOT
PLAN_OFFLINE=1 <PLUGIN_ROOT>/scripts/merlean --data PATH research-propose-revision SID --evidence-root ROOT --json PAYLOAD
PLAN_OFFLINE=1 <PLUGIN_ROOT>/scripts/merlean --data PATH research-ready --root ROOT_ID --mode interface --evidence-root ROOT
PLAN_OFFLINE=1 <PLUGIN_ROOT>/scripts/merlean --data PATH research-ready --root ROOT_ID --mode evidence --evidence-root ROOT
```

`research-checkpoints` may omit `--sid` to inspect all recorded obligations.
`research-ready` accepts repeated `--root ROOT_ID` selections. Supply the research-relevant
roots explicitly rather than treating every historical lemma as a current priority.

A checkpoint payload has `expected_fingerprint`, `outcome`, `evidence` (a list of
`{"path": "relative/path", "sha256": "actual file digest"}`), `note`, and `next_action`.
Obtain the expected fingerprint from a fresh snapshot; compute hashes from the actual
artifacts under the chosen evidence root. Retain enough evidence to explain the finding,
including the precise statement and assumptions, source or ledger, and relevant check/review
output. Never substitute a summary saying a check passed for its available actual artifact.

Allowed outcomes are `progress`, `interface_checkpoint`, `evidence_checkpoint`,
`proof_failure`, `counterexample_candidate`, `interface_mismatch`, `verification_failure`,
`integration_failure`, `infrastructure_failure`, and `budget_exhausted`.
An outcome records the finding main is reporting. It is not an independent verdict on the
content of an artifact. `evidence_checkpoint` does not mean kernel acceptance or scientific
novelty; `counterexample_candidate` does not establish a disproof.

### Version 2 bindings and evidence access

The sidecar schema is version 2. Its evidence-consuming operations bind one canonical
absolute evidence root; subsequent calls must use that same resolved root. Evidence paths
are relative to it. The implementation opens evidence through descriptor-relative,
no-follow traversal and accepts regular files; it fails closed if the required access
primitives are unavailable. This constrains evidence reads, not what the evidence proves.
The JSON sidecar is an operational record, not a tamper-proof or authenticated trust store.
Do not manually rewrite its records or present their hashes as an independent audit.

A snapshot fingerprints the declared plan semantics and declared dependency closure.
It does not parse implicit Lean imports or hash source bytes, libraries, toolchains, or
an entire actual Lean dependency cone. Missing formal dependencies and cycles invalidate
the snapshot. Those checks complement rather than replace the existing source/kernel gates.

To record `evidence_checkpoint`, every direct declared dependency must have a current
`evidence_checkpoint`. The record binds those specific earlier checkpoint IDs. If the
obligation declares `lean_path`, explicitly include that relative path and its actual hash
in this checkpoint's evidence list, along with any relevant review/check artifacts. A plan
path alone is not source evidence. Dependency binding is recursive: changing an artifact of
a bound child invalidates that child checkpoint and dependent checkpoints, even if the
plan's semantic fingerprint is unchanged. Recording a fresh child does not automatically
rebind an old parent's checkpoint; inspect and record the parent again when justified.
Every outcome requires a nonempty evidence list. `note` and `next_action` are optional in the
checkpoint schema, but main should supply them for useful research memory. Revision proposal
fields are all required.

A revision proposal payload has `expected_fingerprint`, `checkpoint_id`, `change`, `reason`,
and `consumer_impact`. Refer to the checkpoint motivating the proposal. Explain whether the
change is a strategy revision, corrected statement, restricted model, additional premise,
or different conclusion, and identify affected consumers. A proposal is a record for review,
not a plan mutation. A new target or assumption needs the same explicit scope decision as
before these commands existed.

## Readiness is advisory

Use `interface` mode when considering speculative proof work: each direct dependency
needs an explicit nonempty plan `anchor`; an informal description or file path alone does
not satisfy that interface check. The command does not elaborate the anchor. Use `evidence` mode when considering work requiring current dependency evidence.
Inspect the command's findings and exclusions. A declared missing/cyclic dependency or a
failed/axiomatic dependency blocks readiness; completed nodes are not offered as new work. Neither mode dispatches an agent or grants
permission to use an unproved claim as a theorem. Existing Heavy signature-locked parallelism
still permits downstream glue before dependency proofs are complete, followed by the full
closure checks. Lite still applies its weakest-link triage before firing Lean.

A matching fingerprint and artifact hash show current identity, not truth. Recheck currentness
on resume and before reuse. Changed claims, dependencies or artifacts can invalidate reuse;
do not repair freshness by merely replacing stored hashes. Review the changed evidence and
record a new appropriate checkpoint. Reusing a fact also requires its intended objects,
premises and interpretation to match the new consumer. Hashes cannot establish this match.
An accepted lemma may remain correct after its route is abandoned while no longer advancing
the current question. Readiness scoped to selected roots helps distinguish these cases.

## Respond to the actual failure

A proof failure calls for diagnosis, decomposition or a rival representation. An interface
mismatch calls for an explicit contract/consumer review. A counterexample candidate goes
through independent verification before a pivot. Verification failure does not become
acceptance because the source compiled previously. Integration failure can leave useful
proof artifacts intact: preserve them while repairing integration, then revalidate the
combined result. Infrastructure failures use the existing classified recovery policy in
`common.md`; a checkpoint outcome neither starts retries nor overrides rate-limit handling.

Token and time budgets are resource constraints, not the research objective. Record
`budget_exhausted` honestly and preserve a resumable state; do not manufacture completion or
a grade. Scientific progress may be a falsified conjecture, a resolved model ambiguity, a
verified literature subtraction, or a useful new bound. Output volume and lemma count alone
do not measure it. Keep novelty and paper coherence in the research ledger and reviews.

The commands add no automatic retries, worker dispatch, worktree manager, global token
accounting, or proof execution. If isolation is useful, use the existing workflow's explicit
workspace/file-ownership discipline; this sidecar does not create isolated workspaces.
No checkpoint or proposal promotes a plan status, SILVER, or GOLD. All existing grading,
intended-model, premise, target and completion gates remain mandatory.
