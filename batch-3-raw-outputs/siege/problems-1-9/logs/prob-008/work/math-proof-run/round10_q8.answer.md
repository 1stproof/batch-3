# round10_q8 — answer (microlocal / semiclassical attack on (JC))

## Plan (written first)
Target: (JC), or the stronger (NJ), by the microlocal approach (1)-(3) of the brief.
Steps: (a) work out exactly what the free choice of c (in particular |Im c| -> infinity) and the wavefront /
defect-measure calculus can see, by testing them on the model chains that exist for non-GH flows;
(b) record every GH-dependent statement I can actually prove about chains at Re c != 0;
(c) state precisely where the approach stops.

Outcome in one line: no proof of (JC) or (NJ) and no counterexample. I prove (Section 1) that approaches (1) and (2)
cannot work as posed: the information they extract at large |Im c| is the same for GH and non-GH flows, and it is
the same at every point of the strip. I also prove (Section 2) that orbit-supported chains are excluded under GH
whenever the orbit is asymptotic to hyperbolic periodic orbits or zeros, or whenever its strip contains 0.
I also prove a microlocal multiplier criterion (Section 3, which is the brief's idea (3)). If the wavefront set of
an eigen-distribution at c admits a symbol that grows at the rate e^{ct} along the lifted flow, then GH at 0 applies to Qu
and kills the eigen-distribution. Such a symbol exists only if the lifted flow is uniformly conformal on WF(u) with
rate Re c / m. That is exactly the situation that non-hyperbolic positive-entropy measures exclude, and it is where
the approach stops.

Conventions as in the brief: nu smooth positive density, d = div_nu X, P = X + d, J_t(x) = int_0^t d(g_s x) ds,
and a chain at c means B, A in (C^1)' with B != 0, B(P phi) = c B(phi), A(P phi) = c A(phi) + B(phi).
In generalized functions, u = B/nu and v = A/nu satisfy Xu = -cu and Xv = -cv - u (Observation 0).

## 1. Model chains without GH: what the strip, |Im c| and wavefront sets can see

**Proposition 1.1 (orbit chains; no GH).** Let x in M and real a < b, C satisfy
 J_t(x) <= C + a t for t >= 0, and J_t(x) <= C + b t for t <= 0.
Then for every z with a < Re z < b the formula
 T_z(phi) := int_R e^{J_t(x) - z t} phi(g_t x) dt
defines a complex Borel measure (order 0). The map z -> T_z(phi) is holomorphic, and it is bounded by C(z) ||phi||_inf,
locally uniformly in z. Moreover T_z(P phi) = z T_z(phi) and T_z != 0. Hence (B, A) = (T_z, d/dz T_z) is a chain at
every z of the strip, of order 0:
 A(P phi) = z A(phi) + B(phi), where A(phi) = -int t e^{J_t(x) - zt} phi(g_t x) dt.

*Proof.* |e^{J_t - zt}| <= e^C e^{(a - Re z)t} for t >= 0 and <= e^C e^{(b - Re z)t} = e^C e^{-(b - Re z)|t|} for t <= 0.
So the integral and its z-derivatives converge absolutely, locally uniformly on the strip, which gives holomorphy and
the bound. Next, d/dt [e^{J_t - zt} phi(g_t x)] = e^{J_t - zt} [(P phi)(g_t x) - z phi(g_t x)], because
d/dt J_t = d(g_t x) and d/dt phi(g_t x) = (X phi)(g_t x). Integrate over [-R, R]; the boundary terms tend to 0 by
the bounds above, so T_z(P phi) = z T_z(phi). Differentiating this identity in z gives the chain relation for
A = d/dz T_z.
Nonvanishing. x is neither a zero nor periodic. Indeed, then J_t(x) = (I/T) t + O(1) for all t, with I/T the mean of d
over the orbit, and the two hypotheses would force I/T <= a and I/T >= b. So t -> g_t x is injective, and near t = 0
the orbit is an embedded arc through a flow box. Take phi = psi chi_n, with psi a bump supported in a flow box around x
and chi_n a sequence of bumps that localises to the plaque of x. Then T_z(phi) tends to
int psi(g_t x) e^{J_t - zt} dt over |t| small, which can be chosen nonzero.
(If the orbit returns to the box, the other plaques are excluded by chi_n, since the returning arcs are disjoint
from the plaque of x.) ∎

**Example 1.2 (strips not containing 0 occur for non-GH fields).** On S^2 take a Morse-Smale gradient-like field with a
source p_1 with eigenvalues 1, 2 (so d(p_1) = tr DX(p_1) = 3; d at a zero does not depend on nu) and a saddle p_2
with eigenvalues 2, -1 (d(p_2) = 1), plus other zeros as needed. Let x be on the stable curve of p_2, with
alpha-limit p_1. By exponential convergence, J_t(x) = 1·t + O(1) for t >= 0 and J_t(x) = 3t + O(1) for t <= 0.
So Proposition 1.1 gives order-0 chains at EVERY c with 1 < Re c < 3, a strip not containing 0. (This X is not GH,
e.g. by Corollary 4.2/Lemma K or simply because of the zeros' basins.)

**Consequences for approaches (1) and (2) of the brief (rigorous statements about the model).**
(a) *The point c does not matter.* In Proposition 1.1, T_{sigma + iy} is the measure T_sigma multiplied, along the
orbit, by the unimodular factor e^{-iyt}. Hence WF(T_{sigma+iy}) is independent of y. Off the closure of the
limit sets it equals the conormal bundle N^*(orbit) \ 0, which is all of Sigma = {xi(X) = 0} over the orbit points.
The semiclassical wavefront set at h = 1/y is the affine set {xi : xi(X) = -1} over the orbit (the phase -t/h has
derivative -1 along X). The damping in the transport equation for any defect measure is the same function
J_t - sigma t for every y. So taking |Im c| -> infinity produces exactly the data available at y = 0, rescaled.
That data exists for non-GH flows with a strip not containing 0 (Example 1.2).
(b) *Consequently an argument of type (1)/(2) must inject GH through a global property.* The facts it uses about
the chain are: WF(u) is closed, conic, contained in Sigma and invariant under the cotangent lift (Lemma 3.1 below);
propagation; radial estimates at sources/sinks of the lifted flow; and transport of defect measures with real
damping Re c. All of these hold verbatim for the chains of Example 1.2, so they cannot by themselves yield a
contradiction. The only GH inputs known (K0, K1, closed range, Theorem J, Lemma K) are global and act at the
spectral point 0, so a proof must transfer the chain to the point 0. Section 3 does this transfer microlocally, and
its limits are identified there.
(c) In Example 1.2 the fibre over p_1 is a radial set for the lifted flow (all covectors decay forward, with rates
-1, -2), so radial estimates do give information there. That information only constrains the regularity of u near
p_1 relative to a threshold depending on Re c. It is consistent with the existence of the chain (the chain exists).
For a non-hyperbolic positive-entropy measure there is a zero exponent transverse to X, so its conormal set
contains neutral directions and no radial set of this type.

## 2. Orbit chains under GH (proved, from Lemma C, Lemma K/K', Corollary 4.1, Observation P, P1)

Call x *(a,b)-admissible* if it satisfies the hypothesis of Proposition 1.1 with a < b.

**Proposition 2.1.** Assume GH and dim M >= 2, and let x be (a,b)-admissible.
(i) 0 is not in (a, b).
(ii) If x is exponentially backward-asymptotic to a periodic point or zero, i.e. d(g_{-mP} x, p) <= C kappa^m for
some p with g_P p = p, some kappa < 1 and all m >= 0 (e.g. x in W^{uu}(q), q on a hyperbolic periodic orbit or a
hyperbolic zero), then a >= 0.
(iii) If x is exponentially forward-asymptotic to a periodic point or zero, then b <= 0.
(iv) x does not lie on a connection W^u(gamma_1) ∩ W^s(gamma_2) between hyperbolic periodic orbits or hyperbolic
zeros (gamma_1 = gamma_2 allowed).
Hence, under GH, no orbit chain of Proposition 1.1 exists whose orbit connects hyperbolic periodic orbits or zeros,
at any c whatsoever. In particular the chains of Example 1.2 are excluded.

*Proof.* (i) If a < 0 < b, then e^{J_t(x)} <= e^C e^{-min(-a, b)|t|}, so int_R e^{J_t(x)} dt < infinity,
contradicting Lemma C.
(ii) If a < 0, then J_t(x) <= C - |a| t for t >= 0, which is hypothesis (b) of Lemma K, with eps = |a|.
Hypothesis (a) of Lemma K is the assumed backward asymptotics, and x != p because x is not periodic (proof of
Proposition 1.1). Lemma K gives a contradiction.
(iii) If b > 0, then J_t(x) <= C - b|t| for t <= 0. With the forward asymptotics, Lemma K' gives a contradiction.
(iv) By [SM] (quoted in R6-a §4), x in W^{uu}(q_1) ∩ W^{ss}(q_2) for some q_i in gamma_i, with exponential
convergence. Then (ii) and (iii) give 0 <= a < b <= 0, which is impossible. ∎
(Alternative for (iv): J_t(x) = lambda_1 t + O(1) for t <= 0 and lambda_2 t + O(1) for t >= 0, with
lambda_i = I(gamma_i)/P_i. Admissibility forces lambda_2 <= a < b <= lambda_1. Corollary 4.1 together with
Observation P and P1 forces lambda_1 < 0 < lambda_2.)

**Remark 2.2 (what is left for orbit chains).** By Proposition 2.1, an orbit chain under GH needs an orbit whose
forward and backward behaviour is not exponentially governed by periodic orbits. For instance, its alpha- and
omega-limit sets carry measures of positive entropy or zero transverse exponents, with Birkhoff rates
lambda_+ <= a < b <= lambda_- of the same sign. This is exactly the planner's statement (SO), restricted to orbits
with exponential bounds. I could not exclude it. General order-1 chains need not be orbit-supported at all;
those of Theorem R come from unstable-leaf conditionals.

## 3. Making GH act at c != 0 microlocally: the multiplier criterion and its obstruction

Notation: p(x, xi) = xi(X(x)) on T^*M; Sigma = {p = 0} \ 0. Phi_t(x, xi) = (g_t x, (Dg_t(x))^{-T} xi) is the
cotangent lift of the flow, which is the Hamilton flow of p (standard). The operator X has full symbol i p.

**Lemma 3.1 (proved).** If u in D'(M) and Xu = -cu, then u o g_t = e^{-ct} u for all real t. Moreover
WF(u) ⊂ Sigma, and WF(u) is invariant under Phi_t. If u != 0 and Re c != 0, then WF(u) is nonempty.
*Proof.* t -> u o g_t is C^1 into D' with derivative (Xu) o g_t = -c u o g_t. (Pair with a test density and
differentiate under the pairing; the pulled-back test densities depend smoothly on t.) So e^{ct} u o g_t is
constant, equal to u. Pull-back by a diffeomorphism transforms wavefront sets by the cotangent map:
WF(u o g_t) = Phi_t^{-1}(WF(u)). Hence WF(u) = Phi_t^{-1} WF(u) for all t. X + c is a first-order differential
operator with principal symbol i p, elliptic off Sigma, so microlocal elliptic regularity gives WF(u) ⊂ Sigma.
If WF(u) = ∅, then u is smooth. f = |u|^2 satisfies Xf = -2 Re c f, and at a maximum point of f we get Xf = 0, so
f = 0 there and u = 0. ∎

**Proposition 3.2 (multiplier criterion; proved).** Assume GH. Let u in D'(M), c in C with Re c != 0, and Xu = -cu.
Suppose there is a pseudodifferential operator Q in Psi^m(M) (classical, any real m) such that
 (1) WF(u) ⊂ ell(Q), and
 (2) WF'(R) ∩ WF(u) = ∅, where R := [X, Q] - c Q.
Then u = 0. Consequently no chain (A, B) at c has WF(B/nu) admitting such a Q.
*Proof.* X(Qu) = Q(Xu) + [X, Q]u = -cQu + [X, Q]u = Ru. By (2), WF(Ru) ⊂ WF'(R) ∩ WF(u) = ∅, so Ru is smooth. By GH,
Qu is smooth. By microlocal elliptic regularity, WF(u) ∩ ell(Q) ⊂ WF(Qu) = ∅, so (1) gives WF(u) = ∅. Lemma 3.1 then
gives u = 0. For a chain, apply this to u = B/nu, which is nonzero. ∎
This is idea (3) of the brief made precise: Qu is the non-smooth distribution with smooth X-derivative. The proof
uses GH exactly once, for a smooth right-hand side.

**Lemma 3.3 (the obstruction; proved).** Let Gamma be a nonempty closed conic Phi-invariant subset of Sigma, and Q
classical of order m with principal symbol q, satisfying (1) and (2) with Gamma in place of WF(u). Then
q(Phi_t zeta) = e^{ct} q(zeta) and q(zeta) != 0 for zeta in Gamma. Consequently m != 0, and, for any Riemannian norm
on T^*M, there is K with
 | log|Phi_t zeta| - log|zeta| - (Re c / m) t | <= K for all zeta in Gamma and all real t.
So the lifted flow on Gamma is *uniformly conformal*: every covector in Gamma grows (or decays) at the single rate
chi = Re c / m, up to a bounded factor, in both time directions.
*Proof.* The principal symbol of [X, Q] is (1/i){ip, q} = {p, q} = H_p q, so sigma_m(R) = H_p q - c q. By (2), R is
smoothing microlocally near Gamma, so its principal symbol vanishes on a conic neighbourhood of Gamma. Hence
d/dt q(Phi_t zeta) = (H_p q - cq)(Phi_t zeta) + c q(Phi_t zeta) = c q(Phi_t zeta) for zeta in Gamma (Phi_t zeta stays in
Gamma), so q(Phi_t zeta) = e^{ct} q(zeta). By (1), q != 0 on Gamma. Write q(zeta) = |zeta|^m q(hat zeta), with hat zeta the
unit covector. Gamma ∩ {|zeta| = 1} is compact, and |q| is continuous and positive there, between q_min and q_max.
Taking log|.| gives m log(|Phi_t zeta|/|zeta|) = Re c · t + log|q(hat zeta)| - log|q(hat{Phi_t zeta})|. The last two terms
are bounded by log(q_max/q_min). If m = 0 this gives |Re c · t| <= const for all t, contradicting Re c != 0. ∎

**Corollary 3.4 (why the microlocal route stops; proved given the cited facts).** Let mu be an ergodic invariant
probability with h_mu(g_1) > 0. By Ruelle's inequality for g_1 and g_{-1} (cited), mu has a positive and a negative
Lyapunov exponent transverse to X. Sigma_x = ann(X(x)) is the dual of the normal space T_xM/RX(x), and Phi_t acts on it
as the inverse transpose of the induced normal cocycle. So for mu-a.e. x, Sigma_x contains covectors growing at
positive rates and covectors decaying at negative rates. Lemma 3.3 then shows that no classical multiplier exists for
any closed invariant Gamma containing Sigma_x for such an x. The same holds when Gamma contains two covectors over one
regular point whose Oseledets rates differ. In particular:
- the families of Theorem R' (block R9-a, Steps 7-8) are Laplace transforms of a pair
  S = delta_x - e^b delta_y. Here x and y are mu-generic points on one local unstable leaf, and
  T_z = int e^{-zt}(e^{J_t(x)} delta_{g_t x} - e^{b + J_t(y)} delta_{g_t y}) dt.
  So B = T_z is a complex measure carried by the two orbits, whose closure is supp mu. Its WF set is a closed
  Phi-invariant subset of Sigma over supp mu. I expect it to contain the conormal directions Sigma_{g_t x} over the
  orbit, which carry mixed-sign rates, and then Lemma 3.3 forbids a classical multiplier. I have NOT proved this,
  because other arcs of the recurrent orbit accumulate at g_t x and could in principle cancel the local conormal
  singularity. Either way, Proposition 3.2 cannot be applied without knowing that WF(B/nu) is uniformly conformal,
  and nothing makes it so.
- If instead WF(B/nu) lies in a uniformly conformal invariant cone, then (granting the converse, constructing q with
  q o Phi_t = e^{ct} q and solving the lower-order transport equations, which I have NOT proved) the chain is excluded
  by Proposition 3.2.
*Variable orders do not help (sketch).* For q = |zeta|^{m(hat zeta)} rho(hat zeta) (anisotropic classes), H_p q contains
the term (H_p m) log|zeta| q, which is of larger order than c q unless H_p m = 0 on Gamma. Then m is constant on Phi-orbit
closures, and Lemma 3.3 applies on each of them. Over a positive-entropy measure, the projective orbit of a generic
covector has forward and backward limits with different rates, so uniformity fails on a single orbit closure.

**Summary of Section 3.** GH can be made to act at c != 0 microlocally exactly when a symbol "intertwining" X with
X - c exists on the wavefront set. Such a symbol is a uniformly conformal structure of the lifted flow. That structure
is incompatible with positive entropy (mixed-sign transverse exponents), which is precisely the case to be excluded.
So Proposition 3.2 cannot by itself prove (JC). Any microlocal proof needs either a non-pseudodifferential
intertwiner (e.g. a Fourier integral operator or a non-tame object) or a different input than GH at 0.

## 4. Status

**Proved in this answer.**
1. Proposition 1.1 (no GH): every (a,b)-admissible orbit gives order-0 Jordan chains (B, A) = (T_z, d/dz T_z) at
   every z of the strip a < Re z < b. Example 1.2: such strips avoiding 0 occur for smooth non-GH fields on S^2.
   So (NJ) and (JC) are genuinely GH statements even at order 0. The WF and semiclassical data of these chains do
   not depend on Im z, which makes rigorous point 1(a)-(b): taking |Im c| -> infinity gives no new information.
2. Proposition 2.1 (GH): admissible orbits have 0 not in (a,b). Backward exponential asymptotics to a periodic point
   or zero force a >= 0, and forward asymptotics force b <= 0. Connections between hyperbolic periodic orbits or
   zeros are never admissible. So under GH, orbit chains whose orbits are governed at both ends by hyperbolic
   periodic orbits or zeros do not exist, at any c.
3. Lemma 3.1, Proposition 3.2 (GH): an eigen-distribution at c with Re c != 0 is zero as soon as a
   pseudodifferential Q, elliptic on WF(u), satisfies [X,Q] - cQ smoothing near WF(u). This is the precise
   microlocal form of idea (3): Qu is a solution of X(Qu) = smooth, so GH at 0 applies.
4. Lemma 3.3: such a classical Q exists only if the cotangent-lifted flow is uniformly conformal on WF(u), with the
   single rate Re c / m (bounded distortion, both time directions). Corollary 3.4: this is incompatible with the
   mixed-sign transverse exponents of a positive-entropy measure, wherever WF(u) contains a full conormal fibre
   (or two covectors with different Oseledets rates) over a regular point of such a measure.

**Sketched only.** The variable-order extension of Lemma 3.3 (end of Section 3). The expected, unproved
description of WF(B/nu) for the pair families of Theorem R'.

**Not done.** I did not re-check Theorem A (step 3 of the chain); I used only its statement. I found no flaw in
steps 1-2 as quoted (block R9-a); the families there are pair-orbit transforms, as used in Corollary 3.4.

**Open (precisely).**
(O-a) (JC) itself, i.e. for each strip avoiding 0, one point c without an order-1 chain. Equivalently, via Theorem R'
and Theorem A, exclude under GH the pair families T_z = int e^{-zt} S(Gamma_t .) dt, S = delta_x - e^b delta_y, on
strips (lambda + delta, lambda + theta - delta) with lambda = mu(d) != 0 not covered by Prop. 6.1/6.2 of R6-a.
For lambda = 0 the strip touches 0, which is the separate (J1-0) question.
(O-b) The orbit version (SO) for orbits not governed by hyperbolic periodic orbits at both ends (Remark 2.2).
(O-c) A non-pseudodifferential intertwiner: an operator Q, injective on distributions supported in WF(u) (or a
substitute), with X Q - Q (X + c) smoothing, constructed without uniform conformality. By Lemma 3.3 it cannot be a
classical ΨDO. This is where the microlocal approach stops.
(O-d) Whether GH gives a finite-regularity statement (Xw in C^{m(k)} implies w in C^k for distributions w). This
would let Proposition 3.2 tolerate finite-order errors R, but I could not prove it from the closed-graph argument,
since mollification does not commute with X.

Conclusion: (JC) and (NJ) remain unproved and unrefuted, and so does the zero-entropy goal in dim M >= 4.

=== END OF ANSWER round10_q8 ===
