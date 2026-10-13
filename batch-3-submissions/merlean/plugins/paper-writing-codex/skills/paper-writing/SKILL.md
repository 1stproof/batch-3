---
name: paper-writing
description: Compose, refine, resume, or read-only audit a mathematics paper with preserved theorem statements, source-checked citations, and versioned LaTeX. Does not prove new mathematical gaps or promote research grades.
---

Provider: `codex`. Resolve `<PLUGIN_ROOT>` as this installed file's third parent (`skills/<name>/SKILL.md` → package root). Read the following two files completely before acting: `<PLUGIN_ROOT>/ports/codex.md` and `<PLUGIN_ROOT>/workflows/common.md`. Internal references inherit that root.


# Paper-writing

Apply default convergence from `workflows/common.md` to the supported manuscript.
Keep all polishing, compression, readability, reader cycles and final audits;
convergence never licenses skipping these steps or expanding into unrelated research.

For exam/benchmark writing, select the `exam` profile and read
`workflows/paper/exam-mode.md`; it removes novelty and human literature waits while preserving full
polishing, compression, readability and release checks. Both providers use the same profile.

Read `workflows/common.md` and the provider adapter supplied by the installed entrypoint.
Read `workflows/paper-compose.md` for compose/refine/resume/next-version; read
`workflows/paper-audit.md` for audit-only requests. They share `scripts/paperctl` and the
eight-stage, preservation, reference, and refinement checks under `workflows/paper/`.
Claude composition additionally reads `workflows/paper-claude-protocol.md` for its retained
presentation guidance; shared preservation/source gates apply to both providers.

An audit stays read-only; compilation uses isolated temporary output. Refinement never
overwrites its baseline. Keep its coverage, locked main results, source registry, version
and hash checks. Main and GPT auditors default to Astra under the shared dispatch policy;
Claude keeps its configured provider model. Record independent auditor identity without
silently rewriting historical audit records.

Relevant-literature search, content reading, and citation selection are mandatory writing
work, even when novelty assessment is off. Reuse hash-verified sources and search records
before downloading again; select important citations by their actual relevance, without a
minimum or maximum count. Follow `workflows/paper/references.md` for the separate search/read
and input-credit gates. Literature handling defaults to no human authorization or download requests. Use available
permitted retrieval autonomously; omit unavailable optional citations and record limits under
`workflows/paper/references.md`. Novelty assessment defaults off (`assess_novelty: false`, `NOT_REQUESTED`); skip novelty
searches in exam mode. Enabled but inconclusive assessment can finish as `NOT_ASSESSED` without priority
claims and with the required independent audit. Never hide proof dependencies or known credit.

Writing does not certify research: retain the exact recorded grade in evidence sidecars,
and explicit mathematical conditions and unresolved questions in the paper. Read
`workflows/paper/reader-facing-paper.md` for external-reader prose, contextual TikZ figures,
proof bridges, claim-specific citations and useful length; apply it throughout writing and review.
If new mathematical gaps appear, record them and route to Heavy
only when authorized. Do not market a conditional theorem as an unconditional solution.

Read `workflows/paper/mathematical-writing.md` before planning. Assess actual evidence,
including Lite natural-language proofs and incomplete Lean; a critical path is auxiliary,
not a completeness certificate or a reason to discard unformalized mathematics. Preserve a
faithful `paper-raw.tex` and its evidence/status record before editing a separate version.
The raw checkpoint is not the approved-paper baseline or the pre-compression snapshot.

Near the end of composition or refinement, run two sequential fresh-context Astra
single-TeX reading/revision cycles, with different readers, then verify the
second revision. Preserve real feedback and dispositions; justified no-op revisions are
allowed. See `workflows/paper/reader-proof-quality.md` and
`workflows/paper/two-round-review-runtime.md`. Unresolved substantive issues block release.
The final output `.tex` is each fresh reader's sole scientific document input. Supply only
the neutral exposition/attribution rubric as instructions, not author maps,
Lean, source manuscripts, reference archives, or previous verdicts. Source-aware fidelity
and citation audits remain separate; their approval cannot substitute for this reading.
This improves paper generation without adding a new correctness or formalization campaign.


When a Lite pilot supplies `paper-source-handoff.json`, use its immutable submitted
Markdown revision as the authored source, not a mutable working `proof.md` or a log.
Check its original, proof and candidate hashes against the independently accepted
controller artifact. Keep that exact Markdown in the evidence registry while preparing
a distinct `paper-raw.tex`; the existing raw fidelity audit must check the mathematical
translation and retain conditions and unresolved gaps. The handoff does not replace
`freeze-raw`, independent paper review, or any release gate.
