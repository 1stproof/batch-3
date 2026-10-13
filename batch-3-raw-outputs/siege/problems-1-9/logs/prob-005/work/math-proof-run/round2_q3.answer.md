# round2_q3: attempt at a counterexample via the exponent-3 route

## What this file contains
I did not find a counterexample, and I did not prove that the exponent-3 route is impossible. Below are a check of (B10), one new proved constraint on any counterexample in that class, and a record of a failed construction.

## 1. Check of (B10) (proved)
Assume -1 = 1 and g^3 = 1 for every g in G. Put x^3 = y^3 = 1 and w = xy. Then T = 1 ⊞ 1 ⊞ w ⊞ w ⊞ w. By reversibility (with -1 = 1), 1 ∈ T if and only if 0 ∈ 1⊞1⊞1⊞w⊞w⊞w = Q ⊞ wQ. That holds if and only if Q ∩ (-wQ) = Q ∩ wQ ≠ ∅. Also y ∈ 1 ⊞ x if and only if 1 ∈ x ⊞ y, so w ranges over x ⊞ x^2. So (B10) is correct.

## 2. New constraint (proved)
**Lemma.** If -1 = 1, then 1 ∈ Q = 1⊞1⊞1 always.

*Proof.* 1 ∈ Q if and only if 0 ∈ 1⊞1⊞1⊞1 = (1⊞1) ⊞ (1⊞1). That holds if and only if (1⊞1) ∩ -(1⊞1) = (1⊞1) ∩ (1⊞1) is nonempty, which is true. ∎

**Corollary.** In the exponent-3 class, a counterexample needs x and w ∈ x ⊞ x^2 with **w ∉ Q and w^{-1} = w^2 ∉ Q**.
- If w ∈ Q, then w = w·1 ∈ wQ (by the Lemma), so w ∈ Q ∩ wQ.
- If w^{-1} ∈ Q, then 1 = w·w^{-1} ∈ wQ and 1 ∈ Q.

Together with (B10), a counterexample in this class also needs 1 ∉ 1 ⊞ 1 and w ≠ 1. In addition, Q must be disjoint from the whole translate wQ. Since 1 ∈ Q, this means wQ must avoid both 1 and w.

## 3. A construction that fails
I wrote G additively as V = F_3^k. The first candidate takes the triangles to be the affine lines {a, b, c} with a+b+c = 0 (a, b, c distinct), together with a ⊞ a = {0}. This addition is single-valued, a ⊞ b = -a-b, and it is **not associative**: (a⊞b)⊞c = a+b-c, but a⊞(b⊞c) = a-b-c.

Adding the degenerate triangles {a, a, c} for c - a in a set D makes a ∈ a ⊞ c. If every sum contains its summands, we are in class (B9d), which cannot give a counterexample. I did not complete an associativity analysis for a partial D.

## Open
- Whether some hyperfield with -1 = 1 and G of exponent 3 has x and w ∈ x ⊞ x^2 with Q ∩ wQ = ∅. By the Corollary, it would need w, w^2 ∉ Q.
- The headline question remains open.

=== END OF ANSWER round2_q3 ===
