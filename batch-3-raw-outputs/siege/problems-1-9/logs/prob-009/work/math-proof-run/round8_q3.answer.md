STATUS: PARTIAL. MS8 is neither proved nor refuted here. What is new and proved:
- **Theorem N.** A twin-free reformulation. Assume (R1), (R2), (Rig) and that Y is non-constant. Then at every time t outside a countable set, a Y_t-copy can leave the "Y-network" only through an interior crossing (IMOV). It can never leave by a merge or by a puncture-move, and in this statement twins play no role at all.
- **Corollary T.** A twin criterion proved under (Rig) alone, with no (O) and no Lock. It contains the quintic mechanism.
- **Lemma X.** The rigid structure that an IMOV exit must have at a generic time (a "pure crossing").

What stays open is stated precisely in §5. The twin problem has not disappeared: it reappears when one passes from generic t back to t = 0, and only there (§5.2).

---

## 0. Setting and conventions

The setting is MS8 exactly as in the task: (R1), (R2) with H_0 = id; V_0 is smooth, closed, 2-dimensional and totally geodesic; Δ_Γ is of product type; ∂V_t has dimension 1; π_i(∂V_t) = {Y_t}; and (Rig) holds.

Notation:
- B_t := closure(V_t) \ V_t = closure(V_t) ∩ ∂M̄_g. This is compact, since V_t is closed in M_g. By (R2), B_t = H_t(B_0), and H_t preserves strata.
- A *coarse piece* (at time 0) is a 1-dimensional irreducible component D of B_0 ∩ Δ_G, for some stable graph G. There are finitely many. We write D_t := H_t(D).
- For Q ∈ B_t, Def(Q) is the versal deformation germ, with smoothing parameters s_e and Aut(Q) acting. Points of the locus {s_e = 0 for all e} have components comp_x labelled by x ∈ V(G_Q). A lifted branch b̃ has a constant *pattern* S_b̃ = {e : s_e ≡ 0 on b̃}.
- A label y is *intact* along b̃ if every edge at y lies in S_b̃, and *merged* otherwise.
- [Z] denotes the class of an n_i-pointed curve in M_{g_i,n_i}/S_{n_i}. A *Y_t-copy* is a component Z with [Z] = [Y_t].
- By PR-A (re-checked; it uses only (R1), (R2)), t ↦ Y_t is holomorphic, so t ↦ [Y_t] is holomorphic.

**Standard fact used (cited from memory: partial normalization of a nodal family along node sections).** For S ⊂ E(G_Q), let G_S be G_Q with the edges not in S contracted. Then there is a holomorphic map Π_S : {s_e = 0 for all e ∈ S} → ∏_{w∈V(G_S)} M̄_w with the following properties.
- It is obtained by normalizing the nodes in S of the fibre curves.
- On the locus where exactly the edges of S vanish, it takes values in ∏ M_w and ξ_{G_S}∘Π_S equals the quotient map.
- At 0, the w-coordinate is the curve glued from the comp_x(0), x ∈ w, along the edges outside S that join them. Its marked points are the half-edges of S-edges at w.

**Finite sets supplied by (Rig).**
- F := ⋃_{(G,M,K)∈𝒦} K ∩ ∂(∏_{u∈M} M̄_u). This set is finite, because each K is an irreducible curve not contained in the boundary.
- F′ := the set of isomorphism classes, as pointed curves with unordered special points, of all smooth components of all coordinates of elements of F. It is finite.
- **Fact (P), the puncture lemma from chain step 3, re-checked.** Let p be a puncture of a piece E at any time. Then pr_{M(E)}ν(p) ∈ F. Indeed, constant vertices take their value in M_w, so some coordinate in M(E) lies in the boundary. Hence pr_{M(E)}ν(p) ∈ K(E) ∩ ∂, which is a subset of F.

---

## 1. Lemma 1 (the Y-locus is analytic)

Put Ŷ := {(Q,t) ∈ M̄_g × Δ : Q has a Y_t-copy}. Then Ŷ is a closed analytic subset of M̄_g × Δ.

*Proof.*
1. Fix a stable graph G of genus g and a vertex v of type (g_i,n_i). Put A_{G,v} := {(z,t) ∈ ∏_w M̄_w × Δ : [z_v] = [Y_t]}. This is the preimage of the graph of the holomorphic map t ↦ [Y_t] under the holomorphic map (z,t) ↦ ([z_v], t). Hence it is closed analytic.
2. The map ξ̄_G × id is finite, hence proper. By Remmert's proper mapping theorem, (ξ̄_G × id)(A_{G,v}) is closed analytic.
3. Ŷ is the finite union of these images over all pairs (G, v).
   - ⊆: let Q be a curve with a Y_t-copy at the vertex v of its own dual graph. Take z = (normalized components) ∈ ∏ M_w.
   - ⊇: let (z,t) ∈ A_{G,v}. Since z_v ≅ Y_t is smooth, ξ̄_G(z) has the irreducible component z_v. Its special points are exactly the n_v half-edges of v, and nodes inside the other z_w do not affect it. So z_v is a Y_t-copy of ξ̄_G(z). ∎

Put 𝓑 := closure(𝒱) ∩ (∂M̄_g × Δ). It is analytic by (R1), and 𝓑 = H(B_0 × Δ) by (R2). Put 𝓝 := Ŷ ∩ 𝓑, which is closed analytic. Its fibre is 𝓝_t = N_t := {Q ∈ B_t : Q has a Y_t-copy}.

---

## 2. Lemma 2 (dichotomy for coarse pieces)

Let D be a coarse piece. Exactly one of the following holds.
- (N) For every t, every point of H_t(closure D) has a Y_t-copy.
- (F) There is a countable set Z_D ⊂ Δ such that for t ∉ Z_D only finitely many points of H_t(closure D) have a Y_t-copy.

*Proof.*
1. **B_0 is pure 1-dimensional.**
   - Locally in Def(Q), every irreducible component X of the preimage of closure(V_0) is 2-dimensional and contains points of V_0. (At a point of X lying on no other component, nearby points of V_0 must lie on X.)
   - So ∏ s_e is not identically 0 on X, and X ∩ {∏ s_e = 0} has pure dimension 1 (Krull).
   - Also dim B_0 ≤ 1, since V_0 is dense in closure(V_0).
2. **The set D°.** Let D° be D minus the finitely many singular points of the compact curve B_0. Then D° is connected, being an irreducible curve minus a finite set. It is also open in B_0, since near a smooth point of B_0 lying on D, B_0 coincides with D.
3. **The set M_D.** M_D := H(D° × Δ) is open in 𝓑 and is a connected topological 4-manifold. Hence 𝓑 has pure dimension 2 along M_D.
   - Sing(𝓑) ∩ M_D is a closed subset of covering dimension ≤ 2. It does not disconnect the connected 4-manifold M_D (a closed set of dimension ≤ n−2 does not separate a connected n-manifold; Hurewicz–Wallman, cited from memory).
   - So M_D ∩ Reg(𝓑) is connected. It therefore lies in the regular part of a single irreducible component W of 𝓑, and M_D ⊂ W.
4. **Case W ⊂ 𝓝.** Then M_D ⊂ 𝓝. Since 𝓝 is closed and H_t(closure D) = closure(H_t(D°)), this is (N).
5. **Otherwise.** W ∩ 𝓝 is a proper analytic subset of the irreducible 2-dimensional W, so its dimension is ≤ 1.
   - Its irreducible components form a locally finite, hence countable, family. Let Z_D be the countable set of t such that some component lies in the fibre over t.
   - For t ∉ Z_D, the fibre (W ∩ 𝓝)_t is discrete. It is also compact, being closed in the compact 𝓑_t. So it is finite.
   - It contains N_t ∩ H_t(D°). Adding the finitely many points of H_t(closure D \ D°) gives (F).
6. **(N) and (F) exclude each other.** H_t(closure D) is infinite. ∎

Define:
- 𝒩 := {D : (N) holds}, and C_t := ⋃_{D∈𝒩} H_t(closure D).
- Every component of ∂V_0 lies in 𝒩, since vertex i ≡ Y_t on ∂V_t. Hence closure(∂V_t) ⊂ C_t.

**Remark 2.1.** Let D ∈ 𝒩 and let E be any piece at time t over D_t. Then some vertex w of E has f_w ≡ Y_t, a constant on E. Indeed, E is the union of the finitely many analytic sets {f_w ≅ Y_t}, so one of them is all of E.

Note: 𝒩 and C_t are defined without choosing or tracking any copy. Twins play no role in them.

---

## 3. Theorem N (how a copy can leave the network at a generic time)

Assume Y is non-constant. Define:
- Z_1 := ⋃_{D∉𝒩} Z_D, which is countable;
- Z_2 := {t : [Y_t] ∈ F′}, which is discrete, since [Y] is holomorphic and non-constant;
- Z := Z_1 ∪ Z_2. Call t ∉ Z *generic*.

**Theorem N.** Let t be generic. Let Q ∈ B_t with lift 0 ∈ Def(Q), let y be a label with comp_y(0) ≅ Y_t, and let b be any branch of B_t at Q, with a lift b̃ through 0 of pattern S. Then y is intact along b̃, and exactly one of the following holds.
- (STAY) comp_y ≡ Y_t along b̃. Then the coarse piece D′ with b \ {Q} ⊂ D′_t lies in 𝒩, so b ⊂ C_t.
- (IMOV) S = E(G_Q), so Q is an interior point of the piece of b, which lies in the stratum of Q. Moreover comp_y is non-constant along b̃.

Moreover N_t \ C_t is finite.

*Proof.*
1. **Setting up the piece.** Let G_b := G_S. Π_S(b̃ \ 0) is a 1-dimensional germ in ξ_{G_b}^{-1}(closure(V_t) ∩ Δ_{G_b}). So it lies in a piece E at time t, and Π_S(0) = ν(p) for a point p ∈ Ē. Let u be the vertex of G_b containing y.
2. **Merge is impossible.** Suppose an edge at y is not in S.
   - f_u(p) is the curve glued from the comp_x(0), x ∈ u. It has a node, so f_u(p) ∈ ∂M̄_u.
   - Hence p is a puncture. Also u ∈ M(E): a constant f_u would take its value in M_u (Lemma C2 of PR-C).
   - comp_y(0), with all its special points (the nodes inside u and the legs from S-edges), is a component of f_u(p).
   - By Fact (P), f_u(p) is a coordinate of an element of F. So [Y_t] ∈ F′, which contradicts t ∉ Z_2.
3. **Puncture-move is impossible.** Suppose y is intact, S ≠ E(G_Q), and comp_y is non-constant along b̃.
   - Then u = {y}, and f_u = comp_y along Π_S(b̃) is non-constant, so u ∈ M(E).
   - Some edge outside S is contracted into a vertex w, so f_w(p) is nodal and p is a puncture.
   - By (P), f_u(p) = comp_y(0) ∈ F′. This again contradicts t ∉ Z_2.
4. **The remaining cases.** y is intact. If comp_y is constant along b̃, every point of b has a Y_t-copy. So N_t ∩ D′_t is infinite, and since t ∉ Z_{D′}, Lemma 2 gives D′ ∈ 𝒩. Otherwise we are in (IMOV).
5. **Finiteness.** N_t \ C_t is finite by Lemma 2 (F) and t ∉ Z_1. ∎

**Corollary N1.** Let Y be non-constant and t generic. Suppose that no point of C_t carries an IMOV copy. Then:
- C_t is open and closed in B_t, so it contains the connected component B_t^∂ of B_t that contains ∂V_t;
- every Y_t-copy at every point of B_t^∂ is intact and constant along every branch of B_t there.

*Proof.* At Q ∈ C_t, every branch is STAY for the Y_t-copy that Q carries, so it lies in C_t. Hence C_t is open in B_t, and it is closed as a finite union of compact sets. ∎

---

## 4. Consequences

### 4.1 Corollary T (twin criterion under (Rig); no (O), no Lock, no restriction on automorphisms)

Let J ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G′}. Let 𝒞 and j(S) be as in PR-I Theorem 4. Assume:
- (Tw1) there is a neighbourhood U of J with B_0 ∩ U ⊂ ∂V_0 ∪ {J};
- (Mg) for all S ≠ S′ in 𝒞, some edge at j(S) is not in S′.

Then MS8 holds: Y_t = Y_0 for all t.

*Proof.*
1. Suppose Y is non-constant and take t generic. Put J_t := H_t(J) ∈ closure(∂V_t), and let q be a lift of J_t.
2. A branch of ∂V_t at J_t lifts to a branch β̃ through q, with pattern S ∈ 𝒞. By Lemma D(1) of PR-I, y := j(S) is intact and comp_y(q) ≅ Y_t.
3. J_t ∉ Δ_Γ, so there is an edge e ∉ S. Let X be an irreducible component, at q, of the preimage of closure(V_t) containing β̃.
   - s_e is not identically 0 on X, since it is nonzero on β̃ \ q.
   - So X ∩ {s_e = 0} is pure 1-dimensional through q (Krull). It contains a branch b̃ ≠ β̃ with e ∈ S_b̃.
4. By (Tw1), transported by H_t, b̃ lies over ∂V_t. So S′ := S_b̃ ∈ 𝒞, and S′ ≠ S because e ∈ S′ \ S.
5. By (Mg), y is merged along b̃. This contradicts Theorem N. ∎

**Remarks.**
- This is PR-I Proposition 3 / Theorem 4 with (O), (Tw2)(iii) and all Teichmüller-curve input replaced by (Rig).
- It holds whether or not Aut(J) swaps the twins. Theorem N concerns every copy at the same lift q, so the identity of "the" tracked copy never enters.
- In the quintic example, 𝒞 = {{e_1},{e_2}}, j({e_1}) = A has e_1 ∉ {e_2}, and symmetrically. So (Mg) holds.

### 4.2 Lemma X (an IMOV exit at a generic time is a pure crossing)

Put Z_3 := the set of t such that [Y_t] lies in the following finite, t-independent set F″:
- take (G,M,K) ∈ 𝒦, u ∈ M and a ∈ F′;
- take the points k ∈ K whose u-coordinate is a relabelling of a (finitely many, because pr_u|_K is non-constant on the irreducible curve K);
- F″ consists of the classes of the components of type (g_i,n_i) of the coordinates of all such k.

Z_3 is discrete when Y is non-constant.

**Lemma X.** Let t ∉ Z ∪ Z_3. Suppose (IMOV) occurs at Q ∈ B_t, with lift 0, copy y, branch b, piece E′ ∋ e_0 (where ξ(e_0) = Q), and x the vertex of E′ at y, so x ∈ M(E′) and f_x(e_0) ≅ Y_t. Let c be any boundary branch of B_t at Q, with lift c̃ through 0. Then every label ℓ corresponding to a vertex of M(E′) is intact and constant along c̃.

*Proof.*
1. Suppose some such ℓ ↔ u ∈ M(E′) were merged along c̃, or intact and moving along c̃ (c̃ is a boundary branch). Steps 2–3 of Theorem N show that comp_ℓ(0) = f_u(e_0) ∈ F′, up to relabelling.
2. Then pr_{M(E′)}(e_0) ∈ K(E′) has its u-coordinate in a finite set. So its x-coordinate Y_t lies in F″, which contradicts t ∉ Z_3. ∎

So at an IMOV exit lying on a boundary branch c (for example a puncture of a STAY piece D ∈ 𝒩), every moving vertex of E′ is a constant vertex of the piece of c. Along t ↦ H_t(Q_0), the M(E′)-coordinates are then values φ_c(t) of constant vertices, which are holomorphic in t by R7-3 Lemma 1(a) in the product case. Hence the holomorphic curve t ↦ (φ_{c(w)}(t))_{w∈M(E′)} runs inside the fixed curve K(E′), and its x-coordinate is Y_t.
- This is the "pure crossing" of the planner's sketch, here derived rigorously at generic t.
- It does not contradict anything at time t: it says that the crossing point slides along K as t varies.

---

## 5. What remains open, and why

### 5.1 The residual statement

Theorem N reduces MS8 to excluding the following configuration for generic t (necessarily for all t in Δ minus a countable set):

> (★) Y is non-constant, and at time t every Y_t-copy at every point of C_t is intact along every branch, and is either constant along it (STAY) or IMOV.

By Corollary N1, without IMOV this means that B_t^∂ is entirely STAY-covered by Y_t-copies. At a single time t, (★) is locally consistent: see the crossing model of R7-2 §4.2 and the non-merge model of PR-C. So the contradiction has to come from t = 0, where total geodesy is available.

### 5.2 Passing to t = 0 (where the twin problem reappears)

Let t_n → 0 be generic, with lifts q_n → 0 of J_{t_n} = H_{t_n}(J). After passing to a subsequence, the copy sets Λ_{t_n}(q_n) equal a fixed nonempty Λ′(J) ⊂ Λ(J). By the limiting argument of R7-1 Step 3 / Step 3′:
- for each branch b at J there is a lift b̃′ = a_b b̃ (a limit of transported lifts through q_n);
- along b̃′, every y ∈ Λ′(J) is intact and comp_y ≡ Y_0, unless the IMOV case applies;
- the labels of b's 𝒴-vertices (constant vertices with φ ≡ Y) along b̃′ lie in Λ′(J).

Call such data a *Y-system*. Proposition K supplies a path-marked track whose tracked copy x ends in MERGE or MOV. To conclude, one needs **track coherence**: at each junction, the lift of the outgoing branch induced by the marking agrees with a_b modulo the stabilizer of the tracked label. Then x ∈ Λ′ throughout, and the MERGE/puncture-MOV endpoint contradicts Theorem N.

Track coherence is exactly the twin problem, and it is not proved. A Y-system alone gives no contradiction at t = 0. In the quintic example with a swap automorphism, the t = 0 data admit Λ′ = {A}; the contradiction there comes from the time-t Krull pair through the same lift q (Corollary T), not from t = 0 data.

### 5.3 Crossings

By Lemma X, an IMOV exit at a generic time forces, at t = 0, a pure crossing Q_0. There, the moving vertices of a deep piece E′ through Q_0 are intact and constant along every boundary branch at Q_0, and the time-curve of their values traces K(E′). Excluding this for a smooth totally geodesic V_0 would need genuine Teichmüller geometry near the corner (a Lemma PA-type analysis in mixed directions). I tried the obvious rescaling: the limit is a product of Teichmüller spaces with the sup metric, which does contain isometric bidiscs, so rescaling alone gives no contradiction. Not done.

### 5.4 The chain

I re-checked chain steps 1 and 3 (consequence (P)) and found no flaw. One remark on step 3: (P) uses that constant vertices take values in M_w, which holds because pieces lie in ∏ M_w. Theorem N uses (Rig) only through the finite set F and, in Lemma X, through K(E′) being a curve.

---

## 6. Summary

**Proved (modulo the cited standard facts: Remmert, Krull, partial normalization of nodal families, non-separation by codimension-2 sets, PR-A, Lemma D(1) of PR-I, Lemma C2 of PR-C):**
- Lemma 1: the Y-locus is analytic.
- Lemma 2: the dichotomy (N)/(F) for coarse pieces; the twin-free network 𝒩.
- Theorem N: at generic t, no Y_t-copy anywhere in B_t merges or puncture-moves; every exit from C_t is IMOV; N_t \ C_t is finite.
- Corollary N1.
- Corollary T: MS8 under (Tw1) + (Mg), for any automorphism group. This is a genuine but partial case.
- Lemma X: the pure-crossing structure of IMOV exits at generic t.

**Not proved:** MS8 itself.

**Open:**
1. Track coherence at twin junctions, i.e. the passage from Theorem N at generic t to a contradiction with Proposition K's track at t = 0 (§5.2).
2. Excluding pure crossings (Lemma X configurations) for smooth totally geodesic V_0 (§5.3).
3. Whether a configuration satisfying (★) for all generic t can come from a totally geodesic V_0. No counterexample was found or constructed.

=== END OF ANSWER round8_q3 ===
