# round4_q7: proof of #19

**Plan (written first).** I prove #19 as stated, for every P. I do not use the suggested fine-model transfer; Section 7 explains why. The proof has four steps.
(a) Each locus E_i is cut out by finitely many non-strict sign conditions x ∈ W, with x in U := Q^gp ⊗ Q.
(b) The nerve condition Φ_σ ⊂ τ is a condition on the cone Q_Q + cone(X_σ).
(c) Compactness gives a finite subcover.
(d) An abstract acyclicity theorem, proved by induction on the number of "undecided" sign conditions. The induction step refines the cover by the two-member sign cover {z ≥ 0}, {z ≤ 0} and uses the standard double-complex comparison of Čech complexes.

Status: **all steps proved below.**

---

## 0. Result

**Theorem.** Let P be any monoid, f : P → Q any map in 𝒞 (the category of integral, saturated, sharp commutative monoids), and {Q → Q_i}_{i∈I} a family of f.p. maps under Q. Assume that every valuation v : Q → V factors through some Q_i. Let τ ⊂ P be any subset with Φ_Q := f^{-1}(0) ⊂ τ. Then:
- N_τ = {σ ⊂ I finite nonempty : Φ_σ ⊂ τ} is nonempty;
- its augmented ordered chain complex is exact, so its reduced integral homology vanishes;
- for every abelian group A, its augmented ordered cochain complex with coefficients A is exact.

In particular #19 holds. Three of its hypotheses are not needed: birhizomy (only "factors through some member" is used), f.p. of Q over P, and principality of τ.

"f.p." is read as: Hom_Q(Q_i, –) commutes with filtered colimits in 𝒞 under Q. If instead it means "presented by finitely many generators and relations", Lemma 1(i) below is immediate.

## 1. Cones and valuations

Put U = Q^gp ⊗ Q. Q^gp is torsion-free: if nx = 0, then x and −x lie in Q by saturation, so x = 0 by sharpness. So Q ⊂ U. Let Q_Q = Q_{≥0}·Q.

A *cone* is a subset K ⊂ U with 0 ∈ K, K + K ⊂ K and Q_{>0}K ⊂ K. Its lineality is lin K = K ∩ (−K). A cone is *total* if W ∪ (−W) = U.

- Q_Q has lineality 0. If x = q/n and −x = q'/n', then n'q + nq' = 0 in Q^gp, so q = q' = 0 by sharpness and torsion-freeness.
- A valuation v : Q → V gives the total cone W_v = {x ∈ U : v(x) ≥ 0 in V^gp ⊗ Q}, which contains Q_Q. (The divisible hull of an ordered group is ordered.)
- Conversely, a total cone W ⊃ Q_Q gives a valuation v_W : Q → V_W. Here V_W is the nonnegative part of the ordered Q-vector space H_W = U/lin W, with positive cone W/lin W. V_W is integral, saturated, sharp and totally ordered.

**Lemma Z.** Every cone K is contained in a total cone W with lin W = lin K.

*Proof.* Cones K' ⊃ K with lin K' = lin K are closed under unions of chains, so Zorn gives a maximal one, K'. Suppose x ∉ K' ∪ (−K'), and put K'' = K' + Q_{≥0}x. If y ∈ lin K'', write y = k_1 + ax and −y = k_2 + bx with a, b ≥ 0. Then k_1 + k_2 = −(a+b)x.
- If a + b > 0, then −x ∈ K', which is a contradiction.
- So a = b = 0, and y = k_1 ∈ lin K'.

Hence lin K'' = lin K'. Since K'' ⊋ K', this contradicts maximality, so K' is total. ∎

**Consequence (injective valuations).** Every M ∈ 𝒞 has a valuation ι : M → V with ι(m) = 0 only for m = 0. To see this, apply Lemma Z to M_Q ⊂ M^gp ⊗ Q, which has lineality 0 as shown above.

## 2. Lemma 1: loci are finite sign conditions

For each i let E_i be the set of total cones W ⊃ Q_Q such that v_W extends to Q_i, i.e. there is g : Q_i → V_W under Q.

**Lemma 1.** For each i there is a finite set X_i ⊂ U such that:
(a) E_i = {W : X_i ⊂ W};
(b) for any valuation v : Q → V, if v extends to Q_i, then X_i ⊂ W_v.

*Proof.*

(i) *Q_i is a retract under Q of a finitely presented object.* Write M = Q_i. For a finite S ⊂ M and a finite set R of relations r = s between elements of Q ⊕ N^S that hold in M, let T(S,R) be the image of (Q ⊕ N^S)/R after integralizing, saturating and sharpening.
- The pairs (S,R) form a directed poset.
- Filtered colimits of objects of 𝒞, computed in monoids, stay in 𝒞: integrality, nx = ny ⇒ x = y, saturation and sharpness are each witnessed at a finite stage.
- The map colim T(S,R) → M is surjective.
- It is injective. Let x, y lie at a common stage T and have the same image in M. Choose n with nx = [a] and ny = [b], where a, b ∈ Q ⊕ N^S; saturation gives this. Then (a,b) is a relation valid in M. Adding it to R makes nx = ny, hence x = y, because the groups are torsion-free.
- So M = colim T(S,R). By f.p., id_M factors through some T = T(S,R), and M is a retract of T under Q.

Maps out of a retract: v extends to M if and only if it extends to T. Compose with M → T → M in one direction and with T → M in the other.

(ii) *Extensions to T.* Let H be an ordered divisible group containing v(Q), with V ⊂ H_{≥0}. A map T → H_{≥0} under Q is the same as a vector y ∈ H^S with y ≥ 0 satisfying the relations. Indeed, a map from Q ⊕ N^S that respects R factors uniquely through integralization, saturation and sharpening, because H_{≥0} is integral, saturated and sharp.

Write the j-th relation as (a_j, α_j) = (b_j, β_j) with a_j, b_j ∈ Q and α_j, β_j ∈ N^S. It reads (α_j − β_j)·y = c_j, where c_j := v(b_j − a_j).

(iii) *Fourier–Motzkin.* Consider a finite system of rational linear inequalities in unknowns y and parameters c, over an ordered divisible group H. Eliminating one unknown replaces the system by the "lower bound ≤ upper bound" pairs together with the inequalities not involving that unknown. This preserves solvability in H: given the rest, take the unknown to be the maximum of its finitely many lower bounds (or the minimum of the upper bounds, or 0 if there are none).

Eliminating all y from {y ≥ 0, (α_j − β_j)·y = c_j} gives finitely many rational vectors u_m, independent of H, with:
solvable in H ⟺ u_m·c ≥ 0 for all m.

Put x_m = Σ_j u_{mj}(b_j − a_j) ∈ U and X_i = {x_m}. Then u_m·c = v(x_m).

Conclusion:
- For H = H_W this gives (a).
- For H = V^gp ⊗ Q, if v extends to Q_i then it extends to T inside H_{≥0}, so v(x_m) ≥ 0 for all m, i.e. X_i ⊂ W_v. This is (b). ∎

## 3. Lemma 2: the nerve condition as a cone condition

For finite σ ⊂ I put X_σ = ∪_{i∈σ} X_i and K_σ = Q_Q + cone(X_σ). For a cone K ⊃ Q_Q put f^{-1}(lin K) = {p ∈ P : f(p) ∈ lin K}.

Since f(p) ∈ Q_Q ⊂ K, this equals {p ∈ P : −f(p) ∈ K}.

**Lemma 2.** Φ_σ := ker(P → Q_σ) = f^{-1}(lin K_σ).

*Proof.* A map Q_σ → V_W under Q is the same as a family of maps Q_i → V_W under Q, i ∈ σ, because Q_σ is the pushout in 𝒞 and V_W ∈ 𝒞. So the set of W for which v_W extends to Q_σ is ∩_{i∈σ} E_i = {W ⊃ K_σ}.

(⊂) Suppose p ∈ Φ_σ. Take W ⊃ K_σ total with lin W = lin K_σ (Lemma Z). Then v_W extends to Q_σ and kills the image of p, so f(p) ∈ lin W = lin K_σ.

(⊃) Suppose f(p) ∈ lin K_σ. Let ι : Q_σ → V be injective (§1) and v = ι|_Q. Since v extends to every Q_i, i ∈ σ, Lemma 1(b) gives X_σ ⊂ W_v, so K_σ ⊂ W_v. Hence v(f(p)) = 0, i.e. ι(image of p) = 0, so the image of p is 0. ∎

Let 𝒢 = {cones K ⊃ Q_Q : f^{-1}(lin K) ⊂ τ}. Then:
- **N_τ = {σ : K_σ ∈ 𝒢}.**
- **(G0)** If Q_Q ⊂ K ⊂ K' and K' ∈ 𝒢, then K ∈ 𝒢.
- **(G1)** If K ∈ 𝒢 and W ⊃ K is total with lin W = lin K, then W ∈ 𝒢. The sets f^{-1}(lin ·) are equal.
- **(G2)** For any cone K ⊃ Q_Q and any z ∈ U, f^{-1}(lin(K + Qz)) = f^{-1}(lin(K + Q_{≥0}z)) ∪ f^{-1}(lin(K + Q_{≥0}(−z))). Indeed, write −f(p) = k + tz and split according to the sign of t. So if K ± z ∈ 𝒢, then K + Qz ∈ 𝒢.
- **(G3)** Q_Q ∈ 𝒢, because f^{-1}(lin Q_Q) = f^{-1}(0) = Φ_Q ⊂ τ. Here lin Q_Q = 0 and Q ⊂ U.

## 4. Lemma 3: finite subcover

The set 𝒯 of total cones W ⊃ Q_Q is closed in {0,1}^U. Each defining condition involves finitely many coordinates:
- z ∈ W or −z ∈ W;
- z, z' ∈ W ⇒ z + z' ∈ W;
- z ∈ W ⇒ rz ∈ W for r ∈ Q_{>0};
- q ∈ W for q ∈ Q_Q.

So 𝒯 is compact by Tychonoff. Each E_i = {X_i ⊂ W} is open. The E_i cover 𝒯: every W gives a valuation v_W, which factors through some Q_i by hypothesis. Hence a **finite J_0 ⊂ I has ∪_{i∈J_0} E_i = 𝒯.**

## 5. Theorem T: abstract acyclicity

Fix:
- a Q-vector space U and a cone K_0;
- a family 𝒢 of cones containing K_0, satisfying (G0), (G1) and (G2) for cones containing K_0;
- an abelian group A.

For a cone K ⊃ K_0 and a finite family (X_j)_{j∈J} of finite subsets of U, let C^•(K) be the augmented ordered Čech complex:
- C^p(K) = ∏_{(j_0,…,j_p) ∈ J^{p+1}} A(K + cone X_{j_0} + … + cone X_{j_p}) for p ≥ −1, where A(K') = A if K' ∈ 𝒢 and 0 otherwise;
- the maps between factors are the identity A → A or 0 (well defined by (G0));
- d is the alternating sum of the deletions.

When K ∈ 𝒢, this is the augmented ordered cochain complex of N(K) = {σ : K + cone X_σ ∈ 𝒢} with coefficients A.

**Theorem T.** If every total cone W ⊃ K contains some X_j, then C^•(K) is exact.

*Proof.* Induction on m(K) = #{z ∈ Z : z ∉ K and −z ∉ K}, where Z = ∪_j X_j is finite. If K ∉ 𝒢, then C^•(K) = 0 by (G0). So assume K ∈ 𝒢.

*Cone lemma.* Suppose there is j* such that σ ∈ N(K) ⇒ σ ∪ {j*} ∈ N(K), and {j*} ∈ N(K). Then (hc)(j_0,…,j_{p−1}) = c(j*, j_0,…,j_{p−1}) is well defined: if the tuple with j* added carries A, so does the tuple without it, by (G0). The usual computation gives dh + hd = id, including in degree −1. So C^• is contractible.

*Base case m(K) = 0.* Take W ⊃ K total with lin W = lin K (Lemma Z). Some X_{j*} ⊂ W. Let z ∈ X_{j*}.
- If z ∉ K, then −z ∈ K because z is decided, so z ∈ lin W = lin K ⊂ K, a contradiction.
- So X_{j*} ⊂ K, and K + cone X_{j*} = K. Hence j* is a cone point and the cone lemma applies.

*Row lemma.* For any cone K' ⊃ K_0 and z ∈ U, the augmented complex of the two-member family X_+ = {z}, X_− = {−z} on K' is exact. If K' ∉ 𝒢 it is zero. If K' ∈ 𝒢:
- By Lemma Z and (G1), some total W ∈ 𝒢 contains K'. Then W contains K' + z or K' − z, so at least one vertex lies in the nerve, by (G0).
- If both vertices lie in it, the edge does too, by (G2).

So the nerve is a vertex or an edge, and the cone lemma applies.

*Inductive step, m(K) > 0.* Pick an undecided z ∈ Z. Consider the double complex
D^{p,q} = ∏_{σ ∈ J^{p+1}, ρ ∈ {±}^{q+1}} A(K + cone X_σ + cone{ρ_0 z, …, ρ_q z}), for p, q ≥ −1,
with commuting deletion differentials in σ and in ρ.
- **Row p** is ∏_σ of the row-lemma complex on K + cone X_σ, hence exact.
- **Column q ≥ 0** is ∏_ρ of C^•(K_ρ), where K_ρ ∈ {K + Q_{≥0}z, K + Q_{≥0}(−z), K + Qz}. The cover hypothesis passes to K_ρ ⊃ K, and m(K_ρ) < m(K) because z is now decided. So these columns are exact by induction.
- **Column q = −1** is C^•(K).

Each total degree involves only finitely many (p, q). Exact rows make Tot D acyclic. The columns q ≥ 0 form a subcomplex whose total complex is acyclic, by filtering by q. The quotient by this subcomplex is column −1, so C^•(K) is exact. ∎

## 6. Proof of #19

1. Apply T with U = Q^gp ⊗ Q, K_0 = K = Q_Q, the family 𝒢 of §3, and the family (X_i)_{i∈J'} for any finite J' ⊃ J_0. The cover hypothesis holds by Lemma 3.
2. By Lemma 2, N(Q_Q) is the full subcomplex N_τ(J') of N_τ on J'. Hence the augmented ordered cochain complex of N_τ(J') with coefficients A is exact, for every A.
3. *Nonemptiness.* Take W_0 ⊃ Q_Q total with lin W_0 = 0. Then W_0 ∈ 𝒢 by (G3) and (G1). It contains some X_i, so K_i ⊂ W_0, so {i} ∈ N_τ by (G0).
4. *Exactness of the chain complex of N_τ(J').* Let C̃ be its augmented ordered chain complex, a complex of free abelian groups in degrees ≥ −1. The universal coefficient theorem gives a surjection H^n(Hom(C̃, A)) → Hom(H_n C̃, A). Taking A = H_n C̃ shows H_n C̃ = 0.
5. *Passage to the infinite complex.* The augmented ordered chain complex of N_τ is the directed union over finite J' ⊃ J_0 of these complexes, so it is exact. Its reduced homology, which is simplicial reduced homology, vanishes.
6. *Cochains of N_τ.* An exact complex of free abelian groups bounded below is split, since subgroups of free groups are free. So Hom(–, A) of it is exact, i.e. the augmented ordered cochain complex of N_τ is exact for every A.

This is what steps 3–6 of the chain use. ∎

## 7. Remarks

**Why I departed from the fine-model transfer.** Lemma 1 already turns everything into finitely many sign conditions inside the true cone Q_Q ⊂ Q^gp ⊗ Q. The proof never passes to the fine submonoids P_S. So the round3_q4 obstruction does not arise: no valuation of a smaller monoid that fails to extend ever needs to be covered.

Outer polyhedral models would in fact fail. Take the valuative Q_0 = {x > 0} ∪ {x = 0, y ≥ 0}. Every rational polyhedral cone containing it also contains −(0,1), which creates spurious lineality.

**Consistency with #15.** The argument reproves the fine case (#15, Steps 2–4) without Lemma K's tangent-cone induction and without the nerve theorem.

**Possible gap in the chain, outside #19 (flagged, not resolved).** A birhizomic cover need only have f.p. members among those that serve as birhizomic witnesses. Chain step 5 asserts that all members of a covering of an f.p. object are f.p. To support that, one should either restrict to the subfamily of witnesses, which is itself a birhizomic cover with all members f.p., and argue with sieves, or check this point separately.

## 8. Status

- **Proved:** #19 exactly as stated, in the stronger form of §0. Every step has its proof written out here, apart from the standard facts listed next.
- **Standard facts used, not reproved:**
  - Tychonoff's theorem;
  - the double-complex comparison (a double complex in the region p, q ≥ −1 with exact rows has an acyclic total complex);
  - the universal coefficient theorem for complexes of free abelian groups;
  - ordered chains compute simplicial homology.
- **Open within this file:** nothing for #19. The chain-level f.p.-membership point in §7 is outside the statement of #19 and is left unchecked here.

=== END OF ANSWER round4_q7 ===
