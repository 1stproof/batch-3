# Codex adapter

Run the selected public agent in the main context. Resolve `<PLUGIN_ROOT>` from its
installed `skills/<name>/SKILL.md`: three parent directories from the file. Internal
workflow and role files never change this root. Do not infer it from the project cwd.

Use available Codex subagent tools for the internal roles in `roles/`; read the role
file before dispatch and pass its bounded contract to the worker. Do not invoke missing
public specialist skills. Obey host concurrency (normally three children in four total
slots); keep the plan graph single-writer. Each problem main may lead execution subagents.
GPT main, research/proof-design leads, paper/referee leads, and independent substantive
reviewers default to `gpt-6-astra`. Delegated execution subagents default to `gpt-6.1-sol`,
including bounded Lean implementation and compile-fix, after Astra supplies context,
formalization hints, owned files, and acceptance checks from `docs/astra-sol-handoff.md`.
Review roles must explicitly request Astra even when dispatched through the subagent API.
Sol may reject or replace Astra's suggested proof route, representation, tactics,
helpers, and proposed Lean spelling and continue autonomously within the task. The fixed boundaries
are the original goal/hypotheses, authorized file scope, established shared interfaces, and existing
verification gates; changing a shared interface requires coordinated plan work. Astra reviews the
result and revises the design when a real blocker remains. Keep any additional fresh independent
reviewer required by the selected workflow. A Sol execution assignment never changes a reviewer
model implicitly, and Claude provider models are unaffected.
No silent model fallback. Capacity recovery is in
`workflows/common.md`; it cannot restart an unavailable host main model.

Use the available Lean MCP tools; `lake build` and Heavy's runtime certificate audit
remain authoritative. The setup script creates a project `.mcp.json` descriptor, but
Codex may require registering that command with its own MCP configuration: do not claim
that a project JSON file automatically installs an MCP server. If no server is loaded,
use Lean CLI diagnostics or explain the required host configuration.

Read the paper protocol and use the same `paperctl` checks as Claude. Internal historical
tool labels such as Task, Read, or Grep mean the corresponding available Codex tools,
not permission to assume a nonexistent API.

## Required original-target reviewer

Codex original-problem scope review requires `gpt-6-astra`. This applies to both Lite and Heavy and overrides general reviewer defaults for this
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
