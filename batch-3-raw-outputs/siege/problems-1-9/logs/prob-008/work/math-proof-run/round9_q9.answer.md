# round9_q9 answer: (PE-NH) via a "non-uniform walk-map dimension count"

## 0. Status (read this first)

**(PE-NH) is NOT proved here, and no counterexample is given.** What this answer does:

1. It reduces the walk-map approach for (PE-NH) to one exact statement about Pesin blocks, using a compactness principle that is new here (Sections 2-3). The statement is "uniformly non-degenerate approximate closing of good su-walks". In the volume case one approximate coincidence of two walks is enough. In general four are needed (Lemma W of R8-f).
2. It proves two sufficient criteria for the missing non-injectivity (Section 4). Each is a complete proof of (PE-NH) for the measures to which it applies:
 - a coarea criterion: the walk map extends to a Lipschitz map of full rank on a positive-measure part of the good parameter set;
 - a co-Hölder criterion: the inverse of the walk map is Hölder with exponent alpha, and the dimension of the good parameters exceeds n/alpha.
3. It proves that neither hypothesis can be dropped by measure theory, regularity or topology alone (Section 5). There are Lipschitz injective maps from compact positive-measure sets of R^D into R^N with D > N, even with the "one smooth leg at a time" structure that walk maps have. Compact sets of almost full measure can be totally disconnected, so Hurewicz-type arguments cannot apply. This makes the brief's caution precise.
4. It analyses the dynamical renormalisation that could supply the missing hypothesis (Section 6).
 - A pigeonhole count (proved) gives pairs of walks whose parameters are separated by eps^{n/sigma} and whose endpoints are eps-close. Here sigma is a Frostman exponent of the good parameter set: sigma = k(u+s) in the volume case, and heuristically about k(delta^u + delta^s) in general.
 - A renormalisation hypothesis (RN) would turn this into the needed statement (conditional proposition, proved).
 - Renormalising by g_{±T} fails. Expanded legs leave every Pesin block, contracted legs degenerate, and the centre defect is neither contracted nor expanded. That is the exact point where the argument stops.
5. It records a heuristic observation (Section 7): commuting su-holonomies would produce cycles for free, so the real difficulty is "free" centre holonomy.

Everything labelled "proved" is proved below, modulo the cited standard theorems (Pesin blocks, coarea formula, McShane extension, Lemma W and Theorem G of the brief). Everything else is labelled sketch or heuristic.

## 1. Setting and notation (from the brief)

M is compact and connected, n = dim M >= 4 (entry 61 covers n <= 3), and X is GH. mu is ergodic and flow-invariant with h_mu(g_1) > 0, non-hyperbolic, and lambda := mu(d) = 0. This is the core case (PE0). The case lambda != 0 is discussed in Section 8.

Fix 0 < eta < theta < min(chi^+_min, |chi^-_max|).

**[PB]** Pesin blocks, quoted in R8-h. There are compact sets K_l with mu(K_l) -> 1 and constants r_l, C_l with the following properties. For z in K_l there are C^1 embedded closed discs W^{uu}_loc(z) and W^{ss}_loc(z) through z, of inner radius >= r_l, depending continuously on z in K_l in the C^1 topology, such that
- d(g_t y, g_t z) <= C_l e^{-theta|t|} for t <= 0 and y in W^{uu}_loc(z);
- d(g_t y, g_t z) <= C_l e^{-theta t} for t >= 0 and y in W^{ss}_loc(z);
- J_t(z) <= l + eta|t| for all real t and all z in K_l (possible since J_t/t -> 0 a.e.).

**Classes.** For x, y in M write x ~u y if limsup_{t->-inf} (1/|t|) log d(g_t x, g_t y) < 0, and x ~s y if the same holds as t -> +inf. Both are equivalence relations: d(g_t x, g_t z) <= d(g_t x, g_t y) + d(g_t y, g_t z), and the rate of the sum is the minimum of the two rates. These are the strong classes (shift 0).

**The su-graph Gamma.** The vertices are the ~s-classes and the ~u-classes. The edges are the points of M: the point y joins its ~s-class to its ~u-class. Gamma is a bipartite multigraph without loops.

**Good walks.** Fix l and k >= 1. A good chain of length 2k from a_0 in K_l is a sequence (a_0, a_1, ..., a_{2k}) of points of K_l with a_{2i-1} in W^{uu}_loc(a_{2i-2}) and a_{2i} in W^{ss}_loc(a_{2i-1}). It is beta-non-degenerate (beta > 0) if d(a_j, a_{j+1}) >= beta for every j.

In the non-volume case the classes are taken with the fixed rate theta, as follows. x ~u^theta y means: d(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0, for some C. x ~s^theta y is the same with t >= 0. Both are equivalence relations, since the sum of two O(e^{-theta|t|}) terms is O(e^{-theta|t|}). By [PB], consecutive points of a good chain are ~u^theta- or ~s^theta-related. In the volume case any theta > 0 will do, because J = 0.

## 2. From walks to Theorem G (proved)

**Lemma 2.1 (walks are graph walks).** Let c = (a_0, ..., a_{2k}) be a beta-non-degenerate good chain. In the graph Gamma_theta (vertices: the ~s^theta- and ~u^theta-classes; edges: points), the edge sequence a_0, a_1, ..., a_{2k} is a walk of length 2k+1 from the vertex [a_0]_s to the vertex [a_{2k}]_u. This walk is non-backtracking. Two different chains from the same a_0 give two different walks.
*Proof.* Edge a_0 joins [a_0]_s to [a_0]_u, and [a_0]_u = [a_1]_u because a_1 is in W^{uu}_loc(a_0). Edge a_1 runs from [a_1]_u to [a_1]_s = [a_2]_s, and so on alternately. Consecutive edges are distinct points, since d(a_j, a_{j+1}) >= beta > 0, so the walk is non-backtracking. A walk is its edge sequence, so different chains give different walks. ∎

**Lemma 2.2 (cycles from coincidences).** Let c, c' be two different beta-non-degenerate good chains of length 2k from the same a_0 in K_l, with a'_{2k} ~u^theta a_{2k}. (In particular this holds if a'_{2k} = a_{2k}, or if a'_{2k} is in W^{uu}_loc(a_{2k}) with a_{2k} in K_l.) Let U be the finite subgraph of Gamma_theta formed by the edges and vertices of the two walks. Then U contains a cycle. If four pairwise different such chains have pairwise ~u^theta-equivalent endpoints, then the cyclomatic number of their union is >= 2.
*Proof.* U is finite and connected, and it has no loops (Gamma_theta is bipartite). Both walks run from [a_0]_s to [a_{2k}]_u, they are non-backtracking, and they are different (Lemma 2.1). In a forest a non-backtracking walk is the unique path between its ends (step 1 of Lemma W, R8-f). So if U were a forest the two walks would coincide. Hence U contains a cycle. The second claim is Lemma W of R8-f: a connected loopless multigraph of cyclomatic number <= 1 carries at most 3 non-backtracking walks of a given length between two given vertices. ∎

**Proposition 2.3 (GH forbids such coincidences; proved from Theorem G of R7-a).** Assume GH.
(a) *Volume case* (nu = omega invariant, d = 0). There are no two different beta-non-degenerate good chains of equal length from a common a_0 with ~u^theta-equivalent endpoints.
(b) *General case* (mu as in Section 1, lambda = 0, [PB] with eta < theta). There are no four pairwise different such chains with pairwise ~u^theta-equivalent endpoints.
*Proof.*
(a) Take a simple cycle in U (Lemma 2.2), with edges z_1, ..., z_{2m} (distinct points) and vertices V_1, ..., V_{2m} (distinct classes), where z_i joins V_i and V_{i+1} (indices mod 2m).
- Every class of a point z_i is one of the V_j.
- Each V_j contains exactly the two cycle edges z_{j-1}, z_j among the points of Z = {z_1, ..., z_{2m}}; a third one would raise the degree of V_j in the simple cycle.
- So the classes of Theorem G (R7-a), restricted to Z, are the V_j, each with two points. Choose any representatives. (S) and (U) hold with the rate theta, by the definition of the theta-classes and finiteness. (R) holds with eta = 0, since J = 0.
- In the volume case all beta^s, beta^u vanish. The weights w_{z_i} = (-1)^i are nonzero, and each class contains two points of opposite sign, so the equations (G) hold.
- Theorem G gives a contradiction. (For m = 1 this is a pair x != y with x ~s y and x ~u y, which is Corollary G2.)
(b) By Lemma 2.2 the union U of the four walks has #edges >= #vertices + 1. Let Z be its edge set. The classes restricted to Z are the vertices of U, because each edge's two classes are vertices of U. (S) and (U) hold at rate theta. All points of Z lie in K_l, so J_t(z) <= l + eta|t|, which is (R) at any choice of representatives. The homogeneous system (G) has #Z unknowns and #vertices < #Z equations, so it has a nonzero solution. Theorem G gives a contradiction. ∎

So **(PE-NH) at lambda = 0 follows from the existence of such coincidences for one Pesin block**: two different walks in the volume case, four in general. This is the brief's dimension-count target, stated with vertex coincidence, which is weaker than point coincidence. It needs n - u, not n, transverse conditions.

## 3. A compactness principle: exact coincidences from uniformly non-degenerate approximate ones (proved)

Fix l, k, beta, and a_0 in K_l. Let Ch = Ch(a_0) be the set of beta-non-degenerate good chains of length 2k from a_0, viewed as a subset of K_l^{2k+1}.

**Lemma 3.1.** Ch is compact. The functions (c, c') -> d(a_{2k}, a'_{2k}) and (c, c') -> dist(a'_{2k}, W^{uu}_loc(a_{2k})) are continuous on Ch x Ch.
*Proof.* K_l^{2k+1} is compact, so it suffices to show that Ch is closed.
- "a_j in K_l" and "d(a_j, a_{j+1}) >= beta" are closed conditions.
- For "y in W^{uu}_loc(z)": write W^{uu}_loc(z) = iota_z(Bbar), where Bbar is a fixed closed ball and z -> iota_z is continuous from K_l to C^1 embeddings ([PB]). Let z_n -> z in K_l and y_n = iota_{z_n}(v_n) -> y. Pass to a subsequence with v_n -> v in Bbar. Uniform convergence of iota_{z_n} to iota_z and the equicontinuity of the family give iota_{z_n}(v_n) -> iota_z(v). So y = iota_z(v), and the relation {(z, y) : y in W^{uu}_loc(z)} is closed in K_l x M. The same holds for W^{ss}_loc.
- Continuity of the second function: z -> W^{uu}_loc(z) is continuous in the Hausdorff metric on compact sets, and dist(y, ·) is 1-Lipschitz for that metric. ∎

**Proposition 3.2 (exact from approximate).** Let gamma > 0. For chains c = (a_j), c' = (a'_j) put sep(c, c') := max_j d(a_j, a'_j).
(a) Suppose that for every eps > 0 there are c, c' in Ch with sep(c, c') >= gamma and dist(a'_{2k}, W^{uu}_loc(a_{2k})) < eps. Then there are c != c' in Ch with a'_{2k} in W^{uu}_loc(a_{2k}), i.e. with ~u^theta-equivalent endpoints.
(b) Likewise, if for every eps there are four chains with pairwise sep >= gamma and pairwise defects < eps, there are four pairwise different chains whose endpoints all lie in W^{uu}_loc of the first endpoint. These endpoints are pairwise ~u^theta-equivalent, because they lie in one local leaf of a point of K_l.
*Proof.* Take eps = 1/j and the corresponding pairs (resp. quadruples). By Lemma 3.1 a subsequence converges in Ch x Ch (resp. Ch^4). The limits satisfy sep >= gamma, a closed condition, so they are different. Their defect is 0, by continuity. Defect 0 means a'_{2k} in W^{uu}_loc(a_{2k}), since that set is compact. ∎

**Corollary 3.3 (the exact missing statement).** Under GH, (PE-NH) at lambda = 0 follows from:

**(AC)** For some l, k, beta, gamma > 0 and some a_0 in K_l, and for every eps > 0, there are four chains in Ch(a_0) with pairwise separation >= gamma and with endpoints pairwise within eps of each other's W^{uu}_loc. In the volume case two chains suffice.

*Proof.* Proposition 3.2 gives exact coincidences, and Proposition 2.3 excludes them. ∎

(AC) is a statement with a *fixed* separation gamma and an arbitrarily small defect. Section 6 explains why counting arguments give only separation of order eps^{n/sigma}, which tends to 0.

## 4. Two sufficient criteria for the coincidences (proved)

**Parametrisation.** By [PB], for z in K_l there are C^1 embeddings iota^u_z : Bbar^u -> W^{uu}_loc(z) and iota^s_z : Bbar^s -> W^{ss}_loc(z), with iota(0) = z, depending continuously on z in K_l. Here Bbar^u, Bbar^s are closed balls in R^u, R^s, with u = dim E^u and s = dim E^s.

For P = (v_1, w_1, ..., v_k, w_k) put a_{2i-1} = iota^u_{a_{2i-2}}(v_i) and a_{2i} = iota^s_{a_{2i-1}}(w_i), as long as the base points lie in K_l. Let A = A(a_0) ⊂ R^D, D = k(u+s), be the set of P for which all a_j lie in K_l and all legs are >= beta. Write F(P) := a_{2k}.

The map P -> chain is a continuous bijection from A onto Ch(a_0); it is injective because the iota are injective. A is closed, by induction as in Lemma 3.1, hence compact. If the legs are short, all endpoints lie in one chart around a_0, and we regard F as a map into R^n.

**Criterion 4.1 (coarea).** Suppose F = Ftilde|_A with Ftilde : R^D -> R^n Lipschitz, D > n. Suppose further that E := {P in A : Ftilde is differentiable at P and rank DFtilde(P) = n} has positive Lebesgue measure. Then some fibre A ∩ F^{-1}(y) is uncountable.
*Proof.* Coarea formula for Lipschitz maps R^D -> R^n, D >= n (Federer 3.2.12; Evans–Gariepy, Thm 3.11; cited):
 ∫_A J_n Ftilde dL^D = ∫_{R^n} H^{D-n}(A ∩ Ftilde^{-1}(y)) dL^n(y), with J_n Ftilde = (det DFtilde DFtilde^T)^{1/2} a.e.
J_n Ftilde > 0 on E, so the left side is positive. Hence H^{D-n}(A ∩ F^{-1}(y)) > 0 for a set of y of positive measure. A set of positive H^{D-n}-measure with D - n >= 1 is uncountable, since countable sets are H^{D-n}-null. ∎

**Corollary 4.2.** Under GH, (PE-NH) at lambda = 0 holds for every mu that has one Pesin block K_l, one a_0 in K_l, one k with k(u+s) > n, and one beta for which the walk map F of A(a_0) satisfies the hypothesis of Criterion 4.1. (It suffices that F be Lipschitz on A, since componentwise McShane extension gives a Lipschitz Ftilde, and that the rank condition hold on a positive-measure part of A.)
*Proof.* An uncountable fibre gives four (indeed infinitely many) pairwise different chains in Ch(a_0) with one common endpoint. Proposition 2.3(b) (and 2.3(a) in the volume case) excludes this. ∎

**Criterion 4.3 (co-Hölder).** If F is injective on A and F^{-1} : F(A) -> A is alpha-Hölder (0 < alpha <= 1), then dim_H A <= n/alpha. Hence, if dim_H A > n/alpha, then either F is not injective, or no inequality d(F(P), F(Q)) >= c|P - Q|^{1/alpha} holds on A.
*Proof.* An alpha-Hölder map g satisfies dim_H g(E) <= dim_H(E)/alpha. To see this, cover E by sets U_i of diameters r_i; their images have diameters <= C r_i^alpha; so H^{t/alpha}(g(E)) <= C' H^t(E). Apply this to g = F^{-1} and E = F(A) ⊂ R^n. ∎

*Remarks.*
- In the volume case, positivity of L^D(A(a_0)) holds for omega-a.e. a_0 and suitable l, beta. Then dim_H A = D = k(u+s), which exceeds any n/alpha for k large. This is cited, not proved here; it is the standard consequence of the absolute continuity of the Pesin laminations of a smooth measure (Pesin 1977; Barreira–Pesin), applied inductively to the legs with Fubini.
- So in the volume case Criterion 4.3 reduces (PE-NH) to a quantitative non-closing estimate: "if two good chains end eps-close, they are eps^alpha-close as chains". This is a quantitative injectivity (expansivity) property of good walks. Nothing in Pesin theory provides it.
- Criterion 4.1 needs regularity of F transverse to the leaves (Lipschitz dependence of the local manifolds on the base point, on K_l) together with "twisting at first order" (full rank). In general Pesin laminations depend only Hölder-continuously on the base point. The first-order effect of twisting (the bracket term, of size r^2 for legs of size r) is then swamped by the Hölder error (of size r^{1+alpha}). Neither hypothesis is available in general.

## 5. Measure, regularity and topology alone cannot give the coincidences (proved)

This makes the brief's caution precise, in the form relevant to walk maps.

**Proposition 5.1 (Lipschitz injective maps on fat sets, in "leg form").** Let D > N >= 1. There are a compact set A ⊂ [0,1]^D with L^D(A) > 0 and an injective Lipschitz map F : A -> R^N of the form
 F(x_1, ..., x_D) = (x_1, ..., x_{N-1}, sum_{i=N}^{D} phi_i(x_i)),
where each phi_i is the restriction to A's i-th factor of an increasing Lipschitz function on [0,1]. In particular the hypothesis "positive measure + Lipschitz + each leg enters separately and monotonically" does not force non-injectivity.
*Proof.*
1. *A fat Cantor set.* Fix 0 < c <= 1. Start from [0,1]. At stage j >= 1 remove from each of the 2^{j-1} closed intervals of stage j-1 the open central interval of length g_j = c 4^{-j}. This is possible: the stage-j intervals have length l_j = (l_{j-1} - g_j)/2 >= 2^{-j}(1 - c/2) > g_{j+1}. The total removed length is sum_j 2^{j-1} c 4^{-j} = c/2, so the limit set C has L^1(C) = 1 - c/2 > 0.
 Code points of C by binary sequences b(x) = (b_1(x), b_2(x), ...) (left = 0, right = 1). If b(x), b(x') first differ at index j, then x and x' lie in the two stage-j subintervals of one stage-(j-1) interval, so |x - x'| >= g_j = c 4^{-j}.
2. *The map.* Put A = C^D and D' := D - N + 1 >= 2. Relabel x_N, ..., x_D as y_1, ..., y_{D'}, and define
 Phi(y) = sum_{j>=1} sum_{i=1}^{D'} b_j(y_i) 3^{-((j-1)D' + i)} = sum_i phi_i(y_i), phi_i(y) := sum_j b_j(y) 3^{-((j-1)D'+i)}.
 - *Injective.* Phi(y) is the base-3 number whose digit string (in {0,1}) interleaves the codes of the y_i. Base-3 expansions with digits in {0,1} are unique: at the first differing digit m the values differ by at least 3^{-m} - sum_{m'>m} 3^{-m'} = 3^{-m}/2.
 - *Lipschitz.* If y != y', let j be the first stage at which some b_j(y_i) != b_j(y'_i). Then |y - y'| >= c 4^{-j}. The digit strings agree in the first (j-1)D' places, so
 |Phi(y) - Phi(y')| <= sum_{m > (j-1)D'} 3^{-m} = (1/2) 3^{-(j-1)D'} <= (1/2) 9^{-(j-1)} <= (9/2) 4^{-j} <= (9/(2c)) |y - y'|.
 - Each phi_i is increasing on C (the code is order-preserving) and Lipschitz by the same estimate. Linear interpolation across the gaps extends it to an increasing Lipschitz function on [0,1].
3. F(x) := (x_1, ..., x_{N-1}, Phi(x_N, ..., x_D)) is injective and Lipschitz on A, and L^D(A) = (1 - c/2)^D > 0. ∎

(By Criterion 4.1, any Lipschitz extension of this F necessarily has rank < N a.e. on A. That is the obstruction in its purest form: the "centre coordinate" Phi is a sum of devil's-staircase-type leg contributions.)

**Proposition 5.2 (topology is blind on Pesin-type parameter sets).** For every eps > 0 there is a compact totally disconnected K ⊂ [0,1]^D with L^D(K) > 1 - eps: take C^D with c small, as in 5.1. Every compact metrizable totally disconnected space embeds topologically in the middle-thirds Cantor set, hence in R (classical; cited). So on such parameter sets continuous injective maps into R^N exist for every N >= 1. Hurewicz's theorem and invariance of domain need parameter sets of positive covering dimension, and give nothing here.
*Proof.* This combines the construction of 5.1 with the cited embedding theorem. ∎

*Consequence.* Any proof of (AC), or of non-injectivity of the walk map, must use dynamics: equivariance under g_t, recurrence, the structure of the conditional measures. The positivity and dimension of the good parameter sets and the leafwise smoothness of the legs are not enough. In particular, approach (a) of the brief cannot be completed by measure and dimension counting alone.

## 6. What counting does give, and the renormalisation that would finish (proved / conditional / heuristic, as marked)

**Proposition 6.1 (pigeonhole with a Frostman measure; proved).** Let A ⊂ R^D be compact and F : A -> R^n Borel, with F(A) in a ball of radius R. Let m be a finite Borel measure on A with m(A) > 0 and m(B(P, r)) <= C_F r^sigma for all P and r (with sigma > 0). Then for every eps in (0, R):
(a) there are P, Q in A with |F(P) - F(Q)| <= eps and |P - Q| >= rho(eps)/2;
(b) there are P_1, ..., P_4 in A with |F(P_i) - F(P_j)| <= eps and |P_i - P_j| >= rho'(eps) for i != j.
Here rho(eps) = (m(A) eps^n / (C_F c_n R^n))^{1/sigma}, rho'(eps) = (m(A) eps^n / (4 C_F c_n R^n))^{1/sigma}, and c_n depends only on n.
*Proof.* Cover the ball by at most c_n (R/eps)^n Borel cubes Q_i of diameter <= eps. The sets E_i = F^{-1}(Q_i) cover A, so some E_i has m(E_i) >= M_0 := m(A) eps^n/(c_n R^n) > 0.
(a) E_i lies in the closed ball of radius diam E_i about any of its points, so M_0 <= C_F (diam E_i)^sigma; in particular diam E_i > 0. Pick P, Q in E_i with |P - Q| >= diam(E_i)/2.
(b) Let rho = rho'(eps), so that 3 C_F rho^sigma < 4 C_F rho^sigma = M_0. Pick P_1 in E_i. Then pick P_2 in E_i outside B(P_1, rho), P_3 outside the two balls, and P_4 outside the three balls. Each step is possible because at most three balls of radius rho carry m-mass at most 3 C_F rho^sigma < M_0 <= m(E_i). ∎

For walk maps, sigma is the Frostman exponent of a measure on A(a_0). In the volume case Lebesgue measure gives sigma = D = k(u+s) (Remark after 4.3). In general one expects sigma ≈ k(delta^u + delta^s), with delta^{u,s} the Ledrappier–Young dimensions of the conditionals; that is not proved here. So **for k large, counting produces pairs (and quadruples) of good chains whose endpoints are eps-close while their parameters are about eps^{n/sigma} apart, with n/sigma < 1**. This is the true content of the dimension count. (AC) needs separation bounded below. The gap between eps^{n/sigma} and a constant is a scale problem.

**Proposition 6.2 (conditional: a renormalisation hypothesis closes the gap; proved given (RN)).** Suppose there are kappa >= 1, C, gamma > 0, k, beta, l and a finite set {a_0^{(1)}, ..., a_0^{(q)}} ⊂ K_l with the following property.

(RN) Whenever c, c' (resp. c_1, ..., c_4) are chains in Ch(a_0) with pairwise separation >= delta and endpoints pairwise eps-close, there are chains in some Ch(a_0^{(i)}) with pairwise separation >= gamma and endpoints pairwise within C eps delta^{-kappa}.

Suppose further that A(a_0) carries a Frostman measure with exponent sigma > kappa n. Then (AC) holds for some a_0^{(i)}. Under GH this gives a contradiction (in the volume case with pairs, in general with quadruples).
*Proof.*
1. By Proposition 6.1, for each eps there are pairs (resp. quadruples) with separation delta >= c eps^{n/sigma} and defect eps.
2. By (RN) they produce chains in some Ch(a_0^{(i)}) with separation >= gamma and defect <= C' eps^{1 - kappa n/sigma}, which tends to 0 as eps -> 0.
3. One index i occurs for a sequence eps_j -> 0. This is (AC) for a_0^{(i)}.
4. Corollary 3.3 (Propositions 3.2 and 2.3) finishes. ∎

**Why (RN) is not available (heuristic analysis; this is where the argument stops).** The natural candidates for (RN) are the time maps g_{±T} followed by a return to K_l.
1. *Directions.* Let the two chains first differ at leg j, by delta.
 - If leg j is an s-leg, g_{-T} with e^{chi T} ≈ 1/delta expands that difference to size ~1.
 - But g_{-T} also expands every other s-leg of the chains to length ~ r e^{chi T} >> r, out of the local manifolds. And it contracts every u-leg to ~ r e^{-chi T}, destroying beta-non-degeneracy.
 - g_T has the opposite effects.
 - A chain contains both kinds of legs, so no single time map keeps a chain in a compact family Ch(·). (In uniformly hyperbolic or uniformly partially hyperbolic dynamics one can re-cut the long legs into short ones, because every point is "good". Here the intermediate points of an expanded leg need not lie in any Pesin block.)
2. *Corners.* The 2k+1 corners lie on different orbits. u-related corners synchronise in backward time and s-related corners in forward time. Simultaneous return of all corners to K_l under g_{±T} is not given by recurrence of a single point.
3. *Defect.* The endpoint defect eps has a component in E^c_0 (exponent 0) which g_{±T} neither contracts nor expands. Its s-component (for g_{-T}) is multiplied by up to e^{chi_max T}. Even ignoring 1-2, the best one can hope for is kappa ≈ chi_max/chi_min, so (RN) would need sigma > n chi_max/chi_min. That is harmless, since sigma grows linearly in k. The real obstructions are 1-2.
4. *Twisting.* Points 1-3 are exactly where twisting (non-joint-integrability of E^u ⊕ E^s ⊕ RX along the support) would have to produce exact closings. Uniformly (Theorem U) this is done by topology. In the non-uniform case topology is blind (Proposition 5.2), and measure plus regularity are blind (Proposition 5.1).

So the missing ingredient is a **non-uniform renormalisation (RN)**, or a substitute: some mechanism that turns the eps^{n/sigma}-separated, eps-close pairs of Proposition 6.1 into uniformly separated ones. I could not prove (RN) or any substitute.

## 7. A remark on commuting holonomies (heuristic; it explains which models are already killed)

Suppose good su-loops based at a good point x0 exist that close modulo the centre. That is, for chains c_1, c_2 from x0 the endpoints lie on the local centre plaque of x0, and the "centre holonomies" h_{c_1}, h_{c_2} (maps between local centre plaques) are defined. If h_{c_1} h_{c_2} = h_{c_2} h_{c_1} at a point, then the concatenations c_1 c_2 and c_2 c_1 are two different chains with the same endpoint, and Proposition 2.3 applies. This is the situation of group extensions with abelian fibre group (rotation cocycles over hyperbolic bases), where commutativity is exact.

So the walk method fails only when the centre holonomy pseudogroup acts "freely". Then an exact coincidence requires a nontrivial su-loop whose holonomy *fixes* a centre point exactly, and this is a fixed-point problem on totally disconnected parameter sets. I state this only as orientation. It is not a proof of anything beyond the abelian case, and I have not checked the abelian case in a non-uniform setting. (Abelian group extensions over hyperbolic bases are excluded under GH anyway, through their periodic orbits.)

## 8. The case lambda != 0

Not treated further here. As the brief records, it is excluded for -chi^+_min < lambda < 0 and 0 < lambda < |chi^-_max| (Prop. 6.1 of R6-a). It is excluded whenever the entropy is not concentrated in the exponents of size <= |lambda| (Prop. N of R7-c). It is excluded completely, modulo non-stationary normal forms along W^u (resp. W^s) (Kalinin–Sadovskaya, "Normal forms for non-uniform contractions", J. Mod. Dyn. 2017; cited from memory, hypotheses not re-checked), by the higher-order vanishing-moment argument of Prop. 6.2 of R6-a.

One point of that argument can be settled here. The worry (R6-d) that the generic points y_i might lie on an algebraic subvariety, degenerating the moment system, is unfounded. Take N + 1 distinct generic points of one unstable plaque, where N is the dimension of the space of polynomials of degree <= d_0 K on E^u (d_0 the degree bound of the sub-resonance group). The homogeneous moment system then has more unknowns than equations, hence a nonzero solution, whatever the positions of the points. Since the points are distinct, S = sum_i w_i delta_{y_i} != 0. Points are available by Lemma 6.0 (non-atomic conditionals).

## 8a. A possible route in the volume case (heuristic only; not used above)

In the volume case two facts help.
- Theorem G needs no genericity: J = 0, so (R) holds everywhere.
- Good corners form a set of *full* leaf measure on almost every leaf, because the Pesin laminations of a smooth measure are absolutely continuous (cited).

So topology fails (Prop. 5.2), but a "measure-theoretic intermediate value theorem" might replace it. The picture, for dim M = 4 (exponents chi, 0, 0, -chi):
- In the 3-dimensional quotient by the flow, the condition that a returning stable curve W^{ss}(y), y in W^{uu}(a_0), meets the weak-unstable leaf of a_0 again is one real condition. The point y carries one real parameter, and so does the base point a_0.
- Suppose the solution set Z of this condition, taken for continuous extensions of the leaf families, were (locally) the graph of a homeomorphism psi between parameter intervals such that psi and psi^{-1} map null sets to null sets.
- Then, because the good parameters have full measure, Z would meet the set of good parameter pairs in a set of positive (indeed full) one-dimensional measure along Z.
- That would give infinitely many exact 2-cycles between the same two vertices, i.e. three edges joining two vertices, which has cyclomatic number 2. Theorem G of R7-f then applies.

The missing lemma is therefore: **the closing correspondence of su-walks is absolutely continuous**, for instance because it is a composition of Pesin holonomies, which are absolutely continuous for smooth measures.

I could not prove this. The correspondence is defined through intersections of leaves, not through holonomies, and the leaf families are only a.e. defined, with continuous extensions existing only on Pesin blocks. Whether Z is a graph at all, i.e. whether there is transversality in the parameters, is the twisting question once more. I record this only as the most concrete direction I see for the volume case.

## 9. Summary: proved, conditional, open

**Proved here (modulo [PB], Theorem G of R7-a, Lemma W of R8-f, and the cited coarea / Hölder / embedding facts):**
1. Lemma 2.1, Lemma 2.2 and Proposition 2.3: under GH (lambda = 0), two different good walks of equal length with ~u^theta-equivalent endpoints are impossible in the volume case, and four are impossible in general. Vertex coincidence suffices, not point coincidence.
2. Lemma 3.1 and Proposition 3.2 (compactness principle): exact coincidences follow from approximate coincidences with a fixed separation. Hence (PE-NH) at lambda = 0 follows from (AC) (Corollary 3.3).
3. Criteria 4.1 and 4.3 and Corollary 4.2: (PE-NH) holds for every mu whose walk map on one Pesin block is Lipschitz of full rank on a positive-measure set, or has a Hölder inverse with dim_H A > n/alpha.
4. Propositions 5.1 and 5.2: these hypotheses cannot be replaced by positivity of measure, Lipschitz regularity, leg structure, or topology.
5. Propositions 6.1 and 6.2: counting gives eps^{n/sigma}-separated, eps-close pairs and quadruples. A renormalisation hypothesis (RN) with sigma > kappa n then yields (AC), hence (PE-NH).

**Not proved (open):**
- (AC) for non-hyperbolic positive-entropy mu with lambda = 0. By Prop. 3.2 (and trivially in the other direction) it is equivalent to the existence of two (resp. four) different good chains with ~u^theta-equivalent endpoints. It is open even in the volume case (CF flows), where Theorem G applies to all points.
- (RN), or any dynamical substitute for it.
- Whether the walk/graph method can work at all for measures whose centre holonomy is "free". If the weak su-graph of good orbits is a pseudoforest for some flow (R7-f), the method gives nothing for it, and the closed-range half of GH would have to be used. No route for that is known (R8-d, R8-e).
- The large-|lambda| case without the normal-form citation.

**Hence (PE-NH), and with it the problem's claim in dimension >= 4, remains open in this chain.** The claim is established, in the brief and in earlier blocks, for dim M <= 3, for hyperbolic measures, for uniformly partially hyperbolic GH flows with small |m(d)|, and for the bands of lambda listed in Section 8.

=== END OF ANSWER round9_q9 ===
