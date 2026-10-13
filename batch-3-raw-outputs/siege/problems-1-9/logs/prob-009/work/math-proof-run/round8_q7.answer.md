# round8_q7 — answer (fresh-lens attempt on MS8)

**Status line / plan.** (1) Check MS8 + (Rig) ⇒ the problem's claim. (2) First move, not on the tried list: a *structure lemma* that (Rig) by itself gives — every piece is literally K° × {constant point}, so only the constant-vertex values move with t. Then a *junction lemma* listing exactly the configurations in which Y_t is not pinned, and finally a *normal-bundle / plumbing-ratio (Abel–Jacobi) constraint* on crossing pieces. Outcome: a partial result. MS8 is reduced to one explicit residual configuration (a "sliding crossing"), and that configuration is excluded when the crossing piece has positive genus and only one moving attachment point enters a ratio. MS8 in full is NOT proved, and no counterexample was found.

## Step 1. MS8 + (Rig) ⇒ the problem's claim

The setting of MS8 is the problem's setting under the readings (R1) and (R2). There are two small additions:
- g ≥ 2;
- dim M_{g_i,n_i} > 0. If dim M_{g_i,n_i} = 0, the space M_{g_i,n_i} is a point, so Y_t = Y_0 trivially.

MS8's extra hypothesis is (Rig), which R-Rig asserts for every admissible family. MS8's conclusion is word for word the problem's conclusion. So MS8 ∧ R-Rig ⇒ the claim. This is valid relative to the readings: (R2) formalises "smoothly trivial" together with (i) and (ii), and (R1) is the closedness of closure(𝒱).

One point needs a remark. The problem says V_0 is "smooth", while MS8 says "smooth closed". "Closed" just means closed in M_g, which "subvariety" includes. Nothing in the derivation goes wrong, and MS8 is not implausible on its face: see §5.

## Step 2. First move: (Rig) forces pieces to be products K° × {c(t)}

Conventions. Work at a fixed time t. By Chow's theorem, closure(V_t) is algebraic (closed analytic in the projective M̄_g, via (R1)), so all the sets below are algebraic.

**Lemma S (structure of pieces under (Rig)).** Let E be a piece at time t in a stratum G, with M = M(E). Write c_u (u ∉ M) for the constant values of f_u. Then E = (K(E) ∩ ∏_{u∈M} M_u) × {(c_u)_{u∉M}} exactly. Moreover Ē is the normalisation of K(E), and the maps f_u (u ∈ M) are the coordinate projections composed with K̃ → K. Hence, by (Rig), the curve Ē and the maps f_u (u ∈ M(E)) come from a t-independent finite list. Only the constant values c_u move.

*Proof.* E is an irreducible component of ξ_G^{-1}(closure(V_t) ∩ Δ_G), which is closed in ∏_w M_w. So E is a closed irreducible 1-dimensional algebraic subset. Because f_u is constant for u ∉ M, we have E = E^M × {c}, where E^M is closed irreducible 1-dimensional in ∏_{u∈M} M_u. The closure K = K(E) is an irreducible curve. Since K is not contained in the boundary, K° := K ∩ ∏_M M_u is a nonempty Zariski-open subset of K, hence irreducible of dimension 1. Then E^M ⊂ K° is a closed 1-dimensional subset of the irreducible curve K°, so E^M = K°. The closure of E in ∏ M̄_w is K × {c}, so its normalisation is K̃. ∎

**Corollary S′ (puncture values and fibres are rigid).** Fix a triple (G, M, K) ∈ 𝒦. Then:
- (a) The set Φ_K of all points of K ∖ K° is finite. Hence so is the set of their coordinates and of the components of these stable curves. Thus the puncture values f_u(p), u ∈ M, of any piece of type K, and all their components, lie in a finite set Φ that is independent of t.
- (b) For u ∈ M and any point z ∈ M̄_u, the set {k ∈ K : pr_u(k) = z} is finite, because pr_u|_K is non-constant on an irreducible curve.

**Lemma S″ (pieces are carried to pieces; K(E_t) is t-independent).** Each stratum restriction of H_t is a homeomorphism of 1-dimensional analytic sets, so it maps irreducible components to irreducible components. The reason is that the irreducible components of a curve X are the closures of the connected components of the set of points where X is a topological 2-manifold: unibranch points are exactly the points with disc neighbourhoods, and multi-branch points form a finite set. Write E_t for the piece corresponding to E_0, with a lift chosen locally continuously in t.

Then t ↦ K(E_t) is locally constant, hence constant on Δ, up to Aut(G). Suppose t_n → t* and K(E_{t_n}) = K′ for all n. H is continuous, so each point of E_{t*} is a limit of points of E_{t_n}. Since K′ is closed, K(E_{t*})° ⊂ K′, and therefore K(E_{t*}) = K′, both being irreducible curves. As 𝒦 is finite, this gives local constancy.

*Caveat (this is where "twins" live).* The constant values c_u(t) are holomorphic as points of Δ_G / Stab. A *lift* to labelled vertices can be branched at isolated values of t, for example {c_u, c_{u′}} = {±√t}, when an automorphism of G exchanges two constant vertices whose values coincide at that t. For the vertex i of the product-type stratum Γ there is no ambiguity, and Y_t is holomorphic (R-Hol).

## Step 3. Junction lemma: where Y_t can and cannot escape pinning

Fix t. Let Q ∈ B_t lie in a stratum G′. Since ∂M̄_g is (orbifold-locally) a Cartier divisor and closure(V_t) is an irreducible surface not contained in it, Krull's principal ideal theorem shows that B_t is pure of dimension 1. So every point of B_t lies on the closure of some 1-dimensional piece.

**Lemma J.** Let E be a piece at time t with Q = ν(p) for a puncture p of E (Q ∈ Δ_{G′}, and G′ contracts to G). Suppose a vertex x of G′ is a constant vertex of E with value Z_t, and let E′ be another piece with Q in its closure. Then one of the following holds.

- (J1) *Merge.* Q is a puncture of E′, and x lies inside a vertex u′ of E′ that is degenerate at that puncture. Then u′ ∈ M(E′), and Z_t is a component of the puncture value f_{u′}(p′). Hence Z_t ∈ Φ.
- (J2) *Puncture move.* Q is a puncture of E′, x is a vertex of E′, and x ∈ M(E′). Then Z_t = f_x(p′) ∈ Φ.
- (J3) *Constant.* x is a constant vertex of E′, and Z_t is unconstrained by this junction.
- (J4) *Pinned crossing.* Q is an interior point q of E′, x ∈ M(E′), and some vertex w ∈ M(E′) of G′ lies in a group G′_u with u ∈ M(E). Then q lies in a finite t-independent subset of K(E′), so Z_t = f_x(q) is in a finite t-independent set.
- (J5) *Sliding crossing.* Q is an interior point q(t) of E′, x ∈ M(E′), and every vertex of M(E′) belongs to a group G′_u with u a **constant** vertex of E. Equivalently, every vertex of G′ that is a component of a fixed puncture value of E is constant along E′.

*Proof.*
- **(J1).** If u′ were constant on E′, then f_{u′}(p′) = c_{u′} ∈ M_{u′} would be non-degenerate, contradicting that x lies in a degenerate vertex. So u′ ∈ M(E′), and Corollary S′(a) applies.
- **(J2).** This is Corollary S′(a) again.
- **(J4).** The value f_w(q) is a component of some fixed puncture value f_u(p), so it lies in Φ. Corollary S′(b) then puts q in a finite set, and Z_t = f_x(q) follows.
- **Exhaustiveness.** If Q is a puncture of E′ we are in (J1), (J2) or (J3). If Q is an interior point of E′, then G′ is E′'s stratum, so x is a vertex of E′: either constant, which is (J3), or moving, which is (J4) or (J5).

The finite sets in (J1), (J2) and (J4) are unions over the finite list 𝒦, so they do not depend on t. ∎

**Consequence (pinning criterion).** Let 𝒯 be the set of times t at which there is an *intact chain* from a generic point of ∂V_t to a junction of type J1, J2 or J4 for the copy. An intact chain is a finite chain of closures of pieces along which a chosen component stays a constant vertex, continuing continuously across junctions, so its value is locally constant: on each piece it is a constant vertex, and at a junction an intact component varies continuously. If 𝒯 accumulates in Δ, then Y_t lies in a finite fixed set for t ∈ 𝒯, and R-Hol gives Y ≡ Y_0.

This refines R-time-t. It shows that **the only escape is that, for all t in a nonempty open set U ⊂ Δ, every intact chain from ∂V_t ends only in (J3) or (J5) junctions.** By Lemma S, the escape has a specific shape. All moving vertex data are fixed. At a (J5) junction, E slides along E′: the moving parameter is the attachment point q(t) on the fixed curve K̃(E′). The constant values of E then equal f_w(q(t)) for w ∈ M(E′), and Y_t = f_x(q(t)) runs along the fixed curve pr_x K(E′).

*Remark on t = 0 information.* Suppose Proposition K's endpoint at t = 0 is a MERGE (J1 at t = 0) at a point Q_0. Then Lemma S applied at Q_t := H_t(Q_0) shows that Q_t has, for **all** t, a component with constant value Y_0: it is a component of the fixed puncture value f_{u′}(p′). The MS8 problem is thus exactly the problem of connecting the vertex i at P_t ∈ ∂V_t to this Y_0-component by an intact chain at time t. The obstruction is the branching of lifts at t = 0 (twins), as in R-Known-partial. Lemma S shows the twin ambiguity is the *only* non-rigid datum. Everything else on the network is rigid.

*Why twins are genuinely topological (and not removable by choosing t generic).* Take a stable curve Q_0 and its Kuranishi chart Def(Q_0), on which Aut(Q_0) acts. In the chart, components are labelled consistently until they merge. A path lifts through a finite-group quotient, but a 2-parameter family (chain × [0, t]) need not. Example: z ↦ z² from C to C/±1 admits no continuous lift of the identity map of a disc around 0. So the copy tracked along the t = 0 chain can be continued to time t only if the square chain × [0, t] does not wind around the twin locus. Lemma S does not touch this point.

## Step 4. Normal-bundle / plumbing-ratio constraint on sliding crossings (sketched)

Let E′ be a piece at time t (stratum G′) and let C := K̃(E′) be its normalisation. By Lemma S, C is fixed. Let S̃ → closure(V_t) be the normalisation, a normal surface. Abusing notation, write E′ also for the curve in S̃ over E′.

For an edge e of G′, let s_e be a local defining equation of the boundary branch D_e (in an orbifold chart). Its pull-back to S̃ vanishes along E′ to an order m_e ≥ 1.

**(a) The m_e are independent of t.** A small loop in V_t around E′ has monodromy in Mod_g of the form ∏_e T_e^{m_e}, a product of Dehn twists about the pinched curves. H_s (s ∈ [0, t]) gives a homotopy of such loops inside M_g, so the monodromy is a homotopy invariant, and the m_e are constant. The same argument shows that the vanishing orders of the s_e along the other boundary branches through a junction point are constant in t.

**(b) Ratio function.** For two edges e, f put F_{e,f} := s_e^{m_f} / s_f^{m_e}. This is a meromorphic function on a neighbourhood of E′ in S̃ whose divisor contains E′ with multiplicity 0. Let ρ_{e,f} := F_{e,f}|_{E′}. Changing the coordinates s_e multiplies ρ_{e,f} by a non-vanishing function, so ρ_{e,f} is canonically a meromorphic section of L_{e,f} := N_{D_e}^{⊗m_f} ⊗ N_{D_f}^{⊗(−m_e)} restricted to C.
- At an interior point q of E′ through which no other branch of B_t passes: S̃ is normal there, and div F_{e,f} has no component through q. So F_{e,f} is a unit near q (normal surface: a meromorphic function with zero divisor is a unit), and ord_q ρ_{e,f} = 0.
- Therefore div ρ_{e,f} is supported on two kinds of points: the punctures of C, which are fixed, and the junction points q_j(t) of E′ with other branches of B_t. Its coefficients there are integers fixed by the topology, as in (a).

**(c) The line bundle is fixed.** Cited from memory (standard deformation theory of nodal curves, e.g. Arbarello–Cornalba–Griffiths, *Geometry of Algebraic Curves II*, ch. XI/XIII): on the normalisation of the branch D_e, the normal bundle is ξ^*N_{D_e} ≅ L_h^∨ ⊠ L_{h′}^∨. Here h, h′ are the two half-edges of e, and L_h is the cotangent line at the marked point h of the vertex carrying it. Pull back to C:
- If the vertex carrying h is constant along E′, this factor is a trivial bundle on C.
- If that vertex is moving, the factor is f_u^* L_h^∨, which is t-independent by Lemma S.

Hence the class of L_{e,f} in Pic(C) is independent of t.

**Proposition N (Abel constraint; sketch, subject to (a)–(c) and the orbifold bookkeeping at orbifold points of E′).** For every pair of edges e, f,

  Σ_j a_j^{(e,f)} · q_j(t) ~ D^{(e,f)}  in Pic(C),

where the integers a_j^{(e,f)} and the divisor D^{(e,f)}, supported on the fixed punctures, do not depend on t.

**Corollary N1 (partial pinning of sliding crossings).** Consider a (J5) junction for the Y_t-copy at q_1(t) ∈ C, and suppose:
- genus(C) ≥ 1;
- for some pair (e, f), the only junction point of E′ with nonzero coefficient that is not already pinned (by J1, J2 or J4 data) is q_1(t).

Then a_1 q_1(t) is constant in Jac(C). Multiplication by a_1 composed with the Abel–Jacobi map C → Jac(C) is finite-to-one when genus ≥ 1, so q_1(t) lies in a finite set, Y_t = f_x(q_1(t)) lies in a finite set, and R-Hol gives Y ≡ Y_0.

In the crossing coordinates (x, y), with E′ = {x = 0} and E = {y = 0}, we have s_A = x^a and s_G = x^b y^c (c ≥ 1). So the pair (e ∈ G-edges, f ∈ A-internal edges) has ord_{q_1} ρ = c·a ≠ 0. The nonzero-coefficient hypothesis on q_1 is therefore automatic for that pair. What is not automatic is that no *other* unpinned junction appears in the same relation.

**Dead end (precise).** When C has genus 0, Pic^0(C) = 0 and Proposition N carries no information: every degree-0 divisor is principal. Teichmüller-curve pieces (the pieces carrying area, by R-PA and R-T′) are frequently of genus 0, for example triangle-group Teichmüller curves. Several sliding points in the same relation also escape Corollary N1. So the normal-bundle move does not close MS8.

## 5. Plausibility of MS8 / counterexample search

No counterexample was found. Lemma S shows that a counterexample has to look as follows. For t in an open set:
- the vertex i of ∂V_t is joined by intact chains only to (J3) and (J5) junctions;
- at every (J5) junction a piece slides along a fixed curve K̃(E′) at a point q(t), and every fixed component (from Φ) is constant along E′;
- for each sliding piece, the attachment points satisfy the Abel relations of Proposition N.

Local models of closure(V_t) near such a crossing (a normal-crossing surface germ with branches E, E′) impose no further condition. The missing constraint must therefore be global, and at t = 0 it must come from total geodesicity. Total geodesicity is not available at t ≠ 0, and transporting it is exactly the twin obstruction. I do not find MS8 implausible. On the t = 0 network everything except the twin-branching of constant-vertex lifts is rigid (Lemma S), and the Examples (R-Examples) all resolve through a MERGE.

## 6. Summary: proved / sketched / open

**Proved (given the readings (R1), (R2), the cited statements R-Hol and (Rig) as a hypothesis, Chow's theorem and Krull's theorem):**
- Step 1: MS8 ∧ R-Rig ⇒ the problem's claim.
- Lemma S, S′, S″: under (Rig), every piece at every time is K° × {c(t)} with K t-independent. Puncture values, normalisations and moving-vertex maps are rigid; only constant-vertex values move. The constant values are holomorphic on Δ_G/Stab, while their labelled lifts may branch at isolated t (twins).
- Lemma J and the pinning criterion: Y ≡ Y_0 as soon as, for t in a set accumulating in Δ, an intact chain from ∂V_t reaches a J1 (merge), J2 (puncture-move) or J4 (pinned crossing) junction. The only escape is the "sliding crossing" (J5) configuration, described exactly.
- If Proposition K's t = 0 endpoint is a MERGE, then for all t the transported point H_t(Q_0) carries a component of value exactly Y_0.

**Sketched (relies on standard facts cited from memory: the normal bundle of a boundary branch is L_h^∨ ⊠ L_{h′}^∨, Dehn-twist monodromy, and orbifold bookkeeping):**
- Proposition N (Abel constraint on attachment points of sliding crossings).
- Corollary N1 (pinning when the crossing piece has genus ≥ 1 and a single unpinned attachment point enters some ratio).

**Open:**
- (O1) MS8 itself. Equivalently: (O1a) exclude, for t in an open set, the situation where intact chains from ∂V_t meet only (J3) and (J5) junctions; or (O1b) show that the copy tracked along Proposition K's t = 0 chain continues to small t. That is, show that the square chain × [0, t] does not wind around a twin locus, or that twin-swapped copies both lead to a Y_0-valued merge.
- (O2) Sliding crossings on genus-0 crossing pieces, or with several unpinned attachment points in each Abel relation.
- (O3) (Rig) itself (R-Rig) remains open input, as stated in the task.

=== END OF ANSWER round8_q7 ===

