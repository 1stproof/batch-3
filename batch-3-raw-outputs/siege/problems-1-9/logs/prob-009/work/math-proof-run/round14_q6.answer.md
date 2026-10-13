# round14_q6 — attempt on (NRT_P) / the detaching mirror

**Plan/status line.** (NRT_P) is **not proved and not refuted** here. Option 3 (partial): I prove two new local-but-coarse lemmas and derive partial forms of (M1) and (M3):
- §1 **Lemma N** (stratum coincidence + equivariance): case II of round13_q6 Prop. D forces m_e ≥ k for **every** edge e ∈ E_c, and (k/gcd(k,ℓ_e)) | m_e, where m_e = ord_{c̃}(s_e|_S) and ℓ_e is the length of the h-orbit of e. This is strictly stronger than "k | M". Partial (M1): case II is impossible whenever some e ∈ E_c has m_e < k (e.g. S transverse to some {s_e = 0} along c̃), or h^{ℓ_e} acts non-trivially on the smoothing parameter of some node e ∈ E_c.
- §2 **Lemma C** (the coarse boundary of V_t is locally irreducible at generic points, because of H): at a generic point p_0 of c̃, the irreducible components of the boundary germ at (p_0,0) form **one Stab_G(p_0)-orbit**. No (Sm) needed.
- §3 **Corollary C1/C2** (partial (M3)): in case I, every anchored sheet of c̃ is pointwise fixed by a Stab_G(p_0)-conjugate of h. So a moved branch is gD with g^{-1}hg ∉ Stab(D), and a case-I failure through a needs a non-central in Stab_G(p_0). In particular a case-I failure is impossible when a is central in Stab_G(p_0).
- §4 (M2) and the global question: what the homological route needs, and why it is not available in general. Status at end.

Readings: (R1), (R2) with H_0 = id, coarse reading (H_t need not preserve automorphism groups); notation of the task file (G := Aut(Q), Def(Q) ⊃ B, q, s_e, labels, anchored sheets, lift-curves). (R2^orb) is not used. Standard facts are cited from memory and named where used.

---

## 1. Lemma N: case II needs m_e ≥ k for every pinched edge

**Setting** (as in round13_q6 §2). h ∈ G with h(S) = S, h|_S ≠ id, h fixing the lifted boundary branch c̃ ⊂ S pointwise, and h(X) = X for a 3-fold component X ⊃ S × {0}. p_0 ∈ c̃ ∖ {0} is generic. E_c is the set of edges with s_e ≡ 0 on c̃, and N_c := ∏_{e∈E_c} s_e. k ≥ 2 is the order of h|_S. Hypothesis (Sm) holds at (p_0,0). Lemma LN gives coordinates (z,σ,t) on X near (p_0,0) with S = {t = 0}, c̃ × {0} = {σ = t = 0}, h(z,σ,t) = (z, ζσ, t), ζ a primitive k-th root of 1, and D = Fix(h) ∩ X = {σ = 0}.

For e ∈ E_c put m_e := ord_{c̃}(s_e|_S) ≥ 1, so M = Σ_e m_e. Let ℓ_e ≥ 1 be the least integer with h^{ℓ_e}e = e (the length of the h-orbit of e in E_c).

**Lemma N.** Assume (Sm) at (p_0,0) and **case II** (σ ∤ W in Prop. D). Then for every e ∈ E_c:
- (N1) m_e ≥ k; more precisely, for generic (z,t) with t ≠ 0 the σ-roots of s_e|_X near (p_0,0) form a non-empty set Σ_{z,t} ⊂ C*, the same for all e ∈ E_c, which is a union of free ⟨ζ⟩-orbits, and m_e ≥ |Σ_{z,t}| ≥ k;
- (N2) (k / gcd(k, ℓ_e)) divides m_e;
- (N3) equivalently to (N2): h^{ℓ_e} acts trivially on the smoothing parameter of the node e of the curve at p_0 (its eigenvalue there is ζ^{ℓ_e m_e}).

Contrapositive (partial (M1)): **if some e ∈ E_c has m_e < k, or k/gcd(k,ℓ_e) ∤ m_e, then case I holds.** In particular case I holds if S is transverse along c̃ to some boundary divisor {s_e = 0} (m_e = 1). Since M = Σ m_e = Σ_{orbits} ℓ_e m_e and (N2) gives k | ℓ_e m_e, Lemma N implies Prop. D's criterion "k ∤ M ⇒ case I".

*Proof.*
1. *Weierstrass form of each s_e.* On S, s_e|_S = (unit)·σ^{m_e}, so s_e|_X is σ-regular of order m_e at (p_0,0). Weierstrass preparation (cited from memory) gives s_e|_X = U_e · W_e, with U_e a unit and W_e a Weierstrass polynomial of degree m_e in σ, W_e(σ; z, 0) = σ^{m_e}. The product W := ∏_e W_e is the Weierstrass polynomial of N_c|_X (uniqueness in the preparation theorem), as in Lemma LN.
2. *Stratum coincidence.* By Lemma B0 of round13_q6 (proved there from (R2): near q(p_0) the boundary of closure(V_t) is H_t(c ∩ U′) ⊂ Δ_{G_c}, and H preserves strata), every irreducible component of X ∩ {N_c = 0} near (p_0,0) lies in {s_e = 0} for **every** e ∈ E_c. Since {s_e = 0} ∩ X ⊂ {N_c = 0} ∩ X trivially, we get, near (p_0,0),
   {s_e = 0} ∩ X = {N_c = 0} ∩ X =: Z for every e ∈ E_c.
   Fix (z,t) near (z_0, 0). The zeros of s_e on the slice {(z,σ,t) : |σ| small} are the roots of W_e(·; z,t), all of which are small. So the root set Σ_{z,t} of W_e(·; z,t) equals the σ-slice of Z, and **does not depend on e**.
3. *ζ-invariance.* Every g ∈ G maps {s_e = 0} onto {s_{ge} = 0} (G permutes the boundary divisors of Def(Q) according to its action on edges). So h permutes the divisors {s_e = 0}, e ∈ E_c, and preserves Z = their common intersection with the h-invariant X. In the coordinates of LN, h fixes (z,t) and multiplies σ by ζ. Hence ζ·Σ_{z,t} = Σ_{z,t}.
4. *Case II: 0 ∉ Σ_{z,t} generically.* σ ∤ W means W(0; z, t) ≢ 0, so W_e(0; z,t) ≢ 0 for every e. For (z,t) outside the proper analytic set {∏_e W_e(0;z,t) = 0}, 0 is not a root. Also Σ_{z,t} ≠ ∅, since W_e is monic of degree m_e ≥ 1. So Σ_{z,t} is a non-empty ⟨ζ⟩-invariant subset of C*. The group ⟨ζ⟩ of order k acts freely on C*, so |Σ_{z,t}| is a positive multiple of k. Every element of Σ_{z,t} is a root of W_e, so m_e = deg W_e ≥ |Σ_{z,t}| ≥ k. This is (N1).
5. *(N2).* Put ℓ = ℓ_e. Then h^ℓ maps {s_e = 0} onto itself. {s_e = 0} is a smooth reduced hypersurface of Def(Q) (s_e is a coordinate), so s_e ∘ h^ℓ = u · s_e with u a unit near p_0. Restricting to X: W_e(ζ^ℓ σ; z, t) = (unit)·W_e(σ; z,t). Now ζ^{-ℓ m_e} W_e(ζ^ℓ σ) is again a Weierstrass polynomial of degree m_e, so by uniqueness in the preparation theorem W_e(ζ^ℓ σ) = ζ^{ℓ m_e} W_e(σ). Hence the root multiplicity function μ_e of W_e(·; z,t) satisfies μ_e(ζ^{-ℓ}ρ) = μ_e(ρ), i.e. μ_e is constant on the orbits of ⟨ζ^ℓ⟩ in C*. These orbits are free of size k/gcd(k,ℓ). By step 4 (for generic (z,t)) all roots lie in C*, so m_e = Σ_ρ μ_e(ρ) is a multiple of k/gcd(k,ℓ).
6. *(N3).* Evaluate s_e∘h^ℓ = u·s_e on S near c̃: s_e|_S = v·σ^{m_e} (v a unit) gives v(z, ζ^ℓσ)ζ^{ℓ m_e}σ^{m_e} = u·v(z,σ)σ^{m_e}, so u(z,0,0) = ζ^{ℓ m_e}. u(p_0,0) is the eigenvalue of h^ℓ on the normal line of {s_e = 0} at p_0, i.e. on the smoothing parameter of node e. It equals 1 iff (k/gcd(k,ℓ)) | m_e. (Direct proof of "eigenvalue ≠ 1 ⇒ case I": h^ℓ fixes D pointwise, so on D, s_e = s_e∘h^ℓ = u·s_e with u ≈ ζ^{ℓ m_e} ≠ 1 near (p_0,0), hence s_e ≡ 0 on D, so D ⊂ {N_c = 0}: case I.) ∎

**Remarks.**
- The chart models of case II (round13_q6 §3: s_e = s_{e′} = σ² − t², k = 2, m_e = 2, Σ = {±t}; round13_q4 §1) satisfy (N1)–(N3) with equality m_e = k. So Lemma N sharpens the necessary condition but does not exclude case II at chart level. This agrees with Lemma NG.
- The twin configuration with h an involution swapping x and y, with the edges at x and y forming orbits of length 2 and no h-fixed edge in E_c, passes (N2)–(N3) automatically. In that configuration the only constraint from Lemma N is (N1): m_e ≥ 2 for all e ∈ E_c, i.e. **S is tangent to every boundary divisor {s_e = 0}, e ∈ E_c, along c̃**. This is a t = 0 condition. Whether a totally geodesic V_0 can satisfy it at a reflection mirror is the remaining t = 0 form of (M1) (see §4).

---

## 2. Lemma C: boundary branches at a generic point of c̃ form one Stab(p_0)-orbit

This lemma uses (R2) more strongly than Lemma B0. B0 uses only that H preserves strata. Lemma C also uses that H is a **homeomorphism**, so the coarse boundary of V_t near a generic point of c_t is a topological disc, hence locally irreducible.

**Setting.** c is a branch of B_0, P ∈ c a point at which c is a smooth curve and B_0 = c near P (all but finitely many points of c qualify). p_0 ∈ Def(Q) with q(p_0) = P (e.g. p_0 a generic point of a lifted branch c̃). G_{p_0} := Stab_G(p_0). A := closure(𝒱) ∩ (∂M̄_g × Δ). 𝔅 := the germ at (p_0,0) of q^{-1}(A) ⊂ Def(Q) × Δ, where q(p,t) := (q(p),t).

**Lemma C.**
1. The germ (A,(P,0)) is irreducible and of pure dimension 2.
2. The irreducible components of the germ 𝔅 at (p_0,0) form a single G_{p_0}-orbit.
3. Consequently, any two local branches at (p_0,0) of boundary sheets (anchored sheets of lifted branches through p_0, or components of X ∩ {N = 0} for any 3-fold component X) are G_{p_0}-translates of each other.

*Proof.*
1. Choose an open neighbourhood U′ of P in closure(V_0) with B_0 ∩ U′ = c ∩ U′ homeomorphic to a disc. By (R2), H maps B_0 × Δ onto A (H maps (closure V_0 ∩ Δ_G) × Δ onto closure(𝒱) ∩ (Δ_G × Δ) for every stratum, so it maps the boundary onto the boundary), and H is a homeomorphism closure(V_0) × Δ → closure(𝒱) with H_0 = id. So for ε > 0 and U″ ⊂ U′ a smaller disc neighbourhood, Ω(U″,ε) := H((U″ ∩ c) × Δ_ε) is an open neighbourhood of (P,0) in A homeomorphic to an open 4-ball. These sets form a fundamental system of neighbourhoods of (P,0) in A, since H is a homeomorphism.
   - A is a closed analytic set, and near (P,0) it is a topological 4-manifold, so it has pure complex dimension 2 there.
   - Sing(A) ∩ Ω is a closed analytic subset of complex dimension ≤ 1, so it has topological (covering) dimension ≤ 2 = 4 − 2. A closed subset of covering dimension ≤ n − 2 does not separate a connected n-manifold (Hurewicz–Wallman, cited from memory). So Reg(A) ∩ Ω is connected for every Ω = Ω(U″,ε).
   - If the germ (A,(P,0)) had two distinct irreducible components A_1, A_2, then for small Ω every point of A_1 ∩ A_2 is singular. (At a regular point x the germ of A is irreducible, so the 2-dimensional germs of A_1 and A_2 at x would both equal it, and then A_1 = A_2 by the identity principle for irreducible germs.) Hence Reg(A) ∩ Ω would be the disjoint union of the non-empty relatively open sets Reg(A) ∩ Ω ∩ (A_1 ∖ A_2) and Reg(A) ∩ Ω ∩ (A_2 ∖ A_1). That contradicts connectedness. So (A,(P,0)) is irreducible.
2. Near p_0, the map q: Def(Q) → M̄_g is the quotient by G_{p_0} (slice property of finite group actions, cited from memory). So q × id is, near (p_0,0), the quotient of a G_{p_0}-invariant neighbourhood by G_{p_0}, onto a neighbourhood of (P,0). G_{p_0} permutes the irreducible components of 𝔅 = (q×id)^{-1}(A). For an orbit O of components, Y_O := ⋃O is a G_{p_0}-invariant analytic germ. Its image (q×id)(Y_O) is an analytic germ (finite map), and these images, over the finitely many orbits, cover the germ A. By 1, A is irreducible, so (q×id)(Y_O) = A for some O. Since Y_O is G_{p_0}-invariant, (q×id)^{-1}((q×id)(Y_O)) = G_{p_0}·Y_O = Y_O. Hence 𝔅 = (q×id)^{-1}(A) = Y_O, and every component of 𝔅 lies in the single orbit O.
3. Each such local branch is a 2-dimensional irreducible germ contained in 𝔅 (the transport family Ñ_c̃ and every X ∩ {N = 0} lie over A). 𝔅 is pure 2-dimensional, because A is and q is finite. So each branch is a component of 𝔅, and 2 applies. ∎

**Remark.** Lemma C is not "t = 0 only": it uses H_t for t ≠ 0. It is "chart-local" only in the weak sense that it concerns germs at generic points. It does not contradict the case-II models: there the boundary branches T_± = {σ = ±t} are exchanged by h ∈ G_{p_0}, as Lemma C requires.

---

## 3. Consequences in case I (partial (M3))

**Setting.** As in §1: (Sm) at generic points p_0 ∈ c̃ arbitrarily close to 0, h(X) = X, h fixing c̃ pointwise, h|_S ≠ id, and **case I**: D = Fix(h) ∩ X = {σ = 0} ⊂ {N_c = 0}.

**Corollary C1.** In case I:
1. every component of the boundary germ 𝔅 at (p_0,0) is gD for some g ∈ G_{p_0};
2. every anchored sheet T of c̃ is **pointwise fixed** by h_T := g h g^{-1} for some g ∈ G_{p_0} ⊂ G. Equivalently T = gT_D, where T_D is the anchored sheet containing D;
3. on T, F_{h_T z}(p) ≅ F_z(p) for every label z and every (p,t) ∈ T at which z is intact (Lemma E(3) of round13_q6), and h_T fixes every lift-curve contained in T pointwise.

*Proof.*
1. D is a smooth 2-dimensional germ contained in X ∩ {N_c = 0} ⊂ 𝔅, hence a component of the pure 2-dimensional germ 𝔅. Apply Lemma C(2).
2. T ⊃ c̃ × {0} ∋ (p_0,0). Choose a representative of the germ T on a neighbourhood containing (p_0,0), with p_0 generic and close to 0. T ⊂ closure(Ñ_c̃) ⊂ (q×id)^{-1}(A), and T is irreducible of dimension 2, hence pure 2-dimensional at (p_0,0). So its germ there contains a component of 𝔅, i.e. some gD with g ∈ G_{p_0} (by 1).
   - gD is pointwise fixed by h_T = ghg^{-1}. So Fix(h_T) ∩ T is a closed analytic subset of T of dimension 2. T is irreducible of dimension 2, so T ⊂ Fix(h_T).
   - Likewise gT_D ⊃ gD. Both T and gT_D are irreducible 2-dimensional and share the 2-dimensional germ gD, so T = gT_D.
   - Here G_{p_0} ⊂ G = Aut(Q), so g, h_T act on the whole chart.
3. The first part is Lemma E(3). Every point of a lift-curve L ⊂ T is fixed by h_T. ∎

**Corollary C2 (restriction on case-I failures).** Consider a reflection-type failure of (NRT_P) at Q via a ∈ G, with a fixing c̃ pointwise, aS = S, a|_S ≠ id, the lift-curve L contained in an anchored sheet T of c̃ carrying x (x ∈ C_Φ(L), a^{-1}x rigid along L). Assume (Sm) and case I for h := a (so a(X) = X). Then:
1. T = gT_D with g ∈ G_{p_0} and g^{-1} a g ∉ Stab(T_D); in particular **a is not central in G_{p_0} = Stab_G(p_0)**;
2. hence a case-I failure through a is impossible whenever a is central in Stab_G(p_0) for generic p_0 ∈ c̃ near 0 (e.g. when Stab_G(p_0) is abelian). This settles (M3) in that sub-case;
3. in general, the failure (a, L) is carried by g^{-1} to a failure (b, L_D) on the mirror sheet T_D, with b := g^{-1}ag, L_D := g^{-1}L ⊂ T_D, x′ := g^{-1}x. Here T_D is pointwise a-fixed and b ∉ Stab(L_D). So in case I every failure can be moved onto the h-fixed boundary sheet, at the price of replacing the lost element by a G_{p_0}-conjugate that does not fix that sheet.

*Proof.*
1. By Cor. C1, T = gT_D is pointwise fixed by gag^{-1}. A failure needs a ∉ Stab(T). (Cor. E1 of round13_q6, re-checked: if aT = T then aL ⊂ T, and by Lemma 3 of round13_q5, C_Φ(L) = P_Φ(T) = C_Φ(aL) = a·C_Φ(L). So C_Φ(L) is a-invariant and a^{-1}x ∈ C_Φ(L). But a rigid label is not in C_Φ(L), since its value germ is constant and every branch in Φ is non-constant.) Now a ∈ Stab(gT_D) ⟺ g^{-1}ag ∈ Stab(T_D). If a were central in G_{p_0}, then g^{-1}ag = a would fix T_D pointwise, a contradiction.
2. Immediate from 1.
3. By Lemma E, g^{-1} maps T to T_D, L to the lift-curve g^{-1}L ⊂ T_D, and C_Φ(g^{-1}L) = g^{-1}C_Φ(L) ∋ g^{-1}x. The rigid label g^{-1}a^{-1}x = b^{-1}x′ is rigid along g^{-1}L. Finally b ∉ Stab(L_D) ⟺ a ∉ Stab(L), which holds because a failure needs isotropy drop. ∎

**What this does and does not give for (M3).** Cor. D1's moved-branch configuration B_x ≠ D, hB_x ≠ B_x is, by Cor. C1, B_x = gD with g^{-1}hg ∉ Stab(D). So it requires h to be non-central in Stab_G(p_0). Non-central reflections do occur in general: Stab_G(p_0) ⊃ K_S·⟨a⟩, and the K_S-modifications a′ = k a of Lemma R are typical conjugates. So (M3) is **proved only when a is central in Stab_G(p_0)**. In general the failure is transported to the mirror sheet T_D (item 3), where it becomes a failure via a conjugate b of a, on a sheet that a fixes pointwise. I could not exclude that.

**A consequence of Lemma C in case II (recorded, no contradiction).** In case II the boundary branches at (p_0,0) are the G_{p_0}-translates of the branch R_x carrying x. In the coarse coordinate w = σ^k (when G_{p_0} acts on X through ⟨h⟩), c_t near q(p_0) is the single irreducible germ {W_1(w; z,t) = 0} and the mirror is {w = 0}. So the mirror is a parallel copy of c_t inside V_t, exactly as in the models. Lemma C adds nothing more here.

---

## 4. (M2), (M1) and the global question: routes examined

### 4.1 (M2) via homology — conditional only
Suppose 𝒟 is as in round13_q6 Prop. G with 𝒟_0 ⊂ B_0, and write 𝒟_0 = Σ a_j C_j (a_j > 0, C_j ⊂ B_0, c̄ among them with multiplicity 1, since D is smooth and maps generically injectively, modulo the generic stabiliser, onto q(D)). For generic small t, 𝒟_t ∩ ∂M̄_g is finite, because 𝒟 ∩ (∂ × Δ) is a proper analytic subset of the irreducible surface 𝒟. If
- (IT) closure(V_t) carries an intersection pairing on curve classes that is topological, so that it is transported by H_t (e.g. closure(V_0) normal with Q-homology-manifold singularities, so that Mumford's Q-valued pairing is the topological one), and
- (Neg) the intersection matrix (C_j·C_k) of the boundary curves occurring in 𝒟_0 is negative definite,

then (M2) holds: [𝒟_t] = Σ a_j [H_t(C_j)], so (Σ a_j C_j)² = Σ_j a_j 𝒟_t·H_t(C_j) ≥ 0, since 𝒟_t has no common component with B_t. This contradicts (Neg). Neither (IT) nor (Neg) is known. (Neg) is not a general property of boundaries of totally geodesic surfaces either. Boundary curves of the type of ∂V_0 (a constant factor times a moving Teichmüller-curve factor) have log-canonical degree K + B > 0 by adjunction, so no natural nef class vanishes on B_0 as it does for toroidal compactifications of ball or Hilbert modular quotients. So I do not claim it. This is the brief's route; I add only the precise list of what it needs.

### 4.2 (M2) via a maximum principle — fails for want of a global function
𝒟_t is a compact curve in closure(V_t) lying, for small t, in an arbitrarily small neighbourhood of B_0 (properness of 𝒟 → Δ and 𝒟_0 ⊂ B_0). A continuous function on a neighbourhood of 𝒟_0 in M̄_g, psh on the interior and non-constant on 𝒟_t, would give a contradiction: a bounded subharmonic function on the compact normalisation of 𝒟_t, minus finitely many points, is constant. Near generic points of c, u := Σ_{e∈E_c} ℓ_e (hyperbolic lengths) is psh (Wolpert's strict plurisubharmonicity of geodesic-length functions, cited from memory) and non-constant on the mirror. But u is defined only where the set E_c of short curves is locally well defined. Near the punctures of c the monodromy permutes E(G_Q) ⊋ E_c, and a symmetrisation Σ_γ ψ(ℓ_γ) over all short curves needs ψ increasing, convex and eventually constant, which is impossible. So I have no global psh function and the route stops. (Its local content is consistent with the models: on the mirror, −1/log|W_e(0;z,t)| is subharmonic in z, and its maximum is pushed to the ends of c, i.e. to the punctures.)

### 4.3 (M1): what remains after Lemma N
After Lemma N, case II at a mirror (S, h, c̃) of a totally geodesic V_0 requires the following t = 0 property:
- **(M1′)** S is tangent to order ≥ k along c̃ to **every** boundary divisor {s_e = 0}, e ∈ E_c, and h^{ℓ_e} acts trivially on each smoothing parameter s_e at p_0.

In flat terms: if ψ is the monodromy of the coarse loop around c in V_0, then ψ^k acts near c as the multitwist ∏_e D_e^{m_e} (modulo K_S). So (M1′) says every pinched curve is twisted at least once per coarse loop on average (m_e/k ≥ 1). For a cusp of a Teichmüller disc, m_e/k is proportional to the modulus of the cylinder of e, with a scale fixed by the parabolic. I see no bound forcing m_e < k. The models have m_e = k = 2. So I do **not** claim (M1). Lemma N is the sharpest t = 0 criterion I could prove.

---

## 5. Summary: proved / not proved / open

**Proved** (cited standard facts: Weierstrass preparation and its uniqueness, Cartan linearisation via Lemma LN, the slice theorem for finite group actions, Hurewicz–Wallman non-separation, the local-irreducibility criterion via connectedness of the regular locus; round13_q6 Lemmas E, LN, B0 and round13_q5 Lemma 3 used as stated, with the parts used re-checked):
- **Lemma N** (§1): under (Sm), case II forces m_e ≥ k and (k/gcd(k,ℓ_e)) | m_e for every e ∈ E_c. Equivalently, h^{ℓ_e} acts trivially on every smoothing parameter. This strengthens "k ∤ M ⇒ case I". **Partial (M1):** case II is excluded whenever some pinched edge has m_e < k (e.g. S transverse to some {s_e = 0} along c̃) or carries a non-trivial h^{ℓ_e}-eigenvalue.
- **Lemma C** (§2): at a generic point of a boundary branch, the boundary germ of q^{-1}(closure 𝒱) is a single Stab_G(p_0)-orbit of irreducible components. Proof: by (R2) the coarse boundary H((c∩U)×Δ) is a topological 4-ball, hence an irreducible germ.
- **Cor. C1, C2** (§3): in case I every anchored sheet of c̃ is pointwise fixed by a Stab_G(p_0)-conjugate of h. A case-I failure through a needs a non-central in Stab_G(p_0). **Partial (M3):** the moved-branch configuration of Cor. D1 cannot occur when a is central in Stab_G(p_0). In general a case-I failure can be moved onto the h-fixed mirror sheet T_D via a conjugate b = g^{-1}ag.

**Not proved:** (NRT_P); (M1) in general (reduced to (M1′)); (M2) (conditional on (IT) + (Neg), neither known); (M3) for non-central a; the cases without (Sm), the moving-S case, and the (γ°) and endpoint origins (not treated here). No counterexample is given.

**Open questions (named):**
1. (M1′): can a mirror boundary curve of a totally geodesic smooth V_0 have S tangent to order ≥ k to all its boundary divisors, with h acting trivially on all smoothing parameters?
2. (M2) under (IT)+(Neg), or by any global argument (e.g. a continuous function near B_0, psh on the interior and non-constant on 𝒟_t).
3. (M3) for a non-central in Stab_G(p_0): exclude a failure via b = g^{-1}ag on the pointwise-a-fixed mirror sheet T_D.
4. (NRT_P) itself, and (Rig).

Verdict: **not proved** (partial: Lemma N, Lemma C, Cor. C1/C2). (NRT_P): open.

=== END OF ANSWER round14_q6 ===
