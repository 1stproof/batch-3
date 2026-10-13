# round12_q1 — attempt on MS11♭

## 0. Status (read this first)

- **MS11♭ is NOT proved and NOT refuted here.** This file is PARTIAL. It contains no proof of the problem's claim and no counterexample.
- What the file does contain:
  1. **Lemma F** (proved): stabiliser transfer for anchored sheets. MS11♭ for (β̃, b̃, x) depends only on the Stab(b̃)-orbit of x. This gives a sufficient criterion (Cor. F2) that covers every case in which the "twin" automorphism fixes b̃.
  2. **Model M1** (proved, chart level): an explicit local model showing that the planner's proposed "2-dimensional analogue" in suggestion step 4 is false *as a local statement*. The claim was that g ∈ G_X fixing S × {0} pointwise fixes the lift-curve L_0. In M1 it does not. MS11♭ still holds in M1, by Lemma F. So step 4 of the suggestion has to be reformulated, and Lemma F shows that the reformulated version is automatic in the pointwise-fixed case.
  3. **Chain check** (§4): no flaw found in the steps I re-checked (2(b) at the endpoint, 2(d), step 1). I record two dependencies the chain must keep explicit.
  4. **A dead end** (§5): a "copy-free" variant of Proposition K that would avoid labels altogether. I say exactly where it fails.
- Readings throughout: (R1), (R2) with H_0 = id, the definitions of the brief (piece, chart Def(Q), labels, transport family Ñ_c̃, anchored sheet, Y-persistent, lift-curve, P(T), C(L)), and (Rig) and "Y non-constant" as hypotheses of MS11♭.

Plan as executed: (a) read the brief; (b) look for a global argument (total geodesy, or Y non-constant) that controls which lift-curve an anchored sheet of b̃ contains; (c) failing that, isolate what is provable and check the chain.

---

## 1. Inputs used (from the brief; not re-proved here unless said)

- (K1) The preimages in Def(Q) of a point near Q form one Aut(Q)-orbit. (K3) F_x(a p) ≅ F_{a^{-1}x}(p), and s_e(p) = 0 ⟺ s_{ae}(ap) = 0. Here a ∈ Aut(Q) acts on Def(Q), on labels (vertices of G_Q) and on edges. These are standard and are restated in R7-3 §1.
- Transport family Ñ_c̃: the connected component, containing c̃ ∖ {0}, of q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε). B is Aut(Q)-invariant.
- **(PC)** "P(T) = C(L)": for a boundary-type anchored sheet T and any lift-curve L ⊂ T, the set of labels Y-persistent on T equals the set of labels y with F_y ≅ Y_t along L. The brief attributes this to round11_q4 Lemma 2.2 and round11_q1 Lemma 2.3, under (Rig) and Y non-constant. **I have not re-checked (PC).** The brief's extract does not contain its proof. Only Cor. F2 below uses it; Lemma F does not.
- Every anchored sheet of b̃ contains at least one lift-curve. (This is round9_q2 Lemma 1, and B1♭ as used in the brief; again not re-checked by me.)

---

## 2. Lemma F (stabiliser transfer) — proved

**Lemma F.** Let c̃ be a lifted branch through 0 ∈ Def(Q). Let a ∈ Aut(Q) satisfy a c̃ = c̃ (setwise). Then:
1. a Ñ_c̃ = Ñ_c̃, so a permutes the irreducible components of closure(Ñ_c̃);
2. a maps anchored sheets of c̃ to anchored sheets of c̃;
3. for every anchored sheet T of c̃, P(aT) = a·P(T);
4. for every lift-curve L, C(aL) = a·C(L), and aL is again a lift-curve.

*Proof.*
1. The set q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε) is Aut(Q)-invariant, because q∘a = q and B is invariant. So a maps its connected components onto its connected components. a Ñ_c̃ is the component that contains a(c̃ ∖ {0}) = c̃ ∖ {0}, so it is Ñ_c̃. Since a is a biholomorphism of B × Δ_ε (acting trivially on t), it maps closure(Ñ_c̃) onto itself and permutes its irreducible components.
2. If T ⊃ c̃ × {0}, then aT ⊃ a c̃ × {0} = c̃ × {0}.
3. Let (p,t) ∈ T and y a label. By (K3):
   - y is intact at ap ⟺ every edge e at y has s_e(ap) = 0 ⟺ every edge a^{-1}e at a^{-1}y has s_{a^{-1}e}(p) = 0 ⟺ a^{-1}y is intact at p;
   - F_y(ap) ≅ F_{a^{-1}y}(p).

   Hence y is Y-persistent on aT ⟺ a^{-1}y is Y-persistent on T.
4. The set {(p,t) : q(p) = Q_t} is Aut(Q)-invariant, so a permutes its irreducible components. The identity for C is (K3) again. ∎

**Corollary F1.** Fix β̃, b̃, x as in MS11♭. The statement "x is Y-persistent on some anchored sheet of b̃" depends only on the orbit Stab(b̃)·x. Likewise, the hypothesis "x is Y-persistent on some anchored sheet of β̃" depends only on Stab(β̃)·x.

*Proof.* By Lemma F(2),(3), the union ⋃_T P(T) over the anchored sheets T of b̃ is Stab(b̃)-invariant. ∎

**Corollary F2 (a sufficient criterion for MS11♭; uses (PC)).** Let Λ_β^x be the set of lift-curves L contained in some anchored sheet T_β of β̃ with x ∈ P(T_β). Let Λ_b be the set of lift-curves contained in anchored sheets of b̃. If
  Λ_b ∩ Stab(b̃)·Λ_β^x ≠ ∅,
then the conclusion of MS11♭ holds for (β̃, b̃, x).

*Proof.*
- Let L = aL′ ∈ Λ_b with a ∈ Stab(b̃) and L′ ∈ Λ_β^x. By Lemma F(2), a^{-1} maps the anchored sheet T ⊃ L of b̃ to an anchored sheet a^{-1}T ⊃ L′ of b̃.
- Anchored sheets of b̃ are of boundary type: their pattern is the pattern of b̃, and that pattern is not all of E(G_Q), by (P).
- By (PC), P(a^{-1}T) = C(L′) = P(T_β) ∋ x. ∎

**What this says about failures.** A counterexample to MS11♭ needs every lift-curve met by an anchored sheet of b̃ to lie outside Stab(b̃)·Λ_β^x. In particular:
- If the automorphisms responsible for the twin (the g with g^{-1}x ∉ C(L_0)) all fix b̃ setwise, then no failure occurs. This holds, for example, when they lie in the pointwise stabiliser Stab_pt(S) of the common sheet S ⊃ β̃, b̃.
- So the case "g ∈ G_X fixes S × {0} pointwise" in the planner's step 4 is harmless, *whatever* g does to L_0. A failure needs a twin automorphism that moves b̃ (or β̃), i.e. one acting non-trivially on S or not preserving S.

This is consistent with the brief's description of Mechanism D, where labels change only by (β)-twists σ ∈ Stab_pt(c̃) and at (γ°)-edges. Lemma F is the elementary reason why a twist by an element of Stab(b̃) can always be undone.

---

## 3. Model M1: "g fixes S × {0} pointwise" does not imply "g fixes L_0" — proved (chart level)

The planner's step 4 asks for a 2-dimensional analogue of Lemma D3: *if g ∈ G_X fixes S × {0} pointwise, then g fixes the lift-curve L_0 setwise.* As a statement about local configurations this is false.

**The model.**
- Coordinates (u, v, w) on X ≅ C³, with t|_X = w².
- Def(Q) has coordinates (z_1, z_2, s_1, s_2, …). Embed X by ι(u,v,w) = (z_1 = u, z_2 = w, s_1 = v, s_2 = u² − w², other coordinates 0), together with t = w². This is injective and an immersion.
- G_Q has two edges e_1, e_2 with smoothing parameters s_1, s_2. Aut(Q) ⊇ ⟨g, h⟩ ≅ (Z/2)², acting by g: z_2 ↦ −z_2 and h: z_1 ↦ −z_1, fixing s_1 and s_2. On X: g(u,v,w) = (u,v,−w) and h(u,v,w) = (−u,v,w). Both preserve X, t, s_1 and s_2.
- S := X_0^{red} = {w = 0}, with coordinates (u, v). **g fixes S pointwise**; h acts on S by u ↦ −u.

**t = 0.** On S: s_1 = v and s_2 = u². The boundary curves of S are:
- β̃ = {v = 0} (the u-axis), with pattern {e_1};
- b̃ = {u = 0} (the v-axis), with pattern {e_2}.

Both pass through 0 and lie in S, so (S) holds. Q is a puncture of the piece of each, so (P) holds. They are distinct lifts (indeed lifts of different coarse branches).

**Coarse picture.** Take G_X = ⟨g, h⟩ and X the only component. Then q(X) = X/⟨g,h⟩ ≅ C³ with coordinates (U = u², v, t = w²): a smooth trivial family of planes over Δ.
- At time t the boundary is {v = 0} ∪ {U = t}.
- Q_t = (U, v) = (t, 0).
- The translation U ↦ U + t gives a homeomorphism H with H_0 = id that preserves the two strata {v = 0}, {U = t} and the point Q_t, as (R2) requires. It is holomorphic in t.

**Lift-curves.** {(p,t) ∈ X : q(p) = Q_t} = {v = 0, u² = w²} = L_0 ∪ L_1, with L_0 = {u = w, v = 0} and L_1 = {u = −w, v = 0}.
- gL_0 = L_1 = hL_0 ≠ L_0, although g fixes S × {0} pointwise. This refutes the proposed 2-dimensional analogue.

**Anchored sheets.**
- Of β̃: the preimage of the transported branch {v = 0} is T_β = {v = 0} ⊂ X, which is irreducible and contains both L_0 and L_1.
- Of b̃: the preimage of {U = t, v ≠ 0} is {u² = w², v ≠ 0}. It is connected (its two components meet along b̃ × {0}), so it is Ñ_b̃. Its closure has two irreducible components, T⁺ = {u = w} ⊃ L_0 and T⁻ = {u = −w} ⊃ L_1. Both contain b̃ × {0}, so both are anchored, and gT⁺ = T⁻ (Lemma F, g ∈ Stab(b̃)).

**MS11♭ in M1.** If x is persistent on T_β, then by (PC) x ∈ C(L_0) = P(T⁺). So MS11♭ holds in M1. This is consistent with §2: the automorphism g that moves L_0 fixes b̃.

**Moral.** In the pointwise-fixed case, (1L_X) can fail (here X contains two lift-curves), but this does no harm. The planner's sufficient condition (1L_X) is therefore stronger than needed. The right target is the condition of Cor. F2.

M1 is a chart-level model only. I do not claim that it is realised by a smooth, closed, totally geodesic V_0 and an admissible family. It is used only to show that a proposed local implication is false.

---

## 4. Check of the chain (problem ⇐ MS11♭ + (Rig))

I re-checked the following steps against the statements quoted in the brief.
- **Step 2(d), non-product endpoint.**
  - MS11♭ gives an anchored sheet T ⊃ b̃ × {0} with x Y-persistent on T. Restricting to t = 0: at every p ∈ b̃, x is intact and F_x(p) ≅ Y_0.
  - MERGE (some edge at x unpinched along b̃) contradicts intactness.
  - Puncture-MOV (x intact, F_x non-constant along b̃) contradicts F_x ≡ Y_0.
  - This step is correct.
- **(P) at the endpoint.** An iMOV endpoint (Q_0 in the stratum of b) is not covered by MS11♭, because (P) fails for b̃. It is removed by step 2(b): Theorem X*_all forces every boundary curve of the common sheet through Q_0 to lie over the branch of the piece containing Q_0, and Remark 3 there excludes two distinct lifts of one branch in one sheet. So b̃ = β̃, which contradicts "x constant along β̃, moving along b̃".
  - The same argument covers the case in which Q_0 is an interior point of the *entering* piece: then b̃ = β̃ again, and the endpoint is not a MERGE or MOV.
  - This relies on Theorem X*_all for non-product strata (entry 97, round10_q1), which I did not re-read; the brief records it as proved.
- **Step 1.** "Goal ⇐ MS8 + (Rig) + entry 19" is correct as a logical implication. It needs (Rig) **for the given family**, i.e. entry 82. That entry is OPEN, and it is not a consequence of MS11♭. So **even a proof of MS11♭ would not settle the problem**: (Rig) remains.
  - Remark from memory, not used: (Rig) is a rigidity statement for the moving parts of 1-dimensional boundary pieces. For a piece whose moving part is a Teichmüller curve in its max-speed factor, McMullen's rigidity theorem for Teichmüller curves (C. McMullen, "Rigidity of Teichmüller curves", 2009; quoted from memory) suggests that the max-speed projection cannot deform. The slower moving factors and the joint curve K ⊂ ∏_{u∈M} M̄_u are not covered by it. I did not pursue this.
- **Logical status.** MS11♭ assumes "Y non-constant", so *any* proof that Y is constant (under (R1), (R2), (Rig)) proves MS11♭ vacuously. Conversely, a counterexample to MS11♭ is a counterexample to the problem. MS11♭ is therefore exactly as hard as the problem under (Rig). Its value is only as a localisation of where a proof must act.

**Verdict:** no flaw found in the parts re-checked. The derivation does depend on entries 82 (open), 97–99 and (PC), which I did not re-check.

---

## 5. Dead end: a copy-free Proposition K

**Idea.** Replace the marked subsurface Σ_i in Prop K by the copy-free defect
  E(X) := min over subsurfaces Σ of the topological type of Σ_i of max(Ext_X(∂Σ)/δ, d(ψ_Σ(X), Y_0)/η).
Stop the ray at the first time T_n with E = 1. Twins would then never matter: switching from one Y_0-copy to another costs nothing.

**What works.**
- For a cylinder direction (Lemma NH(1)), the whole ray γ_n([0,∞)) stays within ρ_n → 0 of B_0, hence of B_0^∂:
  - for s ≤ S, by convergence to ∂V_0 (Lemma G′);
  - for s ≥ S, because Ext(c) ≤ e^{−2S}/m.
- In the sealed case (II-a) of round9_q1, every point of B_0^∂ has a Y_0-copy. By compactness E < 1 along the whole ray.
- A **single** subsurface Σ cannot remain a (δ,η)-copy for all s ≥ s_0. Sketch, not fully written out: its core part has fixed positive flat area, and the Teichmüller deformation of a positive-area flat subsurface has unbounded displacement. This is incompatible with ψ_Σ staying η-close to the fixed point Y_0, unless the area escapes into the boundary collars. Escaping area forces non-peripheral horizontal cylinders inside Σ, which pinch curves of Σ. This is the copy-free version of Lemma NH(2).

**Where it fails.**
- (a) For a cylinder direction, the copies may *switch* infinitely often (Σ_1, Σ_2, … with s → ∞), and E never reaches 1. This is exactly the "no well-founded quantity" problem of round9_q7 (R-tw), now at t = 0. Nothing in the argument bounds the number of switches.
- (b) For a recurrent direction (Kerckhoff–Masur–Smillie, quoted from memory: for a.e. direction the ray returns to a compact part of M_g), E does reach 1. But at that time the ray need not be close to B_0: with δ fixed and n → ∞ the stopping points converge to points of V_0, not of B_0. Taking δ → 0 afterwards produces a point of B_0 but no MERGE branch. The MERGE/MOV conclusion of Prop K needs the stopping point to lie *on* B_0, which only the cylinder direction provides.

So the copy-free stopping rule and Prop K's localisation on B_0 pull in opposite directions. Combining them would need a direction that is both cylinder-like (to stay near B_0) and releasing for every Y_0-copy. I could not find one.

---

## 6. Summary

**Proved here:**
- Lemma F and Cor. F1: anchored sheets and persistence sets are equivariant under Stab(c̃). MS11♭ depends only on the Stab(b̃)-orbit of x.
- Cor. F2 (uses (PC), which is cited and not re-checked): MS11♭ holds whenever Λ_b ∩ Stab(b̃)·Λ_β^x ≠ ∅. In particular it holds when every twin automorphism fixes b̃, e.g. when it lies in Stab_pt(S).
- Model M1: the implication "g ∈ G_X fixes S × {0} pointwise ⇒ gL_0 = L_0" (planner's step 4) is false in a chart-level model consistent with (R1), (R2). (1L_X) fails there, yet MS11♭ holds.

**Not proved:**
- MS11♭ itself, in any generality. Cor. F2 is a sufficient condition, i.e. a partial result in the sense of the task.
- No counterexample to MS11♭, or to the problem, was constructed.

**Open (precise):**
1. **(Twin-moves-b̃)** Exclude: a lift-curve met by the anchored sheets of b̃ lies outside Stab(b̃)·Λ_β^x. By Lemma F, any such failure needs an automorphism of Q that moves x to a non-persistent label and moves b̃ (or does not preserve the 3-fold component X).
2. **(Rig)** (entry 82). It is needed for the goal independently of MS11♭.
3. The cited prior inputs (PC), B1♭ and Theorem X*_all, which I did not re-check.
4. The copy-free variant of Prop K (§5): bound the number of copy switches along a cylinder-direction ray, or find a direction that both stays near B_0 and releases every Y_0-copy.

=== END OF ANSWER round12_q1 ===
