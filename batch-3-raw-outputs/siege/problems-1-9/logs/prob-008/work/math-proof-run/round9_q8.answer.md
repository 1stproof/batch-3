# round9_q8 answer

## Status (read this first)
- **Neither (1) nor (2) is achieved.** (EF) remains open. So does the [GOAL] in dimension >= 4: the earlier rounds proved it for dim M <= 3.
- **What is proved here.**
  1. Proposition A, a "nu-aligned defect" lemma. It corrects the candidate mechanism of the planner's sketch (A): the defect lemma as the planner stated it is false, and the true form is Proposition A.
  2. Theorem B, a strict strengthening of Lemma M for strips touching 0. Let T_z be an eigen-family (EF) on a strip with 0 on its boundary. It is enough that **the restriction of T_z to the nu-mean-zero functions** continues holomorphically across 0. Along the direction nu-hat, T_z may be arbitrarily singular at 0 (divergent, essential singularity, natural boundary). This turns the Patterson asymptotics of R8-c into a precise residual target.
  3. Two "dead end, and why" statements: Remark C on the planner's mechanism (B), and Remark D on countability of the point spectrum. Also Remark E, a model computation: the residual target cannot be met by single orbits, so pair cancellation is essential.
- **The chain itself.** I found no flaw in the chain. I did not re-verify Theorem R, whose proof is not quoted in my brief.

Conventions are those of the brief: nu is a smooth positive density, nu-hat = nu/nu(M), d = div_nu X, P phi = X phi + d phi. A *distribution density* is a continuous linear functional on C^inf(M), complex-valued where needed. (F1) and (F2) are as in R6-a §1:
- (F1) T∘P = 0 implies T = c nu-hat.
- (F2) T∘P = c' nu-hat implies c' = 0.
Both follow from (K0) and (K1) alone, by R7-b Lemma 1.1.

---

## 1. Proposition A (nu-aligned defect lemma) — proved, using only (K0) and (K1)

**Proposition A.** Assume (K0) and (K1); GH suffices. Let D be an open disc around 0. Let (A_z), z in D, be distribution densities such that:
- z -> A_z(phi) is holomorphic on D for every smooth phi;
- there are k and C with |A_z(phi)| <= C ||phi||_{C^k} for all z in D (locally uniform suffices);
- A_z(P phi) = z A_z(phi) + c(z) nu-hat(phi) for all phi and all z in D, for some function c.

Then c is holomorphic on D, and there is a holomorphic alpha on D with A_z = alpha(z) nu-hat and c(z) = -z alpha(z).

Conversely, every such pair is a solution, since nu-hat∘P = 0. So the defect equation does **not** force A = 0. The planner's sketch (A) asked whether "a family with nu-valued defect must vanish". The answer is no: it must be **nu-aligned**.

*Proof.*
1. *c is holomorphic.* Fix phi_1 smooth with nu-hat(phi_1) = 1. Then c(z) = A_z(P phi_1) - z A_z(phi_1), which is holomorphic.
2. *Taylor coefficients.* Write A_z = sum_n A_n z^n, with A_n(phi) = (1/2 pi i) ∮ A_w(phi) w^{-n-1} dw over a small circle in D. Each A_n is a distribution density of order <= k (Cauchy estimates). Write c(z) = sum_n c_n z^n.
3. *Comparing coefficients.* Comparing coefficients in the defect equation gives
   - A_0∘P = c_0 nu-hat, and
   - A_n∘P = A_{n-1} + c_n nu-hat for n >= 1.
4. *Induction.*
   - n = 0: by (F2), c_0 = 0. Then (F1) gives A_0 = a_0 nu-hat.
   - Step: if A_{n-1} = a_{n-1} nu-hat, then A_n∘P = (a_{n-1} + c_n) nu-hat. By (F2), a_{n-1} + c_n = 0, and by (F1), A_n = a_n nu-hat.
5. *Conclusion.* a_n = A_n(phi_1), so alpha(z) := sum a_n z^n converges on D. We get A_z = alpha(z) nu-hat, and c_n = -a_{n-1}, i.e. c(z) = -z alpha(z). ∎

**Meromorphic variant (same proof).** Suppose A_z is holomorphic on D \ {0} and meromorphic at 0 with finite pole order. Then the Laurent coefficients satisfy A_n∘P = A_{n-1} + c_n nu-hat. The same recursion, started at the least index with A_n != 0, gives the same conclusion. Below that index, the relation gives c_n = 0.

---

## 2. Theorem B (strips touching 0: only the mean-zero part needs to continue) — proved, using only (K0) and (K1)

**Theorem B.** Assume (K0) and (K1); GH suffices.
- Let W be a connected open set with 0 on its boundary, e.g. W = Sigma(0,b) = {0 < Re z < b}.
- Let (T_z), z in W, be an EF on W: T_z(phi) is holomorphic in z for each phi, T_z is locally uniformly of finite order, and T_z∘P = z T_z.
- Suppose there are a disc D around 0 and distribution densities H_z (z in D) such that:
  - z -> H_z(phi) is holomorphic on D;
  - |H_z(phi)| <= C ||phi||_{C^k} on D;
  - D ∩ W is connected and nonempty;
  - H_z(phi) = T_z(phi) for every z in D ∩ W and every phi with nu-hat(phi) = 0.

Then T_z = 0 for all z in W.

**Nothing at all is assumed about z -> T_z(phi_1) near 0** for phi_1 with nu-hat(phi_1) = 1. In particular:
- the divergence of the forward transform along nu-hat as Re z -> 0+ (the Patterson behaviour of R8-c, Lemma 2.2 / Corollary 2.3) is harmless;
- so is an essential singularity, or a natural boundary, in that one direction.

Lemma M of R6-b is the special case in which T_z itself continues.

*Proof.*
1. *Projected family.* Fix phi_1 with nu-hat(phi_1) = 1. For z in D put H'_z(phi) := H_z(phi - nu-hat(phi) phi_1). This is holomorphic and of order <= k (phi_1 is fixed and smooth), and H'_z(phi_1) = 0 for all z.
2. *Defect equation on D ∩ W.* Let z be in D ∩ W.
   - Since nu-hat∘P = 0, H'_z(P phi) = H_z(P phi) = T_z(P phi) = z T_z(phi).
   - Also z H'_z(phi) = z T_z(phi) - z nu-hat(phi) T_z(phi_1).
   - Hence H'_z(P phi) - z H'_z(phi) = c(z) nu-hat(phi), with c(z) := z T_z(phi_1).
3. *Extension to D.* Define c~(z) := H'_z(P phi_1) for z in D; it is holomorphic on D. On D ∩ W, step 2 with phi = phi_1 gives c~(z) = c(z), since H'_z(phi_1) = 0. For each fixed phi, both sides of
   H'_z(P phi) - z H'_z(phi) = c~(z) nu-hat(phi)
   are holomorphic on the connected disc D and agree on the nonempty open set D ∩ W. By the identity theorem they agree on D.
4. *Proposition A.* It gives H'_z = alpha(z) nu-hat on D and c~ = -z alpha. Evaluating at phi_1 gives alpha = 0. Hence H' = 0 on D and c~ = 0.
5. *T vanishes near 0.* On D ∩ W we get z T_z(phi_1) = c(z) = c~(z) = 0. Since 0 is not in W, T_z(phi_1) = 0. Then T_z(phi) = H'_z(phi) + nu-hat(phi) T_z(phi_1) = 0 for every phi.
6. *T vanishes on W.* For each phi, z -> T_z(phi) vanishes on the open set D ∩ W. By the identity theorem (W connected) it vanishes on W. ∎

**Remark B1 (what this says about (PE0), the case lambda = mu(d) = 0 of Theorem R).** There T_z = B_z + G_z on Sigma(0, theta).
- B_z, the backward part, is holomorphic on Re z < theta, so across 0.
- G_z(phi) = int_0^inf e^{-zt} F_phi(t) dt, with F_phi(t) = e^{J_t(x)} phi(g_t x) - e^b e^{J_t(y)} phi(g_t y).

By Theorem B, the whole case (PE0) of the chain follows from the following statement.

**(A-res).** For every nu-mean-zero smooth phi, the forward pair transform G_z(phi) continues holomorphically from {0 < Re z < theta} to a neighbourhood of 0, with C^k bounds that are uniform in phi.

R8-c's Corollary 2.3 shows that the divergent leading term of G_s as s -> 0+ is aligned with nu-hat. So (A-res) says exactly that **after the nu-hat direction is removed, nothing singular is left at 0**. I could not prove (A-res).

The meromorphic variant of Proposition A lets (A-res) be weakened to meromorphic continuation with bounded pole order. By Lemma H of R7-e, it can presumably also be replaced by quasi-analytic flatness on a half-disc. I have not written out that version, so I do not claim it.

---

## 3. Dead ends, with reasons

**Remark C (the planner's mechanism (B) adds no information by itself).** Leibniz gives P(phi psi) = phi X psi + psi P phi. So the identity
  V_z(X psi) = z V_z(psi) - T_z((P phi) psi),  with V_z := T_z(phi ·),
is literally the eigen-relation T_z∘P = z T_z tested on the product phi psi. Taking phi = 1 recovers the eigen-relation. So the family of identities indexed by (phi, psi) is equivalent to the eigen-relation alone.

Taking phi = e^a with a smooth gives the eigen-relation for P_a = X + (d + Xa). That is just the change nu -> e^{a} nu, which is already absorbed in the statement of (EF). The best one can do this way is inf_a ||d + Xa||_inf = max_mu |mu(d)|. (This is the Hahn–Banach distance from d to the closure of the coboundaries in C^0, cited as standard.) So the weight can never be made smaller than the largest |mu(d)|.

Combining (B) with the tame inverse R of X (Lemma B of R7-d) gives
  T_z(phi f) = z T_z(phi R f) - T_z((P phi) R f)  for f in X(C^inf).
Inserting the tame bound ||Rf||_{C^1} <= C ||f||_{C^m} gives an estimate *weaker* than the trivial |T_z(phi f)| <= ||T_z|| ||phi f||_{C^1}. So no contradiction can come from size estimates alone. A contradiction would need a kernel (Jordan-chain) argument for the unweighted operator. By R8-d Corollary C, that needs dim I = 1, i.e. (V).

Moreover, without (V), X(C^inf) is the annihilator of I, which has codimension dim I >= 2. Then R is not even defined on all nu-mean-zero functions. **(B) can therefore act only through (V), as the round-8 dichotomy predicted.**

**Remark D (countability of Sigma_1 ∩ {Re z != 0} cannot come from soft arguments).**
- Eigenvectors for distinct eigenvalues are linearly independent. But (C^1)' has uncountable algebraic dimension and is not separable, so cardinality gives nothing.
- Operators with an open set of eigenvalues of the transpose exist in every infinite-dimensional setting; the backward shift is an example.
- GH is a statement about X = P - 0 only.

So countability off iR would itself need a mechanism transferring GH to P - z. Remark 3.3 of R8-b explains why such a transfer seems to contain the [GOAL]. I found none.

**Remark E (model computation: (A-res) fails for single orbits, even for GH fields).** Let Y be a Diophantine linear field on T^n, with nu = Lebesgue (so d = 0), and phi a mean-zero trigonometric polynomial. Then
  int_0^inf e^{-zt} phi(x + t alpha) dt = sum_{k != 0} phi-hat_k e^{2 pi i k.x} / (z - 2 pi i k.alpha).
This has poles at 2 pi i k.alpha. For general smooth mean-zero phi these poles accumulate at 0 along iR, so iR is generically a natural boundary.

Hence the single-orbit transforms of mean-zero functions do **not** continue across 0, even for the model GH fields. Any proof of (A-res) must use the cancellation inside the pair S = delta_x - e^b delta_y, which has no analogue in the model (Diophantine flows have no asymptotic pairs). This is consistent with R6-e's remark that Re z = 0 is generally a natural boundary, now isolated to the mean-zero part.

---

## 4. On option (2) (a counterexample to the method)

I could not construct one. The constraints I found:
- (K0) and (K1) alone already exclude:
  - every hyperbolic periodic orbit with a homoclinic point (Lemma K, via R7-b Lemma 1.2);
  - every partially hyperbolic configuration covered by Theorem U, in the cases where it uses only Proposition MG / Theorem J;
  - every heteroclinic connection with the wrong signs of I(gamma).
  So a counterexample needs an EF produced without hyperbolic horseshoes. The candidates are:
  - (a) positive entropy carried by non-hyperbolic measures only (dim >= 4);
  - (b) an exponentially backward-asymptotic pair with sub-exponential Jacobian growth (R5-a Theorem B), in a zero-entropy flow.
  I know no example of either kind that satisfies (K0).
- In the volume case, (K0) plus closed range already implies GH. If X(C^inf) is closed, then X(C^inf) = annihilator of I = ker omega-hat by (K0). So Xu = f smooth with u in D' gives f = Xv with v smooth (since omega-hat(f) = 0), hence X(u - v) = 0, hence u is smooth by (K0). So a counterexample to the method satisfying (K0), (K1) and closed range must be **dissipative** (not (V)), and then dim I >= 2.

  I do not know whether, without (V), GH is strictly stronger than (K0), (K1) and closed range together. The missing piece is exactly: "Xu in C^inf with u in D' implies Xu in X(C^inf)". This is the further consequence of GH that any such example would violate.

---

## 5. Summary

**Proved:**
- Proposition A: nu-aligned defect lemma, holomorphic and meromorphic forms; uses only (K0) and (K1).
- Theorem B: under (K0) and (K1), an EF on a connected open set with 0 on its boundary vanishes as soon as its restriction to ker nu-hat continues holomorphically to a disc around 0. No condition is needed in the nu-hat direction. This strictly contains Lemma M (strip version).
- Remarks C and E, rigorous as stated: (B) is equivalent to the eigen-relation, and it acts only through (V); single-orbit transforms of mean-zero functions do not continue across 0, even for Diophantine flows.
- In the volume case, (K0) plus closed range implies GH (§4).

**Open:**
- (EF) in general; neither option (1) nor option (2) is achieved.
- In particular (A-res): continuation across 0 of the mean-zero part of the forward pair transform, for mu-generic pairs on one Pesin unstable leaf of a positive-entropy ergodic mu with mu(d) = 0. By Theorem B this would settle the case lambda = 0 of the chain; the strips not touching 0 would still need (EF) in full.
- Whether, without (V), GH is strictly stronger than (K0), (K1) and closed range together.
- Hence the [GOAL] in dimension >= 4.

=== END OF ANSWER round9_q8 ===
