# Running summary after round 5 planning

## Goal and status
The problem fixes the claim (ledger #1, [GOAL]): for EVERY monoid P (integral, saturated, sharp; NOT assumed finitely generated) and every presheaf of abelian groups F on B_P^op, F -> R pi_* pi^{-1} F is a quasi-isomorphism. Expected answer: YES.

**Status after round 4: a complete written proof of YES for all P is in hand.** The last missing piece was the nerve statement #19 (OPEN in round 4). Eight of the nine round-4 deep engines proved it, by several independent methods: round4_q1, q2, q3, q5, q6, q7, q8, q9. round4_q4 (the refutation attempt) found no counterexample and proved structural results (below). All the proofs actually show a stronger statement (#20 in this round's ledger block). Only the cover's *factorization property* is used: every valuation of Q factors through some member. Neither birhizomicity beyond that nor principality of tau is used. The [GOAL] is recorded PROVED this round (entry #22). It is NOT yet certified by verify queries. This round's wave is the audit wave.

**Chain chosen for the audit:** #16 (round3_q2 Part 1) + #20 proved by round4_q7, plus the chain derivation below. The chain's sheaf-theoretic steps are those of #15 (round3_q1 Steps 0, 3, 5, 6). round4_q7 was chosen because it is the most self-contained proof of #20. It cites only Tychonoff, Zorn, Fourier–Motzkin elimination (proved inline) and standard homological algebra. It avoids the Borsuk nerve theorem, Tarski completeness and quantifier elimination altogether, replacing them with an induction on "undecided sign conditions" using a double-complex comparison.

## The chain (complete; derivation as in round4 summary, now with step 4 proved)
1. (#16) B_P ≃ the poset of principal faces of P. It is directed: face(x) ∨ face(y) = face(x+y). For f.p. Q, (Lan F)(Q) = F(Phi_Q) via the terminal object P[-x_Q]^sharp. Lan is exact, pi^{-1} = (Lan -)^sh is exact, and pi_* is restriction to B_P.
2. I_{tau,A}(b) = A if Phi_b ⊂ tau and 0 otherwise. Hom(F, I_{tau,A}) = Hom(F(tau), A). F embeds into the product over tau of the I_{tau,E(F(tau))}, which gives a resolution F -> I^• by products of these.
3. On f.p. Q, Lan of a product is the product of the Lans (Lan is evaluation at b(Q) there). For a covering of an f.p. Q, the augmented Čech complex of Lan I_{tau,A} is 0 if Phi_Q ⊄ tau. Otherwise it is the augmented ordered cochain complex of N_tau = {sigma : Phi_{Q_sigma} ⊂ tau}.
4. (#20, round4_q7 and others) N_tau is nonempty with exact augmented ordered (co)chain complexes.
5. Lan I^k, and hence Lan F, satisfy the sheaf condition on coverings of f.p. objects. Sheafification does not change values on f.p. objects, so pi_* pi^{-1} F = F.
6. Cartan's criterion (Stacks 03F7) with B = f.p. objects gives H^p(U, pi^{-1}F) = 0 for p > 0 and U in B. R^p pi_* G = (b ↦ H^p(b, G)). So the [GOAL] holds.

**Chain-level point flagged by round4_q7 §7 (to be handled in the write-up and checked by the audit).** A birhizomic cover need not have all members f.p.: only the members serving as witnesses (birhizomic at some lift) are f.p. by definition. Fix: the witness subfamily of any birhizomic cover is itself a birhizomic cover all of whose members are f.p., and it refines the original. So coverings of f.p. objects with all members f.p. (and all fibre products f.p.) are cofinal among all coverings of f.p. objects. This is exactly what Cartan's criterion requires, and it is enough for the plus construction. round3_q1 Step 5.4 said "members are f.p. because birhizomic maps are f.p. by definition", which is too quick; the cofinality argument repairs it. round4_q9 also remarked that it does not matter whether the birhizomic covers are the coverings of a pretopology or only generate the topology, since they are cofinal.

## Standing results
- #2 (round1_q1): reduction via terminal object id_P / slices (valid; not on the current line).
- #3 (round1_q2): M -> N with M valuative is infinitesimal iff it kills no nonzero element; every infinitesimal map kills no nonzero element of its source.
- #4 (round1_q3): P = N valuation-level check. Not on the current line.
- #5 (round1_q4): finite-poset lemma for fans. Not on the current line.
- #9 (round2_q4): f.p. maps are birhizomic at the zero map; P -> P[-x]^sharp is birhizomic at every map (R2); R4 open-cone extensions are birhizomic.
- #10, #11 (round2_q1): Lemma A and Proposition B (fine P, rank one).
- #12 (round2_q2): fine P: B_P = finite face poset; reduction to F concentrated at one face.
- #15 (round3_q1): complete solution for finitely generated P (YES). Its Steps 0, 3, 5, 6 are reused in the general chain. Its Lemma K is replaced in general by compactness, as in #20.
- #16 (round3_q2 Part 1; also round3_q4 Thm 1.3): for every P and every f.p. P -> Q, the kernel face is principal. It cites the retract-of-finite-presentation description of f.p. objects; round4_q3 Lemma 0.1, round4_q5 Lemma 1.1 and round4_q7 Lemma 1(i) prove that description.
- #17 (round3_q4): filtered colimits stay in the category; valuations of P_S need not extend. Not on the current line.
- #20 (NEW, round4_q7; independently round4_q1, q2, q3, q5, q6, q8, q9). The nerve statement in strengthened form. Take any P, any f : P -> Q, any family of f.p. maps Q -> Q_i such that every valuation of Q factors through some member, and any subset tau ⊂ P containing Phi_Q. Then N_tau is nonempty, and its augmented ordered chain and cochain complexes (any coefficients) are exact. The methods:
  - q7: lifting loci are finitely many sign conditions (Fourier–Motzkin); Tychonoff gives a finite subcover; abstract acyclicity Theorem T by induction on undecided sign conditions.
  - q1 and q5: real functionals on a finite-rank subgroup approximating C_tau; Borsuk's nerve theorem.
  - q2, q8, q9: convex combinations of witnesses with coefficients in a real closed field; Tarski transfer of the nerve theorem.
  - q3 and q6: descent to a fine level P_S by compactness, then the #15 convex argument.
- #21 (NEW, round4_q5 Appendix A Theorem C; also round4_q4 Corollary 2). Exact characterization of birhizomy, via the initial infinitesimal test object M(v). Not needed for the goal; useful for "Other routes".
- #22 (NEW): [GOAL] PROVED via the chain. Awaiting audit.

## Dead ends (refuted statements only)
- #7/#10: "closed subdivision charts are birhizomic at wall valuations", REFUTED by Lemma A (round2_q1).
- Director's naive real-parameter Hahn convexification "loci are open along segments / have connected nerves": shown false by explicit examples (round4_q1 §6, round4_q8 §0, round4_q4 Example 8). This is moot now; #20 avoids it.

## Open gaps
- No mathematical gap known in the chain. Two things still need doing:
  - The audit: two independent verify queries on the whole chain.
  - The write-up of the sheaf-theoretic steps with the witness-subfamily cofinality fix, plus the statement of Cartan's criterion with its cofinality hypothesis.
- Cited standard facts: Cartan's criterion (Stacks 03F7); Tychonoff; Zorn; Gordan (in #16); the double-complex lemma; the universal coefficient theorem.

## Target for the next round (round 5 wave = audit wave)
A complete written proof is in hand, so the audit rule governs this wave and the escalation rule does not apply. The wave:
- q1 = q2: identical verify queries. Each carries the whole chain spliced verbatim: the chain derivation (with the cofinality fix), round3_q2 Part 1 (#16), round3_q1 in full (Steps 0, 3, 5, 6 are reused), and round4_q7 in full (#20). Each asks for a step-by-step check and a verdict on entry #22.
- q3: an independent verify of the second proof of #20 (round4_q5), as a backup in case the q7 proof fails its audit.
- q4: a full rigorous write-up of chain steps 1, 2, 3, 5, 6 for arbitrary P, including the non-f.p.-member cofinality point and the precise use of Cartan's criterion. This is material for the final document.

If both q1 and q2 certify, record two [AUDIT] lines citing #22 and conclude. If one finds a gap, act on it as follows:
- if it is in round4_q7's #20 proof, fall back on round4_q5 or round4_q1 (q3 checks round4_q5);
- if it is in the chain, repair it, using q4's write-up.
