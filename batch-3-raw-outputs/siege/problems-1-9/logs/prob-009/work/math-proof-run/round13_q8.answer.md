# round13_q8: attempt on (Rig) under the coarse reading (R2)

## Plan/status line (written first)
Plan:
1. Remove the dependence of (T_c) on the transport H. I replace it by a **pointwise** condition (P_t) that refers to time t only. Then I show that (P_t) holding at a non-discrete set of times already gives (Rig) for the piece (Proposition U).
2. Check whether the global count available under (Rig-v) (Riemann–Hurwitz over the Teichmüller curve, plus Lemma P0) excludes the cone-point mechanisms. It does not (Lemma RH, and §4).
3. Record a correction to round12_q9 Proposition C, concerning constant vertices.

Final status (also stated in §5): **not proved; open.** §§1–3 contain proved reductions and corrections.

Readings (R1) and (R2) are adopted throughout: coarse reading, no (R2^orb). G is a product-type stratum unless stated otherwise. Prior results are used as quoted in the brief and are not re-proved:
- Lemma R0/W: W is irreducible, 2-dimensional and proper over Δ, with W_t = closure(E_t).
- L1′: whether a vertex is non-constant along E_t does not depend on t.
- Lemma S″, Lemma CD/Cor. CD1, Lemma P0, Lemma Deg.
- Theorem TV, Lemma J0, Lemma CS, Lemma CL.
- Lemma R*′ (its proof only).
- Imayoshi–Shiga (IS), cited from memory as in round12_q9 §6, with the same caveat on scope.

## 1. Correction to round12_q9 Proposition C: constant vertices must be left out of (T_c)

The brief states (T_c) for maps into T_G = ∏_{w∈V(G)} T_w, with equivariance for "some (equivalently every) g ∈ R(θ_tλ)". For a constant vertex u ∉ M(E_0), the u-coordinate of F_0 is a point ỹ_u(0) lying over the constant value c_u(0). The pointwise stabiliser S of F_0 contains {1} × … × Stab(ỹ_u(0)) × … × {1}. So R(λ) contains elements whose u-component is any element of Stab(ỹ_u(0)).

Consequences:
- The "every g" version of (T_c) at time t forces Stab(ỹ_u(0)) ⊂ Stab(ỹ_u(t)). It is therefore **false** whenever the constant component c_u(t) moves off a curve with extra automorphisms. That is exactly the kind of motion the problem is about, so "every" is not equivalent to "some".
- The "some g" version is harmless for constant vertices, because the u-component can be taken to be 1.

Theorem RO only uses the coordinates u ∈ M(E_0). The vertex j belongs to M(E_0). So from now on all lifts are taken into T_M := ∏_{u∈M} T_u with M := M(E_0). Write Mod_M := ∏_{u∈M} Mod_u (pure mapping class groups) and p_M : T_M → ∏_{u∈M} M_u. This is the form in which the reduction is stated below.

## 2. A pointwise, H-free sufficient condition for (Rig) (Proposition V, proved)

**Setting.**
- G is of product type, E_0 is a piece at t = 0, E_t := H_t(E_0) (round8_q7 Lemma S″), and M := M(E_0). By L1′, M(E_t) = M.
- By Theorem TV there are: a vertex j ∈ M; the Teichmüller curve C ⊂ M_j with normalisation κ : C^ν = H/Γ′ → M̄_j (Γ′ a lattice); and the Teichmüller disc D : H → T_j with κ∘q_{Γ′} = u := (projection of D).
- K(E_t) := closure of pr_M(E_t) ⊂ ∏_{u∈M} M̄_u. K^j_t := closure of π_j(E_t).
- Ê_t is the normalisation of E_t, with ν_t : Ê_t → E_t. It is a compact Riemann surface minus finitely many points (round12_q9 §1).

**Condition (V_t) at a single time t.** The following three conditions hold:
- (i) K^j_t = C̄. Then π_j∘ν_t lifts to a holomorphic p_t : Ê_t → C^ν, by the universal property of normalisation: Ê_t is smooth and the map is non-constant.
- (ii) p_t is *orbifold-unramified* for the orbifold structure H/Γ′ on C^ν. That is, p_t has ramification only at points over orbifold points y of C^ν, with local degree dividing the order m_y. In addition, p_t extends to the compactifications with punctures going to cusps and no point of Ê_t going to a cusp.
- (iii) Give Ê_t the pulled-back orbifold structure O_t, so that by (ii) O_t = H/Λ_t for a subgroup Λ_t ⊂ Γ′ of finite index, with p_t induced by the inclusion. Then the map pr_M∘ν_t : Ê_t → ∏_{u∈M} M_u lifts to a holomorphic map F_t : H → T_M with p_M∘F_t = pr_M∘ν_t∘q_t, where q_t : H → H/Λ_t = Ê_t.

By Lemma CL, (iii) is equivalent to the existence of a continuous lift. Locally it is equivalent to: at every point of Ê_t, the minimal orbifold order of the joint M-map divides the cone order of O_t there, with order 1 at regular points.

**At t = 0**, (V_0) holds. (i) and (ii) are TV items 1–3. (iii) is Lemma J0(i), projected to T_M; here Λ_0 = Λ_E, and q_0 is q composed with γ_0 as in J0.

**Proposition V.** Let 𝒯_V := {t ∈ Δ : (V_t) holds}. Then:
- (a) There is a countable set 𝒦_V of irreducible curves in ∏_{u∈M} M̄_u, depending only on (G, M, Γ′, D), such that K(E_t) ∈ 𝒦_V for every t ∈ 𝒯_V.
- (b) If 𝒯_V is uncountable, then K(E_t) = K(E_0) for all t ∈ Δ. In particular (Rig) holds for the family of E_0, with the single triple (G, M, K(E_0)), and so do the conclusions of round8_q7 Cor. S′ (fixed puncture values of the non-constant vertices).
- (c) Either 𝒯′ := {t : K(E_t) ∈ 𝒦_V} = Δ, or 𝒯′ is countable, and then 𝒯_V ⊂ 𝒯′ is countable.

*Proof.*

**Step 1 (the source is one of finitely many orbifolds).** Fix t ∈ 𝒯_V. By (i) and Lemma Deg (prior result; it uses K^j_t = K^j_0 = C̄), deg p_t = d_0. By (ii), Λ_t is a subgroup of Γ′ of index d_0, up to conjugacy in Γ′; conjugating changes nothing below. A finitely generated group has only finitely many subgroups of a given index, so Λ_t belongs to a finite set 𝔏 of subgroups of Γ′. Note that the complex structure of Ê_t is then determined by Λ_t: Ê_t ≅ H/Λ_t.

**Step 2 (normalising the j-coordinate).** pr_j∘F_t and D are holomorphic lifts H → T_j of the same map κ∘q_{Γ′} = π_j∘ν_t∘q_t (Λ_t ⊂ Γ′). By Lemma CS, pr_j∘F_t = h∘D for some h ∈ Mod_j. Replace F_t by (h^{-1}, 1, …, 1)∘F_t. Then pr_j∘F_t = D.

**Step 3 (coset monodromy and a torsion-free homomorphism).**
- For λ ∈ Λ_t, F_t∘λ and F_t are holomorphic lifts of the same map, since q_t∘λ = q_t. By Lemma CS, R_t(λ) := {g ∈ Mod_M : F_t∘λ = g∘F_t} is a coset of the finite group S_t := {s ∈ Mod_M : s∘F_t ≡ F_t}.
- As in Lemma J0(iii), R_t(λμ) = R_t(λ)R_t(μ), and R_t(λ) ⊂ N(S_t). So λ ↦ R_t(λ) is a homomorphism Λ_t → N(S_t)/S_t.
- Fix N ≥ 3 and Mod[N] := ∏_{u∈M} Mod_u[N], which is torsion-free and of finite index I in Mod_M.
- Let Λ_t^♮ be the intersection of the following two subgroups:
  - a torsion-free normal subgroup of finite index in Λ_t (Selberg);
  - the preimage of (N(S_t) ∩ Mod[N]S_t)/S_t.

  Λ_t^♮ has finite index in Λ_t and is torsion-free.
- For μ ∈ Λ_t^♮, R_t(μ) ∩ Mod[N] is a single element r_t(μ). It is nonempty by construction. Two such elements would differ by an element of S_t ∩ Mod[N], which is trivial: S_t is finite and Mod[N] is torsion-free. The map r_t : Λ_t^♮ → Mod[N] is a homomorphism, and F_t∘μ = r_t(μ)∘F_t.

**Step 4 (countably many homotopy data).**
- Λ_t^♮ is a finite-index subgroup of a member of the finite set 𝔏. A finitely generated group has countably many finite-index subgroups.
- r_t is a homomorphism from a finitely generated group into the countable group Mod[N], so there are countably many choices.
- Hence the pair (Λ_t^♮, r_t) lies in a countable set 𝒫 that does not depend on t.

**Step 5 (Imayoshi–Shiga).**
- R_t := H/Λ_t^♮ is a Riemann surface of finite type, being a finite cover of the finite-area orbifold H/Λ_t. It depends only on Λ_t^♮.
- For u ∈ M, F_t^u := pr_u∘F_t is r_{t,u}-equivariant, so it descends to a holomorphic ḡ^u_t : R_t → M_u[N] := T_u/Mod_u[N]. This is a complex manifold and a K(π,1), since T_u is contractible.
- ḡ^u_t is non-constant: it covers the map (pr_u∘ν_t) composed with R_t → Ê_t, and u ∈ M = M(E_t) by L1′.
- *Fixed free homotopy class.* Two holomorphic maps R_t → M_u[N] whose lifts H → T_u are equivariant for the same homomorphism r_{t,u} are homotopic. The homotopy is pointwise Teichmüller-geodesic interpolation between the two lifts. It is continuous, because Teichmüller geodesics are unique and depend continuously on their endpoints. It is equivariant, because Mod_u acts by isometries. (Cited from memory: uniqueness and continuity of Teichmüller geodesics.)
- So by (IS), for each (Λ^♮, r) ∈ 𝒫 and each u ∈ M, there are only finitely many possibilities ψ_{u,1}, …, ψ_{u,k} for ḡ^u_t.

**Step 6 (the image).**
- p_M∘F_t(H) = pr_M∘ν_t∘q_t(H) = pr_M(E_t), since q_t is onto Ê_t.
- Also p_M∘F_t = (∏_u (M_u[N] → M_u)∘ḡ^u_t)∘(H → R_t).
- So pr_M(E_t) is the image of R_t under one of countably many explicit maps, indexed by an element of 𝒫 and a choice of ψ_{u,i} for each u.
- Let 𝒦_V be the set of closures of these images that are irreducible curves. It is countable and contains K(E_t). This proves (a).

**(b) and (c).** These are Cor. CD1 / Lemma CD of round10_q9 (prior result, product case) applied with M = M(E_0) and the countable class 𝒦_V:
- 𝒯′ = ∪_{C∈𝒦_V} T_C, where T_C = {t : K(E_t) ⊂ C}.
- Each T_C is either Δ or closed discrete. A closed discrete subset of Δ is countable.
- If some T_C = Δ, then K(E_t) = C for all t; taking t = 0 gives C = K(E_0), using that K(E_t) is an irreducible curve for every t (L1′, Lemma S″).
- Otherwise 𝒯′ is a countable union of countable sets, hence countable.

Finally 𝒯_V ⊂ 𝒯′ by (a). ∎

**Remarks.**
1. Proposition V uses neither H_t-transported cone points, nor any isotopy class θ_t, nor Lemma R*′. Condition (i) together with orbifold-unramifiedness (ii) pins the complex structure of the source to one of finitely many orbifolds H/Λ, Λ ∈ 𝔏. Round12_q9 got this pinning from Thurston's theorem through R*′.
2. Compared with Proposition C of round12_q9, it is weaker in three ways:
   - it is pointwise in t;
   - it needs only uncountably many times, not all t;
   - the monodromy is unconstrained (no "constant coset monodromy" requirement (β)).

   Condition (β) of the brief has disappeared. What remains is (α), split into (ii) and (iii).
3. (i) for uncountably many t implies (i) for all t, by Lemma CD with C = C̄ and M = {j}. That is (Rig-v). So in effect:

   **(Rig) for E_0 ⟸ (Rig-v) for E_0, and (ii) and (iii) for uncountably many t.**
4. Conversely, if (ii) or (iii) fails for all but countably many t, then by (c) K(E_t) ∉ 𝒦_V for all but countably many t, unless K(E_t) ≡ K(E_0).
   - This alone is not a contradiction. A constant joint image can be reached by a varying, more ramified source map, as in Prop. X of R7-7.
   - So (ii)/(iii) are sufficient conditions and not necessary ones.

## 3. What (Rig-v) gives for condition (ii): Lemma RH

**Lemma RH.** Assume (Rig-v) for E_0, i.e. K^j_t = C̄ for all t. Let p_t : Ê_t → C^ν be as in (V_t)(i), and C° := C^ν (the open orbifold curve H/Γ′, without cusps). Then:
- (a) For every t, p_t extends to the compactifications. Moreover p_t^{-1}(cusps) is exactly the set of punctures of Ê_t, so p_t : Ê_t → C° is a proper holomorphic map of degree d_0.
- (b) The total ramification Σ_{x∈Ê_t}(e_x − 1) of p_t equals that of p_0, call it R_0, for every t.
- (c) (ii) holds at t iff every ramification point x of p_t lies over an orbifold point y of C° with e_x | m_y. In that case χ^orb(O_t) = d_0·χ^orb(H/Γ′) = χ^orb(O_0).
- (d) For each orbifold point y, ρ_y(t) := d_0 − #p_t^{-1}(y) (the ramification over y) is upper semicontinuous in t. Hence for t near 0, the ramification over orbifold points satisfies Σ_y ρ_y(t) ≤ R_0. The defect b_t := R_0 − Σ_y ρ_y(t) ≥ 0 is the ramification of p_t over non-orbifold points.

*Proof.*

**(a), interior points.** Let x ∈ Ê_t be an interior point. Its j-coordinate lies in M_j. Every point of C^ν maps into M_j, and every cusp maps into ∂M̄_j, because C ⊂ M_j is closed and H/Γ′ → M_j is proper. So no interior point goes to a cusp.

**(a), punctures.** Let P be a puncture of Ê_t. It lies on a component Π of the puncture locus 𝓟 of the normalised family 𝓦^ν, and Π surjects onto Δ (proof of Lemma P0). So Π_0 is a nonempty set of points of 𝓦^ν_0 over closure(E_0) ∖ E_0.
- By TV item 4, every end of Ê_0 has j-coordinate in ∂M̄_j. Every point of closure(E_0) ∖ E_0 is a limit along an end. So j is degenerate at the points of Π_0.
- By Lemma P0, j is then degenerate along all of Π, in particular at P.
- So P maps to a point of C̄ ∩ ∂M̄_j, which is the image of a cusp. The extension of p_t over the puncture lands on a cusp.

Properness follows. The degree is d_t = d_0 by Lemma Deg.

**(b).** Riemann–Hurwitz for the proper branched covering p_t of the finite-type surface C° gives χ(Ê_t) = d_0·χ(C°) − Σ(e_x − 1). Moreover χ(Ê_t) = χ(Ê_0), since Ĥ_t is a homeomorphism of finite-type surfaces mapping punctures to punctures.

**(c).** The first statement is the definition of orbifold-unramified. For the second, use orbifold Riemann–Hurwitz for an orbifold covering.

**(d).** Lower semicontinuity of #p_t^{-1}(y) in t. Let 𝓝 be the normalised family. The map (p, t) : 𝓝 → C^ν × Δ is finite near every point over (y, t*), because its fibres are finite and it is proper over Δ. A finite holomorphic map of 2-dimensional irreducible germs onto a smooth 2-dimensional target is open (cited from memory; Remmert's open mapping theorem). So every preimage x* of (y, t*) has preimages of (y, t) nearby, for t near t*. Distinct x* give disjoint neighbourhoods. ∎

(Ramification indices at points over non-orbifold points are not controlled by (d). This is where (ii) can fail.)

**Interpretation.** Under (Rig-v), condition (ii) fails at t exactly when one of the following happens:
- ramification of p_t leaves the fibres over the orbifold points (b_t > 0); or
- ramification redistributes inside such a fibre with e_x ∤ m_y.

The first is precisely mechanism (ram) of round6_q7 §4 with the *image fixed*: locally p_t(w) = w² − t near an orbifold point y = 0 of order 2. All of (a)–(d) are satisfied by this local model:
- at t = 0, one point with e = 2 over y, which is orbifold-unramified;
- at t ≠ 0, two unramified points over y and one simple ramification point over the regular point −t.

So the Riemann–Hurwitz bookkeeping available from (R2) cannot exclude it. A topological Hurwitz-type argument cannot exclude it either: the local monodromy around a loop enclosing y and −t is the same transposition as at t = 0.

## 4. Why I could not close the remaining gap (the dead ends of this round)

What remains, given Proposition V, is to show for uncountably many t:
- (Rig-v);
- (ii): no ramification of p_t over non-orbifold points of C, and orders dividing at orbifold points;
- (iii): the joint M-map acquires no cone points beyond those of O_t.

Under (Rig-v), Lemma RH reduces (ii) to excluding the fixed-image (ram) mechanism. I tried the following, without success.

1. **Openness/closedness in t (attack (i) of the brief).**
   - Closedness is not needed any more: Proposition V needs only uncountably many t.
   - Openness at t = 0 is exactly the local question. Round6_q7 §4 shows that it cannot be decided locally: the three local models satisfy Lemma N and the conclusions of Lemma RH.
2. **Global counts.**
   - Riemann–Hurwitz (Lemma RH(b)) and upper semicontinuity (Lemma RH(d)) are consistent with ramification drifting off the orbifold fibres.
   - The Schwarz–Pick/area and Arakelov counts go the wrong way (round7_q7 §4).
   - Lemma Deg / Lemma Red fix degrees and homology classes only.
3. **Using V_t (attack (ii) of the brief).** A moving simple ramification point x_t of p_t over a regular point of C is a point of E_t at which the j-coordinate of the stable curve has a critical point along the piece. Nothing in conditions (i), (ii) of the problem refers to critical points of vertex projections of boundary curves.
   - Lemma Loc of round9_q9 shows that boundary-local realisations, including the 2-dimensional open part, of motions of a constant factor exist.
   - I expect the analogous statement for moving ramification of a non-constant vertex, but I have not checked it.
   - Hence any exclusion must again be global along V_t, and I found no such argument.
4. **Lemma CD (attack (iii) of the brief).** Proposition V is the precise form of this attack. It turns countable-class membership into conditions (ii)/(iii). It does not prove them.

## 5. Final status

**Proved here** (readings (R1), (R2) only, product-type strata; prior results TV, J0, CS, CL, Lemma CD/CD1, L1′, Lemma S″, Lemma Deg, Lemma P0 used as quoted; (IS), Selberg, uniqueness and continuity of Teichmüller geodesics, and Remmert's open mapping theorem cited from memory):
- **§1 (correction).** The "every g" form of (T_c) in Proposition C of round12_q9 is too strong: it fails whenever a constant vertex moves off an orbifold point. Lifts should be taken into T_{M(E_0)}.
- **Proposition V.** (Rig) holds for the family of a piece E_0 (indeed K(E_t) ≡ K(E_0)) as soon as the following conditions hold for uncountably many t:
  - (i) the Teichmüller-vertex image is the Teichmüller curve C, i.e. (Rig-v);
  - (ii) the source map to C^ν is orbifold-unramified;
  - (iii) the joint map of the non-constant vertices lifts over the pulled-back orbifold.

  This needs no transport of cone points by H, no constant-monodromy condition, and not Lemma R*′. It strictly weakens the hypothesis (T_c) of Proposition C.
- **Lemma RH.** Under (Rig-v):
  - all punctures are j-degenerate at every t;
  - the total ramification of p_t is constant;
  - ramification over orbifold points is upper semicontinuous;
  - (ii) fails exactly when ramification leaves the orbifold fibres or acquires non-dividing orders.

**Not proved:** (Rig) for every admissible family under the coarse reading (R2). Equivalently, given Proposition V: (Rig-v), (ii) and (iii) for uncountably many t. (T_c) is not proved either.

**Open (named):**
1. (Rig-v) under (R2) at an image-level type jump (as in earlier rounds).
2. **Fixed-image (ram):** can the source map p_t : Ê_t → C^ν of a boundary piece of an admissible V_t acquire ramification over non-orbifold points for t ≠ 0, while V_0 is totally geodesic?
3. **Joint cone points (iii):** can the joint map of the non-constant vertices acquire cone points not present in the pulled-back orbifold (mechanisms cross/fix for the joint map)?
4. Non-product strata (twin ambiguity), not treated here.
5. The realisability questions Q1/Q2 of earlier rounds, which a counterexample would need.

Entry 82 under the coarse reading: **not proved / open.** (Partial: Proposition V, Lemma RH, and the correction in §1.)

=== END OF ANSWER round13_q8 ===

