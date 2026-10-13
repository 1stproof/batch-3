kind: attempt
Open question attempted: the twin step inside the run's missing statement MS8 (ledger entry 68). It is posed as the self-contained claim (TW*) below. The specific target is star coherence (SC) of R8-8 at the points of Proposition K's chain, without the extra hypotheses (IP), (U_J) or (NB).

## Task
Prove (TW*) below in full, or exhibit a configuration showing that it fails, with every check written out.

**Named approach for this query: the track's lifted 3-fold component and its stabiliser.** You may depart from it if you say why. It differs from the fixed-locus case analysis of R8-5 Prop. D. The planner's outline, every step to be checked or repaired:

1. At a junction J (likewise at the endpoint), define:
   - Def(J) with the action of Aut(J);
   - 𝒞° = the connected component of the preimage of 𝒱 ∩ (U × Δ_ε) in Def(J) × Δ_ε that contains the lifted track (R8-5 (C3));
   - 𝒳 := closure(𝒞°), an irreducible 3-dimensional analytic germ at (0,0);
   - Γ := Stab_{Aut(J)}(𝒞°).
   By R8-5 Fact 0, 𝒞° → 𝒜 := 𝒞°/Γ is the quotient map onto a connected component 𝒜 of 𝒱 ∩ (U × Δ_ε). Then the lifts of J_t := H_t(J) lying in 𝒳_t should form exactly ONE Γ-orbit (closure of the quotient). Prove this.
2. By (TD_J) (R8-5 §1), the lifted track comes within ρ of generic points of the two specific lifted branches β̃ (of D^m) and β̃′ (of D^{m+1}) at 0. Hence both lie in 𝒳_0, and their transport families Ñ, Ñ′ (R8-8 §0, R7-4 Lemma 2) lie in 𝒳. Prove this, using (R2) near generic points of the branches and connectedness of Ñ.
3. Each closure(Ñ_t), closure(Ñ′_t) contains a lift of J_t, which then lies in 𝒳_t. So (SC) at J holds as soon as, for t in a set accumulating in Δ, the Γ-orbit of a lift q_t of J_t is a single point, i.e. Γ ⊂ Stab(q_t) = Aut(J_t) ∩ Γ. It also holds whenever the two families pass through a common point of the orbit.
4. The remaining case: Γ ⊄ Aut(J_t), so automorphisms in Γ "drop" at time t. Then work at the level of 𝒳 rather than the 2-dimensional germs:
   - Show that the two families pass through a common lift. Possible tools:
     - Krull/Hurwitz arguments inside the irreducible 3-fold 𝒳 and its boundary divisors 𝒳 ∩ {s_e = 0};
     - the generic-time trichotomy at every lift q_t (R8-2 Theorem 1; R8-3 Corollary T applies at a single lift whatever the automorphisms);
     - the fact that Prop K's track at t = 0 enters and leaves J within ONE lifted sheet of closure(V_0) (the "same-sheet" property: V_0 is smooth, so near J the sheets are the closures of the components of V_0 ∩ U);
     - Lemma U.
   - Or show that a Γ-orbit with several points forces the twins to stay isomorphic (Lock), since elements of Γ act on 𝒳 and permute both the lifts of J_t and the labels.
   - Or show that dropping automorphisms of Γ at J_t (but not at J) is incompatible with (R2) and with the irreducibility of 𝒳 near (0,0).
5. Do the same at the endpoint Q_0, to obtain (b) of (TW*).

## The claim (TW*) to prove or refute

**Setting.** That of MS8 (below), with (Rig). Assume, for contradiction, that t ↦ Y_t is non-constant. Take Proposition K's chain from ∂V_0 (PR-H §3; chart forms (K′) in R8-8 §0, (TD_J) and (TD_Q) in R8-5 §1, §5):
- points P ∈ ∂V_0, junctions J_1, …, J_{k−1}, and an endpoint Q_0;
- pieces D^1, …, D^k, with D^1 ⊂ ∂V_0;
- constant vertices c_m of D^m with value ≅ Y_0, where c_1 = i;
- tracked chart vertices x_m at the junctions and x at the endpoint;
- a terminal branch b at Q_0 of type MERGE or puncture-MOV. (Interior-MOV endpoints and junction crossings are a separate task; you may assume none occur.)

**Claim (TW*).**
- (a) For every m, the value function satisfies [φ_{c_m}] ≡ [Y] on Δ. That is, there is no twin jump at any junction.
- (b) For all t in a set accumulating in Δ, some lift of Q_t := H_t(Q_0) carries a Y_t-copy that is merged along, or intact and non-constant at a puncture along, a lifted branch of H_t(b) through that lift.

(b) contradicts the generic-time trichotomy (R8-2 Theorem 1), so (TW*) proves MS8 in the case where the chain has no crossings.

**What is known.**
- (TW*) holds under any of: (U_J)/(Lock) (R8-5 Theorems A, B); (SC)/(NT)/(IP) (R8-8 Theorem 1, Corollaries 1–2); (NB)+(NB_∂) (R8-2 Theorem S).
- A failure needs the configurations of R8-5 Prop. D, (A), (B) or (C), and of R8-8 Prop. 3: a persistent twin on the next piece, or an endpoint twin exchanged by α ∈ Aut(Q_0) that STAYs along b.
- Proofs under (U_J), (SC), (NB), (IP), (Lock) or "no twins" are already known and do NOT answer the question.
- A proof for only some V_0 does not answer it either, though report it if it is all you find.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties:
  - it is smooth on V_0 × Δ;
  - it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G, including the open stratum M_g.
  - Write H_t = H(·,t); one may assume H_0 = id.
  - This is our formalisation of "smoothly trivial" together with (i) and (ii). It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- Notation:
  - B_t := closure(V_t) \ V_t.
  - A "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.

## The missing statement MS8 and its chain (for context)

**Definitions used below** (unchanged from round 8).
- A *piece at time t* is a 1-dimensional irreducible component E of ξ_G^{-1}(closure(V_t) ∩ Δ_G) ⊂ ∏_{w∈V(G)} M_w, for some stable graph G (any G).
- ν: Ē → ∏M̄_w is the normalization of its closure.
- A *puncture* is a point p ∈ Ē with ν(p) ∉ ∏M_w. Put f_u = pr_u∘ν.
- M(E) := {u : f_u non-constant}.
- K(E) := the closure of the image of E in ∏_{u∈M(E)} M̄_u.

**Chain.**
1. Entry 19: t ↦ Y_t is holomorphic. So if Y_t lies in a finite (or countable) set for t in a set accumulating in Δ, then Y ≡ Y_0.
2. Entry 70 (Theorem TV, with (F2) now proved) together with entry 45 (Lemma PA): every piece at time 0, in every stratum, has a Teichmüller vertex. Its π_j∘ν is a proper orbifold covering of a Teichmüller curve whose lift is the Teichmüller disc.
3. Entry 56 (L2 under (O_G), product strata), the L2′ sketch (non-product strata), entry 54 (L1′) and entry 71 (Lemma U) give **(Rig)**:
   - there is a finite set 𝒦 of triples (G, M, K), up to Aut(G), with M ⊂ V(G) and K an irreducible closed curve in ∏_{u∈M} M̄_u not contained in its boundary;
   - every piece E at every time t has (G, M(E), K(E)) ∈ 𝒦.
   - This is entry 82 (OPEN; replaces entry 69). It still needs (O_G) for every piece and L2′. By round8_q9 (Examples Z, Z′), it cannot follow from piece-level data alone; it needs global input.
   - Consequence: all puncture values of non-constant vertices lie in a t-independent finite set F.
4. **MS8** (entry 68, wording unchanged): (Rig) ⇒ Y_t = Y_0 for all t.

Steps 1–4 give the goal from MS8 together with entry 82.
- MS8 is the strongest intermediate claim the main line needs next. After MS8, only entry 82 remains.
- MS8 is quantified over all admissible V_0 and families; it is not a sub-class.
- Inside MS8, entry 72 (R8-2 Theorem 1) already settles the generic-time analysis. What MS8 still needs is to connect the t = 0 track of Prop K (entry 50) to generic t across twins and crossings.

**Missing statement (MS8)** (unchanged; OPEN entry 68, locator round8_plan).
- *Setting.* g ≥ 2. V_0 ⊂ M_g is a smooth closed 2-dimensional subvariety, totally geodesic for the Teichmüller metric.
  - V_t (t ∈ Δ) is a holomorphic family deforming V_0 as in the problem, satisfying (i), (ii) in the readings (R1), (R2), with H_0 = id.
  - Δ_Γ ≅ ∏_j M_{g_j,n_j} is of product type. ∂V_t := closure(V_t) ∩ Δ_Γ has dimension 1, and π_i(∂V_t) = {Y_t} for all t, for a fixed i with dim M_{g_i,n_i} > 0.
  - V_t is not assumed totally geodesic for t ≠ 0.
- *Hypothesis (Rig)*, as in chain step 3: there is a finite set 𝒦 of triples (G, M, K), M ⊂ V(G), K ⊂ ∏_{u∈M} M̄_u an irreducible closed curve not contained in the boundary, such that for every t ∈ Δ and every piece E at time t, (G, M(E), K(E)) ∈ 𝒦 up to the action of Aut(G).
- *Conclusion.* Y_t = Y_0 for all t ∈ Δ.

## Prior results (verbatim from earlier answer files; re-check what you use)
Labels:
- PR-H = Lemma PA / Proposition K file.
- PR-I = the quintic/Krull file. Its §2, the quintic example, is not reproduced: the surface of cyclic quintic covers in M_6, which is totally geodesic but NOT smooth, with twin copies A, C of Y_0 at its cusp exchanged by an automorphism.
- PR-C = Lemma C1/C2.
- PR-A = holomorphy of t ↦ Y_t.
- "PR-D Lemma R0" = the lifted family of a piece, an irreducible 2-dimensional analytic set proper over Δ.
- R7-k = round-7 files.
- R8-k = round8_qk.
- R7-6 is the round-7 "continuity principle", not reproduced (it has a gap); its chart readings (K*), (Ch), (Tr), Sp are restated in full as (TD_J), (TD_Q) in R8-5.
- (O) is an orbifold-transport hypothesis not needed here.

## 3. Proposition K: Y_0 merges or moves somewhere on its own boundary network (proved, modulo routine marking details)

Notation:
- B := closure(V_0) \ V_0. This is a compact 1-dimensional analytic set; work on a level cover if needed.
- Σ_i ⊂ S_g is the subsurface of vertex i, and ∂Σ_i = {γ_e : e ∈ Γ_i}. Both are path-marked.
- ψ(X) ∈ M̄_{g_i,n_i} is the "Σ_i-part" of X. Fix a pants decomposition of Σ_i. ψ(X) is the surface with the Fenchel–Nielsen coordinates of X inside Σ_i and boundary lengths set to 0. It is continuous on augmented Teichmüller space near points where ∂Σ_i is pinched, and there it equals the stable curve on the Σ_i-side.
- d is a metric on M̄_{g_i,n_i}.

**Cited facts (from memory).**
- Kerckhoff: Ext_Y(γ) ≤ e^{2 d_T(X,Y)} Ext_X(γ).
- Maskit's comparison (Ext) of PR-F.
- Lemma G / G′ of PR-F: limits of g_{s_n}X_n with s_n → s* < ∞ lie in ∂V_0. Each such limit equals φ(g_{s*}), up to a subsequence of the φ's.

For δ, η > 0 let T_n = T_n(δ,η) be the first s ≥ 0 at which max_{e∈Γ_i} Ext_{g_sX_n}(γ_e) = δ or d(ψ(g_sX_n), Y_0) = η.

**Step 1 (T_n is finite and tends to ∞).** By Lemma NH(2), Ext(γ_{e_0}) → ∞ along the ray, so T_n < ∞. For s in a compact set, g_sX_n converges to points of ∂V_0, uniformly in s (Lemma G′). At those points ∂Σ_i is pinched and ψ = Y_0, because vertex i of every point of ∂V_0 is Y_0. Hence T_n → ∞.

**Step 2 (the continuum).** Let K = K(δ,η) be a Hausdorff limit (subsequence) of the compact connected sets {g_sX_n : 0 ≤ s ≤ T_n}. Then K is compact and connected, and it contains P. Every point of K is a limit of g_{s_n}X_n with s_n ≤ T_n:
- if s_n stays bounded, the limit lies in ∂V_0 ⊂ B;
- if s_n → ∞, the curve c is pinched by Lemma NH(1), so the limit lies in B.

So K ⊂ B. On K, every ∂Σ_i curve has Ext ≤ δ (in the limit sense along the approximating sequences) and d(ψ, Y_0) ≤ η. Let Q = Q(δ,η) ∈ K be a limit of the endpoints g_{T_n}X_n. Then Q ∈ B, and either
- (a) some γ_e, e ∈ Γ_i, has Ext = δ > 0 at Q, so it is unpinched at Q; or
- (b) d(ψ(Q), Y_0) = η.

**Step 3 (δ_k, η_k → 0).** Pass to a subsequence with K(δ_k,η_k) → K_0 and Q_k := Q(δ_k,η_k) → Q_0. Then K_0 ⊂ B is compact and connected, and contains P and Q_0. At every point of K_0 the curves ∂Σ_i are pinched (Ext ≤ δ_k → 0 along approximating sequences) and the Σ_i-side is the single smooth component Y_0. So vertex "i" is intact, ≅ Y_0, at every point of K_0, consistently with the path marking.

**Proposition K.** There are a compact connected set K_0 ⊂ B containing ∂V_0's point P, along which the Σ_i-component is intact and equal to Y_0, a point Q_0 ∈ K_0, and a 1-dimensional branch b of B at Q_0 such that one of the following holds:
- **(MERGE)** along b \ {Q_0} some curve of ∂Σ_i is unpinched, i.e. the Y_0-component of Q_0 is merged with other components along b (the merge property of PR-C, at Q_0);
- **(MOV)** along b all of ∂Σ_i stays pinched, but the Σ_i-component is non-constant along b, with limit Y_0 at Q_0.

*Proof.*
- In case (a) for infinitely many k, Q_k ≠ Q_0, because γ_e is pinched at Q_0 and unpinched at Q_k. Put Q̃_k → Q̃_0 in augmented Teichmüller space by choosing lifts and applying mapping classes, so that the path markings converge; this is possible since M̄_g is the quotient of augmented Teichmüller space.
- Near Q_0, B is a finite union of branches, each of which minus Q_0 lies in one stratum. Infinitely many Q_k lie on one branch b, and γ_e is unpinched on b \ {Q_0}: (MERGE).
- In case (b) for infinitely many k: if some ∂Σ_i curve is unpinched at infinitely many Q_k, argue as before to get (MERGE).
- Otherwise ∂Σ_i is pinched at the Q_k, so the Σ_i-side of Q_k is a union of components with ψ(Q_k) at distance η_k > 0 from Y_0 = ψ(Q_0). Again Q_k ≠ Q_0, and the Q_k lie on one branch b, along which ψ is non-constant: (MOV). ∎

**What Proposition K does not give.**
- Q_0 need not lie in closure(∂V_0). K_0 can leave closure(∂V_0) through "STAY" branches: branches of B at points of closure(∂V_0) along which the Y_0-vertex stays intact and constant, but which are not contained in closure(∂V_0).
- The ρ-variant settles nothing. Add the stopping condition "g_sX_n leaves the ρ-neighbourhood of closure(∂V_0)", with η ≪ ρ. That variant shows: **at some point Q ∈ closure(∂V_0) there is a branch of B, not contained in closure(∂V_0), of type MERGE, MOV or STAY.** This is only Lemma C1 of PR-C with the extra edge located; it does not exclude STAY.
- Heuristic for why STAY should really occur, from the multi-scale picture, not proved. Suppose the zero-area part of the limit at P has two levels below the top: a vertex w at level −1 and the vertex i at level −2, attached below w. Along the ray, lower levels are "released" (become commensurate with the contracted top-level skeleton) top-down. w merges with the top-level skeleton first, along a branch b_w at the cusp Q of ∂V_0, and the Y_0-vertex is still intact and constant along b_w. The merge of Y_0 then happens at a cusp of b_w, which is in general not in closure(∂V_0).




### PR-I. The quintic-cover example, the Krull/twin mechanism, Lemma D (merge or twin), the Pinning Lemma and Theorem 4 (from round6_q6, verbatim, sections 2–4). The example surface is NOT smooth (it has a coarse A_1 point at y^5 = x^5 − x and two fixed-locus sheets crossing at the Fermat quintic; proved in round6_q3), so it is a test case, not an admissible V_0.

## 3. In the example the problem's conclusion still holds: the twin mechanism

**Proposition 3.** Let V_0 be the surface of Section 2. Let V_t be a family as in the problem, with readings (R1), (R2), and with ∂V_t := closure(V_t) ∩ Δ_Γ 1-dimensional and π_1(∂V_t) = {Y_t}. Assume condition (O) of PR-E for the piece E_0 = ∂V_0 and the genus-4 vertex. Then Y_t = Y_0 for all t ∈ Δ.

(Smoothness of V_0 plays no role in the argument.)

*Proof.*

**Step 0 (rigid factor).**
- π_2 : ∂V_0 = {Y_0} × C → C is a bijection, and C is the covering-construction curve from M_{0,4}.
- The lift T_{0,4} → T_{4,1} is a holomorphic isometric embedding. It is equivariant for the subgroup of Mod_{0,4} that preserves the monodromy data. So hypothesis (H_0) of PR-E holds: π_2(∂V_0) is a Teichmüller curve in the orbifold sense. Its normalization is the quotient of the disc by the stabilizer of the Teichmüller disc (standard).
- By Lemma R\* (PR-E, under (O)), K := closure(π_2(∂V_t)) = closure(C) ⊂ M̄_{4,1} for every t.
- K is an irreducible compact curve meeting M_{4,1}, so K_∂ := K ∩ ∂M̄_{4,1} is finite.
- Let F ⊂ M_{2,1} be the finite set of 1-pointed curves that occur as a smooth component of a point of K_∂, marked at one of its special points.

**Step 1 (the transported cusp).**
- Put P_t := H_t(P_0). Since H_t preserves strata, closure(V_t) ∩ Δ_{G'} = {P_t}, closure(V_t) \ V_t = ∂V_t ⊔ {P_t}, and P_t ∈ closure(∂V_t).
- So P_t is a chain A_t — B_t — C_t of genus-2 curves. A_t and C_t each carry one node point, and B_t carries two.

**Step 2 (local chart).**
- Let Def(P_t) be the versal deformation germ of P_t, a smooth germ of dimension 15 on which Aut(P_t) acts. The germ of M̄_6 at P_t is Def(P_t)/Aut(P_t).
- Let s_1, s_2 be the smoothing parameters of the nodes A–B and B–C. The locus {s_1 = 0 ≠ s_2} maps to Δ_Γ, with genus-2 vertex the deformation of A_t. The locus {s_2 = 0 ≠ s_1} also maps to Δ_Γ, with genus-2 vertex the deformation of C_t. The locus {s_1 = s_2 = 0} maps to Δ_{G'}.
- Let S̃ ⊂ Def(P_t) be the preimage of the germ of closure(V_t). It is analytic by (R1), since a fibre of an analytic set is analytic. It is of pure dimension 2, since V_t is a dense 2-dimensional manifold in closure(V_t) and the quotient map is finite.
- Moreover S̃ ∩ {s_1 s_2 = 0} is the preimage of ∂V_t ∪ {P_t}, and S̃ ∩ {s_1 = s_2 = 0} = {0}.

**Step 3 (A_t ≅ Y_t).**
- Since P_t ∈ closure(∂V_t), S̃ ∩ {s_1 s_2 = 0} has a branch β̃ through 0.
- β̃ \ {0} is connected and lies in the disjoint union of the relatively open sets {s_1 = 0 ≠ s_2} and {s_2 = 0 ≠ s_1}. Renaming A ↔ C if needed, β̃ \ {0} ⊂ {s_1 = 0 ≠ s_2}.
- Points of β̃ \ {0} lie over ∂V_t, so their genus-2 component (the A-side one) is Y_t. That component depends continuously on the point of the chart, and its value at 0 is A_t. Hence A_t ≅ Y_t as 1-pointed curves.

**Step 4 (the second branch; Lemma C1 of PR-C).**
- Let X_S be an irreducible component of S̃ containing β̃. The function s_2 is not identically 0 on X_S, because it is nonzero on β̃ \ {0}, and s_2(0) = 0.
- So {s_2 = 0} ∩ X_S is of pure dimension 1 through 0. It does not contain β̃, so it contains a branch b̃ ≠ β̃ with b̃ \ {0} ⊂ {s_2 = 0 ≠ s_1}, using S̃ ∩ {s_1 = s_2 = 0} = {0}.
- Points of b̃ \ {0} lie over closure(V_t) ∩ Δ_Γ = ∂V_t, so their genus-2 component, now the C-side one, is Y_t. Letting the point tend to 0 gives C_t ≅ Y_t.

**Step 5 (pinning).**
- Along β̃, π_2 takes values in π_2(∂V_t) ⊂ K: the genus-4 curve obtained by smoothing B ∪ C.
- Its limit at 0 is W_t := B_t ∪ C_t, glued at the B–C node and marked at the point of B_t over the A–B node. So W_t ∈ K ∩ ∂M̄_{4,1} = K_∂.
- C_t is a smooth component of W_t, marked at its special point, so C_t ∈ F. By Step 4, Y_t ∈ F for every t ∈ Δ.
- t ↦ Y_t is continuous (PR-A) and takes values in a finite set, so it is constant on the connected set Δ. ∎

**Remarks.**
1. Lemma 1 shows that the lift R = (Y_t, W_t) has an *unmerged* copy of Y_t at vertex 1, so Theorem P's (T0-a) fails. The pinning instead comes from a *second* copy (twin) C_t of Y_t, which sits inside the boundary point W_t of the *rigid* Teichmüller factor at the other vertex. Step 4 forces this twin to exist at every t: it is the local analytic Lemma C1 combined with the fact that no other boundary curves exist near P_t.
2. Proposition 3 needs neither t small nor hypothesis (ii) beyond (R2). It uses the totally geodesic structure of V_0 only through Step 0.

## 4. General consequences: a dichotomy, a pinning lemma, and a twin criterion

Throughout this section assume (R1), (R2) and the problem's hypotheses. Write P_t := H_t(P_0).

**Lemma D (merge or twin).** Fix t. Let P ∈ closure(∂V_t) \ ∂V_t lie in Δ_{G'}. Let S̃ be the preimage of the germ of closure(V_t) in the versal deformation germ Def(P), and let s_e (e ∈ E(G')) be the smoothing parameters. For a boundary branch c̃ of S̃ through 0, let S_c ⊂ E(G') be the set of edges with s_e ≡ 0 on c̃. Let β̃ be a branch lying over ∂V_t. Then:
1. The edges of G' not in S_β are contracted by the induced contraction c_β : G' → Γ. Its preimage c_β^{-1}(i) is a single vertex j with no loops and no contracted edges, and the component P_j is isomorphic to Y_t.
2. Let b̃ be another boundary branch with the merge property, i.e. some edge f of G' at j has f ∉ S_b. Then exactly one of the following holds.
   - **(D1) Merge.** b̃ lies over a 1-dimensional piece E of closure(V_t) ∩ Δ_{G_b} with G_b ≠ Γ. Then π_v(E) is non-constant, where v is the vertex of G_b containing j (Lemma C2 of PR-C).
   - **(D2) Twin.** b̃ lies over ∂V_t. Then c_b^{-1}(i) is a single loop-free vertex j' ≠ j, and P_{j'} ≅ Y_t. So P has a second component isomorphic to Y_t.

*Proof.*
1. Along β̃ \ {0}, the i-coordinate is the constant smooth curve Y_t. Its limit at 0 is the stable curve assembled from the components P_k, k ∈ c_β^{-1}(i), glued along the edges of G' contracted into i.
   - This limit is the smooth curve Y_t. So the assembled curve has no node, which means c_β^{-1}(i) is one vertex j with no contracted edges or loops, and P_j ≅ Y_t.
2. The coarse image of b̃ \ {0} lies in a single stratum, by connectedness. If that stratum is not Δ_Γ we are in (D1).
   - Otherwise b̃ lies over closure(V_t) ∩ Δ_Γ = ∂V_t. Part 1, applied to b̃, gives the single loop-free vertex j' = c_b^{-1}(i) with P_{j'} ≅ Y_t.
   - The edge f at j is contracted by c_b (f ∉ S_b). So the vertex c_b(j) contains a contracted edge, hence c_b(j) ≠ i, i.e. j ≠ j'. ∎

**Lemma (Pinning).** Let 𝒰 be a finite set of pairs (E_0, u). Here E_0 is a 1-dimensional component of closure(V_0) ∩ Δ_{G}, G product type, u is a vertex of G, π_u(E_0) is a Teichmüller curve in the orbifold sense, and condition (O) of PR-E holds for (E_0, u). Put E_t := H_t(E_0). Suppose:

**(Pin)** For every t in a disc around 0 there is (E_0, u) ∈ 𝒰 such that Y_t is isomorphic, after relabelling, to a smooth component of a point of closure(π_u(E_t)) ∩ ∂M̄_u.

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. By Lemma R\* (PR-E), closure(π_u(E_t)) = closure(π_u(E_0)) =: K_u for all t. Each K_u ∩ ∂M̄_u is finite.
2. So Y_t lies in a fixed finite set for t in the disc. By continuity (PR-A) it is constant there.
3. By holomorphy (PR-A) and the identity theorem, Y_t = Y_0 on Δ. ∎

The step-3 argument of Theorem P shows that **(T0) ⇒ (Pin)**. Proposition 3 shows that **(Pin) holds in the example of Section 2**, where (T0) fails. The following criterion abstracts Proposition 3. Like (T0), it is a condition on V_0 alone.

**Theorem 4 (twin criterion).** Let P_0 ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G'}. Let 𝒞 be the set of edge sets S ⊂ E(G') such that contracting E(G') \ S gives a graph identified with Γ, by an identification compatible with ξ_Γ, in which the preimage of vertex i is a single loop-free vertex j(S). Assume:
- **(Tw1)** There is a neighbourhood U of P_0 with (closure(V_0) \ V_0) ∩ U ⊂ ∂V_0 ∪ {P_0}.
- **(Tw2)** For all S ≠ S' in 𝒞:
  - j(S) ≠ j(S');
  - the vertex w = w(S, S') of Γ that contains j(S') under the contraction by S has an edge of G' among the edges contracted into it;
  - for every component E_0 of ∂V_0 with P_0 ∈ closure(E_0), π_w(E_0) is a Teichmüller curve in the orbifold sense satisfying (O).

Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. **Transport.** By (R2), H_t maps closure(V_0) ∩ U onto a neighbourhood of P_t in closure(V_t), preserving strata. So near P_t, closure(V_t) \ V_t ⊂ ∂V_t ∪ {P_t}, and in Def(P_t) we have S̃ ∩ {all s_e = 0, e ∈ E(G')} = {0}.
   - G' and its combinatorics are the same at P_t as at P_0, because the stratum is preserved. The set 𝒞 depends only on G' and Γ.
2. **The branch β̃.** Take a branch β̃ of the preimage of ∂V_t through 0. By Lemma D(1), S_β ∈ 𝒞, and P_t has the component Y_t at j := j(S_β).
   - S_β ≠ E(G'), since P_t ∉ Δ_Γ.
3. **The branch b̃.** Pick e ∉ S_β. Lemma C1 of PR-C, as in Step 4 of Proposition 3, gives a boundary branch b̃ ≠ β̃ through 0 with e ∈ S_b.
   - By Step 1, b̃ lies over ∂V_t. So S_b ∈ 𝒞 by Lemma D(1), S_b ≠ S_β, and P_t has the component Y_t at j' := j(S_b) ≠ j, by (Tw2).
4. **The good vertex.** Let E_t = H_t(E_0) be the component of ∂V_t containing the image of β̃, so P_0 ∈ closure(E_0). Let w = w(S_β, S_b).
   - Along β̃ the w-coordinate converges to the stable curve assembled from the components of P_t over w, which include P_{j'} ≅ Y_t.
   - That curve has a node, by (Tw2). So it lies in closure(π_w(E_t)) ∩ ∂M̄_w, and Y_t is one of its smooth components.
5. **Conclusion.** This is (Pin) with 𝒰 the finite set of pairs (E_0, w) allowed by (Tw2), and it holds for every t. The Pinning Lemma concludes. ∎

**Check against Section 2.**
- G' is the chain A — e_1 — B — e_2 — C, and 𝒞 = {{e_1}, {e_2}} with j({e_1}) = A and j({e_2}) = C.
- w({e_1}, {e_2}) is the genus-4 vertex, which contains the edge e_2. Symmetrically, w({e_2}, {e_1}) contains e_1.
- π_2(∂V_0) = C is a Teichmüller curve. (Tw1) holds because closure(V_0) \ V_0 = ∂V_0 ⊔ {P_0}.
- So Proposition 3 is the case (Tw) of Theorem 4, modulo (O).

**What this means for MS5 and the chain.**
- MS5 (= (T0)) is not the right missing statement. It is false without smoothness (Section 2), and the problem's conclusion survives there via (Tw).
- The correct target is **(Pin)**, or the V_0-only disjunction **"(T0) or (Tw) holds at some point P_0 of closure(∂V_0)"**. Both are still open in general.
- Lemma D explains why a disjunction is natural. At a cusp, Lemma C1 always produces a second boundary branch b̃. If b̃ has the merge property, it is either a genuinely new boundary curve (D1, the (T0) mechanism) or ∂V_t again with a twin (D2, the (Tw) mechanism).
- What neither mechanism covers:
  - a cusp where no branch b̃ merges vertex j and no twin arises: the non-merge case of PR-C, still open;
  - (D1)-branches whose merged vertex is not a Teichmüller curve: positive area not established, (PA) of PR-F;
  - (D2)-twins whose host vertex w is not a Teichmüller curve or carries no node.



### R7-1. Time-t lemmas, constant vertices at junctions, and Theorem T (MS6 near t = 0 under (Lock)) (from round7_q6, verbatim, sections 1–3)
## 1. Fixed-t local lemmas (proved)

Fix t. Let Q ∈ B_t, let x ∈ V(G_Q) be a vertex with Q_x a Y_t-copy, and let b be a 1-dimensional branch of B_t at Q. Let b̃ be a branch at a lift q of Q in Def(Q) of π^{-1}(b), with pinched set S_b := {e : s_e ≡ 0 on b̃} and U_b := E(G_Q) \ S_b. Let G_b := G_Q/U_b; this is the dual graph along b̃ \ {q}, which lies in one stratum. Let E be the 1-dimensional piece of closure(V_t) ∩ Δ_{G_b} containing π(b̃ \ {q}), lifted to ∏_w M_w in the way the local labelling of b̃ induces. Let p ∈ Ē be the point over Q determined by b. Write [x] for the vertex of G_b containing x.

**Lemma 1 (merges and puncture-moves give MS6).**
- (a) Suppose some edge of G_Q at x lies in U_b ("merge"). Then f_{[x]} is non-constant on E, p is a puncture of E, and f_{[x]}(p) has the component Q_x with the same special points. So MS6 holds at t, witnessed by (E, [x], p).
- (b) Suppose all edges at x lie in S_b, Q ∉ Δ_{G_b} (i.e. U_b ≠ ∅), and f_{[x]} = f_x is non-constant on E. Then p is a puncture and f_x(p) = Q_x ≅ Y_t. So MS6 holds at t.

*Proof.*
- (a) By (Def1), as r → q along b̃ the [x]-component of C_r tends to the curve glued from the components Q_y, y ∈ [x], along the edges of U_b inside [x]. This set of edges contains an edge at x, so the limit is a nodal curve in ∂M̄_{[x]}. Off q the [x]-component lies in M_{[x]}. So f_{[x]} is non-constant (PR-C, Lemma C2), and ν(p) ∉ ∏_w M_w, so p is a puncture.
  - Q_x is a component of the limit curve f_{[x]}(p). Its special points there are the branches of nodes internal to [x] together with the marked points coming from edges leaving [x]. Together these are exactly the node branches of Q at Q_x. So the pointed curve is unchanged.
- (b) Here [x] = {x}, and by (Def1) f_x(p) = Q_x. Some edge of G_Q lies in U_b, so it is contracted into some vertex w of G_b, and f_w(p) is nodal. Hence ν(p) ∉ ∏ M_w, and p is a puncture. ∎

**Lemma 2 (closedness).** N_t := {Q ∈ B_t : Q has a Y_t-copy} is closed in B_t. More generally: if t_n → t, Q_n ∈ B_{t_n}, Q_n → Q, and Q_n has a Y_{t_n}-copy, then Q has a Y_t-copy.

*Proof.*
- Lift to Def(Q): r_n → q. Pass to a subsequence with U(r_n) = U constant, and with the copy of Q_n at a fixed vertex V of G_Q/U.
- By (Def1), the V-component of C_{r_n} converges to the curve glued from the Q_y, y ∈ V, along the edges of U inside V. Since Y_{t_n} → Y_t (PR-A) and Y_t is smooth, this limit is smooth.
- So V is a single vertex y, with no edge of U at y forming a node inside V, and Q_y ≅ Y_t. ∎

**Lemma 3 (dichotomy at a point of N_t).** Suppose MS6 fails at t. Let Q ∈ N_t, let x be any Y_t-copy of Q, and let b be any branch of B_t at Q (any lift b̃). Then exactly one of the following holds:
- (STAY) all edges at x are pinched along b̃, and f_x is constant (≡ Q_x) on the piece E of b; or
- (IMOV, interior move) all edges at x are pinched along b̃, U_b = ∅ (so Q ∈ E is an interior point of the piece, in the same stratum), and f_x is non-constant on E.

Consequently, if moreover no IMOV occurs at points of N_t, then N_t is open in B_t. By Lemma 2 it is then a union of connected components of B_t, and it contains the connected component C_t of B_t containing ∂V_t (on which vertex i is a copy).

*Proof.*
- Lemma 1(a) excludes a merge, and Lemma 1(b) excludes a non-constant f_x with U_b ≠ ∅. What remains is STAY or IMOV.
- Openness: near Q, B_t is the union of its finitely many branches b. If b is STAY for some copy x, the points of b near Q carry the constant component Q_x, so they lie in N_t. ∎

**Remarks on the approach of the task.**
1. IMOV cannot be excluded by Lemma 1: an interior point is not a puncture. L1 and L2 give only that Y_t lies on the t-independent curve closure(π_x(E_0)), with value Y_t = g(σ(t)) where g is one of finitely many maps (L2) and σ(t) := A_t^{-1}(Q̃_t) ∈ Ē_0. The point σ(t) is the transported "junction point" Q_t on E_t. Nothing ties it to a puncture or to a cone point of Ē_t, because A_t is the Thurston/Teichmüller identification and not H_t. So the IMOV case is **not pinned** by these tools. It remains open (see §4).
2. **Step 2(b) is dead in the stated generality (heuristic, not proved).** At a fixed t ≠ 0, V_t is an arbitrary algebraic surface: total geodesy is not available. The only time-t inputs are (R1) and the local analytic structure. A configuration in which a connected component C of the boundary carries a fixed isolated constant component Y is not locally contradictory. Near such a component, closure(V_t) looks like a smoothing of "Y glued to a moving family", with the normal direction contracting (negative normal degree, -ψ·C < 0, so Grauert contractibility is consistent). I did not construct a global algebraic example, so this is only a heuristic. But it shows that any contradiction must come from t = 0, as in option (a), and hence must face the twin problem. §2 explains exactly where that problem enters, and §3 bypasses it under (Lock).

## 2. Where option 2(a) breaks: twins (analysis)

Suppose MS6 fails, and Lemma 3 gives N_{t_n} ⊇ C_{t_n} = H_{t_n}(C_0) for generic t_n → 0. Pass to t = 0, and fix Q_0 ∈ C_0 together with the MERGE branch b of Proposition K, in which the tracked copy c of Q_0 merges along a lift b̃.
- For lifts q_n → q_0 of Q_{t_n}, every lift-branch b̃_n of b_{t_n} at q_n converges into a lift γ b̃ of b, for some γ ∈ Aut(Q_0). By the edge count of Step 3 below, its pinched set is S_{b̃_n} = γ S_b̃. So the label γc merges along b̃_n.
- The Y_{t_n}-copies of Q_{t_n} converge to Y_0-copies of Q_0 (Lemma 2), so the limiting labels lie in Λ(Q_0) := {ℓ ∈ V(G_{Q_0}) : Q_{0,ℓ} is a Y_0-copy}.
- But γc need not be among them. Q_0 may have several Y_0-copies, a merged one and an unmerged twin, and for t ≠ 0 these may stop being isomorphic. Then the merged one is not a Y_t-copy, and no contradiction arises.

This is exactly the twin phenomenon of PR-G/PR-I. Option (a) and the direct transport of §3 fail or succeed at the same place. I therefore isolate the needed property as a hypothesis.

**Definition (Lock).** Let R ∈ B_0 ∩ Δ_{G'}, let q_0 ∈ Def(R) be a lift, and let Λ(R) ⊂ V(G') be the set of labels of Y_0-copies of R. Note that Λ(R) is Aut(R)-invariant. R is *locked* if there is ε > 0 such that, for |t| < ε and every lift q of R_t := H_t(R) in a fixed small neighbourhood of q_0 in Def(R), the components C_{q,ℓ}, ℓ ∈ Λ(R), are pairwise isomorphic as pointed curves up to reordering.
- (Lock) holds trivially if |Λ(R)| = 1, i.e. R has a unique Y_0-copy.
- It holds at the point P_0 of the quintic example (PR-I, Proposition 3, Steps 3–4: A_t ≅ C_t ≅ Y_t for all t, and Λ(P_0) = {A, C} since B_0 has two special points).
- Note that R_t ∈ Δ_{G'} for all t by (R2), so its lifts lie in D' := {s_e = 0 for all e} ⊂ Def(R), where the labels make sense.

---

## 4. What remains open, and why

### 4.1 Twins (removing (NT\*))
Without (NT\*), Step 1 fails, and λ_t becomes a multivalued function on K_0.
- At a point J ∈ K_0 with two components x, y ≅ Y_0, the continuations x(t) and y(t) can carry different holomorphic labels: z_D(t) from one adjacent STAY piece D, and z_{D′}(t) from another adjacent STAY piece D′.
- The Y_0-network of Proposition K is only "consistent with the path marking". Path markings at a boundary point are defined only up to Aut(J) and the approximating sequence. So the network may jump from x to y at J.
- At time t ≠ 0 the automorphism realising the jump may disappear. Then the copy of Y_t being followed is lost.
- The quintic example (PR-I) shows that such twin points really occur, although on a non-smooth V_0. There the problem's claim is rescued by a different mechanism: the twin sits in a puncture value of a rigid vertex (PR-I, Theorem 4).
- **Open question 1.** Is (NT\*) dispensable? Concretely: at a twin junction J, does one of the following always happen at time t?
  - the Y_t-copy continues along a STAY piece carrying the label Y;
  - the Y_t-copy enters a non-constant vertex at a puncture (that is, MS6).

  The only other possibility is a crossing (4.2). I have no argument.

### 4.2 Crossings (removing (E))
Suppose the endpoint is of type MOV-interior. Then Q_0 ∈ E_b, where E_b is a piece in the stratum of Q_0, and the vertex x is non-constant on E_b with f_x(Q_0) = Y_0. Also, Q_0 lies in the closure of an adjacent STAY piece.

Under (NT\*) and (PT), Steps 1–5 still give λ_t(Q_0) = Y_t. That is:

  **Y_t = f_x^t(H_t(Q_0))**, the value of the non-constant vertex x at the INTERIOR point H_t(Q_0) of the transported piece E_{b,t}.

This is not the MS6 configuration. Nor does it yield rigidity:
- If x is a Teichmüller vertex of E_b satisfying (O), Lemma R\* only gives that Y_t moves inside the fixed curve closure(π_x(E_{b,0})).
- H_t(Q_0) is an uncontrolled point of E_{b,t}.

**A crossing is locally consistent (so no Krull-type argument can exclude it).**
- Take a smooth germ of closure(V_t) with coordinates (σ, ρ).
- Put s_e = ρσ for the edges e at x, and s_f = ρ for the other edges. Let the x-coordinate equal σ.
- Then {ρ = 0} is E_b: all edges are pinched and x moves.
- {σ = 0} is the STAY piece: the edges at x are pinched, the others are smoothed, and x is constant.
- Points with ρσ ≠ 0 lie in M_g.

This is compatible with (R1), (R2), (i) and (ii), at t = 0 and at every t. It is the same phenomenon as in PR-C.

- **Open question 2.** Can Proposition K be sharpened (choice of rays, or of stopping rule) so that its endpoint is never a crossing? Equivalently, for smooth totally geodesic V_0: does every Y_0-network reach a MERGE, or a MOV at a puncture?
- Note that MS6 for constant families (MS6_0, §1.4) requires a positive answer, or an argument that handles crossings differently.

### 4.3 Why I did not transport the Teichmüller rays to time t (a dead end, recorded)
The natural route to removing (NT\*) is to transport the marked ray segments g_s X_n of Proposition K by H_t, and to follow the marked Σ_i along them at time t. Continuity in s of the marked Σ_i-part, together with finiteness of the label set (Step 4), would then remove the ambiguity at twin junctions.

This breaks down for the following reason.
- The marking at H_t(g_s X_n) must be defined by lifting the square (s, τ) ↦ H_τ(g_s X_n) to Teichmüller space.
- The square can meet orbifold points of the moving surfaces V_τ. These are points with extra automorphisms, which (unlike at τ = 0) move with τ and sweep real hypersurfaces of V_0 under H^{-1}. So they cannot be avoided by perturbing the ray.
- The monodromy of the lift around such a point is an automorphism α of a curve close to the boundary. It can send Σ_i to a twin subsurface α(Σ_i). Its part is isomorphic at that moment, but it is continued by a *different* label afterwards.
- So the transported-ray argument meets exactly the twin problem again, now at interior times τ ∈ (0, t).
- Passing to level-N covers does not help. The pull-back to V_0 × Δ of the branched cover M_g[N] → M_g need not be a product, because its branch locus varies with τ.

---


### R7-3. Kuranishi-chart transport lemmas, (TR) without twins, the twin dichotomy, and a chart-local twin-jump model (from round7_q5, verbatim, sections 1–5)
## 1. Set-up: Kuranishi charts and chart components

**Standard facts (cited from memory).**

(K1) Let J be a stable curve. It has a universal deformation over a smooth germ Def(J), with smoothing parameters s_e for the nodes e ∈ E(G_J), and Aut(J) acts on Def(J). A neighbourhood of J in M̄_g is Def(J)/Aut(J). So the preimages in Def(J) of a point J′ near J form one Aut(J)-orbit.

(K2) Let x be a vertex of G_J, and let L_x := {s_e = 0 for every edge e at x}, a smooth subgerm. Over L_x the fibre curve has a component "x", deforming J_x. This gives a holomorphic map F_x : L_x → M_{g_x,n_x}. Its special points are labelled by the half-edges at x.

(K3) For σ ∈ Aut(J) and q ∈ L_x we have σq ∈ L_{σx}, and σ induces an isomorphism of fibre curves taking component x to component σx. Hence

 F_x(σq) ≅ F_{σ^{-1}x}(q)  (as pointed curves, after relabelling).

Throughout, "≅ Y" means isomorphic as an n_i-pointed curve up to relabelling. Equivalently, we compare images in the coarse space M_{g_i,n_i}/S_{n_i}, which is an analytic space. All identity-theorem arguments below take place there.

**Interpretation of the hypotheses of (TR).** "The c_m-limit along D^m and the c_{m+1}-limit along D^{m+1} are the same component of J_m (tracked by path markings)" is read as follows. There are lifts β̃^m, β̃^{m+1} ⊂ Def(J_m), through 0, of the relevant branches of ξ(D^m) and ξ(D^{m+1}) at J_m, and a vertex x_m of G_{J_m}, such that:
- c_m is the single chart vertex x_m along β̃^m;
- c_{m+1} is the single chart vertex x_m along β̃^{m+1}.

This is what continuity of the marking inside the chart gives. The merge at Q_0 is read the same way: there are lifts β̃^k, β̃^E ⊂ Def(Q_0) and a chart vertex x with c_k = {x} along β̃^k and x ∈ class(u) along β̃^E.

A constant vertex c has a smooth limit at J. So c corresponds to a single chart vertex with no contracted edges, and the branch lies in L_x.

## 2. Transport lemmas

**Lemma 1 (constant values are holomorphic; generic constancy).** Let D be a piece at time 0, D_t := H_t(D) its transport, and c a vertex of D's graph.
(a) If c is constant on D, then c is constant on D_t for every t. Its value φ_c(t) is a holomorphic function of t.
(b) If c is non-constant on D, then c is non-constant on D_t for all t outside a countable set.

*Proof.* (a) Constancy is L1. Fix p ∈ D. Then φ_c(t) = pr_c of a lift of H(p,t). This is continuous in t, because H is continuous and lifts through the finite map ξ can be chosen continuously along paths.

Let 𝓦 be the irreducible 2-dimensional analytic set of Lemma R0 (PR-D) for D. Then Γ := (pr_c, t)(𝓦) is an irreducible analytic set (Remmert), whose fibre over each t is finite by L1. So Γ is a curve, finite over Δ. A continuous function whose graph lies in such a curve is holomorphic off a discrete set, where the curve is locally a union of graphs, and hence everywhere by Riemann extension.

(b) Let C ⊂ 𝓦 be the analytic set where (pr_c, t) has rank ≤ 1. Suppose pr_c is constant on the fibre components over uncountably many t. Then C contains uncountably many fibre curves. A ≤ 1-dimensional analytic set contains only countably many of them, so C = 𝓦. By the rank theorem the image Γ is then an irreducible curve that is not contained in a fibre of t, so it is finite over Δ. Hence pr_c is constant on every fibre component, including at t = 0. ∎

**Lemma 2 (transport of a lifted branch in a fixed chart).** Let J ∈ closure(V_0) \ V_0 and J(t) := H_t(J). Let β̃ ⊂ Def(J) be a lifted branch at 0 of a piece D, where either J is a puncture of D, or J ∈ ξ(D) and β̃ is the lifted germ of D itself. Let x be a chart vertex such that a vertex c, constant on D, equals {x} along β̃. Then for |t| < ε there is a set Ñ ⊂ Def(J) × Δ_ε with the following properties:
- Ñ is a connected analytic set with Ñ ∩ {t = 0} = β̃ \ {0}, or β̃ itself in the interior case;
- for each t, closure(Ñ_t) contains a lift J̃_β(t) of J(t), and Ñ_t ∪ {J̃_β(t)} ⊂ L_x;
- F_x ≡ φ_c(t) on Ñ_t ∪ {J̃_β(t)}.

*Proof (puncture case; the interior case is the same with D's own lifted family).*

1. Let β be the image branch of ξ(D) at J. Then N := H((β \ {J}) × Δ_ε) is a topologically trivial family of punctured discs. By (R2), near J(t) we have closure(ξ(D_t)) ∩ Δ_{G_J} = {J(t)}, because closure(ξ(D)) \ ξ(D) is finite and H_t is a stratum-preserving homeomorphism.
2. Let Ñ be the connected component of the preimage of N in Def(J) × Δ_ε that contains β̃ \ {0}. The preimage of the analytic family of D is analytic (Lemma R0 and Remmert), and N is open and closed in it near (J,0). So Ñ is analytic. Ñ is a connected topological 4-manifold, being a cover of a punctured disc times a disc. Hence Ñ is irreducible: removing a singular set of real codimension ≥ 2 does not disconnect it.
3. The pinching pattern {e : s_e ≡ 0} is constant on the irreducible set Ñ. At t = 0 it contains every edge at x, so Ñ ⊂ L_x.
4. Fix once and for all an identification of the contracted graph with D's graph. This gives a holomorphic map from Ñ to ∏_w M_w. Its image is irreducible and meets the lift of D at t = 0. So it lies in the lifted family 𝓦 of D, and F_x = pr_c on Ñ. By L1 and Lemma 1, pr_c ≡ φ_c(t) on 𝓦_t.
5. Ñ_t → N_t = β_t \ {J(t)} is proper and finite (K1). So points of Ñ_t approaching J(t) accumulate at lifts of J(t). Pick one, J̃_β(t). It lies in L_x because L_x is closed, and F_x(J̃_β(t)) = φ_c(t) by continuity of F_x. ∎

**Remark.** The same proof applies when the vertex containing x along β̃ is a non-constant vertex u. Then the u-limit at J̃_β(t) is the curve obtained by gluing the chart components in class(u) at J̃_β(t). This is a puncture value f_u^t(p) of D_t, at the puncture of D_t lying over J(t). Moreover u is non-constant on D_t whenever class(u) contains a contracted edge: a constant smooth curve cannot have a nodal limit (Lemma C2 of PR-C).

**Lemma 3 (twist).** Let β̃, β̃′ be lifted branches at 0 ∈ Def(J), with transports Ñ, Ñ′ and lifts J̃_β(t), J̃_{β′}(t). Then for each t there is σ_t ∈ Aut(J) with J̃_{β′}(t) = σ_t J̃_β(t). Some single σ occurs for all t in a set T_σ that is uncountable, and in particular accumulates at 0.
Moreover σ_t^{-1}·closure(Ñ′_t) is a lifted branch of D′_t through J̃_β(t). Along it, the vertex containing a chart vertex y is the σ_t^{-1}-image of the vertex of Ñ′_t containing σ_t y.

*Proof.* The two lifts of J(t) lie in one Aut(J)-orbit by (K1). Aut(J) is finite, and a finite union of the sets T_σ covers the uncountable disc. Aut(J) preserves the preimage of closure(V_t). The last statement is (K3). ∎

## 3. Theorem A: (TR) holds without twins

**Hypothesis (NT).**
- For each junction J_m (m < k): every σ ∈ Aut(J_m) fixes the chart vertex x_m.
- At Q_0: every σ ∈ Aut(Q_0) fixes x.

A sufficient condition: no other component of J_m (respectively Q_0) is isomorphic to the x_m-component (respectively the x-component), as a curve with unordered special points.

**Theorem A.** Assume the hypotheses of (TR), L1, and (NT). Then:
- φ_{c_m} ≡ Y for every m;
- for all t in a disc around 0 minus a countable set, the transported piece E_t has a vertex u that is non-constant on E_t and a puncture p′ such that f_u^t(p′) has a component isomorphic to Y_t.

*Proof.*
1. **Junctions.** Fix m < k. Apply Lemma 2 at J = J_m to (β̃^m, c_m, x_m) and to (β̃^{m+1}, c_{m+1}, x_m). This gives
 F_{x_m}(J̃^m(t)) = φ_{c_m}(t) and F_{x_m}(J̃^{m+1}(t)) = φ_{c_{m+1}}(t).
 By Lemma 3, J̃^{m+1}(t) = σ_t J̃^m(t). By (K3) and (NT),
 F_{x_m}(σ_t J̃^m(t)) = F_{σ_t^{-1}x_m}(J̃^m(t)) = F_{x_m}(J̃^m(t)).
 So φ_{c_{m+1}}(t) = φ_{c_m}(t) for all small t, and both functions are holomorphic (Lemma 1). Hence φ_{c_{m+1}} ≡ φ_{c_m} on Δ by the identity theorem.
 By induction from φ_{c_1} = Y (since c_1 = i on ∂V_t), we get φ_{c_k} ≡ Y.
2. **The merge at Q_0.** Apply Lemma 2 at Q_0 to (β̃^k, c_k, x), and apply the Remark after Lemma 2 to (β̃^E, u). Then F_x(Q̃^k(t)) = Y_t.
 Let Q̃^E(t) = σ_t Q̃^k(t). The u-limit of E_t at the puncture over Q(t) is the gluing of the components in class(u) at Q̃^E(t). This class contains x, whose component is
 F_x(σ_t Q̃^k(t)) = F_{σ_t^{-1}x}(Q̃^k(t)) = F_x(Q̃^k(t)) = Y_t, by (NT).
 Q(t) is not in ξ(E_t), because H_t preserves strata and Q_0 ∉ ξ(E). So this limit is a puncture value f_u^t(p′).
3. **u is non-constant.** In the MERGE case, class(u) contains a contracted edge, and the Remark after Lemma 2 shows that u is non-constant on E_t for every t. In the puncture-MOV case (u = {x} along β̃^E), u is non-constant on E_0, so it is non-constant on E_t for all t outside a countable set, by Lemma 1(b). ∎

**Corollary A.** Combine Theorem A with chain steps 1–4 (which use L1, L2 and (O)). If Prop K's configuration at t = 0 satisfies (NT) and ends in MERGE or in puncture-MOV, then Y_t = Y_0 for all t.

Note that (NT) **fails** in the quintic example (PR-I). There P_0 = A–B–C with A ≅ C ≅ Y_0, and the symmetric chain has an automorphism exchanging A and C. That example is settled by a different, time-t Krull argument (see §5).

## 4. The twin case: a robust analysis

From now on we argue by contradiction and **assume Y is non-constant**. Let Φ be the finite family of holomorphic functions consisting of:
- Y;
- the φ_c for all pieces D at time 0 and all vertices c constant on D;
- the constant functions given by the (finitely many) components of the elements of the finite sets F(E_0,u) of L2.

Let Z ⊂ Δ be the countable set of t at which one of the following happens:
- two distinct functions of Φ take the same value;
- some vertex changes from non-constant to constant (Lemma 1(b)).

Call t ∉ Z *generic*.

**Lemma 4 (closedness of the Y-network at generic time).** Let t be generic, J ∈ closure(V_0) \ V_0, and let q ∈ Def(J) be a lift of J(t). Let β̃_t, β̃′_t be two transported lifted branches through q, i.e. sets of the form ρ·closure(Ñ_t) with ρ ∈ Aut(J). Let y be a chart vertex that is, along β̃_t, a single constant vertex c with φ_c ≡ Y. Let w be the vertex of the piece D′ of β̃′_t that contains y. Then one of the following holds.
- (a) w = {y} is a constant vertex of D′ with φ_w ≡ Y.
- (b) J(t) ∈ ξ(D′_t) is an interior point of D′_t, and w = {y} is non-constant on D′_t with pr_y(J(t)) ≅ Y_t. Call this *interior-MOV*.

In particular, (i) w never contains a contracted edge, and (ii) w is never a non-constant vertex at a puncture.

*Proof.*
- F_y(q) ≅ φ_c(t) = Y_t.
- Suppose w contains a contracted edge, or w is non-constant on D′_t with J(t) a puncture. Then Y_t is a component of a puncture value f_w^t(p), which lies in a finite set F(D′_0, w) by L2 (and L1). So Y_t equals one of the constant functions in Φ, which is impossible for generic t because Y is non-constant.
- Suppose w is constant. Then w = {y} (its limit is smooth) and φ_w(t) = Y_t. For generic t this forces φ_w ≡ Y.
- The remaining case is (b). ∎

**Theorem B (twin dichotomy).** Assume Y is non-constant. Let a junction J_m satisfy φ_{c_m} ≡ Y. Then:
- either φ_{c_{m+1}} ≡ Y;
- or there is σ ∈ Aut(J_m) with σ x_m ≠ x_m (a *twin jump*) such that, along the t = 0 branch β̃^{m+1}, the chart vertex σx_m is a single constant vertex c′ of D^{m+1} with φ_{c′} ≡ Y. The exception is an interior-MOV event at J_m.

Similarly, at Q_0: either the conclusion of (TR) holds for all generic t (impossible, since it forces Y_t into a finite set), or there is σ ∈ Aut(Q_0) with σx ≠ x such that, along β̃^E, σx is a single constant vertex of E with φ ≡ Y (again up to interior-MOV).

Hence, if Y is non-constant and there is no interior-MOV event, the Y-network performs at least one twin jump along the chain of (TR).

*Proof.*
1. Take t ∈ T_σ (Lemma 3) generic, q = J̃^m(t), β̃_t = closure(Ñ^m_t), β̃′_t = σ^{-1}closure(Ñ^{m+1}_t), and y = x_m.
2. Lemma 4 says the vertex of β̃′_t containing x_m is a Y-network constant. By (K3), that vertex is the σ^{-1}-image of the vertex of Ñ^{m+1}_t containing σx_m.
3. The pinching pattern and the vertex structure are constant along Ñ^{m+1}, so the same holds on β̃^{m+1} at t = 0.
4. If σx_m = x_m, this vertex is c_{m+1}, and φ_{c_{m+1}} ≡ Y.
5. At Q_0, run the same argument with β̃′ = σ^{-1}·(transport of β̃^E). If σx = x, the vertex containing x is u, which contradicts Lemma 4 (i)/(ii). ∎

**What a twin jump means.** At t = 0 the curve J_m has two components x_m ≠ σx_m, both isomorphic to Y_0 and exchanged by an automorphism. The marked track of Prop K continues along x_m into a constant vertex c_{m+1} with φ_{c_{m+1}} ≢ Y. The deformation, however, carries the Y-network on to the twin σx_m. For t ≠ 0 the automorphism σ no longer exists: J(t) has two different components φ_{c_m}(t) = Y_t and φ_{c_{m+1}}(t), which coincide at t = 0.

## 5. Why (TR) is not decided here: a local model and a t = 0 reformulation

**Local model (twin jump, consistent in the chart).**
- Let Def(J_0) contain coordinates (a, b) of the two Y_0-components x, y, with σ(a, b) = (b, a). Let J(t) have lifts J̃(t) = (t, −t, …) and σJ̃(t) = (−t, t, …).
- Suppose the transported D^m passes through J̃(t), with constant vertex at x of value Y_0 + t (= Y_t) and constant vertex at y of value Y_0 − t.
- Suppose the transported D^{m+1} passes through σJ̃(t), with c_{m+1} at x of value Y_0 − t, and a network vertex at y of value Y_0 + t.
- At t = 0 both branches pass through 0, and c_m, c_{m+1} both sit at x. So the hypotheses of (TR) at this junction hold.
- Lemma 4 is satisfied at every time, because D^m has a network vertex at y as well. Krull's theorem at time t gives no further constraint unless the global stratum structure is known, as in PR-I.

So no argument confined to the Kuranishi charts at the junctions can prove (TR). Any proof must use global information about how the marked Teichmüller track of Prop K sits relative to the deformation. Constructing an actual family V_t realizing this model is out of reach; I have **no counterexample**.

**How the quintic example escapes.** There the extra input is Krull at time t in Def(P_t) (PR-I Prop 3), together with the knowledge that every boundary branch near P_t lies over ∂V_t. This produces, at the same point q at time t, a branch with the opposite pinching pattern. Its network vertex lies inside the non-constant vertex of the first branch, which is the violation (ii) of Lemma 4. The general version of this observation: Krull at time t produces coherent pairs of branches (pairs through the same lift) with a prescribed pinched edge, but it does not control which pieces they belong to.

**A t = 0 statement that would suffice (MS7, open).** Call a set 𝒩 of pairs (D, c) — D a piece at time 0, c constant on D with value ≅ Y_0, containing (each component of ∂V_0, i) — **Aut-closed** if the following holds. For every J ∈ closure(V_0) \ V_0, every lifted branch β̃ at 0 ∈ Def(J) of some (D, c) ∈ 𝒩 with c = {x}, and every lifted branch β̃′ at 0 of any piece D′ through J, there is τ ∈ Aut(J) such that the vertex of D′ containing τx along β̃′ is a single constant vertex c′ with (D′, c′) ∈ 𝒩. (Interior points of D′ are included.)

- Lemma 4, transported to t = 0 as in Theorem B, shows: **if Y is non-constant and no interior-MOV event occurs, then the Y-network {(D, c) : φ_c ≡ Y} is Aut-closed.**
- So MS7 — "no Aut-closed set 𝒩 exists" — implies Y_t = Y_0, modulo the interior-MOV case.
- Prop K does not prove MS7. Its track follows the marking, which at a twin junction may continue along x_m rather than along σx_m (§4). If the track always stays inside 𝒩, Prop K does give a contradiction (Theorem A is the special case where this is automatic).


### R7-4. Time-t criterion, transport of branch patterns, total-merge transport, spreading of Y_t-copies (from round7_q2, verbatim, sections 0–4)
## 0. Notation used throughout

- B_t := closure(V_t) \ V_t. This is a compact analytic set of dimension ≤ 1. By (R2), H_t(B_0) = B_t, and H_t preserves strata.
- For a point Q ∈ B_0, put Q_t := H_t(Q).
- Def(Q) is the versal deformation germ of the stable curve Q, with smoothing parameters s_e, e ∈ E(G_Q). The group 𝔅 := Aut(Q) acts on Def(Q). The germ of M̄_g at Q is q : Def(Q) → Def(Q)/𝔅.
- On the locus {s_e = 0 for all e ∈ E(G_Q)} ≅ ∏_{x ∈ V(G_Q)} Def(Q_x), each point p has components comp_x(p), labelled by the vertices x of G_Q. Each comp_x(p) is a smooth curve carrying its special points, and it depends holomorphically on p.
- An element a ∈ 𝔅 acts on labels, and comp_x(a p) ≅ comp_{a^{-1}x}(p) as pointed curves.
- The fibre q^{-1}(Q) is {0}. Since q is proper, every lift of Q_t tends to 0 as t → 0.
- **Pattern.** For a point p of Def(Q) put S(p) := {e : s_e(p) = 0}. For S ⊂ E(G_Q):
  - an edge not in S is *unpinched*;
  - a vertex x is *intact* for S if every edge at x lies in S, and *merged* otherwise;
  - M(S) denotes the set of merged vertices.
- A *Y_t-copy* of a point P is a component of P that is isomorphic to Y_t as an n_i-pointed curve, in some order of its special points.
- C_0(Q) := {x ∈ V(G_Q) : comp_x(0) is a Y_0-copy}. This set is 𝔅-invariant.
- A *boundary branch* at Q is a local branch b at Q of B_0 with Q ∉ the stratum of b. Equivalently, Q is a puncture of the piece E_b that contains b.
  - A lift b̃ ⊂ Def(Q) has constant pattern S_b̃. The other lifts are the translates a b̃, with patterns a S_b̃.
  - M^+(b̃) := M(S_b̃) ∪ {x intact for S_b̃ : comp_x is non-constant along b̃}.

## 1. Lemma 1 (time-t criterion for MS6)

**Lemma 1.** Fix t. Suppose there are:
- a point P ∈ B_t,
- a lift P̃ ∈ Def(P),
- a Y_t-copy y of P̃,
- a lift c̃ through P̃ of a boundary branch c at P,

such that y ∈ M(S_c̃), or y is intact for S_c̃ and comp_y is non-constant along c̃. Then the MS6 configuration exists at time t.

*Proof.*
1. Let E be the piece at time t that contains c̃. Concretely, E is the irreducible component, in ∏_w M_w of the stratum Δ_{G_c}, of the lift of closure(V_t) ∩ Δ_{G_c} that contains the image of c̃. Here the stratum locus S_c̃ of Def(P) is mapped to ∏_w M_w by taking partial normalizations. This is compatible with ξ_{G_c}, after identifying G_P / (E(G_P) \ S_c̃) with G_c.
2. P is not in Δ_{G_c}. So the endpoint of c̃ corresponds to a puncture p of Ē.
3. Let u be the vertex of G_c that contains y. Then f_u(p) is the curve obtained by gluing the components comp_x(P̃), x ∈ u, along the unpinched edges between them.
   - comp_y(P̃) is an irreducible component of f_u(p).
   - Its special points in f_u(p) are its special points in P. A half-edge at y is either part of an unpinched edge inside u, which becomes a node of f_u(p), or a half-edge of a pinched edge, which becomes a marked point of M̄_u.
   - So it is a Y_t-copy.
4. **Case y merged.** f_u(p) has a node, so f_u(p) ∈ ∂M̄_u. On E the values of f_u lie in M_u. So f_u is not constant. This is Lemma C2 of PR-C.
5. **Case y intact.** u = {y}, and f_u = comp_y along c̃ is non-constant by hypothesis. In both cases (E, u, p) is an MS6 configuration at time t. ∎

**Remark.** The converse does not hold in the relevant sense. A configuration "Y_t-copy y at an interior point P ∈ E, with the vertex of E carrying y non-constant" (called **MOV-interior** below) is NOT an MS6 configuration. At an interior point there is no puncture, and the moving value lies on a curve, not in a finite set.

## 2. Lemma 2 (transport of branch patterns)

**Lemma 2.** Let Q ∈ B_0 and let b be a boundary branch at Q. Put N := H((b \ {Q}) × Δ) near (Q,0). Then:
- (a) the components of q^{-1}(N) ⊂ Def(Q) × Δ are permuted transitively by 𝔅, and the pattern is constant on each of them. So the components are the a Ñ, with patterns a S, where Ñ ⊃ b̃ has pattern S = S_b̃;
- (b) for every t and every lift Q̃_t of Q_t, some a Ñ has Q̃_t in the closure of its t-slice. For that a, the lift of the branch H_t(b) through Q̃_t has pattern a S;
- (c) the closure of N near (Q,0) is a union of irreducible 2-dimensional germs of an analytic set. The same holds for q^{-1}(N).

*Proof.*
(a) **Patterns are constant on components.**
- The sets {S(p) = S'} for distinct S' with isomorphic contracted graphs are pairwise disjoint.
- Each is relatively open in the union of all strata of that graph type, because a nearby point has fewer zero coordinates unless it is in the same stratum.
- So S(·) is locally constant on q^{-1}(N) ⊂ q^{-1}(Δ_{G_b} × Δ), and hence constant on each component.

**Transitivity.**
- q restricted to q^{-1}(N) is open and closed (finite quotient), and q^{-1}(N) is locally connected (semi-analytic). So each component maps onto N, which is connected: it is homeomorphic to a punctured disc times a disc.
- If Z_1, Z_2 were components with 𝔅Z_1 ∩ 𝔅Z_2 = ∅, take a point n ∈ N. Its fibre is a single 𝔅-orbit, and it would have to lie in both 𝔅Z_1 and 𝔅Z_2, a contradiction.

(b) Q_t ∈ closure(H_t(b)). Hence the closure of q^{-1}(H_t(b)) contains a point of q^{-1}(Q_t) = 𝔅 Q̃_t. By 𝔅-invariance it contains Q̃_t. Near Q̃_t the set q^{-1}(H_t(b)) is contained in ⋃_a (a Ñ)_t. Apply (a).

(c) **The set 𝒜.** Let 𝒜 := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ). It is analytic by (R1). Let 𝒵 be the part of 𝒜 over strata deeper than Δ_{G_b}; it is analytic.

**N is open and closed in 𝒜 \ 𝒵.**
- Near (Q,0), 𝒜 \ 𝒵 = H((closure(V_0) ∩ Δ_{G_b} ∩ U) × Δ) by (R2).
- For U small, closure(V_0) ∩ Δ_{G_b} ∩ U is a disjoint union of punctured branches at Q, since Q ∉ Δ_{G_b}.
- So N is open and closed in 𝒜 \ 𝒵.

**Conclusion.**
- Let X be an irreducible component of 𝒜 not contained in 𝒵. The set X minus (𝒵, Sing 𝒜, and the other components) is connected and dense in X.
- Hence the closure of a union of connected components of 𝒜 \ 𝒵 is a union of such X.
- Preimages under the finite map q of analytic sets are analytic. ∎

## 3. Theorem 3 (total-merge transport)

**Theorem 3.** Let Q ∈ B_0. Assume:
- (Y) there is a sequence t_n → 0, t_n ≠ 0, such that Q_{t_n} has a Y_{t_n}-copy;
- (TM) for every y ∈ C_0(Q) there is a boundary branch b at Q, with a lift b̃, such that 𝔅·y ⊂ M^+(b̃).

Then for all but finitely many n, the MS6 configuration exists at time t_n. In particular MS6 holds, with T = {t_n : n ≥ n_0} minus a finite set. T accumulates at 0 ∈ Δ.

Hypothesis (Y) holds whenever Q ∈ closure(∂V_0), as shown in the proof.

*Proof.*
1. **Hypothesis (Y) for Q ∈ closure(∂V_0).**
   - Q_t ∈ closure(∂V_t), because H_t commutes with closures and preserves Δ_Γ.
   - Take a branch of ∂V_t at Q_t, and lift it to Def(Q) through a lift Q̃_t. Along it, the vertex-i curve is the constant Y_t ∈ M_{g_i,n_i}.
   - In the chart, the vertex-i curve converges to the curve glued from the components over the contracted vertex. That curve is Y_t, which is smooth, so it is a single component (Lemma D(1) of PR-I; re-checked).
2. **Choice of a limit copy.** Fix lifts Q̃_{t_n} and Y_{t_n}-copies y_n.
   - Pass to a subsequence along which y_n = y is constant and the ordering of special points is fixed.
   - Q̃_{t_n} → 0, and comp_y is continuous. M_{g_i,n_i} is Hausdorff and Y_{t_n} → Y_0 (PR-A). So comp_y(0) ≅ Y_0, i.e. y ∈ C_0(Q).
   - Arguing by contradiction on subsequences, it suffices to show that MS6 holds at t_n for all large n in this subsequence.
3. **Applying (TM).** Take b, b̃ as in (TM) for this y.
   - By Lemma 2(b), at time t_n there is a lift of H_{t_n}(b) through Q̃_{t_n} with pattern a_n S_b̃, lying in a_n Ñ.
   - Pass to a subsequence with a_n = a. Then a^{-1} y ∈ 𝔅y ⊂ M^+(b̃).
4. **Case a^{-1}y ∈ M(S_b̃).** Then y ∈ M(a S_b̃): y is merged along the lift through Q̃_{t_n}. Lemma 1 gives MS6 at t_n. (Q_{t_n} ∉ Δ_{G_b}, because H_t preserves strata.)
5. **Case a^{-1}y intact, with comp_{a^{-1}y} non-constant along b̃.** Then y is intact for a S_b̃, and comp_y is non-constant along a b̃.
   - Let W̃ be any irreducible germ of closure(a Ñ) at (0,0) (Lemma 2(c)). φ := comp_y is holomorphic on W̃, because y is intact for the constant pattern a S_b̃.
   - t is non-constant on W̃, so W̃_0 has pure dimension 1 (Krull). Its components are lifts a′b̃ with a′S_b̃ = a S_b̃, and along each of them φ = comp_{a′^{-1}y} along b̃.
   - a′^{-1}y ∈ 𝔅y is intact for S_b̃, so it is not in M(S_b̃). Hence comp_{a′^{-1}y} is non-constant along b̃. So φ is non-constant on every component of W̃_0.
6. **Generic rank of Φ = (φ, t) on W̃ is 2.**
   - Otherwise every fibre of Φ has dimension ≥ 1 at every point (semicontinuity of fibre dimension).
   - The fibre of Φ through a point of W̃_0 \ {0} lies in W̃_0 ∩ {φ = const}, which is 0-dimensional there. Contradiction.
7. **Only finitely many bad times.**
   - The set Σ := {p ∈ W̃ : dim_p Φ^{-1}Φ(p) ≥ 1} is analytic (Cartan–Remmert, cited from memory). It is a proper subset, so dim Σ ≤ 1.
   - So only finitely many 1-dimensional components of Σ lie in t-fibres, and φ is non-constant on W̃_t for t outside a finite set.
   - There are finitely many germs W̃. So for large n, φ is non-constant along the lift through Q̃_{t_n}, and Lemma 1 (intact case) gives MS6 at t_n. ∎

**Corollary 3′.** If 𝔅 = Aut(Q) fixes every element of C_0(Q), then (TM) reads: every Y_0-copy of Q is merged, or is intact and moving, along some boundary branch at Q. Hence MS6 holds if some Q ∈ closure(∂V_0) with this property exists.

**How Theorem 3 relates to Prop K and to PR-I.**
- Prop K (PR-H) produces a MERGE or MOV branch at a point Q_0 for the *path-marked* copy x_0 only. In general:
  - (G1) Q_0 ∉ closure(∂V_0), so (Y) is not automatic;
  - (G2) other Y_0-copies at Q_0, or 𝔅-translates of x_0, need not be merged (TM fails);
  - (G3) the MOV branch may have Q_0 in its own stratum (MOV-interior), which is excluded from M^+.
- In the quintic example of PR-I (not smooth), at P_0 = A—B—C one has C_0 = {A, C}, branch β (S = {e_1}) with M = {B, C}, and branch β′ (S = {e_2}) with M = {A, B}.
  - If Aut(P_0) does not swap A and C, (TM) holds and Theorem 3 applies.
  - If it does swap them, (TM) fails, and one needs PR-I's Krull-at-time-t argument (Lemma D) instead.
- So Theorem 3 does not supersede PR-I's Theorem 4. It is a different sufficient condition.

## 4. Lemma 4 (spreading of Y_t-copies at a time t where MS6 fails)

Call a coarse piece D (an irreducible 1-dimensional component of closure(V_t) ∩ Δ_G) **MOV-blocked at P** if P ∈ D and no vertex of a lift of D that is constant along D takes a value at P isomorphic to Y_t.

**Lemma 4.** Fix t, and suppose there is NO MS6 configuration at time t. Let P ∈ B_t have a Y_t-copy, and let D be a coarse piece with P ∈ closure(D). Assume that either
- (a) P ∉ D, or
- (b) P ∈ D and D is not MOV-blocked at P.

Then some lift-piece E of D has a vertex u with f_u ≡ const ≅ Y_t, and every point of closure(D) has a Y_t-copy.

*Proof.*
1. **Case (a).** Lift a branch of D at P to Def(P) through a lift P̃ carrying a Y_t-copy y. This is possible by the argument of Lemma 2(b) at fixed t.
   - Since MS6 fails at t, Lemma 1 says that y is intact for the branch pattern, and that comp_y is constant along the branch.
   - So the vertex u = {y} of the lift-piece E containing the branch has f_u constant on a branch, hence on E by the identity theorem on Ē. Its value is comp_y(P̃) ≅ Y_t.
2. **Case (b).** The vertex given by the hypothesis is constant along D with value ≅ Y_t.
3. **Every point of closure(D) has a Y_t-copy.**
   - ξ_G(E) = D, since ξ_G(E) ⊂ D, both are irreducible, and ξ_G(E) contains a branch of D.
   - Every R ∈ closure(D) is ξ̄_G(ν(r)) for some r ∈ Ē, and the u-coordinate of ν(r) is the smooth curve Y_t ∈ M_u.
   - So R has a component ≅ Y_t, carrying the same special points as in the proof of Lemma 1. ∎

**Corollary 4′.** Let B_t^∂ be the connected component of B_t containing ∂V_t. Note B_t^∂ = H_t(B_0^∂). Suppose MS6 fails at t and no coarse piece in B_t^∂ is MOV-blocked at a point of B_t^∂. Then:
- every point of B_t^∂ has a Y_t-copy;
- every coarse piece in B_t^∂ has a lift with a vertex that is constant and ≅ Y_t.

*Proof.*
1. B_t^∂ is a finite union of closures of coarse pieces. A compact analytic set of dimension ≤ 1 has 1-dimensional irreducible components, each the closure of the piece of its generic stratum, together with isolated points. The component containing the 1-dimensional set ∂V_t is a union of the former, and their incidence graph (two pieces adjacent if their closures meet) is connected.
2. Start from the pieces of ∂V_t, whose vertex i is ≡ Y_t, and apply Lemma 4 along the incidence graph. ∎

**What Lemma 4 shows.** If MS6 fails, the Y_t-copies are never "lost" at a puncture. They can be lost only at MOV-blocked incidences, i.e. MOV-interior configurations. They can also be carried by a component different from the one at t = 0 (twins). Lemma 4 is purely a time-t statement and uses neither total geodesy nor L2.



### R8-2 (excerpt). Lemma U, the generic-time trichotomy (Theorem 1), Theorem S (MS8 under (NB),(NB_∂)) (from round8_q2, verbatim, §§1–4)
## 1. Conventions and cited facts

- Classes of pointed curves are compared in the coarse space 𝔐 := M_{g_i,n_i}/S_{n_i}. "≅ Y" means equal class.
- For a stable graph G, 𝓦_G ⊂ ∏_w M̄_w × Δ is the lifted family of R7-5 (P2). It is analytic by (R1) and proper over Δ. "W" always denotes a 2-dimensional irreducible component of some 𝓦_G.
- By R7-5 (P4), applied at every t (the argument is symmetric in t by (R2), and closure(V_t) is compact analytic by (R1)): every fibre W_t is non-empty and of pure dimension 1. Each 1-dimensional component D of W_t is the closure of a piece E at time t, so (Rig) applies to E. Write M(D) := M(E) and K(D) := K(E).
- Cited from memory (standard):
  - **Remmert's proper mapping theorem.**
  - **Cartan–Remmert.** For a holomorphic map Φ of complex spaces, {x : dim_x Φ^{-1}Φ(x) ≥ k} is analytic.
  - **Stein factorization** (Grauert–Remmert). A proper holomorphic map f: X → S factors as X → T → S, with X → T proper, surjective and with connected fibres, and T → S finite. If X is normal, so is T.
  - **Normal surfaces** have isolated singularities.

## 2. Lemma U (uniformity under (Rig)) — proved

**Lemma U.** Assume (R1), (R2) and (Rig). Let W be a 2-dimensional irreducible component of 𝓦_G. There are a set M_W ⊂ V(G) and an irreducible closed curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, with the following property. For **every** t ∈ Δ and **every** 1-dimensional component D of W_t:
- M(D) = M_W and K(D) = K_W;
- every vertex u ∉ M_W is constant on D;
- D = K_W × {c_D} for a point c_D ∈ ∏_{u∉M_W} M_u.

*Proof.*

**Step 1 (generic moving set).** Let n: W^ν → W be the normalization, a normal surface. Let W^ν →a T →b Δ be the Stein factorization of t∘n, which is proper. T is a normal, hence smooth, curve and b is finite.
- **Critical values are discrete.** Let C be an irreducible curve of critical points of a on W^ν_reg. Then d(a|_C) = 0, so a is constant on C. The singular points of W^ν are isolated. Hence the set of critical values of a (images of Sing W^ν, of isolated critical points, and of critical curves) is discrete in T.
- **Generic fibres are irreducible.** For τ ∈ T outside a discrete set, a^{-1}(τ) is a smooth, compact, connected curve, hence irreducible.
- **Fibres of W.** Since n is finite and surjective, for every t, W_t = ⋃_{τ ∈ b^{-1}(t)} n(a^{-1}(τ)). Every component of W_t is the image of a component of some a^{-1}(τ). For generic t the components of W_t are exactly the irreducible curves n(a^{-1}(τ)), τ ∈ b^{-1}(t).
- **The dichotomy for a vertex u.** Put Φ_u := (pr_u∘n, a): W^ν → M̄_u × T and R_u := {x : dim_x Φ_u^{-1}Φ_u(x) ≥ 1}, which is analytic by Cartan–Remmert.
  - If R_u = W^ν: let K be a component of a fibre a^{-1}(τ) and x ∈ K a point on no other component. The Φ_u-fibre through x lies in a^{-1}(τ) and is 1-dimensional at x, so it contains the germ of K at x. Hence pr_u is constant on K. So u is constant on every component of every fibre of a, and therefore on every component of every W_t.
  - If R_u ≠ W^ν: then dim R_u ≤ 1. Every fibre component on which pr_u is constant lies in R_u, and the components of R_u are locally finite. So this happens only for τ in a discrete subset of T.
- Put M_W := {u : R_u ≠ W^ν}. Then for t outside a discrete set Z_W ⊂ Δ, every component of W_t has moving set exactly M_W. For every t and every component of W_t, every u ∉ M_W is constant on it. M_W ≠ ∅, since components of W_t are curves.

**Step 2 (one image curve).** Let Σ := (pr_{M_W}, t)(W) ⊂ ∏_{u∈M_W} M̄_u × Δ. It is closed, analytic and irreducible (Remmert; the map is proper on W). It has dimension 2, since t is non-constant on it and its generic fibres are curves.
- For t ∉ Z_W and a component D of W_t, pr_{M_W}(D) is the closure of the image of the piece, i.e. K(D).
- By (Rig), K(D) belongs to the finite list {α^{-1}K : α ∈ Aut(G), (G, αM_W, K) ∈ 𝒦}, with factors relabelled by α. Call its members K_1, …, K_N.
- So Σ ∩ {t ∉ Z_W} ⊂ ⋃_j K_j × Δ, and by closedness Σ ⊂ ⋃_j K_j × Δ.
- Σ is irreducible of dimension 2, so it lies in one K_j × Δ, and equals it since both are irreducible of dimension 2. Put K_W := K_j.
- For each u ∈ M_W, pr_u|_{K_W} is non-constant, because K_W = K(D) for a generic-time component D with u ∈ M(D).

**Step 3 (all times).** Let t be arbitrary and D a component of W_t.
- By Step 1 the vertices outside M_W are constant on D. So D ⊂ pr_{M_W}^{-1}(pr_{M_W}(D)) ∩ {coordinates outside M_W constant}.
- pr_{M_W}(D) ⊂ Σ_t = K_W is closed and irreducible, so it is a point or all of K_W. If it were a point, every coordinate would be constant on the curve D, which is absurd.
- So pr_{M_W}(D) = K_W. Every u ∈ M_W is non-constant on D (end of Step 2), so M(D) = M_W and K(D) = K_W.
- D is an irreducible curve inside the irreducible curve K_W × {c_D}, so the two are equal. Here c_D ∈ ∏ M_u, because D is the closure of a subset of ∏_w M_w and the coordinates of c_D are constant on D. ∎

**Corollaries.**
- **U1 (L1′ with its converse; no non-product pathology).** For each W and vertex u, the following are equivalent:
  - u is constant on one component of one fibre;
  - u ∉ M_W;
  - u is constant on all components of all fibres.

  In particular the situation of R7-5 §1.4 (u constant on E_0 but non-constant on σE_0 inside the same W) cannot occur under (Rig). Consequently, for a component W' through a point p obtained from W by ρ ∈ Aut(G): M_{ρW} = ρM_W and K_{ρW} = ρK_W.
- **U2 (t-independent image curves; the earlier worker's Lemma 6, repaired).** The partial file's Lemma 6 asserts that "M is the same for all t by L1′". L1′ gives only one direction, and for non-product G the fibres of W can have components with different moving sets unless (Rig) is used as above. Lemma U is the correct statement.
- **U3 (puncture values).** For each W, the values pr_{M_W}(ν(p)) at punctures p of components of W_t lie in K_W ∩ ∂(∏ M̄_u). This is a finite set independent of t.
- **U4 (constant-vertex value curves).** For u ∉ M_W, Γ_{W,u} := (pr_u, t)(W) is an irreducible curve, finite over Δ. Its fibre over t is the set of values of u on the components of W_t.

## 3. Generic times and the trichotomy (Theorem 1) — proved

From now on assume, for contradiction, that **Y is non-constant**. Y: Δ → 𝔐 is holomorphic by PR-A, so its graph is an irreducible curve.

**The finite set 𝔉 ⊂ 𝔐 (independent of t).**
- Let 𝒫_1 be the set of points of K ∩ ∂(∏_{u∈M} M̄_u), over all (G, M, K) ∈ 𝒦 and all Aut(G)-relabellings. It is finite: K is an irreducible compact curve not contained in the boundary.
- Let A_1 be the set of classes of the smooth components, with their special points, of all coordinates of points of 𝒫_1.
- Let 𝒫_2 be the set of points κ ∈ K such that the class of some coordinate pr_z(κ), z ∈ M, lies in A_1. It is finite, because pr_z|_K is non-constant for z ∈ M (Lemma U).
- Let 𝔉 be the set of classes of the smooth components of all coordinates of the points of 𝒫_1 ∪ 𝒫_2.

**The set Z.** Z is the set of t ∈ Δ such that one of the following holds:
- Y_t ∈ 𝔉;
- (Y_t, t) lies on the image in 𝔐 × Δ of some curve Γ_{W,u} (u ∉ M_W, M_u of type (g_i,n_i)) that is not the graph of Y.

Each W, and each such pair (W,u), contributes a discrete set: in the first case because Y is non-constant, in the second because two distinct irreducible curves meet discretely. The components W are locally finite over Δ. Hence **Z is discrete** in Δ.

Call a pair (W,u) with Γ_{W,u} ↦ graph(Y) a **Y-vertex**.

**Theorem 1.** Let t ∉ Z, Q ∈ B_t, q a lift of Q in Def(Q), and y a Y_t-copy of q (comp_y(q) ≅ Y_t). Let b̃ be a lifted branch through q of a branch b of B_t at Q. Let E be the piece of b at time t, with graph G_b and component W ⊃ E. Then exactly one of the following holds.
- **(STAY)** Every edge at y is pinched along b̃, y is a constant vertex of E, and (W, y) is a Y-vertex.
- **(IMOV)** Q is an interior point of E (so Q ∈ Δ_{G_b}), and y ∈ M_W. Moreover, for every z ∈ M_W and every other lifted branch b̃′ through q, z is neither merged along b̃′ nor non-constant at a puncture along b̃′.

In particular, a Y_t-copy is never merged along a branch (**MERGE excluded**), and never intact and non-constant at a puncture (**puncture-MOV excluded**).

*Proof.*
1. **Merge.** Suppose some edge at y is unpinched along b̃. By R7-1 Lemma 1(a) (= R7-4 Lemma 1), the point p of Ē over Q is a puncture, the vertex u ∋ y of G_b is non-constant, and comp_y(q) is a component, with the same special points, of f_u(p).
   - By Lemma U, u ∈ M_W and pr_{M_W}ν(p) ∈ 𝒫_1.
   - So Y_t ∈ A_1 ⊂ 𝔉, contradicting t ∉ Z.
2. **Puncture-move.** Suppose y is intact, {y} is non-constant, and Q ∉ Δ_{G_b}. Then p is a puncture and f_y(p) = comp_y(q) (R7-1 Lemma 1(b)). So Y_t ∈ A_1, again a contradiction.
3. **Constant.** Suppose y is intact and constant on E. Its value is comp_y(q) ≅ Y_t, so (Y_t, t) lies on the image of Γ_{W,y}. Since t ∉ Z, Γ_{W,y} maps onto graph(Y): this is STAY.
4. **Remaining case.** Here y is intact and non-constant, and Q ∈ Δ_{G_b}. So y ∈ M_W, and κ := pr_{M_W}(lift of Q) ∈ K_W.
   - Suppose some z ∈ M_W were merged, or moving at a puncture, along another branch b̃′ through q. Then, as in 1–2, comp_z(q) = pr_z(κ) has class in A_1. So κ ∈ 𝒫_2, and Y_t ≅ pr_y(κ) lies in 𝔉, a contradiction. ∎

**Remark.** Theorem 1 never compares two copies. At a generic t, *every* Y_t-copy obeys it, whatever the automorphisms of Q. Twins matter only when information is transported between t = 0 (where total geodesy is available) and generic t. That is the subject of §4.

## 4. Theorem S: the twin problem is a monodromy problem (conditional; partial)

### 4.1 Where the twin problem sits

Proposition K follows the subsurface Σ_i ⊂ S_g with a **marking** along an interior path γ ⊂ V_0, i.e. a lift γ̃ to T_g. R7-6 tried to carry this to time t by transporting along τ ↦ H_τ(γ(s)). As the planner noted, this needs the transported markings to be coherent in s, i.e. the square

 F(s,τ) := H_τ(γ(s)),  s ∈ [0,1], τ ∈ [0,t],

must lift to T_g × Δ. Two markings of the same surface differing by a mapping class g send Σ_i to different subsurfaces. In chart terms, the merged copy and the copy that stays ≅ Y_t differ by an automorphism α of the end point. This is exactly the twin swap of R7-2 §4.1 and R7-3 §4. So the twin problem is the monodromy of ∂F, and it can come only from **branch points of the covering 𝒱̃ → 𝒱** met by F. Below I show:
- (i) branch points over t = 0 are harmless, even if every curve of V_0 has automorphisms that disappear for t ≠ 0;
- (ii) the remaining ones matter only if they accumulate on K_0 × {0}.

That is hypothesis (NB). A similar issue inside boundary strata (Aut(G)-branching of the lifted boundary families) is controlled by Lemma U up to a coincidence condition, (NB_∂).

### 4.2 Definitions and the input from t = 0

- 𝒱̃ ⊂ T_g × Δ is the preimage of 𝒱 (Mod_g acts trivially on Δ). A point v ∈ 𝒱 is **regular** if it has a neighbourhood U such that every connected component of the preimage of U maps homeomorphically onto U. Over the open set 𝒱^reg of regular points, 𝒱̃ → 𝒱 is a covering map. The preimage of a small neighbourhood of any point of 𝒱 is a disjoint union of neighbourhoods of the (finitely many modulo Mod_g) fibre points, because Mod_g acts properly discontinuously.
- **Input (K\*+).** This is (K\*) of R7-6 §2.0 (Proposition K, PR-H §3, "proved modulo routine marking details"; not re-verified here), with the special set Sp ⊂ K_0 of R7-6, plus one robustness clause. For every ρ > 0 and every function θ : b \ {Q_0} → (0,∞) there are a marked path γ̃ (projecting to γ ⊂ V_0) and Q′ ∈ b \ {Q_0} satisfying (K\*)(a)–(c) with ρ, and in addition d(γ(1), Q′) < θ(Q′).
  - The clause reflects the two-step limit in Proposition K: first fix k, which fixes the end point Q′ = Q_k ≠ Q_0 at which γ_e has extremal length δ_k > 0; then let n → ∞, so the ray segments approach Q_k.
  - The path γ̃ is a Teichmüller ray segment, so it lies in one Teichmüller disc, hence in one irreducible component S of the preimage of V_0 in T_g.
- **(Ch), (Tr)** denote the chart lemma and the transport of vanishing data of R7-6 §2.1. They are used only at points of compact subsets of strata, at a fixed time t, with ρ chosen after t. This is the setting in which R7-6's proofs of them are routine.

**Hypotheses.**
- **(NB)** There are t_1 > 0 and an open neighbourhood 𝒪 of K_0 × {0} in closure(𝒱) such that every point of 𝒪 ∩ 𝒱 with 0 < |t| < t_1 is regular.
- **(NB_∂)** For every stable graph G, every 2-dimensional component W of 𝓦_G, every w ∉ M_W and every u ∈ M_W with M_w, M_u of type (g_i,n_i): the image of Γ_{W,w} in 𝔐 × Δ is not contained in pr_u(K_W) × Δ (classes in 𝔐). Equivalently, by irreducibility, the set D_∂(W,w,u) of τ at which some value of w on a component of W_τ has the class of a point of pr_u(K_W) is discrete. Let D_∂ be the union of these sets, which is discrete.

**Theorem S.** Assume the hypotheses of MS8 (with (R1), (R2), (Rig)), the input (K\*+) with end point of type MERGE or puncture-MOV, and (NB) and (NB_∂). Then Y_t = Y_0 for all t ∈ Δ.

No hypothesis on twins ((NT\*), (Lock)) is made.

### 4.3 Proof of Theorem S

Suppose Y is non-constant. Let Z be as in §3.

**Step 0 (choice of t).** Choose t ≠ 0 with the following properties.
- |t| < t_1, and |t| is small enough that, for the finitely many charts Def(z) used in Steps 3–5, H_τ(z) stays in the chart of z for τ ∈ [0,t].
- |t| is small enough that the finite exceptional set of R7-4 Theorem 3, steps 5–7, for the germs of closure(Ñ) at the end point (Step 5) is avoided.
- t ∉ Z.
- The segment [0,t] meets D_∂ only at 0 (possibly). Since D_∂ ∩ {|τ| ≤ t_1/2} is finite, only finitely many directions arg t are excluded.

Z is discrete, so such t exist. From now on t is fixed. All smallness requirements on ρ, θ below may depend on t.

**Step 1 (the path).** Take γ̃ ⊂ S from (K\*+) with ρ small.
- Let Bad ⊂ S be the proper analytic subset consisting of:
  - Sing(S);
  - the branch locus of S → V_0 (points with non-trivial stabilizer in Stab(S)/ker);
  - the sets S ∩ hS with hS ≠ S (all components of the preimage of the irreducible V_0 are translates of S).
- At each of its points, the Teichmüller disc containing γ̃ lies in a single local irreducible branch of S. In that branch the complement of Bad is connected and dense. So γ̃ can be perturbed, inside S and uniformly close to it in the Teichmüller metric, to a path avoiding Bad.
- Conditions (K\*)(a)–(c) are open conditions on the marked path, after replacing ρ by 2ρ. So they survive the perturbation. Keep the names γ̃, γ.
- Since γ avoids the image of Bad, a lift of γ to the preimage of V_0 is determined by its initial point.

**Step 2 (the square lifts).** For ρ small, γ ⊂ 𝒰′, where 𝒰′ is a neighbourhood of K_0 in closure(V_0) with H(𝒰′ × {|τ| ≤ |t|}) ⊂ 𝒪 (compactness, H continuous, H_0 = id).
- The half-open square F|_{[0,1]×(0,t]} lies in 𝒪 ∩ 𝒱 ∩ {0 < |τ| < t_1} ⊂ 𝒱^reg by (NB). It is simply connected, so it lifts to 𝒱̃.
- **Extension to τ = 0.** Fix s. The preimage of a small neighbourhood of (γ(s), 0) is a disjoint union of neighbourhoods of fibre points. The connected set F([s−δ, s+δ] × (0,δ]) lifts into one of them. Hence the lift extends continuously to τ = 0, and the extension is a continuous lift of γ into the preimage of V_0.
- Translate the whole lift by a deck element so that the extension starts at γ̃(0). By the uniqueness in Step 1, the extension equals γ̃.
- Over t = 0 the covering may branch along all of V_0 × {0}. This happens when every curve of V_0 carries automorphisms that disappear for t ≠ 0, as in the local model t = u^m of a deformation off a fixed locus. Such branching does no harm here: it lies on the boundary edge of the square only.
- **Consequence.** For every s, the *top-edge marking* of H_t(γ(s)) (continuation along s at time t) equals the *τ-transport* of the marking γ̃(s) along τ ↦ H_τ(γ(s)). In particular, R7-6's coherence gap does not arise.

**Step 3 (the class along arcs is a constant-vertex value).** Fix r > 0 smaller than half the minimal distance between points of Sp, and small for the charts at Sp.
- For s with d(γ(s), Sp) < 2r, take z_s ∈ Sp.
- Otherwise take z_s ∈ K_0 with d(γ(s), z_s) < ρ; then d(z_s, Sp) > r.
- Let c(s) ∈ 𝔐 be the class of the component of H_t(z_s) onto which Σ_i collapses, in the marking of Step 2. It is well defined for ρ small by (Tr), and up to o(1) as ρ → 0 independent of the choice of z_s, by (Ch).

*(a) Special points.* If z_s = J ∈ Sp, then c(s) is the class of a component of H_t(J): finitely many values.

*(b) Arc points.* Let K^r := K_0 \ (r-neighbourhood of Sp), a compact set of non-special points, each a smooth point of a piece. Cover K^r by finitely many charts Def(z_k) × Δ (z_k ∈ K^r, stratum G_k, piece D_k). The charts are so small that, in chart k, Σ_i corresponds for all points z of the chart to one chart label w_k, with comp_{w_k} ≅ Y_0 at the lift p^0_z of z selected by the marking at τ = 0 ((K\*)(b)). Consider the lifts of the points H_τ(z), z ∈ K^r ∩ chart k, τ ∈ [0,t]. They lie on the lifted boundary family of 𝒜_k := closure(𝒱) ∩ (Δ_{G_k} × Δ), whose 2-dimensional components W′ are as in Lemma U. Put:
- G′ := lifts lying on some W′ with w_k ∉ M_{W′};
- B′ := lifts lying on some W″ with w_k ∈ M_{W″}.

Both sets are compact. Every lift lies in G′ ∪ B′.

**Claim.**
- (i) G′ ∩ B′ ∩ {τ ∈ (0,t]} = ∅.
- (ii) At τ = 0, every point of B′ has comp_{w_k} ≇ Y_0. Hence B′ ∩ {τ = 0} stays at distance ≥ δ′ > 0 from the compact set of lifts with comp_{w_k} ≅ Y_0, which contains every p^0_z.

*Proof.*
- **The lifted fibre components through a point.** Let p be a lift of H_τ(z), z ∈ K^r. The fibre components through p are lifted branches of the germ of H_τ(D_k) at H_τ(z). This germ is unibranch: H_τ is a stratified homeomorphism and z is a smooth point of D_k, so the germ has a punctured neighbourhood homeomorphic to a punctured disc. Hence these fibre components are Stab(p)-translates of one another. So if W′, W″ both pass through p, there is σ ∈ Stab(p) with M_{W″} = σM_{W′}, by Lemma U applied to the fibre components through p.
- **(i).** Let p ∈ W′ ∩ W″ with w := w_k ∉ M_{W′}, w ∈ M_{W″} = σM_{W′}, over τ ∈ (0,t]. Then σ^{-1}w ∈ M_{W′} is moving on W′ while w is constant there. Since σ fixes p, comp_{σ^{-1}w}(p) ≅ comp_w(p). Here comp_w(p) is the value of w on the component of W′_τ through p, and comp_{σ^{-1}w}(p) lies in pr_{σ^{-1}w}(K_{W′}) (Lemma U). So τ ∈ D_∂(W′, w, σ^{-1}w), contradicting Step 0.
- **(ii).** Let p ∈ B′ at τ = 0 with comp_w(p) ≅ Y_0. Then w is a moving vertex of a lifted branch of D_k through p (the fibre component of W″ through p), and its value at z is ≅ Y_0. So z ∈ Sp (R7-6's Sp contains the points of D ∩ K_0 at which a non-constant vertex has class Y_0). This contradicts z ∈ K^r. The distance statement follows by compactness and continuity of comp_w on the stratum locus. ∎

**Consequence.** By (i), (ii) and compactness, there are τ_0 > 0 and δ_t > 0 such that:
- for τ ∈ [0, τ_0], B′ ∩ {τ ≤ τ_0} lies within δ′/4 of B′ ∩ {τ = 0} (upper semicontinuity for the compact set B′), and X̃_τ stays within δ′/4 of X̃_0 (uniform continuity of H and of the chart lift). So X̃_τ keeps distance ≥ δ′/4 − ε from B′;
- for τ ∈ [τ_0, t], G′ and B′ are at distance ≥ δ_t from each other (disjoint compact sets, by (i)).

The τ-transported marked surface X̃_τ (chart lift, continuous in τ) stays within ε = ε(ρ) of some lift of H_τ(z), by (Tr), and starts near p^0_z ∈ G′ \ B′. For ε < min(δ_t, δ′)/4, continuity forces X̃_τ to stay near G′ for all τ ∈ [0,t]. At τ = t, therefore, c(s) is, up to o(1), comp_{w_k} at a point of G′, i.e. the value of the constant vertex w_k on a component of some W′_t. These values form a finite set.

*(c) The finite set.* Let S_t be the union of:
- the classes of values of constant vertices on components of W_t, over all W;
- the classes of components of H_t(J), J ∈ Sp.

S_t is finite and contains Y_t. Let 2g_t > 0 be the minimal distance between distinct elements of S_t (in a fixed metric on the compactification of 𝔐). By (a), (b): for ρ small, every c(s) lies within g_t/4 of S_t.

**Step 4 (c is constant, equal to Y_t).**
- **Near-continuity.** By (Ch) applied at time t (finitely many charts covering H_t(K_0); Lebesgue number; ρ small), |c(s) − c(s′)| < g_t/4 whenever |s − s′| is small. Hence the element of S_t near c(s) is locally constant, so constant on [0,1].
- **Start.** P ∈ Sp, and for γ(0) near P we take z_0 = P. In Def(P), Σ_i ↔ the chart label i ((K\*)(a)).
  - Δ_Γ is of product type and dim M_{g_i,n_i} > 0, so every automorphism of a curve in Δ_Γ fixes the vertex i. (A graph automorphism moving i would act non-trivially on ∏_w M_w while ξ_Γ is injective.) Hence comp_i takes the same value at all lifts of P_t = H_t(P) ∈ ∂V_t.
  - That value is the vertex-i coordinate Y_t. So c(0) = Y_t.
- **Conclusion.** Hence c(1) = Y_t.

**Step 5 (the end point).** Work in Def(Q_0) × Δ. Let Ñ be the component of q^{-1}(H((b \ {Q_0}) × Δ)) containing b̃ \ {0}. Here b̃ is the lifted branch near which γ̃(1) lies, and along b̃ the chart label x of Σ_i is merged (MERGE) or intact and moving (MOV), by (K\*)(b),(c).
- **The right edge stays near Ñ.** Distinct components of q^{-1}(H((b∖Q_0)×Δ)) are disjoint. So the lifts of H_τ(Q′), τ ∈ [0,t], lying in Ñ and in the other components are at distance ≥ δ(Q′) > 0. Choose θ(Q′) ≪ δ(Q′) in (K\*+). Then the τ-transport of γ̃(1), i.e. the right edge of the lifted square, stays near Ñ_τ, with Σ_i ↔ x throughout.
- **The top edge ends at a lift of Q_t on that branch.** By Step 2 the top-edge marking at s = 1 is this one. As ρ → 0, Q′ → Q_0, so d(H_t(Q′), Q_t) becomes small compared with the separation of the (fixed) lifts of Q_t. So the end point lies near a lift q of Q_t, and the lifted branch of H_t(b) through q containing the lift of H_t(Q′) is a branch of closure(Ñ_t). Its pattern is the constant pattern S_b̃ of Ñ.
- **x is a Y_t-copy at q.** By Step 4, comp_x(q) ≅ c(1) = Y_t.
- **MERGE.** x is merged along a branch at q. Theorem 1 (merge excluded) gives Y_t ∈ 𝔉, so t ∈ Z, contradicting Step 0.
- **Puncture-MOV.** x is intact along the branch. By R7-4 Theorem 3, steps 5–7 (applied to the germs of closure(Ñ) at (0,0), with t outside their finite exceptional set by Step 0), comp_x is non-constant along it, and Q_t ∉ Δ_{G_b}. Theorem 1 (puncture-MOV excluded) gives a contradiction.

Hence Y is constant. ∎

### 4.4 Remarks on Theorem S

1. **What replaces (Lock) / (NT\*).** Neither is assumed. Twins at junction points are harmless as long as the square lifts, because the class c(s) is then read off in one coherent marking at time t. This is exactly R7-6's "why twins do no harm" remark, now with its gap closed by (NB).
2. **(NB) is a statement about new orbifold points only.** Branching along V_0 × {0} itself is allowed (Step 2). What (NB) forbids is a sequence of curves X_n ∈ V_{τ_n}, τ_n → 0, τ_n ≠ 0, with more automorphisms than the generic curve of the relevant sheet of 𝒱̃, converging to a point of K_0. By upper semicontinuity of |Aut| on M̄_g (cited from memory), the closure in M̄_g × Δ of the locus of such points is analytic (it is a union of components of an analytic set not contained in {t = 0}). Its t = 0 slice is a compact analytic set of dimension ≤ 1. So (NB) fails only if this slice meets K_0.
3. **(NB_∂) is a coincidence condition internal to single families W.** It fails only if, for some W, a constant vertex w and a moving vertex u of the same type satisfy: for every τ, the constant value of w lies on the fixed trace curve pr_u(K_W). For instance, in the quintic example (PR-I) the only family through ∂V_0 has M_W = {genus-4 vertex} and the constant vertex has genus 2. So the types differ and (NB_∂) holds there. I do not know how to exclude the coincidence in general.
4. **Interior-MOV end point.** Steps 0–4 work verbatim and give c(1) = Y_t. At the end, x is intact and non-constant along a branch through an interior point Q_t of E_{b,t}. That is an IMOV configuration of a Y_t-copy, which Theorem 1 allows. So Theorem S does not cover the crossing case (see §5).


### R8-3 (excerpt). Theorem N and Corollary T (Krull pair at one lift, any automorphisms) (from round8_q3, verbatim, §§0–4.1)
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


### R8-4 (excerpt). Lemma P, Lemma G, Corollary G1, Theorem 2V, twin jumps under (Rig) (from round8_q4, verbatim, §§1–3, §5)
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


### R8-1 (excerpt). Lemma S (sheets are topological and transported by H_t) (from round8_q1, verbatim, §4.1)
### 4.1 Lemma S (sheets are topological and are transported by H_t)
For Q ∈ B_t, the irreducible components ("sheets") of the germ of closure(V_t) at Q are in canonical bijection with the elements of lim← π_0(V_t ∩ W), taken over neighbourhoods W of Q and keeping only components whose closure contains Q. A boundary branch b at Q lies in the sheet corresponding to a component if b ∖ {Q} lies in the closure of that component, for all W.

Consequently H_t maps sheets at Q_0 bijectively onto sheets at H_t(Q_0), compatibly with the boundary branches they contain.

*Proof.*
- For an analytic germ (X, Q), the irreducible components correspond to lim← π_0(Reg(X) ∩ W). This is the standard local description: a germ is irreducible iff its regular part is locally connected at Q.
- Here X = closure(V_t), and Reg(X) ∩ W ∖ V_t lies in the 1-dimensional boundary. That set has real codimension 2 in the manifold Reg(X), so removing it does not change π_0.
- The description is purely topological in the pair (closure(V_t), V_t). By (R2), H_t is a homeomorphism of pairs (closure(V_0), V_0) → (closure(V_t), V_t) that preserves strata and pieces (PR-B). ∎


### R8-5. Twin step under (U_J): covering lemma, Theorems A and B, Corollary C, Proposition D (from round8_q5, verbatim, §§1–6)
## 1. Set-up and readings

I adopt the task's readings (R1) and (R2), with H_0 = id, and the setting of MS8. I add the following conventions.

**(C1) Charts (standard; cited from memory).** Let J be a stable curve.
- Def(J) is its versal deformation germ. Aut(J) acts on it, and we may take the action to be linear in suitable coordinates (Cartan).
- Fix an Aut(J)-invariant open ball B ⊂ Def(J) around 0 and an Aut(J)-invariant Hermitian norm |·|. Then q : B → U := B/Aut(J) is a neighbourhood of J in M̄_g.
- On U use the quotient metric d̄(q(p), q(p')) = min_α |p − α p'|. It induces the topology of U. Every lift of a point realises the distance to the orbit of any other point.
- s_e (e ∈ E(G_J)) are the smoothing parameters. B° := B ∖ {∏ s_e = 0} lies over U ∩ M_g.
- For a vertex y, L_y := {s_e = 0 for all edges e at y}. It is closed, and F_y : L_y → M_{g_y,n_y}/S_{n_y} (coarse) is continuous (holomorphic into the coarse space).
- For α ∈ Aut(J): α L_y = L_{αy} and F_y(αp) = F_{α^{-1}y}(p) (K3 of R7-3).
- On product sets B × Δ_ε, the map q × id is again written q.

**(C2) The track at a junction (reading of Proposition K / (K\*) of R7-6 / the interpretation in R7-3 §1).** Let J = J^k be a junction between D := D^{k−1} and D' := D^k. Let β̃ ⊂ Def(J) and β̃' ⊂ Def(J) be lifts of the branches of D and D' at J, and let x be a chart vertex with:
- c_{k−1} = {x} along β̃, and c_k = {x} along β̃';
- c_{k−1} constant on D and c_k constant on D'.

Shrinking B, assume B_0 ∩ U is a finite union of branches through J (cone structure). Fix generic points z̃_1 ∈ β̃ ∖ 0 and z̃_2 ∈ β̃' ∖ 0, and put z_j = q(z̃_j). The track datum (TD_J) is: for every ρ > 0 there are a path γ : [a,b] → V_0 ∩ U and a continuous lift γ̃ : [a,b] → B° such that:
- (T1) |γ̃(a) − z̃_1| < ρ and |γ̃(b) − z̃_2| < ρ;
- (T2) for every s there is z_s ∈ B_0 ∩ U with d̄(γ(s), z_s) < ρ, with z_a = z_1 and z_b = z_2;
- (T3) for every s with d̄(z_s, J) ≥ r_1 (r_1 > 0 arbitrary, fixed before ρ), there is a lift ẑ_s ∈ L_x of z_s with |γ̃(s) − ẑ_s| < ρ and F_x(ẑ_s) ≅ Y_0. One may take ẑ_a = z̃_1 and ẑ_b = z̃_2.

(T3) is the chart form of (K\*)(b): "Σ_i ↔ a single component of z_s of class Y_0". Here the region of γ̃(s) corresponding to Σ_i is the chart region x, which is constant along the continuous lift γ̃. Away from J the nearest lift of z_s is well defined up to the stabiliser, which is harmless; see Lemma 3. Proposition K yields (T1)–(T3) "modulo routine marking details" (PR-H). I have not re-proved Proposition K, and (TD_J) is the precise form in which I use it.

**(C3) The deformed family near J.**
- Put 𝒱_U := 𝒱 ∩ (U × Δ_ε) and ℬ° := B° × Δ_ε. Then q^{-1}(𝒱_U) ⊂ ℬ°.
- V_t is closed in M_g, so closure(𝒱) ∩ (M_g × Δ) = 𝒱.
- Let 𝒞° be the connected component of q^{-1}(𝒱_U) that contains γ̃ × {0}. Passing to a subsequence ρ_n → 0, it is the same for all the paths of (TD_J), because q^{-1}(𝒱_U) has finitely many components meeting a neighbourhood of 0. (I only use this for a single ρ at a time, so the subsequence is harmless.)
- Γ := {α ∈ Aut(J) : α𝒞° = 𝒞°}, and Γ_x := {α ∈ Γ : αx = x}.

**Fact 0.** q|_{𝒞°} : 𝒞° → 𝒜 := q(𝒞°) is the quotient map by Γ, and 𝒜 is a connected component of 𝒱_U.

*Proof.*
- q restricted to the saturated set q^{-1}(𝒱_U) is open and closed onto 𝒱_U. So q(𝒞°) is open, closed and connected, i.e. a component.
- If p, p' ∈ 𝒞° and q(p) = q(p'), then p' = αp for some α ∈ Aut(J). Then α𝒞° is a component of q^{-1}(𝒱_U) containing p', so α𝒞° = 𝒞°, i.e. α ∈ Γ. ∎

Let K ⊲ Γ be the kernel of the action of Γ on 𝒞°, i.e. the generic automorphisms of the family component. It is normal, so Γ_x^+ := K·Γ_x is a subgroup of Γ.

**Hypothesis (U_J).** After shrinking B and ε, every p ∈ 𝒞° satisfies Stab_Γ(p) ⊂ K·Γ_x.

(Generic twins, i.e. elements of K moving x, are thus allowed.)

In words: no curve of V_τ near J (|τ| < ε) in the family component 𝒜 has an automorphism, induced by an element of Aut(J), that maps the region x to a different region. Two remarks:
- (NT) at J (every σ ∈ Aut(J) fixes x) implies (U_J) trivially, since then Γ_x = Γ.
- (U_J) is a germ condition at (J, 0): it fails iff (0,0) ∈ closure(Fix(α) ∩ 𝒞°) for some α ∈ Γ ∖ KΓ_x.

## 2. The covering lemma: squares lift modulo Γ_x (proved)

**Lemma 1 (intermediate quotients).** Let a finite group G act on a Hausdorff, locally compact space X, and let H ≤ G. The natural map π : X/H → X/G is a local homeomorphism at the point Hp if and only if G_p ⊂ H. If this holds at every point, then π is a finite covering map over each connected component of X/G.

*Proof.*
- Since G is finite and X Hausdorff, p has a G_p-invariant open neighbourhood V with gV ∩ V = ∅ for g ∉ G_p.
- Then V/G_p → X/G and V/H_p → X/H are open embeddings, where H_p = G_p ∩ H. In these charts π is V/H_p → V/G_p, which is a homeomorphism iff H_p = G_p.
- π is closed with finite fibres, hence proper. A proper local homeomorphism between locally compact Hausdorff spaces is a covering over each component of the base (standard). ∎

**Lemma 2 (square lifting).** Assume (U_J). Let F : [a,b] × [0,1] → 𝒜 be continuous, and let F̂_0 : [a,b] → 𝒞° be a lift of F(·,0). Then:
- for every s, every lift μ_s : [0,1] → 𝒞° of F(s,·) with μ_s(0) = F̂_0(s), and
- every lift λ : [a,b] → 𝒞° of F(·,1) with λ(a) = μ_a(1),

satisfy λ(s) ∈ Γ_x · μ_s(1) for all s.

(Lifts of paths in 𝒞° exist for any initial point, by path lifting for finite group quotients: Bredon, *Introduction to compact transformation groups*, II.6.2, cited from memory.)

*Proof.*
- By Fact 0, 𝒜 = 𝒞°/Γ. By (U_J) and Lemma 1 (with H = K·Γ_x), π : 𝒞°/(KΓ_x) → 𝒜 is a covering.
- Let F̃ be the unique lift of F to 𝒞°/(KΓ_x) with F̃(a,0) = [F̂_0(a)] (homotopy lifting for coverings).
- Uniqueness of path lifts gives:
  - [F̂_0(s)] = F̃(s,0) for all s;
  - [μ_s(τ)] = F̃(s,τ) for all τ, since both are lifts of F(s,·) from [F̂_0(s)];
  - [λ(s)] = F̃(s,1), since both are lifts of F(·,1) from [μ_a(1)] = F̃(a,1).
- Hence λ(s) = kγ μ_s(1) with k ∈ K and γ ∈ Γ_x.
- Since K is normal and acts trivially on 𝒞°, kγ μ_s(1) = γ(γ^{-1}kγ)μ_s(1) = γ μ_s(1). So λ(s) ∈ Γ_x μ_s(1). ∎

We apply this with F(s,τ) := (H(γ(s), τt), τt) and F̂_0 := γ̃ × {0}.
- F takes values in 𝒱_U for |t| small: γ([a,b]) is a compact subset of U ∩ V_0, H is uniformly continuous, and H_0 = id.
- F takes values in 𝒜, because F([a,b]×[0,1]) is connected and contains γ × {0} ⊂ 𝒜.

## 3. τ-transport away from J (proved)

Fix 0 < r_1 small. Put B_0^{U} := B_0 ∩ U ∖ {J}. By the cone structure it is a finite union of punctured branches β_1, …, β_N.

Let 𝒵 be the set of connected components of q^{-1}(H(B_0^{U} × Δ_ε)). This set is finite:
- each H(β_j × Δ_ε) is connected;
- the components of its preimage are permuted transitively by Aut(J), as in Fact 0.

Each Z ∈ 𝒵 has a constant pinching pattern S(Z), because Z is connected and lies over a single stratum (R7-4 Lemma 2(a)).

**Lemma 3 (separation).** Fix t with |t| < ε/2. Let 𝔑 := q^{-1}(H((B_0^{U} ∖ {d̄(·,J) < r_1/2}) × [0,t])), where [0,t] := {τt : τ ∈ [0,1]}. Then:
- 𝔑 is compact;
- the sets 𝔑_Z := 𝔑 ∩ Z, Z ∈ 𝒵, are compact and pairwise disjoint;
- hence d'(r_1, t) := min_{Z ≠ Z'} dist(𝔑_Z, 𝔑_{Z'}) > 0.

*Proof.*
- The set (B_0 ∩ closure(U)) ∖ {d̄ < r_1/2} is compact; take U to be the image of a closed ball. Its image under the continuous H, intersected with times in [0,t], is compact, and q is proper. So 𝔑 is compact.
- 𝔑 ⊂ q^{-1}(H(B_0^U × Δ_ε)), in which each Z is closed. So 𝔑_Z is closed in 𝔑, hence compact.
- Distinct components are disjoint. ∎

**Corollary 3′ (τ-transport near the boundary).** Let s be such that d̄(z_s, J) ≥ r_1, and let ẑ_s ∈ Z_s ∈ 𝒵 be as in (T3). Let μ_s be a lift in 𝒞° of τ ↦ F(s,τ) from γ̃(s). Let ε_1 := ε_1(ρ) be such that d̄(X, z) < ρ implies d̄(H(X,τt), H(z,τt)) < ε_1 for all τ (uniform continuity of H; ε_1 → 0 as ρ → 0). If ρ < ε_1 < d'(r_1,t)/3, then:
- μ_s(1) lies within ε_1 of a point w ∈ Z_s that is a lift of H(z_s, t);
- w ∈ L_x;
- F_x(w) ∈ S_t, where S_t is the finite set defined in §4.

*Proof.*
- For each τ, the coarse distance between q(μ_s(τ)) = H(γ(s),τt) and H(z_s, τt) is < ε_1. So μ_s(τ) lies within ε_1 of some lift of H(z_s,τt), which lies in 𝔑 (for t small, H keeps z_s at distance ≥ r_1/2 from J(τt)).
- By Lemma 3, the Z for which dist(μ_s(τ), 𝔑_Z) < ε_1 is unique. It is locally constant in τ, hence constant.
- At τ = 0, μ_s(0) = γ̃(s) is within ρ < ε_1 of ẑ_s ∈ Z_s. So Z = Z_s for all τ, and at τ = 1 we get w ∈ Z_s, a lift of H(z_s,t), with |μ_s(1) − w| < ε_1.
- **w ∈ L_x.** The pattern S(Z_s) is constant, and ẑ_s ∈ L_x. So x is intact on Z_s, i.e. Z_s ⊂ L_x.
- **F_x(w) ∈ S_t.** Let D_s be the piece of the branch β_j ∋ z_s, and v the vertex of D_s that contains x along Z_s. Then v = {x}, since x is intact.
  - If v is constant on D_s, then F_x ≡ φ_v(t) on Z_s ∩ {time t}. This is Lemma 2 of R7-3 (transport of a lifted branch): Z_s is the set Ñ there.
  - Otherwise F_x(ẑ_s) ≅ Y_0 says that z_s ∈ Sp_J, the finite set defined in §4. Then F_x(w) is the class of a component of H(z_s,t). ∎

## 4. Theorem A: no twin jump at J under (U_J) (proved, given (TD_J))

**The finite set S_t.** Let Sp_J be the set of points z ∈ B_0^U such that some vertex v that is non-constant on the piece through z has a value ≅ Y_0 at z. Sp_J is finite: f_v extends to the compact normalisation Ē of each of the finitely many pieces meeting U, and f_v^{-1} of the finitely many relabellings of Y_0 is finite. Then S_t ⊂ M_{g_i,n_i}/S_{n_i} is the finite union of:
- the values φ_v(t) of all constant vertices v of type (g_i,n_i) of the finitely many pieces with a branch in B_0^U;
- the classes of all type-(g_i,n_i) components of H(z,t), for z ∈ Sp_J;
- the classes of all type-(g_i,n_i) components of J(t) := H(J,t).

Let 2ε'(t) > 0 be the minimum distance between distinct elements of S_t (put ε'(t) = 1 if |S_t| = 1). Note that S_t does not depend on r_1.

**Theorem A.** Assume the setting of MS8, the readings (R1), (R2), (C1)–(C3), the track datum (TD_J), and (U_J). Then φ_{c_{k−1}} ≡ φ_{c_k} on Δ.

Hence, if (TD_J) and (U_J) hold at every junction J^1, …, J^m of the chain, then φ_{c_k} ≡ Y for every k, i.e. (TW1) holds. This is by induction from c_0 = i, with φ_i = Y.

Theorem A uses neither (Rig) nor the non-constancy of Y.

*Proof.* By the identity theorem (φ_c is holomorphic: R7-3 Lemma 1), it suffices to prove φ_{c_{k−1}}(t) = φ_{c_k}(t) for all t ≠ 0 in a small disc Δ_{t_0}. Here t_0 is chosen so that, for |t| < t_0, F(s,τ) := (H(γ(s), τt), τt) stays in 𝒱_U for every path of (TD_J) (uniform continuity of H on the compact closure(V_0) ∩ closure(U)). Fix such a t ≠ 0.

**Choice of constants.**
- Let d_J(t) > 0 be the minimum distance in B between distinct lifts of J(t). (The lifts form one finite Aut(J)-orbit.)
- Let ω_H be a modulus of continuity of z ↦ H(z, τt) on closure(B_0 ∩ U), uniform in τ ∈ [0,1].
- Let ω_F be a modulus of continuity of F_x on the compact set L_x ∩ closure(B).
- Choose r_1 > 0 with:
  - r_1 < min(d̄(z_1,J), d̄(z_2,J));
  - r_2 := 2ω_H(r_1) < d_J(t)/4;
  - ω_F(3r_2) < ε'(t).
- Then choose ρ so small that ρ < ε_1(ρ) < min(ω_H(r_1), d'(r_1,t)/3) (Lemma 3, Corollary 3′).
- Take γ, γ̃, z_s, ẑ_s from (TD_J) for this ρ, and define F as above.

**Lifts.**
- For each s, let μ_s be a lift in 𝒞° of F(s,·) from γ̃(s).
- Let λ be a lift in 𝒞° of F(·,1) from μ_a(1).
- By Lemma 2, for every s there is κ_s ∈ Γ_x with λ(s) = κ_s μ_s(1). Take κ_a = id.

**The class function.** For each s choose u(s) ∈ L_x with |λ(s) − u(s)| < r_2 and F_x(u(s)) ∈ S_t, as follows.
- *Regime (ii): d̄(z_s, J) ≥ r_1.*
  - Corollary 3′ gives w_s ∈ L_x, a lift of H(z_s,t), with |μ_s(1) − w_s| < ε_1 and F_x(w_s) ∈ S_t.
  - Put u(s) := κ_s w_s. The norm is Aut(J)-invariant, so |λ(s) − u(s)| = |μ_s(1) − w_s| < ε_1 < r_2.
  - Since κ_s x = x, we have u(s) ∈ L_{κ_s x} = L_x and F_x(u(s)) = F_{κ_s^{-1}x}(w_s) = F_x(w_s) ∈ S_t.
  - **This is the only place where (U_J) is used.** Without it κ_s^{-1}x could be a twin region, which need not be intact at w_s or could carry a different value.
- *Regime (i): d̄(z_s, J) < r_1.*
  - d̄(q λ(s), J(t)) ≤ d̄(H(γ(s),t), H(z_s,t)) + d̄(H(z_s,t), H(J,t)) < ε_1 + ω_H(r_1) ≤ r_2.
  - So some lift ĵ(s) of J(t) has |λ(s) − ĵ(s)| < r_2 < d_J(t)/4, and it is unique.
  - Lifts of J(t) lie in {s_e = 0 for all e} ⊂ L_x. Put u(s) := ĵ(s); then F_x(u(s)) is the class of a component of J(t), so it lies in S_t.

Put c(s) := F_x(u(s)) ∈ S_t.

**Near-continuity.**
- λ is uniformly continuous, so there is δ > 0 with |λ(s) − λ(s')| < r_2 whenever |s − s'| < δ.
- For such s, s' we get |u(s) − u(s')| < 3r_2, with both points in L_x ∩ closure(B). Hence d(c(s), c(s')) ≤ ω_F(3r_2) < ε'(t).
- Since c takes values in S_t, whose distinct elements are ≥ 2ε'(t) apart, c(s) = c(s') whenever |s − s'| < δ. So c is constant on [a,b].

**Endpoints.**
- At s = a: z_a = z_1, so we are in regime (ii), and w_a lies in the component Z_a ∈ 𝒵 containing ẑ_a = z̃_1 ∈ β̃. This component is the set Ñ of R7-3 Lemma 2 for (D, c_{k−1}, x), on which F_x ≡ φ_{c_{k−1}}(t). With κ_a = id, c(a) = φ_{c_{k−1}}(t).
- Likewise c(b) = F_x(w_b) with w_b ∈ Z_b ∋ z̃_2 ∈ β̃'. So c(b) = φ_{c_k}(t).
- Hence φ_{c_{k−1}}(t) = φ_{c_k}(t). ∎

**Remarks on Theorem A.**
1. **Which gap of R7-6 this repairs.**
   - *(Monodromy.)* R7-6 transported markings along the 2-parameter square without controlling branch points. Under (U_J), the only branch points of 𝒞° → 𝒜 have stabilisers fixing x. These are invisible in the covering 𝒞°/Γ_x, which is exactly the object the labels live on.
   - *(Uniformity near J.)* R7-6 needed charts of the boundary points z_s to have size ≫ ε uniformly, which fails as z_s → J. Here, for z_s within r_1 of J, I compare with the lifts of J(t) themselves. They are separated by d_J(t) > 0 because t is fixed first, and all regions are intact at them. The two regimes are glued by the continuity of F_x on L_x.
   - The order of choices (t, then r_1, then ρ) is essential. This is possible because the identity theorem only needs the equality for each fixed small t, and (TD_J) provides tracks for every ρ.
2. **The twin jump of R7-3 §5 is exactly a monodromy phenomenon.** In the proof, every step except the line marked in regime (ii) holds without (U_J). So a twin jump at J (φ_{c_{k−1}} ≢ φ_{c_k}) forces: for a sequence ρ → 0 (with t fixed), some κ_s ∉ Γ_x. That means a nontrivial lift-monodromy of the square F in 𝒜, coming from points of 𝒞° whose stabiliser moves x. This is the precise content of the planner's sketch, step 5(b).
3. **Relation to (Lock).** If (Lock) holds at J (R7-1), then φ_{c_{k−1}} ≡ φ_{c_k} by R7-1 Step 2. So at each junction it suffices to have **(U_J) or (Lock_J)**.
   - In the quintic example (PR-I; not smooth, so only a test case), the twins A, C at P_0 = Y_0 — B_0 — Y_0 are exchanged by automorphisms of interior curves. These are the covers of the configurations (a_1, a_2, 1, 1/a_1, 1/a_2), whose involution x ↦ 1/x lifts because all local monodromies are equal.
   - So there (U) fails, while (Lock) holds. This is a sketch; I did not check which component 𝒞° the track uses.

## 5. Theorem B: the terminal point (TW2) under (U_{Q_0})

**Endpoint datum (TD_Q).** Let Q_0, the last STAY piece D := D^m and its lift β̃ with c_m = {x}, and the terminal branch b with a lift b̃ ⊂ Def(Q_0) be as in Proposition K. So either:
- (MERGE) some edge at x is unpinched along b̃; or
- (puncture-MOV) every edge at x is pinched along b̃, F_x is non-constant along b̃, and Q_0 ∉ Δ_{G_b}.

Fix generic z̃_1 ∈ β̃ ∖ 0 and a point z̃_b ∈ b̃ ∖ 0, with z_b = q(z̃_b). (TD_Q) asks that for every r_1 > 0 small and every ρ ≤ ρ_0(r_1) there are γ : [a,e] → V_0 ∩ U and a lift γ̃ such that:
- (TQ1) |γ̃(a) − z̃_1| < ρ and |γ̃(e) − z̃_b| < ρ;
- (TQ2) for every s there is z_s ∈ B_0 ∩ U with d̄(γ(s), z_s) < ρ, with z_a = z_1 and z_e = z_b;
- (TQ3) with s_* := sup{s : d̄(z_s, Q_0) ≤ r_1}: (T3) holds for every s < s_* with d̄(z_s, Q_0) ≥ r_1.

The point z_b is FIXED, independent of ρ. This is the difference from (K\*)(c) of R7-6, where the merge witness Q′ satisfies d(Q′, Q_0) < ρ.
- **Where it comes from (sketch, not proved).** In the proof of Proposition K, fix k and let n → ∞. The ray endpoints converge to Q_k ∈ b ∖ {Q_0}, which is at a fixed distance from Q_0. Then take z_b := Q_k.
- The price is that along the track ∂Σ_i is only Ext-short (Ext ≤ δ_k), not pinched. So (T3) holds only approximately: there is a lift with |s_e| ≤ σ_k for the edges at x, where σ_k → 0 as k → ∞.
- In regime (ii) this suffices, after choosing k large depending on r_1. On the compact part {d̄(·, Q_0) ≥ r_1/2} of the finitely many lifted branches along which x is merged, some |s_e| with e at x is bounded below by m(r_1) > 0, since s_e is a holomorphic function on the branch vanishing only at the centre. So once σ_k + ρ < m(r_1)/2, the nearby boundary lift has x intact.
- I record this as the reading (TD_Q). Its derivation from Proposition K is a sketch.

Define Γ, Γ_x, 𝒞° and (U_{Q_0}) at Q_0 exactly as in (C3), with the track of (TD_Q).

**Theorem B.** Assume the setting of MS8, (R1), (R2), (C1)–(C3) at Q_0, (TD_Q) and (U_{Q_0}). Assume also φ_{c_m} ≡ Y (for instance from Theorem A at all junctions). Then for every t in a disc Δ_{t_0}, with t ≠ 0, there are:
- a lift Q̂ of Q(t) := H(Q_0, t) with F_x(Q̂) ≅ Y_t, and
- a lifted branch Z′ of b_t := H_t(b) through Q̂ (i.e. Q̂ ∈ closure(Z′)),

such that:
- (MERGE) some edge at x is unpinched along Z′; or
- (puncture-MOV) every edge at x is pinched along Z′, and F_x is non-constant along Z′ for t outside a countable set.

In particular (TW2) holds, and by R7-4 Lemma 1 (= R7-1 Lemma 1) the MS6 configuration exists at every such t.

*Proof.* Fix t as in Theorem A. Use the same constants, with J replaced by Q_0, plus two more:
- Let 𝒵_b be the finite set of connected components of q^{-1}(H_t(b ∩ U ∖ {Q_0})). The set H_t(b ∩ U ∖ Q_0) is connected, being the image of a punctured disc.
- For a lift Q̂ of Q(t), let η_1(t) > 0 be the minimum, over all lifts Q̂ and all Z′ ∈ 𝒵_b with Q̂ ∉ closure(Z′), of dist(Q̂, closure(Z′)). It is positive because there are finitely many compact closures.
- Shrink r_1 so that also 2r_2 < η_1(t). Shrink ρ so that ε_1 < d″/3, where d″ > 0 is the minimum distance between the compact sets closure(Z′) ∩ q^{-1}(H_t(b ∩ U ∩ {d̄(·,Q_0) ≥ r_1/2})), Z′ ∈ 𝒵_b. Also require that distinct branches of B_0 in the closed annulus {r_1/2 ≤ d̄(·,Q_0) ≤ r} are > 2ρ apart.

**Step 1 (class function up to s_*).** Run the proof of Theorem A on [a, s_*]. Regime (ii) uses (TQ3) and (U_{Q_0}); regime (i) uses the lifts of Q(t), separated by d_Q(t).
- This gives c constant on [a, s_*], with c(a) = φ_{c_m}(t) = Y_t.
- At s_* we have d̄(z_{s_*}, Q_0) ≤ r_1, i.e. regime (i). So the unique lift Q̂ of Q(t) with |λ(s_*) − Q̂| < r_2 satisfies F_x(Q̂) = c(s_*) = Y_t.

**Step 2 (after s_*, the track follows b).**
- For s ∈ (s_*, e] we have d̄(z_s, Q_0) > r_1. Consider z_s inside the annulus where the branches are separated. Since γ is continuous and d̄(γ(s), z_s) < ρ, the branch carrying z_s is locally constant. It equals b, because z_e = z_b ∈ b.
- (If z_s leaves the annulus outward, it is no longer near Q_0, and the same argument applies with U large enough to contain b up to z_b.)

**Step 3 (time t).**
- For s ∈ [s_*, e], λ(s) is within ε_1 of a lift of H(z_s, t) with z_s ∈ b and d̄(z_s, Q_0) ≥ r_1. That lift lies in some Z′ ∈ 𝒵_b.
- By the d″-separation, this Z′ =: Z′_* is the same for all s ∈ [s_*, e].
- At s = e: λ(e) = κ_e μ_e(1) with κ_e ∈ Γ_x (Lemma 2). As in Corollary 3′, μ_e(1) is within ε_1 of a point w_e of the component Z_b of q^{-1}(H((b∖Q_0) × Δ_ε)) that contains z̃_b. So λ(e) is within ε_1 of κ_e w_e ∈ κ_e Z_b.
- κ_e w_e lies in some component of 𝒵_b contained in (κ_e Z_b)_t. By d″-separation it is Z′_*. Hence Z′_* ⊂ κ_e Z_b.
- The pattern of κ_e Z_b is κ_e S(b̃), and κ_e x = x.
  - (MERGE) An edge at x is unpinched along b̃, so the edge κ_e(e_0) at x is unpinched along κ_e Z_b ⊃ Z′_*.
  - (MOV) All edges at x are pinched along κ_e Z_b. Also F_x(κ_e p) = F_x(p) for p ∈ Z_b. By R7-3 Lemma 1(b), F_x is non-constant on the time-t transport of the piece of b for t outside a countable set (the identity theorem on Ē gives non-constancy on each of its branches). Hence F_x is non-constant along Z′_* for such t.

**Step 4 (Q̂ lies on Z′_*).**
- λ(s_*) is within r_2 of Q̂ and within ε_1 of Z′_*. So dist(Q̂, Z′_*) < r_2 + ε_1 < 2r_2 < η_1(t).
- Therefore Q̂ ∈ closure(Z′_*). Put Z′ := Z′_*. ∎

**Corollary C (MS8 under (U), modulo the readings).** Assume:
- the setting of MS8 with (Rig);
- (TD_J) and [(U_J) or (Lock_J)] at every junction;
- (TD_Q) and (U_{Q_0}) at the terminal point;
- that the terminal branch is MERGE or puncture-MOV.

Then Y_t = Y_0 for all t.

*Proof.*
- Theorem A, or R7-1 Step 2 under (Lock), gives φ_{c_m} ≡ Y.
- Theorem B gives, for all t in a punctured disc outside a countable set, a non-constant vertex u of a piece E at time t and a puncture p with Y_t a component of f_u(p) (R7-4 Lemma 1). Here u = [x] in the MERGE case and u = {x} in the MOV case.
- By (Rig), puncture values of non-constant vertices lie in the finite set F, so Y_t is a component of an element of F for uncountably many t accumulating at 0.
- t ↦ Y_t is holomorphic (PR-A), so it is constant. ∎

## 6. The residual case: what a twin jump requires (partly proved, partly open)

**Proposition D (necessary conditions for a twin jump; proved, given (TD_J)).** Suppose φ_{c_{k−1}} ≢ φ_{c_k} at the junction J. Then:
- (a) (Lock_J) fails, and (U_J) fails. So there is α ∈ Γ ∖ KΓ_x (in particular αx ≠ x, and α is not a generic automorphism of the family) with (0,0) ∈ closure(Fix(α) ∩ 𝒞°): curves of V_τ near J, with |τ| arbitrarily small, have an automorphism (induced by α ∈ Aut(J)) that exchanges the tracked region x with a different region αx.
- (b) Let Φ be an irreducible component, through (0,0), of the analytic germ Fix(α) ∩ closure(𝒞°) ⊂ Def(J) × Δ that is not contained in {∏ s_e = 0}. One of the following holds:
  - **(A)** Φ ∩ {τ = 0} contains points of B° near 0, arbitrarily close to 0. That is: curves of V_0 itself, arbitrarily close to J, admit an automorphism (from Aut(J) acting on Def(J)) that moves x.
  - **(B)** Φ ∩ {τ = 0} ⊂ {∏ s_e = 0} and has dimension ≥ 1. That is: some lifted branch of B_0 at J (lying in closure(𝒞°)) is fixed pointwise by α. Then every boundary point of V_0 on that branch has an automorphism exchanging the components (or merged vertices) containing x and αx.
  - **(C)** dim Φ = 1 and Φ ∩ {τ = 0} = {(0,0)}. That is: there is a holomorphic arc τ ↦ C_τ ∈ V_τ (after a base change τ = σ^k) of smooth curves with automorphism α, converging to J as τ → 0. This is invisible at t = 0.

*Proof.*
- (a) is the contrapositive of Theorem A, together with R7-1 Step 2 for (Lock). For the germ reformulation of (U_J), see (C3).
- (b) closure(𝒞°) is a 3-dimensional analytic set. It is the closure of a connected component of the preimage of the 3-dimensional manifold 𝒱 (R1); closures of unions of components of q^{-1}(𝒱_U) are analytic, as in R7-4 Lemma 2(c). Fix(α) = Fix_{Def(J)}(α) × Δ is a smooth submanifold (linear action). So Fix(α) ∩ closure(𝒞°) is analytic, and Φ has dimension 1, 2 or 3.
  - **dim 3.** Then α fixes 𝒞° pointwise, i.e. α ∈ K ⊂ KΓ_x, contradicting the choice of α. So this case does not occur.
  - **dim Φ ≥ 2.** Φ ∩ {τ = 0} has dimension ≥ 1 at (0,0) (Krull, if τ ≢ 0 on Φ; trivially otherwise). It lies in closure(𝒞°) ∩ {τ=0} ⊂ q^{-1}(closure(V_0) ∩ U), by (R2): H commutes with closures and H_0 = id. Either it meets B° arbitrarily close to 0, giving (A), or it lies in the boundary, giving (B).
  - **dim 1.** If Φ ⊂ {τ = 0}, then Φ ∖ (0,0) consists of interior points of V_0's lift, giving (A). Otherwise τ|_Φ is finite at (0,0), and since Φ ⊄ {∏s_e = 0}, Φ ∖ (0,0) ⊂ B° × Δ near (0,0) (a proper analytic subset of an irreducible curve germ is the point). This is (C), with the normalisation of Φ giving the base change. ∎

**How this relates to the planner's dichotomy (step 5(b) of the sketch, and the "named approach").**
- The first alternative, "Fix(α) ∩ 𝓛 stays away from the region swept by the transported paths", is (U_J). Under it, Theorem A makes R7-6's argument rigorous at J.
- The second alternative, "the closure of the fixed locus meets the boundary at points J′_τ near J_τ at which α exchanges two components both ≅ Y_τ", is **not** forced by the analysis above. In case (C), Φ meets the boundary only at (0,0). In case (B), it meets it only at τ = 0.
- Even when Φ ∩ {∏s_e = 0} contains an arc Ψ with τ|_Ψ non-constant, the point ψ(τ) ∈ Ψ may be:
  - a lift ĵ(τ) of J(τ). Then F_x(ĵ(τ)) = F_{αx}(ĵ(τ)): the twins are locked at that particular lift, which is a pointwise form of (Lock).
  - a point of a lifted transported branch Z. Then only the components x, αx of that boundary point are exchanged.

  In neither case did I find a way to show that the monodromy κ of the square (a product of conjugates of such α's) fixes the class F_x on the transported D'-branch. Heuristically (this is not a construction), the R7-3 §5 local model, completed by an interior 3-fold, is compatible with (C). Take Def coordinates (a, b) for the two twin components with σ(a,b) = (b,a), and let 𝒞̄ be any irreducible 3-fold containing both transported branches and meeting Fix(σ) = {a = b} in a curve through (0,0) only.

So the chart-plus-interior-local analysis does not exclude (C) either. Any proof of (TW) must use total geodesy at t = 0, or global information, to exclude (A), (B) and (C) at a twin junction, or to show that they force (Lock).

**Remark (where total geodesy could enter, not carried out).** In case (A), the lift of V_0 and Fix(α) are both totally geodesic in T_g. Fix(α) is the image of the Teichmüller space of the quotient orbifold, a holomorphic isometric embedding. So their intersection near the lift of J is a totally geodesic subvariety of V_0 consisting of α-symmetric curves, whose closure contains J. One would want to show that such a sub-locus forces the twins x, αx to stay isomorphic at J(τ) under every deformation satisfying (i), (ii). That would be a (Lock) statement, and it is the natural next target. I have no proof.


### R8-8. Theorem 1 (MS8 under star coherence), isotropy preservation, Proposition 3, pure crossings, the scale conflict (from round8_q8, verbatim, §§0–6)
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


## Reminder
- Never assume V_t totally geodesic for t ≠ 0, and never assume H_t preserves automorphism groups. That is the orbifold reading, which is NOT adopted.
- Chart-local arguments alone cannot exclude twin jumps (R7-3 §5 model; R8-5 §6 heuristic). If your argument is purely chart-local, check it against those models before claiming it.
- Begin with a plan/status line. End with: proved / not proved / open.
