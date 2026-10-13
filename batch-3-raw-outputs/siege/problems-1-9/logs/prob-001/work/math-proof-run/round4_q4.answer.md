# round4_q4: attempt to refute #19

## Plan (written first; updated as I go)
1. Find the *initial* infinitesimal test object M_v for a valuation v of Q. This turns "birhizomic at g" into a concrete criterion: the existence of a lift Q_i -> M_v, plus uniqueness.
2. Use the criterion to describe the birhizomic loci E_i^b, and in particular prove an "openness" property (the blocking lemma asked for).
3. Test the suggested counterexample spaces against the criterion.
4. Record what is proved and what remains open.

Conventions: as in the query. For a valuation v : Q -> V write Phi_v = v^{-1}(0), a face of Q. Write Qbar_v = Q[-Phi_v]^sharp = (Q + Phi_v^gp)/Phi_v^gp and L_v = Q^gp/Phi_v^gp = Qbar_v^gp, which is torsion-free. vbar : Qbar_v -> V is the induced map; it has trivial kernel.

## 1. The initial infinitesimal test object (proved)

**Definition.** M_v = {0} ∪ { x ∈ L_v : vbar(x) > 0, and there are y ∈ Qbar_v and n ≥ 1 with y + x ∈ Qbar_v, y - x ∈ Qbar_v and vbar(y) ≤ n vbar(x) }. Let p_v = vbar^gp restricted to M_v, and let iota : Q -> Qbar_v ⊂ M_v.

**Theorem 1.** (a) M_v is an integral, saturated, sharp monoid with Qbar_v ⊂ M_v and M_v^gp = L_v, and p_v : M_v -> V is infinitesimal with p_v iota = v.
(b) (M_v, iota, p_v) is initial among triples (M, h, p) with h : Q -> M, p : M -> V infinitesimal and ph = v. That is, there is exactly one homomorphism phi : M_v -> M with phi iota = h, and it satisfies p phi = p_v.

*Proof of (a).*
- Q̄ ⊂ M_v: take y = x.
- Closed under addition: if y1 witnesses x1 and y2 witnesses x2, then y1 + y2 witnesses x1 + x2.
- Saturated: suppose nx ∈ M_v with witness y. Then n(y + x) = (y + nx) + (n-1)y lies in Q̄, so y + x ∈ Q̄ by saturation. Likewise y - x ∈ Q̄. Also v̄(y) ≺ v̄(nx) ≺ v̄(x).
- Sharp: x and -x cannot both have positive value.
- M_v^gp = L_v, because Q̄ ⊂ M_v.

*Infinitesimality.* Suppose x ∈ L_v, y ∈ M_v, p(x) ∈ V, my ≤ x ≤ ny in M_v, and m' p(x) ≤ p(y) ≤ n' p(x).
- If p(x) = 0, then p(y) = 0, so y = 0, since p_v has trivial kernel on M_v. Then 0 ≤ x ≤ 0 gives x = 0.
- If p(x) > 0, put N = max(|m|, |n|). Then Ny - x and Ny + x lie in M_v, and y ≠ 0 (otherwise ±x ∈ M_v, so x = 0).
  - Let z, z1, z2 ∈ Q̄ witness y, Ny - x and Ny + x respectively (take z_i = 0 if the element is 0).
  - Put y' = z1 + z2 + Nz. Then y' - x = [z1 + (Ny - x)] + z2 + N(z - y) ∈ Q̄ and y' + x = [z2 + (Ny + x)] + z1 + N(z - y) ∈ Q̄.
  - v̄(z) ≺ v̄(y) ≤ n' v̄(x), and v̄(Ny ± x) ≤ (Nn' + 1) v̄(x). So v̄(y') ≤ K v̄(x) for some K.
  - Hence x ∈ M_v. ∎

*Proof of (b).*
- By R1, h(Φ_v) ⊂ p^{-1}(0) = 0. So h^gp induces h̄ : L_v -> M^gp with h̄(Q̄) ⊂ M and p^gp h̄ = v̄^gp.
- Let x ∈ M_v \ 0 with witness y. Then -h̄(y) ≤ h̄(x) ≤ h̄(y) in M, so h̄(x) ≺ h̄(y). Also p(h̄(y)) = v̄(y) ≺ v̄(x) = p(h̄(x)) ∈ V. Infinitesimality of p gives h̄(x) ∈ M.
- So φ = h̄|_{M_v} works. It is unique because Q̄ generates L_v. ∎

**Corollary 2 (criterion for birhizomy; proved).** Let f : Q -> Q' be f.p., g : Q' -> V, v = gf, and Φ' = g^{-1}(0). Then f is birhizomic at g iff both of the following hold:
- (E) there is u_0 : Q' -> M_v with u_0 f = iota and p_v u_0 = g;
- (U') the cokernel of f^gp(Q^gp) + Φ'^gp -> Q'^gp is torsion.

*Proof.*
- Sufficiency.
  - Existence: compose u_0 with the map φ of Theorem 1(b).
  - Uniqueness: let u, u' be two solutions in a test M. They agree on f(Q). They also agree on Φ', since both send Φ' into p^{-1}(0) = 0. So they agree on a subgroup of finite index, and M^gp is torsion-free (M is saturated and sharp). Hence u = u'.
- Necessity of (E): M_v is itself a test object.
- Necessity of (U').
  - Suppose (U') fails. The cokernel is finitely generated (Q' is f.p.), so there is a nonzero δ : Q'^gp -> Z vanishing on f(Q^gp) + Φ'^gp.
  - Put M = {(x, k) ∈ L_v × Z : x ∈ M_v \ 0} ∪ {(0,0)} and p(x, k) = p_v(x).
  - M is integral, saturated and sharp. It is infinitesimal over V: the first coordinate reduces this to the infinitesimality of M_v, and the kernel is trivial.
  - Both u = (u_0, 0) and u' = (u_0, δ) are solutions with values in M. Indeed, for q ∈ Q' either u_0(q) ≠ 0, or g(q) = 0, in which case q ∈ Φ' and δ(q) = 0.
  - Since δ ≠ 0, these two solutions differ. ∎

**Corollary 3 (Proposition B and R4 in every rank, for every Q; proved).** Let Q ⊂ Q' ⊂ Q^gp with Q' saturated and Q' f.p. over Q, let g : Q' -> V, and suppose Φ_v = 0 on Q. Then Q -> Q' is birhizomic at g iff every a in a generating set of Q' (generating as a saturated monoid over Q) satisfies both:
- v(a) > 0;
- there is y ∈ Q with y ± a ∈ Q and v(y) ≺ v(a).

Equivalently, a = b - c with b, c ∈ Q and v(b + c) ≺ v(a), possibly after replacing a by 2a.

*Proof.* Here (U') is automatic, and (E) says Q' ⊂ M_v. Since M_v is a saturated monoid containing Q, it suffices to check generators. ∎

So the sufficient condition of R4 is also necessary, and Lemma A is a special case.

## 2. Openness of birhizomic loci (the blocking property; proved)

Let f : Q -> Q' be f.p. Then Q' is a retract under Q of (Q ⊕ N^k / R)^{int,sat,sharp}; this is cited from memory, as in #16. Let a_1, ..., a_k be the images of the basis vectors. Then every q' ∈ Q' has a multiple n q' ∈ f(Q) + Σ N a_j. Call such a_j *generators* of Q' over Q.

Write E^b(Q') for the set of valuations v of Q such that f is birhizomic at some lift g of v.

**Lemma 4 (transport).** Let v ∈ E^b(Q') via u_0 as in (E). Put x_j = u_0(a_j) ∈ M_v, and let y_j be a witness for x_j when x_j ≠ 0. Let w be a valuation of Q with Φ_w ⊇ Φ_v, and let π : L_v -> L_w be the projection. Suppose that for each j, either π(x_j) = 0, or w̄(πx_j) > 0 and w̄(πy_j) ≺ w̄(πx_j). Then w ∈ E^b(Q').

*Proof.*
- π(Q̄_v) ⊂ Q̄_w, so π(y_j) witnesses π(x_j) ∈ M_w.
- M_w is saturated and every element of Q' has a multiple in f(Q) + Σ N a_j. Hence π u_0(Q') ⊂ M_w, and π u_0 f = iota_w.
- Put g_w = p_w π u_0. This gives (E) for w.
- p_v and p_w have trivial kernels, so g_w^{-1}(0) = (π u_0)^{-1}(0) ⊇ u_0^{-1}(0) = g^{-1}(0). Therefore (U') for w follows from (U') for v. ∎

**Corollary 5.** E^b(Q') is stable under the following two operations:
- (i) Coarsening: w = c ∘ v with c : V -> W a monotone surjection. If w(x_j) = 0 then w(y_j) = 0. Then y_j and y_j ± x_j have preimages in Φ_w, so π(x_j) = 0. Otherwise v(y_j) ≤ n v(x_j) gives w(y_j) ≤ n w(x_j).
- (ii) Refinement with the same kernel: Φ_w = Φ_v and v̄(x) > 0 ⇒ w̄(x) > 0. Then v((n+1)x_j - y_j) > 0, so w(y_j) ≤ (n+1) w(x_j).

Part (ii) is the "Lemma A pattern" of the director's sketch (d), now proved. One restriction applies: a refinement of v that is nonzero on Φ_v can leave the locus. The example is Q' = Q[-x]^sharp with x ∈ Φ_v, by R2.

**Lemma 6 (relative openness on open faces of the convexification).**
- Setting: valuations v_1, ..., v_r of Q, all with values in one Hahn-type ordered real vector space H, and Δ the standard simplex. Put w_μ = Σ μ_σ v_σ for μ ∈ Δ.
- Claim: if w_λ ∈ E^b(Q') and s = supp(λ), then w_μ ∈ E^b(Q') for all μ in a neighbourhood of λ inside the open face relint(Δ_s).

*Proof.*
- Kernels are constant on the open face. For μ ∈ relint(Δ_s), Φ_{w_μ} = ∩_{σ∈s} Φ_{v_σ} = Φ_{w_λ}, because there is no cancellation among nonnegative values.
- Fix j with x_j ≠ 0. The leading class γ of w_μ(y_j) is the maximum of the leading classes of the v_σ(y_j), σ ∈ s, and so does not depend on μ in the open face.
- From y_j ± x_j ∈ Q̄ we get |w_μ(x_j)| ≤ w_μ(y_j). So the coefficients of w_μ(x_j) above γ vanish.
- At λ, w_λ(x_j) > 0 and w_λ(y_j) ≤ n w_λ(x_j). Hence the γ-coefficient c(λ) of w_λ(x_j) is positive.
- c(μ) is linear in μ, so c(μ) > 0 near λ. Then w_μ(x_j) > 0 with the same leading class as w_μ(y_j), i.e. w_μ(y_j) ≺ w_μ(x_j).
- Apply Lemma 4 with π = id. ∎

This is exactly where the ≺ clause enters. Without it, the condition w_μ(x_j) > 0 would not be open: the leading coefficient of w_λ(x_j) could vanish while a higher-class coefficient changes sign nearby.

## 3. Reduction of #19 to a convex covering property (H*), without Lemma K (proved)

Setting of #19. F_i is the set of valuations of Q that factor through Q_i. We use the director's valuation form: σ ∈ N_τ iff some valuation v ∈ C_τ has compatible lifts to all Q_i, i ∈ σ, with values in a single valuative V.

**Convexification data.**
- Let J ⊂ I be finite. For each simplex σ of N_τ(J) choose a witness v_σ : Q -> V_σ with compatible lifts g_{σ,i} : Q_i -> V_σ, i ∈ σ, and v_σ ∈ C_τ.
- Embed all the V_σ^gp in one Hahn product H = R^((Γ)), where Γ is the disjoint union of the Γ_σ, given *some* total order. This uses Hahn's embedding theorem, cited from memory. H_{≥0} is a valuative monoid.
- Let Δ be the simplex with vertex set {σ}, and put w_μ = Σ μ_σ v_σ.
- Let K_i = {μ ∈ Δ : w_μ lifts to some Q_i -> H_{≥0}}.

**Properties.**
1. K_i is convex: a convex combination of lifts is a lift.
2. If ∩_{i∈σ'} K_i ≠ ∅, then σ' ∈ N_τ.
   - The lifts at a common point μ define a map Q_{σ'} -> H_{≥0}.
   - Its kernel on P lies in ∩_{supp μ} ker(v_σ|_P) ⊂ τ, because there is no cancellation.
3. Each vertex e_σ lies in K_i for all i ∈ σ. So the nerve of {K_i}_{i ∈ J'} contains N_τ(J) for every J' ⊇ J.
4. The cover property applied to w_μ : Q -> H_{≥0} gives an i and a lift into H_{≥0} itself. So the sets K_i^b = {μ : w_μ ∈ E^b(Q_i) with a lift into H_{≥0}} ⊂ K_i cover Δ, and Lemma 6 applies to them.

**(H*)** For the given data, Δ is a finite union of compact convex sets D_1, ..., D_r with D_k ⊂ K_{i(k)}.

**Proposition 7.** Suppose (H*) holds for every choice of convexification data, or merely for one choice for each finite J. Then #19 holds.

*Proof.*
- **Nonemptiness.** Φ_Q ⊂ τ, so an injective valuation of Q (order extension) lies in C_τ and factors through some Q_i.
- **Setup.** Let z be a reduced cycle of N_τ, supported on the finite vertex set J. Build Δ for J, and take D_k as in (H*). Put J' = J ∪ {i(k)}. For i ∈ J' set C_i = conv( ∪_{i(k)=i} D_k ∪ {e_σ : i ∈ σ} ), discarding empty ones.
- **The sets C_i.** Each C_i is compact, convex and contained in K_i. Together they cover Δ.
- **The nerve.** N(C) ⊂ N_τ(J') by property 2, and N(C) ⊇ N_τ(J) by the e_σ.
- **Conclusion.** By the nerve theorem for finite families of compact convex sets (Borsuk/Leray, cited from memory), N(C) ≃ Δ is contractible. So z bounds in N(C) ⊂ N_τ. Hence N_τ has vanishing reduced homology, and the augmented ordered cochain complex is exact, as in #15 Step 4.7. ∎

Note that Lemma K (finite subcovers) is **not** needed. Compactness of Δ replaces it.

**(H*) is automatic when every K_i is closed.** This happens when all witnesses can be taken real and embedded in R, which is the fine case of #15. In general it is not automatic, and it depends on the embedding, as the next example shows.

**Example 8 ((H*) fails for a bad embedding, inside the fine case N^2; proved).**
- Q = P = N^2, τ = P.
- Witnesses: v_0 = x1 + x2/2, placed in the *lower* class of H = R^2_lex, and v_1 = x2, placed in the *upper* class.
- Then for μ ∈ (0,1], w_μ is equivalent to the lexicographic valuation (x2, x1): x2 refined by v_0.
- Take the members Q_1 = sat(N^2 + N(e1 - e2)) and Q_3 = sat(N^2 + N(2e1 - e2) + N(2e2 - e1)). On the edge [v_0, v_1] they give K_1 = K_3 = {0}.
- Take Q_2 = sat(N^2 + N(e2 - e1)). It gives K_2 ⊃ (0,1], and K_2 does not contain 0.
- If no member of the cover factors both v_0 and (x2, x1), then (H*) fails near the vertex v_0. Yet with both witnesses embedded in R, all K_i are closed and (H*) holds.

So the convexification proof of #19 needs a **choice of witnesses and embedding that aligns leading classes**. In the fine case one can use real witnesses. For the Z^3 monoid of the task, every valuation in C_0 has the form (x3, w): x3 leads and the rest lives on Z e1 + Z e2. Aligning x3 in the top class reduces the picture to the real picture for N^2. I have not proved that an aligning choice exists in general. This is the remaining gap on the positive side.

## 4. Consequences for the refutation attempt

**What a counterexample must look like.** By Proposition 7, any counterexample has (H*) failing for *every* choice of witnesses and embeddings. By Lemma 6, the failure cannot happen inside one open face of Δ, where kernels are constant: there the loci K_i^b are open and cover. So it must happen across faces, where kernels shrink. Corollary 5 constrains such configurations:
- E^b loci are closed under coarsening, and under refinement with the same kernel.
- The candidate [0,1) ∪ [1,2] pattern along a segment with constant kernel is excluded outright, because the open face is connected and covered by open K^b's that sit inside the K's.

The pattern of Example 8 is an artefact of the embedding.

**The suggested candidates (heuristic checks, not proofs).**
- **P = {x3 > 0} ∪ {x3 = 0, x1, x2 ≥ 0} ⊂ Z^3.**
  - Every v ∈ C_0 is (x3, w), lexicographically, with w a valuation of Z^2 positive on N^2 \ 0.
  - Proved: for such v, M_v ∩ {x3 = 0} equals M_w computed for N^2. Indeed a witness y must satisfy y3 = 0, because v(y) ≺ v(x) forces y into the lower class, and then y ± x ∈ N^2.
  - So the birhizomic condition at points of C_0 only sees N^2-data. Aligning x3 in the top class makes the convexification for τ = 0 a copy of the real N^2 picture, where (H*) holds.
  - For the other principal faces, real witnesses exist: x3 lies in C_{N^2 face}. I found no disconnection.
- **P = V × N, V = Z^2_lex ∩ (≥ 0).**
  - Proved: a leading functional d_0 ≥ 0 on P has the form α a + γ c with α, γ ≥ 0.
  - C_0 fibres over the arc of these directions. The fibres are: a point (irrational interior), a half-circle of second-level directions (rational interior), C_0(N^2) (endpoint a), and the single point (a, b) (endpoint c). All are connected.
  - I found no disconnection.
- **Rank-2 P = Z^2 ∩ (non-closed cone).** C_0 is either an arc of real directions with refinements, or a single rank-2 point (the valuative case), or {x2} together with two refinements (the open half-plane). All are acyclic. In rank 2 no disconnection is possible.
- **Infinite rank.**
  - Sketched, not proved in detail: M_v = colim_S M_{v_S}. Hence E^b over P is the union of the pullbacks of the E^b over the fine P_S, by the compactness of f.p. objects. So the valuation space of P is the inverse limit of those of the P_S.
  - The obstruction noted in #17 remains: covers over P only cover the image of Val(P) in Val(P_S).

**Verdict.** I did not find a counterexample to #19. Every mechanism suggested in the task is blocked by Theorem 1, Corollaries 3 and 5, and Lemma 6. The blocking property is stated and proved as Lemma 4, Corollary 5 and Lemma 6. I could not complete a proof of #19 either; the gap is (H*).

## 5. Status

**Proved:**
- Theorem 1: the initial infinitesimal test object M_v.
- Corollary 2: the exact criterion for birhizomy, (E) plus (U').
- Corollary 3: the converse of R4 in every rank and for non-fine Q.
- Lemma 4 and Corollary 5: transport, and stability under coarsening and same-kernel refinement.
- Lemma 6: relative openness on open faces of a convexification.
- Proposition 7: #19 follows from (H*), with no Lemma K needed.
- Example 8: (H*) depends on the embedding.

**Cited from memory:**
- the description of f.p. objects as retracts;
- Hahn's embedding theorem;
- the nerve theorem for finite compact convex covers;
- the director's valuation form of N_τ, which relies on amalgamation of lifts.

**Heuristic:** the candidate analyses in §4 and the descent sketch.

**Open:**
- (Q1) Do witnesses and an embedding always exist for which (H*) holds? For instance, can one align leading classes using the inductive structure of C_τ, with leading functional in the closed dual cone and fibre C_0 of the face it cuts out?
- (Q2) Is #19 itself true? Neither a proof nor a counterexample is established. The evidence leans towards true.
- (Q3) Does the headline question hold for non-finitely-generated P? It is not settled here.

=== END OF ANSWER round4_q4 ===

