# round1_q3 — partial answer (question not settled)

**Status:** I found neither a proof nor a counterexample. Below are the proved results, followed by the exact remaining obstacle.

I use the normalized form (B2): given 1 ∈ x ⊞ y, is 1 ∈ T := x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ xy?

## Basic tool (proved)
If a ∈ S (a hypersum) then any multi-sum containing a as one summand is contained in the same multi-sum with S in place of a. This holds by associativity and because sums are unions over choices. It follows that replacing one summand c by a set that contains c can only shrink the target. That is the wrong direction for a proof, but it is used below in the following form: if c ∈ (p ⊞ q), then (… ⊞ p ⊞ q) ⊇ (… ⊞ c).

## Proposition 1 (diagonal case, proved): if 1 ∈ x ⊞ x, then 1 ∈ x^3 ⊞ x^3 ⊞ x^2 ⊞ x^2 ⊞ x^2.
Proof.
1. Multiplying 1 ∈ x ⊞ x by x^2 gives x^2 ∈ x^3 ⊞ x^3.
2. Therefore x^3 ⊞ x^3 ⊞ x^2 ⊞ x^2 ⊞ x^2 ⊇ x^2 ⊞ x^2 ⊞ x^2 ⊞ x^2, choosing x^2 from x^3 ⊞ x^3.
3. Multiplying by x gives x ∈ x^2 ⊞ x^2, so x^2 ⊞ x^2 ⊞ x^2 ⊞ x^2 ⊇ x ⊞ x.
4. Since 1 ∈ x ⊞ x, the target contains 1. ∎

## Proposition 2 (expansion, proved): 1 ∈ x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ w for some w ∈ xy(x ⊞ y).
Proof.
1. From 1 ∈ x ⊞ y we get x ∈ x^2 ⊞ xy and x^2 ∈ x^3 ⊞ x^2y, so x ∈ x^3 ⊞ x^2y ⊞ xy.
2. Similarly y ∈ y^3 ⊞ xy^2 ⊞ xy.
3. Hence 1 ∈ x ⊞ y ⊆ x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ (x^2y ⊞ xy^2), and x^2y ⊞ xy^2 = xy(x ⊞ y). ∎

So the implication holds whenever this witness can be taken to be w = xy, i.e. whenever the element u ∈ x ⊞ y used here can be taken to be 1. In particular it holds whenever x ⊞ y = {1}. For example, this covers hyperfields in which x ⊞ y is a singleton for this pair.

## Remaining obstacle (open)
In general the witness u ∈ x ⊞ y produced by the associativity bracketing need not equal 1. The field proof uses cancellation in the factorisation x^3 + y^3 + 3xy − 1 = (x + y − 1)(x^2 − xy + y^2 + x + y + 1). In a hyperfield, a ⊞ −a may be strictly larger than {0}, so that cancellation is not available.

- A counterexample would have to be a hyperfield that is not a quotient of a field (B3).
- By the run's search (B5), it would also have to be larger than every case covered there: |G| ≤ 8 and G = Z3 × Z3.
- I did not build or analyze the free "closure" hyperfield suggested in the task.

**The question remains open:** is 1 ∈ T forced in every hyperfield (equivalently, can the witness u in Proposition 2 always be taken to be 1)?

=== END OF ANSWER round1_q3 ===
