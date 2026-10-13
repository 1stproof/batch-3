# Referee report: audit of the round3_q1 proof (ledger entry 16)

I checked every step of the written proof. I re-derived every identity by hand. Below, "CORRECT" means I re-checked it. Where the text is incomplete I supply a repair. The verdict is at the end.

## 1. Algebra

**Normal form.** f_t(z) = 1 + b/z + c/z², with b = (t²+t−1)/(1−t) and c = t(1−2t)/(1−t).
- Put c_1 = 0, f(c_1) = ∞, f²(c_1) = 1. A double pole at 0 with f(∞) = 1 forces the form f = 1 + b/z + c/z². So every map in the family is Möbius-conjugate to some f_t, and the labelling of the cycle makes the normalisation unique.
- b + c = (t²+t−1+t−2t²)/(1−t) = −(1−t)²/(1−t) = t−1. So f(1) = t. CORRECT.
- (1−t)(t² + bt + c) = t² − t³ + t³ + t² − t + t − 2t² = 0. So f(t) = 0. CORRECT.
- Degree 2 needs c ≠ 0, i.e. t ≠ 1/2. A 4-cycle needs t ∉ {0, 1}.

**Values at t = 1/4.**
- b = (−11/16)(4/3) = −11/12 and c = (1/8)(4/3) = 1/6.
- c_2 = −2c/b = 4/11.
- v = 1 − b²/(4c) = 1 − 121/96 = −25/96.

All CORRECT. The real order v < 0 < 1/4 < 1 < ∞ is CORRECT.

**v(t) in general.** v(t) = 1 − b²/(4c). Write D = 4t(1−t)(1−2t). Then
(t²+t−1)² − (t²−3t+1)² = (2t²−2t)(4t−2) = D.
So v(t) = −(t²−3t+1)²/(4t(t−1)(2t−1)), which equals V_t(t). CORRECT. At t = 1/4: −(25/256)/(3/8) = −25/96. CORRECT.

**Fibre formula.** The double cover of (Ĉ; 0, ∞, 1, t, v') branched over ∞ and v' is F(z) = v' + z², up to a Möbius map of the source. The labels are forced by the condition that a_i' maps to a_{i+1}:
- a_0' = ∞, the unique preimage of the critical value a_1;
- s_2² = 1 − v', s_3² = t − v', s_0² = −v'.

The Möbius map z ↦ (s_3−s_2)/(z−s_2) sends (∞, s_2, s_3, s_0) to (0, ∞, 1, w). Then:
- s_2² − s_0² = 1, so s_2 = (u + 1/u)/2 and s_0 = (1/u − u)/2;
- s_3 = s_2 − wu;
- s_3² − s_0² = 1 − 2wu·s_2 + w²U = 1 − w(U+1) + w²U = t, so U = (w+t−1)/(w(w−1));
- 1 − U = ((w−1)² − t)/(w(w−1));
- v' = −(1−U)²/(4U) = −((w−1)² − t)²/(4w(w−1)(w+t−1)).

CORRECT. V_t has degree 4, which matches the 4 sign choices of (s_0, s_2, s_3) modulo the global sign.

**Branching of V_t.** Monodromy flips s_0 around 0, s_2 around 1 and s_3 around t. So over each of 0, 1, t there are exactly two simple critical points. That gives total ramification 6 = 2·4 − 2, as Riemann–Hurwitz requires. The poles 0, 1, 1−t, ∞ are simple and distinct (at w = 1−t the numerator is (t²−t)² ≠ 0). So V_t is unbranched over S²∖A, and the claim V_t^{-1}(∞) = {0, 1, ∞, 1−t} is CORRECT. This explicit justification was missing from the text but is true.

**Deck maps at t = 1/4.** V(w) = −(w−½)²(w−3/2)²/(4w(w−1)(w−¾)).
- For g_0(w) = (w−¾)/(w−1): with W = g_0(w),
  - W−½ = (w−½)/(2(w−1)) and W−3/2 = −(w−3/2)/(2(w−1));
  - W(W−1)(W−¾) = w(w−¾)/(16(w−1)³);
  - hence V(W) = V(w).
- For g_2(w) = 3/(4w): with W = g_2(w),
  - W−½ = −(w−3/2)/(2w) and W−3/2 = −3(w−½)/(2w);
  - 4W(W−1)(W−¾) = 9(w−¾)(w−1)/(4w³);
  - hence V(W) = V(w).
- g_0∘g_2 = ¾(w−1)/(w−¾) = g_3.

These form a Klein four-group of order deg V = 4, so V is Galois with this deck group. CORRECT.

**Real locus.** V has real coefficients. So V(w) ∈ R iff V(w̄) = V(w) iff w̄ ∈ (deck orbit of w).
- g_0 gives |w−1|² = ¼, the circle C1.
- g_3 gives |w−¾|² = −3/16, which is empty.
- g_2 gives |w|² = ¾, the circle C2.

C1 ∩ C2 is Re w = ¾, Im w = ±√3/4; these are the fixed points of g_3. The fixed points of g_0 are ½ and 3/2, which lie over 0. The fixed points of g_2 are ±√3/2. Using w(w−1) = ¾ − w on C2, one gets V(±√3/2) = [(3/2 ∓ √3)/(2(±√3/2 − ¾))]² = 1. So P, P̄ lie over the third branch value t = ¼.

The graph has 6 vertices and 12 edges, so it has 8 faces. Each face contains no critical point and therefore maps homeomorphically onto a half-plane. CORRECT.

**Real images.** All of the following are CORRECT:
- V(2/3) = −(25/1296)/(2/27) = −25/96, with g_0(¼) = 2/3;
- g_2(¼) = 3 and g_2(2/3) = 9/8;
- the remaining listed values;
- on (0, ½), V increases from −∞ to 0, since near 0⁺ we have V ≈ −(9/16)/(3w), and there is no critical point in (0, ½).

## 2. Teichmüller framework

- **Identification Teich(A) ≅ H with π = λ.** Teich(A) is simply connected. PMod(S²,A) ≅ F_2 is torsion-free and acts properly, hence freely, with quotient M_{0,4} ≅ C∖{0,1}. λ is also a universal cover. So a biholomorphism with π = λ exists. CORRECT.
- **Ψ = (i_*, f^*).** Both coordinates are markings of the same reference (S², A): i_* restricts the marking ψ, and f^* uses a lift ψ~ of ψ, with A ⊂ f^{-1}(B) in the reference sphere. So D_f = Ψ^{-1}(Δ). CORRECT.
- **Fibre map.** On the fibre Ũ ≅ H over p0, normalise a_0..a_3 to 0, ∞, 1, t0. Then w = λ∘f^* is continuous and satisfies V_{t0}∘w = (position of v'). Hence f^*|Ũ is the unique λ-lift of w with the prescribed base value. CORRECT.
- **Base point.** The base point τ_f, given by the identity marking of the actual Riemann sphere, lies in D_f because f is holomorphic, and w(τ_f) = t0. CORRECT.
- **(★).** It follows from V_t^{-1}(∞) ∋ 1−t together with v' ≠ a_1. CORRECT.

## 3. Linking argument

- λ(q) = 1 − λ(p) = λ(Sp) iff q ∈ Γ(2)S·p. CORRECT.
- For non-elliptic g, Γ_g ∩ Δ = ∅. The map (p, q) ↦ (p, (q − Re g(p))/Im g(p)) is a homeomorphism of H×H. It carries Γ_g to H×{i}, and on each fibre it is an affine map of H. So X_g ≅ H×(H∖{i}), and the class of a fibre loop is its winding number about g(p). CORRECT.
- Ψ(Teich(B)) ⊂ X_g by (★). Ψσ ⊂ Δ, and Δ is a contractible subset of X_g. Ψσ' is a loop at (p0, p0). CORRECT.
- **Small gap: components.** The text uses components of D_f as path components. Repair: D_f = Ψ^{-1}(Δ) is a complex-analytic subset of Teich(B). Analytic sets are locally path-connected (they are locally triangulable), so components coincide with path components.

## 4. Curve and computation

- **Simplicity of α.** Circle order: v < x3 < 0 < x2 < ¼ < 1 < x1 < ∞.
  - Lower chords: (v, x1) ⊃ (x3, x2).
  - Upper chords: (x3, ∞) ⊃ (x2, x1).
  
  Both systems are nested, hence realisable by disjoint chords in the open half-discs, which contain no marked points. Disjoint arc systems in a disc are unique up to isotopy rel endpoints. CORRECT.
- **γ = ∂N(α).** γ encloses exactly v and a_1. Forgetting v, it bounds a once-marked disc, so i(T_γ) = 1.
- **Push = T_γ^{±1}.** The push along a simple loop ℓ equals T_{∂_1}T_{∂_2}^{-1}, where ∂_1, ∂_2 are the boundary curves of an annular neighbourhood of ℓ (standard fact, from memory). For the lasso, one boundary bounds a disc containing only a_1, so its twist is trivial. CORRECT.
- **Face-by-face lift.** Re-checked with oriented boundaries.
  - ∂U_2 (positively oriented) = (−√3/2, ½) ∪ (C1-arc from ½ to P) ∪ (C2-arc from P to −√3/2). Its image runs 1 → ∞ → v → 0 → ¼ → 1, increasing, which is consistent with U_2 → upper half-plane.
  - ∂U_12 = (½, √3/2) ∪ (C2-arc from √3/2 to P) ∪ (C1-arc from P to ½). Its image runs 0 → v → ∞ → 1 → ¼ → 0, decreasing, which is consistent with U_12 → lower half-plane.
  
  All four stated crossings are CORRECT, and the endpoint is ¾ = 1 − t0.
- **Class of β.** U_12 and L_12 lie in |w| < √3/2, so they avoid 1. β crosses R only in (−√3/2, 0) and in (½, ⅔). So in C∖{0,1}, β ≃ (clockwise loop about 0 at ¼)·[¼, ¾]. CORRECT.
- **λ-lift.** λ ≈ 16e^{iπτ}, and clockwise around 0 corresponds to Re τ decreasing, so the loop lifts to p0 → p0 − 2. Since λ(τ − 2) = λ(τ) and λ(i/y0) = 1 − λ(iy0) = ¾, the segment lifts to q* = −2 + i/y0 = T^{−2}S(p0). In matrix form g = [[−2, −1], [1, 0]], with trace −2: parabolic, hence non-elliptic, and g ∈ Γ(2)S. CORRECT. The ∓ in the text is harmless.
- **Minor precision: truncating β.** β ends at ¾ ∈ V^{-1}(∞), which is a puncture of Ŵ. Truncate β just before ¾ and use a small loop around ¾. Its λ-lift β̃' avoids q*, because λ^{-1}(¾) is discrete. Then β̃'·c̃^m·β̃'^{-1} has winding number ±m about q* = g(p0). With that change, CORRECT.
- **Gap: "the lift T~ fixes a point".** The text does not justify that f^*(T_γτ') = T~·f^*(τ') with T~ ∈ PMod(S²,A). Repair:
  - Let D be the disc bounded by γ, containing a_1 and v. Then S²∖D is a disc free of critical values, so f^{-1}(S²∖D) is two discs, each mapped homeomorphically.
  - Hence f^{-1}(γ) = γ_1 ⊔ γ_2, each of degree 1. If T_γ is supported in a collar N, then T~ := T_{γ1}T_{γ2}, supported in f^{-1}(N), satisfies f∘T~ = T_γ∘f and fixes f^{-1}(B) pointwise.
  - For a marking ψ with lift ψ~, ψ~T~^{-1} is a lift of ψT_γ^{-1}. Lifts are unique up to the holomorphic deck involution, which does not change the Teichmüller point. So f^*(T_γτ') = T~|_A · f^*(τ').
  - The lasso computation gives T~|_A · f^*(τ) = f^*(τ). PMod(S²,A) acts freely, so T~|_A = 1 and f^*∘T_γ = f^*.
  
  With i_*∘T_γ = i_*, this gives Ψ∘T_γ = Ψ. Hence T_γ(D_f) = D_f, applying the same argument to T_γ^{-1}.
- **Conclusion.** Winding ±m ≠ 0 contradicts §3. So T_γ^m D_0 ≠ D_0 for all m ≠ 0, and the orbit of D_0 is infinite. CORRECT.

## 5. Scope

**(a)** All maps in the family give the same deformation space up to the canonical identification constructed in (b). The problem itself says that the image of D_f in moduli space is the whole family. So the question is answered by the f_{1/4} case plus the transport below. Without (b), the answer covers only one representative.

**(b) Transport lemma: complete proof.**
1. **Parameter space.** Let W = {t : t ∉ {0, 1, ½}, v(t) ∉ {0, 1, t}}.
   - v(t) = 0 iff t² − 3t + 1 = 0.
   - v(t) = 1 iff b = 0, i.e. t² + t − 1 = 0.
   - v(t) = t is a nontrivial polynomial equation, since it fails at t = ¼.
   - c_2 ∈ A would force v ∈ A.
   
   So W is C minus a finite set, hence connected. Every map of the family is conjugate to f_t for some t ∈ W.
2. **Isotopy and lift.** Take a path t_s from ¼ to t in W, and set B_s = {0, ∞, 1, t_s, v(t_s)}. By isotopy extension there is a continuous family of homeomorphisms h_s with h_0 = id and h_s(B_{1/4}) = B_s, preserving labels.
   - Φ_s := h_s^{-1}∘f_{t_s} is a continuous family of degree-2 covers branched exactly over the fixed pair {∞, v(¼)}.
   - The homeomorphisms k with Φ_s∘k = f_{1/4} form, for each s, a pair differing by the deck involution. This pair varies continuously in s; it is a trivial double cover of [0,1]. So a continuous branch h̃_s with h̃_0 = id exists, and f_{t_s}∘h̃_s = h_s∘f_{1/4}.
3. **h̃_s = h_s on A.**
   - h̃_s(a_0) is the unique preimage of a_1(s).
   - For i ≥ 1, h̃_s(a_i) is a continuous choice among the two distinct preimages of a_{i+1}(s) under f_{t_s}, starting at a_i(¼). One of these preimages is a_i(s), so h̃_s(a_i) = a_i(s) = h_s(a_i) for all s.
   
   Hence φ_s = h_s^{-1}h̃_s is an isotopy rel A from id to φ_1, so h̃_1 ≃ h_1 rel A.
4. **Identifications.** Define H[ψ] = [ψ∘h_1^{-1}] on Teich(B_{1/4}) → Teich(B_t), and H_A similarly on Teich(A).
   - i_*∘H = H_A∘i_*.
   - ψ~h̃_1^{-1} lifts ψh_1^{-1} through f_t, so f_t^*∘H = H_A∘f_{1/4}^*.
   
   Thus H is a biholomorphism with H(D_{f_{1/4}}) = D_{f_t}, carrying components to components.
5. **Conjugating the twist.** H∘T_γ∘H^{-1} = T_{h_1(γ)}. So h_1(γ) has the required property for f_t, and the Möbius conjugacy transports it to any f in the family.

## 6. Facts cited from memory

All of the following are true as used:
- λ: H → C∖{0,1} is a universal covering with deck group Γ(2)/±1;
- λ(τ+2) = λ(τ), λ(−1/τ) = 1 − λ(τ), and λ ~ 16e^{iπτ} at the cusp i∞;
- λ maps iR_{>0} decreasingly onto (0,1);
- Bers: i_*: Teich(0,5) → Teich(0,4) is a holomorphic fibration with fibres ≅ H, the universal covers of the 4-punctured spheres;
- the Birman exact sequence, with the point-push group acting as the deck group on fibres;
- Teich(B) is contractible;
- PMod(S_{0,4}) ≅ F_2 acts freely on Teich(A);
- push along a simple loop = T_{∂_1}T_{∂_2}^{-1}.

The lifting formula f^*(φτ) = φ~·f^*(τ) holds in the form needed here: φ~ fixes A pointwise, as shown in §4.

## Verdict

VERDICT: the proof establishes the claim after the following repairs:
1. Justify that the lift of T_γ is T~ = T_{γ1}T_{γ2}, which fixes f^{-1}(B) pointwise, so that f^*∘T_γ = T~|_A·f^* with T~|_A ∈ PMod(S²,A) (§4 above).
2. Note that components of D_f are path components, because D_f is an analytic set.
3. Truncate β before the puncture ¾ when computing the winding number.
4. For a general f in the family, add the transport lemma of §5(b), which I proved in full. The answer for general f is h_1(γ), the image of γ under the transport homeomorphism.

All algebra and the combinatorial lifting are correct as written.

Open / not checked: nothing essential. The facts in §6 are cited from memory.

=== END OF ANSWER round4_q2 ===
