# round1_q2: what GH gives structurally

Notation: GH means: if u ∈ D'(M), f ∈ C^∞ and Xu = f, then u ∈ C^∞. Fix a smooth positive density ω₀ (no invariance assumed). Sobolev spaces H^s are taken with respect to it, and c(u) = ∫u ω₀ / ∫ω₀.

## L1 (proved). ker(X on D') = constants.
Proof. Suppose Xu = 0 with u ∈ D'. By GH, u is smooth. Suppose u is not constant. Choose c with min u < c < max u. Then U₊ = {u>c} and U₋ = {u<c} are nonempty open sets. Take smooth nondecreasing functions H_ε on R with H_ε(t) = 0 for t ≤ -ε and H_ε(t) = 1 for t ≥ 0, and set v_ε = H_ε(u-c). This is smooth and Xv_ε = H_ε'(u-c)·Xu = 0. As ε→0, v_ε → v = 1_{U₊} pointwise and boundedly, hence in L¹, hence in D'. Since X is continuous on D', Xv = 0. By GH, v agrees a.e. with a continuous function w. Then w ∈ {0,1} a.e., hence everywhere by continuity. Since M is connected, w is constant. But w = 1 a.e. on U₊ and w = 0 on U₋, and both sets have positive measure. Contradiction. ∎

## L2 (proved). For every r there are k and C with ||u-c(u)||_{H^r} ≤ C||Xu||_{H^k} for all u ∈ C^∞. Hence X(C^∞) is closed in C^∞.
Proof. Fix s. Let F_s = {u ∈ H^{-s} : Xu ∈ C^∞} with the seminorms ||u||_{H^{-s}} + ||Xu||_{H^j}, j ∈ N. F_s is Fréchet: a Cauchy sequence converges in H^{-s} to u, and Xu_n converges in C^∞ to some g; since X: H^{-s} → H^{-s-1} is continuous, g = Xu.

By GH, F_s ⊂ C^∞. The inclusion has closed graph, because both spaces embed continuously in H^{-s}. By the closed graph theorem for Fréchet spaces (a linear map between Fréchet spaces with closed graph is continuous), the inclusion is continuous. So for each r there are j and C with
(*) ||u||_{H^r} ≤ C(||u||_{H^{-s}} + ||Xu||_{H^j}).

Now fix r > -s, take j large enough that (*) holds both for r and for r+1, and suppose the claimed estimate fails with k = j. Then there are smooth u_n with c(u_n) = 0, ||u_n||_{H^r} = 1 and ||Xu_n||_{H^j} → 0. By (*) at level r+1 (note ||u_n||_{H^{-s}} ≤ ||u_n||_{H^r} = 1), the u_n are bounded in H^{r+1}. By Rellich (H^{r+1} → H^r is compact on a compact manifold), a subsequence converges in H^r to some u with ||u||_{H^r} = 1 and c(u) = 0. Moreover Xu = lim Xu_n = 0 in H^{r-1}. By L1, u is constant, and then c(u) = 0 forces u = 0. Contradiction.

Closed range: suppose Xu_n → f in C^∞. Apply the estimate to u_n - c(u_n): this sequence is Cauchy in every H^r, so it converges in C^∞ to some u, and Xu = f. ∎

Duality consequence: X(C^∞) is exactly the annihilator of the X-invariant distribution densities. Indeed, by Hahn–Banach, a closed subspace of C^∞ equals the annihilator of its annihilator in D'-densities, and that annihilator is {T : L_X T = 0}.

## L3, L4, L5, L6: not established. Gaps stated honestly.
- **L3 (no zeros).** If X(p) = 0, then δ_p is invariant, so every f ∈ X(C^∞) vanishes at p. This does not contradict L2. Scaling test functions φ((x-p)/ε) give ||u_ε - c||_{L²} ~ ε^{n/2} against ||Xu_ε||_{H^k} ~ ε^{n/2-k}, which is consistent with L2. So L2 alone does not exclude zeros. What is needed is a non-smooth u with Xu smooth, built locally at p, and I have not constructed one for degenerate zeros. **Open.**
- **L6 (no periodic orbits), partial.** Let γ be a periodic orbit. Take tube coordinates (θ, y), θ ∈ R/TZ, with X = a∂_θ + b·∂_y, b(θ,0) = 0 and a(θ,0) > 0. For u = c(θ)δ(y), a computation gives
  Xu = [a c' - c (div_y b)(θ,0)] δ(y).
  This vanishes for the periodic choice c = exp∫(div_y b/a) exactly when ∫_γ (div_y b/a) dθ = 0. This integral equals log|det DP| for the Poincaré return map P. So **if |det DP| = 1, then u is a non-smooth solution of Xu = 0, contradicting GH (or L1).** For general γ, one would need a transversal distribution homogeneous under DP. **Open.**
- **L4.** A time change hX with h > 0 smooth preserves GH, since (hX)u = f gives Xu = f/h. But L_X T = 0 written as v = T/ω₀ reads Xv + (div X)v = 0, which is not of GH form. I found no argument that ker L_X^t is one-dimensional or smooth. **Open.** L5 follows from L4 plus L2 together with the duality remark above. Without L4 only the L2 half is proved.

## Bonus: entropy
Zero entropy is not derived here. L1–L6, even with L4 (uniquely ergodic with smooth invariant volume, minimal), do not imply zero topological entropy by themselves. Uniquely ergodic minimal flows can have positive topological entropy (Jewett–Krieger-type constructions, cited from memory), though not with a smooth measure that has positive metric entropy. An additional use of GH, for example the tame estimates of L2 applied to growth of derivatives of the flow, would be needed. **Open.**

=== END OF ANSWER round1_q2 ===
