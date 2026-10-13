# Research adaptation review — September 10, 2026

This historical feature review records research-oriented effort guidance and optional offline
checkpoint bookkeeping. It is intended for evolving mathematical research questions, not
only completion of fixed benchmark statements. Humanfia's Humanize2 and Flowverse are
acknowledged in NOTICE, README, and the feature documentation; their runtime is not vendored.

The comparison baseline was the public MerLean release
`4d9c24a72d988e57867d67cd825bd4b0299780c7`. Package and test counts below describe the
September 10 review, not the current release. Current packaging contains four agents for
two providers; run the documented checks against the version being released.

## What changed

- Shared Lite/Heavy guidance now describes sustained inference, diverse parallel attacks,
  substantive review/repair, useful reuse, and evidence-driven route changes. This protocol
  operates through the host agent; it is not a new autonomous scheduler or token meter.
- Five offline command families expose target snapshots, evidence-bound checkpoints,
  currentness inspection, explicit revision proposals, and root-scoped readiness.
- Checkpoints retain readable original target/dependency snapshots and declared local
  evidence hashes. Explicit dependency checkpoint IDs propagate stale evidence to consumers.
- Revision proposals preserve their motivating observation but never edit the target.
  Operational failure records do not silently erase still-current mathematical artifacts.
- Descriptor-relative evidence access rejects path escapes and symlink substitution. The
  journal binds its canonical evidence root and uses the existing plan transaction lock.
- All six generated packages contain the shared runtime, workflow changes, and attribution.
  Actual CLI behavior is tested in Lite/Heavy on both Codex and Claude.

## Trust boundary

The existing grade engine, grade policy, offline plan-store implementation, Lite/Heavy entry
templates, and trust-gate document remain byte-identical to the baseline. Checkpoint identity
does not establish proof validity, scientific relevance, novelty, or a verification grade.
The snapshot covers declared plan dependencies; unlisted Lean imports are not discovered by
this utility. Include all consumed evidence and retain the existing complete-cone audits.
The sidecar is cooperative research memory, not an authenticated same-user security boundary.

## Validation

- Full suite: **194 tests, 193 passed, one skipped**. The optional live Mathlib regression
  requires `MERLEAN_LEAN_TEST_PROJECT` pointing to a built project, which was not configured.
- The 16 new targeted tests cover semantic and artifact staleness, retained historical
  statements, evidence escapes, wrong roots, malformed history, concurrent CLI writes,
  explicit backend selection, root scope, axiomatic dependencies, proposal isolation,
  integration-failure preservation, and all four research packages.
- Shared runtime parity and standalone six-archive audits pass. Three Codex manifests and
  six skill definitions validate.
- `python3 scripts/demo_research_checkpoints.py` passes using a disposable three-node
  synthetic campaign. It checks readiness changes, preserved proposals, stale dependency
  propagation, and unchanged theorem status/grade. It makes no model calls or proof claims.
- Separate Lean 4.28.0 smoke checks accept `0 + n = n` with no axioms and reject an attempted
  proof of `False` using `True.intro`. This is a compiler smoke test, not full Gold validation.
- Independent Astra reviews cover research suitability, core trust boundaries, adversarial
  evidence reads, and generated-package compatibility. Symlink-race and dependency-currentness
  findings from interim reviews were repaired before acceptance.

Research data and runtime caches are not part of this feature distribution. The release
preview contains the sanitized demonstration and synthetic regression fixtures only.
