# round8_q9 answer

## Plan (written first)
Target: (PE-NH), or zero topological entropy by any route. After reading the brief, I take as given: Theorem J; Theorem G of R7-a (finite configurations, "more points than classes"); and the standard fact limsup_{t->inf} sup_x J_t(x)/t = max_m m(d).
New idea tried: produce the cycles that Theorem G needs by a topological dimension count (invariance of domain / Hurewicz) applied to the "su-walk map". This needs strong leaves through every point of an open set, which is available for uniformly partially hyperbolic flows but not in Pesin theory. A second idea is a measure-valued ("smeared") form of Theorem G.

Status: I did NOT prove (PE-NH) or the full problem. What is proved is below (Sections 1-3); Section 4 says exactly where the argument stops.

## 0. Conventions
These are as in the brief: nu is a smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P phi = X phi + d phi, and F_phi(t) = S(e^{J_t} phi o g_t) for a distribution density S. Theorem J (R6-a §2) is used as proved: under GH, if |F_phi(t)| <= C e^{-eps|t|} ||phi||_{C^k} for all real t and all phi, then S = 0.

## 1. A measure-valued form of Theorem G (proved; GH + Theorem J only)

**Proposition MG.** Assume GH. Let K ⊂ M be a Borel set and m a finite positive Borel measure on K. Let ξ^s and ξ^u be partitions of K that are measurable for m, with disintegrations m = ∫ m_A dm̂^s(A) = ∫ m_B dm̂^u(B), where the m_A, m_B are probabilities on the elements. Let C, θ > η >= 0 be constants such that:
 (S) if z, z' lie in one ξ^s-element, then d(g_t z, g_t z') <= C e^{-θ t} for t >= 0;
 (U) if z, z' lie in one ξ^u-element, then d(g_t z, g_t z') <= C e^{-θ|t|} for t <= 0;
 (R) J_t(z) <= C + η|t| for all z in K and all real t.
For z, z' in one ξ^s-element put β^s(z,z') := lim_{t->+inf}(J_t z - J_t z'). The limit exists: the derivative of J_t z - J_t z' in t is bounded by Lip(d) C e^{-θ t}. Moreover |J_t z - J_t z' - β^s(z,z')| <= K e^{-θ t} for t >= 0, with K = Lip(d) C/θ. Define β^u for t -> -inf in the same way. Both satisfy the cocycle rule β(z,z'') = β(z,z') + β(z',z'').
Let w be in L^inf(m) such that, for m̂^s-a.e. A and some (hence, by the cocycle rule, every) a in A,
 ∫_A w(z) e^{β^s(z,a)} dm_A(z) = 0,
and, for m̂^u-a.e. B and b in B,
 ∫_B w(z) e^{β^u(z,b)} dm_B(z) = 0.
Then w = 0 m-a.e.

*Proof.* Let S := w m, a finite signed measure and so a distribution density of order 0.
- *t >= 0.* For fixed A and any a in A, the hypothesis gives ∫_A w(z) e^{J_t(a) + β^s(z,a)} φ(g_t a) dm_A(z) = 0. Averaging over a in A with respect to m_A, we get
 ∫_A w e^{J_t} φ o g_t dm_A = ∫_A ∫_A w(z) [ e^{J_t z} φ(g_t z) - e^{J_t a + β^s(z,a)} φ(g_t a) ] dm_A(z) dm_A(a).
- The bracket equals e^{J_t a} [ e^{J_t z - J_t a} φ(g_t z) - e^{β^s(z,a)} φ(g_t a) ]. We have |J_t z - J_t a - β^s| <= K e^{-θt}, |β^s| <= K, and |φ(g_t z) - φ(g_t a)| <= ||φ||_{C^1} C e^{-θt}. So the bracket is at most e^{J_t a} C_1 e^{-θ t} ||φ||_{C^1}, where C_1 depends only on C, K. By (R), this is at most C_2 e^{-(θ-η)t} ||φ||_{C^1}.
- Integrating over A gives |F_φ(t)| = |∫ w e^{J_t} φ o g_t dm| <= C_2 ||w||_inf m(K) e^{-(θ-η)t} ||φ||_{C^1} for t >= 0.
- *t <= 0.* The same argument with ξ^u, (U), β^u and (R) gives the same bound with |t|.
Theorem J (k = 1, eps = θ - η), applied to Re S and Im S, gives S = 0. A finite signed measure that vanishes on C^inf vanishes, so w = 0 m-a.e. ∎

*Remarks.*
- The case where m is counting measure on a finite set is Theorem G of R7-a: the conditions on w are the equations (G).
- In the volume-preserving case (ν = ω invariant), d = 0, so all β vanish and (R) holds with η = 0. The conditions then say: E_m[w | ξ^s] = 0 and E_m[w | ξ^u] = 0. **So under GH plus volume, L^2(m, σ(ξ^s)) + L^2(m, σ(ξ^u)) is dense in L^2(m) for every such (K, m, ξ^s, ξ^u).**
- For a hyperbolic μ, local product structure on a Pesin block makes m ≈ (marginal) ⊗ (marginal), and a product w = f(s-index) g(u-index) with mean-zero factors works. This gives another proof of Theorem 5.1 of R6-a that does not use horseshoes. For non-hyperbolic μ, see §4.

## 2. GH excludes uniform partial hyperbolicity (proved, modulo cited classical theorems)

**Definition.** X is *partially hyperbolic* if there are a continuous Dg_t-invariant splitting TM = E^s ⊕ E^c ⊕ E^u with X in E^c, dim E^s >= 1 and dim E^u >= 1, and constants C >= 1, θ > 0, θ' > 0, such that for t >= 0:
- ||Dg_t|E^s|| <= C e^{-θt} and ||Dg_{-t}|E^u|| <= C e^{-θt};
- ||Dg_t|E^s(x)|| · ||Dg_{-t}|E^c(g_t x)|| <= C e^{-θ' t}, and symmetrically for E^u with t replaced by -t (domination).
Anosov flows are included (E^c = RX).

**Cited [HPS]** (Hirsch–Pugh–Shub, strong stable manifold theorem, from memory). For such a flow there are continuous foliations W^{ss}, W^{uu} with C^1 leaves tangent to E^s, E^u. "Continuous" means the following: around every x0 there are a chart φ: V -> R^n with E^u(x0) = R^u × 0, a neighbourhood V0 of x0 and ρ > 0, such that for a in V0 the plaque of W^{uu}(a) through a is, in the chart, the graph of a C^1 map h_a over the ball B^u(π(a), ρ), with (a, v) -> h_a(v) continuous. The same holds for W^{ss} with E^s(x0). Leaves are tangent to E^s, so a C^1 path in a leaf is contracted: d(g_t y, g_t z) <= d_{W^{ss}}(g_t y, g_t z) <= C e^{-θt} d_{W^{ss}}(y,z) for y in W^{ss}(z) and t >= 0. Likewise for W^{uu} with t <= 0.

**Cited [Hu]** (Hurewicz's theorem on closed maps, from memory). If f: X -> Y is a closed continuous map of separable metric spaces, then dim X <= dim f(X) + sup_y dim f^{-1}(y) (covering dimension). Also used: dim of a closed ball in R^D is D, and every subset of an n-manifold has dim <= n.

**Lemma W (graphs).** Let G be a finite connected multigraph without loops, and let E - V + 1 <= 1 be its cyclomatic number. Then for vertices s, t and a length L there are at most 3 non-backtracking walks of length L from s to t. (Non-backtracking: consecutive edges are distinct.)
*Proof.*
1. *Trees.* In a tree a non-backtracking walk is a path. Suppose a vertex repeats, v_i = v_j with j - i minimal. Then j - i = 1 is a loop, which is impossible. j - i = 2 needs two distinct edges between v_i and v_{i+1}, which is impossible in a tree (equal edges would be backtracking). j - i >= 3 gives a cycle. Paths between two vertices of a tree are unique, so there is at most 1 walk.
2. *Unicyclic graphs.* If E - V + 1 = 1, let C be the unique cycle; it may have length 2, i.e. a pair of parallel edges. G minus the edges of C is a forest, and each of its components T_c contains exactly one vertex c of C.
   - A non-backtracking walk that uses no edge of C lies in one T_c, so by step 1 it is the unique path from s to t.
   - Otherwise, consider any maximal sub-walk between two cycle edges. It lies in a single T_c, and it starts and ends at c, because c is the only vertex of T_c incident to cycle edges. A non-backtracking walk in a tree from c to c has length 0 (step 1). So all cycle edges used are consecutive.
   - Every cycle vertex has exactly two cycle edges. So the cycle part of the walk is determined by its first edge, which is one of the 2 cycle edges at the entry vertex c1, together with its length.
   - The part before the cycle is the tree path from s to c1, where c1 is the root of the component of s. The part after it is the tree path from c2 to t, where c2 is the root of the component of t. So the length of the cycle part is L - d(s,c1) - d(c2,t), which is determined.
   - Hence there are at most 2 walks of this kind, and at most 3 walks in all. ∎

**Theorem U.** Assume GH. Then X is not partially hyperbolic with |m(d)| < θ for every flow-invariant probability m. In particular, **a GH vector field preserving a smooth positive density is not partially hyperbolic** (take ν = ω, so that d = 0).

*Proof.* Suppose X is partially hyperbolic and max_m |m(d)| < η < θ. (The maximum is attained, since m -> m(d) is continuous and affine on a compact set.) Let u = dim E^u, s = dim E^s, n = dim M.

*Step 1 (uniform growth bound).* By the standard fact (R4-q7 Prop 2.1, step 1), limsup_{t->+inf} sup_x J_t(x)/t = max_m m(d) < η. The same fact for the reversed flow gives limsup_{t->+inf} sup_x J_{-t}(x)/t = max_m(-m(d)) < η. Hence J_t(x) <= C_0 + η|t| for all x and all real t. So (R) of Proposition MG holds for every point.

*Step 2 (the walk map).* Fix x0 and the chart, V0 and ρ of [HPS] (for both foliations). Define Φ^u_a(v) := φ^{-1}(π(a) + v, h_a(π(a)+v)) for |v| < ρ, and Φ^s_a(w) in the same way. These are continuous in (a, v), injective in v, and Φ_a(0) = a. Fix k with k(u+s) >= n+1. For a parameter vector P = (v_1, w_1, ..., v_k, w_k) put
 a_0 = x0, a_{2i-1} = Φ^u_{a_{2i-2}}(v_i), a_{2i} = Φ^s_{a_{2i-1}}(w_i).
By continuity there is a neighbourhood N0 of 0 in R^D, D = k(u+s), on which all a_j lie in V0. Let B be a closed ball contained in {P in N0 : all v_i ≠ 0, all w_i ≠ 0}, which is open and nonempty. Put F(P) := a_{2k}. F is continuous on the compact set B, hence closed. The point sequence (a_0, ..., a_{2k}) determines P, because v_i = π(a_{2i-1}) - π(a_{2i-2}) and similarly for w_i.

*Step 3 (four walks with a common end).* If every fibre of F|B had at most 3 points, [Hu] would give D = dim B <= dim F(B) <= n, a contradiction. So there are a point z and four distinct parameter vectors P^1, ..., P^4 in B with F(P^r) = z.

*Step 4 (the class graph).* Let Γ be the bipartite multigraph whose vertices are the global leaves of W^{ss} and of W^{uu}. Its edges are the points of M: the point y joins W^{ss}(y) and W^{uu}(y).
- For a parameter vector P, the edges a_0, a_1, ..., a_{2k} form a walk of length 2k+1 from the vertex W^{ss}(x0) to the vertex W^{uu}(z). Indeed a_{2i-1} and a_{2i-2} share their uu-leaf, and a_{2i} and a_{2i-1} share their ss-leaf.
- This walk is non-backtracking, because a_{j+1} ≠ a_j (the v_i, w_i are nonzero and the Φ are injective).
- The four walks are distinct (Step 2). Let U be the finite subgraph formed by their edges and vertices. It is connected, since all walks start at x0, and it has no loops.
- By Lemma W, U has cyclomatic number >= 2, i.e. #edges >= #vertices + 1.

*Step 5 (contradiction).* Let Z be the edge set of U (finitely many distinct points). The stable classes are the ss-vertices of U, and the unstable classes are its uu-vertices. Every point of Z lies in exactly one class of each kind. Then:
- (S) and (U) of Proposition MG hold with m the counting measure on Z: points in a class lie on one global strong leaf at finite leaf distance, and [HPS] gives d(g_t y, g_t y') <= C d_leaf(y,y') e^{-θ|t|} on the relevant half-line.
- (R) holds by Step 1.
- The equations of Proposition MG (= the equations (G)) form a homogeneous linear system with #Z unknowns and #vertices < #Z equations, so it has a nonzero solution w.
Proposition MG gives w = 0, a contradiction. ∎

*Remark (the volume case needs only invariance of domain).* If ν = ω is invariant, then all β = 0. A single cycle in Γ then already gives a solution (alternating signs ±1 around the even cycle; this is item (c) of R7-a). It is enough that F|B is not injective, which follows from invariance of domain because D > n. Two distinct walks with the same ends contain a cycle made of their edges (by step 1 of Lemma W, applied to a forest).

*Remark (scope).* By Yomdin's theorem (C^inf: h_top >= the exponential growth rate of volumes of discs; cited from memory), partially hyperbolic flows have h_top >= the growth rate of uu-discs > 0. So Theorem U excludes a class of positive-entropy flows outright, in every dimension, without Pesin theory or horseshoes. It is a statement about a sub-class of vector fields, so by the task's rules it does NOT answer (PE-NH).

## 3. Two further corollaries (proved)

**Corollary E (no two-sided exponential decay of a density).** Assume GH. There is no nonzero w in L^1(ν) with |∫ (w o g_{-t}) φ dν| <= C e^{-ε|t|} ||φ||_{C^k} for all real t and all smooth φ.
*Proof.* Let S = wν. Since ∫ ψ o g_t e^{J_t} dν = ∫ ψ dν (change of variables), F_φ(t) = ∫ w e^{J_t} φ o g_t dν = ∫ (w o g_{-t}) φ dν. Apply Theorem J. ∎
In the volume case (ν = ω, J = 0) this says: under GH no nonzero (mean-zero) w in L^1 has correlations ∫ w · φ o g_t dω decaying exponentially, uniformly in C^k norms. So GH + volume rules out exponential mixing of any nonzero mean-zero density. By Theorem J*, it also rules out mixing at any quasi-analytic rate.

**Corollary U' (dimension 4 and up, partially hyperbolic positive-entropy measures).** This is contained in Theorem U. A GH flow with a smooth invariant volume has no continuous invariant splitting of the above kind on M. Note: under GH any invariant compact set with nonempty interior is M (Lemma D of R7-d), so "partially hyperbolic on an invariant set with interior" is the same thing.

## 4. Why this does not reach (PE-NH): the precise stopping point

For a non-hyperbolic ergodic μ with h_μ > 0 and μ(d) = 0, the same scheme needs one of the following.

(a) *Finite version (Theorem G / Step 3 of Theorem U).* The walk map is now defined only on parameters whose vertices are Pesin-regular. It is continuous only on Pesin blocks: compact sets of positive measure, which in general have topological dimension 0, e.g. fat Cantor sets.
- So neither invariance of domain nor Hurewicz applies. A continuous injection of a 0-dimensional compact set of positive D-dimensional measure into R^n with D > n exists.
- Hölder continuity of Pesin holonomies gives only upper bounds on the dimension of images, not the lower bound that injectivity would contradict.
- So the dimension-count mechanism of Theorem U, which is new here, works exactly when strong leaves pass through every point of an open set with continuous dependence, i.e. in the uniform case.

(b) *Measured version (Proposition MG).* One needs a nonzero w in L^inf(m) on a Pesin block whose (twisted) conditional expectations vanish on both the local stable and the local unstable partitions. Write ρ for the image of m under z -> (s-plaque, u-plaque) in Y_s × Y_u. Then:
- If ρ is not singular with respect to ρ_s ⊗ ρ_u, then w = f(y_s) g(y_u)/k works (k the density), as in the hyperbolic case.
- For non-hyperbolic μ, generic s- and u-plaques do not meet, so ρ is singular. The existence of w becomes a kernel question for a "Radon-type" transform between L^2(Y_u) and functions on Y_s.
- Heuristically the kernel is huge in the volume case: w depends on n variables, and the constraints are functions of n - s and n - u variables. But I could not prove it with only measurable (Pesin) regularity of the plaque families. Abstract measure theory alone cannot decide it: two sub-σ-algebras with non-atomic fibres can have L^2-dense sum.
- For singular measures μ (conditional dimensions small), the dimension count heuristically goes the wrong way (R7-f).

So the open statement, in its sharpest form found here, is:

**(MG-ex), open.** For every ergodic non-hyperbolic μ with h_μ(g_1) > 0 and μ(d) = 0 there are a Pesin block K, a finite measure m on K (μ_K, or any other) with subordinate measurable partitions into local stable / local unstable plaques, and a nonzero bounded w satisfying the twisted conditional-expectation equations of Proposition MG.

By Proposition MG, (MG-ex) implies (PE-NH) for μ(d) = 0. Together with Prop N / 6.1 and the conditional Prop 6.2, it would give the problem modulo the large-|μ(d)| case (R1).

**Status of the chain.** I re-read entry 60 (Theorem 5.1) and step 4 (variational principle via flow-ergodic decomposition). I found no flaw.

## Summary
- **Proved:**
  - Proposition MG (measure-valued form of Theorem G; GH + Theorem J).
  - Theorem U: under GH, X is not partially hyperbolic whenever |m(d)| < θ for all invariant m; in particular no volume-preserving GH flow is partially hyperbolic. This is a positive-entropy class excluded in every dimension. The proof is new: a dimension count via Hurewicz on the su-walk map, plus a graph lemma, plus Theorem G. It cites [HPS] and [Hu].
  - Corollary E: no density with two-sided exponential (transfer-operator) decay; under volume, no exponentially mixing smooth/L^1 observable.
- **Not proved:** (PE-NH) and hence the problem in dimension >= 4 for general GH fields.
- **Open questions:** (MG-ex) above; equivalently, the existence of two-sided cancelling (measured) configurations for non-hyperbolic positive-entropy measures. The case (R1) also remains open.

=== END OF ANSWER round8_q9 ===
