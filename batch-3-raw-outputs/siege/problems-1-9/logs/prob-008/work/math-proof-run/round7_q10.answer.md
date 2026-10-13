# round7_q10: answer

## 0. Verdict (summary)

- **(PE-NH) is NOT proved here, and no counterexample is given.** The problem's claim (zero topological entropy
  under GH) therefore stays proved only for dim M <= 3 (entry 61) and, in every dimension, for hyperbolic
  positive-entropy measures (entry 60).
- **Chain check.** Steps 2 and 4 of the chain are correct as stated (Section 1). Step 1 is the gap.
- **New results, proved in full** (they use only GH via Theorem J, i.e. L1 + GH for constant right-hand sides):
  - **Theorem J\*** (Section 2). Theorem J stays true when exponential decay is replaced by any decay e^{-w(|t|)}
    whose moments form a quasi-analytic (Denjoy-Carleman) sequence, e.g. w(t) = t/log(e+t). This makes the
    planner's mechanism (iii) rigorous.
  - **Theorem G** (Section 3). This is a "graph" version of Theorem J. GH excludes every finite configuration of
    distinct points, grouped into forward-asymptotic ("stable") classes and backward-asymptotic ("unstable")
    classes, that carries a nonzero weight vector cancelling at first order in every class, provided the Jacobian
    growth at the class representatives is slower than the asymptotic rate.
  - **Corollaries G1-G3.** Under GH:
    - no closed su-cycle (of any even length) with zero Jacobian holonomy exists;
    - when there is a smooth invariant volume, no closed su-cycle exists at all; in particular there are no two
      distinct points that are exponentially asymptotic in both time directions;
    - no configuration with more points than classes exists, for any Jacobian constants.
- **Reduction (Section 4).** At mu(d) = 0, which is the hard case (PE0), (PE-NH) follows from the existence, among
  mu-typical points, of one such configuration. Section 4 explains why Pesin theory does not supply one when mu is
  non-hyperbolic, and states this as the precise open point.

## 1. Check of the chain

**Step 2 (entry 60 / Theorem 5.1).**
- mu(Zero X) = 0 holds, since otherwise mu is carried by the closed invariant set Zero X, where g_1 = id, so
  h_mu = 0.
- The flow-direction exponent is 0 mu-a.e.
- Ruelle's inequality for g_1 and for g_{-1} gives a positive and a negative exponent.
- If mu were hyperbolic (all exponents nonzero except the flow direction), the Katok horseshoe theorem for flows
  (Katok 1980; Lian-Young for C^2 flows in any dimension; cited from memory) would give a hyperbolic periodic orbit
  gamma with a homoclinic point. Corollary 4.2 excludes this.
- Corollary 4.2 rests on Lemma K and Lemma K', which I re-checked:
  - the Cayley-Hamilton step: L preserves I_K because g_{-P} p = p;
  - the Taylor bound on I_K;
  - the forward estimate via (b).
  All are correct.
- Corollary 4.2 also needs Observation P (no periodic orbit with I(gamma) = 0) and P1 (d(p) != 0 at zeros). Both
  are correct.

**Step 4 (variational principle).** h_top(g_1) = sup_m h_m(g_1). For a g_1-invariant m put
mbar = int_0^1 (g_s)_* m ds. Then:
- mbar is flow-invariant;
- h_{(g_s)_* m}(g_1) = h_m(g_1), because g_s conjugates g_1 to itself;
- by the integral (Jacobs) formula for entropy, h_mbar(g_1) = h_m(g_1) <= ess sup of h_mu(g_1) over the
  flow-ergodic components mu of mbar.

So zero entropy for every flow-ergodic mu gives h_top(g_1) = 0. This is correct. (For the integral formula one may
use the ergodic decomposition of mbar under g_1 and the fact that the map m -> h_m(g_1) is affine and
"integrable", by Jacobs' theorem.)

**Remark on the status of the problem (from memory, hedged).** I recall that the zero-entropy statement in
dimension 3 for cohomology-free / GH flows was obtained in the literature through Katok's horseshoe theorem. That
is the same mechanism as Theorem 5.2 here (Kocsard's work on the Katok conjecture in dimension 3; Forni's paper on
the Greenfield-Wallach and Katok conjectures). I do not recall a proof of zero entropy for GH flows in dimension
>= 4. The statement is implied by the Greenfield-Wallach conjecture, which is open as far as I know. So the
non-hyperbolic case may well be a genuinely open problem. This recollection is not used anywhere below.

## 2. Theorem J* (quasi-analytic version of Theorem J) — proved

Notation as in the brief: P phi = X phi + d phi, and F_phi(t) = S(e^{J_t} (phi o g_t)).

**Theorem J\*.** Assume GH. Let w : [0, inf) -> [0, inf) be measurable with
M_j := int_R |t|^j e^{-w(|t|)} dt < inf for every j >= 0, and with sum_{j>=1} M_j^{-1/j} = inf.
Let S be a distribution density for which there are k and C with
 |F_phi(t)| <= C e^{-w(|t|)} ||phi||_{C^k}  for all real t and all smooth phi.  (**)
Then S = 0.

*Proof.*
1. As in Theorem J step 1, F_phi is C^1 and F_phi' = F_{P phi}. By (**) applied to P phi,
   |F_phi'(t)| <= C e^{-w(|t|)} ||P phi||_{C^k}.
2. *Moments.* m_j(phi) := int t^j F_phi(t) dt satisfies |m_j(phi)| <= C M_j ||phi||_{C^k}. So m_j is a
   distribution density of order <= k.
3. *Jordan relations.* Fix j >= 0 and phi, and put h(R) := R^j (|F_phi(R)| + |F_phi(-R)|).
   - By (**) and M_j < inf, int_1^inf h(R) dR < inf, hence liminf_{R -> inf} h(R) = 0. Choose R_n -> inf with
     h(R_n) -> 0.
   - Integrate by parts on [-R_n, R_n]: int_{-R_n}^{R_n} t^j F_phi'(t) dt = [t^j F_phi]_{-R_n}^{R_n} - j int t^{j-1} F_phi dt.
   - Let n -> inf. Both integrals converge absolutely by (**) and step 1, and the boundary term tends to 0.
   This gives m_0(P phi) = 0 and m_j(P phi) = -j m_{j-1}(phi) for j >= 1.
4. *Induction.* Exactly as in Theorem J step 4 (using F1 and F2), m_j = 0 for all j.
5. *Quasi-analyticity.* Fix phi and put G(xi) := int e^{-i xi t} F_phi(t) dt for real xi.
   - G is C^inf, with G^{(j)}(xi) = int (-it)^j e^{-i xi t} F_phi dt, so |G^{(j)}(xi)| <= C_phi M_j and
     G^{(j)}(0) = (-i)^j m_j(phi) = 0.
   - The sequence (M_j) is log-convex. By Cauchy-Schwarz, M_j = int |t|^{(j-1)/2} |t|^{(j+1)/2} e^{-w} dt <=
     (M_{j-1} M_{j+1})^{1/2}.
   - Put Mt_j := M_j / M_0. Then Mt_0 = 1, (Mt_j) is still log-convex, and Mt_j^{-1/j} = M_0^{1/j} M_j^{-1/j}.
     Since M_0^{1/j} lies between min(1, M_0) and max(1, M_0), sum Mt_j^{-1/j} = inf.
   - Denjoy-Carleman theorem (cited from memory; Rudin, *Real and Complex Analysis*, Thm 19.11). For a log-convex
     sequence with Mt_0 = 1, the class C{Mt_j} = {f in C^inf(R) : ||f^{(j)}||_inf <= beta_f B_f^j Mt_j} is
     quasi-analytic iff sum Mt_j^{-1/j} = inf. Here G lies in the class with beta = C_phi M_0 and B = 1.
   - So G, all of whose derivatives vanish at 0, is identically 0.
   - F_phi is continuous and in L^1 with Fourier transform 0, so F_phi = 0. Then S(phi) = F_phi(0) = 0. ∎

**Example.** w(t) = t / log(e + t) is admissible. Laplace's method gives max_t (j log t - w(t)) = j log(j log j) + O(j),
the maximum being near t ~ j log j. Hence M_j^{1/j} = O(j log j) and sum M_j^{-1/j} >= c sum 1/(j log j) = inf.
(This is a routine estimate, given here in outline only.) By contrast, w(t) = t^{1-delta} with delta > 0 is NOT
admissible: then M_j^{1/j} ~ j^{1/(1-delta)}, and the sum converges.

**What J\* buys.** An S with two-sided decay e^{-|t|/log|t|} already contradicts GH. So in Theorem G below, and in
Prop. 6.1 / Lemma K, it is enough that the cancellation rate beats the Jacobian growth at the representatives by a
margin of order |t|/log|t|. For example, J_t(x) <= C + theta|t| - |t|/log(e+|t|) suffices against the cancellation
rate e^{-theta|t|}. This does not help in the core case: there the difficulty is the existence of two-sided
cancellation at all, not the size of the margin.

## 3. Theorem G (finite configurations with stable and unstable cancellation) — proved

**Setting.**
- Z = {z_1, ..., z_N} is a set of N >= 1 *distinct* points of M.
- Z is partitioned in two ways: into "stable classes" A_1, ..., A_p and into "unstable classes" B_1, ..., B_q.
  Every point lies in exactly one A and exactly one B.
- In each class a representative is fixed: a(A) in A and b(B) in B.
- Fix constants C >= 1 and theta > eta >= 0. Assume:
  - (S) for each A and each z in A: dist(g_t z, g_t a(A)) <= C e^{-theta t} for all t >= 0;
  - (U) for each B and each z in B: dist(g_t z, g_t b(B)) <= C e^{-theta |t|} for all t <= 0;
  - (R) for each A: J_t(a(A)) <= C + eta t for t >= 0; for each B: J_t(b(B)) <= C + eta |t| for t <= 0.

**Jacobian constants.** For z in A put beta^s_z := lim_{t -> +inf} (J_t(z) - J_t(a(A))). It exists because
J_t(z) - J_t(a) = int_0^t (d(g_s z) - d(g_s a)) ds and the integrand is at most Lip(d) C e^{-theta s}. Moreover
|J_t(z) - J_t(a) - beta^s_z| <= K e^{-theta t} for t >= 0, with K = Lip(d) C/theta. Similarly, for z in B,
beta^u_z := lim_{t -> -inf} (J_t(z) - J_t(b(B))), and |J_t(z) - J_t(b) - beta^u_z| <= K e^{-theta|t|} for t <= 0.

**Theorem G.** Assume GH. In the setting above there is no nonzero vector (w_z)_{z in Z} with
 sum_{z in A} w_z e^{beta^s_z} = 0 for every stable class A, and sum_{z in B} w_z e^{beta^u_z} = 0 for every unstable class B.  (G)

*Proof.* Suppose (w_z) is nonzero and satisfies (G). Put S := sum_z w_z delta_z. Then S != 0, since the points are
distinct, and F_phi(t) = sum_z w_z e^{J_t(z)} phi(g_t z).

*t >= 0.* Fix a class A with representative a. For z in A write
- e^{J_t(z)} = e^{J_t(a)} e^{beta^s_z} e^{r_z(t)}, with |r_z(t)| <= K e^{-theta t} <= K;
- phi(g_t z) = phi(g_t a) + e_z(t), with |e_z(t)| <= ||phi||_{C^1} C e^{-theta t}.

Expanding the product and using |e^{r} - 1| <= |r| e^{|r|}:
 sum_{z in A} w_z e^{J_t(z)} phi(g_t z) = e^{J_t(a)} [ phi(g_t a) sum_{z in A} w_z e^{beta^s_z} + E_A(t) ],
 with |E_A(t)| <= C' e^{-theta t} ||phi||_{C^1}.
The first term vanishes by (G). By (R), |sum_{z in A} ...| <= C'' e^{-(theta - eta) t} ||phi||_{C^1}. Summing over
the finitely many A gives |F_phi(t)| <= C''' e^{-(theta - eta)t} ||phi||_{C^1} for t >= 0.

*t <= 0.* The same computation with the unstable classes, (U), (R) and the second half of (G) gives
|F_phi(t)| <= C''' e^{-(theta-eta)|t|} ||phi||_{C^1}.

So (*) of Theorem J holds with k = 1 and eps = theta - eta > 0. Hence S = 0, a contradiction. ∎

(By Theorem J\*, (R) can be weakened to J_t(rep) <= C + theta|t| - w(|t|) with w admissible.)

**Linear algebra of (G).** (G) is a homogeneous linear system with N unknowns and p + q equations. Each point z
occurs in exactly one equation of each family, with nonzero coefficient. So the system is the incidence system
of a bipartite multigraph Gamma: vertices are the classes, and edges are the points (an edge joins the stable
class and the unstable class of z), with nonzero weights e^{beta}. Hence:
- (a) If N > p + q, a nonzero solution exists, whatever the beta's are.
- (b) A connected component of Gamma that is a tree carries only the zero solution.
- (c) Suppose the component is a single even cycle z_1, ..., z_{2n} (n >= 1, indices mod 2n), where z_{2i-1}, z_{2i}
  share an unstable class and z_{2i}, z_{2i+1} share a stable class. Put
  beta^u(x, y) := lim_{t -> -inf} (J_t(x) - J_t(y)) and beta^s(x, y) := lim_{t -> +inf} (J_t(x) - J_t(y)).
  - The equations are w_{2i} = -w_{2i-1} e^{beta^u(z_{2i-1}, z_{2i})} and w_{2i+1} = -w_{2i} e^{beta^s(z_{2i}, z_{2i+1})}.
  - Going once around the cycle, a nonzero solution exists iff the **Jacobian holonomy** vanishes:
    H := sum_{i=1}^{n} [ beta^u(z_{2i-1}, z_{2i}) + beta^s(z_{2i}, z_{2i+1}) ] = 0.
  - The sign factors contribute (-1)^{2n} = 1.
  - Check: beta^u(x, y) = beta^u_x - beta^u_y for x, y in one unstable class, and similarly for stable classes;
    these are the constants entering (G).

**Corollary G1 (closed su-cycles with zero holonomy).** Assume GH. There are no n >= 1 and distinct points
z_1, ..., z_{2n} (indices mod 2n) such that all of the following hold:
- z_{2i} is exponentially backward-asymptotic to z_{2i-1}, i.e. (U) holds for the pair;
- z_{2i+1} is exponentially forward-asymptotic to z_{2i}, i.e. (S) holds;
- H = 0;
- the growth condition (R) holds at one point of each pair, with eta < theta.

*Proof.* Take the classes {z_{2i-1}, z_{2i}} (unstable) and {z_{2i}, z_{2i+1}} (stable), apply (c) and then
Theorem G. For n = 1 the "cycle" is a pair x != y that is exponentially asymptotic in both time directions. Then
H = beta^u(x, y) + beta^s(y, x) = 0 means lim_{-inf} (J_t x - J_t y) = lim_{+inf} (J_t x - J_t y). ∎

**Corollary G2 (smooth invariant volume).** Assume GH and that X preserves a smooth positive density omega.
- There is no closed su-cycle as in G1 at all, for any n >= 1.
- In particular, no two distinct points are exponentially asymptotic in both time directions.
- Also, no nondegenerate "su-quadrilateral" exists: x, y in W^{uu}(x), z in W^{ss}(x), and a fourth point in
  W^{ss}(y) ∩ W^{uu}(z), with the four points distinct and all asymptotics exponential.

*Proof.* Take nu = omega. Then d = 0 and J = 0, so every beta vanishes, H = 0, and (R) holds with eta = 0.
Corollary G1 applies. ∎

**Corollary G3 (more points than classes).** Assume GH. There is no configuration as in the setting with N > p + q.
This holds for arbitrary Jacobian constants, hence with no holonomy condition. Example: a 3 x 2 "rectangle": three
distinct points x_1, x_2, x_3 on one unstable class, and three distinct points x'_i forward-asymptotic to x_i,
forming a second unstable class (classes {x_i, x'_i} stable). Here N = 6 > 2 + 3 = 5.

*Proof.* By (a), a nonzero solution of (G) exists; Theorem G applies. ∎

**Relation to earlier results.** The single pair (one unstable class of 2 points, two singleton stable classes) is
the case of Prop 6.1, where the forward decay instead comes from lambda < 0 (a singleton stable class with
J_t(a) <= -c t needs no cancellation; Theorem G is stated with eta >= 0, but the same proof allows a singleton
class whose representative has J_t <= C - c|t| on its side). Lemma K is the analogous statement with
Cayley-Hamilton cancellation along a single orbit.

Precise form of the variant, used in Section 4. In Theorem G, any class (stable or unstable) whose representative
satisfies J_t(rep) <= C - c|t| on the relevant time half-line (c > 0) may be **exempted** from its equation in
(G). The proof of Theorem G bounds that class's contribution by e^{J_t(rep)} sum |w_z| ... <= C' e^{-c|t|} ||phi||_inf
without any cancellation. Then eps = min(c, theta - eta).

*Sanity check (consistency, not needed).* Let M = T^1 Sigma × T^2, where Sigma is a closed hyperbolic surface, and
let X = (geodesic generator) + (Diophantine constant field on T^2). This X preserves volume and has positive
entropy. It is not GH, by (O2): the measure mu_gamma ⊗ Leb_{T^2} for a closed geodesic gamma is a second
invariant measure.
- The relation (u(1) l(-1))^3 = ±I in SL(2, R) between the upper and lower unipotents gives closed
  strong-stable/strong-unstable hexagons in T^1 Sigma.
- These hexagons lift to M with the T^2 coordinate unchanged.
So Corollary G2 independently confirms that this X is not GH, as it must be.

## 4. Reduction of (PE-NH) to a configuration statement, and where it stops

**Proposition 4.1 (conditional reduction; proved given its hypothesis).** Assume GH. Let mu be ergodic,
flow-invariant, with h_mu(g_1) > 0 and mu(d) = 0. Assume the following.

**(CH)** There is a finite configuration as in Section 3 whose class representatives are mu-generic in both time
directions, i.e. J_t(rep)/t -> 0 as t -> ±inf. Each stable (resp. unstable) class is contained in the Pesin local
strong stable (resp. unstable) manifold of its representative. The configuration is either
- a closed su-cycle of distinct points with zero Jacobian holonomy H = 0 (automatic if X preserves a smooth volume),
  or
- a configuration with more points than classes.

Then we have a contradiction. So, under GH, (CH) fails for every such mu.

*Proof.* Steps:
1. *Rates.* Let chi^+_min, chi^-_max be as in the brief. Fix 0 < theta < min(chi^+_min, |chi^-_max|) and
   eta := theta/2.
2. *Asymptotics.* By Pesin theory [P] (for g_1 and for g_{-1}), points of the local strong stable manifold of a
   regular point a satisfy dist(g_m z, g_m a) <= C(a) e^{-theta m} for integers m >= 0. Interpolating to real
   t >= 0 with L' = max_{s in [0,1]} Lip(g_s) gives (S) with constant L' C(a) e^{theta}. Likewise (U).
3. *Growth.* For a mu-generic representative, J_t(rep) <= C(rep) + eta|t| for all t in both directions, since
   J_t/t -> 0. This gives (R).
4. *Conclusion.* All constants are finite, because the configuration is finite. Linear algebra (c), respectively
   (a), gives a nonzero solution of (G), and Theorem G gives the contradiction. ∎

Prop. 4.1 only uses that the representatives satisfy (R). It also applies to non-generic points whose Jacobian
grows sub-linearly.

**Hence (PE-NH) at mu(d) = 0 would follow from (CH).** Together with Prop. 6.1 and the (conditional) Prop. 6.2 of
round 6, this would complete the problem, apart from the large-|lambda| case (R1) discussed below.

### Where the argument stops (precise)

1. **(CH) is not available for non-hyperbolic mu.** The center bundle E^c has dimension c >= 2 (the flow
   direction plus at least one zero exponent). So dim W^{ss} + dim W^{uu} = n - c <= n - 2.
   - Closing an su-path into a cycle imposes c independent conditions (closure in the center directions,
     including the temporal direction).
   - Pesin leaves exist only through mu-typical points and vary only measurably (continuously on Pesin blocks,
     which are compact sets with empty interior in general). So no implicit-function argument can produce exact
     closures.
   - For hyperbolic measures, local product structure gives exact rectangles. Corollary G3 then gives another
     proof of Theorem 5.1 that avoids horseshoes. But hyperbolic measures are already excluded.
   - Whether positive entropy plus GH forces some "accessibility" that closes su-cycles is exactly the missing
     point. Nothing in GH that I can see produces it. The only global consequences of GH used so far are L1, F1,
     F2 (on distributions) and their corollaries: Lemma D (uniqueness of the nu-conformal measure), Corollary D1
     (supp mu = M if mu(d) = 0), and B3/B4 (conservativity).
2. **Approximate cycles do not suffice.** Suppose a cycle closes up to a center/temporal defect delta. Then S
   misses cancellation by a term of size delta · e^{J_t} ||phi||_{C^1}. That term does not decay when lambda = 0,
   whatever delta > 0 is, so Theorems J and J\* cannot be applied. Spreading the point masses along a center
   transversal (planner's mechanism (i)) replaces the defect by a derivative in the center direction. Center
   derivatives are not contracted in either time direction (zero exponents), so the C^k norm does not absorb
   them. This is the precise reason mechanism (i) stops.
3. **Mechanism (iii) (sub-exponential decay) is now rigorous (Theorem J\*), but does not help.** Two-sided
   cancellation is still needed, and the only source of cancellation is exponential asymptoticity along strong
   leaves; it is first-order, and exponential when it exists.
4. **Mechanism (ii) (continuation across Re z = 0).** I have nothing to add to round 6.
   - Lemma M needs a meromorphic continuation of single-orbit Laplace transforms.
   - For generic orbits of a non-hyperbolic measure there is no exact self-similarity, which is the ingredient
     Theorem B used.
   - Theorem J\* shows that "quasi-analytic" two-sided decay suffices, but this is still a decay statement for one
     fixed distribution, which is the same difficulty.
5. **Case (R1) (lambda <= -chi^+_min, or the symmetric case).** Theorem G does not help here.
   - The stable side can be exempted (J_t <= C - c t forward).
   - The unstable side needs cancellation at a rate > |lambda| >= chi^+_min. First-order cancellation (Theorem G)
     gives only the rate chi^+_min - delta.
   - Higher-order cancellation requires the non-stationary normal forms along W^u, as in round 6 Prop. 6.2. That
     citation remains unchecked in dimension of W^u >= 2.

## 5. Final status

**Proved here (in full, given the background results L1, F1, F2, Theorem J and the cited classical theorems).**
- Theorem J\*: the quasi-analytic version of Theorem J. Two-sided decay e^{-w(|t|)} with moments satisfying
  sum M_j^{-1/j} = inf (e.g. w(t) = t/log(e+t)) already forces S = 0 under GH. Cited: Denjoy-Carleman.
- Theorem G and Corollaries G1-G3: under GH, no finite configuration of distinct points grouped into exponentially
  forward-asymptotic and exponentially backward-asymptotic classes carries a nonzero class-wise cancelling weight
  vector, provided the representatives have Jacobian growth slower than the asymptotic rate. In particular:
  - no closed su-cycle with zero Jacobian holonomy;
  - with a smooth invariant volume, no closed su-cycle at all and no doubly exponentially asymptotic pair;
  - no configuration with more points than classes.
- Proposition 4.1: (PE-NH) at mu(d) = 0 follows from the configuration hypothesis (CH) (cited: Pesin theory).
- The chain's steps 2 and 4 are correct (Section 1).

**Not proved: (PE-NH) itself, hence the problem in dimension >= 4.**

**Open questions.**
- (Q1) = (PE0): under GH, is there an ergodic, non-hyperbolic mu with h_mu(g_1) > 0 and mu(d) = 0?
- (Q2) Configuration question: does every such mu (for a GH flow, or for any C^inf flow) admit a configuration (CH)?
  This would mean a closed su-cycle of mu-typical points with zero Jacobian holonomy, or a configuration with more
  points than classes. A yes answer settles (Q1) by Prop. 4.1.
- (Q3) Volume case: does a C^inf flow preserving a smooth volume omega, uniquely ergodic, with h_omega > 0 and
  non-hyperbolic, necessarily have a nondegenerate closed su-cycle of exponentially asymptotic points? A yes answer
  gives the problem in the volume-preserving case (Cor. G2).
- (Q4) Case (R1): tempered non-stationary normal forms along multi-dimensional Pesin unstable leaves, as needed
  for round 6 Prop. 6.2.

=== END OF ANSWER round7_q10 ===



