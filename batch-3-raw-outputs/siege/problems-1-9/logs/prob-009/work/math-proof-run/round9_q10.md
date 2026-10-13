kind: attempt
Open question attempted: ledger entry 13 / open gap E, rigidity of V_0 itself. This route is set aside, not refuted, and the main line does not descend from it. Show that a smooth closed 2-dimensional totally geodesic subvariety V_0 ⊂ M_g admits no non-trivial deformation V_t satisfying the problem's hypotheses (i), (ii), in readings (R1), (R2). Either version settles the problem's claim at once:
- closure(V_t) = closure(V_0) for |t| small, and then for all t by holomorphy of t ↦ Y_t;
- or every V_t is totally geodesic, and then countability of totally geodesic subvarieties gives the same.

## Task
Prove one of the following, for every smooth closed 2-dimensional totally geodesic V_0 ⊂ M_g and every family V_t as in the problem (readings (R1), (R2) below):
- **(D1)** first-order rigidity at t = 0: the Zariski tangent space of the Douady space of a smooth level cover M̂ → M̄_g at the flat limit of p^{-1}(closure(V_0)) vanishes. When the flat limit is reduced, this is H^0(p^{-1} closure V_0, N) = 0 for the normal sheaf N.
- **(D2)** persistence: every V_t is totally geodesic for the Teichmüller metric.
- **(D3)** any other argument giving closure(V_t) = closure(V_0) for small |t|.

Alternatively, exhibit a non-trivial admissible deformation of some smooth closed totally geodesic surface, every check written out. This would show the route is dead, NOT that the problem's claim fails.

**Facts already established** (in earlier answer files; statements and proofs below where used):
- **Proposition A (round4_q8 §A).** (D1) implies the claim (Douady theory).
- **Theorem B (round4_q9).** If the V_t are biholomorphic to V_0 compatibly with the trivialization, then V_t = V_0. This uses Imayoshi–Shiga rigidity of homotopic holomorphic maps from a finite-type source into M_g.
- **(entry 22).** Countably many isomorphism classes of V_t's level-cover components suffice.
- **(round5_q7 §3).** Every holomorphic logarithmic vector field near closure(V_0) is tangent to V_0. So any non-trivial deformation must change the complex structure of V_t.
- **(entry 5).** If every V_t is totally geodesic, the claim follows. Totally geodesic subvarieties are countable: Wright's correspondence with GL(2,R)-orbit closures and Eskin–Mirzakhani–Mohammadi, cited from memory.
- **Theorem TV (round8_q10).** Every boundary piece of closure(V_0) has a vertex projecting as a proper orbifold covering onto a Teichmüller curve.
- **Teichmüller-geometric structure (round8_q6 §4).** Near a boundary point, the Teichmüller norm on T_X V_0 tends to a sup-norm over the vertex factors.

**Suggested approaches** (choose, combine, or replace; say which):
1. **(D1) by a vanishing theorem.** A holomorphic section of the normal sheaf is an infinitesimal deformation of V_0 as a subvariety. Total geodesy says that the Teichmüller discs tangent to V_0 stay in V_0. Kobayashi-hyperbolicity / Schwarz–Pick-type arguments for a family of complex geodesics might force such a section to vanish:
   - differentiate the family of Teichmüller discs D_q (q ∈ Q_V(X)) along a normal deformation;
   - use the uniqueness of complex geodesics in T_g and the fact that holomorphic maps 𝔻 → T_g that are isometric at one point are Teichmüller discs (Royden; the Kobayashi–Teichmüller equality);
   - mind the boundary: N must be controlled at the boundary of closure(V_0), using the log structure, and (R2) for the deformation.
2. **(D2) via Hodge theory, modelled on Möller's rigidity of Teichmüller curves** (round4_q8 §D, steps (α), (β), (γ)):
   - the rank-4 tautological sub-VHS persists if its isotypic multiplicity is one;
   - maximality of its Higgs field is detected by a topological (Toledo-type) invariant constant in t;
   - a characterisation: maximal Higgs together with the zero conditions implies totally geodesic.
   Each of (α), (β), (γ) is open. Settle them, or show precisely which fails.
3. **Induction from the boundary.** Use Theorem TV and the closure structure: the boundary curves of closure(V_0) are rigid at the level of their Teichmüller vertices under (O) (Lemma R*). Show that a deformation of V_0 fixing its boundary "to first order" is trivial, e.g. by a maximum principle for sections of N vanishing along the boundary.

Results only for special V_0 (for instance covering constructions) do not settle the route; report them, labelled partial, if that is all you find. Begin with a plan/status line and end with: proved / not proved / open.

## Readings of the problem's hypotheses (adopted throughout; state them in any proof)
- (R1) closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t) (closures in M̄_g).
- (R2) There is a homeomorphism H: closure(V_0) × Δ → closure(𝒱) over Δ with the following properties:
  - it is smooth on V_0 × Δ;
  - it maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum Δ_G, including the open stratum M_g.
  - Write H_t = H(·,t); one may assume H_0 = id.
  - This is our formalisation of "smoothly trivial" together with (i) and (ii). It is the coarse reading: H_t need not preserve automorphism groups of boundary points.
- Notation:
  - B_t := closure(V_t) \ V_t.
  - A "Y_t-copy" of a stable curve is an irreducible component which, with its special points (preimages of nodes and marked points) in some order, is isomorphic to Y_t as an n_i-pointed curve.

## Prior results (verbatim from earlier answer files; re-check what you use)

### round4_q8 §0–§D (verbatim): infinitesimal rigidity suffices; the Hodge step and its limits; the missing lemma and the Möller-type route
## §0. Re-check of P-a Lemma 1 (holomorphy of t ↦ Y_t), with a repair
As written, the properness claim in P-a is not quite right. A sequence in ∂V_{t_n} can leave Δ_Γ into deeper strata even when its π_i-images converge. Here is the repair.
- Let ξ: ∏_j M̄_{g_j,n_j} → M̄_g be the gluing map. Its restriction to ∏ M_{g_j,n_j} is the isomorphism onto Δ_Γ that is assumed in the problem.
- Let S ⊂ ∏_j M̄_{g_j,n_j} × Δ be the closure of (ξ × id)^{-1}(closure(𝒱)) ∩ (∏_j M_{g_j,n_j} × Δ).
  - S is analytic: (ξ×id)^{-1}(closure 𝒱) is analytic and closed, the open stratum part is open in it, and the closure of an open subset of an analytic set is a union of irreducible components.
  - S is proper over Δ.
- π_i extends to the projection π̄_i onto M̄_{g_i,n_i}. On S_t the map π̄_i is identically Y_t: it equals Y_t on the dense subset ∂V_t and is continuous.
- By Remmert's proper mapping theorem (cited from memory), (π̄_i × id)(S) is an analytic subset of M̄_{g_i,n_i} × Δ, and it is the graph {(Y_t, t)}. This is a 1-dimensional analytic set mapping bijectively and properly onto Δ.
- Its normalization maps bijectively and holomorphically onto the smooth disc Δ, so it is biholomorphic to Δ. Hence t ↦ Y_t is holomorphic.
- Consequently, if Y is constant on a non-empty open subset of Δ, it is constant on Δ (identity theorem).

## §A. Infinitesimal rigidity at t = 0 suffices for all t
**Setting.**
- Let p: M̂ → M̄_g be a finite Galois cover by a smooth projective variety, with group G. Such covers exist via level structures (Looijenga; Boggi–Pikaart; cited from memory).
- Let 𝒱̂ be the closure in M̂ × Δ of (p × id)^{-1}(𝒱), with its reduced structure.
- Every irreducible component of 𝒱̂ dominates Δ. Indeed, φ: 𝒱 → Δ is a submersion, every component of (p×id)^{-1}(𝒱) has 2-dimensional fibres over every t, and taking closure adds no component.
- So t is a non-zero-divisor on O_{𝒱̂}, and 𝒱̂ is flat over Δ. Let Ẑ_t be its scheme-theoretic fibre. Ẑ_t is a compact subspace of M̂, and its support is p^{-1}(closure V_t), using (R1) and the fact that p is finite and open.

**Proposition A.** Suppose the Zariski tangent space of the Douady space D(M̂) at [Ẑ_0] vanishes, i.e.
  Hom_{O_{Ẑ_0}}(I/I², O_{Ẑ_0}) = 0, where I is the ideal of Ẑ_0.
Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. Ẑ is a flat family of compact subspaces of M̂ over Δ. By the universal property of the Douady space (Douady, cited from memory) it is classified by a holomorphic map τ: Δ → D(M̂) with τ(t) = [Ẑ_t].
2. Let m be the maximal ideal of the local ring of D(M̂) at [Ẑ_0]. That local ring is a noetherian analytic algebra, and the Zariski tangent space is (m/m²)^∨. If this vanishes then m = m², so m = 0 by Nakayama. Hence the germ (D(M̂), [Ẑ_0]) is a reduced point.
3. Therefore τ is constant near 0. So Ẑ_t = Ẑ_0 for |t| < ε, and hence closure V_t = p(supp Ẑ_t) = closure V_0.
4. So ∂V_t = ∂V_0 and Y_t = Y_0 for |t| < ε. By §0, Y_t = Y_0 for all t. ∎

**Remarks.**
- If Ẑ_0 is reduced, i.e. equals p^{-1}(closure V_0) (a natural strengthening of (R1)), the hypothesis reads H^0(p^{-1} closure V_0, N) = 0, where N is the normal sheaf.
- This is a condition at t = 0 only, where V_0 is totally geodesic and all its structure (the orbit closure, the rank-4 sub-VHS W) is available.
- The point is that rigidity of the *whole* germ is first-order checkable. Rigidity of the single function Y on the germ is not, which is the t²v issue raised in the task.
- I have not proved the vanishing. It is a form of the missing lemma (§D).

## §B. The proposed Hodge step: what it is and why it cannot close the gap by itself

### B.1 The claim is equivalent to the conclusion
- Suppose g_i ≥ 1. The limiting mixed Hodge structure along ∂V_t contains in Gr^W_1 the polarized summand H^1(Ỹ_t). Here Ỹ_t is the compact curve underlying Y_t, and the summand is constant along ∂V_t.
- By Torelli (cited from memory), the polarized H^1(Ỹ_t) determines Ỹ_t up to isomorphism.
- The n_i special points (marked points and node branches) are recorded only in the extension data of the LMHS. Roughly, these are the classes in Ext(Gr^W_2, Gr^W_1), whose components on J(Ỹ_t) are Abel–Jacobi images of differences of special points. I cite this description from memory (Carlson's extension classes); I do not verify the exact normalisation here.
- These data determine (Ỹ_t, points) up to a finite ambiguity. Combined with continuity, constancy of H^1(Ỹ_t) plus its extension data would give Y_t = Y_0.
- Conversely, Y_t = Y_0 makes the data constant.
- For g_i = 0 only the extension data carry information.
- So the "claim to prove" is the conclusion of MS4 rewritten in Hodge-theoretic language. It is not a weaker intermediate step.

### B.2 Global Hodge theory available, and why it does not compare different t
These facts are topological, or rigid on a fixed base.
- (a) By (R2), π_1(V_t) ≅ π_1(V_0) and the monodromy ρ_t is conjugate to ρ_0 (P-c).
- (b) By Deligne's semisimplicity theorem (cited from memory), the local system H^1 over V_t decomposes as ⊕_k L_k ⊗ U_k, with L_k irreducible and pairwise non-isomorphic. This decomposition is the same for all t, since it depends only on ρ.
- (c) Each L_k carries a VHS over V_t that is unique up to a Tate shift (Deligne).
- (d) U_k carries a constant Hodge structure.

The uniqueness in (c) is uniqueness **for a fixed complex structure on the base**. The base V_t changes complex structure with t, and the VHS on L_k over V_t is a different object for each t. Nothing in (a)–(d) compares them. In particular:
- If H^1(Ỹ_t) extended to a summand with finite monodromy (a fixed part), the theorem of the fixed part (cited from memory) would make it constant **on V_t**. But t ↦ (that constant Hodge structure) would be an arbitrary holomorphic map of t, as far as (a)–(d) are concerned.
- The model "V × {Y_t}" inside a product stratum shows that such a fixed part can move. That model satisfies (a)–(d) for every holomorphic arc Y_t.
- If H^1(Ỹ_t) is only a piece of Gr^W_1 of the local monodromy, the situation is the same. It is a local system on a punctured tubular neighbourhood of ∂V_t, and nothing global is attached to it.

### B.3 No semi-local argument can work
Observation 4 of P-a and Lemma 1 of P-b already show the following.
- In coordinates (y, z, s) near ∂V_t, take any holomorphic arc Y_t and any germ y = Y_t + s·h(z, s, t). Such germs satisfy every condition that hypotheses (i) and (ii) impose near closure(∂V_t): the stratum incidences, the triviality of the strata families, and the compatibility of closures.
- They have the same local monodromy N, hence the same weight filtration.
- Their LMHS has Gr^W_1 ⊃ H^1(Ỹ_t), which moves with the arc.
- Asymptotic Hodge theory (the nilpotent and SL_2-orbit theorems of Schmid and Cattani–Kaplan–Schmid, cited from memory) describes the period map near ∂V_t *given* the LMHS. It places no constraint on which LMHS occurs.

Hence any proof must use the interior of V_t globally, together with something that ties V_t back to the total geodesy of V_0.

The only t-independent global data are topological: (R2), ρ, the boundary combinatorics, and the Kobayashi inequalities of P-e. Topological data alone do not suffice, since every hypothesis is invariant under the model deformations above wherever such deformations exist globally. So what is missing is a **rigidity statement**.

## §C. Sub-classes in which the conclusion is proved (labelled; none of them settles MS4)
- **C1.** dim M_{g_i,n_i} = 0, i.e. (g_i, n_i) = (0, 3). Trivial: the factor is a point.
- **C2.** Every V_t is totally geodesic. Totally geodesic subvarieties form a countable set (Eskin–Mirzakhani–Mohammadi; Filip; Wright; cited from memory). So t ↦ V_t takes countably many values, and hence so does t ↦ Y_t. A continuous map from Δ with countable image is constant, since Δ is connected and a countable connected metric space is a point.
- **C3.** The closure of V_0 is infinitesimally rigid in the sense of Proposition A. This is §A.
- **C4.** The family closure(V_t) is constant for |t| < ε for some ε > 0. Then Y_t = Y_0 for all t by §0. (Recorded to make clear that only a germ at t = 0 is needed.)

### Can MS4 fail? No counterexample is known to me
- A counterexample would be a totally geodesic surface V_0 that deforms non-trivially, satisfying (i) and (ii), with a 1-dimensional boundary piece in a product stratum that is constant on a factor which moves.
- I checked the obvious candidate: the bielliptic surface B ⊂ M_2. It is totally geodesic, being the image of the fixed set of an isometry of T_2, and it is a divisor, so it might move in a linear system on M̄_2.
- It is not relevant to MS4. The codimension-1 strata of M̄_2 are Δ_0 ≅ M_{1,2}/(Z/2) and Δ_1 ≅ Sym² M_{1,1}, both quotient strata, which the problem excludes.
- Strata of codimension ≥ 2 meet a surface in dimension 1 only by containing a whole 1-dimensional stratum. For M̄_2 the only such candidate has M_{0,3} as its constant factor, which is case C1.
- (I also find closure(B) ∩ Δ_1 = the diagonal {(E, E)}, which is not constant on a factor.)
- So the question remains open; I do not claim MS4 is false.

## §D. The single missing lemma
**Missing Lemma (local rigidity of totally geodesic surfaces).** Let V_0 ⊂ M_g be a smooth 2-dimensional totally geodesic subvariety, and let 𝒱 be a family as in MS4, satisfying (i), (ii), (R1), (R2). Then closure(V_t) = closure(V_0) for all |t| sufficiently small.

By §0 the Missing Lemma implies MS4. Either of the following is sufficient for it:
- **(D1)** (first-order, at t = 0 only) Hom(I/I², O_{Ẑ_0}) = 0 for the flat limit Ẑ_0 of §A. When Ẑ_0 is reduced this is H^0(closure V_0, N) = 0 on the level cover. (Proposition A.)
- **(D2)** (persistence) Every V_t is totally geodesic. (C2.)

### Suggested route to (D2), modelled on Möller's rigidity of Teichmüller curves (all unproved here)
Möller (cited from memory: "Variations of Hodge structures of a Teichmüller curve", JAMS 2006) proves that Teichmüller curves are rigid. He uses that the rank-2 tautological sub-VHS has maximal Higgs field (Arakelov equality), and that maximality is a topological invariant of the monodromy (a Toledo-type invariant).

The surface analogue would need three steps.
- **(α) The tautological summand persists as a sub-VHS.** Let W ⊂ H^1 over V_0 be the rank-4 tautological sub-local system of the orbit closure. Transport it to V_t via ρ. It is a sub-VHS over V_t if it is a sum of isotypic components of multiplicity one, by B.2(b),(c). I have not checked this multiplicity condition.
- **(β) Maximality is invariant.** Over V_0, the Higgs field of W is "maximal": T_X V_0 is spanned by the Beltrami differentials ω̄/ω for ω ∈ W^{1,0}_X, and θ_{ω̄/ω}(ω) = [ω̄] ≠ 0. One would need a characteristic number of the pair (ρ|_W, cusps) — a Toledo invariant in bounded cohomology, in the sense of Burger–Iozzi–Wienhard (cited from memory) — that is constant in t and detects this maximality.
- **(γ) Characterization.** A surface in M_g carrying a rank-4 sub-VHS with maximal Higgs field in the sense of (β), with the appropriate zero conditions, is totally geodesic. This would be the analogue of Möller's characterization of Teichmüller curves. I know of no such result, and (γ) is the core open point.

The hypothesis that ∂V_t is constant on the factor i is not used in this route. If the Missing Lemma holds, MS4 holds for every boundary piece. The constancy hypothesis would only matter for a proof that pins Y_t through some special property of Y_0, and §B shows that no such property is visible near ∂V_t.

## Status
- **Proved:**
  - §0: holomorphy of t ↦ Y_t, with the repaired properness argument.
  - Proposition A: infinitesimal rigidity at t = 0 implies MS4.
  - §B.1: the Hodge claim is equivalent to the conclusion, modulo the cited Torelli and extension-class facts.
  - §B.3: no semi-local proof exists (building on P-a and P-b).
  - Sub-classes C1–C4 (C2 relies on the cited countability theorem).

### round4_q9 (verbatim): Imayoshi–Shiga rigidity, Theorems A and B
## Cited theorem (from memory)
**Rigidity theorem (Arakelov–Parshin; Imayoshi–Shiga 1988, "A finiteness theorem for holomorphic families of Riemann surfaces"; McMullen's Bull. AMS survey states it in this form).** Let S be a Riemann surface of finite type, i.e. a compact Riemann surface minus finitely many points. Then:
- a homotopy class of maps S -> M_g contains only finitely many non-constant holomorphic maps;
- in particular, a non-constant holomorphic map S -> M_g is rigid.

The original statement is for holomorphic families. It says that two locally non-trivial holomorphic families of genus-g curves over S that are topologically equivalent are holomorphically equivalent. To pass from families to maps into the coarse space one goes to a finite level cover M_g[m], m ≥ 3. I take this reduction as standard and do not re-prove it here. (Caveat: if one insists on orbifold homotopy classes, the continuous families below give orbifold-homotopic maps as long as the homotopy lifts. For the families below the homotopy is a continuous family of holomorphic maps, and I take that to suffice.)

**Lemma 0.** Let F_t : S -> M_g, t ∈ Δ, be holomorphic maps with (s,t) -> F_t(s) continuous, and suppose F_0 is non-constant. Then F_t = F_0 for all t.

*Proof.*
1. Suppose F_t were constant for some t. Since F_t is homotopic to F_0, the map F_0 would induce the trivial orbifold-monodromy class. Then F_0 would lift, on a finite cover S' of S (also of finite type), to a holomorphic map into Teichmüller space T_g.
2. T_g is a bounded domain (Bers embedding). Bounded holomorphic functions extend over punctures, so the lift extends to the compact surface S̄'. A holomorphic map from a compact Riemann surface into a bounded domain is constant (maximum principle applied to the coordinate functions). So F_0 would be constant, a contradiction.
3. Hence every F_t is non-constant and homotopic to F_0. By the rigidity theorem, the set Φ of non-constant holomorphic maps homotopic to F_0 is finite.
4. The map t -> F_t is continuous into C(S, M_g) with the compact-open topology, which is Hausdorff. So it is a continuous map from the connected set Δ into the finite, hence discrete, set Φ. It is therefore constant. ∎

## Theorem A (pinning by a rigid test curve)
Suppose there are:
- a compact Riemann surface S̄, a finite set P ⊂ S̄, S = S̄ \ P, and a point p ∈ P;
- continuous maps h : S̄ × Δ -> M̄_g with each h_t := h(·,t) holomorphic;

such that h_t(S) ⊂ V_t, h_0|_S is non-constant, and h_t(p) ∈ ∂V_t for all t. Then Y_t = Y_0 for all t.

*Proof.* Lemma 0 applied to F_t = h_t|_S (which maps into V_t ⊂ M_g) gives h_t|_S = h_0|_S. By continuity h_t(p) = h_0(p) for every t. This point lies in ∂V_t, so it lies in Δ_Γ, and π_i of it is Y_t. Hence Y_t = π_i(h_0(p)) = Y_0. ∎

## Theorem B (constant complex structure ⇒ V_t = V_0)
Suppose there are biholomorphisms Φ_t : V_0 -> V_t with (x,t) -> Φ_t(x) continuous and Φ_0 = id. This holds, for instance, if 𝒱 -> Δ is holomorphically locally trivial. Then V_t = V_0 for all t, and hence Y_t = Y_0.

*Proof.*
1. V_0 is quasi-projective (R1 and Chow's theorem). Fix x ∈ V_0.
2. A general complete-intersection curve through x in a projective closure gives an irreducible algebraic curve C ⊂ V_0 through x that is smooth at x (Bertini).
3. Let ν : S -> C be its normalization, with finitely many points removed so that S is of finite type and still contains a point s_x with ν(s_x) = x.
4. F_t := Φ_t ∘ ν : S -> M_g is a continuous family of holomorphic maps. F_0 = ν is non-constant.
5. Lemma 0 gives Φ_t(x) = F_t(s_x) = F_0(s_x) = x.
6. Since x was arbitrary, V_t = Φ_t(V_0) = V_0. So closure(V_t) = closure(V_0), ∂V_t = ∂V_0 and Y_t = Y_0. ∎

**Corollary B'.** Suppose the closures form a smooth proper family of log pairs (V̄_t, D_t) (simple normal crossing boundary) and H^1(V̄_0, T_{V̄_0}(-log D_0)) = 0. Then the claim holds. The same is true if all the pairs (V̄_t, D_t) are biholomorphic to one another.
- *Proof sketch.* Kodaira–Spencer–Kuranishi theory for log pairs, or the Fischer–Grauert theorem in the second case (both cited from memory), makes the family locally holomorphically trivial near t = 0. Then Theorem B applies near 0. The identity theorem for the holomorphic map t -> Y_t (P-a Lemma 1) extends constancy to the whole disc.
- *Status.* This is conditional on the extra hypotheses: that the family is log-smooth, and that the H^1 vanishes or the pairs are isomorphic. These are not part of the problem.

## What this says about the general case
1. **Any counterexample needs varying complex structure.**
   - By Theorem B, the abstract complex manifolds V_t must vary in moduli.
   - By Theorem A, the curves in V_t that pass into ∂V_t (in the sense of A) must have complex structures that change with t, or must fail to deform continuously.
   - So the claim is equivalent to a global rigidity statement about V̄_t near ∂V_t. Local data (plumbing coordinates, monodromy, weight filtrations, hypothesis (ii) along Γ) cannot decide it. This matches P-a Obs. 4 and P-b, which I re-checked and agree with.
2. **Heuristic evidence that (i), (ii) and smooth triviality are very restrictive.** (Sketch; not used anywhere.)
   - *Example 1.* In M_{0,7}, take V_0 = {there is an involution with p1<->p2, p3<->p4, p5<->p6 and p7 fixed}. It is totally geodesic, being a covering construction from M_{0,5}. It has a boundary curve in D_{127} ≅ M_{0,4} × M_{0,5} with a constant factor, the harmonic 4-pointed sphere (Y_0 is non-trivial here).
   - The natural deformation moves p7 off the fixed point within the 3-fold W where only the pairs are imposed. Every such deformation makes p7 collide with ±a or ±b over curves inside V_0. So V_t would meet new boundary strata, and smooth triviality fails.
   - Equivalently: a deformation of this kind would be a section of the log normal bundle ≈ ψ_7^∨|_{V̄_0}, and ψ_7 is nef and big, so no such section exists. I also checked that a deformation with p7 = t·h(X) would need h/a and h/b to be bounded regular functions on an affine variety, which is impossible.
   - *Example 2.* In M_{0,6}, viewed as a blow-up of the Segre cubic, the involution locus is a hyperplane section. It moves in a P^4 of hyperplane sections. However, (i) forces V_t to contain the same boundary curves of the codimension-2 strata (6 lines) and to pass through the same 4 nodes. This seems to leave only V_0. I did not complete this verification.
   - These examples suggest that the claim is "true because V_0 is rigid under (i) and (ii)". That is far from a proof.

## What is proved / not proved
- **Proved** (modulo the cited rigidity theorem and the standard reduction from families to the coarse space):
  - Lemma 0;
  - Theorem A (claim holds whenever there is a continuous family of holomorphic test curves of fixed complex structure reaching ∂V_t);
  - Theorem B (claim holds, indeed V_t = V_0, whenever the V_t are biholomorphic to V_0 compatibly with the family).
- **Conditional:** Corollary B' (log-smooth family together with H^1(T(-log D)) = 0, or isomorphic pairs).
- **Also known (P-a Lemma 3, re-checked):** the claim holds if every V_t is totally geodesic (countability of totally geodesic subvarieties, cited from memory).
- **Heuristic only:** the examples above.
- **Open:**
  - (Q1) Is every totally geodesic surface V_0 ⊂ M_g rigid among families satisfying (i), (ii) and smooth triviality, i.e. is V_t = V_0? A yes answer implies the claim.
  - (Q2) Without such rigidity, does some global mechanism pin Y_t? Candidates are a Hodge-theoretic coupling of the interior VHS to Gr^W_1 ⊃ H^1(Y_t), or the incidence mechanism of P-d.

### round5_q7 §§1–3 (verbatim): one-point pinning, persistence of Teichmüller curves, holomorphically trivial deformations are trivial
## §1. One-point pinning (proved)

**Lemma 1.** Suppose there is a set S ⊂ Δ with an accumulation point in Δ such that, for each t ∈ S, closure(V_t) ∩ closure(∂V_0) ∩ Δ_Γ ≠ ∅. Then Y_t = Y_0 for all t ∈ Δ.

*Proof.*
1. Fix t ∈ S and a point p in the intersection.
2. Since p ∈ closure(V_t) ∩ Δ_Γ = ∂V_t, we have π_i(p) = Y_t.
3. Since p ∈ closure(∂V_0) ∩ Δ_Γ, and the latter set equals ∂V_0 because ∂V_0 is closed in Δ_Γ, we have π_i(p) = Y_0.
4. So Y_t = Y_0 on S. The map t ↦ Y_t is holomorphic (PR-1), so the identity theorem gives Y ≡ Y_0. ∎

So MS4 is equivalent to the statement that ∂V_t meets ∂V_0 for t in a set accumulating in Δ. Conversely, if Y_t ≠ Y_0 then ∂V_t ∩ ∂V_0 = ∅.

---

## §2. Teichmüller curves: persistence is equivalent to containment

**Cited theorem (McMullen, rigidity of Teichmüller curves) [mem].** Let f : B → M_g be a Teichmüller curve, with B a hyperbolic Riemann surface of finite type. Let f' : B' → M_g be a holomorphic map from a Riemann surface of finite type, and let h : B → B' be a homeomorphism (preserving punctures) such that f' ∘ h is homotopic to f. Then f'(B') = f(B). In fact h is homotopic to a biholomorphism B → B' that intertwines the maps up to finite ambiguity.

The proof is the one recalled in the task:
- Royden's theorem plus Schwarz–Pick give ℓ_{B'}(h_*γ) ≥ τ_T(ρ(γ)) = ℓ_B(γ) for all γ.
- Thurston's theorem (a surface of the same finite-area type cannot have its length spectrum dominate unless isometric) gives B' ≅ B.
- Imayoshi–Shiga then gives f' = f ∘ h^{-1} up to finitely many choices. Continuity in a parameter removes this ambiguity.

**Proposition 2.** Let T = f(B) ⊂ V_0 be a Teichmüller curve with closure(T) ∩ ∂V_0 ≠ ∅. Fix t. The following are equivalent:
- (a) there is a holomorphic map f_t : B_t → V_t from a finite-type Riemann surface, and a homeomorphism h : B → B_t, such that ι_t ∘ f_t ∘ h is homotopic to ι_0 ∘ f, where ι_s : V_s ⊂ M_g;
- (b) T ⊂ V_t.

If (a) or (b) holds for all t in a set accumulating in Δ, then Y_t ≡ Y_0.

*Proof.*
1. (b) ⇒ (a): take f_t = f.
2. (a) ⇒ (b): by the cited theorem, f_t(B_t) = T, so T ⊂ V_t.
3. Under (b), closure(T) ⊂ closure(V_t). Pick p ∈ closure(T) ∩ ∂V_0. Then p ∈ closure(V_t) ∩ ∂V_0, and Lemma 1 applies. ∎

In particular, a family f_t ⊂ V_t obtained by continuously deforming f along the trivialization of (R2) would give (a), because the homotopy then exists automatically.

**Consequence for the suggested strategy (first bullet of the task).** "Show that T forces a holomorphic curve T_t ⊂ V_t homotopic to T" is *literally equivalent* to "T ⊂ V_t". So it carries the full difficulty: it is the claim that V_t contains a fixed curve of V_0. At first order this is the following.

- Let σ ∈ H^0(V_0, N_{V_0/M_g}) be the first-order deformation (the Kodaira–Spencer normal section) defined by 𝒱.
- Suppose a curve deformation T_t ⊂ V_t exists. Then T_t = T by the above, so T ⊂ V_t for all small t, and the first-order normal motion of V_0 vanishes along T, i.e. σ|_T = 0.
- So persistence of the Teichmüller curves of a dense family forces σ ≡ 0. That is first-order rigidity of V_0, which is exactly what is unknown.

Deformation theory cannot produce T_t either.
- The obstruction to lifting T into the fibres of 𝒱 lies in H^1 of the (log) normal bundle N_{T/V_0}.
- That group is in general nonzero. T is rigid in V_0, so h^0(N) = 0, and Riemann–Roch gives h^1(N) = −χ(N) = −deg N + g(T̄) − 1.
- By analogy with totally geodesic curves in locally symmetric surfaces (e.g. the diagonal in C × C has self-intersection 2 − 2g), I expect this to be positive. I have not proved deg N < 0 here.
- Even where h^1 = 0 one gets T_t ⊂ V_t only for those t, and then T_t = T, i.e. the conclusion T ⊂ V_t again.

**Status.** Proposition 2 is proved, modulo the cited McMullen theorem. It turns the first suggested route into the equivalent problem "V_t ⊃ T". I could not solve that.

---

## §3. Holomorphically trivial deformations are trivial; PR-6's mechanism is void

**Proposition 3.** Suppose there are biholomorphisms Φ_t : V_0 → V_t with (x,t) ↦ Φ_t(x) continuous and Φ_0 = id. Then V_t = V_0 for all t, so Y_t ≡ Y_0.

This is PR-4 Theorem B. I re-checked its proof:
- through every x ∈ V_0 there passes an algebraic curve, with normalization ν : S → V_0 and ν(s_x) = x;
- Lemma 0 (Imayoshi–Shiga finiteness, cited, plus connectedness of Δ) applied to Φ_t ∘ ν gives Φ_t(x) = x.

The only external input is the Imayoshi–Shiga / Arakelov–Parshin finiteness [mem].

**Corollary 3′ (correction to PR-6).** No holomorphic vector field ξ satisfying (a) and (b) of PR-6 Theorem B, with v(Y_0) ≠ 0, exists. More generally, every logarithmic holomorphic vector field ξ defined near closure(V_0) is tangent to V_0 along V_0.

*Proof.*
1. Let Φ_s be the flow of ξ. For |s| small, Φ_s restricts to biholomorphisms V_0 → Φ_s(V_0), continuous in s with Φ_0 = id. These are subvarieties of M_g: Φ preserves M_g and the strata, and Chow's theorem applies, as in PR-6 step 2.
2. Proposition 3 gives Φ_s(V_0) = V_0 for all small s, so ξ is tangent to V_0 along V_0.
3. Under (b), PR-6 shows that π_i(Φ_s(∂V_0)) = {φ_s(Y_0)}. Since Φ_s(V_0) = V_0, it is also {Y_0}. Hence φ_s(Y_0) = Y_0 for small s, and v(Y_0) = 0. ∎

So the "open question" at the end of PR-6 is settled in the negative: PR-6's construction never yields a counterexample. **Any counterexample to MS4 must be a family in which the abstract complex structure of V_t, or of the pair (closure V_t, boundary), genuinely varies.** That is, the family 𝒱 → Δ is not holomorphically locally trivial near any t. Equivalently, the problem is a statement about the Kodaira–Spencer class of 𝒱, not about ambient motions.

---


### round8_q10 §5 (verbatim): Theorem TV
## 5. The form needed by chain step 2 (task item 3)

**Theorem TV (every boundary piece has a Teichmüller vertex).** Let G be the dual graph of a boundary stratum (any G with at least one edge, product type or not), Â := ξ_G^{-1}(closure(V_0) ∩ Δ_G) ⊂ Δ̂_G = ∏_w M_{g_w,n_w}, and E any 1-dimensional irreducible component of Â (no assumption that E meets closure(∂V_0)), with normalization ν: E^ν → E. Then there are a vertex j of G and an integrable quadratic differential η_j ≠ 0 on a curve Y_j ∈ π_j(E) such that, with D: H → T(Σ_j) the Teichmüller disc of (Y_j,η_j) and Γ′ ⊂ Aut(H) the (projectivized) Veech group:
1. C := closure of π_j(E) is a Teichmüller curve, C^ν = H/Γ′, and Γ′ is a lattice;
2. p := π_j∘ν: E^ν → C^ν is **proper** and E^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p;
3. **orbifold structure**: give E^ν the orbifold structure of H/Λ_E, i.e. a point e over an orbifold point of C^ν of order m, at which p has local degree k, gets order m/k (k always divides m). Then p is an orbifold covering (orbifold-unramified), and the lift of π_j∘ν to orbifold universal covers is D, an isometric holomorphic embedding onto the Teichmüller disc, equivariant for Λ_E → Mod(Σ_j);
4. E is not compact, and every end of E^ν maps to a cusp of C (so along every end of E the j-component degenerates).
For product-type G (the case of the problem's Δ_Γ), Â = closure(V_0) ∩ Δ_G and ξ_G = id.

*Proof.* Pick P̂ ∈ E outside the finite set Sing Â ∪ (E ∩ other components) and outside the discrete exceptional set of PR-H Lemma PA, and let P = ξ_G(P̂). Lemma PA (PR-H, quoted; its proof is local in the plumbing chart at P, an orbifold chart of M̄_g whose fibres carry a labelling of components by V(G), hence it applies at P̂ ∈ Δ̂_G; and it uses only a ≠ 0 at P̂, true off a discrete set) gives generating pairs (X_n,q_n), ‖q_n‖ = 1, X_n → P along the branch of closure(V_0) through P̂, and a vertex j with q_j ≢ 0 (it maximizes the Teichmüller norm of the j-component of the tangent vector a of E at P̂). Lemma TR turns this into "j carries positive area" (Def. FA, η_j := q_j integrable, ∫|η_j| ≤ 1). Corollary Φ̂ gives φ̂: H → Â with φ̂(i) = P̂ (the labelled lift defined by the plumbing markings is P̂) and π_j∘φ̂ = u. Steps 2′, 3′, 4′, 5 of §4 then give 1–4; Step 2′ produces the component through φ̂(i) = P̂, which is E by the choice of P̂. ∎

**Caveats on item 3 (stated precisely).**
- The orbifold structure in (3) is the one *induced by Λ_E*; I have **not** shown that it coincides with the orbifold structure E inherits as a curve in the orbifold Δ̂_G (or M̄_g). They agree away from the finitely many points over orbifold points of C. If one prefers to avoid orbifolds, pass to a level-m cover: replace Γ′ by the torsion-free Γ′_m := π_1(C'^ν) and E^ν by a component of the fibre product E^ν ×_{C^ν} C'^ν normalized; then p becomes a genuine unramified finite covering of Riemann surfaces and the lift to universal covers is again D.
- Lemma PA is quoted, not re-proved, and in the non-product case its applicability on Δ̂_G rests on the labelled plumbing chart (Pl), which I have only described.
- The map φ̂ depends on the chosen subsequence; Theorem TV does not.
