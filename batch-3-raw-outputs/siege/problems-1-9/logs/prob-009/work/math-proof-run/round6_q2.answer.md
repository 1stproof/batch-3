# round6_q2 — answer (work in progress)

## Plan
Test MS5 on the most symmetric covering construction, V = {y^5 = quintic} ⊂ M_6 (the cyclic Z/5 covers of P^1 branched at 5 points).
Claim being checked: for this V, closure(V) ∩ ∂M̄_6 consists of a single 1-dimensional piece ∂V, which lies in one stratum Δ_Γ, plus one point P_*.
Hence the only candidate in MS5 is (G, P_0) = (Γ, P_*), and it fails (a).
Then: (1) check smoothness, since this is the only hypothesis in doubt; (2) work out the consequences for the chain.

## 0. Verdict (summary)

- **MS5 fails for the closed, totally geodesic surface V = {y^5 = f(x), deg f = 5} ⊂ M_6.** V meets every hypothesis of MS5 except smoothness: it has (at least) an A_1 singular point (Section 3). The failure is total. The only admissible candidate is (G, P_0) = (Γ, P_*), and it violates (a) for every lift R (Proposition 2.4).
- **MS5 also fails for V° := the smooth locus of V.** V° is a smooth, locally closed, 2-dimensional subvariety of M_6 that is totally geodesic in the local sense. It has the same closure as V, so the same boundary (Proposition 3.3). V° is not closed in M_6, so it violates only the word "closed" in MS5. The problem statement (verbatim copy) asks only for a "smooth subvariety". So under the reading where "subvariety" may be locally closed, V° satisfies the problem's hypotheses on V_0, and **the chain's input MS5 is false**.
- For closed and smooth V_0, MS5 is **neither proved nor refuted** here. Its conclusion depends only on closure(V_0) ∩ ∂M̄_g, which is the same for V and V°. So any proof of MS5 must use smoothness (or closedness) of V_0 at interior points of M_g in an essential way. None of the mechanisms proposed in the chain does this. In particular, step 3 of the planner's mechanism would "prove" MS5 for V as well, and so it cannot be correct as stated. The failure mechanism is identified in Section 4: the merge branch at the cusp is itself a branch of ∂V_0, along which a *twin* of Y_0 plays the role of the constant factor.
- What I can prove about the problem's own claim for V and V° is only a conditional pinning (Proposition 4.2). Whether Y_t is constant for deformations of V° is left **open**.

## 1. Cited facts (all cited from memory)

- **(C1) Covering constructions are totally geodesic.** Let p : S → S_{0,5} be a fixed branched cover of the 5-punctured sphere, with branch points among the punctures. Pull-back of complex structures gives a holomorphic map ι : T_{0,5} → T_g. If every quadratic differential q on P^1 with at most simple poles at the 5 points has holomorphic pull-back p^*q, then ι is an isometric embedding for the Teichmüller metrics. Reason: Teichmüller maps lift to Teichmüller maps with the same dilatation, and lifted differentials are holomorphic. Consequently every Teichmüller disc tangent to ι(T_{0,5}) lies in it, and the image V of M_{0,5} in M_g is totally geodesic.
- **(C2) Admissible covers (Harris–Mumford).** For cyclic covers the monodromy into the abelian group Z/d is determined by the local monodromies. So over each stable 5-pointed curve B there is exactly one admissible Z/d-cover with the given branching data, and the map to M_g extends to a morphism Φ̄ : M̄_{0,5} → M̄_g. Φ̄(B) is the stabilization of the source curve of the admissible cover. Over a component of B with special points of local monodromies m_1, …, m_r (Σ m_j ≡ 0 mod d), the cover is the Z/d-cyclic cover with those exponents. Above a node or marked point of monodromy m there are gcd(m, d) points, each with ramification index d/gcd(m, d).
- **(C3) Riemann–Hurwitz** for a connected cyclic Z/d cover of P^1 with r branch points, all of exponent prime to d: 2h − 2 = −2d + r(d − 1).

## 2. The example and the failure of MS5

**Setting.** Let d = 5 and all exponents k_1 = … = k_5 = 1. For (P^1; a_1, …, a_5) ∈ M_{0,5}, let Φ(a) be the curve y^5 = ∏_j (x − a_j).
- Σ k_j = 5 ≡ 0, so ∞ is unbranched, and by (C3) 2h − 2 = −10 + 5·4 = 10, so h = 6.
- A simple pole of q at a_j pulls back under w = z^5 to 25 z^3 dz^2, which is holomorphic. So (C1) applies.
- Let V := Φ(M_{0,5}) ⊂ M_6. Φ is S_5-invariant, because the curve depends only on the set {a_j}.

**Lemma 2.1 (V is a closed, totally geodesic surface).** V is a closed, irreducible, 2-dimensional subvariety of M_6, totally geodesic, and closure(V) = Φ̄(M̄_{0,5}) in M̄_6.

*Proof.*
1. Total geodesy is (C1).
2. Φ is quasi-finite. A genus-6 curve has a finite automorphism group, hence finitely many subgroups of order 5, hence finitely many quotient configurations up to PGL_2. So dim V = 2. V is irreducible as the image of an irreducible variety.
3. Φ̄(M̄_{0,5}) is compact, contains V, and is contained in closure(V), since M_{0,5} is dense in M̄_{0,5} and Φ̄ is continuous. Hence closure(V) = Φ̄(M̄_{0,5}).
4. Over every point of ∂M̄_{0,5} the admissible cover has a node over each base node, and the stabilization keeps at least one of them (Lemma 2.2). So Φ̄(∂M̄_{0,5}) ⊂ ∂M̄_6, and closure(V) ∩ M_6 = Φ(M_{0,5}) = V. So V is closed in M_6. ∎

**Lemma 2.2 (the boundary).** Let D_{12} ⊂ M̄_{0,5} be the divisor where a_1 and a_2 collide, and D_{12}° its open part.
- (a) Every point of Φ̄(D_{12}°) is a stable curve A' ∪_n W. Here A' is a fixed 1-pointed genus-2 curve Y_0, and W is a varying 1-pointed genus-4 curve. The node n is separating. So Φ̄(D_{12}°) ⊂ Δ_Γ, where Γ has two vertices (genus 2 and genus 4) joined by one edge. Δ_Γ ≅ M_{2,1} × M_{4,1} is of product type, since the two vertices have different genera.
- (b) All ten divisors D_{jk} have the same image ∂V := Φ̄(D_{12}°). All fifteen corner points D_{jk} ∩ D_{lm} map to one point P_*. P_* is a chain Y_A – Y_B – Y_C of three genus-2 curves, joined at two separating nodes. Y_A ≅ Y_C ≅ Y_0 as 1-pointed curves.
- (c) closure(V) \ V = ∂V ⊔ {P_*}, and closure(V) ∩ Δ_Γ = ∂V. Moreover π_1(∂V) = {Y_0} with dim M_{2,1} = 4 > 0, π_2(∂V) is not a point, and dim ∂V = 1.

*Proof.*
- (a) A point of D_{12}° is a bubble A ∋ a_1, a_2, q attached at q to a main component M ∋ a_3, a_4, a_5, q'.
  - Local monodromies on A: 1, 1, and −2 ≡ 3 at q. On M: 1, 1, 1, and 2 at q'.
  - All are prime to 5, so both covers are connected and totally ramified at every branch point. There is a single point over q.
  - By (C3), the cover of A has 2h − 2 = −10 + 3·4 = 2, so h = 2. The cover of M has 2h − 2 = −10 + 4·4 = 6, so h = 4. Check: 2 + 4 = 6.
  - Both components are stable, so nothing is contracted.
  - The A-cover is the fixed cyclic cover of (P^1; 0, 1, ∞) with exponents (1, 1, 3), pointed at the point over ∞. Call it Y_0. The W-cover is the cyclic cover of (P^1; a_3, a_4, a_5, q') with exponents (1, 1, 1, 2), pointed at the point over q'.
  - W is non-constant as q' varies. Its family is the image of the Teichmüller disc T_{0,4} under the isometric pull-back of (C1), with the 4 points as poles. That map is injective on T_{0,4}, and the quotient to moduli space is finite-to-one, so W does not stay constant.
- (b) Φ̄ is S_5-invariant on M_{0,5}, hence by continuity on M̄_{0,5}. S_5 is transitive on the divisors D_{jk} and on the corners. At the corner D_{12} ∩ D_{34} the base is a chain A(a_1, a_2) – B(a_5) – C(a_3, a_4).
  - The monodromies on B are 2 at q_1, 1 at a_5, and 2 at q_2.
  - On C they are 1, 1, 3.
  - All are prime to 5, so every node has one preimage, and every component has genus 2 by (C3).
  - The source is a stable chain of three genus-2 curves. The C-cover has exponents (1, 1, 3) with the node over the exponent-3 point, so it is isomorphic to Y_0 as a pointed curve, just like the A-cover.
- (c) closure(V) \ V = Φ̄(∂M̄_{0,5}) = ∂V ∪ {P_*}. P_* has two nodes, so P_* ∉ Δ_Γ. The rest follows from (a). ∎

**Lemma 2.3 (the only candidate).** Let Δ_G be a stratum such that closure(V) ∩ Δ_G has a 1-dimensional irreducible component E. Then G = Γ, E = ∂V, and closure(E) \ E = {P_*}.

*Proof.*
- By Lemma 2.2(c), closure(V) ∩ ∂M̄_6 = ∂V ⊔ {P_*}. The point P_* gives no 1-dimensional component, so G = Γ, and E is the unique 1-dimensional component of ∂V.
- ∂V is irreducible as the image of D_{12}°.
- closure(∂V) = Φ̄(D̄_{12}) = ∂V ∪ {P_*}. ∎

**Proposition 2.4 (MS5 fails for V).** Let Δ_Γ, i = the genus-2 vertex, and Y_0 be as above. Then V and Δ_Γ satisfy all hypotheses of MS5 except smoothness of V, and the conclusion of MS5 fails.

*Proof.*
- **Hypotheses.** g = 6 ≥ 2. V is closed, 2-dimensional and totally geodesic (Lemma 2.1). Δ_Γ is of product type. ∂V is 1-dimensional and π_1(∂V) = {Y_0}, with dim M_{2,1} > 0 (Lemma 2.2).
- **Candidates.** MS5 needs a product-type Δ_G and P_0 ∈ closure(∂V) with P_0 ∈ closure(E^{(a)}) \ E^{(a)} for some 1-dimensional component E^{(a)} of closure(V) ∩ Δ_G. By Lemma 2.3, the only possibility is G = Γ, E^{(1)} = ∂V and P_0 = P_*.
- **Lifts.** 𝐂^{(1)} is the closure of ξ_Γ^{-1}(∂V) = {Y_0} × π_2(∂V) in M̄_{2,1} × M̄_{4,1}. So every R ∈ 𝐂^{(1)} has R_1 = Y_0. At least one R exists with ξ̄_Γ(R) = P_*: take a limit of lifts of points of ∂V converging to P_*, using compactness.
- **Failure of (a).** Take such an R and u = 1 (= i). R_u = Y_0 is a smooth curve whose only component is isomorphic to Y_0. Condition (a) requires R_u ∈ ∂M̄_{2,1}, which is false.
- So no candidate (G, P_0) satisfies the requirement. ∎

**Remark 2.5 (where the merge is).** At P_* the curve ∂V has two lifted branches, the images of D_{12} and of D_{34}. Along D_{12} the end Y_A stays and B ∪ C is smoothed. Along D_{34} the end Y_C stays and A ∪ B is smoothed.
- So the copy Y_A of Y_0 *is* merged, but along a branch that is itself contained in ∂V ⊂ Δ_Γ. There the constant factor is the twin Y_C ≅ Y_0.
- The corner stabilizer contains (13)(24), which swaps the two branches. So in M̄_6 the two branches even coincide. closure(∂V) ≅ P^1/S_3 has a single branch at P_*.
- MS5 requires the merge to happen in a stratum G ≠ Γ, which never occurs here.

## 3. Smoothness

**Standard facts used (cited from memory).**
- Near X ∈ M_g, with X̃ ∈ T_g a lift, M_g is (T_g, X̃)/Aut(X). For g ≥ 3, Aut(X) acts effectively.
- For a finite subgroup H ⊂ Mod_g, Fix(H) ⊂ T_g is a closed connected complex submanifold. It is biholomorphic to the Teichmüller space of the quotient orbifold, equivariantly for N(H)/H.
- The preimage Ṽ of V in T_6 is the union of the sheets Fix(H′), where H′ runs over the Mod_6-conjugates of the deck group H of the topological cover. Each sheet is biholomorphic to T_{0,5}. Inside a sheet, the curve over a configuration a is Φ(a).

**Lemma 3.1 (V is not smooth).**
- (a) In the coarse sense, V is singular at X_4 : y^5 = x^5 − x.
- (b) In the orbifold sense, V is not smooth at the Fermat quintic X_F : X^5 + Y^5 + Z^5 = 0. Three distinct sheets pass through a lift of X_F and meet there in an isolated point.

*Proof.*
- **(a) The stabilizer of the configuration.** The branch set is {0, ±1, ±i}. Its stabilizer in PGL_2 is C_4 = ⟨x ↦ ix⟩.
  - A finite subgroup containing C_4 is C_{4k}, D_{2k}, or S_4.
  - The 5-point set must be a union of orbits. The orbit sizes are 1, 1, 4k for C_{4k}; 2, 2k, 2k, 4k for D_{2k}; and ≥ 6 for S_4.
  - Only C_4 allows 5 = 1 + 4.
- **(a) All of C_4 lifts.** ix ↦ (ix)^5 − ix = i(x^5 − x), so x ↦ ix lifts to (x, y) ↦ (ix, i^{1/5} y). Hence N(H)/H ≅ C_4, acting on the sheet Fix(H) ≅ T_{0,5} at the configuration.
- **(a) The tangent representation.** Use push-forward of vector fields.
  - On ⊕_j T_{a_j}P^1 the generator has eigenvalues i (at 0) and 1, i, −1, −i (on the 4-cycle).
  - On sl_2 = ⟨∂_x, x∂_x, x^2∂_x⟩ it has eigenvalues i, 1, −i.
  - The quotient T_a M_{0,5} therefore has eigenvalues {i, −1}: the generator acts as diag(i, −1).
- **(a) The quotient germ.** C[u,v]^{C_4} is generated by u^4, v^2, u^2 v, with the single relation (u^2v)^2 = u^4·v^2. So C^2/C_4 is an A_1 singularity, which is normal and not smooth.
- **(a) Comparison with V.** Fix(H)/N(H) → (V, X_4) is finite. It is generically injective: if g ∈ Aut(X_4) maps a point y ∈ Fix(H) with Stab(y) = H into Fix(H), then g^{-1}Hg = H. Suppose V were smooth at X_4. Then the germ is normal and locally irreducible, and a finite bimeromorphic map from a normal germ onto a normal germ is an isomorphism. That would make C^2/C_4 smooth, a contradiction. If several Aut(X_4)-orbits of sheets passed through the lift, the germ of V would be locally reducible, hence again not smooth.
- **(b)** H_Z : Z ↦ ζZ has quotient map [X:Y:Z] ↦ [X:Y]. It is totally ramified over the 5 roots of X^5 + Y^5 = 0, with exponents all 1. So X_F ∈ V, and the same holds for H_X and H_Y. Fix(H_Z) ∩ Fix(H_X) = Fix(⟨H_X, H_Z⟩). The group ⟨H_X, H_Z⟩ is (Z/5)^2, and the quotient by it is P^1 with 3 branch points, so this fixed set is 0-dimensional. Two 2-dimensional submanifolds meeting in an isolated point do not form a submanifold. ∎

So V is not a valid counterexample to MS5 as stated in the task, which requires V_0 to be smooth and closed.

**Lemma 3.2 (the smooth part V°).** Let Σ ⊂ V be the union of two sets:
- Sing(V), the singular locus of the coarse variety;
- the image Σ_orb of the set of points of Ṽ lying on at least two distinct sheets.

Then Σ is a closed analytic subset of V of dimension ≤ 1. V° := V \ Σ is a smooth (coarse and orbifold sense), locally closed, irreducible 2-dimensional subvariety of M_6, and closure(V°) = closure(V) in M̄_6. V° is totally geodesic in the local sense: for X ∈ V° and a complex line L ⊂ T_X V°, a neighbourhood of X in the Teichmüller disc tangent to L lies in V°.

*Proof.*
- Sing(V) is a proper closed subvariety of the irreducible surface V.
- The family of sheets is locally finite in T_6, because Mod_6 acts properly discontinuously. Two distinct sheets are distinct connected 2-dimensional submanifolds, so their intersection is analytic of dimension ≤ 1. The union of these intersections is Mod_6-invariant and locally finite, so its image Σ_orb is closed analytic of dimension ≤ 1.
- So V° is open and dense in V, hence closure(V°) = closure(V).
- Smoothness: away from Σ_orb exactly one sheet passes through each lift, and away from Sing(V) the coarse space is smooth.
- Total geodesy: by (C1) the disc lies in V, and V° is open in V.
- (Algebraicity of Σ_orb: it is the locus of curves in V carrying two distinct order-5 subgroups of the given type. This is a finite union of images of Hurwitz-type spaces, since |Aut| ≤ 84·5. I state this without a detailed proof; it is only needed if "subvariety" must mean algebraic.) ∎

**Proposition 3.3 (MS5 fails for V°).** V° satisfies every hypothesis of MS5 except "closed", and the conclusion of MS5 fails for it.

*Proof.* Everything in the hypotheses and conclusion of MS5, other than "V_0 smooth closed totally geodesic", depends only on closure(V_0) ∩ ∂M̄_g. This covers the strata Δ_G, the components E^{(a)}, the sets 𝐂^{(a)}, the candidates P_0, the conditions (a) and (b), ∂V_0 and Y_0. This set is the same for V° and V (Lemma 3.2). Apply Proposition 2.4. ∎

**Consequence.** The problem text only says "smooth subvariety". If that allows locally closed subvarieties, which is the usual meaning of "subvariety", then V° is an admissible V_0 and MS5 is false as an input to the problem. If V_0 must be closed, MS5 stays open, but any proof of it must use smoothness or closedness of V_0 *at interior points of M_g*. The reason is that its conclusion cannot distinguish V from V°.

## 4. Consequences for the chain

**4.1 Which earlier steps break on this example.**
- **Theorem P (PR-D).** Its hypothesis (T0) is MS5, which fails. So Theorem P does not apply.
- **PR-F, Proposition 4.1, "(T0\*) ⇒ (T0)(a)".** This implication is false as a route to MS5. In the example (T0\*) holds:
  - take P_0 = P_*, with vertex i of G′ = G_* equal to the end Y_A;
  - take E_0 = the D_{34}-branch of ∂V, which lies in Δ_{G″} with G″ = Γ;
  - the edge A–B at Y_A is unpinched along E_0 (merge);
  - the merged vertex v = (A∪B smoothed) is the genus-4 vertex, which carries positive area. It is the pull-back of a finite-area limit on the 4-pointed base component, and π_2(∂V) is the Teichmüller curve of (C1).

  But MS5 quantifies over **every** lift R and every vertex u with a Y_0-component. The lift along the same branch is R = (Y_C, Y_A ∪ Y_B), and its vertex 1 carries the unmerged twin Y_C ≅ Y_0. The step "twins are permuted by Aut(P_∞) and treated symmetrically" (planner's step 5) is exactly what fails. The automorphism swapping Y_A and Y_C swaps the branch merging Y_A with the branch merging Y_C, but along each single branch exactly one copy is merged.
- **Planner's step 3** ("the resulting branch then has the merge property at i"). Here the merge branch is produced, as expected, but it is a branch of ∂V_0 itself (G_b = Γ). The merge property of PR-C holds for it, yet MS5 fails. So step 3 together with steps 4–5 cannot yield MS5 without an extra input excluding twins on merge branches inside Δ_Γ.
- **Lemma V and Proposition C (PR-F).** These are consistent with the example. Vertex i (= Y_0) carries no area, and vertex 2 does.

**4.2 What the example does give for the problem's claim (conditional pinning).** Work in the problem's setting with V_0 = V° (or V), readings (R1) and (R2), and the family V_t. Put P_t := H_t(P_*). Assume:
- **(L2)** K_2 := closure of π_2(∂V_t) in M̄_{4,1} is independent of t.

(L2) is the conclusion of Lemma R\* (PR-E) for the pair (∂V, vertex 2). It holds under (O), given that π_2(∂V) is a Teichmüller curve in the orbifold sense. The latter I verify only in outline: the lift T_{0,4} → T_{4,1} by pull-back is an isometry by (C1). The bookkeeping between ρ and the finite pointwise stabilizer generated by the deck group, which fixes the whole disc, is not written out.

**Proposition 4.2.** Under (R1), (R2) and (L2), the following hold for all small |t|.
- P_t is a chain Z′_t – B_t – Z_t of three genus-2 curves, and P_t = ξ̄_Γ(Y_t, c^t), where c^t lies in the finite set F := K_2 ∩ ∂M̄_{4,1}. In particular Y_t is one end of the chain, say Z′_t ≅ Y_t, and the other end Z_t lies in the finite set F′ of 1-pointed genus-2 components of points of F.
- Consequently, if Z_t ≅ Y_t (as 1-pointed curves) for all small |t|, then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **The stratum of P_t.** By (R2), P_t lies in the stratum Δ_{G_*} of P_*, where G_* is the path with three genus-2 vertices. Also P_t ∈ closure(∂V_t) (PR-B, Lemma B′).
2. **The lift (Y_t, c^t).** Take x_n ∈ ∂V_t with x_n → P_t. Then x_n = ξ_Γ(Y_t, c_n) with c_n ∈ π_2(∂V_t) ⊂ K_2. By compactness, pass to a subsequence with c_n → c^t ∈ K_2. By continuity of ξ̄_Γ, P_t = ξ̄_Γ(Y_t, c^t).
3. **c^t is a boundary point.** P_t has two nodes, so c^t ∈ ∂M̄_{4,1}.
4. **F is finite.** K_2 is a compact irreducible curve that meets M_{4,1}, so F is finite.
5. **The chain.** Matching components, P_t is Y_t glued at one end to the 2-component curve c^t. So the far end Z_t is a component of c^t, and hence lies in F′.
6. **Conclusion under Z_t ≅ Y_t.** Then Y_t ∈ F′ for small |t|. Y_t is continuous in t (PR-A), so it is constant near 0. It is holomorphic on Δ (PR-A), so by the identity theorem it is constant on Δ. ∎

**Why I cannot remove the condition Z_t ≅ Y_t.** At t = 0 it holds (Z_0 = Y_C ≅ Y_0), and Aut(P_*) contains the end-swap σ. In a Kuranishi chart Def(P_*), let the coordinates s_1 and s_2 smooth the two nodes.
- The lifted germ S_0 of closure(V) at P_* is σ-invariant. It has boundary branches in both {s_1 = 0} and {s_2 = 0}.
- For t ≠ 0, let 𝒲′ be the irreducible component of the lifted family through S_0 × {0}. An open-mapping argument shows that 𝒲′_t still has boundary points of both types, near lifts P̂_t and P̂′_t of P_t.
- Along the type-{s_1 = 0} points the A-end is ≅ Y_t, and along the type-{s_2 = 0} points the C-end is ≅ Y_t.
- However, P̂′_t may equal σP̂_t ≠ P̂_t. This is to be expected, because V_t loses the Z/5 automorphisms of V. A degree-conservation argument then forces 𝒲′_t to have degree ≥ |K_0| ≥ 5 over the (s_1, s_2)-plane, where K_0 ⊇ Z/5 is the generic stabilizer of S_0. So 𝒲′_t can split into σ-related sheets.
- In that case both observations concern the same end of P_t, and give no information about Z_t.

So for deformations of V° (if V° is admissible), the problem's claim is **open**. It is equivalent, by Proposition 4.2, to excluding P_t = Y_t – B_t – Z_t with Z_t ≇ Y_t, given that B_t ∪ Z_t is pinned.

## 5. Status

**Proved (modulo the cited standard facts (C1)–(C3) and the local structure of M_g at curves with automorphisms):**
- (P1) MS5 fails for the closed totally geodesic surface V = {y^5 = quintic} ⊂ M_6 (Proposition 2.4). The unique candidate (Γ, P_*) violates (a) for every lift.
- (P2) V is not smooth: it has a coarse A_1 point at y^5 = x^5 − x, and three sheets cross at the Fermat quintic (Lemma 3.1). So V is not a counterexample to MS5 as stated, which requires V_0 smooth and closed.
- (P3) The smooth locus V° (Lemma 3.2) is a smooth, locally closed, locally totally geodesic surface with the same boundary, and MS5 fails for it (Proposition 3.3). Under the reading "smooth subvariety = smooth locally closed subvariety" of the problem text, MS5 is therefore false as stated, and the chain through Theorem P cannot work for all admissible V_0.
- (P4) PR-F Proposition 4.1 does not yield MS5: (T0\*) holds in the example while MS5 fails. The planner's mechanism fails at the "twins" step (Section 4.1).
- (P5) A conditional pinning for the example (Proposition 4.2).

**Not proved / open:**
- (Q1) MS5 for **closed** smooth totally geodesic V_0. No counterexample with all hypotheses verified is given. Any proof must use interior smoothness or closedness, since the conclusion sees only closure(V_0) ∩ ∂M̄_g.
- (Q2) The problem's claim for deformations of V° (or of any V_0 whose cusps carry unmerged twins of Y_0). By Proposition 4.2 this reduces to whether the far end Z_t of P_t stays isomorphic to Y_t.
- (Q3) Whether the problem intends V_0 to be closed. This decides whether V° is admissible.
- (Q4) A corrected hypothesis replacing (T0) that tolerates twins, for example one asserting that every unmerged Y_0-component at P_0 stays isomorphic to Y_t at P_t. I have no proof of any such statement.
- (Q5) The orbifold bookkeeping making π_2(∂V) a Teichmüller curve "in the orbifold sense" with a genuine homomorphism ρ into Mod_{4,1}. The deck group fixes the disc pointwise, so ρ is a priori defined only modulo it. This is only sketched.

=== END OF ANSWER round6_q2 ===

