# Round 4 summary (after folding rounds 1-3)

## Problem / goal
Decide: in every hyperfield, does 0 ∈ x⊞y⊞z imply 0 ∈ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz? Ledger [GOAL] (#1): the universal claim, OPEN. The problem poses the claim: a proof, or a verified explicit counterexample (REFUTED), settles the run.

## Normal form and coordinator facts (elementary; re-prove in proof.md if used)
- z = 0 trivial; for z ≠ 0 scale by -1/z: equivalent to "1 ∈ x⊞y ⇒ 1 ∈ T := x^3⊞y^3⊞xy⊞xy⊞xy", x, y nonzero.
- Quotients F/U satisfy it; the class satisfying it is closed under quotients H/U. Counterexample must be non-quotient.
- Coordinator computer search (unrefereed, /tmp/hf/s2.py): no counterexample with |G| ≤ 9. Coordinator check (/tmp/hf3/chk.py): subgroup-triangle families on F_3^k (k ≤ 3) trivial.
- Coordinator lemma (B11c,d): with -1 = 1, associativity ⇔ 4-point symmetry "(a⊞b)∩(c⊞e) ≠ ∅ ⇔ (b⊞c)∩(a⊞e) ≠ ∅"; if 1⊞1 = {0} (and -1 = 1) H is a field.
- Exponent-3, -1 = 1 hyperfields exist beyond fields: e.g. the quotient F_4((t))^*/(cubes) has G ≅ F_3^2 (it satisfies the claim, being a quotient).

## Standing results
- #2 (round1_q1): composition rule; linear-derivation obstruction.
- #3 (round1_q3): diagonal case y = x; witness expansion 1 ∈ x^3⊞y^3⊞xy⊞xy⊞w, w ∈ xy(x⊞y).
- #4 (round1_q4): -1 = 1 ⇒ goal follows from (C); idempotent ⇒ goal ⇔ (C); goal holds when -1 = 1 and a⊞-a = H.
- #7 (round2_q3): exponent-3 reduction (B10) with constraints on w.
- #8 (round2_q4): idempotent-class lemmas.
- round3_q4 (new, proved): in the class a⊞-a = H (all a ≠ 0), any multi-sum containing two opposite nonzero summands is H, so the claim holds unless the generic case; union-type hyperfields (a⊞b = {a,b} for b ≠ -a, a⊞-a = H, any G with -1 ≠ 1) are hyperfields and satisfy the claim.
- round3_q1 (new, proved): exact translation of the exponent-3, -1 = 1 class into translation-invariant triangle systems Δ on F_3^k with 4-point condition; linear derivations fail there too (integer-multiplicity obstruction, generic case).
- round3_q2 (new, proved): with -1 = 1, chains of 4-point exchanges are compositions; no linear derivation proves (C) or 1 ∈ T.
- round3_q3 (new, observation): derivations using single multipliers, substitutions and (B5) always end in a sum containing the target's terms as a sub-multiset; cannot contract.

## Dead ends (each only as a closed candidate, not a refuted route)
No REFUTED ledger line exists; hence no route is dead in the strict sense. Closed candidates (set aside, not refuted):
- Linear/compositional derivations (round1_q1, round3_q1, round3_q2, round3_q3: proved impossible as a method).
- Iterated witness moving (round2_q2, round3_q3 route b); symmetric form with a multiplier c (round3_q3 route a).
- Single-valued affine-line rule on F_3^k (round2_q3); subgroup-triangle families (coordinator); Krasner extensions (round1_q2); union-type hyperfields (round3_q4); sums-contain-summands classes; |G| ≤ 9 search.
- round1_q2 (proved, small): Krasner extensions give T = (x^3⊞y^3) ∪ (x^3⊞y^3⊞xy); the one-line Krasner family satisfies the claim apart from one sketched step.

## Coordinator computations this round (unrefereed; scripts in /tmp/hf4: gen.py, solve.c, srch.py, insp2.py)
- Exponent-3, -1 = 1 triangle systems: exhaustive searches found no counterexample on F_3^3 (translation + ±1 symmetry, using GL-transitivity to fix x = e1, w ∈ {e1, 2e1, e2}), on F_3^3 with the order-13 or full F_27^* multiplicative symmetry, and on F_3^4 with F_81^* symmetry. A search on F_3^3 with translation symmetry only was still running when this summary was written.
- Every non-field associative system enumerated (F_3^2, F_3^3, various symmetries) with 1 ∉ 1⊞1 has Q = 1⊞1⊞1 ⊇ G. So small groups are too "dense". A counterexample in this class needs |Q| ≤ |G|/2, which forces large k.
- These facts are recorded in the background as Part C (C1–C4) of /tmp/hf4/bg4.md, the background block spliced into the round-4 queries.

## Open gaps
1. The goal itself (equivalently the normalized statement N below). No reduction beyond normalization is proved.
2. (C) for -1 = 1 (#5): set aside, not refuted.
3. Exponent-3, -1 = 1 counterexample existence (#9): set aside, not refuted. Small cases are excluded computationally (dense sums); large sparse structures are unexplored.
4. Class a⊞-a = H with -1 ≠ 1, generic case (#6): set aside, not refuted.
5. Krasner extensions / projective geometries with an abelian regular group: set aside, not refuted.
6. New lens (untried): the free hyperfield on x, y with 1 ∈ x⊞y, built by a chase. The goal holds iff 1 ∈ T there. Its existence as a hyperfield is unchecked.

## The chain and the missing statement
Chain. (1) The normalization (elementary, proved in round1_q1 §3 and restated as (A2) in the round-4 background): if z = 0, then y = -x and the target contains 0 ∈ x^3⊞-x^3 by absorption; if z ≠ 0, multiply the hypothesis and the target by the single element -z^{-1} (distributivity) and rename x/(-z), y/(-z) as x, y. Then the [GOAL] claim is equivalent to the missing statement N for nonzero x, y. (2) N is the missing statement. A proof of N proves [GOAL]. An explicit hyperfield with nonzero x, y, 1 ∈ x⊞y and 1 ∉ T refutes [GOAL] (take z = -1). No PROVED entry reduces N further: entries #2, #3, #4, #7, #8 and the round-3 results settle only sub-classes or rule out proof methods.

Missing statement (N). Let H be a hyperfield: H = G ∪ {0}, where G is an abelian multiplicative group, and ⊞ is a commutative, associative multivalued addition with nonempty values, with 0 neutral, a unique -a for each a with 0 ∈ a⊞-a, reversibility (c ∈ a⊞b ⇒ a ∈ c⊞-b), and distributivity w(a⊞b) = wa⊞wb. Let x, y ∈ G with 1 ∈ x⊞y. Then 1 ∈ T := x^3⊞y^3⊞xy⊞xy⊞xy. (Ledger: OPEN line, round4_plan.)

Why it should hold (coordinator's sketch; I am genuinely unsure of the truth value).
- For: (C1) shows no counterexample below 11 elements. (C2) shows that in the exponent-3 char-2 class every small structure has Q = G. Every structured family examined satisfies N: quotients, union-type, a⊞-a = H with -1 = 1, circular/ordered types (an informal check by the coordinator: 1 lies "between" x and y, so 1 lies in the cone of x^3, y^3, xy).
- A proof must use witnesses: linear derivations fail (#2, round3_q1, round3_q2). Candidate mechanism: the zero-sum calculus. Its moves are composition along a shared element, splitting a zero-sum Z = Z1 ⊔ Z2 into Z1+t, Z2+(-t) with a fresh t (this is associativity), scaling, and adding pairs {a, -a}. The field identity 1 - x^3 - y^3 - 3xy = (1 - x - y)(1 + x + y + x^2 - xy + y^2) needs the six scaled hypothesis relations R_m (m ∈ {1, x, y, x^2, -xy, y^2}). Their 18 terms cancel in 6 opposite pairs, but a tree of 6 relations allows only 5 gluings, so one cycle remains (for (C) with -1 = 1, 7 cancellations are needed against 5 gluings). The hope is that splitting closes the extra cycle(s), by routing them through fresh witnesses that are then eliminated by composing two copies of a split.
- Against: the free hyperfield of (C4). If the chase never needs the cycle-closing step, the free object is a counterexample. Showing that needs an invariant of chase steps, e.g. a weight on fresh generators, that the target violates.

Tried so far (on N or the goal itself):
- round1_q1: linear compositions → obstruction (no proof).
- round1_q3: diagonal case + witness expansion → special case only.
- round1_q4: class analysis → classes a⊞-a = H (-1 = 1); reduction to (C).
- round1_q2: counterexample search, Krasner extensions → nothing.
- round2_q1/q2/q3/q4: (C), witness iteration, exponent-3 construction, idempotent class → small lemmas, obstructions.
- round3_q1: exponent-3 triangle translation → linear obstruction in that class.
- round3_q2: 4-point exchanges → equivalent to compositions, obstruction.
- round3_q3: symmetric multiplier c, witness moving, certificates → dead for single multipliers.
- round3_q4: -1 ≠ 1 classes → coincidence cases + union-type family.

## Target for round 4's wave (where the next round should concentrate)
Progress test: rounds 2 and 3 produced no progress on the chain, so the main line is stalled with no universal progress. Those rounds yielded only sub-class lemmas and method obstructions, and no shortening of the chain. What differs from last round: the chain is now stated explicitly with N as the single missing statement, and the sketch names two new mechanisms that no earlier query used. One is splitting-based cycle closing in the zero-sum calculus (proof side). The other is the free hyperfield / chase invariant (refutation side). There is also a quantitative constraint from computation: counterexamples in the exponent-3 class must be sparse, which needs large groups.

Round-4 wave (escalation rule; deep workers; 10 queries, all "kind: attempt"):
- q1–q4: closing task, byte-identical copies. Prove N, or give an explicit counterexample, with the full background (/tmp/hf4/bg4.md) spliced in.
- q5: refute N by an explicit sparse non-quotient construction, with a verification checklist.
- q6: free-hyperfield/chase lens. Either a derivation of 1 ∈ T, or an invariant of chase steps that gives a counterexample.
- q7: zero-sum calculus with splitting. Try to close the two extra cycles of the field identity's gluing graph.
- q8: fresh-first-move query. It gets only the statement and the statements of the cited entries, and must first re-derive the chain.
- q9 (elsewhere 1): counterexample or proof within the class a⊞-a = H, -1 ≠ 1 (#6, generic case).
- q10 (elsewhere 2): the exponent-3, -1 = 1 class (#9). Prove Q ∩ wQ ≠ ∅ there, or build a sparse system on large F_3^k.

Any proposed counterexample must be machine-checked by the coordinator (for a finite one, /tmp/hf3/chk.py or /tmp/hf4 tools), then audited by two verify queries.
