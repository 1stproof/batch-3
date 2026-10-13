# Running summary after round 3 planning (round 1 and 2 results folded in)

## Problem
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN). No proof of the goal exists yet; no step of the main chain beyond the functional-analytic preliminaries is proved.

## Established
- L1 (round1_q2; ledger #2): ker X on D' = constants (GH + level-set indicator argument).
- L2 (round1_q2 H^r form, round1_q1 C^k form; #3): ||u - mean||_{C^k} <= C||Xu||_{C^m}; X(C^inf) closed, X: C^inf_0 -> X(C^inf) topological isomorphism; X(C^inf) = annihilator of invariant distribution densities I.
- #4 (round1_q2), refined in round2_q4 (Observation P): no periodic orbit whose Poincare map has Jacobian 1 (via changing nu so that div vanishes on the orbit, then mu_gamma/nu' in ker X). Dissipative periodic orbits NOT excluded.
- round2_q1 P1 (new ledger line): at a zero p, div_nu X(p) != 0 (delta_p/nu would be in ker X). Sketch (unverified): order-N distributions at p exclude resonances d(p) + sum alpha_i lambda_i = 0. Linear sources/sinks excluded by homogeneous invariant functions (round 1 notes, not re-verified).
- #5 (round1_q3) / round2_q3 P2: under H, for y on the unstable manifold of x, u(x)-u(y) = integral_{-inf}^0 (f(g_t x)-f(g_t y)) dt, bounded by C||f||_{C^m} d(x,y).
- round2_q3 (new ledger line), under H: P1 uniform bounded ergodic integrals with tame constant; P3 derivative cocycle identity du(Dg_t v) = du(v) + integral_0^t df(Dg_s v) ds; P4 f = X^j u_j for all j, so sigma_f vanishes to infinite order at 0.
- round2_q2 Proposition S, under H: ||P_eps f|| <= C eps ||f||_{C^m} (spectral projection of A = -iX); zero Green–Kubo variance of all smooth observables.
- Hyperbolic case (round1_q3, citing Katok/Lian–Young closing for flows): under H, if omega's only zero exponent is the flow direction, positive entropy contradicts UE.
- Reduction (round1_q3): under H, h_top = h_omega = integral of positive exponents.

## Planner observations (elementary, sent to workers in round 3 for checking; NOT yet verified)
- O1 dual estimate; O2: smooth invariant volume => all invariant measures equal it => UE, no zeros, no periodic orbits, cohomology-free with tame estimates (this is "H"); O3: V <=> d = div_nu X in R + X(C^inf); O4: GH invariant under time change, sign, conjugation by e^a.
- N1 (new): GH => every Borel set B with g_t B = B is Lebesgue null or conull (1_B in ker X). So the flow is ergodic for Lebesgue measure class.
- N2 (new): hence conservative (Hopf decomposition; totally dissipative ergodic would be carried by one orbit), dim >= 2. No invariant open set of non-full volume; no attractor with basin of positive non-full volume.
- N3 (new): measurable Livsic regularity: any L^1 (distributional) u with u o g_t - u = integral_0^t f o g_s, f smooth, is smooth. In particular an a.c. sigma-finite invariant measure rho nu with log rho in L^1 gives V.
- N4 (new): V <=> d - c in X(D') <=> d - c in C^m-closure of X(C^inf) <=> Jacobian cocycle J_t is an L^1 measurable coboundary. mu(d) = sum of exponents of ergodic mu; V forces it 0 for all mu.
- Under H, GH <=> cohomology-free (CF): so under H, GH on distributions gives no information beyond CF except the measurable regularity N3 and N1.

## Diagnostics (constraints on any proof)
- D1: tame estimate / closed range alone cannot give zero entropy (transitive Anosov flows have closed range). Must use range = all mean-zero (UE + volume), or GH on non-smooth objects.
- D2: single-pair bump strategy loses derivatives (needs m < L/lambda).
- Spectral: vanishing of sigma_f at 0 (even to infinite order) is consistent with a Lebesgue-spectrum component (round2_q3 dead end 1); the needed statement (M) (round2_q2) is a quantitative "smooth observables see Lebesgue spectrum", unproved.
- Single-pair Lipschitz bound P2 is O(d(x,y)) consistent with expansion (round2_q3 dead end 2); P3 tautological for exact forms (dead end 3).
- UE alone insufficient (minimal UE positive-entropy systems exist).
- Asymptotic-pair distributions need smooth families of pairs; Pesin holonomies only absolutely continuous (round2_q4 R2).
- Literature (recalled by workers, uncertain): Greenfield–Wallach / Katok conjectures; Forni 2008 and Kocsard 2009 (dim 3); possibly "GH => CF" in Forni; no worker recalls a general proof of zero entropy. Do not accept "open" as a verdict.

## Dead ends
- Naive tame-estimate vs derivative growth (round1_q3/q4, round2_q3 dead end 4).
- Linearised leaf distributions, forward ergodic integrals (round1_q3).
- Local analysis at zeros/periodic orbits does not reach V (round2_q1, round2_q4): dissipative saddles have no local obstruction.

## Open gaps (the chain)
Chain: GH => (a) V => H (by O2) => (b) omega has no positive exponent => h_top = 0.
(a) V (ledger #6): GH => smooth invariant volume. Reduced (N3/N4, unverified) to existence of an a.c. invariant measure with log-density in L^1.
(b) Core (ledger #7): under H (+GH) no positive exponent, including zero transverse exponents. Possible sub-routes: (M) (new OPEN line); uniform polynomial discrepancy (round2_q3 Q1); pure point spectrum/equicontinuity (round2_q3 Q2); measurable regularity N3 + Pesin structures.

## Round 3 wave (4 attempt queries)
- q1: V via nonsingular ergodic theory (N1-N4, Maharam extension, Krieger type, ratio ergodic theorem).
- q2: V via microlocal/analytic lens (WF sets of invariant distributions, commutator construction, transpose, excluding obstructions).
- q3: core via quantitative recurrence/combinatorics (uniform discrepancy F1, uniform Lipschitz ergodic integrals F2, Brin–Katok, Kushnirenko).
- q4: core via smooth ergodic theory using N3 (measurable regularity), Pesin unstable lamination, Ledrappier–Young, martingale constructions.

## Next round should concentrate on
Round 4 is the escalation round. If round 3 proves V, verify it (load-bearing) and focus on (b). If (b) stays blocked, identify the single missing statement precisely (most likely: "smooth volume, UE, CF with tame estimates => zero exponents" or (M)) and give it the escalation treatment. If N1-N4 are confirmed, record them in the ledger.
