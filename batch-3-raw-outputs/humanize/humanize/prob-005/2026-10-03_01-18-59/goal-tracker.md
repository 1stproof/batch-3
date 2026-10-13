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

The problem: for a hyperfield $\mathbb{H}$ and $x,y,z\in\mathbb{H}$ with
$0\in x\boxplus y\boxplus z$, decide (and prove) whether
$0\in x^3\boxplus y^3\boxplus z^3\boxplus -xyz\boxplus -xyz\boxplus -xyz$.

## Acceptance Criteria

### Acceptance Criteria

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
<!-- Update each round with justification for all changes -->

### Plan Version: 2 (Updated: Round 1 review, by reviewer)

#### Plan Evolution Log
| Round | Change | Reason | Impact on AC |
|-------|--------|--------|--------------|
| 0 | Initial plan | - | - |
| 0 | Reduction strategy formalized: theorem reduced to a precisely isolated Exchange Lemma; free case completed only modulo that lemma | Substitution/tableau arguments insufficient; finite enumeration (137 403 instances, 0 failures) used as support | AC-1 partially; rejected by R0 review |
| 0 | Round-0 review demanded: replace exchange-lemma/descent block with an axiom-level proof (Option A) or downgrade to a conditional theorem with the open core stated (Option B); delete enumeration, the false |G|∈{1,3} claim, and errata B3.2–B3.3 | AC-1 negative test triggered verbatim; AC-3 numerical-evidence failure | Set the R1 mainline |
| 1 | Option A attempted via six calculi (saturated S1-closure; decorated towers; value-swap; cancellation-with-negated-block; witness families 82.6% coverage; quotient-by-cubes) — none closed; Option B implemented: conditional theorem + precisely stated Elevation Problem; enumeration/false-claim/proof-by-citation fully excised; errata fixed; doc now 5 pages, compiles clean | Per R0 review binding instructions | AC-2, AC-3, AC-4, AC-5 restored for what is in the document; AC-1 remains unmet (free case open) |
| 1R | Reviewer verification of R1: Option-B implementation is faithful and all surviving proofs audit clean (lem:basic, atoms A1–A3, prop:degen, lem:collapse/cor:collapse, lem:scale, lem:towers, lem:prop, conditional thm:main). Verdict NOT COMPLETE: AC-1 immutable and unmet. Two over-statements corrected: (i) the "reviewer's chain is dead" claim is true only at single-witness level — existential closure remains open; (ii) residual delete-list words ("enumeration", "exchange") still appear in meta-sentences. Independent reviewer experiments confirmed the tempting cube-injection sublemmas are FALSE (K_7: cube of a pairsum value need not lie in a^3⊞b^3; K_13: ab·(a⊞b) ⊄ a^3⊞b^3) — Option A is genuinely hard | Adjudicate Option-B acceptance bar; keep Option A open with explicit untried routes | Downgrade is provisional; R2 must attack the ordered routes below or record their rigorous refutations |
| 2 | Round-2 routes M1(1)–(4) executed and settled. CRITICAL correction discovered: the Elevation Problem had been stated with threefold hypersums a^{⊞3}⊞b^{⊞3}, which is strictly STRONGER than needed (scalar invariance only transports element cubes) and FALSE already in fields (2279 of 7899 premise-pairs fail); re-stated as the element-cube form 0∈a³⊞b³⊞(−1)⊞(ab)^{⊞3}, which is exactly equivalent to the original free case and verified true on every computed model (7899 premise-pairs, 0 fails; original theorem 271 139 relations + 618 867 small-hyperfield instances, 0 fails). Routes resolved: (1) 1⊞1-saturation REFUTED (1∈1⊞1 fails in 30/55 models; derived sublemma fails even when 1∈1⊞1); (2) permutation-tower COLLAPSES to null pairs {t,−t}, no new relation; (3) H4-collapse REFUTED (F₅: c=2,d=4,s=1,t=3); Delta-condition REFUTED; (4) quantifier CORRECTED — existential F3-witness (g,m) always exists but single-witness swap-step 0∈g⊞(−1)⊞(ab)^{⊞3} fails ~24%, so swap route does not close (E). Zero-trap phenomenon isolated: in F19/{±1} the completing zero is realized only at self-inverse unpaired elements (0∈x⊞x, −x∉x⊞x, x=−x); no substitution proof can exhibit it. All four routes settled, none closes (E) from (H1)–(H4); Option B retained | Review §M1 binding order 1→2→3→4; also repair inherited hypersum-vs-cube flaw | AC-1 still unmet (free case open, but now correctly stated and every Itemized review route refuted/collapsed/corrected); AC-2, AC-3, AC-4, AC-5 maintained |
| 2R | Reviewer (r2) verdict: STALLED again — all four routes correctly settled and every numeric claim independently re-verified (element-cube (E) 0 fails on 925 premise pairs p≤43; hypersum form fails in fields; F₅ H4-collapse counterexample 9 tuples; swap fails on positive fraction; F19/{±1} axiom-clean + zero-trap tight; original theorem 9441 relations 0 fails). But refuting dead routes is groundwork, not proof progress: AC-1 still unmet, Elevation Problem open. Round 3 must produce a PROVED positive partial statement (ordered: (1) prove (E) in the no-self-inverse case −1∉U via forced paired realization; (2) else prove a single-step elevation lemma licensing the special-value replacement −w∈P; (3) else classify the self-inverse obstruction family and prove the theorem on its complement) | Refutations alone don't discharge AC-1; pivot from route-autopsy to proving a sub-theorem | Round-3 mainline defined; AC-1 remains the sole open gate |
| CB | Circuit breaker (Stop hook) after 2R: 3rd consecutive STALLED; state mainline_stall_count=3, drift_status=replan_required, "this loop should not continue automatically". Root cause of the repeated stall: the free case is a genuinely hard open subproblem and three rounds faithfully executed review-directed *route-clearing* (removing dead ends) without generating one new *proved* lemma that shrinks the open case — necessary groundwork, not proof progress. Worker re-read plan.md: AC-1 immutable; its Implementation Notes expressly prefer an honest obstruction to an invented theorem. Reviewer's round-3 ordered mainline (recorded above in 2R) is the recovered objective for any future loop. WORKER DECISION: did not start a fresh RLCR loop — that is an operator decision and the worker policy forbids re-running setup or editing loop state; further proof attempts this turn would fabricate an already-escalated STALLED verdict instead of honestly surfacing the impasse. Worker applies only the reviewer's own two non-blocking cosmetics (Q4 notation unify; delete the two unproved counts 30/55 and the ~24% phrase), commits, and exits for operator / fresh-loop decision. | Circuit-breaker hook fired; operator must choose fresh loop (with the 2R recovered objective) or manual takeover | AC-1 remains the sole bottleneck; plan unchanged; worker obeys "do not continue this loop automatically" |

#### Active Tasks
| Task | Target AC | Status | Tag | Owner | Capability | Notes |
|------|-----------|--------|-----|-------|------------|-------|
| [mainline] R3: prove a positive partial theorem shrinking the open free case, per round-2-review ordered plan: (1) prove element-cube (E) in the no-self-inverse case (−1∉U ⇒ every nonzero x has x≠−x) by forcing a paired realization of 0∈a³⊞b³⊞(−1)⊞(ab)^{⊞3}; (2) else prove a single-step elevation lemma licensing the special-value replacement −w∈P in lem:towers(i); (3) else classify the self-inverse/zero-trap family and prove the theorem on its complement | AC-1 | active | coding | claude | N/A | Set by round-2 review (2R). Prior round's four refuted routes are DONE and recorded; do not re-refute. A proved sub-theorem is required for the verdict to leave STALLED; another set of route autopsies without a proved positive step reads as STALLED. If any route closes element-cube (E) in general, restore full unconditional proof (Option A). Element-cube (E) is verified true on 925 premise pairs / 9441 relations by reviewer (p≤43) and 7899/271 139 by worker (p≤127): answer is very likely "yes" |

#### Blocking Side Issues
| Issue | Discovered Round | Blocking AC | Resolution Path |
|-------|-----------------|-------------|-----------------|
| Elevation Problem (element-cube form) unproved: Theorem 2.1 of solution.tex holds only conditionally, so AC-1's negative test ("leaves a substantive case or lemma unproved") still triggers | 0 (reformulated R1; element-cube restatement R2) | AC-1 | R2 exhausted review §M1 routes 1–4 (all refuted/collapsed/corrected, verified by R2 reviewer). R3: follow the round-2-review ordered plan — prove (E) in the no-self-inverse case, or a single-step elevation lemma licensing −w∈P, or classify the zero-trap family and prove the theorem on its complement. Option B may be finalized only after R3 either proves a positive partial theorem or classifies the full obstruction family |

#### Queued Side Issues
| Issue | Discovered Round | Why Not Blocking | Revisit Trigger |
|-------|-----------------|------------------|-----------------|
| bitlesson-selector binary not present in environment | 0 | Informational; bitlesson.md read manually instead | If binary appears in later rounds |
| R0 git history contains the enumeration-based draft | 0 | Superseded; no action | n/a |
| Notation/typo: `prob:elevation` writes the *element-cube* (E) but `thm:main`'s conditional conclusion writes the same relation as `X^{\bp3}bp Y^{\bp3}...` (with ⊞3 superscripts) even though it means element cubes; cosmetic lacuna, no logical content — unify the superscript convention if a further editing round touches the text | 2 | Purely editorial; flags a mismatch the reader may trip over; no proof step depends on it | Next pass over solution.tex |

#### Completed and Verified
<!-- Only move tasks here after reviewer verification -->
| AC | Task | Completed Round | Verified Round | Evidence |
|----|------|-----------------|----------------|----------|
| AC-2, AC-3, AC-5 | R1: strip enumeration/external/false-cube-subgroup content; fix errata B3.2 (lem:basic(iv)) and B3.3 (prop:degen typo); keep document within 16 pages, article class, standard packages | 1 | 1R | pdflatex × 2 exit 0, 5 pages, no undefined refs; PDF text audit by reviewer: no Massouros/Baker–Bowler/154/618 867/137 403/99.6%/"verified"; proofs in §§1–3 audit line-by-line clean against (H1)–(H4) |
| AC-4 | R1: honest demarcation — conditional theorem stated conditionally, Elevation Problem explicitly open, no "yes" asserted, conjecture labelled as judgement | 1 | 1R | Abstract + Remark 4.3 + Remark 5.1 audits |

| AC-1 (routes) | R2: executed review §M1 routes (1)–(4) on the Elevation Problem and settled each: (1) 1⊞1-saturation REFUTED; (2) permutation-tower collapses to null pairs; (3) H4-collapse and Delta-condition REFUTED (F₅ counterexample); (4) value-swap quantifier corrected (existential witness exists, swap-step fails ~24%). Also corrected the Elevation Problem statement from the false threefold-hypersum form to the element-cube form exactly equivalent to the original theorem, verified universally (7899 premise-pairs, 271 139 relations, 618 867 small-hyperfield instances, 0 failures) | 2 | 2 (reviewer r2) | solution.tex rem:honest(e), rem:zerotrap, prob:elevation; round-2-summary.md; R2 reviewer independently re-verified every numeric claim (element-cube 0 fails; hypersum form fails in fields F_5; F5 H4-collapse counterexample 9 instances; swap ~5-19% by convention; F19/{+-1} axioms clean + zero-trap example tight) |
| AC-3 (hygiene) | R2: removed residual delete-list strings "enumeration"/"exchange" (and "descent"); tidied the redundant "conversely" sentence; kept field-identity + model-count data labelled as evidence/motivation, not proof steps | 2 | 2 | grep on solution.tex finds none of enumeration/exchange/descent/Massouros/Baker/Bowler/137/618 867; pdflatex 2 passes clean, 6 pages |

#### Explicitly Deferred
<!-- Items here require strong justification -->
| Task | Original AC | Deferred Since | Justification | When to Reconsider |
|------|-------------|----------------|---------------|-------------------|
| (none) — the Elevation Problem is NOT deferred; it is the active mainline task for R2 | — | — | Review protocol: current-scope work may not be parked as "deferred" while untried routes exist | — |
