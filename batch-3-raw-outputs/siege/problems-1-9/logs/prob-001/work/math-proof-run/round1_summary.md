# Running summary after round 1 planning (no results yet)

## Goal
The problem fixes the claim: for every monoid P (integral, saturated, sharp; not assumed finitely generated) and every presheaf of abelian groups F on B_P^op, is F -> R pi_* pi^{-1} F a quasi-isomorphism? Ledger [GOAL] line states the YES claim; a counterexample would make it REFUTED.

## Established
Nothing yet (round 1; no result files).

## Director's unverified heuristics (not established)
- A_P^op has terminal object id_P, and P lies in B_P; on B_P^op (trivial topology) RGamma of F = F(P). For objects P[-x]^sharp the question reduces to the same question for that monoid. So the claim amounts to: pi^{-1}F has sections F(P) at P and no higher cohomology there, for all P.
- Saturated sharp => P^gp torsion-free and the order extends to a total order, so a valuation with v^{-1}(0)=0 always exists; covers by localizations P[-x]^sharp are trivial.
- For fine P: faces of dual cone sigma <-> objects of B_P; covers ~ subdivisions; expected finite-poset lemma: R lim over Sigma^op of F(r(c)) = F(sigma) by Quillen A/convexity. Suggests YES for fine P.
- Least certain: non-finitely-generated P (quasi-compactness, colimit arguments, non-principal faces), and the role of higher-rank valuations / infinitesimal maps.

## Dead ends
None yet.

## Open gaps
1. Concrete characterization of infinitesimal maps, birhizomic morphisms, covers, points/stalks.
2. Degree-0: pi^{-1}F(P[-x]^sharp) = F(P[-x]^sharp).
3. Higher-degree vanishing for fine P (finite-poset lemma + reduction to subdivisions).
4. General (non-fg) P: proof or counterexample.

## Next round (round 1 wave)
Exploration: q1 full proof attempt (points/base change), q2 foundational lemmas L1-L5, q3 counterexample hunt (N, N^2, non-fg monoids), q4 combinatorial core + reduction for fine P.
