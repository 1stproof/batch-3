# round9_q7 — answer

## Summary of outcome
(EF) is **not** proved here, and I give no counterexample. What the file does establish:
- **Proposition B1.** The Leibniz family V_{z,phi} carries no information beyond (iii) itself.
- **Proposition B2.** The choice phi = e^w (idea (a)) is exactly a change of the reference density nu -> e^w nu. (EF) is invariant under such changes, so idea (a) gives nothing new. In the volume case it only reproduces the normalisation P = X.
- **Proposition B3.** Multiplication by a C^2 function phi can move the eigenvalue of an eigen-density, z -> z - c, only if X phi = c phi on the support K of the eigen-density. When Re c != 0 this forces phi = 0 on K. So weighted multipliers can never move a family horizontally: they cannot shift a strip so that it contains 0 (idea (d)). For the unweighted coupling (P phi = c phi on K) only a weaker necessary condition is proved, (d1)/(d2), and any such multiplier would lead to the unweighted situation, which needs (V).
- **Proposition B4.** In the volume-preserving case the two operators coincide (P = X), so the coupling is vacuous. For the families the problem produces, (EF) in this case reduces exactly to the Theorem V / Lemma Q situation of rounds 7–8. Also, in the volume case GH is equivalent to "DUE + closed range" (Katok's cohomology-free property).
- **Conclusion.** Approach (B) is a dead end in all four of the forms (a)–(d) listed in the brief. The precise point where it stops is Proposition B3 together with B4.
- I re-checked the chain (steps 1–3). I found no flaw: Theorem R and the variational step are as stated, modulo the cited Pesin/Ledrappier–Young theory.

Notation is as in the brief: nu is a smooth positive density, d = div_nu X, P = X + d, u_z = T_z/nu, and L_t phi = e^{J_t} (phi o g_t). Recall T(L_t phi) = e^{zt} T(phi) whenever T o P = zT (Lemma 1.1 of R8-b).

---

## B1. The Leibniz identities are equivalent to (iii)

**Proposition B1.** Let T be a distribution density of order <= 1 and z in C. The following are equivalent.
(1) T(P psi) = z T(psi) for all smooth psi.
(2) For all smooth phi and psi, V_phi(X psi) = z V_phi(psi) - T((P phi) psi), where V_phi := T(phi ·).
(2') For all smooth phi and psi, V_phi(P psi) = z V_phi(psi) - T((X phi) psi).

*Proof.* The product rules are P(phi psi) = (P phi) psi + phi X psi = (X phi) psi + phi P psi.
- (1) => (2): T(phi X psi) = T(P(phi psi)) - T((P phi) psi) = z T(phi psi) - T((P phi) psi).
- (1) => (2'): the same argument with the second product rule.
- (2) => (1): take phi = 1. Then P1 = d, and (2) reads T(X psi) = z T(psi) - T(d psi), which is (1).
- (2') => (1): take phi = 1. Then X1 = 0, and (2') is (1). ∎

So the coupling is a reformulation. Any proof built on it must bring in an extra estimate or structure that depends on phi. The rest of this answer examines the candidates.

## B2. phi = e^w is a change of reference density (idea (a))

**Proposition B2.** Let w be smooth (real or complex), nu' := e^w nu, d' := div_{nu'} X = d + Xw and P' := X + d'. Then V := T_z(e^w ·) satisfies V o P' = z V. The map T -> T(e^w ·) is an order-preserving bijection between the eigen-families for (nu, P) and for (nu', P'). It preserves (i), (ii) and (iii).

*Proof.* P'psi = Xpsi + d psi + (Xw) psi, and e^w P' psi = X(e^w psi) + d e^w psi = P(e^w psi). So V(P' psi) = T_z(P(e^w psi)) = z T_z(e^w psi) = z V(psi). The inverse map is T -> T(e^{-w} ·). Multiplication by e^{±w} is a topological automorphism of C^1 and of C^inf. ∎

*Consequence.* Choosing phi = e^w with Xw ≈ -d means working with a reference density whose divergence d + Xw is small. Two cases arise.
- If d + Xw is constant, then (O3) says e^w nu is invariant, the constant is 0, and P' = X: this is the volume case (B4).
- Otherwise the residual d' = d + Xw cannot be made small in every C^k. By (O3) and closed range, d is not in R + X(C^inf), which is a closed subspace. So the error term T_z((P e^w) psi) = V(d' psi) is not small in any norm that the tame inverse R can absorb (R loses derivatives, Lemma A of R7-d).

So idea (a) either reduces to the volume case or produces an error term of fixed size. In neither case does it combine with R.

## B3. Multipliers cannot move the eigenvalue horizontally

This is the structural reason why (b) and (d) fail. A multiplier changes the eigen-parameter only through an eigenfunction relation for X, and that relation forces the multiplier to vanish wherever the eigen-density lives.

**Lemma B3.0 (support).** Let T != 0 be a distribution density with T o P = zT, and let K := supp T. Then K is a nonempty closed flow-invariant set.

*Proof.*
- Suppose psi is smooth with supp psi ∩ K = ∅. Then L_t psi = e^{J_t} psi o g_t is supported in g_{-t}(supp psi).
- So T(L_t psi) = e^{zt} T(psi) = 0, i.e. T vanishes on all smooth functions supported in g_{-t}(M \ K), for every t.
- Hence g_{-t}(M \ K) ⊂ M \ K for all t, so K is invariant. ∎

**Lemma B3.1 (division).** Let T be a distribution density of order <= 1, f in C^1(M) and K = supp T. Suppose T(f psi) = 0 for all smooth psi. Then f = 0 on K.

*Proof.*
- Suppose f(x0) != 0 for some x0 in K. Choose a neighbourhood U of x0 on which f != 0. There 1/f is C^1.
- For smooth psi supported in U, psi/f is C^1 with compact support in U, and T(psi) = T(f · (psi/f)) = 0. The last equality holds by continuity of T on C^1 and density of smooth functions in C^1.
- So x0 is not in supp T, a contradiction. ∎

**Lemma B3.2 (no bounded multiplier with real growth).** Let K be a closed invariant set, phi continuous and C^1 along orbits, and c in C with Re c != 0. Suppose X phi = c phi on K. Then phi = 0 on K.

*Proof.* For x in K, s -> phi(g_s x) solves y' = c y. So |phi(g_s x)| = e^{(Re c) s} |phi(x)|. The left side is bounded by ||phi||_inf for all s in R. Letting s -> +inf or s -> -inf, according to the sign of Re c, gives phi(x) = 0. ∎

**Proposition B3.** Let T_z != 0 be an order-<=1 eigen-density, T_z o P = z T_z, with support K. Let phi be in C^2 and c in C, and put V := T_z(phi ·).
(a) V o P = (z - c) V holds iff T_z((X phi - c phi) psi) = 0 for all psi. In that case X phi = c phi on K.
(b) V o X = (z - c) V holds iff T_z((P phi - c phi) psi) = 0 for all psi. In that case P phi = c phi on K.
(c) In case (a) with Re c != 0: phi = 0 on K. In particular, if K = M then phi = 0 and V = 0.
(d) In case (b) with Re c != 0:
 (d1) if K = M, phi has no zeros;
 (d2) for general K: every x in K with phi(x) != 0 has an orbit closure carrying flow-invariant probabilities mu_+ and mu_- with mu_+(d) >= Re c >= mu_-(d).
 In particular, (d1) is impossible.

*Proof.*
(a), (b) The equivalences are Proposition B1 with the eigenvalue moved: V(P psi) = z V(psi) - T_z((X phi) psi), and V(X psi) = z V(psi) - T_z((P phi) psi). The conclusion on K follows from Lemma B3.1 with f = X phi - c phi (resp. P phi - c phi), which is C^1.
(c) This is Lemma B3.2 applied on the invariant set K (Lemma B3.0).
(d) On K we have X phi = (c - d) phi, so for x in K, |phi(g_s x)| = |phi(x)| exp((Re c) s - J_s(x)).
- (d2) Suppose phi(x) != 0. Boundedness of phi gives (Re c) s - J_s(x) <= C' for all real s.
  - For s -> +inf, J_s(x)/s >= Re c - C'/s. So every weak* limit mu_+ of (1/s) int_0^s delta_{g_r x} dr (an invariant probability on the orbit closure, which lies in K) has mu_+(d) >= Re c.
  - For s -> -inf, the backward empirical measures (1/|s|) int_s^0 delta_{g_r x} dr have d-average -J_s(x)/|s| <= Re c + C'/|s|. So their limits mu_- satisfy mu_-(d) <= Re c.
- (d1) If K = M and phi has no zeros, log|phi| is smooth with X log|phi| = Re c - d. So d lies in R + X(C^inf), and (O3) forces the constant to vanish: Re c = 0, a contradiction. ∎

*Remark (what is rigorous in B3).* Everything stated in B3 is proved. For the weighted form (a) the conclusion is complete: phi vanishes on K. For the brief's unweighted form (b) the conclusion is weaker:
- with full support and no zeros, a shift is impossible (d1);
- in general, the multiplier can be nonzero only at points whose orbit closures carry invariant measures with mu(d) on both sides of Re c (d2).
This weaker form is natural: tilted conformal measures (Prop. 2.2 of R4-q7) show that eigen-objects with real eigenvalue mu(d) do exist, so soft arguments cannot exclude such multipliers on small invariant sets. Whether a C^2 phi with P phi = c phi on supp T_z (Re c = Re z) can exist for the families of Theorem R is not settled here. If one did exist, the unweighted coupling would turn T_z into an X-transpose eigen-family near 0. Excluding a family of that kind would still require dim I = 1 (Observation 2.1 of R8-e), i.e. (V).

**What B3 means for the approach.**
- *Idea (d) (build a family holomorphic through 0 from V_{z,phi}).* This requires V_{z,phi} o P = (z - c)V with Re(z - c) = 0, i.e. Re c = Re z != 0 throughout the strip. By B3(a) the multiplier vanishes on supp T_z. So the only C^2 multipliers that move a strip horizontally are those that kill the family on its support. For the families of Theorem R in the case lambda = 0, the support is contained in supp mu, which is M under GH (Corollary D1). If supp T_z = M, the multiplier is 0.
- *Idea (b) (vary phi to show T_z vanishes on products).* By B1, T_z(phi psi) for all phi, psi is just T_z on C^inf. There is no smaller set of products to exploit unless phi satisfies an eigen-relation, and B3 excludes that horizontally.
- *Idea (c) (Jordan chains).* Differentiating (2) in z gives V'_{z,phi}(X psi) = z V'(psi) + V(psi) - T'_z((P phi) psi). These are again the Leibniz identities for the Taylor coefficients of T, so B1 applies to each coefficient. Pairing with R gives exactly the iteration T_z(phi) = z^N T_z(R^N phi_0) of Theorem V / Lemma Q, and only in the volume case (Proposition A of R8-d).
- *Imaginary shifts.* When Re c = 0 a nonvanishing smooth multiplier with X phi = c phi may exist (a circle-valued eigenfunction, e.g. a torus factor). It moves the family vertically, which is harmless and useless.

## B4. The volume case: the coupling is vacuous, and what (EF) means there

Assume GH and a smooth invariant density omega, and take nu = omega. Then d = 0 and P = X. The weighted and unweighted operators coincide, so B1 says the "coupling" adds nothing: the brief's two halves of GH already live on the same operator.

**Observation B4.1 (proved).** In the volume case, GH is equivalent to (K0) together with closed range of X on C^inf.
*Proof.*
- (=>) This is L1 together with Corollary 3 of Text B.
- (<=) Let Xu = f be smooth with u in D'. Then <f, omega> = <Xu, omega> = -<u, L_X omega> = 0, so f lies in the annihilator of the invariant densities, which by (K0) is spanned by omega.
- By closed range and Hahn–Banach, f = Xv with v smooth. Then X(u - v) = 0, so u - v is constant by (K0), and u is smooth. ∎
So in the volume case the problem is: *a C^inf flow with a smooth invariant volume that is DUE (only one invariant distribution up to scale) and cohomology-free with tame inverse has zero entropy.* For the families the problem produces (Theorem R with lambda = omega(d) = 0), this is the strip Sigma(0, theta) with T_z(1) = 0 and |T_z(phi)| <= C ||phi||_{C^1} / Re z near the left edge. The only GH input available on T_z is T_z(phi) = z^N T_z(R^N phi_0) (Theorem V of R7-e, Lemma Q of R8-a). The Leibniz coupling adds nothing to this (B1, with P = X).

**Observation B4.2 (proved; where the strip transform's boundary lives).** In the volume case, for the pair family T_z = B_z + G_z of Theorem V, put F_phi(t) = phi(g_t x) - phi(g_t y).
- The forward part G_z is a family of complex measures: |G_z(phi)| <= 2||phi||_inf / Re z.
- It satisfies G_z(phi) = z G_z(R phi_0) - (R phi_0)(x) + (R phi_0)(y).
- Hence G_s(phi) -> -[(R phi_0)(x) - (R phi_0)(y)] = -B_0(phi) as s -> 0+, nontangentially. Indeed |z G_z(R phi_0)| <= 2|z| ||R phi_0||_inf / Re z -> 0 in any Stolz angle.
So T_z(phi) -> 0 nontangentially at z = 0, for every smooth phi. Iterating gives T_z(phi) = O(|z|^N K'_N(phi) / Re z) for every N, which is the flatness of R7-e/R8-a.
The edge Re z = 0 is reached through the distributional boundary value of T, namely the Fourier transform of the bounded function F_phi on R. By GH, F_phi = (d/dt)^N F_{R^N phi_0} with F_{R^N phi_0} bounded. Vanishing of T would follow if, for a C^1-dense set of phi, the tempered distribution F_phi-hat vanished on a neighbourhood of 0. For instance this holds if ||R^N phi_0||_inf <= C eps^{-N}: then <F_phi-hat, chi> = <F_{R^N phi_0}-hat, (i xi)^N chi>, which is <= C eps^{-N} (eps')^N -> 0 for chi supported in |xi| < eps' < eps. This is Theorem V again, now in its "spectral gap at 0" form. GH gives no growth control on ||R^N phi_0|| (Lemma Q of R8-a, "why it stops").

## B5. Exact point where approach (B) stops
1. The coupling changes the eigen-parameter only through multipliers satisfying an eigen-relation for X (or for P) on the support of the family (B1, B3).
2. Horizontal shifts require multipliers with real growth along orbits. These vanish on the support (B3.2), so they cannot move a strip onto 0.
3. The choice phi = e^w is a change of density (B2). It reaches the volume case only when (V) holds; otherwise it leaves an error term of fixed size that R cannot absorb.
4. In the volume case the two operators coincide (B4), and the problem is again the quantitative growth of R^N (Theorem V / Lemma Q), on which GH, through the closed graph theorem, gives no information.
So (B) cannot prove (EF) in any of its forms (a)–(d). A proof of (EF) needs a genuinely new use of GH at z != 0, or new control of the growth of R^N on a dense set, or a new geometric input (closing of su-configurations, R7-a/R7-f).

## Status of the chain (checked)
- Step 1 (variational reduction) is correct as stated.
- Step 2 (Theorem R) is correct, modulo the cited Ruelle inequality, Pesin unstable manifolds, the Ledrappier–Young subordinate partition and Lemma 6.0. The family is on Omega = {lambda + delta < Re z < lambda + theta - delta}, has order <= 1 and bounds uniform on closed substrips, and is nonzero off a discrete set.
- Step 3 ((EF)) remains **open**.
- I see no flaw in the chain. I also see no counterexample to (EF): any counterexample would be a GH field not conjugate to a Diophantine linear flow (round8_q5 §4.1).

## What is proved / sketched / open
- **Proved:** B1; B2; B3.0–B3.2 and B3(a)–(d); B4.1; B4.2.
- **Not settled:** whether the unweighted coupling (B3(b)) admits multipliers with zeros on supp T_z when Re c != 0. Only the necessary condition (d2) is proved. Even if such multipliers existed, they would lead to the unweighted situation, which needs (V).
- **Open:** (EF) itself. In particular these are open:
  - (EF) on Sigma(0, theta) in the volume-preserving case, i.e. "DUE + tame cohomology-free + smooth volume ⇒ zero entropy";
  - whether GH gives any control on ||R^N phi|| for a dense set of phi (quasi-analytic vectors of R);
  - whether GH constrains eigen-distributions of X at any non-imaginary z off 0.

=== END OF ANSWER round9_q7 ===
