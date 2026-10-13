# round6_q4 — attempt to refute (PE)

Status: (PE) is neither refuted nor proved here. Below are: (1) new reduction lemmas, all proved; (2) a class-by-class check of the suggested candidate classes; (3) a combined structural theorem for a minimal counterexample; (4) the attempts to reach a contradiction and where they stop; (5) the open questions.

Conventions are those of the brief: nu is a smooth positive density, d = div_nu X, J_t is the log-Jacobian cocycle, and GH means: u in D', Xu in C^inf implies u in C^inf.

## 1. Reduction lemmas (proved)

**Lemma R1 (smooth factors inherit GH).** Let pi: M -> B be a surjective submersion of compact manifolds and X_B a vector field on B with D pi(X) = X_B o pi. If X is GH on M, then X_B is GH on B.

*Proof.*
1. For a submersion, pullback pi^*: D'(B) -> D'(M) is defined, continuous and injective.
2. pi^*(X_B u) = X(pi^* u). This holds for smooth u by the chain rule. It extends to all of D'(B) because C^inf(B) is dense in D'(B) and both sides are continuous in u.
3. pi^* u smooth implies u smooth. Locally pi is the projection (a,b) -> a, and pi^* u = u (x) 1. If u (x) 1 = F with F smooth, then F does not depend on b, since d_b F = 0 in D'. Pairing with phi(a)chi(b), where int chi = 1, gives u = F(., b0).
4. Now suppose X_B u = f is smooth. Then X(pi^* u) = pi^* f is smooth, so pi^* u is smooth by GH, and u is smooth by step 3. ∎

**Corollary R2 (products).** Let M = M1 x M2 with M1, M2 compact connected, and X = X1 (+) X2. If X is GH, then X1 and X2 are GH (Lemma R1 applied to the two projections). For the flows, h_top = h_top(X1-flow) + h_top(X2-flow) (product formula for topological entropy; cited, standard).

So if a product were a counterexample to (PE), one of the factors would be a counterexample of smaller dimension. In particular, for the theta-independent skew product X = alpha.d_theta + Y on T^d x F, the entropy is that of Y, and GH(X) implies GH(Y) on F. This class therefore reduces to dimension dim F.

**Lemma R3 (suspensions: the flow problem contains the diffeomorphism problem).** Let f be a C^inf diffeomorphism of a compact connected manifold N. Let M_f = (N x R)/Z, where the generator acts by F(y,s) = (f(y), s-1), and let X = d_s. Say f is GH if v in D'(N) and v o f - v in C^inf imply v in C^inf. Then X is GH on M_f if and only if f is GH. Moreover h_top(time-1 map) = h_top(f), by Abramov's formula with roof 1 (cited).

*Proof.* Distributions on M_f are the F-invariant distributions U on N x R.

(Step 1) GH of f implies GH of X.
1. Suppose d_s U = H with H smooth. Put K(y,s) = int_0^s H(y,sigma) dsigma.
2. Then d_s(U - K) = 0, so U - K = v (x) 1 for some v in D'(N). (A distribution on N x R with d_s V = 0 is a pullback from N.)
3. F-invariance of U gives v o f - v = K(y,s) - K(f y, s-1), which is smooth.
4. If f is GH, then v is smooth, and hence so is U.

(Step 2) GH of X implies GH of f.
1. Let v o f - v = h with h smooth. Choose chi in C^inf(R) with chi = 0 on (-inf, 1/3] and chi = 1 on [2/3, inf).
2. Define K = chi(s) h(y) on N x [0,1]. Extend K to N x R by requiring K(y,s) = h(y) + K(f y, s-1).
3. The extension is smooth across the integers. Near s = 1 from the left, K = h(y). From the right, K = h(y) + chi(s-1) h(f y) = h(y), because chi(s-1) = 0 there. The same check works at every integer.
4. Then U = v (x) 1 + K is F-invariant: U(F(y,s)) = v(f y) + K(y,s) - h(y) = U(y,s).
5. Also d_s U = d_s K is smooth, and U is smooth iff v is smooth. ∎

Consequence: a positive-entropy GH diffeomorphism would give a counterexample to (PE). The obstructions carry over to diffeomorphisms verbatim. For example, a periodic point whose orbit has Jacobian product 1 gives a non-smooth v with v o f = v (a weighted sum of deltas over the orbit).

**Lemma R4 (invariances; recalled).** By (O4), GH is preserved under time changes hX with h > 0 smooth, under X -> -X, and under smooth conjugacy. Positivity of topological entropy is preserved by the same operations. For time changes, Abramov's formula h_{mu~} = h_mu / mu(1/h) applied to corresponding invariant measures, plus the variational principle (cited), gives this. So "time changes and smooth conjugates" of a non-counterexample are never counterexamples.

**Lemma R5 (volume-preserving flows; elementary).** Suppose X preserves a smooth positive density omega, so d = div_omega X = 0.
- Every periodic orbit has int_gamma d = 0, i.e. a Jacobian-1 Poincaré map. Every zero p has d(p) = 0.
- Hence, under GH, X has no zeros (P1) and no periodic orbits (Observation P, dim >= 2).
- Also, by (O2), GH forces unique ergodicity with measure omega, and minimality.

So a volume-preserving GH flow with positive entropy satisfies h_top = h_omega(g_1) > 0. By Ruelle's inequality and Katok's horseshoe theorem (Lian–Young for flows; cited), a hyperbolic omega would produce a horseshoe and therefore periodic orbits, which is excluded. So omega has a zero exponent transverse to the flow, and dim M >= 4. This is Corollary 4.3 of the background, re-derived here.

## 2. The suggested candidate classes

**(a) Products and theta-independent skew products alpha.d_theta + Y over Diophantine linear flows.** Corollary R2 reduces these to Y on a lower-dimensional manifold. They are not new counterexamples: one exists only if a lower-dimensional one does.

**(b) Time changes and smooth conjugates.** Lemma R4 shows they are never counterexamples unless the original flow is one.

**(c) Homogeneous flows g_t(Gamma x) = Gamma x exp(tX)** on compact Gamma\G, with Gamma a cocompact lattice and X in Lie(G).

Facts used:
- G is unimodular because it has a lattice, so Haar measure omega on Gamma\G is a smooth invariant volume.
- Entropy is positive iff ad X has an eigenvalue with nonzero real part (cited from memory: entropy of homogeneous flows equals the sum of the positive real parts of the eigenvalues of ad X).

By Lemma R5, GH would force the following:
- (i) unique ergodicity and minimality;
- (ii) no closed orbits, i.e. no gamma in Gamma conjugate in G into exp(RX), and X(x) != 0 always (X != 0);
- (iii) Haar measure is non-hyperbolic: besides X itself, ad X has a further generalized eigenvalue with zero real part.

Proved: a homogeneous flow with positive entropy is not GH if it has a closed orbit, or if the generalized eigenspace of ad X for eigenvalues with zero real part is just RX. The second case follows from Lemma R5 with Katok/Lian–Young.

Not proved here: the remaining case (partially hyperbolic X with a non-trivial central part, no closed orbits). There, GH reduces to excluding unique ergodicity of a partially hyperbolic homogeneous flow. I believe a theorem of this type is in the homogeneous-dynamics literature (Starkov's work on minimal and uniquely ergodic homogeneous flows), but I do not remember a precise statement, so I do not rely on it. The class is therefore not fully settled in this answer. It is, however, a very unlikely source of counterexamples, since such a flow would have to be uniquely ergodic.

**(d) Skew products over Diophantine linear flows with chaotic, theta-dependent fibre dynamics:** X = alpha.d_theta + Y(theta, y) on T^d x F.
- The base T^d is a smooth factor. By Lemma R1, GH of X implies GH of the base, which holds for Diophantine alpha, so there is no obstruction from the base.
- The Lyapunov spectrum of any invariant measure contains d zeros, coming from the base directions; they include the flow direction. So for d >= 2 every invariant measure is non-hyperbolic, and the Katok-horseshoe obstructions (Corollary 4.3, Theorem 4.1) do not apply.
- If the fibre flows preserve a smooth volume on F, X preserves one on T^d x F. By Lemma R5, GH then forces unique ergodicity and minimality of the skew product.
- Whether a positive-fibre-entropy skew product over a Diophantine flow can be uniquely ergodic, let alone GH, is not decided here.
- **This is the class I regard as the most serious candidate for a counterexample.** It is exactly the configuration left open by the structural theorem below (non-hyperbolic positive-entropy measures, dim >= 4). I could not prove GH for any member, nor exclude the class.

**(e) A dissipative saddle-type horseshoe embedded in an otherwise "elliptic" region.**
- In dimension 3, Theorem 4.1 of the background shows that this is the only possible configuration (H3).
- Every known necessary condition is compatible with it: periodic orbits all volume-contracting (for X or -X), a uniformly volume-contracting non-attracting horseshoe with nu-null stable set, nu ergodic and conservative, dense nu-typical orbits, and full support of every ergodic mu with mu(d) = 0.
- I found no construction proving GH for such a flow. Proving GH requires controlling every distributional solution near the horseshoe, and no technique I know does this outside the elliptic (Fourier) setting.
- I also found no argument excluding the class (Section 4).

**(f) Anosov flows.** These are excluded: by Prop 5.2 of [R5-e] (sketch) in general, and rigorously in the volume-preserving case (periodic orbits exist, plus Lemma R5).

## 3. Structural theorem for a counterexample (proved, modulo the cited classical theorems named)

**Theorem S.** Suppose X is GH on a compact connected M^n and h_top(g_1) > 0. Then all of the following hold.
1. n >= 3. For n = 1 every flow has zero entropy. For n = 2, flows on surfaces have zero topological entropy (Young's theorem; cited).
2. ker X on D' consists of the constants. X(C^inf) is closed with a tame inverse. nu is ergodic and conservative. There is no measurable time function, and no L^1 or BV solution of XW = kappa W with Re kappa != 0. (Background results L1, L2, Lemma 0/T, Theorem 1, Corollaries 2–3.)
3. Every zero p is non-resonant: tr A + alpha.lambda != 0 for every multi-index alpha (Lemma H), in particular d(p) != 0. No periodic orbit has Jacobian 1 (Observation P). There is no orbit with int e^{J_t} dt < inf (Lemma C), and there is no heteroclinic connection from a volume-expanding to a volume-contracting hyperbolic periodic orbit (Prop 4.0).
4. Every smooth factor of X (by a submersion) is GH (R1). If X = X1 (+) X2 is a product, then one factor is a lower-dimensional counterexample (R2). If X is a suspension of f with constant roof, then f is a positive-entropy GH diffeomorphism (R3).
5. (Volume case.) If X preserves a smooth volume omega, then:
   - the flow is uniquely ergodic and minimal, with no zeros and no periodic orbits;
   - h_omega = h_top > 0;
   - omega has a zero exponent transverse to the flow, so n >= 4 (R5).
6. (Hyperbolic case.) If some ergodic mu with h_mu > 0 has all non-flow exponents nonzero, then, for X or -X, there is a horseshoe Lambda != M with the following properties:
   - every periodic orbit in Lambda is volume-contracting;
   - J_t <= b - at on Lambda;
   - Lambda is not an attractor, and its stable set is nu-null.
   Moreover, every ergodic measure with mu(d) = 0 has full support (Theorem 4.1, Corollary 4.3, Corollary D1). For n = 3 this case always occurs.
7. There exist real kappa != 0 and a nonzero u in D' with Xu = kappa u ([R5-a]; no GH needed). Every such u is non-integrable. If u is a measure density, it is singular to nu.

Consequently, a minimal counterexample lies in one of two classes:
- (I) n >= 3, a dissipative non-attracting saddle horseshoe, in the configuration of item 6;
- (II) n >= 4, all positive-entropy measures non-hyperbolic, with transverse zero exponents. This class contains every volume-preserving counterexample.

The suggested classes (a), (b), (c, partly) and (f) are excluded. Classes (d) and (e) are the surviving templates of (II) and (I) respectively.

## 4. Attempts to reach a contradiction, and where they stop

**(i) Eigen-distributions of measure type.** If d = 0 (invariant volume) and T is a finite signed measure with T(X phi) = kappa T(phi), kappa real and nonzero, then T = 0.
*Proof.* The relation integrates to (g_t)_* T = e^{-kappa t} T. Comparing total variations, ||T|| = e^{-kappa t}||T|| for all t, so T = 0. ∎
This is trivial and does not reach the order-1 eigen-distributions T_kappa of [R5-a] Theorem B, which are what positive entropy actually produces. So (E1) for order >= 1 distributions remains the crux in the volume case.

**(ii) Class (I) via one-sided orbit integrals.** For x in W^s(Lambda), S(phi) = int_0^inf e^{J_t(x)} phi(g_t x) dt converges and solves a delta-source equation. Making the source smooth requires averaging over a set of positive volume, but W^s(Lambda) is nu-null (B3). With stopping times, Lemma 5.1 of [R5-d] shows that the Jacobian weights cancel, so this produces only smooth solutions or non-smooth sources. Dead end, for the reason already recorded in [R5-d].

**(iii) Class (II) via Pesin theory.** Zero transverse exponents block both Katok's horseshoe theorem and the uniform hyperbolic tools. Theorem B of [R5-a] still produces eigen-distributions, but they are of order 1 and are not excluded by any known GH consequence.

## 5. Verdict and open questions

- **No counterexample was found, and (PE) was not proved.** The new rigorous content here is: the factor, product and suspension reductions (R1–R3); the invariance of both properties under time change (R4); the volume-case consolidation (R5); the exclusion of products, time changes, Anosov flows and part of the homogeneous class; and the dichotomy (I)/(II) for a minimal counterexample.
- Open question Q1: is (E1) true? That is, under GH, is there no nonzero distribution u with Xu = kappa u for real kappa != 0? By [R5-a], a positive answer would give lambda* = 0 and hence (PE).
- Open question Q2 (class (II), volume case): can a C^inf flow be uniquely ergodic with a smooth invariant volume of positive entropy that has zero transverse exponents, as in a skew product over a Diophantine flow? If so, is it ever GH?
- Open question Q3 (class (I)): can a GH flow contain a uniformly volume-contracting, non-attracting saddle horseshoe?
- Open question Q4: are partially hyperbolic homogeneous flows with a non-trivial central part never uniquely ergodic? A positive answer would complete the exclusion of class (c).

=== END OF ANSWER round6_q4 ===
