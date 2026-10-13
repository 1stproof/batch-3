kind: attempt
Open question attempted: AUDIT of the headline claim recorded as ledger entry #22 ("PROVED: [GOAL] for every monoid P and every presheaf of abelian groups F on B_P^op, F -> R pi_* pi^{-1} F is a quasi-isomorphism — answer YES"). You are asked to verify a complete written proof chain, step by step.

# Task: verify a complete proof that the answer to the question is YES for every monoid P

Below is a complete written proof chain, assembled from several independent pieces. Your job is to be a careful, skeptical referee:

1. Check EVERY inference of every part below, in order: Part A (the chain derivation), Part B (principality of kernel faces), Part C (the sheaf-theoretic steps, as written for finitely generated P, which Part A reuses for arbitrary P), and Part D (the nerve statement for arbitrary P).
2. For each step, say whether it is correct, correct with a repairable gap (supply the repair), or wrong (give the reason, and a counterexample if you can).
3. Pay particular attention to the following points.
   - (a) Does Part D prove exactly what step 4 of Part A needs? That is: for every covering of an f.p. object Q, and every principal face tau with Phi_Q ⊂ tau, the augmented ordered cochain complex of N_tau with coefficients in any abelian group is exact.
   - (b) Part D's Lemma 1: the retract-of-a-finite-presentation argument, and the Fourier–Motzkin elimination over ordered divisible groups. Lemma 2: the kernel of P -> Q_sigma described through cones. Theorem T: the cone lemma, the base case, the row lemma, and the double-complex argument, including the boundary row/column q = -1, p = -1.
   - (c) In Part C, the steps written for fine P that Part A reuses for arbitrary P. These are Steps 0, 3, 5 and 6. Steps 1, 2 and 4 of Part C are fine-specific and are replaced, for arbitrary P, by Parts B and D. Check that nothing fine-specific is silently used in Steps 0, 3, 5 and 6: finiteness of the face poset, finiteness of products, fine-ness of f.p. objects.
   - (d) The point flagged in Part A, step 7: members of a birhizomic cover that are not witnesses need not be f.p. Is the cofinality repair given there correct and sufficient, both for the plus construction and for Cartan's criterion?
   - (e) The identification of pi_* with restriction, of R pi_* with b ↦ H^p(b, -), and of the unit F -> pi_* pi^{-1} F with the identity.
4. Standard results quoted from memory are allowed: Tychonoff, Zorn, Gordan's lemma, the universal coefficient theorem, the double-complex lemma, Cartan's criterion (Stacks 03F7), and that ordered chains compute simplicial homology. Check that each is quoted correctly and applied within its hypotheses.
5. End with an explicit verdict, one of:
   - "VERDICT: the chain proves the claim exactly as stated (YES for every monoid P and every F)";
   - "VERDICT: gap", naming the exact step and what is missing, and saying whether you can repair it;
   - "VERDICT: false", with the counterexample.

   A gap you can repair completely, with the repair written out, still counts as a proof; say so.

(Conventions throughout: "monoid" = integral, saturated, sharp, commutative. "f.p." = of finite presentation in that category, i.e. compact in the relevant under-category. Presheaves on A_P^op are covariant functors A_P -> Ab. Fibre products in A_P^op are pushouts in the category of integral saturated sharp monoids. Phi_Q denotes the kernel face f^{-1}(0) of the structure map f : P -> Q, and for a family {Q -> Q_i} and a finite nonempty index set sigma, Q_sigma is the pushout over Q of the Q_i, i in sigma, with Phi_sigma = Phi_{Q_sigma}. A "valuation" of a monoid M is a homomorphism M -> V with V valuative.)

---------------------------------------------------------------------
## PART A. The chain derivation (arbitrary P)

**Chain.** Throughout, P is an arbitrary monoid. "f.p." means of finite presentation under the source. Coverings of an object Q of A_P^op are the birhizomic covers {Q -> Q_i} of Q. Fibre products are pushouts in the category of integral saturated sharp monoids. Composites and pushouts of f.p. maps are f.p.
1. (#16) B_P is equivalent to the poset of principal faces of P. This poset is directed, since face(x) ∨ face(y) = face(x+y). For f.p. Q, the comma category has the terminal object P[-x_Q]^sharp, so (Lan F)(Q) = F(Phi_Q). For an arbitrary Q, (Lan F)(Q) is a filtered colimit over the principal faces contained in Phi_Q. Hence Lan is exact, pi^{-1} = (Lan -)^sh is exact, and pi_* is restriction to B_P (round3_q1 Step 0, with "finite face poset" replaced by #16).
2. For a principal face tau and an abelian group A, define I_{tau,A}(b) = A if Phi_b ⊂ tau and 0 otherwise. Then Hom(F, I_{tau,A}) = Hom(F(tau), A). So F embeds into the (possibly infinite) product over tau of the I_{tau,E(F(tau))}, and iterating gives a resolution F -> I^• by products of such presheaves (round3_q1 Step 3).
3. On f.p. Q, Lan of a product is the product of the Lans, because Lan is evaluation at b(Q) there. Fix a covering of an f.p. Q. If Phi_Q ⊄ tau, the augmented Čech complex of Lan I_{tau,A} is zero. If Phi_Q ⊂ tau, it is the augmented ordered cochain complex, with coefficients A, of N_tau = {finite nonempty sigma ⊂ I : Phi_{Q_sigma} ⊂ tau}. Repeated indices are harmless: Phi of a pushout depends only on the set of indices, by the valuation description below.
4. **MISSING STATEMENT (#19):** N_tau is acyclic whenever Phi_Q ⊂ tau.
5. By 4, every augmented Čech complex of every Lan I^k on every covering of an f.p. object is exact, and products of exact complexes are exact. So Lan I^k, and hence Lan F as a kernel, satisfy the sheaf condition on coverings of f.p. objects. Coverings of f.p. objects, and their fibre products, consist of f.p. objects, so sheafification does not change the values on f.p. objects. Therefore pi_* pi^{-1} F = F (round3_q1 Step 5).
6. Apply Cartan's criterion (Stacks 03F7) with B = the f.p. objects and Cov = all coverings of f.p. objects. Each pi^{-1}I^k has vanishing positive-degree Čech cohomology on Cov, so H^{>0}(U, pi^{-1}I^k) = 0 for U in B. Since pi^{-1} is exact, H^p(U, pi^{-1}F) = H^p(I^•(Phi_U)) = 0 for p > 0. Finally R^p pi_* G = (b ↦ H^p(b, G)), because pi_* is restriction and preserves injectives, being right adjoint to an exact functor. Every P[-x]^sharp is f.p. So F -> R pi_* pi^{-1} F is a quasi-isomorphism, i.e. the [GOAL] holds (round3_q1 Step 6).

The derivation is that of #15 with "fine" removed. The only fine-specific inputs of #15 were Step 0 (now #16), Steps 1, 2 and 4 (all used only to prove 4 above), and the finiteness of the products in Step 3 (handled in 3).

Step 4 is now PROVED by Part D below, in a stronger form: Part D's Theorem allows any map f : P -> Q, any subset tau ⊂ P containing Phi_Q, and any family of f.p. maps Q -> Q_i such that every valuation of Q factors through some member. Every birhizomic cover has this factorization property: by definition, every valuation v : Q -> V factors through some member Q -> Q_i (which is moreover birhizomic at that factorization).

7. **Members that are not witnesses (repair of round-3 Step 5.4).** By definition, a member Q -> Q_i of a birhizomic cover is guaranteed to be f.p. only if it is birhizomic at some factorization of some valuation; call such members witnesses. The witnesses alone form a birhizomic cover: every valuation still factors through a witness at which it is birhizomic. They generate a sieve contained in the sieve of the original family. So, for every f.p. object U, the coverings of U all of whose members are f.p. are cofinal among all coverings of U. Their fibre products (iterated pushouts under U) are f.p. too, since composites and pushouts of f.p. maps are f.p.
   - Take Cov := the set of coverings of f.p. objects all of whose members are f.p. Steps 5 and 6 are to be read with this Cov.
   - The sheaf condition, and the plus construction G^+(U) = colim over coverings of Ȟ^0, may be computed on a cofinal system of coverings.
   - Cartan's criterion requires exactly this cofinality.
   - If the birhizomic covers only generate the topology rather than being its coverings, covering sieves containing a birhizomic cover are cofinal, and the same argument applies.

---------------------------------------------------------------------
## PART B. Principality of kernel faces for every P (ledger #16; source: round3_q2, Part 1)

## Part (1). Theorem: for any monoid P and any f.p. f : P -> Q, Phi_Q = f^{-1}(0) is the face generated by a single element.

**Reduction to a finite presentation.** Q is a retract under P of Q' = (P (+) N^k / R)^{int,sat,sharp} with R finite. This is the standard description of compact objects in the under-category, which I cite from memory rather than prove. If maps Q -> Q' -> Q compose to id_Q under P, then ker(P->Q) = ker(P->Q'). Indeed, x killed in Q' implies x killed in Q. Conversely, if x is killed in Q, its image in Q' is the image of 0, which is 0.

**Kernel of P -> Q'.** Let G = (P^gp (+) Z^k)/L, where L is generated by l_j = r_j - s_j, j = 1..J. Let M0 be the image of P (+) N^k in G, and let M1 = {g : ng in M0 for some n >= 1} be its saturation. Then Q' = M1/M1^*. So x in P is killed iff its image is a unit of M1. This happens iff -nx in M0 for some n >= 1, i.e. iff -nx - p - m in L for some p in P and m in N^k (all taken in P^gp (+) Z^k). Write the element of L as sum c_j l_j with c in Z^J. The Z^k-component condition says c lies in K = {c in Z^J : Z^k-part of sum c_j l_j lies in -N^k}. K is the set of lattice points of a rational polyhedral cone, so it is a finitely generated monoid (Gordan). Let psi : K -> P^gp be the P^gp-part of c |-> -sum c_j l_j, and let Y = psi(K), a finitely generated submonoid of P^gp. Then x is killed iff nx + p in Y for some n >= 1 and p in P. Such an element y = nx + p lies in S := Y ∩ P, and nx <= y. Conversely, if nx <= y in S, then p := y - nx is in P. Hence

  Phi_Q = face of P generated by the submonoid S = Y ∩ P.

**Principality.** For s in S let F(s) be the face generated by s. Then F(s+t) is the join of F(s) and F(t), so the family {F(s)} is directed. I claim that a strictly increasing chain F(s_1) ⊊ F(s_2) ⊊ ... has length at most rk Y^gp + 1, which is finite.
- A face F of a saturated P satisfies F^gp ∩ P = F: if x = a - b with a, b in F, then x <= a, so x is in F.
- Put G_i = F(s_i)^gp ∩ Y^gp. Suppose some n s_{i+1} lies in G_i with n >= 1. Then n s_{i+1} is in F(s_i)^gp ∩ P = F(s_i), and since F(s_i) is a face, s_{i+1} is in F(s_i). That contradicts strictness.
- So the ranks of the G_i strictly increase.

Hence a maximal F(s) exists. By directedness it contains every F(t), so Phi_Q = F(s) with s in S. ∎

Consequence: Step 0 of Background B holds for every P. The comma category of b -> Q over B_P has the terminal object P[-s]^sharp, so (Lan F)(Q) = F(Phi_Q) on f.p. Q, and pi^{-1}F is the sheafification of F∘b. (For non-f.p. Q the kernel face need not be principal. Example: P valuative of infinite rank and P -> 0. These objects are irrelevant here because Cartan's criterion only uses the f.p. objects.)

(The "standard description of compact objects" cited at the start of Part B is proved in Part D, Lemma 1(i), in the same way for objects under P as for objects under Q.)

---------------------------------------------------------------------
## PART C. The sheaf-theoretic steps, as written for finitely generated P (ledger #15; source: round3_q1, verbatim)

Read Steps 0, 3, 5 and 6 with "finite poset of faces" replaced by "poset of principal faces" (Part B). Read "finite products" as "products": Lan is evaluation at b(Q) on f.p. Q, so it commutes with arbitrary products there, and Čech complexes of products are products of Čech complexes. Read "coverings of f.p. objects" as the cofinal Cov of Part A, step 7. Steps 1, 2 and 4 are superseded for arbitrary P by Part D. "Background B" refers to an outline that this text implements; it is not needed.

# Answer to round3_q1: the question for finitely generated P

**Result.** For every fine monoid P (finitely generated, saturated, sharp) and every presheaf of abelian groups F on B_P^op, the unit F -> R pi_* pi^{-1} F is a quasi-isomorphism. The proof follows Background B, with every step checked. Lemma K gets a new proof by induction on dimension using tangent cones and flag valuations; the Tychonoff / quantifier-elimination sketch is not used. All steps are proved below; I found no false step. Steps 2–6 rely on standard facts quoted from memory: Borsuk's nerve theorem, Cartan's criterion, and the local conic structure of polyhedra. The case of P not finitely generated is not treated and remains open.

Conventions are those of Background B. Presheaves on A_P^op are covariant functors A_P -> Ab. Objects are maps under P. Fibre products in A_P^op are pushouts in the category of integral saturated sharp monoids.

## Step 0: the Kan extension and the unit

**B_P is a preorder.**
- Let f : P -> Q be in A_P. A map P[-x]^sharp -> Q under P exists iff f(x) = 0, and it is then unique, by the universal property.
- Phi_Q := f^{-1}(0) is a face of P, because Q is sharp and integral.
- P is finitely generated, so Phi_Q is generated as a face by x_Q, the sum of the generators of P lying in Phi_Q. Hence f(x) = 0 iff x lies in Phi_Q iff the face of x is contained in Phi_Q.
- So B_P is equivalent to the finite poset of faces of P.
- The category of pairs (b, b -> Q) has the terminal object b(Q) = P[-x_Q]^sharp.

**The left Kan extension.** Let u : B_P^op -> A_P^op be the inclusion. The left Kan extension of presheaves is
(u_p F)(Q) = colim over the pairs (b, b -> Q in A_P) of F(b).
Because there is a terminal object, this equals F(b(Q)) = F(Phi_Q). So u_p F = F∘b, and u_p is exact, being evaluation at an object.
Hence pi^{-1} F = (F∘b)^sh, and pi^{-1} is exact.

**pi_* is restriction to B_P.** We have Hom(pi^{-1}F, G) = Hom_psh(F∘b, G) = Hom(F, G|_B). So pi_* G = G|_B.
For b in B_P we have b(b) = b. The unit F(b) -> (F∘b)(b) = F(b) is therefore the identity, and it remains so after sheafification once Step 5 shows that sheafification does not change values on f.p. objects.

## Step 1: kernel faces via real valuations

**f.p. objects over fine P are fine.**
- Every object Q is the filtered union of the saturations sat(S), taken in S^gp, of the finitely generated submonoids S ⊂ Q containing f(P).
- Such an sat(S) lies in Q, because Q is saturated: if x is in S^gp ⊂ Q^gp and nx is in Q, then x is in Q. It is sharp, being a submonoid of Q. It is finitely generated by Gordan's lemma.
- Filtered unions of integral saturated sharp monoids are again of that kind, and they are the colimit in this category.
- If Q is f.p., the identity of Q factors through some sat(S). So Q is a retract of a fine monoid, i.e. an image of a finitely generated one, hence fine.
- Pushouts and compositions of f.p. maps are f.p. So all the Q_sigma below are fine.

**Strictly positive functional.** A fine saturated sharp Q has a strictly positive functional w in Q^v_R, with w(q) > 0 for every q ≠ 0. Indeed, sharpness means that the dual cone has nonempty interior; take w in that interior. Hence
Phi_Q = {x in P : w(f x) = 0 for all w in Q^v_R}.

**Real valuations of a pushout.** R_{>=0} is a monoid of our kind. By the universal property, Hom(Q_sigma, R_{>=0}) is the set of compatible tuples of maps Q_i -> R_{>=0}. So the image of Q_sigma^v_R in Q^v_R is T_sigma, the intersection over i in sigma of the T_i.
Each T_i is a closed polyhedral cone, being the linear image of a polyhedral cone. Applying the formula above to Q_sigma gives
Phi_{Q_sigma} = {x in P : w(x) = 0 for all w in T_sigma}.

## Step 2: Lemma K (proved)

Put S = Q^v_R, a closed polyhedral cone in Hom(Q^gp, R) = R^n.

**Definition.** A flag (d_0, ..., d_m) of vectors *lies in* a closed polyhedral cone C if the sum over k of δ^k d_k lies in C for all sufficiently small δ > 0. Writing C = {ℓ_j >= 0}, this is equivalent to: for every j, the tuple (ℓ_j(d_0), ..., ℓ_j(d_m)) is >= 0 in the lexicographic order. Indeed, a polynomial in δ is >= 0 for all small δ > 0 iff its lowest nonzero coefficient is positive.

**Hypothesis (H): every flag lying in S lies in some T_i.** Proof of (H) from the cover property:
- Let V be the nonnegative part of R^{m+1} with the lexicographic order. V is a valuative monoid.
- A flag lying in S defines a valuation v : Q -> V, q ↦ (d_0(q), ..., d_m(q)).
- By the cover property, v factors through some Q_i -> V. The components of this lift give a flag (d'_k) in Hom(Q_i^gp, R) lying in Q_i^v_R. Its image is (d_k), so the sum of δ^k d_k lies in T_i for small δ.

**Local conic structure (standard).** Let C be a polyhedral set and w a point of C. Then TC_C(w) := {d : w + δd ∈ C for small δ > 0} is a closed polyhedral cone, cut out by the constraints active at w. There is a ball N around w with C ∩ N = (w + TC_C(w)) ∩ N.

**Lemma K.** Let S be a closed polyhedral cone in R^n and {T_i} a family of closed polyhedral cones T_i ⊂ S satisfying (H). Then finitely many T_i cover S.

*Proof.* Induction on n.

*Base case n = 0.* The flag (0) gives some T_i containing 0, so T_i = S.

*Reduction to a local statement.* Since everything is conic, and 0 is covered by the case m = 0, it suffices to cover a neighbourhood in S of each point w with |w| = 1. Compactness of S ∩ (unit sphere) then finishes the proof.

*The local cover at w.*
1. Let I_w = {i : w ∈ T_i}. Every cone TC_S(w) and TC_i(w), for i in I_w, contains the line Rw.
2. Put S' = TC_S(w)/Rw and T_i' = TC_i(w)/Rw in R^n/Rw, which has dimension n-1. These are closed polyhedral cones, T_i' ⊂ S'.
3. *(H) holds for S' and the T_i'.*
   - Take a flag (e_0, ..., e_m) lying in S', with lifts d_1, ..., d_{m+1}. Because TC_S(w) contains Rw, the flag (d_1, ..., d_{m+1}) lies in TC_S(w).
   - Put x_δ = sum of δ^{k-1} d_k. It lies in TC_S(w) and stays bounded. By local conic structure, w + δ x_δ lies in S for small δ. So the flag (w, d_1, ..., d_{m+1}) lies in S.
   - By (H) it lies in some T_i. Letting δ -> 0 gives w ∈ T_i, so i is in I_w.
   - By local conic structure of T_i, δ x_δ lies in TC_i(w), hence x_δ lies in TC_i(w). So the flag (e_k) lies in T_i'.
4. By induction, a finite set F ⊂ I_w of the T_i' covers S'. Hence the TC_i(w), i in F, cover TC_S(w).
5. Choose a ball N around w on which local conic structure holds for S and for the T_i, i in F. If x lies in S ∩ N, then x - w lies in TC_S(w), so x - w lies in TC_i(w) for some i in F, so x lies in (w + TC_i(w)) ∩ N ⊂ T_i. ∎

This yields a finite J_0 ⊂ I with the union of the T_i, i in J_0, equal to Q^v_R. (Note that Lemma A shows the cover property, not just covering of S by the T_i, is essential: S can be covered by infinitely many rays with no finite subcover.)

## Step 3: the Čech complex of I_{tau,A}∘b

**The presheaf I_{tau,A}.** Define I_{tau,A}(b) = A if Phi_b ⊂ tau, and 0 otherwise, with identity transition maps when both values are A.
- This is a functor: if b -> b', then Phi_b ⊂ Phi_b'. So a value A at b' forces the value A at b.
- A map F -> I_{tau,A} amounts to compatible maps F(b) -> A for Phi_b ⊂ tau. These are determined by their component at tau, since F(b) -> F(tau) -> A. Hence Hom(F, I_{tau,A}) = Hom(F(tau), A), and I_{tau,A} is injective when A is.
- F embeds into the product over the finitely many faces tau of I_{tau, E(F(tau))}, where E denotes the injective hull. Iterating this embedding on cokernels gives injective resolutions by finite products of such presheaves.

**Identification of the Čech complex.** Let G = I_{tau,A}∘b and let {Q -> Q_i} be a covering of an f.p. object Q.
- G(Q_sigma) = A iff Phi_{Q_sigma} ⊂ tau.
- This holds iff T_sigma meets C := {w ∈ S : w(x) > 0 for all x ∈ P \ tau}.
  - (⇐) A point of T_sigma ∩ C kills nothing outside tau.
  - (⇒) Let w_0 be the sum of the generators of the polyhedral cone T_sigma. Then ker(w_0) ∩ P = Phi_{Q_sigma} ⊂ tau, so w_0 lies in C.
- C is convex: it suffices to impose w(x) > 0 on the finitely many generators of P outside tau.
- Transition maps between nonzero terms are identities.

So the Čech complex of G on the covering is the ordered cochain complex, with coefficients A, of N_tau = {finite tuples sigma : T_sigma ∩ C ≠ ∅}, the nerve of {T_i ∩ C}. (The empty tuple corresponds to Q itself.) The ordered cochain complex computes the simplicial cohomology of N_tau (standard).

## Step 4: N_tau is contractible

**If C ∩ S is empty**, then N_tau is empty and G(Q) = 0, so all Čech groups vanish.

**Otherwise:**
1. Take a finite subcomplex L of N_tau, and let J' = vertices(L) ∪ J_0, which is finite.
2. Choose a witness point in T_sigma ∩ C for each simplex sigma of N_tau(J'). Let D be their convex hull. D is compact, convex, nonempty and contained in C.
3. The sets T_i ∩ D, i in J', are compact and convex. They cover D, because D ⊂ S is covered by the T_i, i in J_0.
4. Their nerve is exactly N_tau(J'): it is contained in N_tau(J') because D ⊂ C, and it contains N_tau(J') because of the witnesses.
5. **Nerve theorem (Borsuk 1948; Leray), quoted from memory:** the nerve of a finite family of compact convex sets in R^n is homotopy equivalent to their union. Hence N_tau(J') ≃ D, which is contractible.
6. So every finite subcomplex lies in a contractible finite subcomplex. Therefore the reduced homology of N_tau vanishes, since homology commutes with this direct limit.
7. The augmented chain complex is then a free acyclic complex, so it is split exact. Applying Hom(-, A) gives cohomology A in degree 0 and 0 in degrees > 0.

**Conclusion.** The Čech cohomology of G on every covering of every f.p. object is G(Q) in degree 0 and 0 in positive degrees.

## Step 5: the sheaf property

1. Take 0 -> F -> I^0 -> I^1 with I^0, I^1 finite products of injectives of the form I_{tau,A}.
2. Composing with b is exact. The Čech H^0 is left exact.
3. By Step 4, I^0∘b and I^1∘b satisfy the sheaf condition on all coverings of f.p. objects. Hence so does F∘b, as a kernel.
4. Coverings of f.p. objects, and all their fibre products, consist of f.p. objects, because birhizomic maps are f.p. by definition.
5. So the plus construction does not change values on f.p. objects: pi^{-1}F(Q) = F(Phi_Q) for f.p. Q, and pi_* pi^{-1} F = F via the unit, which is the identity by Step 0.

## Step 6: higher vanishing

**Cartan's criterion** (Stacks Project, tag 03F7, from memory). Let B be a set of objects of a site and Cov a set of coverings such that:
- every covering in Cov is a covering of an object of B and has its members in B;
- all fibre products U_{i_0} × ... × U_{i_p} of a covering in Cov lie in B;
- for U in B, the coverings of U in Cov are cofinal among all coverings of U.

If a sheaf G has Ȟ^p(𝒰, G) = 0 for all 𝒰 in Cov and all p > 0, then H^p(U, G) = 0 for all U in B and all p > 0.

**Application.**
- Take B = f.p. objects and Cov = all coverings of objects in B. The hypotheses hold: cofinality is trivial, and the members and fibre products are f.p.
- G = pi^{-1}I_{tau,A} agrees with I_{tau,A}∘b on B by Step 5, so Step 4 gives the required Čech vanishing. Finite products of such G are acyclic as well.
- Since pi^{-1} is exact, pi^{-1}F -> pi^{-1}I^• is a resolution by sheaves acyclic on B.
- For U in B, H^p(U, pi^{-1}F) is therefore the p-th cohomology of I^•(Phi_U), which is exact in degrees > 0. So H^p(U, pi^{-1}F) = 0 for p > 0.

**R^p pi_*.** pi_* is right adjoint to the exact functor pi^{-1}, so it preserves injectives. It is restriction to B. Hence R^p pi_* G is the presheaf b ↦ H^p(b, G). Every P[-x]^sharp is f.p., so R^p pi_* pi^{-1} F = 0 for p > 0, and R^0 pi_* pi^{-1} F = F.

**Answer: YES for finitely generated P.**

## Sanity check: P = N^2

The faces are 0, ⟨e1⟩, ⟨e2⟩ and N^2, so S = R_{>=0}^2 and C is respectively:
- tau = 0: the open quadrant;
- tau = ⟨e1⟩: {w_1 = 0, w_2 > 0};
- tau = ⟨e2⟩: {w_1 > 0, w_2 = 0};
- tau = N^2: all of S.

Consider a cover made of the three localizations P[-e1]^sharp, P[-e2]^sharp, P[-e1-e2]^sharp, together with finitely many R4-type open cones. Here T for P[-e1]^sharp is the ray {w_1 = 0}.

Coverage must include the flag valuations at the boundary rays. For example, the flag (w, d) = ((0,1), (1,0)) must lie in some T_i, so some T_i is a 2-dimensional cone containing the ray w_1 = 0. For tau = ⟨e1⟩, the members meeting C are the localization at e1 and the cones containing that ray. They pairwise meet along that ray inside C, so N_tau is a full simplex, which is contractible. The other three faces behave the same way. This is consistent with the general proof.

## Status

- **Proved:** the full statement for fine P (Steps 0–6 and Lemma K, the latter via a new tangent-cone induction).
- **Quoted from memory:** Borsuk's nerve theorem, Cartan's criterion (Stacks tag 03F7), and the local conic structure of polyhedra.
- **Open:** non-finitely-generated P. There Step 0 (principal kernel faces), Step 1 (real valuations detecting kernels) and the nerve theorem for non-closed convex sets all fail or are unverified; see the Remark in Background B.

---------------------------------------------------------------------
## PART D. The nerve statement for arbitrary P (ledger #20; source: round4_q7, verbatim)

# round4_q7: proof of #19

**Plan (written first).** I prove #19 as stated, for every P. I do not use the suggested fine-model transfer; Section 7 explains why. The proof has four steps.
(a) Each locus E_i is cut out by finitely many non-strict sign conditions x ∈ W, with x in U := Q^gp ⊗ Q.
(b) The nerve condition Φ_σ ⊂ τ is a condition on the cone Q_Q + cone(X_σ).
(c) Compactness gives a finite subcover.
(d) An abstract acyclicity theorem, proved by induction on the number of "undecided" sign conditions. The induction step refines the cover by the two-member sign cover {z ≥ 0}, {z ≤ 0} and uses the standard double-complex comparison of Čech complexes.

Status: **all steps proved below.**

---

## 0. Result

**Theorem.** Let P be any monoid, f : P → Q any map in 𝒞 (the category of integral, saturated, sharp commutative monoids), and {Q → Q_i}_{i∈I} a family of f.p. maps under Q. Assume that every valuation v : Q → V factors through some Q_i. Let τ ⊂ P be any subset with Φ_Q := f^{-1}(0) ⊂ τ. Then:
- N_τ = {σ ⊂ I finite nonempty : Φ_σ ⊂ τ} is nonempty;
- its augmented ordered chain complex is exact, so its reduced integral homology vanishes;
- for every abelian group A, its augmented ordered cochain complex with coefficients A is exact.

In particular #19 holds. Three of its hypotheses are not needed: birhizomy (only "factors through some member" is used), f.p. of Q over P, and principality of τ.

"f.p." is read as: Hom_Q(Q_i, –) commutes with filtered colimits in 𝒞 under Q. If instead it means "presented by finitely many generators and relations", Lemma 1(i) below is immediate.

## 1. Cones and valuations

Put U = Q^gp ⊗ Q. Q^gp is torsion-free: if nx = 0, then x and −x lie in Q by saturation, so x = 0 by sharpness. So Q ⊂ U. Let Q_Q = Q_{≥0}·Q.

A *cone* is a subset K ⊂ U with 0 ∈ K, K + K ⊂ K and Q_{>0}K ⊂ K. Its lineality is lin K = K ∩ (−K). A cone is *total* if W ∪ (−W) = U.

- Q_Q has lineality 0. If x = q/n and −x = q'/n', then n'q + nq' = 0 in Q^gp, so q = q' = 0 by sharpness and torsion-freeness.
- A valuation v : Q → V gives the total cone W_v = {x ∈ U : v(x) ≥ 0 in V^gp ⊗ Q}, which contains Q_Q. (The divisible hull of an ordered group is ordered.)
- Conversely, a total cone W ⊃ Q_Q gives a valuation v_W : Q → V_W. Here V_W is the nonnegative part of the ordered Q-vector space H_W = U/lin W, with positive cone W/lin W. V_W is integral, saturated, sharp and totally ordered.

**Lemma Z.** Every cone K is contained in a total cone W with lin W = lin K.

*Proof.* Cones K' ⊃ K with lin K' = lin K are closed under unions of chains, so Zorn gives a maximal one, K'. Suppose x ∉ K' ∪ (−K'), and put K'' = K' + Q_{≥0}x. If y ∈ lin K'', write y = k_1 + ax and −y = k_2 + bx with a, b ≥ 0. Then k_1 + k_2 = −(a+b)x.
- If a + b > 0, then −x ∈ K', which is a contradiction.
- So a = b = 0, and y = k_1 ∈ lin K'.

Hence lin K'' = lin K'. Since K'' ⊋ K', this contradicts maximality, so K' is total. ∎

**Consequence (injective valuations).** Every M ∈ 𝒞 has a valuation ι : M → V with ι(m) = 0 only for m = 0. To see this, apply Lemma Z to M_Q ⊂ M^gp ⊗ Q, which has lineality 0 as shown above.

## 2. Lemma 1: loci are finite sign conditions

For each i let E_i be the set of total cones W ⊃ Q_Q such that v_W extends to Q_i, i.e. there is g : Q_i → V_W under Q.

**Lemma 1.** For each i there is a finite set X_i ⊂ U such that:
(a) E_i = {W : X_i ⊂ W};
(b) for any valuation v : Q → V, if v extends to Q_i, then X_i ⊂ W_v.

*Proof.*

(i) *Q_i is a retract under Q of a finitely presented object.* Write M = Q_i. For a finite S ⊂ M and a finite set R of relations r = s between elements of Q ⊕ N^S that hold in M, let T(S,R) be the image of (Q ⊕ N^S)/R after integralizing, saturating and sharpening.
- The pairs (S,R) form a directed poset.
- Filtered colimits of objects of 𝒞, computed in monoids, stay in 𝒞: integrality, nx = ny ⇒ x = y, saturation and sharpness are each witnessed at a finite stage.
- The map colim T(S,R) → M is surjective.
- It is injective. Let x, y lie at a common stage T and have the same image in M. Choose n with nx = [a] and ny = [b], where a, b ∈ Q ⊕ N^S; saturation gives this. Then (a,b) is a relation valid in M. Adding it to R makes nx = ny, hence x = y, because the groups are torsion-free.
- So M = colim T(S,R). By f.p., id_M factors through some T = T(S,R), and M is a retract of T under Q.

Maps out of a retract: v extends to M if and only if it extends to T. Compose with M → T → M in one direction and with T → M in the other.

(ii) *Extensions to T.* Let H be an ordered divisible group containing v(Q), with V ⊂ H_{≥0}. A map T → H_{≥0} under Q is the same as a vector y ∈ H^S with y ≥ 0 satisfying the relations. Indeed, a map from Q ⊕ N^S that respects R factors uniquely through integralization, saturation and sharpening, because H_{≥0} is integral, saturated and sharp.

Write the j-th relation as (a_j, α_j) = (b_j, β_j) with a_j, b_j ∈ Q and α_j, β_j ∈ N^S. It reads (α_j − β_j)·y = c_j, where c_j := v(b_j − a_j).

(iii) *Fourier–Motzkin.* Consider a finite system of rational linear inequalities in unknowns y and parameters c, over an ordered divisible group H. Eliminating one unknown replaces the system by the "lower bound ≤ upper bound" pairs together with the inequalities not involving that unknown. This preserves solvability in H: given the rest, take the unknown to be the maximum of its finitely many lower bounds (or the minimum of the upper bounds, or 0 if there are none).

Eliminating all y from {y ≥ 0, (α_j − β_j)·y = c_j} gives finitely many rational vectors u_m, independent of H, with:
solvable in H ⟺ u_m·c ≥ 0 for all m.

Put x_m = Σ_j u_{mj}(b_j − a_j) ∈ U and X_i = {x_m}. Then u_m·c = v(x_m).

Conclusion:
- For H = H_W this gives (a).
- For H = V^gp ⊗ Q, if v extends to Q_i then it extends to T inside H_{≥0}, so v(x_m) ≥ 0 for all m, i.e. X_i ⊂ W_v. This is (b). ∎

## 3. Lemma 2: the nerve condition as a cone condition

For finite σ ⊂ I put X_σ = ∪_{i∈σ} X_i and K_σ = Q_Q + cone(X_σ). For a cone K ⊃ Q_Q put f^{-1}(lin K) = {p ∈ P : f(p) ∈ lin K}.

Since f(p) ∈ Q_Q ⊂ K, this equals {p ∈ P : −f(p) ∈ K}.

**Lemma 2.** Φ_σ := ker(P → Q_σ) = f^{-1}(lin K_σ).

*Proof.* A map Q_σ → V_W under Q is the same as a family of maps Q_i → V_W under Q, i ∈ σ, because Q_σ is the pushout in 𝒞 and V_W ∈ 𝒞. So the set of W for which v_W extends to Q_σ is ∩_{i∈σ} E_i = {W ⊃ K_σ}.

(⊂) Suppose p ∈ Φ_σ. Take W ⊃ K_σ total with lin W = lin K_σ (Lemma Z). Then v_W extends to Q_σ and kills the image of p, so f(p) ∈ lin W = lin K_σ.

(⊃) Suppose f(p) ∈ lin K_σ. Let ι : Q_σ → V be injective (§1) and v = ι|_Q. Since v extends to every Q_i, i ∈ σ, Lemma 1(b) gives X_σ ⊂ W_v, so K_σ ⊂ W_v. Hence v(f(p)) = 0, i.e. ι(image of p) = 0, so the image of p is 0. ∎

Let 𝒢 = {cones K ⊃ Q_Q : f^{-1}(lin K) ⊂ τ}. Then:
- **N_τ = {σ : K_σ ∈ 𝒢}.**
- **(G0)** If Q_Q ⊂ K ⊂ K' and K' ∈ 𝒢, then K ∈ 𝒢.
- **(G1)** If K ∈ 𝒢 and W ⊃ K is total with lin W = lin K, then W ∈ 𝒢. The sets f^{-1}(lin ·) are equal.
- **(G2)** For any cone K ⊃ Q_Q and any z ∈ U, f^{-1}(lin(K + Qz)) = f^{-1}(lin(K + Q_{≥0}z)) ∪ f^{-1}(lin(K + Q_{≥0}(−z))). Indeed, write −f(p) = k + tz and split according to the sign of t. So if K ± z ∈ 𝒢, then K + Qz ∈ 𝒢.
- **(G3)** Q_Q ∈ 𝒢, because f^{-1}(lin Q_Q) = f^{-1}(0) = Φ_Q ⊂ τ. Here lin Q_Q = 0 and Q ⊂ U.

## 4. Lemma 3: finite subcover

The set 𝒯 of total cones W ⊃ Q_Q is closed in {0,1}^U. Each defining condition involves finitely many coordinates:
- z ∈ W or −z ∈ W;
- z, z' ∈ W ⇒ z + z' ∈ W;
- z ∈ W ⇒ rz ∈ W for r ∈ Q_{>0};
- q ∈ W for q ∈ Q_Q.

So 𝒯 is compact by Tychonoff. Each E_i = {X_i ⊂ W} is open. The E_i cover 𝒯: every W gives a valuation v_W, which factors through some Q_i by hypothesis. Hence a **finite J_0 ⊂ I has ∪_{i∈J_0} E_i = 𝒯.**

## 5. Theorem T: abstract acyclicity

Fix:
- a Q-vector space U and a cone K_0;
- a family 𝒢 of cones containing K_0, satisfying (G0), (G1) and (G2) for cones containing K_0;
- an abelian group A.

For a cone K ⊃ K_0 and a finite family (X_j)_{j∈J} of finite subsets of U, let C^•(K) be the augmented ordered Čech complex:
- C^p(K) = ∏_{(j_0,…,j_p) ∈ J^{p+1}} A(K + cone X_{j_0} + … + cone X_{j_p}) for p ≥ −1, where A(K') = A if K' ∈ 𝒢 and 0 otherwise;
- the maps between factors are the identity A → A or 0 (well defined by (G0));
- d is the alternating sum of the deletions.

When K ∈ 𝒢, this is the augmented ordered cochain complex of N(K) = {σ : K + cone X_σ ∈ 𝒢} with coefficients A.

**Theorem T.** If every total cone W ⊃ K contains some X_j, then C^•(K) is exact.

*Proof.* Induction on m(K) = #{z ∈ Z : z ∉ K and −z ∉ K}, where Z = ∪_j X_j is finite. If K ∉ 𝒢, then C^•(K) = 0 by (G0). So assume K ∈ 𝒢.

*Cone lemma.* Suppose there is j* such that σ ∈ N(K) ⇒ σ ∪ {j*} ∈ N(K), and {j*} ∈ N(K). Then (hc)(j_0,…,j_{p−1}) = c(j*, j_0,…,j_{p−1}) is well defined: if the tuple with j* added carries A, so does the tuple without it, by (G0). The usual computation gives dh + hd = id, including in degree −1. So C^• is contractible.

*Base case m(K) = 0.* Take W ⊃ K total with lin W = lin K (Lemma Z). Some X_{j*} ⊂ W. Let z ∈ X_{j*}.
- If z ∉ K, then −z ∈ K because z is decided, so z ∈ lin W = lin K ⊂ K, a contradiction.
- So X_{j*} ⊂ K, and K + cone X_{j*} = K. Hence j* is a cone point and the cone lemma applies.

*Row lemma.* For any cone K' ⊃ K_0 and z ∈ U, the augmented complex of the two-member family X_+ = {z}, X_− = {−z} on K' is exact. If K' ∉ 𝒢 it is zero. If K' ∈ 𝒢:
- By Lemma Z and (G1), some total W ∈ 𝒢 contains K'. Then W contains K' + z or K' − z, so at least one vertex lies in the nerve, by (G0).
- If both vertices lie in it, the edge does too, by (G2).

So the nerve is a vertex or an edge, and the cone lemma applies.

*Inductive step, m(K) > 0.* Pick an undecided z ∈ Z. Consider the double complex
D^{p,q} = ∏_{σ ∈ J^{p+1}, ρ ∈ {±}^{q+1}} A(K + cone X_σ + cone{ρ_0 z, …, ρ_q z}), for p, q ≥ −1,
with commuting deletion differentials in σ and in ρ.
- **Row p** is ∏_σ of the row-lemma complex on K + cone X_σ, hence exact.
- **Column q ≥ 0** is ∏_ρ of C^•(K_ρ), where K_ρ ∈ {K + Q_{≥0}z, K + Q_{≥0}(−z), K + Qz}. The cover hypothesis passes to K_ρ ⊃ K, and m(K_ρ) < m(K) because z is now decided. So these columns are exact by induction.
- **Column q = −1** is C^•(K).

Each total degree involves only finitely many (p, q). Exact rows make Tot D acyclic. The columns q ≥ 0 form a subcomplex whose total complex is acyclic, by filtering by q. The quotient by this subcomplex is column −1, so C^•(K) is exact. ∎

## 6. Proof of #19

1. Apply T with U = Q^gp ⊗ Q, K_0 = K = Q_Q, the family 𝒢 of §3, and the family (X_i)_{i∈J'} for any finite J' ⊃ J_0. The cover hypothesis holds by Lemma 3.
2. By Lemma 2, N(Q_Q) is the full subcomplex N_τ(J') of N_τ on J'. Hence the augmented ordered cochain complex of N_τ(J') with coefficients A is exact, for every A.
3. *Nonemptiness.* Take W_0 ⊃ Q_Q total with lin W_0 = 0. Then W_0 ∈ 𝒢 by (G3) and (G1). It contains some X_i, so K_i ⊂ W_0, so {i} ∈ N_τ by (G0).
4. *Exactness of the chain complex of N_τ(J').* Let C̃ be its augmented ordered chain complex, a complex of free abelian groups in degrees ≥ −1. The universal coefficient theorem gives a surjection H^n(Hom(C̃, A)) → Hom(H_n C̃, A). Taking A = H_n C̃ shows H_n C̃ = 0.
5. *Passage to the infinite complex.* The augmented ordered chain complex of N_τ is the directed union over finite J' ⊃ J_0 of these complexes, so it is exact. Its reduced homology, which is simplicial reduced homology, vanishes.
6. *Cochains of N_τ.* An exact complex of free abelian groups bounded below is split, since subgroups of free groups are free. So Hom(–, A) of it is exact, i.e. the augmented ordered cochain complex of N_τ is exact for every A.

This is what steps 3–6 of the chain use. ∎

## 7. Remarks

**Why I departed from the fine-model transfer.** Lemma 1 already turns everything into finitely many sign conditions inside the true cone Q_Q ⊂ Q^gp ⊗ Q. The proof never passes to the fine submonoids P_S. So the round3_q4 obstruction does not arise: no valuation of a smaller monoid that fails to extend ever needs to be covered.

Outer polyhedral models would in fact fail. Take the valuative Q_0 = {x > 0} ∪ {x = 0, y ≥ 0}. Every rational polyhedral cone containing it also contains −(0,1), which creates spurious lineality.

**Consistency with #15.** The argument reproves the fine case (#15, Steps 2–4) without Lemma K's tangent-cone induction and without the nerve theorem.

**Possible gap in the chain, outside #19 (flagged, not resolved).** A birhizomic cover need only have f.p. members among those that serve as birhizomic witnesses. Chain step 5 asserts that all members of a covering of an f.p. object are f.p. To support that, one should either restrict to the subfamily of witnesses, which is itself a birhizomic cover with all members f.p., and argue with sieves, or check this point separately.

## 8. Status

- **Proved:** #19 exactly as stated, in the stronger form of §0. Every step has its proof written out here, apart from the standard facts listed next.
- **Standard facts used, not reproved:**
  - Tychonoff's theorem;
  - the double-complex comparison (a double complex in the region p, q ≥ −1 with exact rows has an acyclic total complex);
  - the universal coefficient theorem for complexes of free abelian groups;
  - ordered chains compute simplicial homology.
- **Open within this file:** nothing for #19. The chain-level f.p.-membership point in §7 is outside the statement of #19 and is left unchecked here.


---------------------------------------------------------------------
## Reminder of what to deliver
Give a step-by-step check of Parts A–D as instructed above. End with the explicit VERDICT line on whether the chain proves, exactly as stated in the problem, that F -> R pi_* pi^{-1} F is a quasi-isomorphism for every monoid P and every presheaf of abelian groups F on B_P^op.
