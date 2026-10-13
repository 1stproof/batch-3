# round11_q1 — answer

**Status: PARTIAL.** I neither prove MS11 nor give a counterexample. What I add:
- §1: a logical remark. Under (Rig), MS11 is *equivalent* to the problem's claim, not merely sufficient for it. So the chain is a correct reduction (I found no flaw in the steps I re-checked, §6), but MS11 carries the full difficulty of the problem.
- §2: a copy-free reformulation of MS11 by lift-curves and stars (Lemmas 2.1–2.4, proved). In particular MS11 always holds "up to an automorphism".
- §3: a complete and corrected write-up of the planner's Mechanism D (Grothendieck connectedness in the 3-fold). It is proved down to a trichotomy of failure configurations, (β) / (γ) / (ι) (Theorem 3.6). I also record one gap in the planner's sketch and how it is absorbed.
- §4: a new necessary condition at the chain's endpoint, the *rigid twin* (Lemma 4.1). If MS11 fails at a MERGE/pMOV endpoint, then Q_t has, for every t, both a component ≅ Y_t and a component ≅ Y_0 (constant in t). Consequently Y_0 ∈ F′.
- §5: an explicit local model (smooth 3-fold, involution σ) showing that the (β)-failure is consistent with every chart-and-family-local constraint, including (R1), (R2), Theorem N and the pattern rules. It also isolates the Teichmüller-geometric feature that a proof would have to exclude ("square-root approach" of twin moduli).
- §6: chain check; §7: proved / not proved / open.

Readings: (R1), (R2) with H_0 = id, exactly as in the task. Notation is as in the task file: Def(Q), q, B, s_e, N := ∏_e s_e, labels, L_y := {s_e = 0 for all e at y}, F_y, (K1)–(K4), transport families Ñ_c̃, transport sheets, lift-curves. "Generic t" means: outside the countable exceptional set of Theorem N (R8-3 §3), the discrete sets Z_A, Z_φ of R8-8 §4, and the countable sets of R7-3 Lemma 1(b) for the finitely many (piece, vertex) pairs. Cited results of the run that I use as stated are named at the point of use: Theorem N (R8-3), Lemma U (R8-2), Lemma T (round9_q7), R7-4 Lemma 2, round9_q2 Lemma 1.

---

## 1. Logical status of MS11

**Proposition 1.1.** Assume the problem's hypotheses together with (Rig). Then the following are equivalent:
- (a) MS11 holds for every admissible datum (Q, B, β̃, b̃, x);
- (b) Y_t = Y_0 for all t.

*Proof.*
- (a) ⇒ (b) is the chain (§6 re-checks it).
- (b) ⇒ (a): MS11 has "t ↦ Y_t is non-constant" among its hypotheses. If (b) holds, no family satisfies that hypothesis, so MS11 is vacuously true. ∎

**Consequences.**
1. A proof of MS11 is a proof of the problem under (Rig). Any such proof must derive a contradiction from "Y non-constant" at some point.
2. The t = 0 shadow of MS11's conclusion is false in general: at the walk chain's endpoint, x is MERGE/MOV along b̃. So no argument that uses only t = 0 data and never uses the non-constancy of Y can work.
3. Hence the "missing statement" format (MS8, MS10, MS11, all containing "Y non-constant") does not reduce the logical difficulty. It localises where the contradiction has to be found. A statement that genuinely reduced the problem would be of the type of MS7 (a property of V_0 alone), or a statement about families that does not mention Y.

---

## 2. Copy-free reformulation: lift-curves and stars

Fix Q, B, ε as in MS11. Let 𝒥 := {(p,t) ∈ B × Δ_ε : q(p) = Q_t}, Q_t := H_t(Q). Its irreducible components through (0,0) are the lift-curves; let 𝔏 denote the set of lift-curves. By round9_q2 Lemma 1 (re-checked):
- 𝔏 is finite and permuted transitively by Aut(Q);
- each L ∈ 𝔏 is finite over Δ_ε and surjects onto it;
- after shrinking, every point of 𝒥 lies on some L.

A lift-curve lies in the locus {all s_e = 0}, so every label is intact on it and F_y is continuous on L.

**Definition.**
- For L ∈ 𝔏, C(L) is the set of labels y with F_y(p) ≅ Y_t for all (p,t) ∈ L.
- For a transport sheet Σ (of any lifted branch at 0), P(Σ) is the set of labels Y-persistent on Σ.
- Σ is *of boundary type* if its branch c̃ is a boundary branch at Q (Q is a puncture of the piece of c), and *of interior type* otherwise.

**Lemma 2.1 (sheets contain lift-curves; t = 0 slices).** Let Σ be a transport sheet of a lifted branch c̃.
- (a) Σ is an irreducible 2-dimensional analytic germ, and t is not identically 0 on Σ.
- (b) Σ ∩ {t = 0} is a union of lifted branches at 0.
- (c) Σ contains at least one lift-curve.

*Proof.*
- (a) Σ is a component of closure(Ñ_c̃), which has pure dimension 2 (R7-4 Lemma 2(c)). Its generic points lie in Ñ_c̃, which is open in a set fibred over t with 1-dimensional fibres. So t ≢ 0 on Σ.
- (b) By Krull, Σ_0 := Σ ∩ {t = 0} is a curve germ at (0,0). It lies in q^{-1}(B_0) by (R2) (H_0 = id, and H commutes with closures). Hence it is a union of lifted branches.
- (c) For small t ≠ 0, Σ_t ≠ ∅ (a non-constant holomorphic function on an irreducible germ is open). Every irreducible curve of Σ_t lies in a lift of a punctured branch H_t(c′) ∖ {Q_t} of the cone B_t ∩ U. A connected finite cover of a punctured disc is a punctured disc, so the closure of that curve adds exactly one point, a lift of Q_t. Hence Σ ∩ 𝒥 has points over every small t ≠ 0. It is analytic of dimension ≤ 1, since 𝒥 is a curve. So it contains a component of 𝒥 through (0,0). ∎

**Lemma 2.2 (all sheets of c̃ form one Stab_pt(c̃)-orbit).** Let G_c̃ ⊂ Aut(Q) be the pointwise stabiliser of c̃. Then the transport sheets of c̃ are exactly the sets σΣ_1, σ ∈ G_c̃, for any one sheet Σ_1. Moreover, every irreducible 2-dimensional germ at (0,0) of q^{-1}(closure 𝓑) (with 𝓑 = H(B_0 × Δ)) that contains c̃ × {0} is a transport sheet of c̃.

*Proof.*
1. Pick a generic p ∈ c̃ ∖ 0. Then Stab(p) = G_c̃, since stabilisers are generically constant along an irreducible curve. Also no other lifted branch passes through p, since distinct lifted branches meet only at 0.
2. Near (q(p), 0), 𝓑 coincides with N_c := H((c ∖ Q) × Δ_ε), a topological 4-manifold. A pure 2-dimensional analytic germ that is a topological manifold is irreducible: two components would meet in a set of real dimension ≤ 2, whose removal disconnects the union but cannot disconnect a 4-manifold (Hurewicz–Wallman).
3. Hence the local irreducible components of q^{-1}(N_c) at (p,0) are permuted transitively by Stab(p) = G_c̃ (quotient of an irreducible germ by a finite group).
4. Each of these local components meets {t = 0} in the germ of q^{-1}(c) at p, which is c̃. Their union is therefore connected and contains c̃ ∖ 0, so it lies in Ñ_c̃. So near (p,0), closure(Ñ_c̃) = q^{-1}(N_c).
5. Let Σ, Σ′ be sheets of c̃, i.e. irreducible germs containing c̃ × {0}. Each contains some local component at (p,0); say ℓ ⊂ Σ and ℓ′ ⊂ Σ′, with ℓ′ = σℓ, σ ∈ G_c̃. Then σΣ ∩ Σ′ contains the 2-dimensional ℓ′. Both are irreducible of dimension 2, so σΣ = Σ′.
6. The last claim: such a germ coincides near (p,0) with a union of local components of q^{-1}(N_c) ⊂ closure(Ñ_c̃). By irreducibility it lies in closure(Ñ_c̃), and being 2-dimensional it is a component. ∎

Consequently P(σΣ) = σP(Σ), by (K3).

**Lemma 2.3 (persistence is read off any lift-curve).** Let Y be non-constant. Let Σ be a transport sheet of boundary type and L ⊂ Σ a lift-curve. Then P(Σ) = C(L).

*Proof.*
- ⊆: if y is intact on Σ with F_y ≅ Y_t, the same holds on the closed set L ⊂ Σ, by continuity of F_y on the closed set L_y.
- ⊇: let y ∈ C(L) and let t be generic. Take p ∈ L_t. The curves of Σ_t ending at p are lifted branches through p of transported boundary branches; Q_t is a puncture of their pieces because H_t preserves strata. By Theorem N, the Y_t-copy y is intact and STAY along each of them, i.e. y is intact with F_y ≡ Y_t there.
- So the analytic set A_y := {(p′,t′) ∈ Σ ∩ L_y : F_y(p′) ≅ Y_{t′}} contains, for uncountably many t, a curve of Σ_t. Hence dim A_y = 2, and A_y = Σ by irreducibility. (A_y is analytic because t ↦ [Y_t] is holomorphic; R8-3 Lemma 1.) ∎

**Proposition 2.4 (MS11 in incidence form).** Assume MS11's setting (Y non-constant). Put (c̃, L) ∈ I iff some transport sheet of c̃ contains L, and Star(L) := {c̃ : (c̃, L) ∈ I}. Then:
1. x is Y-persistent on some sheet of b̃ iff there is L with x ∈ C(L) and b̃ ∈ Star(L).
2. The hypothesis gives L_1 with x ∈ C(L_1) and β̃ ∈ Star(L_1).
3. For every L and every coarse branch c at Q, Star(L) contains some lift of c.
4. (MS11 up to automorphism.) There is a ∈ Aut(Q) such that a^{-1}x is Y-persistent on some sheet of b̃. Explicitly, a b̃ ∈ Star(L_1).

*Proof.*
1. Combine Lemmas 2.1(c) and 2.3.
2. The hypothesis sheet T contains some L_1 (Lemma 2.1(c)), and x ∈ P(T) = C(L_1).
3. Q_t ∈ closure(H_t(c)), so the closure of q^{-1}(H_t c) contains a lift of Q_t. By Aut(Q)-invariance it contains every lift, in particular L(t). Then some component a Ñ_b̃ has L(t) in the closure of its t-slice (R7-4 Lemma 2(b)). Take an irreducible component of its closure containing the analytic set of such points (round9_q2 Lemma 1 argument).
4. By item 3 there is a with a b̃ ∈ Star(L_1). So x ∈ P(Σ) for a sheet Σ of a b̃, and a^{-1}Σ is a sheet of b̃ with a^{-1}x ∈ P(a^{-1}Σ). ∎

So **the entire content of MS11 is to take a ∈ Stab(x)**. Its failure is a twin phenomenon, as known; Proposition 2.4 states it without tracks or squares. This is the form used in §§3–4.

---

## 3. Mechanism D, written out, with its failure trichotomy

### 3.1 Set-up
- Let S be the component in (S). The analytic set q^{-1}(closure 𝒱) ∩ (B × Δ_ε) has pure dimension 3 (R1), and S × {0} is an irreducible 2-dimensional subset of it. So S × {0} ⊂ X for some irreducible 3-dimensional germ component X at (0,0). Fix one.
- X_0 := X ∩ {t = 0} is pure 2-dimensional (Krull; t ≢ 0 on X since X ⊄ {t = 0}). It is contained in q^{-1}(closure V_0), and S ⊂ X_0.
- N ≢ 0 on X, because S contains points over V_0. Put D := X ∩ {N = 0}, of pure dimension 2 (Krull).

**Lemma 3.1.** Every irreducible component (call it a *D-sheet*) of the germ D is a transport sheet of a lifted branch c̃ ⊂ X_0. Some D-sheet is a transport sheet of β̃, and some D-sheet is a transport sheet of b̃.

*Proof.*
- Let Σ be a D-sheet. Σ ⊄ {t = 0}, since X_0 ∩ {N = 0} is at most 1-dimensional (V_0 is dense in each component of X_0).
- So Σ ∩ {t = 0} is a curve in X_0 ∩ {N = 0}, i.e. a union of lifted branches c̃ ⊂ X_0.
- Σ ⊂ q^{-1}(closure 𝓑), since X ∖ q^{-1}(𝒱) lies over the boundary. By Lemma 2.2, Σ is a transport sheet of c̃.
- β̃ × {0} ⊂ S × {0} ∩ {N = 0} ⊂ D lies in some D-sheet, and that sheet is a sheet of β̃ by Lemma 2.2. The same holds for b̃. ∎

**Gap in the planner's sketch (step 2), and how it is absorbed.** The D-sheet of β̃ need not be the sheet T on which x is persistent: X ⊃ S × {0} was chosen independently of T. By Lemma 2.2 it is σT with σ ∈ G_β̃, carrying the label σx. Either σx = x, or this is already a configuration of type (β) below, with c̃ = β̃. Choosing X ⊃ T instead loses (S), because X_0 then contains β̃ but need not contain S.

### 3.2 Connectedness

**Cited (from memory): Grothendieck's connectedness theorem** (SGA 2, Exp. XIII, Thm 2.1; also Brodmann–Sharp, *Local cohomology*, Ch. 19). Let A be a complete local noetherian domain of dimension d and f_1, …, f_r ∈ m with r ≤ d − 2. Then Spec(A/(f_1, …, f_r)) ∖ {m} is connected.

Apply it with A = Ô_{X,(0,0)}, d = 3, r = 1, f = N. A is a domain: X is an irreducible complex-analytic germ, so O_X is a henselian excellent local domain with a single point in its normalisation, hence analytically irreducible.

The formal components of D are its analytic components, and two of them meet in the punctured spectrum iff they share a curve germ through (0,0). Hence:

**Lemma 3.2.** The graph 𝔊 whose vertices are the D-sheets, with an edge when two D-sheets share a curve germ through (0,0), is connected.

### 3.3 The edges

**Lemma 3.3 (edge types).** Let Σ ≠ Σ′ be D-sheets sharing an irreducible curve germ C through (0,0). Then exactly one of the following holds.
- (α) C is a lift-curve.
- (β) C ⊂ {t = 0}. Then C = c̃ is a lifted branch, both Σ and Σ′ are sheets of c̃, and Σ′ = σΣ with σ ∈ G_c̃.
- (γ) C ⊄ {t = 0} and C is not a lift-curve. Then C ∖ (0,0) lies in q^{-1}(N_c) for a single coarse branch c, both sheets are sheets of lifts of c, and Σ′ = gΣ near the generic point of C, for some g ∈ Aut(Q) fixing C pointwise.

*Proof.*
- (β): C is a curve in Σ ∩ {t = 0}, hence a lifted branch (Lemma 2.1(b)). Lemma 2.2 gives the rest.
- (γ): near a generic point p of C with t(p) ≠ 0, the set q^{-1}(closure 𝓑) is q^{-1}(N_c) for the coarse branch c through q(p), because B_t ∩ U is a cone at Q_t. Its local components at p are permuted transitively by Stab(p), as in Lemma 2.2. So the local components of Σ and Σ′ at p satisfy ℓ′ = gℓ, g ∈ Stab(p). Generic points of C have a common stabiliser, so g fixes C pointwise, and Σ′ = gΣ by irreducibility.
- (α) is what remains, since C ⊂ q^{-1}(𝓑) and q^{-1}(𝓑) near (0,0) consists of 𝒥 and the sets q^{-1}(N_c). ∎

**Lemma 3.4 (label rules).** Let Y be non-constant.
- (α) If Σ, Σ′ share a lift-curve L and both are of boundary type, then P(Σ) = C(L) = P(Σ′).
- (β), (γ): P(Σ′) = σP(Σ), respectively gP(Σ).

*Proof.* (α) is Lemma 2.3. (β) and (γ) follow from Σ′ = σΣ and (K3). ∎

### 3.4 The failure trichotomy

Call a D-sheet *good* if it is of boundary type and x ∈ P.

**Lemma 3.5.**
- (β-fail) Suppose a (β)-edge joins a good Σ to Σ′ = σΣ that is not good. Then y := σ^{-1}x ≠ x. Along c̃ at t = 0, both x and y are intact and constant with value ≅ Y_0. On Σ (as on every sheet of the transported piece containing it), y is intact and constant with a value function ψ satisfying ψ(0) = Y_0 and [ψ] ≢ [Y]. In short: **the piece of c carries, at t = 0, a pair of twin constant vertices exchanged by the generic automorphism σ of its curves, and the deformation separates them.**
- (γ-fail) Suppose a (γ)-edge joins a good Σ to Σ′ = gΣ that is not good. Then for generic t and p ∈ C_t, the label y := g^{-1}x is a Y_t-copy at p that is IMOV along Σ_t at p. It is a moving vertex of the lifted family W ⊃ Π(Σ), and the point of K_W over p has y-coordinate ≅ Y_t. Moreover p → 0 as t → 0. That is, the transported piece has, for every small t ≠ 0, a self-crossing at a g-symmetric curve near Q_t, at which a moving vertex passes through Y_t; the crossing disappears into the cusp Q at t = 0.
- (ι-fail) Suppose an (α)-edge joins a good Σ to an interior-type sheet Σ′, and Σ′ contains a further lift-curve L′ with x ∉ C(L′). Then x is IMOV along Σ′_t at L(t) for generic t: Q_t is an interior point of the piece E′ of Σ′ (Q ∈ stratum(E′)), x is a moving vertex of E′, and F_x(L(t)) ≅ Y_t while F_x(L′(t)) ≇ Y_t.

*Proof.*
- (β-fail).
  - x ∉ σP(Σ) means y ∉ P(Σ); and y ≠ x since x ∈ P(Σ).
  - σ fixes c̃ pointwise, so F_y(p) = F_x(σp) = F_x(p) ≅ Y_0 for p ∈ c̃, and y is intact along c̃ because x is (σ maps L_x to L_{σx}).
  - The pattern is constant on Ñ_c̃, so y is intact on Σ. y is constant along c̃, hence constant on every fibre of the component W of the lifted boundary family that contains Π(Σ) (Lemma U, Cor. U1). Its value function ψ is holomorphic with ψ(0) = Y_0.
  - [ψ] ≢ [Y]: otherwise y ∈ P(Σ).
- (γ-fail).
  - At p ∈ C_t, g ∈ Stab(p), so y is intact at p and F_y(p) = F_x(gp) = F_x(p) ≅ Y_t.
  - Here p is a point of a transported punctured branch, so it is an interior point of its piece, and Theorem N applies with "interior" allowed. If y were STAY along Σ_t at p for uncountably many t, the argument of Lemma 2.3 would give y ∈ P(Σ), i.e. x ∈ P(Σ′). So y is IMOV, and by Lemma U, y ∈ M_W.
  - C is a curve germ through (0,0) not in {t = 0}, so p → 0 as t → 0.
- (ι-fail). x ∈ C(L) by Lemma 2.3 applied to Σ. Along Σ′_t at L(t), Theorem N gives STAY or IMOV. STAY would give, by the argument of Lemma 2.3 inside the irreducible Σ′, x intact with F_x ≡ Y_t on Σ′, hence x ∈ C(L′). So x is IMOV, which requires Q_t ∈ stratum of the piece, i.e. Σ′ is of interior type. ∎

**Theorem 3.6 (failure trichotomy for MS11; proved).** Assume MS11's setting, and suppose its conclusion fails for (Q, β̃, b̃, x). Then for every choice of X ⊃ S × {0}, the boundary D of X contains a configuration of type (β-fail) (possibly with c̃ = β̃), (γ-fail) or (ι-fail).

*Proof.*
- If no D-sheet of β̃ is good: the D-sheet of β̃ is σT with σ ∈ G_β̃ (Lemma 2.2) and x ∉ σP(T). Then T and σT are joined by the common t = 0 branch β̃, and this is (β-fail) with c̃ = β̃, applied to Σ = T. (T need not lie in D, but Lemma 3.5(β-fail) only uses Σ, σΣ and c̃.)
- Otherwise there is a good D-sheet. No D-sheet of b̃ is good, since MS11 fails (Proposition 2.4, item 1).
- 𝔊 is connected (Lemma 3.2), so some edge joins a good D-sheet Σ to a non-good D-sheet Σ′.
  - If it is a (β)- or (γ)-edge, Lemma 3.5 applies.
  - If it is an (α)-edge, Σ′ is not of boundary type (Lemma 3.4(α)). So Σ′ is of interior type, and x ∈ C(L) for the shared L.
  - If moreover x ∈ C(L′) for every lift-curve L′ ⊂ Σ′, then all boundary-type neighbours of Σ′ through (α)-edges are good. Replace Σ′ by the next sheet: the bad set is reached only through (β), (γ) or (ι)-fail edges.
  - Formally: let 𝔊_x be the set of good sheets together with the interior-type sheets all of whose lift-curves L′ have x ∈ C(L′). This is a non-empty proper subset of the vertices of 𝔊, so some edge leaves it. Checking the three types as above gives (β-fail), (γ-fail) or (ι-fail). ∎

**Comparison with the planner's sketch.**
- Steps 1–4 hold, with the correction of §3.1 and with (ι) added. The sketch omits the case where an (α)-edge passes through an interior-type sheet, where Theorem N allows IMOV.
- Step 5's sufficient condition, "every (β)- and (γ)-edge element fixes x", must be supplemented by "no (ι)-fail".
- Step 6's identification of the residual configurations with (B-pure) and same-branch crossings is consistent with Lemma 3.5:
  - (β-fail) is the τ = 0 trace of a (B)-type fixed locus, Fix(σ) ⊃ c̃;
  - (γ-fail) is the same-branch crossing at t ≠ 0;
  - (ι-fail) is an interior-MOV through the cusp of a non-product piece.

None of the three is excluded here.

---

## 4. The rigid twin at a MERGE / pMOV endpoint (new necessary condition)

**Lemma 4.1.** Assume MS11's setting, (Rig), Y non-constant, and moreover that at t = 0 the label x is MERGE along b̃ (some edge at x is unpinched on b̃) or pMOV along b̃ (x intact, F_x non-constant along b̃, Q not in the stratum of b). This is the situation at the chain's endpoint. Then for every lift-curve L′ contained in a transport sheet of b̃:

 F_x(p) ≅ Y_0 for all (p,t) ∈ L′  (independently of t).

Consequently, if MS11 fails there, then with L_1 as in Proposition 2.4 and a ∈ Aut(Q) with a b̃ ∈ Star(L_1) (so ax ≠ x):
- for every t, the curve Q_t has a component ≅ Y_t (label x at L_1(t)) and a different component ≅ Y_0 (label ax at L_1(t));
- these two components are exchanged at t = 0 by a^{-1} ∈ Aut(Q). Precisely, F_{ax}(0) = F_x(a^{-1}·0) = F_x(0).

In particular **Y_0 ∈ F′** (the finite (Rig)-set of classes of components of puncture values).

*Proof.*
1. Let T′ ⊃ L′ be a sheet of b̃, and let t be generic. Take p ∈ L′_t. The pattern on T′ equals that of b̃. Q_t is a puncture of the transported piece E_t of b, since strata are preserved.
2. **MERGE.** The vertex u ∋ x of E_t contains an unpinched edge. Its limit at p is the curve glued from the F_y(p), y ∈ u, which is nodal. So u is non-constant (Lemma C2 of PR-C), and that nodal curve is the puncture value f_u(p′), which lies in F by (Rig) (R8-8 Lemma 2). Hence [F_x(p)] ∈ F′.
3. **pMOV.** u = {x} is non-constant on E_0, hence x ∈ M_W for the component W of the lifted boundary family containing Π(T′), hence non-constant on every fibre (Lemma U). Its puncture value at p′ is F_x(p), which lies in F′ by (Rig).
4. So [F_x] takes values in the finite set F′ at all points of L′ over generic t. F_x is continuous on L′ (L′ ⊂ {all s_e = 0} ⊂ L_x), and the points over generic t are dense in the irreducible curve L′. Hence [F_x] is constant on L′, equal to [F_x(0)] = [Y_0]. Since M_{g_i,n_i} → M_{g_i,n_i}/S_{n_i} has finite fibres and F_x is continuous, F_x itself is constant up to the fixed relabelling.
5. For the consequence: a b̃ ∈ Star(L_1) means some sheet T″ of a b̃ contains L_1, so a^{-1}T″ is a sheet of b̃ containing a^{-1}L_1.
   - By 1–4, F_x ≡ Y_0 on a^{-1}L_1.
   - By (K3), F_{ax}(p) = F_x(a^{-1}p) for p ∈ L_1, so F_{ax} ≡ Y_0 on L_1.
   - Also F_x ≡ Y_t on L_1, and ax ≠ x because [Y] is non-constant.
   - Y_0 ∈ F′ by step 2 or 3 at t = 0 (or by closedness). ∎

**Remarks.**
- At the endpoint, the twin that takes over the network along b is the Y-copy x seen from the frame L_1. The copy that merges is a *rigid* copy, whose class is Y_0 for all t, not some other moving function. This sharpens R8-8 Prop. 3 (endpoint), which only gave a second copy with [φ] ≡ [Y] on the piece of b. Here, in the frame of L_1, we get a constant copy at the cusp point Q_t itself.
- So a counterexample would have two components of Q_t, one moving as Y_t and one frozen at Y_0, exchanged by an automorphism of Q_0. The frozen one is a component of a cusp value of a (Rig)-curve.
- This does not by itself contradict anything. Y_0 ∈ F′ is a t = 0 statement, whereas pinning needs Y_t ∈ F′ for t in an open set.

---

## 5. A local model for (β-fail)

The model shows that (β-fail) is compatible with every chart-and-family-local constraint used in the run. It concerns an edge configuration, not an entire V_0. All claims are direct computations.

**The model.**
- Coordinates (u, v, w) near 0 on a smooth 3-fold X ⊂ Def(Q) × Δ, with t = u + v.
- σ is an involution of Def(Q) acting on X by (u, v, w) ↦ (v, u, w) and preserving t.
- Two twin labels x, y = σx, exchanged by σ, with all their edges pinched on {uv = 0}: for those edges, s_e|_X = uv (σ swaps the edges e ↔ σe; both restrict to uv).
- An antisymmetric coordinate m_x − m_y = u − v (twin moduli difference), and a symmetric one m_x + m_y = 2Y_0 + (u + v)(…).
- w is the coordinate along the branch c̃ = {u = v = 0}.

**Checks.**
- D = X ∩ {N = 0} ⊇ {uv = 0} = Σ ∪ σΣ, with Σ = {u = 0} and σΣ = {v = 0}. Each is smooth, and on each, t-slices are w-lines (v = t on Σ). So these are transport sheets of c̃ with constant pattern; the pattern is constant on each sheet, as required.
- Σ ∩ σΣ = c̃ × {0} ⊂ {t = 0}: a (β)-edge.
- X_0 = {v = −u} is a smooth surface S′ with boundary c̃, and N|_{S′} vanishes to even order (s_e = −u²).
- σ acts on S′ as the reflection u ↦ −u, fixing only c̃. So the coarse V_0 near c is S′/σ, which is smooth (coordinate u²). This is consistent with V_0 smooth in the coarse space.
- On Σ: F_x − F_y = (u − v)|_{u=0} = −t, so F_x ≠ F_y for t ≠ 0. Choose F_x|_Σ = Y(t) and F_y|_Σ = ψ(t) := Y(t) + t(…). Then x ∈ P(Σ), y ∉ P(Σ), and on σΣ the roles are swapped. This is exactly (β-fail).
- Fix(σ) ∩ X = {u = v} is 2-dimensional. Its t-slices for t ≠ 0 are the curves {u = v = t/2}, with uv = t²/4 ≠ 0, i.e. *interior* σ-symmetric curves of V_t. They converge to c̃ at t = 0 and have no boundary points near Q_t. This is precisely R9-5's (B-pure).
- Theorem N holds at every time: at points of Σ_t, the Y_t-copy x is STAY along Σ_t. The copy y has value ψ(t) ≠ Y_t, so Theorem N says nothing about it.

**What a proof would have to exclude (heuristic, not proved).** In the model, V_0 approaches the boundary piece c along S′ with:
- plumbing parameter ≈ u² for the edges at the twins;
- twin moduli difference ≈ u.

That is, the two Y_0-regions are pinched at equal rates, while their conformal types differ at the order of the *square root* of the plumbing parameter.

For a totally geodesic V_0, the tangent direction ∂_u at points near c is dominated in Teichmüller norm by the plumbing part. Its norm is of order 1/(|u| log(1/|u|)) by (C) of PR-H §1.2, while the twin-difference part is O(1). The Teichmüller disc it generates is a "cusp disc" pinching the twin collars. One expects, for instance from Lemma PA and the flat-limit description (Fl), that along such a disc the conformal types of the intact zero-area components converge to their limit at a rate polynomial in the cusp parameter, *holomorphically* in it. In S′/σ the cusp parameter is u² up to a power. A twin difference ≈ u = (u²)^{1/2} would then require the cusp parameter's relevant power to be even, an arithmetic condition on the cylinder moduli of e and σe.

I have not been able to turn this into a contradiction. It is recorded as the most concrete lead for (β-fail).

---

## 6. Chain check

Re-checked, with no flaw found:
- Step 1 (Goal ⇐ MS8 + (Rig) + PR-A), and Proposition 1.1's converse.
- Step 2(c), the "Base" and the "(α)-type" propagation. Lemma 2.3 above gives a self-contained proof that persistence is a property of the sheet and equals C(L) for any lift-curve in it. This is the "component-wise" reading.
- Step 2(d), non-product endpoint. Given a sheet T of b̃ with x ∈ P(T), T ∩ {t = 0} ⊇ b̃ (Lemma 2.1(b) and Lemma 2.2: every sheet of b̃ contains b̃ × {0}), and x intact with F_x ≡ Y_0 along b̃ contradicts MERGE/MOV. (Lemma B1(a)'s "non-empty open subset" is in fact all of b̃ ∖ 0.)
- Step 2(c), "Transfer along D^{m+1}". A sheet T′ of β̃′_m maps under Π into one component W of the lifted boundary family, with W_0 ⊇ the lifted piece Ê of D^{m+1}.
  - W, being irreducible with W_0 ⊇ Ê, has a local component along Ê near the J_{m+1}-end. By Lemma 2.2 at J_{m+1}, this is the image of a sheet of β̃_{m+1}.
  - Persistence of the vertex u = Π-image of x_m holds on all of W (Lemma U, Cor. U1). So x_{m+1}, the label of u along β̃_{m+1}, is persistent on that sheet.
  - The step therefore holds *provided* the identification of x_m and x_{m+1} with the same vertex u of W is the one used by the walk (the "R(D) repair"). I did not re-audit that repair.
  - **Caution:** if Ê lies in two components W ≠ σ̄W (σ̄ ∈ Aut(G) fixing Ê pointwise), the transfer must use the sheet over W, not over σ̄W. Otherwise one lands in a (β-fail) configuration along D^{m+1}. Lemma 2.2 shows that a sheet over W exists, so the step is correct as long as "some sheet" is used throughout, as MS11 does.

Not re-checked: Prop K_w and the R(D) repair, Theorem X*_all (non-product), Lemma S̃′ (the (S) property via canonical lifts), and the cited inputs.

One point to watch in Lemma S̃′: V_0 smooth in the coarse M_g does not make its preimage in Def(J) locally irreducible at interior orbifold points. For example, {ab = 0} ⊂ C² is the preimage of a smooth curve under the swap (a,b) ↦ (b,a). So a lifted path can change lifted components at such points. The (S) property therefore really needs the canonical lift of the Teichmüller track (a lift through one smooth component of the preimage in T_g, reading (T4)), not an arbitrary path lift. As far as the task file states it, round10_q10 §6.3 uses canonical lifts, so I flag this only as a point to keep explicit.

---

## 7. Summary

**Proved here** (modulo the cited results of the run named in each proof, and Grothendieck's connectedness theorem, cited from memory):
1. Proposition 1.1: under (Rig), MS11 ⇔ the problem's claim.
2. Lemmas 2.1–2.3 and Proposition 2.4:
   - sheets contain lift-curves;
   - all sheets of a lifted branch form one orbit of its pointwise stabiliser;
   - P(Σ) = C(L) for every lift-curve L in a boundary-type sheet Σ;
   - MS11 in incidence form, with "MS11 up to an automorphism" always true.
3. Lemmas 3.1–3.5 and Theorem 3.6: Mechanism D written out, with:
   - the correction that the D-sheet of β̃ need not be the persistent one (absorbed into (β-fail));
   - the omitted (ι) case added.

   Failure of MS11 forces a (β-fail), (γ-fail) or (ι-fail) configuration in the boundary of any 3-fold component X ⊃ S × {0}.
4. Lemma 4.1 (rigid twin): at a MERGE/pMOV endpoint, failure forces Q_t to carry, for all t, both a Y_t-component and a component frozen at Y_0, exchanged at t = 0 by an automorphism of Q. In particular Y_0 ∈ F′.
5. §5: an explicit local model realising (β-fail), compatible with every local constraint used so far, including (B-pure).

**Not proved:** MS11, hence (by Prop. 1.1) the problem itself, under (Rig) or otherwise. No counterexample is given.

**Open questions (precise):**
- (Q1) (β-fail): can a boundary piece c of a smooth totally geodesic V_0 at a non-product cusp Q consist of curves with a generic automorphism σ exchanging two Y_0-components, with the sheet of V_0 along c being σ-reflected (as in §5: plumbing ≈ u², twin moduli difference ≈ u)? Lead: a Teichmüller-norm computation of the cusp discs tangent to ∂_u (§5, heuristic).
- (Q2) (γ-fail): can the transported piece self-cross, for every small t ≠ 0, at a g-symmetric curve near Q_t at which a moving vertex passes through Y_t, the crossing collapsing into Q at t = 0?
- (Q3) (ι-fail): can a non-product piece E′ with Q ∈ stratum(E′) carry, at Q_t, an interior-MOV of the Y_t-copy at one lift-curve but not at another?
- (Q4) Whether Lemma 4.1's rigid twin (a component of Q_t frozen at Y_0, which is a component of a cusp value of a (Rig)-curve) can be combined with total geodesy at t = 0 to force Y_t ∈ F′ for t near 0.
- (Q5) (Rig) (entry 82), untouched.

=== END OF ANSWER round11_q1 ===
