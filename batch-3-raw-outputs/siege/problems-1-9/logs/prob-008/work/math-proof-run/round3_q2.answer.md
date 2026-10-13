# round3_q2: attempt on (V) — I did not settle it

Plan: reduce (V) to a statement about the dimension of I, prove that reduction rigorously, and record exactly where the gap is.

Notation is as in the brief. I is the space of X-invariant distribution densities. By Text A, X(C^∞) = I^⊥, and X(C^∞) is closed.

## Lemma A (proved). (V) holds if and only if dim I = 1.
Proof.
(⇐) Krylov–Bogolyubov gives an invariant probability measure μ, and μ ∈ I. So I = Rμ. Let c = μ(d)/μ(1). Then d − c is annihilated by I. By Text A, d − c = Xa with a smooth. By (O3), e^{-a}ν is a smooth positive invariant density, and c = 0.
(⇒) Let ω be a smooth invariant density, normalised to ω(M) = 1. Take T ∈ I and write T = vω with v ∈ D'. Since div_ω X = 0, we get L_X T = (Xv)ω, so Xv = 0 in D'. By L1, v is constant. ∎

So (V) is equivalent to: **every X-invariant distribution density is a constant multiple of one invariant probability measure.** In particular, (V) implies unique ergodicity.

## Lemma B (proved). If μ ∈ I is a measure with μ = ρν for some ρ ∈ L¹(ν) with log ρ ∈ L¹(ν), then (V) holds.
This is planner observation (N3). I checked it: the invariance of ρν means L_X(ρν) = 0, i.e. Xρ + dρ = 0 in D'. Formally, a = log ρ satisfies Xa = −d. Rigorously, J_t is the log-Jacobian, and invariance gives ρ∘g_t · e^{J_t} = ρ a.e. Hence a∘g_t − a = −J_t = −∫_0^t d∘g_s ds a.e. Pairing with test densities and differentiating at t = 0 gives Xa = −d in D'. Then GH makes a smooth, and e^{a}ν is the smooth invariant volume. ∎
So (V) also follows from the existence of one absolutely continuous invariant measure whose density is log-integrable.

## Where the attempts stop
(a) Microlocal route. For T = vν ∈ I we have (X + d)v = 0. The operator P = X + d has real principal symbol iξ(X), and Hörmander's propagation theorem makes WF(v) invariant under the lifted flow in Σ. To transfer this to X one would need an order-0 pseudodifferential operator A with Xu ∈ C^∞ for u = Av. This needs [X, A]v − A(dv) ∈ C^∞, i.e. a symbol a with H_p a = d·a near WF(v), together with control at infinity. Solving H_p a = d·a along the lifted flow requires the Jacobian cocycle ∫ d along orbits to be bounded. That is exactly (V) again, so the argument is circular. I could not break the circularity.

(b) Finite-dimensionality of I would not suffice anyway. Lemma A needs dim I = 1, and I see no argument from the closed-range and a priori estimates (Text A/B) that bounds dim C^∞/X(C^∞).

(c) I could not exclude zeros of X beyond P1 (which gives d(p) ≠ 0), nor dissipative periodic orbits beyond R-b.

From memory, and not verified: the literature on the Greenfield–Wallach and Katok conjectures (Forni; Kocsard; Hurder; Chen–Chi) treats "GH ⟹ cohomological rigidity / smooth invariant volume" as nontrivial. As far as I recall it is settled only in low dimensions (dimension 3 via Forni and Kocsard, with some extra input). So (V) in general may well be open.

## Summary
- **Proved:** (V) ⇔ dim I = 1 ⇔ uniqueness of the invariant distribution density. Also proved: (V) follows from the existence of an absolutely continuous invariant measure with log-integrable density.
- **Open:** (V) itself, and the uniqueness of invariant distributions (or even of invariant measures) under GH.
- **Consequence for the problem:** the zero-entropy problem additionally needs lemma (M) of R-d, even assuming (V).

=== END OF ANSWER round3_q2 ===
