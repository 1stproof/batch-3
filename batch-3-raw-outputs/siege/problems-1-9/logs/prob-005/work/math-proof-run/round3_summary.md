# Round 3 summary (after folding rounds 1-2)

## Problem / goal
Decide: in every hyperfield, does 0 ∈ x⊞y⊞z imply 0 ∈ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz? Ledger [GOAL] (#1): universal claim, OPEN. The problem poses the claim: a proof, or a verified explicit counterexample (REFUTED), settles the run.

## Normal form and coordinator facts (elementary; re-prove in proof.md if used)
- z = 0 trivial; for z ≠ 0 scale by -1/z: equivalent to "1 ∈ x⊞y ⇒ 1 ∈ T := x^3⊞y^3⊞xy⊞xy⊞xy", x, y nonzero.
- Quotients F/U satisfy it; the class of hyperfields satisfying it is closed under quotients H/U; ordered-group extensions inherit it (sketch only). Counterexample must be non-quotient.
- Coordinator computer search (unrefereed, /tmp/hf/s2.py): no counterexample with |G| ≤ 9. Round 3 coordinator check (/tmp/hf3/chk.py): F_3^k (k ≤ 3), -1 = 1, triangles "a+b+c ∈ K" + doubles from D ∈ {∅, K\0, G\0}: only trivial associative members, all satisfy the claim.
- Coordinator lemma (B11c,d, elementary, in round3 queries): with -1 = 1, associativity ⇔ 4-point symmetry "(a⊞b)∩(c⊞e) ≠ ∅ ⇔ (b⊞c)∩(a⊞e) ≠ ∅"; and if 1⊞1 = {0} (with -1 = 1) then H is a field (sums a⊞c, c ∈ H, partition H). So non-field char-2 hyperfields have D = (1⊞1)\{0} ≠ ∅.

## Established
- round1_q1: composition rule (0 ∈ A⊞t, 0 ∈ B⊞-t ⇒ 0 ∈ A⊞B); linear-derivation obstruction (contraction of the set x^2y⊞xy^2 to xy is needed).
- round1_q3: diagonal case y = x; witness expansion 1 ∈ x^3⊞y^3⊞xy⊞xy⊞xyu for some u ∈ x⊞y (re-checked round2_q2).
- round1_q4: absorption; class a⊞-a = H with -1 = 1 holds; -1 = 1 ⇒ goal follows from (C) 1 ∈ x^3⊞y^3⊞xy; a⊞a = {a} ⇒ goal ⇔ (C).
- round1_q2: Krasner extensions reduce to projective geometries; not promising.
- round2_q1/q2/q3: (B10) exponent-3 reduction verified (three independent checks): with -1 = 1 and g^3 = 1, counterexample iff ∃x, w ∈ x⊞x^2 with Q∩wQ = ∅, Q = 1⊞1⊞1. Also 1 ∈ Q always when -1 = 1; hence also need w ∉ Q, w^{-1} ∉ Q (round2_q1 P1, round2_q3 corollary), 1 ∉ 1⊞1, w ≠ 1.
- round2_q4: idempotent class: 1 ∈ x^2⊞xy⊞y^2 and 1 ∈ x^3⊞y^3⊞x^2y⊞xy^2; same contraction obstacle.

## Dead ends
- Linear/compositional derivations (round1_q1); iterating the witness expansion (round2_q2: witness ranges over all x⊞y each time); re-bracketing (x⊞y)^3 (round2_q2).
- Single-valued affine-line rule on F_3^k (non-associative, round2_q3); subgroup-triangle families on F_3^k (coordinator check).
- Krasner extensions; sums-contain-summands classes; class a⊞-a = H with -1 = 1; small search ≤ 10 elements.
- "Frobenius" 1 ∈ x^2⊞y^2 needs xy⊞xy = {0}, which forces a field (B11d).

## Open gaps
1. The goal itself.
2. (C) / 1 ∈ T for -1 = 1 (ledger #5).
3. Exponent-3, -1 = 1 counterexample existence (new OPEN line this round).
4. Class a⊞-a = H with -1 ≠ 1 (#6); idempotent class (C).
5. Whether some witness/certificate argument evades the obstruction.

## Impression
Two exploratory rounds produced only partial facts; workers' answers are short. Evidence: small search says YES-ish; structural obstruction says a proof needs genuinely non-linear use of associativity. Undecided.

## Round 3 target
Four attempt queries, different lenses, all with an updated background block (B1–B14): q1 exponent-3 char-2 class — construct or exclude via 4-point condition; q2 (C)/1∈T for -1 = 1 via 4-point exchanges and minimal-configuration blueprint; q3 general affirmative proof via symmetric form / witness moving / certificate-or-partial-model; q4 -1 ≠ 1: class a⊞-a = H, coarsened quotients, idempotent circular-order constructions. Escalation to deep workers expected from round 4; if round 3 again yields nothing, concentrate deep queries on the char-2 class (q1/q2 line) where the combinatorial formulation is cleanest.
