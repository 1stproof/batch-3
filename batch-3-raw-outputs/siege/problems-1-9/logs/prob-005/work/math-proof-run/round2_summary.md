# Round 2 summary (after folding round 1)

## Problem / goal
Decide: in every hyperfield, does 0 ∈ x⊞y⊞z imply 0 ∈ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz? Ledger [GOAL] (#1): the universal claim, OPEN; the problem poses the claim, so either a proof or a verified explicit counterexample (REFUTED) settles the run.

## Normal form and coordinator facts (elementary; re-prove in proof.md if used)
- z = 0 trivial; for z ≠ 0 scale by -1/z: equivalent to "1 ∈ x⊞y ⇒ 1 ∈ T := x^3⊞y^3⊞xy⊞xy⊞xy", x, y nonzero WLOG.
- Quotient hyperfields F/U satisfy it (lift to field). Ordered-group extensions H⋊Γ inherit it from H (coordinator's leading-term sketch, not written in full). So a counterexample is non-quotient.
- Computer search (coordinator, unrefereed, script /tmp/hf/s2.py): no counterexample with |G| ≤ 9 (all abelian groups of order ≤ 8, Z9, Z3×Z3). Counterexample needs ≥ 11 elements.
- Exponent-3 reduction (coordinator, plan of round 2, elementary): if all g^3 = 1 (forcing -1 = 1), put Q = 1⊞1⊞1; then H is a counterexample iff ∃x ∈ G, nonzero w ∈ x⊞x^2 with Q ∩ wQ = ∅ (needs 1 ∉ 1⊞1, w ≠ 1). Not yet checked by a worker.
- Massouros-type "a⊞b = {a,b,a+b} (b ≠ -a), a⊞-a = F" on a field F and "a⊞b = {a,b}, a⊞-a = H" types satisfy the implication (coordinator, quick check).

## Established in round 1 (all four answers genuine, none settles the goal)
- round1_q1: Composition rule: 0 ∈ A⊞t and 0 ∈ B⊞-t ⇒ 0 ∈ A⊞B. Obstruction: in a formal-monomial model, no derivation composing only the hypothesis multiples R_w : 0 ∈ wx⊞wy⊞-w via the composition rule yields the target (term count forces R_1, R_{x^2}, R_{y^2} + one more, which cannot cancel the 6 unwanted terms). The field step x^2y+xy^2 = xy needs contracting a set to an element. So any proof needs auxiliary witnesses + their relations (associativity/reversibility).
- round1_q3: Diagonal case: 1 ∈ x⊞x ⇒ 1 ∈ T. Expansion with witness: 1 ∈ x^3⊞y^3⊞xy⊞xy⊞w for some w ∈ xy(x⊞y); hence 1 ∈ T whenever the witness can be xy (e.g. x⊞y = {1}).
- round1_q4: Absorption: H⊞a = H; 0 ∈ S ⇒ A⊞S ⊇ A. Class a⊞-a = H (all a ≠ 0) with -1 = 1: holds (T = H). With -1 ≠ 1 only the subcase "some cube equals xyz" is done. Reduction: if -1 = 1, the goal follows from (C): 1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy; if a⊞a = {a} for all a, the goal is equivalent to (C). Stringent and doubly distributive classes: holds conditional on Bowler–Su classifications cited from memory (all quotients) — not verified.
- round1_q2: Krasner extensions (-1 = 1, a⊞a = {0,a}): T = (x^3⊞y^3) ∪ (x^3⊞y^3⊞xy); x = y case fine; the "one-line" family x⊞y = G\{x,y} gives no counterexample (one bullet only sketched, axioms not verified). Krasner extensions ≈ projective geometries with abelian regular collineation group, all known ones Desarguesian ⇒ quotients; not promising.

## Dead ends
- Pure expansion / linear composition proofs (round1_q1 obstruction).
- Small exhaustive search (≤ 10 elements): nothing.
- Krasner extensions/projective geometries, Massouros-type "sums contain summands", class a⊞-a = H with -1 = 1: all satisfy the claim, no counterexample there.

## Open gaps
1. The goal itself (proof or counterexample).
2. (C) for -1 = 1 hyperfields (settles that class) — and for a⊞a = {a} hyperfields (equivalent to goal there).
3. Class a⊞-a = H with -1 ≠ 1.
4. Exponent-3 / char-2 construction route (B10): is there a hyperfield with g^3 = 1 for all g, 1 ∉ 1⊞1, and x, w as above with Q ∩ wQ = ∅?

## Round 2 target
Still exploration, four genuinely different attempts: q1 the -1 = 1 class via (C) (proof or counterexample); q2 a general affirmative proof built on auxiliary witnesses (must evade the B6 obstruction); q3 explicit counterexample construction, especially via the exponent-3 reduction and other non-quotient constructions; q4 the idempotent class a⊞a = {a} (-1 ≠ 1, where goal ⇔ (C)) and the a⊞-a = H class with -1 ≠ 1. If any counterexample is proposed, the coordinator checks it by computer before sending two verify queries.
