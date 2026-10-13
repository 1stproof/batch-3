# Answer to round5_q5: (E1) for integrable eigen-distributions; status of (E1) in general

## Summary of status
- **Proved (Theorem 1).** Assume GH. Then (E1) holds for every W in L^1(M), and in fact for every measurable W satisfying the pointwise eigen-relation. In other words, there is no nonzero W in L^1(M) with XW = κW in D'(M) for a real κ ≠ 0. This needs no invariant volume, no restriction on |κ|, and no restriction on the growth of Dg_t. Dimension 1 is included.
- **Proved (Corollary 2).** Assume GH. Every solution of (E1) of order 0, i.e. W = T/ν with T a complex Radon measure, is singular with respect to ν. Every L^p or H^s (s ≥ 0) solution is 0.
- **Proved (Proposition 3).** (E1') holds for all T of order 0, even without GH. Under GH plus a smooth invariant volume, (E1) holds for all W of order 0.
- **Proved (Corollary 4).** This is what the chain needs. Assume GH. A closed current of finite mass and dimension n−1 that satisfies C(L_X β) = s C(β) with s ≠ 0 is zero.
- **Correction to the chain.** Step (c) of the planner's sketch has a degree error. Curve currents have dimension 1. A closed dimension-1 current that kills closed forms is the boundary of a dimension-2 current, which is an (n−2)-form-current. It is a generalized function only when n = 2. The fix is to use hypersurface currents of dimension n−1; then Corollary 4 settles step (d) completely.
- **Open.** (E1) for singular W: non-L^1 distributions, including singular measures and higher-order distributions. As the task notes, positive singular measure solutions exist whenever some ergodic μ has μ(div_ν X) ≠ 0. So full (E1) contains "every invariant probability has μ(d) = 0" and "X has no zeros", and I do not prove these. Full (E1) is neither proved nor refuted here. A refutation would require a GH field that is not conjugate to a Diophantine linear flow, i.e. a counterexample to the (open) Greenfield–Wallach conjecture.

## Conventions
ν is a smooth positive density and d = div_ν X. J_t(x) = ∫_0^t d(g_s x) ds, so (g_t)^*ν = e^{J_t} ν. A generalized function W pairs with smooth densities ρ, and XW is defined by ⟨XW, ρ⟩ = −⟨W, L_X ρ⟩. For smooth W this agrees with the usual derivative. L1 (Text A) says: if Xu = 0 with u in D', then u is constant. GH is the hypothesis of the problem. n = dim M.

## Lemma 0 (ergodicity of ν; this is "N1", reproved here)
Assume GH. Let A be a Borel set with ν(g_t A Δ A) = 0 for every t. Then ν(A) = 0 or ν(M∖A) = 0.

*Proof.* Let φ be smooth. By change of variables, ∫_A (φ∘g_t) e^{J_t} dν = ∫_{g_t A} φ dν = ∫_A φ dν for all t. The integrand is C^1 in t, with t-derivative bounded uniformly in x for |t| ≤ 1, and at t = 0 that derivative equals Xφ + dφ. Differentiating under the integral at t = 0 gives ∫_A (Xφ + dφ) dν = 0. This says ⟨X1_A, φν⟩ = −⟨1_A, L_X(φν)⟩ = 0, so X1_A = 0 in D'. By L1, 1_A is a.e. constant. ∎

## Lemma 1 (integrated eigen-relation)
Let W be in D'(M) and κ in C with XW = κW. Then for every smooth density ρ and every real t,
⟨W, (g_{−t})^*ρ⟩ = e^{κt} ⟨W, ρ⟩.
If W is in L^1(M), this says W∘g_t = e^{κt} W ν-a.e., for each t.

*Proof.* Put F(t) = ⟨W, (g_{−t})^*ρ⟩. The map t ↦ (g_{−t})^*ρ is smooth into the space of smooth densities, with derivative −(g_{−t})^* L_X ρ = −L_X (g_{−t})^*ρ. (L_X commutes with pullback by its own flow.) Hence
F'(t) = −⟨W, L_X (g_{−t})^*ρ⟩ = ⟨XW, (g_{−t})^*ρ⟩ = κ F(t),
so F(t) = e^{κt} F(0).

Now let W be in L^1 and ρ = φν. Then (g_{−t})^*ρ = (φ∘g_{−t}) e^{J_{−t}} ν. Substituting x = g_{−t} y gives
∫ W(g_t x) φ(x) dν(x) = ∫ W(y) φ(g_{−t}y) e^{J_{−t}(y)} dν(y) = F(t) = e^{κt} ∫ W φ dν.
This holds for all smooth φ, so W∘g_t = e^{κt} W a.e. ∎

## Lemma T (no measurable time function)
Assume GH and n ≥ 2. There is no Borel function τ : M → R (finite ν-a.e.) such that, for each t, τ∘g_t = τ + t ν-a.e.

*Proof.* Suppose such a τ exists. Define π(x) = g_{−τ(x)} x. This is Borel, because x ↦ (τ(x), x) is Borel and (s, y) ↦ g_{−s} y is continuous.

For each t, and for a.e. x,
π(g_t x) = g_{−τ(x)−t} g_t x = π(x).

Let E be a Borel set in M and A = π^{−1}(E). Then g_t^{−1}A = A mod ν for every t, because each g_t is a diffeomorphism and therefore preserves ν-null sets. By Lemma 0, ν(A) is either 0 or ν(M). So m = π_*(ν/ν(M)) is a Borel probability on the compact metric space M that takes only the values 0 and 1.

Its support is a single point. If p ≠ q were both in the support, disjoint neighbourhoods of p and q would both have positive m-measure, hence both measure 1, which is impossible. So m = δ_p for some p. Then π(x) = p a.e., which means x = g_{τ(x)} p, i.e. a.e. x lies on the orbit O(p) = {g_s p : s in R}.

But O(p) is the union over k in Z of the images of [k, k+1] under the smooth map s ↦ g_s p. Each image has Hausdorff dimension ≤ 1 < n, so it is ν-null, and O(p) is ν-null. This contradicts ν(M) > 0. ∎

## Theorem 1 ((E1) for integrable W)
Assume GH. Let κ be real with κ ≠ 0, and let W be in L^1(M) (complex-valued) with XW = κW in D'(M). Then W = 0 a.e.

More generally, the same conclusion holds for any Borel function W that satisfies, for each t, W∘g_t = e^{κt} W a.e.

*Proof, n ≥ 2.* By Lemma 1 it suffices to treat the pointwise relation. Since κ is real, |W|∘g_t = e^{κt}|W| a.e. So A = {W ≠ 0} satisfies g_t^{−1}A = A mod ν for every t.

Suppose W is not a.e. 0. Then ν(A) > 0, so A is conull by Lemma 0. Then τ = κ^{−1} log|W| is finite a.e. and satisfies τ∘g_t = τ + t a.e. for each t. This contradicts Lemma T. ∎

*Proof, n = 1.* Then M = S^1. We first show that X has no zeros; let Z be its zero set.
- If Z = M, then X = 0 and every distribution solves Xu = 0, so GH fails.
- If M∖Z has a component I (an open invariant arc) with ν(M∖I) > 0, then 1_I is a non-constant invariant function. Indeed, g_t I = I, and Lemma 0's computation gives X1_I = 0. This contradicts L1.
- Otherwise M∖Z is a single arc of full measure, so Z = {p} is a single point. Then X does not change sign, so X'(p) = 0 in a chart. Hence div_ν X(p) = 0, which contradicts P1.

So X has no zeros. Then every orbit is the whole circle, with a common period P, and g_P = id. Hence W = W∘g_P = e^{κP} W a.e., which forces W = 0. ∎

**Remarks.**
1. Theorem 1 covers every W in H^s for s ≥ 0 and every W in L^p for p ≥ 1.
2. It also works for complex κ with Re κ ≠ 0: use Re κ in place of κ.
3. The proof uses only L1 and Lemma 0, which give ergodicity and hence conservativity of ν. It does not use the tame estimate.
4. Sanity check: GH is necessary. The north–south flow on S^2 has an L^1 eigenfunction W = e^{κτ}, where τ is a time function on the wandering region. It is integrable when κ is smaller than the contraction exponent at the sink. That flow is not GH.

## Corollary 2 (measure solutions are singular)
Assume GH. Let T be a complex Radon measure, let W = T/ν, and suppose XW = κW with κ real and nonzero. Then T is singular with respect to ν.

*Proof.* By Lemma 1, T_t = e^{κt} T for every t, where T_t(φ) := T((φ∘g_{−t}) e^{J_{−t}}). This identity first holds for smooth φ, and then for bounded Borel φ because both sides are measures.

The operation T ↦ T_t is a push-forward by a diffeomorphism followed by multiplication by a positive smooth function. So it maps measures absolutely continuous to ν to absolutely continuous ones, and singular measures to singular ones. By uniqueness of the Lebesgue decomposition T = T_ac + T_s, we get (T_ac)_t = e^{κt} T_ac for all t.

Write T_ac = Wν with W in L^1. The relation (T_ac)_t = e^{κt} T_ac is exactly ⟨W, (g_{−t})^*ρ⟩ = e^{κt}⟨W, ρ⟩. Differentiating at t = 0 gives XW = κW. By Theorem 1, W = 0, so T = T_s. ∎

This is consistent with known item (1): the tilted conformal measures are carried by supp μ, and by B4 they have ν-null basins.

## Proposition 3 (order-0 cases)
**(a) (E1') for order 0, no GH needed.** Let T be a functional on C^∞ of order 0 with T(Xφ) = κT(φ) for all φ, where κ is real and nonzero. Then T = 0.

*Proof.* Differentiating in t shows T(φ∘g_t) = e^{κt}T(φ). Also |T(φ∘g_t)| ≤ ||T||_{(C^0)'} ||φ||_∞ for all t. Let t → +∞ if κ > 0, or t → −∞ if κ < 0. ∎

This is the case k = 0 of known item (2).

**(b) The volume case.** If X preserves a smooth positive density ω, then (E1) and (E1') coincide (taking ν = ω). So under GH plus a smooth invariant volume, (E1) holds for all W of order 0, by (a). It also holds for all L^1 solutions, by Theorem 1, and in that case the integrability is used in a weaker form. Solutions of order ≥ 1 that are not L^1 remain open even in the volume case.

## Corollary 4 (what the chain needs, with a corrected degree)
Assume GH and n ≥ 2, and orient M (otherwise pass to the orientation double cover, where the lift of X is still GH). Let C be a current of dimension n−1 with finite mass, i.e. a functional on (n−1)-forms of order 0. Suppose C is closed, meaning C(dα) = 0 for all (n−2)-forms α, and that for some s ≠ 0
C(L_X β) = s C(β) for all smooth (n−1)-forms β.
Then C = 0.

*On the GH claim for the double cover.* Let p : M̃ → M be the orientation double cover, σ the deck involution, and X̃ the lift of X. Let ũ be in D'(M̃) with X̃ũ smooth. The even part ũ + σ^*ũ is the pullback of a distribution u_0 on M with Xu_0 smooth, so it is smooth by GH. The odd part is p^*(u_1 ⊗ o), where o is the orientation line bundle. GH for X acting on o-twisted distributions follows from the same closed-graph setup only if one assumes it. **This point is not checked.** It is safer to read Corollary 4 under the assumption that M is orientable.

*Proof.* Take β closed. Then L_X β = d(i_X β), so C(L_X β) = C(d i_X β) = 0, and since s ≠ 0 we get C(β) = 0. Thus C vanishes on all closed (n−1)-forms. By de Rham's theorem for currents (cited from memory), C is a boundary: C(β) = ⟨W, dβ⟩ for some n-dimensional current W, i.e. a generalized function (the dual of n-forms). Then
C(L_X β) = ⟨W, d L_X β⟩ = ⟨W, L_X dβ⟩ = −⟨XW, dβ⟩,
so ⟨XW + sW, dβ⟩ = 0 for all β. On a connected manifold, a generalized function V with ⟨V, dβ⟩ = 0 for all β is constant (its differential is zero). Hence XW + sW = c for a constant c.

Put W' = W − c/s. Then XW' = XW = −sW + c = −sW', so XW' = κW' with κ = −s.

Since dW = ±C has measure coefficients, W is in BV(M), which is contained in L^1(M). This is standard BV theory, cited. A proof sketch: in a chart, with cutoffs χ_0 ≺ χ_1 ≺ … ≺ χ_N, write χ_j W = Σ_i (∂_iΦ) * ∂_i(χ_j W), where Φ is the Newtonian kernel and ∂_iΦ is in L^1_loc. Each convolution splits into a term (∂_iΦ) * (χ_j ∂_i W), which is in L^1, and a term involving (∂_iχ_j) W, which is one Sobolev order smoother than the previous step. Starting from W in H^{−σ}, after N > σ + n/2 steps, χ_0 W lies in L^1 + L^∞.

So W' is in L^1. By Theorem 1, W' = 0. Hence W is constant and C = ±dW = 0. ∎

**Consequence for the chain.** Step (d) of the planner's sketch is now proved, in the form the chain needs. That form is: a closed limit current of finite mass, obtained by the Patterson construction from hypersurface pieces (dimension n−1), and satisfying the eigen-relation, must vanish. So in that version the whole difficulty moves to the nonvanishing step (N). This is pointwise information only: it does not by itself give a contradiction unless (N) is established.

**The degree error.** The planner's currents C^s(β) = ∫ e^{−st} ∫_{g_tγ} β dt act on 1-forms, so they have dimension 1. A closed dimension-1 current that kills closed 1-forms is ∂D with D of dimension 2, which is an (n−2)-form with distribution coefficients. It is a generalized function only when n = 2. For n = 2 the conclusion is in any case known: continuous surface flows have zero entropy (cited from memory). So:
- In the version with curves, step (c) needs an (n−2)-form version of (E1) when n ≥ 3. That version is open; Theorem 1 does not address it.
- In the version with hypersurfaces, Corollary 4 applies.

For a hypersurface piece Σ, the (n−1)-volume of g_tΣ grows at the rate given by the sum of the top n−1 exponents of Σ's tangent directions. For example, it grows exponentially if Σ contains the unstable and flow directions and the flow expands its total (n−1)-volume. Whether that growth can be arranged and the limit current shown to be nonzero is the step (N); I did not address it.

## Where general (E1) stops
- The argument above needs W to be a function, so that log|W| defines a measurable time function. For a singular W there is no pointwise meaning.
- The singular case genuinely contains statements not reachable this way. For instance, at a zero p of X, W = δ_p/ν is a singular solution with κ = −d(p) (P1 shows d(p) ≠ 0). So (E1) for measures implies "GH ⇒ no zeros". It also implies "GH ⇒ μ(d) = 0 for every invariant μ", via the tilted conformal measures of [R4-q7] Prop 2.2.
- None of the tools here (L1, ergodicity of ν, the tame estimate, flow pullbacks, multiplication by smooth functions) produces from a singular W a non-smooth u with Xu smooth. I checked the following and they give nothing:
  - multiplying by smooth a: one would need Xa + κa = 0 on a neighbourhood of supp W, which forces a = 0 on supp W;
  - flow averages ∫ h(t) W∘g_t dt: these equal ĥ·W;
  - variable-time pullbacks W∘Φ_τ: these equal e^{κτ}W, again a multiplication.

**Open questions.**
1. (E1) for distributions W that are not L^1, in particular singular measures and higher-order distributions.
2. Equivalently, for order 0: does GH force μ(div_ν X) = 0 for every invariant probability μ, and does it force X to have no zeros?
3. An (n−2)-form analogue of Theorem 1, which the curve-current version of the chain would need.
4. Step (N), the nonvanishing of the limit current. It was not attempted.

=== END OF ANSWER round5_q5 ===
