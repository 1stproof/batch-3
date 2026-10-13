# round14_q6: answer

## Summary of outcome
(SC) is **not** settled in general.

What is proved:
- **Theorem 1.** (SC) holds whenever mu is hyperbolic, meaning that its only zero Lyapunov exponent (for g_1) is the flow direction. In particular (SC) holds whenever n <= 3; for n = 2 its hypotheses are never met. The proof cites, from memory, the Katok horseshoe theorem for flows with control of the periodic orbits.
- **Lemma 2.** A measure-theoretic statement drawn from the Ledrappier-Young / Pinsker picture: for mu-a.e. x, the support of the Pinsker conditional measure contains points of W^s_loc(x) and of W^u_loc(x) other than x.
- **Proposition 3.** A reduction: (SC) follows from a metric closedness property (CL) of summable-chain accessible sets.

The planner's route, step by step:
- It fails at the step "mod 0 implies metric". Section 4 states the exact place.
- For a general (non-SRB, non-hyperbolic) mu, s-holonomy is not absolutely continuous with respect to the u-conditional measures. So every statement that the Pinsker coincidence yields is about mu-conull sets of base points. (SC), however, asks for a point inside a set that is null for the relevant conditional measures: the weak-stable plaque, met by a chain that does not pass through the orbit of its own limit. A mod-0 statement can never supply such a point. The two missing ingredients are local product structure and closedness.
- No counterexample to (SC) was found. Section 5 checks the natural candidates (product and skew-product extensions of contact Anosov flows, constant-roof suspensions); all of them satisfy (SC).

Conventions are as in the task. Pesin data are for f = g_1. "Cited" means cited from memory.

---

## 1. Theorem 1 (hyperbolic measures; proved modulo cited classical results)

**Cited results.**
- [Ru] Ruelle's inequality: for a C^1 diffeomorphism f and an ergodic f-invariant mu, h_mu(f) <= sum of the positive exponents.
- [SM] Stable manifold theorem for a hyperbolic periodic orbit gamma of a smooth flow (period P, and X != 0 on gamma). Let chi_s > 0 (resp. chi_u > 0) be the smallest modulus of the stable (resp. unstable) Floquet exponents, i.e. log|eigenvalue|/P. For every delta > 0 and q in gamma, the strong stable manifold W^{ss}(q) is an injectively immersed submanifold with the following properties:
  - Every y in W^{ss}(q) satisfies d(g_t y, g_t q) <= C_{y,delta} e^{-(chi_s - delta) t} for t >= 0. If y is in a fixed local disc W^{ss}_loc(q), the constant can be taken to be C_delta d(y, q). For general y in W^{ss}(q), one pushes forward into the local disc: for t in [0, T] Lipschitz bounds give a factor e^{LT}, and the constant then depends on the pair.
  - W^s(gamma) = union over r of W^{ss}(g_r q), and g_r W^{ss}(q) = W^{ss}(g_r q).
  - The same holds for W^{uu}, chi_u and t <= 0.
- [KH] Katok's horseshoe theorem, flow version, with periodic-orbit approximation. References from memory: Katok 1980 (Publ. IHES 51), covering flows in dimension 3; Lian-Young (2012) for C^2 flows in any dimension; for the exponent approximation, Wang-Sun (Trans. AMS 2010) for diffeomorphisms, the flow analogue being standard. Statement: let mu be an ergodic invariant probability of a C^2 flow with h_mu(g_1) > 0, mu(Zero X) = 0, and all exponents other than the flow-direction one nonzero. Let chi_min > 0 be the smallest modulus of a nonzero exponent. Then for every eps > 0 there is a compact invariant hyperbolic set Lambda on which the flow is topologically conjugate to the suspension (continuous positive roof) of a transitive subshift of finite type of positive entropy. Moreover the following hold.
  - (a) Every periodic orbit gamma in Lambda has |(1/P) int_gamma phi - int phi dmu| < eps for a fixed finite set of continuous functions phi, in particular phi = d.
  - (b) All Floquet exponents of gamma transverse to X have modulus >= chi_min - eps.

  **Flag:** part (b), and the joint validity of (a), (b) inside one horseshoe, is how I remember the Katok-Mendoza / Wang-Sun refinements. I have not rechecked the flow version.

**Theorem 1.** Assume the hypotheses of (SC), and that mu is hyperbolic (the flow direction is its only zero exponent). Then the conclusion of (SC) holds.

**Proof.**

0. *Preliminaries.*
   - mu(Zero X) = 0. Otherwise ergodicity puts mu on the closed invariant set Zero X, where g_1 = id, and h_mu = 0.
   - int J_1 dmu = int_0^1 int d(g_s x) dmu ds = mu(d). So mu(d) = 0.
   - By [Ru] for g_1 and g_{-1}, mu has a positive and a negative exponent, so chi_min is defined.
   - Put theta := chi_min/2 and eps := min(chi_min/8, theta/2). Apply [KH] with this eps and with phi = d, which gives Lambda.

1. *A periodic orbit with small divergence.*
   - Lambda contains a periodic orbit gamma, of period P, say. Its transverse Floquet exponents have modulus >= chi_min - eps > theta + eps, and its average satisfies |I(gamma)|/P < eps, where I(gamma) = int_0^P d(g_s q) ds.
   - Fix q in gamma. Since J_{mP}(q) = m I(gamma), we get |J_t(q) - (t/P) I(gamma)| <= 2P||d||_inf, hence |J_t(q)| <= C_0 + eps|t| for all real t.
   - The same bound holds for every point g_b q of gamma, with constant C_0 + eps|b|.

2. *Two homoclinic orbits.*
   - In the symbolic model, gamma corresponds to the orbit of a periodic sequence w^infinity.
   - The SFT is transitive and has positive entropy, so it is not a single periodic orbit. Hence there is an admissible word u, beginning and ending so that ...w w u w w... is admissible, such that the sequences s_n := ...w w u w^n u w w... (n >= 1) are pairwise in distinct shift orbits and none lies in the orbit of w^infinity.
   - Points of Lambda whose codes agree with that of gamma in the far past (resp. far future) lie in W^u(gamma) (resp. W^s(gamma)). This is standard for hyperbolic sets with local product structure, via expansivity and the shadowing estimate.
   - Hence there are two orbits O_a != O_b in Lambda, both disjoint from gamma and both contained in W^u(gamma) ∩ W^s(gamma).
   - By [SM], each O_c meets W^{uu}(q): if z in O_c lies in W^{uu}(g_r q), then g_{-r} z lies in W^{uu}(q). Let z_c be such a point.
   - Again by [SM], z_c lies in W^{ss}(g_{b_c} q) for some real b_c.
   - z_c is not periodic: a periodic point has its own orbit as alpha-limit set, whereas the alpha-limit set of z_c is gamma and z_c is not on gamma. It is not a zero of X, because z_c lies in Lambda, which carries a nonvanishing X: Lambda is the suspension of a subshift with positive roof.

3. *The chains.*
   - Put x_0 := q. The chain (a_i) is a_0 = q, a_1 = z_a, a_i = g_{b_a} q for i >= 2. The chain (b_i) is defined in the same way with z_b and b_b.
   - Legs a_{2i+1} -> a_{2i+2} and a_{2i} -> a_{2i+1} with i >= 1 have length 0, and constant padding is allowed by the remarks to (SC).
   - (L1): the leg q -> z_a satisfies d(g_t q, g_t z_a) <= C e^{-theta|t|} d(q, z_a) for t <= 0, since z_a lies in W^{uu}(q) with backward rate >= chi_min - eps - delta > theta. The pair-dependent constant is absorbed into C; there are finitely many nontrivial legs and each has positive length.
   - (L2): the same argument applies to z_a -> g_{b_a} q, which is a stable leg.
   - (L3): the chain is a finite sum.
   - (E): p = g_{b_a} q and tau = b_a, so the left side is 0.
   - (L4), even vertices: x_0 = q and the vertices g_{b_a} q satisfy J_t <= C' + eps|t| for all t (step 1).
   - (L4), odd vertex x_1 = z_a for t >= 0: with q' := g_{b_a} q,
     |J_t(z_a) - J_t(q')| <= Lip(d) int_0^inf d(g_s z_a, g_s q') ds < infinity,
     and J_t(q') <= C' + eps t.
   - (L4), padded odd vertices: these equal q', so the bound above applies.
   - (L4), J_t(x_0) for t >= 0: covered by step 1.
   - Take eta := eps < theta and C' large.
   - *Orbit-isolated vertices.* The combined vertex list is {q, z_a, g_{b_a} q, z_b, g_{b_b} q}. The point z_a != q occurs exactly once, because z_b lies on the other orbit O_b. It is neither a zero nor periodic. Its orbit O_a contains neither q, nor g_{b_c} q (both on gamma), nor z_b (on O_b), nor the limit points (on gamma). The same holds for z_b. ∎

**Corollary 1.1.** (SC) holds if n <= 3. If n = 2 its hypotheses are never met.

*Proof.*
- As in step 0, mu(Zero X) = 0, the flow-direction exponent is 0, and there is a positive exponent and a negative exponent.
- If n = 2 there are only two exponents, one of them the flow-direction 0, so a positive and a negative exponent cannot both occur.
- If n = 3 the exponents are chi+ > 0, 0 and chi- < 0, so mu is hyperbolic. Theorem 1 applies. ∎

*Relation to earlier results.* Under GH the hyperbolic case was already excluded directly (R6-a, Theorem 5.1). Theorem 1 therefore adds nothing to the goal. It only shows that (SC) is not false for a "cheap" reason in the hyperbolic case. The open part of (SC) is exactly the **non-hyperbolic** case: an extra zero exponent transverse to X, with mu(d) = 0.

---

## 2. What the Pinsker coincidence gives rigorously (Lemma 2)

**Setting.** f = g_1, and mu is ergodic with h_mu(f) > 0 (so also h_mu(f^{-1}) > 0). No hyperbolicity is assumed.

**Cited results.**
- [LS/LY] There is a measurable partition xi^s subordinate to W^s, meaning that xi^s(x) is contained in W^s_loc(x) and contains a W^s-neighbourhood of x. It satisfies f^{-1} xi^s ≥ xi^s, and the tail satisfies ∧_n f^{-n} xi^s = π mod mu, where π is the Pinsker partition of f. Sources, from memory: Ledrappier-Young, Ann. Math. 122 (1985), Part I, the part identifying the Pinsker partition with the measurable hull of the partition into global unstable manifolds, applied to f^{-1}; the Pinsker algebras of f and f^{-1} coincide. Only the easy consequence is used: **the sigma-algebra of π is contained, mod mu, in that of xi^s**, i.e. xi^s refines π mod 0. The same holds for an unstable partition xi^u.
- Lemma 6.0 of R6-a (quoted in the task file; its proof is complete there): the conditional measures mu^u_x of a subordinate unstable partition are non-atomic for a.e. x when h > 0. Applied to f^{-1}, the same holds for mu^s_x.

**Lemma 2.** For mu-a.e. x:
(i) supp mu^s_x ⊂ supp mu^π_x and supp mu^u_x ⊂ supp mu^π_x;
(ii) hence supp mu^π_x ∩ W^s_loc(x) contains uncountably many points other than x, and so does supp mu^π_x ∩ W^u_loc(x).

*Proof.*
1. *Notation.* Write S(y) := supp mu^π_y.
   - y -> mu^π_y is measurable into Prob(M) and constant on π-atoms. Hence y -> 1_{M \ S(y)}(z) is jointly measurable. (Use a countable base U_k: z ∉ S(y) iff there is k with z in U_k and mu^π_y(U_k) = 0.)
   - Since xi^s refines π mod 0, for a.e. y we have S(z) = S(y) for mu^s_y-a.e. z.
2. *The integral computation.* Then
   int mu^s_y(M \ S(y)) dmu(y) = int int 1_{M\S(z)}(z) dmu^s_y(z) dmu(y) = int 1_{M\S(z)}(z) dmu(z).
   The last equality is disintegration over xi^s. By disintegration over π, the right-hand side equals int mu^π_x(M \ S(x)) dmu(x) = 0.
3. *Conclusion of (i).* So mu^s_y(M \ S(y)) = 0 a.e., i.e. supp mu^s_y ⊂ S(y). The u-statement is identical.
4. *Proof of (ii).* mu^s_x is non-atomic and carried by xi^s(x) ⊂ W^s_loc(x), so its support is an uncountable subset of W^s_loc(x). This support is contained in S(x) by (i). ∎

**Meaning.** The Pinsker atom of x, taken metrically through the support of its conditional measure, contains nontrivial points of the target set W^s_loc(x) ⊂ W^{cs}(x) of (E). This is all that the "mod 0" picture can say about the target. The question is whether such a point is reached by a summable su-chain whose vertices are off its orbit. Section 3 isolates exactly this; Section 4 explains why the Pinsker coincidence does not provide it.

---

## 3. Reduction of (SC) to a metric closedness property (Proposition 3; proved)

**Pesin-Egorov block.** Fix mu as in (SC), so mu(d) = 0. Fix theta with 0 < theta < min(chi^+_min, |chi^-_max|), and fix eta in (0, theta). By Pesin theory and Egorov there is a compact K with mu(K) > 0 and constants C_K, r_K, C' such that every z in K satisfies:
- W^s_loc(z) and W^u_loc(z) are embedded discs of size r_K.
- d(g_t y, g_t z) <= C_K e^{-theta t} d(y, z) for y in W^s_loc(z) and t >= 0. Interpolation from integer times uses Lip(g_s) for |s| <= 1.
- The same bound holds for y in W^u_loc(z) and t <= 0.
- J_t(z) <= C' + eta|t| for all real t. Birkhoff gives J_t(z)/t -> mu(d) = 0 as t -> ±infinity a.e., and Egorov makes the bound uniform.

**K-chains.** A *K-chain from x_0* is a sequence (x_i) in K such that x_{2i+1} in W^u_loc(x_{2i}) and x_{2i+2} in W^s_loc(x_{2i+1}) for all i, and sum_i d(x_i, x_{i+1}) < infinity. Every K-chain satisfies (L1), (L2), (L3) with C = C_K. It satisfies (L4), because all vertices satisfy the two-sided bound.

**Property (CL)** (closedness of K-accessibility on Pinsker supports). For mu-a.e. x_0 in K, every mu-conull set G, and every y in K ∩ supp mu^π_{x_0}, there is a K-chain from x_0 converging to y whose vertices x_i (i >= 1) lie in G and lie on pairwise distinct orbits.

**Proposition 3.** (CL) implies (SC) for mu, whether or not mu is hyperbolic.

*Proof.*
1. *The conull set G_0.* Let G_0 be the set of points that are neither zeros nor periodic. It is mu-conull: mu is ergodic with positive entropy, so it is not carried by Zero X nor by a periodic orbit, and the set of periodic points carries no ergodic measure of positive entropy. Also every single orbit O is mu-null: otherwise ergodicity puts mu on O, and h_mu = 0.
2. *Choice of x_0.* By Lemma 2 and mu(K) > 0, we can choose x_0 in K with the following properties.
   - x_0 is good for (CL) and for Lemma 2.
   - mu^s_{x_0}(K) > 0. This holds on a set of positive measure, since int mu^s_x(K) dmu = mu(K) > 0.
   - The set K ∩ supp mu^s_{x_0} ⊂ K ∩ W^s_loc(x_0) ∩ supp mu^π_{x_0} is uncountable. (The restriction of the non-atomic mu^s_{x_0} to K has positive mass, so its support is uncountable.)
3. *Choice of the targets.* Choose y_a != y_b in that set, both off the orbit of x_0, and y_b off the orbit of y_a. This is possible because orbits are countable unions of arcs and meet the disc W^s_loc(x_0) in a countable set (flow-box argument with transversality of the local stable disc to X near x_0; at distant times use countability of the returns).
4. *Chain a.* Apply (CL) with G_a := G_0 minus the orbits of x_0, y_a, y_b. This gives chain a, converging to y_a.
5. *Chain b.* Apply (CL) with G_b := G_a minus the orbits of all vertices of chain a; this is a countable union of null sets. This gives chain b, converging to y_b.
6. *(E).* p_a = y_a lies in W^s_loc(x_0) with x_0 in K, so d(g_t p_a, g_t x_0) <= C_K e^{-theta t} for t >= 0. Thus (E) holds with tau = 0. The same holds for chain b.
7. *(L4) at x_0.* x_0 is in K, so J_t(x_0) <= C' + eta t for t >= 0.
8. *Orbit-isolated vertices.* v_a := a_1 is not x_0, since it lies in G_a. It is neither a zero nor periodic, since it lies in G_0. Its orbit contains:
   - no other vertex of chain a (pairwise distinct orbits);
   - no vertex of chain b (by the choice of G_b);
   - neither y_a nor y_b (by the choice of G_a).

   For the same reason, v_a occurs only once in the combined list. The vertex v_b := b_1 is handled in the same way, with the roles reversed via G_b. ∎

So the whole difficulty of (SC) is in (CL). By Theorem 1 it suffices to prove (CL), or (SC) directly, for non-hyperbolic mu.

---

## 4. The planner's route: where "mod 0" fails to become "metric"

The planner's dichotomy is (i) "A(x) meets W^{cs}_loc(x) nontrivially", or (ii) "{A(x)} is a measurable u- and s-saturated partition, so A(x) is mod 0 a union of Pinsker atoms, and then come back to (i)". Each step is examined below.

**4.1. A(x) does not define a partition, and the inclusion goes the wrong way.**
- Let A_K(x) be the set of limits of summable K-chains from x. "y in A_K(x)" is not an equivalence relation. One cannot extend a chain beyond the limit of an infinite chain: the limit need not lie in K, and need not have local manifolds of size r_K. So the relation is not transitive.
- The natural equivalence relation is accessibility by **finite** K-chains, or its f-saturation ~. Its classes are analytic sets, and their partition is generally not measurable. Only its measurable hull H (the sigma-algebra of measurable ~-saturated sets) is available.
- A ~-saturated measurable set is u-saturated mod 0 and s-saturated mod 0, so by [LY] it is a Pinsker set. Thus **H ⊂ π**: the hull is *coarser* than the Pinsker algebra. This is the correct form of "(ii)".
- It says that the atoms of H are unions of Pinsker atoms. It does **not** say that a single class [x]_~ fills the Pinsker atom of x mod mu^π_x. In general the classes are mu^π_x-null: for instance, finite chains from x reach at most a countable union of (u+s)-dimensional sets, which is null whenever mu^π_x has larger "dimension" in the centre direction.
- So the planner's statement "A(x) is (mod 0) a union of Pinsker atoms" does not follow. What follows is the weaker fact H ⊂ π, and that fact carries no information about single classes.

**4.2. Why a Hopf argument cannot close the gap without absolute continuity.**
- To prove that a class [x]_~ has full mu^π_x-measure, the Hopf argument needs the following: s-holonomy between u-plaques sends mu^u-conull sets to mu^u-conull sets (absolute continuity of holonomies *with respect to the conditional measures*).
- For volume or SRB measures this follows from absolute continuity of Pesin holonomies with respect to leaf volume, together with mu^u ≪ leaf volume. For a general mu of positive entropy, mu^u_x can be singular to leaf volume (e.g. carried by a Cantor set of positive dimension), and the stable holonomy can map mu^u-typical points into a mu^u-null set. Already for Gibbs measures on horseshoes, holonomies preserve the class of the conditionals only because of the symbolic product structure.
- So, in general, the step "class saturates the Pinsker atom" is unavailable. I see no substitute that uses only the Pinsker algebra.

**4.3. Even full saturation would only give a mod-0 statement, while (SC) needs a point of a conditional-null set.**
- Suppose one had the strongest mod-0 conclusion: mu^π_x-a.e. point lies in the class of x.
- The targets of (E) lie in W^{cs}(x) := union over tau of W^{ss}(g_tau x). For non-hyperbolic mu this has dimension s + 1 < n - u. Lemma 2 shows that it meets supp mu^π_x nontrivially. But it can be, and in the product-type examples is, a mu^π_x-null set.
- No mod-0 statement can produce a point of a null set. One needs a **closedness** property: the accessible set contains the support of mu^π_x, and not only mu^π_x-a.e. point. With summable chains this is exactly (CL).
- Closedness in turn needs a *quantitative local accessibility* estimate. Suppose z in K lies at distance delta from a target y in K ∩ supp mu^π_x. Then a K-chain of cost O(delta^alpha) (alpha > 0) must lead from z to a point of K at distance <= delta/2 from y, and inside the prescribed conull set G. Iterating gives a geometric, hence summable, chain.
- In the hyperbolic case this estimate is supplied by **local product structure**. W^u_loc(z) ∩ W^{cs}_loc(y) is a single point at distance O(delta), and Katok closing or a horseshoe makes this uniform; this is the mechanism behind Theorem 1. In the non-hyperbolic case dim W^u + dim W^{cs} < n, so W^u_loc(z) ∩ W^{cs}_loc(y) = ∅ for generic pairs. The only remaining mechanism for moving in the centre direction is non-integrability of the su-legs (Brin quadrilaterals, with cost ~ delta^{1/2} for displacement delta). For that one needs:
  - (a) continuity of Pesin manifolds on K, in the C^1 topology, which is available;
  - (b) a **quantitative non-integrability** (or exact joint integrability) of the measurable families W^u, W^s on K in the centre direction, which is **not** a consequence of h_mu > 0, of [LY], or of anything mod 0.

**This is the precise failure point:** the passage from [LY] (an identity of sigma-algebras mod mu) to the quantitative local accessibility estimate needed for (CL).

**4.4. A sketch that the two extreme cases behave well (not proved; heuristic).**
- *Exact joint integrability on K.* Suppose that for z in K the local W^u and W^s plaques lie in local (u+s)-dimensional su-plaques with local product structure. Then for x in K, x_1 in W^u_loc(x), x_2 in W^s_loc(x_1) close to x, the point x_3 := W^u_loc(x_2) ∩ W^s_loc(x) exists. The chain x, x_1, x_2, x_3 (padded) ends at x_3 in W^s_loc(x), and the vertices x_1, x_2 can be taken off the orbit of x_3.
- *Uniform non-integrability on K.* In this case Brin's quadrilateral argument gives centre displacements of both signs at cost O(delta^{1/2}), and hence (CL).
- **The intermediate measurable regime** (non-integrability that degenerates on a set of positive measure, or varies measurably) is not covered. I see no way to rule it out using positive entropy and [LY] alone.
- The notions "joint integrability on K" and "non-integrability on K" are not even standardly defined for Pesin laminations. I mark 4.4 as a sketch.

---

## 5. Search for a counterexample to (SC) (none found)

(SC) needs no GH, so it could fail for a non-GH flow. The following checks found no counterexample.
- *Contact Anosov flows* (geodesic flows of negatively curved manifolds) with mu = Liouville, so d = 0 for nu = Liouville. The strong foliations are not jointly integrable, so (Brin) every point is reachable by a finite su-chain. Take p in W^{ss}(x_0) and a 4-leg chain to it, with intermediate vertices off the orbit of p. Then (SC) holds with tau = 0. (These are hyperbolic anyway: Theorem 1.)
- *Products N × S^1* with flow (phi_t x, theta + omega t), where phi is contact Anosov. Here mu = Liouville × Leb is non-hyperbolic (a second zero exponent).
  - The legs preserve theta. The target in (E) at tau = 0 is W^{ss}_N(x_0) × {theta_0}, and it is reached inside N × {theta_0} by su-accessibility of phi.
  - So (SC) holds. (CL) also holds, if one accepts, cited from memory and unchecked here, that the Pinsker algebra of this product is the theta-algebra.
- *Circle extensions* (phi_t x, theta + int_0^t a(phi_r x) dr).
  - If a = c + Yb (Y the generator of phi), the extension is conjugate to the product with rotation speed c, which is the previous case.
  - Otherwise the su-holonomy group of the extension is a closed subgroup of S^1. If it is all of S^1 (accessibility), every point is reachable. If it is finite, the extension has a finite rotation factor, and one can return exactly to the fibre value by a loop whose holonomy is trivial (e.g. a commutator of loops, or a loop iterated k times).
  - In each case (SC) holds. I did not write out every detail.
- *Suspensions of products with constant roof* (Anosov automorphism × rotation): the legs stay in a fibre, and homoclinic points of the automorphism give (SC).

In all these examples (SC) holds, so they do not show (SC) to be false. A counterexample would need a non-hyperbolic positive-entropy measure whose su-legs are neither jointly integrable nor uniformly non-integrable on Pesin blocks, in a way that prevents exact return. I could not construct one.

---

## 6. Status

**Proved.**
1. Theorem 1: (SC) for every hyperbolic mu, in particular for n <= 3. Cited inputs: [Ru], [SM], and [KH] with the periodic-orbit refinements (a), (b). Refinement (b) is flagged as cited from memory, flow version unchecked.
2. Lemma 2: Pinsker-conditional supports contain the supports of the stable and unstable conditionals; hence they contain nontrivial points of W^s_loc(x) and W^u_loc(x). Proof complete given the cited [LY] inclusion "xi^s refines π" and Lemma 6.0 of R6-a.
3. Proposition 3: (CL) implies (SC), with orbit isolation handled by removing countably many mu-null orbits. Proof complete given standard Pesin-block facts.

**Shown not to follow, and why** (Section 4).
- The planner's step "A(x) is mod 0 a union of Pinsker atoms" does not follow. The correct consequence of [LY] is that the hull of the su-accessibility relation is a sub-sigma-algebra of π, which is coarser and says nothing about single classes.
- A Hopf argument would need absolute continuity of holonomies with respect to the conditional measures, which fails for general mu.
- Even a full mod-0 saturation would not give (SC), because the target is conditional-null. The missing ingredient is quantitative local accessibility in the centre direction on Pesin blocks.

**Sketched only.** Section 4.4 (the jointly integrable and uniformly non-integrable regimes) and parts of Section 5.

**Open.**
- (SC) for non-hyperbolic mu (an extra zero exponent transverse to X, mu(d) = 0). Equivalently, by Proposition 3, it suffices to prove (CL) for such mu, or to find a counterexample.
- A precise sub-question: on a Pesin block of a non-hyperbolic positive-entropy measure, do summable su-chains through the block reach every point of the block in the support of the Pinsker conditional measure?

=== END OF ANSWER round14_q6 ===
