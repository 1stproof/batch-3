# round4_q5 — answer (work in progress)

## Plan
1. Check the chain (V) + E14 + E15 + E16 => zero topological entropy.
2. Attack (V) with a first move not used before: **functional-analytic duality between X on C^infty and
   X on D'** (closed range theorem for Frechet spaces, applied to the transposed operator), i.e. a
   Fredholm-type comparison of the cokernels of X on C^infty and on D'. Target statement:
   (V) <=> X(D') is closed in D'  (under GH), and then try to prove closedness.

Notation: nu smooth positive density, d = div_nu X, so L_X(r nu) = ((X+d)r) nu. Distributions u in D'(M)
are generalized functions; distribution densities are elements of D'_dens = (C^infty)'. A smooth density
is w = rho nu. S := {smooth densities w : L_X w = 0}. I := invariant distribution densities.
All function spaces complex, but X and d are real, so real/imaginary parts of elements of S, I, X(D') stay there.

## Part 1. The chain (V) + E14 + E15 + E16 => h_top = 0

If dim M = 1, M = S^1 and every continuous flow on S^1 has zero topological entropy (g_1 is a circle
homeomorphism). Let dim M >= 2 and assume (V): a smooth positive density omega with L_X omega = 0.
* By E14, the flow is uniquely ergodic, so the only invariant Borel probability is omega/omega(M), which is
  therefore ergodic; X has no zeros and no periodic orbits.
* By the variational principle (for the time-one map g_1, and h_top of the flow := h_top(g_1)),
  h_top = sup_mu h_mu(g_1) = h_omega(g_1) (this is E15's first statement).
* Suppose h_omega > 0. Ruelle's inequality (cited from memory: for a C^1 diffeo and invariant mu,
  h_mu <= int sum of positive Lyapunov exponents) gives a positive exponent for omega (exponents are
  a.e. constant by ergodicity). Two cases:
  (a) no zero exponent transverse to X: omega is a hyperbolic ergodic measure of a C^infty flow without
      fixed points, with positive entropy; Katok's theorem for flows (from memory) produces horseshoes,
      in particular periodic orbits — contradicting E14. (This is E15's second statement.)
  (b) a zero transverse exponent and a positive exponent: excluded by E16.
  Hence h_omega = 0 and h_top = 0.

**Verdict on step 1.** The derivation is correct, *but it needs both (V) and E16*. (V) alone (with E14,
E15) settles only dim M <= 3 (in dim 3 the transverse space is 2-dimensional and, by volume preservation,
the transverse exponents sum to 0, so a positive one forces the other to be negative: case (b) cannot
occur; in dim 2 the transverse exponent is 0 by volume preservation, so h_omega = 0 by Ruelle).
So even a proof of (V) would leave E16 open in dim >= 4. I flag this explicitly.

## Part 2. Duality lemmas (new first move: comparing cokernels of X on C^infty and on D')

**Lemma A (transposed solvability).** Under GH: for every distribution density T with T(1) = 0 there is a
distribution density R with L_X R = T. Equivalently, X + d : D' -> D' has range exactly
{t in D' : <t, nu> = 0}, a closed hyperplane, and kernel {r : r nu in I}.

*Proof.* By E3, for every k there are m, C with ||u - mean(u)||_{C^k} <= C ||Xu||_{C^m} (u smooth).
Let T have order <= k, T(1) = 0. On the subspace X(C^infty) define S(Xu) := T(u). It is well defined since
ker X|_{C^infty} = constants (E2) and T(1)=0, and |S(Xu)| = |T(u - mean u)| <= C' ||Xu||_{C^m}.
Hahn–Banach extends S to a functional R' on C^infty continuous for the C^m norm, i.e. a distribution
density of order <= m with R'(Xu) = T(u) for all smooth u. Since R'(Xu) = -(L_X R')(u), R = -R' works. The
reformulation in terms of X + d is L_X(r nu) = ((X+d) r) nu. Necessity of <t,nu>=0: (L_X R)(1) = -R(X1) = 0. QED

**Lemma B (positive parts).** If w = rho nu in S with rho real (continuous suffices), then rho^+ nu and
rho^- nu are finite invariant measures and int d rho^{+-} nu = 0. Hence <d, w> = int d rho nu = 0 for all
w in S.

*Proof.* L_X w = 0 means g_t^* w = w, i.e. (rho o g_t) e^{J_t} = rho; since e^{J_t} > 0, the same identity
holds for rho^+, so mu := rho^+ nu is invariant. On the invariant set P = {rho > 0}, J_t = log rho - log rho o g_t.
By Birkhoff, J_t/t = (1/t) int_0^t d o g_s ds -> dbar mu-a.e., with int dbar dmu = int d dmu. Since log rho o g_t
has the same mu-distribution as log rho (finite on P), (log rho - log rho o g_t)/t -> 0 in mu-measure.
So dbar = 0 mu-a.e. and mu(d) = 0. Same for rho^-. QED

**Proposition C.** Under GH, (V) holds iff X(D') is closed in D' (strong topology).

*Proof.* (<=) D' is the dual of the Frechet–Montel (hence reflexive) space C^infty_dens, so for convex sets
strong closure = weak closure = weak* closure; a closed subspace equals the annihilator of its annihilator.
The annihilator of X(D') in C^infty_dens is {w : <Xu, w> = 0 for all u in D'} = {w : L_X w = 0} = S.
So X(D') = S^perp. By Lemma B, d in S^perp, so d = Xu for some u in D'; GH gives u smooth, and
omega := e^{-u} nu satisfies L_X omega = e^{-u}(d - Xu) nu = 0. (u can be taken real: replace by Re u.)
(=>) If omega is a smooth invariant positive density, use omega as reference density: then d = 0 and
Lemma A says X(D') = {t : <t, omega> = 0}, closed. QED

**Corollary D.** Under GH:
(i) (V) <=> d in X(D') (then d = Xu with u smooth by GH); and d in cl_{D'} X(D') = S^perp *always* (Lemma B).
So if (V) fails, d is in the closure of X(D') but not in X(D'): X(D') is not closed.
(ii) If S = {0}, X(D') is dense in D' and is a proper subspace: if X(D') = D' then
C^infty = C^infty ∩ X(D') = X(C^infty) (GH), so I = X(C^infty)^perp = 0, contradicting Krylov–Bogolyubov.
(iii) C^infty ∩ X(D') = X(C^infty) (GH); in general the obstruction lives exactly in
(C^infty ∩ S^perp) / X(C^infty): (V) fails iff this quotient contains the class of d.

So the whole of (V) is reduced to the closedness of the range of X on D', equivalently (Frechet closed-range
theorem, cited from memory) closedness of the range of the transpose X + d on C^infty, i.e. an estimate
dist_{C^k}(v, S) <= C ||(X+d) v||_{C^m}. This is a "GH-type estimate for the transposed operator,
without the regularity statement", weaker than GH of X + d.

**Why this does not close.** GH of X gives closed range of X on C^infty (E3) and hence, by duality,
closed range of X + d on D' (Lemma A). The two remaining "corners" — X on D' and X + d on C^infty — are
dual to each other and each is equivalent to (V) (Prop. C). Nothing in GH of X (a statement about
X^{-1}(C^infty)) transfers to them: GH controls preimages of *smooth* data, while closedness of X(D') concerns
limits of X u_j with *distributional* data. If (V) fails, non-closedness means there are smooth v_j with
(X+d)v_j -> 0 in every C^m but dist_{C^k}(v_j, S) = 1 (approximate invariant densities oscillating more
and more); bounded in C^k they converge in C^{k-1} to an invariant density in C^{k-1}, possibly 0, so no
contradiction arises. This is exactly the expected behaviour near singular (SRB-like) invariant measures,
so this route is a reformulation, not a proof.

## Part 3. Further rigorous reductions of (V)

**Proposition E (bounded distortion).** Under GH (using E11): (V) <=> sup_{t in R} ||J_t||_{L^infty} < infinity.
*Proof.* (=>) If omega = e^{a} nu is invariant, g_t^* omega = omega gives J_t = a - a o g_t, bounded by 2||a||_infty.
(<=) Let |J_t| <= B for all t. The density sigma_t of (g_t)_* nu = (g_{-t})^* nu is e^{J_{-t}} in [e^{-B}, e^{B}].
Cesaro averages (1/T) int_0^T sigma_t dt lie in this order interval of L^infty; a weak* (L^infty = (L^1)') limit
rho along T_j -> infinity satisfies e^{-B} <= rho <= e^B, and rho nu is invariant because
||(g_s)_* nu_T - nu_T||_TV <= 2|s| e^B nu(M)/T. Then F = log rho is bounded and, from (rho o g_t) e^{J_t} = rho,
F o g_t - F = int_0^t (-d) o g_s ds, so by E11 F is smooth, X F = -d, and e^F nu is a smooth invariant volume. QED

**Proposition G (approximate invariant volumes).** (No GH needed.) The following are equivalent:
(a) mu(d) = 0 for every X-invariant Borel probability mu (i.e. every ergodic invariant measure has zero
    sum of Lyapunov exponents);
(a') for every eps > 0 there is a smooth positive density nu_eps with sup |div_{nu_eps} X| < eps;
(a'') J_t / t -> 0 uniformly on M.
*Proof.* (a)=>(a'): the annihilator in C(M)' of the C^0-closure of X(C^infty) is the space of signed measures m with
m(Xu) = 0 for all smooth u, i.e. invariant signed measures (d/dt m(u o g_t) = m(X(u o g_t)) = 0). Their Jordan
parts are invariant (g_t is a homeomorphism, so (g_t)_* m^{+-} are the Jordan parts of (g_t)_* m = m), so by (a)
they all kill d; Hahn–Banach gives smooth real u with ||d + X u||_infty < eps; nu_eps := e^{u} nu has
div = d + Xu. (a')=>(a''): with nu_eps = e^{u} nu, J_t = J^eps_t + u o g_t - u... precisely
J_t = int_0^t (d + Xu) o g_s ds - (u o g_t - u), so |J_t| <= eps t + 2||u||_infty. (a'')=>(a): mu(d) = mu(J_t)/t. QED

**Consequence.** Under GH, (V) <=> (a) and (b), where
(b) every invariant distribution T in I (not only measures) satisfies T(d) = 0; given (a), this says that
    d, which then lies in the C^0-closure of X(C^infty), actually lies in X(C^infty) (= its C^infty-closure, E3).
(Proof of the consequence: (V) <=> d in X(C^infty) <=> T(d) = 0 for all T in I by E3; (b) is that, and (a) is the
special case of measures.)
(a) is a statement about invariant measures only; (b) is the part of (V) invisible to measures. Neither is
proved here. Known pieces of (a): E8 and E4 show (a) FAILS at a zero (delta_p(d) = d(p) != 0) or at a periodic orbit
(mu_gamma(d) = log|det Poincare| / period != 0). So (a), hence (V), already contains the statement
"a GH vector field has no zeros and no periodic orbits", which is open here.

**Lemma H (jet non-resonance at zeros; extends E8).** Under GH, if X(p) = 0 and lambda_1..lambda_n are the eigenvalues
(with multiplicity) of A = DX(p), then tr A + sum alpha_i lambda_i != 0 for every multi-index alpha in N^n.
*Proof.* In coordinates at p let V_k = span{ phi -> (partial^alpha phi)(p) : |alpha| <= k }, viewed as generalized
functions via phi nu <-> phi; finite-dimensional. For u in V_k, (Xu)(phi) = -u(X phi + d phi). Since X(p)=0,
partial^alpha (X_i partial_i phi)(p) involves only derivatives of phi of order <= |alpha|, with top-order part
sum_{i,j} alpha_j (partial_j X_i)(p) partial^{alpha - e_j + e_i} phi(p); and d(p) = tr A. So V_k is X-invariant and on
V_k/V_{k-1} X acts as -(tr A + (derivation induced by A on degree-k symmetric tensors)), with eigenvalues
-(tr A + alpha.lambda), |alpha| = k. A zero eigenvalue would give 0 != u in V_k with Xu = 0, u not smooth,
contradicting GH. QED
(This forbids resonant zeros but does not forbid zeros; global stable/unstable manifolds of saddles obstruct the
local cut-off constructions that work for sinks/sources, cf. E13.)

## Part 4. Other first moves examined (dead ends, with reason)

1. **Family X + z d, z in C.** (V) (d = Xa) implies ker_{D'}(X + z d) contains e^{-z a} for every z, and
   X + z d = e^{-za} X e^{za} is GH for all z. Conversely a nowhere-vanishing smooth kernel element u_z for one z != 0
   gives z d = -Xu_z/u_z, i.e. z d = -eta(X) for the closed 1-form eta = du_z/u_z; for real z and real u_z
   (constant sign) this is (V) with a = -log|u_z|/z; for z = i lambda, Re eta(X) = X log|u_z| = 0 forces |u_z| const
   (E2), and Im eta = closed real 1-form theta = da' + h (h in a finite-dim space of representatives of H^1) gives
   lambda d = -X a' - h(X), i.e. (V) modulo the finite-dimensional asymptotic-cycle obstruction. But GH of X gives no
   control of X + z d for z != 0 (perturbation theory fails: 0 is not isolated in any spectrum of X — already
   for Diophantine linear flows the L^2-spectrum of X is dense in iR), and the first-order perturbation equation
   is Xu_1 + d = E_1, which is (V) itself. Dead end: circular.
2. **Semigroups e^{t(X + s d)} and "pressure" q(s) = limsup (1/t) log int e^{s J_t} dnu.** q is convex,
   q(0) = q(1) = 0 (mass conservation int e^{J_t} dnu = nu(M)), so q <= 0 on [0,1]; (V) => q == 0. X + d/2 is
   skew-adjoint on L^2(nu) and int e^{J_t/2} dnu = <U_t 1, 1>. q(1/2) < 0 would mean exponential decay of a
   correlation of a unitary group — not contradicted by anything derived from GH. Dead end.
3. **Asymptotic cycles / currents.** T in I iff r i_X nu is a closed (n-1)-current (T = r nu), since
   L_X(r nu) = d(r i_X nu). The map I -> H^{n-1}(M; R) has kernel K = {T in I : T(h(X)) = 0 for all closed 1-forms h}.
   For Diophantine linear flows K = 0. Proving K = 0 under GH would give dim I <= b_1(M) and, via Schwartzman–Fried–
   Sullivan (from memory), a global cross-section; but already T = delta_p at a zero lies in K, so K = 0 contains
   "no zeros", again open. Dead end at the same place as (a).

## Summary of status
* Proved (given E2, E3, E11 and standard functional analysis): Lemma A, Lemma B, Proposition C
  ((V) <=> X(D') closed <=> d in X(D')), Proposition E ((V) <=> uniformly bounded log-Jacobians),
  Proposition G (characterization of the measure-theoretic half (a) of (V)), Lemma H (non-resonance at zeros).
* Part 1: (V) + E14 + E15 + E16 => h_top = 0 is a correct derivation; (V) + E14 + E15 alone give it only for
  dim M <= 3. E16 remains a separate open input in dim >= 4.
* NOT proved, open: (V) itself. The precise missing statements are:
  (Q1) closedness of X(D') in D' (equivalently of (X+d)(C^infty) in C^infty) under GH;
  equivalently (Q2) = (a) + (b): every invariant measure has zero exponent sum (which includes: no zeros,
  no periodic orbits), and every invariant distribution kills d.
  No counterexample was found; I see no mechanism for one, but also no proof.
* Literature note (from memory, not used in any proof): I believe the implication "GH => cohomology-free (hence
  smooth invariant volume)" is attributed to Forni in work on the Greenfield–Wallach/Katok conjectures, but I do not
  recall the argument and have not relied on it.

=== END OF ANSWER round4_q5 ===

