kind: write-up (consolidation into a complete, self-contained proof; simplification welcome)

## Task
A research document on the problem stated below presents, as its main result, a CONDITIONAL theorem:

**Theorem A.** Assume the problem's hypotheses, read as (R1) and (R2^orb) below (equivalently, by "Theorem LG", (R1), (R2) and the chart-level local orbifold reading (Loc)). Then Y_t = Y_0 for all t ∈ Δ.

The proof was found and refereed in earlier analyses; that material is spliced verbatim below (the write-up "round13_q10", its referee report with repairs (Rep-1)–(Rep-6), Theorem RO and its verification with repairs R1′–R3′, the walk-chain check, and the transport lemmas it uses: Lemma U and the generic-time trichotomy, Theorem N and Lemma 1, the Kuranishi-chart transport lemmas, Lemmas T, S, J and Theorem R, Lemma PT). It is scattered, uses shifting notation and refers to further texts.

Your job: write ONE coherent Markdown text "Part II" giving a complete, self-contained proof of Theorem A, in consistent notation, with all referee repairs incorporated, so that a referee who sees ONLY your text, the problem statement, and the "Part I" statements listed below can check every step. Rules:
- You may take as given ONLY: (a) the Part I results listed below (they are written up separately, with full proofs; quote them by the labels I.1–I.6 and state precisely the form you use); (b) classical theorems, cited explicitly by name with the precise statement used. Everything else — Theorem RO with Lemma R*′, Lemma 1.1 and Prop. T; Lemma U and Theorem 1 (generic-time trichotomy); Theorem N and its Lemma 1; the transport-family lemmas (closure(Ñ_c̃) ⊂ Ñ_c̃ ∪ 𝒥, pure dimension 2, Lemma B1♭); Lemmas T, S, J, Theorem R and the product-type endpoint; Lemmas 3.1, 3.2, Prop. 3.3, Lemmas 4.1, 4.2, Prop. 4.3; the induction along the walk chain and the endpoint argument; Theorem LG — must be proved in your text.
- Simplification is welcome. Under (R2^orb) much of the twin machinery should collapse (one Aut(Q)-fixed lift-curve at every puncture point; isotropy preserved; a descended transport Π_t at the level of ∏_w M_w that maps pieces to pieces). If you see a shorter complete route to Theorem A from Part I and (R2^orb), give it — but it must be complete. If you keep the original route, streamline it.
- Do not refer to the spliced analyses by name (no "round13_q10", "R8-3", "entry 19"); write each argument out.
- Where a step cannot be completed, mark it "GAP:" with a precise description. Flag the scope question for the Imayoshi–Shiga finiteness theorem with marked points used in Theorem RO, and resolve it if you can (e.g. by passing to level covers / finite-type targets, or via the hyperbolic-curve rigidity for (1,1), (0,4)).
- For EVERY lemma, say explicitly whether its proof uses (R2^orb) or only (R1), (R2) (the coarse reading: H a stratum-preserving homeomorphism, H_0 = id), plus (Rig) where needed. The document also presents a coarse-reading reduction that reuses the coarse-valid lemmas (Lemma U, the generic-time trichotomy, Theorem N and its Lemma 1, the transport-family lemmas, B1♭, Lemmas T, S, J, Theorem R, Lemma 4.1(a),(b) first part, Lemma 4.2), so please prove those under the weakest hypotheses their proofs allow and label them accordingly.
- Also state precisely the readings (R1), (R2), (R2^orb), (Loc), and the qualification (Rep-6): (R2^orb) formalises the embedded/substack orbifold reading, not the intrinsic one.

## Part I (taken as given; statements only — make them precise as you use them; their exact forms appear in the spliced texts)
- I.1 Lemma PA: at a generic point of any 1-dimensional boundary piece E of closure(V_0), norming differentials of tangent vectors of V_0 have full-area limits supported on the vertices of maximal Teichmüller speed along E; some vertex has positive area, constant vertices have none.
- I.2 Theorem TV (with Corollary Φ̂): every 1-dimensional boundary piece E of closure(V_0) in every stratum has a vertex j with π_j∘ν: E^ν → C^ν a proper orbifold covering of a Teichmüller curve C (C^ν = H/Γ′, E^ν = H/Λ_E, Λ_E ⊂ Γ′ of finite index), whose universal-cover lift is the Teichmüller disc; every end of E maps to a cusp; E is not compact.
- I.3 Lemmas CS, CL, J0: Lemma CL (a continuous lift through a properly discontinuous quotient of a holomorphic map is holomorphic); Lemma J0 (at t = 0 the joint vertex map of every piece, in every stratum, lifts holomorphically to T_G over H/Λ_E, with isometric Teichmüller coordinate and coset-valued monodromy; repair R3′ in non-product strata).
- I.4 Theorem X*_all.
- I.5 Proposition K_w (walk chain) with repairs, Gap A repair and Lemma S̃′: from a generic point of ∂V_0 there are pieces D^1 ⊂ ∂V_0, D^2, …, D^k of closure(V_0) (in various strata), transition points J_1, …, J_{k−1} and an endpoint Q_0; at J_m an entering lift β̃_m (of a branch of D^m) and a leaving lift β̃′_m (of a branch of D^{m+1}) in a chart Def(J_m), with common chart label x_m, both lifts in one irreducible component of q^{-1}(closure V_0) ∩ B; along each travel interval the tracked label is a constant vertex of the piece with value ≅ Y_0 and the marking identification x_m ↔ c ↔ x_{m+1} holds; at Q_0 an entering lift β̃ with label x and a terminal lift b̃ in one such component, with x MERGE (some edge at x unpinched along b̃ ∖ 0) or MOV ([F_x] non-constant along b̃) at t = 0. The finite sets R(D) are included among the transition points (interior transitions).
- I.6 Corollary IMOV_all: a transition point in the stratum of either adjacent piece has β̃′_m = β̃_m with the same label; hence Q_0 and every genuine transition (β̃′_m ≠ β̃_m) satisfy (P): they are punctures of both adjacent pieces (not in the stratum of either).
- Lemma PT: in a product-type stratum no automorphism of a stable curve moves a vertex of positive-dimensional type.

Output format: a single Markdown document headed "Part II", with numbered conventions, statements and proofs, ending with "Proof of Theorem A", then "Cited classical facts" (precise statements) and "GAPs" (possibly empty). Completeness matters more than brevity; up to about 25,000 words is fine. Begin with a one-paragraph status line saying what you achieved (in particular whether your proof of Theorem A from Part I is complete).

## Spliced material (verbatim; bookkeeping lines removed)
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





### Referee report on the write-up above (verbatim)
# round14_q9 — referee check of round13_q10 ("(R1) + (R2^orb) ⇒ Y_t = Y_0")

**Plan/status line.**
- I read the whole task file: round13_q10, and the spliced round12_q9, round13_q9, round11_q9, round11_q1, round11_q4, R8-3 and R8-2 excerpts.
- I check §§0–7 of round13_q10 in order. "✓" means I checked the inference and it is valid; "repair" means I supply a fix.
- Verdict, repairs and remaining dependencies are at the end (§V).

**Status at the end.**
- No fatal gap in the derivation of the conditional theorem.
- Six repairs or corrections are needed. Four are minor and do not touch the main line: (Rep-1) to (Rep-3) and (Rep-5).
- Two concern side claims:
  - (Rep-4): the closing remark of §6, "(Loc) near t_0 = 0 suffices", is **not proved** as written.
  - (Rep-6): the faithfulness claim of §7 has to be qualified. (R2^orb) is faithful to the *embedded / substack* orbifold reading, not to an *intrinsic* orbifold reading. The §7 example in fact satisfies the intrinsic reading.

---

## 1. §§0–1: the formalisation of (R2^orb) and the convention on Mod_G

**(R2^orb) as (a)–(d).**
- The formal statement is unambiguous: a continuous H̃^G on Ã_0 × Δ satisfying (a) lifting, (b) Mod_G-equivariance, (c) equality of Mod_G-stabilisers, (d) H̃_0 = id. ✓
- (R2^orb) contains (R2) verbatim, so Step 1 is trivial. ✓
- **Standing-reading caveat (not new; stated so the dependency list is complete).** (R2) is itself an interpretation of the problem's (i)+(ii). The problem gives, stratum by stratum, smoothly trivial families together with the compatibility (ii). (R2) assumes **one** homeomorphism H : closure(V_0) × Δ → closure(𝒱) over Δ that trivialises all strata simultaneously, with H_0 = id. (R1) — closure(𝒱) analytic with fibres closure(V_t) — is likewise a reading. round13_q10 takes both as the run's standing readings. I do not re-examine them here, but they are dependencies of the final claim.

**Convention on Mod_G.**
- Mod_G is the group of pairs (σ, (φ_w)), with σ ∈ Aut(G) acting on half-edges. It contains ∏_w Mod_w (pure) with finite index, and T_G/Mod_G = Δ_G as a set and as a coarse space. ✓
- This agrees with round12_q9 §1: "finite extension by lifts of Aut(G), [T_G/Mod_G] = Δ_G as a sub-orbifold, isotropy Aut(z)".
- Allowing σ to swap the two half-edges of an edge is necessary. Automorphisms of Z can exchange the branches at a node, for example at a self-loop. Lemma 3.2 needs this to make the stabiliser map surjective. ✓

**Consequences listed in §1.** Items 1–3 are correct pointers to Lemma 3.2 + (c), round12_q9 Lemma 1.1, and Prop. T. ✓

## 2. §2: Theorem RO applies; which of (a)–(d) it uses

I re-traced the uses against the spliced round12_q9 and its verification round13_q9.

- **Lemma 1.1.**
  - Descent uses (b) for Mod_Π. ✓
  - Π_t lands in Â_t by (a). ✓
  - Injectivity uses (a), injectivity of H_t, and **one inclusion** of (c), namely Stab(H̃_t x) ⊂ Stab(x). ✓
  - Surjectivity uses (a), (b) and Mod_G-invariance of Ã_0. ✓
  - Continuity of Π_t holds because p × id is open on the saturated set Ã_0 × Δ. ✓
  - Continuity of Π_t^{-1} uses properness of ξ_G. ✓
  - "Pieces to pieces" is topological. ✓
  - The finite-type claim for Ê_t needs the repair (R1′) of round13_q9 (Chow). Round13_q10 inherits that repair through "Theorem RO with its repairs".
- **Prop. T** uses (a) through Lemma 1.1 and (b) for g ∈ Mod_Π, and Lemma CL gives holomorphy. ✓
- **Where (d) is used.** I can confirm one place where (d) is genuinely needed: in RO Step 6 (constancy), Π_0 = id is what identifies the constant value with K(E_0). In Prop. T, (d) only gives the consistency F_t|_{t=0} = F_0. Round13_q10's description is accurate.
- **Hence** Theorem RO applies under (R1), (R2^orb), TV/Φ̂ (+PA/TR) and Imayoshi–Shiga. It gives (Rig) in the labelled form, with K(E_t) = K(E_0) and M(E_t) = M(E_0). ✓
- **Strength of the output.** The (Rig) needed by Theorem N, Lemma U (R8-2) and the chain is the "finite set 𝒦 of triples up to Aut(G)-relabelling" form. RO's labelled form is stronger, so it suffices. ✓

**Verdict on §2:** correct. RO uses (a), (b), (c) (one inclusion) and (d), each exactly as stated.

## 3. §3: Lemma 3.1, Lemma 3.2, Proposition 3.3

### Lemma 3.1 (t ↦ Q_t holomorphic at a puncture point) — correct

**Step 1.**
- Near (Q,0), 𝓑 = H((c_1 ∪ ⋯ ∪ c_m) × Δ_ε), because H : B_0 × Δ → 𝓑 is a homeomorphism (by (R2), boundary maps onto boundary). ✓
- The decomposition 𝓑 = Γ_Q ⊔ ⊔_k N_{c_k} near (Q,0) holds by injectivity of H. ✓
- Each N_{c_k} is open in 𝓑 ∖ Γ_Q, because H is a homeomorphism and c_k ∖ Q is open in B_0 ∖ Q near Q. ✓

**Step 2.**
- dim 𝓑 ≤ 2, since 𝓑 is a proper analytic subset of the 3-dimensional closure(𝒱), in which 𝒱 is dense. ✓
- A 1-dimensional component W_i of the germ is not contained in the union of the others. At a point of W_i off the others, 𝓑 is locally a 1-dimensional analytic set, of topological dimension 2. Such a point cannot lie in an N_c, which is a 4-manifold. So W_i minus the other components lies in Γ_Q. By density and closedness, W_i ⊂ Γ_Q. ✓
- The 2-dimensional components cover N := ⊔N_c. Since Γ_Q ⊂ closure(N), they cover 𝓑. ✓

**Step 3.**
- For an irreducible germ, a small representative has connected Reg(W_j) (standard). ✓
- The removed set R := (Γ_Q ∪ ⋃_{i≠j} W_i) ∩ Reg(W_j) is closed in Reg(W_j) and has covering dimension ≤ 2: Γ_Q ≅ disc, and W_i ∩ W_j is analytic of dimension ≤ 1. ✓
- Hurewicz–Wallman (from memory): a closed subset of dimension ≤ n − 2 does not separate a connected n-manifold. ✓
- So Reg(W_j) ∖ R is connected and lies in one N_{c_k}. It is dense in W_j, because R has empty interior in the 4-manifold. Hence W_j ⊂ closure(N_{c_k}) = H(c_k × Δ_ε) (closure taken near (Q,0)). ✓

**Step 4.** Distinct c_k are disjoint off Q and H is injective, so each W_j lies in one H(c_k × Δ). Hence H(c_k × Δ_ε) is the union of the W_j it contains, and so it is analytic. ✓

**Step 5.**
- By (P), β ∩ Δ_G = {Q} near Q. H preserves strata, so Γ_Q = H(β × Δ_ε) ∩ (Δ_G × Δ_ε).
- Δ_G is open in closure(Δ_G): its complement there is a union of smaller strata, which is closed. So near Q we may replace Δ_G by closure(Δ_G), and Γ_Q is a closed analytic curve germ. ✓

**Step 6.** Γ_Q → Δ_ε is a homeomorphism, with inverse t ↦ (Q_t, t), which is continuous. So Γ_Q is locally irreducible everywhere and its normalisation is bijective. t∘ν is a bijective holomorphic map of smooth curves, hence biholomorphic. Therefore t ↦ Q_t is holomorphic. ✓

**Step 7.** ✓

**Scope.** Lemma 3.1 needs one branch with (P) at Q. Every point where the chain invokes MS11♭, and the endpoint, has (P) for both lifts (round11_q9 §1.2, entry 99). ✓

### Lemma 3.2 (Stab_{Mod_G}(x̂) ≅ Aut(Z)) — correct; two examples in the remark are wrong (Rep-1)

**The proof.**
- Uniqueness of α_w: two biholomorphisms in the same isotopy class differ by a biholomorphism of a stable pointed surface isotopic to the identity, which is the identity. ✓
- σ preserves the pairing of half-edges, so ⊔α_w descends to Z. ✓
- Injectivity: α(g) = id forces σ = id on vertices and on half-edges, hence α_w = id and φ_w = 1. ✓
- Surjectivity: lift α to the normalisation. ✓
- K_G ⊂ every stabiliser. ✓
- "(c) modulo K_G ⇔ (c)": both stabilisers contain K_G, so each is determined by its image in Mod_G/K_G. ✓

**(Rep-1), correction to the remark "cases named in the brief".** Two of the listed examples of elements of K_G are wrong. Neither is used anywhere.
- *"Hyperelliptic involution of a (2,0)-component."* A boundary stratum has at least one edge and a connected graph, so every vertex carries at least one half-edge. A (2,0)-vertex therefore does not occur.
- *"Elliptic involution of a (1,2)-component, extended by the identity."* With both special points labelled and fixed, the involution x ↦ −x about p_1 fixes p_2 only when p_2 is 2-torsion. So it is not a generic automorphism.
- *Correct examples:*
  - the elliptic involution of a (1,1)-vertex, extended by the identity;
  - for a (1,2)-vertex whose two special points are the half-edges of a self-loop, the pair (σ swapping the two half-edges, x ↦ p_1 + p_2 − x). That pair is an automorphism of every curve in the stratum.
- The statement "(c) controls all of Aut(Z)" is unaffected.

### Proposition 3.3 [orb] (one lift-curve) — correct

**Item 1.** x̂ ∈ Ã_0 over Q (Q ∈ A_0 trivially) and ŷ = H̃_t x̂ lies over Q_t by (a). Then (c) and Lemma 3.2 give Aut(Q_t) ≅ Aut(Q). ✓

**Item 2.**
- (Kur), from memory: for B small, [B/Aut(Q)] → M̄_g is an open embedding of stacks. That is, Stab_{Aut(Q)}(p) ≅ Aut(X_p) for every p ∈ B. ✓ (This is the standard Deligne–Mumford local structure. The isomorphism is with the full, possibly non-effective, Aut(Q), which is consistent with Lemma 3.2 counting K_G.)
- So |Stab_{Aut(Q)}(p)| = |Aut(Q_t)| = |Aut(Q)|. Hence Stab = Aut(Q), and the orbit q^{-1}(Q_t) ∩ B is a single point. ✓

**Item 3.**
- Continuity: the graph is closed, q is proper on a closed invariant ball, and q^{-1}(Q) ∩ B̄ = {0}. ✓
- Lemma CL applies to the finite group Aut(Q) acting on B. Its proof needs only a properly discontinuous action of a countable group and the Cartan quotient. t ↦ Q_t is holomorphic into q(B) ≅ B/Aut(Q) by Lemma 3.1 and (Kur). ✓
- 𝒥 = graph(p). ✓

## 4. §4: Lemma 4.1, Lemma 4.2, Proposition 4.3

### Shrinking convention — correct, and an even simpler route
- Ñ′_c̃ is connected, lies in q^{-1}(N_c) ∩ (B × Δ_ε), and meets Ñ_c̃. Hence Ñ′_c̃ ⊂ Ñ_c̃.
- An irreducible T′ lies in some component T of closure(Ñ_c̃), and T is anchored.
- The persistence locus is analytic and contains T′, so it equals T. ✓
- The opposite direction (big sheet ⇒ small sheet), which the chain also uses, is immediate here, since persistence equals C(L) and L is a germ. If x ∈ P(T) for an anchored T at scale (B, ε), then x ∈ C(L) by Lemma 4.1(b) and Lemma 4.2 (⊆). By Lemma 4.2, x ∈ P(T′) for every anchored T′ of a branch with (P), at any smaller scale. ✓
- Anchored sheets (T ⊃ c̃ × {0}) coincide with round11_q9's c̃-sheets (slice containing an open subset of c̃ ∖ 0). This is by closedness, given that c̃ ∩ B is irreducible (Milnor ball). ✓

### Lemma 4.1 — correct
- **(a)** c̃ × {0} ⊂ closure(Ñ_c̃), and an irreducible curve lies in one of the finitely many components. ✓
- **(b), setting up.**
  - t ≢ 0 on T, and Krull gives slices of pure dimension 1 at each point. ✓
  - The points (p_n, t_n) ∈ T ∖ 𝒥 exist. ✓
  - q(p_n) ∈ H_{t_n}(c ∖ Q), because T ⊂ Ñ_c̃ ∪ 𝒥 near (0,0) (R7-4 Lemma 2). ✓
  - z_n → Q by continuity of H^{-1}. ✓
  - The arc α_n ⊂ c ∩ U, and H_{t_n}(α_n) ⊂ q(B″). ✓
- **(b), arc argument.**
  - q|_B : B → B/Aut(Q) is proper, so Remmert gives q(C) a closed irreducible curve in q(B), contained in Z = B_{t_n} ∩ q(B). ✓
  - Z is a topological 2-manifold at the points of the open arc, because H_{t_n} is a homeomorphism and B_0 is a smooth disc there. Hence Z is locally irreducible there. ✓
  - O is non-empty (it contains q(p_n), the endpoint H_{t_n}(z_n)). It is open by definition. It is closed in the arc, because q(C) is closed and its germ at any of its points is pure 1-dimensional inside the irreducible germ Z_w. ✓
  - So the arc lies in q(C). Q_{t_n} lies in the closure of the arc and in q(B), so Q_{t_n} ∈ q(C). ✓
- **(b), conclusion.**
  - p′_n → 0 by properness and q^{-1}(Q) ∩ B̄ = {0}.
  - (0,0) is therefore not isolated in the analytic set T ∩ 𝒥, so the germ contains a curve. That curve is a component of the 1-dimensional germ 𝒥, which has no component in {t = 0} because 𝒥 ∩ {t = 0} = {(0,0)}. So T contains a lift-curve. ✓
- This gives a precise proof of round11_q1 Lemma 2.1(c), whose original wording ("every irreducible curve of Σ_t … ") was loose.

### Lemma 4.2 — correct (given Theorem N, R8-3 Lemma 1, entry 19)
- ⊆ ✓.
- ⊇:
  - T_t is pure 1-dimensional at p = p(t). ✓
  - γ ∖ p ⊂ Ñ_c̃ ∩ {t} ⊂ q^{-1}(H_t(c ∖ Q)). So q(γ) is the branch H_t(c) of B_t at Q_t; that branch is locally irreducible, being homeomorphic to a disc. ✓
  - By (Kur), the germ of Def(Q) at p is a versal deformation of Q_t compatible with labels, so Theorem N applies at (Q_t, p, γ). ✓
  - IMOV needs Q_t ∈ Δ_{G_c}. But Q_t ∈ Δ_{G_Q} ≠ Δ_{G_c}, because H preserves strata and (P) holds. So STAY holds. ✓
- The countability argument: an analytic set of dimension ≤ 1 contains curves in only countably many t-slices, while generic t form an uncountable set. Hence A_y = T by irreducibility. ✓

### Proposition 4.3 — correct
- Prop. 3.3 gives 𝒥 = L.
- Lemma 4.1(b) gives L ⊂ T_β and L ⊂ T_b.
- Lemma 4.2 (⊆) on T_β, which needs no (P), gives x ∈ C(L). Lemma 4.2 (⊇) on T_b, which needs (P) for b̃, gives x ∈ P(T_b). ✓
- The hypothesis and conclusion match MS11♭ (round11_q9 §5), since anchored sheets = c̃-sheets. The extra hypotheses of MS11♭ ((S), β̃ ≠ b̃) are not needed. ✓

## 5. §5: the chain

- **Step 1.** (Rig) comes from RO. Every result proved under (R1), (R2), (Rig) and "Y non-constant" applies, because (R2^orb) ⊃ (R2). ✓
- **Steps 2–3.**
  - At genuine transitions (β̃′_m ≠ β̃_m) and at the endpoint, both lifts satisfy (P) (round11_q9 §1.2, from S̃′ + X*_all). So these points are puncture points. ✓
  - Trivial transitions (β̃′ = β̃) need nothing. ✓
- **Step 4.** MS11♭ is invoked only at non-product genuine transitions. There Prop. 4.3's hypotheses hold:
  - J_m is a puncture point;
  - (P) holds for β̃′_m;
  - persistence holds on an anchored (= β̃_m-) sheet, by the induction hypothesis in round11_q9's strong form;
  - (Rig) holds and Y is non-constant.

  The other steps are round11_q9 §§2.5–2.7 (inherited). ✓
- **Step 5 (endpoint).**
  - *Product type:* inherited (Lemma PT, Lemma J, Theorem R). ✓
  - *Non-product type:* Prop. 4.3 gives an anchored T ⊃ b̃ × {0} with x persistent. At t = 0, x is intact on b̃ ∩ B and F_x ≅ Y_0 there.
  - **(Rep-2), a small precision.** The MOV witness z̃^∞ ∈ b̃ ∖ 0 of round11_q9 may lie outside the shrunken ball B used for Prop. 3.3. Then argue as in round11_q9 §2.8:
    - the pattern is constant on b̃ ∖ 0, so x is intact on all of b̃;
    - F_x is holomorphic on L_x ⊃ b̃;
    - the identity theorem along the connected normalisation of b̃ (in the original Milnor ball) propagates [F_x] ≡ [Y_0] to z̃^∞.

    This contradicts MOV ([F_x(z̃^∞)] ≠ [Y_0]). MERGE contradicts intactness. ✓
- **Step 6.**
  - The contradiction shows [Y] is constant.
  - **(Rep-3), a precision.** The problem asks for π_i(∂V_t) = {Y_0} in M_{g_i,n_i}, not only [Y_t] = [Y_0] in M_{g_i,n_i}/S_{n_i}.
    - By PR-A (entry 19, as quoted in R8-3 §0), t ↦ Y_t ∈ M_{g_i,n_i} is itself holomorphic.
    - If [Y_t] ≡ [Y_0], then Y_t lies in the finite set S_{n_i}·Y_0.
    - A continuous map from the connected Δ into a finite set is constant, so Y_t = Y_0. ✓

## 6. §6: Theorem LG and the reading (Loc)

**"Why (Loc) is the chart-level reading" — (Rep-5).**
- The inclusion Stab(h_s u) ⊂ φ(Stab u) is proved for elements b in the image of φ, i.e. b ∈ Stab(h_{t_0} x̂). To get equality of the **full** Mod_G-stabilisers, shrink W and I so that h((W ∩ Ã_0) × I) ⊂ W′. Here W′ is a slice neighbourhood of h_{t_0}(x̂) with gW′ ∩ W′ ≠ ∅ ⇒ g ∈ Stab(h_{t_0} x̂), and W is a slice neighbourhood of x̂ of the same kind.
- Then every b ∈ Mod_G fixing h_s(u) lies in Stab(h_{t_0} x̂), and every a ∈ Mod_G fixing u lies in Stab(x̂). So Stab_{Mod_G}(h_s u) = φ(Stab_{Mod_G}(u)), and (L2) holds.
- The sentence "φ is independent of s by continuity, since the set of isomorphisms is discrete" is not a deduction. The equivariance relation determines φ_s(a) only modulo the pointwise stabiliser of h_s(W ∩ Ã_0), which can be non-trivial on a 1-dimensional Ã_0. So "a single φ for all s ∈ I" has to be part of the reading of "continuous family of orbifold maps", not a consequence of it. This does not affect Theorem LG, which assumes (L1), (L2) directly.

**Lemma U.**
- E is closed (T_G is Hausdorff).
- E is open: use the slice neighbourhood U of y, the fact that fibres of ξ_G∘p are Mod_G-orbits, g_s ∈ Stab(y), and local constancy of Stab(γ_1(s)). ✓
- Only γ_1 needs locally constant stabiliser.

**Construction.**
- (Loc) at (x, τ_j) gives lifts h^j of H_s for s ∈ I_j, defined on neighbourhoods of the **same** x ∈ Ã_0 (the domain is at time 0). So the gluing is meaningful. ✓
- The normalisation h^1_0(x) = a x is correct, since H_0 = id. ✓
- The stabiliser is constant on each closed piece by (L2), and the values agree at the junctions. ✓
- Uniqueness follows from Lemma U. ✓

**(a)–(d) and uniqueness of H̃.** ✓ For (b), g∘γ_{x,t} lifts the same path, starts at gx, and has locally constant stabiliser, so it is γ_{gx,t} by Lemma U.

**Joint continuity.**
- j = 1: x and a_x x both tend to x_0, so a_x ∈ Stab(x_0) by proper discontinuity. ✓
- Induction: K_j = Stab(y_0) = K_{j+1}, and the two candidates lie in a common slice neighbourhood of y_0 over the same point. So they differ by k′ ∈ Stab(y_0), and Lemma U applies on [r_j, r_{j+1}]. ✓
- Final step: k ranges in a finite group fixing H̃_{t_1}(x_0). ✓
- **Theorem LG is correct.**

**(Rep-4): the closing remark "(Loc) only near t_0 = 0 suffices" is not proved.**
- (Loc) at (x̂, 0) gives a disc I(x̂) whose radius depends on x̂. Ã_0 is not compact modulo Mod_G: A_0 accumulates on smaller strata at the punctures of the pieces. So there may be no common r > 0 with (a)–(d) on Ã_0 × Δ_r.
- Theorem RO needs H̃ on all of Ã_0 for each t considered (Lemma 1.1's surjectivity and the piece transport), so a non-uniform radius does not suffice as written.
- The disc-size caveat in that remark is itself harmless: rescaling t ↦ rt yields an admissible family over Δ, and entry 19 propagates the identity Y_t ≡ Y_0. Uniformity of the radius is the real issue.
- The remark is correct if (Loc) is assumed at all (x̂, t_0) with |t_0| < r for a fixed r > 0. The main Theorem assumes (Loc) at all t_0 ∈ Δ and is unaffected.

## 7. §7: is (R2^orb) a faithful formalisation?

**(Rep-6): the claim must be qualified.**
- "Orbifold reading" admits two inequivalent precise forms.
- **(O-emb), the embedded / substack reading.** A_t is the reduced closed substack of the stack Δ_G = [T_G/Mod_G], so its isotropy at z is the full Aut(z). The trivialisation is an isomorphism of substacks over Δ, i.e. local lifts equivariant through **isomorphisms of the ambient local groups** Aut(z) → Aut(H_t z).
  - Under (O-emb), (L1)+(L2) hold, by the computation above with (Rep-5). Theorem LG then gives (a)–(d).
  - So **(R2^orb) is faithful to (O-emb).** ✓
- **(O-int), the intrinsic reading.** Each A_t (and V_t) is given its own effective orbifold structure, and H_t is an orbifold diffeomorphism A_0 → A_t of these intrinsic structures. Equivalently, an orbifold map into Δ_G whose local group homomorphisms need not be onto, or injective, on the ambient groups.
  - (O-int) is strictly weaker than (O-emb).
  - **The §7 example satisfies (O-int).** σ : u ↦ −u fixes the curve {u = 0} pointwise, so the intrinsic (effective) isotropy of that curve is trivial. The transported curve {u = ±t}/σ is a smooth curve with trivial intrinsic isotropy. Hence H_t is an intrinsic orbifold diffeomorphism (of trivial orbifolds), while (c) fails.
- So the correct statement is:
  - **(R2^orb) ⇔ (O-emb) ⊊ (O-int) ⊆ coarse (R2)**, at least locally. The first equivalence ⇐ is Theorem LG; ⇒ holds by definition.
  - The Theorem settles the problem under (O-emb) only.
- The problem's wording ("smooth subvariety of M_g", "complex submanifold 𝒱 ⊂ M_g × Δ", "smoothly trivial family") does not choose among these. As §7 itself says, the literal wording leans towards the coarse reading.

**The example itself.**
- The coarse chart is smooth (U = u²).
- H_t(U, v) = (U + t², v) is holomorphic, stratum-preserving and smooth, so it is (R2)-admissible at chart level.
- |Aut(H_t z)| < |Aut(z)| for t ≠ 0, so (c) fails.
- The non-existence of a lift with (a) and (c) follows directly by counting stabiliser orders. Lemma U is not even needed.
- It is a chart-level model only, as stated. Whether a global admissible family with such an isotropy drop exists is open. ✓

**"Compatibility (ii) is not needed beyond (R2)."** Correct as a statement about the proof. But (ii) is one of the problem's hypotheses that (R2) is meant to encode; see §1 above.

---

## §V. Verdict, repairs, remaining dependencies

### Verdict
**Round13_q10, together with the cited inputs, proves the conditional theorem exactly as stated:** under (R1) and (R2^orb) — equivalently, by Theorem LG, under (R1), (R2) and (Loc) at all (x̂, t_0) ∈ Ã_0 × Δ — Y_t = Y_0 for all t ∈ Δ.
- The new parts are Lemma 3.1, Lemma 3.2, Prop. 3.3, Lemmas 4.1–4.2, Prop. 4.3, the chain bookkeeping of §5, and Theorem LG. I checked every inference in them and found them valid, with the minor repairs below.
- The key mechanism is sound: (c) + Lemma 3.2 + (Kur) ⇒ the lift locus is a single Aut(Q)-fixed curve, so every anchored sheet contains it, and persistence transfers through it.
- The conclusion π_i(∂V_t) = {Y_0} follows with (Rep-3).
- Not established by round13_q10 as written:
  - the §6 closing remark (Rep-4);
  - the unqualified claim in §7 that (R2^orb) is "the" orbifold reading (Rep-6).

  Neither is needed for the theorem.

### Repairs (all supplied above)
- **(Rep-1)** Lemma 3.2 remark: the (2,0) and (1,2) examples of K_G are wrong. Correct examples are given. Not used anywhere.
- **(Rep-2)** Endpoint: if the MOV witness lies outside the shrunken ball, propagate along b̃ by the identity theorem (as in round11_q9 §2.8).
- **(Rep-3)** From [Y_t] constant to Y_t constant in M_{g_i,n_i}: holomorphy of Y_t (PR-A), finiteness of S_{n_i}-orbits, and connectedness of Δ.
- **(Rep-4)** The §6 remark "(Loc) near t_0 = 0 suffices" is unproved: radii of (Loc) are not uniform on the non-compact A_0. It is valid if (Loc) holds on a fixed disc Δ_r (then rescale).
- **(Rep-5)** "Why (Loc)": shrink to slice neighbourhoods to get equality of the full Mod_G-stabilisers. The constancy of φ in s is part of the reading, not a deduction.
- **(Rep-6)** §7: (R2^orb) is faithful to the embedded/substack orbifold reading (O-emb), not to the intrinsic one (O-int). The §7 example satisfies (O-int) but violates (R2^orb).

### Remaining unchecked dependencies (from round13_q10 §8.2, confirmed and completed)
1. **Standing readings:** (R1), and (R2) as one global stratum-preserving homeomorphism encoding (i)+(ii). Also the choice (O-emb) for (R2^orb).
2. **Theorem RO inputs:**
   - round8_q10 Theorem TV (items 1–4; by round13_q9 §3.1(d), item 2 reduces to properness of p_E) and Corollary Φ̂;
   - Lemma PA / Lemma TR (positive area at the vertex j), which round8_q10 itself cites from memory;
   - round13_q9 repairs (R1′), (R2′), (R3′);
   - Imayoshi–Shiga finiteness for punctured types (scope from memory; types (1,1) and (0,4) are covered by hyperbolic-curve rigidity instead).
3. **Chain (round11_q9):**
   - entries 85, 98, 112, 113 (walk chain, Gap A / R(D) repair, including the "routine" marking-continuity detail along travel intervals);
   - Lemma S̃′, Theorem X*_all (via Lemma P with (Res)/(Neg)/(RA)), Cor. IMOV_all (entries 97, 99);
   - Lemma B1♭;
   - Lemma PT, Lemmas T, S, J, Theorem R (entries 84, 86, 87);
   - the cited inputs listed in round11_q9 §4 (Lemma NH, (Fl), (Prop), Kerckhoff, Maskit, Wolpert/Abikoff, T̄_g/Def chart description, Milnor conic structure).
4. **Run lemmas used in §4:**
   - Theorem N and Lemma 1 of R8-3;
   - R7-4 Lemma 2 (closure(Ñ_c̃) ⊂ Ñ_c̃ ∪ 𝒥, pure dimension 2);
   - R8-2 Lemma U / Theorem 1 (through the chain);
   - entries 19 (PR-A) and 24.
5. **Classical results cited from memory:**
   - Deligne–Mumford local structure (Kur), in the stack form Stab_{Aut(Q)}(p) ≅ Aut(X_p);
   - proper discontinuity of Mod_G and slice neighbourhoods;
   - connectedness of Reg of an irreducible germ;
   - Hurewicz–Wallman non-separation;
   - invariance of domain;
   - normalisation of curves;
   - Remmert;
   - Krull;
   - Chow;
   - the classical inputs of RO (Royden, Earle–Kra, Bers, Thurston, Selberg, orbifold uniformisation, Bers embedding, Cartan).

### Open (named)
- The problem under the coarse reading (R2), and under the intrinsic orbifold reading (O-int). Both (Rig) and MS11♭ are open there, and the obstruction is isotropy drop at boundary points.
- Existence of a global admissible family (satisfying (i), (ii)) with isotropy drop at the boundary.
- The exact scope of Imayoshi–Shiga for punctured types.
- Whether (Loc) near t_0 = 0 alone (with non-uniform radii) implies (a)–(d) on some Δ_r × Ã_0.


### Kuranishi-chart transport lemmas R7-3 and R7-4 (verbatim excerpts)
### R7-3. Kuranishi-chart transport lemmas, (TR) without twins, the twin dichotomy, and a chart-local twin-jump model (from round7_q5, verbatim, sections 1–5)
## 1. Set-up: Kuranishi charts and chart components

**Standard facts (cited from memory).**

(K1) Let J be a stable curve. It has a universal deformation over a smooth germ Def(J), with smoothing parameters s_e for the nodes e ∈ E(G_J), and Aut(J) acts on Def(J). A neighbourhood of J in M̄_g is Def(J)/Aut(J). So the preimages in Def(J) of a point J′ near J form one Aut(J)-orbit.

(K2) Let x be a vertex of G_J, and let L_x := {s_e = 0 for every edge e at x}, a smooth subgerm. Over L_x the fibre curve has a component "x", deforming J_x. This gives a holomorphic map F_x : L_x → M_{g_x,n_x}. Its special points are labelled by the half-edges at x.

(K3) For σ ∈ Aut(J) and q ∈ L_x we have σq ∈ L_{σx}, and σ induces an isomorphism of fibre curves taking component x to component σx. Hence

 F_x(σq) ≅ F_{σ^{-1}x}(q)  (as pointed curves, after relabelling).

Throughout, "≅ Y" means isomorphic as an n_i-pointed curve up to relabelling. Equivalently, we compare images in the coarse space M_{g_i,n_i}/S_{n_i}, which is an analytic space. All identity-theorem arguments below take place there.

**Interpretation of the hypotheses of (TR).** "The c_m-limit along D^m and the c_{m+1}-limit along D^{m+1} are the same component of J_m (tracked by path markings)" is read as follows. There are lifts β̃^m, β̃^{m+1} ⊂ Def(J_m), through 0, of the relevant branches of ξ(D^m) and ξ(D^{m+1}) at J_m, and a vertex x_m of G_{J_m}, such that:
- c_m is the single chart vertex x_m along β̃^m;
- c_{m+1} is the single chart vertex x_m along β̃^{m+1}.

This is what continuity of the marking inside the chart gives. The merge at Q_0 is read the same way: there are lifts β̃^k, β̃^E ⊂ Def(Q_0) and a chart vertex x with c_k = {x} along β̃^k and x ∈ class(u) along β̃^E.

A constant vertex c has a smooth limit at J. So c corresponds to a single chart vertex with no contracted edges, and the branch lies in L_x.

## 2. Transport lemmas

**Lemma 1 (constant values are holomorphic; generic constancy).** Let D be a piece at time 0, D_t := H_t(D) its transport, and c a vertex of D's graph.
(a) If c is constant on D, then c is constant on D_t for every t. Its value φ_c(t) is a holomorphic function of t.
(b) If c is non-constant on D, then c is non-constant on D_t for all t outside a countable set.

*Proof.* (a) Constancy is L1. Fix p ∈ D. Then φ_c(t) = pr_c of a lift of H(p,t). This is continuous in t, because H is continuous and lifts through the finite map ξ can be chosen continuously along paths.

Let 𝓦 be the irreducible 2-dimensional analytic set of Lemma R0 (PR-D) for D. Then Γ := (pr_c, t)(𝓦) is an irreducible analytic set (Remmert), whose fibre over each t is finite by L1. So Γ is a curve, finite over Δ. A continuous function whose graph lies in such a curve is holomorphic off a discrete set, where the curve is locally a union of graphs, and hence everywhere by Riemann extension.

(b) Let C ⊂ 𝓦 be the analytic set where (pr_c, t) has rank ≤ 1. Suppose pr_c is constant on the fibre components over uncountably many t. Then C contains uncountably many fibre curves. A ≤ 1-dimensional analytic set contains only countably many of them, so C = 𝓦. By the rank theorem the image Γ is then an irreducible curve that is not contained in a fibre of t, so it is finite over Δ. Hence pr_c is constant on every fibre component, including at t = 0. ∎

**Lemma 2 (transport of a lifted branch in a fixed chart).** Let J ∈ closure(V_0) \ V_0 and J(t) := H_t(J). Let β̃ ⊂ Def(J) be a lifted branch at 0 of a piece D, where either J is a puncture of D, or J ∈ ξ(D) and β̃ is the lifted germ of D itself. Let x be a chart vertex such that a vertex c, constant on D, equals {x} along β̃. Then for |t| < ε there is a set Ñ ⊂ Def(J) × Δ_ε with the following properties:
- Ñ is a connected analytic set with Ñ ∩ {t = 0} = β̃ \ {0}, or β̃ itself in the interior case;
- for each t, closure(Ñ_t) contains a lift J̃_β(t) of J(t), and Ñ_t ∪ {J̃_β(t)} ⊂ L_x;
- F_x ≡ φ_c(t) on Ñ_t ∪ {J̃_β(t)}.

*Proof (puncture case; the interior case is the same with D's own lifted family).*

1. Let β be the image branch of ξ(D) at J. Then N := H((β \ {J}) × Δ_ε) is a topologically trivial family of punctured discs. By (R2), near J(t) we have closure(ξ(D_t)) ∩ Δ_{G_J} = {J(t)}, because closure(ξ(D)) \ ξ(D) is finite and H_t is a stratum-preserving homeomorphism.
2. Let Ñ be the connected component of the preimage of N in Def(J) × Δ_ε that contains β̃ \ {0}. The preimage of the analytic family of D is analytic (Lemma R0 and Remmert), and N is open and closed in it near (J,0). So Ñ is analytic. Ñ is a connected topological 4-manifold, being a cover of a punctured disc times a disc. Hence Ñ is irreducible: removing a singular set of real codimension ≥ 2 does not disconnect it.
3. The pinching pattern {e : s_e ≡ 0} is constant on the irreducible set Ñ. At t = 0 it contains every edge at x, so Ñ ⊂ L_x.
4. Fix once and for all an identification of the contracted graph with D's graph. This gives a holomorphic map from Ñ to ∏_w M_w. Its image is irreducible and meets the lift of D at t = 0. So it lies in the lifted family 𝓦 of D, and F_x = pr_c on Ñ. By L1 and Lemma 1, pr_c ≡ φ_c(t) on 𝓦_t.
5. Ñ_t → N_t = β_t \ {J(t)} is proper and finite (K1). So points of Ñ_t approaching J(t) accumulate at lifts of J(t). Pick one, J̃_β(t). It lies in L_x because L_x is closed, and F_x(J̃_β(t)) = φ_c(t) by continuity of F_x. ∎

**Remark.** The same proof applies when the vertex containing x along β̃ is a non-constant vertex u. Then the u-limit at J̃_β(t) is the curve obtained by gluing the chart components in class(u) at J̃_β(t). This is a puncture value f_u^t(p) of D_t, at the puncture of D_t lying over J(t). Moreover u is non-constant on D_t whenever class(u) contains a contracted edge: a constant smooth curve cannot have a nodal limit (Lemma C2 of PR-C).

**Lemma 3 (twist).** Let β̃, β̃′ be lifted branches at 0 ∈ Def(J), with transports Ñ, Ñ′ and lifts J̃_β(t), J̃_{β′}(t). Then for each t there is σ_t ∈ Aut(J) with J̃_{β′}(t) = σ_t J̃_β(t). Some single σ occurs for all t in a set T_σ that is uncountable, and in particular accumulates at 0.
Moreover σ_t^{-1}·closure(Ñ′_t) is a lifted branch of D′_t through J̃_β(t). Along it, the vertex containing a chart vertex y is the σ_t^{-1}-image of the vertex of Ñ′_t containing σ_t y.

*Proof.* The two lifts of J(t) lie in one Aut(J)-orbit by (K1). Aut(J) is finite, and a finite union of the sets T_σ covers the uncountable disc. Aut(J) preserves the preimage of closure(V_t). The last statement is (K3). ∎

## 3. Theorem A: (TR) holds without twins

**Hypothesis (NT).**
- For each junction J_m (m < k): every σ ∈ Aut(J_m) fixes the chart vertex x_m.
- At Q_0: every σ ∈ Aut(Q_0) fixes x.

A sufficient condition: no other component of J_m (respectively Q_0) is isomorphic to the x_m-component (respectively the x-component), as a curve with unordered special points.

**Theorem A.** Assume the hypotheses of (TR), L1, and (NT). Then:
- φ_{c_m} ≡ Y for every m;
- for all t in a disc around 0 minus a countable set, the transported piece E_t has a vertex u that is non-constant on E_t and a puncture p′ such that f_u^t(p′) has a component isomorphic to Y_t.

*Proof.*
1. **Junctions.** Fix m < k. Apply Lemma 2 at J = J_m to (β̃^m, c_m, x_m) and to (β̃^{m+1}, c_{m+1}, x_m). This gives
 F_{x_m}(J̃^m(t)) = φ_{c_m}(t) and F_{x_m}(J̃^{m+1}(t)) = φ_{c_{m+1}}(t).
 By Lemma 3, J̃^{m+1}(t) = σ_t J̃^m(t). By (K3) and (NT),
 F_{x_m}(σ_t J̃^m(t)) = F_{σ_t^{-1}x_m}(J̃^m(t)) = F_{x_m}(J̃^m(t)).
 So φ_{c_{m+1}}(t) = φ_{c_m}(t) for all small t, and both functions are holomorphic (Lemma 1). Hence φ_{c_{m+1}} ≡ φ_{c_m} on Δ by the identity theorem.
 By induction from φ_{c_1} = Y (since c_1 = i on ∂V_t), we get φ_{c_k} ≡ Y.
2. **The merge at Q_0.** Apply Lemma 2 at Q_0 to (β̃^k, c_k, x), and apply the Remark after Lemma 2 to (β̃^E, u). Then F_x(Q̃^k(t)) = Y_t.
 Let Q̃^E(t) = σ_t Q̃^k(t). The u-limit of E_t at the puncture over Q(t) is the gluing of the components in class(u) at Q̃^E(t). This class contains x, whose component is
 F_x(σ_t Q̃^k(t)) = F_{σ_t^{-1}x}(Q̃^k(t)) = F_x(Q̃^k(t)) = Y_t, by (NT).
 Q(t) is not in ξ(E_t), because H_t preserves strata and Q_0 ∉ ξ(E). So this limit is a puncture value f_u^t(p′).
3. **u is non-constant.** In the MERGE case, class(u) contains a contracted edge, and the Remark after Lemma 2 shows that u is non-constant on E_t for every t. In the puncture-MOV case (u = {x} along β̃^E), u is non-constant on E_0, so it is non-constant on E_t for all t outside a countable set, by Lemma 1(b). ∎

**Corollary A.** Combine Theorem A with chain steps 1–4 (which use L1, L2 and (O)). If Prop K's configuration at t = 0 satisfies (NT) and ends in MERGE or in puncture-MOV, then Y_t = Y_0 for all t.

Note that (NT) **fails** in the quintic example (PR-I). There P_0 = A–B–C with A ≅ C ≅ Y_0, and the symmetric chain has an automorphism exchanging A and C. That example is settled by a different, time-t Krull argument (see §5).

## 4. The twin case: a robust analysis

From now on we argue by contradiction and **assume Y is non-constant**. Let Φ be the finite family of holomorphic functions consisting of:
- Y;
- the φ_c for all pieces D at time 0 and all vertices c constant on D;
- the constant functions given by the (finitely many) components of the elements of the finite sets F(E_0,u) of L2.

Let Z ⊂ Δ be the countable set of t at which one of the following happens:
- two distinct functions of Φ take the same value;
- some vertex changes from non-constant to constant (Lemma 1(b)).

Call t ∉ Z *generic*.

**Lemma 4 (closedness of the Y-network at generic time).** Let t be generic, J ∈ closure(V_0) \ V_0, and let q ∈ Def(J) be a lift of J(t). Let β̃_t, β̃′_t be two transported lifted branches through q, i.e. sets of the form ρ·closure(Ñ_t) with ρ ∈ Aut(J). Let y be a chart vertex that is, along β̃_t, a single constant vertex c with φ_c ≡ Y. Let w be the vertex of the piece D′ of β̃′_t that contains y. Then one of the following holds.
- (a) w = {y} is a constant vertex of D′ with φ_w ≡ Y.
- (b) J(t) ∈ ξ(D′_t) is an interior point of D′_t, and w = {y} is non-constant on D′_t with pr_y(J(t)) ≅ Y_t. Call this *interior-MOV*.

In particular, (i) w never contains a contracted edge, and (ii) w is never a non-constant vertex at a puncture.

*Proof.*
- F_y(q) ≅ φ_c(t) = Y_t.
- Suppose w contains a contracted edge, or w is non-constant on D′_t with J(t) a puncture. Then Y_t is a component of a puncture value f_w^t(p), which lies in a finite set F(D′_0, w) by L2 (and L1). So Y_t equals one of the constant functions in Φ, which is impossible for generic t because Y is non-constant.
- Suppose w is constant. Then w = {y} (its limit is smooth) and φ_w(t) = Y_t. For generic t this forces φ_w ≡ Y.
- The remaining case is (b). ∎

**Theorem B (twin dichotomy).** Assume Y is non-constant. Let a junction J_m satisfy φ_{c_m} ≡ Y. Then:
- either φ_{c_{m+1}} ≡ Y;
- or there is σ ∈ Aut(J_m) with σ x_m ≠ x_m (a *twin jump*) such that, along the t = 0 branch β̃^{m+1}, the chart vertex σx_m is a single constant vertex c′ of D^{m+1} with φ_{c′} ≡ Y. The exception is an interior-MOV event at J_m.

Similarly, at Q_0: either the conclusion of (TR) holds for all generic t (impossible, since it forces Y_t into a finite set), or there is σ ∈ Aut(Q_0) with σx ≠ x such that, along β̃^E, σx is a single constant vertex of E with φ ≡ Y (again up to interior-MOV).

Hence, if Y is non-constant and there is no interior-MOV event, the Y-network performs at least one twin jump along the chain of (TR).

*Proof.*
1. Take t ∈ T_σ (Lemma 3) generic, q = J̃^m(t), β̃_t = closure(Ñ^m_t), β̃′_t = σ^{-1}closure(Ñ^{m+1}_t), and y = x_m.
2. Lemma 4 says the vertex of β̃′_t containing x_m is a Y-network constant. By (K3), that vertex is the σ^{-1}-image of the vertex of Ñ^{m+1}_t containing σx_m.
3. The pinching pattern and the vertex structure are constant along Ñ^{m+1}, so the same holds on β̃^{m+1} at t = 0.
4. If σx_m = x_m, this vertex is c_{m+1}, and φ_{c_{m+1}} ≡ Y.
5. At Q_0, run the same argument with β̃′ = σ^{-1}·(transport of β̃^E). If σx = x, the vertex containing x is u, which contradicts Lemma 4 (i)/(ii). ∎

**What a twin jump means.** At t = 0 the curve J_m has two components x_m ≠ σx_m, both isomorphic to Y_0 and exchanged by an automorphism. The marked track of Prop K continues along x_m into a constant vertex c_{m+1} with φ_{c_{m+1}} ≢ Y. The deformation, however, carries the Y-network on to the twin σx_m. For t ≠ 0 the automorphism σ no longer exists: J(t) has two different components φ_{c_m}(t) = Y_t and φ_{c_{m+1}}(t), which coincide at t = 0.

## 5. Why (TR) is not decided here: a local model and a t = 0 reformulation

**Local model (twin jump, consistent in the chart).**
- Let Def(J_0) contain coordinates (a, b) of the two Y_0-components x, y, with σ(a, b) = (b, a). Let J(t) have lifts J̃(t) = (t, −t, …) and σJ̃(t) = (−t, t, …).
- Suppose the transported D^m passes through J̃(t), with constant vertex at x of value Y_0 + t (= Y_t) and constant vertex at y of value Y_0 − t.
- Suppose the transported D^{m+1} passes through σJ̃(t), with c_{m+1} at x of value Y_0 − t, and a network vertex at y of value Y_0 + t.
- At t = 0 both branches pass through 0, and c_m, c_{m+1} both sit at x. So the hypotheses of (TR) at this junction hold.
- Lemma 4 is satisfied at every time, because D^m has a network vertex at y as well. Krull's theorem at time t gives no further constraint unless the global stratum structure is known, as in PR-I.

So no argument confined to the Kuranishi charts at the junctions can prove (TR). Any proof must use global information about how the marked Teichmüller track of Prop K sits relative to the deformation. Constructing an actual family V_t realizing this model is out of reach; I have **no counterexample**.

**How the quintic example escapes.** There the extra input is Krull at time t in Def(P_t) (PR-I Prop 3), together with the knowledge that every boundary branch near P_t lies over ∂V_t. This produces, at the same point q at time t, a branch with the opposite pinching pattern. Its network vertex lies inside the non-constant vertex of the first branch, which is the violation (ii) of Lemma 4. The general version of this observation: Krull at time t produces coherent pairs of branches (pairs through the same lift) with a prescribed pinched edge, but it does not control which pieces they belong to.

**A t = 0 statement that would suffice (MS7, open).** Call a set 𝒩 of pairs (D, c) — D a piece at time 0, c constant on D with value ≅ Y_0, containing (each component of ∂V_0, i) — **Aut-closed** if the following holds. For every J ∈ closure(V_0) \ V_0, every lifted branch β̃ at 0 ∈ Def(J) of some (D, c) ∈ 𝒩 with c = {x}, and every lifted branch β̃′ at 0 of any piece D′ through J, there is τ ∈ Aut(J) such that the vertex of D′ containing τx along β̃′ is a single constant vertex c′ with (D′, c′) ∈ 𝒩. (Interior points of D′ are included.)

- Lemma 4, transported to t = 0 as in Theorem B, shows: **if Y is non-constant and no interior-MOV event occurs, then the Y-network {(D, c) : φ_c ≡ Y} is Aut-closed.**
- So MS7 — "no Aut-closed set 𝒩 exists" — implies Y_t = Y_0, modulo the interior-MOV case.
- Prop K does not prove MS7. Its track follows the marking, which at a twin junction may continue along x_m rather than along σx_m (§4). If the track always stays inside 𝒩, Prop K does give a contradiction (Theorem A is the special case where this is automatic).


### R7-4. Time-t criterion, transport of branch patterns, total-merge transport, spreading of Y_t-copies (from round7_q2, verbatim, sections 0–4)
## 0. Notation used throughout

- B_t := closure(V_t) \ V_t. This is a compact analytic set of dimension ≤ 1. By (R2), H_t(B_0) = B_t, and H_t preserves strata.
- For a point Q ∈ B_0, put Q_t := H_t(Q).
- Def(Q) is the versal deformation germ of the stable curve Q, with smoothing parameters s_e, e ∈ E(G_Q). The group 𝔅 := Aut(Q) acts on Def(Q). The germ of M̄_g at Q is q : Def(Q) → Def(Q)/𝔅.
- On the locus {s_e = 0 for all e ∈ E(G_Q)} ≅ ∏_{x ∈ V(G_Q)} Def(Q_x), each point p has components comp_x(p), labelled by the vertices x of G_Q. Each comp_x(p) is a smooth curve carrying its special points, and it depends holomorphically on p.
- An element a ∈ 𝔅 acts on labels, and comp_x(a p) ≅ comp_{a^{-1}x}(p) as pointed curves.
- The fibre q^{-1}(Q) is {0}. Since q is proper, every lift of Q_t tends to 0 as t → 0.
- **Pattern.** For a point p of Def(Q) put S(p) := {e : s_e(p) = 0}. For S ⊂ E(G_Q):
  - an edge not in S is *unpinched*;
  - a vertex x is *intact* for S if every edge at x lies in S, and *merged* otherwise;
  - M(S) denotes the set of merged vertices.
- A *Y_t-copy* of a point P is a component of P that is isomorphic to Y_t as an n_i-pointed curve, in some order of its special points.
- C_0(Q) := {x ∈ V(G_Q) : comp_x(0) is a Y_0-copy}. This set is 𝔅-invariant.
- A *boundary branch* at Q is a local branch b at Q of B_0 with Q ∉ the stratum of b. Equivalently, Q is a puncture of the piece E_b that contains b.
  - A lift b̃ ⊂ Def(Q) has constant pattern S_b̃. The other lifts are the translates a b̃, with patterns a S_b̃.
  - M^+(b̃) := M(S_b̃) ∪ {x intact for S_b̃ : comp_x is non-constant along b̃}.

## 1. Lemma 1 (time-t criterion for MS6)

**Lemma 1.** Fix t. Suppose there are:
- a point P ∈ B_t,
- a lift P̃ ∈ Def(P),
- a Y_t-copy y of P̃,
- a lift c̃ through P̃ of a boundary branch c at P,

such that y ∈ M(S_c̃), or y is intact for S_c̃ and comp_y is non-constant along c̃. Then the MS6 configuration exists at time t.

*Proof.*
1. Let E be the piece at time t that contains c̃. Concretely, E is the irreducible component, in ∏_w M_w of the stratum Δ_{G_c}, of the lift of closure(V_t) ∩ Δ_{G_c} that contains the image of c̃. Here the stratum locus S_c̃ of Def(P) is mapped to ∏_w M_w by taking partial normalizations. This is compatible with ξ_{G_c}, after identifying G_P / (E(G_P) \ S_c̃) with G_c.
2. P is not in Δ_{G_c}. So the endpoint of c̃ corresponds to a puncture p of Ē.
3. Let u be the vertex of G_c that contains y. Then f_u(p) is the curve obtained by gluing the components comp_x(P̃), x ∈ u, along the unpinched edges between them.
   - comp_y(P̃) is an irreducible component of f_u(p).
   - Its special points in f_u(p) are its special points in P. A half-edge at y is either part of an unpinched edge inside u, which becomes a node of f_u(p), or a half-edge of a pinched edge, which becomes a marked point of M̄_u.
   - So it is a Y_t-copy.
4. **Case y merged.** f_u(p) has a node, so f_u(p) ∈ ∂M̄_u. On E the values of f_u lie in M_u. So f_u is not constant. This is Lemma C2 of PR-C.
5. **Case y intact.** u = {y}, and f_u = comp_y along c̃ is non-constant by hypothesis. In both cases (E, u, p) is an MS6 configuration at time t. ∎

**Remark.** The converse does not hold in the relevant sense. A configuration "Y_t-copy y at an interior point P ∈ E, with the vertex of E carrying y non-constant" (called **MOV-interior** below) is NOT an MS6 configuration. At an interior point there is no puncture, and the moving value lies on a curve, not in a finite set.

## 2. Lemma 2 (transport of branch patterns)

**Lemma 2.** Let Q ∈ B_0 and let b be a boundary branch at Q. Put N := H((b \ {Q}) × Δ) near (Q,0). Then:
- (a) the components of q^{-1}(N) ⊂ Def(Q) × Δ are permuted transitively by 𝔅, and the pattern is constant on each of them. So the components are the a Ñ, with patterns a S, where Ñ ⊃ b̃ has pattern S = S_b̃;
- (b) for every t and every lift Q̃_t of Q_t, some a Ñ has Q̃_t in the closure of its t-slice. For that a, the lift of the branch H_t(b) through Q̃_t has pattern a S;
- (c) the closure of N near (Q,0) is a union of irreducible 2-dimensional germs of an analytic set. The same holds for q^{-1}(N).

*Proof.*
(a) **Patterns are constant on components.**
- The sets {S(p) = S'} for distinct S' with isomorphic contracted graphs are pairwise disjoint.
- Each is relatively open in the union of all strata of that graph type, because a nearby point has fewer zero coordinates unless it is in the same stratum.
- So S(·) is locally constant on q^{-1}(N) ⊂ q^{-1}(Δ_{G_b} × Δ), and hence constant on each component.

**Transitivity.**
- q restricted to q^{-1}(N) is open and closed (finite quotient), and q^{-1}(N) is locally connected (semi-analytic). So each component maps onto N, which is connected: it is homeomorphic to a punctured disc times a disc.
- If Z_1, Z_2 were components with 𝔅Z_1 ∩ 𝔅Z_2 = ∅, take a point n ∈ N. Its fibre is a single 𝔅-orbit, and it would have to lie in both 𝔅Z_1 and 𝔅Z_2, a contradiction.

(b) Q_t ∈ closure(H_t(b)). Hence the closure of q^{-1}(H_t(b)) contains a point of q^{-1}(Q_t) = 𝔅 Q̃_t. By 𝔅-invariance it contains Q̃_t. Near Q̃_t the set q^{-1}(H_t(b)) is contained in ⋃_a (a Ñ)_t. Apply (a).

(c) **The set 𝒜.** Let 𝒜 := closure(𝒱) ∩ (closure(Δ_{G_b}) × Δ). It is analytic by (R1). Let 𝒵 be the part of 𝒜 over strata deeper than Δ_{G_b}; it is analytic.

**N is open and closed in 𝒜 \ 𝒵.**
- Near (Q,0), 𝒜 \ 𝒵 = H((closure(V_0) ∩ Δ_{G_b} ∩ U) × Δ) by (R2).
- For U small, closure(V_0) ∩ Δ_{G_b} ∩ U is a disjoint union of punctured branches at Q, since Q ∉ Δ_{G_b}.
- So N is open and closed in 𝒜 \ 𝒵.

**Conclusion.**
- Let X be an irreducible component of 𝒜 not contained in 𝒵. The set X minus (𝒵, Sing 𝒜, and the other components) is connected and dense in X.
- Hence the closure of a union of connected components of 𝒜 \ 𝒵 is a union of such X.
- Preimages under the finite map q of analytic sets are analytic. ∎

## 3. Theorem 3 (total-merge transport)

**Theorem 3.** Let Q ∈ B_0. Assume:
- (Y) there is a sequence t_n → 0, t_n ≠ 0, such that Q_{t_n} has a Y_{t_n}-copy;
- (TM) for every y ∈ C_0(Q) there is a boundary branch b at Q, with a lift b̃, such that 𝔅·y ⊂ M^+(b̃).

Then for all but finitely many n, the MS6 configuration exists at time t_n. In particular MS6 holds, with T = {t_n : n ≥ n_0} minus a finite set. T accumulates at 0 ∈ Δ.

Hypothesis (Y) holds whenever Q ∈ closure(∂V_0), as shown in the proof.

*Proof.*
1. **Hypothesis (Y) for Q ∈ closure(∂V_0).**
   - Q_t ∈ closure(∂V_t), because H_t commutes with closures and preserves Δ_Γ.
   - Take a branch of ∂V_t at Q_t, and lift it to Def(Q) through a lift Q̃_t. Along it, the vertex-i curve is the constant Y_t ∈ M_{g_i,n_i}.
   - In the chart, the vertex-i curve converges to the curve glued from the components over the contracted vertex. That curve is Y_t, which is smooth, so it is a single component (Lemma D(1) of PR-I; re-checked).
2. **Choice of a limit copy.** Fix lifts Q̃_{t_n} and Y_{t_n}-copies y_n.
   - Pass to a subsequence along which y_n = y is constant and the ordering of special points is fixed.
   - Q̃_{t_n} → 0, and comp_y is continuous. M_{g_i,n_i} is Hausdorff and Y_{t_n} → Y_0 (PR-A). So comp_y(0) ≅ Y_0, i.e. y ∈ C_0(Q).
   - Arguing by contradiction on subsequences, it suffices to show that MS6 holds at t_n for all large n in this subsequence.
3. **Applying (TM).** Take b, b̃ as in (TM) for this y.
   - By Lemma 2(b), at time t_n there is a lift of H_{t_n}(b) through Q̃_{t_n} with pattern a_n S_b̃, lying in a_n Ñ.
   - Pass to a subsequence with a_n = a. Then a^{-1} y ∈ 𝔅y ⊂ M^+(b̃).
4. **Case a^{-1}y ∈ M(S_b̃).** Then y ∈ M(a S_b̃): y is merged along the lift through Q̃_{t_n}. Lemma 1 gives MS6 at t_n. (Q_{t_n} ∉ Δ_{G_b}, because H_t preserves strata.)
5. **Case a^{-1}y intact, with comp_{a^{-1}y} non-constant along b̃.** Then y is intact for a S_b̃, and comp_y is non-constant along a b̃.
   - Let W̃ be any irreducible germ of closure(a Ñ) at (0,0) (Lemma 2(c)). φ := comp_y is holomorphic on W̃, because y is intact for the constant pattern a S_b̃.
   - t is non-constant on W̃, so W̃_0 has pure dimension 1 (Krull). Its components are lifts a′b̃ with a′S_b̃ = a S_b̃, and along each of them φ = comp_{a′^{-1}y} along b̃.
   - a′^{-1}y ∈ 𝔅y is intact for S_b̃, so it is not in M(S_b̃). Hence comp_{a′^{-1}y} is non-constant along b̃. So φ is non-constant on every component of W̃_0.
6. **Generic rank of Φ = (φ, t) on W̃ is 2.**
   - Otherwise every fibre of Φ has dimension ≥ 1 at every point (semicontinuity of fibre dimension).
   - The fibre of Φ through a point of W̃_0 \ {0} lies in W̃_0 ∩ {φ = const}, which is 0-dimensional there. Contradiction.
7. **Only finitely many bad times.**
   - The set Σ := {p ∈ W̃ : dim_p Φ^{-1}Φ(p) ≥ 1} is analytic (Cartan–Remmert, cited from memory). It is a proper subset, so dim Σ ≤ 1.
   - So only finitely many 1-dimensional components of Σ lie in t-fibres, and φ is non-constant on W̃_t for t outside a finite set.
   - There are finitely many germs W̃. So for large n, φ is non-constant along the lift through Q̃_{t_n}, and Lemma 1 (intact case) gives MS6 at t_n. ∎

**Corollary 3′.** If 𝔅 = Aut(Q) fixes every element of C_0(Q), then (TM) reads: every Y_0-copy of Q is merged, or is intact and moving, along some boundary branch at Q. Hence MS6 holds if some Q ∈ closure(∂V_0) with this property exists.

**How Theorem 3 relates to Prop K and to PR-I.**
- Prop K (PR-H) produces a MERGE or MOV branch at a point Q_0 for the *path-marked* copy x_0 only. In general:
  - (G1) Q_0 ∉ closure(∂V_0), so (Y) is not automatic;
  - (G2) other Y_0-copies at Q_0, or 𝔅-translates of x_0, need not be merged (TM fails);
  - (G3) the MOV branch may have Q_0 in its own stratum (MOV-interior), which is excluded from M^+.
- In the quintic example of PR-I (not smooth), at P_0 = A—B—C one has C_0 = {A, C}, branch β (S = {e_1}) with M = {B, C}, and branch β′ (S = {e_2}) with M = {A, B}.
  - If Aut(P_0) does not swap A and C, (TM) holds and Theorem 3 applies.
  - If it does swap them, (TM) fails, and one needs PR-I's Krull-at-time-t argument (Lemma D) instead.
- So Theorem 3 does not supersede PR-I's Theorem 4. It is a different sufficient condition.

## 4. Lemma 4 (spreading of Y_t-copies at a time t where MS6 fails)

Call a coarse piece D (an irreducible 1-dimensional component of closure(V_t) ∩ Δ_G) **MOV-blocked at P** if P ∈ D and no vertex of a lift of D that is constant along D takes a value at P isomorphic to Y_t.

**Lemma 4.** Fix t, and suppose there is NO MS6 configuration at time t. Let P ∈ B_t have a Y_t-copy, and let D be a coarse piece with P ∈ closure(D). Assume that either
- (a) P ∉ D, or
- (b) P ∈ D and D is not MOV-blocked at P.

Then some lift-piece E of D has a vertex u with f_u ≡ const ≅ Y_t, and every point of closure(D) has a Y_t-copy.

*Proof.*
1. **Case (a).** Lift a branch of D at P to Def(P) through a lift P̃ carrying a Y_t-copy y. This is possible by the argument of Lemma 2(b) at fixed t.
   - Since MS6 fails at t, Lemma 1 says that y is intact for the branch pattern, and that comp_y is constant along the branch.
   - So the vertex u = {y} of the lift-piece E containing the branch has f_u constant on a branch, hence on E by the identity theorem on Ē. Its value is comp_y(P̃) ≅ Y_t.
2. **Case (b).** The vertex given by the hypothesis is constant along D with value ≅ Y_t.
3. **Every point of closure(D) has a Y_t-copy.**
   - ξ_G(E) = D, since ξ_G(E) ⊂ D, both are irreducible, and ξ_G(E) contains a branch of D.
   - Every R ∈ closure(D) is ξ̄_G(ν(r)) for some r ∈ Ē, and the u-coordinate of ν(r) is the smooth curve Y_t ∈ M_u.
   - So R has a component ≅ Y_t, carrying the same special points as in the proof of Lemma 1. ∎

**Corollary 4′.** Let B_t^∂ be the connected component of B_t containing ∂V_t. Note B_t^∂ = H_t(B_0^∂). Suppose MS6 fails at t and no coarse piece in B_t^∂ is MOV-blocked at a point of B_t^∂. Then:
- every point of B_t^∂ has a Y_t-copy;
- every coarse piece in B_t^∂ has a lift with a vertex that is constant and ≅ Y_t.

*Proof.*
1. B_t^∂ is a finite union of closures of coarse pieces. A compact analytic set of dimension ≤ 1 has 1-dimensional irreducible components, each the closure of the piece of its generic stratum, together with isolated points. The component containing the 1-dimensional set ∂V_t is a union of the former, and their incidence graph (two pieces adjacent if their closures meet) is connected.
2. Start from the pieces of ∂V_t, whose vertex i is ≡ Y_t, and apply Lemma 4 along the incidence graph. ∎

**What Lemma 4 shows.** If MS6 fails, the Y_t-copies are never "lost" at a puncture. They can be lost only at MOV-blocked incidences, i.e. MOV-interior configurations. They can also be carried by a component different from the one at t = 0 (twins). Lemma 4 is purely a time-t statement and uses neither total geodesy nor L2.





### Lemmas T, S, J and Theorem R (verbatim)
# round9_q7 — answer (MS8)

**Status: PARTIAL.** I do not prove MS8 in full and I do not give a counterexample. What I do:
- I prove three structural lemmas (T, S, J) from (R1), (R2) and (Rig).
- From them I get a reduction (Theorem R): MS8 holds unless the Prop K track meets one of two explicitly described configurations, (R-tw) "twin switch" and (R-cr) "interior MOV crossing".
- Both residual configurations stay OPEN. Inside the reduction they are the precise forms of the chain's "residual twins" and "residual crossings".

New compared with the round-8 material:
- **Lemma T.** H transports each piece into a single irreducible component of the boundary total space, both globally and locally at a point. The proof uses a non-separation argument from dimension theory. Before this, transport through crossings was not controlled.
- **Lemma S.** Under (Rig), a component of the boundary total space has the same non-constant vertex set M and the same curve K on *every* fibre, including t = 0.
- **Consequence.** A "crossing" can occur only at a twin switch or at the final branch of the track. It cannot occur in the middle of an aligned track.

Readings: (R1), (R2) as in the task, with H_0 = id. (Rig) as in MS8. Throughout, F denotes the finite set of pointed curves (with all orderings of special points) that occur as a smooth component of some coordinate of some point of K ∩ ∂(∏_{u∈M} M̄_u), for (G,M,K) ∈ 𝒦. It is finite because 𝒦 is finite and each K is an irreducible curve not contained in the boundary.

**Pinning principle (P).** If Y_t ∈ F for all t in a nonempty open set U ⊂ Δ, then Y ≡ Y_0.

*Proof.* Y is continuous and takes values in a finite set on a connected open subset of U, so it is constant there. By holomorphy (PR-A) and the identity theorem, which applies in an orbifold chart, Y is constant on Δ. ∎

## 1. Notation

- ℬ := closure(𝒱) ∩ (∂M̄_g × Δ). By (R1) it is analytic. By (R2) it is homeomorphic over Δ to B_0 × Δ, hence of pure dimension 2.
- Every irreducible component of ℬ dominates Δ, since fibres are 1-dimensional. So by Krull every fibre of every component is pure 1-dimensional.
- For a stratum Δ_G put ℬ_G := ℬ ∩ (Δ_G × Δ). This is an analytic subset of Δ_G × Δ.
- A *component of ℬ_G* means an irreducible component of ℬ_G. It has dimension 2, because H maps (B_0 ∩ Δ_G) × Δ onto it and B_0 ∩ Δ_G is 1-dimensional or empty.
- A *piece* at time 0 is an irreducible component E of B_0 ∩ Δ_G.

## 2. Lemma T (transport respects components)

**Lemma T.** Let E be a piece at time 0 in Δ_G.
(a) There is a unique component κ(E) of ℬ_G with H(E × Δ) ⊂ κ(E).
(b) Every component 𝒲 of ℬ_G satisfies 𝒲 = ∪_{κ(E)=𝒲} H(E × Δ). In particular 𝒲_0 = ∪_{κ(E)=𝒲} E, and a piece E lies in 𝒲_0 iff κ(E) = 𝒲.
(c) (Local version.) Let Q ∈ B_0 and let β be a branch at Q of a piece E. Let ℬ^{(1)}, …, ℬ^{(m)} be the local irreducible components at (Q,0) of the germ of ℬ_{G_β} ∪ {deeper strata}, i.e. of ℬ. For a small closed sub-branch β′ ∋ Q and a small disc D ∋ 0, H(β′ × D) lies in exactly one ℬ^{(k(β))}. Hence (H_t(Q), t) ∈ ℬ^{(k(β))} for t ∈ D. Moreover ℬ^{(k(β))} is a local component at (Q,0) of closure(κ(E)).

*Proof.*
1. Let E° be E minus the singular points of the analytic set B_0 ∩ Δ_G. This removes finitely many points of E. E° is a connected real 2-manifold, because E is irreducible and its regular locus minus a finite set is connected. So E° × Δ is a connected real 4-manifold.
2. Let Σ := Sing(ℬ_G). This includes all pairwise intersections of components. It is analytic of complex dimension ≤ 1, so its covering dimension is ≤ 2.
3. H^{-1}(Σ) ∩ (E° × Δ) is closed in E° × Δ and homeomorphic to a subset of Σ, so its dimension is ≤ 2 = 4 − 2.
4. Cited from memory (Hurewicz–Wallman, *Dimension Theory*, Thm IV 4): a closed subset of dimension ≤ n − 2 does not separate a connected n-manifold. So R := (E° × Δ) \ H^{-1}(Σ) is connected.
5. H(R) is a connected subset of Reg(ℬ_G). Each connected component of Reg(ℬ_G) lies in exactly one irreducible component. So H(R) lies in one component 𝒲 = κ(E).
6. R is dense in E × Δ, since a closed set of dimension ≤ 2 has empty interior in a 4-manifold, and E° is dense in E. Taking closures in Δ_G × Δ gives H(E × Δ) ⊂ 𝒲, because 𝒲 is closed there. Uniqueness: H(R) is not contained in Σ. This proves (a).
7. For (b), let x ∈ 𝒲 lie on no other component. By (R2), x = H(e,t) with e in some piece E′ of B_0 ∩ Δ_G. By (a), H(E′ × Δ) ⊂ κ(E′), and x is on no other component, so κ(E′) = 𝒲. So 𝒲 \ (other components) ⊂ ∪_{κ(E′)=𝒲} H(E′ × Δ).
8. The right-hand side is closed in Δ_G × Δ: it is a locally finite union of images of the relatively closed sets E′ × Δ under the homeomorphism H. The left-hand side is dense in 𝒲. This gives (b). If E ⊂ 𝒲_0 = ∪_{κ(E′)=𝒲} E′, then E = E′ for one of them, by irreducibility.
9. (c) is the same argument. Replace E° × Δ by β°′ × D, where β°′ = β′ \ {Q} is a punctured disc. Replace Σ by the singular locus of the germ union the pairwise intersections of the ℬ^{(k)}. Continuity of H at (Q,0) keeps H(β′ × D) inside a representative neighbourhood. Then (H_t(Q),t) ∈ closure(H(β°′ × {t})) ⊂ ℬ^{(k(β))}. The last claim holds because H(β′ × D) ⊂ κ(E). ∎

**Remark.** Lemma T is exactly what is needed to transport "which sheet" a branch lies on, using only the coarse homeomorphism H. It does not give vertex labels: H says nothing about the action of Aut(Q). That is where twins enter.

## 3. Lemma S (structure of components under (Rig))

Let 𝒲 be a component of ℬ_G. Let 𝒲̃ be an irreducible component of its preimage in ∏_{w∈V(G)} M_w × Δ; this is a finite map, and the preimage is permuted by Aut(G). Write f_u for the coordinate maps.

**Lemma S.**
(a) There are a set M = M(𝒲) ⊂ V(G) and an irreducible curve K = K(𝒲) with (G,M,K) ∈ 𝒦 such that:
- for every t, every 1-dimensional irreducible component E of 𝒲̃_t has M(E) = M and K(E) = K;
- t = 0 is included.
(b) For u ∉ M, the map (f_u, t): 𝒲̃ → M_u × Δ has 1-dimensional image 𝒞_u. So f_u is constant on each connected component of each fibre 𝒲̃_t, taking finitely many values c_u(t) that vary in t as a multivalued holomorphic function.
(c) Let x ∉ M. Suppose f_x ≅ Y_t (as pointed curves, some ordering) on a subset of 𝒲̃ of real dimension 4. Then it holds on all of 𝒲̃.

*Proof.*
1. Let M be the set of u such that f_u is non-constant on the components of the generic fibre. For u ∉ M, the image of (f_u,t) is 1-dimensional: its fibres over t are finite for generic t, and it is irreducible. So the image is a curve finite over Δ near generic points. Its closure meets each {t} in a discrete set, for every t, because the image is an irreducible curve that is not a vertical line. A vertical line would need f_u to be non-constant on fibre components. So f_u takes finitely many locally constant values on 𝒲̃_t for every t. This is (b).
2. By (Rig), for generic t the pieces of 𝒲̃_t carry curves from the finite set 𝒦. So by irreducibility and continuity one K works for all generic t, and 𝒲̃ maps into K × ∏_{u∉M} M_u × Δ (a closed condition), for all t.
3. Let E be any 1-dimensional component of a fibre, including t = 0. By (b), the vertices u ∉ M are constant on E. Since E is 1-dimensional, its image in K is not a point, hence it is dense in K. Each u ∈ M has non-constant projection on K, by the definition of M. So M(E) = M and K(E) = K. This is (a).
4. (c): {p ∈ 𝒲̃ : f_x(p) ≅ Y_{t(p)}} is analytic, since Y is holomorphic. An analytic subset of an irreducible 2-dimensional space that has real dimension 4 is the whole space. ∎

**Definition (persistent).** Call 𝒲 *persistent* if its generic points have a Y_t-copy. Equivalently, by S(c) and the Lemma D(1) argument, some vertex x ∉ M(𝒲) has f_x ≡ Y_t on 𝒲̃. Such an x is a *persistent vertex*.
- Every component κ(E), with E a component of ∂V_0, is persistent with persistent vertex i: H_t(E) ⊂ ∂V_t, and vertex i of ∂V_t is Y_t.
- Locally at a point (Q,0) with Q ∈ Δ_{G_Q}: let 𝒲̃^a be a germ component of the preimage of closure(𝒲) in Def(Q) × Δ. If 𝒲 is persistent, there is a vertex y_a of G_Q such that all edges at y_a are identically 0 on 𝒲̃^a and z_{y_a} ≅ Y_t on 𝒲̃^a.
  - Proof: limits of smooth Y_t-copies at nearby points are smooth, so as in Lemma D(1) the copy comes from a single intact vertex. Finitely many vertices cover the irreducible germ, so one vertex works everywhere on it.

## 4. Lemma J (junction trichotomy)

**Setting.**
- Q ∈ B_0 lies in Δ_{G_Q}.
- β is a branch at Q of a piece E. Let 𝒲̃^a be a germ component at (0,0) ∈ Def(Q) × Δ of the preimage of ℬ^{(k(β))}, containing a lift β̃ of β. Assume 𝒲̃^a has persistent vertex x.
- b is another branch at Q, of a piece E″ in stratum Δ_{G″}. Let 𝒲̃″ be a germ component of the preimage of ℬ^{(k(b))} containing a lift b̃ of b.
- U_b := the edges of G_Q that are not identically 0 on b̃. Then G″ = G_Q / U_b.
- Write [y] for the vertex of G″ containing y.

**Lemma J.** There are g′ ∈ Aut(Q) and a nonempty open set U ⊂ Δ \ {0} near 0 such that, with x̂ := g′^{-1}x, exactly one of the following holds.
- **(J1) pinned:** Y_t ∈ F for t ∈ U. Hence Y ≡ Y_0 by (P). This happens whenever, along b̃ (equivalently, generically on 𝒲̃″), x̂ is merged, i.e. [x̂] ≠ {x̂}. It also happens whenever [x̂] = {x̂} ∈ M(κ(E″)) and U_b ≠ ∅ (puncture-move).
- **(J2) persistent:** [x̂] = {x̂} ∉ M(κ(E″)). Then x̂ is a persistent vertex of 𝒲̃″, so κ(E″) is persistent.
- **(J3) crossing:** U_b = ∅, so b lies in the stratum of Q and Q is an interior point of E″, and x̂ ∈ M(κ(E″)).

*Proof.*
1. **Finding g′ and U.** Put Q_t := H_t(Q). By Lemma T(c), (Q_t,t) ∈ ℬ^{(k(β))} ∩ ℬ^{(k(b))} for t ∈ D. The preimage of ℬ^{(k(β))} is ∪_g g𝒲̃^a, because Aut(Q) permutes the preimage components of an irreducible germ transitively, and similarly for ℬ^{(k(b))}.
   - For g, h ∈ Aut(Q), let T_{g,h} := {t ∈ D* : some lift of Q_t lies in g𝒲̃^a ∩ h𝒲̃″}. These are finitely many sets covering D*.
   - Each is closed in D*: lifts of Q_t stay in a compact neighbourhood of 0, since the preimage of Q is {0}.
   - By Baire, some T_{g,h} has interior. Put g′ := g^{-1}h. Then for t in an open set U there is q_t ∈ 𝒲̃^a ∩ g′𝒲̃″ over (Q_t,t).
   - Shrink U to avoid the discrete set of t over which some germ component has a fibre component inside a deeper stratum. Then for t ∈ U, q_t is a limit of points of the fibre at t of g′𝒲̃″ that lie in the generic stratum Δ_{G″} (relabelled by g′).
2. **At q_t.** Since q_t ∈ 𝒲̃^a, vertex x is intact at q_t and z_x(q_t) ≅ Y_t. On g′𝒲̃″ the role of x is played by the vertex x̂ = g′^{-1}x of 𝒲̃″. So in what follows, "x on g′𝒲̃″" is "x̂ on 𝒲̃″".
3. **Merged.** Suppose [x̂] ≠ {x̂}.
   - (i) [x̂] ∈ M″. If not, the [x̂]-coordinate is constant, equal to c, a smooth curve, on fibre components at t. Its limit at q_t is the curve assembled from the components in [x̂]. That curve contains an edge at x̂, which is pinched at q_t because x is intact there, so it is nodal and differs from c. Contradiction.
   - (ii) So the limit at q_t of the M″-coordinates is a point of K(κ(E″)) whose [x̂]-coordinate is nodal. That is a point of K ∩ ∂, and z_x(q_t) ≅ Y_t is a smooth component of it. Hence Y_t ∈ F. This is (J1).
4. **Puncture-move.** Suppose [x̂] = {x̂} ∈ M″ and U_b ≠ ∅. Some edge e ∈ U_b lies inside some vertex group [w] of G″. As in step 3(i), [w] ∈ M″. So the limit point of K at q_t lies in K ∩ ∂, and its x̂-coordinate is z_x(q_t) ≅ Y_t. Hence Y_t ∈ F. This is (J1).
5. **Constant.** Suppose [x̂] = {x̂} ∉ M″. By Lemma S(b), z_x is constant on the fibre components of g′𝒲̃″ through q_t, and q_t lies in the closure of their generic part. So the constant is z_x(q_t) ≅ Y_t, for every t ∈ U. The union of these fibre components over t ∈ U has real dimension 4. By S(c), applied to the germ and then to the global irreducible component, x̂ is persistent on 𝒲̃″ and κ(E″) is persistent. This is (J2).
6. **The remaining case** is [x̂] = {x̂} ∈ M″ with U_b = ∅, which is (J3).
7. **Generic behaviour equals behaviour along b̃.** The generic points of b̃ and of 𝒲̃″ lie in the same stratum Δ_{G″}, because E″ ⊂ κ(E″)_0 ∩ Δ_{G″}. So U_b is the set of edges not identically 0 on 𝒲̃″. By Lemma S(a), the piece E″ has M(E″) = M(κ(E″)). So "x̂ merged / moving / constant along b at t = 0" coincides with the generic behaviour on 𝒲̃″. ∎

**Corollary J′ (aligned junctions).** In Lemma J, suppose x̂ = x, i.e. g′ fixes the vertex x. Suppose also that x is intact and constant along b at t = 0, as happens in the middle of a Prop K track. Then (J2) holds with persistent vertex x on 𝒲̃″ ⊃ b̃.
- (J3) cannot occur: x constant along b implies x ∉ M(κ(E″)), by Lemma J step 7.
- (J1) cannot occur either: under the hypothesis x is neither merged nor moving along b.

So **in an aligned track, crossings never occur in the middle**. They can occur only at a non-aligned junction (g′x ≠ x) or at the terminal branch.

## 5. Theorem R (reduction of MS8)

**Input from Prop K (PR-H §3), used as stated there, "modulo routine marking details".**
- There is a compact connected K_0 ⊂ B_0 containing a generic point P of ∂V_0, and a point Q_0 ∈ K_0 with a terminal branch b_* of type MERGE or MOV.
- The labeled Σ_i-vertex x is intact and ≅ Y_0 along K_0, consistently with the path marking.
- A closed connected subset of the finite topological graph B_0 is path-connected through finitely many vertices. So there is an embedded arc in K_0 from P to Q_0, passing through finitely many junction points Q_1, …, Q_r. At each Q_k the arc arrives along a branch β_k and leaves along a branch b_k. Lifts β̃_k, b̃_k carry the *same* labeled track vertex x; this is the marking consistency.
- Inside a piece the persistent vertex does not change. By Lemma S(c) it is a global property of the lifted component κ(E) with the labeling of E.

**Definitions.**
- A junction (including the terminal point Q_0 with b = b_*) is *aligned* if, in Lemma J applied with x the track vertex, some admissible g′ fixes x.
- Otherwise it is *non-aligned*. Then g′x ≠ x for every admissible g′, so x and x̂ = g′^{-1}x are two distinct components of Q exchanged by an automorphism of Q. These are twins in the sense of PR-I.

**Theorem R.** Assume (R1), (R2), (Rig) and the conclusion of Prop K. Suppose every junction Q_1, …, Q_r is aligned, Q_0 is aligned, and the terminal branch b_* is MERGE or MOV with b_* not contained in the stratum of Q_0 (puncture-MOV). Then Y_t = Y_0 for all t.

*Proof.*
1. **Base.** The arc starts in a component of ∂V_0, whose κ is persistent with persistent vertex i = x (§3).
2. **Induction.** Inside a piece the persistent vertex is unchanged. At an aligned junction Q_k, Corollary J′ either pins Y (and we are done by (P)) or makes x persistent on the germ containing b̃_k, hence on κ of the next piece.
3. **Terminal point.** At Q_0, alignment gives x̂ = x.
   - If b_* is MERGE for x, then x is merged along b_*, which is case (J1) step 3.
   - If b_* is puncture-MOV, then x ∈ M with U_b ≠ ∅, which is case (J1) step 4.
   - Either way Y_t ∈ F for t in an open set, and (P) gives Y ≡ Y_0. ∎

**What Theorem R does not cover: the residual configurations (OPEN).**
- **(R-tw) Twin switch.** Some junction Q (possibly Q_0) is non-aligned. Then Q has a nontrivial automorphism g′ with g′x ≠ x. Along the outgoing branch, the persistent copy is x̂ = g′^{-1}x, whose value is ≡ Y_t on its component, while the track copy x is not persistent there. Its constant c(t) satisfies c(0) = Y_0 and c ≢ Y_t, or x is merged/moving generically but not at t = 0.
  - Lemma J still gives (J1), (J2) or (J3) for x̂. In case (J2) the network of *persistent* pieces continues, but on a different copy than the track. Prop K says nothing about where x̂ eventually merges or moves.
  - Restarting Prop K from the piece with the copy x̂ (Lemma PA applies to any piece, PR-H Remark) produces a new track that can switch again. I found no well-founded quantity that rules out infinitely many switches or cycles.
- **(R-cr) Interior MOV / crossing.** Either the terminal branch b_* (aligned) lies in the stratum of Q_0 and x moves along it, or a non-aligned junction falls into (J3). Then Y_t ∈ pr_x(K) for a fixed K ∈ 𝒦 and t near 0. This is a curve condition, not a finiteness condition, so no pinning follows. Excluding it would need more: either that a Prop K track can be continued past an interior MOV point, or a further geometric property of totally geodesic V_0. Theorem X (R8-1) covers only crossings inside a common Q-factorial sheet.

**Relation to the chain.**
- Lemma T shows that the coarse homeomorphism H always respects irreducible components, globally and locally. So "crossings" in the sense of H mixing sheets do not occur.
- Lemmas S and J then show that the only crossings that matter are (J3)-crossings, and Corollary J′ shows these occur only at non-aligned junctions or at the terminal branch.
- So the open part of MS8 is exactly (R-tw) together with the terminal (R-cr). This matches the chain's list of "residual twins and residual crossings", in a sharper form.
- I found no flaw in the chain's derivation of the problem's claim from MS8 in the part I used: holomorphy of Y_t (PR-A) and the finiteness of F under (Rig). I did not audit the rest of the chain.

## 6. Summary

**Proved here** (from (R1), (R2), (Rig); dimension-theory and analytic-geometry facts cited from memory as indicated):
- Lemma T: H maps each piece into a unique global, and local, irreducible component.
- Lemma S: M and K are constant on all fibres of each component, including t = 0. Constant vertices vary along a curve 𝒞_u finite over Δ. Persistence of a Y-copy is a property of the whole component.
- Lemma J: the junction trichotomy pinned / persistent / crossing, for the transported vertex x̂ = g′^{-1}x.
- Corollary J′: there are no crossings inside an aligned track.
- Theorem R: MS8 holds whenever the Prop K track is aligned at all its junctions and its terminal branch is a MERGE or a puncture-MOV.

**Not proved: MS8 in full.** The open cases are (R-tw), a non-aligned (twin) junction, and (R-cr), a terminal interior MOV or a (J3) crossing after a twin switch. Theorem R depends on these extra conditions, so by the task's rules it is a partial result, not a proof of MS8.

**No counterexample** was constructed.



### Lemma PT (verbatim)
## 3. Lemma PT: product-type strata carry no twins of positive dimension

**Lemma PT.** Let Δ_G be of product type, Q ∈ Δ_G, and α ∈ Aut(Q). Let x be a vertex of G with dim M_{g_x,n_x} > 0. Then α maps the component Q_x to itself. More generally, the partial-normalization map Π : {s_e = 0 ∀e} ⊂ Def(Q) → ∏_w M_w (comp_y ↦ y-th factor, for a fixed identification G_Q ≅ G) satisfies ξ_G∘Π = q and is independent of the identification; so comp_x = pr_x∘Π on the stratum locus of Def(Q), and comp_x(αp) ≅ comp_x(p) for all α ∈ Aut(Q).

*Proof.*
1. α induces σ ∈ Aut(G), which acts on ∏_w M_w by permuting the factors and relabelling marked points, and ξ_G∘σ = ξ_G on all of ∏_w M_w (gluing does not see the order of the factors).
2. ξ_G is injective (product type), so σ acts as the identity on ∏_w M_w.
3. If σ(x) = x′ ≠ x, then for every z ∈ ∏_w M_w the coordinate z_{x′} would be a fixed relabelling of z_x. Since dim M_x > 0, choose z with z_x arbitrary and z_{x′} different from every relabelling of z_x (possible: the coordinates are independent and M_{x′} ≅ M_x up to relabelling is positive-dimensional). Contradiction. So σ(x) = x.
4. Two identifications G_Q ≅ G differ by some σ ∈ Aut(G); by step 2, Π does not change. By (K3), comp_x(αp) ≅ comp_{α^{-1}x}(p) = comp_x(p). ∎

**Consequences.**
- At a junction J or end point Q_0 of Prop K's chain whose stratum is of product type, (NT) holds for the tracked chart vertex (it has type (g_i,n_i) and dim M_{g_i,n_i} > 0). So no twin jump can occur there (R7-3 Theorem A, R8-8 Theorem 1 with (NT_m)).
- R8-6 type (T) ("same-branch twin") cannot occur at a point of a product-type stratum.
- Hence **every twin problem of the chain lives at points of non-product strata.** (This was used for Δ_Γ in R8-2 Step 4; here it is recorded for all strata.)

---

