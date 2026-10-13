# round5_q2: audit of the chain proving YES for every monoid P

Plan: check Parts B, D, A, C in dependency order. For each step the verdict is one of: correct, repairable gap (with the repair written out), or wrong. The verdict is at the end.

Conventions: 𝒞 is the category of integral, saturated, sharp commutative monoids. "f.p." means compact in the relevant under-category. Presheaves on A_P^op are covariant functors A_P -> Ab.

## Preliminary facts used repeatedly (all checked)

**(F1) Filtered colimits.** A filtered colimit of objects of 𝒞, computed in monoids, lies in 𝒞, because each axiom is witnessed at a finite stage.
- Integral: a+c = b+c in the colimit already holds at some stage, so a = b there.
- Saturated: if x is in the colimit group and nx lies in the colimit, then both facts hold at some stage, so x lies in that stage.
- Sharp: x+y = 0 holds at some stage.

**(F2) Composites and pushouts of f.p. maps are f.p.**
- Composites: Hom_P(Q', M) is the disjoint union over a in Hom_P(Q, M) of Hom_Q(Q', M via a). Both kinds of Hom-set commute with filtered colimits.
- Pushouts: Hom_{Q'}(Q' ⊔_Q Q_i, M) = Hom_Q(Q_i, M).

**(F3) P -> P[-x]^sharp.** This map is f.p. and its kernel face is face(x) = {y : y <= nx for some n}.
- Hom_P(P[-x]^sharp, M) is a point if x maps to 0 and empty otherwise. By (F1), "x maps to 0 in colim M_k" already holds at some stage.
- The units of P[-x] are the y - nx with y <= nx. So y in P dies iff y is in face(x).
- Hence there is a map P[-x]^sharp -> P[-y]^sharp under P iff face(x) ⊂ face(y), and it is then unique.
- So B_P is equivalent to the poset of principal faces. This poset is directed, since face(x) ∨ face(y) = face(x+y).

**(F4) Torsion-freeness.** M^gp is torsion-free for M in 𝒞: if nx = 0, then x and -x lie in M by saturation, so x = 0 by sharpness. Consequently nx = ny implies x = y.

## Part D (checked first, because Part B cites its Lemma 1(i))

**§1. Correct.**
- Torsion-freeness of Q^gp and the embedding Q ⊂ U are correct (F4).
- lin Q_Q = 0 is correct.
- W_v is a total cone containing Q_Q. The divisible hull of a totally ordered abelian group is totally ordered.
- V_W := W/lin W is valuative in the sense of the problem. Its group is U/lin W = H_W, since W ∪ (-W) = U, and the order on H_W is total.
- V_W is in 𝒞. It is integral as a submonoid of a group. It is saturated: in an ordered group, x < 0 implies nx < 0. It is sharp.
- Lemma Z (Zorn) is correct.
  - The union of a chain of cones with lineality lin K is a cone with lineality lin K.
  - For the extension step, k_1 + k_2 = -(a+b)x. If a+b > 0, dividing by a+b puts -x in K', a contradiction. Otherwise y = k_1 and -y = k_2 both lie in K'.
- The injective valuation is correct. Apply Lemma Z to M_Q, which has lineality 0. Then v_W(m) = 0 forces m ∈ lin W = 0.

**§2, Lemma 1. Correct, with one wording repair.**
- (i) "T(S,R) := the image of (Q⊕N^S)/R after integralizing, saturating and sharpening" must be read as the object (Q⊕N^S/R)^{int,sat,sharp}, not as its image in M. The image in M need not be f.p.
- With that reading the argument is correct.
  - The (S,R) are directed, and the colimit is computed in monoids (F1).
  - Every element x of T(S,R) has a multiple nx in the image of Q⊕N^S, by construction of the saturation.
  - The relation (a,b) holds in M, so adding it gives nx = ny at a later stage, hence x = y (F4). So colim T(S,R) -> M is bijective, hence an isomorphism in 𝒞 under Q.
  - Compactness gives a section s : M -> T, so M is a retract of T. The "extends to M iff extends to T" argument is correct.
- (ii) Correct. H_{>=0} lies in 𝒞, so maps out of Q⊕N^S that respect R factor uniquely through the int/sat/sharp reflection. The relation (a_j,α_j) = (b_j,β_j) becomes (α_j - β_j)·y = v(b_j) - v(a_j). Here v is extended Q-linearly to U -> H, which is possible because H is divisible.
- (iii) Fourier–Motzkin over a totally ordered Q-vector space H is correct.
  - Every constraint is homogeneous in (y, c), of the form ">= 0" or "= 0". Each "= 0" is two ">= 0".
  - When eliminating one unknown, dividing by positive rationals preserves order. Since H is totally ordered, a finite set of lower bounds has a maximum, which is <= every upper bound.
  - The elimination is purely syntactic, so the final system "u_m·c >= 0" does not depend on H. No strict inequalities ever arise.
- The conclusions (a) and (b) are correct.
  - For (a), v_W(x) >= 0 in H_W iff x ∈ W + lin W = W.
  - For (b), only "v extends to Q_i ⇒ v extends to T inside V ⊂ (V^gp⊗Q)_{>=0}" is needed, and that is true.

**§3, Lemma 2 and (G0)–(G3). Correct.**
- The pushout property and V_W ∈ 𝒞 give: v_W extends to Q_σ iff W ⊃ K_σ.
- The argument works verbatim for tuples with repeated indices: maps out of Q_i ⊔_Q Q_i are pairs of maps. So Φ of an iterated pushout depends only on the underlying set of indices, as Part A step 3 needs.
- (⊂) is correct.
- (⊃) is correct. If v(f(p)) is both >= 0 and <= 0, it is 0 in V^gp ⊗ Q. Since V^gp is torsion-free, it is 0 in V, and injectivity of ι on 0 finishes.
- For cones K ⊃ Q_Q ⊃ f(P), f^{-1}(lin K) = {p : -f(p) ∈ K}.
- (G0), (G1) and (G3) are immediate.
- (G2): write -f(p) = k + tz and split according to the sign of t. This is correct.

**§4, Lemma 3. Correct.**
- 𝒯 is an intersection of conditions, each involving finitely many coordinates, so it is closed in {0,1}^U and compact by Tychonoff.
- E_i = {X_i ⊂ W} is clopen, because X_i is finite.
- The E_i cover 𝒯 because v_W factors through some member. "Factors through Q_i" means exactly "extends to Q_i under Q".

**§5, Theorem T. Correct, with one misstated justification.**
- Well-definedness of C^•: a coface map goes from a tuple to a larger tuple. If the larger cone is in 𝒢, so is the smaller one, by (G0). So each component is the identity A -> A or a map to 0. This is the Hom(-, A) dual of the ordered chain complex of the downward-closed family N(K).
- **Cone lemma.** The file justifies h by "if the tuple with j* added carries A, so does the tuple without it, by (G0)". That is the wrong direction. The fact needed is the hypothesis itself: if the target tuple τ' carries A, i.e. τ' ∈ N, then τ' ∪ {j*} ∈ N, so the source carries A too, and h is the identity there. (When τ' ∉ N the target is 0.)
  - With this, the identity dh + hd = id holds componentwise on tuples in N, all of whose relevant neighbours are in N, and trivially on tuples not in N.
  - In degree -1, (hdc)() = (dc)(j*) = c needs {j*} ∈ N, which is assumed.
  - **Repair:** replace that sentence by the one above. Nothing else changes.
- **Base case.** Correct. For z ∈ X_{j*} ⊂ W, if z ∉ K then -z ∈ K ⊂ W, so z ∈ lin W = lin K ⊂ K, a contradiction. So K + cone X_{j*} = K, and j* is a cone point.
- **Row lemma.** Correct. The nerve on {+,-} is {+}, {-}, or {+}, {-}, {+,-}. The last case occurs whenever both vertices are present, by (G2). In each case it is a cone.
- **Inductive step.** Correct.
  - Row p, including the boundary row p = -1, is the product over σ of row-lemma complexes on K + cone X_σ, hence exact.
  - Column q >= 0 is the product over ρ of C^•(K_ρ). Here K_ρ ⊃ K inherits the cover hypothesis, and m(K_ρ) < m(K): z becomes decided, and decided elements stay decided.
  - Column q = -1 is C^•(K).
  - The region p, q >= -1 has finitely many (p,q) in each total degree. Filtering by p gives a finite filtration in each degree, whose graded pieces are the exact rows, so Tot D is acyclic.
  - The columns q >= 0 form a subcomplex, since d_q raises q. Filtering that subcomplex by q shows it is acyclic.
  - The quotient is column -1, up to sign. The long exact sequence then shows it is acyclic.

**§6. Correct.**
- Z = ∪_{j∈J'} X_j is finite because J' is finite.
- N(Q_Q) = N_τ(J').
- The universal coefficient argument is correct. For any complex C of free abelian groups, H^n(Hom(C,A)) -> Hom(H_n C, A) is surjective. Take A = H_n C and lift the identity to a class in H^n = 0.
- The ordered chain complex of N_τ is the directed union over finite J' ⊃ J_0, so it is exact.
- An exact complex of free abelian groups is split: Z_{n-1} = B_{n-1} ⊂ C_{n-1} is free, so C_n -> B_{n-1} splits. Hence Hom(-, A) is exact.
- That Hom complex is the product over all tuples in N_τ, which is exactly the Čech complex in step 3.
- So **(a): yes.** Part D proves precisely what Part A step 4 needs, for every covering in Cov (all members f.p., every valuation factoring through a member), every principal τ ⊃ Φ_Q, and every A.

## Part B (principality). Correct.
- The retract reduction is Lemma 1(i) of Part D with P in place of Q. The kernel equality under a retraction is correct.
- The description of the kernel of P -> Q' is correct.
  - (P^gp⊕Z^k)/L is the group of the quotient monoid. M_1/M_1^* is its int/sat/sharp reflection, and the quotient of a saturated monoid by its units is saturated.
  - x dies iff -nx ∈ M_0 iff ψ(c) = nx + p for some c ∈ K.
  - K is the set of lattice points of the rational cone {c : the Z^k-part of Σc_j l_j is <= 0}, hence finitely generated (Gordan). ψ is additive, so Y is a finitely generated monoid.
- Φ_Q is the face generated by the submonoid S = Y ∩ P: S ⊂ Φ_Q (take n = 1, p = 0), and conversely.
- The principality argument is correct.
  - F^gp ∩ P = F holds for any face, even without saturation.
  - n s_{i+1} ∈ G_i would give s_{i+1} ∈ F(s_i).
  - Equal ranks with G_i ⊂ G_{i+1} would force some n s_{i+1} into G_i. So ranks strictly increase, and chain lengths are bounded by rk Y^gp + 1.
  - In a directed poset without infinite ascending chains a maximal element exists, and it is the maximum.

## Part A and Part C (Steps 0, 3, 5, 6)

**A1 / C-Step 0. Correct; this answers (e).**
- B_P is equivalent to the poset of principal faces (F3).
- The colimit for u_p F at Q runs over the directed poset of principal faces contained in Φ_Q. That poset is nonempty, since it contains face(0), and P[-0]^sharp = P.
  - So u_p is exact, being a filtered colimit, and π^{-1} = sh ∘ u_p is exact.
  - On f.p. Q the poset has the maximum Φ_Q (Part B), so u_pF(Q) = F(Φ_Q).
- From Hom(sh u_p F, G) = Hom(u_p F, G) = Hom(F, G|_B) we get π_* = restriction. This holds for every P.
- The unit at b is the composite F(b) -> u_pF(b) -> (u_pF)^sh(b).
  - The first map is the coprojection at the terminal pair (b, id), hence an isomorphism.
  - The second map is an isomorphism once Step 5 is known.
- Nothing fine-specific is used. "Finite poset" is never used.

**A2 / C-Step 3 (the I_{τ,A}). Correct for arbitrary P.**
- I_{τ,A} is a functor: if b -> b', then Φ_b ⊂ Φ_b'.
- Hom(F, I_{τ,A}) = Hom(F(τ), A) uses only that τ is an object and the poset structure.
- F embeds into ∏_τ I_{τ,E(F(τ))}, since the component at τ = b is injective. Arbitrary products of injectives are injective, so injective resolutions by (possibly infinite) products exist.
- The convexity and "w_0" parts of C-Step 3 are fine-specific. They are not used, being replaced by Part D Lemma 2.

**A3. Correct.**
- On f.p. Q, Lan is evaluation at Φ_Q, so it commutes with arbitrary products.
- For a covering in Cov, every iterated pushout Q_σ is f.p. (F2), so Lan I(Q_σ) = I(Φ_σ), which is A iff Φ_σ ⊂ τ. The transition maps are identities or zero.
- Repeated indices are handled by Lemma 2.
- If Φ_Q ⊄ τ, then everything vanishes, since Φ_σ ⊃ Φ_Q.

**A4.** Supplied by Part D (see (a) above).

**A5 / C-Step 5. Correct once read with Cov from A7.** The step "sheafification does not change values on f.p. objects" deserves the following explicit argument.
- Let G = u_p F. G satisfies the sheaf condition on every 𝒰 ∈ Cov.
  - Take 0 -> F -> I^0 -> I^1 and evaluate at f.p. objects; this is exact.
  - Ȟ^0(𝒰, -) is left exact, and only f.p. objects occur in it.
  - Augmented Čech exactness in degrees -1 and 0 gives G'(U) ≅ Ȟ^0(𝒰, G') for G' = Lan I^k. Here the Čech complex is a product of exact complexes, and products of exact complexes of abelian groups are exact.
  - The four-term diagram then gives the isomorphism for G.
- For f.p. U, G^+(U) = colim over coverings of Ȟ^0(𝒰, G). One may restrict to the cofinal family Cov(U), on which every term is G(U) via the canonical maps. So G(U) ≅ G^+(U).
- Since G -> G^+ is an isomorphism on all f.p. objects, and Ȟ^0(𝒰, -) for 𝒰 ∈ Cov only sees f.p. objects, the same argument gives G^+(U) ≅ G^{++}(U).
- So π^{-1}F(U) = F(Φ_U) for f.p. U, and π_*π^{-1}F = F via the unit.

**A6 / C-Step 6. Correct.**
- Cartan's criterion (Stacks 03F7, Cohomology on Sites, quoted from memory) is applied within its hypotheses. Its hypotheses are:
  - every covering in Cov is a covering of an object of B, with all members and all iterated fibre products U_{i_0} ×_U … ×_U U_{i_p} in B;
  - for each U ∈ B, the coverings of U in Cov are cofinal, i.e. every covering of U is refined by one in Cov.
- Then, for an abelian sheaf G, Ȟ^p(𝒰, G) = 0 for all 𝒰 ∈ Cov and p > 0 implies H^p(U, G) = 0 for U ∈ B and p > 0.
- Here B = f.p. objects and Cov is as in A7. The fibre products are f.p. by (F2).
- G = π^{-1}I^k is a sheaf. It agrees with Lan I^k on B (A5 applied to I^k), so its Čech complexes on Cov are products of the exact complexes of A3/A4. Infinite products are harmless.
- π^{-1}F -> π^{-1}I^• is a resolution by Γ(U,-)-acyclic objects, so H^p(U, π^{-1}F) = H^p(I^•(Φ_U)), which is 0 for p > 0.
- π_* preserves injectives, being right adjoint to the exact π^{-1}. So R^pπ_*G = (b ↦ H^p(b, G)).
- Every b = P[-x]^sharp is f.p. (F3). Hence R^pπ_*π^{-1}F = 0 for p > 0, and R^0 = F via the unit.

**(c).** Steps 0, 3, 5 and 6 use no finiteness of the face poset and no fineness of f.p. objects. Finiteness of products is replaced correctly by arbitrary products. The fine-specific passages of C-Step 3 (convexity of C, w_0) and C-Step 5.4 ("all members f.p.") are not used, being replaced by Lemma 2 and A7.

**A7 / (d). Correct; one bullet needs the following supplement, which I now supply.**
- The witnesses form a birhizomic cover with all members f.p. As a subfamily, it refines the original cover, so Cov(U) is cofinal among coverings of each f.p. U.
- That is exactly the cofinality needed for the plus construction and for Cartan's criterion. For the plus construction, the colimit over the directed system of coverings (Ȟ^0 refinement maps are independent of choices) can be computed on a cofinal subsystem.
- The last bullet of A7 claims that, for a *generated* topology, the sieves containing a birhizomic cover are cofinal. This needs the birhizomic covers to form a pretopology. Then the sieves containing a cover already form a Grothendieck topology, and every covering sieve contains a birhizomic cover.
- The problem asserts that the birhizomic covers form a topology. To be safe, here is a proof of the pretopology axioms. In A_P^op the fibre products are pushouts in 𝒞; write a cover as {a_i : Q -> Q_i}.
  - *Isomorphisms.* For an isomorphism φ : Q -> Q', any valuation v of Q' satisfies v = (vφ^{-1})φ. Given Q -h-> M -p-> V with p infinitesimal, u = hφ^{-1} is the unique map with uφ = h, and p u = vφ^{-1}.
  - *Base change* along c : Q -> Q'. Let v' be a valuation of Q'. Then v'c factors as g_i a_i, with a_i birhizomic at g_i. Put Q'_i = Q' ⊔_Q Q_i and g' = (v', g_i). The map Q' -> Q'_i is f.p. (F2).
    - Given Q' -h-> M -p-> V with ph = v' and p infinitesimal, (hc, p) is a factorization of v'c = g_i a_i. So there is a unique u_i : Q_i -> M with p u_i = g_i and u_i a_i = hc.
    - Then u = (h, u_i) satisfies pu = g' and restricts to h on Q'.
    - Uniqueness: any such u restricts on Q_i to a map with the same properties as u_i, hence equal to u_i.
  - *Composition.* Let v be a valuation of Q. Then v = g_i a_i with a_i birhizomic at g_i, and g_i = g_ij b_ij with b_ij : Q_i -> Q_ij birhizomic at g_ij. The composite b_ij a_i is f.p. (F2).
    - Given (h, p) with ph = v, take the unique u_i with p u_i = g_i and u_i a_i = h.
    - Then take the unique u with pu = g_ij and u b_ij = u_i. It satisfies u b_ij a_i = h.
    - Uniqueness: if u' has these properties, then u' b_ij has the properties of u_i, so u' b_ij = u_i, and then u' = u.
- Hence the covering sieves of the topology are exactly the sieves containing a birhizomic cover, and Cov(U) is cofinal in either reading.

## Quoted standard results
All are quoted correctly and used within their hypotheses: Tychonoff, Zorn, Gordan's lemma, the universal coefficient theorem (any complex of free abelian groups), the first-quadrant double-complex lemma (finitely many (p,q) per total degree), and Cartan's criterion (Stacks 03F7, statement recalled from memory and given above).

Ordered chains computing simplicial homology is not actually needed. Part D proves exactness of the ordered (cochain) complexes directly, and these are literally the Čech complexes. The general framework is set-theoretic only: it uses sheafification on the large site A_P^op, which the problem takes as given.

## Summary of repairs (all written out above)
1. Part D Lemma 1(i): T(S,R) is the int/sat/sharp object, not the image in M.
2. Part D Theorem T, cone lemma: the well-definedness of h comes from the cone-point hypothesis, not from (G0).
3. A5: an explicit plus-construction argument for "values on f.p. objects are unchanged".
4. A7, last bullet: a proof that birhizomic covers satisfy the pretopology axioms, so the covering sieves are the sieves containing a birhizomic cover.

None of these changes any statement.

Only the following is used about the cover: every valuation factors through some member, and the witnessing members are f.p. Infinitesimality never enters, which is consistent with the claim.

**VERDICT: the chain proves the claim exactly as stated (YES for every monoid P and every F).** This holds with the four small gaps above, each repaired completely in this file.

=== END OF ANSWER round5_q2 ===
