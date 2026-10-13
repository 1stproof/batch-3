# round9_q4 — answer

**Status.**
- Part 1, the claim (CR*): **proved for every normal singularity**, given Steps 1–4 of Theorem X (R8-1), which I re-checked. Q-factoriality is not needed, and neither is the monomial criterion. The new ingredient replaces Step 5 (Hurwitz applied to a Q-Cartier equation) by a homological intersection argument on a resolution of Ŝ, using Mumford's negative definiteness.
- Part 2, the same-sheet lemma: **the literal reading (TD_J) does not follow from Proposition K as written.** The chain read off the Hausdorff limit K_0 can record a transition at a point J that the approximating rays never pass near. I give a repaired version of Proposition K, the "walk chain", built from a single approximating ray. Every transition of the walk chain is realised by a sub-path that stays inside a small Milnor ball around the transition point. For the walk chain the same-sheet lemma is **proved**.
- Combination: in the walk chain, no junction or endpoint is a crossing, except in the case where the incoming and outgoing branches are the same coarse branch of the same piece. That residual case is the twin case (type (T) of R8-6), which is outside this task.

Plan, written first:
- §1: prove (CR*) in a strengthened form (Theorem X*).
- §2: same-sheet lemma: what fails, and the repair.
- §3: the combination.
- §4: summary of what is proved and what is open.

---

## 1. Part 1: (CR*) for arbitrary normal sheets

### 1.1 Statement
Setting and notation are exactly as in Theorem X (R8-1 §3.1):
- V_0 ⊂ M_g is a closed totally geodesic surface. Smoothness is not needed for this part.
- E is a piece of B_0 in a product-type stratum Δ_G.
- Q_0 ∈ E, so Q_0 lies in Δ_G.
- β is a local branch of E at Q_0, and β̃ is a lift of β to Def(Q_0).
- S is an irreducible component of the germ at 0 of the preimage of closure(V_0) in Def(Q_0), with S ⊃ β̃.
- ν: Ŝ → S is the normalisation, and ŝ_0 = ν^{-1}(0).
- B̂ = ν^{-1}(S ∩ {∏ s_e = 0}).
- Ê_1, …, Ê_r are the components of the germ (B̂, ŝ_0) that map onto β̃, and C_1, …, C_m are the others.

**Theorem X\*.** m = 0. That is, every irreducible component at ŝ_0 of the boundary curve of Ŝ maps onto the single lifted branch β̃.

In particular (CR*) holds. Any sheet S of closure(V_0) at Q_0 that contains a branch of E contains no other boundary curve through Q_0. This excludes boundary curves of other pieces, and also other branches of E itself, including other lifts αβ̃ ≠ β̃ of β.

### 1.2 What is used from Theorem X (re-checked)
Steps 1–4 of R8-1 §3.2 produce the following, and I re-checked each item:
- a connected open set Ω ⊂ 𝔻;
- holomorphic maps D̂_n: Ω → Ŝ with D̂_n(Ω) ∩ B̂ = ∅;
- a holomorphic L̂: Ω → Ŝ with D̂_n → L̂ locally uniformly;
- a point w* ∈ Ω with L̂(w*) = ŝ_0, and L̂(Ω) ⊂ Ê_1.

Here is the check, item by item.
- **L̂(Ω) ⊂ Ê_1.** L̂(Ω) ⊂ B̂, since L takes values in the boundary. The sets L̂^{-1}(Ê_l) and L̂^{-1}(C_i) are analytic and cover Ω, and L̂^{-1}(Ê_1) contains a neighbourhood of 0. By the identity principle it is all of Ω.
- **L̂ is non-constant.** Its image under ν is a lift of L, and L is non-constant by (Fl).
- **L̂^{-1}(ŝ_0) is discrete.** It is analytic and does not contain 0.
- **Surjectivity of L onto E^ν (Step 3).** This uses:
  - the closedness of Teichmüller discs and the local finiteness of their translates, (Prop);
  - finiteness of the set Λ of lifts;
  - properness of L̄.
  I re-checked each of these.
- **Lifting to Def(Q_0) and to Ŝ (Steps 2 and 5).**
  - The Teichmüller disc lifts to T_g. A component of the preimage of the chart interior maps holomorphically to Def(Q_0)°. This is cited, as in R8-1.
  - The lifted disc lies in S, by an analytic-covering argument plus the choice of X̃_n off S ∩ S_i.
  - It lifts to Ŝ by the universal property of normalisation, since X̃_n is off the non-normal locus.
- **Ŝ is smooth off ŝ_0 near ŝ_0.** A normal surface has isolated singular points, and ŝ_0 ∈ B̂. Hence D̂_n maps into the smooth part of Ŝ.

Only Step 5 of R8-1 (the Hurwitz step with a Q-Cartier equation G) is replaced.

### 1.3 Cited standard facts (from memory)
- **(Res)** Let (Ŝ, ŝ_0) be a normal surface germ. There is a resolution π: S′ → W, where W = Ŝ ∩ (closed Milnor ball) is a small closed neighbourhood of ŝ_0, such that:
  - π is an isomorphism over W ∖ {ŝ_0};
  - Exc := π^{-1}(ŝ_0) is a compact connected curve with irreducible components F_1, …, F_p, p ≥ 1. Connectedness follows from Zariski's main theorem. If ŝ_0 is a smooth point, take π to be the blow-up of ŝ_0, so that p = 1 and F_1² = −1.
  - U′ := π^{-1}(int W) deformation retracts onto Exc. Hence H_2(U′; ℤ) is free with basis [F_1], …, [F_p].
- **(Neg)** (Du Val, Mumford, Grauert.) The intersection matrix N = (F_j · F_k) is negative definite.
- **(Int)** Let A ⊂ U′ be a closed analytic curve. The intersection number with A, z ↦ z · A, is a well-defined homomorphism on H_2(U′; ℤ) (Poincaré–Lefschetz duality: A defines a Borel–Moore class). Suppose a 2-cycle z consists of pieces that are disjoint from A, together with holomorphic discs meeting A in isolated interior points. Then z · A is the sum of the local intersection multiplicities at those points, and each multiplicity is > 0.
- **(Pos)** This is elementary, and I prove it here. Let N be a negative definite symmetric real matrix whose off-diagonal entries are ≥ 0 and whose graph ({j,k} is an edge iff N_{jk} > 0) is connected. Let λ ≥ 0 with λ ≠ 0. Then x := −N^{-1}λ has all entries strictly positive.
  *Proof.*
  - Write x = x⁺ − x⁻, where x⁺ and x⁻ are non-negative with disjoint supports.
  - Then (x⁻)ᵀ N x = (x⁻)ᵀ N x⁺ − (x⁻)ᵀ N x⁻.
  - The first term is ≥ 0, because the supports are disjoint and the off-diagonal entries are ≥ 0. The second term, −(x⁻)ᵀ N x⁻, is ≥ 0, with equality only if x⁻ = 0. So (x⁻)ᵀ N x ≥ 0.
  - But (x⁻)ᵀ N x = −λ · x⁻ ≤ 0. Hence x⁻ = 0, i.e. x ≥ 0.
  - Suppose x_j = 0 for some j. Then Σ_{k≠j} N_{jk} x_k = (Nx)_j = −λ_j ≤ 0. Every term on the left is ≥ 0, so x_k = 0 for every neighbour k of j.
  - By connectedness x = 0. Then λ = −Nx = 0, a contradiction. ∎
  For the matrix N of (Neg), the off-diagonal entries F_j · F_k (j ≠ k) are ≥ 0, and the graph is connected because Exc is connected.

### 1.4 Proof of Theorem X*
Suppose m ≥ 1, and fix C := C_1.

**Choices.**
- Choose W as in (Res) so small that, inside W, C ∩ Ê_1 = {ŝ_0}. Distinct irreducible curve germs meet only at the base point.
- Choose ε > 0 so small that the closed disc Ω̄_ε := {|w − w*| ≤ ε} lies in Ω, L̂(Ω̄_ε) ⊂ int W, and L̂^{-1}(ŝ_0) ∩ Ω̄_ε = {w*}.
- For n large, D̂_n(Ω̄_ε) ⊂ int W, by uniform convergence on Ω̄_ε.

**Lifts.**
- D′_n := π^{-1} ∘ D̂_n is holomorphic, since π is an isomorphism over W ∖ {ŝ_0} ⊃ W ∖ B̂.
- Its image avoids π^{-1}(B̂). That set contains Exc, the strict transform C′ of C, and the strict transform Ê′_1.
- L̂|_{Ω_ε} takes values in the curve Ê_1, and is not contained in its singular locus. So it factors through the normalisation of Ê_1, and that normalisation maps holomorphically onto Ê′_1 ⊂ S′. This defines a holomorphic L′: Ω_ε → Ê′_1 ⊂ S′ with π ∘ L′ = L̂.
- L′(w) ∈ Exc only for w = w*.
- C′ ∩ Ê′_1 ⊂ Exc, because C ∩ Ê_1 = {ŝ_0} in W. Hence L′(Ω̄_ε) ∩ C′ = ∅.

**Boundary circles.**
- K := L̂(∂Ω_ε) is a compact subset of Ê_1 ∖ {ŝ_0}. Over a neighbourhood of K, π^{-1} is a biholomorphism. Hence D′_n → L′ uniformly on ∂Ω_ε.
- K′ := L′(∂Ω_ε) is compact and disjoint from Exc ∪ C′. Fix a Riemannian metric and a tubular neighbourhood N_K of K′ in U′ that is disjoint from Exc ∪ C′.
- For n large, the short-geodesic homotopy between D′_n|_{∂Ω_ε} and L′|_{∂Ω_ε} sweeps a singular annulus A_n ⊂ N_K with ∂A_n = L′(∂Ω_ε) − D′_n(∂Ω_ε).

**The cycle.** Put
 Z_n := D′_n(Ω̄_ε) − L′(Ω̄_ε) + A_n.
This is a singular 2-cycle in U′. By (Res), [Z_n] = Σ_j k_j [F_j] with k_j ∈ ℤ.

**Intersection with F_k.**
- The piece D′_n(Ω̄_ε) is disjoint from F_k, and so is A_n.
- L′(Ω̄_ε) meets Exc only at L′(w*), in isolated points. Put λ_k := (local intersection number of the disc L′ with F_k) ≥ 0. Then Σ_k λ_k > 0, because L′(w*) ∈ Exc and L′ ⊄ Exc.
- By (Int), Σ_j k_j (F_j · F_k) = Z_n · F_k = −λ_k for all k. That is, N k = −λ.
- N is invertible by (Neg). So k = −N^{-1}λ, and by (Pos) all k_j > 0.

**Intersection with C′.** C′ is a closed analytic curve in U′.
- Each piece of Z_n is disjoint from C′: D′_n avoids π^{-1}(B̂), L′ avoids C′, and A_n ⊂ N_K. Hence Z_n · C′ = 0.
- On the other hand, Z_n · C′ = Σ_j k_j (F_j · C′).
  - Each F_j · C′ ≥ 0, because F_j ≠ C′ are distinct curves.
  - Some F_j · C′ > 0. C passes through ŝ_0, so points of C ∖ {ŝ_0} accumulate at ŝ_0. Their preimages accumulate on the compact set Exc, and C′ is closed, so C′ ∩ Exc ≠ ∅.
  - With all k_j > 0, this gives Z_n · C′ > 0.

This contradiction proves m = 0. ∎

**Remarks.**
1. In the language of Mumford's ℚ-valued intersection theory, the proof says the following.
   - The local intersection C · L̂ at ŝ_0 is strictly positive, as always for two distinct curves through a normal surface point.
   - Mumford intersection numbers are continuous under the convergence D̂_n → L̂.
   - Mumford's pull-back π^*C = C′ + Σ a_j F_j is numerically trivial on Exc. So the homology class of the bubble Σ k_j F_j that may appear in the limit of the D′_n contributes nothing.

   The Q-Cartier equation G of Theorem X is only needed to make this continuity hold for an honest function. Q-factoriality is therefore irrelevant.
2. Only the following were used: the discs D̂_n avoid the whole boundary B̂, and their limit L̂ is a disc inside one boundary curve Ê_1 passing through ŝ_0. The second fact is the place where total geodesy enters (Lemma PA, (Fl), (Prop): the limit disc sweeps all of E).
3. Strengthening. Two different branches of the same piece E at Q_0 (or two different lifts β̃, αβ̃ of one branch) never lie in a common sheet S of the chart. Indeed, apply Theorem X* with β; the curve over the other branch would be a C_i.
4. As in R8-1 Remark 2, product type of the stratum of E is used: the global coordinate f_j on E appears in Step 3. Non-product strata are not checked.
5. From chart sheets to coarse sheets. Suppose a sheet 𝒮 of closure(V_0) at Q_0 in M̄_g contains a branch b of E and another boundary branch β′. Take a chart component S over 𝒮. The preimage of 𝒮 is ⋃_α αS, so S contains some lift of b and some lift of β′. Theorem X* then gives a contradiction, unless β′ = b as coarse branches.

---

## 2. Part 2: the same-sheet lemma

### 2.1 Sheets and Milnor balls (Lemma S, made precise)
This lemma is cited and standard (local structure of analytic germs).

Let X = closure(V_0) ⊂ M̄_g and Q ∈ B_0. Assume V_0 is smooth, so Sing X ⊂ B_0. Put Z := Sing X ∪ B_0. For W in a fundamental system of small (Milnor) neighbourhoods of Q:
- the connected components of V_0 ∩ W = (X ∖ Z) ∩ W are exactly the sets X_k ∩ W ∖ Z, where X_k runs over the irreducible components of the germ (X, Q);
- each such set is connected, and its closure in W is X_k ∩ W.

Fix such a W. Choose it also so small that B_0 ∩ W is the union of the branches of B_0 at Q, each branch minus Q lying in one stratum. Then:

**Lemma S′.** Let γ: [a,b] → V_0 ∩ W be a path. Suppose there are a sequence of such paths γ_n and points z^1 ∈ β ∖ {Q} and z^2 ∈ β′ ∖ {Q}, where β, β′ are branches of B_0 at Q, such that γ_n(a) → z^1 and γ_n(b) → z^2. Then some sheet X_k contains both β and β′.

*Proof.*
- Pass to a subsequence along which all the γ_n lie in the same component X_k ∩ W ∖ Z. There are finitely many components.
- X_k ∩ W is closed in W, so z^1 ∈ X_k.
- Near z^1, B_0 coincides with β, since z^1 is not Q and W contains no other special point.
- X_k ∩ ∂M̄_g is locally the zero set of ∏ s_e on the 2-dimensional germ X_k. So it is either empty near z^1 or of pure dimension 1 through z^1. It contains z^1, so it is the germ of β at z^1.
- So X_k contains an open piece of the irreducible germ β, hence all of β. The same argument applies to β′. ∎

### 2.2 What fails in the reading (TD_J)
Proposition K (PR-H §3) produces the continuum K_0 as a Hausdorff limit of K(δ_k, η_k). Each K(δ, η) is in turn a Hausdorff limit of the ray segments {g_s X_n : 0 ≤ s ≤ T_n}. The chain D^1, J_1, …, Q_0 is then read off from K_0.

Hausdorff convergence says nothing about the order in which a ray visits the parts of K_0. Here is a failure mode, which nothing in the proof excludes.
- Suppose the rays come near β at J, then leave every small ball around J along β, run around a loop of B_0, and re-enter the ball along β′.
- Then K_0 ⊃ (β ∪ β′) near J, and J ∈ K_0. A chain read off K_0 may record the transition D → D′ "at J".
- But no ray sub-path stays near J while passing from β to β′.

So the clause in (TD_J) that γ maps into V_0 ∩ U, with U a small neighbourhood of J, is not justified by Proposition K as written. In this situation the same-sheet conclusion at J has no support: β and β′ may lie in different sheets at J (the case Cr1). This is exactly what the "routine marking details" hide.

### 2.3 Repair: the walk chain (Proposition K_w)
**Data.**
- P (generic on ∂V_0), (X_n, q_n), the ray γ_n(s) := g_s X_n and T_n = T_n(δ, η) are as in PR-H §2–3.
- **Special set Σ.** Σ is the finite set of points of B_0 consisting of:
  - junctions (points in the closures of two distinct pieces);
  - singular points of B_0;
  - punctures of pieces;
  - points of a piece D at which some vertex non-constant on D has a value of class [Y_0].

  The last kind is finite: a non-constant vertex takes a given value at finitely many points, and there are finitely many pieces and vertices.
- Fix r > 0 so small that:
  - the balls B(J, 3r), J ∈ Σ, are pairwise disjoint;
  - each B(J, 3r) is a Milnor neighbourhood as in §2.1;
  - each B(J, 3r) lies in an orbifold chart Def(J)/Aut(J);
  - P ∉ B(J, 3r) for all J.

  Put K_D := closure(D) ∖ ⋃_J B(J, r/2). This is compact, and the K_D are pairwise disjoint. Let 4ρ_* be the least distance between distinct K_D.
- Choose δ, η small, depending on r, so that (a) and (b) hold.
  - (a) **Short curves are node curves.** If a stable curve z ∈ B_0 lies outside ⋃ B(J, r/2), and X is within distance ρ_* of z, then every curve with Ext_X ≤ δ is a node curve of z under the nearby marking. This holds by compactness of the stratum parts involved (collar lemma, cited).
  - (b) **η separates Y_0.** For every piece D and every vertex u non-constant on D, the class of u on K_D is at distance > 2η from [Y_0]. For every constant vertex of every piece whose value is not ≅ Y_0, the value is at distance > 2η from [Y_0].

**Step 0 (closeness to B_0).** ρ_n := sup_{s ≤ T_n} dist(γ_n(s), B_0) → 0.
- Let s_n ≤ T_n.
- If s_n is bounded, Kerckhoff gives Ext_{γ_n(s_n)}(Γ-curves) ≤ e^{2s_n} Ext_{X_n} → 0.
- If s_n → ∞, Lemma NH(1) gives Ext(c_n) ≤ e^{−2s_n}/m → 0.
- In either case every limit point of γ_n(s_n) lies in closure(V_0) ∩ ∂M̄_g = B_0, by Maskit's comparison.

**Step 1 (travel and excursions).** Take n large, with ρ_n < min(ρ_*, r/2).
- A time s is a *travel time* if γ_n(s) lies outside ⋃ B(J, r). Then the B_0-points within ρ_n of γ_n(s) lie in a unique K_D. The piece D is locally constant on maximal intervals of travel times.
- An *excursion* at J is a maximal interval of times in B(J, 2r) that contains a time in B(J, r). Its interior endpoints are travel times on the sphere of radius 2r.
- By uniform continuity there are finitely many excursions. Every excursion crosses the shell r ≤ d ≤ 2r.
- The complement of the excursions consists of travel times, so [0, T_n] is a finite alternation: travel along D^1, excursion at J_1, travel along D^2, …. The first travel is along the piece D^1 ⊃ P of ∂V_0.

**Step 2 (STAY along travel intervals).** Let s be a travel time on D, and z_s ∈ K_D a point at distance < ρ_n from γ_n(s).
- Since Ext(∂Σ_i) ≤ δ, (a) shows that the curves of ∂Σ_i are node curves of z_s.
- ψ is continuous on augmented Teichmüller space, so the Σ_i-side of z_s is within η + o(1) of Y_0. In particular it is a single smooth component, a vertex c of D.
- By (b), c is a constant vertex of D with value ≅ Y_0.
- Consequently, at travel times Ext(∂Σ_i) = o(1) < δ and d(ψ, Y_0) = o(1) < η. So **T_n is not a travel time**, and the walk ends inside an excursion, at some Q ∈ Σ.

**Step 3 (chart consistency inside an excursion at J).**
- During the excursion, γ_n lies in the chart Def(J)/Aut(J) and lifts continuously to γ̃_n in Def(J)°. Path lifting through a finite quotient is cited (Bredon).
- The T_g-marking along γ_n is compatible with the chart. The component of the preimage of the chart in T_g covers Def(J)°, with deck group generated by the Dehn twists about the vanishing cycles and the stabiliser. So the vanishing cycle of each chart edge e is a well-defined marked curve throughout the excursion.
- At the entry time, ∂Σ_i is the set of node curves around the constant vertex c of D. A constant vertex stays intact at J, since its value lies in M_w. So c = {x} for a single chart vertex x along the entry lift β̃ (a branch of D at J), and ∂Σ_i = {vanishing cycles of the edges at x}.
- This identification persists along the whole excursion.
- At the exit time (if the excursion is not the last), Step 2 applies on the exit piece D′ along a lift β̃′. The same x satisfies c′ = {x} along β̃′.

So the walk gives a chain in the sense of (K′): constant vertices c_m ≅ Y_0, and a common chart vertex x_m at each J_m.

**Step 4 (the endpoint).** Let Q be the point of the last excursion, entered from D along β̃ with chart vertex x.
- Take a subsequence n → ∞, with (r, δ, η) fixed. The finite combinatorial data are then constant: Q, D, β̃, x.
- The nearest boundary lifts z̃_n of γ̃_n(T_n) converge to some z̃^∞ ∈ (preimage of B_0) ∩ closure(B(Q, 2r)).
- **z̃^∞ ≠ 0.**
  - F_x(0) ≅ Y_0, by continuity of F_x on L_x along β̃.
  - If z̃^∞ = 0, then near 0 every s_e with e at x tends to 0, so Ext(∂Σ_i) → 0. Also ψ → F_x(0) ≅ Y_0.
  - Both stopping conditions would then fail at T_n.
- So z̃^∞ lies on a lifted branch b̃ ∖ {0} at Q. At T_n one of the two stopping conditions holds.
  - **Ext(γ_e) = δ for some e at x.** Then s_e(z̃^∞) ≠ 0, so e is unpinched along b̃: **MERGE**.
  - **d(ψ, Y_0) = η.** Then all edges at x are pinched along b̃, and d(F_x(z̃^∞), Y_0) = η > 0 while F_x(0) ≅ Y_0: **MOV** (interior or puncture).

**Step 5 (same sheet at every transition).**
- Each junction transition of the walk chain is a sub-path of γ_n inside B(J_m, 2r) ⊂ W. It starts within ρ_n of a point of β^m ∩ shell and ends within ρ_n of a point of β^{m+1} ∩ shell.
- Over the subsequence these points converge to points of the branches other than J_m.
- Lemma S′ applies: the incoming branch and the outgoing branch lie in a common sheet at J_m.
- At the endpoint, the last excursion goes from near β to near z^∞ ≠ Q on b. So β and b lie in a common sheet at Q.

The walk chain depends on (r, δ, η, n), but it is a single finite chain with all the properties (K′) requires. **Proposition K_w (proved, modulo the inputs of PR-H: Lemma PA, Lemma NH, Kerckhoff, Maskit, the T_g ↔ Def chart description, and the collar lemma, all cited):** there is a chain as in (K′), with endpoint MERGE or MOV, in which every transition, including the endpoint, has its incoming and outgoing branches in a common sheet.

---

## 3. Combination with Theorem X*
Assume the pieces of the chain are of product type (PT_chain), as MS8 already assumes. Use the walk chain.

**(a) No junction lies in the stratum of an adjacent piece, except along a single coarse branch.**
- Suppose J_m ∈ stratum(D^{m+1}), i.e. J_m is a point of the piece D^{m+1}.
- The common sheet at J_m contains a branch of D^{m+1} and the incoming branch β^m.
- By Theorem X* and Remark 5, β^m and the outgoing branch are the same coarse branch of the same piece, so D^m = D^{m+1}.
- The same holds with the roles of m and m+1 exchanged.

**(b) The junction crossing of R8-8 Prop. 3(c).**
- Case (c) asserts J_m ∈ stratum(D^{m+1}), with c_{m+1} = {x_m} constant on D^{m+1} along β^{m+1}_−. Strata are transported by H_t, so this is a statement at t = 0.
- By (a), D^m = D^{m+1} and the two branches coincide coarsely. Then the lifts satisfy β̃^{m+1}_− = aβ̃^m_+ for some a ∈ Aut(J_m).
- This is the same-branch twin configuration (type (T) of R8-6), not a crossing.
- So genuine junction crossings (a different piece, or a different coarse branch) do not occur.

**(c) Endpoint.**
- Suppose the endpoint is iMOV, i.e. Q ∈ stratum(E_b).
- The common sheet at Q contains b and β. By Theorem X*, β and b are the same coarse branch, so E_b = D.
- But x is constant along β̃ (STAY) and non-constant along b̃. So b̃ = aβ̃ with ax ≠ x: again the twin type (T).
- Hence the endpoint is MERGE, puncture-MOV, or a same-branch twin.

**Conclusion of the derivation.** Under MS8's hypotheses plus (PT_chain), the walk chain has no interior-MOV endpoint and no junction crossing, apart from configurations of same-branch twin type. The planner's derivation is therefore correct for the walk chain, after this caveat about twins is added. It was not correct for the K_0-chain without the repair of §2.3.

---

## 4. Summary
**Proved:**
- **Theorem X\*** ((CR*) in strengthened form) for every normal sheet. It assumes Steps 1–4 of R8-1 Theorem X (re-checked) and a product-type stratum for E. Its corollary: two distinct coarse boundary branches through an interior point of a piece never share a sheet.
- **Lemma S′** and **Proposition K_w**: the walk chain, whose transitions are local, and which therefore satisfies the same-sheet lemma. This is modulo the cited inputs of PR-H.
- The combination of §3: crossings (Cr1) and (Cr2) are eliminated for the walk chain.

**Found false or unsupported:**
- The reading (TD_J) for the chain read off the Hausdorff limit K_0. The track need not stay near J during the transition (§2.2). The repair is to replace that chain by the walk chain.

**Open / not covered:**
- (i) The same-branch twin configurations (type (T)) at junctions and at the endpoint. These were excluded from this task.
- (ii) Non-product strata (Theorem X Step 3 uses the global coordinate f_j).
- (iii) The cited inputs: (Fl), the T_g ↔ Def chart description, Proposition K's Lemmas PA and NH, and (Res), (Neg), (Int), all cited from memory.
- (iv) Entry 82 (Rig), as before.

=== END OF ANSWER round9_q4 ===
