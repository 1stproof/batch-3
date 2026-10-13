# Task: a complete rigorous write-up of the sheaf-theoretic part of the proof (arbitrary P)

**Context.** The answer to the question is claimed to be YES for every monoid P (integral, saturated, sharp; not necessarily finitely generated). The proof splits into a combinatorial part and a sheaf-theoretic part.

The combinatorial part is already proved. You may use the following two results as given.

**Result B (principal kernels).** For every monoid P and every f.p. map f : P -> Q, the kernel face Phi_Q = f^{-1}(0) is generated, as a face, by a single element x_Q. Its proof is reproduced below for reference.

**Result D (nerve statement).** Let P be a monoid and f : P -> Q a homomorphism. Let tau be any subset of P containing Phi_Q. Let {Q -> Q_i}_{i in I} be a family of f.p. maps such that every valuation of Q factors through some member. For finite nonempty sigma ⊂ I:
- let Q_sigma be the pushout over Q of the Q_i, i in sigma;
- let Phi_sigma = ker(P -> Q_sigma);
- let N_tau = {sigma : Phi_sigma ⊂ tau}.

Then N_tau is nonempty, and its augmented ordered chain complex, and its augmented ordered cochain complex with any coefficients, are exact.

**What to write.** Write a complete, rigorous, self-contained proof of the sheaf-theoretic part. That is, deduce from Results B and D that F -> R pi_* pi^{-1} F is a quasi-isomorphism for every monoid P and every presheaf of abelian groups F on B_P^op. Below are the chain derivation and the earlier text for finitely generated P, which your write-up should generalize and make airtight. In particular, treat each of the following in full.

1. **The categories.**
   - B_P is equivalent to the directed poset of principal faces. Here you need: a map P[-x]^sharp -> Q under P exists iff f(x) = 0, and is then unique.
   - Presheaves on B_P^op and on A_P^op are covariant functors on B_P and A_P.
   - Compute the left Kan extension, and identify it on f.p. objects with Q ↦ F(Phi_Q).
   - Show that Lan is exact for arbitrary objects, as a filtered colimit, so pi^{-1} = (Lan -)^sh is exact.
   - Show that pi_* is restriction, and that the unit is the identity on f.p. objects once step 4 below is done.
   - State clearly any set-theoretic or universe conventions you need, since A_P is large.
2. **The injectives I_{tau,A}.**
   - Show Hom(F, I_{tau,A}) = Hom(F(tau), A).
   - Embed F into the possibly infinite product over tau of the I_{tau,E(F(tau))}, and build the resolution.
3. **The Čech complexes.**
   - For a covering of an f.p. object Q all of whose members are f.p., show the augmented Čech complex of Lan I_{tau,A} is 0 if Phi_Q ⊄ tau, and otherwise is the augmented ordered cochain complex of N_tau. Repeated indices are allowed; explain why they are harmless.
   - Lan commutes with products on f.p. objects.
4. **Coverings with non-f.p. members (important).**
   - A birhizomic cover is a family of morphisms P -> Q_i (here, over an object Q) such that every valuation factors through some member that is birhizomic at that factorization. "Birhizomic" includes "f.p.", but members that serve as no such witness need not be f.p.
   - Show that the witness subfamily is again a birhizomic cover and refines the original. Hence the coverings of f.p. objects whose members are all f.p. are cofinal among all coverings of f.p. objects, and their iterated fibre products are f.p.
   - Deduce that a presheaf satisfying the sheaf condition for this cofinal system Cov is unchanged on f.p. objects by sheafification (plus construction applied twice).
   - Handle both readings of "the birhizomic covers form a Grothendieck topology": covering families of a pretopology, or generators of the covering sieves.
5. **Cohomology.**
   - State Cartan's criterion precisely, with its hypotheses on B and Cov, and either prove it or cite it exactly (Stacks Project, tag 03F7, or the lemma it refers to).
   - Verify each hypothesis in this situation.
   - Deduce H^p(U, pi^{-1}F) = 0 for p > 0 and U f.p.
   - Show R^p pi_* G = (b ↦ H^p(b, G)): pi_* is right adjoint to an exact functor, so it preserves injectives.
   - Conclude that F -> R pi_* pi^{-1} F is a quasi-isomorphism, noting that every P[-x]^sharp is f.p.
   - Check carefully that the identification at the level of derived categories is compatible with the given morphism F -> R pi_* pi^{-1} F (the derived unit).

If you find any step that is false or cannot be repaired, say so explicitly. That would be the most valuable outcome. Otherwise end with a clean statement of what has been proved, from what.

(Conventions: "monoid" = integral, saturated, sharp, commutative. "f.p." = of finite presentation, i.e. compact in the under-category of integral saturated sharp monoids. Fibre products in A_P^op are pushouts in that category. A valuation of M is a homomorphism M -> V with V valuative.)

---------------------------------------------------------------------
## The chain derivation (as recorded)

**Chain.** Throughout, P is an arbitrary monoid. "f.p." means of finite presentation under the source. Coverings of an object Q of A_P^op are the birhizomic covers {Q -> Q_i} of Q. Fibre products are pushouts in the category of integral saturated sharp monoids. Composites and pushouts of f.p. maps are f.p.
1. (#16) B_P is equivalent to the poset of principal faces of P. This poset is directed, since face(x) ∨ face(y) = face(x+y). For f.p. Q, the comma category has the terminal object P[-x_Q]^sharp, so (Lan F)(Q) = F(Phi_Q). For an arbitrary Q, (Lan F)(Q) is a filtered colimit over the principal faces contained in Phi_Q. Hence Lan is exact, pi^{-1} = (Lan -)^sh is exact, and pi_* is restriction to B_P (round3_q1 Step 0, with "finite face poset" replaced by #16).
2. For a principal face tau and an abelian group A, define I_{tau,A}(b) = A if Phi_b ⊂ tau and 0 otherwise. Then Hom(F, I_{tau,A}) = Hom(F(tau), A). So F embeds into the (possibly infinite) product over tau of the I_{tau,E(F(tau))}, and iterating gives a resolution F -> I^• by products of such presheaves (round3_q1 Step 3).
3. On f.p. Q, Lan of a product is the product of the Lans, because Lan is evaluation at b(Q) there. Fix a covering of an f.p. Q. If Phi_Q ⊄ tau, the augmented Čech complex of Lan I_{tau,A} is zero. If Phi_Q ⊂ tau, it is the augmented ordered cochain complex, with coefficients A, of N_tau = {finite nonempty sigma ⊂ I : Phi_{Q_sigma} ⊂ tau}. Repeated indices are harmless: Phi of a pushout depends only on the set of indices, by the valuation description below.
4. **MISSING STATEMENT (#19):** N_tau is acyclic whenever Phi_Q ⊂ tau.
5. By 4, every augmented Čech complex of every Lan I^k on every covering of an f.p. object is exact, and products of exact complexes are exact. So Lan I^k, and hence Lan F as a kernel, satisfy the sheaf condition on coverings of f.p. objects. Coverings of f.p. objects, and their fibre products, consist of f.p. objects, so sheafification does not change the values on f.p. objects. Therefore pi_* pi^{-1} F = F (round3_q1 Step 5).
6. Apply Cartan's criterion (Stacks 03F7) with B = the f.p. objects and Cov = all coverings of f.p. objects. Each pi^{-1}I^k has vanishing positive-degree Čech cohomology on Cov, so H^{>0}(U, pi^{-1}I^k) = 0 for U in B. Since pi^{-1} is exact, H^p(U, pi^{-1}F) = H^p(I^•(Phi_U)) = 0 for p > 0. Finally R^p pi_* G = (b ↦ H^p(b, G)), because pi_* is restriction and preserves injectives, being right adjoint to an exact functor. Every P[-x]^sharp is f.p. So F -> R pi_* pi^{-1} F is a quasi-isomorphism, i.e. the [GOAL] holds (round3_q1 Step 6).

The derivation is that of #15 with "fine" removed. The only fine-specific inputs of #15 were Step 0 (now #16), Steps 1, 2 and 4 (all used only to prove 4 above), and the finiteness of the products in Step 3 (handled in 3).

(Step 4 is Result D.)

---------------------------------------------------------------------
## Proof of Result B (source: round3_q2, Part 1, verbatim)

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

---------------------------------------------------------------------
## The earlier write-up for finitely generated P (source: round3_q1, verbatim). Steps 0, 3, 5 and 6 are the ones to generalize; Steps 1, 2 and 4 are replaced by Result D.

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
