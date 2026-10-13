# round12_q10 answer

## 0. Summary and status

**(PE0) is not settled here.** I found neither a proof nor a counterexample. What this file does contain:

- **§1 (chain check).** The chain "variational principle → R11-a Theorem 3.1 → (PE0)" does derive the problem's claim from (PE0), modulo the theorems R11-a cites. No gap found.
- **§2 (Theorem A0, proved; no GH used).** A no-go result for the planner's Mechanism A in its "scale r → 0" form. Take any sequence of finite (or general) configurations whose supports shrink to a point of a Lyapunov block of μ. Suppose their weighted transports satisfy two-sided exponential bounds with uniform constants on time windows |t| ≤ T_n → ∞. Then every weak* limit is a distribution supported at one point, and it is **zero**. This holds in every smooth flow, GH or not. So Mechanism A cannot produce a nonzero two-sided decaying S by shrinking arrays. It has to work at a scale bounded below. There the compactness argument of R9-i turns approximate cycles into exact ones, so the mechanism is exactly the open statement (AC) of R9-i.
- **§3 (Theorem B0, proved; pure topological dynamics).** A no-go result for Mechanism B in its "soft" form. There is a minimal, uniquely ergodic subshift with positive entropy in which **every locally constant function is cohomologous to its mean through a continuous transfer function**. So every "regular" observable has bounded ergodic sums, zero asymptotic variance and spectral measure O(ξ²) at 0. Hence "positive entropy ⇒ some regular observable has spectral density bounded below near 0" is false at the level of topological/symbolic dynamics. Mechanism B would have to use the differentiable structure (exponential expansion linking fine and coarse scales), not only entropy plus regularity of observables.
- **§4.** What remains open, stated precisely.

Conventions are those of the brief: ν is a smooth positive density, d = div_ν X, J_t(x) = ∫_0^t d(g_s x) ds, Γ_t φ = e^{J_t}(φ∘g_t), and P = X + d, so that (d/dt)Γ_tφ = Γ_t Pφ.

---

## 1. Check of the chain (step C of the plan)

1. If h_top(g_1) > 0, the variational principle for the homeomorphism g_1 gives a g_1-invariant m with h_m(g_1) > 0. Jacobs' formula for its ergodic decomposition then gives a g_1-ergodic μ with h_μ(g_1) > 0. This is classical; it was re-checked in R9-a §3.
2. R11-a, Theorem 3.1: for such μ, λ := μ(J_1) = 0. It uses GH through Theorem J, together with [P], [LS] (with Lemma 6.0, which needs g_1-ergodicity, available here) and [NF].
3. (PE0) is stated for exactly this class: g_1-ergodic, h_μ(g_1) > 0, μ(J_1) = 0. It excludes μ, so h_top(g_1) = 0. By definition the flow's entropy is h_top(g_1). Dimension 1 is trivial.

So the chain does derive the problem's claim from (PE0), modulo the theorems R11-a cites ([P], [LS], [NF]; [NF] is the citation R11-a flags as not re-checked). I found no gap.

---

## 2. Theorem A0: shrinking configurations cannot give two-sided decay (proved; no GH)

The planner's Mechanism A (brief, "A SUGGESTION", item (1)) builds arrays S_r inside a Pesin block at scale r. It asks for bounds |S_r(Γ_tφ)| ≤ C e^{−ε|t|}‖φ‖_{C^k} on windows |t| ≤ T(r) → ∞, and then takes a nonzero normalised weak* limit S, to be killed by Theorem J. The result below shows that, **for any smooth vector field whatsoever**, such a limit is necessarily 0 whenever the arrays shrink to a point of a Lyapunov block. Theorem J (GH) is never needed to kill it, so the mechanism in this form cannot produce a contradiction with GH.

### 2.1 Setting: Lyapunov blocks

Let X be any smooth vector field on the compact manifold M (GH is not assumed in this section), and let μ be a g_1-invariant, g_1-ergodic Borel probability. Let χ_1 > … > χ_p be the distinct Lyapunov exponents of (Dg_1, μ), with multiplicities d_1, …, d_p, and put λ := μ(J_1). Fix bundle norms on TM (a Riemannian metric).

**Definition.** For ε > 0 and l ≥ 1, let K_{ε,l} be the set of x ∈ M for which there are subspaces E_1(x), …, E_p(x) with T_xM = E_1(x) ⊕ … ⊕ E_p(x) and dim E_i(x) = d_i, satisfying the following for all real t. Here E_i(g_t x) := Dg_t(x)E_i(x), and Π_i(g_t x) denotes the projection onto E_i(g_t x) along the other E_j(g_t x).
- (L1) For v ∈ E_i(x): l^{−1} e^{χ_i t − ε|t|}|v| ≤ |Dg_t(x)v| ≤ l e^{χ_i t + ε|t|}|v|.
- (L2) ‖Π_i(g_t x)‖ ≤ l e^{ε|t|} for every i.
- (L3) |J_t(x) − λt| ≤ l + ε|t|.

**Fact L (cited; standard).** For every ε > 0, μ(∪_l K_{ε,l}) = 1.

*Source and reduction (from memory).* Apply the Oseledets theorem to the invertible cocycle Dg_1 over g_1 (two-sided, so μ-a.e. point is Lyapunov–Perron regular). Combine it with the tempering-kernel lemma (Barreira–Pesin, *Nonuniform Hyperbolicity*, the theorem that a regular point satisfies, for every ε > 0, the two-sided estimates (L1)–(L2) at integer times with a constant l(x) < ∞). Pass from integer to real times using sup_{|s|≤1} ‖Dg_s^{±1}‖ < ∞, which only enlarges l. For (L3), Birkhoff's theorem for J_1 under g_1 and under g_{−1} gives J_n(x)/n → λ as n → ±∞ for a.e. x, and |J_t − J_{⌊t⌋}| ≤ ‖d‖_∞.

**Lemma A1 (proved).** K_{ε,l} is closed.

*Proof.* Let x_n ∈ K_{ε,l} with x_n → x, and choose splittings E_i(x_n) as in the definition. Grassmannians are compact, so after passing to a subsequence E_i(x_n) → E_i in Gr(d_i, TM).
- (L1) For each fixed t, (L1) passes to the limit: Dg_t is continuous, every v ∈ E_i is a limit of v_n ∈ E_i(x_n), and both bounds are closed conditions.
- (L3) For each fixed t, (L3) passes to the limit because J_t is continuous.
- (L2) For fixed t, the subspaces Dg_t(x_n)E_i(x_n) converge to Dg_t(x)E_i. The projections Π_i(g_t x_n) are uniformly bounded (by l e^{ε|t|}), so along a further subsequence they converge to linear maps Π_i with Π_iΠ_j = δ_{ij}Π_i, ΣΠ_i = Id, range Π_i = Dg_t(x)E_i and the same norm bound. Hence Dg_t(x)E_1 ⊕ … ⊕ Dg_t(x)E_p is a direct sum equal to T_{g_t x}M, and its projections are the Π_i.

Taking t = 0 shows that the E_i span T_xM directly. ∎

### 2.2 The jet cocycle

For y ∈ M let J^k_y be the space of k-jets of smooth functions at y. For y ∈ M and real t define

 A_t(y): J^k_{g_t y} → J^k_y,  A_t(y)(j^k_{g_t y}φ) := j^k_y(Γ_tφ) = j^k_y(e^{J_t}·φ∘g_t).

- *Well defined.* By the chain and Leibniz rules, the k-jet of e^{J_t}·(φ∘g_t) at y depends only on the k-jet of φ at g_t y.
- *Cocycle.* Γ_{t+s} = Γ_sΓ_t, because e^{J_{t+s}(x)} = e^{J_s(x)}e^{J_t(g_s x)}. Hence A_{t+s}(y) = A_s(y)A_t(g_s y).
- *Invertible.* Γ_tΓ_{−t} = Id, because J_t(x) + J_{−t}(g_t x) = 0.

### 2.3 Theorem A0

**Theorem A0 (proved, given Fact L only for the remark after it).** Let k ≥ 0, ε_0 > 0 and ε > 0 with (4k+1)ε < ε_0, and let x* ∈ K_{ε,l}. Let S be a distribution (a continuous linear functional on C^∞(M)) of order ≤ k with supp S ⊂ {x*}. Suppose there is a constant C such that

 |S(Γ_tφ)| ≤ C e^{−ε_0|t|}‖φ‖_{C^k}  for all real t and all smooth φ.  (A.1)

Then S = 0.

*Proof.*

**Step 1 (S is a jet functional).** A distribution of order ≤ k supported at one point is a finite combination of derivatives of order ≤ k of the Dirac mass (Schwartz). So S(φ) = ℓ(j^k_{x*}φ) for a linear functional ℓ on J^k_{x*}. Then

 S(Γ_tφ) = ℓ(A_t(x*) j^k_{g_t x*}φ) = ℓ_t(j^k_{g_t x*}φ),  where ℓ_t := ℓ∘A_t(x*) ∈ (J^k_{g_t x*})^*.

**Step 2 (from test functions to jets).** Fix a smooth bundle norm on J^k and the dual norm on (J^k)^*. There is c > 0 such that for every y ∈ M and every ξ ∈ (J^k_y)^*,

 sup{ |ξ(j^k_yφ)| : ‖φ‖_{C^k} ≤ 1 } ≥ c|ξ|.

Indeed, by compactness there is C_1 such that every a ∈ J^k_y is the jet of some φ_a with ‖φ_a‖_{C^k} ≤ C_1|a|: take a polynomial in coordinates of one of finitely many charts, times a fixed cutoff. Then the sup is ≥ |ξ(a)|/(C_1|a|) for every a ≠ 0. With (A.1) this gives

 |ℓ_t| ≤ (C/c) e^{−ε_0|t|} for all real t.  (A.2)

**Step 3 (filtration by order).** For 0 ≤ m ≤ k let V_m(y) ⊂ (J^k_y)^* consist of the functionals that vanish on every jet whose m-jet is zero. Put V_{−1} := 0, so 0 = V_{−1} ⊂ V_0 ⊂ … ⊂ V_k = (J^k_y)^*.
- *Invariance.* If ℓ ∈ V_m(x*), then ℓ_t ∈ V_m(g_t x*). Indeed, if φ has zero m-jet at g_t x*, then Γ_tφ has zero m-jet at x*.
- *The quotient.* V_m/V_{m−1} is canonically Sym^m T_y. A class is determined by its values on functions with zero (m−1)-jet at y, and these values are determined by D^mφ(y) ∈ Sym^m T^*_y.
- *The induced action.* For φ with zero (m−1)-jet at g_t y,
 D^m(Γ_tφ)(y) = e^{J_t(y)} D^mφ(g_t y)[Dg_t(y)·, …, Dg_t(y)·].
 Every other term of the chain and Leibniz rules contains a derivative of φ of order < m at g_t y, and those vanish. So if ℓ ∈ V_m(x*) has class w ∈ Sym^m T_{x*}, then ℓ_t ∈ V_m(g_t x*) has class
 w_t := e^{J_t(x*)} Sym^m(Dg_t(x*)) w ∈ Sym^m T_{g_t x*}.
- *Quotient norms.* Quotient norms are bounded by C_2 times the norms. By (A.2), |w_t| ≤ C_3 e^{−ε_0|t|} for all t.

**Step 4 (lower bounds on symmetric powers).** Fix y = g_t x* and put q := l e^{ε|t|}, so ‖Π_i(y)‖ ≤ q by (L2). Define on T_y the auxiliary inner product ⟨u, v⟩' := Σ_i ⟨Π_i u, Π_i v⟩.
- *Comparison with the original norm.* |u|' ≤ √p q|u| and |u| ≤ Σ_i|Π_i u| ≤ √p|u|'. On each E_i(y), |·|' = |·|.
- *Orthogonality.* The splitting is |·|'-orthogonal. Hence, in the induced inner product on T_y^{⊗m}, the subspaces E_{i_1}⊗…⊗E_{i_m} are mutually orthogonal.
- *The pieces E_I.* For a multiset I = {i_1, …, i_m} let E_I(y) ⊂ Sym^m T_y be the symmetric tensors in W_I := ⊕_σ E_{i_{σ(1)}}⊗…⊗E_{i_{σ(m)}}. Then Sym^m T_y = ⊕_I E_I(y) orthogonally for |·|', and the |·|'-orthogonal projections onto E_I have original-norm operator norm ≤ (√p q)^{2m}.
- *Lower bound.* Dg_t(x*) maps E_i(x*) onto E_i(g_t x*), so Dg_t^{⊗m} maps W_I(x*) onto W_I(g_t x*). On each tensor piece its smallest singular value, in the primed norms, is ≥ the product of the smallest singular values of Dg_t on the factors. By (L1) that product is ≥ l^{−m} e^{χ_I t − mε|t|}, where χ_I := χ_{i_1} + … + χ_{i_m}. The pieces are orthogonal and the product is the same for every ordering, so the bound holds on W_I and hence on E_I. Converting to the original norms at x* (q = l) and at g_t x* (q = l e^{ε|t|}) gives, for w ∈ E_I(x*),
 |Sym^m(Dg_t(x*)) w| ≥ c_4 e^{χ_I t − 2mε|t|} |w|,  with c_4 = c_4(l, p, m) > 0.

**Step 5 (conclusion).** Suppose ℓ ≠ 0, and let m ∈ {0, …, k} be least with ℓ ∈ V_m(x*). Its class w ∈ Sym^m T_{x*} is nonzero. (For m = 0, Sym^0 = R, w is a nonzero number, and χ_I := 0.) Write w = Σ_I w_I with w_I ∈ E_I(x*), and pick I with w_I ≠ 0.

The pieces are invariant, so the E_I-component of w_t is e^{J_t(x*)} Sym^m(Dg_t)w_I. Using the projection bound, Step 3, Step 4 and (L3) (which gives e^{J_t(x*)} ≥ e^{−l} e^{λt − ε|t|}):

 c_4 e^{−l} e^{(λ+χ_I)t − (2m+1)ε|t|} |w_I| ≤ (√p l)^{2m} e^{2mε|t|} C_3 e^{−ε_0|t|},

that is, e^{(λ+χ_I)t} ≤ C_5 e^{−(ε_0 − (4m+1)ε)|t|} for all real t. Since (4m+1)ε ≤ (4k+1)ε < ε_0:
- letting t → +∞ gives λ + χ_I < 0;
- letting t → −∞ gives λ + χ_I > 0.

This is a contradiction, so ℓ = 0 and S = 0. ∎

*Remark.* This is the statement "a vector of a Lyapunov-regular finite-dimensional cocycle cannot decay in both time directions", applied to the dual k-jet cocycle. The only work is to make it uniform on the closed set K_{ε,l}, which is what lets one pass to limits below.

### 2.4 Consequence for Mechanism A

**Corollary A1 (proved).** Let k, ε_0, ε, l be as in Theorem A0, and let K = K_{ε,l}. Let S_n be distributions with supp S_n ⊂ B(x_n, r_n), x_n ∈ K and r_n → 0. Suppose:
- (i) there are C and T_n → ∞ with |S_n(Γ_tφ)| ≤ C e^{−ε_0|t|}‖φ‖_{C^k} for |t| ≤ T_n and all smooth φ;
- (ii) S_n(φ) → S(φ) for every smooth φ.

Then S = 0.

*Proof.* Pass to a subsequence with x_n → x*; then x* ∈ K by Lemma A1.
- *Support.* If φ vanishes on a neighbourhood of x*, then S_n(φ) = 0 for large n. So supp S ⊂ {x*}.
- *Order.* (i) at t = 0 gives |S(φ)| ≤ C‖φ‖_{C^k}, so S has order ≤ k.
- *Decay.* For fixed t, Γ_tφ is smooth, so S(Γ_tφ) = lim S_n(Γ_tφ), and the bound of (i) holds as soon as T_n ≥ |t|. So S satisfies (A.1).

Theorem A0 gives S = 0. ∎

**What this says about the planner's sketch (1).** Normalise the arrays S_r in any way, say S_r/‖S_r‖. Suppose the arrays shrink to points of a Lyapunov block, and the normalised arrays satisfy two-sided bounds with a uniform constant on windows |t| ≤ T(r) → ∞. Then their weak* limits are 0. The "nonzero density with two-sided exponential decay" therefore never materialises, **in any smooth flow, GH or not**: if such limits existed they would contradict Theorem A0, not GH.

By Fact L, every μ-typical base point lies in some K_{ε,l} for every ε > 0. So this applies to arrays at μ-typical points, whatever the block constant l. (In the planner's sketch ε_0 is the decay rate of the arrays; it is fixed first, and then ε < ε_0/(4k+1) is chosen.)

The same scale analysis explains concretely what goes wrong. Take arrays with stable spread ρ and unstable spread r and leaf moments of orders j, j'. Exploiting both cancellations at once forward needs jθ ≥ j'Λ^u, and backward needs j'θ ≥ jΛ^s. Here θ < χ^+_min is the cancellation rate and Λ^u, Λ^s are the largest expansion rates forward and backward. Together these force θ² ≥ Λ^uΛ^s, which is impossible. This is a heuristic; Theorem A0 is the rigorous form.

**Remark A2 (what is not covered).**
- (a) *Arrays of diameter bounded below.* Their limits are finite sums of jets at finitely many distinct points, or exact finite configurations. Along R11-b (Lemma N and the remark after it), forward and backward cancellation between such points forces exact (time-shifted) stable/unstable asymptotic relations. This is precisely the closing problem (AC) of R9-i, which the compactness principle of R9-i (Prop. 3.2) reduces to. I did not write out the jet version of Lemma N.
- (b) *Configurations whose number of points grows while the diameter stays fixed.* These may converge to non-point-supported limits such as densities, as in Proposition MG of R8-f. They are not covered.

So Mechanism A can only live at a positive scale. There it is (AC), or the measured version of R8-f.

---

## 3. Theorem B0: positive entropy does not force a regular observable to have nonzero variance (proved; symbolic)

Mechanism B (brief, item (2)) conjectures that positive entropy yields a smooth f whose spectral density near frequency 0 is bounded below, contradicting the infinite-order flatness that GH gives in the volume case (R7-b Prop. 3.1, R11-c). The following example shows that the soft version of this principle is false. In a positive-entropy uniquely ergodic minimal system, every locally constant observable can be a continuous coboundary up to its mean.

### 3.1 Construction

Words are over {0, 1}. Put N_0 = 2, L_0 = 1, W_0 = {B_0^1, B_0^2} = {0, 1}.

Suppose W_k = {B_k^1, …, B_k^{N_k}} has been built: N_k ≥ 2 distinct words of length L_k. Choose an integer m_k ≥ 2 (fixed in §3.3).
- *The graph.* Let H_k be the directed multigraph on the vertex set {1, …, N_k} with exactly m_k parallel edges a → b for every ordered pair (a, b), loops included. Fix one copy e*_k of an edge N_k → 1, and let G_k := H_k − e*_k.
- *Degrees.* In H_k every vertex has in-degree = out-degree = m_kN_k. In G_k, vertex 1 has out − in = 1, vertex N_k has in − out = 1, and all other vertices are balanced. Since N_k ≥ 2 and G_k is connected, G_k has Eulerian trails, and each starts at 1 and ends at N_k.
- *Vertex sequences.* Such a trail has E_k := m_kN_k² − 1 edges and a vertex sequence (i_0, …, i_{E_k}) with i_0 = 1 and i_{E_k} = N_k.
- *The next level.* W_{k+1} is the set of words B_k^{i_0}B_k^{i_1}⋯B_k^{i_{E_k}}, one for each distinct vertex sequence of an Eulerian trail of G_k. Then L_{k+1} = m_kN_k²L_k, and N_{k+1} := #W_{k+1}. Distinct vertex sequences give distinct words, because the B_k^a are distinct words of the same length.

Properties, immediate from the construction:
- (P1) Every word of W_{k+1} begins with B_k^1 and ends with B_k^{N_k}.
- (P2) In the vertex sequence of any element of W_{k+1}, the consecutive pairs (i_s, i_{s+1}), 0 ≤ s < E_k, run through the edges of G_k. Add the "wrap-around" pair (i_{E_k}, 1) = (N_k, 1). Then **every ordered pair (a, b) occurs exactly m_k times**.
- (P3) Every vertex has outgoing edges, so every element of W_{k+1} contains every element of W_k as one of its level-k sub-blocks. Elements of W_{k+1} are concatenations of elements of W_j aligned at multiples of L_j, for every j ≤ k+1.

Let X ⊂ {0,1}^Z be the set of sequences all of whose finite subwords are subwords of elements of ∪_k W_k, and let σ be the shift.
- X is closed and σ-invariant.
- X is nonempty. Each vertex occurs m_kN_k ≥ 4 times in a vertex sequence, so a level-k block w_k can be placed at an interior sub-block position of some w_{k+1} ∈ W_{k+1}, with at least L_k symbols on each side. Iterating gives a nested sequence of words whose margins tend to infinity on both sides; its limit lies in X.

### 3.2 Lemmas

**Lemma B1 (cutting; proved).** For every x ∈ X and k ≥ 0 there is p ∈ Z such that x[p + iL_k, p + (i+1)L_k) ∈ W_k for every i ∈ Z.

*Proof.* For each n, the window x[−n, n) is a subword of some element of W_K, and by (P3) we may take K ≥ k. That element is a concatenation of level-k blocks aligned at multiples of L_k. So there is a phase q_n ∈ {0, …, L_k − 1} such that every length-L_k subword of x[−n, n) that starts at a position ≡ q_n (mod L_k) and lies inside the window belongs to W_k. Some phase q occurs for infinitely many n; take p = q. ∎

**Lemma B2 (equal block sums; proved).** Let 1 ≤ ℓ ≤ L_k, F: {0,1}^ℓ → R, and f(x) := F(x_0 … x_{ℓ−1}). Put

 Φ(a, b) := Σ_{q=0}^{L_k−1} F((B_k^a B_k^b)[q, q+ℓ)),  Q_k(F) := m_k Σ_{a,b=1}^{N_k} Φ(a, b).

Let x ∈ X, and let p be a level-(k+1) cutting phase of x (Lemma B1). Then for every i ∈ Z, with P := p + iL_{k+1},

 Σ_{n=P}^{P+L_{k+1}−1} f(σ^n x) = Q_k(F).

*Proof.* Write x[P, P+L_{k+1}) = B_k^{i_0}⋯B_k^{i_E}. The next level-(k+1) block of x begins with B_k^1 by (P1); put i_{E+1} := 1. For n = P + sL_k + q with 0 ≤ s ≤ E and 0 ≤ q < L_k, the window x[n, n+ℓ) lies inside the s-th and (s+1)-th level-k sub-blocks, because q + ℓ < 2L_k. So f(σ^n x) = F((B_k^{i_s}B_k^{i_{s+1}})[q, q+ℓ)). Summing over q and s gives Σ_{s=0}^{E} Φ(i_s, i_{s+1}). By (P2), with the wrap-around pair, every ordered pair occurs exactly m_k times, so the sum is Q_k(F). ∎

### 3.3 The theorem

**Theorem B0 (proved, modulo the cited Gottschalk–Hedlund and BEST theorems).** For a suitable choice of the m_k, the subshift (X, σ) has the following properties.
- (i) It is minimal.
- (ii) It is uniquely ergodic, with invariant measure μ.
- (iii) h_top(X) = h_μ(σ) ≥ (log 2)/2 > 0.
- (iv) For every k, every 1 ≤ ℓ ≤ L_k, every F: {0,1}^ℓ → R and f(x) = F(x_0 … x_{ℓ−1}):
 sup_{x ∈ X, n ≥ 1} |S_n f(x) − nμ(f)| ≤ 4L_{k+1}‖F‖_∞.
 Hence f − μ(f) = v∘σ − v with v ∈ C(X) and ‖v‖_∞ ≤ 4L_{k+1}‖F‖_∞.

Consequently every locally constant real f ∈ L²(μ) has bounded ergodic sums and asymptotic variance lim ‖S_n(f − μf)‖²_2/n = 0. Its spectral measure satisfies σ_{f−μf} = |e^{iξ} − 1|² σ_v, so σ_{f−μf}([−η, η]) ≤ η²‖v‖²_2. In particular no locally constant observable has spectral density bounded below near 0.

*Proof.*

(iv) and (ii). Let x ∈ X and n ≥ 1, and cut x at level k+1 (Lemma B1).
- *Block decomposition.* The complete level-(k+1) blocks inside [0, n) are consecutive, say q of them. The rest of [0, n) consists of at most two intervals, each of length < L_{k+1}.
- *Bound.* By Lemma B2, |S_n f(x) − qQ_k(F)| ≤ 2L_{k+1}‖F‖_∞, and 0 ≤ n − qL_{k+1} < 2L_{k+1}.
- *Unique ergodicity.* Hence (1/n)S_n f → Q_k(F)/L_{k+1} uniformly on X. Integrating against any invariant probability ν gives ν(f) = Q_k(F)/L_{k+1}. Locally constant functions are dense in C(X), so the invariant probability is unique; call it μ.
- *Discrepancy.* Then |S_n f(x) − nμ(f)| ≤ 2L_{k+1}‖F‖_∞ + |Q_k(F)|·|q − n/L_{k+1}| ≤ 4L_{k+1}‖F‖_∞, using |Q_k(F)| ≤ L_{k+1}‖F‖_∞.
- *Coboundary.* By Gottschalk–Hedlund (cited: for a minimal homeomorphism of a compact metric space and g ∈ C(X) with sup_n |S_n g(x_0)| < ∞ for some x_0, g = v∘σ − v with v continuous; the proof defines v on the orbit of x_0 by v(σ^n x_0) = S_n g(x_0) and extends it, so ‖v‖_∞ ≤ sup_{x,n}|S_n g(x)|), applied with g = f − μ(f) and using (i), we get v with ‖v‖_∞ ≤ 4L_{k+1}‖F‖_∞.

(i). Let w be a word occurring in X. Then w occurs in some level-j block, and hence by (P3) in every level-(j+1) block. Every x ∈ X is a concatenation of level-(j+1) blocks (Lemma B1), so w occurs in every window of x of length 2L_{j+1}. So every orbit is dense.

(iii). *Counting.* BEST theorem (cited; de Bruijn–van Aardenne-Ehrenfest–Smith–Tutte): in a connected Eulerian directed multigraph H with distinguishable edges, the number of Eulerian circuits beginning with a fixed edge e equals t(H)∏_v (deg^+(v) − 1)!, where t(H) ≥ 1 is the number of spanning arborescences towards a fixed vertex.
- Apply it to H_k with e = e*_k. Deleting e*_k from such a circuit gives an Eulerian trail of G_k from 1 to N_k, bijectively.
- Two labelled trails with the same vertex sequence differ by permuting labels within classes of parallel edges, so each vertex sequence arises from at most (m_k!)^{N_k²} labelled trails.
- Hence, with N = N_k and m = m_k,
 N_{k+1} ≥ ((mN − 1)!)^N / (m!)^{N²}.

*Estimating.* Use (mN−1)! = (mN)!/(mN) with (mN)! ≥ (mN/e)^{mN}, and m! ≤ e·m^{m+1/2}e^{−m}, so log m! ≤ m log m − m + log m + 1. Then
 log N_{k+1} ≥ N(mN log(mN) − mN − log(mN)) − N²(m log m − m + log m + 1) = mN² log N − N log(mN) − N²(log m + 1).
Dividing by L_{k+1} = mN²L_k gives
 (log N_{k+1})/L_{k+1} ≥ (log N_k)/L_k − δ_k,  δ_k := [log(m_kN_k)/(m_kN_k) + (log m_k + 1)/m_k]/L_k.

*Choice of m_k.* At stage k, N_k and L_k are already fixed and δ_k → 0 as m_k → ∞. So choose m_k with δ_k ≤ (log 2)2^{−k−2}. Then (log N_k)/L_k ≥ log 2 − Σ_k δ_k ≥ (log 2)/2 for all k. In particular N_{k+1} ≥ 2, so the construction continues.

*Entropy.* Every element of W_k occurs in X: every x contains a level-(k+1) block, and that block contains all level-k blocks. So the number p_X(L_k) of words of length L_k in X is ≥ N_k. Hence h_top(X) = lim_n (1/n) log p_X(n) ≥ limsup_k (log N_k)/L_k ≥ (log 2)/2. By unique ergodicity and the variational principle, h_μ = h_top > 0.

*Spectral statement.* If f − μ(f) = v∘σ − v with v ∈ L², then for the Koopman operator U, f − μ(f) = (U − I)v, so dσ_{f−μf} = |e^{iξ} − 1|² dσ_v. Bounded S_n gives zero asymptotic variance. ∎

### 3.4 What Theorem B0 does and does not show

- **It shows:** positive entropy (even with minimality and unique ergodicity) does not force any locally constant observable, the most regular observables available, to have positive Green–Kubo variance or a spectral density bounded below at 0. So the conjecture in the brief's Mechanism B cannot follow from "entropy along unstable leaves" in a soft way. The symbolic system has all the C^0-level features that GH gives in the volume case: unique ergodicity, minimality, and bounded ergodic integrals with transfer functions bounded in terms of the observable (R7-d Lemmas C and F). A proof along Mechanism B must use the differentiable structure.
- **It does not show** that such behaviour is compatible with GH, or even with smoothness.
  - The constant 4L_{k+1} grows doubly exponentially in the window length ℓ: L_{k+1} ≥ N_k² ≈ e^{2hL_k}, and a window of length just above L_{k−1} already needs level k+1.
  - In a smooth system the GH tame bound ‖u‖_{C^0} ≤ C‖f‖_{C^m} gives a bound polynomial in 1/ε for an observable at spatial resolution ε. That is only single-exponential in a symbolic window length ℓ ≈ log(1/ε)/χ.
  - So the example violates the analogue of the tame bound. I expect (sketch only, not checked) that a "method of types" variant can give single-exponential bounds: require all level-(k+1) blocks to have identical ℓ_{k+1}-subword statistics with ℓ_{k+1} ≈ c log L_{k+1}, and let the L_k grow geometrically. That would make even the quantitative C^0 consequences of GH compatible with positive entropy at the symbolic level.
  - I have also not checked infinite-order divisibility (whether v − μ(v) is again a coboundary, and so on), which is the full analogue of GH-flatness.

---

## 4. What is proved, what is not, and the open questions

**Proved in this file.**
1. §1: the chain "variational principle + R11-a Theorem 3.1 + (PE0) ⇒ h_top(g_1) = 0" is valid, modulo the theorems R11-a cites.
2. §2, Theorem A0 and Corollary A1. This needs no GH; it uses only the closedness of Lyapunov blocks, proved as Lemma A1. Fact L (that Lyapunov blocks have full measure, from Oseledets plus tempering) is cited and is used only to say that typical points lie in blocks.
   - Theorem A0: no nonzero distribution supported at a point of a Lyapunov block has two-sided exponentially decaying weighted transport.
   - Corollary A1: any weak* limit of configurations shrinking into a block, with uniform two-sided bounds on growing time windows, is 0.
   - Consequence: the planner's Mechanism A, in its shrinking-array form, cannot yield a nonzero S in any smooth flow. It must operate at a scale bounded below, where it is (AC) of R9-i, or its measured form, Proposition MG of R8-f.
3. §3, Theorem B0, modulo the classical Gottschalk–Hedlund and BEST theorems: a minimal, uniquely ergodic, positive-entropy subshift in which every locally constant function is a continuous coboundary up to its mean. Consequence: the soft form of Mechanism B is false. It needs differentiable structure.

**Sketched only.**
- The scale-mismatch heuristic θ² ≥ Λ^uΛ^s in §2.4.
- The single-exponential "method of types" refinement of Theorem B0 in §3.4.

**Not achieved: (PE0) itself.** I could not prove it and found no counterexample. Neither result above is a proof of (PE0) for a subclass. They are barrier results: each closes one proposed route and pins down what a successful route must use.

**Open questions (explicit).**
- (O-1) **(PE0)**, unchanged: under GH, no g_1-ergodic μ with h_μ(g_1) > 0 and μ(J_1) = 0.
- (O-2) **(AC)** of R9-i, in the volume case. For a Pesin block of a positive-entropy volume (necessarily non-hyperbolic), are there two distinct non-degenerate good su-chains of equal length from one point with u-equivalent endpoints, i.e. a closed su-cycle through good points? By Corollary A1, this fixed-scale closing statement is the only form in which finite-configuration mechanisms can work. By R8-f/R9-i it would settle the volume case of (PE0).
- (O-3) A **jet version of Lemma N** (R11-b): if a finite sum of jets at points of finitely many orbits has two-sided decaying transport, must the orbits be pairwise exponentially asymptotic up to time shifts, along stable and unstable classes? Theorem A0 is the one-point case. A positive answer would make the reduction of Mechanism A to (AC) a theorem rather than a remark (Remark A2(a)).
- (O-4) For Mechanism B: in a C^∞ flow with a smooth invariant volume and positive entropy, is there always a smooth observable with nonzero Green–Kubo variance, or at least one whose spectral measure is not flat at 0? Theorem B0 shows that any proof must use the smooth structure, e.g. the Pesin unstable geometry linking fine and coarse scales. Whether the single-exponential refinement of Theorem B0 (§3.4) holds would decide whether even the quantitative C^0 consequences of GH are compatible with positive entropy at the symbolic level.

=== END OF ANSWER round12_q10 ===
