# Answer to round4_q2: the nerve statement (#19) for arbitrary P

**Plan.** I prove #19 as stated, for every monoid P. The proof does not use the director's ordered-R-vector-space convexification. It has three ingredients:
1. **Patch compactness.** It gives a finite subfamily J_0 ⊂ I such that every valuation of Q factors through some Q_i with i in J_0.
2. **Convexification over a real closed field K.** Valuations are taken with values in (K,+) and mixed with coefficients λ in K. This makes every member locus a *closed* K-polytope in the K-simplex, so the half-open phenomenon [0,1) ∪ [1,2] cannot occur.
3. **Tarski transfer** of the classical nerve theorem for finite closed convex covers from R to K.

The proof uses only the *weak* cover property: every valuation factors through some member. Birhizomicity is never used beyond this. I also re-checked the chain #15/#16/#19 → YES and found no flaw; a few remarks are in Section 4.

Conventions are as in the task. G := Q^gp ⊗ Q. "DOAG" means divisible ordered abelian group, possibly trivial. "RCF" means real closed field.

## 0. Facts quoted from memory (not proved here)

- (F1) **Compact objects are retracts of finite presentations.** A map Q → Q' that is f.p. in the category of integral, saturated, sharp monoids is, as an object under Q, a retract of Q'' = (Q ⊕ N^k / R)^{int,sat,♯}, where R is a finite set of relations. #16 cites the same fact.
- (F2) **Order extension (Levi / Fuchs).** A partial order on a torsion-free abelian group whose positive cone M satisfies "nx ∈ M, n ≥ 1 ⇒ x ∈ M" extends to a total order.
- (F3) **Fourier–Motzkin / Farkas.** Let A be an integer matrix. There are finitely many rational vectors c_1, …, c_t with the following property. For every DOAG D and every b ∈ D^r, the system Az = b, z ≥ 0 has a solution z ∈ D^k iff ⟨c_s, b⟩ ≥ 0 for all s.
  - Proof sketch: the equivalence holds over Q by Minkowski–Weyl. It is a first-order sentence in the language of ordered groups (clear denominators). The theory of nontrivial DOAGs is complete (Robinson). The trivial group D = 0 is immediate.
  - Alternatively: the steps of Fourier–Motzkin elimination are valid verbatim in any DOAG.
- (F4) **Embedding into a real closed field.** Every finitely generated ordered abelian group embeds, as an ordered group, into R^d with the lexicographic order (Hahn, finite rank). The ordered group R^d_lex embeds into the additive group of the real closure of R(t), where 0 < t < every positive real, via (a_1, …, a_d) ↦ Σ a_k t^{k−1}.
  - By the compactness theorem applied to RCF ∪ (the diagrams of finitely many ordered abelian groups V_1, …, V_N), there is one real closed field K containing ordered copies of all the V_j^gp.
- (F5) **Nerve theorem (Borsuk 1948 / Leray).** Let finitely many closed convex sets in R^n cover the standard simplex. Then their nerve is homotopy equivalent to the simplex, so it has vanishing reduced homology.
- (F6) **Tarski.** The theory RCF is complete.

## 1. Valuation description of N_tau (re-check of the director's note)

For σ ⊂ I finite and nonempty, Q_σ is the pushout of the Q_i (i ∈ σ) over Q, and Φ_σ = ker(P → Q_σ).

**Lemma 1.** Φ_σ ⊂ τ iff there is a valuation w : Q → V (V valuative) such that:
- w factors through Q_i → V for every i in σ, and
- w(x) ≠ 0 for every x ∈ P \ τ.

*Proof.*
- (⇐) Compatible lifts Q_i → V define a map Q_σ → V, because V is an object of the category. Hence Φ_σ ⊂ ker(w|_P) ⊂ τ.
- (⇒) Q_σ is integral, saturated and sharp. By (F2), its order extends to a total order. This gives a valuative V_σ and u_σ : Q_σ → V_σ with u_σ(q) = 0 ⇒ q = 0. Then w := u_σ ∘ (Q → Q_σ) factors through every Q_i, and ker(w|_P) = Φ_σ ⊂ τ. ∎

Such a w with u_σ injective is called a **witness** for σ. Its kernel on P is exactly Φ_σ.

Repeated indices are harmless: w factors through Q_i ⊕_Q Q_i iff it factors through Q_i.

**Nonemptiness of N_tau.** Take an injective valuation of Q from (F2). Its kernel on P is Φ_Q ⊂ τ. It factors through some Q_i by the cover property, so {i} ∈ N_tau.

## 2. Step A: a finite weak subcover (patch compactness)

Let X be the set of subsets C ⊂ G with:
- C + C ⊂ C;
- C ∪ (−C) = G;
- qC ⊂ C for all rational q > 0;
- the image of Q lies in C.

These conditions each involve finitely many elements, so X is closed in {0,1}^G and hence compact (Tychonoff).

**From points of X to valuations.** For C ∈ X:
- C ∩ (−C) is a Q-subspace.
- V_C^gp := G/(C ∩ −C) is a totally ordered Q-vector space with positive cone the image of C. In particular it is a DOAG.
- Its positive part V_C is valuative: integral, sharp, total, and saturated because qC ⊂ C.
- w_C : Q → V_C, q ↦ [q], is a valuation.

**From valuations to points of X.** Conversely, a valuation w : Q → V extends uniquely to G → V^gp ⊗ Q, and C_w := {x : w(x) ≥ 0} lies in X.

**The loci E_i.** Fix i ∈ I. By (F1), choose Q_i'' = (Q ⊕ N^k / R)^{int,sat,♯} together with maps s : Q_i → Q_i'' and r : Q_i'' → Q_i under Q, with rs = id.
- Let V be valuative. A lift of w : Q → V through Q_i gives the lift g ∘ r through Q_i''. A lift g'' through Q_i'' gives the lift g'' ∘ s through Q_i. So lifts through Q_i exist iff lifts through Q_i'' exist.
- A lift through Q_i'' is a tuple z ∈ V^k satisfying the finitely many relations of R. Each relation has the form Σ_j (m_rj − m'_rj) z_j = w(a'_r − a_r) with a_r, a'_r ∈ Q.
  - Integralization, saturation and sharpening impose no further condition, since V is integral, saturated, sharp, and V^gp is torsion-free.
- Now take V^gp to be a DOAG. By (F3), a lift exists iff w(y_s^{(i)}) ≥ 0 for finitely many elements y_1^{(i)}, …, y_t^{(i)} of G. These elements are rational combinations of the a'_r − a_r and do not depend on w or V.
- Hence, for every DOAG-valued valuation w of Q:

  (*) w factors through Q_i ⟺ w(y_s^{(i)}) ≥ 0 for all s.

Put E_i = {C ∈ X : y_s^{(i)} ∈ C for all s}. This is clopen in X.

**The E_i cover X.** Let C ∈ X. By the cover property applied to w_C : Q → V_C, w_C factors through some Q_i → V_C. By (*), C ∈ E_i.

**Conclusion of Step A.** By compactness there is a finite J_0 ⊂ I with X = ∪_{i∈J_0} E_i. Consequently, by (*), every valuation of Q with values in a DOAG factors through Q_i for some i ∈ J_0.

## 3. Step B: finite full subcomplexes are acyclic

Let L be a finite subcomplex of N_tau. Put J' = vert(L) ∪ J_0, a finite set, and let N' = N_tau(J') be the full subcomplex on J', i.e. the σ ⊂ J' with Φ_σ ⊂ τ. Then L ⊂ N' ⊂ N_tau.

**Claim.** N' has vanishing reduced integral homology.

*Proof.*

**Setup.**
- Let Σ_1, …, Σ_N be the simplices of N'. There are finitely many, and N ≥ 1 because L, or the vertex from Section 1, is nonempty.
- For each Σ_m choose a witness v_m : Q → V_m (Lemma 1). Its kernel on P is Φ_{Σ_m} ⊂ τ, and it factors through Q_i for every i ∈ Σ_m.
- By (F4), choose one real closed field K and ordered-group embeddings ι_m : V_m^gp → (K,+). Put v'_m = ι_m ∘ v_m : Q → K_{≥0}.
- Let Δ = {λ ∈ K^N : λ_m ≥ 0, Σ λ_m = 1} and w_λ = Σ_m λ_m v'_m.

**(a) Each w_λ is a valuation of Q in C_tau.**
- w_λ is a monoid homomorphism Q → K_{≥0}, and K_{≥0} is valuative.
- In an ordered field a sum of nonnegative terms vanishes only if every term does. Hence ker(w_λ|_P) is the intersection of the ker(v_m|_P) over the m with λ_m > 0.
- At least one λ_m is positive, and each of these kernels lies in τ. So ker(w_λ|_P) ⊂ τ.

**(b) The sets K_i are polytopes.** For i ∈ J', put K_i = {λ ∈ Δ : w_λ factors through Q_i into K_{≥0}}.
- K is a DOAG, so (*) applies: K_i = {λ ∈ Δ : Σ_m λ_m v'_m(y_s^{(i)}) ≥ 0 for all s}. Here v'_m is extended to G, which is possible because K is divisible.
- So each K_i is defined by finitely many K-linear non-strict inequalities with coefficients in K. It is a closed convex K-polytope.

**(c) The K_i with i ∈ J_0 cover Δ.** By (a), each w_λ is a K-valued valuation of Q. By Step A it factors through some Q_i with i ∈ J_0.

**(d) The nerve of {K_i}_{i∈J'} equals N'.**
- (⊂) If λ lies in K_i for every i ∈ σ ⊂ J', then w_λ factors through every Q_i with i ∈ σ, and by (a) w_λ is nonzero on P \ τ. By Lemma 1, Φ_σ ⊂ τ.
- (⊃) If σ = Σ_m ∈ N', the vertex e_m of Δ gives w_{e_m} = v'_m. This factors through every Q_i with i ∈ σ, so e_m lies in every such K_i.
- In particular K_i ≠ ∅ exactly when {i} ∈ N'.

**(e) Transfer of the nerve theorem.**
- Fix N, the number M = |J'| of sets, a common number p of inequalities per set (pad with 0 ≥ 0), and a simplicial complex 𝒩 on a subset of [M] with nonzero reduced homology.
- Consider the following first-order sentence in the language of ordered fields, quantified over all coefficient tuples a ∈ K^{M·p·N}. Write K_i(a) for the polytope in Δ defined by the inequalities ⟨a_{i,s}, λ⟩ ≥ 0. The sentence says:

  "if ∪_i K_i(a) = Δ, then it is not the case that, for every nonempty σ ⊂ [M], ∩_{i∈σ} K_i(a) ≠ ∅ ⟺ σ ∈ 𝒩."

- Over R this is true by (F5): the K_i(a) are closed and convex, so a cover of the simplex has acyclic nerve.
- By (F6) the sentence is true over K.
- By (b), (c) and (d), our configuration over K covers Δ and has nerve N'. Hence N' cannot be a complex with nonzero reduced homology.
- There are finitely many candidate complexes 𝒩, so H̃_*(N'; Z) = 0. ∎

**Conclusion (proof of #19).**
- N_tau is nonempty (Section 1).
- Every finite subcomplex L of N_tau lies in a subcomplex N' ⊂ N_tau with H̃_*(N') = 0. So every reduced cycle of N_tau bounds, and H̃_*(N_tau; Z) = 0.
- The augmented simplicial chain complex is therefore a free acyclic complex, hence split exact. So its dual with coefficients in any abelian group A is exact.
- The ordered cochain complex is chain-homotopy equivalent to the alternating one (standard). So the augmented ordered cochain complex of N_tau with coefficients A is exact. ∎

**Remarks.**
- The proof uses only that every valuation of Q (with values in a DOAG) factors through some member. Birhizomicity, the R4 / Lemma A conditions, and any "openness lemma" are not needed for #19.
- Two problems the director anticipated are handled as follows:
  - Non-closed convex loci only arise when λ is real and the values are non-archimedean. Taking λ in K makes every locus a closed K-polytope.
  - Infinite covers are reduced to finite ones by patch compactness, which replaces Lemma K.
- The argument also re-proves Step 4 of #15 for fine P without Lemma K.

## 4. Re-check of the chain #15/#16/#19 ⇒ YES

I went through steps 1–6 of the chain and found no error. Comments:

- **Step 1.**
  - π_* = restriction to B_P, since Hom(π^{-1}F, G) = Hom(Lan F, G) = Hom(F, G|_B).
  - Lan is exact, being a filtered colimit, and on f.p. Q it equals F(Φ_Q) by #16.
- **Step 2.** A map F → I_{τ,A} is determined by its component at τ; τ is principal, so it is an object of B_P. F embeds into ∏_τ I_{τ,E(F(τ))}, because the factor τ = b is injective at b. Products of injectives are injective.
- **Step 3.** This is correct. For a repeated index, Φ is unchanged (Section 1).
- **Step 5.** If a presheaf satisfies the sheaf condition for all covering families of objects of B (f.p. objects), and these families and their fibre products lie in B, then the plus construction leaves its values on B unchanged.
  - Sieves generated by covering families are cofinal among covering sieves, given that birhizomic covers form a pretopology, as the problem asserts.
  - Applying this twice gives sheafification = identity on B.
- **Step 6.** This uses Cartan's criterion (Stacks, Lemma "Cartan's criterion", tag 03F7, from memory):
  - Hypotheses: every covering in Cov is of an object of B, with all members and all multiple fibre products in B; the Cov-coverings of each U ∈ B are cofinal; and Ȟ^p(𝒰, G) = 0 for 𝒰 ∈ Cov and p > 0.
  - Conclusion: H^p(U, G) = 0 for U ∈ B and p > 0.
  - Here Čech vanishing for π^{-1}I^k holds because the Čech complex of a product is the product of the Čech complexes.
  - Then R^p π_* π^{-1}F (b) = H^p(b, π^{-1}F) = H^p(I^•(Φ_b)), which is 0 for p > 0 and F(b) for p = 0. Each b = P[−x]^♯ is f.p.

**Answer to the headline question: YES.** For every monoid P and every presheaf F of abelian groups on B_P^op, F → Rπ_*π^{-1}F is a quasi-isomorphism. This is conditional only on the facts quoted from memory: (F1)–(F6) above, together with #16, Cartan's criterion, and the standard facts used in the chain.

## 5. Status

- **Proved:** #19 exactly as stated, for every P, every f.p. Q, every birhizomic cover, and every principal τ ⊇ Φ_Q. With the chain, this gives YES for all P.
- **Cited from memory, not reproved:** (F1)–(F6) and Cartan's criterion. (F1) is also used in #16.
- **Open:** nothing within the scope of the task, beyond the cited facts.

=== END OF ANSWER round4_q2 ===
