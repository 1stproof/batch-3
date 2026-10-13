# Round 1 summary (no results yet; planning only)

## Problem
Minimax L^2-squared rate for recovering f in F(alpha,r) (C^alpha ball of radius r around 1, r small) from Y = u_f + n^{-1/2}W, div(f grad u)=1 on the unit ball, u=0 on boundary, d>=2, alpha>1.

## Goal chosen (ledger [GOAL], OPEN)
Rate = n^{-2alpha/(2alpha+d+3)} up to log factors (lower + matching upper bound). This is the planner's conjecture, NOT the "textbook degree-one" rate n^{-2alpha/(2alpha+d+2)}. If refuted, replace the goal by the correct rate (the problem fixes the question "what is the rate").

## Planner's heuristic (unverified)
- Exact identity: u_g - u_f = -L_g^{-1} div(h V_f), h=g-f, V_f = grad u_f; for f=1, V = x/d (radial, source at 0).
- Perturbations oscillating at frequency lambda in angular directions (perpendicular to V) and smooth radially: div(hV) has no lambda factor, so ||Dh|| ~ lambda^{-2}||h|| (degree 2). Radial oscillation mu: ~ mu lambda^{-2}. Symbol ~ (1+|xi_rad|)/|xi|^2.
- Lower bound by Assouad with 2^{j(d-1)} angular pieces (radial length O(1)) gives n^{-2alpha/(2alpha+d+3)}; isotropic pieces give only n^{-2alpha/(2alpha+d+2)}; bump at source gives a weaker (single-bump) bound.
- Upper heuristic: spectral cutoff variance n^{-1}2^{J(d+3)} vs bias 2^{-2J alpha}; source point integrable for d>=2.
- Ray picture: f solves V.grad f + f Delta u = 1 along flow lines; Delta u enters pointwise (2 derivatives), integration along rays gains one derivative radially.

## Established
Nothing yet.

## Open gaps
1. Rigorous lower bound n^{-2alpha/(2alpha+d+3)} (control of angular part of V_{f_theta'}, dual-norm H^{-2}-type estimate on thin tubes, Assouad).
2. Upper bound: estimator attaining it (plug-in/transport, linearization at pilot, or M-estimator + anisotropic stability). Unclear whether all alpha>1 can be handled.
3. Independent check that the conjectured exponent is right (vs d+2).

## Round 1 wave (4 attempt queries)
q1 lower bound proof; q2 upper bound via plug-in/linearization/transport; q3 adversarial exact computation for f=1 via spherical harmonics + verdict on exponent; q4 stability estimate + M-estimator route.

## Next round should concentrate on
Reading q3 for the verdict on the exponent first; then consolidating whichever half (lower/upper) is closest to complete, attacking the other half's gaps.
