# Answer to round6_q5: claim (DH)

## Summary

I could not prove (DH), and I found no counterexample. Two new results are proved rigorously below, using only GH, L1 and Lemma C from the brief.
- **Theorem 1** (jet non-resonance at periodic orbits): GH excludes every exact multiplicative resonance |det A|·μ^α = 1 of a periodic orbit's linear Poincaré map A. This extends Observation P (the case α = 0) and is the periodic-orbit analogue of Lemma H at zeros.
- **Theorem 2** (set version of Proposition 4.0): no orbit can go from a uniformly volume-expanding compact invariant set to a uniformly volume-contracting one.

Section 3 explains why these do not yet give (DH), and states exactly where the argument stops.

## 1. Theorem 1: jet non-resonance at periodic orbits (proved)

**Theorem 1.** Assume GH and n = dim M ≥ 2. Let γ be a periodic orbit of minimal period P > 0. Let Σ be a small transversal disc through p ∈ γ, and let F : Σ_0 → Σ be the Poincaré return map, with F(p) = p. Let A = DF(p), with eigenvalues μ_1, …, μ_{n-1} (complex, counted with multiplicity). Then for every multi-index α ∈ N^{n-1},

  |det A| · μ_1^{α_1} ⋯ μ_{n-1}^{α_{n-1}} ≠ 1.

For α = 0 this is Observation P, since log|det A| = ∫_γ d.

*Proof.*

1. **Chart around γ.** Take coordinates y ∈ R^{n-1} on Σ with p = 0. Let τ(y) be the return time, so τ(0) = P and F(y) = g_{τ(y)}(y). For small δ and a small disc Σ_0, the map Ψ(r, y) = g_r(y) on (−δ, P+δ) × Σ_0 is a local diffeomorphism onto an open neighbourhood U of γ. Its only self-overlaps are the following: for r near P,
   Ψ(r, y) = Ψ(r − τ(y), F(y)).
   This is the standard flow-box/tubular construction, using minimality of P. In the chart, X = ∂_r.

2. **Gluing an X-invariant distribution.** Let w be a generalized function on Σ_0, supported at 0, of finite order. In the chart define u = 1(r) ⊗ w(y). Then ∂_r u = 0, so Xu = 0 locally.
   - On the overlap, the two chart expressions agree iff (1 ⊗ w)∘Φ = 1 ⊗ w, where Φ(r, y) = (r − τ(y), F(y)).
   - Since 1 ⊗ w does not depend on r, (1 ⊗ w)∘Φ = 1 ⊗ (w∘F). Here w∘F is the pullback of a generalized function by a diffeomorphism, so for a test density h dy we have (w∘F)(h) = w((h∘F^{-1})·|det DF^{-1}|).
   - So if w∘F = w, then u is a well-defined distribution on U, supported on γ. Extend it by 0 to M. It is a distribution on M with Xu = 0 (Xu = 0 holds on U, and on M∖γ).

3. **Contradiction with L1 when w ≠ 0.** By L1, u is constant. Since u is supported on the ν-null set γ (n ≥ 2), that constant is 0. But u ≠ 0 when w ≠ 0. So under GH, the only generalized function w supported at 0 with w∘F = w is w = 0.

4. **Linear algebra.** Let D_k = {Σ_{|β|≤k} c_β ∂^β δ}. This space is finite-dimensional.
   - The map w ↦ w∘F sends D_k into D_k. Indeed, (∂^βδ)∘F applied to h equals ±∂^β((h∘F^{-1})·|det DF^{-1}|)(0), which involves derivatives of h at 0 of order ≤ |β| only.
   - So the map preserves the filtration D_0 ⊂ D_1 ⊂ … ⊂ D_k.
   - On D_m/D_{m-1} it acts through the linear part A. The m-th derivative tensor of h∘A^{-1} at 0 is D^m h(0)(A^{-1}·, …, A^{-1}·), and the Jacobian factor is |det A|^{-1}. Hence the eigenvalues on this graded piece are |det A|^{-1} μ^{-α} with |α| = m.
   - The operator is block triangular, so its spectrum is the union of these eigenvalues over m ≤ k.
   - If |det A| μ^α = 1 for some α, take k = |α|. Then 1 is an eigenvalue of the real operator on D_k, so there is a real nonzero w with w∘F = w. This contradicts step 3. ∎

**Remarks.**
- The condition is invariant under X → −X (the Poincaré map becomes F^{-1}), under time changes and under smooth conjugacy, as it must be.
- In dimension 3, for a saddle orbit of a horseshoe with real multipliers μ_u, μ_s (|μ_u| > 1 > |μ_s|), Theorem 1 excludes
  |μ_u μ_s| μ_u^a μ_s^b = 1, i.e. (1+a) log|μ_u| + (1+b) log|μ_s| = 0 (with the correct signs when μ_u or μ_s is negative), for all a, b ≥ 0.
- In exponent language: no periodic orbit of Λ has (1+a)χ^u + (1+b)χ^s = 0 exactly.

## 2. Theorem 2: no orbit from a volume-expanding set to a volume-contracting set (proved)

**Lemma 2.1 (uniform contraction near K).** Let K be a compact invariant set with μ(d) < 0 for every invariant probability μ carried by K. Then there are c > 0, a neighbourhood U of K and T_0 such that J_T(z) ≤ −cT whenever T ≥ T_0 and g_s z ∈ U for all s ∈ [0, T].

*Proof.*
1. The map μ ↦ μ(d) is continuous on the compact set of invariant probabilities on K, so max μ(d) = −2c < 0 for some c > 0.
2. If the lemma fails, then for each k there are T_k ≥ k and z_k whose orbit segment of length T_k stays in the 1/k-neighbourhood of K, with J_{T_k}(z_k) > −cT_k.
3. The empirical measures (1/T_k)∫_0^{T_k} δ_{g_s z_k} ds have a weak* limit m. It is invariant, because T_k → ∞.
4. m is carried by K: for every j it gives mass 1 to the closed 1/j-neighbourhood of K.
5. Also m(d) = lim J_{T_k}(z_k)/T_k ≥ −c, contradicting step 1. ∎

**Theorem 2.** Assume GH and n ≥ 2. Let K_1 and K_2 be compact invariant sets such that every invariant probability on K_1 has μ(d) > 0 and every invariant probability on K_2 has μ(d) < 0. Then no x ∈ M has α(x) ⊂ K_1 and ω(x) ⊂ K_2.

*Proof.*
1. **Forward half.** Since M is compact, dist(g_t x, ω(x)) → 0 as t → ∞. So g_t x ∈ U for all t ≥ t_1, with U from Lemma 2.1 applied to K_2.
2. Then J_t(x) = J_{t_1}(x) + J_{t−t_1}(g_{t_1} x) ≤ C − c(t − t_1) for t ≥ t_1 + T_0. Hence ∫_0^∞ e^{J_t(x)} dt < ∞.
3. **Backward half.** Apply the same argument to −X. Its ν-divergence is −d, and its log-Jacobian at time t is J_{−t}. Now K_1 plays the role of K_2. This gives ∫_{−∞}^0 e^{J_t(x)} dt < ∞.
4. So ∫_R e^{J_t(x)} dt < ∞, which contradicts Lemma C. ∎

**Consequences for the (H3) configuration.**
- Let Λ be uniformly volume-contracting. Then no point of W^s(Λ) has its α-limit set inside a uniformly volume-expanding set. Examples of such sets: a zero p with d(p) > 0; a periodic orbit with ∫ d > 0; a volume-expanding basic set. Proposition 4.0 is the special case where both sets are periodic orbits.
- More precisely, Lemma C itself gives limsup_{t→−∞} J_t(x)/|t| ≥ 0 for every x ∈ W^s(Λ).

## 3. Why (DH) is not reached, and the exact stopping point

1. **Theorem 1 is not enough.** It forbids only exact resonances at periodic orbits, and these are countably many codimension-one conditions. A horseshoe whose periodic orbits avoid all of them (the generic case) is not excluded.
   - The conditions are rigid: Poincaré multipliers are unchanged by time change and by conjugacy (both preserve GH), so these tools give no way to create a resonance.

2. **The non-periodic analogue is the natural next step, and it is not proved.** On Λ (dim 3), the weighted jet cocycle φ ↦ j^k(e^{J_t} φ∘g_t) has graded growth rates μ(d) + aχ^u(μ) + bχ^s(μ) = (1+a)χ^u + (1+b)χ^s.
   - Suppose the ratio χ^u/|χ^s| over invariant μ on Λ fills a nondegenerate interval. Then some ergodic μ has an exactly vanishing rate for suitable a, b, since rationals are dense.
   - A Patterson-type construction along a μ-generic orbit, like Lemma D but with jet-valued weights, then gives distributions T_s of order ≤ k with |T_s(Pφ)| ≤ s‖φ‖_{C^k}·(unnormalized mass).
   - Any nonzero weak* limit T would satisfy T∘P = 0 while being supported on Λ ≠ M. That contradicts L1, and would prove (DH) in dimension 3 for such Λ.
   - **It stops at two points.**
     - (a) Unlike for positive measures, the normalized T_s can converge to 0 because of cancellations. This is the same obstruction as (E1)/(E2).
     - (b) Mixed stable/unstable jets need a C^k local product structure, but stable and unstable holonomies are only C^{1+α}. Pure unstable-leaf jets (b = 0) avoid (b), but they need |χ^s|/χ^u = 1+a to be an exact integer for some μ.
   - The case where the ratio χ^u/|χ^s| is the same constant for every invariant measure on Λ (possibly irrational) is not covered even in principle.

3. **Positive (zero-order) objects are exhausted.** This rechecks R5-d §5 by pressure.
   - A product of conformal measures m^u_{ψ_1} × m^s_{ψ_2} × dt on Λ is ν-conformal iff P(ψ_1 + d) = P(ψ_1). But by the variational principle, P(ψ + d) ≤ P(ψ) + max μ(d) < P(ψ).
   - On W^s(Λ), using Lebesgue measure on stable leaves, it needs P(−φ^u) = 0. By Bowen's formula this means δ^u = 1, i.e. the zero escape rate of an attractor, which is excluded by B3.
   - The local measure δ(y_u)|y_s|^{−κ} near a saddle orbit, with κ = χ^u/|χ^s| < 1, is locally X-invariant. But its global extension along W^s(γ) has infinite mass, by Lemma C.
   - So a contradiction must come from genuinely signed or higher-order distributions.

## Status

- **Proved:**
  - Theorem 1 (jet non-resonance at periodic orbits, any dimension n ≥ 2).
  - Theorem 2 (no orbit from a uniformly volume-expanding to a uniformly volume-contracting compact invariant set).
- **Not proved (open):**
  - (DH) itself, including in dimension 3 (configuration (H3)).
  - The jet-conformal limit step 3.2 (non-vanishing of the limit; regularity of mixed jets).
  - The constant-ratio case.
  - (E1), which would imply (DH) at once through the tilted conformal measures of [R4-q7] Prop. 2.2.

=== END OF ANSWER round6_q5 ===
