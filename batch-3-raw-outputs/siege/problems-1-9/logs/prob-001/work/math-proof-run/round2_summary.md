# Running summary after round 2 planning

## Goal
The problem fixes the claim (ledger #1, OPEN [GOAL]): for every monoid P (integral, saturated, sharp; NOT assumed finitely generated) and every presheaf of abelian groups F on B_P^op, F -> R pi_* pi^{-1} F is a quasi-isomorphism. Answer YES = PROVED, counterexample = REFUTED.

## Round 1 results (all four answers were thin; none settles anything major)
- round1_q1: reduction only. id_P is terminal in A_P^op and B_P^op; the slice of A_P^op over P[-x]^sharp is A_{P[-x]^sharp}^op and similarly for B; so the claim is equivalent to: for every P and F, H^0(A_P, pi^{-1}F) = F(P) and H^i = 0 for i > 0 (cohomology at the terminal object). Its fine-P sketch relied on subdivision (closed chart) covers, which is now known to be wrong (see R3 below).
- round1_q2: proved Lemma L1: for M valuative, f : M -> N is infinitesimal iff f^{-1}(0) = {0} (iff f^gp injective). The proof's (=>) part shows in general that an infinitesimal map kills no nonzero element of its source. Quotient Z^2_lex -> Z is not infinitesimal. L2-L5 not settled.
- round1_q3: proved N -> 0 is birhizomic at the zero map; claimed (unchecked) that covers of N are trivial so the claim holds for P = N. Nothing on N^2 or non-fg monoids.
- round1_q4: proved Part A (finite-poset lemma): for a fan Sigma subdividing sigma, R lim_{Sigma^op} G o r = G(sigma) in degree 0 (Quillen A + star-shaped complements; quotes Theorem A and a regular-CW deformation-retract fact from memory). Part B (reduction of birhizomic cohomology to subdivisions) not done -- and per R3 it is false as stated.

## Director's own checks made in round 2 planning (hand proofs; recorded as OPEN in the ledger until a worker confirms)
- R2: every finitely presented P -> Q is birhizomic at the zero map Q -> V (infinitesimal p kills nothing nonzero, so h = 0 and u = 0 uniquely); P -> P[-x]^sharp is birhizomic at every g. So the zero valuation lies in every "open" U_Q.
- R3: closed subdivision charts are NOT birhizomic at wall valuations: P = N^2, Q = <e2, e1-e2>, g(e2)=1, g(e1-e2)=0; test object M = {x in Z^2 : x1+x2 > 0} u {0} with p = x1+x2 is infinitesimal, h = inclusion, and no u exists. The round-1 heuristic "covers = subdivisions" is dead.
- R4: "open-cone" neighbourhoods are birhizomic: Q = sat(P + <a_1..a_k>) with v(a_i) > 0 and a_i = b_i - c_i, v(b_i + c_i) prec v(a_i) (automatic at archimedean V) is sharp and P -> Q is birhizomic at the extension of v (u = h^gp|_Q). So neighbourhoods of an interior rank-one valuation are dual to rational cones containing it in their interior.
- R5 (heuristic only): the birhizomic topos looks like sheaves on a space of valuations in which face objects P[-x]^sharp are open, the zero valuation is in every nonempty open, interior rank-one points have open-cone neighbourhoods, and rank-two points (e.g. v(e1)=1, v(e2)=eps on N^2) have neighbourhoods all containing a boundary point; they glue faces to the interior. A heuristic H^0 computation for N^2 with F concentrated at a ray is consistent with YES. Stalk of pi^{-1}F at v expected: colim over x with v(x)=0 of F(P[-x]^sharp).

## Dead ends
- Covers by closed charts of subdivisions of the dual cone (R3): not birhizomic covers, so the finite-poset lemma (#5) is not directly the computation; it may still be useful in a different guise.

## Open gaps
1. Characterize birhizomic morphisms (role of the prec condition at higher-rank valuations), covers, quasi-compactness, points and stalks (#8).
2. The claim for fine P (devissage to F concentrated at a single face; N^2 completely first) (#8).
3. Non-finitely-generated P: valuative P of rank >= 2 and non-fg rank 1, N^(infinity) (non-principal faces), irrational cones, Q_{>=0}^2. Prime suspect for a counterexample if there is one.
4. A structural proof for all P (injective co-skyscraper resolutions on the face poset; identify pi^{-1} of a co-skyscraper as pushforward of a constant sheaf from the slice site; cohomology of constant sheaves).

## Next round (round 2 wave, 4 attempt queries, each carrying the background R0-R6 inline)
- q1: classify birhizomic morphisms/covers/points/stalks; compute H^0, H^1 for N^2.
- q2: prove the claim for fine P (devissage + N^2 + general convexity argument).
- q3: counterexample hunt / verdicts for non-fg and valuative P (rank-2 lex, Q_{>=0}, N^(infinity), irrational cone, Q_{>=0}^2).
- q4: structural proof for all P via co-skyscraper injectives and constant-sheaf cohomology.
Later: once a candidate full proof appears, send two verify queries; check whether R2-R4 are confirmed by workers and record them as PROVED.
