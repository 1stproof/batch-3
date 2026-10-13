# round1_q1 — partial answer (the main claim is NOT proved here)

**Convention.** Fix a smooth positive density ν on M. A distribution is a continuous linear functional on smooth densities. Using ν, identify distributions u with functionals φ ↦ ⟨u, φν⟩ on C^∞(M). Then L_X u is defined by ⟨L_X u, ρ⟩ = −⟨u, L_X ρ⟩. Write d = div_ν X, so that L_X(φν) = (Xφ + dφ)ν. For smooth u, L_X u = Xu. The facts below do not depend on this choice of identification.

## Lemma 1 (invariant distributions). If u ∈ D'(M) and L_X u = 0, then u is constant.
*Proof.* By hypothesis (with f = 0), u is smooth and Xu = 0. Fix c ∈ ℝ. Take smooth functions h_n: ℝ → [0,1], all bounded by 1, converging pointwise to the indicator of (c, ∞). Then X(h_n∘u) = h_n'(u)·Xu = 0. Also h_n∘u converges to H := 1_{u>c} in L¹(ν), and so in D'. Since L_X is continuous on D', L_X H = 0. By hypothesis H is smooth. H takes only the values 0 and 1, and M is connected, so H is constant. This holds for every c, so u is constant. ∎

## Lemma 2 (a priori estimate; Peetre-type argument). For every k there are m and C such that ‖u‖_{C^k} ≤ C‖Xu‖_{C^m} for all u ∈ C^∞ with ∫u dν = 0.
*Proof.* Fix s > n/2 + 1. Let Y = {u ∈ H^{-s} : Xu ∈ C^∞}. Give Y the Fréchet topology defined by the seminorms ‖u‖_{-s} and ‖Xu‖_{C^j}, j ≥ 0. Y is complete, because X: H^{-s} → H^{-s-1} is continuous. By hypothesis Y ⊂ C^∞. The inclusion Y → C^∞ has closed graph, since both topologies are finer than D'. By the closed graph theorem for Fréchet spaces, the inclusion is continuous. So
(∗) ‖u‖_{C^k} ≤ C(‖u‖_{-s} + ‖Xu‖_{C^m}) for some m and C.

Suppose the estimate of the lemma fails. Then there are u_n with zero mean, ‖u_n‖_{C^k} = 1 and Xu_n → 0 in C^m. A bounded set in C^k is precompact in H^{-s} (Rellich), so a subsequence is Cauchy in H^{-s}. By (∗) that subsequence is Cauchy in C^k, so u_n → u in C^k. In the limit Xu = 0 in D', so u is constant by Lemma 1. Also u has mean 0, so u = 0. This contradicts ‖u‖_{C^k} = 1. ∎

## Corollary 3. X(C^∞) is closed in C^∞, and X: C^∞_0 → X(C^∞) is a topological isomorphism. Here C^∞_0 denotes the smooth functions with ν-mean zero.
*Proof.* Suppose Xu_n → f with u_n ∈ C^∞_0. By Lemma 2, (u_n) is Cauchy in every C^k, so u_n → u and Xu = f. ∎

## Reduction of the entropy claim (standard theorems, cited from memory)
Suppose h_top(g_1) > 0. By the variational principle there is an ergodic invariant probability measure μ with h_μ(g_1) > 0. By the Ruelle inequality, μ has a positive Lyapunov exponent. If μ is hyperbolic (all exponents nonzero except the flow direction), Katok's horseshoe theorem for C² flows gives hyperbolic horseshoes. Those carry uncountably many ergodic measures and periodic orbits γ. Each periodic orbit gives an invariant distribution, namely the orbit measure δ_γ.

To get a contradiction from this, one still needs to show that GH rules out (a) periodic orbits, or (b) more than one invariant measure. From Corollary 3, each invariant measure annihilates X(C^∞). However, GH alone does not obviously make the cokernel C^∞/X(C^∞) one-dimensional. That would need global hypoellipticity of the transpose X + d, which I have not derived.

## Gaps (open; not proved here)
- **Lemma A (missing).** GH ⇒ the only X-invariant distributions (T with T(Xφ) = 0 for all φ ∈ C^∞) are multiples of one smooth positive density. Consequences: X has no zeros, the flow is uniquely ergodic with a smooth invariant volume, and every zero-mean function is a smooth coboundary.
- **Lemma B (missing).** If a C^∞ flow preserves a smooth volume, is uniquely ergodic, and has positive entropy, then it violates GH. This covers the case where the volume has zero exponents transverse to the flow, where Katok's closing lemma is unavailable. I do not know a proof. The point flagged in the task, that minimal positive-entropy systems exist, shows that unique ergodicity alone cannot suffice; the tame cohomological estimate of Lemma 2 would have to be used.

**Status.** Lemmas 1 and 2 and Corollary 3 are proved. The headline claim remains open in this answer.

=== END OF ANSWER round1_q1 ===
