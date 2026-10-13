# round2_q3: attempt on (S) — partial results only

**Status.** I did not prove (S). Below are the rigorous partial statements I proved, followed by the dead ends I checked. The core claim is still open.

Standing assumptions are those of (S). In particular, ω is a smooth invariant probability volume. Every ω-mean-zero smooth f equals Xu with u smooth. Text B, Lemma 2 then gives, for each k, constants m = m(k) and C_k with ||u||_{C^k} ≤ C_k ||f||_{C^m} when u is normalised to ω-mean zero.

## P1 (proved). Uniformly bounded ergodic integrals.
For every smooth f, every x and every T:
|∫_0^T f(g_t x) dt − T ω(f)| ≤ 2C_0 ||f − ω(f)||_{C^m} ≤ 4C_0 ||f||_{C^m}.
*Proof.* Write f − ω(f) = Xu. Then d/dt u(g_t x) = (f − ω(f))(g_t x). Integrate and use |u| ≤ C_0 ||f − ω(f)||_{C^m}. ∎

## P2 (proved). The unstable-leaf formula with an ambient Lipschitz bound.
Let x, y satisfy d(g_{−t}x, g_{−t}y) → 0 as t → ∞, with the integral below converging. This holds, for example, for y on the Pesin unstable manifold of an ω-regular x, where the convergence is exponential. Then for every smooth f:
(i) u(x) − u(y) = ∫_{−∞}^0 (f(g_t x) − f(g_t y)) dt;
(ii) |∫_{−∞}^0 (f(g_t x) − f(g_t y)) dt| ≤ 2C_1 ||f||_{C^{m(1)}} d(x,y).

*Proof.* The constant ω(f) cancels in the difference, so we may take f of mean zero, with Xu = f. Then
u(x) − u(y) − [u(g_{−T}x) − u(g_{−T}y)] = ∫_{−T}^0 (f(g_t x) − f(g_t y)) dt.
The bracket tends to 0 because u is uniformly continuous. For (ii), use ||du||_{C^0} ≤ C_1 ||f − ω(f)||_{C^{m(1)}} and a geodesic between x and y. ∎

The analogous statements hold for stable manifolds, with the integral taken over [0, ∞).

## P3 (proved). The derivative cocycle identity.
For smooth f with f − ω(f) = Xu, every tangent vector v and every t:
du(Dg_t v) = du(v) + ∫_0^t df(Dg_s v) ds.
Consequently |∫_0^t df(Dg_s v) ds| ≤ 2C_1 ||f||_{C^{m(1)}} (|v| + |Dg_t v|).

*Proof.* We have L_X du = d(Xu) = df. Differentiate α(Dg_s v) in s, with α = du. ∎

## P4 (proved). Spectral decay at zero frequency.
Iterate the cohomological equation. For smooth mean-zero f there are smooth u_j with X^j u_j = f. Hence the spectral measure satisfies σ_f = λ^{2j} σ_{u_j}, so σ_f([−ε, ε]) ≤ ||u_j||_{L^2}^2 ε^{2j}.

## Dead ends (checked)
1. **P4 with Pinsker / Lebesgue spectrum.** This does not give a contradiction. In a countable Lebesgue spectrum component, the vectors whose spectral measure vanishes near 0 are dense, so the linear spectral data alone is consistent with positive entropy.

2. **P2 with Pesin theory, at first order.** For y on W^u(x), the integral in P2(i) is at most about ∫ |Dg_t (y − x)| dt ≈ d(x,y)/λ. This is already O(d(x,y)), so the Lipschitz bound P2(ii) produces no contradiction. To get one, a single f with bounded C^m norm would need df aligned with the displacement along the whole backward orbit. A recurrent orbit returns to the same region with different displacement directions, so such an f does not exist.

3. **P3.** The bound grows with |Dg_t v| itself, so it cannot rule out exponential growth of Dg_t. The identity is a tautology for exact forms. A contradiction would need solvability of L_X α = β for some non-exact 1-forms β, which (S) does not provide.

4. **Derivative growth against the tame estimate.** As the planner noted, this fails because derivatives are lost: ||f ∘ g_s||_{C^m} ~ e^{mLs}.

## What remains open
(S) itself remains open. Two precise sub-questions would suffice; I proved neither:

- **(Q1)** Does a uniform polynomial-in-scale discrepancy for all orbits force zero topological entropy? Concretely: for each ε-scale bump f with ||f||_{C^m} ~ ε^{−m}, one has ∫_0^T f(g_t x) dt = T ω(f) + O(ε^{−m}) uniformly in x and T, as in P1.
- **(Q2)** Is the flow equicontinuous? Or does it have pure point spectrum? By Kushnirenko's theorem (cited from memory), discrete spectrum implies zero measure-theoretic entropy. With unique ergodicity and the variational principle (also cited from memory), that gives zero topological entropy.

=== END OF ANSWER round2_q3 ===
