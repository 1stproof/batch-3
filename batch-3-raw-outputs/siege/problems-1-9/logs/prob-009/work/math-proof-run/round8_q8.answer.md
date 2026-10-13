# round8_q8 — answer (MS8)

**Status line.** MS8 is NOT proved in full here, and no counterexample is given. What this file proves:
1. A partial theorem (Theorem 1). Twins are handled exactly when a *star-coherence* condition (SC) holds at the finitely many points of Prop K's chain. (SC) holds automatically when the automorphism groups of those points do not drop under the deformation ("isotropy preservation", (IP)). Under (IP) and the other hypotheses, MS8 follows whenever Prop K's endpoint is MERGE or puncture-MOV.
2. A precise description of what a failure of (SC) forces (Proposition 3, a "persistent twin" along a whole piece).
3. A precise description of the crossing endpoint at generic times under (Rig) (Lemma 4, a "pure crossing").
4. A reading remark. If "smoothly trivial" is read in the orbifold sense, so that (IP) holds everywhere, the twin obstruction disappears completely, and MS8 reduces to the single interior-MOV (crossing) case.

The open cases are listed at the end: (O1) twins with (SC) failing, under plain (R2); (O2) crossing endpoints.

Plan (written first, as required): (a) set-up and two elementary lemmas; (b) Theorem 1, with proof; (c) the (IP) corollary and the orbifold reading; (d) what a twin jump forces; (e) pure crossings at generic t; (f) the chain check; (g) proved / not proved / open.

---

## 0. Conventions and inputs

All of the following are adopted verbatim from the task: readings (R1) and (R2) with H_0 = id, B_t := closure(V_t) \ V_t, "piece", ν, puncture, f_u, M(E), K(E), and (Rig).

- For a stable curve J, Def(J) is its versal deformation germ, with smoothing parameters s_e (e ∈ E(G_J)). Aut(J) acts on Def(J), and π: Def(J) → Def(J)/Aut(J) is a neighbourhood of J in M̄_g.
- For a vertex x put L_x := {s_e = 0 for all edges e at x}. F_x: L_x → M_{g_x,n_x} is the x-component of the fibre curve.
- Facts (K1)–(K3) of R7-3 §1 are used. Cited from memory as standard:
  - (K1) the preimage of a point is one Aut(J)-orbit;
  - (K3) F_x(σq) ≅ F_{σ^{-1}x}(q).
- (K4) (standard, from memory; the local structure of the Deligne–Mumford stack M̄_g = [Def(J)/Aut(J)] near J) For q ∈ Def(J) close to 0, Aut(fibre curve at q) ≅ Stab_{Aut(J)}(q). Hence for J′ near J,
  #π^{-1}(J′) = |Aut(J)| / |Aut(J′)|.
- "≅" between pointed curves always means: isomorphic after some relabelling of the special points. Equivalently, the images [·] in the coarse space M_{g_i,n_i}/S_{n_i}, which is a reduced complex analytic space, are equal.

**Transport families** (R7-3 Lemma 2, R7-4 Lemma 2; I re-checked the steps used).
- Let J ∈ B_0, and let β̃ be a lifted branch at 0 ∈ Def(J) of a piece D. Either J is a puncture of D, or J lies on D and β̃ is the lifted germ of D.
- Put N := H((β \ {J}) × Δ_ε), and let Ñ be the connected component of π^{-1}(N) ⊂ Def(J) × Δ_ε that contains β̃ \ {0}.
- Then the pinched-edge pattern is constant on Ñ, and Ñ ∩ {t = 0} = β̃ \ {0}.
- For every t, closure(Ñ_t) contains at least one point of π^{-1}(J_t), where J_t := H_t(J).
- If D lies in a product-type stratum and the vertex c of D is constant on D with c = {x} along β̃, then Ñ_t ⊂ L_x and F_x ≡ φ_c(t) on Ñ_t. Here φ_c(t) is the (constant) value of c on the transported piece D_t = H_t(D). The proof uses L1 for product type (R7-5 §1.2), which I checked.
- t ↦ φ_c(t) is holomorphic (R7-3 Lemma 1(a)).
- Since L_x is closed and F_x is continuous on it, **F_x ≡ φ_c(t) on closure(Ñ_t) ∩ L_x = closure(Ñ_t)**. (∗)

**Input (K′) (Prop K, PR-H §3, in the reading of R7-3 §1).** Taken as input, "proved modulo routine marking details" there and not re-proved here. There are:
- points J_0 = P ∈ ∂V_0, J_1, …, J_{k−1} (junctions) and J_k = Q_0 (endpoint), all in B_0;
- pieces D^1, …, D^k at time 0, with D^1 the component of ∂V_0 through P;
- for each m, a vertex c_m of D^m that is constant on D^m with value ≅ Y_0, where c_1 = i;
- for 1 ≤ m ≤ k−1: lifted branches β̃^m_+ (of D^m) and β̃^{m+1}_− (of D^{m+1}) at 0 ∈ Def(J_m), and a chart vertex x_m of G_{J_m}, with c_m = {x_m} along β̃^m_+ and c_{m+1} = {x_m} along β̃^{m+1}_−;
- at Q_0: a lifted branch β̃^k_+ of D^k with c_k = {x}, and a lifted branch β̃^E at 0 ∈ Def(Q_0) of a piece E, of one of three types:
  - **(MERGE)** the vertex class u of E containing x contains an edge of G_{Q_0} that is unpinched along β̃^E;
  - **(pMOV)** x is intact along β̃^E, f_{\{x\}} is non-constant on E, and Q_0 ∉ stratum(E);
  - **(iMOV)** as (pMOV), but Q_0 ∈ stratum(E) (a crossing).

**Hypothesis (PT_chain).** The pieces D^1, …, D^k and E lie in product-type strata. This is needed for L1. R7-5 §1.4 shows that L1 can fail for non-product strata; this caveat is inherited from R7-1 (T2) and R7-2 (PT).

## 1. Two elementary lemmas

**Lemma 1 (identity theorem in the coarse space).** Let f, g: Δ → Z be holomorphic maps into a reduced complex space Z. If {f = g} has an accumulation point in Δ, then f ≡ g. If f takes values in a finite set A on a set with an accumulation point in Δ, then f is constant.

*Proof.*
- {f = g} is an analytic subset of Δ: locally, embed Z in C^N and compare coordinates. A proper analytic subset of the connected Δ is discrete, so one with an accumulation point is all of Δ.
- For the second claim, some a ∈ A is taken on a set with an accumulation point. Apply the first claim with g ≡ a. ∎

**Lemma 2 (the finite set from (Rig)).** Put
 F := { pr_u(κ) : (G, M, K) ∈ 𝒦, u ∈ M, κ ∈ K ∩ ∂(∏_{u∈M} M̄_u) }.
Let A ⊂ M_{g_i,n_i}/S_{n_i} be the finite set of classes of smooth components of elements of F, of type (g_i, n_i), taken with their special points.
1. F and A are finite. For every piece E at every time t, every u ∈ M(E) and every puncture p of E, f_u(p) ∈ F up to relabelling.
2. If Y is non-constant, then Z_A := {t : [Y_t] ∈ A} is a closed discrete subset of Δ.

*Proof.*
1. K is irreducible and not contained in the boundary, so K ∩ ∂ is a proper analytic subset of a compact irreducible curve, hence finite. 𝒦 is finite.
   - At a puncture p, some coordinate of ν(p) lies in a boundary. Constant vertices take values in M_w. So the boundary coordinate is some u ∈ M(E), and pr_{M(E)}ν(p) ∈ K(E) ∩ ∂.
   - (Rig) identifies (G, M(E), K(E)) with an element of 𝒦 up to Aut(G). This only renames the vertices and the marked points.
2. t ↦ [Y_t] is holomorphic (PR-A, composed with the quotient map). It is non-constant: otherwise Y_t would lie in a finite S_{n_i}-orbit, and by continuity Y would be constant. Lemma 1 then gives the claim. ∎

## 2. Theorem 1: MS8 under star coherence (proved, given the inputs listed)

**Notation.** Write Ñ^m_+ and Ñ^{m+1}_− for the transport families of β̃^m_+ and β̃^{m+1}_− at J_m. At m = k write Ñ^k_+ and Ñ^E for those of β̃^k_+ and β̃^E at Q_0. Put J_{m,t} := H_t(J_m). The two families compared at J_m are:
- Ñ^m_+ and Ñ^{m+1}_−, for m < k;
- Ñ^k_+ and Ñ^E, for m = k.

**Definition.**
- (SC_m) (*star coherence at J_m*): the set
 T_m := { t ∈ Δ_ε : closure(first family at J_m)_t ∩ closure(second family at J_m)_t ∩ π^{-1}(J_{m,t}) ≠ ∅ }
 has an accumulation point in Δ_ε.
- (NT_m): every σ ∈ Aut(J_m) fixes the tracked chart vertex (x_m, or x at m = k).
- (C_m) := (SC_m) or (NT_m).

**Theorem 1.** Assume:
- (R1), (R2) and the hypotheses of MS8, including (Rig);
- the input (K′), with endpoint of type MERGE or pMOV;
- (PT_chain);
- (C_m) for every m = 1, …, k.

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*

**Step 1: [φ_{c_m}] ≡ [Y] for all m, by induction.**
- *Base.* c_1 = i on the component D^1 of ∂V_0, and vertex i is ≡ Y_t on ∂V_t. So φ_{c_1} = Y.
- *Induction step, case (SC_m).* Let t ∈ T_m and pick j̃ in the triple intersection defining T_m. By (∗), applied to both families with the same chart vertex x_m:
 F_{x_m}(j̃) ≅ φ_{c_m}(t) and F_{x_m}(j̃) ≅ φ_{c_{m+1}}(t).
 So [φ_{c_{m+1}}(t)] = [φ_{c_m}(t)] = [Y_t] for t ∈ T_m. By Lemma 1, [φ_{c_{m+1}}] ≡ [Y].
- *Induction step, case (NT_m).* Pick any j̃^+ ∈ closure(Ñ^m_{+,t}) ∩ π^{-1}(J_{m,t}) and j̃^− ∈ closure(Ñ^{m+1}_{−,t}) ∩ π^{-1}(J_{m,t}). Both sets are nonempty (§0).
  - By (K1), j̃^− = σ j̃^+ for some σ ∈ Aut(J_m).
  - By (K3) and σ^{-1}x_m = x_m: F_{x_m}(j̃^−) ≅ F_{x_m}(j̃^+).
  - Conclude as in the (SC_m) case, now for every t ∈ Δ_ε.

**Step 2: the endpoint.** Let t ∈ T_k in case (SC_k), or any t ∈ Δ_ε in case (NT_k). Choose q̃ ∈ closure(Ñ^E_t) ∩ π^{-1}(Q_t) such that F_x(q̃) ≅ φ_{c_k}(t) ≅ Y_t. This uses Step 1 and (∗), and in case (NT_k) the (K3)-trick of Step 1.
- Pattern and vertex structure are constant on Ñ^E. So along Ñ^E_t the vertex class of x is the class u that it has along β̃^E.
- Take r_n ∈ Ñ^E_t with r_n → q̃. By (PT_chain), their images lie in the lifted transported piece E_t ⊂ ∏_w M_w. By properness of ν_t they converge to ν_t(p′) for some p′ ∈ Ē_t.
- H_t preserves strata and Q_0 ∉ stratum(E). So Q_t ∉ stratum(E_t), and ν_t(p′) ∉ ∏_w M_w, because ξ̄ maps ∏_w M_w into Δ_{G_E}. Hence p′ is a puncture.
- By continuity of the plumbing (Def1), f_u(p′) is the curve glued from the components F_y(q̃), y ∈ u, along the edges of u unpinched along β̃^E. Its component F_x(q̃) keeps its special points (R7-4 Lemma 1, step 3). So F_x(q̃) ≅ Y_t is a component of f_u(p′).
- **(MERGE).** f_u(p′) has a node. A constant vertex has a smooth limit, so u ∈ M(E_t). By Lemma 2, f_u(p′) ∈ F, so [Y_t] ∈ A.
- **(pMOV).** Here u = {x}. By R7-2 Lemma 2.1, applied to the irreducible lifted family of E (product type, Lemma R0), x ∈ M(E_t) for all t outside a closed discrete set D_E. For such t, f_x(p′) ≅ Y_t lies in F, so [Y_t] ∈ A.
- In both cases [Y_t] ∈ A for all t in T_k \ D_E (or Δ_ε \ D_E). This set has an accumulation point in Δ_ε, because D_E is closed and discrete. By Lemma 1, [Y] is constant. Since Y is continuous and the map M_{g_i,n_i} → M_{g_i,n_i}/S_{n_i} has finite fibres, Y is constant, i.e. Y_t = Y_0 for all t. ∎

*Remarks.*
1. Step 1 uses neither (Rig) nor "generic t". (Rig) enters only at the endpoint, through Lemma 2.
2. Theorem 1 is the common form of R7-3 Theorem A (which assumed (NT) everywhere) and R7-1 Theorem T (which assumed (Lock)). The new point is that (SC) is exactly what the twin step needs. Below it is shown to follow from a purely group-theoretic condition, (IP).

## 3. When does (SC) hold? Isotropy preservation and the orbifold reading (proved)

**Corollary 1.** (SC_m) holds in either of the following cases.
- (a) **(IP_m)**: |Aut(J_{m,t})| = |Aut(J_m)| for t in a set with an accumulation point in Δ_ε.
- (b) The lifted branch defining one of the two families at J_m is Aut(J_m)-invariant, i.e. Stab_{Aut(J_m)}(β̃) = Aut(J_m).

*Proof.*
- (a) By (K4), #π^{-1}(J_{m,t}) = |Aut(J_m)| / |Aut(J_{m,t})| = 1 for those t. Both closures contain a point of π^{-1}(J_{m,t}) (§0), so they contain the same point.
- (b) If a ∈ Stab(β̃), then aÑ is the component of π^{-1}(N) containing aβ̃ \ {0} = β̃ \ {0}. So aÑ = Ñ.
  - Hence closure(Ñ_t) ∩ π^{-1}(J_{m,t}) is a nonempty Stab(β̃)-invariant subset of one Aut(J_m)-orbit (K1). If Stab(β̃) = Aut(J_m), it is the whole orbit.
  - So it contains the point that the other closure contains. ∎

**Corollary 2.** Assume the hypotheses of Theorem 1, but replace (C_m) by: "(NT_m), (IP_m) or Corollary 1(b) holds at each J_m". Then Y_t = Y_0 for all t. ∎

**Remark (the orbifold reading).** M̄_g is an orbifold (a DM stack). Suppose "smoothly trivial family" in the problem is read in the orbifold category: the trivialization H, restricted to each stratum, is an orbifold isomorphism, so in particular it preserves isotropy groups. Then:
- **(R2^orb)** |Aut(H_t(z))| = |Aut(z)| for every z ∈ B_0 and every t.
- (R2^orb) gives (IP_m) at every point. So under (R2^orb), **the twin obstruction disappears entirely**. MS8 then holds whenever Prop K's endpoint is MERGE or pMOV.
- The only remaining case is the interior-MOV (crossing) endpoint, together with the inherited inputs (K′) and (PT_chain).

Under the coarse reading (R2) adopted by the task, (IP) is an extra hypothesis. Automorphisms of boundary points can disappear for t ≠ 0, and this is exactly the twin mechanism: §4 shows that a failure of (C_m) forces Aut(J_{m,t}) ⊊ Aut(J_m).

## 4. What a failure of (C_m) forces (proved)

Assume Y is non-constant. Put Z := Z_A ∪ Z_φ ∪ D_all, where:
- Z_A is as in Lemma 2;
- Z_φ is the union, over the finitely many pairs (D, c) with D a piece at time 0 and c a constant vertex of D such that [φ_c] ≢ [Y], of the coincidence sets {t : [φ_c(t)] = [Y_t]}. Each is closed and discrete by Lemma 1.
- D_all is the union, over the pieces at time 0 in product-type strata and the vertices non-constant on them, of the closed discrete exceptional sets of R7-2 Lemma 2.1.

Z is a finite union of closed discrete sets, hence closed and discrete. Call t ∈ Δ_ε \ Z *generic*.

**Proposition 3.** Assume (R1), (R2), (Rig), (K′), (PT_chain, extended to D^{m+1}), and that Y is non-constant.
- **(Junction.)** Suppose [φ_{c_m}] ≡ [Y] but [φ_{c_{m+1}}] ≢ [Y] for some m ≤ k−1. Then (C_m) fails; in particular (IP_m) fails, and (NT_m) fails. Moreover, for every generic t there is a ∈ Aut(J_m) with a^{-1}x_m ≠ x_m such that one of the following holds.
  - **(b) persistent twin.** Along β̃^{m+1}_−, the chart vertex a^{-1}x_m is a single intact vertex w of D^{m+1}, constant on D^{m+1}, with [φ_w] ≡ [Y]. So D^{m+1} carries two distinct constant vertices, c_{m+1} and w, both with value ≅ Y_0 at t = 0, and with different value functions.
  - **(c) junction crossing.** J_m ∈ stratum(D^{m+1}), and a^{-1}x_m is an intact vertex of D^{m+1} that is non-constant on D^{m+1}, with value ≅ Y_0 at J_m.
- **(Endpoint.)** Suppose the endpoint is MERGE or pMOV and [φ_{c_k}] ≡ [Y]. Then (C_k) fails. For every generic t there is a ∈ Aut(Q_0) with a^{-1}x ≠ x such that, along β̃^E, a^{-1}x is a single intact vertex w of E, constant on E, with [φ_w] ≡ [Y]. So Q_0 has two Y_0-copies, x and a^{-1}x, exchanged by a ∈ Aut(Q_0). The copy x merges or moves along β̃^E, while its twin stays along β̃^E and carries Y.

*Proof (junction).*
- (C_m) fails, since otherwise Step 1 of Theorem 1 would give [φ_{c_{m+1}}] ≡ [Y].
- Fix a generic t, and pick j̃ ∈ closure(Ñ^m_{+,t}) ∩ π^{-1}(J_{m,t}). By (∗), F_{x_m}(j̃) ≅ Y_t.
- The coarse branch β^{m+1}_− (or the germ of D^{m+1}, in the interior case) is transported to a branch at J_{m,t}. Its preimage near j̃ lies in ⋃_a (aÑ^{m+1}_−)_t and has j̃ in its closure (R7-4 Lemma 2(b); the interior case is identical). Choose a with j̃ ∈ closure((aÑ^{m+1}_−)_t).
- Along aÑ^{m+1}_−, the class of x_m is a·(the class of a^{-1}x_m along Ñ^{m+1}_−), by (K3). The latter class is the vertex w of D^{m+1} containing a^{-1}x_m along β̃^{m+1}_−, because the vertex structure is constant on Ñ.
- *w merged* (contains an unpinched edge). Then J_m ∉ stratum(D^{m+1}). As in Step 2 of Theorem 1, Y_t ≅ F_{x_m}(j̃) is a component of the puncture value of the non-constant vertex w of D^{m+1}_t. So [Y_t] ∈ A, contradicting t ∉ Z_A.
- *w = {a^{-1}x_m} intact and non-constant on D^{m+1}.*
  - If J_m ∉ stratum(D^{m+1}): since t ∉ D_all, w ∈ M(D^{m+1}_t), and its puncture value is ≅ Y_t. So [Y_t] ∈ A, a contradiction.
  - Otherwise we are in (c). The value at J_m is F_{a^{-1}x_m}(0) ≅ F_{x_m}(a·0) = F_{x_m}(0) ≅ Y_0.
- *w = {a^{-1}x_m} intact and constant on D^{m+1}.*
  - By (K3) and (∗), F_{x_m} ≡ φ_w(t) on closure((aÑ^{m+1}_−)_t). So [φ_w(t)] = [Y_t], and since t ∉ Z_φ, [φ_w] ≡ [Y].
  - If a^{-1}x_m = x_m, then w = c_{m+1}, contradicting [φ_{c_{m+1}}] ≢ [Y]. So a^{-1}x_m ≠ x_m.
  - Two distinct chart vertices that are both intact along β̃^{m+1}_− are distinct vertices of G_{D^{m+1}}. So w ≠ c_{m+1}, and both are constant with value ≅ Y_0 at t = 0. This is (b).
- In cases (b) and (c), a moves x_m, so (NT_m) fails. (IP_m) fails by Corollary 1(a). ∎

*Proof (endpoint).* Identical, with E in place of D^{m+1}.
- The cases "w merged" and "w intact, non-constant" give [Y_t] ∈ A, because Q_0 ∉ stratum(E) in the MERGE and pMOV cases, so the limit point is a puncture. This contradicts genericity.
- So w = {a^{-1}x} is intact and constant with [φ_w] ≡ [Y].
- If a^{-1}x = x, then x would be intact and constant along β̃^E, which contradicts MERGE/pMOV. ∎

**Meaning.** A twin jump needs one of two things:
- a whole piece D^{m+1} that carries two constant Y_0-vertices with different deformations ("persistent twins"), which Prop K's track enters on the wrong one;
- or, at the endpoint, a boundary point Q_0 with an automorphism exchanging the merging copy with a staying twin.

In both cases the automorphism group of the junction must drop for t ≠ 0. This is consistent with R7-3 Theorem B, but here it is derived with (Rig) replacing L2. It also locates the extra structure: persistent twins live on a whole piece of the chain, not only at an isolated point.

## 5. Crossings at generic times are "pure" (proved)

**Lemma 4 (pure crossing).** Assume (Rig) and that Y is non-constant. There is a closed discrete set Z′ ⊃ Z_A such that the following holds for t ∉ Z′.
- Let Q ∈ B_t, q̃ a lift, and x a chart vertex with F_x(q̃) ≅ Y_t.
- Let γ̃ be a lifted branch through q̃ of a piece E with Q ∈ stratum(E) and x ∈ M(E) (an IMOV of x).
- Let β̃ be a lifted branch through q̃ of a piece D with Q ∉ stratum(D), along which x is intact and constant.

Then every w ∈ M(E) is, along β̃, a single intact vertex {w} of D that is constant on D. Hence pr_{M(E)} of the point of E over Q is (φ^D_w(t))_{w∈M(E)} ∈ K(E), a point whose coordinates are constant-vertex values of D.

*Proof.*
- Let F′ be the finite set of classes of components (with special points) of elements of F.
- For (G, M, K) ∈ 𝒦 and w ∈ M, pr_w is non-constant on K: otherwise f_w would be constant on every piece with that triple.
- So F″ := ⋃_{(G,M,K), w ∈ M} K ∩ pr_w^{-1}(F′) is finite. Let A″ be the set of classes of all coordinates of points of F″ of type (g_i, n_i). Put Z′ := Z_A ∪ {t : [Y_t] ∈ A″}, which is closed and discrete by Lemma 1.
- Let w ∈ M(E), and let [w] be the vertex of D containing w along β̃.
  - *[w] ∈ M(D).* Then Q is a puncture of D, and F_w(q̃) is a component of f_{[w]}(p_D) ∈ F. So the point κ := pr_{M(E)}(point of E over Q) ∈ K(E) has its w-coordinate in F′, i.e. κ ∈ F″. Its x-coordinate is F_x(q̃) ≅ Y_t, so [Y_t] ∈ A″, contradicting t ∉ Z′.
  - *[w] constant on D.* Its value is smooth and equals the curve glued from the components in [w]. So [w] = {w} is intact. ∎

So at generic t every crossing adjacent to a coarser staying branch is *pure*: the staying branch freezes every moving vertex of the crossing piece. The point of K(E) at the crossing is κ(t) = (φ^D_w(t))_w. It moves holomorphically along the fixed curve K(E), and its x-coordinate is Y_t. Nothing in (R1), (R2), (Rig) excludes this (compare the local model of R7-2 §4.2). Crossings with D in the same stratum as E are not constrained even this much: there κ(t) is an intersection point of the two fixed-type curves K(D) × {φ^D(t)} and K(E) × {φ^E(t)}.

## 6. Why (SC) is hard under plain (R2): the scale conflict (analysis; not a proof)

This section records why I could not prove (SC), so that the next attempt does not repeat it.

1. **Stars are disjoint (proved sketch).** Fix t. For small W, B_t ∩ W = H_t(B_0 ∩ W) is a cone at J_t: a union of arcs from J_t.
   - Each lifted arc starts at a lift of J_t.
   - Two lifted arcs from different lifts of J_t cannot meet. Away from J_t the stabilizer is locally constant along the arc, so lifting backwards from a common point is unique.
   - Hence π^{-1}(B_t ∩ W) is a disjoint union of "stars", one at each lift of J_t. (SC_m) says that the two transported branches lie in a common star.
2. **Fixed t: the time-t network is coherent inside each star.** At generic t, every Y_t-copy at a lift j̃ stays along every branch of the star of j̃, by Lemma 2 and R7-4 Lemma 1. So inside one star there are no twin problems.
3. **The obstruction is a monodromy.** Transport Prop K's interior path γ_ρ (within ρ of B_0) to time t, as H_t∘γ_ρ.
   - For fixed t and ρ → 0, the transported path stays near a single star, because the stars are at positive mutual distance.
   - In a twin jump, the two branches lie in different stars. So the square (s, τ) ↦ H_τ γ_ρ(s), τ ∈ [0, t], cannot lift to the orbifold chart. It must meet the orbifold locus of 𝒱 (curves with automorphisms), and the monodromy of the square moves the star.
   - These orbifold points lie at times τ where the stars at J_τ are closer together than the distance ε(ρ) of the path to B_τ.
4. **The two scales conflict.**
   - Making the transported path resolve the stars needs ρ ≪ (star separation at time t), and the separation tends to 0 as t → 0.
   - Making the square avoid orbifold points needs t ≪ ρ.
   - I found no way to reconcile the two. The defect of the square is a product of local monodromies around the 2-dimensional orbifold locus O ∩ 𝒱. Jumps at generic τ preserve the time-τ network, since automorphisms preserve isomorphism classes. Jumps at τ → 0 are uncontrolled.

So (SC) is a genuinely mixed statement: Prop K's information is at t = 0, while the coherence lives at t ≠ 0. Under (R2^orb) the problem disappears, because there are then no stars to choose between.

## 7. The chain's derivation from MS8

- I find no flaw in "MS8 + entry 69 (Rig) ⇒ the problem's claim": MS8's conclusion is literally the claim, given (Rig).
- Two remarks on the chain.
  - (i) Every known route to MS8, including Theorem 1 here, R7-1 Theorem T and R7-3 Theorem A, uses L1 for the pieces along Prop K's chain. L1 is proved only for product-type strata. R7-5 §1.4 shows that it can fail in the non-product case. So (PT_chain), or a non-product substitute, is an additional open input that is not listed in entry 69. It should be added to the ledger.
  - (ii) MS8 as stated has the hypothesis (Rig) but not Prop K. Any proof along these lines also needs (K′), i.e. Prop K, which is "modulo routine marking details". This is not a flaw, but it is a dependency the ledger should record next to MS8.

## 8. Summary

**Proved (modulo the cited inputs (K′), L1 for product type, R7-2 Lemma 2.1, R7-4 Lemma 2, and the standard facts (K1)–(K4)):**
1. Lemma 2: under (Rig), all puncture values of non-constant vertices lie in a t-independent finite set F. If Y is non-constant, [Y_t] ∈ A only on a closed discrete set.
2. **Theorem 1:** MS8 holds when Prop K's endpoint is MERGE or puncture-MOV, the chain is of product type, and at every junction and at the endpoint either (NT) or the star-coherence condition (SC) holds.
3. **Corollaries 1 and 2:** (SC) holds at a point whose automorphism group does not drop under the deformation (IP), or at which one of the two lifted branches is Aut-invariant. Under the orbifold reading (R2^orb) of "smoothly trivial", (IP) holds everywhere. MS8 then holds except at a crossing endpoint.
4. **Proposition 3:** if Y is non-constant and the conclusion fails at a junction, then (IP) and (NT) fail there, and either (b) the next piece of the chain carries two distinct constant Y_0-vertices with different deformations (persistent twins), or (c) a crossing occurs at the junction. At an endpoint of type MERGE or pMOV, failure forces a twin of the merging copy, exchanged by an automorphism of Q_0, which stays along the merge branch.
5. **Lemma 4:** at generic t, every crossing adjacent to a coarser staying branch is pure: all moving vertices of the crossing piece are frozen along the staying branch.

**Not proved:**
- MS8 itself.
- (SC) under plain (R2).
- Exclusion of crossing endpoints.
- §6 is analysis only.

**Open questions (named):**
- **(O1) Twin coherence.** For a smooth closed totally geodesic V_0 and an admissible family under plain (R2): does (SC) hold at the points of Prop K's chain? Equivalently, can the persistent-twin configuration (b), or the endpoint twin of Proposition 3, actually occur?
- **(O2) Crossing endpoint.** Can Prop K's endpoint be an interior-MOV, i.e. a pure crossing in the sense of Lemma 4? This is open even under (R2^orb).
- **(O3) Inherited inputs.** (K′) (Prop K's marking details), L1 for non-product strata ((PT_chain)), and (Rig) itself (entry 69).

=== END OF ANSWER round8_q8 ===
