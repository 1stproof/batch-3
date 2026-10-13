# round6_q8: Patterson constructions along unstable manifolds, and what they can give toward (PE)

## Summary of outcome
(PE) is **not** proved here. What I do prove is that the suggested construction, and in fact every construction of its type, reduces to one support condition and nothing more. This is where the construction stops.

The type: push a finite positive measure m forward with the Jacobian weights e^{J_t}, then Abel/Patterson-normalise. Any such procedure produces a positive measure T with T(Xφ + dφ) = δ_m T(φ), carried by the ω-limit set ω(supp m), where δ_m is the critical exponent. (Proposition 3.)

GH, through L1, rules out such a T only when δ_m = 0 and ω(supp m) ≠ M (Corollary 4). Every other outcome is consistent with everything known. Positive eigen-measures with δ ≠ 0 exist under no constraint beyond δ ∈ [min μ(d), max μ(d)] (Lemma 1 and [R4-q7] Prop 2.2). So (E1) for positive measures says nothing new.

The weights cannot be changed to get around this. With other weights (unstable Jacobian, u-volume), L1 applies only when the weight cocycle is smoothly cohomologous to d + const (Lemma 2). For the unstable Jacobian that would essentially mean (V).

In the residual configuration (H3) (a uniformly volume-contracting horseshoe Λ), every m whose forward orbits accumulate only on Λ has δ_m ≤ −a < 0 (Corollary 5). Unstable discs of Λ or of a Pesin measure have uncontrolled ω-limit sets and uncontrolled δ_m.

So the construction proves (PE) only under an extra input that I cannot supply:

**(Q)** If h_top > 0, there is a finite positive m with δ_m = 0 and ω(supp m) ≠ M (or the same for −X).

Conventions are those of the brief: ν is a smooth positive density, d = div_ν X, and J_t(x) = ∫_0^t d(g_s x) ds. P denotes the operator Pφ = Xφ + dφ on functions. Q_t φ := e^{J_t}·(φ∘g_t).

---

## Lemma 0 (semigroup; no GH)
Q_{t+s} = Q_t Q_s. Also d/dt Q_tφ = Q_t Pφ = P Q_tφ for smooth φ, and the difference quotients converge uniformly.

*Proof.* We have Q_tQ_sφ = e^{J_t}·e^{J_s∘g_t}·φ∘g_{s+t} = e^{J_{t+s}}φ∘g_{t+s}, by the cocycle rule. Next, d/dt[e^{J_t(x)}φ(g_t x)] = e^{J_t(x)}(dφ + Xφ)(g_t x) = Q_t(Pφ)(x). Uniformity holds because (t, x) ↦ Q_tφ(x) is smooth on compact sets. Finally, d/ds|_{s=0} Q_sQ_tφ = P(Q_tφ) gives the second identity. ∎

## Lemma 1 (positive eigen-measures: where their eigenvalues can lie; no GH)
Let T ≠ 0 be a finite positive Borel measure with T(Pφ) = κT(φ) for all smooth φ, where κ is real. Then:

(a) T(Q_tφ) = e^{κt}T(φ) for all t and all continuous φ.

(b) K := supp T is a closed invariant set.

(c) κ ∈ [min_μ μ(d), max_μ μ(d)], where μ ranges over invariant probabilities carried by K.

Under GH, κ = 0 forces T = cν (Observation 0 and L1), and hence K = M.

*Proof.*
(a) Put f(t) = T(Q_tφ). By Lemma 0 and dominated convergence, f'(t) = T(PQ_tφ) = κ f(t). So f(t) = e^{κt}f(0) for smooth φ. Both sides are measures in φ, so the identity extends to continuous φ.

(b) Let φ ≥ 0 be continuous with φ = 0 on K. By (a), T(e^{J_t}·φ∘g_t) = 0. So φ∘g_t = 0 T-a.e., and hence on K by continuity. This holds for every such φ, so g_t K ⊂ K for all real t.

(c) Take φ = 1 in (a): T(e^{J_t}) = e^{κt}T(1). Since T ≥ 0 and T is carried by K, this gives min_K J_t ≤ κt ≤ max_K J_t. Divide by t > 0 and let t → ∞. On the compact invariant set K, the standard fact used in [R4-q7] Prop 2.1 step 1 (weak* limits of empirical measures) gives lim sup_t max_K J_t/t = max_{μ on K} μ(d) and lim inf_t min_K J_t/t = min_{μ on K} μ(d). ∎

Remark. Every value κ = μ(d), for μ ergodic, is realised by a positive T carried by supp μ ([R4-q7] Prop 2.2). Combined with Lemma 1, this gives: a nonzero positive eigen-measure with κ ≠ 0 exists if and only if some invariant μ has μ(d) ≠ 0. The "if" direction is Prop 2.2. For "only if": if all μ(d) = 0, then (c) forces κ = 0.

Consequently, under GH, "E1 for positive measures" is equivalent to "μ(d) = 0 for all invariant μ". By Corollary D1 the latter forces every ergodic measure to have full support, hence minimality. That is at least as hard as the goal ([R5-h]). So no contradiction can come from the eigenvalue alone. Only κ = 0 bites, through L1.

## Lemma 2 (which weights L1 can see; no GH for the computation)
Let a be continuous, let A_t = ∫_0^t a∘g_s be the corresponding cocycle, and let T be a positive measure with T(Xφ + aφ) = κT(φ) for all smooth φ. (This is exactly what Patterson averages with weights e^{A_t} produce; see Proposition 3, whose proof works verbatim with d replaced by a.)

(i) If a = d + Xb − κ with b smooth, then T' := e^{−b}T satisfies T'(Pψ) = 0. So under GH, T = c·e^{b}ν.

(ii) In general u = T/ν satisfies Xu = −(d − a + κ)u. L1 says nothing about this equation unless the multiplier d − a + κ vanishes after the conjugation in (i).

*Proof of (i).* Put φ = e^{−b}ψ. Then Xφ = e^{−b}(Xψ − ψXb). So Xφ + aφ − κφ = e^{−b}(Xψ + dψ). The hypothesis then says T(e^{−b}Pψ) = 0. Conclude by Observation 0 and L1.

(ii) is the computation ⟨Xu, φν⟩ = −T(Xφ + dφ) = −T(Xφ + aφ) − T((d − a)φ) = −κT(φ) − T((d − a)φ). ∎

Consequence for the brief's options.
- Normalising with the unstable Jacobian or the u-volume of g_tD gives a = (unstable expansion rate). The limits are then u-Gibbs-type invariant measures (κ = 0, a ≈ log-unstable-Jacobian rate), and L1 sees them only if that cocycle is smoothly cohomologous to d + const.
- With a = 0 (invariant measures), (i) requires d ∈ R + X(C^∞), which is (V) by (O3).

So the only weights GH can act on are e^{J_t}, up to smooth coboundaries and constants. That is the choice analysed below.

## Proposition 3 (Patterson output for an arbitrary initial measure; no GH)
Let m be a finite positive Borel measure, m ≠ 0. Put F(t) = ∫ e^{J_t} dm for t ≥ 0, and δ = δ_m := lim sup_{t→∞} (1/t) log F(t). Note |δ| ≤ ‖d‖_∞, since |F'| ≤ ‖d‖_∞ F. Let

ω(m) := ∩_{r≥0} closure(∪_{t≥r} g_t(supp m)),

which is a nonempty compact invariant set. Then there is a Borel probability T carried by ω(m) with T(Pφ) = δT(φ) for all smooth φ. Consequently, by Lemma 1(c), δ_m ∈ [min, max] of μ(d) over invariant μ on ω(m).

*Proof.*
1. Put T_t(φ) = ∫ Q_tφ dm. By Lemma 0, d/dt T_t(φ) = T_t(Pφ), and T_t(1) = F(t).
2. **Divergent case:** ∫_0^∞ e^{−δt}F(t) dt = ∞. For s > δ put T^s = ∫_0^∞ e^{−st}T_t dt. This is finite, since ∫e^{−st}F < ∞ for s > δ. Also e^{−st}F(t) → 0: its logarithmic derivative is bounded, so the argument of Lemma C applies.
   Integrating by parts gives T^s(Pφ) = sT^s(φ) − m(φ). Put S_s = T^s/T^s(1). Then |S_s(Pφ) − sS_s(φ)| ≤ ‖φ‖_∞ m(M)/T^s(1), which tends to 0 as s ↓ δ by monotone convergence. Any weak* limit T satisfies T(Pφ) = δT(φ).
   Support: let φ vanish on a neighbourhood of closure(∪_{t≥r} g_t supp m). Then only times t < r contribute to T^s(φ), so |S_s(φ)| ≤ ‖φ‖_∞ ∫_0^r F / T^s(1) → 0. Hence T is carried by every such closure, and so by ω(m).
3. **Convergent case:** ∫_0^∞ e^{−δt}F(t) dt < ∞. Use Patterson's slowly-varying-weight trick (Patterson 1976; cited from memory, standard). There is a nondecreasing C^1 function h ≥ 1 with h'/h → 0 at ∞ and ∫ h(t)e^{−δt}F(t) dt = ∞, while ∫ h(t)e^{−st}F(t) dt < ∞ for s > δ.
   Repeat step 2 with the weight c(t) = h(t)e^{−st}. Integration by parts now gives an extra term ∫ h'(t)e^{−st}T_t(φ) dt. Given ε > 0, h'/h < ε for t ≥ t_ε. So after normalisation this term is at most ε‖φ‖_∞ + o(1). Hence the limit equation is again T(Pφ) = δT(φ).
   Step 3 is only sketched, since the construction of h is cited.
4. The final claim follows from Lemma 1(c) applied to T. ∎

## Corollary 4 (the only lever; GH)
Assume GH. For every finite positive m ≠ 0: if δ_m = 0, then ω(m) = M.

Equivalently: for every m with ω(m) ≠ M, δ_m ≠ 0. Moreover the sign of δ_m is fixed by the interval of μ(d) over invariant μ on ω(m), which does not contain 0 at its ends.

The same holds backward in time, applying it to −X, which is GH by (O4).

*Proof.* By Proposition 3 there is a positive T with T(Pφ) = 0 carried by ω(m). By L1, T = ν̂, which has full support. ∎

Special cases.
- m = δ_x gives the following. If lim sup_{t→+∞} J_t(x)/t ≤ 0 and ∫_0^∞ e^{J_t(x)} dt = ∞, then the **forward** orbit of x is dense. (The convergent sub-case is not needed here: when δ = 0 is divergent, step 2 suffices.) This is a one-sided strengthening of Lemma 4.3 of [R5-e]. Its proof uses only step 2 of Proposition 3, so it is fully proved.
- By Borel–Cantelli, ν{J_n > εn} ≤ e^{−εn}ν(M), which is summable, and |J_t − J_n| ≤ ‖d‖ for t ∈ [n, n+1]. So lim sup J_t/t ≤ 0 holds ν-a.e. with no GH needed. This is consistent with the ergodicity and conservativity of ν.

## Corollary 5 (why the construction cannot reach the residual horseshoe configuration; GH)
Let Λ be a compact invariant set with μ(d) ≤ −a < 0 for every invariant μ on Λ. (This is the situation of Theorem 4.1 / Corollary 4.3 of [R5-d] and of (H3).) Then every finite positive m with ω(m) ⊂ Λ has δ_m ≤ −a.

This applies to measures on Λ, on local stable discs W^s_loc(x) for x ∈ Λ, and on any subset of W^s(Λ). Their forward Patterson limits are strictly "subcritical" eigen-measures, with no contradiction.

Backward in time, measures on Λ or on local unstable discs of Λ have backward critical exponent ≥ a > 0 (apply Proposition 3 to −X, whose d is −d). Again there is no contradiction.

*Proof.* This is immediate from Proposition 3 and Lemma 1(c). ∎

So within the configuration (H3), a contradiction from this construction needs an m whose ω-limit set contains points outside Λ, is still ≠ M, and has critical exponent exactly 0. None of the established results give control over such sets.

## Where the suggested construction stops (precise)
Take μ ergodic with h_μ > 0. Take D a Pesin unstable disc through a μ-generic x, with leaf volume m_D. (Such discs exist: Ruelle's inequality gives a positive exponent, and the Pesin unstable manifold theorem gives the disc; both cited from memory.)

1. By Proposition 3, the Jacobian-weighted Patterson limit is a positive T on ω(m_D) with T(Pφ) = δ_D T(φ). Here ω(m_D) ⊃ supp μ, because x ∈ D is μ-generic and so its forward orbit accumulates on supp μ.
2. L1 bites only if δ_D = 0 and ω(m_D) ≠ M (Corollary 4).
   - δ_D is not determined by μ. Write e^{J_t} = (u-Jacobian of g_t along D) × (complementary Jacobian). The first factor integrates to vol_u(g_tD). Its growth rate is at least the sum of positive exponents on the part of D that follows x (Pesin/Ledrappier–Young; cited). Yomdin–Newhouse relate the maximal disc-volume growth to h_top, but say nothing about the complementary factor.
   - The complementary factor along the part of g_tD that wanders away from the orbit of x is uncontrolled.
   - ω(m_D) is uncontrolled too: it is typically the closure of the global unstable set, possibly all of M.
3. Switching to u-volume weights produces invariant (u-Gibbs) limits. By Lemma 2, L1 applies to those only under (V).
4. The Lemma H route needs L^1(ν) approximate solutions. A disc measure is ν-singular. Thickening it into a smooth family of discs reproduces the Jacobian cancellation of [R5-d] Lemma 5.1, and so leads back only to Theorem K of [R5-f]. This point is a remark, not a theorem.

So: **(PE) ⇐ (Q)**, where (Q) is: positive entropy yields a finite positive m with δ_m = 0 and ω(m) ≠ M (forward or backward). This implication is proved by Corollary 4, with no further hypotheses. I could not prove (Q) for unstable discs. By Corollary 5, (Q) cannot be met by measures whose ω-limit lies in a uniformly dissipative horseshoe.

## Status
- **Proved:**
  - Lemmas 0, 1 and 2(i).
  - Proposition 3, divergent case (step 2). Step 3 relies on Patterson's slowly varying weight, which is cited and sketched.
  - Corollary 4, and its special case for points, which uses only step 2.
  - Corollary 5, modulo the Proposition 3 citation.
  - The reduction (PE) ⇐ (Q).
- **Not proved:** (PE) itself.
- **Open:**
  - (Q).
  - Whether δ_D = 0 for some Pesin unstable disc D of a positive-entropy measure, together with ω(m_D) ≠ M.
  - Whether a uniformly volume-contracting non-attracting horseshoe (configuration (H3)) can coexist with GH.
  - The (V) question (smooth invariant volume under GH).

=== END OF ANSWER round6_q8 ===
