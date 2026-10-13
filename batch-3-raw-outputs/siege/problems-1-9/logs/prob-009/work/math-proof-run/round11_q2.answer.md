# round11_q2 — attempt on MS11

**Status line.** PARTIAL. MS11 is NOT proved and no counterexample is given. What this file establishes:
1. **A new gap in the chain (Gap C), with an explicit local model:** Lemma B1(a) and B1(b) of round10_q3 are false as stated. A transport sheet of a lifted branch b̃ need not contain b̃ × {0}. As a result, chain step 2(d) (endpoint) and the transfer step of 2(c) do not follow from MS11 as worded. **Repair:** restate MS11 with *anchored* sheets (sheets containing the lifted branch at t = 0). The resulting MS11ᵃ is what the chain actually needs, and the repaired chain uses only MS11ᵃ (§1).
2. **Mechanism D made rigorous as far as it goes** (§2). This covers the 3-fold X, the divisor D = X ∩ {N = 0}, the connectedness of the sheet graph (Grothendieck), the classification of adjacencies into three types, and the label-transport rule across each type.
3. **Reduction** (§3). In a precise form, MS11ᵃ is equivalent to a statement about the group elements produced along a path in the sheet graph. Three obstructions are named: (O1) the x-carrying sheet may lie outside X; (O2) D may contain interior-type sheets; (O3) adjacencies of types (β) and (γ) change labels by automorphisms that may move x. None of them is removed here.
4. Proved / not proved / open (§4).

Plan (written first): (1) check the definitions MS11 relies on (Lemma B1); (2) make the planner's Mechanism D rigorous; (3) reduce MS11 and isolate what is missing; (4) summary.

Readings (R1), (R2) with H_0 = id, (Rig), and "Y non-constant" are assumed throughout, as in MS11. Notation is that of the task file: Def(Q), the quotient map q, the smoothing coordinates s_e, N := ∏_e s_e, labels, F_y, Q_t = H_t(Q), lift-curves λ (the irreducible components of 𝒥 = {(p,t) : q(p) = Q_t}), and the sets P(T) and Λ(λ) of round10_q7 §1. The group Aut(Q) acts on B × Δ_ε by acting on the first factor. For a lifted branch c̃, Fix(c̃) denotes the pointwise stabiliser of c̃ in Aut(Q), and N_c := H((c ∖ Q) × Δ_ε).

---

## 1. Gap C: Lemma B1(a),(b) are false; anchored sheets

### 1.1 What B1 claims, and where its proof breaks
Lemma B1(a) (round10_q3 §2.2) states that every irreducible component Ñ¹ of Ñ = Ñ_b̃ satisfies: Ñ¹ ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0. Its proof asserts that "Ñ ∩ {t = 0} = b̃ ∖ 0". That assertion is unjustified. Ñ is a *connected component* of q^{-1}(N_b) ∩ (B × Δ_ε), and its t = 0 slice can contain other lifts a·b̃ (a ∈ Aut(Q)), because these can be connected to b̃ ∖ 0 through t ≠ 0.

### 1.2 Local model (proved, local)
**Coordinates and action.**
- Take coordinates (z, w, s, …) on Def(Q). Here s stands for the smoothing parameters s_e of the edges e in the pattern of b, so the b-stratum locus is {s = 0}. The coordinate z = s_{e′} is the smoothing parameter of one further edge e′ of G_Q, so the stratum of Q is {s = 0, z = 0}. The remaining coordinates are fixed at 0 throughout.
- An automorphism a ∈ Aut(Q) of order 2 acts by w ↦ −w and fixes z and s.
- Coarse coordinates are (z, u = w², s).

**The data at t = 0.**
- b is the coarse curve {u = z², s = 0}.
- Its lifts are b̃ = {w = z, s = 0} and a·b̃ = {w = −z, s = 0}. They are distinct, and Fix(b̃) = 1.
- Along b̃ ∖ 0 we have z = s_{e′} ≠ 0, so Q is a puncture of the piece of b, as (P) requires.

**The transport.** Put H_t(z, z², 0) := (z, (z − t)², 0). Then:
- H_t is a homeomorphism of b onto the curve b_t := {u = (z − t)², s = 0};
- Q = (0,0,0) is sent to Q_t = (0, t², 0), which lies in the stratum of Q;
- b ∖ Q is sent into the b-stratum {s = 0, z ≠ 0}.

So N_b = {u = (z − t)², s = 0, z ≠ 0} is a smooth surface germ, and all strata are respected.

**The preimage.**
- q^{-1}(N_b) = T₁ ∪ T₂ minus {z = 0}, where T₁ := {w = z − t, s = 0} and T₂ := {w = −(z − t), s = 0} = a·T₁.
- T₁ ∩ T₂ = C := {w = 0, z = t, s = 0}. Off t = 0 this curve lies in N_b's preimage, because z = t ≠ 0. So Ñ_b̃ = (T₁ ∪ T₂) ∖ {z = 0} is **connected**.
- Its t = 0 slice is (b̃ ∪ a·b̃) ∖ 0.
- The lift-curves are λ₋ = {z = 0, w = −t} ⊂ T₁ and λ₊ = {z = 0, w = t} ⊂ T₂.

**Conclusion of the model.** closure(Ñ_b̃) has exactly two irreducible components, T₁ and T₂.
- T₂ ∩ {t = 0} = a·b̃, which does not meet b̃ ∖ 0. This contradicts B1(a).
- Fix(b̃) = 1 does not act transitively on {T₁, T₂}. This contradicts B1(b).

The curve C consists of boundary points of V_t that have the extra automorphism a, and they converge to the cusp Q as t → 0. This is the same kind of degeneration as the (γ)-curves of §2.

Locally this model is compatible with (R1), (R2), (i) and (ii): the coarse family {u = (z − t)², s = 0} is a smooth, topologically trivial family of smooth curves, transported stratum by stratum. Whether it occurs for an actual totally geodesic V_0 is not decided here, just as for the models of round10_q3 §2.2 and round10_q7 §3.

### 1.3 Consequence for the chain
Suppose MS11's conclusion is given in the form "x is Y-persistent on some transport sheet T of b̃". In the model, T could be T₂, whose t = 0 fibre is a·b̃. Persistence on T₂ says only that x is intact along a·b̃ with F_x ≡ Y_0. Equivalently, a^{-1}x is intact along b̃ with F ≡ Y_0. That does not contradict MERGE or MOV *of x* along b̃.

So **chain step 2(d), non-product case, does not follow from MS11 as worded**. The step cites B1(a) exactly at this point. The transfer step of 2(c) (round10_q3 §2.2 item 3) also cites B1(a): it needs "the t = 0 slice of Ñ′¹ contains an arc of the track's lifted curve".

### 1.4 Repair: anchored sheets
**Definition.** An *anchored sheet* of a lifted branch c̃ is an irreducible component T of the germ at (0,0) of closure(Ñ_c̃) with c̃ × {0} ⊂ T.

**Lemma B1ᵃ (proved).**
- (a) Every transport sheet T of c̃ is a·T′ for some anchored sheet T′ of c̃ and some a ∈ Stab_{Aut(Q)}(Ñ_c̃).
- (b) Fix(c̃) permutes the anchored sheets of c̃ transitively.
- (c) P(gT) = g·P(T) for all g ∈ Aut(Q).

*Proof.*
- **(a) Step 1: closure(Ñ) ∖ 𝒥 = Ñ.** q^{-1}(H((c ∖ Q) × Δ_ε)) is the closed set q^{-1}(H(c × Δ_ε)) minus 𝒥, so it is closed in (B × Δ_ε) ∖ 𝒥. It is locally connected, so its connected components are closed in (B × Δ_ε) ∖ 𝒥. Hence closure(Ñ) ∖ 𝒥 = Ñ.
- **(a) Step 2: which lifts appear at t = 0.** 𝒥 ∩ {t = 0} = {0}. So T ∩ {t = 0}, which is a curve because t|_T is not constant, is a union of lifts a·c̃ with a·c̃ ∖ 0 ⊂ Ñ.
- **(a) Step 3: conclusion.** Then a(c̃ ∖ 0) ⊂ Ñ ∩ aÑ, so aÑ = Ñ, since both are connected components. So a^{-1}T is a component of closure(Ñ) containing c̃ × {0}.
- **(b)** Let p ∈ c̃ ∖ 0 be generic, so that Stab(p) = Fix(c̃).
  - N_c is a topological 4-manifold, so its germ at q(p) is irreducible (R7-4 Lemma 2(a), round10_q3). Hence the germ components of q^{-1}(N_c) at (p,0) are permuted transitively by Stab(p).
  - An anchored sheet is a global irreducible component that contains a germ component at (p,0). The identity principle gives one global component per germ component.
  - Fix(c̃) preserves Ñ, because it fixes c̃ ∖ 0.
- **(c)** This is (K3): F_{gy}(gp) ≅ F_y(p), and patterns are moved by g. ∎

**Repaired statement MS11ᵃ.** MS11 with "transport sheet" replaced by "anchored sheet" in both the hypothesis (x ∈ P(T) for some anchored sheet T of β̃) and the conclusion (x ∈ P(T′) for some anchored sheet T′ of b̃). By B1ᵃ(b),(c), the conclusion is equivalent to x ∈ Fix(b̃)·P(T′) for any one anchored sheet T′ of b̃.

**The chain with MS11ᵃ (checked).**
- *Base.* Δ_Γ is of product type, and by Lemma PT every element of Aut(Q) fixes the vertex. All components of q^{-1}(N_b) are Aut(Q)-translates of one another (N_b is irreducible), so persistence holds on every sheet, anchored or not.
- *Product-type junctions* (round9_q7 Lemma J and Cor. J′). They produce persistence on a germ component at a generic point of b̃. The global component containing that germ contains an open arc of b̃, hence b̃ (identity principle on the irreducible curve germ). So it is anchored.
- *Transfer along D^{m+1}* (round10_q3 item 3).
  - Start from an anchored Ñ′¹ ⊃ β̃′_m × {0}. Its t = 0 slice contains β̃′_m, which supplies the arc of E that the argument needs; this replaces the appeal to B1(a).
  - The component Ñ″¹ built at a generic p̃ ∈ β̃_{m+1} contains an arc of β̃_{m+1}, so it is anchored.
- *Non-product junctions and R(D)-points.* MS11ᵃ is used here.
- *Endpoint.* MS11ᵃ gives an anchored T ⊃ b̃ × {0} with x ∈ P(T). So x is intact along b̃ and F_x ≡ Y_0 there, which contradicts MERGE or MOV.

So the chain is correct with MS11ᵃ in place of MS11, and with MS11 as worded it is not. I found no other flaw in the parts of the chain I checked: steps (b), (c), (d) and the definitions they use. I did not re-derive Proposition K_w, Lemma PA, or the cited Teichmüller facts.

---

## 2. Mechanism D, made rigorous as far as it goes

### 2.1 The 3-fold and the divisor (proved)
**Lemma D1.**
- 𝒳 := q^{-1}(closure 𝒱) ⊂ B × Δ_ε is an analytic set of pure dimension 3 near (0,0).
- Some irreducible component X of its germ at (0,0) contains S × {0}.
- X ⊄ {N = 0}.
- D := X ∩ {N = 0} has pure dimension 2, and none of its components lies in {t = 0}.

*Proof.*
- **Pure dimension 3 and the component X.** closure(𝒱) is the closure of the 3-dimensional complex manifold 𝒱, and it is analytic by (R1). So it has pure dimension 3, and so does its preimage under the finite open map q × id.
- S × {0} is irreducible and lies in 𝒳, hence in some component X.
- **X ⊄ {N = 0}.** 𝒳 ∩ {N = 0} = q^{-1}(H(B_0 × Δ_ε)) has dimension 2, because H is a homeomorphism and B_0 × Δ has real dimension 4.
- **D.** By Krull, every component of D through (0,0) has dimension exactly 2. X ∩ {t = 0} ∩ {N = 0} lies in q^{-1}(B_0), which is 1-dimensional, so no component of D lies in {t = 0}. ∎

**Lemma D2 (components of D are anchored sheets).** Let T be a component of D, and let c̃ be a lifted branch with c̃ × {0} ⊂ T. Then T is an anchored sheet of c̃. In particular:
- the component of D containing β̃ × {0} is an anchored sheet T_β of β̃, since β̃ ⊂ S ⊂ X_0;
- likewise there is an anchored sheet T_b of b̃ in D.

*Proof.*
- T ∖ 𝒥 is connected: an irreducible germ minus a proper analytic subset, with suitable representatives.
- T ∖ 𝒥 lies in q^{-1}(H((B_0 ∖ Q) × Δ_ε)). That set is the disjoint union of the sets q^{-1}(N_c) ∖ 𝒥 over the branches c, which are closed in the complement of 𝒥.
- So T ∖ 𝒥 lies in one connected component, and that component meets c̃ ∖ 0. Hence it is Ñ_c̃, and T ⊂ closure(Ñ_c̃).
- T is 2-dimensional and irreducible, so it is a component of closure(Ñ_c̃), and it contains c̃ × {0}. ∎

### 2.2 Connectedness (proved, citing Grothendieck)
**Cited (from memory).** *Grothendieck's connectedness theorem* (SGA 2, Exp. XIII, Thm. 2.1; Hartshorne's form): if A is a complete local noetherian domain of dimension d, and f_1, …, f_r lie in the maximal ideal with d − r ≥ 2, then the punctured spectrum of A/(f_1, …, f_r) is connected.

**Transfer to the analytic germ.**
- O_{X,0} is an analytic local domain, hence excellent and henselian. Its normalisation is therefore local, and its completion is a domain.
- An irreducible analytic germ is unibranch, by the same argument. So the minimal primes of O_{D,0} = O_{X,0}/(N) correspond to the germ components of D, and they stay prime after completion.
- Two components D_a, D_b satisfy "P_a + P_b is not m-primary" iff dim(D_a ∩ D_b) ≥ 1.
- The punctured spectrum is connected iff the graph on minimal primes, with edges given by "not m-primary", is connected.

**Proposition D3.** Here d = 3 and r = 1. So the *sheet graph* is connected: its vertices are the components of D, and two components are adjacent when they share an irreducible curve germ C through (0,0). In particular there is a path T_β = U_0, U_1, …, U_m = T_b. ∎

### 2.3 Classification of adjacencies and label transport (proved)
Let U ≠ U′ be components of D sharing an irreducible curve germ C. Exactly one of the following holds.
- **(α)** C ⊂ 𝒥, i.e. C is a lift-curve λ. If U and U′ are both of boundary type, then P(U) = Λ(λ) = P(U′), by round10_q7 Lemmas I1 and I2. I re-checked them: I1 is formal; I2 uses R8-3 Theorem N at generic t, which needs (Rig) and Y non-constant.
- **(β)** C ⊂ {t = 0}. Then C = c̃ × {0} for a lifted branch c̃, U and U′ are both anchored sheets of c̃ (Lemma D2), and U′ = σU with σ ∈ Fix(c̃) (B1ᵃ(b)). Hence P(U′) = σP(U).
- **(γ)** Otherwise. Then C ⊄ 𝒥 ∪ {t = 0}, and U′ = gU with g ∈ Aut(Q) fixing C pointwise. Hence P(U′) = gP(U). The points of C ∖ (0,0) are boundary points of V_t, at t ≠ 0, that have the nontrivial automorphism g.

*Proof of the trichotomy and of (γ).*
- **The common branch.** Points of C ∖ 𝒥 lie in U ∖ 𝒥 ⊂ Ñ_c and in U′ ∖ 𝒥 ⊂ Ñ_{c′}. These are components of the disjoint union above, so c = c′ and U, U′ ⊂ q^{-1}(N_c).
- **Local transitivity.** Take p ∈ C ∖ 𝒥 with t(p) ≠ 0 generic, so Stab(p) = Fix(C). The germ of N_c at q(p) is irreducible (a topological 4-manifold). So Stab(p) permutes transitively the germ components of q^{-1}(N_c) at p.
- **Conclusion.** Some g ∈ Fix(C) maps a germ component of U at p onto one of U′. By the identity principle gU = U′.
- **g ≠ 1.** U ≠ U′. Since g fixes p, the stable curve over p has the automorphism g.
- **(β).** It is the same argument at a generic p ∈ c̃ ∖ 0. ∎

Example. In the model of §1.2, T₁ and T₂ are adjacent of type (γ) along C, with g = a.

---

## 3. The reduction, and what blocks it

### 3.1 Reduction (proved)
**Proposition R.** Assume the setting of MS11ᵃ. Let X, D, T_β, T_b be as in §2, and let U_0, …, U_m be a path from T_β to T_b in the sheet graph. Suppose all U_k are of boundary type. Then:
- P(T_b) = h·P(T_β), where h ∈ Aut(Q) is the ordered product of the elements σ or g attached to the (β)- and (γ)-steps of the path;
- if moreover x ∈ P(T_β) and x ∈ Fix(b̃)·h·x, then MS11ᵃ's conclusion holds.

*Proof.* Compose the rules of §2.3 along the path, and use B1ᵃ(b),(c). ∎

**Corollary R′ (a sufficient condition; partial).** MS11ᵃ holds when all three of the following hold:
- the anchored sheet of β̃ carrying x lies in X (as in Proposition R);
- every component of D is of boundary type;
- every element of Aut(Q) fixing pointwise a curve germ C ⊂ D that is a (β)- or (γ)-adjacency fixes x.

This is again a no-twin-type hypothesis. It does NOT answer the question.

### 3.2 The three obstructions (not removed)
- **(O1) The x-carrying sheet may lie outside X.**
  - By B1ᵃ(b), the anchored sheets of β̃ form one Fix(β̃)-orbit. The one carrying x is σT_β with σ ∈ Fix(β̃), so σ^{-1}x ∈ P(T_β).
  - If σ moves x, the path argument in X starts from σ^{-1}x.
  - Using σX instead of X does not help: σX contains σS ⊃ β̃, but σS need not contain b̃.
  - This is the planner's (F2) in sheet language.
- **(O2) Interior-type sheets.**
  - X_0 may contain components S′ ≠ S of q^{-1}(closure V_0) that contain a lifted branch c̃ of a piece with Q in its stratum. By Theorem X\*_all, such an S′ has no other boundary curve, but nothing removes S′ from X_0.
  - The anchored sheet of c̃ is then of interior type, and Lemma I2 is unavailable at (α)-steps through it.
  - A path in the sheet graph may be forced through such sheets.
- **(O3) Label-changing adjacencies.**
  - (β)-steps use elements of Fix(c̃), and (γ)-steps use elements fixing a curve of symmetric boundary curves at t ≠ 0 that converges to the cusp.
  - Neither is controlled by chart-local data: the models of §1.2, round10_q3 §2.2 and §3.3, and round10_q7 §3 realise them.
  - The planner's hope that total geodesy enters at (β)-steps (Lemma TG: Fix(σ) ∩ S is S, a Teichmüller disc, or c̃ alone) does not by itself show that σ fixes x. The model of round10_q3 §3.3 has σ-fixed loci of exactly the allowed kinds and a σ moving x.
  - For (γ)-steps, total geodesy at t = 0 is invisible, because C meets {t = 0} only at (0,0).
- **Why a further idea is needed.** By the Γ-symmetry no-go of round10_q7 §2 (re-checked, it applies verbatim to D), every quantity built from D and the P(U) is equivariant under the elements h above. So connectedness of D alone cannot decide whether h fixes x. Some input that breaks the symmetry is needed, such as the position of the walk's track, which is not Aut(Q)-invariant. I did not find one.

---

## 4. Summary

**Proved here** (modulo the cited facts: Grothendieck's connectedness theorem, excellence and henselianity of analytic local rings, Krull, irreducibility of topological-manifold germs, and the prior lemmas I1, I2 and Theorem N, which I re-checked as used):
1. **Gap C.** Lemma B1(a),(b) of round10_q3 are false: there is an explicit local model (§1.2) with a transport sheet of b̃ whose t = 0 fibre is a·b̃ ≠ b̃, and with Fix(b̃) = 1 not transitive on the sheets. Consequently chain step 2(d) and the transfer step 2(c) do not follow from MS11 as worded.
2. **Repair.** Lemma B1ᵃ for anchored sheets, and the restated MS11ᵃ. The chain goes through with MS11ᵃ: base, product-type junctions, transfer, and endpoint were all checked.
3. **Mechanism D** (Lemmas D1, D2; Proposition D3; the classification of adjacencies (α), (β), (γ) with their label rules).
4. **Proposition R / Corollary R′.** A reduction of MS11ᵃ to a group-element condition along a path, and a sufficient condition. This is partial: it is of no-twin type.

**Not proved:** MS11, and MS11ᵃ. No counterexample is given. By round10_q3 Prop. 1.1, a counterexample would disprove the problem for (Rig)-families.

**Open (precise):**
- (Q1) MS11ᵃ in general. Equivalently, remove (O1), (O2) and (O3) of §3.2: show that along some path from T_β to T_b (allowing the Fix(β̃)-translate of the x-carrying sheet) the composite element h satisfies x ∈ Fix(b̃)·h·x, or handle the interior-type sheets.
- (Q2) Whether configurations like §1.2 (a curve of symmetric boundary curves of V_t converging to the cusp, making a sheet of b̃ unanchored) occur for smooth totally geodesic V_0.
- (Q3) Entry 82, (Rig), still needed by the chain.
- (Q4) The inputs inherited from earlier rounds (Proposition K_w's marking details, Lemma PA, (Fl), (T4)) are not re-proved here.

=== END OF ANSWER round11_q2 ===
