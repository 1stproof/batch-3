# Answer to round1_q2: the line bundle lemma (O2)

Status: **not settled.** Below I prove an exact reduction (Proposition A), the base case, and a conditional inductive argument (Proposition B). The gaps are named in Section 4.

## 1. A criterion (Proposition A, proved)

**Prop A.** Let (D,ω_D) be closed symplectic and L → D a complex line bundle. Suppose there are
(i) an open set U ⊂ D and an integrable complex structure J_U on U that is ω_D-tame, and
(ii) a closed real 2-form F on D with supp F ⊂ U compact, F of type (1,1) for J_U on U, and [F] = 2π c_1(L) in H^2(D;R).
Then there is an ω_D-tame J_D on D, with J_D = J_U near supp F, together with a cocycle for L made of nonvanishing J_D-holomorphic transition functions.

*Proof.*
1. **Extend J_U.** Fix a compact neighbourhood K ⊂ U of supp F. The ω_D-tame structures are the sections of a bundle whose fibres are contractible. So J_U|_K extends to an ω_D-tame J_D on D.
2. **Choose a connection.** Choose a Hermitian metric on L. The curvature forms of U(1)-connections are exactly the closed forms representing 2π c_1(L), multiplied by i (with the usual sign convention). So there is a unitary connection ∇ with curvature iF. In particular ∇ is flat on D \ supp F.
3. **Frames on the flat part.** On D \ supp F, take local ∇-parallel frames over contractible open sets. Two such frames differ by a locally constant transition function, and a locally constant function is J_D-holomorphic for any J_D.
4. **Frames on the integrable part.** On int K, J_D = J_U is integrable. The operator ∂̄_∇ = ∇^{0,1} satisfies (∂̄_∇)² = (iF)^{0,2} = 0. By Newlander–Nirenberg and the Koszul–Malgrange theorem (cited from memory), L|_{int K} has local frames s with ∂̄_∇ s = 0.
5. **Overlaps.** The two kinds of open sets overlap only inside int K \ supp F. There, parallel frames are also ∂̄_∇-holomorphic. The ratio of two ∂̄_∇-holomorphic frames is a holomorphic function for the integrable J_U = J_D.
6. **Cover.** Holomorphic frames on int K and parallel frames on D \ supp F together cover D. This gives the required cocycle. ∎

**Remark.** The obstruction is topological and integrability-theoretic. A_c := Im(H^2_c(U) → H^2(D)) must contain c_1(L) ⊗ R. By duality, U must carry codimension-2 homology dual to c_1(L). Two tempting choices fail:
- U a union of Darboux balls: then A_c = 0.
- U a neighbourhood of a low skeleton: also too small when n ≥ 3.

U could be a neighbourhood of a large set, such as the complement of a 1-skeleton. But I know of no theorem giving a tame *integrable* structure there. Gromov's h-principle gives only almost complex structures.

**Base case (proved).** If dim_R D = 2, take U = D. Every J is integrable, and every 2-form is of type (1,1). Choose F = c·ω_D with the right integral. So the lemma holds, with any tame J_D.

## 2. Route O3 (Proposition B, conditional)

Let P(m) be the statement of the problem in real dimension 2m, **without** deforming ω, for SC divisors that are already ω-regularized (TMZ sense).

**Prop B.** Assume P(m−1). Let (D^{2m},ω_D) be closed symplectic and L → D a line bundle. Suppose there are closed symplectic hypersurfaces E_1, E_2 ⊂ D such that:
- E_1 ∪ E_2 is an ω_D-regularized SC divisor;
- c_1(L) = PD[E_1] − PD[E_2].

Then the line bundle lemma holds for L. Moreover, J_D can be taken to have J_D-holomorphic local defining functions for E_1 and E_2.

*Proof.*
1. P(m−1) gives a tame J_D and local J_D-holomorphic defining functions f^{(k)}_a of E_k on open sets U_a covering D. On sets U_a that miss E_k, take f^{(k)}_a = 1.
2. The functions g_ab = (f^{(1)}_a / f^{(1)}_b)(f^{(2)}_b / f^{(2)}_a) are nonvanishing on U_a ∩ U_b. Each is a product of ratios of defining functions, so it is J_D-holomorphic: off E_k this is clear, and across E_k it follows from removable singularities, as in O1.
3. The cocycle {g_ab} defines O(E_1) ⊗ O(E_2)^{-1}. This bundle has the same c_1 as L, and complex line bundles are classified by c_1. So it is isomorphic to L. ∎

**Supplying E_1, E_2 (sketch only).**
1. Choose a rational symplectic form ω' close to ω_D, and a prequantum bundle P with c_1(P) = k[ω'].
2. By Donaldson–Auroux asymptotically holomorphic sections (cited from memory), for k large there are sections of P^k and of L ⊗ P^k with zero sets E_2 and E_1. These are symplectic and meet transversally with positive symplectic intersection. Symplecticity is an open condition, so it holds for ω_D as well.
3. In homology, PD[E_1] − PD[E_2] = c_1(L ⊗ P^k) − c_1(P^k) = c_1(L).
4. **Missing step:** an ω_D-regularization of E_1 ∪ E_2 without changing ω_D. TMZ allow changing ω. Here one would instead need to isotope E_1 so that it meets E_2 ω_D-orthogonally, with a standard model nearby. I believe this is achievable by a local perturbation along E_1 ∩ E_2, but I have not proved it.

**Assessment of the induction.** P(m−1) is the full problem one dimension lower, including the r ≥ 2 case, so Prop B is not a free-standing proof. A complete induction P(m−1) ⇒ P(m) would also require:
- the relative line bundle lemma for each N_{D_i}, compatible along the strata D_I (O4);
- extending J from a neighbourhood of the deeper strata.

Neither is proved here.

## 3. Relative version

Prop A has a relative form. Suppose J_D is already fixed and integrable near a closed set C, and F can be chosen of type (1,1) there. Then Steps 3–5 of the proof apply unchanged, and the new cocycle restricts on C to holomorphic frames for the given structure. If J_D near E is only "holomorphic in the normal directions" and not integrable, Prop A does not apply. That case is open.

## 4. What is proved and what is open

**Proved:**
- Prop A: the criterion via an integrable region plus a compactly supported (1,1) curvature form.
- The base case dim_R D = 2.
- Prop B: the conditional reduction of the lemma to the problem one dimension lower.

**Open:**
- (Q1) Is there, in every closed symplectic D, an open U with a tame integrable structure such that Im(H^2_c(U) → H^2(D;R)) contains c_1(L), with a (1,1) representative?
- (Q2) Can a pair of Donaldson hypersurfaces be regularized without deforming ω_D?
- (Q3) The compatibility over strata (O4) needed to run the induction for r ≥ 2.

Consequently the YES answer to the original problem is **not established** here. No counterexample was found either: O1 only shows that J must be special, not that it cannot exist.

=== END OF ANSWER round1_q2 ===
