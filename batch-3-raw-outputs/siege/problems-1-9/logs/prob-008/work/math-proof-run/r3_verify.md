# Verification query: check the draft proof below step by step

Below is the complete current draft of a proof document for the problem. Its status section says the problem's full claim is **not** proved: it proves the case dim M ≤ 3 and a number of partial results and reductions. Your job is to referee it.

Instructions:
1. Go through the document step by step. For every inequality, every interchange of limits, sums or integrals, every cited result and every "it follows that", decide whether it actually follows as written. Check the hypotheses of each cited classical theorem against how it is used.
2. In particular check: Lemma 1.1 (the truncation argument), Lemma 1.3, Lemma 1.4 (closed graph plus Rellich), Theorem J (moments and the Fourier step), Lemma K (the jet-space Cayley–Hamilton argument and the choice of K), Corollaries 3.2–3.3, Lemmas 4.1–4.2, Theorems A and B (use of Ruelle's inequality and Katok's horseshoe theorem for flows), Theorem C, Theorem C′ (in particular Lemma 6.4 and Step 4), Proposition 6.5, Proposition 7.1, Proposition 7.3, Theorem 7.5 (especially steps 1, 4 and 5), Theorem D, Lemma 8.1, and Theorems E and E′.
3. List every error or gap you find, ordered by severity: fatal (a claimed result is false or unproved), serious (repairable, but the repair needs a real argument), minor (wording, constants, notation). For each, quote the location and give a repair if you can.
4. Say explicitly whether the main claim of the problem (zero topological entropy for every GH field) is proved by this document. Separately, say which of its stated results (Theorem A for dim ≤ 3, Theorem B, Theorems C/C′, Theorem D, Proposition 6.5, Theorems E/E′) are proved as stated, modulo the citations the document lists.
5. Check that the document's account of what is cited and what remains open (§0.3, §10) is accurate.

---- BEGIN DRAFT ----

# Globally hypoelliptic flows and topological entropy: the case dim M ≤ 3, partial results and reductions in general

## Status (read this first)

**The claim is not proved in full here.** This document proves:

* **Theorem A (main result).** If X is globally hypoelliptic (GH) and dim M ≤ 3, then the flow has zero topological entropy (§5). The proof uses three classical theorems cited from the literature: the variational principle, Ruelle's inequality, and Katok's horseshoe theorem for flows.
* **Theorem B (any dimension).** Under GH, every ergodic invariant measure of positive entropy is *non-hyperbolic*: besides the flow direction, it has a zero Lyapunov exponent (§5).
* **Theorems C and C′ (any dimension).** These constrain the mean divergence μ(div X) of a positive-entropy ergodic measure μ (§6). Theorem C (unconditional modulo Pesin theory) excludes a band around 0, minus the point 0 itself. Theorem C′ shows μ(div X) = 0. It is proved modulo one citation, the non-stationary normal forms on Pesin unstable manifolds; that citation is not needed when the unstable dimension is 1. Consequences:
  * **Corollary C″.** The problem is *equivalent* to the statement (PE0) of §6.4 (modulo that citation).
  * **Corollary C‴.** In dimension 4 every positive-entropy ergodic measure has exponents (χ, 0, 0, −χ) and zero mean divergence.
* **Theorem D (volume-preserving case).** If X is GH and preserves a smooth positive density, the claim holds whenever b₁(M) ≥ dim M − 2 (§7). Here GH plus a smooth invariant volume is the same as *cohomology-free* (Proposition 7.1).
* **Proposition 6.5 (any dimension, GH and Atkinson's recurrence theorem only).** Every ergodic measure with zero mean divergence (in particular, modulo [NF], every positive-entropy ergodic measure) has full support, and a.e. forward orbit is dense.
* **Theorems E and E′ (§8).** Under GH, certain infinite "su-chains" with summable leg lengths cannot exist. This reduces (PE0), and hence the problem, to a purely geometric statement (SC) that makes no reference to GH (Corollary 8.3).

**What remains open** (§10): the problem in dimension ≥ 4, outside the volume-preserving case with b₁(M) ≥ dim M − 2. Equivalently (modulo the normal-form citation), (PE0): under GH, no ergodic measure of positive entropy has zero mean divergence. The problem would follow from the Greenfield–Wallach conjecture, and in the volume case from Katok's conjecture on cohomology-free vector fields. Both are recalled in §10 and are open in dimension ≥ 4 as far as I know. Gaps and citations are listed explicitly in §0.3 and §10.

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
* **[KLY]** Katok's horseshoe theorem for flows (Katok, Publ. IHÉS 1980; Lian–Young for C^2 flows in any dimension). Suppose μ is an ergodic invariant probability of a C^2 flow with h_μ(g_1) > 0 and μ(Zero(X)) = 0, and suppose every Lyapunov exponent other than the one in the flow direction is nonzero. Then the flow has a hyperbolic horseshoe. In particular it has a hyperbolic periodic orbit γ with a (transverse) homoclinic point, i.e. a point of W^u(γ) ∩ W^s(γ) not on γ.
* **[P]** Pesin theory for f = g_1 and an f-invariant, f-ergodic μ, as follows. For μ-a.e. x the unstable set W^u(x) = {y : limsup_m (1/m) log d(f^{−m}y, f^{−m}x) < 0} is an injectively immersed C^∞ submanifold tangent to E^u_x (the sum of the Oseledets spaces of positive exponents), with f^{−1}W^u(x) = W^u(f^{−1}x). For every compact Q ⊂ W^u(x) (intrinsic topology) and δ > 0 there is C = C(x,Q,δ) with d^u(f^{−m}y, f^{−m}x) ≤ C e^{−(χ^+_min − δ)m} for y ∈ Q and m ≥ 0, where χ^+_min is the smallest positive exponent. There are Pesin sets (compact sets Λ_l, μ(Λ_l) → 1) on which the local stable/unstable discs have uniform size and contraction constants and depend continuously (C^1) on the base point. Symmetric statements hold for W^s.
* **[LS]** Ledrappier–Strelcyn / Ledrappier–Young. There is a measurable partition ξ subordinate to W^u: ξ(x) ⊂ W^u(x), and ξ(x) contains a leaf-neighbourhood of x. It is increasing (fξ ≤ ξ, i.e. ξ refines fξ) and h_μ(f) = H_μ(ξ | fξ).
* **[NF]** (used only in Theorem C′, §6.3) Non-stationary sub-resonance normal forms on Pesin unstable manifolds (Kalinin–Sadovskaya, J. Mod. Dyn. 2017; Melnick 2019), with measurable dependence on the base point. The precise form used is stated in §6.3. **This is the one citation whose exact hypotheses I could not check.** When dim E^u = 1 it reduces to the classical existence of affine parameters on one-dimensional unstable leaves.
* **[Eh]** Ehresmann's fibration theorem.
* **[At]** Atkinson's recurrence theorem (1976). If T is an invertible ergodic measure-preserving transformation of a probability space and f ∈ L^1 has ∫f = 0, then for a.e. x and every ε > 0 there are infinitely many n ≥ 1 with |Σ_{j=0}^{n−1} f(T^jx)| < ε. (Used only in Proposition 6.5.)
* **[Ab]** Abramov's formula in the simple form h_μ(g_c) = |c|·h_μ(g_1) for a flow-invariant μ. (Used only in §7.)

### 0.3 Dependence summary
* Theorems J, K and Corollaries 3.2–3.3 use only GH and [SM]. Theorem A uses in addition [VP], [Os], [Ru] and [KLY]. Theorem B uses [Os], [Ru] and [KLY].
* Theorem C uses [P] and [LS]. Theorem C′ uses [P], [LS] and [NF]. Theorem D uses [VP], [Ab], [Os], [P], [LS], [Ru] and [Eh]; within [P] it uses the continuous (C^1) dependence of local stable/unstable discs on the base point in a Pesin set (step 5 of Theorem 7.5). Proposition 6.5 (full support) uses GH and [At]. Lemmas 4.1–4.2 use [VP] (Jacobs) and the ergodic decomposition only. Theorems E and E′ use GH only.

---

## 1. Elementary consequences of GH

**Lemma 1.1 (kernel).** Assume GH. If u is a distribution with Xu = 0, then u is constant.

*Proof.* By GH u is smooth. Suppose u is not constant, and choose c with min u < c < max u. Let H_ε be smooth and nondecreasing with H_ε = 0 on (−∞, −ε] and H_ε = 1 on [0, ∞). Then v_ε := H_ε(u − c) is smooth and Xv_ε = H_ε′(u − c)·Xu = 0. As ε → 0, v_ε → 1_{\{u≥c\}} =: v boundedly and pointwise (on {u ≥ c} every v_ε equals 1; at a point with u − c < 0, v_ε = 0 as soon as ε ≤ c − u), hence in L^1 and in D′. So Xv = 0, and by GH v agrees a.e. with a continuous function w. Then w ∈ {0,1} a.e., hence everywhere, so w is constant because M is connected. But w = 1 a.e. on the nonempty open set {u > c} and w = 0 a.e. on the nonempty open set {u < c}. Contradiction. (Complex-valued u: apply this to the real and imaginary parts.) ∎

**Lemma 1.2.** Assume GH.
(F1) If S is a distribution density with S(Pφ) = 0 for all φ, then S = cν for a constant c.
(F2) If S(Pφ) = c′∫φ dν for all φ, where c′ is a constant, then c′ = 0.

*Proof.* (F1): u = S/ν has Xu = 0 by (0.1), so u is constant by Lemma 1.1. (F2): u = S/ν has Xu = −c′ by (0.1), so u is smooth by GH. At a maximum point q of u the function s ↦ u(g_s q) has a maximum at s = 0. Hence (Xu)(q) = 0 and c′ = 0. ∎

**Lemma 1.3 (closed orbits).** Assume GH and n ≥ 2. Let q ∈ M and P > 0 with g_P q = q. Then J_P(q) ≠ 0. In particular d(p) ≠ 0 at every zero p of X (take any P: J_P(p) = P d(p)). Also, the Poincaré map of a periodic orbit never has Jacobian determinant of modulus 1, because e^{J_P(q)} = |det Dg_P(q)| equals that modulus.

*Proof.* Put S(φ) := ∫_0^P e^{J_s(q)} φ(g_s q) ds. Then S(Pφ) = ∫_0^P (d/ds)[e^{J_s(q)}φ(g_s q)] ds = (e^{J_P(q)} − 1)φ(q). If J_P(q) = 0, (F1) gives S = cν. But S is a nonzero positive measure (S(1) > 0) carried by the orbit of q. That orbit is a point or a closed C^1 curve, so it is ν-null when n ≥ 2. Contradiction. ∎

**Lemma 1.4 (tame estimate and closed range; used only in §7).** Assume GH. Then X(C^∞(M)) is closed in C^∞(M).

*Proof.* Fix a smooth density ω₀ and Sobolev spaces H^s(M), and fix s ≥ 0. Let F_s := {u ∈ H^{−s} : Xu ∈ C^∞}, with the seminorms ‖u‖_{H^{−s}} and ‖Xu‖_{H^j}, j ∈ ℕ. This is a Fréchet space. By GH, F_s ⊂ C^∞, and the inclusion has closed graph since both spaces embed continuously in H^{−s}. By the closed graph theorem it is continuous: for every r there are j and C with ‖u‖_{H^r} ≤ C(‖u‖_{H^{−s}} + ‖Xu‖_{H^j}).

Now let c(u) := ∫u ω₀/∫ω₀. We claim ‖u − c(u)‖_{H^r} ≤ C′‖Xu‖_{H^j} for smooth u, with j chosen so that the previous estimate holds at levels r and r+1. If not, there are smooth u_m with c(u_m) = 0, ‖u_m‖_{H^r} = 1 and ‖Xu_m‖_{H^j} → 0. The previous estimate at level r+1 bounds u_m in H^{r+1}. By Rellich a subsequence converges in H^r to some u with ‖u‖_{H^r} = 1, c(u) = 0 and Xu = 0. By Lemma 1.1 u is constant, hence u = 0. Contradiction.

So if Xu_m → f in C^∞, then (u_m − c(u_m)) is Cauchy in every H^r and converges in C^∞ to some u with Xu = f. ∎

**Corollary 1.5 (ν-ergodicity; not used later).** Assume GH. If A ⊂ M is measurable and ν(A △ g_t^{−1}A) = 0 for every t, then ν(A) = 0 or ν(M∖A) = 0.

*Proof.* Put v := 1_A. Since e^{J_t} is the ν-Jacobian of g_t, ∫ψ∘g_t·e^{J_t}dν = ∫ψdν for bounded measurable ψ. With ψ := (v∘g_{−t})φ this gives ∫v·Γ_tφ dν = ∫(v∘g_{−t})φ dν = ∫vφ dν for smooth φ. Differentiating at t = 0 (step 1 of the proof of Theorem J) gives ∫v·Pφ dν = 0. So S := vν satisfies S(Pφ) = 0, and S = cν by (F1). Hence v = c ν-a.e., and c ∈ {0,1}. ∎

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

All further uses of GH in §§3–8 go through Theorem J, except in §7, which also uses Lemma 1.4.

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

*Check.* The cocycle identity used here and the formula e^{J_t(x)} = |Dg_t(x)| (relative to ν) were confirmed numerically on the circle flow x′ = 1 + ½ sin x (agreement to 1e−9).

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

## 7. The volume-preserving case

In this section ω is a smooth positive density with L_Xω = 0, normalised so that ω(M) = 1. We take ν = ω, so d = 0 and J ≡ 0. Call X **cohomology-free (CF)** if every smooth f can be written f = c + Xu with c a constant and u smooth.

**Proposition 7.1.** Suppose X preserves a smooth positive density ω.
(a) X is GH if and only if X is CF.
(b) If X is GH, the flow is uniquely ergodic with invariant measure ω, and it is minimal.

*Proof.*
* **GH ⇒ CF.** By Lemma 1.4, X(C^∞) is closed. By Hahn–Banach it is the annihilator of the distribution densities T with T(Xφ) = 0 for all φ. For such T, u := T/ω satisfies Xu = 0 by (0.1) (P = X here), so u is constant (Lemma 1.1) and T = cω. Hence X(C^∞) = {f : ∫f dω = 0}, which gives CF.
* **CF ⇒ GH.** No smooth u has Xu = 1 (look at a maximum of u). So c(f) is well defined, and it is a linear functional whose kernel is X(C^∞). If T is an invariant distribution density, T annihilates X(C^∞) = ker ω; so T = T(1)ω. Now let u ∈ D′ with Xu = f smooth. Then ∫f dω = −⟨u, L_Xω⟩ = 0, so f = Xv with v smooth. Then X(u − v) = 0, so (u − v)ω is an invariant density, equal to cω. Hence u = v + c is smooth.
* **(b).** For any invariant probability m, m(Xu) = 0, so m(f) = ∫f dω for all f. This is unique ergodicity. Every orbit closure carries an invariant measure, which must be ω, whose support is M. Hence the flow is minimal. ∎

**Lemma 7.2 (invariant representatives of cohomology classes).** Assume GH and L_Xω = 0. Every class c ∈ H^1(M;ℝ) contains a unique smooth closed 1-form η_c with L_Xη_c = 0 and i_Xη_c ≡ ρ(c) constant, and c ↦ ρ(c) is linear.
*Proof.*
* Existence: for closed η ∈ c, CF gives i_Xη = ρ + Xu. Put η_c := η − du. Then i_Xη_c = ρ and L_Xη_c = d(i_Xη_c) + i_Xdη_c = 0.
* Uniqueness: two such forms differ by dv with Xv constant. That constant is 0 (maximum of v), so v is constant by Lemma 1.1.
* Linearity follows from uniqueness. ∎

**Proposition 7.3 (torus fibration).** Assume GH, L_Xω = 0 and b := b_1(M) ≥ 1. Let c_1, …, c_b ∈ H^1(M;ℤ) map to a basis of H^1(M;ℝ), put η_i := η_{c_i}, fix p ∈ M, and let π(x) := (∫_p^xη_i)_i mod ℤ^b.
(a) π : M → T^b is smooth, and π(g_tx) = π(x) + tα with α = (ρ(c_i))_i.
(b) π is a surjective submersion, hence a smooth fibre bundle with compact fibres F_θ of dimension f := n − b.
(c) k·α ≠ 0 for all k ∈ ℤ^b∖{0}.
(d) If d(g_{t_j}x, g_{t_j}y) → 0 along some sequence |t_j| → ∞, then π(x) = π(y).

*Proof.*
(a) The periods of the η_i are integers, so π is well defined. dπ = (η_i)_i and Xπ = α.
(b) g_t^*η_i = η_i, so the rank r(x) of (η_i(x))_i is flow-invariant. The set where r is maximal is open, nonempty and invariant; its complement is closed and invariant. By minimality the complement is empty, so the rank is constant, equal to r_0. Then K(x) := {c : Σc_iη_i(x) = 0} is a continuous, flow-invariant map to a Grassmannian. It is constant on the dense orbits, hence constant, equal to K. For c ∈ K, Σc_iη_i ≡ 0, so Σc_i[η_i] = 0 in cohomology and c = 0. Thus π is a submersion. Its image is open and compact, hence all of T^b, and [Eh] gives the bundle structure.
(c) If k·α = 0, then e := exp(2πik·π) satisfies Xe = 0. So e is constant (Lemma 1.1), d(k·π) = Σk_iη_i = 0, and k = 0.
(d) The map g_t acts on T^b as a translation, so dist(πx, πy) = dist(πg_tx, πg_ty) ≤ Lip(π)d(g_tx, g_ty) → 0 along t = t_j. ∎

**Lemma 7.4 (Lyapunov structure).** Let V := ker Dπ.
(i) V is Dg_t-invariant, and Dg_t induces the identity on TM/V ≅ T^b × ℝ^b.
(ii) The exponents of Dg_t|_V sum to 0 at ω-a.e. point.
(iii) E^s(x) + E^u(x) ⊂ V(x) at Oseledets-regular points.

*Proof.*
(i) This is Dπ∘Dg_t = Dπ.
(ii) Write ω = ω_V ⊗ π^*(dθ), with ω_V a continuous positive density on V. Since Dg_t preserves ω and acts trivially on the quotient, its Jacobian on V with respect to ω_V is 1.
(iii) For v ∈ E^s, Dπ(v) = Dπ(Dg_tv) → 0 as t → +∞. Use t → −∞ for E^u. ∎

**Theorem 7.5.** Assume GH, L_Xω = 0, b_1(M) ≥ 1 and h_top(g_1) > 0. Then the vertical cocycle Dg_t|_V has a zero exponent.

*Proof.*
1. By Lemma 4.1 there is a g_1-ergodic μ with h_μ(g_1) > 0, and μ̄ is flow-invariant with h_{μ̄}(g_1) = h_μ(g_1). By unique ergodicity of the flow (Proposition 7.1(b)), μ̄ = ω, so h_ω(g_1) > 0. The field cX (c > 0) satisfies the same hypotheses with the same ω and π (GH is clearly invariant under X ↦ cX), its time-one map is g_c, and h_ω(g_c) = c·h_ω(g_1) > 0 by [Ab]. The flow (g_t) is ω-ergodic and its L²(ω) eigenvalues form a countable set Σ ⊂ ℝ (L²(ω) is separable and eigenfunctions with distinct eigenvalues are orthogonal). The map g_c is ω-ergodic unless some eigenvalue σ ≠ 0 has e^{icσ} = 1, i.e. unless c ∈ ∪_{σ∈Σ∖0} (2π/σ)ℤ, a countable set. Replacing X by cX for c outside this set (all Lyapunov exponents get multiplied by c, so zero exponents stay zero), we may assume T := g_1 is ω-ergodic with h_ω(T) > 0.
2. Suppose all vertical exponents are nonzero. Then V = V^− ⊕ V^+, with V^− ⊂ E^s and V^+ ⊂ E^u. With Lemma 7.4(iii) this gives E^s ⊕ E^u = V.
3. By Proposition 7.3(d), local stable and unstable manifolds lie in fibres of π.
4. Fix a Pesin set Λ_l with ω(Λ_l) > 0. Let ξ be the [LS] partition for T and ξ′ the one for T^{−1} (subordinate to W^s). *Density fact:* for a measurable A and a measurable partition η with conditionals ω^η, a.e. x ∈ A lies in the support of ω^η_x|_A. (Fix a countable basis of open sets; the set of x ∈ A having a basic neighbourhood U with ω^η_x(A ∩ U) = 0 has conditional measure 0 on every atom, hence measure 0.) Apply this with A = Λ_l to ξ and ξ′, and combine with Lemma 6.0 for T and for T^{−1} (non-atomic conditionals). Then for a.e. x ∈ Λ_l and every δ > 0, the set Λ_l ∩ ξ(x) ∩ B(x,δ) has positive, non-atomic conditional measure, so it contains a point y ≠ x; likewise there is z ≠ x in Λ_l ∩ ξ′(x) ∩ B(x,δ). Since ξ(x) contains a leaf-neighbourhood of x and the local discs of points of Λ_l have uniform size, for δ small y ∈ W^u_loc(x) and z ∈ W^s_loc(x).
5. (Local product structure inside the fibre.) By step 3, the discs W^s_loc(x), W^u_loc(x), W^s_loc(y) and W^u_loc(z) all lie in the fibre F through x (y and z lie in F, and every point of W^s_loc(y), W^u_loc(z) is asymptotic to y, resp. z). F is a compact embedded f-dimensional submanifold (we take F to be the connected component of π^{−1}(π(x)) containing x; local discs are connected, so they lie in that component). By step 2, T_xW^u_loc(x) = E^u_x and T_xW^s_loc(x) = E^s_x are complementary in V_x = T_xF. Choose a chart ψ of F near x with ψ(x) = 0 and Dψ_x(E^u_x) = ℝ^a × 0, Dψ_x(E^s_x) = 0 × ℝ^{f−a}. By [P] (C^1-continuous dependence of local discs on the base point in Λ_l), there are r > 0 and δ_0 > 0 such that for y, z ∈ Λ_l with d(x,y), d(x,z) < δ_0, ψ(W^u_loc(z)) contains the graph of a C^1 map h_u : B^a_r → ℝ^{f−a} and ψ(W^s_loc(y)) contains the graph of a C^1 map h_s : B^{f−a}_r → ℝ^a, with Lip(h_u), Lip(h_s) ≤ 1/3 and |h_u(0)|, |h_s(0)| ≤ r/3, where the last bound is obtained by taking δ smaller if needed. The map (α, β) ↦ (h_s(β), h_u(α)) sends B̄^a_{r′} × B̄^{f−a}_{r′} into itself for r′ = r/2 (since r/3 + r′/3 ≤ r′), and it is a contraction (constant 1/3) in the max-norm. Its fixed point (α, β) gives a point w := ψ^{−1}(α, β) ∈ W^u_loc(z) ∩ W^s_loc(y).
6. Then:
   * x and y are backward asymptotic, as are z and w: d(g_tx, g_ty), d(g_tz, g_tw) ≤ Ce^{−θ|t|} for t ≤ 0;
   * x and z are forward asymptotic, as are y and w: d(g_tx, g_tz), d(g_ty, g_tw) ≤ Ce^{−θt} for t ≥ 0.
7. Let S := δ_x − δ_y + δ_w − δ_z. It is nonzero: otherwise the multisets {x,w} and {y,z} would coincide, forcing x ∈ {y,z}.
   * For t ≤ 0, group S(φ∘g_t) as [φ(g_tx) − φ(g_ty)] + [φ(g_tw) − φ(g_tz)].
   * For t ≥ 0, group it as [φ(g_tx) − φ(g_tz)] + [φ(g_tw) − φ(g_ty)].
   So |S(Γ_tφ)| ≤ 2Ce^{−θ|t|}‖φ‖_{C^1}, and Theorem J (with ν = ω, J ≡ 0) gives S = 0. Contradiction. ∎

**Theorem D.** If X is GH, preserves a smooth positive density, and b_1(M) ≥ dim M − 2, then h_top(g_1) = 0.

*Proof.*
* If b = 0, then n ≤ 2 and Theorem A applies.
* Let b ≥ 1 and suppose h_top > 0. By step 1 of the proof of Theorem 7.5, h_ω(g_1) > 0.
* Let f = n − b ≤ 2. If f = 0 there are no vertical exponents. If f ∈ {1, 2}, the vertical exponents sum to 0 (Lemma 7.4(ii)) and one of them is 0 (Theorem 7.5), so all vertical exponents vanish.
* The quotient exponents vanish by Lemma 7.4(i). By [Os] all exponents of ω vanish, and [Ru] gives h_ω(g_1) = 0. Contradiction. ∎

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

Then (SC) implies (PE0), and hence (via Corollary C″, i.e. modulo [NF]) the problem in every dimension. In the volume-preserving case one chain suffices: a summable chain whose limit lies in the strong stable set of x_0 and which has an isolated vertex contradicts Theorem E.

*Proof.* Under GH, the data provided by (SC) contradict Theorem E′. ∎

*Remark (honest assessment).* (SC) is not proved. It is not known to be easier than (PE0). It moves the whole difficulty into the geometry of non-uniformly partially hyperbolic measures with a centre exponent 0 transverse to the flow: su-paths must be steered back into the weak-stable set of the base point, in the limit and with summable cost, along the centre directions. Some special cases do hold, though none of them is new:
* Hyperbolic measures (Katok horseshoes give homoclinic points of periodic orbits, i.e. finite chains). These are already excluded by Theorem B.
* Uniformly partially hyperbolic and fibred models (accessible, or integrable with local product structure inside su-leaves). These are model computations only, not theorems about general flows.

---

## 9. Other routes recorded (not used above; only briefly described, proofs not reproduced here)

These were explored and gave partial statements. They are recorded for orientation only. Nothing in §§1–8 depends on them, and they should be regarded as unproved in this document.
* **Finite su-configurations (volume case).** In the volume-preserving GH case, a finite chain of exponentially asymptotic unstable/stable legs that closes up to a flow shift, x_{2L} = g_τx_0, has τ = 0 and vanishing alternating configuration. In the general case, finite configurations with zero total boundary have zero unstable boundary. In both cases the argument is Theorem J with a group-ring device as in Theorem E′. The geometric existence of such closed configurations for non-hyperbolic measures is exactly what is missing.
* **Holomorphic eigen-families.** A positive-entropy measure yields a nonzero holomorphic family T_z of order-≤1 distribution densities with T_z(Pφ) = zT_z(φ) on a vertical strip. The problem would follow if GH excluded such families. The strip does not reach Re z = 0 in a way GH controls, and spectral-flatness arguments at 0 were shown to be insufficient in model examples.
* **Conformal measures / Hopf decomposition.** These give a second proof of the exclusion of hyperbolic positive-entropy pieces, but no proof of (PE0).
* **Tame estimate alone (Lemma 1.4) is insufficient.** Anosov flow × Diophantine translation satisfies the C^1-level a priori estimate and its dual, yet has positive entropy. So any proof must use the full kernel statement (Lemma 1.1, or Theorem J), not just the closed-range estimate.
* **Local injectivity of X + κ.** (PE0) would follow if, under GH, X + κ were injective on order-≤1 distributions for uncountably many small κ > 0. In the volume case this was shown to be equivalent to a dynamical statement that is still open.
* **Quantitative near-homoclinicity (volume case).** Using the tame inverse, approximate closing of su-configurations at polynomial precision would already contradict GH + volume. So the volume case reduces to a GH-free *rate* of accumulation of unstable on stable leaves, which was not obtained.

---

## 10. What remains open

1. **The problem in dimension ≥ 4.** By Corollary C″ (modulo [NF]) it is equivalent to **(PE0)**: under GH there is no ergodic invariant probability of positive entropy with zero mean divergence. Such a measure would have to satisfy all of the following:
   * be non-hyperbolic (Theorem B);
   * have full support, with μ-a.e. forward orbit dense (Proposition 6.5);
   * have dim M ≥ 4 (Theorem A).

   In the volume-preserving case it would also need b_1(M) ≤ dim M − 3 (Theorem D) and a zero vertical exponent (Theorem 7.5).
2. **The missing input** is geometric, not analytic. Theorems J, E and E′ kill every exact configuration of exponentially asymptotic points (finite, or infinite with summable legs) that cancels in the weak-stable class of its base point. What is not known is that a non-hyperbolic positive-entropy measure produces such a configuration; this is statement (SC) of Corollary 8.3. The obstruction is the centre direction transverse to the flow. In that direction su-paths do not close, and Pesin leaves depend only measurably (Hölder on Pesin sets) on the base point.
3. **Named known statements.**
   * The **Greenfield–Wallach conjecture** (every GH vector field on a closed manifold is smoothly conjugate to a Diophantine linear flow on a torus) implies the problem immediately, since such flows are isometric and have zero entropy.
   * In the volume-preserving case, Proposition 7.1 shows the problem is exactly the statement "**cohomology-free flows have zero topological entropy**", which is implied by **Katok's conjecture** (cohomology-free vector fields are smoothly conjugate to Diophantine linear flows).
   * As far as I recall these conjectures are proved in dimension ≤ 3 (Forni; Kocsard; F. and J. Rodriguez Hertz for the torus factor of dimension b_1), consistently with Theorem A. I know of no proof in dimension ≥ 4. These literature statements are recalled from memory and were not checked.
4. **Citations not re-verified here.**
   * [NF], used in Theorem C′ (Corollaries C″ and C‴ depend on it, the latter only in its classical one-dimensional form).
   * The C^1-continuity of local stable/unstable discs on Pesin sets, used in step 5 of Theorem 7.5 (part of [P]).
   * The classical theorems listed in §0.2.

---- END DRAFT ----
