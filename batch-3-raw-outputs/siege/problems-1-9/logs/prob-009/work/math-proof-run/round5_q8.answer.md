# round5_q8: MS4. No counterexample found. A new pinning theorem (partial result)

## 0. Plan and status
- **Goal.** Decide MS4: construct a counterexample, or prove the statement.
- **Outcome.**
  - I did **not** construct a counterexample.
  - I did **not** prove MS4 in general.
  - I prove a new conditional theorem, **Theorem M**. It pins Y_t using a *merged boundary curve whose normalization is a thrice-punctured sphere*. It replaces the Hodge-theoretic Proposition D and the cited results (K), (Ct), (H2') of PR-3 by the Imayoshi–Shiga finiteness theorem. Teichmüller rigidity of a thrice-punctured sphere makes that theorem applicable.
  - I find a **gap in PR-3 Theorem E**: it does not track automorphisms of the cusp curve P_0. Theorem M states the needed hypothesis (M2) explicitly, and §3 explains why some such hypothesis is needed.
  - **Corollary N** applies Theorem M to cyclic covering constructions from M_{0,5}. There the merge hypothesis (M1) and the (0,3) hypothesis (M3) are *proved*. The hypotheses (M2), (M4), (M5) remain to be checked case by case.
- Throughout I assume the readings (R1), (R2) of the task, and I use PR-1 (holomorphy of t ↦ Y_t). I re-checked PR-1's argument and found it sound. I also use P-b Lemma 1: every point of closure(∂V_t) contains Y_t as an intact component at vertex i. This follows from the properness of the gluing map, as in PR-2 step 2.

## 1. Setting and notation
- H : closure(V_0) × Δ → closure(𝒱) is the stratified homeomorphism of (R2). Write H_t = H(·, t).
- **Orbifold chart at a point P_0 of Δ_{G'}.**
  - W̃ = ∏_{w ∈ V(G')} U_w × ∏_{e ∈ E(G')} D_e is the base of the Kuranishi family of P_0. Here U_w is a small ball in the deformation space of the pointed component P_0^w, and s_e ∈ D_e is the plumbing coordinate.
  - K_0 = Aut(P_0) acts on W̃, and q : W̃ → W̃/K_0 ≅ W is a neighbourhood of P_0 in M̄_g (standard; cited).
  - For k ∈ K_0 and P ∈ W̃, the curves C_P and C_{kP} are isomorphic by an isomorphism that sends the component of vertex w to the component of vertex k(w). Hence x_{k(w)}(kP) ≅ x_w(P) as pointed curves, up to relabelling of the special points.
  - N_0 ⊂ W̃ is a small K_0-stable ball around P̃_0.
- **Faces.** For S ⊂ E(G'), the face is Φ_S = {s_e = 0 for e ∈ S, s_e ≠ 0 for e ∉ S} ∩ N_0.
  - Φ_S is connected: it is a product of balls and punctured discs.
  - Points of Φ_S have dual graph G'/(E(G') \ S), with vertex classes the connected components of (V(G'), E(G') \ S).
  - For a vertex class c, Plumb_c : W̃ → M̄_{g_c,n_c} is the holomorphic map that plumbs the components w ∈ c along the edges inside c. On Φ_S it takes values in M_{g_c,n_c}.
- **Lifted branches and the merge property.** A local branch c of a curve lying in a stratum at P_0 has lifts c̃ through points of q^{-1}(P_0). Such a lift lies, off P̃_0, in a single face Φ_{S(c̃)}, because the face type is locally constant on the connected punctured branch.

## 2. Theorem M

**Theorem M.** Assume (R1), (R2) and the hypotheses of the problem. Suppose there exist:
- a stratum Δ_G that is a **product stratum** (M5), with factor projections π_u;
- an irreducible 1-dimensional component E_0 of closure(V_0) ∩ Δ_G;
- a point P_0 ∈ closure(E_0) ∩ closure(∂V_0), lying in a stratum Δ_{G'};
- a local branch β of ∂V_0 at P_0, a local branch b of E_0 at P_0, and lifts β̃, b̃ through the *same* point P̃_0 ∈ q^{-1}(P_0);

such that the following hold.
- **(M1) Merge.** By P-b, the global vertex i of Γ corresponds, on β̃, to a single vertex of G' (also called i), all of whose edges lie in S(β̃). Let c_b be the vertex class of b̃ containing i. Then some edge of G' incident to i is not in S(b̃). In other words, c_b contains an edge of G' that is unpinched along b̃. Let v ∈ V(G) be the global vertex that corresponds to c_b on b̃ (see Step 1), and let M_{h,m} be its factor.
- **(M2) Automorphisms.** Every automorphism k of the stable curve P_0 satisfies k(i) ∈ c_b, for the action of k on the dual graph G'.
- **(M3) Rigid normalization.** The normalization Ẽ_0 of E_0 is a thrice-punctured sphere. Its punctures are the ends of E_0, that is, the points of closure(E_0) \ E_0 counted with branches.
- **(M4) Fine target.** M_{h,m} has no orbifold points. This holds if h = 0, or if m ≥ 2h + 3, because a nontrivial automorphism of a genus-h curve fixes at most 2h + 2 points.

Then Y_t = Y_0 for all t ∈ Δ.

**Cited results (from memory).**
- **(IS) Imayoshi–Shiga (1988), building on Parshin–Arakelov.** Let S be a Riemann surface of finite type, and let M_{h,m} be a fine moduli manifold with 2h − 2 + m > 0. Each free homotopy class of maps S → M_{h,m} contains only finitely many non-constant holomorphic maps. In the original form: there are finitely many non-isotrivial holomorphic families of type (h,m) over S with given monodromy, and for a fine moduli manifold, families correspond to classifying maps.
- **(MCG)** Every self-homeomorphism of P^1 \ {0,1,∞} is isotopic to the restriction of one of the 12 Möbius or anti-Möbius maps that permute {0,1,∞}. This is the extended mapping class group of S_{0,3}, isomorphic to S_3 × Z/2; see e.g. Farb–Margalit.
- **Liouville-type fact.** A fine moduli manifold M_{h,m} has the bounded domain T_{h,m} as universal cover (Bers). Hence every holomorphic map from P^1, C or C* to M_{h,m} is constant.

### Proof

**Step 1. Constant labels on faces.**
- Δ_G is a product. Since ξ_G : ∏_u M_u → Δ_G is a continuous bijection that is finite and proper, ξ_G^{-1} is continuous. Hence π_v ∘ q is continuous on Φ_{S(b̃)}.
- At each point z̃ of the face, π_v(q(z̃)) = Plumb_c(z̃) for some vertex class c. The coincidence sets C_c = {π_v ∘ q = Plumb_c} are closed, and they cover the face.
- If two plumbing maps agree identically, merge their classes. Otherwise the pairwise coincidence sets {Plumb_c = Plumb_{c'}} are proper analytic subsets. Off them the sets C_c are disjoint and closed, and they cover a connected set (the complement of a proper analytic subset of a connected manifold).
- So a single class works on a dense set, and by continuity on the whole face. Defining v as the global vertex attached to c_b, we get: **π_v ∘ q = Plumb_{c_b} on all of Φ_{S(b̃)}**.
- In the same way, **π_i ∘ q = x_i on all of Φ_{S(β̃)}**. Here the class is the single vertex i, which has no internal edges.

**Step 2. Transported objects.** For small |t|:
- E_t := H_t(E_0) is an irreducible component of closure(V_t) ∩ Δ_G. Indeed, H_t preserves strata, and the irreducible components of a 1-dimensional analytic set are topologically determined: they are the closures of the connected components of the set minus its multi-branch points.
- P_t := H_t(P_0) ∈ Δ_{G'} ∩ closure(E_t) ∩ closure(∂V_t).
- β_t := H_t(β) and b_t := H_t(b) are local branches at P_t of ∂V_t and E_t respectively. A homeomorphism maps branches to branches, since the branches are the closures of the components of a punctured neighbourhood.

**Step 3. Lifts at time t.**
- Fix r_0 ∈ β \ {P_0} and z_0 ∈ b \ {P_0} close to P_0. Put r_t = H_t(r_0) and z_t = H_t(z_0).
- **The lifts stay in the same faces.** Faces of the same type as Φ_{S(b̃)} have images under q that are either equal (if K_0-related) or disjoint. Each image is closed in the type-G locus of q(N_0), because q is proper. The continuous path t ↦ z_t stays in the type-G locus. A connected disc covered by finitely many disjoint closed sets lies in one of them. Hence z_t ∈ q(Φ_{S(b̃)}) for all small t. Pick z̃_t ∈ Φ_{S(b̃)} with q(z̃_t) = z_t. Likewise pick r̃_t ∈ Φ_{S(β̃)}.
- **The lifted branches reach the fibre over P_t.** Every irreducible component of q^{-1}(b_t) ∩ N_0 maps onto the irreducible germ b_t, since q is finite. So the component through z̃_t contains a point P̂^b ∈ O_t := q^{-1}(P_t) ∩ N_0. Off P̂^b this component lies in Φ_{S(b̃)}, because the face type is locally constant on a connected punctured branch. Similarly there is P̂^β ∈ O_t such that the component of q^{-1}(β_t) through r̃_t lies, off P̂^β, in Φ_{S(β̃)}.
- O_t is a single K_0-orbit, so P̂^b = k P̂^β for some k ∈ K_0.

**Step 4. Y_t is read at P̂^β.**
- For points r ∈ β_t \ {P_t}, with lifts r̃ in Φ_{S(β̃)}, Step 1 gives Y_t = π_i(r) = x_i(r̃).
- Letting r̃ → P̂^β gives x_i(P̂^β) = Y_t.
- By the K_0-equivariance in §1, x_{k(i)}(P̂^b) ≅ x_i(P̂^β) = Y_t, up to relabelling of the marked points.

**Step 5. The merged curve F_t is rigid.**
- Ẽ_t, the normalization of E_t, is homeomorphic to Ẽ_0 compatibly with ends: H_t lifts to normalizations, and ends correspond to the branches at the finitely many points of closure(E_t) \ E_t, which is finite by (R1). By (M3), Ẽ_t is a genus-0 surface with 3 punctures, hence biholomorphic to S := P^1 \ {0,1,∞}.
- Choose biholomorphisms ψ_t : S → Ẽ_t. Put f_t := π_v ∘ ν_t ∘ ψ_t : S → M_{h,m}, which is holomorphic. Put g_t := π_v ∘ H_t ∘ ν_0 ∘ ψ_0, which is continuous in (s,t). Then g_t is homotopic to g_0 = f_0.
- With h_t : Ẽ_0 → Ẽ_t the lift of H_t, we have g_t = f_t ∘ φ_t, where φ_t = ψ_t^{-1} h_t ψ_0 is a homeomorphism of S. By (MCG), φ_t is isotopic to one of 12 maps μ. Hence f_t ≃ f_0 ∘ μ^{-1}.
- **f_t is not constant.** Along the branch b_t, π_v = Plumb_{c_b} on the lifted branch, and this tends to Q_t := Plumb_{c_b}(P̂^b). By (M1), c_b contains an edge e with s_e(P̂^b) = 0, so Q_t ∈ ∂M̄_{h,m}. A constant f_t would force Q_t ∈ M_{h,m}, a contradiction.
- **f_t lies in a finite set.** By (IS) and (M4), f_t lies in a finite set Φ of holomorphic maps, independent of t.
- **The closures agree.** Put F_t = π_v(E_t) = f_t(S).
  - closure(F_t) in M̄_{h,m} is an irreducible compact curve. It is the image of the compact curve closure(E_t), lifted through the finite map ξ̄_G, under the proper projection to the v-factor (Remmert).
  - Let T_F = {t : closure(F_t) = F}. These sets are finitely many, pairwise disjoint, and cover the small disc.
  - Each T_F is closed. If t_n → t with closure(F_{t_n}) = F, then for every x ∈ E_0 we have π_v(H_t(x)) = lim π_v(H_{t_n}(x)) ∈ F. So F_t ⊂ F, and by irreducibility closure(F_t) = F.
  - A connected disc is not a disjoint union of finitely many nonempty closed sets. Hence **closure(F_t) = closure(F_0)** for all small t.

**Step 6. Conclusion.**
- Q_t = lim π_v along b_t lies in closure(F_0) ∩ ∂M̄_{h,m}. This is a finite set Ω, since F_0 ⊄ ∂ and closure(F_0) is a compact curve.
- The gluing map ∏_{w∈c_b} U_w → M̄_{h,m}, restricted to the locus s = 0, is finite. So (x_w(P̂^b))_{w∈c_b} lies in a finite set Ω̃, independent of t.
- By (M2), k(i) ∈ c_b. So, by Step 4, Y_t ≅ x_{k(i)}(P̂^b) lies in the finite set Λ ⊂ M_{g_i,n_i} of relabellings of components occurring in Ω̃.
- t ↦ Y_t is continuous (PR-1, step 1). So Y_t is constant for small |t|.
- By PR-1, t ↦ Y_t is holomorphic on Δ, so by the identity theorem Y_t = Y_0 for all t. ∎

**What Theorem M uses beyond PR-1 and P-b.** Only (IS), (MCG) and the standard local structure of M̄_g at a stable curve. It does not use the totally geodesic property of V_0. That property enters only through which V_0 satisfy (M1)–(M5), as in §4.

## 3. A gap in PR-3 Theorem E: hypothesis (M2) is needed
- PR-3's proof of Theorem E (step 5) takes for granted that "the component of P_t at vertex i lies in the merged vertex v" holds for every t because it holds at t = 0. That identification is made in an orbifold chart and is defined only up to Aut(P_t).
- When Aut(P_0) ⊋ Aut(P_t), the transported branch b_t may pass through a *different* lift kP̂ of P_t than β_t does.
- In that case, geometrically, E_t merges a former "twin" component x_{k(i)} of P_t, which at t = 0 was isomorphic to Y_0, instead of the Y_t-component.
- I see no local or topological argument excluding this. Theorem E should therefore carry a hypothesis such as (M2), for example "Aut(P_0) fixes the component Y_0".
- This scenario is also a possible counterexample mechanism, to be checked: a cusp whose symmetry is broken in the family.

## 4. Corollary N: covering constructions from M_{0,5}

**Setting.**
- Φ : M_{0,5} → M_g is a cyclic covering construction, sending (P^1, a_1, …, a_5) to the curve y^d = ∏ (x − a_j)^{k_j}.
- V_0 = Φ(M_{0,5}) is assumed smooth, as the problem requires.
- V_0 is totally geodesic: Teichmüller maps lift to covers, and the lifted map is extremal (standard; cited from memory).
- For abelian covers the admissible cover over a stable 5-pointed tree is unique, so Φ extends to Φ̄ : M̄_{0,5} → M̄_g, sending a stable curve to the stable model of the admissible cover (Harris–Mumford; cited from memory). Then closure(V_0) = Φ̄(M̄_{0,5}).

**Corollary N.** In this setting:
- Suppose that, for some boundary divisor D_{12}, say, with Φ̄(D_{12}°) ⊂ ∂V_0, the constant vertex i is a component Ŷ of the admissible cover lying over the 3-pointed bubble A ∋ a_1, a_2. Call this condition (B).
- Then there is a cusp P_0 = Φ̄(D_{12} ∩ D_{kl}), with {k,l} ⊂ {3,4,5}, at which (M1) and (M3) hold, with E_0 the component containing Φ̄(D_{kl}°).
- Hence, if (M2), (M4) and (M5) also hold at that cusp, Y_t is constant.

*Proof.*

**(a) The lifts.**
- Near the point D_{12} ∩ D_{kl} of M̄_{0,5}, take coordinates (λ_1, λ_2) with D_{12} = {λ_1 = 0} and D_{kl} = {λ_2 = 0}.
- The family of stable models over this polydisc is pulled back from the Kuranishi family by a classifying map κ, by versality.
- Then β̃ := κ{λ_1 = 0} and b̃ := κ{λ_2 = 0} are lifts through the common point κ(0) = P̃_0.

**(b) Monodromy at the cusp.** Over the chain A–B–C at the cusp:
- A carries a_1, a_2 and the node q; B carries a_m, with {m} = {3,4,5} \ {k,l}; C carries a_k, a_l.
- Let σ_3, σ_4, σ_5, σ_q be the monodromies of the main-side cover, the one over the sphere carrying a_3, a_4, a_5, q. Their product is 1.
- An edge of Γ at i corresponds to a node y of Ŷ over q, that is, to a cycle c of σ_q.
- Let W_B be the component over B at y. It is unstable if and only if it is a *bridge*: genus 0, with one preimage of each node. Then W_B, as a cover of B, has sheet set equal to c, and σ_r is a full cycle on c. Riemann–Hurwitz then gives 2·genus(W_B) = |c| − #cycles(σ_m|_c). So W_B is a bridge if and only if c is ⟨σ_q, σ_m⟩-invariant and σ_m|_c = id.
- If W_B is stable, then the node y is an edge of G' from i to W_B. It is smoothed along D_{kl}, where A ∪ B is smoothed. So (M1) holds with c_b ∋ i.

**(c) Some choice of m gives a merge.**
- Suppose, for contradiction, that W_B is a bridge for all three choices of m.
- Then c is invariant under σ_3, σ_4, σ_5, which act trivially on it. So σ_q|_c = (σ_3σ_4σ_5)^{-1}|_c = id, and |c| = 1.
- The main-side component at y is then a degree-1 rational tail with a single special point. It is contracted by stabilization, so y is not an edge of Γ. Contradiction.
- Vertex i has at least one Γ-edge. Otherwise Δ_Γ = M_{g_i,n_i} and ∂V_t would be a point, contradicting dim ∂V_t = 1. So some m gives the merge.

**(d) (M3).**
- Φ̄ maps D̄_{kl} ≅ P^1 onto closure(E_0), so the normalization of closure(E_0) has genus 0.
- Each puncture of Ẽ_0 has a preimage among the 3 special points of D̄_{kl}: D_{kl}° maps into Δ_G, and the map is surjective. Hence Ẽ_0 has at most 3 punctures.
- f_0 is non-constant (Step 5 above). By (M4) and the Liouville-type fact, Ẽ_0 has at least 3 punctures.
- Hence Ẽ_0 has exactly 3 punctures. ∎

**Remark.** Hypothesis (B) excludes the case where the constant factor is a component over the 4-pointed side that happens to be isotrivial. I have not analysed that case.

## 5. Counterexample search: what a counterexample must look like
- By PR-4 Theorem B, a counterexample needs a varying abstract complex structure. By PR-5, it needs a nonzero normal section.
- By Theorem M, at **every** cusp P_0 of ∂V_0 and for every merged boundary curve E_0 through it, at least one of the following must fail:
  - (M2): automorphisms of P_0 move Y_0 out of the merged class;
  - (M3): the merged curve has moduli as a punctured curve;
  - (M4): the merged factor has orbifold points;
  - (M5): Δ_G is a quotient stratum;
  - or no merged curve exists at that cusp (C-merge fails).
- By Corollary N, for cyclic M_{0,5}-constructions with a bubble-type constant factor, the merge always exists and (M3) is automatic. So a counterexample of that type must exploit (M2), (M4) or (M5).
- The PR-6 converse (log vector fields) remains the only general source of counterexamples. I did not find a totally geodesic V_0 carrying such a field.

## 6. Proved / conditional / open
- **Proved, modulo the cited results (IS), (MCG), the standard orbifold charts of M̄_g, PR-1 and P-b:** Theorem M.
- **Proved, modulo admissible-cover theory (cited):** Corollary N, parts (M1) and (M3).
- **Flagged:** the identification gap in PR-3 Theorem E, which needs an (M2)-type hypothesis.
- **Open:**
  1. MS4 in general.
  2. Whether (M2), (M4) and (M5) can be removed. For (M4), the issue is that maps from S into the coarse space through orbifold points may deform, since cone points can move.
  3. The case where the constant factor lies over the non-bubble side.
  4. Whether any totally geodesic V_0 admits the PR-6 flow, which would give a counterexample.
  5. Whether the symmetry-breaking mechanism of §3 can actually produce a counterexample.

=== END OF ANSWER round5_q8 ===
