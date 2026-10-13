# Answer to round2_q1: does GH force a smooth invariant volume, (V)?

**Status: (V) is NOT proved here. It remains OPEN in this work.** Below are one proved partial result, a sketched partial result, and a precise statement of the gap.

Convention (Text B): ν is a smooth positive density, d = div_ν X, and a distribution u corresponds to the density uν. Then L_X(uν) = (Xu + d u)ν, so Xu = (L_X(uν))/ν − d u.

## P1 (proved). If X(p) = 0, then d(p) ≠ 0.
*Proof.* Let u be the distribution with uν = δ_p, i.e. ⟨u, φν⟩ = φ(p). For a test function φ, ⟨L_X δ_p, φ⟩ = −⟨δ_p, Xφ⟩ = −(Xφ)(p) = 0, because X(p) = 0. So L_X(uν) = 0, and therefore Xu = −d u = −d(p) u. (The product d·δ_p equals d(p)δ_p.) If d(p) = 0, then Xu = 0 with u not smooth. This contradicts GH (equivalently L1). ∎

The conclusion of P1 does not depend on the choice of ν. If ν' = e^{a}ν, then div_{ν'} X = d + Xa, and Xa(p) = 0 at a zero p.

## P2 (sketch, not fully verified). At a zero p, no integer combination of the eigenvalues of DX(p) of the form d(p) + Σ α_i λ_i (with α a multi-index) may vanish.
*Sketch.* Let V_N be the space of distributions supported at p of order ≤ N. Then L_X preserves V_N, and so does the operator u ↦ Xu in the ν-identification, because X(p) = 0. If this finite-dimensional operator has a kernel, GH fails exactly as in P1. Computing the spectrum of this operator through the triangular filtration by order: its eigenvalues should be −(d(p) + Σ α_i λ_i), where the λ_i are the eigenvalues of DX(p). I have not checked the signs or the convention in detail. This step excludes some zeros, but not all of them (for example, hyperbolic sinks with generic eigenvalues are not excluded). Earlier notes handle linear sources and sinks with degree-0 homogeneous invariant functions; I have not re-verified that argument here.

## Gap (open)
1. Show that the space I of X-invariant distribution densities is one-dimensional and spanned by a smooth positive density. Equivalently, show d ∈ ℝ + X(C^∞) (O3).
2. Even the weaker claims are not proved here: unique ergodicity, absence of all zeros, and absence of periodic orbits.

From memory, and uncertain: Forni (2008) is recalled to prove that GH vector fields admit a smooth invariant volume and are uniquely ergodic (hence cohomology-free). I could not reconstruct the argument, so it is not used here.

Neither the duality (O1) nor the a priori estimates alone gives dim I = 1. They identify X(C^∞) with the annihilator of I, but they do not bound its codimension.

=== END OF ANSWER round2_q1 ===
