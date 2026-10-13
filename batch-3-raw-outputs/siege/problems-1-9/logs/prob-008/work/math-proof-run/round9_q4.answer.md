# round9_q4: attempt to refute (EF)

## Plan
1. Look for a counterexample: a GH field outside the Diophantine class, or a structural reason why (EF) is too strong.
2. Failing that, record why each counterexample template fails, and prove whatever parts of (EF) can be proved.

## Summary of outcome
- **(EF) is neither refuted nor proved.**
- **Any refutation must disprove the Katok / Greenfield-Wallach conjecture.** A refutation needs a GH field that is not smoothly conjugate to a Diophantine linear flow. Section 4 explains why none of the standard templates gives one.
- **No contradiction can be derived from (EF).** It is a statement only about GH fields. The only GH fields known (Diophantine flows and their smooth conjugates, including time changes) satisfy it.
- **Proved here (Section 1):** (EF) is a statement about a bounded band of Re z only. Outside that band the eigen-densities vanish with no GH used. By the identity theorem, the whole content of (EF) is "the family vanishes on some open set".
- **Sketched (Section 3):** the Paley-Wiener form of (EF), as a two-sided "gap" statement about transported distributions. This is presumably entry 83 again.
- **Isolated in Section 2:** the precise point where mechanism (B) of the planner and an analytic-Fredholm approach both fail. It is the derivative loss of the tame inverse R of X.
- I do not think the chain (steps 1-3) is flawed; I have no objection to Theorem R or step 1. Section 4, item T6, gives a plausibility check of Theorem R on Anosov flows.

Notation as in the brief: L_t phi := e^{J_t} (phi o g_t), so d/dt L_t phi = L_t P phi = P L_t phi.

## 1. Rigorous facts about families as in (EF)

**Lemma 1.1 (no GH, no holomorphy).** Let T be a continuous linear functional on C^1(M) with T(P phi) = z T(phi) for all smooth phi. Then T(L_t phi) = e^{zt} T(phi) for all smooth phi and all real t.

*Proof.*
1. The map (t,x) -> L_t phi(x) is smooth, so t -> L_t phi is C^1 as a curve in C^1(M), with derivative P L_t phi.
2. Hence f(t) = T(L_t phi) is differentiable, with f'(t) = T(P L_t phi) = z f(t), using (iii) for the smooth function L_t phi.
3. Therefore f(t) = e^{zt} f(0). ∎

**Lemma 1.2 (outer bands vanish; no GH).** Define
- Λ_+ := limsup_{t→+∞} (1/t) log ||L_t||_{C^1→C^1},
- Λ_- := limsup_{t→+∞} (1/t) log ||L_{-t}||_{C^1→C^1}.

Both are finite: ||L_t||_{C^1→C^1} ≤ C e^{K|t|}, with K depending on ||d||_{C^1} and sup||DX||. If T is as in Lemma 1.1 and Re z > Λ_+ or Re z < -Λ_-, then T = 0.

*Proof.*
1. By Lemma 1.1, |T(phi)| = e^{-Re z · t} |T(L_t phi)| ≤ ||T|| e^{-Re z · t} ||L_t|| ||phi||_{C^1}.
2. If Re z > Λ_+, let t → +∞: the right-hand side tends to 0.
3. The other case is symmetric, letting t → -∞.
4. So T vanishes on C^∞. By density of C^∞ in C^1 and continuity, T = 0 on C^1. ∎

**Corollary 1.3 (reduction to an open set).** Let (T_z) satisfy (i) on a strip Ω. If T_z = 0 for all z in some nonempty open subset of Ω, then T_z = 0 on all of Ω.

*Proof.* For each smooth phi, z -> T_z(phi) is holomorphic on the connected set Ω, so the identity theorem applies. Since each T_z is continuous on C^1, density extends the conclusion to C^1. ∎

Consequently (EF) is equivalent to the following: for every GH field, every family as in (EF) vanishes on some open set. Lemma 1.2 gives this whenever Ω meets {Re z > Λ_+} ∪ {Re z < -Λ_-}. The strips produced by Theorem R lie inside (λ, λ+θ) with θ < χ^+_min. These are always inside the band [-Λ_-, Λ_+], where Lemma 1.2 says nothing. So Lemma 1.2 cannot be used directly. Any proof of (EF) needs one of two things:
- an analytic continuation of the family across the band, which nothing in the hypotheses provides; or
- a GH argument at some z with Re z ≠ 0.

**Lemma 1.4 (smooth eigenfunctions; no GH).** Let b be smooth with Xb = -z b and Re z ≠ 0. Then b = 0.

*Proof.*
1. X|b|^2 = -2 Re z |b|^2.
2. At a maximum point of |b|^2 the left-hand side vanishes, so max |b|^2 = 0. ∎

This is the analogue, at Re z ≠ 0, of the planner's Remark 3.3 (which I have not checked and do not rely on). Under GH it is all that can be said about smooth eigenfunctions. The eigen-equation (X + z)u_z = 0 has a non-smooth right-hand side after any rearrangement, so GH of X never applies to it directly.

## 2. Mechanisms tried and where they fail

### 2.1 Mechanism (B) (Leibniz), written out

The tame inverse here is R := X^{-1}: X(C^∞) → C^∞_0, a continuous map by Text B, Corollary 3. Take χ in X(C^∞), so that Rχ is defined and smooth; for a ν-mean-zero χ this needs χ in X(C^∞).

1. Applying (iii) to Rχ: T_z(χ) = T_z(X Rχ) = T_z(P Rχ) - T_z(d Rχ) = T_z((z - d) Rχ).
2. So T_z is a fixed vector of the transpose of K_z := (z - d)R, restricted to X(C^∞). The family K_z is affine in z.
3. If R extended to a **compact** operator on some Banach space B ⊃ C^∞ with T_z in B', the analytic Fredholm alternative would apply: the set of z where 1 is in the spectrum of K_z is either discrete or all of C.
   - "Discrete" contradicts a nonzero holomorphic family on an open set.
   - "All of C" contradicts Lemma 1.2 at large Re z, provided the B'-eigenvectors are of order ≤ 1.
4. This is exactly where it fails. Under GH, R is only tame: it maps C^m to C^k with m = m(k) > k. It is not compact, and not even bounded, on any fixed C^k or H^s. Diophantine flows show that the loss of derivatives is real.

The general Leibniz identity, with V_z := T_z(phi ·), is V_z(Xψ) = z V_z(ψ) - T_z((P phi)ψ). Every choice of phi leads back to the same affine fixed-point problem with the same R. Choosing phi so that P phi is small (approximately invariant densities) only moves the error term; it does not remove the loss of derivatives.

### 2.2 The volume case does not become easy

Suppose X also preserves a smooth volume (d = 0).
- T_z(1) = 0 for z ≠ 0, and the identity reduces to T_z o R = z^{-1} T_z on X(C^∞).
- Iterating gives |T_z(ψ)| ≤ |z|^n C_z C_n ||ψ||_{C^{m_n}}, with uncontrolled constants C_n and orders m_n. This gives no conclusion; it is the gap (E1) of R4-q10.
- X is skew-adjoint on L^2(ν), so P^T has no L^2 eigenvectors off iR. But T_z is only in (C^1)'. I found no way to use GH to upgrade an order-1 eigen-density to L^2: smoothing along the flow does not regularise in the transverse directions.

### 2.3 Tensor products

T_z ⊗ T_w is an eigen-density for X⊕X (or X⊕(-X)) on M×M. These product fields are never GH: in the Diophantine case the frequency vector (α, α) is resonant. So no GH leverage is gained.

## 3. Paley-Wiener form of (EF) (sketch)

Assume (i)-(iii) with the bounds of (ii) uniform in Im z.

1. For smooth phi and c in (a,b), y -> T_{c+iy}(phi) is bounded.
2. By the Paley-Wiener theorem for two-sided Laplace transforms, there is a distribution Σ_phi in t such that:
   - e^{-ct} Σ_phi is tempered for every c in (a,b), and T_z(phi) = <Σ_phi, e^{-zt}>;
   - Lemma 1.1 gives Σ_{L_s phi} = Σ_phi(· + s).
3. Formally Σ_phi(t) = S(L_t phi) for the distribution S := "Σ_.(0)", made rigorous by pairing with test functions in t.
4. The growth conditions say:
   - S o L_t grows at most like e^{(a+ε)t} as t → +∞;
   - S o L_t decays at least like e^{-(b-ε)|t|} as t → -∞.
5. Equivalently, for every c in (a,b), the tilted transport e^{-ct} L_t, which is the transfer operator of P - c (weight d - c), makes S o L_t decay in both time directions.

So (EF) says: under GH, Theorem J holds simultaneously for all weights d - c with c in an open interval, not only for the weight d where (F1) and (K1) supply the Jordan-chain argument. The interval cannot be moved to contain 0:
- changing ν changes d to d + Xa;
- a constant time change rescales z;
- shifting d by a constant c would need Xw = c with w smooth, which (K1) forbids.

## 4. Counterexample templates and where each fails

- **T1. Diophantine linear flows on T^n, their smooth conjugates, and their time changes.** Time changes hX of Diophantine flows are smoothly conjugate to linear flows, by solving the cohomological equation; this is standard and cited from memory.
  - In Fourier terms (d = 0, P = X), T_z(e_k)(i k·α - z) = 0, so the eigenvalues lie in iR.
  - On a strip, each z -> T_z(e_k) is holomorphic and vanishes off a single point, so it vanishes identically.
  - (EF) holds; no counterexample here.
- **T2. Perturbations of T1.** GH is not an open condition. KAM-type rigidity (Herman's theory, cited from memory) returns the perturbations that remain GH to the conjugacy class of T1.
- **T3. Products and skew products.**
  - For a product X⊕Y, GH requires Y to be GH: apply it to 1⊗w with w a non-smooth distribution on the second factor. It also requires a joint Diophantine condition. So one is back in T1.
  - Skew products over Diophantine rotations whose fibre dynamics is non-trivial have non-smooth distributions annihilated by X (fibrewise invariant ones), so they violate L1.
- **T4. Parabolic flows** (horocycle flows, Heisenberg and other nilflows). These have non-smooth invariant distributions u with Xu = 0 (Flaminio-Forni, cited from memory), so they violate L1 and are not GH.
- **T5. Gradient-like flows and flows with zeros or non-dissipative closed orbits.**
  - Excluded by P1 and Lemma H (resonant zeros) and by Observation P (Jacobian-1 periodic orbits).
  - Excluded by B3 when an attractor has a basin of positive volume.
- **T6. Hyperbolic flows (Anosov, horseshoes).**
  - For these, families violating (EF) do exist. For example, mean-zero leaf measures on local strong-unstable disks, differentiated along the leaf, transported by L_t: their backward transport decays at the unstable rate, and their forward transport decays at the exponential mixing rate.
  - This is the mechanism behind Theorem R, and it shows that (EF) genuinely needs GH.
  - These flows are not GH (periodic orbits with homoclinic points are excluded by Lemma K of round 6).
- **T7. Abstract operators X + q** (GH by (O4) when q ∈ X(C^∞)). Their eigenvalue sets are lines Re z = const, never strips. The same holds for the non-vector-field operators X + c with c constant.

**Conclusion.** Every template is either within T1, where (EF) holds, or not GH. A refutation of (EF) would require a GH field outside T1, which would disprove the Katok / Greenfield-Wallach conjecture. I found none. A refutation of type (b), deriving a known falsehood from (EF), is impossible with current knowledge, because (EF) holds for every known GH field.

## 5. What remains open
- **(EF) itself.** The minimal missing ingredient is any GH-based vanishing statement for order-1 eigen-densities on an open set of z with Re z ≠ 0. By Corollary 1.3 this would suffice.
- **A sufficient conditional.** If the inverse R of X on X(C^∞) extended to a compact operator on a Banach space whose dual contains the T_z, then (EF) would follow by the analytic Fredholm argument of Section 2.1.
- **The volume case (statement (C), E1).** It remains open even with a smooth invariant volume.
- **The [GOAL].** It is not settled here.

=== END OF ANSWER round9_q4 ===
