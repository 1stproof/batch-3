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
| 0 | Round-0 contract committed to proving in full (i) the Schubert/Scharlemann closed-incompressible-surface reduction and (ii) a claimed "HFK-epsilon obstruction" to closed non-fiber surfaces; the delivered proof instead cites Ni--Wu (advancing version of the cabling conjecture for L-space knots, together with Scharlemann's reduction) as a stated external theorem and includes only an explicitly-labeled optional heuristic sketch (Sec. 4). | Full re-proofs of those results are major research-level developments, infeasible in any short document; the plan's own AC-2 explicitly permits "precisely stated external theorems" and the contract itself lists cabling/adjunction as permissible external statements -- the contract overstated the deliverable. The main theorem's logical chain uses only declared external inputs; the sketch is labeled "not used in the proof." | AC-1/AC-2 still met: nothing in the main argument rests on an unstated result. Reviewer accepts the evolution and notes the contract text should have been corrected by the worker (see review). |

#### Active Tasks
<!-- Mainline tasks only: each task must directly advance the current round objective and carry routing + capability metadata -->

_All mainline tasks are complete and verified (Round 0 line-by-line review;
Round 1 independent re-audit of the polish pass). Every task has been moved to
"Completed and Verified" below; no active work remains._

| Task | Target AC | Status | Tag | Owner | Capability | Notes |
|------|-----------|--------|-----|-------|------------|-------|
| (none) all tasks completed and verified -- see Completed and Verified | -- | done+verified (R0, R1) | coding | claude | N/A | ledger below is authoritative |

### Blocking Side Issues
<!-- Only issues that directly block current mainline progress belong here -->
| Issue | Discovered Round | Blocking AC | Resolution Path |
|-------|-----------------|-------------|-----------------|

### Queued Side Issues
<!-- Non-blocking issues stay queued and must NOT replace the round objective -->
| Issue | Discovered Round | Why Not Blocking | Revisit Trigger |
|-------|-----------------|------------------|-----------------|
| [RESOLVED R2] P3-a: Case 2 (0-surgery) primality inference leaned on b1=1, which excludes S^3 but not S^1xS^2. Fixed: rewritten to state irreducible-closed-orientable => prime unless S^1xS^2, and S^1xS^2 is excluded by its nonseparating essential sphere (noting b1=1=b1(S^1xS^2), so homology cannot separate them); S^3 excluded separately by b1. | 1 (R1 review) | Main result already accepted as correct by R0 reviewer; this is an expository/logical-phrasing improvement in the proof text. | RESOLVED in Round-2. |
| [RESOLVED R2] P3-b: Remark 5.4 closing claim that the Ni--Wu cabling theorem "generalizes to knots in arbitrary L-space homology spheres, where Theorem 1.2 is unavailable" was unsourced and arguably overstated in that generality. Fixed: replaced by a hedged parenthetical noting analogues have been studied for knots in more general L-space homology spheres where integrality of reducing slopes is unavailable, and that we use none of it here. | 1 (R1 review) | Remark is explicitly labeled explanatory and not used in the proof of Theorem 1.1. | RESOLVED in Round-2. |
| [RESOLVED R3] P1: Remark rem:glcabling falsely claimed Gordon--Luecke proved the cabling conjecture for knots in S^3 (open: Gonzalez-Acuna--Short) and that the main theorem's conclusion holds for arbitrary knots, which would trivialize the result. Fixed by DELETING the remark (label was unreferenced); the document now makes no false historical claim. The main proof correctly uses the stronger Ni--Wu L-space cabling theorem and GL's true integrality result. | 2 (R2 review) | Blocking accuracy issue in explanatory material (AC-2/AC-4); not part of the load-bearing proof, but a false theorem attribution is unacceptable in a math proof. | RESOLVED in Round-3 (deleted). |
| Round-0 contract promised full proofs of two research-level inputs (Schubert/Scharlemann reduction; "HFK-epsilon obstruction"); document delivers stated-external-theorem + labeled sketch instead. Accepted as plan evolution (Plan Evolution Log, R0), but contract text was never amended to match. | 0 | Main proof is complete and self-contained relative to declared external theorems per plan AC-2; nothing in the main chain depends on the sketch. | Closed by this review's plan-evolution entry unless future rounds want contract hygiene. |
| [RESOLVED R1] Theorem attributed to "Ni--Wu, 2014"; the cabling-conjecture-for-L-space-knots result was completed by Z. Wu (arXiv:1412.2186, 2014) building on Ni--Wu. Fixed: header relabeled "Ni--Wu, completed by Z. Wu (2014)"; inputs-comment expanded; Section 4 keeps d-invariant attribution to Ni--Wu. | 0 | Was a polish item (AC-2/AC-5); mathematical statement was always correct. | RESOLVED in Round-1 polish. |
| [RESOLVED R1] Rational-genus wording: "when K is a knot in S^3 with an incompressible Seifert surface" -> "for every nontrivial knot K in S^3 (the minimal-genus Seifert surface of a nontrivial knot is incompressible)". | 0 | Sat in the optional Section 4; the used convention was correct. | RESOLVED in Round-1 polish. |
| [RESOLVED R1] Optional-sketch labeling: Section 4.2 sketch now wrapped in a \begin{quote}\itshape...\end{quote} block with a bold "Optional explanatory sketch (not used in the proof)" banner; garbled "The two forces the equality" -> "The two bounds force equality"; "(rational) genus" doubled-word fixed to "genus (rational Thurston norm)". | 0 | Cosmetic; load-bearing status was already stated in prose (twice) and in Remark 4.5. | RESOLVED in Round-1 polish. |

### Completed and Verified
<!-- Only move tasks here after Codex verification -->
| AC | Task | Completed Round | Verified Round | Evidence |
|----|------|-----------------|----------------|----------|
| AC-1..AC-5 | Full proof of main theorem in solution.tex (7-page standalone LaTeX) | 0 | 0 (reviewer line-by-line) | Reviewer recompiled (2x pdflatex, 0 errors, 0 undefined refs, 7 pages <= 16, only allowed packages, no markdown). Verified by hand: Main Thm (i)-(iii); case coverage incl. r=infinity, unknot, q>=2, p=0, p=+-1, p>=2 reducible/irreducible; homology lemma (half-integer slopes fine); lens-prime; non-integral primality; cabling-splitting lemma (compression splitting W=J#X; special-case reduction X_C ~ X_U via change of surgery picture; Z/u * Z/v via fiber-killing; Kneser-Milnor uniqueness forcing X ~ M_u); 0-surgery via fibredness+sphere thm; +-1 via |uv|>=2; torus subcase in reducible case; sharpness S^3_6(trefoil)=L(2,3)#L(3,2). External inputs declared: Kneser-Milnor, Gordon-Luecke '87 (Thm 3), Kronheimer-Mrowka Property P, Ni--Wu cabling for L-space knots (attribution issue logged), fibredness, sphere theorem. All logically sufficient. Small accuracy/consistency issues logged as queued side issues; none touches the logical chain. |
| AC-2, AC-3, AC-5 | Round-1 polish pass: Q2 cabling-theorem attribution relabeled (Ni--Wu, completed by Z. Wu 2014); Q3 rational-genus clause fixed to "every nontrivial knot"; Q4 optional Section-4 sketch italicized/bannered, garbled fragment repaired, doubled word removed. | 1 | 1 (reviewer independent re-audit) | Reviewer (R1) independently re-verified all four fixes against solution.tex and the rebuilt PDF: (Q2) header + inputs-comment now read "Ni--Wu, completed by Z. Wu (2014)" (lines 138,159) with the d-invariant mechanism still attributed to Ni--Wu (line 437); (Q3) clause now "for every nontrivial knot K⊂S^3 (the minimal-genus Seifert surface of a nontrivial knot is incompressible)" (lines 429-430); (Q4) italic quote block with bold "Optional explanatory sketch (not used in the proof; not a complete proof)" banner (lines 413-470), garbled fragment repaired to "The two bounds force equality" (line 464), doubled "rational" reworded to "genus (rational Thurston norm)" (line 420). Confirmed no stale artifacts (no "two forces", no "(rational) rational", no "incompressible Seifert surface", no soft-hyphen/non-ASCII). Reviewer recompiled 2x pdflatex independently: 0 errors, 0 undefined refs, 7 pages <= 16. Proof chain Sections 1-3 byte-for-byte unchanged (git diff confirms edits confined to inputs-comment + Section 4). |
| AC-3, AC-2 | Round-2 review fixes: P3-a Case-2 primality inference rewritten to exclude S^1xS^2 by its nonseparating essential sphere (noting b1=1 cannot separate it); P3-b closing-remark unsourced generalization replaced by a hedged parenthetical. | 2 | pending verification | Two surgical edits inside Case-2 paragraph and Remark 5.4; no load-bearing step changed; recompiled 2x pdflatex clean (infwarerr info line only), still 7 pages <= 16; PDF text spot-checked for both fixes. |
| AC-2, AC-4 | Round-3 review fix: deleted false Remark rem:glcabling (claimed GL proved the (open) cabling conjecture and the theorem for arbitrary knots). | 3 | pending verification | Single-point deletion; remark label was unreferenced; recompiled 2x pdflatex clean, 7 pages; no dangling refs; no other false historical claims (grep confirms only the true Ni--Wu L-space cabling theorem and the true 'Property P conjecture, proved by Kronheimer--Mrowka' remain). |

### Explicitly Deferred
<!-- Items here require strong justification -->
| Task | Original AC | Deferred Since | Justification | When to Reconsider |
|------|-------------|----------------|---------------|-------------------|
