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
| 0 | Answer determined: YES. The birhizome collapses to dimension
  one: every valuative monoid is {0} or N (lex cones impossible),
  valuative points are halfspace functionals; atomicity reduces
  birhizomicity-at to a value-group equality; all covers refine to
  folds + CFA pieces; equiface probes give ungrown kernels on key
  overlaps. | Proven lemmas; kills the junk-cocycle
  counterexample strategy (pinned to zero by identity transitions) |
  AC-1, AC-4 |
| 1 | Round-1 (post-review): the theorem is proved for finitely
  generated P, with the general case explicitly described as
  obstructed (f.p. of P->P/K; infinite face poset) | R0 review B-1
  required deleting the silent global f.g. redefinition; within the
  session the STAR comparison route could not be closed | AC-1, AC-3
  (scope now honest); AC-4 logs that the general case remains open
  with a precise diagnosis |
| 1 | Round-1 review: loose deferred check list (old Q-1) replaced
  by the structured SPINE (Steps 0-4) for the Section-4 vanishing
  argument; B-7/B-8/B-9 added; B-2 ratified as sound in its
  stronger written form (sharpness essential; valid even for H_1
  non-archimedean) | The R1 audit found the vanishing argument
  needs one genuinely new support step (generic filter lemma by
  DEPTH) rather than residual checks; lem:sieve/lem:sandwich must
  be re-derived from it in Round 2 | AC-1 (line-by-line
  verifiability of the endgame) |
| 2 | Round-2 (post-review): Section 4 partly rewritten per SPINE
  Steps 0-1 (nerve-complex subsection with (0a)-(0e), filter
  lemma, sieve re-derived, anchor deleted, d-lemma, K-slice
  theorem added); HOWEVER the vanishing argument (prop:vanish
  Steps 1-3) could NOT be honestly closed: repeated attempts hit
  the same obstruction — the unit F->R pi_* pi^{-1} F splits
  (kernel/cokernel = R pi_* M, M = complement-extended part), so
  for idempotent F the claim forces R^{>0} pi_* M = 0, which is
  NOT proved and appears FALSE on the full birhizomic site unless
  pi^{-1}F is a B-sheaf (trivial on A\B); that sheaf property is
  EXACTLY the open point, not a derived consequence | Earnest
  repair attempts at the derived-fiber level all reduce to A=A
  instead of forcing the sheaf/triviality of M's fibers | AC-1,
  AC-3 (Section 4 endgame genuinely open/work-in-progress);
  AC-4 (if the theorem is FALSE as stated, a disproof is needed;
  currently UNRESOLVED) |
| 3 | Round-3 (post-review): review REJECTED the worker's
  "likely false / counterexample" verdict as an analysis of the
  WRONG map (pi^{-1} = Lan+sheafification lands in sheaves;
  thm:descent already gives pi^{-1}F a sheaf; no complement
  term). Worker re-anchored: the D-slice is a point with trivial
  cohomology, so dead-sector values are coboundaries after
  refinement — this is the fact that neutralises the phantom
  obstruction. Implemented Steps 3.1-3.3: lem:sieve(i) re-proved
  soundly by per-fold-ray contractible strands (false
  single-constant pin M-2 DELETED; dead sector untouched);
  lem:sieve(ii) retained; dead-sector hygiene + two-fold
  comparison F(pi_{K->P})(z_K-hat)=0 restored; lem:restrict
  (q-restriction-lemma) added; prop:vanish Steps 1-4 rewritten as
  named references. RESIDUAL DELICACY: the final kill of the
  pinned K-constant z_K-hat (needs F(pi_{K->P})-inverse-image
  control / D(K) in degree q-1) is not yet forced transparently;
  compiles clean (15pp, 0 errors/undef refs) | Honest status:
  linchpin sound, one Step-3 clause still audited | AC-1, AC-3 |
| 4 | Round-4 (post-review): M-5 FIXED (lem:sieve re-proved with the
  explicit self-contained contraction; false (ii) pin DELETED;
  lem:constcx citation removed). The M-8 residuum was TRIED and found
  UNSOUND for arbitrary F: Step 3's iB-contraction only closes [z]=0
  if G's transitions on the base/quotient faces are identities, which
  for a general presheaf they are NOT (quotient maps F(b)->F(P/K)) —
  the dead/iB discrepancy at kernel-J tuples cannot be absorbed into
  step-1's w. Per AC-4 the deliverable is honestly RESTATED:
  thm:main/prop:vanish now assert ONLY the sheaf property
  (thm:descent) + the degree-zero unit (R^0 pi_* pi^{-1} F = F),
  both verified; a Closing remark records the two open points
  ((1) R^{q>0} not shown to vanish for arbitrary F, no counterexample
  known; (2) non-f.g. P obstructed by rem:nonfg's two items). Title
  aligned. The review's B3 residuum could not be written soundly for
  all F; the reviewer must adjudicate whether the residual contraction
  has a valid completion it over-estimated | Earnest Steps A/B/C all
  attempted; Step 3 residuum is the irreducible point | AC-4
  (f.g.-degree-0 proved; q>0 + general P honestly open); AC-1
  (partial: descent/sheaf machinery underlies edges of the reduction) |
| 4R | Round-4 review (Codex): lem:sieve repair RATIFIED (M-5/B-8
  RESOLVED — contraction (w_r)_sigma := z_{(f_r,sigma)} now written
  out, two-term identity displayed, identity transports cited to
  lem:nerve(i) Case A / lem:mixed(C1), no lem:constcx citation; (ii)
  deleted, lemma renamed "Sieve: fold terraces"; lem:restrict deleted
  with no dangling refs). INDEPENDENTLY VERIFIED the worker's central
  objection: the M-8/B3 residuum IS unsound for arbitrary F. The
  residuum {iB, i(P/K)}_{K supsetneq J} has G-values on DISTINCT
  groups F(P/J) and F(P/K), with structure maps = F of the genuine
  quotients P/J ->> P/K — NOT id_A — so lem:const/lem:constcx
  (which require a single value group with identity transitions) do
  not apply and the iB-contraction identity cannot be written. The
  constant case the reviewer's B3(iv) silently invokes (R_min=R_max=
  iB) is VALID ONLY on the dead slice (all kernels = P, truly
  constant) and in rank <= 1 (no intermediate faces K); it fails on
  the rank >= 2 residuum. Round-3 review's own M-5 foreshadowed this
  (the minimum/identity hypothesis fails on mixed iB/fold tuples).
  Therefore AC-4's honest branch is CONFIRMED as the only legitimate
  deliverable, and thm:main/prop:vanish/prop:thm:main-end + Closing
  remark now state exactly the verified content. Reviewer's requested
  OWN-B3-completion: REJECTED — B3(iv)'s "residuum = constant cocycle,
  kill via contraction" has no valid completion for arbitrary F; the
  reviewer over-estimated it. AC-1 remains NOT MET for the full
  question (quasi-isomorphism for all F / arbitrary P); AC-4's
  precise-diagnosis clause is satisfied for the proved fragment |
  Reviewer adjudicates the worker's B3 objection and UPHOLDS it; the
  loop is at a genuine mathematical wall (neither a proof of q>0
  vanishing nor a counterexample exists) | AC-4 (satisfied: honest
  diagnosis, no conjecture-as-fact); AC-1 (NOT MET on the full
  question); AC-3 (the unproved q>0 is not asserted anywhere) |
| 3R | Round-3 review (Codex): lem:sieve(i)'s ray-by-ray re-proof
  RATIFIED with one citation fracture (M-5: lem:constcx invoked
  through a minimum-piece hypothesis that fails for tuples
  containing iB alongside the fold; the mathematics intended is the
  explicit front-insertion contraction and must be written out, not
  cited through lem:constcx); dead-sector hygiene Step 1 verified;
  q-skippedcases CLOSED. prop:vanish's final kill remains UNSOUND
  (M-6): circular thm:descent citation at the induction target, and
  (fatal) the conflation of the surviving pinned value as a nonzero
  class on the one-object K-exact strand — a strand with no
  higher-degree classes at all (lem:constcx); (dagger) annihilates
  only the image F(pi_{K->P})(z_K-hat), never the element, and the
  degree-inductive bookkeeping is not made precise. STRUCTURAL
  (M-7): the document proves the theorem only for f.g. P while
  problem.tex asks arbitrary P; AC-4's honest-diagnosis branch is
  authorized as the closure path (f.g. theorem + two named
  obstructions + open verdict). DIRECTIVE (M-8): replace the face
  induction by explicit degree induction with the verified sieve(ii)
  display relocated to the downward depth induction on the CFA
  residuum (iB-min constant strand kill, zero on the nose within one
  cover), DELETE sieve(ii) as a separate lemma + lem:restrict + the
  (dagger) paragraph; then close per AC-4 with a Closing Remark.
  Worker's implicit request to mark T2-R3 complete REJECTED | Review
  of 3b00c07: dead-sector/sieve machinery now healthy; the last 3
  sentences of prop:vanish are not a proof | AC-1, AC-3 (still
  open on the final-kill fragment); AC-4 (f.g./general split must
  be made the document's definitive verdict) |
| 2R | Round-2 review (Codex): Steps 0-1 verified as LANDED
  (ssec:nervetricks with (0a)-(0e), lem:filter, lem:sieve
  re-derived as corollaries, lem:dlemma, lem:anchor deleted,
  correct lem:sandwich as common refinement, q-b2 + Q-3(J') +
  q0-delta-terminal closed; compile clean, 15 pp, all refs
  defined). RATIFIED UNRESOLVED: prop:vanish Steps 1-3 still
  contain the R1-flagged floating-parenthetical clauses and,
  worse, the worker's own summary states the main theorem is
  likely FALSE as stated (splitting obstruction) while
  thm:main / thm:main-end / prop:vanish still ASSERT it as
  proved — AC-4 demands resolving this tension. DECISION FOR
  ROUND 3: do NOT construct a counterexample; RESTORE the proof of
  prop:vanish per the R1-SPINE Step 3 directive: the claimed
  "splitting" is of the WRONG map (site-extension
  Sh(B)->PSh(A) vs the sheafified pi^{-1}); G_F IS a sheaf
  (thm:descent, verified) so the unit is the single map
  F -> R pi_* G_F and there is NO complement term; the
  D-level CONSTANT at F(b_P) is dispensed by the Step-2
  two-fold/displayed-equation comparison, NOT by the
  impossible section-out-of-D. Worker verdict: STALLED (not
  regressed) | Reviewer verification + mathematical
  re-anchoring | AC-1, AC-3, AC-4 (honesty restored):
  the deliverable must not carry an unproven theorem |

#### Active Tasks
<!-- Mainline tasks only: each task must directly advance the current round objective and carry routing + capability metadata -->
| Task | Target AC | Status | Tag | Owner | Capability | Notes |
|------|-----------|--------|-----|-------|------------|-------|
| [mainline] T1: Normalize all definitions and quantifiers in problem.tex (birhizomic topology, B_P, Kan extension, R pi_*); determine expected answer (YES/NO) | AC-1, AC-2 | completed | coding | claude | N/A | Answer: YES (valuative collapse). REVIEW R0: normalization VIOLATED — f.g. silently added to def of monoid (see B-1) |
| [mainline] T2: Develop complete proof that F -> R pi_* pi^{-1} F is a quasi-isomorphism (or a rigorous counterexample) | AC-1, AC-4 | in_progress | coding | claude | N/A | ROUND 2: Sections 2-3 remain verified. Section 4 SPINE Steps 0-1 LANDED (nerve-complex subsection, filter lemma lem:filter, sieve re-derived as two references, lem:anchor deleted, lem:dlemma, correct common-refinement lem:sandwich). prop:vanish Steps 1-3 remain UNCLOSED (worker honest-admit). ROUND-2-REVIEWER RE-ANCHOR: the claimed splitting is of the WRONG map (site-extension Sh(B)->PSh(A) vs the sheafified pi^{-1}); thm:descent PROVED G_F is a sheaf, so the unit is the single map F -> R pi_* G_F with NO complement term; the D-level constant is dispensed by the Step-2 two-fold comparison, NOT by the impossible section-out-of-D. The proof must be RESTORED, not countered |
| [mainline] T2b: Higher direct images R^{q>0} pi_* (pi^{-1} F) for ARBITRARY F — OPEN mainline item. Round-4 review CONFIRMS the only closed route (M-8/B3 iB-residuum contraction) is unsound for general F: residuum transitions F(b)->F(P/K) are quotients, not identities, so lem:const/lem:constcx do not apply and the contraction cannot be written. No proof and no counterexample found in 5 rounds. The sheaf property (thm:descent) and degree-zero unit (R^0) ARE proved for f.g. P; the q>0 vanishing is the irreducible open core of the question | AC-1, AC-4 | OPEN | coding | claude | N/A | Genuine mathematical wall, not a worker-side gap: neither the reviewer's B3 nor any prior SPINE step yields H^{q>0}=0 for arbitrary F. Requires a genuinely new ingredient (not a residuum contraction on non-constant strands) OR a counterexample |
| [mainline] T2-R3: Implement the Round-3-review directive for prop:vanish — Steps A (M-5 sieve repair) DONE and RATIFIED; Step B/M-8 (degree-inductive residuum) ATTEMPTED and reviewer-CONFIRMED UNSOUND for arbitrary F (see T2b / Round-4 review row); Step C/M-7 (AC-4 honest closure) DONE — the old face-induction and its unsound final kill (M-6) are DELETED, lem:restrict and sieve(ii) removed, thm:main/prop:vanish/thm:main-end restated to exactly the proved content (sheaf + R^0 for f.g. P) + Closing remark recording the two open points, no counterexample claimed. NO unproved theorem text remains (grep verified) | AC-1, AC-3, AC-4 | CLOSED as far as honestly possible (the directive's fallback "restating thm:main per AC-4 when unfixable" is exactly the branch taken and is reviewer-ratified; the residuum route it prescribed is confirmed unsound) | coding | claude | N/A | Round-4 review: M-5/B-8 RESOLVED; M-6 fragment deleted; M-7 AC-4 closure verified; M-8 residuum rejected as unsound (reviewer over-estimate) |
| [mainline] T3: Write full argument as standalone solution.tex (article class, standard packages) | AC-1, AC-2, AC-5 | in_progress | coding | claude | N/A | 14 typeset pages, compiles clean (0 errors, 0 undefined refs, harmless hyperref warnings only); iffalse block and tag citations removed — AC-5 OK |
| [mainline] T4: Compile with pdflatex, audit logical direction/quantifiers/edge cases vs problem.tex | AC-3, AC-5 | in_progress | coding | claude | N/A | R1 reviewer recompile clean; audit found B-7 (proof-dependent Cech foundations: sieves/filtrations/depth-level undefined — queued definition issue, no mathematical gap), B-8 (lem:sieve overclaims; undermined by a superior GENERIC filter lemma now designed in the R1 review), B-9 (lem:sandwich coverage/refusal-preservation clauses rest on unsupported sub-claims; absorbed into the SPINE steps of the R1 review) |
| [mainline] T5: Commit round, write summary, resolve all reviewer findings | AC-1, AC-3 | in_progress | coding | claude | N/A | R1 committed 3522e48 with summary; R1 review REPLACES the deferred Q-1 check list by the structured SPINE (steps 0-4) in round-1-review-result.md, to be implemented in Round 2 |

### Blocking Side Issues
<!-- Only issues that directly block current mainline progress belong here -->
| Issue | Discovered Round | Blocking AC | Resolution Path |
|-------|-----------------|-------------|-----------------|
| B-1: solution.tex line 43 redefines "monoid" as finitely generated; problem.tex has no f.g. hypothesis; whole proof assumes f.g. | 0 (review) | AC-1, AC-3 | RESOLVED R1: Branch B implemented — Section 1 now states monoids per problem.tex, isolates a "Scope hypothesis: f.g. P" paragraph listing exactly where f.g. is used (Prop 2.1, Lem 2.4, Cor 2.5, face induction) and the two obstructions in the general case (f.p. of P->P/K; infinite face poset), with Theorem 1.1 restated for f.g. P. Remark rem:nonfg cross-references it |
| B-2: Lemma 2.4 (lem:N) Step 2 contradiction is invalid: "but δ−g ∈ H1 (same class)" — δ−g ∉ H1 since g ∉ H1 | 0 (review) | AC-1 | RESOLVED R1: Step 2 fully rewritten (no "same class" anywhere): H_2/H_1 is archimedean via convex pull-back, generator classes outside H_1 bounded below by c_0>0 inside the embedding Lambda↪R, so at most N_0 outside summands; a fixed partial sum s occurs infinitely often; w=δ−s ∈ H_1 and 0≤nγ≤w in archimedean H_1 for infinitely many n: contradiction |
| B-3: Birhizomicity's finite-presentation hypothesis never verified anywhere | 0 (review) | AC-1, AC-3 | RESOLVED R1: new subsection "Finite presentation" (ssec:fp) with prop:fp (f.p. characterization; f.p. of P->N, P->P/K, pushouts), rem:nonfg recording f.p. of all cover/refinement/test maps, one-sentence notes added at lem:atomic (necessity maps), cor:probecover, lem:sandwich; new lem:surj gives the surjective-cover w.l.o.g. |
| B-4: Čech nerve never defined; cofinality cited by website tag | 0 (review) | AC-1 | RESOLVED R1: def:nerve (nerve = iterated pushouts over the slice, alternating complex), lem:nervemaps (structure maps iff kernel refines, modulo surjectivity), rem:verdier (Verdier hypercovering theorem, SGA 4 Exp. V Thm 7.4.1, stated in words with hypotheses); tag numbers removed from prop:vanish |
| B-5: Lemma 4.3(b) ambiguous/false as written | 0 (review) | AC-1 | RESOLVED R1: restated as (C1) and (C2) with the exact Z-hypotheses and full pushout-criterion proofs (face-property argument for K/J); iteration clause added |
| B-6: iffalse workflow block; tag-number citation | 0 (review) | AC-5, AC-2 | RESOLVED R1: iffalse block deleted (reviewer re-verified none remains); see B-4 for the citation |
| B-7: Section 4 relies on filtrations, sieves, exact/constant complexes, simplicial/complex foundations never spelled out | 1 (review) | AC-1, AC-2 | RESOLVED R2 (foundations part): ssec:nervetricks "The nerve complex: depth, strands, and transfers" inserted with (0a) rem:normalize, (0b) def:strand, (0c) lem:constcx (front-insertion homotopy relocated; lem:const reproved as corollary), (0d) lem:subquot (exact subquotient / signed transport), (0e) lem:depth (order-respecting via lem:nervemaps), (0e') rem:transfer. Verified by Round-2 reviewer; every later support sentence now has a named reference. The part needed by prop:vanish Steps 2-3 is folded into reopened B-8 |
| B-8: lem:sieve(i)/(ii) overclaims (filters to level-exactness not properly supported) | 1 (review) | AC-1 | RESOLVED R4: (i) re-proved self-containedly with the explicit contraction (w_r)_sigma := z_{(f_r,sigma)} and the two-term identity displayed, identity transports cited to lem:nerve(i) Case A / lem:mixed(C1), NO lem:constcx citation (the M-5 fracture is repaired exactly as the Round-4 reviewer prescribed); (ii) is DELETED/retired (no longer a separate claim; the residuum that would have used it is itself unsound for arbitrary F, so it is not needed). Lemma renamed "Sieve: fold terraces"; verified by Round-4 reviewer, no dangling refs |
| B-9: lem:sandwich coverage and refusal-preservation clauses rest on unsupported sub-claims (no real description of the refined cover) | 1 (review) | AC-1 | RESOLVED R2: lem:sandwich replaced by the correct common-refinement lemma (piecewise pushout of two covers covers and refines both, via the birhizomic pretopology) — the flagged same-ray / GF-min / survival sub-claims are gone; only the weakened statement prop:vanish actually invokes is kept. Verified by Round-2 reviewer |

### Queued Side Issues
<!-- Non-blocking issues stay queued and must NOT replace the round objective -->
| Issue | Discovered Round | Why Not Blocking | Revisit Trigger |
|-------|-----------------|------------------|-----------------|
| Q-1: Global-verification pass for nerve kernel claims under common-refinement parents | 0 (review) | REPLACED R1 by the structured SPINE (steps 0-4) in round-1-review-result.md | Round 2 implements SPINE Steps 0-3 (or 4) |
| Q-2: No statement outside Lemma 2.4 Step 2 / Example 2.17 implicitly uses "same class" | 0 (review) | RESOLVED R1: B-2 rewritten with a different, verified argument; document-wide grep finds no residual "same class" usage; Ex. ff verified in R0 | Closed R1 |
| Q-3: Final typography/labels pass ("leaves the kernel" wording; rank-one parentheticals) | 0 (review) | Cosmetic; the J'-rigid slip was closed R2 (def:square now says "rigid") | Final round before completion |
| q-complex-foundations: write the complex theory (sieves, filtration, exactness, support criterion) generically once | 1 (review) | Definition/organization gap only; no mathematical error found in the concrete computations | CLOSED R2 (B-7): ssec:nervetricks written; verified |
| q-d-lemma: standalone tight-CFA-face lemma (tight chi has chi^gp((K/J)^gp)=dZ, d>=1) | 1 (review) | Small exactness sub-lemma | CLOSED R2: lem:dlemma stated and proved (from ker chi^gp=0 via prop:bp(c)); available for the Round-3 Step-2/Step-3 citations |
| q-restriction-lemma: what pullback does to standard rigid covers and their strata | 1 (review) | Was hand-waved in prop:vanish Step 3; lem:restrict added in R3 but its only use was the unsound final-kill fragment (M-6) | CLOSED as superseded by Round-3 review M-8 (lem:restrict to be DELETED with the face induction; the residuum route never restricts to a face slice) |
| q-accounting: support/weight accounting for prop:vanish | 1 (review) | lem:filter exists; floating parentheticals replaced by named references in R3 (verified) | CLOSED as superseded by Round-3 review M-8/B4: after the residuum rewrite lem:filter has no remaining citations (cosmetic decision whether to keep it; only page-budget-relevant) |
| q0-delta-terminal: D is NOT terminal of the B-slice; delete the "terminal" parenthetical, state D-initial correctly | 1 (review) | One-line editorial/Math fix | CLOSED R2: lem:dead now states D is the initial object; the wrong parenthetical is gone; verified |
| q0-lem-anchor: delete or genuinely use; currently vacuous filler | 1 (review) | Unused lemma | CLOSED R2: lem:anchor deleted; its content absorbed into lem:constcx; verified |
| q-b2-microtypo: solution.tex N_0 := phi(delta-bar)/c_0 mixes phi (embedding) with functionals | 0/1 (review) | Notation micro-typo | CLOSED R2: renamed to \mu_\Lambda (embedding) and \mu_E (inclusion); verified |
| q-skippedcases: ensure the rank-one (dim(bar P) <= 1) and P={0} cases of prop:vanish are treated by a named reference (lem:const + the lem:dead base case), not a floating parenthetical | 2 (review) | CLOSED R3: prop:vanish opening treats bar P={0} by lem:dead and dim(bar P)<=1 by lem:const (R_min=R_max=iB), both named | Round 3 review verified |
| q-dead-sector: lem:filter's (F2) single anchor U covers binary dead pieces only; pieces built from >= 2 folds lie outside (F2)'s pattern | 2 (review) | Not on the critical path: R3's sieve(i) leaves the dead sector untouched and verified; on the M-8 residuum route no non-dead value ever needs a deep dead piece | WONTFIX pending M-8 landing in Round 4 (close fully once B4 deletions are in) |
| q-scope-lifting: general (non-finitely-generated) P case of thm:main | 3 (review) | Two exact obstructions named in rem:nonfg (f.p. of P->P/K can fail; face poset can be infinite, breaking depth-induction finiteness and the finitely-many-rays clause); AC-4 closure (Closing Remark with the obstructions + open verdict) is the authorized deliverable path | Explicitly OUT of scope; do not attempt in any round --- revisit only if a future plan version re-scopes the problem |

### Completed and Verified
<!-- Only move tasks here after Codex verification -->
| AC | Task | Completed Round | Verified Round | Evidence |
|----|------|-----------------|----------------|----------|
| AC-1/AC-2 | T1: normalize definitions/quantifiers from problem.tex | 0 | 1 | Section 1 states monoids per problem.tex (no silent f.g. redefinition); birhizomic/B_P/Kan/R-pi_* per statement; reviewer-verified R1 |
| AC-1 | Sheaf property of pi^{-1}F (thm:descent) for f.g. P | 0-1 | 1-4 | prop:adj (G_F = F∘B), prop:sep, thm:descent verified across rounds 1-4; carried unchanged |
| AC-1 | Degree-zero unit R^0 pi_* pi^{-1} F = F for f.g. P (prop:thm:main-end) | 4 | 4 | Section 3 + prop:vanish(a): H^0(i(b),G)=F(b); verified Round 4 |
| AC-1 | lem:sieve "Sieve: fold terraces" self-contained contraction | 4 | 4 | (w_r)_sigma := z_{(f_r,sigma)}, two-term identity, lem:nerve(i)A/lem:mixed(C1) citations; no lem:constcx; reviewer-ratified |
| AC-4 | Honest AC-4 closure: no unproved assertion anywhere | 4 | 4 | thm:main/prop:vanish/thm:main-end restated to proved content; Closing remark lists the two open points; grep-verified no unsupported R^{q>0} claim |
| AC-5 | Standalone compilable solution.tex <= 16 pp, standard packages | 0 | 4 | pdflatex x2: 0 errors / 0 undefined refs / 15 pages; article class, allowed packages only; no markdown/workflow text |

### Explicitly Deferred
<!-- Items here require strong justification -->
| Task | Original AC | Deferred Since | Justification | When to Reconsider |
|------|-------------|----------------|---------------|-------------------|
