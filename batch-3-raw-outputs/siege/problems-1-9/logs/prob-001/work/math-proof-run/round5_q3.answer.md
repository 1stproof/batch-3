# round5_q3: referee report on the round4_q5 proof of the nerve statement (#20)

Plan: check each step of the proof in order (§0, Lemmas 1.1–1.4, Lemma 2.1 and Application 2.2, §3, §4(a)–(d), §5). For each step I say whether it is correct and supply any repair needed. A verdict comes at the end.

Summary in advance: every step checks out. I found only presentational points, and I repair each of them below. I did not check Appendix A, which the proof does not use.

---

## §0 Conventions: correct

- **Torsion-freeness of Q^gp.** If nx = 0, saturation gives x ∈ Q, and likewise -x ∈ Q. Sharpness then gives x = 0. Correct.
- **Γ.** Clearing the denominators of Σ r_i q_i shows that every element of Γ has a positive integer multiple in Q. Correct.
- **From valuations to cones.** An ordered abelian group is torsion-free, and its ⊗Q carries a unique compatible total order. So C_v is a valuation cone, and it contains Q. Correct.
- **From cones to valuations.**
  - C ∩ -C is a Q-subspace.
  - The image V_C of C in G/(C∩-C) is the nonnegative part of a total order on that group.
  - V_C is integral and sharp. It is saturated because C is closed under multiplication by Q_{>0}.
  - The group of V_C is G/(C∩-C), because C ∪ -C = G.
  - g has image ≥ 0 iff g ∈ C + (C∩-C) = C. So C_{v_C} = C.
  - Correct.
- **Patch topology.**
  - X(G) is an intersection of conditions that are each clopen and each involve finitely many coordinates, so it is closed in {0,1}^G.
  - X_Q and C_tau are intersections of clopen sets, hence closed.
  - Restriction ρ : X(G) -> X(G_0) is a coordinate projection, so it is continuous, and C ∩ G_0 is again a valuation cone.
  - Correct.

## Lemma 1.1 (retract of a finite presentation): correct

- **The colimit.** Filtered colimits of iss monoids, computed in monoids, are iss. Each axiom is checked at a single stage:
  - Integrality: an equation that holds in the colimit already holds at some stage.
  - Saturation: x ∈ colim^gp = colim M_λ^gp, and nx equal to an element of M, both hold at some stage μ, so x_μ ∈ M_μ.
  - Sharpness: x + y = 0 holds at some stage.
  
  A filtered colimit in the under-category is computed in the underlying category.
- **Surjectivity.** For t ∈ Q', take any λ with t ∈ T. For elements of Q, use any λ.
- **Injectivity.** The iss reflection is a quotient of a submonoid of a quotient of M^gp. So its group is a quotient of (Q ⊕ N^T)^gp = Q^gp ⊕ Z^T, and the representatives z, z' exist.
  - Write z - z' = (q1, a+) - (q2, a-). The two terms have equal images in Q'^gp ⊇ Q'.
  - Adding the relation (q1, a+) ~ (q2, a-), which holds in Q', kills z - z' in Q''_{λ'}^gp. Since Q''_{λ'} is integral, x = y there.
- **Compactness.** Hom_Q(Q', colim Q''_λ) = colim Hom_Q(Q', Q''_λ). So id_{Q'} factors as r_λ s with s : Q' -> Q''_λ, and s is under Q.
- Correct.

## Lemma 1.2 (Fourier–Motzkin): correct

**Step 1 (transfer through the retraction).** If ℓ lifts v to Q_i, then ℓ r lifts v to Q''. If ℓ'' lifts v to Q'', then ℓ'' s lifts v to Q_i. Both work because r and s are maps under Q. Correct.

**Steps 2–3 (the linear system).**
- A map Q'' -> V under Q is the same as a map Q ⊕ N^T -> V that restricts to v on Q and respects R. Such a map factors through the congruence quotient, and then through the iss reflection because V is iss.
- So lifts correspond to y ∈ V^T with (n'_j - n_j)·y = v(q_j) - v(q'_j) = v_Q(b_j).
- Correct.

**Step 4 (elimination over W).** Write each equation as two non-strict inequalities, and include y_k ≥ 0. Over a totally ordered Q-vector space W, with rational coefficients and right-hand sides rational combinations of d = v_Q(b):
- An inequality with positive (respectively negative) coefficient on y_k gives a lower (respectively upper) bound for y_k. The division by a rational number is legitimate in W.
- Given values of the other variables that satisfy the derived system, the finitely many bounds lie in a totally ordered set. If max(lower) ≤ min(upper), then y_k := max(lower) works; if there is no lower bound, take min(upper); if there are no bounds, take 0.
- So "the system is feasible iff the derived system is feasible" holds over W, and the derived system is formal: it depends only on the coefficient matrix.
- After all variables are eliminated, each surviving condition reads 0 ≥ Σ u_j d_j, possibly with the sign flipped, i.e. Σ u'_j d_j ≥ 0 with u' rational.

Correct.

**Step 5.** v_Q is Q-linear, so v_Q(Σ u_{m,j} b_j) = Σ u_{m,j} d_j. Correct.

**(A).** A lift y ∈ V^T is a solution in W^T. Correct.

**(B).** If V^gp is divisible, then V^gp -> V^gp ⊗ Q is an isomorphism, because V^gp is torsion-free. So the solution lies in (V^gp)^T, and y ≥ 0 means y ∈ V^T, since the order is defined by V. Correct.

## Lemma 1.3: correct

**(⇒)**
- Q_σ is iss: the pushout is taken in iss monoids. So it has an injective valuation w; the special case of 2.1, checked below, provides it.
- v = w∘(Q -> Q_σ) lifts to each Q_i, i ∈ σ, through Q_i -> Q_σ. So C_v ∈ E_σ by 1.2(A).
- For x ∉ tau we have x ∉ Phi_σ. So the image of x in Q_σ is nonzero, w is positive on it, and -f(x) ∉ C_v. Also Q ⊂ C_v.
- The degenerate case Q_σ = 0 works with V = 0.

**(⇐)**
- For C ∈ E_σ ∩ C_tau, the extension v_{C,Q} is the quotient map G -> G/(C∩-C). So v_{C,Q}(c_{i,m}) ≥ 0 iff c_{i,m} ∈ C.
- V_C has divisible group, so 1.2(B) gives lifts under Q. The pushout property in iss monoids gives a map Q_σ -> V_C.
- Then x ∈ Phi_σ gives f(x) ∈ C ∩ -C, which forces x ∈ tau because C ∈ C_tau.

Correct.

## Lemma 1.4: correct

- For C ∈ C_tau, v_C : Q -> V_C is a valuation into a valuative monoid. The covering property gives a factorization through some Q_i, and 1.2(A) gives C ∈ E_i.
- C_tau is closed in the compact space X(G), hence compact, and the E_i are open.

Correct.

## Lemma 2.1 (extension lemma): correct

**Necessity.**
- Γ ∩ G_0 ⊂ C ∩ G_0 = D.
- For s ∈ S ∩ G_0 we have -s ∉ C, so -s ∉ D. Since D is a valuation cone of G_0, s ∈ D. So s ∈ D^{>0}.

**Step 2 (U + U ⊂ U).**
- D^{>0} + D^{>0} ⊂ D^{>0}. If d + d' ∈ -D with d, d' ∈ D^{>0}, then -d = -(d+d') + d' ∈ D, a contradiction.
- The mixed cases all land in S + D^{>0}. This uses S + S ⊂ S and D^{>0} + D^{>0} ⊂ D^{>0}.
- Hence T + T ⊂ T, Q_{>0}T ⊂ T and T + C_0 ⊂ T.

**Step 3 (U ∩ (-C_0) = ∅).**
- C_0 ∩ (-T) = ∅ iff U ∩ (-C_0) = ∅, because c = -(u + c') iff u = -(c + c').
- The three cases:
  - d' ∈ D^{>0} with d' = -(γ + d): then γ ∈ Γ ∩ G_0 ⊂ D would give -d' = γ + d ∈ D, a contradiction.
  - s = -(γ + d): then s + γ ∈ S ∩ G_0 ⊂ D^{>0}, but its negative d lies in D.
  - s + d' = -(γ + d): then s + γ = -(d + d') ∈ S ∩ G_0 ⊂ D^{>0}, but its negative d + d' lies in D.
- All three uses of S + Γ ⊂ S are legitimate. Correct.

**Steps 4–5.**
- Zorn's lemma applies: C_0 is admissible, and a union of a chain of admissible cones is admissible.
- Suppose g ∉ C ∪ -C. The cones C + Q_{≥0}g and C - Q_{≥0}g strictly contain C, so both meet -T. The coefficients α and β are > 0. Then βc_1 + αc_2 = -(βt_1 + αt_2) ∈ C ∩ -T, a contradiction.
- Correct.

**Step 6.**
- S ⊂ U ⊂ T, using 0 ∈ C_0.
- For g ∈ G_0 \ D we have -g ∈ D \ (-D) = D^{>0} ⊂ T, so g ∉ C.
- Correct.

## Application 2.2 and injective valuations: correct

**S satisfies the hypotheses.** S + S ⊂ S because r'f(x') ∈ Γ, since f(x') ∈ Q. Also Q_{>0}S ⊂ S and S + Γ ⊂ S. If P = tau, then S = ∅ and everything is trivial.

**S describes C_tau.** For C ⊇ Γ (equivalently C ⊇ Q):
- (⇒) Take s = f(x).
- (⇐) If -(rf(x) + γ) ∈ C, then -rf(x) ∈ C, and hence -f(x) ∈ C.

So the C of 2.1 with these data are exactly C_tau.

**The formula for ρ(C_tau).** Condition (ii), S_0 ⊂ D^{>0}, is equivalent to "-s ∉ D for all s ∈ S_0", because D is a valuation cone. So the formula for ρ(C_tau) is exactly 2.1. Correct.

**Injective valuations.**
- The data are G_0 = 0, D = {0} and D^{>0} = ∅. Condition (i) is trivial. Condition (ii) is 0 ∉ S.
- S satisfies S + S ⊂ S by the same absorption argument.
- Clearing denominators uses a common N with Nr ∈ Z_{≥1} and Nγ ∈ Q_σ.
- The relation kq + q'' = 0 makes kq a unit, so kq = 0 by sharpness, and q = 0 by torsion-freeness. Q_σ embeds in H because Q_σ^gp is torsion-free.
- Applied to Q: the kernel of v∘f is f^{-1}(0) = Phi_Q ⊂ tau, so C_v ∈ C_tau ≠ ∅.

Correct.

## §3 Compactness and approximation: correct

**Step 1.**
- Homology of a simplicial complex is the directed colimit of the homology of its finite subcomplexes. So "every finite subcomplex lies in a finite subcomplex with H̃ = 0", together with nonemptiness, gives H̃_*(N_tau) = 0, including H̃_0.
- Nonemptiness: C_tau ≠ ∅ and C_tau ⊂ ∪_{J_0} E_i give i ∈ J_0 with E_i ∩ C_tau ≠ ∅, so {i} ∈ N_tau by 1.3.
- Since J ⊇ J_0, N(J) is nonempty for every J. This matters in §4(d), where Δ must be nonempty.

**Step 2.**
- E_i = ρ^{-1}(E_i^0), because c_{i,m} ∈ G_0.
- σ ∈ N(J) ⇔ ρ^{-1}(E_σ^0) ∩ C_tau ≠ ∅ ⇔ E_σ^0 ∩ ρ(C_tau) ≠ ∅.
- ρ(C_tau) ⊂ ∪_J E_i^0 uses J_0 ⊂ J.
- (Notation clash: this U is not the U of 2.1. This is harmless.)

**Step 3.**
- R_α is clopen: Γ_α ⊂ D iff the finitely many generators lie in D.
- R_α is decreasing in α.
- ∩_α R_α = {D : Γ_0 ⊂ D, -s ∉ D for all s ∈ S_0}, since each element of Γ_0 generates an admissible Γ_α. This set is ρ(C_tau) by 2.2.

**Step 4.** X(G_0) is compact (closed in {0,1}^{G_0}). In a compact space, a downward-directed family of closed sets with empty intersection has an empty member.
- Since ∩_α(R_α \ U) = ∅, this gives R_{α_0} ⊂ U for some α_0, and hence for all α ≥ α_0.
- For each of the finitely many σ ⊂ J with σ ∉ N(J), the family E_σ^0 ∩ R_α has empty intersection, so it is empty for some α_σ.
- For σ ∈ N(J), E_σ^0 ∩ R_α ⊇ E_σ^0 ∩ ρ(C_tau) ≠ ∅ for every α.
- An α above α_0 and all the α_σ exists by directedness.

Correct.

## §4 Real functionals: correct

**Preliminaries.** D_φ is a valuation cone of G_0, R^ℝ is convex (an intersection of closed and open half-spaces), and the T_i are closed.

**(a) Motzkin.** Motzkin's transposition theorem (from memory): for real matrices A and B with B nonempty, exactly one of the following holds:
- there is x with Ax ≥ 0 and Bx > 0;
- there are y ≥ 0 and z ≥ 0 with z ≠ 0 and A^T y + B^T z = 0.

The proof quotes this correctly, with B the strict rows s_l.

*Rationality of the certificate.* The proof only asserts this, so here is a justification.
- Coordinatize G_0 by a Q-basis. Then W ≅ R^d, and A and B have rational entries.
- The certificates normalized by Σz = 1 form a nonempty polyhedron defined over Q. It has a vertex, which is rational.
- The rational vector identity then holds in G_0 itself.

*The contradiction in D.* Every a lies in D, since Γ_α ⊂ D and D ∈ E_σ^0. Every s_l lies in D^{>0}. A sum of an element of D and an element of D^{>0} lies in D^{>0}: if d + d' ∈ -D, then -d' ∈ D. So the combination is nonzero, a contradiction. The case p = 0 is handled by φ = 0. Correct.

**(b).** φ ∈ R^ℝ gives D_φ ⊇ Γ_α, because D_φ is a cone containing the generators g_k. Also -s_l ∉ D_φ. So D_φ ∈ R_α ⊂ U, and hence φ ∈ T_i for some i ∈ J. Correct.

**(c).** Both directions are correct, as written.

**(d) The nerve theorem.**
- Δ is a nonempty polytope, nonempty because N(J) ≠ ∅, and Δ ⊂ R^ℝ by convexity.
- The T_i ∩ Δ are compact and convex, and they cover Δ by (b).
- Their nerve is exactly N(J), by (c) and the points φ_σ. Members with T_i ∩ Δ = ∅ simply do not appear, which is consistent with i ∉ N(J).
- The nerve theorem for finite families of compact (even closed) convex sets in R^d is correctly quoted (Borsuk 1948, from memory). Only acyclicity is needed, and that also follows from Leray's theorem or Mayer–Vietoris.
- So N(J) ≃ Δ, which is contractible.

Correct.

## §5 Ordered chains: correct

- The ordered chain complex of a simplicial complex (tuples with repetitions whose underlying set is a simplex) has the same homology as the oriented complex. This is standard (acyclic models) and holds for infinite complexes. Alternatively, both commute with directed unions of finite subcomplexes.
- The augmented ordered complex is a free complex, bounded below and acyclic. So it is contractible, and Hom(-, A) of it is exact.

Correct.

## Side remark: repeated indices

The proof's remark says that Phi of a tuple with repetitions depends only on its underlying set. This is outside the statement, but it is true for a simpler reason than the one given.
- Let i_* be a tuple with underlying set σ. The codiagonal gives a map Q_{i_*} -> Q_σ under P, and the inclusion of summands gives a map Q_σ -> Q_{i_*} under P.
- So Phi_{i_*} = Phi_σ exactly.
- This matters because the pushout Q_i ⊔_Q Q_i is not Q_i in general. Lemma 1.3 does hold verbatim for tuples, though.

## Minor observations (not gaps)

- The hypothesis that tau is a face of P is never used. Only Phi_Q ⊂ tau is used, and only to get C_tau ≠ ∅.
- The proof also uses neither birhizomy of the members nor finite presentation of Q over P, as it claims.
- In Lemma 1.2, the vectors c_{i,m} depend on the chosen presentation (b and M). They do not depend on v, which is all that is needed.

## VERDICT

VERDICT: the proof establishes the statement exactly as stated.

I checked every step and none has a gap. The only unexplained point was the rationality of the Motzkin certificate in §4(a), and I have written out its justification above. Everything quoted from memory is quoted correctly and used within its hypotheses: Tychonoff, Zorn, Motzkin transposition, Borsuk's nerve theorem, and ordered versus simplicial chains. Appendix A was not checked. Nothing remains open for statement #20 itself. This audit does not cover the other steps of the chain to the headline YES answer.

=== END OF ANSWER round5_q3 ===
