# round11_q8 — attempt on MS11

**Status line.** MS11 is NOT proved and I give no counterexample. What this file contains:
- §1 (proved, local): a flaw in the chain's bookkeeping. Lemma B1(a) and B1(b) of round10_q3 (entry 100) are false as stated. Chain step 2(d) (the endpoint) uses B1(a), so as worded it does not follow from MS11. The repair costs nothing: read "transport sheet of c̃" as "irreducible component of closure(Ñ_c̃) that contains c̃ × {0}" everywhere, in MS11's hypothesis and conclusion and in the chain. With that repair the chain is checked again in §2.
- §3: a check of the planner's Mechanism D. Steps 1–4 are sound, with precise citations, and I prove a sheet-wise identity (Lemma 3.3). The remaining obstruction is located exactly: the label twists along (β)- and (γ)-edges.
- §4: proved / not proved / open.

Readings: (R1), (R2) with H_0 = id, as in the task file. (Rig) is assumed wherever "generic t" is used.

---

## 1. Lemma B1(a),(b) are false as stated (local model), and the repair

### 1.1 What B1 claims
round10_q3 Lemma B1 says that for a lifted branch b̃ with transport family Ñ = Ñ_b̃:
- (a) every irreducible component Ñ^1 of Ñ has Ñ^1 ∩ {t = 0} a non-empty open subset of b̃ ∖ 0;
- (b) the pointwise stabiliser Stab(b̃) permutes the components of Ñ transitively.

The proof of (a) uses "Ñ ∩ {t = 0} = b̃ ∖ 0". That equality is never proved. It is the same claim as R7-3 Lemma 2 ("Ñ ∩ {t=0} = β̃ ∖ {0}") and round9_q1 (Fam) ("the t = 0 slice of aÑ is ab̃ ∖ 0"). It fails when a connected component of q^{-1}(N) runs, through times t ≠ 0, from one lift b̃ to another lift hb̃ of the same coarse branch, with h ∉ Stab(b̃).

### 1.2 Local model (proved; local only)
Work in Def(Q). Use coordinates s_1, s_2 (smoothing parameters of two edges), z (a deformation coordinate of the stratum locus), plus further coordinates set to 0 throughout. Let h ∈ Aut(Q) act by z ↦ −z and fix s_1, s_2. Assume that near the relevant points the stabilisers are ⟨h⟩ or trivial. Then the coarse coordinates are (s_1, s_2, w) with w = z².
- t = 0: b̃ := {s_1 = 0, z = s_2}. Then hb̃ = {s_1 = 0, z = −s_2} ≠ b̃, and Stab(b̃) is trivial in ⟨h⟩. The coarse branch b = q(b̃) = {s_1 = 0, w = s_2²} is smooth. s_2 ≢ 0 on b̃, so Q is a puncture of the piece of b, as in (P).
- Transport: H_t(Q) := q(0, 0, t), and H_t of the point of b with parameter s_2 is (s_1, s_2, w) = (0, s_2, (s_2 + t)²). Then N := H((b ∖ Q) × Δ_ε) = {s_1 = 0, w = (s_2 + t)², s_2 ≠ 0} is a smooth graph over (s_2, t). H is a stratum-preserving homeomorphism, smooth off Q, and H_0 = id.
- Preimage: q^{-1}(N) = (T_1 ∪ T_2) ∩ {s_2 ≠ 0}, with T_1 := {s_1 = 0, z = s_2 + t} and T_2 := hT_1 = {s_1 = 0, z = −s_2 − t}.
- T_1 ∩ T_2 = {s_1 = z = 0, s_2 = −t}. For t ≠ 0 this lies over b_t ∖ Q_t. It is the point of b_t whose curve has the extra automorphism h; this is allowed under the coarse reading (R2).

So the connected component Ñ_b̃ of q^{-1}(N) ∩ (B × Δ_ε) containing b̃ ∖ 0 is all of (T_1 ∪ T_2) ∩ {s_2 ≠ 0}. Its t = 0 slice is (b̃ ∪ hb̃) ∖ 0. Its closure has the two components T_1 and T_2, and T_2 ∩ {t = 0} = hb̃, which is disjoint from b̃ ∖ 0. **So B1(a) fails for the component T_2.** Also Stab(b̃) = 1 while there are two components, **so B1(b) fails.**

This is a model of the transport of a single boundary branch. Like the run's other local models, it is not claimed to be realisable by an actual totally geodesic V_0. But the point is logical: B1(a) was derived from an unproved equality, and nothing in (R1), (R2), (i), (ii) forces that equality.

### 1.3 Why it matters for the chain
Chain step 2(d) (non-product endpoint) argues as follows. MS11 gives a transport sheet T of b̃ on which x is persistent. By B1(a), T_0 is open in b̃, so x is intact along b̃ with F_x ≡ Y_0, which contradicts MERGE/MOV.

In the model, T = T_2 is a transport sheet of b̃ in MS11's sense. Persistence of x on T_2 gives, at t = 0, x intact with F_x ≡ Y_0 along hb̃. By (K3) that is persistence of h^{-1}x along b̃, and it does not contradict x merging along b̃. **So, as worded, MS11 does not imply the endpoint contradiction.** The junction step has the same problem: the transfer step 3 of round10_q3 §2.2 needs the persistent sheet's t = 0 slice to lie on the track's lift β̃′_m, so that it maps into the lifted family component of the track's lifted curve.

### 1.4 Repair (proved)
**Definition.** A *based transport sheet* of c̃ is an irreducible component T of closure(Ñ_c̃) with c̃ × {0} ⊂ T.

**Lemma 1.4.**
- (a′) Every component of closure(Ñ_c̃) is of the form a·T, with T a based transport sheet of c̃ and a ∈ Aut(Q).
- (b′) Stab(c̃) permutes the based transport sheets of c̃ transitively.
- (c′) If x is Y-persistent on a based sheet T of b̃, then x is intact along b̃ with F_x ≡ Y_0.

*Proof.*
- (a′) Let T′ be a component, and N the coarse transported set. N is a topological 4-manifold, so q(T′) = closure(N) near (Q,0), by Remmert and irreducibility as in B1(a). Hence T′ meets {t = 0} over b ∖ Q, i.e. in ∪_a a c̃. By Krull the slice T′_0 is pure 1-dimensional, so it contains an open piece of some a c̃, and then all of a c̃ (identity theorem on the irreducible germ). Then a^{-1}T′ is a component of q^{-1}(closure N) containing c̃ × {0}. It lies in closure(Ñ_c̃), because near a generic point (p̃, 0) of c̃ it meets Ñ_c̃ in an open set.
- (b′) This is the proof of B1(b) restricted to germ components at (p̃, 0), p̃ ∈ c̃ generic, where it is correct: near (p̃, 0), q is the quotient by Stab(p̃) = Stab(c̃). Each based sheet contains such a germ component, and germ components at (p̃, 0) determine global components.
- (c′) The t = 0 slice of T contains b̃. Persistence is a closed condition, so it holds at t = 0 along b̃. ∎

**Repaired MS11 (MS11♭).** In MS11, read "transport sheet" as "based transport sheet" in both the hypothesis and the conclusion.

---

## 2. The chain with MS11♭ (checked)

I re-check only the places where sheets enter.
- **Base** (Δ_Γ of product type). Persistence of vertex i holds on every sheet of every lift of a branch of D^1, so in particular on based sheets.
- **Product-type junctions** (Lemma J / Cor. J′, component-wise as in round10_q3 §2.2 item 2). Their conclusion is persistence on a germ component 𝒲̃″ ⊃ b̃ at (p̃, 0). The global component containing it contains b̃ × {0}, so it is based.
- **Transfer along D^{m+1}** (round10_q3 §2.2 item 3). It needs the persistent sheet at J_m to be based at β̃′_m, so that its Π_S-image lies in the lifted family component 𝒲̃ of the track's lifted curve E. That is exactly what MS11♭ (or the product-type step) supplies. It then produces a germ component at a generic point of β̃_{m+1}, i.e. a based sheet of β̃_{m+1}. This is what MS11♭'s hypothesis at J_{m+1} requires.
- **Interior transitions** (Cor. IMOV_all). Here β̃′_m = β̃_m as sets, so the based sheets coincide.
- **Endpoint, non-product case.** MS11♭ and Lemma 1.4(c′) give the contradiction directly; B1(a) is no longer needed.
- **Endpoint, product case.** Unchanged.

With "transport sheet" replaced by "based transport sheet" everywhere, I found no further flaw in the chain steps I checked. I did not re-derive Proposition K_w, Lemma PA, or the cited Teichmüller facts.

Note: B1(d) (product type) survives. Its proof uses only that every α ∈ Aut(Q) fixes x (Lemma PT), and then persistence on T is equivalent to persistence on aT for every a.

---

## 3. Mechanism D (planner's sketch): what is sound and where it stops

Setting of MS11♭; Y is non-constant. 𝒥 denotes the set of lift-curves, i.e. the irreducible components of {(p,t) : q(p) = Q_t}; it is Aut(Q)-stable. For a sheet Z and a lift-curve L ⊂ Z write P(Z) := {labels Y-persistent on Z} and Copies(L) := {y : F_y ≅ Y_t along L}.

### 3.1 Steps 1–3 (sound)
- **Step 1.** Let X be a 3-dimensional irreducible component of the germ of q^{-1}(closure 𝒱) at (0,0) with S × {0} ⊂ X. It exists: S × {0} lies in q^{-1}(closure 𝒱), whose germ has pure dimension 3. Put D := X ∩ {N = 0}, N = ∏ s_e.
- **Step 2.** N ≢ 0 on X, so by Krull D has pure dimension 2 at (0,0). Every component Z of D satisfies dim(Z ∩ {t = 0}) = 1, again by Krull, since D ∩ {t = 0} ⊂ X_0 ∩ {N = 0} is a curve. By the argument of Lemma 1.4(a′), Z is a component of q^{-1}(closure N_c) for some branch c of B_0 at Q, and it is based at some lift of c. Moreover D_0 ⊃ β̃, b̃, so D contains a based sheet of β̃ and a based sheet of b̃.
- **Step 3.** Cited from memory: Grothendieck's connectedness theorem (SGA 2 XIII 2.1; Brodmann–Sharp, Local Cohomology, 19.2). For a complete local noetherian ring A and f ∈ m, c(A/fA) ≥ min{c(A), sdim A − 1} − 1, where c is the connectedness dimension. Here A is the completion of the analytic local ring of X. It is a domain, because an excellent Henselian local domain has a domain completion; this needs the germ X to be irreducible, which it is. So c(A) = sdim A = 3 and c(A/N) ≥ 1. Hence the components of the germ D form a graph that is connected when two components are joined if they meet in a curve. Passing from formal to analytic components only merges vertices.

### 3.2 Step 4: classification of edges (sound)
Let Z_a ≠ Z_b be components of D sharing a curve germ C through (0,0). Then exactly one of the following holds.
- (α) C ∈ 𝒥 is a lift-curve.
- (β) C = c̃ × {0} for a lifted branch c̃. Then Z_b = σ Z_a with σ ∈ Stab(c̃). This is Lemma 1.4(b′), applied to the two based sheets of c̃.
- (γ) C ⊄ {t = 0} and C ∉ 𝒥. Then for generic t the slices of Z_a, Z_b are distinct lifted branches through a point p with q(p) ∈ H_t(c) ∖ Q_t. Two different slices cannot share a curve germ for all t: that would force Z_a = Z_b. In a small ball, H_t(c) ∖ Q_t is a topological 1-manifold, because H_t is a homeomorphism and B_0 ∖ Q is smooth there. So both slices lift the same unibranch coarse germ at q(p). Hence they differ by some g ∈ Stab(p), and C ⊂ Fix(g). By identity on the open set where the slices agree, Z_b = gZ_a.

The model of §1.2 shows (γ) occurring, with T_1 ∩ T_2 = C ⊂ Fix(h).

### 3.3 Lemma (persistence = copies on boundary-type sheets; proved, essentially round9_q2 Prop. 4(ii))
Let Z be a component of D whose branch c has Q as a puncture of its piece (boundary type). Then:
- (i) Z contains a lift-curve;
- (ii) P(Z) = Copies(L) for every lift-curve L ⊂ Z.

*Proof.*
- (i) q(Z) is a 2-dimensional irreducible analytic set inside closure(N_c), which is topologically a disc times a disc. So q(Z) = closure(N_c) near (Q,0), and in particular it contains (Q_t, t). The set Z ∩ q^{-1}{(Q_t,t)} is a curve finite over Δ, so it contains a lift-curve.
- (ii) "⊂" is trivial. For "⊃", take y ∈ Copies(L) and a generic t (R8-3 Theorem N / R8-2 Theorem 1, under (Rig) and Y non-constant). The slice Z_t near L(t) is a non-empty union of lifted branches of H_t(c) at L(t), by Krull. Q_t is a puncture of their piece, since H_t preserves strata. So Theorem N excludes MERGE and puncture-MOV of y, and y is intact and ≡ Y_t on the germ of Z_t at L(t). The set A_y := {(p,t) ∈ Z : y intact at p, F_y(p) ≅ Y_t} is analytic. For uncountably many t it contains a curve germ of the slice, so it is not contained in a proper (≤ 1-dimensional) analytic subset of Z. Hence A_y = Z. ∎

**Corollary 3.4 (reformulation of MS11♭).** MS11♭ holds iff some based sheet T of b̃ contains a lift-curve L′ with x ∈ Copies(L′). If x ∈ Copies(L_β) for a lift-curve L_β, then Copies(aL_β) = a·Copies(L_β) by (K3). So the condition reads: T ⊃ aL_β for some a with a^{-1}x ∈ Copies(L_β).

### 3.4 Where Mechanism D stops
Run along a path in the graph of §3.1–3.2. P is unchanged across (α)-edges between boundary-type sheets, by Lemma 3.3(ii). Across a (β)-edge P is multiplied by some σ ∈ Stab(c̃), and across a (γ)-edge by some g ∈ Stab(p). There are two further leaks:
- **At the start.** The based sheet Z′ of β̃ inside D need not be the sheet T_β on which x is persistent. Lemma 1.4(b′) only gives Z′ = σ_0 T_β with σ_0 ∈ Stab(β̃), so P(Z′) ∋ σ_0 x. σ_0 fixes β̃ pointwise, but it may swap Y_0-copies at its generic points.
- **Interior-type sheets.** If X_0 ⊋ S contains a sheet whose boundary is a lifted branch in {all s_e = 0}, an (α)-edge into it does not transport P: at such sheets only P(Z) ⊂ Copies(L) holds, because IMOV is possible there.

So the path gives x ∈ g·P(T) for a composite twist g. MS11♭ follows only if some path has g ∈ Stab(x)·(something fixing persistence on T), for example if every σ and g met fixes x. That is the old twin condition ((NT), (U_J), (SC)) in a new form. The model of §1.2, with the extra feature that h swaps two Y_0-copies x, hx at Q, is locally consistent with every listed constraint: the copies separate as Y_t and φ(t) on T_1 and T_2. So Mechanism D alone cannot conclude, and the global input (total geodesy at (β)-edges, as in the planner's item 5) is still needed. I could not supply it.

---

## 4. Summary

**Proved.**
1. Lemma B1(a),(b) of round10_q3 are false as stated (§1.2, explicit local model consistent with (R1), (R2)). The unproved equality "Ñ_b̃ ∩ {t=0} = b̃ ∖ 0" (R7-3 Lemma 2, round9_q1 (Fam), B1) fails when a fixed-point curve of h ∉ Stab(b̃) meets the transported branch at t ≠ 0.
2. Consequently, chain step 2(d), and the transfer step after a non-product junction, do not follow from MS11 as worded. The repair: read MS11 and the chain with **based** transport sheets (Lemma 1.4). With that reading I re-checked the chain's sheet bookkeeping (§2) and found no further flaw.
3. Mechanism D, steps 1–4 (§3.1–3.2), with the connectedness theorem cited precisely, and Lemma 3.3 / Corollary 3.4 (a reformulation of MS11♭ via lift-curves).

**Not proved.** MS11, and MS11♭.

**Open.**
- MS11♭: show that some based sheet of b̃ contains a lift-curve carrying x as a Y_t-copy. Equivalently, show that the composite twist along some path of Mechanism D's graph fixes x. This includes the start twist σ_0 ∈ Stab(β̃) and the (β)/(γ) twists.
- Whether the model of §1.2 (a same-coarse-branch crossing through an h-fixed point at t ≠ 0) can occur for a smooth totally geodesic V_0.
- (Rig) (entry 82), which is unchanged.
- No counterexample is claimed.

=== END OF ANSWER round11_q8 ===

