# round9_q2 — answer

## 0. Status (read this first)

**I did not prove (EF), and I did not find a counterexample.** What this file contains is:

1. a **proved structural lemma** on the *modulus* of an order-0 eigen-family (Lemma 1), together with a proof
   that the positivity information carried by a strip family is **vacuous** under GH (Prop. 2, Cor. 3): the set of
   "conformal eigenvalues" always contains every number of the form mu(d), mu ergodic, so no argument that only
   sees |T_z| can prove (EF). This closes one route with a proof.
2. a **proved "no-information" theorem for the planner's mechanism (B)** (the Leibniz/module structure):
   in the volume case, the full content of the eigen-equation `T o X = z T` for an order-<=1 functional T, z != 0,
   is **exactly** the single fixed-point relation `tau = z (tau o R)` on smooth omega-mean-zero functions together
   with `T(1) = 0` (Theorem 5). Consequently every identity obtainable from the Leibniz rule (and in particular the
   expansion `T(phi psi) = z^N T(phi R^N psi) - sum_{j=1}^N z^{j-1} T((X phi) R^j psi)` of Prop. 6) is a formal
   consequence of the relation already exploited in Theorem V of R7-e, and cannot exclude T. So mechanism (B) of
   the suggestion **cannot work**, in the volume case, for any choice of the auxiliary function phi. (Outside the
   volume case P has no tame inverse at all, by Proposition A of R8-d, so the mechanism does not even start.)
3. a **reformulation** of (EF) in the volume case as a statement about the point spectrum of the transpose of the
   tame inverse R, plus the observation (with the unilateral-shift example) that this statement is **not** a formal
   consequence of Banach/Fréchet operator theory: open sets of adjoint eigenvalues with holomorphic normalised
   eigenvectors are the generic situation for one-sided shifts (Remark 7). This explains, rigorously, why no purely
   functional-analytic use of GH ("kernel = constants + closed range") can give (EF), and matches the heuristic of
   R8-c Section 3.
4. an elementary **band lemma** (Lemma 8) locating all possible strips, and a short list of the routes I checked
   and found dead, with reasons (Section 5).

Everything labelled Lemma/Proposition/Theorem below is proved in full. Nothing below is conditional on unchecked
citations except where explicitly stated. Conventions are those of the brief: nu is a smooth positive density,
d = div_nu X, J_t(x) = int_0^t d(g_s x) ds, P phi = X phi + d phi, Gamma_t phi = e^{J_t} (phi o g_t), and a
distribution density is a continuous linear functional on C^inf(M); "order <= k" means continuous for the C^k norm.
GH is the hypothesis of the problem; L1, (F1), (F2), (K0), (K1) are as in the brief's background.

I also record that I believe the chain of the attempt (steps 1-3 of the brief) to be correct as stated; I re-checked
step 1 and Theorem R (Section 6) and found no flaw.

---

## 1. Preliminaries used throughout

**Fact 1.1 (transport identity; no GH).** For a distribution density T and smooth phi, t -> Gamma_t phi is C^inf
from R into C^inf(M), with (d/dt) Gamma_t phi = Gamma_t (P phi) = P(Gamma_t phi). Hence if T o P = z T then
h(t) := T(Gamma_t phi) satisfies h' = z h, i.e.

  T(Gamma_t phi) = e^{z t} T(phi)   for all real t.        (1.1)

(Proof: as in Theorem J step 1 of R6-a and Lemma 1.1 of R8-b; (t,x) -> e^{J_t(x)} phi(g_t x) is jointly smooth, so
difference quotients converge in every C^m uniformly on compact t-intervals.)

**Fact 1.2 (pushforward form of (1.1); no GH).** If T is a *complex Borel measure* on M then
T(Gamma_t phi) = int phi d[(g_t)_*(e^{J_t} T)], so (1.1) is equivalent to

  (g_t)_* ( e^{J_t} T ) = e^{z t} T   for all real t.       (1.2)

---

## 2. The modulus of an order-0 eigen-family: positivity is vacuous

**Lemma 1 (modulus lemma; proved, no GH).** Let T be a nonzero complex Borel measure on M with T o P = z T for
some z in C. Put m := |T| (total variation measure) and c := Re z. Then

  (i) (g_t)_*(e^{J_t} m) = e^{c t} m for all t, equivalently m(P phi) = c m(phi) for all smooth phi
      ("m is a c-conformal probability after normalisation");
  (ii) c = m(d)/m(M);
  (iii) writing T = h m with |h| = 1 m-a.e. (polar decomposition), one has h o g_t = e^{-i (Im z) t} h  m-a.e.,
        for every t: the conformal measure m carries a measurable unimodular eigenfunction of the flow with
        eigenvalue -i Im z.

*Proof.* (i) For a positive continuous weight w one has |w T| = w |T| (write dT = h d|T| with |h| = 1), and for a
Borel bijection G with Borel inverse one has |G_*rho| = G_*|rho| (pushforward along a bijection matches partitions
of a set with partitions of its preimage). Apply this with w = e^{J_t} and G = g_t to (1.2):
|e^{zt} T| = e^{ct} m on the one hand, and |(g_t)_*(e^{J_t}T)| = (g_t)_*(e^{J_t} m) on the other. This is the
displayed identity; pairing with phi gives m(Gamma_t phi) = e^{ct} m(phi), and differentiating at t = 0 (dominated
convergence, Fact 1.1) gives m(P phi) = c m(phi).
(ii) Put phi = 1 in m(P phi) = c m(phi) and use P 1 = d.
(iii) Fix t. The measure (g_t)_*(e^{J_t} T) = e^{zt} h m has, with respect to (g_t)_*(e^{J_t} m) = e^{ct} m, the
density (h o g_t^{-1}); comparing the two expressions of the same measure gives h o g_{-t} = e^{i(Im z) t} h
m-a.e., which is the claim with t replaced by -t. ∎

So the modulus of an order-0 eigen-density is a tilted conformal measure in the sense of Prop. 2.2 of R4-q7, whose
eigenvalue is Re z and which "knows" Im z only through a measurable unimodular eigenfunction.

**Proposition 2 (conformal eigenvalues always fill at least the set of ergodic averages of d; proved, no GH).**
Let C := { c in R : there is a Borel probability m on M with m(P phi) = c m(phi) for all smooth phi }. Then
 (a) C is a nonempty compact subset of R;
 (b) C contains mu(d) for every ergodic flow-invariant probability mu;
 (c) C contains a number >= 0 and a number <= 0; under GH, 0 in C and the 0-conformal probability is unique,
     namely nu-hat = nu/nu(M).

*Proof.* (b) is Prop. 2.2 of R4-q7, re-proved here for completeness: take x generic for mu in both time directions,
so J_t(x) - mu(d) t = o(|t|) as t -> ±inf; then c_s(t) := e^{J_t(x) - mu(d) t - s|t|} is integrable for each s > 0
and tends to 0 at ±inf; integrating d/dt [c_s(t) phi(g_t x)] = c_s(t)[(P phi - mu(d) phi)(g_t x) - s sgn(t)
phi(g_t x)] over R gives |T_s(P phi - mu(d) phi)| <= s ||phi||_inf for the normalised probabilities T_s carried by
the orbit; any weak* limit as s -> 0+ is a probability m with m(P phi) = mu(d) m(phi).
(a) Nonemptiness follows from (b) (invariant measures exist). Compactness: if m_n is c_n-conformal, c_n -> c and
m_n -> m weak*, then m is a probability and m(P phi) = c m(phi); boundedness of C follows from (ii) of Lemma 1
(|c| = |m(d)| <= ||d||_inf).
(c) By Prop. 2.1 of R4-q7 there are ergodic mu_± with mu_+(d) >= 0 >= mu_-(d); apply (b). Under GH, nu-hat is
0-conformal (int P phi dnu = int L_X(phi nu) = 0) and uniqueness is (F1). ∎

**Corollary 3 (the positivity route to (EF) is vacuous; proved).** Let (T_z) be a family as in (EF) which in
addition consists of *measures* (order 0). Then the only information extractable from the moduli |T_z| is that the
numbers Re z, z in Omega, all lie in C. Since C contains, with no hypothesis at all, every value mu(d) of an
ergodic measure, and since the problem's own chain produces strips at Re z near lambda = mu(d) (Theorem R), GH does
not contradict this. In particular no argument which uses only the positive measures |T_z| (conformality,
uniqueness of conformal measures at eigenvalue 0, Lemma C/Lemma D of the background) can prove (EF).

*Proof.* Immediate from Lemma 1 and Proposition 2: the map z -> |T_z| forgets Im z, and the resulting constraint
"Re z in C for all z in Omega" is satisfiable: e.g. take X with an ergodic mu, lambda = mu(d), and recall from
Prop. 2 that lambda in C; the conformal measures produced by Prop. 2 exist for GH fields as well (nothing in the
proof of Prop. 2 uses or contradicts GH). ∎

**Remark 4 (what Lemma 1(iii) would need).** One could hope to contradict (EF) for order-0 families as follows: if
the c-conformal probability were *unique* for each c (as it is for c = 0 under GH, by (F1)), then all the measures
|T_{c+iy}|, y in R, would be one fixed probability m_c, and by Lemma 1(iii) m_c would carry measurable unimodular
eigenfunctions for every eigenvalue in an interval of iR, hence (taking products and quotients of the h's) for
every real eigenvalue. For a *measure-preserving* ergodic flow this is impossible (eigenvalues form a countable
group, by orthogonality in the separable space L^2). For a nonsingular (here: conformal, hence not invariant)
ergodic action it is **not** impossible: the translation flow on R with any probability measure equivalent to
Lebesgue has h_y(x) = e^{i y x} as eigenfunction for every y. I could neither prove uniqueness of c-conformal
measures for c != 0 under GH (Lemma C and Lemma D of the background use (F1), i.e. c = 0, in an essential way:
the tilted equation m(P phi) = c m(phi) is not the kernel of any operator to which GH applies), nor rule out the
dissipative single-orbit behaviour, which is exactly the behaviour of the measures that Theorem R produces. So
Remark 4 is a *possible* route for order-0 families only, and it needs a new uniqueness theorem at c != 0; note
that Lemma C of the background (int_R e^{J_t(x)} dt = inf under GH) does **not** tilt: its proof uses (F1).

---

## 3. The Leibniz/module mechanism (B) carries no information

Throughout this section: GH holds **and** X preserves a smooth positive probability density omega (the "volume
case"). Take nu = omega, so d = 0, J = 0, P = X, Gamma_t phi = phi o g_t. By (O2) the invariant distribution
densities are the multiples of omega, X(C^inf) = C_0^inf := {f : omega(f) = 0} (duality consequence of Text A),
and by Corollary 3 of Text B, X : C_0^inf -> C_0^inf is a topological isomorphism of Fréchet spaces; let
R := (X|_{C_0^inf})^{-1} and phi_0 := phi - omega(phi) (omega normalised to mass 1). Note R(C_0^inf) = C_0^inf.

Outside the volume case none of this is available: by Proposition A of R8-d, P(C^inf) is closed **iff** X preserves
a smooth positive density, so P has no continuous inverse on its range unless we are in the volume case. This is
why mechanism (B), which needs to divide by X or by P, is confined to the volume case from the start.

**Proposition 5 (Leibniz identity; proved).** Let T be any linear functional on C^inf with T o X = z T. Then for
every smooth phi and every smooth psi with omega(psi) = 0,

  T(phi psi) = z T(phi R psi) - T((X phi) R psi).        (3.1)

*Proof.* X(phi · R psi) = (X phi)(R psi) + phi X(R psi) = (X phi)(R psi) + phi psi. Apply T and use
T(X(·)) = z T(·). ∎

**Proposition 6 (the iterated expansion; proved).** With the hypotheses of Prop. 5, for every N >= 1,

  T(phi psi) = z^N T(phi R^N psi) - sum_{j=1}^{N} z^{j-1} T( (X phi) R^{j} psi ).      (3.2)

*Proof.* Put A_k := T(phi R^k psi), B_k := T((X phi) R^k psi) (all R^k psi are smooth and omega-mean-zero). By
(3.1) applied to R^k psi in place of psi: A_k = z A_{k+1} - B_{k+1}. Iterate from k = 0. ∎

For phi = 1 this is the relation T(psi) = z^N T(R^N psi) used in Theorem V of R7-e and in Lemma Q of R8-a. The
planner's suggestion (B) was to use nonconstant phi to transport tame estimates. The next theorem shows that this
cannot help, for a reason that is not quantitative but logical: (3.1), (3.2) and every other consequence of the
Leibniz rule are formal consequences of the single relation of Theorem V.

**Theorem 5' (the content of the eigen-equation; proved).** Assume the volume case above and let z != 0. The
restriction map T -> tau := T|_{C_0^inf} is a bijection

  { T : C^inf -> C linear, T o X = z T }  -->  { tau : C_0^inf -> C linear, tau = z (tau o R) },

and its inverse is tau -> T, T(phi) := tau(phi_0). Under this bijection T(1) = 0 automatically, and T is
continuous for the C^k norm if and only if tau is.

*Proof.* (a) If T o X = z T then T(1) = z^{-1} T(X 1) = 0, hence T(phi) = T(phi_0) for all phi, so T is determined
by tau. For psi in C_0^inf we have psi = X(R psi), so tau(psi) = T(X R psi) = z T(R psi) = z tau(R psi) (using
R psi in C_0^inf). Thus tau satisfies the fixed-point relation.
(b) Conversely let tau satisfy tau = z (tau o R) on C_0^inf, and put T(phi) := tau(phi_0). Then for smooth phi,
X phi is in C_0^inf and (X phi)_0 = X phi, so T(X phi) = tau(X phi); also phi_0 = R(X phi_0) = R(X phi), so
z T(phi) = z tau(phi_0) = z tau(R(X phi)) = tau(X phi) by the hypothesis. Hence T o X = z T.
(c) The two constructions are mutually inverse, and continuity in the C^k norm is preserved in both directions
because phi -> phi_0 is C^k-bounded. ∎

**Corollary (mechanism (B) cannot work).** Let z != 0. Every identity satisfied by all order-<=1 functionals T with
T o X = z T — in particular (3.1), (3.2) for all phi and psi, and any identity derived from the Leibniz rule, from
the module structure of C^inf over itself, or from the dual division of GH (O1) — is a formal consequence of the
single relation `tau = z(tau o R)` on C_0^inf. Hence no such identity can exclude the existence of a nonzero T:
the set of solutions it cuts out is exactly the set of solutions of the fixed-point relation. In particular, to
prove (EF) along the lines of (B) one must prove that the fixed-point relation has no nonzero order-1 solution for
z in the strip, i.e. precisely the statement that Theorem V of R7-e reduces to a Carleman condition on
||R^N phi||_{C^1}. Quantitatively: the "new" terms in (3.2) are the T((X phi)R^j psi), whose only available bounds
are C ||X phi||_{C^1} ||R^j psi||_{C^1} with the *non-decaying* coefficients |z|^{j-1}; so the estimate obtained
from (3.2) is never better than the one obtained from the case phi = 1 (which has no such terms), and it is worse
unless X phi = 0, i.e. (by L1) unless phi is constant.

*Proof.* The first two sentences are Theorem 5' (the solution set is unchanged). The quantitative last sentence is
read off (3.2): taking absolute values gives
|T(phi psi)| <= C|z|^N ||phi R^N psi||_{C^1} + C sum_{j=1}^N |z|^{j-1} ||X phi||_{C^1} ||R^j psi||_{C^1}, and the
sum contains ||R^j psi||_{C^1} for every j <= N with coefficient |z|^{j-1} > 0. ∎

**Remark 7 (why no functional analysis alone can give (EF)).** By Theorem 5', in the volume case (EF) says exactly:
*the transpose of R has no holomorphic family of order-<=1 eigenfunctionals with eigenvalues 1/z filling an open
set.* This is **not** a formal property of operators: for the unilateral forward shift S on l^2, the adjoint S^*
has every point of the open unit disc as an eigenvalue, with eigenvectors depending holomorphically and locally
boundedly on the eigenvalue. The tame properties that GH gives R (continuity, ||R psi||_{C^k} <= C_k
||psi||_{C^{m_k}}, injectivity, surjectivity onto C_0^inf) are all shared by a shift-like operator. Therefore any
proof of (EF) must use the *dynamical* fact that R inverts the generator of a one-parameter group of composition
operators, not only the operator-theoretic consequences of GH. This makes rigorous the heuristic of R8-c Section 3
("in infinite dimensions the finite-dimensional argument fails as soon as there is continuous spectrum; the shift
on L^2(R) has functionals with one-sided decay").

---

## 4. A band lemma (elementary, locates the possible strips)

**Lemma 8 (proved, no GH).** Fix k >= 0 and let T != 0 be a distribution density of order <= k with T o P = z T.
Put Lambda_k^+ := limsup_{t -> +inf} (1/t) log ||Gamma_t||_{C^k -> C^k} and
Lambda_k^- := limsup_{t -> +inf} (1/t) log ||Gamma_{-t}||_{C^k -> C^k}. Then

  -Lambda_k^- <= Re z <= Lambda_k^+ .

*Proof.* Pick phi with T(phi) != 0. By (1.1), e^{Re z t} |T(phi)| = |T(Gamma_t phi)| <= ||T||_{(C^k)'}
||Gamma_t||_{C^k->C^k} ||phi||_{C^k}. Take logarithms, divide by t and let t -> +inf; then do the same with
t -> -inf. ∎

Consequences. (i) ||Gamma_t||_{C^0->C^0} = sup_x e^{J_t(x)}, whose exponential rate is max_mu mu(d) forward and
max_mu(-mu(d)) backward (Prop. 2.1 step 1 of R4-q7). So all order-0 eigenvalues satisfy
min_mu mu(d) <= Re z <= max_mu mu(d), the extrema being over invariant probabilities; and by Proposition 2 every
value mu(d), mu ergodic, is attained by an order-0 eigen-density. So Lemma 8 is essentially sharp at k = 0 and
gives no contradiction. (ii) For k = 1 the rate involves in addition sup_x ||Dg_t(x)||, whose rate is the
quantity lambda* of R5-a; so a nonzero order-1 eigen-distribution with Re z > max_mu mu(d) forces lambda* > 0.
This is a (very weak) converse to Theorem R, and it shows that (EF) for strips far from 0 is "allowed" by the
coarse growth bounds exactly in the positive-entropy regime; no contradiction.

---

## 5. Routes checked and found dead (with the reason)

(D1) **Positivity / moduli.** Dead by Corollary 3: the modulus of an order-0 eigen-density is a conformal measure,
and conformal measures with eigenvalue c exist for every c = mu(d); GH constrains only c = 0.

(D2) **Leibniz / module structure (the planner's bet (B)).** Dead by Theorem 5' and its corollary: in the volume
case the Leibniz identities carry no information beyond the fixed-point relation tau = z(tau o R); outside the
volume case the required division by P is unavailable (Prop. A of R8-d).

(D3) **Moving the strip.** Dead for the reasons already recorded in the brief ((C)) and re-checked here:
 - changing nu to e^a nu conjugates P by e^{a} and changes neither Sigma_k nor the strip (brief's remark);
 - a constant time change X -> cX rescales z by c, so it cannot move a strip contained in {Re z > 0} to one
   containing 0;
 - a real shift z -> z - kappa would require a smooth a with X a = kappa != 0, forbidden by (K1);
 - multiplication by a smooth eigenfunction (X psi = i gamma psi, |psi| = 1) shifts z by i gamma only, i.e. moves
   the strip vertically, never horizontally; and a smooth psi with X psi = kappa psi, kappa real != 0, cannot exist
   (at a maximum of |psi|^2 one gets 2 kappa |psi|^2 = X|psi|^2 = 0).
 - a general time change hX (h > 0 smooth) does not act on eigen-distributions at all: X u = -z u gives
   (hX) u = -z h u, which is not an eigen-equation.

(D4) **Tensor square / Hilbert-space positivity.** If T is an order-<=1 eigen-density with T o P = z T, the kernel
U := T (x) conj(T) on M x M satisfies (X (+) X) U = 2 Re z · U and is a positive-definite kernel
(U(sum_i phi_i (x) conj(phi_i)) = sum_i |T(phi_i)|^2 >= 0). This is a genuine positivity statement surviving in
order 1 (unlike (D1)). It is nevertheless useless here, for two proved reasons: (i) X (+) X on M x M is never GH,
because f(x,y) = F(the difference of first integrals) can be invariant — concretely, for a Diophantine linear flow
on T^n the product field on T^{2n} has the nonconstant invariant functions e^{2 pi i k.(x-y)}, so GH fails for the
product even when it holds for X; (ii) a positive-definite kernel distribution of order 1 need not be a measure
(T = derivative of a Dirac mass gives U(phi (x) conj(phi)) = |phi'(x)|^2 >= 0), so Lemma 1 cannot be applied to U.

(D5) **Principal symbol on the sphere bundle.** An order-<=1 functional can be represented (Riesz) as
T(phi) = mu_0(phi) + <m, dphi> with mu_0 a complex measure and m a complex TM-valued measure; (1.1) transforms the
pair by a *triangular* cocycle whose top block is m -> (g_t)_*(e^{J_t} Dg_t m) and whose off-diagonal term
(coming from d(e^{J_t}) = e^{J_t} dJ_t) lands in the order-0 part. Taking total variations of the top block would
produce a conformal measure S on the unit sphere bundle SM for the cocycle J_t + A_t, A_t(v) = log|Dg_t v|, with
eigenvalue Re z (hence Re z = int (d + a) dS by the computation of Lemma 1(ii), a(v) = <grad_v X, v>), exactly as in
Lemma C of R4-q10. I could not make this rigorous, because the decomposition (mu_0, m) is not canonical: m is
determined only modulo TM-valued measures whose divergence is a measure, and the off-diagonal term of the cocycle
is of exactly that size. Even if it were rigorous, the conclusion is a *bound* on Re z (by max_{SM}(d + a)), not a
contradiction; so this route is at best a refinement of Lemma 8.

(D6) **Strips touching 0 (suggestion (A)).** I have nothing to add beyond R8-c Corollary 2.3: the splitting
T_z = B_z + G_z has B_z holomorphic across 0, and the singular part of G_s as s -> 0+ is
(N_x(s) - e^b N_y(s)) nu-hat + o(N) with N(s) -> inf, i.e. exactly the behaviour that (F1)/(F2) permit. What is
missing is the second-order asymptotics of G_s - (that leading term) as s -> 0+, i.e. a Patterson expansion with
remainder. I looked for one and found that it requires a rate in Lemma 2.2 of R8-c (the one-sided Patterson lemma),
and that lemma's proof (weak* compactness + (F1)) is rate-free by nature; a rate would amount to an equidistribution
rate for weighted orbit averages, which is a mixing-type statement of the kind GH is not known to give.
(Indeed Corollary E of R8-f shows GH *forbids* exponential mixing rates for L^1 densities, so quantitative
equidistribution of this type cannot be expected in the form needed.)

(D7) **Making GH act at z != 0 by hypoellipticity of P - z.** Dead for the reason given in Remark 3.3 of R8-b and
re-checked: hypoellipticity of P - z for small real z > 0 already implies that
u_0 = int_{-inf}^0 e^{z s} (f o g_s) ds is smooth for every smooth f, which forces subexponential growth of the
derivatives of f o g_s and so is at least as strong as the conclusion we want. So this is circular, not a route.

---

## 6. Re-check of the chain (requested by the brief)

Step 1 (variational step) is correct: h_top(g_1) = sup over g_1-invariant m of h_m(g_1) (variational principle);
mbar := int_0^1 (g_s)_* m ds is flow-invariant and h_mbar(g_1) = h_m(g_1) because g_s conjugates g_1 to itself and
m -> h_m(g_1) is affine with the integral (Jacobs) formula over measurable decompositions; applying this to the
flow-ergodic decomposition of mbar yields a flow-ergodic component of positive g_1-entropy.

Step 2 (Theorem R) is correct as stated; I re-read the proof in R8-a. The only non-elementary inputs are Ruelle's
inequality (for g_1 and g_{-1}, giving a positive and a negative exponent), Pesin local unstable manifolds, and the
Ledrappier-Young subordinate partition together with Lemma 6.0 of R6-a (non-atomicity of the unstable conditionals
when h_mu > 0). The resulting family satisfies (i),(ii),(iii) of (EF) with the *uniform* (C^1)'-bound of (ii) on
closed substrips (the bound C(1/(Re z - lambda - delta) + 1/(lambda + theta - delta - Re z)) ||phi||_{C^1} is
uniform in Im z), so the version of (EF) in the brief (bounded, not merely polynomially bounded, on substrips) is
indeed what is needed.

Hence (EF) does imply the problem's claim, and my failure to prove (EF) leaves the problem open along this chain.

---

## 7. Explicit list of what is open

(O-1) **(EF) itself**, for strips Omega with 0 not in the closure of Omega, and for strips of the form (0, theta)
with the 1/Re z blow-up allowed at the left edge (the case lambda = mu(d) = 0 of Theorem R). Both remain open.
By Theorem 5' the volume case of (EF) is equivalent to: the transpose of the tame inverse R has no holomorphic,
locally bounded family of nonzero order-1 eigenfunctionals with eigenvalues in an open set. By Remark 7 this is not
a formal operator-theoretic statement, so a proof must use that R inverts the generator of a flow.

(O-2) **Uniqueness of c-conformal measures under GH for c != 0.** If true (for all c in an interval), Remark 4
would give (EF) for order-0 families in a possibly usable form; and it would be a genuinely new consequence of GH
away from z = 0. Status: open; I could not even decide it for c in a small interval around 0. Note it is *not*
implied by Lemma D of the background, whose proof is confined to c = 0.

(O-3) **A Patterson expansion with remainder** for the one-sided weighted orbit transforms N(s)^{-1} int_0^inf
e^{J_t(x) - st} phi(g_t x) dt as s -> 0+ (route (D6)). Open, and by Corollary E of R8-f one should not expect
exponential rates.

(O-4) The problem itself in dimension >= 4 (equivalently (PE0) of R6-a), which is what (EF) was introduced to
settle.

=== END OF ANSWER round9_q2 ===
