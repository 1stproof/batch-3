# Code Review Findings

You are in the **Review Phase**. Codex has performed a code review and found issues that need to be addressed.

## Required Re-anchor

Before touching code:
- Re-read the original plan at @plan.md
- Re-read the goal tracker at @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
- Refresh the current round contract at @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/round-2-contract.md

The round contract must preserve a single mainline objective. Code review findings do NOT automatically become the new round objective.
If the original plan contains `## Feature Map / Capability Map`, the refreshed contract must also preserve or update the current Capability Anchor intentionally.

## Review Results

## Codex Review Issues

- [P3] Curious wording in Case 2: it is not $S^3$ (indeed $b_1=1$) — /work/first-proof-humanize-tdgou2bu/005-prob-006/solution.tex:340-341
  In Case 2 (0-surgery), the aside `It is not $S^3$ (indeed $b_1=1$)` is odd, since of course $b_1(S^3)=0$ makes the claim true but the parenthetical is the trivial direction; more importantly the immediately following inference `hence it is prime` requires excluding the other irreducible-but-not-prime possibility $S^1\times S^2$. The proof actually disposed of this in the preceding sentence ($\pi_2=0$ plus the sphere theorem gives irreducibility, and an irreducible manifold with $b_1=1$... wait — an irreducible closed orientable non-prime manifold is exactly $S^1\times S^2$, which has $\pi_2=0$ too, so irreducibility alone does not exclude it; it is excluded only by noting $S^3_0(K)$ has no $S^2$ summand... precisely: irreducibility of $S^3_0(K)$ already means every embedded $S^2$ bounds a ball, whereas $S^1\times S^2$ contains the non-separating essential sphere $\{pt\}\times S^2$, so the cited homology remark is doing no work and the logical chain is slightly muddled). This is expository rather than fatal — the irreducibility established two lines earlier already implies primality once $S^1\times S^2$ is excluded, and $b_1=1$ does exclude $S^3$ but not $S^1\times S^2$ — but the sentence as written suggests $b_1=1$ settles primality, which it does not. Consider replacing with: `It is not $S^1\times S^2$ (that manifold contains a nonseparating sphere, contradicting irreducibility) and not $S^3$ (since $b_1=1$), hence it is prime.`

- [P3] Unsourced claim that Theorem 1.4 generalizes where Theorem 1.2 is unavailable — /work/first-proof-humanize-tdgou2bu/005-prob-006/solution.tex:500-503
  The closing sentence of Remark 5.4 asserts that Theorem 1.4 (Ni--Wu cabling theorem) `is the statement that generalizes to knots in arbitrary $L$-space homology spheres, where Theorem 1.2 [Gordon--Luecke integrality] is unavailable.` This is asserted without citation and is delicate: the Ni--Wu argument uses the mapping-cone formula for knot Floer complexes, whose analogues in general $L$-space homology spheres require extra hypotheses (e.g. the knot must be rationally null-homologous / the surgery must be an integer with respect to the right basis, and integrality of reducing slopes is exactly what fails in general), so as stated the remark is at least unsubstantiated and arguably inaccurate in this generality. Since this remark is explicitly labeled explanatory and is not used in the proof of Theorem 1.1, it does not affect correctness of the main result, but a standalone-solution reader would benefit from either a citation or a hedged formulation (e.g. `analogues of this statement have been pursued for knots in $L$-space homology spheres`), per the AGENTS.md requirement that solution.tex be a self-contained deliverable whose claims are supported.
solution.tex compiles cleanly to 7 pages, answers the problem.tex question (yes via Kneser--Milnor + Gordon--Luecke + Property P + Ni--Wu cabling theorem + cable-splitting computation), and the case analysis is complete and watertight. The only flagged items are two low-priority expository issues in explanatory, proof-irrelevant material: an oddly argued primality sentence in Case 2 and an unsourced generalization claim in the closing remark.

Full review comments:

- [P3] Curious wording in Case 2: it is not $S^3$ (indeed $b_1=1$) — /work/first-proof-humanize-tdgou2bu/005-prob-006/solution.tex:340-341
  In Case 2 (0-surgery), the aside `It is not $S^3$ (indeed $b_1=1$)` is odd, since of course $b_1(S^3)=0$ makes the claim true but the parenthetical is the trivial direction; more importantly the immediately following inference `hence it is prime` requires excluding the other irreducible-but-not-prime possibility $S^1\times S^2$. The proof actually disposed of this in the preceding sentence ($\pi_2=0$ plus the sphere theorem gives irreducibility, and an irreducible manifold with $b_1=1$... wait — an irreducible closed orientable non-prime manifold is exactly $S^1\times S^2$, which has $\pi_2=0$ too, so irreducibility alone does not exclude it; it is excluded only by noting $S^3_0(K)$ has no $S^2$ summand... precisely: irreducibility of $S^3_0(K)$ already means every embedded $S^2$ bounds a ball, whereas $S^1\times S^2$ contains the non-separating essential sphere $\{pt\}\times S^2$, so the cited homology remark is doing no work and the logical chain is slightly muddled). This is expository rather than fatal — the irreducibility established two lines earlier already implies primality once $S^1\times S^2$ is excluded, and $b_1=1$ does exclude $S^3$ but not $S^1\times S^2$ — but the sentence as written suggests $b_1=1$ settles primality, which it does not. Consider replacing with: `It is not $S^1\times S^2$ (that manifold contains a nonseparating sphere, contradicting irreducibility) and not $S^3$ (since $b_1=1$), hence it is prime.`

- [P3] Unsourced claim that Theorem 1.4 generalizes where Theorem 1.2 is unavailable — /work/first-proof-humanize-tdgou2bu/005-prob-006/solution.tex:500-503
  The closing sentence of Remark 5.4 asserts that Theorem 1.4 (Ni--Wu cabling theorem) `is the statement that generalizes to knots in arbitrary $L$-space homology spheres, where Theorem 1.2 [Gordon--Luecke integrality] is unavailable.` This is asserted without citation and is delicate: the Ni--Wu argument uses the mapping-cone formula for knot Floer complexes, whose analogues in general $L$-space homology spheres require extra hypotheses (e.g. the knot must be rationally null-homologous / the surgery must be an integer with respect to the right basis, and integrality of reducing slopes is exactly what fails in general), so as stated the remark is at least unsubstantiated and arguably inaccurate in this generality. Since this remark is explicitly labeled explanatory and is not used in the proof of Theorem 1.1, it does not affect correctness of the main result, but a standalone-solution reader would benefit from either a citation or a hedged formulation (e.g. `analogues of this statement have been pursued for knots in $L$-space homology spheres`), per the AGENTS.md requirement that solution.tex be a self-contained deliverable whose claims are supported.

## Issue Classification

Classify each review finding before acting on it:
- **blocking side issue**: prevents the current mainline objective from succeeding safely or prevents review acceptance
- **queued side issue**: valid follow-up, but does not block the current round objective

Queued issues may be documented, but they must NOT take over the round.

## Task Rules

Every task must use one lane tag:
- `[blocking]` for review findings that must be fixed now
- `[queued]` for non-blocking follow-up work

Do not create new `[mainline]` tasks in review phase unless the review proves the previous mainline objective was incomplete.

## Instructions

1. **Refresh the round contract** at `/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/round-2-contract.md`
2. **Address blocking issues first** and keep the mainline objective stable
3. **Keep fixes inside the Capability Anchor** unless the review proves the anchor was wrong
4. **Focus on fixes only** - do not add new features or make unrelated changes
5. **Commit your changes** after fixing the issues
6. **Write your summary** to: `/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/round-2-summary.md`

## Summary Template

Your summary should include:
- The mainline objective for this round
- Which blocking issues were fixed
- Which issues were reclassified as queued follow-up
- How each fixed issue was resolved
- Any issues that could not be resolved (with explanation)
- Confirmation that `goal-tracker.md` was updated if the blocking/queued issue lists changed
- A Goal Tracker Update Request only if tracker reconciliation still needs Codex help

## Important Notes

- The COMPLETE signal has no effect during the review phase
- You must address the code review findings to proceed
- After you commit and write your summary, Codex will perform another code review
- The loop continues until no `[P0-9]` issues are found

## BitLesson Selection (REQUIRED FOR EACH FIX TASK)

Before implementing each fix task, you MUST:

1. Read @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each fix task/sub-task to select relevant lesson IDs
3. Follow the selected lesson IDs (or `NONE`) during implementation

Reference: @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/bitlesson.md

## Task Tag Routing Reminder

Follow the plan's per-task routing tags strictly:
- `coding` task -> Claude executes directly
- `analyze` task -> execute via `/humanize:ask-codex`, then integrate the result
- Keep Goal Tracker Active Tasks columns `Tag` and `Owner` aligned with execution

## Capability Anchor Reminder

If the plan contains `## Feature Map / Capability Map`:
- The round contract must name the relevant Capability ID(s) or capability/feature name(s)
- Goal Tracker Active Tasks must keep their `Capability` column aligned with the round contract
- Mainline work must preserve the selected capability's business, design, and implementation context
- Do not let queued or future-scope capability work take over the current round
