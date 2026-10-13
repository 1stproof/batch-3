# Answer to round5_q9: Claim (Z0), equivalently (V)

## 0. Plan and status (written first, updated at the end)

Plan:
(a) Prove a new global criterion for (V) that needs no invariant measure. The idea is a one-sided compactness lemma (Lemma H) applied to two natural families of approximate solutions of Xa = -d: the Cesaro-averaged log-Jacobians Jbar_T, and the logs of the two-sided Patterson normalisers R_s.
(b) Use it to reformulate the failure of (V) as divergence of the relative entropy D((g_t)_* nu || nu), and show that this divergence is spatially homogeneous.
(c) Reduce (Z0) to cases, and record the dead ends.

Outcome in brief: (Z0) is NOT settled. New results are proved in Sections 1-4: Lemma H, Theorem K, Theorem R, and the case reduction in Section 4. The exact point where the argument stops is given in Section 5.

## 1. Conventions and two technical lemmas

Conventions are those of the brief. nu is a smooth positive density and nu^ = nu/nu(M). d = div_nu X. J_t(x) = int_0^t d(g_r x) dr, which is smooth in (t,x). The cocycle rule is J_{t+r}(x) = J_r(x) + J_t(g_r x). A distribution u acts by phi -> <u, phi nu>, and <Xu, phi nu> = -<u, (X phi + d phi) nu>. L1 means ker(X on D') = constants.

Change of variables (used throughout): for bounded Borel psi,
 int psi(g_r x) dnu(x) = int psi(y) e^{J_{-r}(y)} dnu(y),
and int e^{J_t} dnu = nu(g_t M) = nu(M).

**Lemma T1 (orbitwise derivative = distributional derivative).** Let a be in L^1(nu), and let w be a bounded Borel function. Suppose there is a g-invariant Borel set Omega of full nu-measure such that, for every x in Omega, t -> a(g_t x) is finite and locally absolutely continuous with derivative w(g_t x) for a.e. t. Then Xa = w in D'.

*Proof.* For x in Omega, a(g_r x) - a(x) = int_0^r w(g_sigma x) dsigma. Multiply by a smooth phi and integrate against nu. By Fubini (w is bounded and (sigma,x) -> w(g_sigma x) is Borel),
 int (a o g_r - a) phi dnu = int_0^r [ int w (phi o g_{-sigma}) e^{J_{-sigma}} dnu ] dsigma.
The bracket is continuous in sigma (dominated convergence), so after dividing by r and letting r -> 0 the right side tends to int w phi dnu. The left side equals int a [ (phi o g_{-r}) e^{J_{-r}} - phi ] dnu. The bracket divided by r converges uniformly to -(X phi + d phi), and a is in L^1. So the left side divided by r tends to -int a (X phi + d phi) dnu = <Xa, phi nu>. ∎

*Chain rule.* Under the hypotheses of T1, a^- = max(-a, 0) satisfies them as well, with w replaced by -1_{a<0} w. Reason: for an absolutely continuous function alpha, alpha^- is absolutely continuous and (alpha^-)' = -1_{alpha<0} alpha' a.e., because alpha' = 0 a.e. on {alpha = 0}. So X(a^-) = -1_{a<0} w in D'.

**Lemma T2 (Cesaro averages of the Koopman flow).** For continuous f put D_T f = (1/T) int_0^T f o g_t dt. Every weak* limit point in L^infinity(nu) = L^1(nu)' of (D_{T_n} f) with T_n -> infinity is an a.e. constant c. The constant is c = lim int D_{T_n} f dnu^.

*Proof.* Let G be such a limit. Then ||(D_T f) o g_r - D_T f||_inf <= 2|r| ||f||_inf / T -> 0. The map h -> h o g_r is weak*-continuous on L^infinity, since it is the adjoint of psi -> (psi o g_{-r}) e^{J_{-r}} on L^1. Hence G o g_r = G a.e. for every r. Therefore int G [ (phi o g_{-r}) e^{J_{-r}} - phi ] dnu = 0. Dividing by r and letting r -> 0 gives -int G (X phi + d phi) dnu = 0, i.e. XG = 0 in D'. By L1, G is constant. ∎

## 2. Lemma H: a one-sided compactness principle

**Lemma H.** Assume GH. Let (a_n) be functions in L^1(nu) satisfying T1 with derivatives w_n. Assume:
 (H1) int a_n^+ dnu <= K for all n;
 (H2) ||w_n||_inf <= K for all n;
 (H3) w_n -> -d + c in D' for some constant c.
Put N_n = int a_n^- dnu. Then:
 (i) if liminf N_n < infinity, then (V) holds;
 (ii) if N_n -> infinity, then (a_n^-/N_n) nu -> nu/nu(M) weak* as measures. That is, int phi a_n^- dnu / N_n -> int phi dnu / nu(M) for every continuous phi.
 (iii) Consequently, if for some nonempty open O we have liminf_n int_O a_n^- dnu < infinity, then (V) holds.

*Proof.* (i) Pass to a subsequence with N_n <= K'. Then ||a_n||_1 <= K + K', so the measures a_n nu have bounded total variation. Extract a further subsequence converging weak* in C(M)' to a signed measure beta, and let b be the distribution <b, phi nu> = beta(phi). Then
 <Xb, phi nu> = -beta(X phi + d phi) = lim -int a_n (X phi + d phi) dnu = lim <X a_n, phi nu> = lim int w_n phi dnu = int (-d + c) phi dnu.
So Xb = -d + c is smooth, and by GH b is smooth. Then L_X(e^b nu) = e^b (Xb + d) nu = c e^b nu. Integrating over M, the left side has integral 0 (the integral of a Lie derivative of a density vanishes), so c = 0 and e^b nu is a smooth positive invariant density. That is (V). (This is (O3).)

(ii) Put u_n = a_n^-/N_n >= 0, so int u_n dnu = 1. By the chain rule and T1, X u_n = -1_{a_n<0} w_n / N_n, which has sup norm at most K/N_n -> 0. Let lambda be any weak* limit point of u_n nu. It is a positive measure with lambda(M) = 1, and
 lambda(X phi + d phi) = lim int u_n (X phi + d phi) dnu = -lim int (X u_n) phi dnu = 0.
By Observation 0 and L1, lambda = nu/nu(M). Every limit point is the same, so the whole sequence converges.

(iii) Pass to a subsequence along which int_O a_n^- dnu stays bounded. If N_n is bounded along a further subsequence, (i) gives (V). Otherwise N_n -> infinity along the subsequence. Take continuous psi with 0 <= psi <= 1, supp psi in O and psi not identically 0. Then int psi u_n dnu <= int_O a_n^- dnu / N_n -> 0. But by (ii) it tends to int psi dnu / nu(M) > 0. Contradiction. ∎

Lemma H is the mechanism of Theorem 1 of [R4-q9], freed from the need for an a priori invariant density. What the earlier proofs needed (log rho in L^1, or rho >= delta on an open set) is replaced by an L^1 bound on the negative part of an approximate solution of Xa = -d.

## 3. Two families, and the resulting criteria for (V)

### 3.1 Family 1: Cesaro-averaged log-Jacobians. Theorem K (relative entropy criterion)

Put Jbar_T = (1/T) int_0^T J_t dt. This is a smooth function. The facts needed are:
- X J_t = d o g_t - d. (Differentiate J_t(g_r x) = J_{t+r}(x) - J_r(x) at r = 0.) Hence X Jbar_T = -d + D_T d, with D_T as in T2, and ||X Jbar_T||_inf <= 2||d||_inf.
- J^+ <= e^J and int e^{J_t} dnu = nu(M). Hence int Jbar_T^+ dnu <= (1/T) int_0^T int J_t^+ dnu dt <= nu(M).
- Relative entropy. (g_t)_* nu has nu-density e^{J_{-t}}, so
 D((g_t)_* nu || nu) = int J_{-t} e^{J_{-t}} dnu = int J_{-t}(g_t x) dnu(x) = -int J_t dnu >= 0.
 In particular -int Jbar_T dnu = (1/T) int_0^T D((g_t)_* nu || nu) dt =: H_T. Also N_T := int Jbar_T^- dnu = H_T + int Jbar_T^+ dnu lies in [H_T, H_T + nu(M)].

**Theorem K (proved; assumes GH).** The following are equivalent:
 (a) (V);
 (b) sup_{t in R} D((g_t)_* nu || nu) < infinity;
 (c) liminf_{T -> infinity} H_T < infinity, i.e. the Cesaro mean of the relative entropy D((g_t)_* nu || nu), t >= 0, does not tend to infinity;
 (d) there are a nonempty open set O and T_n -> infinity with sup_n int_O Jbar_{T_n}^- dnu < infinity.
 A sufficient condition for (d) is sup_n (1/T_n) int_0^{T_n} int_O J_t^- dnu dt < infinity, because x -> x^- is convex.
Moreover, if (V) fails, then H_T -> infinity, and (Jbar_T^- / N_T) nu -> nu/nu(M) as T -> infinity. So the divergence of the relative entropy is spatially homogeneous: on every nonempty open set, Jbar_T -> -infinity in L^1-mean at the same rate as on all of M.

*Proof.*
- (a) => (b): with omega = e^b nu invariant and b smooth, J_t = b - b o g_t, so |J_t| <= 2||b||_inf.
- (b) => (c) and (c) => (d) with O = M: immediate, since N_T <= H_T + nu(M).
- (d) => (a): take the sequence a_n = Jbar_{T_n}, along a subsequence for which D_{T_n} d converges weak* in L^infinity. By T2 the limit is a constant c. Weak* convergence in L^infinity implies convergence in D'. So (H1) to (H3) hold with w_n = -d + D_{T_n} d. Lemma H(iii) gives (V).
- The "moreover" part: if (V) fails, then (c) fails, so H_T -> infinity and N_T -> infinity. Apply Lemma H(ii) along any sequence T_n -> infinity; this needs no convergence of D_T d, since only the sup bound (H2) is used there. ∎

Remarks.
- The same holds with t <= 0, i.e. with D((g_{-t})_* nu || nu). Apply the theorem to -X, which is GH by (O4).
- Theorem K is the "ergodic-average" form of the closed-range question. u_T = -Jbar_T is the Cesaro-regularised candidate solution of Xu = d - c. The theorem says that a one-sided L^1 bound on these candidates, even on a single open set, already forces (V).

### 3.2 Family 2: two-sided Patterson normalisers. Theorem R

For s in (0,1] and x in M put
 R_s(x) = int_R e^{J_t(x) - s|t|} dt in (0, infinity],
 R_s^+(x) = int_0^infinity e^{J_t(x) - st} dt, R_s^-(x) = int_{-infinity}^0 e^{J_t(x) + st} dt.
R_s(x) is exactly the normaliser P(s) of Lemma D at the point x.

Facts:
1. int R_s dnu = int_R e^{-s|t|} nu(M) dt = 2nu(M)/s (Tonelli). So rho_s := s R_s / 2 satisfies int rho_s dnu = nu(M), and R_s < infinity a.e.
2. R_s(g_r x) = e^{-J_r(x)} int_R e^{J_u(x) - s|u - r|} du. Since e^{-s|u-r|} <= e^{s|r|} e^{-s|u|}, the set Omega_s = {R_s < infinity} is invariant. Differentiating in r (dominated convergence on compact r-sets) gives, at y = g_r x,
 d/dr R_s(g_r x) = -d(y) R_s(y) + s (R_s^+(y) - R_s^-(y)).
 So a_s := log rho_s satisfies T1 on Omega_s with
 w_s = -d + s (R_s^+ - R_s^-)/R_s, and |w_s + d| <= s.
3. R_s >= c_0 := int_{-1}^{1} e^{-(||d||_inf + 1)|t|} dt > 0. Hence a_s >= log(s c_0/2), and a_s^+ <= rho_s. So a_s is in L^1 and int a_s^+ dnu <= nu(M).

**Theorem R (proved; assumes GH).** The following are equivalent:
 (a) (V);
 (b) sup_{0<s<=1} int |log(s R_s)| dnu < infinity;
 (c) liminf_{s -> 0} int (log(s R_s))^- dnu < infinity;
 (d) for some nonempty open O, liminf_{s -> 0} int_O (log(s R_s))^- dnu < infinity.
 In particular, (V) holds if there are a nonempty open O, delta > 0 and s_n -> 0 with s_n R_{s_n} >= delta nu-a.e. on O. That is, it suffices that the two-sided Abel density of e^{J_t(x)} be bounded below uniformly for x in some open set.
If (V) fails, then int (log(s R_s))^- dnu -> infinity as s -> 0, but never faster than nu(M) log(1/s) + O(1) (by Fact 3), and (log(sR_s))^- nu / int(...) -> nu/nu(M).

*Proof.* (a) => (b): J_t = b - b o g_t with b bounded gives e^{-2||b||} <= s R_s/2 <= e^{2||b||}. (b) => (c) => (d) is trivial; constants are absorbed, since log(sR_s) = a_s + log 2. (d) => (a): apply Lemma H(iii) to a_n = a_{s_n} with (H1) to (H3) from Facts 2-3 (here w_n -> -d uniformly, c = 0). The last sentence is Lemma H(ii). ∎

Remark. Theorem R needs neither conservativity (N2) nor Hopf's criterion. Using the two-sided weight e^{-s|t|} makes the error term in X log R_s bounded by s, whereas the one-sided resolvent (s - P)^{-1}1 = R_s^+ produces the error 1/R_s^+, whose vanishing needs Hopf's criterion. Note also that R_s^+ is the resolvent of P = X + d applied to 1: (P - s) R_s^+ = -1 along orbits.

## 4. Reductions of (Z0) (proved)

Call z *bad* (for X) if sup_{t>=0} J_t(z) =: B < infinity and (1/T) int_0^T e^{J_t(z)} dt -> 0. (Z0) says that no point is bad for X or for -X.

**Lemma 4.1 (two-sided bounded points).** Let z satisfy sup_{t>=0} J_t(z) <= B, and put L = limsup_{t->infinity} J_t(z).
(i) If L > -infinity, there is y in the omega-limit set of z with J_s(y) <= max(0, B - L) for all s in R.
(ii) If in addition (V) fails and GH holds, then for this y: (1/T) int_0^T e^{J_t(y)} dt -> 0, (1/T) int_{-T}^0 e^{J_t(y)} dt -> 0, int_R e^{J_t(y)} dt = infinity, and s R_s(y) -> 0 as s -> 0.

*Proof.* (i) Choose t_n -> infinity with J_{t_n}(z) -> L and g_{t_n} z -> y. Fix s.
- For s >= 0: J_s(g_{t_n} z) = J_{t_n+s}(z) - J_{t_n}(z) <= sup_{t>=t_n} J_t(z) - J_{t_n}(z) -> L - L = 0.
- For s < 0 and n large (so that t_n + s >= 0): J_s(g_{t_n} z) <= B - J_{t_n}(z) -> B - L.
J_s is continuous in the point, so the bounds pass to y.
(ii) Since (V) fails, Corollary 2 of [R4-q6] applies to y in both time directions, because J is bounded above on each half-orbit. This gives the two Cesaro statements. Lemma C gives the divergence of int_R e^{J_t(y)} dt. For the last claim: an Abel mean is an average of Cesaro means, since s int_0^inf e^{-st} f dt = s^2 int_0^inf e^{-st} F(t) dt with F(t) = int_0^t f. So F(t) = o(t) gives Abel means o(1) on both sides. ∎

So, in Case L > -infinity, (Z0) is equivalent to excluding a point y whose whole orbit has J bounded above while e^J has zero Cesaro density in both time directions.

**Lemma 4.2 (Case L = -infinity contains non-zero Lyapunov sums).** Suppose some ergodic invariant probability mu has mu(d) != 0. Then there is a bad point, for X if mu(d) < 0 and for -X if mu(d) > 0. Hence (Z0) implies:
 (Z0-lin) every invariant probability mu satisfies mu(d) = 0.

*Proof.* If mu(d) < 0, take z mu-generic for Birkhoff's theorem. Then J_t(z)/t -> mu(d) < 0. So J_t(z) is bounded above on t >= 0 and e^{J_t(z)} -> 0 exponentially, which makes z bad for X. If mu(d) > 0, J_{-t}(z)/t -> -mu(d) < 0, so z is bad for -X, since J^{-X}_t = J_{-t}. ∎

(Z0-lin) is necessary for (V) (under (V), (O2) gives unique ergodicity with mu = nu^ and mu(d) = 0). I could not prove (Z0-lin) from GH either. It is the cleanest special case of the open problem. It includes excluding every periodic orbit gamma with int_gamma d != 0, which Observation P of R-b does NOT exclude. Combined with Observation P (the case int_gamma d = 0) and P1 (at a zero p, delta_p is invariant with delta_p(d) = d(p) != 0), (Z0-lin) would give: X has no zeros and no periodic orbits.

**Lemma 4.3 (move (iv) of the brief is a dead end: badness is invariant under time change and change of nu).** Let h > 0 be smooth and Y = hX, with flow g^h_sigma x = g_{tau(sigma,x)} x. Then
 div_nu(hX) = h d + Xh,
 J^Y_sigma(x) = J_{tau}(x) + log h(g_tau x) - log h(x).
Indeed, dsigma = dt/h along the orbit, h d dsigma = d dt, and (Xh) dsigma = d(log h).
Since h is bounded above and below, sigma and tau are comparable, and int_0^S e^{J^Y} dsigma is comparable to int_0^{tau(S)} e^{J} dt. So z is bad for Y iff it is bad for X. Changing nu to e^a nu changes d to d + Xa, and hence J_t(x) to J_t(x) + a(g_t x) - a(x). That is a bounded change, so badness is unchanged as well. Hence time changes and changes of density cannot by themselves remove a bad point; any use of (iv) has to involve GH more substantially. ∎

**Lemma 4.4 (partial progress on (Z0-lin): no hyperbolic sinks or sources; proved).** Assume GH and dim M = n >= 2. Then X has no hyperbolic attracting zero and no hyperbolic attracting periodic orbit, i.e. none whose nontrivial Floquet multipliers all have modulus < 1. Applying this to -X (GH by (O4)), there are no hyperbolic repelling zeros or periodic orbits either.

*Proof.* Let K be such a zero or orbit. In each case we build a bounded function u that is not a.e. equal to a continuous function but has Xu smooth.

*Step 1: a section.*
- Zero p with DX(p) = A, all eigenvalues with negative real part. By the Lyapunov equation there is a positive definite Q with QA + A^T Q < 0. The function q(x) = <Q(x-p), x-p>, in a chart, decreases strictly along the flow on a small punctured ball. So every orbit in the punctured ball D = {q <= r} \ {p} crosses the sphere S = {q = r} exactly once and then converges to p. Put Sigma = S.
- Attracting periodic orbit gamma. Take a small transverse disc Sigma_0 at a point of gamma, with Poincare map f, f(0) = 0, and spectral radius of Df(0) less than 1. In an adapted norm, f maps a small closed ball D_0 into its interior and f^k(D_0) shrinks to 0. Put Sigma = A_0 := D_0 \ int f(D_0), a compact annulus. Every point of D_0 \ {0} lies in f^k(A_0) for some k >= 0.

*Step 2: an invariant function.* Choose a smooth psi on Sigma, not identically 0, with compact support in the interior of Sigma (interior of A_0 in the periodic case; for the sphere, any non-constant psi will do). Let W be the union of all orbits meeting D (zero case) or D_0 \ {0} (periodic case). W is open and invariant and does not contain K. Define psihat on W by psihat(g_t x) = psi(x) for x in Sigma, extended in the periodic case by f-invariance: psi(f^{-k} y) for y in f^k(A_0).
- psihat is well defined. In the zero case each orbit in W crosses S once. In the periodic case an orbit near gamma meets Sigma_0 near 0 only along an f-orbit, and psi vanishes near the two boundary spheres of A_0, so the pieces f^k(A_0) glue smoothly.
- psihat is smooth on W, by flow boxes.
- psihat is invariant under the flow.
- In every neighbourhood of K, psihat takes the value 0 and also values near max |psi| != 0, each on sets of positive measure.

*Step 3: the function u.* Let chi be smooth, with chi = 1 near K and supp chi contained in a small neighbourhood U of K with U \ K contained in W. Put u = chi psihat on U \ K and u = 0 elsewhere.
- u is bounded.
- u is orbitwise Lipschitz on the invariant full-measure set M \ K, with orbit derivative psihat X chi. This function is smooth on M: it vanishes near K and outside U, and on W it is a product of smooth functions.
- By Lemma T1, Xu = psihat X chi in D', which is a smooth function.
- u is not a.e. equal to a continuous function near K, by the last property in Step 2.
This contradicts GH. ∎

Remark. Hence the non-zero-Lyapunov-sum invariant measures that (Z0-lin) must exclude are all of saddle type, or non-atomic and not supported on periodic orbits. I could not handle saddles. The construction above needs a nonconstant invariant function on a full punctured neighbourhood. For a saddle the orbits leave every neighbourhood, so the support of X chi meets the local stable and unstable manifolds, where psihat is singular.

## 5. Where the argument stops; dead ends

1. **The gap between pointwise and open-set information.** (Z0) is a statement about ONE half-orbit. Theorems K and R reduce (V) to a statement about a nonempty OPEN set: a uniform lower bound for log(sR_s), or for Jbar_T, in L^1(O). At a single point the relevant quantity, s R_s(x), is lower semicontinuous in x for each fixed s, but with no uniformity as s -> 0. So the bad point of (Z0) cannot be thickened. Conversely, Theorem K says that if (V) fails then Jbar_T -> -infinity on average on every open set, homogeneously. This is consistent with bad points existing densely, and gives no contradiction by itself.

2. **Soft compactness cannot see the remaining case (heuristic, not proved).** Every argument so far uses GH only through L1 (ker X on D' = constants) and the closed-graph estimate of Lemma 2. Lemma H shows how far L1 alone goes: it turns one-sided L^1 bounds into (V). In the failure scenario the picture given by Theorem K is: the relative entropy D((g_t)_* nu || nu) diverges and (g_t)_* nu becomes singular in a spatially homogeneous way. This is exactly what happens for a C^infinity transitive Anosov flow that does not preserve volume ((g_t)_* nu -> SRB measure). Whether L1 holds for such flows I could not decide. If it does, then L1-based arguments (Lemma C, Lemma D, Proposition 1, Theorems 1, 3, K, R, Lemma H) can never prove (Z0). A proof would then have to use GH in its stronger form X(D') ∩ C^infinity = X(C^infinity). For Anosov flows this form fails, through distributional solutions u = -int_0^infinity f o g_t dt built by mixing; L1 might not fail.

3. **Two-sided (signed) compactness is insufficient; the one-sided bound (H1) is essential.** For a Diophantine linear flow on T^n (which is GH), u_k = e^{2 pi i k.x} with |k.alpha| -> 0 are L^1-normalised, mean zero, and have ||X u_k||_inf -> 0. So "normalised near-kernel elements" exist under GH, and only positivity, as in Lemma H(ii), produces the contradiction.

4. **The dual estimate (O1) applied to the resolvent family.** P rho_s = s(rho_s - 1) for the one-sided rho_s = s R_s^+. (O1) gives rho_s nu = I_s + S_s with I_s an invariant distribution density and ||S_s||_{(C^m)'} = O(s). This only re-proves that the limits of rho_s nu are invariant; it gives no lower bound on the a.c. part.

5. **Move (iv) (time changes).** This is dead by Lemma 4.3.

6. **Weights e^{lambda J}, 0 < lambda < 1.** These give lambda-conformal limits, i.e. distributions in ker(X + (1-lambda)d). GH says nothing about these operators, and they converge to nu^ only qualitatively as lambda -> 1.

7. **Smearing the one-sided measure at a forward-integrable bad point** (Case II with int_0^infinity e^{J_t(z)} dt < infinity, which gives X(A_z/nu) = delta_z/nu). Smearing over a transversal family produces u = int_0^infinity b o g_{-t} dt, which needs int b R_0^+ dnu < infinity. This fails ν-a.e. by conservativity, so the right-hand side cannot be made smooth.

## 6. Final summary: proved / open

Proved here (all assuming GH, dim M >= 2 where needed):
- Lemma T1, Lemma T2 (technical).
- **Lemma H**: approximate solutions a_n of Xa = -d + c with bounded positive parts either force (V), or have negative parts that equidistribute to nu^. A bound on the negative parts on any nonempty open set forces (V).
- **Theorem K**: (V) holds iff sup_t D((g_t)_* nu || nu) < infinity, iff the Cesaro means of this relative entropy do not tend to infinity, iff the Cesaro-averaged log-Jacobians are L^1-bounded below on some nonempty open set. If (V) fails, the divergence is spatially homogeneous.
- **Theorem R**: (V) holds iff liminf_{s->0} int_O (log s R_s)^- dnu < infinity for some nonempty open O, where R_s(x) = int_R e^{J_t(x) - s|t|} dt is the Patterson normaliser of Lemma D. In particular a uniform positive lower bound for the two-sided Abel density of e^{J} on an open set gives (V).
- **Lemma 4.1**: when limsup J_t(z) > -infinity, a bad point yields a point y whose whole orbit has J bounded above, with null Cesaro and Abel densities in both directions.
- **Lemma 4.2**: (Z0) implies (Z0-lin), i.e. mu(d) = 0 for every invariant mu.
- **Lemma 4.4**: no hyperbolic attracting or repelling zeros or periodic orbits.
- **Lemma 4.3**: badness is invariant under time change and change of nu.

Not proved: (Z0) itself, hence not (V) along this line.

Open questions (precise):
- (Q1) (Z0): exclude, under GH, a point z with sup_{t>=0} J_t(z) < infinity and (1/T) int_0^T e^{J_t(z)} dt -> 0.
- (Q2) (Z0-lin), a necessary special case: under GH, mu(d) = 0 for every ergodic invariant mu. Even the case of a hyperbolic saddle periodic orbit with int_gamma d != 0 is open here.
- (Q3) Open-set form, equivalent to (V) by Theorems K and R: under GH, find a nonempty open O with liminf_T int_O Jbar_T^- dnu < infinity, or one with liminf_s int_O (log sR_s)^- dnu < infinity.
- (Q4) Meta-question deciding whether L1-based ("soft") methods can suffice: does L1 (ker X on D' = constants) hold for C^infinity transitive Anosov flows that do not preserve volume?

=== END OF ANSWER round5_q9 ===

