# round13_q9 — verification of round12_q9 (Lemma CS, CL, J0, 1.1, Prop. T, Lemma R*′, Theorem RO, Prop. C)

**Plan/status line (written first).** I read the whole brief, including round12_q9 verbatim. I check each lemma inference by inference, in the order CS, CL, J0, 1.1 (with O_t, h̃_t, θ_t), Prop. T, R*′, RO, Prop. C. Then I give the verdicts.

**Status at the end.**
- No fatal gap found.
- Three minor repairs are needed, all supplied below:
  - (R1′) finite type of Ê_t: the argument given is incomplete, and is repaired by algebraicity;
  - (R2′) the definition of the torsion-free level subgroups Mod_w[N] in genus 0 and type (1,1);
  - (R3′) the labelled lift φ̂(i) = P̂ in non-product strata: repaired by Aut(G)-relabelling.
- Proposition C's non-product clause is only a sketch.
- Every external input is cited from memory, by me as in round12_q9: Bers, Thurston, Royden, Selberg, Imayoshi–Shiga, orbifold uniformisation, Cartan.
- Theorem RO also depends on prior results that I did not re-check because they are not spliced: TV items 1–3 (the proofs of round8_q10 §4, Steps 2′–5) and Lemma PA. It also depends on the reading (R2^orb) in its global form (a)–(d).

Notation is that of round12_q9. "✓" means I checked the inference and it is valid.

---

## 1. Lemma CS — correct

- Q = ∪_{g∈Γ} Z_g with Z_g = {F′ = gF}. Each Z_g is the coincidence set of two holomorphic maps into a manifold, so it is closed analytic. Γ is countable and Q is a Baire space, so some Z_g has interior. Q is connected, so the identity theorem gives F′ ≡ gF. ✓
- If gF ≡ g′F, then g^{-1}g′ ∈ S_F. So the solution set is the coset gS_F. ✓
- S_F ⊂ Stab_Γ(F(y)), which is finite because the action is properly discontinuous. ✓

## 2. Lemma CL — correct

- **Chart.** Stab_Γ(x̂) = A is finite. Cartan's linearisation gives an A-invariant ball B with linear A-action. By proper discontinuity, B can be shrunk so that gB ∩ B ≠ ∅ ⇒ g ∈ A. By the definition of Cartan's quotient structure, B/A → X is an open embedding. ✓
- **Holomorphy of σ̄∘h.** The A-invariant polynomials σ_k are A-invariant holomorphic functions on B. By definition of the quotient structure sheaf, they are holomorphic functions on B/A. So σ̄∘h is holomorphic on Q_0, since h(Q_0) = p(L(Q_0)) ⊂ B/A. ✓ (The embedding property of σ̄ is not needed. Only two facts are used: σ separates A-orbits, which holds for finite groups, and σ_k descends.)
- **Z.** Z is analytic, and its fibre over y is {b ∈ B : σ(b) = σ(L(y))} = A·L(y), because σ separates orbits. ✓
- **Properness.** For compact K ⊂ Q_0, Z ∩ (K × B) is a closed subset of K × A·L(K), which is compact. ✓
- **Σ is discrete.** Sing Z and the 0-dimensional part are closed and discrete. On Reg Z the critical points of the projection are discrete, since a 1-dimensional component of critical points would be a curve on which the projection is constant, i.e. a curve inside a finite fibre. Images of closed discrete sets under a proper finite map are closed and discrete. ✓
- **Covering.** Over Q_0∖Σ, Z is a 1-manifold mapping by a proper local biholomorphism, hence a finite covering whose sheets are graphs of holomorphic maps. ✓
- **Conclusion.** y ↦ (y, L(y)) is a continuous section. Over a connected evenly covered disc it stays in one sheet, so L is holomorphic off Σ. L is bounded in the ball coordinates and continuous, so Riemann's extension theorem makes it holomorphic on Q_0. ✓

## 3. Lemma J0 — correct, given TV items 1–3 and Corollary Φ̂ as stated (one minor repair in non-product strata)

### 3.1 What TV and Φ̂ actually state, against what J0 quotes

**(a) Is there a continuous Φ : H → T_G with 1-Lipschitz coordinates?**
- Yes. Corollary Φ̂ gives, along a subsequence, maps φ̂_w : H → T(Σ_w), each 1-Lipschitz from d_H (curvature −4) to d_T.
- Put Φ := (φ̂_w)_w. It is continuous, and p∘Φ = ([φ̂_w])_w = φ̂.
- Φ̂ also states φ̂(H) ⊂ Â, using that X^g_n ∈ V_0 by total geodesy. ✓

**(b) pr_j∘Φ = D?**
- Φ̂ states: "if moreover v carries positive area η_v, then … φ̂_v = D (as maps to T(Σ_v))".
- The proof of TV supplies positive area at the vertex j, via Lemma PA (cited from memory in round8_q10) and Lemma TR. TV's D is the Teichmüller disc of (Y_j, η_j) with Y_j = P̃_j, which is the same D.
- So pr_j∘Φ = D holds, **conditional on Lemma PA**. ✓

**(c) φ̂(i) = P̂ with P̂ generic?**
- This is **not** in the statement of Φ̂. It is asserted in the proof of TV: "φ̂(i) = P̂ (the labelled lift defined by the plumbing markings is P̂)".
- What Φ̂ itself gives is φ̂(i) = λ(P̃), the labelled lift of the limit of (X_n, f_n), since g = 1 gives X^1_n = X_n.
- **Product type** (ξ_G = id): λ(P̃) = P = P̂ automatically. ✓
- **Non-product type:** λ(P̃) is one of the finitely many points of ξ_G^{-1}(P). It equals P̂ only through the labelled plumbing chart (Pl), which round8_q10 says it has "only described".
- **Repair (R3′).** In general λ(P̃) = σP̂ for some σ in the finite group Mod_G/Mod_Π acting on ∏M_w. That group acts because Mod_Π ⊲ Mod_G.
  - σP̂ is again generic: it lies off Sing Â and off the other components, since σ permutes the components of the σ-invariant set Â.
  - So Steps 1–5 below run verbatim for the piece σE.
  - Then a lift σ̃ ∈ Mod_G of σ^{-1} gives σ̃∘F, which satisfies (i)–(iii) for E. It uses the vertex σ^{-1}(j), the same Λ (E^ν ≅ (σE)^ν via σ), S replaced by σ̃Sσ̃^{-1}, and R(λ) by σ̃R(λ)σ̃^{-1}. This uses that σ̃ normalises Mod_Π.
  - So J0 holds for every piece, with the Teichmüller vertex and disc transported by σ. Nothing downstream uses the specific j.

**(d) E^ν = H/Λ_E with Λ_E ⊂ Γ′?**
- TV item 2 states it: "E^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p". Item 3 states that the lift of π_j∘ν to the universal cover is D.
- This is what J0 quotes: p_E∘q = q_{Γ′} and κ∘q_{Γ′} = u.
- The proof of item 2 (round8_q10 §4, Steps 2′–5) is **not spliced**, so I could not check it. It is a dependency.
- **Remark (partial independent check).** Given Φ̂ alone, Steps 2–3 below produce a holomorphic φ^ν : H → E^ν with p_E∘φ^ν = q_{Γ′}. Suppose one also knows that p_E : E^ν → C^ν is proper (TV items 2 and 4: ends go to cusps). Then:
  - At a point x ∈ H that is not an elliptic fixed point, q_{Γ′} has local degree 1. So p_E has local degree 1 at φ^ν(x), and p_E is unbranched over C^ν∖Br.
  - A proper unbranched finite map is a covering. So φ^ν restricted to H^♮ is a covering of p_E^{-1}(C^ν∖Br), with deck group a finite-index Λ_E ⊂ Γ′.
  - Hence E^ν ≅ H/Λ_E, after filling in the cone points.
  - So TV item 2 reduces to **properness of p_E** (TV item 4). That is the only part of TV's §4 that J0 really needs beyond Φ̂ and Lemma PA.

### 3.2 Steps of J0

**Step 1 (φ̂(H) ⊂ E).** ✓, including non-product strata. The argument is purely topological in ∏M_w.
- Â is closed in ∏M_w and of dimension ≤ 1: it lies in the boundary, and closure(V_0) is an irreducible surface not contained in it.
- Z is a locally finite union of points and curves.
- For a compact disc K ⊂ H, φ̂(K) meets only finitely many of the following: points of E ∩ E′ (closed discrete), isolated points, and components on which π_j is constant. So π_j takes finitely many values on φ̂(K) ∩ Z.
- Hence φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite) ∩ K, which is finite because u = κ∘q_{Γ′} is non-constant. Here π_j∘φ̂ = u needs (b).
- **Clopen argument.** Â∖Z = (E∖Z) ⊔ ⋃_{E′}(E′∖Z), where the union runs over E′ ≠ E with π_j non-constant on E′. E∖Z misses every E′, because points of E on other components lie in Z. Both parts are relatively closed, the second by local finiteness.
- i ∈ φ̂^{-1}(E∖Z), because P̂ is non-isolated, off the other components, and therefore off Z.
- H° is connected, so φ̂(H°) ⊂ E. E is closed and H° is dense, so φ̂(H) ⊂ E.
- **Non-product strata:** the only issue is (c) above, which is repaired by (R3′).

**Step 2 (φ̂ holomorphic).** ✓
- Σ_E is discrete in E. It consists of Sing E, the critical points of π_j on Reg E, and the preimage of the discrete set Sing C. A non-constant map from an irreducible curve has discrete fibres. Finiteness of π_j|_E is not needed.
- φ̂^{-1}(Σ_E) is discrete. Σ_E is closed and discrete in the closed set E, so it meets φ̂(K) in a finite set; then argue as in Step 1.
- At x with φ̂(x) = e ∉ Σ_E: by continuity φ̂ maps a neighbourhood of x into a neighbourhood U_e on which π_j is a biholomorphism onto a neighbourhood of a smooth point of C. There φ̂ = (π_j|_{U_e})^{-1}∘u, which is holomorphic.
- Riemann extension in a local embedding of ∏M_w then gives holomorphy everywhere.

**Step 3.** ✓
- The lift φ^ν exists by the universal property of normalisation: H is smooth and φ̂^{-1}(Sing E) is discrete.
- κ∘p_E∘φ^ν = u = κ∘q_{Γ′}. Since κ is injective off a finite set N and q_{Γ′} is non-constant, the two maps agree off the discrete set q_{Γ′}^{-1}(κ^{-1}κ(N)), hence everywhere.

**Step 4.** ✓
- Over C^ν∖Br, H/Λ → H/Γ′ is the covering H^♮/Λ → H^♮/Γ′, since both groups act freely on H^♮. The fibre over [x_0] is {Λγx_0 : γ ∈ Γ′}.
- φ^ν and q∘γ_0 are lifts of q_{Γ′}|_{H^♮} that agree at x_0. H^♮ is connected, so they agree on H^♮, and by density on H.

**Step 5.** ✓
- F := Φ∘γ_0^{-1}, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q.
- Lemma CL applies with T = T_G and Γ = Mod_Π. The action is properly discontinuous, the group is countable, and T_G/Mod_Π = ∏M_w as analytic spaces. So F is holomorphic.
- (ii): pr_j∘F = D∘γ_0^{-1}, and γ_0^{-1} is a biholomorphic isometry of H.
- (iii) R(λ) is a coset of S: by Lemma CS, since p∘F∘λ = ν∘q∘λ = ν∘q.
- (iii) Normality: if g ∈ R(λ) and s ∈ S, then s g F = s(F∘λ) = (sF)∘λ = F∘λ = gF, so g^{-1}sg ∈ S.
- (iii) Product rule: by normality gS·hS = ghS, and ghS ⊂ R(λμ) is a coset of S, hence equal to R(λμ). ✓

**Consequences.**
- "Example Z cannot occur at t = 0" is correct. At a simple zero z_* of J_0 that is not a cone point of Λ_E, a holomorphic lift L to T_{1,1} = H would satisfy J_0 = (unit)·(L − L_*)^3 near z_*, contradicting the simple zero.
- At z = 0, which is a cone point of order 2, J_0∘q ~ w² is not a cube.
- This is a remark only and is not used downstream.

**Verdict on J0: correct, with the repair (R3′) in non-product strata.** It is conditional on TV items 1–3 (equivalently on properness of p_E, by the Remark in 3.1(d)), on Corollary Φ̂, and on Lemma PA/TR for positive area at j.

## 4. Lemma 1.1 and the transported orbifold — correct after repair (R1′)

**Descent.** ✓ By (b) for Mod_Π, the map p∘H̃_t is Mod_Π-invariant on the saturated set Ã_0, so it descends. By (a), ξ_G Π_t(px) = H_t(ξ_G px) ∈ A_t, so Π_t lands in Â_t.

**Injectivity on Ã_0.** ✓
- H̃_t x = H̃_t y gives H_t ξ_G p x = H_t ξ_G p y, so ξ_G p x = ξ_G p y, so y = gx with g ∈ Mod_G. This uses that ξ_G∘p is the quotient by Mod_G.
- Then gH̃_t x = H̃_t x, so g ∈ Stab(H̃_t x) = Stab(x) by (c), and y = x.
- Only the inclusion Stab(H̃_t x) ⊂ Stab(x) is used.

**Surjectivity onto Ã_t.** ✓ Ã_0 is Mod_G-invariant.

**Bijectivity of Π_t.** ✓

**Joint continuity.** ✓ Restricted to the saturated set Ã_0 × Δ, p × id is still open onto Â_0 × Δ: (U ∩ p^{-1}B) maps onto p(U) ∩ B. So p × id is a quotient map, and continuity descends.

**Continuity of Π_t^{-1}.** ✓
- H_t is a homeomorphism closure(V_0) ∩ Δ_G → closure(V_t) ∩ Δ_G, by (R2).
- ξ_G is proper and Â_0 is closed in ∏M_w.
- Every limit point x satisfies Π_t x = y, and is unique by injectivity.

**Pieces to pieces.** ✓
- In a ≤1-dimensional analytic set, isolated points are topologically characterised.
- A non-isolated point has a disc neighbourhood iff it lies on exactly one irreducible local branch.
- The set of such points on a component E is the image of the connected normalisation minus a discrete set, so it is connected and dense in E. Two different components can meet only at non-manifold points.
- So the components of the 1-dimensional part are the closures of the connected components of the "disc points", and a homeomorphism permutes them.
- Surjectivity of Π_t gives "every piece at time t arises".

**Ĥ_t on normalisations.** ✓ Local branches are the components of punctured links.

**Gap in "Ê_t has finite type with puncture ends", and repair (R1′).**
- The argument says that Ê_t maps finitely onto the normalisation of closure(ξ_G E_t) minus finitely many points, and that "a finite unbranched cover of a punctured disc is a disjoint union of punctured discs".
- But nothing shown makes the map unbranched near the punctures. A finite branched (even Galois) cover of a punctured disc may have branch points accumulating at the puncture and infinite genus; e.g. w² = sin(π/z) over 0 < |z| < 1.
- **Repair.**
  - By (R1), closure(V_t) is a closed analytic subset of the projective variety M̄_g, hence algebraic by Chow's theorem (from memory).
  - Δ_G is locally closed algebraic, and ξ_G : ∏M_w → Δ_G is a finite algebraic morphism of quasi-projective varieties.
  - So Â_t is a quasi-projective algebraic set and E_t is an irreducible quasi-projective curve.
  - Its normalisation is a smooth quasi-projective curve, i.e. a compact Riemann surface minus finitely many points, whose ends are conformal punctures.
- Ĥ_t is a homeomorphism, so it maps ends to ends, i.e. punctures to punctures. With this repair the statement is correct.

**Transported orbifold O_t.** ✓ given (R1′).
- O_t has the signature of O_0, so χ^orb(O_t) = χ^orb(O_0) < 0.
- Its underlying surface is a compact Riemann surface minus finitely many points.
- So the uniformisation theorem for hyperbolic 2-orbifolds (from memory; there are no bad orbifolds since χ < 0) gives a lattice Λ_t whose cusps are exactly the punctures, with holomorphic u_t. Finite type is exactly what makes the ends cusps rather than funnels; this is why (R1′) matters.

**h̃_t and θ_t.** ✓
- A homeomorphism of underlying surfaces sending cone points to cone points of the same order and punctures to punctures is an orbifold homeomorphism. Locally at a cone point, a homeomorphism of punctured discs lifts through z ↦ z^e.
- So it lifts to h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0.
- For λ ∈ Λ_t: u_0∘(h̃_t^{-1}λh̃_t) = Ĥ_t^{-1}u_tλh̃_t = u_0. So h̃_t^{-1}λh̃_t is a deck transformation of the Galois covering H^♮ → H^♮/Λ, where H^♮ is H minus the elliptic fixed points. Hence it lies in Λ, and θ_t is a well-defined isomorphism.
- h̃_t may a priori reverse orientation. Nothing proves Ĥ_t orientation-preserving, but R*′ handles that case, and Prop. T does not need it.

## 5. Proposition T — correct

- F_0(H) ⊂ Ã_0, since p F_0 = ν_0 u_0 ∈ Â_0. So F_t = H̃_t∘F_0∘h̃_t^{-1} is defined and continuous.
- p F_t = Π_t p F_0 h̃_t^{-1} = Π_t ν_0 u_0 h̃_t^{-1} = Π_t ν_0 Ĥ_t^{-1} u_t = ν_t u_t. This uses ν_t Ĥ_t = Π_t ν_0 and u_t h̃_t = Ĥ_t u_0.
- ν_t u_t is holomorphic, so F_t is holomorphic by Lemma CL. ✓
- (2): h̃_t^{-1}λ = θ_t(λ)h̃_t^{-1}. Then F_0∘θ_t(λ) = gF_0 for g ∈ R(θ_tλ), and (b) gives H̃_t g = g H̃_t. ✓
- The key point is that no local orbifold analysis is needed: Lemma CL turns the continuous transported lift into a holomorphic one. The monodromy is transported by construction, with no continuity-in-t argument.
- Only (a), (b) and (c) of (R2^orb) are used, with (c) entering through Lemma 1.1. ✓

## 6. Lemma R*′ — correct

**Step 1: Bers' classification for g ∈ R_j(μ).**
- g = pr_j(g̃) with g̃F_0 = F_0∘μ, so g f_0 = f_0 μ.
- f_0 is an isometric embedding onto 𝔇 (J0(ii)). So g preserves 𝔇 = f_0(H) and acts on it as f_0 μ f_0^{-1}.
- The image f_0(α_μ) of the hyperbolic axis is a Teichmüller geodesic, and g translates it by **exactly** ℓ_0(μ) > 0. This is because f_0 is an isometry for the matching normalisations (curvature −4 on H, as in Φ̂). ✓
- **Pseudo-Anosov, justified directly.** g is represented on X = f_0(x), x ∈ α_μ, by a map that is affine for the defining differential q, with derivative diag(e^{ℓ}, e^{−ℓ}).
  - Horizontal saddle connections and horizontal cylinder circumferences form finite sets of lengths permuted by a power of g, yet they are scaled by e^{kℓ} ≠ 1. So there are none.
  - Hence the horizontal foliation is minimal and filling, and likewise the vertical one. So g is pseudo-Anosov.
- Bers (from memory): for pseudo-Anosov g, τ_T(g) = inf d(X, gX) is attained exactly on the unique invariant Teichmüller geodesic. Along that geodesic the translation equals τ_T(g).
- Since f_0(α_μ) is g-invariant, it is the axis. So τ_T(g) = ℓ_0(μ) and Min(g) = f_0(α_μ). ✓
- Elements of the kernel K of Mod_j → Aut(T_j) are harmless, since everything concerns the action on T_j.

**Step 2: direction of the inequality.**
- θ_t is conjugation by a homeomorphism that maps punctures to punctures. So it preserves elliptic (fixed point in H), parabolic (peripheral) and hyperbolic (the rest), and θ_tγ is hyperbolic. ✓
- Prop. T(2) gives f_t(γx) = g f_t(x). Royden gives τ_T(g) ≤ d_T(f_t x, f_t γx) ≤ d_H(x, γx) = ℓ_t(γ).
- So ℓ_t(γ) ≥ ℓ_0(θ_tγ): the time-t lengths dominate. This is the direction Thurston needs. ✓

**Step 3: Thurston on H/Λ′ versus H/Λ′_t.**
- Λ′_t = θ_t^{-1}(Λ′) is torsion-free, normal and of finite index in Λ_t.
- h̃_t λ′ h̃_t^{-1} = θ_t^{-1}(λ′) ∈ Λ′_t, so h̃_t descends to a homeomorphism H/Λ′ → H/Λ′_t inducing θ_t^{-1} on deck groups.
- Both surfaces are complete and of finite area, and the marking is type-preserving (cusps to cusps).
- Closed geodesics correspond to hyperbolic conjugacy classes, and Step 2, applied to γ = θ_t^{-1}(λ′), gives ℓ_{H/Λ′_t}(h̃_t c) ≥ ℓ_{H/Λ′}(c) for every closed curve c.
- Thurston's theorem (from memory, "Minimal stretch maps…", which covers complete finite-area surfaces with cusps): sup_c ℓ_X(c)/ℓ_Y(c) ≥ 1, with equality iff X = Y in Teichmüller space. Equivalently, the optimal Lipschitz constant is ≥ 1 by the area comparison of equal-area surfaces, with equality only for an isometry in the marking class. Here the sup is ≤ 1, so the structures coincide. ✓
- **Orientation.** If h̃_t reverses orientation, replace H/Λ′_t by its complex conjugate. Lengths are unchanged and the marking becomes orientation-preserving, so the resulting isometry is orientation-reversing. This is correct.
- **The lift A_t.** Lifting the homotopy between the isometry and the descended h̃_t gives an equivariant homotopy, so the lift A_t satisfies A_tλ′A_t^{-1} = θ_t^{-1}(λ′) on Λ′. The conjugation is constant along the homotopy by discreteness. ✓

**Extension from Λ′ to Λ.** ✓ (I re-did the computation.)
- Put ψ(x) := A_t^{-1}θ_t^{-1}(x)A_t. Then ψ = id on Λ′, and c := λ^{-1}ψ(λ).
- For λ′ ∈ Λ′: cλ′c^{-1} = λ^{-1}ψ(λλ′λ^{-1})λ = λ′, using normality of Λ′.
- The centraliser of a lattice in the full Isom(H) is trivial. If c commutes with a hyperbolic λ′, it maps the attracting fixed point of λ′ to the attracting fixed point of cλ′c^{-1} = λ′, so it fixes both fixed points. Fixed points of hyperbolic elements are dense in ∂H. An isometry fixing ∂H pointwise is the identity; a reflection fixes only 2 boundary points.

**Step 4: k_t = f_0.** ✓
- k_t(μx) = f_t(θ_t^{-1}(μ)A_t x) = g k_t(x) for g ∈ R_j(μ).
- For x on α_μ: d(k_t x, g k_t x) ≤ ℓ_0(μ) = τ_T(g), so k_t x ∈ Min(g) = f_0(α_μ).
- At a transverse intersection x of two axes, injectivity of f_0 gives k_t(x) = f_0(x).
- For a lattice, pairs of axis endpoints are dense in ∂H × ∂H, so such intersection points are dense. Continuity then gives k_t = f_0.
- **Orientation.** If A_t were anti-holomorphic, k_t would be both anti-holomorphic and equal to the non-constant holomorphic f_0. Then ∂k = ∂̄k = 0, which is impossible. So A_t ∈ PSL_2(ℝ). ✓
- ā_t is a biholomorphism, and π_j ν_t ā_t = π_j ν_0. ✓

## 7. Theorem RO — correct after repair (R2′), given (R2^orb), TV/Φ̂ and (IS)

**Step 0.** ✓
- closure(V_0) ∩ closure(Δ_G) is compact analytic, and A_0 is its open part in Δ_G. So A_0 has finitely many components.
- The preimage under a finite map of a curve with finitely many components has finitely many components.
- Lemma 1.1 gives "every piece at time t is Π_t(E_0)".

**Step 1: torsion-free level subgroup and the homomorphism r.**
- **Repair (R2′).** Mod_w[N] must be specified, since H_1 of a closed genus-0 surface is 0. Define Mod_w[N] := PMod_w ∩ ker(PMod_w → Sp(2g_w, ℤ/N)), with N ≥ 3 and pure mapping classes. For g_w = 0 this is all of PMod_{0,n}. It is torsion-free:
  - a finite-order pure class is realised by an automorphism of some (X, marked points) fixing every marked point;
  - for g = 0, n ≥ 3, such an automorphism is a Möbius map fixing 3 points, hence the identity;
  - for g = 1, n ≥ 1, it is a group automorphism with the marked point as origin, acting trivially on H_1, hence the identity — the elliptic involution acts by −1 ≢ 1 mod N;
  - for g ≥ 2, Serre's lemma (trivial on H_1(·;ℤ/N), N ≥ 3 ⇒ trivial on H_1) and Hurwitz's theorem give the identity (from memory).
- So Mod[N] = ∏Mod_w[N] is torsion-free and normal of finite index in Mod_Π. Its stabilisers in T_G are finite, hence trivial, and M[N] = T_G/Mod[N] is a manifold.
- The homomorphism λ ↦ R(λ) ∈ N(S)/S is J0(iii). ✓
- Mod[N]S is a subgroup because Mod[N] is normal. (N(S) ∩ Mod[N]S)/S has finite index ≤ [Mod_Π : Mod[N]] in N(S)/S. So Λ^N has finite index. ✓
- Λ″ exists by Selberg plus the normal core. ✓
- For μ ∈ Λ″: R(μ) = gS with g = ms, m ∈ Mod[N], s ∈ S. Then m = gs^{-1} ∈ R(μ), and uniqueness holds since S ∩ Mod[N] = 1. So r is a homomorphism. ✓

**Step 2.** ✓
- g_t(μx) = F_t(θ_t^{-1}(μ)A_t x) = r(μ)g_t(x). The equivariance r is **independent of t**. This is the crucial point, and it holds by Prop. T(2) and R*′.
- R = H/Λ″ is a finite-area surface of finite type.
- p g_t = ν_t u_t A_t = ν_t ā_t u_0, so E_t is the image of R. ✓

**Step 3: free homotopy.** ✓
- M_w[N] is a K(π,1), being a free quotient of the contractible T_w, and R is a CW complex.
- So free homotopy classes of maps R → M_w[N] correspond to homomorphisms Λ″ → Mod_w[N] up to conjugacy.
- ḡ^w_t induces r_w for every t, so all ḡ^w_t are freely homotopic.

**Step 4: the non-constancy criterion.** ✓
- If ḡ^w_t is constant, then g^w_t is constant, since its fibres are discrete orbits and H is connected. Then r_w(Λ″) ⊂ Stab(y) is finite, hence trivial.
- If r_w = 1, then g^w_t descends to R → T_w. T_w is bounded by the Bers embedding (from memory), and R = R̄ minus finitely many points. Bounded holomorphic functions extend over the punctures and are then constant on the compact R̄.
- Since M_w[N] → M_w is finite-to-one, f^w_t is constant iff ḡ^w_t is. This gives (a).

**Step 5: (IS).**
- **The version I recall (from memory, not checked against the paper).** Imayoshi–Shiga, MSRI Publ. 11 (1988), state for holomorphic families of Riemann surfaces of type (g,n), i.e. genus g with n punctures, 2g−2+n > 0, over a Riemann surface B of finite type:
  - (Rigidity) two locally non-trivial families with the same monodromy are holomorphically equivalent;
  - (Finiteness) there are only finitely many locally non-trivial families.
- I believe punctured types, including g = 0 and (1,1), are covered: the proof works on T_{g,n} and the Bers fibre space. I cannot confirm this from the text.
- **Application.** RO applies (IS) **factor by factor**, to ḡ^u_t : R → M_u[N] for u ∈ M(E_0). So product targets are not needed: a finite choice in each factor gives a finite set of tuples.
- Translation into the needed statement: under rigidity, two non-constant homotopic ḡ^u_t, ḡ^u_{t′} give equivalent families, so their classifying maps to the coarse M_u agree. Lifts of one map R → M_u through the finite map M_u[N] → M_u differ by elements of Mod_u/Mod_u[N]: argue as in Lemma CS on the lifts to T_u, then descend. So there are at most |Mod_u/Mod_u[N]| maps in each homotopy class. This is the "finitely many" used. ✓
- **Robustness for (1,1) and (0,4).** M_u[N] is then a hyperbolic curve. Every non-constant holomorphic map from a finite-type R has non-elementary monodromy: maps to D* or to an annulus are bounded, hence constant. Homotopic non-constant holomorphic maps into a hyperbolic curve with non-elementary monodromy are equal (classical Schwarz–Pick rigidity; from memory). So these types do not depend on the scope of (IS).

**Step 6: constancy.** ✓
- T_K is closed, by joint continuity of Π. Every point Π_{t*}(x) is the limit of Π_{t_n}(x) ∈ E_{t_n}, and K is closed, so pr_M(E_{t*}) ⊂ K.
- K(E_{t*}) is an irreducible curve, by (a) and irreducibility. So it equals K.
- The T_K are finitely many, pairwise disjoint and closed, and they cover the connected Δ. So K(E_t) ≡ K(E_0).
- Using Π avoids needing continuity in t of h̃_t or A_t, which is never established. This is a good design choice.
- **Puncture values.**
  - At a puncture p of Ê_t some u ∈ M degenerates. If no vertex degenerated, the limit would lie in the closed set Â_t, hence in E_t. That contradicts properness of the normalisation Ê_t → E_t. Constant vertices cannot degenerate.
  - So the joint limit lies in the finite set K(E_0) ∖ ∏_{u∈M}M_u, and every coordinate f_u(p), u ∈ M, including non-degenerate ones, is a coordinate of one of these finitely many points.
  - This excludes the Z′ mechanism. ✓

**Is the conclusion exactly (Rig)?** Yes.
- 𝒦 = {(G, M(E_0), K(E_0))} is finite (Step 0).
- Every piece of Â_t, at every t and in every stratum, is Π_t(E_0) with the same triple.
- RO in fact gives this **without** quotienting by Aut(G): all labelled lifts are tracked individually by Π_t. That is stronger than "up to Aut(G)".
- (Rig-w) and the joint-image form follow, since K(E_t) = K(E_0).

## 8. Proposition C and §7 of round12_q9

**Product type.** Correct.
- Π_t := H_t on the stratum is a homeomorphism mapping pieces to pieces, by Lemma S″ (re-checked in §4 above).
- Ĥ_t, O_t, θ_t are then defined, and (T_c) replaces Prop. T verbatim in R*′ and RO.
- (R1′) is needed here as well.

**Non-product type.** This is a sketch only, and it has a gap.
- (T_c) presupposes a family E_t with transport Ĥ_t.
- Under coarse (R2), pieces of Â_t are components of ξ_G^{-1}(H_t(·)). Their continuous choice in t can branch (twins), and the claim that a finite branched cover of Δ makes the lifts continuous is not proved.
- (b), finiteness, is plausible but is not proved there either: (T_c) is not even formulated without such a choice.

**"(T_c) ⟺ (α) ∧ (β)" and the (★_J) sketch.** These are heuristic, are not proved, and are not used by RO.

## 9. Verdicts

**Lemma CS: correct. Lemma CL: correct.**

**Lemma J0: correct after the stated repair (R3′)**, which is needed in non-product strata only. Conditional on:
- Corollary Φ̂;
- TV items 1–3. By §3.1(d), item 2 reduces to properness of p_E (TV item 4), given Φ̂;
- Lemma PA/TR (positive area at j), which round8_q10 itself cites from memory.

None of these proofs is spliced into this brief, so none was re-checked.

**Lemma 1.1: correct after repair (R1′)**, i.e. finite type of Ê_t via Chow's theorem.

**Proposition T: correct.**

**Lemma R*′: correct.** Bers is applied correctly, with the pseudo-Anosov property justified directly. The inequality goes the right way. Thurston is applied to type-preserving markings of finite-area cusped surfaces, with orientation handled. The extension to Λ is valid in the full Isom(H). Step 4 is valid.

**Theorem RO: correct after the stated repairs (R1′), (R2′)** (and (R3′) through J0). Its conclusion is exactly (Rig), indeed in a labelled, Aut(G)-free form. Conditional on:
- the reading (R2^orb) in its global form (a)–(d);
- TV/Φ̂/PA as above;
- Imayoshi–Shiga, in the version stated in §7, from memory. For vertex types (1,1) and (0,4) it can be replaced by classical rigidity of maps to hyperbolic curves.

**Proposition C: correct for product-type strata (with (R1′)). The non-product clause is a gap (sketch).**

## 10. Open / not checked here

1. TV items 1–4 and Lemma PA (round8_q10 §4 and the cited PA) are not re-checked. J0 needs Φ̂, positive area at j, and properness of p_E.
2. Local-to-global for (R2^orb): whether isotropy-preserving local lifts imply the global equivariant lift (a)–(d). This is open, as stated in round12_q9.
3. The exact published scope of Imayoshi–Shiga for punctured types with g ≥ 1 and n ≥ 1, or g = 0 and n ≥ 5. This is from memory.
4. Proposition C in non-product strata under coarse (R2).
5. Not in scope: MS11♭ under (R2^orb), and the chain step "(Rig) + MS11♭ ⇒ the problem's claim".

=== END OF ANSWER round13_q9 ===
