kind: verify

Task: you are a hostile, meticulous referee. Below is the complete current draft proof document for the problem (stated after this query). Check its argument **step by step**: for every inequality, every interchange (of limits, of quotient and closure, of lift and transport, of "for all t" and "for small t"), every cited classical result (is it true, is it stated with the right hypotheses and scope, is it applied within that scope?), and every "it follows that" / "hence" / "so", decide whether it actually follows **as written**. Pay particular attention to:
1. Whether the document's main claims are correctly labelled: it does NOT claim the problem's statement in general; it claims (a) Theorem A: the claim under (R1)+(R2^orb), equivalently (Theorem 7.5) under (R1)+(R2)+(AP); (b) Corollary C.5 / Theorem C.7 (unconditional under (R1)+(R2) when boundary automorphisms satisfy a local criterion); (c) Theorem B (claim under (R1)+(R2)+(Rig)+(NRT_P)); (d) Section U results. Check each of these is actually proved, modulo the explicitly listed cited facts.
2. Whether the readings (R1), (R2), (R2^orb) are honest formalisations of the problem's hypotheses (i), (ii) and "smoothly trivial family", and whether the document is transparent about which reading each result uses.
3. Part II §7 (Theorem 7.5, path lifting at constant isotropy order) and Section C (C.5, C.7, C.8, C.10): these are the newest parts.
4. The Bridge section (Lemmas L.1–L.3), Part I §I.5 (walk chain) and Part III in their present consolidated form: these have not been independently refereed.
5. Every place where a fact is used outside the scope in which it was established (e.g. product-type vs non-product strata, coarse vs orbifold statements, fixed vs varying pants decompositions, t = 0 vs t ≠ 0).

Output format: (i) a list of every error or gap found, **in order of severity** (fatal / serious-but-repairable / minor), each with its exact location (section, lemma, step), what is wrong, and a repair if you see one; (ii) a short verdict per main result (Theorem A, Theorem 7.5, C.5, C.7/C.8, C.10, Theorem B, Section U); (iii) an explicit sentence saying whether **the problem's main claim (as posed)** is proved by this document — and, separately, whether each conditional theorem is proved under its stated hypotheses. Be concrete; do not summarise the document back.

=== DRAFT PROOF (verbatim) ===

# Constant boundary factors of deformations of totally geodesic surfaces: what is proved, what is reduced, what is open

## 0. Status (read this first)

**The claim as posed is not proved in this document, and no counterexample is known.** What the document establishes:

1. **Theorem A (Part II; a complete proof, modulo cited classical facts).** *The claim holds for every family satisfying the problem's hypotheses (with V_0 closed in M_g), provided "smoothly trivial family" together with (i), (ii) is read in the embedded-orbifold sense (R2^orb).* (R2^orb) asks that, on every boundary stratum, the trivialisation lifts to a mapping-class-equivariant, isotropy-preserving map of Teichmüller spaces. By Theorem LG (Part II §7) it is equivalent to its chart-level local version (Loc).
   - **New in this revision (Theorem 7.5, Part II §7).** Given the coarse trivialisation (R2), (R2^orb) is *equivalent* to the single condition **(AP)**: |Aut(H_t(z))| = |Aut(z)| for every boundary point z ∈ B_0 and every t. That is, the trivialisation never changes the order of the automorphism group of a boundary curve. The proof is a path-lifting argument at constant isotropy order. So Theorem A reads: **the claim holds under (R1) + (R2) + (AP)**, and (AP) is only needed for |t| < r, for some r > 0.
   - **Unconditional consequences under the coarse reading (Corollary C.5, Theorem C.7).** If no point of closure(V_0) ∖ V_0 has a non-trivial automorphism, then (AP) holds for small |t| automatically, and the claim holds under (R1) + (R2) alone (modulo the cited classical facts behind Theorem A). More generally (Theorem C.7) the same holds whenever, at every boundary point z, |Aut| is constant near z on each local stratum branch through z that meets B_0 — e.g. when the only automorphisms are elliptic involutions of generic elliptic tails (Remark C.9(d)). By Theorem C.8 any failure of (AP) near t = 0 is located next to the closed set F of points where this local criterion fails.
   - The two inputs that earlier versions flagged as citations of uncheckable scope are now proved in this document:
     - Proposition Ψ (Part I §I.6A): the subsurface restriction map on augmented Teichmüller space, including convergence at vertex subsurfaces uniformly in the auxiliary pants decomposition (formerly GAP 1);
     - Lemma F1 (Part II §10): finiteness of non-constant holomorphic maps from a finite-type Riemann surface into the level covers M_{h,m}[N], h ≥ 1 (formerly GAP G1); genus 0 is Lemma F0.
   - These proofs, like the rest, rely on classical theorems cited from memory with precise statements (§§I.7, II.10, III.7). The heaviest new ones are Thurston's stretch-map rigidity (Th), properness of filling length functions (Prop), the closed-fibre Imayoshi–Shiga finiteness theorem (IS_c) and the branched-cover embedding of Teichmüller spaces (BC).
2. **Theorem B (Part III; the coarse reading).** Under the coarse reading (R1) + (R2), the claim holds provided two statements hold:
   - (Rig), finiteness of the moving image curves of boundary pieces;
   - (NRT_P), "no rigid twin at puncture points".

   Given (Rig), (NRT_P) is *equivalent* to the claim.
3. **Unconditional corollaries of Theorem B (Section C).** Under (R1), (R2) and (Rig), the claim holds whenever no automorphism of a "puncture point" of the boundary moves a component isomorphic to Y_0 to another component. This covers three cases:
   - 2g_i − 2 + n_i > g − 1;
   - every puncture point lies in a product-type stratum;
   - the isotropy groups of the transported puncture points do not drop.
4. **Unconditional results (Section U).**
   - t ↦ Y_t is holomorphic, which gives several equivalent forms of the claim.
   - The claim holds in genus 2.
   - The claim holds if uncountably many V_t are totally geodesic.
   - The claim holds if the V_t have countably many complex-structure classes (on a level cover).
   - The claim holds if closure(V_0) is isolated in the Douady space.
5. **Open (Section G).** The claim under the coarse reading when (AP) fails on every disc around t = 0, i.e. when the trivialisation changes the automorphism order of some boundary point arbitrarily close to t = 0. Equivalently, granting (Rig): (NRT_P). Also (Rig) itself.

**How the parts were produced and checked.**
- Parts I–III consolidate proofs whose components were each checked earlier by an independent reader.
- The consolidated texts, the new streamlined assembly in Part II (§§5, 6, 9: one Aut-fixed lift, then a chain of equalities), and the Bridge section have been checked only by the author of this document. That check included numerical verification of two explicit formulas in Part I.
- **Independent referee reports (latest revision).** Two independent hostile referees checked (1) Theorem 7.5 (with Lemmas 7.1, 2.5, Prop. 5.1), Corollary C.5, Lemmas F0/F1 and Proposition Ψ with Lemma S, and (2) all of Part II §§2–7, §9 and the §10 citations (Theorem A given the Part I inputs I.2, I.3, I.5, I.6). Verdict: **no fatal error; all correct after minor repairs**, which are incorporated: two wording repairs in Theorem 7.5 (translates of local sections through arbitrary base points; slices from a Lebesgue cover are slices for every point of the K-fixed path), a rigorous geodesic-homotopy proof of the marking identification in Lemma S, the ordering of the torsion-freeness argument in Lemma F1, an open-versus-closed disc slip in Setting 6.0, closedness of V_t in M_g (§II.1.2), and citation qualifiers ((Th) for cusped surfaces, (Sel), Kerckhoff's formula). The Bridge, Part I (other than Prop. Ψ) and Part III in consolidated form, and the new Theorems C.7, C.8 and Proposition C.10 (proved by a separate worker, checked by the author), have not been independently refereed in their present form.
- **Revision note (latest audit).** A hostile re-reading of the whole document found one faulty step: Lemma L.2, Step 4(b), had used a dimension-theoretic inequality in the wrong direction (closed finite-to-one maps can raise covering dimension). That step is now repaired by a Remmert argument. The same audit narrowed GAP G1 by proving the genus-0 case of the finiteness theorem (Lemma F0). A further revision then (i) proved the remaining case (Lemma F1), (ii) proved (Ψ) as Proposition Ψ, and (iii) found and repaired a second, subtler flaw: Lemma TI(3)–(4), Step 4 (§I.5.8) and Lemma L.1 Step 2 had applied (Ψ) with a fixed pants decomposition after transporting by mapping classes that vary along the sequence (which moves the pants decomposition). Proposition Ψ(c), (d) are stated and proved uniformly in the pants decomposition, and those steps now invoke them explicitly. **Latest revision (refine 3).** (i) New Theorem 7.5 (Part II §7): under (R2), the orbifold reading (R2^orb) is equivalent to (AP), preservation of automorphism orders of boundary points; this turns Theorem A into "(R1)+(R2)+(AP) ⇒ claim" and yields the unconditional Corollary C.5. (ii) Lemma F1, Steps 2c–2d: the old text treated "lifts of mapping classes" as a group mapping to PMod with kernel G, which tacitly assumed the Birman–Hilden property; it now works with pairs (ϑ, lift), which needs no such property, and torsion-freeness of Γ_1 is now argued directly (Nielsen realisation + Serre's lemma). Theorem 7.5, Corollary C.5 and the repaired F1 were subsequently checked by independent referees (see the item above). **Final pass of refine 3:** referee repairs incorporated; new Theorems C.7, C.8, Proposition C.10 and Remarks C.9, C.11 (Section C). All explicit formulas the document relies on (Lemma B, the collar Beltrami coefficient of Lemma PA, Lemma M on random instances, the Riemann–Hurwitz bound of Lemma F0) were re-checked numerically or by hand.

**Organisation and conventions.**
- §1: setting and the readings of the hypotheses.
- Section U: unconditional results.
- Part I: geometry of closure(V_0) at t = 0 (statements about V_0 alone).
- Bridge: Lemmas L.1–L.3, which put Part I and Appendix A of Part II into the exact forms used by Parts II and III.
- Part II: Theorem A, with Appendix A (coarse-valid lemmas).
- Part III: Theorem B.
- Section C: corollaries. Section R: other routes. Section G: gaps.
- **Numbering.** Inside Part I, II or III, a bare reference such as "Lemma 2.3", "§5.7" or "Step 4" refers to that Part's own numbering; the section headings carry a prefix (I., II., III.) for orientation. References across Parts are written explicitly, e.g. "Part I Lemma TI". Results of Section U are numbered U.1–U.8, those of the Bridge L.1–L.3, and those of Section C C.1–C.11.
- Each Part restates the conventions it needs. Where Parts use slightly different letters for the same object (for example 𝓦_G and 𝒲_G for the lifted boundary families), the definitions agree.

---

## 1. Setting and readings

- **Spaces.**
  - M̄_g is the coarse Deligne–Mumford space, a normal projective variety.
  - Δ_G is the stratum of stable curves with dual graph G.
  - ξ_G : ∏_{w∈V(G)} M_w → Δ_G is the finite gluing map, with M_w = M_{g_w,n_w} and the special points labelled by the half-edges at w.
  - Δ_G is *of product type* if ξ_G is injective. By hypothesis Δ_Γ is of product type, and Δ_Γ ≅ ∏_j M_{g_j,n_j}.
- **V_0 and the family.** V_0 ⊂ M_g is smooth, 2-dimensional and totally geodesic. We read "subvariety" as closed and irreducible, so V_0 is closed in M_g and connected. 𝒱 ⊂ M_g × Δ is the total space of the family, and V_t its fibres.
- **Closures and boundaries.** All closures are taken in M̄_g or M̄_g × Δ. B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g, and ∂V_t := closure(V_t) ∩ Δ_Γ.
- **Classes.** 𝔐 := M_{g_i,n_i}/S_{n_i} (marked points unordered), and [Z] ∈ 𝔐 denotes the class of an n_i-pointed curve Z of type (g_i,n_i).
- **The hypothesis.** dim ∂V_t = 1 and π_i(∂V_t) = {Y_t}. If dim M_{g_i,n_i} = 0 there is nothing to prove, so we assume dim M_{g_i,n_i} ≥ 1 throughout.
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- **(R2)** (the coarse reading). There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ, written H(z,t) = (H_t(z), t), such that:
  - H is smooth on V_0 × Δ;
  - H_0 = id;
  - for every stratum G, including the open stratum M_g, H maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ).

  (R2) encodes "smoothly trivial" together with (i) and (ii) as one stratum-preserving trivialisation. This is a reading: literally, (i) and (ii) give trivialisations stratum by stratum together with the compatibility (ii). Under (R2), H_t need not preserve automorphism groups of boundary points.
- **(R2^orb)** (the embedded orbifold reading) strengthens (R2). It is defined in Part II §1.3 and used only for Theorem A.
- **(AP)** (automorphism orders preserved): |Aut(H_t(z))| = |Aut(z)| for all z ∈ B_0 and all t ∈ Δ. By Part II Theorem 7.5, (R2) + (AP) ⇔ (R2^orb).
- **Algebraicity.** By (R1) and Chow's theorem, closure(V_t) is a projective algebraic subset of M̄_g.

---

## U. Unconditional results

### Proposition U.1 (holomorphy of Y)
Under (R1) and (R2), t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}.

*Proof.*
1. **Continuity.** Fix p ∈ ∂V_0. By (R2), H(p,t) ∈ ∂V_t, so Y_t = π_i(H(p,t)), which is continuous in t.
2. **The analytic set A.** A := closure(𝒱) ∩ (Δ_Γ × Δ) is a closed analytic subset of the analytic space Δ_Γ × Δ, by (R1). By (R2) it is homeomorphic to ∂V_0 × Δ. Let A′ be the union of the 2-dimensional irreducible components of A. Since the 1-dimensional part of ∂V_0 is non-empty, A′_t ≠ ∅ for every t.
3. **The bad set.** No component of A′ lies in a fibre of φ := pr_Δ, because fibres have dimension ≤ 1. Let 𝔅 be the union of Sing(A′) and of the critical set of φ on Reg(A′). 𝔅 is analytic of dimension ≤ 1. Its 1-dimensional components lying in fibres of φ form a locally finite family, so they lie over a discrete set D ⊂ Δ.
4. **Local sections.** For t_0 ∉ D the fibre A′_{t_0} has dimension 1 and is not contained in 𝔅. Pick a ∈ A′_{t_0} ∖ 𝔅. Near a, A′ is a manifold and φ a submersion, so there is a local holomorphic section σ with σ(t_0) = a. Then Y_t = π_i(σ(t)) is holomorphic near t_0, because Δ_Γ ≅ ∏_j M_{g_j,n_j} and π_i is holomorphic.
5. **Extension.** Y is continuous on Δ and holomorphic off the discrete set D. Near Y_{t_0}, the normal analytic space M_{g_i,n_i} embeds locally in some ℂ^N. The coordinate functions of Y are continuous and holomorphic off D, so by Riemann's removable singularity theorem they are holomorphic. ∎

### Corollary U.2 (reformulations)
Under (R1) and (R2), the following are equivalent:
- (a) Y_t = Y_0 for all t ∈ Δ (the claim);
- (b) {t : Y_t = Y_0} has an accumulation point in Δ;
- (c) for some uncountable S ⊂ Δ, the set {Y_t : t ∈ S} is countable;
- (e) [Y_t] ∈ 𝔐 lies in a finite set for all t in a non-empty open subset of Δ.

Moreover (d) implies (a), where
- (d) ∂V_t ∩ ∂V_0 ≠ ∅ for all t in a set with an accumulation point in Δ.

(The converse of (d) is not claimed: with Y_t ≡ Y_0, the curves ∂V_t = {Y_0} × C_t may still be disjoint from ∂V_0.)

*Proof.*
- (a) ⇒ (b), (c), (e) is clear.
- (b) ⇒ (a). Y^{-1}(Y_0) is an analytic subset of the connected disc Δ with an accumulation point, hence all of Δ.
- (c) ⇒ (b). Some value y is taken on an uncountable set S_y. Some compact subdisc contains infinitely many points of S_y, so S_y accumulates in Δ. As above, Y ≡ y, and y = Y_0.
- (d) ⇒ (b). Every point of ∂V_t has i-th coordinate Y_t, so a common point of ∂V_t and ∂V_0 forces Y_t = Y_0.
- (e) ⇒ (a). Let U be a connected open set on which [Y_t] takes values in a finite set. t ↦ [Y_t] is continuous, so it is constant on U, say equal to [y]. Then Y_t lies in the finite fibre of M_{g_i,n_i} → 𝔐 over [y] for t ∈ U, and by continuity Y is constant on U. Now (b) applies. ∎

### Theorem U.3 (genus 2)
For g = 2 the claim holds: either factor i is 0-dimensional (and the claim is trivial), or no stratum Δ_Γ as in the problem exists.

*Proof.*
- For a stable graph, Σ_w (2g_w − 2 + n_w) = 2g − 2 = 2, and each term is ≥ 1 by stability.
- A vertex of positive dimension (3g_w − 3 + n_w ≥ 1) has 2g_w − 2 + n_w ≥ 1, with equality only for (g_w,n_w) = (1,1). The only other type with value 1 is (0,3), of dimension 0.
- Suppose dim M_{g_i,n_i} ≥ 1. Since ∂V_t is 1-dimensional and π_i(∂V_t) is a point, some other factor also has positive dimension. Two vertices of positive dimension have values summing to at most 2, so both are of type (1,1) and there are no further vertices.
- The graph is two (1,1)-vertices joined by one edge. Its stratum is Δ_1 ≅ (M_{1,1} × M_{1,1})/S_2, where the swap acts non-trivially. This is a stratum that needs a finite quotient, which the problem excludes. ∎

### Lemma U.4 (twin points are small)
Let Q be a stable curve of genus g with two distinct components, each isomorphic to an n_i-pointed curve of type (g_i,n_i). Then 2(2g_i − 2 + n_i) ≤ 2g − 2.

*Proof.* Σ_w (2g_w − 2 + n_w) = 2g − 2 over the components of Q, with n_w counting the special points, and every term is ≥ 1. ∎

### Theorem U.5 (totally geodesic members)
Assume (R1) and (R2). If V_t is totally geodesic for uncountably many t, then the claim holds.

*Cited (from memory).* There are only countably many totally geodesic subvarieties of dimension ≥ 2 in M_g. Two routes:
- Wright (*Totally geodesic submanifolds of Teichmüller space*, J. Differential Geom., 2020) proves that totally geodesic subvarieties of dimension ≥ 2 come from GL(2,ℝ)-orbit closures of quadratic differentials, and that there are only finitely many of them in each moduli space;
- countability alternatively follows from that correspondence together with Eskin–Mirzakhani–Mohammadi.

*Proof.* Let S be the uncountable set of such t. The map t ↦ V_t on S takes countably many values, so some W equals V_t for uncountably many t ∈ S. For those t, ∂V_t = closure(W) ∩ Δ_Γ, so Y_t is the same point. Corollary U.2(c) gives the claim. ∎

(With Wright's finiteness, "uncountably many" can be weakened to "a set of t with an accumulation point in Δ".)

### Theorem U.6 (rigidity of complex structure ⇒ claim)
Fix m ≥ 3 and let M′ = M_g[m] = T_g/Γ′, where Γ′ = ker(Mod_g → Sp(2g, ℤ/m)). For t ∈ Δ let V′_t be an irreducible component of p^{-1}(V_t), where p : M′ → M_g is the finite quotient by G = Sp(2g,ℤ/m). Assume (R1) and (R2). If the set of isomorphism classes of the analytic spaces V′_t, t ∈ Δ, is countable, then Y_t = Y_0 for all t. In particular this holds if all V′_t are biholomorphic to one another.

*Cited.*
- (a) Γ′ is torsion-free (Serre). M′ is a smooth quasi-projective variety and a K(Γ′,1), since T_g is contractible and Γ′ acts freely. T_g is biholomorphic to a bounded domain (Bers).
- (b) **Imayoshi–Shiga rigidity** (Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces", MSRI Publ. 11, 1988; the rigidity half of the Parshin–Arakelov theorem; from memory). Let C be a Riemann surface of finite type. Two locally non-trivial holomorphic families of compact genus-g curves over C with conjugate monodromy are isomorphic over C. Consequently, if u_1, u_2 : C → M′ are non-constant, holomorphic and homotopic, then p∘u_1 = p∘u_2.

**Lemma U.6.1.** Let C be of finite type and u : C → M′ holomorphic. If u_* : π_1(C) → Γ′ has finite image, then u is constant.

*Proof.* Γ′ is torsion-free, so u_* is trivial and u lifts to ũ : C → T_g ⊂ ℂ^N, which is bounded. Bounded holomorphic functions extend over the punctures of C, so ũ extends to the compact surface C̄ and is constant by the maximum principle. ∎

**Lemma U.6.2.** Let 𝔅 be an irreducible quasi-projective variety and f_1, f_2 : 𝔅 → M′ homotopic holomorphic maps. Assume every b ∈ 𝔅 lies on an irreducible curve C ⊂ 𝔅 with f_1|_C non-constant; this holds, for example, when f_1 is injective. Then p∘f_1 = p∘f_2.

*Proof.* Let ν : C̃ → C be the normalisation, a finite-type Riemann surface. f_1∘ν and f_2∘ν are homotopic. f_1∘ν is non-constant, so its monodromy is infinite (Lemma U.6.1); hence so is that of f_2∘ν, which is therefore non-constant too. By (b), p∘f_1∘ν = p∘f_2∘ν. Evaluate at a preimage of b. ∎

**Lemma U.6.3.** For 𝔅 as above, the set {p∘f : f : 𝔅 → M′ holomorphic and injective} is countable.

*Proof.* M′ is a K(Γ′,1), so free homotopy classes of maps 𝔅 → M′ correspond to conjugacy classes of homomorphisms π_1(𝔅) → Γ′. π_1(𝔅) is finitely generated, because 𝔅 has the homotopy type of a finite CW complex (triangulability of algebraic varieties). Γ′ is countable. So there are countably many classes, and p∘f is constant on each by Lemma U.6.2. ∎

*Proof of Theorem U.6.*
1. V_t is irreducible: it is homeomorphic to V_0. p(V′_t) = V_t, since G permutes the components of p^{-1}(V_t) transitively, and each V′_t is quasi-projective (closed in M′, with V_t quasi-projective by (R1) and Chow).
2. Some class is taken by V′_t for t in an uncountable set S. Fix t_1 ∈ S and 𝔅 := V′_{t_1}. For t ∈ S choose a biholomorphism h_t : 𝔅 → V′_t and put f_t := (inclusion)∘h_t, which is injective.
3. By Lemma U.6.3, {p(f_t(𝔅)) = V_t : t ∈ S} is countable. Each V_t determines Y_t, so Corollary U.2(c) applies. ∎

*Remark U.6.4.* If there are biholomorphisms Φ_t : V_0 → V_t, continuous in t, with Φ_0 = id, one expects V_t = V_0. Argue with curves C ⊂ V_0 and the maps Φ_t∘ν into M_g, using the finiteness half of Imayoshi–Shiga. This needs the maps to lift to a level cover compatibly in t, which fails in general when V_0 lies in the locus of curves with automorphisms. So this document claims only the level-cover form, Theorem U.6.

### Proposition U.7 (Douady isolation)
Assume (R1). Let X_t be the complex-analytic fibre over t of closure(𝒱) → Δ. If [X_0] is an isolated point of the Douady space 𝒟(M̄_g) of compact analytic subspaces of M̄_g, then the claim holds.

*Proof.*
- closure(𝒱) is reduced and irreducible, being the closure of the connected manifold 𝒱 ≅ V_0 × Δ, and it dominates Δ. So its local rings have no t-torsion, and it is flat over the smooth curve Δ.
- It is proper over Δ, since M̄_g is compact.
- By the universal property of the Douady space, t ↦ [X_t] is holomorphic. Since [X_0] is isolated, [X_t] = [X_0] for small t.
- Then closure(V_t) = supp X_t = supp X_0 = closure(V_0), so Y_t = Y_0 for small t, and Corollary U.2(b) gives the claim. ∎

(If X_0 is reduced, [X_0] = [closure V_0]. Isolation holds, for instance, if H^0(X_0, 𝒩_{X_0}) = 0. No such vanishing is known for totally geodesic surfaces.)

### Remark U.8 (total geodesy must enter globally)
Two examples show that the hypotheses other than total geodesy, and any argument local to the boundary, cannot prove the claim.
- **A global example (in M_{0,7}, not in M_g).** Let f : M̄_{0,7} → M̄_{0,5} forget the points 6, 7. Let y : Δ → M_{0,5} be a non-constant holomorphic disc with small image, and put V_t := f^{-1}(y(t)) ∩ M_{0,7}.
  - closure(V_t) is the blow-up of P^1 × P^1 at the five points (p_k(t), p_k(t)).
  - Moving the p_k by diffeomorphisms of P^1 that are translations near the p_k gives a stratum-preserving trivialisation satisfying (R1), (R2), (i), (ii).
  - For Γ = (vertex {1,6,7}) — (vertex {2,3,4,5}), ∂V_t = M_{0,4} × {y(t)′}, with y(t)′ the configuration y(t) with label 1 renamed as the node. So the constant factor moves.
  - V_0 is not known to be totally geodesic, and the ambient space is M_{0,7}. So this is not a counterexample; it shows only that every hypothesis except total geodesy is compatible with a moving Y_t.
- **Local example.** At a generic point of ∂V_0 (under a mild hypothesis on automorphisms), the germ of closure(V_0) admits local stratum-preserving deformations that move the constant factor: in the product chart, replace Y_0 by Y_t. So no argument confined to a neighbourhood of ∂V_0 can work.


---

# Part I — The geometry of closure(V_0) at t = 0

**What this Part proves.** All results of this Part are statements about V_0 alone, at t = 0. They use smoothness, closedness and total geodesy of V_0, and the problem's hypotheses at t = 0. They do not use (R1) or (R2), except in Convention 0.6, which only records how strata are transported for later Parts. The results are:
- Lemma PA (§1);
- the Fuchsian toolbox (Lemmas B, Conv, Conj, Lim), Theorem F2*, Corollaries G′* and Φ̂, Lemma TR and Theorem TV (§2);
- Lemmas PT, CS, CL and J0 (§3);
- Theorem X*_all (§4);
- the walk chain: Lemma NH, Lemma TI, Lemma S̃′ and Proposition K_w (§5);
- Corollary IMOV_all (§6).

The classical facts used are listed with precise statements in §I.7. Proposition Ψ (§I.6A), formerly a cited fact, is now proved. Open points are listed in §I.8. Nothing in Part I proves the problem's claim.

## I.0. Readings, conventions, notation

**0.1 Readings of the hypotheses.**
- **(R0)** V_0 is a closed (in M_g), irreducible, 2-dimensional algebraic subvariety of the coarse space M_g, and it is smooth. "Totally geodesic" means that every complex Teichmüller geodesic (Teichmüller disc) tangent to V_0 at a point lies in V_0. Equivalently, for every X ∈ V_0 and every non-zero tangent vector v of V_0 at X, the Teichmüller disc generated by the norming differential q_v of v (see (Dual)) lies in V_0. In that case (X, q_v) is called a **generating pair**. Smoothness means V_0 is a complex submanifold of the coarse space. In particular every point of V_0 is a locally irreducible point of V_0. Where only this weaker property (Sm) is used, I say so.
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- **(R2)** There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties: it is smooth on V_0 × Δ; it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum (including M_g); and H_0 = id.
- **Use of the readings in Part I.** All results of Part I are statements about V_0 alone, at t = 0. They use (R0) and total geodesy, and they use neither (R1) nor (R2). The only exception is Convention 0.6, which records how strata are transported for later Parts. For each result I list the hypotheses actually used.
- **Closure.** closure(V_0) is a closed analytic subset of the projective coarse space M̄_g, hence an irreducible projective surface (Chow). B_0 := closure(V_0) ∖ V_0 = closure(V_0) ∩ ∂M̄_g, because V_0 is closed in M_g.

**0.2 Strata.** For a stable graph G with at least one edge:
- Δ̂_G := ∏_{w∈V(G)} M_w, where M_w := M_{g_w,n_w} and the n_w special points are labelled by half-edges and legs.
- ξ_G: Δ̂_G → Δ_G is the finite gluing map. On coarse spaces it is the quotient by Aut(G), which acts by permuting factors and relabelling special points.
- G (or Δ_G) is of **product type** if ξ_G is injective. For the problem's Γ, ξ_Γ is an isomorphism.
- T_G := ∏_w T_w, where T_w is the Teichmüller space of type (g_w,n_w) with labelled special points. Mod_Π := ∏_w Mod_w (pure mapping class groups), and p: T_G → Δ̂_G is the quotient map.
- **Piece.** A *piece at t = 0* is a 1-dimensional irreducible component E of closure(V_0) ∩ Δ_G. A *lifted piece* is a 1-dimensional irreducible component Ê of Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ Δ̂_G. (For product type the two notions coincide.) The normalisation is denoted ν: E^ν → E, or Ê^ν → Ê.
- **Facts on Â.** Â is a closed analytic subset of Δ̂_G of dimension ≤ 1, since closure(V_0) ∩ ∂M̄_g has dimension ≤ 1. It is algebraic (Chow), so it has finitely many irreducible components and finitely many singular points.

**0.3 Charts.** For a stable curve Q with dual graph G_Q:
- **Def(Q).** Def(Q) is the Kuranishi (plumbing) space: a small ball B ⊂ C^{3g−3}, Aut(Q)-invariant, with coordinates (z, (s_e)_{e∈E(G_Q)}). Here s_e is the smoothing parameter of the node e, and q: B → B/Aut(Q) ⊂ M̄_g is the orbifold chart.
- N := ∏_e s_e, and B° := B ∖ {N = 0} = q^{-1}(M_g) ∩ B.
- **Stratum locus.** L := {s_e = 0 ∀e}. Fixing an identification G_Q ≅ G gives the partial-normalisation map Π: L → Δ̂_G, with ξ_G∘Π = q|_L.
- **Labels.** Labels are the vertices of G_Q. A label x is *intact* at p ∈ B if s_e(p) = 0 for every edge e at x. Then F_x(p) denotes that component of the fibre C_p, with its special points. On L_x := {s_e = 0 ∀ e at x}, the map F_x is holomorphic into M_x.
- **Branches and lifts.** A *branch* of a curve at a point is an irreducible component of its germ there. A *lift* β̃ of a branch β of B_0 at Q is an irreducible component of the germ of q^{-1}(β) at 0. The lifts of β are the a·β̃, a ∈ Aut(Q).
- **Sheet.** A *sheet* at Q is an irreducible component of the germ at 0 of q^{-1}(closure V_0). For B a small enough Milnor ball these are represented by the global irreducible components of q^{-1}(closure V_0) ∩ B (Milnor conic structure, cited).

**0.4 Canonical chart description (CD)** (Abikoff, Bers, Hubbard–Koch, Wolpert; cited from memory). Let T̄_g be augmented Teichmüller space, and Q̃ ∈ T̄_g a point over Q with node curves α_e (e ∈ E(G_Q)).
- Stab(Q̃) ⊂ Mod_g sits in an exact sequence 1 → Tw → Stab(Q̃) → Aut(Q) → 1, where Tw ≅ Z^{E(G_Q)} is generated by the Dehn twists about the α_e.
- There is a Stab(Q̃)-invariant neighbourhood U of Q̃ that is precisely invariant (gU ∩ U = ∅ for g ∉ Stab(Q̃)), such that:
  - U/Tw ≅ B ⊂ Def(Q), compatibly with the maps to M̄_g;
  - U/Stab(Q̃) ≅ B/Aut(Q) = q(B);
  - U° := U ∩ T_g → B° is a holomorphic covering with group Tw, which acts freely.
- Write p_U: U → B for this map. The node curve α_e is pinched at a point of U exactly where s_e∘p_U = 0. The components of S ∖ ∪_e α_e are marked subsurfaces Σ_y, one for each label y. At a point of U over p ∈ L_y, the Σ_y-part of the marked stable curve is F_y(p).

**0.5 Teichmüller notation.**
- Q(X) is the space of integrable holomorphic quadratic differentials (at most simple poles at punctures).
- ‖·‖_T is the Teichmüller norm. Teichmüller distance is d_T = ½ log K.
- d_H is the hyperbolic metric of curvature −4 on H = SO(2)\SL(2,R), with d_H(SO(2)a, SO(2)b) = ½ log K(ba^{-1}).
- K(g) is the dilatation of the real-linear map g.
- For a pair (X,q), the *Teichmüller disc* g ↦ g·(X,q) is denoted D_{(X,q)}: H → T, and u = its projection to moduli space.

**0.6 Strata under H (used only in later Parts).** By (R2), H_t maps closure(V_0) ∩ Δ_G onto closure(V_t) ∩ Δ_G.

---

## I.1. Lemma PA (positive area at generic points of every piece)

**Hypotheses used:** (R0) (smoothness of V_0 is used, so that tangent vectors at points of V_0 are Teichmüller tangent vectors) and total geodesy (only in Step 5). Product type is not needed.

**Cited facts:** (Pl) with smooth Kuranishi data, (Dual), (Bun). See "Cited classical facts".

**Setting.** Let E be a piece in any stratum Δ_G, and P ∈ E. Work in the chart Def(P) = B, with coordinates (z, (t_e)_{e∈E(G)}), where z = (z_w)_w and z_w is a coordinate on the Kuranishi space of the component Y_w. The stratum locus is L = {t = 0}, with labels w ∈ V(G).

**Notation of transplantation.** By (Pl), X(z,t) is obtained from the components Y_w(z) = h_z(Y_w) (h_z a smooth quasiconformal diffeomorphism, conformal off a fixed compact K_w ⊂ Y_w, with h_z → id in C^∞ on compacts as z → 0) by plumbing z_e w_e = t_e in fixed coordinate discs. For r > 0 put Y_w^r := Y_w minus the coordinate discs of radius r. For |t| small there is a natural embedding ι = ι_{(z,t)}: Y_w^r → X(z,t), in the marking class, equal to h_z on Y_w^r. For a quadratic differential φ on X(z,t), "ι^*φ → φ_w locally uniformly on Y_w" means:
- uniform convergence of the coefficients on compact subsets of Y_w ∖ K_w, where ι is holomorphic;
- uniform convergence of h_z^*(φ|_{h_z(K_w)}), as smooth tensors, on K_w.

**Lemma PA.** Let E be a piece in a stratum Δ_G (any G). There is a discrete subset Ξ ⊂ E such that for every P ∈ E ∖ Ξ the following hold.
- There are a branch N of closure(V_0) at P containing the germ of E at P, points X_n ∈ V_0 ∩ N with X_n → P, non-zero tangent vectors v_n of V_0 at X_n, and the norming differentials q_n ∈ Q(X_n), ‖q_n‖_1 = 1, of the v_n. Each (X_n, q_n) is a generating pair.
- After passing to a subsequence, ι_n^*q_n → q_w locally uniformly on each Y_w, with q_w ∈ Q(Y_w).
- Let a = (a_w)_w ≠ 0 be the tangent vector of E at P in the chart (a_w ∈ T_{Y_w}M_w), and A := max_w ‖a_w‖_T > 0. Then:
  1. Σ_w ‖q_w‖_1 = 1 (no area is lost in the collars);
  2. q_w ≠ 0 implies ‖a_w‖_T = A (the vertices of maximal Teichmüller speed), and q_w then norms a_w;
  3. some q_j ≠ 0;
  4. in particular, if w is a constant vertex of E (π_w|_E constant), then a_w = 0 and q_w = 0. In the problem's situation (G = Γ, E ⊂ ∂V_0), q_i = 0 and j ≠ i.

*Proof.*

**Step 1 (local model; genericity).**
- Since E ⊂ closure(V_0), some branch of the germ of q^{-1}(closure V_0) at the point over P contains a lift of the germ of E. Let N be that branch and ν: N^ν → N its normalisation, a normal surface germ.
- Normal surfaces have isolated singularities, and ν^{-1}(E) is a curve. Hence for P outside a discrete set, N^ν is smooth at the point over P and there are coordinates (s,τ) on N^ν in which ν^{-1}(E) = {τ = 0}.
- The plumbing coordinates pull back to holomorphic functions t_e(s,τ) vanishing on {τ = 0}. Write t_e = u_e τ^{m_e} with m_e ≥ 1 and u_e not divisible by τ. The zero set of u_e|_{τ=0} is discrete.
- z(s,0) parametrises E, and a := ∂_s z(s_0, 0).
- **The discrete set Ξ** consists of: singular points of N^ν and of ν^{-1}(E); points where s ↦ z(s,0) is not an immersion (where a = 0); zeros of the u_e|_{τ=0}; points of E on other components of closure(V_0) ∩ Δ_G. (In a non-product stratum, also the images of Sing Â; this is used later.)
- **Constant vertices.** If π_w is constant on E, then z_w(s,0) is a continuous map into the finite fibre of the Kuranishi chart over that value, hence constant. So a_w = 0.
- Off Ξ, a ≠ 0, so A > 0.

**Step 2 (the vectors v_n).**
- Take τ_n → 0 with τ_n ≠ 0, and X_n := ν(s_0, τ_n). Then t_e(X_n) ≠ 0, so X_n ∈ V_0.
- v_n := dν(∂_s) at (s_0,τ_n) is a tangent vector of V_0. V_0 is smooth and B° is a local chart of T_g up to a covering, so v_n is a Teichmüller tangent vector. It is non-zero, because ∂_s z(s_0,τ_n) → a ≠ 0.
- In coordinates, v_n = (∂_s z(s_0,τ_n), (∂_s t_e(s_0,τ_n))_e). Since u_e is a unit near (s_0, 0), we have ∂_s t_e = (∂_s u_e/u_e) t_e, so |∂_s t_e| ≤ C|t_e|.
- **Collar Beltrami.** In the collar of e at X(z,t_0), with coordinate z_e on {|t_0| < |z_e| < 1}, put F_t(z) := z·exp(c λ(z)) with λ = log|z|/log|t_0| and c = log(t/t_0), and F_t = id off the collar.
  - At |z| = 1, F_t = id.
  - In the coordinate w = t_0/z, F_t is w ↦ w(t/t_0)^{1−λ}, which is the identity at |w| = 1.
  - So F_t: X(z,t_0) → X(z,t) is quasiconformal and in the marking class.
  - Since ∂_zλ = 1/(2zL) and ∂_{z̄}λ = 1/(2z̄L), with L = log|t_0|, one computes μ_{F_t} = (z/z̄)(c/2L)/(1 + c/2L).
  - Differentiating at c = 0: the vector b ∂/∂t_e (b = t_0 δ) is represented by the Beltrami differential (δ/2L)(z/z̄) on the collar. Its sup norm is |b|/(2|t_0| log(1/|t_0|)).
- **Smooth (Pl).** The vector ∂/∂z_k at (z,t) is represented by the transplant h_{z,*}μ̂_k(z) of a smooth Beltrami differential μ̂_k(z) supported in K_w, depending continuously on z.
- **Hence.** v_n is represented by μ_n = Σ_w ι_{n,*}μ_w^{(n)} + ν_n, where:
  - μ_w^{(n)} → μ_w uniformly, with μ_w representing a_w (and μ_i^{(n)} → 0 when a_i = 0);
  - ‖ν_n‖_∞ ≤ C′/log(1/max_e|t_e(X_n)|) → 0.

**Step 3 (upper bound: limsup ‖v_n‖_T ≤ A).**
- Let φ_n ∈ Q(X_n), ‖φ_n‖_1 = 1. Since |φ| is subharmonic in local coordinates, the mean value inequality makes {ι_n^*φ_n} locally bounded on each Y_w. By Montel, after a subsequence, ι_n^*φ_n → φ_w locally uniformly (on K_w in the transplanted sense: h_n → id in C^1).
- The sets ι_n(Y_w^r) are disjoint in X_n. By Fatou, Σ_w ‖φ_w‖_1 ≤ 1. An integrable holomorphic quadratic differential on a punctured disc has at most a simple pole, so φ_w ∈ Q(Y_w).
- By change of variables, ∫ ι_{n,*}μ_w^{(n)} φ_n = ∫_{K_w} μ_w^{(n)} · h_n^*φ_n → ∫ μ_w φ_w. Also |∫ ν_n φ_n| ≤ ‖ν_n‖_∞ → 0.
- Hence Re∫ μ_n φ_n → Σ_w Re∫ μ_w φ_w ≤ Σ_w ‖a_w‖_T ‖φ_w‖_1 ≤ A, by (Dual) on Y_w.
- Applying this to near-norming φ_n and using (Dual) on X_n gives limsup ‖v_n‖_T ≤ A.

**Step 4 (lower bound: liminf ‖v_n‖_T ≥ A).**
- Let j attain A, and let φ ∈ Q(Y_j), ‖φ‖_1 = 1, with Re∫ μ_j φ = A ((Dual) on Y_j).
- φ ⊕ 0 lies in the fibre at P of the holomorphic subbundle ker(a_e : e ∈ E(G)) of (Bun); it is a subbundle because the a_e are linearly independent near P. Extend φ ⊕ 0 to a holomorphic section and let φ_n be its value at X_n. Then ι_n^*φ_n → φ on Y_j and → 0 on the other Y_w.
- **Collar mass.** In the collar {|t|/r_0 < |z| < r_0} write φ_n = Σ_k c_k z^k dz².
  - c_{−2} = a_e(φ_n) = 0.
  - For k ≥ −1, |c_k| ≤ M r_0^{−k} (Cauchy on |z| = r_0).
  - The terms with k ≤ −3 equal c_k t^{k+2} w^{−k−4} dw² in w = t/z, with exponent ≥ −1, and are bounded in the same way by Cauchy on |w| = r_0.
  - Since ∫_{|z|<ρ} |z|^k dA ≤ 2πρ for k ≥ −1 and ρ ≤ 1, the mass of φ_n in {|t|/ρ < |z| < ρ} is ≤ Cρ, uniformly in n.
- Near the punctures of Y_j, φ has at most simple poles, so its tail mass is small. With convergence on the thick parts, ‖φ_n‖_1 → 1.
- Then Re∫ μ_n φ_n/‖φ_n‖ → Re∫ μ_j φ = A, so liminf ‖v_n‖_T ≥ A.

**Step 5 (the norming differentials).**
- Let q_n be the norming differential of v_n. By (Dual) the Teichmüller disc tangent to v_n is generated by q_n. v_n is tangent to V_0, so total geodesy puts that disc in V_0: (X_n, q_n) is a generating pair.
- Pass to a subsequence with ι_n^*q_n → q_w as in Step 3. Then
  A = lim ‖v_n‖_T = lim Re∫ μ_n q_n = Σ_w Re∫ μ_w q_w ≤ Σ_w ‖a_w‖_T ‖q_w‖_1 ≤ A Σ_w ‖q_w‖_1 ≤ A.
- All inequalities are equalities. Therefore:
  - Σ_w ‖q_w‖_1 = 1 (item 1);
  - if q_w ≠ 0 then ‖a_w‖_T = A, and Re∫ μ_w q_w = ‖a_w‖‖q_w‖, so q_w/‖q_w‖ norms a_w (item 2);
  - some q_j ≠ 0 (item 3);
  - a constant vertex has a_w = 0 < A, so q_w = 0 (item 4). ∎

**Remark 1.1.** The proof uses only the chart at P, the branch N, and a ≠ 0. It therefore applies verbatim to a lifted piece Ê ⊂ Δ̂_G at a point P̂ ∈ Ê ∖ (Sing Â ∪ other components) in a non-product stratum: the chart Def(P) carries the labelling of components by V(G).
- **Inside another chart.** If P lies in a chart Def(Q_0) of a nearby point Q_0, then a neighbourhood of a lift P̃ of P in Def(Q_0) is itself a Kuranishi chart for the fibre over P̃ (openness of versality, cited in (Pl)). So the X_n can be taken inside any prescribed sheet of q^{-1}(closure V_0) at P̃ containing the lift of the germ of E. This is used in §4.

---

## I.2. Fuchsian toolbox, Theorem F2*, Corollary Φ̂, Lemma TR, Theorem TV

### I.2.0 Setting

S is a closed oriented surface of genus g. For a multicurve γ = γ_G with dual graph G:
- Σ_w (w ∈ V(G)) are the closures of the components of S ∖ (open collars of γ);
- Γ_w := π_1(Σ_w) ⊂ π_1(S) is defined up to conjugation.

A *holonomy* of a marked hyperbolic surface (X,f) is a discrete faithful ρ: π_1(S) → PSL(2,R) with H/ρ(π_1 S) = X compatibly with f. It is unique up to conjugation. q̃ denotes the lift of a quadratic differential q to H via ρ.

A point P̃ of the γ_G-stratum of T̄ has marked components P̃_w ∈ T(Σ_w) = T_w and a labelled image λ(P̃) := ([P̃_w])_w ∈ Δ̂_G, with ξ_G(λ(P̃)) the image of P̃ in M̄_g.

The results of this section use the cited facts (GC1)–(GC3) and (QC1)–(QC3), Maskit's comparison (Ext), Royden, Bers, Masur and Veech.

### I.2.1 Four elementary lemmas (no hypotheses on V_0)

**Lemma B (Beltrami coefficient of an affine map).** Let q ≢ 0 be a meromorphic quadratic differential on a Riemann surface X, and let g = (g_11 g_12; g_21 g_22) ∈ GL^+(2,R). Write g as ζ ↦ αζ + βζ̄, where
α = ((g_11+g_22) + i(g_21−g_12))/2,  β = ((g_11−g_22) + i(g_21+g_12))/2,
so that |α|² − |β|² = det g > 0. Then the surface g·(X,q) is X^μ with μ = c_g q̄/|q|, where c_g := β/α and |c_g| < 1. The identity X → X^μ is the map that is affine of derivative g in natural coordinates. Moreover, for s ∈ C^*: q̄/|q| = (s̄/|s|) · \overline{(q/s)}/|q/s|.

*Proof.*
- Solving αζ + βζ̄ = (α+β)x + i(α−β)y against the matrix gives α + β = g_11 + i g_21 and α − β = g_22 − i g_12. This yields the formulas for α, β, and |α|² − |β|² = g_11g_22 − g_12g_21.
- Near a point where q ≠ 0, ∞, take a natural coordinate ζ (q = dζ²). The new chart is ζ′ = αζ + βζ̄.
- In a local coordinate z: ∂_zζ′ = αζ_z and ∂_{z̄}ζ′ = β\overline{ζ_z}. So μ = (β/α)(\overline{ζ_z}/ζ_z) dz̄/dz.
- Since q = ζ_z² dz², we have q̄/|q| = (\overline{ζ_z}/ζ_z) dz̄/dz. Hence μ = c_g q̄/|q|.
- The rescaling identity is immediate. ∎

For g ∈ SL(2,R) the identity map is the Teichmüller map of dilatation K(g) = (|α|+|β|)/(|α|−|β|). K is bi-SO(2)-invariant, and K(diag(e^s, e^{−s})) = e^{2s}.

**Lemma Conv.** Let D ⊂ C be a domain and f_n: D → C K-qc embeddings converging locally uniformly to a non-constant f, with μ_{f_n} → μ a.e. on D. Then f is a qc embedding and μ_f = μ a.e.

*Proof.*
- f is a K-qc embedding by (QC1).
- Extend μ_n := μ_{f_n} and μ by 0 to C, so ‖μ_n‖_∞ ≤ k = (K−1)/(K+1). Let w_n := w^{μ_n} and w := w^μ be the normalised solutions.
- By (QC2), w_n → w uniformly on Ĉ. The inverses w_n^{-1} are normalised K-qc maps; by (QC1) they are relatively compact, and every subsequential limit is w^{-1}. So w_n^{-1} → w^{-1} uniformly.
- Let L ⊂ w(D) be compact, and L′ ⊂ D a compact neighbourhood of w^{-1}(L). For large n, w_n^{-1}(L) ⊂ L′.
- h_n := f_n∘w_n^{-1} is conformal on w_n(D), by (QC3) (equal Beltrami coefficients).
- On L, |h_n(x) − f(w^{-1}x)| ≤ sup_{L′}|f_n − f| + ω_f(|w_n^{-1}x − w^{-1}x|) → 0, where ω_f is the modulus of continuity of f on L′.
- So h := f∘w^{-1} is a locally uniform limit of holomorphic maps, hence holomorphic, and it is injective. Therefore f = h∘w and μ_f = μ_w = μ a.e. ∎

**Lemma Conj.** Let Γ be a group and ρ_n, R: Γ → PSL(2,R) with ρ_n → R pointwise, where R is discrete, faithful and non-elementary. Let B_n ∈ PSL(2,R) with B_nρ_nB_n^{-1} → σ pointwise, σ discrete and faithful. Then a subsequence of (B_n) converges to some B ∈ PSL(2,R), and σ = BRB^{-1}.

*Proof.*
- R(Γ) contains hyperbolic R(γ_1), R(γ_2) without common fixed points (standard for non-elementary Fuchsian groups). In a discrete group, two hyperbolic elements cannot share exactly one fixed point, and if they share both they commute. So γ_1, γ_2 do not commute, and σ(γ_1), σ(γ_2) do not commute (σ faithful).
- tr σ(γ_k) = lim tr ρ_n(γ_k) = tr R(γ_k), so σ(γ_k) is hyperbolic. By the same discreteness facts, the four fixed points of σ(γ_1), σ(γ_2) are distinct.
- Fixed points of hyperbolic elements depend continuously on the element. So B_n maps three distinct points x^k_n → x^k (fixed points of ρ_n(γ_k)) to three points y^k_n → y^k (fixed points of B_nρ_n(γ_k)B_n^{-1}), with the x^k distinct and the y^k distinct.
- A Möbius map depends continuously on the images of three distinct points. Hence B_n → B with B(x^k) = y^k, and σ(γ) = lim B_nρ_n(γ)B_n^{-1} = BR(γ)B^{-1}. ∎

**Lemma Lim.** Let ρ_n → R pointwise on a group Γ, with R discrete, faithful and type-preserving. Let F̃_n: H → H be K-qc homeomorphisms and ρ′_n: Γ → PSL(2,R) with F̃_n∘ρ_n(γ) = ρ′_n(γ)∘F̃_n. Let M_n ∈ PSL(2,R) be such that M_nF̃_n fixes 0, 1, ∞; this is possible since the boundary map preserves cyclic order. Then, after a subsequence:
- M_nF̃_n → F̃ uniformly on H̄ (spherical metric), where F̃ is a K-qc self-homeomorphism of H;
- M_nρ′_nM_n^{-1} → R′ := F̃RF̃^{-1} pointwise, and R′ is discrete, faithful and type-preserving;
- F̃ descends to a K-qc homeomorphism H/R(Γ) → H/R′(Γ) inducing γ ↦ γ.

*Proof.*
- Extend by reflection to Ĉ. (QC1) gives the subsequence and the K-qc limit F̃, which preserves H. Inverses converge uniformly as well.
- So M_nρ′_n(γ)M_n^{-1} = (M_nF̃_n)ρ_n(γ)(M_nF̃_n)^{-1} → F̃R(γ)F̃^{-1} uniformly. A uniform limit of Möbius maps that is a homeomorphism is Möbius, so R′(γ) ∈ PSL(2,R).
- R′ is a faithful homomorphism. It is properly discontinuous, being conjugate by a homeomorphism to R, hence discrete.
- A parabolic element has one fixed point, on R̂; this property is preserved, so R′ is type-preserving. F̃ is equivariant, so it descends. ∎

### I.2.2 Definition FA and Theorem F2*

**Definition FA.** Let (X_n,f_n) → P̃ in T̄, with P̃ in the γ_G-stratum. (By (GC3) this can be arranged after a subsequence whenever X_n → P ∈ Δ_G.) Put Y_v := P̃_v and let σ_v be a type-preserving holonomy of Y_v. Let q_n ∈ Q(X_n) ∖ 0 and s_n > 0. **Vertex v carries η_v at scale s_n** if there are holonomies ρ_n of (X_n,f_n) with ρ_n|_{Γ_v} → σ_v pointwise and q̃_n/s_n → η̃_v locally uniformly on H, where η̃_v ≢ 0 is the σ_v-lift of a holomorphic quadratic differential η_v on Y_v. **Positive area at v** means: ‖q_n‖_1 = 1, s_n = 1, and η_v ∈ Q(Y_v).

(If s_n ∈ C^* with arg s_n → θ, Lemma B shows that replacing s_n by |s_n| replaces η_v by e^{iθ}η_v. So s_n > 0 loses no generality.)

**Theorem F2*.** Assume Definition FA at v. For g ∈ SL(2,R), let F_n: X_n → X′_n be affine of derivative g for q_n, so that X′_n = g·(X_n,q_n), and put f′_n := F_n∘f_n. Then:
1. every subsequence of (X′_n,f′_n) has a further subsequence converging in T̄, and every limit P̃′ lies in the γ_G-stratum;
2. for every such limit, P̃′_v = g·(Y_v,η_v) as marked surfaces, with the marking transported by the affine map Y_v → g·(Y_v,η_v);
3. if X′_n → P′ in M̄_g, then P′ ∈ Δ_G and the v-entry of λ(P̃′) is [g·(Y_v,η_v)]. In particular, for product-type G, π_v(P′) = [g·(Y_v,η_v)].

Neither integrability of η_v nor any control of area elsewhere is needed, and the statement is for each fixed g.

*Proof.*
- **Step 1 (lifts).** F_n lifts to a K(g)-qc map F̃_n: H → H, and there are holonomies ρ′_n of (X′_n,f′_n) with F̃_n∘ρ_n(γ) = ρ′_n(γ)∘F̃_n. By Lemma B, a.e. on H:
  μ_{F̃_n} = c_g \overline{q̃_n}/|q̃_n| = c_g \overline{(q̃_n/s_n)}/|q̃_n/s_n|.
- **Step 2 (each vertex).** Fix w. By (GC1) there are B^w_n with B^w_nρ_n|_{Γ_w}(B^w_n)^{-1} → σ_w (for w = v take B^v_n = 1). σ_w(Γ_w) is non-elementary, since P̃_w is hyperbolic of finite area. Apply Lemma Lim to these representations and the maps F̃_n(B^w_n)^{-1}. After a subsequence, Möbius conjugates of ρ′_n|_{Γ_w} converge to R′_w, discrete, faithful and type-preserving, and H/R′_w is K(g)-qc to P̃_w in the marking class, hence of finite area. Do this for the finitely many w in turn.
- **Step 3 (convergence).**
  - ℓ_{X_n}(γ_e) → 0 (GC1), so by Maskit's comparison Ext_{X_n}(γ_e) → 0.
  - Ext is K-quasi-invariant, so Ext_{X′_n}(γ_e) ≤ K(g) Ext_{X_n}(γ_e) → 0, hence ℓ_{X′_n}(γ_e) → 0.
  - By (GC2), (X′_n,f′_n) converges to the γ_G-stratum point P̃′ with P̃′_w = H/R′_w.
  - Any subsequential limit P̃″ also equals the limit of a further subsequence produced this way; T̄ is Hausdorff. This gives item 1.
- **Step 4 (the v-component).**
  - Take w = v and B^v_n = 1. In Lemma Lim, M_nF̃_n → F̃ uniformly, and μ_{M_nF̃_n} = μ_{F̃_n}.
  - The zero set Z of η̃_v is discrete. Off Z, \overline{(q̃_n/s_n)}/|q̃_n/s_n| → \overline{η̃_v}/|η̃_v|. So μ_{M_nF̃_n} → c_g\overline{η̃_v}/|η̃_v| a.e., with sup norm |c_g| < 1.
  - Lemma Conv on discs D ⋐ H gives μ_{F̃} = c_g\overline{η̃_v}/|η̃_v| a.e.
  - F̃ descends to Φ: Y_v → H/R′_v = P̃′_v in the marking class, with μ_Φ = c_g η̄_v/|η_v|. By Lemma B this is the Beltrami coefficient of the affine map ι_g: Y_v → g·(Y_v,η_v).
  - By (QC3), Φ∘ι_g^{-1} is conformal and in the marking class. It maps punctures to punctures with the same labels, because peripheral subgroups correspond. This gives item 2, independently of the subsequence.
  - Item 3 follows, since T̄ → M̄_g is continuous. ∎

**Corollary G′*.** If d_T(X_n,X′_n) → 0 and X_n → P in M̄_g, then X′_n → P. Consequently the map (M_g, d_T) → M̄_g is uniformly continuous.

*Proof.*
- It suffices to show that every subsequence has a further subsequence converging to P.
- Choose markings with (X_n,f_n) → P̃ (GC3), and Teichmüller maps F_n: X_n → X′_n of dilatation K_n → 1.
- Steps 1–3 of F2* run verbatim with F_n in place of the affine map (they use only (GC1), (GC2) and Lemma Lim). They give a limit P̃′ in the γ_G-stratum with P̃′_w ≅ H/R′_w.
- Since ‖μ_{F̃_n}‖_∞ → 0, Lemma Conv (with μ = 0) makes F̃ Möbius. So P̃′_w = P̃_w for all w, P̃′ = P̃, and X′_n → P.
- Uniform continuity follows by the usual contradiction argument, using compactness of M̄_g. ∎

### I.2.3 Corollary Φ̂ (the marked limiting disc)

**Corollary Φ̂.** Uses total geodesy (only for the inclusion in Â). Let X_n → P ∈ Δ_G, with markings (X_n,f_n) → P̃ in the γ_G-stratum, and q_n ∈ Q(X_n) with ‖q_n‖_1 = 1. For g ∈ SL(2,R) let X^g_n := g·(X_n,q_n) and f^g_n := F^g_n∘f_n, where F^g_n is the affine map. Then there are a subsequence and continuous maps φ̂_w: H → T_w, each 1-Lipschitz from d_H to d_T, such that for every g, (X^g_n, f^g_n) converges in T̄ to the γ_G-stratum point P̃^g with P̃^g_w = φ̂_w(g). Put Φ := (φ̂_w)_w: H → T_G, φ̂ := p∘Φ: H → Δ̂_G, and φ := ξ_G∘φ̂. Then:
- (a) φ(g) = lim_n X^g_n in M̄_g, and φ̂(i) = λ(P̃).
- (b) If the (X_n,q_n) are generating pairs for V_0, then φ(H) ⊂ closure(V_0) ∩ Δ_G and φ̂(H) ⊂ Â.
- (c) If v carries positive area η_v (Definition FA), then φ̂_v = D, the Teichmüller disc of (Y_v,η_v) in T_v, and π_v∘φ̂ = u := (T_v → M_v)∘D.

*Proof.*
- **Countable dense set.** Let {g_k} be countable and dense in SL(2,R). By F2*(1), whose proof does not use Definition FA, and a diagonal argument, there is a subsequence along which (X^{g_k}_n, f^{g_k}_n) → P̃^{g_k} for all k.
- **Lipschitz comparison.** Fix k, l, w. The map F^{g_l}_n∘(F^{g_k}_n)^{-1} is affine of derivative g_lg_k^{-1} for g_k·q_n, so it is K_{kl} := K(g_lg_k^{-1})-qc, and it carries f^{g_k}_n to f^{g_l}_n.
  - Lift it, using holonomies of X^{g_k}_n normalised by (GC1) so that their restrictions to Γ_w converge to σ^k_w (a holonomy of P̃^{g_k}_w).
  - Lemma Lim gives a K_{kl}-qc map in the marking class from P̃^{g_k}_w onto H/R′, where R′ is a limit of conjugates of ρ^{g_l}_n|_{Γ_w}.
  - By (GC1), other conjugates of the same representations converge to σ^l_w. Lemma Conj then gives R′ conjugate to σ^l_w, as marked groups.
  - Hence d_T(P̃^{g_k}_w, P̃^{g_l}_w) ≤ ½ log K_{kl} = d_H(g_k,g_l).
- **Extension.** T_w is complete, so the map extends to a 1-Lipschitz φ̂_w on SL(2,R). It factors through SO(2)\SL(2,R) because K is bi-SO(2)-invariant.
- **Every g.** For arbitrary g, F2*(1) gives subsequential limits P̃″ in the γ_G-stratum. The same comparison gives d_T(P̃″_w, φ̂_w(g_k)) ≤ d_H(g,g_k) for all k, so P̃″_w = φ̂_w(g). A stratum point is determined by its components, so the limit is unique and the sequence converges.
- **(a)** follows from continuity of T̄ → M̄_g and X^1_n = X_n.
- **(b)** X^g_n lies on the Teichmüller disc of a generating pair, so X^g_n ∈ V_0 by total geodesy. Limits lie in closure(V_0); they lie in Δ_G by F2*(1).
- **(c)** is F2*(2). ∎

**Remark 2.1 (local uniformity).** For fixed g, g′: d_T(X^g_n, X^{g′}_n) ≤ d_H(g,g′). By Corollary G′* the maps g ↦ X^g_n are then equicontinuous into M̄_g. So the pointwise convergence X^g_n → φ(g) is locally uniform on H. This is used in §4.

### I.2.4 Lemma TR (plumbing convergence gives Definition FA)

**Setting.** As in §1: X_n = X(z_n,t_n) → P in a plumbing chart, with markings f_n from the marked plumbing family, so (X_n,f_n) → P̃. For a vertex v, ι_n: Y_v^{r_n} → X_n (r_n → 0) are (1+ε_n)-qc embeddings in the marking class (ε_n → 0), conformal off K_v. U ⊂ Y_v ∖ K_v is a non-empty connected open set.

**Lemma TR.** Assume ‖q_n‖_1 = 1 and ι_n^*q_n → q_v ≢ 0 locally uniformly on U, with q_v holomorphic on Y_v. Then, after a subsequence, v carries q_v at scale 1 in the sense of Definition FA, and ∫_{Y_v}|q_v| ≤ 1. In particular Lemma PA yields positive area at its vertex j.

*Proof.*
- **(a) Lifts.**
  - Let σ be a holonomy of Y_v, and Ỹ^r ⊂ H the preimage of Y_v^r. Ỹ^r is H minus disjoint horodiscs; it is connected and simply connected.
  - ι_n lifts to ι̃_n: Ỹ^{r_n} → H with ι̃_n∘σ(γ) = ρ_n(γ)∘ι̃_n for γ ∈ Γ_v. Normalise so that ι̃_n(x_0) = x_0.
  - The ι̃_n omit the lower half-plane, so by (QC1) and a diagonal argument a subsequence converges locally uniformly on H to ι̃.
  - ι̃ is not constant. Otherwise, for γ with σ(γ) hyperbolic, d(x_0, ρ_n(γ)x_0) → 0, so ℓ_{X_n}(γ) → 0, contradicting ℓ_{X_n}(γ) → ℓ_{Y_v}(γ) > 0 (GC1).
  - By Lemma Conv (with μ = 0), ι̃ is a conformal embedding.
  - Each ρ_n(γ) moves x_0 a bounded amount, so after a diagonal subsequence ρ_n|_{Γ_v} → R pointwise, with ι̃∘σ = R∘ι̃.
- **(b) ι̃ is Möbius.**
  - Suppose Ω := ι̃(H) ≠ H. Then the hyperbolic metric of Ω is strictly larger than that of H on Ω (strict Schwarz–Pick), and ι̃: H → Ω is an isometry.
  - For σ(γ) hyperbolic and x on its axis: ℓ(R(γ)) ≤ d_H(ι̃x, ι̃σ(γ)x) < length_Ω(ι̃[x,σ(γ)x]) = ℓ(σ(γ)).
  - But ℓ(R(γ)) = lim ℓ_{X_n}(γ) = ℓ_{Y_v}(γ) by (GC1) and continuity of the trace. This is a contradiction.
  - So ι̃ is Möbius. Conjugating, we may take ι̃_n → id and ρ_n|_{Γ_v} → σ.
- **(c)** On the preimage Ũ of U, ι̃_n is holomorphic, so ι̃_n′ → 1 locally uniformly. Since (q̃_n∘ι̃_n)(ι̃_n′)² → q̃_v and ι̃_n^{-1} → id, we get q̃_n → q̃_v locally uniformly on Ũ.
- **(d) Convergence on all of H.**
  - Let L ⊂ L′ be concentric closed discs in H. For large n, ι̃_n(L′) ⊃ L by a degree argument.
  - The covering H → X_n restricted to ι̃_n(L′) is at most N(L′)-to-one, where N(L′) := #{γ : σ(γ)L′ ∩ L′ ≠ ∅}; this uses that ι_n is injective. So ∫_L|q̃_n| ≤ N(L′).
  - The mean value inequality makes {q̃_n} locally bounded. By Montel and the identity theorem (the limit is q̃_v on Ũ), q̃_n → q̃_v locally uniformly on H.
- **(e) Integrability.** Take disjoint compact L′_k ⊂ H mapping injectively to Y_v with disjoint images. Then Σ_k ∫_{ι̃_n(L′_k)}|q̃_n| ≤ 1, and in the limit Σ_k ∫_{L′_k}|q̃_v| ≤ 1. Hence ∫_{Y_v}|q_v| ≤ 1. ∎

### I.2.5 Theorem TV (every piece has a Teichmüller vertex)

**Hypotheses used:** (R0), total geodesy, and Lemma PA. The stratum may be of any type.

**Theorem TV.** Let G be any stratum and Ê a 1-dimensional irreducible component of Â = ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ Δ̂_G, with normalisation ν: Ê^ν → Ê. (For product type, Ê is a piece E.) Then there are a vertex j, a curve Y_j ∈ π_j(Ê) and η_j ∈ Q(Y_j) ∖ 0 with the following properties. Let D: H → T_j be the Teichmüller disc of (Y_j,η_j), u: H → M_j its projection, and Γ′ the image in Aut(H) of the Veech group, i.e. the set of γ ∈ Aut(H) with D∘γ = ψ_γ∘D for some ψ_γ ∈ Mod_j.
1. C := closure of π_j(Ê) in M_j is a Teichmüller curve. u lifts to u^ν: H → C^ν, and C^ν = H/Γ′ via u^ν. Γ′ is a lattice.
2. p := π_j∘ν: Ê^ν → C^ν (lifted to the normalisation) is **proper**, and Ê^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p.
3. Give Ê^ν the orbifold structure of H/Λ_E. A point over an orbifold point of order m of C^ν, at which p has local degree k, has order m/k (and k | m). With this structure p is an orbifold covering, and the lift of π_j∘ν to orbifold universal covers is D, a holomorphic isometric embedding, equivariant for Λ_E → Mod_j.
4. Ê is not compact, and every end of Ê^ν maps to a cusp of C. So along every end of Ê the j-component leaves every compact subset of M_j.

Nothing is claimed about the comparison of the orbifold structure in item 3 with the one Ê inherits from Δ̂_G at the finitely many points over orbifold points of C. It is not used below.

*Proof.*

**Choice of base point.**
- Pick P̂ ∈ Ê outside Sing Â, outside the other components of Â, and outside the discrete set Ξ of Lemma PA (Remark 1.1). Let P := ξ_G(P̂).
- Lemma PA, in the chart Def(P) labelled so that the stratum point over P̂ has labelled image P̂, gives generating pairs (X_n,q_n) → P and a vertex j with q_j ≠ 0.
- Lemma TR (with U a disc in Y_j ∖ K_j where q_j ≠ 0) turns this into positive area at j, with η_j := q_j ∈ Q(Y_j).
- The plumbing markings converge to P̃ with λ(P̃) = P̂. In a non-product stratum, if one prefers not to rely on the labelled chart, see Supplement R3′ in §3: λ(P̃) = σP̂ for some σ ∈ Aut(G), and one argues for σÊ.
- Corollary Φ̂ gives φ̂: H → Â with φ̂(i) = P̂ and π_j∘φ̂ = u.

**Step 2′ (φ̂ lifts holomorphically into Ê^ν).**
- u is non-constant: D is an isometric embedding and T_j → M_j has discrete fibres. Hence Z := u^{-1}(π_j(Sing Â)) is discrete.
- Off Z, φ̂ lands in Reg Â, where it lifts uniquely and continuously to the normalisation Â^ν.
- At z_0 ∈ Z, a small punctured disc around z_0 is connected and maps into a small punctured neighbourhood of φ̂(z_0). That neighbourhood is a disjoint union of punctured branches. φ̂(z_0) is not an isolated point of Â, since otherwise φ̂ and hence u would be locally constant. So the punctured disc lies in one branch, and the lift extends continuously over z_0.
- This gives a continuous φ^ν: H → Â^ν with p∘φ^ν = u.
- The union of the components of Â^ν on which π_j∘ν is constant is open and closed. Its preimage is open and closed in H and not all of H (u is non-constant), hence empty.
- **Holomorphy (the coarse target may be singular).** At z_0 with e_0 = φ^ν(z_0), choose a holomorphic function f near p(e_0) on the normal space M_j (for instance an invariant coordinate in an orbifold chart) with f∘p non-constant near e_0. Choose a local coordinate ζ at e_0 with f∘p = ζ^k + const. Then (ζ∘φ^ν)^k = f∘u − const is holomorphic, so ζ∘φ^ν is a continuous k-th root of a holomorphic function. It is holomorphic off the zeros, and holomorphic across them by Riemann's extension theorem.
- So φ^ν is holomorphic. H is connected, so φ^ν lands in one component, the one through φ^ν(i), which lies over P̂ ∈ Ê. Hence φ^ν: H → Ê^ν.

**Step 3′ (C is a Teichmüller curve; C^ν = H/Γ′).**
- C is an irreducible algebraic curve in M_j: π_j(Ê) is constructible, and C is the closure in M_j.
- Fix a level m ≥ 3 with M[m] := T_j/Mod_j[m] a manifold. (In genus 0 and type (1,1), use any torsion-free finite-index normal subgroup, which exists by Selberg's lemma.)
- Let C′ be the component of the preimage of C containing u′(H), where u′ := (T_j → M[m])∘D.
- u′ lifts to the universal cover C̃ of C′^ν. C̃ ≅ H, because C′^ν is not covered by C or P¹: it admits a non-constant bounded holomorphic map to T_j ⊂ C^N (Bers embedding), and Liouville applies.
- Let Λ: C̃ → T_j be the lift with Λ∘ũ = D, adjusted by a deck transformation so that the two lifts of u′ agree. By Royden (Kobayashi = Teichmüller on T_j), D is a Kobayashi isometry. Λ and ũ are Kobayashi contractions, so ũ preserves d_H, and hence ũ ∈ Aut(H). Therefore u′: H → C′^ν is the universal covering.
- **Definition.** Define Γ′ := {γ ∈ Aut(H) : u^ν∘γ = u^ν}, using the lift u^ν: H → C^ν rather than u (which could identify points on different branches at singular points of C).
- C^ν ≅ C′^ν/Stab(C′): a finite birational map between normal curves is an isomorphism.
- **Bijectivity of H/Γ′ → C^ν.** If u^ν(x) = u^ν(y), the images of x and y in C′^ν differ by an element of the finite group Stab(C′)/Mod_j[m]. Lifting that element through the universal covering u′ gives γ ∈ Γ′ with u′(γx) = u′(y), so y ∈ π_1(C′^ν)·γx ⊂ Γ′x.
- Γ′ ⊃ π_1(C′^ν) with finite index, and π_1(C′^ν) is a lattice (C′^ν is an algebraic curve). So Γ′ is a lattice. Since D∘γ and D are both lifts of u differing by a Mod_j-element on a non-discrete set, Γ′ is the projectivised Veech group, by Lemma CS of §3.

**Step 4′ (Ê^ν = H/Λ_E; properness of p).**
- Let p̄: Ē^ν → C̄^ν be the extension of p to smooth compactifications.
- Let C° ⊂ C^ν be C^ν minus three finite sets: the orbifold points of H/Γ′, the branch values of p̄, and p̄(Ē^ν ∖ Ê^ν) ∩ C^ν. Put E° := p̄^{-1}(C°) ⊂ Ê^ν and H° := (u^ν)^{-1}(C°), which is connected.
- p: E° → C° is a finite unramified covering (a restriction of p̄ to a full preimage). u^ν: H° → C° is the regular Γ′-covering. φ^ν(H°) ⊂ E°.
- **φ^ν(H°) = E°.** φ^ν is locally p^{-1}∘u^ν, hence a local homeomorphism, so the image is open. It is also closed in E°: take an evenly covered disc for both coverings; the sheets of u^ν map onto sheets of p. E° is connected.
- So φ^ν: H° → E° is a covering (a continuous surjection φ with p∘φ and p coverings is a covering). It is an intermediate cover of the regular Γ′-cover, hence the quotient by Λ_E := {γ ∈ Γ′ : φ^ν∘γ = φ^ν}, of index deg p.
- **h is a biholomorphism.** φ^ν descends to a holomorphic h: H/Λ_E → p̄^{-1}(C^ν). h is proper, because H/Λ_E → C^ν is finite. It is injective over the dense set C°, and its target is connected. A proper holomorphic map that is injective on a dense open set has degree 1, so h is biholomorphic.
- Hence p̄^{-1}(C^ν) = φ^ν(H) ⊂ Ê^ν ⊂ p̄^{-1}(C^ν). So Ê^ν = p̄^{-1}(C^ν), which is item 2, including the properness of p.

**Item 3.** At x ∈ H over an orbifold point c of order m, Stab_{Γ′}(x) ≅ Z/m and Stab_{Λ_E}(x) ≅ Z/m′, so the local degree is k = m/m′. The lift is D, because π_j∘ν∘φ^ν = u = proj∘D.

**Item 4.**
- p is proper, and C^ν → M_j is proper (C is closed in M_j). So every end of Ê^ν leaves every compact subset of M_j under π_j, i.e. maps to a cusp of C.
- Ê is not compact, because Γ′ is not cocompact. (Veech; cited. A lattice Veech group contains parabolic elements: by Masur's theorem there is a cylinder direction, and by the Veech dichotomy it is parabolic.) Λ_E has finite index in Γ′, so it is not cocompact either, and Ê^ν = H/Λ_E is not compact. ∎

**Remark 2.2 (the problem's Δ_Γ).** For G = Γ and Ê = E ⊂ ∂V_0 with π_i(∂V_0) = {Y_0}: j ≠ i by Lemma PA(4).

---

## I.3. Lemmas PT, CS, CL and J0

### I.3.1 Lemma PT (no hypotheses on V_0)

**Lemma PT.** Let Δ_G be of product type, Q ∈ Δ_G, α ∈ Aut(Q), and x a vertex of G with dim M_x > 0. Then:
- α maps the component Q_x to itself.
- More precisely, the map Π: L ⊂ Def(Q) → Δ̂_G does not depend on the identification G_Q ≅ G.
- comp_x = pr_x∘Π on L, and comp_x(αp) ≅ comp_x(p) for all p ∈ L and α ∈ Aut(Q).

*Proof.*
1. α induces σ ∈ Aut(G). σ acts on Δ̂_G by permuting factors and relabelling special points, and ξ_G∘σ = ξ_G, since gluing does not see the order of the factors.
2. ξ_G is injective, so σ acts as the identity on Δ̂_G.
3. Suppose σ(x) = x′ ≠ x. Then for every z ∈ Δ̂_G the coordinate z_{x′} is a fixed relabelling of z_x. The coordinates are independent and M_{x′} ≅ M_x is positive-dimensional, so we can choose z with z_{x′} different from all finitely many relabellings of z_x. This is a contradiction, so σ(x) = x.
4. Two identifications G_Q ≅ G differ by some σ ∈ Aut(G), which acts trivially by step 2, so Π is unchanged. Hence comp_x(αp) ≅ comp_{α^{-1}x}(p) = comp_x(p). ∎

Consequence: in a product-type stratum no automorphism of a stable curve moves a vertex of positive-dimensional type. In particular no automorphism moves the vertex i of the problem's Δ_Γ, which has dim M_{g_i,n_i} > 0 because π_i is a factor on which ∂V_0 is constant while dim ∂V_0 = 1. (Strictly, positive dimension of M_{g_i,n_i} is part of the problem's setting: a factor of dimension 0 would make the claim trivial.)

### I.3.2 Two lifting lemmas (no hypotheses on V_0)

Let Γ be a countable group acting properly discontinuously by biholomorphisms on a complex manifold T, let X := T/Γ with Cartan's quotient structure, let p: T → X be the quotient map, and let Q be a connected Riemann surface.

**Lemma CS.** If F, F′: Q → T are holomorphic with p∘F = p∘F′, then F′ = g∘F for some g ∈ Γ. The set of such g is a coset g·S_F, where S_F := {s ∈ Γ : s∘F ≡ F} is finite.

*Proof.*
- Q = ∪_{g∈Γ} Z_g, where Z_g := {F′ = gF} is a closed analytic subset.
- Γ is countable, so by Baire some Z_g has interior. By the identity theorem, F′ ≡ gF.
- gF ≡ g′F if and only if g^{-1}g′ ∈ S_F, and S_F ⊂ Stab(F(y)), which is finite. ∎

**Lemma CL.** If h: Q → X is holomorphic and L: Q → T is continuous with p∘L = h, then L is holomorphic.

*Proof.* The statement is local; fix y_0 and put x̂ := L(y_0), A := Stab_Γ(x̂) (finite).
- **Chart (Cartan).** There is an A-invariant neighbourhood B of x̂ that is A-equivariantly a ball with linear A-action, such that gB ∩ B ≠ ∅ implies g ∈ A, and B/A → X is an open embedding.
- **Invariants.** Let σ = (σ_1,…,σ_m) be generators of the A-invariant polynomials. They separate A-orbits, and they descend to holomorphic functions σ̄ on B/A. So σ̄∘h is holomorphic near y_0.
- **Fibre product.** Take a disc Q_0 ∋ y_0 with L(closure Q_0) ⊂ B, and put Z := {(y,b) ∈ Q_0 × B : σ(b) = σ̄(h(y))}.
  - Z is analytic, and its fibre over y is A·L(y).
  - Z is proper over Q_0, since fibres lie in the compact set A·L(closure Q_0).
  - Let Σ be the image of Sing Z, of the 0-dimensional part of Z, and of the critical points of the projection on Reg Z. Σ is discrete: a curve of critical points would lie in a finite fibre.
  - Over Q_0 ∖ Σ, Z is a finite covering whose local sheets are graphs of holomorphic maps.
- **Conclusion.** y ↦ (y, L(y)) is a continuous section, so over each evenly covered disc it stays in one sheet. Hence L is holomorphic off Σ. It is continuous and bounded in ball coordinates, so it is holomorphic on Q_0 by Riemann's extension theorem. ∎

### I.3.3 Lemma J0 (the joint vertex map lifts at t = 0)

**Hypotheses used:** those of Theorem TV and Corollary Φ̂, i.e. (R0), total geodesy and Lemma PA. Neither (R1) nor (R2) is used.

**Lemma J0.** Let Ê be a 1-dimensional component of Â (any stratum G). Take j, D, Γ′, Λ := Λ_E as in Theorem TV, and let q_Λ: H → H/Λ = Ê^ν be the quotient map. There are γ_0 ∈ Γ′ and a holomorphic F: H → T_G with:
- (i) p∘F = ν∘q_Λ, so F lifts the whole vertex map of Ê;
- (ii) pr_j∘F = D∘γ_0^{-1}, an isometric holomorphic embedding onto the Teichmüller disc D(H);
- (iii) for every λ ∈ Λ, the set R(λ) := {g ∈ Mod_Π : F∘λ = g∘F} is a coset of the finite group S := {s ∈ Mod_Π : s∘F ≡ F}; every element of R(λ) normalises S; and R(λμ) = R(λ)R(μ).

*Proof.* Let P̂ and Φ = (φ̂_w)_w: H → T_G be as in the proof of Theorem TV (Corollary Φ̂), with φ̂ = p∘Φ, φ̂(i) = P̂ and π_j∘φ̂ = u. Write κ: C^ν → M_j for the normalisation map, so that κ∘u^ν = u.

**Step 1 (φ̂(H) ⊂ Ê).**
- Let Z be the union of three sets: the points of Ê on other components of Â; the isolated points of Â; and the components Ê′ ≠ Ê of Â on which π_j is constant. Z is closed and is a locally finite union of points and curves.
- For a compact disc K ⊂ H, φ̂(K) meets only finitely many of these, and π_j takes finitely many values on φ̂(K) ∩ Z. So φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite set) ∩ K, which is finite. Hence φ̂^{-1}(Z) is discrete, and H^o := H ∖ φ̂^{-1}(Z) is connected.
- Â ∖ Z is the disjoint union of Ê ∖ Z and the sets Ê′ ∖ Z (π_j non-constant on Ê′). Each is relatively closed and the family is locally finite, so Ê ∖ Z is open and closed in Â ∖ Z.
- Its preimage is open and closed in H^o and contains i, since P̂ ∉ Z. So φ̂(H^o) ⊂ Ê, and by density and closedness φ̂(H) ⊂ Ê.

**Step 2 (φ̂ is holomorphic).**
- Let Σ_E be the set of points of Ê that are singular, or at which π_j|_Ê is not a local biholomorphism onto a smooth point of C. Σ_E is discrete in Ê, and as in Step 1, φ̂^{-1}(Σ_E) is discrete.
- Off it, φ̂ = (π_j|_{U_e})^{-1}∘u is holomorphic.
- By Riemann's extension theorem (in a local embedding of Δ̂_G), φ̂ is holomorphic on H.

**Step 3.** φ̂ lifts to a holomorphic φ^ν: H → Ê^ν (universal property of normalisation; H is smooth and φ̂^{-1}(Sing Ê) is discrete). Then κ∘p∘φ^ν = u = κ∘u^ν. κ is injective off a finite set, so p∘φ^ν = u^ν off a discrete set, hence everywhere.

**Step 4 (φ^ν = q_Λ∘γ_0).**
- Let Br ⊂ C^ν be the set of orbifold points, and H^♮ := (u^ν)^{-1}(C^ν ∖ Br), which is connected. Over C^ν ∖ Br, both u^ν and p: H/Λ → H/Γ′ are coverings.
- Fix x_0 ∈ H^♮. The fibre p^{-1}(u^ν(x_0)) is {q_Λ(γx_0) : γ ∈ Γ′}, so φ^ν(x_0) = q_Λ(γ_0x_0) for some γ_0 ∈ Γ′.
- φ^ν and q_Λ∘γ_0 are lifts of u^ν|_{H^♮} through a covering that agree at x_0. So they agree on H^♮, and by density on H.

**Step 5.**
- Put F := Φ∘γ_0^{-1}. It is continuous, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q_Λ.
- ν∘q_Λ is holomorphic, so F is holomorphic by Lemma CL (with T = T_G, Γ = Mod_Π). This gives (i).
- (ii) holds because pr_j∘Φ = D and γ_0^{-1} is an isometry of H.
- (iii): F∘λ and F are holomorphic lifts of ν∘q_Λ∘λ = ν∘q_Λ, so Lemma CS gives the coset statement.
  - Normality: if g ∈ R(λ) and s ∈ S, then sgF = s(F∘λ) = (sF)∘λ = F∘λ = gF, so g^{-1}sg ∈ S.
  - Product rule: if a ∈ R(λ) and b ∈ R(μ), then F∘λμ = a(F∘μ) = abF, so ab ∈ R(λμ). By normality R(λ)R(μ) = abS = R(λμ). ∎

**Supplement R3′ (non-product strata: the base point).** Corollary Φ̂ gives φ̂(i) = λ(P̃), the labelled image of the marked limit. In general λ(P̃) = σP̂ for some σ ∈ Aut(G) (the finite group Mod_G/Mod_Π acting on Δ̂_G). σP̂ is again generic: σ permutes the components of the σ-invariant set Â and preserves Sing Â. So Steps 1–5 run verbatim for the lifted piece σÊ, with vertex j and Teichmüller disc D. Let σ̃ ∈ Mod_G be a lift of σ^{-1}; it normalises Mod_Π. Then σ̃∘F satisfies (i)–(iii) for Ê, with the following replacements: Teichmüller vertex σ^{-1}(j); the same Λ (via (σÊ)^ν ≅ Ê^ν); S replaced by σ̃Sσ̃^{-1}; R(λ) replaced by σ̃R(λ)σ̃^{-1}. Hence J0 holds for every lifted piece. Nothing downstream uses which vertex is the Teichmüller vertex.

**Consequence.** At t = 0, the joint vertex map of every piece has an equivariant holomorphic lift over the single orbifold structure H/Λ_E, for which the Teichmüller coordinate is an isometry. Every cone point of the joint map is a cone point of Λ_E, of dividing order.

---

## I.4. Theorem X*_all (a sheet through a branch of a piece meets the boundary only in that branch)

**Hypotheses used:** (R0), including smoothness of V_0 (used through Lemma PA), and total geodesy. The stratum may be of any type. (R1), (R2) and the reading (T4) are not used.

### I.4.1 Lemma M and Lemma P (local analytic geometry; no hypotheses on V_0)

**Lemma M.** Let M be a real symmetric negative definite r×r matrix with M_kj ≥ 0 for k ≠ j, whose graph (k ~ j iff M_kj > 0) is connected. If Mc = −b with b ≥ 0 and b ≠ 0, then c_k > 0 for all k.

*Proof.*
- Write c = c⁺ − c⁻ with c^± ≥ 0 of disjoint supports. Then (c⁻)ᵀMc = (c⁻)ᵀMc⁺ − (c⁻)ᵀMc⁻.
- The first term is ≥ 0, by disjoint supports and off-diagonal entries ≥ 0. The second term, −(c⁻)ᵀMc⁻, is > 0 unless c⁻ = 0.
- But (c⁻)ᵀMc = −(c⁻)ᵀb ≤ 0. So c⁻ = 0 and c ≥ 0.
- If c_k = 0, then −b_k = Σ_{j≠k} M_kj c_j ≥ 0. This forces c_j = 0 for every neighbour j of k. By connectedness c = 0, hence b = 0: a contradiction. ∎

**Lemma P.** Let (Ŝ,ŝ_0) be a normal 2-dimensional germ, W a small Stein representative, C ⊂ W a curve through ŝ_0 (a finite union of irreducible germs), and A_1,…,A_l irreducible curve germs at ŝ_0 not contained in C. After shrinking W, there is a holomorphic function g on W ∖ C such that |g(z_n)| → ∞ for every l′ and every sequence z_n ∈ A_{l′} ∖ {ŝ_0} with z_n → ŝ_0.

*Proof.*
1. Take π: W̃ → W as in (Res). Let E_1,…,E_r be the components of Exc = π^{-1}(ŝ_0), C̃ the strict transform of C, and p_{l′} the point where the strict transform Ã_{l′} meets Exc (Str).
2. **Mumford pull-back.** Put b_k := C̃·E_k ≥ 0. Then b ≠ 0, since C passes through ŝ_0 (Str). Solve Mc* = −b, where M = (E_k·E_j) is negative definite (Neg) with connected graph. By Lemma M, c*_k > 0.
3. **Anti-ample cycle.** Solve Mz = −(1,…,1). By Lemma M, z_k > 0. Choose an integer d ≥ 1 with dz integral, and put Z := Σ_k dz_k E_k. Then Z·E_j = −d.
4. **The divisor.** Choose an integer m ≥ 1 with mc*_k ∈ Z and mc*_k − dz_k ≥ 1 for all k. Then D := m(C̃ + Σ c*_k E_k) − Z = mC̃ + Σ_k (mc*_k − dz_k)E_k is an effective integral divisor with support C̃ ∪ Exc, and D·E_j = d > 0 for all j.
5. **Sections.** Let L := O(D) with canonical section s. By (RA), after shrinking W, L^{⊗N} is globally generated for some N. Choose a global section σ with σ(p_{l′}) ≠ 0 for all l′.
6. Put g̃ := σ/s^N. It is holomorphic on W̃ ∖ (C̃ ∪ Exc), which π maps biholomorphically onto W ∖ C. Put g := g̃∘π^{-1}.
7. **Blow-up along A_{l′}.** If z_n ∈ A_{l′} ∖ ŝ_0 and z_n → ŝ_0, then π^{-1}(z_n) → p_{l′}. There σ ≠ 0, while s^N(p_{l′}) = 0 because Exc ⊂ supp D. So |g(z_n)| → ∞. ∎

### I.4.2 Statement

**Setting.**
- E is a piece in a stratum Δ_G (any G), and Q_0 ∈ E, so Q_0 lies in the stratum of E.
- β is a branch of E at Q_0, and β̃ ⊂ L ⊂ Def(Q_0) is a lift of β.
- S is a sheet at Q_0 with S ⊃ β̃. ν_S: Ŝ → S is its normalisation, and ν_S^{-1}(0) = {ŝ_0} (S is an irreducible germ). B̂ := ν_S^{-1}(S ∩ {N = 0}).
- An irreducible component of the germ (B̂,ŝ_0) is *of type β̃* if it maps onto β̃. These are denoted Ê_1,…,Ê_r, with r ≥ 1. All other components are *foreign*; this includes any component over a lift aβ̃ ≠ β̃ of the same coarse branch.

**Theorem X*_all.** There is no foreign component. Equivalently, S ∩ {∏_e s_e = 0} = β̃ near 0.

**Corollary 4.1.**
- Two distinct lifts β̃ ≠ aβ̃ never lie in a common sheet, and neither do lifts of two different branches of E at Q_0.
- Distinct lifted boundary branches at Q_0 that lie in a common sheet cannot include a branch of a piece whose stratum contains Q_0.

### I.4.3 Proof

Choose the chart ball B ⊂ Def(Q_0) small (Milnor ball for q^{-1}(closure V_0) and for q^{-1}(B_0)). Then:
- the sheets are global components of q^{-1}(closure V_0) ∩ B;
- the lifted branches of q^{-1}(B_0) at 0 are closed in B, and pairwise meet only at 0;
- each lifted branch minus 0 is smooth.

**Step 1 (base point).**
- Π(β̃) is an irreducible curve germ at ẑ_0 := Π(0) contained in Â, since ξ_G∘Π = q. It lies in a unique lifted piece Ê, because distinct components meet in finitely many points.
- Let e_0 ∈ Ê^ν be the point over ẑ_0 on the branch Π(β̃).
- Use Ê^ν = H/Λ_E (Theorem TV). Choose a closed disc B_e ⊂ Ê^ν around e_0 that is the image of a closed hyperbolic disc B̃_e ⊂ H centred at a preimage of e_0 and precisely invariant under its stabiliser in Λ_E (gB̃_e ∩ B̃_e ≠ ∅ only for g ∈ Stab). Every component of the preimage of int B_e is then a translate of int B̃_e, on which q_Λ is proper onto int B_e. Require moreover: ν(B_e) is contained in the germ Π(β̃ ∩ B_{1/2}), where B_{1/2} is a smaller Aut(Q_0)-invariant ball; and ξ_G(ν(B_e ∖ e_0)) ⊂ β ∖ {Q_0}.
- Pick P̃_1 ∈ β̃ ∖ {0} with Π(P̃_1) ∈ ν(int B_e) and P_1 := q(P̃_1) generic. Generic means: P_1 ∉ Ξ (Lemma PA), and Π(P̃_1) is off Sing Â and off the other components of Â. The excluded set is discrete.

**Step 2 (approximants in S).**
- By Remark 1.1, a neighbourhood of P̃_1 in B is a Kuranishi chart of the fibre over P̃_1. Take for N in Lemma PA a local branch of S at P̃_1 containing the germ of β̃. This is possible since S ⊃ β̃.
- Lemma PA gives points X̃_n = ν(s_0,τ_n) ∈ S ∩ B° and generating pairs (X_n,q_n), with X_n := q(X̃_n) → P_1. Choosing s_0 and the τ_n generically, X̃_n lies off Sing S and off the other components of q^{-1}(closure V_0) ∩ B. (Both are proper analytic subsets of the branch N, and the curve τ ↦ ν(s_0,τ) is not contained in them for generic s_0.)
- **Markings.** By (CD) choose X̂_n ∈ U° over X̃_n, with U the neighbourhood of a point Q̃_0 over Q_0. After a subsequence, X̂_n → P̃ ∈ U over P̃_1.
  - The node curves of P̃ are the α_e of Q̃_0, since P̃_1 ∈ L.
  - The vertex subsurfaces Σ_y are labelled by V(G_{Q_0}) ≅ V(G).
  - So, with this labelling, λ(P̃) = Π(P̃_1) =: P̂_1.
- **Lemma TR and Corollary Φ̂.** Lemma TR gives positive area at the vertex j of Lemma PA. Corollary Φ̂ (with Lemma TR) gives Φ, φ̂ with φ̂(i) = P̂_1 and π_j∘φ̂ = u. Write D_n(g) := X^g_n.
- **Lemma J0.** P̂_1 is generic in the sense of Theorem TV. So Steps 1–4 of Lemma J0 (with base point P̂_1) give φ̂(H) ⊂ Ê and φ^ν = q_Λ∘γ_0: H → Ê^ν. In particular φ^ν is surjective.

**Step 3 (a path to Q_0).**
- Let W_e be the component of (φ^ν)^{-1}(int B_e) containing i. Since φ^ν = q_Λ∘γ_0, W_e is γ_0^{-1} of a translate of int B̃_e, and φ^ν is proper from W_e onto int B_e.
- Hence there is w* ∈ W_e with φ^ν(w*) = e_0.
- Join i to w* by a path in W_e, and let Ω ⊂ W_e be a connected relatively compact open neighbourhood of it.
- Put φ := ξ_G∘φ̂ = ξ_G∘ν∘φ^ν. Then φ(Ω̄) ⊂ q(B_{1/2}), φ(Ω) ⊂ β ∪ {Q_0}, and φ^{-1}(Q_0) ∩ Ω = (φ^ν)^{-1}(e_0) ∩ Ω, which is discrete and contains w*.

**Step 4 (chart lifts and their limit).**
- By Remark 2.1, D_n → φ uniformly on Ω̄. So for large n, D_n(Ω̄) ⊂ q(B_{1/2}).
- Let D̂_n: H → T_g be the Teichmüller disc of (X̂_n, q_n). The preimage of q(B) ∩ M_g in T_g is the disjoint union of the translates gU°, and D̂_n(Ω̄) is connected and contains X̂_n ∈ U°. So D̂_n(Ω̄) ⊂ U°.
- Put D̃_n := p_U∘D̂_n: Ω → B_{1/2} ∩ B°. It is holomorphic, with q∘D̃_n = D_n and D̃_n(i) = X̃_n.
- **D̃_n(Ω) ⊂ S.** The sets D̃_n^{-1}(S_l), for the global components S_l of q^{-1}(closure V_0) ∩ B, are analytic and cover the connected Ω. So one of them is all of Ω. It contains i, and X̃_n lies only on S.
- **Limit.** By Montel, a subsequence D̃_n → L̃: Ω → B̄_{1/2} ⊂ B, holomorphic, with q∘L̃ = φ|_Ω.
  - Hence L̃(Ω) ⊂ q^{-1}(β ∪ {Q_0}) ∩ S ⊂ ∪_a aβ̃.
  - L̃(i) = P̃_1 ∈ β̃, and L̃^{-1}(0) = φ^{-1}(Q_0) ∩ Ω is discrete and contains w*.
  - The sets aβ̃ ∖ 0 are pairwise disjoint or equal, and closed in B ∖ 0. Ω minus a discrete set is connected. So L̃(Ω) ⊂ β̃, L̃(w*) = 0, and L̃ is non-constant.
- **Lift to Ŝ.** D̃_n(i) = X̃_n ∉ Sing S, so D̃_n(Ω) is not contained in the non-normal locus of S. By the universal property of normalisation (cited), D̃_n lifts uniquely to a holomorphic D̂^S_n: Ω → Ŝ. Its image avoids B̂, because D̃_n(Ω) ⊂ B°.
- ν_S is finite, so the D̂^S_n are locally bounded in a local embedding of Ŝ. By Montel, a subsequence converges to L̂_S: Ω → Ŝ with ν_S∘L̂_S = L̃. In particular L̂_S(w*) = ŝ_0, and L̂_S^{-1}(ŝ_0) = L̃^{-1}(0) is discrete.

**Step 5′ (maximum principle).** Suppose a foreign component exists, and let C be the union of all foreign components.
1. L̂_S(Ω) ⊂ ν_S^{-1}(β̃). Shrink a Stein representative W of (Ŝ,ŝ_0) so that ν_S^{-1}(β̃) ∩ W = (Ê_1 ∪ … ∪ Ê_r) ∩ W and W ∩ C ∩ (∪Ê_l) = {ŝ_0}. (A foreign component maps onto a curve germ other than β̃, so it meets ν_S^{-1}(β̃) only at ŝ_0 near ŝ_0.) Apply Lemma P to (W, C, Ê_1,…,Ê_r) to get g.
2. Choose a closed disc Δ* ⊂ Ω centred at w* with L̂_S(Δ*) ⊂ W and L̂_S^{-1}(ŝ_0) ∩ Δ* = {w*}. Then L̂_S(Δ* ∖ w*) ⊂ (∪Ê_l) ∖ ŝ_0 ⊂ W ∖ C, and K := L̂_S(∂Δ*) is a compact subset of W ∖ C.
3. D̂^S_n → L̂_S uniformly on Δ*. Fix a compact neighbourhood K′ ⊂ W ∖ C of K. For large n, D̂^S_n(∂Δ*) ⊂ K′ and D̂^S_n(Δ*) ⊂ W. So max_{∂Δ*}|g∘D̂^S_n| → max_{∂Δ*}|g∘L̂_S| =: M_* < ∞.
4. D̂^S_n(Δ*) ⊂ W ∖ B̂ ⊂ W ∖ C, so g∘D̂^S_n is holomorphic on Δ*. By the maximum principle, |g∘D̂^S_n| ≤ max_{∂Δ*}|g∘D̂^S_n| on Δ*.
5. For w ∈ Δ* ∖ {w*}, g is continuous at L̂_S(w) ∈ W ∖ C, so |g(L̂_S(w))| ≤ M_*.
6. Take w_k → w* with w_k ≠ w*. After a subsequence the points L̂_S(w_k) lie on one Ê_{l′} and tend to ŝ_0. By Lemma P, |g(L̂_S(w_k))| → ∞, contradicting step 5.

Hence there is no foreign component. ν_S maps B̂ onto S ∩ {N = 0}, so S ∩ {N = 0} = β̃ near 0. ∎

*Proof of Corollary 4.1.* If aβ̃ ≠ β̃, or a lift of another branch, lay in S, it would be a curve germ in S ∩ {N = 0} different from β̃. ∎

**Remark 4.2.** Total geodesy enters only through Lemma PA, Corollary Φ̂ and Lemma J0. Together they produce discs in the interior of S that converge to a parametrisation of β̃ through 0.


---

## I.5. The walk chain: Lemma NH, Lemma TI, Lemma S̃′, Proposition K_w

**Hypotheses used.**
- (R0), including smoothness, and total geodesy.
- The problem's hypotheses at t = 0 only: Γ is of product type; ∂V_0 := closure(V_0) ∩ Δ_Γ has dimension 1; π_i(∂V_0) = {Y_0}.
- Neither (R1), (R2) nor (T4) is used.

### I.5.1 Data

- **Base point.** Let D^1 be a 1-dimensional component of ∂V_0 and P ∈ D^1 a generic point (it will also be required to avoid the finite set Σ below).
- **Generating pairs.** Lemma PA at P gives generating pairs (X_n,q_n), ‖q_n‖ = 1, X_n → P, with limit differentials (q_w)_w: q_i = 0, and q_j ≠ 0 for some j ≠ i.
- **Markings.** Mark X_n by the plumbing family, so that (X_n,f_n) → P̃ ∈ T̄_g. Σ_w ⊂ S denotes the vertex subsurfaces of P̃. In particular ∂Σ_i = {γ_e : e ∈ Γ_i}, where Γ_i is the set of edges at i, and Σ_i is a fixed marked subsurface ("path marking").
- **The function ψ.** Fix a pants decomposition P_i of Σ_i. For X̂ ∈ T_g, ψ(X̂) ∈ T(Σ_i°) is the point whose Fenchel–Nielsen coordinates on P_i are those of X̂, with the boundary lengths of ∂Σ_i set to 0. Here Σ_i° is Σ_i with its boundary curves replaced by punctures labelled as at P. [ψ] is its class in M̄_{g_i,n_i}, and d is a metric on M̄_{g_i,n_i} for labelled points. The properties of ψ used below are Proposition Ψ(a)–(d), proved in §I.6A.
- **The rays.** Let γ̂_n(s) := g_s·(X̂_n,q_n) ∈ T_g be the Teichmüller ray (g_s = diag(e^{−s},e^{s})), and γ_n(s) its image in M_g. γ_n(s) ∈ V_0 by total geodesy.

### I.5.2 Lemma NH (choice of direction)

**Lemma NH.** After passing to a subsequence and replacing q_n by e^{−2iθ_n}q_n with θ_n → 0 (which keeps all conclusions of Lemma PA, the limits being multiplied by e^{−2iθ_n} → 1), we may assume:
1. there are an essential non-peripheral curve c of Y_j (hence a curve of S not homotopic into ∪_e γ_e) and m > 0 such that each q_n has a horizontal cylinder in the class c_n of c, of modulus ≥ m; hence Ext_{γ̂_n(s)}(c_n) ≤ e^{−2s}/m for all s ≥ 0;
2. there is e_0 ∈ Γ_i such that the q_n-geodesic representative of γ_{e_0} is not horizontal; hence Ext_{γ̂_n(s)}(γ_{e_0}) → ∞ as s → ∞, for each n.

*Proof.*
- By Lemma TR, q_j is integrable on Y_j. Masur's theorem (cited) says that cylinder directions of a finite-area quadratic differential are dense in RP¹.
- **Cylinder cores are non-peripheral.** If a cylinder core bounded a disc containing at most one puncture, Gauss–Bonnet would fail. The flat disc bounded by a geodesic core needs total interior curvature 2π. Zeros contribute ≤ −π each, and the only possible puncture, a simple pole, contributes π. So a disc would need at least two poles.
- **Direction of γ_{e_0}.** Fix a non-loop edge e_0 at i. It exists: Γ is connected, and it has more than one vertex, since otherwise π_i constant on ∂V_0 would force dim ∂V_0 = 0. For each n, the q_n-geodesic of γ_{e_0} is either a cylinder core or a chain of saddle connections. If all its segments are parallel, call the common direction θ_n ∈ RP¹; otherwise θ_n is undefined. Pass to a subsequence along which θ_n is always undefined or converges to some θ_∞.
- **Choice of cylinder.** Choose a cylinder direction of q_j different from θ_∞, and rotate so that it is horizontal. Let A ⊂ Y_j be the open horizontal cylinder and A′ ⋐ A a compact sub-annulus of modulus m′ > 0.
  - A′ may meet K_j, where ι_n is not holomorphic. But q_n is holomorphic on the region ι_n(A′) ⊂ X_n. By smooth (Pl) (h_n → id in C^∞) and the transplanted convergence of §1, the pull-back of q_n to A′ converges to q_j in C¹ as a smooth tensor. So the flat structures of q_n on ι_n(A′) converge to that of q_j on A′. This is all the argument below uses.
  - √q_n is defined on ι_n(A′) for large n (the sign holonomy around the core is discrete and converges). The developing map of ι_n(A′) is equivariant under a translation v_n → v ∈ R ∖ {0}, and its image contains a strip in direction v_n of width close to that of A′.
  - So q_n has a cylinder in the class of c of modulus ≥ m := m′/2, in direction arg v_n → 0. Put θ_n := arg v_n and rotate by it; the cylinder becomes exactly horizontal.
  - Under g_s the modulus of a horizontal cylinder is multiplied by e^{2s}, and Ext ≤ 1/modulus. This gives item 1.
- **Item 2.** Since arg v_n → 0 ≠ θ_∞, for large n the rotated geodesic of γ_{e_0} is not horizontal. Then its vertical measure v_n := i(γ_{e_0}, F_hor(q_n)) is > 0 (the q-geodesic realises intersection numbers with the measured foliations; cited). So ℓ_{g_sq_n}(γ_{e_0}) ≥ e^s v_n, and Ext ≥ ℓ²/Area = ℓ² → ∞. ∎

**The stopping time.** For δ, η > 0 let T_n = T_n(δ,η) be the first s ≥ 0 at which max_{e∈Γ_i} Ext_{γ̂_n(s)}(γ_e) = δ or d(ψ(γ̂_n(s)), Y_0) = η.
- T_n < ∞ by NH(2).
- For n large, T_n > 0, since at s = 0 both quantities are small: X̂_n → P̃ in T̄_g, so Ext(γ_e) → 0 ((GC1) and Maskit); and Σ_i is a vertex subsurface of P̃ whose component is Y_0 (π_i(P) = Y_0), so d([ψ(X̂_n)], Y_0) → 0 by Proposition Ψ(c).
- On [0,T_n] both quantities are ≤ δ and ≤ η respectively.

### I.5.3 The special set, the radii, the thresholds

**The special set Σ.** Σ ⊂ B_0 is the union of the following sets:
- (Σ1) junctions: points lying in the closures of two distinct pieces (pieces of all strata);
- (Σ2) singular points of B_0;
- (Σ3) punctures of pieces: closure(D) ∖ D;
- (Σ4) points of a piece D at which some vertex that is non-constant on D, of type (g_i,n_i), has value class [Y_0];
- (Σ5) for every piece D in a stratum Δ_G, the set R(D) of points z ∈ D near which ξ_G^{-1}(D) is not a disjoint union of smooth arcs each mapped homeomorphically onto a neighbourhood of z in D.

**Σ is finite.**
- There are finitely many strata. Each closure(V_0) ∩ Δ_G is algebraic of dimension ≤ 1, so there are finitely many pieces.
- D is closed in Δ_G, so closure(D) ∖ D ⊂ ∂Δ_G is a proper analytic subset of the compact irreducible curve closure(D), hence finite.
- (Σ1), (Σ2), (Σ4) are finite by the same compactness: a non-constant algebraic function on an irreducible curve takes a value finitely often.
- R(D) consists of images of the singular points of the compact curve ξ̄_G^{-1}(closure D) ⊂ ∏_w M̄_w, which include all crossings Ê_k ∩ σÊ_k, and of the ramification points of the finite maps from the normalisations of its components to the normalisation of closure(D). Both sets are finite.
- **Every point of B_0 ∖ Σ is an interior point of exactly one piece.** It lies in some stratum Δ_G. B_0 has pure dimension 1, since ∂M̄_g is locally the zero set of one function, N_Aut := ∏_{a∈Aut} a^*N, on the irreducible surface closure(V_0). If the point were isolated in closure(V_0) ∩ Δ_G, it would lie in the closure of a piece of another stratum, as a puncture (Σ3).
- Require P ∉ Σ.

**The metric.** Fix a metric d̄ on M̄_g that, near each J ∈ Σ, is the quotient of an Aut(J)-invariant Euclidean metric on the chart ball B_J ⊂ Def(J). Then small balls B(J,ρ) are images of round Aut(J)-invariant balls B̃(J,ρ).

**Choice of r** (first). r > 0 is so small that:
- the balls B(J,3r), J ∈ Σ, are pairwise disjoint, and P ∉ ∪_J B(J,3r);
- B̃(J,3r) ⊂ B_J lies inside the (CD)-image of a precisely invariant neighbourhood U_J of a lift J̃ of J;
- B̃(J,3r) is a Milnor ball for q^{-1}(closure V_0) and for q^{-1}(B_0). So the global irreducible components X̃_1,…,X̃_p of q^{-1}(closure V_0) ∩ B̃(J,3r) represent the sheets at J, and q^{-1}(B_0) ∩ B̃(J,3r) is the union of the lifted branches at 0;
- distinct lifted branches meet only at 0 in B̃(J,3r), and each lifted branch minus 0 is smooth there (finitely many pairs of distinct irreducible germs; Puiseux);
- B_0 ∩ B(J,3r) is the union of the branches of B_0 at J, each branch minus J lying in one stratum.

Put K_D := closure(D) ∖ ∪_J B(J,r/2) for every piece D. Then K_D ⊂ D is compact (punctures are in Σ). The K_D are pairwise disjoint, because common points of two closures are junctions. Let 4ρ_* be less than the least distance between distinct K_D.

**Thresholds** (then δ, η and a possibly smaller ρ_*, depending on r). Let ℓ_1 > 0 be less than half the systole of every component of every point of K_* := ∪_D K_D. ℓ_1 exists because K_D is a compact subset of the stratum of D, and the systole of components is continuous and positive there.
- **(a)** δ < c_1, where c_1 > 0 is chosen so that Ext_X(c) ≤ c_1 implies ℓ_X(c) < ℓ_1 (Maskit: ℓ ≤ π Ext).
- **(a′) Gap property.** By shrinking ρ_*: for every X̂ ∈ T_g whose image lies within ρ_* of some z ∈ K_D, the curves c with Ext_X̂(c) ≤ c_1 form exactly the node multicurve of a lift z̃ ∈ T̄_g of a point z′ ∈ K_D, and each of them has Ext_X̂(c) ≤ ε(ρ_*), where ε(ρ) → 0 as ρ → 0 and ε(ρ_*) < δ.
  - *Proof of (a′), by contradiction.* Suppose X̂_k has image within 1/k of K_D, and either some curve c_k has Ext ∈ (ε_0, c_1], or the set {Ext ≤ c_1} is not a node multicurve as stated. After a subsequence the images converge to z ∈ K_D. By (GC3) there are h_k ∈ Mod_g with h_kX̂_k → z̃ over z. By (Thin) (cited), for large k the curves of length < ℓ_1 on h_kX̂_k are exactly the node curves of z̃, and their lengths tend to 0, hence so do their Ext (Maskit). This contradicts both alternatives, with z′ := z and the lift h_k^{-1}z̃.
- **(b)** For every piece D and every vertex u of type (g_i,n_i) that is non-constant on D, the class of u on K_D is at distance > 2η from [Y_0]. For every constant vertex (of type (g_i,n_i)) of every piece whose value class is not [Y_0], that value is at distance > 2η from [Y_0]. (Only finitely many values are involved.)
- **(b0)** 2η < d(Y_0, ∂M̄_{g_i,n_i}).
- **(b1)** 2η < min{d(σY_0,Y_0) : σ ∈ S_{n_i}, σY_0 ≠ Y_0} (relabellings of the special points; the stopping rule uses the labelled distance, while "≅ Y_0" is unlabelled).
- **(b2)** Let K̂_* := ξ^{-1}(K_*) ⊂ ∪_G Δ̂_G. For each piece D, ξ_{G_D}^{-1}(K_D) is a finite disjoint union of compact sets K̂_D^1, K̂_D^2, …. Each is contained in one lifted piece and is mapped homeomorphically onto a union of components of K_D. This holds because R(D) ⊂ Σ, and K_D avoids the r/2-balls around R(D). Let 4ρ̂ be less than their mutual distances, measured in a fixed metric on ∏_w M̄_w.

Finally choose n_0 such that for n ≥ n_0: ρ_n < min(ρ_*, r/2) (Step 0 below), and the o(1) terms of Lemma TI below are less than min(δ, η, ρ̂).

### I.5.4 Step 0 (closeness to B_0)

**Claim.** ρ_n := sup_{s≤T_n} d̄(γ_n(s), B_0) → 0.

*Proof.*
- Let s_n ≤ T_n. γ_n(s_n) ∈ V_0, so every limit point lies in closure(V_0).
- If s_n is bounded: d_T(X_n, γ_n(s_n)) = s_n. Kerckhoff's formula gives Ext_{γ̂_n(s_n)}(γ_e) ≤ e^{2s_n} Ext_{X̂_n}(γ_e) → 0.
- If s_n → ∞ (along a subsequence): Ext(c_n) ≤ e^{−2s_n}/m → 0 by NH(1).
- In both cases some curve has Ext → 0, hence hyperbolic length → 0 (Maskit), so every limit point lies in ∂M̄_g. Hence it lies in closure(V_0) ∩ ∂M̄_g = B_0.
- If ρ_n did not tend to 0, choose s_n with d̄(γ_n(s_n), B_0) ≥ ε. A subsequence converges in the compact M̄_g to a point of B_0, a contradiction. ∎

### I.5.5 Step 1 (travel times and excursions)

Fix n ≥ n_0.
- **Travel times.** A time s ∈ [0,T_n] is a *travel time* if γ_n(s) ∉ ∪_J B(J,r).
- **Excursions.** An *excursion at J* is a maximal subinterval of [0,T_n] on which γ_n stays in B(J,2r) and which contains a time in B(J,r).
- **Finitely many excursions.** γ_n(0) = X_n is near P, and P ∉ B(J,3r). So each excursion contains a crossing of the shell r ≤ d̄(·,J) ≤ 2r. By uniform continuity of γ_n on [0,T_n], each crossing takes time ≥ τ_n > 0. The balls B(J,3r) are disjoint, so excursions at different points are disjoint. Hence there are at most T_n/τ_n + 1 excursions.
- **Times outside excursions are travel times.** A time with γ_n(s) ∈ B(J,r) lies in an excursion.
- **A unique piece at each travel time.** If s is a travel time and z ∈ B_0 with d̄(z,γ_n(s)) ≤ ρ_n < r/2, then z ∉ ∪_J B(J,r/2), so z ∈ K_D for some D. Two such points are within 2ρ_n < 4ρ_* of each other, so they lie in the same K_D. By continuity, D is constant on each maximal interval of travel times (a *travel interval*).
- **Structure of the walk.** [0,T_n] is a finite alternation: travel along D^1, excursion at J_1, travel along D^2, …. The first travel is along the piece D^1 ∋ P, since P ∉ Σ. The walk ends either in a travel interval or in an excursion; Step 2 excludes the former.

### I.5.6 Lemma TI (labels along a travel interval) — the "marking identification", written out

**Lemma TI.** There is n_1 ≥ n_0 such that for n ≥ n_1 and every travel interval I on a piece D (stratum Δ_G), the following hold.
1. **Constant short multicurve.** The set A(s) := {c : Ext_{γ̂_n(s)}(c) ≤ c_1} is independent of s ∈ I. Call it A. A is the node multicurve of a lift of a point of K_D, so the dual graph of A is G. Every c ∈ A has Ext ≤ ε(ρ_n) on I.
2. **Σ_i is a vertex subsurface.** ∂Σ_i ⊂ A, and Σ_i is one of the components Σ_y (y ∈ V(G_A)) of S ∖ A. Call this label c_I.
3. **Continuous labelled lift.** Fix an identification of V(G_A) with V(G), compatible with special-point labels. The map Λ(s) := ([ψ_{Σ_y}(γ̂_n(s))])_{y} ∈ ∏_y M̄_y = closure of Δ̂_G is continuous on I. It stays within o(1) of ξ^{-1}(K_D), and in fact within o(1) of a single component K̂_D^k of (b2), for all s ∈ I.
4. **The tracked vertex is a constant Y_0-vertex.** The factor c_I is a constant vertex of the lifted piece Ê ⊃ K̂_D^k, with labelled value Y_0. Along I, Ext(∂Σ_i) = o(1) and d([ψ(γ̂_n(s))], Y_0) = o(1).

In particular **the label is constant along travel intervals**: it is the fixed subsurface Σ_i, which is the vertex subsurface Σ_{c_I} of the constant short multicurve, on one lifted curve Ê. Hence T_n is not a travel time.

*Proof.*
1. For s ∈ I, γ_n(s) is within ρ_n < ρ_* of K_D, so (a′) applies. Each curve has Ext either ≤ ε(ρ_n) or > c_1. Ext_{γ̂_n(s)}(c) is continuous in s (Kerckhoff's formula gives Lipschitz dependence of log Ext). So for each c the set {s ∈ I : c ∈ A(s)} is open and closed in the interval I, hence empty or all of I. The other claims are (a′).
2. For s ≤ T_n, Ext(γ_e) ≤ δ < c_1 for e ∈ Γ_i, so ∂Σ_i ⊂ A. Suppose a curve a ∈ A lay in the interior of Σ_i and were essential and non-peripheral there. Then a non-peripheral simple closed curve of Σ_i would have Ext_{γ̂_n(s)} ≤ ε(ρ_n), hence hyperbolic length ≤ πε(ρ_n) (Maskit). By (b0), d(Y_0, ∂M̄_{g_i,n_i}) > 2η, and d([ψ(γ̂_n(s))], Y_0) ≤ η for s ≤ T_n, so d([ψ(γ̂_n(s))], ∂M̄_{g_i,n_i}) > η. Proposition Ψ(b) with η′ = η gives ε > 0, independent of n, s and of the pants decomposition, such that this is impossible once πε(ρ_n) < ε, which holds for n ≥ n_1 (enlarging n_1 if necessary; ρ_n → 0 by Step 0). So no curve of A lies inside Σ_i. Since ∂Σ_i ⊂ A, Σ_i is a component of S ∖ A.
3. Continuity of Λ follows from Proposition Ψ(a), because the Σ_y and the pants decompositions are fixed along I.
   - **Closeness, by contradiction.** Suppose there are n_k → ∞, travel intervals I_k and times s_k ∈ I_k with Λ(s_k) at distance ≥ ε from ξ^{-1}(K_D). (Finitely many pieces: pass to one D.) The images γ_{n_k}(s_k) converge to some z ∈ K_D. By (GC3) there are h_k with h_kγ̂_{n_k}(s_k) → z̃ over z. By (Thin), h_k(A_k) is, for large k, the node multicurve α(z̃).
   - h_k maps the components of S ∖ A_k onto the vertex subsurfaces of z̃. After a subsequence, the bijection V(G_{A_k}) → V(G_{z̃}) induced by h_k (composed with the fixed identifications with V(G)) is a fixed σ ∈ Aut(G). There are finitely many bijections, and the gluing data are preserved because h_k is a homeomorphism.
   - By Proposition Ψ(a), the y-coordinate of Λ(s_k) equals [ψ_{h_kΣ_y, h_kP_y}(h_kγ̂_{n_k}(s_k))], with punctures labelled through h_k. After the subsequence, h_kΣ_y is the fixed vertex subsurface of z̃ labelled σ(y), while the pants decompositions h_kP_y may vary with k. Proposition Ψ(c), which is uniform in the pants decomposition, gives convergence to the σ(y)-component of z̃. Hence Λ(s_k) → σ·λ(z̃) ∈ ξ^{-1}(z) ⊂ ξ^{-1}(K_D). This is a contradiction.
   - **One component.** ξ^{-1}(K_D) is the disjoint union of the compact sets K̂_D^k, at mutual distance ≥ 4ρ̂. The continuous path Λ(I) stays within o(1) < ρ̂ of their union, so it stays near one of them.
4. Let s ∈ I. Λ(s) is within o(1) of a point ẑ ∈ K̂_D^k ⊂ Ê. Its c_I-coordinate is [ψ(γ̂_n(s))], within η of Y_0. So pr_{c_I}(ẑ) is within η + o(1) < 2η of Y_0.
   - If c_I were a vertex non-constant on Ê, then ξ(ẑ) ∈ K_D would contradict (b).
   - So c_I is constant on Ê, and its value class is [Y_0] by (b).
   - Its labelled value lies within 2η of Y_0 and is a relabelling of Y_0, so it equals Y_0 by (b1).
   - Then, in the marking of (GC3) as in item 3, the curves of ∂Σ_i are node curves of z̃, so Ext(∂Σ_i) = o(1) uniformly.
   - Also d([ψ(γ̂_n(s))], Y_0) ≤ d(Λ(s)_{c_I}, Y_0) = o(1), because ẑ_{c_I} = Y_0, and the o(1) is uniform by the contradiction argument of item 3 (Proposition Ψ(a), (c)).
   - So neither stopping condition holds at a travel time once o(1) < min(δ,η). ∎

(Lemma TI is the "marking identification" along travel intervals. It rests on the cited facts (GC3), (Thin) and Kerckhoff's formula, and on Proposition Ψ (§I.6A). The contradiction arguments make every o(1) uniform over all travel times of all walks with n ≥ n_1.)

### I.5.7 Step 3 (the canonical chart lift inside an excursion)

Let [s_1,s_2] be an excursion at J.
- The T_g-path γ̂_n([s_1,s_2]) is connected and lies over B(J,2r) ⊂ q(B̃(J,3r)). The preimage of q(B̃(J,3r)) ∩ M_g in T_g is the disjoint union of the translates g·U_J° (precise invariance, (CD)). So the path lies in a single translate. Replace J̃ by gJ̃; this relabels the chart's marking.
- **Canonical lift.** γ̃_n := p_{U_J}∘γ̂_n: [s_1,s_2] → B̃(J,2r) ∩ B°. It is a continuous lift of γ_n, determined up to one global element of Aut(J), and no choice is made at orbifold points. (An arbitrary path lift through q may switch by an element h ∈ Stab at an orbifold point, and then the vanishing cycles at x get replaced by those at h(x); the canonical lift avoids this.)
- **Fixed marked curves.** The node curves α_e of J̃ are fixed marked curves of S, Tw-invariant, pinched exactly where s_e = 0. The components of S ∖ ∪α_e are fixed marked subsurfaces Σ_y, one for each label y of J.

**Entry.** Let the excursion be entered from the travel interval I on D, and let s_1 be the entry time (a travel time).
- By Lemma TI, at s_1 the short multicurve A has Σ_i as a component of S ∖ A, with value Y_0, and A is the node multicurve of a lift z̃ of a point z ∈ K_D within ρ_n of γ_n(s_1).
- γ̂_n(s_1) ∈ U_J and its image is near z, which lies in B(J, 2r + ρ_n) ⊂ q(B̃(J,3r)). So the lift of z near γ̃_n(s_1) is a point z̃_{s_1} ∈ B̃(J,3r), and it lies on a lifted branch β̃ of D at J.
- **A = node curves.** The node curves of the fibre over z̃_{s_1}, in the marking of U_J, are the α_e with s_e(z̃_{s_1}) = 0, i.e. with s_e ≡ 0 on β̃ (β̃ ∖ 0 lies in one stratum).
  - The point γ̃_n(s_1) is within o(1) of z̃_{s_1}. So these α_e have Ext_{γ̂_n(s_1)} = o(1) < c_1, uniformly: (CD) and Maskit, with compactness of closure(B̃(J,3r)). Hence they belong to A.
  - Their number is |E(G_D)|, which equals |A| by Lemma TI(1). Hence A = {α_e : s_e ≡ 0 on β̃}.
- **Σ_i is a single label x with no internal edge.** Σ_i is a component of S ∖ A. So it is a union of subsurfaces Σ_y over a connected subgraph S_c of G_J, glued along the α_f with f an edge of S_c (s_f ≢ 0 on β̃).
  - Suppose S_c had an edge f. Along β̃ ∖ {0}, s_f ≠ 0, but s_f → 0 at 0. So the hyperbolic length of α_f in the Σ_i-component of the fibre tends to 0 (continuity of hyperbolic metrics in plumbing families; (CD), cited).
  - That component is constant ≅ Y_0 along β̃ ∖ {0}. Indeed, its class, computed in the fixed marking of U_J, is an analytic function on the connected curve β̃ ∖ {0}. Near z̃_{s_1} it equals the value of the constant vertex c_I, namely Y_0 (Lemma TI(4)). So by the identity principle it is ≡ Y_0. And α_f is essential and non-peripheral in it. So its length is the constant ℓ_{Y_0}(α_f) > 0. Contradiction.
- Hence Σ_i = Σ_x for a single label x of J, as marked subsurfaces; all edges at x are pinched along β̃; and ∂Σ_i = {α_e : e at x}. Moreover x is intact along β̃, and F_x ≡ Y_0 (labelled) on β̃ ∖ {0}, hence on β̃ by continuity of F_x on L_x ⊃ β̃.

**Persistence and exit.**
- Σ_i (path marking) and Σ_x (marking of U_J) are both fixed marked subsurfaces, and the path stays in U_J. So Σ_i = Σ_x throughout the excursion.
- At the exit time s_2 (if the excursion is not the last), the same argument on the exit piece D′ gives a lifted branch β̃′ of D′ at J and a label x′ with Σ_i = Σ_{x′}. Then Σ_x = Σ_{x′}, so x′ = x. Equality of subsurfaces, not just of boundary-curve sets, is what fixes the label: if J has two vertices joined by all its edges, they have the same edge set.
- Hence the label **x = x_m** is well defined at each transition J_m, with entering lift β̃_m and leaving lift β̃′_m. x is a constant vertex ≅ Y_0 (labelled = Y_0) of D^m along β̃_m and of D^{m+1} along β̃′_m.

### I.5.8 Step 4 (the endpoint)

By Lemma TI, T_n lies in an excursion: the last one, at a point Q ∈ Σ, entered from a piece D along a lift β̃ with label x.
- **Normalisation.** Fix (r,δ,η). The endpoint *types* — Aut(Q)-orbits of (Q, D, β̃, x) — form a finite set. Pass to a subsequence of n with constant type, and normalise each canonical lift by the global Aut(Q)-element so that (β̃,x) is the same for all n.
- **Limit point.** Let z̃_n be a lift of a boundary point within ρ_n of γ_n(T_n), chosen within ρ_n (in the Euclidean metric of B̃) of γ̃_n(T_n). A subsequence converges to z̃^∞ ∈ q^{-1}(B_0) ∩ closure(B̃(Q,2r)).
- **z̃^∞ ≠ 0.** Suppose z̃^∞ = 0. Then γ̃_n(T_n) → 0, so s_e(γ̃_n(T_n)) → 0 for every e at x, and Ext(α_e) → 0 ((CD) and Maskit).
  - The points γ̂_n(T_n) lie in the chart neighbourhood (translated as in §5.7, with Σ_i = Σ_x), and p_U(γ̂_n(T_n)) = γ̃_n(T_n) → 0 ∈ L_x. Transporting by the normalising chart translate replaces the fixed pants decomposition P_i of Σ_i by a pants decomposition of Σ_x that may depend on n. By Proposition Ψ(d), which allows this, d([ψ(γ̂_n(T_n))], [F_x(0)]) → 0, and F_x(0) = Y_0 (labelled).
  - For large n neither stopping condition holds at T_n, a contradiction.
- So z̃^∞ lies on a lifted branch b̃ ∖ {0} at Q, the only branch through z̃^∞ in B̃(Q,3r). Pass to a further subsequence on which the same stopping condition holds for all n.
  - **Ext(α_e) = δ for some e at x.** If s_e(z̃^∞) = 0, then Ext(α_e) → 0 at T_n ((CD), Maskit), contradicting = δ. So s_e(z̃^∞) ≠ 0. Since b̃ ∖ {0} lies in one stratum, e is unpinched on all of b̃ ∖ {0}: **MERGE**.
  - **d(ψ,Y_0) = η, and no edge at x unpinched along b̃.** Then b̃ ⊂ L_x, x is intact on b̃, and by Proposition Ψ(d) (applied to γ̃_n(T_n) → z̃^∞ ∈ L_x), d(F_x(z̃^∞), Y_0) = lim d([ψ(γ̂_n(T_n))], Y_0) = η > 0, while F_x(0) = Y_0. F_x(z̃^∞) is a smooth curve by (b0). So F_x is non-constant on b̃: **MOV**. (If some edge at x is unpinched along b̃, we are in MERGE.)
- In particular b̃ ≠ β̃. By (b1), [F_x(z̃^∞)] ≠ [Y_0] in the MOV case.

### I.5.9 Lemma S̃′ (one sheet at each transition)

**Lemma S̃′.** Let J ∈ Σ, with r chosen as in §5.3. Let γ̃_{n′} be canonical lifts (§5.7) of excursion paths at J, along an infinite set of n′. Suppose their entry points are within ρ_{n′} of points of a lifted branch β̃, and their exit points (respectively the points γ̃_{n′}(T_{n′}) at the endpoint) are within ρ_{n′} of points of a lifted branch β̃′ (respectively b̃). Assume these points converge to z̃^1 ∈ β̃ ∖ {0} and z̃^2 ∈ β̃′ ∖ {0} (respectively z̃^∞ ∈ b̃ ∖ {0}). Then some global irreducible component X̃_l of q^{-1}(closure V_0) ∩ B̃(J,3r), i.e. a sheet at J, contains both β̃ and β̃′ (respectively β̃ and b̃).

*Proof.*
1. **The path lies on a holomorphic curve in q^{-1}(V_0).**
   - Let F: H → T_g be the Teichmüller disc of (X̂_{n′}, q_{n′}). Since V_0 is totally geodesic and the pair is generating, F(H) lies over V_0. (The rotation of NH does not change the disc.)
   - Let R be the connected component of F^{-1}(gU_J ∩ preimage of q(B̃(J,3r))) containing the parameters of the excursion arc. (The component of F^{-1}(gU_J) alone would not suffice, since f(R) must lie in B̃(J,3r).)
   - R is a connected Riemann surface, f := p_{U_J}∘F|_R is holomorphic, f(R) ⊂ q^{-1}(V_0) ∩ B̃(J,3r), and γ̃_{n′} ⊂ f(R).
2. **One component.** The sets f^{-1}(X̃_l) are analytic in R and cover R, so one of them has interior and, by the identity theorem, equals R. So γ̃_{n′} ⊂ X̃_{l(n′)}. This holds even if f(R) passes through crossing points of sheets at orbifold points of B°: a connected holomorphic curve cannot change sheet. (An arbitrary path lift can change sheet. Reflection model: q(u,v_1,v_2) = (u²,v_1,v_2), whose smooth coarse surface {w = v_2²} has preimage {u = v_2} ∪ {u = −v_2}.)
3. **Conclusion.**
   - Pass to a subsequence with l(n′) = l. X̃_l is closed in B̃, so z̃^1, z̃^2 ∈ X̃_l.
   - X̃_l is irreducible of dimension 2 and not contained in {N = 0}. So X̃_l ∩ {N = 0} has pure dimension 1 at z̃^1 (Krull), and it lies in q^{-1}(B_0), which near z̃^1 is the smooth curve β̃ (choice of r).
   - So X̃_l contains a neighbourhood of z̃^1 in β̃. β̃ ∩ B̃ is irreducible (Milnor ball), with normalisation a disc, and X̃_l ∩ β̃ is an analytic subset of it with interior. Hence X̃_l ⊃ β̃.
   - The same argument gives β̃′ (respectively b̃). ∎

Total geodesy is used in Step 1. The reading (T4) is not used.

### I.5.10 One chain with recurrent types

The number of excursions in [0,T_n] may grow with n, so the walks for different n need not have the same combinatorics.
- **Types.** A *transition type* is an Aut(J)-orbit of (J, β̃, β̃′, x); an *endpoint type* is an Aut(Q)-orbit of (Q, D, β̃, x). Both sets are finite.
- **Recurrent types.** Call a type recurrent if it occurs in the walks of infinitely many n. Choose N ≥ n_1 beyond the last n at which a non-recurrent type occurs.
- **Fixed walk.** Fix any n ≥ N and its walk. Every transition of this walk has a recurrent type τ.
  - Along the infinite set of n′ at which τ occurs, the corresponding excursions are canonical lifted paths in q^{-1}(V_0) ∩ B̃(J,2r). Normalise them by the global Aut(J)-element to have the same (β̃,β̃′,x). Their entry and exit points are within ρ_{n′} of points of β̃, β̃′ on the sphere of radius ≈ 2r, and a subsequence converges to z̃^1 ∈ β̃ ∖ {0}, z̃^2 ∈ β̃′ ∖ {0}.
  - Lemma S̃′ applies. Translating back by the normalising element: Aut(J) permutes the sheets, so the walk n's own pair also lies in one sheet.
- **Endpoint.** The endpoint type of the fixed walk is recurrent. Step 4, run along the n′ of that type, supplies b̃, the MERGE/MOV dichotomy and the convergent terminal points.

The witnessing sequences at different transitions come from different subsequences. No common subsequence is claimed, and none is needed in this Part.

### I.5.11 Proposition K_w (final statement)

**Proposition K_w.** Assume the hypotheses listed at the head of §5. Fix r, δ, η as in §5.3 and N as in §5.10, and fix a walk n ≥ N. Then there are:
- pieces D^1 ⊂ ∂V_0 (with D^1 ∋ P), D^2, …, D^k (in arbitrary strata);
- transition points J_1, …, J_{k−1} ∈ Σ, where J_m ∈ closure(D^m) ∩ closure(D^{m+1}), and an endpoint Q_0 ∈ Σ ∩ closure(D^k);
- at each J_m, a lifted branch β̃_m of D^m and a lifted branch β̃′_m of D^{m+1} (lifts of branches through 0 ∈ Def(J_m)), and a label x_m of G_{J_m};
- at Q_0, an entering lift β̃ of a branch of D^k, a label x, and a terminal lifted branch b̃ at Q_0, of a piece E_b;

with the following properties.
1. **Labels along travel.** Along the travel interval on D^m, the tracked subsurface Σ_i is the vertex subsurface of one fixed factor c_m of a single lifted curve Ê^m ⊂ ξ^{-1}(D^m). c_m is a constant vertex of Ê^m with labelled value Y_0 (Lemma TI). For D^1, c_1 = i.
2. **Chart labels.** At J_m, Σ_i = Σ_{x_m} in the canonical chart marking. x_m is intact and F_{x_m} ≡ Y_0 along β̃_m and along β̃′_m. All edges at x_m are pinched along both. x_m corresponds to c_m on Ê^m and to c_{m+1} on Ê^{m+1} (§5.7).
3. **Common sheet.** β̃_m and β̃′_m lie in a common irreducible component of q^{-1}(closure V_0) ∩ B̃(J_m,3r), i.e. in a common sheet at J_m (Lemma S̃′ with §5.10).
4. **Endpoint.** At Q_0, Σ_i = Σ_x, x is intact with F_x ≡ Y_0 along β̃, and β̃ and b̃ lie in a common sheet at Q_0. Along b̃ ∖ {0}, either (MERGE) some edge at x is unpinched, or (MOV) all edges at x are pinched along b̃, x is intact on b̃, F_x(0) = Y_0, and at the point z̃^∞ ∈ b̃ ∖ {0} the value F_x(z̃^∞) is at labelled distance η from Y_0 with [F_x(z̃^∞)] ≠ [Y_0]; so F_x is non-constant on b̃ and [F_x] ≢ [Y_0] along b̃.
5. **Witnesses.** For each transition and for the endpoint there is a witnessing sequence of canonical lifted Teichmüller-disc paths, as in Lemma S̃′.

*Proof.* Steps 0–4 (§§5.4–5.8), Lemma TI, Lemma S̃′ and §5.10. ∎

---

## I.6. Corollary IMOV_all

**Hypotheses used:** those of Proposition K_w (§5) and of Theorem X*_all (§4). The stratum may be of any type, and (T4) is not used.

**Corollary IMOV_all.** In the chain of Proposition K_w, let J be a transition point J_m, with entering lift β̃ (piece D = D^m) and leaving lift β̃′ (piece D′ = D^{m+1}); or let J be the endpoint Q_0, with β̃ (piece D^k) and b̃ (piece E_b).
- (a) If J lies in the stratum of D or in the stratum of D′, then β̃′ = β̃ (as germs, hence as sets in B̃(J,3r)). Consequently D′ = D, and x is intact with F_x ≡ Y_0 along β̃′ = β̃.
- (b) **Endpoint.** Q_0 lies in neither the stratum of D^k nor that of E_b. So Q_0 is a puncture of both D^k and E_b. In particular the endpoint is MERGE or puncture-MOV, never interior-MOV, whatever the stratum of Q_0.
- (c) **Property (P).** Every genuine transition (β̃′_m ≠ β̃_m) occurs at a point that is a puncture of both adjacent pieces. Transitions at R(D)-points and at other interior points of D^m or D^{m+1} are trivial (β̃′_m = β̃_m): the walk never switches lifted curve or lift of a branch inside the stratum of a piece. Junction crossings (a different piece entered at an interior point) and turning twins (β̃′ = aβ̃ ≠ β̃ at an interior point) do not occur.

*Proof.*
- (a) Suppose J lies in the stratum of D. Since D is closed in its stratum and J ∈ closure(D), J ∈ D.
  - By Proposition K_w(3), a sheet S at J contains β̃ ∪ β̃′.
  - Theorem X*_all, applied to (E, Q_0, β, S) := (D, J, q(β̃), S), gives S ∩ {N = 0} = β̃ near 0.
  - β̃′ is an irreducible curve germ at 0 inside S ∩ {N = 0}, so β̃′ = β̃ as germs. Both are irreducible representatives in the Milnor ball, so they are equal as sets.
  - Then q(β̃) ∖ {J} lies in D and in D′, so D and D′ are irreducible components of closure(V_0) ∩ Δ_G (for the same G, the stratum of β̃ ∖ 0) with infinitely many common points. Hence D = D′.
  - x is intact with F_x ≡ Y_0 along β̃ (Proposition K_w(2)), hence along β̃′. The label is x′ = x in any case, by Σ_i = Σ_x = Σ_{x′} (§5.7).
  - The case of the stratum of D′ is symmetric.
- (b) At the endpoint, Proposition K_w(4) gives a common sheet containing β̃ and b̃. If Q_0 were in the stratum of D^k or of E_b, then (a) would give b̃ = β̃, so x would be intact with F_x ≡ Y_0 along b̃.
  - This contradicts MERGE: some edge at x would be unpinched along b̃ = β̃, where all edges at x are pinched.
  - It also contradicts MOV: [F_x(z̃^∞)] ≠ [Y_0].
  - Q_0 ∈ closure(D^k) ∩ closure(E_b), since β̃ and b̃ are lifts of branches of these pieces at Q_0. So Q_0 is a puncture of both.
- (c) This is the contrapositive of (a). R(D)-points are interior points of D (Σ5), so (a) applies there. ∎

**Remark 6.1 (Lemma PT in the chain).** At a transition point or endpoint J whose stratum is of product type, every a ∈ Aut(J) fixes every label of positive-dimensional type (Lemma PT). In particular it fixes x, which has type (g_i,n_i). So normalising lifts by a global element of Aut(J) (§5.8, §5.10) never changes the tracked label at such points. Twin phenomena (a ∈ Aut(J) moving x) can only occur at points of non-product strata.

**Remark 6.2 (what Part I does not settle).** Part I is entirely about t = 0. It gives the problem's claim for no t ≠ 0. The data it hands to later Parts are:
- the chain of Proposition K_w;
- the sheet property at each transition;
- property (P) for the endpoint and for every genuine transition (Corollary IMOV_all);
- Theorem TV;
- Lemma J0.

---

## I.6A. Proposition Ψ (the subsurface restriction map) — proved here

This section proves the properties of the function ψ used in §5 and in Lemma L.1 of the Bridge. (Earlier versions of this document cited them as a classical fact "(Ψ)" whose exact scope was unchecked.) The only inputs are classical facts listed in §I.7: Fenchel–Nielsen coordinates (FN), (GC1), the collar lemma (Coll), Mumford compactness (Mum), properness of filling length functions (Prop), Thurston's stretch-map rigidity (Th) and elementary hyperbolic trigonometry (Hex).

**Conventions.**
- S is the closed reference surface of genus g. Σ′ ⊂ S is an essential subsurface: a component of S cut open along a multicurve, with boundary curves γ_1, …, γ_r. If both sides of one curve of S belong to Σ′, they count as two distinct boundary components. Σ′° is Σ′ with each γ_j replaced by a puncture, labelled by γ_j. T(Σ′°) is its Teichmüller space, M(Σ′°) the moduli space with labelled punctures, M̄(Σ′°) its Deligne–Mumford compactification with a fixed metric d, and [Y] the class of Y ∈ T(Σ′°).
- A curve β ⊂ Σ′ is *non-peripheral* if it is an essential closed curve in int Σ′ not freely homotopic into a boundary curve.
- If Σ′ is a pair of pants, T(Σ′°) is a point and everything below is trivial. So assume it is not.
- **FN data.** Let P′ be a pants decomposition of Σ′ (interior curves only), with fixed seams in every pair of pants: three disjoint arcs joining the cuffs in pairs. For b ∈ [0,∞)^r and c = (ℓ_α, τ_α)_{α∈P′} ∈ (ℝ_{>0}×ℝ)^{P′}, Φ_{P′}(b,c) is the marked surface obtained as follows. Each pair of pants with cuff lengths given by c and b is the double H ∪ H̄ of a right-angled hexagon H across its seams; a side on γ_j of length b_j/2 = 0 is replaced by an ideal vertex (a cusp). The pants are glued along each α ∈ P′ with twist τ_α. By (FN), c ↦ Φ_{P′}(0,c) is a homeomorphism (ℝ_{>0}×ℝ)^{P′} → T(Σ′°).
- For X ∈ T_g let c(X) be the P′-coordinates of X and b(X) = (ℓ_{γ_j}(X))_j. Then the bordered surface X|Σ′ obtained by cutting X along the geodesics γ_j is Φ_{P′}(b(X), c(X)), and **ψ_{Σ′,P′}(X) := Φ_{P′}(0, c(X))**. For every non-peripheral β ⊂ Σ′, ℓ_β(X|Σ′) = ℓ_β(X), since π_1(Σ′) ⊂ π_1(S) and the holonomy of X|Σ′ is the restriction.
- A *vertex subsurface* of z̃ ∈ T̄_g is a component Σ′ of S cut along the node curves of z̃. Then every boundary curve of Σ′ is a node curve of z̃, no node curve of z̃ lies in int Σ′, and the component of z̃ on Σ′ is a marked point W_{Σ′}(z̃) ∈ T(Σ′°), with cusps at the nodes on ∂Σ′.

**Proposition Ψ.**
- **(a) Continuity and naturality.** ψ_{Σ′,P′} : T_g → T(Σ′°) is continuous. For h ∈ Mod_g, ψ_{hΣ′,hP′}(hX) = h_*ψ_{Σ′,P′}(X), where h_* : T(Σ′°) → T(hΣ′°) is the change of marking. In particular [ψ_{hΣ′,hP′}(hX)] = [ψ_{Σ′,P′}(X)], with the punctures of hΣ′ labelled by the h-images of the γ_j. If h is a product of Dehn twists about curves that are disjoint from int Σ′ (for example boundary curves of Σ′), then ψ_{Σ′,P′}(hX) = ψ_{Σ′,P′}(X).
- **(b) Shrinking.** For every X ∈ T_g, every P′ and every non-peripheral closed curve β ⊂ Σ′, ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X). Consequently, for every η′ > 0 there is ε > 0, depending only on the type of Σ′°, such that: if some non-peripheral simple closed curve of Σ′ has ℓ_X < ε (for instance Ext_X < ε/π), then d([ψ_{Σ′,P′}(X)], ∂M̄(Σ′°)) < η′, for every P′.
- **(c) Convergence, uniformly in the pants decomposition.** Let X_k ∈ T_g with X_k → z̃ in T̄_g, and let Σ′ be a vertex subsurface of z̃. Let P′_k be **any** sequence of pants decompositions of Σ′. Then ψ_{Σ′,P′_k}(X_k) → W_{Σ′}(z̃) in T(Σ′°), and hence [ψ_{Σ′,P′_k}(X_k)] → [W_{Σ′}(z̃)] in M(Σ′°).
- **(d) Chart form.** Let J, a lift J̃, U, Tw, B = U/Tw and p_U be as in (CD) (§0.4), let y be a label of J, and Σ_y its marked vertex subsurface. Let w_k ∈ U ∩ T_g with p_U(w_k) → p ∈ L_y, and let P_k be any pants decompositions of Σ_y. Then [ψ_{Σ_y,P_k}(w_k)] → [F_y(p)].

The uniformity in (c) and (d) matters: in the applications the subsurface is fixed only up to a mapping class that varies with the sequence (h_k in Lemma TI(3), the twists τ_k in Lemma L.1, the chart translates in §5.8), and transporting by it replaces a fixed pants decomposition by a varying one.

### Proof of (a)
Extend P′ to a pants decomposition P of S by adding the curves γ_j and a pants decomposition of S ∖ Σ′, and extend the seams. By (FN), the P-coordinates are a homeomorphism T_g → (ℝ_{>0}×ℝ)^P. The P′-coordinates depend only on the pants inside Σ′. So ψ_{Σ′,P′} is the composite of the projection to the P′-coordinates with the homeomorphism Φ_{P′}(0,·), hence continuous.

Naturality: the geodesic representative of hα on hX is that of α on X, and h carries seams to seams. So the (hP′, h(seams))-coordinates of hX are the (P′, seams)-coordinates of X, and ψ_{hΣ′,hP′}(hX) = h_*ψ_{Σ′,P′}(X). If h is a product of twists about curves disjoint from int Σ′, h can be supported in annuli outside int Σ′; then hΣ′ = Σ′, hP′ = P′ with the same seams, the marking of X|Σ′ is unchanged, and the P′-coordinates of hX and X agree. ∎

### Proof of (b): the shrinking lemma

**Lemma S.** Let b ∈ ℝ_{>0}^r and c ∈ (ℝ_{>0}×ℝ)^{P′}. There is a continuous map F : Φ_{P′}(b,c) → Φ_{P′}(0,c) that does not increase the length of any rectifiable path and induces the marking identification on π_1(Σ′). Consequently ℓ_β(Φ_{P′}(0,c)) ≤ ℓ_β(Φ_{P′}(b,c)) for every non-peripheral closed curve β ⊂ Σ′; in particular ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X) for X ∈ T_g.

**Reduction to hexagons.** The idea is to build F pants by pants, and each pants map from a map of one hexagon H_a (boundary sides of length a = b_j/2 > 0) to the corresponding hexagon H_0 (those sides replaced by ideal vertices). The hexagon map f must have these properties:

- (H1) f is 1-Lipschitz for the hyperbolic metrics. Both hexagons are convex in ℍ², so this is the same as for their intrinsic metrics.
- (H2) f maps each "interior half-cuff" side (half of a curve of P′) isometrically onto the corresponding side, matching endpoints.
- (H3) f maps each seam side into the same seam side (or its closure through ideal vertices).
- No condition is imposed on the sides lying on the γ_j.


**Why such hexagon maps suffice.**
- Each pants is Y = H ∪ H̄, where H̄ is the mirror image across the seams. The pants map is f on H and σ_0 f σ_a on H̄, where σ is the reflection. Because f maps seams into seams, which σ fixes pointwise, the two definitions agree on the seams.
- On each interior cuff α, the pants map is the isometry fixing the seam feet. So two pants glued along α with twist τ_α, in both surfaces, give a well-defined continuous F. Pants not touching ∂Σ′ are mapped by the identity.
- F is locally 1-Lipschitz. Near any point, a geodesic segment between two nearby points crosses the hexagon sides (geodesic arcs) at finitely many points z_1, …, z_m, and each subsegment lies in one hexagon, where F is 1-Lipschitz; the triangle inequality gives d(Fx,Fy) ≤ Σ d(Fz_l, Fz_{l+1}) ≤ d(x,y). A locally 1-Lipschitz map does not increase lengths of paths.
- **F induces the marking identification.** (This item was only sketched in an earlier version; the following rigorous argument is due to an independent referee and has been checked.)
  - *The reference map.* Both Φ(b,c) and Φ(0,c) are glued from the same combinatorial data (pants, seams, cuffs, twist parameters), and the marking identification between them is induced by a reference homeomorphism Ψ_0 from the interior Φ(b,c) ∖ ∂ onto Φ(0,c), built hexagon by hexagon: on each hexagon, Ψ_0 is a homeomorphism H_a ∖ (boundary sides) → H_0 (each a closed disc minus boundary arcs, resp. ideal vertices) that maps each seam onto the same seam and each interior half-cuff onto itself as the identity in the arclength coordinate with the seam foot as origin (such a homeomorphism exists by the Schoenflies theorem, the boundary map being prescribed); it is extended to H̄_a by reflection and glued across interior cuffs, which is consistent because both surfaces have the same (ℓ_α, τ_α).
  - *The homotopy.* For z in a hexagon H_a, both Ψ_0(z) and F(z) lie in the closed-up hexagon H_0, which is convex. Let F_s(z) (s ∈ [0,1]) be the point at parameter s on the geodesic segment from Ψ_0(z) to F(z) in H_0, and define F_s on H̄_a by reflection. On a seam both endpoints lie in that seam (a geodesic arc or ray), so the segment stays in the seam, which the reflection fixes pointwise; the two definitions agree. On interior half-cuffs F = Ψ_0, so the homotopy is constant there and the gluings across cuffs match. F_s is continuous.
  - Hence F ≃ Ψ_0 on Σ′ minus an open collar of ∂Σ′, which is a deformation retract of the interior of Σ′. So F∘β ≃ Ψ_0∘β for every closed curve β in Σ′, i.e. F induces the marking identification on π_1(Σ′).
- Hence for the closed geodesic β of Φ(b,c), F∘β is freely homotopic to β in Φ(0,c) and has length ≤ ℓ_β(Φ(b,c)). Since β is non-peripheral, it has a geodesic representative in Φ(0,c), whose length minimises length in the free homotopy class. This gives the inequality.
- For X ∈ T_g: X|Σ′ = Φ(b(X), c(X)), ψ(X) = Φ(0, c(X)), and ℓ_β(X|Σ′) = ℓ_β(X).

Each pants of P′ has 1 or 2 cuffs among the γ_j; 3 cuffs would make Σ′ a pair of pants. If some γ_j coincide as curves of S they are still distinct boundary components of Σ′, so no pants has the same γ_j twice. This leaves two hexagon cases.

**Case 1: one boundary side.** Write H_a for the hexagon with alternate sides a (on γ), x, y. Here x and y are halves of interior cuffs, possibly two halves of the same curve. Its seams are s_{ax}, s_{xy}, s_{ya}, with V = x ∩ s_{xy} and W = y ∩ s_{xy}. H_0 is the hexagon with sides x, y and an ideal vertex ξ in place of a.

Write s_a = |s_{xy}(H_a)| and s_0 = |s_{xy}(H_0)|. By (Hex), cosh s_a − cosh s_0 = (cosh a − 1)/(sinh x sinh y) > 0, so s_a > s_0. Put d = (s_a − s_0)/2 > 0.

*Fermi picture.* Use Fermi coordinates (τ, h) about the line of s_{xy}: τ is the position of the foot (τ = 0 at V), and h ≥ 0 is the distance on the side of the hexagon.
- The lines of x and y are the fibres τ = 0 and τ = s (s = s_a or s_0).
- By convexity, each fibre τ = τ_0 with 0 ≤ τ_0 ≤ s meets the hexagon in a segment {0 ≤ h ≤ top(τ_0)}.
- The τ-projections of the top sides s_{ax}, a, s_{ya} are consecutive intervals [0, τ_C], [τ_C, τ_D], [τ_D, s_a]. Here C = s_{ax} ∩ a and D = a ∩ s_{ya}; monotonicity comes from (Hex). A side line cannot be perpendicular to s_{xy}: e.g. s_{ax} and s_{xy} are both perpendicular to the x-line, hence ultraparallel.
- In H_0, the ideal vertex ξ projects to a point B′ at τ = u_1′ ∈ (0, s_0); write u_2′ = s_0 − u_1′. The perpendicular ray ω′ from B′ to ξ lies in H_0. In H_0, s_{ax} projects onto [0, u_1′) and s_{ya} onto (u_1′, s_0].

*x-placement.* Put H_a and H_0 in ℍ² so that they share V, the x-side and the direction of s_{xy}. Then they also share the full line of s_{ax}: it is the perpendicular to the x-side at its other endpoint, on the same side. H_a's seam s_{ax} is the segment of this line from the top of x to C, and C lies on H_0's ray from the top of x to ξ. By monotonicity of the projection along that ray, τ_C < u_1′.

*y-placement.* Symmetrically, sharing W, the y-side and s_{ya}, one gets s_a − τ_D < u_2′.

*Cut.* Let u := u_1′ + d. Then:
- τ_C < u_1′ < u;
- τ_D > s_a − u_2′ = u_1′ + 2d > u, using s_a = s_0 + 2d.

So the fibre τ = u in H_a is a segment c from B ∈ s_{xy} up to a point of the side a. Cut H_a = P_1 ∪ P_2 along c, with P_1 = H_a ∩ {τ ≤ u} and P_2 = H_a ∩ {τ ≥ u}, both convex. Likewise cut H_0 = Q_1 ∪ Q_2 along ω′, with Q_1 = H_0 ∩ {τ ≤ u_1′}, both convex.

*The map.* In the x-placement, set f := π_{Q_1} on P_1 (nearest-point projection, 1-Lipschitz by (Hex)). In the y-placement, set f := π_{Q_2} on P_2. Check P_1; P_2 is symmetric.
- The x-side and the seam segment s_{ax} of P_1 lie in Q_1 (on its boundary), so they are fixed. This gives (H2) and (H3) for them.
- Points of s_{xy} with τ ≤ u_1′ are fixed. A point with u_1′ < τ ≤ u projects to the half-plane {τ ≤ u_1′} at B′ (s_{xy} ⟂ ω′ at B′), and B′ ∈ Q_1. So the base goes into s_{xy}.
- A point q ∈ c at height h projects to the half-plane {τ ≤ u_1′} at its foot q′ on the line of ω′. This is the orthogonal projection between two lines perpendicular to s_{xy} at distance d, so q′ is on the upper half-line, i.e. on the ray ω′ ⊂ Q_1, at a height p(h, d) depending only on (h, d). Hence π_{Q_1}(q) = q′.
- The side a goes somewhere into Q_1, which is allowed.
- From P_2 the cut c also lies at distance d beyond ω′: in the y-placement its foot is at distance s_a − u = u_2′ + d from W. So π_{Q_2}(q) is the point of ω′ at height p(h, d) too. Both definitions agree on c, and f is continuous on H_a.
- f is 1-Lipschitz on H_a: a geodesic of H_a crosses c at most once, and each piece is mapped 1-Lipschitz.
- (H2) holds for both x and y, and (H3) holds: s_{ax} → s_{ax}, s_{xy} → s_{xy}, s_{ya} → s_{ya}.

**Case 2: two boundary sides.** Write H_a for the hexagon with alternate sides a_1, a_2 (on γ's), x (an interior half-cuff), and seams σ_1 = s_{a_1 x}, σ_2 = s_{x a_2}, s_{12}. H_0 has sides x and two ideal vertices ξ_1, ξ_2. Its seams are:
- the ray L_1 from the endpoint A_1 of x to ξ_1, perpendicular to x;
- the ray L_2 from the endpoint A_2 of x to ξ_2, perpendicular to x;
- the full geodesic M = ξ_1ξ_2.

Place H_a so that it shares x, L_1 and L_2. Then σ_i = [A_i, C_i] ⊂ L_i, and f := π_{H_0}|_{H_a} is 1-Lipschitz.
- x is fixed, giving (H2). No point of H_a projects into the interior of x, because H_a lies on the inner side of the x-line.
- σ_i is fixed.
- It remains to show that s_{12}(H_a) lies in the closed half-plane beyond M (the side not containing H_0). Then each of its points projects to its foot on M, and M lies entirely in ∂H_0, so (H3) holds.

s_{12}(H_a) is the segment D_1D_2, with D_i = a_i ∩ s_{12}. By convexity of half-planes it suffices that D_1 and D_2 are beyond M. By symmetry, treat D_1.

Use the upper half-plane with ξ_1 = ∞ and A_1 = iα. Then:
- L_1 = {i t : t ≥ α};
- x is the arc of |z| = α from iα to A_2 = α e^{iφ}, with cot(φ/2) = e^{x}, so sin φ = 1/cosh x and cos φ = tanh x;
- L_2 is the circle orthogonal to |z| = α at A_2, with centre α/cos φ and radius α tan φ; its outer endpoint is ξ_2 = α(1 + sin φ)/cos φ = α coth(x/2);
- M = {Re z = α coth(x/2)}, and H_0 ⊂ {Re z ≤ α coth(x/2)};
- C_1 = i α e^{σ_1};
- the a_1-line is the circle |z| = α e^{σ_1}, and D_1 = α e^{σ_1} e^{iθ}, where arclength a_1 from the top means cot(θ/2) = e^{a_1}, i.e. cos θ = tanh a_1.

So D_1 is beyond M iff e^{σ_1} tanh a_1 ≥ coth(x/2), i.e. e^{σ_1} ≥ R := cosh a_1 (cosh x + 1)/(sinh a_1 sinh x).

By (Hex), cosh σ_1 = (cosh a_2 + cosh a_1 cosh x)/(sinh a_1 sinh x). Hence R − cosh σ_1 = (cosh a_1 − cosh a_2)/(sinh a_1 sinh x).
- If a_1 ≤ a_2 this is ≤ 0, and we are done.
- Otherwise we need sinh σ_1 ≥ (cosh a_1 − cosh a_2)/(sinh a_1 sinh x). With Nn = cosh a_1 cosh x + cosh a_2 and Dd = sinh a_1 sinh x, this means Nn² − Dd² ≥ (cosh a_1 − cosh a_2)². Factoring:

  Nn² − (cosh a_1 − cosh a_2)² = cosh a_1 (cosh x + 1)(cosh a_1 (cosh x − 1) + 2 cosh a_2),

  while Dd² = sinh² a_1 (cosh x − 1)(cosh x + 1). The required inequality reduces to

  cosh² a_1 (cosh x − 1) + 2 cosh a_1 cosh a_2 ≥ sinh² a_1 (cosh x − 1),

  which is obvious.


(The two inequalities used — cosh s_a − cosh s_0 = (cosh a − 1)/(sinh x sinh y) > 0 in Case 1, and e^{σ_1} ≥ R in Case 2 together with the factorisation displayed there — were also checked numerically on 2·10^5 random hexagons.)

*Consequence (the second sentence of (b)).* The set K := {[Y] ∈ M̄(Σ′°) : d([Y], ∂M̄(Σ′°)) ≥ η′} is a compact subset of M(Σ′°). The systole is continuous and positive on M(Σ′°), so it is ≥ some ε > 0 on K. If ℓ_β(X) < ε for a non-peripheral simple β, then sys(ψ_{Σ′,P′}(X)) ≤ ℓ_β(ψ_{Σ′,P′}(X)) ≤ ℓ_β(X) < ε by Lemma S, so [ψ_{Σ′,P′}(X)] ∉ K. Maskit's comparison ℓ ≤ π Ext gives the parenthetical form. ∎

### Proof of (c)
Write Y_k := ψ_{Σ′,P′_k}(X_k) and W := W_{Σ′}(z̃).
1. **Bounded lengths of a filling set.** Fix finitely many non-peripheral simple closed curves β_1, …, β_p of Σ′ that fill Σ′° (every non-peripheral simple closed curve of Σ′ meets some β_j essentially; e.g. a pants decomposition of Σ′ together with one dual curve for each of its curves). Since Σ′ is a vertex subsurface of z̃, (GC1) gives ℓ_β(X_k) → ℓ_β(W) for every non-peripheral closed curve β ⊂ Σ′. By Lemma S, ℓ_{β_j}(Y_k) ≤ ℓ_{β_j}(X_k), which is bounded in k. This bound does not depend on the P′_k.
2. **Precompactness.** By (Prop), {Y ∈ T(Σ′°) : ℓ_{β_j}(Y) ≤ C for all j} is compact. So every subsequence of (Y_k) has a further subsequence converging to some W′ ∈ T(Σ′°).
3. **Identification of the limit.** Length functions are continuous on T(Σ′°). So for every non-peripheral closed curve β ⊂ Σ′, ℓ_β(W′) = lim ℓ_β(Y_k) ≤ lim ℓ_β(X_k) = ℓ_β(W), by Lemma S and (GC1). Peripheral curves are cusps on both surfaces. By Thurston's theorem (Th), applied to the identity marking W → W′ (all closed geodesics of W are non-peripheral, and lengths do not increase), the identity is homotopic to an isometry, i.e. W′ = W in T(Σ′°).
4. Every subsequence has a further subsequence converging to W, so Y_k → W. The map T(Σ′°) → M(Σ′°) is continuous. ∎

### Proof of (d)
The quotient map U → U/Tw = B is open. Fix w′ ∈ U over p and a neighbourhood basis O_1 ⊃ O_2 ⊃ … of w′ in U. For each j, p_U(O_j) is a neighbourhood of p, so for k ≥ k_j there is τ ∈ Tw with τw_k ∈ O_j. Choosing τ_k accordingly gives τ_kw_k → w′ in T̄_g.
- The node curves of w′ are the α_e with s_e(p) = 0. Since p ∈ L_y, all boundary curves of Σ_y are nodes of w′, and no α_e lies in int Σ_y (Σ_y is a component of S ∖ ∪_e α_e). So Σ_y is a vertex subsurface of w′, and by (CD) its component is F_y(p): [W_{Σ_y}(w′)] = [F_y(p)].
- τ_k is a product of twists about the α_e, which are disjoint from int Σ_y. By (a), ψ_{Σ_y,P_k}(w_k) = ψ_{Σ_y,P_k}(τ_kw_k).
- By (c), applied to τ_kw_k → w′ and the pants decompositions P_k, [ψ_{Σ_y,P_k}(τ_kw_k)] → [F_y(p)]. ∎

*Remark (what is not claimed).* For a fixed point X, ψ_{Σ′,P′}(X) depends on P′; only limits at vertex subsurfaces are intrinsic. Convergence when node curves of z̃ lie inside Σ′ (and cross P′) is neither proved nor used: every use is at a vertex subsurface, which is guaranteed in §5 by (b0) and Lemma TI(2), and in Lemma L.1 by the pattern S.


## I.7 Cited classical facts (Part I) (all cited from memory; stated in the form used)

- **(Pl) Plumbing / Kuranishi charts** (Masur 1976; Bers; Wolpert). Near P ∈ Δ_G there is an orbifold chart Def(P)/Aut(P) of M̄_g with coordinates (z,(t_e)) as described in §1. The component deformations come from smooth Beltrami differentials supported in fixed compacts K_w, so that h_z → id in C^∞ on compacts. Plumbing z_ew_e = t_e is done in fixed coordinate discs. The fibres carry a labelling of components by V(G). Openness of versality: near any of its points p, Def(P) is a Kuranishi chart for the fibre over p.
- **(Dual) Teichmüller duality** (Teichmüller, Hamilton, Krushkal, Royden). For a tangent vector v at X ∈ T_{g,n} represented by μ: ‖v‖_T = sup{Re∫μφ : φ ∈ Q(X), ‖φ‖_1 = 1}. The supremum is attained at a unique norming φ = q_v, the extremal Beltrami differential is ‖v‖ q̄_v/|q_v|, and the Teichmüller disc tangent to v is the one generated by q_v.
- **(Bun)** For a plumbing family, π_*(ω^{⊗2}) is locally free of rank 3g−3. Its fibre at a stable curve consists of differentials on the components with at most double poles at node branches and equal quadratic residues a_e on the two branches. The a_e(φ) = (2πi)^{-1}∮_{|z_e|=r_0} z_eφ/dz_e are holomorphic and linearly independent at P, with common kernel ⊕_w Q(Y_w).
- **(GC1)–(GC3) Augmented Teichmüller space** (Abikoff; Bers; Fenchel–Nielsen).
  - (GC1) If (X_n,f_n) → P̃ in the γ-stratum, then ℓ(γ_e) → 0, and suitably conjugated holonomies restricted to Γ_w converge to type-preserving holonomies of P̃_w, with ℓ_{X_n}(c) → ℓ_{P̃_w}(c) for non-peripheral c ⊂ Σ_w.
  - (GC2) Conversely, if ℓ(γ_e) → 0 and conjugates of ρ_n|_{Γ_w} converge to discrete faithful type-preserving R_w with finite-area quotient, then (X_n,f_n) converges to the γ-stratum point with components H/R_w.
  - (GC3) If X_n → P in M̄_g, then after a subsequence there are markings with (X_n,f_n) convergent in T̄ to a lift of P.
- **(CD) Canonical chart description** (Abikoff, Bers, Hubbard–Koch, Wolpert): as stated in §0.4. Also: hyperbolic metrics of plumbing fibres vary continuously off the collars, and ℓ(α_e) → 0 (equivalently Ext(α_e) → 0) iff s_e → 0, uniformly on compact parts of the chart.
- **(Thin)** (collar lemma; Abikoff topology). If X_k → z̃ in T̄_g and ℓ_1 is less than half the systole of every component of z̃, then for large k the curves of hyperbolic length < ℓ_1 on X_k are exactly the node curves of z̃ (in the marking), and their lengths tend to 0.
- **(FN) Fenchel–Nielsen coordinates** (Fenchel–Nielsen; Wolpert for analyticity). For a pants decomposition P of S (with seams), the coordinates (ℓ_α, τ_α)_{α∈P} give a real-analytic diffeomorphism T_g → (ℝ_{>0}×ℝ)^P. For a finite-type surface F° with cusps and a pants decomposition P of F, c ↦ Φ_P(0,c) (gluing of hexagons with ideal vertices, §I.6A) is a homeomorphism (ℝ_{>0}×ℝ)^P → T(F°). The coordinates of α ∈ P depend only on the (one or two) pants adjacent to α.
- **(Hex) Hyperbolic plane geometry.** Nearest-point projection onto a closed convex subset of ℍ² is 1-Lipschitz. The fibres of nearest-point projection onto a geodesic line L are the geodesics perpendicular to L; so its restriction to a geodesic disjoint from L and not perpendicular to it is injective and continuous, hence monotone. In a right-angled hexagon with alternate sides a, x, y, the side opposite to a has cosh s = (cosh a + cosh x cosh y)/(sinh x sinh y); this stays valid for a = 0 (ideal vertex).
- **(Coll) Collar lemma.** If α is a simple closed geodesic of length ℓ and β a closed geodesic, then ℓ_β ≥ i(α,β)·2 arcsinh(1/sinh(ℓ/2)).
- **(Mum) Mumford compactness.** For a finite-type F° and ε > 0, {[Y] ∈ M(F°) : sys(Y) ≥ ε} is compact.
- **(Prop) Properness of filling length functions** (Kerckhoff, *The Nielsen realization problem*, 1983, Lemma 3.1, and its standard extension to finite-area surfaces with cusps). If β_1, …, β_p fill F° (every essential non-peripheral simple closed curve meets some β_j essentially), then {Y ∈ T(F°) : ℓ_{β_j}(Y) ≤ C ∀j} is compact. *Sketch:* by (Coll) the systole is ≥ ε(C) > 0 on this set; by (Mum) there are mapping classes φ_k with φ_kY_k in a fixed compact set K; by Wolpert's inequality ℓ_c(Y′) ≤ e^{2d_T(Y,Y′)}ℓ_c(Y) only finitely many curves have length ≤ C somewhere on K, so the φ_k(β_j) range over a finite set; the subgroup of the pure mapping class group fixing every β_j is finite (Alexander method), so the φ_k range over a finite set, and the Y_k lie in finitely many translates of K.
- **(Th) Thurston's stretch-map rigidity** (Thurston, "Minimal stretch maps between hyperbolic surfaces", 1986 preprint, cited from memory; the same fact is (Th) of Part II §10). Let X, Y be complete hyperbolic surfaces of finite area and ψ : Y → X a homeomorphism (cusps to cusps). If ℓ_X(ψ(c)) ≤ ℓ_Y(c) for every closed geodesic c of Y, then ψ is homotopic to an isometry. *(Scope caveat: rigidity is certainly in Thurston's paper for closed surfaces; that it covers complete finite-area surfaces with cusps is believed but cited from memory. An alternative route for the cusped case: length-spectrum domination gives a 1-Lipschitz map in the homotopy class (Thurston's best-Lipschitz-constant theorem), and equal hyperbolic areas force it to be an isometry.)*
- **(Ext) Maskit's comparison.** ℓ_X(γ)/π ≤ Ext_X(γ) ≤ (ℓ_X(γ)/2)e^{ℓ_X(γ)/2}.
- **Kerckhoff's formula.** d_T(X,Y) = ½ log sup_γ Ext_Y(γ)/Ext_X(γ), the supremum over simple closed curves γ. In particular Ext_Y(γ) ≤ e^{2d_T(X,Y)}Ext_X(γ), and Ext is K-quasi-invariant.
- **(QC1)** (Lehto–Virtanen II.5). Normalised K-qc maps of Ĉ form a sequentially compact family with K-qc limits. K-qc embeddings of a domain omitting two values form a normal family whose limits are constant or K-qc embeddings.
- **(QC2)** (Lehto–Virtanen V.5.3; Ahlfors V). If μ_n → μ a.e. with ‖μ_n‖_∞ ≤ k < 1, then the normalised solutions w^{μ_n} → w^μ uniformly on Ĉ.
- **(QC3)** A qc map with μ = 0 a.e. is conformal (Weyl). If μ_f = μ_h a.e., then f∘h^{-1} is conformal.
- **Royden's theorem.** The Kobayashi metric of T_{g,n} equals the Teichmüller metric. Hence a Teichmüller disc is a holomorphic isometric embedding of (H, d_H), and holomorphic maps are contractions.
- **Bers embedding.** T_{g,n} is biholomorphic to a bounded domain in C^{3g−3+n}.
- **Masur.** Cylinder directions of a finite-area quadratic differential are dense in RP¹. The q-geodesic representative of a curve realises its intersection numbers with the horizontal and vertical measured foliations.
- **Veech.** The Veech group of a Teichmüller curve is a non-cocompact lattice. A cylinder direction of a lattice surface is parabolic (Veech dichotomy), so Teichmüller curves are never compact.
- **Selberg's lemma.** A finitely generated linear group has a torsion-free normal subgroup of finite index.
- **Chow; Remmert.** Closed analytic subsets of projective varieties are algebraic. The image of an irreducible analytic set under a proper (finite) holomorphic map is an irreducible analytic set.
- **Krull / active lemma.** If S is a pure 2-dimensional analytic set and f is holomorphic and not identically 0 on any local component at a zero z, then {f = 0} ∩ S is pure 1-dimensional at z.
- **Milnor conic structure.** For an analytic germ (X,0) and small round balls B_ε, X ∩ B_ε is homeomorphic to the cone over its link. The irreducible components of X ∩ B_ε represent the germ components, and the branches of a curve germ meet only at 0 in B_ε.
- **Cartan.** For a properly discontinuous action of a countable group by biholomorphisms, T/Γ is a normal complex space. Near a point with stabiliser A there is an A-invariant ball with linear action, precisely invariant, and B/A → T/Γ is an open embedding. Invariant polynomials of a finite group separate orbits.
- **Normalisation.** The normalisation of an irreducible germ is an irreducible normal germ (one point over 0). A holomorphic map from a normal (for example 1-dimensional smooth) space whose image is not contained in the non-normal locus lifts uniquely to the normalisation. Normal surfaces have isolated singularities.
- **(Res)** (resolution of normal surface germs; Zariski's main theorem). There is a resolution π: W̃ → W, biholomorphic off ŝ_0, with compact connected exceptional curve Exc = ∪E_k. (Str): the strict transform of an irreducible curve germ meets Exc in exactly one point.
- **(Neg)** (Du Val, Mumford, Grauert). The intersection matrix (E_k·E_j) is negative definite.
- **(RA)** (Grauert; Cartan's Theorem A). A line bundle of positive degree on every E_k becomes, after shrinking W and passing to a power, globally generated on W̃.
- **Strict Schwarz–Pick.** A proper simply connected subdomain Ω ⊊ H has hyperbolic metric strictly larger than that of H at every point.
- **Elementary analysis:** Montel, Riemann extension, the identity theorem, the maximum principle, Baire, and Gauss–Bonnet for flat surfaces with conical singularities.

## I.8 Gaps and open points of Part I

1. **Former GAP 1 (fact (Ψ)) — now resolved, modulo classical citations.** Lemma TI, Steps 0 and 4 and Lemma L.1 use the properties of the subsurface restriction map ψ. These are now Proposition Ψ (§I.6A), proved in full from the classical facts (FN), (Hex), (Coll), (Mum), (Prop), (GC1), (CD) and Thurston's rigidity theorem (Th).
   - The key new ingredient is the shrinking lemma (Lemma S): setting boundary lengths to 0 at fixed interior FN coordinates does not lengthen any closed geodesic. It is proved by explicit 1-Lipschitz maps of right-angled hexagons.
   - Convergence at a vertex subsurface (Proposition Ψ(c)) is proved uniformly in the pants decomposition, by Lemma S, properness and (Th). This uniformity is genuinely needed: the earlier formulation, with one fixed pants decomposition, did not literally cover Lemma TI(3), §5.8 or Lemma L.1 Step 2, where the subsurface is transported by mapping classes that vary along the sequence. Those three places now invoke Ψ(c)/(d) explicitly.
   - Not proved and not used: convergence when node curves of the limit lie inside the subsurface.
   - (Th) and (Prop) are cited from memory. (Th) was already used in Part II (Lemma 4.3).

   With this, the marking identification along travel intervals is proved in Lemma TI and §5.7 (and completed in the labelled form needed later by Lemma L.1 of the Bridge section).
2. **(Thin), (CD).** These are cited in the form stated. The uniformity statements derived from them (the gap property (a′), the o(1) terms of Lemma TI) are proved here by compactness and contradiction.
3. **Orbifold structure in Theorem TV(3).** Whether the H/Λ_E orbifold structure on Ê^ν agrees with the structure inherited from Δ̂_G at points over orbifold points of C is open. It is not used.
4. **No common witnessing sequence.** The witnessing sequences for different transitions of one chain come from different subsequences (§5.10). A single common subsequence is not established, and Part I does not need it.
5. **Reading (R0) at orbifold points.** If V_0 lies in the orbifold locus of M_g, "tangent vector of V_0 at X_n" and "total geodesy" are read on q^{-1}(V_0) at regular points of the relevant sheet. This is how they are used in Lemma PA (with X̃_n ∈ Reg S, §4.3 Step 2) and in Lemma S̃′. This is a reading, stated explicitly, and not a gap in the proofs.

---

# Bridge — putting Part I and Appendix A into the forms used by Parts II and III

This section uses the notation of Part I §5 (the walk chain) and of the Kuranishi-chart conventions of Part I §0.3. For a lift λ̃ at a point J of the chain, S(λ̃) is its pattern (the set of edges e with s_e ≡ 0 on λ̃). G_S is G_J with the edges outside S contracted, and Π_S is the partial normalisation map (fact (PN) of Part II §1.4).

## Lemma L.1 (labelled lifts along the walk chain)

**Setting.** Consider the chain of Part I Proposition K_w, built from a walk n ≥ N. Here N is chosen as in Part I §5.10, and enlarged if necessary so that N ≥ n_2, where n_2 is given in Step 2 below and depends only on the data (r, δ, η) of Part I §5.3. For m = 1, …, k:
- I_m is the travel interval along the piece D^m, with stratum graph G^m;
- A_m is its constant short multicurve (Part I Lemma TI(1));
- θ_m : G_{A_m} → G^m is the identification of Part I Lemma TI(3), compatible with special-point labels;
- K̂^m is the compact component of ξ^{-1}(K_{D^m}) near which Λ(I_m) stays (Lemma TI(3));
- Ê^m is the lifted piece containing K̂^m;
- c_m := c_{I_m} is the vertex given by Lemma TI(2), (4). It is constant on Ê^m with labelled value Y_0, and c_1 = i (Part I Proposition K_w(1)).

Let (J, λ̃, y, I_m) be one of the following triples of a point, a lift and a chart label, together with the travel interval adjacent to the excursion at J on the side of λ̃:
- (J_m, β̃_m, x_m, I_m), for 1 ≤ m ≤ k−1 (entering lift);
- (Q_0, β̃, x, I_k) (entering lift at the endpoint);
- (J_{m−1}, β̃′_{m−1}, x_{m−1}, I_m), for 2 ≤ m ≤ k (leaving lift).

Put S := S(λ̃).

**Statement.** y is intact for S, and there is a graph isomorphism ι : G_S → G^m with ι({y}) = c_m and

  ι∘Π_S((λ̃ ∩ B̃(J,3r)) ∖ {0}) ⊂ Ê^m

(Π_S followed by the relabelling induced by ι).

**Consequences.**
- Part II's input I.5, i.e. (K-a)–(K-c) with Definition 1.2 of Part II, holds with E^m := Ê^m. For the MERGE/MOV alternative in (K-c), see L.3(i) below.
- Part III's BB1-M holds with the same E^m, c_m, with ι_m the isomorphism for (J_m, β̃_m) and ι′_{m−1} the isomorphism for (J_{m−1}, β̃′_{m−1}).

*Proof.*

**Step 1 (the identification).** Let s* ∈ I_m be the time at which the walk enters (for an entering lift), respectively leaves (for a leaving lift), the excursion at J. It is a travel time.
- Part I §5.7 ("Entry", and "Persistence and exit" for leaving lifts) shows the following, in the marking of the chart neighbourhood U_J, which is the path marking because the excursion path lies in U_J:
  - the constant short multicurve A_m equals {α_e : e ∈ S} as a set of curves on the reference surface;
  - y is intact for S (all edges at y are pinched along λ̃);
  - Σ_i = Σ_y as marked subsurfaces.
- The vertices of G_S are the classes w of vertices of G_J under the edges outside S. The subsurface Σ_w — the union of the Σ_u, u ∈ w, glued along the collars of the α_f with f ∉ S — is a component of S ∖ ∪_{e∈S} α_e = S ∖ A_m. The half-edges of G_S are the two sides of the curves α_e, e ∈ S.
- This gives a canonical isomorphism κ : G_S → G_{A_m}. Put ι := θ_m∘κ.
- Since Σ_y = Σ_i is the vertex subsurface labelled c_{I_m} (Lemma TI(2)), we get ι({y}) = θ_m(Σ_i) = c_m.

**Step 2 (one point of λ̃ lands in K̂^m).** Part I §5.7 provides a point z ∈ K_{D^m} within ρ_n of γ_n(s*), and its lift z̃ ∈ (λ̃ ∩ B̃(J,3r)) ∖ {0} within o(1) of the canonical chart point γ̃_n(s*).

*Claim.* There is n_2 such that for n ≥ n_2, at every such entry or exit event, the distance in ∏_w M̄_w between ι∘Π_S(z̃) and Λ(s*) is less than ρ̂ (ρ̂ as in Part I §5.3(b2)).

*Proof of the claim, by contradiction and compactness.*
- Suppose there are n_k → ∞ and events with distance ≥ ρ̂.
- There are finitely many points J ∈ Σ, finitely many lifts up to Aut(J) (the canonical lift is determined up to one global element of Aut(J)), and finitely many bijections V(G_S) → V(G^m). Pass to a subsequence with fixed J, λ̃, S, D^m and ι.
- The points z^{(k)} lie outside B(J, r/2), since K_{D^m} avoids these balls. So a subsequence z̃^{(k)} → z̃* ∈ (λ̃ ∩ closure B̃(J,3r)) ∖ {0}. Hence γ̃_{n_k}(s*_k) → z̃* as well.
- By (CD) (Part I §0.4), U_J/Tw ≅ B_J, and the quotient map by a group action is open. So there are τ_k ∈ Tw with τ_k γ̂_{n_k}(s*_k) → ẑ, a point of U_J over z̃*.
- The node curves of ẑ are the α_e with e ∈ S, because z̃* has pattern exactly S. Each Σ_w (w ∈ V(G_S)) has its boundary among them.
- Let P_w be the pants decomposition of Σ_w used in Λ. The twists τ_k are about the curves α_e of J; those with e ∈ S are boundary curves of Σ_w, but those with e ∉ S lie inside Σ_w. So τ_k maps Σ_w to itself (fixing its boundary curves, hence the puncture labels) but may move P_w. By Proposition Ψ(a),
  [ψ_{Σ_w,P_w}(γ̂_{n_k}(s*_k))] = [ψ_{Σ_w,τ_kP_w}(τ_kγ̂_{n_k}(s*_k))].
  Σ_w is a vertex subsurface of ẑ (its node curves are exactly the α_e, e ∈ S). By Proposition Ψ(c), which is uniform in the pants decompositions τ_kP_w, the right-hand side converges to [Σ_w-side of ẑ] = Π_S(z̃*)_w, with labelled special points. (The earlier version of this step treated the τ_k as acting trivially on the fixed-P_w restriction, which is not literally true for twists inside Σ_w; the uniform statement Ψ(c) repairs this.) The last equality is the description of the fibre over z̃* in the marked chart: its Σ_w-part is the w-component of the partial normalisation at the S-nodes.
- So Λ(s*_k) → ι∘Π_S(z̃*). Also ι∘Π_S(z̃^{(k)}) → ι∘Π_S(z̃*), by continuity of Π_S on L_S. This contradicts the distance bound ≥ ρ̂.

*Conclusion of Step 2.*
- Since z̃ has pattern exactly S, (PN1) gives ξ_{G^m}(ι∘Π_S(z̃)) = q(z̃) = z ∈ K_{D^m}. So ι∘Π_S(z̃) ∈ ξ^{-1}(K_{D^m}), the disjoint union of the compact sets K̂_{D^m}^l, which are at mutual distance ≥ 4ρ̂.
- Λ(s*) lies within o(1) < ρ̂ of K̂^m (Lemma TI(3)), and ι∘Π_S(z̃) lies within ρ̂ of Λ(s*).
- Hence ι∘Π_S(z̃) lies within 2ρ̂ of K̂^m, so ι∘Π_S(z̃) ∈ K̂^m ⊂ Ê^m.

**Step 3 (the whole lift).**
- Put λ := q(λ̃), a branch of closure(D^m) at J. By the choice of r (Part I §5.3), λ ∖ J lies in one stratum and in B(J,3r) ∖ {J}, which contains no point of Σ.
- Points of closure(D^m) ∖ D^m are punctures, which lie in Σ. So λ ∖ J ⊂ D^m ∖ R(D^m).
- Off R(D^m), ξ^{-1}(D^m) is locally a disjoint union of smooth arcs, each mapped homeomorphically onto a neighbourhood in D^m. Each arc is an irreducible germ inside Â, so it lies in a single lifted piece. Hence a point of ξ^{-1}(λ ∖ J) lying in Ê^m has its whole arc in Ê^m, because Ê^m has pure dimension 1.
- So (ξ^{-1}(λ ∖ J)) ∩ Ê^m is open in ξ^{-1}(λ ∖ J). It is also closed there, since Ê^m is closed in ∏_w M_w.
- (λ̃ ∩ B̃(J,3r)) ∖ {0} is connected: λ̃ ∩ B̃ is irreducible with a disc as normalisation. Its image under ι∘Π_S is a connected subset of ξ^{-1}(λ ∖ J), by (PN1). By Step 2 it meets Ê^m.
- Hence the image lies in Ê^m. ∎

## Lemma L.2 (transport families are analytic: BB6 of Part III)

**Statement.** Let Q ∈ B_0 with chart q : B → q(B), and let c be a branch of B_0 at Q with c ∖ Q ⊂ Δ_G. Let c̃ be a lift, and let N_c, Ñ = Ñ_c̃ and ε be as in Part III §0.7. Then, after shrinking B and ε, closure(Ñ) is a closed analytic subset of B × Δ_ε of pure dimension 2. This is true whether or not Q ∈ Δ_G.

*Proof.*
1. **Analytic sets.**
   - 𝒜 := closure(𝒱) ∩ (closure(Δ_G) × Δ) and 𝒵 := closure(𝒱) ∩ ((closure(Δ_G) ∖ Δ_G) × Δ) are closed analytic, by (R1); closure(Δ_G) and closure(Δ_G) ∖ Δ_G are closed algebraic.
   - Put X := (q × id)^{-1}(𝒜) ∩ (B × Δ_ε) and Z_1 := (q × id)^{-1}(𝒵) ∩ (B × Δ_ε). Both are closed analytic.
2. **Localisation.**
   - Let c = c_1, …, c_r be the branches of B_0 at Q, represented by closed discs that meet only at Q, each c_k ∖ Q lying in one stratum.
   - H^{-1} is continuous and H^{-1}(Q,0) = (Q,0), and H preserves strata. So after shrinking B and ε, every point of closure(𝒱) ∩ (Δ_G × Δ) ∩ (q(B) × Δ_ε) has the form H(z,t) with z ∈ c_k° ∖ Q for some k with c_k ∖ Q ⊂ Δ_G, or with z = Q (the latter only if Q ∈ Δ_G).
   - Put Γ_Q := H({Q} × Δ_ε), Λ := (q × id)^{-1}(Γ_Q) ∩ (B × Δ_ε) and Z := Z_1 ∪ Λ. Then
     X ∖ Z = (q × id)^{-1}(⊔_{k : c_k∖Q ⊂ Δ_G} N_{c_k}) ∩ (B × Δ_ε).
   - Each N_{c_k} is open in this disjoint union, because H is a homeomorphism and c_k° ∖ Q is open in closure(V_0) ∩ Δ_G near Q. So (q × id)^{-1}(N_c) is open and closed in X ∖ Z.
   - Ñ is a connected component of (q × id)^{-1}(N_c), hence a connected component of X ∖ Z.
3. **Dimension of Λ.** Γ_Q is homeomorphic to Δ_ε via t, so it has covering dimension 2. The map q × id : Λ → Γ_Q is closed (q × id is proper on B × Δ_ε, being the quotient by a finite group, and Λ is closed) with finite, hence 0-dimensional, fibres. By Hurewicz's theorem on closed maps of separable metric spaces (dim X ≤ dim Y + sup_y dim f^{-1}(y)), Λ has covering dimension ≤ 2 + 0 = 2. (Only this direction of Hurewicz's theorems is used. The reverse inequality dim f(X) ≤ dim X is false in general for closed finite-to-one maps, and is not used.)
4. **Components of X.** Let X_l be the irreducible components of X, a locally finite family.
   - (a) **X_l ⊄ Z and dim X_l = 2.** Then X_l ⊄ Z_1, so X_l° := X_l ∖ (Sing X ∪ ⋃_{l′≠l} X_{l′} ∪ Z_1) is a connected 4-manifold, dense in X_l (fact (Reg)). Removing the closed set Λ ∩ X_l°, of covering dimension ≤ 2, leaves it connected and dense (Hurewicz–Wallman, (HW)). X_l ∖ Z lies between X_l° ∖ Λ and its closure, so X_l ∖ Z is connected and dense in X_l.
   - (b) **X_l ⊄ Z and dim X_l ≤ 1 is impossible.**
     - X_l ∖ Z is a non-empty open subset of X_l, so it contains a point x on no other component. Near x, X = X_l.
     - Let U be an open neighbourhood of x in B × Δ_ε with X ∩ U = X_l ∩ U ⊂ X ∖ Z. Then X ∩ U is open in X ∖ Z, and X ∖ Z = (q × id)^{-1}(⊔N_{c_k}) ∩ (B × Δ_ε) is saturated for the Aut(Q)-action. The restriction of a finite-group quotient map to a saturated set is open onto its image. So (q × id)(X ∩ U) is a non-empty open subset of the topological 4-manifold ⊔N_{c_k} (more precisely of its part inside q(B) × Δ_ε), and therefore has covering dimension 4.
     - On the other hand, q × id : B × Δ_ε → q(B) × Δ_ε is a finite holomorphic map, and X_l is a closed analytic subset of B × Δ_ε of dimension ≤ 1. By Remmert's finite mapping theorem, (q × id)(X_l) is a closed analytic subset of q(B) × Δ_ε of the same dimension ≤ 1, hence of covering dimension ≤ 2 (HW). It contains (q × id)(X ∩ U), of covering dimension 4. Covering dimension is monotone on subsets of separable metric spaces (HW), so this is a contradiction.
5. **Conclusion.**
   - By 4, X ∖ Z = ⋃_{X_l ⊄ Z} (X_l ∖ Z), each X_l ∖ Z is connected, and each such X_l has dimension 2.
   - The component Ñ is therefore a union of some of the sets X_l ∖ Z, and closure(Ñ) is the union of the corresponding X_l.
   - This is a locally finite union of 2-dimensional irreducible analytic sets, so it is analytic of pure dimension 2. ∎

## Lemma L.3 (the remaining inputs)

**(i) Part II's inputs I.2, I.3, I.6 and the endpoint alternative.**
- I.2 is Part I Theorem TV, items 1–3, valid for every lifted piece in every boundary stratum.
- I.3 consists of Part I Lemmas CL and J0, with Part I Supplement R3′ for non-product strata.
- I.6 is Part I Corollary IMOV_all(b).
- **The endpoint alternative in (K-c).**
  - MERGE in Part I Proposition K_w(4) says that some edge at x is unpinched along b̃, i.e. x is not intact for S_b̃.
  - MOV in K_w(4) says that x is intact on b̃, F_x(0) = Y_0, and [F_x(z̃^∞)] ≠ [Y_0] at a point z̃^∞ ∈ b̃ ∖ 0. So [comp_x] is non-constant along b̃.

**(ii) Part III's inputs.**
- **BB1:** Part I Proposition K_w, together with Corollary IMOV_all.
  - BB1 says: if J_m lies in the stratum of D^m or of D^{m+1}, then β̃′_m = β̃_m. This is IMOV_all(a).
  - BB1 says: if J_m lies in neither stratum, it is a puncture of both. Indeed, D^m is closed in its stratum and J_m ∈ closure(D^m), so J_m ∈ closure(D^m) ∖ D^m; likewise for D^{m+1}.
  - The endpoint statements of BB1 are IMOV_all(b) and K_w(4).
  - BB1-M is Lemma L.1.
- **BB2:** Proposition U.1.
- **BB6:** Lemma L.2.
- **BB3.** Apply Part II Appendix A, Lemmas A.5 and A.6, to the restricted family over Δ_*, rescaled to the unit disc. It satisfies (R1), (R2) and (Rig) whenever the original family does. This gives:
  - 𝒲_G (the closure of Â over Δ_*, as in Part III §0.4; it is A.5's 𝓦_G) is closed analytic and proper over Δ_*;
  - for every 2-dimensional component W, every fibre W_t is non-empty and is a finite union of curves D = K_W × {c_D}, with (U1).

  The remaining items of BB3 follow from these.
  - **F_W is finite.** K_W is an irreducible compact curve not contained in the boundary, so F_W = K_W ∩ ∂ is finite.
  - **Γ_{W,u} for u ∉ M_W.** Every point of W lies on a component K_W × {c_D} of its fibre. So pr_u(W) ⊂ M_u, and the fibre of (pr_u, t)(W) over t is the finite set {c_D[u]}. By Remmert's theorem, (pr_u, t)(W) is an irreducible closed analytic subset of M̄_u × Δ_*, contained in M_u × Δ_*, with finite fibres over Δ_*. It is therefore an irreducible curve finite over Δ_*. ∎


---

# Part II — Theorem A: the claim under the embedded orbifold reading

**What this Part proves.** Theorem A (§9): under (R1) and (R2^orb) — equivalently, by Theorem 7.2, (R1), (R2) and (Loc); equivalently, by Theorem 7.5, (R1), (R2) and (AP) (the trivialisation preserves the order of the automorphism group of every boundary point) — we have Y_t = Y_0 for all t. Inputs:
- the Part I results, in the forms I.2, I.3, I.5, I.6 stated in §1.6. These forms are derived from Part I in the Bridge section (Lemma L.1);
- classical facts, listed in §II.10.

The finiteness of holomorphic maps into the level covers M_u[N] (formerly the cited fact (IS), GAP G1) is now proved: Lemma F0 (genus 0) and Lemma F1 (genus ≥ 1, by reduction to the closed-fibre Imayoshi–Shiga theorem via a characteristic branched covering), both in §10. It is used only once, at the endpoint (§9.3).

**Labels.** Lemmas are labelled by the hypotheses they use:
- [coarse] uses at most (R1) and (R2);
- [coarse+Rig] uses in addition (Rig);
- [orb] uses (R2^orb), with the items (a)–(d) used listed;
- [none] uses no hypothesis on the family.

**Route.** Under (R2^orb) two facts hold:
- at every boundary point Q, the lift locus of the transported point Q_t is a single Aut(Q)-fixed point p(t) (Prop. 5.2);
- the descended transport Π_t carries constant vertex values along pieces (Theorem 4.4(a) and Prop. 6.2).

So the value of the tracked Y_0-copy at p(t) can be read from both sides of every transition of the walk chain. The chain becomes a chain of equalities [φ_{c_m}(t)] = [φ_{c_{m+1}}(t)] (§9).

**Appendix A.** Appendix A proves the coarse-valid lemmas under the weakest hypotheses their proofs allow. It is not used for Theorem A. Its Lemmas A.5 and A.6 are used in Part III, through Lemma L.3.

## II.1. Conventions, readings, and the Part I input

### 1.1 Stable graphs, strata, Teichmüller spaces

**C1 (stable graphs).**
- A stable graph G of genus g consists of:
  - a vertex set V(G) with genera g_w;
  - a set H(G) of half-edges with an attaching map to V(G);
  - a fixed-point-free involution on H(G), whose orbits are the edges E(G).
- n_w denotes the number of half-edges at w. Stability means 2g_w − 2 + n_w > 0.
- Aut(G) is the group of pairs of bijections of V(G) and H(G) that respect attachment, the involution and the genera. **Such an automorphism may exchange the two half-edges of an edge.**
- Contraction: for a subset U ⊂ E(G), G/U is the graph obtained by contracting the edges of U. Its vertices are the connected subgraphs spanned by U; for y ∈ V(G), [y] denotes the vertex of G/U containing y.

**C2 (strata).**
- For a stable graph G, Δ_G ⊂ M̄_g is the locally closed algebraic subset of stable curves whose dual graph is isomorphic to G.
- It is a boundary stratum iff E(G) ≠ ∅.
- closure(Δ_G) ∖ Δ_G is a union of strata Δ_{G′} with G ≅ G′/U for some U ≠ ∅ ("deeper" strata), and it is closed.

**C3 (vertex moduli and Teichmüller spaces).**
- For each w ∈ V(G), fix a reference surface Σ_w of genus g_w with n_w distinct points labelled by the half-edges at w.
- M_w denotes the moduli space of genus-g_w curves with n_w distinct points labelled by these half-edges, M̄_w its Deligne–Mumford compactification, and ∂M̄_w := M̄_w ∖ M_w.
- T_w is the Teichmüller space of (Σ_w, labelled points), and Mod_w the pure mapping class group (isotopy classes of orientation-preserving homeomorphisms of Σ_w fixing each labelled point).
- T_G := ∏_w T_w, Mod_Π := ∏_w Mod_w, and p : T_G → ∏_w M_w = T_G/Mod_Π is the quotient map.
- pr_w denotes the w-th coordinate. For W ⊂ V(G), pr_W denotes the projection to ∏_{w∈W}.

**C4 (the stratum group Mod_G).**
- Mod_G is the group of pairs g = (σ, (φ_w)_w), where:
  - σ ∈ Aut(G);
  - φ_w is an isotopy class of orientation-preserving homeomorphisms Σ_w → Σ_{σ(w)} carrying the point labelled h to the point labelled σ(h).
- It acts on T_G by sending (C_w, f_w)_w to the point whose σ(w)-coordinate is C_w, with marking f_w∘φ_w^{-1} and with the point f_w(h) relabelled σ(h).
- ξ_G : ∏_w M_w → Δ_G is the gluing map: for every edge {h, h′}, glue the point labelled h to the point labelled h′.
- We use the following standard facts (St), cited at the end:
  - (St1) Mod_G acts properly discontinuously by biholomorphisms on T_G. Every point x̂ has a Stab(x̂)-invariant open neighbourhood U ("slice neighbourhood") with gU ∩ U ≠ ∅ ⇒ g ∈ Stab(x̂), and these form a neighbourhood basis.
  - (St2) ξ_G∘p : T_G → Δ_G is surjective, and its fibres are exactly the Mod_G-orbits.
  - (St3) Mod_Π is the kernel of Mod_G → Aut(G), (σ, φ) ↦ σ; this map is onto. So Aut(G) = Mod_G/Mod_Π acts on ∏_w M_w by permuting factors and relabelling points, and ξ_G is the quotient map by this finite group.
  - (St4) ξ_G is a finite (hence proper) morphism of quasi-projective varieties. It extends to the finite gluing morphism ξ̄_G : ∏_w M̄_w → closure(Δ_G).
- (Mod_G is the stack-theoretic stratum group: [T_G/Mod_G] = Δ_G as a substack of M̄_g. See Lemma 2.4 for its stabilisers.)

**C5 (time-t objects).** For a boundary stratum G and t ∈ Δ put:
- A_t = A^G_t := closure(V_t) ∩ Δ_G;
- Â_t := ξ_G^{-1}(A_t) ⊂ ∏_w M_w;
- Ã_t := p^{-1}(Â_t) ⊂ T_G, which is Mod_G-invariant;
- B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g.

A **piece** (at time t, in the stratum G) is a 1-dimensional irreducible component E of the analytic set Â_t. For a piece E:
- ν : Ê → E is its normalisation;
- M(E) := {w ∈ V(G) : pr_w|_E is non-constant} (the moving vertices);
- K(E) := closure of pr_{M(E)}(E) in ∏_{u∈M(E)} M̄_u;
- for a vertex c ∉ M(E), φ_c(E) ∈ M_c denotes the constant value of pr_c on E.

**C6 (classes).**
- For a type (h, m), 𝔐_{h,m} := M_{h,m}/S_m (unordered marked points), with finite quotient map Z ↦ [Z].
- Let C be a smooth irreducible component of a stable pointed curve. "C with its special points" means the normalisation of C, with the preimages of nodes and the marked points lying on C as an unordered set of special points. Its class is taken in the appropriate 𝔐.

### 1.2 The data of the problem

- V_0 ⊂ M_g is a smooth totally geodesic complex surface. 𝒱 ⊂ M_g × Δ is the family, V_t its fibres, and closures are taken in M̄_g, respectively M̄_g × Δ.
- Γ is the fixed stable graph. By the problem's assumption, Δ_Γ is of product type: ξ_Γ : ∏_{j} M_{g_j,n_j} → Δ_Γ is an isomorphism, and π_j = pr_j∘ξ_Γ^{-1}.
- ∂V_t := closure(V_t) ∩ Δ_Γ = A^Γ_t. It has dimension 1, and π_i(∂V_t) = {Y_t} with Y_t ∈ M_{g_i,n_i}.
- **Dimension of B_t (used tacitly).** Under (R1), B_t is a closed analytic subset of dimension ≤ 1.
  - Every irreducible component Z of the analytic set closure(V_t) contains points of V_t: the points of Z on no other component form a non-empty open subset of closure(V_t), and V_t is dense.
  - So Z meets the 2-dimensional manifold V_t in a non-empty open set, and dim Z = 2.
  - B_t = closure(V_t) ∩ ∂M̄_g is analytic and contains no open subset of any Z. Hence dim B_t ≤ 1.
  - (V_t is closed in M_g, so that B_t = closure(V_t) ∖ V_t: by (R2) applied to the open stratum M_g, closure(V_t) ∩ M_g = H_t(closure(V_0) ∩ M_g) = H_t(V_0) = V_t, V_0 being closed in M_g by our reading. Only A^G_t ⊂ closure(V_t) ∩ ∂M̄_g is used below in any case. V_t is a 2-dimensional embedded submanifold because 𝒱 is a submanifold and the family is smoothly trivial, which justifies the first item.)
  - Consequently every Â_t has dimension ≤ 1.

### 1.3 The readings

**(R1)** closure(𝒱) is a closed analytic subset of M̄_g × Δ, and its fibre over t is closure(V_t).

**(R2)** (coarse reading of the smooth triviality and of (i), (ii)). There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ (write H_t := H(·, t)) such that:
- H_0 = id;
- H is smooth on V_0 × Δ (never used below);
- for every stratum G, including the open one, H((closure(V_0) ∩ Δ_G) × Δ) = closure(𝒱) ∩ (Δ_G × Δ).

Consequently H_t(A^G_0) = A^G_t for all G, H_t(B_0) = B_t, and H_t(∂V_0) = ∂V_t.

*Standing-reading caveat.* (R1) and (R2) are themselves readings of the problem. In particular (R2) encodes (i) and (ii) by **one** stratum-preserving homeomorphism that trivialises all strata simultaneously. Everything below is conditional on them.

**(R2^orb)** (embedded orbifold reading). (R2) holds, and for every boundary stratum G there is a continuous map H̃ = H̃^G : Ã_0 × Δ → T_G (write H̃_t := H̃(·, t)) such that for all t ∈ Δ:
- (a) ξ_G∘p∘H̃_t = H_t∘ξ_G∘p on Ã_0;
- (b) H̃_t(g x) = g H̃_t(x) for all g ∈ Mod_G and x ∈ Ã_0;
- (c) Stab_{Mod_G}(H̃_t x) = Stab_{Mod_G}(x) for all x ∈ Ã_0;
- (d) H̃_0 = id.

**(Loc)** (chart-level local reading). For every boundary stratum G, every x̂ ∈ Ã_0 and every t_0 ∈ Δ there are:
- an open neighbourhood W of x̂ in T_G;
- an open disc I ∋ t_0;
- a continuous h : (W ∩ Ã_0) × I → T_G,

such that:
- (L1) ξ_G∘p∘h_s = H_s∘ξ_G∘p on W ∩ Ã_0, for s ∈ I;
- (L2) for each u ∈ W ∩ Ã_0, Stab_{Mod_G}(h_s(u)) does not depend on s ∈ I.

By Theorem 7.2, (R2) + (Loc) ⇔ (R2^orb). The direction ⇒ is the content of the theorem; ⇐ holds with h := H̃, by (a) and (c).

**The two orbifold readings.** "Regard M̄_g and its strata as orbifolds" admits two inequivalent precise forms.
- **(O-emb), embedded/substack reading.** A_t is the reduced closed substack of the stack Δ_G = [T_G/Mod_G]; its isotropy at z is the full Aut(z) (Lemma 2.4). The trivialisation is an isomorphism of substacks over Δ. That is, its local lifts are equivariant through isomorphisms of the **ambient** local groups Aut(z) → Aut(H_t z), these isomorphisms being locally constant in s (this constancy is part of the reading, not a consequence; see Remark 7.3).
  - (O-emb) gives (Loc) (Remark 7.3), hence (R2^orb) by Theorem 7.2. Conversely, (R2^orb) gives (O-emb) by definition.
  - So **(R2^orb) formalises (O-emb).**
- **(O-int), intrinsic reading.** Each A_t carries its own effective orbifold structure, and H_t is an orbifold diffeomorphism of these intrinsic structures. The local homomorphisms need not be onto, or injective, on the ambient groups.
  - (O-int) is strictly weaker: the chart-level model of §8.2 satisfies (O-int) but violates (c).
- Locally, **(R2^orb) ⇔ (O-emb) ⊊ (O-int) ⊆ (R2)**. Theorem A is proved under (O-emb) only. The wording of the problem ("smooth subvariety of M_g", "complex submanifold", "smoothly trivial") does not decide between these readings, and arguably leans towards the coarse one.

### 1.4 Kuranishi charts (classical facts, cited as (Kur), (K2), (PN); precise statements at the end)

Let J be a stable curve with dual graph G_J.
- **(Kur)** There is a universal deformation over a smooth germ Def(J), on which Aut(J) acts.
  - Part of the coordinates are smoothing parameters s_e, e ∈ E(G_J). The node e persists in the fibre X_p iff s_e(p) = 0.
  - The dual graph of X_p is canonically G_J/{e : s_e(p) ≠ 0}.
  - For a sufficiently small Aut(J)-invariant ball B ⊂ Def(J), the map q : B → M̄_g, p ↦ [X_p], induces an isomorphism of analytic spaces from B/Aut(J) onto an open set q(B). Moreover, for every p ∈ B, restriction gives an isomorphism Stab_{Aut(J)}(p) ≅ Aut(X_p).
  - In particular q^{-1}(q(p)) ∩ B = Aut(J)·p, and q^{-1}(J) ∩ B = {0}.
- **(K2)** For a vertex x of G_J, put L_x := {s_e = 0 for every edge e at x}. Over L_x ∩ B the fibres have a smooth component labelled x, whose special points are labelled by the half-edges at x. This gives a holomorphic map comp_x : L_x ∩ B → M_{g_x,n_x}.
- **(PN)** For S ⊂ E(G_J), put L_S := {s_e = 0 for all e ∈ S} and G_S := G_J/(E(G_J) ∖ S). Partial normalisation of the fibres along the nodes in S gives a holomorphic map Π_S : L_S ∩ B → ∏_{w∈V(G_S)} M̄_w with the following properties.
  - (PN1) If p has pattern exactly S, i.e. {e : s_e(p) = 0} = S, then Π_S(p) ∈ ∏_w M_w and ξ_{G_S}(Π_S(p)) = q(p).
  - (PN2) If p ∈ L_S lies in the deepest locus {s_e = 0 for all e}, then the w-coordinate of Π_S(p) is the stable curve glued from the comp_y(p), y ∈ w, along the edges of E(G_J) ∖ S inside w.
  - (PN3) If x is **intact** for S (every edge at x lies in S), then {x} is a vertex of G_S, and pr_{{x}}∘Π_S = comp_x on L_S ∩ B.
  - Given an isomorphism ι : G_S → G onto a reference graph, write Π_{S,ι} for Π_S followed by the induced relabelling ∏_{w∈V(G_S)} M̄_w → ∏_{w∈V(G)} M̄_w. Then (PN1) reads ξ_G∘Π_{S,ι} = q on the pattern-S locus.

### 1.5 Branches, lifts, patterns, labels

Let J ∈ B_0.
- **Branch.** A branch of B_0 at J is a local irreducible component β of the germ of B_0 at J. In a small neighbourhood:
  - β ∖ J is a punctured disc lying in a single stratum Δ_{G_β} (the strata meet β∖J in analytic subsets, one of which is open and dense; shrink);
  - distinct branches meet only at J.
- **(P).** We say **(P) holds for β** if J ∉ Δ_{G_β}, i.e. J is a puncture of the piece containing β∖J.
- **Lift.** A lift β̃ of β is an irreducible component at 0 of q^{-1}(β) in Def(J). For B small, β̃ ∩ B is irreducible and β̃ ∖ 0 is connected.

**Lemma 1.1 (patterns) [none].** For p ∈ B put S(p) := {e : s_e(p) = 0}. Then on q^{-1}(Δ_{G′}) ∩ B, for any stratum G′, S(·) is locally constant. Hence:
- every lift β̃ has a constant pattern S_β̃ on β̃ ∖ 0;
- G_{S_β̃} ≅ G_β.

*Proof.*
- Near p_0, s_e ≠ 0 for every e ∉ S(p_0), so S(p) ⊆ S(p_0).
- If q(p), q(p_0) ∈ Δ_{G′}, then |S(p)| = |E(G′)| = |S(p_0)|, because the number of nodes of X_p is |S(p)|.
- Hence S(p) = S(p_0). Since β̃ ∖ 0 is connected and lies in q^{-1}(Δ_{G_β}), the rest follows from (Kur). ∎

**Definition 1.2 (labelled lifts).** Let β̃ be a lift of a branch β at J, S := S_β̃, and x ∈ V(G_J). Let E be a piece at time 0 in the stratum G of β ∖ J, and c ∈ V(G). We say **(β̃, x) is labelled by (E, c)** if there is an isomorphism ι : G_S → G such that:
- x is intact for S and ι({x}) = c;
- Π_{S,ι}(β̃ ∖ 0) ⊂ E.

In that case, by (PN3), comp_x = ι^*(pr_c∘Π_{S,ι}) on L_S ∩ B, where ι^* is the relabelling of special points induced by ι on the half-edges at x. In particular [comp_x(p)] = [pr_c Π_{S,ι}(p)].

### 1.6 Part I input, in the precise forms used

The following are taken as given (proved in Part I). I.1, I.4 and Lemma PT are not used here.

**I.2 (Theorem TV, the part used).** Let G be a boundary stratum and E a piece of Â_0. Then there are a vertex j of G and a lattice Λ = Λ_E ⊂ PSL_2(ℝ) (of finite index in the Veech group Γ′ of a Teichmüller curve in M_j), such that Ê ≅ H/Λ as Riemann surfaces. We write u_0 : H → Ê for the quotient map.
- O_0 := H/Λ is regarded as a hyperbolic 2-orbifold. Its cone points c have orders e_c, its cusps are the punctures of Ê, and χ^orb(O_0) < 0.
- Ê is a compact Riemann surface minus finitely many points.

**I.3 (Lemmas CS, CL, J0).**
- **CL.** Let Γ be a countable group acting properly discontinuously by biholomorphisms on a complex manifold T, X := T/Γ with Cartan's quotient structure, and p : T → X the quotient map. Let Q be a connected Riemann surface, h : Q → X holomorphic, and L : Q → T continuous with p∘L = h. Then L is holomorphic.
- **J0** (valid in every boundary stratum, by Part I Supplement R3′). In the situation of I.2, there is a holomorphic F_0 : H → T_G with:
  - (i) p∘F_0 = ν∘u_0;
  - (ii) f_0 := pr_j∘F_0 : H → T_j is an isometric holomorphic embedding. Here H carries the Poincaré metric of curvature −4, T_j the Teichmüller metric, and the image is a Teichmüller disc;
  - (iii) for every λ ∈ Λ, the set R(λ) := {g ∈ Mod_Π : F_0∘λ = g∘F_0} is a coset gS of the finite group S := {s ∈ Mod_Π : s∘F_0 = F_0}. Moreover R(λ) ⊂ N(S), the normaliser, and R(λμ) = R(λ)R(μ).
  - Consequently λ ↦ R(λ) is a homomorphism Λ → N(S)/S.

**I.5 (Proposition K_w, walk chain; a statement about V_0 only; Part I §I.5 with Lemma L.1 of the Bridge section).** There are the following data.
- **(K-a) Pieces and constant vertices.** For m = 1, …, k: a boundary stratum G_m, a piece E^m of Â_0^{G_m}, and a vertex c_m ∉ M(E^m). Moreover G_1 = Γ, E^1 ⊂ Â_0^Γ = ∂V_0 (identified via ξ_Γ), and c_1 = i.
- **(K-b) Transitions.** For m = 1, …, k−1: a point J_m ∈ B_0, lifts β̃_m, β̃′_m at 0 ∈ Def(J_m) of branches of B_0 at J_m, and a vertex x_m of G_{J_m}, such that:
  - (β̃_m, x_m) is labelled by (E^m, c_m);
  - (β̃′_m, x_m) is labelled by (E^{m+1}, c_{m+1}).
- **(K-c) Endpoint.** A point Q_0 ∈ B_0, a lift β̃ at 0 ∈ Def(Q_0) and a vertex x of G_{Q_0} with (β̃, x) labelled by (E^k, c_k). Also a lift b̃ at 0 ∈ Def(Q_0) of a branch b of B_0 at Q_0 such that, with S_b := S_b̃, one of the following holds:
  - **MERGE:** x is not intact for S_b;
  - **MOV:** x is intact for S_b and [comp_x] is non-constant along b̃.

(This is the chain's "common chart label x_m" with the "marking identification x_m ↔ c ↔ x_{m+1}", made precise through Definition 1.2. The interior transitions coming from the finite sets R(D) are among the J_m. The requirement that both lifts at a transition lie in one irreducible component of q^{-1}(closure V_0) is part of I.5 but is not used here.)

**I.6 (Corollary IMOV_all, the part used).** In (K-c), (P) holds for b: Q_0 ∉ Δ_{G_b}.

---

## II.2. Preliminaries that use at most (R1), (R2)

**Lemma 2.1 (algebraicity and finite type) [coarse: (R1) only].** For every t ∈ Δ and every boundary stratum G:
1. Â_t is a closed algebraic subset of dimension ≤ 1 of the quasi-projective variety ∏_w M_w. It has finitely many pieces and finitely many isolated points, and its singular set Sing(Â_t) is finite.
2. For a piece E, the normalisation Ê is a compact Riemann surface minus finitely many points, and ν : Ê → E is finite (hence proper).
3. For a piece E, M(E) ≠ ∅. K(E) is an irreducible projective curve in ∏_{u∈M(E)} M̄_u, not contained in the boundary ∂ := ∏_{u∈M(E)} M̄_u ∖ ∏_{u∈M(E)} M_u. The set K(E) ∩ ∂ is finite.

*Proof.*
1. By (R1), closure(V_t) is a closed analytic subset of the projective variety M̄_g, hence algebraic (Chow).
   - Δ_G is locally closed algebraic, so A_t is locally closed algebraic. ξ_G is a morphism (St4), so Â_t is a closed algebraic subset of ∏_w M_w, of dimension ≤ 1 by §1.2.
   - The analytic irreducible components of an algebraic set are its algebraic irreducible components (fact (Irr)). There are finitely many of them.
   - The singular set of a ≤1-dimensional algebraic set is a closed algebraic subset of dimension 0, hence finite.
2. E is an irreducible quasi-projective curve. Its (analytic = algebraic) normalisation is a smooth irreducible quasi-projective curve, i.e. a compact Riemann surface minus finitely many points, and ν is finite.
3. **M(E) ≠ ∅**, since E is not a point.
   - The closure Ē of E in the projective variety ∏_w M̄_w is an irreducible projective curve.
   - pr_{M(E)}(Ē) is compact, contains pr_{M(E)}(E), and lies in its closure. So K(E) = pr_{M(E)}(Ē) is an irreducible projective curve. It is not a point, because each u ∈ M(E) is non-constant on E.
   - K(E) ⊄ ∂, because pr_{M(E)}(E) ⊂ ∏ M_u. So K(E) ∩ ∂ is a proper closed algebraic subset of an irreducible curve, hence finite. ∎

**Definition 2.1′ (finite set of a piece).** For a piece E put M := M(E). F′(E) is the set of classes (C6) of all smooth irreducible components, with their special points, of all coordinates κ_u (u ∈ M) of all points κ ∈ K(E) ∩ ∂. By Lemma 2.1(3) it is finite.

**Lemma 2.2 (ends of pieces) [none].** Let E be a piece, z_n ∈ E, and z_n → κ in ∏_w M̄_w.
1. If κ_w ∈ ∂M̄_w, then w ∈ M(E).
2. If some coordinate of κ lies in the boundary, then pr_{M(E)}(κ) ∈ K(E) ∩ ∂.

*Proof.*
1. If w ∉ M(E), then pr_w(z_n) = φ_w(E) ∈ M_w for all n, so κ_w = φ_w(E) ∈ M_w.
2. pr_{M(E)}(z_n) ∈ pr_{M(E)}(E), so the limit lies in the closed set K(E). By (1), the boundary coordinate is indexed by an element of M(E), so pr_{M(E)}(κ) ∈ ∂. ∎

**Lemma 2.3 (holomorphy of t ↦ Y_t) [coarse: (R1), (R2)].** The map Δ → M_{g_i,n_i}, t ↦ Y_t, is holomorphic. Consequently, if Y_t = Y_0 for all t in a non-empty open subset of Δ, then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Continuity.** Fix z_0 ∈ ∂V_0. By (R2), H_t(z_0) ∈ ∂V_t, so Y_t = π_i(H_t(z_0)). This is continuous in t.
2. **Setting up a proper map.**
   - Put 𝒜′ := closure(𝒱) ∩ (closure(Δ_Γ) × Δ), which is analytic by (R1).
   - Let 𝒵 ⊂ 𝒜′ be the closed analytic subset lying over closure(Δ_Γ) ∖ Δ_Γ. Then 𝒜′ ∖ 𝒵 = ⋃_t ∂V_t × {t}.
   - Let 𝒜̂′ := (ξ̄_Γ × id)^{-1}(𝒜′) ⊂ ∏_j M̄_{g_j,n_j} × Δ, and let 𝒜̂ be the union of its irreducible components not contained in 𝒵̂ := (ξ̄_Γ × id)^{-1}(𝒵).
   - Then 𝒜̂ is the closure of 𝒜̂′ ∖ 𝒵̂ (fact (Cl)). Since ∏_j M̄_{g_j,n_j} is compact, the map φ := (pr_i, t) : 𝒜̂ → M̄_{g_i,n_i} × Δ is proper.
3. **The image is the graph.**
   - By Remmert's proper mapping theorem, Σ := φ(𝒜̂) is analytic.
   - Since φ is proper, hence closed, Σ = closure(φ(𝒜̂′ ∖ 𝒵̂)). By the product-type assumption, φ(𝒜̂′ ∖ 𝒵̂) = {(Y_t, t) : t ∈ Δ}.
   - This graph is already closed in M̄_{g_i,n_i} × Δ: if (Y_{t_n}, t_n) → (y, t), then y = Y_t by continuity. So Σ is the graph of Y.
4. **Holomorphy.**
   - The projection t : Σ → Δ is a homeomorphism, with inverse t ↦ (Y_t, t). So Σ is a 1-dimensional analytic set (topological dimension 2).
   - Σ is locally irreducible at every point: a curve germ with r ≥ 2 branches has punctured neighbourhoods with ≥ 2 components, whereas a disc does not.
   - So the normalisation ν_Σ : Σ̂ → Σ is a homeomorphism, and t∘ν_Σ : Σ̂ → Δ is a bijective holomorphic map of Riemann surfaces, hence biholomorphic.
   - Thus Y = pr_1∘ν_Σ∘(t∘ν_Σ)^{-1} is holomorphic.
5. **Identity theorem.** The set {t : Y_t = Y_0} is the preimage of a point under a holomorphic map, hence a closed analytic subset of the connected disc Δ. If it has interior, it is Δ. ∎

**Lemma 2.4 (topological characterisation of pieces) [none].** Let X be a closed analytic set of dimension ≤ 1 in a complex space, and let X^disc be the set of points of X having a neighbourhood in X homeomorphic to an open disc of ℝ². Then:
- the 1-dimensional irreducible components of X are exactly the closures of the connected components of X^disc;
- consequently, a homeomorphism X → X′ between two such sets maps the 1-dimensional irreducible components of X bijectively onto those of X′.

*Proof.* We use the local structure of curve germs (fact (CG)). If z ∈ X lies on a 1-dimensional component and the germ (X, z) has r ≥ 1 branches, then:
- z has arbitrarily small neighbourhoods U for which U ∖ {z} is a disjoint union of r punctured discs, one in each branch;
- each branch is homeomorphic to a disc.

1. **X^disc = the non-isolated points with r(z) = 1.**
   - If r(z) = 1, the branch is a disc neighbourhood.
   - Isolated points are not in X^disc.
   - Suppose r(z) ≥ 2 and z had a disc neighbourhood V. Choose U as above inside V, and a closed topological disc D ∋ z, a neighbourhood of z, with D ⊂ U. Then D ∖ {z} is connected, so it lies in one of the punctured discs of U ∖ {z}. But D is a neighbourhood of z, so it meets every branch. Contradiction.
2. **Points of X^disc lie on exactly one component.** A point on two distinct components has at least two branches, since distinct components share no open subset. For a component E, put X^disc_E := X^disc ∩ E. It is E minus a closed discrete subset of E: the points of E on other components, together with the multi-branch points of E.
3. **X^disc_E is connected and dense in E.** It equals ν(Ê ∖ D) with D closed and discrete in the connected Riemann surface Ê. So it is connected and dense in E.
4. **X^disc_E is a connected component of X^disc.**
   - It is open in X^disc, since it is the complement of the closed, locally finite union of the other components.
   - It is closed in X^disc, since E is closed.
   - X^disc = ⊔_E X^disc_E, so these are exactly the components.
5. **Homeomorphisms.** A homeomorphism maps X^disc onto X′^disc. It maps components to components and closures to closures. ∎

**Lemma 2.5 (stabilisers are automorphism groups) [none].** Let x̂ ∈ T_G and Z := ξ_G p(x̂). Then Stab_{Mod_G}(x̂) ≅ Aut(Z), canonically.

*Proof.* Write x̂ = (C_w, f_w)_w.
1. **The homomorphism.**
   - g = (σ, (φ_w)) fixes x̂ iff for each w there is a biholomorphism α_w : C_w → C_{σ(w)}, isotopic to f_{σ(w)}∘φ_w∘f_w^{-1} and carrying the point labelled h to the point labelled σ(h).
   - α_w is unique, because a biholomorphism of a stable pointed curve isotopic to the identity is the identity (fact (Iso)).
   - Since σ respects the pairing of half-edges, ⊔_w α_w descends to an automorphism α(g) of Z. Then g ↦ α(g) is a homomorphism.
2. **Injective.** If α(g) = id, its lift to the normalisation ⊔_w C_w is the identity. It fixes each component and each preimage of each node, so σ = id on V(G) and H(G). Then each α_w = id, so φ_w is trivial.
3. **Surjective.** Let α ∈ Aut(Z).
   - α lifts to the normalisation. It permutes components and node preimages compatibly with the pairing, which defines σ ∈ Aut(G), with its action on half-edges, and biholomorphisms α_w : C_w → C_{σ(w)}.
   - Put φ_w := [f_{σ(w)}^{-1}∘α_w∘f_w]. Then g := (σ, (φ_w)) ∈ Mod_G fixes x̂, and α(g) = α. ∎

*Remark.* Let K_G be the kernel of the action of Mod_G on T_G. Then K_G ⊂ Stab(x̂) for every x̂. Correct examples of non-trivial elements of K_G:
- the elliptic involution of a (1,1)-vertex, extended by the identity;
- for a (1,2)-vertex whose two special points are the half-edges of a self-loop, the half-edge swap together with z ↦ p_1 + p_2 − z.

There are no (2,0)-vertices in boundary strata. Since every stabiliser contains K_G, condition (c) "modulo K_G" is equivalent to (c). None of this is used below.

---

## II.3. The descended transport Π_t [orb]

Fix a boundary stratum G and use the notation of C5. Put Â := ⋃_t Â_t × {t} = (ξ_G × id)^{-1}(closure(𝒱) ∩ (Δ_G × Δ)), a closed subset of ∏_w M_w × Δ.

**Lemma 3.1 (descended transport) [orb: (a); (b) for all g ∈ Mod_G (descent uses only g ∈ Mod_Π; injectivity and surjectivity use general g); the inclusion "⊂" of (c); (d)].** There is a map Π : Â_0 × Δ → ∏_w M_w, Π_t := Π(·, t), with the following properties.
1. p∘H̃_t = Π_t∘p on Ã_0.
2. Π_t is a homeomorphism Â_0 → Â_t, ξ_G∘Π_t = H_t∘ξ_G, and Π_0 = id.
3. Θ : Â_0 × Δ → Â, (z, t) ↦ (Π_t z, t), is a homeomorphism.
4. For every y ∈ A_0 and t ∈ Δ: ξ_G^{-1}(H_t(y)) = Π_t(ξ_G^{-1}(y)).
5. For each piece E of Â_0, E_t := Π_t(E) is a piece of Â_t, and E ↦ E_t is a bijection between the pieces at times 0 and t.
6. For each piece E there is a homeomorphism Ĥ_t : Ê → Ê_t with ν_t∘Ĥ_t = Π_t∘ν. It maps the punctures (ends) of Ê bijectively to those of Ê_t.

*Proof.*
1. **Descent.** If p(x) = p(y) with x, y ∈ Ã_0, then y = gx with g ∈ Mod_Π, and H̃_t y = gH̃_t x by (b). So Π_t(p x) := p(H̃_t x) is well defined, and (1) holds.
   - By (a), ξ_G(Π_t(px)) = H_t(ξ_G p x) ∈ H_t(A_0) = A_t (R2). So Π_t maps into Â_t and ξ_G∘Π_t = H_t∘ξ_G.
   - By (d), Π_0 = id.
2. **H̃_t is injective on Ã_0.**
   - Let H̃_t x = H̃_t y. By (a), H_t(ξ_G p x) = H_t(ξ_G p y), and H_t is injective, so ξ_G p x = ξ_G p y.
   - By (St2), y = gx for some g ∈ Mod_G. Then g H̃_t x = H̃_t(gx) = H̃_t x by (b), so g ∈ Stab(H̃_t x) = Stab(x), using the inclusion "⊂" of (c). Hence y = x.
3. **H̃_t is onto Ã_t.**
   - Let y ∈ Ã_t. Then ξ_G p y ∈ A_t = H_t(A_0), so ξ_G p y = H_t(ξ_G p x) = ξ_G p H̃_t x for some x ∈ Ã_0.
   - By (St2), y = gH̃_t x = H̃_t(gx), and gx ∈ Ã_0 because Ã_0 is Mod_G-invariant.
4. **Π_t is bijective onto Â_t.**
   - Injective: if Π_t(px) = Π_t(py), then H̃_t y = gH̃_t x = H̃_t(gx) with g ∈ Mod_Π. By step 2, y = gx, so py = px.
   - Surjective by step 3.
5. **Joint continuity of Π.** p is the quotient map of a group action, hence open. Its restriction to the saturated set Ã_0 is open onto Â_0, so p × id : Ã_0 × Δ → Â_0 × Δ is a quotient map. The map (x, t) ↦ p(H̃_t x) is continuous and constant on its fibres, so Π is continuous.
6. **Continuity of Θ^{-1}, hence (2) and (3).**
   - Let (w_n, t_n) → (w, t) in Â, and z_n := Π_{t_n}^{-1}(w_n). Then ξ_G(z_n) = H_{t_n}^{-1}(ξ_G w_n) → H_t^{-1}(ξ_G w), by continuity of H^{-1}.
   - ξ_G is proper (St4), so the z_n lie in a compact set.
   - Every limit point z of (z_n) lies in the closed set Â_0 and satisfies Π_t z = w, by joint continuity. By injectivity z = Π_t^{-1} w, so z_n → Π_t^{-1}w.
   - Thus Θ is a continuous bijection with continuous inverse. Restricting to a fixed t gives (2).
7. **(4).** "⊇" follows from ξ_G Π_t = H_t ξ_G. For "⊆": if ξ_G(w) = H_t(y) with w ∈ Â_t, write w = Π_t(z). Then H_t(ξ_G z) = H_t(y), so ξ_G z = y.
8. **(5)** follows from (2) and Lemma 2.4, applied to Â_0 and Â_t; both have dimension ≤ 1 by §1.2.
9. **(6).**
   - Let F ⊂ E be the finite set (Lemma 2.1) of multi-branch points of E together with Π_t^{-1}(multi-branch points of E_t).
   - ν and ν_t are homeomorphisms over the complements of the multi-branch points (continuous, bijective, proper). So Ĥ_t := ν_t^{-1}∘Π_t∘ν is a homeomorphism Ê ∖ ν^{-1}(F) → Ê_t ∖ ν_t^{-1}(Π_t F).
   - Let ẑ ∈ ν^{-1}(F) and let D be a small closed disc around ẑ. As points of D ∖ ẑ approach ẑ, their images approach the finite set ν_t^{-1}(Π_t ν ẑ), because ν_t is proper.
   - Ĥ_t(D ∖ ẑ) is connected. For D small it therefore lies in a small neighbourhood of a single point of that finite set; define Ĥ_t(ẑ) to be that point.
   - Doing the same for Ĥ_t^{-1} gives a continuous inverse. So Ĥ_t is a homeomorphism Ê → Ê_t, and it maps ends to ends.
   - By Lemma 2.1(2), the ends are the punctures. ∎

**Remark 3.2 (where (R2^orb) enters).** Under (R2) alone, (1)–(6) are available for product-type strata, with Π_t := H_t. In non-product strata a continuous, bijective choice of lifts of H_t to ∏_w M_w is exactly what may fail: it is the "twin" problem of the original route.

---

## II.4. Rigidity of transported pieces (Theorem RO) [orb]

Fix a boundary stratum G and a piece E of Â_0. Take j, Λ, u_0 : H → Ê and O_0 = H/Λ from I.2, and F_0, f_0, R(λ), S from J0 (I.3). For t ∈ Δ let E_t := Π_t(E), with ν_t : Ê_t → E_t and Ĥ_t : Ê → Ê_t from Lemma 3.1.

Throughout this section:
- H carries the Poincaré metric of curvature −4, with distance d_H. For hyperbolic γ ∈ PSL_2(ℝ), α_γ is its axis and ℓ(γ) := d_H(x, γx) for x ∈ α_γ is its translation length.
- T_j carries the Teichmüller metric d_T. For a mapping class g, τ(g) := inf_X d_T(X, gX).

**Lemma 4.1 (transported orbifold) [orb, through Lemma 3.1].** For every t ∈ Δ there are:
- a lattice Λ_t ⊂ PSL_2(ℝ) and a holomorphic map u_t : H → Ê_t inducing a biholomorphism H/Λ_t ≅ Ê_t. Its elliptic fixed points lie exactly over the points Ĥ_t(c), c a cone point of O_0, with order e_c, and its cusps correspond to the punctures of Ê_t;
- a homeomorphism h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0;
- an isomorphism θ_t : Λ_t → Λ, θ_t(λ) := h̃_t^{-1}λh̃_t, which maps elliptic, parabolic and hyperbolic elements to elements of the same type.

For t = 0 we take Λ_0 = Λ, u_0 and h̃_0 = id.

*Proof.*
1. **The lattice Λ_t.** Let O_t be the orbifold with underlying Riemann surface Ê_t, cone points Ĥ_t(c) of order e_c, and the punctures of Ê_t as cusps.
   - Ĥ_t is a homeomorphism mapping punctures to punctures (Lemma 3.1(6)). So Ê and Ê_t have the same genus and number of punctures, and χ^orb(O_t) = χ^orb(O_0) < 0.
   - By the uniformisation theorem for hyperbolic 2-orbifolds (Unif), there is a lattice Λ_t with a holomorphic quotient map u_t : H → H/Λ_t = Ê_t, branched exactly over the cone points with the given orders, whose cusps correspond to the punctures.
2. **Lifting Ĥ_t.** Let H^♮_t := H ∖ u_t^{-1}(cone points) and O_t^♮ := Ê_t ∖ (cone points).
   - u_t : H^♮_t → O_t^♮ is a regular covering with deck group Λ_t. It corresponds to the normal subgroup N_t ⊂ π_1(O_t^♮) normally generated by the e_c-th powers of small loops around the cone points.
   - Ĥ_t maps a small disc around a cone point c onto a disc around Ĥ_t(c) containing no other cone point. So it maps a small loop around c to a loop freely homotopic to a small loop around Ĥ_t(c), or to its inverse. Hence (Ĥ_t)_* N_0 = N_t.
   - By the lifting criterion, Ĥ_t lifts to a homeomorphism H^♮_0 → H^♮_t; the same applies to Ĥ_t^{-1}.
   - Near a preimage of a cone point, u is locally z ↦ z^{e}. A homeomorphism of punctured discs commuting with z ↦ z^e extends continuously over 0.
   - So the lift extends to a homeomorphism h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0.
3. **The isomorphism θ_t.** For λ ∈ Λ_t,
   u_0∘h̃_t^{-1}λh̃_t = Ĥ_t^{-1}∘u_t∘λ∘h̃_t = Ĥ_t^{-1}∘u_t∘h̃_t = u_0.
   - So h̃_t^{-1}λh̃_t is a deck transformation of u_0 : H^♮_0 → O_0^♮, i.e. an element of Λ.
   - θ_t is an injective homomorphism, and the symmetric argument gives its inverse.
4. **Types.**
   - θ_t preserves orders, and in a Fuchsian group the non-trivial elements of finite order are exactly the elliptic ones.
   - For an infinite-order element λ: λ is parabolic iff it stabilises a component of u^{-1}(P), where P is a punctured-disc neighbourhood of a puncture containing no cone point.
     - Such a component C covers P with infinite cyclic deck group, generated by the image of the peripheral loop, which is parabolic.
     - Conversely, a parabolic λ fixes the cusp point at which C sits, so λC = C.
     - In a Fuchsian group, an element fixing a parabolic fixed point is parabolic or trivial.
   - h̃_t maps the components of u_0^{-1}(P) onto the components of u_t^{-1}(Ĥ_t P). So θ_t preserves parabolicity, and hence also hyperbolicity. ∎

**Proposition 4.2 (transport of the joint lift) [orb: (a), (b) for g ∈ Mod_Π, and via Lemma 3.1 also (c), (d)].** Put F_t := H̃_t∘F_0∘h̃_t^{-1} : H → T_G. Then:
1. F_t is holomorphic and p∘F_t = ν_t∘u_t;
2. F_t∘λ = g∘F_t for every λ ∈ Λ_t and every g ∈ R(θ_t λ).

*Proof.*
1. **Lifting.** F_0(H) ⊂ Ã_0, since p F_0 = ν u_0 takes values in Â_0. So F_t is defined and continuous. By Lemma 3.1(1) and (6) and Lemma 4.1,
   p∘F_t = Π_t∘p∘F_0∘h̃_t^{-1} = Π_t∘ν∘u_0∘h̃_t^{-1} = Π_t∘ν∘Ĥ_t^{-1}∘u_t = ν_t∘u_t.
   ν_t∘u_t is holomorphic, so F_t is holomorphic by CL (I.3), applied with Γ = Mod_Π acting on T = T_G.
2. **Equivariance.** We have h̃_t^{-1}λ = θ_t(λ)h̃_t^{-1}. For g ∈ R(θ_tλ),
   F_t(λy) = H̃_t F_0(θ_t(λ)h̃_t^{-1}y) = H̃_t(g F_0(h̃_t^{-1}y)) = g F_t(y),
   using (b). ∎

**Lemma 4.3 (rigidity of the Teichmüller coordinate) [orb, through Prop. 4.2].** There is A_t ∈ PSL_2(ℝ) with A_tλA_t^{-1} = θ_t^{-1}(λ) for all λ ∈ Λ. In particular A_tΛA_t^{-1} = Λ_t. Moreover f_t∘A_t = f_0, where f_t := pr_j∘F_t.

*Proof.* For μ ∈ Λ put R_j(μ) := pr_j(R(μ)), a set of mapping classes of the vertex j. Every g ∈ R_j(μ) satisfies g∘f_0 = f_0∘μ.

1. **Step 1.** Let μ ∈ Λ be hyperbolic and g ∈ R_j(μ). Then g is pseudo-Anosov, τ(g) = ℓ(μ), and the set Min(g) where d_T(X, gX) = τ(g) is the geodesic f_0(α_μ).
   - By J0(ii), f_0 is an isometry onto the Teichmüller disc 𝔇 = f_0(H). So g preserves 𝔇, acts on it as f_0μf_0^{-1}, and translates the Teichmüller geodesic f_0(α_μ) by ℓ(μ) > 0.
   - A mapping class preserving a Teichmüller disc and acting on it as a hyperbolic isometry is pseudo-Anosov (fact (VT)).
   - By Bers' theorem (Bers), a pseudo-Anosov g has a unique invariant Teichmüller geodesic, its axis. Min(g) is exactly the axis, and τ(g) is the translation along it. So the axis is f_0(α_μ) and τ(g) = ℓ(μ).
2. **Step 2: ℓ_t(γ) ≥ ℓ(θ_tγ) for hyperbolic γ ∈ Λ_t.** Here ℓ_t denotes translation length for Λ_t.
   - θ_tγ is hyperbolic (Lemma 4.1). Take x ∈ α_γ and g ∈ R_j(θ_tγ).
   - By Prop. 4.2(2), f_t(γx) = g f_t(x). f_t is holomorphic, so it is 1-Lipschitz by Royden's theorem (Roy). Hence
     τ(g) ≤ d_T(f_t x, g f_t x) = d_T(f_t x, f_t γx) ≤ d_H(x, γx) = ℓ_t(γ).
   - By Step 1, τ(g) = ℓ(θ_tγ).
3. **Step 3: Thurston.**
   - By Selberg's lemma (Sel), Λ has a torsion-free normal subgroup Λ′ of finite index. Put Λ′_t := θ_t^{-1}(Λ′) = h̃_tΛ′h̃_t^{-1}.
   - X := H/Λ′ and X_t := H/Λ′_t are complete hyperbolic surfaces of finite area. h̃_t descends to a homeomorphism φ : X → X_t, mapping cusps to cusps, which induces θ_t^{-1} on deck groups.
   - For every closed geodesic class of X, represented by a hyperbolic λ′ ∈ Λ′, Step 2 with γ := θ_t^{-1}(λ′) gives ℓ_{X_t}(φ(λ′)) ≥ ℓ_X(λ′). Thus ψ := φ^{-1} : X_t → X does not increase lengths of closed curves.
   - If φ reverses orientation, replace X_t by its complex conjugate. This changes no lengths.
   - By Thurston's theorem (Th), ψ is homotopic to an isometry. Lifting the homotopy equivariantly gives an isometry A_t of H with A_tλ′A_t^{-1} = θ_t^{-1}(λ′) for λ′ ∈ Λ′. The conjugation is constant along the lifted homotopy, because Λ′_t is discrete.
   - A_t is a priori possibly orientation-reversing.
4. **Extension to Λ.**
   - For λ ∈ Λ put ψ(λ) := A_t^{-1}θ_t^{-1}(λ)A_t and c := λ^{-1}ψ(λ).
   - For λ′ ∈ Λ′, normality of Λ′ gives ψ(λλ′λ^{-1}) = λλ′λ^{-1}, i.e. cλ′c^{-1} = λ′.
   - The centraliser of a lattice in Isom(H) is trivial (Cent), so c = 1. Hence A_tλA_t^{-1} = θ_t^{-1}(λ) for all λ ∈ Λ.
5. **Step 4: k_t := f_t∘A_t equals f_0.**
   - For μ ∈ Λ and g ∈ R_j(μ): k_t(μx) = f_t(θ_t^{-1}(μ)A_t x) = g k_t(x), by Prop. 4.2(2) with λ = θ_t^{-1}(μ), since R_j(θ_tλ) = R_j(μ).
   - k_t is 1-Lipschitz (Roy). For hyperbolic μ and x ∈ α_μ,
     d_T(k_t x, g k_t x) = d_T(k_t x, k_t μx) ≤ ℓ(μ) = τ(g).
     So k_t(x) ∈ Min(g) = f_0(α_μ).
   - At a transverse intersection point x of two distinct axes α_μ, α_ν we get k_t(x) ∈ f_0(α_μ) ∩ f_0(α_ν) = {f_0(x)}, by injectivity of f_0.
   - Such points are dense in H (Dens). By continuity, k_t = f_0.
6. **Orientation.** If A_t reversed orientation, k_t would be anti-holomorphic and equal to the non-constant holomorphic f_0, which is impossible. So A_t ∈ PSL_2(ℝ). ∎

**Consequence.** A_t descends to a biholomorphism ā_t : Ê = H/Λ → H/Λ_t = Ê_t with u_t∘A_t = ā_t∘u_0.

**Theorem 4.4 (Theorem RO) [orb: everything used in Lemma 3.1, Prop. 4.2, Lemma 4.3; part (b) also uses Lemmas F0, F1 of §10].** For all t ∈ Δ:
- (a) M(E_t) = M(E);
- (b) K(E_t) = K(E).

*Proof.*
1. **Step 1 (an honest homomorphism into a torsion-free group).**
   - Fix N ≥ 3. For each w, Mod_w[N] is defined as the kernel of Mod_w → Sp(2g_w, ℤ/N) if g_w ≥ 1, and as Mod_w if g_w = 0. Each Mod_w[N] is torsion-free and normal of finite index in Mod_w (fact (TF)). Put Mod[N] := ∏_w Mod_w[N].
   - S is finite, so S ∩ Mod[N] = {1}.
   - By J0(iii), λ ↦ R(λ) is a homomorphism Λ → N(S)/S. Let Λ^N be the preimage of the subgroup (N(S) ∩ Mod[N]S)/S. This is a subgroup because Mod[N] is normal in Mod_Π, and its index is at most [Mod_Π : Mod[N]] < ∞. So Λ^N has finite index in Λ.
   - By Selberg's lemma and passing to the normal core, there is a torsion-free normal subgroup Λ″ ⊂ Λ^N of finite index in Λ.
   - For μ ∈ Λ″, R(μ) ∩ Mod[N] consists of exactly one element r(μ). It is non-empty by the definition of Λ^N, and two such elements differ by an element of S ∩ Mod[N] = {1}.
   - r : Λ″ → Mod[N] is a homomorphism, because r(μ)r(ν) ∈ R(μν) ∩ Mod[N].
2. **Step 2 (normalised maps with t-independent equivariance).** Put g_t := F_t∘A_t : H → T_G, which is holomorphic. For μ ∈ Λ″, by Lemma 4.3 and Prop. 4.2(2) with r(μ) ∈ R(μ) = R(θ_t(θ_t^{-1}μ)),
   g_t(μx) = F_t(θ_t^{-1}(μ)A_t x) = r(μ) g_t(x).
   - Mod[N] acts freely and properly discontinuously on T_G (finite stabilisers in a torsion-free group are trivial). So M[N] := T_G/Mod[N] = ∏_w M_w[N] is a complex manifold, and each M_w[N] = T_w/Mod_w[N] is a K(Mod_w[N], 1), since T_w is contractible.
   - R := H/Λ″ is a Riemann surface of finite type with π_1(R) = Λ″, a finite cover of the finite-area orbifold H/Λ.
   - g_t descends to a holomorphic ḡ_t = (ḡ^w_t)_w : R → M[N]. Moreover p∘g_t = ν_t∘u_t∘A_t = ν_t∘ā_t∘u_0.
3. **Step 3 (fixed homotopy classes).**
   - The coordinate g^w_t := pr_w∘g_t is a lift of ḡ^w_t that is r_w-equivariant, with r_w := pr_w∘r.
   - So ḡ^w_t induces r_w on fundamental groups, up to conjugation (base-point changes).
   - By (KP1), free homotopy classes of maps from R into a K(π,1) correspond to homomorphisms π_1(R) → π modulo conjugation. Hence, for each w, the maps ḡ^w_t (t ∈ Δ) are all freely homotopic.
4. **Step 4 (part (a)).** We show: ḡ^w_t is constant ⟺ r_w = 1. The right-hand side does not depend on t.
   - (⇒) If ḡ^w_t is constant, then g^w_t takes values in one discrete Mod_w[N]-orbit, so it is constant (H is connected), say ≡ y. Then r_w(Λ″) ⊂ Stab(y), which is finite and hence trivial.
   - (⇐) If r_w = 1, then g^w_t descends to a holomorphic map R → T_w. T_w is biholomorphic to a bounded domain (Bers embedding, (BE)). Bounded holomorphic functions extend over the punctures of R to its compactification R̄, and are then constant. So ḡ^w_t is constant.
   - Next, pr_w∘ν_t∘ā_t∘u_0 = π_w∘g^w_t, where π_w : T_w → M_w factors through the finite-to-one map M_w[N] → M_w. Since ā_t∘u_0 is onto Ê_t and H is connected:
     pr_w is constant on E_t ⟺ ḡ^w_t is constant ⟺ r_w = 1.
   - Hence M(E_t) = {w : r_w ≠ 1} for every t, and (a) follows.
5. **Step 5 (finitely many candidates).** Put M := M(E). For u ∈ M, the maps ḡ^u_t (t ∈ Δ) are non-constant, holomorphic, and freely homotopic (Step 3).
   - They lie in a finite set Φ_u independent of t: for g_u = 0 by Lemma F0 (§10; then Mod_u[N] = Mod_u and M_u[N] = M_u = M_{0,n_u}); for g_u ≥ 1 (including type (1,1)) by Lemma F1 (§10), which gives finiteness of all non-constant holomorphic maps R → M_u[N].
   - pr_M(E_t) = pr_M ν_t ā_t u_0(H) is the image of R under (ρ_u∘ḡ^u_t)_{u∈M}, where ρ_u : M_u[N] → M_u.
   - Hence K(E_t) lies in a finite set 𝒦_E of curves, independent of t.
6. **Step 6 (constancy).** For K ∈ 𝒦_E put T_K := {t ∈ Δ : K(E_t) = K}.
   - **T_K is closed.** Let t_n → t* with t_n ∈ T_K. Every point of E_{t*} is Π_{t*}(z) = lim_n Π_{t_n}(z) for some z ∈ E, by joint continuity (Lemma 3.1). So pr_M(E_{t*}) ⊂ K, hence K(E_{t*}) ⊂ K.
   - By (a) and Lemma 2.1(3), K(E_{t*}) is an irreducible curve. So it equals the irreducible curve K.
   - The T_K are finitely many, pairwise disjoint, closed, and cover the connected Δ. So one of them is Δ, and by Π_0 = id it is T_{K(E)}. ∎

*Remarks.*
- Only (a) is used for the transitions in §9. (b) is used only at the endpoint, in §9.3, and only through Corollary 4.5 below.
- Part (a) does not use Lemmas F0, F1.

**Corollary 4.5 (ends of transported pieces) [orb, Lemmas F0/F1 through 4.4(b)].** Let z_n ∈ E_t with z_n → κ ∈ ∏_w M̄_w, and suppose some coordinate of κ lies in the boundary. Then:
- every boundary coordinate of κ is indexed by an element of M(E);
- pr_{M(E)}(κ) ∈ K(E) ∩ ∂;
- every smooth component, with its special points, of every coordinate κ_u (u ∈ M(E)) has its class in the finite, t-independent set F′(E) of Definition 2.1′.

*Proof.* Lemma 2.2 applied to the piece E_t, together with M(E_t) = M(E) and K(E_t) = K(E) from Theorem 4.4. ∎

*Remark 4.6 (observation of an independent referee; not used).* Theorem 4.4(a) does not need Lemma 4.3 or (Th): with Λ″_t := θ_t^{-1}(Λ″) ⊂ Λ_t, the map F_t satisfies F_t(λy) = r(θ_t λ)F_t(y) and descends to H/Λ″_t → ∏M_w[N], and the criterion "ḡ^w constant ⟺ r_w = 1" is proved as in Step 4. Lemma 4.3 (hence (Th)) is needed only for (b), to fix the source surface. So the transport of constant values along the chain in §9 is independent of (Th); only the endpoint step §9.3 uses it.

---

## II.5. Isotropy is transported; the lift of Q_t is unique [orb]

For Q ∈ B_0 put Q_t := H_t(Q). By (R2), Q_t ∈ Δ_{G_Q}.

**Proposition 5.1 (isotropy) [orb: (a), (c)].** For every Q ∈ B_0 and t ∈ Δ, |Aut(Q_t)| = |Aut(Q)|.

*Proof.*
- Let G := G_Q. Then Q ∈ A^G_0, so there is x̂ ∈ Ã_0 with ξ_G p(x̂) = Q.
- By (a), ŷ := H̃_t(x̂) satisfies ξ_G p(ŷ) = Q_t.
- By Lemma 2.5 and (c): Aut(Q_t) ≅ Stab_{Mod_G}(ŷ) = Stab_{Mod_G}(x̂) ≅ Aut(Q). ∎

**Proposition 5.2 (one fixed lift) [orb: (a), (c)].** Let J ∈ B_0, and let B′ ⋐ B be Aut(J)-invariant balls in Def(J), both small enough for (Kur). Then there is ε > 0 such that for |t| < ε:
- J_t ∈ q(B′);
- q^{-1}(J_t) ∩ B = {p(t)} is a single point, fixed by Aut(J), and p(t) ∈ B′;
- t ↦ p(t) is continuous, with p(0) = 0;
- p(t) lies in the deepest locus {s_e = 0 for all e ∈ E(G_J)}.

*Proof.*
1. **Choice of ε.** t ↦ J_t is continuous and J_0 = J ∈ q(B′), which is open. Choose ε with J_t ∈ q(B′) for |t| < ε.
2. **One point.**
   - By (Kur), q^{-1}(J_t) ∩ B is one Aut(J)-orbit Aut(J)·p. It has |Aut(J)|/|Stab_{Aut(J)}(p)| elements.
   - Again by (Kur), Stab_{Aut(J)}(p) ≅ Aut(X_p) ≅ Aut(J_t), which by Prop. 5.1 has order |Aut(J)|.
   - So the orbit is a single point p(t), fixed by Aut(J). Since q^{-1}(J_t) ∩ B′ ≠ ∅, we have p(t) ∈ B′. Also p(0) = 0, because q^{-1}(J) ∩ B = {0}.
3. **Continuity.** Let t_n → t. The p(t_n) lie in the compact set closure(B′) ⊂ B. Any limit point p* satisfies q(p*) = J_t, so p* = p(t). Hence p(t_n) → p(t).
4. **Deepest locus.** J_t ∈ Δ_{G_J}, so X_{p(t)} has |E(G_J)| nodes. By (Kur), all s_e(p(t)) vanish. ∎

*Remark 5.3.*
- Under (R2) alone, q^{-1}(J_t) ∩ B may consist of several points: the "lift-curves" permuted by Aut(J). This happens when the isotropy drops at t ≠ 0 (§8.2), and it is the source of all the twin configurations of the original route.
- Prop. 5.2 removes them. Holomorphy of p (which holds when (P) holds for some branch at J, by Lemma A.1(2) and CL) is not needed.

---

## II.6. Transport of lifted branches [items 1–2 coarse; items 3–5 orb]

**Setting 6.0.** Let J ∈ B_0 and choose balls B′ ⋐ B ⊂ Def(J) as in Prop. 5.2. Let β be a branch of B_0 at J, with stratum G := G_β of β ∖ J, β̃ a lift, S := S_β̃, and ι : G_S → G an isomorphism (Lemma 1.1). We shrink the neighbourhood of J and ε > 0 so that the following hold.
- (i) β is an **open** disc neighbourhood of J in the branch, with β ∖ J ⊂ Δ_G, and H(β × Δ_ε) ⊂ q(B′) × Δ_ε. This is possible by continuity of H at (J, 0), since H(J, 0) = (J, 0) (take a closed disc β_c with these properties and let β be its interior). Then β ∖ J is a connected punctured open disc, and it is open in A^G_0: near any y ∈ β ∖ J, B_0 coincides with the branch β by (iv), and A^G_0 ⊂ B_0. Compactness of β is never used; Lemma 6.1(4) only needs points y_n ∈ β ∖ J with y_n → J. (An earlier version took β closed; openness of β ∖ J is what Lemma 6.1(1),(3) need.)
- (ii) β ∖ J avoids the finite set ξ_G(Sing Â_0 ∪ {isolated points of Â_0}) (Lemma 2.1(1)).
- (iii) Prop. 5.2 holds on Δ_ε.
- (iv) Near J, B_0 is the union of its branches at J, and these meet only at J.

Since (i)–(iv) involve finitely many conditions, they can be imposed simultaneously for finitely many branches at finitely many points.

Define:
- N := H((β ∖ J) × Δ_ε);
- Ñ := the connected component of q^{-1}(N) ∩ (B × Δ_ε) containing (β̃ ∖ 0) × {0}, which is connected;
- Ñ_t := {p : (p, t) ∈ Ñ}.

By (Kur), q^{-1}(q(B′)) ∩ B = B′, so Ñ ⊂ B′ × Δ_ε.

Let E be the piece of Â_0 containing Π_{S,ι}(β̃ ∖ 0). It exists and is unique: Π_{S,ι}(β̃ ∖ 0) is a connected subset of ξ_G^{-1}(β ∖ J), which by (ii) lies in the 1-manifold of regular 1-dimensional points of Â_0, and each component of that manifold lies in a single piece.

**Lemma 6.1 (transported lifts).** In Setting 6.0:
1. [coarse: (R1), (R2)] q(Ñ) = N. In particular Ñ_t ≠ ∅ and q(Ñ_t) = H_t(β ∖ J) for every t ∈ Δ_ε.
2. [coarse: (R2)] Every (p, t) ∈ Ñ has pattern S(p) = S.
3. [orb: through Lemma 3.1] Π_{S,ι}(Ñ_t) ⊂ E_t = Π_t(E) for every t ∈ Δ_ε.
4. [orb: through Prop. 5.2] For every t ∈ Δ_ε there are points (p_n, t) ∈ Ñ with p_n → p(t). For every such sequence, Π_{S,ι}(p_n) → κ̂(t) := Π_{S,ι}(p(t)) ∈ ∏_w M̄_w.
5. If (P) holds for β, then κ̂(t) has a coordinate in the boundary.

*Proof.*
1. **q(Ñ) = N.**
   - N is homeomorphic to (β ∖ J) × Δ_ε, hence connected.
   - N is open in ℬ_G := closure(𝒱) ∩ (Δ_G × Δ_ε). Indeed, H is a homeomorphism (A^G_0 × Δ_ε) → ℬ_G by (R2), and β ∖ J is open in A^G_0 by (iv).
   - q^{-1}(ℬ_G) ∩ (B × Δ_ε) is an analytic subset of the locally closed analytic set q^{-1}(Δ_G) × Δ_ε, hence locally connected. Its open subset q^{-1}(N) is locally connected too, so its components are open.
   - Aut(J) permutes these components. The union of the translates of Ñ is open, closed and Aut(J)-invariant in q^{-1}(N).
   - q restricted to the saturated set q^{-1}(N) is an open and closed map onto N, being a quotient by a finite group. So q(Ñ) = q(Aut(J)·Ñ) is non-empty, open and closed in N, hence equal to N.
2. **Pattern.** For (p, t) ∈ Ñ we have q(p) ∈ H_t(β ∖ J) ⊂ Δ_G, by (R2). By Lemma 1.1, S(p) is locally constant on Ñ, which is connected. At t = 0 it equals S on β̃ ∖ 0.
3. **Π_{S,ι}(Ñ_t) ⊂ E_t.**
   - By (2) and (PN1), ξ_G(Π_{S,ι}(p)) = q(p) ∈ H_t(β ∖ J) for (p, t) ∈ Ñ. By Lemma 3.1(4), Π_{S,ι}(p) ∈ Π_t(ξ_G^{-1}(β ∖ J)).
   - So Ψ : Ñ → ∏_w M_w × Δ_ε, (p, t) ↦ (Π_{S,ι}(p), t), maps the connected set Ñ into Θ(ξ_G^{-1}(β ∖ J) × Δ_ε) (Θ as in Lemma 3.1(3)).
   - ξ_G^{-1}(β ∖ J) is an open subset of the analytic set Â_0, hence locally connected. Let γ̂ be its connected component containing the connected set Π_{S,ι}(β̃ ∖ 0). Then γ̂ is open and closed in ξ_G^{-1}(β ∖ J).
   - By (ii), γ̂ is a connected subset of the regular 1-dimensional locus of Â_0, so it lies in a single piece, namely E.
   - Since Θ is a homeomorphism, Θ(γ̂ × Δ_ε) is open and closed in Θ(ξ_G^{-1}(β ∖ J) × Δ_ε). It meets Ψ(Ñ), because Θ(γ̂ × {0}) = γ̂ × {0} ⊃ Ψ((β̃ ∖ 0) × {0}), using Π_0 = id.
   - Hence Ψ(Ñ) ⊂ Θ(γ̂ × Δ_ε). That is, Π_{S,ι}(Ñ_t) ⊂ Π_t(γ̂) ⊂ Π_t(E) = E_t.
4. **Convergence to p(t).**
   - Fix t. Take y_n ∈ β ∖ J with y_n → J. By (1) there are (p_n, t) ∈ Ñ with q(p_n) = H_t(y_n) → H_t(J) = J_t.
   - Let (p_n, t) ∈ Ñ be any sequence with q(p_n) → J_t. The p_n lie in the compact set closure(B′) ⊂ B, and every limit point p* satisfies q(p*) = J_t, so p* = p(t) by Prop. 5.2. Hence p_n → p(t).
   - In particular the sequence just constructed converges to p(t), which proves the existence claim.
   - The p_n lie in L_S ∩ B by (2), p(t) lies in the deepest locus ⊂ L_S, and Π_{S,ι} is continuous on L_S ∩ B. Hence Π_{S,ι}(p_n) → Π_{S,ι}(p(t)).
5. **A boundary coordinate under (P).**
   - If S = E(G_J), then G_β ≅ G_S = G_J and J ∈ Δ_{G_β}, contrary to (P). So there is an edge e ∈ E(G_J) ∖ S.
   - e is contracted into a vertex w of G_S. By (PN2), the ι(w)-coordinate of κ̂(t) is glued along the node e, so it is nodal, i.e. lies in ∂M̄_{ι(w)}. ∎

**Proposition 6.2 (value of a constant label at the fixed lift) [orb: Lemma 6.1(3),(4) and Theorem 4.4(a)].** In Setting 6.0, assume (β̃, x) is labelled by (E, c) with c ∉ M(E) (Definition 1.2, with the ι of the setting). Then for |t| < ε:
- c ∉ M(E_t);
- comp_x(p(t)) = ι^*(φ_c(E_t)), where φ_c(E_t) is the constant value of pr_c on E_t;
- in particular [comp_x(p(t))] = [φ_c(E_t)].

*Proof.*
- By Theorem 4.4(a), c ∉ M(E_t).
- Take (p_n, t) ∈ Ñ with p_n → p(t) (Lemma 6.1(4)). By Definition 1.2, (PN3) and Lemma 6.1(2),(3):
  comp_x(p_n) = ι^*(pr_c Π_{S,ι}(p_n)) = ι^*(φ_c(E_t)).
- comp_x is continuous on L_x ∩ B ⊃ L_S ∩ B, and p(t) ∈ L_S. So comp_x(p(t)) = ι^*(φ_c(E_t)). ∎

**Proposition 6.3 (merge or move at a puncture lands in a finite set) [orb, with Lemmas F0/F1 through Cor. 4.5].** In Setting 6.0, assume (P) for β. Let x ∈ V(G_J) satisfy one of:
- (MERGE) x is not intact for S;
- (MOV) x is intact for S and [comp_x] is non-constant along β̃.

Then [comp_x(p(t))] ∈ F′(E) for all |t| < ε.

*Proof.*
- By Lemma 6.1(4),(5), κ̂(t) is a limit of points Π_{S,ι}(p_n) ∈ E_t and has a boundary coordinate. By Corollary 4.5, pr_M(κ̂(t)) ∈ K(E) ∩ ∂, with M := M(E).
- Let [x] be the vertex of G_S containing x and u := ι([x]). By (PN2), κ̂(t)_u is the stable curve glued from the comp_y(p(t)), y ∈ [x]. So comp_x(p(t)), with the half-edges at x as special points, is one of its smooth components with its special points.
- **u ∈ M.**
  - (MERGE): some edge at x lies in E(G_J) ∖ S and is contracted into [x]. So κ̂(t)_u is nodal, and u ∈ M by Corollary 4.5.
  - (MOV): [x] = {x}. By (PN3), pr_u∘Π_{S,ι} = (ι^{-1})^* comp_x is non-constant on β̃ ∖ 0, whose image lies in E. So u ∈ M(E).
- By Corollary 4.5, [comp_x(p(t))] ∈ F′(E). ∎

**Remark 6.4 (robustness of the labelling under Aut(G)) [orb: (b)].** Suppose Part I supplies the labelled identification of I.5 only up to relabelling by Aut(G). That is, (β̃, x) is labelled by (σE, σ(c)) for some σ ∈ Aut(G), instead of by (E, c). Then the conclusions of §9 are unchanged.
- Choose g ∈ Mod_G lifting σ (St3). By (b), H̃_t∘g = g∘H̃_t, which descends to Π_t∘σ = σ∘Π_t on Â_0.
- Hence (σE)_t = σ(E_t), and σ(c) is constant on (σE)_t with value the relabelling of φ_c(E_t).
- So [φ_{σ(c)}((σE)_t)] = [φ_c(E_t)].

---

## II.7. The local reading (Loc) implies (R2^orb) (Theorem LG)

**Lemma 7.1 (unique continuation of stabiliser-constant lifts) [none].** Let I ⊂ ℝ be an interval, and let γ_1, γ_2 : I → T_G be continuous with ξ_G p γ_1 = ξ_G p γ_2. Suppose s ↦ Stab_{Mod_G}(γ_1(s)) is locally constant and γ_1(s_0) = γ_2(s_0) for some s_0. Then γ_1 = γ_2.

*Proof.*
- E := {s : γ_1(s) = γ_2(s)} is closed, since T_G is Hausdorff.
- **E is open.** Let s_1 ∈ E, y := γ_1(s_1), and U a slice neighbourhood of y (St1).
  - For s near s_1, both γ_i(s) lie in U. By (St2), γ_2(s) = g_sγ_1(s) for some g_s ∈ Mod_G. Then g_sU ∩ U ≠ ∅, so g_s ∈ Stab(y).
  - By local constancy, Stab(γ_1(s)) = Stab(y) for s near s_1. So g_s fixes γ_1(s), and γ_2(s) = γ_1(s).
- I is connected, so E = I. ∎

**Theorem 7.2 (Theorem LG) [coarse (R2) + (Loc)].** Assume (R2) and (Loc). Then for every boundary stratum G there is a continuous H̃ : Ã_0 × Δ → T_G satisfying (a)–(d). It is unique even among continuous maps satisfying only (a), (c) and (d).

*Proof.*

**1. Construction.** For x ∈ Ã_0 and t ∈ Δ, let γ_{x,t} : [0,1] → T_G be a continuous lift of r ↦ H_{rt}(ξ_G p x) with γ_{x,t}(0) = x and with r ↦ Stab(γ_{x,t}(r)) locally constant. Put H̃_t(x) := γ_{x,t}(1).

**2. Existence of γ_{x,t}.**
- For each τ in the segment {rt : 0 ≤ r ≤ 1}, (Loc) at (x, τ) gives W_τ, I_τ and h^τ. By compactness and a Lebesgue number, there are τ_1, …, τ_k and 0 = r_0 < ⋯ < r_k = 1 with {rt : r ∈ [r_{j−1}, r_j]} ⊂ I_j := I_{τ_j}. Write h^j := h^{τ_j}.
- 0 ∈ I_1. By (L1) and H_0 = id, h^1_0(x) lies over ξ_G p(x), so h^1_0(x) = a x for some a ∈ Mod_G (St2). Replace h^1 by a^{-1}h^1; (L1) and (L2) are preserved, since Stab(a^{-1}y) = a^{-1}Stab(y)a. Now h^1_0(x) = x.
- Put γ(r) := h^1_{rt}(x) on [r_0, r_1].
- Inductively, γ(r_j) and h^{j+1}_{r_j t}(x) lie over the same point, so γ(r_j) = g h^{j+1}_{r_j t}(x) with g ∈ Mod_G. Put γ(r) := g h^{j+1}_{rt}(x) on [r_j, r_{j+1}].
- γ is continuous. By (L2), Stab(γ(r)) is constant on each [r_{j−1}, r_j], and these constants agree at the junctions. So Stab(γ(r)) = Stab(x) for all r.

**3. Uniqueness of γ_{x,t}.** This is Lemma 7.1. In particular:
- H̃ is well defined;
- H̃_{rt}(x) = γ_{x,t}(r), by uniqueness applied to the reparametrised path.

**4. Properties.**
- (a) holds by construction.
- (d): for t = 0 the constant path is the lift.
- (c): Stab(H̃_t x) = Stab(γ_{x,t}(1)) = Stab(x).
- (b): for g ∈ Mod_G, g∘γ_{x,t} lifts the same path (since ξ_G p g = ξ_G p), starts at gx, and has constant stabiliser g Stab(x) g^{-1}. By Lemma 7.1 it equals γ_{gx,t}.
- **Uniqueness of H̃.** Let H̃′ be continuous with (a), (c), (d). Then r ↦ H̃′_{rt}(x) is a lift starting at x, by (d), with constant stabiliser Stab(x), by (c). By Lemma 7.1 it equals γ_{x,t}, so H̃′ = H̃.

**5. Joint continuity at (x_0, t_1).**
- Take the data of step 2 for (x_0, t_1). Absorb the elements g into the h^j, so that γ_{x_0,t_1}(r) = h^j_{rt_1}(x_0) on [r_{j−1}, r_j].
- Each h^j is defined on (W_j ∩ Ã_0) × I_j, with W_j a neighbourhood of x_0. Put W := ⋂_j W_j.
- By compactness there is δ > 0 with rt ∈ I_j for r ∈ [r_{j−1}, r_j] and |t − t_1| < δ.
- Let K := Stab(x_0). By step 2, K = Stab(γ_{x_0,t_1}(r)) for all r. It is finite.

**Claim.** For (x, t) ∈ (W ∩ Ã_0) × Δ close enough to (x_0, t_1) and each j, there is k_j ∈ K with γ_{x,t}(r) = k_j h^j_{rt}(x) on [r_{j−1}, r_j].

*Proof of the claim.*
- **j = 1.** h^1_0(x) = a_x x with a_x ∈ Mod_G. As x → x_0, both x and a_x x = h^1_0(x) tend to h^1_0(x_0) = x_0. So, for x close to x_0, both lie in a slice neighbourhood of x_0, and a_x ∈ K.
  - The path r ↦ a_x^{-1}h^1_{rt}(x) lifts the path, starts at x, and has constant stabiliser. By Lemma 7.1 it equals γ_{x,t} on [0, r_1]. Take k_1 := a_x^{-1}.
- **j → j + 1.** Put y_0 := γ_{x_0,t_1}(r_j) = h^j_{r_jt_1}(x_0) = h^{j+1}_{r_jt_1}(x_0); then Stab(y_0) = K.
  - For (x, t) close to (x_0, t_1), both k_j h^j_{r_jt}(x) and h^{j+1}_{r_jt}(x) lie in a K-invariant slice neighbourhood U of y_0 and over the same point.
  - So they differ by some k′ ∈ Stab(y_0) = K.
  - By Lemma 7.1 on [r_j, r_{j+1}], γ_{x,t} = k′h^{j+1}_{rt}(x) there. Take k_{j+1} := k′.

**Continuity.** H̃_t(x) = k_k h^k_t(x) with k_k ∈ K. As (x, t) → (x_0, t_1), h^k_t(x) → h^k_{t_1}(x_0) = H̃_{t_1}(x_0) =: y_1, and every element of K fixes y_1. Since K is finite, H̃_t(x) → y_1. ∎

**Remark 7.3 ((O-emb) ⇒ (Loc)).** Under (O-emb), at x̂ ∈ Ã_0 and t_0 there are:
- a slice neighbourhood W of x̂;
- injective continuous local lifts h_s : W ∩ Ã_0 → T_G of H_s (s ∈ I);
- an isomorphism φ : Stab(x̂) → Stab(h_{t_0}x̂), **independent of s by the reading**, with h_s(au) = φ(a)h_s(u).

Shrinking W and I, we may assume h((W ∩ Ã_0) × I) ⊂ W′, a slice neighbourhood of h_{t_0}x̂. Then Stab(h_s u) = φ(Stab u) for all s:
- If b ∈ Mod_G fixes h_s(u) ∈ W′, then b ∈ Stab(h_{t_0}x̂), so b = φ(a) with a ∈ Stab(x̂). Then h_s(au) = h_s(u), and au ∈ W, so au = u by injectivity.
- Conversely, if au = u with u ∈ W, then a ∈ Stab(x̂), and φ(a)h_s(u) = h_s(u).

This gives (L2); (L1) is the lifting property.

The independence of φ from s cannot be *deduced* from equivariance: equivariance determines φ_s(a) only modulo the pointwise stabiliser of h_s(W ∩ Ã_0), which may be non-trivial on the 1-dimensional set Ã_0. So it is part of the reading (O-emb).

**Remark 7.4 ((Loc) only near t_0 = 0).**
- The radius of the disc I given by (Loc) at (x̂, 0) may depend on x̂, and Ã_0 is not compact modulo Mod_G. So (Loc) at t_0 = 0 alone does **not** give (a)–(d) on any Ã_0 × Δ_r, and is not known to suffice. This is open.
- If (Loc) holds at all (x̂, t_0) with |t_0| < r for a fixed r > 0, then:
  - Theorem 7.2 gives (a)–(d) over Δ_r;
  - the rescaled family t ↦ V_{rt} satisfies (R1) and (R2^orb) over Δ;
  - Theorem A then gives Y_t = Y_0 for |t| < r, and Lemma 2.3 extends this to Δ.

**Theorem 7.5 (preservation of automorphism orders implies (R2^orb)) [coarse (R2) + (AP); no use of (Loc)].** Assume (R2) and

- **(AP)** |Aut(H_t(z))| = |Aut(z)| for every boundary point z ∈ B_0 and every t ∈ Δ.

Then for every boundary stratum G there is a continuous H̃ : Ã_0 × Δ → T_G satisfying (a)–(d) of §1.3. Conversely, (R2^orb) implies (AP) (Prop. 5.1). Hence, under (R2), **(R2^orb) ⇔ (AP) ⇔ (Loc)**, and Theorem A holds under (R1) + (R2) + (AP).

*Proof.* Fix a boundary stratum G and write P := ξ_G∘p : T_G → Δ_G.

**0. Two facts about P.**
- (P1) P is continuous, surjective and open, and its fibres are the Mod_G-orbits. Indeed p is the quotient map of a group action, hence open; ξ_G is a finite, hence closed, surjective morphism whose fibres are the Aut(G)-orbits (St3, St4), so it is a quotient map whose fibres are orbits of a finite group, hence open; fibres by (St2).
- (P2) Let y ∈ T_G, A := Stab_{Mod_G}(y) (finite), and U a slice neighbourhood of y (St1). Then: (i) P(U) is open and P^{-1}(P(U)) = ⊔_{gA ∈ Mod_G/A} gU, a disjoint union; (ii) every u ∈ U has Stab(u) ⊂ A; (iii) U → P(U) is the quotient by A and is proper (preimages of compact sets are compact); (iv) if |Stab(u)| = |A| for some u ∈ U, then Stab(u) = A, i.e. u ∈ Fix(A); (v) P restricted to Fix(A) ∩ U is a homeomorphism onto P(Fix(A) ∩ U) = {z ∈ P(U) : |Aut(z)| = |A|}.
  - (i): P(U) is open by (P1). If gU ∩ g′U ≠ ∅ then g^{-1}g′ ∈ A, so the translates are disjoint or equal; a point over P(U) is h·u with u ∈ U, so lies in hU.
  - (ii): gu = u ∈ U gives gU ∩ U ≠ ∅, so g ∈ A.
  - (iii): two points of U with the same image are related by some g with gU ∩ U ≠ ∅, so g ∈ A. Properness: a finite group quotient map is proper.
  - (iv) follows from (ii), since the groups are finite.
  - (v): P is injective on Fix(A) ∩ U, because two points of U with the same image differ by an element of A, which fixes both. Fix(A) ∩ U is closed in U and A-saturated, and the quotient map U → U/A ≅ P(U) is closed, so its restriction to Fix(A) ∩ U is a closed continuous injection, i.e. a homeomorphism onto its image. By Lemma 2.5, |Aut(P(u))| = |Stab(u)|; so by (ii) and (iv) a point z ∈ P(U) has |Aut(z)| = |A| iff its lift in U lies in Fix(A).

**1. Path lifting at constant automorphism order.** Let c : [0,1] → Δ_G be continuous with |Aut(c(r))| = k for all r, and let x ∈ P^{-1}(c(0)). Then there is exactly one continuous γ : [0,1] → T_G with P∘γ = c and γ(0) = x. Moreover Stab(γ(r)) = Stab(x) for all r.
- *Local sections.* For r_* ∈ [0,1], pick y ∈ P^{-1}(c(r_*)), its stabiliser A (|A| = k by Lemma 2.5) and a slice U. By (P2)(v), σ := (P|_{Fix(A)∩U})^{-1} is a continuous section of P over the set {z ∈ P(U) : |Aut z| = k}, which contains c(r) for all r in an open interval J_{r_*} ∋ r_*. Replacing y by gy replaces U by gU and σ by gσ, with the same domain; so J_{r_*} depends only on r_*. Moreover, for every r ∈ J_{r_*} and every x′ ∈ P^{-1}(c(r)), the points over c(r) form the single orbit Mod_G·σ(c(r)) (P1), so x′ = gσ(c(r)) for some g ∈ Mod_G, and gσ is a continuous section of P over the same domain passing through x′.
- *Existence.* Choose 0 = r_0 < ⋯ < r_m = 1 such that each [r_{l−1}, r_l] lies in some J_{r_*} (Lebesgue number). Lift successively: if [r_{l−1}, r_l] ⊂ J_{r_*}, use on [r_{l−1}, r_l] a translate gσ of the section attached to r_* that passes through the already constructed point over c(r_{l−1}) (it exists by the previous item, applied with r = r_{l−1} ∈ J_{r_*}). The pieces agree at the junctions by construction.
- *Constant stabiliser.* Near any r_1, γ(r) lies in a slice U of γ(r_1) and has stabiliser of order k = |Stab(γ(r_1))|, hence equal to Stab(γ(r_1)) by (P2)(iv). So r ↦ Stab(γ(r)) is locally constant, hence constant.
- *Uniqueness* is Lemma 7.1, whose hypothesis (locally constant stabiliser) has just been checked for any such lift.

**2. Definition of H̃.** For x ∈ Ã_0 and t ∈ Δ, the path c_{x,t}(r) := H_{rt}(P(x)), r ∈ [0,1], is continuous, lies in Δ_G because H preserves strata (R2), and has constant automorphism order |Aut(P(x))| by (AP). Let γ_{x,t} be its lift from step 1 with γ_{x,t}(0) = x, and put H̃_t(x) := γ_{x,t}(1). Since c_{x,t} lies in A^G_{rt}, γ_{x,t}(1) ∈ Ã_t.
- (a): P(H̃_t x) = c_{x,t}(1) = H_t(P x).
- (d): for t = 0 the path is constant, and so is its lift.
- (c): Stab(H̃_t x) = Stab(γ_{x,t}(1)) = Stab(x) by step 1.
- (b): for g ∈ Mod_G, g∘γ_{x,t} is a lift of the same path c_{x,t} = c_{gx,t} (as P(gx) = P(x)), starting at gx. By uniqueness it is γ_{gx,t}, so H̃_t(gx) = gH̃_t(x).

**3. Joint continuity at (x_0, t_1).** Let γ_0 := γ_{x_0,t_1} and K := Stab(x_0) = Stab(γ_0(r)) for all r (step 1).
- For each r, choose a slice neighbourhood U(r) of γ_0(r) (St1). By (St1), "slice neighbourhood of y" depends on y only through Stab(y): it is a Stab(y)-invariant open set containing y with gU ∩ U ≠ ∅ ⇒ g ∈ Stab(y). Since every γ_0(r) has the same stabiliser K, **each U(r) is a slice neighbourhood of every point γ_0(r′) it contains.** By a Lebesgue-number argument for the open cover {γ_0^{-1}(U(r))}_r of [0,1], there are 0 = r_0 < ⋯ < r_m = 1 and, for each j < m, some r′_j with γ_0([r_j, r_{j+1}]) ⊂ U_j := U(r′_j); by the observation just made, U_j is a slice neighbourhood (with group K) of both γ_0(r_j) and γ_0(r_{j+1}), and (P2)(i), (iii) apply to it with A = K. Also let U_m be a slice neighbourhood of γ_0(1).
- The map (z, s) ↦ H_s(z) is continuous, so c_{x,t} → c_{x_0,t_1} uniformly on [0,1] as (x, t) → (x_0, t_1). Since c_{x_0,t_1}([r_j, r_{j+1}]) is a compact subset of the open set P(U_j) ⊂ Δ_G (write P(U_j) = O_j ∩ Δ_G with O_j open in M̄_g; the compact set has positive distance from M̄_g ∖ O_j, and every c_{x,t} lies in Δ_G), for (x, t) close to (x_0, t_1) we have c_{x,t}([r_j, r_{j+1}]) ⊂ P(U_j) for all j.
- **Induction.** Let (x_n, t_n) → (x_0, t_1) with x_n ∈ Ã_0, and γ_n := γ_{x_n,t_n}. We show γ_n(r_j) → γ_0(r_j) for j = 0, …, m. For j = 0 this is x_n → x_0. Assume it for j < m. For large n, γ_n(r_j) ∈ U_j, and γ_n([r_j, r_{j+1}]) is a connected subset of P^{-1}(P(U_j)) = ⊔ gU_j (disjoint open sets, (P2)(i)) meeting U_j; hence γ_n([r_j, r_{j+1}]) ⊂ U_j. The points γ_n(r_{j+1}) ∈ U_j lie over c_{x_n,t_n}(r_{j+1}) → c_{x_0,t_1}(r_{j+1}) = P(γ_0(r_{j+1})). By properness of U_j → P(U_j) ((P2)(iii)), every subsequence has a further subsequence converging to a point of U_j over P(γ_0(r_{j+1})), i.e. to a point of the K-orbit of γ_0(r_{j+1}); since K fixes γ_0(r_{j+1}), that point is γ_0(r_{j+1}). So γ_n(r_{j+1}) → γ_0(r_{j+1}).
- For j = m this gives H̃_{t_n}(x_n) → H̃_{t_1}(x_0). T_G is metrisable, so H̃ is continuous.

**4. The equivalences.** (R2^orb) ⇒ (AP) is Prop. 5.1 (which uses only (a), (c) and Lemma 2.5). (R2) + (AP) ⇒ (R2^orb) is steps 0–3. (R2) + (Loc) ⇒ (R2^orb) is Theorem 7.2, and (R2^orb) ⇒ (Loc) with h := H̃. Theorem A (§9) uses only (R1) and (a)–(d). ∎

*Remark 7.6 (what Theorem 7.5 changes).*
- The orbifold reading is now a single, checkable condition on the coarse trivialisation: H_t must not change the order of the automorphism group of any boundary point. The difference between the coarse reading (R2) and (R2^orb) is exactly the possibility of **isotropy change** at boundary points along the family (drop, as in the chart model of §8.2, or rise).
- (AP) is only needed on a disc: if (AP) holds for |t| < r, apply Theorem 7.5 and Theorem A to the rescaled family t ↦ V_{rt}, and extend by Lemma 2.3.
- In particular, by Corollary C.5 below, the claim holds under (R1) + (R2) whenever no point of B_0 has a non-trivial automorphism, and more generally under the local criterion of Theorem C.7. (Self-contained argument for the first statement: by (Kur), |Aut| is upper semicontinuous on M̄_g, so {z : Aut(z) = 1} is an open set containing the compact set B_0; by continuity of H and H_0 = id, H_t(B_0) stays in it for |t| < r, so (AP) holds on Δ_r.)

---

## II.8. Discussion: what (R2^orb) buys, and the coarse reading

### 8.1 Dependency table

| Result | Hypotheses on the family | Other inputs |
|---|---|---|
| Lemma 1.1, Def. 1.2 | none | (Kur) |
| Lemma 2.1 | (R1) | Chow, (Irr) |
| Lemma 2.2 | none | — |
| Lemma 2.3 | (R1), (R2) | Remmert, (Cl), normalisation |
| Lemma 2.4 | none | (CG) |
| Lemma 2.5 | none | (Iso) |
| Lemma 3.1 | (R2^orb): (a), (b), (c) "⊂", (d) | (St), Lemmas 2.1, 2.4 |
| Lemma 4.1 | via Lemma 3.1 | (Unif), lifting criterion |
| Prop. 4.2 | (a), (b) for Mod_Π, via Lemma 3.1 | I.2, J0, CL |
| Lemma 4.3 | via Prop. 4.2 | (Roy), (VT), (Bers), (Sel), (Th), (Cent), (Dens) |
| Theorem 4.4(a) | via Lemma 4.3 | (TF), (KP1), (BE) |
| Theorem 4.4(b), Cor. 4.5 | via 4.4(a) | Lemma F0 for genus 0; Lemma F1 (from (IS_c), (BC), (TF)) for genus ≥ 1 |
| Prop. 5.1, 5.2 | (a), (c) | Lemma 2.5, (Kur) |
| Lemma 6.1(1),(2) | (R1), (R2) | (Kur), Lemma 1.1 |
| Lemma 6.1(3)–(5) | via Lemma 3.1, Prop. 5.2 | (PN) |
| Prop. 6.2 | via 6.1, 4.4(a) | (PN3), (K2) |
| Prop. 6.3 | via 6.1, Cor. 4.5 | (PN2) |
| Theorem A | (R1), (R2^orb) | I.2, I.3, I.5, I.6 |
| Lemma 7.1 | none | (St) |
| Theorem 7.2 | (R2), (Loc) | (St) |

### 8.2 The coarse reading admits isotropy drop (chart-level model)
This model shows that (R2^orb) is strictly stronger than (R2), and that (O-int) does not imply (c).
- At a boundary point Q, take stratum coordinates (u, v) on Def(Q)^{G_Q}. Let σ ∈ Aut(Q) act by u ↦ −u, fixing v.
- The coarse coordinates are (U, v) with U = u², so the coarse chart is smooth.
- Let B_0 contain, near Q, the curve {u = 0}. Each of its points carries the extra automorphism σ.
- H_t(U, v) := (U + t², v) is a holomorphically varying, stratum-preserving trivialisation. So (R2) holds at chart level.
- For t ≠ 0, the transported curve is {u = ±t}, on which σ acts freely. So |Aut(H_t z)| < |Aut(z)|, and (c) fails.
- No continuous lift with (a) and (c) exists, by counting stabiliser orders.
- (O-int) holds: σ fixes {u = 0} pointwise, so the intrinsic (effective) isotropy is trivial both before and after transport.
- Whether a **global** family satisfying (i), (ii) and such an isotropy drop at the boundary exists is open.

### 8.3 Where the proof breaks under (R2) alone
1. **Prop. 5.2.** q^{-1}(J_t) ∩ B may consist of several points (the lift-curves), permuted by Aut(J) and not individually Aut(J)-fixed. Then the two applications of Prop. 6.2 at J_m in §9.2 may concern **different** lifts p(t) ≠ p′(t) = a·p(t). One only gets [φ_{m+1}(t)] = [comp_{a^{-1}x_m}(p(t))]: the twin problem.
2. **Lemma 3.1 in non-product strata.** Without a continuous bijective lift Π_t, a constant vertex of a piece cannot be followed to a well-defined piece at time t, and (Rig) is not available.

Both obstructions are exactly the isotropy change of §8.2. This is now a theorem: by Theorem 7.5, under (R2) the failure of (R2^orb) is equivalent to the failure of (AP). The coarse-valid lemmas used for the coarse reading (Part III) are proved in Appendix A.

---

## II.A. Appendix A: coarse-valid lemmas (not used in the proof of Theorem A; Lemmas A.5, A.6 are used in Part III)

These are proved under the weakest hypotheses their proofs allow. Labels:
- [coarse] = (R1), (R2);
- [coarse+P] = in addition (P) for the branch considered;
- [coarse+Rig] = in addition (Rig);
- [+Ync] = in addition "t ↦ [Y_t] is non-constant".

**(Rig)** means: there is a finite set 𝒦 of triples (G, M, K) — G a boundary stratum, M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible curve — such that every piece E at every time t, in every stratum, has (G, M(E), K(E)) ∈ 𝒦 up to relabelling by Aut(G). Under (R2^orb), (Rig) holds by Theorem 4.4, with 𝒦 := {(G, M(E), K(E)) : E a piece at time 0}.

**Setting A.0.**
- J ∈ B_0, b a branch at J with lift b̃, Ñ := Ñ_b̃ as in Setting 6.0. Only items (i), (ii) and (iv) of Setting 6.0 are used; item (iii) (Prop. 5.2) is not.
- Γ_J := {(J_t, t) : |t| < ε}.
- 𝒥 := {(p, t) ∈ B × Δ_ε : q(p) = J_t}, the lift locus. A **lift-curve** is an irreducible component of the germ of 𝒥 at (0,0).
- An **anchored sheet** (= b̃-sheet) is an irreducible component T of closure(Ñ) (closure in B × Δ_ε) with b̃ × {0} ⊂ T.
- For a vertex y of G_J and an analytic set T ⊂ B × Δ_ε, put A_y(T) := {(p, t) ∈ T : p ∈ L_y, [comp_y(p)] = [Y_t]}. Then:
  - y is **Y-persistent on T** (y ∈ P(T)) if A_y(T) = T;
  - for a lift-curve L, C(L) := {y : A_y(L) = L}.
- Ω denotes a small open neighbourhood of (J, 0) in M̄_g × Δ_ε with Ω ∩ ℬ ⊂ H((B_0 ∩ U) × Δ_ε), where U is as in Setting 6.0(iv). It exists by continuity of H^{-1} at (J, 0).

**Fact (Cl′) [none].** Let X be an analytic set, Z ⊂ X a closed analytic subset, and C a union of connected components of X ∖ Z. Then closure(C) is the union of those irreducible components X_l of X, not contained in Z, for which X_l ∖ Z ⊂ C. In particular closure(C) is analytic.

*Proof.*
- For X_l ⊄ Z, the set X_l° := X_l ∖ (Z ∪ Sing X ∪ ⋃_{l′≠l} X_{l′}) is connected and dense in X_l. (Fact (Reg): the regular locus of an irreducible analytic set is a connected manifold, and a proper analytic subset does not disconnect it.)
- X_l ∖ Z lies between X_l° and its closure, so it is connected. Hence each X_l ∖ Z lies in a single component of X ∖ Z.
- X ∖ Z = ⋃_l (X_l ∖ Z), so C is the union of the X_l ∖ Z that it contains. Their closures are the X_l. ∎

**Fact (TrQ) [none].** Let a finite group A act on a complex manifold germ, with quotient map π, and let X be an irreducible germ in the quotient. Then A permutes the irreducible components of π^{-1}(X) transitively.

*Proof.* Let Y be one component. A·Y is analytic and A-invariant. π(A·Y) is analytic (Remmert), of dimension dim X and contained in X, hence equal to X. So π^{-1}(X) = π^{-1}(π(A·Y)) = A·Y. ∎

**Lemma A.1 (transport families) [coarse+P].** Assume (P) for b. Then, inside Ω:
1. H(b × Δ_ε) = N ⊔ Γ_J is a closed analytic set of pure dimension 2. It is irreducible after shrinking Ω.
2. Γ_J is a closed analytic curve, and t ↦ J_t is holomorphic on Δ_ε. 𝒥 is a closed analytic subset of B × Δ_ε, of dimension ≤ 1, with 𝒥 ∩ {t = 0} = {(0,0)}.
3. closure(Ñ) is analytic of pure dimension 2, and closure(Ñ) ⊂ Ñ ∪ 𝒥.

*Proof.*
1. **Analyticity and dimension.**
   - Let 𝒜 := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ_ε), which is analytic by (R1). Let 𝒵 ⊂ 𝒜 be its closed analytic part over closure(Δ_{G_b}) ∖ Δ_{G_b}.
   - In Ω, 𝒜 ∖ 𝒵 = ⊔_k N_k, where N_k := H((b_k ∖ J) × Δ_ε) and b_k runs over the branches at J with b_k ∖ J ⊂ Δ_{G_b}. (J ∉ Δ_{G_b} by (P).)
   - Each N_k is open in 𝒜 ∖ 𝒵, because H is a homeomorphism. So N = N_1 is open and closed there.
   - By (Cl′), closure(N) ∩ Ω is a union of irreducible components of 𝒜 ∩ Ω. Each contains a non-empty open subset of the topological 4-manifold N, so each has dimension 2.
   - Since b × Δ_ε is closed and H is a homeomorphism onto the closed set closure(𝒱), closure(N) ∩ Ω = H(b × Δ_ε) ∩ Ω = (N ∪ Γ_J) ∩ Ω.
   - **Irreducibility.** N ∖ Sing(closure N) is connected, since Sing has real dimension ≤ 2 in the 4-manifold N (Hurewicz–Wallman, (HW)). So it lies in the regular part of a single component, and is dense.
2. **Γ_J.**
   - N ⊂ Δ_{G_b} × Δ, and Δ_{G_b} ∩ closure(Δ_{G_J}) = ∅, because G_b is a proper contraction of G_J.
   - So Γ_J = closure(N) ∩ (closure(Δ_{G_J}) × Δ_ε) ∩ Ω is analytic. The projection t : Γ_J → Δ_ε is a homeomorphism, and as in Lemma 2.3(4), t ↦ J_t is holomorphic.
   - 𝒥 = (q × id)^{-1}(Γ_J) is analytic and finite over Γ_J, so dim 𝒥 ≤ 1. Also 𝒥 ∩ {t = 0} = q^{-1}(J) × {0} = {(0,0)}.
3. **closure(Ñ).**
   - q is open, so closure(q^{-1}(N)) = q^{-1}(closure N) = q^{-1}(N) ∪ 𝒥.
   - Ñ is a component of the locally connected space q^{-1}(N) (proof of Lemma 6.1(1)), so it is open and closed there. Hence closure(Ñ) ⊂ Ñ ∪ 𝒥.
   - Apply (Cl′) with X := q^{-1}(closure N), Z := 𝒥 and C := Ñ: closure(Ñ) is a union of components X_l of X.
   - **Pure dimension 2.** For each such X_l, the set X_l ∖ (𝒥 ∪ other components) is open in Ñ. Its image under the open map q|_{q^{-1}(N)} is open in the 4-manifold N. So dim q(X_l) = 2, hence dim X_l = 2. ∎

**Lemma A.2 (anchored sheets) [coarse+P].** Assume (P) for b, and let T be an irreducible component of closure(Ñ).
- (a′) q(T) = H(b × Δ_ε) ∩ Ω, (0,0) ∈ T, and t is non-constant on T. Moreover T ∩ {t = 0} is a union of lifts a b̃ (a ∈ Aut(J)), each satisfying (a b̃ ∖ 0) × {0} ⊂ Ñ and aS_b̃ = S_b̃.
- (a″) Anchored sheets exist. For every p̃ ∈ b̃ ∖ 0, every irreducible component of the germ of closure(Ñ) at (p̃, 0) lies in an anchored sheet, and every anchored sheet contains such a germ component.
- (b′) The pointwise stabiliser Stab_pt(b̃) := {a ∈ Aut(J) : a|_b̃ = id} permutes the anchored sheets transitively.

*Proof.*
1. **(a′).**
   - q is finite on B × Δ_ε, so q(T) is an irreducible 2-dimensional analytic subset (Remmert) of the irreducible H(b × Δ_ε) (Lemma A.1(1)), hence equal to it.
   - (J, 0) ∈ q(T) and q^{-1}(J) = {0}, so (0,0) ∈ T.
   - If t were constant on T, T would lie in closure(Ñ) ∩ {t = 0} ⊂ q^{-1}(b) × {0}, which has dimension 1. So t is non-constant on T, and by Krull, T ∩ {t = 0} is of pure dimension 1 at each of its points.
   - T ∩ {t = 0} ⊂ q^{-1}(b) ∩ B = ⋃_a a b̃, and each a b̃ ∩ B is irreducible. So T ∩ {t = 0} is a union of some of the a b̃.
   - Since 𝒥 ∩ {t = 0} = {(0,0)} and T ⊂ Ñ ∪ 𝒥, we get (a b̃ ∖ 0) × {0} ⊂ Ñ. The pattern is constant (= S_b̃) on Ñ (Lemma 6.1(2)), and equals aS_b̃ on a b̃ ∖ 0. So aS_b̃ = S_b̃.
2. **(a″).**
   - b̃ × {0} ⊂ closure(Ñ) is an irreducible curve, so it lies in a component: an anchored sheet exists.
   - A germ component at (p̃, 0) of closure(Ñ) lies in exactly one global component T, because two distinct components meet in dimension ≤ 1. By (a′), T ∩ {t = 0} is a union of lifts containing p̃. For B small, distinct lifts meet only at 0, so this union contains b̃, and T is anchored.
   - Conversely, an anchored sheet contains (p̃, 0), so its germ there contains a germ component.
3. **(b′).**
   - Choose p̃ ∈ b̃ ∖ 0 with Stab_{Aut(J)}(p̃) = Stab_pt(b̃). This excludes, for each a ∉ Stab_pt(b̃), the discrete set of its fixed points on b̃.
   - Near p̃, q is the quotient by Stab(p̃) (Kur). Near (q(p̃), 0), the set H(b × Δ_ε) is the topological 4-manifold N. Its germ is irreducible: otherwise removing the ≤ 1-dimensional intersection of two components would disconnect a punctured neighbourhood, contradicting (HW).
   - By (TrQ), Stab(p̃) permutes the germ components of closure(Ñ) at (p̃, 0) transitively. Near (p̃, 0), closure(Ñ) coincides with q^{-1}(N).
   - Every a ∈ Stab_pt(b̃) maps Ñ to the component of q^{-1}(N) containing a(b̃ ∖ 0) = b̃ ∖ 0, i.e. to Ñ. So it maps anchored sheets to anchored sheets.
   - If T and T′ are anchored sheets with germ components g ⊂ T and g′ ⊂ T′ at (p̃, 0), choose a with ag = g′. Then aT ⊃ g′, so aT = T′. ∎

**Lemma A.3 (anchored sheets contain a lift-curve) [coarse+P].** Assume (P) for b. Then every anchored sheet T contains a lift-curve.

*Proof.*
1. **Points of T away from 𝒥 and {t = 0}.** T is of pure dimension 2 at (0,0), and T ∩ (𝒥 ∪ {t = 0}) has dimension ≤ 1. So there are (p_n, t_n) ∈ T ∖ (𝒥 ∪ {t = 0}) converging to (0,0).
   - By Lemma A.1(3), (p_n, t_n) ∈ Ñ, so q(p_n) ∈ H_{t_n}(b ∖ J).
   - Put z_n := H_{t_n}^{-1}(q(p_n)) ∈ b ∖ J. Then z_n → J by continuity of H^{-1}.
2. **Arcs.** Parametrise b by a closed disc centred at J, and let α_n be the radial segment from z_n to J.
   - By uniform continuity of H on b × closure(Δ_{ε′}), H_{t_n}(α_n) → {J}.
   - So for large n, H_{t_n}(α_n) ⊂ q(B″), where B″ ⋐ B is a smaller invariant ball with p_n ∈ B″.
3. **The image of a component reaches J_{t_n}.**
   - Let C be an irreducible component through p_n of the analytic curve T_{t_n} ∩ B″ (pure 1-dimensional by Krull). Then q(C) is an irreducible analytic curve, closed in q(B″) (Remmert, q|_{B″} proper).
   - q(C) lies in Z := H_{t_n}(b) ∩ q(B″), which is analytic (the t_n-slice of Lemma A.1(1)). Indeed q(T_{t_n}) ⊂ H_{t_n}(b ∖ J) ∪ {J_{t_n}}, since T ⊂ Ñ ∪ 𝒥.
   - At each w ∈ H_{t_n}(α_n ∖ J), Z is homeomorphic to a disc near w, hence locally irreducible.
   - Let O be the set of such w near which q(C) contains a neighbourhood of w in Z.
     - O ∋ q(p_n): the 1-dimensional germ of q(C) at q(p_n) lies in the irreducible germ of Z there, hence equals it.
     - O is open in the arc.
     - O is closed in the arc: a limit point w lies in the closed set q(C), and the same germ argument applies.
   - So O is the whole connected arc. Since J_{t_n} lies in its closure and q(C) is closed in q(B″), J_{t_n} ∈ q(C).
4. **Conclusion.**
   - There is p′_n ∈ C with q(p′_n) = J_{t_n}, i.e. (p′_n, t_n) ∈ T ∩ 𝒥. By properness and q^{-1}(J) = {0}, p′_n → 0.
   - So (0,0) is not isolated in the analytic set T ∩ 𝒥, and this set contains an irreducible curve germ at (0,0).
   - That germ is a component of the germ of 𝒥, since dim 𝒥 ≤ 1. ∎

*Complement to Lemma A.2(b′).* The claim "near (p̃, 0), closure(Ñ) coincides with q^{-1}(N)" holds for the following reasons.
- 𝒥 is closed and meets {t = 0} only at (0,0).
- By the local conic structure of analytic sets, every point of q^{-1}(N) close to (p̃, 0) is joined to (p̃, 0) ∈ Ñ inside q^{-1}(N). Hence it lies in Ñ.

**Global objects for the remaining lemmas.**
- ℬ := closure(𝒱) ∩ (∂M̄_g × Δ). It is analytic by (R1) and equals H(B_0 × Δ) by (R2). It has dimension ≤ 2.
- For a stratum G, ℬ_G := ℬ ∩ (Δ_G × Δ).
- A **coarse piece** is a 1-dimensional irreducible component D of B_0 ∩ Δ_G, for some G; we put D_t := H_t(D). By the argument of Lemma 2.1, applied in M̄_g, the analytic set B_0 is algebraic, has finitely many coarse pieces, and has a finite singular set.

**Lemma A.4 (transport respects components) [coarse].** Let D be a coarse piece in Δ_G.
- (a) There is a unique irreducible component κ(D) of ℬ_G with H(D × Δ) ⊂ κ(D).
- (b) Every irreducible component 𝒲 of ℬ_G satisfies 𝒲 = ⋃_{κ(D)=𝒲} H(D × Δ).

*Proof.*
1. Let D° be D minus the finitely many singular points of B_0 ∩ Δ_G. D° is connected, being the image of the connected normalisation of D minus a finite set, and it is a real 2-manifold. So D° × Δ is a connected 4-manifold.
2. Σ := Sing(ℬ_G) has covering dimension ≤ 2, and so does H^{-1}(Σ) ∩ (D° × Δ).
3. By (HW), R := (D° × Δ) ∖ H^{-1}(Σ) is connected. H(R) is a connected subset of Reg(ℬ_G), so it lies in one component κ(D).
4. R is dense in D × Δ, and κ(D) is closed. So H(D × Δ) ⊂ κ(D). Uniqueness: H(R) ⊄ Σ.
5. For (b), let x ∈ 𝒲 lie on no other component. Then x = H(e, t) with e in some coarse piece D′, or e an isolated point of B_0 ∩ Δ_G.
   - In the second case, H({e} × Δ) is a curve of real dimension 2. The points of 𝒲 on no other component form a set of real dimension 4, so the first case occurs on a dense subset.
   - By (a), κ(D′) = 𝒲. So a dense subset of 𝒲 lies in the set ⋃_{κ(D′)=𝒲} H(D′ × Δ), which is closed because it is a finite union of images of closed sets under the homeomorphism H. ∎

**Lemma A.5 (fibres of the lifted families) [coarse].** For a boundary stratum G, let 𝓦_G be the union of those irreducible components of (ξ̄_G × id)^{-1}(closure(𝒱) ∩ (closure(Δ_G) × Δ)) ⊂ ∏_w M̄_w × Δ that are not contained in the preimage of the deeper strata. Then:
- 𝓦_G is closed analytic and proper over Δ;
- 𝓦_G ∩ (∏_w M_w × Δ) = Â;
- for every 2-dimensional irreducible component W of 𝓦_G and every t ∈ Δ, the fibre W_t is non-empty and of pure dimension 1, and each irreducible component of W_t is the closure in ∏_w M̄_w of a piece at time t.

*Proof.*
1. **Closedness, properness, and the open part.** By (Cl′), 𝓦_G = closure(Â), and Â is closed in ∏_w M_w × Δ. Properness follows from compactness of ∏_w M̄_w.
2. **The deeper part of each fibre is finite.**
   - (ξ̄_G × id)(𝓦_G) ⊂ closure(ℬ_G) = H(closure(A_0) × Δ), using that H is a closed embedding.
   - closure(A_0) ∖ A_0 is finite: it consists of the finitely many points added to the closures of the finitely many curves of A_0 (Lemma 2.1).
   - So the part of W_t over deeper strata is finite, since ξ̄_G is finite.
3. **Fibres.** dim W_t ≤ 1, so t is non-constant on W. t|_W is proper, so its image is a closed analytic subset of Δ of dimension 1, i.e. Δ. By Krull, each W_t is of pure dimension 1.
4. **Components.** Let D be a component of W_t. Then D ∩ ∏_w M_w is D minus a finite set, hence an irreducible curve in Â_t. It lies in a piece E, and since it is closed and 1-dimensional, it equals E. So D = closure(E). ∎

**Lemma A.6 (Lemma U) [coarse+Rig].** Let W be a 2-dimensional irreducible component of some 𝓦_G. Then there are M_W ⊂ V(G) and an irreducible curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, such that for every t and every component D = closure(E) of W_t:
- M(E) = M_W and K(E) = K_W;
- every u ∉ M_W is constant on E;
- D = K_W × {c_D} for some c_D ∈ ∏_{u∉M_W} M_u.

*Proof.*
1. **Step 1 (generic moving set).**
   - Let n : W^ν → W be the normalisation, a normal surface. Let W^ν →^a T →^{b′} Δ be the Stein factorisation (SF) of t∘n, which is proper. Then T is a normal curve, hence smooth, and b′ is finite.
   - The critical values of a are discrete. Critical curves of a on Reg W^ν are contracted by a, and Sing W^ν is discrete (normal surfaces have isolated singularities).
   - So for τ outside a discrete set, a^{-1}(τ) is a smooth compact connected curve, hence irreducible.
   - For every t, W_t = ⋃_{τ ∈ b′^{-1}(t)} n(a^{-1}(τ)). For t outside a discrete set the components of W_t are exactly the curves n(a^{-1}(τ)).
   - For a vertex u let Φ_u := (pr_u∘n, a) and R_u := {x : dim_x Φ_u^{-1}Φ_u(x) ≥ 1}, which is analytic by Cartan–Remmert (CR).
     - If R_u = W^ν, then pr_u is constant on every component of every fibre of a, hence on every component of every W_t.
     - Otherwise dim R_u ≤ 1. Fibre components on which pr_u is constant lie in R_u, so this happens only for τ in a discrete set.
   - Put M_W := {u : R_u ≠ W^ν}. There is a discrete Z_W ⊂ Δ such that for t ∉ Z_W every component of W_t has moving set exactly M_W. For every t, every u ∉ M_W is constant on every component.
2. **Step 2 (one curve; uses (Rig)).**
   - Σ := (pr_{M_W}, t)(W) is closed, analytic and irreducible (Remmert), and has dimension 2.
   - For t ∉ Z_W, Σ_t is the union of the curves K(E), and by (Rig) these lie in the finite list K_1, …, K_N (relabellings included). So Σ ∩ {t ∉ Z_W} ⊂ ⋃_j K_j × Δ, and by closedness Σ ⊂ ⋃_j K_j × Δ.
   - Σ is irreducible of dimension 2, so Σ = K_j × Δ for one j. Put K_W := K_j.
   - Each pr_u (u ∈ M_W) is non-constant on K_W.
3. **Step 3 (all times).** Let D = closure(E) be a component of W_t.
   - The u ∉ M_W are constant on D.
   - pr_{M_W}(D) ⊂ Σ_t = K_W is closed and irreducible, and it is not a point (else D would be a point). So pr_{M_W}(D) = K_W.
   - Hence M(E) = M_W, K(E) = K_W, and D = K_W × {c_D}, with c_D ∈ ∏ M_u since the constant values on E lie in M_u. ∎

*Lemma S, parts (b) and (c), as consequences.*
- For u ∉ M_W, (pr_u, t)(W) is an irreducible curve, finite over Δ. Its fibre over t is the finite set of values of u on the components of W_t.
- If, for a vertex x ∉ M_W, the analytic set {[pr_x] = [Y_t]} ⊂ W has real dimension 4, then it is all of W.

**Lemma A.7 (the Y-locus is analytic) [coarse].** Ŷ := {(Q, t) ∈ M̄_g × Δ : Q has a smooth component which, with its special points, has class [Y_t]} is a closed analytic subset of M̄_g × Δ.

*Proof.*
- For a stable graph G and a vertex v of type (g_i, n_i), put A_{G,v} := {(z, t) ∈ ∏_w M̄_w × Δ : [z_v] = [Y_t]}. This is the preimage of the graph of the holomorphic map t ↦ [Y_t] (Lemma 2.3), so it is closed analytic. It forces z_v ∈ M_v.
- (ξ̄_G × id)(A_{G,v}) is closed analytic, since ξ̄_G is finite (Remmert).
- Ŷ is the finite union of these images.
  - ⊆: take G := G_Q and z the normalised components of Q.
  - ⊇: the smooth factor z_v is an irreducible component of ξ̄_G(z), and its special points there are its n_v marked points. ∎

**Lemma A.8 (dichotomy for coarse pieces) [coarse].** Let D be a coarse piece. Exactly one of the following holds.
- (N) For every t, every point of H_t(closure D) has a component of class [Y_t].
- (F) There is a countable Z_D ⊂ Δ such that, for t ∉ Z_D, only finitely many points of H_t(closure D) have such a component.

*Proof.*
1. Let D° be D minus the finitely many singular points of B_0. D° is connected and open in B_0. So M_D := H(D° × Δ) is open in ℬ and is a connected 4-manifold.
2. By (HW), M_D ∖ Sing(ℬ) is connected. So M_D lies in one irreducible component W of ℬ.
3. 𝓝 := Ŷ ∩ ℬ is analytic (Lemma A.7).
4. If W ⊂ 𝓝, then (N) holds, because 𝓝 is closed and H_t(closure D) = closure(H_t D°).
5. Otherwise dim(W ∩ 𝓝) ≤ 1. Its components form a countable, locally finite family. Let Z_D be the set of t such that some component lies in the fibre over t.
   - For t ∉ Z_D, (W ∩ 𝓝)_t is discrete and compact, hence finite.
   - Together with the finite set H_t(closure D ∖ D°), this gives (F).
6. (N) and (F) exclude each other, since H_t(closure D) is infinite. ∎

Let 𝒩 be the set of coarse pieces with (N).

**Theorem A.9 (generic-time dichotomy) [coarse+Rig+Ync].** Define:
- 𝒫 := ⋃_{(G,M,K)∈𝒦} (K ∩ ∂), over all relabellings, which is finite;
- F′_𝒦 := the set of classes of the smooth components, with special points, of the coordinates of points of 𝒫;
- Z := ⋃_{D∉𝒩} Z_D ∪ {t : [Y_t] ∈ F′_𝒦}, which is countable (the second set is discrete, because [Y] is holomorphic and non-constant).

Let t ∉ Z, Q ∈ B_t, and let y be a vertex of G_Q with [comp_y(0)] = [Y_t] in a chart Def(Q). Let b be a branch of B_t at Q, with lift b̃ and pattern S. Then y is intact for S, and exactly one of the following holds.
- **(STAY)** comp_y is constant along b̃, and the coarse piece D′ with H_t^{-1}(b ∖ Q) ⊂ D′ lies in 𝒩.
- **(IMOV)** S = E(G_Q), and [comp_y] is non-constant along b̃.

*Proof.*
1. **Setting up.** Choose ι : G_S → G_b. Shrinking b̃, the set Π_{S,ι}(b̃ ∖ 0) lies in a single piece E at time t (Lemma 2.1 at time t). Put κ := Π_{S,ι}(0), which is the limit of Π_{S,ι} along b̃ (PN). Let u := ι([y]).
2. **Merge is impossible.** Suppose an edge at y is not in S.
   - By (PN2), κ_u is nodal, so by Lemma 2.2, u ∈ M(E) and pr_{M(E)}κ ∈ K(E) ∩ ∂ ⊂ 𝒫.
   - comp_y(0), with its special points, is a component of κ_u. So [Y_t] ∈ F′_𝒦, contradicting t ∉ Z.
3. **Puncture-move is impossible.** Suppose y is intact, S ≠ E(G_Q), and [comp_y] is non-constant along b̃.
   - Then u = {y} ∈ M(E).
   - κ has a nodal coordinate, coming from an edge outside S. So pr_{M(E)}κ ∈ 𝒫 and κ_u = comp_y(0). Again [Y_t] ∈ F′_𝒦, a contradiction.
4. **The constant case.** If y is intact and comp_y is constant along b̃, then every point of b near Q has a component of class [Y_t].
   - Since b ∖ Q ⊂ H_t(D′), H_t(closure D′) has infinitely many such points. As t ∉ Z_{D′}, Lemma A.8 gives D′ ∈ 𝒩.
5. **Otherwise** y is intact, comp_y is non-constant, and S = E(G_Q): this is (IMOV). ∎

**Lemma A.10 (persistence is read off a lift-curve) [coarse+Rig+Ync+P].** In Setting A.0 with (P) for b, let T be an anchored sheet and L ⊂ T a lift-curve. Then P(T) = C(L).

*Proof.*
1. **⊆.** Immediate, since L ⊂ T.
2. **⊇: curves in slices.** Let y ∈ C(L). t is non-constant on L, since 𝒥 ∩ {t = 0} = {(0,0)}. So L_t ≠ ∅ for small t ≠ 0.
   - Take such a t ∉ Z (Theorem A.9) and (p, t) ∈ L.
   - T_t has pure dimension 1 at p (Krull), so it contains a curve germ γ at p.
   - Since T ⊂ Ñ ∪ 𝒥 and 𝒥_t is finite, γ ∖ p ⊂ Ñ_t. So q(γ) is the germ at J_t of the branch H_t(b) of B_t, which is locally irreducible since it is a disc.
   - By (Kur′), the germ (B, p) is a universal deformation of X_p ≅ J_t. Since p lies in the deepest locus, its vertex labels are those of G_J.
   - Theorem A.9 at (J_t, p, y, H_t(b), γ) applies, because [comp_y(p)] = [Y_t] (y ∈ C(L)). (IMOV) would require H_t(b) ∖ J_t ⊂ Δ_{G_J}, which contradicts (P) and stratum preservation. So (STAY) holds: comp_y ≡ const of class [Y_t] along γ, i.e. γ ⊂ A_y(T).
3. **⊇: conclusion.**
   - A_y(T) = T ∩ (L_y × Δ) ∩ {([comp_y], [Y_t]) ∈ diagonal} is analytic.
   - It contains a curve in the slice {t} for uncountably many t.
   - An analytic set of dimension ≤ 1 has only countably many irreducible components, so it contains curves in only countably many slices.
   - Hence dim A_y(T) = 2, and A_y(T) = T by irreducibility. ∎


---

## II.9. Proof of Theorem A

**Theorem A.** Assume the hypotheses of the problem, read as (R1) and (R2^orb) — equivalently, by Theorem 7.2, as (R1), (R2) and (Loc) — and the Part I results I.2, I.3, I.5, I.6 in the forms of §1.6. Then Y_t = Y_0 for all t ∈ Δ, i.e. π_i(∂V_t) = {Y_0}.

*Proof.*

### 9.1 Set-up
- Take the data of I.5: pieces E^m with constant vertices c_m (m = 1, …, k); transitions J_m with labelled lifts (β̃_m, x_m) and (β̃′_m, x_m); the endpoint Q_0 with the labelled lift (β̃, x) and the terminal lift b̃.
- At each of the finitely many points J_1, …, J_{k−1}, Q_0, fix balls B′ ⋐ B as in Prop. 5.2. Impose Setting 6.0 for each of the finitely many lifts β̃_m, β̃′_m (at J_m) and β̃, b̃ (at Q_0), with one common ε > 0.
- Shrinking a lift to a smaller ball preserves "labelled by" (Definition 1.2). For each labelled lift, use in Setting 6.0 the isomorphism ι supplied by Definition 1.2. The piece of Setting 6.0 is then the piece named in I.5, since it is the piece containing Π_{S,ι}(lift ∖ 0). (If I.5 gives the labels only up to Aut(G), use Remark 6.4.)
- For b̃ choose any ι_b : G_{S_b} → G_b, and let E_b be the piece of Setting 6.0.
- Let p_m(t) (respectively p_0(t)) be the unique lift of H_t(J_m) (respectively H_t(Q_0)) given by Prop. 5.2.
- Put φ_m(t) := φ_{c_m}(E^m_t), where E^m_t = Π_t(E^m). This is well defined, since c_m ∉ M(E^m_t) by Theorem 4.4(a).

### 9.2 The value of the tracked copy is carried along the chain
**Claim.** [φ_m(t)] = [Y_t] for m = 1, …, k and |t| < ε.

1. **Base, m = 1.**
   - E^1 ⊂ ∂V_0 (via ξ_Γ), and E^1_t = Π_t(E^1) ⊂ Â^Γ_t = ∂V_t, by Lemma 3.1(2) and (R2).
   - On ∂V_t, pr_i = π_i ≡ Y_t, and c_1 = i. So φ_1(t) = Y_t, in fact for all t ∈ Δ.
2. **Step m → m + 1.** Apply Prop. 6.2 at J_m twice:
   - to (β̃_m, x_m), labelled by (E^m, c_m): [comp_{x_m}(p_m(t))] = [φ_m(t)];
   - to (β̃′_m, x_m), labelled by (E^{m+1}, c_{m+1}): [comp_{x_m}(p_m(t))] = [φ_{m+1}(t)].

   Both statements concern the **same point** p_m(t), the unique, Aut(J_m)-fixed lift of H_t(J_m) in B (Prop. 5.2). Hence [φ_{m+1}(t)] = [φ_m(t)].
   - No case distinction is needed: J_m may be a puncture of either adjacent piece or lie in its stratum (interior and R(D)-transitions), and the strata may or may not be of product type.

### 9.3 The endpoint
1. Prop. 6.2 at Q_0, applied to (β̃, x) labelled by (E^k, c_k), together with 9.2, gives
   [comp_x(p_0(t))] = [φ_k(t)] = [Y_t] for |t| < ε.
2. By I.6, (P) holds for b. By (K-c), x is in case MERGE or MOV for S_b. Prop. 6.3, applied to b̃ at the same point p_0(t), gives
   [comp_x(p_0(t))] ∈ F′(E_b).
3. Hence [Y_t] ∈ F′(E_b) for |t| < ε, and F′(E_b) is a finite set independent of t (Definition 2.1′).

### 9.4 Conclusion
- The preimage of the finite set F′(E_b) under M_{g_i,n_i} → 𝔐_{g_i,n_i} is finite.
- t ↦ Y_t is continuous (Lemma 2.3) and Δ_ε is connected, so Y_t = Y_0 for |t| < ε.
- By Lemma 2.3 (holomorphy of t ↦ Y_t and the identity theorem), Y_t = Y_0 for all t ∈ Δ. ∎

**Remarks on the proof.**
- **No contradiction argument is needed.** We never assume that Y is non-constant. The proof rests on three facts:
  - one fixed lift p(t) (Prop. 5.2);
  - constancy of the constant vertices of every transported piece (Theorem 4.4(a));
  - continuity of comp_x.
- **The finiteness Lemmas F0/F1 enter only through Theorem 4.4(b), used once, in step 9.3(2),** and only for the moving vertices of the single piece E_b. Theorem 4.4(a), which carries the value along the chain, does not use it.
- **Uses of (R2^orb).**
  - (a), (b), the inclusion "⊂" of (c), and (d) enter through Lemma 3.1, and through it Prop. 4.2, Lemma 4.3, Theorem 4.4 and Lemma 6.1(3).
  - (a) and both inclusions of (c) enter through Props. 5.1 and 5.2. The inclusion "⊃" is the one giving |Aut(J_t)| ≥ |Aut(J)|.
- **Part I used:** I.2 and I.3 (through Theorem 4.4), I.5 (the chain), I.6 (only (P) at Q_0). I.1 enters only through I.2/I.3. I.4 and Lemma PT are not used.

---

## II.10 Cited classical facts (Part II; from memory; precise statements as used)

**Moduli and Kuranishi theory**
- **(St)** For a stable graph G, with the notation of C4:
  - Mod_G acts properly discontinuously by biholomorphisms on T_G = ∏ T_w, with slice neighbourhoods;
  - ξ_G∘p is surjective onto Δ_G, with fibres the Mod_G-orbits;
  - Mod_Π = ker(Mod_G → Aut(G)), and this map is onto;
  - ξ_G : ∏ M_w → Δ_G is the quotient by Aut(G), a finite morphism of quasi-projective varieties, extending to the finite gluing morphism ξ̄_G : ∏ M̄_w → closure(Δ_G);
  - M̄_g and the M̄_w are projective.

  (Deligne–Mumford, Knudsen; Arbarello–Cornalba–Griffiths, *Geometry of Algebraic Curves II*, Ch. XI–XII.)
- **(Kur), (K2), (PN)** As stated in §1.4 (ACG II, Ch. XI).
- **(Kur′)** For p ∈ B, the germ (B, p) with the restricted family is a universal deformation of X_p, and q near p is the quotient by Stab_{Aut(J)}(p).
- **(Iso)** A biholomorphism of a stable pointed Riemann surface that is isotopic to the identity rel marked points is the identity.
- **(TF)** For N ≥ 3, Mod_w[N] (C4/Step 1 of Theorem 4.4) is torsion-free and normal of finite index. Ingredients:
  - Nielsen realisation (Kerckhoff): a finite-order class is realised by an automorphism;
  - g = 0: a Möbius map fixing ≥ 3 points is the identity;
  - g = 1: a group automorphism of an elliptic curve trivial on H_1(·, ℤ/N), N ≥ 3, is the identity;
  - g ≥ 2: Serre's lemma.
- **(BE)** Bers embedding: T_{h,m} is biholomorphic to a bounded domain in ℂ^{3h−3+m}.

**Teichmüller and hyperbolic geometry**
- **(Roy)** Royden; Earle–Kra, Gardiner for punctured surfaces: on T_{h,m} the Teichmüller metric equals the Kobayashi metric. Hence every holomorphic map from H, with the Poincaré metric of curvature −4, to T_{h,m} is 1-Lipschitz.
- **(VT)** Thurston, Veech: a mapping class preserving a Teichmüller disc and acting on it as a hyperbolic isometry is pseudo-Anosov. Equivalently, an affine automorphism of a half-translation surface with hyperbolic derivative is pseudo-Anosov.
- **(Bers)** For a pseudo-Anosov class g, τ(g) = inf_X d_T(X, gX) > 0. It is attained exactly on the unique g-invariant Teichmüller geodesic (the axis), along which g translates by τ(g).
- **(Th)** Thurston, "Minimal stretch maps between hyperbolic surfaces": let X, Y be complete hyperbolic surfaces of finite area and ψ : Y → X a homeomorphism (cusps to cusps). If ℓ_X(ψ(c)) ≤ ℓ_Y(c) for every closed geodesic c of Y, then ψ is homotopic to an isometry. *(Scope caveat: rigidity is certainly in Thurston's paper for closed surfaces; that it covers complete finite-area surfaces with cusps is believed but cited from memory. An alternative route for the cusped case: length-spectrum domination gives a 1-Lipschitz map in the homotopy class (Thurston's best-Lipschitz-constant theorem), and equal hyperbolic areas force it to be an isometry.)*
- **(Sel)** Selberg's lemma: finitely generated subgroups of GL_n(ℂ) (more generally, of GL_n over a field of characteristic 0) are virtually torsion-free. Lattices in PSL_2(ℝ) are finitely generated.
- **(Cent)** The centraliser of a lattice of PSL_2(ℝ) in the full isometry group of H is trivial.
- **(Dens)** For a lattice, the pairs of fixed points of hyperbolic elements are dense in ∂H × ∂H. Hence transverse intersection points of axes are dense in H.
- **(Unif)** Uniformisation of hyperbolic 2-orbifolds of finite type: given a compact Riemann surface minus finitely many points, with finitely many points c_k of assigned orders e_k ≥ 2 and χ^orb < 0, there is a lattice Λ and a holomorphic Galois branched covering H → H/Λ ≅ the surface. It is branched of order e_k exactly over c_k, and its cusps correspond to the punctures.
- **Lifting criterion** for coverings; local model z ↦ z^e at cone points.
- **(IS)** (finiteness for the targets M_u[N]). No longer cited: for g_u = 0 it is Lemma F0, and for g_u ≥ 1 it is Lemma F1 below, both proved here. Lemma F1 rests on the closed-fibre Imayoshi–Shiga theorem (IS_c), on (BC) and on (TF), stated with it.
- **(dF)** Generalised de Franchis theorem (Imayoshi 1983; from memory): if R and Y are Riemann surfaces of finite type and Y is hyperbolic, there are only finitely many non-constant holomorphic maps R → Y.

**Lemma F0 (finiteness for genus-0 targets; proved here, no citation beyond big Picard and Riemann–Hurwitz).** Let R be a Riemann surface of finite type, i.e. R = R̄ ∖ P with R̄ compact of genus h and P finite, |P| = k. Then:
- (a) there are only finitely many non-constant holomorphic maps R → P¹ ∖ {0,1,∞};
- (b) for every n ≥ 4 there are only finitely many non-constant holomorphic maps R → M_{0,n} (points labelled).

*Proof.*
- (a) Let f : R → P¹ ∖ {0,1,∞} be holomorphic and non-constant. By the big Picard theorem f has no essential singularity at a point of P (near such a point it would take the value 0 or 1), so f extends to a non-constant holomorphic map f̄ : R̄ → P¹ of some degree d ≥ 1, with f̄^{-1}{0,1,∞} ⊂ P.
  - **Degree bound.** Over the three points 0, 1, ∞ the ramification satisfies Σ_{p ∈ f̄^{-1}{0,1,∞}} (e_p − 1) = 3d − #f̄^{-1}{0,1,∞} ≥ 3d − k. Riemann–Hurwitz gives 2h − 2 = −2d + Σ_{p ∈ R̄}(e_p − 1) ≥ −2d + 3d − k, i.e. d ≤ 2h − 2 + k.
  - **Divisors.** div(f̄) is supported in P, and its positive and negative parts have degree d ≤ 2h − 2 + k. So div(f̄) lies in a finite set of divisors.
  - **Constants.** Two meromorphic functions with the same divisor differ by a constant factor (their quotient is holomorphic and zero-free on the compact R̄). Fix f_0 with div(f_0) = div(f̄), so f̄ = c f_0 with c ∈ ℂ^*. f̄ is surjective, so it takes the value 1 at some point, which lies in P; at that point p, f_0(p) ∈ ℂ^* and c = 1/f_0(p). So c lies in the finite set {1/f_0(p) : p ∈ P, f_0(p) ∈ ℂ^*}.
  - Hence there are finitely many f.
- (b) Normalising the points labelled 1, 2, 3 to 0, 1, ∞ identifies M_{0,n} with {(x_4, …, x_n) ∈ (P¹ ∖ {0,1,∞})^{n−3} : x_l ≠ x_m for l ≠ m}. A holomorphic map g = (x_4, …, x_n) : R → M_{0,n} has coordinates x_m : R → P¹ ∖ {0,1,∞}, each constant or, by (a), one of finitely many non-constant maps.
  - If g is non-constant, some x_l is non-constant. Its extension x̄_l : R̄ → P¹ is surjective, so P¹ ∖ x_l(R) ⊂ x̄_l(P), a finite set.
  - A constant coordinate x_m ≡ c_m must satisfy c_m ≠ x_l(z) for all z ∈ R, so c_m ∈ x̄_l(P).
  - So g is determined by finitely many choices: which coordinates are constant, the non-constant ones from the finite set of (a), and the constants from the finite sets x̄_l(P). ∎

(Sanity check: for R = P¹ ∖ {0,1,∞}, (a) gives d ≤ 1, and the maps are the six Möbius maps permuting {0,1,∞}, as expected.)

**Lemma F1 (finiteness for targets of genus ≥ 1 with marked points; proved here from closed-surface finiteness).** Let h ≥ 1, m ≥ 1, N ≥ 3, and let Mod_{h,m}[N] be the kernel of PMod_{h,m} → Sp(2h, ℤ/N) (so Mod_u[N] of Theorem 4.4 for g_u ≥ 1). Put M_{h,m}[N] := T_{h,m}/Mod_{h,m}[N]. For every Riemann surface R of finite type, the set of **all** non-constant holomorphic maps R → M_{h,m}[N] is finite.

(In particular each free homotopy class contains finitely many such maps, which is all that Theorem 4.4(b) needs. The case (1,1) is included; it is also covered by (dF). The proof uses no finiteness statement for families of punctured surfaces: it reduces to closed fibres by a characteristic branched covering. Notation inside this proof is local: Φ, Π, Λ, G, L, K, Q, M, Υ have the meanings given here, unrelated to their uses elsewhere in Part II.)

*Cited inputs (from memory).*
- **(IS_c) Imayoshi–Shiga finiteness, closed fibres** (Imayoshi–Shiga 1988; for compact bases this is the Parshin–Arakelov theorem). Let B be a Riemann surface of finite type and g ≥ 2. There are only finitely many isomorphism classes, over B, of locally non-trivial holomorphic families of closed Riemann surfaces of genus g over B. (A holomorphic family is a proper holomorphic submersion from a complex surface onto B with fibres of genus g; locally non-trivial means that over no non-empty open subset of B are all fibres isomorphic.)
- **(BC) Branched covers and Teichmüller spaces** (MacLachlan–Harvey 1975; Birman–Hilden; Bers–Greenberg; Nag's book). For a finite regular branched covering of the kind constructed in Step 2c below, the induced map Φ : T_{h,m} → T_{h′} is holomorphic and injective. *Sketch:* uniformise the orbifold (Σ_0, cone order n_j at x_j) by a cocompact Fuchsian group Γ_0, and let Γ_Y = ker(Γ_0 → G); by Bers–Greenberg T(Γ_0) ≅ T_{h,m}, and T(Γ_Y) ≅ T_{h′}, compatibly with markings; in Bers' model (Γ-compatible Beltrami coefficients modulo w^μ = w^ν on ℝ) Φ is the inclusion [μ] ↦ [μ], injective because the equivalence relation is the same, and holomorphic because in the Bers embedding it is the restriction of the linear inclusion B_2(Γ_0) ⊂ B_2(Γ_Y).
- **(TF)** (Serre's lemma for closed surfaces): Mod_g[N′] is torsion-free for N′ ≥ 3.

*F1 §0.* Trivial case and conventions

*Ordering remark.* From here on we use that Mod_{h,m}[N] (N ≥ 3) is torsion-free, hence (having finite stabilisers) acts freely on T_{h,m}, so that T_{h,m} → M_{h,m}[N] is an unramified covering. This is proved in Step 2d below (Nielsen realisation for cyclic groups + Serre's lemma); that argument uses nothing from §0–§2c, so there is no circularity.

If R is not hyperbolic, its universal cover is C or P^1. By the Bers embedding, T_{h,m} is biholomorphic to a bounded domain in C^{3h-3+m}. A lift of a holomorphic map R → M_{h,m}[N] to universal covers is therefore constant (Liouville, or compactness for P^1). So every holomorphic map R → M_{h,m}[N] is constant, and the set in question is empty.

From now on R = D/Π, where D is the unit disc and Π ≅ π_1(R) is a Fuchsian group. Π is finitely generated because R has finite type.

Write T = T_{h,m}, PMod = PMod_{h,m}, and M = M_{h,m}[N] = T/Mod_{h,m}[N]. Mapping classes act on T by [X, φ] ↦ [X, φ∘ϑ^{-1}], where φ: (Σ_0, P) → (X, P_X) is a marking. Here Σ_0 is a closed genus-h surface, P ⊂ Σ_0 is a set of m labelled points, and S_0 = Σ_0 \ P.

*F1 §1.* The closed case

**Lemma F1.1.** Let B be of finite type, g ≥ 2 and N' ≥ 3. Then there are only finitely many non-constant holomorphic maps B → M_g[N'].

*Proof.*

1. **M_g[N'] is a fine moduli space.** Mod_g[N'] acts freely on T_g by (TF). It therefore acts freely on the Teichmüller curve, and the quotient is a universal curve C → M_g[N']; this is a proper holomorphic submersion. As a set, M_g[N'] = {(X, α)}/iso, where α is a symplectic isomorphism (Z/N')^{2g} → H_1(X, Z/N'). Indeed, two markings of X inducing the same α differ by an element of Mod_g[N'].

2. **Non-constant maps give locally non-trivial families.** Let F: B → M_g[N'] be holomorphic and non-constant. Then the composite B → M_g is non-constant, because M_g[N'] → M_g has finite fibres and B is connected. By the identity theorem it is non-constant on every open set. Hence F^*C is locally non-trivial.

3. **Isomorphic families give maps differing by Sp(2g, Z/N').** Suppose F_1^*C ≅ F_2^*C over B via Θ. Each F_i comes with a continuous level structure α_i(b) on the fibre over b, that is, a section of the finite covering space of symplectic frames of H_1(X_b, Z/N'). Then σ(b) := α_1(b)^{-1} ∘ Θ_b^{-1} ∘ α_2(b) is a continuous map into the finite group Sp(2g, Z/N'). It is therefore constant, say σ, and F_2 = σ·F_1, where σ acts by (X, α) ↦ (X, α∘σ).

4. **Count.** By (IS_c) there are finitely many families, and each family arises from at most |Sp(2g, Z/N')| maps. ∎

*F1 §2.* The branched-cover construction

**Step 2a (a characteristic subgroup).** Let π = π_1(S_0). It is free of rank 2h+m-1 ≥ 2. Let c_1, ..., c_m be loops around the punctures; each is non-trivial in π.

- π is residually finite, so for each j there is a normal subgroup K_j of finite index with c_j ∉ K_j. Let d be the largest of these indices.
- Let K be the intersection of all subgroups of π of index ≤ d. There are finitely many such subgroups, since π is finitely generated.
- K is characteristic in π, has finite index, and no c_j lies in K.

Let G = π/K, and let n_j ≥ 2 be the order of the image of c_j in G.

**Step 2b (the covering of a pointed curve).** For a pointed curve (X, P_X) of type (h,m), let Y° → X \ P_X be the regular G-cover corresponding to K. It is canonical because K is characteristic, and it is unique up to deck transformations. Fill in the ends to get a compact Riemann surface Y_X with a branched G-cover Y_X → X. This cover is branched exactly over P_X, with order n_j over x_j.

By Riemann–Hurwitz, 2h'-2 = |G|·(2h-2 + Σ_j (1 - 1/n_j)) > 0, because h ≥ 1 and m ≥ 1. So the genus h' of Y_X satisfies h' ≥ 2. In particular Aut(Y_X) is finite (Hurwitz).

**Step 2c (the map Φ and lifts of mapping classes).** Fix Y_0 → Σ_0 for the base point. Define Φ: T_{h,m} → T_{h'} by [X, φ] ↦ [Y_X, φ̃], where φ̃ is any lift of φ.

- Lifts exist because φ_*(K) = K (K is characteristic).
- Two lifts differ by a deck transformation, which is conformal on Y_X, so they define the same point of T_{h'}.
- An isotopy rel P lifts to an isotopy.

Every ϑ ∈ PMod lifts to Y_0: a representing homeomorphism of (Σ_0, P) acts on π by an automorphism defined up to inner automorphisms, which preserves the characteristic subgroup K, so it lifts to the regular cover Y_0° and extends over the filled-in points. The isotopy classes of the lifts of ϑ form a coset ϑ̃G in Mod(Y_0), where G ⊂ Mod(Y_0) is the group of deck classes: lifts of one homeomorphism differ by deck transformations, and an isotopy rel P downstairs lifts to an isotopy upstairs. G injects into Mod(Y_0), because a non-trivial conformal automorphism of a surface of genus ≥ 2 is not isotopic to the identity.

To avoid any appeal to the Birman–Hilden property (whether a lift isotopic to the identity upstairs forces the downstairs class to be trivial), we work with **pairs**. Let L be the set of pairs (ϑ, ϑ̃) with ϑ ∈ PMod and ϑ̃ ∈ Mod(Y_0) the isotopy class of a lift of a representative of ϑ. Under componentwise composition L is a group. The projection L → PMod, (ϑ, ϑ̃) ↦ ϑ, is a surjective homomorphism, and its kernel is {(1, g) : g ∈ G}, which is isomorphic to G. The second projection L → Mod(Y_0), (ϑ, ϑ̃) ↦ ϑ̃, is also a homomorphism (it need not be injective, and we never use injectivity). Directly from the definitions, **Φ(ϑ·p) = ϑ̃·Φ(p)** for every (ϑ, ϑ̃) ∈ L.

By (BC), Φ is holomorphic and injective.

**Step 2d (choosing levels).** Fix N' ≥ 3. Let Λ := {(ϑ, ϑ̃) ∈ L : ϑ̃ ∈ Mod(Y_0)[N']}, the preimage of the finite-index subgroup Mod(Y_0)[N'] under the second projection; it has finite index in L. The intersection of Λ with the kernel of the first projection is {(1, g) : g ∈ G ∩ Mod(Y_0)[N']}. Since Mod(Y_0)[N'] is torsion-free (TF), G is finite and G injects into Mod(Y_0), this intersection is trivial. So the first projection maps Λ isomorphically onto a subgroup Γ'' ⊂ PMod, of finite index because L → PMod is onto and [L : Λ] < ∞. Let λ: Γ'' → Mod_{h'}[N'] be the inverse isomorphism followed by the second projection, ϑ ↦ ϑ̃; it is a homomorphism, and Φ(ϑp) = λ(ϑ)Φ(p) for ϑ ∈ Γ''.

Let Γ_1 be the normal core in PMod of Γ'' ∩ Mod_{h,m}[N]. Then Γ_1 is normal in PMod, of finite index, and contained in Mod_{h,m}[N]. It is torsion-free, because Mod_{h,m}[N] is: a finite-order element of PMod_{h,m} is represented by a conformal automorphism f of some pointed curve (X, P_X) fixing each marked point (Nielsen realisation for finite cyclic groups); if it lies in Mod_{h,m}[N], then f acts trivially on H_1(X; ℤ/N) with N ≥ 3 and h ≥ 1, so f = id by Serre's lemma (the genus-≥1 form of (TF): an automorphism of a compact Riemann surface of genus ≥ 1 that fixes a point and acts trivially on H_1(·; ℤ/N), N ≥ 3, is the identity), and the mapping class is trivial. Put M_1 := T/Γ_1. This is a complex manifold and a finite unramified cover q: M_1 → M.

Define Υ: M_1 → M_{h'}[N'] by Γ_1 p ↦ Mod_{h'}[N']·Φ(p). It is well defined by the equivariance in Step 2d, and holomorphic because locally it is Φ read in covering charts.

**Lemma F1.2.** (a) Υ is locally injective. (b) Υ has finite fibres.

*Proof.*

(a) Let x = Γ_1 p.
- Choose a neighbourhood W of Φ(p) on which the covering T_{h'} → M_{h'}[N'] is injective.
- Choose a neighbourhood U of p on which T → M_1 is injective and with Φ(U) ⊂ W.
- On U, Υ∘(projection) = (projection)∘Φ, and the right-hand side is injective on U because Φ is injective (BC).
- Hence Υ is injective on the open set image(U) ∋ x.

(b) Suppose Υ(Γ_1 q) = Υ(Γ_1 p).
- Then Y_q ≅ Y_p via some conformal c. Hence Σ_q ≅ Y_p / (c G_q c^{-1}), and the iso carries the labelled points x_j(q) to branch points of this quotient.
- Aut(Y_p) is finite and has finitely many subgroups, and there are finitely many labellings. So the pointed curve [Σ_q, x(q)] ∈ M_{h,m} lies in a finite set.
- The map M_1 → M_{h,m} has fibres of size at most [PMod : Γ_1] < ∞. ∎

*F1 §3.* Proof of Lemma F1

Let f: R → M be holomorphic and non-constant.

**Step 1 (the homomorphism ρ_f).** Choose a lift f̃: D → T. Since Mod_{h,m}[N] acts freely as the deck group, there is a homomorphism ρ_f: Π → Mod_{h,m}[N] with f̃∘γ = ρ_f(γ)∘f̃. Changing the lift conjugates ρ_f.

**Step 2 (finitely many intermediate covers).** Since Γ_1 is normal, H_f := ρ_f^{-1}(Γ_1) is the kernel of the induced map Π → Q := Mod_{h,m}[N]/Γ_1. Q is a finite group and Π is finitely generated, so there are finitely many homomorphisms Π → Q. Hence H_f ranges over a finite set {H_1, ..., H_s} of finite-index subgroups.

It therefore suffices to fix H = H_k and to show that the set 𝓕_H of non-constant f with H_f = H is finite.

**Step 3 (lifting f to R').** Let R' = D/H. It is a connected finite unramified cover p_H: R' → R, so it has finite type and is hyperbolic.

For f ∈ 𝓕_H, fix one lift f̃. It descends to a holomorphic f': R' → M_1 with q∘f' = f∘p_H. Since p_H is surjective, f' determines f. So f ↦ f' is injective on 𝓕_H.

**Step 4 (the composite F' is non-constant).** Let F' := Υ∘f': R' → M_{h'}[N']. If F' were constant, then Φ∘f̃ would take values in a single Mod_{h'}[N']-orbit. That orbit is discrete, because the action is properly discontinuous, and D is connected, so Φ∘f̃ would be constant. Since Φ is injective, f̃ would be constant, and so would f, a contradiction.

**Step 5 (finitely many values of F').** By Lemma F1.1 applied to B = R' and g = h', there are only finitely many possible F'.

**Step 6 (finitely many f' over each F').** Fix F', and let f'_a, f'_b: R' → M_1 be continuous maps with Υ∘f'_a = Υ∘f'_b = F'. Let E = {r : f'_a(r) = f'_b(r)}.
- E is closed, since M_1 is Hausdorff.
- E is open by Lemma F1.2(a): near a point of E both maps take values in a neighbourhood on which Υ is injective.
- R' is connected, so either f'_a = f'_b or the two maps disagree at every point.

Fix r_0 ∈ R'. Distinct lifts then take distinct values in Υ^{-1}(F'(r_0)), which is finite by Lemma F1.2(b). So there are finitely many f' over each F'.

**Conclusion.** Combining Steps 3–6, 𝓕_H is finite. Hence the set of all non-constant holomorphic maps R → M_{h,m}[N] is finite. ∎

(This is the argument suggested as a "possible repair" in an earlier version of II.11; it is now carried out.)


**Topology and analytic geometry**
- **(KP1)** For a connected CW complex X and Y = K(π, 1), free homotopy classes [X, Y] correspond to Hom(π_1 X, π) modulo conjugation.
- **(Chow)** Closed analytic subsets of projective varieties are algebraic.
- **(Irr)** For a complex algebraic variety:
  - analytic irreducible components are the algebraic ones;
  - the analytic normalisation is the algebraic one;
  - the Euclidean closure of a constructible set equals its Zariski closure;
  - smooth irreducible quasi-projective curves are compact Riemann surfaces minus finitely many points.
- **(Remmert)** The image of an analytic set under a proper holomorphic map is analytic. Finite maps preserve dimension and map irreducible sets to irreducible sets.
- **(Krull)** If T is an irreducible analytic set of dimension d and f is holomorphic and non-constant on T, then every non-empty fibre of f has pure dimension d − 1.
- **(Cl)** For analytic X and a closed analytic Z ⊂ X, closure(X ∖ Z) is the union of the irreducible components of X not contained in Z.
- **(Reg)** The regular locus of an irreducible analytic set is a connected manifold. A proper analytic subset does not disconnect a connected complex manifold.
- **(CG)** Local structure of curve germs:
  - a 1-dimensional germ with r branches has arbitrarily small neighbourhoods U with U ∖ {z} a disjoint union of r punctured discs;
  - branches are homeomorphic to discs;
  - normalisation separates branches.
- **(Con)** Analytic sets are locally connected and locally conic, in particular locally contractible.
- **(HW)** Hurewicz–Wallman, *Dimension Theory*, Thm. IV.4:
  - a closed subset of covering dimension ≤ n − 2 does not separate a connected n-manifold;
  - analytic sets of complex dimension k have covering dimension 2k;
  - covering dimension is monotone on subsets of separable metric spaces.
  - (Hurewicz's theorem on closed maps, used in Lemma L.2 Step 3) if f : X → Y is a closed surjection of separable metric spaces, then dim X ≤ dim Y + sup_y dim f^{-1}(y). (The inequality dim Y ≤ dim X fails in general for closed finite-to-one maps and is never used.)
- **(SF)** Stein factorisation of proper holomorphic maps (Grauert–Remmert).
- **(CR)** Cartan–Remmert: {x : dim_x Φ^{-1}Φ(x) ≥ k} is analytic.
- **Riemann extension theorem; identity theorem.**
- **CL (Part I, I.3)** is quoted, not classical; see §1.6.

---

## II.11 Gaps of Part II

- **Former G1 (finiteness for marked targets) — resolved, modulo classical citations.** Theorem 4.4(b) needs, for the moving vertices u of E_b, that a fixed finite-type R admits only finitely many non-constant holomorphic maps (in a given free homotopy class) into M_u[N]. This is now proved: Lemma F0 for g_u = 0 (big Picard and Riemann–Hurwitz only), and Lemma F1 for g_u ≥ 1 (all n_u ≥ 1, including (1,1)). Lemma F1 reduces to closed fibres by a characteristic branched covering T_{h,m} → T_{h′} (h′ ≥ 2) and uses only the closed-fibre Imayoshi–Shiga theorem (IS_c), the branched-cover fact (BC) and Serre's lemma, all cited from memory. Whether the original Imayoshi–Shiga paper covers marked targets directly is no longer relevant.
- **G2 (interface with Part I).** I.5 is used in the form (K-a)–(K-c) with Definition 1.2. This form is derived from Part I in Lemma L.1 of the Bridge section (which uses Part I Lemma TI, §I.5.7 and Proposition Ψ of Part I §I.6A). Remark 6.4 shows that the argument also tolerates relabelling by Aut(G).
  - I.2/I.3 are used as stated in §1.6. In particular this includes J0 in every boundary stratum (Part I, Supplement R3′).
- **Readings (not gaps in the proof, but conditions of the result).**
  - Theorem A is proved under (R1) and (R2^orb) = (O-emb), equivalently (R1), (R2) and (Loc), equivalently (R1), (R2) and (AP) (Theorem 7.5).
  - **Open:**
    - the problem under the coarse reading (R2), and under the intrinsic reading (O-int);
    - whether a global admissible family with isotropy change at the boundary exists (§8.2); by Theorem 7.5 this is exactly the question whether (AP) can fail on every disc around t = 0;
    - whether (Loc) at t_0 = 0 alone suffices (Remark 7.4). (By Theorem 7.5 and Remark 7.6, (AP) on a disc |t| < r suffices.)

---

# Part III — Theorem B: the claim under the coarse reading, given (Rig) and (NRT_P)

**What this Part proves.** Theorem B (stated in §0.10): under (R1), (R2), (Rig) and (NRT_P), Y_t = Y_0 for all t. Moreover, given (Rig), (NRT_P) is equivalent to the claim, and any violation of (NRT_P) forces an isotropy drop.

The inputs BB1–BB6 are stated in §1 in the precise forms used. Each is proved elsewhere in this document; see the head of §1. Every other step is proved here, including:
- Lemmas 1–3, Proposition 4 and Lemma 5;
- the Φ-version of the generic-time dichotomy (Proposition 3.1);
- the lift-curve facts (Lemmas 2.3–2.5);
- the induction along the walk chain and the endpoint.

(Rig) and (NRT_P) are hypotheses of Theorem B and are not proved.

*Structure:*
- §0: conventions and statement;
- §1: the inputs;
- §2: preliminary lemmas;
- §3: the Φ-dichotomy;
- §4: Lemmas 1–3 and Proposition 4;
- §5: Lemma 5;
- §6: proof of Theorem B and the isotropy drop;
- §III.7: cited facts; §III.8: gaps.

## III.0. Conventions, definitions, statement

**0.1 Setting and readings.** g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric. 𝒱 ⊂ M_g × Δ is the family of the problem, V_t its fibres. The hypotheses (i), (ii) and "smoothly trivial" are read as follows.
- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set. Its fibre over t is closure(V_t) (closures in M̄_g).
- **(R2)** There is a homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ, i.e. H(z,t) = (H_t(z), t). It is smooth on V_0 × Δ, and H_0 = id. For every stratum Δ_G (including the open stratum M_g), H maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ).

  This is the *coarse* reading: H_t need not preserve automorphism groups of points.

Δ_Γ is a boundary stratum of *product type*: the gluing map ξ_Γ : ∏_{w∈V(Γ)} M_w → Δ_Γ is bijective on coarse spaces. Here M_w = M_{g_w,n_w}, with the half-edges at w as the marked points. So Δ_Γ ≅ ∏_j M_{g_j,n_j}, and π_i = pr_i ∘ ξ_Γ^{-1}. We put ∂V_t := closure(V_t) ∩ Δ_Γ and assume dim ∂V_t = 1 and π_i(∂V_t) = {Y_t} for all t, with dim M_{g_i,n_i} > 0.

**0.2 Notation.**
- B_t := closure(V_t) ∖ V_t = closure(V_t) ∩ ∂M̄_g.
- By (R2), H_t(B_0) = B_t, and H_t maps closure(V_0) ∩ Δ_G onto closure(V_t) ∩ Δ_G for every stratum.
- 𝔐 := M_{g_i,n_i}/S_{n_i}, a normal complex space. For an n_i-pointed curve Z of genus g_i, [Z] ∈ 𝔐 is its class with the marked points unordered.
- A *component of type (g_i,n_i)* of a nodal curve is an irreducible component whose normalisation has genus g_i and carries n_i special points (preimages of nodes and marked points).
- Y : Δ → M_{g_i,n_i} denotes t ↦ Y_t. Since M_{g_i,n_i} → 𝔐 has finite fibres and Δ is connected, Y is constant iff [Y] is constant.
- *Germs.* "Germ" always means a germ of a complex-analytic set. Inclusions and equalities of germs are inclusions and equalities of germs.

**0.3 Charts (classical; see facts K1–K5 at the end).** For Q ∈ M̄_g, Def(Q) is the base of the Kuranishi family of the stable curve C_Q. B ⊂ Def(Q) is a small Aut(Q)-invariant ball centred at the point 0 representing C_Q. The map q : B → M̄_g is the quotient by Aut(Q) onto an open neighbourhood q(B) of Q.
- For every edge e of the dual graph G_Q there is a plumbing coordinate s_e on B. For p ∈ B, the nodes of the fibre C_p correspond bijectively to the edges e with s_e(p) = 0.
- The *labels* are the vertices of G_Q.
- A label y is *intact at p* if s_e(p) = 0 for every edge e at y. Then C_p has a distinguished irreducible component deforming the component y of C_Q; with its special points, this is F_y(p).
- Put L_y := {p : y intact at p}. Then p ↦ F_y(p) is holomorphic on L_y (fact PN below), with values in M_{g_y,n_y} for a chosen ordering of the half-edges at y.
- The *pattern* at p is S(p) := {e : s_e(p) = 0}.
- An element a ∈ Aut(Q) acts on B, on the labels and on the edges.

**0.4 Pieces, lifted families, (Rig).**
- A *lifted piece at time t* in a stratum Δ_G is a 1-dimensional irreducible component E of the analytic set ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w. Its image ξ_G(E) is a *piece* (at time t).
- M(E) is the set of vertices w for which pr_w is non-constant on E. K(E) is the closure of pr_{M(E)}(E) in ∏_{u∈M(E)} M̄_u.
- **(Rig)** There is a finite set 𝒦 of triples (G, M, K) with the following properties:
  - M ⊂ V(G);
  - K ⊂ ∏_{u∈M} M̄_u is an irreducible closed curve not contained in the boundary;
  - for every t and every lifted piece E at time t in Δ_G, the triple (G, M(E), K(E)) lies in 𝒦 up to the action of Aut(G).
- The *lifted family* 𝒲_G is the closure in ∏_w M̄_w × Δ_* of (ξ_G × id)^{-1}(closure(𝒱) ∩ (Δ_G × Δ_*)). Here Δ_* ⊂ Δ is the disc fixed in 0.6.
- For a 2-dimensional irreducible component W of 𝒲_G, write W_t for its fibre over t, and M_W, K_W, F_W for the data of BB3 (§1).

**0.5 Remark (dimensions).** dim B_0 ≤ 1. Indeed, B_0 is an analytic subset of the 2-dimensional analytic set closure(V_0). Every point of B_0 is a limit of points of V_0, so B_0 contains no 2-dimensional component of closure(V_0).

By (R2), closure(𝒱) ∩ (∂M̄_g × Δ) = H(B_0 × Δ). This set has topological dimension ≤ 4, so as an analytic set it has dimension ≤ 2. Since ξ_G is finite, 𝒲_G^∘ := 𝒲_G ∩ (∏M_w × Δ_*) = (ξ_G × id)^{-1}(closure 𝒱 ∩ (Δ_G × Δ_*)) has dimension ≤ 2. (𝒲_G^∘ is closed in ∏M_w × Δ_*, being the preimage of a set closed in Δ_G × Δ_*.)

Let C be an irreducible component of 𝒲_G. Pick x ∈ C on no other component, and a neighbourhood U of x with 𝒲_G ∩ U = C ∩ U. Since x lies in the closure of 𝒲_G^∘, C ∩ U meets 𝒲_G^∘. So C ∩ (∏M_w × Δ_*) is a non-empty open subset of C. It is contained in 𝒲_G^∘, hence dim C ≤ 2.

**0.6 The disc Δ_*, the finite set 𝔉, the value curves, and Φ.**
- Fix a closed disc Δ̄_* ⊂ Δ centred at 0, with interior Δ_*. All lifted families are taken over Δ_*.
- 𝒲_G is proper over Δ_* (BB3). Each 2-dimensional component W surjects onto Δ_* (BB3: every fibre W_t is non-empty). Components are locally finite, and all of them meet the compact set 𝒲_G ∩ {t = 0}. Hence there are only finitely many components, and there are finitely many stable graphs G of genus g. So **the set 𝒲 of all 2-dimensional components W of all 𝒲_G is finite.**
- For W ∈ 𝒲, let 𝔉_W ⊂ 𝔐 be the set of classes of components of type (g_i,n_i), with their special points, of the coordinates κ[w] (w ∈ M_W) of points κ ∈ F_W. A coordinate that is a smooth curve counts as its own unique component. 𝔉_W is finite because F_W is finite (BB3). Put 𝔉 := ⋃_{W∈𝒲} 𝔉_W, a finite set.
- For W ∈ 𝒲 and a vertex u ∉ M_W of type (g_i,n_i), let Γ̄_{W,u} ⊂ 𝔐 × Δ_* be the image of Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ_* under M_u × Δ_* → 𝔐 × Δ_*.
  - Γ_{W,u} is an irreducible closed curve, finite over Δ_* (BB3; it is closed by Remmert, since (pr_u,t) is proper on W).
  - M_u → 𝔐 is finite, so Γ̄_{W,u} is again an irreducible closed analytic curve, finite over Δ_*.
  - Put Γ̄_all := ⋃_{W,u} Γ̄_{W,u}, a finite union of closed curves.
- **Definition (Φ).** Φ is the set of irreducible germs φ at (Y_0, 0) ∈ 𝔐 × Δ_* that are local branches at (Y_0,0) of some Γ̄_{W,u} (W ∈ 𝒲, u ∉ M_W of type (g_i,n_i)) and are *non-constant*, i.e. φ ≠ germ of {Y_0} × Δ_*. Φ is finite.
- A branch φ may be a Puiseux branch of degree > 1 over Δ_*. So "the value of φ over t" is the finite set φ_t := φ̂ ∩ (𝔐 × {t}), where φ̂ is a fixed small closed representative. All statements involving φ_t are statements about this set.

**0.7 Transport families, anchored sheets, lift-curves.** Let Q ∈ B_0, with chart q : B → q(B), and let c be a local branch of B_0 at Q, i.e. an irreducible component of the germ of B_0 at Q.
- Since B_0 is a curve, after shrinking B we may represent c by a closed subset of q(B) that is homeomorphic to a closed disc with centre Q. After a further shrinking, c ∖ Q lies in a single stratum Δ_{G_c}. Reason: each stratum meets c ∖ Q in a locally closed analytic subset, and c ∖ Q is a connected punctured disc, so only the stratum containing the generic points of c meets c ∖ Q near Q. Possibly G_c = G_Q; then c ⊂ Δ_{G_Q} near Q.
- Choose ε > 0 with H(c × Δ̄_ε) ⊂ q(B) × Δ_ε. Put N_c := H((c° ∖ Q) × Δ_ε), where c° is the interior of the disc c. N_c is homeomorphic to a punctured disc times a disc, hence connected.
- A *lifted branch* (lift) c̃ of c is an irreducible component at 0 of the germ q^{-1}(c). Its pattern S(c̃) := {e : s_e ≡ 0 on c̃}. After shrinking B, s_e ≠ 0 on c̃ ∖ 0 for e ∉ S(c̃), so S(p) = S(c̃) on c̃ ∖ 0.
- The **transport family** Ñ_c̃ is the connected component, containing (c̃ ∖ 0) × {0}, of (q × id)^{-1}(N_c) ⊂ B × Δ_ε.
- An **anchored sheet** of c̃ is an irreducible component T of the germ at (0,0) of closure(Ñ_c̃) (closure in B × Δ_ε) with c̃ × {0} ⊂ T. Anchored sheets exist: the irreducible germ c̃ × {0} lies in the germ of closure(Ñ_c̃), hence in one of its components.
- c̃ (and any anchored sheet of c̃) is **of boundary type** if Q ∉ Δ_{G_c}. Q is a **puncture point** if it has a branch c of boundary type, i.e. a branch with c ∖ Q in a stratum other than Δ_{G_Q}. Being of boundary type depends only on the coarse branch c, not on the lift.
- Put Q_t := H_t(Q), 𝒬 := {(Q_t, t) : t ∈ Δ_ε}, and the *lift locus* Λ := (q × id)^{-1}(𝒬) ⊂ B × Δ_ε.
- A **lift-curve** is an irreducible component of the germ of Λ at (0,0). (§2 shows that, at a puncture point, Λ is analytic near (0,0) and that its germ is a finite union of curve germs.)

**0.8 Persistence.** Let T be an irreducible 2-dimensional germ at (0,0) in B × Δ_ε, L an irreducible curve germ at (0,0), and z a label. For a germ X on which z is intact, write v_z : X → 𝔐 × Δ_ε, (p,t) ↦ ([F_z(p)], t).
- z is **Y-persistent** on T if z is intact on T (T ⊂ L_z × Δ_ε) and [F_z(p)] = [Y_t] for all (p,t) in a representative of T.
- z is **Φ-persistent on T with function φ** (φ ∈ Φ) if z is intact on T and the image germ v_z(T) is contained in φ. Then P_Φ(T) := the set of labels Φ-persistent on T with some φ ∈ Φ. The function is unique: if v_z(T) ⊂ φ ∩ φ′, then since t|_T is non-constant (Lemma 2.1(c)), v_z(T) is a 1-dimensional germ in both irreducible 1-dimensional germs, so φ = v_z(T) = φ′.
- For a lift-curve L (on which every label is intact, Lemma 2.3(c)): C_Φ(L) := the set of labels z for which the image germ v_z(L) is a branch in Φ.
- z is a **rigid Y_0-copy along L** if v_z(L) is the germ of {Y_0} × Δ_ε.
- **Y ∈ Φ** means: the germ of the graph of [Y] at (Y_0,0) belongs to Φ (proved in Lemma 2.7, assuming Y non-constant).

**0.9 Statement (NRT_P).** *Setting:* that of 0.1, together with (R1), (R2), (Rig), and "t ↦ Y_t is non-constant". *Claim:* there do not exist a puncture point Q ∈ B_0, an automorphism a ∈ Aut(Q), a lift-curve L at Q and a label x of G_Q such that
- x ∈ C_Φ(L), and
- a^{-1}x is a rigid Y_0-copy along L.

In words: along L, for all small t ≠ 0, the component x is intact with class on a branch φ ∈ Φ, while the component a^{-1}x is intact with class ≡ Y_0. (Necessarily a^{-1}x ≠ x: a label cannot be both.)

**0.10 Theorem B.** *Assume the setting of 0.1 with (R1), (R2), Δ_Γ of product type, dim M_{g_i,n_i} > 0, (Rig) and (NRT_P). Then Y_t = Y_0 for all t ∈ Δ.* Moreover:
- (NRT_P) is implied by the problem's conclusion, and a counterexample to (NRT_P) is a counterexample to the problem;
- any configuration violating (NRT_P) forces an isotropy drop |Aut(Q_t)| < |Aut(Q)| for small t ≠ 0.

---

## III.1. The inputs BB1–BB6, in the form used

All inputs are proved elsewhere in this document: BB1 is Part I Proposition K_w and Corollary IMOV_all, together with Lemma L.1 of the Bridge section (which gives the labelled form BB1-M); BB2 is Proposition U.1; BB3 is Part II Appendix A, Lemmas A.5 and A.6 (applied to the family restricted to Δ_* and rescaled), together with the elementary consequences derived in Lemma L.3 of the Bridge section; BB6 is Lemma L.2 of the Bridge section. (Rig) is a hypothesis of Theorem B and enters only through BB3.

**BB1 (walk chain; t = 0 geometry of V_0).** Assume Y non-constant (this is the situation in which BB1 is invoked). There are the following data:
- pieces D^1, …, D^k at t = 0 (k ≥ 1), with D^1 ⊂ ∂V_0 (so G(D^1) = Γ);
- points J_1, …, J_{k−1} ∈ B_0 with J_m ∈ closure(D^m) ∩ closure(D^{m+1});
- an endpoint Q_0 ∈ closure(D^k) ∩ B_0.

For uniform notation put J_k := Q_0.

*At each J_m (1 ≤ m ≤ k), in the chart Def(J_m):*
- an *entering lift* β̃_m of a branch β_m of closure(D^m) at J_m;
- a label x_m of G_{J_m}, the *common chart label*.

*At each J_m with m ≤ k − 1, in addition:*
- a *leaving lift* β̃′_m of a branch β′_m of closure(D^{m+1}) at J_m.

*At J_k = Q_0, in addition:*
- a *terminal lift* b̃ of a branch b of B_0 at Q_0, belonging to a piece E_b;
- (MERGE or MOV) at t = 0: either some edge at x_k is not in S(b̃) (MERGE), or x_k is intact along b̃ and [F_{x_k}] is not identically [Y_0] on b̃ ∩ B (MOV).
- Here b̃ ∩ B is irreducible: B is a Milnor ball for b̃, so the normalisation of b̃ ∩ B is a disc.

*(IMOV_all) and (P):*
- If J_m (m ≤ k−1) lies in Δ_{G(D^m)} or in Δ_{G(D^{m+1})}, then β̃′_m = β̃_m (same label x_m).
- If J_m lies in neither stratum, it is a puncture of both adjacent pieces. In particular J_m is a puncture point, and β̃_m, β̃′_m are of boundary type.
- (P) at the endpoint: Q_0 ∉ Δ_{G(D^k)} and Q_0 ∉ Δ_{G(E_b)}. So β̃_k and b̃ are of boundary type, and Q_0 is a puncture point.

*(BB1-M) marking identification, in the precise form used.* For each m = 1, …, k (the travel interval along D^m that ends at J_m), there are:
- a lifted piece E^m ⊂ ∏_{w∈V(G(D^m))} M_w over D^m;
- a vertex c_m of G(D^m) that is constant on E^m with value of class [Y_0];
- for m ≥ 2, a graph isomorphism ι′_{m−1} : G_{S(β̃′_{m−1})} → G(D^m) such that ι′_{m−1}∘Π_{S(β̃′_{m−1})} maps β̃′_{m−1} ∖ 0 into E^m;
- a graph isomorphism ι_m : G_{S(β̃_m)} → G(D^m) such that ι_m∘Π_{S(β̃_m)} maps β̃_m ∖ 0 into E^m.

These satisfy:
- x_m is intact along β̃_m, and ι_m({x_m}) = c_m;
- for m ≥ 2: whenever x_{m−1} is intact along β̃′_{m−1}, ι′_{m−1}({x_{m−1}}) = c_m;
- for m = 1: c_1 = i (the tracked vertex on ∂V_0 is the vertex i of Γ).

Here G_S is G_{J} with the edges outside S contracted, and Π_S is the partial normalisation map of fact PN. "{x}" denotes the vertex of G_S consisting of x alone, which is a vertex exactly when x is intact along the lift.

*Source.* BB1 is Part I Proposition K_w (items 1–4) and Corollary IMOV_all; BB1-M is Lemma L.1 of the Bridge section.

**BB2 (holomorphy).** Under (R1), (R2), t ↦ Y_t ∈ M_{g_i,n_i} is holomorphic.

**BB3 (Lemma U, under (Rig)), form used.**
- 𝒲_G is a closed analytic subset of ∏_w M̄_w × Δ_*, proper over Δ_*.
- For each 2-dimensional irreducible component W of 𝒲_G there are a set M_W ⊂ V(G) and an irreducible closed curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, such that for every t and every 1-dimensional irreducible component D of W_t:
  - D = K_W × {c_D} for a point c_D ∈ ∏_{u∉M_W} M_u;
  - each u ∈ M_W is non-constant on D, and each u ∉ M_W is constant on D. (U1)
- Every fibre W_t is non-empty and is a finite union of such curves D.
- F_W := K_W ∩ ∂(∏_{u∈M_W} M̄_u) is finite and does not depend on t.
- For u ∉ M_W, Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ_* is an irreducible curve, finite over Δ_*. Its fibre over t is the set of values c_D[u] for the components D of W_t.

Consequence: t is non-constant on W, since otherwise a fibre would be 2-dimensional. So every W_t is of pure dimension 1 (Krull), and every point of W_t lies on some component K_W × {c_D}.

**BB4.** Not used. (Its analogue for Y is Part II Appendix A, Theorem A.9; the Φ-version needed here is proved in full in §3.)

**BB5.** Not used.

**BB6 (transport families), form used.** For every Q ∈ B_0 and every lift c̃ as in 0.7, closure(Ñ_c̃) is, near (0,0), a closed analytic subset of B × Δ_ε of pure dimension 2. (Proved as Lemma L.2 of the Bridge section.)

---

## III.2. Preliminary lemmas: transport families, lift-curves, equivariance

Throughout §§2–5, Q ∈ B_0 has chart q : B → q(B), c is a branch of B_0 at Q, c̃ is a lift of c, S := S(c̃), Ñ := Ñ_c̃, and ε is as in 0.7. The data B and ε may be shrunk finitely many times; all statements are about germs at (0,0), or hold for small enough representatives. Z_S := {p ∈ B : s_e(p) = 0 for all e ∈ S}, and Z_S^∘ := {p : S(p) = S}.

**Lemma 2.1 (transport families).**
- (a) For every (p,t) ∈ Ñ: S(p) = S, and q(p) ∈ H_t(c° ∖ Q) ⊂ closure(V_t) ∩ Δ_{G_c}.
- (b) (q × id)(Ñ) = N_c.
- (c) Near (0,0): closure(Ñ) ⊂ Ñ ∪ Λ; closure(Ñ) ⊂ Z_S × Δ_ε; and closure(Ñ) ∩ {t = 0} ⊂ q^{-1}(c) × {0}, which has dimension ≤ 1.
- (d) Near (0,0), for every t_0 ≠ 0, closure(Ñ) ∩ {t = t_0} has dimension ≤ 1.

  Consequently, if T̂ is a small representative of a 2-dimensional germ in closure(Ñ) at (0,0), then t − t_0 vanishes identically on no local irreducible component of T̂ at any of its points. Hence every slice T̂_{t_0} := T̂ ∩ {t = t_0} has pure dimension 1 wherever it is non-empty.

*Proof.*
- (a) q(p) ∈ H_t(c° ∖ Q) by definition of N_c. Since c° ∖ Q ⊂ closure(V_0) ∩ Δ_{G_c}, (R2) gives H_t(c° ∖ Q) ⊂ closure(V_t) ∩ Δ_{G_c}. So C_p has exactly |E(G_c)| nodes, i.e. |S(p)| = |E(G_c)| (fact K2). If s_e(p) ≠ 0, then s_e ≠ 0 near p. So S(p′) ⊂ S(p) for p′ near p, and on Ñ equality of cardinalities gives S(p′) = S(p). Thus S(·) is locally constant on the connected set Ñ. At points of (c̃ ∖ 0) × {0} it equals S (0.7).
- (b) (q × id) : B × Δ_ε → q(B) × Δ_ε is the orbit map of the finite group Aut(Q). Paths in the orbit space lift to paths starting at any preimage of the initial point (fact T1).
  - Let n ∈ N_c, and pick (p_0, 0) ∈ (c̃ ∖ 0) × {0} ⊂ Ñ. N_c is path connected, so there is a path in N_c from q(p_0) to n. Its lift starting at (p_0, 0) stays in (q × id)^{-1}(N_c) and is connected, so it lies in Ñ. Hence n ∈ (q × id)(Ñ).
  - The reverse inclusion holds by definition.
- (c) Let (p,t) ∈ closure(Ñ) be close to (0,0).
  - Then (q(p), t) lies in the closure of N_c, which is contained in H(c × Δ_ε) because c is closed and H is a homeomorphism onto the closed set closure(𝒱). So (q(p), t) = H(z, t) with z ∈ c, and z is close to Q because H is a homeomorphism with H_0 = id.
  - If z ≠ Q, then (q(p), t) ∈ N_c, so (p,t) lies in (q × id)^{-1}(N_c) and in the closure of its connected component Ñ. Connected components are closed in the space, so (p,t) ∈ Ñ.
  - If z = Q, then q(p) = Q_t, i.e. (p,t) ∈ Λ.
  - The inclusion closure(Ñ) ⊂ Z_S × Δ_ε follows from (a), since Z_S is closed.
  - At t = 0, (q(p), 0) = H(z, 0) = (z, 0) with z ∈ c, so p ∈ q^{-1}(c). The set q^{-1}(c) is a curve, because q is finite.
- (d) By (c) and (a), closure(Ñ) ∩ {t = t_0} ⊂ q^{-1}(H_{t_0}(c)) ∪ Λ_{t_0}.
  - H_{t_0}(c) is contained in the curve B_{t_0}, so q^{-1}(H_{t_0}(c)) has dimension ≤ 1.
  - Λ_{t_0} ⊂ q^{-1}(Q_{t_0}) is finite.

  For the consequence: a local component on which t ≡ t_0 would be a 2-dimensional subset of a slice of dimension ≤ 1, which is impossible. Krull's principal ideal theorem then gives pure dimension 1 for the slices. ∎

**Lemma 2.2 (Σ_c, 𝒬 and Λ are analytic at a puncture point).** Assume c is of boundary type (Q ∉ Δ_{G_c}).
- (a) Near (Q,0), Σ := (q × id)(closure(Ñ)) is a closed analytic set, equal to H(c × Δ_ε). Its germ at (Q,0) is irreducible of pure dimension 2.
- (b) Near (Q,0), 𝒬 = Σ ∩ (Δ_{G_Q} × Δ_ε) is a closed analytic curve. Λ = (q × id)^{-1}(𝒬) is closed analytic near (0,0), with Λ ∩ {t = 0} = {(0,0)} and Λ_t finite for every t.

*Proof.*
- (a) Analyticity and the equality.
  - q × id is proper (finite group quotient). closure(Ñ) is closed analytic near (0,0) (BB6). By Remmert's proper mapping theorem (fact A1), Σ is closed analytic near (Q,0).
  - By Lemma 2.1(b), Σ ⊃ N_c, and Σ is closed, so Σ ⊃ closure(N_c). Conversely Σ ⊂ closure((q × id)(Ñ)) = closure(N_c) by continuity.
  - Near (Q,0), closure(N_c) = H(c° × Δ_ε), because c° ∖ Q is dense in c° and H is a homeomorphism.
- (a) Irreducibility. Near (Q,0), Σ is homeomorphic to c° × Δ_ε, a topological 4-manifold. So every irreducible component of the germ has dimension 2: a component of dimension ≤ 1 would contain points, off the other components, where Σ has topological dimension ≤ 2.
  - Suppose the germ were Σ_1 ∪ Σ_2 with Σ_1 ⊄ Σ_2 and Σ_2 ⊄ Σ_1. Then dim(Σ_1 ∩ Σ_2) ≤ 1.
  - Take a neighbourhood U of (Q,0) in which Σ ∩ U is homeomorphic to a 4-ball and representatives of Σ_1, Σ_2 are defined.
  - The set (Σ ∩ U) ∖ (Σ_1 ∩ Σ_2) is connected, since a closed set of topological dimension ≤ 2 does not separate a connected 4-manifold (fact T2).
  - But it is the disjoint union of the relatively open sets Σ_1 ∖ Σ_2 and Σ_2 ∖ Σ_1, both non-empty for all small U. This is a contradiction.
- (b) By fact K2, q^{-1}(Δ_{G_Q}) ∩ B = {s_e = 0 for all e}, a closed Aut(Q)-invariant analytic set. So Δ_{G_Q} ∩ q(B) is closed analytic in q(B) (fact A1).
  - By (R2), Σ ∩ (Δ_{G_Q} × Δ_ε) = H((c ∩ Δ_{G_Q}) × Δ_ε) near (Q,0).
  - Here c ∩ Δ_{G_Q} = {Q}, because c ∖ Q ⊂ Δ_{G_c} and distinct strata are disjoint. So this set equals 𝒬, which is therefore analytic near (Q,0), and so is its preimage Λ.
  - Finally, q^{-1}(Q) = Aut(Q)·0 = {0} (fact K1), and q^{-1}(Q_t) is finite. ∎

*Remark.* 𝒬 is homeomorphic to a disc via t, so it is locally irreducible. Its normalisation maps biholomorphically onto Δ_ε, and t ↦ Q_t is therefore holomorphic. This is not needed below.

**Lemma 2.3 ((I1): lift-curves).** Let Q be a puncture point.
- (a) Every irreducible component L of the germ of Λ at (0,0) is a curve germ on which t is non-constant. In particular t(L) contains a neighbourhood of 0, and L ∩ {t = 0} = {(0,0)}. There is at least one lift-curve.
- (b) If L_0 is a lift-curve, the lift-curves are exactly the germs aL_0, a ∈ Aut(Q). So they form one Aut(Q)-orbit.
- (c) Every label is intact at every point of Λ (near (0,0)).

*Proof.*
- (a) Λ ∩ {t = 0} = {(0,0)} (Lemma 2.2(b)), so t is a finite map on Λ near (0,0) and dim Λ ≤ 1.
  - As t → 0, Q_t → Q. Since q is proper with q^{-1}(Q) = {0}, the non-empty sets q^{-1}(Q_t) converge to 0. So (0,0) is not isolated in Λ, the germ has positive dimension, and all its components are curves: a 0-dimensional component {(0,0)} would make (0,0) isolated.
  - On a component L, t ≢ 0, since L ⊄ {(0,0)}. By the open mapping property for a non-constant function on an irreducible curve germ (fact A3), t(L) is a neighbourhood of 0.
- (b) Each aL_0 is a component, because a is an automorphism of B × Δ_ε preserving t and Λ.
  - Let L be any component, and take small representatives. For (p,t) ∈ L with t ≠ 0 small, (a) gives (p′,t) ∈ L_0 with p′ near 0. Since q(p) = Q_t = q(p′), fact K1 gives p = ap′ for some a ∈ Aut(Q).
  - Hence L ⊂ ⋃_a aL_0 as germs. L is irreducible, so L ⊂ aL_0 for one a. Both are irreducible curve germs, so L = aL_0.
- (c) q(p) = Q_t ∈ Δ_{G_Q}, since H preserves strata. So all s_e(p) = 0 (fact K2). ∎

**Lemma 2.4 ((I3): equivariance).** Let a ∈ Aut(Q).
- (a) For p ∈ B and a label y: y is intact at ap iff a^{-1}y is intact at p, and then F_y(ap) ≅ F_{a^{-1}y}(p) as pointed curves (unordered special points).
- (b) a(Ñ_c̃) = Ñ_{ac̃}. If T is an anchored sheet of c̃, then aT is an anchored sheet of ac̃. ac̃ is a lift of the same branch c, so aT is of boundary type iff T is.
- (c) If L is a lift-curve, so is aL, and C_Φ(aL) = a·C_Φ(L). If z is Φ-persistent on T with function φ, then az is Φ-persistent on aT with function φ.

*Proof.*
- (a) This is fact K3.
- (b) (q × id)^{-1}(N_c) is a-invariant, because q∘a = q. So a permutes its connected components, and the image of Ñ_c̃ is the component containing a((c̃ ∖ 0) × {0}) = (ac̃ ∖ 0) × {0}, i.e. Ñ_{ac̃}.
  - a is a biholomorphism of B × Δ_ε fixing (0,0). So it maps closure(Ñ_c̃) onto closure(Ñ_{ac̃}), and the germ components at (0,0) of the one onto those of the other.
  - If T ⊃ c̃ × {0}, then aT ⊃ ac̃ × {0}.
  - ac̃ is a component of the germ q^{-1}(c), because q∘a = q.
- (c) Λ is a-invariant, so aL is a lift-curve. By (a), v_y(ap,t) = v_{a^{-1}y}(p,t). So v_y(aL) = v_{a^{-1}y}(L) as germs, which gives y ∈ C_Φ(aL) ⟺ a^{-1}y ∈ C_Φ(L). The statement for T is the same computation, together with: az intact at ap ⟺ z intact at p. ∎

**Lemma 2.5 ((I2): every anchored sheet of boundary type contains a lift-curve).** Let Q be a puncture point, c of boundary type, and T an anchored sheet of c̃. Then T contains a lift-curve.

*Proof.*
- Let B′ ⊂ B be any smaller Aut(Q)-invariant ball and 0 < ε′ ≤ ε. Let T̂ be a representative of T that is closed analytic in B′ × Δ_{ε′}, of pure dimension 2 (BB6).
- By Remmert (fact A1), (q × id)(T̂) is closed analytic in q(B′) × Δ_{ε′}.
- Its germ at (Q,0) is the image of the germ T, since (0,0) is the only preimage of (Q,0). So it is 2-dimensional, because q × id is finite.
- It is contained in the germ of Σ, which is irreducible and 2-dimensional (Lemma 2.2(a)). Hence it equals the germ of Σ, which contains 𝒬.
- So for all small t there is (p,t) ∈ T̂ with q(p) = Q_t, i.e. T̂ ∩ Λ has points with t ≠ 0 in every B′ × Δ_{ε′}.
- Therefore the analytic germ T ∩ Λ is not contained in {(0,0)}. It has a 1-dimensional irreducible component. That component is an irreducible curve germ inside the germ Λ, so it lies in a component of Λ and equals it by dimension. ∎

**Lemma 2.6 (a sheet maps into one component W).** Let T be an anchored sheet of c̃ (any type). Fix a graph isomorphism ι : G_S → G_c, and put Π := ι_*∘Π_S : Z_S → ∏_{w∈V(G_c)} M̄_w.
- (a) There is W ∈ 𝒲, a component of 𝒲_{G_c}, such that (Π, t)(T̂) ⊂ W for a small representative T̂ of T.
- (b) Π(c̃ ∖ 0) lies in a single lifted piece E at time 0, and closure(E) is an irreducible component of W_0.
- (c) For (p,t) ∈ T̂ and u ∉ M_W: Π(p)[u] ∈ M_u and (Π(p)[u], t) ∈ Γ_{W,u}.

*Proof.*
- (a) Set-up. By Lemma 2.1(c), T̂ ⊂ Z_S × Δ_ε, so (Π, t) is defined and continuous on T̂.
  - Ñ is dense in closure(Ñ). The points of T̂ lying on no other germ component of closure(Ñ) form a dense open subset of T̂. Hence T̂ ∩ Ñ is dense in T̂.
  - For (p,t) ∈ Ñ we have p ∈ Z_S^∘ (Lemma 2.1(a)). So Π(p) ∈ ∏M_w and ξ_{G_c}(Π(p)) = q(p) ∈ closure(V_t) ∩ Δ_{G_c} (fact PN(ii)), i.e. (Π(p), t) ∈ 𝒲_{G_c}.
  - By closedness, (Π, t)(T̂) ⊂ 𝒲_{G_c}.
- (a) Choice of W. Only finitely many components of 𝒲_{G_c} pass through (Π(0), 0). Their preimages are analytic subgerms covering the irreducible germ T, so T maps into one of them, W.
  - On T̂ ∩ Ñ, (Π, t) has finite fibres: Π_S has finite fibres on Z_S^∘ (fact PN(v)). So the image of the 2-dimensional germ T is 2-dimensional (fact A4), and dim W ≥ 2.
  - By 0.5, dim W ≤ 2. So W ∈ 𝒲.
- (b) For p ∈ c̃ ∖ 0, S(p) = S and q(p) ∈ c ∖ Q ⊂ closure(V_0) ∩ Δ_{G_c}. So Π(c̃ ∖ 0) ⊂ ξ_{G_c}^{-1}(closure(V_0) ∩ Δ_{G_c}).
  - The irreducible components of that analytic set are countably many. c̃ ∖ 0 is a connected punctured disc (on its normalisation), and Π is non-constant on it.
  - So the preimage of some component is not discrete. It is then all of c̃ ∖ 0, by the identity theorem on the normalisation (Baire). That component is 1-dimensional, i.e. a lifted piece E.
  - E × {0} meets the analytic set W_0 ∩ (∏M_w) in a set with non-empty interior in E. E is irreducible, so E ⊂ W_0, and closure(E) ⊂ W_0.
  - W_0 has pure dimension 1 (BB3, consequence), so the irreducible curve closure(E) is a component of W_0.
- (c) (Π(p), t) ∈ W_t lies on a component K_W × {c_D} (BB3). Hence Π(p)[u] = c_D[u] ∈ M_u, and (c_D[u], t) ∈ Γ_{W,u}. ∎

**Lemma 2.7 (Y ∈ Φ).** Assume Y is non-constant. Let E be a lifted piece in Δ_Γ at time 0, i.e. over a piece of ∂V_0, and let W ∈ 𝒲 be a component of 𝒲_Γ such that closure(E) is a component of W_0. Then:
- i ∉ M_W;
- Γ_{W,i} = graph(Y|_{Δ_*});
- the germ of graph([Y]) at (Y_0,0) is a non-constant irreducible germ belonging to Φ.

Such a W exists: apply Lemma 2.6(a),(b) to an anchored sheet of the lift β̃_1 at J_1 (BB1), with E := E^1.

*Proof.*
- For z ∈ E, ξ_Γ(z) ∈ ∂V_0, so z[i] = π_i(ξ_Γ(z)) = Y_0. Here we use product type: π_i∘ξ_Γ = pr_i. So i is constant on the fibre component closure(E), and i ∉ M_W by (U1).
- Let D = K_W × {c_D} be a component of W_t. K_W is not contained in the boundary, so D contains points z ∈ ∏M_w. They lie in 𝒲_Γ ∩ (∏M_w × Δ_*) = 𝒲_Γ^∘, so ξ_Γ(z) ∈ closure(V_t) ∩ Δ_Γ = ∂V_t, and c_D[i] = z[i] = Y_t.
- Hence Γ_{W,i} ⊂ graph(Y). Y is holomorphic (BB2), so graph(Y) is an irreducible closed curve. Γ_{W,i} is a closed curve surjecting onto Δ_*, so Γ_{W,i} = graph(Y).
- Its image in 𝔐 × Δ_* is graph([Y]). This is the graph of a holomorphic map, so its germ at (Y_0,0) is irreducible, and it is non-constant because [Y] is non-constant (0.2).
- i has type (g_i,n_i). So the germ lies in Φ. ∎

**Lemma 2.8 (Φ avoids 𝔉 off t = 0).** After shrinking ε, for every φ ∈ Φ:
- φ_t ∩ 𝔉 = ∅ for 0 < |t| < ε;
- φ̂ ∩ {t = 0} = {(Y_0,0)}.

*Proof.*
- For f ∈ 𝔉, the germ φ ∩ ({f} × Δ_*) is a proper analytic subgerm of the irreducible 1-dimensional germ φ. If f = Y_0 this is because φ is non-constant; if f ≠ Y_0, the line {f} × Δ_* does not pass through (Y_0,0). So it is ⊂ {(Y_0,0)}.
- φ ⊄ {t = 0}, because φ lies in a curve that is finite over Δ_*.
- Φ and 𝔉 are finite. ∎

---

## III.3. The Φ-dichotomy at punctures

Part II Theorem A.9 is stated for Y and a generic time t ∉ Z. We need it for every φ ∈ Φ, but only at points that are punctures of the piece. In that case its trichotomy STAY / IMOV / excluded collapses: IMOV requires the point to lie in the stratum of the piece. We run its argument with Y replaced by φ. The only property of the time t that it uses is "the value avoids the finite set 𝔉". For a Puiseux branch φ this is read as φ_t ∩ 𝔉 = ∅, and by Lemma 2.8 it holds for **all** 0 < |t| < ε. So no discrete exceptional set Z_Φ is needed at all.

**Proposition 3.1 (Φ-dichotomy at a puncture).** Let Q be a puncture point, c of boundary type, c̃ a lift, T an anchored sheet of c̃, and T̂ a small representative. Let ι, Π, W be as in Lemma 2.6. Suppose:
- 0 < |t| < ε and (p,t) ∈ T̂ ∩ Λ (so q(p) = Q_t);
- y is a label with [F_y(p)] ∈ φ_t for some φ ∈ Φ (y is intact at p by Lemma 2.3(c));
- b is an irreducible component of the germ at p of the slice T̂_t.

Then y is intact at every point of b, and p′ ↦ F_y(p′) is constant on b.

(In the language of Part II Theorem A.9: y is STAY along b, MERGE and puncture-MOV being excluded.)

*Proof.*
- **Set-up.** By Lemma 2.1(d), b is an irreducible curve germ at p. Λ_t is finite, and T̂ ∖ Λ ⊂ Ñ by Lemma 2.1(c). So b ∖ {p} ⊂ Ñ ⊂ Z_S^∘ × Δ_ε.
  - By Lemma 2.6(a), Π(b) ⊂ W_t. Π has finite fibres on Z_S^∘, so Π(b) is an irreducible 1-dimensional germ at Π(p). It therefore lies in one component D = K_W × {c_D} of W_t (BB3).
  - Write Π(p′) = (κ(p′), c_D) for p′ ∈ b, with κ(p′) ∈ K_W.
- **Π(p) is a puncture value.** ξ̄_{G_c}(Π(p)) = q(p) = Q_t (fact PN(ii)). Q ∉ Δ_{G_c} and H_t preserves strata, so Q_t ∉ Δ_{G_c} = ξ_{G_c}(∏M_w). Hence Π(p) ∉ ∏M_w. Since c_D ∈ ∏_{u∉M_W} M_u, the point κ := κ(p) has a coordinate in the boundary, i.e. κ ∈ F_W.
- Let u be the vertex of G_S that contains y, transported to G_c by ι.
- **Step 1 (MERGE excluded).** Suppose some edge e at y is not in S. Then e is contracted in G_S, so e joins two vertices of u (possibly y to itself).
  - By fact PN(iii), Π(p)[u] is the curve glued from the components of C_p labelled by the vertices of u, along the edges outside S joining them. It contains the node e, so Π(p)[u] ∈ ∂M̄_u.
  - If u ∉ M_W, then Π(p)[u] = c_D[u] ∈ M_u, a contradiction. So u ∈ M_W and Π(p)[u] = κ[u].
  - By PN(iii), F_y(p) with all its special points is an irreducible component, with its special points, of κ[u]. All edges are pinched at p ∈ Λ, so the special points of F_y(p) are exactly the half-edges at y, and these are exactly its special points in κ[u]: half-edges outside S become nodes of κ[u], half-edges in S become marked points.
  - Hence [F_y(p)] ∈ 𝔉_W ⊂ 𝔉. But [F_y(p)] ∈ φ_t, and φ_t ∩ 𝔉 = ∅ (Lemma 2.8). Contradiction.
  - So every edge at y lies in S. Then y is intact on Z_S ⊃ b, u = {y} is a vertex of G_S, and F_y = Π(·)[{y}] on Z_S (PN(iii)).
- **Step 2 (puncture-MOV excluded).** Suppose {y} ∈ M_W. Then F_y(p) = κ[{y}] is a coordinate of κ ∈ F_W, and it is a smooth curve because F_y(p) ∈ M_y. So [F_y(p)] ∈ 𝔉_W ⊂ 𝔉, which again contradicts Lemma 2.8.
  - Hence {y} ∉ M_W, and F_y(p′) = Π(p′)[{y}] = c_D[{y}] for every p′ ∈ b. ∎

*Remark.* No genericity of t beyond 0 < |t| < ε was used, and no comparison of different copies of Y_0 was made. The proof uses only BB3 (through F_W, 𝔉 and the product form K_W × {c_D}) and fact PN.

---

## III.4. Values along lift-curves; persistence equals lift-curve values; Proposition 4

**Lemma 1 (values along a lift-curve: Φ or rigid).** Let Q be a puncture point, T a boundary-type anchored sheet at Q, L ⊂ T a lift-curve, and y a label with [F_y(0)] = Y_0. Then the image germ v_y(L) is either a branch φ ∈ Φ (so y ∈ C_Φ(L)) or the germ of {Y_0} × Δ (y is a rigid Y_0-copy along L).

*Proof.*
- **Step 1.** y is intact on L (Lemma 2.3(c)), so v_y is holomorphic on L. The t-component of v_y is finite on L (Lemma 2.3(a)), so v_y|_L is a finite map. Hence v_y(L) is an irreducible 1-dimensional germ at v_y(0,0) = (Y_0, 0) (fact A4).
- **Step 2 (the components of Q_t).** Let ι, Π, W be as in Lemma 2.6 for T, and T̂ a small representative. Let (p_*, t) ∈ L with 0 < |t| < ε.
  - By Lemma 2.1(d), T̂_t has pure dimension 1 at p_*. Λ_t is finite. So there are points p_n ∈ T̂_t ∖ Λ ⊂ Ñ with p_n → p_*.
  - By Lemma 2.6(a), Π(p_n) ∈ W_t. W_t has finitely many components; pass to a subsequence lying in one of them, K_W × {c_D}. Then Π(p_n) = (κ_n, c_D) with κ_n ∈ K_W.
  - Π is continuous on Z_S, so Π(p_*) = lim Π(p_n) = (κ_∞, c_D) with κ_∞ ∈ K_W (K_W is compact).
  - As in the proof of Proposition 3.1, ξ̄(Π(p_*)) = Q_t ∉ Δ_{G_c}, so κ_∞ ∈ F_W.
  - Q_t = q(p_*) is the curve obtained by gluing the coordinates of (κ_∞, c_D) (fact PN(ii)). Gluing identifies marked points pairwise and does not change the set of special points on any irreducible component.
  - So every irreducible component of Q_t, with its special points, is of one of two kinds:
    - **(a)** a whole coordinate c_D[w] with w ∉ M_W; then (c_D[w], t) ∈ Γ_{W,w};
    - **(b)** a component of a coordinate κ_∞[w] with w ∈ M_W; if it has type (g_i,n_i), its class lies in 𝔉_W.
  - F_y(p_*) is the component of Q_t labelled y, of type (g_i,n_i).
  - Hence v_y(p_*, t) ∈ 𝒢 := ⋃ {Γ̄_{W,w} : w ∉ M_W of type (g_i,n_i)} ∪ (𝔉_W × Δ_*). This is a closed analytic curve in 𝔐 × Δ_*.
- **Step 3 (the dichotomy).** By Step 2 and closedness, v_y(L) ⊂ 𝒢 as germs at (Y_0,0).
  - An irreducible 1-dimensional germ inside a 1-dimensional analytic germ equals one of its irreducible components. So v_y(L) is either a branch at (Y_0,0) of some Γ̄_{W,w} (w ∉ M_W of type (g_i,n_i)), or the germ of {f} × Δ for some f ∈ 𝔉_W. In the second case f = Y_0, since the germ passes through (Y_0,0).
  - In the first case: if the branch is non-constant, it belongs to Φ by definition (W ∈ 𝒲). Otherwise it is the germ of {Y_0} × Δ. ∎

**Lemma 2 ((NRT_P) at Q ⇔ C_Φ is Aut(Q)-invariant).** Let Q be a puncture point. Then Lemma 1 applies to every lift-curve L at Q. Moreover the following are equivalent:
- (i) there is no (a, L, x) at Q as excluded in (NRT_P);
- (ii) C_Φ(L) is Aut(Q)-invariant for some lift-curve L;
- (iii) C_Φ(L) is Aut(Q)-invariant for every lift-curve L, and C_Φ(L) = C_Φ(L′) for all lift-curves L, L′ at Q.

*Proof.*
- **Lemma 1 applies everywhere.** Q has a boundary-type branch c. Let c̃ be a lift and T an anchored sheet of c̃ (both exist, 0.7). By Lemma 2.5, T contains a lift-curve L_1. By Lemma 2.3(b), every lift-curve has the form aL_1. Then aL_1 ⊂ aT, which is a boundary-type anchored sheet of ac̃ (Lemma 2.4(b)).
- **(i) ⇒ (iii).** Let L be a lift-curve, x ∈ C_Φ(L) with branch φ, and a ∈ Aut(Q).
  - v_x(0,0) = (Y_0,0), so [F_x(0)] = Y_0.
  - By Lemma 2.4(a) with p = 0 (a fixes 0), F_{a^{-1}x}(0) ≅ F_x(0), so [F_{a^{-1}x}(0)] = Y_0.
  - By Lemma 1, a^{-1}x is in C_Φ(L) or is a rigid Y_0-copy along L. The second alternative is exactly the configuration excluded by (i). Hence a^{-1}x ∈ C_Φ(L).
  - As a ranges over the group Aut(Q), this shows that C_Φ(L) is Aut(Q)-invariant.
  - Then for every a, C_Φ(aL) = a·C_Φ(L) = C_Φ(L) (Lemma 2.4(c)). By Lemma 2.3(b) this covers all lift-curves.
- **(iii) ⇒ (ii).** Trivial.
- **(ii) ⇒ (i).** Suppose (a, L′, x) is an excluded configuration, and let L be the lift-curve in (ii). By Lemma 2.3(b), L′ = hL for some h ∈ Aut(Q), and C_Φ(L′) = h·C_Φ(L), which is Aut(Q)-invariant.
  - x ∈ C_Φ(L′), so a^{-1}x ∈ C_Φ(L′), i.e. v_{a^{-1}x}(L′) ∈ Φ.
  - But v_{a^{-1}x}(L′) is the germ of {Y_0} × Δ, which is not in Φ. Contradiction. ∎

**Lemma 3 (P_Φ(T) = C_Φ(L)).** Let Q be a puncture point, T a boundary-type anchored sheet at Q, and L ⊂ T a lift-curve. Then P_Φ(T) = C_Φ(L). Moreover, the function on T of a label y ∈ P_Φ(T) is the branch v_y(L).

*Proof.*
- **(⊂).** Let y ∈ P_Φ(T) with function φ. y is intact on L ⊂ T, and v_y(L) ⊂ v_y(T) ⊂ φ. By Lemma 1, Step 1, v_y(L) is a 1-dimensional irreducible germ, so v_y(L) = φ ∈ Φ and y ∈ C_Φ(L).
- **(⊃), the analytic set A_y.** Let y ∈ C_Φ(L), with φ := v_y(L) ∈ Φ. Let T̂ be a small representative of T, closed analytic in a neighbourhood U of (0,0), with L̂ ⊂ T̂. Put

  A_y := {(p,t) ∈ T̂ : y intact at p and ([F_y(p)], t) ∈ Γ̄_all}.

  A_y is a closed analytic subset of T̂: L_y is closed analytic, F_y is holomorphic on it, and Γ̄_all is closed analytic.
- **The slices.** For 0 < |t| < ε and (p,t) ∈ L̂, we have [F_y(p)] ∈ φ_t.
  - By Proposition 3.1, along every irreducible component b of the germ of T̂_t at p, y is intact and F_y is constant, equal to F_y(p). Its class lies in φ_t ⊂ Γ̄_all.
  - So A_y contains the germ of T̂_t at (p,t), which is 1-dimensional (Lemma 2.1(d)).
- **Countability argument.** By Lemma 2.3(a), such points (p,t) exist for every t in a punctured disc, i.e. for uncountably many t, inside every neighbourhood of (0,0).
  - If the germ A_y had dimension ≤ 1, some representative in a neighbourhood U′ ⊂ U would have dimension ≤ 1. Its 1-dimensional irreducible components are countably many (local finiteness). Each one either lies in a single level {t = t_0} or meets every level in a discrete set.
  - A 1-dimensional germ of A_y ∩ {t = t_0} must lie in a component contained in {t = t_0}. So only countably many levels could carry such germs. This is a contradiction.
  - Hence the germ A_y is 2-dimensional. T is an irreducible 2-dimensional germ, so A_y = T as germs (all statements are germ statements, and the uncountably many slices occur in every neighbourhood).
- **Single branch.** Thus y is intact on T, and v_y(T) ⊂ Γ̄_all. Γ̄_all has finitely many irreducible branches at (Y_0,0). Their preimages under v_y are analytic subgerms covering the irreducible germ T, so v_y(T) lies in one branch φ′.
  - Then φ = v_y(L) ⊂ φ′. Both are irreducible 1-dimensional germs, so φ′ = φ ∈ Φ.
  - Hence y ∈ P_Φ(T), with function φ. ∎

**Proposition 4 (transfer between boundary-type sheets at one puncture point).** Assume (NRT_P). Let Q be a puncture point, T, T′ boundary-type anchored sheets at Q (of lifts c̃, c̃′, equal or not, of the same or different branches), and x ∈ P_Φ(T). Then:
- x ∈ P_Φ(T′);
- if T′ is an anchored sheet of c̃′, then x is intact along c̃′ and [F_x] ≡ Y_0 on c̃′ near 0.

The second item holds for any anchored sheet T′ of c̃′ with x ∈ P_Φ(T′); it does not use (NRT_P).

*Proof.*
- By Lemma 2.5, choose lift-curves L ⊂ T and L′ ⊂ T′.
- By Lemma 3, x ∈ C_Φ(L). By (NRT_P) and Lemma 2 (i) ⇒ (iii), C_Φ(L′) = C_Φ(L) ∋ x. By Lemma 3 for T′, x ∈ P_Φ(T′).
- **Last clause.** Let ψ be the function of x on T′. Since c̃′ × {0} ⊂ T′, x is intact along c̃′, and v_x(p,0) ∈ ψ̂ ∩ {t = 0} = {(Y_0,0)} for p ∈ c̃′ near 0 (Lemma 2.8). ∎

---

## III.5. Lemma 5 (Φ-transfer along a travel interval)

**Lemma 5.** Let 1 ≤ m ≤ k − 1. Let T be an anchored sheet of the leaving lift β̃′_m (in Def(J_m)) with x_m ∈ P_Φ(T), with function φ. Then there is an anchored sheet T″ of the entering lift β̃_{m+1} (in Def(J_{m+1})) with x_{m+1} ∈ P_Φ(T″), with some function ψ ∈ Φ, possibly ψ ≠ φ. Neither (NRT_P) nor boundary type is used.

*Proof.* Write G := G(D^{m+1}), E := E^{m+1}, c := c_{m+1} (BB1-M).

**Step 1 (the component 𝒲̃).**
- In Def(J_m), the branch β′_m of closure(D^{m+1}) has β′_m ∖ J_m ⊂ D^{m+1} ⊂ Δ_G, so G_{β′_m} = G.
- Put S′ := S(β̃′_m) and Π′ := (ι′_m)_*∘Π_{S′}.
- By Lemma 2.6(a), applied with ι := ι′_m, there is 𝒲̃ ∈ 𝒲, a component of 𝒲_G, with (Π′, t)(T̂) ⊂ 𝒲̃.
- By BB1-M, Π′(β̃′_m ∖ 0) ⊂ E. So by Lemma 2.6(b), closure(E) is a component of 𝒲̃_0.
- c is constant on E, so **c ∉ M_𝒲̃** by (U1).

**Step 2 (x_m is the vertex c on T).**
- x_m is intact on T ⊃ β̃′_m × {0}, hence along β̃′_m. By BB1-M, ι′_m({x_m}) = c.
- By fact PN(iii), F_{x_m}(p) = Π′(p)[c] for p ∈ Z_{S′}. By Lemma 2.6(c), (Π′(p)[c], t) ∈ Γ_{𝒲̃,c} for (p,t) ∈ T̂.
- Since [F_{x_m}(0)] = Y_0, the vertex c has type (g_i,n_i).
- Put Γ̄ := Γ̄_{𝒲̃,c}, a closed irreducible curve in 𝔐 × Δ_*, finite over Δ_*. We get v_{x_m}(T̂) ⊂ Γ̄.

**Step 3 (Γ̄ ⊃ φ).**
- t is non-constant on the irreducible germ T (Lemma 2.1(c)), so t(T̂) contains a neighbourhood of 0 (fact A3).
- Hence v_{x_m}(T̂), which lies in φ̂ ∩ Γ̄, meets 𝔐 × {t} for every small t.
- So the germ φ ∩ Γ̄ is an analytic subgerm of the irreducible curve germ φ that is not ⊂ {(Y_0,0)}. Hence it equals φ, i.e. φ ⊂ Γ̄.

**Step 4 (every branch of Γ̄ at (Y_0,0) lies in Φ).**
- Suppose some branch of Γ̄ at (Y_0,0) were the germ of {Y_0} × Δ. Then Γ̄ ∩ ({Y_0} × Δ_*) would be an analytic subset of the irreducible curve Γ̄ of dimension 1, hence all of Γ̄ (fact A2), and Γ̄ ⊂ {Y_0} × Δ_*.
- This contradicts φ ⊂ Γ̄ with φ non-constant.
- So every branch of Γ̄ at (Y_0,0) is non-constant. Since 𝒲̃ ∈ 𝒲 and c ∉ M_𝒲̃ is of type (g_i,n_i), every such branch belongs to Φ.

(This replaces the Y-version's "persistence holds on all of 𝒲̃": the function may change from φ to another branch of the same irreducible Γ̄, but it can never become constant.)

**Step 5 (a sheet T″ of β̃_{m+1} mapping into 𝒲̃).** Work in Def(J_{m+1}).
- Put β̃ := β̃_{m+1}, of the branch β := β_{m+1} of closure(D^{m+1}). Put S″ := S(β̃) and Π″ := (ι_{m+1})_*∘Π_{S″}. By BB1-M, Π″(β̃ ∖ 0) ⊂ E.
- Choose p̃ ∈ β̃ ∖ 0 so close to 0 that the following hold:
  - (α) closure(Ñ_β̃) is analytic of pure dimension 2 near (p̃,0) (BB6);
  - (β) q(p̃) is a smooth point of the curve B_0, near which B_0 coincides with D^{m+1}, hence with β. All but finitely many points of β ∖ J_{m+1} near J_{m+1} qualify: B_0 has finitely many singular points, and β ∖ J_{m+1} ⊂ D^{m+1}.
- Put z := Π″(p̃) ∈ E. Then (z,0) ∈ 𝒲̃, by Step 1.
- **(i)** Δ_G ⊂ ∂M̄_g, so closure(V_0) ∩ Δ_G = B_0 ∩ Δ_G. By (β), this coincides with β near q(p̃). By (R2), near (q(p̃), 0),
  closure(𝒱) ∩ (Δ_G × Δ) = H((closure(V_0) ∩ Δ_G) × Δ) = H(β × Δ),
  and this is the transport base N_β near that point.
- **(ii)** Let (p,t) be near (p̃,0).
  - If (q(p),t) ∈ closure(𝒱) ∩ (Δ_G × Δ), then |S(p)| = |E(G)| = |S″| and S(p) ⊂ S(p̃) = S″. So S(p) = S″ and p ∈ Z_{S″}^∘.
  - Conversely, points of Z_{S″} near p̃ lie in Z_{S″}^∘, because s_e(p̃) ≠ 0 for e ∉ S″.
  - Since ξ_G∘Π″ = q on Z_{S″}^∘ (fact PN(ii)), near (p̃,0) we get
    (q × id)^{-1}(N_β) = {(p,t) ∈ Z_{S″} × Δ_ε : (Π″(p), t) ∈ 𝒲_G}.
- **(iii)** By fact PN(iv), Π″ × id is a finite open map from a neighbourhood of (p̃,0) in the manifold Z_{S″} × Δ_ε onto a neighbourhood of (z,0) in ∏M_w × Δ_*. These manifolds have the same dimension.
  - Hence the germ at (p̃,0) of (Π″ × id)^{-1}(𝒲̃) has dimension 2. It is ≤ 2 by finiteness and ≥ 2 by openness (fact A4).
  - Let Z be a 2-dimensional irreducible component of this germ.
- **(iv)** By (ii), Z ⊂ (q × id)^{-1}(N_β). Take a connected representative of Z containing (p̃,0) (fact A5). Since (p̃,0) ∈ Ñ_β̃, which is a connected component of (q × id)^{-1}(N_β), this representative lies in Ñ_β̃.
- **(v)** The germ of closure(Ñ_β̃) at (p̃,0) is the union of the germs of its global irreducible components through (p̃,0). Let 𝒯 be one containing Z. It has pure dimension 2 and lies in Z_{S″} × Δ_ε (Lemma 2.1(c)).
  - 𝒯 ∩ (Π″, t)^{-1}(𝒲̃) is an analytic subset of the irreducible 𝒯 containing the 2-dimensional germ Z. So it is 𝒯 (fact A2), i.e. (Π″, t)(𝒯) ⊂ 𝒲̃.
- **(vi)** By Lemma 2.1(c),(d) and Krull, Z ∩ {t = 0} has pure dimension 1 at (p̃,0). It lies in q^{-1}(β) × {0}, and near p̃ this equals β̃ × {0}, since distinct lifts of β meet only at 0.
  - So 𝒯 ∩ (β̃ × {0}) contains a non-empty open subset of the irreducible curve β̃ ∩ B (B a Milnor ball, fact A5). Hence it contains all of β̃ ∩ B, and (0,0) ∈ 𝒯.
- **(vii)** 𝒯 has pure dimension 2, and so does closure(Ñ_β̃). So each irreducible component of the germ of 𝒯 at (0,0) is a component of the germ of closure(Ñ_β̃) at (0,0).
  - The irreducible germ β̃ × {0} lies in one of them, T″. So T″ is an anchored sheet of β̃_{m+1}, and (Π″, t)(T″) ⊂ 𝒲̃.

**Step 6 (x_{m+1} on T″).**
- By BB1-M, x_{m+1} is intact along β̃ and ι_{m+1}({x_{m+1}}) = c. So x_{m+1} is intact on Z_{S″} ⊃ T″, and F_{x_{m+1}} = Π″(·)[c] there (fact PN(iii)).
- For (p,t) ∈ T̂″, (Π″(p), t) ∈ 𝒲̃_t lies on a component K_𝒲̃ × {c_D}. Since c ∉ M_𝒲̃, Π″(p)[c] = c_D[c] with (c_D[c], t) ∈ Γ_{𝒲̃,c}. So v_{x_{m+1}}(T̂″) ⊂ Γ̄.
- At the origin: for p ∈ β̃ ∖ 0, Π″(p) ∈ E, on which c is constant of class Y_0. By continuity, [F_{x_{m+1}}(0)] = Y_0.
- So v_{x_{m+1}}(T″) is a germ at (Y_0,0) inside Γ̄. Since T″ is irreducible, it lies in a single branch ψ of Γ̄ at (Y_0,0): the preimages of the branches are analytic subgerms covering T″.
- By Step 4, ψ ∈ Φ. Hence x_{m+1} ∈ P_Φ(T″) with function ψ. ∎

---

## III.6. Proof of Theorem B

**Lemma 6.1 (base).** Assume Y is non-constant. For every anchored sheet T of β̃_1 (in Def(J_1)):
- x_1 is Y-persistent on T;
- consequently x_1 ∈ P_Φ(T), with function the germ of graph([Y]), which belongs to Φ by Lemma 2.7.

*Proof.*
- Put S := S(β̃_1) and Π := (ι_1)_*∘Π_S. By BB1-M (with m = 1, c_1 = i), x_1 is intact along β̃_1 and ι_1({x_1}) = i. So x_1 is intact on Z_S, and F_{x_1} = Π(·)[i] there (fact PN(iii)).
- Let (p,t) ∈ Ñ_{β̃_1}. By Lemma 2.1(a), p ∈ Z_S^∘ and q(p) ∈ H_t(β_1 ∖ J_1) ⊂ closure(V_t) ∩ Δ_Γ = ∂V_t, since β_1 ∖ J_1 ⊂ D^1 ⊂ Δ_Γ.
- By fact PN(ii), ξ_Γ(Π(p)) = q(p). By product type, Π(p)[i] = π_i(q(p)) = Y_t. So [F_{x_1}(p)] = [Y_t].
- Ñ_{β̃_1} is dense in a representative of T (proof of Lemma 2.6(a)), and both sides are continuous on Z_S × Δ_ε. Hence [F_{x_1}] = [Y_t] on all of T̂, and v_{x_1}(T) ⊂ graph([Y]). ∎

**The induction.** Suppose, for contradiction, that Y is non-constant. Then BB1 applies. For m = 1, …, k consider:

**(C_m)** There is an anchored sheet T_m of β̃_m (in Def(J_m)) with x_m ∈ P_Φ(T_m).

- **(C_1)** holds by Lemma 6.1, because anchored sheets of β̃_1 exist (0.7).
- **(C_m) ⇒ (C_{m+1})** for 1 ≤ m ≤ k − 1. First we produce an anchored sheet T′_m of the leaving lift β̃′_m with x_m ∈ P_Φ(T′_m). The two cases are exhaustive.
  - **Case (a): J_m ∈ Δ_{G(D^m)} ∪ Δ_{G(D^{m+1})}.** By BB1 (IMOV_all), β̃′_m = β̃_m with the same label. Take T′_m := T_m.
  - **Case (b): otherwise.** By BB1 (P), J_m is a puncture point, and β̃_m, β̃′_m are of boundary type. Let T′_m be any anchored sheet of β̃′_m (0.7). Proposition 4, applied at Q = J_m to T = T_m and T′ = T′_m, gives x_m ∈ P_Φ(T′_m). This is the only place, besides the endpoint, where (NRT_P) is used.

  Lemma 5 applied to T′_m then gives (C_{m+1}).
- **Endpoint.** By (C_k), x := x_k ∈ P_Φ(T_k) for an anchored sheet T_k of β̃_k at Q_0. By BB1 (P), Q_0 is a puncture point and β̃_k, b̃ are of boundary type.
  - Let T_b be an anchored sheet of b̃. By Proposition 4, x ∈ P_Φ(T_b), and x is intact along b̃ with [F_x] ≡ Y_0 on b̃ near 0.
  - **MERGE is impossible.** For an edge e at x, s_e vanishes on b̃ near 0, hence on the irreducible germ b̃. So e ∈ S(b̃).
  - **MOV is impossible.**
    - x is intact along b̃, so F_x is holomorphic on the irreducible curve b̃ ∩ B.
    - Let n : D → b̃ ∩ B be the normalisation, where D is a disc (connected).
    - [F_x]∘n : D → 𝔐 is holomorphic and equals Y_0 on a non-empty open set. The preimage of the point Y_0 is an analytic subset of D with interior, so it is all of D (fact A2).
    - Hence [F_x] ≡ [Y_0] on b̃ ∩ B, contradicting MOV.
  - Since BB1 asserts MERGE or MOV at the endpoint, we have a contradiction. (The case k = 1 is included: then J_1 = Q_0 and the induction is empty.)

Hence Y is constant, so Y_t = Y_0 for all t ∈ Δ. ∎ (main statement of Theorem B)

**Where the hypotheses enter.**
- (R1), (R2): everywhere.
- (Rig): only through BB3, used in Lemmas 2.6, 2.7, Proposition 3.1, Lemma 1 and Lemma 5.
- Product type: Lemmas 2.7 and 6.1.
- (NRT_P): only through Lemma 2, i.e. Proposition 4, at the puncture transitions of case (b) and at Q_0. All of these are puncture points, so (NRT_P), which is stated only at puncture points, suffices.
- dim M_{g_i,n_i} > 0 is used only to make the non-constancy assumption meaningful. If dim M_{g_i,n_i} = 0, Y is trivially constant.

**6.2 The "moreover" clauses.**
- **(NRT_P) is implied by the problem's conclusion.** The setting of (NRT_P) (0.9) includes "t ↦ Y_t is non-constant". If the problem's conclusion holds for a family, i.e. Y_t = Y_0 for all t, that family does not satisfy the setting, and (NRT_P) holds vacuously for it.
- **A counterexample to (NRT_P) is a counterexample to the problem.** Such a counterexample is a family satisfying the setting of (NRT_P) and admitting a configuration (Q, a, L, x). In particular it satisfies the problem's hypotheses (in the readings (R1), (R2)) and has Y non-constant, so the problem's conclusion fails for it. Theorem B and this remark together say that, under (Rig), the problem and (NRT_P) are equivalent.
- **Isotropy drop.** Let (Q, a, L, x) be a configuration violating (NRT_P).
  - Then aL ≠ L. Otherwise C_Φ(L) = C_Φ(aL) = a·C_Φ(L) (Lemma 2.4(c)), so C_Φ(L) = a^{-1}·C_Φ(L) ∋ a^{-1}x. But a^{-1}x is a rigid Y_0-copy along L, so v_{a^{-1}x}(L) ∉ Φ. Contradiction.
  - L and aL are distinct irreducible curve germs, so after shrinking they meet only at (0,0). For small t ≠ 0 and (p,t) ∈ L, we get (ap,t) ∈ aL ∖ L, hence ap ≠ p.
  - So a ∉ Stab_{Aut(Q)}(p). By fact K4, Stab_{Aut(Q)}(p) ≅ Aut(C_p) = Aut(Q_t).
  - Hence |Aut(Q_t)| = |Stab(p)| < |Aut(Q)|, and Q_t has |Aut(Q)|/|Aut(Q_t)| ≥ 2 preimages in B.
  - So a failure of (NRT_P) requires the automorphism a of the puncture curve Q to be lost along the transported points Q_t (t ≠ 0). This is possible under the coarse reading (R2), which does not require H_t to preserve automorphism groups.

---

## III.7 Cited classical facts (Part III)

All are cited from memory; standard references are indicated.

- **K1 (Kuranishi chart).** For a stable curve C_Q and a small enough Aut(Q)-invariant ball B ⊂ Def(Q), q : B → M̄_g is the quotient by Aut(Q) onto an open neighbourhood of Q. Its fibres are Aut(Q)-orbits, and q^{-1}(Q) = {0}. (Arbarello–Cornalba–Griffiths, *Geometry of Algebraic Curves II*, Ch. XI.)
- **K2 (plumbing coordinates).** For each edge e of G_Q there is a coordinate s_e on B such that the nodes of C_p correspond to the edges with s_e(p) = 0, and the dual graph of C_p is G_{S(p)}. In particular q^{-1}(Δ_{G_Q}) ∩ B = {s_e = 0 for all e}.
- **K3 (equivariance).** For a ∈ Aut(Q) and p ∈ B there is an isomorphism C_p → C_{ap} that maps the node of e to the node of ae, and, when y is intact at p, the component labelled y to the component labelled ay. Hence s_e(p) = 0 ⟺ s_{ae}(ap) = 0 and F_{ay}(ap) ≅ F_y(p). Lemma 2.4(a) is this with y replaced by a^{-1}y.
- **K4 (isotropy).** For B small and p ∈ B, Stab_{Aut(Q)}(p) ≅ Aut(C_p).
- **PN (partial normalisation along node sections).** For S ⊂ E(G_Q) there is a holomorphic map Π_S : Z_S → ∏_{w∈V(G_S)} M̄_w (G_S := G_Q with the edges outside S contracted) such that:
  - (i) it is obtained by normalising the nodes in S of the fibres;
  - (ii) ξ̄_{G_S}∘Π_S = q on Z_S, and Π_S(Z_S^∘) ⊂ ∏M_w;
  - (iii) for p ∈ Z_S, the u-coordinate Π_S(p)[u] is the partial normalisation of C_p at the S-nodes, restricted to the part labelled by u, with the S-half-edges as marked points. If S(p) = E(G_Q), it is glued from the components labelled by the vertices of u along the non-S edges joining them. If every edge at y lies in S, then {y} is a vertex of G_S and Π_S(p)[{y}] = F_y(p) on Z_S. This is the definition of F_y, and it shows that F_y is holomorphic on L_y = Z_{S_y};
  - (iv) near p̃ ∈ Z_S^∘, Z_S is smooth, and Π_S|_{Z_S} is finite and open onto a neighbourhood of Π_S(p̃) in ∏M_w (equisingular deformations of C_{p̃} are the deformations of its pointed normalisation);
  - (v) Π_S has finite fibres on Z_S^∘, by (ii) and the finiteness of q.
- **A1 (Remmert proper mapping theorem).** The image of a closed analytic set under a proper holomorphic map is analytic; finite maps preserve dimension.
- **A2 (irreducibility, identity).**
  - An analytic subset (or subgerm) of an irreducible analytic set (or germ) X that has dimension dim X, or contains a non-empty open subset of X, equals X.
  - An irreducible germ contained in a finite union of analytic germs lies in one of them.
  - Global irreducible components are locally finite, and the germ of an analytic set at a point is the union of the germs of the global components through it.
- **A3 (open mapping).** A holomorphic function that is non-constant on an irreducible germ maps it onto a neighbourhood germ of its value.
- **A4 (images and dimension).** Under a finite map, the image of an irreducible germ is an irreducible germ of the same dimension. A holomorphic map with discrete fibres on a pure k-dimensional set has k-dimensional image (Remmert rank theorem). A finite open map between equidimensional manifolds pulls back a k-dimensional analytic germ to a k-dimensional germ.
- **A5 (local topology).**
  - An analytic germ has arbitrarily small connected representatives (conic structure theorem).
  - An irreducible curve germ has, in a small Milnor ball, an irreducible representative whose normalisation is a disc; distinct irreducible curve germs at a point meet only at the point in a small ball.
- **A6 (Krull).** If f is holomorphic on a pure k-dimensional analytic set and does not vanish identically on any local component at x, then {f = 0} has pure dimension k − 1 at x.
- **T1 (path lifting).** For a finite group acting on a Hausdorff space, every path in the orbit space lifts to a path starting at any prescribed preimage of its initial point (Bredon, *Introduction to Compact Transformation Groups*, II.6.2).
- **T2 (non-separation).** A closed subset of covering dimension ≤ n − 2 does not separate a connected n-manifold (Hurewicz–Wallman, *Dimension Theory*).

---

## III.8 Gaps of Part III

- **Marking identification (BB1-M).** Lemma 5 (Steps 1, 2 and 6) and Lemma 6.1 use BB1 in the precise form BB1-M (§1): one lifted piece E^{m+1} serves at both ends of each travel interval, with identifications under which both end-lifts land in it and the chart labels map to c_{m+1}. This is proved in Lemma L.1 of the Bridge section, which rests on Part I Lemma TI and Proposition Ψ (Part I §I.6A, proved there; formerly GAP 1).

- No other gaps. In particular:
  - (I1)–(I3) are Lemmas 2.3, 2.4 and 2.5;
  - the Φ-dichotomy is Proposition 3.1, which needs no exceptional set Z_Φ;
  - the existence of anchored sheets is the trivial germ argument of 0.7, so no separate existence lemma is needed;
  - the base is Lemma 6.1, and the endpoint is §6.

**Open (outside Theorem B):** (NRT_P) itself, and (Rig). By §6.2, under (Rig), (NRT_P) is equivalent to the problem's conclusion. A counterexample to it would need an automorphism of a puncture curve that exchanges a Φ-copy of Y_0 with a rigid Y_0-copy and is lost along Q_t.

---

# Section C — Corollaries

Throughout this section assume (R1), (R2), that Δ_Γ is of product type, and that dim M_{g_i,n_i} ≥ 1. A **puncture point** is a point Q ∈ B_0 having a branch c of B_0 with c ∖ Q contained in a stratum other than Δ_{G_Q} (Part III §0.7).

**Corollary C.1 (no moving Y_0-copies).** Assume (Rig). Suppose that for every puncture point Q ∈ B_0, no automorphism of Q maps an irreducible component C of Q with [C] = [Y_0] (with its special points) onto a different component. Then Y_t = Y_0 for all t ∈ Δ. In particular this holds in each of the following cases:
- (a) 2g_i − 2 + n_i > g − 1;
- (b) every puncture point of B_0 lies in a stratum of product type;
- (c) every puncture point Q of B_0 has Aut(Q) = {1}.

*Proof.*
- By Theorem B (Part III), it suffices to verify (NRT_P), in the setting where Y is non-constant.
- Suppose (Q, a, L, x) violates (NRT_P), so Q is a puncture point.
- Since x ∈ C_Φ(L), the germ v_x(L) passes through (Y_0, 0), so the component of Q labelled x has class [Y_0].
- a^{-1}x ≠ x, because a label cannot be both in C_Φ(L) and a rigid Y_0-copy along L (Part III §0.9).
- By Part III fact K3 (at p = 0), the automorphism a of Q maps the component labelled a^{-1}x onto the component labelled x. These are distinct components of class [Y_0], contradicting the hypothesis.

The special cases:
- (a) Two distinct components of type (g_i, n_i) would give 2(2g_i − 2 + n_i) ≤ 2g − 2 by Lemma U.4.
- (b) By Part I Lemma PT, in a product-type stratum every automorphism maps each component of positive-dimensional type to itself, and M_{g_i,n_i} has positive dimension.
- (c) is clear. ∎

**Corollary C.2 (no isotropy drop).** Assume (Rig). Suppose that for every puncture point Q ∈ B_0 there are t_n → 0 with t_n ≠ 0 and |Aut(H_{t_n}(Q))| = |Aut(Q)|. Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
- By Part III §6.2, a configuration (Q, a, L, x) violating (NRT_P) satisfies ap ≠ p for every (p,t) ∈ L with small t ≠ 0, hence |Aut(Q_t)| < |Aut(Q)| for such t.
- t(L) contains a neighbourhood of 0 (Part III Lemma 2.3(a)). So the isotropy drops for every small t ≠ 0, contrary to the hypothesis.
- Hence (NRT_P) holds, and Theorem B applies. ∎

**Corollary C.3 (shape of a counterexample).** Let a family satisfying the problem's hypotheses, read as (R1) and (R2), have Y non-constant. Then:
- (a) g ≥ 3 (Theorem U.3);
- (b) V_t is totally geodesic for at most countably many t (Theorem U.5);
- (c) the level-cover complex structures V′_t take uncountably many isomorphism classes (Theorem U.6), and closure(V_0) is not an isolated point of the Douady space (Proposition U.7);
- (d) either (Rig) fails, or there is a puncture point Q ∈ B_0 with the following properties:
  - Q lies in a non-product stratum;
  - Q has two distinct components of class [Y_0] exchanged by an automorphism, so 2g_i − 2 + n_i ≤ g − 1;
  - |Aut(H_t(Q))| < |Aut(Q)| for all small t ≠ 0;

  (Corollaries C.1, C.2 and Theorem B);
- (e) the family does not satisfy (R2^orb), nor (Loc) on any disc |t_0| < r (Theorem A and Part II Remark 7.4); equivalently (Part II Theorem 7.5), on every disc |t| < r some boundary point z ∈ B_0 has |Aut(H_t(z))| ≠ |Aut(z)| for some t. In particular some point of B_0 has a non-trivial automorphism (Corollary C.5), and indeed the closed set F of points of B_0 where the local criterion (K_z) fails is non-empty (Theorem C.7). This rests on the cited facts of Theorem A.

*Remark C.4 (the readings genuinely differ).* Part II §8.2 gives a chart-level model of a smooth, stratum-preserving trivialisation satisfying (R2) under which isotropy drops at the boundary, so that (R2^orb) fails. Whether a *global* admissible family with such an isotropy change exists is unknown. If none exists, i.e. if (AP) holds for every admissible family on some disc around 0, then the coarse problem is solved outright by Theorem 7.5 and Theorem A (no (Rig) needed).

**Corollary C.5 (trivial automorphisms on the boundary).** Assume (R1) and (R2). If Aut(z) = {1} for every z ∈ B_0 = closure(V_0) ∖ V_0, then Y_t = Y_0 for all t ∈ Δ. (This rests on Theorem A and its cited classical facts.)

*Proof.*
1. **The set Z := {w ∈ M̄_g : Aut(w) ≠ {1}} is closed.** Near any J ∈ M̄_g take the chart q : B → q(B) ≅ B/Aut(J) of (Kur). For p ∈ B, Aut(X_p) ≅ Stab_{Aut(J)}(p), so Z ∩ q(B) = q(⋃_{a ≠ 1} Fix(a)). Each Fix(a) is closed in B, there are finitely many a, and q is closed (a finite-group quotient map). So Z ∩ q(B) is closed in q(B), for every J; hence Z is closed.
2. **(AP) on a small disc.** B_0 is compact (closed in the compact M̄_g) and disjoint from Z, so it has positive distance from Z for a metric on M̄_g. H is uniformly continuous on B_0 × {|t| ≤ 1/2} and H_0 = id, so there is r > 0 with H_t(B_0) ∩ Z = ∅ for |t| < r. Then |Aut(H_t z)| = 1 = |Aut z| for z ∈ B_0 and |t| < r.
3. **Conclusion.** Part II Remark 7.6 (rescale to t ↦ V_{rt}, apply Theorem 7.5 and Theorem A, extend by Lemma 2.3). ∎

*Remark C.6.* The hypothesis of C.5 fails whenever B_0 contains a curve with an elliptic tail, or more generally a component with an automorphism fixing its special points, so C.5 is far from the general case (Theorem C.7 below removes part of this restriction, e.g. generic elliptic tails). Upper semicontinuity of |Aut| gives |Aut(H_t z)| ≤ |Aut z| for |t| small depending on z, but not the reverse inequality, and not uniformly in z; this is why the general case is open.

**A local criterion for (AP) (Theorem C.7; it contains C.5).** The rest of this section is an extension of C.5, first obtained by an independent worker and checked step by step by the author. Notation: for J ∈ M̄_g, A := Aut(J) and q : B → q(B) is the chart of (Kur) (Part II §1.4), with smoothing coordinates s_e (e ∈ E(G_J)), shrunk so that Stab_A(p) ≅ Aut(X_p) for all p ∈ B. We take B to be a coordinate ball in which the s_e are among the linear coordinates. For S ⊆ E(G_J) put L_S := {s_e = 0 for e ∈ S} and L_S^∘ := {p : S(p) = S} = L_S ∩ {s_e ≠ 0 for e ∉ S}. By (Kur), X_p has exactly |S(p)| nodes and dual graph G_J/(E(G_J) ∖ S(p)).

*Lemma C.7.0 (local stratum decomposition).* Let B″ ⊂ B be an A-invariant ball centred at 0 and G′ a stratum. Then P_{G′} := q^{-1}(Δ_{G′}) ∩ B″ is the disjoint union of the sets L_S^∘ ∩ B″ over those S with G_J/(E(G_J) ∖ S) ≅ G′, each relatively closed in P_{G′}. For an A-orbit O of such S put M_O := ⋃_{S∈O} L_S^∘ ∩ B″. Then the finitely many sets q(M_O) partition Δ_{G′} ∩ q(B″) into relatively open-and-closed subsets.

*Proof.* The decomposition is (Kur). If p_k ∈ L_S^∘ and p_k → p ∈ P_{G′}, then S(p) ⊇ S (the s_e with e ∈ S vanish at p) and |S(p)| = |E(G′)| = |S|, so S(p) = S: relative closedness. Since a·L_S^∘ = L_{aS}^∘ for a ∈ A, each M_O is A-saturated and relatively closed in P_{G′}. P_{G′} is q-saturated and q is closed (finite-group quotient), so q|_{P_{G′}} : P_{G′} → Δ_{G′} ∩ q(B″) is closed; hence each q(M_O) is relatively closed. They are pairwise disjoint (the M_O are saturated and disjoint), finitely many, and cover; so each is also relatively open. ∎

**Definition (K_z).** Let z ∈ B_0, with chart q : B → q(B) at z and A = Aut(z). **(K_z)** holds if there is an A-invariant ball B′ ⊂ B centred at 0 such that for every S ⊆ E(G_z) with q(L_S^∘ ∩ B′) ∩ B_0 ≠ ∅, the function w ↦ |Aut w| is constant on q(L_S^∘ ∩ B′).

*Equivalent form.* L_S^∘ ∩ B′ is connected (a ball in a linear subspace minus coordinate hyperplanes). For p′ near p one has Stab_A(p′) ⊆ Stab_A(p) (finite group acting linearisably), with equality when the orders agree; hence constancy of |Stab_A| on L_S^∘ ∩ B′ is equivalent to constancy of Stab_A there, i.e. to: **every g ∈ A either fixes L_S ∩ B′ pointwise or has no fixed point in L_S^∘ ∩ B′.** For S = E(G_z) (always relevant, since q(0) = z ∈ B_0) this says that A acts trivially on the germ at 0 of the stratum locus D := L_{E(G_z)}. Only the definition, not this equivalent form, is used in the proof below.

**Theorem C.7 (local criterion).** Assume (R1), (R2) and that (K_z) holds for every z ∈ B_0. Then there is r > 0 with |Aut(H_t z)| = |Aut z| for all z ∈ B_0 and |t| < r, i.e. (AP) holds on Δ_r. Consequently (Part II Remark 7.6: Theorem 7.5, Theorem A, Lemma 2.3) Y_t = Y_0 for all t ∈ Δ.

**Theorem C.8 (localisation).** Assume (R1), (R2). Let F := {z ∈ B_0 : (K_z) fails}. For every open N ⊇ F there is r > 0 with |Aut(H_t z)| = |Aut z| for all z ∈ B_0 ∖ N and |t| < r.

*Proof of C.7 and C.8 (C.7 is the case F = N = ∅).*
1. Suppose the conclusion fails. Then there are t_n → 0 and z_n ∈ B_0 ∖ N with |Aut(H_{t_n} z_n)| ≠ |Aut z_n|. Since B_0 ∖ N is compact, after passing to a subsequence z_n → z_* ∈ B_0 ∖ N, so (K_{z_*}) holds; let B, B′, A be as in its definition. There are finitely many strata, so after a further subsequence all z_n lie in one stratum Δ_{G′}.
2. Choose an A-invariant ball B″ ⊂ B′ centred at 0; q(B″) is an open neighbourhood of z_*. Put c_n(ρ) := H_{ρt_n}(z_n), ρ ∈ [0,1]. H is uniformly continuous on the compact set closure(V_0) × {|s| ≤ 1/2} and H_0 = id, so sup_ρ d(c_n(ρ), z_n) → 0; as z_n → z_*, for large n the whole path c_n lies in q(B″). By (R2) it also lies in Δ_{G′}.
3. c_n is connected, so by Lemma C.7.0 it lies in a single q(M_O), the one containing z_n = c_n(0). Write z_n = q(p_n) with p_n ∈ L_{S_n}^∘ ∩ B″. Then H_{t_n}z_n = c_n(1) = q(p′_n) for some p′_n ∈ M_O (M_O is q-saturated in B″); replacing p′_n by an A-translate (B″ is A-invariant), p′_n ∈ L_{S_n}^∘ ∩ B″. Pass to a subsequence with S_n = S constant.
4. q(L_S^∘ ∩ B′) contains z_n ∈ B_0, so (K_{z_*}) applies to S: |Aut z_n| = |Aut q(p_n)| = |Aut q(p′_n)| = |Aut H_{t_n}z_n|, contradicting the choice of (z_n, t_n). ∎

*Remarks C.9.*
- (a) C.5 is the special case in which every Aut(z), z ∈ B_0, is trivial.
- (b) **Pointwise version.** If z ∈ B_0 and Aut(z) acts trivially on the germ of D = L_{E(G_z)} at 0, then |Aut(H_t z)| = |Aut z| for all small |t|: H_t z ∈ Δ_{G_z} and H_t z → z, and near z, Δ_{G_z} ∩ q(B) = q(D ∩ B), every point of which has stabiliser A.
- (c) By Theorem C.8, every failure of (AP) close to t = 0 happens next to the closed set F. F contains every z at which Aut(z) acts non-trivially on the germ of its own stratum; in particular it contains the puncture points Q of Corollary C.3(d) (an automorphism exchanging two components of class [Y_0] swaps the corresponding moduli coordinates in D, which are non-trivial as dim M_{g_i,n_i} ≥ 1). So C.7 does not reach the configuration of C.3(d); it is consistent with it.
- (d) **Elliptic tails (example; relies on one standard fact, cited from memory: the Kuranishi family of J can be chosen Aut(J)-equivariantly, with smoothing coordinates built from Aut(J)-equivariant local coordinates at the nodes).** Suppose every z ∈ B_0 has Aut(z) generated by elliptic involutions ι_T of smooth elliptic tails T with j(T) ∉ {0, 1728} (and contains nothing else); trivial Aut(z) is allowed. The deformation space of (T, attaching point p) is H^1(T, T_T(−p)) ≅ H^1(T, T_T) ≅ H^1(T, O_T) ⊗ H^0(T, T_T) (from 0 → T_T(−p) → T_T → T_pT → 0, as H^0(T_T) → T_pT is an isomorphism), on which ι_T acts by (−1)(−1) = +1, and ι_T acts trivially on the other components; on the smoothing coordinate s_{e_T} = (product of the two branch coordinates at the node) it acts by −1 (−1 on the tangent line of T at p, +1 on the other branch), and trivially on all other s_e. For g = ∏_{T∈𝒯} ι_T: if S ⊇ {e_T : T ∈ 𝒯}, g fixes L_S pointwise; otherwise some s_{e_T} with e_T ∉ S is non-zero on L_S^∘ and is negated, so g has no fixed point in L_S^∘. Hence (K_z) holds for all z ∈ B_0, and **by Theorem C.7 the claim holds for such families.** This covers the case singled out in Remark C.6 as missed by C.5.

**Proposition C.10 (isolated boundary points: drop is all-or-nothing).** Assume (R1), (R2). Let z ∈ B_0 be isolated in B_0 ∩ Δ_{G_z}. Then t ↦ H_t(z) is holomorphic near t = 0, and there is r > 0 such that |Aut(H_t z)| is constant on 0 < |t| < r and ≤ |Aut z|.

*Proof.* {z} is open in closure(V_0) ∩ Δ_{G_z}, and by (R2) H restricts to a homeomorphism of (closure(V_0) ∩ Δ_{G_z}) × Δ onto 𝒟 := closure(𝒱) ∩ (Δ_{G_z} × Δ), a locally closed analytic set by (R1). So Γ_z := H({z} × Δ) is open in 𝒟, hence a locally closed analytic set, homeomorphic to Δ via the projection t; it is therefore 1-dimensional and locally irreducible, its normalisation ν : Γ̃ → Γ_z is a homeomorphism, and t∘ν is a bijective holomorphic map of Riemann surfaces, hence biholomorphic. So t ↦ H_t(z) is holomorphic. For each k, Z_k := {w : |Aut w| ≥ k} is a closed analytic subset of M̄_g (in a chart it is q(⋃_{C ≤ A, |C| ≥ k} Fix(C)), closed analytic by Remmert's proper mapping theorem), so {t : H_t(z) ∈ Z_k} is an analytic subset of a disc: all of it or discrete. Shrinking r, |Aut H_t z| is constant on 0 < |t| < r; upper semicontinuity of |Aut| at t = 0 gives ≤ |Aut z|. ∎

*Remark C.11 (why (AP) is not an easier intermediate statement; heuristic).* Suppose Y_0 has an automorphism α (fixing each marked point) that acts non-trivially on the germ of M_{g_i,n_i} at Y_0. Extending α by the identity gives an automorphism of every point of ∂V_0 that acts non-trivially on the stratum germ, so ∂V_0 ⊂ F. If Y_t ≠ Y_0 and Y_t does not carry an automorphism of the same order, ∂V_t loses α: a drop of isotropy along all of ∂V_0. So when Y_0 is an orbifold point of its factor, proving (AP) would essentially include the conclusion of the problem. Moreover, chart-level models (Part II §8.2; also a model with a genus-2 component attached at a Weierstrass point, whose hyperelliptic involution acts by −1 on the displacement and smoothing coordinates) show that drop along a whole boundary piece is compatible with the local plumbing structure of a totally geodesic surface near its boundary. So (AP) cannot be proved by local arguments; any proof must be global.

---

# Section R — Other routes (notes)

- **Hodge-theoretic / Arakelov-type characterisation.** One could look for a characterisation of totally geodesic surfaces that is stable under deformation, an analogue of Möller's rigidity of Teichmüller curves. None is available.
- **Infinitesimal rigidity.** H^0(N^{log}) = 0 for closure(V_0) would give the hypothesis of Proposition U.7, and more. It is unknown. First-order arguments cannot suffice in any case: a family with Y_t = Y_0 + ct² has dY(0) = 0.
- **Kobayashi / Royden arguments.** The lift of V_0 is Kobayashi-isometric, and translation lengths of monodromy elements cannot decrease under the deformation. This pins Y only if a Teichmüller disc persists.
- **Incidence / pinning.** Suppose a deeper point of closure(∂V_0), isolated in its stratum, lies on a boundary curve whose closure does not move. Then (ii) transports the incidence, and Y_t = Y_0. The existence of such a curve is not known in general.
- **Counting, level structures, arithmetic.** These give nothing beyond the above: every conserved count is equivariant and compatible with a failure, and level structures reproduce Aut(Q) at the deck level.
- **Arguments using only t = 0 data** cannot prove (NRT_P). The trivial family satisfies every hypothesis of the twin statements except "Y non-constant", and violates their conclusions at some transitions.
- **Local arguments near ∂V_0** cannot prove the claim (Remark U.8).
- **(Rig) under the coarse reading.** Partial results were obtained but are not reproduced here.
  - (Rig) cannot be derived from piece-level data alone: there are holomorphic families of maps with a fixed Teichmüller vertex whose joint image curve moves. Whether these are realisable by admissible families is unknown.
  - For a product-type piece family, (Rig) follows if, for uncountably many t, three conditions hold:
    - the Teichmüller-vertex image is the Teichmüller curve;
    - the source map is orbifold-unramified;
    - the joint map lifts over the pulled-back orbifold.
  - If the first condition holds for all t, the obstruction reduces to t = 0 being an isolated "jump time" of these conditions. Excluding a jump exactly at the totally geodesic member is open.
- **Rigidity of V_0 itself.** If smooth closed totally geodesic surfaces admit no non-trivial admissible deformation, the claim is vacuous. This is open even for the known examples (the flex and gothic loci, and covering constructions).

---

# Section G — What remains open (gaps, clearly marked)

1. **The claim as posed, under the coarse reading (R1) + (R2): NOT PROVED in general.** It is proved whenever (AP) holds on some disc around t = 0 (Theorem 7.5 + Theorem A), in particular whenever no boundary point of V_0 has a non-trivial automorphism (Corollary C.5), and more generally under the local criterion (K_z) at every boundary point (Theorem C.7; e.g. generic elliptic tails, Remark C.9(d)). In the remaining case — the trivialisation changes the automorphism order of boundary points arbitrarily close to t = 0 — it follows by Theorem B from (Rig) + (NRT_P), and given (Rig) it is equivalent to (NRT_P). Both are open in general. Corollaries C.1 and C.2 settle the cases listed there. **The single open question is therefore whether an admissible deformation of a totally geodesic surface can change the isotropy of its boundary points (and, if so, whether the constant factor can then move).** By Theorem C.8 such a change near t = 0 can only occur next to the closed set F of points where (K_z) fails; by Proposition C.10, at boundary points isolated in their stratum it occurs for all small t ≠ 0 or for none. Chart-level models show that isotropy drop (even along a whole boundary piece) is locally compatible with the plumbing structure, and when Y_0 is an orbifold point of M_{g_i,n_i} a moving Y_t is itself an isotropy drop along ∂V_0 (Remark C.11). So (AP) is not a strictly easier intermediate statement, and no local argument can settle it.
2. **Theorem A rests on the reading (R2^orb)** (equivalently (R2) + (Loc), equivalently (R2) + (AP) by Theorem 7.5). This reading is strictly stronger than (R2) and than the intrinsic orbifold reading (Part II §1.3, §8.2). Whether the problem intends it is a matter of interpretation. Whether (Loc) at t_0 = 0 alone suffices is open (Part II Remark 7.4).
3. **Formerly flagged citations, now proved here.**
   - (Ψ) is now Proposition Ψ (Part I §I.6A). Only the case actually used is proved: convergence at vertex subsurfaces of the limit (no node curve inside the subsurface), uniformly in the pants decomposition. It rests on the cited facts (Th) (Thurston) and (Prop) (properness).
   - Finiteness for marked targets (formerly GAP G1) is now Lemmas F0 and F1 (Part II §10). Lemma F1 rests on the cited closed-fibre Imayoshi–Shiga theorem (IS_c) and on (BC).
   - All classical facts are cited from memory, with the precise statements used listed in §§I.7, II.10 and III.7. Under the reading (R2^orb), Theorem A is therefore complete modulo these citations, but see item 5.
4. **Reading at orbifold points (Part I §I.8, item 5).** If V_0 meets the orbifold locus of M_g, then "tangent vector of V_0" and "total geodesy" are read on the preimage of V_0 in Kuranishi charts, at regular points of the relevant sheet.
5. **Verification status.**
   - The consolidated Parts I–III, the streamlined proof of Theorem A (Part II §§5, 6, 9), and the Bridge Lemmas L.1–L.3 have been checked only by the author of this document. A second full re-reading by the author found and repaired one faulty step (Lemma L.2, Step 4(b), now a Remmert argument); a third pass found the fixed-pants-decomposition flaw in the uses of (Ψ) (see §0) and repaired it. This is still not an independent referee.
   - Proposition Ψ (§I.6A) and Lemma F1 (§II.10) were produced by separate workers, checked by the author (the hexagon inequalities of Lemma S also numerically), and then by an independent referee (next item). In an earlier revision the author found that Lemma F1, Steps 2c–2d, tacitly used the Birman–Hilden property (that "lifts of mapping classes" form a group mapping onto PMod with kernel the deck group); this is now avoided by working with pairs (ϑ, lift).
   - Theorem 7.5 ((R2) + (AP) ⇔ (R2^orb)), Corollary C.5, Lemmas F0/F1, Proposition Ψ with Lemma S, and all of Part II §§2–7, §9, §10 have now been checked by independent referees: correct after minor repairs, all incorporated (see §0). Theorems C.7, C.8 and Proposition C.10 were proved by a separate worker and checked only by the author; Remark C.9(d) also rests on a cited equivariance fact for Kuranishi families. The referees flagged one citation scope to double-check: (Th) for cusped finite-area surfaces (used only in Lemma 4.3, hence only for Theorem 4.4(b) and the endpoint step §9.3, see Remark 4.6 of Part II; and in Proposition Ψ(c)).
   - The component arguments of Parts I and III, and Theorems LG and RO of Part II, were checked earlier by independent readers.


=== END OF DRAFT PROOF ===
