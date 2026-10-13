# Round 1 summary (no results yet)

## Established
Nothing yet: round 1 is the first planning step; no result files exist.

## Planner's working picture (heuristic, unverified)
Notation: cycle a_0=c_1, a_1=f(c_1), a_2, a_3; A={a_0..a_3}; B=A∪{v}; critical values a_1, v.
- G = {φ ∈ PMod(S^2,B): some lift φ~ fixes A and φ~ = i(φ) in PMod(S^2,A)} preserves D_f.
- W = image of D_f in M_{0,5}; G acts transitively on fibers of D_f → W; components ↔ G/G_0, G_0 = stabilizer of a component = image of π_1(W) → PMod(S^2,B). Orbit of a component under ⟨φ⟩ infinite iff no nonzero power of φ in G_0.
- γ around {v,a_j}, j∈{0,2,3}: T_γ^2 lifts to a twist about a curve peripheral rel A, so T_γ^2 ∈ G. But punctures of W where f(c_2)=a_j give loops whose monodromy is a power of such a twist (for the specific "short" curve of that degeneration), so those curves give FINITE orbits. The answer curve must be different (other arc, two cycle points, or both critical values).
- Candidate obstruction: image of H_1(W) in H_1(M_{0,5}) ≅ Z^5 not containing the twist class rationally.
- Literature: Hironaka–Koch, "A disconnected deformation space of rational maps" (recollection only).

## Open gaps
All of: explicit γ; T_γ^k ∈ G; no power in G_0.

## Next round
Round 1 wave (4 attempt queries, all at the goal): q1 full attempt via abelianization; q2 explicit computation of Per_4(0), W, punctures, H_1 image; q3 combinatorial curve-lifting classification with a concrete model map; q4 structural facts + i_*|D_f local biholomorphism picture + infinite-orbit criterion.
