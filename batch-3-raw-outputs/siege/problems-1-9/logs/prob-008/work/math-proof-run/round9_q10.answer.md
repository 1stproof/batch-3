# round9_q10: check of Theorem R (block R8-a), Lemma 6.0 (block R6-a §6), the variational step, and the derivation (EF) => [GOAL]

## Summary of findings
- Every analytic step of Theorem R checks out: the interpolation, the constant b, both one-sided bounds, absolute and locally uniform convergence, the bound (ii) (uniform in Im z), holomorphy, the integration by parts giving (iii), and the non-vanishing argument.
- **One genuine but minor gap.** Lemma 6.0 and the Ledrappier–Young/Ledrappier–Strelcyn facts [LY] are applied to f = g_1. The proof of Lemma 6.0 uses ergodicity of mu **under f = g_1** ("w = w_0 a.e. by ergodicity"), and [LY] is usually stated for f-ergodic measures. But Theorem R, and the variational step, only provide a **flow**-ergodic mu, and a flow-ergodic mu need not be g_1-ergodic. The gap is repaired below (§1.0, §3): pass to a g_1-ergodic component nu of mu with h_nu(g_1) > 0 and nu(G) = 1, or, more simply, start the chain directly from a g_1-ergodic measure. After the repair, Theorem R and the chain are correct, modulo the cited classical theorems (Ruelle's inequality, Pesin's local unstable manifolds, the Ledrappier–Strelcyn subordinate partition, the variational principle and the ergodic decomposition).
- A cosmetic slip in the last line of Lemma 6.0 is corrected in §2.
- The derivation (EF) + Theorem R + variational step => h_top(g_1) = 0 is correct. No hypothesis of (EF) is stronger than what Theorem R delivers. Neither dim M >= 2 nor mu(Zero X) = 0 is needed.

Conventions (as in the brief): nu_0 is a fixed smooth positive density (written nu in the brief; I write nu_0 to free the letter nu for measures). d = div_{nu_0} X, P phi = X phi + d phi, J_t(z) = int_0^t d(g_s z) ds. Fix a Riemannian distance on M. Then |phi(p) - phi(q)| <= ||dphi||_inf d(p,q), and d is Lipschitz with constant Lip(d). Let ||phi||_{C^1} = ||phi||_inf + ||dphi||_inf.

---

## 1. Theorem R

### 1.0 The gap and the corrected statement

**Where the gap is.** In step 2 of Theorem R, the facts "for mu-a.e. x the conditional mu^xi_x is non-atomic" (Lemma 6.0) and "h_mu(g_1) = H_mu(xi | g_1 xi)" ([LY]) are used for f = g_1 and the flow-ergodic mu.
- In the proof of Lemma 6.0 one gets w o f = w a.e. The conclusion "w is a.e. constant" then requires f-ergodicity.
- Without it, the argument only shows that {w > 0} is an f-invariant set on which the integrand of H(xi | f xi) vanishes. If h_mu(f) > 0, this gives mu{w = 0} > 0, not w = 0 a.e.
- A flow-ergodic mu fails to be g_1-ergodic exactly when the flow has an L^2(mu)-eigenfunction with eigenvalue in 2 pi i Z \ {0}. This can certainly happen, for instance for suspensions with constant roof 1/k.

So, as written, step 2 is not justified for every flow-ergodic mu.

**Corrected statement (Theorem R').** Let X be any smooth vector field on a compact manifold M (GH not used). Let nu be a Borel probability that is g_1-invariant and g_1-ergodic, with h_nu(g_1) > 0. Put lambda := nu(J_1) = int int_0^1 d(g_s z) ds dnu(z). Let chi > 0 be the smallest positive Lyapunov exponent of (g_1, nu), and fix 0 < theta < chi and 0 < delta < theta/4. Put Omega := {lambda + delta < Re z < lambda + theta - delta}. Then there is a family T_z (z in Omega) of continuous linear functionals on C^1(M) satisfying (i), (ii), (iii) of (EF), with T_z != 0 for all z in Omega outside a discrete subset of Omega.

**Relation to the original statement.** Let mu be flow-ergodic with h_mu(g_1) > 0, and let mu = int nu dtau(nu) be its g_1-ergodic decomposition.
- By Jacobs' formula, h_mu(g_1) = int h_nu(g_1) dtau. So tau{nu : h_nu(g_1) > 0} > 0.
- Let G_mu be the set of z with J_t(z)/t -> mu(d) as t -> +inf and as t -> -inf. By the continuous-time Birkhoff theorem for the flow-ergodic mu (applied to the flow and to the reversed flow), mu(G_mu) = 1. Hence nu(G_mu) = 1 for tau-a.e. nu.
- For such nu, nu-a.e. point has J_n/n -> nu(J_1) (Birkhoff for g_1). So nu(J_1) = mu(d).
- The Lyapunov spectrum of g_1 is flow-invariant, because Dg_s is uniformly bounded for |s| <= 1. So it is mu-a.e. constant, and nu has the same chi.

So Theorem R' applied to such a nu gives the family of Theorem R for mu, with the same lambda = mu(d), the same chi and the same strip. **Theorem R as stated is therefore true, but its proof must go through nu.**

### 1.1 Proof of Theorem R' (written out in full, with each check)

**Step 1 (exponents).** h_nu(g_{-1}) = h_nu(g_1) > 0.
- [Ru] Ruelle's inequality (cited from memory): for a C^1 diffeomorphism f of a compact manifold and an f-invariant ergodic nu, h_nu(f) <= sum of the positive Lyapunov exponents of (f, nu), with multiplicity. Here g_{+-1} is C^inf, and nu is ergodic for both.
- Applied to g_1, it gives a positive exponent, so chi := chi^+_min > 0 exists. (Applied to g_{-1}, it gives a negative exponent; that is not needed below.)
- Exponents are nu-a.e. constant by ergodicity.

**Step 2 (generic points).** Let G := {z : J_t(z)/t -> lambda as t -> +inf and as t -> -inf}.
- *Birkhoff.* J_n(z) = sum_{k=0}^{n-1} J_1(g_k z). So J_n/n -> nu(J_1) = lambda nu-a.e. (Birkhoff for g_1).
- *Backward.* J_{-n}(z) = -sum_{k=1}^{n} J_1(g_{-k} z), and nu is g_{-1}-ergodic. So J_{-n}/(-n) -> lambda nu-a.e.
- *Real times.* |J_t - J_{floor(t)}| <= ||d||_inf. So the integer limits give the real ones.
- Hence nu(G) = 1. G is Borel: it is defined by integer-time limits of continuous functions.

**Step 3 (choice of the pair; checks the citations [P], [LY] and Lemma 6.0).** Cited from memory, for the C^inf diffeomorphism f = g_1 and the f-ergodic nu:
- [P] (Pesin; Ruelle 1979; Fathi–Herman–Yoccoz; no hyperbolicity assumption on the other exponents). For nu-a.e. x there is a local unstable manifold W^u_loc(x), an embedded C^1 disc tangent to the sum of the Oseledets spaces of the positive exponents. For every delta' > 0 and every y in W^u_loc(x): d(f^{-m}x, f^{-m}y) <= C(x, delta') e^{-(chi - delta')m} for m >= 0.
  - The same holds, with a constant depending also on y, for y in the global unstable manifold W^u(x) = union_n f^n W^u_loc(f^{-n}x). Indeed, if f^{-n}y lies in W^u_loc(f^{-n}x), apply [P] at f^{-n}x for m >= n, and absorb the finitely many m < n into the constant.
- [LS/LY] (Ledrappier–Strelcyn 1982; Ledrappier–Young 1985, Part I). There is a measurable partition xi subordinate to W^u, with xi(x) contained in W^u(x) (indeed in a local unstable manifold) for a.e. x. It is increasing: xi refines f xi, i.e. xi(fx) ⊂ f(xi(x)). And h_nu(f) = H_nu(xi | f xi) = -int log nu^{f xi}_z(xi(z)) dnu(z).
  - These are stated for ergodic measures and C^2 (indeed C^{1+alpha}) diffeomorphisms, zero exponents allowed. Both hypotheses hold here because nu is g_1-ergodic, and that is the point of the repair.
  - Since h_nu(f) <= sum chi^+ < inf by [Ru], H(xi | f xi) is finite.
- Lemma 6.0 (re-proved in §2) gives: nu^xi_x({x}) = 0 for nu-a.e. x.
- *The conditional is carried by G.* nu(G) = 1 and nu = int nu^xi_x dnu(x). So int nu^xi_x(G) dnu(x) = 1, hence nu^xi_x(G) = 1 for a.e. x. (G is Borel, so this is legitimate.)
- *The pair.* Intersect the full-measure sets: the set where [P] holds, x in G, nu^xi_x({x}) = 0, nu^xi_x(G) = 1, and nu^xi_x(xi(x)) = 1. Take x in this intersection. Then nu^xi_x(G ∩ xi(x) \ {x}) = 1, so there is y in G ∩ xi(x) with y != x. **Answer to the brief's question:** the conditional is carried by G because G has full measure and conditionals of a full-measure set are a.e. full. No dynamical property of G is needed beyond its Borel measurability.
- *Rate.* Choose delta' with chi - delta' > theta. By [P] (global form): d(g_{-m}x, g_{-m}y) <= C e^{-(chi - delta')m} for integers m >= 0, where C depends on x and y.

**Step 4 (interpolation to real times).** Let t <= 0 and write t = -m - s with m >= 0 an integer and s in [0,1). Then g_t = g_{-s} o g_{-m}. Put L' := max_{s in [0,1]} Lip(g_{-s}); it is finite because (s, z) -> g_{-s}(z) is C^1 on [0,1] x M with M compact. Then

d(g_t x, g_t y) <= L' C e^{-(chi - delta')m} <= L' C e^{chi} e^{-(chi - delta')|t|} <= C_0 e^{-theta|t|}.

Checked.

**Step 5 (the constant b).** For t <= 0, J_t(x) - J_t(y) = -int_t^0 (d(g_s x) - d(g_s y)) ds. The integrand is bounded by Lip(d) C_0 e^{-theta|s|}, which is integrable on (-inf, 0]. So
- b := lim_{t -> -inf} (J_t(x) - J_t(y)) = -int_{-inf}^0 (d(g_s x) - d(g_s y)) ds exists, and
- J_t(x) - J_t(y) - b = int_{-inf}^t (d(g_s x) - d(g_s y)) ds, so |J_t(x) - J_t(y) - b| <= K e^{-theta|t|} with K := Lip(d) C_0/theta.

Checked.

**Step 6 (one-sided growth bounds).** Since x and y lie in G, there is C_1 (depending on x and y) with:
- J_t(x) <= C_1 + (lambda + delta)t and J_t(y) <= C_1 + (lambda + delta)t for t >= 0;
- J_t(x) <= C_1 + (-lambda + delta)|t| for t <= 0, because J_t(x) = lambda t + o(|t|) = -lambda|t| + o(|t|) as t -> -inf.

Checked.

**Step 7 (the two bounds of step 4 of R8-a).** Put S := delta_x - e^b delta_y and F_phi(t) := e^{J_t(x)} phi(g_t x) - e^{b + J_t(y)} phi(g_t y). This makes sense for every continuous phi, and is continuous in t.
- *t >= 0.* |F_phi(t)| <= (1 + e^b) e^{C_1} e^{(lambda + delta)t} ||phi||_inf.
- *t <= 0.* Write r_t := J_t(x) - J_t(y) - b, so that e^{b + J_t(y)} = e^{J_t(x)} e^{-r_t} and |r_t| <= K e^{-theta|t|} <= K. Then
  F_phi(t) = e^{J_t(x)} [ (phi(g_t x) - phi(g_t y)) + (1 - e^{-r_t}) phi(g_t y) ].
  Using |phi(p) - phi(q)| <= ||dphi||_inf d(p,q), Step 4, and |1 - e^{-r}| <= |r| e^{|r|}:
  |F_phi(t)| <= e^{C_1} e^{(-lambda + delta)|t|} (C_0 + K e^K) e^{-theta|t|} ||phi||_{C^1} = C_2 e^{-(theta + lambda - delta)|t|} ||phi||_{C^1}.
- *Constants.* C_2 = e^{C_1}(C_0 + K e^K) and C_3 := (1 + e^b) e^{C_1} depend on x, y and the flow, never on phi. That is all that is required, since the pair is fixed once and for all.

Checked.

**Step 8 (convergence, holomorphy, bound (ii)).** Let a := lambda + delta and b_0 := lambda + theta - delta. Then a < b_0 because theta > 2 delta (indeed delta < theta/4). For z with sigma = Re z in (a, b_0):
- for t >= 0: |e^{-zt} F_phi(t)| <= C_3 e^{-(sigma - a)t} ||phi||_inf;
- for t <= 0: |e^{-zt} F_phi(t)| = e^{sigma|t|} |F_phi(t)| <= C_2 e^{-(b_0 - sigma)|t|} ||phi||_{C^1}.

So T_z(phi) := int_R e^{-zt} F_phi(t) dt converges absolutely for every phi in C^1(M), and is linear in phi. On a closed substrip a < a_1 <= Re z <= b_1 < b_0:

|T_z(phi)| <= ( C_3/(a_1 - a) + C_2/(b_0 - b_1) ) ||phi||_{C^1},

uniformly in Im z. This gives (ii) and continuity of T_z on C^1(M).
- *Holomorphy (i).* For fixed t the integrand is entire in z, and it is jointly continuous in (t, z). On every compact subset of Omega it is dominated by the z-independent integrable function C_3 e^{-(a_1 - a)t} 1_{t >= 0} + C_2 e^{-(b_0 - b_1)|t|} 1_{t <= 0} (times the norm of phi). So z -> T_z(phi) is holomorphic, by Morera plus Fubini, or by differentiation under the integral sign. This holds for every phi in C^1, in particular for smooth phi.

Checked.

**Step 9 (the eigen-relation (iii)).** For smooth phi, F_phi is C^1 with F_phi' = F_{P phi}. This is elementary here and needs no C^inf-valued argument. For a single point w:

d/dt [e^{J_t(w)} phi(g_t w)] = d(g_t w) e^{J_t(w)} phi(g_t w) + e^{J_t(w)} (X phi)(g_t w) = e^{J_t(w)} (P phi)(g_t w),

using d/dt J_t(w) = d(g_t w) and d/dt phi(g_t w) = (X phi)(g_t w). Apply this to w = x and to w = y (with the constant factor e^b).

On [-R, R]:

int_{-R}^{R} e^{-zt} F_{P phi}(t) dt = [e^{-zt} F_phi(t)]_{-R}^{R} + z int_{-R}^{R} e^{-zt} F_phi(t) dt.

- *Boundary terms.* By Step 8 applied to phi, |e^{-zR} F_phi(R)| <= C_3 e^{-(sigma - a)R} ||phi||_inf -> 0 and |e^{zR} F_phi(-R)| <= C_2 e^{-(b_0 - sigma)R} ||phi||_{C^1} -> 0.
- *Integrals.* Both integrals converge absolutely as R -> inf, by Step 8 applied to phi and to P phi (P phi is smooth, so in C^1).

Hence T_z(P phi) = z T_z(phi) for every smooth phi and every z in Omega. This is (iii). Checked.

**Step 10 (non-vanishing).** Since x != y, there is a smooth phi_0 with phi_0(x) = 1 and phi_0(y) = 0. Then F_{phi_0}(0) = 1.
- Fix a real kappa_0 in (a, b_0). By Step 8, G(t) := e^{-kappa_0 t} F_{phi_0}(t) is continuous and in L^1(R), with G(0) = 1.
- Its Fourier transform is Ghat(omega) = int e^{-i omega t} G(t) dt = T_{kappa_0 + i omega}(phi_0).
- If z -> T_z(phi_0) vanished identically on Omega, then Ghat = 0. By uniqueness of the Fourier transform on L^1, G = 0 a.e., hence everywhere by continuity. This contradicts G(0) = 1.
- So the holomorphic function z -> T_z(phi_0) on the connected open strip Omega is not identically zero. By the identity theorem its zero set Z is discrete and closed in Omega.
- For z in Omega \ Z we have T_z(phi_0) != 0, so T_z != 0.

Checked. ∎

**Conclusion on (1).** With the repair of §1.0, Theorem R holds as stated: there is no GH, and the family satisfies (i), (ii) and (iii) of (EF) on Omega, with T_z != 0 off a discrete set.

---

## 2. Lemma 6.0 (re-checked, with two clarifications)

**Setting.** f a C^2 diffeomorphism, nu an **f-ergodic** invariant probability, and xi as in [LS/LY]: increasing, with H(xi | f xi) = h_nu(f) in (0, inf).

**Claim.** nu^xi_x({x}) = 0 for a.e. x, and a.e. conditional nu^xi_x is non-atomic.

**Proof (the R6-a proof, with the missing justifications supplied).**
1. *Transport of conditionals.* (f xi)(fx) = f(xi(x)). By invariance of nu and uniqueness of disintegration, nu^{f xi}_{fx} = f_* nu^xi_x for a.e. x. Hence nu^{f xi}_{fx}({fx}) = nu^xi_x({x}) =: w(x).
   - w is measurable: w(z) = lim_n nu^xi_z(Q_n(z)) for a refining sequence of finite partitions Q_n generating the Borel sigma-algebra.
2. *Restriction formula (clarification 1).* Since xi refines f xi:
   nu^xi_z = nu^{f xi}_z(· ∩ xi(z)) / nu^{f xi}_z(xi(z)) for a.e. z.
   This needs nu^{f xi}_z(xi(z)) > 0 a.e., which holds because -int log nu^{f xi}_z(xi(z)) dnu = H(xi | f xi) < inf.
   - Given that, nu^{f xi}_z-almost every point lies in one of the countably many xi-cells of positive conditional mass inside (f xi)(z).
   - The right side is then a xi-measurable system of probabilities whose average over each f xi-cell, hence over M, reproduces nu. Uniqueness of disintegration gives the formula.
   R6-a used this without comment; it is correct.
3. *Monotonicity.* With z = fx and {fx} ⊂ xi(fx):
   w(fx) = nu^{f xi}_{fx}({fx}) / nu^{f xi}_{fx}(xi(fx)) = w(x) / nu^{f xi}_{fx}(xi(fx)) >= w(x).
4. *Invariance.* 0 <= w <= 1 and nu is invariant, so int (w o f - w) dnu = 0. The integrand is nonnegative, so w o f = w a.e.
5. *Constancy.* By **f-ergodicity**, w = w_0 a.e. (This is the step that needs g_1-ergodicity; see §1.0.)
6. *If w_0 > 0.* Step 3 with equality gives nu^{f xi}_{fx}(xi(fx)) = 1 for a.e. x, hence nu^{f xi}_z(xi(z)) = 1 for a.e. z (f preserves nu). Then H(xi | f xi) = 0, contradicting h_nu(f) > 0. So w_0 = 0.
7. *Non-atomicity (clarification 2).* Let A := {z : nu^xi_z({z}) > 0} = {w > 0}. Then nu(A) = 0 by step 6. (R6-a wrote "nu(A) = int w dnu"; that is a slip, since nu(A) = nu{w > 0}, but the conclusion is the same.)
   - Conditionals are constant on cells. So A ∩ xi(x) is exactly the set of atoms of nu^xi_x.
   - Hence 0 = nu(A) = int nu^xi_x(A) dnu(x) = int nu^xi_x(atoms of nu^xi_x) dnu(x).
   - So a.e. conditional is non-atomic. ∎

Only "nu^xi_x({x}) = 0 a.e." is actually used in Theorem R (§1.1 Step 3). Lemma 6.0 is correct for f-ergodic nu.

---

## 3. The variational step (step 1 of the chain)

**Statement needed (repaired form).** If h_top(g_1) > 0, then there is a g_1-invariant, g_1-ergodic Borel probability nu with h_nu(g_1) > 0.

**Proof (cited classical theorems).**
- *Variational principle* (Goodwyn–Dinaburg–Goodman; g_1 is a homeomorphism of a compact metric space): h_top(g_1) = sup h_m(g_1) over g_1-invariant m. So some m has h_m(g_1) > 0.
- *Jacobs' formula*: if m = int nu dtau(nu) is the g_1-ergodic decomposition, then h_m(g_1) = int h_nu(g_1) dtau. Hence some ergodic component nu has h_nu(g_1) > 0.
- This is all Theorem R' needs. The topological entropy of the flow is by definition h_top(g_1), and h_top(g_t) = |t| h_top(g_1).

**The chain's original version.** It passes through m-bar = int_0^1 (g_s)_* m ds and the flow-ergodic decomposition. It is also correct:
- (g_r)_* m-bar = m-bar, because s -> (g_s)_* m is 1-periodic when (g_1)_* m = m.
- h_{(g_s)_* m}(g_1) = h_m(g_1), because g_s conjugates (g_1, m) to (g_1, (g_s)_* m).
- The barycentre formula holds for these integral decompositions into g_1-invariant measures (combine Jacobs' formula with the decomposition of the ergodic decompositions).

But it then needs the reduction of §1.0 (flow-ergodic to g_1-ergodic) before Lemma 6.0 can be applied. Going directly to a g_1-ergodic nu is shorter.

---

## 4. The derivation (EF) + Theorem R' + variational step => h_top(g_1) = 0

1. Suppose h_top(g_1) > 0. By §3 there is a g_1-ergodic nu with h_nu(g_1) > 0.
2. By Theorem R' (with the same smooth density nu_0 used to define d and P in (EF)), there is a family T_z on Omega = {a < Re z < b_0} with a < b_0, satisfying (i), (ii), (iii), and T_z != 0 for some z in Omega.
3. *Hypothesis-by-hypothesis comparison with (EF).*
   - T_z is a continuous linear functional on C^1(M) (Step 8).
   - (i): holomorphy for smooth phi. Delivered for all C^1 phi.
   - (ii): sup over closed substrips and ||phi||_{C^1} <= 1. Delivered, uniformly in Im z.
   - (iii): T_z(P phi) = z T_z(phi) for smooth phi. Delivered.
   - Same nu_0, d and P on both sides.
   **No hypothesis of (EF) is stronger than what Theorem R' gives.** (EF) is even stated with a uniform bound, which is exactly what Step 8 gives; no polynomial growth in |Im z| is needed.
4. Under GH, (EF) gives T_z = 0 for all z in Omega. This is a contradiction, so h_top(g_1) = 0.

**Dimension and zeros.**
- Neither Theorem R' nor the derivation uses dim M >= 2.
- If dim M = 1, Theorem R' is vacuous: by [Ru] for g_1 and g_{-1} a positive-entropy measure would need a positive and a negative exponent among n = 1 exponents. In any case flows on compact 1-manifolds have zero entropy.
- mu(Zero X) = 0 is not used anywhere. If nu(Zero X) > 0, then nu(Zero X) = 1 by ergodicity (Zero X is invariant), and since g_1 = id there, h_nu = 0. So such nu never enter, but the proof does not need this.
- GH enters only through (EF).

**Remark on (EF) (no attempt).** The strip Omega may or may not contain 0. When it does, (EF) on Omega is already Lemma M / Theorem J, so the open content of (EF) is the case of strips avoiding 0, as the brief says.

---

## 5. Status
- **Proved here (modulo the cited classical theorems** [Ru], [P], [LS/LY], the variational principle, Jacobs' formula, and the Birkhoff theorems): Theorem R' (§1.1); Lemma 6.0 for g_1-ergodic measures (§2); the reduction of flow-ergodic to g_1-ergodic measures (§1.0), so Theorem R as originally stated is true; the variational step (§3); and the implication (EF) => [GOAL] (§4).
- **Gap found and repaired:** the original Theorem R and Lemma 6.0 used ergodicity of mu under g_1 while mu was only flow-ergodic.
- **Open (not addressed, as instructed):** the statement (EF) itself, for strips not containing 0.

VERDICT: gap found — Lemma 6.0/[LY] need g_1-ergodicity but mu is only flow-ergodic; repaired via a g_1-ergodic component (Theorem R' §1), after which Theorem R and the chain derivation are correct

=== END OF ANSWER round9_q10 ===
