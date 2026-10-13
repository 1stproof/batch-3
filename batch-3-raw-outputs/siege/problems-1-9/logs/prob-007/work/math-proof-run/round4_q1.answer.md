# Referee report on ledger entry 16 (round3_q1 proof)

I checked every step of the written proof by hand. Notation is as in the proof: A = {a_0,…,a_3} with a_0 = c_1 and a_{i+1} = f(a_i), and B = A ∪ {v}.

**Summary.** The core argument (§§1–4) is correct. Every algebraic identity checks out. Three steps need a short additional argument, which I supply below:
- (R1) Why the lift of T_γ is a *pure* mapping class of (S²,A), so that "T~ fixes a point, hence T~ = 1" is legitimate.
- (R2) Why the components of D_f are path-connected.
- (R3) The transport from f_{1/4} to an arbitrary map f of the family. The original proof only sketched this; a complete proof is given here.

There are also cosmetic sign fixes: the loop about 0 lifts to p0 − 2 exactly, so g = T^{−2}S. With these additions the proof is complete.

---

## 1. Algebra (§1, §2, §4): all CORRECT

**Normal form.** Consider f_t(z) = 1 + b/z + c/z² = (z² + bz + c)/z². This has degree 2 iff c ≠ 0. The point 0 is a double pole, hence critical with f(0) = ∞, and f(∞) = 1.
- With b = (t²+t−1)/(1−t) and c = t(1−2t)/(1−t), we get b + c = (−t²+2t−1)/(1−t) = t − 1. Hence f(1) = 1 + b + c = t.
- f(t) = 0 ⇔ t² + bt + c = 0. Multiplying by (1−t) gives t² − t³ + t³ + t² − t + t − 2t² = 0. ✓
- Conversely, every map in the family is Möbius-conjugate to exactly one f_t. Normalising (c_1, f(c_1), f²(c_1)) to (0, ∞, 1) forces f = (z² + bz + c)/z², and the two cycle conditions f(1) = t, f(t) = 0 then determine b and c.

**At t = 1/4.**
- b = (1/16 + 4/16 − 16/16)·(4/3) = −11/12 and c = (1/8)(4/3) = 1/6.
- f′(z) = −b/z² − 2c/z³ vanishes at c_2 = −2c/b = 4/11.
- v = f(4/11) = 1 − (11/12)(11/4) + (1/6)(121/16) = (96 − 242 + 121)/96 = −25/96. ✓

The real order is v < 0 < 1/4 < 1 < ∞, and v ∉ A. ✓

**General critical value.**
- In general v(t) = 1 − b²/(4c) = 1 − (t²+t−1)²/(4t(1−t)(1−2t)).
- The identity (t²+t−1)² − (t²−3t+1)² = (2t²−2t)(4t−2) = 4t(1−t)(1−2t) turns this into v(t) = −(t²−3t+1)²/(4t(t−1)(2t−1)).
- At t = 1/4 this gives −(25/256)/(3/8) = −25/96. ✓

**Pullback model.** Let τ' be represented by (Ĉ; 0, ∞, 1, t, v') with marking h. The pulled-back structure carries a degree-2 holomorphic map F with F∘h~ = h∘f. The critical values of h∘f are h(a_1) = ∞ and h(v) = v′, so up to Möbius F(z) = v' + z². The marked preimages are:
- a_0' = ∞, the unique preimage of a_1 = ∞;
- a_1' with a_1'² = 1 − v';
- a_2' with a_2'² = t − v';
- a_3' with a_3'² = −v'.

The Möbius map M(z) = (s_3−s_2)/(z−s_2) satisfies M(∞) = 0, M(s_2) = ∞, M(s_3) = 1. So w = M(s_0) = (s_3−s_2)/(s_0−s_2). ✓

**Fibre formula.** Put u = s_2 − s_0 and U = u².
- Since s_2² − s_0² = 1, we get s_2 + s_0 = 1/u, s_2 = (u + 1/u)/2 and s_0 = (1/u − u)/2.
- s_3 = s_2 − wu, so s_3² − s_0² = 1 − w(U+1) + w²U = t. Hence U = (w+t−1)/(w(w−1)).
- 1 − U = ((w−1)² − t)/(w(w−1)), and v' = −s_0² = −(1−U)²/(4U).

This gives V_t(w) = −((w−1)²−t)²/(4w(w−1)(w+t−1)). ✓ Moreover V_t(t) = −(t²−3t+1)²/(4t(t−1)(2t−1)) = v(t). ✓

**Poles.** The numerator has degree 4 and the denominator degree 3. So the poles are 0, 1, 1−t (simple) and ∞ (simple), and V_t^{-1}(∞) = {0, 1, ∞, 1−t}. At w = 1−t the numerator equals (t²−t)², which is nonzero. Hence V_t(w) = ∞ = a_1 whenever w = 1−t, and since v' ≠ a_1 we get w ≠ 1 − t. So (★) is CORRECT.

**Factorisation at t = 1/4.** (w−1)² − 1/4 = (w−½)(w−3/2), giving the factorised V. ✓

**Deck maps.**
- *g_2(w) = 3/(4w).* Then w−½ ↦ −(w−3/2)/(2w) and w−3/2 ↦ −3(w−½)/(2w). The numerator becomes 9N/(16w⁴), where N = (w−½)²(w−3/2)². The denominator becomes 9(w−¾)(w−1)/(4w³). So V∘g_2 = V. ✓
- *g_0(w) = (w−¾)/(w−1).* Then w−½ ↦ (w−½)/(2(w−1)) and w−3/2 ↦ −(w−3/2)/(2(w−1)). Also g_0 − 1 = (1/4)/(w−1) and g_0 − ¾ = (w/4)/(w−1). The denominator becomes w(w−¾)/(4(w−1)³). So V∘g_0 = V. ✓
- g_0∘g_2 = g_2∘g_0 = ¾(w−1)/(w−¾) = g_3.

So the deck group is the Klein group. Since deg V = 4, V is Galois with this group. ✓

**Real locus.** V has real coefficients, so V(w) ∈ R̂ ⇔ V(w̄) = V(w) ⇔ w̄ = h(w) for some deck map h.
- h = g_0 gives |w−1|² = 1/4, the circle C1.
- h = g_3 gives |w−¾|² = 9/16 − 3/4 = −3/16, which is empty.
- h = g_2 gives |w|² = 3/4, the circle C2.

C1 ∩ C2 is found by subtracting the equations: x = ¾, y = ±√3/4. ✓

**Critical points of V.** By Riemann–Hurwitz there are 6 critical points. They are:
- ½ and 3/2: double zeros, over 0, and the fixed points of g_0;
- ±√3/2: fixed points of g_2, both over 1;
- P and P̄: fixed points of g_3, roots of w² − (3/2)w + ¾ = 0, both over 1/4.

Direct checks:
- At ±√3/2: w² − 2w + ¾ = 3/2 ∓ √3 and 4w(w−1)(w−¾) = 6w − 7w² = ±3√3 − 21/4. Hence V = 1. ✓
- At P: (P−½)(P−3/2) = −P/2 and 4P(P−1)(P−¾) = −P². Hence V(P) = 1/4. ✓

So the branch values are 0, 1 and 1/4 (each with two double preimages). V is therefore an unbranched covering Ĉ∖V^{-1}(A) → Ĉ∖A. ✓

**Images of real points.** ¼ ↦ v; ⅔ = g_0(¼), 3 = g_2(¼) and 9/8 = g_2(⅔) also map to v. The remaining values listed are all ✓.

**Monotonicity on R.**
- Near 0, V ≈ −3/(16w), so V → +∞ as w → 0⁻ and V → −∞ as w → 0⁺.
- On (0,¾) the denominator is positive, so V ≤ 0. V increases from −∞ to 0 on (0,½) and decreases from 0 to −∞ on (½,¾).
- On (−√3/2, 0), V increases from 1 to +∞.
- On (¾, √3/2), V decreases from +∞ to 1.

So V′(¼) > 0. ✓

**Faces.** V^{-1}(R̂) consists of R̂, C1 and C2: 8 faces, each mapped homeomorphically onto an open half-plane. No branch value lies off R, and every pole is on R̂.

∂U_2 consists of [−√3/2, ½] (traversed left to right), then the C1-arc from ½ to P, then the C2-arc from P to −√3/2. Its image runs 1 → ∞ → v → 0 → ¼ → 1, increasing along R̂. So U_2 maps to the upper half-plane, and faces alternate. ✓

---

## 2. Lifting of α (§4): CORRECT

- **Start.** V′(¼) > 0, so leaving v downward lifts into L_2, which maps to the lower half-plane.
- **Into U_2.** On ∂L_2 the preimage of (1, ∞) is (−√3/2, 0). The lift crosses there into U_2.
- **Into U_12.** On ∂U_2 the preimage of (0, ¼) is the C1-arc from ½ to P. This arc lies inside C2, so beyond it is U_12, which maps to the lower half-plane.
- **Into L_12.** On ∂U_12 the image of (½, ¾) is (−∞, 0), decreasing with ⅔ ↦ v. So the preimage of (v, 0) is (½, ⅔), and the lift crosses into L_12.
- **End.** The closure of L_12 contains no pole except ¾: 1 is outside C2 and 0 is outside C1. So β ends at ¾ = 1 − t0. ✓

**Homotopy class of β.** β lies in the disc |w| < √3/2, which contains 0 but not 1. Its continuous argument goes 0 → −π (crossing the negative axis upward) → −2π (crossing (½,⅔) downward) and ends at ¾ approached from below, with argument −2π. So β ≃ (clockwise loop about 0)·[¼,¾] in D∖{0} ⊂ C∖{0,1}. ✓

**λ-lift.** From λ = 16q + O(q²) with q = e^{iπτ}, a counterclockwise loop about 0 based at ¼ lifts to the path from p0 to p0 + 2. So the clockwise loop lifts to the path p0 → p0 − 2.

The segment [¼, ¾] lifts vertically from iy0 − 2 to i/y0 − 2, because λ(i/y0) = λ(−1/(iy0)) = 1 − ¼ = ¾.

So q* = −2 − 1/p0 = g(p0) with g = T^{−2}S = [[−2, −1], [1, 0]].
- The trace is −2, so g is parabolic, with fixed point −1 ∈ ∂H.
- g ∈ Γ(2)S.

The proof's "∓" should be "−". This is harmless, since T^{+2}S is parabolic as well.

A side remark: an element hS ∈ Γ(2)S has even trace b − c, so it is elliptic iff its trace is 0. Non-ellipticity therefore really does need this computation.

**Lasso.** ∞ has the simple preimage ¾, so a small loop about ∞ lifts to a small loop about ¾. That loop is null-homotopic in C∖{0,1}, so it lifts through λ to a small closed loop c̃ about q*. The m-th power of the lasso lifts to β̃'·c̃^{m}·β̃'^{-1}, where β̃' stops short of q*. Its winding number about q* is ±m. ✓

**Simplicity (explicit realisation).** Take x1 = 2, x2 = 1/8, x3 = −1/8, and build α from four pieces:
- the lower semicircle from v to 2 (centre ≈ 0.87, radius ≈ 1.13);
- the upper semicircle over [1/8, 2];
- the lower semicircle over [−1/8, 1/8]: its farthest point from (v+2)/2 is at distance ≈ 1.0 < 1.13, so it lies strictly inside the first semicircle;
- the vertical ray from −1/8 upward to ∞, which misses the upper semicircle because −1/8 < 1/8.

These pieces are pairwise disjoint and avoid B except at the endpoints, so α is simple. (The remark "isotopy class determined by crossing pattern" is not needed.) ✓

**γ and push.** By the standard formula (cited from memory, Farb–Margalit), the point-push Push(δ) along a simple based loop δ equals T_{δ_1}T_{δ_2}^{-1}, where δ_1, δ_2 are the boundary curves of a regular neighbourhood of δ.

For the lasso δ, one boundary curve bounds a disc containing only a_1, so its twist is trivial. The other boundary curve is γ. Hence Push(δ) = T_γ^{±1}, and i(T_γ) = 1. ✓ γ encloses exactly {v, a_1} and is essential, with 2 marked points on one side and 3 on the other.

---

## 3. Teichmüller framework and §3: CORRECT, with repairs R1–R2

**Standard facts, cited from memory and true as used.**
- **Bers fibration and Birman exact sequence** (needs χ(S²∖A) < 0; here |A| = 4). Over p ∈ Teich(A), the fibre of i_* maps by τ' ↦ v'(τ') as a universal covering onto Ĉ∖A_p. The kernel of PMod(S²,B) → PMod(S²,A), which is π_1(S²∖A, v), acts on the fibre as its deck group. Teich(B) is contractible.
- **Modulus map.** π: Teich(A) → C∖{0,1} is a universal covering. PMod(S²,A) ≅ F_2 is torsion-free and acts with finite stabilisers, hence freely. Since λ: H → C∖{0,1} is also a universal covering, we may identify Teich(A) with H, π with λ, and the base point i_*τ_f with iy0. The same identification serves both coordinates of Ψ: f^*τ' is marked by the labels a_i ↦ a_i', and its modulus is the w above. So D_f = Ψ^{-1}(Δ). ✓
- **λ-facts.** λ(−1/τ) = 1 − λ(τ), λ(τ+2) = λ(τ), and λ(q) = λ(r) ⇔ q ∈ Γ(2)r. ✓
- f^* is holomorphic, in particular continuous. ✓

**f^* on a fibre.** On the fibre over p (λ(p) = t), V_t∘(λ∘f^*) = v'. So w = λ∘f^* is a lift of the universal covering through the unbranched covering V_t, and f^* is its lift through λ. Lifts from the simply connected fibre are determined by one value. At τ_f ∈ D_f, w(τ_f) = λ(p0) = t0. ✓

**Linking argument.**
- By (★), Ψ(Teich(B)) ⊂ X_g. Since g has no fixed point in H, Δ ⊂ X_g.
- X_g ≅ H × (H∖{i}) via (p, q) ↦ (p, (q − Re g(p))/Im g(p)), so the class of a fibre loop is its winding number about g(p).
- The homotopy σ ≃ σ' (Teich(B) is contractible), pushed forward by Ψ, stays in X_g. Ψσ ⊂ Δ, which is contractible.

All CORRECT.

**R1 (gap in "T~ = 1").** The formula f^*(φτ) = φ~·f^*(τ) in Teich(A) needs a lift φ~ fixing A *pointwise*; a lift may in general swap a_i with the other preimage of a_{i+1}. Here is the repair.
- Let N be a thin annulus around γ, with D the disc containing {v, a_1} and D' the complementary disc containing {a_0, a_2, a_3}.
- D' contains no critical value, so f^{-1}(D') is two discs, each mapped with degree 1. Hence f^{-1}(N) is two annuli N_1, N_2, each mapped homeomorphically onto N.
- Define T~ = (f|_{N_j})^{-1}∘T_γ∘f on N_j and T~ = id elsewhere. This is continuous because T_γ = id on ∂N, and f∘T~ = T_γ∘f.
- T~ fixes f^{-1}(B) ⊃ A pointwise, so [T~] ∈ PMod(S²,A).
- Write τ = [ψ] and f^*τ = [ψ~]. Then ψ~∘T~^{-1} is a lift of ψ∘T_γ^{-1}, so f^*(T_γτ) = [T~]·f^*(τ).
- The closed λ-lift of the lasso gives f^*(T_γτ_f) = f^*(τ_f). Freeness then gives [T~] = 1, and Ψ∘T_γ = Ψ on all of Teich(B). ✓

**R2 (path-connectedness of components).** On each fibre, w = λ∘f^* is locally injective (V_t∘w = v' is a local homeomorphism), so the fibre derivative of f^* is nonzero. In local coordinates (p, x) on Teich(B), the equation f^*(p, x) − p = 0 therefore has ∂/∂x ≠ 0. By the implicit function theorem, D_f is a smooth complex curve, locally a graph x = x(p). Hence components are path components, and σ ⊂ D_0 exists. ✓

**Conclusion for f_{1/4}.**
- T_γ is a homeomorphism of Teich(B) with T_γ^{±1}(D_f) = D_f, so it permutes the components of D_f.
- Suppose T_γ^m D_0 = D_0 with m ≠ 0. Then the fibre loop f^*∘σ' winds ±m ≠ 0 about g(p0), contradicting §3.
- Hence the orbit of D_0 under ⟨T_γ⟩ is infinite.

---

## 4. Scope (point 5)

**(a)** The problem says "Consider a quadratic rational map f …". The safe reading is "for each such f", so the f_{1/4} case alone does not settle it.

**(b) Complete transport proof (R3).**

*Setup.*
- Any f in the family equals M∘f_t∘M^{-1} with M Möbius and t ∈ W. Here W ⊂ C is the parameter set: t ∉ {0, ½, 1}, b(t) ≠ 0, and v(t) ∉ {0, 1, t, ∞}.
- W is C minus a finite set (the conditions are nontrivial polynomial equations, e.g. t = ¼ satisfies none of them), hence connected.
- Choose a path t_s in W from ¼ to t. Write a_i(s) and v(s) for the marked points of f_{t_s}, and B_s = B(t_s).

*Isotopy.*
- Choose an isotopy h_s of Ĉ, continuous in (s, z), with h_0 = id and h_s mapping B_0 to B_s label by label. This exists because the 5 labelled points move in configuration space and Homeo(Ĉ) → Conf_5 is a fibration (standard, from memory).

*Lift.*
- Let F(s,z) = (s, f_{t_s}(z)) and G(s,z) = (s, h_s f_{1/4}(z)).
- Off the critical-value curves, F is a proper local homeomorphism, hence a 2-sheeted covering. G maps Q = [0,1] × (Ĉ∖f_{1/4}^{-1}V(f_{1/4})) into the base of that covering.
- Q deformation retracts onto its s = 0 slice, where G = F lifts to the identity. So G has a lift h~ with h~_0 = id.
- Each h~_s is a homeomorphism (a lift of a homeomorphism between double covers) and extends continuously over the critical points. It satisfies f_{t_s}∘h~_s = h_s∘f_{1/4}.

*Agreement on A.*
- h~_s(a_0) is the unique preimage of the critical value a_1(s), namely a_0(s).
- For i ≥ 1, h~_s(a_i) moves continuously within the two disjoint continuous branches of f_{t_s}^{-1}(a_{i+1}(s)). It starts on the branch a_i(s), so h~_s(a_i) = a_i(s) for all s.
- Hence h_s^{-1}h~_s fixes A pointwise for every s, and φ1 := h~_1 is isotopic to φ0 := h_1 rel A.

*Identification of deformation spaces.* Define Φ[ψ] = [ψ∘φ0^{-1}]: Teich(B_0) → Teich(B_1). This is a biholomorphism.
- If F∘ψ~ = ψ∘f_{1/4}, then F∘(ψ~∘φ1^{-1}) = ψ∘φ0^{-1}∘f_t. So f_t^*Φ = Φ_A^{(1)}∘f_{1/4}^*.
- Also i_*Φ = Φ_A^{(0)}∘i_*.
- Since φ0 ≃ φ1 rel A, Φ_A^{(0)} = Φ_A^{(1)}, and this map is bijective. Hence Φ(D_{f_{1/4}}) = D_{f_t}, carrying components onto components.
- Φ∘T_γ = T_{φ0(γ)}∘Φ.

*Conclusion.* The curve M(h_1(γ)) works for f. It encloses exactly v and f(c_1), and T_{M h_1(γ)} has an infinite orbit on π_0(D_f). ✓

When the real order v < c_1 < f³(c_1) < f²(c_1) < f(c_1) persists (for example real t near ¼), the same explicit description applies verbatim in the normal-form coordinates.

---

## 5. What remains

**Cited from memory:**
- the Bers fibration and Birman exact sequence;
- the push = T_{δ_1}T_{δ_2}^{-1} formula;
- the λ-function facts;
- that the free PMod action on Teich(A) is the deck action;
- that Homeo(Ĉ) → Conf_5 is a fibration.

**Not settled here:** whether the actual number of components of D_f is infinite. That follows anyway: an infinite orbit forces infinitely many components.

**Open questions:** none affecting the claim.

VERDICT: the proof establishes the claim after the following repairs:
- (R1) show that the lift of T_γ, taken to be the identity off f^{-1}(N), fixes A pointwise, so that f^*∘T_γ = [T~]∘f^* with [T~] ∈ PMod(S²,A) (§3 above);
- (R2) prove that D_f is a smooth curve, so its components are path-connected;
- (R3) supply the complete transport to an arbitrary f in the family (§4b), giving γ_f = M h_1(γ);
- minor: replace ∓ by −, so that g = T^{−2}S; and realise α by explicit semicircles.

=== END OF ANSWER round4_q1 ===
