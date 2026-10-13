# round10_q7 — attempt on MS10 via counting (conservation of number)

**Final status: NOT PROVED; partial.** The counting route is shown to be a no-go (§2). The literal MS10 is shown to be too strong, by a local model (§3). A Krull-linkage theorem proves the corrected MS10′ under Q-factoriality (§4). Full summary in §5.

**Original plan (stage 2).** Read the whole brief. Plan:
1. §1: an incidence lemma (proved). Persistent label sets propagate along chains "transport family ⊃ lift-curve ⊂ transport family". This is the part of the counting idea that really works.
2. §2: the counting route itself. I show that every count in the suggested list is Γ-equivariant and is conserved, with multiplicity, in a failure configuration. So counting alone cannot contradict a failure of MS10 (a precise "no-go" statement, proved).
3. §3: a definitional problem with MS10 as literally worded (Ñ_b̃ is a *connected* component). I give an explicit local analytic model in which the literal conclusion fails, while the hypotheses that can be checked locally hold. In the same model the corrected version (irreducible component inside 𝒳) holds. This also shows that the claim "Ñ is irreducible" in R7-3 Lemma 2, step 2, is false in general.
4. §4: an attempt at an explicit local model of a genuine (corrected) failure, if time permits.
5. Summary: proved / not proved / open.

Notation and readings are those of the task file: (R1), (R2) with H_0 = id, Def(Q), q, s_e, labels, F_y, L_y, (K1)–(K4), transport families, lift-curves λ ⊂ 𝒥_Q, the 3-fold 𝒳 = closure(𝒞°), and Γ = Stab_{Aut(Q)}(𝒞°).

---

## 1. Incidence propagation (proved)

**Setting.** Q ∈ B_0, with chart Def(Q) ⊃ B (a small Aut(Q)-invariant ball) and ε small.
- 𝒥 = 𝒥_Q := {(q,t) ∈ B × Δ_ε : q(q) = Q_t}, where Q_t := H_t(Q). Its irreducible components are the **lift-curves** λ. Each is finite over Δ_ε and surjects onto it (round9_q2 §1).
- A **transport sheet** is an irreducible component T of closure(aÑ_c), where c is a branch of B_0 at Q (boundary or interior) and a ∈ Aut(Q). It is a 2-dimensional irreducible analytic germ at (0,0) (R7-4 Lemma 2(c)).
- The pinching pattern is constant on aÑ_c (R7-4 Lemma 2(a)). Hence T has a well-defined generic pattern S(T). Call T of **boundary type** if S(T) ≠ E(G_Q), i.e. Q ∉ stratum(c), and of **interior type** otherwise.
- For a lift-curve λ put Λ(λ) := {y : [F_y(q)] = [Y_t] for all (q,t) ∈ λ}. This makes sense because λ lies in the stratum locus {all s_e = 0} ⊂ L_y.
- For a transport sheet T put P(T) := {y : y is intact for S(T) and [F_y(p)] = [Y_{t(p)}] for all p ∈ T}. If y is intact for S(T), then T ⊂ L_y, because L_y is closed and T ∩ aÑ_c is dense in T.

**Lemma I0 (every transport sheet contains a lift-curve).** Let T be a transport sheet. Then T ∩ 𝒥 contains a lift-curve λ.

*Proof.*
- closure(aÑ_c) ∖ aÑ_c ⊂ 𝒥 ∪ {|t| = ε} inside B × Δ_ε. Indeed, its points lie over closure(N_c) ∖ N_c with N_c = H((c ∖ Q) × Δ_ε), and near (Q,0) that set is H({Q} × Δ_ε).
- t is non-constant on T: T ∩ {t = 0} ⊂ closure(c̃ ∖ 0) up to Aut(Q), which is a curve, and T is 2-dimensional. So for every small t ≠ 0, T_t := T ∩ {t} is a non-empty curve (Krull and openness of t|_T).
- Each component of T_t ∖ 𝒥 is a union of lifted branches of H_t(c). By the cone structure of B_t at Q_t, each such branch has a lift of Q_t in its closure.
- So T ∩ 𝒥 is an analytic subset of the curve 𝒥 that meets every fibre t ≠ 0. It therefore contains a component of 𝒥. ∎

**Lemma I1 (one inclusion, no hypotheses).** If λ ⊂ T, then P(T) ⊆ Λ(λ).

*Proof.* Let y ∈ P(T). Then T ⊂ L_y, and the set {p ∈ T : [F_y(p)] = [Y_{t(p)}]} is closed, because F_y is continuous on L_y and t ↦ [Y_t] is continuous (PR-A). It is all of T by definition, so it contains λ. ∎

**Lemma I2 (the converse at boundary sheets).** Assume Y is non-constant and (Rig) holds, so that R8-3 Theorem N applies at generic t. Let T be a transport sheet of boundary type with λ ⊂ T. Then Λ(λ) ⊆ P(T). Hence P(T) = Λ(λ) for every lift-curve λ ⊂ T. In particular, all lift-curves contained in one boundary-type sheet have the same Λ.

*Proof.* Let y ∈ Λ(λ), and let t ∉ Z be generic and small, with Z the countable exceptional set of Theorem N. Put q := λ(t), a lift of Q_t, so [F_y(q)] = [Y_t].
- T_t is a curve through q (Lemma I0, proof). Its germ at q minus q lies in aÑ_c ∩ {t}, so it consists of lifted branches c̃_t of H_t(c) through q.
- Q_t ∉ stratum(H_t(c)), because H_t preserves strata and T is of boundary type. By Theorem N, y is intact along c̃_t and we are in case STAY: F_y ≡ Y_t along c̃_t.
- y is intact along c̃_t, and the pattern is constant on the dense subset T ∩ aÑ_c. So y is intact for S(T), and T ⊂ L_y.
- The analytic set A := {p ∈ T : [F_y(p)] = [Y_{t(p)}]} contains a curve in T_t for uncountably many t. A proper analytic subset of the irreducible 2-dimensional T has at most countably many 1-dimensional components. So A = T, i.e. y ∈ P(T). ∎

**Corollary I3 (propagation along the incidence graph).** Let 𝔊 be the bipartite graph whose vertices are the transport sheets and the lift-curves at Q, with T — λ iff λ ⊂ T. Assume Y is non-constant and (Rig). Let
 T_0 — λ_1 — T_1 — λ_2 — ⋯ — λ_k — T_k
be a path in 𝔊 with T_1, …, T_k of boundary type. Then P(T_0) ⊆ P(T_k).

*Proof.* P(T_0) ⊆ Λ(λ_1) by Lemma I1. Then Λ(λ_j) = P(T_j) = Λ(λ_{j+1}) by Lemma I2, and Λ(λ_k) = P(T_k). ∎

**Corollary I4 (MS10 under linkage).** In the data of MS10, let T_β ⊂ closure(Ñ_β̃) be a transport sheet with x ∈ P(T_β) (one exists whenever x is Y-persistent along β̃). Let b be a boundary branch, and suppose **every** transport sheet contained in closure(Ñ_b̃) is joined to T_β in 𝔊 by a path through boundary-type sheets. Then x is Y-persistent along b̃: x is intact on Ñ_b̃ and F_x ≅ Y_t there. ∎

Remarks.
- The joining hypothesis of MS10 is not used in I3/I4. It is replaced by linkage in 𝔊.
- Corollary I4 contains round9_q2 Corollary 3 (a single lift-curve in closure(𝒞°)) and Proposition 4(ii). The new point is that linkage may pass through several lift-curves, through transport sheets that are not in the track's 3-fold, and through other branches at Q.
- Consequently, **a failure of MS10 at a boundary branch b forces some sheet T_b ⊂ closure(Ñ_b̃) to lie in a different connected component of 𝔊_∂ (𝔊 restricted to the boundary-type sheets and the lift-curves) from every sheet carrying x.** Since T_b contains some λ′ (Lemma I0), and the lift-curves in 𝒳 form one Γ-orbit (round9_q6 Lemma 1), this means: λ′ = γλ for some γ ∈ Γ, Λ(λ′) = γΛ(λ) by (K3), and x ∉ γΛ(λ).

---

## 2. The counting route: a no-go statement (proved)

The task suggests building finite analytic families over Δ_ε and comparing degrees at t = 0 with generic t. Here is what all such counts give.

**Lemma C1 (dichotomy along a lift-curve).** For a lift-curve λ and a label y, A_y(λ) := {(q,t) ∈ λ : [F_y(q)] = [Y_t]} is either all of λ (iff y ∈ Λ(λ)) or a finite set.

*Proof.* A_y(λ) is analytic in the irreducible curve λ, since F_y is holomorphic into the coarse space on the stratum locus and [Y] is holomorphic. ∎

**Lemma C2 (equivariance).** For γ ∈ Aut(Q): γλ is a lift-curve and Λ(γλ) = γΛ(λ). For transport sheets, P(γT) = γP(T).

*Proof.* (K3): F_y(γq) ≅ F_{γ^{-1}y}(q). The pattern of γT is γS(T). ∎

**Proposition C3 (all suggested counts are conserved, also in a failure configuration).** Let λ_1, …, λ_k be the lift-curves in 𝒳 (one Γ-orbit), d_j := deg(λ_j → Δ_ε), and r := |Λ(λ_1)| = ⋯ = |Λ(λ_k)| (Lemma C2). Consider the analytic set
 𝒜 := {((q,t), y) : (q,t) ∈ 𝒥 ∩ 𝒳, [F_y(q)] = [Y_t]} ⊂ (𝒥 ∩ 𝒳) × V(G_Q).
1. Its 1-dimensional part 𝒜¹ is ⋃_j λ_j × Λ(λ_j). It is finite over Δ_ε of degree r·Σ_j d_j. By conservation of number for finite maps of curves, its fibre over t = 0, counted with multiplicity, has the same degree. The label y occurs there with multiplicity Σ_{j : y ∈ Λ(λ_j)} d_j, and the set of labels that occur is ΓΛ(λ_1).
2. Its 0-dimensional part sits over t = 0 (and over a finite set of other times). It consists of the Y_0-copies at Q that lie in no Λ(λ_j). It is not flat over Δ, so conservation of number says nothing about it.
3. The same holds for the counts of pairs (lift, persistent label), (boundary branch of 𝒳_t through a lift, persistent label), and for the multiplicity of {F_x ≅ Y_t} ∩ 𝒳 along λ_j. Each is a Γ-invariant function of the configuration. Its value at generic t is r times a Γ-invariant number (the number of lifts, or of branches), and the t = 0 limit is the same number counted with multiplicities.

*Proof.* (1) and (2) follow from Lemma C1 applied to each λ_j and each label. For (3), every count listed is a sum over the Γ-orbit of lift-curves of a quantity that Lemma C2 makes constant along the orbit. ∎

**Consequence (the no-go).** In a failure of MS10 at a boundary branch b (§1, last remark), x ∈ Λ(λ) and x ∉ Λ(λ′) = γΛ(λ). The "(r+1)-st copy" of the Count lemma (round9_q3 §5) is the label x seen from λ′. In the set 𝒜 above it is **not** an extra point. It is carried by the 1-dimensional component λ × {x}, through the other lift-curve λ. So:
- the count r at a single lift and the count |ΓΛ(λ)| ≥ r + 1 at t = 0 are different quantities, and neither is violated;
- a conservation-of-number contradiction would need a Y_0-copy at Q lying in no Λ(λ_j). Its existence is neither forced nor forbidden by a failure of MS10, and its existence alone contradicts nothing (part 2).

So **every count built from the families of move 1 is consistent with a failure of MS10.**

**Ledger correction.** The (r+1)-st copy described in the task's opening paragraph ("A failure of MS10 at Q forces Q to carry at least r + 1 components isomorphic to Y_0 at t = 0") is not a drop in any conserved count. It is the union over the Γ-orbit of the persistent sets. What distinguishes failure from success is *which* labels are persistent at which lift-curve (Λ(λ) is not Γ-invariant), not *how many* there are. Counts are invariant under the symmetry γ that exchanges the two situations. The counting route cannot decide MS10 without further input, and that input must break the Γ-symmetry. Total geodesy of V_0 is Γ-symmetric at t = 0 too, so it has to enter through something non-numerical, for example the position of the track.

---

## 3. The literal wording of MS10 is too strong: a local model, and a flaw in R7-3 Lemma 2 (proved, as a local statement)

MS10 defines Ñ_b̃ as the **connected** component of q^{-1}(H((b ∖ Q) × Δ_ε)) ∩ (B × Δ_ε) that contains b̃ ∖ 0. It defines "x Y-persistent along b̃" as a condition at **every** point of Ñ_b̃. R7-3 Lemma 2, step 2, asserts that Ñ is a topological 4-manifold ("being a cover of a punctured disc times a disc") and hence irreducible. The following explicit germ shows that this is false. In the germ, the literal conclusion of MS10 fails while every hypothesis of MS10 that can be checked in the chart holds.

### 3.1 The model
- **Graph.** G_Q has vertices x, x′, w, z and edges e_1 = {x,w}, e_2 = {x′,w}, e_3 = {w,z}. The components x, x′ have the type (g_i,n_i) of Y and are isomorphic at Q. There is σ ∈ Aut(Q) of order 2 with σ(x) = x′, σ(e_1) = e_2, σ(e_3) = e_3. The stratum Δ_{G_Q} is not of product type, since σ exchanges two vertices of positive-dimensional type.
- **Chart coordinates.** The relevant chart coordinates are (s_1, s_2, s_3, a, b). Here s_j smooths e_j, a is a local coordinate of [F_x] near [Y_0] (so [F_x] = [Y_0] ⇔ a = 0), and b = a∘σ is the same for x′. For simplicity take dim M_{g_i,n_i} = 1 and put [Y_t] ↔ a = t. The remaining chart coordinates are set to 0. σ acts by (s_1, s_2, s_3, a, b) ↦ (s_2, s_1, s_3, b, a).
- **The 3-fold.** In (s,a,b,t)-space put
 𝒳′ := {s_1 = s_2 s_3, a = t, b = 0}, a smooth 3-fold (a graph over (s_2, s_3, t)),
 and let the preimage of closure(𝒱) near (0,0) be 𝒳′ ∪ σ𝒳′, with σ𝒳′ = {s_2 = s_1 s_3, b = t, a = 0}.

**Elementary checks.**
1. 𝒳′ ∩ σ𝒳′ = {s_1 = s_2 = 0, a = b = t = 0} = D̃ × {0}, where D̃ := {(0,0,r,0,0)}. Indeed a = t and a = 0 give t = 0. Then s_1 = s_2 s_3 and s_2 = s_1 s_3 give s_1(1 − s_3²) = 0, so s_1 = s_2 = 0 near 0. The set D̃ is fixed pointwise by σ, and it lies in the boundary {s_1 s_2 s_3 = 0}.
2. So q|_{𝒳′} is injective (q(p) = q(p′) means p′ ∈ {p, σp}, and σp ∈ 𝒳′ forces σp = p). The coarse family closure(𝒱) near (Q,0) is q(𝒳′), homeomorphic to C³ by the graph coordinates (s_2, s_3, t).
3. Interior points of 𝒳′ (s_1 s_2 s_3 ≠ 0) have trivial stabiliser. So V_t is smooth there, and so is V_0.
4. **H.** Define H_t(q(s_2, s_3, 0)) := q(s_2, s_3, t). The zero pattern of (s_1, s_2, s_3) = (s_2 s_3, s_2, s_3) depends only on (s_2, s_3). Hence H is a stratum-preserving homeomorphism, smooth on the interior. This gives (R1), (R2), (i) and (ii) locally, and H_t(Q) = Q_t := q(0,0,0,t,0).
5. **Boundary at t ≠ 0.** 𝒳′_t ∩ {s_1 s_2 s_3 = 0} = {s_2 s_3 = 0} has two branches through λ(t) := (0,0,0,t,0):
   - T_F := {s_1 = s_3 = 0, s_2 = r, a = t, b = 0}, with pattern {e_1, e_3};
   - T_D := {s_1 = s_2 = 0, s_3 = r, a = t, b = 0}, with pattern {e_1, e_2}.
   Their σ-images pass through σλ(t) = (0,0,0,0,t). At λ(t) the unique Y_t-copy is x (a = t, b = 0 ≠ t), so r = 1, and x is intact and ≡ Y_t along both branches. Krull at the lift (round9_q1 Lemma 1(c)) holds: the patterns cover e_1, e_2, e_3.
6. **The pieces.**
   - Pattern {e_1,e_3} contracts e_2. The stratum has vertices x, w ∪ x′, z, and x is constant ≡ Y_t. This plays the role of ∂V_t ⊂ Δ_Γ, a stratum that can be of product type.
   - Pattern {e_1,e_2} contracts e_3. Its vertices are x, x′, w ∪ z. This is a non-product piece D with constant vertices x (≡ Y_t) and x′ (≡ Y_0, "frozen") and moving vertex w ∪ z. Both constant vertices are ≅ Y_0 at t = 0. At t = 0, D̃ is fixed pointwise by σ: every point of D has the extra automorphism σ at t = 0, and it is lost for t ≠ 0 (allowed under (R2)).

### 3.2 Literal MS10 fails in the model
- Take β̃ := F̃ = T_F ∩ {t = 0} = {(0, r, 0, 0, 0)} and b̃ := D̃. Both lie in the smooth connected surface 𝒳′_0, whose interior {s_2 s_3 ≠ 0} is connected. So they are joined inside the chart by paths in q^{-1}(V_0) ∩ B.
- **Ñ_β̃ = T_F.** q^{-1}(N_f) = T_F ∪ σT_F, and these are disjoint (s_2 = r ≠ 0 on T_F, s_2 = 0 on σT_F). So x is Y-persistent along β̃ (s_1 = 0 and a = t on T_F).
- **Ñ_b̃ = T_D ∪ σT_D.** q^{-1}(N_d) = T_D ∪ σT_D, and T_D ∩ σT_D = D̃ × {0} ≠ ∅. So the connected component containing D̃ ∖ 0 is the union. It is reducible, and it is not a topological manifold along D̃ × {0}: two real 4-planes meet in a real 2-plane. Its quotient by σ, which is N_d, is a manifold.
- On σT_D, x is intact but F_x ↔ a = 0 ≠ t. So **x is not Y-persistent along b̃ in the literal sense**. The same holds for x′. MS10's conclusion fails, while Q is non-product, β̃ and b̃ are joined, x is persistent along β̃, and Y (a = t) is non-constant.
- **The corrected reading holds in the model.** The track's component is 𝒞° = 𝒳′ ∖ {s_1 s_2 s_3 = 0} (𝒳′° and σ𝒳′° are disjoint), so 𝒳 = 𝒳′, Γ = {1}, and the component of Ñ_b̃ in 𝒳 is T_D, along which x ≡ Y_t.

This is a germ, not a global V_0. Total geodesy and (Rig) for global pieces cannot be checked in it. So it is **not** a counterexample to the problem. It shows two things:
- the literal MS10 cannot be proved by arguments that see only the chart;
- R7-3 Lemma 2 step 2 ("Ñ is irreducible") is false whenever the pointwise stabiliser of b̃ at t = 0 is larger than the generic stabiliser along the family, and moves one irreducible component of Ñ to another.
  - In R8-8 §0, the identity (∗) ("F_x ≡ φ_c(t) on closure(Ñ_t)") is stated only for D of product type. There Lemma PT makes every such stabiliser element fix x, so F_x agrees on the components and (∗) survives.
  - In non-product strata, which is where MS10 lives, the analogue of (∗) fails: in the model it fails on σT_D.

### 3.3 The corrected statement
**MS10′.** Same setting and data as MS10. Let 𝒞° be the connected component of q^{-1}(𝒱) ∩ (B × Δ_ε) that contains the interior paths γ_n (after passing to a subsequence; finitely many components meet a neighbourhood of 0), let 𝒳 := closure(𝒞°), and replace "Y-persistent along c̃" by:
- *(Pers_𝒳)* x is intact, and F_x ≅ Y_t, on every irreducible component of closure(Ñ_c̃) that is contained in 𝒳.

Conclusion: if (Pers_𝒳) holds for β̃, it holds for b̃.

Comments.
- round9_q2 Lemma 2 and round9_q6 Lemma 2 show that some irreducible component of each of closure(Ñ_β̃) and closure(Ñ_b̃) lies in 𝒳. With (Rep3)-generic base points, Stab(z̃) is the pointwise stabiliser, which may permute the components; the q6 proof only gives "some component".
- Every later use of (∗), R7-3 Lemma 2 and R8-8 §0 should be read for irreducible components. In the chain this matters exactly at branches that are σ-fixed pointwise at t = 0. I have not re-audited every such use; this is recorded as an open bookkeeping item.

---

## 4. Where a conservation law does work: Krull linkage in the 3-fold (proved)

Section 2 says that numerical counts are blind to *which* label persists. One intersection-theoretic statement is not blind: two divisors on a 3-fold that is Q-factorial at a point meet in a curve through that point. Applied to two transport sheets inside the track's 3-fold, this curve is forced to be a common lift-curve, and Corollary I3 then transports the label. This is the "conservation of number" that the task asks for, in its correct form: the intersection T_β · T_b is non-empty at every time t if it is non-empty at t = 0 and one of the sheets is Cartier.

**Theorem Q.** Assume Y is non-constant and (Rig) holds. Let Q ∈ B_0 (any stratum). Let T_β and T_b be transport sheets at Q, both of boundary type, contained in a common irreducible component X of the germ (𝒳,(0,0)), with x ∈ P(T_β). Assume:
- (QC) there is a holomorphic h on a neighbourhood of (0,0) in X with Z(h) ∩ X = T_b (set-theoretically) near (0,0). This holds, for instance, if X is smooth at (0,0), or normal and Q-factorial there;
- (Sep) T_β ∩ T_b ∩ {t = 0} = {(0,0)} near (0,0). This holds automatically if β and b are distinct coarse branches.

Then one of the following holds.
- (a) T_β and T_b contain a common lift-curve λ. Hence x ∈ P(T_b): x is intact and F_x ≅ Y_t on T_b (MS10′'s conclusion for this sheet).
- (b) *Same-branch crossing.* β = b as coarse branches, and there are g ∈ Aut(Q) with T_b = gT_β and an irreducible curve germ C ⊂ T_β, finite over Δ_ε and not contained in 𝒥, fixed pointwise by g. Moreover, for all t outside a countable set, the label g^{-1}x is an IMOV copy of Y_t at the point q(C_t) ∈ H_t(β ∖ Q). That is, q(C_t) is an interior point of its piece, g^{-1}x has value ≅ Y_t there and moves along the branch.

*Proof.*
1. **Krull.** T_β ≠ T_b by (Sep), and T_β ⊄ T_b since both are irreducible of dimension 2. So h|_{T_β} ≢ 0 and h(0,0) = 0. By Krull, T_β ∩ Z(h) = T_β ∩ T_b has pure dimension 1 at (0,0). Let C be an irreducible component of its germ at (0,0).
2. **C is finite over Δ.** C ∩ {t = 0} ⊂ T_β ∩ T_b ∩ {t = 0} = {(0,0)} by (Sep). So t|_C is non-constant and finite, and C_t ≠ ∅ for every small t.
3. **Case C ⊂ 𝒥.** Then C is a lift-curve λ with λ ⊂ T_β ∩ T_b. By Lemma I1, x ∈ P(T_β) ⊆ Λ(λ). By Lemma I2 (T_b is of boundary type), Λ(λ) = P(T_b). This is (a).
4. **Case C ⊄ 𝒥.** C ∩ 𝒥 is a proper analytic subset of the irreducible germ C, hence {(0,0)}. Take p ∈ C_t with t ≠ 0 small.
   - p ∈ T_β ∖ 𝒥 ⊂ ⋃_a aÑ_β, so q(p) ∈ H_t(β ∖ Q). Likewise q(p) ∈ H_t(b ∖ Q).
   - H_t is injective and H_t(β ∖ Q) ∩ H_t(b ∖ Q) = ∅ for distinct coarse branches. So β = b.
   - Near p, the slices T_{β,t} and T_{b,t} are lifted local branches through p of the coarse curve H_t(β) at q(p). Stab(p) permutes these lifts transitively. So there is g_t ∈ Stab(p) mapping the germ of T_{β,t} at p onto the germ of T_{b,t} at p.
   - Aut(Q) is finite. So one g occurs for infinitely many points p = p_n ∈ C, accumulating at (0,0) and with distinct times.
   - Then gT_β ∩ T_b contains infinitely many distinct 1-dimensional germs. So it is 2-dimensional, and gT_β = T_b by irreducibility.
   - Fix(g) ∩ C is analytic in C and contains the p_n, which accumulate at (0,0). So C ⊂ Fix(g).
5. **The label.** For p ∈ C_t we have p ∈ T_β ⊂ L_x and F_x(p) ≅ Y_t. Since gp = p, (K3) gives that g^{-1}x is intact at p and F_{g^{-1}x}(p) ≅ F_x(gp) = F_x(p) ≅ Y_t.
   - Apply R8-3 Theorem N at the point q(p) (generic t) to the label g^{-1}x and the branch T_{β,t} through p. Either STAY or IMOV.
   - If STAY holds for uncountably many t, then the analytic set {F_{g^{-1}x} ≅ Y_t} ⊂ T_β contains uncountably many slice curves. So g^{-1}x ∈ P(T_β) and x ∈ gP(T_β) = P(T_b) (Lemma C2): conclusion (a) for T_b.
   - Otherwise IMOV holds for all t outside a countable set, which is (b). q(p) is an interior point of its piece because it lies on H_t(β ∖ Q). ∎

**Corollary Q1 (MS10′ under Q-factoriality).** In the setting of MS10′, with b a boundary branch and β ≠ b as coarse branches: suppose every irreducible component of closure(Ñ_b̃) lying in 𝒳 lies on a common irreducible component X of 𝒳 with some sheet T_β ⊂ closure(Ñ_β̃) satisfying x ∈ P(T_β), and suppose X is Q-factorial at (0,0) (e.g. smooth). Then MS10′'s conclusion holds at (β̃, b̃). ∎

**Corollary Q2 (shape of a failure of MS10′).** Let b be a boundary branch with β ≠ b, and suppose MS10′ fails at (β̃, b̃) with Y non-constant. Then for some sheet T_b ⊂ closure(Ñ_b̃) ∩ 𝒳 with x ∉ P(T_b), and every sheet T_β ⊂ closure(Ñ_β̃) ∩ 𝒳 with x ∈ P(T_β), one of the following holds:
- **(F1)** T_β and T_b lie on a common irreducible component X of 𝒳, and T_b is not set-theoretically principal on X at (0,0). In particular X is not Q-factorial at (0,0): the track's 3-fold has a non-Q-factorial singularity at (0,0), of 3-fold-node type or worse;
- **(F2)** T_β and T_b lie on no common irreducible component of 𝒳.

*Proof.* Otherwise Theorem Q applies, and (b) is excluded because β ≠ b. ∎

**Remarks.**
- In (F2), 𝒞° is connected, so the components of 𝒳 are linked through interior points. At such a point p, Stab(p) permutes the local components transitively, because the coarse germ of 𝒱 at q(p) is irreducible. So the joining happens at interior points fixed by elements of Γ that exchange components of 𝒳. This matches the known necessary condition (an α ∈ Γ moving x with an interior fixed locus).
- The local model of (F1) is the 3-fold node 𝒳 = {xy = zw}. The two planes {x = z = 0} and {y = w = 0} (same ruling) meet only at 0. For t := x + y, the slices 𝒳_t (t ≠ 0) are smooth quadrics in which the two lines are disjoint, while at t = 0 they meet at the vertex of the A_1 cone 𝒳_0. This is exactly the "star splitting" of R8-8 §6.
- An involution that exchanges the two planes and preserves the node is of the form M ↦ AMB on 2×2 matrices M = [[x,z],[w,y]] of rank ≤ 1, since it preserves the ruling. Its fixed locus in 𝒳 is a finite union of lines. So, in a slice 𝒳_t, it has isolated fixed points, and the coarse quotient V_t would have A_1 points there unless those points lie in the boundary. Together with round9_q5 Corollary 1 (a twin jump needs a ≥ 2-dimensional relevant fixed component), this suggests that (F1) may be incompatible with smoothness of V_t. I have **not** proved this: a non-Q-factorial X need not be a node, and Γ need not preserve X.
- Theorem Q does not use total geodesy. Total geodesy can only enter through (QC), i.e. through the singularity type of the track's 3-fold at (0,0), or through (F2).

**A side correction (R8-8 §6, item 1, "stars are disjoint").** That sketch argues that two lifted arcs starting at different lifts of J_t cannot meet, "because away from J_t the stabiliser is locally constant along the arc". This fails at isolated points of an arc with a larger stabiliser.

*Example.* Def = C² ∋ (u,v), σ(u,v) = (−u,v), and the line L = {u = v − c}.
- q(L) = {(w,v) = ((v − c)², v)} is a smooth arc in C²/σ.
- Its two lifts L and σL start at the different points (−c,0) and (c,0), and they meet at the σ-fixed point (0,c).

So two stars can touch at symmetric points of an arc. This is precisely alternative (b) of Theorem Q. Nothing proved above relies on disjointness of stars.

**What (F2) reduces to, in the simplest combinatorics (analysis; sketched, not proved in general).** Let X ∋ T_β be a component of 𝒳 all of whose boundary sheets keep the edges E_x at x pinched. Let σ ∈ Γ with σx ≠ x, and let Σ ⊂ X ∩ Fix(σ) be a relevant 2-dimensional fixed component.
- For an edge f, Krull gives a curve Σ ∩ Z(s_f) through (0,0). At its points with t ≠ 0, the edges E_x ∪ σE_x are pinched.
- If f together with E_x ∪ σE_x exhausts E(G_Q), the curve lies in 𝒥. Then σ fixes a lift-curve of X, which gives "pointwise Lock" (round9_q5 (Ψ-J)) and kills the failure.
- Otherwise the curve lies in T ∩ σT for a boundary sheet T ⊂ X: a same-branch crossing as in Theorem Q(b). Or it lies in {t = 0}: (B-pure), round9_q5 (O2″).

So, in that case, a failure of MS10′ always ends in one of the two configurations the run already lists as open: same-branch IMOV crossings near Q at generic t, or (B-pure). This also assumes Q is isolated in B_0 ∩ Δ_{G_Q}; otherwise interior pieces through Q add a third possibility.

---

## 5. Summary

**Outcome: MS10 is NOT proved, and no global counterexample is given.**
- The assigned counting route provably cannot settle MS10 by itself (§2).
- MS10 as literally worded is too strong. A local model satisfies all of its chart-checkable hypotheses and violates its conclusion (§3). The corrected statement MS10′ is proposed.
- MS10′ is proved under a Q-factoriality hypothesis on the track's 3-fold (§4). Without it, a failure is reduced to two explicit shapes.

**Proved** (from (R1), (R2), (Rig), R8-3 Theorem N, and the cited standard facts of Krull's theorem and the identity theorem):
1. **Lemma I0–I2, Corollaries I3–I4.** Every transport sheet contains a lift-curve. P(T) ⊆ Λ(λ) for λ ⊂ T, with equality for boundary-type T when Y is non-constant. Persistent labels propagate along paths of the incidence graph 𝔊, so MS10 holds whenever the sheets of b̃ are 𝔊-linked to a sheet carrying x through boundary-type sheets. A failure of MS10 at a boundary branch means that T_b contains a lift-curve γλ (γ ∈ Γ) with x ∉ γΛ(λ).
2. **Proposition C3 and the no-go.** Every count in the task's list is conserved and Γ-equivariant, and remains consistent in a failure configuration:
   - lifts × persistent labels;
   - boundary branches through lifts × persistent labels;
   - multiplicities of {F_x ≅ Y_t} along lift-curves.
   The "(r+1)-st copy" of the Count lemma is carried by the other lift-curve of the Γ-orbit, not by an isolated point. A counting argument cannot distinguish which label persists.
3. **§3 model.** An explicit germ in which:
   - Ñ_b̃ (a connected component) is reducible and not a manifold;
   - the literal conclusion of MS10 fails;
   - the corrected statement MS10′ holds.
   Consequences:
   - R7-3 Lemma 2 step 2 ("Ñ irreducible") is false in general.
   - Every analogue of (∗) in non-product strata must be read on irreducible components.
   - In product strata (∗) survives, by Lemma PT.
4. **Theorem Q (Krull linkage).** Suppose two boundary sheets T_β ∋ x-persistence and T_b lie on a common irreducible component X of 𝒳 on which T_b is set-theoretically principal (e.g. X smooth or Q-factorial at (0,0)), and their t = 0 slices meet only at 0. Then either they share a lift-curve, so x is persistent on T_b, or there is a same-branch IMOV crossing near Q at generic t (alternative (b), possible only when β = b coarsely).
   - **Corollary Q1:** MS10′ holds when β ≠ b and the relevant component of 𝒳 is Q-factorial.
   - **Corollary Q2:** a failure with β ≠ b forces (F1) a non-Q-factorial component of 𝒳 at (0,0) containing both sheets, or (F2) the two sheets on different components of 𝒳, joined through interior fixed loci of elements of Γ.
5. Side correction: the "stars are disjoint" sketch of R8-8 §6 is false at isolated symmetric points (explicit example). Theorem Q(b) is exactly this phenomenon.

**Sketched only.**
- The reduction of (F2), in the simplest combinatorics, to the already-open same-branch crossings or (B-pure) (§4, last paragraph).
- The heuristic that (F1) of 3-fold-node type is incompatible with smoothness of V_t (the ruling-preserving involutions of a node have only 1-dimensional fixed loci).

**Open (named).**
- **(O-MS10′)** MS10′ itself.
- **(O-F1)** Can a component of the track's 3-fold 𝒳 be non-Q-factorial at (0,0), with T_b not principal on it, for smooth V_t and totally geodesic V_0? A negative answer would leave only (F2).
- **(O-F2)** (F2), equivalently round9_q5's (D2)/(B-pure) and the same-branch IMOV crossings.
- **(O-audit)** Re-audit of the uses of R7-3 Lemma 2 and (∗) at branches fixed pointwise at t = 0 by a label-moving automorphism (non-product strata).
- Entry 82 ((Rig)) is untouched.

proved: Lemmas I0–I2, Corollaries I3–I4, Proposition C3 and the counting no-go, the §3 local model with the R7-3 Lemma 2 correction, Theorem Q with Corollaries Q1–Q2, the star-disjointness correction.
not proved: MS10, and MS10′, in general.
open: O-MS10′, O-F1, O-F2, O-audit (and entry 82).

=== END OF ANSWER round10_q7 ===
