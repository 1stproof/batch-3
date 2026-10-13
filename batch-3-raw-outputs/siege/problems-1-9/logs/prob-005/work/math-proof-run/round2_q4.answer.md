# round2_q4 — partial results only

Neither (i) nor (ii) is settled. Below are proved intermediate lemmas and the exact obstacle.

## (i) Idempotent class (a ⊞ a = {a} for all a)

Normalized hypothesis: x, y nonzero, 1 ∈ x ⊞ y. Target (C): 1 ∈ x^3 ⊞ y^3 ⊞ xy (equivalent to the headline here, since xy⊞xy⊞xy = {xy}).

**Lemma 1.** 1 ∈ x^2 ⊞ xy ⊞ y^2.
Proof. Multiply 1 ∈ x⊞y by x and by y: x ∈ x^2⊞xy, y ∈ xy⊞y^2. Substituting into 1 ∈ x⊞y (merging rule B1, in reverse: 1 ∈ x⊞y ⊆ (x^2⊞xy)⊞(xy⊞y^2)) gives 1 ∈ x^2⊞xy⊞xy⊞y^2 = x^2⊞xy⊞y^2, using xy⊞xy = {xy}. ∎

**Lemma 2.** 1 ∈ x^3 ⊞ y^3 ⊞ x^2y ⊞ xy^2.
Proof. Multiply Lemma 1 by x and y: x ∈ x^3⊞x^2y⊞xy^2, y ∈ x^2y⊞xy^2⊞y^3. Substitute into 1 ∈ x⊞y and use idempotence to merge the repeated terms x^2y, xy^2. ∎

**Obstacle.** Lemma 2 differs from (C) only by having the set x^2y⊞xy^2 = xy(x⊞y) (which contains xy) in place of the single element xy. Membership does not allow contracting a set to one of its elements ("S ⊞ A ⊇ S ⊞ a for a ∈ A" goes the wrong way). So (C) would follow from the extra property: "if 1 ∈ x⊞y then 1 ∈ x^3⊞y^3⊞xy·u holds for u = 1", i.e. that the witness u ∈ x⊞y in Lemma 2/B8 can be chosen to be 1. This holds whenever x⊞y = {1}. I could not prove it in general nor construct a counterexample (which, by B4, needs ≥ 11 elements and must be non-quotient).

## (ii) Class a ⊞ -a = H (a≠0), -1 ≠ 1

Not settled. Note only: if any partial sum of x^3, y^3, xy, xy, xy contains an element and its negative in a way making two opposite summands appear after merging, T = H. No further progress.

## Status
- Proved: Lemmas 1, 2 (idempotent class).
- Open: (C) in the idempotent class; the headline question in class (ii).

=== END OF ANSWER round2_q4 ===
