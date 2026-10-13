# Round 4, q7: continuing the incidence route for MS4

**Bottom line.** I do not have a complete proof of MS4. Below are:
- (A) a correction to the prior results;
- (B) a rigorous reduction of the incidence step to a transport statement. Under (R2), Lemma B no longer needs hypothesis (ii);
- (C) a local lemma that settles part of (H1), plus an exact description of the configurations it leaves open;
- (D) a replacement for (H2)/(H3) that needs no condition on zeros and handles multiplicity > 1. The part from maximal Higgs to Kobayashi isometry is proved here; it then relies on two results cited from memory;
- (E) the resulting conditional theorem, with a short list of remaining hypotheses;
- (F) a second pinning mechanism, by intersecting two rigid curves;
- (G) what remains open.

Throughout I use readings (R1) and (R2) from the query. I also use the following.
- By Lemma 1 of P-a (re-checked, fine), t ↦ Y_t is holomorphic. So it suffices to prove that Y_t is constant for t near 0 (identity theorem). This is used freely below.
- I work in local manifold charts of the orbifold M̄_g, which are finite covers. Plumbing coordinates s_ε for the edges ε of a dual graph cut out the strata locally.

---

## A. Correction to the prior results

The task's prior results say, in the paragraph after Proposition A of the spliced partial result: "0-dimensional strata of closure(V_t) are finite and continuous in t, hence constant." This is **false** as stated.
- A 0-dimensional piece closure(V_t) ∩ Δ_G is a finite set that moves continuously in t.
- It is constant only if it lies in a fixed finite set independent of t. That happens, for example, when Δ_G is itself a point (all vertices of type (0,3)), or when the points lie in closure(E_0) for a curve E_0 that does not move, as in Lemma B.

So the "induction on codimension terminating at 0-dimensional strata" does not close by itself. Lemma B is unaffected.

## B. Under (R2), incidences are transported automatically

**Lemma B′.** Let H : closure(V_0) × Δ → closure(𝒱) be the stratified homeomorphism of (R2). Let E_0 be a 1-dimensional piece of closure(V_0) ∩ Δ_{G''}, and let P_0 ∈ closure(E_0) ∩ closure(∂V_0) ∩ Δ_{G'}. Put E_t := H(E_0 × {t}) and P_t := H(P_0, t). Then:
- E_t ⊂ Δ_{G''};
- P_t ∈ closure(E_t) ∩ closure(∂V_t) ∩ Δ_{G'};
- t ↦ P_t is continuous.

*Proof.*
1. H is a homeomorphism over Δ that maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every G.
2. A homeomorphism commutes with closures. Hence H(closure(E_0) × {t}) = closure(E_t), and H(closure(∂V_0) × {t}) = closure(∂V_t).
3. Continuity of P_t follows from continuity of H. ∎

So neither hypothesis (ii) nor the "isolated point" condition in (H1) is needed under (R2). Under a weaker reading one would fall back on (ii) as in P-d. By P-b, the component of P_t at the vertex i of G' is Y_t: the vertex i stays intact because π_i is constant along ∂V_t.

## C. Local structure at a cusp of ∂V_t (partial (H1))

Fix t and a point P ∈ closure(∂V_t) \ ∂V_t. Then P lies in some Δ_{G'}, where G' degenerates Γ: it has edge set E(Γ) ∪ X with X ≠ ∅, and vertex i is intact. Let S be the germ of closure(V_t) at P. It is pure 2-dimensional, because V_t is dense in it.

**Lemma C1.** S has a 1-dimensional boundary branch b through P, other than the branches of closure(∂V_t), such that some edge e ∈ X is pinched along b.

*Proof.*
1. closure(∂V_t) \ ∂V_t is a proper analytic subset of a 1-dimensional analytic set, hence discrete.
2. So a branch β of closure(∂V_t) at P satisfies β \ {P} ⊂ Δ_Γ. Let X_S be an irreducible component of S containing β.
3. Take e ∈ X. On β \ {P} exactly the edges of Γ are pinched, so s_e ≠ 0 there. Hence s_e|_{X_S} is a non-unit that is not identically zero on the irreducible 2-dimensional germ X_S.
4. Its zero set is therefore of pure dimension 1 (Krull's principal ideal theorem / Weierstrass preparation; standard).
5. That zero set meets β only at P. So it contains a branch b ≠ β, and b lies in the boundary with s_e ≡ 0 on b. ∎

**Definition (merge property).** Let b be a boundary branch at P, and let G_b be the dual graph of a generic point of b. Equivalently, G_b is G' with the edges unpinched along b contracted. Let v be the vertex of G_b containing vertex i of G'. Say b has the *merge property* if v is strictly bigger than {i}, that is, some edge of G' incident to i is unpinched along b.

**Lemma C2 (merging forces variation).** Suppose b has the merge property. Let E be the 1-dimensional piece of closure(V_t) ∩ Δ_{G_b} containing b. Then π_v(E) is not a point. Moreover, the limit Q of π_v along b at P is a boundary point of M̄_{h,m}, where M_{h,m} is the factor of vertex v. The dual graph of Q is the subgraph of G' contracted into v, and its component at vertex i is Y_t.

*Proof.*
1. As a point of b tends to P, the edges of G' inside v get pinched. So π_v tends to the stable curve Q described in the statement. Q lies in ∂M̄_{h,m}, because v contains at least one such edge.
2. Its component at vertex i is the component of P at vertex i, which is Y_t.
3. If π_v were constant on E, equal to some Z ∈ M_{h,m}, then its limit along b would be Z ∈ M_{h,m}, not a boundary point. Contradiction. ∎

**What C1 does not give.** C1 produces a branch b on which an extra edge e is pinched. It does not control the edges at vertex i. The merge property fails exactly when every edge of G' incident to i is pinched along b. Lemma C1 cannot exclude this. Example: in local coordinates (u,v) on a smooth germ, s_γ = uv and s_e = v, with β = {u=0} and b = {v=0} ⊂ Δ_{G'}. Nothing in (i), (ii), (R1) or (R2) rules out a surface whose boundary branches all look like this at every cusp of ∂V_0; compare Observation 4 of P-a. Define:

**(C-merge)** There is a cusp P_0 of ∂V_0 and a boundary branch b of closure(V_0) at P_0 with the merge property.

(C-merge) is the precise residue of (H1). It is not proved in general.

## D. Rigidity of the varying factor without Möller's zero condition

**Möller's characterization, as I recall it** (from memory, Möller, *Variations of Hodge structures of a Teichmüller curve*, JAMS 19 (2006); flagged as uncertain):
- A curve C → M_g is a Teichmüller curve (generated by an abelian differential) **iff** the VHS of the family contains a rank-2 sub-VHS L with maximal Higgs field, **and** the zeros of a generating section ω of L^{1,0} are horizontal: after a finite base change they form sections.
- I believe the second condition is genuinely needed. Shimura-type families with a maximal-Higgs rank-2 piece are not Teichmüller curves; compare Möller's paper on Shimura- and Teichmüller curves (J. Mod. Dyn. 2011), from memory.
- I see no reason why topological transport would preserve that zero condition. So step 5 of Proposition A, as written, is unjustified. I bypass it as follows.

**Setting.**
- F_t := π_v(E_t) ⊂ M_{h,m}, where E_t = H(E_0 × {t}), so that E_t ⊂ Δ_{G_b} for all t.
- Pass to a finite level cover, so that the universal family of genus-h curves exists over F_t (normalized), with local system R^1_t of rank 2h.
- By (R2), the classifying maps are homotopic. So there is an orientation-preserving homeomorphism of punctured curves h_t : F_0 → F_t with R^1_t ∘ h_t ≅ R^1_0 as local systems.

**(H2′)** R^1_0 contains a real rank-2 sub-VHS L_0 whose Higgs field is maximal. Equivalently (Arakelov equality), its period map F̃_0 → ℍ is a biholomorphism.

This holds if F_0 is a Teichmüller curve generated by an abelian differential (Möller, cited from memory). It does **not** hold for curves in M_{0,m}, where h = 0, nor in general for Teichmüller curves generated by quadratic differentials.

**Proposition D.** Under (R2) and (H2′), F_t = F_0 for all t, as subsets of M_{h,m}. This uses two cited results, (K) and (Ct) below.

*Proof.*

*Step 1 (the monodromy of L is Fuchsian).*
- Maximal Higgs at t = 0 means the ρ_0-equivariant period map φ_0 : F̃_0 → ℍ is a biholomorphism.
- So the monodromy ρ_0 of L_0 is a discrete faithful representation onto a lattice Λ ⊂ SL_2(ℝ) (up to ±1), and in particular Zariski dense. Then L_0 is absolutely irreducible.
- Let L_t ⊂ R^1_t be the transported sub-local system, with ρ_t = ρ_0 ∘ (h_t)_*^{-1}.

*Step 2 (L_t is a sub-VHS, including multiplicity > 1).*
- By Deligne's semisimplicity and the isotypic decomposition of a polarizable VHS (cited from memory: Deligne, *Un théorème de finitude pour la monodromie*, §1), the ρ_t-isotypic component of R^1_t ⊗ ℂ is L_t ⊗ W_t.
- Here L_t carries a VHS that is unique up to shift of the Hodge types, and W_t is a Hodge structure.
- ρ_t has non-compact Zariski closure. So L_t is not unitary, and its two Hodge types are adjacent, say {q, q−1}.
- If W_t had two types s < s′, the tensor product would have at least three distinct types among q−1+s, q+s, q−1+s′, q+s′. A weight-1 VHS has only the types 1 and 0. Hence W_t is pure, of one type.
- So for any real w ≠ 0 in W_t, the rank-2 local system L_t ⊗ w ≅ L_t is a real sub-VHS of R^1_t of types (1,0)+(0,1).
- This settles the multiplicity worry (H2) of the earlier answer.

*Step 3 (maximality transports).*
- For a rank-2 real VHS on a punctured curve with quasi-unipotent local monodromy, 2·deg L^{1,0} of the Deligne extension equals the Toledo invariant T(ρ) (up to a fixed normalization). This is cited from memory, e.g. from the theory of maximal representations of Burger–Iozzi–Wienhard and Koziarz–Maubon.
- The Toledo invariant is natural under orientation-preserving homeomorphisms, so T(ρ_t) = T(ρ_0) = |χ(F_0)| = |χ(F_t)|.
- Hence L_t is maximal Higgs. Equivalently, its period map φ_t : F̃_t → ℍ is a local isometry of complete hyperbolic disks, hence an isometry. (Pointwise Schwarz–Pick inequality plus equality of total integrals forces pointwise equality.)

*Step 4 (Kobayashi isometry; proved here).*
- On F̃_t the local system is trivial. So L := L_t is a fixed real symplectic plane in V = H^1(S_h, ℝ), and V = L ⊕ L^⊥ (symplectic orthogonal).
- Choose a symplectic basis adapted to this splitting. The map Ξ : ℍ_h → ℍ, τ ↦ τ_{11} (the upper-left entry, i.e. the L-block) is holomorphic. Its imaginary part is positive, as a principal minor of Im τ > 0.
- At points where L is a sub-Hodge structure, τ is block diagonal, so Ξ(τ) is the period of L.
- Hence φ_t = Ξ ∘ Per ∘ f_t, where f_t : F̃_t → T_{h,m} is the lift of the classifying map, and Per : T_{h,m} → T_h → ℍ_h is the period map after forgetting the marked points.
- All maps are holomorphic and do not increase Kobayashi distances. By Royden's theorem (cited), k_{T_{h,m}} = d_T. Therefore
  k_ℍ(φ_t x, φ_t y) ≤ k_{ℍ_h} ≤ d_T(f_t x, f_t y) ≤ k_{F̃_t}(x,y) = k_ℍ(φ_t x, φ_t y).
- So f_t is a holomorphic Kobayashi-isometric embedding of the disk into T_{h,m}.

*Step 5 (cited).*
- **(K)** A holomorphic isometric disk in T_{h,m} for the Teichmüller metric is a Teichmüller disk. Cited from memory, in the form I believe McMullen proves it in *Rigidity of Teichmüller curves* (Math. Res. Lett. 2009); not checked.
- Hence F_t is a Teichmüller curve, possibly generated by a quadratic differential.
- **(Ct)** Teichmüller curves in M_{h,m} form a countable set. Cited from memory: they are defined over ℚ̄ / rigid (Möller, McMullen), or alternatively by Eskin–Mirzakhani–Mohammadi.

*Step 6 (constancy).*
- t ↦ closure(F_t) is continuous in the Hausdorff metric on compact subsets of M̄_{h,m}, by (R2).
- A connected subset of a countable metric space is a point: the distance to a fixed point takes countably many values on a connected set, hence is constant.
- So closure(F_t) is constant, and F_t = F_0. ∎

## E. Conditional theorem

**Theorem E.** Assume (R1) and (R2). Assume also:
- (C-merge) holds, with merged vertex v carrying the factor M_{h,m};
- (H2′) holds for F_0 = π_v(E_0);
- the cited results (K) and (Ct) hold.

Then π_i(∂V_t) = {Y_0} for all t.

*Proof.*
1. Take E_t and P_t as in Lemma B′.
2. By Lemma C2, F_t = π_v(E_t) is a curve, and its limit Q_t at P_t lies in closure(F_t) ∩ ∂M̄_{h,m}. Its component at vertex i is Y_t.
3. By Proposition D, closure(F_t) = closure(F_0). This is a compact curve, so its intersection with ∂M̄_{h,m} is a finite set.
4. Q_t depends continuously on t, through P_t. So Q_t is constant.
5. Its component at vertex i is determined up to the finite ambiguity of graph automorphisms, and depends continuously on t. Hence Y_t is constant. ∎

This replaces the earlier conditional theorem: (H3) is removed and (H2) is weakened to (H2′), at the price of the cited results (K) and (Ct).

## F. Second pinning mechanism (when the merge property fails)

Suppose that at cusps of ∂V_0 there are boundary branches b without the merge property. Then vertex i is a vertex of G_b. Let E_0 ⊃ b be the corresponding boundary piece. Then π_i(E_0) is either the point Y_0, or a curve through Y_0.

**Lemma F.** Suppose there are two such pieces E_0, E′_0, with E_t, E′_t transported as in Lemma B′, such that:
- F_t := π_i(E_t) and F′_t := π_i(E′_t) are curves;
- (H2′) holds for both;
- closure(F_0) and closure(F′_0) have no common irreducible component through Y_0.

Then Y_t is constant.

*Proof.*
1. By Proposition D, F_t = F_0 and F′_t = F′_0.
2. Y_t is the limit of π_i along E_t at P_t, so Y_t ∈ closure(F_0) ∩ M_{g_i,n_i}. Likewise Y_t ∈ closure(F′_0). For E′_t, P′_t is its own transported cusp, and the component of P′_t at vertex i is again Y_t.
3. Y_t therefore lies in the finite set closure(F_0) ∩ closure(F′_0) near Y_0. It is continuous in t, hence constant. ∎

If π_i(E_0) = {Y_0}, then E_0 is another boundary piece that is constant on factor i, and the problem recurs for E_0. Such recursions cannot be ruled out by the local data.

## G. Status, and what remains open

**Proved (given (R1) and (R2)):**
- the correction in A;
- Lemma B′;
- Lemmas C1 and C2;
- Steps 1, 2 and 4 of Proposition D, using only Deligne's decomposition and Royden's theorem, both cited;
- Theorem E and Lemma F, as implications.

**Cited from memory, not verified:**
- Deligne's isotypic decomposition of a VHS;
- Toledo invariant = 2 deg L^{1,0} for rank-2 VHS on punctured curves;
- (K): holomorphic isometric disks are Teichmüller disks (attributed to McMullen);
- (Ct): Teichmüller curves in M_{h,m} are countable;
- the exact form of Möller's characterization. I believe it includes a condition on the zeros of ω, which is why I avoided it.

**Open:**
1. **(C-merge).** Does a cusp of ∂V_0 always carry a boundary branch of closure(V_0) on which an edge at vertex i is unpinched? Section C shows this cannot follow from local analysis. It would need the global structure of totally geodesic surfaces: Wright's correspondence with rank-2 orbit closures, and the description of the boundary by Chen–Wright and multi-scale differentials. I could not derive it.
2. **(H2′) for F_0.** One needs F_0 = π_v(E_0) to be a Teichmüller curve generated by an **abelian** differential in M_{h,m} with h ≥ 1. This is not proved; it is expected only heuristically from orbit-closure boundary theory.
   - When v has genus 0, or F_0 is generated by a genuinely quadratic differential, (H2′) fails for the family's own H^1.
   - The double-cover local system is not obviously transported, because the odd zeros are not marked points of M_{h,m}.
   - A different rigidity argument would be needed there.
3. **The recursive case.** It is open how to handle boundary pieces that are again constant on factor i (end of F).
4. **The statement itself.** The claim as posed (MS4) remains **unproved**. I also have no counterexample.
   - Hypotheses (i) and (ii) constrain only the boundary incidence pattern.
   - Any proof must use global rigidity of V_0. For example, if V_0 had no deformations as a closed surface in M̄_g, the claim would be vacuous; whether it has none is itself open.

=== END OF ANSWER round4_q7 ===
