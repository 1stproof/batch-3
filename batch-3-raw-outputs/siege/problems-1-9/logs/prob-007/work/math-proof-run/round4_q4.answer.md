# round4_q4 — the twist curve γ: an independent description and cross-check

Plan: (1) compute α_0 exactly; (2) find the loop L with β ≃ ℓ·σ and get α ≃ L·α_0, so that α = P(α_0) for an explicit point push P; (3) check independently that T_γ preserves D_f, using f^{-1}(α) in a coordinate where f is z ↦ z²; (4) give the final description.

Notation is the proof's: f = f_{1/4}(z) = 1 − 11/(12z) + 1/(6z²). On the real line, v = −25/96 < a_0 = c_1 = 0 < a_3 = 1/4 < a_2 = 1, and a_1 = ∞. The map is V(w) = −(w−½)²(w−3/2)² / (4w(w−1)(w−¾)).

All twists are left (positive) Dehn twists. "Push(δ)" means dragging v forward along the loop δ.

**Summary.**
- Every step of the proof was re-checked and I found no error. Two loose phrasings are noted in §5.
- The point push is T_c^{-1}, where c is the round circle |z − 1/2| = 3/5. It encloses a_0, a_3 and a_2 but not v.
- We get α ≃ T_c^{-1}(α_0^+), γ = T_c^{-1}(γ_0^+) and T_γ = T_c^{-1} T_{γ_0^+} T_c.
- Independent check: T_γ preserves D_f, with trivial lift.
- Orientation: T_γ = Push(lasso of α, traversed with a_1 on its right). Equivalently, T_γ^{-1} is the push with a_1 on its left.

## 0. Preliminary checks (re-derived by hand)

**The parameters of f.** b = −11/12 and c = 1/6. The second critical point is c_2 = 4/11, and v = f(c_2) = −25/96.

**The deck group of V.** It is {id, g_0, g_2, g_3}. The fixed points of each element are:
- g_0(w) = (w−¾)/(w−1) fixes 1/2 and 3/2;
- g_2(w) = 3/(4w) fixes ±√3/2;
- g_3(w) = ¾(w−1)/(w−¾) fixes P, P̄ = ¾ ± (√3/4)i.

These are the 6 = 2·4 − 2 critical points of V, so there are no others.

**Values of V.** V(1/4) = −25/96 = v and V(−√3/2) = 1. The orbit of 1/4 under the deck group is {1/4, 2/3, 9/8, 3}, and V(9/8) = −25/96 by direct computation, as it must be.

**Monotonicity.** V has no critical points in (0, 1/2) or in (1/2, 3/4). So:
- V increases from −∞ to 0 on (0, 1/2), passing through v at w = 1/4;
- V decreases from 0 to −∞ on (1/2, 3/4), passing through v at w = 2/3.

## 1. The arc α_0 (task item 1)

The real segment [1/4, 3/4] is **not** a path in the unbranched covering Ŵ = Ĉ ∖ V^{-1}(A). It contains w = 1/2, a critical point with V(1/2) = 0 = a_0. It also contains w = 2/3, which maps to v.

Its image runs entirely along R:
- [1/4, 1/2] goes from v rightwards to a_0 = 0;
- [1/2, 2/3] goes back leftwards from 0 to v;
- [2/3, 3/4] goes from v leftwards to −∞ = a_1.

So "the arc α_0" needs a perturbation at w = 1/2.

**The perturbation.** Near w = 1/2 we have V(w) ≈ −4(w−½)². Here 4w(w−1)(w−¾) = 1/4 and (w−3/2)² = 1 at w = 1/2.
- Passing 1/2 **above** (w = ½ + εe^{iθ}, with θ going from π to 0) makes V go once around 0 **clockwise**: from the left of 0, over the top, around the right, under the bottom, and back to the left.
- Passing **below** makes V go once around 0 counterclockwise.

Call the two perturbed segments σ^±. As paths in S² ∖ A:
- α_0^+ := V(σ^+) runs from v to near 0, makes a clockwise full turn around a_0, then runs left along R to ∞.

Pulling this tight (v is not a puncture for these homotopies) gives the simple arc

  **α_0^+:** from v, go into the upper half-plane; cross R downward at a point of (0, 1/4); then stay in the lower half-plane until ∞.

Its mirror image is

  **α_0^-:** from v, go down; cross upward in (0, 1/4); stay in the upper half-plane until ∞.

These two arcs differ by pushing v once around a_0. Both σ^± are homotopic to [1/4, 3/4] in C ∖ {0, 1}, because 1/2 is not a puncture of the λ-plane. So both lift through λ from p_0 = iy_0 to S(p_0) = i/y_0. This gives g = S, which is elliptic, as the proof says.

## 2. α as an explicit point-push image of α_0^+ (task item 2)

### (a) The lift β

I re-checked the face-by-face lift in the proof. The faces L_2, U_2, U_12 and L_12 and the boundary preimages it uses are all correct. They give:
- β leaves 1/4 into the lower half-plane;
- it crosses R in (−√3/2, 0) into U_2, so it has gone clockwise around w = 0;
- it crosses the C1-arc from 1/2 to P, so it passes **above** 1/2;
- it crosses down through (1/2, 2/3) and then runs inside L_12 to 3/4.

The faces U_12 and L_12 are discs, and P, P̄ and 3/4 lie on their boundaries. So in Ŵ,

  β ≃ ℓ_0^{cw} · σ^+,

where ℓ_0^{cw} is the clockwise circle |w| = 1/4 based at w = 1/4.

### (b) The image L := V(ℓ_0^{cw})

The closed disc |w| ≤ 1/4 contains no point of V^{-1}(A) except the simple pole w = 0. The circle |w| = 1/4 meets V^{-1}(R) only at w = ±1/4. This is because C1 (|w−1| = 1/2) and C2 (|w| = √3/2) lie at distance more than 1/4 from 0.

We have V(1/4) = v and V(−1/4) = 441/320 ∈ (1, ∞). The upper half of the circle lies in U_2, which maps to the upper half-plane. Hence:

  **L:** v → lower half-plane → cross R upward at a point x_1 ∈ (1, ∞) → upper half-plane → back to v.

This is a **counterclockwise** simple loop based at v around {a_0, a_3, a_2}; equivalently, a lasso around a_1. It is consistent with the local form V ≈ −3/(16w) near w = 0.

So α ≃ V(β) ≃ L · α_0^+ as paths in S² ∖ A from v to a_1.

### (c) Consistency with the crossing pattern of α

L · α_0^+ is: v → lower → up at x_1 ∈ (1, ∞) → upper (pass near v, still in the upper half-plane) → down at x_2 ∈ (0, 1/4) → lower → ∞.

This is not simple. The lower chords v–x_1 and x_2–∞ interleave, because v < x_2 < x_1 < ∞.

To fix this, replace the last piece "x_2 → lower → ∞" by "x_2 → lower → up at x_3 ∈ (v, 0) → upper → ∞". The two pieces together bound a disc whose only marked point is v. The point v is not a puncture for homotopies of paths in S² ∖ A. Hence the replacement is a homotopy rel endpoints, and the result is exactly the proof's α.

By Epstein's theorem (cited from memory: homotopic simple arcs rel endpoints are isotopic rel endpoints), together with isotopy extension, α is isotopic rel B to the simple representative of L·α_0^+.

### (d) The push formula

**Push action on arcs.** Let H_s be the dragging isotopy, with H_s(v) = δ(s) and A fixed. Then δ|_{[0,s]} · H_s(α_0) is a homotopy rel endpoints from α_0 to δ·H_1(α_0). Hence

  Push(δ)(α_0) ≃ δ^{-1} · α_0.

Therefore α ≃ Push(L^{-1})(α_0^+).

**Push along a simple loop.** Model the push in an annulus N(δ) as (r, θ) ↦ (r, θ + 2πψ(r)), with ψ = 0 at both boundary curves and ψ = 1 on the core. A strand traversed outward through the part where ψ rises turns left, so that part is a left twist. This gives (as in Farb–Margalit)

  Push(δ) = T_{δ_L} T_{δ_R}^{-1},

where δ_L and δ_R are the push-offs of δ to its left and to its right.

For L (counterclockwise, with {a_0, a_3, a_2} on its left):
- δ_L ≃ c, the circle **|z − 1/2| = 3/5**, which encloses 0, 1/4 and 1 but not v;
- δ_R bounds a disc containing only a_1, so its twist is trivial.

Hence Push(L) = T_c, and

  **P := Push(L^{-1}) = T_c^{-1},  α = T_c^{-1}(α_0^+),  γ = T_c^{-1}(γ_0^+),  T_γ = T_c^{-1} T_{γ_0^+} T_c,**

where γ_0^+ = ∂N(α_0^+). The curve c can also be described as ∂N(ρ), where ρ = (−∞, v] is the real ray from v to a_1.

**Direct check of the sign.** Under a left twist T_c^{-1}, the strand of α_0^+ entering the disc bounded by c picks up one counterclockwise turn around c, which is the loop L. The strand leaving picks up a clockwise turn, which can be absorbed into the endpoint a_1. So T_c^{-1}(α_0^+) ≃ L·α_0^+. By contrast, T_c(α_0^+) ≃ L^{-1}·α_0^+, which is a different arc.

## 3. Independent verification that T_γ preserves D_f (task item 3)

### Criterion

Let T ∈ PMod(S², B) with i(T) = 1. Then T preserves D_f if and only if its A-fixing lift T~ is trivial in PMod(S², A). (Use f^*(Tτ) = T~ f^*τ, i_*(Tτ) = i_*τ, and the fact that PMod(S², A) acts freely on Teich(A).)

For T = T_γ:
- γ bounds a disc D containing both critical values v and a_1.
- f^{-1}(D) is an annulus, and f^{-1}(S² ∖ D) is two discs D'_1 and D'_2, each mapped homeomorphically. Their boundaries are γ_1 and γ_2, and T_γ lifts to T_{γ_1} T_{γ_2}.
- a_0 = c_1 lies in the annulus, and a_1, a_2, a_3 lie in D'_1 ∪ D'_2.
- So T~ is trivial if and only if the split of {a_1, a_2, a_3} between D'_1 and D'_2 is 3/0. If it is 2/1, the curve around the two points is essential and T~ ≠ 1.
- The discs D'_i are the two complementary components of the Jordan curve f^{-1}(α), which passes through c_2 and c_1.

### A coordinate in which f is a square

Put y = z − v on the target, and s = 1/z − 11/4 on the source. Then

  y = f(z) − v = s²/6,

because f = 1 + bu + cu² = (1/6)(u − 11/4)² + v with u = 1/z.

The marked points in these coordinates:
- Target: v = 0, a_0 = 25/96, a_3 = 49/96, a_2 = 121/96, a_1 = ∞.
- Source: a_0 = ∞, a_1 = −11/4, a_2 = −7/4, a_3 = 5/4, and c_2 = 0. Check: (11/4)²/6 = 121/96, (7/4)²/6 = 49/96, (5/4)²/6 = 25/96, so f(a_1) = a_2, f(a_2) = a_3, f(a_3) = a_0.

### The preimage of α

In the y-plane, α runs: from 0 into the lower half-plane; up at y_1 > 121/96; down at y_2 ∈ (25/96, 49/96); up at y_3 ∈ (0, 25/96); then above to ∞.

Under s ↦ s²/6, the lower half-plane pulls back to the 2nd and 4th quadrants, and the upper half-plane to the 1st and 3rd. So f^{-1}(α) = Λ_1 ∪ (−Λ_1), where:
- Λ_1 starts at 0 in the 4th quadrant;
- it crosses R at s_1 = √(6y_1) > 11/4, then at s_2 ∈ (5/4, 7/4), then at s_3 ∈ (0, 5/4);
- it ends at ∞ in the 1st quadrant;
- it stays in Re s > 0.

### Parity count

- **a_3 = 5/4 versus a_2 = −7/4.** Take the path [5/4, ε], then the upper semicircle of radius ε, then [−ε, −7/4]. It crosses Λ at s_3, at the ray of −Λ_1 leaving 0 into the 2nd quadrant, at −s_3 and at −s_2: 4 crossings, which is even.
- **a_2 versus a_1.** The segment [−11/4, −7/4] contains none of −s_1, −s_2, −s_3: 0 crossings.

So the split is **3/0**, T~ = 1, and T_γ preserves D_f, with f^*∘T_γ = f^* and i_*∘T_γ = i_*. This agrees with the proof.

### Side checks with the same method

- **α_0^+.** Λ_1 starts in the 1st quadrant and crosses R only at s_2 ∈ (5/4, 7/4). The counts are 2 and 0, so the split is 3/0 and T_{γ_0^+} also preserves D_f. This is consistent: the linking argument only fails for it because g = S is elliptic.
- **c.** Here ρ = (−∞, v] pulls back to the imaginary axis, which separates a_3 from {a_1, a_2}. The split is 2/1, so T_c does **not** preserve D_f. Hence T_γ preserving D_f is not a formal consequence of the conjugation formula; it has to be (and here was) checked separately.

### Orientation

The regular neighbourhood of the lasso of α is an annulus. One boundary curve bounds a disc containing only a_1, and the other is γ. So, by §2(d):
- Push(lasso traversed with a_1 on its **right**) = T_γ;
- Push(lasso traversed with a_1 on its **left**) = T_γ^{-1}.

## 4. Clean description (task item 4)

**Setting.** Take f(z) = 1 − 11/(12z) + 1/(6z²). Its critical points are c_1 = 0 and c_2 = 4/11. The 4-cycle is 0 → ∞ → 1 → 1/4 → 0, and v = −25/96. On R the order is v < c_1 < f³(c_1) < f²(c_1) < f(c_1) = ∞.

**The curve.** γ is the boundary of a thin neighbourhood of the simple arc α from v to f(c_1) = ∞:
- leave v downward and cross R upward to the right of 1;
- come back over the top and cross R downward between 0 and 1/4;
- pass under 0 and cross R upward between v and 0;
- go over v to ∞.

So γ encloses exactly v and f(c_1). It separates them from c_1, f²(c_1) and f³(c_1), and it winds once around {c_1, f³(c_1), f²(c_1)} relative to the "straight" curve.

**Formula.** γ = T_c^{-1}(γ_0), where:
- γ_0 = ∂N(α_0), and α_0 goes from v over 0, down through (0, 1/4), and through the lower half-plane to ∞;
- c is the circle |z − 1/2| = 3/5;
- T_c^{-1} = Push(L^{-1}), i.e. it drags v once clockwise around {0, 1/4, 1}.

Equivalently, α ≃ L · α_0 with L = V(clockwise loop around w = 0).

**Result.** T_γ preserves D_f. By the proof's §3 linking argument, its orbit on π_0(D_f) is infinite.

## 5. Errors and status

**Errors found: none.** The algebra, the face assignments and the final claims are all correct. Two loose phrasings:
- The "straight segment" [1/4, 3/4] passes through w = 1/2 ∈ V^{-1}(a_0). So α_0 is defined only after perturbing, as in §1. Both perturbations give g = S, so the proof's statement about g = S is unaffected.
- The final pattern step "cross upward in (v, 0)" in α is needed only to make the arc simple. Homotopically it is trivial (§2(c)).

**Status.**
- Proved: §§0–4, modulo the results cited from memory. These are Epstein's theorem on homotopic arcs, the push formula Push(δ) = T_{δ_L} T_{δ_R}^{-1} (re-derived in §2(d)), and the free action of PMod(S_{0,4}) on Teich.
- Not addressed: other maps f in the family. As in the proof, this remains only sketched.

=== END OF ANSWER round4_q4 ===
