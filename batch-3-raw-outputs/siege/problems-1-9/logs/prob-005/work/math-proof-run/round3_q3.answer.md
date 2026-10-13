# round3_q3: attempt on the normalized claim 1 ∈ x ⊞ y ⇒ 1 ∈ T = x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ xy

**Status: not settled.** Nothing below proves or refutes the headline question. What follows is the analysis of routes (a)–(c) and why each one stalls, plus one small precise observation.

## Route (a): the symmetric form with a multiplier c
Let c be any single element. Distributivity gives 0 ∈ cx ⊞ cy ⊞ cz exactly. To relate this relation to the target, cx, cy, cz must be replaced by sums. Suppose c ∈ x^2 ⊞ y^2 ⊞ z^2 ⊞ -xy ⊞ -yz ⊞ -zx. Then cx lies in the sum x^3 ⊞ xy^2 ⊞ xz^2 ⊞ -x^2y ⊞ -xyz ⊞ -x^2z, and similarly for cy and cz.

Substituting these memberships into 0 ∈ cx ⊞ cy ⊞ cz gives 0 ∈ S18. Here S18 is the 18-term sum whose terms are the three cubes, three copies of -xyz, and the six cross pairs m ⊞ -m (m ∈ {x^2y, xy^2, x^2z, xz^2, y^2z, yz^2}).

To reach the target we would need the step 0 ∈ C ⊞ m ⊞ -m ⇒ 0 ∈ C, which fails in general (B5). Choosing c inside a different auxiliary sum (x ⊞ -y, x^2 ⊞ -yz, ...) gives the same pattern: every exact substitution adds terms, and nothing allows them to be removed. Removal is possible only through (B5), which needs a *single* element t together with a separate relation for -t. The cross pairs m ⊞ -m arise inside one relation, not in two separate ones, so (B5) does not apply. **Dead end** for any choice of a single multiplier c.

## Route (b): moving the witness
From (B8) we get 1 ∈ x^3 ⊞ y^3 ⊞ xy ⊞ xy ⊞ xyu with u ∈ x ⊞ y. Apply (B8) again to 1 ∈ u^{-1}x ⊞ u^{-1}y. This produces a relation with terms u^{-3}x^3, u^{-3}y^3, u^{-2}xy (twice) and u^{-2}xy·u' with u' ∈ u^{-1}(x ⊞ y).

To combine the two relations by (B5), they must share a single element t, appearing as t in one and as -t in the other. The only candidates are the witness terms, and these have different degrees in u, so no common t exists unless u' = u^{-1}·u, i.e. u' = 1. Requiring u' = 1 is exactly the original problem again. **No progress.**

## Route (c): certificates
I did not construct a consistent partial hyperfield with 1 ∈ x ⊞ y and 1 ∉ T. Per (B4) and (B13c), any such configuration needs at least 11 elements and a non-quotient structure. In the exponent-3 class with -1 = 1, (B10)–(B11) reduce the search to the following statement:

> Find G ∪ {0} with -1 = 1, every g ∈ G satisfying g^3 = 1, satisfying the four-point condition, and containing x and w ∈ x ⊞ x^2 with w, w^{-1} ∉ Q = 1 ⊞ 1 ⊞ 1 and Q ∩ wQ = ∅.

## Small observation (proved)
Every derivation of 0 ∈ (target) from 0 ∈ x ⊞ y ⊞ z that only uses
- exact distributivity with single multipliers,
- substitution of memberships into sums, and
- (B5) cancellation with single elements

ends in a sum that *contains* the target's terms as a sub-multiset. To conclude, it would therefore need a contraction or cancellation step that is not available. This extends (B6): auxiliary multipliers c alone do not escape the obstruction. A proof would have to use reversibility to create new relations, not only substitutions.

## Open
- The headline question.
- The core claim (C) for -1 = 1.
- The exponent-3 search problem stated in route (c).

=== END OF ANSWER round3_q3 ===
