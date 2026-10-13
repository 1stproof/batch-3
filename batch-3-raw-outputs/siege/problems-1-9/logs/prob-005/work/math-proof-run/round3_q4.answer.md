# round3_q4 — partial answer (the main question is still open)

Conventions are those of (B1)/(B2). Normalized form: x, y are nonzero, 1 ∈ x ⊞ y, and T = x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ xy. The goal is 1 ∈ T, or equivalently 0 ∈ T ⊞ (-1).

## 1. Coincidences in the class a ⊞ -a = H (proved)

Let H be a hyperfield with a ⊞ -a = H for every a ≠ 0.

**Lemma 1.** Let S be a multi-sum whose summands include two nonzero opposite elements a and -a. Then S = H.

*Proof.* Write S = (a ⊞ -a) ⊞ R = H ⊞ R. We have H ⊞ r = H for every element r: given h, pick h' ∈ h ⊞ -r; by reversibility h ∈ h' ⊞ r. Applying this to each summand of R gives S = H. ∎

**Corollary.** If two of the summands of T ⊞ (-1) are opposite, namely the summands x^3, y^3, xy, xy, xy, -1, then T ⊞ (-1) = H ∋ 0 and the claim holds. So the claim holds whenever one of the following holds:
- x^3 = -y^3,
- x^3 = 1 or y^3 = 1 (opposite to -1),
- xy = 1,
- xy = -x^3, i.e. y = -x^2,
- xy = -y^3, i.e. x = -y^2,
- xy = -xy, which is impossible because -1 ≠ 1.

Only the "generic" case remains, where none of these coincidences occurs. In that case xy ⊞ xy does not contain 0, because 0 ∈ a ⊞ a forces a = -a. So nothing more can be extracted from Lemma 1. I could not settle this generic case.

## 2. A natural family in this class satisfies the claim (proved)

**Construction.** Let G be any abelian group containing an element -1 of order 2. Put H = G ∪ {0}, with 0 neutral, and for nonzero a, b define:
- a ⊞ b = {a, b} if b ≠ -a (in particular a ⊞ a = {a});
- a ⊞ -a = H.

**Claim.** H is a hyperfield.

*Proof.* Every multi-sum is computed as follows. If the nonzero summands contain an opposite pair, the sum is H. Otherwise it is the set of the distinct nonzero summands, or {0} if every summand is 0. This rule gives the same set under every bracketing, so ⊞ is associative. It is also commutative.

Reversibility: suppose c ∈ a ⊞ b with a, b ≠ 0.
- If b = -a, then c is arbitrary, and a ∈ c ⊞ a in each subcase c = 0, c = a, c = -a, or c generic, where c ⊞ a = {c, a}.
- If b = a, then c = a, and a ∈ a ⊞ -a = H.
- Otherwise c ∈ {a, b}. If c = a, then a ∈ a ⊞ -b = {a, -b}. If c = b, then a ∈ b ⊞ -b = H.

The cases where a or b is 0 are trivial. Distributivity holds because multiplication by w maps opposite pairs to opposite pairs. ∎

The sign hyperfield is the case G = {±1}.

**Claim.** The implication holds in this H.

*Proof.* Suppose 1 ∈ x ⊞ y with x, y ≠ 0. Then either y = -x or 1 ∈ {x, y}.
- If y = -x, then x^3 and y^3 are opposite, so T = H.
- If x = 1 or y = 1, then 1 is a summand of T. So T is either H or the set of its summands, and either way 1 ∈ T. ∎

So "union-type" hyperfields in this class satisfy the claim. A counterexample must have sums that are genuinely larger than the set of summands but smaller than H.

## 3. Why the generic case resists (recorded obstacle)

Choosing the element 1 in each factor of x(x ⊞ y) and y(x ⊞ y) gives 1 ∈ x^2 ⊞ xy ⊞ xy ⊞ y^2. Doing it once more gives 1 ∈ x^3 ⊞ x^2y ⊞ xy ⊞ xy ⊞ xy^2 ⊞ y^3. To reach T, the set x^2y ⊞ xy^2 = xy(x ⊞ y) would have to be replaced by its element xy, which is contraction, not containment. This is the same obstacle as (B6) and (B8). The hypothesis a ⊞ -a = H does not help in the generic case, because then no opposite pair occurs among the summands.

## Status

- **Proved:** Lemma 1 and the list of coincidences that make T = H in the class a ⊞ -a = H. Also that the union-type hyperfields of Section 2 (a hyperfield for every G with -1 ≠ 1) satisfy the implication.
- **Open:** the generic case of the class a ⊞ -a = H with -1 ≠ 1. That is: x, y with 1 ∈ x ⊞ y and none of x^3 = -y^3, x^3 = 1, y^3 = 1, xy = 1, y = -x^2, x = -y^2.
- **Open:** part (ii). No counterexample with -1 ≠ 1 was constructed, and no candidate was verified. The headline question remains open.

=== END OF ANSWER round3_q4 ===
