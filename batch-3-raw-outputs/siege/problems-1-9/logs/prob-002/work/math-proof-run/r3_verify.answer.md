# Verification of the draft proof (minimax rate for Darcy near f = 1)

## Verdict

**The main claim is proved, assuming the standard facts the draft cites.** The rate is
n^{-2α/(2α+d+3)} up to logarithmic factors, for small fixed r. Both halves hold:
- the lower bound holds for all r in (0,1);
- the upper bound holds for r ≤ r_0, with a (log n)^4 factor that is absent for non-integer α.

I re-derived every inequality listed below. I found no error that affects the conclusion. The defects are bookkeeping, wording, and reliance on cited facts. They are listed in order of severity after the step-by-step check. The cited facts are standard (Gilbarg–Trudinger L^p and H^2 theory, Gagliardo–Nirenberg, Assouad, Hestenes/Seeley extension, Zygmund–Schauder, Dudley, Borell–TIS). I checked each one from memory, and each is quoted in a form that is correct and adequate for its use.

## Step-by-step check

### Part I (lower bound)

- **Radial identity.** Let G = b(ρ)Ψ, where Ψ = ΔΦ_k is homogeneous of degree −2. Then x·∇G = ρb'Ψ − 2bΨ. Hence div(G x/d) = (x·∇G + dG)/d = ((ρb' + (d−2)b)/d)Ψ. This holds for every d, so the "checked symbolically in d = 2, 3" remark can be replaced by this one-line proof.
- **Integration by parts.** cψ is compactly supported in the annulus, where Φ_k is smooth. So ⟨cΔΦ_k, ψ⟩ = ∫Φ_kΔ(cψ), and this is at most ‖Φ_k‖_{L²(annulus)}·C‖ψ‖_{H²}. Since ‖Φ_k‖_{L²(annulus)} ≍ 2^{−j(d−1)/2} and ‖h_k‖_2 ≍ 2^{−jα}2^{−j(d−1)/2}, the bound C2^{−2j}‖h_k‖_2‖ψ‖_{H²} follows. Correct.
- **Drift term.**
  - ‖q‖_p ≲ 2^{−jα}, so ‖w‖_{W^{2,p}} ≲ 2^{−jα} by GT 9.15 and 9.17. Uniqueness of the H¹_0 solution identifies w with the W^{2,p} solution.
  - Duality gives ‖w‖_p ≲ 2^{−j(α+2)}. The identity ∫wφ = ∫wL_fψ = −∫qψ is legitimate because both functions vanish on ∂D.
  - In Gagliardo–Nirenberg, t = (1+d/p)/2 < 1 because p > d. The exponents combine as αt + (α+2)(1−t) = α + 1 − d/p.
  - Choosing d/p = min(α−1, 1/2) gives ‖W‖_∞ ≲ 2^{−2j}. This is where α > 1 is needed. Correct.
- **Membership in the class.** The bound |Δ_h^m(2^{−jα}G_θ)| ≤ C2^{−jα}min((2^j|h|)^m, 1) ≤ C|h|^α is correct, uniformly in θ and j.
- **Sizes, KL, Pinsker and Assouad.**
  - KL = (n/2)‖u_θ − u_θ'‖² ≲ n2^{−4j}2^{−j(2α+d−1)} = n2^{−j(2α+d+3)}.
  - The reduction to testing uses that f_θ − 1 = θ_kh_k on S_k, which holds because the supports are disjoint.
  - Assouad (Tsybakov Thm 2.12) then gives a lower bound of order M·min_k‖h_k‖² ≍ 2^{−2jα} ≍ n^{−2α/(2α+d+3)}. Correct.
- **Why this construction is the right one.** I also checked anisotropic variants: angular frequency 2^j and radial frequency 2^{j'}. These give KL ≍ n2^{j'}2^{−j(2α+d+3)} with the same loss 2^{−2jα}, so j' = 0 is optimal. This is consistent with the draft's "other constructions" remark.

### Part II (upper bound)

- **(C4).** The Neumann series in C^{α+1}, together with the product estimate in C^α, is correct. It gives ‖∇u_f − x/d‖_{C^1} ≤ Cr; this is where small r enters.
- **Lemma 1.1** (Littlewood–Paley sum) and **Lemma 1.** Correct. The β-Hölder argument works because DV^E ∈ C^{α−1}.
- **Lemma 2.**
  - Item 1: the contraction constant is dε ≤ 1/8, and B(0, dε) ⊂ D.
  - Items 3–6: correct as written.
  - The exponent β = d(1−dε)/(1+dε) ≥ 14/9 > 1. Correct.
- **Lemma 3.**
  - (a) and (a′): verified by differentiating (SG). Correct.
  - (b): ∫e^{−7s/8}ds = 8/7. Correct.
  - (c): γ·X ≥ |γ|(|γ|/d − ε) ≥ 3/(16d) when |γ| ≥ 1/2. The time needed to cross the layer is ≤ 16dδ/3 ≤ 6dδ. Correct.
- **Lemma 3.1, (d), (e).** The Duhamel bound ∫e^{−a(s−σ)}e^{−2aσ}dσ ≤ e^{−as}/a is correct.
- **f_0 bounds.** These require 2(2−α)_+ ≤ (3−α)_+ for α ≥ 1, which holds. Correct.
- **Identity (★).** Re-derived: T_{V̂}(f̂ − f_0 + Z) = div(Z∇ξ), then uniqueness (a) applies. Correct.
- **Bias.**
  - Commutator identity: re-derived, including the sign of R.
  - Term div(gV): T_{V_J}^{−1}T_{V_J}g = g by (a). This exact inversion is the key point; it avoids the naive 2^{−J(α−1)}.
  - Term div R: products Δ_hA·Δ_hB with (a, b) = (α−1, α). Polynomial parts have degree in [2, 2α−1) and are killed by the vanishing moments. Remainders are O(|h|^α L²), including the case a < 1 where P_A is empty.
  - Term k_J*G: it is O(2^{−J(α−1)}) and supported in a layer of width O(2^{−J}); Lemma 3(c) then gives 2^{−Jα}.
  - Total bias ≲ J²2^{−Jα}. Correct.
- **Variance.**
  - Kernel bound: |𝒟_y k_J| ≲ 2^{J(d+2)}1{|y−z| ≤ δ}, since ‖∇f_0‖ ≲ J2^{J(2−α)_+} ≲ 2^J for α > 1.
  - The Fubini step and the change of variables (M) are correct.
  - Small-ball mass: for ρ(y) ≥ 4δ, r' ranges over [ρ/2, 3ρ/2].
  - Integration: ∫m dμ_x ≲ min(1, δ/ρ_x), so ‖h_x‖² ≲ 2^{J(d+3)}/|x − x_J|. This is integrable for d ≥ 2, giving E‖Z‖² ≲ n^{−1}2^{J(d+3)} ≤ C2^{−2Jα}. Correct.
- **Noise levels.** n^{−1/2}2^{J(d/2+m)} ≤ 2^{−J(α+3/2−m)}. This gives the exponents α + 1/2, α − 1/2 and α − 3/2 for m = 1, 2, 3. Correct.
- **Remainder.** It is ≲ J^4 2^{−J(2α−1)} = o(2^{−Jα}) because α > 1. Correct.
- **Cross-term exponents.** The draft needs (2−α)_+ ≤ 1 and (3−α)_+ ≤ 2; both hold for α ≥ 1.
- **Dudley, Borell–TIS, and P(A^c) ≤ Ce^{−cJ²}.** Correct. ξ does not depend on f.
- **Assembly.**
  - On A^c, clipping gives |f̃ − f| ≤ 2r.
  - The final bound is J^4 2^{−2Jα} ≍ (log n)^4 n^{−2α/(2α+d+3)}.
  - For non-integer α, no log factor enters the bias or the variance. The J factors from the event A and from the f_0 bounds appear only in absorbed terms. So the claim of a log-free bound for non-integer α holds.

## Errors and gaps, in order of severity

None of these invalidates the theorem.

1. **Dependence on cited facts.** The only substantive caveat. The following are quoted, not proved:
   - Zygmund–Schauder for the Dirichlet Laplacian at integer α (S);
   - boundedness of a finite-reflection (Hestenes-type) extension on B^s_{∞∞} up to order S_0, in the radial form (C1). This needs λ_iη < 1, and boundedness at integer s follows by interpolation;
   - uniformity of the GT constants over the class;
   - the Zygmund Taylor formula with a log factor at integer order (C3).

   All are standard and correctly stated as far as I can verify from memory. The proof is complete relative to them.
2. **J-power bookkeeping in II.7.** ‖G_ξ‖_∞ ≤ CJ²2^{−J(α−1/2)}, not CJ. The term ∇f_0·∇ξ contributes J·J. Consequently:
   - ‖Z‖_∞ gets J²;
   - the remainder bound becomes C J^4 2^{−J(2α−1)} (unchanged power J^4, from ‖∇Z‖‖∇ξ‖);
   - the product ‖Z‖‖Δξ‖ is J³2^{−J(2α−1)}.

   This is harmless, since all of these terms are o(2^{−Jα}).
3. **Radial identity.** It is described as "checked symbolically in d = 2, 3", but it is used for all d. The general proof is one line and is given above, so this is not a real gap.
4. **Wording in II.1.** It says the event A is unobservable "since ξ depends on the unknown u". In fact ξ = n^{−1/2}K_J𝕎 does not depend on u. A is unobservable because ξ = K_JY − K_Ju and u is unknown. This affects nothing.
5. **Heuristic Fourier symbol.** The symbol (1+|ξ_rad|)/|ξ|² is only motivation and is not used in the proof. The draft says so itself.

## What remains open (as the draft itself states)

- Whether the (log n)^4 factor for integer α is removable.
- The rate when r is not small. The upper-bound argument needs a single critical point of ∇u_f and the Neumann-series proof of (C4); the lower bound holds for all r.

## Conclusion

The minimax rate, up to log factors and for small fixed r, is

**n^{−2α/(2α+d+3)}.**

The draft proves this, relative to the standard facts it cites.

=== END OF ANSWER r3_verify ===
