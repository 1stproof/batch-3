# round12_q9 — attempt on (Rig) (ledger entry 82)

**Plan/status line (written first).** Brief read in full.
1. Item 1 ((Rig) under the coarse reading (R2)): I found no global argument. I record a new reduction (§7).
2. Item 2 ((Rig) under the orbifold reading): I formalise (R2^orb) as an equivariant lift of H on every stratum (§1). Then:
   - (H_0) holds for the **joint** vertex map of every piece at t = 0, over the Veech-type orbifold structure Λ_E. This is Lemma J0, derived from Theorem TV and Corollary Φ̂ of round8_q10. It is what makes Example Z irrelevant at t = 0.
   - (R2^orb) transports this joint lift (§4).
   - Lemma R* with set-valued monodromy, plus Imayoshi–Shiga, then gives (Rig) for all pieces in all strata, product or not (§5–§6).
3. The weakest form proved, the cited inputs, and the open questions are listed in §8.

---

## 1. Readings and conventions

(R1) and (R2) are as in the task: H is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, H_0 = id, mapping strata to strata.

**Stratum notation.** For a stable graph G with at least one edge:
- T_G := ∏_{w∈V(G)} T_w, where T_w is the Teichmüller space of type (g_w, n_w) with labelled special points.
- Mod_Π := ∏_w Mod_w, where Mod_w is the pure mapping class group.
- p : T_G → ∏_w M_w = T_G/Mod_Π is the quotient (coarse spaces).
- Mod_G ⊃ Mod_Π is the finite extension, by lifts of Aut(G), for which [T_G/Mod_G] is the stratum Δ_G as a sub-orbifold of M̄_g. Its isotropy groups are the Aut(z), modulo generic automorphisms.
- ξ_G : ∏M_w → Δ_G is the finite quotient map.
- A_t := closure(V_t) ∩ Δ_G, Â_t := ξ_G^{-1}(A_t) ⊂ ∏_w M_w, and Ã_t := p^{-1}(Â_t) ⊂ T_G.

All groups act properly discontinuously by biholomorphisms, and they are countable.

**Reading (R2^orb) (formal version used here).** For every stratum G there is a continuous map H̃ = H̃^G : Ã_0 × Δ → T_G, written H̃_t := H̃(·, t), such that for all t:
- (a) H̃_t lifts H_t: ξ_G∘p∘H̃_t = H_t∘ξ_G∘p on Ã_0;
- (b) H̃_t is Mod_G-equivariant: H̃_t(g x) = g H̃_t(x) for all g ∈ Mod_G;
- (c) H̃_t preserves isotropy: Stab_{Mod_G}(H̃_t x) = Stab_{Mod_G}(x);
- (d) H̃_0 = id.

*Why this is the content of "H restricted to each stratum is an orbifold isomorphism, compatible with the charts Def(z)/Aut(z)".*
- Near ẑ ∈ T_G over z, the chart Def(z) → Def(z)/Aut(z) is a Stab(ẑ)-invariant neighbourhood of ẑ in T_G, modulo Stab(ẑ) ≅ Aut(z).
- A family of orbifold maps of the global quotient [Ã_0/Mod_G] into [T_G/Mod_G] that starts at the identity is represented by an equivariant lift, with equivariance through an automorphism of Mod_G. Since t ↦ that automorphism is continuous into a discrete set and is the identity at t = 0, it is the identity.
- (c) is "preserves isotropy groups".
- I do **not** prove that a purely local formulation (local equivariant lifts at each z, with no coherent choice) implies the global one. That is a gap in the *interpretation*, not in the proofs below: every later use of (R2^orb) is a use of (a)–(d).

**Uses of (R2^orb)** are marked [orb] below. Everything not marked uses only (R1) and (R2).

**Lemma 1.1 [orb] (descended transport).** H̃_t descends to a map Π_t : Â_0 → Â_t (so p∘H̃_t = Π_t∘p) with the following properties:
- Π_t is a homeomorphism;
- ξ_G∘Π_t = H_t∘ξ_G;
- (x, t) ↦ Π_t(x) is continuous;
- Π_t maps each piece (1-dimensional irreducible component) of Â_0 onto a piece of Â_t, and every piece at time t arises this way.

*Proof.*
- **Descends.** By (b) for g ∈ Mod_Π, H̃_t descends. By (a) the descended map lands in Â_t, because ξ_G p H̃_t(x) = H_t(ξ_G p x) ∈ A_t.
- **Injective on Ã_0.** If H̃_t x = H̃_t y, then by (a) and injectivity of H_t we get ξ_G p x = ξ_G p y, so y = g x for some g ∈ Mod_G. Then g H̃_t x = H̃_t x. By (c), g ∈ Stab(H̃_t x) = Stab(x), so y = x.
- **Surjective onto Ã_t.** Let y ∈ Ã_t. Then ξ_G p y = H_t(ξ_G p x) = ξ_G p H̃_t x for some x ∈ Ã_0, so y = g H̃_t x = H̃_t(g x).
- **Π_t is bijective.** Injectivity: if Π_t(p x) = Π_t(p y), then H̃_t x = g H̃_t y = H̃_t(g y) with g ∈ Mod_Π, so x = g y. Surjectivity is immediate from the surjectivity of H̃_t.
- **Continuity.** H̃ is continuous and p is open, so Π_t is continuous, jointly in (x, t).
- **Continuity of Π_t^{-1}.** Let y_n → y and x_n := Π_t^{-1} y_n. Then ξ_G(x_n) = H_t^{-1} ξ_G(y_n) converges. Since ξ_G is finite, hence proper, the x_n lie in a compact set. Every limit point x satisfies Π_t x = y, so x_n → Π_t^{-1}y.
- **Pieces.** A homeomorphism of 1-dimensional analytic sets maps isolated points to isolated points, and irreducible components of the 1-dimensional part to irreducible components. The latter are the closures of the connected components of the set of points with a disc neighbourhood (round8_q7 Lemma S″, argument re-checked). ∎

For a piece E_0 of Â_0, put E_t := Π_t(E_0). Its normalisation is ν_t : Ê_t → E_t. Π_t lifts to a homeomorphism Ĥ_t : Ê_0 → Ê_t with ν_t∘Ĥ_t = Π_t∘ν_0, because local branches are the components of punctured links (round5_q4 §2.1).

**Ê_t has finite type with puncture ends.** The closure of ξ_G(E_t) in M̄_g is a component of the compact analytic set closure(V_t) ∩ closure(Δ_G). So its normalisation is a compact Riemann surface minus finitely many points. Ê_t maps finitely onto that normalisation, and a finite unbranched cover of a punctured disc is a disjoint union of punctured discs. Hence Ê_t is a compact Riemann surface minus finitely many points, and Ĥ_t maps punctures to punctures.

## 2. Two lifting lemmas (proved; no hypothesis beyond the setting)

Throughout §2, Γ is a countable group acting properly discontinuously by biholomorphisms on a complex manifold T. X := T/Γ carries Cartan's quotient analytic structure, and p : T → X is the quotient map. Q is a connected Riemann surface.

**Lemma CS (two holomorphic lifts differ by one group element).** Let F, F′ : Q → T be holomorphic with p∘F = p∘F′. Then F′ = g∘F for some g ∈ Γ. The set of such g is a coset g·S_F, where S_F := {s ∈ Γ : s∘F ≡ F} is a finite group.

*Proof.*
- Q = ∪_{g∈Γ} Z_g, where Z_g := {y : F′(y) = gF(y)}.
- Each Z_g is a closed analytic subset of Q, and Γ is countable. By Baire, some Z_g has interior.
- By the identity theorem F′ ≡ gF.
- If gF ≡ g′F, then g^{-1}g′ ∈ S_F. Finally S_F ⊂ Stab(F(y)), which is finite. ∎

**Lemma CL (continuous lifts of holomorphic maps are holomorphic).** Let h : Q → X be holomorphic and L : Q → T continuous with p∘L = h. Then L is holomorphic.

*Proof.* The statement is local. Fix y_0 and put x̂ := L(y_0), A := Stab_Γ(x̂) (finite).

**Chart.** By Cartan there is an A-invariant neighbourhood B of x̂ such that:
- B is A-equivariantly a ball with linear A-action;
- gB ∩ B ≠ ∅ implies g ∈ A;
- B/A → X is an open embedding.

Let σ = (σ_1, …, σ_m) be generators of the A-invariant polynomials. They induce an embedding σ̄ of B/A into ℂ^m. Since h is holomorphic, σ̄∘h is holomorphic near y_0.

**Fibre product.** Take a disc Q_0 ∋ y_0 whose closure satisfies L(closure Q_0) ⊂ B. Put Z := {(y,b) ∈ Q_0 × B : σ(b) = σ̄(h(y))}.
- Z is analytic, and its fibre over y is the finite orbit A·L(y).
- Z → Q_0 is proper, since fibres lie in the compact set A·L(closure Q_0).
- So Z is finite over Q_0. Let Σ ⊂ Q_0 be the image of Sing Z, of the 0-dimensional part of Z, and of the critical points of the projection on Reg Z. Σ is discrete: a curve of critical points would lie in a fibre, and fibres are finite.
- Over Q_0 ∖ Σ, Z → Q_0 is a finite covering map whose local sheets are graphs of holomorphic maps.

**Conclusion.** The graph of L|_{Q_0∖Σ} is a continuous section of this covering. Over every evenly covered disc a continuous section lies in a single sheet, so L is holomorphic on Q_0 ∖ Σ. L is continuous and bounded in the coordinates of the ball B, so by Riemann's extension theorem it is holomorphic on Q_0. ∎

*Remark.* Lemma CL is why no orbifold bookkeeping (cone orders, minimal orbifolds) is needed below. If a continuous lift exists, it is automatically holomorphic, and cone points that would obstruct it cannot be present.

## 3. Lemma J0: the joint vertex map of every piece at t = 0 lifts over the Veech orbifold (no use of (R2^orb))

**Prior results used** (round8_q10, quoted in the brief; not re-proved here):
- **Theorem TV.** Let E be a piece of Â_0 (any G). There are:
  - a vertex j;
  - a closed Teichmüller curve C ⊂ M_j, with normalisation κ : C^ν = H/Γ′ → M̄_j (Γ′ a lattice);
  - a subgroup Λ_E ⊂ Γ′ of finite index, with E^ν ≅ H/Λ_E such that p_E := (π_j∘ν lifted to normalisations) : E^ν → C^ν is the map H/Λ_E → H/Γ′ induced by the inclusion.

  The Teichmüller disc D : H → T_j satisfies D∘γ = (affine class of γ)∘D for γ ∈ Γ′, and κ∘q_{Γ′} = u := (projection of D to M_j).
- **Corollary Φ̂, together with the proof of TV.** For a point P̂ ∈ E chosen off Sing Â and off the other components of Â, there is a continuous map Φ = (φ̂_w)_w : H → T_G with:
  - each φ̂_w 1-Lipschitz;
  - φ̂ := p∘Φ mapping H into Â;
  - φ̂(i) = P̂;
  - φ̂_j = D, so π_j∘φ̂ = u.

**Lemma J0.** Let E be a piece at t = 0, with the notation of TV. Put Λ := Λ_E and let q : H → H/Λ = E^ν be the quotient map. There are γ_0 ∈ Γ′ and a **holomorphic** map F : H → T_G such that:
- (i) p∘F = ν∘q, i.e. F lifts the whole vertex map of E;
- (ii) pr_j∘F = D∘γ_0^{-1}, an isometric holomorphic embedding of H onto the Teichmüller disc 𝔇 := D(H);
- (iii) for every λ ∈ Λ the set R(λ) := {g ∈ Mod_Π : F∘λ = g∘F} is a coset of the finite group S := {s ∈ Mod_Π : s∘F ≡ F}. Moreover R(λμ) = R(λ)R(μ), and every element of R(λ) normalises S.

*Proof.*

**Step 1 (φ̂(H) ⊂ E).** Let Z be the union of the following sets:
- the points of E lying on other components of Â;
- the isolated points of Â;
- the components E′ ≠ E of Â on which π_j is constant.

Z is closed, and it is a locally finite union of points and curves. For a compact disc K ⊂ H, φ̂(K) is compact. It meets only finitely many points and components making up Z, and π_j takes finitely many values on φ̂(K) ∩ Z. Hence φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite set) ∩ K, which is finite because u is non-constant holomorphic. So φ̂^{-1}(Z) is discrete, and H° := H ∖ φ̂^{-1}(Z) is connected.

Now Â ∖ Z is the disjoint union of E ∖ Z and the sets E′ ∖ Z (E′ ≠ E, π_j non-constant on E′). Each of these is relatively closed, and the family is locally finite, so E ∖ Z is clopen in Â ∖ Z. Its preimage is clopen in H° and contains i, because P̂ ∉ Z. Hence it is all of H°, and since E is closed, φ̂(H) ⊂ E.

**Step 2 (φ̂ is holomorphic).** Let Σ_E ⊂ E be the discrete set consisting of:
- Sing E;
- the points where π_j|_E : E → C is not a local biholomorphism onto a smooth point of C.

π_j|_E is a non-constant finite map of curves, so Σ_E is discrete. As in Step 1, φ̂^{-1}(Σ_E) is discrete. Off it, φ̂ = (π_j|_E)^{-1}_{loc}∘u is holomorphic. Since φ̂ is continuous, Riemann's extension theorem (in a local embedding of ∏M_w) makes it holomorphic on H.

**Step 3 (lift to E^ν, and p_E∘φ^ν = q_{Γ′}).** φ̂ lifts to a holomorphic φ^ν : H → E^ν, by the universal property of normalisation. Then κ∘p_E∘φ^ν = π_j∘φ̂ = u = κ∘q_{Γ′}. Since κ is generically injective, p_E∘φ^ν = q_{Γ′}.

**Step 4 (φ^ν = q∘γ_0).** Let Br ⊂ C^ν be the finite set of orbifold points of H/Γ′.
- Over C^ν ∖ Br, both H → H/Γ′ and the finite map p_E : H/Λ → H/Γ′ are unbranched coverings.
- Put H^♮ := q_{Γ′}^{-1}(C^ν ∖ Br), a connected set (H minus a discrete set), and fix x_0 ∈ H^♮.
- The fibre p_E^{-1}(q_{Γ′} x_0) is {q(γ x_0) : γ ∈ Γ′}. So φ^ν(x_0) = q(γ_0 x_0) for some γ_0 ∈ Γ′.
- φ^ν and q∘γ_0 are both lifts of q_{Γ′}|_{H^♮} through a covering map, and they agree at x_0. So they agree on H^♮, hence on H.

**Step 5 (F).** Put F := Φ∘γ_0^{-1}.
- F is continuous, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q.
- ν∘q is holomorphic, so F is holomorphic by Lemma CL (with Γ = Mod_Π). This gives (i).
- (ii): pr_j∘F = D∘γ_0^{-1}, and γ_0^{-1} is an isometry of H.
- (iii): for λ ∈ Λ, F∘λ and F are holomorphic lifts of the same map ν∘q∘λ = ν∘q, so Lemma CS applies.
- Product rule: if a ∈ R(λ) and b ∈ R(μ), then F(λμx) = aF(μx) = abF(x).
- Normality: if g ∈ R(λ) and s ∈ S, then g^{-1}sgF = g^{-1}s(F∘λ) = g^{-1}(F∘λ) = F, so g^{-1}sg ∈ S. ∎

**Consequences.**
- **(H_0) for the joint map.** At t = 0 the whole vertex map of every piece, not only its Teichmüller coordinate, has an equivariant holomorphic lift over the single orbifold structure Λ_E for which the j-coordinate is an isometry. This is hypothesis (H_0) of Lemma R*, together with (O_u) at t = 0 in L2 (round7_q9).
- In particular the joint minimal orbifold structure of ν_0 is dominated by Λ_E: every cone point of the joint map is a cone point of Λ_E, with order dividing.
- **Example Z (round8_q9) cannot occur at t = 0.** There the u-coordinate z³ + z needs cone points (orders 3 and 2 at roots of J_0 = 0, 1728, and order 6 at z = 0) that Λ_E does not have. So Lemma J0 excludes it as a boundary piece of a totally geodesic V_0. This answers the t = 0 half of question Q1 of round9_q9 for Example Z: E_0 is not realisable. For Example Z′, Lemma J0 excludes E_0 unless J_0∘q lifts holomorphically to T_{1,1} = H. I have not decided which J_0 satisfy this. So the remaining objection to Z/Z′-type deformations concerns t ≠ 0: Lemma J0 says nothing about E_t for t ≠ 0.

## 4. [orb] Transport of the joint lift: (O_G), (O), (OT), (O_u) hold under (R2^orb)

Fix a piece E_0 at t = 0, with Λ := Λ_E, q = u_0 : H → Ê_0 = E^ν, and F_0 := F as in Lemma J0. Write e_c for the cone orders of the orbifold O_0 := H/Λ, and E_t, Ê_t, Ĥ_t as in §1.

**Transported orbifold.** Let O_t be the orbifold with underlying Riemann surface Ê_t, cone points Ĥ_t(c) of order e_c, and the punctures of Ê_t as cusps.
- O_t has the same signature as O_0, so χ^orb(O_t) = χ^orb(O_0) < 0.
- By the uniformisation theorem for hyperbolic 2-orbifolds (cited from memory), O_t = H/Λ_t for a lattice Λ_t ⊂ PSL_2(ℝ), with holomorphic quotient map u_t : H → Ê_t.
- Ĥ_t is a homeomorphism O_0 → O_t preserving cone points with their orders and cusps. So it lifts to a homeomorphism h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0, and conjugation by h̃_t gives an isomorphism θ_t : Λ_t → Λ, θ_t(λ) := h̃_t^{-1} λ h̃_t. (Lifting orbifold homeomorphisms to orbifold universal covers is standard; cited from memory.)
- At t = 0 take h̃_0 = id.

**Proposition T [orb].** Put F_t := H̃_t∘F_0∘h̃_t^{-1} : H → T_G. Then:
- (1) F_t is holomorphic and p∘F_t = ν_t∘u_t. That is, F_t is a holomorphic lift of the whole vertex map of E_t over the transported orbifold O_t.
- (2) For λ ∈ Λ_t and every g ∈ R(θ_t λ): F_t∘λ = g∘F_t.

So the orbifold-transport hypothesis holds in the following form:
- **(O_G)** (round7_q9 §2.1) holds with the joint monodromy ρ_0∘θ_t, where ρ_0 is any choice function λ ↦ ρ_0(λ) ∈ R(λ).
- Projecting to a vertex gives **(O)** of PR-E and **(O_u)** for every u.
- With Λ_E as the orbifold structure, it gives **(OT)** of Lemma TR.

*Proof.*
- **(1), lifting.** F_t is continuous. By (a) of (R2^orb) and the definition of Π_t, p∘H̃_t = Π_t∘p on Ã_0. Hence
  p∘F_t = Π_t∘ν_0∘u_0∘h̃_t^{-1} = Π_t∘ν_0∘Ĥ_t^{-1}∘u_t = ν_t∘u_t.
  Since ν_t∘u_t is holomorphic, F_t is holomorphic by Lemma CL.
- **(2), equivariance.** Using (b) of (R2^orb) for g ∈ Mod_Π ⊂ Mod_G, and F_0∘θ_t(λ) = g∘F_0 for g ∈ R(θ_tλ):
  F_t(λy) = H̃_t F_0(h̃_t^{-1} λ y) = H̃_t F_0(θ_t(λ) h̃_t^{-1} y) = H̃_t(g F_0(h̃_t^{-1}y)) = g F_t(y). ∎

**Where (R2^orb) was used.** Only (a), (b) and (c) of the reading, through Lemma 1.1 and the identity H̃_t∘g = g∘H̃_t for g ∈ Mod_Π.

This answers the task's question: (R2^orb) implies the transport hypotheses (O), (O_G), (OT) and (O_u). (H_0) is independent of (R2^orb): it is Lemma J0. Under the coarse reading, the step that fails is exactly the existence of a continuous Mod_Π-equivariant lift H̃_t. Without it, nothing produces the continuous lift F_t, and Lemma CL has nothing to act on.

*Note on cone points (the task's remark).* An automorphism of one component C_v fixing its special points extends by the identity to an automorphism of the stable curve. So stabilisers in Mod_Π are visible in Aut(z), and hence in Mod_G. This is why (c) for Mod_G gives (c) for Mod_Π: Stab_{Mod_Π}(x) = Stab_{Mod_G}(x) ∩ Mod_Π. The proof above does not need cone orders explicitly.

## 5. Lemma R*′ (Lemma R* with coset-valued monodromy; re-proved here)

**Cited from memory.**
- **(Roy)** Royden, and Earle–Kra / Gardiner for punctured surfaces: holomorphic maps H → T_{h,m} are 1-Lipschitz from the Poincaré metric of curvature −4 to d_T.
- **(Bers)** If φ ∈ Mod preserves a Teichmüller geodesic and translates it by ℓ > 0, then φ is pseudo-Anosov, τ_T(φ) = ℓ, and Min(φ) is that geodesic.
- **(Th)** Thurston: for marked complete finite-area hyperbolic structures X, Y on the same surface, if ℓ_Y ≥ ℓ_X on all closed curves, then X = Y. Equivalently, there is an isometry homotopic to the marking.
- **(Sel)** Selberg's lemma.
- Axes of hyperbolic elements of a lattice have transverse intersection points dense in H.

**Lemma R*′ [orb].** In the setting of Proposition T, let j be the Teichmüller vertex and put f_t := pr_j∘F_t. There is an isometry A_t of H with A_t Λ A_t^{-1} = Λ_t and A_t λ A_t^{-1} = θ_t^{-1}(λ) for all λ ∈ Λ. A_t is holomorphic, i.e. A_t ∈ PSL_2(ℝ), and f_t∘A_t = f_0.

*Proof.* For μ ∈ Λ put R_j(μ) := pr_j(R(μ)). Every g ∈ R_j(μ) satisfies g∘f_0 = f_0∘μ.

**Step 1.** Let μ be hyperbolic and g ∈ R_j(μ). By Lemma J0(ii), f_0 is an isometry onto 𝔇. So g preserves 𝔇 and translates the geodesic f_0(α_μ) by ℓ_0(μ). By (Bers), g is pseudo-Anosov, τ_T(g) = ℓ_0(μ), and Min(g) = f_0(α_μ).

**Step 2.** Let γ ∈ Λ_t be hyperbolic, x on its axis, and g ∈ R_j(θ_tγ). By Prop. T(2), g f_t(x) = f_t(γ x). By (Roy),
  τ_T(g) ≤ d_T(f_t x, f_t γ x) ≤ ℓ_t(γ).
By Step 1, τ_T(g) = ℓ_0(θ_t γ). Hence ℓ_t(γ) ≥ ℓ_0(θ_tγ).

**Step 3 (Thurston).**
- By (Sel) take Λ′ ⊂ Λ torsion-free, normal, of finite index, and put Λ′_t := θ_t^{-1}(Λ′).
- h̃_t descends to a homeomorphism H/Λ′ → H/Λ′_t between complete finite-area hyperbolic surfaces. It induces θ_t^{-1} on π_1, and θ_t preserves the parabolic/hyperbolic type.
- Step 2 says that lengths on H/Λ′_t dominate lengths on H/Λ′ under this marking. If h̃_t reverses orientation, apply (Th) to the conjugate structure; lengths do not see orientation.
- So there is an isometry A_t of H, possibly orientation-reversing, with A_t λ A_t^{-1} = θ_t^{-1}(λ) for λ ∈ Λ′.
- **Extension to Λ.** For λ ∈ Λ, c := λ^{-1}A_t^{-1}θ_t^{-1}(λ)A_t centralises Λ′. A lattice has trivial centraliser in Isom(H), so c = 1.

**Step 4 (the maps coincide).** Put k_t := f_t∘A_t. For μ ∈ Λ and g ∈ R_j(μ): k_t(μx) = f_t(θ_t^{-1}(μ)A_t x) = g k_t(x), by Prop. T(2). k_t is 1-Lipschitz, since it is f_t composed with an isometry.
- For hyperbolic μ and x ∈ α_μ: d_T(k_t x, g k_t x) ≤ ℓ_0(μ) = τ_T(g). So k_t x ∈ Min(g) = f_0(α_μ).
- At a transverse intersection point x of two axes α_μ, α_ν: k_t(x) ∈ f_0(α_μ) ∩ f_0(α_ν) = {f_0(x)}, by injectivity of f_0.
- By density of such points and continuity, k_t = f_0.
- If A_t reversed orientation, k_t would be anti-holomorphic and also equal to the holomorphic non-constant f_0, which is impossible. So A_t ∈ PSL_2(ℝ). ∎

So A_t descends to a biholomorphism ā_t : Ê_0 → Ê_t (an orbifold isomorphism O_0 → O_t), with π_j∘ν_t∘ā_t = π_j∘ν_0. In particular (Rig-v): closure π_j(E_t) = closure π_j(E_0) = C̄.

## 6. Theorem RO: (Rig) under (R2^orb)

**Cited from memory: (IS) Imayoshi–Shiga**, "A finiteness theorem for holomorphic families of Riemann surfaces" (MSRI Publ. 11, 1988). Let R be a Riemann surface of finite type, and Y = T_{h,m}/Γ with Γ ⊂ Mod_{h,m} torsion-free of finite index (3h−3+m > 0). Then each free homotopy class of maps R → Y contains at most finitely many non-constant holomorphic maps.

*Caveat.* I recall the theorem for families of Riemann surfaces of type (h,m) in general, which is the form used in round7_q9 and round8_q9. If the published statement covers only some types, then Theorem RO holds for the pieces whose non-constant vertices are of the covered types.

**Theorem RO [orb].** Assume (R1), (R2) and (R2^orb), and the prior results TV and Φ̂ (round8_q10). Let E_0 be any piece at t = 0, in any stratum G (product or not), and E_t := Π_t(E_0). Then:
- (a) M(E_t) = M(E_0) for all t;
- (b) there is a finite set 𝒦(E_0) of curves with K(E_t) ∈ 𝒦(E_0) for all t;
- (c) in fact K(E_t) = K(E_0) for all t, and every puncture value f_u(p), u ∈ M(E_0), of E_t lies in the t-independent finite set of points of K(E_0) ∖ ∏_u M_u, together with their components.

Consequently **(Rig) holds**, with 𝒦 := {(G, M(E_0), K(E_0)) : G a stratum, E_0 a piece of Â_0}. This set is finite, and every piece at every time has its triple in 𝒦. (Rig-w) and the joint-image form (Rig-all) follow as well.

*Proof.*

**Step 0 (finitely many pieces).**
- There are finitely many strata.
- For each G, the 1-dimensional components of A_0 are open dense parts of components of the compact analytic set closure(V_0) ∩ closure(Δ_G), so there are finitely many.
- ξ_G is finite, so Â_0 has finitely many pieces.
- By Lemma 1.1, every piece at time t is Π_t(E_0) for one of them.

So (b) for every E_0 gives (Rig).

**Step 1 (a lattice on which the monodromy is an honest homomorphism into a torsion-free group).** Fix N ≥ 3 and put Mod[N] := ∏_w Mod_w[N], which is torsion-free. Note S ∩ Mod[N] = {1}, since S is finite.
- By Lemma J0(iii), λ ↦ R(λ) is a homomorphism Λ → N(S)/S.
- Let Λ^N be the preimage of (N(S) ∩ Mod[N]S)/S. It has finite index in Λ, since Mod[N] has finite index in Mod_Π.
- Take Λ″ ⊂ Λ^N torsion-free, normal and of finite index in Λ (Selberg, then normal core).
- For μ ∈ Λ″, R(μ) ∩ Mod[N] consists of exactly one element r(μ): it is nonempty by definition of Λ^N, and two elements would differ by an element of S ∩ Mod[N] = {1}.
- r is a homomorphism Λ″ → Mod[N]: r(μ)r(ν) ∈ R(μν) ∩ Mod[N].

**Step 2 (the normalised maps).** Put g_t := F_t∘A_t : H → T_G. By Prop. T(2) and A_t μ A_t^{-1} = θ_t^{-1}(μ), for μ ∈ Λ″:
  g_t(μ x) = F_t(θ_t^{-1}(μ) A_t x) = r(μ) g_t(x),
since r(μ) ∈ R(μ) = R(θ_t(θ_t^{-1}μ)).
- Mod[N] acts freely and properly on T_G. So M[N] := T_G/Mod[N] = ∏_w M_w[N] is a complex manifold and a K(π,1), since T_w is contractible.
- R := H/Λ″ is a Riemann surface of finite type (a finite cover of the finite-area orbifold H/Λ).
- g_t descends to a holomorphic ḡ_t = (ḡ^w_t)_w : R → ∏_w M_w[N], and p∘g_t = ν_t∘u_t∘A_t = ν_t∘ā_t∘q.
- So E_t = ν_t(Ê_t) is the image of R under ∏_w (M_w[N] → M_w) ∘ ḡ_t.

**Step 3 (fixed homotopy classes).** For each w, ḡ^w_t lifts to g^w_t, which is r_w-equivariant (r_w := pr_w∘r). Maps into the K(π,1) M_w[N] are determined up to free homotopy by the induced homomorphism up to conjugacy, so all ḡ^w_t, t ∈ Δ, are freely homotopic.

**Step 4 (non-constancy is t-independent).**
- If ḡ^w_t is constant, then g^w_t is constant (connected domain, discrete fibres). Then r_w(Λ″) fixes a point of T_w, so it is finite, hence trivial, since Mod_w[N] is torsion-free.
- Conversely, if r_w is trivial, then g^w_t descends to a holomorphic map R → T_w. T_w is biholomorphic to a bounded domain (Bers embedding, cited). R is a compact surface minus finitely many points, and bounded holomorphic functions extend over punctures. So the map is constant.
- Hence ḡ^w_t is constant ⟺ r_w = 1, which does not depend on t. Since ν^w_t∘ā_t∘q = (M_w[N] → M_w)∘ḡ^w_t∘(H → R), this gives (a).

**Step 5 (finiteness).** For u ∈ M(E_0), (IS) and Step 3 show that ḡ^u_t lies in a finite set {ψ_{u,1}, …, ψ_{u,k_u}} independent of t. Hence pr_{M}(E_t) is the image of R under one of the finitely many maps (ψ_{u,i_u})_{u∈M}, followed by the projections to M_u. So K(E_t) lies in a finite set 𝒦(E_0). This proves (b).

**Step 6 (constancy, (c)).** For K ∈ 𝒦(E_0), put T_K := {t : K(E_t) = K}.
- T_K is closed. Suppose t_n → t* with K(E_{t_n}) = K. Π is jointly continuous (Lemma 1.1), so every point of E_{t*} is a limit of points of E_{t_n}. Hence pr_M(E_{t*}) ⊂ K, and K(E_{t*}) = K because both are irreducible curves.
- The T_K are finitely many disjoint closed sets covering the connected Δ. So K(E_t) ≡ K(E_0).
- The statement on puncture values follows as in round8_q7 Cor. S′(a): K(E_0) ∖ ∏M_u is finite. ∎

**Explicit list of uses of (R2^orb):**
- Lemma 1.1 (descent and bijectivity of Π_t, which needs (b) and (c));
- Prop. T (equivariance (b), and the lifting property (a));
- through these, Lemma R*′ and Theorem RO.

Lemma J0, Lemma CS and Lemma CL do not use it.

## 7. The coarse reading (R2): precise reduction (item 1 not achieved)

I found no global argument proving (Rig) under the coarse reading. What §§3–6 give without (R2^orb) is the following reduction. It is proved: the proofs of R*′ and RO use (R2^orb) only through Prop. T.

**Hypothesis (T_c) for a piece E_0.** For every t there is a holomorphic F_t : H → T_G with:
- p∘F_t = ν_t∘u_t, where u_t uniformises the transported orbifold O_t of §4;
- F_t∘λ = g∘F_t for every λ ∈ Λ_t and some (equivalently every) g ∈ R(θ_tλ).

Here θ_t is induced by a lift of a homeomorphism Ê_0 → Ê_t isotopic to Ĥ_t and preserving the cone data of Λ_E.

**Proposition C.** Under (R1), (R2) and TV/Φ̂ (no (R2^orb)): if (T_c) holds for every piece at t = 0, then (Rig) holds, together with (a)–(c) of Theorem RO.

*Proof.* There are two places where (R2^orb) entered.
- Prop. T: this is replaced verbatim by (T_c).
- Lemma 1.1, used in Theorem RO Step 0 and Step 6.

Under (R2) alone, Lemma 1.1 must be replaced as follows.
- **Product-type G.** Π_t := H_t restricted to strata. It is a homeomorphism, and it maps pieces to pieces by round8_q7 Lemma S″.
- **Non-product G.** Pieces of Â_t are components of ξ_G^{-1} of the curves H_t(components of A_0). There are finitely many of them, and each is mapped finitely onto its image. Step 0 then still yields finitely many families of pieces. However, the continuous choice E_t needed in Step 6 is available only away from the "twin" branching (round8_q7, Caveat after Lemma S″).

Hence (b), the finiteness, holds in all strata. (c), constancy, holds in product-type strata. In non-product strata it holds after replacing Δ by the finite branched cover of Δ on which the lifts are continuous; finiteness, which is all that (Rig) asks for, is unaffected. ∎

**What (T_c) amounts to.** By Lemma CL, (T_c) holds iff two conditions hold:
- (α) for every t, the transported cone data of Λ_E dominate the joint minimal orbifold structure of ν_t. Equivalently, no cone point of the joint vertex map is created, split or moved away from the transported Λ_E cone points;
- (β) the joint monodromy is constant in t, as a coset-valued homomorphism.

This is (O_G) of round7_q9 with the *specific* structure Λ_E. Lemma J0 is what makes this structure available for all vertices at once.

**Sketch (not proved): (T_c) under (★_J) and (★∞_J).**
- The joint lift F_0 of Lemma J0 is an injective holomorphic immersion H → T_G, because its j-coordinate is.
- So the local analysis of round6_q7 (Lemma N, Prop. L1, Cor. L2, Prop. L3) applies with T replaced by T_G, f_0 by F_0, and Stab(X̂) by Stab_{Mod_Π}(F_0(c̃)) modulo S. It only needs a smooth disc germ L with faithful action under (★).
- **(★_J) at c ∈ Ê_0:** every element of Stab_{Mod_Π}(F_0(c̃)) lies in R(λ) for some λ ∈ Stab_Λ(c̃), up to S.
- **(★∞_J):** the boundary points of E_0 in ∏M̄_w have no effective automorphisms.
- If (★_J) and (★∞_J) hold everywhere, Theorem L's argument gives (α) and (β), hence (T_c) and (Rig) for that piece.

This inherits the "careful sketch" status of Theorem L §3.3, and I have not re-verified Prop. L1 in the product target. In particular it covers pieces whose joint image, at t = 0, avoids the orbifold locus of ∏M_w (modulo generic automorphisms) and whose boundary points have no automorphisms (round7_q9 §2.5).

**What remains open under (R2).** The three mechanisms (cross), (fix), (ram) of round6_q7 §4, now for the joint map: cone points of the joint vertex map of E_t appearing at t ≠ 0 at points that are not transported cone points of Λ_E. Lemma J0 excludes such points at t = 0 only. The dead ends recorded earlier still apply:
- local data cannot exclude these mechanisms (round6_q7 §4, round9_q9 Lemma Loc);
- area and Schwarz–Pick inequalities go the wrong way (round7_q7 §4).

## 8. Final status

**Proved here**, under (R1) and (R2), with the prior results TV and Corollary Φ̂ of round8_q10 used as stated and not re-proved:
- **Lemma CS, Lemma CL** (§2): elementary lifting lemmas.
- **Lemma J0** (§3, no (R2^orb)):
  - at t = 0, the whole vertex map of every piece, in any stratum, lifts holomorphically over the Veech-type orbifold H/Λ_E;
  - the Teichmüller coordinate of this lift is an isometric embedding onto a Teichmüller disc;
  - the monodromy is coset-valued (cosets of the finite pointwise stabiliser S).
  - Consequences: joint (H_0); the joint minimal orbifold structure at t = 0 is dominated by Λ_E; Example Z is not a boundary piece of a totally geodesic V_0.
- **Proposition T** [orb] (§4): (R2^orb), read as (a)–(d) of §1, implies (O_G), (O), (O_u) and (OT) for every piece, with the orbifold structure Λ_E.
- **Lemma R*′** [orb] (§5): Lemma R* with coset-valued monodromy and with orientation reversal excluded. It gives (Rig-v) and a biholomorphism ā_t : Ê_0 → Ê_t.
- **Theorem RO** [orb] (§6): (Rig) for every admissible family under (R2^orb), in product and non-product strata. Moreover:
  - M(E_t) = M(E_0);
  - K(E_t) = K(E_0);
  - puncture values lie in a fixed finite set.
- **Proposition C** (§7, coarse reading): (Rig) follows from the transport hypothesis (T_c) for the Λ_E structure.

**Cited from memory:**
- Royden, Earle–Kra / Gardiner;
- Bers' classification;
- Thurston's stretch theorem (finite-area version);
- Selberg's lemma;
- uniformisation of hyperbolic 2-orbifolds and lifting of orbifold homeomorphisms;
- Bers embedding (boundedness of T_w);
- Cartan's linearisation and quotient theorem;
- density of intersection points of axes of a lattice;
- Imayoshi–Shiga finiteness, with the caveat on its scope stated in §6.

**Dependencies not re-checked:**
- Theorem TV and Corollary Φ̂ (round8_q10), in particular:
  - the choice φ̂(i) = P̂ with P̂ generic on E;
  - TV item 2, E^ν = H/Λ_E with Λ_E ⊂ Γ′;
  - Lemma PA, which round8_q10 itself cites from memory.
- The claim that under (R2^orb) MS11♭ holds (round11_q4), and the chain step "(Rig) + MS11♭ ⇒ the problem's claim" (entry 124).
- If these hold, Theorem RO completes a proof of the problem's claim **under the reading (R2^orb)** of §1. That conclusion is conditional on those prior results and is not established here.

**Weakest form of (Rig) obtained:**
- Unconditionally on the orbifold reading: (Rig) for every piece satisfying (T_c) (Prop. C). In sketch, (T_c) holds for every piece satisfying (★_J) and (★∞_J).
- Under (R2^orb): (Rig) in full, with constancy of the triples.

**Open (named):**
1. **(Rig) under the coarse reading (R2)**: equivalently (T_c) for every piece. Precisely, can the joint vertex map of E_t, t ≠ 0, acquire cone points not transported from Λ_E (mechanisms cross/fix/ram of round6_q7 for the joint map)?
2. **Local-to-global for (R2^orb)**: does the purely local formulation (isotropy-preserving local lifts at each z ∈ closure(V_0)) imply the global equivariant lift (a)–(d) of §1?
3. The exact scope of Imayoshi–Shiga finiteness for targets M_{h,m}[N] with marked points (h = 0 or (h,m) = (1,1) included?).
4. Realisability questions Q1/Q2 of earlier rounds. For Example Z′, whether J_0∘q lifts to T_{1,1} (Lemma J0's criterion).

**Entry 82 overall: not proved in general; proved under (R2^orb) (partial: conditional on that reading and on round8_q10's TV/Φ̂); open under the coarse reading.**

=== END OF ANSWER round12_q9 ===
