# Claude Code adapter

Run the selected public agent in the main context. `<PLUGIN_ROOT>` is
`${CLAUDE_PLUGIN_ROOT}` when provided by Claude Code, otherwise the directory three
parents above the installed `skills/<name>/SKILL.md`. Internal references do not reset it.

Read `roles/<role>.md` and dispatch its bounded instructions using available Claude Code
Task/subagent tools. Background workers own disjoint files; the main agent alone writes
the plan store. The old named specialist agents are internal roles, not extra public
agents. Use the available concurrency, never more than four children, and retain the
signature-locked scheduling and independent audits.

Preserve the user's configured Claude model. GPT research calls, when explicitly
available, default to `gpt-6-astra`; do not replace Anthropic model identifiers with GPT
identifiers. Read `workflows/common.md` for capacity recovery and authority limits.

For project setup use `scripts/setup.sh --project <LIB_DIR>`; reload the host to pick up
a newly created project `.mcp.json`. If Lean MCP is unavailable, use `lake build` and Lean
CLI diagnostics. `<PLUGIN_ROOT>/scripts/merlean` works in both online and explicit
`PLAN_OFFLINE=1` modes, with optional `MERLEAN_RUNTIME` for a writable external venv.

Paper-writing uses the same deterministic `paperctl` preservation/refinement checks as
Codex. Its historical Claude eight-step presentation protocol is retained as an internal
reference; it does not replace the shared reference, baseline, and completion gates.

## Required original-target reviewer

Claude original-problem scope review requires Fable using the actual host-resolved model ID. This applies to both Lite and Heavy and overrides general reviewer defaults for this
gate. The reviewer is independent of the submitter/orchestrator and every implementer;
a compile-fix worker cannot approve its own result. Record the actual dispatch in the
hash-bound `reviewer_provenance` specified by `roles/original-problem-reviewer.md`.
If the required model is unavailable, keep full original completion/submission blocked;
do not silently substitute Sol, Opus, or another family. No universal Fable ID is assumed.

## Final original-question review independence

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

## Selective Lite verification execution

Apply the concrete uncertainty, intended-object, noncircular-premise and feasibility/value
selection in `workflows/lite-research.md`. An already approved unchanged local module
may perform a bounded source/compile/implementation-repair cycle using its original
cumulative worker/probe limits and complete retained evidence. Prospective host workers
request this with `compile_pending`, exact row/source, `implementation_complete` and
`next_step`; no uncertainty-reduction claim is required before a diagnostic. Revalidate
task, claim, premises, scope, candidate and approval before every execution. Changed
boundaries, material adverse findings or exhausted bounds require existing reassessment.
Terminal historical returns are not reopened by this protocol. Provider-driven hosts
apply the same boundaries with their actual tools; do not claim automatic scheduler
support where absent. Clean compilation still needs independent semantic acceptance,
full-proof and two fresh original-scope reviews, and every existing Silver/Gold gate.

## Optional Lite NL capability

An explicit `-NL` / `--nl` selects Lite with Lean disabled; standalone `-NL` and
`-lite -NL` are equivalent. Read `docs/nl-mode.md` before setup or dispatch. Persist
and inherit the capability; never silently change a resumed campaign. Keep the same
NL discovery, plan ownership, independent review, original-scope and Silver gates.
Do not dispatch formalization, Lean MCP, lean/lake/elan, compiler inventory or Lean
workers/probes. Keep required unresolved certificates and findings; do not auto-deselect,
downgrade grades or claim Gold. Paper work inherits this restriction and preserves
history. Use the shared guarded setup/CLI; native arbitrary shell enforcement is
instruction-bound, not an OS-level prohibition.
