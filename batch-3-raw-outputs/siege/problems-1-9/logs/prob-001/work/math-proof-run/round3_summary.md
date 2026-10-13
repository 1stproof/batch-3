# Running summary after round 3 planning

## Goal
The problem fixes the claim (ledger #1, OPEN [GOAL]). For every monoid P (integral, saturated, sharp, and NOT assumed finitely generated) and every presheaf of abelian groups F on B_P^op, the map F -> R pi_* pi^{-1} F is a quasi-isomorphism. Answer YES = PROVED; a counterexample = REFUTED.

## Established so far (worker results)
- round1_q1 (#2): reduction. id_P is terminal in A_P^op and in B_P^op, and slices are the sites of the localizations. So the claim is equivalent to H^0(A_P, pi^{-1}F) = F(P) and H^{>0} = 0 for all P and F. The director's Step 6 below gives a cleaner route that needs no slicing.
- round1_q2 (#3): a map M -> N with M valuative is infinitesimal iff it kills no nonzero element. Every infinitesimal map kills no nonzero element of its source.
- round1_q3 (#4): the claim for P = N, at the level of valuations.
- round1_q4 (#5): the finite-poset lemma for subdivisions. It is not directly needed now.
- round2_q4 (#9): re-checked R1, R2 and R4. R2: every f.p. map is birhizomic at the zero map, and localizations are birhizomic everywhere. R4: open-cone extensions sat(P + <a_i>) are birhizomic when v(a_i) > 0 under the prec-control, given finite presentation. It also checked that I_{tau,A} (the co-skyscrapers on the face poset) are injective and that F embeds into their product. It flagged that pi^{-1} might not commute with infinite products; this is irrelevant for fine P, where the products are finite.
- round2_q1 (#10, #11): Lemma A and Proposition B.
  - Lemma A: let P be fine, P ⊂ Q ⊂ P^gp, and v nonzero on P\0. If P -> Q is birhizomic at g, then g > 0 on Q\0. The test object is M = {v > 0} ∪ {0}. In particular, closed subdivision charts are not birhizomic at wall valuations.
  - Proposition B: at rank one with v injective on P, the map is birhizomic iff g^{-1}(0) = 0.
  - Open there: whether the prec condition is necessary at higher rank, and maps that are not injective on groups.
- round2_q2 (#12): for fine P, B_P is the finite face poset. A filtration by up-sets plus the five lemma reduces the claim to F concentrated at one face.
- round2_q3: proved only two small observations; nothing load-bearing. (Its "Observation 1", that g is a retraction of f, is tautological because gf = id is assumed.)

## NEW: the director's proof outline for finitely generated P (ledger #13, OPEN until a worker writes it out and it is verified)
The full text is "Background B", reproduced verbatim inside round3_q1..q4.md. In summary:
- **Step 0.** For fine P, every kernel face Phi_Q = f^{-1}(0) is principal. The comma category for the left Kan extension has a terminal object b(Q) = P[-x_Q]^sharp. So Lan F = F∘b, with (F∘b)(Q) = F(Phi_Q). Presheaves on A_P^op are covariant functors on A_P.
- **Step 1.** For fine Q, Phi_Q = P ∩ T_Q^⊥, where T_Q is the cone of real valuations. Real valuations of a pushout are the compatible tuples, so T_sigma = ∩ T_i.
- **Step 2 (Lemma K).** Every birhizomic covering has a finite subfamily whose real cones T_i cover Q^v_R. Proof sketch: compactness of the patch space of total preorders on Q^gp⊗Q, plus Fourier–Motzkin/quantifier elimination, which makes the sets "factors through Q_i" clopen. Lemma K holds for arbitrary Q.
- **Step 3.** Every F has a finite injective resolution by products of I_{tau,A}. The Čech complex of I_{tau,A}∘b on a covering is the ordered cochain complex of N_tau = nerve of {T_i ∩ C}, where C = {w : w > 0 on P \ Phi_tau} is convex.
- **Step 4.** Every finite subcomplex of N_tau lies in a full subcomplex on J' ⊇ J_0, whose nerve is that of a finite compact convex cover of a compact convex set D, hence contractible. So N_tau is contractible.
- **Step 5.** Hence F∘b satisfies the sheaf condition on all coverings of f.p. objects, and pi^{-1}F = F∘b on f.p. objects. This gives pi_* pi^{-1} F = F.
- **Step 6.** Cartan's criterion (Stacks 03F7), with B = the f.p. objects and Cov = all their coverings, gives H^{>0}(U, pi^{-1}F) = 0 for all f.p. U, including the objects of B_P. R^p pi_* is computed objectwise, so the answer is YES for fine P.
- **Notable feature:** the outline uses only two properties of coverings: their members are f.p., and every valuation factors through some member. Birhizomicity itself is not used for fine P.

## Dead ends
- Covers by closed charts of subdivisions are not birhizomic (R3, Lemma A). The finite-poset lemma (#5) is not the mechanism.
- Exactness of pi_! = Lan along b fails in general: the comma categories are not filtered. So the "pi^{-1} preserves injectives" route is not available.
- The topological-space picture (R5: open-cone neighbourhoods, generic zero valuation, rank-two points gluing faces to the interior) is consistent with the outline but no longer needed for fine P.

## Open gaps
1. **(#13)** A complete rigorous write-up of the fine-P outline, especially:
   - Lemma K, in full;
   - the nerve theorem for compact convex sets and the passage to infinite complexes;
   - Cartan's criterion and its hypotheses (f.p. objects are closed under pushouts, and f.p. objects over fine P are fine);
   - the formula for R^p pi_*;
   - the interpretation that coverings of a non-terminal object Q are the birhizomic covers of Q.
2. **(#14)** Arbitrary P. Three issues:
   - (a) Are kernel faces of f.p. maps principal? A sketch says yes: the face generated by Y ∩ P, with Y a finitely generated monoid, is principal, using rational points of rational polyhedra and saturation.
   - (b) Real valuations do not detect faces. Example: P = {x3 > 0} ∪ (N^2 × 0) in Z^3.
   - (c) The nerve N_tau equals the nerve of {E_i ∩ C_Omega} for higher-rank valuations. These sets are convex in Hom(Q^gp, H) for a Hahn group H but not closed, so the convex nerve theorem fails. This is where the birhizomic prec condition may be essential: covers by "closed" sign splits are not birhizomic. A counterexample to the headline claim would need a birhizomic covering with disconnected or acyclicity-failing N_tau.
   - Observation: for a sign split by a, the overlap has kernel 0 whenever injective valuations of both signs exist (an order-extension argument). So sign splits cannot produce disconnection.
3. A reduction route for #14: P is a filtered union of fine P_S. Two caveats: valuations of P_S need not extend to P (example: P = N^2, S = {e1, e1+2e2}), and descending covers needs Lemma K.

## Next round (round 3 wave: 4 attempt queries, all carrying Background A (R1–R4, Lemma A/Prop B) and Background B verbatim)
- q1: a complete rigorous proof for fine P along Background B (target #13), with an N^2 sanity check.
- q2: a positive proof for arbitrary P: principal kernels, plus the property of birhizomic loci that makes N_tau contractible (target #14).
- q3: a counterexample hunt among non-fg P for a birhizomic covering with non-contractible N_tau, with birhizomicity rigorously verified; also an adversarial check of Background B.
- q4: reduce arbitrary P to fine P via filtered unions, descent of f.p. objects and coverings, and limits of topoi.

Afterwards: once q1 returns a complete fine-P proof, send it to two verify queries. If q2 or q4 yields arbitrary P, that becomes the [GOAL] proof. If only fine P is proved, the posed goal still covers all P; keep #14 as the target (escalation round 4).
