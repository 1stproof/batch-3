# round1_q1 answer: F -> R pi_* pi^{-1} F

## Status
Expected answer: **YES**. What follows is a reduction and a sketch, not a complete proof. The full statement is still open in this file.

## Reduction (proved, apart from the standard slice facts)
1. id_P is terminal in both A_P^op and B_P^op.
2. For y = P[-x]^sharp, the slice A_P^op/y is A_y^op, and the slice B_P^op/y is B_y^op: an object P[-x']^sharp under y is y[-x']^sharp. Restricting to a slice commutes with pi^{-1}, pi_* and R pi_*.
3. So it is enough to show two things for every monoid P:
   - (i) H^0(A_P, pi^{-1}F) = F(P);
   - (ii) H^i(A_P, pi^{-1}F) = 0 for i > 0.
   Here the cohomology is taken at the terminal object, and the trivial topology on B_P gives F(P) with no higher cohomology on the B side.

## Sketch for fine P (not verified)
- Take sigma = Hom(P, R_{>=0}). Log modifications coming from subdivisions Sigma of sigma should be birhizomic covers. Such a cover should be cofinal among the covers of P, using valuative points and finite presentation.
- On such a cover, pi^{-1}F should be represented by c -> F(r(c)), where r(c) is the smallest face of sigma containing the cone c.
- Then the Čech/derived limit over Sigma^op should be computed by Quillen's Theorem A. For each face tau, the set of cones c with r(c) containing tau forms a poset whose realization is the open star of relint(tau). This star is convex, hence contractible. So the derived limit is F(sigma) = F(P), concentrated in degree 0.
- Passing to the colimit over subdivisions should then give (i) and (ii).

## Non-fine P (not done)
The idea is to write P as a filtered colimit of fine saturated sharp submonoids. One would need to check that A_P, B_P and the birhizomic covers commute with this colimit; the finite-presentation clause in the definition of "birhizomic" suggests they do. This step is not done.

## Open gaps
1. Show that subdivision covers are cofinal among birhizomic covers. This needs the characterization of infinitesimal maps into valuative monoids.
2. Identify the sheaf pi^{-1}F on a subdivision.
3. Carry out the colimit argument for general P.

=== END OF ANSWER round1_q1 ===
