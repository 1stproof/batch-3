# Answer to round14_q2 (missing statement (SC))

## 0. Outcome in one paragraph

**(SC) is neither proved nor refuted here.** I found no counterexample to it. In every model class I could check by hand (listed in §2), the chains (SC) asks for exist. I also see no route to (SC) in the generality required (Pesin blocks, fractal leaf sets, at least one extra zero exponent).

I checked that the chain of the brief derives the goal from (SC): the hypotheses of Theorem IC2 are exactly (L1)-(L4), (E) and orbit isolation (§1).

The new material is a different use of GH in the **volume-preserving case**. The chain never uses the closed-range (tame) half of GH. Using it, I prove a quantitative "isoperimetric" inequality for configurations of asymptotic legs (Theorem AC, §3, fully proved). It shows that, in the volume case, **approximate** closing at polynomial precision is already contradictory, so exact closing is not needed.

Consequences:
- The volume case of the problem reduces to a GH-free **quantitative near-homoclinic** statement (QNH-vol), §4. Its qualitative version (unstable leaves accumulate on stable leaves) follows from Ledrappier-Young theory (cited, §5). Only a **rate** is missing.
- I also prove that this mechanism cannot work outside the volume case without information on the invariant distributions (Proposition E, §6).

---

## 1. Check of the chain of the brief

Theorem IC2 (Block R13-a, quoted in the task file) assumes:
- two summable chains (a_i), (b_i) with a_0 = b_0 = x_0, with the same constants (C, θ);
- (L4) with the same η < θ for both chains;
- weak-stable endings d(g_t p_k, g_{t+τ_k} x_0) ≤ C e^{-θt} for t ≥ 0;
- an orbit-isolated vertex in each chain, in exactly the sense of (SC).

(SC) delivers exactly these data: (L1), (L2), (L3) are the summable-chain conditions, then (L4), (E) and orbit isolation. Step 4 of the chain is therefore a verbatim application of IC2.

I re-read the proof of IC2, steps 1-4 (ring C[R], the two endpoint terms, the cancellation (1 - c_2[τ_2])(1 - c_1[τ_1]) - (1 - c_1[τ_1])(1 - c_2[τ_2]) = 0, and the bump at v_1). I found no gap. One point is used implicitly: the weights w_i of an infinite chain must converge, so that S_k - S'_k = δ_{x_0} - w_∞ δ_{p_k} holds in (C^1)'. This follows from (L1)-(L3), since |β| along a leg is ≤ Lip(d)·C·(leg length)/θ, which is summable.

I did not re-verify entry 113 (Block R11-a) or the variational step; they are quoted as checked in the ledger.

**Conclusion: the chain "variational step + entry 113 + (SC) + IC2 ⇒ h_top = 0" is logically sound, modulo the cited blocks.**

---

## 2. (SC): model checks and the shape of a possible counterexample (sketches; GH-free)

In each class below, chains as in (SC) exist. I give only the mechanism; these are checks, not proofs of (SC) for the class.

(i) **Hyperbolic measures.** Katok / Lian-Young give a horseshoe with periodic orbits whose mean divergence is close to μ(d) = 0. A transverse homoclinic point a_1 of a periodic x_0 gives the finite chain x_0 →u a_1 →s a_2 with a_2 ∈ W^s(a_1) ∩ W^s(orbit x_0). Two distinct homoclinic orbits give two chains.

(ii) **Anosov flow × Diophantine translation on T^q.** Strong leaves are W^{ss/uu}_N × {θ}. Chains stay in a fibre, and return to W^{ss}(n_0) exactly:
- by su-accessibility of the Anosov flow (Brin), when it is not a suspension;
- inside the su-leaf, when it is a constant-roof suspension (local product structure in the fibre T^2).

(iii) **Compact group extensions / torus skew products over Anosov maps.** Let Γ be the group of su-loop holonomies. Either Γ is the whole fibre group (accessible), or loops near degenerate ones have holonomy 0 (integrable). In both cases there are non-degenerate loops of zero holonomy: concatenate a loop of holonomy γ with a different loop of holonomy -γ.

(iv) **Herman-type skew products over rotations acting on SL(2,R)/Γ.** su-paths are products of the opposite unipotent groups U(θ), L(θ), which close exactly by (u(1)l(-1))^3 = ±I. Regularity is a property of θ alone, so all vertices are regular.

(v) **Skew products over isometries with 2-dimensional fibres.** Local product structure in the fibre closes su-quadrilaterals exactly.

**What a counterexample would need.**
- The flow may have no horseshoe at all, because of (i).
- Its su-structure must be "acyclic even in the limit" everywhere in M, not only on supp μ. The reason is that x_0 in (SC) is an arbitrary point of M.
- This forces genuinely twisted centre directions together with fractal (Pesin) leaf sets of small conditional dimension. That is the scenario of R7-f §3(a) and R13-a §4.

I could neither build such a flow nor exclude it.

---

## 3. Theorem AC: an isoperimetric inequality for asymptotic legs (volume case; proved)

**Setting (V-GH).**
- X is GH, dim M ≥ 2, and X preserves a smooth probability density ω.
- By (O2): X has no zeros, the flow is uniquely ergodic, and X: C^∞_0 → C^∞_0 is a topological isomorphism. Here C^∞_0 = {ω-mean zero}.
- Write R for its inverse. By Text B, Lemma 2 with k = 1, there are m, C_1 with ||R f||_{C^1} ≤ C_1 ||f||_{C^m} for f ∈ C^∞_0.
- Fix a Riemannian distance d, and put V := max|X| > 0.

**Definitions.**
- A *leg* ℓ = (a, b; H) is a pair of points with H = (-∞,0] (type u) or H = [0,∞) (type s), such that d(g_t a, g_t b) ≤ C_ℓ e^{-θ|t|} for t ∈ H, for some C_ℓ and some θ > 0.
- Its functional is λ_ℓ(φ) := ∫_H (φ(g_t a) - φ(g_t b)) dt for Lipschitz φ. This converges absolutely, with |λ_ℓ(φ)| ≤ Lip(φ) C_ℓ/θ, and λ_ℓ(1) = 0.
- Its boundary is ∂ℓ := δ_a - δ_b (type u) or δ_b - δ_a (type s).
- A *flow segment* σ = (x, τ) has functional λ_σ(φ) := ∫_0^τ φ(g_s x) ds (oriented integral if τ < 0), and boundary ∂σ := δ_{g_τ x} - δ_x.
- A *configuration* is a finite real combination Λ = Σ_k ε_k λ_{ℓ_k} + Σ_j ε'_j λ_{σ_j}. Its boundary is ∂Λ := Σ ε_k ∂ℓ_k + Σ ε'_j ∂σ_j, a finite signed measure of total mass 0. Its *flow length* is τ(Λ) := Λ(1) = Σ ε'_j τ_j.
- Put ||∂Λ||_W := sup{ |∂Λ(u)| : u Lipschitz, Lip(u) ≤ 1 } (the Kantorovich-Wasserstein norm). For example ||δ_p - δ_q||_W = d(p,q).

**Lemma 3.1 (boundary identity; no GH).** For every C^1 function u, Λ(Xu) = ∂Λ(u).

*Proof.* Since (Xu)(g_t a) = (d/dt) u(g_t a), the following hold.
- For a u-leg, ∫_{-∞}^0 (d/dt)[u(g_t a) - u(g_t b)] dt = u(a) - u(b). The limit at -∞ vanishes because d(g_t a, g_t b) → 0 and u is uniformly continuous.
- For an s-leg, the same computation gives lim_{t→∞}[u(g_t a) - u(g_t b)] - (u(a) - u(b)) = u(b) - u(a).
- For a flow segment, ∫_0^τ (Xu)(g_s x) ds = u(g_τ x) - u(x).

Summing with the coefficients gives the identity. ∎

**Theorem AC (proved under (V-GH)).** For every configuration Λ and every smooth φ,

 |Λ(φ) - τ(Λ) ω(φ)| ≤ C_1 ||φ - ω(φ)||_{C^m} · ||∂Λ||_W ≤ 2 C_1 ||φ||_{C^m} ||∂Λ||_W.

*Proof.*
1. Put f := φ - ω(φ) ∈ C^∞_0 and u := R f, which is smooth with Xu = f.
2. Since Λ(1) = τ(Λ), we get Λ(φ) - τ(Λ)ω(φ) = Λ(f).
3. By Lemma 3.1, Λ(f) = Λ(Xu) = ∂Λ(u).
4. |∂Λ(u)| ≤ Lip(u) ||∂Λ||_W, and Lip(u) ≤ ||du||_∞ ≤ ||u||_{C^1} ≤ C_1 ||f||_{C^m}.
5. Finally ||f||_{C^m} ≤ ||φ||_{C^m} + |ω(φ)| ≤ 2||φ||_{C^m}. ∎

So, under GH plus volume, a configuration of asymptotic legs with a small boundary is small as a distribution of order m. Exact closing (∂Λ = 0) is the case treated by Theorem T (R12-a) and Theorem IC. Theorem AC is the quantitative, stable version, and it is the only place in this file where the closed-range half of GH enters.

### 3.1 The bump test: quantitative non-closing

Fix χ ∈ C^∞([0,∞)) with 0 ≤ χ ≤ 1, χ = 1 on [0, 1/4] and χ = 0 on [1, ∞). For a point v and 0 < r ≤ r_* (r_* below half the injectivity radius), put φ_{v,r}(x) := χ(d(x,v)^2/r^2). This function is smooth. There is C_χ, independent of v and r ≤ r_*, with ||φ_{v,r}||_{C^j} ≤ C_χ r^{-j} for j ≤ m. Moreover φ_{v,r} = 1 on B(v, r/2), supp φ_{v,r} ⊂ B(v, r), and ω(φ_{v,r}) ≤ C_ω r^n.

For a configuration Λ and a point v, let:
- c_-(v) be the sum of the coefficients with which the backward half-orbit of v enters Λ: +ε_k if v = a_k of a u-leg, and -ε_k if v = b_k of a u-leg;
- c_+(v) be the same for forward half-orbits (s-legs);
- flow segments starting at v, or along v's orbit, count with their coefficient on the corresponding piece of v's orbit.

Call v *admissible* if v's orbit enters Λ with coefficients of one sign, at least one of them nonzero. Put κ(v) := max(|c_-(v)|, |c_+(v)|) > 0.

Let W(Λ) := Σ_k |ε_k| C_{ℓ_k} and fix T > 0. Say v is **(r, T)-isolated in Λ** if every leg or segment endpoint w that is not on the orbit of v satisfies d(g_t w, v) ≥ r for all |t| ≤ T. (Points on v's own orbit are allowed: they contribute with the sign of v.)

**Corollary AC1 (quantitative non-closing; proved under (V-GH)).** Let Λ be a configuration and v an admissible point that is (r, T)-isolated, with r ≤ r_* and

 T ≥ T(r) := θ^{-1} log( 4 V C_χ W(Λ) / (θ κ(v) r^2) ).

Then

 κ(v) r/(4V) ≤ |τ(Λ)| C_ω r^n + 2 C_1 C_χ r^{-m} ||∂Λ||_W.

In particular, if |τ(Λ)| C_ω r^{n-1} ≤ κ(v)/(8V), then ||∂Λ||_W ≥ c_0 κ(v) r^{m+1}, with c_0 := 1/(16 V C_1 C_χ).

*Proof.* Put φ := φ_{v,r}. Split every leg integral into |t| ≤ T and |t| > T.
1. *Tails.* For a leg with t ∈ H and |t| > T, |φ(g_t a) - φ(g_t b)| ≤ Lip(φ) C_ℓ e^{-θ|t|} ≤ C_χ r^{-1} C_ℓ e^{-θ|t|}. The total tail is at most C_χ r^{-1} W e^{-θT}/θ ≤ κ r/(4V), by the choice of T.
2. *Window.* For |t| ≤ T, φ(g_t w) = 0 for every endpoint w off the orbit of v, by isolation. So inside the window only the orbit of v contributes. Its contributions have the sign of c_±(v), and φ ≥ 0.
3. *Main term.* For |t| ≤ r/(2V) we have d(g_t v, v) ≤ r/2, so φ(g_t v) = 1. Hence the window contribution has absolute value at least κ ∫_0^{r/(2V)} 1 dt ≥ κ r/(2V). (For segments the same bound holds on the covered side.)

So |Λ(φ)| ≥ κ r/(2V) - κ r/(4V) = κ r/(4V). On the other hand, Theorem AC gives

 |Λ(φ)| ≤ |τ(Λ)| ω(φ) + 2C_1 ||φ||_{C^m} ||∂Λ||_W ≤ |τ| C_ω r^n + 2 C_1 C_χ r^{-m} ||∂Λ||_W. ∎

Interpretation: in the volume case, every finite su-configuration (chains, loops, grids, possibly with flow shifts) that closes up to a defect δ (= ||∂Λ||_W) but has a vertex isolated at scale r must satisfy δ ≥ c_0 r^{m+1}. Exact closing (δ = 0) is therefore impossible as soon as some vertex is isolated at some scale with the window T(r). **Approximate closing with δ ≤ c r^{m+1} is equally impossible.** This is exactly what Theorems J, G, IC and IC2 could not use, since their contradiction needs exact class membership (R7-a §4, item 2).

---

## 4. Consequence: the volume case reduces to a GH-free approximate statement

### 4.1 The simplest configuration: a near-homoclinic pair

Let v ∈ M and τ ∈ R. Let a and b be points, not on the orbit of v, such that:
- d(g_t v, g_t a) ≤ C_a e^{-θ|t|} for t ≤ 0 (a lies in the global strong unstable set of v);
- d(g_{t+τ} v, g_t b) ≤ C_b e^{-θ t} for t ≥ 0 (b lies in the global strong stable set of g_τ v).

Put

 Λ := λ^u(v, a) + λ_{(v,τ)} + λ^s(g_τ v, b).

Then:
- ∂Λ = (δ_v - δ_a) + (δ_{g_τ v} - δ_v) + (δ_b - δ_{g_τ v}) = δ_b - δ_a, so ||∂Λ||_W = d(a, b);
- τ(Λ) = τ;
- the orbit of v enters with coefficient +1 on all of R, so c_- = c_+ = 1 and κ = 1;
- the only endpoints off the orbit of v are a and b, and W(Λ) = C_a + C_b.

**Corollary AC2 (proved under (V-GH)).** In this situation, let r ≤ r_* with |τ| C_ω r^{n-1} ≤ 1/(8V). Suppose that d(g_t a, v) ≥ r and d(g_t b, v) ≥ r for all |t| ≤ T(r) := θ^{-1} log(4V C_χ (C_a + C_b)/(θ r^2)). Then d(a, b) ≥ c_0 r^{m+1}.

*Proof.* This is Corollary AC1 for the configuration above. ∎

### 4.2 The reduction

Consider the following GH-free statement.

**(QNH-vol) (quantitative near-homoclinic points).** Let g_t be a C^∞ flow on a compact connected manifold of dimension n ≥ 2. Suppose it preserves a smooth probability density ω and h_ω(g_1) > 0. Then there is θ > 0 such that, for every M_0 ≥ 1 and every c > 0, there exist r ∈ (0, r_*], v, τ, a, b as in 4.1 (with some constants C_a, C_b), satisfying:
- |τ| ≤ (8 V C_ω)^{-1} r^{-(n-1)};
- the isolation condition of Corollary AC2 at scale r;
- d(a, b) < c r^{M_0}.

The constants V, C_ω, C_χ, r_* entering T(r) and the bound on |τ| depend only on X, ω, the metric and χ, not on GH.

**Theorem 4.1 (proved).** Assume (QNH-vol). Then every GH vector field that preserves a smooth positive density generates a flow with zero topological entropy.

*Proof.*
1. If dim M = 1 there is nothing to prove.
2. Under GH plus a smooth invariant volume, the flow is uniquely ergodic with invariant measure ω (O2).
3. So h_top(g_1) > 0 would give h_ω(g_1) > 0, by the variational principle.
4. Apply (QNH-vol) with M_0 := m + 1 and c := c_0, where m and c_0 are the constants of Theorem AC and Corollary AC1. The configuration it provides contradicts Corollary AC2. ∎

**More general form (AC-vol).** Replace "near-homoclinic pair" by "any finite configuration Λ" with an admissible (r, T(r))-isolated point v, |τ(Λ)| C_ω r^{n-1} ≤ κ(v)/(8V), and ||∂Λ||_W < c κ(v) r^{M_0}. Theorem 4.1 holds verbatim with (AC-vol) in place of (QNH-vol).

**Comparison with the earlier targets (volume case).**
- Exact non-degenerate finite configurations ((Q-vol) of R12-a, a closed chain or a chain from x to g_τ x) satisfy ∂Λ = 0. Given in addition a vertex v whose orbit is not approached by the other vertices' orbits faster than e^{-θ|t|/2}, they satisfy (AC-vol) with every M_0.
- Truncations of a summable chain as in (γ) of (IC-vol), closed by one extra stable leg from the limit p to x_0, have ||∂Λ||_W = d(x_N, p) → 0 at a fixed isolation scale. So they also give (AC-vol).
- Hence (AC-vol) is implied by all of the exact targets, and it asks for much less: **no exact closing, only closing up to an error that is polynomially small compared with the isolation scale.**

---

## 5. What is known towards (QNH-vol): qualitative accumulation of unstable on stable leaves (GH-free)

**Lemma 5.1 (proved, modulo the cited theorems).** Let f = g_1. Let μ be f-invariant and f-ergodic, with h_μ(f) > 0, and let π be the Pinsker partition. Then:
- (a) for μ-a.e. x, the global strong unstable set W^u(x) is dense in supp μ_{π(x)};
- (b) for μ-a.e. x, every point of supp μ^s_x lies in supp μ_{π(x)}.

Here μ^s_x is the conditional on a Pesin stable partition ξ^s, and μ_{π(x)} the conditional on π. Consequently, for μ-a.e. v and every b ∈ supp μ^s_v (in particular for μ^s_v-a.e. b ≠ v, by non-atomicity, Lemma 6.0 applied to f^{-1}), we have inf{ d(a, b) : a ∈ W^u(v) } = 0.

*Cited (from memory).*
- [LS] For f C^2 and μ f-ergodic there is a measurable partition ξ subordinate to W^u. It is increasing (ξ refines fξ), satisfies ∨_{n≥0} f^{-n}ξ = point partition, and H(ξ | fξ) = h_μ(f) (Ledrappier-Strelcyn; Ledrappier-Young I).
- [RS] Rokhlin-Sinai: for such a ξ, the tail ∧_{n≥0} f^n ξ is the Pinsker partition π mod 0.
- The same holds for ξ^s and f^{-1}.

*Proof.*
(a) Fix a countable base (U_k).
1. Put B_n := { x : μ^{f^n ξ}_x(U_k) > 0 }. By the restriction formula (R9-a §2, step 2), the conditional of f^{n+1}ξ restricted to f^nξ(x) is proportional to μ^{f^nξ}_x. So B_n ⊂ B_{n+1}. Each B_n is f^nξ-measurable.
2. Let A_k := ∪_n B_n. For every N, A_k = ∪_{n≥N} B_n is f^Nξ-measurable, since f^nξ is coarser than f^Nξ for n ≥ N. So A_k is measurable for the tail ∧_N f^N ξ, which is π by [RS].
3. A.e. x lies in the support of its own conditional μ^ξ_x. Hence U_k ⊂ A_k mod μ.
4. A_k is a union of π-atoms mod μ. So for a.e. atom P with μ_P(U_k) > 0, μ_P(A_k) ≥ μ_P(U_k) > 0, and hence μ_P-a.e. point of P lies in A_k.
5. x ∈ A_k means that some atom f^nξ(x) ⊂ W^u(x) has positive conditional mass in U_k. In particular W^u(x) ∩ U_k ≠ ∅.
6. Intersecting over k: for a.e. x, W^u(x) meets every U_k with μ_{π(x)}(U_k) > 0, i.e. it is dense in supp μ_{π(x)}.

(b) π is coarser than ξ^s (it is the tail of ξ^s for f^{-1}), so μ_{π(x)} = ∫ μ^s_y dμ_{π(x)}(y).
1. For each k, consider the set of x with μ^s_x(U_k) > 0 but μ_{π(x)}(U_k) = 0. Integrating μ^s_x(U_k) over this set atom by atom gives ∫ μ_P(U_k) over atoms with μ_P(U_k) = 0, which is 0.
2. So that set is null, and the claim follows by taking the countable union over k. ∎

**The gap between Lemma 5.1 and (QNH-vol) is exactly a rate.** Take v, b as in the lemma and a_j ∈ W^u(v) with d(a_j, b) → 0. Write a_j = g_{t_j}(a_j^0) with a_j^0 in the local unstable manifold of g_{-t_j} v; then C_{a_j} ≈ e^{χ_max t_j}. The isolation condition of Corollary AC2 at a fixed scale r needs two things:
- (I1) the "wandering" piece g_{[-t_j, 0]} a_j avoids B(v, r);
- (I2) v does not return to B(v, 2r) during |t| ∈ [t_j, t_j + O(θ^{-1} log(1/r))]. After time t_j the point a_j shadows v's orbit, and returns of v are harmless only when the shadowing error is ≤ r^2.

A typical orbit piece of length t meets B(v, r) once t ≳ r^{-(n-1)}. So (I1), (I2) are expected exactly when t_j ≪ r^{-(n-1)}. Since we need d(a_j, b) ≤ c r^{m+1}, (QNH-vol) amounts (heuristically) to:

 **(Rate) For ω-a.e. v, the unstable leaf W^u(v) comes within δ of the stable leaf W^s(v) (away from v) within leaf-time t(δ) = δ^{-o(1)} as δ → 0. Exponential volume growth of leaves suggests t(δ) = O(log 1/δ).**

Lemma 5.1 gives t(δ) < ∞ for every δ, but no rate. In the integrable (product-type) models of §2, t(δ) is bounded (exact homoclinic points exist). In accessible uniformly partially hyperbolic models the expected t(δ) is O(log 1/δ). I could not prove (Rate) for general non-hyperbolic positive-entropy volume-preserving flows: it is a quantitative equidistribution statement for long unstable leaves relative to long stable leaves, and no rates of mixing are available.

**Corollary 5.2 (what GH + volume would force; proved conditionally on h_ω > 0).** Assume (V-GH) and h_ω(g_1) > 0. Then for ω-a.e. v and every b as in Lemma 5.1, every sequence a_j ∈ W^u(v) with d(a_j, b) → 0 has the following property: for each fixed r ≤ r_*, once d(a_j, b) < c_0 r^{m+1}, the isolation condition of Corollary AC2 at scale r fails for (v, a_j, b).

*Proof.* This is Corollary AC2 with τ = 0 and b ∈ W^s_loc(v), applied to the pairs supplied by Lemma 5.1. ∎

In words: under GH plus volume, unstable leaves can approach stable leaves only "slowly", in the sense of (I1)/(I2). Proving that they approach fast would finish the volume case.

---

## 6. Why the approximate mechanism is confined to the volume case (proved)

**Proposition E (GH, no volume assumed).** There are m' and C' such that every configuration Λ (§3) lies within C' ||∂Λ||_W of the space I of invariant distribution densities in (C^{m'})'. Precisely, there is T_Λ ∈ I with

 |Λ(φ) - T_Λ(φ)| ≤ C' ||∂Λ||_W ||φ||_{C^{m'}} for all smooth φ.

*Proof.*
1. ∂Λ is a finite signed measure with ∂Λ(1) = 0, and |∂Λ(u)| ≤ ||u||_{C^1} ||∂Λ||_W. So ||∂Λ||_{(C^1)'} ≤ ||∂Λ||_W.
2. By Lemma B(iii) of R7-d (tame dual solvability, a consequence of GH via closed range), there is S ∈ (C^{m'})' with S(Xu) = ∂Λ(u) for all smooth u, and ||S|| ≤ C' ||∂Λ||_{(C^1)'}.
3. By Lemma 3.1, Λ(Xu) = ∂Λ(u). So T_Λ := Λ - S annihilates X(C^∞), i.e. T_Λ ∈ I. (Λ is a distribution of order ≤ 1, by the leg bounds.) ∎

*Consequence.*
- In the volume case I = R·ω (O2). Then T_Λ = cω, and Proposition E gives Theorem AC again.
- Without a smooth invariant volume, Proposition E combined with the bump test shows only this: an approximately closed configuration with an isolated vertex produces an invariant distribution density T_Λ with T_Λ(φ_{v,r}) ≥ κ r/(4V) - C' C_χ r^{-m'} δ, i.e. an invariant distribution "concentrated near the orbit of v" at scale r. GH is not known to exclude such invariant distributions: dim I ≥ 2 exactly when (V) fails (Proposition B of R8-d).
- So outside the volume case, approximate closing gives nothing, and one is back to the exact (Theorem J-based) statements: (SC) via IC2. This agrees with the table of R8-e §2 ("the closed-range half of GH can enter only in the volume case").

---

## 7. Summary: proved, sketched, open

**Proved here (complete proofs above).**
1. §1: the chain of the brief derives the goal from (SC). IC2's hypotheses are exactly those of (SC).
2. Lemma 3.1 and **Theorem AC** (GH + smooth invariant volume): |Λ(φ) - τ(Λ)ω(φ)| ≤ 2C_1 ||φ||_{C^m} ||∂Λ||_W for every finite configuration of exponentially asymptotic legs and flow segments.
3. **Corollaries AC1 and AC2 (quantitative non-closing):** in the volume case, a configuration with an admissible vertex isolated at scale r (window T(r) ~ θ^{-1} log(W/r^2)) has boundary ≥ c_0 κ r^{m+1}. This applies in particular to near-homoclinic pairs a ∈ W^u(v), b ∈ W^s(g_τ v).
4. **Theorem 4.1:** the volume case of the problem follows from the GH-free statement (QNH-vol), or more generally (AC-vol). Both are implied by the exact closing statements sought earlier ((Q-vol), (IC-vol)(γ), the volume case of (SC)), and require only approximate closing at polynomial precision relative to the isolation scale.
5. **Proposition E:** without a smooth invariant volume, approximately closed configurations are always within C'δ of invariant distributions. So this mechanism needs (V) or control of I.

**Proved modulo cited theorems (Pesin partitions, Ledrappier-Strelcyn, Rokhlin-Sinai; from memory).**
6. Lemma 5.1: for every ergodic positive-entropy μ of g_1, a.e. unstable leaf is dense in the support of its Pinsker atom, and a.e. stable leaf lies in that support. Hence near-homoclinic pairs of arbitrarily good precision exist (no rate).
7. Corollary 5.2: under GH + volume + h > 0, these approaches would be "slow" in the sense of (I1)/(I2).

**Sketched only.**
- The model checks of §2.
- The heuristic that (QNH-vol) is equivalent to the rate statement (Rate) of §5.

**Open (explicitly).**
- **(SC)** itself, in particular centre steering on Pesin blocks (Proposition CP (ii)), for non-hyperbolic positive-entropy measures with ∫J_1 dμ = 0. No proof and no counterexample.
- **(QNH-vol) / (AC-vol), equivalently (heuristically) (Rate):** a sub-polynomial-time (ideally logarithmic-time) approach of unstable leaves to stable leaves for positive-entropy volume-preserving flows. This would settle the volume case of the problem through Theorem AC; Lemma 5.1 gives the qualitative version.
- **(V):** does GH imply a smooth invariant volume? A positive answer combined with (QNH-vol) would settle the problem. Without (V), Proposition E shows that the approximate mechanism must be supplemented by information on the invariant distributions.

=== END OF ANSWER round14_q2 ===
