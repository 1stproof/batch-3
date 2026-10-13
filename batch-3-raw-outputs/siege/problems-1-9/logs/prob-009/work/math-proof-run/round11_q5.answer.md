# round11_q5 — Mechanism D (connectedness of the boundary divisor) for MS11

**Status: NOT PROVED (partial).** Steps 1–4 of the route are proved below, with an extra simplification: edges of types (β) and (γ) are one and the same kind, a "g-edge". The proof of Step 4 does not use the round10 lemmas, except Lemmas I1–I2 for (α)-edges, which I cite from the brief and did not re-check. Step 5 is reduced to a precise group-theoretic condition on a path of g-edges. I could not prove that condition, and I isolate the configuration a failure needs. The connectedness theorem gives no information about labels, and that is exactly where MS11 lives.

Notation and readings (R1), (R2) are as in the brief. Write A := Aut(Q), acting on Def(Q) and on the labels V(G_Q). Note that s_e∘a = (unit)·s_{a(e)}, so N := ∏_e s_e is A-invariant up to a unit and {N=0} is A-invariant.

## 1. The 3-fold X

**Lemma 1.** q^{-1}(cl 𝒱) ∩ (B×Δ_ε) is an analytic set of pure dimension 3. Some irreducible component X of its germ at (0,0) contains S×{0}. X need not be unique.

*Proof.*
- By (R1), cl 𝒱 is analytic, and it is the closure of the 3-manifold 𝒱. Hence it is of pure dimension 3: every irreducible component meets the dense open set 𝒱.
- q×id is finite and open (a quotient by a finite group), so preimages of pure-dimensional sets are pure of the same dimension.
- S×{0} is an irreducible germ contained in the union of the components, so it lies in one of them.
- Non-uniqueness, local model: take A ∋ a with a: z ↦ −z, S ⊂ {z=0}. Suppose the image 3-fold is w = t² in the quotient coordinate w = z². Its preimage is z = ±t: two components, both containing S×{0}.
- So uniqueness can fail exactly when generic curves of V_0 have automorphisms that generic curves of V_t lose. This matches the hint.
- Below, X is any such component; nothing depends on the choice. ∎

## 2. The boundary divisor D := X ∩ {N=0}

**Lemma 2.**
- (a) D has pure dimension 2.
- (b) No component of D lies in {t=0}.
- (c) Let T be a component of D. Then T ∩ {t=0} ∖ {0} is a non-empty union of lifted branches of a single coarse branch c, and T is a transport sheet of each of them.
- (d) D contains a sheet of β̃ and a sheet of b̃.

*Proof.*

(a)
- X ⊄ {N=0}: otherwise X ⊂ q^{-1}(H(B_0×Δ)), which has dimension 2 by (R2).
- N(0,0) = 0.
- O_{X,(0,0)} is a domain because X is irreducible. By Krull's Hauptidealsatz, the germ of X ∩ {N=0} is non-empty and of pure codimension 1.

(b)
- X ∩ {t=0} ∩ {N=0} ⊂ q^{-1}(B_0) ∩ B, which is 1-dimensional.

(c)
- Since t ≢ 0 on T and t(0,0) = 0, the set T_0 := T ∩ {t=0} has pure dimension 1 (Krull again, inside T).
- T_0 ⊂ q^{-1}(B_0) ∩ B, so it is a union of lifted branches.
- Let L := q^{-1}(H({Q}×Δ_ε)) ∩ T be the lift-curve locus. It is an analytic subset of dimension ≤ 1, because q^{-1}(Q_t) is finite for each t. L ∩ {t=0} = {0}, since q^{-1}(Q) ∩ B = {0}.
- T∖L is connected: the complement of a proper analytic subset of an irreducible germ is connected for a good representative.
- T∖L is covered by the sets q^{-1}H((c∖Q)×Δ_ε), c running over the branches of B_0 at Q.
  - These sets are pairwise disjoint, because H_t is injective and the branches meet only at Q.
  - Each is relatively closed in the complement of q^{-1}H(Q×Δ_ε), because the branches are closed and meet only at Q.
- Hence T∖L lies in one of these sets, for a single c, and in one connected component of it.
- That component contains every c̃∖0 ⊂ T_0∖0. So it is Ñ_c̃, for each lifted branch c̃ of c contained in T_0.
- Hence T ⊂ cl Ñ_c̃. T is 2-dimensional and irreducible, and cl Ñ_c̃ is 2-dimensional (it lies in q^{-1}H(c×Δ_ε)). So T is an irreducible component of cl Ñ_c̃, i.e. a transport sheet.

(d)
- β̃×{0} ⊂ S×{0} ⊂ X, and N ≡ 0 on β̃ because β̃ lies over the boundary. So β̃×{0} ⊂ D, and it lies in some component T.
- By (c), T is a sheet of β̃. The same argument applies to b̃. ∎

## 3. Connectedness

**Form used.** Grothendieck's connectedness theorem (SGA 2, Exp. XIII, Thm 2.1 and its corollaries), cited from memory in the following form:

> Let (R, m) be a complete local noetherian domain of dimension n, and let f_1, …, f_r ∈ m with n − r ≥ 2. Then the punctured spectrum Spec(R/(f_1, …, f_r)) ∖ {m} is connected.

Apply it with R := the completion of O_{X,(0,0)}, n = 3, r = 1, f = N.

*Hypotheses.*
- O_{X,(0,0)} is a domain, and analytic local rings are excellent. Hence its completion is a domain: an excellent normalisation is finite, analytic irreducibility is preserved, and analytic local rings are Henselian, so "irreducible germ" agrees with "analytically irreducible".
- So R is a complete local domain of dimension 3, and n − r = 2.

*Translation.*
- Minimal primes of R/N correspond bijectively to the irreducible components of the germ D. This holds again by excellence and Henselianity of O_{D,0}.
- Connectedness of the punctured spectrum is equivalent to the following graph being connected:
  - vertices: the components of D;
  - edges: pairs T, T′ such that T ∩ T′ ⊋ {(0,0)}, i.e. T and T′ share an irreducible curve germ C through (0,0).

  Indeed, a splitting of the vertex set into two groups whose unions meet only in the closed point would disconnect the punctured spectrum.

**Corollary 3.** There is a chain T_β = T^0, T^1, …, T^k = T_b of components of D with:
- T_β a sheet of β̃;
- T_b a sheet of b̃;
- T^{j−1} and T^j sharing a curve germ C_j through (0,0), for each j.

I can only take T_β to be one sheet of β̃ that lies in D. If x is persistent on some other sheet of β̃ that is not in X, the route needs either that sheet to lie in some such X, or MS11's persistent sheet to be chosen inside X. Choose X to contain the given persistent sheet T_x of β̃:
- T_x is a 2-dimensional irreducible germ in q^{-1}(cl 𝒱).
- T_x ⊂ X′ for some component X′ of that germ.
- But X′ need not contain S×{0}: Lemma 2(d) for b̃ needs b̃×{0} ⊂ X′.

**This is a genuine gap (G0).** One needs a single component X containing both T_x and b̃×{0}. It holds if X is unique (Lemma 1), for instance when the generic automorphism group of V_0 persists to V_t.

## 4. Classification of edges

Let C be a curve germ through (0,0) in T ∩ T′, with T ≠ T′ components of D. Exactly one of the following holds:
- (α) C is a lift-curve, i.e. q(C) ⊂ H(Q×Δ_ε);
- (β) C ⊂ {t=0};
- (γ) neither.

**Lemma 4.** In cases (β) and (γ), T and T′ are sheets of lifts of the same coarse branch c. There is also g ∈ A fixing C pointwise with T′ = gT.

*Proof.*
- A generic point (p,t) of C lies in q^{-1}H((c∖Q)×Δ_ε) for some branch c. In case (β), with t = 0, this is p ∈ c̃∖0. By Lemma 2(c), T and T′ are both sheets of lifts of c.
- Near y := q(p), the set M := H((c∖Q)×Δ_ε) is a topological manifold of real dimension 4.
- q(T) and q(T′) are complex 2-dimensional analytic germs at y contained in M. By invariance of domain, each is a neighbourhood of y in M. Hence q(T) = q(T′) as germs at y.
- q is, near p, the quotient by Stab(p). The preimage of an irreducible germ under a finite quotient consists of Stab(p)-translates of one irreducible germ, so T′ = gT near (p,t) for some g ∈ Stab(p).
- gT and T′ are irreducible germs at (0,0) that agree on an open set, so they are equal.
- Take p generic on C. The stabiliser is constant on a dense open subset of C, so g fixes C pointwise. ∎

So the (β) and (γ) edges of the route are both **g-edges**:
- T′ = gT with g ∈ Fix_A(C);
- persistence transforms as P(T′) = g·P(T), since F_{gy}(gp) ≅ F_y(p).

For (α)-edges I rely on round10_q7 Lemmas I1–I2 as quoted in the brief: P(T) = Λ(C) = P(T′) for boundary-type sheets. I did not re-verify these lemmas.

**Completeness.** The trichotomy is exhaustive, and it covers interior-type sheets too: Lemma 4 never used the boundary type.

One more point needs care. For an interior-type sheet (pattern = all of E(G_Q)), "x persistent" requires every edge at x to stay pinched, which is automatic. So only the condition F_x ≅ Y_t carries information there, and the (α) rule of I1–I2 is not available. **An (α)-edge with an interior-type endpoint is therefore a second gap (G1)** for this route, unless it can be avoided.

## 5. Label bookkeeping: reduction and the failure configuration

Suppose that along the chain of Corollary 3:
- the (α)-edges avoid interior-type sheets, or (G1) is closed;
- (G0) holds.

Then, with g_j := id at (α)-edges, the label y := g_k ⋯ g_1 x is persistent on T_b.

**Proposition 5 (reduction).** MS11 holds as soon as some chain satisfies y ∈ Stab_A(b̃)·x, where Stab_A(b̃) is the setwise stabiliser.

*Proof.* Take h ∈ Stab_A(b̃) with h y = x.
- h(b̃∖0) = b̃∖0, so h Ñ_b̃ = Ñ_b̃ (connected component containing the same set).
- Hence hT_b is a sheet of b̃.
- x = hy is persistent on hT_b. ∎

**What a failure needs.** Every chain from a sheet of β̃ to a sheet of b̃ in the edge graph of D must have composite label y ∉ Stab(b̃)·x. In particular:
- (F-a) some g-edge with g·y_j ≠ y_j. At the generic points of its curve C_j, the fibre curve then carries two distinct Y_t-copies y_j ≠ g y_j, swapped by an automorphism g that fixes C_j pointwise.
  - For a (β)-edge, C_j = c̃ is a boundary branch of S at t = 0. Every curve of c has two Y_0-copies exchanged by g. Lemma TG (round9_q5, quoted in the brief) says Fix(g) ∩ S is S, a Teichmüller disc, or c̃. None of these three alternatives gives a contradiction by itself.
  - For a (γ)-edge, C_j lies at t ≠ 0, generically interior to a branch of B_t. The curves there have twin Y_t-copies exchanged by g. Total geodesy says nothing at t ≠ 0, so the constraint would have to come from Theorem X*_all / (R8-2), which I have not verified for this purpose.
- (F-b) no cancellation along the chain: the composite is not in Stab(b̃)·Stab(x).

This is the twin-copy configuration already known from the quintic example (PR-I). That example has twin copies A, C of Y_0 at the cusp, exchanged by an automorphism, but its surface is not smooth. Step 5 cannot be closed by connectedness alone. Connectedness only yields "some label y with F_y ≅ Y_t is persistent on some sheet of b̃". That is a label-free statement, and it is compatible with x being MERGE or MOV along b̃ while a twin y is intact with F_y ≡ Y_0.

**A label-free corollary (proved, modulo (G0), (G1) and I1–I2).** Some label y ∈ A·x is Y-persistent on some transport sheet of b̃. Consequently, by Lemma B1(a) as quoted:
- y is intact along b̃ at t = 0;
- F_y ≡ Y_0 there.

So at the endpoint Q_0 of the walk chain, a contradiction with MERGE or MOV of x follows whenever x is the only label in its A-orbit that can be intact along b̃ with F ≡ Y_0, e.g. when A·x ∩ Stab(b̃)-orbits is a single orbit. In general, MS11 reduces to the following.

## Open (named)
- **(G0)** Some component X of q^{-1}(cl 𝒱) contains both a persistent sheet of β̃ and b̃×{0}. This is automatic if the component X of Lemma 1 is unique.
- **(G1)** Persistence across (α)-edges at interior-type sheets.
- **(L5)** Label condition: for some chain, y ∈ Stab(b̃)·x. Equivalently, rule out twin Y_t-copies swapped by a g fixing an edge curve pointwise (F-a/F-b). I did not prove this. Total geodesy at (β)-edges (Lemma TG) does not decide it by itself.

**Verdict on MS11: not proved. Open.**

=== END OF ANSWER round11_q5 ===
