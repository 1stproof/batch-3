# round4_q8: proof of statement #19

## Summary

**Statement #19 is proved, exactly as stated** (Theorem below). The proof does **not** go through the requested route of a structure theorem for birhizomic maps followed by refinement to standard covers. The reason for leaving that route is that **#19 does not use birhizomy at all**. The only input from the cover is the *factorization property*: every valuation v : Q -> V lifts to some Q_i. The genuine difficulties for non-finitely-generated Q were:
- the finite reduction (Lemma K);
- the nerve of a non-closed convex cover (the [0,1) ∪ [1,2] pathology).

Both are removed by one device. Take all witness valuations with values in a single **non-archimedean real closed field R\***, and parametrize convex combinations by the simplex Δ(R\*) over R\*, not by the real simplex. Over R\* the loci K_i become *closed* convex polyhedra defined by finitely many parameters. Then:
- finite reduction follows from the compactness theorem of first-order logic, applied to the cover property in elementary extensions of R\*;
- the nerve theorem transfers from R to R\* by Tarski's theorem.

Section 0 also explains why the naive real convex combination (the director's sketch (b)) really fails.

Facts cited from memory (standard): Zorn's lemma; Hölder's theorem (an archimedean ordered group embeds in R); the compactness theorem and the completeness of the theory RCF of real closed fields (Tarski); Farkas' lemma together with Minkowski–Weyl over R; Borsuk's nerve theorem for finite families of compact convex sets; and the description of finitely presentable objects of the coslice category Q/Mon as retracts of finite colimits of the free objects Q ⊕ N^k (the same fact #16 used).

## Conventions

- Mon is the category of integral, saturated, sharp commutative monoids.
- f : P -> Q is the structure map. The cover is {f_i : Q -> Q_i}_{i in I}. Each f_i is f.p., and for every valuative V and every v : Q -> V there are i and g : Q_i -> V with g f_i = v. Only this property is used.
- Q_σ is the colimit in Mon of the f_i, i ∈ σ, under Q, and Φ_σ = ker(P -> Q_σ). N_τ = {σ : Φ_σ ⊂ τ}. This is a simplicial complex: σ' ⊂ σ gives Q_σ' -> Q_σ under P, hence Φ_σ' ⊂ Φ_σ.
- τ may be any face of P with Φ_Q ⊂ τ. Principality of τ is not used.

## 0. Why the naive convexification fails (dead end, proved)

Take Q = N^2 and H = R^2 with the lexicographic order. Let w(e1) = (0,1) and w(e2) = (0,2); this is a rank-one injective valuation. Let a = e2 - e1, so w(a) = (0,1) > 0, and put Q' = ⟨e1, e2 - e1⟩.

By Proposition B, Q -> Q' is birhizomic at the lift of w. Now let w'(e1) = (1,0) and w'(e2) = 0. Then ((1-δ)w + δw')(a) = (-δ, 1-δ) < 0 for every real δ > 0.

So the locus {λ : w_λ lifts} need not contain any real neighbourhood of the point w, even at a birhizomic point. The reason is that w' lives in a larger archimedean class. With real parameters, the loci are "lexicographic half-spaces", which are neither open nor closed, and the [0,1) ∪ [1,2] pathology cannot be excluded this way. Over R\* the corresponding locus is the closed set {λ_2 ≤ r λ_1}, where r ∈ R\* is infinitesimal. Points with infinitesimal λ_2/λ_1 are invisible to real parameters but are R\*-points, and the cover property covers them too. This is what the proof below exploits.

## 1. Lemmas

**Lemma 1 (order extension; proved).** Every M in Mon admits a homomorphism ι : M -> V with V valuative and ι^{-1}(0) = {0}.

*Proof.*
1. M^gp is torsion-free. If nx = 0, then nx ∈ M, so x ∈ M by saturation; likewise -x ∈ M, so x = 0 by sharpness.
2. Call C ⊂ M^gp an *isolated cone* if C + C ⊂ C, C ∩ -C = {0}, and nx ∈ C with n ≥ 1 implies x ∈ C. Then M is an isolated cone.
3. Isolated cones containing M, ordered by inclusion, have unions of chains as upper bounds. By Zorn's lemma there is a maximal one, C.
4. Suppose C were not total: pick x with x ∉ C ∪ -C. Put C' = {y : ny ∈ C + Nx for some n ≥ 1}. Then C' ⊇ C ∪ {x}, C' is closed under +, and C' is isolated.
5. Check C' ∩ -C' = 0. Suppose ny = c + ax and m(-y) = c' + bx. Then 0 = mc + nc' + (ma+nb)x.
   - If ma + nb > 0, then -(ma+nb)x ∈ C, so -x ∈ C, a contradiction.
   - Otherwise a = b = 0. Then nm·y ∈ C ∩ -C = 0, so y = 0 by step 1.
6. So C' is an isolated cone strictly larger than C, contradicting maximality. Hence C is total.
7. Now V := C is a valuative monoid with V^gp = M^gp, and the inclusion M ⊂ C has trivial kernel. ∎

**Lemma 2 (valuation form; proved).**
- (a) If a valuation v : Q -> V lifts along every f_i, i ∈ σ, then Φ_σ ⊂ ker(v∘f).
- (b) If σ ∈ N_τ, there is a valuation v_σ of Q that lifts along every f_i, i ∈ σ, and has ker(v_σ∘f) = Φ_σ ⊂ τ.

*Proof.*
- (a) The lifts are compatible under Q and V is in Mon, so they induce a map Q_σ -> V.
- (b) Take v_σ = ι∘(Q -> Q_σ), with ι from Lemma 1 applied to Q_σ. ∎

Nonemptiness of N_τ: let v = ι_Q. Then ker(v∘f) = Φ_Q ⊂ τ. Some f_i admits a lift of v, and by 2(a), {i} ∈ N_τ.

**Lemma 3 (one real closed field; proved modulo Hölder and compactness).** For finitely many ordered abelian groups G_1, ..., G_n, there are a real closed field R\* and order-preserving injective homomorphisms G_s -> (R\*, +).

*Proof.*
1. Give G = ⊕ G_s the lexicographic order. Each G_s is then an ordered subgroup, so it suffices to embed G.
2. By the compactness theorem, consider the theory RCF together with constants c_g for g ∈ G and the axioms c_g + c_h = c_{g+h} and c_g < c_h for g < h. A model gives the required embedding, so it suffices to embed each finitely generated subgroup G_0.
3. W = G_0 ⊗ Q is an ordered Q-vector space of finite dimension. Its convex subgroups are subspaces, and they form a chain 0 = W_0 ⊊ ... ⊊ W_k = W. Each quotient W_j/W_{j-1} is archimedean, so it embeds into R by some φ_j (Hölder).
4. Choose a Q-linear splitting W = U_1 ⊕ ... ⊕ U_k with W_j = U_1 ⊕ ... ⊕ U_j. Write x = Σ x_j and send x to Σ_j φ_j(x_j) T^j. This lands in the real closure of R(T), ordered with T > R.
5. The map is order-preserving and injective. If x > 0 and j is the largest index with x_j ≠ 0, then the class of x in W_j/W_{j-1} is positive, so φ_j(x_j) > 0, and this term dominates. ∎

**Lemma 4 (uniform polyhedrality of lifting loci; proved modulo the cited facts).** Let v_1, ..., v_n : Q -> R\*_{≥0} be homomorphisms, and fix i ∈ I. There are finitely many h_{m s} ∈ R\* (m = 1..M) with the following property. For every real closed field F ⊇ R\* and every λ ∈ Δ(F) = {λ ∈ F^n : λ_s ≥ 0, Σλ_s = 1}, the map w_λ := Σ_s λ_s v_s : Q -> F_{≥0} lifts along f_i iff θ_i(λ) holds, where θ_i(λ) is the conjunction over m of Σ_s λ_s h_{ms} ≥ 0.

*Proof.*
1. Since f_i is f.p., Q_i is a retract under Q of some Q'' = (Q ⊕ N^k / {r_j = s_j}_{j=1..J})^{int,sat,♯} (cited fact). A lift to Q_i exists iff a lift to Q'' exists: compose with the retraction, respectively with the projection.
2. F_{≥0} lies in Mon. So, writing r_j = (q_j, a_j) and s_j = (q'_j, a'_j), a lift to Q'' amounts to a vector y ∈ F^k with y ≥ 0 and Ay = b(λ). Here A is the integer matrix with rows a_j - a'_j, and b(λ)_j = w_λ(q'_j) - w_λ(q_j) = Σ_s λ_s b^{(s)}_j with b^{(s)} ∈ R\*^J.
3. By Farkas and Minkowski–Weyl over R, there are rational u_1, ..., u_M such that, for all b, {y ≥ 0, Ay = b} is feasible iff u_m·b ≥ 0 for all m. This is a first-order sentence with rational parameters, so it holds in every real closed F (Tarski).
4. Put h_{ms} = u_m·b^{(s)}. ∎

So K_i(F) := {λ ∈ Δ(F) : θ_i(λ)} is a closed convex polyhedron in Δ(F), defined over R\*, uniformly in F.

## 2. Theorem (#19) and proof

**Theorem.** N_τ is nonempty and has vanishing reduced integral homology. Consequently its augmented ordered cochain complex with coefficients in any abelian group A is exact. Only the factorization property of the cover and the finite presentation of the f_i are used.

*Proof.*
1. **Setup.** Nonemptiness was shown above. Let L ⊂ N_τ be a finite nonempty subcomplex with simplices σ_1, ..., σ_n, and let v_s := v_{σ_s} be the witnesses from Lemma 2(b). By Lemma 3, all v_s may be taken with values in R\*_{≥0} for a single real closed field R\*.
2. **Every w_λ lies in C_τ.** For λ ∈ Δ(F) with F ⊇ R\* real closed, w_λ is a homomorphism Q -> F_{≥0}, and F_{≥0} is a valuative monoid. A sum of nonnegative elements of F vanishes only if each term does, so ker(w_λ∘f) = ∩_{λ_s>0} ker(v_s∘f) ⊂ τ.
3. **Finite reduction.** Let F be any elementary extension of R\* and λ ∈ Δ(F). The cover property gives some i ∈ I with λ ∈ K_i(F). Hence the set of formulas {λ ∈ Δ} ∪ {¬θ_i(λ) : i ∈ I}, together with the elementary diagram of R\*, has no model. By compactness, a finite J_0 ⊂ I already gives an inconsistent set, so R\* satisfies ∀λ ∈ Δ ∨_{i∈J_0} θ_i(λ).
4. **The finite family.** Let J = vert(L) ∪ J_0, which is finite. Then {K_i(R\*)}_{i∈J} is a finite family of closed convex polyhedra covering Δ(R\*). Let N_Δ = {σ ⊂ J : ∩_{i∈σ} K_i(R\*) ≠ ∅}.
5. **N_Δ is acyclic (transfer).** Fix n, |J| and the numbers of inequalities. Consider the first-order sentence: for all parameters h, if the polyhedra K_i(h) cover Δ, then their nerve is one of the finitely many acyclic simplicial complexes on J. Over R this holds by Borsuk's nerve theorem: the K_i(R) are compact and convex, and their union Δ(R) is contractible. By completeness of RCF it holds over R\*. So N_Δ has vanishing reduced homology.
6. **N_Δ ⊂ N_τ.** A point λ ∈ ∩_{i∈σ} K_i(R\*) gives a valuation w_λ ∈ C_τ lifting along every f_i, i ∈ σ. Lemma 2(a) then gives Φ_σ ⊂ ker(w_λ∘f) ⊂ τ.
7. **L ⊂ N_Δ.** The vertex e_s of Δ satisfies w_{e_s} = v_s, which lifts along every f_i with i ∈ σ_s. So e_s ∈ K_i(R\*) for every i ∈ σ_s, and σ_s ∈ N_Δ.
8. **Conclusion.** Every finite subcomplex of N_τ lies in a finite subcomplex with vanishing reduced homology. Since homology commutes with the directed union of finite subcomplexes, H̃_*(N_τ) = 0. The augmented ordered chain complex of N_τ has the same homology, and it is a complex of free abelian groups, so it is split exact. Applying Hom(-, A) therefore gives an exact complex. Since Φ_σ depends only on the underlying set of σ, repeated indices are harmless. ∎

## 3. Consequences, status, open points

- **Proved here:** #19 exactly as stated, for an arbitrary monoid Q and arbitrary f.p. covers. The proof is complete modulo the classical facts listed in the summary.
- **The chain.** Together with the chain in the query file (Steps 1–6, which use #16), this yields YES to the headline question for every monoid P. I did not re-verify that chain beyond checking that it uses #19 only in the form proved here: augmented Čech complexes of I_{τ,A}∘b on covers of f.p. objects are exact. #16 itself relies on the cited description of f.p. objects as retracts of finite presentations, which is also used in Lemma 4 above.
- **By-product, proved.** The finite reduction (the director's (a), Lemma K for arbitrary Q) holds in the form of step 3. Moreover, the fine-case Steps 2 and 4 of #15 are special cases of this argument.
- **Not attempted, since unnecessary:** the structure theorem for birhizomic maps, and the refinement-invariance programme ((1)–(3) of the task). The named route is not needed, because birhizomy plays no role in #19.

=== END OF ANSWER round4_q8 ===
