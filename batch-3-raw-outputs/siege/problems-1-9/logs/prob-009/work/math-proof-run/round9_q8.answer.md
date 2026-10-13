kind: attempt (round9_q8)

## Status line
Plan: (1) record two short lemmas that hold in configuration (PT): the partner of the twin on the incoming side, and the frozen terminal function; (2) push Option 1 (several mechanisms, each tested); (3) Option 2 (what a realisation needs).
Outcome: **(PT) is neither excluded nor realised.** MS8 stays OPEN. What is proved is structural information that every realisation of (PT) must have (§§1–2). §3 records why each Option-1 mechanism I tried does not close the gap, and §4 does the same for Option 2.

Throughout, the readings (R1), (R2) with H_0 = id, the hypotheses of MS8 including (Rig), the input (K′) of R8-8, and (PT_chain) are assumed as in the task file. Notation is as in R8-8: Ñ^m_+, Ñ^{m+1}_−, Ñ^E are the transport families, (∗) is the identity F_x ≡ φ_c(t) on closure(Ñ_t), (K3) is F_x(σq) ≅ F_{σ^{-1}x}(q), A is the finite class set of R8-8 Lemma 2, and "generic t" is as in R8-8 §4 (t ∉ Z = Z_A ∪ Z_φ ∪ D_all). [·] denotes the class in M_{g_i,n_i}/S_{n_i}.

## 1. Proved: the twin partner on the incoming side (Lemma 1)

**Setting.** We are in case (i) of (PT), i.e. R8-8 Proposition 3, junction case (b). So [φ_{c_m}] ≡ [Y] and [φ_{c_{m+1}}] ≢ [Y]. Fix a generic t and a point j̃ ∈ closure(Ñ^m_{+,t}) ∩ π^{-1}(J_{m,t}). Pick a ∈ Aut(J_m) with j̃ ∈ closure((aÑ^{m+1}_−)_t), as in the proof of Proposition 3.

**Lemma 1.**
- (a) F_{x_m}(j̃) ≅ Y_t and F_{a x_m}(j̃) ≅ φ_{c_{m+1}}(t). In particular a x_m ≠ x_m.
- (b) Let v be the vertex of D^m that contains the chart vertex a x_m along β̃^m_+. Exactly one of the following holds.
  - (α) *Frozen partner.* v is merged along β̃^m_+, or v = {a x_m} is intact and non-constant on D^m with J_m ∉ stratum(D^m). Then [φ_{c_{m+1}}] ≡ [Y_0] is constant.
  - (β) *Persistent partner.* v = {a x_m} is intact and constant on D^m, v ≠ c_m, and [φ_v] ≡ [φ_{c_{m+1}}]. So D^m carries two distinct constant vertices, c_m and v, both ≅ Y_0 at t = 0, with value functions [Y] and [φ_{c_{m+1}}].
  - (γ) *Incoming crossing.* v = {a x_m} is intact and non-constant on D^m, and J_m ∈ stratum(D^m).

*Proof.*
(a)
- a acts on Def(J_m) only, not on t. Hence a^{-1}·closure((aÑ^{m+1}_−)_t) = closure(Ñ^{m+1}_{−,t}), so a^{-1} j̃ ∈ closure(Ñ^{m+1}_{−,t}).
- c_{m+1} = {x_m} along β̃^{m+1}_−. By (∗), F_{x_m}(a^{-1}j̃) ≅ φ_{c_{m+1}}(t).
- By (K3) with σ = a^{-1}, F_{x_m}(a^{-1}j̃) ≅ F_{a x_m}(j̃).
- By (∗) on Ñ^m_+, F_{x_m}(j̃) ≅ φ_{c_m}(t) ≅ Y_t.
- If a x_m = x_m, then [Y_t] = [φ_{c_{m+1}}(t)]. That is excluded since t ∉ Z_φ.

(b) The three cases exhaust the possibilities. Either v contains an unpinched edge, or v is a singleton {a x_m}, which is then constant or non-constant on D^m.
- (α), merged case.
  - An unpinched edge along β̃^m_+ means J_m ∉ stratum(D^m). So the limit of the transported branch at j̃ is a puncture p′ of D^m_t (R8-8 Theorem 1, Step 2).
  - f_v(p′) is glued from the F_y(j̃), y ∈ v. It contains F_{a x_m}(j̃) as a component with its special points (R7-1 Lemma 1(a)).
  - f_v(p′) is nodal, so v ∈ M(D^m_t). By R8-8 Lemma 2, f_v(p′) ∈ F.
  - Hence [φ_{c_{m+1}}(t)] ∈ A. Here a x_m has the type (g_i,n_i) of x_m, since a is an automorphism.
- (α), non-constant singleton case. Since t ∉ D_all, v ∈ M(D^m_t). Then f_v(p′) = F_{a x_m}(j̃) ∈ F, and again [φ_{c_{m+1}}(t)] ∈ A.
- (α), conclusion. In both sub-cases [φ_{c_{m+1}}(t)] ∈ A for all generic t, a set accumulating at 0. By R8-8 Lemma 1, [φ_{c_{m+1}}] is constant, and its value at t = 0 is [Y_0].
- (β).
  - By (∗) applied to (Ñ^m_+, v), F_{a x_m} ≡ φ_v(t) on closure(Ñ^m_{+,t}). So [φ_v(t)] = [φ_{c_{m+1}}(t)] for every small t, and the identity theorem gives [φ_v] ≡ [φ_{c_{m+1}}].
  - v ≠ c_m, because a x_m ≠ x_m and distinct intact chart vertices are distinct vertices of G_{D^m}.
  - At t = 0, φ_v(0) ≅ F_{a x_m}(0) ≅ F_{x_m}(a·0) = F_{x_m}(0) ≅ Y_0. ∎

**Endpoint analogue (Lemma 1′).** Case (ii) of (PT): Q_0 has copies x and x′ = a^{-1}x, x merges (or puncture-moves) along β̃^E, and x′ is intact and constant on E with [φ_{x′}] ≡ [Y]. Choose q̃(t) ∈ closure(Ñ^E_t) ∩ π^{-1}(Q_t) with F_{x′}(q̃(t)) ≅ Y_t. Then for all small t:
- [F_x(q̃(t))] = [Y_0] (**the merging copy is frozen**);
- at the D^k-side lift a q̃(t), the chart vertex x is the Y_t-copy and the chart vertex a x has frozen class [Y_0].

*Proof.*
- q̃(t) lies over Q_t ∈ Δ_{G_{Q_0}}, so q̃(t) ∈ L_x. Its pinching pattern is that of β̃^E, so x is merged (or moving at a puncture) along Ñ^E_t.
- By R7-1 Lemma 1 and R8-8 Lemma 2, [F_x(q̃(t))] ∈ A for every t.
- F_x is continuous on L_x, and q̃(t) → 0, so [F_x(q̃(t))] → [Y_0]. A is finite, hence [F_x(q̃(t))] = [Y_0] for small t.
- The last claim follows from (K3): F_x(a q̃) ≅ F_{a^{-1}x}(q̃) = F_{x′}(q̃) ≅ Y_t, and F_{ax}(a q̃) ≅ F_x(q̃) ≅ Y_0. ∎

## 2. Proved: the tracked function is frozen at a coherent endpoint (Lemma 2)

**Lemma 2.** Suppose the endpoint is MERGE or pMOV and (C_k) holds, i.e. (SC_k) or (NT_k). Then [φ_{c_k}] ≡ [Y_0]. **No assumption [φ_{c_k}] ≡ [Y] is needed.**

*Proof.* This is R8-8 Theorem 1, Step 2, with Y_t replaced by φ_{c_k}(t).
- Step 2 uses only (∗) for (Ñ^k_+, c_k), giving a q̃ with F_x(q̃) ≅ φ_{c_k}(t), together with R8-8 Lemma 2.
- It yields [φ_{c_k}(t)] ∈ A for t in a set accumulating at 0.
- By R8-8 Lemma 1, [φ_{c_k}] is constant, and its value at t = 0 is [Y_0]. ∎

**Corollary 3 (bookkeeping along the chain).** Put f_m := [φ_{c_m}], so f_1 = [Y]. By R8-8 Theorem 1, Step 1, f_{m+1} = f_m whenever (C_m) holds. Assume Y is non-constant. Then:
- either the endpoint is a twin (case (ii)), with a frozen merging copy by Lemma 1′;
- or (C_k) holds and f_k ≡ [Y_0] is constant (Lemma 2), so f jumps at least once on its way from the non-constant [Y] to a constant.

At the first jump m_1, Lemma 1 applies (when the jump is of type (b)). It shows that the twin pair at J_{m_1} carries, at a single lift j̃, the two classes [Y_t] and f_{m_1+1}(t). The partner of the Y-copy is either frozen (α), persistent on D^{m_1} (β), or a crossing (γ).

**Consequence.** Every realisation of (PT) has a point of B_0 with an automorphism a exchanging two Y_0-copies whose deformations differ, one ≅ Y_t and the other of another class (often the frozen class Y_0). By R8-8 §3 this is possible only if |Aut(J_{m,t})| < |Aut(J_m)| for generic t, i.e. only under the coarse reading (R2). This sharpens R8-4 (T1)–(T2), but it is not a contradiction.

## 3. Option 1: mechanisms tried, and where each one stops

**3.1 Interior paths (thin squares). Reduction proved; it lands on R8-5 Proposition D.**
- At t = 0, β̃^m_+ and β̃^{m+1}_− lie on a common irreducible component X_0 of the lifted germ S̃_0 at 0 ∈ Def(J_m). So their interior neighbourhoods are joined by paths γ in X_0 ∖ {∏ s_e = 0} inside B(0, ρ), for every ρ.
- Fix a generic t. Let d(t) > 0 be the minimal distance between distinct lifts of J_{m,t}. Use the quotient metric, so that π^{-1}(B(J_{m,t}, r)) is the union of the balls B(ℓ, r) around the lifts ℓ.
- H is uniformly continuous on closure(V_0) × Δ̄_r. Hence for ρ small, H_t(π(γ)) ⊂ B(J_{m,t}, d(t)/3), and every lift of it lies in a single ball.
- If the square (τ, s) ↦ H_s(γ(τ)), s ∈ [0, t], lifts to Def(J_m) without monodromy, then:
  - the left edge, the transport of a point near β̃^m_+, ends in the ball of j^m(t);
  - the right edge ends in the ball of j^{m+1}(t);
  - so j^m(t) = j^{m+1}(t), which is (SC_m).
- The monodromy is non-trivial only if the square meets the branch locus. The branch locus consists of curves of V_σ that have an automorphism coming from Aut(J_m) and moving x_m, at points within distance ω(ρ) of J_{m,σ}.
- For σ bounded away from 0, a small ρ avoids such points. As σ → 0 it does not. This is exactly Proposition D, cases (A), (B), (C), of R8-5.
- So 3.1 gives no new exclusion. It does give a clean reformulation: **a twin jump at J_m happens only if curves of V_σ with an extra automorphism moving x_m accumulate at J_m as σ → 0.**

**3.2 Lock from a persistent automorphism along D^{m+1}. Dead.**
- By Lemma 1(a), at generic t the two copies at j̃ have different classes, Y_t and φ_{c_{m+1}}(t).
- So no automorphism exchanging c_{m+1} and w can persist along the transported piece D^{m+1}_t.
- An automorphism exchanging them along D^{m+1} at t = 0 (which total geodesy might supply) is not transported, because H_t need not preserve automorphism groups under (R2).
- Under (R2^orb) it would be transported, and the twin problem disappears altogether (R8-8 §3).

**3.3 Restarting Prop K on the partner. Reduces to MS7.**
- Lemma PA and Prop K apply to any piece and any constant vertex. Restarting from (D^{m+1}, w) with [φ_w] ≡ [Y] gives a new chain, which may jump again.
- The set of pairs (D, c) at time 0 is finite, so the restarts eventually cycle. I found no quantity that decreases strictly along a restart, for example one tied to Teichmüller levels.
- This is MS7 of R7-3: the Y-network is an Aut-closed set.

**3.4 Krull pair at one lift (endpoint case). Consistent, so no contradiction.**
- At generic t, at q̃(t) (Lemma 1′), x′ is the Y_t-copy.
- By Lemma G (R8-4), every boundary branch through q̃(t) keeps x′ intact.
- Let X be an irreducible component, through q̃(t), of the preimage of closure(V_t). Then X ∩ {∏ s_e = 0} = X ∩ L_{x′} = X ∩ {s_f = 0} for each edge f at x′. All of these sets are 1-dimensional, by Krull.
- This holds only in a ball whose size depends on t, and the time-0 limit of these balls is the point 0. It is compatible with the R7-3 §5 local model.

**3.5 Total geodesy in case (A) of Proposition D. Sketch only.**
- Fix(α) lifts to a totally geodesic complex submanifold of T_g, the image of the Teichmüller space of the quotient orbifold.
- Teichmüller geodesics are unique, so Fix(α) ∩ (lift of V_0) is geodesically convex. Hence any 1-dimensional component of it is a Teichmüller disc, so Fix(α) ∩ V_0 near J is a union of Teichmüller curves of α-symmetric curves, with J in their closure.
- I could not show that such a curve forces the twins at J_{m,t} to stay isomorphic (Lock).
- Cases (B) and (C) are untouched. Case (C) is invisible at t = 0.

## 4. Option 2: what a realisation of (PT) needs; not achieved

A counterexample to MS8 through (PT) needs all of the following.
1. A smooth closed totally geodesic V_0 whose network has a point J (or Q_0) with an automorphism a exchanging two Y_0-copies. At a junction, one copy is the tracked copy x_m, and by Lemma 1 the incoming piece carries a frozen, persistent or crossing partner. At the endpoint, one copy merges.
2. At every cusp of ∂V_0, the conditions (Tw1)+(C1)+(C2) must fail (R8-4 Theorem 2V), and so must (IP), (U_J) and (NB).
3. A family V_t satisfying (R1), (R2) and (Rig) with the following properties:
   - |Aut(J_t)| < |Aut(J)| for generic t;
   - the copies separate as Y_t versus φ′(t) (Lemma 1), where φ′ is often the frozen constant Y_0;
   - curves with an automorphism moving x_m accumulate at J as t → 0 (§3.1).

What is known about each of these:
- Item 1 is typical for Galois covering constructions, where deck groups permute boundary components. But the run found merges at cusps of ∂V_0 for every Galois construction over M_{0,5} and M_{1,2}, so these constructions do not obviously satisfy item 2. Item 2 is unchecked for any smooth example. The quintic example (PR-I) is not smooth, and it satisfies Theorem 2V anyway.
- Item 3 is entirely open. The local chart models (R7-3 §5, R8-4 §5, R8-5) satisfy every local constraint known, including (Rig), Lemma G, Lemma X and Krull. But I know no method to build a non-totally-geodesic deformation V_t whose boundary is controlled stratum by stratum.
- **No counterexample is claimed.**

## 5. Summary

**Proved.**
- Lemma 1 and Lemma 1′: the twin partner at a jump carries the other class function at the same lift. On the incoming side it is frozen (constant [Y_0]), persistent, or a crossing. The merging copy at an endpoint twin is frozen.
- Lemma 2: at a coherent MERGE/pMOV endpoint, the tracked function is frozen, [φ_{c_k}] ≡ [Y_0].
- Corollary 3: the bookkeeping of value functions along Prop K's chain.
- §3.1: the reformulation of a twin jump as accumulation of symmetric curves of V_σ at J_m.

**Not proved / open.**
- Whether (PT) can occur, i.e. the twin half of MS8.
- MS7: no Aut-closed Y-network exists.
- Lock in cases (A), (B), (C) of Proposition D.
- Entry 82 ((Rig) itself).
- A realisable family V_t for any candidate V_0.

**Conditional.** Under the orbifold reading (R2^orb), twin jumps cannot occur (R8-8 Corollary 1(a)), and MS8 then reduces to the interior-MOV endpoint case.

=== END OF ANSWER round9_q8 ===

