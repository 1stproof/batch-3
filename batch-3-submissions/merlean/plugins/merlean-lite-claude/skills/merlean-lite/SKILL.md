---
name: merlean-lite
description: >-
  Default MerLean research agent. Use for bare MerLean, -lite, or informal mathematical
  research without an explicit full-formalization request. Develop and audit natural-language
  proofs, probe claims, and certify only the weakest links in Lean. Target SILVER, with
  honest BRONZE when evidence is incomplete; never award GOLD or automatically start Heavy.
---

Provider: `claude`. Resolve `<PLUGIN_ROOT>` as this installed file's third parent (`skills/<name>/SKILL.md` → package root). Read the following two files completely before acting: `<PLUGIN_ROOT>/ports/claude.md` and `<PLUGIN_ROOT>/workflows/common.md`. Internal references inherit that root.


# MerLean Lite

Read `<PLUGIN_ROOT>/ports/claude.md` and `<PLUGIN_ROOT>/workflows/common.md`
before campaign work, using the provider and plugin root supplied by the installed entrypoint.
These provide the shared runtime, authority, persistence, and trust requirements.

## Select the mode before doing mathematics

Bare `MerLean` and `MerLean -lite` select Lite. `-heavy`, `lite off`, and an explicit
request for full Lean formalization, completion of Lean proofs, or GOLD select Heavy.
An existing proof, paper, or Lean file supplied merely as context does not change modes.
Treat `-lite` and `-heavy` as mutually exclusive selectors: a request containing both
needs resolution before mode-dependent work; do not silently prefer one. An explicit
Lite request to audit or screen a supplied proof remains Lite. Preserve an explicitly
requested continuation's campaign mode; do not infer a new Heavy campaign from old artifacts.

If the request selects Heavy, use the public MerLean Heavy entrypoint instead of starting
Lite. Do not claim to switch the active model or install another plugin through prose.
If Heavy is unavailable, report that routing limitation honestly. Specialist workers and
internal workflow files are implementation details, not additional public agents.

## Execute Lite

Apply default all-mode convergence from `workflows/common.md` as soon as a promising
proof skeleton appears. It is independent of exam scheduling and preserves every
mathematical, scope and certificate gate.

For an explicitly requested `--exam` run, read `<PLUGIN_ROOT>/docs/exam-mode.md`.
Use its shared whole-exam clock and actual automatic paper workflow; the metadata-only
agent selector does not start a timer. Preserve the original problem and every proof,
scope and selected-grade gate. Hour 23 changes the work phase, not the truth status
of an unfinished result. Readability, compression and manuscript audits remain required.

Read and follow `<PLUGIN_ROOT>/workflows/lite-research.md` in full. Read its referenced
internal workflows and roles when their instructions are needed. Its dossier, frozen
target and goal contracts, step ledger, independent review, applicable numerical checks,
targeted Lean triage, and final composition audit remain mandatory. Default to developing
one promising candidate, then preserve its progress while repairing the first substantive
objection from a fresh reviewer. Use uncertainty analysis, alternative representations,
and route scouts when an observed obstruction calls for them; an up-front route portfolio
is optional. See `docs/lite-design.md` for the policy and its evidence boundary. A supplied
proof is candidate mathematical evidence to inspect and audit; it is not a trust root.
Preserve the no-setup path, failure log, resumable memory, and single-writer plan store.

Develop the natural-language argument before selecting local Lean work. Record a reason
for each row's L3 decision; 0–3 selected rows is typical, not a target or maximum. Checked
routine facts, exact exhaustive calculations and audited cited results do not automatically
need Lean. Keep research gaps separate from missing certificates. Independently justified
retriage preserves old decisions, evidence and all substantive gaps; encoding cost may leave
an honest BRONZE result. Repeated auxiliary repair while the novel crux stays open triggers
route reconsideration before more certificate work. Focused fresh reviews guide intermediate
repair; final closure still requires a comprehensive independent review of the whole proof.
Faithfully bind intended objects in NL throughout. Hashed Lean adapters apply to selected
certificate interfaces and their SILVER certification; they do not mandate formalizing
all NL objects. Scope, premise and intended-meaning audits remain mandatory.

Lite targets SILVER: a closed ledger with every triaged inference Lean-certified and its
transitive premise manifest closed. This is an evidence threshold, not a promised label.
Report BRONZE when the existing workflow permits it, such as missing Lean infrastructure
or unresolved encoding work on triaged steps. An open mathematical residual cannot be
hidden by a grade. Report exact conditions, cited roots, intended-object limitations,
and the distinction between the checked implication and the research question.

Lite's ceiling is SILVER, even when a local certificate happens to be a complete theorem.
Do not emit GOLD, call the Gold recorder, or silently escalate to Heavy after SILVER.
Prepare the documented Heavy handoff (source hashes, theorem faces, contracts, ledger,
premise/interface census, goal alignment, adapters, and existing evidence) when useful.
Execute that handoff only when the user's request already authorizes Heavy; otherwise
finish with the achieved grade and the remaining obligations. Describe readiness for
Heavy as a handoff status, never as a fourth grade.

Before reporting the original question settled or presenting a complete answer, apply the
submitter-owned original-problem gate in `docs/trust-and-instantiation-gates.md` and obtain
two independent `roles/original-problem-reviewer.md` interface reviews by default. Freeze the original
source and answer criterion separately from the Lite ledger's chosen milestone. A SILVER
certificate for a special case is useful partial research, not evidence of full original
coverage. An unknown, failed, missing or stale gate leaves that completion claim blocked.

The original-target interface reviewer is mandatory Astra (`gpt-6-astra`) on GPT/Codex
and Fable (actual host-resolved ID) on Claude, independent of both submitter and all
implementers. Its absence blocks full original completion; no Sol/Opus downgrade is allowed.
See `roles/original-problem-reviewer.md` for the shared executable evidence handoff.

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
