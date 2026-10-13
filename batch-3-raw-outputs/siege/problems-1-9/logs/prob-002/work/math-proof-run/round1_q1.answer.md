# Lower bound n^{-2α/(2α+d+3)} for the Darcy problem

**Result.** Fix α>1, d≥2 and r∈(0,1). There are constants c>0 and n_0 such that for all n≥n_0
  inf_{f̂} sup_{f∈F(α,r)} E_f ||f̂−f||²_{L²(D)} ≥ c n^{-2α/(2α+d+3)}.
I prove this below. The proof uses no linearisation. Its main device is to write each perturbation as an exact angular Laplacian; this replaces the Bramble–Hilbert argument and controls the non-radial drift. Constants depend on α, d, r and the fixed profiles, and never on j or n.

The results I cite are quoted from memory:
- (E1) Gilbarg–Trudinger Thm 8.12/8.13 (global H² regularity). If g∈C^{0,1}(D̄) and g≥1/2, then L_g w = div(g∇w) with w∈H¹_0 satisfies ||w||_{H²} ≤ C||L_g w||_{L²}. The constant C depends only on ||g||_{C^{0,1}}.
- (E2) Gilbarg–Trudinger Thm 9.15 and Lemma 9.17 (W^{2,p} theory, 1<p<∞). For a nondivergence operator a_{ij}∂_{ij}+b_i∂_i with continuous a and bounded b, on a C^{1,1} domain with Dirichlet data, the solution exists, is unique and satisfies ||w||_{W^{2,p}} ≤ C||Lw||_{L^p}. We apply this to L_g w = gΔw+∇g·∇w with g∈C¹. The constant C is uniform over g∈F(α,r), because this family is compact in C¹.
- (A) Assouad's lemma (Tsybakov, Introduction to Nonparametric Estimation, Thm 2.12(ii), in squared-distance form).

## 1. The hypercube
- Choose ω_1,…,ω_M ∈ S^{d−1} with pairwise geodesic distance ≥ 2·2^{-j}. A maximal such set has M ≥ c_d 2^{j(d−1)}.
- Fix φ_0 ∈ C_c^∞([0,1/2)), constant near 0 and not identically 0. Set Φ_k(ω) = φ_0(2^j d_S(ω,ω_k)). This is smooth, and the supports of the Φ_k are disjoint.
- Extend each Φ_k to ℝ^d∖{0} as a function homogeneous of degree 0. Then ΔΦ_k = |x|^{-2}(Δ_SΦ_k)(x/|x|).
- Put χ_k := 2^{-2j}Δ_SΦ_k. In geodesic normal coordinates this is the rescaling by 2^j of the Laplacian of a fixed bump, up to metric corrections of order O(2^{-j}). Hence
  - ||∂^m χ_k||_∞ ≤ C_m 2^{jm} for every m;
  - c 2^{-j(d−1)} ≤ ||χ_k||²_{L²(S)} ≤ C 2^{-j(d−1)}. The lower bound holds because Δ applied to a nonzero compactly supported function is nonzero.
- Fix b ∈ C_c^∞((1/4,3/4)), not identically 0.
- Define
  h_k(x) := κ 2^{-j(α+2)} b(|x|) ΔΦ_k(x) = κ 2^{-jα} b(|x|)|x|^{-2} χ_k(x/|x|).
- For θ ∈ {0,1}^M put f_θ = 1 + Σ_k θ_k h_k.

**Membership in F(α,r).** Write G_θ := Σθ_kχ_k. Its pieces are disjoint and 2^{-j}-separated, and each satisfies ||∂^mχ_k||_∞ ≤ C2^{jm}. Hence 2^{-jα}G_θ ∈ C^α(S) with norm ≤ C, uniformly in θ and j. To see this, take m=⌊α⌋+1 (or second differences in the Zygmund case of integer α) and split the difference quotient:
- if |x−y| < 2^{-j}, use the bound on the (m)-th derivative;
- otherwise use the sup bound on the lower derivatives.
Multiplying by the smooth function b(|x|)|x|^{-2}, which is supported away from 0, keeps the norm bounded. Choosing κ small (depending on r) gives ||f_θ−1||_{C^α} ≤ r. Then f_θ ≥ 1−r and ||f_θ||_{C¹} ≤ 1+r, uniformly.

**Sizes.** By disjointness, ||f_θ−f_θ'||²_2 = Σ_{k:θ_k≠θ'_k} ||h_k||²_2. In polar coordinates,
  ||h_k||²_2 = κ²2^{-2jα} ∫ b(ρ)²ρ^{d−5}dρ · ||χ_k||²_{L²(S)} ≍ 2^{-2jα−j(d−1)}.
Also ||Φ_k||_{L²(supp b)} ≍ 2^{-j(d−1)/2} and ||Φ_θ||_∞ ≤ ||φ_0||_∞.

## 2. Key estimate
**Claim.** If θ and θ' differ only in coordinate k, then
  ||u_{f_θ} − u_{f_θ'}||_2 ≤ C 2^{-2j} ||h_k||_2.

**Exact identity.** Let f = f_θ', and let g = f+h with h = ±h_k, so that g = f_θ. Subtracting the two equations gives div(g∇(u_g−u_f)) = −div(h∇u_f). Hence
  u_g − u_f = −L_g^{-1} div(hV),  where V = ∇u_f.

**(i) Duality.** L_g is self-adjoint on H¹_0. Therefore
  ||L_g^{-1}F||_2 = sup_{||φ||_2≤1} ⟨F, ψ⟩,  ψ := L_g^{-1}φ,
and by (E1), ||ψ||_{H²} ≤ C. So it suffices to show |⟨div(hV),ψ⟩| ≤ C2^{-2j}||h_k||_2 ||ψ||_{H²} for every ψ ∈ H²∩H¹_0.

**Splitting.** Write V = x/d + W, where W = ∇(u_f−u_1) and u_1 = (|x|²−1)/(2d).

**(ii) Radial part.** Since Φ_k is 0-homogeneous, ΔΦ_k is homogeneous of degree −2. This gives the identity
  div(b ΔΦ_k · x/d) = (1/d)(r∂_r + d)(bΔΦ_k) = c(|x|) ΔΦ_k,  with c = (rb' + (d−2)b)/d ∈ C_c^∞(1/4,3/4).
Integrating by parts twice (cψ has compact support in D),
  |⟨div(h_k x/d), ψ⟩| = κ2^{-j(α+2)} |∫ Φ_k Δ(cψ)| ≤ C 2^{-j(α+2)} ||Φ_k||_{L²(supp c)} ||ψ||_{H²} ≤ C 2^{-2j} ||h_k||_2 ||ψ||_{H²}.
This step plays the role of the vanishing-moment / anisotropic Bramble–Hilbert argument.

**(iii) Drift part.** We have |⟨div(h_kW),ψ⟩| = |∫ h_k W·∇ψ| ≤ ||h_k||_2 ||W||_∞ ||ψ||_{H¹}. It remains to show ||W||_∞ ≤ C_ε 2^{-j(α+1−ε)} for every ε>0. Taking ε < α−1 then makes this term at most 2^{-2j}||h_k||_2 ||ψ||_{H²}.

*Equation for w.* Let w = u_f − u_1 and F = f−1 = Σθ'_l h_l. The same identity as above gives
  w = −L_f^{-1} q,  q = div(F x/d) = κ2^{-j(α+2)} c(|x|) ΔΦ_{θ'},
by step (ii) applied termwise, where Φ_{θ'} = Σθ'_lΦ_l.

*W^{2,p} bound.* We have ||q||_{L^p} ≤ C2^{-jα}, because q = κ2^{-jα}c|x|^{-2}Σθ'_lχ_l and the χ_l are bounded. By (E2), ||w||_{W^{2,p}} ≤ C_p 2^{-jα}.

*L^p bound.* By duality with ψ = L_f^{-1}φ, ||φ||_{L^{p'}} ≤ 1, and (E2) in L^{p'}:
  |∫ wφ| = |∫ qψ| = κ2^{-j(α+2)} |∫ Φ_{θ'} Δ(cψ)| ≤ C2^{-j(α+2)} ||Φ_{θ'}||_∞ ||ψ||_{W^{2,p'}} ≤ C2^{-j(α+2)}.
So ||w||_{L^p} ≤ C2^{-j(α+2)}.

*Interpolation.* Take p > d. The Gagliardo–Nirenberg inequality on the ball, ||∇w||_∞ ≤ C||w||^{t}_{W^{2,p}} ||w||^{1−t}_{L^p} with t = (1+d/p)/2, gives
  ||W||_∞ ≤ C 2^{-jα} 2^{-2j(1−t)} = C 2^{-j(α+1−d/p)}.
Taking p large proves the bound on ||W||_∞, and with it the Claim. Combining with the sizes from Section 1,
  ||u_θ − u_θ'||²_2 ≤ C 2^{-j(2α+d+3)}.

## 3. Assouad's lemma and the choice of j
In the white-noise model, KL(P_θ, P_θ') = (n/2)||u_θ − u_θ'||²_2 ≤ C n 2^{-j(2α+d+3)}. Choose 2^j ≍ n^{1/(2α+d+3)} with a constant large enough that KL ≤ 1/8 for all neighbours. Then by Pinsker, TV ≤ 1/4.

Apply Assouad's lemma to the squared L² loss. Because the supports are disjoint, the loss is additive over coordinates. This gives
  inf sup E||f̂−f||²_2 ≥ (M/8) · min_k ||h_k||²_2 · (1−1/4) ≥ c 2^{j(d−1)} 2^{-2jα−j(d−1)} = c 2^{-2jα} = c n^{-2α/(2α+d+3)}.
This holds for all large n, with c depending only on (α, d, r, φ_0, b). ∎

**Where α>1 is used.** It is used only in step (iii), to absorb the drift W. It also guarantees f ∈ C¹, which (E1) and (E2) need.

## 4. Other constructions
- **Concentrating at the source.** Take one bump at scale 2^{-j} at the origin. There |V| ~ 2^{-j}, and one gets KL ~ n 2^{-j(2α+d+4)}, while the separation is ||h||² ~ 2^{-j(2α+d)}. This gives the rate n^{-(2α+d)/(2α+d+4)}, which is faster, so it is not better.
- **Isotropic wavelets.** These give n^{-2α/(2α+d+2)}, which is also faster.
- **Radial oscillation.** Adding radial oscillation at frequency μ increases ||u−u'|| by a factor μ, so it does not help.

So n^{-2α/(2α+d+3)} is the best lower bound I can justify.

## Status
- **Proved:** the lower bound above. Cited facts E1, E2, A and Gagliardo–Nirenberg are from memory; the stated results are standard.
- **Not addressed (open here):** the matching upper bound n^{-2α/(2α+d+3)}, up to logarithmic factors. That part of the planner's conjecture remains open.

**Answer to the question:** the conjectured minimax rate, up to logarithmic factors, is n^{-2α/(2α+d+3)}. Only the lower-bound half is proved here.

=== END OF ANSWER round1_q1 ===
