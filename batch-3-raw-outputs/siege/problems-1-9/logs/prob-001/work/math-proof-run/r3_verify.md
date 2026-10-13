The document below is a draft proof. Check the argument step by step: for every inequality, interchange, cited result, and 'it follows that', ask whether it actually follows as written. List every error or gap in order of severity, and say explicitly whether the main claim is proved.

## The draft proof

# Answer: YES, for every monoid P

**Main Theorem.** Let P be a monoid (integral, saturated, sharp, commutative; P is *not* assumed finitely generated). For every presheaf of abelian groups F on B_P^op, the morphism F → Rπ_*π^{-1}F is a quasi-isomorphism. More precisely:
- the unit F → π_*π^{-1}F is an isomorphism;
- R^pπ_*π^{-1}F = 0 for p > 0.

The proof never uses the infinitesimality condition in the definition of "birhizomic". It uses only two properties of a birhizomic cover. Every valuation of the base factors through some member at which the member is birhizomic, and such members are of finite presentation.

**Outline.**
- §1 Conventions and elementary facts: the category, filtered colimits, finite presentation, the objects P[−x]^♯, the site.
- §2 Theorem B: for every f.p. map P → Q, the kernel face f^{-1}(0) is principal.
- §3 Theorem D (the nerve theorem): Čech nerves of coverings are acyclic, for arbitrary P.
- §4 The sheaf-theoretic part: Kan extension, injectives, Čech complexes, sheafification, Cartan's criterion, and the conclusion.
- §5 Other routes worth recording.
- §6 Status and what is quoted.

---

## §1 Conventions and elementary facts

**1.0 Notation.**
- 𝒞 is the category of integral, saturated, sharp commutative monoids ("monoids").
- For a monoid B, B/𝒞 is the category of maps B → M in 𝒞. Its morphisms are the maps under B, and Hom_B(M, N) denotes its Hom-sets.
- For f : P → Q, write Φ_Q := f^{-1}(0).
- For x ∈ P, face(x) := {y ∈ P : y ≤ nx for some n ≥ 1}. Here y ≤ z means z − y ∈ P.
- A *face* of P is a submonoid F with a + b ∈ F ⇒ a, b ∈ F. A face is *principal* if it equals face(x) for some x.
- **Size.** Fix universes U ∈ V with P ∈ U. A_P consists of the maps P → Q with Q ∈ U, and presheaves take values in V-small groups. The usual theory (plus construction, enough injectives, derived functors) then applies to the V-small site A_P^op. Nothing below depends on this choice.

**1.1 Torsion-freeness (F4).** For M ∈ 𝒞, M^gp is torsion-free. If nx = 0 then nx ∈ M, so x ∈ M by saturation; likewise −x ∈ M, so x = 0 by sharpness. Consequently nx = ny ⇒ x = y, and M ⊂ M^gp ⊂ M^gp ⊗ Q.

**1.2 Filtered colimits (F1).** A filtered colimit of objects of 𝒞, computed in commutative monoids, lies in 𝒞. Each axiom is witnessed at a finite stage:
- a + c = b + c in the colimit already holds at some stage, so a = b there;
- nx = m (with x in the group) already holds at some stage;
- x + y = 0 already holds at some stage.

So filtered colimits in 𝒞 and in B/𝒞 are computed on underlying sets.

**1.3 The int/sat/sharp reflection and pushouts.** Let N be a commutative monoid and E ⊂ N × N a set of relations. Form the quotient monoid N/E and let G be its group completion. Let M_0 be the image of N/E in G, let M_1 = {g ∈ G : ng ∈ M_0 for some n ≥ 1}, and put T = M_1/M_1^*.
- T ∈ 𝒞. It is integral as a submonoid of G/M_1^*, and it is sharp. It is saturated: if ng ∈ T for g ∈ G/M_1^*, then a lift g̃ has n g̃ ∈ M_1, so g̃ ∈ M_1.
- Every map N → X with X ∈ 𝒞 that respects E factors uniquely through T. It extends to G → X^gp. It sends M_1 into X, because X is saturated and X^gp is torsion-free. It kills M_1^*, because X is sharp.

We write T = (N/E)^{int,sat,sharp}. Pushouts in 𝒞 are formed this way from pushouts of commutative monoids. Fibre products in A_P^op are pushouts under P.

**1.4 Finite presentation.** A map B → M in 𝒞 is *f.p.* if Hom_B(M, −) commutes with filtered colimits in B/𝒞. This is the problem's "of finite presentation in the category of monoids".

**Lemma 1.5.**
- (a) Composites of f.p. maps are f.p.
- (b) If Q → Q' is f.p. and Q → R is arbitrary, then R → Q' ⊔_Q R is f.p.
- (c) Each P → P[−x]^♯ is f.p.

Hence every finite iterated pushout over Q of f.p. maps Q → Q_i, with Q f.p. under P, is f.p. under P.

*Proof.*
- (b) Hom_R(Q' ⊔_Q R, X) = Hom_Q(Q', X), and a filtered colimit under R is also one under Q.
- (a) Let P → Q → Q' be f.p. and X = colim X_k under P. A map Q' → X under P is a pair (a, c): a map a : Q → X under P, and a map c : Q' → X under Q, where X is viewed under Q via a.
  - a factors through some X_k, uniquely up to going further along.
  - The X_{k'} with k' ≥ k, viewed under Q, have colimit X, so c factors through some X_{k'}, again uniquely up to going further.
  - Hence colim_k Hom_P(Q', X_k) → Hom_P(Q', X) is bijective.
- (c) follows from 1.6: Hom_P(P[−x]^♯, X) is a point if x ↦ 0 in X and empty otherwise. In a filtered colimit, x ↦ 0 holds iff it holds at some stage (1.2). ∎

**1.6 The objects b_x = (P → P[−x]^♯).**
- *Construction.* P[−x] := {p − nx : p ∈ P, n ≥ 0} ⊂ P^gp. It is integral, and it is saturated: if m(g) ∈ P[−x], then m(g + kx) ∈ P for some k, so g + kx ∈ P. P[−x]^♯ := P[−x]/P[−x]^*, which is in 𝒞.
- *Universal property.* For f : P → Q in A_P, a map P[−x]^♯ → Q under P exists iff f(x) = 0, and it is then unique. If f(x) = 0, f extends uniquely to P[−x], which is generated by P and −x, and the extension kills units because Q is sharp. Conversely, x is a unit in P[−x], so it maps to 0 in P[−x]^♯.
- *Kernel.* Φ_{b_x} = face(x). Indeed y ↦ 0 iff y is a unit of P[−x], iff −y = p − nx for some p, n, iff y + p = nx, iff y ≤ nx.
- *Kernel faces in general.* For any f : P → Q, Φ_Q is a face, since f(a) + f(b) = 0 forces f(a) = f(b) = 0 in sharp Q. A map Q → Q' under P gives Φ_Q ⊂ Φ_{Q'}. Also x ∈ Φ_Q iff face(x) ⊂ Φ_Q.
- *Consequences.*
  - Hom_{A_P}(b_x, b_y) is a point if face(x) ⊂ face(y), and empty otherwise.
  - So B_P is a preorder, equivalent to the poset Pr(P) of principal faces.
  - Pr(P) is directed, since face(x), face(y) ⊂ face(x + y), and has least element face(0) = {0}, with b_0 = P.
  - For τ ∈ Pr(P), write b_τ for any b_x with face(x) = τ, and F(τ) := F(b_τ).

**1.7 Lemma (retract of a finite presentation).** Let B ∈ 𝒞 and let B → M be f.p. Then there are a finite set S and a finite set R of relations in B ⊕ N^S such that M is a retract under B of T := ((B ⊕ N^S)/R)^{int,sat,sharp}. Note that T is this object itself, not its image in M.

*Proof.* Consider pairs (S, R): S ⊂ M finite, and R a finite set of pairs (a, b) of elements of B ⊕ N^S having the same image in M under the obvious map. These pairs are directed by inclusion. Let T(S,R) be the reflection (1.3). Then T(S,R) → M exists, and so do the transition maps. Let L = colim T(S,R) (1.2).
- L → M is surjective: m ∈ M is the image of the generator of T({m}, ∅).
- L → M is injective. Let x, y lie in a common T(S,R) and have the same image in M. By construction of the reflection there is n ≥ 1 with nx = [a] and ny = [b], for some a, b ∈ B ⊕ N^S. Then (a, b) has equal images in M. In T(S, R ∪ {(a,b)}) we get nx = ny, hence x = y by 1.1.

So M = colim T(S,R) in B/𝒞. Since M is f.p., id_M factors through some T = T(S,R): there is s : M → T under B whose composite with T → M is id_M. ∎

**1.8 The site.**
- *Covers of an object.* For an object Q of A_P, a *birhizomic cover of Q* is a family {a_i : Q → Q_i} of maps under P that is a birhizomic cover in the sense of the problem, with Q as base. (A map under P out of Q is just a map out of Q.)
- *Witness set.* I_0 = {i : there are a valuative V and g : Q_i → V such that a_i is birhizomic at g}. By definition of "birhizomic at", every a_i with i ∈ I_0 is f.p.

**Lemma 1.9 (pretopology axioms).** Birhizomic covers satisfy the following:
- isomorphisms are covers;
- base change: if {a_i : Q → Q_i} is a cover and c : Q → Q', then {Q' → Q'_i := Q' ⊔_Q Q_i} is a cover;
- composition: if {a_i : Q → Q_i} is a cover and each {b_ij : Q_i → Q_ij} is a cover, then {b_ij a_i} is a cover.

*Proof.*
- *Isomorphisms.* Let φ : Q → Q' be an isomorphism and v a valuation of Q. Then v = (vφ^{-1})φ, and φ is f.p. Given h : Q → M and an infinitesimal p : M → V with ph = v, the map u = hφ^{-1} is the unique one with uφ = h, and pu = vφ^{-1}.
- *Base change.* Let v' be a valuation of Q'. Then v'c = g_i a_i with a_i birhizomic at g_i. Put g' = (v', g_i) : Q'_i → V. The map Q' → Q'_i is f.p. by 1.5(b).
  - Let h : Q' → M and an infinitesimal p : M → V satisfy ph = v'. Then (hc, p) factors g_i a_i, so there is a unique u_i : Q_i → M with p u_i = g_i and u_i a_i = hc.
  - u = (h, u_i) : Q'_i → M has pu = g' and restricts to h on Q'.
  - Uniqueness: any such u restricts on Q_i to a map with the defining properties of u_i.
- *Composition.* Let v be a valuation of Q. Write v = g_i a_i with a_i birhizomic at g_i, and g_i = g_ij b_ij with b_ij birhizomic at g_ij. The composite b_ij a_i is f.p. by 1.5(a).
  - Given (h, p) with p infinitesimal and ph = v, take the unique u_i with p u_i = g_i and u_i a_i = h.
  - Then take the unique u with pu = g_ij and u b_ij = u_i. It satisfies u b_ij a_i = h.
  - Uniqueness: if u' has these properties, then u' b_ij has those of u_i, so u' b_ij = u_i, and then u' = u. ∎

Hence the Grothendieck topology J that the birhizomic covers define on A_P^op has as covering sieves of Q exactly the sieves containing (the sieve generated by) some birhizomic cover of Q (SGA4 II.1.3–1.4; quoted). Its sheaves are the presheaves satisfying the sheaf condition for birhizomic covers. This agrees with the problem's assertion that the birhizomic covers form a Grothendieck topology. The property used below is:

(★) every covering sieve of every object Q contains all members of some birhizomic cover of Q.

**Lemma 1.10 (witness subfamily).** {Q → Q_i}_{i ∈ I_0} is a birhizomic cover of Q, all of whose members are f.p.

*Proof.* For a valuation v of Q, the cover property gives i and a factorization through Q_i at which a_i is birhizomic. Then i ∈ I_0. ∎

---

## §2 Theorem B: kernel faces of f.p. maps are principal

**Theorem B.** For every monoid P and every f.p. f : P → Q, Φ_Q = face(s) for some s ∈ P.

*Proof.*

*Step 1: reduction.* By 1.7 with B = P, Q is a retract under P of Q' = ((P ⊕ N^k)/R)^{int,sat,sharp}, with R finite. Then ker(P → Q) = ker(P → Q'):
- if x dies in Q', it dies in Q, which is the image of Q' under the retraction;
- if x dies in Q, apply the section Q → Q', which is a map under P.

*Step 2: the kernel of P → Q'.* Write the relations as pairs (r_j, s_j) in P ⊕ N^k, for j = 1..J, and put l_j = r_j − s_j ∈ P^gp ⊕ Z^k. Let L be the subgroup they generate and G = (P^gp ⊕ Z^k)/L. As in 1.3, M_0 is the image of P ⊕ N^k in G, M_1 is its saturation in G, and Q' = M_1/M_1^*.

x ∈ P dies in Q' iff its image is a unit of M_1, iff −x ∈ M_1, iff −nx ∈ M_0 for some n ≥ 1, iff (−nx − p, −m) ∈ L for some p ∈ P and m ∈ N^k. Write the element of L as Σ c_j l_j with c ∈ Z^J.
- The Z^k-component condition says c lies in K := {c ∈ Z^J : the Z^k-part of Σ c_j l_j lies in −N^k}.
- K is the set of lattice points of a rational polyhedral cone, so it is a finitely generated monoid (Gordan's lemma).
- Let ψ : K → P^gp be the P^gp-part of c ↦ −Σ c_j l_j. It is additive, so Y := ψ(K) is a finitely generated submonoid of P^gp.
- The condition reads nx + p = ψ(c). Conversely, for c ∈ K with ψ(c) = nx + p, put m := −(Z^k-part of Σ c_j l_j) ∈ N^k.

Hence x dies iff nx + p ∈ Y for some n ≥ 1 and p ∈ P, i.e. iff nx ≤ y for some y ∈ S := Y ∩ P. Since x ≤ nx, this is iff x ≤ y for some y ∈ S. So Φ_Q is the face generated by the submonoid S, namely ∪_{t ∈ S} face(t).

*Step 3: principality.* The family {face(t) : t ∈ S} is directed, since face(t + t') ⊃ face(t), face(t'). Consider a strictly increasing chain face(s_1) ⊊ face(s_2) ⊊ … with s_i ∈ S, and put G_i := face(s_i)^gp ∩ Y^gp.
- For any face F of P, F^gp ∩ P = F: if x = a − b with a, b ∈ F and x ∈ P, then x + b = a ∈ F, so x ∈ F.
- If n s_{i+1} ∈ G_i for some n ≥ 1, then n s_{i+1} ∈ face(s_i)^gp ∩ P = face(s_i), so s_{i+1} ∈ face(s_i), contradicting strictness.
- So s_{i+1} ∈ G_{i+1} has infinite order modulo G_i. Since G_i ⊂ G_{i+1}, the ranks strictly increase inside the finitely generated free group Y^gp (P^gp is torsion-free).

Hence chains have length ≤ rk Y^gp + 1, and there is a maximal face(s) with s ∈ S, starting from s = 0. By directedness it contains every face(t), t ∈ S, so Φ_Q = face(s). ∎

**Corollary 2.1.** For f.p. Q, (b_s, b_s → Q) is terminal in the comma category of objects of B_P over Q (§4.1).

---

## §3 Theorem D: the nerve theorem

**Theorem D.** Let P be any monoid, f : P → Q any map in 𝒞, and {Q → Q_i}_{i ∈ I} a family of f.p. maps under Q such that every valuation v : Q → V (V valuative) factors through some Q_i. For finite nonempty σ ⊂ I, let Q_σ be the pushout of the Q_i (i ∈ σ) over Q in 𝒞, and put Φ_σ := ker(P → Q_σ). Let τ ⊂ P be any subset with Φ_Q ⊂ τ, and put N_τ := {σ : Φ_σ ⊂ τ}. Then:
- N_τ is a nonempty simplicial complex, i.e. closed under nonempty subsets, since Q_{σ'} → Q_σ for σ' ⊂ σ;
- its augmented ordered chain complex is exact;
- its augmented ordered cochain complex with coefficients in any abelian group A is exact.

**Ordered complexes.** The *augmented ordered chain complex* C̃(N) of a simplicial complex N on a vertex set I has:
- C̃_p free on the tuples (i_0, …, i_p) ∈ I^{p+1}, repetitions allowed, with {i_0, …, i_p} ∈ N, for p ≥ 0;
- C̃_{−1} = Z;
- the differential d = Σ_j (−1)^j (delete i_j), with each vertex mapping to 1 ∈ C̃_{−1}.

The augmented ordered cochain complex is Hom(C̃(N), A).

### 3.1 Cones and valuations

Put U := Q^gp ⊗ Q. Then Q ⊂ U (1.1). Let Q_Q := Q_{≥0}·Q.
- A *cone* is a subset K ⊂ U with 0 ∈ K, K + K ⊂ K and Q_{>0}K ⊂ K. Its lineality is lin K := K ∩ (−K), a subspace.
- A cone W is *total* if W ∪ (−W) = U.

Facts:
- lin Q_Q = 0. If x = q/n and −x = q'/n', then n'q + nq' = 0 in Q^gp, so q = q' = 0 by sharpness.
- A valuation v : Q → V gives the total cone W_v := {x ∈ U : v(x) ≥ 0 in V^gp ⊗ Q} ⊃ Q_Q. Here v is extended Q-linearly, and the divisible hull of a totally ordered group is totally ordered.
- Conversely, a total cone W ⊃ Q_Q gives a valuation v_W : Q → V_W := W/lin W. V_W is the nonnegative part of the totally ordered Q-vector space H_W := U/lin W, so it is integral, saturated, sharp and valuative. Moreover v_W(x) ≥ 0 iff x ∈ W, and v_W(x) = 0 iff x ∈ lin W.

**Lemma Z.** Every cone K is contained in a total cone W with lin W = lin K.

*Proof.* Cones K' ⊃ K with lin K' = lin K are closed under unions of chains, so Zorn's lemma gives a maximal one, K'. Suppose x ∉ K' ∪ (−K'), and put K'' = K' + Q_{≥0}x. If y ∈ lin K'', write y = k_1 + ax and −y = k_2 + bx with k_i ∈ K' and a, b ≥ 0. Then k_1 + k_2 = −(a + b)x.
- If a + b > 0, dividing gives −x ∈ K', a contradiction.
- So a = b = 0, and y ∈ lin K'.

Thus lin K'' = lin K' while K'' ⊋ K', contradicting maximality. So K' is total. ∎

**Injective valuations.** Every M ∈ 𝒞 has a valuation ι : M → V with ι(m) = 0 only for m = 0. Apply Lemma Z to M_Q ⊂ M^gp ⊗ Q, which has lineality 0, and take v_W.

### 3.2 Lemma 1: lifting loci are finitely many sign conditions

For i ∈ I, let E_i be the set of total cones W ⊃ Q_Q such that v_W extends to Q_i, i.e. there is g : Q_i → V_W under Q.

**Lemma 1.** For each i there is a finite set X_i ⊂ U such that:
- (a) E_i = {W : X_i ⊂ W};
- (b) for every valuation v : Q → V, if v extends to Q_i then X_i ⊂ W_v.

*Proof.*

(i) By 1.7 with B = Q, M := Q_i is a retract under Q of T = ((Q ⊕ N^S)/R)^{int,sat,sharp}, with S, R finite. A map out of Q under Q extends to M iff it extends to T: compose with T → M in one direction, and with M → T in the other.

(ii) Let H be a totally ordered Q-vector space and v : Q → H_{≥0} a map. A map T → H_{≥0} under Q is the same as a vector y ∈ H^S with y ≥ 0 satisfying the relations. This holds by 1.3, since H_{≥0} ∈ 𝒞. Write the j-th relation as (a_j, α_j) = (b_j, β_j), with a_j, b_j ∈ Q and α_j, β_j ∈ N^S. It reads (α_j − β_j)·y = c_j, where c_j := v(b_j − a_j) and v is extended Q-linearly to U.

(iii) *Fourier–Motzkin.* The system {y ≥ 0; (α_j − β_j)·y − c_j = 0} is a finite homogeneous system of non-strict rational linear inequalities in (y, c), each equation counting as two inequalities. Eliminating one unknown y_s replaces the system by:
- all sums of a lower bound and an upper bound for y_s (after scaling by positive rationals);
- the inequalities not involving y_s.

This preserves solvability over any totally ordered Q-vector space H: given the other unknowns, take y_s to be the maximum of its finitely many lower bounds, or the minimum of its upper bounds if there are no lower bounds, or 0 if there are neither. Eliminating all of y gives finitely many rational vectors u_m, obtained by a formal procedure independent of H, such that:

  the system is solvable in H ⟺ u_m·c ≥ 0 for all m.

Put x_m := Σ_j u_{mj}(b_j − a_j) ∈ U and X_i := {x_m}. Then u_m·c = v(x_m).
- (a) Take H = H_W. Then v_W extends to Q_i iff v_W(x_m) ≥ 0 for all m, iff X_i ⊂ W.
- (b) Take H = V^gp ⊗ Q, which contains V in H_{≥0}. If v extends to Q_i, it extends to T with values in V ⊂ H_{≥0}, so v(x_m) ≥ 0, i.e. X_i ⊂ W_v. ∎

### 3.3 Lemma 2: the nerve condition as a cone condition

For finite σ put X_σ := ∪_{i∈σ} X_i and K_σ := Q_Q + cone(X_σ). For a cone K ⊃ Q_Q put f^{-1}(lin K) := {p ∈ P : f(p) ∈ lin K}. Since f(p) ∈ Q_Q ⊂ K, this is {p : −f(p) ∈ K}.

**Lemma 2.** Φ_σ = f^{-1}(lin K_σ). The same holds for an ordered tuple t with repetitions, Q_t = Q_{i_0} ⊔_Q … ⊔_Q Q_{i_p}: then Φ_t = Φ_{set(t)}.

*Proof.* A map Q_σ → V_W under Q is a family of maps Q_i → V_W under Q, i ∈ σ, because Q_σ is the pushout in 𝒞 and V_W ∈ 𝒞. So v_W extends to Q_σ iff W ∈ ∩_{i∈σ} E_i, iff K_σ ⊂ W.
- (⊂) Let p ∈ Φ_σ. Take W ⊃ K_σ total with lin W = lin K_σ (Lemma Z). Then v_W extends to Q_σ and kills the image of p, so f(p) ∈ lin W = lin K_σ.
- (⊃) Let f(p) ∈ lin K_σ. Take an injective valuation ι : Q_σ → V and put v = ι|_Q. Then v extends to each Q_i, i ∈ σ, so by Lemma 1(b), X_σ ⊂ W_v and K_σ ⊂ W_v. Hence v(f(p)) = 0 in V^gp ⊗ Q, so it is 0 in V (1.1). Thus ι kills the image p̄ of p, and p̄ = 0.

For tuples, maps out of Q_t are again tuples of maps out of the Q_{i_j}, so the same argument gives Φ_t = f^{-1}(lin K_{set(t)}). ∎

Let 𝒢 := {cones K ⊃ Q_Q : f^{-1}(lin K) ⊂ τ}. Then N_τ = {σ : K_σ ∈ 𝒢}, and:
- **(G0)** if Q_Q ⊂ K ⊂ K' and K' ∈ 𝒢, then K ∈ 𝒢;
- **(G1)** if K ∈ 𝒢 and W ⊃ K has lin W = lin K, then W ∈ 𝒢;
- **(G2)** for a cone K ⊃ Q_Q and z ∈ U, f^{-1}(lin(K + Qz)) = f^{-1}(lin(K + Q_{≥0}z)) ∪ f^{-1}(lin(K + Q_{≥0}(−z))). To see this, write −f(p) = k + tz and split on the sign of t. Hence if K + Q_{≥0}z and K + Q_{≥0}(−z) are both in 𝒢, so is K + Qz;
- **(G3)** Q_Q ∈ 𝒢, because f^{-1}(lin Q_Q) = f^{-1}(0) = Φ_Q ⊂ τ.

### 3.4 Lemma 3: finite subcover

The set 𝒯 of total cones W ⊃ Q_Q is a closed subset of {0,1}^U. Each defining condition involves finitely many coordinates:
- z ∈ W or −z ∈ W;
- z, z' ∈ W ⇒ z + z' ∈ W;
- z ∈ W ⇒ rz ∈ W;
- q ∈ W for q ∈ Q_Q.

So 𝒯 is compact (Tychonoff). Each E_i = {X_i ⊂ W} is open, since X_i is finite. The E_i cover 𝒯: v_W is a valuation, so it factors through some Q_i, i.e. W ∈ E_i. **Hence there is a finite J_0 ⊂ I with ∪_{i∈J_0} E_i = 𝒯.**

### 3.5 Theorem T: abstract acyclicity

Fix:
- a Q-vector space U and a cone K_0 ⊂ U;
- a family 𝒢 of cones containing K_0, satisfying (G0), (G1) and (G2) for cones containing K_0;
- a finite family (X_j)_{j∈J} of finite subsets of U;
- an abelian group A.

For a cone K ⊃ K_0, let C^•(K) be the complex with C^p(K) = ∏_{(j_0..j_p) ∈ J^{p+1}} A(K + cone X_{j_0} + … + cone X_{j_p}) for p ≥ −1. Here:
- A(K') = A if K' ∈ 𝒢 and 0 otherwise;
- the term for p = −1 is A(K);
- the component maps are id_A when both ends are A, and 0 otherwise. This is well defined by (G0), since a coface map goes to a larger cone;
- d is the alternating sum of the deletions.

If K ∈ 𝒢, C^•(K) is the augmented ordered cochain complex of the simplicial complex N(K) := {σ : K + cone X_σ ∈ 𝒢}. If K ∉ 𝒢, C^•(K) = 0 by (G0).

**Theorem T.** If every total cone W ⊃ K contains some X_j, then C^•(K) is exact.

*Proof.* Induction on m(K) := #{z ∈ Z : z ∉ K and −z ∉ K}, where Z := ∪_j X_j is finite. We may assume K ∈ 𝒢.

*Cone lemma.* Suppose there is j* with {j*} ∈ N(K) such that σ ∈ N(K) ⇒ σ ∪ {j*} ∈ N(K). Define (hc)(j_0..j_{p−1}) := c(j*, j_0..j_{p−1}).
- h is well defined by the cone-point hypothesis. If the target tuple carries A, its set lies in N(K), so the set with j* added does too, and the source tuple carries A. If the target carries 0, there is nothing to check.
- The standard computation gives dh + hd = id. On a tuple t carrying A, every tuple involved has its set inside set(t) ∪ {j*} ∈ N(K), so all component maps are identities. In degree −1, (hdc)() = (dc)(j*) = c, which uses {j*} ∈ N(K) and K ∈ 𝒢.

So C^•(K) is contractible.

*Base case m(K) = 0.* Take W ⊃ K total with lin W = lin K (Lemma Z), and some X_{j*} ⊂ W. Let z ∈ X_{j*}. If z ∉ K, then −z ∈ K, because z is decided, so z ∈ lin W = lin K ⊂ K, a contradiction. So X_{j*} ⊂ K and K + cone X_{j*} = K. Hence j* is a cone point, and the cone lemma applies.

*Row lemma.* For any cone K' ⊃ K_0 and z ∈ U, the complex built as above from K' and the two-member family X_+ = {z}, X_− = {−z} is exact. If K' ∉ 𝒢 it is zero. Otherwise:
- some total W ⊃ K' with lin W = lin K' lies in 𝒢 (Lemma Z, (G1));
- W contains z or −z, so K' + Q_{≥0}z or K' + Q_{≥0}(−z) lies in 𝒢 (G0), i.e. one vertex is in the nerve;
- if both vertices are, so is the edge, because K' + cone{z, −z} = K' + Qz (G2).

So the nerve is a vertex or an edge, and the cone lemma applies.

*Inductive step, m(K) > 0.* Pick an undecided z ∈ Z and form the double complex

D^{p,q} = ∏_{σ ∈ J^{p+1}, ρ ∈ {±}^{q+1}} A(K + cone X_σ + cone{ρ_0 z, …, ρ_q z}),  p, q ≥ −1,

with the two commuting deletion differentials.
- **Rows.** For fixed p, the row is the product over σ of row-lemma complexes on K + cone X_σ, hence exact.
- **Columns q ≥ 0.** The column is ∏_ρ C^•(K_ρ), with K_ρ ∈ {K + Q_{≥0}z, K + Q_{≥0}(−z), K + Qz}. The cover hypothesis passes to K_ρ ⊃ K. Also m(K_ρ) < m(K), because z becomes decided and decided elements stay decided. So these columns are exact by induction.
- **Column q = −1** is C^•(K).

Each total degree involves finitely many (p, q). Filtering by p, with exact rows, shows Tot D is acyclic. The columns q ≥ 0 form a subcomplex, since the q-differential raises q. Filtering that subcomplex by q shows it is acyclic. The quotient is column −1 (up to sign), so the long exact sequence shows C^•(K) is exact. ∎

### 3.6 Proof of Theorem D

1. *Finite pieces.* Let J' ⊃ J_0 be finite. Apply Theorem T with U = Q^gp ⊗ Q, K_0 = K = Q_Q, the family 𝒢 of 3.3, and (X_i)_{i∈J'}. Every total W ⊃ Q_Q contains some X_i with i ∈ J_0, by Lemma 3 and Lemma 1(a). By Lemma 2, N(Q_Q) is the full subcomplex N_τ(J') of N_τ on J'. So the augmented ordered cochain complex of N_τ(J') with coefficients A is exact, for every A.
2. *Nonemptiness.* Take W_0 ⊃ Q_Q total with lin W_0 = 0 (Lemma Z). Then W_0 ∈ 𝒢 by (G3) and (G1). W_0 contains some X_i, so K_{{i}} ⊂ W_0 and {i} ∈ N_τ by (G0).
3. *Chains, finite case.* C̃ := C̃(N_τ(J')) is a complex of free abelian groups. The universal coefficient theorem gives a surjection H^n(Hom(C̃, A)) → Hom(H_n C̃, A). Taking A = H_n C̃ shows H_n C̃ = 0.
4. *Chains, general case.* C̃(N_τ) is the directed union of the C̃(N_τ(J')) over finite J' ⊃ J_0, so it is exact.
5. *Cochains, general case.* An exact complex of free abelian groups is split: each boundary group B_{n−1} ⊂ C̃_{n−1} is free, so 0 → Z_n → C̃_n → B_{n−1} → 0 splits. Hence Hom(C̃(N_τ), A) is exact for every A. ∎

---

## §4 The sheaf-theoretic part

### 4.1 Kan extension, π^{-1}, π_*

Presheaves on A_P^op (resp. B_P^op) are functors A_P → Ab (resp. B_P → Ab), and ι : B_P → A_P is the inclusion. Since the topology on B_P^op is trivial, exactness in Sh(B_P) = PSh(B_P) is objectwise.

**Left Kan extension.** (Lan F)(Q) = colim_{(b, b→Q) ∈ ι/Q} F(b). By 1.6, a pair (b_x, b_x → Q) exists iff x ∈ Φ_Q, and the map is then unique. So ι/Q is equivalent to the poset {face(x) : x ∈ Φ_Q}, which is nonempty (it contains {0}) and directed (x, y ∈ Φ_Q ⇒ x + y ∈ Φ_Q). Hence Lan F(Q) is a filtered colimit, and **Lan is exact.**

**Lemma 4.1 (f.p. objects).** Let Q be f.p. under P. By Theorem B, Φ_Q = face(x_Q). Put b(Q) := b_{x_Q}.
- (b(Q), b(Q) → Q) is terminal in ι/Q, so F(Φ_Q) := F(b(Q)) → (Lan F)(Q) is an isomorphism, natural in F.
- For a map Q → Q' of f.p. objects, Lan F(Q → Q') corresponds to F(b(Q) → b(Q')).
- For b ∈ B_P, the unit F(b) → (Lan F)(b) is an isomorphism (b is terminal in ι/b).
- Consequently, (Lan ∏_j F_j)(Q) = ∏_j (Lan F_j)(Q) naturally for f.p. Q. This is used only on f.p. objects.

**π^{-1} and π_*.**
- π^{-1}F = (Lan F)^#, where # is sheafification for J. It is exact, since Lan and # are.
- For a sheaf G, Hom(π^{-1}F, G) = Hom(Lan F, G) = Hom(F, G∘ι). So **π_*G = G|_{B_P}.**
- The unit F → π_*π^{-1}F at b is the composite F(b) ≅ (Lan F)(b) → (Lan F)^#(b).

### 4.2 Injectives

For τ ∈ Pr(P) and an abelian group A, let I_{τ,A}(b) = A if Φ_b ⊂ τ and 0 otherwise, with transition maps id_A or 0. This is a functor: b → b' gives Φ_b ⊂ Φ_{b'}, so a pattern 0 → A never occurs.

**Lemma 4.2.** Hom(F, I_{τ,A}) ≅ Hom(F(τ), A). Hence I_{τ,A} is injective when A is.

*Proof.* If Φ_b ⊂ τ, there is a unique map b → b_τ, and naturality forces φ_b = φ_τ ∘ F(b → b_τ). Conversely this formula, with φ_b = 0 otherwise, defines a natural map, because B_P is a preorder. So Hom(−, I_{τ,A}) = Hom(ev_{b_τ}(−), A), which is exact when A is injective. ∎

**Resolution.** Take E(−) an injective embedding of abelian groups. Then F → ∏_{τ ∈ Pr(P)} I_{τ, E(F(τ))} is a monomorphism: at b, the component τ = Φ_b is F(b) ↪ E(F(b)). Iterating on cokernels gives an objectwise-exact injective resolution 0 → F → I^0 → I^1 → …, with I^k = ∏_τ I_{τ, A_{k,τ}}. The products may be infinite.

### 4.3 The system Cov

Let 𝔅 be the set of f.p. objects of A_P. Let **Cov** be the set of birhizomic covers {Q → Q_i} with Q ∈ 𝔅 and every Q → Q_i f.p.

**Lemma 4.3.**
- (i) Every member of Cov is a covering family for J.
- (ii) For 𝒰 ∈ Cov, every Q_i and every iterated pushout Q_t = Q_{i_0} ⊔_Q … ⊔_Q Q_{i_p} lies in 𝔅 (Lemma 1.5).
- (iii) For Q ∈ 𝔅 and every covering sieve R of Q, there is 𝒰 ∈ Cov all of whose members lie in R. Indeed, by (★) R contains a birhizomic cover, and its witness subfamily (Lemma 1.10) lies in Cov.
- (iv) In 𝒰 ∈ Cov, every valuation of Q factors through some member.

Every b ∈ B_P lies in 𝔅 (Lemma 1.5(c)).

### 4.4 Čech complexes

For a presheaf G and 𝒰 = {Q → Q_i}_{i∈I}, the augmented Čech complex is

Č^p(𝒰, G) = ∏_{t ∈ I^{p+1}} G(Q_t) for p ≥ 0, with Č^{−1} = G(Q),

with the alternating restriction differential (all ordered tuples, repetitions allowed).

**Proposition 4.4.** Let Q ∈ 𝔅, 𝒰 ∈ Cov over Q, τ ∈ Pr(P), and G = Lan I_{τ,A}. Then:
- if Φ_Q ⊄ τ, the augmented Čech complex of G on 𝒰 is 0;
- otherwise it is the augmented ordered cochain complex of N_τ with coefficients A.

In both cases it is exact.

*Proof.* All Q_t are f.p. (4.3(ii)), so G(Q_t) = I_{τ,A}(Φ_t) by Lemma 4.1, which is A iff Φ_t ⊂ τ. The restriction maps between nonzero terms are id_A.
- If Φ_Q ⊄ τ, then since Φ_Q ⊂ Φ_t every term vanishes.
- Otherwise Φ_t = Φ_{set(t)} by Lemma 2 of §3. Here P → Q → Q_t is the composite, and Q_t is the same pushout. So the complex is Hom(C̃(N_τ), A).

Exactness is Theorem D. Its hypotheses hold: the members are f.p. under Q, every valuation of Q factors through one (4.3(iv)), and Φ_Q ⊂ τ. ∎

**Corollary 4.5.** For Q ∈ 𝔅 and 𝒰 ∈ Cov, the augmented Čech complex of each Lan I^k is exact. On 𝔅, Lan I^k = ∏_τ Lan I_{τ,A_{k,τ}} (Lemma 4.1), only objects of 𝔅 occur, and products of exact complexes are exact.

### 4.5 Sheafification does not change values on f.p. objects

**Standard facts (quoted).**
- For a sieve R generated by a family {U_i → U} with pushouts, Hom_PSh(R, G) is the equalizer of ∏ G(U_i) ⇉ ∏ G(U_{ij}).
- G^+(U) = colim_{R ∈ J(U)} Hom(R, G).
- G^# = G^{++}.

**Lemma 4.6.** Let G be a presheaf such that, for all Q ∈ 𝔅 and 𝒰 ∈ Cov over Q, the sequence 0 → G(Q) → ∏ G(Q_i) ⇉ ∏ G(Q_ij) is exact (an equalizer). Then G(Q) → G^#(Q) is an isomorphism for Q ∈ 𝔅.

*Proof.*
- By 4.3(iii), the sieves generated by members of Cov are cofinal in J(Q). On each of them Hom(R, G) = G(Q), compatibly with the transition maps, so G(Q) ≅ G^+(Q).
- For 𝒰 ∈ Cov, all of Q, Q_i, Q_ij lie in 𝔅, where G → G^+ is an isomorphism. So G^+ satisfies the same hypothesis.
- Repeat to get G^{++}. ∎

**Corollary 4.7.**
- Lan F satisfies Lemma 4.6. To see this, use the exact sequence 0 → Lan F → Lan I^0 → Lan I^1 and Cor. 4.5 in degrees −1, 0, 1, then chase:
  - if s ∈ Lan F(Q) restricts to 0 everywhere, its image in Lan I^0(Q) is 0, so s = 0;
  - a compatible family (s_i) glues in Lan I^0 to some t;
  - t maps to an element of Lan I^1(Q) with all restrictions 0, hence to 0;
  - so t comes from s ∈ Lan F(Q), and s restricts to s_i by injectivity of Lan F(Q_i) → Lan I^0(Q_i).
- Hence for Q ∈ 𝔅, F(Φ_Q) ≅ Lan F(Q) ≅ π^{-1}F(Q), naturally.
- In particular **the unit F → π_*π^{-1}F is an isomorphism.**
- Likewise π^{-1}I^k(Q) = I^k(Φ_Q) on 𝔅, so **Ȟ^p(𝒰, π^{-1}I^k) = 0 for p > 0 and 𝒰 ∈ Cov** (Cor. 4.5).

### 4.6 Cartan's criterion (proved)

**Proposition 4.8.** Let G be an abelian sheaf on (A_P^op, J) with Ȟ^p(𝒰, G) = 0 for all p > 0 and all 𝒰 ∈ Cov. Then H^p(U, G) = 0 for all p > 0 and all U ∈ 𝔅.

**Fact.** For an injective sheaf I and any family 𝒰 with pushouts, Ȟ^p(𝒰, I) = 0 for p > 0.

*Proof of the Fact.* Let K_p = ⊕_{t ∈ I^{p+1}} Z_{U_t}, where Z_V is the free abelian presheaf on h_V, with the alternating face differential. Then Hom_PSh(K_•, G) = Č^•(𝒰, G).

Evaluate at W. K_•(W) splits as a sum over ψ : U → W (maps in A_P, i.e. W under U). The summand for ψ is the chain complex of the full simplex, with repetitions, on T_ψ = {(i, φ) : φ : U_i → W compatible with ψ}. Prepending a fixed element of T_ψ contracts it in positive degrees. So K_• resolves the sieve presheaf Z_R. Sheafification is exact, and Hom_Sh(−, I) is exact. Hence Č^•(𝒰, I) = Hom_Sh(K_•^#, I) is exact in positive degrees. ∎

*Proof of Proposition 4.8.* Embed G ↪ I with I an injective sheaf, and let Q = I/G (sheaf quotient). Then G(W) = ker(I(W) → Q(W)).

(a) I(V) → Q(V) is onto for V ∈ 𝔅.
- Take s ∈ Q(V). It lifts locally on some covering sieve R.
- By 4.3(iii), choose 𝒱 = {V → V_i} ∈ Cov with members in R and lifts t_i of s|_{V_i}.
- c_ij := t_j − t_i on V_ij lies in G(V_ij) and is a Čech 1-cocycle for G.
- Since Ȟ^1(𝒱, G) = 0, c = dg with g ∈ Č^0(𝒱, G).
- The family (t_i − g_i) is compatible, so it glues in the sheaf I to some t, and t maps to s, because Q is a sheaf.

(b) Q satisfies the hypothesis.
- For 𝒰 ∈ Cov all the U_t lie in 𝔅, so 0 → Č(𝒰, G) → Č(𝒰, I) → Č(𝒰, Q) → 0 is exact by (a).
- By the Fact, Ȟ^p(𝒰, Q) ≅ Ȟ^{p+1}(𝒰, G) = 0 for p ≥ 1.

(c) Conclusion.
- H^1(U, G) = coker(I(U) → Q(U)) = 0 by (a).
- H^p(U, G) ≅ H^{p−1}(U, Q) for p ≥ 2.
- Induction on p, applied to all sheaves satisfying the hypothesis at once, finishes the proof. ∎

### 4.7 Conclusion

- By Cor. 4.7 and Prop. 4.8, H^p(U, π^{-1}I^k) = 0 for p > 0 and U ∈ 𝔅.
- Since π^{-1} is exact, π^{-1}F → π^{-1}I^• is a resolution by Γ(U, −)-acyclic sheaves. So for U ∈ 𝔅, H^p(U, π^{-1}F) = H^p(I^•(Φ_U)), which is F(Φ_U) for p = 0 and 0 for p > 0 (Cor. 4.7 and the exactness of the resolution).
- π_* is restriction. Taking an injective resolution G → J^•, we get (R^pπ_*G)(b) = H^p(J^•(b)) = H^p(b, G). Cohomology of presheaves on B_P is objectwise.
- Every b ∈ B_P is f.p. Hence R^pπ_*π^{-1}F = 0 for p > 0. On H^0, the derived unit F → π_*π^{-1}F → Rπ_*π^{-1}F induces the underived unit, which is an isomorphism (Cor. 4.7).

So F → Rπ_*π^{-1}F is a quasi-isomorphism. **This proves the Main Theorem.** ∎

---

## §5 Other routes worth recording

- **Fine case first (finitely generated P).** For finitely generated P, B_P is the finite poset of faces. The Čech nerves can be identified with nerves of real polyhedral dual cones, and they are acyclic by the convex (Borsuk) nerve theorem. This gives the same conclusion; the argument above supersedes it.
- **Theorem D via real approximation.** An independent proof of Theorem D compactifies the valuation space via Fourier–Motzkin (the lifting loci are closed), approximates by real linear functionals, and applies the closed-convex nerve theorem. A separate referee check found this proof correct.
- **Characterization of birhizomy (not needed).** Let f : Q → Q' and g : Q' → V be f.p. Then f is birhizomic at g iff both of the following hold:
  - the induced map of groups modulo kernel faces is an isomorphism;
  - Q'[−K']^♯ lies in an initial infinitesimal test object attached to v.

  Also, for valuative M, a map M → N is infinitesimal iff it kills no nonzero element. Neither fact is used above.
- **Dead ends.**
  - "Closed subdivision charts are birhizomic at wall valuations" is false (P = N^2): birhizomy at g forces g > 0 on Q∖{0} when v is nonzero on P∖{0}. So covers are not refinements of subdivision covers.
  - Naive descent of covers to finitely generated submonoids P_S of P fails, because valuations of P_S need not extend to P.
  - Real-parameter "Hahn convexification" does not give connected loci.

  The proof above avoids all of these by working directly with total cones in Q^gp ⊗ Q.

## §6 Status

- **Proved:** the Main Theorem (answer YES) for every monoid P and every presheaf F, as written in §§1–4. The chain was checked twice, step by step, during the attempt. In my own reading, every step written here is complete.
- **Standard results quoted, not reproved:**
  - Zorn's lemma, Tychonoff's theorem and Gordan's lemma;
  - the universal coefficient surjection for complexes of free abelian groups;
  - the double-complex lemma for complexes in the region p, q ≥ −1;
  - the description of the topology generated by a pretopology (SGA4 II);
  - the plus construction (G^# = G^{++}, sieve-equalizer description);
  - existence of injective embeddings in Ab and in abelian sheaves;
  - set-theoretic size handling by universes.
- **Interpretation choices** (stated explicitly, harmless):
  - Coverings of an object Q of A_P are birhizomic covers with base Q.
  - "Finite presentation" means compactness in the under-category. Under the literal reading (finitely many generators and relations), Lemma 1.7 is immediate and nothing changes.
- **Gaps:** none known.
