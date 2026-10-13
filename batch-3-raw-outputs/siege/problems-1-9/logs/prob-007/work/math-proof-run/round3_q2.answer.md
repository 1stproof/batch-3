# Answer to round3_q2

Setting: t0 = 1/4, f(z) = 1 − 11/(12z) + 1/(6z²), a_0 = c_1 = 0, a_1 = ∞, a_2 = 1, a_3 = 1/4, c_2 = 4/11, v = −25/96.
V(w) := V_{1/4}(w) = −((w−1)² − 1/4)² / (4w(w−1)(w−3/4)). Check: V(1/4) = −(25/256)/(3/8) = −25/96 = v.
Steps 1–3 (the planner's formula for V_t and the linking-number argument) are used as given. I re-checked V_{1/4}(1/4) = v and the deck group at t = 1/4. I did not re-derive the general formula.

## (a) α = V∘β is a simple arc from v to ∞, and where it crosses R

**Deck maps at t = 1/4.** g_0(w) = (w−3/4)/(w−1), g_3(w) = (3/4)(w−1)/(w−3/4), and g_2 = g_0∘g_3 = 3/(4w). This last formula is computed directly: g_3 − 3/4 = −(3/16)/(w−3/4) and g_3 − 1 = −(w/4)/(w−3/4).

**Real locus.** V(w) is real exactly when w̄ ∈ {w, g_0 w, g_2 w, g_3 w}.
- w̄ = g_0(w) is equivalent to |w|² − 2 Re w + 3/4 = 0, i.e. the circle C_1: |w−1| = 1/2.
- w̄ = g_2(w) is the circle C_0: |w| = √3/2.
- w̄ = g_3(w) is equivalent to |w − 3/4|² = −3/16, which has no solutions.

So V^{-1}(R̂) = R̂ ∪ C_0 ∪ C_1. This locus cuts the sphere into 8 open regions. Each region is mapped conformally by V onto an open half-plane, because V has degree 4 and is a Galois cover. The points of V^{-1}(B) are 0, 1, ∞, 3/4, 1/2, 3/2, ±√3/2, 1/4, 2/3, 9/8, 3 and 3/4 ± i√3/4. All of them lie in R̂ ∪ C_0 ∪ C_1.

**The path β.** It has three pieces:
- P1: the lower half of |w| = 1/4, from 1/4 to −1/4;
- P2: the upper half of |w − 5/32| = 13/32, from −1/4 to 9/16;
- P3: the lower half of |w − 21/32| = 3/32, from 9/16 to 3/4.

**Where each piece meets the real locus.**
- P1 lies in |w| ≤ 1/4. Such points satisfy |w−1| ≥ 3/4, so P1 avoids C_0 and C_1.
- P3 lies in |w| ≤ 3/4 < √3/2. Its circle lies inside the open disc of C_1, because 11/32 + 3/32 < 1/2. So P3 avoids C_0 and C_1.
- P2 lies in |w| ≤ 9/16, so it avoids C_0. It meets C_1 exactly once, at w* = (19 + i√35)/36. This comes from solving |w|² = (5/16)x + 9/64 together with |w|² = 2x − 3/4, which gives x = 19/36.

So the interior of β meets the real locus only at w*, and β avoids V^{-1}(B) except at its endpoints.

**Values at the special points.**
- V(1/4) = v.
- V(−1/4) = 441/320 ≈ 1.378, which lies in (1, ∞).
- V(9/16) = −225/12096 ≈ −0.0186, which lies in (v, 0).
- V(3/4) = ∞ = a_1.
- V(w*) lies in (0, 1/4). Reason: the arc of C_1 from 1/2 to the critical point 3/4 + i√3/4 contains no critical point. V is real on it and the endpoint values are V(1/2) = 0 and V(3/4 + i√3/4) = 1/4. So V maps this arc injectively onto [0, 1/4]. The point w* lies on the open arc: arg(w* − 1) is about 160.8°, which is between 120° and 180°.

**Signs of the imaginary parts.** V is real on the real locus, so on each region Im V has a constant sign. Following the four sub-arcs P1, P2 up to w*, P2 after w*, and P3, the signs alternate. The numerics quoted in the brief fix the first sign as lower. This can also be checked exactly: V'(1/4) is real and nonzero, and P1 leaves 1/4 going downward. So α consists of:
1. A1: from v to 441/320, in the lower half-plane;
2. A2: from 441/320 to V(w*) ∈ (0, 1/4), in the upper half-plane;
3. A3: from V(w*) to −225/12096, in the lower half-plane;
4. A4: from −225/12096 to ∞, in the upper half-plane.

**Simplicity.** Each sub-arc is injective, because it is the image under V of an arc lying in one region where V is conformal. Sub-arcs in opposite half-planes are disjoint, and the five real endpoints are distinct. That leaves two pairs to check.
- A1 and A3. g_0 maps the region of P2-after-w* to the region of P1. It is real with negative determinant, so it swaps the half-planes; it sends the inside of C_1 to the outside; and it preserves C_0. So A1 ∩ A3 = ∅ if and only if g_0(P2 after w*) ∩ P1 = ∅. Now g_0(−1/4) = 4/5 and g_0(9/16) = 3/7. Hence g_0 maps the circle of P2 onto the circle with centre 43/70 and radius 13/70, and every point of that circle has Re ≥ 3/7 > 1/4 ≥ |P1|. So the two arcs are disjoint.
- A2 and A4. By the same reasoning, A2 ∩ A4 = ∅ if and only if g_0(P2 up to w*) ∩ P3 = ∅. The circle of P3 has centre 21/32 and radius 3/32. The centres differ by 94/2240, which is less than the difference of the radii, 13/70 − 3/32 = 206/2240. So the circle of P3 lies strictly inside the image circle, and the arcs are disjoint.

Therefore α is a simple arc from v to a_1 = ∞ whose interior lies in S²∖B. In order, it:
- leaves v going downward;
- passes below 0, 1/4 and 1;
- crosses R upward in (1, ∞);
- passes above 1 and 1/4;
- crosses R downward in (0, 1/4);
- passes below 0;
- crosses R upward in (v, 0);
- goes to ∞ in the upper half-plane.

## (b) Lifting β through λ

Recalled from memory: λ(τ+2) = λ(τ), λ(−1/τ) = 1 − λ(τ), λ maps iR_+ decreasingly onto (0, 1), and λ ≈ 16e^{iπτ} as Im τ → ∞.

**Homotopy class of β in C∖{0,1}.** P1 followed by the part of P2 back to the real axis is a clockwise loop around 0 based at 1/4. The rest of β is homotopic, relative to its endpoints, to the segment [1/4, 3/4]: neither 0 nor 1 lies between these arcs and the real axis, and the point 1/4 is not a puncture here.

**Lifting the loop.** Deform the loop into: the segment from 1/4 to ε, a small clockwise circle around 0, and the segment back. The real segments lift to the imaginary axis. The small circle lifts in the region where λ ≈ 16e^{iπτ}, so a change of −2π in arg λ forces Re τ to change by −2. Hence the loop lifts from p0 to p0 − 2.

**Lifting the segment.** The segment [1/4, 3/4] lifts, from p0, down the imaginary axis to the point where λ = 3/4 = 1 − 1/4, which is S(p0). By invariance under the translation by −2, the lift starting from p0 − 2 ends at S(p0) − 2.

So q* = T^{-2}S(p0), with g(τ) = −1/τ − 2, matrix [[−2, −1], [1, 0]]. Its trace is −2, so g is parabolic, with fixed point −1. It is not elliptic. Step 3 then gives an infinite orbit.

## (c) Independent check that T_γ preserves D_f (the 3/0 split)

Put u = 1/z. Then f = v + s²/6 with s = u − 11/4. In the s-coordinate:
- c_1 = 0 corresponds to s = ∞, and c_2 to s = 0;
- a_1 = ∞ corresponds to s = −11/4, and f(a_1) = 1;
- a_2 = 1 corresponds to s = −7/4, and f(a_2) = 1/4;
- a_3 = 1/4 corresponds to s = 5/4, and f(a_3) = 0.

The curve f^{-1}(α) is the set of s with s² ∈ 6(α − v). It passes through s = 0 (that is, c_2) and s = ∞ (that is, c_1). Its two complementary components are swapped by s ↦ −s, and each corresponds to one branch h of √(6(x − v)) on S²∖α. So a_1, a_2, a_3 lie on the same side if and only if the branch h takes the values −11/4, −7/4, 5/4 at x = 1, 1/4, 0, up to one overall sign.

On the real line, the positive branch gives 11/4, 7/4, 5/4 at those three points. Continue h along paths that avoid α. Compared with the real segment between two points, h changes sign by (−1)^k, where k is the number of crossings of that segment with α (mod-2 intersection with an arc from v to ∞). By (a):
- [1/4, 1] has no crossings with α, so h(1) and h(1/4) have the same sign;
- [0, 1/4] has exactly one crossing, so h(0) has the opposite sign.

Hence one branch takes the values (−11/4, −7/4, 5/4). So a_1, a_2, a_3 all lie in one component, and a_0 lies on the curve: this is the 3/0 split. The lifting criterion (the outer preimage disc contains no marked point other than the curve's own points, so the lift of T_γ is trivial relative to A) agrees with Step 4, where β ends at 1 − t0 = 3/4.

## (d) Mapping-class description

I did not carry this out. It is left open.

## (e) Final answer

Take f with t0 = 1/4. On the real line the points are v = −25/96 < c_1 = 0 < f³(c_1) = 1/4 < f²(c_1) = 1, and f(c_1) = ∞.

Let α be the simple arc that:
1. starts at v and goes into the lower half-plane;
2. passes below 0, 1/4 and 1, and crosses R upward in (1, ∞);
3. returns through the upper half-plane above 1 and 1/4, and crosses R downward in (0, 1/4);
4. passes below 0 and crosses R upward in (v, 0);
5. goes to ∞ in the upper half-plane.

Up to isotopy rel B, α is V_{1/4} applied to the β of (a). Let γ be the boundary of a thin regular neighbourhood of α. It is a simple closed curve that separates {v, f(c_1)} from {c_1, f²(c_1), f³(c_1)}.

Then T_γ itself (power 1) preserves D_f, by (c) and Step 4. The ⟨T_γ⟩-orbit of the component of D_f through the base point is infinite, by (b) and Step 3: the associated g = T^{-2}S is parabolic.

For any other f in the family, transport γ along a path in W.

**What is proved, what is not, what is open.**
- Proved here: (a), (b) and (c), assuming the planner's Steps 1–3.
- Not re-derived: Step 1 (the formula for V_t, checked only at the dynamical point for t = 1/4) and Step 3.
- Recalled from memory, not proved: the standard properties of λ used in (b).
- Open: (d), the mapping-class description of γ.

=== END OF ANSWER round3_q2 ===
