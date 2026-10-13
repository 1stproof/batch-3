# round12_q6: answer (in progress)

## Plan / statement attempted
Target: (PE0), via the spectral approach of the brief: flatness at frequency 0 (from GH) played against
the Lebesgue-spectrum / Hardy-filtration structure of the non-Pinsker part (from positive entropy).
Order of work:
 S1. Volume case, step (1): flatness lemma (statement + proof), and the general-case analogue on L^2(mu).
 S2. Step (2): translation (Lax-Phillips/Sinai) representation of H_L, and what smoothness of an observable
     gives there (one-sided decay; strip analyticity of its Fourier transform).
 S3. Step (3): a conditional "Szego" theorem: one-sided exponential decay + super-flatness exp(-c/eps) forces
     P_L f = 0. Proved.
 S4. Obstructions: (a) infinite-order flatness (any rate weaker than exp(-c/eps)) is consistent with the whole
     linear structure; (b) GH does NOT give exp(-c/eps)-flatness even for analytic f on GH flows
     (Diophantine linear flows on T^n, n >= 3) — so the Szego route as planned is dead; (c) the one-sided decay
     rate available from Pesin theory is non-uniform; (d) the general (no volume) case: richness of R_inf.
 S5. Summary: proved / conditional / open.

Outcome in one line: (PE0) is NOT proved. The spectral route is reduced to one quantitative statement (Q)
(super-flatness exp(-c/eps) for a single non-Pinsker smooth observable); the reduction is a proved theorem
(Theorem 3.1), and (Q) is shown NOT to follow from GH-type flatness (Proposition 4.2, Diophantine flows on T^n).
The linear spectral data with only infinite-order flatness is shown to be consistent (Proposition 4.1).

---------------------------------------------------------------------------------------------------------

## S1. Flatness at frequency 0

Conventions. For a Borel probability m on M invariant under the flow, U_t phi = phi o g_t is a strongly continuous
unitary group on L^2(m) (strong continuity: continuous functions are dense and t -> phi o g_t is uniformly continuous
for continuous phi). Write U_t = e^{itA} (Stone), and sigma_phi for the spectral measure:
<U_t phi, phi> = int e^{it xi} d sigma_phi(xi).

**Lemma 1.1 (proved).** Let m be flow-invariant. If u is C^1, then u is in D(A) and iAu = Xu. Consequently, if
f = X^j u_j with u_j in C^inf, then d sigma_f = xi^{2j} d sigma_{u_j} and, for every eps > 0,
  sigma_f([-eps, eps]) <= eps^{2j} ||u_j||_{L^2(m)}^2 <= eps^{2j} ||u_j||_{C^0}^2.
*Proof.* (u o g_t - u)/t -> Xu uniformly on M as t -> 0 (mean value theorem along orbits, Xu uniformly continuous),
hence in L^2(m); so u is in D(A) with iAu = Xu. Since X maps C^inf to C^inf, iterating gives u_j in D(A^j) with
(iA)^j u_j = f. By the spectral theorem, d sigma_{(iA)^j v} = xi^{2j} d sigma_v. The bound follows from
int_{[-eps,eps]} xi^{2j} d sigma_{u_j} <= eps^{2j} sigma_{u_j}(R) = eps^{2j} ||u_j||^2. QED

**Corollary 1.2 (volume case, proved).** Assume GH and a smooth invariant probability density omega. For every j there are m_j and C_j such that every smooth f with omega(f) = 0
satisfies sigma_f([-eps, eps]) <= C_j eps^{2j} ||f||_{C^{m_j}}^2 (spectral measure in L^2(omega)).
*Proof.* By (O2) and the duality consequence of Text A, the omega-mean-zero smooth functions are exactly X(C^inf),
and by Text B Lemma 2 (with nu = omega) the omega-mean-zero solution u = X^{-1} f satisfies ||u||_{C^k} <= C||f||_{C^m}.
Iterating j times (each u_i is again omega-mean-zero) gives u_j with X^j u_j = f and ||u_j||_{C^0} <= C_j' ||f||_{C^{m_j}}.
Apply Lemma 1.1. QED

**General case (what survives without a volume).** For PE0's measure mu (g_1-invariant, g_1-ergodic), put
mu-bar = int_0^1 (g_s)_* mu ds. It is flow-invariant and flow-ergodic (a flow-invariant set A has
(g_s)_*mu(A) = mu(A) in {0,1}), and h_{mu-bar}(g_1) = h_mu(g_1) > 0 (each (g_s)_*mu is g_1-invariant with the same
entropy, g_s conjugating; entropy is affine and Jacobs' formula applies to the integral). Lemma 1.1 applies in
L^2(mu-bar) to every f in X^j(C^inf). Without a volume, X(C^inf) is the annihilator of the space I of invariant
distribution densities (Text A), which may be infinite-dimensional; each X^j(C^inf) is closed (X is a topological
isomorphism C^inf/R -> X(C^inf) by Text B Cor. 3, and X^{j+1}(C^inf) = X(X^j(C^inf) + R), the image of a closed
subspace), so R_inf = cap_j X^j(C^inf) is a closed subspace of C^inf. Whether R_inf is dense in L^2_0(mu-bar) is OPEN
(it is equivalent to: no nonconstant v in L^2(mu-bar) such that v mu-bar lies in the weak*-closed span of the
generalized invariant distributions cup_j ker (L_X)^j). Note that for fixed j, X^j(C^inf) IS dense in L^2_0(mu-bar):
it contains X^j phi for all smooth phi; C^inf is a U_t-invariant dense subspace of D(A^infinity), hence a core for A^j,
so the closure of {A^j phi} is the closure of ran A^j = (ker A^j)^perp = (ker A)^perp = L^2_0 (ergodicity). But this
gives flatness of a fixed finite order 2j only, which is useless for S3. Everything below is therefore written for
a single vector satisfying flatness hypotheses, and applies verbatim to the volume case.

## S2. The non-Pinsker part: filtration and translation representation (cited structure)

Let m be a flow-invariant ergodic probability with h_m(g_1) > 0 (m = omega in the volume case, m = mu-bar in general),
Pi its Pinsker sigma-algebra, H_L = L^2(m) minus L^2(Pi) (orthogonal complement). Spectral measures add over the
orthogonal U-invariant decomposition L^2 = L^2(Pi) + H_L, so sigma_{P_L f} <= sigma_f: **flatness passes to P_L f.**

(F) [cited from memory; Gurevich / Sinai theory of K-flows, relative to the Pinsker algebra; geometric realisation by
Ledrappier–Young-type partitions subordinate to unstable manifolds] There is an increasing family of sigma-algebras
F_s (s in R) with g_t^{-1} F_s = F_{s+t} (so U_t L^2(F_s) = L^2(F_{s+t})), cap_s F_s = Pi, vee_s F_s = Borel (mod m).
Caveat: Ledrappier–Young construct the partition for the time-one map; turning it into a flow-filtration with
cap = Pi is the flow version of the theory and I state it as cited, not proved.

(LP) [Lax–Phillips translation representation, cited from memory] Put H_s = L^2(F_s) minus L^2(Pi). Then
U_t H_s = H_{s+t}, H_s increasing, cap H_s = 0, union dense in H_L. Hence there are a separable Hilbert space N and a
unitary W: H_L -> L^2(R; N) with W U_t W^{-1} = tau_t, (tau_t G)(s) = G(s - t), and W H_0 = L^2((-inf, 0]; N).
(dim N = infinity: countable Lebesgue spectrum.) Then W H_T = L^2((-inf, T]; N).

(Dec) For a Lipschitz f put psi_f(T) = ||f - E[f | F_T]||_{L^2(m)}. Since Pi is contained in F_T, E[.|F_T] commutes with
E[.|Pi], and f - E[f|F_T] lies in H_L; hence, with G = W P_L f,
   int_T^inf ||G(s)||^2 ds = psi_f(T)^2.
If F_T is generated by unstable plaques g_{-T}(eta(x)) (eta subordinate to W^u), then
psi_f(T) <= Lip(f) (int diam(g_{-T} eta(x))^2 dm)^{1/2}. The diameters shrink like C(x) e^{-lambda T} with a measurable
(Pesin) C(x), so psi_f(T) -> 0, but an EXPONENTIAL rate psi_f(T) <= C e^{-aT} holds only under integrability of the
Pesin constants (e.g. uniformly hyperbolic case). This is gap (c) below.

Fourier convention: G^(xi) = int G(s) e^{-is xi} ds; then sigma_G(d xi) = (2 pi)^{-1} ||G^(-xi)||^2 d xi, and all our
conditions are symmetric in xi, so we write sigma_G([-eps,eps]) ~ int_{-eps}^{eps} ||G^||^2.
Paley–Wiener: G supported in (-inf, 0] iff G^ is the boundary function of an N-valued H^2 function of the UPPER
half-plane {Im z > 0} (|e^{-isz}| = e^{s Im z} decays for s < 0).

## S3. A conditional Szego-type theorem (proved)

**Theorem 3.1.** Let G in L^2(R; N). Assume
 (i) (one-sided exponential decay) int_T^inf ||G(s)||^2 ds <= C e^{-2aT} for all T >= 0, some a > 0;
 (ii) (super-flatness) int_{-eps}^{eps} ||G^(xi)||^2 d xi <= exp(-h(1/eps)) for 0 < eps < eps_0, where h is
      nondecreasing and int^inf h(t) dt / t^2 = infinity (e.g. h(t) = c t, i.e. exp(-c/eps)).
Then G = 0.
Consequently (volume or general case): if some f with P_L f != 0 has psi_f(T) <= C e^{-aT} and
sigma_f([-eps,eps]) <= exp(-h(1/eps)), we get a contradiction; so under (F),(LP), a positive-entropy m forces every
such f to be Pinsker-measurable.

*Proof.* Step 1 (strip analyticity). Fix 0 < b < a. For Im z = y < a define Phi_+(z) = int_0^inf G(s) e^{-isz} ds;
it converges absolutely: int_k^{k+1} ||G|| e^{sy} ds <= (C e^{-2ak})^{1/2} e^{(k+1)|y|}... more precisely
<= C^{1/2} e^{-ak} e^{(k+1) max(y,0)}, summable in k when y < a. So Phi_+ is analytic (N-valued) on {Im z < a}.
For Im z > 0, Phi_-(z) = int_{-inf}^0 G(s) e^{-isz} ds converges absolutely (Cauchy–Schwarz with e^{sy} in L^2(-inf,0))
and is analytic. Phi = Phi_+ + Phi_- is analytic on the strip S = {0 < Im z < b}. By Plancherel, for 0 < y < b,
 int ||Phi(x+iy)||^2 dx <= 4 pi ( int_0^inf ||G||^2 e^{2sy} ds + int_{-inf}^0 ||G||^2 e^{2sy} ds ) <= K,
with K independent of y (the first integral is bounded by sum_k C e^{-2ak} e^{2(k+1)b} < inf). By dominated
convergence on the s-side, Phi(. + iy) -> G^ in L^2(R; N) as y -> 0+.

Step 2 (scalar functions, pointwise bound). For a unit vector e in N let phi(z) = <Phi(z), e>. Then phi is analytic
on S, sup_{0<y<b} int |phi(x+iy)|^2 dx <= K, phi(. + iy) -> <G^, e> =: phi_0 in L^2(R) as y -> 0+. Sub-mean-value on
the disc B(z, r), r = dist(z, boundary of S): |phi(z)|^2 <= (pi r^2)^{-1} int_{B(z,r)} |phi|^2 <= 2K/(pi r).

Step 3 (local log-integrability). Suppose phi is not identically 0. Zeros are isolated, so pick t in (0, b/4) with
phi(it) != 0, and r in (2t, b/4). Let D = {|z| < r, Im z > 0} (half-disc), z_0 = it, and omega_{z_0} the harmonic
measure of D at z_0; on the diameter [-r, r] it has a continuous density which is >= c_0 > 0 on [-r/2, r/2], and the
density is bounded on [-r, r] and on the arc. For small delta > 0 the closure of D + i delta lies in S, and log|phi| is
subharmonic, so
 log|phi(z_0 + i delta)| <= int_{[-r,r]} log|phi(x + i delta)| d omega(x) + int_{arc} log|phi(w + i delta)| d omega(w).
Arc term: by Step 2, log|phi(w + i delta)| <= (1/2) log^+ (2K/(pi Im w)) + const, which is omega-integrable on the arc
(the density is bounded and log(1/Im w) is integrable near the endpoints of the arc); so the arc term is <= A
uniformly in delta. Diameter term: write log = log^+ - log^-. Since log^+ is 1-Lipschitz and dominated by |.|, and
phi(. + i delta) -> phi_0 in L^2([-r,r]) hence in L^1(omega), int log^+|phi(. + i delta)| d omega -> int log^+|phi_0| d omega.
Along a subsequence phi(. + i delta) -> phi_0 a.e., so by Fatou int log^-|phi_0| d omega <= liminf int log^-|phi(.+i delta)| d omega.
Letting delta -> 0 (phi continuous at z_0):
 int_{[-r,r]} log^-|phi_0| d omega <= int log^+|phi_0| d omega + A - log|phi(z_0)| < infinity,
hence int_{-r/2}^{r/2} log^-|phi_0(x)| dx < infinity.

Step 4 (super-flatness contradicts Step 3). Let g = ||G^||^2 and I_k = {2^{-k-1} <= |xi| < 2^{-k}}, of length
l_k = 2^{-k}. By Jensen (concavity of log),
 int_{I_k} log g <= l_k log( l_k^{-1} int_{I_k} g ) <= 2^{-k} ( k log 2 - h(2^k) ).
Since h is nondecreasing, int_{2^k}^{2^{k+1}} h(t)/t^2 dt <= h(2^{k+1}) 2^{-k} = 2 * 2^{-(k+1)} h(2^{k+1}), so
int^inf h/t^2 = inf gives sum_k 2^{-k} h(2^k) = infinity. Hence
int_{|xi| < eps} log g = -infinity for every eps > 0, while int log^+ g <= int g < inf; so int_{|xi|<eps} log^- g = inf.
Since |phi_0| <= ||G^|| = g^{1/2}, log^-|phi_0| >= (1/2) log^- g, so int_{-r/2}^{r/2} log^-|phi_0| = infinity,
contradicting Step 3. Therefore phi = 0 on S, so <G^, e> = phi_0 = 0 a.e. for every unit e; taking e in a countable
dense set, G^ = 0 a.e., so G = 0. QED

**Remark 3.2 (the threshold, in terms of the tame constants).** If f = X^j u_j with ||u_j||_{L^2} <= B A^j j! for all j,
then sigma_f([-eps,eps]) <= inf_j eps^{2j} B^2 A^{2j} (j!)^2 <= B'' eps^{-1} exp(-2/(A eps)) (take j = floor(1/(A eps))
and Stirling, j! (A eps)^j <= C sqrt(j) e^{-j}), i.e. (ii) holds with h(t) = c t for any c < 2/A and small eps. So the conditional theorem needs a non-Pinsker smooth f whose iterated X-primitives have FACTORIAL
(Gevrey-1) growth. Gevrey-s growth (j!)^s with s > 1 gives only h(t) = c t^{1/s}, for which int h/t^2 < inf, and
Proposition 4.1 shows this is genuinely insufficient.

## S4. Obstructions

**Proposition 4.1 (proved: infinite-order flatness is consistent with the whole linear structure).**
In L^2(R; N) with the translation group tau_t, let D be the generator (D <-> multiplication by -i xi on Fourier side)
and let m(z) = exp(-(-iz)^{-1/2}) (principal branch) for Im z >= 0, z != 0. Then:
 (a) m is analytic on {Im z > 0}, |m| <= 1 there, and |m(x)| = exp(-1/sqrt(2|x|)) for real x != 0.
 (b) Multiplication by m (on the Fourier side) is a bounded operator Mm commuting with tau_t, with dense range, and
     mapping W H_T = L^2((-inf, T]; N) into itself for every T.
 (c) Every G = Mm F in the range satisfies int_{-eps}^{eps} ||G^||^2 <= exp(-sqrt(2/eps)) ||F^||^2; so G is flat to every order at 0 (but only with h(t) = sqrt(2t),
     int h/t^2 < inf: Theorem 3.1 does not apply, as it must not).
 (d) If G^ = m F^ with F in L^2((-inf, T]; N), then for every j, G = D^j G_j with G_j in L^2((-inf, T]; N) and
     ||G_j|| <= M_j ||F||, M_j = sup_{w>0} w^{-j} exp(-w^{-1/2}/sqrt 2) = (2 sqrt2 j / e)^{2j} (Gevrey-2 growth in j).
Hence: a dense, U-invariant subspace of H_L, compatible with the filtration, consists of vectors that are flat at
frequency 0 to infinite order, lie in the range of every power of the generator with preimages in the same H_T, and
(taking F supported in (-inf, 0]) satisfy the one-sided decay (i) of Theorem 3.1 trivially (G vanishes on (0, inf)).
So steps (1)+(2) of the planned approach, without quantitative constants at the exp(-c/eps) level and without
non-linear (multiplicative) or geometric input, cannot produce a contradiction.
*Proof.* (a) For Im z > 0, Re(-iz) = Im z > 0, so arg(-iz) in (-pi/2, pi/2), arg((-iz)^{-1/2}) in (-pi/4, pi/4) and
Re (-iz)^{-1/2} >= |z|^{-1/2} cos(pi/4) > 0; this also holds on the real axis minus 0 with arg(-ix) = -+pi/2, giving
|m(x)| = exp(-|x|^{-1/2}/sqrt 2). Analyticity is clear (principal branch on the right half-plane).
(b) |m| <= 1 gives boundedness; commuting with tau_t (multiplication by e^{-it xi}) is clear; m != 0 a.e., so the
adjoint (multiplication by conj m) is injective and the range is dense. If F is supported in (-inf, T], then
e^{iT xi} F^ is in H^2(upper) (Paley–Wiener, S2), and m e^{iT xi} F^ is in H^2(upper) since m is bounded analytic
there; so G = Mm F is supported in (-inf, T]. (c) is immediate from (a). (d) G_j^ = G^/(-i xi)^j = (m(xi)/(-i xi)^j) F^;
the function m(z)/(-iz)^j is analytic on Im z > 0 and bounded by M_j there (by (a), |m(z)| <= exp(-|z|^{-1/2}/sqrt 2)),
so G_j is again in the range of a bounded H^infinity multiplier applied to F and is supported in (-inf, T].
The value of M_j: with s = w^{-1/2}, maximise s^{2j} e^{-s/sqrt2}: s = 2 sqrt2 j. QED

**Proposition 4.2 (proved: GH does not yield super-flatness, even for analytic observables).** Let n >= 3 and let
alpha in R^n be Diophantine (|k . alpha| >= c |k|^{-tau} for k in Z^n \ 0); the linear flow x -> x + t alpha on T^n is
GH (classical, Greenfield–Wallach; by Fourier series: Xu = f gives u_k = f_k / (2 pi i k.alpha), which decays rapidly
when f_k does, and the distributional case is identical). Let f(x) = sum_{k != 0} e^{-|k|_1} e^{2 pi i k.x} (real
analytic). Then there are C', eps_1 > 0 with
   sigma_f([-eps, eps]) >= exp(-C' eps^{-1/(n-1)})  for all 0 < eps < eps_1.
So (ii) of Theorem 3.1 fails for f (h(t) <= C' t^{1/(n-1)}, int h/t^2 < inf), although f is analytic and the flow
is GH; more generally no hypothesis of the type "GH + smoothness (even analyticity) of f" implies (ii).
*Proof.* The spectral measure in L^2(Leb) is sigma_f = sum_k |f_k|^2 delta_{2 pi k.alpha}. WLOG alpha_n != 0; put
theta_i = alpha_i/alpha_n (i < n). Dirichlet's theorem for one linear form in n-1 variables (pigeonhole): for every
N >= 1 there are q in Z^{n-1} \ 0 with max|q_i| <= N and p in Z with |q.theta - p| <= N^{-(n-1)}. Put
k = (q, -p) != 0; then |k.alpha| = |alpha_n| |q.theta - p| <= |alpha_n| N^{-(n-1)} and |k|_1 <= B N with B depending
only on alpha. With eps_N = 2 pi |alpha_n| N^{-(n-1)}: sigma_f([-eps_N, eps_N]) >= e^{-2|k|_1} >= e^{-2BN}
= exp(-C eps_N^{-1/(n-1)}). Since eps_{N+1} >= 2^{-(n-1)} eps_N, for eps in [eps_{N+1}, eps_N] monotonicity gives
sigma_f([-eps,eps]) >= exp(-C eps_{N+1}^{-1/(n-1)}) >= exp(-C' eps^{-1/(n-1)}). QED
Consequence for the plan: in step (3) the GH side can only supply flatness of the type exp(-c eps^{-1/tau'}) with
tau' > 1 in general (this is what actual GH flows exhibit, and these are the only GH flows known); Theorem 3.1 needs
tau' <= 1. A proof of (PE0) along this route would have to show that positive entropy IMPROVES the arithmetic at
frequency 0 beyond what Diophantine flows exhibit — there is no mechanism for this in sight. I regard the
quantitative Szego route of the brief as dead.
(Note: in the relevant dimensions dim M >= 4 (entry 61), the example with n = 4 gives exp(-C eps^{-1/3}).)

**4.3 Gap (c): the decay rate along the filtration (not resolved).** Even granting (ii), Theorem 3.1 needs
psi_f(T) <= C e^{-aT}. Pesin theory gives diam(g_{-T} eta(x)) <= C(x) e^{-lambda T} with only measurable C(x), hence
psi_f(T) -> 0 with a rate governed by the tails of C. With a slower rate e^{-w(T)} the function Phi_+ is no longer
analytic across the real axis; it lies in a Carleman class, and one expects (NOT proved here) a version of Theorem 3.1
when int^inf w(T) dT/T^2 = inf (Denjoy–Carleman/Beurling–Levinson type quasi-analyticity), but no such bound on w
is available from Pesin theory for a non-uniformly hyperbolic measure, and the hypothetical mu of (PE0) is
non-hyperbolic (zero centre exponent), which makes uniform control even less plausible.

**4.4 The multiplicative structure (remark with proof; it shows what kind of input could work).** In a Gaussian
flow with even spectral density p (a K-flow when p is a.c. and non-trivial), for a real first-chaos variable
Y = int phi dW with rho = |phi|^2 p, the Wick square Z = Y^2 - E Y^2 has
Cov(Z, U_t Z) = 2 Cov(Y, U_t Y)^2 (Isserlis' formula), so sigma_Z has density 2 (rho * rho)(xi) (up to the 2 pi
normalisation), whose value at 0 is 2 int rho(xi)^2 d xi > 0 when phi != 0. So in Gaussian K-flows the algebra
generated by any non-zero first-chaos vector contains vectors that are NOT flat at 0 (positive asymptotic variance),
whereas under GH (volume case) every mean-zero element of the algebra C^inf is flat. This is the only mechanism I
found that defeats the consistency of Proposition 4.1 (which is a linear statement). For a smooth flow with
positive entropy there is no chaos decomposition, and the analogous statement — some smooth f with P_L f != 0 such
that f^2 (or some polynomial in f and its translates) has positive asymptotic variance, i.e. a CLT-type
non-degeneracy — does not follow from positive entropy in general (abstract K-systems admit bounded functions
f = v o g_1 - v with |f| = 1, so f^2 is constant). I could not find a geometric (unstable-leaf) substitute.

**4.5 General case (no volume).** As noted in S1, for fixed j, X^j(C^inf) is dense in L^2_0(mu-bar), but
infinite-order flatness requires f in R_inf = cap_j X^j(C^inf), and density of R_inf in L^2_0(mu-bar) (or merely
R_inf not contained in L^2(Pi)) is OPEN; it is governed by the generalized invariant distributions
cup_j ker(L_X)^j (which contain, e.g., solutions S of L_X S = mu_1 - mu_2 for invariant probabilities mu_1, mu_2,
which exist by (O1)). Since the volume-case route already fails (4.2), I did not pursue this further.

## S5. Summary

PROVED here:
 - Lemma 1.1 / Cor. 1.2: flatness of spectral measures at 0 (orders 2j, with closed-graph constants), volume case and
   for f in X^j(C^inf) on L^2(mu-bar) in general; density of X^j(C^inf) in L^2_0(mu-bar) for each fixed j.
 - Theorem 3.1 (conditional Szego theorem): one-sided exponential decay along the K-filtration + super-flatness
   exp(-h(1/eps)) with int h/t^2 = inf forces the non-Pinsker component to vanish. Remark 3.2: this corresponds to
   Gevrey-1 (factorial) growth of the iterated primitives.
 - Proposition 4.1: the linear spectral structure (Lebesgue spectrum, Hardy filtration, infinite-order flatness,
   preimages under all powers of the generator in the past, one-sided decay) is consistent; a dense invariant
   subspace of H_L has all these properties. So the approach cannot succeed without quantitative or non-linear input.
 - Proposition 4.2: for Diophantine linear flows on T^n (n >= 3; GH), analytic observables are not super-flat
   (sigma_f([-eps,eps]) >= exp(-C eps^{-1/(n-1)})). So GH + smoothness/analyticity does not supply hypothesis (ii);
   the quantitative route of the brief is dead.
 - Remark 4.4 (Gaussian flows): multiplicative structure can force non-flatness in K-flows.
CITED (from memory, not proved): the flow K-filtration relative to Pinsker (F), Lax–Phillips translation
representation (LP), Paley–Wiener, Dirichlet's theorem, Greenfield–Wallach for Diophantine flows, Isserlis' formula.
OPEN:
 - (PE0) itself; in particular its volume case (a cohomology-free = GH volume-preserving flow has zero entropy).
 - (Q) Existence, under GH with a positive-entropy m, of a smooth f with P_L f != 0 and sigma_f([-eps,eps]) <=
   exp(-c/eps) (or any h with int h/t^2 = inf); by Prop. 4.2 this cannot come from GH alone.
 - Exponential (or quasi-analytic-rate) one-sided decay psi_f(T) for non-uniformly hyperbolic / non-hyperbolic m.
 - A non-linear (CLT-type) non-degeneracy for some polynomial in smooth observables of a positive-entropy smooth
   flow, which would contradict flatness of all mean-zero elements of the algebra C^inf.
 - General case: whether R_inf = cap_j X^j(C^inf) is dense in L^2_0(mu-bar) / not Pinsker-measurable.

=== END OF ANSWER round12_q6 ===
