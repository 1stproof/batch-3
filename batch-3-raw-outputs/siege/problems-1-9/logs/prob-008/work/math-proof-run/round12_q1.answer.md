# round12_q1: answer (partial — (PE0) NOT proved, no counterexample found)

## Plan
Target: (PE0). I (i) checked the chain's logic, (ii) proved a reduction of (PE0) to flow-invariant, flow-ergodic measures (Lemma 1 below; elementary, complete), and (iii) examined both suggested mechanisms and record exactly where each stops. I did not find a proof of (PE0) or a counterexample.

## 1. Chain check
Given Step 1 (variational principle + ergodic decomposition: h_top(g_1) > 0 gives a g_1-ergodic mu with h_mu(g_1) > 0), Step 2 (entry 113: such a mu has int J_1 dmu = 0 under GH), and (PE0) (no such mu exists), the conclusion h_top(g_1) = 0 follows. The logic is sound. I did not re-check entry 113 itself: it relies on Pesin theory and non-stationary normal forms, which I cite and do not re-prove. h_top(g_t) = |t| h_top(g_1), so zero entropy of g_1 is the same as zero entropy of the flow.

## 2. Lemma 1 (proved): reduction to flow-ergodic measures
**Lemma 1.** If mu is g_1-invariant and g_1-ergodic with h_mu(g_1) > 0 and int J_1 dmu = 0, then mu-bar := int_0^1 (g_s)_* mu ds has these properties:
- it is flow-invariant and flow-ergodic;
- h_{mu-bar}(g_1) = h_mu(g_1) > 0;
- mu-bar(d) = 0.

Conversely, a flow-invariant, flow-ergodic mu' with h_{mu'}(g_1) > 0 and mu'(d) = 0 has a g_1-ergodic component with the properties in (PE0). So (PE0) is equivalent to: **no flow-ergodic, flow-invariant mu has h_mu(g_1) > 0 and mu(d) = 0.**

*Proof.*
1. **Flow-invariance.** (g_1)_* mu = mu. Hence (g_r)_* mu-bar = int_r^{r+1} (g_s)_* mu ds = mu-bar, using 1-periodicity of s -> (g_s)_* mu.
2. **Flow-ergodicity.** Let A be a flow-invariant Borel set. Then A is g_1-invariant, so mu(A) ∈ {0,1}. Also (g_s)_* mu(A) = mu(g_{-s}A) = mu(A). Hence mu-bar(A) = mu(A) ∈ {0,1}.
3. **Entropy.** g_s commutes with g_1, so g_s conjugates (g_1, mu) to (g_1, (g_s)_* mu). Therefore h_{(g_s)_* mu}(g_1) = h_mu(g_1) for every s. Entropy of g_1 is affine and satisfies Jacobs' integral formula over integral decompositions into g_1-invariant measures (cited, standard). This gives h_{mu-bar}(g_1) = h_mu(g_1).
4. **Mean divergence.** The cocycle identity gives J_1(g_s x) − J_1(x) = J_s(g_1 x) − J_s(x). The right-hand side is a g_1-coboundary of a bounded function, so its mu-integral is 0. Hence int J_1 d(g_s)_* mu = int J_1 dmu = 0 for every s ∈ [0,1], and so int J_1 dmu-bar = 0. Since mu-bar is flow-invariant, int J_1 dmu-bar = int_0^1 mu-bar(d∘g_s) ds = mu-bar(d). So mu-bar(d) = 0.
5. **Converse.** Take the g_1-ergodic decomposition of mu'. Its components are of the form (g_s)_* m for a single g_1-ergodic m, with s distributed over a circle. By step 3, each has entropy h_{mu'}(g_1) > 0. By step 4, each has the same value of int J_1, which equals mu'(d) = 0. ∎

## 3. Where the two suggested mechanisms stop (no proof obtained)
**Mechanism A (Theorem J applied to su-grid configurations).** Theorem J needs exponential decay of F_phi(t) = S(e^{J_t} phi∘g_t) in **both** time directions.
- On an unstable leaf, backward decay can be produced by cancelling normal-form moments (entry 113).
- Forward decay has to come from the stable direction, through the columns of the grid. For points that are not exactly on common stable leaves, the su-defect δ is a centre displacement. Under g_t it grows subexponentially (zero exponent), but it is not damped.
- Pairing phi∘g_t against two nearby points separated by a centre displacement δ gives a contribution of order ||D(phi∘g_t)|| |δ|. This is O(e^{o(t)}) |δ|, not O(e^{-eps t}).
- Exponential decay would therefore require |δ| ≤ e^{-eps T(r)} on the whole time window, i.e. T(r) ≲ log(1/r)/eps. For the normalised limit S_r → S to be nonzero while the decay holds on [−T(r), T(r)] with T(r) → ∞, the weights must stay bounded in (C^k)' as r → 0.
- The moment-cancelling weights on a cluster of diameter r blow up like r^{-N} (Vandermonde inverse). After normalisation, the defect error becomes r^{-N}·(defect) ~ r^{-N}·r^{1+…}, which is not small for N ≥ 2.
- I could not balance these two effects. This is the same obstruction already recorded as "centre defects not absorbed" (Theorem G, round 7).

**Mechanism B (spectral flatness).** This one is only for the volume case or for L^2(mu).
- GH, through the tame inverse, makes the spectral measure σ_f of every smooth mean-zero f flat to infinite order at 0. Indeed f = X u_1, u_1 = X u_2, …, all smooth, so σ_f(ξ) = ξ^{2j} σ_{u_j}(ξ).
- A contradiction needs a **smooth** f whose spectral density on the Lebesgue (Pinsker-orthocomplement) part does not vanish at 0. For a positive-entropy measure, this is a positive asymptotic variance (CLT-type) statement for smooth observables.
- Such statements are known for (non-uniformly) hyperbolic systems with some mixing rate, e.g. via Livsic-type arguments, which also exclude f with zero variance. These are exactly the cases that are already excluded.
- For non-hyperbolic K-systems with centre directions, I know of no theorem that guarantees a smooth observable with non-degenerate variance. Functions with flat spectral measure at 0 are L^2-dense, so density of smooth functions gives nothing by itself. I could not prove the needed statement.

## 4. Status
- **Proved here:** Lemma 1, the reduction of (PE0) to flow-ergodic flow-invariant measures with mu(d) = 0. This is an equivalent reformulation, not an answer.
- **Checked:** the chain is logically sound given entry 113 and the cited theorems (variational principle, Jacobs' formula).
- **Open:** (PE0) itself, already open in the volume-preserving case: does GH plus a smooth invariant volume imply h_vol(g_1) = 0? The precise open sub-steps are:
  - (A) two-sided exponentially decaying configurations built from nearby stable/unstable leaves despite centre defects;
  - (B) positive asymptotic variance for some smooth observable of a positive-entropy non-hyperbolic measure.
- **Consequence:** the problem's claim (zero topological entropy) is **not** established by this attempt in dimension ≥ 4. Dimension ≤ 3 is covered by Theorem 5.2 of round 6.

=== END OF ANSWER round12_q1 ===
