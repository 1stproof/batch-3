# round10_q3 — attempt on MS10

**Plan/status line.** MS10 is NOT proved here, and no counterexample is given. This is a PARTIAL answer. The file contains:
- §1: the logical status of MS10. A counterexample to MS10 is the same thing as a counterexample to the problem, for families satisfying (Rig). So the "counterexample" option of the task cannot be easier than disproving the problem.
- §2: an audit of the chain MS10 ⇒ MS8 ⇒ goal. I found **two places where the derivation is incomplete, both at non-product pieces**:
  - (Gap A) the walk chain's special set Σ misses the points where two lifts of a non-product piece cross. At such a point the tracked label can switch sheets in the middle of a "travel" interval.
  - (Gap B) under the coarse reading (R2), a transport family Ñ need **not** be irreducible. The claim in R7-3 Lemma 2, step 2, that it is irreducible is false in general (explicit local model below). As a result, MS10's notion of "Y-persistent along β̃", which quantifies over every point of Ñ, can fail along a non-product piece even when no twin jump occurs. So the induction claim (b) of the chain is false as worded in such configurations.
  
  I give repairs for both: enlarge Σ, and use a component-wise notion of persistence. After the repairs the chain reduces the problem to a component-wise variant MS10′ of MS10, at points of non-product strata.
- §3: an attempt on MS10/MS10′, and an explicit local model (coarse-smooth, totally-geodesic-compatible at t = 0) of the interior mechanism that a failure needs. The model shows exactly what a proof must exclude.
- §4: proved / not proved / open.

Throughout: the readings (R1), (R2) with H_0 = id, the notation of the task file, and (Rig). Facts cited from memory are marked as such.

---

## 1. The logical status of MS10

**Proposition 1.1.** Fix an admissible configuration: V_0, a family V_t satisfying the problem's hypotheses in the readings (R1), (R2), Γ, i with dim M_{g_i,n_i} > 0, and (Rig).
- (a) If the problem's conclusion Y_t ≡ Y_0 holds for this family, then MS10 holds for every choice of the data (Q, B, β̃, b̃, γ_n, x) in this family, vacuously.
- (b) Any counterexample to MS10 is a family satisfying all the problem's hypotheses, plus (Rig), with Y non-constant. That is, it is a counterexample to the problem.
- (c) Assume the chain's derivation (MS10 + (Rig) ⇒ goal) is correct, after the repairs of §2. Then, for the class of families satisfying (Rig), "MS10 holds for all configurations" is equivalent to "the problem's claim holds for all families".

*Proof.* MS10 has the hypothesis "t ↦ Y_t is non-constant". (a): that hypothesis fails, so the implication holds. (b): a counterexample satisfies all the hypotheses of MS10, which include all the problem's hypotheses, (Rig), and the non-constancy of Y. (c): one direction is (a), the other is the chain. ∎

**Consequences.**
- The task's option "give an explicit counterexample to MS10" is exactly as hard as disproving the problem for (Rig)-families. In particular it needs an actual deformable smooth totally geodesic surface, and none is known (round9_q8 §4).
- MS10 is not a reduction to a *weaker* statement. It is a *localisation*: it says where, in a hypothetical counterexample, the contradiction must be found. A proof of MS10 has to exclude a configuration that, by (a), cannot exist at all if the problem is true. So a proof must derive a contradiction from data that includes "Y non-constant". It cannot be a pure t = 0 statement about V_0.
- Remark (repeated from the task file, re-checked): MS10 without the hypothesis "Y non-constant" is false, because Prop K's endpoint violates its conclusion.

---

## 2. Audit of the chain (MS10 ⇒ MS8 ⇒ goal)

Notation. For a stable graph G, Δ_G ≅ (∏_w M_w)/Aut(G) (standard, cited from memory; Aut(G) acts by permuting factors and relabelling marked points), with quotient map ξ = ξ_G. For a piece D ⊂ Δ_G at t = 0, ξ^{-1}(D) = E_1 ∪ … ∪ E_r, irreducible curves permuted transitively by Aut(G). κ(D) is the component of ℬ_G containing H(D × Δ) (round9_q7 Lemma T). A *lifted family component* of D is an irreducible component 𝒲̃ of (ξ × id)^{-1}(κ(D)) ⊂ ∏_w M_w × Δ. Persistence of a label is a property of a lifted family component *together with the labelling of ∏_w M_w* (round9_q7 Lemma S(c)). It is not a property of the coarse κ(D). For product-type G, ξ is injective, so the two notions coincide. For non-product G they do not, and the two gaps below come from this.

### 2.1 Gap A: sheet switching in the middle of a travel interval

**The step concerned.** Chain step (b): "persistence passes along D^{m+1} to β̃_{m+1}, because persistence is a property of the whole component κ(D^{m+1}) (Lemma S(c)) and the chart vertex is c_{m+1} on both ends (K_w Step 3)."

**What is missing.** Along a travel interval of the walk chain (round9_q4 §2.3), the track stays near K_D, and its marking gives a continuous lift to ∏_w M̄_w near ξ^{-1}(D). The tracked subsurface Σ_i corresponds to one fixed factor c of ∏_w M_w along the whole interval, by continuity. But the lift can pass from one lifted curve E_k to another one, σE_k (σ ∈ Aut(G)), at a point z ∈ E_k ∩ σE_k. Then:
- before z, the track's label is c on E_k;
- after z, the label is still the factor c, but now on σE_k. In terms of E_k, the factor c of σE_k is the factor σ^{-1}c of E_k.

So the label the track follows after z is the twin σ^{-1}c, not c. The special set Σ of the walk chain consists of junctions, singular points of B_0, punctures, and points where a non-constant vertex has value [Y_0]. It does **not** contain such crossing points in general.

**Local model showing that such a point need not be in Σ (proved, local).** Take G non-product with σ ∈ Aut(G) exchanging two vertices c, c′ = σc of type (g_i, n_i), and exchanging two further vertices m, m′ of the same type. Assume near the point z the other factors are σ-fixed. Use local coordinates a on M_m and b on M_{m′} centred at z, with σ(a, b) = (b, a). Let
- E_k := {z_c = z_{c′} = Y_0, (a, b) = (s, 2s), other coordinates fixed}, so on E_k both c and c′ are constant with value Y_0, and m, m′ move;
- σE_k = {z_c = z_{c′} = Y_0, (a, b) = (2s, s), …}.

They meet at z (s = 0), which is fixed by σ. In the quotient coordinates (u, v) = (a + b, ab), E_k maps to u = 3s, v = 2s² = 2u²/9, a smooth curve. So, if Stab(z) = ⟨σ⟩, D = ξ(E_k) is **smooth** at ξ(z). ξ(z) is not a junction, not a puncture, not singular on B_0, and the non-constant vertices m, m′ have value z_m = z_{m′} there, which need not be ≅ Y_0. So ξ(z) ∉ Σ.

At the family level, let 𝒲̃ ⊃ E_k × {0} be the lifted family component on which c is persistent. Then σ𝒲̃ ⊃ σE_k × {0}, and on σ𝒲̃ the factor c carries the value function of c′ on 𝒲̃. If c′ is a "persistent twin" with [φ_{c′}] ≢ [Y] (round9_q3 §5(b)), the track's label is no longer persistent after z. Nothing in the chain's step (b) detects this.

**Repair (proved, given the walk-chain inputs).** For each piece D let R(D) be the set of P ∈ D such that, near ξ^{-1}(P), the set ξ^{-1}(D) is not a disjoint union of smooth arcs each mapped homeomorphically onto a neighbourhood of P in D.
- R(D) is finite. It consists of images of singular points of the compact curve ξ̄^{-1}(closure D) ⊂ ∏ M̄_w, and of ramification points of the finite maps from the normalisations of its components to the normalisation of closure(D). Both sets are finite.
- Replace Σ by Σ ∪ ⋃_D R(D) in round9_q4 §2.3, before choosing r. Everything there goes through unchanged: Σ is still finite.
- Then, over a neighbourhood of K_D, ξ^{-1}(D) is a disjoint union of compact arcs at positive mutual distance. By continuity, the track's lift stays near one arc of one lifted curve E for the whole travel interval, and its label is a fixed factor c. (This is a "routine marking detail" of the same kind as K_w Step 3. I use it in the same way.)
- The new transition points P ∈ R(D) are interior points of D. The track arrives along a lift β̃ and leaves along a lift b̃ of a branch of D at P, possibly of the same coarse branch, joined inside the chart (K_w Steps 3 and 5 apply verbatim). If the two lifts lie on different lifted curves, ξ is not injective, so Δ_G is non-product. Then this is exactly an MS10 configuration. MS10 explicitly allows "lifts of the same coarse branch", so it already covers these points. If both lifts lie on the same E_k at a ramification point, the label is unchanged and nothing is needed.

So Gap A is a gap in the walk-chain bookkeeping. It does not change the missing statement, but **the list of points where MS10 is invoked must include R(D) for every non-product piece D of the chain.**

### 2.2 Gap B: transport families can be reducible, and then "persistent along β̃" is the wrong notion

**The claim concerned.** R7-3 Lemma 2, step 2: "Ñ is a connected topological 4-manifold, being a cover of a punctured disc times a disc. Hence Ñ is irreducible." This is used, for instance, in round9_q2 Lemma 2 step 5 and Proposition 4 step 4. MS10's definition of "x is Y-persistent along b̃" quantifies over *every* point of Ñ_b̃.

**Claim B0.** Under the coarse reading (R2), q^{-1}(N) → N is a finite quotient map, but *not* a covering, wherever stabilisers jump. Ñ can then be reducible, and the step-2 claim is false.

**Local model (proved, local).** Let D be a piece in a non-product stratum. Suppose every curve of D has an automorphism inducing σ ∈ Aut(G), where σ exchanges two vertices c, c′ of type (g_i, n_i) that are both constant on D with value Y_0. Suppose also that the lifted curve E is fixed pointwise by σ. Near a generic point P of D, use coordinates on the stratum locus of Def(P): e along E, p on the c-factor, p′ on the c′-factor (with Y_0 ↔ 0), and w for the remaining coordinates. Here σ acts by p ↔ p′, and E = {p = p′ = 0, w = 0}. Choose the deformation
- E_t^+ := {p = t, p′ = −t, w = 0} (c has value "Y_t" ↔ t, c′ has value "φ(t)" ↔ −t), and E_t^− := σE_t^+ = {p = −t, p′ = t, w = 0}.

The coarse coordinates are (e, s, y²) with s = p + p′ and y = p − p′. The coarse transported piece is {s = 0, y² = 4t², w = 0}: a smooth, topologically trivial family of smooth curves, with H_t(e, 0, 0) = (e, 0, 4t²). Its preimage is
 q^{-1}(N) = {p = t, p′ = −t, w = 0} ∪ {p = −t, p′ = t, w = 0} =: G_+ ∪ G_−.
This is connected, since the two pieces meet along {t = 0} = E. It is reducible. It is not a manifold along E × {0}. So Ñ = G_+ ∪ G_−. The same picture occurs along the lifted branch β̃ at a puncture J of D, at generic points of β̃.

In this model:
- on G_+ the chart label x (↔ c) has F_x ≅ Y_t, and on G_− it has F_x ≅ φ(t);
- for the twin label αx (↔ c′, α ∈ Aut(J) realising σ and fixing β̃ pointwise), the roles are exchanged.

So **neither x nor αx is Y-persistent along β̃ in MS10's sense**, although every point of the transported piece carries a Y_t-copy, D ∈ 𝒩, and no twin jump has happened anywhere. The model is consistent with (R1), (R2), Lemma U (D = K_W × {c_D}, with c_D = (Y_t, φ(t)) on G_+) and (Rig), which constrains only non-constant vertices. Whether it occurs for an actual totally geodesic V_0 is not known. Covering constructions, whose boundary curves carry deck automorphisms permuting components, are the natural candidates.

**Consequence for the chain.** If some D^{m+1} of the chain is a piece of this kind, the induction claim (b), "x_{m+1} is Y-persistent along β̃_{m+1}", is false. MS10's hypothesis at J_{m+1} is then never available, and MS10 is vacuous there. So **the derivation "MS8 ⇐ MS10" is not correct as worded.** It has to be rephrased component-wise, as follows.

**Lemma B1 (components of a transport family; proved).** Let Q ∈ B_0, b a branch of B_0 at Q with lift b̃, Ñ := Ñ_b̃, and let Stab(b̃) ⊂ Aut(Q) be the pointwise stabiliser of b̃. Then:
- (a) every irreducible component Ñ^1 of Ñ maps onto N = H((b ∖ Q) × Δ_ε), and Ñ^1 ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0;
- (b) Stab(b̃) permutes the irreducible components of Ñ transitively;
- (c) for α ∈ Stab(b̃) and every component Ñ^1: x is Y-persistent on Ñ^1 iff α x is Y-persistent on α Ñ^1;
- (d) if Δ_{G_Q} is of product type, then a label of positive-dimensional type is Y-persistent on one component iff it is Y-persistent on all of them. Hence the component-wise notion agrees with MS10's.

*Proof.*
- (a) N is a topological 4-manifold (H is a homeomorphism), so its germs are irreducible. By Remmert, q(Ñ^1) is an irreducible analytic set of dimension 2 in N, hence all of N. So Ñ^1 meets {t = 0}, where Ñ ∩ {t = 0} = b̃ ∖ 0. Since t is non-constant on Ñ^1, Krull makes the slice pure 1-dimensional. A 1-dimensional analytic subset of the irreducible curve germ b̃ ∖ 0 contains an open subset of it.
- (b) Let p̃ ∈ b̃ ∖ 0 be generic, so Stab(p̃) = Stab(b̃) (stabiliser jumps on the curve b̃ form a discrete set). Near (p̃, 0), q is the quotient by Stab(p̃). So the germ components of q^{-1}(N) at (p̃, 0) are permuted transitively by Stab(p̃), because the germ of N there is irreducible (R7-4 Lemma 2(a) argument). Each of them has its t = 0 slice in b̃ (by (a), applied to the germ), so it lies in Ñ. Every global component of Ñ contains such a germ for generic p̃, by (a). An element α ∈ Stab(b̃) maps Ñ to Ñ, because αÑ is the component of q^{-1}(N) containing αb̃ ∖ 0 = b̃ ∖ 0. So α maps global components to global components. Transitivity on germs at (p̃, 0) therefore gives transitivity on global components.
- (c) By (K3), F_x(αp) ≅ F_{α^{-1}x}(p), and α preserves intactness patterns. So persistence of y on Ñ^1 is persistence of αy on αÑ^1.
- (d) By Lemma PT (round9_q3 §3), every α ∈ Aut(Q) fixes x. Combine with (b) and (c). ∎

**Repaired notion and repaired missing statement.**
- *x is Y-persistent on a component*: there is an irreducible component Ñ^1 of Ñ_b̃ such that x is intact and F_x(p) ≅ Y_t at every (p, t) ∈ Ñ^1.
- **MS10′** is MS10 with both the hypothesis and the conclusion read in this component-wise sense. Hypothesis: x is Y-persistent on some component of Ñ_β̃. Conclusion: x is Y-persistent on some component of Ñ_b̃.
- At product-type points MS10 and MS10′ coincide, by B1(d). At non-product points neither implies the other formally.

**The chain with MS10′ (checked).**
1. *Base.* Δ_Γ is of product type, so by B1(d) nothing changes.
2. *Product-type junctions.* round9_q7 Lemma J and Corollary J′ are already component-wise: they use a germ component 𝒲̃^a ⊃ β̃ with persistent vertex x. Their conclusion, persistence on a germ component 𝒲̃″ ⊃ b̃, gives persistence on the global component of Ñ_b̃ that contains that germ, by the identity principle (the persistence set is analytic, round9_q7 Lemma S(c)).
3. *Transfer along a travel interval* (this is what step (b) asserts, now proved component-wise, given the Gap A repair). Let Ñ′^1 be a component of the leaving family at J_m on which x_m ↔ c is persistent, and let 𝒲̃ be the lifted family component containing Π_S(Ñ′^1). Its t = 0 slice contains an arc of the track's lifted curve E, hence all of E. Let p̃ ∈ β̃_{m+1} ∖ 0 be generic at J_{m+1}, with Π_S(p̃) = z ∈ E.
   - Near p̃, Def(J_{m+1}) is a versal deformation of the curve C_p̃.
   - Near (p̃, 0), Π_S maps the germ components of q^{-1}(N″) finitely onto the germ components of ξ^{-1}(κ(D)) at (z, 0). So some germ component maps into 𝒲̃.
   - Its t = 0 slice lies on β̃_{m+1}, so it lies in Ñ″ := Ñ_{β̃_{m+1}}. Let Ñ″^1 be the global component containing it.
   - By the identity principle, Π_S(Ñ″^1) ⊂ 𝒲̃.
   - The chart label x_{m+1} corresponds to the factor c, by K_w Step 3 and the Gap A repair.
   - By Lemma S(c) (persistence is global on the irreducible 𝒲̃), x_{m+1} is Y-persistent on Ñ″^1.
4. *Non-product junctions and R(D)-points:* MS10′.
5. *Endpoint.* MS10′ gives a component Ñ^1 of Ñ_b̃ on which x is Y-persistent. By B1(a), its t = 0 slice is an open subset of b̃ ∖ 0, on which x is intact with F_x ≡ Y_0. By the identity theorem on the irreducible curve b̃ and the constancy of the pattern, x is intact along b̃ and F_x ≡ Y_0 there. This contradicts MERGE and MOV, as in chain step (d).
6. Product-type endpoint, (c) of the chain: unchanged, by B1(d).

So, after the repairs of 2.1 and 2.2, **the chain reduces the goal to (Rig) + MS10′, invoked at non-product junctions, non-product endpoints and the points of R(D).** I found no other flaw in the parts I checked (steps (a)–(d) and the base). I did not re-derive Prop K_w's marking details, Lemma PA, or the cited Teichmüller facts.

---

## 3. Attempt on MS10 / MS10′

Setting: as in MS10′. Q ∈ B_0 lies in a non-product stratum, x is Y-persistent on a component Ñ^1_β̃ of Ñ_β̃, Y is non-constant, and Q_t := H_t(Q).

### 3.1 The deformation must move Q off itself (proved)

**Lemma 3.1.** Assume Q is isolated in B_0 ∩ Δ_{G_Q}, i.e. Q is a puncture of every piece through it. This holds at every junction and endpoint of the walk chain that is not a crossing. Then:
- (a) for small τ, B_τ ∩ Δ_{G_Q} ∩ U = {Q_τ} for a fixed neighbourhood U of Q;
- (b) F_x(q_τ) ≅ Y_τ at some lift q_τ of Q_τ;
- (c) the set T_Q := {τ : Q ∈ closure(V_τ)} is closed and discrete near 0. More generally, no point Q′ of Δ_{G_Q} near Q lies in closure(V_τ) for τ in a set accumulating at 0, unless [Y_τ] = [F_x(q′)] there for a lift q′ of Q′.

*Proof.*
- (a) Choose U with B_0 ∩ Δ_{G_Q} ∩ closure(U) = {Q}. Suppose P_n ∈ B_0 ∩ Δ_{G_Q} and τ_n → 0 with H_{τ_n}(P_n) ∈ U converging to Q. Since H is a homeomorphism with H(Q, 0) = (Q, 0), (P_n, τ_n) → (Q, 0), so P_n = Q for n large. H_τ maps B_0 ∩ Δ_{G_Q} onto B_τ ∩ Δ_{G_Q} by (R2). So (a) holds.
- (b) By Lemma B1(a), q(Ñ^1) = N := H((β ∖ Q) × Δ_ε). For fixed τ the slice N_τ accumulates at Q_τ, and q is proper. So the closure of Ñ^1_τ contains a lift q_τ of Q_τ. F_x ≅ Y_τ on Ñ^1_τ, and F_x is continuous on the closed set L_x ∋ q_τ.
- (c) If Q ∈ closure(V_τ), then Q ∈ B_τ ∩ Δ_{G_Q} ∩ U, so Q = Q_τ by (a). Then q_τ = 0, because q^{-1}(Q) = {0}, and (b) gives [Y_τ] = [F_x(0)] = [Y_0]. Since [Y] is holomorphic and non-constant (PR-A), this happens only on a closed discrete set. The general statement is the same argument with Q′ in place of Q. ∎

So, in MS10's setting, the cusp Q of V_0 is not a boundary point of V_τ for generic small τ. Every object attached to Q at τ = 0 must move with Q_τ.

### 3.2 Consequence for the surviving obstruction (A2-disc), using rigidity of Teichmüller curves (conditional)

Recall round9_q5 Corollary 2. A failure of MS10 at Q (under the readings (R3), (T4) used there) needs α ∈ Γ moving x and a 2-dimensional relevant component Φ of Fix(α) ∩ 𝒳. In case (A2-disc), Φ_0 lies on the lift of a Teichmüller curve 𝒯 ⊂ V_0 of α-symmetric curves with cusp Q. For each small τ ≠ 0, Φ_τ is a curve of α-symmetric curves in V_τ.

**Cited fact (Rigidity of Teichmüller curves; from memory: McMullen, "Rigidity of Teichmüller curves", 2009; also Möller 2006 via variations of Hodge structure).** Let f: C → M_g be (the normalisation of) a Teichmüller curve. If f_s: C_s → M_g, s ∈ Δ, is a holomorphic family of holomorphic maps, defined on a holomorphic family of Riemann surfaces of finite type C_s with C_0 = C, and f_0 = f, then f_s(C_s) = f(C) for all s. I state this in the form I need. I have not checked whether the published statements are literally this form, in particular in the orbifold sense.

**Proposition 3.2 (conditional; partial).** In the setting of MS10/MS10′ with Q isolated in its stratum, suppose case (A2-disc) occurs. Let Φ^glob be the irreducible component of 𝒱 ∩ (M_g^{[h]} × Δ) containing q(Φ), where M_g^{[h]} is the closed locus of curves admitting an automorphism of the topological type h of α. Assume:
- **(Eq)** after a base change τ = s^k, the family of curves Φ^glob_τ is the image of a holomorphic family f_s: C_s → M_g as in the cited fact, with f_0 the normalisation of 𝒯.

Then (Eq) is impossible. So in case (A2-disc), the α-symmetric curves Φ_τ ⊂ V_τ do **not** form an equisingular deformation of the Teichmüller curve 𝒯.

*Proof.* By rigidity, f_s(C_s) = 𝒯 for all s, so 𝒯 ⊂ V_τ for all small τ. Q is a cusp of 𝒯, so Q ∈ closure(𝒯) ⊂ closure(V_τ) for all small τ. This contradicts Lemma 3.1(c). ∎

**What this means.** In a hypothetical failure of MS10 of type (A2-disc), the closure of Φ^glob is a 2-dimensional analytic family of curves, proper over Δ. Its central fibre contains closure(𝒯) but is not an equisingular limit of the Φ_τ. Either:
- the central fibre has other components, which by Lemma TG are further Teichmüller curves of h-symmetric curves of V_0, or boundary curves (case (B)); or
- closure(𝒯) appears with multiplicity, or the family acquires extra cusps that move into the boundary at τ = 0.

In every case Φ_τ must "let go" of the cusp Q (Lemma 3.1). This is new information on (O1″) of round9_q5, but it does not exclude (A2-disc). Removing (Eq) would need a rigidity statement for Teichmüller curves that appear as one component of a degenerate fibre. I do not know such a statement, and I suspect it is false in general.

### 3.3 The interior mechanism of a twin jump is locally realisable with V_0 coarse-smooth (proved, local model)

This explains why, once more, local arguments cannot finish. The model is in the right dimension: complex surfaces, so that the bad locus has real codimension 2 in the 3-fold family and the squares of R8-5 / round9_q5 do meet it.

Let α act linearly on C^n ⊃ (germ of T_g) with fixed space F, of dimension k, and (−1)-eigenspace N, of dimension r ≥ 1. The coarse germ is F × (N/±1). Embed N/±1 by n ↦ n ⊗ n. Pick d ∈ F and v = v_F + v_N with v_N ≠ 0 and v_F ∉ C·d. Put
- S := {a d + b v : a, b ∈ C} and αS = {a d + b(v_F − v_N)}. Both contain the line D := C·d ⊂ F, and S ≠ αS;
- V_0 := image of S = {(a d + b v_F, b² v_N ⊗ v_N)}. The map (a, b) ↦ this is an injective immersion, so V_0 is a **smooth** surface germ in the coarse space, and its preimage is S ∪ αS, two sheets crossing along D;
- V_τ := {(a d + b v_F, (b² + τ) v_N ⊗ v_N)}. This is again an injective immersion, so a smooth surface germ, and τ ↦ V_τ is a smooth, topologically trivial family. Its preimage is {a d + b v_F + c v_N : c² = b² + τ}, which is **irreducible** for τ ≠ 0: the two sheets S, αS merge;
- V_τ ∩ (image of F) = {b² = −τ}, a curve for each τ ≠ 0. So Fix(α) meets the family in a 2-dimensional relevant set Φ with Φ_0 = D. This is case (D2)/(A2-disc) of round9_q5, with D playing the role of the lifted Teichmüller curve 𝒯 (Lemma TG says S ∩ Fix(α) is a Teichmüller disc when S is totally geodesic; in the linear model S, αS are linear subspaces).

So two lifted sheets of a coarse-smooth V_0 that cross along a curve of symmetric curves can be merged by a coarse-smooth deformation. On the merged sheet, a label carried along S continues onto αS, i.e. onto its twin. Total geodesy of V_0 at τ = 0 constrains only S and αS (both totally geodesic, meeting along a Teichmüller disc). It says nothing about the merging, because V_τ is not totally geodesic. Excluding the twin jump therefore needs **global** input: for instance a global form of Proposition 3.2 (what the symmetric curves Φ_τ can converge to), or a global count. I could not supply it.

### 3.4 Where a proof of MS10′ would have to come from (analysis, not proved)

Combining §1, §3.1–3.3 with the prior results:
- A failure of MS10′ at Q needs, in the 3-fold 𝒳, two lift-curves λ ≠ λ′ of Q_t (round9_q2 Lemma 2), an α ∈ Γ moving x, and a 2-dimensional α-fixed family Φ (round9_q5). In case (A2-disc) it also needs a non-equisingular degeneration of α-symmetric curves of V_τ onto a Teichmüller curve 𝒯 ⊂ V_0 with cusp Q, which must leave Q (Prop 3.2, Lemma 3.1).
- Each of these is locally realisable (§3.3, R7-3 §5, round9_q6 §4).
- By §1, a proof must use "Y non-constant". The only global consequence of Y non-constant used so far is genericity (finiteness via (Rig)). Lemma 3.1 is a second, different use: the cusp moves. A possible route, which I did not complete: the curve τ ↦ Q_τ is holomorphic (round9_q2 §1, R8-6 Lemma 3.1), non-constant by Lemma 3.1, and its x-twins satisfy [F_x(q_τ)] = [Y_τ] ≠ [F_{α^{-1}x}(q_τ)] at generic τ (round9_q8 Lemma 1′). Comparing this with the h-symmetric curves Φ_τ, which accumulate at a point of B_τ near Q_τ (by Lemma 3.1 not at Q), might force (Ψ-J) at a lift of Q_τ, and with it α ∈ Aut(Q_τ). That would contradict the separation of the twins. The missing step is to show that the trace Ψ of Φ is of type (Ψ-J), i.e. to exclude (Ψ-Z) and (B-pure). This is exactly the open part of round9_q5 §§3–4, and I could not close it.

---

## 4. Summary

**Proved here** (modulo the cited standard facts and the prior results used as stated):
1. **Proposition 1.1.** MS10 is vacuous whenever the problem's claim holds. Any counterexample to MS10 is a counterexample to the problem for (Rig)-families. So the counterexample option is equivalent to disproving the problem.
2. **Gap A in the chain** (walk chain / step (b)): at points of R(D) of a non-product piece D, the tracked label can switch to a twin in the middle of a travel interval. Such points need not lie in the special set Σ; a smooth local model is given. **Repair:** add the finite sets R(D) to Σ. The new transitions are MS10 configurations at non-product points, which MS10 already allows.
3. **Gap B in the chain:** under (R2), a transport family Ñ can be reducible. R7-3 Lemma 2, step 2 ("Ñ is a connected 4-manifold, hence irreducible") is false in general; an explicit local model is given. In that model no label is Y-persistent along β̃ in MS10's sense, although no twin jump occurs. So chain step (b), as worded, can fail at non-product pieces.
   - **Lemma B1:** the components of Ñ are permuted transitively by the pointwise stabiliser of b̃, and persistence transforms by (K3). In product-type strata the component-wise and the global notions agree.
   - **Repair:** the component-wise MS10′. The chain then goes through: base, product-type junctions (round9_q7 Lemma J is already component-wise), transfer along travel intervals (proved here component-wise, given the Gap A repair), and the endpoint.
4. **Lemma 3.1:** in MS10's setting, with Q isolated in its stratum, Q ∉ closure(V_τ) for τ outside a discrete set, i.e. the cusp must move.
5. **§3.3:** an explicit coarse-smooth local model in which a deformation merges two lifted sheets of V_0 crossing along a curve of symmetric curves. This is the interior mechanism of a twin jump, case (D2)/(A2-disc).

**Proved only conditionally (partial):**
- **Proposition 3.2:** case (A2-disc) cannot occur through an equisingular deformation (Eq) of the Teichmüller curve 𝒯. This depends on a rigidity theorem for Teichmüller curves (McMullen / Möller), cited from memory in a form I did not verify, and on the extra hypothesis (Eq).

**Not proved:**
- MS10 and MS10′ themselves. I give no proof and no counterexample; by Proposition 1.1, a counterexample would disprove the problem.

**Open (precise):**
- (Q1) MS10′ at non-product junctions, endpoints and R(D)-points.
- (Q2) Case (A2-disc) without (Eq): can the h-symmetric curves Φ_τ ⊂ V_τ degenerate non-equisingularly onto a configuration containing a Teichmüller curve 𝒯 ⊂ V_0 with cusp Q, while leaving Q (Lemma 3.1)?
- (Q3) Cases (A2-sheet), (B-pure) and (D3) of round9_q5, untouched here.
- (Q4) Entry 82, (Rig), still needed in addition to MS10′.
- (Q5) Whether the Gap B configuration (a non-product piece all of whose curves carry an automorphism exchanging two Y_0-copies) actually occurs for a smooth totally geodesic V_0. If it never occurs, MS10 can be used as originally worded.
- The inputs inherited from earlier rounds (Prop K_w's marking details, Lemma PA, (Fl), (R3), (T4)) are not re-proved here.

=== END OF ANSWER round10_q3 ===

