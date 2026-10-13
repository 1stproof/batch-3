# Running summary after round 4 planning

## Goal
The problem fixes the claim (ledger #1, OPEN [GOAL]): for EVERY monoid P (integral, saturated, sharp; NOT assumed finitely generated) and every presheaf of abelian groups F on B_P^op, F -> R pi_* pi^{-1} F is a quasi-isomorphism. YES = PROVED, counterexample = REFUTED. Status: YES is proved for finitely generated P (#15); arbitrary P is open. No complete proof of the goal is in hand.

## Standing results
- #2 (round1_q1): reduction via terminal object id_P / slices (superseded in practice by the Kan-extension route below, still valid).
- #3 (round1_q2): M -> N with M valuative is infinitesimal iff it kills no nonzero element; every infinitesimal map kills no nonzero element of its source.
- #4 (round1_q3): P = N, valuation-level check. Not on the current line.
- #5 (round1_q4): finite-poset lemma for fans. Not on the current line.
- #9 (round2_q4): every f.p. map is birhizomic at the zero map; P -> P[-x]^sharp is birhizomic at every map (R2). R4: open-cone extensions sat(P + <a_i>) with v(a_i) > 0 and prec-control are birhizomic (given f.p.).
- #10, #11 (round2_q1): Lemma A (fine P ⊂ Q ⊂ P^gp, v nonzero on P\0, birhizomic ⇒ g > 0 on Q\0; test object M = {v>0} ∪ {0}); Proposition B (rank one, v injective on P: birhizomic iff g^{-1}(0)=0).
- #12 (round2_q2): fine P: B_P = finite face poset; reduction to F concentrated at one face.
- #15 (round3_q1): COMPLETE SOLUTION FOR FINITELY GENERATED P: answer YES. Steps: Lan F = F∘b, (F∘b)(Q) = F(Phi_Q); kernel faces read off real valuations; Lemma K (finite subcover of the dual cone, proved by tangent-cone/flag induction from the cover property applied to lexicographic flag valuations); Čech complex of I_{tau,A}∘b = ordered cochains of N_tau = nerve of {T_i ∩ C}; N_tau contractible via convex hull of witnesses + Borsuk nerve theorem; sheaf condition; Cartan's criterion on f.p. objects. Quoted from memory: Borsuk/Leray nerve theorem for finite compact convex families, Cartan's criterion (Stacks 03F7), local conic structure of polyhedra. round3_q3 independently re-checked the Background B outline step by step and found no error. Not yet separately verified as a write-up.
- #16 (round3_q2 Part 1; also round3_q4 Thm 1.3, different proof): for EVERY P and f.p. P -> Q, Phi_Q is principal. Hence B_P ≃ poset of principal faces (directed under join: face(x) ∨ face(y) = face(x+y)), and (Lan F)(Q) = F(Phi_Q) on f.p. Q. Step 0 holds for all P.
- #17 (round3_q4): filtered colimits stay in the category; P = colim P_S; but valuations of P_S need not extend (N^2, S={e1,e1+2e2}), so covers do not descend naively; also "S large" needed for kernel descent.

## Dead ends (refuted statements only)
- #7/#10: "closed subdivision charts are birhizomic at wall valuations" — REFUTED by Lemma A (round2_q1). So birhizomic covers are not refinements of closed-chart subdivision covers.
- "pi^{-1} preserves injectives via exactness of pi_! (filtered comma categories)" — the comma categories are not filtered in general (round2 work); route not available (minor).

## Open gaps / set aside, not refuted
- Main gap: arbitrary P, the nerve statement (#19, see the chain below).
- Set aside, not refuted: reduction of arbitrary P to fine P_S via filtered unions (round3_q4: obstruction = non-extension of valuations; proposed fix = sites over P_S whose topology covers only Val(P)|_{P_S}, not carried out).
- Set aside, not refuted: "≺-openness of birhizomic loci" (round3_q3 heuristic: a member birhizomic at v contains a neighbourhood of v; Lemma A is the rank-one instance).
- Lemma K for arbitrary Q (patch compactness + quantifier elimination sketch in Background B) is not written out; round3_q1 proved it only for fine Q by a different argument.
- Finite rank but non-fg P (e.g. P = {x3 > 0} ∪ (N^2 × 0) ⊂ Z^3) is not settled either.

## The chain and the missing statement

**Chain.** Throughout, P is an arbitrary monoid. "f.p." means of finite presentation under the source. Coverings of an object Q of A_P^op are the birhizomic covers {Q -> Q_i} of Q. Fibre products are pushouts in the category of integral saturated sharp monoids. Composites and pushouts of f.p. maps are f.p.
1. (#16) B_P is equivalent to the poset of principal faces of P. This poset is directed, since face(x) ∨ face(y) = face(x+y). For f.p. Q, the comma category has the terminal object P[-x_Q]^sharp, so (Lan F)(Q) = F(Phi_Q). For an arbitrary Q, (Lan F)(Q) is a filtered colimit over the principal faces contained in Phi_Q. Hence Lan is exact, pi^{-1} = (Lan -)^sh is exact, and pi_* is restriction to B_P (round3_q1 Step 0, with "finite face poset" replaced by #16).
2. For a principal face tau and an abelian group A, define I_{tau,A}(b) = A if Phi_b ⊂ tau and 0 otherwise. Then Hom(F, I_{tau,A}) = Hom(F(tau), A). So F embeds into the (possibly infinite) product over tau of the I_{tau,E(F(tau))}, and iterating gives a resolution F -> I^• by products of such presheaves (round3_q1 Step 3).
3. On f.p. Q, Lan of a product is the product of the Lans, because Lan is evaluation at b(Q) there. Fix a covering of an f.p. Q. If Phi_Q ⊄ tau, the augmented Čech complex of Lan I_{tau,A} is zero. If Phi_Q ⊂ tau, it is the augmented ordered cochain complex, with coefficients A, of N_tau = {finite nonempty sigma ⊂ I : Phi_{Q_sigma} ⊂ tau}. Repeated indices are harmless: Phi of a pushout depends only on the set of indices, by the valuation description below.
4. **MISSING STATEMENT (#19):** N_tau is acyclic whenever Phi_Q ⊂ tau.
5. By 4, every augmented Čech complex of every Lan I^k on every covering of an f.p. object is exact, and products of exact complexes are exact. So Lan I^k, and hence Lan F as a kernel, satisfy the sheaf condition on coverings of f.p. objects. Coverings of f.p. objects, and their fibre products, consist of f.p. objects, so sheafification does not change the values on f.p. objects. Therefore pi_* pi^{-1} F = F (round3_q1 Step 5).
6. Apply Cartan's criterion (Stacks 03F7) with B = the f.p. objects and Cov = all coverings of f.p. objects. Each pi^{-1}I^k has vanishing positive-degree Čech cohomology on Cov, so H^{>0}(U, pi^{-1}I^k) = 0 for U in B. Since pi^{-1} is exact, H^p(U, pi^{-1}F) = H^p(I^•(Phi_U)) = 0 for p > 0. Finally R^p pi_* G = (b ↦ H^p(b, G)), because pi_* is restriction and preserves injectives, being right adjoint to an exact functor. Every P[-x]^sharp is f.p. So F -> R pi_* pi^{-1} F is a quasi-isomorphism, i.e. the [GOAL] holds (round3_q1 Step 6).

The derivation is that of #15 with "fine" removed. The only fine-specific inputs of #15 were Step 0 (now #16), Steps 1, 2 and 4 (all used only to prove 4 above), and the finiteness of the products in Step 3 (handled in 3).

**Missing statement (#19).** Let P be a monoid (integral, saturated, sharp, commutative; not necessarily finitely generated), and let f : P -> Q be of finite presentation in the category of integral saturated sharp monoids. Let {Q -> Q_i}_{i in I} be a birhizomic cover of Q in the sense of the problem, with Q in the role of P: each Q -> Q_i is f.p., and for every valuative V and every v : Q -> V there are i and g : Q_i -> V extending v such that Q -> Q_i is birhizomic at g. For each finite nonempty sigma ⊂ I, let Q_sigma be the pushout over Q of the Q_i (i in sigma) in that category, and let Phi_sigma = ker(P -> Q_sigma), a face of P. Let tau be a face of P generated by one element, with Phi_Q := f^{-1}(0) ⊂ tau. Then the simplicial complex N_tau = {sigma : Phi_sigma ⊂ tau} is nonempty and has vanishing reduced integral homology (equivalently, its augmented ordered cochain complex with coefficients in any abelian group A is exact).

Equivalent valuation form. Phi_sigma ⊂ tau holds iff some valuation v : Q -> V factors through every Q_i with i in sigma and satisfies v(x) > 0 for all x in P \ tau. Proof: by the order-extension theorem, Q_sigma has an injective valuation; conversely, compatible lifts define a map out of the pushout. So N_tau is the nerve of {E_i ∩ C_tau}, where E_i is the set of valuations of Q that factor through Q_i, and C_tau is the set of valuations with kernel on P contained in tau. Nonemptiness also follows: an injective valuation of Q lies in C_tau and factors through some Q_i.

**Why it should hold (director's sketch).**
(a) *Finite reduction.* Lemma K should hold for every Q, by the patch-compactness and quantifier-elimination argument: valuations are total preorders on Q^gp ⊗ Q, and each E_i is constructible. So a finite J_0 ⊂ I has E_i (i in J_0) covering all valuations.
(b) *Convexification.* Fix a finite subcomplex L of N_tau, let J' = vert(L) ∪ J_0, and pick one witness valuation v_sigma in E_sigma ∩ C_tau for each simplex sigma of N_tau(J'). Embed all value groups into one ordered R-vector space H (a Hahn product) and set w_λ = Σ λ_sigma v_sigma for λ in the standard simplex Δ.
  - The kernel of w_λ on Q is the intersection of the kernels of the v_sigma with λ_sigma > 0, because there is no cancellation among nonnegative elements. So w_λ lies in C_tau.
  - K_i := {λ : w_λ in E_i} is convex, since a convex combination of lifts is a lift.
  - The K_i (i in J') cover Δ, and their nerve is exactly N_tau(J').
(c) *What is missing* is a nerve theorem for this finite convex but non-closed cover; [0,1) ∪ [1,2] shows that one is needed. The birhizomic condition should supply it via an "openness lemma" generalising Lemma A and R4. If Q -> Q_i is birhizomic at a lift of w, then E_i contains every valuation obtained from w by a perturbation that is infinitesimal in the ≺ sense. One candidate: w(a) > 0 together with w(b+c) ≺ w(a) for the R4-generators a = b - c should be necessary as well as sufficient. Along segments t ↦ t w + (1-t) w' there is no cancellation in w_t(b+c), and |w_t(a)| ≤ w_t(b+c). So the R4 condition "lead coefficient of w_t(a) at the leading level of w_t(b+c) is > 0" is open in t on (0,1). With this, a lexicographic nerve theorem, proved by induction on dimension or rank as in the tangent-cone proof of Lemma K in round3_q1, should give contractibility of N_tau(J').
(d) *Alternative mechanism.* Treat the valuation space X(Q), topologised by birhizomic loci, as a space whose sheaves model Sh(A_P) over Q. Then show C_tau is acyclic by a homotopy through refinements (w ⇝ (w, w_0) lexicographic), since a refinement of w lies in every birhizomic locus containing w (the Lemma A pattern).

**Tried so far (on #19 or its earlier wording #14).**
- round3_q2, a direct positive proof. It yielded principal kernels (#16). The nerve was not settled; the suggested reduction to a fine P_0 fails because covers do not restrict.
- round3_q3, a counterexample hunt. No counterexample was found. Sign splits cannot disconnect N_tau, and closed-side splits are not birhizomic at the boundary (Lemma A pattern). It proposed the "≺-openness of birhizomic loci" lemma.
- round3_q4, reduction to fine P_S by filtered unions. The obstruction is that valuations of P_S need not extend. A modified-site idea over P_S was proposed but not carried out.

## Target for round 5 wave (composed in round 4; escalation rules apply)

**Progress test.** The last two rounds made progress on the chain. #16 (round3_q2, independently round3_q4) holds for every P and removes Step 0 from the chain, reducing it to the single nerve statement #19. #15 (fine P) is a solved special case recorded under Standing results; by itself it does not count as progress.

**Wave (9 queries, all `kind: attempt`, all on #19).**
- q1 = q2 = q3 = q9: the closing task, byte-identical. It contains the full statement of #19, the spliced proofs (Background A, round3_q1 in full, round3_q2 Part 1, round3_q4 §1–2, round3_q3 hunt section), the chain, and the sketch.
- q4: refute #19 exactly as stated. This is the first wave since the wording changed.
- q5: the hardest step of the sketch, posed on its own. Prove an openness lemma for birhizomic loci (a converse of R4) plus a lexicographic nerve theorem for the convexified cover, and from them deduce #19.
- q6: approach (d), a valuation space with the birhizomic topology and a homotopy or acyclicity argument for C_tau through refinements.
- q7: finite-data transfer. Use Lemma K for arbitrary Q, then try to build a fine model (P', Q', covering) whose nerve contains the given finite subcomplex and is computable by #15. This is a different reduction from round3_q4's P_S unions: it builds models from the finitely many witness valuations and generators rather than descending covers.
- q8: a structure theorem for birhizomic morphisms. Characterize Q -> Q' birhizomic at g via R4 data and localizations, and from that compute N_tau via refinement to standard covers.

**Afterwards.**
- If a proof of #19 returns, record the [GOAL] as PROVED, citing #15, #16 and the new file. Send two verify queries carrying the whole chain: round3_q1 + round3_q2 Part 1 + the new proof + the chain text above.
- If q4 refutes #19, the counterexample should give a NO to the goal via the chain. Check whether it really gives nonvanishing H^1 or an H^0 failure; it would then become the [GOAL] refutation candidate and needs verify queries.
