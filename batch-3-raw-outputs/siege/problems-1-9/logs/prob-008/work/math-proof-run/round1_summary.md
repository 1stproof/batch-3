# Running summary after round 1 planning (no results yet)

## Problem
X smooth vector field on compact connected M, globally hypoelliptic (GH): every distribution u with L_X u in C^infinity is smooth. Show the flow g_t has zero topological entropy. Goal = ledger [GOAL] line (OPEN).

## Established
Nothing yet (round 1; no result files).

## Planner's own preliminary analysis (NOT established; to be checked by workers)
Conventions: "distribution" = generalized function, dual of smooth densities; L_X u defined by <L_X u, rho> = -<u, L_X rho>.
Expected structural consequences of GH (classical-looking; status unverified):
1. ker(X) on D' = constants: ker is inside C^infinity, closed graph + compact Sobolev embedding gives finite dimension; a nonconstant smooth invariant F would give infinitely many invariants phi(F). Connectedness gives constants.
2. Peetre-type estimate ||u - mean||_{H^s} <= C ||Xu||_{H^{k(s)}}, hence X has closed range on C^infinity.
3. Hoped: invariant distribution densities are 1-dimensional, spanned by a smooth positive volume omega with div_omega X = 0. Sketch idea: if div X is in range(X)+const then e^{a} * (mu/omega) lies in ker = constants. Not yet proven; also "X has no zeros" not yet proven (needed? a zero p gives the invariant measure delta_p).
4. If 3 holds: flow uniquely ergodic w.r.t. smooth volume, minimal; every zero-mean smooth f = Xu with u smooth and tame estimates (cohomology-free); dually ||w - mean||_{(C^{k})'} <= C ||Xw||_{(C^{s})'} for distributions w (transposed open-mapping estimate). No periodic orbits if dim M >= 2 (orbit measure would be a second invariant measure). dim M = 1: entropy trivially zero.
5. Then h_top = h_vol (variational principle + UE) <= integral of positive exponents (Ruelle). If the volume is hyperbolic (only the flow direction has zero exponent) Katok's closing/horseshoe theorem for flows gives periodic orbits, contradiction. Genuine difficulty: positive entropy with additional zero exponents (center directions) — UE + no periodic orbits alone does not exclude positive entropy (Herman-type minimal positive-entropy examples), so GH must be used beyond UE.
6. Candidate obstruction construction (planner's idea): for y in W^u(x), w = int_{-inf}^0 (delta_{g_t x} - delta_{g_t y}) dt converges as an order-1 distribution and X w = delta_y - delta_x (sign check needed). If y is close to x (unstable manifold returning near x), Xw is small in (C^1)' (<= d(x,y)), while w tested on a bump of size eps around a "free" segment of y's orbit is ~eps with C^k-norm eps^{-k}; dual estimate then contradicts if d(x,y) << eps^{k+1}. Needs a Pesin-theoretic existence argument; unclear.
7. Spectral facts: GH implies spectral measures of smooth zero-mean f vanish to infinite order at 0; measure-theoretically alone not contradictory with positive entropy; the algebra structure of C^infinity must be used.
Possible literature (from memory, uncertain): Greenfield–Wallach (tori), Hounie (surfaces), Chen–Chi (2000, "Hypoelliptic vector fields and almost periodic motions"), Forni (2008, GW and Katok conjectures in dim 3), Kocsard (2009, Katok conjecture dim 3), Rodriguez Hertz–Rodriguez Hertz (cohomology-free systems and first Betti number). Katok conjecture would give the answer but is open in general.

## Dead ends
None recorded yet. Naive comparisons of tame estimates with derivative growth (u∘g_t, ergodic integrals with slowly varying weights) give no contradiction because of loss of derivatives.

## Open gaps
(a) Rigorous structural lemmas 1-4 (especially 3: smooth invariant volume / unique ergodicity, and nonvanishing).
(b) The dynamical core: GH-structure => zero entropy, including the non-hyperbolic (zero center exponent) case.

## Next round target
Round 1 is exploratory: four independent attempts — (q1) full proof by any route; (q2) the structural lemmas rigorously; (q3) the dynamical core assuming the structure, via Pesin theory / obstruction distributions; (q4) a fresh functional-analytic lens (subexponential derivative growth, rigidity, discrete spectrum, algebra structure).
