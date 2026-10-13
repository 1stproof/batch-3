# Round 1 Review Result — prob-001

Reviewer: moonshotai/Kimi-k3 (max effort), reviewing Round 1 commit 3522e48
(worker "Claude" per the RLCR loop). Scope checked against plan.md AC-1..AC-5,
problem.tex (verbatim), round-1-contract.md, the R0 review directive items 1-6,
and the full solution.tex (1391 lines, read line by line; Sections 2-3
re-verified at proof level, Section 4 audited for support).

Reviewer recompile: pdflatex twice, **0 errors, 0 undefined references,
14 pages** (limit 16); only harmless hyperref PDF-string warnings.
Greps: no `iffalse`, no `Stacks Tag`, no "same class", no "..." artifacts.

## Part 1 — Verification of the R0 directive items (B-1..B-6)

| Item | Directive | Status |
|---|---|---|
| 1 (B-1) | Branch B honest scoping, or STAR | **DONE (Branch B)**. Section 1 now defines "monoid" exactly as in problem.tex and isolates a "Scope hypothesis" paragraph: theorem proved for f.g. P; exact uses of f.g. listed; Theorem 1.1 restated for f.g. P; rem:nonfg describes the two obstructions precisely. Accepted; old B-1 (silent redefinition) removed. |
| 2 (B-2) | Delete false "same class" clause, keep the convex-submonoid finish | **DONE, and in fact SUPERSEDED** (see new N-1 below): Step 2 now uses the finite-partial-sum argument with sharpness of V; the argument is verified SOUND by this reviewer. No "same class" string anywhere. |
| 3 (B-3) | f.p. subsection + w.l.o.g. + sentence notes | **DONE** (ssec:fp, prop:fp, rem:nonfg, lem:surj, one-sentence notes at lem:atomic / cor:probecover / lem:sandwich). Content accepted. |
| 4 (B-4) | def:nerve + lem:nervemaps + named Verdier | **DONE** (def:nerve, lem:nervemaps, rem:verdier; tag numbers removed; SGA4 Exp. V, Thm 7.4.1 named in words with the used consequence). Caveat: lem:nervemaps is stated imprecisely ("iff kernel refines" needs the surjectivity/CFA-side hypotheses its use actually has); its only uses are the identity-transition and kernel-refinement clauses, which are correct. Logged under B-7. |
| 5 (B-5) | Restate Lem 4.3(b) as (C1),(C2) with proofs | **DONE** (lem:mixed (C1),(C2), with full pushout-criterion proofs; iteration clause added). Verified correct. |
| 6 (B-6) | Delete iffalse block; Q-1/Q-2; recompile | **DONE**: iffalse absent; Q-2 closed (document-wide grep: no "same class" resurface; Ex. ex:ff was already verified in R0); recompile clean. Q-1 was deferred by the R0 review to the Round-2 audit and is REPLACED by this review's SPINE below. |

Sections 2-3 were re-verified line by line at proof level after the
repairs: prop:bp, constr:pushout, prop:fp, lem:surj, lem:N (new Step 2),
cor:function, lem:inj0, lem:infstruct, lem:atomic, cor:cfa, thm:normalform,
rem:cover-points, lem:Zpointed, lem:pushout, ex:ff, prop:equiface,
cor:probecover, cor:probecovers, prop:adj, prop:sep, thm:descent (Claims A/B
and the endgame). No mathematical errors found. The descent endgame's
"first map surjective" clause is correct (constant systems are compatible).

## Part 1 (cont.) — Ratification of the B-2 repair (N-1)

**N-1 (ratified; stronger than the directive).** The written Step 2 of
lem:N does NOT implement the R0 directive's finish ("g, delta-g in V∩H_1;
delta >= n gamma; H_1 archimedean"); it implements a better argument:
decompose delta - n gamma = s_n + h_n with at most N_0 summands outside
H_1 (bounded via the archimedean quotient H_2/H_1 hookrightarrow R and
c_0 > 0); fix s_n = s for infinitely many n; then w := delta - s has
h_n = w - n gamma in V∩H_1, so for infinitely many n
0 <= n gamma <= w in H_1 while the archimedean bound n <= floor(w/gamma)
holds. This closes even when H_1 is discrete (s != delta since delta not in
H_1, so w != 0, hence w has a strictly positive H_1-part — sharpness of V is
what forces w > 0, and THIS is the clause the R0-criticized "same class"
argument was trying and failing to replace) or when H_1 is not archimedean
(w of strictly larger convex class dominates every element of H_1). The
reviewer verified all steps line by line. Minor fact used: a totally
ordered f.g. abelian group has a MAXIMAL convex chain, hence H_2/H_1
archimedean; standard (isolated subgroups are the union of f.g.-many
classes by the Gordan/rank argument implicit in Step 3's d-computation).
One micro-typo: the embedding Lambda -> R is called phi while phi is
overloaded for functionals; rename mu (queued as q-b2-microtypo).

## Part 1 (cont.) — New findings in Section 4 (the relaxed state)

### MAINLINE GAPS

**M-1 (= B-8).** `lem:sieve` (i) and (ii) overclaim. (i) asserts vanishing
on every terrace containing a kernel-J fold via an induction whose
"solvability gives z_tau = 0" clause does not restrict to level-exactness:
the face-omitting-iB term need not be at the level claimed, and the
"residual fold-free/no-fold configuration ... (vacuous)" clause is exactly
where support can leak. (ii) asserts equality of the K-exact values
"through the connected overlap graph", but overlaps of two K-exact pieces
can be at the DEAD level, where transports land in F(b_P) and no uniqueness
is available without the vanishing already established on deeper levels —
i.e. (ii) as used needs the depth-order support criterion, not the
face-width graph argument written. The vanishing argument (prop:vanish
Steps 1-3) genuinely requires the first real support step of the spine: a
**support criterion for exact cocycles on filtered poset nerves by DEPTH
(position in the face-poset depth order), not by face width**. In the
correct formulation (SPINE Step 1 below) the sieve statements follow from a
generic filter lemma.

**M-2 (= B-9).** `lem:sandwich` coverage and refusal-preservation clauses
rest on unsupported sub-claims: (a) "a point served by the R-fold U is
served via its factorization through some S-fold V on the same ray" — true
only after a normal-form/same-ray factorization fact that is neither stated
nor isolated; (b) "birhizomicity from lem:atomic (value groups match along
the composite)" — the required value-group equality for the product piece
U otimes V is never computed; (c) "Rigidify as usual; the kernel-J folds of
S survive as pieces" — the deletion procedure can delete refused pieces
(they carry nonidentity maps to iB), so an explicit survival clause is
required. The refined family R^flat is described loosely ("all products
U otimes V") with no precise index set.

### BLOCKING SIDE ISSUES

**B-7 (foundations; queued as definitions).** Section 4 uses filtrations,
sieves (S(K)), exact/constant complexes, and simplicial facts (normalized =
alternating quotient, Eilenberg-Zilber special case, homotopy transfer
across refinements) that are never spelled out. This is currently NOT
observably a mathematical gap — every concrete identity the reviewer
checked is correct — but the section cannot be audited line by line (AC-1)
until the complex theory is written generically once (SPINE Step 0) and
every later sentence references it. It becomes mainline the instant the
generic lemma is substituted into sieve/sandwich/prop:vanish.

### QUEUED SIDE ISSUES

- q-complex-foundations (= B-7's implementation): write the complex theory
  generically ONCE (exact subquotients, degeneracy quotient,
  homotopy-transfer criterion, depth-level support) and make every later
  sentence reference it. No mathematical gap observed; pure
  definition/organization gap.
- q-d-lemma: standalone tight/CFA-face lemma (functional values on a face K
  of a tight target and its group: chi(K gp\{0}) often and wrongly invoked
  as "dZ for d >= 1" inside Step-3-type computations; isolated and proved
  once, it is one line from ker chi gp = 0) — currently embedded
  unseparated inside proofs.
- q-restriction-lemma: what pullback does to standard rigid covers and
  their strata (restriction to the slice over i(P/K); the sifted family
  S = {U otimes D}). Only hand-waved at present; needed in whichever SPINE
  branch is taken.
- q-accounting: support/weight bookkeeping for prop:vanish AFTER the
  generic lemma exists (replace the floating "(the residual fold-free /
  no-fold configuration)" and "(dead or stricter-level overlap)" clauses by
  named references).
- q0-delta-terminal: D is NOT terminal of the B-slice; it carries
  B(D) = b_P, the INITIAL object. lem:dead's mathematics is right
  (initial slice object), but the "terminal P-level piece" wording in
  prop:vanish and the terminality parenthetical should be corrected.
- q0-lem-anchor: lem:anchor is vacuous filler (its rho is never given
  cochain-level meaning; its conclusions duplicate lem:const); delete or
  genuinely use (e.g. as the contractibility engine for Step 4).
- q-b2-microtypo: N_0 := phi(delta-bar)/c_0 symbol collision
  (phi = the archimedean embedding of Lambda, phi = generic functional).
  Rename to mu.
- Q-3 typography pass remains queued (final round); includes Def. 4.1's
  "J-prime-rigid" slip (no J' defined) and "leaves the kernel" phrasing.

## Part 2 — Goal Alignment Summary

AC progress: AC-1/AC-3 now have honest scope (B-1 repaired) and Sections
2-3 fully verified; AC-2 fixed by rem:verdier; AC-5 fixed by iffalse
deletion (14 pp). AC-4 not triggered (answer remains YES; the f.g.
restriction is logged in the Plan Evolution Log, with the precise
obstruction statement). Remaining work sits on AC-1 (Section 4 must be made
line-by-line verifiable) and AC-3 (prop:vanish must reference definite
lemmas).

ACs: 3.5/5 addressed (AC-1, AC-3 partial; AC-2, AC-5 done; AC-4 n/a) |
Forgotten items: 0 | Unjustified deferrals: 0 (Q-1 was review-authorized
and is now superseded by the SPINE)

Tracker state reconciled by this reviewer: B-1..B-6 remain marked RESOLVED
(correct); B-7/B-8/B-9 added to Blocking; Q-1 replaced by the SPINE; Q-2
closed; queued items q-complex-foundations / q-d-lemma /
q-restriction-lemma / q-accounting / q0-* / q-b2-microtypo / Q-3 recorded;
Plan Evolution Log entry added. No scope drift.

## Part 3 — Capability Map Summary

Capability anchor: N/A (plan.md has no feature/capability map) |
Dependency gaps: 0 | Scope drift: no

## Part 4 — Directive implementation plan for Round 2 (SPINE; singular; execute as written)

Round 2's sole mainline objective: make prop:vanish (and its lemmas)
line-by-line verifiable by implementing the generic support machinery ONCE
and substituting references below. Execute Steps 0-3 in order. Step 4 is an
OPTIONAL consolidation, only after Steps 0-3 land.

**Step 0 (foundations; B-7 / q-complex-foundations).** Insert, before
def:square, a subsection "The nerve complex" with:
  (0a) Definition: nerve N_q(R) = coproduct over tuples of iterated
  pushouts; face/degeneracy maps; for a presheaf W the Cech complex
  C^q(R;W) := prod_tau W(bar tau) with the displayed alternating
  differential; the alternating = normalized quotient A^q and the standard
  isomorphism H^*(C) = H^*(A) (degenerate cochains form a contractible
  subcomplex; statement only, "standard normalization").
  (0b) Filtration: define the DEPTH of a piece U as the poset-depth of
  Phi_U in the face lattice of bar P (J = depth 0; joins increase depth;
  D = maximal depth); kernels refine along structure maps (lem:nervemaps +
  the kernel functor T |-> Phi_T), so depth is order-respecting on nerve
  pieces. Define the sieve S(K).
  (0c) Constant complexes lemma (formal lem:const): a strand on which all
  face maps are identities and which contains a minimum piece is acyclic in
  degrees >= 1, H^0 = value at the minimum. Relocate the existing (correct)
  front-insertion homotopy here.
  (0d) Exact-subquotient / support transfer lemma: if C = C' + C'' is a
  decomposition closed under the differential and C' is contractible, then
  H^*(C) = H^*(C''), and a cocycle's highest-stratum component transforms
  by the stated signed transport. Give the six-line check.
  (0e) Homotopy-transfer criterion for pullbacks along refinement maps of
  covers (Cech comparison maps are canonical up to homotopy; compatible
  with the colimit from rem:verdier). One paragraph.
  (0f) Delete lem:anchor (q0-lem-anchor) or re-derive it as the terminal
  case of (0c); delete the wrong "terminal" parenthetical at lem:dead
  (q0-delta-terminal).

**Step 1 (generic filter lemma; B-8).** Formal statement and proof:
  Let (X_mu) be a finite poset of levels, W a presheaf with quotient
  transports, and z a degree q >= 1 cocycle on a nerve whose pieces carry
  order-respecting (X_mu)-labels. If every cocycle value at the TOP level
  vanishes, then after pullback along any refinement inducing the identity
  on labels, z is cohomologous to a cocycle supported one level lower, with
  the transported values at the next level changed by the stated signed
  image. Proof: apply (0d) to the stratification by level; the contracting
  homotopy lives inside the top strand (identity transports; (0c)) and
  raises support one level at a time; finiteness of the poset terminates
  the iteration at the initial level.
  Corollaries (the sieve statements): derive lem:sieve(i) by the choice
  poset = {fold-ray strata} with the dead stratum on top (any nerve piece
  containing two distinct-ray kernel-J folds, or a kernel-J fold against a
  dead/deeper piece, is dead: lem:nerve(i), lem:mixed(a)/(C1)); derive
  lem:sieve(ii) by the choice poset = {K-slices} with the P-slice on top
  (overlaps of two K-exact pieces lie at depth >= depth(K): lem:nerve,
  lem:mixed), pins provided by the chain through i(P/K) per (0c). DELETE
  the current terrace-induction and replace (i)/(ii)'s proofs by two
  references each.

**Step 2 (sandwich isolation; B-9).** Inline the two needed facts:
  (2a) In prop:vanish Step 1 replace the sifted-cover paragraph by: "S :=
  {U otimes D : U in R} refines the singleton cover {D} of D, hence is a
  cover of D; the pulled cocycle lies on the constant strand of value
  F(b_P); by (0c) its class vanishes after refinement, and the pullback
  exists by (0e)/rem:verdier." Then the constancy on the D-level is no
  longer needed as an unsupported clause: Step 1's generic lemma (applied
  with the two-level poset {nondead < dead}) yields a cohomologous cocycle
  with vanishing dead-level support, i.e. z_P-terminal = 0 directly.
  (2b) In Step 3 replace "lem:sandwich provides the common refinement" by
  the explicit restriction: pullback of R along i(b) -> i(P/K) is a cover
  of i(P/K); each piece U otimes i(P/K) has kernel Phi_U join K
  (lem:nerve(i)/(ii), lem:mixed(C2)); the restricted cocycle has
  transport-zero on depth >= depth(K) levels by the conclusion of
  prop:vanish's earlier Steps + Step 1's lemma. State and prove
  q-restriction-lemma here (one-paragraph: statement as above; proof via
  the CFA kernel table).
  Only if a common refinement with an arbitrary S is still needed
  elsewhere, repair lem:sandwich properly: precise index set
  (products U otimes V over kernel-J folds U of R and S-folds V on the same
  ray, plus named pieces); coverage via atomicity with the explicit
  value-group computation GF(U otimes V) = min(GF(U), GF(V)) on the shared
  ray; and the survival clause (during deletion never delete a refused
  piece; delete only pieces with a nonidentity map to a surviving one, and
  check the served-point transfer).

**Step 3 (rewrite prop:vanish Steps 1-3 as references).**
  Step 1: one or two sentences citing (0c)+(0e)+Step 1 generic lemma,
  concluding z_P-terminal = 0 (the current "Subtracting the pullback of
  partial w ... still has constant values hat z_P" long sentence is
  deleted; its content is absorbed).
  Step 2: keep the displayed two-fold subtraction (correct as written),
  including the rank-one and b = b_P parentheticals; promote the d-lemma
  (q-d-lemma) to a standalone proven lemma and cite it wherever
  "chi(K gp) = dZ, d >= 1"-type statements are used (lem:nerve Case B).
  Step 3: replace the long parenthetical "(the sifted restricted cover is
  standard rigid over i(P/K); its D(K)-level constant equals ... bounded by
  the vanishing P-level constant of D(l))" by: induction hypothesis at the
  strictly larger face (the D(K)-statement) + q-restriction-lemma +
  Step 1 generic lemma; the phrase "after one more pullback" must cite
  (0e); the final "outward maps F(pi_{K to P}) of that constant are zero"
  must reference the Step-2 displayed equations.
  Step 4 + consistency note: keep (already correct).

**Step 4 (OPTIONAL consolidation).** If Steps 1-3 suggest it, reorder
Section 4: nerve complex (Step 0) -> kernel computations (nerve, mixed,
C1/C2) -> support machinery (0c/Step-1 lemma) -> vanishing -> dead/base
cases. Do NOT delay Steps 0-3 for this.

**Closeout.** Fix q-b2-microtypo and run the Q-3 typography pass (J-prime
slip in def:square; "leaves the kernel" phrasing; q0 items). Recompile
twice; verify 0 errors, 0 undefined refs, <= 16 pages (currently 14; Steps
0-2 add roughly 1.5 pages, so the limit is safe). Update goal-tracker
(B-7/B-8/B-9 -> resolved; queue items closed; T2/T4 statuses per reality).
Commit with a message referencing this review; write the round-2 summary.

Round 3 (review-driven): full line-by-line re-audit of the restructured
Section 4 and a closing consistency check of the whole document against
problem.tex.

---

Mainline Progress Verdict: ADVANCED
