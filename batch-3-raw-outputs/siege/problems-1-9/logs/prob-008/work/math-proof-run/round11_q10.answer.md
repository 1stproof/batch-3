# round11_q10 — answer (partial; (AP) not settled)

## Plan
Target: statement (AP) (no backward-exponentially-asymptotic pair x != y of bi-recurrent points with common Birkhoff average lambda <= 0 of d), or zero entropy directly. Steps: (1) check the chain; (2) record what is rigorously available for the pair; (3) attempt lambda = 0 in the volume case via the inverse R = X^{-1}; (4) state exactly where it stops.

## 1. Check of the chain (no flaw found)
- Step 2: (a), (b), (c) follow as stated: y in xi(x) lies in the Pesin local unstable manifold, so dist(g_t x, g_t y) <= C e^{-theta|t|} for t <= 0 for every theta < chi. Since nu'(G ∩ Rec) = 1, a.e. conditional nu'^xi_x gives full mass to G ∩ Rec, and conditionals are non-atomic, so there is y != x in xi(x) ∩ G ∩ Rec.
- Extra remark (proved): y is automatically off the orbit of x. Suppose y = g_s x with s != 0. Then dist(g_t x, g_{t+s} x) -> 0 as t -> -inf. Take t_n -> -inf with g_{t_n} x -> x, which is possible by (c). In the limit dist(x, g_s x) = 0, so g_s x = x and y = x, a contradiction. So (AP)-pairs are pairs of distinct orbits.
- Step 3 (lambda > 0, pass to -X): this is correct. div_nu(-X) = -d and J^{-X}_t = J_{-t}. The pair then comes from local stable manifolds of X, which are the local unstable manifolds of -X. -X is GH by (O4).
- Range of lambda that actually needs (AP). For |lambda| < chi one may choose theta in (|lambda|, chi), and then Theorem J applies; I rechecked this. In detail, with S = delta_x - e^b delta_y:
  - backward: |F_phi(t)| <= C e^{J_t(x) - theta|t|} ||phi||_{C^1} <= C' e^{(|lambda| + eps' - theta)|t|} ||phi||_{C^1};
  - forward: |F_phi(t)| <= C e^{(lambda + eps')t} ||phi||_inf.
  
  So the open content is lambda = 0, and lambda <= -chi with chi the smallest positive exponent carrying the pair.

## 2. Volume case, lambda = 0: what the inverse of X gives (proved), and why it does not close
Setting: GH plus a smooth invariant density omega. Take nu = omega, so d = 0 and J = 0. By (O2) and the duality consequence of Text A, every omega-mean-zero smooth phi equals X(R phi). Here R phi is smooth with mean zero, and by Text B Lemma 2, ||R phi||_{C^k} <= C_k ||phi||_{C^{m(k)}}.

Let (x, y) satisfy (a) and put D_psi(t) = psi(g_t x) - psi(g_t y). This function is bounded on R, and |D_psi(t)| <= C ||psi||_{C^1} e^{-theta|t|} for t <= 0. For 0 < Re z < theta set
 T_z(psi) = ∫_R e^{-zt} D_psi(t) dt.
This is an order-1 distribution density, holomorphic in z, with |T_z(psi)| <= C ||psi||_{C^1} (1/Re z + 1/(theta - Re z)).

**Lemma 2.1 (proved).**
(i) T_z(X psi) = z T_z(psi) and T_z(1) = 0.
(ii) For omega-mean-zero phi and every k >= 1, T_z(phi) = z^k T_z(R^k phi). Hence for |z| <= theta/2 we have |T_z(phi)| <= C_k(phi) |z|^k / Re z, with C_k(phi) = 3C ||R^k phi||_{C^1}/theta' finite.
(iii) Consequently T_sigma(phi) -> 0 as sigma -> 0+ along the reals, for every smooth phi.

*Proof.* (i) We have d/dt D_psi(t) = D_{X psi}(t). Integrate e^{-zt} D_{X psi} by parts on [-A, A]. The boundary term at +A tends to 0 because D_psi is bounded and Re z > 0. The boundary term at -A tends to 0 because |D_psi(-A)| e^{Re z A} <= C e^{(Re z - theta)A}. So T_z(X psi) = z T_z(psi). T_z(1) = 0 because D_1 = 0.
(ii) Apply (i) k times to psi = R^k phi, using X R = Id on mean-zero functions. Then use the a priori bound on T_z.
(iii) Write phi = phi-bar + phi_0. T_sigma(phi-bar) = 0, and |T_sigma(phi_0)| <= C_2 sigma^2 / sigma -> 0. ∎

**Why this does not close.** Theorem B (entry 96) would need T_z restricted to ker omega-hat to continue holomorphically across z = 0. The bounds of 2.1 do not give this. For example, h(z) = Σ_n a_n/(z - i tau_n) with tau_n -> 0 and a_n = O(tau_n^k) for every k is holomorphic on Re z > 0 and satisfies |h(z)| <= C_k |z|^k / Re z near 0, yet it has no continuation across 0. Such singularities at i tau_n are boundary eigen-distributions L_X T = -i tau_n T. In the volume case GH does not visibly exclude these: smooth unimodular eigenfunctions exist for Diophantine flows. Even with a uniform linear loss C_k(phi) <= A^k (k!)^m (Gevrey), the resulting bound e^{-c|z|^{-1/m}}/Re z is still met by the nonzero function e^{-z^{-1/m}} when m >= 2. So controlled derivative loss alone does not help either. The missing input is control of the forward behaviour of D_psi(t) at nonzero frequencies, which is the approximate-coincidence problem (AC). I could not supply it, and recurrence (c) did not enter any argument I found.

## 3. lambda <= -chi: status
For S = delta_x - e^b delta_y, backward decay needs theta > |lambda|. Gaining extra backward cancellation needs either:
- more points on a C^infinity unstable arc with vanishing moments, which requires affine parameters or non-stationary normal forms along the leaf (entry 68's mechanism); or
- a smooth signed density on a strong-unstable disc W^{>c}(x) with c > |lambda|. But then forward decay needs limsup J_t(z)/t < 0 for leaf-a.e. z of that disc. This holds only if entropy sits in the strong directions, which Proposition N says it does not when lambda < 0.

Neither variant uses only the pair, so the statement as posed stays open here too.

## Summary
- **Proved:** the chain is valid (with the extra remark that (AP)-pairs lie on distinct orbits). (AP) holds when -chi < lambda < 0, by Theorem J. In the volume case, Lemma 2.1 holds: the pair family is flat to infinite order at z = 0 along the real axis.
- **Shown not to suffice:** the bounds of Lemma 2.1, even with Gevrey loss, are compatible with nonzero families having singularities at i tau_n -> 0.
- **Open:** (AP) for lambda = 0 (including the volume case) and for lambda <= -chi. Hence zero topological entropy for GH flows remains unproved by this route.

=== END OF ANSWER round11_q10 ===
