# Offline research checkpoints

MerLean supports optional artifact-bound bookkeeping for an existing offline plan. It helps
main remember which version of an obligation was investigated, what files support the
reported outcome, and which selected research roots still depend on that work. It does not
turn evolving mathematical research into an endlessly retried fixed theorem.

This addition is available in the release preview. Its presence does not imply a public
release, user-wide plugin installation, or permission to ship research data. Research
directories belong to separate user projects and must not be included in the preview.

## Commands

All commands below require explicit offline operation. Replace `PATH` with the existing
plan-data directory, `ROOT` with the directory containing the evidence, and `SID` with an
existing statement ID. In installed use, resolve `scripts/merlean` through the plugin root.

```text
PLAN_OFFLINE=1 scripts/merlean --data PATH research-snapshot SID
PLAN_OFFLINE=1 scripts/merlean --data PATH research-checkpoint SID --evidence-root ROOT --json PAYLOAD
PLAN_OFFLINE=1 scripts/merlean --data PATH research-checkpoints [--sid SID] --evidence-root ROOT
PLAN_OFFLINE=1 scripts/merlean --data PATH research-propose-revision SID --evidence-root ROOT --json PAYLOAD
PLAN_OFFLINE=1 scripts/merlean --data PATH research-ready --root ROOT_ID --mode interface --evidence-root ROOT
PLAN_OFFLINE=1 scripts/merlean --data PATH research-ready --root ROOT_ID --mode evidence --evidence-root ROOT
```

Square brackets denote an optional argument, not literal shell syntax. Repeat `--root` to
select multiple current research roots. These operations are additive sidecar bookkeeping;
there is no automatic online-to-offline migration. An online campaign or a bare Lite ledger
can continue using its established workflow without these commands.

The checkpoint payload is a JSON object:

```json
{
  "expected_fingerprint": "COPY_FROM_CURRENT_RESEARCH_SNAPSHOT",
  "outcome": "interface_checkpoint",
  "evidence": [{"path": "evidence/interface.txt", "sha256": "COMPUTE_FROM_ACTUAL_FILE"}],
  "note": "State exactly which interface was checked and what remains open.",
  "next_action": "Develop the bounded consumer against this frozen interface."
}
```

The capitalized values are placeholders, not valid evidence. Use actual hashes and the
snapshot's actual fingerprint. Quote JSON safely when passing it to a shell; do not include
credentials. A revision proposal instead uses `expected_fingerprint`, `checkpoint_id`,
`change`, `reason`, and `consumer_impact`. The last field explains consequences for existing
claims and consumers, not just which file needs an edit. A proposal does not apply itself.

## Schema version 2 and freshness

Evidence-consuming commands bind a canonical absolute evidence root to the sidecar. Later
calls must supply that same resolved root. Paths in evidence are relative; reads traverse
from the root with descriptor-relative no-follow access and require regular files. The
implementation fails closed on platforms lacking the required filesystem primitives.
These protections do not make the sidecar tamper-proof, authenticate its author, or verify
an artifact's assertions. It remains local operational bookkeeping.

The snapshot covers **declared plan semantics and declared dependencies**, not implicit Lean
imports or file bytes. In particular it is not a replacement for the real imported-source
closure, Lean toolchain binding, or kernel check. A source edit can leave a plan fingerprint
unchanged; the separately recorded evidence hash is what detects that artifact change.

An `evidence_checkpoint` requires a current evidence checkpoint for each direct declared
dependency and binds the selected earlier checkpoint IDs. When `lean_path` is declared,
that file must be explicitly listed in evidence with its actual hash. The source path must
fit the same relative in-root evidence rules. Invalid child artifacts propagate staleness
through the checkpoint bindings. A newly recorded child does not repair an old parent by
substitution: the parent still refers to the old child checkpoint and needs a reviewed new
record if that binding is no longer current.

Every checkpoint outcome requires nonempty evidence. Checkpoint `note` and `next_action`
are optional schema fields but recommended. All five revision-proposal fields are required.
Interface readiness checks an explicit nonempty `anchor` on each direct dependency; it does
not elaborate the signature. Evidence readiness concerns current dependency checkpoint
records, not proof truth. Declared missing/cyclic and failed/axiomatic dependencies block
readiness; already completed nodes are not offered as new work.

## Interpretation and limits

Outcomes are `progress`, `interface_checkpoint`, `evidence_checkpoint`, `proof_failure`,
`counterexample_candidate`, `interface_mismatch`, `verification_failure`,
`integration_failure`, `infrastructure_failure`, and `budget_exhausted`.
They are main's recorded classifications, not new verification grades. Current artifact
hashes establish that the same evidence is available; they do not prove its assertions.

Interface readiness supports the existing practice of developing glue against frozen
signatures before all proofs finish. Evidence readiness addresses work requiring current
dependency evidence. Both are advisory, scoped to the roots selected by main. Neither
starts work, proves a claim, or closes the dependency cone. The research and grade audits
remain authoritative. A checkpoint cannot award SILVER/GOLD, mark a theorem complete,
settle a conjecture, or certify that a cited result is new or applicable.

Keep the research question and versioned obligations distinct. False conjectures and failed
representations can prompt new versions through the existing scope/pivot gates. Do not
silently weaken an old statement or carry its acceptance into a new one. Preserve useful
facts with their assumptions and evidence even when their original route is retired;
scientific relevance must be reconsidered for the new consumer. Integration repair should
retain accepted proof artifacts while the combined result is rechecked, rather than
restarting mathematical discovery without cause.

A budget limit is a reason to preserve an honest checkpoint, not a reason to claim success.
Scientific progress includes negative evidence, improved understanding of the model, and
verified novelty subtraction. More tokens, more workers, or more accepted lemmas need not
produce a more coherent or significant paper.

No automatic worker dispatcher, retry policy, global token meter, worktree isolation, or
proof runner is introduced. Workspace isolation remains the responsibility of the existing
research workflow. Main alone writes plan and sidecar state; workers report bounded findings.
See [the internal procedure](../workflows/research-checkpoints.md) and
[the trust gates](trust-and-instantiation-gates.md).

## Small local demonstration

From the engine checkout, run:

```bash
python3 scripts/demo_research_checkpoints.py
```

The demonstration uses a temporary synthetic three-node dependency graph. It makes no model
calls, runs no Lean proof, and awards no verification grade. It checks the distinction
between interface and evidence readiness, then changes a bound child source artifact and
checks that the child's evidence, dependent checkpoint bindings and linked revision proposal
become stale. It also checks that plan statuses and grades remain unchanged. A passing demo
validates these bookkeeping behaviors; it is not a demonstration of a proved mathematical
result or improved research performance. It does not operate on your research campaign.

## Sustained inference and later operational events

More inference can materially help large research: explore distinct representations in
parallel, continue promising proof repairs, independently attack counterexamples, and check
literature where it affects the claim. The actionable host-agent protocol is
[research-effort.md](../workflows/research-effort.md). This checkpoint addition supplies
memory for that work, not the compute policy itself or an autonomous executor. It neither
starts model calls nor measures a fleet-wide token budget. Continue an unfinished authorized
goal across checkpoints while respecting the user's limits and actual host capacity.

For dependency reuse, select the latest applicable `evidence_checkpoint`, not simply the
latest event of any outcome. A later progress, integration-failure or budget event does not
silently erase still-current evidence. Artifact and dependency changes can still invalidate
it. Operational history remains visible: main must inspect unresolved proof/verification
objections before relying on an artifact, even when its bytes are current. These outcome
labels are not an authenticated proof revocation or acceptance mechanism.

## Inspiration and implementation boundary

The design discussion inspected Humanize2 commit
[`3e0e6edf1d47ae27a70c1a334ee6cf364d05f59b`](https://github.com/humanfia/humanize2/tree/3e0e6edf1d47ae27a70c1a334ee6cf364d05f59b)
and Flowverse commit
[`1dd53c4437e62934ed053bf28fbcdfd0ffa6bbcd`](https://github.com/humanfia/flowverse/tree/1dd53c4437e62934ed053bf28fbcdfd0ffa6bbcd).
Useful ideas include durable proof checkpoints and separating mathematical repair from
integration repair. MerLean's implementation is original and additive; it does not import
those runtimes or adopt their indefinite proof loops. Existing MerLean route diversity,
step ledgers, independent counterexample checks and grading contracts remain in force.
