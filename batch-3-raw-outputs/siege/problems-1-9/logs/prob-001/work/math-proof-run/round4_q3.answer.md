# round4_q3: proof of the nerve statement (#19) for every monoid P

## Summary

**Theorem (#19, proved here).** Let P be any monoid, f : P -> Q of finite presentation, {phi_i : Q -> Q_i}_{i in I} a birhizomic cover of Q, and tau ANY face of P with Phi_Q ⊂ tau (principality is not needed). Then N_tau = {finite nonempty sigma ⊂ I : Phi_sigma ⊂ tau} is nonempty and has vanishing reduced integral homology. Consequently its augmented ordered cochain complex with coefficients in any abelian group A is exact.

The proof only uses the following **weak cover property**, which every birhizomic cover has:

(WC) every valuation v : Q -> H_{>=0}, with H a divisible totally ordered abelian group, factors through some phi_i.

Birhizomicity itself plays no role. The reduction to fine monoids works by first-order compactness and by descent of f.p. objects. At the fine level, factorization loci are *closed* polyhedral cones, so the [0,1) ∪ [1,2]-type obstruction never arises.

## 0. Conventions and standard facts used

- C denotes the category of integral, saturated, sharp commutative monoids. Colimits exist in C: take the colimit of commutative monoids and apply the reflector M |-> ((M^int)^sat)^sharp. One checks that sharpening a saturated integral monoid keeps it saturated.
- Filtered colimits in C are computed as in commutative monoids (#17, 1.1; re-checked).
- **f.p.** A map P -> Q is f.p. iff Q is a compact object of the under-category P/C, i.e. Hom_P(Q, -) commutes with filtered colimits. Composites of f.p. maps are f.p. Pushouts of f.p. maps are f.p.
- **Fine monoids are compact in C.** By Rédei's theorem (quoted from memory), a finitely generated commutative monoid is finitely presented as a commutative monoid. Filtered colimits in C are computed in monoids. So for fine M, Hom(M, colim N_j) = colim Hom(M, N_j).
- **Pushouts.** A pushout in C of fine monoids is fine. Integralization and sharpening keep finite generation, and saturation does too by Gordan's lemma.
- **Divisible targets.** For an ordered abelian group H, H_{>=0} is a valuative monoid. Call a valuation *divisible-valued* if it has the form v : Q -> H_{>=0} with H divisible.
  - Every Q in C has an injective divisible-valued valuation. The positive cone Q_Q of Q^gp ⊗ Q is a partial order: it is antisymmetric because Q is sharp and saturated. It is isolated: nx >= 0 implies x >= 0. Such a partial order extends to a total order (Levi / Fuchs, quoted from memory). With this order, the inclusion Q -> (Q^gp ⊗ Q)_{>=0} is injective.
- **P_S.** For finite S ⊂ P, P_S is the saturation in <S>^gp of <S>. It is fine, it lies in P (P is saturated), and P = colim_S P_S is a filtered union.

**Lemma 0.1 (finite presentations).** Let Q -> Q' be f.p. Then Q' is a retract under Q of some Q'' = (Q ⊕ N^k / R)^{iss}, with R a finite set of relations.

*Proof.* Index over pairs (T, R): T is a finite subset of Q', and R is a finite set of relations, in Q ⊕ N^T, that hold in Q'. This index is directed. Put X_{T,R} = (Q ⊕ N^T/R)^{iss}, which maps to Q'. Let X be the colimit in Q/C.

For Y in Q/C, Hom_Q(X, Y) is the set of maps of sets Q' -> Y that respect every finite family of relations holding in Q', together with the structure map from Q. This set is exactly Hom_Q(Q', Y). By Yoneda, X = Q'. Compactness of Q' then factors id_{Q'} through some X_{T,R}. ∎

**Consequence (factorization is existential).** If Q -> Q' is f.p., then "v : Q -> H_{>=0} factors through Q'" is equivalent to: there exist y_1, ..., y_k in H with y_j >= 0 such that every relation of R holds for (v(q))_q and y. This is an existential first-order formula Fact_{Q'} in the language of ordered groups, with constants for finitely many elements of Q.

*Proof.* A map Q'' -> H_{>=0} is the same as such data. A map from Q ⊕ N^k respecting R factors through the integralization, saturation and sharpening, because H_{>=0} lies in C. Factoring through Q'' is equivalent to factoring through its retract Q': compose with Q' -> Q'' or with Q'' -> Q'. ∎

## 1. A finite subfamily already covers (Lemma K for arbitrary Q)

**Lemma 1.** There is a finite J_0 ⊂ I such that every divisible-valued valuation of Q factors through some Q_i with i in J_0.

*Proof.* Suppose not. Then for every finite J ⊂ I there is a divisible-valued v_J not factoring through any Q_i with i in J.

Consider the first-order theory consisting of:
- the axioms of divisible ordered abelian groups;
- constants c_q for q in Q^gp, with c_{q+q'} = c_q + c_{q'};
- c_q >= 0 for q in Q;
- ¬Fact_{Q_i}(c) for every i in I.

Every finite subset of this theory involves only finitely many i, so v_J satisfies it for a suitable J. By the compactness theorem the theory has a model H. This gives a valuation v : Q -> H_{>=0} that factors through no Q_i. That contradicts (WC). ∎

**Nonemptiness of N_tau.** Take an injective divisible-valued valuation v of Q (§0). By (WC), v factors through some Q_i, and by Lemma 1 we may take i in J_0. If x lies in Phi_i, then v(f(x)) = 0, so f(x) = 0, so x lies in Phi_Q ⊂ tau. Hence {i} is in N_tau.

## 2. Descent to a fine level

**Lemma 2 (descent of objects).** Let Q be f.p. under P. Then there are a finite S ⊂ P and a fine Q_S under P_S with Q ≅ P ⊕_{P_S} Q_S under P.

*Proof.*
1. **A retract of a pushout.** For finite S ⊂ P and finite T ⊂ Q, let M_{S,T} be the saturation, inside Q^gp, of the submonoid generated by f(S) ∪ T. It is fine: it is finitely generated by Gordan's lemma, sharp as a submonoid of Q, and contained in Q because Q is saturated. It contains f(P_S). Put R_{S,T} = P ⊕_{P_S} M_{S,T}. Since colimits commute, colim_{S,T} R_{S,T} = P ⊕_{colim P_S} colim M_{S,T} = P ⊕_P Q = Q. By compactness of Q, id_Q = can ∘ s with s : Q -> R := R_{S,T} under P. So e = s ∘ can is an idempotent of R under P.
2. **Descending the idempotent.** Write M = M_{S,T} and R_{S_1} = P_{S_1} ⊕_{P_S} M, so R = colim_{S_1} R_{S_1}. The map e|_M : M -> R factors through some R_{S_1}, because M is compact. Since e is under P, the two maps P_S -> R_{S_1} (one through M, one through P_{S_1}) agree in R, hence at a later stage, because P_S is compact. So e descends to e_1 : R_{S_1} -> R_{S_1} under P_{S_1}, and its base change to P is e. Maps out of a pushout are determined by their restrictions. Now e_1 ∘ e_1 and e_1 agree on M after base change, hence at a later stage S_2. So we get an idempotent e_2 of the fine monoid R_2 under P_{S_2}, whose base change is e.
3. **The image is fine.** Q_2 := e_2(R_2) is in C and is fine. It is integral and sharp as a submonoid of R_2. It is saturated: if x is in Q_2^gp and nx is in Q_2, then x is in R_2, since R_2 is saturated. Also e_2^gp(x) = x, because x lies in the image of the idempotent e_2^gp. So e_2(x) = x lies in Q_2.
4. **Conclusion.** Q_2 splits e_2. Base change P ⊕_{P_{S_2}} (-) preserves split idempotents, since they are absolute. So P ⊕_{P_{S_2}} Q_2 splits e, as does Q. Splittings are unique up to unique isomorphism, so Q ≅ P ⊕_{P_{S_2}} Q_2. ∎

**Lemma 2' (descent of maps).** Let J ⊂ I be finite. Then for some finite S there are fine Q_S and Q_{i,S} (i in J) under P_S, and maps Q_S -> Q_{i,S} under P_S, whose base changes along P_S -> P are Q, Q_i and phi_i.

*Proof.*
1. Each Q_i is f.p. under P, as a composite of f.p. maps, so Lemma 2 applies to Q and to each Q_i. Base-change everything to a common S.
2. The map phi_i restricted to Q_S is a map Q_S -> Q_i = colim_{S''} P_{S''} ⊕_{P_S} Q_{i,S}. Since Q_S is fine, it factors through a finite stage.
3. Compatibility with P_S holds after mapping to Q_i, because phi_i is under P. Hence it holds at a later stage, since P_S is compact.
4. Base-change Q_S to that stage. The base change of the resulting map to P agrees with phi_i on P and on Q_S, so it equals phi_i. Do this for the finitely many i in J. ∎

**Notation.** For finite S' ⊃ S put Q_{S'} = P_{S'} ⊕_{P_S} Q_S and Q_{i,S'} = P_{S'} ⊕_{P_S} Q_{i,S}. For finite nonempty sigma ⊂ J, let Q_{sigma,S'} be the pushout of the Q_{i,S'} (i in sigma) over Q_{S'}. All of these are fine.

Colimits commute, which gives two facts:
- Q_sigma = P ⊕_{P_{S'}} Q_{sigma,S'};
- Q_sigma = colim_{S'} Q_{sigma,S'}, a filtered colimit, computed in monoids.

Put Phi_{sigma,S'} = ker(P_{S'} -> Q_{sigma,S'}) and tau' = tau ∩ P_{S'}, a face of P_{S'}.

**Factorization at level S'.** A valuation of Q_{S'} into H_{>=0} is a pair (alpha, beta):
- alpha is a valuation of P_{S'} and beta is a valuation of Q_S;
- they agree on P_S.

The pair (alpha, beta) factors through Q_{i,S'} iff beta factors through Q_{i,S}. Indeed, a lift beta' of beta gives the lift (alpha, beta'), and conversely a lift restricts to Q_{i,S}. The same holds at the level of P, with Q = P ⊕_{P_S} Q_S and Q_i = P ⊕_{P_S} Q_{i,S}.

## 3. Choosing the fine level

Fix a finite subcomplex L of N_tau, and put J = J_0 ∪ vert(L). Take S as in Lemma 2' for this J.

**Lemma 3 (covering at a finite level).** There is a finite S_1 ⊃ S such that, for every S' ⊃ S_1, every divisible-valued valuation of Q_{S'} factors through some Q_{i,S'} with i in J_0.

*Proof.*

*Monotonicity.* Suppose the property holds at S_1, and let S' ⊃ S_1. A valuation (alpha, beta) of Q_{S'} restricts to a valuation of Q_{S_1}. That restriction factors through some Q_{i,S_1}, so its Q_S-component beta factors through Q_{i,S}. Hence (alpha, beta) factors through Q_{i,S'}. So the property propagates to every S' ⊃ S_1.

*Existence by compactness.* Suppose the property fails for every finite S'. Then for every S' there is a divisible-valued (alpha_{S'}, beta_{S'}) such that beta_{S'} factors through no Q_{i,S} with i in J_0. Consider the theory consisting of:
- the axioms of divisible ordered abelian groups;
- constants a_p for p in P^gp and b_q for q in Q_S^gp, both additive;
- a_p >= 0 for p in P, and b_q >= 0 for q in Q_S;
- a_p = b_{f_S(p)} for p in P_S^gp;
- ¬Fact_{Q_{i,S}}(b) for i in J_0.

Q_{i,S} is fine over Q_S, so Fact_{Q_{i,S}} is existential (Rédei).

A finite subset mentions finitely many a_p. Choose S' ⊃ S containing every p in P for which positivity is asserted, and both halves p_1, p_2 of a decomposition p = p_1 - p_2 of every mentioned p in P^gp. Then (alpha_{S'}, beta_{S'}) satisfies that finite subset.

By compactness the theory has a model. It gives a valuation alpha of P and a valuation beta of Q_S, agreeing on P_S. So (alpha, beta) is a divisible-valued valuation of Q = P ⊕_{P_S} Q_S, and it factors through no Q_i with i in J_0. This contradicts Lemma 1. ∎

**Lemma 4 (kernels are detected at a finite level).** There is a finite S_2 ⊃ S such that, for all S' ⊃ S_2 and all nonempty sigma ⊂ J, Phi_sigma ⊂ tau iff Phi_{sigma,S'} ⊂ tau'.

*Proof.*
- (⇒) This holds for every S'. P_{S'} -> Q_{sigma,S'} -> Q_sigma gives Phi_{sigma,S'} ⊂ Phi_sigma ∩ P_{S'} ⊂ tau ∩ P_{S'}.
- (⇐) For each of the finitely many sigma with Phi_sigma ⊄ tau, pick x_sigma in Phi_sigma \ tau. Its image in the filtered colimit Q_sigma = colim Q_{sigma,S'} is 0. So it is already 0 in some Q_{sigma,S'} with x_sigma in S'. Take S_2 to contain all such S'. Then x_sigma lies in Phi_{sigma,S'} \ tau' for every S' ⊃ S_2. ∎

Fix S' ⊃ S_1 ∪ S_2. By Lemma 4, **N_tau(J) := N_tau ∩ 2^J equals N' := {sigma ⊂ J : Phi_{sigma,S'} ⊂ tau'}**.

## 4. The fine-level nerve is contractible (the closed-convex argument of #15, re-checked)

**The cones.** Write S_R = Hom(Q_{S'}, R_{>=0}), a closed polyhedral cone. Let T_i ⊂ S_R be the image of Hom(Q_{i,S'}, R_{>=0}), a closed polyhedral cone. By Lemma 3, applied to the divisible group R, **S_R = ∪_{i in J_0} T_i.**

**Real valuations of a pushout.** R_{>=0} lies in C. So Hom(Q_{sigma,S'}, R_{>=0}) is the set of compatible tuples of real valuations of the Q_{i,S'}, and its image in S_R is T_sigma := ∩_{i in sigma} T_i, again a polyhedral cone.

**Kernels are cut out by T_sigma.** Q_{sigma,S'} is fine and sharp, so it has a strictly positive functional (an interior point of its dual cone). Hence
Phi_{sigma,S'} = {x in P_{S'} : w(x) = 0 for all w in T_sigma}.

**The set C.** Let C = {w in S_R : w(x) > 0 for all x in P_{S'} \ tau'}. C is convex. Moreover **sigma ∈ N' iff T_sigma ∩ C ≠ ∅**:
- (⇒) Let w_0 be the sum of a finite generating set of T_sigma. For x in P_{S'}, w_0(x) = 0 iff every generator kills x, since all values are >= 0. That happens iff x lies in Phi_{sigma,S'} ⊂ tau'. So w_0 lies in C.
- (⇐) Let w be in T_sigma ∩ C. If x lies in Phi_{sigma,S'}, then w(x) = 0, so x lies in tau'.

**N' is contractible.**
1. N' is nonempty: it contains the vertex found in §1, since J_0 ⊂ J and N_tau(J) = N'.
2. For each simplex sigma of N', choose w_sigma in T_sigma ∩ C. Let D be the convex hull of these finitely many points. D is compact, convex, nonempty, and D ⊂ C ⊂ S_R.
3. The sets T_i ∩ D (i in J) are compact and convex, and they cover D, because S_R = ∪_{J_0} T_i.
4. Their nerve is exactly N'. It is contained in N' because D ⊂ C. It contains N' because w_sigma lies in D ∩ T_sigma.
5. By the nerve theorem for finite families of compact convex sets in R^n (Borsuk 1948 / Leray; quoted from memory), N' is homotopy equivalent to D, which is contractible.

## 5. Conclusion

Every finite subcomplex L of N_tau lies in N_tau(J) = N', which is contractible. Every reduced cycle of N_tau is supported on a finite subcomplex, so it bounds in N_tau. Hence H̃_*(N_tau; Z) = 0, and N_tau ≠ ∅ by §1.

The augmented ordered chain complex is chain-homotopy equivalent to the augmented simplicial chain complex (standard). It is therefore a free, acyclic complex of free abelian groups. Hence it is split exact, and Hom(-, A) of it, the augmented ordered cochain complex with coefficients A, is exact. This proves #19. ∎

## 6. Remarks on the chain (#16, steps 1-6)

- I re-checked the chain as stated (Steps 1, 2, 3, 5, 6) and found no flaw. With #19 now proved, the chain gives YES to the headline question for every monoid P, subject to the facts it quotes: Cartan's criterion, and #16 (principality of kernel faces), whose proof I did not re-verify in full.
- The argument above never uses birhizomicity, only (WC). So #19 holds for any family of f.p. maps satisfying (WC). Principality of tau is not needed either.
- The worry about non-closed convex loci (the director's (c), and the "≺-openness" lemma) is genuine at the level of higher-rank valuations of a non-fine Q. It is bypassed because, by Lemmas 3 and 4, the whole finite configuration descends to a fine level. There every factorization locus is a closed polyhedral cone.

## Status

- **Proved:** #19 for every monoid P, every f.p. Q, every birhizomic cover (indeed every family with (WC)), and every face tau ⊃ Phi_Q.
- **Quoted from memory (standard):**
  - first-order compactness theorem;
  - Rédei's theorem (finitely generated commutative monoids are finitely presented);
  - Gordan's lemma;
  - extension of isolated partial orders on torsion-free abelian groups to total orders;
  - Borsuk / Leray nerve theorem for compact convex sets;
  - equivalence of ordered and simplicial chain complexes;
  - uniqueness and absoluteness of splittings of idempotents.
- **Interpretation used:** "finite presentation in the category" means "compact object of the under-category P/C". This is the standard meaning; Lemma 0.1 and Lemma 2 prove from it the retract-of-finite-presentation and descent statements, which earlier rounds had only sketched (#17, 1.2).
- **Open:** nothing within #19. For the headline question, the remaining quoted inputs are Cartan's criterion and #16, which I did not re-prove.

=== END OF ANSWER round4_q3 ===
