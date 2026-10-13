# Answer to round5_q2: statement (Lambda)

## Plan / status
Target: (Lambda), or zero topological entropy directly, for globally hypoelliptic (GH) X.
Outcome: **not settled.** Below I prove the following.
- (§1) Step 2 of the chain is correct.
- (§2) (Lambda) is *strictly* stronger than the problem: applied to X and to −X, it forces "GH vector fields have no zeros". That statement is not established and is not needed for zero entropy (a zero carries no entropy). So (Lambda) is a riskier target than h_top = 0.
- (§3) No zeros in dimension 1 (an elementary proof by the log trick), and the reason the trick does not extend.
- (§4) Under GH plus a smooth invariant volume, h_top = h_ω and ω is non-hyperbolic. Hence h_top = 0 in dimension 3. Dimension ≤ 2 is trivial.
- (§5) Where the argument stops.

Conventions are those of the task: ν is a smooth positive density, d = div_ν X, and J_t is the log-Jacobian.

## §1. Step 2 of the chain is fine
For a Lipschitz map f of a compact n-dimensional Riemannian manifold, h_top(f) ≤ n·max(0, log Lip f). This is classical; I cite it from memory: cover by ε-balls and count (n,ε)-spanning sets using Lip(f^k) ≤ L^k. Also h_top(g_T) = |T| h_top(g_1). Lip g_T ≤ max_x ‖Dg_T(x)‖ holds on a compact Riemannian manifold, for the path metric. So h_top(g_1) ≤ (n/T) log^+ max‖Dg_T‖ → n·max(0, λ*). Step 2 is correct.

## §2. (Lambda) forces "no zeros" (proved)
**Claim.** Suppose (Lambda) holds for every GH vector field. Then no GH vector field has a zero.

*Proof.* Let X be GH with X(p) = 0, and let A = DX(p), so that Dg_t(p) = e^{tA}. Choose an eigenvector of A for an eigenvalue λ with maximal real part. Then ‖e^{tA}‖ ≥ e^{t Re λ}, and (Lambda) for X gives max Re λ_i ≤ 0. Now −X is GH by (O4), and its flow has derivative e^{−tA} at p. So (Lambda) for −X gives min Re λ_i ≥ 0. Hence all Re λ_i = 0 and tr A = Σ λ_i = Σ Re λ_i = 0.

In local coordinates write ν = ρ dx. Then d = ρ^{-1} ∂_i(ρ X_i) = ∂_i X_i + X(log ρ), so d(p) = tr A = 0. This contradicts P1 (d(p) ≠ 0 at every zero). ∎

So any proof of (Lambda) must contain a proof that GH fields have no zeros. Zero entropy needs no such thing: a fixed point carries zero entropy, and the variational principle only involves entropies of invariant measures. If the orchestrator keeps (Lambda) as the target, "no zeros" is an unavoidable sub-goal. Lemma H and B3 already exclude resonant zeros, sinks and sources. Saddles remain open in dimension ≥ 2 (§3).

## §3. Zeros: dimension 1 (proved) and the obstruction in higher dimension
**Claim.** On M = S^1, a GH field has no zeros.

*Proof.* Write X = a(θ)∂_θ with a(p) = 0, and take p = 0 in a local coordinate. Let χ be a smooth cutoff with χ ≡ 1 near 0, supported in a small coordinate interval. Put u = χ(θ) log|θ|. This is L^1, hence a distribution, and it is unbounded, hence not smooth.

The distributional derivative of log|θ| is p.v.(1/θ). Since a(0) = 0, the function b(θ) = a(θ)/θ = ∫_0^1 a'(sθ) ds is smooth. For a test function φ, p.v.∫ a φ/θ = ∫ b φ, an ordinary integral. Hence Xu = a χ' log|θ| + χ b. The first term is smooth because χ' vanishes near 0, and the second is smooth. So Xu is smooth while u is not, which contradicts GH. ∎

(In dimension 1 the entropy is 0 anyway. The claim only illustrates the mechanism.)

**Higher dimension; why the trick stalls.** Suppose there were a smooth h, defined near a zero p, with {h = 0} an invariant hypersurface and Xh = c·h for c smooth. Then u = χ log|h| has Xu = χc + (Xχ) log|h|. The second term is singular wherever the hypersurface crosses supp(Xχ). For a saddle, the natural candidate is W^s_loc(p) (a hypersurface when dim W^u = 1). Its continuation is the global stable manifold, which leaves every neighbourhood and may be dense, so no cutoff χ with Xχ = 0 near it exists. I could not get past this. "GH ⇒ no saddle zeros" is open here.

## §4. GH + smooth invariant volume (proved, modulo cited Pesin–Katok theory)
**Theorem 4.1.** Let X be GH on M with dim M ≥ 2, and suppose X preserves a smooth positive probability density ω. Then:
(a) the flow is uniquely ergodic with unique invariant probability ω, has no zeros and no periodic orbits, and h_top(g_1) = h_ω(g_1);
(b) ω is not hyperbolic: besides the zero exponent along X, ω has at least one further zero Lyapunov exponent;
(c) if dim M = 3, h_top(g_1) = 0. (For dim M ≤ 2, h_top = 0 for every C^1 flow, by Young's theorem on surface flows, cited from memory; dimension 1 is trivial.)

*Proof.*
(a) By (O2), every invariant probability equals ω. The measure δ_p at a zero, and the orbit measure of a periodic orbit, are invariant probabilities singular with respect to ω when dim ≥ 2, so neither exists. The variational principle (h_top = sup over invariant μ of h_μ) gives h_top(g_1) = h_ω(g_1). The variational principle for g_1 runs over g_1-invariant μ, which need not be flow-invariant. Let μ be g_1-invariant. Then s ↦ (g_s)_*μ is 1-periodic, so μ̄ = ∫_0^1 (g_s)_*μ ds is flow-invariant, and therefore μ̄ = ω.
- Since g_s commutes with g_1, h_{(g_s)_*μ}(g_1) = h_μ(g_1) for every s.
- Entropy is affine also for integrals of measures (Jacobs' theorem / the ergodic decomposition formula; cited).
Hence h_ω(g_1) = ∫_0^1 h_{(g_s)_*μ}(g_1) ds = h_μ(g_1), and so h_top(g_1) = h_ω(g_1).

(b) Cited from memory: **Katok's closing lemma for flows.** For a C^2 flow on a compact manifold, let μ be an ergodic invariant probability that is not a point mass at a zero and is hyperbolic, i.e. all Lyapunov exponents except the one along X are nonzero. Then supp μ is contained in the closure of the union of periodic orbits; in particular periodic orbits exist. (Katok 1980 for diffeomorphisms; the flow version is standard, cf. Lian–Young.)
ω is flow-ergodic by unique ergodicity, so its exponents are a.e. constant. Since (a) excludes periodic orbits and ω is not a point mass, ω is not hyperbolic. The exponent along X is 0, since |Dg_t X(x)| = |X(g_t x)| is bounded above and is not exponentially small along forward- and backward-recurrent orbits. So a second zero exponent exists.

(c) Let n = 3. The exponents of ω are 0 (along X), λ_1 and λ_2. Liouville's formula ties λ_1 + λ_2 + 0 to ω(div_ω X) = 0, so λ_1 + λ_2 = 0. By (b) one of λ_1, λ_2 is zero, hence both are. Ruelle's inequality, h_ω(g_1) ≤ Σ positive exponents, gives h_ω(g_1) = 0. Then h_top = 0 by (a). ∎

**Remark 4.2 (dim 3 without volume).** If dim M = 3 and only GH is assumed, every ergodic μ with h_μ > 0 is hyperbolic. Ruelle's inequality for g_1 and for g_{−1} gives one positive and one negative exponent, and the third exponent is the flow direction. So Katok's horseshoe theorem gives horseshoes. Their periodic orbits all satisfy ∫_γ d ≠ 0 (result P), and by Cor. C1 (whose heteroclinic part is only a sketch) all have the same sign within a horseshoe. I found no contradiction: dissipative horseshoes are not visibly excluded by GH.

## §5. A further proved criterion, and where the argument stops

**Proposition 5.1 (proved).** Let X be GH. Suppose there are an invariant probability μ and an integer k with the following property: for every smooth f with μ(f) = 0 there is c_f ∈ L^1([0,∞)) such that |∫ (f∘g_t) φ dν| ≤ c_f(t)‖φ‖_{C^k} for all smooth φ and t ≥ 0. ("Integrable decay of ν-correlations towards μ.") Then every smooth f with μ(f) = 0 equals Xu with u smooth, and μ is the unique invariant probability.

*Proof.* Define u by ⟨u, φν⟩ = ∫_0^∞ ∫ (f∘g_t) φ dν dt, a distribution of order k. Recall L_X(φν) = (Xφ + dφ)ν and ∫ X(w)φν = −∫ w L_X(φν). Then
⟨Xu, φν⟩ = −⟨u, L_X(φν)⟩ = −∫_0^∞ ∫ (f∘g_t) L_X(φν) dt = ∫_0^∞ ∫ X(f∘g_t) φν dt = ∫_0^∞ (d/dt) F(t) dt, where F(t) = ∫ (f∘g_t)φν.
F is Lipschitz, since |F'| ≤ ‖Xf‖_∞ ‖φ‖_{L^1(ν)}, and integrable, so F(t) → 0. Hence ⟨Xu, φν⟩ = −F(0), i.e. Xu = −f. By GH, u is smooth, so f = X(−u).
Let μ' be any invariant probability. Then μ'(Xw) = 0 for smooth w, so μ'(f) = 0 for every f with μ(f) = 0, i.e. μ' = μ. ∎
*Consequence.* No GH flow has integrable decay of ν-correlations together with two distinct invariant measures. This kills, e.g., every flow with a hyperbolic basic set or horseshoe plus an SRB-type measure with summable mixing rate. Positive entropy does not by itself give any decay rate, so this does not reach the general case.

**Where the general argument stops (precise points).**
1. *Planner's current/Patterson mechanism.* Steps (a)–(c) produce a nonzero closed eigen-current only if the limit current C does not vanish (the problem (N)). They then need (E1), the absence of real eigen-distributions XW = κW, κ ≠ 0.
   - (E1) in the "function" form is at least as strong as "every invariant μ has μ(d) = 0" (by Prop. 2.2 of R4-q7), which in turn contains "no zeros" (§2, P1).
   - In the "density" form T(Xφ) = κT(φ) coming from the Krein–Rutman measure S on SM, with κ = λ*, the a-priori bound |T_S(φ∘g_t)| ≤ ‖T_S‖_{(C^1)'} C e^{λ* t}‖φ‖_{C^1} is saturated, not violated, so order considerations give no contradiction.
   - The operator Ψ ↦ |Dg_t v|Ψ(ĝ_t v) commutes with the antipodal map v ↦ −v, so one may (and with a simple top eigenvalue must) take S even. Then T_S(φ) = ∫ dφ(v) dS = 0. A nonzero T_S needs a *continuous* orientation of the dominant direction, which does not exist in general (problem (N) is real, not technical).
2. *Quantitative GH estimates.* From (O1) one gets distributions S of fixed order m with S(ψ∘g_t) = S(ψ) + t(μ_1 − μ_2)(ψ) for two invariant measures μ_1, μ_2. This yields only linear lower bounds ‖ψ∘g_t‖_{C^m} ≥ ct, which is compatible with exponential growth. The analogous test functions u = ∫χ(t) φ∘g_t dt always put the exponentially large derivatives of g_t on the *right* side of ‖u‖ ≤ C‖Xu‖_{C^m}, so no contradiction results.
3. *Measure-theoretic route.* Positive entropy gives an ergodic μ with positive and negative exponents. Without volume, GH so far forbids only Jacobian-one periodic orbits (P), sign changes of ∫d inside a horseshoe (C1, partly sketched), basins of positive volume (B3), and full-support failure when μ(d) = 0 (D1). None of these excludes a dissipative positive-entropy hyperbolic set with all ∫_γ d of one sign, nor non-hyperbolic positive-entropy measures in dimension ≥ 4 (even with a volume, §4(b) leaves exponents (λ, 0, −λ, …) possible).

## Summary
**Proved.**
- Step 2 of the chain (§1).
- (Lambda) ⇒ GH fields have no zeros (§2), so (Lambda) is strictly harder than zero entropy.
- No zeros on S^1 (§3).
- GH + smooth invariant volume ⇒ h_top = h_ω, and ω is non-hyperbolic. Hence h_top = 0 when dim M = 3, and trivially when dim M ≤ 2. This uses Katok's closing lemma for flows, Ruelle's inequality and the variational principle, all cited from memory.
- GH + integrable decay of ν-correlations ⇒ unique ergodicity, with every μ-mean-zero smooth function a smooth coboundary (Prop. 5.1).

**Open.**
- (Lambda) itself.
- Zero entropy for general GH flows, including dim 3 without a volume and dim ≥ 4 with a volume.
- Whether GH excludes saddle zeros (dim ≥ 2).
- (E1).
- The non-vanishing problem (N) for eigen-currents.

No counterexample was found; the expected picture (Greenfield–Wallach conjecture: GH fields are Diophantine linear flows on tori) makes (Lambda) very likely true. From memory, and unverified: I believe the dimension-3 case of the related Katok/Greenfield–Wallach conjectures was treated by Forni and by Kocsard using Katok horseshoes, in line with §4.

=== END OF ANSWER round5_q2 ===
