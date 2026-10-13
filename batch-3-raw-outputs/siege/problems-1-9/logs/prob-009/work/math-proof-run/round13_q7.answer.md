# round13_q7 — answer

**Plan/status.** (1) I re-derive "MS11♭ + (Rig) ⇒ claim" step by step from the listed statements. (2) I attack MS11♭. My first move is not in the tried table: *degenerate the Teichmüller discs of V_0 near Q on the two sides β̃, b̃ of the t = 0 sheet S (area functions of labels).* I combine it with a reformulation of the failure as a choice of lift of the coarse branch b.
Status: (1) done, modulo the cited entries. (2) partial: one reformulation and one t = 0 lemma are proved, and I explain exactly why this move cannot close MS11♭. MS11♭ remains OPEN.

Readings used throughout: (R1) and (R2) as stated in the query, with H_0 = id. The orbifold reading (R2^orb) is **not** used.

---

## 1. Derivation: MS11♭ + (Rig) ⇒ the problem's claim

**Step 0 (trivial case).** If dim M_{g_i,n_i} = 0, then (g_i,n_i) = (0,3) and M_{0,3} is a point, so Y_t = Y_0 trivially. From here on, dim M_{g_i,n_i} > 0, which is the setting of MS11♭.

**Step 1 (holomorphy).** By entries 2/19, t ↦ Y_t is a holomorphic map Δ → M_{g_i,n_i}. So either Y ≡ Y_0, or Y_t ≠ Y_0 for all t outside a discrete set. Suppose, for contradiction, that Y is non-constant. Then every hypothesis of MS11♭ that concerns the family holds: (R1), (R2), (Rig) (assumed), product type of Δ_Γ, dim ∂V_t = 1, and Y non-constant.

**Step 2 (the walk chain at t = 0).** By Prop. K_w with repairs (entries 85, 98), a Teichmüller ray in V_0 from a generic point of ∂V_0 gives a finite walk chain:
- pieces E^0 = ∂V_0, E^1, …, E^m;
- transition points Q^1, …, Q^m, each with an entering lift β̃^k and a leaving lift b̃^k (or a terminal lift);
- the label x tracked by the walk;
- an endpoint of type MERGE or MOV.

Lemma S̃′ (entry 98) puts the entering and leaving lifts of each transition in one irreducible component of q^{-1}(closure V_0) ∩ B. This is hypothesis (S) of MS11♭. Cor. IMOV_all (entry 99) makes every genuine transition and the endpoint a puncture of both adjacent pieces. This is hypothesis (P), and it excludes interior-MOV endpoints, so the endpoint is a MERGE or a puncture-MOV.

**Step 3 (base).** On ∂V_0 the constant vertex i is intact with value Y_0. By (R2) and entry 24, H_t carries ∂V_0 to ∂V_t, on which vertex i has value Y_t. Hence vertex i, read as a label x in the chart at Q^1, is Y-persistent on an anchored sheet of the entering lift β̃^1. Anchored sheets exist by entry 112 (Lemma B1♭).

**Step 4 (induction over transitions).** Suppose x is Y-persistent on an anchored sheet of β̃^k.
- If Q^k lies in a non-product stratum, MS11♭ applies with data (Q^k, β̃^k, b̃^k, x). Its hypotheses (P) and (S) come from Step 2. Its conclusion is that x is Y-persistent on an anchored sheet of b̃^k.
- If Q^k lies in a product-type stratum, Lemma PT (entry 86) says no automorphism moves a positive-dimensional vertex. So there are no twins, the label is unambiguous, and the product-type junction step of entry 113 gives persistence on an anchored sheet of b̃^k. That step uses entries 84–87 and Theorem X′.
- Along a piece between transitions, persistence is constant on whole components of the boundary total space (Lemmas T/S, entry 87). By B1♭ (entry 112), adding the finite sets R(D) keeps the label on one lifted curve. So x is Y-persistent on an anchored sheet of the entering lift β̃^{k+1}.

This is exactly entry 113's chain check, which says MS11♭ supplies steps 2(b)–(d).

**Step 5 (endpoint).** By induction, the track is aligned at every junction, and the endpoint is a MERGE or puncture-MOV of the persistent label x. Theorem R (entry 87) then gives Y_t ≡ Y_0, contradicting Step 1. Hence Y ≡ Y_0.

**Verdict on part 1.**
- The derivation goes through as a formal combination of the listed statements. I could not re-check the proofs of entries 85/98 (walk chain), 87 (Theorem R) and 113 (chain check), since they are not supplied. The derivation is only as sound as those entries.
- MS11♭ is **not implausible in itself**. Its hypothesis contains "Y non-constant", so under (Rig) it is vacuously true if the problem's claim is true (entry 122). Any refutation of MS11♭ would be a counterexample to the problem. Its plausibility is therefore exactly that of the problem's claim.
- The full proof of the claim also needs (Rig) (entry 82), which is still OPEN under the coarse reading (R2).

---

## 2. Attack on MS11♭

**First move (new): degenerate the Teichmüller discs of V_0 near Q on the two sides β̃ and b̃ of the t = 0 sheet S, and compare which labels carry zero limiting area on each side.** Before using it, §2.1 pins down exactly what a failure of MS11♭ looks like.

### 2.1 Lift-curve reformulation (proved from entries 112 and 114)

**Conventions.**
- Aut(Q) acts on Def(Q) and on the labels.
- The stable curve over h·p is identified with the curve over p, with the component labelled hy over h·p corresponding to the component y over p. So F_{hy}(h·p) ≅ F_y(p).

**Lemma 2.1.** Assume the MS11♭ setting with Y non-constant. Let T be an anchored sheet of β̃ on which x is Y-persistent. Let L ⊂ T be a lift-curve of Q_t, and set Λ := Λ(L), the set of labels y with F_y ≅ Y_t along L. Then:

(a) Every lift-curve of Q_t is h·L for some h ∈ Aut(Q). Moreover Λ(hL) = hΛ.

(b) For every h ∈ Aut(Q) and every lifted branch c̃: h maps the anchored sheets of c̃ bijectively onto the anchored sheets of hc̃, and P(hT″) = hP(T″).

(c) x ∈ Λ. Every anchored sheet T′ of b̃ contains some lift-curve hL, and P(T′) = hΛ.

(d) MS11♭ holds at this datum ⇔ there is an anchored sheet T′ ⊇ hL of b̃ with h^{-1}x ∈ Λ.
- In every case, x is Y-persistent on the anchored sheet h^{-1}T′ of the lift h^{-1}b̃ of the same coarse branch b.
- So a failure means precisely this: the lift of b that carries x is h^{-1}b̃, not the lift b̃ that lies in S together with β̃.

*Proof.*

(a)
- q is the quotient by Aut(Q), so q^{-1}(Q_t) = Aut(Q)·(L ∩ {t}).
- Hence ⋃_h hL is the whole analytic set {(p,t) : q(p) = Q_t}.
- Its irreducible components are the irreducible curves hL. This gives the first claim.
- The second claim follows from F_{hy}(hp) ≅ F_y(p).

(b)
- B is Aut(Q)-invariant and q∘h = q.
- So h preserves q^{-1}(H((c ∖ {Q}) × Δ_ε)) ∩ (B × Δ_ε), and it sends the connected component containing c̃ ∖ 0 to the one containing hc̃ ∖ 0. Thus hÑ_{c̃} = Ñ_{hc̃}.
- Closures, irreducible components, and the condition "⊇ c̃ × {0}" are transported by h.
- Persistence is transported by the label convention.

(c)
- By (P), Q is not in the stratum of the piece of β or of b. So all anchored sheets of β̃ and b̃ are of boundary type.
- Entry 114 gives: every transport sheet contains a lift-curve, and P = Λ(λ) for any lift-curve λ in a boundary-type sheet.
- With (a), this gives P(T) = Λ, hence x ∈ Λ, and P(T′) = hΛ.

(d)
- By (c), x ∈ P(T′) ⇔ h^{-1}x ∈ Λ. This is the stated equivalence.
- For the second claim: by (b), h^{-1}T′ is an anchored sheet of h^{-1}b̃ that contains L.
- By (c), P(h^{-1}T′) = Λ ∋ x. ∎

**Corollary 2.2 (t = 0 trace of non-constancy).** Under the hypotheses of Lemma 2.1, at t = 0 the labels in hΛ (with hL ⊂ T′ as above, so hΛ ≠ ∅) are intact along b̃ with constant value Y_0.

So whenever Y is non-constant, *some* Y_0-copy stays intact and constant along b̃ at t = 0. A failure of MS11♭ forces x ∉ hΛ, so this copy is a label y = hx″ ≠ x with x″ ∈ Λ, i.e. a twin of a Y_t-label.

*Proof.* Persistence at (p, 0), p ∈ b̃, means that y is intact and F_y(p) ≅ Y_0. ∎

### 2.2 The first move: Teichmüller-disc degeneration at t = 0

**Set-up.**
- For p ∈ S ∖ {N = 0} (lifted points of V_0) and a unit vector v ∈ T_pS, let q_{p,v} be the unit-area norming differential of the Teichmüller disc of V_0 through (p, v). This exists because V_0 is totally geodesic.
- For a label y, let A_y(p, v) be the q_{p,v}-area of the thick region of the plumbing chart belonging to y.

**Lemma 2.3 (area on the two sides; consequence of Lemma PA, entry 45, read in the chart).** Let c̃ ∈ {β̃, b̃}. If a label y is intact along c̃ with π_y constant on the piece of c, then A_y(p, v) → 0 as p → a generic point of c̃, uniformly in v. Some label intact along c̃ has positive limiting area.

So, by the hypothesis on x and by Corollary 2.2:
- on the β̃ side, x has zero limiting area;
- under Y non-constant, on the b̃ side, the labels of hΛ have zero limiting area.

S ∖ {N = 0} is connected, since it is an irreducible germ minus a proper analytic subset. So the normalised flat structures can be followed continuously from the β̃ side to the b̃ side.

**Why this move cannot close MS11♭ (proved no-go).**

**Lemma 2.4 (NG).** Let (Q, β̃, b̃, x) be any t = 0 datum satisfying all t = 0 conditions of MS11♭ (closure(V_0), Q non-product, (P), (S)), with x intact and ≡ Y_0 along β̃, but with x not intact and constant along b̃. Then the trivial family V_t ≡ V_0 (H = id) satisfies:
- (R1), (R2), (i), (ii);
- (Rig), with 𝒦 the finite set of pieces of V_0;
- the persistence hypothesis on β̃;
and it violates the conclusion of MS11♭. Only "Y non-constant" fails.

*Proof.*
- For the trivial family, Ñ_{c̃} = (c̃ ∖ 0) × Δ_ε. Distinct lifted branches meet only at 0, and c̃ ∖ 0 is a punctured disc, hence connected.
- So the unique anchored sheet of c̃ is c̃ × Δ_ε. Then x is Y-persistent on it iff x is intact along c̃ with F_x ≡ Y_0.
- (Rig) holds because closure(V_0) meets each of the finitely many strata in finitely many components.
- By assumption, the persistence hypothesis holds on β̃ and the conclusion fails on b̃. ∎

Such t = 0 data exist at the terminal transition of any walk chain whose endpoint lies in a non-product stratum:
- Lemma S̃′ (entry 98) gives the common component.
- Entry 99 gives (P).
- At a MERGE endpoint, x is not intact along the terminal lift. At a puncture-MOV endpoint, F_x is non-constant along it.

**Consequences.**
1. Any proof of MS11♭ must use "Y non-constant" essentially, even for the t = 0 part of its conclusion ("x intact along b̃ with F_x ≡ Y_0").
2. Lemma 2.3, and any argument that uses only the totally geodesic geometry of closure(V_0) at Q, involves only data that the trivial family shares. Such an argument therefore cannot prove MS11♭: it would prove the t = 0 statement that Lemma 2.4 refutes at terminal transitions.
3. The Teichmüller-disc move can contribute only as a supplement to a t ≠ 0 argument. Specifically, it would have to show the following:

   (★) at t = 0, a label of zero limiting area on the β̃ side that is Y_0-twinned (via h ∈ G_X) with a zero-area label on the b̃ side must be that same label.

   That (★) is false in general is again shown by terminal MERGE data: there x has zero area on the β̃ side, merges on the b̃ side, and other Y_0-copies may stay. So the move gives no new constraint on its own.

### 2.3 What would close the gap

By Lemma 2.1(d), MS11♭ at a datum is equivalent to **(Lift)**: the lift-curve hL contained in an anchored sheet of b̃ can be chosen with h^{-1}x ∈ Λ(L).

By entries 114 and 129, (Lift) is automatic if Q_t has a single lift-curve in X (that is, G_X ⊆ Stab(L)). The residual case is the rigid-twin configuration (NRT), entry 137:
- at Q_t, x ≅ Y_t;
- a twin x′ = h^{-1}-related to x is frozen at Y_0;
- the two are exchanged at t = 0 by an automorphism of Q that is lost for t ≠ 0.

My attempt gives nothing beyond Corollary 2.2 against (NRT). Under (NRT) the twin y on b̃ in Corollary 2.2 is exactly the image of the Y_t-label, and x on b̃ is either merging, moving, or frozen. In all three cases every t = 0 condition is met: Lemma 2.4 for the first two, and for the third the t = 0 picture is identical to the non-failing one.

---

## 3. Summary lists

**Proved here** (modulo the cited ledger entries):
- §1: the step-by-step derivation that MS11♭ + (Rig) + entries 2/19, 24, 45, 85–87, 98, 99, 112–114 imply the claim, including the trivial case dim M_{g_i,n_i} = 0.
- Lemma 2.1: the lift-curve reformulation of MS11♭ as (Lift). A failure means that the lift of the coarse branch b carrying x is h^{-1}b̃ ≠ b̃.
- Corollary 2.2: under Y non-constant, some Y_0-copy stays intact and constant along b̃ at t = 0.
- Lemma 2.3: zero-area labels on both sides (a reading of Lemma PA).
- Lemma 2.4 (NG): the trivial family satisfies every hypothesis of MS11♭ except "Y non-constant" and violates its conclusion at any terminal-transition datum in a non-product stratum. So t = 0-only arguments, including Teichmüller-disc degeneration, cannot prove MS11♭, not even its t = 0 part.

**Not proved:**
- MS11♭ itself.
- The rigid-twin exclusion (NRT).
- (★), which is false as a t = 0 statement.

**Open:**
- MS11♭ (entry 124), equivalently (NRT) (entry 137), equivalently (under (Rig)) the problem's claim.
- (Rig) under the coarse reading (R2) (entry 82).
- Whether walk-chain endpoints in non-product strata actually occur for some totally geodesic V_0. This is only relevant to how sharp Lemma 2.4 is.

=== END OF ANSWER round13_q7 ===
