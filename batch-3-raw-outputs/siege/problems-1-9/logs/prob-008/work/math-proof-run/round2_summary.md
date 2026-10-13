# Running summary after round 2 planning (round 1 results folded in)

## Problem
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u smooth is smooth. Show the flow g_t has zero topological entropy. Goal = ledger entry 1 ([GOAL], OPEN).

## Established (round 1)
- L1 (round1_q2, also round1_q1, round1_q4 partly): ker X on D' = constants. Proof: u smooth by GH; indicator 1_{u>c} is a D'-limit of H_eps(u-c) in ker X, hence smooth, hence constant by connectedness.
- L2 (round1_q2 in H^r form; round1_q1 in C^k form): for every r there are k, C with ||u - mean||_{H^r} <= C||Xu||_{H^k} (resp. ||u||_{C^k} <= C||Xu||_{C^m} for nu-mean-zero u). Proof: closed graph theorem on F_s = {u in H^{-s}: Xu smooth} with Fréchet seminorms, then Rellich compactness + L1. Consequence: X(C^inf) closed; X: C^inf_0 -> X(C^inf) topological isomorphism; X(C^inf) = annihilator of X-invariant distribution densities (Hahn–Banach).
- L6-partial (round1_q2): periodic orbit with |det DP| = 1 gives u = c(theta) delta(y) with Xu = 0, contradicting GH.
- Lemma A (round1_q3), assuming smooth invariant volume + UE + cohomology-free (H): for y in W^u(x) (Pesin), integral_{-inf}^0 (f(g_t x) - f(g_t y)) dt = u(x) - u(y), so bounded by C||f||_{C^k} d_M(x,y).
- Hyperbolic case (round1_q3, modulo cited Katok/Lian–Young closing lemma for flows): under H, if omega's only zero exponent is the flow direction, positive entropy gives periodic orbits, contradicting UE.
- Reductions (round1_q3): under H, h_top = h_omega = integral of positive exponents (variational principle, Pesin formula).

## Planner observations (elementary, recorded in round-2 queries as O1–O4; to be confirmed by workers)
- O1 dual estimate: for T in (C^k)' with T(1)=0 there is S in (C^m)' with S(Xu) = T(u), ||S|| <= C||T||. For points: S_{x,y} with norm <= C d(x,y).
- O2: if X preserves a smooth density omega, any invariant probability mu gives v = mu/omega with Xv = 0, so mu = omega by L1. Hence a smooth invariant volume immediately gives UE, minimality, no zeros, no periodic orbits, cohomology-free with tame estimates. So "GH => smooth invariant volume" (call it V) is THE structural step.
- O3: V <=> div_nu X in R + X(C^inf) <=> T(d) = c T(1) for all invariant distribution densities T.
- O4: GH invariant under time change, sign, conjugation by e^a.
- Zeros: distributions supported at p of order <= N form finite-dim space preserved by X; kernel there (e.g. delta_p if div X(p)=0) violates GH; linear sources/sinks violated via degree-0 homogeneous functions. Saddle periodic orbits: P-invariant functions singular along whole W^s/W^u, so no local obstruction.

## Diagnostics (important constraints on any proof)
- D1: The tame estimate / closed range alone cannot give zero entropy: transitive Anosov flows have X(C^inf) closed (Livsic with tame estimates, recalled) and positive entropy. Any proof must use that the range is ALL mean-zero functions (UE + smooth volume) or GH itself on non-smooth distributions; the needed mechanism is a "distributional closing lemma" replacing periodic orbits in the non-hyperbolic case.
- D2: Loss of derivatives in the single-pair bump strategy (round1_q3 (L)): eps-separation window of backward orbits exists only if delta >= eps^{1+L/lambda}, but contradiction needs delta << eps^{m+1}; works only if m < L/lambda.
- Spectral vanishing of sigma_f at 0 to infinite order is not contradictory with Lebesgue spectrum on its own (round1 notes, round1_q2 bonus).
- Invariant pseudometric sup{|u(x)-u(y)| : ||Xu||_{C^0} <= 1} is invariant but infinite off orbits; C^r version not invariant.
- Minimal/UE systems with positive entropy exist, so UE alone is insufficient (round1_q2).

## Dead ends
- Naive tame-estimate vs derivative growth comparisons (round1_q3, round1_q4): loss of derivatives.
- Linearised leaf distributions w_v, forward ergodic integrals, uniform bounded ergodic integrals: all consistent with exponential growth (round1_q3).

## Open gaps
(a) V: GH => smooth invariant volume (ledger OPEN). Literature recollection: possibly Forni 2008 / Kocsard 2009 ("GH => cohomology-free"); unverified.
(b) Dynamical core: under H (+GH), omega has no positive exponent, including zero transverse exponents (ledger OPEN; open lemma (L) of round1_q3, blocked by D1/D2).
(c) Alternatively a route bypassing (a): rigidity (Glasner–Maon), asymptotic pairs + smoothing families, Yomdin volume growth.

## Round 2 wave (4 attempt queries)
- q1: prove V (structural).
- q2: dynamical core via Pesin/unstable pairs, with D1/D2 constraints and Lemma A inline.
- q3: dynamical core via spectral/ergodic theory (statement S: smooth vol + ergodic + all mean-zero smooth f = Xu with C^0 tame bound => h_omega = 0).
- q4: topological routes without V (uniform rigidity; asymptotic pairs + smooth families; volume growth).

## Next round should concentrate on
Whatever of (a)/(b) moved. If V is proved, verify it (it is load-bearing) and focus all remaining attempts on (b). If (b) stays blocked, consider literature reconstruction and the dimension-3/hyperbolic special case write-up as fallback material, but do not lower the goal.
