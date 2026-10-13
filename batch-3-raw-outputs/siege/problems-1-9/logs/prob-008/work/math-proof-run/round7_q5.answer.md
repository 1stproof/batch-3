# round7_q5 — answer

## Plan
Target: Conjecture (C), the purely dynamical statement. I neither prove nor refute it. What I do prove is a reduction: (C) is at least as strong as a statement that, as far as I know, is open and quite different in kind.

**(DUE-0)** Every C^inf volume-preserving flow on a compact connected manifold whose only invariant distribution density is a multiple of the volume ("distributionally uniquely ergodic", DUE) has zero topological entropy.

More generally, (C) implies that every flow satisfying the two weak conditions (K0) and (K1) below has zero entropy. Both are much weaker than GH. Consequences for strategy:
- (C) cannot be refuted without building a positive-entropy flow satisfying (K0) and (K1), for example a DUE positive-entropy volume flow.
- Proving (C) proves more than the problem asks.
- Any successful route has to use the part of GH that Theorem J ignores: closed range, i.e. the tame estimate.

---

## 1. Theorem J and the whole chain use only (K0) and (K1)

Define two conditions on a smooth vector field X (u ranges over distributions, i.e. generalized functions; Xu is the distributional derivative). Neither depends on any choice of density.
- **(K0)** If u is in D'(M) and Xu = 0, then u is constant.
- **(K1)** There is no u in D'(M) with Xu = 1.

GH implies both:
- (K0) is L1 of Text A.
- (K1): GH makes u smooth, and at a maximum point of u we get (Xu) = 0, not 1. This is the argument of (F2).

**Lemma 1.1 (checked).** Theorem J holds with GH replaced by (K0) ∧ (K1).
*Proof.* I re-read the proof of Theorem J (R6-a §2). GH enters only through (F1) and (F2).
- (F1): T(Pφ) = 0 for all φ implies T = cν. Its proof is "u = T/ν has Xu = 0, so u is constant": this is exactly (K0).
- (F2): T(Pφ) = c'∫φ dν implies c' = 0. Its proof is "u = T/ν has Xu = -c'": if c' ≠ 0 then u/(-c') solves Xw = 1, contradicting (K1).
Steps 1–3 and 5 (regularity in t, moments, integration by parts, Fourier uniqueness) use no hypothesis on X. ∎

**Lemma 1.2 (checked).** The following hold under (K0) ∧ (K1) for dim M ≥ 2, with the same proofs:
- P1: at a zero p, d(p) ≠ 0;
- Observation P: no periodic orbit with ∫_γ d = 0;
- Lemma K / K';
- Corollaries 4.1 and 4.2: no homoclinic point of a hyperbolic periodic orbit or zero;
- Theorem 5.1: every positive-entropy ergodic measure is non-hyperbolic. This one is modulo the cited Ruelle inequality and the Katok / Lian–Young horseshoe theorem.

For Lemma K' (applied to -X) note that (K0) and (K1) are invariant under X → -X: Xu = 1 becomes (-X)(-u) = 1.

*Proof.* Where each result uses GH:
- P1 and Observation P use only "Xu = 0 implies u constant", which is (K0). The distribution u there is μ_γ/ν' or δ_p/ν. It is not constant because it is supported on a ν-null set and is nonzero.
- Lemma K uses only Theorem J, which holds by Lemma 1.1.
- Corollaries 4.1 and 4.2 use Lemma K / K', P1, Observation P and the classical stable manifold theorem.
- Theorem 5.1 uses Corollary 4.2 together with the cited [Ru] and [KLY].
None of these uses closed range or the tame estimate. ∎

**Proposition 1.3 (proved, modulo the citations of Lemma 1.2 and the variational principle).** Assume (C) holds for every C^inf flow. Then every C^inf vector field X on a compact connected manifold that satisfies (K0) and (K1) generates a flow of zero topological entropy.

*Proof.*
1. If dim M = 1, every flow on a compact 1-manifold has zero entropy.
2. Let dim M ≥ 2. By the variational principle and the reduction to flow-ergodic measures (step 2 of the chain, checked in R6-a §5), it suffices to show h_μ(g_1) = 0 for every ergodic flow-invariant μ.
3. Suppose h_μ(g_1) > 0. By Lemma 1.2 (Theorem 5.1), μ is non-hyperbolic. Then the 0 exponent of g_1 has multiplicity ≥ 2: the flow direction contributes one (R5-d, as quoted in the brief) and there is at least one further zero exponent.
4. (C) gives a nonzero S with two-sided exponential decay.
5. Lemma 1.1 (Theorem J under (K0) ∧ (K1)) gives S = 0. This is a contradiction. ∎

**Corollary 1.4.** (C) implies (DUE-0).
*Proof.* Let ω be a smooth invariant volume and take ν = ω, so d = 0 and P = X.
- (K0) is DUE. If Xu = 0, then T = uω satisfies L_X T = (Xu)ω = 0, so T is invariant and hence T = cω, i.e. u = c. Conversely, DUE says exactly that every invariant distribution density is cω.
- (K1) is automatic. If Xu = 1, pairing with ω gives ⟨Xu, ω⟩ = -⟨u, L_X ω⟩ = 0. But ⟨1, ω⟩ = ω(M) > 0.
Proposition 1.3 then applies. ∎

**Remarks.**
- DUE means only that the transposed operator has dense range. GH means kernel = constants plus closed range.
- I know no proof of (DUE-0) and no reference for it, from memory. The DUE diffeomorphisms I recall (Avila–Fayad–Kocsard, built by approximation by conjugation) have zero entropy, but I know of no theorem saying DUE forces zero entropy.
- So proving (C) would in particular settle (DUE-0). That statement is stronger than the problem, and the problem's extra hypothesis (closed range) is not used.
- Conversely, refuting (C) requires a flow that has a non-hyperbolic positive-entropy ergodic measure but no S. Note that this does not need such a flow to satisfy (K0) or (K1). Still, by Proposition 1.3, the most natural source of counterexamples (flows where some (K0) ∧ (K1) mechanism forbids S) would be positive-entropy (K0) ∧ (K1) flows, and I cannot construct one.

## 2. Evidence for (C) in structured cases (sketch, not needed for the main point)

**Products.** Let X = X_1 + X_2 on M_1 × M_2. Suppose X_1 preserves a smooth probability m_1, and X_2 preserves a smooth volume ω_2 and is exponentially mixing for C^k observables (cited from memory: e.g. contact Anosov flows, Dolgopyat / Liverani). Let h be smooth with ∫h dω_2 = 0, h ≠ 0, and put S = m_1 ⊗ (hω_2). Take ν = m_1 ⊗ ω_2, so d = 0.
- Write Φ(y) = ∫φ(x, y) dm_1(x). Then S(φ∘g_t) = ∫ h · Φ∘g^2_t dω_2, by invariance of m_1.
- ||Φ||_{C^k} ≤ ||φ||_{C^k}, so (C) holds for every μ of positive entropy.
- Such flows carry non-hyperbolic positive-entropy measures, for instance m_1 ⊗ ω_2 when dim M_1 ≥ 1.

**Isometric skew products.** The same argument works for M = N × T^r and X = X_N + Σ a_i(y)∂_{θ_i}, with S = (hω_N) ⊗ Leb.

**General zero-center-exponent skew products.** Here one would use the holonomy-invariant disintegration of the invariance principle (Ledrappier, Avila–Viana; cited from memory). The construction needs Hölder dependence of the conditionals and exponential mixing for Hölder observables. I have not checked this.

In all these cases S comes from a smooth factor. General (C) has no factor, and this is exactly what is missing.

## 3. A GH-only spectral fact that DUE does not give (proved)

This records a consequence of the closed-range part of GH, which Section 1 shows must eventually be used.

**Proposition 3.1.** Assume GH and that X preserves a smooth probability ω. Let A be the self-adjoint generator of the unitary Koopman group U_t f = f∘g_t on L^2(ω), so that U_t = e^{itA} and X = iA on smooth functions. For f in L^2 let σ_f be its spectral measure. Then for every j there are m_j and C_j such that for every smooth f with ∫f dω = 0:
 σ_f({0}) = 0, and ∫ ξ^{-2j} dσ_f(ξ) ≤ C_j ||f||^2_{C^{m_j}}.

*Proof.*
1. By (O2), the invariant distribution densities are cω. Closed range (Corollary 3) and its duality consequence give f = Xu_1 with u_1 smooth, and we may take ∫u_1 dω = 0.
2. Lemma 2 (Text B) gives ||u_1||_{C^k} ≤ C||f||_{C^m}. Iterating gives smooth mean-zero u_j with X^j u_j = f and ||u_j||_{L^2} ≤ C_j ||f||_{C^{m_j}}.
3. Unique ergodicity (O2) gives ker A = constants. Since f ⊥ 1, σ_f({0}) = 0.
4. f = (iA)^j u_j gives dσ_f = ξ^{2j} dσ_{u_j}. Hence ∫ξ^{-2j} dσ_f = σ_{u_j}(R \ {0}) ≤ ||u_j||^2. ∎

So the spectral measures of smooth functions vanish to infinite order at 0, tamely in f. Theorem J is the analytic form of this statement for one fixed S: it kills all Taylor coefficients at 0 of the cross-spectral density, and then uses analyticity.

Positive entropy gives countable Lebesgue spectrum on the orthocomplement of the Pinsker factor. That alone gives no contradiction: smooth functions approximating a Lebesgue-spectrum vector in L^2 can have spectral measures vanishing to infinite order at 0, with constants that blow up.

A contradiction would need **tame** control on how smooth functions see the Lebesgue part near frequency 0. That is the same missing ingredient as the decay rate required by (C).

## 4. Status

**Proved.**
- Lemma 1.1, Lemma 1.2 and Proposition 1.3: Theorem J and the whole hyperbolic chain need only (K0) ∧ (K1). Hence (C) implies zero entropy for all (K0) ∧ (K1) flows, in particular (DUE-0) (Corollary 1.4).
- Proposition 3.1, a closed-range-specific spectral property.

**Sketched.** (C) holds for product and isometric-skew-product flows over exponentially mixing volume flows (Section 2).

**Not achieved.** Neither a proof nor a refutation of (C). The case μ(d) = 0, non-hyperbolic, positive entropy, remains exactly where R6 left it.

**Open questions, named explicitly.**
- (Q1) Is (DUE-0) true? I.e. does a C^inf volume-preserving flow whose only invariant distribution is the volume have zero entropy? (C) implies it.
- (Q2) More generally, do (K0) ∧ (K1) imply zero entropy?
- (Q3) Conjecture (C) itself.

**Recommendation for the chain.** If (Q1) is genuinely open, (C) is likely out of reach as a standalone statement. A more promising target for the problem would combine Theorem J–type objects with the tame closed-range estimate (Lemma 2, Proposition 3.1), which GH has and DUE lacks. Example: allow S to depend on t through X^{-1}-corrections, so that only "approximate" exponential decay modulo X(C^inf) is needed.

=== END OF ANSWER round7_q5 ===
