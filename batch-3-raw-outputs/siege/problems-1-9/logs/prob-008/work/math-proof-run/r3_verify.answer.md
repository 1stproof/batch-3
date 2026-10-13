# Referee report on the draft "Globally hypoelliptic flows and topological entropy"

Plan: go through §§1–8 in order, recheck every computation, then classify the issues and assess the status claims (§0.3, §10). All literature statements below are from memory and are marked as such.

## 0. Verdict in brief

* **The problem's main claim is NOT proved by the document** (zero topological entropy for every GH field on every compact connected M). The document says the same. What is missing is (PE0) in dimension ≥ 4, equivalently (SC). Outside the case covered by Theorem D, the volume-preserving case is also missing.
* I found **no fatal error.** Each stated result is proved as stated, modulo the citations the document lists, together with two small additions to those citations (items S1 and S2 below):
  * Theorem A (dim ≤ 3);
  * Theorem B;
  * Theorem C;
  * Theorem C′, modulo [NF];
  * Corollaries C″ and C‴;
  * Proposition 6.5;
  * Theorem D and Theorem 7.5;
  * Theorems E and E′, and Corollary 8.3 (a purely logical reduction).
* I re-derived every displayed identity: the cocycle identities, the derivative of Γ_t, the moment recursion, the Cayley–Hamilton step, the holonomy identity (6.1), the identity S(Γ_tφ) = e^{J_t(x)}Σw_iΨ(y_i′), the leg identities in Lemma 8.1, and the group-ring cancellation. All are correct.

## 1. Step-by-step check

**Lemma 1.1.** Correct.
* v_ε → 1_{u≥c} pointwise and boundedly, so Xv = 0 in D′, and GH applies to the L^∞ function v.
* The continuous representative w takes values in {0,1} off a null open set, hence everywhere.
* For complex u, X is real, so the argument applies to Re u and Im u.

**Lemma 1.2.** Correct. In (F2) for complex c′, take real and imaginary parts (trivial).

**Lemma 1.3.** Correct.
* S(Pφ) = e^{J_P(q)}φ(g_Pq) − φ(q) = (e^{J_P(q)} − 1)φ(q).
* S is a positive measure on a ν-null set, so it is not cν.
* The Jacobian remark is fine, because the density at q is the same at both ends of the period.

**Lemma 1.4.** Correct.
* F_s is complete: if u_m → u in H^{−s} and Xu_m → f in C^∞, then Xu = f.
* The closed graph theorem gives a bound by finitely many seminorms.
* The compactness argument needs ‖u‖_{H^{−s}} ≤ C‖u‖_{H^r}; this holds since r ≥ 0 ≥ −s.
* c(·) is continuous on H^{−s}.
* The final Cauchy argument is fine, with j = j(r).

**Corollary 1.5.** Correct (unused).

**Theorem J.** Correct.
* Step 1: d/dt[e^{J_t}φ∘g_t] = e^{J_t}(Pφ)∘g_t, and joint smoothness gives C^1 dependence into C^∞.
* Step 3: boundary terms vanish by (J) applied to φ, and F′_φ = F_{Pφ} is integrable by (J) applied to Pφ.
* Step 4: the induction alternates (F1) and (F2) correctly.
* Step 5: G is holomorphic on the strip, all its derivatives vanish at 0, so G ≡ 0, and Fourier uniqueness applies to the continuous L^1 function F_φ.
* Remark (ii), the north–south example, is correct: J_t(y) → −∞ linearly in both time directions.

**Lemma K.** Correct.
* Γ is a group: Γ_sΓ_t = Γ_{s+t}. So L^m = Γ_{−mP}, and Σ_jw_j(Γ_tφ)(y_j) = (L^mQ(L)Φ_r)(y).
* J_{−mP}(y) = −Σ_{i=1}^m J_P(g_{−iP}y) is right.
* In step 6, K log(1/κ) > max(0, −I) + 1 gives an exponent < −1 per period in both cases I ≥ 0 and I < 0.
* Step 7: w_je^{J_t(y_j)} = q_je^{J_{t−jP}(y)}. This is bounded for t < jP and ≤ C − ε(t − jP) otherwise. Since j ≤ N, this is fine.
* Distinctness of the y_j and the conclusion S ≠ 0 (because w_N ≠ 0) are correct.

**Lemma K′.** Correct: under −X, J_t becomes J_{−t}.

**Corollaries 3.2 and 3.3.** Correct.
* q_1 is fixed by g_{−mP_1}, so (a) of Lemma K follows from the asymptotic phase.
* (b) follows from |J_t(y) − J_t(q_2)| = O(1).
* y ∉ γ_1 gives y ≠ q_1.
* Corollary 3.3 then contradicts Lemma 1.3.

**Lemmas 4.1 and 4.2.** Correct.
* μ̄ is flow-invariant because s ↦ (g_s)_*μ is 1-periodic.
* {(g_s)_*μ : s ∈ [0,1]} is a decomposition into g_1-ergodic measures. Such a decomposition is unique, so Jacobs applies.
* In Lemma 4.2, J_1∘g_s = J_1 + J_s∘g_1 − J_s is correct.
* The flow-direction exponent argument is correct: log|X| is a.e. finite and has the same distribution as log|X|∘g_t.

**Theorem B and Theorem A.** Correct, modulo [KLY].
* As recalled from memory: Katok (1980) covers flows on 3-manifolds; Lian–Young (C^2 (semi)flows, JAMS 2012) give horseshoes in any dimension. The hypotheses are an ergodic measure, positive entropy, only the flow exponent equal to zero, and the measure not carried by a fixed point.
* A horseshoe contains hyperbolic periodic orbits with transverse homoclinic points.
* Dimension count: for n = 2 one would need three distinct exponents. For n = 3 the exponents are simple and nonzero off the flow direction.

**Lemma 6.0.** Correct.
* w(fx) = w(x)/μ^{fξ}_{fx}(ξ(fx)) ≥ w(x).
* w_0 > 0 forces ξ = fξ mod μ, hence zero entropy.
* The final atom-counting identity is correct.

**Theorem C.** Correct, modulo [P] and [LS].
* For t ≤ 0, e^{J_t(x)} ≤ Ce^{(|λ|+δ)|t|} is beaten by e^{−θ|t|}, since θ > |λ| + δ.
* The time-reversal check holds: λ(−X) = −λ, and χ^+_min(−X) = |χ^−_max|.

**Proposition 6.5.** Correct.
* Atkinson's theorem (1976) is recalled correctly from memory. It also covers atomic (periodic) ergodic measures.
* The [n_i, n_i+1] are disjoint subintervals of [0, n_k], giving Z(n_k) ≥ (k−1)e^{−1−‖d‖}.
* Weak-* limits preserve m(Pφ) = 0, and (F1) gives full support.

**Theorem C′ (§6.3).** Correct, modulo [NF] as formulated.
* Lemma 6.1: weights add, and each monomial has weight ≥ |s|χ_l, so the degree is ≤ d_0.
* (6.1): β_{g_sw}(g_sz) = β_w(z) + ∫_0^s(…) is correct, and so is the series form.
* Lemma 6.4:
  * The identity T_m = Φ_m∘P^{(m′)}_w − Φ_m(0) holds because f^{−m}H_w^{−1} = f^{m′−m}H_{w_{m′}}^{−1}P^{(m′)}_w and w_m = f^{m′−m}H^{−1}_{w_{m′}}(0).
  * Every Faà di Bruno term carries at least one derivative of P, hence a factor O(e^{−(χ_l−δ)m′}).
  * Summability holds since δ(c_K + 1) < χ_l.
* Step 4: I re-derived β_{x_{m′}}(y_i′) + J_s(y_i′) − J_s(x_{m′}) = β_x(y_i) + J_t(y_i) − J_t(x). This gives the displayed formula.
* The bound on ‖Θ‖_{C^{K+1}} by e^{((K+2)c′_K + 2‖d‖)s} is right. It is the exponential of a function with C^{K+1} norm ≤ L + Ce^{c′_Ks} and oscillation ≤ 2s‖d‖, times φ∘g_s∘H^{−1}.
* (T_KΘ)∘P^{(m′)}_x has degree ≤ Kd_0 = D, so the moment condition kills it.
* Exponent bookkeeping: c″_Kδ|t| − (K+1)(χ_l−δ)|t| + (|λ|+δ)|t| ≤ −|t|/2. Correct.
* The proof uses positive entropy only to produce many generic points on ξ(x). This is consistent.

**Corollaries C″ and C‴.** Correct. The sum of exponents equals μ̄(d) by Birkhoff applied to J_t/t.

**Proposition 7.1 and Lemma 7.2.** Correct. One implicit step: in "CF ⇒ GH", c(f) = ∫f dω, because ∫Xu dω = 0. Hence ker c = ker ω.

**Proposition 7.3.** Correct.
* Integral periods make π well defined.
* The rank and kernel of (η_i) are flow-invariant. Minimality makes them constant, hence the kernel is trivial and π is a submersion.
* π is surjective, and Ehresmann gives the bundle.
* (c) and (d) are fine.

**Lemma 7.4.** Correct. Typo: "TM/V ≅ T^b × ℝ^b" should read TM/V ≅ M × ℝ^b (trivialised by Dπ).

**Theorem 7.5.** Correct, with one small gap (S1 below).
* Step 1 (all correct):
  * Unique ergodicity gives μ̄ = ω.
  * Abramov gives h_ω(g_c) = c·h_ω(g_1).
  * g_c is non-ergodic iff some eigenvalue σ ≠ 0 has cσ ∈ 2πℤ. This follows from the Fourier decomposition of g_c-invariant functions under the circle action ℝ/cℤ.
  * Rescaling preserves GH, π and the vanishing of exponents.
* Step 2: E^s ∩ V = V^− and E^u ∩ V = V^+, so E^s ⊕ E^u = V.
* Step 5:
  * W^s_loc(y) and W^u_loc(z) lie in the component F.
  * They are C^1-close to the discs of x inside F.
  * The graph-transform map is a 1/3-contraction of B̄_{r/2} × B̄_{r/2} into itself, since r/3 + r/6 = r/2.
* Step 7: the coefficient of δ_x in S is 1 or 2, so S ≠ 0. The two groupings give two-sided decay.

**Theorem D.** Correct.
* For f = 1, Lemma 7.4(ii) alone gives the zero exponent.
* For f = 2, Theorem 7.5 is needed.
* The quotient exponents are 0, since the action on M × ℝ^b is the identity.
* Ruelle then gives zero entropy.

**Lemma 8.1, Theorem E, Theorem E′.** Correct.
* Leg identity: w_ae^{J_t(a)}φ(g_ta) + w_be^{J_t(b)}φ(g_tb) = w_ae^{J_t(a)}[φ(g_ta) − e^{−r_t}φ(g_tb)].
* The partial sums of S and S′ differ by δ_{x_0} − w_{2N}δ_{x_{2N}}.
* In E′:
  * The E_k formula checks out.
  * For t ≥ T_0, all shifted times are ≥ |τ_k|, so step 1 applies.
  * The F-terms cancel by commutativity of ℂ[ℝ].
  * The case 1 − c_k[τ_k] = 0 is exactly (L5) + (HC) for chain k.
  * In step 4, v_1 is an isolated atom with coefficient w_{v_1}·1 (if τ_2 ≠ 0) or w_{v_1}(1 − c_2) ≠ 0 (if τ_2 = 0).
* Corollary 8.3 is a valid (trivial) implication.

## 2. Errors and gaps, by severity

**Fatal:** none found.

**Serious (repairable, but a precise argument or citation must be added):**
* **S1 (Theorem 7.5, step 4).** "ξ(x) contains a leaf-neighbourhood of x … so for δ small, y ∈ W^u_loc(x)" does not follow from [LS] as stated in §0.2. A point of W^u(x) that is M-close to x can be far from x intrinsically, because the immersed leaf returns.
  * Repair: add to [LS] the standard property of the Ledrappier–Strelcyn/Ledrappier–Young construction, recalled from memory: ξ(x) is contained in an embedded local Pesin unstable disc D(x) of measurable size. On D(x) the topology of M and the intrinsic topology agree. So for δ = δ(x) small, y ∈ ξ(x) ∩ B(x,δ) lies in the uniform-size disc W^u_loc(x) (x ∈ Λ_l).
  * δ may depend on x, which is all that step 5 needs. The same applies to ξ′ and W^s.
* **S2 ([NF], Theorem C′).** The hypotheses of the cited normal-form theorems were not checked; the document says so. Kalinin–Sadovskaya (JMD 2017) is, as far as I recall, formulated for measurable extensions by fibre maps of ℝ^m. Melnick (ETDS 2019) treats Pesin unstable manifolds.
  * Simplification: the proof needs only **local** normal forms on discs of measurable (tempered) radius, not global H_x : W^u(x) → E^u_x. The N_D + 1 points y_i can be chosen in ξ(x) arbitrarily close to x, since x lies in the support of its conditional for a.e. x. The citation should be restated in that local form.
  * The measurability of w ↦ ‖β_w∘H_w^{−1}‖_{C^{K+1}(B(0,1/L))}, needed for (G3), should be deduced explicitly from [NF](c) and the series (6.1).
  * Theorem C′ and Corollary C″ are therefore proved only conditionally, as the document says. Corollary C‴ needs only the classical 1-dimensional affine parameters; their C^{K+1} smoothness along leaves for C^∞ f is classical.

**Minor:**
1. §0.3 dependencies are slightly inaccurate:
   * Theorem J and Lemma K do not use [SM]; only Corollaries 3.2–3.3 do.
   * Theorem B (hence Theorem A) also uses [SM], via Corollary 3.3.
   * Theorem D for b = 0 invokes Theorem A, hence [KLY] and [SM]. It also uses Lemma 1.4 (closed graph theorem, Rellich) and Lemma 6.0.
   * Corollary C‴ also uses [Os], [Ru] and [KLY], via Theorem B.
2. §4 "Check … confirmed numerically": out of place in a proof. The one-line derivation from J_{t+s} = J_s + J_t∘g_s should replace it.
3. Lemma 7.4(i): T^b × ℝ^b should be M × ℝ^b.
4. Proposition 7.1: state c(f) = ∫f dω explicitly.
5. Corollary 8.3, volume case: "strong stable set" should be "exponentially forward-asymptotic with rate θ, i.e. (L5)".
6. [KLY]: make explicit that Katok's 1980 flow statement is for 3-manifolds, and that the general-dimension version (C^2) is Lian–Young (recalled from memory).
7. Lemma 1.2 (F2): complex constants need real and imaginary parts (trivial).

## 3. Are the stated results proved?

| Result | Status |
|---|---|
| Main problem (all dimensions) | **Not proved** |
| Theorem A (dim ≤ 3) | Proved, modulo [VP], [Os], [Ru], [KLY], [SM] |
| Theorem B | Proved, modulo [Os], [Ru], [KLY], [SM] |
| Theorem C | Proved, modulo [P], [LS] |
| Theorem C′ | Proved modulo [NF] (S2); unconditional in the 1-dimensional cases |
| Corollary C″ | Proved modulo [NF] |
| Corollary C‴ | Proved, modulo [P], [LS], [KLY], [Ru], [Os] and 1-dimensional affine parameters |
| Proposition 6.5 | Proved (GH and [At]) |
| Theorem 7.5 and Theorem D | Proved modulo the listed citations plus the [LS] localisation property (S1) |
| Theorems E and E′ | Proved (GH only) |
| Corollary 8.3 | Valid reduction; (SC) itself is unproved |

## 4. Accuracy of §0.3 and §10

* §0.3 is accurate except for the omissions in Minor item 1.
* §10 is accurate:
  * the open problem is (PE0) in dimension ≥ 4, outside Theorem D;
  * (SC) is unproved, and (SC) ⇒ (PE0) ⇒ problem, modulo [NF];
  * the Greenfield–Wallach and Katok conjectures would each imply the claim (Katok's in the volume case).
* The literature attributions in §10.3 cannot be verified here; the document already hedges them.
* One remark, low confidence, from memory: the literature (e.g. Forni's work on the GW and Katok conjectures in dimension 3) relates GH to the existence of a smooth invariant volume and to the equivalence of the two conjectures. If it were known that every GH field preserves a smooth volume, the problem would reduce to §7's setting (CF flows). The author should check this; I could not confirm it.

## 5. Open questions (as identified by the draft, confirmed)

1. (PE0): under GH, can there be an ergodic g_1-invariant μ with h_μ(g_1) > 0 and ∫J_1 dμ = 0? Such a μ would be non-hyperbolic and of full support, with n ≥ 4.
2. (SC), the geometric existence of summable su-chains with weak-stable endings, for non-hyperbolic positive-entropy measures.
3. The volume-preserving case with b_1(M) ≤ dim M − 3.

=== END OF ANSWER r3_verify ===
