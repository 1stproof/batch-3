# round2_q2 — answer

**Status: NOT resolved.** I do not have a proof that H plus GH forces zero Lyapunov exponents. What follows is (1) a short, rigorous spectral reformulation of what H gives quantitatively, which I believe is new relative to the background, (2) a precisely stated missing lemma that would finish the proof, with a remark on why it is not obviously easier, and (3) a note on the literature, cited from memory.

## 1. Spectral estimate (proved)

Setting: omega is a smooth invariant probability volume. Then X is skew-symmetric on C^∞ ⊂ L²(omega), and its closure is skew-adjoint because the flow is unitary on L²(omega) (Stone's theorem). Write X = iA with A self-adjoint, and let P_ε = 1_{[-ε,ε]}(A) be the spectral projection.

**Proposition S.** There are m and C such that for every smooth f with ∫f omega = 0 and every ε > 0,
 ||P_ε f||_{L²} ≤ C ε ||f||_{C^m}.
Equivalently, the spectral measure σ_f satisfies σ_f([-ε,ε]) ≤ C² ε² ||f||²_{C^m}, and ∫ s^{-2} dσ_f(s) ≤ C²||f||²_{C^m}.

*Proof.*
1. By H (or by O2 together with Text B, Lemma 2 with ν = omega and k = 0), f = Xu, where u is smooth with mean zero and ||u||_{C^0} ≤ C||f||_{C^m}. Hence ||u||_{L²} ≤ C||f||_{C^m}.
2. Then P_ε f = i P_ε A u = i (A P_ε) u. Since ||A P_ε|| ≤ ε, we get ||P_ε f|| ≤ ε||u||.
3. For the second form: σ_f = s² σ_u, so ∫ s^{-2} dσ_f = ||u||². ∎

**Consequences.**
- The spectral measure of every smooth mean-zero f vanishes to second order at 0, uniformly in the C^m norm.
- In particular, the Green–Kubo variance of every smooth mean-zero f is 0. Equivalently, the ergodic integrals ∫_0^T f∘g_t are uniformly bounded (by 2C||f||_{C^m}), so no smooth observable satisfies a CLT with nondegenerate variance.

## 2. Missing lemma (open)

**(M)** Let g_t be a C^∞ flow that preserves a smooth volume omega, with h_omega(g_1) > 0. Then for every m there are smooth mean-zero f_n and ε_n → 0 such that
 ||P_{ε_n} f_n|| / (ε_n ||f_n||_{C^m}) → ∞.

(M) together with Proposition S contradicts H. Then Pesin's formula and the variational principle (the reduction in the earlier partial result) give h_top = 0.

**Why (M) is plausible.** By Rokhlin–Sinai, positive entropy gives countable Lebesgue spectrum on the orthocomplement of L²(Pinsker) (cited from memory). So there is F ∈ L² with σ_F equal to Lebesgue measure near 0, and hence ||P_ε F||² ≈ 2ε, which is much larger than ε².

**Why (M) is not proved.** Smooth f_n → F in L² need not inherit this: ||P_ε f_n|| can be as small as about ε·||f_n||_{C^m}, because the C^m norms blow up. One would need to approximate F by smooth functions whose C^m norm grows slower than ε^{-1/2} at the scale where ||P_ε(F − f_n)|| is small. This is a quantitative "smooth observables see the Lebesgue spectrum" statement, and it is exactly where the hard dynamics enters.

**The tame estimate alone cannot settle it (consistent with D1).** For Anosov flows, generic smooth f has positive Green–Kubo variance, so (M) holds there trivially. But that proof uses the hyperbolic structure (CLT for smooth observables), which is not available here. A plausible route is a CLT, or merely positive variance for a single smooth observable, for nonuniformly hyperbolic smooth-volume flows with positive entropy. Such a result is known in special cases (e.g. Young towers) but not, to my knowledge, in general.

## 3. Literature remarks (from memory, unverified)

- The statement "GH implies zero entropy" is connected to the Greenfield–Wallach and Katok conjectures. Forni (around 2008) studied GH and cohomology-free vector fields.
- Kocsard (2009) proved the Katok conjecture in dimension 3. Rodriguez Hertz–Rodriguez Hertz have related work.
- I do not recall a general proof of zero entropy for GH flows in arbitrary dimension, and I do not claim one.

## Summary

- **Proved:** Proposition S (spectral vanishing at 0 for smooth observables, with tame constants), and zero asymptotic variance for all smooth observables.
- **Open:** Lemma (M). Equivalently, whether a positive-entropy smooth-volume flow must have a smooth observable with nontrivial spectral mass near 0 that is not controlled by ε·||f||_{C^m}. The full zero-entropy claim, including when there are zero transverse exponents, remains open here.

=== END OF ANSWER round2_q2 ===
