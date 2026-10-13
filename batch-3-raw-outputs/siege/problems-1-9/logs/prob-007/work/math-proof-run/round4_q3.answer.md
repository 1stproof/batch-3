# round4_q3: reduction to the model, transport, and the Teichmüller facts

Plan: (A) normal form f_t and the parameter set W; (B) transport from f_{1/4} to every f_t, and from there to an abstract f; (C) precise statements and proofs of the Teichmüller facts. I also flag, and repair, the places where the round-3 proof uses them incorrectly. Throughout, "[mem]" marks a result cited from memory.

Conventions. Ĉ = S². A *marking* of (S², X) (X finite, |X| ≥ 3) is an orientation-preserving homeomorphism φ: S² → Ĉ. Teich(X) is the set of markings modulo φ₁ ~ φ₂, which holds iff there is a Möbius M such that M∘φ₁ = φ₂ on X and M∘φ₁ is isotopic to φ₂ rel X. PMod(S², X) acts on the left by g·[φ] = [φ∘g⁻¹].

---

## (A) Reduction to the model

**Proposition A.** Let f be a quadratic rational map with a critical point c₁ of exact period 4, and suppose v = f(c₂) is not on the cycle of c₁. Then there is exactly one t ∈ W and exactly one Möbius M such that M∘f∘M⁻¹ = f_t and M(c₁) = 0. Here

f_t(z) = 1 + b/z + c/z², with b = (t²+t−1)/(1−t) and c = t(1−2t)/(1−t),

W = C ∖ E, and E = {0, 1, 1/2} ∪ {t²−3t+1 = 0} ∪ {t²+t−1 = 0} ∪ {3t²−3t+1 = 0}.

E has **9** points: 0, 1, 1/2, (3±√5)/2, (−1±√5)/2 and 1/2 ± i/(2√3). These are pairwise distinct. The query's count of "10" is only right if t = ∞ ∈ Ĉ is also counted. Conversely, for every t ∈ W the map f_t has these properties, with c₁ = 0. W is open and connected.

Uniqueness is for the pair (f, c₁). If c₂ also happens to be 4-periodic (on another cycle), the other labelling may give a different t.

**Proof.**

*Existence of the normal form.* Write a_i = f^i(c₁). These four points are distinct, so there is a unique Möbius M with M(a₀, a₁, a₂) = (0, ∞, 1). Put t = M(a₃) ∉ {0, 1, ∞}, and g = M f M⁻¹.

- Since 0 is a critical point of g with g(0) = ∞, g has a double pole at 0 and no other pole. So g = P(z)/z² with deg P ≤ 2 and P(0) ≠ 0.
- g(∞) = 1 forces the z²-coefficient of P to be 1. So g = 1 + b/z + c/z² with c ≠ 0.
- The conditions g(1) = t and g(t) = 0 read 1 + b + c = t and t² + bt + c = 0. Substituting c = t − 1 − b into the second gives b(t−1) = 1 − t − t². Hence b = (t²+t−1)/(1−t) (in particular t ≠ 1), and c = t − 1 − b = t(1−2t)/(1−t).

*Uniqueness.* Suppose M' f M'⁻¹ = f_s with M'(c₁) = 0. Then M' sends the orbit a₀, a₁, a₂, a₃ to the orbit 0, ∞, 1, s of 0 under f_s. So M' agrees with M on three points, M' = M, and s = t.

*Which t occur.* For t ∉ {0, 1}, b and c are finite.
- If t = 1/2 then c = 0 and f_t = 1 + b/z has degree 1. So t ≠ 1/2.
- For t ∉ {0, 1, 1/2} we have c ≠ 0. Then z² and z² + bz + c are coprime, so deg f_t = 2. The orbit 0 → ∞ → 1 → t → 0 consists of distinct points (by the computation above, f_t(1) = t and f_t(t) = 0). So 0 is a critical point of exact period 4.
- Since f_t' = −(bz + 2c)/z³, the second critical point is c₂ = −2c/b if b ≠ 0, and c₂ = ∞ if b = 0.
- b = 0 ⇔ t² + t − 1 = 0. In that case c₂ = ∞ = a₁ lies on the cycle, so v lies on the cycle and t must be excluded.
- Otherwise, v = f_t(c₂) = 1 − b²/(4c) = 1 − (t²+t−1)²/(4t(1−t)(1−2t)). Using (t²+t−1)² − (t²−3t+1)² = (4t−2)(2t²−2t) = 4t(1−t)(1−2t), this becomes

  v(t) = −(t²−3t+1)² / (4t(1−t)(1−2t)).   (A.1)

Now check v against each point of the cycle:
- v = ∞ is impossible for t ∉ {0, 1, 1/2}.
- v = 0 ⇔ t² − 3t + 1 = 0.
- v = 1 ⇔ (t²+t−1)² = 0, which is already excluded.
- v = t ⇔ 4t(1−t)(1−2t) − (t²+t−1)² = 4t²(1−t)(1−2t) ⇔ 4t(1−t)²(1−2t) = (t²+t−1)². Expanding, 4t − 16t² + 20t³ − 8t⁴ = t⁴ + 2t³ − t² − 2t + 1. That is, 9t⁴ − 18t³ + 15t² − 6t + 1 = 0, i.e. (3t²−3t+1)² = 0.

If v ∉ A then c₂ ∉ A automatically, since f(A) = A. So the admissible t are exactly W.

*Connectedness.* W is C minus a finite set, hence open and path-connected. ∎

**Useful formulas** (verified by expanding). For t ∈ W:

c₂(t) = −2t(1−2t)/(t²+t−1),  1 − v(t) = b²/(4c),

f_t(z) = v(t) + (1 − v(t))·(1 − c₂(t)/z)² = M_t(N_t(z)²),   (A.2)

with N_t(z) = z/(z − c₂(t)) and M_t(y) = v(t) + (1 − v(t))/y.

To check (A.2), expand: v + (1−v)(1 − 2c₂/z + c₂²/z²). The 1/z-coefficient is −2(1−v)c₂ = −2(b²/4c)(−2c/b) = b, and the 1/z²-coefficient is (1−v)c₂² = c. Here N_t(c₁ = 0) = 0, N_t(c₂) = ∞, M_t(0) = ∞ = a₁ and M_t(∞) = v(t). The maps N_t and M_t are Möbius (v ≠ 1, c₂ ≠ 0, ∞) and depend continuously (indeed holomorphically) on t ∈ W.

**Real parameters.** By (A.1), for t ∈ (0, 1/2) the denominator 4t(1−t)(1−2t) is positive, so v(t) < 0 unless t = (3−√5)/2 ≈ 0.382. The interval I := (0, (3−√5)/2) contains 1/4 and no point of E. For t ∈ I the real order is

v(t) < a₀ = 0 < a₃ = t < a₂ = 1 < a₁ = ∞,

and v(t) → −∞ as t → 0⁺. At t = 1/4 we get v = −25/96, as in round 3.

---

## (C) The Teichmüller facts (placed before (B), which uses them)

Throughout this section f: S² → S² is an orientation-preserving branched cover of degree d ≥ 2, and A, B ⊂ S² are finite with |A|, |B| ≥ 3.

### C1. The pullback f^*: Teich(B) → Teich(A), assuming f(A) ∪ V(f) ⊂ B

**Construction.** Given a marking φ, pull back the complex structure of Ĉ by φ∘f. Off the finitely many critical points this is a complex structure, and it extends across them, because locally φ∘f looks like z ↦ z^k. By uniformization there is a homeomorphism ψ: S² → Ĉ, unique up to post-composition with a Möbius map, such that F := φ∘f∘ψ⁻¹ is holomorphic, hence a rational map of degree d. Define f^*[φ] := [ψ] ∈ Teich(A).

**Lemma C1 (well-defined).**
1. If ψ is replaced by M∘ψ, the class in Teich(A) does not change.
2. Suppose φ' = M∘φ∘θ, where M is Möbius and θ is isotopic to id rel B through θ_s. Then the isotopy θ_s lifts to an isotopy θ̃_s with f∘θ̃_s = θ_s∘f and θ̃₀ = id. Each θ̃_s fixes f⁻¹(B) pointwise, and one may take ψ' = ψ∘θ̃₁. So [ψ'] = [ψ] in Teich(f⁻¹(B)), and a fortiori in Teich(A) since A ⊂ f⁻¹(B).

*Proof.*
1. This is immediate from the definition.
2. f restricts to a covering S² ∖ f⁻¹(V) → S² ∖ V, where V = V(f) ⊂ B, and each θ_s fixes V pointwise. By the homotopy lifting property, the map (s, x) ↦ θ_s(f(x)) on [0,1] × (S² ∖ f⁻¹(V)) lifts to a continuous θ̃ with θ̃₀ = id.
   - Each θ̃_s is a homeomorphism of S² ∖ f⁻¹(V), being a lift of a homeomorphism that is connected by lifting to the identity. It extends continuously by the identity on f⁻¹(V): near a critical point the lift of a map fixing the critical value fixes the critical point.
   - For x ∈ f⁻¹(B), θ̃_s(x) ∈ f⁻¹(f(x)), which is a finite set, and s ↦ θ̃_s(x) is continuous. So θ̃_s(x) = x.
   - Finally φ'∘f = M∘φ∘θ₁∘f = M∘φ∘f∘θ̃₁ = (M∘F)∘(ψ∘θ̃₁). Since M∘F is rational, ψ' := ψ∘θ̃₁ is a valid choice. ∎

(f^* is holomorphic and contracts the Teichmüller metric (Douady–Hubbard [mem]). Only continuity is needed below, and it follows from the fact that the solution of the Beltrami equation depends continuously on the coefficient.)

### C2. Equivariance, and the error in round 3

**Lemma C2.** Let φ: S² → S² be a homeomorphism fixing B pointwise, and let φ̃ be a homeomorphism with f∘φ̃ = φ∘f. Then for every marking ψ₀,

f^*[ψ₀∘φ⁻¹] = [ψ∘φ̃⁻¹], where ψ represents f^*[ψ₀].

In particular, *if φ̃ fixes A pointwise*, then f^*(φ·τ) = φ̃·f^*(τ), with φ̃ ∈ PMod(S², A).

*Proof.* From f∘φ̃ = φ∘f we get φ⁻¹∘f = f∘φ̃⁻¹. Hence ψ₀∘φ⁻¹∘f = ψ₀∘f∘φ̃⁻¹ = F∘(ψ∘φ̃⁻¹). ∎

**Correction to round 3.** Round 3 states "for φ ∈ PMod(S², B) there is a lift φ̃ … and f^*(φτ) = φ̃·f^*(τ)" with φ̃ ∈ PMod(S², A). This is not correct in general.
- For a ∈ A, φ̃(a) is only known to lie in f⁻¹(f(a)). In our setting each a_i (i = 1, 2, 3) has a second preimage-mate a_i' ≠ a_i with f(a_i') = f(a_i). A lift of a homeomorphism fixing B can exchange a_i and a_i'. Then φ̃ does not even preserve A, and the right-hand side is not of the form g·f^*(τ) with g ∈ PMod(S², A).
- It is true that if φ is *isotopic to the identity rel B*, the lift obtained by lifting the isotopy fixes f⁻¹(B) pointwise (Lemma C1). But the twist T_γ is not isotopic to the identity rel B.

Round 3 uses equivariance only for T_γ. The repair is to exhibit an explicit lift of T_γ that fixes A pointwise.

**Lemma C2' (lift of T_γ).** Let f be quadratic as in the problem. Let α ⊂ S² be a simple arc from v to a₁ (the two critical values) with interior disjoint from B, and let γ = ∂N, where N is a closed regular neighbourhood (a disc) of α disjoint from B ∖ {v, a₁}. Let R ⊂ S² ∖ N be a closed collar annulus adjacent to γ, disjoint from B, and realise T_γ as a twist supported in R. Then:
1. f⁻¹(R) = R₁ ⊔ R₂, and each R_j is mapped homeomorphically onto R by f.
2. T̃ := (f|_{R_j})⁻¹∘T_γ∘f on R_j (j = 1, 2), and T̃ := id elsewhere, is a homeomorphism with f∘T̃ = T_γ∘f.
3. T̃ fixes f⁻¹(B) pointwise, in particular A. It equals T_{γ̃₁}T_{γ̃₂}, where γ̃_j is the core of R_j.

Hence, by Lemma C2, f^*(T_γ·τ) = T̃·f^*(τ) for all τ ∈ Teich(B), with T̃ ∈ PMod(S², A).

*Proof.*
1. R contains no critical value, so f: f⁻¹(R) → R is a 2-sheeted covering. Its monodromy along the core of R, which is homotopic to γ, is the product of the local monodromies around the two critical values enclosed by γ. Each of these is the transposition of the two sheets, and the product is trivial. So the covering is trivial: two components, each mapped homeomorphically.
2. T_γ = id on ∂R, so T̃ is continuous on S². It is bijective, and a continuous bijection of S² is a homeomorphism. The identity f∘T̃ = T_γ∘f holds on each R_j by construction and elsewhere trivially.
3. f⁻¹(B) ∩ f⁻¹(R) = ∅, so T̃ fixes f⁻¹(B) pointwise. f is orientation-preserving, so T̃|_{R_j} is a positive twist about γ̃_j. ∎

### C3. Free action

**Lemma C3.** PMod(S², X) acts freely on Teich(X) when |X| ≥ 3.

*Proof.* Suppose g·[φ] = [φ], i.e. [φ∘g⁻¹] = [φ]. Then there is a Möbius M with M∘φ = φ∘g⁻¹ on X, and M∘φ isotopic to φ∘g⁻¹ rel X. Since g fixes X pointwise, M fixes the ≥ 3 points of φ(X), so M = id. Then φ∘g⁻¹ ≃ φ rel X, i.e. g⁻¹ ≃ id rel X, so g = 1 in PMod(S², X). ∎

(No Γ(2) argument is needed. This repairs nothing, but it makes the step "T̃ fixes a point, hence T̃ = 1" in round 3 §4 self-contained.)

### C4. Teich(A) ≅ H and the λ-function

**λ facts [mem].** The modular function λ: H → C ∖ {0, 1} is a holomorphic universal covering. Its fibres are exactly the orbits of Γ(2), which acts through Γ(2)/{±I}. Moreover:
- λ(τ+2) = λ(τ) and λ(−1/τ) = 1 − λ(τ);
- λ(τ) = 16q − 128q² + O(q³), with q = e^{iπτ}, as Im τ → ∞;
- λ(i) = 1/2, and y ↦ λ(iy) is a strictly decreasing bijection (0, ∞) → (0, 1).

So λ(q) = λ(−1/p) = 1 − λ(p) iff q ∈ Γ(2)·S(p). Every element of Γ(2) has even trace, and trace 0 is impossible: a ≡ d ≡ 1 (mod 2) and ad − bc = 1 with b, c even force ad ≡ 1 (mod 4), whereas d = −a would give ad = −a² ≡ −1 (mod 4). So Γ(2)/{±I} has no elliptic elements.

**Identification.** Let X = {x₀, x₁, x₂, x₃}. The modulus map mod: Teich(X) → C ∖ {0, 1} sends [φ] to the cross-ratio t for which some Möbius M gives M∘φ(x₀, x₁, x₂, x₃) = (0, ∞, 1, t).
- Teich(X) is simply connected, indeed homeomorphic to a disc (Teichmüller's theorem [mem]).
- mod is the quotient by the free (Lemma C3) and properly discontinuous ([mem]) action of PMod(S², X). Hence it is a universal covering.

So there is a biholomorphism Θ: Teich(X) → H with λ∘Θ = mod. Θ is unique once Θ of one base point is chosen. For the base point [id] of f_{1/4} we choose Θ([id]) = p₀ := iy₀, where λ(iy₀) = 1/4.

### C5. Contractibility, the forgetful map, and the fibres

**Contractibility [mem, Teichmüller's theorem].** Teich(S², n points) is homeomorphic to R^{2(n−3)}, hence contractible. In particular Teich(B) ≅ R⁴.

**The forgetful map.** i_*[φ] = [φ] viewed rel A. This is well-defined, because an isotopy rel B is an isotopy rel A. It is equivariant: i_*(g·τ) = i(g)·i_*(τ), where i: PMod(S², B) → PMod(S², A) forgets v.

**Fibres (Bers fibration / Birman exact sequence [mem]).** Fix p ∈ Teich(A) and a representative φ_p normalised with φ_p(a₀, a₁, a₂) = (0, ∞, 1), and put A_p = φ_p(A). Then:
- The fibre i_*⁻¹(p) is homeomorphic to the universal cover of Ĉ ∖ A_p. The homeomorphism sends [φ] (normalised so that φ ≃ φ_p rel A by an isotopy φ_s, which is unique up to homotopy because Homeo₀(S², A) is contractible for |A| ≥ 3 [mem, Hamstrom]) to the homotopy class of the path s ↦ φ_s(v).
- The point-push subgroup ker(i) ≅ π₁(S² ∖ A, v) acts on the fibre as the deck group.
- In particular each fibre is connected and simply connected.

**Local coordinates.** Consider the map Teich(B) → M_{0,5} = {(t, v') : t ∈ C ∖ {0, 1}, v' ∈ C ∖ {0, 1, t}}, which records the normalised positions of a₃ and v. It is the quotient by the free, properly discontinuous action of PMod(S², B), hence a covering map. So (t, v') are local coordinates on Teich(B).

### C6. D_f is a smooth complex curve (needed so that components = path components)

Round 3 §3 picks a path σ ⊂ D₀ from τ to T^mτ inside a *connected component* D₀ of D_f. This silently assumes that components of D_f are path-connected. This is a gap rather than an error, and it is closed as follows.

**Lemma C6.** For f = f_t (t ∈ W), D_f is a 1-dimensional complex submanifold of Teich(B). Near each of its points, in the local coordinates (t', v'), it is the graph {v' = v(t')} of the holomorphic function (A.1). Consequently D_f is locally path-connected, and its connected components are path components. Moreover, the coordinate t' restricted to D_f is a local homeomorphism D_f → W.

*Proof.*
- By the fibre formula of round 3 §2 (re-derived below in Lemma C7), the modulus of f^*(τ') is a number w satisfying V_{t'}(w) = v', where (t', v') are the coordinates of τ'.
- Let τ₁ ∈ D_f with coordinates (t₁, v₁). Then w(τ₁) = λ(f^*τ₁) = λ(i_*τ₁) = t₁, so v₁ = V_{t₁}(t₁) = v(t₁). Hence t₁ ∈ W, because v₁ ∉ {0, 1, t₁, ∞}.
- The critical values of V_{t₁} lie in {0, 1, t₁, ∞}. To see this, fix v' ∉ {0, 1, t₁, ∞}.
  - The solutions of V_{t₁}(w) = v' are the values w(ε) = (s₃−s₂)/(s₀−s₂) for the 8 sign choices of (s₂, s₃, s₀) in Lemma C7. A global sign change does not alter w, so there are at most 4 values.
  - These 4 values are distinct. Suppose two sign classes give the same w. Then there is an affine L with L(s_j) = ±s_j (j = 2, 3, 0), with the sign pattern not ± a constant. The quadratic polynomial L(z)² − z² vanishes at the three distinct points s₂, s₃, s₀ (their squares 1−v', t₁−v', −v' are distinct). So L(z)² ≡ z², i.e. L(z) = ±z, a contradiction.
  - V_{t₁} has degree 4 (numerator of degree 4 coprime to the denominator, by the zero/pole computation in C7). So v' has 4 distinct preimages and is not a critical value.

  Since v₁ is not among {0, 1, t₁, ∞}, V_{t₁} is a local biholomorphism near w = t₁.
- By continuity of f^*, near τ₁ the function w(τ') is the branch of V_{t'}⁻¹(v') through t₁, which is holomorphic in (t', v').
- f^*τ' and i_*τ' are both near the common value f^*τ₁ = i_*τ₁, and λ is injective near that point. So near τ₁ the condition f^*τ' = i_*τ' is equivalent to λ(f^*τ') = λ(i_*τ'), i.e. w(t', v') = t', i.e. v' = V_{t'}(t') = v(t').
- That is a graph over a neighbourhood of t₁ in W. ∎

### C7. The fibre formula and (★)

**Lemma C7 (round 3 §2, checked).** For τ' with coordinates (t, v'), w := λ(f^*τ') satisfies

V_t(w) = −((w−1)² − t)² / (4w(w−1)(w+t−1)) = v'.

Consequently λ(f^*τ') ≠ 1 − λ(i_*τ') for all τ' ∈ Teich(B).   (★)

*Proof.*
- The pulled-back structure is realised by F(z) = v' + z². Its critical points are ∞ ↦ ∞ = a₁ and 0 ↦ v', and the marked preimages are a₀' = ∞, a₁' = s₂, a₂' = s₃, a₃' = s₀, where s₂² = 1 − v', s₃² = t − v', s₀² = −v' (signs fixed by the marking). One checks F(a_i') = a_{i+1}.
- The Möbius map z ↦ (s₃ − s₂)/(z − s₂) sends (∞, s₂, s₃, s₀) to (0, ∞, 1, w), with w = (s₃ − s₂)/(s₀ − s₂).
- Put u = s₂ − s₀ and U = u². Since s₂² − s₀² = 1, we get s₂ = (u + 1/u)/2 and s₀ = (1/u − u)/2. Also s₃ = s₂ − wu.
- Then s₃² − s₀² = t reads 1 − w(U+1) + w²U = t, so U = (w+t−1)/(w(w−1)), and 1 − U = ((w−1)² − t)/(w(w−1)).
- Hence v' = −s₀² = −(1−U)²/(4U), which gives the formula.
- At w = 1 − t the denominator vanishes and the numerator is (t² − t)² ≠ 0. So V_t(1−t) = ∞ = a₁ ≠ v'. Hence w ≠ 1 − t = 1 − λ(i_*τ'). ∎

(As a sanity check, V_t(t) = −(t²−3t+1)²/(4t(t−1)(2t−1)), which equals v(t) of (A.1).)

### C8. Remaining checks of the round-3 argument

1. **Point push.** "T_γ is the point push of v around the lasso ℓ = α'·(small loop around a₁)·α'⁻¹, and i(T_γ) = 1." This is correct. Push(ℓ) = T_{δ₁}T_{δ₂}⁻¹, where δ₁ and δ₂ are the boundary curves of a regular neighbourhood of ℓ ([mem], Farb–Margalit, Fact 4.7). Here δ₂ bounds a disc containing only a₁, so its twist is trivial, and δ₁ = γ. Forgetting v, γ bounds a disc containing only a₁, so i(T_γ) = 1.

2. **"T_γ preserves D_f."** Correct, after the repair in C2'. Round 3 shows that on the fibre over p₀, f^*(T_γτ') = f^*(τ') for τ' in that fibre: the lifted lasso closes up in H. By C2', the left side equals T̃·f^*(τ') with T̃ ∈ PMod(S², A). By C3, T̃ = 1. Hence f^*∘T_γ = f^* on all of Teich(B), and with i_*∘T_γ = i_* this gives Ψ∘T_γ = Ψ, so T_γ(D_f) = D_f.

   (The same argument shows that the two boundary curves γ̃₁ and γ̃₂ of the annulus f⁻¹(N) are both inessential in (S², A). One of the two complementary discs contains a₁, a₂, a₃, and the annulus contains a₀ = c₁.)

3. **The linking argument (§3).** Correct, given C6 (components are path components), C5 (the fibre is simply connected, Teich(B) is contractible) and (★). The class of a loop in {p₀} × (H ∖ {g(p₀)}) in H₁(X_g) ≅ Z is its winding number about g(p₀). The map (p, q) ↦ (p, (q − Re g(p))/Im g(p)) restricts on each fibre to an orientation-preserving affine map, so it preserves winding numbers.

   One precision is needed. The fibre loop must be homotoped *inside H ∖ λ⁻¹(1 − t₀)*, not merely inside H. This is legitimate: f^* maps the whole fibre into H ∖ λ⁻¹(1 − t₀) by (★), and the fibre is simply connected. So σ' may be replaced by any path in the fibre with the same endpoints. Take one whose projection is the loop ℓ^{±m} through the truncated arc α' (stopping just before a₁). Its image under f^* is β̃'·c̃^{±m}·β̃'⁻¹, where c̃ is a small positively oriented Jordan curve around q* = g(p₀); λ is locally biholomorphic there. Its winding number about g(p₀) is ±m ≠ 0.

4. **The group element.** g = T^{∓2}S has matrix [[∓2, −1], [1, 0]] and trace ∓2, so it is parabolic, has no fixed point in H, and Γ_g ∩ Δ = ∅. This is correct. Note that the argument genuinely needs the specific g: S ∈ Γ(2)S itself is elliptic (it fixes i).

5. **Base point.** Since f_{1/4} is rational, f_{1/4}^*[id] = [id] = i_*[id]. So τ₀ = [id] ∈ D_f, and its i_*-image is p₀ by the choice of Θ in C4.

I found no other incorrect uses. The §4 lifting computation, which is specific to t₀ = 1/4, was not re-audited in this round beyond spot checks. These were: the factorisation at t = 1/4, ((w−1)² − 1/4) = (w − 1/2)(w − 3/2) and w + t − 1 = w − 3/4; the values λ(i/y₀) = 3/4; and the direction of lifts near i∞, where a counter-clockwise loop about 0 lifts to τ ↦ τ + 2.

---

## (B) Naturality and transport

Fix t ∈ W and a path t_s (s ∈ [0, 1]) in W from t₀ = 1/4 to t₁ = t. Write B_s = {a₀ = 0, a₁ = ∞, a₂ = 1, a₃ = t_s, v_s = v(t_s)}. These are five distinct points depending continuously on s, labelled. Write f_s := f_{t_s} and A_s = B_s ∖ {v_s}.

### B1. The isotopy h_s

**Lemma B1.** There is an isotopy h_s of S² (continuous in (s, z) together with its inverse) with h₀ = id and h_s fixing 0, 1, ∞, such that h_s(t₀) = t_s and h_s(v₀) = v_s.

*Proof.* We use a disc-push.
- For |q| < 1 the map P_q(z) = z + (1 − |z|)q is a homeomorphism of the closed unit disc D̄ that is the identity on ∂D and sends 0 to q.
  - Injective: P_q(z) = P_q(z') gives z − z' = (|z| − |z'|)q, so |z − z'| ≤ |z − z'|·|q|, hence z = z'.
  - Surjective: by invariance of domain the image of the open disc is open. It is also closed in the open disc, because |P_q(z)| ≤ |z| + (1 − |z|)|q| < 1 for |z| < 1 and the boundary is fixed. So it is everything.
  - (q, z) ↦ (q, P_q(z)) is a continuous bijection of {|q| ≤ ρ} × D̄ (ρ < 1), a compact Hausdorff space, hence a homeomorphism. So P_q⁻¹ is jointly continuous too.
- Choose a partition 0 = σ₀ < … < σ_N = 1 and radii r > 0 such that, for each k:
  - the discs D(t_{σ_k}, r) and D(v_{σ_k}, r) are disjoint from each other and from {0, 1};
  - for s ∈ [σ_k, σ_{k+1}], |t_s − t_{σ_k}| < r/2 and |v_s − v_{σ_k}| < r/2.
  This is possible by uniform continuity.
- On [σ_k, σ_{k+1}] put h_s = (push in D(t_{σ_k}, r) from t_{σ_k} to t_s) ∘ (push in D(v_{σ_k}, r) from v_{σ_k} to v_s) ∘ h_{σ_k}. Each push is a conjugate of P_q∘P_{q'}⁻¹ by an affine map, and is the identity outside its disc. ∎

### B2. The lift h̃_s

**Lemma B2.** There is a continuous family of homeomorphisms h̃_s with f_s∘h̃_s = h_s∘f₀, h̃₀ = id, and h̃_s = h_s on A₀ for all s.

*Proof.* Use (A.2): f_s = M_s∘Q∘N_s, with Q(z) = z², M_s := M_{t_s} and N_s := N_{t_s} continuous in s.
- Put k_s := M_s⁻¹∘h_s∘M₀. Then k₀ = id. Since h_s fixes ∞ and sends v₀ to v_s, and M_s(0) = ∞, M_s(∞) = v_s, we get k_s(0) = 0 and k_s(∞) = ∞.
- *Lifting through Q.* Consider K: [0,1] × C* → C*, K(s, z) = k_s(z²). Since [0,1] × C* deformation retracts to {0} × C*, where K = Q, we have K_*(π₁) ⊂ Q_*(π₁(C*)) = 2Z. So K lifts through the covering Q: C* → C* to a continuous k̃ with k̃₀ = id; the lift is unique given k̃(0, 1) = 1. Write k̃_s := k̃(s, ·).
- *k̃_s is odd.* The maps (s, z) ↦ k̃_s(−z) and (s, z) ↦ −k̃_s(z) are both lifts of K and agree at (0, 1). So k̃_s(−z) = −k̃_s(z).
- *k̃_s is a homeomorphism.* It is injective: k̃_s(z) = k̃_s(z') implies z'² = z², so z' = ±z, and z' = −z is ruled out by oddness. It is surjective: given y, pick z with z² = k_s⁻¹(y²); then k̃_s(z) = ±y, and oddness gives y. Since |k̃_s(z)|² = |k_s(z²)|, setting k̃_s(0) = 0 and k̃_s(∞) = ∞ gives a continuous bijection of S², jointly continuous in (s, z) because k is uniformly continuous on [0,1] × Ĉ. So it is a homeomorphism.
- Put h̃_s := N_s⁻¹∘k̃_s∘N₀. Then f_s∘h̃_s = M_s Q k̃_s N₀ = M_s k_s Q N₀ = h_s M₀ Q N₀ = h_s∘f₀, and h̃₀ = id.
- *Agreement on A₀.*
  - h̃_s(a₀): f_s(h̃_s(a₀)) = h_s(a₁) = ∞, and f_s⁻¹(∞) = {0}. So h̃_s(0) = 0 = h_s(0).
  - For i = 1, 2, 3: f_s(h̃_s(a_i)) = h_s(a_{i+1}) = a_{i+1}(s). The point a_{i+1}(s) ∈ {1, t_s, 0} is not a critical value of f_s (those are ∞ and v_s). So its preimage consists of two distinct points: a_i(s), and a_i'(s) := the other one. Both depend continuously on s as points of Ĉ. Each is a simple preimage, so by the argument principle (or the implicit function theorem in a chart at ∞, where a₁ = ∞ is one of the preimages of a₂ = 1) it moves continuously with (s, value).
  - s ↦ h̃_s(a_i) is a continuous selection from {a_i(s), a_i'(s)} that equals a_i(0) at s = 0. So it equals a_i(s) = h_s(a_i) for all s. ∎

### B3. The comparison homeomorphism is isotopic to the identity

**Lemma B3.** h₁⁻¹∘h̃₁ is isotopic to id rel A₀.

*Proof.* κ_s := h_s⁻¹∘h̃_s is a homeomorphism, jointly continuous in s (B1, B2). It fixes A₀ pointwise for each s (B2), and κ₀ = id. So κ_s is an isotopy rel A₀ from id to κ₁. ∎

### B4. Transport of D_f and of the twist

Let h = h₁ and h̃ = h̃₁. Define the change-of-marking maps

h^*: Teich(B_t) → Teich(B₀), [φ] ↦ [φ∘h],

and similarly h^*: Teich(A_t) → Teich(A₀). These are well-defined: an isotopy rel B_t precomposed with h is an isotopy rel B₀. They are bijective, with inverse (h⁻¹)^*. They are isometries of the Teichmüller metrics, because the quasiconformal maps compared are the same. So they are homeomorphisms.

**Proposition B4.**
1. i_*∘h^* = h^*∘i_*, and f₀^*∘h^* = h^*∘f_t^*.
2. Hence h^*(D_{f_t}) = D_{f₀}, and h^* induces a bijection π₀(D_{f_t}) → π₀(D_{f₀}).
3. For every g ∈ PMod(S², B₀), h^*∘(hgh⁻¹) = g∘h^*. In particular h^*∘T_{h(γ)} = T_γ∘h^*.

*Proof.*
1. The first identity is trivial. For the second, let ψ represent f_t^*[φ], so that φ∘f_t = F∘ψ with F rational. Then φ∘h∘f₀ = φ∘f_t∘h̃ = F∘(ψ∘h̃). So f₀^*[φ∘h] = [ψ∘h̃] = [ψ∘h∘(h⁻¹h̃)] = [ψ∘h], by Lemma B3; and [ψ∘h] = h^*f_t^*[φ].
2. Using part 1, [φ] ∈ D_{f_t} ⇔ f_t^*[φ] = i_*[φ] ⇔ h^*f_t^*[φ] = h^*i_*[φ] ⇔ f₀^*(h^*[φ]) = i_*(h^*[φ]) ⇔ h^*[φ] ∈ D_{f₀}. A homeomorphism carries components onto components.
3. h^*(hgh⁻¹·[φ]) = [φ∘hg⁻¹h⁻¹∘h] = [(φ∘h)∘g⁻¹] = g·h^*[φ]. Finally hT_γh⁻¹ = T_{h(γ)}, because h is orientation-preserving (it is isotopic to id). ∎

**Corollary B5 (the answer for every f_t).** Let γ be the round-3 curve for f_{1/4}, and suppose T_γ^k preserves D_{f_{1/4}} and has an infinite orbit on π₀(D_{f_{1/4}}). (Round 3 claims this with k = 1, proved modulo the §4 computation and the repairs of (C).) Then γ_t := h₁(γ) is a simple closed curve in (S², B_t) such that T_{γ_t}^k preserves D_{f_t} and has an infinite orbit on π₀(D_{f_t}).

Like γ, the curve γ_t bounds a disc containing exactly v_t and a₁ = f_t(c₁): it is the boundary of a regular neighbourhood of the arc h₁(α).

*Proof.* By B4, h^* conjugates the action of T_{γ_t} on Teich(B_t) to the action of T_γ on Teich(B₀), and maps D_{f_t} onto D_{f₀}, components to components. ∎

The curve h₁(γ) depends on the homotopy class of the path t_s in W (monodromy), but every choice works.

### B6. Explicit description for real t ∈ I = (0, (3−√5)/2)

Take the path t_s ⊂ I as the real segment from 1/4 to t. Along it the order v_s < 0 < t_s < 1 is preserved (Section A), and v_s stays in a compact subset of (−∞, 0), say v_s > −R + 1.

Let φ_s: R → R be the increasing piecewise-linear map with nodes −R ↦ −R, v₀ ↦ v_s, 0 ↦ 0, t₀ ↦ t_s, 1 ↦ 1, equal to the identity outside [−R, 1]. Put H_s(x + iy) = φ_s(x) + iy and H_s(∞) = ∞.
- H_s is a homeomorphism of C. Since |H_s(z) − z| ≤ R + 1, it extends continuously to Ĉ.
- H_s is jointly continuous in s, with H₀ = id.
- It fixes 0, 1, ∞, and sends t₀ ↦ t_s, v₀ ↦ v_s.
- It preserves R and each open half-plane, and it maps each interval between consecutive marked points onto the corresponding interval.

Use h_s := H_s in B2–B4. (B2 and B3 only need some isotopy with the labelled endpoints.) Then h₁(α) is a simple arc from v_t to ∞ with the same crossing pattern as α. Explicitly, the arc α_t:
1. leaves v_t into the lower half-plane and crosses R upward at a point of (1, ∞);
2. runs in the upper half-plane and crosses downward at a point of (0, t);
3. runs in the lower half-plane and crosses upward at a point of (v_t, 0);
4. stays in the upper half-plane until it reaches ∞.

**The crossing pattern determines the arc up to isotopy rel B_t.** Suppose two such arcs are transverse to R with the same crossing data. First, a homeomorphism of the type H above, preserving R, the half-planes and the marked points, moves the crossing points of one arc to those of the other. Then in each closed half-plane (a disc) the arc pieces form disjoint chords with the same endpoints. Disjoint families of chords with the same endpoint pairs in a disc are ambient isotopic rel boundary, by the Schoenflies theorem applied piece by piece [mem, standard].

So for t ∈ I the answer is the same picture as for t = 1/4, with 1/4 replaced by t: γ_t = ∂(thin neighbourhood of α_t). It encloses exactly v_t and f_t(c₁) = ∞.

### B7. f given abstractly

Let f be as in the problem, M the Möbius map of Proposition A, and t = M(f³(c₁)). Then M∘f = f_t∘M, M(B_f) = B_t, and M(A_f) = A_t labelled. In B4, take h = M (as a map from (S², B_f) to (S², B_t)) and h̃ = M; then f_t∘M = M∘f and h⁻¹h̃ = id. Proposition B4, with f in place of f₀, shows that M^* conjugates T_{γ_t} to T_{M⁻¹(γ_t)} and carries D_{f_t} onto D_f.

**So for f, the curve is γ_f := M⁻¹(γ_t) = M⁻¹(h₁(γ)).** In words, it is the boundary of a thin neighbourhood of an arc from v to f(c₁), and the arc is M⁻¹ of the arc described above. For t ∈ I, this arc is described as follows.
- Let C := M⁻¹(R̂), the circle through c₁, f(c₁), f²(c₁), f³(c₁) and v. These five points are cocircular exactly when t ∈ R, and for t ∈ I they appear on C in the cyclic order v, c₁, f³(c₁), f²(c₁), f(c₁).
- Let the "upper" side of C be M⁻¹ of the upper half-plane. Equivalently, it is the side to the left when C is traversed in the cyclic order c₁ → f³(c₁) → f²(c₁) → f(c₁).
- The arc leaves v into the lower side and crosses C into the upper side between f²(c₁) and f(c₁) (the arc of C not containing c₁). It crosses back into the lower side between c₁ and f³(c₁), crosses into the upper side again between v and c₁, and then runs in the upper side to f(c₁).

---

## Summary / status

**Proved here.**
- (A) Normal form with uniqueness for the pair (f, c₁). The excluded set E consists of exactly 9 finite values; the query's "10" counts ∞. W is connected. The factorisation f_t = M_t∘Q∘N_t. On the real interval I = (0, (3−√5)/2) the order v < 0 < t < 1 holds.
- (B) The isotopy h_s (B1); the lift h̃_s with h̃_s = h_s on A₀ (B2); h₁⁻¹h̃₁ ≃ id rel A₀ (B3); h^* carries D_{f_t} onto D_{f_{1/4}} and conjugates T_{h(γ)} to T_γ (B4). Hence the curve h₁(γ), and M⁻¹h₁(γ) for an abstract f, has the required property whenever γ has it for f_{1/4} (B5, B7). For t ∈ I the explicit crossing-pattern description holds (B6).
- (C)
  - Well-definedness of f^* (C1).
  - Equivariance (C2). The round-3 claim that every φ ∈ PMod(S², B) has a lift in PMod(S², A) is **incorrect** in general, since a lift may swap a_i with its preimage-mate. It is repaired by an explicit lift of T_γ supported near f⁻¹(γ) (C2').
  - Free action of PMod (C3), with an elementary proof.
  - The Teich(A) ≅ H identification (C4).
  - D_f is a smooth complex curve, locally the graph v' = v(t'), so its components are path components (C6). This closes a gap in round-3 §3.
  - (★) via the fibre formula (C7), re-derived.
  - The winding-number step must be done in H ∖ λ⁻¹(1−t₀), which is legitimate by (★) (C8.3).

**Cited from memory, not proved:**
- the λ-function facts;
- Teichmüller's theorem (Teich ≅ R^{2(n−3)});
- the Bers fibration / Birman exact sequence (fibre = universal cover, point pushes = deck group);
- the contractibility of Homeo₀(S², A) (Hamstrom);
- the proper discontinuity of the PMod action;
- the point-push formula Push(ℓ) = T_{δ₁}T_{δ₂}⁻¹;
- the isotopy classification of disjoint chord families in a disc;
- the holomorphy of f^* (only continuity is used).

**Not re-audited in this round:** the t₀ = 1/4 lifting computation of round-3 §4 (the face structure of V⁻¹(R) and the path of the lift β). Only spot checks were done (C8). The final result for all f depends on it through Corollary B5.

=== END OF ANSWER round4_q3 ===
