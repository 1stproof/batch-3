# round12_q10: the twin-free route (attempt)

**Plan/status line.** I did not run the restart scheme of the brief (steps 1–3) as written. I replaced it with a **single twin-free walk**. It uses the Mod-invariant functional 𝔪 of round11_q4 §6 with *unlabelled* comparison to Y_0, and needs no restarts and no label tracking. Results:
- **§2, Theorem TW (proved, modulo the inherited walk inputs listed in §2.0).** Assume the twin-free walk *terminates* (hypothesis (Term) below). Then Y is constant. The proof uses Prop. 3.1 of round11_q4 (ℛ ⊂ 𝒩), Theorem X*_all and Lemma S̃′. It never uses MS11♭, Lemma PT, R(D)-points or any label.
- **§3.3 (proved).** A fixed-ray analysis of (Term). Non-termination along a ray means the ray carries a Y_0-shaped thick subsurface with short boundary at *every* time. The good subsurfaces at one time are pairwise disjoint twins, so a non-terminating ray relays between twins infinitely often or keeps one twin forever. In the second case, for large s, the twin's boundary and a filling set of its curves have vertical measure O(e^{-s}). I explain why Lemma NH (direction choice) cannot force termination by itself: a Jenkins–Strebel-type ray can converge to a boundary point that keeps a Y_0-twin.
- **§4.** The restart graph of the brief: what a cycle means; no monotone quantity found.
- **§3.1–3.2 (main finding).**
  - (Term) ⇒ (MS-ray) ⇒ (MS-R) of round11_q4, so the twin-free route is a special case of Criterion R.
  - For the non-smooth symmetric quintic surface of PR-I, every boundary point has a Y_0-component (sketch, via admissible covers). So (Term) and (MS-R) fail there, and the t = 0 restart graph has cycles, although the claim holds there by TFM.
  - Hence any twin-free or restart argument must use smoothness of V_0, persistence (the deformation), or label-level data such as (TF).
- **Not proved:** (Term) / (MS-R) for smooth V_0, hence not the problem. The open question is isolated as (O-sm) in §5.

Readings: (R1), (R2) with H_0 = id, (Rig), "Y non-constant" for contradiction, and the notation of the brief. 𝔐 := M_{g_i,n_i}/S_{n_i}. All comparisons with Y_0 are made in 𝔐, i.e. unlabelled.

---

## 1. Good subsurfaces and the twin-free stopping time

**Definitions.**
- A *Y-type subsurface* of S_g is a compact essential subsurface Σ ⊂ S_g that is the closure of one component of S_g ∖ μ, for a multicurve μ, such that Σ with its boundary curves pinched to punctures has signature (g_i, n_i).
  - Two boundary curves of Σ may be the same curve of μ, approached from both sides (a loop edge). Then pinching gives two punctures, matching the special-point count of a vertex with a loop.
  - Every vertex y of a stable curve with (g_y, n_y) = (g_i, n_i), in any marking, gives such a subsurface Σ_y.
- For X ∈ T_g and Σ of Y-type with max_{γ⊂∂Σ} Ext_X(γ) < δ_0, let ψ_Σ(X) ∈ M̄_{g_i,n_i} be defined as in PR-H §3: Fenchel–Nielsen coordinates of X inside Σ, with the boundary lengths set to 0. Write [ψ_Σ(X)] for its class in 𝔐̄.
  - ψ_Σ is continuous on augmented Teichmüller space near points where ∂Σ is pinched. There it equals the Σ-side of the stable curve. (Cited in PR-H §3 and round10_q10 §3.)
  - ψ_Σ depends only on the isotopy class of Σ, so (X, Σ) ↦ [ψ_Σ(X)] is Mod_g-equivariant.
- Fix δ < δ_0 and η > 0. For X ∈ M_g, let 𝒮(X) = 𝒮_{δ,η}(X) be the set of Y-type Σ (up to isotopy) with
  max Ext_X(∂Σ) < δ and d([ψ_Σ(X)], [Y_0]) < η.
  Here d is a metric on the coarse space 𝔐̄. 𝒮(X) is defined on M_g because it is Mod-invariant. Elements of 𝒮(X) are called *good*.
- For the generating pairs (X_n, q_n) of PR-H (Lemma PA + Lemma NH(1), at a generic point P of ∂V_0) and the rays γ_n(s) := g_s(X_n, q_n), put
  T_n^{tf} = T_n^{tf}(δ,η) := inf{s ≥ 0 : 𝒮(γ_n(s)) = ∅} ∈ [0, ∞].

**Lemma 1.1 (elementary properties).**
- (a) For fixed n, the set {s : 𝒮(γ_n(s)) ≠ ∅} is open in [0,∞). Hence if T_n^{tf} < ∞, then 𝒮(γ_n(T_n^{tf})) = ∅.
- (b) If δ is small enough (depending on Y_0, η), then at any X the good subsurfaces are pairwise disjoint up to isotopy, or equal. Their number is at most (2g−2)/(2g_i−2+n_i).
- (c) T_n^{tf} → ∞ as n → ∞.

*Proof.*
- (a) Each condition defining "Σ good at γ_n(s)" is open in s: Ext is continuous along the ray, and ψ_Σ is continuous where ∂Σ is short. A union of open sets is open. Its complement in [0,∞) is closed, so it contains its infimum.
- (b) Let Σ ≠ Σ′ be good at X.
  - Curves of Ext < δ (δ below the collar constant) are pairwise disjoint. So ∂Σ ∪ ∂Σ′ is a multicurve.
  - Since d([ψ_Σ], [Y_0]) < η, with η < d([Y_0], ∂𝔐̄)/2 (condition (b0) of round10_q10), the Σ-part is in a fixed compact part of 𝔐. So the non-peripheral curves of Σ have hyperbolic length on X at least some ℓ_1 = ℓ_1(Y_0,η) > 0, once δ is small. This uses continuity of length functions in augmented Teichmüller space (Abikoff), uniformly over the compact η-neighbourhood.
  - Take δ so small that Ext < δ forces hyperbolic length < ℓ_1 (Maskit's comparison). Then no curve of ∂Σ′ is non-peripheral in Σ, and vice versa.
  - So the interiors are either disjoint, or Σ ⊂ Σ′ up to isotopy with peripheral boundary, i.e. Σ = Σ′.
  - The count follows from additivity of the Euler characteristic.
- (c) This is Step 1 of PR-H Prop. K. For s in a compact set, γ_n(s) converges uniformly to points of ∂V_0 (Lemma G′). There, the marked Σ_i has pinched boundary and ψ_{Σ_i} = Y_0, so Σ_i ∈ 𝒮. ∎

**Hypothesis (Term).** There are arbitrarily small admissible (r, δ, η) (in the sense of §2.0 below) for which T_n^{tf}(δ,η) < ∞ for infinitely many n.

Remark. For the *marked* stopping time T_n of PR-H (only Σ = Σ_i is used), finiteness is Lemma NH(2). Since T_n^{tf} ≥ T_n, (Term) is a genuine extra statement. §3 analyses it.

---

## 2. The twin-free walk: (Term) ⇒ Y constant

### 2.0 Inputs (inherited, not re-derived; all are label-free in the form used)
- **(W0)** Step 0 of Prop. K_w (round10_q10 §1). For any s_n ≥ 0, sup_{0≤s≤s_n} dist(γ_n(s), B_0) → 0 as n → ∞. This holds because limit points with bounded s lie in ∂V_0, and with s → ∞ the curve c of Lemma NH(1) is pinched, uniformly in n since its modulus is ≥ m. No stopping rule is used. Hence every limit point of γ_n(s_n) lies in B_0.
- **(W1)** The excursion/travel decomposition of round9_q4 §2.3 / round10_q10 §§2, 4, with repair (R-a)(a′), the canonical lifts (R-b) and the recurrent types (R-d). It uses:
  - a finite special set Sp ⊂ B_0 (junctions, singular points of B_0, punctures, and any further finite set);
  - a radius r (Milnor conditions up- and downstairs, distinct lifted branches meeting only at 0, the balls B(J,3r) disjoint);
  - ρ_n := sup_{s ≤ s_n} dist(γ_n(s), B_0) → 0.

  For a fixed walk n ≥ N, [0, s_n] splits into finitely many excursions (maximal intervals in some B(J,2r), J ∈ Sp, that reach B(J,r)) and travel intervals. On a travel interval the walk is ρ_n-close to K_D for a single piece D, where K_D := closure(D) ∖ ⋃_J B(J, r/2). The first piece D^1 contains P, so D^1 ⊂ ∂V_0. The fixed walk n ≥ N has only recurrent transition and endpoint types.
  - None of this uses a label or the stopping rule. Only Step 2 of K_w uses the stopping rule, and only Step 3 uses the label. Neither is used below.
- **(W2)** Lemma S̃′ (round10_q10 §6.3, re-checked in round11_q9 §1.1), for every transition of recurrent type and for the endpoint. Let γ̃_{n′} be canonical lifts of excursion paths at J whose entry points converge to z̃^1 ∈ β̃ ∖ 0 and whose exit points (or endpoints) converge to z̃^2 ∈ b̃ ∖ 0. Then β̃ and b̃ lie in one irreducible component (sheet) of q^{-1}(closure V_0) ∩ B̃(J,3r). The proof uses only that the path lies on a Teichmüller disc of a generating pair (total geodesy).
- **(W3)** Theorem X*_all (round10_q1 §2, re-checked in round11_q9 §1.3). Let E be a piece in any stratum and J ∈ E, i.e. J lies in the stratum of E. Then a sheet at J containing a lift of a branch of E meets {∏ s_e = 0} near 0 only in that lift.
- **(W4)** round11_q4 Prop. 3.1 (ℛ ⊂ 𝒩): under (R1), (R2), (Rig) and Y non-constant, every piece in ℛ has a constant vertex c with φ_c ≡ Y, in particular with value ≅ Y_0 at t = 0. It uses R8-2 Theorem 1, which is proved under (Rig).
- **(W5)** A constant vertex has a smooth limit (R7-3 §1). Let E be a piece with a constant vertex c whose value is Y_0, and let Q ∈ closure(ξ(E)). Then Q has a component isomorphic, as an n_i-pointed curve, to Y_0.
  - Justification: in a chart at Q, along a lift of a branch of E the vertex c is a single intact label y (round10_q10 §4, entry argument). F_y is continuous on L_y, so F_y(0) = lim F_y = Y_0.
  - Equivalently: the set 𝒴 ⊂ M̄_g of stable curves having a component of class [Y_0] is closed. By continuity of ψ, a limit of such curves keeps a Y-type subsurface with pinched boundary and ψ = [Y_0], which is smooth and therefore a single component.

### 2.1 The network closure 𝒞
Put 𝒞 := ⋃_{E ∈ ℛ} closure(ξ(E)) ⊂ B_0. It is compact, being a finite union of compact sets. It is defined from V_0 alone.

**Lemma 2.1.** If Y is non-constant, every point of 𝒞 has a component of class [Y_0], i.e. 𝒞 ⊂ 𝒴.

*Proof.* Combine (W4) and (W5). ∎

### 2.2 Walks stay in 𝒞 (label-free; Y need not be non-constant)

**Proposition 2.2.** Let s_n ∈ [0,∞) be arbitrary times, and let z^∞ be any limit point of γ_n(s_n) along a subsequence. Then z^∞ ∈ 𝒞. The same holds for every point of the Hausdorff limit of γ_n([0,s_n]).

*Proof.* Fix the data of (W1) for the times s_n, and a walk n ≥ N in the subsequence (all its types are recurrent). Let D^1, …, D^k be the pieces of its travel intervals, in order, and J_1, …, J_{k−1} its genuine transition points.

*Induction: D^m ∈ ℛ.*
- D^1 ⊂ ∂V_0, so D^1 ∈ ℛ.
- Suppose D^m ∈ ℛ. The walk leaves K_{D^m}, makes an excursion at J := J_m ∈ closure(D^m), and travels next on D^{m+1} near a branch β′ at J. Let β be the branch of D^m along which it entered.
- If J is a puncture of D^{m+1} (J ∉ stratum(D^{m+1})), then D^{m+1} ∈ ℛ by the closure rule (PT) of ℛ, because J ∈ closure(ξ(D^m)).
- Otherwise J lies in the stratum of D^{m+1}. By (W2) (recurrent type), lifts β̃ of β and β̃′ of β′ lie in one sheet at 0 ∈ Def(J). By (W3), applied to D^{m+1} at J, that sheet meets the boundary near 0 only in β̃′. So β̃ = β̃′, hence β = β′ and D^{m+1} = D^m ∈ ℛ.
- (No label is involved. The R(D)-points of round10_q3 Gap A are irrelevant here: they matter only for which label is followed.)

*Endpoint.* Let z^∞ = lim γ_{n′}(s_{n′}) along a subsequence of recurrent endpoint type. Endpoint types are finite, so we may fix one.
- *Travel type* (s_{n′} in a travel interval on D^k): γ_{n′}(s_{n′}) is ρ_{n′}-close to K_{D^k}, so z^∞ ∈ K_{D^k} ⊂ 𝒞.
- *Excursion type* at J ∈ closure(D^k): z^∞ ∈ B_0 ∩ closure(B(J,2r)). In the Milnor ball this is the union of the branches at J.
  - If z^∞ = J, then z^∞ ∈ closure(ξ(D^k)) ⊂ 𝒞.
  - Otherwise z^∞ ∈ b ∖ {J} for a branch b of a piece E_b, and the canonical lifts converge to z̃^∞ ∈ b̃ ∖ 0 (round10_q10 §5).
  - If J is a puncture of E_b, then E_b ∈ ℛ by (PT), and z^∞ ∈ ξ(E_b) ⊂ 𝒞.
  - If J lies in the stratum of E_b, then (W2) in endpoint form puts β̃ (the entering lift of D^k) and b̃ in one sheet, and (W3) for E_b gives β̃ = b̃. So E_b = D^k ∈ ℛ and z^∞ ∈ 𝒞.

*Hausdorff limit.* Apply the above to every sequence s′_n ≤ s_n. ∎

### 2.3 Theorem TW

**Theorem TW.** Assume (R1), (R2), (Rig), and the inputs (W0)–(W5). Suppose:
- **(MS-ray)** for some generic P ∈ ∂V_0 and generating pairs (X_n, q_n) as in Lemma PA + Lemma NH(1), there are times s_n ≥ 0 such that some limit point z^∞ of γ_n(s_n) has **no component of class [Y_0]**.

Then Y_t = Y_0 for all t.

(Term) implies (MS-ray): take s_n := T_n^{tf}(δ,η) for the n with T_n^{tf} < ∞. By Lemma 1.1(a), 𝒮(γ_n(s_n)) = ∅. Suppose z^∞ := lim γ_n(s_n) had a vertex y with F_y ≅ Y_0. Then in a chart at z^∞, the subsurface Σ_y has Ext(∂Σ_y) → 0 and [ψ_{Σ_y}] → [Y_0] along γ_n(s_n), by continuity of ψ in augmented Teichmüller space. So Σ_y ∈ 𝒮(γ_n(s_n)) for large n, a contradiction.

*Proof of Theorem TW.* Suppose Y is non-constant. By Proposition 2.2, z^∞ ∈ 𝒞. By Lemma 2.1, z^∞ has a component of class [Y_0]. This contradicts (MS-ray). So Y is constant, and Y_t = Y_0 by PR-A. ∎

**Remarks.**
1. (MS-ray) and (Term) are statements about V_0 and its Teichmüller rays only (t = 0). The deformation enters only through (W4).
2. Proposition 2.2 together with Lemma 2.1 is a **twin-free form of Proposition K**. If Y is non-constant, every point of B_0 reachable as a limit of the rays γ_n (at any times) carries a Y_0-component. No marking is followed, so twins play no role.
3. Compared with the brief's restart scheme: no restart is needed, because 𝒮 already contains every twin. The termination problem of the restart scheme (cycles in the restart graph) becomes exactly the termination problem (Term) of a single twin-free walk.
4. Theorem TW does not use MS11♭, Lemma PT, Lemma J or any persistence-of-label statement. It uses Prop. 3.1, which is about pieces.

---

## 3. What (Term) really is, and why the coarse twin-free route cannot work without smoothness

### 3.1 (Term) ⇒ (MS-ray) ⇒ (MS-R): Theorem TW is a special case of Criterion R

**Proposition 3.1.** The following implications hold. They are label-free, need no deformation, and hold for every closed 2-dimensional totally geodesic V_0, smooth or not, given (W0)–(W3), (W5).
- (Term) ⇒ (MS-ray). Shown in §2.3; that argument uses neither (W4) nor the deformation.
- (MS-ray) ⇒ **(MS-R)**: some piece E ∈ ℛ has no constant vertex of class [Y_0].

*Proof of the second implication.*
- By Proposition 2.2 (which does not use Y), z^∞ ∈ closure(ξ(E)) for some E ∈ ℛ.
- If E had a constant vertex of class [Y_0], then (W5) would give z^∞ a component of class [Y_0], contradicting (MS-ray). ∎

So Theorem TW is Criterion R of round11_q4 (Cor. 3.2) applied to the piece produced by the walk. The twin-free walk is only a device for *finding* a piece of ℛ ∖ 𝒩_0. The route through 𝔪 suggested in round11_q4 §6 can therefore succeed exactly when (MS-R) holds, and the walk has located the witness.

There is also a pure t = 0 sufficient condition for (MS-R):
- **(B𝒴)**: some point of 𝒞 has no component of class [Y_0].

Indeed (B𝒴) ⇒ (MS-R) by (W5). Conversely, (MS-R) gives a piece E ∈ ℛ with no constant [Y_0]-vertex. Its generic points then have a component of class [Y_0] only through a moving vertex, which takes the value [Y_0] at finitely many points. So (MS-R) ⇔ (B𝒴).

### 3.2 The symmetric quintic surface: (MS-R), (MS-ray) and (Term) all fail

Take the surface of PR-I: V_0 ⊂ M_6 is the locus of the cyclic covers y^5 = ∏_{k=1}^{5}(x − x_k), the image of M_{0,5} (it factors through M_{0,5}/S_5). It is totally geodesic and 2-dimensional (covering construction; cited from memory, as in PR-I). It is **not smooth** (PR-I).

The boundary is described by admissible covers over M̄_{0,5} (cited from memory, as in round11_q4 §4.1). Over a boundary point, the cover of a component R of the stable base, with special points carrying monodromies a_1, …, a_k ∈ Z/5 (each ≢ 0, sum ≡ 0), is the totally ramified cyclic cover. Its genus is given by 2g − 2 = 5(k − 2) − k.
- **D_{12}.** The base is R_{12} ∪ R_{345}, and the node carries monodromy 3 on the R_{12} side and 2 on the other.
  - Over R_{12}, with monodromies (1,1,3): a genus-2 curve Y_0 with one special point, the unique preimage of the node.
  - Over R_{345}, with monodromies (1,1,1,2): a genus-4 curve with one special point.
  - Genus check: 2 + 4 = 6. Γ consists of two vertices of genera 2 and 4 joined by one edge. Δ_Γ ≅ M_{2,1} × M_{4,1} is of product type, and dim M_{2,1} = 4 > 0.
  - ∂V_0 (the D_{12}-piece) is constant ≡ Y_0 on the M_{2,1} factor, because R_{12} is rigid.
- **D_{12} ∩ D_{34}.** The base is R_{12} — R_5 — R_{34}, with monodromies (1,1,3), (2,1,2), (3,1,1). The fibre is genus 2 + 2 + 2 = 6, with one node over each base node.
  - Every component is stable, so assumption (A) of round11_q4 §4.1 holds; this is checked here by the genus count.
  - The components over R_{12} and over R_{34} are both ≅ (Y_0, node point), since both have monodromies (1,1,3).
- **Every boundary point.** It lies over some D_{kl}. The component over R_{kl} has monodromies (1,1,3), so it is ≅ (Y_0, point).

**Consequences (sketch status: rests on the cited admissible-cover description).**
- **B_0 ⊂ 𝒴.** Every point of B_0 has a component of class [Y_0].
- **(B𝒴), (MS-R), (MS-ray) and (Term) all fail.** In fact T_n^{tf}(δ,η) = ∞ for all large n and all admissible (δ,η). Otherwise §2.3 would produce a point of B_0 with no [Y_0]-component.
- **Every pair (piece, constant [Y_0]-vertex) has a restart.** The D_{kl}-piece has its R_{kl}-copy constant. Its marked walk ends at some Q = D_{kl} ∩ D_{mn}, where the R_{kl}-copy merges along the D_{mn}-branch while the R_{mn}-copy is intact and constant along it.
  - So at t = 0 every node of the brief's restart graph has an outgoing edge.
  - The graph is finite, so **it contains a cycle**. By the S_5-symmetry, cycles appear among the pieces D_{kl}.
- **The problem's conclusion does hold for this V_0 under (Rig).** This is TFM (round11_q4 Theorem 3.3 and §4.1): (TF) holds because each twin merges along *every* lift of the other branch.
  - So this V_0 is not a counterexample. It shows that the coarse, twin-free criteria are **strictly weaker** than the label-level criterion (TF).

**Corollary 3.2 (limits of the twin-free coarse route).** No argument that uses only:
- total geodesy of V_0;
- the coarse network data (pieces, ℛ, constant vertices and their classes);
- Teichmüller rays in V_0;

and *not* smoothness of V_0, can prove (MS-R) or (Term) for all V_0 as in the problem. Likewise, no such argument can prove acyclicity of the t = 0 restart graph. The quintic surface (modulo the cited admissible-cover description) satisfies all those inputs and violates the conclusions.

Hence a successful twin-free argument must use one of:
- **(i)** smoothness of V_0, for example to exclude B_0 ⊂ 𝒴 or ℛ ⊂ 𝒩_0;
- **(ii)** the non-constancy of Y in a way that goes beyond Prop. 3.1. For instance, the restart edges must be required to carry a *persistent* twin (φ ≡ Y), which at t = 0 is invisible;
- **(iii)** label-level data at t = 0, as in (TF).

This answers the brief's step 3 negatively in the form stated there: "show directly that the graph of restarts cannot contain a cycle" is false for the t = 0 restart graph without smoothness.

### 3.3 Fixed-ray analysis of non-termination (proved, but it does not close the gap)

For completeness, here is what non-termination means along one ray. It shows that Lemma NH-type direction choices cannot force (Term) by themselves.

**Lemma 3.3.** Fix n and suppose T_n^{tf} = ∞. Then:
- (a) For every s there is a good Σ_s. At each s the good subsurfaces are pairwise disjoint twins (Lemma 1.1(b)), and at most (2g−2)/(2g_i−2+n_i) of them exist.
- (b) There are constants C (depending on Y_0, η, δ) and, for each good Σ_s, a set Φ_s of curves filling Σ_s and containing ∂Σ_s, such that every γ ∈ Φ_s has vertical measure v(γ) := i(γ, F_hor(q_n)) ≤ C e^{-s}.
- (c) Let h_n > 0 be the minimal height of the horizontal cylinders of q_n. For e^{-s}C < h_n, no curve of Φ_s crosses a horizontal cylinder of q_n. So Σ_s is isotopic into the complement of the open horizontal cylinders, with cores allowed as peripheral curves. That complement is the union of the closures of the minimal components and of the horizontal critical graph.

*Proof.*
- (a) is Lemma 1.1.
- (b) Choose Φ_s as ∂Σ_s together with the images of a fixed finite filling set of Y_0-curves under a marking realising d([ψ_{Σ_s}], [Y_0]) < η.
  - Their hyperbolic lengths on γ_n(s) are bounded, by continuity of length functions (Abikoff), uniformly over the compact η-neighbourhood, for δ small. So their Ext is bounded by a constant C′ (Maskit).
  - Ext_{g_sX}(γ) ≥ ℓ_{g_s q}(γ)² ≥ (e^s v(γ))², since the area is 1 and g_s multiplies vertical measure by e^s.
- (c) A q-geodesic that crosses a flat cylinder enters through one boundary and leaves through the other, so its vertical measure is at least the height. The q-geodesic representatives of Φ_s therefore avoid the cylinder interiors except as horizontal cores. ∎

**Why this does not give (Term).** If F_hor(q_n) is completely periodic, Lemma 3.3(c) puts Σ_s into a neighbourhood of the critical graph. The Jenkins–Strebel ray then converges in M̄_g (Masur 1975, cited from memory) to the curve obtained by pinching the cores. Its components are the Strebel surfaces of the complementary regions. Nothing prevents one of them from being ≅ Y_0, and in the quintic surface something of this kind must happen, by §3.2. So even a completely periodic direction does not force termination. Lemma NH(2) works for the *marked* Σ_i only because one curve can be made non-horizontal by the choice of direction. The candidate twins form an n-dependent family that the choice of direction cannot control.

---

## 4. The restart scheme of the brief (steps 1–3)

- **Step 1 (generalising Prop. K_w to a start on any E ∈ ℛ with a constant Y_0-vertex c).**
  - Lemma PA's proof (PR-H Step 1) uses only a local branch of closure(V_0) along E at a generic point. Its Remark says it applies to product-type strata. For non-product strata it applies on the lifted piece in ∏_w M_w, as in Theorem X*_all (round11_q9 §1.3(i)); I accept this as inherited.
  - Lemma NH needs a vertex of E with a boundary curve (an edge at c) and a positive-area vertex j ≠ c. Here j exists because q_c = 0 (c is constant, so a_c = 0).
  - So Steps 0–5 of K_w go through with c in place of i. The base step of the chain (persistence on every sheet) uses product type of Δ_Γ, so in general it must be replaced by "c is persistent on some E-sheet". That is the restart hypothesis.
  - I did not find an obstruction in step 1.
- **Step 2.** This is as in the brief: (NC2) and round11_q1 §4 give the twin c′.
- **Step 3 (termination).** By §3.2, the restart graph built from t = 0 data has cycles for the quintic surface. So acyclicity cannot be proved from t = 0 data plus total geodesy alone. It must use persistence (φ ≡ Y), i.e. the deformation, or smoothness.
  - With persistence imposed, a cycle (E_1, c_1) → … → (E_k, c_k) → (E_1, c_1) is a closed chain of marked walks. Each walk ends with the tracked copy merging or moving while a persistent twin stays.
  - I found no functional that strictly improves around such a cycle. The functional 𝔪 of round11_q4 §6 is identically "good" along non-terminating rays (§3.2–3.3), so it cannot be that quantity.

---

## 5. Summary

**Proved here** (modulo the inherited inputs (W0)–(W5): Prop. K_w Steps 0, 1, 5 with repairs (R-a)–(R-d), Lemma S̃′, Theorem X*_all, round11_q4 Prop. 3.1, R7-3 §1, and the standard facts cited in them):
1. Lemma 1.1: properties of the twin-free stopping time T_n^{tf}. At each time the good subsurfaces are pairwise disjoint twins.
2. **Proposition 2.2 (twin-free Prop. K, label-free).** Every limit point of the rays γ_n, at arbitrary times, lies in the closure 𝒞 of the reachable network ℛ. This holds with no hypothesis on Y and no label tracking. With Lemma 2.1: if Y is non-constant, every such point has a component ≅ Y_0.
3. **Theorem TW.** (Term), or more generally (MS-ray), implies Y_t ≡ Y_0 under (Rig).
4. **Proposition 3.1.** (Term) ⇒ (MS-ray) ⇒ (MS-R) ⇔ (B𝒴). So the twin-free route is a special case of Criterion R.
5. Lemma 3.3: the anatomy of a non-terminating ray.

**Sketched (rests on the admissible-cover description of the boundary, cited from memory):**
6. §3.2: for the (non-smooth) quintic surface of PR-I, B_0 ⊂ 𝒴. Hence (MS-R), (MS-ray) and (Term) fail, T_n^{tf} ≡ ∞, and the t = 0 restart graph has cycles, although the problem's conclusion holds there by TFM.
7. **Corollary 3.2.** Neither the twin-free coarse route nor the brief's acyclicity step can work from total geodesy plus coarse network data alone. Smoothness of V_0, persistence (the deformation), or label-level t = 0 data such as (TF) must enter.

**Not proved:**
- The problem's claim (equivalently MS11♭ under (Rig)).
- (Term), (MS-ray) and (MS-R) for smooth V_0.
- Acyclicity of the persistent restart graph.

**Open questions (precise):**
- **(O-sm)** Let V_0 ⊂ M_g be a **smooth** closed 2-dimensional totally geodesic subvariety with ∂V_0 ⊂ Δ_Γ constant ≡ Y_0 on factor i. Can every point of the reachable closure 𝒞 have a component ≅ Y_0? A negative answer, i.e. (B𝒴), proves the problem under (Rig), by Criterion R (§3.1). A point of B_0 ∖ 𝒞 without such a component would not be enough. The quintic surface shows the answer is "yes" without smoothness, even for all of B_0. So smoothness would have to be used essentially.
- **(O-TF)** The brief's route 4, (MS-TF): does every smooth V_0 satisfy (TF) of round11_q4 Theorem 3.3 at some point? The quintic satisfies (TF) (round11_q4 §4.1), so it is not a counter-instance. I found no V_0 at which (TF) fails everywhere.
- **(O-cyc)** A functional that decreases strictly along restart edges carrying *persistent* twins. By §3.2 it must use the deformation or the smoothness of V_0.
- (Rig) (entry 82) remains open, as before.

=== END OF ANSWER round12_q10 ===

