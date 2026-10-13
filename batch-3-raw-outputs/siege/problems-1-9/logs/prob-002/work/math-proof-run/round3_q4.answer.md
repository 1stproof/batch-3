# Referee check of the lower-bound proof (ledger #4)

I checked every step. Minor remarks are given where relevant. None of them is a gap.

**1. Membership in C^α.** Write s=⌊α⌋ and g=2^{-jα}G_θ.
- Non-integer α. If |x−y|<2^{-j}, then |∂^s g(x)−∂^s g(y)| ≤ C2^{-jα}2^{j(s+1)}|x−y| ≤ C|x−y|^{α−s}. Otherwise the difference is ≤ 2C2^{-jα+js} ≤ 2C|x−y|^{α−s}.
- Integer α (Zygmund case). Take second differences of ∂^{α−1}g. For |h|<2^{-j}, use the second-derivative bound: C2^{-jα}2^{j(α+1)}|h|² ≤ C|h|. Otherwise use the sup bound: C2^{-j}≤C|h|.
- In both cases it does not matter if x and y lie in different bumps, because only sup bounds are used there.
- Multiplying by the smooth factor b(|x|)|x|^{-2} (supported in an annulus) and extending 0-homogeneously is a smooth operation on the annulus, so the norm stays bounded. Then choose κ small.
- F(α,r) is compact in C¹ by Arzelà–Ascoli, since α>1. Verdict: OK.

**2. Norms.** In polar coordinates the weight is |x|^{-4}ρ^{d−1}=ρ^{d−5}. Rescaling gives ||Δ_SΦ_k||² ≍ 2^{4j}2^{-j(d−1)}, so ||χ_k||² ≍ 2^{-j(d−1)}. The lower bound holds for j large, because the metric corrections are O(2^{-j}). Hence ||h_k||_2 ≍ 2^{-jα-j(d−1)/2} and ||Φ_k||_{L²(annulus)} ≍ 2^{-j(d−1)/2}.
- The supports have angular radius <2^{-j}/2 and centres ≥2·2^{-j} apart, so they are disjoint and 2^{-j}-separated. Verdict: OK.

**3. Homogeneity identity.** Let H=ΔΦ_k, which is homogeneous of degree −2. Then div(bH x)=x·∇(bH)+d·bH=r b'H−2bH+d·bH. Dividing by d gives c=(rb'+(d−2)b)/d ∈ C_c^∞(1/4,3/4). Verdict: correct.

**4. Step (ii).** Φ_k is smooth on supp c, which lies away from 0. Also cψ ∈ H² has compact support in the annulus, so integrating by parts twice produces no boundary terms. Then
  2^{-j(α+2)}·2^{-j(d−1)/2} ≍ 2^{-2j}||h_k||_2.
Verdict: OK.

**5. Step (i).** u_g−u_f = −L_g^{-1}div(hV) holds in H¹_0, and div(hV) ∈ H^{-1}. Self-adjointness gives ||L_g^{-1}F||_2 = sup⟨F,L_g^{-1}φ⟩. Estimate (E1) applies because g is Lipschitz and g ≥ 1−r. Verdict: OK.

**6. Step (iii).**
- The equation for w is correct: div(f∇w) = 1−Δu_1−div(F x/d) = −div(F x/d).
- ||q||_∞ ≤ C2^{-jα}. (E2) applies with continuous leading coefficient f and bounded drift ∇f. The constants are uniform over the C¹-compact family.
- Duality: ∫wφ = ∫w L_fψ = ∫(L_f w)ψ = −∫qψ, with both functions in W^{2,·}∩W^{1,·}_0. Then |∫Φ_{θ'}Δ(cψ)| ≤ ||Φ_{θ'}||_∞ ||Δ(cψ)||_{L¹} ≤ C||ψ||_{W^{2,p'}} ≤ C||φ||_{p'}. Here 1<p'<∞, so (E2) holds. The pairing is correct.
- Gagliardo–Nirenberg scaling: 1 = t(2−d/p)+(1−t)(−d/p) = 2t−d/p, so t=(1+d/p)/2. This is valid for p>d, i.e. t<1, in the bounded-domain form with the full W^{2,p} norm. The result is 2^{-jα}2^{-2j(1−t)} = 2^{-j(α+1−d/p)}.
- Choosing d/p ≤ α−1 gives ||W||_∞ ≤ C2^{-2j}. Moreover |∫h_kW·∇ψ| ≤ ||h_k||_2||W||_∞||ψ||_{H¹}.
- Remark: the claim holds for any θ', so it does not matter which of the two hypotheses is called f.

Verdict: OK. α>1 is used exactly here and for f ∈ C¹.

**7. KL divergence and Assouad.**
- In the white-noise model, KL = (n/2)||u_θ−u_θ'||². With KL ≤ 1/8, Pinsker gives TV ≤ 1/4.
- Additivity: ||f̂−f_θ||² ≥ Σ_k ||f̂−f_θ||²_{L²(supp h_k)} ≥ Σ_k (||h_k||²/4)·1{θ̂_k≠θ_k}, where θ̂_k is the nearest choice on that support.
- Averaging over the cube gives ≥ (M/8)·min||h_k||²·(1−1/4).
- M ≍ 2^{j(d−1)}, so the bound is ≍ 2^{-2jα} = n^{-2α/(2α+d+3)}, with 2^j ≍ n^{1/(2α+d+3)} times a large constant. Verdict: OK.

**Verdict: PROVED.** The argument proves exactly as stated that inf sup E||f̂−f||²_{L²} ≥ c n^{-2α/(2α+d+3)} for all α>1, d≥2, r∈(0,1) and n ≥ n_0. The cited results (E1), (E2), Assouad's lemma and Gagliardo–Nirenberg are standard and are cited from memory. Only the lower bound is checked here; the matching upper bound is still open in this ledger.

=== END OF ANSWER round3_q4 ===
