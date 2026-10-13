# round4_q4 — answer

**Verdict: COUNTEREXAMPLE to (N).** This also answers the original question: **NO**.

The counterexample is an infinite (countable) Krasner-type hyperfield with -1 = 1. Its underlying geometry is a projective plane on which the infinite cyclic group Z acts regularly. The plane is built from a perfect difference set D ⊂ Z that is constructed greedily, with three incidences forced and one non-incidence protected. Every hyperfield axiom is verified below for all triples. The target sum is computed exactly.

## 1. Perfect difference set D ⊂ Z

**Definitions.** A set A ⊂ Z is *Sidon* if every nonzero integer has at most one representation d1 − d2 with d1, d2 ∈ A. A set D is a *perfect difference set* if every nonzero integer has exactly one such representation.

**Lemma 1 (extension step).** Let A ⊂ Z_{≥0} be a finite Sidon set with 0 ∈ A, and let m ≥ 1 with m ∉ A − A. Let x > 2·max A + m. Then A ∪ {x, x+m} is Sidon.

*Proof.* Put W = max A. Every old nonzero difference has absolute value at most W. The positive new differences are:
- m, which is not an old difference since m ∉ A − A;
- x − a for a ∈ A;
- x + m − a for a ∈ A.

The values x − a and x + m − a are all greater than W + m. So they differ from every old difference and from m.

Among the new positive values:
- x − a = x − a' forces a = a';
- x + m − a = x + m − a' forces a = a';
- x − a = x + m − a' forces a' − a = m, which is impossible because m ∉ A − A.

The negative new differences are the negatives of these values, so they are distinct for the same reasons. ∎

**Construction.** Start with A_0 = {0, 1, 7, 100, 103, 108}.

A_0 is Sidon. Its positive differences are:
- 1, 7, 6 within {0, 1, 7};
- 3, 8, 5 within {100, 103, 108};
- 100 + s − f for s ∈ {0, 3, 8} and f ∈ {0, 1, 7}. The values s − f are 0, −1, −7, 3, 2, −4, 8, 7, 1. These are pairwise distinct, so these differences are the nine distinct numbers 93, …, 108.

All 15 positive differences are distinct.

For each k:
- let m_k be the least positive integer not in A_k − A_k;
- let x_k := 2·max A_k + m_k + 1;
- let A_{k+1} := A_k ∪ {x_k, x_k + m_k}.

By Lemma 1 each A_k is Sidon. Put D := ∪_k A_k. Then D is Sidon, since any two representations of a difference already lie in some A_k.

The sequence m_k is strictly increasing. Indeed, every positive integer ≤ m_k lies in A_{k+1} − A_{k+1}, so m_{k+1} > m_k. Hence every positive integer, and by symmetry every nonzero integer, is a difference of D. So D is a perfect difference set.

All the added elements are at least x_0 = 2·108 + m_0 + 1 > 121. Since 121 ∉ A_0, it follows that **121 ∉ D**, while **0, 1, 7, 100, 103, 108 ∈ D**.

## 2. The projective plane Π

The points of Π are the integers. The lines are the translates D + n for n ∈ Z, and a point p lies on D + n iff p − n ∈ D.

**Two distinct points p, q lie on exactly one line.** We need p − n, q − n ∈ D. This holds iff (p − n) − (q − n) = p − q is a difference d1 − d2 of D with n = p − d1. That difference has exactly one representation, so n is unique.

**Two distinct lines D + m and D + n meet in exactly one point.** A common point p has p − m = d1 and p − n = d2, so d1 − d2 = n − m ≠ 0. That representation is unique, so p is unique.

Every line is infinite. Translations p ↦ p + k map lines to lines.

Write ℓ(p, q) for the line through p ≠ q.

## 3. The hyperfield H

**Elements and multiplication.** Write the group G = Z multiplicatively as {t^n : n ∈ Z}, and put H = G ∪ {0}. Multiplication is t^m · t^n = t^{m+n}, with 0 absorbing. The point n of Π is identified with t^n, so multiplying by t^k is the translation by k.

**The element −1.** We take −1 := 1.

**Addition (every pair).** For a, b ∈ G:
- 0 ⊞ a = a ⊞ 0 = {a}, and 0 ⊞ 0 = {0};
- a ⊞ a = {0, a};
- a ⊞ b = ℓ(a, b) \ {a, b} for a ≠ b.

**Axioms.**
- *Commutativity and nonemptiness:* clear from the definition.
- *0 is neutral:* by definition.
- *Unique negatives:* 0 ∈ a ⊞ b iff a = b. For a ≠ b, the set ℓ(a, b) \ {a, b} contains no 0. And 0 ∈ 0 ⊞ b = {b} iff b = 0.
- *Distributivity:* multiplying by w ∈ G is a collineation. It maps {0, a} to {0, wa} and ℓ(a, b) \ {a, b} to ℓ(wa, wb) \ {wa, wb}. Multiplying by w = 0 gives {0} = 0 ⊞ 0 on both sides.
- *Reversibility.* We must show c ∈ a ⊞ b ⇒ a ∈ c ⊞ (−b) = c ⊞ b.
  - If a = 0, then c = b, and 0 ∈ b ⊞ b.
  - If b = 0, then c = a, and a ∈ a ⊞ 0.
  - If a = b ≠ 0, then c ∈ {0, a}, and both a ∈ 0 ⊞ a and a ∈ a ⊞ a hold.
  - If a ≠ b are both nonzero, then c ∈ ℓ(a, b) \ {a, b}. So c ⊞ b = ℓ(a, b) \ {c, b}, which contains a.

**Associativity, reduced to a 4-point condition.** Put P(a, b, c, e) :⇔ (a ⊞ b) ∩ (c ⊞ e) ≠ ∅.

By reversibility with −c = c, we have e ∈ t ⊞ c ⇔ t ∈ c ⊞ e. Hence:
- e ∈ (a ⊞ b) ⊞ c ⇔ P(a, b, c, e);
- e ∈ a ⊞ (b ⊞ c) = (b ⊞ c) ⊞ a ⇔ P(b, c, a, e).

So associativity follows once P is invariant under all permutations of its four arguments. I prove this by showing that P(a, b, c, e) equals a symmetric predicate Z of the multiset of the *nonzero* entries.

**Definition of Z.**
- Z(∅) is true.
- Z({p}) is false.
- Z({p, q}) holds iff p = q.
- Z({p, q, r}) holds iff p = q = r, or p, q, r are distinct and collinear.
- Z of a 4-multiset is given by the following table:
  - {p, p, p, p} and {p, p, q, q}: true.
  - {p, p, p, q}: false.
  - {p, p, q, r} with p, q, r distinct: true iff p, q, r are collinear.
  - {p, q, r, s} all distinct: true iff all four are collinear or no three are collinear.

**Check, all entries nonzero.** Two facts are used:
- if a ≠ b and c ≠ e with ℓ(a, b) = ℓ(c, e), the intersection is a line minus at most 4 points, hence nonempty;
- if the two lines are different, they meet in a single point t, and the intersection is {t} or ∅ according to whether t ∉ {a, b, c, e}.

Case by case:
- *{p, p, q, q}.* The pairing (pp)(qq) gives {0, p} ∩ {0, q} ∋ 0. The pairing (pq)(pq) gives the same line on both sides. Both are true.
- *{p, p, p, q}.* The only pairing type gives {0, p} ∩ (ℓ(p, q) \ {p, q}) = ∅. False.
- *{p, p, q, r}.*
  - (pp)(qr): {0, p} ∩ (ℓ(q, r) \ {q, r}) is nonempty iff p ∈ ℓ(q, r).
  - (pq)(pr): if p, q, r are collinear, it is the same line, so true. Otherwise the two lines meet only at p, which is excluded, so false.
- *Four distinct points.*
  - If all four are collinear, every pairing is the same line, so true.
  - If exactly three are collinear, say p, q, r on L and s ∉ L, then in each pairing the two lines meet at one of p, q, r, which is excluded. False.
  - If no three are collinear, each intersection point is not among the four points. True.

**Check, some entries 0.**
- *One zero,* say e = 0: P = [c ∈ a ⊞ b], which is exactly Z({a, b, c}). Other positions reduce to this by symmetry.
- *Two zeros:* {0} ∩ (c ⊞ e) ≠ ∅ iff c = e, and {b} ∩ {e} ≠ ∅ iff b = e. Both agree with Z.
- *Three zeros:* the intersection is ∅.
- *Four zeros:* the intersection is {0}.

So P is symmetric, and ⊞ is associative. H is a hyperfield.

## 4. The counterexample

Take x = t, y = t^7, z = 1 (= −1). Then xy = t^8, x³ = t^3, y³ = t^21, and −xyz = xyz = t^8.

**Hypothesis.** The points 0, 1, 7 are distinct and lie on the line D. So 0 ∈ x ⊞ y ⊞ z. In normalized form, 1 ∈ x ⊞ y.

**Target.** Put S := x³ ⊞ y³ ⊞ z³ ⊞ xyz ⊞ xyz ⊞ xyz = t^3 ⊞ t^21 ⊞ 1 ⊞ t^8 ⊞ t^8 ⊞ t^8.

First, t^8 ⊞ t^8 ⊞ t^8 = {0, t^8} ⊞ t^8 = {t^8} ∪ {0, t^8} = {0, t^8}. Hence

S = (t^3 ⊞ t^21 ⊞ 1) ∪ (t^3 ⊞ t^21 ⊞ 1 ⊞ t^8).

- **First part.** 0 ∈ t^3 ⊞ t^21 ⊞ 1 iff the points 3, 21, 0 are collinear.
  - The unique line through 0 and 3 is D − 100, because 100 and 103 lie in D.
  - The point 21 lies on D − 100 iff 121 ∈ D, which is false.

  So 0 is not in the first part.
- **Second part.** 0 ∈ A ⊞ B ⊞ C ⊞ E iff (A ⊞ B) ∩ (C ⊞ E) ≠ ∅, because 0 ∈ s ⊞ s' iff s = s'. So 0 lies in the second part iff Z({3, 21, 0, 8}) holds.
  - The points 0, 3, 8 lie on D − 100, because 100, 103 and 108 lie in D.
  - The point 21 is not on that line.

  So exactly three of the four distinct points are collinear, Z is false, and 0 is not in the second part.

Hence **0 ∉ S**.

Equivalently, for (N): 1 ∈ x ⊞ y but 1 ∉ x³ ⊞ y³ ⊞ xy ⊞ xy ⊞ xy. With −1 = 1, if 1 were in that sum then 0 would lie in it ⊞ 1, which is S.

## 5. Remarks

- **What the claim says in this class.** For every Krasner-type hyperfield built from a projective plane with a regular abelian collineation group, the claim reduces to an incidence statement: if 1, x, y are collinear, then {1, x³, y³, xy} is not a set of four distinct points with exactly three of them collinear (unless 1, x³, y³ are collinear). In Desarguesian planes this holds by the cubic identity. A free-style construction of a non-Desarguesian plane with a regular Z-action breaks it.
- **Consistency with the background.** H is infinite, which fits the search result (C1) that there is no counterexample with at most 10 elements. The question of a *finite* counterexample is left open. Every finite abelian planar difference set known is Desarguesian.
- **What was used from the background.** Only the normalization (A2) and the equivalence in (A5)(c) are used, and the latter is re-proved in §3. Nothing else is assumed.

=== END OF ANSWER round4_q4 ===
