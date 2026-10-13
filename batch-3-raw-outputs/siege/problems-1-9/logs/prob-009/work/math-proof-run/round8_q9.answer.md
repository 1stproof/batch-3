# round8_q9 — attempt on (Rig-all)

## Status / plan (written first; final status in §7)
Plan:
1. Prove that the central fibre of the lifted family is reduced (Lemma Red). This uses only (R1)/(R2) and the product case.
2. Use Lemma Red to show that the degree of pr_v is constant in homology (Lemma Deg). In the *birational case*, i.e. when pr_v : E_0 → K_0 is generically injective, deduce that image-rigidity for the Teichmüller vertex v makes the whole normalized source family trivial (Cor. B).
3. Show that, under (Rig-v), punctures lying over v-cusps cannot move (Lemma P).
4. Prove rigidity of the other vertices in the birational case under a fixed-orbifold condition (Prop. F).
5. Give an explicit family of maps (Example Z). It satisfies every piece-level property that is available: constant Teichmüller vertex, trivial source family, fixed punctures, no type jump, (O) for v. Yet the joint image K_t ⊂ M̄_v × M̄_u varies with t. So (Rig-all) in its joint-image form cannot be proved from piece data alone. This is not a counterexample to the problem, since I have not checked that the family can be realized by an admissible V_t.

Statement now attempted: steps 1–4. The product case is assumed throughout: ξ_G is injective on ∏M_w.

## 1. Setting
Readings (R1), (R2) are as in the task. H_0 = id.

G is a product-type stable graph, and E_0 is a piece, i.e. a 1-dimensional irreducible component of closure(V_0) ∩ Δ_G, identified with its lift in ∏_w M_w. Put E_t := H_t(E_0).

W := 𝓦^{(a)} ⊂ ∏_w M̄_w × Δ is the irreducible 2-dimensional analytic set of Lemma R0. By R7-5 §1.2 (L1, product case), W_t = closure(E_t) as sets for every t, and W → Δ is proper.

For a vertex w, put K^w_t := pr_w(W_t) = closure of pr_w(E_t). It is a point or an irreducible curve (Remmert).

v is a Teichmüller vertex of E_0, i.e. (H_0) of PR-E holds. Let ι : K̃ → K_0 := K^v_0 be the normalization of the closed Teichmüller curve.

**(Rig-v)** denotes the image-level Lemma R for v: K^v_t = K_0 for all t. It is proved under (O) for v (PR-D, PR-E). By Cor. G2 of R7-7 it also holds unless 0 is a type-jump time with no Teichmüller generic member; that case is open.

## 2. Lemma Red (the central fibre is reduced)

**Lemma Red.** Regard t as a holomorphic function on W. Its divisor over 0 is the reduced cycle [closure(E_0)], with multiplicity 1. Consequently the fibre cycles [W_t] are all homologous to [closure(E_0)] in H_2(∏_w M̄_w; ℤ).

*Proof.*

**Setup.** W_0 = closure(E_0) as a set, and it is irreducible. So the divisor of t over 0 is m·[closure(E_0)] for some integer m ≥ 1. We must show m = 1.

- Choose x ∈ E_0 such that closure(E_0) is a smooth curve germ at x. Choose x also generic in the following sense: it is not a multi-branch point of the 1-dimensional part of closure(V_0) ∩ Δ_G, and not a puncture.
- Embed a neighbourhood of x in the coarse analytic space ∏M̄_w into some ℂ^N. Some linear coordinate s restricts to a local coordinate on the smooth germ (closure(E_0), x). Put s(x) = 0.
- Near x, Ψ := (s, t) : W → ℂ² has Ψ^{-1}(0,0) = {x}. So Ψ is finite at x.

**Step 1 (m = local degree μ of Ψ).** Let μ be the local degree of Ψ at x: the number of preimages near x of a generic point near (0,0). By the projection formula for the finite map Ψ, Ψ_*(div t near x) = Ψ_*(m·[closure E_0]) = m·deg(s|_{closure E_0})·[t = 0] = m·[t = 0]. Also Ψ_*Ψ^*[t = 0] = μ·[t = 0]. Hence m = μ.

**Step 2 (counting via H).**
- Fix r > 0 small. Let B := {y ∈ closure(E_0) : |s(y)| ≤ r} be a closed disc around x.
- Since H is a homeomorphism of closure(V_0) × Δ onto closure(𝒱), H_t → id and H_t^{-1} → id uniformly near x as t → 0. In the product case lifting through ξ_G is a homeomorphism near x, so we may work upstairs.
- Hence there are a neighbourhood N of x and ε > 0 with the following properties for every |t| < ε:
  - (a) H_t(B) ⊂ N.
  - (b) |s(H_t(y))| > r/2 for all y ∈ ∂B.
  - (c) every y ∈ W_t ∩ N with |s(y)| < r/2 lies in H_t(B).
  - For (c): if y ∈ W_t is close to x, then H_t^{-1}(y) is close to x, so it lies in B.
- Fix c with |c| < r/2, and t with 0 < |t| < ε. By (a) and (c), the solutions of s = c on W_t ∩ N are exactly the solutions on the topological disc H_t(B).
- H_t(B) is a disc, so it contains no multi-branch point of the curve W_t. Hence it is a topological 2-manifold that is oriented by the complex structure at its smooth points.
- **Holomorphic count.** For generic (c, t), s|_{H_t(B)} has μ simple solutions, each of local degree +1.
- **Topological count.** The map s ∘ H_t : B → ℂ has topological degree over c equal to ±μ. The sign is that of the homeomorphism H_t : B → H_t(B) with respect to the complex orientations.
- **Homotopy.** τ ↦ s ∘ H_{τt}, τ ∈ [0,1], is a homotopy from s|_B to s ∘ H_t. By (b) it never takes the value c on ∂B. So the degree over c is that of s|_B, which is 1, because s|_B is a homeomorphism onto the disc |s| ≤ r.
- Hence ±μ = 1, so μ = 1 and m = 1.

**Homology.** The fibre cycles [W_t] = div(t − t_0) of the proper map t : W → Δ are homologous in W, since Δ is connected. This is the standard fact that fibre cycles of a proper flat family over a connected base are homologous. So [W_t] is homologous to [W_0] = [closure E_0] in ∏M̄_w. ∎

*Remark.* Only (R2), continuity and the product case are used. The proof is a topological degree argument. It is the "degree" counterpart of the unibranchness of the central fibre (Lemma N in the chain).

## 3. Lemma Deg and the birational transfer

**Lemma Deg.** Let w be a vertex with K^w_0 a curve. Let d_t be the degree of pr_w : closure(E_t) → K^w_t when K^w_t is a curve, and put d_t := 0 when it is a point. Then d_t·[K^w_t] = d_0·[K^w_0] in H_2(M̄_w; ℚ). In particular, if K^w_t = K^w_0, then d_t = d_0.

*Proof.*
- Take pr_{w*} of the homology relation in Lemma Red: pr_{w*}[closure E_t] = d_t·[K^w_t] as cycles.
- M̄_w is projective (Knudsen–Mumford; from memory). So an ample class pairs positively with the curve K^w_0, and [K^w_0] ≠ 0 in H_2(M̄_w; ℚ).
- If K^w_t = K^w_0, we may cancel [K^w_0] and get d_t = d_0. ∎

(Note: by L1, K^w_t is a point for one t iff it is a point for all t. So the case d_t = 0 does not actually occur here.)

**Corollary B (birational case).** Assume (Rig-v), and that pr_v : E_0 → K_0 is generically injective (d_0 = 1). Let n : 𝓦^ν → W be the normalization. Then:
- (a) (lift of pr_v ∘ n, t) : 𝓦^ν → K̃ × Δ is a biholomorphism over Δ;
- (b) under this identification the v-coordinate is ι for every t: pr_v ∘ n(x, t) = ι(x);
- (c) there are holomorphic maps φ^u : K̃ × Δ → M̄_u, one for each vertex u, with ν_t = (φ^u_t)_u, where φ^v_t = ι.

In particular, (O) holds for v trivially, with A_t = id. For this piece, (Rig-all) is equivalent to φ^u_t = φ^u_0 for all non-constant u. The joint image is the image of K̃ under x ↦ (ι(x), φ^u_t(x)), and ι is generically injective, so equality of joint images forces equality of maps.

*Proof.*
- **Degree.** By Lemma Deg and (Rig-v), d_t = 1 for all t.
- **The map exists.** pr_v ∘ n maps 𝓦^ν into K_0, by (Rig-v). 𝓦^ν is normal and no component of it maps into Sing(K_0) × Δ. By the universal property of normalization, (pr_v ∘ n, t) factors through the normalization K̃ × Δ of K_0 × Δ.
- **The map is finite.** It is proper, since 𝓦^ν → Δ is proper. Its fibres are finite, since each W_t maps finitely onto K_0.
- **The map is bimeromorphic.** For generic t, its degree is d_t = 1.
- **Conclusion.** A finite bimeromorphic holomorphic map onto a normal space is biholomorphic. This is the analytic Zariski main theorem; cited from memory. This gives (a). (b) and (c) follow by composing with pr_u ∘ n. ∎

## 4. Lemma P (whether a puncture degenerates at v is constant in t)

**Lemma P0 (general product case).** Let Π be an irreducible component of the puncture locus 𝓟 := n^{-1}(∂(∏M̄_w) × Δ) ⊂ 𝓦^ν, and let w be a vertex. Then either pr_w ∘ n(Π) ⊂ ∂M̄_w, or pr_w ∘ n(Π) ∩ ∂M̄_w = ∅.

*Proof.*

**Π is horizontal and surjects onto Δ.**
- 𝓟 contains no whole fibre, since E_t ⊂ ∏M_w. So 𝓟 is a curve that is proper and finite over Δ.
- Hence each component Π surjects onto Δ, by Remmert's proper mapping theorem and irreducibility.

**The transported point is the same along Π.**
- For y ∈ ∏M̄_w, the stable curve ξ̄_G(y) has |E(G)| + Σ_w δ(y_w) nodes, where δ(y_w) is the number of nodes of the curve y_w.
- Let F_t := closure(E_t) \ E_t ⊂ M̄_g be the finite set of puncture points. By (R2), F_t = H_t(F_0), and H_t preserves strata.
- So the continuous map t ↦ ξ̄_G(n(π(t))), along a local continuous branch π(t) of Π, takes values in H_t(F_0).
- For fixed t the points H_t(f), f ∈ F_0, are distinct, and each depends continuously on t. A continuous selection from finitely many distinct continuous functions is locally one of them. So ξ̄_G(n(π(t))) = H_t(f) for one fixed f ∈ F_0.
- Hence the total number of nodes N(t) := |E(G)| + Σ_w δ(pr_w n π(t)) is independent of t along Π.

**Semicontinuity forces the dichotomy.**
- The sets {δ ≥ k} ⊂ M̄_w are closed. So if π(t) → π(t_1), then δ(pr_w n π(t_1)) ≥ δ(pr_w n π(t)) for each vertex w and all t near t_1.
- N(t) is constant along Π, so all these inequalities are equalities.
- In particular, if pr_w n π(t_1) ∈ ∂M̄_w, i.e. δ ≥ 1, then pr_w n π(t) ∈ ∂M̄_w for all t near t_1. So the set where pr_w n ∈ ∂M̄_w is open in Π.
- That set is also closed and analytic, and Π is irreducible, hence connected. So it is empty or all of Π. ∎

**Lemma P (birational case).** Under the hypotheses of Cor. B, put Cusp := ι^{-1}(∂M̄_v), a finite subset of K̃. Every component of 𝓟 ⊂ K̃ × Δ is either:
- {c} × Δ for some c ∈ Cusp, or
- disjoint from Cusp × Δ.

In particular:
- the punctures of E_t at which v degenerates are the fixed points c ∈ Cusp ∩ 𝓟_0, and their v-values ι(c) are independent of t;
- if every puncture of E_0 is a v-degenerate puncture, then 𝓟 = 𝓟_0 × Δ. That is, the punctures of E_t, as points of the fixed curve K̃, do not move.

*Proof.* By Cor. B, pr_v ∘ n(x, t) = ι(x). By Lemma P0 a component Π either lies in Cusp × Δ, or misses it. In the first case Π is a component of {c} × Δ, which is irreducible, so Π = {c} × Δ. ∎

*Remark.* For the problem itself, Lemma P0 says that "which vertices degenerate at a given puncture" is a deformation invariant. This uses only (R2) and node counting.

## 5. Prop. F (rigidity of the other vertices in the birational case, fixed orbifold data)

Fix a non-constant vertex u. By L1′ applied with arbitrary base time (its proof is symmetric in t), φ^u_t is non-constant for every t. Let M′ := M_u[N] → M_u (N ≥ 3) be the level cover. M′ is a complex manifold and a fine moduli space. Let 𝓢 be the normalization of (K̃ × Δ \ 𝓟) ×_{M_u} M′. It is a finite map onto K̃ × Δ \ 𝓟, and it is branched along an analytic set R̂ of pure dimension 1, by Zariski–Nagata purity: 𝓢 is normal and the base is smooth.

**(Σ-fixed for u).** There is a finite set Σ_u ⊂ K̃ with R̂ ∪ 𝓟 ⊂ Σ_u × Δ.

**Prop. F.** Assume (Rig-v), d_0 = 1 (Cor. B), and (Σ-fixed) for u. Then φ^u_t = φ^u_0 for all t.

*Proof.*

**The cover is a product.**
- Over B° := (K̃ \ Σ_u) × Δ, the map 𝓢 → B° is finite and unbranched onto a manifold, with normal source. So it is a finite covering map.
- B° deformation retracts onto (K̃ \ Σ_u) × {0}. Coverings are classified by π_1 and are homotopy invariant. So each connected component of 𝓢|_{B°} is isomorphic over B° to S° × Δ, where S° → K̃ \ Σ_u is a connected finite covering.
- In particular S° is a Riemann surface of finite type, and is fixed.

**The lifted maps.**
- The fibre product gives a holomorphic lift φ̂ : S° × Δ → M′ of φ^u.
- φ̂_t is non-constant for each t, because φ^u_t is.
- t ↦ φ̂_t is a continuous family of maps from the fixed surface S°, so all φ̂_t are homotopic.

**Finiteness.** *Cited from memory: Imayoshi–Shiga, "A finiteness theorem for holomorphic families of Riemann surfaces", MSRI Publ. 11, 1988.* For a finite-type Riemann surface S° and a torsion-free finite-index Γ ⊂ Mod_{h,m} with 2h − 2 + m > 0, a homotopy class of maps S° → T_{h,m}/Γ contains only finitely many non-constant holomorphic maps. So φ̂_t ∈ {ψ_1, …, ψ_r} for every t.

**Constancy.**
- Each set {t : φ̂_t = ψ_j} is closed, by pointwise continuity in t.
- These finitely many disjoint closed sets cover the connected Δ, so only one is nonempty, and φ̂_t = φ̂_0.
- Projecting to M_u gives φ^u_t = φ^u_0 on K̃ \ Σ_u. By continuity this holds on all of K̃. ∎

**Theorem B (what is now proved for (Rig-all)).** Let E_0 be a product-type piece with Teichmüller vertex v. Assume:
- (Rig-v) for v; this holds e.g. under (O) for v, or under Cor. G2's condition;
- pr_v|_{E_0} is generically injective;
- (Σ-fixed) holds for every non-constant vertex u.

Then ν_t = ν_0 ∘ (identification of Cor. B) for all t. Hence the joint image K_t ⊂ ∏_{u∈M} M̄_u is independent of t, and so are all puncture values. So (Rig-all) holds for E_0.

**Sufficient conditions for (Σ-fixed) for u.** Suppose:
- (1) every puncture of E_0 is v-degenerate; then 𝓟 = 𝓟_0 × Δ by Lemma P;
- (2) for every t, φ^u_t(K̃ \ 𝓟_t) avoids the locus of M_u where the automorphism group is larger than the generic one.

Then R̂ = ∅ and (Σ-fixed) holds with Σ_u := 𝓟_0.

Condition (1) is what one expects for boundary pieces of a totally geodesic V_0. Heuristically, all cylinders pinch only at the cusps of the SL_2ℝ-orbit. This is a sketch, not proved here.

## 6. Example Z: the joint-image form of (Rig-all) does not follow from piece data

**Data** (the Teichmüller curve is cited from memory, as in Prop. X of R7-7).
- **Vertex v.** M_v = M_{2,1}. ι : ℂ → M_{2,1} is the closed Teichmüller curve of the double regular pentagon (Veech group Δ(2,5,∞)), in the coarse coordinate z on C_V ≅ ℂ:
  - an orbifold point of order 2 at z = 0;
  - an orbifold point of order 5 at z = 1;
  - a cusp at z = ∞, so ι(∞) ∈ ∂M̄_{2,1}.

  ι is generically injective.
- **Vertex u.** M_u = M_{1,1}. Its coarse space is the j-line ℂ, with orbifold points j = 0 (order 3) and j = 1728 (order 2), and ∂M̄_{1,1} = {∞}.
- **The stratum.** G is the genus-3 graph with a genus-2 vertex v and a genus-1 vertex u joined by one edge. It has no automorphisms, and Δ_G ≅ M_{2,1} × M_{1,1} is of product type.
- **The family.** For |t| < ε put J_t(z) := z³ + z + t z² and

  E_t := {(ι(z), J_t(z)) : z ∈ ℂ} ⊂ M_{2,1} × M_{1,1},

  normalized by K̃ = ℙ¹ through z ↦ (ι(z), J_t(z)).

**Properties (proved).**
- (a) **Trivial source, one fixed puncture.** The source family is the trivial family ℙ¹ × Δ. The map depends holomorphically on (z, t). Its only puncture is z = ∞, with constant value (ι(∞), ∞). So the family is smoothly trivial and its puncture is v-degenerate. Condition (1) of §5 holds, and the conclusion of Lemma P holds.
- (b) **The v-coordinate is ι for all t.** So (H_0) holds for v, (O) holds for v with A_t = id, (Rig-v) holds, and d_0 = 1.
- (c) **No type jump of the joint minimal orbifold for small t.** J_t(z) = z(z² + tz + 1).
  - Its zeros are z = 0 (fixed) and the two roots of z² + tz + 1 (near ±i, moving). For small t they are simple, since J_0′(0) = 1 and J_0′(±i) = −2.
  - The three roots of J_t = 1728 are simple and move. The discriminant of z³ + z − c is −4 − 27c² ≠ 0 at c = 1728.
  - None of these points meets z = 1 or another of them for small t, because J_0(1) = 2 ∉ {0, 1728}.
  - So the joint orbifold is ℙ¹ with a cusp at ∞ and cone points of orders 6 (at z = 0, lcm(2,3)), 3, 3, 2, 2, 2 and 5. Its type is constant, but the cone points of orders 3 and 2 move. Hence (Σ-fixed) fails for u.
  - (O_G) holds in the sense of a type-preserving transport with constant monodromy (by continuity). But (H_0) fails for the *joint* orbifold: the lift of ι from the joint orbifold's universal cover is a branched map, not an isometry. So L2 (R7-8) does not apply. This is consistent with L2.
- (d) **The joint image varies.** Suppose closure(E_t) = closure(E_{t′}).
  - For generic z, ι^{-1}(ι(z)) = {z}. So (ι(z), J_t(z)) ∈ E_{t′} forces J_t(z) = J_{t′}(z).
  - Then t z² = t′ z² for generic z, so t = t′.
  - Hence the joint image curves K_t ⊂ M̄_v × M̄_u are pairwise distinct. The conclusion of (Rig-all) fails for this family of pieces.
- (e) **The single-vertex images and the puncture values are constant.** K^u_t = M̄_{1,1}, because J_t is onto. The only puncture value is (ι(∞), ∞).

**What Example Z shows, and what it does not.**
- It is a family of *maps* (pieces) only. I have NOT checked:
  - that E_0 is a boundary piece of a totally geodesic surface V_0 (its u-coordinate z³ + z is arbitrary);
  - that the deformation extends to a family V_t satisfying (i) and (ii).

  So it is not a counterexample to (Rig-all) or to the problem.
- It does show that **no argument using only the piece family** can prove the joint-image form of (Rig-all). That covers source triviality, the Teichmüller anchor, (O) for v, puncture behaviour and orbifold type constancy. Theorem B's hypothesis (Σ-fixed) cannot simply be dropped.
- The mechanism is general. Let E_0 be any product-type piece with a non-constant vertex u of type (1,1) and pr_v birational. Then J_t := φ^u_0 + t·g, with g a rational function on K̃ whose poles lie among those of φ^u_0 with smaller order, deforms the piece with fixed punctures and varying joint image. Any proof must therefore use the global existence of V_t (conditions (i), (ii) on all strata, including the 2-dimensional open part), or the totally geodesic structure at t = 0 combined with such global input.
- One might hope to retreat to the **weak form (Rig-w)**: the puncture values of the non-constant vertices lie in a t-independent finite set. The task states that this consequence is what the reduction to MS8 uses. Example Z satisfies (Rig-w), but Example Z′ shows that (Rig-w) also fails at the piece level.

**Example Z′ ((Rig-w) also fails for families of pieces).**
- Let ι : K̃ → M̄_{2,1} be any closed Teichmüller curve whose normalization K̃ has at least two cusps c_1 ≠ c_2, i.e. points of ι^{-1}(∂M̄_{2,1}). Arithmetic Teichmüller curves of L-shaped square-tiled surfaces in H(2) are standard examples; cited from memory.
- By Riemann–Roch choose a non-constant meromorphic function J_0 on K̃ whose only pole is at c_1. Put J_t := J_0 + t, and let E_t be the image of z ↦ (ι(z), J_t(z)) in M_{2,1} × M_{1,1} (same stratum G as in Example Z).
- **Fixed data.** The source family is trivial, and the v-coordinate is constant in t. The punctures are the cusps of K̃, and are fixed. Every puncture is v-degenerate, so Lemma P's hypothesis holds. (Rig-v) holds and d_0 = 1.
- **Moving puncture value.** At the puncture c_2 the vertex u is *not* degenerate, and its value J_0(c_2) + t ∈ M_{1,1} moves with t.
- **Translation to M̄_g.** The deeper boundary point H_t(P_0) ∈ Δ_{G′} has a genus-1 component whose j-invariant varies with t. This is exactly the phenomenon the problem asks to exclude, now for a non-constant vertex. Again, realizability by an admissible V_t is unchecked.

**Consequence for the chain.** Neither (Rig-all) nor (Rig-w) can be derived from properties of the individual piece families: (R2) on the piece, the Teichmüller anchor, (O) for v, puncture rigidity, Lemma P0. A proof must use the global family V_t, e.g.:
- the 2-dimensional open part and its compatibility (ii) with all strata;
- or the totally geodesic structure at t = 0 in a way that propagates to t ≠ 0. That is, at t = 0, φ^u_0 must be shown to be constrained by V_0, and the constraint must be shown to persist.

The same is true of the problem itself: with u constant, Y_t := j_0 + t is a piece-level "counterexample" in the same sense. So (Rig) is not an easier intermediate statement than the problem at the level of piece data.

## 7. Final status

**Proved** (product-type strata, readings (R1)/(R2); literature cited from memory as indicated):
- **Lemma Red.** The central fibre of the lifted 2-dimensional family W is reduced: div(t)|_0 = [closure E_0]. So all fibre cycles are homologous to [closure E_0]. The proof is a topological degree argument from (R2).
- **Lemma Deg.** d_t·[K^w_t] = d_0·[K^w_0]. Under image constancy the degree d_t of pr_w is constant.
- **Cor. B.** If (Rig-v) holds and pr_v|_{E_0} is birational, then the normalized family is K̃ × Δ, the v-map is ι for all t, and (O) for v holds with A_t = id. This uses the analytic Zariski main theorem, cited.
- **Lemma P0.** For every component of the puncture locus and every vertex w, w is degenerate along the whole component or nowhere on it. The proof is node counting plus stratum preservation by H.
- **Lemma P.** In the birational case, v-degenerate punctures are fixed points of K̃ with fixed v-values. If all punctures at t = 0 are v-degenerate, no puncture moves.
- **Prop. F / Theorem B.** In the birational case, (Rig-v) together with (Σ-fixed) for every non-constant u gives ν_t ≡ ν_0, hence (Rig-all) for the piece. This uses Imayoshi–Shiga finiteness, cited. Sufficient conditions are: all punctures v-degenerate, and the u-maps avoiding the extra-automorphism locus of M_u.
- **Examples Z and Z′.** Explicit holomorphic families of pieces with:
  - a constant Teichmüller vertex, trivial source family and fixed punctures;
  - in Z, no orbifold type jump and (O) for v;
  - nevertheless, a varying joint image (Z) and a varying interior puncture value (Z′).

  So (Rig-all), and even its weak form (Rig-w), cannot be proved from piece-level data. These are not counterexamples to (Rig-all) or to the problem, because realizability by an admissible V_t is unchecked.

**Not proved.** (Rig-all) in general. In particular:
- the non-birational case (d_0 > 1, as in Prop. X);
- (Rig-v) at a type-jump time (J1 ∧ J2 of R7-7);
- non-constant vertices hitting orbifold points of M_u at moving points;
- punctures that are not v-degenerate.

**Sketched only.** That for a totally geodesic V_0 all punctures of a piece are v-degenerate (§5, condition (1)).

**Open questions.**
- (Q1) Can Examples Z/Z′, or the problem's own analogue Y_t = j_0 + t, be realized as boundary pieces of an admissible family V_t deforming a totally geodesic V_0? If yes, (Rig-all) and (Rig-w) are false, and the problem's claim would be in doubt. If no, the obstruction is global (conditions (i), (ii) and the 2-dimensional open part), and identifying it is the real content of the problem.
- (Q2) Is a 2-dimensional totally geodesic V_0 ⊂ M_g rigid as a subvariety, i.e. has no non-trivial deformations V_t satisfying (i), (ii)? This would make the problem vacuous-true.
- (Q3) The non-birational case of Theorem B, i.e. FAC of R7-7 given (Rig-v).
- (Q4) (Rig-v) at type-jump times (Q1′ of R7-7).

=== END OF ANSWER round8_q9 ===

