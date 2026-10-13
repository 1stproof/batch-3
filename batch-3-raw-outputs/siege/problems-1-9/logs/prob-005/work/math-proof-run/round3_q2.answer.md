# round3_q2: the core claim (C) in characteristic 2 (-1 = 1)

**Status: (C) is NOT settled.** This file proves one thing: chains of 4-point exchanges cannot prove (C) on their own. Such chains are the same as gluing scaled copies of the hypothesis triangle, and a counting argument rules them out. So any proof has to bring in genuinely new auxiliary elements (witnesses). If no proof exists, a counterexample must break the specific configuration described in section 3.

## 1. Exchanges are compositions

Assume -1 = 1. By (B11)(c), "0 ∈ a⊞b⊞c⊞e" holds iff (a⊞b)∩(c⊞e) ≠ ∅, and this relation is symmetric in a, b, c, e.

A 4-point exchange only re-reads this symmetric relation. The only way to *produce* a new 4-term (or longer) relation from triangles is to glue two relations along a shared element t. This is the composition rule (B5): from 0∈A⊞t and 0∈B⊞t, conclude 0∈A⊞B (here -t = t).

So a chain built only from the hypothesis triangles {g, gx, gy} (all g ∈ G, coming from y ∈ 1⊞x), using exchanges, is a "linear derivation" in the sense of (B6).

## 2. Proposition: no linear derivation proves (C) when -1 = 1

**Claim.** No linear derivation proves (C).

**Proof.**
1. Suppose a derivation glues k relations R_w = {w, wx, wy} (monomial labels w; repeats allowed) into a tree with k-1 gluings.
2. Each gluing removes 2 terms. The relations contribute 3k terms, so the final sum has 3k - 2(k-1) = k + 2 terms.
3. The target 0 ∈ 1⊞x^3⊞y^3⊞xy has 4 terms, so k = 2.
4. Two relations R_w and R_{w'} share a term only if w' ∈ {wx, wy, wx^{-1}, wy^{-1}, wxy^{-1}, wyx^{-1}}. Gluing them leaves 4 terms of the form w·{…}.
5. For the result to equal {1, x^3, y^3, xy} as monomials, the exponents would have to match. Checking all 6 cases, none does: the glued 4-sets have total degree spread at most 2, but {1, x^3} has spread 3.

So the derivation is impossible. ∎

**Why the field proof does not transfer.** Over F_2 one has 1+x^3+y^3+xy = (1+x+y)(1+x+y+x^2+xy+y^2). This combines the six relations R_1, R_x, R_y, R_{x^2}, R_{xy}, R_{y^2}, which have 18 terms. Reaching 4 terms needs 7 cancelled pairs, but a tree on 6 relations allows only 5 gluings. Closing the extra cycles would need the inference "0∈C⊞a⊞a ⇒ 0∈C", which is invalid in hyperfields.

The same argument covers the weaker target 1∈T, with T = x^3⊞y^3⊞xy⊞xy⊞xy. That target has 6 terms, so k = 4. The 12 terms of four relations, glued in a tree, would have to give exactly {1, x^3, y^3, xy, xy, xy}. The coefficient polynomial would have to be a degree-2 multiple of (1+x+y) matching the field identity, which needs 6 relations, not 4. So this is impossible too, as in (B6).

**Consequence.** Any affirmative proof must use auxiliary existential elements, such as d ∈ (1⊞1)\{0} or witnesses u ∈ x⊞y with u ≠ 1, together with the axioms they satisfy. Exchange chains alone, which are idea (a) of the task, cannot work.

## 3. What a counterexample would need (exponent-3, char-2 class)

Combining (B10) and (B11), a counterexample in this class needs all of the following:
- 1 ∉ 1⊞1;
- an element x and some w ∈ x⊞x^2 with w ≠ 1;
- w ∉ Q and w^{-1} ∉ Q, where Q = 1⊞1⊞1 = {1} ∪ (1⊞D) and D = (1⊞1)\{0} ≠ ∅;
- Q ∩ wQ = ∅;
- the triangle set must be G-invariant and satisfy the 4-point condition.

I did not build such a hyperfield, and I did not rule one out. The exhaustive search in (B4) suggests any counterexample has at least 11 elements.

## 4. Open questions

- Is (C) true for hyperfields with -1 = 1? This is open.
- Is the original implication true? This is open in general.
- Does the configuration in section 3 extend to an associative hyperfield? This is open.

=== END OF ANSWER round3_q2 ===
