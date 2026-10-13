# round12_q7 — attempt on the (β)-twist obstruction to MS11♭

**Status line.** PARTIAL. I do not prove MS11♭, and I do not build a counterexample. What I do: I replace the single function Y by the finite family Φ of all *non-constant* constant-vertex value functions with value Y_0 at t = 0 ("Φ-persistence"). In this reformulation every (β)-twist (and the initial twist) whose twin y has a **non-constant** value function ψ is harmless: persistence passes the twist, though its function changes from Y to ψ. The only surviving form of the (β)-obstruction is the **rigid-twin case**: on T the twin y has value ≡ Y_0 for all t. The same dichotomy holds at the endpoint: the merging label x is rigid on every anchored sheet of b̃. So the obstruction is sharpened from "an automorphism of Q lost by Q_t" to "a Φ-copy and a rigid copy of Y_0 exchanged by an automorphism at t = 0". The rigid-twin case stays open. The task's own criteria make this a partial answer.

Readings (R1), (R2) and the definitions (pieces, charts, labels, anchored sheets, lift-curves, P(T), C(L)) are those of the task file. Throughout: (Rig) holds, Y is non-constant (for contradiction), and the disc Δ is shrunk where needed.

---

## 1. The family Φ and Φ-persistence

**Constant-vertex value curves (R8-2, Lemma U and U4; re-checked).** Let W be a 2-dimensional irreducible component of a lifted family 𝒲_G, and u ∉ M_W a constant vertex. Then Γ_{W,u} := (pr_u, t)(W) ⊂ M_u × Δ is an irreducible curve, finite over Δ. Its fibre over t is the set of values of u on the components of W_t. Near t = 0, Γ_{W,u} (mapped to the coarse space 𝔐_u = M_u/S_{n_u}) is a finite union of irreducible local branches. Each branch is the graph of a multivalued (Puiseux) function of t.

**Definition.** Φ is the set of local branches φ at t = 0 of the curves Γ_{W,u} with
- (g_u, n_u) = (g_i, n_i),
- φ(0) = Y_0 (as classes in 𝔐 = M_{g_i,n_i}/S_{n_i}),
- φ not constant.

Here W ranges over the finitely many components of the 𝒲_G meeting {t = 0} near the relevant compact set, after shrinking Δ. So Φ is finite. Y ∈ Φ: Y is the value curve of the constant vertex i of ∂V_t, and it is non-constant by assumption.

A label z (chart vertex) at a point is a **rigid Y_0-copy** along something if its value is ≡ Y_0 there for all t.

**Definition (Φ-persistence).** Let T be an anchored sheet (germ at (0,0) of an irreducible 2-dimensional analytic set in B × Δ_ε) and z a label. z is **Φ-persistent on T, with function φ ∈ Φ**, if at every (p,t) ∈ T, z is intact at p and (class of F_z(p), t) lies on the branch φ. Put P_Φ(T) := {z : z is Φ-persistent on T with some φ ∈ Φ}. Since T is irreducible and the branches are finitely many, the function φ is determined by (z, T). Also P(T) ⊂ P_Φ(T): P(T) is the set of z with φ = Y.

**Generic times for Φ.** Put Z_Φ := ⋃_{φ∈Φ} Z_φ. Here Z_φ is the set Z of R8-2 §3 with Y replaced by φ:
- φ(t) ∈ 𝔉; or
- (φ(t), t) lies on some Γ_{W,u} whose branch through it is not φ; or
- φ(t) = φ′(t) for some φ′ ∈ Φ ∖ {φ}.

Each condition gives a discrete set, because φ is non-constant and distinct irreducible curves meet discretely. Φ is finite, so Z_Φ is discrete.

**Lemma 1.1 (Theorem 1 of R8-2 for every φ ∈ Φ).** Let t ∉ Z_Φ, and let y be a φ(t)-copy at a lift q of Q ∈ B_t, with φ ∈ Φ. Let b̃ be a lifted branch through q. Then y is either STAY along b̃, with (W,y) a φ-vertex (its value curve is the branch φ), or IMOV.

*Proof.* This is the proof of R8-2 Theorem 1 verbatim, with Y_t replaced by φ(t). The proof uses only three facts:
- φ(t) ∉ 𝔉 (for steps 1, 2 and 4);
- (φ(t), t) lies on no other value curve (for step 3);
- 𝔉 is a finite, t-independent set (from (Rig), through Lemma U).

The remark after Theorem 1 ("never compares two copies") applies unchanged. ∎

**Lemma 1.2 (constant vertices of a piece carry their value curve along a whole sheet).** Let c be a piece at t = 0, c̃ a lifted branch of c at Q, and T an anchored sheet of c̃. Let y be a label that is intact and constant along c̃ at t = 0, with F_y ≅ Y_0 there. Then T determines one branch ψ of a value curve Γ_{W,y} with ψ(0) = Y_0, such that at every (p,t) ∈ T, y is intact with F_y(p) of class ψ(t). Consequently exactly one of the following holds:
- ψ is non-constant, so ψ ∈ Φ and y ∈ P_Φ(T);
- ψ ≡ Y_0, and y is a rigid Y_0-copy on T.

*Proof.*
- T is irreducible. Its generic points (t ≠ 0) lie over the transported piece c_t = H_t(c). Fixing the identification of the generic pattern with G_c gives a holomorphic map from a dense open subset of T to ∏_w M_w. Its image is irreducible, so it lies in one component W ⊃ ĉ × {0} of 𝒲_{G_c}.
- y is constant on ĉ, so y ∉ M_W by U1 (constancy on one fibre component is equivalent to constancy on all).
- So on T over c_t, y is intact with constant value, and that value lies on Γ_{W,y}.
- At the points of T over Q_t (the lift-curves), y is still intact, and its value is the limit of the constant value. This uses c_D ∈ ∏ M_u (Lemma U), so constant values are smooth curves and no edge at y opens.
- T is irreducible, so the value t ↦ F_y lies on a single branch ψ.
- At t = 0, y is intact with F_y ≅ Y_0 along c̃, so ψ(0) = Y_0. ∎

## 2. The (β)-twist in the Φ-reformulation

**Proposition 2.1 (twists with a non-rigid twin are harmless).** Let T, σT be a (β)-edge: anchored sheets of one lifted branch c̃, with σ ∈ Stab_pt(c̃). Let x ∈ P_Φ(T), and put y := σ^{-1}x.
1. P_Φ(σT) = σP_Φ(T). If z ∈ P_Φ(T) has function φ on T, then σz has the same function φ on σT.
2. x ∈ P_Φ(σT) if and only if y ∈ P_Φ(T). In that case the function of x on σT is the function ψ of y on T.
3. In the task's failure configuration (x and y intact constant twins ≅ Y_0 along c̃ at t = 0, with x ∈ P(T) and y ∉ P(T)), Lemma 1.2 gives exactly one of:
   - ψ non-constant: then x ∈ P_Φ(σT) with function ψ, and the twist does **not** break Φ-persistence;
   - ψ ≡ Y_0: the **rigid-twin case**.

*Proof.*
1. σ ∈ Aut(Q) acts on B × Δ_ε, preserving t and the boundary. By (K3), F_{σz}(σp) ≅ F_z(p), and σ maps intact labels to intact labels. Applying this pointwise on T gives the claim.
2. This follows from (1): x ∈ σP_Φ(T) ⟺ σ^{-1}x ∈ P_Φ(T).
3. Combine (2) with Lemma 1.2 applied to y, which is intact and constant along c̃ at t = 0. ∎

The same argument applies verbatim to the **initial twist** τ ∈ Stab_pt(β̃): there the x-carrying anchored sheet of β̃ reaches X only after the twist τ.

**Corollary 2.2 (composites).** Take a path T_0, T_1, …, T_k in the sheet graph of D (inside a 3-fold component X ⊃ S × {0}), together with the initial twist. Suppose:
- every edge is a lift-curve edge, a t ≠ 0 curve edge outside (γ°), or a (β)-edge;
- at every (β)-edge (T_{j}, σ_jT_{j}), the label σ_j^{-1}x_j is not rigid on T_j, where x_j is the image of x after the earlier twists.

Then x_k := σ_{k}⋯σ_1x ∈ P_Φ(T_k). For lift-curve edges, P_Φ(T) = C_Φ(L) = P_Φ(T′) for a common lift-curve L; this is the Φ-version of round11_q4 Lemma 2.2 and is discussed in §3. For t ≠ 0 curve edges outside (γ°), persistence passes as in round11 Mechanism D, whose argument uses only Lemma 1.1.

So in the Φ-reformulation, the "label-moving composite of (β)-twists" obstruction reduces exactly to the rigid-twin case.

## 3. The Φ-version of the chain (what must be re-checked)

The chain of the task (steps 1–2 (a)–(d)) is phrased with "Y-persistent". Define **MS11♭_Φ**: the same as MS11♭, with
- hypothesis: "x Φ-persistent on some anchored sheet of β̃";
- conclusion: "x Φ-persistent on some anchored sheet of b̃".

The conclusion still gives, at t = 0, that x is intact along b̃ with F_x ≡ Y_0, and so still contradicts MERGE and MOV at the endpoint.

Uses of Y in the chain, with their Φ-versions:
- **Base.** Vertex i with φ = Y ∈ Φ. Unchanged.
- **Genericity.** Replace Z by Z_Φ (§1), which is still discrete.
- **Product-type endpoint (d).** It derives "Y_t lies in a finite set on an open set". The same argument gives "φ_t lies in a finite set on an open set" for the current function φ ∈ Φ. That is a contradiction because φ is non-constant.
- **P(T) = C(L)** (round11_q4 Lemma 2.2, round11_q1 Lemma 2.3). Its input is R8-2 Theorem 1 / Theorem N at generic t. Lemma 1.1 supplies this for every φ ∈ Φ, so P_Φ(T) = C_Φ(L) for boundary-type sheets, where C_Φ(L) is the set of labels whose value along L lies on some branch of Φ.
- **Lemma PT, Lemma J / Cor. J′, the transfer along D^{m+1} (B1♭, Lemma S(c)).** I have **not** re-read these proofs line by line; the file is too large to verify all of them here. Their statements use "Y" only as the value function of a constant vertex that is non-constant and generic. If any of them uses a property of Y that a general φ ∈ Φ lacks, the Φ-chain needs a repair there. I flag this as **to be checked**. I expect it to be routine, because R7-3 §4 already worked with the full family of constant-vertex functions.
- **One genuine change.** The function attached to the persistent label may change along the chain, from Y to ψ at a non-rigid twist. Every endpoint argument uses only that the current function is non-constant, so this is harmless.

**Conclusion of §§2–3.** If the substitutions above are valid (to be checked), then MS11♭_Φ, and with it MS8 and the goal under (Rig), hold unless one of the following occurs:
- the rigid-twin configuration of §4;
- the separate obstruction (γ°), not treated here.

## 4. The endpoint, and the remaining case stated precisely

**Lemma 4.1 (rigidity at the endpoint).** Let Q_0 be the endpoint of the walk, b̃ the terminal lift, and x the label that merges or moves along b̃ at t = 0. Then for every anchored sheet T_b of b̃ and every lift-curve L_b ⊂ T_b, x is a rigid Y_0-copy along L_b: on L_b, F_x ≡ Y_0, which lies in 𝔉. In particular, a (Rig) counterexample needs Y_0 ∈ 𝔉.

*Proof.*
- Take a lift-curve L. Q_t is a puncture of a piece through it. So every component of Q_t on L is either:
  - a constant vertex of that piece, whose value lies on a value curve; or
  - a component of a puncture value f_u(p), u ∈ M_W, whose class lies in the finite t-independent set 𝔉 (Lemma U3).
- Hence the value of x along L is a branch of a value curve, or a constant in 𝔉. Since F_x(0) ≅ Y_0, it is either in Φ or ≡ Y_0.
- Suppose it were in Φ along some L_b ⊂ T_b. Lemma 1.1 at generic t makes x STAY along the branches of T_b through L_b(t) (IMOV is excluded, because Q is a puncture of b by (P)). So x is intact and constant on T_b, and at t = 0 it is intact and constant along b̃. This contradicts MERGE/MOV of x along b̃.
- For the last clause: if Y_0 ∉ 𝔉, steps 1–2 of the proof of R8-2 Theorem 1 apply to the Y_0-copy x at t = 0 itself. They show that x neither merges nor puncture-moves at Q_0, so the endpoint could only be an interior MOV. ∎

So a counterexample must have, at the endpoint, a Φ-copy x along L_β ⊂ T_β and a rigid Y_0-copy a^{-1}x along L_β, where L_b = aL_β and a ∈ Aut(Q_0). This is again a rigid twin.

**Open case (R-twin).** Q ∈ B_0, a lifted branch c̃ through 0 of a piece c, a label pair x ≠ y = σ^{-1}x with σ ∈ Stab_pt(c̃) (or, at the endpoint, a ∈ Aut(Q)), and an anchored sheet T of c̃ such that:
- (i) at t = 0, x and y are intact constant Y_0-copies along c̃, exchanged by σ;
- (ii) on T, x has a non-constant value function φ ∈ Φ;
- (iii) on T, y has value ≡ Y_0 for all t (rigid), and Y_0 ∈ 𝔉.

Equivalently: the transported piece c_t has, for every t, one constant vertex of value exactly Y_0 and one of value φ(t), and these two vertices become exchanged by a generic automorphism of the curves of c at t = 0.

**Observations on (R-twin)** (true, but none of them closes the case):
1. (R-twin) is invisible at t = 0. Total geodesy (Lemma TG, Lemma PA, Lemma V) sees only V_0. At t = 0 the Φ-copy and the rigid copy are both intact constant Y_0-components exchanged by an automorphism. Distinguishing them needs first-order information in t, which round11_q6 §3 found to give nothing.
2. **Counting.** At t ∉ Z_Φ, the number m_t(q) of labels at a lift point q whose value lies on Φ is the same along every lifted branch through q at which Q is a puncture (Lemma 1.1). So m is locally constant on the Φ-network at generic t. Consequently every D-sheet T of X has the same |P_Φ(T)| = m*. A twist edge with rigid twin y swaps a Φ-label and a rigid label; it does not change the count. So counting alone cannot exclude (R-twin).
3. If no rigid Y_0-copy occurs anywhere along the walk (for instance if the only Y_0-copies of points of the walk with constant value curve are excluded by some other means), the chain closes, modulo §3's checks and (γ°).

## 5. Summary list

**Proved here.**
- Lemma 1.1: R8-2 Theorem 1 holds for every non-constant constant-vertex value function φ with φ(0) = Y_0, at t ∉ Z_Φ (Z_Φ discrete).
- Lemma 1.2: on an anchored sheet, a constant twin label carries a single value branch ψ; it is either non-constant (in Φ) or ≡ Y_0.
- Proposition 2.1 / Corollary 2.2: with Φ-persistence, a (β)-twist, or the initial twist, preserves persistence whenever the twin is not rigid. The persistent function changes from φ to ψ.
- Lemma 4.1: at the endpoint, the merging label is rigid on every anchored sheet of b̃, and a counterexample needs Y_0 ∈ 𝔉.

**Not proved / to be checked.**
- That Lemma PT, Lemma J / Cor. J′, the transfer along D^{m+1}, and round11_q4 Lemma 2.2 go through verbatim with Y replaced by a varying φ ∈ Φ (§3). I expect this to be routine, but I have not verified it.

**Open.**
- (R-twin), §4: a non-constant constant-vertex function φ and a rigid copy ≡ Y_0, exchanged at t = 0 by an automorphism σ of the curves of a piece.
- (γ°), untouched.
- (Rig) (entry 82), untouched.
- Realisability of (R-twin) by an admissible family with smooth totally geodesic V_0: no counterexample is constructed.

=== END OF ANSWER round12_q7 ===
