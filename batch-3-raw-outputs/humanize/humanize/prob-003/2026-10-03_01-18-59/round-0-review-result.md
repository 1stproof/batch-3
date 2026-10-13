# Round 0 Review Result - prob-003 (bigon algebra = generalized quantum double)

Reviewer: independent audit of `solution.tex` (commit 233fa71), `plan.md`,
`goal-tracker.md`, and worker scratch. Build state: pdflatex compiles,
6 pages, no undefined refs - AC-5 mechanically fine. The mathematics is not:
Part 1 is broken at its single nontrivial point (the cross relation), and
Part 2 inherits the break plus has its own logic gaps.

## Mainline Progress Verdict: STALLED

(Salvageable Round-0 progress: SS1 setup, the Lemma 1.1 pairing table on
grouplikes, the PBW strategy for Theorem 3.1, and the tensor-factorization
instinct of Lemma 4.2. But all three numbered results - Lemma 1.2, Prop 3.3,
Thm 4.2 - that carry the mainline are false or unproved as written.)

```
ACs: 1/5 fully met (AC-5 only) | Forgotten items: 0 | Unjustified deferrals: 2
(Definition 2.1 "standard construction" deferral; Part-1 well-definedness
deferral via quips)
Capability anchor: N/A | Dependency gaps: 0 | Scope drift: no
```

=====================================================================
## A. BLOCKING SIDE ISSUES (on the mainline path; must be fixed)
=====================================================================

### A1 (FATAL). Proposition 3.3 is unproved AND false under the paper's own axioms; the fix is a convention repair, not prose

Prop 3.3 is the only place in the paper where the cross product (SK) is
applied to a non-grouplike pair - it is the entire "quantum double" content
of the problem. Audit findings against the paper's own SS1 axioms
((PA), (P), (C), (SK) as printed):

(i) The regenerated coproduct is mis-copied: with Delta(E) = E x K + 1 x E,
    (Delta x id)Delta(E) = E x K x K + 1 x E x K + 1 x 1 x E.
    The paper writes the first tensorand as EK ("(E_iK_i, K_i, K_i)+...").
(ii) The line "hence also S^{-1}(F_r) = -F_r K_r^{-1}" is wrong:
    m(S x id)Delta(F) = S(F) + KF = 0 gives S(F) = -KF, and
    m(S^{-1} x id)Delta^{op}(F) = F + S^{-1}(F)K^{-1} = 0 gives
    S^{-1}(F) = -FK. (Same wrong value is hard-coded in scratch/double3.py's
    `scount`.)
(iii) Channel evaluation under the printed (SK) + (PA): for x = F in B^-,
    y = E in B^+, all channels in the double sum vanish except
    ((K^{-1},F,1),(1,E,K)) giving EF and ((K^{-1},K^{-1},F),(1,1,E)) giving
    <F,E> K^{-1} = theta K^{-1}. In particular the channel the proof claims
    ("S^{-1}(F)-against-(EK) leaving K") vanishes: <S^{-1}F, EK> = 0 since by
    (PA) <-FK^{-1}, EK> = <K^{-1},EK><F,K> + <K^{-1},K><F,E> evaluated with
    Delta-slot bookkeeping gives the F-pairing against a Cartan/epsilon
    factor. (Checked both with the paper's displayed Delta^2(E) and with the
    corrected one; either way) the honest outcome is

        (SK), as printed:   F E = E F + theta K^{-1},

    which is NOT (H2). With (ii) corrected and the S-version cross relation
    (see below), also not (H2) without the sign repair in (iv).
(iv) The patch sentence "... which is (H2) up to the global sign convention
    E <-> -F" is void: under E |-> -E, F |-> -F the commutator [E,F] is
    invariant (two sign flips), so no "sign convention" can change theta
    times one Cartan monomial into theta(K - K^{-1}). This is confidence
    language substituting for a failed computation (AC-3 negative test; and
    plan.md: never present "an invented theorem or concealed gap").

Corroboration: the worker's own `scratch/double3.py` line 33 hard-codes
`# EF commutation (verified): F E = E F + TH(Ki G - K Gi)` - the
(H2)-compatible relation [E,F] = theta(K - K^{-1}) - and never derives it
from the Tanisaki (SK) `cross` it implements. The "exact symbolic SK
verification" claim in the summary and in BitLesson
BL-20261003-skew-pairing-bookkeeping is therefore inaccurate: the script
ASSERTS the SK-incompatible answer while implementing the SK pairing; the
gap between them is exactly this finding.

Repair (directive, see D1): the cross relation that is consistent with the
paper's (PA)+(P)+(H1) and yields exactly (H2) is the Drinfeld-Tanisaki
convention  psi(y, x') = <S(x'_1), y_1> x'_2 y_2 <x'_3, y_3>  (the antipode
S, not S^{-1}, on the B^- coproduct side). With the corrected Delta^2 and
S(F) = -KF, its two surviving channels give
   E F = F E - theta K + theta K^{-1},
i.e. [E,F] = theta(K - K^{-1}) = (K - K^{-1})/(q^{-1} - q)^{-1}...
cleanly [E,F] = (K - K^{-1})/(q - q^{-1}) = (H2). Verification that the
pairing (P) is compatible with the paper's (H1) sign (one line: apply
tau(F_s, -) to K_i E_r K_i^{-1} = q^{+a_r(i)} E_r using (PA) and Delta(F);
the identity holds with the printed +a sign) should be written down too.
The reviewer checked both computations explicitly; they take under a page.

### A2 (BLOCKING). Lemma 1.2 ("grouplikes commute across the double") is false as stated; the entire Cartan-side bookkeeping of Parts 1-2 rests on it

Under either the printed (SK) or the corrected S-version cross relation,
for g = K_i on the B^- side one computes, from Delta^2(E) and (PA),
   psi(E_r, g) = <g, K_r> g E_r = q^{a_r(i)} g E_r,
NOT commutation. (The proof's claim that "in every tensorand at most one
factor contains an E... the two pairing factors are inverse and telescope"
is false: only ONE of the two pairing slots receives a Cartan argument - the
E-containing slot is killed by (T:e) - so a single q-power survives.)
Consequences:
- Definition 2.1(C)'s first family ("diagonal arcs commute with everything
  in the other copy") is unsubstantiated; every diagonal mixed relation must
  be computed channel-wise (some may indeed be trivial - the worker's scratch
  suggests e.g. b_11 c_21 commutes in its model - but nothing may be asserted
  via Lemma 1.2).
- Lemma 4.1's centrality argument ("by Lemma 1.2, Omega commutes with
  U_q(b^-)") is broken. The correct central/kernel elements are the products
  omega_i |-> K_i(B^+) * K_i(B^-) (the RATIO in cross-conjugation exponents,
  since internal B^+ conjugation gives q^{+a} while the B^--side cross acts
  compatibly only for the product); in particular the paper's assignment
  Phi(c_ii) = K_i^{-1} (s_ii) makes Phi(omega_i) = K_i^+ (K_i^-)^{-1}, whose
  centrality follows only after the anti-identification bookkeeping - which
  the paper never performs. The quotient by b_ii c_ii - 1 ANTI-identifies
  the two Cartan lattices (K_i of B^- gets identified with K_i^{-1} of B^+,
  consistently with the cross-conjugations q^{pm a}); the fate of
  Omega = prod K_i and the rank of the surviving Cartan lattice must be
  re-derived and reconciled with the target U_q(sl(n)).
The whole of SS4 is built on the false Lemma 1.2 and must be rewritten.

### A3 (BLOCKING). Definition 2.1 does not define S_n(B*); well-definedness of Phi is never proved

- The problem's central object is introduced via "we take the following
  concrete presentation as our definition; that it is the bigon surface
  algebra is the content of the standard construction". This defers the
  entire input side of Part 1 to an unstated external theorem (AC-2 negative
  test, verbatim). Either state the identification theorem precisely (name,
  hypotheses, conclusion, in the paper's notation) or declare S_n(B*) to be
  the presented algebra in one honest sentence.
- (MX) is literally undefined: the placeholder "(diagonal arc factors)_{arc
  form}, spelled out as (MXg) below" refers to an equation in H that is never
  translated back to arc generators; the constants in (MXg)
  (q^{a_l(i+1) - 2a(i+1,l)} etc.) are never derived and mix the charts
  a_{ij} / a_r(i).
- Relation (A)'s fourth family has the tautological condition "i<k, l<j with
  the interlacement i<k<l<j"; the higher generators t_{i,i+2} = ... are
  justified by "etc." and "(H2)-(H3)" hand-waving; Proposition 3.1 admits its
  displayed commutation is the RECIPROCAL of (A) and patches it with "our q
  is the inverse of the RTT parameter - harmless", a mid-paper parameter swap
  never carried through (H1)/(MX).
- Since Prop 3.3 (A1) and Lemma 1.2 (A2) are false as stated, Theorem 3.1's
  well-definedness proof ("the mixed relations hold by Lemma 1.2 and
  rescaling to (H2)") is void even granting the presentation.

### A4 (BLOCKING for Part 2). Theorem 4.2 is circular; Lemma 4.2 is internally contradictory

- Thm 4.2 Step 2 concludes by "same generators and relations as
  U_q(sl(n)) = H/(Omega - 1), which is the content of Lemma 4.1". Lemma 4.1
  concerns the double D, not S/I; the bridge is the phrase "transporting
  through the PBW identification" - exactly the missing deduction. The
  intended proof exists (Lemma 4.2 factorization + omega_i = w_i + the
  anti-identification of A2) but is nowhere written.
- Lemma 4.2 states d_i(c_jj) = -delta_ij, then mid-proof "take instead
  d_i(c_jj) = +delta_ij": with the stated signs Upsilon(omega_i) = w_i^0 = 1,
  so the stated Upsilon cannot be an isomorphism; the lemma as printed is
  false and self-corrected only inside its proof.
- Centrality of omega_i in S is asserted and then never proved (it is
  circular to read it off Phi when Phi(omega_i)-centrality in D is precisely
  what requires the A2 bookkeeping).

=====================================================================
## B. MAINLINE GAPS (vs plan ACs)
=====================================================================

- G1 (AC-1): Part 1 not established (A1, A2, A3). Part 2 not established
  (A2, A4). Neither numbered problem statement is currently proved.
- G2 (AC-2): sole external input ("standard construction") unstated - see A3.
- G3 (AC-3): constant/sign audit failed at the single most delicate point
  (A1); scratch asserted rather than computed the decisive relation; the
  q-vs-q^{-1} RTT quip in Prop 3.1 is a second unaudited constant issue.
- G4 (AC-4): currently presents a false derivation as proved; honest repair
  exists and is specified below.
- G5 (AC-5): OK (6 pages, standard packages, compiles clean). Preserve.

=====================================================================
## C. QUEUED SIDE ISSUES (do NOT take over next round)
=====================================================================

- Q1. scratch/ build artifacts and experiments unignored; tidy before final
  submission only.
- Q2. q vs q^{-1} RTT orientation (already tracked); resolve inside A3's
  rewrite, do not spend separate effort.
- Q3. BitLesson BL-20261003-skew-pairing-bookkeeping must be UPDATED (not
  left as-is): the real lesson is - S vs S^{-1} in the cross formula is a
  different algebra; Delta^2(E)'s first tensorand is E (EK appears only in
  the OTHER iterated-coproduct bracketing, and only after coassociativity is
  applied with care); S(F) = -KF and S^{-1}(F) = -FK; never hard-code the
  desired [E,F] then claim the SK computation "verified" it.
- Q4. Label hygiene ((conj)/(CJ) tag clash, "(MXg)" forward reference) -
  normalize while editing; no functional impact.

=====================================================================
## D. IMPLEMENTATION PLAN FOR ROUND 1 (directive; execute in order)
=====================================================================

Objective: make Part 1 true and proved; deduce Part 2. ~2 pages net change.
Do not touch plan/AGENTS/state files.

D1. Cross-relation repair (fixes A1, A2).
  1. SS1: replace (SK) by psi(y,x') = <S(x'_1),y_1> x'_2 y_2 <x'_3,y_3>;
     fix Delta^2(E) display (first tensorand E); fix S(F) = -KF and
     S^{-1}(F) = -FK; recompute Lemma 1.1(c),(d) under the final convention
     (values change; keep only what is used).
  2. Delete the "E <-> -F sign convention" sentence.
  3. Rewrite Prop 3.3 as the two-channel computation giving
     [E_i,F_l] = delta_il (K_i - K_i^{-1})/(q - q^{-1}); add the one-line
     pairing/(H1) compatibility check noted in A1.
  4. Replace Lemma 1.2 by the true statement: for g grouplike in B^- and
     y in B^+, psi(y,g) is a single q-power times gy (cross-conjugation);
     compute psi(E_r, K_j) = q^{a_r(j)} K_j E_r and the mirror
     psi-values for F_r and for grouplikes of B^+ versus B^- elements.
  5. Cartan bookkeeping: prove omega_i |-> K_i(B^+) K_i(B^-) is central in D
     (cross-conjugation exponents cancel for the product); state that the
     quotient by b_ii c_ii - 1 anti-identifies the two Cartan lattices;
     determine Omega and the residual Cartan lattice explicitly.
D2. Presentation + well-definedness (fixes A3).
  1. Definition 2.1: complete presentation - full RTT lists including
     |i-j| >= 2 via quantum minors (one nontrivial verification carried
     out); every mixed relation per generator pair in closed form computed
     from (P) and D1.4; no "(arc form)" placeholders; resolve the
     q-exponent orientation (A) vs Prop 3.1 once, in one displayed line.
  2. Choose Phi-normalizations (placement of Cartan factors in t_{i,i+1},
     s_{i+1,i}, and s_ii) so that (A),(B), the mixed relations, AND
     omega-centrality (D1.5) all hold simultaneously; verify each relation
     family in one displayed computation per family.
  3. Theorem 3.1: well-definedness = itemized check list of D2.1-2;
     injectivity via the existing PBW argument (sound as written).
  4. One honest sentence on S_n(B*) = the presented algebra (or a precisely
     stated external identification theorem). No "standard construction".
D3. Part 2 (fixes A4).
  1. Restate Lemma 4.2 once, consistent grading; prove via PBW refinement.
  2. Theorem 4.2: S/I = (D tensor C[Z^n])/(w_i - 1) = D/(omega_i - 1)
     transported, = U_q(sl(n)) via D1.5's anti-identification and Omega
     bookkeeping. Remove the circular Lemma-4.1 citation chain and the
     (QT)/(conj) presentation-chasing (optional remark at most).
D4. Housekeeping.
  1. Goal tracker: keep Part-1/Part-2 Active until D1-D3 verified; log
     plan-evolution entry "cross relation S vs S^{-1} repaired; Lemma 1.2
     replaced by cross-conjugation; Part-2 Cartan story rebuilt".
  2. BitLesson: Action update per Q3.
  3. Recompile; <= 16 pages; commit with a message naming the sign repair.

=====================================================================
## E. GOAL-TRACKER / SUMMARY DISCREPANCIES (handled by reviewer)
=====================================================================

- Tracker row "AC-1 both parts addressed ... pending review" was premature;
  reviewer reset Part-1/Part-2 and the pairing/cross-computation tasks to
  Active, and added A1/A2/A3/A4 as Blocking Side Issues.
- Plan Evolution Log line about "explicit SK channel computations
  (scratch/double3.py verification)" corrected: double3.py ASSERTS the
  H1-compatible EF rule; it does not derive it from its (SK) implementation.
- No forgotten plan items; capability map N/A; no scope drift.

Reviewer verdict: NOT complete. Round 1 must execute Part D.
