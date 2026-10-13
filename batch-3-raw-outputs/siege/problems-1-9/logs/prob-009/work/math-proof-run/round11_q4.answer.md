# round11_q4 — attempt to REFUTE MS11

**Status line.** No counterexample and no contradiction were found: MS11 is **not refuted**. Its status stays **open**. Along the way I prove four things.
- (§1) Logical status. Refuting MS11, by either route, is the same as finding a counterexample to the problem under (Rig). The "derivation" route cannot succeed unless the problem itself is false or some PROVED entry is wrong.
- (§2) An exact reformulation of MS11 in terms of **lift-curve components**: the Y-persistent labels of a transport sheet are exactly the "Y-labels" Y(L) of any lift-curve component L contained in the sheet. This gives a clean proved sufficient condition (1L) and an exact description of what a failure needs.
- (§3) A **twin-free closure theorem**. If Y is non-constant, every piece reachable from ∂V_0 by puncture transitions has a constant vertex φ ≡ Y. There is also a **twin-free t=0 criterion (TFM)** that forces Y to be constant. Both are proved modulo R8-2 Theorem 1 (which uses (Rig)).
- (§4) As a sketch: covering constructions from M_{0,5} satisfy TFM, so they cannot be counterexamples. The flex and gothic loci are not candidates as stated, since they live in M_{1,3}.

The chain question (component-wise wording) is answered in §5. Open questions are listed in §6.

Throughout I use the run's readings (R1), (R2), H_0 = id, (Rig), and its notation (B_t, pieces, Def(Q), q, labels, F_x, transport family Ñ, transport sheet, lift-curve). Results used from earlier rounds are cited by their run labels and were re-read from the brief; they are not re-proved here. Standard analytic-geometry facts are cited from memory: Remmert's finite mapping theorem; the open mapping property of a non-constant holomorphic function on an irreducible germ; the fact that an analytic germ whose complement of a real-codimension-2 set is a connected manifold is irreducible.

**Convention (germs).** As in MS11's choice of B, transport sheets and 3-fold components are taken as irreducible components of germs at (0,0) ∈ Def(Q) × Δ. MS11 already shrinks B so that components of q^{-1}(closure V_0) ∩ B are germ components; I assume the same for closure(Ñ_c̃) and q^{-1}(closure 𝒱). If a sheet as defined in the brief (a component of the closure in B × Δ_ε) does not pass through (0,0), it is irrelevant for MS11 after shrinking B and ε. Write G := Aut(Q), acting on Def(Q) × Δ trivially in t.

## 1. Logical status of a refutation

MS11's setting contains the hypothesis "t ↦ Y_t is non-constant".
- If the problem's conclusion holds for every admissible family satisfying (Rig), then MS11's setting is empty and MS11 is vacuously true. Nothing false can then be derived from MS11 together with true statements.
- Hence route 2 of the task ("derive a known-false statement from MS11 + proved results") can succeed only if (a) the problem is false under (Rig), or (b) one of the PROVED entries used is wrong.
- Route 1 (an explicit configuration) is, by round10_q4 Prop. 1, a counterexample to the problem under (Rig).

So both routes require a counterexample to the problem itself, or an error in the ledger. This explains why local chart models (round10_q3 §3.3, round10_q7 §3, R7-3 §5, round9_q9) never refute MS11: refutation is a global question. The useful outputs of a "refutation attempt" are therefore sharpened **necessary conditions for a counterexample** (§§2–4).

## 2. Lift-curve reformulation of MS11 (proved, modulo R8-2 Theorem 1)

**Notation.**
- Q_t := H_t(Q). It is holomorphic in t (PR-B / R7-3 Lemma 1) and lies in Δ_{G_Q}, since H preserves strata.
- The *lift locus* is Λ := {(p,t) ∈ B × Δ_ε : q(p) = Q_t}. Its irreducible components through (0,0) are the lift-curve components. G permutes them transitively: Λ is the preimage of the irreducible curve germ {(Q_t,t)} under the quotient map q × id, and components of the preimage of an irreducible germ under a finite group quotient form one orbit.
- Fix one lift-curve component L_0 and put H_L := Stab_G(L_0). The lift-curve components are gL_0, g ∈ G/H_L.
- Every point of Λ lies in {s_e = 0 ∀ e}, so every label is intact there.
- For a lift-curve component L, let **Y(L)** be the set of labels y with F_y(p) ≅ Y_t at all (p,t) ∈ L. This is an analytic condition, equivalent to holding at generic points of L.
- By (K3) of R7-3, Y(gL) = g·Y(L). In particular Y(L) is H_L-invariant.
- For a lifted branch c̃ through 0 (Q a puncture of the piece of c), let **𝓛(c̃)** be the set of lift-curve components contained in some transport sheet of c̃.

**Lemma 2.1 (every sheet contains a lift-curve component).** Let c̃ be a lifted branch of a branch c of B_0 at Q, and T a transport sheet of c̃ (a germ at (0,0)). Then T contains some lift-curve component.

*Proof.*
- Let Σ_c be the germ at (Q,0) of closure(H(c × Δ_ε)) ⊂ M̄_g × Δ. By (R1) and (R2) it is a 2-dimensional analytic germ: it is the germ of a component of closure(𝒱) ∩ (closure(Δ_{G_c}) × Δ).
- Σ_c contains the dense subset H((c∖Q) × Δ_ε), which is a connected topological 4-manifold. The rest, {(Q_t,t)}, has real codimension 2. Hence Σ_c is an irreducible germ.
- T ⊂ (q × id)^{-1}(Σ_c), and q × id is finite. By Remmert's finite mapping theorem, (q × id)(T) is a 2-dimensional analytic subgerm of the irreducible 2-dimensional germ Σ_c, so it equals Σ_c.
- In particular, for every small t there is (p,t) ∈ T with q(p) = Q_t. So T ∩ Λ is an analytic subset of T whose projection to t contains a neighbourhood of 0. Hence T ∩ Λ contains a curve through (0,0) not contained in {t = 0}, i.e. a lift-curve component. ∎

**Lemma 2.2 (persistent labels of a sheet).** In the situation of Lemma 2.1, assume (P): Q is a puncture of the piece of c. Let T be a transport sheet of c̃, L ⊂ T a lift-curve component, and y a label. Then
 y is Y-persistent on T ⟺ y ∈ Y(L).
In particular, Y(L) is the same for all lift-curve components L ⊂ T.

*Proof.*
- (⇒) Evaluate the persistence condition at the points of L ⊂ T.
- (⇐) Let A_y := {(p,t) ∈ T : s_e(p) = 0 for all e at y, and class F_y(p) = class Y_t in 𝔐}. This is a closed analytic subset of T (F_y is holomorphic on L_y, and Y is holomorphic by PR-A).
- Let t be generic in the sense of R8-2 §3, i.e. t ∉ Z, where Z is discrete. Let (p,t) ∈ L. Then Q_t is a puncture of the transported piece (H preserves strata and pieces), and y is a Y_t-copy at p.
- Every branch of the curve T_t = T ∩ {t} at p is a lifted branch of the transported branch c_t at Q_t, because T_t ⊂ q^{-1}(closure c_t). By R8-2 Theorem 1 (IMOV is excluded at a puncture), y is STAY along each such branch: it is intact, and F_y is constant, equal to F_y(p) ≅ Y_t.
- So A_y contains the germ of T_t at (p,t). This germ is 1-dimensional, because T is an irreducible 2-dimensional germ and t ≢ 0 on T.
- This holds for all t ∉ Z near 0, an uncountable set. An analytic set of dimension ≤ 1 has 1-dimensional fibres over at most countably many t. Hence dim A_y = 2, and A_y = T since T is irreducible. ∎

**Proposition 2.3 (exact reformulation).** Under the hypotheses of MS11 the following hold.
- The labels Y-persistent on some transport sheet of c̃ are exactly ⋃_{L ∈ 𝓛(c̃)} Y(L).
- MS11 for (Q, β̃, b̃, x) is equivalent to: if x ∈ Y(L) for some L ∈ 𝓛(β̃), then x ∈ Y(L′) for some L′ ∈ 𝓛(b̃).

*Proof.* Combine Lemmas 2.1 and 2.2. ∎

**Corollary 2.4 (sufficient condition (1L), proved).** Suppose some irreducible 3-dimensional component X of the germ of q^{-1}(closure 𝒱) at (0,0) satisfies:
- X contains a transport sheet of β̃ on which x is persistent, and some transport sheet of b̃;
- X contains exactly one lift-curve component.

Then MS11 holds for (Q, β̃, b̃, x).

*Proof.* Both sheets lie in X, so by Lemma 2.1 both contain the unique lift-curve component L ⊂ X. By Lemma 2.2, x ∈ Y(L) is persistent on the b̃-sheet. ∎

**Corollary 2.5 (anatomy of a failure, proved).** Suppose MS11 fails for (Q, β̃, b̃, x), and let L ∈ 𝓛(β̃) with x ∈ Y(L). Then:
1. L ∉ 𝓛(b̃): no sheet of b̃ contains L. In particular |G·L| ≥ 2, i.e. H_L ≠ G. This recovers the necessary condition |Aut(Q_t)| < |Aut(Q)|.
2. 𝓛(b̃) ≠ ∅ (Lemma 2.1), and every element of 𝓛(b̃) is gL with x ∉ g·Y(L). The persistent labels gx on b̃-sheets are twins of x, Y_0-copies different from x. The required α moving x is any such g.
3. By Lemma B1(a), at t = 0 the labels in g·Y(L) are intact and ≡ Y_0 along b̃. So the piece E_b of b has a constant vertex with φ ≡ Y that is **not** x along b̃ (a "staying twin").
4. The persistent sheet of β̃ and every sheet of b̃ contain disjoint sets of lift-curve components. So any 3-fold component X containing sheets of both contains at least two lift-curve components L, gL. Hence (1L) fails, by one of two mechanisms:
   - **(F-a)** S × {0} lies in two different 3-fold components X ≠ X′. This needs S to lie in the fixed locus of some σ ∈ G that is not in the generic stabiliser of the time-t surfaces (the planner's (β)-edges).
   - **(F-b)** a single X contains several lift-curve components.

**Relation to the planner's Mechanism D.** In this language the label-change rule of the planner's sketch (§4 of the brief) is automatic.
- Two sheets that share a lift-curve component have the same persistent labels (Lemma 2.2). This is the (α)-edge statement, without Lemmas I1/I2.
- Labels change only between sheets that contain different lift-curve components L ≠ gL, and the change is y ↦ gy.
- Grothendieck connectedness of X ∩ {N = 0} ∖ {(0,0)} therefore yields MS11 only if one can show that the lift-curve components met along a connecting path are related by elements g with x ∈ g·Y(L). Connectedness alone does not give this, and I found no global input that does. This is where the Mechanism-D attempt stops.

## 3. Twin-free closure of the Y-network, and a twin-free t = 0 criterion (proved, modulo R8-2 Theorem 1)

The twin problem comes from following the *marked* copy x. Membership statements that do not track a particular label can be transported with no twin problem at all. This section makes that precise. It yields necessary conditions for a counterexample that involve V_0 only.

**Definitions.**
- For a piece E at t = 0 and a vertex c constant on E, φ_c(t) is the value of c on E_t = H_t(E). It is holomorphic by R7-3 Lemma 1(a).
- 𝒩 is the set of pieces E (at t = 0) having a constant vertex c with φ_c ≡ Y.
- 𝒩_0 ⊃ 𝒩 is the set of pieces having a constant vertex with value ≅ Y_0.
- A *puncture* of E is a point of closure(ξ(E)) outside the stratum Δ_{G_E}. Pieces are closed in their stratum, so this is the same as a point of closure(ξ(E)) ∖ ξ(E).
- **ℛ** is the smallest set of pieces with these two properties:
  - it contains every piece of ∂V_0;
  - **(PT)** if E ∈ ℛ, Q ∈ closure(ξ(E)), and E′ is a piece of which Q is a puncture, then E′ ∈ ℛ.

**Proposition 3.1 (ℛ ⊂ 𝒩).** Assume (R1), (R2), (Rig), and that Y is non-constant. Then every piece in ℛ has a constant vertex c with φ_c ≡ Y. In particular ℛ ⊂ 𝒩_0.

*Proof.* Pieces of ∂V_0 lie in 𝒩, via the vertex i. It remains to show that 𝒩 is closed under (PT). Let E ∈ 𝒩 with constant vertex c, φ_c ≡ Y. Let Q ∈ closure(ξ(E)), and let E′ be a piece with Q as a puncture.
- Let t ∉ Z be generic (R8-2 §3) and let q be any lift of Q_t = H_t(Q).
- Take a lifted branch of E_t through q, or the lifted germ of E_t if Q_t ∈ ξ(E_t). Along it, the constant vertex c is a single label z, intact at q, with F_z(q) = φ_c(t) = Y_t: a constant vertex has a smooth limit (R7-3 §1).
- E′_t has Q_t as a puncture, since H preserves strata and closures (PR-B). E′_t has a lifted branch through q, because q is an open map.
- By R8-2 Theorem 1, IMOV is impossible since Q_t is a puncture of E′_t. So z is STAY: z is a constant vertex of E′_t with value Y_t, and (W, z) is a Y-vertex.
- E′_t has finitely many vertices, identified with those of E′ by transport. So some vertex c′ of E′ is constant with φ_{c′}(t) = Y_t for uncountably many t. By the identity theorem φ_{c′} ≡ Y, i.e. E′ ∈ 𝒩. ∎

Note that no label is tracked across Q here: q is an arbitrary lift, and the conclusion is about *some* vertex of E′. This is why twins play no role.

**Corollary 3.2 (criterion R).** Under (R1), (R2), (Rig): if some piece reachable from ∂V_0 by puncture transitions has no constant vertex isomorphic to Y_0, then Y_t = Y_0 for all t.

*Proof.* Proposition 3.1 shows that Y is constant, and Y_t = Y_0 by PR-A. ∎

**Theorem 3.3 (twin-free merge criterion, TFM).** Assume (R1), (R2), (Rig). Suppose there are a point Q ∈ B_0, a piece E′ ∈ ℛ with Q ∈ closure(ξ(E′)), and a piece E″ of which Q is a puncture, such that the following condition holds.
- **(TF)** For every lifted branch (or lifted germ) ẽ′ of E′ at 0 ∈ Def(Q), every label z that is intact and ≡ Y_0 along ẽ′, and every lifted branch ẽ″ of E″ at 0, the label z is *not* intact-and-≡ Y_0 along ẽ″.

Then Y_t = Y_0 for all t.

(TF) holds vacuously if E′ has no constant vertex ≅ Y_0. It concerns V_0 and t = 0 only.

*Proof.* Suppose Y is non-constant. By Proposition 3.1, E′ has a constant vertex c with φ_c ≡ Y.
1. Let 𝔗′ (respectively 𝔗″) be the germ at (0,0) of the closure of q^{-1}(H(β′ × Δ_ε)), where β′ ranges over the branches of E′ at Q (respectively of E″). Each is a finite union of irreducible 2-dimensional germs ("sheets"), by the argument of Lemma 2.1.
2. For each generic t near 0, pick a lift q_t of Q_t.
   - As in the proof of 3.1, there is a branch of 𝔗′_t through (q_t,t) along which some label z_t is intact with F ≡ Y_t (the label of c).
   - There is also a branch of 𝔗″_t through (q_t,t) along which z_t is STAY (R8-2 Theorem 1).
3. There are finitely many sheets, labels and lift-curve components, and uncountably many t. So we may fix a sheet T′ ⊂ 𝔗′, a sheet T″ ⊂ 𝔗″, a label z and a lift-curve component L, such that for uncountably many t the point (q_t,t) lies on L, with both branches in T′ and T″ respectively and z_t = z. Then L ⊂ T′ ∩ T″, since an irreducible curve meeting an analytic set in uncountably many points lies in it.
4. The argument of Lemma 2.2 (the analytic set A_z is 2-dimensional) applies on T′ and on T″. So z is intact with F_z ≅ Y_t on all of T′ and on all of T″.
5. T′ ∩ {t = 0} and T″ ∩ {t = 0} are 1-dimensional, since t ≢ 0 on these irreducible 2-dimensional germs. By H_0 = id they lie in the union of the lifted branches of E′, respectively of E″, at 0. So some lifted branch ẽ′ ⊂ T′_0 and some ẽ″ ⊂ T″_0 carry z intact and ≡ Y_0.
6. This contradicts (TF). Hence Y is constant, and Y_t = Y_0 by PR-A. ∎

**Corollary 3.4 (necessary conditions for a counterexample to the problem, under (Rig)).** If Y is non-constant, then V_0 satisfies both of the following.
- **(NC1)** Every piece reachable from ∂V_0 by puncture transitions carries a constant component ≅ Y_0.
- **(NC2)** For every Q ∈ closure(⋃_{E∈ℛ} ξ(E)), every E′ ∈ ℛ with Q ∈ closure(ξ(E′)), and every piece E″ of which Q is a puncture, there are lifts ẽ′ of E′ and ẽ″ of E″ at 0 ∈ Def(Q), and a label z, intact and ≡ Y_0 along both. That is, every Y_0-copy can be "continued" from E′ to E″ by some twin.

These are V_0-only conditions; no deformation appears in them. Any explicit counterexample to MS11 (hence to the problem) must satisfy them at every point of the reachable network, not just at one non-product point Q. In particular, at the chain endpoint where MS11 would fail, Corollary 2.5(3) and (NC2) agree: E_b carries a staying twin.

## 4. Candidate surfaces

### 4.1 Covering constructions from M_{0,5} (sketch: they satisfy TFM, so they are not counterexamples)
**Setting and assumptions (A).**
- V_0 is the image in M_g of the covering construction attached to a branched cover C → P^1 whose branch locus is the five marked points, each genuinely branched.
- closure(V_0) is described by admissible covers over M̄_{0,5}, followed by stabilisation. This is standard, cited from memory.
- Assume moreover that over the boundary points of M̄_{0,5} used below, every component of the admissible covering curve is already stable, so stabilisation contracts nothing.
- Let Δ_Γ be the stratum of the image of D_{12}°: the points 1, 2 collide, the base is R_{12} ∪_{n} R_{345}, and the pieces of ∂V_0 come from D_{12}. Y_0 is a component over R_{12}, with its node points as special points.
- Smoothness of V_0 is not used. (Covering constructions are often not smooth, e.g. the quintic example of PR-I.)

**Argument.**
- Let Q be the image of D_{12} ∩ D_{34}. The base is R_{12} —n1— R_5 —n2— R_{34}.
- Q is a puncture of the ∂V_0 piece E″ (the D_{12} piece) and of the piece E′ of D_{34}. Hence E′ ∈ ℛ by (PT).
- The constant vertices of E′ are the components over R_{34}: they cover a fixed 3-pointed sphere. The components over the moving 4-pointed component R_{125} are the non-constant ones (generically).
- Every component z over R_{34} maps onto R_{34}, so it carries a preimage of n2, and that is a node of the covering curve (by (A) this node survives stabilisation).
- Moving from Q into D_{12} smooths n2, hence smooths every node over n2. So such a z is merged along **every** lift of the E″ branch.
- Thus (TF) holds: vacuously if no component over R_{34} is ≅ Y_0, and because every such twin merges otherwise.
- By Theorem 3.3, Y_t = Y_0 under (Rig).

This recovers PR-I Proposition 3 (the quintic case, where the twin C over R_{34} sits inside the moving vertex along ∂V_0) without using (O) or Krull at time t, and extends it to all covering constructions from M_{0,5} satisfying (A).

The sketch status is due to (A) and to the admissible-cover description, which are cited, not proved. Without (A), a rational bridge over R_5 could be contracted. A component over R_{34} might then stay intact and constant along D_{12}, giving a staying twin, and (TF) can fail. I did not analyse that case.

### 4.2 Other candidates
- **Loci in the hyperelliptic locus of genus 3** (round10_q4 §4(c)). The totally geodesic surfaces I know there are covering constructions from M_{0,5} (cited from memory, not checked). For them §4.1 applies when (A) holds. I could not determine whether smooth examples violating (A) exist.
- **Flex and gothic loci** (cited from memory: Mirzakhani–McMullen–Mukamel–Wright / Eskin–McMullen–Mukamel–Wright). These are primitive totally geodesic surfaces in **M_{1,3}**, not in M_g. They are not admissible V_0 for the problem as stated, which concerns closed subvarieties of M_g, so they are not candidates here. I do not know a primitive totally geodesic surface in an unmarked M_g to test.
- **Explicit configuration for MS11.** By Corollaries 2.5 and 3.4, a counterexample needs all of the following:
  - a V_0 satisfying (NC1) and (NC2) at every point of the reachable network (staying twins everywhere);
  - a non-product point Q with |G·L| ≥ 2;
  - a failure of (1L) via (F-a) or (F-b).

  I found no surface with even (NC1) together with a non-product twin point, other than symmetric covering constructions. Those violate (NC2) by §4.1 (under (A)). **Attempt stopped here: no counterexample.**

## 5. Is the component-wise wording enough for the chain (steps 2(c), 2(d))?

Yes, as far as I can check, provided Lemma B1(a) and entry 100's transfer hold as stated.
- **Endpoint 2(d).** The chain needs one sheet T of b̃ on which x is persistent. Lemma B1(a) gives a non-empty open subset of b̃ ∖ 0 at t = 0 on which x is intact and ≡ Y_0. The identity theorem along b̃ then contradicts MERGE or MOV. "Some sheet" is exactly what is needed.
  - Lemma 2.2 gives an independent route to the open set: T ∩ {t = 0} is 1-dimensional and contained in the lifted branches of b, and A_x = T.
  - One point should be checked in B1(a): that T ∩ {t = 0} lies in b̃ itself and not in another lift σb̃. If it lay in σb̃, one would get x intact along σb̃, i.e. σ^{-1}x along b̃. That is a twin, not x, and the contradiction would be lost.
- **Transfer 2(c).** Persistence of x on a sheet of β̃′_m is an analytic identity (A_x = sheet) on an irreducible set. It therefore continues along the irreducible travel family of D^{m+1} (entry 100; R7-3 Lemma 2, steps 3–4, where pattern and label data are constant on irreducible families) to every sheet of β̃_{m+1} contained in that travel family. "Some sheet" again suffices.
  - The point to watch is the same: the label carried along must be the t = 0 continuation of x_m, not an Aut(G)-relabelling. For non-product strata of D^{m+1}, the sheet's slice may lie over ρE_t rather than E_t inside the same lifted family W (R8-2 Lemma U). I did not re-verify the R(D) repair that is said to fix the label; I flag it.
- **Simplification.** By Lemma 2.2, the induction claim can be stated as "x_m ∈ Y(L) for some L ∈ 𝓛(β̃_m)", and MS11 as Proposition 2.3. By Proposition 3.1, the piece-level statement (every chain piece lies in 𝒩) is already proved without MS11. Only the label-level statement needs MS11.

## 6. Summary: proved / sketched / open

**Proved** (modulo the cited R8-2 Theorem 1, PR-A, PR-B, R7-3 Lemmas 1–2, Lemma B1(a), and standard analytic facts):
- §1: refuting MS11, by either route, amounts to a counterexample to the problem under (Rig), or an error in a PROVED entry.
- Lemma 2.1: every transport sheet contains a lift-curve component.
- Lemma 2.2: the persistent labels of a sheet are exactly Y(L) for any lift-curve component L in it.
- Proposition 2.3: the exact reformulation of MS11.
- Corollary 2.4: the sufficient condition (1L).
- Corollary 2.5: the anatomy of a failure, with mechanisms (F-a) and (F-b).
- Proposition 3.1: ℛ ⊂ 𝒩, twin-free.
- Corollary 3.2: criterion R.
- Theorem 3.3: the twin-free t = 0 criterion TFM.
- Corollary 3.4: the necessary conditions (NC1), (NC2) for a counterexample.

**Sketched:**
- §4.1: covering constructions from M_{0,5} under (A) satisfy TFM, hence the conclusion under (Rig).
- §5: the component-wise wording suffices for the chain, with two flagged checks (B1(a) lands in b̃ itself; label consistency in the transfer for non-product pieces).

**Not proved / open:**
- **MS11 itself: open, neither proved nor refuted.** Precisely where each attempt stopped:
  - Mechanism D: connectedness does not control which lift-curve components are met (§2, end).
  - (1L): no general reason why a 3-fold component should contain only one lift-curve component; both (F-a) and (F-b) are unexcluded.
  - Counterexample search: no V_0 known satisfying (NC1) and (NC2) with a non-product twin point.
- **New open targets, V_0-only (t = 0), twin-free, and each sufficient for the problem under (Rig):**
  - (MS-R): ℛ ⊄ 𝒩_0;
  - more generally (MS-TF): the hypothesis of Theorem 3.3 holds at some point.

  A twin-free version of Proposition K would prove (MS-R). It would use the Mod-invariant functional 𝔪(X) = inf over subsurfaces Σ of type Σ_i of [max Ext(∂Σ) + d(ψ_Σ(X), Y_0)] instead of the marked Σ_i. Its endpoint branch would lie on a piece with no constant Y_0-component, i.e. outside 𝒩_0. The gap is termination: along the chosen Teichmüller rays some twin subsurface might keep a short boundary and ψ ≈ Y_0 forever. Lemma NH only lengthens ∂Σ_i of the marked subsurface. Interior (IMOV) transitions would also have to be handled, as in entry 99.
- (Rig) (entry 82) remains open, as before.

=== END OF ANSWER round11_q4 ===

