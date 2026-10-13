kind: attempt
Open question attempted: is the conditional theorem "(R1) + (R2^orb) ⇒ Y_t = Y_0" (ledger entries 128 and 149) correctly proved? The summary flags it as the centre of the run's final document if the coarse goal is not reached; its full write-up (round13_q10) has not been checked by a separate query. (Final-round allowance: verification of a standing result the final document presents.)

## Task
Check round13_q10 (spliced verbatim below) step by step, as an independent referee:
- §0–§1: the formalisation of (R2^orb) and the convention on Mod_G.
- §2: that Theorem RO (round12_q9, spliced; independently verified in round13_q9 with repairs R1′, R2′, R3′, also spliced) applies, and exactly which of (a)–(d) it uses.
- §3: Lemma 3.1 (t ↦ Q_t holomorphic at puncture points; the topological-dimension argument with Hurewicz–Wallman and invariance of domain), Lemma 3.2 (Stab_{Mod_G}(x̂) ≅ Aut(Z), including automorphisms acting trivially on the stratum), Proposition 3.3 (one lift-curve; |Aut(Q_t)| = |Aut(Q)|; holomorphy of p via Lemma CL).
- §4: Lemma 4.1 (every anchored sheet contains a lift-curve; the arc argument), Lemma 4.2 (P(T) = C(L), via Theorem N), Proposition 4.3 (MS11♭ at every puncture point).
- §5: the proof of the Theorem through the walk chain (round11_q9, spliced) — in particular that every invocation of MS11♭ is at a puncture point and that the endpoint contradiction is valid.
- §6: Theorem LG (the local orbifold reading (Loc) implies the global lift (a)–(d)): Lemma U (unique continuation), the construction, joint continuity.
- §7: the discussion of the reading: is (R2^orb) a faithful formalisation of the orbifold reading of the problem's hypotheses, and is the example of a coarse-admissible local family violating (R2^orb) correct?
For every inference say whether it is valid; repair what you can (say so); and end with an explicit verdict: does round13_q10, together with the cited inputs, prove "under (R1) and (R2^orb) (or (Loc)), Y_t = Y_0 for all t" exactly as stated, and which inputs (listed in its §8.2) remain unchecked dependencies?

Begin with a plan/status line. End with: verdict / repairs / remaining dependencies.

## round13_q10 (verbatim) — the write-up to be checked
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


## round12_q9 (verbatim): Lemmas CS, CL, J0, Prop. T, Lemma R*′, Theorem RO
# round12_q9 — attempt on (Rig) (ledger entry 82)

**Plan/status line (written first).** Brief read in full.
1. Item 1 ((Rig) under the coarse reading (R2)): I found no global argument. I record a new reduction (§7).
2. Item 2 ((Rig) under the orbifold reading): I formalise (R2^orb) as an equivariant lift of H on every stratum (§1). Then:
   - (H_0) holds for the **joint** vertex map of every piece at t = 0, over the Veech-type orbifold structure Λ_E. This is Lemma J0, derived from Theorem TV and Corollary Φ̂ of round8_q10. It is what makes Example Z irrelevant at t = 0.
   - (R2^orb) transports this joint lift (§4).
   - Lemma R* with set-valued monodromy, plus Imayoshi–Shiga, then gives (Rig) for all pieces in all strata, product or not (§5–§6).
3. The weakest form proved, the cited inputs, and the open questions are listed in §8.

---

## 1. Readings and conventions

(R1) and (R2) are as in the task: H is a homeomorphism closure(V_0) × Δ → closure(𝒱) over Δ, H_0 = id, mapping strata to strata.

**Stratum notation.** For a stable graph G with at least one edge:
- T_G := ∏_{w∈V(G)} T_w, where T_w is the Teichmüller space of type (g_w, n_w) with labelled special points.
- Mod_Π := ∏_w Mod_w, where Mod_w is the pure mapping class group.
- p : T_G → ∏_w M_w = T_G/Mod_Π is the quotient (coarse spaces).
- Mod_G ⊃ Mod_Π is the finite extension, by lifts of Aut(G), for which [T_G/Mod_G] is the stratum Δ_G as a sub-orbifold of M̄_g. Its isotropy groups are the Aut(z), modulo generic automorphisms.
- ξ_G : ∏M_w → Δ_G is the finite quotient map.
- A_t := closure(V_t) ∩ Δ_G, Â_t := ξ_G^{-1}(A_t) ⊂ ∏_w M_w, and Ã_t := p^{-1}(Â_t) ⊂ T_G.

All groups act properly discontinuously by biholomorphisms, and they are countable.

**Reading (R2^orb) (formal version used here).** For every stratum G there is a continuous map H̃ = H̃^G : Ã_0 × Δ → T_G, written H̃_t := H̃(·, t), such that for all t:
- (a) H̃_t lifts H_t: ξ_G∘p∘H̃_t = H_t∘ξ_G∘p on Ã_0;
- (b) H̃_t is Mod_G-equivariant: H̃_t(g x) = g H̃_t(x) for all g ∈ Mod_G;
- (c) H̃_t preserves isotropy: Stab_{Mod_G}(H̃_t x) = Stab_{Mod_G}(x);
- (d) H̃_0 = id.

*Why this is the content of "H restricted to each stratum is an orbifold isomorphism, compatible with the charts Def(z)/Aut(z)".*
- Near ẑ ∈ T_G over z, the chart Def(z) → Def(z)/Aut(z) is a Stab(ẑ)-invariant neighbourhood of ẑ in T_G, modulo Stab(ẑ) ≅ Aut(z).
- A family of orbifold maps of the global quotient [Ã_0/Mod_G] into [T_G/Mod_G] that starts at the identity is represented by an equivariant lift, with equivariance through an automorphism of Mod_G. Since t ↦ that automorphism is continuous into a discrete set and is the identity at t = 0, it is the identity.
- (c) is "preserves isotropy groups".
- I do **not** prove that a purely local formulation (local equivariant lifts at each z, with no coherent choice) implies the global one. That is a gap in the *interpretation*, not in the proofs below: every later use of (R2^orb) is a use of (a)–(d).

**Uses of (R2^orb)** are marked [orb] below. Everything not marked uses only (R1) and (R2).

**Lemma 1.1 [orb] (descended transport).** H̃_t descends to a map Π_t : Â_0 → Â_t (so p∘H̃_t = Π_t∘p) with the following properties:
- Π_t is a homeomorphism;
- ξ_G∘Π_t = H_t∘ξ_G;
- (x, t) ↦ Π_t(x) is continuous;
- Π_t maps each piece (1-dimensional irreducible component) of Â_0 onto a piece of Â_t, and every piece at time t arises this way.

*Proof.*
- **Descends.** By (b) for g ∈ Mod_Π, H̃_t descends. By (a) the descended map lands in Â_t, because ξ_G p H̃_t(x) = H_t(ξ_G p x) ∈ A_t.
- **Injective on Ã_0.** If H̃_t x = H̃_t y, then by (a) and injectivity of H_t we get ξ_G p x = ξ_G p y, so y = g x for some g ∈ Mod_G. Then g H̃_t x = H̃_t x. By (c), g ∈ Stab(H̃_t x) = Stab(x), so y = x.
- **Surjective onto Ã_t.** Let y ∈ Ã_t. Then ξ_G p y = H_t(ξ_G p x) = ξ_G p H̃_t x for some x ∈ Ã_0, so y = g H̃_t x = H̃_t(g x).
- **Π_t is bijective.** Injectivity: if Π_t(p x) = Π_t(p y), then H̃_t x = g H̃_t y = H̃_t(g y) with g ∈ Mod_Π, so x = g y. Surjectivity is immediate from the surjectivity of H̃_t.
- **Continuity.** H̃ is continuous and p is open, so Π_t is continuous, jointly in (x, t).
- **Continuity of Π_t^{-1}.** Let y_n → y and x_n := Π_t^{-1} y_n. Then ξ_G(x_n) = H_t^{-1} ξ_G(y_n) converges. Since ξ_G is finite, hence proper, the x_n lie in a compact set. Every limit point x satisfies Π_t x = y, so x_n → Π_t^{-1}y.
- **Pieces.** A homeomorphism of 1-dimensional analytic sets maps isolated points to isolated points, and irreducible components of the 1-dimensional part to irreducible components. The latter are the closures of the connected components of the set of points with a disc neighbourhood (round8_q7 Lemma S″, argument re-checked). ∎

For a piece E_0 of Â_0, put E_t := Π_t(E_0). Its normalisation is ν_t : Ê_t → E_t. Π_t lifts to a homeomorphism Ĥ_t : Ê_0 → Ê_t with ν_t∘Ĥ_t = Π_t∘ν_0, because local branches are the components of punctured links (round5_q4 §2.1).

**Ê_t has finite type with puncture ends.** The closure of ξ_G(E_t) in M̄_g is a component of the compact analytic set closure(V_t) ∩ closure(Δ_G). So its normalisation is a compact Riemann surface minus finitely many points. Ê_t maps finitely onto that normalisation, and a finite unbranched cover of a punctured disc is a disjoint union of punctured discs. Hence Ê_t is a compact Riemann surface minus finitely many points, and Ĥ_t maps punctures to punctures.

## 2. Two lifting lemmas (proved; no hypothesis beyond the setting)

Throughout §2, Γ is a countable group acting properly discontinuously by biholomorphisms on a complex manifold T. X := T/Γ carries Cartan's quotient analytic structure, and p : T → X is the quotient map. Q is a connected Riemann surface.

**Lemma CS (two holomorphic lifts differ by one group element).** Let F, F′ : Q → T be holomorphic with p∘F = p∘F′. Then F′ = g∘F for some g ∈ Γ. The set of such g is a coset g·S_F, where S_F := {s ∈ Γ : s∘F ≡ F} is a finite group.

*Proof.*
- Q = ∪_{g∈Γ} Z_g, where Z_g := {y : F′(y) = gF(y)}.
- Each Z_g is a closed analytic subset of Q, and Γ is countable. By Baire, some Z_g has interior.
- By the identity theorem F′ ≡ gF.
- If gF ≡ g′F, then g^{-1}g′ ∈ S_F. Finally S_F ⊂ Stab(F(y)), which is finite. ∎

**Lemma CL (continuous lifts of holomorphic maps are holomorphic).** Let h : Q → X be holomorphic and L : Q → T continuous with p∘L = h. Then L is holomorphic.

*Proof.* The statement is local. Fix y_0 and put x̂ := L(y_0), A := Stab_Γ(x̂) (finite).

**Chart.** By Cartan there is an A-invariant neighbourhood B of x̂ such that:
- B is A-equivariantly a ball with linear A-action;
- gB ∩ B ≠ ∅ implies g ∈ A;
- B/A → X is an open embedding.

Let σ = (σ_1, …, σ_m) be generators of the A-invariant polynomials. They induce an embedding σ̄ of B/A into ℂ^m. Since h is holomorphic, σ̄∘h is holomorphic near y_0.

**Fibre product.** Take a disc Q_0 ∋ y_0 whose closure satisfies L(closure Q_0) ⊂ B. Put Z := {(y,b) ∈ Q_0 × B : σ(b) = σ̄(h(y))}.
- Z is analytic, and its fibre over y is the finite orbit A·L(y).
- Z → Q_0 is proper, since fibres lie in the compact set A·L(closure Q_0).
- So Z is finite over Q_0. Let Σ ⊂ Q_0 be the image of Sing Z, of the 0-dimensional part of Z, and of the critical points of the projection on Reg Z. Σ is discrete: a curve of critical points would lie in a fibre, and fibres are finite.
- Over Q_0 ∖ Σ, Z → Q_0 is a finite covering map whose local sheets are graphs of holomorphic maps.

**Conclusion.** The graph of L|_{Q_0∖Σ} is a continuous section of this covering. Over every evenly covered disc a continuous section lies in a single sheet, so L is holomorphic on Q_0 ∖ Σ. L is continuous and bounded in the coordinates of the ball B, so by Riemann's extension theorem it is holomorphic on Q_0. ∎

*Remark.* Lemma CL is why no orbifold bookkeeping (cone orders, minimal orbifolds) is needed below. If a continuous lift exists, it is automatically holomorphic, and cone points that would obstruct it cannot be present.

## 3. Lemma J0: the joint vertex map of every piece at t = 0 lifts over the Veech orbifold (no use of (R2^orb))

**Prior results used** (round8_q10, quoted in the brief; not re-proved here):
- **Theorem TV.** Let E be a piece of Â_0 (any G). There are:
  - a vertex j;
  - a closed Teichmüller curve C ⊂ M_j, with normalisation κ : C^ν = H/Γ′ → M̄_j (Γ′ a lattice);
  - a subgroup Λ_E ⊂ Γ′ of finite index, with E^ν ≅ H/Λ_E such that p_E := (π_j∘ν lifted to normalisations) : E^ν → C^ν is the map H/Λ_E → H/Γ′ induced by the inclusion.

  The Teichmüller disc D : H → T_j satisfies D∘γ = (affine class of γ)∘D for γ ∈ Γ′, and κ∘q_{Γ′} = u := (projection of D to M_j).
- **Corollary Φ̂, together with the proof of TV.** For a point P̂ ∈ E chosen off Sing Â and off the other components of Â, there is a continuous map Φ = (φ̂_w)_w : H → T_G with:
  - each φ̂_w 1-Lipschitz;
  - φ̂ := p∘Φ mapping H into Â;
  - φ̂(i) = P̂;
  - φ̂_j = D, so π_j∘φ̂ = u.

**Lemma J0.** Let E be a piece at t = 0, with the notation of TV. Put Λ := Λ_E and let q : H → H/Λ = E^ν be the quotient map. There are γ_0 ∈ Γ′ and a **holomorphic** map F : H → T_G such that:
- (i) p∘F = ν∘q, i.e. F lifts the whole vertex map of E;
- (ii) pr_j∘F = D∘γ_0^{-1}, an isometric holomorphic embedding of H onto the Teichmüller disc 𝔇 := D(H);
- (iii) for every λ ∈ Λ the set R(λ) := {g ∈ Mod_Π : F∘λ = g∘F} is a coset of the finite group S := {s ∈ Mod_Π : s∘F ≡ F}. Moreover R(λμ) = R(λ)R(μ), and every element of R(λ) normalises S.

*Proof.*

**Step 1 (φ̂(H) ⊂ E).** Let Z be the union of the following sets:
- the points of E lying on other components of Â;
- the isolated points of Â;
- the components E′ ≠ E of Â on which π_j is constant.

Z is closed, and it is a locally finite union of points and curves. For a compact disc K ⊂ H, φ̂(K) is compact. It meets only finitely many points and components making up Z, and π_j takes finitely many values on φ̂(K) ∩ Z. Hence φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite set) ∩ K, which is finite because u is non-constant holomorphic. So φ̂^{-1}(Z) is discrete, and H° := H ∖ φ̂^{-1}(Z) is connected.

Now Â ∖ Z is the disjoint union of E ∖ Z and the sets E′ ∖ Z (E′ ≠ E, π_j non-constant on E′). Each of these is relatively closed, and the family is locally finite, so E ∖ Z is clopen in Â ∖ Z. Its preimage is clopen in H° and contains i, because P̂ ∉ Z. Hence it is all of H°, and since E is closed, φ̂(H) ⊂ E.

**Step 2 (φ̂ is holomorphic).** Let Σ_E ⊂ E be the discrete set consisting of:
- Sing E;
- the points where π_j|_E : E → C is not a local biholomorphism onto a smooth point of C.

π_j|_E is a non-constant finite map of curves, so Σ_E is discrete. As in Step 1, φ̂^{-1}(Σ_E) is discrete. Off it, φ̂ = (π_j|_E)^{-1}_{loc}∘u is holomorphic. Since φ̂ is continuous, Riemann's extension theorem (in a local embedding of ∏M_w) makes it holomorphic on H.

**Step 3 (lift to E^ν, and p_E∘φ^ν = q_{Γ′}).** φ̂ lifts to a holomorphic φ^ν : H → E^ν, by the universal property of normalisation. Then κ∘p_E∘φ^ν = π_j∘φ̂ = u = κ∘q_{Γ′}. Since κ is generically injective, p_E∘φ^ν = q_{Γ′}.

**Step 4 (φ^ν = q∘γ_0).** Let Br ⊂ C^ν be the finite set of orbifold points of H/Γ′.
- Over C^ν ∖ Br, both H → H/Γ′ and the finite map p_E : H/Λ → H/Γ′ are unbranched coverings.
- Put H^♮ := q_{Γ′}^{-1}(C^ν ∖ Br), a connected set (H minus a discrete set), and fix x_0 ∈ H^♮.
- The fibre p_E^{-1}(q_{Γ′} x_0) is {q(γ x_0) : γ ∈ Γ′}. So φ^ν(x_0) = q(γ_0 x_0) for some γ_0 ∈ Γ′.
- φ^ν and q∘γ_0 are both lifts of q_{Γ′}|_{H^♮} through a covering map, and they agree at x_0. So they agree on H^♮, hence on H.

**Step 5 (F).** Put F := Φ∘γ_0^{-1}.
- F is continuous, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q.
- ν∘q is holomorphic, so F is holomorphic by Lemma CL (with Γ = Mod_Π). This gives (i).
- (ii): pr_j∘F = D∘γ_0^{-1}, and γ_0^{-1} is an isometry of H.
- (iii): for λ ∈ Λ, F∘λ and F are holomorphic lifts of the same map ν∘q∘λ = ν∘q, so Lemma CS applies.
- Product rule: if a ∈ R(λ) and b ∈ R(μ), then F(λμx) = aF(μx) = abF(x).
- Normality: if g ∈ R(λ) and s ∈ S, then g^{-1}sgF = g^{-1}s(F∘λ) = g^{-1}(F∘λ) = F, so g^{-1}sg ∈ S. ∎

**Consequences.**
- **(H_0) for the joint map.** At t = 0 the whole vertex map of every piece, not only its Teichmüller coordinate, has an equivariant holomorphic lift over the single orbifold structure Λ_E for which the j-coordinate is an isometry. This is hypothesis (H_0) of Lemma R*, together with (O_u) at t = 0 in L2 (round7_q9).
- In particular the joint minimal orbifold structure of ν_0 is dominated by Λ_E: every cone point of the joint map is a cone point of Λ_E, with order dividing.
- **Example Z (round8_q9) cannot occur at t = 0.** There the u-coordinate z³ + z needs cone points (orders 3 and 2 at roots of J_0 = 0, 1728, and order 6 at z = 0) that Λ_E does not have. So Lemma J0 excludes it as a boundary piece of a totally geodesic V_0. This answers the t = 0 half of question Q1 of round9_q9 for Example Z: E_0 is not realisable. For Example Z′, Lemma J0 excludes E_0 unless J_0∘q lifts holomorphically to T_{1,1} = H. I have not decided which J_0 satisfy this. So the remaining objection to Z/Z′-type deformations concerns t ≠ 0: Lemma J0 says nothing about E_t for t ≠ 0.

## 4. [orb] Transport of the joint lift: (O_G), (O), (OT), (O_u) hold under (R2^orb)

Fix a piece E_0 at t = 0, with Λ := Λ_E, q = u_0 : H → Ê_0 = E^ν, and F_0 := F as in Lemma J0. Write e_c for the cone orders of the orbifold O_0 := H/Λ, and E_t, Ê_t, Ĥ_t as in §1.

**Transported orbifold.** Let O_t be the orbifold with underlying Riemann surface Ê_t, cone points Ĥ_t(c) of order e_c, and the punctures of Ê_t as cusps.
- O_t has the same signature as O_0, so χ^orb(O_t) = χ^orb(O_0) < 0.
- By the uniformisation theorem for hyperbolic 2-orbifolds (cited from memory), O_t = H/Λ_t for a lattice Λ_t ⊂ PSL_2(ℝ), with holomorphic quotient map u_t : H → Ê_t.
- Ĥ_t is a homeomorphism O_0 → O_t preserving cone points with their orders and cusps. So it lifts to a homeomorphism h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0, and conjugation by h̃_t gives an isomorphism θ_t : Λ_t → Λ, θ_t(λ) := h̃_t^{-1} λ h̃_t. (Lifting orbifold homeomorphisms to orbifold universal covers is standard; cited from memory.)
- At t = 0 take h̃_0 = id.

**Proposition T [orb].** Put F_t := H̃_t∘F_0∘h̃_t^{-1} : H → T_G. Then:
- (1) F_t is holomorphic and p∘F_t = ν_t∘u_t. That is, F_t is a holomorphic lift of the whole vertex map of E_t over the transported orbifold O_t.
- (2) For λ ∈ Λ_t and every g ∈ R(θ_t λ): F_t∘λ = g∘F_t.

So the orbifold-transport hypothesis holds in the following form:
- **(O_G)** (round7_q9 §2.1) holds with the joint monodromy ρ_0∘θ_t, where ρ_0 is any choice function λ ↦ ρ_0(λ) ∈ R(λ).
- Projecting to a vertex gives **(O)** of PR-E and **(O_u)** for every u.
- With Λ_E as the orbifold structure, it gives **(OT)** of Lemma TR.

*Proof.*
- **(1), lifting.** F_t is continuous. By (a) of (R2^orb) and the definition of Π_t, p∘H̃_t = Π_t∘p on Ã_0. Hence
  p∘F_t = Π_t∘ν_0∘u_0∘h̃_t^{-1} = Π_t∘ν_0∘Ĥ_t^{-1}∘u_t = ν_t∘u_t.
  Since ν_t∘u_t is holomorphic, F_t is holomorphic by Lemma CL.
- **(2), equivariance.** Using (b) of (R2^orb) for g ∈ Mod_Π ⊂ Mod_G, and F_0∘θ_t(λ) = g∘F_0 for g ∈ R(θ_tλ):
  F_t(λy) = H̃_t F_0(h̃_t^{-1} λ y) = H̃_t F_0(θ_t(λ) h̃_t^{-1} y) = H̃_t(g F_0(h̃_t^{-1}y)) = g F_t(y). ∎

**Where (R2^orb) was used.** Only (a), (b) and (c) of the reading, through Lemma 1.1 and the identity H̃_t∘g = g∘H̃_t for g ∈ Mod_Π.

This answers the task's question: (R2^orb) implies the transport hypotheses (O), (O_G), (OT) and (O_u). (H_0) is independent of (R2^orb): it is Lemma J0. Under the coarse reading, the step that fails is exactly the existence of a continuous Mod_Π-equivariant lift H̃_t. Without it, nothing produces the continuous lift F_t, and Lemma CL has nothing to act on.

*Note on cone points (the task's remark).* An automorphism of one component C_v fixing its special points extends by the identity to an automorphism of the stable curve. So stabilisers in Mod_Π are visible in Aut(z), and hence in Mod_G. This is why (c) for Mod_G gives (c) for Mod_Π: Stab_{Mod_Π}(x) = Stab_{Mod_G}(x) ∩ Mod_Π. The proof above does not need cone orders explicitly.

## 5. Lemma R*′ (Lemma R* with coset-valued monodromy; re-proved here)

**Cited from memory.**
- **(Roy)** Royden, and Earle–Kra / Gardiner for punctured surfaces: holomorphic maps H → T_{h,m} are 1-Lipschitz from the Poincaré metric of curvature −4 to d_T.
- **(Bers)** If φ ∈ Mod preserves a Teichmüller geodesic and translates it by ℓ > 0, then φ is pseudo-Anosov, τ_T(φ) = ℓ, and Min(φ) is that geodesic.
- **(Th)** Thurston: for marked complete finite-area hyperbolic structures X, Y on the same surface, if ℓ_Y ≥ ℓ_X on all closed curves, then X = Y. Equivalently, there is an isometry homotopic to the marking.
- **(Sel)** Selberg's lemma.
- Axes of hyperbolic elements of a lattice have transverse intersection points dense in H.

**Lemma R*′ [orb].** In the setting of Proposition T, let j be the Teichmüller vertex and put f_t := pr_j∘F_t. There is an isometry A_t of H with A_t Λ A_t^{-1} = Λ_t and A_t λ A_t^{-1} = θ_t^{-1}(λ) for all λ ∈ Λ. A_t is holomorphic, i.e. A_t ∈ PSL_2(ℝ), and f_t∘A_t = f_0.

*Proof.* For μ ∈ Λ put R_j(μ) := pr_j(R(μ)). Every g ∈ R_j(μ) satisfies g∘f_0 = f_0∘μ.

**Step 1.** Let μ be hyperbolic and g ∈ R_j(μ). By Lemma J0(ii), f_0 is an isometry onto 𝔇. So g preserves 𝔇 and translates the geodesic f_0(α_μ) by ℓ_0(μ). By (Bers), g is pseudo-Anosov, τ_T(g) = ℓ_0(μ), and Min(g) = f_0(α_μ).

**Step 2.** Let γ ∈ Λ_t be hyperbolic, x on its axis, and g ∈ R_j(θ_tγ). By Prop. T(2), g f_t(x) = f_t(γ x). By (Roy),
  τ_T(g) ≤ d_T(f_t x, f_t γ x) ≤ ℓ_t(γ).
By Step 1, τ_T(g) = ℓ_0(θ_t γ). Hence ℓ_t(γ) ≥ ℓ_0(θ_tγ).

**Step 3 (Thurston).**
- By (Sel) take Λ′ ⊂ Λ torsion-free, normal, of finite index, and put Λ′_t := θ_t^{-1}(Λ′).
- h̃_t descends to a homeomorphism H/Λ′ → H/Λ′_t between complete finite-area hyperbolic surfaces. It induces θ_t^{-1} on π_1, and θ_t preserves the parabolic/hyperbolic type.
- Step 2 says that lengths on H/Λ′_t dominate lengths on H/Λ′ under this marking. If h̃_t reverses orientation, apply (Th) to the conjugate structure; lengths do not see orientation.
- So there is an isometry A_t of H, possibly orientation-reversing, with A_t λ A_t^{-1} = θ_t^{-1}(λ) for λ ∈ Λ′.
- **Extension to Λ.** For λ ∈ Λ, c := λ^{-1}A_t^{-1}θ_t^{-1}(λ)A_t centralises Λ′. A lattice has trivial centraliser in Isom(H), so c = 1.

**Step 4 (the maps coincide).** Put k_t := f_t∘A_t. For μ ∈ Λ and g ∈ R_j(μ): k_t(μx) = f_t(θ_t^{-1}(μ)A_t x) = g k_t(x), by Prop. T(2). k_t is 1-Lipschitz, since it is f_t composed with an isometry.
- For hyperbolic μ and x ∈ α_μ: d_T(k_t x, g k_t x) ≤ ℓ_0(μ) = τ_T(g). So k_t x ∈ Min(g) = f_0(α_μ).
- At a transverse intersection point x of two axes α_μ, α_ν: k_t(x) ∈ f_0(α_μ) ∩ f_0(α_ν) = {f_0(x)}, by injectivity of f_0.
- By density of such points and continuity, k_t = f_0.
- If A_t reversed orientation, k_t would be anti-holomorphic and also equal to the holomorphic non-constant f_0, which is impossible. So A_t ∈ PSL_2(ℝ). ∎

So A_t descends to a biholomorphism ā_t : Ê_0 → Ê_t (an orbifold isomorphism O_0 → O_t), with π_j∘ν_t∘ā_t = π_j∘ν_0. In particular (Rig-v): closure π_j(E_t) = closure π_j(E_0) = C̄.

## 6. Theorem RO: (Rig) under (R2^orb)

**Cited from memory: (IS) Imayoshi–Shiga**, "A finiteness theorem for holomorphic families of Riemann surfaces" (MSRI Publ. 11, 1988). Let R be a Riemann surface of finite type, and Y = T_{h,m}/Γ with Γ ⊂ Mod_{h,m} torsion-free of finite index (3h−3+m > 0). Then each free homotopy class of maps R → Y contains at most finitely many non-constant holomorphic maps.

*Caveat.* I recall the theorem for families of Riemann surfaces of type (h,m) in general, which is the form used in round7_q9 and round8_q9. If the published statement covers only some types, then Theorem RO holds for the pieces whose non-constant vertices are of the covered types.

**Theorem RO [orb].** Assume (R1), (R2) and (R2^orb), and the prior results TV and Φ̂ (round8_q10). Let E_0 be any piece at t = 0, in any stratum G (product or not), and E_t := Π_t(E_0). Then:
- (a) M(E_t) = M(E_0) for all t;
- (b) there is a finite set 𝒦(E_0) of curves with K(E_t) ∈ 𝒦(E_0) for all t;
- (c) in fact K(E_t) = K(E_0) for all t, and every puncture value f_u(p), u ∈ M(E_0), of E_t lies in the t-independent finite set of points of K(E_0) ∖ ∏_u M_u, together with their components.

Consequently **(Rig) holds**, with 𝒦 := {(G, M(E_0), K(E_0)) : G a stratum, E_0 a piece of Â_0}. This set is finite, and every piece at every time has its triple in 𝒦. (Rig-w) and the joint-image form (Rig-all) follow as well.

*Proof.*

**Step 0 (finitely many pieces).**
- There are finitely many strata.
- For each G, the 1-dimensional components of A_0 are open dense parts of components of the compact analytic set closure(V_0) ∩ closure(Δ_G), so there are finitely many.
- ξ_G is finite, so Â_0 has finitely many pieces.
- By Lemma 1.1, every piece at time t is Π_t(E_0) for one of them.

So (b) for every E_0 gives (Rig).

**Step 1 (a lattice on which the monodromy is an honest homomorphism into a torsion-free group).** Fix N ≥ 3 and put Mod[N] := ∏_w Mod_w[N], which is torsion-free. Note S ∩ Mod[N] = {1}, since S is finite.
- By Lemma J0(iii), λ ↦ R(λ) is a homomorphism Λ → N(S)/S.
- Let Λ^N be the preimage of (N(S) ∩ Mod[N]S)/S. It has finite index in Λ, since Mod[N] has finite index in Mod_Π.
- Take Λ″ ⊂ Λ^N torsion-free, normal and of finite index in Λ (Selberg, then normal core).
- For μ ∈ Λ″, R(μ) ∩ Mod[N] consists of exactly one element r(μ): it is nonempty by definition of Λ^N, and two elements would differ by an element of S ∩ Mod[N] = {1}.
- r is a homomorphism Λ″ → Mod[N]: r(μ)r(ν) ∈ R(μν) ∩ Mod[N].

**Step 2 (the normalised maps).** Put g_t := F_t∘A_t : H → T_G. By Prop. T(2) and A_t μ A_t^{-1} = θ_t^{-1}(μ), for μ ∈ Λ″:
  g_t(μ x) = F_t(θ_t^{-1}(μ) A_t x) = r(μ) g_t(x),
since r(μ) ∈ R(μ) = R(θ_t(θ_t^{-1}μ)).
- Mod[N] acts freely and properly on T_G. So M[N] := T_G/Mod[N] = ∏_w M_w[N] is a complex manifold and a K(π,1), since T_w is contractible.
- R := H/Λ″ is a Riemann surface of finite type (a finite cover of the finite-area orbifold H/Λ).
- g_t descends to a holomorphic ḡ_t = (ḡ^w_t)_w : R → ∏_w M_w[N], and p∘g_t = ν_t∘u_t∘A_t = ν_t∘ā_t∘q.
- So E_t = ν_t(Ê_t) is the image of R under ∏_w (M_w[N] → M_w) ∘ ḡ_t.

**Step 3 (fixed homotopy classes).** For each w, ḡ^w_t lifts to g^w_t, which is r_w-equivariant (r_w := pr_w∘r). Maps into the K(π,1) M_w[N] are determined up to free homotopy by the induced homomorphism up to conjugacy, so all ḡ^w_t, t ∈ Δ, are freely homotopic.

**Step 4 (non-constancy is t-independent).**
- If ḡ^w_t is constant, then g^w_t is constant (connected domain, discrete fibres). Then r_w(Λ″) fixes a point of T_w, so it is finite, hence trivial, since Mod_w[N] is torsion-free.
- Conversely, if r_w is trivial, then g^w_t descends to a holomorphic map R → T_w. T_w is biholomorphic to a bounded domain (Bers embedding, cited). R is a compact surface minus finitely many points, and bounded holomorphic functions extend over punctures. So the map is constant.
- Hence ḡ^w_t is constant ⟺ r_w = 1, which does not depend on t. Since ν^w_t∘ā_t∘q = (M_w[N] → M_w)∘ḡ^w_t∘(H → R), this gives (a).

**Step 5 (finiteness).** For u ∈ M(E_0), (IS) and Step 3 show that ḡ^u_t lies in a finite set {ψ_{u,1}, …, ψ_{u,k_u}} independent of t. Hence pr_{M}(E_t) is the image of R under one of the finitely many maps (ψ_{u,i_u})_{u∈M}, followed by the projections to M_u. So K(E_t) lies in a finite set 𝒦(E_0). This proves (b).

**Step 6 (constancy, (c)).** For K ∈ 𝒦(E_0), put T_K := {t : K(E_t) = K}.
- T_K is closed. Suppose t_n → t* with K(E_{t_n}) = K. Π is jointly continuous (Lemma 1.1), so every point of E_{t*} is a limit of points of E_{t_n}. Hence pr_M(E_{t*}) ⊂ K, and K(E_{t*}) = K because both are irreducible curves.
- The T_K are finitely many disjoint closed sets covering the connected Δ. So K(E_t) ≡ K(E_0).
- The statement on puncture values follows as in round8_q7 Cor. S′(a): K(E_0) ∖ ∏M_u is finite. ∎

**Explicit list of uses of (R2^orb):**
- Lemma 1.1 (descent and bijectivity of Π_t, which needs (b) and (c));
- Prop. T (equivariance (b), and the lifting property (a));
- through these, Lemma R*′ and Theorem RO.

Lemma J0, Lemma CS and Lemma CL do not use it.

## 7. The coarse reading (R2): precise reduction (item 1 not achieved)

I found no global argument proving (Rig) under the coarse reading. What §§3–6 give without (R2^orb) is the following reduction. It is proved: the proofs of R*′ and RO use (R2^orb) only through Prop. T.

**Hypothesis (T_c) for a piece E_0.** For every t there is a holomorphic F_t : H → T_G with:
- p∘F_t = ν_t∘u_t, where u_t uniformises the transported orbifold O_t of §4;
- F_t∘λ = g∘F_t for every λ ∈ Λ_t and some (equivalently every) g ∈ R(θ_tλ).

Here θ_t is induced by a lift of a homeomorphism Ê_0 → Ê_t isotopic to Ĥ_t and preserving the cone data of Λ_E.

**Proposition C.** Under (R1), (R2) and TV/Φ̂ (no (R2^orb)): if (T_c) holds for every piece at t = 0, then (Rig) holds, together with (a)–(c) of Theorem RO.

*Proof.* There are two places where (R2^orb) entered.
- Prop. T: this is replaced verbatim by (T_c).
- Lemma 1.1, used in Theorem RO Step 0 and Step 6.

Under (R2) alone, Lemma 1.1 must be replaced as follows.
- **Product-type G.** Π_t := H_t restricted to strata. It is a homeomorphism, and it maps pieces to pieces by round8_q7 Lemma S″.
- **Non-product G.** Pieces of Â_t are components of ξ_G^{-1} of the curves H_t(components of A_0). There are finitely many of them, and each is mapped finitely onto its image. Step 0 then still yields finitely many families of pieces. However, the continuous choice E_t needed in Step 6 is available only away from the "twin" branching (round8_q7, Caveat after Lemma S″).

Hence (b), the finiteness, holds in all strata. (c), constancy, holds in product-type strata. In non-product strata it holds after replacing Δ by the finite branched cover of Δ on which the lifts are continuous; finiteness, which is all that (Rig) asks for, is unaffected. ∎

**What (T_c) amounts to.** By Lemma CL, (T_c) holds iff two conditions hold:
- (α) for every t, the transported cone data of Λ_E dominate the joint minimal orbifold structure of ν_t. Equivalently, no cone point of the joint vertex map is created, split or moved away from the transported Λ_E cone points;
- (β) the joint monodromy is constant in t, as a coset-valued homomorphism.

This is (O_G) of round7_q9 with the *specific* structure Λ_E. Lemma J0 is what makes this structure available for all vertices at once.

**Sketch (not proved): (T_c) under (★_J) and (★∞_J).**
- The joint lift F_0 of Lemma J0 is an injective holomorphic immersion H → T_G, because its j-coordinate is.
- So the local analysis of round6_q7 (Lemma N, Prop. L1, Cor. L2, Prop. L3) applies with T replaced by T_G, f_0 by F_0, and Stab(X̂) by Stab_{Mod_Π}(F_0(c̃)) modulo S. It only needs a smooth disc germ L with faithful action under (★).
- **(★_J) at c ∈ Ê_0:** every element of Stab_{Mod_Π}(F_0(c̃)) lies in R(λ) for some λ ∈ Stab_Λ(c̃), up to S.
- **(★∞_J):** the boundary points of E_0 in ∏M̄_w have no effective automorphisms.
- If (★_J) and (★∞_J) hold everywhere, Theorem L's argument gives (α) and (β), hence (T_c) and (Rig) for that piece.

This inherits the "careful sketch" status of Theorem L §3.3, and I have not re-verified Prop. L1 in the product target. In particular it covers pieces whose joint image, at t = 0, avoids the orbifold locus of ∏M_w (modulo generic automorphisms) and whose boundary points have no automorphisms (round7_q9 §2.5).

**What remains open under (R2).** The three mechanisms (cross), (fix), (ram) of round6_q7 §4, now for the joint map: cone points of the joint vertex map of E_t appearing at t ≠ 0 at points that are not transported cone points of Λ_E. Lemma J0 excludes such points at t = 0 only. The dead ends recorded earlier still apply:
- local data cannot exclude these mechanisms (round6_q7 §4, round9_q9 Lemma Loc);
- area and Schwarz–Pick inequalities go the wrong way (round7_q7 §4).

## 8. Final status

**Proved here**, under (R1) and (R2), with the prior results TV and Corollary Φ̂ of round8_q10 used as stated and not re-proved:
- **Lemma CS, Lemma CL** (§2): elementary lifting lemmas.
- **Lemma J0** (§3, no (R2^orb)):
  - at t = 0, the whole vertex map of every piece, in any stratum, lifts holomorphically over the Veech-type orbifold H/Λ_E;
  - the Teichmüller coordinate of this lift is an isometric embedding onto a Teichmüller disc;
  - the monodromy is coset-valued (cosets of the finite pointwise stabiliser S).
  - Consequences: joint (H_0); the joint minimal orbifold structure at t = 0 is dominated by Λ_E; Example Z is not a boundary piece of a totally geodesic V_0.
- **Proposition T** [orb] (§4): (R2^orb), read as (a)–(d) of §1, implies (O_G), (O), (O_u) and (OT) for every piece, with the orbifold structure Λ_E.
- **Lemma R*′** [orb] (§5): Lemma R* with coset-valued monodromy and with orientation reversal excluded. It gives (Rig-v) and a biholomorphism ā_t : Ê_0 → Ê_t.
- **Theorem RO** [orb] (§6): (Rig) for every admissible family under (R2^orb), in product and non-product strata. Moreover:
  - M(E_t) = M(E_0);
  - K(E_t) = K(E_0);
  - puncture values lie in a fixed finite set.
- **Proposition C** (§7, coarse reading): (Rig) follows from the transport hypothesis (T_c) for the Λ_E structure.

**Cited from memory:**
- Royden, Earle–Kra / Gardiner;
- Bers' classification;
- Thurston's stretch theorem (finite-area version);
- Selberg's lemma;
- uniformisation of hyperbolic 2-orbifolds and lifting of orbifold homeomorphisms;
- Bers embedding (boundedness of T_w);
- Cartan's linearisation and quotient theorem;
- density of intersection points of axes of a lattice;
- Imayoshi–Shiga finiteness, with the caveat on its scope stated in §6.

**Dependencies not re-checked:**
- Theorem TV and Corollary Φ̂ (round8_q10), in particular:
  - the choice φ̂(i) = P̂ with P̂ generic on E;
  - TV item 2, E^ν = H/Λ_E with Λ_E ⊂ Γ′;
  - Lemma PA, which round8_q10 itself cites from memory.
- The claim that under (R2^orb) MS11♭ holds (round11_q4), and the chain step "(Rig) + MS11♭ ⇒ the problem's claim" (entry 124).
- If these hold, Theorem RO completes a proof of the problem's claim **under the reading (R2^orb)** of §1. That conclusion is conditional on those prior results and is not established here.

**Weakest form of (Rig) obtained:**
- Unconditionally on the orbifold reading: (Rig) for every piece satisfying (T_c) (Prop. C). In sketch, (T_c) holds for every piece satisfying (★_J) and (★∞_J).
- Under (R2^orb): (Rig) in full, with constancy of the triples.

**Open (named):**
1. **(Rig) under the coarse reading (R2)**: equivalently (T_c) for every piece. Precisely, can the joint vertex map of E_t, t ≠ 0, acquire cone points not transported from Λ_E (mechanisms cross/fix/ram of round6_q7 for the joint map)?
2. **Local-to-global for (R2^orb)**: does the purely local formulation (isotropy-preserving local lifts at each z ∈ closure(V_0)) imply the global equivariant lift (a)–(d) of §1?
3. The exact scope of Imayoshi–Shiga finiteness for targets M_{h,m}[N] with marked points (h = 0 or (h,m) = (1,1) included?).
4. Realisability questions Q1/Q2 of earlier rounds. For Example Z′, whether J_0∘q lifts to T_{1,1} (Lemma J0's criterion).

**Entry 82 overall: not proved in general; proved under (R2^orb) (partial: conditional on that reading and on round8_q10's TV/Φ̂); open under the coarse reading.**


## round13_q9 (verbatim): independent verification of round12_q9
# round13_q9 — verification of round12_q9 (Lemma CS, CL, J0, 1.1, Prop. T, Lemma R*′, Theorem RO, Prop. C)

**Plan/status line (written first).** I read the whole brief, including round12_q9 verbatim. I check each lemma inference by inference, in the order CS, CL, J0, 1.1 (with O_t, h̃_t, θ_t), Prop. T, R*′, RO, Prop. C. Then I give the verdicts.

**Status at the end.**
- No fatal gap found.
- Three minor repairs are needed, all supplied below:
  - (R1′) finite type of Ê_t: the argument given is incomplete, and is repaired by algebraicity;
  - (R2′) the definition of the torsion-free level subgroups Mod_w[N] in genus 0 and type (1,1);
  - (R3′) the labelled lift φ̂(i) = P̂ in non-product strata: repaired by Aut(G)-relabelling.
- Proposition C's non-product clause is only a sketch.
- Every external input is cited from memory, by me as in round12_q9: Bers, Thurston, Royden, Selberg, Imayoshi–Shiga, orbifold uniformisation, Cartan.
- Theorem RO also depends on prior results that I did not re-check because they are not spliced: TV items 1–3 (the proofs of round8_q10 §4, Steps 2′–5) and Lemma PA. It also depends on the reading (R2^orb) in its global form (a)–(d).

Notation is that of round12_q9. "✓" means I checked the inference and it is valid.

---

## 1. Lemma CS — correct

- Q = ∪_{g∈Γ} Z_g with Z_g = {F′ = gF}. Each Z_g is the coincidence set of two holomorphic maps into a manifold, so it is closed analytic. Γ is countable and Q is a Baire space, so some Z_g has interior. Q is connected, so the identity theorem gives F′ ≡ gF. ✓
- If gF ≡ g′F, then g^{-1}g′ ∈ S_F. So the solution set is the coset gS_F. ✓
- S_F ⊂ Stab_Γ(F(y)), which is finite because the action is properly discontinuous. ✓

## 2. Lemma CL — correct

- **Chart.** Stab_Γ(x̂) = A is finite. Cartan's linearisation gives an A-invariant ball B with linear A-action. By proper discontinuity, B can be shrunk so that gB ∩ B ≠ ∅ ⇒ g ∈ A. By the definition of Cartan's quotient structure, B/A → X is an open embedding. ✓
- **Holomorphy of σ̄∘h.** The A-invariant polynomials σ_k are A-invariant holomorphic functions on B. By definition of the quotient structure sheaf, they are holomorphic functions on B/A. So σ̄∘h is holomorphic on Q_0, since h(Q_0) = p(L(Q_0)) ⊂ B/A. ✓ (The embedding property of σ̄ is not needed. Only two facts are used: σ separates A-orbits, which holds for finite groups, and σ_k descends.)
- **Z.** Z is analytic, and its fibre over y is {b ∈ B : σ(b) = σ(L(y))} = A·L(y), because σ separates orbits. ✓
- **Properness.** For compact K ⊂ Q_0, Z ∩ (K × B) is a closed subset of K × A·L(K), which is compact. ✓
- **Σ is discrete.** Sing Z and the 0-dimensional part are closed and discrete. On Reg Z the critical points of the projection are discrete, since a 1-dimensional component of critical points would be a curve on which the projection is constant, i.e. a curve inside a finite fibre. Images of closed discrete sets under a proper finite map are closed and discrete. ✓
- **Covering.** Over Q_0∖Σ, Z is a 1-manifold mapping by a proper local biholomorphism, hence a finite covering whose sheets are graphs of holomorphic maps. ✓
- **Conclusion.** y ↦ (y, L(y)) is a continuous section. Over a connected evenly covered disc it stays in one sheet, so L is holomorphic off Σ. L is bounded in the ball coordinates and continuous, so Riemann's extension theorem makes it holomorphic on Q_0. ✓

## 3. Lemma J0 — correct, given TV items 1–3 and Corollary Φ̂ as stated (one minor repair in non-product strata)

### 3.1 What TV and Φ̂ actually state, against what J0 quotes

**(a) Is there a continuous Φ : H → T_G with 1-Lipschitz coordinates?**
- Yes. Corollary Φ̂ gives, along a subsequence, maps φ̂_w : H → T(Σ_w), each 1-Lipschitz from d_H (curvature −4) to d_T.
- Put Φ := (φ̂_w)_w. It is continuous, and p∘Φ = ([φ̂_w])_w = φ̂.
- Φ̂ also states φ̂(H) ⊂ Â, using that X^g_n ∈ V_0 by total geodesy. ✓

**(b) pr_j∘Φ = D?**
- Φ̂ states: "if moreover v carries positive area η_v, then … φ̂_v = D (as maps to T(Σ_v))".
- The proof of TV supplies positive area at the vertex j, via Lemma PA (cited from memory in round8_q10) and Lemma TR. TV's D is the Teichmüller disc of (Y_j, η_j) with Y_j = P̃_j, which is the same D.
- So pr_j∘Φ = D holds, **conditional on Lemma PA**. ✓

**(c) φ̂(i) = P̂ with P̂ generic?**
- This is **not** in the statement of Φ̂. It is asserted in the proof of TV: "φ̂(i) = P̂ (the labelled lift defined by the plumbing markings is P̂)".
- What Φ̂ itself gives is φ̂(i) = λ(P̃), the labelled lift of the limit of (X_n, f_n), since g = 1 gives X^1_n = X_n.
- **Product type** (ξ_G = id): λ(P̃) = P = P̂ automatically. ✓
- **Non-product type:** λ(P̃) is one of the finitely many points of ξ_G^{-1}(P). It equals P̂ only through the labelled plumbing chart (Pl), which round8_q10 says it has "only described".
- **Repair (R3′).** In general λ(P̃) = σP̂ for some σ in the finite group Mod_G/Mod_Π acting on ∏M_w. That group acts because Mod_Π ⊲ Mod_G.
  - σP̂ is again generic: it lies off Sing Â and off the other components, since σ permutes the components of the σ-invariant set Â.
  - So Steps 1–5 below run verbatim for the piece σE.
  - Then a lift σ̃ ∈ Mod_G of σ^{-1} gives σ̃∘F, which satisfies (i)–(iii) for E. It uses the vertex σ^{-1}(j), the same Λ (E^ν ≅ (σE)^ν via σ), S replaced by σ̃Sσ̃^{-1}, and R(λ) by σ̃R(λ)σ̃^{-1}. This uses that σ̃ normalises Mod_Π.
  - So J0 holds for every piece, with the Teichmüller vertex and disc transported by σ. Nothing downstream uses the specific j.

**(d) E^ν = H/Λ_E with Λ_E ⊂ Γ′?**
- TV item 2 states it: "E^ν ≅ H/Λ_E for a subgroup Λ_E ⊂ Γ′ of index deg p". Item 3 states that the lift of π_j∘ν to the universal cover is D.
- This is what J0 quotes: p_E∘q = q_{Γ′} and κ∘q_{Γ′} = u.
- The proof of item 2 (round8_q10 §4, Steps 2′–5) is **not spliced**, so I could not check it. It is a dependency.
- **Remark (partial independent check).** Given Φ̂ alone, Steps 2–3 below produce a holomorphic φ^ν : H → E^ν with p_E∘φ^ν = q_{Γ′}. Suppose one also knows that p_E : E^ν → C^ν is proper (TV items 2 and 4: ends go to cusps). Then:
  - At a point x ∈ H that is not an elliptic fixed point, q_{Γ′} has local degree 1. So p_E has local degree 1 at φ^ν(x), and p_E is unbranched over C^ν∖Br.
  - A proper unbranched finite map is a covering. So φ^ν restricted to H^♮ is a covering of p_E^{-1}(C^ν∖Br), with deck group a finite-index Λ_E ⊂ Γ′.
  - Hence E^ν ≅ H/Λ_E, after filling in the cone points.
  - So TV item 2 reduces to **properness of p_E** (TV item 4). That is the only part of TV's §4 that J0 really needs beyond Φ̂ and Lemma PA.

### 3.2 Steps of J0

**Step 1 (φ̂(H) ⊂ E).** ✓, including non-product strata. The argument is purely topological in ∏M_w.
- Â is closed in ∏M_w and of dimension ≤ 1: it lies in the boundary, and closure(V_0) is an irreducible surface not contained in it.
- Z is a locally finite union of points and curves.
- For a compact disc K ⊂ H, φ̂(K) meets only finitely many of the following: points of E ∩ E′ (closed discrete), isolated points, and components on which π_j is constant. So π_j takes finitely many values on φ̂(K) ∩ Z.
- Hence φ̂^{-1}(Z) ∩ K ⊂ u^{-1}(finite) ∩ K, which is finite because u = κ∘q_{Γ′} is non-constant. Here π_j∘φ̂ = u needs (b).
- **Clopen argument.** Â∖Z = (E∖Z) ⊔ ⋃_{E′}(E′∖Z), where the union runs over E′ ≠ E with π_j non-constant on E′. E∖Z misses every E′, because points of E on other components lie in Z. Both parts are relatively closed, the second by local finiteness.
- i ∈ φ̂^{-1}(E∖Z), because P̂ is non-isolated, off the other components, and therefore off Z.
- H° is connected, so φ̂(H°) ⊂ E. E is closed and H° is dense, so φ̂(H) ⊂ E.
- **Non-product strata:** the only issue is (c) above, which is repaired by (R3′).

**Step 2 (φ̂ holomorphic).** ✓
- Σ_E is discrete in E. It consists of Sing E, the critical points of π_j on Reg E, and the preimage of the discrete set Sing C. A non-constant map from an irreducible curve has discrete fibres. Finiteness of π_j|_E is not needed.
- φ̂^{-1}(Σ_E) is discrete. Σ_E is closed and discrete in the closed set E, so it meets φ̂(K) in a finite set; then argue as in Step 1.
- At x with φ̂(x) = e ∉ Σ_E: by continuity φ̂ maps a neighbourhood of x into a neighbourhood U_e on which π_j is a biholomorphism onto a neighbourhood of a smooth point of C. There φ̂ = (π_j|_{U_e})^{-1}∘u, which is holomorphic.
- Riemann extension in a local embedding of ∏M_w then gives holomorphy everywhere.

**Step 3.** ✓
- The lift φ^ν exists by the universal property of normalisation: H is smooth and φ̂^{-1}(Sing E) is discrete.
- κ∘p_E∘φ^ν = u = κ∘q_{Γ′}. Since κ is injective off a finite set N and q_{Γ′} is non-constant, the two maps agree off the discrete set q_{Γ′}^{-1}(κ^{-1}κ(N)), hence everywhere.

**Step 4.** ✓
- Over C^ν∖Br, H/Λ → H/Γ′ is the covering H^♮/Λ → H^♮/Γ′, since both groups act freely on H^♮. The fibre over [x_0] is {Λγx_0 : γ ∈ Γ′}.
- φ^ν and q∘γ_0 are lifts of q_{Γ′}|_{H^♮} that agree at x_0. H^♮ is connected, so they agree on H^♮, and by density on H.

**Step 5.** ✓
- F := Φ∘γ_0^{-1}, and p∘F = φ̂∘γ_0^{-1} = ν∘φ^ν∘γ_0^{-1} = ν∘q.
- Lemma CL applies with T = T_G and Γ = Mod_Π. The action is properly discontinuous, the group is countable, and T_G/Mod_Π = ∏M_w as analytic spaces. So F is holomorphic.
- (ii): pr_j∘F = D∘γ_0^{-1}, and γ_0^{-1} is a biholomorphic isometry of H.
- (iii) R(λ) is a coset of S: by Lemma CS, since p∘F∘λ = ν∘q∘λ = ν∘q.
- (iii) Normality: if g ∈ R(λ) and s ∈ S, then s g F = s(F∘λ) = (sF)∘λ = F∘λ = gF, so g^{-1}sg ∈ S.
- (iii) Product rule: by normality gS·hS = ghS, and ghS ⊂ R(λμ) is a coset of S, hence equal to R(λμ). ✓

**Consequences.**
- "Example Z cannot occur at t = 0" is correct. At a simple zero z_* of J_0 that is not a cone point of Λ_E, a holomorphic lift L to T_{1,1} = H would satisfy J_0 = (unit)·(L − L_*)^3 near z_*, contradicting the simple zero.
- At z = 0, which is a cone point of order 2, J_0∘q ~ w² is not a cube.
- This is a remark only and is not used downstream.

**Verdict on J0: correct, with the repair (R3′) in non-product strata.** It is conditional on TV items 1–3 (equivalently on properness of p_E, by the Remark in 3.1(d)), on Corollary Φ̂, and on Lemma PA/TR for positive area at j.

## 4. Lemma 1.1 and the transported orbifold — correct after repair (R1′)

**Descent.** ✓ By (b) for Mod_Π, the map p∘H̃_t is Mod_Π-invariant on the saturated set Ã_0, so it descends. By (a), ξ_G Π_t(px) = H_t(ξ_G px) ∈ A_t, so Π_t lands in Â_t.

**Injectivity on Ã_0.** ✓
- H̃_t x = H̃_t y gives H_t ξ_G p x = H_t ξ_G p y, so ξ_G p x = ξ_G p y, so y = gx with g ∈ Mod_G. This uses that ξ_G∘p is the quotient by Mod_G.
- Then gH̃_t x = H̃_t x, so g ∈ Stab(H̃_t x) = Stab(x) by (c), and y = x.
- Only the inclusion Stab(H̃_t x) ⊂ Stab(x) is used.

**Surjectivity onto Ã_t.** ✓ Ã_0 is Mod_G-invariant.

**Bijectivity of Π_t.** ✓

**Joint continuity.** ✓ Restricted to the saturated set Ã_0 × Δ, p × id is still open onto Â_0 × Δ: (U ∩ p^{-1}B) maps onto p(U) ∩ B. So p × id is a quotient map, and continuity descends.

**Continuity of Π_t^{-1}.** ✓
- H_t is a homeomorphism closure(V_0) ∩ Δ_G → closure(V_t) ∩ Δ_G, by (R2).
- ξ_G is proper and Â_0 is closed in ∏M_w.
- Every limit point x satisfies Π_t x = y, and is unique by injectivity.

**Pieces to pieces.** ✓
- In a ≤1-dimensional analytic set, isolated points are topologically characterised.
- A non-isolated point has a disc neighbourhood iff it lies on exactly one irreducible local branch.
- The set of such points on a component E is the image of the connected normalisation minus a discrete set, so it is connected and dense in E. Two different components can meet only at non-manifold points.
- So the components of the 1-dimensional part are the closures of the connected components of the "disc points", and a homeomorphism permutes them.
- Surjectivity of Π_t gives "every piece at time t arises".

**Ĥ_t on normalisations.** ✓ Local branches are the components of punctured links.

**Gap in "Ê_t has finite type with puncture ends", and repair (R1′).**
- The argument says that Ê_t maps finitely onto the normalisation of closure(ξ_G E_t) minus finitely many points, and that "a finite unbranched cover of a punctured disc is a disjoint union of punctured discs".
- But nothing shown makes the map unbranched near the punctures. A finite branched (even Galois) cover of a punctured disc may have branch points accumulating at the puncture and infinite genus; e.g. w² = sin(π/z) over 0 < |z| < 1.
- **Repair.**
  - By (R1), closure(V_t) is a closed analytic subset of the projective variety M̄_g, hence algebraic by Chow's theorem (from memory).
  - Δ_G is locally closed algebraic, and ξ_G : ∏M_w → Δ_G is a finite algebraic morphism of quasi-projective varieties.
  - So Â_t is a quasi-projective algebraic set and E_t is an irreducible quasi-projective curve.
  - Its normalisation is a smooth quasi-projective curve, i.e. a compact Riemann surface minus finitely many points, whose ends are conformal punctures.
- Ĥ_t is a homeomorphism, so it maps ends to ends, i.e. punctures to punctures. With this repair the statement is correct.

**Transported orbifold O_t.** ✓ given (R1′).
- O_t has the signature of O_0, so χ^orb(O_t) = χ^orb(O_0) < 0.
- Its underlying surface is a compact Riemann surface minus finitely many points.
- So the uniformisation theorem for hyperbolic 2-orbifolds (from memory; there are no bad orbifolds since χ < 0) gives a lattice Λ_t whose cusps are exactly the punctures, with holomorphic u_t. Finite type is exactly what makes the ends cusps rather than funnels; this is why (R1′) matters.

**h̃_t and θ_t.** ✓
- A homeomorphism of underlying surfaces sending cone points to cone points of the same order and punctures to punctures is an orbifold homeomorphism. Locally at a cone point, a homeomorphism of punctured discs lifts through z ↦ z^e.
- So it lifts to h̃_t : H → H with u_t∘h̃_t = Ĥ_t∘u_0.
- For λ ∈ Λ_t: u_0∘(h̃_t^{-1}λh̃_t) = Ĥ_t^{-1}u_tλh̃_t = u_0. So h̃_t^{-1}λh̃_t is a deck transformation of the Galois covering H^♮ → H^♮/Λ, where H^♮ is H minus the elliptic fixed points. Hence it lies in Λ, and θ_t is a well-defined isomorphism.
- h̃_t may a priori reverse orientation. Nothing proves Ĥ_t orientation-preserving, but R*′ handles that case, and Prop. T does not need it.

## 5. Proposition T — correct

- F_0(H) ⊂ Ã_0, since p F_0 = ν_0 u_0 ∈ Â_0. So F_t = H̃_t∘F_0∘h̃_t^{-1} is defined and continuous.
- p F_t = Π_t p F_0 h̃_t^{-1} = Π_t ν_0 u_0 h̃_t^{-1} = Π_t ν_0 Ĥ_t^{-1} u_t = ν_t u_t. This uses ν_t Ĥ_t = Π_t ν_0 and u_t h̃_t = Ĥ_t u_0.
- ν_t u_t is holomorphic, so F_t is holomorphic by Lemma CL. ✓
- (2): h̃_t^{-1}λ = θ_t(λ)h̃_t^{-1}. Then F_0∘θ_t(λ) = gF_0 for g ∈ R(θ_tλ), and (b) gives H̃_t g = g H̃_t. ✓
- The key point is that no local orbifold analysis is needed: Lemma CL turns the continuous transported lift into a holomorphic one. The monodromy is transported by construction, with no continuity-in-t argument.
- Only (a), (b) and (c) of (R2^orb) are used, with (c) entering through Lemma 1.1. ✓

## 6. Lemma R*′ — correct

**Step 1: Bers' classification for g ∈ R_j(μ).**
- g = pr_j(g̃) with g̃F_0 = F_0∘μ, so g f_0 = f_0 μ.
- f_0 is an isometric embedding onto 𝔇 (J0(ii)). So g preserves 𝔇 = f_0(H) and acts on it as f_0 μ f_0^{-1}.
- The image f_0(α_μ) of the hyperbolic axis is a Teichmüller geodesic, and g translates it by **exactly** ℓ_0(μ) > 0. This is because f_0 is an isometry for the matching normalisations (curvature −4 on H, as in Φ̂). ✓
- **Pseudo-Anosov, justified directly.** g is represented on X = f_0(x), x ∈ α_μ, by a map that is affine for the defining differential q, with derivative diag(e^{ℓ}, e^{−ℓ}).
  - Horizontal saddle connections and horizontal cylinder circumferences form finite sets of lengths permuted by a power of g, yet they are scaled by e^{kℓ} ≠ 1. So there are none.
  - Hence the horizontal foliation is minimal and filling, and likewise the vertical one. So g is pseudo-Anosov.
- Bers (from memory): for pseudo-Anosov g, τ_T(g) = inf d(X, gX) is attained exactly on the unique invariant Teichmüller geodesic. Along that geodesic the translation equals τ_T(g).
- Since f_0(α_μ) is g-invariant, it is the axis. So τ_T(g) = ℓ_0(μ) and Min(g) = f_0(α_μ). ✓
- Elements of the kernel K of Mod_j → Aut(T_j) are harmless, since everything concerns the action on T_j.

**Step 2: direction of the inequality.**
- θ_t is conjugation by a homeomorphism that maps punctures to punctures. So it preserves elliptic (fixed point in H), parabolic (peripheral) and hyperbolic (the rest), and θ_tγ is hyperbolic. ✓
- Prop. T(2) gives f_t(γx) = g f_t(x). Royden gives τ_T(g) ≤ d_T(f_t x, f_t γx) ≤ d_H(x, γx) = ℓ_t(γ).
- So ℓ_t(γ) ≥ ℓ_0(θ_tγ): the time-t lengths dominate. This is the direction Thurston needs. ✓

**Step 3: Thurston on H/Λ′ versus H/Λ′_t.**
- Λ′_t = θ_t^{-1}(Λ′) is torsion-free, normal and of finite index in Λ_t.
- h̃_t λ′ h̃_t^{-1} = θ_t^{-1}(λ′) ∈ Λ′_t, so h̃_t descends to a homeomorphism H/Λ′ → H/Λ′_t inducing θ_t^{-1} on deck groups.
- Both surfaces are complete and of finite area, and the marking is type-preserving (cusps to cusps).
- Closed geodesics correspond to hyperbolic conjugacy classes, and Step 2, applied to γ = θ_t^{-1}(λ′), gives ℓ_{H/Λ′_t}(h̃_t c) ≥ ℓ_{H/Λ′}(c) for every closed curve c.
- Thurston's theorem (from memory, "Minimal stretch maps…", which covers complete finite-area surfaces with cusps): sup_c ℓ_X(c)/ℓ_Y(c) ≥ 1, with equality iff X = Y in Teichmüller space. Equivalently, the optimal Lipschitz constant is ≥ 1 by the area comparison of equal-area surfaces, with equality only for an isometry in the marking class. Here the sup is ≤ 1, so the structures coincide. ✓
- **Orientation.** If h̃_t reverses orientation, replace H/Λ′_t by its complex conjugate. Lengths are unchanged and the marking becomes orientation-preserving, so the resulting isometry is orientation-reversing. This is correct.
- **The lift A_t.** Lifting the homotopy between the isometry and the descended h̃_t gives an equivariant homotopy, so the lift A_t satisfies A_tλ′A_t^{-1} = θ_t^{-1}(λ′) on Λ′. The conjugation is constant along the homotopy by discreteness. ✓

**Extension from Λ′ to Λ.** ✓ (I re-did the computation.)
- Put ψ(x) := A_t^{-1}θ_t^{-1}(x)A_t. Then ψ = id on Λ′, and c := λ^{-1}ψ(λ).
- For λ′ ∈ Λ′: cλ′c^{-1} = λ^{-1}ψ(λλ′λ^{-1})λ = λ′, using normality of Λ′.
- The centraliser of a lattice in the full Isom(H) is trivial. If c commutes with a hyperbolic λ′, it maps the attracting fixed point of λ′ to the attracting fixed point of cλ′c^{-1} = λ′, so it fixes both fixed points. Fixed points of hyperbolic elements are dense in ∂H. An isometry fixing ∂H pointwise is the identity; a reflection fixes only 2 boundary points.

**Step 4: k_t = f_0.** ✓
- k_t(μx) = f_t(θ_t^{-1}(μ)A_t x) = g k_t(x) for g ∈ R_j(μ).
- For x on α_μ: d(k_t x, g k_t x) ≤ ℓ_0(μ) = τ_T(g), so k_t x ∈ Min(g) = f_0(α_μ).
- At a transverse intersection x of two axes, injectivity of f_0 gives k_t(x) = f_0(x).
- For a lattice, pairs of axis endpoints are dense in ∂H × ∂H, so such intersection points are dense. Continuity then gives k_t = f_0.
- **Orientation.** If A_t were anti-holomorphic, k_t would be both anti-holomorphic and equal to the non-constant holomorphic f_0. Then ∂k = ∂̄k = 0, which is impossible. So A_t ∈ PSL_2(ℝ). ✓
- ā_t is a biholomorphism, and π_j ν_t ā_t = π_j ν_0. ✓

## 7. Theorem RO — correct after repair (R2′), given (R2^orb), TV/Φ̂ and (IS)

**Step 0.** ✓
- closure(V_0) ∩ closure(Δ_G) is compact analytic, and A_0 is its open part in Δ_G. So A_0 has finitely many components.
- The preimage under a finite map of a curve with finitely many components has finitely many components.
- Lemma 1.1 gives "every piece at time t is Π_t(E_0)".

**Step 1: torsion-free level subgroup and the homomorphism r.**
- **Repair (R2′).** Mod_w[N] must be specified, since H_1 of a closed genus-0 surface is 0. Define Mod_w[N] := PMod_w ∩ ker(PMod_w → Sp(2g_w, ℤ/N)), with N ≥ 3 and pure mapping classes. For g_w = 0 this is all of PMod_{0,n}. It is torsion-free:
  - a finite-order pure class is realised by an automorphism of some (X, marked points) fixing every marked point;
  - for g = 0, n ≥ 3, such an automorphism is a Möbius map fixing 3 points, hence the identity;
  - for g = 1, n ≥ 1, it is a group automorphism with the marked point as origin, acting trivially on H_1, hence the identity — the elliptic involution acts by −1 ≢ 1 mod N;
  - for g ≥ 2, Serre's lemma (trivial on H_1(·;ℤ/N), N ≥ 3 ⇒ trivial on H_1) and Hurwitz's theorem give the identity (from memory).
- So Mod[N] = ∏Mod_w[N] is torsion-free and normal of finite index in Mod_Π. Its stabilisers in T_G are finite, hence trivial, and M[N] = T_G/Mod[N] is a manifold.
- The homomorphism λ ↦ R(λ) ∈ N(S)/S is J0(iii). ✓
- Mod[N]S is a subgroup because Mod[N] is normal. (N(S) ∩ Mod[N]S)/S has finite index ≤ [Mod_Π : Mod[N]] in N(S)/S. So Λ^N has finite index. ✓
- Λ″ exists by Selberg plus the normal core. ✓
- For μ ∈ Λ″: R(μ) = gS with g = ms, m ∈ Mod[N], s ∈ S. Then m = gs^{-1} ∈ R(μ), and uniqueness holds since S ∩ Mod[N] = 1. So r is a homomorphism. ✓

**Step 2.** ✓
- g_t(μx) = F_t(θ_t^{-1}(μ)A_t x) = r(μ)g_t(x). The equivariance r is **independent of t**. This is the crucial point, and it holds by Prop. T(2) and R*′.
- R = H/Λ″ is a finite-area surface of finite type.
- p g_t = ν_t u_t A_t = ν_t ā_t u_0, so E_t is the image of R. ✓

**Step 3: free homotopy.** ✓
- M_w[N] is a K(π,1), being a free quotient of the contractible T_w, and R is a CW complex.
- So free homotopy classes of maps R → M_w[N] correspond to homomorphisms Λ″ → Mod_w[N] up to conjugacy.
- ḡ^w_t induces r_w for every t, so all ḡ^w_t are freely homotopic.

**Step 4: the non-constancy criterion.** ✓
- If ḡ^w_t is constant, then g^w_t is constant, since its fibres are discrete orbits and H is connected. Then r_w(Λ″) ⊂ Stab(y) is finite, hence trivial.
- If r_w = 1, then g^w_t descends to R → T_w. T_w is bounded by the Bers embedding (from memory), and R = R̄ minus finitely many points. Bounded holomorphic functions extend over the punctures and are then constant on the compact R̄.
- Since M_w[N] → M_w is finite-to-one, f^w_t is constant iff ḡ^w_t is. This gives (a).

**Step 5: (IS).**
- **The version I recall (from memory, not checked against the paper).** Imayoshi–Shiga, MSRI Publ. 11 (1988), state for holomorphic families of Riemann surfaces of type (g,n), i.e. genus g with n punctures, 2g−2+n > 0, over a Riemann surface B of finite type:
  - (Rigidity) two locally non-trivial families with the same monodromy are holomorphically equivalent;
  - (Finiteness) there are only finitely many locally non-trivial families.
- I believe punctured types, including g = 0 and (1,1), are covered: the proof works on T_{g,n} and the Bers fibre space. I cannot confirm this from the text.
- **Application.** RO applies (IS) **factor by factor**, to ḡ^u_t : R → M_u[N] for u ∈ M(E_0). So product targets are not needed: a finite choice in each factor gives a finite set of tuples.
- Translation into the needed statement: under rigidity, two non-constant homotopic ḡ^u_t, ḡ^u_{t′} give equivalent families, so their classifying maps to the coarse M_u agree. Lifts of one map R → M_u through the finite map M_u[N] → M_u differ by elements of Mod_u/Mod_u[N]: argue as in Lemma CS on the lifts to T_u, then descend. So there are at most |Mod_u/Mod_u[N]| maps in each homotopy class. This is the "finitely many" used. ✓
- **Robustness for (1,1) and (0,4).** M_u[N] is then a hyperbolic curve. Every non-constant holomorphic map from a finite-type R has non-elementary monodromy: maps to D* or to an annulus are bounded, hence constant. Homotopic non-constant holomorphic maps into a hyperbolic curve with non-elementary monodromy are equal (classical Schwarz–Pick rigidity; from memory). So these types do not depend on the scope of (IS).

**Step 6: constancy.** ✓
- T_K is closed, by joint continuity of Π. Every point Π_{t*}(x) is the limit of Π_{t_n}(x) ∈ E_{t_n}, and K is closed, so pr_M(E_{t*}) ⊂ K.
- K(E_{t*}) is an irreducible curve, by (a) and irreducibility. So it equals K.
- The T_K are finitely many, pairwise disjoint and closed, and they cover the connected Δ. So K(E_t) ≡ K(E_0).
- Using Π avoids needing continuity in t of h̃_t or A_t, which is never established. This is a good design choice.
- **Puncture values.**
  - At a puncture p of Ê_t some u ∈ M degenerates. If no vertex degenerated, the limit would lie in the closed set Â_t, hence in E_t. That contradicts properness of the normalisation Ê_t → E_t. Constant vertices cannot degenerate.
  - So the joint limit lies in the finite set K(E_0) ∖ ∏_{u∈M}M_u, and every coordinate f_u(p), u ∈ M, including non-degenerate ones, is a coordinate of one of these finitely many points.
  - This excludes the Z′ mechanism. ✓

**Is the conclusion exactly (Rig)?** Yes.
- 𝒦 = {(G, M(E_0), K(E_0))} is finite (Step 0).
- Every piece of Â_t, at every t and in every stratum, is Π_t(E_0) with the same triple.
- RO in fact gives this **without** quotienting by Aut(G): all labelled lifts are tracked individually by Π_t. That is stronger than "up to Aut(G)".
- (Rig-w) and the joint-image form follow, since K(E_t) = K(E_0).

## 8. Proposition C and §7 of round12_q9

**Product type.** Correct.
- Π_t := H_t on the stratum is a homeomorphism mapping pieces to pieces, by Lemma S″ (re-checked in §4 above).
- Ĥ_t, O_t, θ_t are then defined, and (T_c) replaces Prop. T verbatim in R*′ and RO.
- (R1′) is needed here as well.

**Non-product type.** This is a sketch only, and it has a gap.
- (T_c) presupposes a family E_t with transport Ĥ_t.
- Under coarse (R2), pieces of Â_t are components of ξ_G^{-1}(H_t(·)). Their continuous choice in t can branch (twins), and the claim that a finite branched cover of Δ makes the lifts continuous is not proved.
- (b), finiteness, is plausible but is not proved there either: (T_c) is not even formulated without such a choice.

**"(T_c) ⟺ (α) ∧ (β)" and the (★_J) sketch.** These are heuristic, are not proved, and are not used by RO.

## 9. Verdicts

**Lemma CS: correct. Lemma CL: correct.**

**Lemma J0: correct after the stated repair (R3′)**, which is needed in non-product strata only. Conditional on:
- Corollary Φ̂;
- TV items 1–3. By §3.1(d), item 2 reduces to properness of p_E (TV item 4), given Φ̂;
- Lemma PA/TR (positive area at j), which round8_q10 itself cites from memory.

None of these proofs is spliced into this brief, so none was re-checked.

**Lemma 1.1: correct after repair (R1′)**, i.e. finite type of Ê_t via Chow's theorem.

**Proposition T: correct.**

**Lemma R*′: correct.** Bers is applied correctly, with the pseudo-Anosov property justified directly. The inequality goes the right way. Thurston is applied to type-preserving markings of finite-area cusped surfaces, with orientation handled. The extension to Λ is valid in the full Isom(H). Step 4 is valid.

**Theorem RO: correct after the stated repairs (R1′), (R2′)** (and (R3′) through J0). Its conclusion is exactly (Rig), indeed in a labelled, Aut(G)-free form. Conditional on:
- the reading (R2^orb) in its global form (a)–(d);
- TV/Φ̂/PA as above;
- Imayoshi–Shiga, in the version stated in §7, from memory. For vertex types (1,1) and (0,4) it can be replaced by classical rigidity of maps to hyperbolic curves.

**Proposition C: correct for product-type strata (with (R1′)). The non-product clause is a gap (sketch).**

## 10. Open / not checked here

1. TV items 1–4 and Lemma PA (round8_q10 §4 and the cited PA) are not re-checked. J0 needs Φ̂, positive area at j, and properness of p_E.
2. Local-to-global for (R2^orb): whether isotropy-preserving local lifts imply the global equivariant lift (a)–(d). This is open, as stated in round12_q9.
3. The exact published scope of Imayoshi–Shiga for punctured types with g ≥ 1 and n ≥ 1, or g = 0 and n ≥ 5. This is from memory.
4. Proposition C in non-product strata under coarse (R2).
5. Not in scope: MS11♭ under (R2^orb), and the chain step "(Rig) + MS11♭ ⇒ the problem's claim".


## Other inputs (verbatim prior results; bookkeeping lines removed)

### round11_q9 (verbatim)
# round11_q9: check of chain steps 2(b)–2(d) (entries 99, 100), MS11 ⇒ MS8

**Plan/status.** I checked every item of the brief against the spliced proofs:
- round10_q1 §2 and §4;
- round10_q10 §6.3;
- round10_q3 §2;
- round9_q7 Lemmas S, J and Cor. J′;
- round9_q3 Lemma PT, Lemma P, Theorem X′.

**Verdict: correct after named repairs.** With MS11 worded as it is, the chain has a gap at two places: step 2(c), the transfer along a travel interval, and step 2(d), the MOV case of the endpoint. Both come from Lemma B1(a), which is false as stated. The repair is to replace "transport sheet of c̃" by "c̃-sheet" (defined in §2) in MS11 and in the induction claim; the repaired statement is called MS11♭ below. With that change every step 2(b)–(d) goes through. Everything else checks, modulo the inherited cited inputs and one inherited "routine marking detail" (§4).

Readings throughout: (R1), (R2) with H_0 = id, (Rig), and the notation of the task file. [Z] is the class in 𝔐 = M_{g_i,n_i}/S_{n_i}.

---

## 1. Item 1: Lemma S̃′ ⇒ Theorem X*_all ⇒ Cor. IMOV_all (entry 99). Correct.

### 1.1 Lemma S̃′ supplies exactly the hypothesis of Theorem X*_all
Theorem X*_all needs three things:
- a point Q_0 lying in the stratum of a piece E;
- a lift β̃ ⊂ L (the stratum locus) of a branch β of E;
- a sheet S, i.e. an irreducible component of the germ at 0 of q^{-1}(closure V_0), with S ⊃ β̃.

Its conclusion is S ∩ {∏ s_e = 0} = β̃ near 0.

Lemma S̃′ gives a component X̃_l of q^{-1}(closure V_0) ∩ B̃ with X̃_l ⊃ β̃ ∪ β̃′. Because B̃(J,3r) is taken to be a Milnor ball, X̃_l represents a germ component, i.e. a sheet.

I re-checked the proof of S̃′.
- **Step 1.** The ray g_s(X_n,q_n) lies on the Teichmüller disc F of the generating pair. The rotation by e^{-2iθ_n} from Lemma NH does not change the disc. F lies over V_0 by total geodesy, in the form already used in Lemma PA Step 5. (T4) is **not** needed, so S̃′ really replaces Lemma 1SS.
- **Minor repair in Step 1.** R should be the component of F^{-1}(gU ∩ (preimage of B̃(J,3r))) that contains the excursion arc, not the component of F^{-1}(gU). Otherwise f(R) need not lie in B̃, which is where the X̃_l live. The excursion arc lies in B(J,2r), so this changes nothing else.
- **Step 2.** The sets f^{-1}(X̃_l) are analytic subsets of the connected Riemann surface R and cover it, so one of them is R. Correct.
- **Step 3.** z̃^1 lies in X̃_l because X̃_l is closed in B̃. X̃_l ∩ {∏ s_e = 0} is pure 1-dimensional at z̃^1: no local component of X̃_l at z̃^1 can lie in the 1-dimensional set q^{-1}(B_0). Near z̃^1, q^{-1}(B_0) = β̃, because distinct lifted branches meet only at 0. So X̃_l contains a neighbourhood of z̃^1 in β̃, hence all of β̃, since β̃ ∩ B̃ is irreducible in a Milnor ball. Correct.

### 1.2 Cor. IMOV_all(a) at every transition in the stratum of an adjacent piece
- **J in the stratum of D (entering piece).** Apply X*_all to (D, coarse branch of β̃, S = X̃_l). Then β̃′ ⊂ S ∩ {∏ s_e = 0} = β̃ near 0. Both are irreducible representatives in B̃, so β̃′ = β̃.
- **J in the stratum of D′ (leaving piece).** Symmetric: apply X*_all to D′.
- **The label.** The label does not change, independently of S̃′. By (R-b), Σ_x = Σ_i = Σ_{x′}, so x′ = x.
- **Consequences.** The coarse branches coincide, so the transport families Ñ_β̃ and Ñ_β̃′ coincide, and so do their sheets. Persistence passes unchanged.
- **R(D)-points.** These are interior points of D. Entering and leaving lifts are lifts of branches of D; in the Gap A model they lie over E_k and σE_k. The same argument gives β̃′ = β̃. So the walk never switches lifted curve at an R(D)-point, and these transitions are trivial. Correct.
- **Endpoint.** S̃′ also holds with z̃^2 = z̃^∞ ∈ b̃ ∖ 0. If Q_0 were in the stratum of D^k or of E_b, then b̃ = β̃, so x would be intact and ≡ Y_0 along b̃, contradicting MERGE/MOV. So Q_0 satisfies (P). A genuine transition (β̃′ ≠ β̃) also satisfies (P), by contraposition of (a).
- **Small addition.** A puncture transition with β̃′_m = β̃_m needs nothing. MS11 requires β̃ ≠ b̃, so it is invoked only at transitions with β̃′_m ≠ β̃_m. The chain should say this explicitly.

### 1.3 Theorem X*_all where it departs from round9_q4
- **(i) The lift L̂ to ∏_w M_w.**
  - By Wolpert and Abikoff, the node curves of every limit L(w), under the disc's marking, are exactly those of P_1.
  - The vertex subsurfaces are invariant under the twist group Tw, so the labelling does not depend on twisting.
  - The labels are fixed once, by the chart Def(Q_0) at X̃_n near P̃_1. This is consistent in n, because all the lifts X̃_n converge to P̃_1 in one chart.
  - Locally, L̂ = Π_Z ∘ (limit of the chart lifts), so it is holomorphic.
  - The step L̂(𝔻) ⊂ Ê uses that Π(P̃_1) lies on Ê only.
  - Step 3 is correct as written: properness of L̄ is obtained through pr_j ∘ L̄, with no properness of pr_j on Ê needed, and Γ acts on the finite set Λ.
  - Step 4's new point is that the chart limit L̃ lands in the **specific** lift β̃, not only in ⋃_a aβ̃. It is proved correctly: the sets aβ̃ ∖ 0 are pairwise disjoint and closed in B ∖ 0, Ω minus a discrete set is connected, and L̃(0) = P̃_1.
  - Verified, modulo the cited T̄_g ↔ Def chart description.
- **(ii) The homological step.** The corrected sign argument is plausible. If L′ meets C′ only at the isolated point w*, then Z_n · C′ = −μ ≤ 0, while Σ k_j F_j · C′ > 0. But the text of round9_q4 §1.4, with (Int) and (Pos), is not spliced into my brief, so I cannot check it line by line.
- **It is not needed.** The maximum-principle route of round9_q3 (Step 5′ with Lemma P) proves X*_all directly from Steps 1–4. I checked this as follows.
  - Call a component of B̂ at ŝ_0 *of type β̃* if it maps onto β̃. These are the Ê_l. Let C be the union of all the other components; this includes components over aβ̃ ≠ β̃.
  - By Step 4, L̂_S(Ω) ⊂ ν^{-1}(β̃). The germ of ν^{-1}(β̃) at ŝ_0 is ⋃_l Ê_l, because ν is finite and β̃ is irreducible. A component over aβ̃ meets ν^{-1}(β̃) only in ν^{-1}(aβ̃ ∩ β̃) = {ŝ_0}.
  - Lemma P applies to (W, C, Ê_1, …, Ê_r). I re-checked its proof: Lemma M; the Mumford pull-back; the anti-ample cycle Z; D = mπ*C − Z effective with support C̃ ∪ E and D·E_j > 0; (RA); g = σ/s^N. It is correct given (Res), (Neg), (RA).
  - Steps 5′.2–5′.6 then go through verbatim: D̂_n(Δ*) ⊂ W ∖ B̂ ⊂ W ∖ C, the maximum principle bounds |g ∘ D̂_n|, and |g| → ∞ along Ê_l at ŝ_0 gives the contradiction.
  - **So X*_all holds in every stratum, with or without the homological correction.**

---

## 2. Item 2: Lemma B1 is false as stated in (a) and (b), and the repair

### 2.1 Where the proof of B1(a) fails
The proof of B1(a) says: "So Ñ^1 meets {t = 0}, **where Ñ ∩ {t = 0} = b̃ ∖ 0**." Nothing justifies the bold claim.
- Ñ = Ñ_b̃ is the connected component of q^{-1}(N) containing b̃ ∖ 0.
- Its t = 0 slice lies in q^{-1}(b ∖ Q) = ⋃_a (ab̃ ∖ 0).
- Ñ can contain a second lift ab̃ ≠ b̃, joined to b̃ ∖ 0 through points with t ≠ 0.
- Then Ñ_{ab̃} = Ñ_b̃, and Ñ can have an irreducible component whose t = 0 slice lies in ab̃ and misses b̃ ∖ 0.
- The proof of (b) uses (a) ("every global component of Ñ contains such a germ"), so (b) fails too.

### 2.2 Local model 1 (chart-level, consistent with (R2); it refutes B1(a), (b) and the MOV endpoint step under MS11's weak notion)
**Coordinates and branches.**
- Def(Q) has coordinates (s_1, s_2, p, p′, u, …). The labels x and x′ = ax have the same type, with moduli coordinates p and p′; Y_0 ↔ 0, and Y_t ↔ t (to first order).
- a ∈ Aut(Q) acts by p ↔ p′ and u ↦ −u, and fixes s_1, s_2.
- Put b̃ := {s_1 = 0, p = s_2², p′ = 0, u = s_2} and ab̃ = {s_1 = 0, p′ = s_2², p = 0, u = −s_2}.
- These are distinct lifts with the same pattern {e_1}. Q is a puncture: s_2 ≢ 0.
- Along b̃, x is intact and **moving** (MOV), and x′ is constant ≅ Y_0.

**Transport.**
- A := {s_1 = 0, p = t + s_2(s_2+t), p′ = t, u = s_2 + t, s_2 ≠ 0}, and aA := {s_1 = 0, p′ = t + s_2(s_2+t), p = t, u = −(s_2+t), s_2 ≠ 0}.
- A ∩ {t = 0} = b̃ ∖ 0 and aA ∩ {t = 0} = ab̃ ∖ 0.
- For t ≠ 0, A and aA meet at the a-fixed point P_t = (s_2 = −t, p = p′ = t, u = 0), which has s_2 ≠ 0.

**Coarse smoothness.**
- q is injective on A_t, because A_t ∩ aA_t = {P_t} and P_t is a-fixed.
- s_2 is an a-invariant coordinate that restricts to a coordinate on A_t. So N_t := q(A_t) is a smooth coarse curve, a graph over s_2.
- H_t(q(b̃(s_2))) := q(A_t(s_2)) is a smooth trivialisation of N = ⋃_t N_t. The lift of Q_t is s_2 = 0, i.e. p = p′ = t, u = ±t. So |Aut(Q_t)| < |Aut(Q)|, which matches the known necessary conditions.

**Conclusions in the model.**
- Ñ_b̃ = A ∪ aA. It is connected (through P_t) and has two irreducible components, one of which has slice ab̃ ∖ 0. The pointwise stabiliser of b̃ does not contain a. So **(a) and (b) of B1 fail.**
- x is Y-persistent on aA: F_x = p = t ↔ Y_t, and x is intact. So **x is Y-persistent on a transport sheet of b̃ in MS11's sense, while x MOVES along b̃.**
- The model is chart-level only. It satisfies every chart-checkable constraint I know of, the same way the Gap B model of round10_q3 does. The point is that the step "B1(a) ⇒ the endpoint contradiction" is not a valid inference.

### 2.3 The repaired lemma (B1♭), proved
**Definition.** Let c̃ be a lifted branch. A *c̃-sheet* is an irreducible component of closure(Ñ_c̃) in B × Δ_ε whose t = 0 slice contains a non-empty open subset of c̃ ∖ 0.

**Lemma B1♭.** Let Ñ = Ñ_b̃.
- (a′) Every irreducible component Ñ^1 of Ñ maps onto N. Its t = 0 slice is a non-empty union of open subsets of finitely many lifts ab̃ ∖ 0, each with ab̃ ⊂ closure(Ñ) and with aS_b̃ = S_b̃.
- (a″) b̃-sheets exist. For generic p̃ ∈ b̃ ∖ 0 near 0, every germ component of q^{-1}(N) at (p̃, 0) lies in a b̃-sheet, and every b̃-sheet contains such a germ.
- (b′) The pointwise stabiliser Stab(b̃) permutes the b̃-sheets transitively.
- (c), (d) as in round10_q3. In (d), at product-type points every a ∈ Aut(Q) fixes x (Lemma PT). So persistence of x on an ab̃-sheet T is equivalent to persistence of a^{-1}x = x on the b̃-sheet a^{-1}T, and the weak and strong notions agree there.

*Proof.*
- **(a′).** Ñ^1 maps onto N by Remmert: N is a connected topological 4-manifold, hence an irreducible analytic set, and q is finite on Ñ^1. So t is non-constant on Ñ^1, and by Krull its slice is pure 1-dimensional. The slice lies in ⋃_a ab̃ ∖ 0, and these sets are pairwise disjoint and closed in B ∖ 0. The pattern is constant on the connected set Ñ (R7-4 Lemma 2(a)), which gives aS_b̃ = S_b̃.
- **(a″).** Near (q(p̃), 0) the set N is the whole of ℬ. Near p̃, q^{-1}(b) = b̃. So every germ component of q^{-1}(N) at (p̃, 0) has its t = 0 slice in b̃, lies in Ñ (q^{-1}(N) is locally connected at (p̃,0) ∈ Ñ), and lies in one global component, which is then a b̃-sheet. Conversely, a b̃-sheet contains a generic point (p̃, 0) of its slice in b̃ ∖ 0, and with it a germ component there.
- **(b′).** This is the original proof of (b), restricted to b̃-sheets, which is where it is valid. For generic p̃, Stab(p̃) equals the pointwise stabiliser of b̃ and permutes the germ components at (p̃, 0) transitively. Each element of it maps Ñ to itself. ∎

### 2.4 Gap A repair (R(D) added to Σ): correct
- R(D) is finite. It consists of the singular points of ξ̄^{-1}(closure D), which include the crossings E_k ∩ σE_k, together with the images of ramification points of the normalisation maps.
- With R(D) ⊂ Σ chosen before r, ξ^{-1}(K_D) is a disjoint union of compact pieces at positive mutual distance, each mapped by a covering onto K_D. So the marking lift stays on one lifted curve E with a fixed factor c.
- The new transitions are trivial by §1.2.
- The step "marking lift continuous along travel, label = c" is a routine marking detail of the K_w kind. I accept it as inherited; I did not re-derive it.

### 2.5 Base step: correct, and gives the strong notion
- Δ_Γ is of product type, so Aut(Γ) acts trivially on ∏ M_w (Lemma PT, steps 1–2) and Π_S is canonical.
- At every (p,t) ∈ Ñ_{β̃_1}, q(p) ∈ H_t(β_1 ∖ J_1) ⊂ ∂V_t (R2), and the pattern is constant. So x_1 = {i} is intact and F_{x_1}(p) = pr_i Π_S(p) = Y_t.
- Closedness passes this to closure(Ñ). So x_1 is persistent on **every** sheet, in particular on β̃_1-sheets. (B1(d) is not even needed.)

### 2.6 Product-type puncture junction (Lemma J / Cor. J′): correct; weak input suffices, strong output
**Input.**
- Let T be any sheet of Ñ_{β̃_m} on which x is persistent; it may be an aβ̃-sheet.
- T ⊂ q^{-1}(closure H((β∖J)×Δ_ε)), and by Lemma T(c) this lies in q^{-1}(ℬ^{(k(β))}) near (0,0). Also (0,0) ∈ T, since lifts of J_t accumulate there.
- So any germ component of T at (0,0) is a germ component 𝒲̃^a of q^{-1}(ℬ^{(k(β))}) with persistent vertex x.
- Lemma J never uses β̃ ⊂ 𝒲̃^a. Its step 1 uses only that Aut(Q) permutes the preimage germ components transitively, and step 2 uses only persistence on 𝒲̃^a.

**Conclusion.**
- By Lemma PT, x̂ = x.
- x = x_m is intact and constant ≅ Y_0 along b̃ = β̃′_m: this is the track's c′ = {x_m}. So (J1) and (J3) are excluded (Cor. J′), and (J2) holds: x is persistent on a germ component 𝒲̃″ ⊃ b̃ at (0,0).

**Strong output.**
- Take p̃ ∈ b̃ ∖ 0 generic and close enough to 0 that a representative of 𝒲̃″ is defined near (p̃, 0).
- Near (q(p̃), 0), ℬ = N, so the germ of 𝒲̃″ at (p̃,0) is a union of germ components of q^{-1}(N) at (p̃,0). By B1♭(a″) these lie in b̃-sheets.
- The persistence set is analytic: intactness is the pattern, and {[F_x] = [Y_t]} is analytic because [Y] is holomorphic. Persistence holds on an open subset of the irreducible component, hence on all of it (identity principle), and on its closure by continuity.
- So x is persistent on a **β̃′_m-sheet**.

I also checked Lemma J step 5 (Lemma S(b), continuity of F_x on L_x at q_t) and step 7. Both use (Rig) through Lemma S(a), and (Rig) is part of MS8's setting.

### 2.7 Transfer along a travel interval: correct for c̃-sheets, unsupported for MS11's notion
**Proof with the strong notion.**
- Let Ñ′^1 be a component whose closure is a β̃′_m-sheet with x_m ↔ c persistent.
- Π_S(Ñ′^1) is irreducible and 2-dimensional, inside (ξ×id)^{-1}(κ(D)), so it lies in one global component 𝒲̃.
- By B1♭(a′), and **because the sheet is a β̃′_m-sheet**, 𝒲̃_0 contains an open arc of Π_S(β̃′_m), which lies on the track's E. Hence 𝒲̃_0 ⊃ E.
- At J_{m+1}, take p̃ ∈ β̃_{m+1} ∖ 0 generic, with z = Π(p̃) ∈ E under the track's identification. Near p̃, Π is a finite open map from the stratum locus of Def(C_p̃), and q^{-1}(ℬ_G) ∩ L = (Π×id)^{-1}((ξ×id)^{-1}ℬ_G). Near (q(p̃),0), ℬ_G = κ(D), a 4-manifold.
- So the germ components of q^{-1}(N″) at (p̃,0) map onto the germ components at (z,0), and (z,0) ∈ 𝒲̃. Some germ component maps into 𝒲̃. By B1♭(a″) it lies in a β̃_{m+1}-sheet Ñ″^1, and by the identity principle Π(Ñ″^1) ⊂ 𝒲̃.
- c is constant (c ∉ M), so Lemma S(c) applies: persistence of c holds on all of 𝒲̃. Hence x_{m+1} ↔ c is persistent on Ñ″^1, intact by the constant pattern, and persistent on its closure.
- The output is again a **β̃_{m+1}-sheet**.

**Why the weak notion fails.** If the persistent sheet T at J_m is only an aβ̃′_m-sheet with ax_m ≠ x_m, then 𝒲̃ ⊃ Π(T) has its slice on āE, not on E. Equivalently, the persistent label on β̃′_m-sheets is a^{-1}x_m, by (K3), and the transfer carries the factor of the twin a^{-1}x_m. At J_{m+1} the track label is x_{m+1} ↔ c, so MS11's hypothesis there is not supplied.

So step 2(c) is **not** established from MS11 as worded. It is established from MS11♭.

### 2.8 Endpoint 2(d)
- **Product type: correct** with the weak input. Lemma PT makes Q_0 aligned, and Lemma J (J1) applies.
  - MERGE: [x] ≠ {x}.
  - Puncture-MOV: {x} ∈ M(κ(E_b)), using U_b ≠ ∅, (P) and step 7.
  - In both cases Y_t ∈ F on an open set, and (P) with PR-A gives that Y is constant: a contradiction.
- **Non-product, MERGE: correct even with MS11 as worded.** Let T be any sheet of Ñ_b̃ on which x is persistent. Then x is intact on T. The pattern is constant (= S_b̃) on the connected set Ñ_b̃, and T ∩ Ñ_b̃ ≠ ∅. So every edge at x lies in S_b̃, which contradicts MERGE.
- **Non-product, MOV: gap with MS11 as worded.** Local model 1 (§2.2) satisfies "x persistent on a transport sheet of b̃" through the ab̃-sheet aA, while x moves along b̃.
  - The chain's sentence "by Lemma B1(a), T ∩ {t = 0} is a non-empty open subset of b̃ ∖ 0" is false for such T. One only gets F_{a^{-1}x} ≡ Y_0 along b̃, which is the endpoint twin and no contradiction.
  - With MS11♭ the step is correct. T is a b̃-sheet, so its slice contains an open subset of b̃ ∖ 0 on which x is intact and F_x ≅ Y_0. The pattern is constant on b̃ ∖ 0, and F_x is holomorphic on L_x ⊃ b̃. The identity theorem in 𝔐 along the normalisation of b̃ gives [F_x] ≡ [Y_0] along b̃.
  - This contradicts MOV. Here MOV means d(F_x(z̃^∞), Y_0) = η with 0 < 2η < min d(σY_0, Y_0) by (b1), so [F_x(z̃^∞)] ≠ [Y_0].

---

## 3. Item 3: interaction with the repairs (R-a)–(R-d): nothing needs a common sequence
- Each use of S̃′ in 2(a)/(b) concerns one transition.
  - Its witnessing sequence comes from the n′ of that transition's recurrent type τ.
  - The data are normalised by a global a ∈ Aut(J). Since a permutes components, a^{-1}X̃_l contains walk n's own pair (β̃, β̃′).
- Theorem X*_all is a pure t = 0 statement and involves no walks.
- The induction 2(c) uses:
  - the per-transition sheet data;
  - the labels along travel intervals of the **single fixed walk n ≥ N**: canonical lifts for that n, Σ_i = Σ_{x_m}, and the marking lift on E;
  - global analytic objects (𝒲̃, κ(D)).
  None of these refers to other walks.
- The endpoint uses the n′ of type τ_end only to obtain b̃ and the MERGE/MOV dichotomy.
- Shrinking ε finitely many times is harmless. A c̃-sheet for the old ε contains the germ at a generic (p̃,0), hence a c̃-sheet for the new ε, and persistence passes by the identity principle.

So no common subsequence is needed. This confirms round10_q10's remark.

---

## 4. Item 4: other points in 2(a)–(d)
- **Puncture transitions with β̃′_m = β̃_m** are trivial and must be excluded from the MS11 invocations, since MS11 requires distinct branches. This is a wording point only.
- **Inherited, not re-derived:**
  - the marking-continuity detail along travel intervals (round10_q3 §2.1, "routine");
  - the cited inputs: Lemma PA, Lemma NH, (Fl), (Prop), Kerckhoff, Maskit, the T̄_g/Def chart description, Wolpert/Abikoff, (Res)/(Neg)/(RA), Krull, Remmert, Milnor conic structure.
- **(T4)** is not needed by the chain: S̃′ replaces Lemma 1SS.
- **The step "Goal ⇐ MS8 + (Rig) + entry 19"** is unaffected.

---

## 5. Corrected missing statement and corrected chain
**MS11♭ (replaces MS11; same setting and data, including "Y non-constant", (P) and (S)).**
- *Hypothesis:* x is Y-persistent on some **β̃-sheet**, i.e. a component of closure(Ñ_β̃) whose t = 0 slice contains a non-empty open subset of β̃ ∖ 0.
- *Conclusion:* x is Y-persistent on some **b̃-sheet**.

**Chain with MS11♭.** Induction claim: x_m is Y-persistent on some β̃_m-sheet.
- Base: §2.5.
- Interior transitions and R(D)-points: §1.2.
- Product-type puncture junctions: §2.6, which outputs a β̃′_m-sheet.
- Non-product puncture junctions with β̃′_m ≠ β̃_m: MS11♭ (§5).
- Transfer: §2.7.
- Endpoint: §2.8.

So **MS11♭ + entries 19, 24, 84–87, 97–100 (with B1 replaced by B1♭) ⇒ MS8**, and MS8 + (Rig) ⇒ the goal.

**Relation between MS11 and MS11♭.** Neither formally implies the other: MS11♭ has a stronger hypothesis and a stronger conclusion. MS11 alone does not suffice, by §§2.7–2.8 and model 1. MS11♭ is still vacuous whenever the problem's claim holds. Its failure configurations are the same twin configurations as before: an a ∈ Aut(Q) moving x, together with a stabiliser jump of the transported branch at t ≠ 0, as in model 1.

---

## 6. Summary
**Proved / checked:**
- Lemma S̃′ (with the minor repair to R) gives exactly the sheet hypothesis of Theorem X*_all, without (T4).
- Theorem X*_all holds in every stratum. Its new lifting step is checked. The homological correction is plausible but not checkable from the brief, and it is superseded by the Lemma P / maximum-principle route, which I verified for type-β̃ components.
- Cor. IMOV_all(a)–(c) is correct, including at R(D)-points and at the endpoint. So (P) holds wherever MS11 is invoked.
- The Gap A repair, the base step, the product-type junction step (Lemma J / Cor. J′, with weak input and strong output), the product-type endpoint and the non-product MERGE endpoint are correct.
- No common witnessing sequence is needed.

**Found false:**
- Lemma B1(a) and (b) of round10_q3, as stated. Explicit chart-level model in §2.2.
- Corrected version: B1♭ (§2.3), proved.

**Gap at named steps (with MS11 as worded):**
- 2(c), the transfer along a travel interval;
- 2(d), the non-product MOV endpoint.

Both are closed by replacing "transport sheet" by "c̃-sheet", i.e. MS11 by MS11♭.

**Verdict:** the chain proves MS8 from MS11♭ (with entries 19, 24, 84–87, 97–100, B1 replaced by B1♭), modulo the inherited cited inputs and marking details. It does **not** prove MS8 from MS11 exactly as stated.

**Open:**
- MS11♭ itself;
- entry 82 (Rig);
- the inherited inputs listed in §4.

**Status: proved (the corrected derivation MS11♭ ⇒ MS8); not proved (MS11 ⇒ MS8 as worded); open (MS11♭, (Rig)).**



### round11_q1 (verbatim)
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



### round11_q4 (verbatim)
# round11_q4 — attempt to REFUTE MS11

**Status line.** No counterexample and no contradiction were found: MS11 is **not refuted**. Its status stays **open**. Along the way I prove four things.
- (§1) Logical status. Refuting MS11, by either route, is the same as finding a counterexample to the problem under (Rig). The "derivation" route cannot succeed unless the problem itself is false or some PROVED entry is wrong.
- (§2) An exact reformulation of MS11 in terms of **lift-curve components**: the Y-persistent labels of a transport sheet are exactly the "Y-labels" Y(L) of any lift-curve component L contained in the sheet. This gives a clean proved sufficient condition (1L) and an exact description of what a failure needs.
- (§3) A **twin-free closure theorem**. If Y is non-constant, every piece reachable from ∂V_0 by puncture transitions has a constant vertex φ ≡ Y. There is also a **twin-free t=0 criterion (TFM)** that forces Y to be constant. Both are proved modulo R8-2 Theorem 1 (which uses (Rig)).
- (§4) As a sketch: covering constructions from M_{0,5} satisfy TFM, so they cannot be counterexamples. The flex and gothic loci are not candidates as stated, since they live in M_{1,3}.

The chain question (component-wise wording) is answered in §5. Open questions are listed in §6.

Throughout I use the run's readings (R1), (R2), H_0 = id, (Rig), and its notation (B_t, pieces, Def(Q), q, labels, F_x, transport family Ñ, transport sheet, lift-curve). Results used from earlier rounds are cited by their run labels and were re-read from the brief; they are not re-proved here. Standard analytic-geometry facts are cited from memory: Remmert's finite mapping theorem; the open mapping property of a non-constant holomorphic function on an irreducible germ; the fact that an analytic germ whose complement of a real-codimension-2 set is a connected manifold is irreducible.

**Convention (germs).** As in MS11's choice of B, transport sheets and 3-fold components are taken as irreducible components of germs at (0,0) ∈ Def(Q) × Δ. MS11 already shrinks B so that components of q^{-1}(closure V_0) ∩ B are germ components; I assume the same for closure(Ñ_c̃) and q^{-1}(closure 𝒱). If a sheet as defined in the brief (a component of the closure in B × Δ_ε) does not pass through (0,0), it is irrelevant for MS11 after shrinking B and ε. Write G := Aut(Q), acting on Def(Q) × Δ trivially in t.

## 1. Logical status of a refutation

MS11's setting contains the hypothesis "t ↦ Y_t is non-constant".
- If the problem's conclusion holds for every admissible family satisfying (Rig), then MS11's setting is empty and MS11 is vacuously true. Nothing false can then be derived from MS11 together with true statements.
- Hence route 2 of the task ("derive a known-false statement from MS11 + proved results") can succeed only if (a) the problem is false under (Rig), or (b) one of the PROVED entries used is wrong.
- Route 1 (an explicit configuration) is, by round10_q4 Prop. 1, a counterexample to the problem under (Rig).

So both routes require a counterexample to the problem itself, or an error in the ledger. This explains why local chart models (round10_q3 §3.3, round10_q7 §3, R7-3 §5, round9_q9) never refute MS11: refutation is a global question. The useful outputs of a "refutation attempt" are therefore sharpened **necessary conditions for a counterexample** (§§2–4).

## 2. Lift-curve reformulation of MS11 (proved, modulo R8-2 Theorem 1)

**Notation.**
- Q_t := H_t(Q). It is holomorphic in t (PR-B / R7-3 Lemma 1) and lies in Δ_{G_Q}, since H preserves strata.
- The *lift locus* is Λ := {(p,t) ∈ B × Δ_ε : q(p) = Q_t}. Its irreducible components through (0,0) are the lift-curve components. G permutes them transitively: Λ is the preimage of the irreducible curve germ {(Q_t,t)} under the quotient map q × id, and components of the preimage of an irreducible germ under a finite group quotient form one orbit.
- Fix one lift-curve component L_0 and put H_L := Stab_G(L_0). The lift-curve components are gL_0, g ∈ G/H_L.
- Every point of Λ lies in {s_e = 0 ∀ e}, so every label is intact there.
- For a lift-curve component L, let **Y(L)** be the set of labels y with F_y(p) ≅ Y_t at all (p,t) ∈ L. This is an analytic condition, equivalent to holding at generic points of L.
- By (K3) of R7-3, Y(gL) = g·Y(L). In particular Y(L) is H_L-invariant.
- For a lifted branch c̃ through 0 (Q a puncture of the piece of c), let **𝓛(c̃)** be the set of lift-curve components contained in some transport sheet of c̃.

**Lemma 2.1 (every sheet contains a lift-curve component).** Let c̃ be a lifted branch of a branch c of B_0 at Q, and T a transport sheet of c̃ (a germ at (0,0)). Then T contains some lift-curve component.

*Proof.*
- Let Σ_c be the germ at (Q,0) of closure(H(c × Δ_ε)) ⊂ M̄_g × Δ. By (R1) and (R2) it is a 2-dimensional analytic germ: it is the germ of a component of closure(𝒱) ∩ (closure(Δ_{G_c}) × Δ).
- Σ_c contains the dense subset H((c∖Q) × Δ_ε), which is a connected topological 4-manifold. The rest, {(Q_t,t)}, has real codimension 2. Hence Σ_c is an irreducible germ.
- T ⊂ (q × id)^{-1}(Σ_c), and q × id is finite. By Remmert's finite mapping theorem, (q × id)(T) is a 2-dimensional analytic subgerm of the irreducible 2-dimensional germ Σ_c, so it equals Σ_c.
- In particular, for every small t there is (p,t) ∈ T with q(p) = Q_t. So T ∩ Λ is an analytic subset of T whose projection to t contains a neighbourhood of 0. Hence T ∩ Λ contains a curve through (0,0) not contained in {t = 0}, i.e. a lift-curve component. ∎

**Lemma 2.2 (persistent labels of a sheet).** In the situation of Lemma 2.1, assume (P): Q is a puncture of the piece of c. Let T be a transport sheet of c̃, L ⊂ T a lift-curve component, and y a label. Then
 y is Y-persistent on T ⟺ y ∈ Y(L).
In particular, Y(L) is the same for all lift-curve components L ⊂ T.

*Proof.*
- (⇒) Evaluate the persistence condition at the points of L ⊂ T.
- (⇐) Let A_y := {(p,t) ∈ T : s_e(p) = 0 for all e at y, and class F_y(p) = class Y_t in 𝔐}. This is a closed analytic subset of T (F_y is holomorphic on L_y, and Y is holomorphic by PR-A).
- Let t be generic in the sense of R8-2 §3, i.e. t ∉ Z, where Z is discrete. Let (p,t) ∈ L. Then Q_t is a puncture of the transported piece (H preserves strata and pieces), and y is a Y_t-copy at p.
- Every branch of the curve T_t = T ∩ {t} at p is a lifted branch of the transported branch c_t at Q_t, because T_t ⊂ q^{-1}(closure c_t). By R8-2 Theorem 1 (IMOV is excluded at a puncture), y is STAY along each such branch: it is intact, and F_y is constant, equal to F_y(p) ≅ Y_t.
- So A_y contains the germ of T_t at (p,t). This germ is 1-dimensional, because T is an irreducible 2-dimensional germ and t ≢ 0 on T.
- This holds for all t ∉ Z near 0, an uncountable set. An analytic set of dimension ≤ 1 has 1-dimensional fibres over at most countably many t. Hence dim A_y = 2, and A_y = T since T is irreducible. ∎

**Proposition 2.3 (exact reformulation).** Under the hypotheses of MS11 the following hold.
- The labels Y-persistent on some transport sheet of c̃ are exactly ⋃_{L ∈ 𝓛(c̃)} Y(L).
- MS11 for (Q, β̃, b̃, x) is equivalent to: if x ∈ Y(L) for some L ∈ 𝓛(β̃), then x ∈ Y(L′) for some L′ ∈ 𝓛(b̃).

*Proof.* Combine Lemmas 2.1 and 2.2. ∎

**Corollary 2.4 (sufficient condition (1L), proved).** Suppose some irreducible 3-dimensional component X of the germ of q^{-1}(closure 𝒱) at (0,0) satisfies:
- X contains a transport sheet of β̃ on which x is persistent, and some transport sheet of b̃;
- X contains exactly one lift-curve component.

Then MS11 holds for (Q, β̃, b̃, x).

*Proof.* Both sheets lie in X, so by Lemma 2.1 both contain the unique lift-curve component L ⊂ X. By Lemma 2.2, x ∈ Y(L) is persistent on the b̃-sheet. ∎

**Corollary 2.5 (anatomy of a failure, proved).** Suppose MS11 fails for (Q, β̃, b̃, x), and let L ∈ 𝓛(β̃) with x ∈ Y(L). Then:
1. L ∉ 𝓛(b̃): no sheet of b̃ contains L. In particular |G·L| ≥ 2, i.e. H_L ≠ G. This recovers the necessary condition |Aut(Q_t)| < |Aut(Q)|.
2. 𝓛(b̃) ≠ ∅ (Lemma 2.1), and every element of 𝓛(b̃) is gL with x ∉ g·Y(L). The persistent labels gx on b̃-sheets are twins of x, Y_0-copies different from x. The required α moving x is any such g.
3. By Lemma B1(a), at t = 0 the labels in g·Y(L) are intact and ≡ Y_0 along b̃. So the piece E_b of b has a constant vertex with φ ≡ Y that is **not** x along b̃ (a "staying twin").
4. The persistent sheet of β̃ and every sheet of b̃ contain disjoint sets of lift-curve components. So any 3-fold component X containing sheets of both contains at least two lift-curve components L, gL. Hence (1L) fails, by one of two mechanisms:
   - **(F-a)** S × {0} lies in two different 3-fold components X ≠ X′. This needs S to lie in the fixed locus of some σ ∈ G that is not in the generic stabiliser of the time-t surfaces (the planner's (β)-edges).
   - **(F-b)** a single X contains several lift-curve components.

**Relation to the planner's Mechanism D.** In this language the label-change rule of the planner's sketch (§4 of the brief) is automatic.
- Two sheets that share a lift-curve component have the same persistent labels (Lemma 2.2). This is the (α)-edge statement, without Lemmas I1/I2.
- Labels change only between sheets that contain different lift-curve components L ≠ gL, and the change is y ↦ gy.
- Grothendieck connectedness of X ∩ {N = 0} ∖ {(0,0)} therefore yields MS11 only if one can show that the lift-curve components met along a connecting path are related by elements g with x ∈ g·Y(L). Connectedness alone does not give this, and I found no global input that does. This is where the Mechanism-D attempt stops.

## 3. Twin-free closure of the Y-network, and a twin-free t = 0 criterion (proved, modulo R8-2 Theorem 1)

The twin problem comes from following the *marked* copy x. Membership statements that do not track a particular label can be transported with no twin problem at all. This section makes that precise. It yields necessary conditions for a counterexample that involve V_0 only.

**Definitions.**
- For a piece E at t = 0 and a vertex c constant on E, φ_c(t) is the value of c on E_t = H_t(E). It is holomorphic by R7-3 Lemma 1(a).
- 𝒩 is the set of pieces E (at t = 0) having a constant vertex c with φ_c ≡ Y.
- 𝒩_0 ⊃ 𝒩 is the set of pieces having a constant vertex with value ≅ Y_0.
- A *puncture* of E is a point of closure(ξ(E)) outside the stratum Δ_{G_E}. Pieces are closed in their stratum, so this is the same as a point of closure(ξ(E)) ∖ ξ(E).
- **ℛ** is the smallest set of pieces with these two properties:
  - it contains every piece of ∂V_0;
  - **(PT)** if E ∈ ℛ, Q ∈ closure(ξ(E)), and E′ is a piece of which Q is a puncture, then E′ ∈ ℛ.

**Proposition 3.1 (ℛ ⊂ 𝒩).** Assume (R1), (R2), (Rig), and that Y is non-constant. Then every piece in ℛ has a constant vertex c with φ_c ≡ Y. In particular ℛ ⊂ 𝒩_0.

*Proof.* Pieces of ∂V_0 lie in 𝒩, via the vertex i. It remains to show that 𝒩 is closed under (PT). Let E ∈ 𝒩 with constant vertex c, φ_c ≡ Y. Let Q ∈ closure(ξ(E)), and let E′ be a piece with Q as a puncture.
- Let t ∉ Z be generic (R8-2 §3) and let q be any lift of Q_t = H_t(Q).
- Take a lifted branch of E_t through q, or the lifted germ of E_t if Q_t ∈ ξ(E_t). Along it, the constant vertex c is a single label z, intact at q, with F_z(q) = φ_c(t) = Y_t: a constant vertex has a smooth limit (R7-3 §1).
- E′_t has Q_t as a puncture, since H preserves strata and closures (PR-B). E′_t has a lifted branch through q, because q is an open map.
- By R8-2 Theorem 1, IMOV is impossible since Q_t is a puncture of E′_t. So z is STAY: z is a constant vertex of E′_t with value Y_t, and (W, z) is a Y-vertex.
- E′_t has finitely many vertices, identified with those of E′ by transport. So some vertex c′ of E′ is constant with φ_{c′}(t) = Y_t for uncountably many t. By the identity theorem φ_{c′} ≡ Y, i.e. E′ ∈ 𝒩. ∎

Note that no label is tracked across Q here: q is an arbitrary lift, and the conclusion is about *some* vertex of E′. This is why twins play no role.

**Corollary 3.2 (criterion R).** Under (R1), (R2), (Rig): if some piece reachable from ∂V_0 by puncture transitions has no constant vertex isomorphic to Y_0, then Y_t = Y_0 for all t.

*Proof.* Proposition 3.1 shows that Y is constant, and Y_t = Y_0 by PR-A. ∎

**Theorem 3.3 (twin-free merge criterion, TFM).** Assume (R1), (R2), (Rig). Suppose there are a point Q ∈ B_0, a piece E′ ∈ ℛ with Q ∈ closure(ξ(E′)), and a piece E″ of which Q is a puncture, such that the following condition holds.
- **(TF)** For every lifted branch (or lifted germ) ẽ′ of E′ at 0 ∈ Def(Q), every label z that is intact and ≡ Y_0 along ẽ′, and every lifted branch ẽ″ of E″ at 0, the label z is *not* intact-and-≡ Y_0 along ẽ″.

Then Y_t = Y_0 for all t.

(TF) holds vacuously if E′ has no constant vertex ≅ Y_0. It concerns V_0 and t = 0 only.

*Proof.* Suppose Y is non-constant. By Proposition 3.1, E′ has a constant vertex c with φ_c ≡ Y.
1. Let 𝔗′ (respectively 𝔗″) be the germ at (0,0) of the closure of q^{-1}(H(β′ × Δ_ε)), where β′ ranges over the branches of E′ at Q (respectively of E″). Each is a finite union of irreducible 2-dimensional germs ("sheets"), by the argument of Lemma 2.1.
2. For each generic t near 0, pick a lift q_t of Q_t.
   - As in the proof of 3.1, there is a branch of 𝔗′_t through (q_t,t) along which some label z_t is intact with F ≡ Y_t (the label of c).
   - There is also a branch of 𝔗″_t through (q_t,t) along which z_t is STAY (R8-2 Theorem 1).
3. There are finitely many sheets, labels and lift-curve components, and uncountably many t. So we may fix a sheet T′ ⊂ 𝔗′, a sheet T″ ⊂ 𝔗″, a label z and a lift-curve component L, such that for uncountably many t the point (q_t,t) lies on L, with both branches in T′ and T″ respectively and z_t = z. Then L ⊂ T′ ∩ T″, since an irreducible curve meeting an analytic set in uncountably many points lies in it.
4. The argument of Lemma 2.2 (the analytic set A_z is 2-dimensional) applies on T′ and on T″. So z is intact with F_z ≅ Y_t on all of T′ and on all of T″.
5. T′ ∩ {t = 0} and T″ ∩ {t = 0} are 1-dimensional, since t ≢ 0 on these irreducible 2-dimensional germs. By H_0 = id they lie in the union of the lifted branches of E′, respectively of E″, at 0. So some lifted branch ẽ′ ⊂ T′_0 and some ẽ″ ⊂ T″_0 carry z intact and ≡ Y_0.
6. This contradicts (TF). Hence Y is constant, and Y_t = Y_0 by PR-A. ∎

**Corollary 3.4 (necessary conditions for a counterexample to the problem, under (Rig)).** If Y is non-constant, then V_0 satisfies both of the following.
- **(NC1)** Every piece reachable from ∂V_0 by puncture transitions carries a constant component ≅ Y_0.
- **(NC2)** For every Q ∈ closure(⋃_{E∈ℛ} ξ(E)), every E′ ∈ ℛ with Q ∈ closure(ξ(E′)), and every piece E″ of which Q is a puncture, there are lifts ẽ′ of E′ and ẽ″ of E″ at 0 ∈ Def(Q), and a label z, intact and ≡ Y_0 along both. That is, every Y_0-copy can be "continued" from E′ to E″ by some twin.

These are V_0-only conditions; no deformation appears in them. Any explicit counterexample to MS11 (hence to the problem) must satisfy them at every point of the reachable network, not just at one non-product point Q. In particular, at the chain endpoint where MS11 would fail, Corollary 2.5(3) and (NC2) agree: E_b carries a staying twin.

## 4. Candidate surfaces

### 4.1 Covering constructions from M_{0,5} (sketch: they satisfy TFM, so they are not counterexamples)
**Setting and assumptions (A).**
- V_0 is the image in M_g of the covering construction attached to a branched cover C → P^1 whose branch locus is the five marked points, each genuinely branched.
- closure(V_0) is described by admissible covers over M̄_{0,5}, followed by stabilisation. This is standard, cited from memory.
- Assume moreover that over the boundary points of M̄_{0,5} used below, every component of the admissible covering curve is already stable, so stabilisation contracts nothing.
- Let Δ_Γ be the stratum of the image of D_{12}°: the points 1, 2 collide, the base is R_{12} ∪_{n} R_{345}, and the pieces of ∂V_0 come from D_{12}. Y_0 is a component over R_{12}, with its node points as special points.
- Smoothness of V_0 is not used. (Covering constructions are often not smooth, e.g. the quintic example of PR-I.)

**Argument.**
- Let Q be the image of D_{12} ∩ D_{34}. The base is R_{12} —n1— R_5 —n2— R_{34}.
- Q is a puncture of the ∂V_0 piece E″ (the D_{12} piece) and of the piece E′ of D_{34}. Hence E′ ∈ ℛ by (PT).
- The constant vertices of E′ are the components over R_{34}: they cover a fixed 3-pointed sphere. The components over the moving 4-pointed component R_{125} are the non-constant ones (generically).
- Every component z over R_{34} maps onto R_{34}, so it carries a preimage of n2, and that is a node of the covering curve (by (A) this node survives stabilisation).
- Moving from Q into D_{12} smooths n2, hence smooths every node over n2. So such a z is merged along **every** lift of the E″ branch.
- Thus (TF) holds: vacuously if no component over R_{34} is ≅ Y_0, and because every such twin merges otherwise.
- By Theorem 3.3, Y_t = Y_0 under (Rig).

This recovers PR-I Proposition 3 (the quintic case, where the twin C over R_{34} sits inside the moving vertex along ∂V_0) without using (O) or Krull at time t, and extends it to all covering constructions from M_{0,5} satisfying (A).

The sketch status is due to (A) and to the admissible-cover description, which are cited, not proved. Without (A), a rational bridge over R_5 could be contracted. A component over R_{34} might then stay intact and constant along D_{12}, giving a staying twin, and (TF) can fail. I did not analyse that case.

### 4.2 Other candidates
- **Loci in the hyperelliptic locus of genus 3** (round10_q4 §4(c)). The totally geodesic surfaces I know there are covering constructions from M_{0,5} (cited from memory, not checked). For them §4.1 applies when (A) holds. I could not determine whether smooth examples violating (A) exist.
- **Flex and gothic loci** (cited from memory: Mirzakhani–McMullen–Mukamel–Wright / Eskin–McMullen–Mukamel–Wright). These are primitive totally geodesic surfaces in **M_{1,3}**, not in M_g. They are not admissible V_0 for the problem as stated, which concerns closed subvarieties of M_g, so they are not candidates here. I do not know a primitive totally geodesic surface in an unmarked M_g to test.
- **Explicit configuration for MS11.** By Corollaries 2.5 and 3.4, a counterexample needs all of the following:
  - a V_0 satisfying (NC1) and (NC2) at every point of the reachable network (staying twins everywhere);
  - a non-product point Q with |G·L| ≥ 2;
  - a failure of (1L) via (F-a) or (F-b).

  I found no surface with even (NC1) together with a non-product twin point, other than symmetric covering constructions. Those violate (NC2) by §4.1 (under (A)). **Attempt stopped here: no counterexample.**

## 5. Is the component-wise wording enough for the chain (steps 2(c), 2(d))?

Yes, as far as I can check, provided Lemma B1(a) and entry 100's transfer hold as stated.
- **Endpoint 2(d).** The chain needs one sheet T of b̃ on which x is persistent. Lemma B1(a) gives a non-empty open subset of b̃ ∖ 0 at t = 0 on which x is intact and ≡ Y_0. The identity theorem along b̃ then contradicts MERGE or MOV. "Some sheet" is exactly what is needed.
  - Lemma 2.2 gives an independent route to the open set: T ∩ {t = 0} is 1-dimensional and contained in the lifted branches of b, and A_x = T.
  - One point should be checked in B1(a): that T ∩ {t = 0} lies in b̃ itself and not in another lift σb̃. If it lay in σb̃, one would get x intact along σb̃, i.e. σ^{-1}x along b̃. That is a twin, not x, and the contradiction would be lost.
- **Transfer 2(c).** Persistence of x on a sheet of β̃′_m is an analytic identity (A_x = sheet) on an irreducible set. It therefore continues along the irreducible travel family of D^{m+1} (entry 100; R7-3 Lemma 2, steps 3–4, where pattern and label data are constant on irreducible families) to every sheet of β̃_{m+1} contained in that travel family. "Some sheet" again suffices.
  - The point to watch is the same: the label carried along must be the t = 0 continuation of x_m, not an Aut(G)-relabelling. For non-product strata of D^{m+1}, the sheet's slice may lie over ρE_t rather than E_t inside the same lifted family W (R8-2 Lemma U). I did not re-verify the R(D) repair that is said to fix the label; I flag it.
- **Simplification.** By Lemma 2.2, the induction claim can be stated as "x_m ∈ Y(L) for some L ∈ 𝓛(β̃_m)", and MS11 as Proposition 2.3. By Proposition 3.1, the piece-level statement (every chain piece lies in 𝒩) is already proved without MS11. Only the label-level statement needs MS11.

## 6. Summary: proved / sketched / open

**Proved** (modulo the cited R8-2 Theorem 1, PR-A, PR-B, R7-3 Lemmas 1–2, Lemma B1(a), and standard analytic facts):
- §1: refuting MS11, by either route, amounts to a counterexample to the problem under (Rig), or an error in a PROVED entry.
- Lemma 2.1: every transport sheet contains a lift-curve component.
- Lemma 2.2: the persistent labels of a sheet are exactly Y(L) for any lift-curve component L in it.
- Proposition 2.3: the exact reformulation of MS11.
- Corollary 2.4: the sufficient condition (1L).
- Corollary 2.5: the anatomy of a failure, with mechanisms (F-a) and (F-b).
- Proposition 3.1: ℛ ⊂ 𝒩, twin-free.
- Corollary 3.2: criterion R.
- Theorem 3.3: the twin-free t = 0 criterion TFM.
- Corollary 3.4: the necessary conditions (NC1), (NC2) for a counterexample.

**Sketched:**
- §4.1: covering constructions from M_{0,5} under (A) satisfy TFM, hence the conclusion under (Rig).
- §5: the component-wise wording suffices for the chain, with two flagged checks (B1(a) lands in b̃ itself; label consistency in the transfer for non-product pieces).

**Not proved / open:**
- **MS11 itself: open, neither proved nor refuted.** Precisely where each attempt stopped:
  - Mechanism D: connectedness does not control which lift-curve components are met (§2, end).
  - (1L): no general reason why a 3-fold component should contain only one lift-curve component; both (F-a) and (F-b) are unexcluded.
  - Counterexample search: no V_0 known satisfying (NC1) and (NC2) with a non-product twin point.
- **New open targets, V_0-only (t = 0), twin-free, and each sufficient for the problem under (Rig):**
  - (MS-R): ℛ ⊄ 𝒩_0;
  - more generally (MS-TF): the hypothesis of Theorem 3.3 holds at some point.

  A twin-free version of Proposition K would prove (MS-R). It would use the Mod-invariant functional 𝔪(X) = inf over subsurfaces Σ of type Σ_i of [max Ext(∂Σ) + d(ψ_Σ(X), Y_0)] instead of the marked Σ_i. Its endpoint branch would lie on a piece with no constant Y_0-component, i.e. outside 𝒩_0. The gap is termination: along the chosen Teichmüller rays some twin subsurface might keep a short boundary and ψ ≈ Y_0 forever. Lemma NH only lengthens ∂Σ_i of the marked subsurface. Interior (IMOV) transitions would also have to be handled, as in entry 99.
- (Rig) (entry 82) remains open, as before.





### R8-3 (excerpt). Theorem N and Corollary T (Krull pair at one lift, any automorphisms) (from round8_q3, verbatim, §§0–4.1)
## 0. Setting and conventions

The setting is MS8 exactly as in the task: (R1), (R2) with H_0 = id; V_0 is smooth, closed, 2-dimensional and totally geodesic; Δ_Γ is of product type; ∂V_t has dimension 1; π_i(∂V_t) = {Y_t}; and (Rig) holds.

Notation:
- B_t := closure(V_t) \ V_t = closure(V_t) ∩ ∂M̄_g. This is compact, since V_t is closed in M_g. By (R2), B_t = H_t(B_0), and H_t preserves strata.
- A *coarse piece* (at time 0) is a 1-dimensional irreducible component D of B_0 ∩ Δ_G, for some stable graph G. There are finitely many. We write D_t := H_t(D).
- For Q ∈ B_t, Def(Q) is the versal deformation germ, with smoothing parameters s_e and Aut(Q) acting. Points of the locus {s_e = 0 for all e} have components comp_x labelled by x ∈ V(G_Q). A lifted branch b̃ has a constant *pattern* S_b̃ = {e : s_e ≡ 0 on b̃}.
- A label y is *intact* along b̃ if every edge at y lies in S_b̃, and *merged* otherwise.
- [Z] denotes the class of an n_i-pointed curve in M_{g_i,n_i}/S_{n_i}. A *Y_t-copy* is a component Z with [Z] = [Y_t].
- By PR-A (re-checked; it uses only (R1), (R2)), t ↦ Y_t is holomorphic, so t ↦ [Y_t] is holomorphic.

**Standard fact used (cited from memory: partial normalization of a nodal family along node sections).** For S ⊂ E(G_Q), let G_S be G_Q with the edges not in S contracted. Then there is a holomorphic map Π_S : {s_e = 0 for all e ∈ S} → ∏_{w∈V(G_S)} M̄_w with the following properties.
- It is obtained by normalizing the nodes in S of the fibre curves.
- On the locus where exactly the edges of S vanish, it takes values in ∏ M_w and ξ_{G_S}∘Π_S equals the quotient map.
- At 0, the w-coordinate is the curve glued from the comp_x(0), x ∈ w, along the edges outside S that join them. Its marked points are the half-edges of S-edges at w.

**Finite sets supplied by (Rig).**
- F := ⋃_{(G,M,K)∈𝒦} K ∩ ∂(∏_{u∈M} M̄_u). This set is finite, because each K is an irreducible curve not contained in the boundary.
- F′ := the set of isomorphism classes, as pointed curves with unordered special points, of all smooth components of all coordinates of elements of F. It is finite.
- **Fact (P), the puncture lemma from chain step 3, re-checked.** Let p be a puncture of a piece E at any time. Then pr_{M(E)}ν(p) ∈ F. Indeed, constant vertices take their value in M_w, so some coordinate in M(E) lies in the boundary. Hence pr_{M(E)}ν(p) ∈ K(E) ∩ ∂, which is a subset of F.

---

## 1. Lemma 1 (the Y-locus is analytic)

Put Ŷ := {(Q,t) ∈ M̄_g × Δ : Q has a Y_t-copy}. Then Ŷ is a closed analytic subset of M̄_g × Δ.

*Proof.*
1. Fix a stable graph G of genus g and a vertex v of type (g_i,n_i). Put A_{G,v} := {(z,t) ∈ ∏_w M̄_w × Δ : [z_v] = [Y_t]}. This is the preimage of the graph of the holomorphic map t ↦ [Y_t] under the holomorphic map (z,t) ↦ ([z_v], t). Hence it is closed analytic.
2. The map ξ̄_G × id is finite, hence proper. By Remmert's proper mapping theorem, (ξ̄_G × id)(A_{G,v}) is closed analytic.
3. Ŷ is the finite union of these images over all pairs (G, v).
   - ⊆: let Q be a curve with a Y_t-copy at the vertex v of its own dual graph. Take z = (normalized components) ∈ ∏ M_w.
   - ⊇: let (z,t) ∈ A_{G,v}. Since z_v ≅ Y_t is smooth, ξ̄_G(z) has the irreducible component z_v. Its special points are exactly the n_v half-edges of v, and nodes inside the other z_w do not affect it. So z_v is a Y_t-copy of ξ̄_G(z). ∎

Put 𝓑 := closure(𝒱) ∩ (∂M̄_g × Δ). It is analytic by (R1), and 𝓑 = H(B_0 × Δ) by (R2). Put 𝓝 := Ŷ ∩ 𝓑, which is closed analytic. Its fibre is 𝓝_t = N_t := {Q ∈ B_t : Q has a Y_t-copy}.

---

## 2. Lemma 2 (dichotomy for coarse pieces)

Let D be a coarse piece. Exactly one of the following holds.
- (N) For every t, every point of H_t(closure D) has a Y_t-copy.
- (F) There is a countable set Z_D ⊂ Δ such that for t ∉ Z_D only finitely many points of H_t(closure D) have a Y_t-copy.

*Proof.*
1. **B_0 is pure 1-dimensional.**
   - Locally in Def(Q), every irreducible component X of the preimage of closure(V_0) is 2-dimensional and contains points of V_0. (At a point of X lying on no other component, nearby points of V_0 must lie on X.)
   - So ∏ s_e is not identically 0 on X, and X ∩ {∏ s_e = 0} has pure dimension 1 (Krull).
   - Also dim B_0 ≤ 1, since V_0 is dense in closure(V_0).
2. **The set D°.** Let D° be D minus the finitely many singular points of the compact curve B_0. Then D° is connected, being an irreducible curve minus a finite set. It is also open in B_0, since near a smooth point of B_0 lying on D, B_0 coincides with D.
3. **The set M_D.** M_D := H(D° × Δ) is open in 𝓑 and is a connected topological 4-manifold. Hence 𝓑 has pure dimension 2 along M_D.
   - Sing(𝓑) ∩ M_D is a closed subset of covering dimension ≤ 2. It does not disconnect the connected 4-manifold M_D (a closed set of dimension ≤ n−2 does not separate a connected n-manifold; Hurewicz–Wallman, cited from memory).
   - So M_D ∩ Reg(𝓑) is connected. It therefore lies in the regular part of a single irreducible component W of 𝓑, and M_D ⊂ W.
4. **Case W ⊂ 𝓝.** Then M_D ⊂ 𝓝. Since 𝓝 is closed and H_t(closure D) = closure(H_t(D°)), this is (N).
5. **Otherwise.** W ∩ 𝓝 is a proper analytic subset of the irreducible 2-dimensional W, so its dimension is ≤ 1.
   - Its irreducible components form a locally finite, hence countable, family. Let Z_D be the countable set of t such that some component lies in the fibre over t.
   - For t ∉ Z_D, the fibre (W ∩ 𝓝)_t is discrete. It is also compact, being closed in the compact 𝓑_t. So it is finite.
   - It contains N_t ∩ H_t(D°). Adding the finitely many points of H_t(closure D \ D°) gives (F).
6. **(N) and (F) exclude each other.** H_t(closure D) is infinite. ∎

Define:
- 𝒩 := {D : (N) holds}, and C_t := ⋃_{D∈𝒩} H_t(closure D).
- Every component of ∂V_0 lies in 𝒩, since vertex i ≡ Y_t on ∂V_t. Hence closure(∂V_t) ⊂ C_t.

**Remark 2.1.** Let D ∈ 𝒩 and let E be any piece at time t over D_t. Then some vertex w of E has f_w ≡ Y_t, a constant on E. Indeed, E is the union of the finitely many analytic sets {f_w ≅ Y_t}, so one of them is all of E.

Note: 𝒩 and C_t are defined without choosing or tracking any copy. Twins play no role in them.

---

## 3. Theorem N (how a copy can leave the network at a generic time)

Assume Y is non-constant. Define:
- Z_1 := ⋃_{D∉𝒩} Z_D, which is countable;
- Z_2 := {t : [Y_t] ∈ F′}, which is discrete, since [Y] is holomorphic and non-constant;
- Z := Z_1 ∪ Z_2. Call t ∉ Z *generic*.

**Theorem N.** Let t be generic. Let Q ∈ B_t with lift 0 ∈ Def(Q), let y be a label with comp_y(0) ≅ Y_t, and let b be any branch of B_t at Q, with a lift b̃ through 0 of pattern S. Then y is intact along b̃, and exactly one of the following holds.
- (STAY) comp_y ≡ Y_t along b̃. Then the coarse piece D′ with b \ {Q} ⊂ D′_t lies in 𝒩, so b ⊂ C_t.
- (IMOV) S = E(G_Q), so Q is an interior point of the piece of b, which lies in the stratum of Q. Moreover comp_y is non-constant along b̃.

Moreover N_t \ C_t is finite.

*Proof.*
1. **Setting up the piece.** Let G_b := G_S. Π_S(b̃ \ 0) is a 1-dimensional germ in ξ_{G_b}^{-1}(closure(V_t) ∩ Δ_{G_b}). So it lies in a piece E at time t, and Π_S(0) = ν(p) for a point p ∈ Ē. Let u be the vertex of G_b containing y.
2. **Merge is impossible.** Suppose an edge at y is not in S.
   - f_u(p) is the curve glued from the comp_x(0), x ∈ u. It has a node, so f_u(p) ∈ ∂M̄_u.
   - Hence p is a puncture. Also u ∈ M(E): a constant f_u would take its value in M_u (Lemma C2 of PR-C).
   - comp_y(0), with all its special points (the nodes inside u and the legs from S-edges), is a component of f_u(p).
   - By Fact (P), f_u(p) is a coordinate of an element of F. So [Y_t] ∈ F′, which contradicts t ∉ Z_2.
3. **Puncture-move is impossible.** Suppose y is intact, S ≠ E(G_Q), and comp_y is non-constant along b̃.
   - Then u = {y}, and f_u = comp_y along Π_S(b̃) is non-constant, so u ∈ M(E).
   - Some edge outside S is contracted into a vertex w, so f_w(p) is nodal and p is a puncture.
   - By (P), f_u(p) = comp_y(0) ∈ F′. This again contradicts t ∉ Z_2.
4. **The remaining cases.** y is intact. If comp_y is constant along b̃, every point of b has a Y_t-copy. So N_t ∩ D′_t is infinite, and since t ∉ Z_{D′}, Lemma 2 gives D′ ∈ 𝒩. Otherwise we are in (IMOV).
5. **Finiteness.** N_t \ C_t is finite by Lemma 2 (F) and t ∉ Z_1. ∎

**Corollary N1.** Let Y be non-constant and t generic. Suppose that no point of C_t carries an IMOV copy. Then:
- C_t is open and closed in B_t, so it contains the connected component B_t^∂ of B_t that contains ∂V_t;
- every Y_t-copy at every point of B_t^∂ is intact and constant along every branch of B_t there.

*Proof.* At Q ∈ C_t, every branch is STAY for the Y_t-copy that Q carries, so it lies in C_t. Hence C_t is open in B_t, and it is closed as a finite union of compact sets. ∎

---

## 4. Consequences

### 4.1 Corollary T (twin criterion under (Rig); no (O), no Lock, no restriction on automorphisms)

Let J ∈ closure(∂V_0) \ ∂V_0 lie in Δ_{G′}. Let 𝒞 and j(S) be as in PR-I Theorem 4. Assume:
- (Tw1) there is a neighbourhood U of J with B_0 ∩ U ⊂ ∂V_0 ∪ {J};
- (Mg) for all S ≠ S′ in 𝒞, some edge at j(S) is not in S′.

Then MS8 holds: Y_t = Y_0 for all t.

*Proof.*
1. Suppose Y is non-constant and take t generic. Put J_t := H_t(J) ∈ closure(∂V_t), and let q be a lift of J_t.
2. A branch of ∂V_t at J_t lifts to a branch β̃ through q, with pattern S ∈ 𝒞. By Lemma D(1) of PR-I, y := j(S) is intact and comp_y(q) ≅ Y_t.
3. J_t ∉ Δ_Γ, so there is an edge e ∉ S. Let X be an irreducible component, at q, of the preimage of closure(V_t) containing β̃.
   - s_e is not identically 0 on X, since it is nonzero on β̃ \ q.
   - So X ∩ {s_e = 0} is pure 1-dimensional through q (Krull). It contains a branch b̃ ≠ β̃ with e ∈ S_b̃.
4. By (Tw1), transported by H_t, b̃ lies over ∂V_t. So S′ := S_b̃ ∈ 𝒞, and S′ ≠ S because e ∈ S′ \ S.
5. By (Mg), y is merged along b̃. This contradicts Theorem N. ∎

**Remarks.**
- This is PR-I Proposition 3 / Theorem 4 with (O), (Tw2)(iii) and all Teichmüller-curve input replaced by (Rig).
- It holds whether or not Aut(J) swaps the twins. Theorem N concerns every copy at the same lift q, so the identity of "the" tracked copy never enters.
- In the quintic example, 𝒞 = {{e_1},{e_2}}, j({e_1}) = A has e_1 ∉ {e_2}, and symmetrically. So (Mg) holds.




### R8-2 (excerpt). Lemma U and the generic-time trichotomy (from round8_q2, verbatim, §§1–3)
## 1. Conventions and cited facts

- Classes of pointed curves are compared in the coarse space 𝔐 := M_{g_i,n_i}/S_{n_i}. "≅ Y" means equal class.
- For a stable graph G, 𝓦_G ⊂ ∏_w M̄_w × Δ is the lifted family of R7-5 (P2). It is analytic by (R1) and proper over Δ. "W" always denotes a 2-dimensional irreducible component of some 𝓦_G.
- By R7-5 (P4), applied at every t (the argument is symmetric in t by (R2), and closure(V_t) is compact analytic by (R1)): every fibre W_t is non-empty and of pure dimension 1. Each 1-dimensional component D of W_t is the closure of a piece E at time t, so (Rig) applies to E. Write M(D) := M(E) and K(D) := K(E).
- Cited from memory (standard):
  - **Remmert's proper mapping theorem.**
  - **Cartan–Remmert.** For a holomorphic map Φ of complex spaces, {x : dim_x Φ^{-1}Φ(x) ≥ k} is analytic.
  - **Stein factorization** (Grauert–Remmert). A proper holomorphic map f: X → S factors as X → T → S, with X → T proper, surjective and with connected fibres, and T → S finite. If X is normal, so is T.
  - **Normal surfaces** have isolated singularities.

## 2. Lemma U (uniformity under (Rig)) — proved

**Lemma U.** Assume (R1), (R2) and (Rig). Let W be a 2-dimensional irreducible component of 𝓦_G. There are a set M_W ⊂ V(G) and an irreducible closed curve K_W ⊂ ∏_{u∈M_W} M̄_u, not contained in the boundary, with the following property. For **every** t ∈ Δ and **every** 1-dimensional component D of W_t:
- M(D) = M_W and K(D) = K_W;
- every vertex u ∉ M_W is constant on D;
- D = K_W × {c_D} for a point c_D ∈ ∏_{u∉M_W} M_u.

*Proof.*

**Step 1 (generic moving set).** Let n: W^ν → W be the normalization, a normal surface. Let W^ν →a T →b Δ be the Stein factorization of t∘n, which is proper. T is a normal, hence smooth, curve and b is finite.
- **Critical values are discrete.** Let C be an irreducible curve of critical points of a on W^ν_reg. Then d(a|_C) = 0, so a is constant on C. The singular points of W^ν are isolated. Hence the set of critical values of a (images of Sing W^ν, of isolated critical points, and of critical curves) is discrete in T.
- **Generic fibres are irreducible.** For τ ∈ T outside a discrete set, a^{-1}(τ) is a smooth, compact, connected curve, hence irreducible.
- **Fibres of W.** Since n is finite and surjective, for every t, W_t = ⋃_{τ ∈ b^{-1}(t)} n(a^{-1}(τ)). Every component of W_t is the image of a component of some a^{-1}(τ). For generic t the components of W_t are exactly the irreducible curves n(a^{-1}(τ)), τ ∈ b^{-1}(t).
- **The dichotomy for a vertex u.** Put Φ_u := (pr_u∘n, a): W^ν → M̄_u × T and R_u := {x : dim_x Φ_u^{-1}Φ_u(x) ≥ 1}, which is analytic by Cartan–Remmert.
  - If R_u = W^ν: let K be a component of a fibre a^{-1}(τ) and x ∈ K a point on no other component. The Φ_u-fibre through x lies in a^{-1}(τ) and is 1-dimensional at x, so it contains the germ of K at x. Hence pr_u is constant on K. So u is constant on every component of every fibre of a, and therefore on every component of every W_t.
  - If R_u ≠ W^ν: then dim R_u ≤ 1. Every fibre component on which pr_u is constant lies in R_u, and the components of R_u are locally finite. So this happens only for τ in a discrete subset of T.
- Put M_W := {u : R_u ≠ W^ν}. Then for t outside a discrete set Z_W ⊂ Δ, every component of W_t has moving set exactly M_W. For every t and every component of W_t, every u ∉ M_W is constant on it. M_W ≠ ∅, since components of W_t are curves.

**Step 2 (one image curve).** Let Σ := (pr_{M_W}, t)(W) ⊂ ∏_{u∈M_W} M̄_u × Δ. It is closed, analytic and irreducible (Remmert; the map is proper on W). It has dimension 2, since t is non-constant on it and its generic fibres are curves.
- For t ∉ Z_W and a component D of W_t, pr_{M_W}(D) is the closure of the image of the piece, i.e. K(D).
- By (Rig), K(D) belongs to the finite list {α^{-1}K : α ∈ Aut(G), (G, αM_W, K) ∈ 𝒦}, with factors relabelled by α. Call its members K_1, …, K_N.
- So Σ ∩ {t ∉ Z_W} ⊂ ⋃_j K_j × Δ, and by closedness Σ ⊂ ⋃_j K_j × Δ.
- Σ is irreducible of dimension 2, so it lies in one K_j × Δ, and equals it since both are irreducible of dimension 2. Put K_W := K_j.
- For each u ∈ M_W, pr_u|_{K_W} is non-constant, because K_W = K(D) for a generic-time component D with u ∈ M(D).

**Step 3 (all times).** Let t be arbitrary and D a component of W_t.
- By Step 1 the vertices outside M_W are constant on D. So D ⊂ pr_{M_W}^{-1}(pr_{M_W}(D)) ∩ {coordinates outside M_W constant}.
- pr_{M_W}(D) ⊂ Σ_t = K_W is closed and irreducible, so it is a point or all of K_W. If it were a point, every coordinate would be constant on the curve D, which is absurd.
- So pr_{M_W}(D) = K_W. Every u ∈ M_W is non-constant on D (end of Step 2), so M(D) = M_W and K(D) = K_W.
- D is an irreducible curve inside the irreducible curve K_W × {c_D}, so the two are equal. Here c_D ∈ ∏ M_u, because D is the closure of a subset of ∏_w M_w and the coordinates of c_D are constant on D. ∎

**Corollaries.**
- **U1 (L1′ with its converse; no non-product pathology).** For each W and vertex u, the following are equivalent:
  - u is constant on one component of one fibre;
  - u ∉ M_W;
  - u is constant on all components of all fibres.

  In particular the situation of R7-5 §1.4 (u constant on E_0 but non-constant on σE_0 inside the same W) cannot occur under (Rig). Consequently, for a component W' through a point p obtained from W by ρ ∈ Aut(G): M_{ρW} = ρM_W and K_{ρW} = ρK_W.
- **U2 (t-independent image curves; the earlier worker's Lemma 6, repaired).** The partial file's Lemma 6 asserts that "M is the same for all t by L1′". L1′ gives only one direction, and for non-product G the fibres of W can have components with different moving sets unless (Rig) is used as above. Lemma U is the correct statement.
- **U3 (puncture values).** For each W, the values pr_{M_W}(ν(p)) at punctures p of components of W_t lie in K_W ∩ ∂(∏ M̄_u). This is a finite set independent of t.
- **U4 (constant-vertex value curves).** For u ∉ M_W, Γ_{W,u} := (pr_u, t)(W) is an irreducible curve, finite over Δ. Its fibre over t is the set of values of u on the components of W_t.

## 3. Generic times and the trichotomy (Theorem 1) — proved

From now on assume, for contradiction, that **Y is non-constant**. Y: Δ → 𝔐 is holomorphic by PR-A, so its graph is an irreducible curve.

**The finite set 𝔉 ⊂ 𝔐 (independent of t).**
- Let 𝒫_1 be the set of points of K ∩ ∂(∏_{u∈M} M̄_u), over all (G, M, K) ∈ 𝒦 and all Aut(G)-relabellings. It is finite: K is an irreducible compact curve not contained in the boundary.
- Let A_1 be the set of classes of the smooth components, with their special points, of all coordinates of points of 𝒫_1.
- Let 𝒫_2 be the set of points κ ∈ K such that the class of some coordinate pr_z(κ), z ∈ M, lies in A_1. It is finite, because pr_z|_K is non-constant for z ∈ M (Lemma U).
- Let 𝔉 be the set of classes of the smooth components of all coordinates of the points of 𝒫_1 ∪ 𝒫_2.

**The set Z.** Z is the set of t ∈ Δ such that one of the following holds:
- Y_t ∈ 𝔉;
- (Y_t, t) lies on the image in 𝔐 × Δ of some curve Γ_{W,u} (u ∉ M_W, M_u of type (g_i,n_i)) that is not the graph of Y.

Each W, and each such pair (W,u), contributes a discrete set: in the first case because Y is non-constant, in the second because two distinct irreducible curves meet discretely. The components W are locally finite over Δ. Hence **Z is discrete** in Δ.

Call a pair (W,u) with Γ_{W,u} ↦ graph(Y) a **Y-vertex**.

**Theorem 1.** Let t ∉ Z, Q ∈ B_t, q a lift of Q in Def(Q), and y a Y_t-copy of q (comp_y(q) ≅ Y_t). Let b̃ be a lifted branch through q of a branch b of B_t at Q. Let E be the piece of b at time t, with graph G_b and component W ⊃ E. Then exactly one of the following holds.
- **(STAY)** Every edge at y is pinched along b̃, y is a constant vertex of E, and (W, y) is a Y-vertex.
- **(IMOV)** Q is an interior point of E (so Q ∈ Δ_{G_b}), and y ∈ M_W. Moreover, for every z ∈ M_W and every other lifted branch b̃′ through q, z is neither merged along b̃′ nor non-constant at a puncture along b̃′.

In particular, a Y_t-copy is never merged along a branch (**MERGE excluded**), and never intact and non-constant at a puncture (**puncture-MOV excluded**).

*Proof.*
1. **Merge.** Suppose some edge at y is unpinched along b̃. By R7-1 Lemma 1(a) (= R7-4 Lemma 1), the point p of Ē over Q is a puncture, the vertex u ∋ y of G_b is non-constant, and comp_y(q) is a component, with the same special points, of f_u(p).
   - By Lemma U, u ∈ M_W and pr_{M_W}ν(p) ∈ 𝒫_1.
   - So Y_t ∈ A_1 ⊂ 𝔉, contradicting t ∉ Z.
2. **Puncture-move.** Suppose y is intact, {y} is non-constant, and Q ∉ Δ_{G_b}. Then p is a puncture and f_y(p) = comp_y(q) (R7-1 Lemma 1(b)). So Y_t ∈ A_1, again a contradiction.
3. **Constant.** Suppose y is intact and constant on E. Its value is comp_y(q) ≅ Y_t, so (Y_t, t) lies on the image of Γ_{W,y}. Since t ∉ Z, Γ_{W,y} maps onto graph(Y): this is STAY.
4. **Remaining case.** Here y is intact and non-constant, and Q ∈ Δ_{G_b}. So y ∈ M_W, and κ := pr_{M_W}(lift of Q) ∈ K_W.
   - Suppose some z ∈ M_W were merged, or moving at a puncture, along another branch b̃′ through q. Then, as in 1–2, comp_z(q) = pr_z(κ) has class in A_1. So κ ∈ 𝒫_2, and Y_t ≅ pr_y(κ) lies in 𝔉, a contradiction. ∎

**Remark.** Theorem 1 never compares two copies. At a generic t, *every* Y_t-copy obeys it, whatever the automorphisms of Q. Twins matter only when information is transported between t = 0 (where total geodesy is available) and generic t. That is the subject of §4.




## Reminder
Check every inference of round13_q10 and give an explicit verdict on whether it proves the conditional theorem exactly as stated, with repairs and remaining dependencies listed.
