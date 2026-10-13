# round7_q8: answer

Plan. Part 1: check that (PE-NH), together with the listed results, gives the problem's claim. Part 2: a first move not on the excluded list. I use **functional analysis of GH itself**: the closed graph theorem gives a tame a priori estimate. From it I get that the range of X on C^inf is closed, the dual (Hahn–Banach) solvability of L_X S = T, and uniformly bounded Birkhoff integrals on the space of coboundaries. Testing GH on **indicator functions of invariant Borel sets** shows that the Lebesgue class is ergodic. Then I see what these facts say about (PE-NH).

Status. Part 1 is done. In Part 2, Lemmas A–F are proved. (PE-NH) is NOT proved. In the case where X preserves a smooth volume, these lemmas reduce (PE-NH) to a statement of Katok-conjecture type, which I could not prove.

---

## Part 1. (PE-NH) plus the listed results imply the claim

**The derivation.** Suppose h_top(g_1) > 0.

1. By the Variational step there is an ergodic flow-invariant mu with h_mu(g_1) > 0.
2. If dim M <= 3, the dimension-<=3 result already gives a contradiction. So let dim M >= 2 in what follows (dim M = 1 is covered by the same result).
3. By the third listed result (positive entropy implies non-hyperbolic), mu has a zero Lyapunov exponent transverse to X.
4. mu is not a Dirac mass at a zero of X, because such a measure has entropy 0. So X != 0 mu-a.e., and the flow direction carries one exponent 0.
5. Together with step 3, the exponent 0 of g_1 has multiplicity >= 2. That is exactly (a) and (b) of (PE-NH), so (PE-NH) gives a contradiction.

Hence h_top(g_1) = 0. Since h_top(g_t) = |t| h_top(g_1), the whole flow has zero topological entropy. The derivation goes through and is immediate.

**Comments.**
- The derivation does not use the mu(d)-band result. That result only narrows the cases (PE-NH) has to handle.
- Conversely, the problem's claim implies (PE-NH): zero topological entropy rules out every mu with h_mu > 0. So, given the listed results, **(PE-NH) is equivalent to the problem**. It is exactly as plausible as the problem, and it carries all of the difficulty, namely the non-hyperbolic case where Katok/Lian–Young horseshoes are unavailable.
- (PE-NH) is not implausible. It is necessary for the claim, and by the dimension-<=3 result it holds when dim M <= 3. But it should not be expected to follow from "soft" properties alone. Smooth minimal flows and diffeomorphisms with positive entropy, built by Herman-type constructions (cited from memory), show that minimality or transitivity cannot be enough. Any proof must use the smoothness gain in GH.

---

## Part 2. First move: closed graph, closed range and duality, plus invariant indicator functions

Notation. nu is a smooth positive density, normalised so that nu(M) = 1. "Distribution" means generalized function, paired with smooth densities. A "distributional density" is an element of (C^inf)'. We write:
- I = { T in (C^inf)' : T(X phi) = 0 for all phi }, the invariant distributional densities. Every invariant Borel probability measure lies in I.
- R = X(C^inf).

### Lemma A (tame a priori estimate). Under GH, for every k >= 1 there exist m and C such that ||u||_{C^k} <= C ||Xu||_{C^m} for every smooth u with int u dnu = 0.

*Proof.*
1. Let E = { u in L^2(nu) : Xu in C^inf (in D') }. Give E the seminorms ||u||_{L^2} and ||Xu||_{C^j}, j >= 0.
2. E is Fréchet. If (u_n) is Cauchy, then u_n -> u in L^2 and Xu_n -> f in C^inf. Since Xu_n -> Xu in D', we get Xu = f.
3. By GH, E is contained in C^inf. The inclusion E -> C^inf has closed graph, because both spaces inject continuously into D'. By the closed graph theorem it is continuous. So for each k there are m, C with ||u||_{C^k} <= C(||u||_{L^2} + ||Xu||_{C^m}).
4. To remove the L^2 term, argue by contradiction. Suppose there are mean-zero smooth u_n with ||u_n||_{C^k} > n ||Xu_n||_{C^m}. Rescale so that ||u_n||_{L^2} = 1. Then ||u_n||_{C^k} <= C(1 + ||u_n||_{C^k}/n), so ||u_n||_{C^k} <= 2C once n >= 2C.
5. Hence ||Xu_n||_{C^m} -> 0. Because k >= 1, Arzelà–Ascoli gives a subsequence u_n -> u in C^0. This u has mean 0, ||u||_{L^2} = 1 and Xu = 0 in D'.
6. By (L1), u is constant, so u = 0. This contradicts ||u||_{L^2} = 1. ∎

### Lemma B (closed range and duality). Under GH:
1. R is closed in C^inf, and R = { f : T(f) = 0 for all T in I }.
2. For f in R, the unique mean-zero solution u = X^{-1} f satisfies ||u||_{C^k} <= C_k ||f||_{C^{m(k)}}.
3. For every T in (C^k)' with T(1) = 0, there is S in (C^{m(k)})' with S(X phi) = T(phi) for all phi, and ||S|| <= C_k ||T||.

*Proof.*
- (i) Take Xu_n -> f in C^inf with u_n of mean zero. Lemma A for every k shows (u_n) is Cauchy in C^inf. Its limit u satisfies Xu = f. The description of R then follows from Hahn–Banach, since R is closed.
- (ii) This is Lemma A.
- (iii) Put S(X phi) := T(phi - nu(phi)) = T(phi). This is well defined because ker X = constants and T(1) = 0. Moreover |S(X phi)| <= ||T|| ||phi - nu(phi)||_{C^k} <= C ||T|| ||X phi||_{C^m}. Extend S to C^m by Hahn–Banach. ∎

In particular, for any two points p, q there is a current S_{pq} of order <= m(0) with uniformly bounded norm such that S_{pq}(X phi) = phi(p) - phi(q).

### Lemma C (bounded Birkhoff integrals). For f in R: sup_{p, t} |int_0^t f(g_s p) ds| <= 2 C_0 ||f||_{C^{m(0)}}.

*Proof.* With u = X^{-1} f, the integral equals u(g_t p) - u(p). ∎

### Lemma D (the Lebesgue class is ergodic). Under GH, every Borel set B with nu(g_t B Δ B) = 0 for all t is nu-null or nu-conull.

*Proof.*
- For a smooth density omega, int_B L_X omega = d/dt|_0 int_B g_t^* omega = d/dt|_0 int_{g_t B} omega = 0. Differentiating under the integral is allowed because g_t^* omega is C^1 in t, uniformly on M.
- So X 1_B = 0 in D'. By (L1), 1_B is a.e. constant. ∎

**Corollaries of Lemma D.**
1. Every nonempty open invariant set is conull. Every proper closed invariant set is nu-null.
2. nu-a.e. orbit is dense. Apply (1) to the saturations of a countable base.
3. If dim M >= 2, the flow is conservative for nu. Sketch, quoting the Hopf decomposition from memory: the dissipative part is invariant, so it is null or conull. If it were conull, ergodicity would force nu to sit on a single orbit, and an orbit is Lebesgue-null when n >= 2.
4. (Cesàro statement.) For w in L^inf, every weak-* limit point of A_T w = (1/T) int_0^T w∘g_s ds is invariant and hence constant.
   - Invariance holds because ||(A_T w)∘g_r - A_T w||_inf <= 2|r| ||w||_inf / T.
   - Hence, for every mean-zero rho in L^1(nu), the Cesàro averages of the transfer operator applied to rho tend to 0 weakly in L^1. By the Yosida–Kakutani mean ergodic theorem (cited from memory) they tend to 0 in norm.
   - So all absolutely continuous probability measures have the same Cesàro push-forward asymptotics.

### Lemma E (absolutely continuous invariant measures). If mu = h nu is flow-invariant with h > 0 a.e. and log h in L^1, then h is smooth. So mu is a smooth invariant volume.

*Proof.*
- Invariance gives log h∘g_t - log h = -J_t a.e. for each t.
- Pair with a test density, divide by t and let t -> 0. Since J_t / t -> d uniformly, this gives X(log h) = -d in D'.
- By GH, log h is smooth. ∎

### Lemma F (the volume-preserving case). Suppose d is in R, i.e. d = -X psi with psi smooth. Equivalently, by Lemma B, T(d) = 0 for every T in I. Then nu' = e^{psi} nu is invariant, and:
1. I = R nu', so the flow is **uniquely ergodic** and **minimal**.
2. R = { f : nu'(f) = 0 }. So **every** mean-zero smooth f is a smooth coboundary with the tame bounds of Lemma B. This is Katok's "cohomological C^inf-stability".
3. There are m, C such that for all p, t and smooth f: |int_0^t f(g_s p) ds - t nu'(f)| <= C ||f||_{C^m}.
4. Consequently, every orbit segment of length >= C' eps^{-(m+n)} meets every eps-ball, where n = dim M.

*Proof.*
1. div_{nu'} X = d + X psi = 0. Write T in I as T(phi) = u(phi nu') with u a generalized function. Then T(X phi) = u(L_X(phi nu')) = -(Xu)(phi nu'). So T is in I iff Xu = 0, which by (L1) means u is constant.
   - Unique ergodicity follows.
   - Minimality: every orbit closure supports an invariant measure, which must be nu'. Since nu' has full support, every orbit closure is M.
2. This is Lemma B(i) combined with (1).
3. Apply Lemma C to f - nu'(f).
4. Apply (3) to a bump f of height 1 and radius eps. Then nu'(f) is of order eps^n and ||f||_{C^m} is of order eps^{-m}. ∎

### What this first move gives for (PE-NH), and where it stops

- **Volume-preserving case.** If d is a coboundary (for instance when X preserves a smooth volume), Lemma F reduces (PE-NH) to the following statement.
  - (*) A C^inf flow cannot have positive entropy if it is minimal and uniquely ergodic with a smooth measure nu', and every mean-zero smooth function is a smooth coboundary with the tame bounds of Lemmas B and C.
  - The non-hyperbolic case of (*) is exactly what remains, since in the hyperbolic case Katok's periodic orbits contradict unique ergodicity.
  - I could not prove (*). Spectral arguments are insufficient. Positive entropy gives countable Lebesgue spectrum on the Pinsker complement. The coboundary property only forces spectral measures of smooth functions to vanish to infinite order at 0 (f = X^k u_k for all k). That is compatible with Lebesgue spectrum, because such vectors are dense in the Pinsker complement.
- **Leaf-cycle variant.** Let x_0, ..., x_{2k} be a closed stable/unstable cycle that closes up to a flow segment. Then the regularized alternating sum of full-orbit "measures" lies in I. In the volume case this sum must therefore be c nu', and testing on 1 gives c = 0.
  - Test it on an eps-bump at a generic vertex x_1. The passage of x_1 through the bump at time 0 contributes about eps. Partner orbits contribute only through returns within time O(log(1/eps)), which do not occur for generic vertices. So the sum is nonzero, a contradiction.
  - Hence: **in the volume case, under GH, no closed s/u-cycle (closing up to a flow segment) passes through generic points of mu.** The step "generic vertices do not return to the bump within time O(log 1/eps)" is only sketched.
  - For hyperbolic mu such cycles exist by local product structure. For non-hyperbolic mu, center directions block local product structure, so existence of cycles is precisely the open point.
  - This is close in spirit to the excluded "Dirac masses on leaves" move. I report it only as a by-product.
- **General (non-volume) case.** Lemmas A–E still hold. But I may contain elements that are not measures, and nothing here controls them or the class [d] in C^inf / R. Note that d is in R exactly when T(d) = 0 for all T in I (Lemma B). So "every T in I kills d" would reduce the general case to the volume case. I could not prove it. By the mu(d)-band result, mu(d) = 0 is one allowed value for a positive-entropy measure, so even the measures in I are not controlled.

### Open questions left by this move
1. **(PE-NH) itself** (equivalently, the problem) in dim M >= 4: open here.
2. **Does GH imply that d is in R?** That is, does every invariant distributional density annihilate div_nu X? This is equivalent, by Lemma B, to X preserving a smooth volume. Lemma E gives it whenever an invariant measure h nu exists with log h in L^1.
3. **Is dim I finite under GH?** Equivalently, is R of finite codimension?
4. **Statement (*)** (zero entropy of cohomologically C^inf-stable, uniquely ergodic, smooth-volume flows). To my knowledge this is a case of Katok's conjecture and is not settled in general (cited from memory). The Rodriguez Hertz–Rodriguez Hertz theorem on a torus factor of dimension b_1 for cohomology-free systems, as I recall it, does not give it.
5. **Existence, for a non-hyperbolic positive-entropy measure, of closed s/u-cycles closing up to a flow segment through generic points.** A positive answer would settle the volume case via the cycle argument.

=== END OF ANSWER round7_q8 ===
