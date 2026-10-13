# round2_q1 — answer (partial; core claim not settled)

## Status
I could not prove (C), or the headline implication, for all hyperfields with -1 = 1. I also could not build a counterexample. Below are the checks and the small partial results that I did prove.

## Checks of the background
- (B9)(b) holds. If -1 = 1, then 0 ∈ xy ⊞ xy. So xy ⊞ xy ⊞ xy ⊇ xy ⊞ 0 = {xy}, and therefore T ⊇ x^3 ⊞ y^3 ⊞ xy.
- 1 ∈ Q := 1 ⊞ 1 ⊞ 1 always holds when -1 = 1, since 0 ∈ 1 ⊞ 1 gives Q ⊇ 1 ⊞ 0 = {1}.
- (B10) holds. Take g^3 = 1 for all g ∈ G and -1 = 1. Then x^3 = y^3 = 1 and T = 1 ⊞ 1 ⊞ wQ, where w = xy. We have 1 ∈ T ⇔ 0 ∈ 1 ⊞ 1 ⊞ 1 ⊞ wQ ⇔ Q ∩ wQ ≠ ∅, because -a = a, so 0 ∈ A ⊞ B ⇔ A ∩ B ≠ ∅. Reversibility gives y ∈ 1 ⊞ x, so w ∈ x ⊞ x^2.

## Partial results (proved)
**P1 (exponent 3, w ∈ Q).** In the setting of (B10), if w ∈ Q or w^{-1} ∈ Q, then 1 ∈ T.
Proof. If w ∈ Q: 1 ∈ Q gives w ∈ wQ, so w ∈ Q ∩ wQ. If w^{-1} ∈ Q: 1 ∈ Q gives w ∈ wQ, and w·w^{-1} = 1 ∈ Q; also 1 ∈ wQ, since 1 = w·w^{-1} with w^{-1} ∈ Q. So 1 ∈ Q ∩ wQ. ∎
So an exponent-3 counterexample needs an x and a w ∈ x ⊞ x^2 with w ∉ Q, w^{-1} ∉ Q and Q ∩ wQ = ∅. In particular w ≠ 1, and Q must be a proper subset of H.

**P2.** If x ⊞ y = {1}, the claim holds by (B8). If a ⊞ a = H for all a ≠ 0, it holds by (B9)(a).

## Remaining obstacle (open)
- Main open question: (C) "1 ∈ x ⊞ y ⇒ 1 ∈ x^3 ⊞ y^3 ⊞ xy" when -1 = 1. The weaker target, 1 ∈ T, is also open.
- Specific gap: (B8) gives 1 ∈ x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ xy·u for some u ∈ x ⊞ y. Proving the claim needs a u that also lies in Q = 1 ⊞ 1 ⊞ 1. I found no axiom-based way to move u into Q.
- Counterexample search: in the exponent-3 case, by P1 one should look for 1 ∉ 1 ⊞ 1 with Q small. One should also look for a G-invariant triangle system in which x ⊞ x^2 avoids Q ∪ Q^{-1} and avoids every w with Q ∩ wQ ≠ ∅. This search was not carried out.
=== END OF ANSWER round2_q1 ===
