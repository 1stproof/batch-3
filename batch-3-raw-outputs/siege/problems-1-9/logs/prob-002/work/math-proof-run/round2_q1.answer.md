# round2_q1: upper bound via plug-in transport estimator

## Answer (conjectured rate)
The minimax rate, up to log factors, is n^{-2alpha/(2alpha+d+3)}. The lower bound is the one proved in round 1; I have not re-checked it here. The upper bound is **NOT PROVED** in this round. What follows is a check of the planner's route, with the gaps stated precisely.

## Checks of the planner's steps (sketches, not full proofs)
1. **Identities (I1)-(I4).** I verified these by direct differentiation. For (I3): div(f grad hat u) = 1 + div(f grad e) and T_{hat V} hat f = 1, so T_{hat V}(hat f - f) = -div(f grad e). Uniqueness of the bounded solution then gives (I3).
2. **Variance (a).** The heuristic count is consistent with the spectral count. On the line measure mu_x, the two transverse derivatives each cost 2^J, and the tube has density 2^{J(d-1)}. This gives E|.|^2 <~ n^{-1} 2^{J(d+3)}. There is a gap near the source: the ray weight rho^{d-1}/|x|^d is integrable, but differentiating across the ray close to the source x_J costs |x - x_J|^{-1} per derivative. Integrating that against the radius gives at most a log factor when d >= 2. This is a sketch, not a proof.
3. **Bias (b), interior.** The commutator argument works when the kernel has vanishing moments of order >= 2. It gives ||T_{V_J}^{-1} div([f,K_J]V)||_2 <~ 2^{-J alpha}. Near the sphere (point 2) the commutator identity fails. Rays cross the layer of width 2^{-J} transversally, and T^{-1} of a term of size 2^{-J(alpha-1)} supported on that layer contributes at most 2^{-J(alpha-1)} times the layer width 2^{-J}, i.e. about 2^{-J alpha} pointwise. This bound needs ||grad b||_{C^1} <~ 2^{-J(alpha-1)} in the layer, which a boundary-corrected local polynomial smoother of order > alpha+1 gives. Not written in full.
4. **Remainder (c), point 1.** If alpha < 2, the field V_J has C^2 norm about 2^{J(2-alpha)}. Then the H^1 bound for T_{V_J}^{-1} picks up a factor 2^{J(2-alpha)}. The remainder estimate is still o(2^{-J alpha}) provided (2alpha-1)/2 > 2-alpha, i.e. alpha > 5/4. For 1 < alpha <= 5/4 the route needs a repair, for example sample splitting so that the remainder is a product of independent factors. That repair is not done.
5. **Uniformity and the bad event (point 4).** The bad event, where ||grad xi||_{C^1} is not small, has probability exp(-c n^{c'}). Since the estimator is truncated to [1-r, 1+r], the bad event contributes O(exp(-c n^{c'})) to the risk. All other constants depend only on (alpha, d, r).

## Status
- **Proved earlier, not re-checked here:** the lower bound c n^{-2alpha/(2alpha+d+3)} (round 1).
- **Upper bound: NOT PROVED.** I believe it holds with rate n^{-2alpha/(2alpha+d+3)}(log n)^K. Remaining gaps, as precise lemmas:
  - **(G1)** sup_x E|T_{V_J}^{-1} div(f grad xi)(x)|^2 <~ n^{-1} 2^{J(d+3)} J, uniformly over F(alpha,r), including near the source.
  - **(G2)** The bias bound ||f_0 - f||_2 <~ 2^{-J alpha} in the boundary layer.
  - **(G3)** The remainder estimate for 1 < alpha <= 5/4.

=== END OF ANSWER round2_q1 ===
