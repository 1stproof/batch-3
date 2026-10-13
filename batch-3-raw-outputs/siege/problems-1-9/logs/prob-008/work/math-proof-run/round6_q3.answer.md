# Answer to round6_q3 (attempt at (PE))

## Plan / status (written first, refined below)
Plan: (1) prove a clean new GH principle ("Theorem J"): under GH, no nonzero distribution u has
u o g_{-t} -> 0 exponentially fast in BOTH time directions (Laplace transform + Jordan-chain argument at z = 0).
(2) Build such distributions from (a) a hyperbolic periodic orbit with a homoclinic point (high-order
cancellation in Sternberg normal-form coordinates on the strong unstable manifold), (b) generic unstable pairs
when -chi^u_min < mu(d) < 0. (3) Consequences: no hyperbolic positive-entropy measures in any dimension;
zero entropy in dim <= 3. (4) State exactly what remains open (non-hyperbolic measures).

## 0. Conventions
nu is a fixed smooth positive density, d = div_nu X, J_t(x) = int_0^t d(g_s x) ds (all real t), so
(g_t)^*nu = e^{J_t} nu and J_{s+t}(x) = J_s(x) + J_t(g_s x). Generalized functions u in D'(M) pair with smooth
densities rho; Xu is defined by <Xu, rho> = -<u, L_X rho>. L1 (Text A): Xu = 0 implies u constant.
For u in D' and real t define u_t ("u o g_{-t}") by <u_t, rho> := <u, (g_t)^* rho>. For smooth u this is
u o g_{-t}. If S is the density functional S(phi) := <u, phi nu>, then
  <u_t, phi nu> = S(e^{J_t} . phi o g_t)      (since (g_t)^*(phi nu) = (phi o g_t) e^{J_t} nu).
For S = delta_y this is e^{J_t(y)} phi(g_t y).

Facts: t -> (g_t)^* rho is a C^1 (indeed smooth) curve in the Frechet space of smooth densities with derivative
(g_t)^* L_X rho = L_X (g_t)^* rho. Hence f_rho(t) := <u_t, rho> is C^1 with f_rho'(t) = <u_t, L_X rho>.

## 1. Theorem J (proved; GH only, any dimension)
**Theorem J.** Assume GH. Let u in D'(M) and suppose there are k, C, delta > 0 with
  |<u_t, phi nu>| <= C e^{-delta|t|} ||phi||_{C^k}   for all real t and all smooth phi.     (DEC)
Then u = 0.

*Proof.*
1. For z in the strip Sigma = {|Re z| < delta} put U_z(rho) := int_R e^{-zt} <u_t, rho> dt. By (DEC) the
   integral converges absolutely and |U_z(phi nu)| <= 2C ||phi||_{C^k} / (delta - |Re z|). So U_z is a
   distribution of order <= k. For fixed rho, z -> U_z(rho) is holomorphic on Sigma (differentiate under the
   integral; |t|^m e^{(|Re z|-delta)|t|} is integrable locally uniformly in z), and
   U_z^{(m)}(rho) = int (-t)^m e^{-zt} <u_t, rho> dt, which again is a distribution of order <= k.
2. Eigen-relation. U_z(L_X rho) = int e^{-zt} f_rho'(t) dt = [e^{-zt} f_rho(t)]_{-inf}^{inf} + z U_z(rho)
   = z U_z(rho); the boundary terms vanish since |e^{-zt} f_rho(t)| <= C' e^{(|Re z| - delta)|t|}.
   Thus <X U_z, rho> = -U_z(L_X rho) = -z U_z(rho): X U_z = -z U_z on Sigma.
3. Jordan chain at z = 0. Differentiating U_z(L_X rho) = z U_z(rho) m times in z and setting z = 0, with
   V_m := U_0^{(m)}: V_m(L_X rho) = m V_{m-1}(rho), i.e. X V_m = -m V_{m-1} (m >= 1), and X V_0 = 0.
   Claim: V_m = 0 for all m. By L1, V_0 is a constant c_0. Suppose V_{m-1} = c_{m-1} is constant. Then
   X V_m = -m c_{m-1} is smooth, so V_m is smooth by GH; a smooth w with Xw = const on a compact manifold has
   const = 0 (evaluate at a maximum point of w). So c_{m-1} = 0, i.e. V_{m-1} = 0, and then X V_m = 0, so V_m is
   a constant c_m by L1. By induction every V_m vanishes.
4. For each rho, z -> U_z(rho) is holomorphic on the connected strip Sigma with all derivatives zero at 0, so
   U_z(rho) = 0 on Sigma. Taking z = i omega: the continuous L^1 function f_rho has identically zero Fourier
   transform, so f_rho = 0; in particular <u, rho> = f_rho(0) = 0. Hence u = 0. QED

Remarks. (i) The proof only uses that some holomorphic family of eigen-distributions X U_z = -z U_z on a
connected open set containing 0 is not identically zero; Theorem J is the natural way to produce one.
(ii) Sanity check: for a Diophantine linear flow on T^n (GH), u -> u o g_{-t} is an isometry of every H^{-k},
so (DEC) indeed never holds for u != 0.
(iii) Theorem J contains Lemma C (u = delta_x/nu with J_t(x) <= b - a|t|) and explains why every earlier
construction stopped exactly when 0 was on the boundary of the strip of convergence.

## 2. Theorem 2: periodic orbits with volume-contracting strong-unstable connections (proved modulo two cited classical theorems)

Cited (from memory):
[SM] Stable/unstable manifold theorem for a hyperbolic periodic orbit O of a C^inf flow, period P, q in O:
  the strong unstable manifold W^uu(q) = {y : d(g_{-t} y, g_{-t} q) -> 0 as t -> +inf} is a C^inf injectively
  immersed manifold tangent to E^uu(q); convergence is exponential; for small eps the local manifold
  W^uu_eps(q) is an embedded C^inf disc, F := g_P maps it over itself, G := F^{-1} restricted to it is a C^inf
  contraction fixing q (all eigenvalues of DG(q) of modulus < 1), and g_{-nP} y lies in W^uu_eps(q) for all
  large n if y in W^uu(q). Also W^u(O) = union_s W^uu(g_s q), and similarly for stable manifolds.
[St] Sternberg's theorem (with Poincare-Dulac): a C^inf germ G of (R^m, 0) with G(0) = 0 and all eigenvalues
  of A = DG(0) of modulus < 1 is C^inf-conjugate, near 0, to a polynomial N(tau) = A tau + (finitely many
  resonant monomials), where after a linear change A is in block form by moduli, and a monomial tau^alpha
  (|alpha| >= 2) appears in component i only if |mu_i| = prod_j |mu_j|^{alpha_j} (mu = eigenvalues).

**Lemma 2.1 (bounded degree of iterates).** With N as in [St] there is D such that every iterate N^n is a
polynomial map of degree <= D.
*Proof.* Give tau_j the weight kappa_j = -log|mu_j| > 0 (for coordinates of the block of modulus |mu_j|).
The linear part preserves the blocks, so component i of A tau is weighted-homogeneous of weight kappa_i;
a resonant monomial tau^alpha in component i has weight sum_j alpha_j kappa_j = kappa_i. So each component N_i
is weighted-homogeneous of weight kappa_i. Substituting weighted-homogeneous polynomials of weights kappa_j
for tau_j into a weighted-homogeneous polynomial of weight kappa_i gives a weighted-homogeneous polynomial of
weight kappa_i; by induction every component of N^n is weighted-homogeneous of weight kappa_i. A monomial of
weight kappa_i has ordinary degree <= kappa_i / min_j kappa_j. So D = max kappa / min kappa works. QED

**Theorem 2.** Assume GH. Let O be a hyperbolic periodic orbit, period P, q in O, with
I := int_0^P d(g_s q) ds < 0 and E^uu(q) != 0. Then there is no point y in W^uu(q), y != q, with
J_t(y) <= b - a t for all t >= 0 (some a > 0, b).

*Proof.* Suppose y is such a point.
1. Coordinates. Let m = dim E^uu. By [SM] and [St], there are a neighbourhood D of q in W^uu_eps(q) and a C^inf
   chart tau: D -> R^m, tau(q) = 0, in which G = g_{-P}|_D reads tau -> N(tau), N as in [St]. Fix c with
   max|mu_j| < c < 1 and an adapted norm; shrinking, assume B := tau(D) is a closed ball of radius r in that norm
   with |N(tau)| <= c|tau| on B, so N(B) ⊂ B and |N^n tau| <= c^n r.
   Since N^n is a polynomial of degree <= D (Lemma 2.1) and all norms on the finite-dimensional space of such
   polynomial maps are equivalent, ||N^n||_{C^l(B)} <= C_l c^n for every l.
2. The weight. Let j := J_{-P} o tau^{-1} on B (smooth), j(0) = J_{-P}(q) = -I = |I| > 0. Put
   W(tau) := sum_{k>=0} [ j(N^k tau) - j(0) ]. By step 1 and the chain rule each term is O(c^k) in C^l(B),
   so W is C^inf on B. Cocycle: for y' in D and n >= 0,
     J_{-nP}(y') = sum_{k<n} J_{-P}(G^k y') = n|I| + W(tau(y')) - W(N^n tau(y')).
3. The points. By [SM], y_0 := g_{-n_0 P} y lies in D for n_0 large. Put y_i := G^i(y_0) = g_{-(n_0+i)P} y,
   i = 0..L. They are distinct: if y_i = y_l (i < l) then G^{l-i} y_i = y_i; but G^{l-i} is a contraction of D
   (|N^n tau| <= c^n |tau|) whose only fixed point is q, so y_i = q and then y = g_{(n_0+i)P} q = q, excluded.
   Fix K with e^{|I|} c^K < 1, let Pol be the space of real polynomials on R^m of degree <= (K-1)D, and take
   L + 1 > dim Pol. Then there are reals a'_0..a'_L, not all 0, with sum_i a'_i Q(tau_i) = 0 for all Q in Pol,
   where tau_i = tau(y_i) (linear dependence of L+1 vectors in R^{dim Pol}). Put a_i := a'_i e^{-W(tau_i)} and
   S := sum_i a_i delta_{y_i}, u := S/nu (so <u, phi nu> = S(phi)). S != 0 since the y_i are distinct.
4. Forward decay. y_i = g_{-s_i} y with s_i >= 0, and J_t(g_{-s} y) = J_{t-s}(y) - J_{-s}(y). Hence
   J_t(y_i) <= b_i - a t for all t >= 0, and |<u_t, phi nu>| = |sum a_i e^{J_t(y_i)} phi(g_t y_i)|
   <= C e^{-a t} ||phi||_inf for t >= 0.
5. Backward decay. Let t = nP + r, n >= 0, r in [0, P). Then g_{-t} = g_{-r} o g_{-nP} and
   J_{-t}(y_i) = J_{-nP}(y_i) + J_{-r}(g_{-nP} y_i). With step 2,
     <u_{-t}, phi nu> = e^{n|I|} sum_i a'_i Psi_{r,phi}(N^n tau_i),
   where Psi_{r,phi}(tau) := e^{-W(tau)} e^{J_{-r}(tau^{-1}(tau))} phi(g_{-r} tau^{-1}(tau)) on B.
   Since r ranges in a compact interval, ||Psi_{r,phi}||_{C^K(B)} <= C_K ||phi||_{C^K}. Write
   Psi = p + R with p its Taylor polynomial of degree K-1 at 0 and |R(tau)| <= C ||Psi||_{C^K} |tau|^K on the
   convex set B. Now p o N^n is a polynomial of degree <= (K-1)D, i.e. lies in Pol, so sum a'_i p(N^n tau_i) = 0.
   Therefore |<u_{-t}, phi nu>| <= e^{n|I|} sum|a'_i| C C_K ||phi||_{C^K} (c^n r)^K
   <= C'' (e^{|I|} c^K)^n ||phi||_{C^K}, which decays exponentially in t.
6. Steps 4-5 give (DEC) with k = K. Theorem J gives u = 0, contradicting S != 0. QED

Remark. Hyperbolicity of O is only used to have [SM]; the same proof works for a zero p of X with d(p) < 0
(use g_1 instead of g_P) and the strong unstable manifold of p.

**Corollary 2.2 (no homoclinic points).** Assume GH and dim M >= 2. Then no hyperbolic periodic orbit O has a
homoclinic point y in (W^u(O) ∩ W^s(O)) \ O.
*Proof.* By Observation P (background), I_O := int_O d != 0. If I_O > 0 replace X by -X: -X is GH (O4), has
the same orbit O with integral -I_O < 0, and W^u, W^s are exchanged, so y is still homoclinic. So let I_O < 0.
Since W^u(O) = union_s W^uu(g_s q) and W^s(O) = union_s W^ss(g_s q), y in W^uu(q1) and y in W^ss(q2) for some
q1, q2 in O; y != q1 as y is not in O. Forward: d(g_t y, g_t q2) <= C e^{-c t}, so
|J_t(y) - J_t(q2)| <= Lip(d) C / c for t >= 0, and J_t(q2) = (t/P) I_O + O(1). So J_t(y) <= b - a t with
a = |I_O|/P. Theorem 2 (with q = q1) gives a contradiction. QED

## 3. Consequences for entropy (proved modulo cited classical theorems)

Cited: [Rue] Ruelle's inequality; [LY-h] Katok's horseshoe theorem, flow version (Lian-Young): if mu is an
ergodic invariant probability of a C^2 flow, not carried by a zero of X, all of whose Lyapunov exponents other
than the flow direction are nonzero, and h_mu(g_1) > 0, then the flow has a horseshoe (a compact, locally
maximal, transitive hyperbolic set conjugate to a suspension of a mixing/transitive SFT of positive entropy);
in particular it has a hyperbolic periodic orbit O with a (transverse) homoclinic point y in W^u(O) ∩ W^s(O) \ O.
(In the symbolic model: a point whose past code is that of O and future code is that of O, but which is not
periodic.)

**Theorem 3.1.** Assume GH and dim M >= 2. Then every ergodic invariant probability mu with h_mu(g_1) > 0 is
non-hyperbolic: besides the flow direction it has at least one zero Lyapunov exponent.
*Proof.* mu is not carried by a zero of X (there g_1 = id on supp mu and h_mu = 0). If all non-flow exponents
were nonzero, [LY-h] would give a hyperbolic periodic orbit with a homoclinic point, contradicting
Corollary 2.2. QED

**Corollary 3.2 (the problem in dimension <= 3).** If dim M <= 3 and X is GH then h_top(g_1) = 0.
*Proof.* dim 1: a flow on the circle has zero entropy (g_1 is a circle homeomorphism; or: it is a time change of
a rotation away from zeros). For dim 2, 3, let mu be ergodic for the flow with h_mu(g_1) > 0. mu is not carried
by a zero; for mu-a.e. x the flow direction has exponent 0 (|Dg_t X(x)| = |X(g_t x)| is bounded, and by
Poincare recurrence it does not tend to 0). By [Rue] for g_1 and g_{-1}, mu has a positive and a negative
exponent. In dimension 2 this gives three exponents, impossible; in dimension 3 the exponents are
chi_1 > 0 = chi_2 > chi_3 with chi_2 the flow direction, so mu is hyperbolic, contradicting Theorem 3.1.
So every ergodic flow-invariant mu has h_mu(g_1) = 0, and step 2 of the chain (variational principle,
averaging a g_1-invariant measure over s in [0,1], ergodic decomposition; I checked it and it is correct)
gives h_top(g_1) = 0. QED

This settles in particular the dimension-3 configuration (H3) of [R5-d] (a uniformly volume-contracting
non-attracting horseshoe): it contains a hyperbolic periodic orbit with a homoclinic point, excluded by
Corollary 2.2. Note that Corollary 2.2 needs neither Proposition 4.0 nor the uniform volume-contraction of
Theorem 4.1: the sign of int_O d is handled by passing to -X.

## 4. Non-hyperbolic measures: what Theorem J gives, and where it stops

Let mu be ergodic, h_mu(g_1) > 0, lambda := mu(d) (independent of nu), chi^u_min > 0 the smallest positive and
-chi^s_min < 0 the negative exponent of smallest modulus (both exist by [Rue] for g_{+-1}).

Cited: [Pes] for mu-a.e. x the Pesin unstable manifold W^u(x) of g_1 (tangent to the positive exponents)
satisfies: for y in W^u_loc(x) and every eps > 0, d(g_{-t} x, g_{-t} y) <= C e^{-(chi^u_min - eps) t}, t >= 0
(integer times from Pesin theory, real times by the Lipschitz bound of g_{-s}, s in [0,1]).
[LY-na] (Ledrappier-Young / Ledrappier-Strelcyn) h_mu(g_1) > 0 implies that for mu-a.e. x the conditional
measures of mu on local unstable manifolds (w.r.t. a measurable partition subordinate to W^u) are non-atomic.

**Proposition 4.1 (proved modulo [Pes], [LY-na]).** Assume GH. Then there is no ergodic mu with h_mu(g_1) > 0 and
-chi^u_min < lambda < 0, and none with 0 < lambda < chi^s_min.
*Proof.* Let -chi^u_min < lambda < 0 and fix eps > 0 with 3 eps < chi^u_min - |lambda|, eps < |lambda|. The set
G of points with J_t(z)/t -> lambda as t -> +-inf has full mu-measure (Birkhoff), hence full conditional
measure on a.e. local unstable leaf; by [LY-na] that conditional measure is non-atomic, so there are x in G
satisfying [Pes] and y in G ∩ W^u_loc(x), y != x. Put theta = chi^u_min - eps. As in [R5-a] Thm B(a),
beta := lim_{t->+inf}(J_{-t}(x) - J_{-t}(y)) exists and |J_{-t}(x) - J_{-t}(y) - beta| <= K e^{-theta t}.
Let S = delta_x - e^beta delta_y, u = S/nu (nonzero since x != y).
Backward (t >= 0): writing e^{beta + J_{-t}(y)} = e^{J_{-t}(x)} e^{-r_t}, |r_t| <= K e^{-theta t},
|<u_{-t}, phi nu>| <= e^{J_{-t}(x)} (C ||d phi||_inf e^{-theta t} + K e^K e^{-theta t} ||phi||_inf)
<= C' e^{(|lambda| + eps - theta) t} ||phi||_{C^1}, using J_{-t}(x) <= (|lambda| + eps) t + C_eps (x in G).
The exponent |lambda| + 2 eps - chi^u_min is < 0.
Forward: |<u_t, phi nu>| <= (e^{J_t(x)} + e^{beta + J_t(y)}) ||phi||_inf <= C e^{(lambda + eps) t} ||phi||_inf,
and lambda + eps < 0. So (DEC) holds with k = 1, and Theorem J gives u = 0, a contradiction.
The case 0 < lambda < chi^s_min is the same for -X (GH by (O4); -X has the same measure mu, d replaced by -d,
exponents negated, unstable manifolds = stable manifolds of X). QED

**Proposition 4.2 (SKETCH, conditional on a cited normal-form theorem whose exact form I am not sure of).**
[NF] (non-stationary normal forms along Pesin unstable manifolds; I believe this is in Kalinin-Sadovskaya,
"Normal forms for non-uniform contractions", J. Mod. Dyn. 2017, but I cite it only from memory and conditionally):
for mu-a.e. x there are C^inf charts H_z : W^u_loc(z) -> E^u(z), z on the orbit of x, H_z(z) = 0, with
tempered C^K bounds (||H_{g_{-n}x}^{+-1}||_{C^K} <= C_eps e^{eps n} on domains of radius >= e^{-eps n}), in which
g_{-1} : W^u_loc(g_{-n}x) -> W^u_loc(g_{-n-1}x) is a sub-resonance polynomial map of degree <= D (D depending
only on the Lyapunov spectrum); compositions of such maps are again of degree <= D.
If [NF] holds in this form, then under GH every ergodic mu with h_mu > 0 has lambda = 0.
*Sketch.* Let lambda < 0 (else use -X). Exactly as in Theorem 2: take x in G as in Prop. 4.1, L+1 distinct
points y_i in G ∩ W^u_loc(x) (non-atomic conditional, [LY-na]); the weights
J_{-n}(y_i) - J_{-n}(x) = W_x(tau_i) - W_{g_{-n}x}(N^{(n)} tau_i) with W smooth and tempered, where N^{(n)} is
the composed normal-form polynomial, |N^{(n)} tau| <= C e^{-(chi^u_min - eps) n}|tau|; choose K with
K chi^u_min > |lambda| + (K + 3) eps... (i.e. K large and eps small), coefficients a'_i annihilating all
polynomials of degree <= (K-1)D at the points tau_i. The backward pairing is
e^{J_{-n}(x)} sum a'_i Psi_n(N^{(n)} tau_i) = O(e^{(|lambda| + eps) n} e^{eps n} e^{-K(chi^u_min - eps) n}),
which decays; forward decay is e^{(lambda + eps)t} since all y_i are in G. Theorem J gives the contradiction.
The unchecked points are exactly the form of [NF] (tempered bounds, uniform degree) and the tempered smoothness
of the weight W along the orbit.

**What remains open: lambda = 0 with mu non-hyperbolic (needs dim M >= 4).**
By Theorem 3.1 and Props. 4.1-4.2 the only case left (unconditionally: non-hyperbolic mu with lambda = 0, or with
lambda outside the ranges of Prop. 4.1) is a non-hyperbolic positive-entropy ergodic mu. For lambda = 0 the
mechanism of Theorem J needs cancellation in BOTH time directions, because e^{J_{+-t}} = e^{o(t)} decays in
neither. Point masses on one unstable leaf give only backward cancellation (strip 0 < Re z < theta, with 0 on the
boundary: this is exactly the old obstruction), and on one stable leaf only forward cancellation.
Linear-algebra reformulation of what would suffice: finitely many generic points z_k, each lying in one
"stable class" (points pairwise exponentially asymptotic forward) and one "unstable class"; first-order
cancellation imposes one linear equation per class on the coefficients; so a nonzero solution exists as soon
as the bipartite graph (classes = vertices, points = edges) has more edges than vertices, e.g. a 3 x 2
"rectangle" x_1, x_2, x_3 on one unstable leaf and their stable-holonomy images x'_1, x'_2, x'_3 on another
unstable leaf. (A single su-cycle (4 points) is not enough: its solvability is a holonomy condition on d which
fails in general.) Such rectangles exist under local product structure, i.e. for hyperbolic measures (already
excluded by Theorem 3.1); for non-hyperbolic mu, W^s(z) and W^u(z') generically do not meet
(dim W^s + dim W^u <= n - 2), and I could not produce such configurations. I also checked that the
pressure function P(q) = sup_m (h_m + q m(d)) does not force a positive-entropy ergodic measure with
lambda != 0 (P may be flat near q = 0), so the lambda = 0 case cannot be reduced away by that route.

## 5. Summary: proved / conditional / open
PROVED (GH only): Theorem J. Under GH no nonzero distribution u has u o g_{-t} -> 0 exponentially in (C^k)'
as t -> +-inf. (Laplace transform gives a holomorphic family of eigen-distributions X U_z = -z U_z on a strip
around 0; the Jordan chain at z = 0, using L1 and GH, kills all Taylor coefficients.)
PROVED modulo [SM], [St] (stable manifold theorem, Sternberg normal form): Theorem 2 and Corollary 2.2 —
under GH (dim >= 2) no hyperbolic periodic orbit has a homoclinic point; more precisely no hyperbolic periodic
orbit with int_O d < 0 has a point of its strong unstable manifold with exponentially decaying forward volume
Jacobian.
PROVED modulo [Rue], [LY-h] (Ruelle inequality, Katok/Lian-Young horseshoes): Theorem 3.1 — under GH every
positive-entropy ergodic measure is non-hyperbolic; Corollary 3.2 — the problem's claim h_top = 0 holds when
dim M <= 3. This removes configuration (H3) of the earlier dimension-3 reduction.
PROVED modulo [Pes], [LY-na]: Prop. 4.1 — (PE) for every ergodic mu with -chi^u_min < mu(d) < 0 or
0 < mu(d) < chi^s_min.
CONDITIONAL (sketch, on a non-uniform normal form theorem [NF] cited uncertainly): Prop. 4.2 — every positive-
entropy ergodic mu has mu(d) = 0.
OPEN: (PE) for non-hyperbolic ergodic mu with h_mu > 0 and mu(d) = 0 (possible only for dim M >= 4), and,
without [NF], also for non-hyperbolic mu with mu(d) != 0 outside the range of Prop. 4.1. Hence the problem's
claim (zero topological entropy) is NOT established here in dimension >= 4. The precise missing ingredient:
a finite (or distributional) combination of points/jets supported near a non-hyperbolic positive-entropy
measure whose weighted transfer decays exponentially in both time directions (Theorem J would then finish).
Step 2 of the chain: checked, correct.

=== END OF ANSWER round6_q3 ===
