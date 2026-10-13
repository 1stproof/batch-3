# round4_q5: proof of statement #19

## Status and plan

I prove #19 exactly as stated, and in fact in a stronger form. Three hypotheses turn out to be unnecessary: that the members are birhizomic (only the covering property "every valuation of Q factors through some Q_i" is used), that tau is principal, and that Q is f.p. over P.

I depart from the named approach ("birhizomic openness + lexicographic nerve theorem"). The reason: the members' valuation loci turn out to be *closed* in a patch (constructible) topology on the space of valuations, because Fourier–Motzkin elimination produces only non-strict conditions. A compactness argument then reduces everything to finitely many elements of a finite-dimensional Q-vector space. Approximating C_tau there by constructible convex sets lets one replace the non-archimedean witnesses by *real* linear functionals. The members' loci then become closed polyhedral cones, and the closed-convex nerve theorem (Borsuk) applies just as in the fine case #15. The non-closedness that worried the director (the [0,1) ∪ [1,2] phenomenon) appears only when the witnesses are allowed to be non-archimedean, and the reduction avoids that.

As a by-product of exploring the named approach, Appendix A characterizes birhizomy completely (Theorem C) and proves an openness lemma. The main proof does not need either.

## Theorem (#19, strengthened)

**Setting.**
- P is a monoid (integral, saturated, sharp), f : P -> Q is any map of such monoids, and tau is any face of P with Phi_Q = f^{-1}(0) ⊂ tau.
- {Q -> Q_i}_{i in I} is a family of maps that are f.p. under Q. Here "f.p." means compact in the category of integral saturated sharp monoids under Q, i.e. Hom_Q(Q_i, -) commutes with filtered colimits.
- **Covering property:** every valuation v : Q -> V (V valuative) factors through some Q -> Q_i.

**Notation.** For a finite nonempty σ ⊂ I, let Q_σ be the pushout of the Q_i (i in σ) over Q in that category, let Phi_σ = ker(P -> Q_σ), and let N_tau = {σ : Phi_σ ⊂ tau}.

**Claim.** N_tau is a nonempty simplicial complex with vanishing reduced integral homology. Hence its augmented ordered cochain complex with coefficients in any abelian group A is exact.

(N_tau is closed under passing to subsets, because Q_{σ'} -> Q_σ for σ' ⊂ σ gives Phi_{σ'} ⊂ Phi_σ.)

## 0. Conventions

**The vector space G.** Put G = Q^gp ⊗ Q.
- Q^gp is torsion-free, since Q is saturated and sharp: nx = 0 gives nx ∈ Q, so x ∈ Q, and likewise -x ∈ Q, so x = 0.
- Hence Q ⊂ Q^gp ⊂ G, and f(P) ⊂ Q ⊂ G.
- Let Γ ⊂ G be the Q_{≥0}-cone spanned by Q. Every element of Γ has a positive integer multiple in Q.

**Cones.** A *cone* in a Q-vector space is a subset containing 0 and closed under addition and under multiplication by Q_{>0}. A *valuation cone* is a cone C with C ∪ -C equal to the whole space. Write X(G) for the set of valuation cones of G. For C in X(G) write C^{>0} = C \ (-C).

**From valuations to cones.** A valuation v : Q -> V gives a cone in X(G):
- V^gp is a totally ordered torsion-free group, so V^gp ⊗ Q is totally ordered, and v extends to v_Q : G -> V^gp ⊗ Q.
- Put C_v := {g : v_Q(g) >= 0}. Then C_v ∈ X(G) and Q ⊂ C_v.

**From cones to valuations.** Conversely, let C ∈ X(G) with Q ⊂ C.
- G/(C ∩ -C) is a Q-vector space, totally ordered with positive cone the image of C.
- Its nonnegative part V_C is a valuative monoid with divisible group, and v_C : Q -> V_C is a valuation with C_{v_C} = C.

**The valuation space.** Put X_Q := {C ∈ X(G) : Q ⊂ C} and
  C_tau := {C ∈ X_Q : -f(x) ∉ C for all x ∈ P \ tau},
the cones in which every f(x) with x ∈ P \ tau is strictly positive.

**Patch topology.** View X(G) as a subset of {0,1}^G with the product topology.
- Each defining condition involves finitely many coordinates: 0 ∈ C; g, h ∈ C ⇒ g + h ∈ C; g ∈ C ⇒ rg ∈ C; g ∈ C or -g ∈ C. So X(G) is closed, hence compact Hausdorff by Tychonoff.
- For g in G, the set {C : g ∈ C} is clopen.
- So X_Q and C_tau are closed, hence compact.

## 1. The locus of a member is cut out by finitely many non-strict conditions

**Lemma 1.1 (f.p. objects are retracts of finitely presented ones; standard, proof sketched).** Let Q -> Q' be f.p. Then there are a finite set T, a finite set R of relations (pairs of elements of Q ⊕ N^T), and maps of monoids under Q
  Q' --s--> Q'' := (Q ⊕ N^T / R)^{iss} --r--> Q'
with r s = id. Here (-)^{iss} is the reflection into integral saturated sharp monoids.

*Proof.* Index by pairs λ = (T, R) with T ⊂ Q' finite and R a finite set of relations among elements of Q ⊕ N^T that hold in Q'; these pairs are ordered by inclusion and form a directed set. Let Q''_λ = (Q ⊕ N^T / R)^{iss}. It maps to Q' because Q' is iss. Claim: Q' = colim_λ Q''_λ.
- By Result #17 §1.1 (re-checked: each axiom is witnessed by finitely many elements), filtered colimits in iss monoids are computed in monoids.
- The comparison map is surjective, since every element of Q' is some e_t.
- It is injective. Suppose x, y ∈ Q''_λ have the same image in Q'. Represent them by z, z' ∈ Q^gp ⊕ Z^T. Then z - z' = (q1 - q2, a+ - a-) with (q1, a+) and (q2, a-) having equal images in Q'^gp, hence in Q', since Q' is integral. Adding the relation (q1, a+) ~ (q2, a-) to R gives λ' >= λ in which x = y.
Since Q' is f.p., id_{Q'} factors through some Q''_λ. ∎

**Lemma 1.2 (Fourier–Motzkin).** For each i in I there are finitely many elements c_{i,1}, ..., c_{i,M_i} of G with the following two properties.
- (A) If a valuation v : Q -> V lifts to Q_i (i.e. v factors through Q -> Q_i), then v_Q(c_{i,m}) >= 0 for all m.
- (B) If V^gp is divisible and v_Q(c_{i,m}) >= 0 for all m, then v lifts to Q_i.

*Proof.*
1. By 1.1, Q_i is a retract under Q of Q'' = (Q ⊕ N^T/R)^{iss}. Then v lifts to Q_i iff v lifts to Q''. Compose a lift on Q'' with s, or a lift on Q_i with r.
2. Lifts of v to Q'' are tuples y ∈ (V^gp)^T with y >= 0 satisfying, for each relation (q_j, n_j) ~ (q'_j, n'_j) in R,
   v(q_j) + n_j·y = v(q'_j) + n'_j·y.
   Indeed, such a tuple gives Q ⊕ N^T -> V compatible with R, and this factors through the iss reflection because V is iss.
3. Put b_j = q_j - q'_j ∈ Q^gp and M = (n'_j - n_j)_j, an integer matrix. The system reads y >= 0, M y = v_Q(b).
4. Fourier–Motzkin elimination of y_1, ..., y_T works verbatim over any totally ordered Q-vector space W, with rational coefficients. To eliminate y_k one compares every lower bound with every upper bound; if each lower bound is at most each upper bound, one takes y_k = the largest lower bound (or the smallest upper bound, or 0). The resulting finite list of conditions depends only on M, not on W or on the right-hand side. Each condition has the form Σ_j u_j d_j >= 0 with u ∈ Q^J, where d = v_Q(b).
5. So, for W = V^gp ⊗ Q, a solution y ∈ W^T exists iff v_Q(c_{i,m}) >= 0 for c_{i,m} := Σ_j u_{m,j} b_j ∈ G, m = 1..M_i.
6. (A): a lift in V is in particular a solution in V^gp ⊗ Q.
7. (B): if V^gp is divisible then V^gp = V^gp ⊗ Q, so the solution lies in V^gp with y >= 0, i.e. y ∈ V^T. ∎

**Definition.** Put E_i := {C ∈ X(G) : c_{i,m} ∈ C for all m}, a clopen subset of X(G). For σ ⊂ I put E_σ := ∩_{i in σ} E_i.

**Lemma 1.3.** For a finite nonempty σ ⊂ I: Phi_σ ⊂ tau ⇔ E_σ ∩ C_tau ≠ ∅.

*Proof.*
(⇒) Q_σ is integral, saturated and sharp, so it has an injective valuation w : Q_σ -> V, i.e. w(z) > 0 for z ≠ 0. This is Lemma 2.1 below applied to Q_σ with G_0 = 0, as in Step 5. Let v = w∘(Q -> Q_σ). Then:
- v lifts to every Q_i, i in σ, so C_v ∈ E_σ by 1.2(A).
- For x ∈ P \ tau we have x ∉ Phi_σ, so v(f(x)) > 0. Hence C_v ∈ C_tau.

(⇐) Let C ∈ E_σ ∩ C_tau.
- v_C has a divisible group, so by 1.2(B) it lifts to each Q_i, i ∈ σ, by maps under Q.
- These lifts induce a map Q_σ -> V_C, by the universal property of the pushout (V_C is iss).
- So every x ∈ Phi_σ has v_C(f(x)) = 0, i.e. -f(x) ∈ C. Since C ∈ C_tau, this forces x ∈ tau. ∎

**Lemma 1.4.** C_tau ⊂ ∪_{i in I} E_i, and there is a finite J_0 ⊂ I with C_tau ⊂ ∪_{i in J_0} E_i.

*Proof.* For C ∈ C_tau, the valuation v_C factors through some Q_i by the covering property, so C ∈ E_i by 1.2(A). The set C_tau is compact and the E_i are open. ∎

## 2. Extension lemma

**Lemma 2.1.** Let H be a Q-vector space and G_0 ⊂ H a subspace. Let Γ ⊂ H be a cone. Let S ⊂ H be a subset with S + S ⊂ S, Q_{>0}S ⊂ S and S + Γ ⊂ S. Let D be a valuation cone of G_0. Then the following are equivalent:
- there is C ∈ X(H) with Γ ⊂ C, S ∩ (-C) = ∅ and C ∩ G_0 = D;
- (i) Γ ∩ G_0 ⊂ D, and (ii) S ∩ G_0 ⊂ D^{>0}.

*Proof.* Necessity is clear, because C ∩ G_0 = D gives C^{>0} ∩ G_0 = D^{>0}.

Sufficiency.
1. *Setup.* Put C_0 = Γ + D, a cone. Put U = S ∪ D^{>0} ∪ (S + D^{>0}) and T = U + C_0.
2. *U + U ⊂ U.* Check the cases. S + S ⊂ S. D^{>0} + D^{>0} ⊂ D^{>0}, because D is a valuation cone. Every other sum lands in S + D^{>0}. Hence T + T ⊂ T, and also Q_{>0}T ⊂ T.
3. *C_0 ∩ (-T) = ∅.* This is equivalent to U ∩ (-C_0) = ∅. We check each part of U.
   - d' ∈ D^{>0} with d' = -(γ + d), where γ ∈ Γ and d ∈ D. Then γ = -(d + d') ∈ Γ ∩ G_0 and γ ∉ D. This contradicts (i).
   - s ∈ S with s = -(γ + d). Then s + γ ∈ S ∩ G_0 and -(s + γ) = d ∈ D. This contradicts (ii).
   - s + d' = -(γ + d) with d' ∈ D^{>0}. Then s + γ ∈ S ∩ G_0 and -(s + γ) = d + d' ∈ D. This contradicts (ii).
4. *A maximal cone.* By Zorn's lemma (a union of a chain of such cones is again one) there is a maximal cone C ⊇ C_0 with C ∩ (-T) = ∅.
5. *C is a valuation cone.* Suppose g ∉ C ∪ (-C). By maximality, both C + Q_{>=0}g and C - Q_{>=0}g meet -T. So c_1 + αg = -t_1 and c_2 - βg = -t_2 with c_k ∈ C and t_k ∈ T. Here α, β > 0, because C ∩ (-T) = ∅. Then βc_1 + αc_2 = -(βt_1 + αt_2) lies in C ∩ (-T), a contradiction.
6. *C has the required properties.*
   - Γ ⊂ C_0 ⊂ C.
   - For s ∈ S we have -s ∈ -T, so -s ∉ C.
   - D ⊂ C. For g ∈ G_0 \ D, we have -g ∈ D^{>0} ⊂ T, so g ∈ -T and g ∉ C. Hence C ∩ G_0 = D. ∎

**Application 2.2.** Take H = G, Γ the cone spanned by Q, and S := Q_{>0}·f(P \ tau) + Γ.
- *S satisfies the hypotheses.* For the sum of two elements, absorb the second term r'f(x') into Γ: (r f(x) + γ) + (r' f(x') + γ') = r f(x) + (r' f(x') + γ + γ'), with r' f(x') ∈ Γ.
- *It describes C_tau.* For C with Γ ⊂ C, the condition S ∩ (-C) = ∅ is equivalent to f(x) ∈ C^{>0} for all x ∈ P \ tau. Indeed, the sum of a strictly positive element and a nonnegative one is strictly positive. So the cones of 2.1 with these data are exactly the elements of C_tau.
- *Consequence.* For a finite-dimensional subspace G_0 ⊂ G and the restriction ρ : X(G) -> X(G_0), C ↦ C ∩ G_0, we get
  ρ(C_tau) = {D ∈ X(G_0) : Γ_0 ⊂ D and -s ∉ D for all s ∈ S_0},
  where Γ_0 := Γ ∩ G_0 and S_0 := S ∩ G_0.

**Injective valuations.** Lemma 1.3 (⇒) uses the following special case. Take H = Q_σ^gp ⊗ Q, G_0 = 0, Γ the cone of Q_σ, and S = Q_{>0}(Q_σ \ 0) + Γ.
- Condition (ii) says 0 ∉ S. A relation r q + γ = 0 with q ≠ 0 gives, after clearing denominators, k q + q'' = 0 in Q_σ^gp with k >= 1 and q'' ∈ Q_σ. Then k q is a unit of Q_σ, so k q = 0 by sharpness, and q = 0 by torsion-freeness. This is a contradiction.
- So there is a valuation cone in which Q_σ \ 0 is strictly positive, i.e. an injective valuation of Q_σ.
- The same argument applied to Q gives an injective valuation v of Q. Its kernel on P is Phi_Q ⊂ tau, so C_v ∈ C_tau and C_tau ≠ ∅.

## 3. Reduction to finitely many data

1. Let L ⊂ N_tau be a finite subcomplex. Let J = vert(L) ∪ J_0, which is finite. Let N(J) := {σ ⊂ J nonempty : σ ∈ N_tau}. This is a finite subcomplex of N_tau containing L.
   - **It suffices to show that every such N(J) is contractible.** Every finite subcomplex then lies in a contractible finite subcomplex. Since simplicial homology commutes with the directed union of finite subcomplexes, the reduced homology of N_tau vanishes.
   - Nonemptiness: C_tau ≠ ∅ (§2) and C_tau ⊂ ∪_{J_0} E_i, so some i ∈ J_0 is a vertex of N_tau.
2. Let G_0 ⊂ G be the Q-span of the finitely many c_{i,m}, i ∈ J. Then:
   - E_i = ρ^{-1}(E_i^0) for i ∈ J, where E_i^0 := {D ∈ X(G_0) : c_{i,m} ∈ D for all m} is clopen in the compact space X(G_0).
   - By 1.3, for σ ⊂ J: σ ∈ N(J) ⇔ E_σ^0 ∩ ρ(C_tau) ≠ ∅.
   - By 1.4: ρ(C_tau) ⊂ U := ∪_{i in J} E_i^0, which is open.
3. *Approximation.* Let the index α run over pairs (Γ_α, F_α), where Γ_α ⊂ Γ_0 is a finitely generated cone and F_α ⊂ S_0 is finite, ordered by inclusion. This is a directed set. Put
   R_α := {D ∈ X(G_0) : Γ_α ⊂ D and -s ∉ D for all s ∈ F_α}.
   Each R_α is clopen (finitely many conditions on the generators of Γ_α and on F_α), and the R_α decrease. By 2.2, ∩_α R_α = ρ(C_tau).
4. *Choosing α.* By compactness of X(G_0):
   - The closed sets R_α \ U form a directed family with empty intersection, so R_α ⊂ U for all large α.
   - For each of the finitely many σ ⊂ J, the sets E_σ^0 ∩ R_α are closed and decreasing. So E_σ^0 ∩ ρ(C_tau) ≠ ∅ iff E_σ^0 ∩ R_α ≠ ∅ for all α. Hence, for α large, E_σ^0 ∩ R_α ≠ ∅ ⇔ σ ∈ N(J).
   - Fix one α with both properties. Let g_1..g_r generate Γ_α, and let F_α = {s_1..s_p}.

## 4. Real functionals and the nerve theorem

Let W = Hom_Q(G_0, R) ≅ R^d. For φ ∈ W, the set D_φ := {g ∈ G_0 : φ(g) >= 0} is a valuation cone of G_0. Define
- R^ℝ := {φ ∈ W : φ(g_k) >= 0 for all k, φ(s_l) > 0 for all l}, which is convex;
- T_i := {φ ∈ W : φ(c_{i,m}) >= 0 for all m}, a closed polyhedral cone, for i ∈ J.

(a) *If E_σ^0 ∩ R_α ≠ ∅, then T_σ ∩ R^ℝ ≠ ∅.*
- Let D be in the intersection. If p = 0, then φ = 0 works. Otherwise we need φ with φ(a) >= 0 for the finitely many a ∈ A := {g_k} ∪ {c_{i,m} : i ∈ σ}, and φ(s_l) > 0 for all l.
- By Motzkin's transposition theorem (quoted from memory: for real matrices, the system "Ax >= 0, Bx > 0" with B nonempty is infeasible iff there are y >= 0 and z >= 0, z ≠ 0, with A^T y + B^T z = 0; for rational data y and z can be taken rational), infeasibility would give rational y, z >= 0 with z ≠ 0 and Σ y_a a + Σ z_l s_l = 0 in G_0.
- In D, every a lies in D and every s_l in D^{>0}. A nonnegative combination in which some s_l has a positive coefficient lies in D^{>0}, so it is ≠ 0. This is a contradiction.

(b) *R^ℝ ⊂ ∪_{i in J} T_i.* For φ ∈ R^ℝ we have D_φ ∈ R_α ⊂ U, so D_φ ∈ E_i^0 for some i, i.e. φ ∈ T_i.

(c) *For σ ⊂ J: T_σ ∩ R^ℝ ≠ ∅ ⇔ σ ∈ N(J).*
- (⇒) If φ lies in the intersection, then D_φ ∈ E_σ^0 ∩ R_α.
- (⇐) Use (a) together with the choice of α.

(d) *Conclusion.*
1. For each σ ∈ N(J), pick φ_σ ∈ T_σ ∩ R^ℝ. Let Δ = conv{φ_σ}. It is compact, convex and nonempty, and Δ ⊂ R^ℝ by convexity of R^ℝ.
2. The sets T_i ∩ Δ, i ∈ J, are compact and convex. By (b) they cover Δ.
3. Their nerve is N(J). If T_σ ∩ Δ ≠ ∅, then σ ∈ N(J) by (c), since Δ ⊂ R^ℝ. Conversely, φ_σ ∈ T_σ ∩ Δ.
4. **Nerve theorem (Borsuk 1948 / Leray; quoted from memory):** a finite family of compact convex sets in R^d has nerve homotopy equivalent to its union.
5. Hence N(J) ≃ Δ, which is contractible.

## 5. Conclusion

By §3, N_tau is nonempty and every finite subcomplex lies in a contractible finite subcomplex N(J). So H̃_*(N_tau; Z) = 0.
- The ordered chain complex (tuples with repetitions allowed, as in the Čech complex) is chain-homotopy equivalent to the simplicial chain complex. This is standard and quoted from memory.
- The augmented ordered chain complex is therefore a free acyclic complex, hence split exact.
- Applying Hom(-, A) shows that the augmented ordered cochain complex with coefficients in A is exact.

This proves #19, and with it step 4 of the chain. **∎**

Remarks.
- Only the covering property of the family was used, never the birhizomy of the members. Lemma 1.2 shows that the locus of any f.p. member is closed and constructible in the patch topology. This is the structural fact behind the nerve acyclicity.
- The equivalent valuation form stated in the task (re-checked) is Lemma 1.3. There the valuations are restricted to divisible value groups, which is harmless, since every valuation can be composed with V ⊂ (V^gp ⊗ Q)_{>=0}.
- Two minor caveats about the chain itself. Step 3's "repeated indices are harmless" holds because, by 1.3, Phi_σ depends only on the set σ. I have not re-verified steps 1, 2, 5, 6 of the chain beyond this.

## Appendix A (by-product, not needed above): characterization of birhizomy, and openness

**Setting.** Let f : Q -> Q' be f.p., g : Q' -> V, and v = g f. Put K = v^{-1}(0) ⊂ Q and K' = g^{-1}(0) ⊂ Q', both faces. Put Q_K = Q[-K]^♯ and Q'_{K'} = Q'[-K']^♯. Their groups Q^gp/K^gp and Q'^gp/K'^gp are torsion-free. Since f^{-1}(K') = K, the map f induces α : Q^gp/K^gp -> Q'^gp/K'^gp.

For x ∈ Q_K^gp with v(x) > 0:
- let Γ(x) be the smallest convex subgroup of V^gp containing v(x);
- let F_x = {q ∈ Q_K : v(q) ∈ Γ(x)}, a face of Q_K.

Define
  M(v) := {0} ∪ {x ∈ Q_K^gp : v(x) > 0 and x ∈ F_x^gp}.

**Theorem C.** f is birhizomic at g iff (a) α is an isomorphism, and (b) under this identification Q'_{K'} ⊂ M(v).

*Proof.*

*(a) is necessary.*
1. Fix a torsion-free abelian group A and a homomorphism w : Q^gp -> A vanishing on K. Put M = {(a,b) ∈ V^gp × A : a > 0} ∪ {0}, h = (v, w) : Q -> M, and p = pr_1.
2. M is integral, saturated and sharp, and h(Q) ⊂ M.
3. p is infinitesimal. Suppose p(x) >= 0. If p(x) > 0, then x ∈ M. If p(x) = 0, then p(y) ≺ 0 forces p(y) = 0, hence y = 0, hence x ≺ 0, hence x = 0.
4. The maps u : Q' -> M with p u = g and u f = h are exactly the maps (g, u_2), where u_2 : Q'^gp -> A kills K' and satisfies u_2 f^gp = w.
5. Birhizomy says there is exactly one such u_2 for each w. So α^* : Hom(Q'^gp/K'^gp, A) -> Hom(Q^gp/K^gp, A) is bijective for every torsion-free A.
6. Taking A to be each of the two groups shows that α is an isomorphism (Yoneda).

*(b) is necessary.*
1. M(v) is a saturated sharp submonoid containing Q_K.
   - Closure under sums: if Γ(x) ⊂ Γ(x'), then Γ(x + x') = Γ(x') and F_x^gp ⊂ F_{x'}^gp.
   - Saturation: Q_K^gp/F^gp is torsion-free.
2. p = v : M(v) -> V is infinitesimal. Let p(x) > 0, y ∈ M(v), x ≺ y and v(y) ≺ v(x). Then y ∈ F_y^gp ⊂ F_x^gp because Γ(y) ⊂ Γ(x). From m y <= x <= n y in M(v) we get x = n y - (n y - x). Both terms lie in M(v) with values in Γ(x), so they lie in F_x^gp, and x ∈ M(v).
   - The case p(x) = 0 is handled as in (a).
3. Birhizomy gives u : Q' -> M(v) under Q. By (a) and uniqueness, u is the canonical map Q' -> Q'_{K'} ⊂ Q_K^gp. So Q'_{K'} ⊂ M(v).

*Sufficiency.* Let P' -h-> M -p-> V be a test factorization with p infinitesimal.
1. p is injective on M (R1), so h kills K.
2. Define u as the composite Q' -> Q'_{K'} ⊂ Q_K^gp --h^gp--> M^gp.
3. u lands in M. Let x ∈ M(v) \ 0. Write x = b - c with b, c ∈ F_x. Put X = h(x) and Y = h(b + c). Then X ≺ Y in M, because Y ± X ∈ 2h(F_x) ⊂ M. Also p(Y) = v(b + c) ≺ v(x) = p(X). Infinitesimality gives X ∈ M.
4. p u = g and u f = h hold by construction.
5. Uniqueness: any such u kills K' (since p is injective on M) and is determined on Q'_{K'}^gp = Q_K^gp. ∎

**Facts used below.**
- *Generators.* Since Q' is f.p., Q'_{K'} = sat(Q_K + N ā_1 + ... + N ā_k) for finitely many ā_j. Proof: Q' is a retract of Q'' as in 1.1, so Q' is the saturation of f(Q) together with finitely many elements. Every element of K' maps to 0 in Q'_{K'}.
- *R4.* The R4 condition "x = b - c with v(b + c) ≺ v(x)" is equivalent to x ∈ M(v).
- *R3 and Lemma A* are the special cases K = 0 of (b).

**Openness lemma.** Let v_1, ..., v_N be valuations of Q into a common ordered R-vector space. Assume they are *uniform*: they all have the same kernel K, and v_σ <= C v_τ on Q for all σ, τ. For λ ∈ Δ (the standard simplex) put w_λ = Σ_σ λ_σ v_σ. If Q -> Q' is birhizomic at a lift of w_λ, then w_{λ'} lifts to Q' for all λ' ∈ Δ with |λ' - λ|_1 < 1/(C N n).

*Proof.*
1. Here n is chosen so that each ā_j (from the generator fact) can be written ā_j = b_j - c_j with b_j, c_j ∈ Q_K and w_λ(b_j + c_j) <= n w_λ(ā_j). Such n exists because ā_j ∈ M(w_λ).
2. Choose τ with λ_τ >= 1/N. Then |v_σ(ā_j)| <= v_σ(b_j + c_j) <= C N w_λ(b_j + c_j).
3. Hence |w_{λ'}(ā_j) - w_λ(ā_j)| < w_λ(ā_j), so w_{λ'}(ā_j) > 0.
4. Also w_{λ'} kills K. So w_{λ'} extends to Q'_{K'} and therefore lifts to Q'. ∎

**Without uniformity the openness fails at the boundary of Δ.** Sets of the form [0,1) do occur as loci of members along non-archimedean segments. Take v_1(ā) > 0 and v_2(ā) < 0 with |v_2(ā)| infinitely small compared with v_1(ā). Then w_t(ā) >= 0 holds exactly for t ∈ [0,1). This is why the main proof avoids non-archimedean witnesses altogether: it works with real functionals on a finite-dimensional slice, where all member loci are closed.

## Summary of status

**Proved:**
- #19 as stated, in the stronger form of the Theorem above. It needs neither birhizomy (only the covering property), nor principality of tau, nor that Q be f.p. over P.
- Together with the chain in the task file, this yields a YES answer for every P, conditional on the chain's other steps, which I did not re-verify.
- By-products: Theorem C, which characterizes birhizomy at g, and the uniform openness lemma.

**Quoted from memory:**
- Motzkin's transposition theorem.
- Borsuk's nerve theorem for finite families of compact convex sets.
- The equivalence of ordered and oriented simplicial chain complexes.
- Tychonoff's theorem.
- The fact that filtered colimits of integral saturated sharp monoids are computed in monoids (#17 §1.1, re-checked).

**Open:** nothing remains open for #19 itself. I have not re-checked the chain's steps 1, 2, 5 and 6 (the Kan extension, the injective resolution, the sheaf condition, and Cartan's criterion).

=== END OF ANSWER round4_q5 ===
