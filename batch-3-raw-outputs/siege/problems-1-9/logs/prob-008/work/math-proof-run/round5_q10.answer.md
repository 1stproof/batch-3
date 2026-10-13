# Answer to round5_q10: statement (Lambda)

## 0. Status and plan (written first, updated at the end)

**Outcome.** I did not settle (Lambda), and I found no counterexample. Below are:
1. a check of chain step 2;
2. a correction to the planner's sketch: step (c) is wrong for dim M ≥ 3 because the degrees of the currents do not match;
3. a corrected version of the reduction, using currents of degree 1 instead of curve currents, together with a cancellation lemma showing one natural instance of it degenerates;
4. new elementary GH consequences (bounded invariant Borel functions, including the pointwise top Lyapunov exponent, are ν-a.e. constant; orbits with two-sided subexponential Jacobian are dense);
5. a hyperbolic partial result: every hyperbolic basic set Λ ≠ M is uniformly volume-contracting or uniformly volume-expanding, and Anosov flows are not GH (this part relies on cited results);
6. the exact place where the argument stops.

Conventions follow the task file: ν is a smooth positive density, d = div_ν X, J_t(x) = ∫_0^t d(g_s x) ds, and P = X + d. A distribution u is paired with densities by ⟨Xu, φν⟩ = −⟨u, Pφ ν⟩. L1 says Xu = 0 in D' implies u is constant.

## 1. Chain step 2 is correct

Cited from memory (Kushnirenko/Ito-type bound): if f is a Lipschitz self-map of a compact n-dimensional Riemannian manifold, then h_top(f) ≤ n·max(0, log Lip f). Also h_top(g_T) = |T|·h_top(g_1). Since Lip(g_T) ≤ max_x ||Dg_T(x)|| (geodesic distance), we get

h_top(g_1) ≤ (n/T)·log^+ max_x ||Dg_T(x)|| → n·max(0, λ*).

So (Lambda) implies zero topological entropy. The limit λ* exists because a_T = log max_x ||Dg_T(x)|| is subadditive, and λ* ≥ 0 because ||Dg_T(x)X(x)|| = ||X(g_T x)||. The reduction is sound. I see no reason to think (Lambda) is the wrong target: under the expected Greenfield–Wallach picture (Diophantine torus flows) both statements hold. Only (Lambda) is used below.

## 2. Step (c) of the planner's sketch fails when n = dim M ≥ 3

The sketch builds a 1-dimensional current C from curves g_tγ. It is closed, C(df) = 0, and satisfies C(L_X β) = s0·C(β) for every 1-form β. Step (c) concludes that "C kills closed forms, hence C = dW for a generalized function W".

**Claim 2.1.** For n ≥ 3 that conclusion does not type-check, and the correct one is weaker.

1. A 1-dimensional current is the same thing as an (n−1)-form ĉ with distribution coefficients, via C(β) = ∫ ĉ ∧ β.
2. Closedness, C(df) = 0, means dĉ = 0.
3. If C also kills every closed 1-form, then de Rham's theorem for currents (cited) gives ĉ = dΘ for an (n−2)-form Θ with distribution coefficients. Equivalently, C(β) = R(dβ) for a 2-dimensional current R.
4. Θ is a generalized function only when n − 2 = 0, i.e. n = 2.
5. For n ≥ 3 the eigen-relation becomes a statement about the (n−2)-current Θ: L_X Θ = ±s0·Θ + (closed). GH is a statement about functions. Lemma B of [R4-q10] lifts it only to closed currents of degree 1, so it says nothing about Θ.

For n ≤ 2 the whole question is classical: flows on surfaces have zero topological entropy (L.-S. Young 1977; Poincaré–Bendixson theory; cited). So the curve-current route, as written, is void exactly where it is needed.

## 3. Corrected reduction, using currents of degree 1

**Proposition 3.1 (proved).** Let C be a current of degree 1, i.e. C(η) = ∫ ĉ ∧ η for an (n−1)-form η, with ĉ a 1-form with distribution coefficients. Suppose:
- C is closed: C(dα) = 0 for all smooth (n−2)-forms α;
- C(L_X η) = κ·C(η) for all smooth (n−1)-forms η, with κ real and nonzero;
- C ≠ 0.

Then there is a non-constant W ∈ D'(M) with XW = −κW. Such a W is never smooth.

*Proof.*
1. **dĉ = 0.** We have d(ĉ∧α) = dĉ∧α − ĉ∧dα, and ∫ d(·) = 0 on the closed manifold M. Hence ∫ dĉ ∧ α = C(dα) = 0 for all α.
2. **Eigen-relation for ĉ.** L_X is a derivation and ∫ L_X(ĉ∧η) = ∫ d i_X(ĉ∧η) = 0. Hence C(L_X η) = −∫ (L_X ĉ) ∧ η. The hypothesis therefore gives L_X ĉ = −κ ĉ as currents.
3. **Decomposition.** By de Rham for currents (cited, as in Lemma B of [R4-q10]), ĉ = h + dW_0, where h is a smooth closed 1-form and W_0 ∈ D'.
4. **h is exact.** Cartan's formula gives L_X ĉ = d(h(X)) + d(XW_0). So by step 2, κh = −d(h(X) + XW_0 + κW_0) is exact as a current. De Rham's isomorphism between smooth and current cohomology (cited) then says h = dw_0 for some smooth w_0.
5. **The eigen-distribution.** Put W_1 = W_0 + w_0, so ĉ = dW_1. Step 2 gives d(XW_1 + κW_1) = 0. A distribution with zero differential on a connected manifold is constant, so XW_1 + κW_1 = c. Then W = W_1 − c/κ satisfies XW = −κW.
6. **W is non-constant.** dW = ĉ ≠ 0 because C ≠ 0.
7. **W is never smooth.** If W were smooth, then W(g_t x) = e^{−κt}W(x). Boundedness of W as t → −sign(κ)·∞ forces W = 0, contradicting step 6. ∎

**Consequence (the corrected chain).** (Lambda) would follow from two statements:
- (N') If λ* > 0, there is a nonzero closed degree-1 current C with C∘L_X = κC for some real κ ≠ 0.
- (E1) Under GH, there is no non-constant W ∈ D' with XW = κW for real κ ≠ 0.

Caution, already noted in the task file. (E1) implies μ(d) = 0 for every invariant probability μ, because the tilted conformal measures of [R4-q7] Prop. 2.2 give W = T/ν ≥ 0 with XW = −μ(d)W. So (E1) is at least as strong as "all invariant measures have zero ν-divergence". I could not prove that statement either; see §6.

**Lemma 3.2 (cancellation; proved). The obvious source of (N') degenerates.** Let B be a smooth closed ball and Σ = ∂B. Let V(t) be the (n−1)-volume of g_tΣ, and suppose the critical exponent s0 of Z(s) = ∫_0^∞ e^{−st}V(t) dt satisfies Z(s) → ∞ as s ↓ s0. Suppose also that the volume exponent v = limsup (1/t) log ν(g_tB) is < s0. Then the normalized currents

C_s(η) = Z(s)^{−1} ∫_0^∞ e^{−st} ∫_{g_tΣ} η dt

tend to 0 as s ↓ s0.

*Proof.* By Stokes, ∫_{g_tΣ} η = ∫_{g_tB} dη. So |C_s(η)| ≤ c·||dη||_∞ · Z(s)^{−1} ∫_0^∞ e^{−st} ν(g_tB) dt. The integral stays bounded for s near s0 > v, while Z(s) → ∞. ∎

Since ν(g_tB) = ∫_B e^{J_t} dν, one has v ≤ max_μ μ(d). So whenever surfaces grow faster than volumes, null-homologous closed hypersurfaces produce C = 0. This is the "cancellation of orientations" hard point (N) in an exact form. A non-trivial C would have to come from hypersurfaces that are not boundaries, or from a measurable orientation of the expanding directions. I could not produce either in general.

## 4. Two new elementary consequences of GH

**Lemma 4.1 (proved; uses only L1).** Let w be a bounded Borel function with w∘g_s = w ν-a.e. for each s ∈ R. Then w is ν-a.e. constant.

*Proof.*
1. **Change of variables.** Since (g_s)^*ν = e^{J_s}ν, for bounded Borel F we have ∫F dν = ∫ (F∘g_s) e^{J_s} dν. Apply this to F = wψ with ψ smooth and use invariance of w. This gives ∫ wψ dν = ∫ w·Q_sψ dν, where Q_sψ = e^{J_s}·(ψ∘g_s).
2. **Differentiate at s = 0.** (Q_sψ − ψ)/s → Xψ + dψ = Pψ uniformly. Hence ∫ w·Pψ dν = 0 for all smooth ψ.
3. **Conclude.** Step 2 says exactly ⟨Xw, ψν⟩ = 0, i.e. Xw = 0 in D'. By L1, w is a.e. constant. ∎

**Corollary 4.2 (proved).** Under GH, the pointwise top exponent χ(x) = limsup_{t→+∞} (1/t) log ||Dg_t(x)|| is ν-a.e. equal to a constant χ_ν ≤ λ*.

*Proof.* We check the three hypotheses of Lemma 4.1.
- *Bounded:* |log ||Dg_t||| ≤ t·||∇X||_∞ by Grönwall.
- *Borel:* t ↦ log ||Dg_t(x)|| is continuous, so the limsup can be taken over rational t.
- *Invariant:* Dg_t(g_s x) = Dg_s(g_t x)·Dg_{t+s}(x)·Dg_s(x)^{−1}, so log ||Dg_t(g_s x)|| differs from log ||Dg_{t+s}(x)|| by at most 2|s|·||∇X||_∞. Hence χ(g_s x) = χ(x).

The same argument applies to liminf_{t→+∞} J_t/t, limsup_{t→+∞} J_t/t, the backward versions, and every Oseledets-type pointwise quantity. ∎

Remark. If liminf_{t→+∞} J_t/t = c > 0 ν-a.e., then Fatou's lemma would give ∫ e^{J_t} dν → ∞. This contradicts ∫ e^{J_t} dν = ν(M). So that constant is ≤ 0.

**Lemma 4.3 (proved; a corollary of Lemma D).** Assume GH. Let x satisfy limsup_{t→+∞} J_t(x)/t ≤ 0 and limsup_{t→−∞} J_t(x)/|t| ≤ 0. Then the orbit of x is dense in M.

*Proof.* The hypothesis is exactly P(s) < ∞ for all s > 0 in Lemma D. By Lemma D, the probabilities T_s converge weak* to ν/ν(M), which has full support. Each T_s is supported in the orbit closure of x, and that closed set therefore also carries the limit. ∎

Consequently, a proper closed invariant set K contains no point whose forward Jacobian growth rate is ≤ 0 and whose backward Jacobian growth rate, in the sense above, is also ≤ 0.

## 5. Hyperbolic partial results (they rely on cited theorems)

**Proposition 5.1 (proved modulo cited thermodynamic formalism).** Assume GH and dim M ≥ 2. Let Λ ≠ M be a hyperbolic basic set of the flow (compact, invariant, locally maximal, transitive, hyperbolic, not a single orbit). Then one of the following holds:
- max{μ(d) : μ invariant on Λ} < 0, so J_t(x) ≤ b − ct on Λ for t ≥ 0, with c > 0 (uniformly volume-contracting); or
- min{μ(d) : μ invariant on Λ} > 0, so the same holds for −X (uniformly volume-expanding).

*Proof.* Let m_− = min μ(d) and m_+ = max μ(d) over invariant probabilities on Λ. Both are attained, and they are attained at ergodic measures, because the ergodic components of an extremal measure are extremal.
1. **Extreme value 0.** If m_+ = 0 or m_− = 0, there is an ergodic μ on Λ with μ(d) = 0. By Corollary D1, supp μ = M, which contradicts supp μ ⊂ Λ ≠ M.
2. **Strictly mixed signs.** Suppose m_− < 0 < m_+. Cited (Bowen–Ruelle thermodynamic formalism for hyperbolic basic sets of flows): for real q the Hölder potential q·d has a unique equilibrium state μ_q on Λ, which is ergodic. Moreover q ↦ μ_q(d) = P'(q) is continuous, with limits m_± as q → ±∞. By the intermediate value theorem some μ_q(d) = 0. This contradicts Corollary D1 as in step 1.
3. **Uniform rate.** The bound J_t ≤ b − ct on Λ follows from limsup_{t→∞} sup_{x∈Λ} J_t(x)/t = m_+, as in [R4-q7] Prop. 2.1 step 1, applied on Λ. ∎

**Proposition 5.2 (sketch; relies on cited Fredholm theory).** An Anosov flow is not GH.

*Sketch.*
1. **Cited (Butterley–Liverani; Faure–Sjöstrand).** There are anisotropic Sobolev spaces H with C^∞ ⊂ H ⊂ D' continuously, C^∞ dense in H, on which X − s is Fredholm of index 0 for Re s > −c(H). In particular X is Fredholm on H, so its range R is closed and has finite codimension.
2. **Range on smooth functions.** R ∩ C^∞ is the common kernel in C^∞ of finitely many continuous functionals. So it has finite codimension in C^∞.
3. **Periodic obstructions.** The periodic-orbit measures μ_γ are infinitely many linearly independent functionals on C^∞ (periodic orbits are dense and infinitely many). Hence ∩_γ ker μ_γ has infinite codimension. So there are f ∈ R ∩ C^∞ and a periodic orbit γ with μ_γ(f) ≠ 0.
4. **Contradiction with GH.** Write f = Xu with u ∈ H ⊂ D'. If u were smooth, integrating Xu along γ would give μ_γ(f) = 0. So u is not smooth, and X is not GH. ∎

**Corollary 5.3 (dimension 3; conditional on the cited Katok theorem).** Assume dim M = 3, GH and h_top > 0. Cited (Katok's horseshoe theorem for C^{1+α} flows on 3-manifolds; Lian–Young for flows in general dimension with hyperbolic measures): there is a hyperbolic basic set Λ with positive entropy. By Prop. 5.2, Λ ≠ M, since a basic set equal to M makes the flow Anosov. By Prop. 5.1, Λ is uniformly volume-contracting or uniformly volume-expanding. So in dimension 3, a GH flow with positive entropy must contain a strictly dissipative (or strictly anti-dissipative) horseshoe of saddle type.

## 6. Where the argument stops

**(a) Dissipative horseshoes cannot be ruled out by local constructions.** Let Λ be uniformly volume-contracting (Prop. 5.1). On Λ, every Patterson or product-conformal construction gives measures T with T(Pφ) = κT(φ). Here κ ranges over {P(ψ + d) − P(ψ)}, which lies inside [m_−, m_+] ⊂ (−∞, 0). Hence κ = 0, which is what L1 would forbid, is unreachable. Only global information would help, for example:
- an orbit that is forward-asymptotic to a contracting basic set and backward-asymptotic to an expanding one, which is excluded by Corollary C1/Lemma C;
- a ν-rapid-mixing resolvent u = ∫_0^∞ f∘g_t dt.

Neither is available in general.

**(b) Non-hyperbolic positive-entropy measures.** In dim ≥ 4 such measures can have zero exponents transverse to the flow. Then even the horseshoe input of Corollary 5.3 is missing.

**(c) The two linear statements remain open:**
- (E1): no real eigen-distributions;
- (N'): a non-degenerate closed degree-1 eigen-current.

GH controls X − κ only at κ = 0. I found no way to transfer it to κ ≠ 0: the a priori estimate loses derivatives, so it cannot be perturbed.

**(d) A further object that exists when λ* > 0 and does not contradict GH (observation, proved).** Use Krein–Rutman for the positive operators Ψ ↦ |Dg_t v|^2·Ψ(ĝ_t v) on C(SM), whose spectral radius is e^{2λ* t}. This gives a probability S on SM with ∫ |Dg_t v|^2 Ψ(ĝ_t v) dS = e^{2λ* t} ∫ Ψ dS. Then B(φ,ψ) = ∫ dφ(v)dψ(v) dS(v) is a nonzero positive semidefinite bilinear form with B(φ∘g_t, ψ∘g_t) = e^{2λ* t}B(φ,ψ). Differentiating gives λ*·B(φ,φ) = B(Xφ, φ), hence λ*^2·B(φ,φ) ≤ B(Xφ, Xφ). This is a "B-Poincaré inequality" that holds automatically, so it gives no contradiction with GH. The form is not symmetric-cancelled (B(φ,φ) > 0 for suitable φ), but turning it into a scalar distribution brings back problem (N).

## 7. Summary

**Proved in this answer:**
- Chain step 2 is sound (§1).
- The planner's step (c) is wrong for n ≥ 3 (§2).
- Corrected reduction: (N') + (E1) imply (Lambda) (Prop. 3.1).
- Null-homologous hypersurfaces give degenerate currents (Lemma 3.2).
- Bounded invariant Borel functions, in particular the pointwise top Lyapunov exponent, are ν-a.e. constant (Lemma 4.1, Corollary 4.2).
- Orbits with two-sided nonpositive Jacobian growth are dense (Lemma 4.3).

**Proved modulo cited theorems:**
- Proper hyperbolic basic sets are uniformly volume-contracting or uniformly volume-expanding (Prop. 5.1).

**Sketched, relying on cited theorems:**
- Anosov flows are not GH (Prop. 5.2).
- Dimension 3 reduction to dissipative horseshoes (Cor. 5.3).

**Open:**
- (Lambda) itself, and zero entropy in general.
- (E1).
- (N').
- Excluding uniformly dissipative horseshoes under GH.
- The non-hyperbolic case in dim ≥ 4.
- Whether every invariant probability μ satisfies μ(div_ν X) = 0 under GH.

=== END OF ANSWER round5_q10 ===
