# Variance lemma (round3_q2): answer

**Summary.** (V1) and (V3) are proved below, along with every property of V_J that the proofs use. (V2) is proved when f is in C^2 (for example α > 2). In a corrected form it is proved for all α > 1: replace f by a smoothed conductivity f_J with ||f_J||_{C^1} ≤ C and ||D²f_J||_∞ ≤ C 2^{J(2-α)_+}. As literally stated, (V2) is **not provable by this method for 1 < α ≤ 2**, and I argue (heuristically, not rigorously) that it is false in general there. The reason is that ∇Z contains the term T^{-1}(D²f ∇ξ), and D²f is only a distribution.

## 0. Notation and conventions
- δ := C_0 2^{-J}, with C_0 chosen so that supp k_J(x,·) ⊂ B(x,δ).
- ρ(y) := |y - x_J|.
- ε := C(r + 2^{-Jβ}), where β ∈ (0, min(α-1,1)) is fixed. We assume r ≤ r_0 and J ≥ J_0, so that ε ≤ 1/(100 d²).
- The constant C changes from line to line. It depends only on α, d, r, k and E.

## 1. Kernel bounds for the Seeley-type extension
Take a Seeley-type extension
- E g(x) = g(x) for |x| ≤ 1;
- E g(x) = ψ(x) Σ_j a_j g(R_j x) for |x| > 1.

Here R_j x = (x/|x|)(1 - λ_j(|x|-1)) with λ_j > 0, ψ is a smooth cutoff, and Σ_j a_j(-λ_j)^k = 1 for k ≤ S+2.

Change variables y = R_j z in the reflected pieces. This gives
- k_J(x,y) = k_J(x-y) + Σ_j a_j k_J(x - R_j^{-1}y) ψ(R_j^{-1}y) |det DR_j^{-1}(y)|, for x, y ∈ D.

Each reflected term is non-zero only if |x - z| ≤ C2^{-J}, where z = R_j^{-1}y has |z| > 1. Since x ∈ D, this forces |z| - 1 ≤ C2^{-J}. Then |y - z| = (1+λ_j)(|z|-1) ≤ C2^{-J}, so |x-y| ≤ C2^{-J}.

The maps R_j^{-1}, the cutoff ψ and the Jacobians are smooth with bounded derivatives. Hence |∂_x^b ∂_y^a k_J(x,y)| ≤ C 2^{J(d+|a|+|b|)}.

Remark on smoothness in y: the function y ↦ k_J(x,y) is smooth on D̄, but this is never needed. All derivatives below fall on the **first** variable, the one in which ξ is differentiated. In that variable k_J(·,z) is C^∞ on all of R^d.

## 2. Properties of V_J
Let u_1 = (|x|²-1)/(2d). Then D²u_1 = I/d.

**Schauder step (cited from memory).** For the divergence-form Dirichlet problem on the ball, ||u_f - u_1||_{C^{2,β}(D̄)} ≤ C ||f - 1||_{C^{1,β}} ≤ C r.

**Extension and smoothing.** Eu ∈ C^{2,β}(R^d), and E u = u on D̄. On D the derivatives of E u up to order 2 agree with those of u. The kernel k has ∫k = 1 and vanishing moments. Hence
- ||D^j(k_J * Eu) - D^j u||_{L^∞(D)} ≤ C 2^{-J(2+β-j)} for j ≤ 2;
- ||D³(k_J * Eu)||_∞ = ||∂k_J * D²Eu||_∞ ≤ ||∂k_J||_{L^1} ||D²Eu||_∞ ≤ C 2^J.

Therefore:
- (P1) ||DV_J - I/d||_{L^∞(D)} ≤ ε, and div V_J ∈ [1 - dε, 1 + dε].
- (P2) ||D²V_J||_∞ ≤ C 2^J.
  - This crude bound suffices below. The sharper bound C2^{J(2-α)_+} also holds, with a log factor at α = 2.
- (P3) On the sphere, V_J·ν ≥ ∇u·ν - C2^{-J} ≥ 1/d - Cr - C2^{-J} ≥ 1/(2d), because ∇u_1·ν = 1/d.
- (P4) V_J has a unique zero x_J in D.
  - Uniqueness: D is convex, so (V_J(x) - V_J(x'))·(x - x') ≥ (1/d - ε)|x - x'|².
  - Existence: V_J·x > 0 on the sphere, so V_J has degree 1 there (homotopy to the identity), and a zero exists in the open ball.
- (P5) Writing A(y) := ∫_0^1 DV_J(x_J + θ(y - x_J)) dθ, we have V_J(y) = A(y)(y - x_J) and ||A - I/d|| ≤ ε.

**The backward flow.** The field V_J is Lipschitz on D̄. By (P3), the backward field -V_J points strictly inward on ∂D. So the backward flow γ(s) = Φ_{-s}x, with γ' = -V_J(γ), exists for all s ≥ 0 and stays in D̄.

**Flow estimates.**
- (F1) By (P5), dρ(γ)/ds = -(γ - x_J)·A(γ - x_J)/ρ ∈ [-(1/d+ε)ρ, -(1/d-ε)ρ]. Hence ρ(x) e^{-(1/d+ε)s} ≤ ρ(γ(s)) ≤ ρ(x) e^{-(1/d-ε)s}. In particular γ(s) → x_J.
- (F2) Let w(s,x) := exp(-∫_0^s div V_J(γ(σ)) dσ). Then e^{-(1+dε)s} ≤ w ≤ e^{-(1-dε)s}, so ∫_0^∞ w ds ≤ 2.
- (F3) The derivative satisfies (d/ds) DΦ_{-s} = -DV_J(γ) DΦ_{-s}. By (P1), (d/ds)|DΦ_{-s} e|² ≤ -2(1/d - ε)|DΦ_{-s} e|². Hence ||DΦ_{-s}|| ≤ e^{-(1/d-ε)s}.
- Consequence for the weight: ∂_e w(s,x) = -w ∫_0^s ∇div V_J(γ(σ))·DΦ_{-σ}e dσ. By (P2) and (F3), |∂_e w| ≤ C 2^J w.

The ray estimate (F4) of the earlier sketch is **not needed**. It is replaced by Lemma B, which uses only (F1).

## 3. Two lemmas
Define the ray measure μ_x := ∫_0^∞ w(s,x) δ_{γ(s)} ds. By (F2), its total mass is μ_x(D̄) ≤ 2.

**Lemma A (L² size of a smeared measure).**
- Hypotheses:
  - ν is a positive measure on D̄ with ν(D̄) ≤ M and sup_y ν(B(y,2δ)) ≤ N;
  - |a(y,z)| ≤ A, and a(y,z) = 0 whenever |y - z| > δ;
  - h(z) := ∫ a(y,z) dν(y).
- Conclusion: ||h||²_{L²} ≤ A² |B_δ| M N.
- Proof.
  1. Pointwise, |h(z)| ≤ A ν(B(z,δ)).
  2. By Fubini, ∫ ν(B(z,δ))² dz = ∫∫ |B(y,δ) ∩ B(y',δ)| dν(y) dν(y').
  3. The intersection has volume at most |B_δ|, and it is empty unless |y - y'| < 2δ.
  4. So the double integral is at most |B_δ| ∫ ν(B(y,2δ)) dν(y) ≤ |B_δ| M N. ∎

**Lemma B (no concentration of the ray measure).**
- Statement: for every y, μ_x(B(y,2δ)) ≤ C min(1, δ/ρ(x)).
- Proof. The bound by 1 (up to the constant 2) is the total mass, so assume ρ(x) > δ. Let t = ρ(y).
  - **Case t ≤ 4δ.** Then B(y,2δ) ⊂ B(x_J,6δ).
    1. By (F1), the ray is inside B(x_J,6δ) only for s ≥ s_0, where e^{-(1/d+ε)s_0} = 6δ/ρ(x) (taking s_0 = 0 if that is negative).
    2. By (F2), the mass there is at most ∫_{s_0}^∞ e^{-(1-dε)s} ds ≤ C(6δ/ρ(x))^{(1-dε)/(1/d+ε)}.
    3. The exponent is ≥ d - Cε ≥ 1. Since δ/ρ(x) < 1, this is ≤ Cδ/ρ(x).
  - **Case t > 4δ.** On B(y,2δ) we have ρ ∈ [t - 2δ, t + 2δ].
    1. By (F1), log ρ(γ(s)) decreases at rate at least 1/d - ε.
    2. So the set of times s at which γ(s) ∈ B(y,2δ) has measure at most log((t+2δ)/(t-2δ))/(1/d - ε) ≤ Cδ/t.
    3. At those times ρ(γ) ≤ 2t. Using (F1) with the upper rate, then (F2): w ≤ e^{-(1-dε)s} ≤ (2t/ρ(x))^{d-Cε}.
    4. The mass is therefore at most C(δ/t)(t/ρ(x))^{d-Cε} = C(δ/ρ(x))(t/ρ(x))^{d-1-Cε}.
    5. Since t ≤ ρ(γ(s)) + 2δ ≤ ρ(x) + 2δ ≤ 3ρ(x) and d - 1 - Cε > 0, this is ≤ Cδ/ρ(x). ∎

## 4. Proof of (V1)
**Writing Z(x) as a Gaussian variable.** Let L := div(f∇·), so L_y g = f Δg + ∇f·∇g. Here f ∈ C^1 with ||f||_{C^1} ≤ 1 + r.

The field ξ(y) = W(k_J(y,·)) has a version that is C^∞ in y (Kolmogorov). Its derivatives are W(∂_y^b k_J(y,·)), and Lξ(y) = W(L_y k_J(y,·)).

The map y ↦ L_y k_J(y,·) ∈ L² is continuous, and ∫ w ds < ∞. Riemann sums of the Bochner integral converge both in L²(Ω) and almost surely. Hence, almost surely,
- Z(x) = ∫_0^∞ Lξ(γ(s)) w ds = W(h_x), where h_x(z) := ∫ L_y k_J(y,z) dμ_x(y).

**Bounding the variance.** By §1, |L_y k_J(y,z)| ≤ C2^{J(d+2)}, supported in |y - z| ≤ δ. Apply Lemma A with:
- A = C2^{J(d+2)};
- M = 2;
- N = C min(1, δ/ρ(x)) from Lemma B.

This gives
- E Z(x)² = ||h_x||²_2 ≤ C 2^{2J(d+2)} 2^{-Jd} min(1, 2^{-J}/ρ(x)) = C 2^{J(d+3)} min(2^J, ρ(x)^{-1}).

**Integrating over D.** Since d ≥ 2, ∫_D ρ^{-1} dx ≤ C. By Tonelli (Z is jointly measurable, being continuous in x by §5's differentiability), E||Z||²_{L²(D)} ≤ C 2^{J(d+3)}. ∎

Remarks:
- No log factor appears.
- The source x_J and the sphere cost nothing in L².
- The pointwise bound has the min(2^J, ρ^{-1}) factor. A uniform sup bound of order 2^{J(d+3)} is not claimed.
- Only f ∈ C^1 is used.

## 5. (V2): proved if f ∈ C^2; corrected form for all α > 1

**Differentiating Z.** Assume G := Lξ ∈ C^1. Since ||DΦ_{-s}|| ≤ 1 and |∂_e w| ≤ C2^J e^{-s/2}, differentiation under the integral is justified by domination. This gives ∂_e Z(x) = I_1 + I_2, where
- I_1 := ∫ ∇G(γ)·DΦ_{-s}e w ds = W(h^1_x);
- I_2 := ∫ G(γ) ∂_e w ds = W(h^2_x).

**The term I_1.** Here h^1_x(z) = ∫ ∇_y L_y k_J(y,z)·b(s) w ds with |b| ≤ 1. Also ∇_y L_y k = ∇f Δk + f ∇Δk + D²f ∇k + D²k ∇f, so |∇_y L_y k_J| ≤ C(1 + ||D²f||_∞ 2^{-2J}) 2^{J(d+3)}.

**The term I_2.** Here h^2_x is Lemma A applied to the measure |∂_e w| ds, which is ≤ C2^J μ_x. Lemma B therefore holds for this measure with an extra factor C2^J in both M and N.

**Bound.** Lemma A gives E(∂_e Z(x))² ≤ C 2^{J(d+5)} min(2^J, ρ^{-1}) for each of the two terms, provided ||D²f||_∞ ≤ C2^{2J}. Integrating over D:
- **E||∇Z||²_{L²(D)} ≤ C 2^{J(d+5)}.**

This proves (V2) whenever f ∈ C^2, i.e. α > 2. In the borderline Zygmund case α = 2, C^2 is not implied.

**Corrected form for all α > 1.** Define Z_J := T_{V_J}^{-1} div(f_J ∇ξ), where f_J := K_J f. Then ||f_J||_{C^1} ≤ C and ||D²f_J||_∞ ≤ C2^{J(2-α)_+} ≤ C2^{2J}. Hence:
- (V1) holds for Z_J;
- (V2) holds for Z_J, E||∇Z_J||² ≤ C2^{J(d+5)};
- ||f - f_J||_{C^1} ≤ C2^{-J(α-1)}, so (V1) for the difference Z - Z_J has the extra factor 2^{-2J(α-1)}.

**What fails for 1 < α ≤ 2 with the unsmoothed f.** The derivative ∇Z contains T^{-1}(D²f ∇ξ). Here D²f ∈ C^{α-2} is only a distribution, so this term is an integral of a distribution along rays. In the model case of a radial linear field V = (x - x_J)/d:
- T^{-1}g(x) = ∫ g(x_J + e^{-s/d}(x - x_J)) e^{-s} ds;
- this averages g over dilations only, so it preserves the angular regularity of g.

Now take f = 1 + c φ, with φ ∈ C^α built so that ∇φ has angular Weierstrass-type roughness of order α - 1 < 1. Then ∇f·∇ξ is, with positive probability, not in H^1 in the angular direction, and neither is T^{-1}(∇f·∇ξ). That would mean ∇Z ∉ L² with positive probability, hence E||∇Z||² = ∞.

I have **not** made this rigorous. The missing pieces are:
- the actual V_J is only a perturbation of the radial field (one would need a C^1 linearisation of the flow, plus the non-cancellation against T^{-1}(fΔξ), which lies in H^1);
- the choice of φ.

So the status is: (V2) for unsmoothed f with α ≤ 2 is **open, and I conjecture it is false**; the f_J version is proved.

## 6. Proof of (V3)
Fix one component X(x) := ∂^b_x ξ(x) = W(∂_x^b k_J(x,·)) with |b| = m. By §1:
- Var X(x) = ||∂^b_x k_J(x,·)||²_2 ≤ C 2^{2J(d+m)} 2^{-Jd} = C 2^{J(d+2m)} =: σ².
- The canonical metric satisfies d_X(x,x') ≤ σ min(2, C2^J|x - x'|), using the bound on ∂_x^{b+e_i} k_J. This needs derivatives of order ≤ 4, which are available.

**Expectation of the supremum.** The covering numbers of (D, d_X) at scale ησ are at most (C2^J/η)^d. Dudley's entropy bound (cited from memory) gives
- E sup_D |X| ≤ Cσ ∫_0^2 sqrt(d log(C2^J/η)) dη ≤ Cσ sqrt(J).

**Concentration.** The Borell–TIS inequality (cited from memory) gives P(sup|X| > E sup|X| + u) ≤ exp(-u²/(2σ²)). Therefore:
- E sup|X|² ≤ C J σ² = C J 2^{J(d+2m)};
- for t ≥ 2C sqrt(J), P(sup|X| > tσ) ≤ exp(-t²/8).

Take a union over the finitely many components of D^m ξ. This proves (V3) for m = 1, 2, 3. ∎

## Status
- **Proved:**
  - (V1) for f ∈ C^1, together with the pointwise bound E Z(x)² ≤ C2^{J(d+3)} min(2^J, |x - x_J|^{-1});
  - (V3);
  - the properties (P1)–(P5) and (F1)–(F3) of V_J, from C^{2,β} Schauder theory;
  - the kernel bounds for the Seeley extension;
  - (V2) when f ∈ C^2;
  - (V2) for the smoothed-conductivity operator Z_J, for every α > 1.
- **Open / conjectured false:** (V2) as stated, for 1 < α ≤ 2 with the unsmoothed f. Section 5 gives a heuristic counterexample mechanism: angular roughness of ∇f is transported unchanged.
- **Recommendation:** the upper-bound argument should use f_J (or the current estimate, smoothed) inside the linearised operator.
- **Also open:** whether the pointwise near-source loss is sharp.

=== END OF ANSWER round3_q2 ===
