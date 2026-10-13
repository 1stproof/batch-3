# Globally hypoelliptic flows and topological entropy: the volume-preserving case in every dimension, the case dim M ≤ 3, and reductions of the general case

## Summary

**The claim to be shown** is that if X is globally hypoelliptic (GH: every distribution u with Xu smooth is itself smooth), then the flow g_t has zero topological entropy, i.e. h_top(g_1) = 0. **The claim is not proved in full here.** The document proves the following.

* **Theorem V (volume-preserving case, every dimension; §7.3).** If X is GH and preserves a smooth positive density, then h_top(g_1) = 0. In fact the maximal number of (T, ε)-separated orbit segments grows at most polynomially in T. The proof uses only standard analysis (closed graph theorem, Hahn–Banach, Rellich, Sobolev embedding) and Bowen's definition of entropy; no Pesin theory.
* **Reduction to a smooth invariant volume (§7.4).** Consequently the problem follows from the statement **(V)**: *every GH field preserves a smooth positive density.* Under GH, (V) is equivalent to a one-sided uniform bound on the log-Jacobian, sup_{t≥0,x} J_t(x) < ∞ (Theorem W), and to the ν-integrability of limsup_{t→∞} J_t (Theorem W′). (V) itself is not proved.
* **Theorem A (dim M ≤ 3; §5).** If X is GH and dim M ≤ 3, then h_top(g_1) = 0, with no volume assumption. The proof uses the variational principle, Ruelle's inequality, the stable manifold theorem and Katok's horseshoe theorem for flows (cited).
* **Theorem B (every dimension; §5).** Under GH every ergodic invariant measure of positive entropy is non-hyperbolic.
* **Theorems C and C′ (§6)** on the mean divergence of a positive-entropy ergodic measure μ (C′ is proved modulo one citation, non-stationary normal forms). Consequences: **Corollary C″**, the problem is equivalent to the statement (PE0) of §6.2 (modulo that citation); **Corollary C‴**, the structure of positive-entropy measures in dimension 4; **Proposition 6.5**, full support.
* **Theorems E and E′ (§8)**, which reduce (PE0), hence the problem, to a statement (SC) that does not mention GH.

The Status section (§9) says exactly what is proved and what is missing; §10 records other routes.

---

## 0. Conventions and cited facts

### 0.1 Notation
* M is compact, connected and smooth, with n = dim M. X is a smooth vector field with flow g_t. We fix a Riemannian distance d(·,·) on M.
* ν is a fixed smooth positive density (not assumed invariant). We write d := div_ν X, so that L_X(φν) = (Xφ + dφ)ν, and put Pφ := Xφ + dφ.
* J_t(x) := ∫_0^t d(g_s x) ds. This is the logarithm of the ν-Jacobian of g_t at x. It satisfies the cocycle identity J_{t+s}(x) = J_s(x) + J_t(g_s x), and d/dt [e^{J_t(x)} φ(g_t x)] = e^{J_t(x)} (Pφ)(g_t x).
* We write Γ_t φ := e^{J_t}·(φ∘g_t).
* A **distribution density** is a continuous linear functional S on C^∞(M). A distribution (generalised function) u is identified with the distribution density S = uν, S(φ) = ⟨u, φν⟩. Then

  ⟨Xu, φν⟩ = −⟨u, L_X(φν)⟩ = −S(Pφ).   (0.1)

  So Xu = f means −S(Pφ) = ∫ fφ dν for all φ.
* **GH** is the hypothesis of the problem: if u is a distribution and Xu is smooth, then u is smooth. If X is GH then so is −X, since (−X)u = f ⇔ Xu = −f. The flow of −X is g_{−t}, its ν-divergence is −d, and its log-Jacobian at time t is J_{−t}.
* ‖φ‖_{C^k} denotes a fixed C^k norm, with ‖φ‖_{C^1} := max(‖φ‖_∞, ‖dφ‖_∞). Then |φ(a) − φ(b)| ≤ ‖φ‖_{C^1} d(a,b), because M is connected.
* h_top(g_1) is the topological entropy of the time-one map. Since h_top(g_t) = |t| h_top(g_1), "the flow has zero entropy" means h_top(g_1) = 0.

### 0.2 Cited classical theorems (used as black boxes, cited from memory)
* **[VP]** The variational principle for the homeomorphism g_1. The ergodic decomposition. Jacobs' theorem: entropy is affine, and h_μ = ∫ h_{μ_ω} dω over the ergodic decomposition.
* **[Os]** Oseledets' multiplicative ergodic theorem. For a cocycle with an invariant subbundle, the Lyapunov spectrum is the union, with multiplicity, of the spectra on the subbundle and on the quotient.
* **[Ru]** Ruelle's inequality. For a C^1 diffeomorphism f and an f-invariant μ, h_μ(f) ≤ ∫ Σ_i χ_i^+ dμ.
* **[SM]** The stable manifold theorem for hyperbolic periodic orbits and hyperbolic zeros, with asymptotic phase (made precise in §3).
* **[KLY]** Katok's horseshoe theorem for flows. Katok (Publ. IHÉS 1980) states it for flows on 3-manifolds; the version in every dimension, for C^2 flows, is due to Lian–Young (J. Amer. Math. Soc. 2012). Both are recalled from memory. Statement used: suppose μ is an ergodic invariant probability of a C^2 flow with h_μ(g_1) > 0 and μ(Zero(X)) = 0, and suppose every Lyapunov exponent other than the one in the flow direction is nonzero. Then the flow has a hyperbolic horseshoe. In particular it has a hyperbolic periodic orbit γ with a (transverse) homoclinic point, i.e. a point of W^u(γ) ∩ W^s(γ) not on γ.
* **[P]** Pesin theory for f = g_1 and an f-invariant, f-ergodic μ, as follows. For μ-a.e. x the unstable set W^u(x) = {y : limsup_m (1/m) log d(f^{−m}y, f^{−m}x) < 0} is an injectively immersed C^∞ submanifold tangent to E^u_x (the sum of the Oseledets spaces of positive exponents), with f^{−1}W^u(x) = W^u(f^{−1}x). For every compact Q ⊂ W^u(x) (intrinsic topology) and δ > 0 there is C = C(x,Q,δ) with d^u(f^{−m}y, f^{−m}x) ≤ C e^{−(χ^+_min − δ)m} for y ∈ Q and m ≥ 0, where χ^+_min is the smallest positive exponent. There are Pesin sets (compact sets Λ_l, μ(Λ_l) → 1) on which the local stable/unstable discs have uniform size and contraction constants and depend continuously (C^1) on the base point. Symmetric statements hold for W^s.
* **[LS]** Ledrappier–Strelcyn / Ledrappier–Young. There is a measurable partition ξ subordinate to W^u: ξ(x) ⊂ W^u(x), and ξ(x) contains a leaf-neighbourhood of x. It is increasing (fξ ≤ ξ, i.e. ξ refines fξ) and h_μ(f) = H_μ(ξ | fξ).
* **[NF]** (used only in Theorem C′, §6.3) Non-stationary sub-resonance normal forms on Pesin unstable manifolds (Kalinin–Sadovskaya, J. Mod. Dyn. 2017; Melnick 2019), with measurable dependence on the base point. The precise form used is stated in §6.3. **This is the one citation whose exact hypotheses I could not check.** The proof only needs it in local form, on discs of measurable (tempered) radius around the base point (the points y_i of §6.3 may be taken in ξ(x) arbitrarily close to x). The measurability required for (G3) of §6.3 is to be deduced from [NF](c) and the series (6.1). When dim E^u = 1 it reduces to the classical existence of affine parameters on one-dimensional unstable leaves.
* **[At]** Atkinson's recurrence theorem (1976). If T is an invertible ergodic measure-preserving transformation of a probability space and f ∈ L^1 has ∫f = 0, then for a.e. x and every ε > 0 there are infinitely many n ≥ 1 with |Σ_{j=0}^{n−1} f(T^jx)| < ε. (Used only in Proposition 6.5.)
* **[An]** Standard analysis on a compact manifold (used only in §7): Sobolev spaces H^s(M); the Sobolev embedding H^r ⊂ C^1 for r > n/2 + 1; Rellich's theorem (H^{r+1} ⊂ H^r compactly); ‖f‖_{H^j} ≤ C‖f‖_{C^j}; the closed graph theorem for Fréchet spaces; the Hahn–Banach theorem in the locally convex space C^∞(M); smoothness of (p,x) ↦ d(p,x)^2 for d(p,x) below the injectivity radius; for a smooth positive density ω the two-sided bound c_ω ρ^n ≤ ω(B(p,ρ)) ≤ C_ω ρ^n for small ρ, uniformly in p.
* **[Bo]** Bowen's definition of topological entropy (used only in §7). For a continuous map G of a compact metric space (M,d), a set E is (k, ε)-separated if for all x ≠ y in E, max_{0≤i≤k−1} d(G^ix, G^iy) > ε; with s(k,ε) the maximal cardinality of such a set, h_top(G) = lim_{ε→0} limsup_{k→∞} (1/k) log s(k,ε). This agrees with the Adler–Konheim–McAndrew definition and does not depend on the compatible metric.

### 0.3 Dependence summary
* Lemmas 1.1–1.4, Corollary 1.5 and Theorem J use only GH (Lemma 1.4 also [An]). Lemma K and Lemma K′ use only Theorem J. Corollaries 3.2–3.3 use in addition [SM].
* **Theorem V (§7.3)** uses GH, Lemma 1.1, Lemma 1.4, [An] and [Bo], and nothing else. Theorems W and W′ (§7.4) use GH, Lemma 1.1 and Corollary 1.5 only.
* Theorem B uses [Os], [Ru], [KLY] and, through Corollary 3.3, [SM]. Theorem A uses in addition [VP].
* Theorem C uses [P] and [LS]. Theorem C′ uses [P], [LS] and [NF]. Corollary C‴ uses [P], [LS], the one-dimensional affine parameters, and, through Theorem B, [Os], [Ru], [KLY], [SM].
* Proposition 6.5 (full support) uses GH and [At]. Lemmas 4.1–4.2 use [VP] (Jacobs) and the ergodic decomposition only. Theorems E and E′ use GH only.

---

## 1. Elementary consequences of GH

**Lemma 1.1 (kernel).** Assume GH. If u is a distribution with Xu = 0, then u is constant.

*Proof.* By GH u is smooth. Suppose u is not constant, and choose c with min u < c < max u. Let H_ε be smooth and nondecreasing with H_ε = 0 on (−∞, −ε] and H_ε = 1 on [0, ∞). Then v_ε := H_ε(u − c) is smooth and Xv_ε = H_ε′(u − c)·Xu = 0. As ε → 0, v_ε → 1_{\{u≥c\}} =: v boundedly and pointwise (on {u ≥ c} every v_ε equals 1; at a point with u − c < 0, v_ε = 0 as soon as ε ≤ c − u), hence in L^1 and in D′. So Xv = 0, and by GH v agrees a.e. with a continuous function w. Then w ∈ {0,1} a.e., hence everywhere, so w is constant because M is connected. But w = 1 a.e. on the nonempty open set {u > c} and w = 0 a.e. on the nonempty open set {u < c}. Contradiction. (Complex-valued u: apply this to the real and imaginary parts.) ∎

**Lemma 1.2.** Assume GH.
(F1) If S is a distribution density with S(Pφ) = 0 for all φ, then S = cν for a constant c.
(F2) If S(Pφ) = c′∫φ dν for all φ, where c′ is a constant, then c′ = 0.

*Proof.* (F1): u = S/ν has Xu = 0 by (0.1), so u is constant by Lemma 1.1. (F2): u = S/ν has Xu = −c′ by (0.1), so u is smooth by GH. If c′ is complex, X is real, so Re u and Im u satisfy X(Re u) = −Re c′ and X(Im u) = −Im c′; it suffices to treat a real constant c′ and a real smooth u. At a maximum point q of u the function s ↦ u(g_s q) has a maximum at s = 0. Hence (Xu)(q) = 0 and c′ = 0. ∎

**Lemma 1.3 (closed orbits).** Assume GH and n ≥ 2. Let q ∈ M and P > 0 with g_P q = q. Then J_P(q) ≠ 0. In particular d(p) ≠ 0 at every zero p of X (take any P: J_P(p) = P d(p)). Also, the Poincaré map of a periodic orbit never has Jacobian determinant of modulus 1, because e^{J_P(q)} = |det Dg_P(q)| equals that modulus.

*Proof.* Put S(φ) := ∫_0^P e^{J_s(q)} φ(g_s q) ds. Then S(Pφ) = ∫_0^P (d/ds)[e^{J_s(q)}φ(g_s q)] ds = (e^{J_P(q)} − 1)φ(q). If J_P(q) = 0, (F1) gives S = cν. But S is a nonzero positive measure (S(1) > 0) carried by the orbit of q. That orbit is a point or a closed C^1 curve, so it is ν-null when n ≥ 2. Contradiction. ∎

**Lemma 1.4 (tame estimate and closed range; used only in §7).** Assume GH. Fix a smooth positive density ω₀ and put c(u) := ∫u ω₀/∫ω₀. For every r ≥ 0 there are j ∈ ℕ and C′ with ‖u − c(u)‖_{H^r} ≤ C′‖Xu‖_{H^j} for all smooth u. Moreover X(C^∞(M)) is closed in C^∞(M).

*Proof.* Fix a smooth density ω₀ and Sobolev spaces H^s(M), and fix s ≥ 0. Let F_s := {u ∈ H^{−s} : Xu ∈ C^∞}, with the seminorms ‖u‖_{H^{−s}} and ‖Xu‖_{H^j}, j ∈ ℕ. This is a Fréchet space. By GH, F_s ⊂ C^∞, and the inclusion has closed graph since both spaces embed continuously in H^{−s}. By the closed graph theorem it is continuous: for every r there are j and C with ‖u‖_{H^r} ≤ C(‖u‖_{H^{−s}} + ‖Xu‖_{H^j}).

Now let c(u) := ∫u ω₀/∫ω₀. We claim ‖u − c(u)‖_{H^r} ≤ C′‖Xu‖_{H^j} for smooth u, with j chosen so that the previous estimate holds at levels r and r+1. If not, there are smooth u_m with c(u_m) = 0, ‖u_m‖_{H^r} = 1 and ‖Xu_m‖_{H^j} → 0. The previous estimate at level r+1 bounds u_m in H^{r+1}. By Rellich a subsequence converges in H^r to some u with ‖u‖_{H^r} = 1, c(u) = 0 and Xu = 0. By Lemma 1.1 u is constant, hence u = 0. Contradiction.

So if Xu_m → f in C^∞, then (u_m − c(u_m)) is Cauchy in every H^r and converges in C^∞ to some u with Xu = f. ∎

**Corollary 1.5 (ν-ergodicity; used in §7.4).** Assume GH. If A ⊂ M is measurable and ν(A △ g_t^{−1}A) = 0 for every t, then ν(A) = 0 or ν(M∖A) = 0. More generally, if b ∈ L^1(ν) and b∘g_t = b ν-a.e. for every t, then b is ν-a.e. constant.

*Proof.* Let b ∈ L^1(ν) with b∘g_t = b a.e. for every t (for the first statement take b := 1_A). Since e^{J_t} is the ν-Jacobian of g_t, ∫ψ∘g_t·e^{J_t}dν = ∫ψdν for ψ ∈ L^1(ν). With ψ := (b∘g_{−t})φ this gives ∫b·Γ_tφ dν = ∫(b∘g_{−t})φ dν = ∫bφ dν for smooth φ. Since Γ_tφ = φ + tPφ + O(t^2) uniformly on M (step 1 of the proof of Theorem J), differentiating at t = 0 gives ∫b·Pφ dν = 0. So S := bν satisfies S(Pφ) = 0, and S = cν by (F1). Hence b = c ν-a.e. (For b = 1_A, c ∈ {0,1}.) ∎

---

## 2. Theorem J: no two-sided exponentially decaying transported distribution

**Theorem J.** Assume GH. Let S be a distribution density, and suppose there are ε > 0, k ∈ ℕ and C with

  |S(Γ_t φ)| ≤ C e^{−ε|t|} ‖φ‖_{C^k}  for all t ∈ ℝ and all φ ∈ C^∞(M).   (J)

Then S = 0.

*Proof.* Write F_φ(t) := S(Γ_t φ).
1. The map (t,x) ↦ e^{J_t(x)}φ(g_t x) is jointly smooth. So t ↦ Γ_tφ is C^1 into C^∞(M), with derivative Γ_t(Pφ). Since S is continuous, F_φ is C^1 and F_φ′ = F_{Pφ}.
2. Put m_j(φ) := ∫_ℝ t^j F_φ(t) dt for j ≥ 0. By (J), |m_j(φ)| ≤ C‖φ‖_{C^k}∫|t|^j e^{−ε|t|}dt. So each m_j is a distribution density.
3. By (J) for Pφ, F_φ′ = F_{Pφ} also decays exponentially. Integrating by parts gives m_0(Pφ) = ∫F_φ′ = 0, and m_j(Pφ) = ∫t^jF_φ′ = −j m_{j−1}(φ) for j ≥ 1.
4. We show m_j = 0 for all j, by induction. By (F1), m_0 = c_0ν. Then m_1(Pφ) = −c_0∫φdν, so c_0 = 0 by (F2). If m_{j−1} = 0, then m_j(Pφ) = 0, so m_j = c_jν by (F1). Then m_{j+1}(Pφ) = −(j+1)c_j∫φ dν, so c_j = 0 by (F2).
5. Fix φ. G(ξ) := ∫e^{−iξt}F_φ(t)dt is holomorphic on the strip |Im ξ| < ε, and G^{(j)}(0) = (−i)^j m_j(φ) = 0 for all j. So G ≡ 0, and by Fourier uniqueness (F_φ is continuous and integrable) F_φ ≡ 0. In particular S(φ) = F_φ(0) = 0. ∎

*Remarks.* (i) The proof uses GH only through Lemma 1.1 and (F2), i.e. through "Xu = constant ⇒ u constant". (ii) The theorem is false without GH. For the north–south flow on S², take y on a source-to-sink orbit; then S = δ_y satisfies (J).

All further uses of GH in §§3–6 and §8 go through Theorem J, except Proposition 6.5, which uses (F1) directly. §7 uses Lemmas 1.1, 1.4 and Corollary 1.5 instead of Theorem J.

---

## 3. Points asymptotic to closed orbits (Lemma K) and homoclinic orbits

**Lemma K.** Assume GH. Let p ∈ M and P > 0 with g_P p = p (p may be a zero of X; no hyperbolicity is assumed). There is no point y ≠ p such that
(a) d(g_{−mP}y, p) ≤ Cκ^m for all integers m ≥ 0, for some C and some κ ∈ (0,1); and
(b) J_t(y) ≤ C − εt for all t ≥ 0, for some ε > 0.

*Proof.* Put I := J_P(p) and suppose y exists.
1. For Ψ ∈ C^∞ put (LΨ)(v) := e^{J_{−P}(v)}Ψ(g_{−P}v). By the cocycle identity, (L^mΨ)(v) = e^{J_{−mP}(v)}Ψ(g_{−mP}v). L is bounded on C^K for every K.
2. Fix K ≥ 1. Let I_K be the space of smooth functions whose derivatives of order < K vanish at p. Since g_{−P}p = p, L(I_K) ⊂ I_K, so L induces a linear map L_K on the finite-dimensional jet space C^∞/I_K, of dimension N. Let Q(ζ) = Σ_{j=0}^N q_jζ^j (q_N = 1) be its characteristic polynomial. By Cayley–Hamilton, Q(L)Ψ ∈ I_K for every Ψ, and ‖Q(L)Ψ‖_{C^K} ≤ C_1‖Ψ‖_{C^K}. By Taylor's formula in a chart ball B around p, |G(v)| ≤ C_2‖G‖_{C^K} d(v,p)^K for G ∈ I_K and v ∈ B.
3. Put y_j := g_{−jP}y and w_j := q_j e^{J_{−jP}(y)} for 0 ≤ j ≤ N, and S := Σ_j w_jδ_{y_j}. The y_j are pairwise distinct. Indeed, g_{−aP}y = g_{−bP}y with a < b would make y fixed by g_{−(b−a)P}, and then (a) forces y = p. Since w_N ≠ 0, S ≠ 0.
4. Let t ≤ 0 and write t = −mP − r with m ≥ 0 an integer and r ∈ [0,P). Put Φ_r := e^{J_{−r}}φ∘g_{−r}; then ‖Φ_r‖_{C^K} ≤ C_3‖φ‖_{C^K}. By the cocycle identity, w_je^{J_t(y_j)}φ(g_ty_j) = q_j(L^{m+j}Φ_r)(y). Hence

   S(Γ_tφ) = (L^mG_r)(y) = e^{J_{−mP}(y)}G_r(g_{−mP}y),  where G_r := Q(L)Φ_r ∈ I_K.
5. By (a), for m ≥ m_0 we have g_{−mP}y ∈ B and |G_r(g_{−mP}y)| ≤ C_2C_1C_3C^K κ^{mK}‖φ‖_{C^K}. Also J_{−mP}(y) = −Σ_{i=1}^m J_P(g_{−iP}y), and |J_P(g_{−iP}y) − I| ≤ Lip(J_P)Cκ^i. So J_{−mP}(y) ≤ −mI + C_4. Hence |S(Γ_tφ)| ≤ C_5 exp(m(−I − K log(1/κ)))‖φ‖_{C^K}.
6. Choose K with K log(1/κ) > max(0, −I) + 1. Then |S(Γ_tφ)| ≤ C_6e^{−|t|/P}‖φ‖_{C^K} for t ≤ 0.
7. For t ≥ 0, J_t(y_j) = J_{t−jP}(y) − J_{−jP}(y). By (b) when t ≥ jP, and trivially when t < jP, this is ≤ C_7 − εt. So |S(Γ_tφ)| ≤ C_8e^{−εt}‖φ‖_∞.
8. By Theorem J, S = 0, which contradicts step 3. ∎

**Lemma K′ (time reversal).** Assume GH. There are no p with g_Pp = p (P > 0) and y ≠ p with d(g_{mP}y, p) ≤ Cκ^m (m ≥ 0) and J_t(y) ≤ C − ε|t| for t ≤ 0.
*Proof.* Apply Lemma K to −X (§0.1). ∎

**[SM], precisely.** Let γ be a hyperbolic periodic orbit of period P, or a hyperbolic zero (then γ = {p} and we put P = 1). There is c > 0 with the following property. For every y with dist(g_ty, γ) → 0 as t → +∞, there are q ∈ γ and C_y with d(g_ty, g_tq) ≤ C_ye^{−ct} for t ≥ 0. Symmetrically, if dist(g_ty, γ) → 0 as t → −∞, there are q′ ∈ γ and C′_y with d(g_ty, g_tq′) ≤ C′_ye^{−c|t|} for t ≤ 0. Put I(γ) := J_P(q) for q ∈ γ; this is independent of q. Then J_t(q) = (t/P)I(γ) + O(1) uniformly in t ∈ ℝ.

**Corollary 3.2 (connections).** Assume GH. Let γ_1, γ_2 be hyperbolic periodic orbits or hyperbolic zeros, and let y ∈ W^u(γ_1) ∩ W^s(γ_2) with y ∉ γ_1 ∪ γ_2. Then I(γ_1) ≤ 0 ≤ I(γ_2).

*Proof.* Take q_1 ∈ γ_1 and q_2 ∈ γ_2 as in [SM]. Since d is Lipschitz, |J_t(y) − J_t(q_2)| is bounded for t ≥ 0 and |J_t(y) − J_t(q_1)| is bounded for t ≤ 0.
* If I(γ_2) < 0, then J_t(y) ≤ C − (|I(γ_2)|/P_2)t for t ≥ 0, and d(g_{−mP_1}y, q_1) ≤ C′e^{−cmP_1}. Lemma K with p = q_1 gives a contradiction.
* If I(γ_1) > 0, Lemma K′ with p = q_2 gives a contradiction in the same way. ∎

**Corollary 3.3 (no homoclinic points).** Assume GH and n ≥ 2. No hyperbolic periodic orbit or hyperbolic zero γ has a homoclinic point, transverse or not.
*Proof.* Corollary 3.2 with γ_1 = γ_2 = γ gives I(γ) = 0. This contradicts Lemma 1.3. ∎

---

## 4. Reduction to ergodic measures

**Lemma 4.1.** If h_top(g_1) > 0, there is a g_1-invariant, g_1-ergodic Borel probability μ with h_μ(g_1) > 0. For such μ, the measure μ̄ := ∫_0^1 (g_s)_*μ ds is flow-invariant and flow-ergodic, with h_{μ̄}(g_1) = h_μ(g_1) and μ̄(d) = ∫J_1 dμ.

*Proof.* [VP] gives a g_1-invariant μ_0 with h_{μ_0}(g_1) > 0. By Jacobs' theorem some ergodic component μ has h_μ(g_1) > 0.
* μ̄ is flow-invariant because (g_1)_*μ = μ.
* A flow-invariant Borel set A is g_1-invariant, so (g_s)_*μ(A) = μ(A) ∈ {0,1}, and μ̄(A) = μ(A). Hence μ̄ is flow-ergodic.
* Each (g_s)_*μ is g_1-ergodic with h_{(g_s)_*μ}(g_1) = h_μ(g_1), since g_s conjugates g_1 to itself. Jacobs' formula for the decomposition μ̄ = ∫_0^1(g_s)_*μ ds gives h_{μ̄}(g_1) = h_μ(g_1).
* Finally μ̄(d) = ∫_0^1 ∫ d∘g_s dμ ds = ∫J_1dμ. ∎

**Lemma 4.2 (g_1-components of a flow-ergodic measure).** Let μ̄ be flow-invariant and flow-ergodic, and let μ̄ = ∫μ_ω dω be its g_1-ergodic decomposition. Then for a.e. ω, h_{μ_ω}(g_1) = h_{μ̄}(g_1) and ∫J_1 dμ_ω = μ̄(d). In particular, if h_{μ̄}(g_1) > 0, then every (a.e.) g_1-ergodic component has positive entropy and the same value of ∫J_1.

*Proof.* Let x ↦ μ_x be the g_1-ergodic decomposition map (defined μ̄-a.e., g_1-invariant). Since g_s commutes with g_1, the decomposition is g_s-equivariant: μ_{g_sx} = (g_s)_*μ_x for μ̄-a.e. x. Now (g_s)_*μ_x has the same g_1-entropy as μ_x (g_s conjugates g_1 to itself), and the same integral of J_1: J_1∘g_s = J_{1+s} − J_s = J_1 + J_s∘g_1 − J_s by the cocycle identity, and ∫(J_s∘g_1 − J_s)dμ_x = 0 by g_1-invariance. Hence x ↦ h_{μ_x}(g_1) and x ↦ ∫J_1dμ_x are flow-invariant measurable functions, so they are μ̄-a.e. constant by flow-ergodicity. Their constant values are h_{μ̄}(g_1) (Jacobs) and ∫J_1dμ̄ = μ̄(d) (flow invariance of μ̄). ∎

*Derivation of the identity used above.* By the cocycle identity, J_{1+s} = J_s + J_1∘g_s and also J_{1+s} = J_1 + J_s∘g_1; subtracting gives J_1∘g_s = J_1 + J_s∘g_1 − J_s.

For a flow-ergodic μ̄, the Lyapunov exponents of Dg_1 are flow-invariant functions, hence constant μ̄-a.e. If μ̄(Zero(X)) = 0, the exponent in the direction of X is 0. (This is the exponent of v = X(x), since Dg_tX(x) = X(g_tx). The limit of (1/t)log|X(g_tx)| exists a.e. by [Os], and it must be 0, because (f∘g_t)/t → 0 in measure for the a.e.-finite function f = log|X|.)

---

## 5. Non-hyperbolicity in every dimension; the problem in dimension ≤ 3

**Theorem B.** Assume GH and n ≥ 2. Let μ be a flow-invariant, flow-ergodic probability with h_μ(g_1) > 0. Then μ is not hyperbolic: besides the exponent 0 in the flow direction, μ has another zero Lyapunov exponent.

*Proof.*
1. μ(Zero(X)) = 0. Otherwise, by ergodicity, μ is carried by the closed invariant set Zero(X), on which g_1 = id, and h_μ(g_1) = 0.
2. So the flow direction carries the exponent 0 (§4).
3. [Ru] for g_1 and for g_{−1} (h_μ(g_{−1}) = h_μ(g_1) > 0) gives a positive and a negative exponent.
4. If all exponents other than the one in the flow direction were nonzero, [KLY] would give a hyperbolic periodic orbit with a homoclinic point. This contradicts Corollary 3.3. ∎

**Theorem A (the problem in dimension ≤ 3).** If X is GH and dim M ≤ 3, then h_top(g_1) = 0.

*Proof.*
* If n = 1, M is a circle and g_1 is a circle homeomorphism, which has zero entropy.
* Let n ∈ {2,3} and suppose h_top(g_1) > 0. Lemma 4.1 gives a flow-ergodic μ̄ with h_{μ̄}(g_1) > 0. By steps 1–3 of the proof of Theorem B, μ̄ has the exponent 0 (flow direction), a positive exponent and a negative exponent.
* If n = 2 this is three exponents in dimension 2, which is impossible.
* If n = 3 the exponents are exactly χ^+ > 0, 0 (flow) and χ^− < 0, so μ̄ is hyperbolic. This contradicts Theorem B. ∎

---

## 6. The mean divergence of a positive-entropy measure

Throughout this section, f := g_1 and μ is an f-invariant, f-ergodic probability with h_μ(f) > 0. We put λ := ∫J_1 dμ (= μ̄(d), Lemma 4.1).

By Birkhoff's theorem applied to f and f^{−1} with the function J_1 (and |J_t − J_{⌊t⌋}| ≤ ‖d‖_∞), J_t(x)/t → λ as t → ±∞ for μ-a.e. x. Let χ^+_min be the smallest positive exponent and χ^−_max the negative exponent closest to 0. Both exist by [Ru] applied to f and f^{−1}.

**Lemma 6.0 (non-atomic unstable conditionals).** Let ξ be as in [LS]. Then for μ-a.e. x the conditional measure μ^ξ_x is non-atomic.

*Proof.*
* ξ refines fξ. Put w(x) := μ^ξ_x({x}). By invariance, μ^{fξ}_{fx} = f_*μ^ξ_x, and μ^ξ_{fx} is μ^{fξ}_{fx} restricted to ξ(fx) and normalised. So w(fx) = w(x)/μ^{fξ}_{fx}(ξ(fx)) ≥ w(x).
* Hence ∫(w∘f − w)dμ = 0 with a nonnegative integrand, so w∘f = w a.e., and w = w_0 a.e. by ergodicity.
* If w_0 > 0, then μ^{fξ}_{fx}(ξ(fx)) = 1 a.e. So ξ = fξ mod μ, and h_μ(f) = H(ξ|fξ) = 0, a contradiction. So w = 0 a.e.
* The μ-measure of the set of points that are atoms of their own conditional is ∫w dμ = 0. It also equals ∫μ^ξ_x(atoms of μ^ξ_x)dμ(x). So a.e. conditional is non-atomic. ∎

Since conditionals of a full-measure set are full for a.e. x, Lemma 6.0 implies the following. For a.e. x and any full-measure set G, ξ(x) ∩ G is uncountable; in particular it contains infinitely many points y ≠ x.

### 6.1 The band (proved modulo [P], [LS])

**Theorem C.** Assume GH. Then neither −χ^+_min < λ < 0 nor 0 < λ < |χ^−_max| holds.

*Proof.* Suppose −χ^+_min < λ < 0. Choose δ > 0 with λ + δ < 0 and θ := χ^+_min − δ > |λ| + δ.
1. Let G be the full-measure set of z with J_t(z)/t → λ as t → ±∞. By [P], [LS] and Lemma 6.0, there are x ∈ G and y ∈ G ∩ ξ(x), y ≠ x, with d(f^{−m}x, f^{−m}y) ≤ C e^{−θm} for m ≥ 0. Interpolating with Lip(g_{−r}), r ∈ [0,1], gives d(g_tx, g_ty) ≤ Ce^{−θ|t|} for t ≤ 0.
2. For t ≤ 0, J_t(x) − J_t(y) = −∫_t^0(d(g_sx) − d(g_sy))ds. The integrand is O(e^{−θ|s|}), so b := lim_{t→−∞}(J_t(x) − J_t(y)) exists and |J_t(x) − J_t(y) − b| ≤ Ce^{−θ|t|}.
3. Let S := δ_x − e^bδ_y ≠ 0.
   * For t ≥ 0: J_t(x), J_t(y) ≤ C + (λ+δ)t, so |S(Γ_tφ)| ≤ Ce^{(λ+δ)t}‖φ‖_∞.
   * For t ≤ 0:

     S(Γ_tφ) = e^{J_t(x)}[(φ(g_tx) − φ(g_ty)) + (1 − e^{b + J_t(y) − J_t(x)})φ(g_ty)],

     so |S(Γ_tφ)| ≤ Ce^{J_t(x)}e^{−θ|t|}‖φ‖_{C^1} ≤ C′e^{−(θ − |λ| − δ)|t|}‖φ‖_{C^1}.
4. Theorem J gives S = 0, a contradiction.

The case 0 < λ < |χ^−_max| follows by applying this to −X, which is GH. Its time-one map is f^{−1}, its exponents are the negatives of those of μ, and its λ is −λ. ∎

### 6.2 The general statement λ = 0

**Theorem C′.** Assume GH. Then λ = 0, i.e. every g_1-ergodic μ with h_μ(g_1) > 0 has ∫J_1dμ = 0, and every flow-ergodic positive-entropy μ̄ has μ̄(div_ν X) = 0. This is proved modulo [P], [LS] and [NF] (§6.3). When dim E^u = 1 and λ < 0, or dim E^s = 1 and λ > 0, [NF] reduces to the classical affine parameters on one-dimensional leaves.

The proof is in §6.3; it treats a g_1-ergodic μ. The statement for a flow-ergodic μ̄ follows from Lemma 4.2, applied to its (positive-entropy) g_1-ergodic components. Here are its consequences.

**Corollary C″ (exact reformulation; modulo [NF]).** For a GH field X the following are equivalent:
(i) h_top(g_1) = 0;
(ii) **(PE0)** there is no g_1-invariant, g_1-ergodic Borel probability μ with h_μ(g_1) > 0 and ∫J_1dμ = 0.
Equivalently (by Lemma 4.1): there is no flow-ergodic μ̄ with h_{μ̄}(g_1) > 0 and μ̄(div_ν X) = 0. By Theorem B such a μ̄ would also be non-hyperbolic.

*Proof.* (i) ⇒ (ii) is trivial by [VP]. (ii) ⇒ (i): Lemma 4.1 gives a g_1-ergodic μ with positive entropy, and Theorem C′ gives ∫J_1dμ = 0, contradicting (ii). ∎

Without [NF], Theorems B and C give the following weaker but unconditional reduction. The problem holds for GH fields provided no flow-ergodic positive-entropy μ̄ is non-hyperbolic with μ̄(d) ∈ (−∞, −χ^+_min] ∪ {0} ∪ [|χ^−_max|, ∞).

**Corollary C‴ (dimension 4; modulo [P], [LS] and the one-dimensional affine parameters).** If X is GH and n = 4, then every flow-ergodic μ̄ with h_{μ̄}(g_1) > 0 has simple exponents χ > 0 = 0 > −χ and μ̄(d) = 0.
*Proof.*
* By Theorem B there are two zero exponents (flow and centre), and [Ru] gives one positive and one negative exponent, each simple.
* Theorem C′ in its one-dimensional case (E^u for λ < 0, E^s for λ > 0) gives λ = 0.
  (Apply it to a g_1-ergodic component μ of μ̄; by Lemma 4.2, μ has positive entropy and ∫J_1dμ = μ̄(d).)
* The sum of all exponents at a regular point x equals lim_{t→∞}(1/t)log|det Dg_t(x)| = lim_{t→∞} J_t(x)/t (the determinant relative to ν differs from that relative to the Riemannian volume by a bounded factor), and J_t(x)/t = (1/t)∫_0^t d(g_sx)ds → μ̄(d) μ̄-a.e. by Birkhoff's theorem for the flow-ergodic μ̄. So the sum is μ̄(d) = 0, and the two nonzero exponents are opposite. ∎

**Proposition 6.5 (full support; GH and [At] only, no Pesin theory).** Assume GH. Let μ be a g_1-invariant, g_1-ergodic probability with ∫J_1 dμ = 0 (no entropy assumption). Then for μ-a.e. x the forward orbit {g_tx : t ≥ 0} is dense in M; in particular supp μ = M. Combined with Theorem C′: under GH (and modulo [NF]) every positive-entropy ergodic measure has full support, and the flow is topologically transitive if h_top(g_1) > 0.

*Proof.*
1. By [At] applied to T = g_1 and f = J_1 (note Σ_{j<n}J_1(g_jx) = J_n(x) by the cocycle identity), for μ-a.e. x there are integers n_1 < n_2 < … → ∞ with |J_{n_i}(x)| < 1. Fix such an x.
2. Put Z(T) := ∫_0^T e^{J_t(x)} dt and m_T := Z(T)^{−1}∫_0^T e^{J_t(x)} δ_{g_tx} dt, a Borel probability carried by the forward orbit of x. Since |J_t(x) − J_{n_i}(x)| ≤ ‖d‖_∞ for t ∈ [n_i, n_i + 1], each interval [n_i, n_i+1] contributes at least e^{−1−‖d‖_∞} to Z, so Z(n_k) ≥ (k − 1)e^{−1−‖d‖_∞} → ∞.
3. By d/dt[e^{J_t(x)}φ(g_tx)] = e^{J_t(x)}(Pφ)(g_tx), m_{n_k}(Pφ) = (e^{J_{n_k}(x)}φ(g_{n_k}x) − φ(x))/Z(n_k), which is at most (e + 1)‖φ‖_∞/Z(n_k) → 0 in modulus.
4. Let m be a weak-* limit point of (m_{n_k}); it is a probability measure with m(Pφ) = 0 for every smooth φ. By (F1), m = cν with c = 1/ν(M) > 0. So supp m = M. But m is carried by the closure of the forward orbit of x. Hence that orbit is dense.
5. supp μ is closed and contains μ-a.e. x, hence contains a point with dense forward orbit, hence the closure of that orbit, which is M. ∎

### 6.3 Proof of Theorem C′

By the time reversal of §0.1 (−X is GH, its λ is −λ, and E^u and E^s are exchanged) it suffices to treat λ < 0. Notation:
* χ_1 > … > χ_l > 0 are the distinct positive exponents, u := dim E^u, and d_0 := ⌊χ_1/χ_l⌋.
* x_m := f^{−m}x.

**[NF] as used.** There is a full-measure set on which, for each x, there is a C^∞ diffeomorphism H_x : W^u(x) → E^u_x with H_x(x) = 0 and D_xH_x = Id, such that the following hold.
(b) P_x := H_{x_1}∘f^{−1}∘H_x^{−1} is a *sub-resonance polynomial map*. Its E_i-component contains only monomials ∏_j(coordinates in E_j)^{s_j} with Σ_j s_jχ_j ≤ χ_i, where E^u = ⊕E_j is the Lyapunov splitting.
(c) The quantities used below (Lipschitz constants of H_x on intrinsic balls, C^{K+1} norms of H_x^{−1} on balls) are measurable in x.
For u = 1, H_x is the classical affine parameter of the leaf, and P_x is linear.

**Lemma 6.1 (closure and degree).** P^{(m)}_x := P_{x_{m−1}}∘⋯∘P_x satisfies H_{x_m}∘f^{−m} = P^{(m)}_x∘H_x on W^u(x), and it is a sub-resonance polynomial map of degree ≤ d_0.
*Proof.*
* The conjugacy follows from (b) by induction.
* Give coordinates in E_j the weight χ_j. Sub-resonance means each E_i-component contains only monomials of weight ≤ χ_i. Substituting such maps into such a monomial yields monomials of weight ≤ χ_i, because weights add under multiplication. So compositions are sub-resonance.
* Every weight is ≥ χ_l, so an allowed monomial of total degree |s| satisfies |s|χ_l ≤ χ_1. ∎

**Lemma 6.2 (Markov-type bound).** For r_0 > 0 there are M_j with ‖Q‖_{C^j(B(0,r_0))} ≤ M_j sup_{B(0,r_0)}|Q| for every polynomial map Q between u-dimensional Euclidean spaces of degree ≤ d_0.
*Proof.* Both sides are norms on a finite-dimensional space, and all norms there are equivalent. ∎

**Lemma 6.3 (good times).** Let G be measurable with μ(G) > 0, and let δ > 0. For a.e. x there is C(x) such that for every real T ≥ 0 there is an integer m ≥ T with x_m ∈ G and m − T ≤ δT + C(x).
*Proof.* By Birkhoff for f^{−1}, N(m) := #{0 ≤ j < m : x_j ∈ G} = mμ(G) + o(m). An interval [T, (1+δ)T] with T large that contains no such j would give N((1+δ)T) = N(T) + O(1), which is impossible. ∎

**The Jacobian holonomy.** For z backward-exponentially asymptotic to w, put β_w(z) := ∫_{−∞}^0(d(g_sz) − d(g_sw))ds. Then

  β_{g_sw}(g_sz) = β_w(z) + J_s(z) − J_s(w) (s ∈ ℝ),  β_w(z) = Σ_{m≥0}[b(f^{−m}z) − b(f^{−m}w)],  b := ∫_{−1}^0 d∘g_s ds.   (6.1)

Fix K ≥ 1 and embed M in some ℝ^N. For L ≥ 1, let G′_L be the set of points w of the full-measure set of [P] and [NF] satisfying:
(G1) |H_w(y)| ≤ L d^u(y,w) for d^u(y,w) ≤ 1/L;
(G2) ‖H_w^{−1}‖_{C^{K+1}(B(0,1/L))} ≤ L.
Then μ(G′_L) > 0 for L large.

**Lemma 6.4.** For a.e. w, β_w∘H_w^{−1} is C^{K+1} near 0.
*Proof.*
* Fix r_0 > 0, let B_w := B(0,r_0) ⊂ E^u_w and Q := H_w^{−1}(B̄_w). Fix δ with δ(c_K + 2) < χ_l, where ‖b∘f^m‖_{C^{K+1}} ≤ Ce^{c_Km} for m ≥ 0.
* By Lemma 6.3 (G = G′_L), for each m there is m′ ≥ m with w_{m′} ∈ G′_L and m′ − m ≤ δm + C.
* By [P], d^u(f^{−m′}y, w_{m′}) ≤ Ce^{−(χ_l−δ)m′} for y ∈ Q. So (G1) and Lemma 6.1 give sup_{B_w}|P^{(m′)}_w| ≤ LCe^{−(χ_l−δ)m′}, and by Lemma 6.2 ‖P^{(m′)}_w‖_{C^{K+1}(B_w)} ≤ C′e^{−(χ_l−δ)m′}.
* By Lemma 6.1, on B_w,

  T_m(z) := b(f^{−m}H_w^{−1}z) − b(w_m) = Φ_m(P^{(m′)}_wz) − Φ_m(0),  Φ_m := b∘f^{m′−m}∘H_{w_{m′}}^{−1},

  and by (G2) ‖Φ_m‖_{C^{K+1}(B(0,1/L))} ≤ C″e^{c_Kδm}.
* By Faà di Bruno, ‖T_m‖_{C^{K+1}(B_w)} ≤ Ce^{c_Kδm}e^{−(χ_l−δ)m}, which is summable. Finitely many initial terms are smooth.
* By (6.1), β_w∘H_w^{−1} = Σ_mT_m converges in C^{K+1}(B_w). ∎

Let G_L ⊂ G′_L be the subset where also (G3) ‖β_w∘H_w^{−1}‖_{C^{K+1}(B(0,1/L))} ≤ L. Then μ(G_L) > 0 for L large.

*Proof of Theorem C′ for λ < 0.*

**Constants.** Choose K with (K+1)χ_l > |λ| + 1. Let c′_K be such that ‖J_s‖_{C^{K+1}} and ‖φ∘g_s‖_{C^{K+1}}/‖φ‖_{C^{K+1}} are ≤ Ce^{c′_Ks} for s ≥ 0, and put c″_K := (K+2)c′_K + 2‖d‖_∞. Choose δ > 0 with λ + δ < 0, δ(c_K + 2) < χ_l and (K+1)(χ_l − δ) − |λ| − δ − δc″_K ≥ 1/2. Fix L with μ(G_L) > 0.

**Step 1.** Choose x such that:
* [P], [NF] and Lemma 6.4 hold at x;
* J_t(x)/t → λ as t → −∞;
* Lemma 6.3 holds for G = G_L;
* μ^ξ_x is non-atomic and gives full mass to G_fwd := {y : J_t(y)/t → λ as t → +∞}.

Let D := Kd_0, and let N_D be the dimension of the space of polynomials of degree ≤ D on E^u_x. Pick N_D + 1 distinct points y_0, …, y_{N_D} ∈ ξ(x) ∩ G_fwd and put z_i := H_x(y_i); these are distinct.

**Step 2.** Choose w ≠ 0 with Σ_iw_iQ(z_i) = 0 for all polynomials Q of degree ≤ D (N_D equations, N_D + 1 unknowns). Put S := Σ_iw_ie^{β_x(y_i)}δ_{y_i} ≠ 0.

**Step 3 (t ≥ 0).** Each y_i ∈ G_fwd, so |S(Γ_tφ)| ≤ Ce^{(λ+δ)t}‖φ‖_∞.

**Step 4 (t ≤ 0).**
* By Lemma 6.3 choose m′ ≥ |t| with x_{m′} ∈ G_L and s := m′ − |t| ∈ [0, δ|t| + C]. Then g_t = g_s∘f^{−m′}. Put y_i′ := f^{−m′}y_i.
* By (6.1) and the cocycle identity,

  S(Γ_tφ) = e^{J_t(x)}Σ_iw_iΨ(y_i′),  Ψ(y) := exp(β_{x_{m′}}(y) + J_s(y) − J_s(x_{m′}))φ(g_sy).

* Θ := Ψ∘H_{x_{m′}}^{−1} satisfies ‖Θ‖_{C^{K+1}(B(0,1/L))} ≤ C(L,K)e^{c″_Ks}‖φ‖_{C^{K+1}}, by (G2), (G3) and |J_s| ≤ s‖d‖_∞.
* The points ζ_i := H_{x_{m′}}(y_i′) = P^{(m′)}_xz_i satisfy |ζ_i| ≤ LCe^{−(χ_l−δ)m′} by [P] and (G1).
* Write Θ = T_KΘ + R, where T_KΘ is the degree-K Taylor polynomial at 0 and |R(ζ)| ≤ C_K‖Θ‖_{C^{K+1}}|ζ|^{K+1}. Then (T_KΘ)∘P^{(m′)}_x is a polynomial of degree ≤ D (Lemma 6.1), so its moment Σ_iw_i(T_KΘ)(ζ_i) vanishes. Hence |Σ_iw_iΨ(y_i′)| ≤ Ce^{c″_Ks}e^{−(K+1)(χ_l−δ)m′}‖φ‖_{C^{K+1}}.
* Since x is backward generic and λ < 0, e^{J_t(x)} ≤ Ce^{(|λ|+δ)|t|}.
* By the choice of δ, |S(Γ_tφ)| ≤ Ce^{−|t|/2}‖φ‖_{C^{K+1}} for t ≤ −m_1. The bounded range −m_1 < t ≤ 0 is trivial.

**Step 5.** Theorem J gives S = 0, contradicting Step 2. ∎

---
## 7. The volume-preserving case in every dimension, and the reduction of the problem to a smooth invariant volume

In §§7.0–7.3, ω is a smooth positive density with L_Xω = 0, normalised so that ω(M) = 1. We take ν = ω, so the divergence is 0, J ≡ 0 and P = X. In these subsections d(·,·) always denotes the Riemannian distance. Functions are real-valued; complex-valued ones are handled through real and imaginary parts. Call X **cohomology-free (CF)** if every smooth f can be written f = c + Xu with c a constant and u smooth.

### 7.0 GH with an invariant volume

**Proposition 7.1.** Suppose X preserves a smooth positive density ω, ω(M) = 1.
(a) X is GH if and only if X is CF. More precisely, under GH, X(C^∞) = {f ∈ C^∞ : ∫f dω = 0}.
(b) If X is GH, the flow is uniquely ergodic with invariant measure ω, and it is minimal.

*Proof.*
* **GH ⇒ CF.** X(C^∞) ⊂ ker ω, since ∫Xu dω = −∫u L_Xω = 0. By Lemma 1.4, X(C^∞) is closed. If f ∈ ker ω were not in X(C^∞), Hahn–Banach would give a continuous linear functional T on C^∞ with T(Xφ) = 0 for all φ and T(f) ≠ 0. For u := T/ω, (0.1) (with P = X) gives Xu = 0, so u is constant (Lemma 1.1) and T = cω; then T(f) = c∫f dω = 0, a contradiction. Hence X(C^∞) = ker ω, and every f equals ∫f dω + Xu.
* **CF ⇒ GH.** No smooth u has Xu = 1 (look at a maximum of u). So in f = c + Xu the constant is unique; call it c(f). It is linear, its kernel is X(C^∞), and c(f) = ∫f dω because ∫Xu dω = 0. If T is a distribution density with T(Xφ) = 0 for all φ, T annihilates X(C^∞) = ker ω, so T = T(1)ω. Now let u ∈ D′ with Xu = f smooth. Then ∫f dω = −⟨u, L_Xω⟩ = 0, so f = Xv with v smooth. Then X(u − v) = 0, so the density (u − v)ω annihilates X(C^∞) and equals cω. Hence u = v + c is smooth.
* **(b).** For any invariant probability m, m(Xu) = 0 for smooth u, so m(f) = ∫f dω for all f. This is unique ergodicity. Every orbit closure carries an invariant probability, which must be ω, whose support is M. Hence every orbit is dense. ∎

**Lemma 7.2 (no zeros).** If X is GH and L_Xω = 0, then X has no zeros.

*Proof.* Let X(p) = 0 and let u be the distribution with uω = δ_p. By (0.1) with ν = ω, ⟨Xu, φω⟩ = −(Xφ)(p) = 0 for all φ. So Xu = 0, and by GH u is smooth, which is impossible since δ_p is not of the form vω with v smooth. ∎

From now on in §§7.1–7.3 we assume **n = dim M ≥ 2**. (For n = 1, M is a circle, g_1 is a circle homeomorphism and has zero entropy; see Theorem A.) By Lemma 7.2, V := max|X| > 0 and min|X| > 0.

### 7.1 Geometric preliminaries

**Norms.** Fix a finite atlas κ_α : U_α → ℝ^n and compact sets K_α ⊂ U_α whose interiors cover M, and put ‖φ‖_{C^m} := max_α max_{|β|≤m} sup_{K_α}|∂^β(φ∘κ_α^{−1})|. Then ‖φ‖_∞ ≤ ‖φ‖_{C^m} and ‖1‖_{C^m} = 1. Since M is connected and d is the length metric,

  (L) |φ(a) − φ(b)| ≤ ‖dφ‖_∞ d(a,b),  and Lip(G) ≤ sup_x‖DG(x)‖ for a C^1 map G : M → M,

where ‖dφ‖_∞ is the supremum of the Riemannian norm of dφ. Also d(g_sz, g_{s′}z) ≤ V|s − s′|, since the orbit arc is a curve of length ≤ V|s − s′|.

**Radius r_*.** By [An], fix r_* ∈ (0,1] such that 2r_* is less than the injectivity radius (so (p,x) ↦ d(p,x)^2 is smooth on {d(p,x) < 2r_*}) and c_ω ρ^n ≤ ω(B(p,ρ)) ≤ C_ω ρ^n for all p ∈ M and 0 < ρ ≤ r_*.

**Lemma 7.3 (bumps).** Fix m ≥ 1. There is C_b ≥ 1 such that for every p ∈ M and 0 < ρ ≤ r_* there is b = b_{p,ρ} ∈ C^∞(M) with 0 ≤ b ≤ 1, b = 1 on the closed ball B̄(p, ρ/2), supp b ⊂ B̄(p, 3ρ/4), and ‖b‖_{C^m} ≤ C_b ρ^{−2m}.

*Proof.* Fix χ ∈ C^∞(ℝ), nonincreasing, with χ = 1 on (−∞, 1/4] and χ = 0 on [9/16, ∞). Put b(x) := χ(d(p,x)^2/ρ^2) if d(p,x) < 2r_* and b(x) := 0 otherwise. On the open set {d(p,·) < 2r_*} b is smooth, and on the open set {d(p,·) > 3ρ/4} it vanishes; these sets cover M, so b is smooth, and the other properties except the norm bound are immediate. For the norm: fix α, |β| ≤ m and x ∈ K_α with d(p,x) ≤ 3ρ/4 ≤ r_* (elsewhere the derivative vanishes). The set Q_α := {(p,x) : x ∈ K_α, d(p,x) ≤ r_*} is compact and lies in the open set where d^2 is smooth, so all chart derivatives of order ≤ m of D_p := d(p, κ_α^{−1}(·))^2 are bounded on Q_α by a constant A. By the chain rule, ∂^β[χ(D_p/ρ^2)] is a sum of at most Bell(m) terms χ^{(k)}(D_p/ρ^2) ρ^{−2k} ∏_{i=1}^k ∂^{β_i}D_p with 1 ≤ k ≤ |β|, each bounded by ‖χ‖_{C^m} max(1,A)^m ρ^{−2m} because ρ ≤ 1. ∎

**Lemma 7.4 (flow constants).**
(a) There are τ_0 ∈ (0,1] and c_0 > 0 with d(z, g_sz) ≥ c_0|s| for all z ∈ M and |s| ≤ τ_0.
(b) There is h_0 ∈ (0,1] with Lip(g_h) ≤ 2 for 0 ≤ h ≤ h_0.

*Proof.* (a) If not, there are z_k ∈ M and s_k ≠ 0, s_k → 0, with d(z_k, g_{s_k}z_k) < |s_k|/k; pass to a subsequence with z_k → z. Take a chart κ around z and a compact neighbourhood W of z in it on which |κa − κb| ≤ λ d(a,b). Let Y := κ_*X; Y(κz) ≠ 0 by Lemma 7.2. For k large and |σ| ≤ |s_k|, g_σz_k ∈ W and |Y(κg_σz_k) − Y(κz)| ≤ |Y(κz)|/2, so |κ(g_{s_k}z_k) − κ(z_k)| = |∫_0^{s_k}Y(κg_σz_k)dσ| ≥ |s_k||Y(κz)|/2, whence d(z_k, g_{s_k}z_k) ≥ |s_k||Y(κz)|/(2λ), contradicting the choice of z_k for k large.
(b) (h,x) ↦ ‖Dg_h(x)‖ is continuous on [0,1] × M, so h ↦ sup_x‖Dg_h(x)‖ is continuous and equals 1 at h = 0. Choose h_0 so that it is ≤ 2 on [0,h_0] and use (L). ∎

**Partitions.** For 0 < η ≤ r_* there is a partition of M into at most C_Mη^{−n} Borel sets of diameter ≤ η/2, where C_M := 8^n/c_ω. Indeed, let {p_j} be a maximal η/4-separated set. The balls B(p_j, η/8) are disjoint, so there are at most 1/(c_ω(η/8)^n) points; the balls B(p_j, η/4) cover M by maximality; and A_j := B(p_j, η/4) ∖ ∪_{i<j}B(p_i, η/4) has diameter ≤ η/2.

### 7.2 The tame inverse and the occupation identity

**Lemma 7.5 (tame inverse).** Assume GH and L_Xω = 0. There are m ∈ ℕ, m ≥ 1, and C_1 such that every f ∈ C^∞ with ∫f dω = 0 can be written f = Xu with u ∈ C^∞ and ‖du‖_∞ ≤ C_1‖f‖_{C^m}.

*Proof.* Apply Lemma 1.4 with ω₀ := ω, at a level r > n/2 + 1: there are j and C′ with ‖u − c(u)‖_{H^r} ≤ C′‖Xu‖_{H^j} for smooth u, where c(u) = ∫u dω. By Proposition 7.1(a), f = Xu for some smooth u; replace u by u − c(u). Then by [An]
‖du‖_∞ ≤ A_0‖u‖_{C^1} ≤ A_0C_S‖u‖_{H^r} ≤ A_0C_SC′‖f‖_{H^j} ≤ A_0C_SC′C_j‖f‖_{C^j},
where A_0 compares ‖dφ‖_∞ with ‖φ‖_{C^1}, C_S is the Sobolev constant and C_j compares H^j with C^j. Put m := max(j,1) and C_1 := A_0C_SC′C_j. ∎

**Corollary 7.6 (occupation identity).** For f ∈ C^∞, x ∈ M and T ≥ 0 put γ_x^T(f) := ∫_0^T f(g_sx) ds. If u is as in Lemma 7.5 for f − ∫f dω, then

  γ_x^T(f) − T∫f dω = u(g_Tx) − u(x),

and consequently, for all x, y ∈ M,

  |γ_x^T(f) − γ_y^T(f)| ≤ 2C_1‖f‖_{C^m}(d(x,y) + d(g_Tx, g_Ty)).   (A1)

*Proof.* (d/ds)u(g_sx) = (Xu)(g_sx) = f(g_sx) − ∫f dω; integrate over [0,T]. For (A1), subtract the identities for x and y (the terms T∫f dω cancel) and use (L) with ‖du‖_∞ ≤ C_1‖f − ∫f dω‖_{C^m} ≤ 2C_1‖f‖_{C^m}. ∎

### 7.3 Theorem V

**Lemma 7.7 (polynomial no-near-return; uses n ≥ 2).** Put K := (2m+1)/(n−1). There is c_B > 0 such that d(z, g_rz) ≥ c_B(1+r)^{−K} for all z ∈ M and all r ≥ τ_0.

*Proof.* Since n ≥ 2 we can fix c ∈ (0, r_*] with C_ω(2Vc^{n−1} + 2c^n) ≤ 1/2. Given z and r ≥ τ_0, put ρ := c(1+r)^{−1/(n−1)} ≤ r_* ≤ 1, Δ := ρ/(2V), N := ⌈r/Δ⌉, p_i := g_{iΔ}z (0 ≤ i ≤ N), b_i := b_{p_i,ρ} (Lemma 7.3) and F := Σ_{i=0}^N b_i ≥ 0.
* *F ≥ 1 on the segment.* For s ∈ [0,r] let i := ⌊s/Δ⌋ ≤ N. Then d(g_sz, p_i) ≤ V(s − iΔ) ≤ VΔ = ρ/2, so b_i(g_sz) = 1. Hence γ_z^r(F) ≥ r.
* *Mass.* N + 1 ≤ 2Vr/ρ + 2, so ∫F dω ≤ (N+1)C_ωρ^n ≤ C_ω(2Vrρ^{n−1} + 2ρ^n) = C_ω(2Vc^{n−1}r/(1+r) + 2ρ^n) ≤ 1/2.
* *Norm.* Since ρ ≤ 1, N + 1 ≤ (2V+2)(1+r)/ρ, so ‖F‖_{C^m} ≤ (N+1)C_bρ^{−2m} ≤ C_b(2V+2)c^{−(2m+1)}(1+r)^{1+K} =: A_3(1+r)^{1+K}.
* By Corollary 7.6, with u for F − ∫F dω and ‖du‖_∞ ≤ 2C_1‖F‖_{C^m}:
  r/2 ≤ γ_z^r(F) − r∫F dω = u(g_rz) − u(z) ≤ 2C_1A_3(1+r)^{1+K} d(z, g_rz).
Since r ≥ τ_0 implies r ≥ (τ_0/(1+τ_0))(1+r), the claim holds with c_B := τ_0/(4C_1A_3(1+τ_0)). ∎

(For n = 1 the scale ρ does not exist, and indeed periodic orbits on the circle return exactly.)

**Lemma 7.8 (Hausdorff closeness).** Put C_C := 8VC_1C_b and ρ(η) := (C_Cη)^{1/(2m+1)}. Let x, y ∈ M, T ≥ 1 and η > 0 with d(x,y) + d(g_Tx, g_Ty) ≤ η, and suppose ρ := ρ(η) ≤ min(r_*, 2V). Then for every t ∈ [0,T] there is σ ∈ [0,T] with d(g_ty, g_σx) ≤ ρ.

*Proof.* Let q := g_ty and suppose d(q, g_{[0,T]}x) > ρ (the segment is compact, so this is the negation). Let ψ := b_{q,ρ}. Its support lies in B̄(q, 3ρ/4), disjoint from the segment, so γ_x^T(ψ) = 0. Put w := ρ/(2V) ≤ 1 ≤ T and I := [t − w, t + w] ∩ [0,T]. For s ∈ I, d(g_sy, q) ≤ V|s − t| ≤ ρ/2, so ψ(g_sy) = 1. The length of I is ≥ w: if t + w ≤ T it contains [t, t+w]; if t + w > T and t ≥ w it contains [t − w, t]; if t + w > T and t < w it is [0,T], of length T ≥ w. So γ_y^T(ψ) ≥ ρ/(2V). By (A1) and Lemma 7.3, ρ/(2V) ≤ 2C_1C_bρ^{−2m}η, i.e. ρ^{2m+1} ≤ 4VC_1C_bη = C_Cη/2 < C_Cη = ρ^{2m+1}. Contradiction. ∎

**Lemma 7.9 (shadowing in time).** Put B := (2m+1)(K+2), η_T := T^{−B} and ρ_T := ρ(η_T) = C_C^{1/(2m+1)}T^{−(K+2)}. For every ε > 0 there is T_0(ε) ≥ 1 such that, if T ≥ T_0(ε) and x, y ∈ M satisfy d(x,y) + d(g_Tx, g_Ty) ≤ η_T, then d(g_tx, g_ty) < ε for all t ∈ [0,T].

*Proof.* Write ρ := ρ_T. Choose T_0(ε) ≥ 1 such that for all T ≥ T_0(ε):
(1) ρ ≤ min(r_*, 2V); (2) η_T ≤ ρ; (3) 3ρ < c_B(T+2)^{−K}; (4) 2ρ + 12VTρ/(c_0h_0) < ε.
This is possible: ρ → 0; η_T/ρ = C_C^{−1/(2m+1)}T^{−(B−K−2)} → 0 because B > K + 2 (as m ≥ 1); ρ(T+2)^K ≤ C_C^{1/(2m+1)}3^KT^{−2} → 0; and Tρ = C_C^{1/(2m+1)}T^{−K−1} → 0.
(i) *Separation of times.* If s_1, s_2 ∈ [0, T+1] and d(g_{s_1}x, g_{s_2}x) ≤ 3ρ, then |s_1 − s_2| ≤ 3ρ/c_0. Indeed, let r := |s_1 − s_2| ≤ T + 1. If r ≥ τ_0, Lemma 7.7 at z := g_{min(s_1,s_2)}x gives d(g_{s_1}x, g_{s_2}x) ≥ c_B(2+T)^{−K} > 3ρ by (3), a contradiction. So r < τ_0, and Lemma 7.4(a) gives c_0r ≤ 3ρ.
(ii) *Time grid.* Let k_max := ⌈T/h_0⌉ and h := T/k_max ≤ h_0. Since T ≥ 1 ≥ h_0, k_max ≤ T/h_0 + 1 ≤ 2T/h_0. For each k = 1, …, k_max, Lemma 7.8 (applicable by (1)) gives σ_k ∈ [0,T] with d(g_{kh}y, g_{σ_k}x) ≤ ρ. Put σ_0 := 0; then d(y, g_{σ_0}x) ≤ η_T ≤ ρ by (2).
(iii) *Induction.* For 0 ≤ k < k_max, Lemma 7.4(b) gives d(g_{(k+1)h}y, g_{σ_k+h}x) ≤ 2d(g_{kh}y, g_{σ_k}x) ≤ 2ρ, hence d(g_{σ_k+h}x, g_{σ_{k+1}}x) ≤ 3ρ. Both times lie in [0, T+1] (σ_k + h ≤ T + h_0 ≤ T + 1), so (i) gives |σ_{k+1} − σ_k − h| ≤ 3ρ/c_0. By induction from σ_0 = 0, |σ_k − kh| ≤ 3kρ/c_0 ≤ 6Tρ/(c_0h_0) for all k ≤ k_max.
(iv) *Conclusion.* For t ∈ [0,T] choose k ≤ k_max − 1 with t ∈ [kh, (k+1)h]. By Lemma 7.4(b),
d(g_tx, g_ty) ≤ 2d(g_{kh}x, g_{kh}y) ≤ 2(d(g_{kh}x, g_{σ_k}x) + d(g_{σ_k}x, g_{kh}y)) ≤ 2(V|kh − σ_k| + ρ) ≤ 2ρ + 12VTρ/(c_0h_0) < ε by (4). ∎

**Theorem V.** Let M be compact and connected and let X be GH and preserve a smooth positive density. Then h_top(g_1) = 0, so the flow has zero topological entropy. More precisely (for n ≥ 2), for each ε > 0 the maximal cardinality s(k, ε) of a (k, ε)-separated set for g_1 satisfies s(T+1, ε) ≤ C_M^2 T^{2nB} for all integers T ≥ T_0(ε) with η_T ≤ r_*.

*Proof.* If n = 1, g_1 is a circle homeomorphism and has zero entropy (Theorem A, first case). Let n ≥ 2 and normalise the density to ω(M) = 1. Fix ε > 0 and an integer T ≥ T_0(ε) with η_T ≤ r_*, and let E be a (T+1, ε)-separated set for g_1 (as in [Bo]). Take the partition of §7.1 at scale η = η_T and assign to x ∈ E the pair (cell of x, cell of g_Tx). This is injective on E: if x ≠ y in E had the same pair, then d(x,y) + d(g_Tx, g_Ty) ≤ η_T/2 + η_T/2 = η_T, so Lemma 7.9 gives d(g_ix, g_iy) < ε for all integers 0 ≤ i ≤ T, contradicting separation. Hence s(T+1, ε) ≤ (C_Mη_T^{−n})^2 = C_M^2T^{2nB}, and

  (1/(T+1)) log s(T+1, ε) ≤ (2 log C_M + 2nB log T)/(T+1) → 0.

So limsup_k (1/k) log s(k,ε) = 0 for every ε > 0, and h_top(g_1) = 0 by [Bo]. Since h_top(g_t) = |t|h_top(g_1), every g_t has zero entropy. ∎

*Dependency of the constants (no circularity).* (1) r_*, c_ω, C_ω, C_M from the metric and ω; (2) m and C_1 from GH (Lemma 7.5), then C_b (Lemma 7.3, for this m); (3) V, τ_0, c_0, h_0 from X (Lemma 7.4); (4) c, A_3, c_B and K = (2m+1)/(n−1) (Lemma 7.7); (5) C_C (Lemma 7.8); (6) B = (2m+1)(K+2) and T_0(ε) (Lemma 7.9). Lemma 7.7 holds for all r ≥ τ_0, and it is only compared with ρ_T through condition (3), a condition on T alone.

*Remark (hypotheses actually used).* The proof of Theorem V uses only: n ≥ 2; X has no zeros; a smooth positive probability density ω (for the ball volumes); and the *tame cohomology-free* property that every smooth f equals ∫f dω + Xu with u smooth and ‖du‖_∞ ≤ C_1‖f‖_{C^m}. GH and invariance of ω are used only to obtain these (Lemmas 7.2 and 7.5). The decisive input is that the invariant distribution densities form the line ℝω; a merely closed range of X is not enough (see §10).

### 7.4 The reduction of the problem to a smooth invariant volume

In this subsection ν is again an arbitrary smooth positive density, d = div_ν X, and J_t, Γ_t, P are as in §0.1. Since e^{J_t} is the ν-Jacobian of g_t,

  ∫ψ∘g_t · e^{J_t} dν = ∫ψ dν  for ψ ∈ L^1(ν), and hence ∫b·Γ_tφ dν = ∫(b∘g_{−t})φ dν for b ∈ L^1(ν), φ ∈ C^∞.   (7.1)

(The second identity is the first with ψ := (b∘g_{−t})φ.) Consider the statement

  **(V)** there is a smooth positive density ω with L_Xω = 0.

**Corollary 7.10 (the problem follows from (V)).** If every GH field satisfies (V), then every GH field has zero topological entropy.

*Proof.* Theorem V. ∎

**Lemma 7.11 (coboundary criterion).** Assume GH. (V) holds if and only if there is b ∈ L^1(ν) with b∘g_s − b = J_s ν-a.e. for every s ∈ ℝ. In that case b agrees a.e. with a smooth function, e^{−b}ν is invariant, and |J_t| ≤ 2 sup|b| for all t and x.

*Proof.* Suppose b exists. By (7.1), ∫b Γ_tφ dν = ∫(b∘g_{−t})φ dν = ∫bφ dν + ∫J_{−t}φ dν. Since Γ_tφ = φ + tPφ + O(t^2) and J_{−t} = −td + O(t^2) uniformly on M, differentiating at t = 0 gives ∫b Pφ dν = −∫dφ dν. By (0.1), ⟨Xb, φν⟩ = −∫bPφ dν = ∫dφ dν, i.e. Xb = d in D′. By GH b is smooth (after modification on a null set), and the identity holds everywhere by continuity. Then h := e^{−b} satisfies Xh + dh = −h(Xb − d) = 0, i.e. L_X(hν) = (Ph)ν = 0. Conversely, if ω = hν with h > 0 smooth is invariant, then Ph = 0, so a := −log h satisfies Xa = d and J_t(x) = ∫_0^t(Xa)(g_sx)ds = a(g_tx) − a(x); take b := a. The bound |J_t| ≤ 2 sup|b| follows from J_t = b∘g_t − b. ∎

**Theorem W ((V) is equivalent to a one-sided Jacobian bound).** Assume GH. The following are equivalent:
(i) (V);
(ii) K_+ := sup_{t≥0, x∈M} J_t(x) < ∞;
(iii) inf_{t≥0, x∈M} J_t(x) > −∞.

*Proof.* (i) ⇒ (ii), (iii): Lemma 7.11.

(ii) ⇒ (i). *Step 1 (a bounded invariant density).* Put E_R := (1/R)∫_0^R e^{J_t}dt for R > 0. Then 0 < E_R ≤ e^{K_+}, and ∫E_R dν = ν(M) by (7.1) with ψ = 1. By the cocycle identity, Γ_s e^{J_t} = e^{J_s}e^{J_t∘g_s} = e^{J_{t+s}}, so Γ_sE_R − E_R = (1/R)(∫_R^{R+s} − ∫_0^s)e^{J_t}dt, whose sup-norm is ≤ 2|s|e^{K_+ + |s|‖d‖_∞}/R → 0 as R → ∞. Let h be a weak-* limit point in L^∞(ν) of (E_R) as R → ∞. By (7.1), ∫(Γ_sb)ψ dν = ∫b·(ψ∘g_{−s})dν for b ∈ L^∞, ψ ∈ L^1, and ψ ↦ ψ∘g_{−s} is bounded on L^1(ν); so Γ_s is weak-* continuous on L^∞(ν), and Γ_sh = h a.e. for every s, i.e.

  h(g_sx)e^{J_s(x)} = h(x) for ν-a.e. x, for every s.   (7.2)

Also 0 ≤ h ≤ e^{K_+} and ∫h dν = ν(M) > 0. By (7.2), the set A := {h > 0} satisfies 1_A∘g_s = 1_A a.e. for every s, so by Corollary 1.5 A is conull (it is not null since ∫h dν > 0). By (7.2) and (7.1), hν is g_s-invariant: ∫ψ∘g_s·h dν = ∫(ψ h)∘g_s e^{J_s}dν = ∫ψh dν.

*Step 2 (a bounded transfer function).* b := −log h is finite a.e., b ≥ −K_+, and by (7.2) b∘g_s − b = J_s a.e. for every s. Let F(x) := sup_{t≥0}J_t(x) ∈ [0, K_+]. By the cocycle identity, F(g_sx) + J_s(x) = sup_{t≥0}J_{t+s}(x) = sup_{t≥s}J_t(x) for s ≥ 0. Put b̃ := b + F. For each s ≥ 0, a.e., b̃∘g_s = b + J_s + F∘g_s = b + sup_{t≥s}J_t ≤ b + F = b̃. Let β := arctan b̃, a bounded Borel function with β − β∘g_s ≥ 0 a.e. for s ≥ 0. Since hν is invariant and β is bounded, ∫(β − β∘g_s)h dν = 0, and since h > 0 a.e., β∘g_s = β a.e. for every s ≥ 0; composing with g_{−s} (which preserves ν-null sets) gives the same for s ≤ 0. By Corollary 1.5, β is a.e. constant, so b̃ = c a.e. and b = c − F ∈ [c − K_+, c] is bounded. Lemma 7.11 gives (V).

(iii) ⇒ (i). −X is GH, its ν-divergence is −d, and its log-Jacobian is J^{(−X)}_t(x) = J_{−t}(x) = −J_t(g_{−t}x). Hence sup_{t≥0,x}J^{(−X)}_t(x) = −inf_{t≥0,y}J_t(y) < ∞, and (ii) ⇒ (i) for −X gives a smooth density invariant under −X, hence under X. ∎

**Theorem W′ ((V) is equivalent to integrability of an explicit transfer function).** Assume GH and put L(x) := limsup_{t→+∞}J_t(x) and ℓ(x) := liminf_{t→+∞}J_t(x), with values in [−∞, ∞]. Then (V) ⇔ L ∈ L^1(ν) ⇔ ℓ ∈ L^1(ν).

*Proof.* If (V) holds, J_t = a∘g_t − a with a smooth (Lemma 7.11), so |L|, |ℓ| ≤ 2 sup|a|. Conversely, J_t(x) = J_s(x) + J_{t−s}(g_sx) for all s, t, x; taking limsup (resp. liminf) as t → ∞ gives L(x) = J_s(x) + L(g_sx) and ℓ(x) = J_s(x) + ℓ(g_sx) whenever the right side is finite (J_s(x) is a finite number, so both sides are then finite together). If L ∈ L^1(ν), then L is finite a.e., and b := −L satisfies b∘g_s − b = J_s a.e. for every s; Lemma 7.11 gives (V). The same for ℓ. ∎

So, by Corollary 7.10 and Theorem W, **the problem follows from the uniform one-sided bound sup_{t≥0,x}J_t(x) < ∞ on the ν-Jacobians of a GH flow**; this bound is not proved here.

---

## 8. Infinite su-chains with summable legs (GH only), and the reduction of (PE0) to a GH-free statement

**Definition (summable chain).** Let C ≥ 1 and θ > 0. A *summable chain* with constants (C, θ) is a sequence (x_i)_{i≥0} in M such that, for all i ≥ 0:
* (L1) d(g_tx_{2i}, g_tx_{2i+1}) ≤ Ce^{−θ|t|}d(x_{2i}, x_{2i+1}) for t ≤ 0 (a "u-leg");
* (L2) d(g_tx_{2i+1}, g_tx_{2i+2}) ≤ Ce^{−θt}d(x_{2i+1}, x_{2i+2}) for t ≥ 0 (an "s-leg");
* (L3) ℓ := Σ_i d(x_i, x_{i+1}) < ∞.

Then x_i → p, the *limit point*. Legs of length 0 are allowed.

**Jacobian constants.** For a u-leg (a,b) put β^u(a,b) := lim_{t→−∞}(J_t(a) − J_t(b)), and for an s-leg β^s(a,b) := lim_{t→+∞}(J_t(a) − J_t(b)). With K_d := Lip(d)C/θ,

  |J_t(a) − J_t(b) − β^u(a,b)| ≤ K_d d(a,b)e^{−θ|t|} for t ≤ 0, and |β^u| ≤ K_d d(a,b);

the same holds for β^s with t ≥ 0. Indeed, J_t(a) − J_t(b) = −∫_t^0(d(g_sa) − d(g_sb))ds, and the integrand is bounded by Lip(d)Cd(a,b)e^{−θ|s|}.

**Weights.** Put w_0 := 1, w_{2i+1} := −w_{2i}e^{β^u(x_{2i},x_{2i+1})} and w_{2i+2} := −w_{2i+1}e^{β^s(x_{2i+1},x_{2i+2})}. Then e^{−K_dℓ} ≤ |w_i| ≤ e^{K_dℓ}, and w_{2N} → w_∞ := exp(Σ_jβ_j) > 0.

Define the u-grouping S := Σ_i(w_{2i}δ_{x_{2i}} + w_{2i+1}δ_{x_{2i+1}}) and the s-grouping S′ := Σ_i(w_{2i+1}δ_{x_{2i+1}} + w_{2i+2}δ_{x_{2i+2}}).

**Lemma 8.1.**
(a) S and S′ converge absolutely in (C^1)′.
(b) S − S′ = δ_{x_0} − w_∞δ_p.
(c) Assume (L4): there are η ∈ [0,θ) and C′ with J_t(x_{2i}) ≤ C′ + η|t| for t ≤ 0 and J_t(x_{2i+1}) ≤ C′ + ηt for t ≥ 0 (all i). Then |S(Γ_tφ)| ≤ C″e^{−(θ−η)|t|}‖φ‖_{C^1} for t ≤ 0, and |S′(Γ_tφ)| ≤ C″e^{−(θ−η)t}‖φ‖_{C^1} for t ≥ 0.

*Proof.*
(a) For a u-leg (a,b) and ‖φ‖_{C^1} ≤ 1: |w_aφ(a) + w_bφ(b)| = |w_a||φ(a) − e^{β^u}φ(b)| ≤ e^{K_dℓ}(1 + K_de^{K_dℓ})d(a,b). This is summable by (L3). The same holds for s-legs.
(b) The N-th partial sums differ by δ_{x_0} − w_{2N}δ_{x_{2N}}, and ‖w_{2N}δ_{x_{2N}} − w_∞δ_p‖_{(C^1)′} ≤ |w_{2N} − w_∞| + w_∞d(x_{2N},p) → 0.
(c) For a u-leg, t ≤ 0 and r_t := J_t(a) − J_t(b) − β^u(a,b),

  w_ae^{J_t(a)}φ(g_ta) + w_be^{J_t(b)}φ(g_tb) = w_ae^{J_t(a)}[(φ(g_ta) − φ(g_tb)) + (1 − e^{−r_t})φ(g_tb)].

  Its modulus is ≤ C_ℓe^{J_t(a)}d(a,b)e^{−θ|t|}‖φ‖_{C^1}. Since Γ_tφ is smooth, S(Γ_tφ) is the sum of these leg terms. Summing with (L4) gives the first bound; the s-legs give the second. ∎

**Theorem E (one chain).** Assume GH. Let (x_i) be a summable chain satisfying (L4) and also J_t(x_0) ≤ C′ + ηt for t ≥ 0. Suppose further:
* (L5) d(g_tx_0, g_tp) ≤ Ce^{−θt} for t ≥ 0;
* (HC) w_∞ = e^{β^s(x_0,p)}.

Then S = 0. Consequently no vertex x_j is distinct both from p and from every x_i with i ≠ j.

In the volume case (d = 0) the conditions (L4) and (HC) hold automatically, and w_i = (−1)^i.

*Proof.*
1. Backward decay is Lemma 8.1(c).
2. For t ≥ 0, S(Γ_tφ) = S′(Γ_tφ) + e^{J_t(x_0)}φ(g_tx_0) − w_∞e^{J_t(p)}φ(g_tp). By (HC), the last two terms equal e^{J_t(x_0)}[(φ(g_tx_0) − φ(g_tp)) + (1 − e^{−r″_t})φ(g_tp)], where r″_t := J_t(x_0) − J_t(p) − β^s(x_0,p) = O(e^{−θt}) by (L5). By (L4) at x_0 this is O(e^{−(θ−η)t})‖φ‖_{C^1}.
3. Theorem J (k = 1) gives S = 0.
4. Suppose x_j were such an isolated vertex. A bump φ at x_j vanishing near the closed set {x_i : i ≠ j} ∪ {p} gives S(φ) = w_j ≠ 0. ∎

**Theorem E′ (two chains; weak-stable endings; no holonomy condition).** Assume GH. Let x_0 ∈ M, and let (a_i), (b_i) be two summable chains with a_0 = b_0 = x_0, common constants (C,θ), limits p_1, p_2, and (L4) with a common η < θ. Assume also J_t(x_0) ≤ C′ + ηt for t ≥ 0. Suppose there are real τ_1, τ_2 with

  d(g_tp_k, g_{t+τ_k}x_0) ≤ Ce^{−θt} for t ≥ 0 (k = 1,2).

Suppose finally that each chain has an *orbit-isolated vertex* v_k ≠ x_0, meaning:
* v_k occurs exactly once in the combined list of vertices of both chains;
* v_k is neither a zero of X nor periodic;
* the orbit of v_k contains no other vertex of either chain, and neither p_1 nor p_2.

Then we have a contradiction.

*Proof.* Let C[ℝ] be the commutative group algebra of finite sums ψ = Σc_j[s_j], and put (ψ⋆S)(φ) := Σc_jS(Γ_{s_j}φ). Then (ψ⋆S)(Γ_tφ) = Σc_jS(Γ_{t+s_j}φ). Let S_k, S′_k be the groupings of chain k.
1. *Endpoint terms.* Put F(t) := e^{J_t(x_0)}φ(g_tx_0) and q_k := g_{τ_k}x_0. Then β_k := lim_{t→∞}(J_t(q_k) − J_t(p_k)) exists, and e^{J_t(q_k)}φ(g_tq_k) = e^{−J_{τ_k}(x_0)}F(t + τ_k). With c_k := w^{(k)}_∞e^{−β_k}e^{−J_{τ_k}(x_0)} > 0, for t ≥ |τ_k|:

   (δ_{x_0} − w^{(k)}_∞δ_{p_k})(Γ_tφ) = ((1 − c_k[τ_k])⋆F)(t) + E_k(t),  |E_k(t)| ≤ C_ke^{−(θ−η)t}‖φ‖_{C^1}.

   Here E_k(t) = c_kF(t+τ_k) − w^{(k)}_∞e^{J_t(p_k)}φ(g_tp_k) = w^{(k)}_∞e^{J_t(q_k)}[e^{−β_k}φ(g_tq_k) − e^{J_t(p_k)−J_t(q_k)}φ(g_tp_k)]. The bound follows from J_t(p_k) − J_t(q_k) = −β_k + O(e^{−θt}), d(g_tp_k, g_tq_k) = O(e^{−θt}), and J_t(q_k) = J_{t+τ_k}(x_0) − J_{τ_k}(x_0) ≤ const + ηt.
2. *Case 1 − c_2[τ_2] = 0, i.e. τ_2 = 0 and c_2 = 1.* Then chain 2 satisfies (L5) and (HC), and Theorem E applied to its isolated vertex v_2 gives a contradiction. The case 1 − c_1[τ_1] = 0 is symmetric.
3. *Otherwise* put ψ_1 := 1 − c_2[τ_2] ≠ 0, ψ_2 := −(1 − c_1[τ_1]) ≠ 0 and S := ψ_1⋆S_1 + ψ_2⋆S_2 ∈ (C^1)′. Let T_0 := |τ_1| + |τ_2|.
   * For t ≤ −T_0 all shifted times are ≤ 0, so Lemma 8.1(c) gives decay.
   * For t ≥ T_0, write S_k = S′_k + δ_{x_0} − w^{(k)}_∞δ_{p_k} and use step 1. The S′_k and E_k terms decay. The F-terms combine into ((1 − c_2[τ_2])(1 − c_1[τ_1]) − (1 − c_1[τ_1])(1 − c_2[τ_2]))⋆F = 0, by commutativity.
   * For |t| ≤ T_0, S(Γ_tφ) is bounded by C‖φ‖_{C^1}.
   So Theorem J gives S = 0.
4. *S ≠ 0.* S is a (grouped) series of Dirac masses at points g_sy, with either y a vertex of chain 1 and s ∈ {0, τ_2}, or y a vertex of chain 2 and s ∈ {0, τ_1}. These points accumulate only at the finitely many points g_sp_k. Suppose g_sy = v_1. Then y is on the orbit of v_1, so y = v_1 (orbit isolation), y lies in chain 1, and s = 0 (v_1 is neither periodic nor a zero). No g_sp_k equals v_1. A bump at v_1 therefore gives S(φ) = w^{(1)}_{v_1}·(coefficient of [0] in ψ_1). This coefficient is 1 if τ_2 ≠ 0, and 1 − c_2 ≠ 0 if τ_2 = 0. So S ≠ 0, contradicting step 3. ∎

**Corollary 8.3 (reduction of the problem to a GH-free geometric statement).** Consider the following statement, which makes no reference to hypoellipticity.

**(SC)** For every smooth vector field X on a compact connected manifold of dimension ≥ 2, and every g_1-invariant, g_1-ergodic probability μ with h_μ(g_1) > 0 and ∫J_1dμ = 0, there are a point x_0 and two summable chains from x_0 satisfying all the hypotheses of Theorem E′: (L4) with η < θ, J_t(x_0) ≤ C′ + ηt for t ≥ 0, weak-stable endings, and orbit-isolated vertices.

Then (SC) implies (PE0), and hence (via Corollary C″, i.e. modulo [NF]) the problem in every dimension. (In the volume-preserving case the problem is already settled, unconditionally, by Theorem V of §7.3; (SC) is only needed for fields without a smooth invariant density.)

*Proof.* Under GH, the data provided by (SC) contradict Theorem E′. ∎

*Remark (honest assessment).* (SC) is not proved. It is not known to be easier than (PE0). It moves the whole difficulty into the geometry of non-uniformly partially hyperbolic measures with a centre exponent 0 transverse to the flow: su-paths must be steered back into the weak-stable set of the base point, in the limit and with summable cost, along the centre directions. Some special cases do hold, though none of them is new:
* Hyperbolic measures (Katok horseshoes give homoclinic points of periodic orbits, i.e. finite chains). These are already excluded by Theorem B.
* Uniformly partially hyperbolic and fibred models (accessible, or integrable with local product structure inside su-leaves). These are model computations only, not theorems about general flows.

---

## 9. Status

**Main claim: NOT fully proved.** The main claim of this document is the problem's statement itself: for every GH vector field X on a compact connected manifold, h_top(g_1) = 0. It is proved here only in the following cases.

* **Proved completely (modulo only the standard analysis facts [An] and Bowen's definition [Bo]):** Theorem V. If X is GH and preserves a smooth positive density, then h_top(g_1) = 0, in every dimension, with at most polynomial growth of separated orbit segments.
* **Proved modulo the cited classical theorems [VP], [Os], [Ru], [SM], [KLY]:** Theorem A. If X is GH and dim M ≤ 3, then h_top(g_1) = 0 (no volume assumption).
* **Proved reductions of the general case.** (a) Corollary 7.10 and Theorems W, W′: the problem follows from (V) ("every GH field preserves a smooth positive density"), and under GH, (V) is equivalent to sup_{t≥0,x}J_t(x) < ∞, to inf_{t≥0,x}J_t(x) > −∞, and to limsup_{t→∞}J_t ∈ L^1(ν). (b) Corollary C″: modulo [NF], the problem is equivalent to (PE0), "no ergodic invariant probability of positive entropy has zero mean divergence". (c) Corollary 8.3: (SC) implies (PE0). Also proved: Theorem B (positive-entropy measures are non-hyperbolic), Theorem C, Theorem C′ and Corollaries C″, C‴ (the last three modulo [NF], C‴ only needing its classical one-dimensional case), Proposition 6.5, Theorems J, E, E′.

**The gap.** Neither (V), nor (PE0), nor (SC) is proved. Hence the problem remains open here for GH fields on manifolds of dimension ≥ 4 that are not assumed to preserve a smooth positive density. Any one of the following would close it: (V) (equivalently, a uniform upper bound on the forward ν-Jacobians of the flow, Theorem W); (PE0) (modulo [NF]); (SC). A GH field on a manifold of dimension ≥ 4 with positive entropy would have to have no smooth invariant density, and every positive-entropy ergodic measure of it would be non-hyperbolic (Theorem B), have zero mean divergence (Theorem C′, modulo [NF]) and full support (Proposition 6.5).

**Citations not re-verified here:** [NF] (used only in Theorem C′ and its corollaries) and the classical theorems of §0.2, all recalled from memory.

## 10. Other routes (recorded for orientation; not used above, and not proved in this document unless stated)

* **Literature pointer for (V) (unverified).** I recall, without being able to check it, that the implication "GH ⇒ existence of a smooth invariant volume" (indeed GH ⇒ cohomology-free) is discussed in work of G. Forni on the Greenfield–Wallach and Katok conjectures (around 2008), and used by A. Kocsard in dimension 3. If (V) is established there, Corollary 7.10 (Theorem V) proves the problem in full. I could not confirm the statement or its proof, so it is not used.
* **Named conjectures.** The Greenfield–Wallach conjecture (every GH field is smoothly conjugate to a Diophantine linear flow on a torus) implies the problem at once. Katok's conjecture (cohomology-free fields are conjugate to Diophantine linear flows) implies the volume case, which is now proved directly by Theorem V. As far as I recall both conjectures are known in dimension ≤ 3 only.
* **Why the occupation-measure argument of Theorem V does not extend directly.** Without an invariant volume, the analogue of Corollary 7.6 says only that the difference of the occupation measures of two orbit segments with close endpoints is small modulo the space I of invariant distribution densities (S(Pφ) = 0 for all φ). A transitive Anosov flow has a closed-range, tame cohomological equation (by Livšic's theorem with the de la Llave–Marco–Moriyón regularity theorem, recalled from memory), so it satisfies every estimate of that type, yet it has positive entropy; I contains all its periodic-orbit measures. So any extension must use the distributional part of GH through a smallness property of I; dim I = 1 is exactly (V). A conditional version was found: under GH, no zeros, dim I < ∞, and a "no long repeats" property μ(Bad_L) → 0 of a positive-entropy ergodic μ, a windowed version of the argument of Theorem V combined with Katok's entropy formula gives h_μ = 0. Neither dim I < ∞ nor the no-long-repeats property was proved.
* **Further consequences of GH found along the way (proofs not reproduced).** Under GH and n ≥ 2 every point is nonwandering (a wandering flow box would carry a nonconstant bounded invariant function, contradicting Corollary 1.5), so no smooth u has Xu = f with f ≥ 0, f ≢ 0, and the flow is chain transitive. Also (V) is equivalent to the existence of a finite absolutely continuous invariant measure whose density has integrable logarithm.
* **Finite su-configurations, holomorphic eigen-families, conformal measures, local injectivity of X + κ.** These were explored for the general case. Each gives either a second proof of the exclusion of hyperbolic positive-entropy measures (Theorem B) or a reformulation of (PE0), but none proves (PE0). The common missing input is geometric: closing of su-paths along a centre direction transverse to the flow for a non-hyperbolic positive-entropy measure, which is (SC).
