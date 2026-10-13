# round9_q1 — answer (work in progress)

## Plan (written first, updated as I go)
Target: the missing statement (EF) (no nonzero holomorphic order-<=1 eigen-family T_z o P = z T_z over an open
vertical strip, under GH), or directly zero entropy.
Lines I am pursuing:
1. Structure of eigen-families of order 0 (complex measures): Jordan chain + Radon-Nikodym => total dissipativity.
2. A "product" (tensor) form of Theorem J on M x M that turns one-sided decays of an unstable pair and of a
   stable pair into two-sided decay, and the exact spectral condition on X (+) X it needs.
3. Whatever GH gives at z != 0 through these.
Status markers: PROVED / SKETCH / OPEN.

Conventions as in the brief: nu smooth positive density, d = div_nu X, P = X + d, J_t(x) = int_0^t d(g_s x) ds,
Q_t phi := e^{J_t} (phi o g_t) (so Q_{t+s} = Q_t Q_s, d/dt Q_t phi = Q_t P phi = P Q_t phi), and for a complex Borel
measure m put L_t m := (g_t)_*(e^{J_t} m), so that (L_t m)(phi) = m(Q_t phi).

## 1. Order-0 Jordan chains force total dissipativity (PROVED; no GH used)

**Lemma 1.1.** Let z = kappa + i y in C, and let B != 0 and A be complex Borel measures on M with
 B(P phi) = z B(phi),  A(P phi) = z A(phi) + B(phi)  for all smooth phi.
Let beta := |B| (total variation). Then for beta-a.e. x,
 I_kappa(x) := int_R e^{J_t(x) - kappa t} dt < infinity.
In particular beta gives no mass to zeros of X or to periodic orbits.

*Proof.*
(a) Transport identities. For smooth phi, h(t) := A(Q_t phi) is C^1 (t -> Q_t phi is C^1 into C^0) with
h'(t) = A(P Q_t phi) = z h(t) + B(Q_t phi), and likewise B(Q_t phi) = e^{zt} B(phi). Hence
A(Q_t phi) = e^{zt}(A(phi) + t B(phi)). Both sides are C^0-continuous in phi (Q_t is bounded on C^0), so the
identities hold for continuous phi, i.e. L_t B = e^{zt} B and L_t A = e^{zt}(A + tB) as measures, and then for
bounded Borel phi.
(b) Elementary properties of L_t: it is positive, |L_t m| = L_t |m| (g_t is a Borel bijection and e^{J_t} > 0), it
preserves absolute continuity and mutual singularity, and if m = k n with k in L^1(n) then
L_t m = (k o g_{-t}) L_t n (direct change of variables).
(c) Polar part. By (b), L_t beta = |L_t B| = e^{kappa t} beta. Write B = h beta, |h| = 1. Then
L_t B = (h o g_{-t}) e^{kappa t} beta = e^{zt} h beta, so h o g_{-t} = e^{iyt} h beta-a.e., for each t.
(d) Lebesgue decomposition of A. Write A = k beta + A_s with A_s singular to beta. By (b),
L_t A = (k o g_{-t}) e^{kappa t} beta + L_t A_s, and L_t A_s is singular to L_t beta = e^{kappa t} beta. Comparing with
e^{zt}(A + tB) = e^{zt}(k + t h) beta + e^{zt} A_s and using uniqueness of the Lebesgue decomposition:
k o g_{-t} = e^{iyt}(k + t h) beta-a.e. Put q := k/h. By (c), q o g_{-t} = q + t beta-a.e., for each real t.
Let r := Re q (a real Borel function, defined beta-a.e.; fix a Borel version). Then for each t:
 r(g_{-t} x) = r(x) + t for beta-a.e. x.   (1.1)
(e) Integrability. Let E := {r in [0,1)} and, for n in Z, E_n := {r in [n, n+1)}. For each t, by (1.1),
g_t E = {x : r(g_{-t}x) in [0,1)} coincides beta-a.e. with {r in [-t, 1-t)}. Using L_t beta = e^{kappa t} beta
with the bounded Borel function 1_E o g_{-t}:
 int e^{J_t} 1_E dbeta = int e^{J_t} (1_E o g_{-t}) o g_t dbeta = e^{kappa t} int 1_E o g_{-t} dbeta = e^{kappa t} beta(g_t E).
By Tonelli,
 int_E I_kappa dbeta = int_R e^{-kappa t} int e^{J_t} 1_E dbeta dt = int_R beta(r in [-t, 1-t)) dt
  = int ( int_R 1{-r(x) <= t < 1 - r(x)} dt ) dbeta(x) = beta(M) < infinity.
(Joint measurability of (t,x) -> e^{J_t(x)} 1_E(x) is clear.) Hence I_kappa < infinity beta-a.e. on E. The same
computation with E_n (replace [0,1) by [n,n+1)) gives I_kappa < infinity beta-a.e. on each E_n, and the E_n cover
a beta-conull set. Finally, at a zero p, J_t(p) = t d(p) and I_kappa(p) = infinity; on a periodic orbit of
period T, J_{t+T} = J_t + J_T(x) and again I_kappa = infinity. ∎

**Corollary 1.2 (GH, dim M >= 2).** (i) There is no order-0 Jordan chain (A, B as in Lemma 1.1) at any z in iR.
(ii) For real kappa != 0, the set N_kappa := {x : I_kappa(x) < infinity} is nu-null, so in an order-0 Jordan chain
at z with Re z != 0, |B| is singular to nu and carried by N_{Re z}.
(iii) If X preserves a smooth positive density (statement (V)), there is no order-0 Jordan chain at any z, hence
no nonzero order-0 eigen-family on any strip.
*Proof.* (i) kappa = 0: Lemma C of the background (GH) says I_0(x) = int e^{J_t(x)} dt = infinity for every x.
(ii) For kappa > 0, I_kappa(x) >= int_{-inf}^0 e^{J_t(x)} dt, which is infinite nu-a.e. by B4 (backward); for
kappa < 0 use the forward half of B4. (iii) Take nu invariant, so d = 0, J = 0 and I_kappa = infinity everywhere.
For the eigen-family statement: if T_z is a nonzero EF of order 0 (bounded in total variation on closed substrips),
then T'_z(phi) = (2 pi i)^{-1} oint T_w(phi)(w-z)^{-2} dw is again a measure, and differentiating T_z o P = z T_z
gives T'_z o P = z T'_z + T_z; at any z with T_z != 0 this is an order-0 Jordan chain. ∎

**Corollary 1.3 (structure; PROVED modulo standard measurable cross-section bookkeeping).** In Lemma 1.1, B is a
superposition of single-orbit Laplace transforms: there are a Borel set Sigma meeting beta-a.e. orbit once, a
finite measure eta on Sigma and a bounded Borel c on Sigma with
 B(phi) = int_Sigma c(sigma) int_R e^{J_s(sigma) - z s} phi(g_s sigma) ds deta(sigma).
(Sketch: Sigma = {r = 0} via x -> g_{r(x)} x; beta is quasi-invariant (L_t beta = e^{kappa t} beta), so its
orbit-disintegration is equivalent to Lebesgue in the time parameter; the identity L_t beta = e^{kappa t} beta forces
the time density on the orbit of sigma to be const(sigma) e^{J_s(sigma) - kappa s}; the phase is h(g_s sigma) =
e^{-iys} h(sigma) by (c).)

*Scope.* This settles order-0 Jordan chains on the imaginary axis and reduces order-0 eigen-families to single
orbits with int e^{J_t - kappa t} dt < infinity, kappa != 0. It does NOT touch the families of Theorem R: those are
genuinely of order 1 (for no z are both single-orbit transforms of x and y convergent: forward convergence needs
Re z > lambda, backward needs Re z < lambda). Single-orbit families with kappa != 0 are themselves not excluded by
anything I know under GH (they are excluded under (V) by (iii)). So this is a sub-class result only.

**Remark 1.4 (order-0 eigen-measures on iR; PROVED).** Under GH, if B is a complex measure with B o P = iy B (y real),
then |B| = c nu and B = c h nu with h in L^inf(nu), |h| = 1, h o g_{-t} = e^{iyt} h nu-a.e. (Proof: by (c) above,
L_t|B| = |B|, i.e. |B|(Q_t phi) = |B|(phi); differentiating at t = 0 gives |B| o P = 0, so |B| = c nu by (F1).)
So order-0 point spectrum on iR = L^inf point spectrum of the (ergodic, Lemma D of R7-d) nu-class flow, and by
Corollary 1.2(i) it is semisimple at the order-0 level. I could not show such h are smooth.

## 2. A product form of Theorem J (PROVED reduction; it is a reformulation, not progress)

Put M2 = M x M, X2 = X(x)1 + 1(x)X, nu2 = nu(x)nu, P2 = X2 + d(x) + d(y), Q2_t = Q_t (x) Q_t. Let mu be ergodic with
h_mu > 0 and lambda = mu(d). Take an unstable pair (x, y) and a stable pair (x', y') of mu-generic points as in
Theorem R and its time reversal, S_u = delta_x - e^b delta_y, S_s = delta_{x'} - e^{b'} delta_{y'}, S2 = S_u (x) S_s != 0.
Grouping the four point masses by the second (resp. first) coordinate and using first-order cancellation in the
first (resp. second) variable, exactly as in Theorem R step 4:
 |S2(Q2_t Phi)| <= C e^{(-2 lambda + 2 delta - theta)|t|} ||Phi||_{C^1}  (t <= 0),
 |S2(Q2_t Phi)| <= C e^{( 2 lambda + 2 delta - theta')t} ||Phi||_{C^1}  (t >= 0).
So for |lambda| < min(theta, theta')/2 - delta (in particular in the open case lambda = 0) S2 has TWO-SIDED
exponential decay on M2. Steps 1-3 and 5 of Theorem J hold verbatim on M2 (no hypothesis on the field). Step 4
needs exactly:
 (N2) X2 has no Jordan chain at 0 on D'(M2): if v, w in D'(M2) (order <= 1), X2 v = 0 and X2 w = v, then v = 0.
Hence (N2) => h_mu = 0 whenever |mu(d)| is small, in particular in case (PE0).
Why this is only a reformulation: (N2) is at least as strong as the needed spectral statement. If T_z is an EF of X
near z0 and T' an eigen-density of X at -z0, then (T'_{z0} (x) T') o P2 = T_{z0} (x) T' and (T_{z0} (x) T') o P2 = 0,
a Jordan chain of X2 at 0. Since Theorem R for X and for -X (lambda = 0) gives eigen-families on (0, theta) and on
(-theta', 0), (N2) would already contradict positive entropy directly. And (N2) cannot come from (K0) on M2: X2 has a
huge kernel (e.g. functions of x - y for linear flows; the graphs of g_s in the volume case). (N2) does hold for
Diophantine linear flows (Fourier: X2 is diagonal on e_k (x) e_l). I see no way to derive (N2) from GH of X.

## 3. Volume case: the missing input localised to two forward orbits (PROVED; small sharpening of Theorem V)

**Proposition 3.1.** Assume GH and that X preserves a smooth positive density omega; take nu = omega, so P = X and
R := (X on mean-zero smooth functions)^{-1} is continuous (Text B, Cor. 3). Let x != y with
d(g_t x, g_t y) <= C_0 e^{-theta|t|} for t <= 0, S = delta_x - delta_y, and T_z(phi) = int_R e^{-zt}(phi(g_t x) - phi(g_t y)) dt
(0 < Re z < theta). For smooth mean-zero phi put
 D_N(phi) := sup_{t >= 0} |(R^N phi)(g_t x) - (R^N phi)(g_t y)|   (<= 2||R^N phi||_inf).
If D_N(phi) <= A_phi B_phi^N for all N, for every phi in a C^1-dense set of mean-zero smooth functions, then T = 0,
which is impossible (R5-a step (f)). Hence for every exponentially backward-asymptotic pair, some mean-zero smooth phi
has D_N(phi) growing faster than every geometric sequence.
*Proof.* Split T_z = B_z + G_z (backward/forward integrals). By R8-e Prop. 3.1(a),(b), B_j := int_{-inf}^0
((-t)^j/j!)(phi(g_t x) - phi(g_t y)) dt equals S o R^{j+1} on mean-zero functions and |B_j(phi)| <= C_0 theta^{-j-1}
||phi||_{C^1}. B_z(psi) = sum_j z^j B_j(psi) for |z| < theta. With psi = R^N phi: B_j(R^N phi) = S(R^{j+N+1} phi) =
B_{j+N}(phi), so |B_z(R^N phi)| <= 2 C_0 theta^{-N-1} ||phi||_{C^1} for |z| <= theta/2. Also |G_z(psi)| <=
sup_{t>=0}|psi(g_t x) - psi(g_t y)| / Re z, so |G_z(R^N phi)| <= D_N(phi)/Re z. Since T_z o X = z T_z and R^N phi is
smooth and mean zero, T_z(phi) = z^N T_z(R^N phi), whence for |z| <= theta/2, Re z > 0:
 |T_z(phi)| <= |z|^N ( 2 C_0 theta^{-N-1} ||phi||_{C^1} + A_phi B_phi^N / Re z ).
For |z| < min(theta/2, 1/(2B_phi)) the right side tends to 0 as N -> inf, so T_z(phi) = 0 on a half-disc, hence on
the strip. T_z has order 1 and the set is C^1-dense, and T_z(1) = 0, so T_z = 0. ∎
(With Lemma H of R7-e the geometric bound may be replaced by any log-convex Carleman sequence.)
*Where it stops.* D_N involves R^N phi at FORWARD times, where x and y separate along the unstable leaf. The leafwise
bounds of R8-e (geometric oscillation of R^N phi along local strong unstable and strong stable leaves, and the
trivial bound s K_{N-1} along flow segments of length s) would bound D_N geometrically if g_t x and g_t y could be
joined by su-paths (plus flow segments) of bounded combinatorial length through Pesin-regular points with uniform
constants. That is exactly local accessibility through regular points, which fails to be available for
non-hyperbolic mu (centre directions): the same obstruction as in R7-a §4, R7-f §3, R8-e §4.

## 4. Status

PROVED here (new):
- Lemma 1.1 (no GH): an order-0 Jordan chain at z makes |B| live on orbits with int_R e^{J_t - (Re z) t} dt < inf.
- Corollary 1.2: under GH no order-0 Jordan chain on iR; order-0 eigen-families off iR consist of nu-singular
  measures carried by such orbits, and (V) excludes them altogether; Remark 1.4 (order-0 spectrum on iR = L^inf
  point spectrum of the nu-class flow).
- §2: the tensor-product form of Theorem J: (N2) "no Jordan chain at 0 for X (x) 1 + 1 (x) X on D'(M x M)" implies
  h_mu = 0 for every ergodic mu with |mu(d)| < min(chi^+_min, |chi^-_max|)/2, in particular in the open case
  (PE0). It is a reformulation (as hard as the target), recorded only so that nobody re-derives it.
- §3: in the volume case the obstruction localises to geometric (or Carleman) growth of the forward two-orbit
  oscillation D_N(phi) of the iterated inverses R^N phi.
NOT proved: (EF) in general; (EF) for the order-1 families of Theorem R; zero topological entropy for GH flows in
dimension >= 4 (dimensions <= 3 are settled by Theorem 5.2 of R6-a, modulo the cited horseshoe theorems).
I found no flaw in the chain (steps 1-3 of the brief); Theorem R and the variational step check out.

Open questions (explicit):
(Q1) (EF) itself; already its smallest instance is open: under GH, can there be a point x and kappa != 0 with
 int_R e^{J_t(x) - kappa t} dt < inf (a single-orbit order-0 eigen-family)? (Excluded for kappa = 0 by Lemma C and
 for all kappa under (V).)
(Q2) (N2) of §2.
(Q3) Volume case: geometric/Carleman bounds for D_N(phi) on a C^1-dense set (§3), equivalently a quantitative
 replacement for su-accessibility through Pesin-regular points.
(Q4) (V): does GH force a smooth invariant volume? (Under (V) all order-0 parts of the problem disappear, but the
 order-1 core, statement (C) of R4-q10, remains.)

Why (Q1) resists the existing tools (analysis, not a theorem): every distribution built from finitely many orbits
(single-orbit transforms, pairs, Lemma K / Theorem G configurations) has X-image again orbit-supported, so GH can act
on it only through (K0)/(K1), i.e. only at z = 0 (Theorem J); a single orbit with int e^{J_t - kappa t} dt < inf,
kappa != 0, has no two-sided decay at z = 0 unless points forward-asymptotic to it share its backward Jacobian decay,
which needs Pesin structure on its alpha- and omega-limit sets. Any proof of (EF) must therefore produce a
non-orbit-supported distribution (as the Anosov resolvent does) or use GH away from z = 0; I found neither.

Final summary: (EF) and the problem in dimension >= 4 remain OPEN after this attempt; the results above are
sub-class results (order-0 families), one reformulation (§2) and one localisation of the volume-case gap (§3).

=== END OF ANSWER round9_q1 ===

