# round14_q3 — attempt on (NRT_P)

**Plan/status line.** (NRT_P) is **not proved and not refuted** here. This file contains:
- §1: a check of the derivation "(NRT_P) ⇒ MS8 ⇒ claim" (round13_q5). I found no flaw at the level of the stated lemmas, and I record two minor points.
- §2, **Proposition M (new, proved as a chart-level statement):** an explicit chart model of a rigid twin of the *sheet-moving* type. In it, h fixes c̃ pointwise but hS ≠ S. The model satisfies (R1), (R2), the stratum condition, the shape required by Lemma U, and in addition it preserves the isotropy of **interior** points. So it has **no** detaching mirror and no family 𝒵 of symmetric curves. Consequence: Lemma R, Prop. D, Prop. G and (NRT-Z) of round13_q4/q6 cannot cover this case. The model is a local realisation of the planner's case (A), the "split lifted family" W ≠ hW.
- §3, **Lemma 3.1 (proved):** in Prop. M, the naive extension to a puncture point Q, with an outgoing branch d̃ ⊂ S along which x moves, *violates (Rig)*. This isolates what any genuine failure must look like: the Φ-sheet and the sheet of the outgoing branch must lie in **different 3-fold components** of the chart. The cause is the MOV mechanism, which works inside a single 3-fold.
- §4, **Proposition 4.2 (sketch, under an extra reading (R2^int)):** suppose H preserves the isotropy of interior points (the orbifold reading, but on the interior only). Then every chart 3-fold component X_S contains exactly one lift-curve. So inside one X_S, C_Φ is the same for all boundary-type anchored sheets. An (NRT_P) failure would then need a lifted branch lying in two distinct chart sheets S ≠ gS, with twin anchored sheets in X_S and X_{gS}.
- §5: open questions.

Final verdict: **not proved** (the partial results are listed in §5).

Readings: (R1) and (R2) with H_0 = id, coarse, as in the brief; (Rig); Y non-constant. §4 alone uses the extra reading (R2^int), stated there.

---

## 1. Check of the derivation (round13_q5)

I re-read Lemmas 1, 2, 3, Proposition 4, Lemma 5 and §4 of round13_q5 against the definitions in the brief.

- **Lemma 1, step 2.** Points of T_t near p_* that are not in Λ_t lie over H_t(c∖Q). Reason: T_t ⊂ q^{-1}(H_t(c̄)) near 0, because closure(Ñ_c̃) ⊂ q^{-1}(H(c̄×Δ)), a closed set (H is a homeomorphism and c̄ is closed near Q). Also H_t(c̄) = H_t(c) ∪ {Q_t} near Q_t. So the step is correct.
  - The constant-vertex components c_t[w] (w ∉ M_W) survive as components of the limit Q_t = ξ̄(κ_∞, c_t), because c_t[w] lies in the open M_w.
- **Lemma 3.** A_y is closed analytic in T. "Intact" is the analytic condition that s_e = 0 for every edge e at y. On that set p ↦ [F_y(p)] is holomorphic, and Γ is closed analytic. The countability argument is correct.
- **Lemma 2 and Prop. 4.** These are formal consequences of (I1)–(I3) and Lemmas 1 and 3. Correct as stated.
- **Minor point 1.** Lemma 1 needs the label y to be of type (g_i, n_i) for the dichotomy "branch in Φ or ≡ Y_0". This holds because F_y(0) ≅ Y_0.
- **Minor point 2.** Lemma 5 uses the claim that Γ_{𝒲̃,c} has no constant branch at (Y_0,0) when it is irreducible and non-constant. That argument is correct (a 1-dimensional analytic subset of an irreducible curve is the whole curve).

**Verdict:** no flaw found, conditional on the cited inputs (I1)–(I6), which I did not re-derive.

---

## 2. Proposition M: a sheet-moving rigid twin with interior isotropy preserved

### 2.1 The data
Work at a generic point p of a boundary piece c, at t = 0. Let P be the stable curve at p, and assume the following.
- P has two components x, y, both ≅ Y_0 (types (g_i,n_i), with dim M_{g_i,n_i} ≥ 1).
- x is attached by one node e, and y by one node e′, to a part R of the curve that moves along c.
- Aut(P) = ⟨h⟩, h² = 1. The involution h swaps x and y, swaps e and e′, and acts on R by an involution exchanging the two attaching points. Along c, the moving part stays inside the h-symmetric locus.
- This is the same t = 0 combinatorics as in round13_q3 §1.2.

Choose h-equivariant coordinates on Def(P) (Cartan linearisation, cited from memory):
- z: a coordinate on the h-fixed directions along c (the moving part);
- s_e, s_{e′}: the plumbing coordinates;
- m_x, m_y: one modulus coordinate each, along a fixed holomorphic curve germ through Y_0 in M_{g_i,n_i}, transported to the x- and y-slots, with value 0 at Y_0;
- all remaining coordinates are set to 0. They span an h-invariant complement, so this is h-invariant.

Then h(z, s_e, s_{e′}, m_x, m_y) = (z, s_{e′}, s_e, m_y, m_x), and N = s_e s_{e′} near p.

**The surfaces and the 3-fold.**
- S := {(z, σ, 2σ, σ, 0)}, parametrised by (z, σ).
- hS = {(z, 2σ, σ, 0, σ)}.
- X := {(z, σ, 2σ, σ + t, 0; t)} ⊂ Def(P) × Δ, parametrised by (z, σ, t).

### 2.2 Proposition M (chart-level statement)
1. S ≠ hS, and S ∩ hS = c̃ := {σ = 0} = {(z,0,0,0,0)}. h fixes c̃ pointwise, and S ∩ Fix(h) = c̃.
2. The coarse germs are smooth: q(S) ≅ S, the coarse 𝒱 ≅ X, and t is a submersion on it. The coarse boundary of q(X_t) is {σ = 0}, and it lies in the stratum of c (s_e = s_{e′} = 0, and nothing else is pinched).
3. H_t(z, σ) := (z, σ), written in the S-coordinates resp. the X_t-coordinates, is a biholomorphism closure V_0 → closure V_t near p. It preserves strata and satisfies H_0 = id. So the chart versions of (R1), (R2), (i), (ii) and of reducedness hold.
4. **Interior isotropy is preserved.** For every t, no interior point of X_t ∪ hX_t is fixed by h. The only points with non-trivial stabiliser are on c̃ at t = 0.
5. **Twin anchored sheets.**
   - The boundary {N = 0} of X ∪ hX consists of T := {(z,0,0,t,0;t)} ⊂ X and hT = {(z,0,0,0,t;t)} ⊂ hX. Both contain c̃ × {0}.
   - On T: F_x has m_x = t, so its class is φ(t) with φ non-constant and φ(0) = Y_0. F_y ≡ Y_0, the rigid twin.
   - On hT the roles are exchanged.
   - Both values are constant along the piece (independent of z), as Lemma U requires.
6. **Split lifted family.** The lifted families of the piece through T and through hT are distinct components W ≠ hW with W_0 = (hW)_0 ⊇ E (the t = 0 lifted piece). This is the planner's case (A), realised locally.
7. Fix(h) ∩ (X ∪ hX) = c̃ × {0}. So **there is no family of h-symmetric curves**: neither interior curves F_t (Lemma R, case (R-i)) nor a pointwise-fixed boundary sheet (case (R-ii)). Lemma R, Prop. D and Prop. G do not apply, because their hypothesis h(X) = X fails: hX ≠ X.

*Proof.*
1. A point of S ∩ hS satisfies (σ, 2σ, σ, 0) = (2σ′, σ′, 0, σ′). Hence σ = 2σ′ and σ′ = 2σ, so σ = σ′ = 0. A point of S fixed by h needs s_e = s_{e′}, i.e. σ = 2σ, so σ = 0.
2. *q(S) is smooth.*
   - If q(s) = q(s′) with s, s′ ∈ S, then s′ ∈ {s, hs}. If hs ∈ S, then s ∈ S ∩ hS = c̃, where hs = s. So q|_S is injective.
   - The h-invariant function s_e + s_{e′} restricts to 3σ on S, and z is invariant. So the map S → B/⟨h⟩ is an injective immersion, and its image is smooth.

   *The coarse 𝒱 is smooth.*
   - Suppose h(z,σ,2σ,σ+t,0) ∈ X, i.e. it equals (z′, σ′, 2σ′, σ′+t, 0). Then 2σ = σ′, σ = 2σ′, 0 = σ′ + t and σ + t = 0. So σ = σ′ = 0 and t = 0.
   - Hence q|_X is injective off c̃ × {0}, where h fixes the points.
   - The invariants (z, s_e + s_{e′} = 3σ, m_x + m_y = σ + t) restrict to coordinates on X. So the coarse 𝒱 ≅ X is smooth, and t is a coordinate on it.

   *The boundary.* N|_{X_t} = 2σ², which vanishes exactly on {σ = 0}. There s_e = s_{e′} = 0, which is the stratum of c.
3. This follows from item 2, since H_t is the identity in the coordinates (z, σ).
4. An h-fixed point of X_t needs s_e = s_{e′}, i.e. σ = 0, and m_x = m_y, i.e. t = 0. The same holds for hX_t.
5. This is direct computation. Both T and hT meet {t = 0} in c̃ × {0}.
6. The value of vertex x is t on W and 0 on hW, so W ≠ hW. At t = 0 both are E.
7. This was computed in item 4. ∎

### 2.3 Consequences
- **(M-a)** The sheet-moving twist (aS ≠ S), listed as "not treated" in round13_q4 §5 and round13_q6 (Refl)(b), occurs at chart level. It is compatible with (R1), (R2) and Lemma U, and also with preservation of interior isotropy. Its mechanism is different from the reflection case: the isotropy drop happens **only on the boundary**, where the two sheets S, hS crossing along c̃ separate for t ≠ 0. No interior orbifold point is created.
- **(M-b)** So the global object of round13_q4 §3 and round13_q6 §4 (a 2-dimensional family 𝒵 or 𝒟 of symmetric curves with 𝒵_0 ⊃ c) does **not** exist in general for (NRT_P) failures. An argument based on excluding 𝒵 (for example by negativity) can at best settle the reflection case.
- **(M-c)** Like the earlier models, the model does not test total geodesy of S at t = 0. The relevant t = 0 question is stated in §5 as (Q-TG).

---

## 3. Lemma 3.1: why a single 3-fold cannot carry a failure

Extend Prop. M to a puncture by letting the moving part R acquire a node f.
- Replace the coordinate z by the plumbing coordinate s_f, so that Q = {s_f = σ = 0} and N = s_e s_{e′} s_f.
- Keep S, X as above with z := s_f. In S there is then a second boundary branch d̃ = {s_f = 0}, along which s_e, s_{e′} ≠ 0 and m_x = σ: the label x is merged into a moving vertex along d̃.
- The lift-curves at Q are L = {(0,0,0,t,0;t)} ⊂ X and hL = {(0,0,0,0,t;t)} ⊂ hX, with L ≠ hL. Along L, x has value φ(t) and y = h^{-1}x is rigid. So this is an (NRT_P) configuration at chart level, with a = h ∈ Stab_pt(c̃).

**Lemma 3.1.** This extended chart model violates (Rig).

*Proof.*
- The boundary of X_t near Q contains the branch d_t := {s_f = 0} ∩ X_t = {(0, σ, 2σ, σ + t, 0)}, which passes through the lift point L_t = (0,0,0,t,0).
- On the stratum of d the edges e, e′ are smoothed, so the components x, y and the adjacent part of R lie in a single vertex of G_d. That vertex is moving, because m_x = σ + t varies along d_t.
- Let W_d be the component of the lifted family of d through the sheet {s_f = 0} ⊂ X. By (Rig) (Lemma U, (I4)), the stable curves obtained as limits of the moving vertex at the puncture are components of coordinates of points of F_{W_d}, a finite set independent of t.
- But at Q_t (σ = 0) the degeneration contains the component x with class φ(t), which is non-constant. So φ(t) would lie in a finite t-independent set for all small t. That is a contradiction. ∎

**Moral.** Inside one 3-fold component X with a single lift-curve, the MOV/MERGE endpoint mechanism of the chain is effective. The anchored sheet of the outgoing branch contains the same lift-curve L, so the tracked label is the Φ-label there. A genuine (NRT_P) failure (one compatible with (Rig)) therefore needs one of two things:
- (F1) the Φ-sheet of β̃ and the relevant sheet of b̃ lie in **different** 3-fold components (X and gX, g ∉ G_X); or
- (F2) a single 3-fold component containing **several** lift-curves (isotropy drop inside G_X, as in the reflection models of round13_q3/q4/q6).

---

## 4. Proposition 4.2 (sketch): under interior-isotropy preservation only (F1) remains

**Reading (R2^int)** (extra; strictly weaker than (R2^orb)). For every z ∈ V_0 and every t, the curve H_t(z) has an automorphism group of the same order as z. Equivalently, interior orbit types in orbifold charts are preserved. Boundary points are unrestricted. Prop. M satisfies (R2^int).

**Lemma 4.1 (sketch).** Assume (R2^int). Let Q ∈ B_0, with chart (B, G = Aut(Q), q), and 𝒴 := q^{-1}(V_0) ∩ (B ∖ {N = 0}), a G-space. Then:
- there is a G-equivariant continuous H̃: 𝒴 × Δ_ε → B ∖ {N = 0} with H̃_0 = inclusion and q∘H̃_t = H_t∘q;
- each H̃_t is injective;
- H̃ extends continuously to (normalisation of the closure of 𝒴) × Δ_ε, still equivariantly.

*Sketch.*
- **Existence.** Apply the covering homotopy theorem for orbit-type-preserving homotopies of orbit spaces of finite-group actions (Palais; Bredon, *Introduction to compact transformation groups*, Ch. II, Thm 7.3; cited from memory). Use it on the G-space 𝒴 × Δ_ε and the homotopy ((z,t),s) ↦ H_{st}(z).
  - Orbit types are preserved: (R2^int) gives equal orders, and upper semicontinuity of stabilisers along lifts gives equality of the stabilisers.
- **Injectivity.** If H̃_t(y) = H̃_t(y′), then y′ = gy, since H_t is injective. So g ∈ Stab(H̃_t(y)) = Stab(y), and therefore y′ = y.
- **Extension.** Fix a boundary point and let w be its image under H_t. Then q^{-1}(small neighbourhood of w) is a disjoint union of small balls around the finitely many lifts of w. The complement of a proper analytic subset in a small irreducible local branch is connected. So H̃ maps each punctured local branch into one ball, and continuity of H on closure(V_0) × Δ gives the extension to the normalisation. ∎

**Proposition 4.2 (sketch).** Assume (R2^int). Let S be a component of q^{-1}(closure V_0) ∩ B, irreducible as a germ at 0, and X_S := H̃(S^ν × Δ_ε). Then X_S ∩ Λ = L_0^S := H̃({ν_0} × Δ_ε), a single lift-curve; here ν_0 is the unique point of S^ν over 0. Hence, for every boundary-type anchored sheet T ⊂ X_S, P_Φ(T) = C_Φ(L_0^S) (Lemma 3 and (I2)). So within X_S, Φ-persistence is the same on all sheets, without (NRT_P).

*Sketch.*
- H̃_t(s) ∈ Λ_t ⇔ H_t(q(s)) = Q_t ⇔ q(s) = Q ⇔ s lies over 0.
- An irreducible germ has exactly one point of its normalisation over 0.
- A continuous section of Λ → Δ lies in one lift-curve. ∎

**Consequence.** Under (R2^int), every (NRT_P) failure is of type (F1). The chain's Lemma S̃′ puts β̃_m and β̃′_m in one sheet S. So a failure needs some branch (β̃ or b̃) to lie in two distinct sheets S ≠ gS, with its relevant anchored sheet in X_{gS}, where gL_0^S ≠ L_0^S. Prop. M shows that this is locally possible.

**What is missing to make §4 a proof under (R2^int):**
- (a) A proof that every anchored sheet of a branch c̃ lies in a single X_{S′} with S′ ⊃ c̃. This needs the analyticity of the sets X_{S′}.
- (b) A Φ-transfer (Lemma 5) that keeps track of which 3-fold component carries the sheet.

Neither is done here.

---

## 5. Summary: proved / not proved / open

**Proved:**
- §1: no flaw found in round13_q5's derivation, conditional on (I1)–(I6).
- §2, Proposition M: a chart-level sheet-moving rigid twin (h ∈ Stab_pt(c̃), hS ≠ S, split lifted family W ≠ hW). It is compatible with (R1), (R2), the stratum condition, reducedness, the Lemma U shape, and interior isotropy preservation. It has no h-symmetric curves in V_t. So the symmetric-family route (Lemma R, Prop. G, (NRT-Z)) cannot settle (NRT_P).
- §3, Lemma 3.1: the naive puncture extension of this model, with the MOV branch in the same sheet, violates (Rig). A failure needs (F1) or (F2).

**Sketched (not proved):** Lemma 4.1 and Proposition 4.2. Under (R2^int), each chart 3-fold component carries a unique lift-curve, so only (F1) failures remain.

**Not proved:** (NRT_P) under the coarse reading (R1)/(R2). No global counterexample is given either.

**Open questions:**
1. **(Q-TG), a t = 0 question.** Can a smooth, closed, totally geodesic V_0 have, at a generic point p of a boundary curve c, a chart sheet S ⊃ c̃ and h ∈ Stab_pt(c̃) with hS ≠ S? A negative answer would kill the sheet-moving case at generic points.
   - It would not kill the case where a moves c̃ at the puncture only.
   - Lemma NG does not forbid a t = 0 answer here, because (Q-TG) is not (NRT_P) itself.
2. (F1) at punctures where a ∉ Stab(c̃): exclude twin sheets in distinct 3-fold components X_S, X_{aS}, using (Rig) and the global walk.
3. (F2): the reflection case. This is open as in round13_q4/q6 ((NRT-Z), Prop. G).
4. Items (a) and (b) of §4.
5. (Rig) (entry 82): untouched.

**Final status: not proved.** (NRT_P) remains open. A counterexample to it would also be a counterexample to the problem (under (Rig)), and none is given.

=== END OF ANSWER round14_q3 ===
