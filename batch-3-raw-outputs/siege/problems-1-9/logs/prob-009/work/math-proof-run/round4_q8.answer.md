# Answer to round4_q8 (MS4 via the limiting Hodge structure along the boundary)

## Plan
1. Settle the "first order at t = 0 only" worry: show that infinitesimal rigidity of closure(V_0) in the Douady sense gives the claim for all t.
2. Look at the proposed step: is the limit of H^1(Y_t) along ∂V_t constant in t? Show that nothing living on ∂V_t, or on a neighbourhood of it, can force this. Locate exactly which global input is missing.
3. Prove what I can for sub-classes, labelled as such. State the single missing lemma in full.

---

## Summary of outcome
- **Not proved:** the statement MS4 in general. I do not believe it can be proved from the listed hypotheses without a global rigidity theorem for totally geodesic surfaces. To my knowledge no such theorem is in the literature; this is from memory.
- **The proposed Hodge step:** the claim "the limit of H^1(Y_t), with its extension data, is constant in t" is a restatement of the conclusion, not a reduction of it (§B). No information living on ∂V_t or on a neighbourhood of it can prove it (§B.3).
- **Proved:**
  - (§A) Infinitesimal rigidity of the closure of V_0 at t = 0 alone already implies the conclusion for all t. This disposes of the worry that a first-order argument at t = 0 cannot exclude Y_t = Y_0 + t²v: it cannot if it is applied only to Y, but it can if it is applied to the whole Douady germ.
  - (§C) The conclusion holds in a few sub-classes, each labelled.
- **Single missing lemma:** stated in §D.

---

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
- **Open:**
  - MS4 itself.
  - The Missing Lemma, through (D1) or (D2).
  - In the suggested route: steps (α), (β) and (γ), with (γ) the main point.
  - Whether any totally geodesic surface in M_g admits a non-trivial deformation of the kind described. No counterexample is known to me.

=== END OF ANSWER round4_q8 ===
