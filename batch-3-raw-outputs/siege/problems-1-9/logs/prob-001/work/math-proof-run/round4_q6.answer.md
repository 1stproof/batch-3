# round4_q6: proof of the missing statement #19

## Summary

**Theorem (proves #19, in a stronger form).** Let P be any monoid (integral, saturated, sharp, commutative). Let f : P -> Q be f.p. in the category **iss** of integral saturated sharp monoids, and let tau be any face of P with Phi_Q := f^{-1}(0) ⊂ tau. Let {Q -> Q_i}_{i∈I} be any family of f.p. maps such that

  (Cov) every valuation v : Q -> V (V valuative) factors through some Q -> Q_i.

For finite nonempty sigma ⊂ I, let Q_sigma be the pushout in **iss** over Q of the Q_i (i ∈ sigma), and let Phi_sigma = ker(P -> Q_sigma). Then the simplicial complex N_tau = {sigma : Phi_sigma ⊂ tau} is nonempty. Moreover every finite subcomplex of N_tau lies in a contractible finite full subcomplex. Hence N_tau has vanishing reduced homology, and its augmented ordered cochain complex with coefficients in any abelian group is exact.

A birhizomic cover satisfies (Cov), so #19 follows. In particular:
- birhizomicity is **not used**, only (Cov) and finite presentation;
- principality of tau is **not used**.

**Departure from the suggested approach.** The task proposed a topological model on the valuation space (Steps 1–3). I did not follow it, for two reasons. First, it is unnecessary: compactness in the patch topology, plus quantifier elimination for divisible ordered abelian groups, reduces everything to finitely many data over a *fine* sub-monoid P' ⊂ P. Second, after the reduction the convex-geometry argument of #15 (Step 4) applies verbatim, because over fine monoids the lifting loci of real valuations are *closed* polyhedral cones. So the non-closed-convex-cover problem ([0,1) ∪ [1,2]) never arises.

**Cited from memory (not reproved here):**
- (QE) The theory DOAG of nontrivial divisible ordered abelian groups, in the language {0, +, −, <}, has quantifier elimination (Tarski / Robinson). Consequently every existential formula is DOAG-equivalent to a quantifier-free one.
- (Nerve) Borsuk/Leray: the nerve of a finite family of compact convex subsets of R^n is homotopy equivalent to their union.
- Gordan's lemma.
- Minkowski–Weyl: a linear image of a polyhedral cone is a closed polyhedral cone.
- Every fine sharp monoid has a strictly positive real functional.
- Tychonoff, and the nonemptiness of inverse limits of nonempty compact Hausdorff spaces.

## 0. Conventions

- A *valuation* of a monoid M is a homomorphism v : M -> V with V valuative.
- Put W_M = M^gp ⊗ Q. Since M is saturated, M^gp is torsion-free and M^gp ⊂ W_M.
- A *valuation class* is a subset π ⊂ W_M with π + π ⊂ π, Q_{>0}π ⊂ π, π ∪ −π = W_M and M ⊂ π. Write X(M) for the set of valuation classes.
- A valuation v gives the class π_v = {x : (v^gp ⊗ Q)(x) ≥ 0}.
- Conversely, π gives the valuation M -> (W_M/(π ∩ −π))_{≥0}. This is a valuative monoid, being the nonnegative part of a totally ordered Q-vector space.
- Two valuations are *equivalent* if they have the same class. For a ∈ M^gp the sign of v(a) depends only on π_v.
- *Patch topology:* X(M) ⊂ 2^{W_M} is cut out by closed conditions, so it is compact Hausdorff. The sets {π : a ∈ π} are clopen. A set is *constructible* if it is a finite Boolean combination of such sets, i.e. defined by sign conditions on finitely many elements of M^gp; such sets are clopen. Restriction along a homomorphism M -> N is a continuous map X(N) -> X(M) (pull back π).
- *v lifts to M'* (for M -> M'): some valuation g of M' has g|_M equivalent to v. E(M') ⊂ X(M) denotes the set of classes that lift.

## 1. Preliminary lemmas

**Lemma 1 (injective valuations).** Every monoid M has a valuation with v^{-1}(0) = {0}. Consequently, for a homomorphism P -> M and a face tau of P: ker(P -> M) ⊂ tau iff some valuation v of M has v > 0 on the image of P \ tau.

*Proof.*
1. C := Q_{≥0}M ⊂ W_M is sharp. If Σα_k m_k = −Σβ_l m'_l, clearing denominators gives a = −b in M^gp with a, b ∈ M, so a = b = 0 by sharpness. All coefficients are nonnegative, so this forces each term to vanish in the sense needed: every element of C ∩ −C is 0.
2. By Zorn, choose a maximal sharp Q_{≥0}-cone π ⊃ C.
3. Suppose x ∉ π ∪ −π. Then π + Q_{≥0}x is still sharp. Indeed, if p + αx = −(p' + βx) with α + β > 0, then −x ∈ π; and α + β = 0 forces p = −p', so p = p' = 0. This contradicts maximality.
4. So π is total. The associated valuation kills only π ∩ −π ∩ M = 0.
5. For the consequence:
   - (⇒) An injective valuation of M has kernel on P equal to ker(P -> M) ⊂ tau, so it is positive on P \ tau.
   - (⇐) A valuation positive on P \ tau kills ker(P -> M), because that set maps to 0. ∎

**Lemma 2 (lifting is constructible, compatible with base change, and real).** Let M be a monoid. Let M' = (M ⊕ N^K/ρ)^{iss}, where ρ is a finite set of pairs (m_e + α_e·y, m'_e + β_e·y) with m_e, m'_e ∈ M and α_e, β_e ∈ N^K. Put b_e = m_e − m'_e ∈ M^gp. There is a quantifier-free formula ψ(x̄) in the language of ordered groups with the following property.

For every valuation v : M -> V: v lifts to M' iff ψ(v(b̄)) holds in V^gp ⊗ Q.

Moreover:
- (a) E(M') is constructible in X(M).
- (b) If w : M -> R_{≥0} lifts to M', then it lifts to a homomorphism M' -> R_{≥0}.
- (c) For any M -> N, the base change N ⊕_M M' = (N ⊕ N^K/ρ)^{iss}. A valuation u of N lifts to it iff ψ(u(b̄)) holds, where b̄ means the images of the b_e in N^gp. In particular this holds iff u|_M ∈ E(M').

*Proof.*
1. **Homomorphisms out of M'.** Since iss is a reflective subcategory, a homomorphism M' -> V' into a valuative V' is the same as a pair (v, ȳ), with v : M -> V' and ȳ ∈ V'^K_{≥0}, such that v(b_e) + (α_e − β_e)·ȳ = 0 in V'^gp for all e. (V' is integral, so a monoid relation holds iff the group relation does.)
2. **The formula.** Let φ(x̄) = ∃ȳ (ȳ ≥ 0 ∧ ∧_e x_e + (α_e − β_e)·ȳ = 0), and let ψ be a quantifier-free DOAG-equivalent of φ, given by (QE).
3. **If v lifts, ψ holds.** Suppose g : M' -> V' lifts v. Then g(M^gp) ⊗ Q and v(M^gp) ⊗ Q are order-isomorphic, with g(b_e) ↔ v(b_e).
   - If V'^gp ⊗ Q ≠ 0, then φ(g(b̄)) holds in it (witness: the images of the generators), so ψ(g(b̄)) holds there.
   - Quantifier-free formulas are preserved under ordered embeddings and isomorphisms, so ψ(v(b̄)) holds in V^gp ⊗ Q.
   - If V'^gp ⊗ Q = 0, then v = 0. φ(0̄) holds in every DOAG (take ȳ = 0), so the variable-free sentence ψ(0̄) is true, also in the trivial group.
4. **If ψ holds, v lifts.** If ψ(v(b̄)) holds and V_Q := V^gp ⊗ Q ≠ 0, then V_Q is a DOAG, so φ holds there. This gives ȳ ∈ V_Q^K, hence a lift M' -> (V_Q)_{≥0}. If V_Q = 0, take ȳ = 0.
5. **(a).** ψ(v(b̄)) is a Boolean combination of sign conditions on the integer combinations of the b_e, which are elements of M^gp. So E(M') is constructible.
6. **(b).** Apply step 4 with V_Q = R, a DOAG containing the values w(b_e). This gives ȳ ∈ R^K_{≥0}.
7. **(c).** The presentation of the base change is the formal consequence of left adjoints commuting with colimits. The criterion is the same proof with N in place of M. ∎

**Lemma 3 (compactness, filtered unions).** Let (M_s) be a filtered system in **iss** with colimit M. (By #17 §1.1 this colimit is computed in monoids.) Then X(M) = lim_s X(M_s) via restriction.

*Proof.* W_M = colim W_{M_s}, so a cone on W_M is the same as a compatible family of cones. Moreover M is the union of the images of the M_s. ∎

**Corollary 3'.** If Z_s ⊂ X(M_s) are nonempty closed sets with Z_t mapping into Z_s for t ≥ s, then some π ∈ X(M) restricts into every Z_s.

*Proof.* An inverse limit of nonempty compact Hausdorff spaces is nonempty. ∎

## 2. Reduction to explicit presentations

**Lemma 4 (retract of a finite presentation).** If A -> B is f.p. in **iss**, then B is a retract under A of some (A ⊕ N^K/ρ)^{iss} with ρ finite.

*Proof.*
1. In commutative monoids under A, B is the filtered colimit of the A ⊕ N^T/ρ. Here T ranges over the finite subsets of B and ρ over the finite sets of relations that hold in B.
2. Applying the reflection iss, which is a left adjoint, shows that B = (B)^{iss} is the filtered colimit in **iss** of the (A ⊕ N^T/ρ)^{iss}.
3. B is f.p., so id_B factors through some stage. ∎

**Reduction.**
1. **Replace Q.** Write Q as a retract under P of R = (P ⊕ N^k/ρ_0)^{iss}, with maps s : Q -> R and r : R -> Q, r s = id, both under P. Put Q~_i = R ⊕_{s,Q} Q_i. Then Q~_sigma = R ⊕_Q Q_sigma.
   - The maps Q_sigma -> Q~_sigma -> Q_sigma (the second one is induced by r and id) compose to the identity under P. Hence ker(P -> Q~_sigma) = Phi_sigma.
   - (Cov) holds for {R -> Q~_i}: if v is a valuation of R, then v∘s lifts to some Q_i, and the pair defines a valuation of Q~_i.
   - Each R -> Q~_i is f.p.
2. **Replace the Q~_i.** By Lemma 4 again, replace each Q~_i by a presented R_i = (R ⊕ N^{k_i}/ρ_i)^{iss} of which it is a retract under R.
   - The pushouts R_sigma and Q~_sigma are mutual retracts under R, so their P-kernels agree.
   - (Cov) persists: compose a lift with the retraction Q~_i -> R_i.
   - So N_tau is unchanged.

From now on, Q = (P ⊕ N^k/ρ_0)^{iss} and Q_i = (Q ⊕ N^{k_i}/ρ_i)^{iss}. Also ker(P -> Q) ⊂ tau still holds.

**Rewriting the relations.** Every element of Q^gp is the class of some element of P^gp ⊕ Z^k. So, as in Lemma 2, a valuation of Q_sigma (sigma ⊂ I) is the same as a tuple (u, z̄, (ȳ_i)_{i∈sigma}) with:
- u : P -> V,
- z̄ ≥ 0 and ȳ_i ≥ 0,
- finitely many integer-linear equations u(a_e) = L_e(z̄, ȳ), where a_e ∈ P^gp.

The equations are those coming from ρ_0 and from the ρ_i with i ∈ sigma. Equivalently, Q_sigma = (P ⊕ N^k ⊕ ⊕_{i∈sigma} N^{k_i} / relations)^{iss}, where each a_e is written as p_e − p'_e with p_e, p'_e ∈ P.

## 3. Proof of the Theorem

**Step A: nonemptiness and a finite subcover.** Let C(Q) = {π ∈ X(Q) : π > 0 on f(P \ tau)}.
- C(Q) is an intersection of clopen sets, so it is closed, hence compact.
- C(Q) is nonempty: by Lemma 1 an injective valuation of Q lies in it, since ker(P -> Q) ⊂ tau.
- By (Cov), C(Q) ⊂ ∪_i E(Q_i). Each E(Q_i) is clopen by Lemma 2(a).

So there is a finite J_0 ⊂ I with C(Q) ⊂ ∪_{i∈J_0} E(Q_i). Since C(Q) ≠ ∅, some i has E(Q_i) ∩ C(Q) ≠ ∅. Then a valuation of Q_i that restricts into C(Q) is positive on P \ tau, so {i} ∈ N_tau by Lemma 1. **So N_tau ≠ ∅.**

**Step B: fix a finite J' ⊃ J_0, and descend to a fine level.** Let L be a finite subcomplex of N_tau, and put J' = vert(L) ∪ J_0. Write N(J') for the full subcomplex of N_tau on J'; it contains L.

Choose a finite S ⊂ P containing all p_e, p'_e from the relations of Q and of the Q_i with i ∈ J'. For finite S' ⊃ S:
- let P_{S'} be the saturation in ⟨S'⟩^gp of ⟨S'⟩; it is fine and contained in P, and P is the filtered union of the P_{S'};
- let Q_{sigma,S'} = (P_{S'} ⊕ N^k ⊕ ⊕_{i∈sigma} N^{k_i} / same relations)^{iss}, for sigma ⊂ J' (sigma = ∅ gives Q_{S'}).

Then:
- Q_{sigma,S'} is fine (finitely generated, and Gordan applies to the saturation).
- Q_{sigma,S'} is the **iss**-pushout over Q_{S'} of the Q_{i,S'} (i ∈ sigma).
- Q_sigma = colim_{S'} Q_{sigma,S'}, since iss commutes with colimits and P = colim P_{S'}.
- tau_{S'} := tau ∩ P_{S'} is a face of P_{S'}.

Put C_{S'}^sigma = {π ∈ X(Q_{sigma,S'}) : π > 0 on the image of P_{S'} \ tau}. If G_{S'} is a finite generating set of P_{S'}, then positivity on P_{S'} \ tau is equivalent to positivity on G_{S'} \ tau. Indeed, tau is a face, so an element outside tau has a summand from G_{S'} \ tau, and values are ≥ 0. Hence C_{S'}^sigma is constructible, so clopen.

*(B1) For S' large, N(J') = {sigma ⊂ J' nonempty : C_{S'}^sigma ≠ ∅} =: N^{S'}.*
1. **N^{S'} is decreasing in S'.** Restricting along Q_{sigma,S'} -> Q_{sigma,S''} preserves the positivity condition.
2. **N(J') ⊂ N^{S'}.** By Lemma 1, sigma ∈ N_tau iff some valuation of Q_sigma is > 0 on P \ tau. Restricting it gives points of every C_{S'}^sigma.
3. **∩_{S'} N^{S'} ⊂ N(J').** Suppose all C_{S'}^sigma are nonempty. By Corollary 3' (they are closed, and compatible under restriction) there is π ∈ X(Q_sigma) whose restrictions lie in all of them. Every x ∈ P \ tau lies in some P_{S'}, so π > 0 on P \ tau, and sigma ∈ N_tau.
4. Since J' is finite, N^{S'} = N(J') for all large S'.

*(B2) For S' large, the E(Q_{i,S'}) with i ∈ J' cover C_{S'}^∅ ⊂ X(Q_{S'}).*
1. Let Bad_{S'} = C_{S'}^∅ \ ∪_{i∈J'} E(Q_{i,S'}). This set is closed, because each E is clopen by Lemma 2(a).
2. **Restriction maps Bad_{S''} into Bad_{S'}.** Q_{i,S''} = Q_{S''} ⊕_{Q_{S'}} Q_{i,S'}, so by Lemma 2(c) a point of X(Q_{S''}) lifts to Q_{i,S''} iff its restriction lifts to Q_{i,S'}. Positivity also restricts.
3. **If all Bad_{S'} are nonempty, we get a contradiction.** Corollary 3' gives π ∈ X(Q) restricting into every Bad_{S'}. Then:
   - π ∈ C(Q), as in (B1) step 3.
   - By Lemma 2(c) with M = Q_{S'} and N = Q, we have Q_i = Q ⊕_{Q_{S'}} Q_{i,S'}, so π ∈ E(Q_i) iff π|_{Q_{S'}} ∈ E(Q_{i,S'}). Hence π ∉ E(Q_i) for every i ∈ J'.
   - This contradicts J_0 ⊂ J'.
4. Bad_{S'} = ∅ is preserved when S' is enlarged (by step 2), so it holds for all large S'.

Fix S' satisfying both (B1) and (B2). Write P' = P_{S'}, tau' = tau_{S'}, Q' = Q_{S'}, Q'_i = Q_{i,S'}, Q'_sigma = Q_{sigma,S'}. All of these are fine.

**Step C: the convex argument (as in #15, Step 4).**

*Setup.*
- Let S_R = Hom(Q', R_{≥0}) ⊂ Hom(Q'^gp, R). This is a closed polyhedral cone.
- Let T_i ⊂ S_R be the image of Hom(Q'_i, R_{≥0}). It is a closed polyhedral cone, by Minkowski–Weyl.
- Let C_R = {w ∈ S_R : w > 0 on G_{S'} \ tau}. It is convex.
- Real points of S_R are valuations of Q'. A real point lies in C_R iff its class lies in C_{S'}^∅.

*Witnesses.* For sigma ∈ N(J') = N^{S'}:
1. By Lemma 1, ker(P' -> Q'_sigma) ⊂ tau'.
2. Q'_sigma is fine and sharp, so it has a strictly positive functional w_0 : Q'_sigma -> R_{≥0}. Then w_0 > 0 on P' \ tau'.
3. So w_sigma := w_0|_{Q'} lies in ∩_{i∈sigma} T_i ∩ C_R.

Let D be the convex hull of the finitely many w_sigma. It is nonempty (N(J') ⊃ N^{S'} ∋ {i} by Step A), compact and convex, and D ⊂ S_R ∩ C_R.

*The sets T_i ∩ D, i ∈ J', are compact and convex, and they cover D.*
- Take w ∈ D. Its class lies in C_{S'}^∅, hence in some E(Q'_i) with i ∈ J', by (B2).
- By Lemma 2(b), w lifts to a real homomorphism Q'_i -> R_{≥0}, i.e. w ∈ T_i.

*Their nerve is exactly N(J').*
- (⊃) The witnesses w_sigma lie in D ∩ ∩_{i∈sigma} T_i.
- (⊂) Take w ∈ D ∩ ∩_{i∈sigma} T_i. The real lifts Q'_i -> R_{≥0} agree on Q', so they glue to Q'_sigma -> R_{≥0}, because R_{≥0} is in **iss**. This is a valuation of Q'_sigma that is > 0 on P' \ tau', since w ∈ C_R. Hence sigma ∈ N^{S'} = N(J').

By the nerve theorem, N(J') ≃ D, which is contractible.

**Step D: conclusion.**
1. Every finite subcomplex L of N_tau lies in the contractible finite full subcomplex N(vert(L) ∪ J_0). Homology commutes with this directed union, so the reduced homology of N_tau is 0.
2. The augmented oriented chain complex is then a free acyclic complex, hence split exact. The augmented ordered chain complex (tuples with repetitions allowed) is chain-homotopy equivalent to it (standard). So applying Hom(−, A) gives an exact augmented ordered cochain complex for every abelian group A.

This proves #19. ∎

## 4. Remarks and status

- **Proved:** #19 as stated, in the stronger form of the Theorem: no birhizomicity, and no principality of tau. This rests on the cited results (QE for DOAG, the nerve theorem for compact convex sets, Gordan, Minkowski–Weyl, Lemma 4's standard compact-object description, Tychonoff).
- **On the director's "equivalent valuation form":** it is correct. Lemma 1 proves the order-extension step. The other step, "compatible lifts give a map out of the pushout", needs the lifts to land in a common target. In the argument above this is handled by Lemma 2(c), via QE / model completeness, instead of an amalgamation theorem; for real lifts it is immediate.
- **On the suggested Steps 1–3:** not needed. The feared non-closed convex covers ([0,1) ∪ [1,2]) cannot occur: after descending to the fine level P' they are replaced by closed polyhedral cones T_i. The descent works because finitely many data (the finite set J', and the finitely many relations) can be realised over a fine P_{S'}, with S' chosen by compactness so that two things hold at once: (B1) the nerve is unchanged, and (B2) the descended family still covers the relevant valuations. This sidesteps the obstruction recorded in #17 §2 (covers do not descend to covers of all of X(Q_{S'})): we only need covering of the set C_{S'}^∅, and only for S' large.
- **Not checked here:** the rest of the chain (#16, Steps 1–3 and 5–6 of the chain). I relied on nothing from it.
- **Open:** nothing remains open for #19 itself. Whether the whole chain is airtight is outside this task.

=== END OF ANSWER round4_q6 ===
