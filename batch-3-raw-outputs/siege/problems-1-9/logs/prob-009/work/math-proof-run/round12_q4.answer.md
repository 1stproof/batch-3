# round12_q4 — attempt to refute MS11♭

**Status line.** NO counterexample to MS11♭ (hence to the problem) was found. There is also NO derivation of a false statement from MS11♭ plus PROVED entries, and I found no error in a PROVED entry. What follows records (§2) some elementary sharper necessary conditions, with proofs, and (§3) why the candidate classes I examined do not give a refutation. Everything is under the readings (R1), (R2) and the hypothesis (Rig), as in the task file.

## 0. Logical position (restated, not new)
MS11♭ assumes "t ↦ Y_t non-constant". So any admissible configuration in which MS11♭ fails is a family V_t satisfying the problem's hypotheses, plus (Rig), with Y_t ≠ Y_0 for some t. That is a counterexample to the problem itself. A type-1 refutation therefore has to meet the full global requirements:
- V_0 is smooth, closed in M_g, 2-dimensional and totally geodesic;
- an actual holomorphic family satisfying (i), (ii), (R1), (R2), (Rig).

Chart-level models do not meet these requirements, and the run already has such models. I did not build a global family. The only known source of totally geodesic surfaces in M_g is covering constructions from the Eskin–McMullen–Mukamel–Wright surfaces and from M_{0,5}, M_{1,2}, quoted from memory. Their images are in general not smooth: the quintic example of PR-I is not. I could not exhibit one that is smooth and has the twin structure required below.

## 1. Necessary conditions already known (taken from the task file, not re-proved)
A failure of MS11♭ at Q requires all of the following:
- (N0) Q lies in a non-product stratum.
- (N0′) There is a ∈ Aut(Q) with a·x ≠ x such that a is not inherited by Q_t (Q_t has more than one lift-curve).
- (N0″) (NC1), (NC2) of round11_q4 hold at every point of the reachable network.
- (N0‴) The failure is realised through a label-moving composite of (β)-twists, or through (γ°), in Mechanism D.

## 2. New elementary necessary conditions (proved)

**Lemma 2.1 (Euler-characteristic bound).** Suppose MS11♭ fails at Q, with label x and twin a·x as in (N0′). Then the following hold.
- Q has two distinct components, x and a·x, each isomorphic to Y_0 as an n_i-pointed curve.
- 2(2g_i − 2 + n_i) ≤ 2g − 2.
- Every other component w of Q satisfies 2g_w − 2 + n_w ≥ 1, so Q has at most (2g−2) − 2(2g_i−2+n_i) further components.

*Proof.* a ∈ Aut(Q) maps the component x isomorphically onto the component a·x ≠ x, and it carries special points to special points. So a·x ≅ F_x(0) ≅ Y_0, of type (g_i,n_i). For a stable curve, Σ_w (2g_w − 2 + n_w) = 2g − 2, where n_w counts the preimages of nodes on w. This is additivity of the Euler characteristic of the normalisation punctured at the special points. Every term is ≥ 1 by stability. ∎

**Corollary 2.2.**
- Since dim M_{g_i,n_i} > 0, we have (g_i,n_i) ≠ (0,3), so 2g_i − 2 + n_i ≥ 1. Equality holds only for (1,1); the value is 2 for (0,4) and (1,2).
- Hence a counterexample needs either (g_i,n_i) = (1,1) and g ≥ 2, or 2g_i − 2 + n_i ≥ 2 and g ≥ 3.

**Lemma 2.3 (g = 2 is vacuous for the problem).** For g = 2 there is no product-type stratum Δ_Γ with a vertex i of positive dimension and a 1-dimensional ∂V_t ⊂ Δ_Γ that is constant on factor i. Hence any counterexample to the problem, and hence any refutation of MS11♭, has g ≥ 3.

*Proof.*
1. ∂V_t is 1-dimensional and constant on factor i. So Σ_{j≠i} dim M_{g_j,n_j} ≥ 1, and dim M_{g_i,n_i} ≥ 1.
2. A vertex of positive dimension has 2g_w − 2 + n_w ≥ 1, with equality only for (1,1). A vertex (g_w,n_w) has dimension 3g_w − 3 + n_w ≥ 1 only if it is not (0,3). The vertices with 2g_w−2+n_w = 1 are exactly (0,3) and (1,1).
3. In genus 2, Σ(2g_w−2+n_w) = 2. So Γ has either:
   - two vertices with value 1, both of positive dimension, i.e. both (1,1); or
   - one vertex with value 2.
4. Two (1,1) vertices: the graph is two elliptic tails joined by a node, Δ_Γ = Δ_1 ≅ (M_{1,1} × M_{1,1})/S_2. This is not product type: the edge-swapping automorphism acts non-trivially on M_{1,1} × M_{1,1}. It is excluded by the problem's footnote.
5. One vertex: then there is no second factor to carry the 1-dimensional ∂V_t, contradicting step 1. ∎

**Lemma 2.4 (g = 3 with (g_i,n_i) = (0,4): the twin point is forced).** Let g = 3 and (g_i,n_i) = (0,4). If MS11♭ fails at Q, then:
- Q consists of exactly two smooth rational components x and a·x, each with 4 special points, both isomorphic to Y_0;
- G_Q is either the "banana" graph (4 edges between the two vertices) or the graph with 2 edges between them and one loop at each vertex.

*Proof.*
1. By Lemma 2.1, the two twin components already give Σ = 4 = 2g − 2, so there are no other components.
2. The valences are 4 = 2·loops(v) + #edges(A–B). Connectedness forces #edges(A–B) ≥ 1, and parity forces #edges(A–B) ∈ {2, 4}.
3. h^1 = |E| − 2 + 1 = 3 holds in both cases. ∎

In both cases Δ_{G_Q} has dimension 2 and codimension 4 in M̄_3. The closure of the 2-dimensional V_0 meets it in a finite set or a curve, so Q is a very special point. Moreover, both cross-ratios of Q must equal the class of Y_0 (up to S_4).

**Lemma 2.5 (g = 3 with (g_i,n_i) = (1,1)).** Here Q has two elliptic-tail-type components x, a·x ≅ Y_0, using Σ-mass 2. The remaining mass 2 is carried by:
- one component of type (0,4), (1,2) or (2,0); or
- two components of types (1,1) or (0,3).

This is immediate from Lemma 2.1. Combined with (N0′), a must exchange two components ≅ (Y_0, p) attached to the rest of Q.

These lemmas narrow the search but do not exclude it: in g = 3 the special points of Lemmas 2.4–2.5 exist in M̄_3.

## 3. Candidate classes tested and why they do not give a refutation
1. **Covering-construction surfaces (M_{0,5}-type, cyclic covers).** Their cusps have many symmetric twin components, so (N0), (N0′) are easy to meet. But:
   - the closure of the image surface in M_g is typically not smooth (PR-I quintic example); smoothness of V_0 is a hypothesis;
   - a deformation V_t satisfying (ii) and (Rig) with Y non-constant would still have to be built globally. I have no construction, and no obstruction either.
2. **g = 3, (0,4)-twins (Lemma 2.4).** This needs a smooth totally geodesic surface in M_3 whose closure passes through a banana-type point with two isomorphic 4-pointed lines.
   - I do not know (from memory) any smooth totally geodesic surface in M_3. Not having one does not prove there is none.
   - So this candidate is untestable here.
3. **Purely local (chart-level) models.** These are excluded by the task: they are known and do not refute MS11♭.

## 4. Summary
- **Proved:** Lemma 2.1 (Euler-characteristic bound for twin points), Corollary 2.2, Lemma 2.3 (the problem is vacuous for g = 2, so every counterexample has g ≥ 3), Lemmas 2.4–2.5 (the shape of a twin point Q for g = 3).
- **Not proved:** a refutation of MS11♭, a counterexample to the problem, an error in a PROVED entry of the run. None was found.
- **Open:**
  - MS11♭ itself.
  - (Rig) (entry 82).
  - Whether a smooth closed totally geodesic surface in M_3 (or any M_g) has a boundary point with a twin pair of positive-dimensional Y_0-copies satisfying (N0)–(N0‴). A negative answer for all g would settle MS11♭ vacuously.

=== END OF ANSWER round12_q4 ===
