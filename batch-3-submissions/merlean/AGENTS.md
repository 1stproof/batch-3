# MerLean repository

## Release-preview policy

This checkout is the maintained private preview of the public MerLean repository.
Keep the public repository's root layout, English documentation, packaging conventions,
and privacy standard. Private visibility is not permission to commit private research,
personal paths, session records, credentials, caches, or unreviewed artifacts.

Routine authorized pushes target the private preview's `origin` only. A push to
`https://github.com/MerLeanProver/MerLean` requires an explicit user instruction naming
that public repository for the current release; a generic "push" does not authorize it.
The `public-upstream` remote is fetch-only by default, with its push URL disabled.
Do not re-enable it without that explicit instruction and the public release/privacy audit.
Push only the specified branch; never publish backup/research refs or use `--all` or `--mirror`.

This repository maintains four agents × two providers: **MerLean Lite**, **MerLean Heavy**,
**Paper-writing**, and **Referee**, each for Claude Code and Codex. Fresh unqualified MerLean research
defaults to Lite (target SILVER). Explicit `-heavy`, former lite-off, or requested full
formalization/proof completion selects Heavy (target GOLD). Paper writing preserves grades. Referee defaults to manuscript-scoped Lite verification;
the report itself has no research grade.

## Source of truth

- `workflows/merlean-lite.md`, `merlean-heavy.md`, `paper-writing.md`, `referee.md`: public entry templates.
- `workflows/common.md`: shared mode, trust, scope, persistence, and capacity policy.
- Other `workflows/*.md` and `roles/*.md`: internal procedures, not extra public agents.
- `ports/claude.md`, `ports/codex.md`: provider adaptations.
- `src/`: one maintained plan/grade/paper engine. Do not create provider runtime copies.
- `scripts/build_bundles.py`: generates eight self-contained packages in `plugins/` (included in public release commits).
  Never hand-edit generated packages; rebuild only receipt-verified unchanged outputs.
- `scripts/merlean`: plan CLI; `scripts/merlean-agent`: mode/entrypoint selector, not an LLM launcher.
- `scripts/paperctl`: deterministic paper operations; `scripts/setup.sh`: shared setup.
- `scripts/merlean-workspace`: opt-in external projects sharing pinned installed Lean
  dependencies; `docs/shared-workspaces.md` records supported layouts and limitations.

For actual research, read the selected entry, provider adapter, shared contract, and all
required internal references completely. Ordinary repository maintenance is not a request to
run autonomous mathematics. For explicit translation-only requests, Heavy uses its internal
statement translation workflow and does not prove or award a research grade.

## Preserved research invariants

Kernel cleanliness is necessary, not sufficient. Read `docs/trust-and-instantiation-gates.md`.
Gold requires the exact frozen theorem, closed public-premise/theorem-face census, intended
objects/adapters, definition independence, independent audits, and live Lean verification.
Every condition is a direct public antecedent propagated to consumers. Exact literature
boundaries additionally require hashed primary text and independent source/use-site audits,
plus the established cost-of-formalization decision. Conditional Gold is not an unconditional
answer. Lite cannot award Gold; neither a selected mode nor completed plan status earns a grade.

Main alone writes the plan graph. Workers own disjoint files and return patches/evidence.
Convergence defaults on in every mode, independently of `--exam`. A promising coherent
high-level skeleton focuses necessary gap repair and pauses nonessential competing
exploration before full proof review. Read `docs/research-convergence.md` and the shared
contract; concrete contrary evidence reopens targeted exploration. Preserve all grade and
original-scope gates, and all manuscript polishing, compression and readability checks.
Lite defaults to sustained candidate development, fresh first-gap review, and contextual
repair; representation scouting and uncertainty-first work are evidence-triggered fallback
tools. See `docs/lite-design.md`; preserve all final verification and grade gates.
Maintain failure-log.md and resume contracts; do not restart campaigns blindly. Checkpoints
are progress while an authorized goal remains open, subject to user interruption and limits.
GPT main, proof-design, paper/referee leads, optional campaign supervisor, and independent
substantive reviewers default to `gpt-6-astra`. Delegated execution subagents default to
`gpt-6.1-sol`, including bounded Lean implementation and compile-fix. Every problem main may
lead several such workers while retaining sole ownership of its plan. Main supplies the
mathematical context, formalization hints, file ownership, and acceptance checks from
`docs/astra-sol-handoff.md`; hints are advisory. Sol returns evidence for Astra review.
Dispatch independent review explicitly as Astra even when it uses a subagent tool; the
execution-worker default never overrides a required reviewer role. Preserve explicit model
choices and Anthropic model IDs.
The optional campaign controller alone writes its registry, state, and generated project table.
Problem agents and their workers may read the table and submit evidence in their own problem
directories; they must never edit controller records. Enforce this boundary in the host sandbox.
Retry explicit model-capacity failures every 10 seconds under common.md, without overriding
rate-limit handling or duplicating running jobs. No rule can revive a host that cannot resume.

## Maintenance and release

Run `python3 -m unittest discover -s tests`, `python3 scripts/audit_research_runtime_parity.py`,
and `python3 scripts/audit_codex_release.py` after changes. Existing Gold/source/receipt tests
must remain substantive. Use independent audits for changes to these trust boundaries.
Regenerate all eight packages and check their skills/manifests when public entrypoints change.
Never include credentials, Lean/Python caches, campaign state, or unrelated research in bundles.

Publish only with explicit user authorization and independent privacy/release audits.
The public tree must contain only the intended demo example, with no credentials,
private research/session records, or runtime caches. Review the outgoing Git ancestry
as well as the current files. Never publish private preservation branches or use a
mirror/all-branches push. Preserve user work locally before any sanitization.
Do not reinstall user-wide plugins without authorization.

## Maintained checkout delivery

Implement and deliver completed upgrades in this maintained checkout. Immutable source
exports are audit snapshots, not a substitute for updating the maintained source. Before
overwriting a path, preserve and reconcile existing local work; never reset unrelated
changes. Verify the maintained files match the delivered release and record the tested
source binding. Use ordinary `codex` authentication by default; do not silently select
a numbered account home or wrapper. Task-isolated configuration must bind the explicitly
selected login without importing unrelated session history.

Exam recovery must continue from the saved interruption point, preserving the original
clock, research/proof/plan/findings/reviews, and paper progress. Reconcile in-flight
completion and process ownership before dispatch; never turn a host restart into a
new campaign or repeat completed work. A fresh conversation after an empty initial
provider failure is an explicit, evidence-bound exception, never a fallback for
existing scientific progress.

Outer runtime supervision must be deterministic and consume no model tokens while
healthy. Invoke model diagnostics only for new actionable infrastructure failures,
with deduplication, bounded context, bounded execution, and no recursive quota
retries. Never use periodic LLM polling as a substitute for a process watchdog.
Report observed usage honestly; response-size validation is not a provider billing
or generation-token cap.
