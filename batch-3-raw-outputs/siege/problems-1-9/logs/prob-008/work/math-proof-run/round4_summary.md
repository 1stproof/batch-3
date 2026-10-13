# Running summary after round 4 planning (rounds 1-3 folded in)

## Problem
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN). No complete proof exists. Main line: GH => (V) smooth invariant volume => H => zero entropy, where the last arrow is proved except in the "non-hyperbolic" case.

Conventions: nu a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds = log of the nu-Jacobian of g_t at x; I = space of X-invariant distribution densities; H = smooth invariant volume omega + unique ergodicity + every omega-mean-zero smooth f is Xu with u smooth, with tame estimates.

## Standing results (never dropped)
- S1 (#2, round1_q2; also round1_q1): ker X on D' = constants.
- S2 (#3, round1_q2 H^r form, round1_q1 C^k form): ||u - mean||_{C^k} <= C||Xu||_{C^m}; X(C^inf) closed, = annihilator of I; X: C^inf_0 -> X(C^inf) topological isomorphism.
- S3 (#4, round1_q2; refined round2_q4 Observation P): no periodic orbit whose Poincare map has Jacobian 1.
- S4 (#8, round2_q1 P1): at a zero p, d(p) != 0.
- S5 (#5, round1_q3; round2_q3 P2): under H, unstable-leaf formula u(x)-u(y) = int_{-inf}^0 (f(g_t x)-f(g_t y))dt, bound C||f||_{C^m} d(x,y). Not on the current line.
- S6 (#9, round2_q3; round2_q2 Prop S): under H, uniformly bounded ergodic integrals; sigma_f([-eps,eps]) <= C eps^2 ||f||^2_{C^m}; zero Green-Kubo variance. Not on the current line.
- S7 (new ledger line, round3_q1 §1): N1 Lebesgue ergodicity (invariant Borel sets null or conull); N2 conservativity (dim >= 2); N3 measurable regularity (L^1 solutions of Xu = f, f smooth, are smooth; an a.c. invariant measure rho nu with log rho in L^1 gives V); N4 V <=> d - c in X(D') <=> d - c in C^m-closure of X(C^inf) <=> T(d) = cT(1) for all T in I.
- S8 (new, round3_q1 §2(a)): an a.c. invariant probability rho nu with rho^{-eps} in L^1 for some eps>0 gives V (in particular density bounded below).
- S9 (new, round3_q1 §2(b)): dim M >= 2: no zero or periodic orbit that is a Lyapunov-stable attractor/repeller with open basin (no hyperbolic sinks/sources, no attracting/repelling periodic orbits). Saddles not excluded.
- S10 (new, round3_q2 Lemma A; round3_q4 Setting): V <=> dim I = 1; V => (with S1, S2) unique ergodicity, no zeros, no periodic orbits (dim >= 2), cohomology-free with tame estimates, i.e. V => H.
- S11 (new, round3_q4 Steps 1-3 + Corollary): under GH + smooth invariant volume omega: h_top = h_omega (UE + variational principle); h_omega = sum of positive exponents (Pesin, cited); if omega has no zero transverse exponent then h_omega = 0 (Katok's horseshoe theorem for C^{1+alpha} flows, cited from memory: positive-entropy hyperbolic ergodic measure gives periodic orbits, excluded by S10); hence zero entropy when dim M <= 3. This is a complete solution of the special case "GH + V + dim M <= 3".
- S12 (new, round3_q3 Lemma R): under H, every orbit segment of length >= C eps^{-m-n} meets every eps-ball. Not on the current line (shown insufficient: minimal UE subshifts with positive entropy have polynomial return times).

## Dead ends (refuted statements only)
- (F2) "under H, x -> int_0^T f(g_t x)dt is Lipschitz uniformly in T" is false as an argument tool: the identity gives Lip <= Lip(u)(1 + Lip(g_T)), not uniform (round3_q3 §1). The route "direction (i)" built on F2 is dead by that refutation.

## Set aside, not refuted (open to re-attack)
- Naive tame estimate vs derivative growth (loses derivatives: ||f o g_s||_{C^m} ~ e^{mLs}; round1_q3/q4, round2_q3 dead end 4).
- Spectral route (M) (#10, round2_q2): smooth observables need not see the Lebesgue spectrum quantitatively; unproved.
- One-point discrepancy / return times (round3_q3 §2): compatible with positive entropy (subshift example), so cannot alone work.
- Local invariant functions at hyperbolic periodic orbits (round3_q3 §3): cut-offs singular along W^u.
- Local analysis at zeros/periodic orbits for V (round2_q1, round2_q4): dissipative saddles have no local obstruction.
- Nonsingular ergodic theory for V (round3_q1): truncations, mollification, time changes, dual estimate, averaging all failed; GH gives no handle on the transposed operator X + d.
- Microlocal route for V (round3_q2): commutator/propagation construction is circular (needs bounded Jacobian cocycle = V).
- Martingale construction of non-smooth solutions under H (round3_q4 (i)): yields the smooth solution itself.

## Diagnostics
- D1: closed range / tame estimates alone cannot give zero entropy (Anosov flows). Need range = all mean-zero (UE + volume) or GH on non-smooth objects.
- Under H, GH <=> ker_{D'} X = constants (a non-smooth u with Xu = f smooth gives u - v in ker X with v smooth, Xv = f).
- UE alone insufficient (minimal UE positive-entropy systems exist).
- Literature recollections by workers (uncertain): Forni 2008 (GW and Katok conjectures in dim 3), Kocsard 2009; one worker recalls Forni proving GH => smooth invariant volume + UE in general, but nobody could reconstruct it. Do not accept "open" as verdict.

## The chain and the missing statement

**Chain.** (Ledger numbers refer to ledger.md plus this round's block: #2 = L1, #3 = L2/closed range, #11 = N1-N4, #12 = S8, #14 = Lemma A / O2, #15 = round3_q4 hyperbolic case and dim <= 3, #16 = non-hyperbolic core lemma, OPEN; #19 = (V), OPEN.)
1. (Missing statement, #19) GH => X preserves a smooth positive density omega.
2. By #14 (with #2, #3): the flow is uniquely ergodic with invariant measure omega, X has no zeros and (dim M >= 2) no periodic orbits, and every omega-mean-zero smooth f is Xu with u smooth (tame estimates), i.e. H holds.
3. By #15: h_top(g_1) = h_omega(g_1) = sum of positive transverse exponents of omega (variational principle + UE; Pesin), and h_omega = 0 whenever omega has no zero transverse exponent (Katok's horseshoe theorem for flows, cited, contradicts "no periodic orbits"); so the GOAL holds when dim M <= 3 (and trivially dim M = 1).
4. What still remains after (V): #16 (OPEN, round3_q4): under GH + smooth invariant volume, omega cannot have a positive exponent together with a zero transverse exponent. With #16, step 3 gives h_omega = 0 always, hence h_top = 0. So (V) is the strongest intermediate claim the main line needs next; after it, exactly #16 remains.

**Missing statement (V).** Let M be a compact connected smooth manifold and X a smooth vector field on M such that every distribution u in D'(M) with Xu in C^infinity(M) lies in C^infinity(M) (global hypoellipticity, GH). Then there is a smooth density omega on M, positive everywhere, with L_X omega = 0. Equivalently: for one (hence every) smooth positive density nu, div_nu X = Xa for some a in C^infinity(M).

**Why it should hold (planner sketch; Lemmas C, D, E, F are the planner's own, proofs written into the round-4 queries, unverified).**
- Lemma C: under GH (dim M >= 2), for EVERY x, int_R e^{J_t(x)} dt = infinity (otherwise T = int e^{J_t(x)} delta_{g_t x} dt is a finite measure on one orbit with L_X T = d T, so T/nu is a non-constant element of ker X, contradicting #2). Consequences: no orbit from a volume-expanding hyperbolic periodic orbit/zero to a volume-contracting one; in a horseshoe all periodic orbits have int_gamma d of one strict sign.
- Lemma D (Patterson-type): if int e^{J_t(x)-s|t|}dt < infinity for all s>0, the normalised measures e^{J_t(x)-s|t|}dt along the orbit converge weak* to nu/nu(M) as s -> 0 (the limit T has L_X T = dT, so T/nu is in ker X). Corollary: every ergodic mu with mu(d) = 0 has full support. So GH already gives "unique ergodicity of the Jacobian-weighted averages"; (V) is the same statement for the transposed operator.
- Lemma E: if the flow is UE with measure mu then mu(d) = 0 (J_t/t -> mu(d) uniformly, while int e^{J_t} dnu = nu(M)); with D the flow is minimal; then by Gottschalk-Hedlund + #12, (V) <=> sup_t |J_t(x0)| < infinity for one x0.
- Lemma F: (V) <=> X + d (acting on functions) is GH (the formal adjoint of a GH field is GH).
- Proposed mechanism: (a) GH => UE: two distinct ergodic measures (or one with mu(d) != 0) should, via Pesin stable/unstable manifolds and Lebesgue ergodicity (#11), yield a finite measure on a family of orbits with L_X T = dT (generalised Lemma C) or force a positive-measure invariant set; (b) GH + UE => bounded J along one orbit, by a Patterson construction along an orbit where J is unbounded, choosing weights that make T_s - (weighted average) converge to a measure T != c nu with L_X T = dT. Alternatively prove Lemma F's right side directly (closed range of X + d on C^infinity via duality with the closed range of X).

**Tried so far (on (V) and its earlier wording #6).**
- round1_q1, round1_q2: posed (V) as the missing lemma; noted it needs GH of the transpose X + d; no attack.
- round2_q1: local analysis at zeros/periodic orbits -> P1 (#8), resonance sketch; no global information.
- round2_q4: periodic orbits -> Observation P (#4 refined).
- round3_q1: nonsingular ergodic theory (Maharam, Krieger type, ratio ergodic theorem) -> verified N1-N4 (#11), S8 (#12), no attractors (#13); gap: no handle on X + d.
- round3_q2: microlocal propagation / commutator -> Lemma A (V <=> dim I = 1, #14); circular.

## Where the next round should concentrate (round 4 wave)
Progress test: rounds 2 and 3 produced no progress on the chain in the strict sense — main line stalled — no universal progress (round3_q4's hyperbolic-case result narrows the downstream core to #16; round3_q1/q2 give equivalent reformulations of (V)). What differs now: the missing statement is fixed as (V) with the planner's new mechanism (conformal/Patterson measures, Lemmas C-F, UE + Gottschalk-Hedlund reduction) instead of local, microlocal or Maharam-extension lenses.
Wave (escalation rule): q1-q3 identical closing task on (V); q4 refutation attempt of (V) exactly as stated; q5 bare task (statements only, new first move); q6 the conformal/Patterson approach continued from Lemmas C-D; q7 hardest sketch step "GH => unique ergodicity"; q8 hardest sketch step "GH + UE => (V)" (bounded Jacobian orbit / invariant distributions of positive order); q9 the transpose route "X + d is GH / has closed range" (Lemma F); q10 (one query elsewhere, the only other open link) the non-hyperbolic core #16.
Next round: if (V) is proved, audit it (it is load-bearing) and give #16 the escalation treatment as the new missing statement; if Lemmas C-F are confirmed by workers, record them as PROVED.
