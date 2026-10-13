# round7_q3 — answer

**Status.** PARTIAL. MS6 is not proved in full, and no counterexample was found.

Proved here:
- **Lemma L1′.** A strengthening of the chain's L1: whether a vertex is constant along a transported piece does not depend on t. I also checked the chain's derivation (L1, L2, steps 1–4); see §4.
- **Theorem A.** MS6 holds, with T a whole disc {|t| < ε}, whenever the t = 0 output of Proposition K (PR-H) meets two conditions:
  - (X) it ends in a *puncture exit*: a MERGE, or a MOV at a puncture of the exit piece;
  - (NT) every junction point on a network arc, and the exit point, has exactly one component isomorphic to Y_0.
- **Lemma B.** What happens at a junction with twins.

Not covered (open): the twin case (NT fails), and the case where Prop K's exit is an *interior* MOV. In the second case MS6 itself is the wrong target (§3.2).

Readings (R1) and (R2) are adopted throughout, as stated in the task.

---

## 0. Conventions

- **Component.** A *component* of a stable curve X means the pointed normalization of an irreducible component of X, with its special points (preimages of nodes and marked points) unordered. Isomorphism classes of such objects of type (g_i, n_i) form the Hausdorff coarse space M′ := M_{g_i,n_i}/S_{n_i}. Fix a metric d on M′. "≅ Y_t" in MS6 means equality in M′.
- **Components move continuously in a stratum.** If X_n → X inside one stratum Δ_G, then the multiset of components of X_n converges to that of X. (Locally Δ_G = (∏_w M_w)/Aut(G), so this is continuity of the coordinates.)
- **Transported pieces.** For a piece D_0 in a stratum Δ_G, put D_t := H_t(D_0). Let 𝓦_D ⊂ ∏M̄_w × Δ be the closure of its lift, as in Lemma R0 of PR-D. When Δ_G is of product type, ξ_G restricted to ∏M_w is a homeomorphism onto Δ_G. Then the fibre (𝓦_D)_t is the closure of the lift of D_t, which is irreducible:
  - 𝓦_D is irreducible of dimension 2, and t is non-constant on it, so every fibre is pure 1-dimensional.
  - A 1-dimensional fibre component cannot lie over the finite set closure(D_t) \ D_t, because ξ̄_G is finite.
  - For non-product strata I use the chain's own standing convention: a chosen lifted component, as in L1. Theorem A is fully rigorous only when the pieces D^k and E used below lie in product-type strata, or under that convention.

## 1. Lemma L1′ (constancy is independent of t). Proved.

**Lemma L1′.** Let 𝓦 be an irreducible 2-dimensional closed analytic subset of ∏M̄_w × Δ that is proper over Δ, with t non-constant on it. Let u be a vertex. Suppose that for some t_0, pr_u is constant on some 1-dimensional component of 𝓦_{t_0} with value in M_u. Then:
1. pr_u is constant on every component of every fibre 𝓦_t, t ∈ Δ;
2. the set Γ_u := (pr_u, t)(𝓦) is an irreducible analytic curve, finite over Δ;
3. in particular, for every δ > 0 there is ε > 0 such that, for |t − t_0| < ε, every value of pr_u on 𝓦_t lies within δ of the value at t_0.

*Proof.*
1. Assume first that pr_u is constant on all of 𝓦_{t_0}, with value Z ∈ M_u. Take an affine open set U ∋ Z of the quasi-projective coarse space M_u.
2. The map pr_u is continuous and 𝓦 is proper over Δ. Hence pr_u(𝓦_t) ⊂ U for |t − t_0| small.
3. A holomorphic map from a compact connected analytic curve to an affine variety is constant. So pr_u is constant on each fibre component for t near t_0.
4. Therefore the proper holomorphic map Φ = (pr_u, t) : 𝓦 → M̄_u × Δ has fibres of positive dimension over a nonempty open set of the irreducible space 𝓦.
5. Its image Γ_u is irreducible and analytic (Remmert), and has dimension ≤ 1. It projects onto Δ non-constantly, so it is a curve finite over Δ.
6. Each fibre 𝓦_t is a compact curve mapping into the finite set Γ_u ∩ {t}. So pr_u is constant on each of its connected components, for every t.
7. Item 3 follows from the properness of Γ_u → Δ.

If pr_u is constant on only one component C of 𝓦_{t_0}: in the situation of §0 the fibre is irreducible, so C is the whole fibre. In general, apply the argument to a neighbourhood of C, which is still proper over a small disc. ∎

The chain's L1 is the case t_0 = 0. **L1 is correct.** L1′ adds that a vertex non-constant on E_0 is non-constant on every E_t, and conversely.

## 2. Theorem A (MS6 for a disc of t, under (X) and (NT)). Proved, modulo cited prior results.

**Prior results used.**
- **Prop K (PR-H §3; cited, not re-proved).** Fix a generic P ∈ ∂V_0. There are:
  - a compact connected set K_0 ⊂ B_0 := closure(V_0) \ V_0, containing P, at every point of which the path-marked subsurface Σ_i is pinched off and its component is the smooth curve Y_0;
  - a point Q_0 ∈ K_0 and a branch b of B_0 at Q_0, of type MERGE or MOV.
- **Lemma C2 (PR-C).**
- **The germ argument (PR-J, Theorem P″, Step 2; cited).** I re-checked its logic. Let b be a branch at Q_0 of a piece E, with lifted limit R^b_0. Then the limits R^b_t of the lifts of the transported branches b_t = H_t(b) converge to R^b_0 as t → 0.

**Network arcs.**
- B_0 is a compact 1-dimensional analytic set, so it is a finite graph after triangulation.
- A compact connected subset of a finite graph is a finite connected subgraph, after subdividing. So K_0 contains an arc α from P to Q_0.
- Subdivide α at finitely many points J^1, …, J^m so that each open sub-arc α_k lies in a single piece D^k (a 1-dimensional irreducible component of B_0 ∩ Δ_{G_k}).
- For generic P, B_0 = ∂V_0 near P, so D^0 ⊂ ∂V_0.
- On α_k the subsurface Σ_i is exactly one vertex u_k of G_k, with value Y_0.
- A holomorphic function on the normalization of D^k that is constant on a real arc is constant. So u_k is constant on all of D^k, with value Y_0. For D^0 this vertex is u_0 = i.
- Put J^{m+1} := Q_0. Then J^k ∈ closure(D^{k−1}) ∩ closure(D^k).

**Hypotheses.**
- **(X)** The branch b given by Prop K is either
  - a MERGE; or
  - a MOV with Q_0 ∉ E, where E is the piece containing b and Q_0 is a puncture of E.
- **(NT)** Each J^k (k = 1, …, m+1) has exactly one component isomorphic to Y_0, i.e. exactly one component equal to Y_0 in M′.

**Theorem A.** Assume (R1), (R2), the problem's hypotheses, total geodesy of V_0, the conclusions of Prop K, and (X) and (NT) for one network arc. Then there is ε > 0 such that MS6 holds at every t with |t| < ε. So T = {|t| < ε} works.

*Proof.*

1. **Exit at t = 0.** Let p be the point of Ē (the normalized closure of E) given by b. Let v be the vertex of G_b that contains Σ_i.
   - **MERGE.** Some edge at Σ_i is pinched at Q_0 but not along b. So Q_0 lies in a deeper stratum than b \ {Q_0}, Q_0 ∉ E, and p is a puncture of E.
     - By Lemma C2, f_v is non-constant on E.
     - f_v(p) = R^b_{0,v} is the gluing of the components of Q_0 contracted into v. It contains Y_0.
   - **MOV with Q_0 ∉ E.**
     - ∂Σ_i stays pinched along b and the limit at Q_0 is the smooth curve Y_0. So Σ_i is a vertex v of G_b.
     - f_v is non-constant on E, and f_v(p) ≅ Y_0, which is itself a component.

2. **Transport.** Put J^k_t := H_t(J^k), D^k_t := H_t(D^k), E_t := H_t(E), b_t := H_t(b), Q_t := J^{m+1}_t.
   - H preserves strata and closures. So J^k_t ∈ closure(D^{k−1}_t) ∩ closure(D^k_t), D^0_t ⊂ ∂V_t, E_t ⊂ Δ_{G_b}, and Q_t ∉ E_t.
   - So b_t gives a puncture p_t of E_t. (Branches correspond under H_t; PR-D Step 2.)
   - By L1′, v is non-constant on E_t, and u_k is constant on D^k_t, with value z_k(t).
   - z_0(t) = Y_t, because D^0_t ⊂ ∂V_t.

3. **Each z_k(t) is a component of J^k_t and of J^{k+1}_t, close to Y_0.**
   - The fibre (𝓦_{D^k})_t maps onto closure(D^k_t) (§0: ξ̄ × id is proper and the image contains the transported family). So there is a point R over J^k_t on it.
   - pr_{u_k} is constant on that fibre (L1′, §0), so R_{u_k} = z_k(t) ∈ M_{u_k}. This is a smooth vertex curve of a point over J^k_t, hence a component of J^k_t. The same holds at J^{k+1}_t.
   - By L1′(3), d(z_k(t), Y_0) < δ for |t| < ε.

4. **Uniqueness near Y_0.**
   - By (NT), J^k has exactly one component ≅ Y_0. Let δ be less than half the distance in M′ from Y_0 to the other components of type (g_i, n_i) of all the J^k.
   - J^k_t → J^k inside the stratum of J^k. By §0, for |t| < ε, J^k_t has exactly one component w_k(t) within δ of Y_0.
   - By Step 3, z_{k−1}(t) = w_k(t) = z_k(t) in M′.
   - Hence Y_t = z_0(t) = z_1(t) = … = z_m(t) = w_{m+1}(t) in M′.

5. **The exit at time t.**
   - By the germ argument, f_v^t(p_t) = R^{b_t}_v → R^b_{0,v} = f_v(p) as t → 0.
   - f_v^t(p_t) is a gluing of components of Q_t, and there are finitely many combinatorial types. Pass to subsequences of fixed type. Gluing maps are continuous, and the components of a stable curve are well defined. So the components of f_v^t(p_t) converge, as a multiset, to those of f_v(p).
   - f_v(p) contains Y_0 (Step 1). Hence for |t| < ε (after shrinking ε) f_v^t(p_t) has a component within δ of Y_0.
   - That component is a component of Q_t, so by Step 4 it is w_{m+1}(t), which is ≅ Y_t.

6. **Conclusion.** For |t| < ε, the data (E_t, v, p_t) satisfy MS6:
   - E_t is a piece at time t (PR-D Step 1);
   - f_v is non-constant on it;
   - f_v(p_t) has a component ≅ Y_t. ∎

**Remark.** Theorem A uses neither path markings at time t nor any choice of lifts at junctions. The identification at each junction comes from (NT) plus continuity alone. Combined with the chain (§4), it gives the problem's conclusion whenever (X), (NT), (O) and (F2) hold.

## 3. What remains: the two uncovered cases

### 3.1 Twins at a junction (NT fails)

**Lemma B (dichotomy at a twin junction).** Fix small t ≠ 0, and suppose the configuration of MS6 does not occur at time t. Let J := J^k have Y_0-components x_1, …, x_r with r ≥ 2. Their continuations in J_t are w_1(t), …, w_r(t). Suppose z_{k−1}(t) = w_1(t) ≅ Y_t, but z_k(t) = w_2(t).

Along a branch of D^k_t at J_t, the vertex of G_J carrying w_1(t) is of one of three kinds:
- (a) an isolated constant vertex of D^k_t. Then D^k has, at t = 0, a *second* constant vertex with value Y_0, and the Y_t-copy continues along D^k_t through this "twin route";
- (b) merged along D^k_t, with J_t a puncture of D^k_t. Then MS6 holds at t, by Lemma C2 at time t, since merges are combinatorial and preserved by H_t;
- (c) a non-constant vertex of D^k_t with J_t ∈ D^k_t: an interior MOV.

*Proof.*
- The pinching pattern of a branch is combinatorial, so it is the same at times t and 0 up to an automorphism of J_0 permuting the x_j.
- Constancy is t-independent (L1′).
- Distinct vertices of G_{D^k} land on disjoint sets of vertices of G_J. This gives the count in (a). ∎

So with twins, the Y_t-class follows at time t a "twisted network": at junctions the copy may jump to a twin. Prop K controls only the untwisted network, the one traced by Teichmüller rays with a fixed path-marked Σ_i. I could not show that a twisted network must reach a MERGE or a puncture MOV.

The quintic example (PR-I) shows twins really occur, and there the twin route itself gives MS6. A general argument would need a Prop K for twisted networks, or an invariant count of Y_0-copies. Neither is available.

### 3.2 Interior MOV exit (MS6 is the wrong target there)

Suppose Prop K's exit has Q_0 ∈ E, i.e. Q_0 lies in the same stratum as b. Then:
- v = Σ_i is a vertex of type (g_i, n_i) moving through Y_0 at an interior point.
- No puncture value f_v(p) can contain Y_0. A nodal curve of type (g_i, n_i) has no component of that type, and a smooth puncture value is a single curve, equal to Y_0 only by accident.

So this exit gives no MS6 configuration. If, for some admissible V_0, every exit of every network were of this kind (and no twin or other mechanism gave a copy), then:
- the *trivial* family V_t ≡ V_0 would be a counterexample to MS6, since there MS6 reduces to the t = 0 statement;
- it would not be a counterexample to the problem.

I can neither exclude this nor build such a V_0. Known smooth totally geodesic surfaces are too scarce to test by hand.

Possible repair of the chain (sketch only, not proved): use L2 at Q_t. It gives f^t ∘ A_t = f^0 on the non-constant vertices of E_t, so Y_t lies on the fixed curve closure(π_v(E_0)). Then intersect with the transported STAY piece through Q_t to obtain finiteness. This needs a vertex non-constant on both pieces, with distinct image curves.

### 3.3 Counterexample

None found. By §3.2, a counterexample would need either a V_0 whose Y_0-networks exit only through interior MOVs (and twin routes that also fail), or a non-trivial deformation family. I could not construct either while checking smoothness and total geodesy.

## 4. Check of the chain (L1, L2, derivation)

- **L1.** Correct; proof in §1. It is fully rigorous for product-type strata, where Lemma R0 (PR-D) holds as stated.
  - **Caveat on R0 for non-product strata.** R0's claim that 𝓦^{(a)} is irreducible (via connectedness of N^{(a)}) fails if one takes the full preimage under a non-injective ξ_G. Aut(G)-translates of the lift may then appear. One must use a chosen lifted component, and check that its fibre over 0 does not contain two translates on which different vertices are constant. This is not done anywhere in the chain.
- **L2.** The argument is sound modulo (O). But there is a gap the chain does not list:
  - The homotopy class of g_t = f_u^t ∘ A_t is an orbifold class for the vertex u. The orbifold structure Λ_t comes from the Teichmüller vertex v. f_u need not lift to T_u over that structure: the cone points needed by u may differ.
  - So an (O)-type condition is needed for every non-constant vertex u, not only for v. Alternatively, a uniform finite (level) cover of Ē_t whose branch data are transported by Ĥ_t.
  - With that added, Imayoshi–Shiga gives the finite set F(E_0, u) as claimed.
- **Derivation steps 1–4.** I found no flaw beyond the two caveats above, plus the dependence on (O) and (F2) that the chain already lists. Step 4's appeal to L1 is correct, and L1′ makes it two-sided.

## 5. Summary

**Proved:**
- L1′: constancy of a vertex along transported pieces is independent of t.
- Theorem A: MS6 on a disc |t| < ε, under (X) and (NT). It relies on Prop K, Lemma C2 and PR-J's germ argument, which are cited, not re-proved.
- Lemma B: the dichotomy at twin junctions.

**Flaws or caveats in the chain:**
- L2 needs (O) for every non-constant vertex u.
- Lemma R0's irreducibility claim needs care for non-product strata.

**Open:**
1. MS6 when (NT) fails, i.e. twisted networks.
2. MS6 when every exit is an interior MOV. MS6 may then simply be false, already at t = 0 for the trivial family. If so, the chain should replace MS6 by a statement that also allows interior MOV exits (§3.2).
3. Whether the problem's claim can bypass MS6 in these cases.

=== END OF ANSWER round7_q3 ===
