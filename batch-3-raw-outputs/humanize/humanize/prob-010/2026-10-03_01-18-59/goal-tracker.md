# Goal Tracker

<!--
This file tracks the ultimate goal, acceptance criteria, and plan evolution.
It prevents goal drift by maintaining a persistent anchor across all rounds.

RULES:
- IMMUTABLE SECTION: Do not modify after initialization
- MUTABLE SECTION: Update each round, but document all changes
- Every task must be in one of: Active, Completed, or Deferred
- Deferred items require explicit justification
-->

## IMMUTABLE SECTION
<!-- Do not modify after initialization -->

### Ultimate Goal

Produce a rigorous, self-contained resolution of the exact mathematical
problem in `problem.tex`. Write the deliverable as a standalone compilable
LaTeX document in `solution.tex`, no longer than 16 typeset pages.

## Acceptance Criteria

### Acceptance Criteria
<!-- Each criterion must be independently verifiable -->
<!-- Claude must extract or define these in Round 0 -->


- AC-1: `solution.tex` answers every part of the exact question and proves
  every claimed implication, construction, bound, or counterexample.
  - Positive test: a specialist can verify the argument line by line.
  - Negative test: the document only sketches an approach or leaves a
    substantive case or lemma unproved.
- AC-2: The solution is self-contained relative to standard graduate-level
  mathematics and precisely states any external theorem it invokes.
  - Positive test: notation, hypotheses, edge cases, and theorem applications
    are explicit.
  - Negative test: undefined notation or an unstated nonstandard result carries
    the argument.
- AC-3: The proof is audited for logical direction, quantifiers, degeneracies,
  constants, and consistency with `problem.tex`.
  - Positive test: the delicate steps and all requested cases are checked.
  - Negative test: confidence language or numerical evidence substitutes for
    proof.
- AC-4: If the proposed assertion is false or ill-posed, the response gives a
  rigorous disproof or precise diagnosis and never presents conjecture as fact.
- AC-5: `solution.tex` begins with `\documentclass`, ends with
  `\end{document}`, uses only the installed standard LaTeX package set,
  contains no Markdown or workflow commentary, and fits within 16 typeset
  pages.

## Path Boundaries

---

## MUTABLE SECTION
<!-- Update each round with justification for changes -->

### Plan Version: 1 (Updated: Round 0)

#### Plan Evolution Log
<!-- Document any changes to the plan with justification -->
| Round | Change | Reason | Impact on AC |
|-------|--------|--------|--------------|
| 0 | Initial plan | - | - |
| 0 (review) | Fibre configuration II*+II*+4I_1 supersedes contract placeholder "I_18+I_1+I_1"; review added Round-1 repair task M-1..M-7 | The implemented root-lattice computation (E_8+E_8 fibre roots forces two II*, Euler number forces 4 I_1) is the correct GT mirror configuration for (H, H+E8+E8); review judgement | Keeps AC-1/AC-2 open until repairs land |
| 1 (review) | Round-1 repairs verified; review adds Round-2 repair task M-8..M-9 | Round-1 edits fixed M-1,M-3,M-4,M-5,M-6,M-7 and most of M-2, but introduced a U vs U(-1) form mismatch in the Def 5.1(4) model and three inconsistent rank statements (rank 16 vs rank 2 quotient; ker N rank 21 vs rk N 2) | Keeps AC-1/AC-2 open until repairs land |
| 2 (review) | Round-2 repairs verified; review adds no further mainline repair task | Round-2 edits fixed M-8 (rank-20 model E=N+Zf'+Zg with E/Zf = N+U(-1) proved by gram-matrix change of basis; Def 5.1(4) checks (iii)/(iv) computed on generators) and M-9 (rank numerology unified: rk E_m=18, rk E_m'=20, E_m'/E_m rank 2 U(-1), ker N rank 20), plus Q-2/Q-3; the worker's departure from the review's suggested model (f'.f=0 instead of f'.f=1) is correct and necessary for the orthogonal decomposition | AC-1/AC-2 now met at specialist line-by-line level |

#### Active Tasks
<!-- Mainline tasks only: each task must directly advance the current round objective and carry routing + capability metadata -->
| Task | Target AC | Status | Tag | Owner | Capability | Notes |
|------|-----------|--------|-----|-------|------------|-------|
| Round 2 repairs M-8..M-9 per round-1-review-result.md (fix E_m'/E_m quadratic form to U(-1) in the explicit rank-20 model; complete Def 5.1(4) checks (iii)-(iv); reconcile rank numerology 18/20/2 and ker N rank 20; Q-2/Q-3 cosmetics; recompile; commit) | AC-1, AC-2 | done | coding | claude | N/A | mainline; verified in round-2 review |
| Round 2 executed: M-8/M-9 repaired (rank-20 model E = N+Zf'+Zg, E/Zf = N+U(-1) shown by displayed gram-matrix change of basis; checks (iii)/(iv) computed on generators; ker N rank 20 and "rank 2 lattice U(-1)" audited unique) + Q-2 (garbled codimension clause rewritten) + Q-3 (E8 sign sentence); see round-2-summary.md | AC-1, AC-2 | done | coding | claude | N/A | commit 39c4fe2, 11 pages |
| Finalize: dead LaTeX definitions removed (definitionn env, cS, Gr, remark theoremstyle); output-equivalent cleanup, 11 pages unchanged | AC-5 | done | coding | claude | N/A | commit d35a62e |


### Blocking Side Issues
<!-- Only issues that directly block current mainline progress belong here -->
| Issue | Discovered Round | Blocking AC | Resolution Path |
|-------|-----------------|-------------|-----------------|

### Queued Side Issues
<!-- Non-blocking issues stay queued and must NOT replace the round objective -->
| Issue | Discovered Round | Why Not Blocking | Revisit Trigger |
|-------|-----------------|------------------|-----------------|
| Q-1: cosmetic grammar/typography items (Prop 4(b) "1-bounds are standard"; "H^{perp-ish}" informal; "$nef$" italic) | 0 (review) | Does not affect mathematics; fix opportunistically in Round 1 edit pass | Next edit of solution.tex |
| Q-2: Thm 4(d) model sentence "N of index $\infty$-codimension $1$" garbled | 1 (review) | One-line English fix | FIXED in round 2 (line 661 now "an overlattice of N of rank 20 ... corank-2 sublattice") |
| Q-3: E_8 sign convention in Lambda_K3 writing needs one clarifying sentence (Prop 1 proof) | 1 (review) | Convention mismatch only; one line | FIXED in round 2 (Section 1 notation block) |

### Completed and Verified
<!-- Only move tasks here after Codex verification -->
| AC | Task | Completed Round | Verified Round | Evidence |
|----|------|-----------------|----------------|----------|
| AC-5 | solution.tex compiles, 10 pages, allowed packages, no commentary | 0 | 0 | pdflatex clean; verified in round-0 review |
| AC-1, AC-2 | Full proof of the mirror-pair statement in solution.tex | 0 | 2 | Verified at commit 39c4fe2, 11 pages; Round-0 gaps M-1..M-7 verified in round-1 review, M-8..M-9 verified in round-2 review; all ACs met |
| AC-1, AC-2 | Round 1 repairs M-1..M-7 | 1 | 1 | Verified at commit d0ad78a, 11 pages; M-2 partial (see M-8) |
| AC-1, AC-2 | Round 2 repairs M-8..M-9 (+Q-2/Q-3) | 2 | 2 | Verified at commit 39c4fe2, 11 pages; grep audit of rank numerology consistent; E/Zf = N+U(-1) gram-matrix check correct |

### Explicitly Deferred
<!-- Items here require strong justification -->
| Task | Original AC | Deferred Since | Justification | When to Reconsider |
|------|-------------|----------------|---------------|-------------------|
