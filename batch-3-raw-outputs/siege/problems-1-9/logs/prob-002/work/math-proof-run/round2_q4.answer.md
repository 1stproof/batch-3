# round2_q4: upper bound via sample splitting and a one-step correction

## Status: NOT PROVED (I give a partial check and name the exact gaps)

**Target statement.** There is an estimator with sup_{F(alpha,r)} E||hat f - f||_2^2 <= C n^{-2alpha/(2alpha+d+3)} (log n)^K.

### What I checked
1. **Independence after splitting.** Y_1 and Y_2 are independent and each has noise level sqrt2 n^{-1/2}, because Cov(W+W', W-W') = I - I = 0 and both are Gaussian. This is correct, so conditionally on Y_1 the second term of the decomposition is a centred Gaussian linear functional of W.
2. **Exact decomposition.** By (I2) with v = tilde u, the quantity hat f - f splits into three parts:
   - the bias (P_J - I)f;
   - the linear term P_J T^{-1} div(tilde f grad(u_f - hat u_2));
   - a quadratic remainder P_J T^{-1} div((tilde f - f) grad(tilde u - u_f)).

   This follows by subtracting the identity from the estimator's definition. It is correct as an algebraic identity.
3. **Bias.** ||(P_J - I)f||_2^2 <~ 2^{-2J alpha}. This holds for a wavelet or spectral projection on D with a boundary-adapted basis.
4. **Quadratic remainder bookkeeping.** Suppose the pilot achieves rates eps_0 (sup norm), eps_1 (C^1) and eps_{-1} (W^{-1}). Then the remainder is of size eps_1^{3/2} eps_{-1}^{1/2} + eps_0 eps_1, up to the operator norm of T^{-1} on L^2, which is bounded.

   The pilot comes from least squares with the isotropic stability estimate, rate rho = n^{-(alpha-1)/(2alpha+d+2)} in L^2. Interpolating with the C^alpha bound gives:
   - eps_s ~ rho^{(alpha-s)/alpha} for s = 0, 1;
   - eps_{-1} ~ rho^{(alpha+1)/alpha}.

   This makes the remainder of order rho^{2 - 1/alpha}, roughly. That is not below the target n^{-alpha/(2alpha+d+3)} for alpha close to 1. Iterating needs the one-step output to have improved C^1 and W^{-1} rates. Those rates follow from L^2 rates by interpolation, but only after projecting back onto F(alpha,r). Projection in C^alpha onto a ball does not preserve L^2 rates without a further argument.

   So the iteration closes only when the following lemma holds.

### Remaining gaps (precise)
- **Gap A (variance lemma).** For the fixed C^alpha field tilde V close to x/d, conditionally on Y_1:

  E||P_J T_{tilde V}^{-1} div(tilde f grad K_J W)||_2^2 <~ 2^{J(d+3)} polylog.

  This needs a regularisation of T^{-1} near the source x_tilde. There the backward ray integrals concentrate, and the representer is not in L^2 when d <= 4. The heuristic count (a tube of radius 2^{-J} and two transverse derivatives) gives 2^{J(d+3)}, but I have not proved it.
- **Gap B (smoothing bias).** ||T^{-1} div(tilde f grad(K_J u_f - u_f))||_2 <~ 2^{-J alpha}. The naive bound only gives 2^{-J(alpha-1)}, because one derivative is lost across the flow. The commutator structure suggested in the task is needed and has not been verified.
- **Gap C (iteration).** One-step outputs must again lie in F(alpha, r') with sup, C^1 and W^{-1} rates improved by a fixed power. This needs a rate-preserving projection.

### Conclusion
- The lower bound n^{-2alpha/(2alpha+d+3)} is from round 1 of this run; I did not re-check it here.
- The answer the run is conjecturing for the minimax rate is n^{-2alpha/(2alpha+d+3)}, up to logarithmic factors.
- The upper bound is **NOT PROVED**. The best rate actually proved for an upper bound is n^{-2(alpha-1)/(2alpha+d+2)}, from least squares; this is the "known insufficient route" in the background. Gaps A, B and C are the open questions.

=== END OF ANSWER round2_q4 ===
