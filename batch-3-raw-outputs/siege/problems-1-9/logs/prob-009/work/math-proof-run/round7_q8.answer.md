# round7_q8 — answer (MS6)

**Status.** PARTIAL. I do not prove MS6 in full, and I do not give a counterexample. What this file contains:
- (§1) A check of the chain (L1, L2, steps 1–4). No fatal flaw. L1 is correct as written. L2 is correct modulo the cited results, with two caveats that need to be written out. One structural remark: MS6 *as stated* is stronger than the chain needs. For constant families it contains a statement about V_0 alone (MS6_0), which nobody has proved. The chain only needs MS6′ ("Y non-constant ⇒ the configuration exists").
- (§2) Rigorous auxiliary lemmas at time t: non-constancy persists off a discrete set; limits of components; finiteness of the label set.
- (§3) **Theorem A (partial).** MS6 holds (for every t with 0 < |t| < t_0 outside a discrete set) if the following three conditions hold:
  - (K) the endpoint of the Y_0-network of Proposition K is of type MERGE, or MOV at a puncture;
  - (NT*) no boundary point of closure(V_0) has two components isomorphic to Y_0 ("no twins");
  - (PT) the strata carrying arcs of the network are of product type.
  (PT) is only a convenience; see Remark 3.5.
- (§4) The cases that remain open, stated precisely: twins on the network, and crossings (the MOV-interior case). I also explain why the natural fix, transporting Teichmüller rays to time t, breaks down on orbifold points.
- (§5) Summary: proved / not proved / open.

Readings (R1), (R2) of the task are used throughout, together with H_0 = id. B_t := closure(V_t) \ V_t.

---

## 1. Check of the chain

### 1.1 L1 (constancy persists): correct
I re-checked each step.
- 𝓦 is closed in ∏_w M̄_w × Δ, so it is proper over Δ. Each fibre is compact and, by Krull, of pure dimension 1.
- If pr_u ≡ Z_0 on the lift of E_0, then pr_u ≡ Z_0 on its closure, which contains 𝓦_0 (Lemma R0).
- The coarse space M_u is quasi-projective, so Z_0 has an affine neighbourhood U. Properness gives pr_u(𝓦_t) ⊂ U for |t| < ε.
- Compact connected curves map to points in an affine variety. So, for small t, the map Φ = (pr_u, t) : 𝓦 → M̄_u × Δ has fibres of dimension ≥ 1 at every point of 𝓦_t.
- The set {p : dim_p Φ^{-1}Φ(p) ≥ 1} is analytic (Cartan–Remmert upper semicontinuity of fibre dimension). It contains a non-empty open subset of the irreducible 𝓦, hence it is all of 𝓦.
- At a point p of a component C of 𝓦_t lying on no other component, the Φ-fibre through p is a germ of dimension ≥ 1 inside 𝓦_t, so it is the germ of C. Hence pr_u is locally constant on C, and constant on C by the identity principle.

A small generalisation is useful: the same proof works if pr_u is constant on every component of 𝓦_0, with possibly different values. Finitely many points of a quasi-projective variety lie in a common affine open set.

### 1.2 L2: correct modulo the cited theorems, with two caveats
- (a) *Homotopy class of g_t.* g_t = f_u^t ∘ A_t and g_0 must be compared as maps from the orbifold Ê_0 into the orbifold M_u. A_t is homotopic to the transported marking Ĥ_t, and f_u^t ∘ Ĥ_t is homotopic to f_u^0 through the homotopy (s, τ) ↦ π_u H(ν_0 s, τ t) of PR-D Step 2.
  - So the two maps agree on the underlying punctured surfaces.
  - In the orbifold sense they agree after passing to the torsion-free finite-index subgroup Λ′_0 of PR-E Step 4 and a level cover of M_u. Imayoshi–Shiga finiteness must be applied there: for maps from the finite-type surface D/Λ′_0 into M_u[N].
  - This is legitimate. It should be written explicitly, because the cone points of f_u need not be those of f_v.
- (b) *Finite set ⇒ constant puncture values.* L2 as written gives g_t ∈ {φ_1, …, φ_r}. To get "f_u^t(p_t) ∈ F(E_0,u) independent of t", one also needs that A_t sends the puncture p_0 to the transported puncture p_t.
  - This holds because A_t ≃ Ĥ_t: on a finite-area hyperbolic surface, distinct punctures have non-conjugate peripheral classes.
  - So f_u^t(p_t) = g_t(p_0) ∈ {φ_j(p_0)}, a finite set.
  - The derivation only uses this finiteness, so this is enough.

### 1.3 Derivation steps 1–4: correct
- **Step 1.** Pigeonhole on a sequence in T converging in Δ, plus the identity theorem for the holomorphic Y (PR-A). F must be closed under relabelling of the n_i points, which it is by definition.
- **Step 4, non-product strata.** One needs that a lifted piece at time t lies in a fibre of the lifted family 𝓦^{(a)} of some piece E_0^{(a)} at time 0. This is immediate from Lemma R0: the lift of closure(V_t) ∩ Δ_G is the t-fibre of ⋃_a 𝓦^{(a)} off the boundary.
- L1 is stated for every 1-dimensional component of 𝓦_t, so it applies whatever the matching of components.
- L2 needs a lifted piece at time t to be identified with the transport of a lifted piece at time 0. This holds on the part where Aut(G) acts freely: there the lift is a covering of E_0° × Δ, and coverings of X × Δ are pulled back from X. Elsewhere one passes to Λ′_0 as in (a).
- I see no flaw.

### 1.4 Structural remark: MS6 is stronger than needed
- **Constant families.** For the constant family V_t ≡ V_0 (H = id), all hypotheses hold. MS6 then reduces to the following statement about V_0 alone:
  **(MS6_0)** some piece E of B_0 has a non-constant vertex u and a puncture p such that f_u(p) has a component ≅ Y_0.
  MS6_0 is NOT known. Section 4.2 explains why: at a "crossing" the copy of Y_0 enters a moving vertex at an interior point, not at a puncture.
- **What the chain uses.** The chain argues by contradiction, so it only needs:
  **(MS6′)** if t ↦ Y_t is non-constant, then the configuration of MS6 exists for t in a set with an accumulation point.
- I recommend replacing MS6 by MS6′ as the target. Everything below is stated so that it applies to both.

---

## 2. Auxiliary lemmas (proved)

Notation:
- "Component ≅ Y_0" means: an irreducible component which, with its special points in some order, is isomorphic to Y_0. Equivalently, its class in M_{g_i,n_i}/S_{n_i} equals that of Y_0.
- Fix a metric d on the compact space M̄_{g_i,n_i}/S_{n_i}.
- Choose ε > 0 so small that the closed ball B̄_{3ε}(Y_0) lies in the open part M_{g_i,n_i}/S_{n_i}.

**Lemma 2.1 (non-constancy persists off a discrete set).** Let 𝓦 be an irreducible 2-dimensional analytic set, closed in ∏_w M̄_w × Δ (hence proper over Δ), with t non-constant on 𝓦. Let u be a vertex. Suppose pr_u is non-constant on some 1-dimensional component of 𝓦_0. Then the set of t such that pr_u is constant on some 1-dimensional component of 𝓦_t is discrete in Δ.

*Proof.*
1. Let Φ = (pr_u, t) and Σ = {p ∈ 𝓦 : dim_p Φ^{-1}Φ(p) ≥ 1}. Σ is analytic (Cartan–Remmert).
2. Suppose t_n → t* ∈ Δ, with t_n pairwise distinct, and pr_u constant on a component C_n of 𝓦_{t_n}. Then C_n ⊂ Σ.
3. If dim Σ ≤ 1, then each C_n is an irreducible component of Σ. Infinitely many of them meet the compact set 𝓦 ∩ {|t − t*| ≤ r}, contradicting local finiteness of the components.
4. So Σ = 𝓦. The last bullet of §1.1 then shows that pr_u is constant on every component of every fibre, including 𝓦_0. This contradicts the hypothesis. ∎

**Lemma 2.2 (limits of components).** Let C_n → C in M̄_g. Let c_n be a component of C_n of type (g_i, n_i) with class in B̄_{3ε}(Y_0). Then, after passing to a subsequence, c_n converges in M̄_{g_i,n_i}/S_{n_i} to the class of a smooth component c of C.

*Proof.*
1. In a versal chart Def(C), for n large, C_n is a smoothing of a subset of the nodes of C. A component c_n of C_n is a smoothing of a connected subcurve A_n of C. After passing to a subsequence, A_n = A is fixed.
2. In the chart, c_n with its special points converges to A, stabilised and pointed by the nodes of C that leave A. This is continuity of the gluing/plumbing maps.
3. If A had two components or an internal node, the limit would lie in the boundary of M̄_{g_i,n_i}. But the limit lies in B̄_{3ε}(Y_0) ⊂ M_{g_i,n_i}/S_{n_i}. So A is a single smooth component c of C. ∎

**Lemma 2.3 (finitely many isolated Y_0-points).** Let F_0 ⊂ B_0 be the union of the following finitely many sets:
- (i) for each stratum G, the isolated points of B_0 ∩ Δ_G (the 0-dimensional components of the compact analytic set B_0 ∩ closure(Δ_G) that lie in Δ_G);
- (ii) the singular points of each 1-dimensional set B_0 ∩ Δ_G;
- (iii) for each piece E (lift of a 1-dimensional component, as in MS6) and each vertex y non-constant on E, the images of the points of E at which f_y takes the value Y_0 (up to relabelling).

Then F_0 is finite.

*Proof.*
- (i) A compact analytic set has finitely many components.
- (ii) Each 1-dimensional set has finitely many singular points on the compact closure.
- (iii) f_y : Ē → M̄_y is a non-constant holomorphic map from a compact Riemann surface. The fibre over each of the finitely many relabellings of Y_0 is finite. ∎

---

## 3. Theorem A (partial result: MS6 without twins)

### 3.1 The input from t = 0 (Proposition K, PR-H, used as a prior result)
I use the following output of Proposition K, which was proved there modulo routine marking details. I did not re-prove it.

**(K)** There are:
- a compact connected set K_0 ⊂ B_0 containing a point P ∈ ∂V_0;
- for every Q ∈ K_0, a component x_Q of Q with x_Q ≅ Y_0 (the "Σ_i-component"), such that at P it is the vertex-i component;
- a point Q_0 ∈ K_0;
- a 1-dimensional branch b of B_0 at Q_0, of one of two types:
  - **(MERGE)** some node of Q_0 at x_{Q_0} is smoothed along b;
  - **(MOV)** all nodes at x_{Q_0} stay pinched along b, and the component carried by x is non-constant along b.

Call the MOV case **at a puncture** if b \ {Q_0} lies in a stratum strictly coarser than that of Q_0, and **interior** otherwise.

### 3.2 Hypotheses
- **(NT\*)** No point of B_0 has two distinct components that are both ≅ Y_0.
  This is a condition on V_0 alone. It FAILS in the quintic example of PR-I, where the point P_0 = Y_0 — B_0 — Y_0 has two components ≅ Y_0.
- **(PT)** Every stratum Δ_G such that K_0 ∩ Δ_G is infinite is of product type.
- **(E)** The endpoint in (K) is of type MERGE, or MOV at a puncture.

**Theorem A.** Assume (R1), (R2), the problem's hypotheses, (K), (NT\*), (PT) and (E). Then there are t_0 > 0 and a discrete set D ⊂ Δ such that the configuration of MS6 exists for every t with |t| < t_0 and t ∉ D.

In the MERGE case D = ∅. In particular MS6 and MS6′ hold under these hypotheses, and with them the problem's claim (via the chain, modulo (O) and (F2)).

### 3.3 Proof of Theorem A

**Step 1 (uniform separation at t = 0).** There is ε > 0, which we may shrink to satisfy §2, such that for every Q ∈ K_0, every component of Q of type (g_i, n_i) other than x_Q has class at distance ≥ 3ε from Y_0.

*Proof.*
1. Otherwise there are Q_n ∈ K_0 and components y_n ≠ x_{Q_n} with y_n → Y_0. Pass to a subsequence with Q_n → Q ∈ K_0 (K_0 is compact).
2. By Lemma 2.2, applied to x_{Q_n} and to y_n (both classes are in B̄_{3ε}(Y_0) for n large), both converge to smooth components of Q isomorphic to Y_0.
3. These limit components are distinct:
   - In a chart Def(Q), for n large, the Q_n lie in a fixed locus of the chart, in which their components are smoothings of fixed disjoint connected subcurves A_x, A_y of Q. Here A_x ≠ A_y because x_{Q_n} ≠ y_n are distinct components.
   - By Lemma 2.2 both are single components, so they are distinct components of Q.
4. So Q has two components ≅ Y_0, contradicting (NT\*). ∎

**Step 2 (uniform separation for small t).** There is t_0 > 0 such that for |t| ≤ t_0 and every Q ∈ K_0, the curve H_t(Q) has exactly one component of type (g_i, n_i) whose class lies in B̄_{2ε}(Y_0), and that component lies in B̄_ε(Y_0). Write λ_t(Q) for its class.

*Proof.* Suppose not. Take t_n → 0 and Q_n ∈ K_0 violating the claim, with Q_n → Q ∈ K_0. Then H_{t_n}(Q_n) → Q, by continuity of H and H_0 = id.

- *Two components in B̄_{2ε}.* Lemma 2.2 and the argument of Step 1 give two distinct components of Q in B̄_{2ε}(Y_0). This contradicts Step 1.
- *None in B̄_ε.* Work in Def(Q).
  1. The path τ ↦ H_τ(Q_n), τ ∈ [0, t_n], has small diameter by uniform continuity of H on compact sets. So it lifts to a path in Def(Q) near 0, by path lifting for finite group quotients (Bredon, *Introduction to compact transformation groups*, II.6, cited from memory).
  2. The whole path lies in one stratum, because H is stratum preserving. Along it, the component that is a smoothing of a fixed connected subcurve A of Q varies continuously.
  3. At τ = 0 the component x_{Q_n} ≅ Y_0 is the smoothing of some A. By Lemma 2.2 and Step 1, A is the single component x_Q.
  4. The A-component of H_{t_n}(Q_n) is close to the A-component at the chart point of H_{t_n}(Q_n), and that point tends to 0. So it converges to x_Q ≅ Y_0, and it lies in B̄_ε(Y_0) for n large. Contradiction. ∎

**Step 3 (λ_t is continuous on K_0 for each fixed |t| ≤ t_0).**
1. Let Q_n → Q in K_0. Then H_t(Q_n) → H_t(Q).
2. By Lemma 2.2, every subsequence of the components realising λ_t(Q_n) has a further subsequence converging to a smooth component of H_t(Q) whose class lies in B̄_ε(Y_0).
3. By Step 2 that component is the one realising λ_t(Q). Hence λ_t(Q_n) → λ_t(Q). ∎

**Step 4 (λ_t takes finitely many values on K_0).** Enlarge F_0 by the finitely many points of K_0 that lie in strata Δ_G with K_0 ∩ Δ_G finite. Call the result F_0′; it is finite. Let Q ∈ K_0 \ F_0′, lying in Δ_G.
1. By (PT), Δ_G is of product type. So ξ_G : ∏M_w → Δ_G is a homeomorphism, the pieces in Δ_G are just the 1-dimensional components of B_0 ∩ Δ_G, and vertex labels are canonical.
2. Since Q ∉ F_0, Q is a smooth point of B_0 ∩ Δ_G on a unique piece D. Its component x_Q is the value at Q of a vertex y_0 of G.
3. Since Q ∉ F_0(iii), y_0 is constant on D, with value ≅ Y_0.
4. Let 𝓦 be the closure of H(D × Δ) in ∏M̄_w × Δ. It is irreducible by Lemma R0 (PR-D). By L1 (§1.1), y_0 is constant on every component of every fibre of 𝓦.
5. D_t = H_t(D) is irreducible (PR-D, Step 1). So y_0 has a single constant value z_{D,y_0}(t) on D_t.
6. The vertex values of H_τ(Q), τ ∈ [0, t], are continuous in τ. By Step 2, for each τ exactly one vertex has value in B̄_{2ε}(Y_0), and that value lies in B̄_ε(Y_0).
7. Hence, for each vertex y, the set {τ : value of y ∈ B̄_ε} equals {τ : value of y ∈ B̄_{2ε}}. It is therefore both closed and open in [0, t]. So the distinguished vertex is y_0 for all τ.
8. Therefore λ_t(Q) = z_{D,y_0}(t).

So λ_t(K_0) is contained in the finite set {z_{D,y}(t)} ∪ {classes of components of H_t(Q′) : Q′ ∈ F_0′}. ∎

**Step 5 (λ_t ≡ Y_t on K_0).**
1. K_0 is connected, and λ_t is continuous (Step 3) with finite image (Step 4). So λ_t is constant on K_0.
2. H_t(P) ∈ ∂V_t by (R2). Its vertex-i component is Y_t.
3. By PR-A, after shrinking t_0, d(Y_t, Y_0) ≤ ε for |t| ≤ t_0. By the uniqueness in Step 2, λ_t(P) = Y_t.
4. Hence **λ_t(Q_0) = Y_t** for |t| ≤ t_0. ∎

**Step 6 (the branch at time t).**

*Setting.*
- Let Q_0 ∈ Δ_{G′}. Let Def(Q_0) be the versal deformation germ, with Aut(Q_0) acting, and smoothing parameters s_e for e ∈ E(G′). Put Q_τ := H_τ(Q_0).
- By (NT\*), every σ ∈ Aut(Q_0) fixes the component x := x_{Q_0}. Indeed σ permutes components preserving isomorphism class, and x is the only component ≅ Y_0.
- Let G_b be the stratum of b \ {Q_0}. Let A′ := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ) and A″ := closure(𝒱) ∩ (closure(Δ_{G′}) × Δ). Both are analytic by (R1), and A″ ∩ (Δ_{G_b} × Δ) = ∅.
- Put N_b := H((b \ {Q_0}) × Δ).

*N_b is a union of irreducible germs of A′.*
1. Since H is a stratum-preserving homeomorphism, near (Q_0, 0) the set N_b is open and closed in A′ \ A″. Its closure is H(b̄ × Δ).
2. An irreducible germ minus a proper analytic subset is connected. So closure(N_b) is a finite union of irreducible 2-dimensional germs W^1, …, W^m of A′ at (Q_0, 0).
3. The τ = 0 fibre of each W^j is of pure dimension 1 (Krull). It is contained in b̄. It is not contained in A″, because b̄ ∩ A″_0 = {Q_0}.
4. Let W̃^j be an irreducible component of the preimage of W^j in Def(Q_0) × Δ.
5. On the connected set W̃^j \ (preimage of A″), the set of edges e with s_e = 0 is locally constant. The loci "exactly S vanish", over subsets S of a fixed size, are disjoint and relatively open. So this set is a constant S_j.
6. At τ = 0 those points lie over b \ {Q_0}. So S_j is the pinched set of a lift σ(b̃) of b, for some σ ∈ Aut(Q_0).
7. Since σ fixes x:
   - in the MERGE case some edge at x is not in S_j;
   - in the MOV case every edge at x is in S_j.

*Limits along b_τ.*
1. Fix τ with |τ| < t_0 (shrunk if necessary), and take R_n ∈ b_τ \ {Q_τ} with R_n → Q_τ. These points lie in N_b.
2. Pass to a subsequence lying in one W^j. Their lifts r̃_n lie in ρ(W̃^j) for a fixed ρ ∈ Aut(Q_0), and converge to a lift q̃ of Q_τ.
3. R_n is the smoothing of q̃ along the edges not in ρ(S_j). Its component containing the deformation of the x-labelled component of q̃ is a smoothing of the connected subcurve A ∋ x spanned by the edges not in ρ(S_j).
4. The x-labelled component of the fibre over q̃ is isomorphic to the one over a continuous lift p_τ (p_0 = 0) of Q_τ, because the relating automorphism fixes x. That one has class close to Y_0 for small τ. By Step 2 its class is λ_τ(Q_0), which equals Y_τ by Step 5.

*Passing to the piece.*
1. Let E be a piece at time τ containing lifts R̂_n of the R_n (finitely many pieces; pass to a subsequence). Let v be the vertex of G_b whose coordinate on R̂_n is the component from item 3 above (fixed after a subsequence).
2. R̂_n converges to ν(p) for some p ∈ Ē. Since Q_τ ∉ Δ_{G_b}, p is a puncture of E.
3. By plumbing continuity (as in Lemma 2.2), f_v(p) = A, pointed by the nodes of Q_τ that leave A. So f_v(p) has the component x(τ) ≅ Y_τ, with its special points.

**Step 7 (conclusion).**
- **MERGE.** A has a node, because some edge at x is not in ρ(S_j). So f_v(p) ∈ ∂M̄_v.
  - f_v is non-constant on E, by Lemma C2: a constant value Z ∈ M_v would have limit Z ∉ ∂M̄_v.
  - So MS6 holds at τ, for every |τ| < t_0.
- **MOV at a puncture.** Here A = {x}, so f_v(p) ≅ Y_τ. It remains to show that f_v is non-constant on E.
  - The vertex receiving x is locally constant on the connected set W̃^j \ (preimage of A″). It equals the MOV vertex at τ = 0.
  - By (PT), G_b is of product type, so vertex labels are canonical. Then E = H_τ(E_b), where E_b is the piece containing b. The family closure(H(E_b × Δ)) is irreducible (Lemma R0).
  - By Lemma 2.1, f_v is non-constant on E for τ outside a discrete set D.
  - So MS6 holds for |τ| < t_0, τ ∉ D. ∎

### 3.4 Remarks on Theorem A
1. **Holomorphy is not used.** The proof never uses that Y is holomorphic. The labels are pinned down by continuity on the connected set K_0, together with finiteness of the label set at a FIXED t (Step 4). In particular Theorem A gives MS6 itself, not only MS6′. It also holds for constant families, where it proves MS6_0 under (K), (NT\*), (PT), (E).
2. **Theorem A gives the problem's claim directly**, without L2, in the MERGE case, provided the vertex v at Q_0 is a Teichmüller vertex satisfying (O). Then f_v(p_τ) ranges in a finite set (L2, or Lemma R\* for v itself), so Y_τ does too, and Y is constant. In general one goes through the chain (§1).
3. **Where each hypothesis is used.**
   - (NT\*) is used in Step 1 (separation), and in Step 6 to make Aut(Q_0) fix x.
   - (PT) is used in Step 4 and in the MOV case of Step 7.
   - (E) is used in Step 7.

### 3.5 Removing (PT) (sketch only, not claimed)
- For a non-product stratum one would replace ∏M_w by Ω_{y} := ∏M_w / Stab_{Aut(G)}(y), the space of points of Δ_G together with a chosen component in the orbit of y. The coordinate p_y is well defined on Ω_y.
- Under (NT\*), at points of K_0 the map Ω_{y_0} → Δ_G is a local homeomorphism near (Q, x_Q). Every automorphism fixing a lift fixes y_0, since x_Q is the only component ≅ Y_0.
- The remaining point is L1 for the sheet (D, x_Q) of the lifted family. One must show that the irreducible family component containing this sheet has no other sheet (D, x′) over τ = 0 on which p_{y_0} is non-constant. That is a monodromy statement about the complement of the ramification locus in the 2-dimensional family. I believe it follows from (NT\*), but I have not written it.

---

## 4. What remains open, and why

### 4.1 Twins (removing (NT\*))
Without (NT\*), Step 1 fails, and λ_t becomes a multivalued function on K_0.
- At a point J ∈ K_0 with two components x, y ≅ Y_0, the continuations x(t) and y(t) can carry different holomorphic labels: z_D(t) from one adjacent STAY piece D, and z_{D′}(t) from another adjacent STAY piece D′.
- The Y_0-network of Proposition K is only "consistent with the path marking". Path markings at a boundary point are defined only up to Aut(J) and the approximating sequence. So the network may jump from x to y at J.
- At time t ≠ 0 the automorphism realising the jump may disappear. Then the copy of Y_t being followed is lost.
- The quintic example (PR-I) shows that such twin points really occur, although on a non-smooth V_0. There the problem's claim is rescued by a different mechanism: the twin sits in a puncture value of a rigid vertex (PR-I, Theorem 4).
- **Open question 1.** Is (NT\*) dispensable? Concretely: at a twin junction J, does one of the following always happen at time t?
  - the Y_t-copy continues along a STAY piece carrying the label Y;
  - the Y_t-copy enters a non-constant vertex at a puncture (that is, MS6).

  The only other possibility is a crossing (4.2). I have no argument.

### 4.2 Crossings (removing (E))
Suppose the endpoint is of type MOV-interior. Then Q_0 ∈ E_b, where E_b is a piece in the stratum of Q_0, and the vertex x is non-constant on E_b with f_x(Q_0) = Y_0. Also, Q_0 lies in the closure of an adjacent STAY piece.

Under (NT\*) and (PT), Steps 1–5 still give λ_t(Q_0) = Y_t. That is:

  **Y_t = f_x^t(H_t(Q_0))**, the value of the non-constant vertex x at the INTERIOR point H_t(Q_0) of the transported piece E_{b,t}.

This is not the MS6 configuration. Nor does it yield rigidity:
- If x is a Teichmüller vertex of E_b satisfying (O), Lemma R\* only gives that Y_t moves inside the fixed curve closure(π_x(E_{b,0})).
- H_t(Q_0) is an uncontrolled point of E_{b,t}.

**A crossing is locally consistent (so no Krull-type argument can exclude it).**
- Take a smooth germ of closure(V_t) with coordinates (σ, ρ).
- Put s_e = ρσ for the edges e at x, and s_f = ρ for the other edges. Let the x-coordinate equal σ.
- Then {ρ = 0} is E_b: all edges are pinched and x moves.
- {σ = 0} is the STAY piece: the edges at x are pinched, the others are smoothed, and x is constant.
- Points with ρσ ≠ 0 lie in M_g.

This is compatible with (R1), (R2), (i) and (ii), at t = 0 and at every t. It is the same phenomenon as in PR-C.

- **Open question 2.** Can Proposition K be sharpened (choice of rays, or of stopping rule) so that its endpoint is never a crossing? Equivalently, for smooth totally geodesic V_0: does every Y_0-network reach a MERGE, or a MOV at a puncture?
- Note that MS6 for constant families (MS6_0, §1.4) requires a positive answer, or an argument that handles crossings differently.

### 4.3 Why I did not transport the Teichmüller rays to time t (a dead end, recorded)
The natural route to removing (NT\*) is to transport the marked ray segments g_s X_n of Proposition K by H_t, and to follow the marked Σ_i along them at time t. Continuity in s of the marked Σ_i-part, together with finiteness of the label set (Step 4), would then remove the ambiguity at twin junctions.

This breaks down for the following reason.
- The marking at H_t(g_s X_n) must be defined by lifting the square (s, τ) ↦ H_τ(g_s X_n) to Teichmüller space.
- The square can meet orbifold points of the moving surfaces V_τ. These are points with extra automorphisms, which (unlike at τ = 0) move with τ and sweep real hypersurfaces of V_0 under H^{-1}. So they cannot be avoided by perturbing the ray.
- The monodromy of the lift around such a point is an automorphism α of a curve close to the boundary. It can send Σ_i to a twin subsurface α(Σ_i). Its part is isomorphic at that moment, but it is continued by a *different* label afterwards.
- So the transported-ray argument meets exactly the twin problem again, now at interior times τ ∈ (0, t).
- Passing to level-N covers does not help. The pull-back to V_0 × Δ of the branched cover M_g[N] → M_g need not be a product, because its branch locus varies with τ.

---

## 5. Summary

**Proved (in this file, modulo the cited results named in each proof):**
- L1 is correct. L2 is correct modulo Imayoshi–Shiga and (O), with caveats (a) and (b) of §1.2 to be written out. The derivation of the problem's claim from MS6 is sound.
- MS6 is stronger than the chain needs. For constant families it contains the V_0-only statement MS6_0. The chain only needs MS6′ ("Y non-constant ⇒ configuration").
- Lemma 2.1: non-constancy of a vertex on a family of pieces persists off a discrete set of t.
- Lemmas 2.2 and 2.3: limits of near-Y_0 components; finiteness of the exceptional set F_0.
- **Theorem A (partial).** Assume (K) (the output of Proposition K, used as a prior result), (NT\*) no boundary point of closure(V_0) has two components ≅ Y_0, (PT) the strata carrying arcs of the network (and G_b in the MOV case) are of product type, and (E) the network ends in a MERGE or a MOV at a puncture. Then MS6 holds for all 0 < |t| < t_0 outside a discrete set (for all such t in the MERGE case), hence also MS6′ and MS6_0. In addition Y_t = λ_t(Q_0) is identified at the endpoint for all small t.

**Sketched only:**
- Removal of (PT) via the spaces Ω_y (§3.5).
- Proposition K itself (PR-H; "modulo routine marking details", not re-proved here).

**Not proved / open:**
- **Open question 1 (twins).** MS6 when some point of B_0 has two components ≅ Y_0.
- **Open question 2 (crossings).** MS6 when the endpoint of every Y_0-network is MOV-interior. This includes the t = 0 statement MS6_0 in that case.
- Inputs outside MS6 that the chain still needs: (O), (F2), and caveats (a) and (b) of L2.

**No counterexample** to MS6 was found. The local models in 4.2 show that any proof must use global information (total geodesy at t = 0, propagated through (R2)), as Theorem A does through the connected set K_0.

=== END OF ANSWER round7_q8 ===
