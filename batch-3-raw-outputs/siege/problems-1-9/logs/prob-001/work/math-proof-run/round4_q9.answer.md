# Answer to round4_q9: the nerve statement #19

## Result

**Theorem (#19, proved).** Let P be any monoid (integral, saturated, sharp; not necessarily finitely generated) and f : P -> Q any morphism. Let {Q -> Q_i}_{i in I} be a family of f.p. maps under Q with the following *factorization cover property*: for every valuative V and every v : Q -> V, some Q_i -> V extends v. Let tau be **any** face of P with Phi_Q ⊂ tau. Then N_tau = {sigma ⊂ I finite nonempty : Phi_sigma ⊂ tau} has these two properties:
- it is nonempty;
- every finite subcomplex of it is contained in a finite *contractible* subcomplex.

Hence N_tau has vanishing reduced integral homology, and its augmented ordered cochain complex with coefficients in any abelian group A is exact.

What the proof does not use:
- Birhizomicity is not used beyond the factorization it implies. A birhizomic cover has the factorization cover property.
- Principality of tau is not used.
- Finite presentation of f is not used.
- Finite presentation of Q -> Q_i is used, through Lemma 1.

The idea that replaces the missing nerve theorem for non-closed sets is to take convex combinations of witness valuations with coefficients in a **real closed field F** that contains all the value groups. The sets "λ such that w_λ lifts to Q_i" are then *closed* polyhedra over F. The real nerve theorem then transfers to F by Tarski's theorem.

Results quoted from memory (all standard):
- (T1) Fuchs/Levi: on a torsion-free abelian group, every isolated partial order (nx >= 0 ⇒ x >= 0) extends to a total order.
- (T2) Hahn embedding: every ordered abelian group embeds, as an ordered group, in the additive group of a Hahn field R((t^Γ')) with Γ' a divisible ordered group, and such a field is real closed.
- (T3) Tarski: the theory of real closed fields is complete.
- (T4) Nerve theorem (Borsuk 1948, Leray): a finite family of compact convex sets in R^n has nerve homotopy equivalent to its union.
- (T5) Compact objects of a reflective subcategory closed under filtered colimits; see Lemma 1.

## Notation

A *valuation* of Q is a homomorphism v : Q -> V≥0, where V is a totally ordered abelian group. We write v also for v^gp : Q^gp -> V.

For an object Q -> Q' under Q, we say *v lifts to Q'* if there is a map Q' -> V≥0 under Q.

## Lemma 0 (valuation form of the nerve condition; re-check of the director's note)

For finite nonempty sigma ⊂ I, Phi_sigma ⊂ tau holds iff some valuation v of Q satisfies both:
- v lifts to every Q_i with i in sigma;
- v(f(x)) > 0 for all x ∈ P \ tau.

*Proof.*

(⇒) Q_sigma is integral, saturated and sharp. So its partial order (positive cone Q_sigma) on the torsion-free group Q_sigma^gp is isolated: nx ∈ Q_sigma ⇒ x ∈ Q_sigma. It is also antisymmetric, by sharpness. By (T1) it extends to a total order, which gives an injective map u : Q_sigma -> V≥0 with u(q) = 0 only for q = 0. Put v = u∘(Q -> Q_sigma).
- v lifts to each Q_i via u∘(Q_i -> Q_sigma).
- If x ∈ P \ tau, then x ∉ Phi_sigma, so the image of x in Q_sigma is nonzero, and v(f x) > 0.

(⇐) Compatible lifts Q_i -> V≥0 (i ∈ sigma) induce a map Q_sigma -> V≥0, because V≥0 is integral, saturated and sharp and Q_sigma is the pushout in that category. If x ∈ Phi_sigma, then v(f x) = 0, so x ∈ tau. ∎

The same argument shows that the condition depends only on the *set* sigma. A valuation lifts to Q_i ⊕_Q Q_i iff it lifts to Q_i: use the same lift twice.

## Lemma 1 (lifting is cut out by finitely many sign conditions)

Let Q -> Q' be f.p. in the category C of integral saturated sharp monoids, under Q. Then there are finitely many y_1, ..., y_R ∈ Q^gp with the following property: for every valuation v : Q -> V≥0 with V **divisible**, v lifts to Q' iff v(y_r) >= 0 for all r.

*Proof.*

(a) *Reduction to a finite presentation.* Let C' be the category of commutative monoids, and let ρ : C' -> C be the reflection (integralize, saturate, sharpen). By 1.1 of round3_q4 (re-checked: each axiom is witnessed by finitely many elements), filtered colimits in C are computed in C'. As in any category of algebras, every commutative monoid under Q is the filtered colimit, under Q, of finitely presented ones A_{T,R} = (Q ⊕ N^T)/⟨R⟩, with T and R finite. Applying the left adjoint ρ gives Q' = colim ρ(A_{T,R}) in Q/C. Since Q' is compact in Q/C, id_{Q'} factors through some ρ(A_{T,R}). So Q' is a retract under Q of A' := ρ(A_{T,R}) = (Q ⊕ N^T / R)^{int,sat,sharp}.
- If maps s : Q' -> A' and r : A' -> Q' under Q satisfy rs = id, then v lifts to Q' iff v lifts to A'. Indeed, a lift g of v to Q' gives the lift gr to A', and a lift g' to A' gives the lift g's to Q'.
- By adjunction, lifts of v to A' with values in V≥0 (an object of C) are exactly the vectors y ∈ V^T with y >= 0 that satisfy, for each relation ((a_j, m_j), (b_j, n_j)) ∈ R (a_j, b_j ∈ Q, m_j, n_j ∈ N^T), the equation (m_j − n_j)·y = v(b_j − a_j).

(b) *Fourier–Motzkin.* Consider a finite system of non-strict linear inequalities with rational coefficients in unknowns y ∈ V^T, with right-hand sides that are rational linear combinations of parameters β ∈ V^J, where V is an ordered divisible group (equations count as two inequalities).
- Eliminating one variable replaces the system by all pairwise "lower bound <= upper bound" inequalities, together with the inequalities not involving that variable.
- The new system has a solution iff the old one does. Given a solution of the new system, the eliminated variable can be set to the maximum of its lower bounds, or to any upper bound or to 0 if there are none. This uses only divisibility by rationals and finite maxima.
- After all variables are eliminated, solvability is equivalent to a finite conjunction ∧_r L_r(β) >= 0. Here the L_r are rational linear forms that **do not depend on V**.

Apply this with β_j = v(b_j − a_j), and let y_r := N_r Σ_j L_{rj}(b_j − a_j) ∈ Q^gp, where N_r > 0 clears denominators. ∎

## Lemma 2 (finite subcover)

Let X be the set of W ⊂ Q^gp such that Q ⊂ W, W + W ⊂ W and W ∪ (−W) = Q^gp. Give X the topology induced from {0,1}^{Q^gp}. Then X is compact.

Each valuation v gives a point W_v = {x : v(x) >= 0} of X. Every W ∈ X arises this way: put U = W ∩ (−W). The group Q^gp/U is torsion-free: if nx ∈ U and, say, −x ∈ W, then x = nx + (n−1)(−x) ∈ W. Hence W/U is the nonnegative cone of a total order, and v_W : Q -> (Q^gp/U)≥0 is a valuation.

For each i, let E_i = {W : y^{(i)}_r ∈ W for all r}, with the y^{(i)}_r of Lemma 1 for Q -> Q_i. Then:
- E_i is open, being a finite intersection of the clopen sets {W : y ∈ W}.
- By Lemma 1, a valuation v into a divisible group lifts to Q_i iff W_v ∈ E_i.
- **The E_i cover X.** Take W ∈ X, and compose v_W with the divisible hull D of Q^gp/U. D≥0 is valuative. By the cover property, some Q_i -> D≥0 extends this valuation, so W ∈ E_i.

X is closed in the compact space {0,1}^{Q^gp}: each defining condition involves at most three coordinates. Hence there is a **finite J_0 ⊂ I with X = ∪_{i∈J_0} E_i**. ∎

## Proposition 3 (the finite nerves are contractible)

Let J' ⊂ I be finite with J' ⊇ J_0, and let N' = N_tau(J') = {sigma ∈ N_tau : sigma ⊂ J'}. Then N' is nonempty and contractible.

*Proof.*

*Nonempty.* Q has an injective valuation u, by (T1) as in Lemma 0. Since Phi_Q ⊂ tau, we have u(f x) > 0 for x ∈ P \ tau. By Lemma 2 (after passing to the divisible hull), u lifts to some Q_i with i ∈ J_0. By Lemma 0, {i} ∈ N'.

*Witnesses.* Let Σ be the (finite, nonempty) set of simplices of N'. For each sigma ∈ Σ, Lemma 0 gives a valuation v_sigma : Q -> V_sigma≥0 that lifts to each Q_i (i ∈ sigma) and satisfies v_sigma(f x) > 0 for x ∈ P \ tau.

Put G = ⊕_{sigma∈Σ} V_sigma with the lexicographic order for some ordering of Σ. Each coordinate inclusion V_sigma -> G is an order embedding. By (T2), G embeds as an ordered group in the additive group of a real closed field F. Composing with these embeddings changes neither the lifting property nor the strict positivity, so we may assume every v_sigma takes values in F.

*Convex combinations.* Let Δ = Δ(F) = {λ ∈ F^Σ : λ_sigma >= 0, Σ λ_sigma = 1}, and put w_λ := Σ_sigma λ_sigma v_sigma : Q^gp -> F.
- w_λ is a valuation Q -> F≥0, and F≥0 is a valuative monoid.
- For q ∈ Q, w_λ(q) = 0 iff v_sigma(q) = 0 for all sigma with λ_sigma > 0. Nonnegative terms cannot cancel, and some λ_sigma > 0. Hence w_λ(f x) > 0 for all x ∈ P \ tau.

*The sets K_i.* For i ∈ J' put K_i := {λ ∈ Δ : w_λ(y^{(i)}_r) >= 0 for all r} = {λ ∈ Δ : Σ_sigma λ_sigma v_sigma(y^{(i)}_r) >= 0 for all r}.
- **K_i is a closed convex polyhedron over F**: it is the intersection of Δ with finitely many closed half-spaces with coefficients in F.
- By Lemma 1, applied with V = F (which is divisible), λ ∈ K_i iff w_λ lifts to Q_i with values in F≥0.
- **The K_i (i ∈ J') cover Δ**: W_{w_λ} lies in some E_i with i ∈ J_0 ⊂ J'.

*Nerve.* For nonempty sigma' ⊂ J', we have ∩_{i∈sigma'} K_i ≠ ∅ iff sigma' ∈ N'.
- (⇒) If λ lies in the intersection, then w_λ lifts to every Q_i (i ∈ sigma') and w_λ(f x) > 0 off tau. By Lemma 0, Phi_{sigma'} ⊂ tau.
- (⇐) If sigma' ∈ Σ, the vertex e_{sigma'} lies in every K_i with i ∈ sigma', because w_{e_{sigma'}} = v_{sigma'}.

So N' is the nerve of the finite family of closed F-polyhedra {K_i} that covers Δ(F). In this nerve, the vertices are the nonempty K_i.

*Transfer.* Fix m = |J'|, n = |Σ|, the numbers R_i of inequalities, and an abstract simplicial complex N on a subset of [m]. Consider the following condition on a matrix of coefficients h:
1. The polyhedra K_i(h) := {λ ∈ Δ : Σ_sigma h^{(i)}_{r,sigma} λ_sigma >= 0 for all r} cover Δ.
2. For every nonempty sigma' ⊂ [m], ∩_{i∈sigma'} K_i(h) ≠ ∅ holds iff sigma' ∈ N.

"There exists h satisfying 1 and 2" is a first-order sentence in the language of ordered fields, with no parameters.

In R, each K_i(h) is compact and convex and their union is the simplex. So by (T4), N is homotopy equivalent to the simplex, hence contractible. Therefore, for non-contractible N the sentence is false in R. By (T3) it is false in F. Our N' satisfies the sentence in F, so N' is contractible. ∎

## Conclusion

Let L be any finite subcomplex of N_tau, and put J' = vert(L) ∪ J_0. Then L ⊂ N_tau(J'), which is nonempty and contractible by Proposition 3. Reduced homology commutes with this directed union of finite subcomplexes, so the reduced integral homology of N_tau vanishes, and N_tau is nonempty.

The ordered (repetition-allowed) augmented chain complex computes the same homology. It is therefore an acyclic, bounded-below complex of free abelian groups, hence split exact. Applying Hom(−, A) gives an exact augmented ordered cochain complex. This is exactly #19. ∎

## Remarks on the chain (#16 → headline)

- Step 3 of the chain only needs #19 for coverings of f.p. objects, with tau = Phi_b principal. That is a special case of the theorem above.
- Repeated indices are harmless (Lemma 0).
- I re-checked the following and found no flaw:
  - Steps 2 and 3: the injectivity of I_{tau,A}, via Hom(F, I_{tau,A}) = Hom(F(tau), A), and the embedding of F into ∏_tau I_{tau,E(F(tau))};
  - Step 5: G^+ = G on f.p. objects when Ȟ^0 = G(U) for every covering of every f.p. U, all of whose members are f.p.;
  - Step 6: the Cartan setup.
- The chain does assume that birhizomic covers *are* the coverings of a pretopology, rather than generating the topology. If they only generate it, Čech colimits over the cofinal family of birhizomic covers give the same plus-construction, so nothing changes.
- I did not re-audit #16/#17 beyond what is used here.
- With #19 proved, the chain answers the headline question **YES for every monoid P**. This rests on the chain's own steps and on the cited facts (T1)–(T5) and Cartan's criterion.

## What is proved / not proved

- **Proved:** #19 in the generality stated, and more: tau can be any face containing Phi_Q, and the cover only needs the factorization property. The proof relies on the standard facts (T1)–(T5), cited from memory.
- **Not separately re-proved here:** the remaining steps of the chain (#16, Cartan's criterion, the Kan-extension identifications). These were checked only at the level described above.
- **Open:** nothing inside #19.

=== END OF ANSWER round4_q9 ===
