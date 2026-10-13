# round11_q6 — answer (work in progress)

Plan/status: (1) check the derivation MS11 + listed results + (Rig) => problem claim; (2) record the logical status of MS11 (a refutation would be a counterexample to the problem itself); (3) attack MS11 with a first move nobody has used: **deformation theory of closure(V_0) as a point of the stratified Douady space (normal-sheaf / Zariski-tangent analysis)**; (4) side result: Thurston length-spectrum dominance applied to the Teichmüller vertex of a piece (conditional lemma TR), and why it cannot see the constant factor.

Current status: not proved (details below).

## 1. Derivation: MS11 (+ listed results + (Rig)) => problem claim, under (R1),(R2)

Suppose, for a contradiction, that t -> Y_t is non-constant. It is holomorphic (entries 2/19), so the MS11 hypothesis "Y non-constant" holds. (Rig) is assumed (entry 82, still OPEN). So everything below is **conditional on (Rig)**.

1. *Start.* Take a generic point P of ∂V_0 (a smooth point of closure(V_0), lying only on ∂V_0, Δ_Γ of product type). Let x be the label of the Y-vertex in Def(P). Near P, H maps ∂V_0 × Δ onto closure(𝒱) ∩ (Δ_Γ × Δ). So every point of the transport family of the lifted branch of ∂V_0 lies over ∂V_t. There x is intact and F_x ≅ Y_t. Hence x is Y-persistent on every transport sheet of that branch.
2. *Chain.* Proposition K_w (entries 85, 98) gives a finite walk chain of boundary pieces from P to an endpoint Q_0 where the tracked Y_0-copy MERGEs (the label is not intact along the leaving branch) or MOVEs (it is intact but F_x is non-constant). By Lemma S̃′ (entry 98), at each transition and at the endpoint the entering lift β̃ and the leaving lift b̃ lie in one irreducible component S of q^{-1}(closure V_0) ∩ B. This is MS11's (S).
3. *Interior transitions.* By Cor. IMOV_all (entry 99), a transition lying in the stratum of either adjacent piece has equal entering and leaving lifts, so it is trivial. The remaining transitions, and Q_0, are punctures of both adjacent pieces. This is MS11's (P).
4. *Travel.* Along a piece between consecutive transitions, persistence moves sheet by sheet (entry 100, Lemma B1, transfer along travel intervals). Persistence is constant on whole components (entry 87, Lemma T). So the tracked label arrives at the next transition Y-persistent on some transport sheet of the entering lift. That is exactly MS11's datum "x Y-persistent on some transport sheet of β̃".
5. *Product-type transitions.* These are handled by Lemma PT (entry 86: there are no twins at product points) and Theorem R (entry 87). The run's chain uses them in this way, and I see no gap here, *provided* "aligned" in Theorem R is what Lemma PT delivers at product-type points. That identification is asserted in the run's chain description; I have not re-verified it.
6. *Non-product puncture transitions.* MS11 moves Y-persistence from β̃ to a sheet of b̃.
7. *Endpoint.* Suppose Q_0 is of product type. Then Theorem R (entry 87; terminal MERGE or puncture-MOV) gives Y ≡ const directly, a contradiction. Otherwise MS11 applies at Q_0. Its conclusion together with Lemma B1(a) says that at t = 0 the label x is intact along b̃ with F_x ≡ Y_0. This contradicts MERGE (x not intact along b̃) and MOV (F_x non-constant along b̃). The labels are the same throughout: the contradiction concerns the single chart label x of Def(Q_0) that MS11 tracks.

**Verdict on Task 1.** The derivation goes through, modulo the cited statements and with two caveats.
- (a) It is conditional on (Rig), which is OPEN.
- (b) It needs the endpoint of K_w to be a *genuine* MERGE/MOV of the *same label* x that is persistent on the entering sheet. When the entering transport family is reducible, the label could change between sheets: entry 100 repairs silent label switches only by adding R(D) to Σ. If that repair holds, there is no gap.

## 2. Logical status of MS11 (important for "refute")

MS11 has "t -> Y_t is non-constant" among its hypotheses. So:

- If the problem's claim is true (under (R1),(R2),(Rig)), there are no admissible data satisfying MS11's hypotheses, and MS11 is **vacuously true**.
- Hence MS11 is implied by the claim. By §1, MS11 implies the claim under (Rig). So under (Rig), MS11 and the problem are equivalent in strength (compare entry 103).
- Consequently, **any explicit admissible configuration refuting MS11 is a counterexample to the problem itself** (an admissible family with Y non-constant). MS11 cannot be "implausible" unless the problem is false. Equally, no local argument at Q can prove MS11: by Lemma Loc (entry 93), local data never forces Y constant. Every proof of MS11 must use global information about closure(V_0). This is why I chose a global first move (deformation theory of the compact surface closure(V_0)).

## 3. First move: deformation theory of V̄_0 := closure(V_0) in the Douady space of M̄_g

**Lemma 3.1 (the family is a holomorphic curve in the Douady space).** Assume (R1) and Lemma Red (entry 80: the central fibre of closure(𝒱) → Δ is reduced). Then t ↦ closure(V_t) is a holomorphic map from Δ to the Douady space 𝒟 of compact analytic subspaces of the coarse space M̄_g, sending 0 to [V̄_0].

*Proof.*
- closure(𝒱) is the closure of the connected 3-dimensional manifold 𝒱, so it is irreducible. No component of it lies in a fibre of t.
- A reduced space over a smooth curve with no component in a fibre has a structure sheaf with no t-torsion, so it is flat over Δ.
- By (R1) the fibres are set-theoretically closure(V_t). The fibre over 0 is reduced by Lemma Red, so scheme-theoretically it is V̄_0.
- Away from 0, generic reducedness alone does not give reduced fibres. However, the parameter value 0 is not special: Lemma Red applied at any base point t_0 gives reducedness of every fibre. If Lemma Red is only stated at 0, use the fibres as they are. The map is still holomorphic into 𝒟, and only its value at 0 matters below.
- The universal property of 𝒟 gives the map. ∎

**Proposition 3.2 (rigid case).** Suppose [V̄_0] is an isolated point of 𝒟. This holds, for example, if the Zariski tangent space H^0(V̄_0, 𝒩), with 𝒩 = Hom(I/I^2, O_{V̄_0}), is 0. Then V̄_t = V̄_0 for all t, so ∂V_t = ∂V_0 and Y_t = Y_0.

*Proof.* A holomorphic map from the connected disc Δ to 𝒟 with value [V̄_0] at 0 is constant if [V̄_0] is isolated. Then H_t(closure(V_0) ∩ Δ_Γ) = closure(V_0) ∩ Δ_Γ, and π_i of this set is {Y_0}. ∎

This settles the claim for every *rigid* V̄_0. It is partial: rigidity is an extra hypothesis.

**3.3 Reformulation (sketch, not fully verified).** Let 𝒟^str be the germ at [V̄_0] of the locally closed analytic subset of 𝒟 defined by the incidence conditions (i), (ii): for each stratum G, the intersection with Δ_G has the same dimension. On 𝒟^str the map Z ↦ π_i(Z ∩ Δ_Γ) is a well-defined holomorphic map 𝒴: 𝒟^str → M_{g_i,n_i}, by the argument of entry 19 applied to the universal family. The problem's claim is then equivalent to:

> (D) 𝒴 is constant on every irreducible component of 𝒟^str through a totally geodesic [V̄_0].

**3.4 What first-order analysis can give, and why this move dies.** Let v be the leading term of the curve t ↦ [V̄_t]: v ∈ C^N with γ(t) = t^m v + O(t^{m+1}) in an embedding of the germ. It lies in the tangent cone, hence in H^0(V̄_0, 𝒩).

- Along ∂V_0 (generic points, product chart), the log normal sheaf fits into the sequence 0 → O^{|E(Γ)|-1} → 𝒩^log|_{∂V_0} → N_{∂V_0/Δ_Γ} → 0. Composing with the projection N_{∂V_0/Δ_Γ} → T_{Y_0} M_{g_i,n_i} gives a holomorphic map on the compact curve closure(∂V_0) (the Y-vertex stays intact at its cusps, entry 48). It is therefore a constant vector c(v).
- If Y_t = Y_0 + t^k c' + …, then k ≥ m. If k = m, then c' = c(v).
- On V_0, totally geodesic means the conormal of V_0 is Q/W, where Q is the bundle of quadratic differentials (= Ω_{M̄_g}(log ∂) restricted) and W is the rank-2 subbundle of differentials whose Teichmüller discs lie in V_0.
- So a first-order deformation is a holomorphic functional σ on Q|_{V̄_0} that kills W. Its Y-component is c(φ) = σ(φ) for φ in Q(Y_0), the quadratic differentials supported on the Y-component.
- To force c = 0 one needs a global section s of Q over V̄_0 that equals φ at a point of ∂V_0 and lies in W at some other point. Then σ(s) is a holomorphic function on compact V̄_0, hence constant, and that constant is both c(φ) and 0.
- I could not produce such sections. H^0(V̄_0, Q) is not controlled by anything the run has proved.

Even c(v) = 0 for all v would only give k > m, not k = ∞. The tangent-cone information is first order, while (D) is a statement about the whole germ, and total geodesy holds only at the single point [V̄_0] of 𝒟^str. So this move yields Prop. 3.2 (rigid case) and the reformulation (D), but no proof of MS11.

**Dead end, recorded:** the deformation-theoretic move cannot prove MS11 without either a vanishing theorem H^0(V̄_0, (Q/W)^∨_{log}) = 0, which would prove much more (rigidity of V̄_0), or a higher-order analysis of 𝒟^str. Neither is available.

## 4. Second move: Thurston length-spectrum dominance for the Teichmüller vertex of a piece

**Setting.**
- E_0 is a 1-dimensional piece in a product-type stratum Δ_G, and E_t is its transport. A homeomorphism of curves maps irreducible components to irreducible components (they are the closures of the components of the complement of the non-manifold points). So H_t maps closure(E_0) ∩ Δ_G onto closure(E_t) ∩ Δ_G, and it induces homeomorphisms between the normalisations (it maps local branches to local branches), with punctures going to punctures.
- K_t is the normalisation of E_t, a punctured compact Riemann surface.
- By Theorem TV (entry 70) there is a vertex j such that f_0 := π_j ∘ ν_0 : K_0 → M_j is a proper orbifold covering of a Teichmüller curve C = H/Γ_C ⊂ M_j, and the ends of K_0 map to cusps.
- f_t := π_j ∘ ν_t : K_t → M_j.

**Hypothesis (OT).** The orbifold structure that f_t induces on K_t (cone points and their orders, read off from local lifts to T_j) is carried by H_t to that of K_0. Then the orbifold fundamental groups are all identified with one group G := π_1^orb(K_0). G is a lattice, because K_0^orb = H/G is a finite-area orbifold cover of C.

**Lemma TR.** Under (R1), (R2) and (OT), for every t the following hold.
- K_t is isometric to K_0, by an isometry homotopic to the map induced by H_t.
- f_t composed with this isometry equals f_0.

In particular closure(π_j(E_t)) = closure(π_j(E_0)) = C̄. The Teichmüller-vertex factor of every piece is t-independent.

*Proof.*
1. *Lifts.* Lift f_t to f̃_t : H → T_j, equivariant for ρ_t : G → Mod_j, and choose the lifts continuously in t. Mod_j is discrete and G is finitely generated, so ρ_t = ρ is independent of t. Let G_t ⊂ PSL_2(R) be the Fuchsian group of K_t^orb, marked by G.
2. *Contraction.* By Royden's theorem (also for T_{g,n}; cited from memory) the Teichmüller metric is the Kobayashi metric. The Poincaré metric, normalised to curvature -4, is the Kobayashi metric of H. Holomorphic maps contract Kobayashi distance, so d_T(f̃_t z, f̃_t w) ≤ d_H(z, w).
3. *t = 0.* The map f̃_0 is an isometric holomorphic embedding onto the Teichmüller disc D_0 of a Veech surface (X, q). ρ(G) preserves D_0 and acts on it as G acts on H. For hyperbolic γ ∈ G, ρ(γ) is affine with hyperbolic derivative, hence pseudo-Anosov, with Teichmüller translation length τ(ρ(γ)) = ℓ_0(γ).
4. *Bers (cited from memory).* For a pseudo-Anosov φ, d_T(x, φx) ≥ τ(φ), with equality exactly on the unique φ-invariant geodesic A_φ. Equality means the extremal map x → φx is a Teichmüller self-map of x in the class φ with dilatation λ_φ. Such a map is affine for some q on x, so x lies on the invariant geodesic, and that geodesic is unique. Here A_{ρ(γ)} ⊂ D_0.
5. *Length dominance.* For z on the axis of γ in H (acting through G_t):
   τ(ρ(γ)) ≤ d_T(f̃_t z, ρ(γ) f̃_t z) = d_T(f̃_t z, f̃_t(γz)) ≤ ℓ_t(γ).
   So ℓ_t(γ) ≥ ℓ_0(γ) for every hyperbolic γ.
6. *Thurston (cited from memory, "Minimal stretch maps between hyperbolic surfaces").* For complete finite-area marked hyperbolic structures X, Y on the same surface, sup_γ ℓ_Y(γ)/ℓ_X(γ) ≥ 1, with equality iff X = Y.
   - Pass to a torsion-free normal subgroup G' of finite index in G (Selberg). Both structures restrict to marked structures of the same type on H/G'. By step 5, sup ℓ_0/ℓ_t ≤ 1, so the two G'-representations are conjugate by some A.
   - For g ∈ G, the element ρ_0(g)^{-1} A ρ_t(g) A^{-1} centralises the lattice ρ_0(G'), so it is trivial.
   - Hence G_t = A G_0 A^{-1} as marked groups. Identify them, so ℓ_t = ℓ_0.
7. *Image lies in D_0.* Steps 4 and 5 are now equalities. Hence f̃_t(z) ∈ A_{ρ(γ)} ⊂ D_0 for every z on the axis of every hyperbolic γ. The axes of hyperbolic elements of a lattice are dense in H, and D_0 is closed. So f̃_t(H) ⊂ D_0.
8. *Conclusion.* D_0 is a closed complex submanifold and f̃_0 : H → D_0 is biholomorphic. So g_t := f̃_0^{-1} ∘ f̃_t is a holomorphic, G-equivariant self-map of H.
   - If g_t were not an automorphism, Schwarz–Pick would make it strictly contracting. Then for z on an axis, d(g_t z, γ g_t z) < ℓ_0(γ) = τ, which contradicts step 4.
   - So g_t is an automorphism commuting with the lattice G, and therefore g_t = id. Thus f̃_t = f̃_0. ∎

**Status of TR:** proved under (OT). Without (OT), cone points of K_t^orb could appear or disappear at t ≠ 0. I have not ruled this out, and the run has no statement covering it.

**Why TR cannot reach Y (dead end for MS11).**
- TR pins only the vertex j whose map is a Teichmüller-isometry. The constant vertex Y never enters it: π_i is constant on ∂V_t, so there is no length spectrum to compare.
- At a puncture-MOV endpoint of MS11, the moving Y_0-copy cannot be a Teichmüller vertex of the leaving piece. By TV, Teichmüller-vertex ends go to cusps of M̄_{g_i,n_i}, but F_x(Q_0) ≅ Y_0 is interior. So the moving copy is a non-Teichmüller moving vertex. Entry 81 (Examples Z, Z′) shows that fixing the Teichmüller vertex does not pin such vertices or their puncture values.
- What TR does add is that every cusp of every piece has a t-independent j-component. This supplies the "fixed Teichmüller vertex" hypothesis that entry 81 assumes, rather than taking it as given.

## 5. Final status

**Proved here (modulo cited inputs, all quoted from memory).**
- §1: MS11 together with the listed run statements implies the problem's claim under (R1), (R2) and (Rig), with caveat (b) on label tracking across sheets, which the R(D) repair of entry 100 covers.
- §2: MS11 is vacuous if the problem is true. Hence any refutation of MS11 is a counterexample to the problem, and no purely local argument can prove MS11 (entry 93).
- Prop. 3.2: the claim holds whenever [V̄_0] is an isolated point of the Douady space, e.g. if H^0(V̄_0, 𝒩) = 0. This uses (R1) and Lemma Red. It is partial, because rigidity is an extra hypothesis.
- Lemma TR: Thurston/Bers/Royden rigidity of the Teichmüller vertex of any product-type piece, under (OT). It is partial and does not touch Y.

**Sketched only.** §3.3: reformulation (D), that the claim is equivalent to the constancy of 𝒴 on the stratified Douady germ. §3.4: the first-order relation c(v) = Y-component of the leading normal field.

**Open.**
- MS11 itself, and hence the problem: **not proved**.
- (Rig) (entry 82).
- Whether H^0(V̄_0, (Q/W)^∨_log) = 0 for totally geodesic V̄_0. This would prove rigidity of V̄_0 and with it the claim.
- Whether (OT) holds automatically.

Final: **not proved** (open).

(Remark on Lemma 3.1: Prop. 3.2 uses only that the fibres form a flat family through the reduced fibre V̄_0. If the map is constant, then every fibre equals V̄_0 as a subspace, and therefore closure(V_t) = V̄_0 as sets. Reducedness at t ≠ 0 is not needed.)

=== END OF ANSWER round11_q6 ===

