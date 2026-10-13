# round14_q5 — attempt on (SPLIT) (case (A) of (NRT_P)), and case (B)

**Plan/status line.** NOT PROVED. Neither (SPLIT) nor case (B) is proved, and no global counterexample is given. This file establishes three things.
1. Case (A) is not one configuration. It splits by how a acts on the pattern of c̃ and on the t = 0 lifted piece E. The planner's "split lifted family / leaving the symmetric locus" picture is valid in exactly one sub-case, (A1).
2. In (A1) I prove a reduction (Prop. 2): the swap σ can be replaced by an automorphism k that fixes E pointwise. That k is realised by an automorphism of the generic curve of the piece c_0, and c_t leaves Fix(k). So (A1) is the generic-symmetry / reflection situation already studied in round13_q4 and round13_q6.
3. In the other sub-cases, (A2) and (A3), the "fact" W ≠ σW carries no information. In (A3) it depends on a choice of identification, and with a suitable choice σ = id. So no "split" or symmetric-locus argument can work there. Case (B) contains configurations of the same kind.

Readings: (R1), (R2) with H_0 = id (coarse reading); (Rig) is used only through Lemma U / U3 as quoted in the brief. Notation is as in the brief: G_c is the dual graph of the generic curve of the piece of c, ξ = ξ_{G_c} : ∏_{w∈V(G_c)} M_w → Δ_{G_c} is the quotient map, 𝒲 := ξ^{-1}(closure 𝒱 ∩ (Δ_{G_c} × Δ)) is the lifted family, and W is the component of 𝒲 containing Π(T).

---

## 0. Conventions: what "σ induced by a" means

Let E_c ⊂ E(G_Q) be the set of edges with s_e ≡ 0 on c̃ (the pattern of c̃). The partial normalisation Π along c̃ uses an identification ι_c̃ : G_Q/(E(G_Q) ∖ E_c) ≅ G_c, i.e. the contraction of the smoothed edges. For ac̃, the pattern is aE_c.

- **(Pattern-preserving, aE_c = E_c.)** Points with pattern E_c use one identification ι for all such points. So Π(a p) = σ(Π(p)), where σ := the automorphism of G_c induced by a (through ι). Then Π(aT) ⊂ σW, and σ(v) = ι(a·y) = ι(x) = u. This is the setting in which the brief's fact "σW = W with σ(v) = u is impossible" is meaningful.
- **(Pattern-moving, aE_c ≠ E_c.)** The identification ι_{ac̃} for the pattern aE_c is a separate choice. With ι_{ac̃} := ι_c̃ ∘ ā^{-1} (ā the isomorphism of contracted graphs induced by a), equivariance (K3) gives Π(aT) = Π(T) ⊂ W, with label ax ↔ u and label x = ay ↔ v on aT. Any other choice changes the "σ" by an arbitrary element of Aut(G_c). **So in the pattern-moving case the statement "the lifted family of aT is σW ≠ W" is an artefact of the identification.** With the choice above, σ = id and there is no split.

Case (A) therefore divides into:
- **(A1)** aE_c = E_c and σE = E, where E is the irreducible component of ξ^{-1}(c_0) containing Π(c̃). This holds for instance when a ∈ Stab(c̃) (then Π(ac̃) = Π(c̃) ⊂ E ∩ σE, and two components of the curve ξ^{-1}(c_0) sharing a curve germ coincide).
- **(A2)** aE_c = E_c and σE ≠ E.
- **(A3)** aE_c ≠ E_c.

All three can occur at chart level. In (A3), x and y are both intact along c̃, and c̃ smooths edges that a does not preserve. Example: G_Q has a vertex z carrying x, y and two subgraphs A_x, A_y, with a swapping x ↔ y and A_x ↔ A_y. c̃ smooths edges inside A_x, and ac̃ smooths edges inside A_y.

---

## 1. Lemma 1 (local irreducibility of the coarse piece family at generic points) — proved

Let 𝒞 := closure 𝒱 ∩ (Δ_{G_c} × Δ). Let P ∈ c_0 := closure V_0 ∩ Δ_{G_c} be a point at which the curve c_0 is locally irreducible. Then the germ (𝒞, (P,0)) is irreducible and of pure dimension 2.

*Proof.*
- By (R2), H restricts to a homeomorphism (closure V_0 ∩ Δ_{G_c}) × Δ → 𝒞 over Δ, with H(P,0) = (P,0). So it maps a neighbourhood U × Δ_ε of (P,0) in c_0 × Δ onto a neighbourhood of (P,0) in 𝒞.
- A locally irreducible curve germ is homeomorphic to a disc (Puiseux parametrisation; normalisation is a homeomorphism). So (𝒞,(P,0)) is homeomorphic to a germ of R^4. Hence every analytic component through (P,0) has real dimension 4, i.e. complex dimension 2.
- Suppose 𝒞 = A_1 ∪ A_2 near (P,0), with neither containing the other. Then A_1 ∩ A_2 has complex dimension ≤ 1, so covering dimension ≤ 2. Let B be a small connected neighbourhood homeomorphic to a 4-ball. Then B ∖ (A_1∩A_2) is the disjoint union of the non-empty relatively open sets B ∩ (A_1∖A_2) and B ∩ (A_2∖A_1). (Each is relatively open, since its complement in B ∖ (A_1∩A_2) is the other one, which is closed there. Each is non-empty, since neither germ contains the other.)
- But a closed subset of covering dimension ≤ n−2 does not separate a connected open subset of an n-manifold (Hurewicz–Wallman, cited from memory). This is a contradiction. ∎

## 2. Lemma 2 (orbit lemma) — proved

Let a finite group K act on a complex analytic space Y, let π : Y → Y/K be the quotient, and let Z ⊂ Y/K be a closed analytic set (or germ) that is irreducible. Then the irreducible components of π^{-1}(Z) form a single K-orbit.

*Proof.*
- π is finite and surjective, so for each component Z_1 of π^{-1}(Z), π(Z_1) is closed analytic. Since π^{-1}(Z) = ∪_j Z_j and Z is irreducible, Z = π(Z_j) for some j. Call that component Z_1.
- Let y ∈ π^{-1}(Z). Then π(y) = π(y′) for some y′ ∈ Z_1, so y = k y′ ∈ kZ_1 for some k ∈ K. Hence π^{-1}(Z) = ∪_{k∈K} kZ_1. Each kZ_1 is irreducible, so every component is one of the kZ_1. ∎

Germ version: near e ∈ Y, π is the quotient by Stab_K(e) (standard for finite group actions, cited from memory). So the germ components of π^{-1}(Z) at e form one Stab(e)-orbit, when (Z, π(e)) is an irreducible germ.

## 3. Proposition 3 (reduction of (A1) to a pointwise stabiliser) — proved

Assume a (SPLIT) configuration of type (A1). Let e ∈ E be generic: e lies over a point P of c_0 at which c_0 is locally irreducible, and e lies outside Fix(g) for every g ∈ Aut(G_c) with E ⊄ Fix(g). Then:
1. there is k ∈ Aut(G_c) fixing E pointwise with σW = kW;
2. put u′ := k^{-1}(u). Then Γ_{W,u′} = {Y_0} × Δ, Γ_{W,u} is non-constant, k(u′) = u, and k ∉ Stab(W);
3. k is realised by an automorphism of every curve of the piece c_0. That curve has two components of type (g_i,n_i), at u′ and u, exchanged by this automorphism, both ≅ Y_0. For t ≠ 0 small, the curves of W_t (whose vertices u′, u carry Y_0 and φ(t) ≠ Y_0, φ the branch of Γ_{W,u}) do not lie in Fix(k). So c_t leaves the k-symmetric locus ξ(Fix(k)) ⊂ Δ_{G_c}, and c_0 lies in it.

*Proof.*
- **Both W and σW pass through e.** Π(T) ⊂ W and c̃ × {0} ⊂ T, so W_0 ⊃ Π(c̃). W_0 is a curve inside ξ^{-1}(closure c_0), so it contains the component E ⊃ Π(c̃). Hence e ∈ W. Likewise (σW)_0 ⊃ σE = E, so e ∈ σW.
- **Germ components.** By Lemma 1, (𝒞,(P,0)) is irreducible. ξ is the quotient by Aut(G_c) (coarse stratum Δ_{G_c} = ∏M_w / Aut(G_c), cited from memory as standard). By the germ version of Lemma 2, the germ components of 𝒲 = ξ^{-1}(𝒞) at (e,0) form one orbit of Stab(e) = Stab_pt(E). Here Stab(e) = Stab_pt(E) by the choice of e.
- **Comparing W and σW.** W and σW are irreducible components of 𝒲, of pure dimension 2, so their germs at (e,0) are unions of germ components of 𝒲. Pick a germ component Z_1 of W at (e,0) and a germ component Z_2 of σW there. Then Z_2 = k Z_1 for some k ∈ Stab(e). So σW and kW are irreducible components of 𝒲 (kW is one, since k permutes 𝒲) sharing the 2-dimensional germ Z_2. Hence σW = kW. This proves item 1.
- **Item 2.** τ := k^{-1}σ satisfies τW = W. For any vertex w, Γ_{τW,τw} = Γ_{W,w}, so Γ_{W,τ(v)} = Γ_{W,v} = {Y_0} × Δ. Also τ(v) = k^{-1}(σ(v)) = k^{-1}(u) = u′. If k ∈ Stab(W), the same identity would give Γ_{W,u} = Γ_{W,k u′} = Γ_{W,u′}, i.e. the non-constant curve equal to the constant one, which is impossible.
- **Item 3.** k fixes e = (e_w)_w. This means that for each vertex w there is an isomorphism e_w ≅ e_{k(w)} of pointed curves compatible with the action of k on half-edges. These isomorphisms glue to an automorphism of the stable curve ξ(e) inducing k on the dual graph (standard description of automorphisms of a stable curve, cited from memory). For t ≠ 0 small, points of W_t near (e,0) have coordinates Y_0 at u′ and φ(t) at u. φ is non-constant with φ(0) = Y_0, so φ(t) ≠ Y_0 for small t ≠ 0. So these points are not fixed by k, and neither are their kW-translates. ∎

**What (A1) has become.** At every generic point P of c_0, Aut(P) contains an element h_k realising k, and h_k exchanges two Y_0-components u′, u. On the lifted family W, near P, one of them keeps the value Y_0 and the other moves along φ. This is exactly the "reflection / generic-symmetry" situation of round13_q4 §1–2 and round13_q6 §2, transported from Q to a generic point P of c. The lifted sheet at P plays the role of S, and h_k the role of the reflection.
- If h_k stabilises the lifted sheet S_P of V_0 at P and acts non-trivially on it, then under (H2)/(Sm) round13_q4 Lemma R / round13_q6 Prop. D apply. Either an anchored sheet at P is pointwise h_k-fixed (case I / R-ii), or V_t contains a curve of smooth h_k-symmetric curves converging to c (case II / R-i).
- Case I is impossible here. On a pointwise-fixed sheet, F_u ≅ F_{u′} by Lemma E(3), i.e. φ(t) ≅ Y_0 up to ordering, which puts φ in a finite set. So only the detaching-mirror case II remains: the global 2-dimensional family 𝒟 of Prop. G / Prop. Z, with 𝒟_0 ⊃ c̄. Excluding it is the still-open (NRT-Z).
- I did not check whether h_k stabilises S_P. If it does not, the round13 lemmas do not apply.

So (A1) is reduced to (NRT-Z) of round13_q4, plus the sheet-stabiliser question. It is not solved.

## 4. (A2), (A3) and case (B): no split, no symmetric locus (observations, proved where stated)

**Observation 4.1 (proved, by §0).** In (A3), with the identification ι_{ac̃} = ι_c̃ ∘ ā^{-1}, Π(aT) ⊂ W, and on aT the label x corresponds to v. So the configuration is a single global component W of the lifted family approached from Q along two lifted branches c̃ ≠ ac̃, with the twin labels x, y exchanging roles between them. "W ≠ σW" carries no information here.

**Observation 4.2.** In (A2) and (A3), the generic curve of c_0 need not have any automorphism exchanging the vertices u, v. In the §0 example (A_x and A_y attached to z at points with no symmetry of the generic z), it has none.
- Then the coarse family 𝒞 near generic points of c is as in Lemma 1 and the lifting is locally unramified: nothing distinguishes t = 0 from t ≠ 0 there.
- The only symmetry in the configuration is Aut(Q) at the single point Q. It is lost at Q_t, which carries the two type-(g_i,n_i) components φ(t) and Y_0, twins under Aut(Q).
- **So the planner's guess cannot work in (A2)/(A3).** Neither Lemma Z / Lemma TG (symmetric loci in V_0) nor Lemma R (forced symmetric curves) has an input: there is no symmetric locus containing c_0 for c_t to leave, and no symmetric interior curve needs to exist near generic points of c_t. (Lemma R at Q itself needs a to fix c̃ pointwise, which fails in (A3).)

**Observation 4.3 (case (B)).** If the twin y is not intact along c̃ (it lies inside a nodal coordinate of the cusp point κ ∈ F_W), then a cannot preserve the pattern. The reason: some edge at y is smoothed along c̃, while every edge at x is unsmoothed along c̃ (x is a constant vertex). Since a^{-1}x = y, we have a(y) = x, so a sends that smoothed edge at y to an edge at x, which is unsmoothed. Hence aE_c ≠ E_c. So this part of (B) is of pattern-moving type, and Observation 4.2 applies.
- The coarse data are then: a piece family K_W × {c_t} with a t-independent moving curve K_W, one cusp of which contains a component ≅ Y_0, and a constant vertex with value φ(t), φ(0) = Y_0.
- At t = 0 the coincidence φ(0) = Y_0 produces the extra automorphism a of Q, and at t ≠ 0 it is gone. Nothing in the boundary data (pieces, values, F_W, Φ) excludes this. Excluding it requires information about how the interior of V_t approaches Q_t, i.e. a genuinely global argument; Lemma NG (round13_q7) already shows t = 0 data alone cannot do it.
- If instead y is intact along c̃, it is a moving vertex whose value at the cusp is the smooth curve Y_0. Then the pattern may be preserved, and the analysis of §3 applies verbatim with σ(u) a moving vertex of σW, so W ≠ σW automatically and no symmetric locus arises either.

## 5. Summary

**Proved.**
- Lemma 1: the coarse piece family 𝒞 is locally irreducible of pure dimension 2 at (P,0) whenever c_0 is locally irreducible at P. This is a topological consequence of (R2).
- Lemma 2: the orbit lemma for finite quotients, including the germ version.
- §0: "σ induced by a" is canonical only when a preserves the pattern of c̃. In the pattern-moving case one may take σ = id, so "W ≠ σW" carries no information.
- Prop. 3: in sub-case (A1) (pattern preserved, σE = E, e.g. a ∈ Stab(c̃)), σ can be replaced by k ∈ Stab_pt(E). k is realised by an automorphism of every curve of c_0 exchanging two Y_0-components, of which one stays rigid and one moves along φ ∈ Φ for t ≠ 0. So c_t leaves the k-symmetric locus that contains c_0. Combined with round13_q6 Lemma E(3), the pointwise-fixed-sheet alternative is excluded, leaving only the detaching-mirror alternative (NRT-Z), provided h_k stabilises the lifted sheet at P and (Sm)/(H2) holds.

**Not proved.**
- (SPLIT) in any sub-case.
- (A1) is reduced to (NRT-Z) plus the open question whether h_k stabilises the lifted sheet of V_0 at generic P.
- (A2), (A3): the planner's mechanism has no input there (Obs. 4.2), and no replacement mechanism is found.
- Case (B): not proved. Its pattern-moving part is of the same kind as (A3) (Obs. 4.3).

**Open questions (explicit).**
1. (NRT-Z) for the generic symmetry k of Prop. 3 (A1): exclude a global 2-dimensional family of smooth k-symmetric curves in closure 𝒱 degenerating onto c̄ at t = 0.
2. (A2)/(A3)/(B): find a global input that forbids a puncture point Q whose t-deformation Q_t carries twin components (twins under Aut(Q)) of type (g_i,n_i) with values φ(t) (non-constant, in Φ) and ≡ Y_0, when no symmetric locus is involved at generic points of c. Any such argument must use the interior of V_t near Q_t, i.e. how V_t near Q_t relates to total geodesy at t = 0, and not just the boundary piece data, which are consistent with this configuration.
3. Whether h_k stabilises the lifted sheet S_P in (A1).

**Verdict: not proved** (partial: the decomposition of case (A) into (A1)/(A2)/(A3), the reduction of (A1) to the generic-reflection case and (NRT-Z), and the observation that the planner's mechanism does not apply to (A2), (A3) or the pattern-moving part of (B)).

=== END OF ANSWER round14_q5 ===
