# Referee report on the planner's sketch (round3_q4)

**Verdict: the argument holds.** I found no fatal error. Every algebraic and topological step that can be checked by hand was re-derived below. That includes the simplicity of α, which the sketch only supported numerically; it is proved here exactly. The only facts not proved here are standard results quoted from memory: the properties of the λ function and Birman's point-push description of the fibre.

## (i) Setting and normalization: correct
- Both coordinates of Ψ = (i_*, f^*) take values in the same space Teich(S², A), with markings induced from the marking on (S², B). One use of i_*, the other by lifting through f. So D_f = Ψ^{-1}(Δ) is literally the definition.
- Fix one biholomorphism Teich(A) ≅ H. The forgetful map Teich(A) → M_{0,4}^{ordered} ≅ C∖{0,1}, sending (a_0,a_1,a_2,a_3) to (0,∞,1,t), is a universal cover. So is λ: H → C∖{0,1}. The identification can therefore be chosen so that π = λ.
- Standard facts used (from memory): λ = θ_2⁴/θ_3⁴, λ(τ+2) = λ(τ), λ(−1/τ) = 1 − λ(τ), λ = 16 e^{iπτ} + O(e^{2iπτ}) at i∞, λ maps iR_+ decreasingly onto (0,1), and the deck group is Γ(2)/±1.
- The maps g with λ∘g = 1 − λ are exactly the coset Γ(2)S.

## (ii) Step 0 and Step 1: correct (re-derived)
**Step 0 at t = 1/4.**
- β = −11/12 and γ = 1/6.
- f(0) = ∞, f(∞) = 1, f(1) = 1/4, f(1/4) = 0.
- f′(z) = 11/(12z²) − 1/(3z³) vanishes at z = 4/11.
- f(4/11) = 1 − 242/96 + 121/96 = −25/96, which agrees with v(t) = −(5/16)²/(3/8).

**Step 1: the pulled-back modulus.**
- The map z ↦ (s_3−s_2)/(z−s_2) sends ∞ ↦ 0, s_2 ↦ ∞, s_3 ↦ 1 and s_0 ↦ w. The labels match: c_1 = a_0 ↦ a_1 = ∞, a_1′ ∈ F^{-1}(1), a_2′ ∈ F^{-1}(t), a_3′ ∈ F^{-1}(0).
- Set u = s_2 − s_0. Since s_2² − s_0² = 1, we get s_2 + s_0 = 1/u.
- From w = (s_3 − s_2)/(−u) we get s_3 = s_2 − wu. Then s_3² − s_2² = t − 1 gives −w(U + 1 − wU) = t − 1, that is, U·w(w−1) = w + t − 1.
- v′ = −s_0² = −(1−U)²/(4U), with 1 − U = ((w−1)² − t)/(w(w−1)). This gives the formula V_t(w) = −((w−1)²−t)²/(4w(w−1)(w+t−1)).
- V_t(t) = −(t²−3t+1)²/(4t(t−1)(2t−1)) = v(t).
- V_t(1−t) = ∞. So w = 1 − t forces v′ = a_1, and the Key consequence of Step 1 holds.
- V_t has 6 = 2·4 − 2 critical points: the double points over 0, 1 and t. So V_t is unramified everywhere else.
- At t = 1/4:
  - V^{-1}(0) = {1/2, 3/2};
  - V^{-1}(1) = {±√3/2};
  - V^{-1}(1/4) = {3/4 ± (√3/4)i};
  - V^{-1}(∞) = {0, 1, ∞, 3/4};
  - V(2/3) = V(3) = −25/96 was checked by hand.

## (iii) Steps 2 and 3: correct
- Ψ(Teich B) avoids every graph Γ_g by the Key consequence. Hence the homotopy σ ≃ σ′ (rel endpoints, inside the contractible Teich(B)) maps into X_g.
- σ′ is a loop under Ψ because:
  - i(T) = 1, so i_*(T^m τ) = p_0;
  - f^*∘T = f^* holds by the lift criterion in (iv).
- Ψσ lies in Δ ≅ H, which is contractible. So Ψσ is null-homotopic in X_g.
- X_g ≅ H × (H ∖ pt), so H_1(X_g) ≅ Z, and the class of a fibre loop is its winding number about g(p_0).
- The non-elliptic hypothesis is exactly what makes Γ_g ∩ Δ = ∅.
- A nonzero winding number therefore contradicts T^m D_0 = D_0.

## (iv) Step 4: correct
**Lift criterion.**
- Let D be the disc bounded by c that contains v and a_1. By Riemann–Hurwitz, f^{-1}(D) is an annulus containing c_1 and c_2.
- f^{-1}(S² ∖ D) is two discs. When the split is 3/0, one disc holds a_1, a_2, a_3 and the other holds none of them.
- So T̃ is a product of twists about a curve bounding an unmarked disc and a curve separating a_0 from the other three marked points. Both are trivial in PMod(S², A).
- Hence f^*∘T = f^* with power 1. This criterion matches the description in the sketch.

**Fibre loop.**
- Pushing v along the lasso of α lifts to β, then a small circle about 3/4, then β^{-1}. The small circle is unramified because 3/4 is a simple preimage of ∞.
- This loop is closed in C∖{0,1}, since 3/4 is not a puncture.
- Its lift to H is closed and winds ±1 about q* = the endpoint of the lift of β.

**Homotopy class of β.**
- The pieces of β are: lower semicircle on [−1/4, 1/4]; upper semicircle on [−1/4, 9/16]; lower semicircle on [9/16, 3/4].
- Together they make one loop around 0 (not around 1), followed by an arc to 3/4.
- The lift starting at p_0 = iy_0 therefore runs to p_0 ± 2 and then to S(p_0) ± 2. So q* = g(p_0) with g = [[±2, −1], [1, 0]] ∈ Γ(2)S.
- g has trace ±2, and its fixed point τ = ±1 is real. So g is not elliptic.

**Simplicity of α (proved here exactly).**
α is simple if and only if β ∩ h(β) = ∅ for every nontrivial deck map h. Each h is a real Möbius map, so it sends semicircles to semicircles or rays. Two semicircles on the same side of R meet if and only if their real intervals interlace. The images of the three pieces of β are:
- g_0 (reverses the half-planes): upper on [2/3, 4/5], lower on [3/7, 4/5], upper on [0, 3/7]. The upper ones are disjoint from or nested in β's upper interval [−1/4, 9/16]. The lower one either contains [9/16, 3/4] or is disjoint from it, and is disjoint from [−1/4, 1/4].
- g_3 (preserves the half-planes): pieces with real span in [15/16, ∞), plus the ray Re w = 7/4, Im w < 0. All lie away from β, whose span is [−1/4, 3/4].
- g_2 = g_0∘g_3: the upper half of |w| = 3, the lower semicircle on [−3, 4/3] (which contains β's lower intervals in nested position), and the upper semicircle on [1, 4/3]. All are disjoint from β.

The interior of β avoids V^{-1}(B), because it meets R only at ±1/4, 9/16 and 3/4. So α is a simple arc from v to a_1, and its interior avoids B.

## (v) Answer to the problem as posed
Take f = f_{1/4}(z) = 1 − 11/(12z) + 1/(6z²), with c_1 = 0 ↦ ∞ ↦ 1 ↦ 1/4 ↦ 0, c_2 = 4/11 and v = −25/96.

**The curve.** Let β be the path in the w-sphere made of three pieces in order:
1. the lower half of |w| = 1/4, from 1/4 to −1/4;
2. the upper half of |w − 5/32| = 13/32, from −1/4 to 9/16;
3. the lower half of |w − 21/32| = 3/32, from 9/16 to 3/4.

Let α = V∘β with V(w) = −((w−1)² − 1/4)²/(4w(w−1)(w−3/4)). Then α is a simple arc from v to a_1 = ∞. Take γ = ∂(a thin regular neighbourhood of α), which encloses exactly v and a_1.

**The theorem.**
- T_γ itself (power 1) preserves D_f.
- For the component D_0 of D_f that contains the point of f, T_γ^m D_0 ≠ D_0 for every m ≠ 0. So the orbit is infinite.

For another f in the family, transport γ along a path in the image W. The sketch's justification for this is only sketched: transport conjugates by a stabilizer element. The problem only needs one f.

**Proved / not proved.**
- Everything above is proved, modulo the cited standard facts (λ, and Birman's description of the fibre by point pushes).
- The transport remark for other f is not fully written out.
- No open questions remain for the problem as posed.

=== END OF ANSWER round3_q4 ===
