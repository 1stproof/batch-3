# round4_q2: referee audit of the chain for the GOAL claim (ledger entry 18)

**Answer to the problem.** For small fixed r, the minimax rate is n^{-2α/(2α+d+3)}, up to logarithmic factors.

**Verdict.** PROVED AFTER THE REPAIRS GIVEN (R1–R5 below). None of the repairs changes a rate. They fix a misstated exponent, a missing converse in the transport lemma, a dangling reference in the cited Schauder fact, and some bookkeeping. Standard facts are accepted as cited from memory; I check each one for correct statement and applicability.

---

## Part A (lower bound): checked step by step

1. **Hypercube.**
   - Φ_k = φ_0(2^j d_S(·,ω_k)) is smooth: φ_0 is constant near 0, and d_S is smooth away from ω_k on the support.
   - The supports are caps of radius 2^{-j}/2 around 2·2^{-j}-separated points, so they are disjoint.
   - Let Φ be homogeneous of degree 0. Then ΔΦ = |x|^{-2}(Δ_SΦ)(x/|x|). Correct.
   - χ_k = 2^{-2j}Δ_SΦ_k satisfies ||∂^mχ_k||_∞ ≤ C2^{jm}. Correct.
   - Lower bound on ||χ_k||_{L^2(S)}. In rescaled normal coordinates, 2^{-2j}Δ_S converges, for j large, to the flat Laplacian applied to φ_0(|·|). That function is compactly supported and nonzero, so its Laplacian is nonzero. Hence ||χ_k||²_{L²(S)} ≍ 2^{-j(d−1)} for j ≥ j_0. Correct.
2. **Membership in F(α,r).** This is the usual estimate for a sum of disjoint bumps (split the difference quotients at |x−y| = 2^{-j}). It gives ||Σθ_k h_k||_{C^α} ≤ Cκ uniformly in θ and j. Taking κ = κ(r) small gives f_θ ∈ F(α,r). Correct.
3. **Sizes.** In polar coordinates, ||h_k||²_2 = κ²2^{-2jα}∫b²ρ^{d−5}dρ ||χ_k||²_{L²(S)} ≍ 2^{-2jα−j(d−1)}. Also ||Φ_k||_{L²(supp b)} ≍ 2^{-j(d−1)/2}. Correct.
4. **Exact identity.** Subtracting div(f∇u_f) = 1 from div(g∇u_g) = 1 gives div(g∇(u_g−u_f)) = −div(h∇u_f). Correct.
5. **Duality.** L_g is self-adjoint on H¹_0, so ||L_g^{-1}F||_2 = sup_{||φ||_2≤1}⟨F, L_g^{-1}φ⟩.
   - (E1) is GT Thm 8.12 combined with uniqueness. It gives ||ψ||_{H²} ≤ C for g ∈ C^{0,1}, g ≥ 1/2, with C uniform over the class. This applies because α > 1 gives g Lipschitz. Correct.
6. **Radial part.** The identity div(G x) = (r∂_r + d)G holds. For G = bΔΦ_k, which is homogeneous of degree −2 times b(|x|), it gives div(bΔΦ_k x/d) = ((rb' + (d−2)b)/d)ΔΦ_k. I checked this.
   - c has compact support in the annulus, so integrating by parts twice is legitimate.
   - The resulting bound C2^{-j(α+2)}2^{-j(d−1)/2}||ψ||_{H²} equals C2^{-2j}||h_k||_2||ψ||_{H²}. Correct.
7. **Drift part.**
   - Integration by parts: ⟨div(h_kW),ψ⟩ = −∫h_k W·∇ψ, with no boundary term because h_k has compact support.
   - Equation for w: div(f∇w) = div(∇u_1) − div(f∇u_1) = −div((f−1)x/d), so w = −L_f^{-1}q. Correct.
   - q = κ2^{-j(α+2)}cΔΦ_{θ'} = κ2^{-jα}c|x|^{-2}Σθ'_lχ_l, so ||q||_{L^p} ≤ C2^{-jα}.
   - (E2): GT Thm 9.15 and Lemma 9.17. These apply to the nondivergence form fΔ + ∇f·∇, which has continuous coefficients because f ∈ C¹. The constant is uniform because F(α,r) is bounded in C^α with α > 1, hence precompact in C¹.
   - L^p duality: |∫Φ_{θ'}Δ(cψ)| ≤ ||Φ||_∞||ψ||_{W^{2,p'}}. This gives ||w||_p ≤ C2^{-j(α+2)}. Correct.
   - Gagliardo–Nirenberg on the ball. In its bounded-domain form, ||∇w||_∞ ≤ C||w||_{W^{2,p}}^t||w||_p^{1−t} + C||w||_p, with t = (1+d/p)/2 < 1 for p > d. The extra lower-order term is O(2^{-j(α+2)}), so it is harmless (Repair R5, cosmetic). Then ||W||_∞ ≤ C2^{-j(α+1−d/p)}. With d/p < α−1 this term is ≤ C2^{-2j}||h_k||_2||ψ||_{H²}. Correct, and this is where α > 1 is used.
8. **KL and Assouad.**
   - In the white-noise model, KL = (n/2)||u_θ−u_θ'||²_2 ≤ Cn2^{-j(2α+d+3)}.
   - The supports are disjoint, so ||f̂−f_θ||² ≥ Σ_k||(f̂−f_θ)1_{S_k}||². The usual reduction (θ̂_k chosen as the nearer of the two values on S_k) bounds the risk below by (min_k||h_k||²/4)·E·Hamming. Tsybakov Thm 2.12(ii) then gives ≥ cM min_k||h_k||² ≍ 2^{-2jα} ≍ n^{-2α/(2α+d+3)}. Correct.

**Part A is correct.** It holds for every α>1, d≥2 and r∈(0,1), with c = c(α,d,r).

---

## Part B (upper bound): checked step by step

### Cited facts
- **(C1) Seeley extension.** Correctly stated. The reflections R_i send {1<|t|<1+η} into {1−λ_iη<|z|<1} when λ_iη<1. Boundedness on C^k for k ≤ S_0+1, plus real interpolation, gives boundedness on B^s_{∞∞} for 0 < s ≤ S_0.
- **(C2) Approximation.** Correct. In the middle bullet the factor J is needed only when m = s is an integer (Zygmund case). For m < s the bound is C||g||_{C^s} with no J.
- **(C3) Taylor remainder and algebra property.** Correct as stated. The log appears only for integer a, e.g. Δ_hA − ∇A·h = ∫_0^1(∇A(x+th)−∇A(x))·h dt with ∇A in the Zygmund class C^1_*.
- **(C4) Schauder estimate: dangling reference.** The text refers to "(I1)", which is not in the spliced chain. **Repair R3** supplies a self-contained argument, which is also exactly where smallness of r enters.
  - Let Δ_D^{-1} be the Dirichlet Laplacian inverse on the ball. It is bounded C^{α−1}(D) → C^{α+1}(D) for α−1 > 0. This is the Zygmund-scale Schauder estimate for the Laplacian on a smooth domain, cited from memory.
  - Write L_f = Δ + div((f−1)∇·). Since C^α·C^α ⊂ C^α (algebra property, (C3)) and ∂: C^{s} → C^{s−1}, ||div((f−1)∇v)||_{C^{α−1}} ≤ C_1||f−1||_{C^α}||v||_{C^{α+1}} ≤ C_1 r||v||_{C^{α+1}}.
  - For r ≤ r_0 with C_1r_0||Δ_D^{-1}|| ≤ 1/2, a Neumann series gives L_f^{-1}: C^{α−1} → C^{α+1}∩{v|_{∂D}=0}, with norm ≤ 2||Δ_D^{-1}||.
  - The subtraction identity of Part A gives u_f − u_1 = −L_f^{-1}div((f−1)x/d), and ||div((f−1)x/d)||_{C^{α−1}} ≤ Cr. Hence ||u_f−u_1||_{C^{α+1}} ≤ Cr, and ||u_f||_{C^{α+1}} ≤ C. This is (C4).
- **(C5) Gaussian facts.** Standard and correctly stated.

### Section 1: estimator and kernel properties
- **E^*.** It equals 1_D·φ + Σ_i a_i(χφ)(R_i^{-1}z)|det DR_i^{-1}(z)|, supported where R_i^{-1} is defined. The Jacobians are bounded.
- **(K1).** Immediate.
- **(K2).** Let t = R_i^{-1}z with |t| > 1, and let x ∈ D with |x−t| ≤ C2^{-J}. Then |t|−1 ≤ C2^{-J} and |z−t| = (1+λ_i)(|t|−1) ≤ C'2^{-J}. Correct.
- **(K3).** sup² × support volume gives 2^{2J(d+|a|)}·2^{-Jd}. The Lipschitz constant comes from the next derivative. Correct.
- **Event A.** Since n^{-1/2} ≤ 2^{-J(α+(d+3)/2)}, the three stated bounds follow. Correct.

### Lemma 1 (fields): misstated exponent, Repair R1
- The first two bullets are correct. ||V_J−V||_{C^1} ≤ C2^{-J(α−1)} by (C2) with m ≤ 1 < α = s, and ||V−x/d||_{C^1} ≤ ||u−u_1||_{C^2} ≤ C||u−u_1||_{C^{α+1}} ≤ Cr.
- **The third bullet is misstated.** V^E ∈ C^α with norm ≤ C, so (C2) gives directly ||D^mV_J||_∞ ≤ CJ2^{J(m−α)_+}. That is the correct, stronger bound.
- The later steps use exactly this stronger bound:
  - ||D div V_J|| ≤ ||D²V_J|| ≤ CJ2^{J(2−α)_+};
  - ||D² div V_J|| ≤ ||D³V_J|| ≤ CJ2^{J(3−α)_+}.
- With the misstated exponent (m+1−α)_+ the argument would fail in §5, which needs ||∇f_0|| ≤ 2^J. **R1: replace (m+1−α)_+ by (m−α)_+.** With that change every later use is consistent.

### Lemma 2 (geometry): correct
1. x − dX(x) = −d(X − x/d)(x). This map has sup ≤ dε and Lipschitz constant ≤ dε, so it maps B(0,1/2) into itself as a contraction. That gives a zero with |x_X| ≤ dε. Uniqueness follows from item 2.
2. Use the mean-value matrix A, with ||A − I/d|| ≤ ε. The segment lies in D because D is convex.
3. On |γ| = 1, γ·X(γ) ≥ 1/d − ε. So the backward flow points inward and D is invariant.
4. d/ds r² = −2(γ−x_X)·X(γ) ∈ [−2(1/d+ε)r², −2(1/d−ε)r²].
5. The symmetric part of DX is ≥ (1/d−ε)I.
6. tr DX ≥ 1 − dε.

### Lemma 3 (transport inverse): correct, plus a converse (Repair R2)
- **(a).** d/ds[g(γ)w] = −(X·∇g + g div X)(γ)w = −H(γ)w. Then w(S) → 0 and g is bounded. Correct.
- **(b).** ∫w ≤ 1/(1−dε) ≤ 2. Correct.
- **(c).** We have |X(y) − y/d| ≤ ε(1+|y|). So on |γ| ≥ 1/2, d/ds|γ|² ≤ −1/(2d) + 4ε ≤ −c. Hence |γ| is decreasing there, and once the ray leaves the layer {|x|>1−C2^{-J}} it never returns (1−C2^{-J} > 1/2). The time spent in the layer is ≤ C2^{-J}, and w ≤ 1. Correct.
- **(d).** ∇_x T^{-1}H = ∫[DΦ_{-s}^T∇H(γ)w + H(γ)∇_xw]ds, with ∇_x w = −w∫_0^s DΦ_{-σ}^T∇div X(γ)dσ. Since ||DΦ_{-σ}|| ≤ e^{-cσ}, we get |∇_x w| ≤ C||D div X||w. Differentiation under the integral is dominated by w(s). Correct.
- **(e).** ∂²w = w[(∂log w)² + ∂²log w]. Here |∂log w| ≤ C||D div X||, and |∂²log w| ≤ s(||D²div X|| + ||D²Φ||·||D div X||). For D²Φ_{-s}: the variational equation has contracting linear part and forcing ≤ ||D²X||e^{-2cσ}, so ||D²Φ_{-s}|| ≤ C||D²X||. Everything is integrable against w(s)(1+s)². Correct as stated.
- **Missing converse (R2).** §3 uses div(f_0V_J) = 1, T_{V̂}f̂ = 1 and T_{V_J}Z = div(f_0∇ξ), and §4 uses T_{V_J}f_0 = 1. These need the converse of (a), which is not stated.
  - **(a') Statement.** If X ∈ C², H ∈ C¹ and g := T_X^{-1}H, then g ∈ C¹ (by (d)) and T_Xg = H.
  - **Proof.** By the flow property, g(Φ_{-t}x) = w_x(t)^{-1}∫_t^∞ H(γ_x(s))w_x(s)ds. Differentiate at t = 0, using d/dt w_x(t)^{-1} = div X(γ_x(t))w_x(t)^{-1}: −X·∇g(x) = div X(x)g(x) − H(x), i.e. T_Xg = H. ∎
  - **Applicability.** In each use the hypotheses hold. V_J and V̂ (on A) are smooth. H = 1 is C¹. H = div(f_0∇ξ) is C¹ because f_0 ∈ C² by (e).

### Section 3: identity (★): correct, given R2
- Step 1 uses T_{V̂}f̂ = 1 and T_{V_J}f_0 = 1 (R2), together with V̂ = V_J + ∇ξ.
- Step 2 uses T_{V_J}Z = div(f_0∇ξ) (R2).
- Step 3 applies Lemma 3(a) to f̂ − f_0 + Z with X = V̂. This function is C¹: f̂ and Z are C¹ by (d)/(a'), and f_0 is smooth. Also div(Z∇ξ) is continuous.
- So every function to which (a) is applied is C¹.
- The f_0 bounds are correct with R1:
  - ||∇f_0|| ≤ CJ2^{J(2−α)_+};
  - ||D²f_0|| ≤ CJ²2^{J(3−α)_+}, using 2(2−α)_+ ≤ (3−α)_+ for α ≥ 1.

### Section 4: bias: correct
- **Identity.** T_{V_J}(f_0−f) = −div(f∇b), using R2 and div(f∇u) = 1. Here f_0 − f ∈ C¹ because f ∈ C^α ⊂ C¹. So (a) applies. Correct.
- **Commutator algebra.** I verified it directly:
  - F(x)(k_J*V^E)(x) − k_J*(FV^E)(x) = −∫k_J(−h)Δ_hF(x)[V^E(x) + Δ_hV^E(x)]dh = gV^E + R,
  - because ∫k_J(−h)Δ_hF(x)dh = k_J*F − F = −g. Correct.
- **The divergence.** div k_J*(FV^E) = 1 + k_J*G, since ∫k_J = 1. Also G ∈ C^{α−1}: it is a product of C^{α−1} and C^α functions, and α − 1 > 0. And G = 0 on D. Correct.
- **(i) The term div(gV).** g ∈ C¹ since α > 1. The four sizes follow from (C2) with m < s in every case. The contribution is ≤ C2^{-Jα} + C2^{-J(2α−1)}. Correct.
- **(ii) The term div R.**
  - Differentiation under the integral is legitimate (F, V^E ∈ C¹).
  - Each term is Δ_hA·Δ_hB with (a,b) = (α−1,α) or (α,α−1).
  - When a < 1, the Taylor polynomial P_A is empty, so Δ_hA = r_A. In every case the non-polynomial part is ≤ C|h|^{min(1+a,1+b,a+b)}L² = C|h|^αL², with L = 1 + log(1/|h|).
  - The polynomial parts P_AP_B have degrees in [2, a+b) ⊂ [2, 2α−1]. So they integrate to zero by the vanishing moments, since S ≥ 2α+2.
  - Result: ||div R||_∞ ≤ CJ²2^{-Jα}. Correct.
- **(iii) The term k_J*G.** On D, k_J*G = k_J*G − G = O(2^{-J(α−1)}), by (C2) with m = 0 and s = α−1. It is supported within C2^{-J} of ∂D, by the support of k_J. Lemma 3(c) then gives C2^{-Jα}. Correct.
- **Total.** ||f_0−f||_∞ ≤ CJ²2^{-Jα}. The section header's "CJ" should read "CJ²" (R4, cosmetic). The assembly correctly uses J².

### Section 5: variance: correct
- **Representation.** It follows from (C5): the integrand s ↦ w(s)D_yk_J(γ(s),·) is continuous into L², with norm ≤ Cw(s)2^{J(d/2+2)}, so it is Bochner integrable.
- **Pointwise bound.** It uses ||∇f_0|| ≤ CJ2^{J(2−α)_+} ≤ 2^J. This holds because (2−α)_+ < 1 strictly for α > 1. **This step needs R1.**
- **Energy bound.** ∫μ(B(z,δ))²dz ≤ |B_δ|∫μ(B(y,2δ))μ(dy), by Fubini. Correct.
- **Ray measure.** r(s) ≥ ρ_xe^{-(1/d+ε)s} gives w ≤ e^{-(1−dε)s} ≤ (r/ρ_x)^β, with β = d(1−dε)/(1+dε) > 1 for d ≥ 2. The change of variables (M) is valid because r is strictly decreasing with |r'| ≥ (1/d−ε)r. (The single point x = x_J is null.)
- **Small-ball masses.** The window [ρ(y)−2δ, ρ(y)+2δ] gives the two cases as stated. The bound (ρ(y)/ρ_x)^β is a valid upper bound even when ρ(y) > ρ_x, because r' ≤ ρ_x.
- **Integration.**
  - The r' ≥ 4δ part gives Cδρ_x^{-2β}∫_0^{ρ_x}r'^{2β−2}dr' = Cδ/ρ_x, which needs β > 1/2. This part is empty if ρ_x < 4δ.
  - The r' < 4δ part gives ≤ Cmin(1,(δ/ρ_x)^{2β}) ≤ Cmin(1,δ/ρ_x).
  - Hence ||h_x||² ≤ C2^{J(d+4)}min(1, 2^{-J}/ρ_x) ≤ C2^{J(d+3)}|x−x_J|^{-1}.
- **Conclusion.** This is integrable on D for d ≥ 2. So E||Z||²_2 ≤ Cn^{-1}2^{J(d+3)} ≤ C2^{-2Jα}. Correct.

### Section 6: remainder and bad event: correct
- **||G_ξ||.** The second term is CJ²2^{J((2−α)_+−α−1/2)}, and (2−α)_+ − 1 < 0. So ||G_ξ|| ≤ CJ²2^{-J(α−1/2)}; the stated "CJ" holds for J large. The J-power is immaterial (R4).
- **||∇G_ξ||.** The three exponents are all ≤ −(α−3/2), because (2−α)_+ ≤ 1 and (3−α)_+ ≤ 2 for α > 1. So ||∇G_ξ|| ≤ CJ³2^{-J(α−3/2)}.
- **Z and ∇Z.** ||Z|| ≤ 2||G_ξ||. For the gradient, ||∇Z|| ≤ C(||∇G_ξ|| + ||G_ξ||·J2^{J(2−α)_+}) ≤ CJ³2^{-J(α−3/2)}.
- **div(Z∇ξ).** ||div(Z∇ξ)|| ≤ CJ⁴2^{-J(2α−1)}. This is o(2^{-Jα}) if and only if α > 1. Correct.
- **Bad event.**
  - The standard deviation of each component of D^mξ is σ_m ≤ Cn^{-1/2}2^{J(d/2+m)}.
  - The canonical metric is ≤ Cσ_m2^J|x−x'|, so the Dudley entropy integral is ≤ Cσ_m√J.
  - Borell–TIS at level Jσ̄_m (with σ̄_m = n^{-1/2}2^{J(d/2+m)}), followed by a union bound over finitely many components, gives P(A^c) ≤ Ce^{-cJ²} uniformly in f. Correct.

### Section 7: assembly: correct
- Truncation is valid: ||f−1||_∞ ≤ ||f−1||_{C^α} ≤ r gives f ∈ [1−r, 1+r], so clipping only reduces |f̃−f|.
- Off A the loss is ≤ 4r²|D|.
- Summing the bounds gives CJ⁴2^{-2Jα}. Then 2^{-2Jα} ≤ 2^{2α}n^{-2α/(2α+d+3)} and J ≤ log₂n.
- The finitely many n with J < J_0 (where Lemma 1's ε-closeness may fail) are covered by the trivial bound 4r²|D|.
- The estimator uses only Y, n, r and fixed kernels, and J depends only on n.

---

## Repairs
- **R1.** Lemma 1, third bullet: ||D^mV_J||_∞ ≤ CJ2^{J(m−α)_+}, which follows from V^E ∈ C^α and (C2). This is the bound actually used in §3, §5 and §6. With it every later exponent is consistent.
- **R2.** Add the converse Lemma 3(a') with its proof (above). It is needed for T_{V_J}f_0 = 1, T_{V̂}f̂ = 1 and T_{V_J}Z = div(f_0∇ξ), all used in (★) and in the bias identity.
- **R3.** Replace the dangling "(I1)" in (C4) by the Neumann-series argument above. This uses the Zygmund Schauder estimate for the Dirichlet Laplacian on the ball (cited from memory) and is where r ≤ r_0 enters.
- **R4.** Cosmetic J-power bookkeeping: the §4 header should say CJ², and ||G_ξ|| carries J² before absorption. The final (log n)^4 is unaffected.
- **R5.** The bounded-domain Gagliardo–Nirenberg inequality in Part A carries an extra lower-order term C||w||_p, which is harmless.

## Final verdict
**PROVED AFTER THE REPAIRS GIVEN (R1–R5).**
- **Lower bound (Part A):** for every α > 1, d ≥ 2 and r ∈ (0,1), the minimax risk is ≥ c n^{-2α/(2α+d+3)}.
- **Upper bound (Part B):** for r ≤ r_0(d,α), the minimax risk is ≤ C(log n)^4 n^{-2α/(2α+d+3)}, with no log when α is not an integer.

Hence, for every α > 1, d ≥ 2 and every fixed r ∈ (0, r_0], the minimax L²-rate is n^{-2α/(2α+d+3)} up to logarithmic factors.

**Dependence on cited facts.** The proof rests on standard facts cited from memory and not re-proved here:
- Seeley extension on Zygmund spaces;
- kernel approximation bounds;
- Zygmund Taylor remainders and the algebra property;
- Schauder estimates for the Dirichlet Laplacian on the Zygmund scale;
- GT H² and W^{2,p} estimates;
- Gagliardo–Nirenberg;
- Dudley's entropy bound and Borell–TIS;
- Assouad's lemma.

**Open (outside the claim):**
- whether the (log n)^4 factor for integer α can be removed;
- the behaviour for r not small, where Part B's Neumann-series Schauder bound and the near-radial geometry of Lemma 2 are not available.

=== END OF ANSWER round4_q2 ===
