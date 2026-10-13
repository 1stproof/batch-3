**Plan/status.** This is a chain check of Proposition K_w and Lemma S′ (round9_q4 §2). I check every step against points 1–7 of the brief.

**Verdict in brief: REPAIRED.** Proposition K_w holds in the form the chain uses, but only after four repairs:
- (R-a) the choice of η and ρ_* needs three extra small conditions;
- (R-b) Step 3: the chart lift must be the *canonical* lift through augmented Teichmüller space, not an arbitrary Bredon lift. With an arbitrary lift, the label x can change at orbifold points;
- (R-c) Step 5, upstairs: an arbitrary lifted path need *not* lie in a single irreducible component of q^{-1}(closure V_0). The canonical lift does lie in one, because it lies on the image of a Teichmüller disc. This also needs r small enough that distinct lifted branches meet only at the chart centre;
- (R-d) the chain's combinatorics are not uniform in n. The number of excursions can grow with n. A single chain with all the properties is obtained by keeping only "recurrent" transition types.

The inputs are taken as given, as in the text: Lemma PA, Lemma NH, Kerckhoff, Maskit, the plumbing/Kuranishi charts and the collar lemma. Below, "cited" means cited from memory.

---

## 0. Conventions made explicit

- **Pieces.** B_0 = closure(V_0) ∖ V_0 is the intersection of the irreducible 2-dimensional analytic set closure(V_0) with ∂M̄_g. Locally, ∂M̄_g is the zero set of the Aut-invariant function N = ∏_{g∈Aut(J)} g^*(∏_e s_e), which descends to the coarse chart. Hence B_0 has pure dimension 1. A *piece* is a 1-dimensional irreducible component of B_0 ∩ Δ_G, for some stratum Δ_G.
  - closure(D) ∖ D consists of punctures of D, which lie in Σ.
  - So K_D ⊂ D, the K_D are compact, and they are pairwise disjoint: common points of two closures are junctions.
- **Vertices of a piece.** For the strata Δ_G of the pieces (which may be quotient strata), "vertex of D" means an orbit of vertices under the monodromy of D. "Constant vertex" and "value class" are monodromy-invariant, so nothing below changes.
- **The metric d.** Σ is finite. I take a metric d on M̄_g which, near each J ∈ Σ, is the quotient of an Aut(J)-invariant Euclidean metric on Def(J). Then small metric balls B(J,ρ) are images of round Aut-invariant balls B̃(J,ρ) ⊂ Def(J). For small ρ these are Milnor balls for the germs (X,J) downstairs and (q^{-1}X, 0) upstairs. (Milnor's conic structure theorem, cited.)

## 1. Step 0 (point 1): correct

Let s_n ≤ T_n. Since (X_n, q_n) is a generating pair and V_0 is totally geodesic, γ_n(s_n) ∈ V_0, so every limit point lies in closure(V_0).
- If s_n stays bounded: Kerckhoff gives Ext_{γ_n(s_n)}(Γ-curves) ≤ e^{2s_n} Ext_{X_n}(Γ-curves) → 0, since X_n → P ∈ Δ_Γ.
- If s_n → ∞: Lemma NH(1) gives Ext(c_n) ≤ e^{-2s_n}/m → 0.
- In both cases some curve has Ext → 0. By Maskit's comparison its hyperbolic length → 0, so the limit lies in ∂M̄_g.

Hence every limit point lies in closure(V_0) ∩ ∂M̄_g = B_0. Here V_0 is closed in M_g (an algebraic subvariety), so closure(V_0) ∩ M_g = V_0.

Uniformity follows by contradiction. If ρ_n ↛ 0, choose s_n ≤ T_n with dist(γ_n(s_n), B_0) ≥ ε along a subsequence. A further subsequence converges, by compactness of M̄_g, to a point of B_0, which is a contradiction. **Verified.**

## 2. Step 1 (point 2, first half): correct

- **T_n is finite.** This is Lemma NH(2), an input. So [0,T_n] is compact and γ_n|[0,T_n] is uniformly continuous into (M̄_g, d).
- **Finitely many excursions.** γ_n(0) = X_n is near P, and P ∉ B(J,3r). So every excursion is entered from the sphere d(·,J) = 2r and must reach d < r. Each excursion therefore contains a sub-interval crossing the shell r ≤ d ≤ 2r. By uniform continuity such a crossing takes time ≥ τ_n > 0. The balls B(J,3r) are disjoint, so excursions at different J are disjoint, and there are at most T_n/τ_n + 1 excursions.
- **Times outside the excursions are travel times.** Suppose γ_n(s) ∈ B(J,r). Then the maximal interval of times in B(J,2r) containing s contains a time in B(J,r), so it is an excursion. Hence a time outside all excursions lies outside ⋃_J B(J,r).
- **The piece at a travel time is unique.** Let s be a travel time and z ∈ B_0 with d(z, γ_n(s)) ≤ ρ_n < r/2. Then d(z,J) > r/2 for all J, so z ∈ K_D for some D, since closure(D) ∖ ⋃B(J,r/2) = K_D. Two such points are within 2ρ_n < 4ρ_* of each other, so they lie in the same K_D. By continuity the same holds on whole travel intervals, so D is locally constant there.
- **First piece.** P ∉ Σ, so the first travel is along the piece D^1 ∋ P, and D^1 ⊂ ∂V_0.

**Verified.** The claim that the walk ends inside an excursion is Step 2.

## 3. Step 2 (points 2 and 3): correct after repair (R-a)

**Repair (R-a).** Add three conditions, all depending only on r:
- **(a′)** Shrink ρ_* if necessary so that the closed ρ_*-neighbourhood N_D of each K_D lies in the open set O_{G_D} of points whose dual graph is a contraction of G_D. This is possible because K_D is compact and K_D ⊂ Δ_{G_D} ⊂ O_{G_D}.
  - Choose ρ_* also below the Lebesgue number of a finite cover of K_D by plumbing charts.
  - Then for z ∈ K_D and X ∈ M_g with d(X,z) ≤ ρ_*, X lies in a chart at z. The node curves of z are well defined on X, up to Aut(z).
  - The non-node curves have hyperbolic length ≥ ℓ_0(r) > 0, by continuity of the hyperbolic metric in plumbing families (Wolpert/Masur, cited) and compactness of N_D.
  - Hence Ext_X ≥ ℓ_0²/(2π(2g−2)) for non-node curves, and (a) holds with δ below this bound. As stated, (a) silently needs this shrinking: points within the original ρ_* of K_D can lie near deeper strata.
- **(b0)** 2η < d(Y_0, ∂M̄_{g_i,n_i}).
- **(b1)** 2η < min{ d(σY_0, Y_0) : σ ∈ S_{n_i}, σY_0 ≠ Y_0 }. This is the labelled versus unlabelled issue: the stopping rule uses labelled distance, while "≅ Y_0" is unlabelled.

**Check of the step.** Let s ≤ T_n be a travel time on D, and z_s ∈ K_D with d(z_s, γ_n(s)) ≤ ρ_n.
- Since s ≤ T_n, every curve of ∂Σ_i has Ext ≤ δ at γ_n(s). By (a)/(a′) they are node curves of z_s.
- Hence ψ(z_s) ∈ M̄_{g_i,n_i} is defined.
- **Uniform continuity of ψ.** ψ depends on (X, isotopy class of Σ_i). It is continuous near pinched points, and the dependence on the auxiliary pants decomposition disappears in the limit ℓ(∂Σ_i) → 0. There are finitely many Mod-classes of pairs (z, subsurface bounded by node curves of z), and the z range over the compact set ⋃K_D. So ψ is uniformly continuous there, and d(ψ(γ_n(s)), ψ(z_s)) = o(1) uniformly in s.
- So d(ψ(z_s), Y_0) ≤ η + o(1) < 2η. By (b0), ψ(z_s) is smooth: Σ_i contains no node curve of z_s, and the Σ_i-side is a single vertex c of D.
- By (b), c is a constant vertex of D whose value class is [Y_0]. By (b1), and continuity of the labelled value along the travel, its labelled value is Y_0.
- Then Ext_{γ_n(s)}(∂Σ_i) = o(1), because these are node curves of z_s and d → 0 uniformly on the compact set N_D. Also d(ψ(γ_n(s)), Y_0) = o(1).
- So for n large, neither stopping condition holds at a travel time. T_n lies in an excursion, at some Q ∈ Σ.

**Verified with (R-a).**

## 4. Step 3 (point 4): gap for an arbitrary lift; repaired by the canonical lift (R-b)

**The gap.** Lifting through Def(J) → Def(J)/Aut(J) (Bredon, cited: paths lift through quotients by compact groups) is not unique. At a time s where γ_n(s) = q(ỹ) with Stab(ỹ) ≠ 1, a lift may continue as h·(lift), h ∈ Stab(ỹ). Then:
- h acts on the fibre curve as an automorphism and permutes the vanishing cycles, e ↦ h(e);
- after the switch, the T_g-marked curves ∂Σ_i correspond to the edges at h(x), not at x.

So with an arbitrary Bredon lift the chart label x is **not** well defined. The text's sentence "the T_g-marking along γ_n is compatible with the chart" is true only for a specific lift, which it does not specify.

**Repair (R-b).** The facts below are cited from memory (Abikoff, Bers; Hubbard–Koch's analytic construction of M̄_g; Wolpert).
- Let J̃ be a point of augmented Teichmüller space T̄_g over J.
- Stab(J̃) ⊂ Mod_g sits in an exact sequence 1 → Tw → Stab(J̃) → Aut(J) → 1, where Tw ≅ Z^{E(J)} is generated by the Dehn twists about the node curves α_e.
- There is a Stab(J̃)-invariant neighbourhood U of J̃, precisely invariant (gU ∩ U = ∅ for g ∉ Stab(J̃)), with:
  - U/Tw ≅ Def(J) (the plumbing/Kuranishi chart);
  - U/Stab(J̃) ≅ Def(J)/Aut(J), a neighbourhood of J in M̄_g;
  - U° := U ∩ T_g → Def(J)° a covering. Tw is torsion-free and acts properly, hence freely.

Construction of the canonical lift:
- The ray γ_n is given in T_g from the start, as the Teichmüller geodesic of the marked (X̃_n, q_n). This is the path marking.
- During an excursion at J the T_g-path is connected and lies in the preimage of B(J,2r) ⊂ B(J,3r) ⊂ image of U. That preimage is the disjoint union of the translates gU, so the path lies in a single translate. Replace J̃ by gJ̃ (relabel the marking).
- Define γ̃_n := image of the T_g-path under U → U/Tw = Def(J). This is a continuous lift into Def(J)°, determined up to one global element of Aut(J). No choice is made at orbifold points.

Consequences:
- Each node curve α_e of J̃ is a fixed marked curve on S_g. It is pinched exactly where s_e = 0, and it is Tw-invariant.
- The components of S_g ∖ ⋃_e α_e are marked subsurfaces Σ_y, one for each vertex y of J.

**Entry.** Let s be the entry time, a travel time on D. Let z_s be as in Step 2, and z̃_s the lift of z_s close to γ̃_n(s); it lies on a lifted branch β̃ of D at J. The node curves of z_s, in the marking of U, are the α_e with s_e(z̃_s) = 0. The Σ_i-side is the constant vertex c ≅ Y_0, and it corresponds to a connected subgraph S_c of J.
- **S_c is a single vertex x with no internal edge.** Suppose S_c had an edge f. Then s_f ≠ 0 along β̃ ∖ {0}, but s_f → 0 at 0. So the hyperbolic length of α_f inside the c-component would tend to 0 (continuity of hyperbolic metrics on plumbing families, cited). That component is constant, equal to Y_0, and α_f is essential and non-peripheral in it, so its length is the constant ℓ_{Y_0}(α_f) > 0. Contradiction.
- Hence c = {x}, all edges of J at x are pinched along β̃, and **Σ_i = Σ_x as marked subsurfaces**, with ∂Σ_i = {α_e : e at x}.

**Persistence.** Σ_i (path marking) and Σ_x (marking of U) are both fixed marked subsurfaces, and the path stays in U. So the identity Σ_i = Σ_x holds throughout the excursion.

**Exit.** Step 2 on D′ gives c′ = {x′} along the lifted branch β̃′ through z̃_{s′}, with Σ_i = Σ_{x′}. Then Σ_x = Σ_{x′}, so x′ = x.
- Remark: equality of the boundary-curve sets alone would not suffice. If J has two vertices joined by all its edges, x and x′ have the same edge set. The subsurface identity is what fixes the label.

**Verified with (R-b).** Orbifold points cause no trouble for the canonical lift, because it is never produced by lifting through T_g → M_g. It is the given T_g-path, pushed down by an honest covering.

## 5. Step 4 (point 5): correct, given (R-b)

- Fix (r, δ, η). Endpoint types (Q, D, Aut-orbit of (β̃, x)) form a finite set. Pass to a subsequence of n on which the type is constant, and normalise lifts by the global Aut(J) element.
- Let z̃_n be a lift of a boundary point within ρ_n of γ_n(T_n), chosen near γ̃_n(T_n). A subsequence converges to z̃^∞ ∈ q^{-1}(B_0) ∩ closure(B̃(Q,2r)).
- **F_x(0) = Y_0.** On L_x := {s_e = 0 for all e at x} the x-component F_x is holomorphic, and β̃ ⊂ L_x with F_x ≡ Y_0 on β̃ ∖ {0}.
- **z̃^∞ ≠ 0.** Suppose z̃^∞ = 0. Then γ̃_n(T_n) → 0, so Ext(α_e) → 0 for every e at x, and ψ(γ_n(T_n)) → ψ(J̃) = F_x(0) = Y_0. Both use Σ_i = Σ_x from (R-b). For large n both stopping conditions then fail at T_n, a contradiction.
- So z̃^∞ ∈ b̃ ∖ {0} for a lifted branch b̃ at Q. In the chosen ball, B_0 ∩ B(Q,3r) is the union of the branches. Pass to a further subsequence on which one stopping condition holds for all n.
  - **Ext(α_e) = δ for some e at x.** If s_e(z̃^∞) = 0, then Ext_{γ_n(T_n)}(α_e) → 0 (Maskit), contradicting = δ. So s_e(z̃^∞) ≠ 0. Since b̃ ∖ {0} lies in one stratum, e is unpinched on all of b̃ ∖ {0}: **MERGE**.
  - **d(ψ, Y_0) = η.** If some edge at x is unpinched along b̃, we are in MERGE. Otherwise b̃ ⊂ L_x, and continuity of ψ with Σ_i = Σ_x gives d(F_x(z̃^∞), Y_0) = η > 0, while F_x(0) = Y_0. Here F_x(z̃^∞) is a smooth curve because all edges at x are pinched. So F_x is non-constant on b̃: **MOV**.
- In particular b̃ ≠ β̃, as it must be.

**Verified.**

## 6. Lemma S′ and Step 5 (point 6)

### 6.1 The coarse Lemma S′ is correct
- **γ_n avoids Z.** V_0 is smooth, so V_0 ⊂ Reg X and V_0 ∩ W = (X ∖ Z) ∩ W.
- **Local sheets.** Each irreducible germ X_k has connected regular part in a Milnor ball. Its normalisation over the ball is connected, and removing a proper analytic subset keeps it connected. Distinct X_k meet inside Sing X ⊂ Z. So the components of V_0 ∩ W are the X_k ∩ W ∖ Z.
- **One sheet along a subsequence.** Each γ_n is connected, so it lies in one X_k ∩ W ∖ Z. There are finitely many, so pass to a subsequence with k fixed.
- **Limit points.** X_k ∩ W is closed in W, so z^1 ∈ X_k; note z^1 ∈ W, since it is at distance 2r from Q.
- **Near z^1.** N|_{X_k} is not identically zero on any local component of X_k at z^1, since X_k is the closure of X_k ∖ Z ⊂ M_g. So X_k ∩ ∂M̄_g is empty or of pure dimension 1 at z^1 (active lemma), and it contains z^1.
- Near z^1, B_0 = β, a smooth curve (W ∩ Σ = {Q}). So X_k ⊃ a neighbourhood of z^1 in β. β ∩ W is irreducible, so X_k ⊃ β ∩ W. The same holds for β′.

**Verified** (coarse statement: β and β′ lie in a common sheet X_k of (X, J)).

### 6.2 Upstairs: an arbitrary lift can change component
Here is a local model of reflection type. Let q(u,v_1,v_2) = (u², v_1, v_2) be the quotient by the reflection u ↦ −u. The smooth coarse surface V = {w = v_2²} (w = u²) has preimage {u = v_2} ∪ {u = −v_2}: two smooth sheets exchanged by the reflection, crossing along {u = v_2 = 0} inside the fixed hyperplane.

If V_0 passes through such a point of the reflection locus inside Def(J)°, then q^{-1}(V_0) is locally reducible there. A Bredon lift may arrive along one sheet and leave along the other. So for an **arbitrary** lift, γ̃_n need **not** lie in a single irreducible component of q^{-1}(closure V_0) ∩ B̃. The coarse conclusion of 6.1 then gives only the weaker statement:

> **(W)** some component of q^{-1}(X_k) contains β̃, and the same component contains g·β̃′ for some g ∈ Aut(J).

Proof of (W): the components of q^{-1}(X_k) are permuted transitively by Aut(J). Two distinct orbits of components would both map onto X_k, and a generic fibre is a single Aut-orbit, which forces them to share a component.

### 6.3 Repair (R-c): the canonical lift stays in one component
**Lemma S̃′.** Choose r so small that, in addition:
- B̃(J,3r) is a Milnor ball for (X̃ := q^{-1}X, 0). The irreducible components X̃_1, …, X̃_p of X̃ ∩ B̃ are then representatives of the germ components (cited, conic structure).
- Distinct lifted branches of q^{-1}(B_0) meet only at 0 in B̃, and each lifted branch minus 0 is smooth. There are finitely many pairs of distinct irreducible curve germs at 0, and each pair meets only at 0 in a small enough ball; Puiseux parametrisations give smoothness.

Let the γ̃_n be canonical lifts (R-b) of transition paths whose endpoints converge to z̃^1 ∈ β̃ ∖ {0} and z̃^2 ∈ β̃′ ∖ {0}. Then some X̃_l contains both β̃ and β̃′.

*Proof.*
1. **The path lies on a holomorphic curve in q^{-1}(V_0).** Let F: H → T_g be the Teichmüller disc of (X̃_n, q_n). Since V_0 is totally geodesic and (X_n,q_n) is generating, F(H) lies over V_0. Let R be the connected component of F^{-1}(gU) containing the parameters of the excursion; R is a connected Riemann surface. Put f := (U° → Def(J)°) ∘ F|_R. Then f is holomorphic, f(R) ⊂ q^{-1}(V_0) ∩ B̃, and γ̃_n ⊂ f(R).
2. **f(R) lies in one component.** Each f^{-1}(X̃_l) is an analytic subset of R, and their finite union is R. So one of them has interior, and by the identity theorem it is all of R. Hence γ̃_n ⊂ X̃_{l(n)}, even if f(R) passes through crossing points such as those in 6.2: a smooth connected curve germ cannot change sheets.
3. **Conclusion.** Pass to a subsequence with l(n) = l. X̃_l is closed in B̃, so z̃^1, z̃^2 ∈ X̃_l. X̃_l is irreducible of dimension 2, so X̃_l ∩ {∏ s_e = 0} is nowhere dense in it and has pure dimension 1 at z̃^1. Near z̃^1, q^{-1}(B_0) = β̃, a smooth curve, by the choice of r. So X̃_l contains an open piece of β̃, hence all of β̃. The same argument gives β̃′. ∎

**Step 5 then holds upstairs for every transition, and at the endpoint.** At the endpoint, z̃^2 = z̃^∞ ∈ b̃ ∖ {0}.

## 7. Point 7: dependence on (r, δ, η, n), and existence of one chain

**Order of choices.**
- First r: all conditions of §2.3, the Milnor conditions up- and downstairs, and the branch-separation condition of 6.3.
- Then δ, η, depending on r: (a), (a′), (b), (b0), (b1).
- Then n_0 such that, for n ≥ n_0, ρ_n < min(ρ_*, r/2) and the o(1) terms of Step 2 are below δ and η.

**The gap.** The text implicitly treats the chain as fixed while n → ∞, both in Step 4 and in Step 5 ("over the subsequence these points converge"). But T_n → ∞, and the number of excursions in [0,T_n] can be unbounded in n: the walk may loop around B_0. So the chains for different n need not agree, and "the same transition along a subsequence" is not automatic.

**Repair (R-d).**
- A *transition type* is an Aut(J)-orbit of (J, β̃, β̃′, x); an *endpoint type* is an orbit of (Q, D, β̃, x). Both sets are finite.
- Call a type recurrent if it occurs in the walks of infinitely many n. Let N ≥ n_0 exceed the last n at which any non-recurrent type occurs.
- Fix any n ≥ N and take its walk chain. Every transition of this chain has a recurrent type τ.
  - Along the infinite set of n′ where τ occurs, the corresponding excursions are canonical lifted paths γ̃_{n′} ⊂ q^{-1}(V_0) ∩ B̃(J,2r). Their entry and exit boundary points lie at distance ≈ 2r from 0.
  - A subsequence converges to points of β̃ ∖ {0} and β̃′ ∖ {0}. This is the sequence of paths the chain form requires, and Lemma S̃′ applies to it.
- The terminal type τ_end of the chosen n is also recurrent. Step 4, run along the n′ of type τ_end, supplies b̃, the MERGE/MOV dichotomy and the convergent terminal paths.

So a single finite chain with all required properties exists. The only caveat: the witnessing sequences of paths at different transitions come from different subsequences of walks, not from one common sequence.
- If the downstream argument needs one common sequence n′ for all transitions at once, this is **not** established: the chain combinatorics need not stabilise.
- As far as I can see, the per-transition form listed in the brief needs only per-transition sequences, and that is what is proved.

## 8. Final verdict

**Proved, with repairs (R-a)–(R-d), modulo the cited inputs** (Lemma PA, Lemma NH, Kerckhoff, Maskit, the T̄_g/Def chart description, collar and continuity of hyperbolic metrics in plumbing families, local analytic geometry). There is a chain:
- pieces D^1 ∋ P (D^1 ⊂ ∂V_0), D^2, …, D^k; transition points J_1, …, J_{k−1}; an endpoint Q_0;
- at each J_m: lifts β̃_m, β̃′_m and a single chart vertex x_m, which is the constant vertex ≅ Y_0 (labelled, = Y_0) of D^m along β̃_m and of D^{m+1} along β̃′_m;
- witnessing sequences of canonical lifted paths γ̃_{n′} ⊂ q^{-1}(V_0) ∩ B̃, with endpoints converging to points of β̃_m ∖ {0} and β̃′_m ∖ {0};
- β̃_m and β̃′_m lie in a common irreducible component of q^{-1}(closure V_0) at 0 (upstairs, by Lemma S̃′), and hence in a common sheet downstairs;
- at Q_0, the entering lift β̃ with vertex x and the terminal lifted branch b̃ are joined in the same way, and along b̃ the vertex x is MERGED or MOVING.

**What the original text gets wrong or leaves implicit.**
- (R-a): three extra smallness conditions.
- (R-b): the chart label x is ill-defined for arbitrary Bredon lifts through orbifold points. The canonical lift through augmented Teichmüller space fixes this.
- (R-c): the upstairs same-component claim is false for arbitrary lifts (reflection model). For them only the weaker (W) holds. It is true for the canonical lift, because that lift lies on a Teichmüller disc.
- (R-d): chain combinatorics depend on n. Fixed by recurrent types; the witnessing sequences are per transition.

**Open / not established.**
- A single subsequence n′ witnessing all transitions of one chain simultaneously.
- Anything about the cited inputs themselves (in particular Lemma NH and the T̄_g/Def(J) chart description, which I used in the form stated in §4).

Overall result: **repaired**.

=== END OF ANSWER round10_q10 ===
