# round12_q5 — MS11♭: derivation of the claim from MS11♭ + (Rig), and a fresh attack

**Plan/status.** Task 1: derive "MS11♭ + (Rig) ⇒ problem's claim" from the ledger statements, and point out exactly what the derivation depends on. Task 2: attack MS11♭ starting from a FIRST MOVE not in the "already tried" table: **(LC) writing the lift-curves of Q_t out explicitly in the product chart ∏_v Def(F_v) of the stratum locus of Def(Q), then reading off which labels can be persistent on a sheet from its lift-curve.** Status at the end: Task 1 goes through, modulo the definitions behind entries 87 and 113 (details below). Task 2 gives a structural lemma (Lemma LC) and an exact reformulation (Prop. LC′) of what MS11♭ requires. **MS11♭ is NOT proved and NOT refuted.**

Readings used throughout: (R1) and (R2) as stated in the query, with H_0 = id. The orbifold reading (R2^orb) is not used, and V_t is not assumed totally geodesic for t ≠ 0.

---

## Task 1. MS11♭ + (Rig) ⇒ claim

Assume (R1), (R2), (Rig), and suppose for contradiction that t ↦ Y_t is non-constant. By entry 19 it is a holomorphic map Δ → M_{g_i,n_i}.

**Step 0 (start).** Take a generic point P of ∂V_0, and a lift of the branch of ∂V_0 through P into a chart at P. The stratum Δ_Γ is of product type. By (R2), H maps (closure V_0 ∩ Δ_Γ) × Δ onto closure 𝒱 ∩ (Δ_Γ × Δ). So the transport family of this branch lies over Δ_Γ, and at time t it lies over ∂V_t, where π_i ≡ Y_t. Hence vertex i is intact and ≅ Y_t at every point of every anchored sheet. In other words, label i is Y-persistent on every anchored sheet of the starting branch.

**Step 1 (walk chain).** Proposition K_w (entries 85, 98) gives a walk chain starting at P:
- pieces E_0 ⊃ ∂V_0, E_1, …, E_m;
- transition points Q_1, …, Q_m;
- an endpoint Q_* which is a MERGE or a MOV.

The chain has these properties:
- Each transition Q_k has an entering lift β̃_k and a leaving lift b̃_k, and both lie in one irreducible component S_k of q^{-1}(closure V_0) ∩ B. This is Lemma S̃′ (entry 98), and it is hypothesis (S) of MS11♭.
- By Cor. IMOV_all (entry 99), every genuine transition and the endpoint is a puncture of both adjacent pieces. This is hypothesis (P). The same entry rules out junction crossings, interior-MOV endpoints and turning twins.
- By entry 112 (B1♭), anchored sheets exist, and the walk's label stays on one lifted curve.

**Step 2 (transfer at a transition).** Suppose x_k is Y-persistent on an anchored sheet of β̃_k.
- **Non-product Q_k.** If β̃_k ≠ b̃_k, MS11♭ applies directly, with Q = Q_k, β̃ = β̃_k, b̃ = b̃_k and x = x_k. The hypotheses "Y non-constant" and (Rig) are the standing assumptions. It gives an anchored sheet of b̃_k on which x_k is Y-persistent. If β̃_k = b̃_k, there is nothing to transfer.
- **Product-type Q_k.** Lemma PT (entry 86) says there are no twins there. Lemma J (entry 87) then gives the trichotomy pinned / persistent / crossing. Crossings are excluded by entry 99. "Pinned" gives Y_t ≡ Y_0 by the pinning lemma (entries 14, 24), contradicting our assumption. So x_k is persistent.

**Step 3 (endpoint).** By induction the tracked label is Y-persistent on an anchored sheet of the last piece at Q_*. By the chain's construction, Q_* is a terminal MERGE or puncture-MOV of that label. So the track is aligned at every junction and at Q_*. Theorem R (entry 87) then gives Y_t ≡ Y_0, a contradiction. Entry 113 records the same chain in the run's form "MS11♭ + 19, 24, 84–87, 97–99, 112 ⇒ MS8", and entry 103 records "MS8/MS10 ⇒ claim under (Rig)".

**What the derivation depends on.**
- (a) The precise meaning of "aligned" in Theorem R, and the statement of MS8, are not reproduced in the query. I am checking against the ledger lines only. At that level of resolution the steps fit together: Step 2 is exactly the label transfer that Theorem R's alignment requires.
- (b) The conclusion needs (Rig), which is still OPEN (entry 82). So MS11♭ alone does not settle the problem; MS11♭ + (Rig) does.
- (c) Logically, MS11♭ contains "Y non-constant" as a hypothesis. Under (Rig) it is therefore equivalent to the claim (entry 122). So it is exactly as plausible as the problem's claim. I see no independent reason to believe it is false.

**Verdict on Task 1:** the derivation goes through, at the resolution of the cited ledger lines.

---

## Task 2. Attack on MS11♭ — first move (LC): lift-curves written out in the stratum chart

**Setting.**
- Def(Q) has plumbing coordinates (s_e) and component coordinates. The stratum locus Z_Q := {s_e = 0 for all e} is locally ∏_{v ∈ V(G_Q)} Def(F_v), where Def(F_v) is the universal deformation of the pointed component F_v.
- Aut(Q) acts on Def(Q) and permutes the factors according to its action on the labels.
- (R2) maps strata to strata, so Q_t := H_t(Q) lies in Δ_{G_Q}.
- A lift-curve L is an irreducible component of {(p,t) : q(p) = Q_t}. It therefore lies in Z_Q × Δ_ε.

**Lemma LC.** Let L be a lift-curve through (0,0). Suppose x, x' are labels with F_x(0) ≅ F_{x'}(0) ≅ Y_0 (twins), and that along L the label x is a Y_t-copy while x' is a Y_0-copy for all t. This is the rigid-twin configuration of entry 118. Then:
1. The Def(F_{x'})-coordinate of L is constant, equal to the base point 0.
2. The Def(F_x)-coordinate of L is a holomorphic curve y(t) with y(0) = 0. If Y is non-constant, y(t) ≠ 0 for small t ≠ 0.
3. For a ∈ Aut(Q) with a(x) = x', the curve a·L has the roles reversed: its x'-coordinate is y(t), up to the identification Def(F_x) ≅ Def(F_{x'}) induced by a, and its x-coordinate is 0. In particular a·L ≠ L.

*Proof.*
- (1) The map Def(F_{x'}) → M_{g_i,n_i} is the quotient by Aut(F_{x'}) near the base point. So the preimage of the single point Y_0 is the base point alone. (This may need a reordering of the special points; any such reordering is absorbed in Aut, since the identification is up to some ordering.)
- (2) The x-coordinate maps to Y_t, which is holomorphic and non-constant. Since the quotient map is finite, the coordinate is a holomorphic curve through 0 that is not identically 0, and its zeros are isolated.
- (3) This follows from equivariance of q.

∎

**Consequence (lift-curve form of MS11♭; compare entry 114).**
- Lemma LC shows that, near Q, the lift-curves of Q_t carry *different* Y_t-labels whenever Q has a twin pair that is not frozen together.
- Let T_β and T_b be anchored sheets of β̃ and b̃ that contain lift-curves L_β and L_b (entries 102 and 114). Then P(T_β) = C(L_β) and P(T_b) = C(L_b).
- So MS11♭ at Q is equivalent to: **(LC′)** some anchored sheet of b̃ contains a lift-curve L with C(L) ∋ x, given that some anchored sheet of β̃ does.
- By Lemma LC, the lift-curves through (0,0) are the curves a·L_β for a ∈ Aut(Q), modulo the stabiliser of L_β. The label x lies in C(a·L_β) if and only if a^{-1}(x) ∈ C(L_β).
- So **MS11♭ fails at Q exactly when every anchored sheet of b̃ contains only lift-curves a·L_β with a^{-1}x ∉ C(L_β).** Equivalently, the "lift-curve class" [a] ∈ Aut(Q)/Stab, attached to anchored sheets of b̃, differs from the class attached to β̃ by an element that moves x outside the persistent set.

**Proposition LC′ (exact reformulation; proved).** Under (R1), (R2), (Rig) and Y non-constant, assign to each anchored sheet T in the 3-fold component X ⊃ S × {0} (Mechanism D, entry 115) the set Λ(T) of lift-curves through (0,0) that it contains; Λ(T) is nonempty by entry 114. MS11♭ at Q is equivalent to the following: the function T ↦ ∪_{L∈Λ(T)} C(L), restricted to the anchored sheets of β̃ and of b̃, takes values that intersect.

*Proof.* Combine P(T) = C(L) for L ⊂ T (entry 114) with Lemma LC. ∎

**Why this does not close.**
- Lift-curves through (0,0) lie in Z_Q × Δ, which is the deepest stratum. Sheets of D (entry 115) are boundary-type and of dimension 2, and they meet Z_Q × Δ along curves.
- To force T_b to contain a lift-curve with x ∈ C, one would need a connection inside D from T_β to T_b that passes only through curves that are not twisted by twin automorphisms.
- Entry 116 shows the only obstructions are configuration (γ°) and label-moving composites of Stab_pt-twists. Entry 119 shows these are realised locally inside one 3-fold. Lemma LC does not exclude them: it describes the lift-curves but not which sheets contain them.
- What would be needed is a *global* input, that is, information not visible in Def(Q) × Δ_ε, forcing the twist class of b̃ relative to β̃ to be trivial. Neither the totally geodesic structure at t = 0 (Theorem TV, entry 70) nor (Rig) visibly supplies this. Both concern the coarse pieces, while the twist lives in the orbifold chart.

**Dead end recorded.** First move (LC) reduces MS11♭ to a statement about which lift-curve classes the anchored sheets of b̃ contain (Prop. LC′). This is essentially the lift-curve reformulation of entry 114, made explicit. It does not decide that statement. Combined with entry 119, this indicates that any proof must use information beyond the chart Def(Q) × Δ_ε together with coarse piece data.

---

## Summary: proved / not proved / open

**Proved (in this file, relying on cited ledger statements and standard facts):**
- Task 1: MS11♭ + (Rig) + the ledger results (entries 14, 19, 24, 85–87, 98, 99, 112, 113) imply the problem's claim. The check is at the resolution of the ledger lines, since the definitions behind "aligned" and MS8 are not reproduced in the query.
- Lemma LC: the explicit form of lift-curves at a twin pair in the product chart of the stratum locus.
- Prop. LC′: MS11♭ is equivalent to a condition on the lift-curve classes contained in anchored sheets of β̃ and b̃.

**Not proved:**
- MS11♭ itself.
- Any reduction of MS11♭ to a statement that is easier than the problem: under (Rig) it is equivalent to the claim (entry 122).

**Open:**
- MS11♭ (entry 124).
- (Rig) (entry 82).
- Whether a global (non-chart-local) argument can force the twist class of b̃ relative to β̃ to be trivial at non-product twin points.

=== END OF ANSWER round12_q5 ===
