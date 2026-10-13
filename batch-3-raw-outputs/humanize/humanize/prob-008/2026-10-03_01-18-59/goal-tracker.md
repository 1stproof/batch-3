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
| 0 | Proof strategy updated from "construct Liouvillian u with L_X u = 1 forcing X = 0" to "GH => Greenfield-Wallach torus action => equicontinuous => zero entropy" | The X = 0/Liouville route covers only the (6.1) suspension case; GH is also satisfied by Diophantine linear flows on tori (no periodic orbit, dense orbits), which must be covered; the compact torus action route handles all GH cases uniformly | AC-1, AC-4 now covered for all cases, not only the suspension case |

#### Active Tasks
<!-- Mainline tasks only: each task must directly advance the current round objective and carry routing + capability metadata -->
| Task | Target AC | Status | Tag | Owner | Capability | Notes |
|------|-----------|--------|-----|-------|------------|-------|

### Blocking Side Issues
<!-- Only issues that directly block current mainline progress belong here -->
| Issue | Discovered Round | Blocking AC | Resolution Path |
|-------|-----------------|-------------|-----------------|

### Queued Side Issues
<!-- Non-blocking issues stay queued and must NOT replace the round objective -->
| Issue | Discovered Round | Why Not Blocking | Revisit Trigger |
|-------|-----------------|------------------|-----------------|

### Completed and Verified
<!-- Only move tasks here after Codex verification -->
| AC | Task | Completed Round | Verified Round | Evidence |
|----|------|-----------------|----------------|----------|
| AC-1, AC-2, AC-4 | Final proof: GH => (Greenfield-Wallach structure theorem) flow is a Diophantine one-parameter subgroup of a smooth compact torus action => isometric/equicontinuous => h_top = 0 | 0 | 0 | solution.tex Sections 2-4; Lemmas 2.2 and 3.2 proved in full and audited line-by-line by reviewer; Theorem 2.1 (Greenfield-Wallach, AJM 94 (1972) 428-430) precisely stated and cited; used only for its topological consequence (compact torus action extending the flow) |
| AC-5 | Compile solution.tex with pdflatex and verify AC-5 constraints (<=16 pages, standard packages, no external files) | 0 | 0 | Reviewer re-ran `pdflatex -interaction=nonstopmode -halt-on-error solution.tex` twice: clean compile, no errors, no undefined refs, 4 pages; standard packages only (amsmath/amssymb/amsthm/mathtools/geometry/enumitem/hyperref) |
| AC-3 | Self-audit proof line by line (quantifiers, logical direction, edge cases X = 0, Diophantine vs Liouville, entropy conventions) | 0 | 0 | Reviewer re-audited: X = 0 not GH (Remark (a)); Diophantine vs Liouville divisor argument correct (Remark (b)); zeros/periodic orbits/hyperbolic pieces excluded (Remark (c)); entropy convention $h_{\mathrm{top}}(g_t) = |t| h_{\mathrm{top}}(g_1)$ handled (Remark rem:conventions); quantifier direction GH => structure => isometry => zero entropy verified non-circular |

### Explicitly Deferred
<!-- Items here require strong justification -->
| Task | Original AC | Deferred Since | Justification | When to Reconsider |
|------|-------------|----------------|---------------|-------------------|
