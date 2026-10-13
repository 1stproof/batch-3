1. OPEN: [GOAL] For every hyperfield H and all x, y, z in H with 0 ∈ x⊞y⊞z one has 0 ∈ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz (settle by proof, or REFUTE by an explicit hyperfield counterexample) — round1_plan
2. PROVED: Composition rule: if 0 ∈ A⊞t and 0 ∈ B⊞(-t) then 0 ∈ A⊞B; and no derivation composing only hypothesis multiples 0 ∈ wx⊞wy⊞-w this way reaches the target (formal-monomial obstruction) — round1_q1
3. PROVED: In normalized form (1 ∈ x⊞y), 1 ∈ T := x^3⊞y^3⊞xy⊞xy⊞xy when y = x, and in general 1 ∈ x^3⊞y^3⊞xy⊞xy⊞w for some w ∈ xy(x⊞y) — round1_q3
4. PROVED: If -1 = 1 the goal follows from (C) "1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy", if a⊞a = {a} for all a the goal is equivalent to (C), and the goal holds when -1 = 1 and a⊞-a = H for all a ≠ 0 — round1_q4
5. OPEN: (C) 1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy, in hyperfields with -1 = 1 or with a⊞a = {a} — round1_q4
6. OPEN: The goal for hyperfields with -1 ≠ 1 and a⊞-a = H for all a ≠ 0 — round1_q4
7. PROVED: If -1 = 1 then 1 ∈ 1⊞1⊞1, the exponent-3 reduction (B10) is correct, and an exponent-3 counterexample with -1 = 1 needs x, w ∈ x⊞x^2 with Q∩wQ = ∅, w ∉ Q, w^{-1} ∉ Q, 1 ∉ 1⊞1 (Q = 1⊞1⊞1) — round2_q3
8. PROVED: In hyperfields with a⊞a = {a} for all a, 1 ∈ x⊞y implies 1 ∈ x^2⊞xy⊞y^2 and 1 ∈ x^3⊞y^3⊞x^2y⊞xy^2 — round2_q4
9. OPEN: Whether some hyperfield with -1 = 1 and G of exponent 3 is a counterexample (exists x, w ∈ x⊞x^2 with (1⊞1⊞1) ∩ w(1⊞1⊞1) = ∅) — round2_q3
10. PROVED: In hyperfields with a⊞-a = H for all a ≠ 0, any multi-sum having two opposite nonzero summands equals H (so the goal holds in all coincidence cases), and the union-type hyperfields (a⊞b = {a,b} for b ≠ -a, a⊞-a = H, any G with -1 ≠ 1) are hyperfields satisfying the goal — round3_q4
11. PROVED: When -1 = 1, chains of 4-point exchanges reduce to compositions of scaled hypothesis triangles, and no such linear derivation yields (C) or 1 ∈ x^3⊞y^3⊞xy⊞xy⊞xy — round3_q2
12. PROVED: Hyperfields with -1 = 1 and G = F_3^k are exactly translation-invariant symmetric triangle systems on F_3^k with the 4-point condition, and in the generic case no linear derivation gives 0 ∈ 1⊞1⊞1⊞w⊞w⊞w — round3_q1
13. OPEN: Missing statement N: in every hyperfield, for all nonzero x, y with 1 ∈ x⊞y one has 1 ∈ x^3⊞y^3⊞xy⊞xy⊞xy (equivalent to the goal by normalization; prove it, or refute it by an explicit hyperfield) — round4_plan
14. REFUTED: [GOAL] The implication fails: there is a hyperfield (Krasner-type, from an infinite non-Desarguesian projective plane on Z with lines the translates of a greedy perfect difference set D ⊇ {0,1,4,103,105,112}, 100 ∉ D) with x = t, y = t^4, z = 1 such that 0 ∈ x⊞y⊞z but 0 ∉ x^3⊞y^3⊞z^3⊞-xyz⊞-xyz⊞-xyz — round4_q2
15. REFUTED: Missing statement N (1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy⊞xy⊞xy in every hyperfield) is false, by the same counterexample (also round4_q1, round4_q4, round4_q6, round4_q7) — round4_q2
16. REFUTED: (C) 1 ∈ x⊞y ⇒ 1 ∈ x^3⊞y^3⊞xy fails in a hyperfield with -1 = 1 (the same Krasner-type example) — round4_q1
17. PROVED: An abelian group G acting regularly by collineations on a projective plane with at least 5 points per line gives a hyperfield H = G ∪ {0} with -1 = 1, a⊞a = {0,a} and a⊞b = ℓ(a,b) \ {a,b}, in which 1 ∈ x⊞y but 1 ∉ x^3⊞y^3⊞xy⊞xy⊞xy whenever 1, x, y are distinct collinear points and x^3, y^3, xy are distinct points on a line M not through 1 (then that sum is M ∪ {0}) — round4_q2
18. PROVED: Hexagon lemma (the target meets μ(1⊞-1) for each mixed monomial μ) and Helly criterion (if x^2⊞-yz, y^2⊞-zx, z^2⊞-xy have a common point the claim holds); quotients of skew fields and alternative division rings satisfy the claim — round4_q5
19. PROVED: Up-closure K^↑ of any hyperfield is a hyperfield of class a⊞-a = H, and (N) holds throughout that class iff every hyperfield satisfies the weak form that some nonempty sub-multiset of {x^3,y^3,xy,xy,xy,-1} is a zero-sum — round4_q9
20. PROVED: (N) holds in hyperfields with -1 = 1 and g^2 = 1 for all g — round4_q3
21. OPEN: Whether a finite hyperfield counterexample to the claim exists — round4_q2
22. PROVED: [AUDIT] Independent step-by-step referee check certifies the round4_q2 counterexample chain (Proposition 1, Lemmas 2-4, instance x = t, y = t^4, z = 1), verdict CORRECT, certifying entry 14 — round5_q1
23. PROVED: [AUDIT] Second independent adversarial recheck (including Krasner, Viro and Baker–Bowler definitions) certifies the round4_q2 counterexample chain, verdict CORRECT, certifying entry 14 — round5_q2
