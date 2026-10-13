# round13_q10 — the conditional theorem "(R1) + (R2^orb) ⇒ Y_t = Y_0", written out

**Plan/status line.** I read the brief and the spliced parts I rely on: round12_q9 in full (§§1–8), round11_q1 §§1–2, round11_q7 §§0–4, round11_q3 §§1–3, and round11_q9 §§2.8, 3–6. Below:
- §0 gives the readings and the precise statement.
- §§1–5 give Steps 1–5 of the derivation.
- §6 treats (L→G); §7 treats (Reading); §8 gives the verdict and the list of inputs.

**Main new observation (Step 4).** If the lift locus at Q is a single curve L, then *every* anchored sheet of *every* lifted branch through 0 contains L. Persistence is then read off L (round11_q1 Lemma 2.3). So MS11♭ holds at Q outright, without (S), without β̃ ≠ b̃, and without any analysis of twins.

Step 3 shows that under (R2^orb) the lift locus is a single curve at every Q that is a puncture of some piece. The mechanism is that (c) forces |Aut(Q_t)| = |Aut(Q)|.

**Verdict.**
- The derivation is complete *relative to* the run's prior results listed in §8.2 (the walk chain of round11_q9, Theorem N of R8-3, TV/Φ̂ of round8_q10, Imayoshi–Shiga, …). I did not re-prove those; I re-checked only the parts I quote.
- (L→G) is **proved** for the natural chart-level local reading (Loc) of §6. So the global form (a)–(d) is not an extra assumption beyond (Loc).

---

## 0. Readings, notation, statement

- **(R1)** closure(𝒱) ⊂ M̄_g × Δ is a closed analytic set whose fibre over t is closure(V_t).
- **(R2)** H : closure(V_0) × Δ → closure(𝒱) is a homeomorphism over Δ with:
  - H smooth on V_0 × Δ;
  - H maps (closure(V_0) ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum (the open one included);
  - H_0 = id.
- **(R2^orb)** (round12_q9 §1). (R2) holds, and for every boundary stratum G there is a continuous H̃ = H̃^G : Ã_0 × Δ → T_G with:
  - (a) ξ_G∘p∘H̃_t = H_t∘ξ_G∘p on Ã_0;
  - (b) H̃_t(gx) = gH̃_t(x) for all g ∈ Mod_G;
  - (c) Stab_{Mod_G}(H̃_t x) = Stab_{Mod_G}(x);
  - (d) H̃_0 = id.

  Here T_G = ∏_w T_w, p : T_G → ∏_w M_w, ξ_G : ∏_w M_w → Δ_G, A_t = closure(V_t) ∩ Δ_G, and Ã_t = (ξ_G∘p)^{-1}(A_t).

**Convention on Mod_G (made explicit here, used in Step 3).**
- Mod_G is the group of pairs (σ, (φ_w)_w), where:
  - σ ∈ Aut(G) is an automorphism of the stable graph, *including its action on half-edges* (so it may exchange the two branches of a node);
  - φ_w is an isotopy class of orientation-preserving homeomorphisms from the reference surface of w to that of σ(w), carrying the special point labelled by a half-edge h to the one labelled σ(h).
- It contains ∏_w Mod_w (pure, labelled) with finite index, and [T_G/Mod_G] = Δ_G. Its point stabilisers are computed in Lemma 3.2.

**Notation at a point Q.**
- Def(Q) is the Kuranishi space of Q, with plumbing coordinates s_e.
- q : Def(Q) → Def(Q)/Aut(Q) ⊂ M̄_g; B ⊂ Def(Q) is a small Aut(Q)-invariant ball; ε > 0 is small.
- B_t := closure(V_t) ∖ V_t, and Q_t := H_t(Q).
- 𝒥 := {(p,t) ∈ B × Δ_ε : q(p) = Q_t} is the lift locus. Its irreducible components through (0,0) are the lift-curves.
- Ñ_c̃, anchored sheets, P(T), C(L), labels, F_x and "Y-persistent" are as in the brief.

**Theorem (conditional).** Assume the hypotheses of the problem, read as (R1) and (R2^orb). Assume also the run's prior results listed in §8.2. Then Y_t = Y_0 for all t ∈ Δ.

(If dim M_{g_i,n_i} = 0 there is nothing to prove, so assume dim M_{g_i,n_i} > 0.)

---

## 1. Step 1: (R2^orb) ⇒ (R2), and what (R2^orb) adds

As formalised, (R2^orb) contains (R2) verbatim: H̃ is a lift of the H of (R2). So the implication is trivial.

What (R2^orb) adds is, for every boundary stratum G, a continuous lift of the transport H_t|_{A_0} to Teichmüller space with three properties:
- it is equivariant for the full stratum group Mod_G;
- it starts at the identity;
- it does not change point stabilisers.

Three consequences are used below.
1. **Isotropy is transported** (from (a) and (c), Lemma 3.2): for every Q ∈ B_0 in the stratum G and every t, Aut(H_t(Q)) ≅ Aut(Q). The coarse reading (R2) gives nothing of this kind.
2. **Descended transport** (round12_q9 Lemma 1.1, from (a), (b), (c)): a homeomorphism Π_t : Â_0 → Â_t on the level of ∏_w M_w, which maps pieces to pieces. Under (R2) alone this exists only for product-type strata.
3. **Transport of the joint Teichmüller lift of each piece** (round12_q9 Prop. T, from (a), (b), via Lemma CL).

---

## 2. Step 2: (R2^orb) ⇒ (Rig), by Theorem RO

Theorem RO (round12_q9 §6), with its proof taken as given per the brief, has these hypotheses:
- (R1) and (R2);
- (R2^orb) in the form (a)–(d);
- Theorem TV and Corollary Φ̂ of round8_q10 (prior results, not re-checked);
- Imayoshi–Shiga finiteness (cited from memory, with the scope caveat of round12_q9 §6).

I checked where (a)–(d) enter its proof.
- **Lemma 1.1.**
  - Descent to Π_t uses (b) for Mod_Π ⊂ Mod_G.
  - Π_t lands in Â_t by (a), together with H_t(A_0) = A_t from (R2).
  - Injectivity uses (c): if H̃_t x = gH̃_t y = H̃_t(gy), then (a) and the injectivity of H_t give gy ∈ Mod_G·x, and (c) then gives equality in Ã_0.
  - Surjectivity uses (a) and (b).
  - Continuity of Π_t uses continuity of H̃ and openness of p. Continuity of Π_t^{-1} uses properness of ξ_G.
  - "Pieces to pieces" is topological.

  I re-checked these lines and they are correct.
- **Prop. T** uses (a) through Lemma 1.1, and (b) for g ∈ Mod_Π. Lemma CL then gives holomorphy.
- **(d)** is used to start the transported orbifold at h̃_0 = id. It also gives F_0 = F at t = 0.

These are exactly the properties (R2^orb) provides. So Theorem RO applies and gives **(Rig)**: there is a finite set 𝒦 of triples (G, M, K) such that every piece at every time has its triple in 𝒦. In fact K(E_t) = K(E_0), and M(E_t) = M(E_0).

Two remarks.
- (Rig) is a hypothesis of MS11♭ and of MS8, and it enters Theorem N (R8-3), which is used in Step 4.
- Theorem RO also covers non-product strata. This matters because the chain's MS11♭ invocations happen at non-product points.

---

## 3. Step 3: under (R2^orb) the lift locus at a puncture point is one curve

Throughout this section, Q ∈ B_0 and G := G_Q. Q is a **puncture point**: some branch β of B_0 at Q satisfies β ∖ Q ⊂ Δ_{G_β} with G_β ≠ G. This is exactly (P) for β. Every Q at which the chain invokes MS11♭ is a puncture point.

Choose a neighbourhood U of Q such that B_0 ∩ U = c_1 ∪ ⋯ ∪ c_m, the branches at Q, where each c_k ∖ Q is a smooth punctured disc and these are pairwise disjoint. Put
- 𝓑 := closure(𝒱) ∖ (M_g × Δ) = H(B_0 × Δ) (by (R2)), a closed analytic set by (R1);
- Γ_Q := H({Q} × Δ) = {(Q_t, t)};
- N_c := H((c ∖ Q) × Δ_ε).

### Lemma 3.1 (t ↦ Q_t is holomorphic). Proved; uses only (R1), (R2) and (P).
For ε small, t ↦ Q_t is a holomorphic map Δ_ε → M̄_g. Hence 𝒥 is a closed analytic subset of B × Δ_ε.

*Proof.*
1. Near (Q,0) the set 𝓑 is H((c_1 ∪ ⋯ ∪ c_m) × Δ_ε), by continuity of H and H^{-1}. It is the disjoint union of Γ_Q and the sets N_{c_k}.
   - Each N_{c_k} is connected, and it is a topological 4-manifold, since (c_k ∖ Q) × Δ_ε is.
   - Each N_{c_k} is open in 𝓑 ∖ Γ_Q.
2. Let W_1, …, W_r be the irreducible components of the germ of 𝓑 at (Q,0). Each has dimension ≤ 2, and since 𝓑 has topological dimension 4 near (Q,0) at the points of N_{c_k}, the 2-dimensional ones cover 𝓑 near (Q,0).
   - A 1-dimensional component would lie in the nowhere dense set Γ_Q: points of N_c have 4-manifold neighbourhoods, and by invariance of domain they cannot lie on a 1-dimensional component sticking out. So it would be contained in Γ_Q and is irrelevant below.
3. Fix a 2-dimensional W_j, with a small representative whose regular part Reg(W_j) is a connected complex 2-manifold. This holds for irreducible germs (standard, cited).
   - The closed subset (Γ_Q ∪ ⋃_{i≠j} W_i) ∩ Reg(W_j) has topological dimension ≤ 2: Γ_Q is homeomorphic to a disc, and W_i ∩ W_j is analytic of dimension ≤ 1.
   - Such a set does not disconnect the connected 4-manifold Reg(W_j) (Hurewicz–Wallman, cited from memory).
   - So the complement is a connected subset of 𝓑 ∖ Γ_Q = ⊔_k N_{c_k}, and it lies in a single N_{c_k}.
   - Its closure is W_j, so W_j ⊂ closure(N_{c_k}) = H(c_k × Δ_ε).
4. Conversely, every point of N_{c_k} lies on some W_j. That W_j lies in H(c_{k′} × Δ) for a single k′, and N_{c_k} ∩ H(c_{k′} × Δ) = ∅ unless k′ = k.
   - Hence H(c_k × Δ_ε) = closure(N_{c_k}) is the union of the W_j it contains.
   - In particular H(β × Δ_ε) is a closed analytic set near (Q,0).
5. Near Q, β ∩ Δ_G = {Q}, because β ∖ Q ⊂ Δ_{G_β} with G_β ≠ G. H is stratum-preserving by (R2), so
   Γ_Q = H(β × Δ_ε) ∩ (Δ_G × Δ_ε) near (Q,0).
   Since Δ_G coincides near Q with the closed analytic set closure(Δ_G), Γ_Q is a closed analytic curve germ.
6. The projection t : Γ_Q → Δ_ε is a homeomorphism.
   - So Γ_Q is irreducible and locally irreducible.
   - Its normalisation ν : Γ̂ → Γ_Q is bijective.
   - t∘ν is a bijective holomorphic map between smooth curves, hence biholomorphic.
   - Therefore t ↦ Q_t = ν((t∘ν)^{-1}(t)) is holomorphic.
7. Finally, 𝒥 = (q × id)^{-1}(Γ_Q) ∩ (B × Δ_ε) is analytic. ∎

### Lemma 3.2 (stabilisers in Mod_G are the automorphism groups). Proved.
Let x̂ ∈ T_G and let Z := ξ_G p(x̂) be the corresponding stable curve. Then Stab_{Mod_G}(x̂) ≅ Aut(Z), canonically.

Let K_G be the kernel of the action Mod_G → Aut(T_G). Then:
- K_G ⊂ Stab(x̂) for every x̂;
- the effective stabiliser is Stab(x̂)/K_G.

*Proof.* Write x̂ = (C_w, f_w)_w, with C_w a pointed Riemann surface of type (g_w, n_w) and f_w a marking. Then Z is obtained by gluing, for each edge e = {h, h′}, the point labelled h to the point labelled h′.

**From stabilisers to automorphisms.**
- g = (σ, (φ_w)) fixes x̂ iff for each w there is a biholomorphism α_w : C_w → C_{σw} with α_w∘f_w isotopic to f_{σw}∘φ_w, carrying the point labelled h to the point labelled σ(h).
- Each α_w is unique, since a biholomorphism of a stable pointed surface isotopic to the identity is the identity.
- Since σ preserves the pairing of half-edges into edges, ⊔_w α_w descends to an automorphism α(g) of Z.
- So g ↦ α(g) is a homomorphism.

**Injective.** If α(g) = id, then the induced map on the normalisation ⊔C_w is the identity. It fixes each component and each preimage of each node, so σ = id on vertices and on half-edges. Then α_w = id, so φ_w is trivial in Mod_w.

**Surjective.** Let α ∈ Aut(Z).
- α lifts to the normalisation ⊔C_w. It permutes the components and the preimages of nodes, respecting the pairing, and so defines σ ∈ Aut(G), with its action on half-edges, and biholomorphisms α_w.
- Put φ_w := [f_{σw}^{-1}∘α_w∘f_w]. Then g = (σ, (φ_w)) ∈ Mod_G fixes x̂, and α(g) = α.

**The kernel.** An element of K_G fixes every point, which gives the first claim. The second is the definition of the effective stabiliser. ∎

*The cases named in the brief.*
- Automorphisms that act trivially on the stratum lie in K_G. Examples: the elliptic involution of a (1,1)- or (1,2)-component, or the hyperelliptic involution of a (2,0)-component, extended by the identity.
- They are nevertheless genuine automorphisms of Z. They can act non-trivially on Def(Z) through the plumbing coordinates: the elliptic involution of a (1,1)-tail acts by s_e ↦ −s_e.
- Lemma 3.2 counts them in Stab(x̂) and in Aut(Z) alike. So (c) controls the whole of Aut(Z), not only its effective image on the stratum.
- If one reads (c) "modulo generic automorphisms", i.e. as equality of the images in Mod_G/K_G, then (c) for the full stabilisers follows. Both stabilisers contain K_G, so a subgroup containing K_G is determined by its image.
- So no strengthening of (c) is needed. Theorem RO is unaffected, since it uses (c) only through Lemma 1.1, where the two readings coincide.

### Cited fact (Kur) (from memory; Deligne–Mumford; Arbarello–Cornalba–Griffiths, *Geometry of algebraic curves II*, Ch. XI)
Let Q be a stable curve and B ⊂ Def(Q) a sufficiently small Aut(Q)-invariant ball. Then:
- B/Aut(Q) → M̄_g is an open embedding of analytic spaces;
- for every p ∈ B, restriction gives an isomorphism Stab_{Aut(Q)}(p) ≅ Aut(X_p), where X_p is the fibre of the Kuranishi family.

Here Aut(Q) acts on Def(Q), possibly non-faithfully: in genus 2 the hyperelliptic involution acts trivially.

### Proposition 3.3 [orb] (one lift-curve). Proved.
Let Q be a puncture point. For ε and B small, there is a holomorphic map p : Δ_ε → B with q^{-1}(Q_t) ∩ B = {p(t)} for every t ∈ Δ_ε, and p(0) = 0. Hence:
- 𝒥 = {(p(t), t)} is a smooth irreducible curve, and it is the only lift-curve L;
- Aut(Q_t) ≅ Aut(Q) for all t ∈ Δ.

*Proof.*
1. **Isotropy is preserved.** Let x̂ ∈ Ã_0 lie over Q (with G = G_Q) and put ŷ := H̃_t(x̂).
   - By (a), ŷ lies over H_t(Q) = Q_t ∈ Δ_G.
   - By Lemma 3.2 and (c): Aut(Q_t) ≅ Stab_{Mod_G}(ŷ) = Stab_{Mod_G}(x̂) ≅ Aut(Q).
   - So |Aut(Q_t)| = |Aut(Q)| for all t.
2. **Fibre size.** For |t| < ε we have Q_t ∈ q(B), by continuity of t ↦ Q_t (Lemma 3.1).
   - Since B is Aut(Q)-invariant, q^{-1}(Q_t) ∩ B is one Aut(Q)-orbit.
   - Its cardinality is |Aut(Q)| / |Stab_{Aut(Q)}(p)| for any p in it.
   - By (Kur), Stab_{Aut(Q)}(p) ≅ Aut(X_p) ≅ Aut(Q_t), which has the order of Aut(Q) by item 1.
   - So the orbit is one point p(t), fixed by all of Aut(Q). Also p(0) = 0.
3. **Regularity.**
   - p is continuous: its graph (q × id)^{-1}(Γ_Q) ∩ (B̄′ × Δ_ε) is closed, and q is proper on a smaller closed invariant ball B̄′.
   - p is a continuous lift of the holomorphic map t ↦ Q_t (Lemma 3.1) through B → B/Aut(Q).
   - By round12_q9 Lemma CL, p is holomorphic. That lemma applies to a properly discontinuous action of a countable group; here the finite group Aut(Q), or its effective quotient, which has the same orbits, acts on the ball B. Its proof re-checked.
   - So 𝒥 is the graph of p: a smooth curve, irreducible, and the unique lift-curve. ∎

*Remark.* Item 1 holds for every Q ∈ B_0. Lemma 3.1, and so analyticity of 𝒥, used (P) at Q. Every invocation of MS11♭ in the chain has (P), for both branches.

---

## 4. Step 4: one lift-curve at Q ⇒ MS11♭ at Q

**Germ conventions.** All statements are about germs at (0,0) ∈ Def(Q) × Δ. The chain allows shrinking B and ε finitely many times (round11_q9 §3, last item). The reason is that an anchored sheet for smaller (B′, ε′) lies in an anchored sheet for (B, ε), and persistence passes between them by the identity principle.

I re-check that reason. Ñ′_c̃ ⊂ Ñ_c̃, so an anchored sheet T′ for (B′, ε′) lies in a component T of closure(Ñ_c̃). That T contains an open piece of c̃ × {0}; since T is closed and c̃ is irreducible, T contains c̃ × {0}, so T is anchored. Finally, {x is intact with F_x ≅ Y_t} ∩ T is analytic (R8-3 Lemma 1, using entry 19) and contains the 2-dimensional T′, so it is all of T.

So I take B and ε small enough for Prop. 3.3 and for the chain's conditions simultaneously.

**Facts on transport families (R7-4 Lemma 2; round11_q7 D1(c), re-checked).**
- Near (Q,0), H(B_0 × Δ_ε) = Γ_Q ⊔ ⊔_c N_c, and each N_c is open and closed in the complement of Γ_Q.
- So q^{-1}(N_c) is analytic in (B × Δ_ε) ∖ 𝒥, and Ñ_c̃, a connected component of it, is analytic there.
- closure(Ñ_c̃) is analytic of pure dimension 2 (R7-4 Lemma 2(c)), and closure(Ñ_c̃) ⊂ Ñ_c̃ ∪ 𝒥 near (0,0).

### Lemma 4.1 (anchored sheets exist and contain a lift-curve). Proved.
Let c̃ be a lifted branch at 0 of a branch c of B_0 at Q.
- (a) c̃ has an anchored sheet.
- (b) Every anchored sheet T of c̃ contains a lift-curve. In particular, under the conclusion of Prop. 3.3, L ⊂ T.

*Proof.*

(a) Since c̃ ∖ 0 ⊂ Ñ_c̃ (at t = 0), we get c̃ × {0} ⊂ closure(Ñ_c̃). The irreducible curve c̃ × {0} lies in the union of the finitely many irreducible components of closure(Ñ_c̃), hence in one of them.

(b) **Setting up.**
- T ⊄ {t = 0}: its generic points lie in Ñ_c̃, which has 1-dimensional t-slices. So t is non-constant on T, and T_s := T ∩ {t = s} has pure dimension 1 for small s ≠ 0, by Krull.
- Pick (p_n, t_n) ∈ T ∖ 𝒥 with t_n ≠ 0 and (p_n, t_n) → (0,0). If no such points exist, then T ⊂ 𝒥 ∪ {t = 0}, which is impossible for dimension reasons.
- Then q(p_n) ∈ H_{t_n}(c ∖ Q). Put z_n := H_{t_n}^{-1}(q(p_n)) ∈ c ∖ Q. Since H^{-1} is continuous and H(Q,0) = (Q,0), we have z_n → Q.
- Let α_n ⊂ c be the arc from z_n to Q. By uniform continuity of H on compacta, H_{t_n}(α_n) ⊂ q(B″) for large n, where B″ ⋐ B is a smaller invariant ball.

**The image of a component reaches Q_{t_n}.**
- Let C be an irreducible component, through p_n, of the curve T_{t_n} (taken in a fixed representative of T in B × Δ_ε). Then q(C) is an irreducible analytic curve contained in Z := B_{t_n} ∩ q(B), by Remmert, since q|_B is finite.
- At every point w ∈ H_{t_n}(α_n ∖ Q), the curve Z is a topological 2-manifold near w: H_{t_n} is a homeomorphism B_0 → B_{t_n}, and B_0 is a smooth disc near H_{t_n}^{-1}(w) ∈ c ∖ Q. So Z is locally irreducible at w. (If the germ had k ≥ 2 branches, a small punctured neighbourhood would have k ≥ 2 components.)
- Let O be the set of w ∈ H_{t_n}(α_n ∖ Q) near which q(C) contains a neighbourhood of w in Z.
  - O is non-empty: it contains q(p_n), since q(C) contains a curve germ there and Z is locally irreducible there.
  - O is open in the arc.
  - O is closed in the arc: if w ∈ closure O, then w ∈ q(C), and the 1-dimensional germ of q(C) at w lies in the irreducible germ Z_w, hence equals it.
- So O is the whole connected arc H_{t_n}(α_n ∖ Q). Since q(C) is closed in q(B), Q_{t_n} ∈ q(C).

**Conclusion.**
- So C, and hence T, contains a point (p′_n, t_n) with q(p′_n) = Q_{t_n}, i.e. (p′_n, t_n) ∈ T ∩ 𝒥.
- Since q^{-1}(Q) ∩ B = {0} and q is proper, p′_n → 0. So the analytic germ T ∩ 𝒥 at (0,0) is not just the point, and it contains a curve germ.
- A curve germ inside the curve 𝒥 is an irreducible component of 𝒥's germ, i.e. a lift-curve.
- Under Prop. 3.3, 𝒥 = L, so L ⊂ T. ∎

This re-proves round11_q1 Lemma 2.1(c) for anchored sheets. The line "every irreducible curve of Σ_t lies in a lift of a punctured branch …" in the original is made precise by the arc argument above.

### Lemma 4.2 (persistence is read off the lift-curve). Proved, given Theorem N (R8-3) and entry 19.
Assume Y is non-constant and (Rig) holds. Let T be an anchored sheet of a lifted branch c̃ with (P), i.e. Q is not in the stratum G_c of c ∖ Q. Let L ⊂ T be a lift-curve. Then P(T) = C(L).

*Proof.* (This re-checks round11_q1 Lemma 2.3.)
- **⊆.** If x is intact with F_x ≅ Y_t at every point of T, the same holds on L ⊂ T.
- **⊇: one slice.** Let y ∈ C(L). Let t ∉ Z ∪ {0} be small, where Z is the countable exceptional set of (TN) (round11_q7 §0). Let (p,t) ∈ L.
  - T_t has pure dimension 1 at p (Lemma 4.1(b), first point), so it has a curve germ γ at p.
  - Near (0,0), T ⊂ Ñ_c̃ ∪ 𝒥, and 𝒥 ∩ {t} is finite. So γ ∖ p ⊂ q^{-1}(H_t(c ∖ Q)), and γ is a lifted branch of B_t at the lift p of Q_t.
  - Its coarse piece lies in Δ_{G_c}, because H_t preserves strata. Also Q_t ∈ Δ_{G_Q} ≠ Δ_{G_c}, so Q_t is not in the stratum of that piece.
  - y is a Y_t-copy at p, since y ∈ C(L). By (TN), y is intact along γ, and STAY or IMOV holds. IMOV requires Q_t to be in the stratum of the piece, so STAY holds: F_y ≡ Y_t along γ.
- **⊇: all of T.** The set A_y := {(p′,t′) ∈ T : y intact at p′, F_y(p′) ≅ Y_{t′}} is closed analytic in T (R8-3 Lemma 1; uses entry 19, holomorphy of t ↦ [Y_t]).
  - A_y contains a curve germ inside the slice {t} for uncountably many t.
  - An analytic set of dimension ≤ 1 has countably many irreducible components, each either contained in one slice or finite over Δ. So it meets only countably many slices in curves.
  - Hence dim A_y = 2, and A_y = T because T is irreducible. So y ∈ P(T). ∎

### Proposition 4.3 [orb] (MS11♭ holds at every puncture point). Proved, given (TN), entry 19, R8-3 Lemma 1, R7-4 Lemma 2.
Assume (R1), (R2^orb), (Rig), and Y non-constant. Let Q ∈ B_0 be a puncture point. Let β̃ and b̃ be lifted branches at 0, with (P) for b̃. Let x be Y-persistent on some anchored sheet T_β of β̃. Then:
- x is Y-persistent on **every** anchored sheet of b̃;
- at least one such sheet exists.

In particular MS11♭'s conclusion holds at every datum (Q, B, β̃, b̃, x) at which the chain invokes it. Neither (S), nor β̃ ≠ b̃, nor non-product type is needed.

*Proof.*
- By Prop. 3.3, 𝒥 = L is the unique lift-curve.
- By Lemma 4.1(b), L ⊂ T_β, so x ∈ P(T_β) ⊆ C(L) by Lemma 4.2, ⊆, which needs no (P).
- Let T_b be any anchored sheet of b̃; one exists by Lemma 4.1(a). By Lemma 4.1(b), L ⊂ T_b.
- T_b is of boundary type by (P) for b̃, so P(T_b) = C(L) ∋ x by Lemma 4.2. ∎

*Comparison with the twin failure configurations.* The run's obstructions to MS11 / MS11♭ are of two kinds:
- the (β)-twin / (B-pure) edges of round11_q3 §3.6 and round11_q7, together with model 1 of round11_q9 §2.2;
- the "rigid twin" of round11_q1 §4.

All of them need either several lift-curves, permuted by an a ∈ Aut(Q) moving x, or a stabiliser jump at t ≠ 0. (round11_q1 Prop. 2.4 reduces MS11 to "a ∈ Stab(x)".) Under (R2^orb) neither can happen:
- by Prop. 3.3 the single lift-curve is Aut(Q)-fixed;
- Aut(Q_t) ≅ Aut(Q).

This is consistent with the local models of round11_q7 §6 and round11_q1 §5: in each, σ fixes the boundary point at t = 0, while the transported point has smaller isotropy at t ≠ 0. These are exactly the families that (c) excludes (see §7).

---

## 5. Step 5: the chain, and the proof of the Theorem

**Proof of the Theorem.** Assume (R1) and (R2^orb), and suppose for contradiction that t ↦ Y_t is non-constant.

1. **(Rig).** By Theorem RO (Step 2), (Rig) holds. So we are in the setting of MS8 (round11_q9 §5; brief, "Chain", item 1), with "Y non-constant".
   - (R2^orb) ⊃ (R2), so every run result proved under (R1), (R2), (Rig) and "Y non-constant" applies to our family. That covers Theorem N, the walk chain and the Gap A repair.
2. **Walk chain** (entries 85, 98, 112; brief, Chain 2(a)). It gives pieces D^1 ⊂ ∂V_0, …, D^k, transitions J_m with entering and leaving lifts β̃_m and β̃′_m, labels x_m, and an endpoint Q_0 with entering β̃ (label x) and terminal b̃. At t = 0, x is MERGE or MOV along b̃.
3. **(P) everywhere it is needed** (entry 99, Chain 2(b)).
   - Interior transitions are trivial.
   - At every genuine transition (β̃′_m ≠ β̃_m) and at Q_0, both lifts satisfy (P).
   - So every such point is a puncture point in the sense of §3, and Prop. 3.3 applies there.
4. **Induction** (Chain 2(c)): x_m is Y-persistent on some anchored sheet of β̃_m.
   - The base, the product-type puncture transitions, and the transfer along D^{m+1} are as in round11_q9 §§2.5–2.7. Those steps use only (R1), (R2), (Rig) and Y non-constant.
   - At a non-product puncture transition with β̃′_m ≠ β̃_m, the chain invokes MS11♭ for (J_m, β̃_m, β̃′_m, x_m). Prop. 4.3 supplies its conclusion: x_m is Y-persistent on every anchored sheet of β̃′_m. Its hypotheses hold: J_m is a puncture point, (P) holds for β̃′_m, x_m is persistent on an anchored sheet of β̃_m, (Rig) holds, and Y is non-constant.
   - (Prop. 4.3 also covers product-type transitions, but the chain does not need it there.)
5. **Endpoint** (Chain 2(d); round11_q9 §2.8, re-read, quoted at the brief's lines on "Non-product, MERGE/MOV").
   - *Product type:* Lemma PT and Lemma J (J1) / Theorem R put Y_t in a finite set for t in an open set. By entry 19, Y is then constant: a contradiction.
   - *Non-product type:* Prop. 4.3, applied to (Q_0, β̃, b̃, x), gives an anchored sheet T ⊃ b̃ × {0} on which x is Y-persistent.
     - Restricting to t = 0: x is intact at every point of b̃ and F_x ≅ Y_0 along b̃.
     - MERGE is excluded: some edge at x is unpinched along b̃ ∖ 0, so x is not intact there.
     - MOV is excluded: [F_x] is non-constant along b̃.
     - Either way, a contradiction.
6. **Conclusion.** Hence t ↦ Y_t is constant, i.e. Y_t = Y_0 for all t ∈ Δ. (Entry 19, holomorphy of t ↦ [Y_t], is what makes "constant on an open set" equivalent to "constant", wherever the chain uses it.) ∎

**What was checked here and what was taken as given.**
- *Checked in this answer:*
  - Steps 1–4: Lemmas 3.1, 3.2, 4.1, 4.2, Prop. 3.3, Prop. 4.3;
  - the (R2^orb)-dependence of Theorem RO (§2);
  - the shrinking convention;
  - the endpoint contradiction from an anchored sheet.
- *Taken as given, per the brief* (verified in earlier rounds, not re-derived here):
  - the walk chain and its repairs (entries 85, 98, 112, 113);
  - Theorem X*_all / Cor. IMOV_all (entries 97, 99), which deliver (P);
  - Lemma PT, Lemmas T, S, J, Theorem R (entries 86, 87);
  - Theorem N (R8-3);
  - R8-3 Lemma 1, R7-4 Lemma 2;
  - entries 19, 24;
  - TV and Φ̂ (round8_q10);
  - the cited classical theorems (§8.2).

---

## 6. (L→G): the local orbifold reading implies the global form (a)–(d). Proved.

**Local reading (Loc).** For every boundary stratum G, every x̂ ∈ Ã_0 and every t_0 ∈ Δ, there are:
- an open neighbourhood W of x̂ in T_G;
- an open disc I ∋ t_0;
- a continuous map h : (W ∩ Ã_0) × I → T_G,

such that:
- (L1) ξ_G p∘h_s = H_s∘ξ_G p on W ∩ Ã_0, for s ∈ I;
- (L2) for each u ∈ W ∩ Ã_0, the subgroup Stab_{Mod_G}(h_s(u)) does not depend on s ∈ I.

**Why (Loc) is the chart-level reading.**
- The chart Def(z)^G → Def(z)^G/Aut(z) of the stratum at z = ξ_G p(x̂) is a Stab(x̂)-invariant slice neighbourhood W of x̂ modulo Stab(x̂) ≅ Aut(z) (Lemma 3.2).
- "H_s is an orbifold embedding, with local lifts depending continuously on (u,s)" means: there are continuous lifts h_s, injective on W ∩ Ã_0 and equivariant through an isomorphism φ : Stab(x̂) → Stab(h_{t_0}x̂) that is independent of s (by continuity in s, since the set of isomorphisms is discrete).
- Equivariance plus injectivity give Stab(h_s u) = φ(Stab(u)) for all s:
  - φ(Stab u) ⊂ Stab(h_s u) by equivariance;
  - if a fixes h_s(u), then h_s(φ^{-1}(a)u) = h_s(u), so φ^{-1}(a) ∈ Stab(u) by injectivity.
- So (L2) holds. Only (L1) and (L2) are used below; equivariance of the local lifts is not needed.

**Lemma U (unique continuation of stabiliser-constant lifts).** Let J be a connected interval and γ_1, γ_2 : J → T_G continuous, with ξ_G p∘γ_1 = ξ_G p∘γ_2 and with s ↦ Stab(γ_i(s)) locally constant for i = 1, 2. If γ_1(s_0) = γ_2(s_0) for some s_0, then γ_1 = γ_2.

*Proof.*
- E := {γ_1 = γ_2} is closed.
- E is open. Let s_1 ∈ E and y := γ_1(s_1). Since Mod_G acts properly discontinuously, there is a Stab(y)-invariant neighbourhood U of y with gU ∩ U ≠ ∅ ⇒ g ∈ Stab(y).
  - For s near s_1, both γ_i(s) ∈ U. The fibres of ξ_G p are Mod_G-orbits, so γ_2(s) = g_sγ_1(s), and then g_s ∈ Stab(y).
  - By local constancy, Stab(γ_1(s)) = Stab(y), so g_s fixes γ_1(s), and γ_2(s) = γ_1(s). ∎

**Theorem LG.** Assume (R2) and (Loc). Then there is a unique continuous H̃ : Ã_0 × Δ → T_G satisfying (a)–(d). Uniqueness holds even among continuous maps satisfying (a), (c) and (d).

*Construction.* For x ∈ Ã_0 and t ∈ Δ, let γ_{x,t} : [0,1] → T_G be a continuous lift of r ↦ H_{rt}(ξ_G p x) with γ(0) = x and r ↦ Stab(γ(r)) locally constant. Put H̃_t(x) := γ_{x,t}(1).

*Existence of γ_{x,t}.*
- Cover the segment [0,t] by discs I_1, …, I_k coming from (Loc) at (x, τ_j), with lifts h^j. Choose a partition 0 = r_0 < ⋯ < r_k = 1 with rt ∈ I_j for r ∈ [r_{j−1}, r_j], and with τ_1 = 0.
- h^1_0 lifts the identity near x. Normalise it: h^1_0(x) = a·x for some a ∈ Mod_G, and replacing h^1 by a^{-1}h^1 gives h^1_0(x) = x.
- Put γ := h^1_{rt}(x) on [r_0, r_1].
- Inductively, γ(r_j) and h^{j+1}_{r_j t}(x) lie over the same point, so γ(r_j) = g_{j+1}h^{j+1}_{r_j t}(x) for some g_{j+1} ∈ Mod_G. Put γ := g_{j+1}h^{j+1}_{rt}(x) on [r_j, r_{j+1}].
- γ is continuous. By (L2), its stabiliser is constant on each closed piece, hence constant on [0,1].

*Uniqueness of γ_{x,t}.* This is Lemma U. In particular H̃ does not depend on the choices.

*Properties.*
- **(a)** holds by construction.
- **(d)**: H_0 = id, so the constant path is the lift for t = 0.
- **(c)**: the stabiliser is constant along γ_{x,t}, so Stab(H̃_t x) = Stab(x).
- **(b)**: for g ∈ Mod_G, g∘γ_{x,t} lifts the same path, starts at gx, and has locally constant stabiliser g Stab(γ(r)) g^{-1}. By Lemma U it is γ_{gx,t}.
- **Uniqueness of H̃ among maps with (a), (c), (d).** For any such H̃′, the path r ↦ H̃′_{rt}(x) is a lift with constant stabiliser Stab(x), by (c). By (d) it starts at x, so Lemma U gives H̃′ = H̃.

*Joint continuity at (x_0, t_1).*
- Take the data above for (x_0, t_1): discs I_j, lifts h^j on W_j ∩ Ã_0, and the partition r_j.
- Choose δ > 0 with rt ∈ I_j for r ∈ [r_{j−1}, r_j] and all |t − t_1| < δ (compactness). Put W := ⋂_j W_j.
- Put K_j := Stab(g_jh^j_τ(x_0)), which is independent of τ ∈ I_j by (L2).
- **Claim:** for (x,t) close to (x_0,t_1), with x ∈ Ã_0, and r ∈ [r_{j−1}, r_j], we have γ_{x,t}(r) = k g_j h^j_{rt}(x) for some k = k(x,t) ∈ K_j.

  *Proof of the claim, by induction on j.*
  - **j = 1.** h^1_0(x) lies over ξ_G p(x), so h^1_0(x) = a_x x with a_x ∈ Mod_G. As x → x_0, both x and a_x x tend to x_0, so a_x ∈ Stab(x_0) = K_1 by proper discontinuity. The path r ↦ a_x^{-1}h^1_{rt}(x) has constant stabiliser and starts at x, so by Lemma U it is γ_{x,t} on [0, r_1].
  - **j → j+1.** Put y_0 := γ_{x_0,t_1}(r_j), and choose g_{j+1} with g_{j+1}h^{j+1}_{r_j t_1}(x_0) = y_0. Then K_j = Stab(y_0) = K_{j+1}.
    - For (x,t) close to (x_0,t_1), both γ_{x,t}(r_j) = k g_j h^j_{r_j t}(x) (with k ∈ Stab(y_0)) and g_{j+1}h^{j+1}_{r_j t}(x) lie in a Stab(y_0)-invariant slice neighbourhood of y_0, and they lie over the same point.
    - So they differ by some k′ ∈ Stab(y_0) = K_{j+1}.
    - By Lemma U on [r_j, r_{j+1}], γ_{x,t} = k′g_{j+1}h^{j+1}_{rt}(x) there.
- **Continuity.** By the claim, H̃_t(x) = k g_k h^k_t(x), with k in the finite group Stab(H̃_{t_1}(x_0)). As (x,t) → (x_0,t_1), g_k h^k_t(x) → H̃_{t_1}(x_0), and every element of that finite group fixes H̃_{t_1}(x_0). Hence H̃_t(x) → H̃_{t_1}(x_0). ∎

**Answer to (L→G).**
- The local reading implies the global one; no extra global assumption is needed. This is the homotopy-lifting argument suggested in the brief, done through stabiliser-constant lifts, which replace orbit-type strata coverings.
- Theorem LG uses (Loc) at all (x̂, t_0), not only at t_0 = 0. That is the natural meaning of "H is a family of orbifold maps": at every point of A_0 × Δ.
- If (Loc) were assumed only near t_0 = 0, one would obtain (a)–(d) only for |t| small. Theorem RO and the chain would then apply over a smaller disc, and the identity theorem (entry 19) would propagate Y_t ≡ Y_0 to all of Δ. So even this weaker local reading suffices for the Theorem.
  - *Caveat:* Theorem RO's Step 6 uses connectedness of the parameter disc. Over a smaller disc Δ_r it gives (Rig) on Δ_r, and the chain is run for the family restricted to Δ_r, which is again admissible. I have not re-checked every step of the chain for the restricted family, but none of the steps I read uses the size of the disc.

---

## 7. (Reading): is (R2^orb) a faithful formalisation?

**The orbifold reading.** Regard M_g, M̄_g and the strata Δ_G as orbifolds, i.e. as the analytic stacks [T_G/Mod_G]. Then the problem's phrases read as follows.
- "Complex submanifold 𝒱 ⊂ M_g × Δ" means a sub-orbifold: locally, the image of an Aut(z)-invariant submanifold of the chart Def(z) × Δ.
- "Smoothly trivial family of submanifolds" means an orbifold diffeomorphism V_0 × Δ ≅ 𝒱 over Δ.
- Hypothesis (i) means the same for closure(V_t) ∩ Δ_G inside the orbifold Δ_G, for every stratum.

An orbifold isomorphism has local lifts that are equivariant through isomorphisms of the local groups, and injective. By §6 ("Why (Loc) is the chart-level reading"), this gives (Loc), and by Theorem LG it gives (a)–(d). So **(R2^orb) is a faithful formalisation of the orbifold reading.** Compatibility (ii) is not needed beyond what (R2) already encodes.

Two further remarks on this reading.
- The interior part of (R2^orb) (G = open stratum) is not used anywhere. Only the boundary strata enter (Theorem RO; Prop. 3.3).
- The reading requires at least: for every boundary point z of V_0 and every t, Aut(H_t(z)) ≅ Aut(z), with an isomorphism varying continuously, i.e. locally constant.

**The coarse reading (R2).**
- M_g is read as the coarse analytic space, and H is merely a stratum-preserving homeomorphism, smooth on V_0 × Δ.
- This is strictly weaker. It allows the isotropy of transported points to drop: Aut(H_t z) can be a proper subgroup of Aut(z) (or a different group) for t ≠ 0.
- In the coarse space, a point with extra automorphisms is generally a singular point or a branch locus, but a homeomorphism does not see this.
- The literal wording ("subvariety of M_g", "(complex) smooth subvariety") is arguably closer to the coarse reading. The problem does not settle the question.

**Example: a coarse-admissible local family that violates (R2^orb).** This is the round11_q7 §6 model, re-read.
- At a boundary point Q, take stratum coordinates (u, v) on Def(Q)^{G_Q}. Let σ ∈ Aut(Q) act by u ↦ −u, fixing v (and act suitably on the plumbing coordinates).
- The coarse coordinates are (U, v) with U = u², so the coarse chart is smooth.
- Let B_0 contain, near Q, the curve {U = 0} = {u = 0}. Each of its points has the extra automorphism σ.
- Define H_t(U, v) := (U + t², v). This is a smooth, stratum-preserving, holomorphically varying trivialisation, so (R2) holds locally.
- The transported curve is {U = t²} = {u = ±t}, on which σ acts freely. So Aut(H_t z) ⊊ Aut(z) for t ≠ 0.
  - (c) fails.
  - No continuous lift with (a) and (c) exists: by Lemma U, a lift of t ↦ H_t(z) through the fixed point u = 0 with constant stabiliser ⟨σ⟩ would have to stay in Fix(σ) = {u = 0}, which H_t leaves.

The global version is the following. Suppose V_0 lies inside a symmetric locus, i.e. every curve of V_0 admits an automorphism σ of a fixed topological type, as for totally geodesic surfaces arising from covering constructions such as the cyclic quintic covers of PR-I. Suppose V_t leaves that locus at the boundary. Then (R2) can hold while (R2^orb) fails.

I do not know whether such a global family satisfying (i) and (ii) exists. If one does, the problem's claim for it is not covered by the Theorem. This is exactly the situation of the run's twin and rigid-twin failure configurations (round11_q1 §§4–5, round11_q9 model 1), all of which involve such a stabiliser drop.

**Verdict on (Reading).**
- (R2^orb) is faithful to the orbifold reading.
- It is strictly stronger than the coarse reading (R2). The difference is exactly the preservation of automorphism groups of points (boundary points suffice here).
- The Theorem settles the problem under the orbifold reading, modulo the inputs of §8.2. Under the coarse reading the problem remains open in this run.

---

## 8. Final status

### 8.1 Proved in this answer
1. Step 1: (R2^orb) ⊃ (R2); its additional content is spelled out (§1).
2. Step 2: the hypotheses of Theorem RO are exactly (R1), (R2), (a)–(d), plus TV/Φ̂ and Imayoshi–Shiga. The uses of (a)–(d) in Lemma 1.1 and Prop. T were re-checked. Hence (R2^orb) ⇒ (Rig).
3. Lemma 3.1: at a puncture point Q, t ↦ Q_t is holomorphic and 𝒥 is analytic. This uses only (R1), (R2) and (P).
4. Lemma 3.2: Stab_{Mod_G}(x̂) ≅ Aut(Z), including the automorphisms acting trivially on the stratum (elliptic and hyperelliptic involutions, which act on plumbing coordinates). (c) read "modulo generic automorphisms" is equivalent to (c) for full stabilisers. No strengthened reading is needed, and Theorem RO is unaffected.
5. Prop. 3.3 [orb]: |Aut(Q_t)| = |Aut(Q)|, and the lift locus at a puncture point is a single smooth curve L = graph of a holomorphic p(t), fixed by Aut(Q).
6. Lemma 4.1: anchored sheets exist, and every anchored sheet contains a lift-curve (so it contains L). This re-proves round11_q1 Lemma 2.1(c), with the arc argument made precise.
7. Lemma 4.2: P(T) = C(L) for boundary-type anchored sheets (round11_q1 Lemma 2.3, re-checked, given Theorem N).
8. Prop. 4.3 [orb]: MS11♭ holds at every puncture point, in the strong form "on every anchored sheet of b̃". It needs neither (S) nor β̃ ≠ b̃.
9. Theorem (conditional): (R1) + (R2^orb) ⇒ Y_t = Y_0, via the chain (§5).
10. Theorem LG: the chart-level local orbifold reading (Loc) implies the global equivariant, isotropy-preserving lift (a)–(d), and the lift is unique. This answers round12_q9's open question 2 affirmatively.

### 8.2 Inputs used and not re-derived here

**Run results (verified in earlier rounds per the brief):**
- entry 19 (PR-A, holomorphy of t ↦ [Y_t]) and entry 24;
- the walk chain and its repairs: entries 85, 98, 112, 113 (round11_q9);
- entries 84, 86, 87, 97, 99 (Theorem X*, Lemma PT, Lemmas T/S/J/Theorem R, Theorem X*_all, Cor. IMOV_all);
- Theorem N (R8-3) and R8-3 Lemma 1;
- R7-4 Lemma 2;
- round8_q10 Theorem TV and Corollary Φ̂, together with Lemma PA, Lemma NH and Proposition K on which the chain rests;
- round12_q9 Lemmas CS, CL, J0, Prop. T, Lemma R*′, Theorem RO. Of these I re-checked Lemma 1.1 and Lemma CL; the rest is taken as given per the brief.

**Classical results cited from memory:**
- Kuranishi/Deligne–Mumford local structure (Kur);
- proper discontinuity of Mod_G on T_G;
- connectedness of the regular part of an irreducible germ;
- Hurewicz–Wallman (closed sets of dimension ≤ n−2 do not separate an n-manifold);
- invariance of domain;
- normalisation of curves;
- Remmert's proper mapping theorem;
- Krull's principal ideal theorem (analytic form);
- the classical inputs of Theorem RO: Royden / Earle–Kra, Bers, Thurston, Selberg, orbifold uniformisation, Bers embedding, Cartan, Imayoshi–Shiga finiteness (with the scope caveat of round12_q9 §6).

### 8.3 Verdict
- **The derivation of the conditional Theorem is complete,** relative to the inputs of §8.2. No step of the derivation is left open.
- Under the orbifold reading, the problem's claim therefore follows from the run's prior results.

### 8.4 Open
1. The problem under the **coarse reading (R2)**: (Rig) (entry 82) and MS11♭ both remain open. The obstruction is exactly isotropy drop at boundary points (§7).
2. The scope of Imayoshi–Shiga finiteness for targets with marked points (round12_q9 open question 3), on which Theorem RO depends.
3. Whether a global family with (i), (ii) and an isotropy drop at the boundary exists, i.e. whether the coarse reading admits genuinely more families than the orbifold one in this setting (§7).

**proved:**
- Lemmas 3.1, 3.2, 4.1, 4.2;
- Props. 3.3, 4.3;
- Theorem LG;
- the conditional Theorem, relative to §8.2.

**not proved:** the problem under the coarse reading (R2).

**open:**
- (Rig) and MS11♭ under (R2);
- Imayoshi–Shiga scope;
- existence of isotropy-dropping admissible families.

=== END OF ANSWER round13_q10 ===
