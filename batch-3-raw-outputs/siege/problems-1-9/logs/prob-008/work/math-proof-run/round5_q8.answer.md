# round5_q8: answer

## Plan and status

**Target.** (Lambda): under global hypoellipticity (GH), lambda* = lim (1/t) log max_x ||Dg_t(x)|| = 0. Alternatively, zero topological entropy directly.

**Outcome.** I did NOT prove (Lambda), and I did not prove zero entropy. What this file contains:

- **(A) A new theorem, proved below as Theorem 1.** GH excludes every *measurable* solution of a cocycle equation XV = -b in which b has nonzero integral against every invariant probability measure.
  - Consequence: GH excludes nonzero *L^1 eigenfunctions* XW = -kappa W with Re kappa != 0 (Corollary 2). This proves the planner's statement (E1) in the class of L^1 functions. In that class it was open before.
  - Consequence: GH excludes nonzero finite-mass closed (n-1)-currents C with C(L_X beta) = s C(beta), s real, s != 0 (Corollary 3).
- **(B) Two flaws in the planner's sketch, each with proof.**
  - (B1) Step (c) is wrong for n >= 3. A closed 1-current that vanishes on closed forms is the boundary of an (n-2)-current. It is not dW for a generalized function W.
  - (B2) The repaired version, using hypersurface ((n-1)-)currents, does lead to functions W, but its Patterson limits are provably ZERO. So that route can never produce the eigen-object.
- **(C) A remark: (Lambda) is strictly stronger than the problem.** (Lambda) contains the open statement "GH excludes zeros of X having an eigenvalue with positive real part". A zero-entropy proof does not need that.
- **(D) A conditional partial result.** In dimension 3, under GH plus a smooth invariant volume, the entropy is zero. The proof cites Katok's horseshoe/closing theory from memory.

Conventions are those of the brief:
- nu is a smooth positive density.
- d = div_nu X, and J_t(x) = int_0^t d(g_r x) dr.
- A distribution u pairs with smooth densities rho. The derivative Xu is defined by <Xu, rho> = -<u, L_X rho>.
- L1 is the result of the brief: GH implies that every u in D' with Xu = 0 is constant.

Throughout, dim M = n >= 2. (For n = 1 the entropy is trivially 0.)

---

## (A) Measurable cocycles and eigenfunctions

### Lemma 0 (transport identity).
Let W be a distribution with XW = -kappa W (kappa in C). Then W o g_t = e^{-kappa t} W in D' for every t. Here (W o g_t)(rho) := W((g_t)_* rho).

*Proof.*
1. For a smooth density rho, the map t -> (g_t)_* rho is a smooth curve in the smooth densities, with derivative -L_X (g_t)_* rho.
2. Let f(t) = <W, (g_t)_* rho>. Then f'(t) = -<W, L_X (g_t)_* rho> = <XW, (g_t)_* rho> = -kappa f(t).
3. Hence f(t) = e^{-kappa t} f(0). ∎

When W is in L^1(nu), the conclusion says W(g_t x) = e^{-kappa t} W(x) for nu-a.e. x, for each fixed t.

The same computation applies to an L^infinity function u with u o g_t = u a.e. for each t. Then <u, L_X rho> = -d/dt|_0 int (u o g_t) rho = 0, so Xu = 0 in D'. This fact is used below and called (*).

### Theorem 1 (proved).
Assume GH and n >= 2. Let b be a continuous real function such that mu(b) != 0 for every invariant Borel probability mu. Write B_t(x) = int_0^t b(g_r x) dr.

Then there is no Borel function V: M -> R such that, for each t in R, V(g_t x) = V(x) - B_t(x) for nu-a.e. x.

*Proof.*

**Step 1 (constant sign).** The set of invariant probabilities is convex and weak* compact. The map mu -> mu(b) is affine and continuous, so it has constant sign. Replacing (V, b) by (-V, -b) if necessary, assume mu(b) > 0 for all mu.

**Step 2 (uniform growth).** There are T0 > 0 and c > 0 with B_T(x) >= cT for all x and all T >= T0.

Suppose not. Then there are T_k -> infinity and points x_k with B_{T_k}(x_k) <= T_k/k. Take a weak* limit point mu of the empirical measures (1/T_k) int_0^{T_k} delta_{g_r x_k} dr. It is invariant and mu(b) <= 0, a contradiction.

**Step 3 (positive cohomologous function).** Fix T >= T0. Put b' = B_T/T, which is continuous with b' >= c > 0. Put w = (1/T) int_0^T B_r dr, which is continuous. Since B_r(g_s x) = B_{r+s}(x) - B_s(x), the function s -> w(g_s x) is C^1 with derivative (b' - b)(g_s x). Hence w o g_t - w = B'_t - B_t, where B'_t = int_0^t b' o g_r.

Set V' = V - w. Then V' o g_t = V' - B'_t a.e., for each t.

**Step 4 (measurable section).** Fix x. The map s -> B'_s(x) is a strictly increasing homeomorphism of R onto R: it is >= cs for s >= 0 and <= cs for s <= 0. Let theta(x) be the unique s with B'_s(x) = V'(x). Then theta(x) = sup{s in Q : B'_s(x) < V'(x)}, so theta is Borel.

Put pi(x) = g_{theta(x)}(x), which is Borel.

Fix t, and take x with V'(g_t x) = V'(x) - B'_t(x); this holds for a.e. x. Using B'_s(g_t x) = B'_{s+t}(x) - B'_t(x), the number theta(g_t x) is the s solving B'_{s+t}(x) = V'(x). So theta(g_t x) = theta(x) - t, and therefore pi(g_t x) = pi(x).

Thus for each t, pi o g_t = pi nu-a.e.

**Step 5 (contradiction with L1).** Let psi be continuous on M and put u = psi o pi, which is in L^infinity. By Step 4, u o g_t = u a.e. for each t. By (*), Xu = 0, so by L1, u is a.e. equal to a constant c_psi.

Take a countable family {psi_j} that separates points. Then for a.e. x, pi(x) is the same point p. So a.e. x equals g_{-theta(x)}(p), which lies on the orbit of p.

That orbit is the image of R under a C^1 map, hence nu-null since n >= 2. This contradicts nu(M) > 0. ∎

### Corollary 2 (E1 for L^1 functions; proved).
Assume GH and n >= 2. If W is in L^1(nu), complex valued, with XW = -kappa W in D' and Re kappa != 0, then W = 0.

*Proof.*
1. By Lemma 0, W o g_t = e^{-kappa t} W a.e., for each t.
2. Let A = {W != 0}. Then 1_A o g_t = 1_A a.e., so X 1_A = 0 by (*). By L1, either nu(A) = 0 (and we are done) or A is conull.
3. In the second case, V = log|W| is a.e. finite and satisfies V o g_t = V - (Re kappa) t a.e.
4. Apply Theorem 1 with b ≡ Re kappa; then mu(b) = Re kappa != 0 for every mu. This gives a contradiction. ∎

**Remark 2'.**
- Same proof, using the variable-multiplier version of Lemma 0: there is no nonzero W in L^1 with L_X(W nu) = -s W nu (s real) whenever -s lies outside [min_mu mu(d), max_mu mu(d)]. Here b = s + d.
- That interval contains 0 by Prop 2.1 of the brief.
- Singular eigenmeasures are not excluded. These are the tilted conformal measures of [R4-q7] Prop 2.2, and they exist. Theorem 1 needs nu-measurable objects, because L1 is a statement about distributions.

### Corollary 3 (proved; M orientable, or pass to the orientation double cover).
Under GH, there is no nonzero closed (n-1)-current C of finite mass with C(L_X beta) = s C(beta) for all smooth (n-1)-forms beta, with s real and s != 0.

*Proof.*
1. Write C(beta) = int beta ∧ Ĉ, where Ĉ is a 1-form with measure coefficients.
2. Closedness: 0 = C(d eta) = ± int eta ∧ dĈ for all eta, so dĈ = 0.
3. The eigen-relation: int L_X beta ∧ Ĉ = -int beta ∧ L_X Ĉ. So L_X Ĉ = -s Ĉ.
4. de Rham–Hodge for currents (cited) gives Ĉ = h + dW, with h a smooth harmonic form and W in D'.
5. Cartan: L_X Ĉ = d(i_X Ĉ). Hence s h = -d(i_X Ĉ + sW) is exact and harmonic, so h = 0.
6. Then d(XW + sW) = 0, so XW + sW is a constant c. Replace W by W - c/s; now XW = -sW, and Ĉ = dW.
7. A distribution whose differential is a finite measure is a BV function (cited, standard). So W is in L^1. By Corollary 2, W = 0, hence C = 0. ∎

---

## (B) The planner's eigen-current sketch

### (B1) Step (c) is wrong for n >= 3.
A closed 1-current C corresponds, by Poincaré duality, to a closed (n-1)-form-current Ĉ. If C vanishes on closed 1-forms, the duality pairing gives that Ĉ is exact: Ĉ = d Theta, where Theta is an (n-2)-current. Theta is a generalized function only when n = 2.

So the curve-current limit gives an (n-2)-current Theta with L_X Theta = -s0 Theta + (closed). That is not a scalar equation, and neither GH nor Theorem 1 applies to it.

### (B2) The hypersurface version produces only C = 0.
The scalar version needs (n-1)-currents, as in Corollary 3. Take a closed hypersurface S = ∂B (or a smooth closed (n-1)-form). Form the Patterson currents C^s(beta) = Z(s)^{-1} int_0^infinity e^{-st} (int_{g_t S} beta) dt, where Z(s) -> infinity as s decreases to s0 > 0.

Then C^s(beta) = Z(s)^{-1} int e^{-st} int_{g_t B} d beta dt, and so

|C^s(beta)| <= ||d beta||_infinity vol(M) / (s Z(s)) -> 0.

The same estimate holds for the forms g_t^* d phi, whose normalised primitives are bounded by ||phi||_infinity. So every such limit is 0, in agreement with Corollary 3. In particular the cancellation problem (N) of the sketch is forced, not accidental, for hypersurfaces and exact forms.

The only data that still have nonzero limits are non-closed objects such as curves. Those lead to (n-2)-currents (B1), or to sphere-bundle measures (the Krein–Rutman T_S, which is the divergence of a vector-valued measure, not an L^1 function).

---

## (C) (Lambda) is strictly stronger than the problem

Let p be a zero of X and A = DX(p). Then lambda* >= max Re spec(A).

What is known under GH:
- tr A != 0 (P1 of the brief);
- the zero is non-resonant (Lemma H of the brief).

Neither excludes a saddle-type zero, which has an eigenvalue with positive real part. Such a zero gives lambda* > 0 without any entropy.

So (Lambda) contains the unresolved statement "GH excludes zeros with an eigenvalue of positive real part", while zero entropy does not need it. Step 2 of the chain (h_top(g_1) <= (n/T) log^+ max ||Dg_T||) is itself correct; only the target is stronger than necessary.

---

## (D) Partial result: n = 3, GH plus a smooth invariant volume omega

*Claim.* The flow has zero topological entropy.

*Argument* (uses results cited from memory):
1. By (O2), the flow is uniquely ergodic with invariant measure omega, and X has no zeros and no periodic orbits.
2. If h_top > 0, the variational principle gives h_omega > 0.
3. The Ruelle inequality, applied to g_1 and to g_{-1}, gives one positive and one negative exponent. Together with the zero exponent of the flow direction, omega is hyperbolic.
4. Katok's closing lemma / horseshoe theorem for C^{1+alpha} flows with a hyperbolic measure of positive entropy (cited from memory) gives periodic orbits.
5. This contradicts step 1.

This covers only some vector fields, so it is not an answer to the question.

---

## What is proved, and what remains open

**Proved:**
- Theorem 1, Corollaries 2 and 3, and Remark 2'.
- (B1) and (B2).
- Remark (C).

**Conditional / cited:** (D).

**Open:**
1. (Lambda) itself, and zero entropy directly.
2. E1 for eigen-distributions that are not L^1 functions. The relevant cases are order >= 1 (e.g. the Krein–Rutman T_S, with T_S(phi o g_t) = e^{lambda* t} T_S(phi)) and singular measures. Theorem 1 handles only nu-measurable objects.
3. A mechanism that converts exponential growth of derivatives (lambda* > 0, or growth of int ||Λ Dg_t|| d nu, via Przytycki's inequality) into a nu-measurable scalar cocycle or an L^1 eigenfunction. Scalar cocycles on M (J_t, Birkhoff integrals) do not see derivative growth. The objects that do see it (tangent-bundle and form-valued) are not scalar, and GH says nothing about the lifted field on the sphere bundle.
4. Under the quantitative approach the task asked for, every test family I tried loses: Xu_T costs e^{m lambda* T} in C^m, while u_T gains only e^{k lambda* T} in C^k. I found no test function that reverses this.

=== END OF ANSWER round5_q8 ===
