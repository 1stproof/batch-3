# round8_q4 — attempt to refute MS8

**Status / plan.** I tried (a) to build a counterexample, (b) to derive a known falsehood from MS8, and (c) to work out exactly what a counterexample would need.

**Result.**
- **No counterexample found.** I could not write down any explicit family V_t; the reasons are given in §6.
- **Nothing false follows from MS8.**
- **What is proved:**
  - a generic-time exclusion lemma (Lemma G);
  - a crossing-rigidity lemma (Lemma X);
  - a new sufficient criterion (Theorem 2V) under which (Rig) does force Y_t = Y_0. It needs neither (O) nor total geodesy, and it covers the quintic-type mechanism.
  - exact local tests of the twin-jump and crossing configurations against (Rig): both survive (Rig) locally, under explicit constraints.
- Throughout I assume (R1), (R2) and (Rig), and I write H_t for the stratum-preserving homeomorphism of (R2).

---

## 1. Notation; the finite sets F′, F″ fixed by (Rig)

**Labels and charts.**
- For R ∈ B_t := closure(V_t) \ V_t, let Def(R) be the versal deformation germ, with smoothing parameters s_e, e ∈ E(G_R).
- The labels ℓ ∈ V(G_R) name the components R_ℓ of R. Each R_ℓ carries as special points its node branches.
- A lifted branch b̃ ⊂ Def(R) through 0 of a 1-dimensional branch b of B_t at R has a constant pattern S_b = {e : s_e ≡ 0 on b̃}.
- b is a *boundary branch* if R is not in the stratum of b. Then R corresponds to a puncture p of the piece E containing b, lifted by b̃ (R7-4 Lemma 1, step 1).
- The label ℓ is *merged* along b̃ if some edge at ℓ is not in S_b, and *intact* otherwise.
- [ℓ] denotes the vertex of the piece's graph G_b = G_R/(E∖S_b) that contains ℓ.

**The set F′.** For (G, M, K) ∈ 𝒦:
- K ∩ ∂(∏_{u∈M} M̄_u) is finite, because K is an irreducible closed curve not contained in the boundary.
- Let F′ be the set of isomorphism classes, as pointed curves with unordered special points, of the smooth irreducible components of the curves pr_u(z), for z ∈ K ∩ ∂, u ∈ M, (G, M, K) ∈ 𝒦.
- F′ is finite and does not depend on t.

**The set F″.** For (G, M, K) ∈ 𝒦, u, x ∈ M, and each of the finitely many points m ∈ M_u whose class lies in F′:
- pr_u|_K is non-constant, because u ∈ M is a non-constant vertex and K is the closure of the image of the piece. So K ∩ pr_u^{-1}(m) is finite.
- Let F″ be the set of classes of pr_x(k) for all such k (when pr_x(k) is a smooth curve). F″ is finite.

**Generic times.**
- t ↦ Y_t is holomorphic (PR-A), and so is its composition with the finite map to the coarse space M_{g_i,n_i}/S_{n_i}.
- If Y is non-constant, Z := {t : class(Y_t) ∈ F′ ∪ F″} is discrete in Δ. Call t ∉ Z *generic*.

**Lemma P (puncture values).** Let b be a boundary branch at R ∈ B_t with lift b̃ and piece E. Let ℓ be a label that is merged along b̃, or intact with [ℓ] = {ℓ} ∈ M(E). Then class(R_ℓ) ∈ F′.

*Proof.*
1. ν(p) ∉ ∏_w M_w, since p is a puncture.
2. Vertices w ∉ M(E) are constant, with values in M_w.
3. Hence z := pr_{M(E)} ν(p) ∈ K(E) ∩ ∂, and (G_b, M(E), K(E)) ∈ 𝒦 up to Aut(G_b).
4. If ℓ is merged, f_{[ℓ]}(p) = pr_{[ℓ]}(z) is the curve glued from the R_y, y ∈ [ℓ], along the unpinched edges. R_ℓ is a component of it, with the same special points (R7-1 Lemma 1(a)).
5. If ℓ is intact and non-constant, f_ℓ(p) = R_ℓ (R7-1 Lemma 1(b)).
6. In both cases [ℓ] ∈ M(E) is forced: a merged vertex has a nodal limit, so it is non-constant (PR-C, Lemma C2). Hence class(R_ℓ) ∈ F′. ∎

## 2. Lemma G (generic-time exclusion) — proved

**Lemma G.** Assume (Rig) and that Y is non-constant. Let t be generic, R ∈ B_t, and ℓ ∈ V(G_R) with R_ℓ ≅ Y_t. Then for every boundary branch b at R and every lift b̃:
- ℓ is intact along b̃;
- {ℓ} is a constant vertex of the piece of b, with value R_ℓ.

At generic t, therefore, a Y_t-copy never merges and never moves at a puncture. The only remaining way for it to move is along a branch whose stratum contains R ("interior-MOV").

*Proof.* Otherwise Lemma P gives class(Y_t) = class(R_ℓ) ∈ F′, contradicting genericity. ∎

**Corollary G1 (merging copies are frozen).** Let R ∈ B_0 and t ↦ q(t) a continuous lift of R_t := H_t(R) into the chart Def(R) (at R, i.e. at t = 0). Suppose that for all t in a connected set T ∋ 0 the label c is merged along some lifted boundary branch through q(t). Then class(comp_c(q(t))) is constant on T.

*Proof.* By Lemma P (applied in the chart at R_t, whose labels are induced from those at R because H_t preserves strata), the class lies in the finite set F′ and is continuous in t. ∎

So for every merge configuration supplied at t = 0 (Proposition K, or the admissible-cover merges for covering constructions), the merged Y_0-copy keeps the fixed class Y_0 at all small t. If Y is non-constant, it is therefore not a Y_t-copy, and the merge point must carry a *second* component ≅ Y_t: a twin. **Every counterexample to MS8 must contain twins at all such merge points.**

## 3. Theorem 2V (a sufficient criterion: (Rig) ⇒ Y constant) — proved

**Combinatorial notation.**
- Let P_0 ∈ closure(∂V_0) \ ∂V_0, with dual graph G′.
- As in PR-I, let 𝒞 be the set of S ⊂ E(G′) such that contracting E(G′) \ S gives a graph identified with Γ in which the preimage of i is a single loop-free vertex j(S).
- Let 𝒞_j := {S ∈ 𝒞 : j(S) = j}.

**Theorem 2V.** Assume (R1), (R2), (Rig) and the problem's hypotheses. Suppose that there is P_0 ∈ closure(∂V_0) \ ∂V_0 such that:
- **(Tw1)** for some neighbourhood U of P_0, (closure(V_0) \ V_0) ∩ U ⊂ ∂V_0 ∪ {P_0};
- **(C1)** on every component E_0 of ∂V_0 with P_0 ∈ closure(E_0), the only constant vertex is i;
- **(C2)** for every S ∈ 𝒞 there is an edge e ∈ E(G′) \ S that lies in no S′ ∈ 𝒞_{j(S)}.

Then Y_t = Y_0 for all t.

**Special case.** If Γ has exactly two vertices i and u, then (C1) is automatic: u must be non-constant, because dim ∂V_t = 1. (C2) is also automatic: 𝒞_j = {edges at j}, since every edge not contracted joins the two blocks (Γ has no loops, being of product type), and S ≠ E(G′) because P_0 ∉ Δ_Γ. So **(Tw1) at one cusp of ∂V_0 suffices when |V(Γ)| = 2.** No totally-geodesic input, no (O) and no Teichmüller-vertex input is needed beyond (Rig).

*Proof.* Suppose Y is non-constant.
1. **Excluded times.** Let Z_1 be the countable set of t at which some vertex that is non-constant on a component E_0 as in (C1) becomes constant on E_t := H_t(E_0). Its countability is R7-3 Lemma 1(b), a prior result; I re-read its rank argument and accept it. Fix t ∉ Z ∪ Z_1; such t exist.
2. **The transported cusp.** Put P_t := H_t(P_0).
   - P_t ∈ closure(∂V_t) \ ∂V_t.
   - G_{P_t} = G′, since strata are preserved.
   - Near P_t, B_t ⊂ ∂V_t ∪ {P_t}, because H_t(U ∩ closure V_0) is a neighbourhood of P_t in closure(V_t), mapped stratum-wise.
3. **The germ.** Work in Def(P_t). Let S̃ be the preimage of the germ of closure(V_t). It is analytic by (R1) and pure 2-dimensional.
4. **The first branch.** Take a lifted branch β̃ of ∂V_t through 0, lying in a component E_t.
   - By PR-I Lemma D(1), S_β ∈ 𝒞, and j := j(S_β) has P_{t,j} ≅ Y_t.
   - Every other label ℓ lies in the block of a vertex w ≠ i. By (C1) and t ∉ Z_1, w ∈ M(E_t). So by Lemma P (P_t is a puncture of E_t), class(P_{t,ℓ}) ∈ F′ ∌ class(Y_t).
   - **Hence j is the unique Y_t-copy of P_t.**
5. **Krull.** By (C2) choose e ∉ S_β lying in no element of 𝒞_j. Let X be an irreducible component of S̃ containing β̃.
   - s_e is not identically zero on X (it is nonzero on β̃ \ 0), and s_e(0) = 0. So X ∩ {s_e = 0} is pure 1-dimensional at 0.
   - Its points lie in ∂M̄_g, hence in B_t. By step 2, any branch b̃ of it lies over ∂V_t off 0.
   - b̃ ≠ β̃.
6. **The second branch.** By Lemma D(1), S_b ∈ 𝒞, and the label j(S_b) is a Y_t-copy. By step 4, j(S_b) = j, so S_b ∈ 𝒞_j. But e ∈ S_b, which contradicts the choice of e. ∎

**Remarks.**
- This is PR-I Theorem 4 with (Rig) in place of (O) and the Teichmüller-curve assumption. (C2) replaces (Tw2): with (Rig), a twin of Y_t inside any non-constant block is impossible at generic t.
- Theorem 2V applies to covering constructions over M_{0,5} with a 2-vertex Γ whenever, at some image cusp, all boundary branches lie in Δ_Γ. An example is the S_5-symmetric quintic of PR-I, but that one is not smooth.
- Hence **a counterexample must have, at every cusp of ∂V_0, either a boundary piece outside Δ_Γ (failure of (Tw1)), or (C1)/(C2) failing.**

## 4. Crossings under (Rig): Lemma X — proved

**Lemma X.** Assume Y is non-constant and t ∉ Z. Let R ∈ B_t be an interior point of a piece D, given by a lift d̃ ⊂ Def(R) with S_d = E(G_R), so that G_D = G_R as labelled graphs. Let x ∈ M(D) with R_x ≅ Y_t. Then for every boundary branch b at R, every lift b̃, and every u ∈ M(D) (including u = x):
- u is intact along b̃;
- {u} is a constant vertex of b's piece.

*Proof.*
1. Suppose not for some u. Lemma P gives class(R_u) ∈ F′, so R_u ∈ M_u is one of finitely many points m.
2. The point k := (R_w)_{w∈M(D)} lies in K(D), since it is the M(D)-projection of the point of D̂ over R.
3. pr_u(k) = m, so k ∈ K(D) ∩ pr_u^{-1}(m), a finite set.
4. Hence class(Y_t) = class(pr_x(k)) ∈ F″, contradicting t ∉ Z. ∎

**Consequences for a crossing at generic t.** Let R_t be an interior-MOV point, i.e. a point where the Y-network passes from a STAY piece D′ into a piece D on which the Y_t-copy x moves.
- **(X1) Y moves inside a fixed curve.** Y_t = pr_x(k_t) with k_t ∈ K(D). So Y_t ∈ closure(pr_x(K(D))) =: C_x, a fixed irreducible curve in M̄_{g_i,n_i}, for all t in a set accumulating at 0. Hence **Y(Δ) ⊂ C_x**: Y is a holomorphic disc in a fixed curve. If x is a maximal-speed vertex at t = 0, C_x is a Teichmüller curve (Lemma PA plus PR-F, modulo (F2)).
- **(X2) Orthogonality.** Along every boundary branch at R_t, all of M(D) is frozen into constant singleton vertices. Moreover the constant-vertex functions c′_u(t) of D′ (u ∈ M(D)) satisfy the algebraic relation (c′_u(t))_{u∈M(D)} ∈ K(D) for all t.
- **(X3) Survival.** The local model of R7-2 §4.2 satisfies (X1)–(X2) at every t:
  - smooth germ (σ, ρ), with s_e = ρσ for the edges at x and s_f = ρ for the others;
  - the x-coordinate is σ + κ(t), and {σ = 0} is the STAY piece, where the other components are smoothed into one moving block;
  - D = {ρ = 0}, with M(D) = {x}.

  This model has M(D) = {x}, so (X2) only says that x is constant along the STAY piece, which holds. Neither (Rig) nor Lemma G excludes it. It is excluded only if some u ∈ M(D) \ {x} sits in a moving block of some boundary branch at R_t.

## 5. Twin jumps under (Rig) — tested

**Model.** The R7-3 §5 model:
- a junction J with Y_0-copies x, y = σx, σ ∈ Aut(J_0);
- D^m through J̃(t) with x ↦ Y_t and y ↦ Y′_t (both constant vertices);
- D^{m+1} through σJ̃(t) with x ↦ Y′_t and y ↦ Y_t.

**Checks.**
- (Rig) constrains only non-constant vertices, and all vertices involved are constant. So **(Rig) is satisfied**, for any holomorphic Y′ with Y′(0) = Y_0.
- **Lemma G is satisfied at every generic t.**
  - At J̃(t) the unique Y_t-copy is x.
  - Along the lift σ^{-1}·(D^{m+1}-branch) through J̃(t), the vertex containing x corresponds, by (K3), to the vertex of D^{m+1} containing σx = y. That vertex is constant ≡ Y.
  - So the Y-network is consistent. Twin jumps per se survive.
- **Where a twin jump is constrained.** Combine with Corollary G1: Prop K's track ends at a MERGE point Q_0 whose merged label γc is frozen (class Y_0 for all small t). The network copy at Q_t is a different label with class Y_t. So a counterexample built on twin jumps needs:
  - **(T1)** a junction J_0 ∈ B_0 with two Y_0-copies exchanged by an automorphism of the stable curve J_0;
  - **(T2)** at the end point Q_0 at least two Y_0-copies: one that merges along the Prop K branch and keeps class Y_0 for all t, and one carried by STAY pieces with class Y_t;
  - **(T3)** by §3, the boundary near Q_0 is not of the form (Tw1) with (C1), (C2). So a second piece outside Δ_Γ passes through Q_0, or another constant vertex is present, or the combinatorics defeat (C2).

  For Galois covering constructions, (T1)/(T2) are typical, because deck transformations act on boundary curves and permute the components over a given base component. So these examples cannot be excluded by the present tools unless (Tw1)+(C1)+(C2) hold at some cusp.

## 6. Why no counterexample and no easy proof

**(i) No easy proof from (Rig).**
- (Rig) constrains only the non-constant parts K(E). The constant-vertex values, which include Y_t and all its twins, are unconstrained holomorphic functions of t (L1′, R7-3 Lemma 1).
- The two local models above (twin jump, orthogonal crossing) satisfy (Rig), Lemma G, Lemma X and Krull at time t, at every t.
- So any proof of MS8 must use global t = 0 information (total geodesy of V_0) and transport it in a way that survives twins and crossings. This is the open problem MS7 / Open Questions 1–2 of R7-2.
- The concrete form that suffices is Theorem 2V, or R7-4 Theorem 3 (TM).

**(ii) No counterexample.**
- A counterexample needs an explicit holomorphic, smoothly trivial family V_t ⊂ M_g of surfaces that are *not* totally geodesic for t ≠ 0. Its boundary must be controlled stratum by stratum ((R2)), and it must satisfy the global constraints of §§3–5.
- The only explicit 2-dimensional subvarieties of M_g whose boundary I can compute are covering constructions and the flex/gothic loci (cited from memory). These are rigid as totally geodesic subvarieties.
- I know no construction of non-totally-geodesic deformations with controlled boundary. Note that V_t must change complex structure, since log vector fields near closure(V_0) are tangent to V_0 (other files of this run).
- Hence (a) was not achieved and (b) gives nothing.

## 7. Summary: proved / not proved / open

**Proved** (assuming (R1), (R2), (Rig) and the cited prior results PR-A, PR-I Lemma D(1), R7-1 Lemma 1, R7-3 Lemma 1(b)):
1. Lemma P and Lemma G: at generic t (outside the discrete set Z), Y_t-copies never merge and never move at punctures.
2. Corollary G1: merged copies have a frozen class. Hence every merge point supplied at t = 0 must carry a twin in any counterexample.
3. **Theorem 2V**: MS8 holds whenever some cusp P_0 of ∂V_0 satisfies (Tw1), (C1), (C2). In particular it holds whenever |V(Γ)| = 2 and (Tw1) holds at one cusp.
4. Lemma X: at an interior-MOV (crossing) point at generic t, Y_t ∈ C_x, a fixed curve, so Y(Δ) ⊂ C_x; and all of M(D) is frozen along every boundary branch (orthogonality).
5. The twin-jump and orthogonal-crossing local models satisfy (Rig), Lemma G and Lemma X. So (Rig) alone does not quickly force Y to be constant; any proof needs global t = 0 input.

**Not achieved:** an explicit counterexample to MS8, and a derivation of a falsehood from MS8.

**Open:**
- **(Q1)** Does every smooth closed totally geodesic V_0 have a cusp of ∂V_0 satisfying the hypotheses of Theorem 2V, or (TM) of R7-4 Theorem 3? If so, MS8 follows.
- **(Q2)** Can a crossing with Y(Δ) inside a fixed Teichmüller curve C_x be globally realised?
- **(Q3)** Can a twin-jump network ((T1)–(T3)) be realised by an actual family? This is equivalent to the existence of an Aut-closed network (MS7 of R7-3) for some admissible V_0.
- MS8 itself remains **open**.

=== END OF ANSWER round8_q4 ===
