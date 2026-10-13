# round9_q3 — answer

## 0. Status summary (read this first)

I did **not** prove the missing statement (EF), and I did not refute it. What this file contains,
all with complete proofs unless explicitly flagged:

0. **Theorem A (Section 7; the main new result).** (EF) on a strip Ω follows from the exclusion of
   an order-k Jordan chain of length 2 at **one single point** c ∈ Ω: if some c ∈ Ω admits no pair
   (A,B) of order-≤k densities with B ≠ 0, B∘(P−c) = 0, A∘(P−c) = B, then every family satisfying
   (i)–(iii) of (EF) on Ω vanishes identically. The proof is Theorem J's moment/Jordan argument run
   on the transport renormalized by e^{−ct}; c = 0 recovers Theorem J, where the Jordan chain is
   killed by (K0) ∧ (K1). This strictly improves Propositions 3.1–3.2 of [R8-b] (which required the
   set of such z to have empty interior) and reduces the whole problem (Corollary 7.1) to the
   pointwise statement (JC): *under GH, in each strip produced by Theorem R there is one point
   c with Re c ≠ 0 carrying no order-1 Jordan chain of P^T.* (JC) remains open; it is the exact
   analogue at c ≠ 0 of (K0) ∧ (K1) at c = 0. Section 7.1 shows the criterion has teeth:
   Proposition 7.3 kills Jordan chains by a growth condition on ‖Γ_t‖_{C^k → C^k}, and
   Corollary 7.4 deduces (with no GH at all) that a volume-preserving field admits **no** nonzero
   holomorphic eigen-family of complex *measures* (order 0) on any strip. The families coming from
   positive entropy have order exactly 1, where the criterion does not apply.
1. **Lemma 1 (spectral band; no GH used).** A localization of the order-k point spectrum of the
   transposed weighted operator inside a vertical band determined by `max_m m(d)` and by the
   exponential growth rate of the derivatives of the flow. Consequence: (EF) is *automatically true*
   for strips lying outside that band, and the band is exactly where the families of Theorem R live
   (so Lemma 1 is a consistency check and a quantitative lower bound on what any proof of (EF) must
   contain, not progress on the open case). A clean by-product that I did not find in the earlier
   rounds: **for a volume-preserving field, every eigen-distribution of order 0 (i.e. a complex
   measure) has purely imaginary eigenvalue** — no GH needed.
2. **Proposition 2 (sharpened target for the core case; proved equivalence).** For strips touching
   the imaginary axis, (EF) is equivalent to the statement (J1-0): *under GH there is no nonzero
   finite-order distribution density S whose weighted transport decays exponentially backwards and
   grows only sub-exponentially forwards.* This is strictly weaker than the planner's (J1) and still
   suffices for the core case (PE0) (λ = μ(d) = 0) of Theorem R.
3. **Lemma 3 (why "divisibility by P" is harmless; proved, no GH).** Any S with backward exponential
   decay at rate θ is geometrically divisible by the transpose of P and of P − w for every w in the
   strip; the only consequence is that S annihilates every φ whose forward P-iterates grow slower
   than θ^n. Since P is a first-order differential operator, these φ are never C^1-dense (they are a
   "low frequency" set), so the geometric divisibility carries no contradiction. This closes off the
   natural "use the geometric Taylor coefficients" idea in the direction opposite to Theorem V of
   [R7-e] and explains precisely why that theorem needed the *inverse* of P.
4. **Section 4: the obstruction, re-derived in the (J1-0) picture.** The one-sided Jordan chain
   produced by the Abel/Patterson means starts at S and not at 0, so (F1)+(F2) cannot be iterated;
   a contradiction would require S itself to be smooth. I verify this in the abstract setting of
   (EF) (no point masses assumed), which shows the obstruction is intrinsic to (EF) and not an
   artefact of the Dirac-mass construction.
5. **Section 5: explicit open questions**, including the precise extra input that would finish the
   chain.

I also record (Section 6) my check of the chain of the brief: steps 1 and 2 are correct as stated;
(EF) is indeed all that is missing.

Conventions throughout are those of the brief: ν is a smooth positive density, d = div_ν X,
J_t(x) = ∫_0^t d(g_s x) ds, P φ = X φ + d φ, Γ_t φ := e^{J_t} (φ ∘ g_t), so that
Γ_t Γ_s = Γ_{t+s}, (d/dt) Γ_t φ = Γ_t (P φ) = P (Γ_t φ). A distribution density is a continuous
linear functional on C^∞(M); it has order ≤ k if it is continuous for ‖·‖_{C^k}. For a distribution
density T, u = T/ν is the generalized function with ⟨u, φν⟩ = T(φ), and T ∘ P = z T is the same as
X u = −z u. Finally
  Σ_k := { z ∈ C : T ∘ P = z T for some nonzero distribution density T of order ≤ k }.

---

## 1. Lemma 1: the spectral band (no GH)

**Transport norms.** For k ≥ 0 let G_k(t) := ‖Γ_t‖_{C^k → C^k} (the operator norm of Γ_t on the
Banach space C^k(M)); it is finite, submultiplicative in t (G_k(t+s) ≤ G_k(t)G_k(s)) and locally
bounded, so the limits
  γ_k^+ := lim_{t → +∞} (1/t) log G_k(t),   γ_k^- := lim_{t → +∞} (1/t) log G_k(−t)
exist in [−∞, ∞) by Fekete's subadditivity lemma, and are finite because G_k(t) ≥ G_0(t) ≥
e^{min_x J_t(x)} > 0.

**Lemma 1.** Let X be any smooth vector field on a compact manifold (GH is **not** used). If
z ∈ Σ_k then
  −γ_k^- ≤ Re z ≤ γ_k^+ .

*Proof.* Let T ≠ 0 of order ≤ k with T ∘ P = zT, and fix φ with T(φ) ≠ 0. Put h(t) := T(Γ_t φ).
Since t ↦ Γ_t φ is C^1 into C^∞ with derivative Γ_t(Pφ) = P(Γ_tφ) (joint smoothness of
(t,x) ↦ e^{J_t(x)}φ(g_t x); this is step 1 of Theorem J), h is C^1 and h'(t) = T(P Γ_t φ) =
z T(Γ_t φ) = z h(t). Hence h(t) = e^{zt} T(φ) and
  e^{Re z · t} |T(φ)| = |T(Γ_t φ)| ≤ ‖T‖_{(C^k)'} G_k(t) ‖φ‖_{C^k}
for every real t. Taking t → +∞ gives Re z ≤ γ_k^+, and t → −∞ gives Re z ≥ −γ_k^-. ∎

**Lemma 1.1 (identification of the band for k = 0, and an upper bound for general k).**
Let D^+ := max_m m(d) and D^- := min_m m(d), the maxima/minima over flow-invariant probabilities
(attained, since m ↦ m(d) is affine and weak*-continuous on a compact convex set). Let
  Λ_k := limsup_{|t| → ∞} (1/|t|) log max_x max_{1 ≤ j ≤ k} ‖D^j g_t(x)‖  (k ≥ 1), Λ_0 := 0.
Then
  (i) γ_0^+ = D^+ and γ_0^- = −D^-; consequently Σ_0 ⊂ { D^- ≤ Re z ≤ D^+ }.
  (ii) γ_k^+ ≤ D^+ + (k² + k) Λ_k and γ_k^- ≤ −D^- + (k² + k) Λ_k.
  (iii) In particular, if X preserves a smooth positive density ω (take ν = ω, d = 0) then
        Σ_0 ⊂ i R: **every eigen-distribution of order 0 has purely imaginary eigenvalue**, and more
        generally Σ_k ⊂ {|Re z| ≤ (k²+k) Λ_k}.

*Proof.* (i) G_0(t) = ‖e^{J_t}‖_∞ = exp(max_x J_t(x)), and the standard fact
limsup_{t→+∞}(1/t) max_x J_t(x) = max_m m(d) ([R4-q7] Prop. 2.1, step 1: the empirical measures of
near-maximizing orbit segments have invariant weak* limits, and conversely Birkhoff gives ≥) yields
γ_0^+ = D^+. Applying this to −X (whose divergence is −d and whose time-t log-Jacobian is J_{−t})
gives γ_0^- = max_m m(−d) = −D^-.

(ii) Write A_t := max(1, max_{1 ≤ j ≤ k} max_x ‖D^j g_t(x)‖), so A_t ≤ C_ε e^{(Λ_k + ε)|t|}. By the
chain rule, for |α| ≤ k, ∂^α(φ∘g_t) is a finite sum of terms (∂^β φ)∘g_t times products of at most
|β| ≤ k derivatives of g_t of orders summing to |α|; hence ‖φ∘g_t‖_{C^k} ≤ C_k ‖φ‖_{C^k} A_t^k.
Next, J_t = ∫_0^t d∘g_s ds, so ‖J_t‖_{C^k} ≤ |t| ‖d‖_{C^k} C_k max_{|s| ≤ |t|} A_s^k, and by the
Faà di Bruno/Leibniz formula ‖e^{J_t}‖_{C^k} ≤ e^{max J_t} C_k (1 + ‖J_t‖_{C^k})^k. Multiplying the
two estimates and using max_x J_t(x) ≤ C_ε + (D^+ + ε)t (t ≥ 0) gives
G_k(t) ≤ C_{k,ε} e^{(D^+ + ε)t} (1 + |t| e^{k(Λ_k+ε)|t|})^k A_t^k ≤ C'_{k,ε} e^{(D^+ + (k²+k)(Λ_k+ε) + ε)t},
whence the bound on γ_k^+. The backward bound is the same statement for −X.

(iii) Immediate from (i), (ii) with d = 0 (so D^± = 0). ∎

**Corollary 1.2 (what Lemma 1 does and does not give for (EF)).**
(a) (EF) holds for every strip Ω with a > γ_1^+ or b < −γ_1^-: there is simply no z ∈ Σ_1 there, so
T_z = 0 for every z (the hypothesis of (EF) that T_z has order ≤ 1 is used here).
(b) The families produced by Theorem R always live inside the band: their strip is
(λ + δ, λ + θ − δ) with λ = μ(d) ≤ D^+ and θ < χ^+_min ≤ Λ_1, so b < D^+ + Λ_1 ≤ γ_1^+ (by
Lemma 1.1(ii) with k = 1, the band is at least [−γ_1^-, D^+ + 2Λ_1]). **So Lemma 1 never applies to
the families coming from positive entropy.** It is a consistency check, plus the following
quantitative statement: any nonzero order-1 EF on a strip with right edge b forces
Λ_1 ≥ (b − D^+)/2, i.e. forces exponential growth of ‖Dg_t‖ when b > D^+. This is the exact
converse of the implication "positive entropy ⇒ Λ_1 > 0 ⇒ eigen-families exist" of Theorem R, and
it shows that any proof of (EF) must in particular contain a proof that GH forbids exponential
derivative growth (with the band interpretation: must push the whole band onto the imaginary axis).

*Proof of (a),(b).* (a) is Lemma 1 with k = 1. For (b): λ = μ(d) ≤ D^+, and θ < χ^+_min, while
χ^+_min ≤ max exponent ≤ Λ_1. ∎

---

## 2. Proposition 2: the sharpened target for strips touching the imaginary axis

For the core case of the chain (λ = μ(d) = 0, the case (PE0)) the strip produced by Theorem R is
(δ, θ − δ) for every small δ > 0, with the *same* family T_z (a Laplace transform of a fixed S);
so the family is holomorphic on Σ(0, θ) = {0 < Re z < θ} with order-1 bounds on closed substrips.
Hence the relevant case of (EF) is a = 0. Proposition 2 replaces it by a statement about a single
distribution, with a forward hypothesis weaker than the one in (J1).

**Statement (J1-0).** Assume GH. There is no nonzero distribution density S for which there exist
k, ε > 0 and C with
  (b−) |S(Γ_t φ)| ≤ C e^{−ε|t|} ‖φ‖_{C^k} for all t ≤ 0 and all φ ∈ C^∞(M);
  (f0) for every η > 0 there is C_η with |S(Γ_t φ)| ≤ C_η e^{η t} ‖φ‖_{C^k} for all t ≥ 0 and all φ.
("backward exponential decay, forward sub-exponential growth".)

**Proposition 2.** For a fixed smooth X on a compact M the following are equivalent.
 (i) For every b > 0 there is no nonzero family (T_z) on Σ(0,b) satisfying (i),(ii),(iii) of (EF)
     (holomorphy, local uniform order-1 bounds, eigen-relation).
 (ii) The statement (J1-0) holds, with "order ≤ k" allowed to be any finite order k.
Moreover (ii) ⟹ (i) already holds with k = 1 in (J1-0), and in (i) the order-1 requirement may be
replaced by order ≤ k throughout.

*Proof.* **(ii) ⟹ (i).** Let (T_z) satisfy (EF)(i)–(iii) on Σ(0,b) and suppose T_{z_0}(φ_0) ≠ 0 for
some z_0, φ_0. Fix a real c ∈ (0, b) with T_{c+iy}(φ_0) ≢ 0 in y (possible: if T_z(φ_0) vanished on
one vertical line it would vanish identically on Σ(0,b) by the identity theorem, contradicting
T_{z_0}(φ_0) ≠ 0; so every line works). For ω ∈ R put ρ_ω(z) := exp((z−c)² + ω(z−c)) and
  S_ω(φ) := (1/2πi) ∫_{Re z = c} ρ_ω(z) T_z(φ) dz.
On the line z = c + iy, |ρ_ω(c+iy)| = e^{−y²} and |T_{c+iy}(φ)| ≤ C_c ‖φ‖_{C^1} by (EF)(ii); so the
integral converges absolutely and S_ω is a distribution density of order ≤ 1 with
‖S_ω‖_{(C^1)'} < ∞. Exactly as in Theorem 2.1(B) of [R8-b] (which I re-checked line by line):
 • transport: by the computation in Lemma 1 above, T_z(Γ_t φ) = e^{zt} T_z(φ), so
   S_ω(Γ_t φ) = (1/2πi)∫_{Re z = c} ρ_ω(z) e^{zt} T_z(φ) dz;
 • contour shift: for 0 < a' < c < b' < b the integrand is holomorphic on a' ≤ Re z ≤ b' and, by
   (EF)(ii) on that closed substrip together with the Gaussian factor
   |ρ_ω(σ+iy)| = e^{(σ−c)² − y² + ω(σ−c)}, it is O(e^{−y²/2}) uniformly for σ ∈ [a',b'] (t fixed).
   Cauchy's theorem lets us move the line to Re z = b' (use for t ≤ 0) or to Re z = a' (use for
   t ≥ 0), giving
   |S_ω(Γ_t φ)| ≤ K_{b'} e^{b' t} ‖φ‖_{C^1} (t ≤ 0),  |S_ω(Γ_t φ)| ≤ K_{a'} e^{a' t} ‖φ‖_{C^1} (t ≥ 0),
   with K_σ := (1/2π) ∫ |ρ_ω(σ+iy)| C_{[a',b']} dy < ∞. The first bound with a fixed b' ∈ (0,b) is
   (b−) with ε = b'; the second, as a' ranges over (0, c), is exactly (f0) (the constants K_{a'}
   are allowed to blow up as a' ↓ 0).
 • nonvanishing: h(y) := T_{c+iy}(φ_0) is continuous, bounded and ≢ 0, and
   S_ω(φ_0) = (1/2π) ∫ e^{−y²} e^{iωy} h(y) dy is the Fourier transform at −ω of the nonzero
   continuous L^1 function e^{−y²}h; by Fourier uniqueness it is ≠ 0 for some ω.
Taking the real or imaginary part of such an S_ω (both satisfy the same bounds, and one of them is
nonzero) contradicts (J1-0) with k = 1.

**(i) ⟹ (ii).** Let S ≠ 0 satisfy (b−) and (f0) with order k and backward rate ε. For each
η ∈ (0, ε) put T_z(φ) := ∫_R e^{−zt} S(Γ_t φ) dt on Σ(η, ε). By (b−),(f0) the integral converges
absolutely and locally uniformly there (the exponents are −(Re z − η)t for t ≥ 0 and
−(ε − Re z)|t| for t ≤ 0), so z ↦ T_z(φ) is holomorphic with
|T_z(φ)| ≤ (C_η/(Re z − η) + C/(ε − Re z)) ‖φ‖_{C^k}. Since F_φ(t) := S(Γ_tφ) is C^1 with
F_φ' = F_{Pφ} and the same bounds hold for Pφ, integration by parts over [−R,R] (boundary terms
→ 0) gives T_z(Pφ) = z T_z(φ). The definition of T_z does not depend on η, so (T_z) is a family on
Σ(0, ε) satisfying (EF)(i)–(iii) with order k. By (i) it vanishes identically; but then, as in step 3
of Theorem 2.1(A) of [R8-b],
  E(z) := ∫_{−∞}^0 e^{−zt}F_φ dt (Re z < ε) and E(z) := −∫_0^∞ e^{−zt}F_φ dt (Re z > 0)
agree on the strip, hence define an entire function which is bounded (by the two one-sided bounds,
split at Re z = ε/2) and tends to 0 along the negative real axis (dominated convergence on t ≤ 0);
so E ≡ 0 by Liouville. Then y ↦ ∫_{−∞}^0 e^{−iyt}F_φ(t)dt ≡ 0, so the L^1 function F_φ·1_{(−∞,0]}
vanishes a.e.; F_φ is continuous, so S(φ) = F_φ(0) = 0 for every φ, i.e. S = 0, a contradiction. ∎

**Remark 2.1.** (J1-0) is weaker than the planner's (J1) (whose forward hypothesis is
|F_φ(t)| ≤ Ce^{at}, a > 0 fixed), because its hypothesis on S is stronger. By Proposition 2 and
Theorem R it is nevertheless enough for the core case: **(J1-0) ⟹ no ergodic measure with
μ(d) = 0 has positive entropy** (take the pair family of Theorem R with λ = 0: its strip is
Σ(0,θ)). For ergodic measures with μ(d) ≠ 0 the strip of Theorem R is
(λ+δ, λ+θ−δ) and does not touch 0, so those cases need the full (EF) (equivalently (J1) for X and
for −X, by Theorem 2.1 of [R8-b]); several of them are already excluded by Prop. 6.1 of [R6-a] and
Proposition N of [R7-c].

---

## 3. Lemma 3: geometric divisibility by P^T is harmless (no GH)

This closes a line that looks promising at first sight: the Taylor coefficients of the backward
Laplace transform give a *geometrically bounded* sequence of "divisors" of S by the transpose of P,
and one might hope to iterate them against the tame estimates. Lemma 3 says exactly what that
iteration yields, and it is not a contradiction.

**Lemma 3.** Let S be a distribution density, k ≥ 0, θ > 0, C with
|S(Γ_t φ)| ≤ C e^{−θ|t|} ‖φ‖_{C^k} for all t ≤ 0 and all smooth φ. Put
  B_j(φ) := ∫_{−∞}^0 ((−t)^j / j!) S(Γ_t φ) dt  (j ≥ 0).
Then:
 (a) B_j is a distribution density of order ≤ k with ‖B_j‖_{(C^k)'} ≤ C θ^{−j−1};
 (b) B_0 ∘ P = S and B_j ∘ P = B_{j−1} (j ≥ 1); hence S = B_{n−1} ∘ P^n for every n ≥ 1 and
     |S(φ)| ≤ C θ^{−n} ‖P^n φ‖_{C^k} for all n ≥ 1 and all smooth φ.
 (c) Consequently S(φ) = 0 for every smooth φ with liminf_n ‖P^n φ‖_{C^k}^{1/n} < θ.
 (d) The same with P − w in place of P, for every complex w with Re w < θ: with
     B_j^w(φ) := ∫_{−∞}^0 e^{−wt}((−t)^j/j!) S(Γ_tφ) dt one gets ‖B_j^w‖ ≤ C (θ − Re w)^{−j−1},
     B_0^w ∘ (P−w) = S, B_j^w ∘ (P−w) = B^w_{j−1}, hence
     |S(φ)| ≤ C (θ − Re w)^{−n} ‖(P−w)^n φ‖_{C^k}.
No hypothesis on X beyond smoothness is used; in particular GH is not used.

*Proof.* (a) |B_j(φ)| ≤ C‖φ‖_{C^k} ∫_0^∞ (t^j/j!) e^{−θt} dt = C θ^{−j−1} ‖φ‖_{C^k}.
(b) F_φ(t) := S(Γ_tφ) is C^1 with F_φ' = F_{Pφ} (as in Lemma 1). For j = 0,
B_0(Pφ) = ∫_{−∞}^0 F_φ'(t)dt = F_φ(0) − lim_{t→−∞}F_φ(t) = S(φ), the limit being 0 by the decay
hypothesis. For j ≥ 1, integrating by parts on [−R, 0],
∫_{−R}^0 ((−t)^j/j!) F_φ'(t)dt = [((−t)^j/j!)F_φ]_{−R}^0 + ∫_{−R}^0 ((−t)^{j−1}/(j−1)!)F_φ dt;
the boundary term at t = 0 vanishes because j ≥ 1, the one at −R tends to 0 by the decay. So
B_j ∘ P = B_{j−1}. Iterating, S = B_0 ∘ P = B_1 ∘ P² = … = B_{n−1} ∘ P^n, and the estimate follows
from (a).
(c) If liminf ‖P^nφ‖^{1/n} = r < θ, pick n_i → ∞ with ‖P^{n_i}φ‖_{C^k} ≤ (r')^{n_i} for some
r < r' < θ; then |S(φ)| ≤ C θ^{−n_i}(r')^{n_i} → 0.
(d) Identical computation; the decay of e^{−wt}F_φ(t) as t → −∞ is e^{(Re w − θ)|t|}. ∎

**Why this is a dead end (and why Theorem V of [R7-e] had to use the inverse of P).**
P is a first-order differential operator, so ‖P^nφ‖_{C^k} typically grows factorially in n; the set
Q_θ := {φ : liminf ‖P^nφ‖_{C^k}^{1/n} < θ} is a "low-frequency" set, never C^1-dense. Example: on
T^1 with X = ∂_x, ν = Lebesgue (d = 0, P = X), for φ = e^{imx} one has ‖P^nφ‖_{C^k} ≍ |m|^{n+k},
so liminf ‖P^nφ‖^{1/n} = |m|, and Q_θ is contained in the span of the modes with |m| < θ, plus
limits — a finite-dimensional-type set, certainly not dense. Thus Lemma 3(c) is consistent with
S ≠ 0 and gives no contradiction. To contradict S ≠ 0 one needs the opposite divisibility, i.e.
estimates of the form |S(φ)| ≤ C r^{−n} ‖R^n φ‖ with R a (tame) *inverse* of P, since then the
smoothing of R can beat r^{−n}. By Proposition A of [R8-d] a tame inverse of P exists only in the
volume case (V), and in that case Theorem V of [R7-e] shows precisely what is still missing
(quasi-analytic growth of ‖R^Nφ‖_{C^1} on a C^1-dense set). Lemma 3 shows that nothing is gained by
re-running the argument in the "forward" direction, for any choice of the base point w in the strip.

---

## 4. The obstruction in the abstract (EF) setting

Earlier rounds located the obstruction using the concrete S = δ_x − e^b δ_y (chain starting at S,
[R8-c] §3). The following shows it is intrinsic to (EF): the Abel/Patterson means of an *abstract*
family produce a Jordan chain whose inhomogeneous term is a distribution of the same (generally
non-smooth) nature as S, so (F1)+(F2) cannot be bootstrapped.

**Proposition 4.1 (proved).** Let (T_z) be a family on Σ(0,b) as in (EF) (holomorphy, order-1
bounds on closed substrips, T_z ∘ P = z T_z), let S be one of the distributions S_ω produced from it
in the proof of Proposition 2 (so S ≠ 0 for a suitable ω, S has order ≤ 1, S satisfies (b−) with
rate ε = b' and (f0)), and for s > 0 put
  W_s(φ) := s ∫_0^∞ e^{−st} S(Γ_t φ) dt.
Then:
 (a) W_s is a distribution density of order ≤ 1, well defined for every s > 0 by (f0), and
     W_s ∘ P = s W_s − s S.
 (b) If ‖W_{s_n}‖_{(C^1)'} is bounded for some sequence s_n ↓ 0, then every weak* limit W of
     (W_{s_n}) satisfies W ∘ P = 0, hence (under GH, by (F1)) W = c ν for a constant c.
 (c) If in addition ‖(W_{s_n} − cν)/s_n‖_{(C^1)'} is bounded, then every weak* limit V of that
     sequence satisfies V ∘ P = c ν − S, i.e. the generalized function v = V/ν solves
     X v = (S − cν)/ν.
 (d) Under GH, (c) forces (S − cν)/ν to be smooth. Hence: **if the family (EF) is nonzero and the
     two normalizations in (b),(c) are bounded, then S agrees with cν plus a smooth density.**
     Conversely, for the families of Theorem R, S is (a Gaussian average of Laplace transforms of)
     a difference of two Dirac masses and is *not* of that form, so the boundedness assumptions in
     (b) or (c) must fail — which is exactly the Patterson blow-up of [R8-c], Cor. 2.3.

*Proof.* (a) Convergence: by (f0) with η = s/2, |S(Γ_tφ)| ≤ C_{s/2} e^{st/2}‖φ‖_{C^1}, so the
integral converges absolutely; the order bound is immediate. For the relation, use F_φ' = F_{Pφ}
and integrate by parts on [0,R]:
s∫_0^R e^{−st}F_{Pφ} dt = s[e^{−st}F_φ]_0^R + s² ∫_0^R e^{−st}F_φ dt; the boundary term at R tends
to 0 (again by (f0) with η = s/2), and at 0 it equals −sF_φ(0) = −sS(φ). This gives
W_s(Pφ) = −sS(φ) + sW_s(φ).
(b) Along a subsequence with bounded (C^1)'-norms, Banach–Alaoglu (or Banach–Steinhaus plus the
separability of C^1(M)) gives a weak* limit W in (C^1)'; passing to the limit in (a),
W(Pφ) = 0·W(φ) − 0·S(φ) = 0. By (F1) (which is GH through L1), W = cν.
(c) ν ∘ P = 0 because ∫ Pφ dν = ∫ L_X(φν) = 0. So, with V_s := (W_s − cν)/s,
V_s ∘ P = (1/s) W_s ∘ P = W_s − S = cν − S + s V_s. Taking weak* limits along a subsequence where
‖V_{s_n}‖ is bounded, and using s_n V_{s_n} → 0 in (C^1)' (norms bounded, s_n → 0), gives
V ∘ P = cν − S.
(d) X v = (S − cν)/ν with the convention ⟨Xv, φν⟩ = −V(Pφ); if the right-hand side is smooth, GH
makes v smooth, which is a statement about S, not a contradiction — hence the assertion as stated.
For the concrete families: S = S_ω is a Gaussian-weighted contour average of
T_z = Laplace transform of t ↦ δ_x(Γ_t·) − e^bδ_y(Γ_t ·); by the computation in Theorem 2.1(B) it is
a (complex) measure-plus-order-1 object concentrated on the single orbit closure of {x,y} and in
particular it is not of the form cν + (smooth density) unless it vanishes (such an S has, e.g.,
non-zero restriction to a ν-null set in the examples). ∎

**What Proposition 4.1 says.** The only mechanism by which GH has ever been made to act — the
Jordan chain at z = 0 coming from the moments of the transport, i.e. (F1)+(F2) — closes only when
the chain is homogeneous. In the two-sided situation (Theorem J) it is homogeneous because all the
moments ∫ t^j F_φ dt exist. In the one-sided situation of (EF) with a ≥ 0 the chain is inhomogeneous
with inhomogeneity S itself, and GH can be applied to it only if S is smooth modulo ν. This is the
same wall as in [R8-c] §3 and [R8-e] §2, now established without any reference to the geometric
origin of S. Making S smooth would require smearing the pair of Theorem R into an absolutely
continuous family with smooth density, which needs (at least) absolute continuity and smoothness of
the Pesin unstable lamination — unavailable.

---

## 5. Open questions (explicit)

1. **(EF)** itself, in the generality of the brief: a nonzero holomorphic family of order-≤1
   eigen-densities of P^T, locally bounded on closed substrips, over an open vertical strip
   Ω ⊂ {Re z ≠ 0}. Open. Equivalently (Theorem 2.1 of [R8-b]) the statement (J1) for X and for −X.
2. **(J1-0)** (Section 2): the special case of (EF) for strips with a = 0, equivalently
   "no nonzero finite-order S with backward exponential decay and forward sub-exponential growth of
   the weighted transport". Open; by Proposition 2 and Theorem R it suffices for the core case
   μ(d) = 0 (which contains the volume-preserving case and the old core (PE0)).
3. **(V)**: does GH imply the existence of a smooth invariant volume? Open (equivalent by
   Proposition A of [R8-d] to closedness of P(C^∞), and by Proposition B to dim I = 1). A positive
   answer would make the weighted and unweighted pictures coincide and would let the tame
   (closed-range) half of GH act on the Jordan chain; by Theorem V of [R7-e] one would then still
   need quasi-analytic growth of ‖R^Nφ‖_{C^1} on a C^1-dense set of φ.
4. **Quantitative tameness**: does GH give a tame estimate with uniform derivative loss and
   geometric constants (‖R φ‖_{C^k} ≤ C B^k ‖φ‖_{C^{k+σ}} with σ fixed)? By Lemma Q of [R8-a] and
   Theorem V this is exactly what is missing in the volume case. Open; GH is obtained from the
   closed graph theorem, which gives no growth information.
5. **Smearing**: is there a nonzero *absolutely continuous* S with smooth density whose weighted
   transport decays backwards exponentially and grows forwards sub-exponentially, in the presence of
   a positive-entropy measure? By Proposition 4.1(d) such an S would let GH act directly. Open (and
   presumably false in general, because the Pesin lamination is only measurable).

---

## 6. Check of the chain of the brief

* Step 1 (variational step) is correct as stated: h_top(g_1) = sup over g_1-invariant m of h_m(g_1)
  (variational principle); m̄ := ∫_0^1 (g_s)_* m ds is flow-invariant and h_{m̄}(g_1) = h_m(g_1)
  because g_s conjugates g_1 to itself and entropy is affine in the measure; Jacobs' formula applied
  to the flow-ergodic decomposition of m̄ produces a flow-ergodic component with at least that
  entropy.
* Step 2 (Theorem R) I re-read in [R8-a]: the construction (generic pair on one unstable leaf with
  non-atomic Ledrappier–Young conditionals, Laplace transform on the strip, non-vanishing by Fourier
  uniqueness) is correct, with the cited inputs (Ruelle's inequality, Pesin local unstable manifolds,
  Ledrappier–Strelcyn/Ledrappier–Young subordinate partitions, Lemma 6.0 of [R6-a]). The family has
  order ≤ 1 and satisfies (EF)(i)–(iii) on the stated strip, and is nonzero off a discrete set.
* So (EF) is indeed the only missing link, and by Lemma 1/Corollary 1.2 it is a statement strictly
  about the part of the band that positive entropy actually produces; by Proposition 2 the core case
  is (J1-0).

**Honest final assessment.** I could not close (A), (B) or (C) of the planner's sketch either.
Mechanism (B) (Leibniz) was examined: for fixed smooth φ the functional V_z(ψ) := T_z(φψ) satisfies
V_z ∘ (X − z) = −V_z^{Pφ} where V_z^{Φ}(ψ) := T_z(Φψ); iterating formally gives
T_z(ψ) = (−1)^n V_z^{P^n 1}((X − z)^{−n}ψ), which requires (α) invertibility of X − z on C^∞ with
quantitative bounds — this is itself essentially equivalent to the sought conclusion (Remark 3.3 of
[R8-b]: hypoellipticity of P − z would already contain sub-exponential growth of derivatives of
φ∘g_t), and (β) beating the factorial growth of ‖P^n 1‖_{C^1}. Both are out of reach with GH alone,
for the reason made precise in Lemma 3: in the weighted picture only *forward* (growing) iteration
of P is available without (V).

---

## 7. Theorem A: (EF) reduces to a **single-point** Jordan-chain exclusion

This is the main new result of this file. It strictly improves Propositions 3.1 and 3.2 of [R8-b]
("the set of z admitting an order-k Jordan chain has empty interior") to "**one** point of the strip
admits no order-k Jordan chain", and it exhibits Theorem J as the special case c = 0 of a general
principle: *the moment/Jordan argument of Theorem J can be run at any point c of the strip, after
renormalizing the transport by e^{−ct}; GH enters only through the exclusion of a Jordan chain of
length 2 at that single point c.*

**Definition.** For c ∈ C and k ≥ 0, say that *c admits an order-k Jordan chain (of length 2)* if
there are distribution densities A, B of order ≤ k with B ≠ 0,
  B ∘ (P − c) = 0 and A ∘ (P − c) = B,
i.e. (with b = B/ν, α = A/ν) X b = −c b, b ≠ 0, X α = −c α − b.

**Theorem A.** Let X be a smooth vector field on a compact manifold M (GH is used only through the
hypothesis below), let a < b be real, Ω = Σ(a,b) = {a < Re z < b}, and let (T_z)_{z ∈ Ω} be
distribution densities such that
 (i) z ↦ T_z(φ) is holomorphic on Ω for every φ ∈ C^∞(M);
 (ii) for every closed substrip a < a_1 ≤ Re z ≤ b_1 < b, sup{ |T_z(φ)| : a_1 ≤ Re z ≤ b_1,
      ‖φ‖_{C^k} ≤ 1 } < ∞ (some fixed k; k = 1 in (EF));
 (iii) T_z ∘ P = z T_z on Ω.
Suppose that **some single point c ∈ Ω** does not admit an order-k Jordan chain. Then T_z = 0 for
every z ∈ Ω.

*Proof.* Suppose T ≠ 0. Fix c ∈ Ω as in the hypothesis and put σ := Re c ∈ (a,b); choose ρ > 0 with
[σ − ρ, σ + ρ] ⊂ (a,b), and set a' := σ − ρ, b' := σ + ρ.

**Step 1 (a renormalized two-sided decaying transport).** Exactly as in the proof of Proposition 2
(the Gaussian contour construction, Theorem 2.1(B) of [R8-b]), with the contour Re z = σ, there is
ω ∈ R such that S := S_ω,
  S(φ) := (1/2πi) ∫_{Re z = σ} exp((z−σ)² + ω(z−σ)) T_z(φ) dz,
is a nonzero distribution density of order ≤ k, and (shifting the contour to Re z = b' for t ≤ 0 and
to Re z = a' for t ≥ 0, which is legitimate by (i),(ii) and the Gaussian decay of the weight)
  |F_φ(t)| ≤ K e^{b' t} ‖φ‖_{C^k} (t ≤ 0),   |F_φ(t)| ≤ K e^{a' t} ‖φ‖_{C^k} (t ≥ 0),
where F_φ(t) := S(Γ_t φ). (Non-vanishing: pick φ_0, z_0 with T_{z_0}(φ_0) ≠ 0; then
h(y) := T_{σ+iy}(φ_0) is continuous, bounded and ≢ 0 by the identity theorem, and
S_ω(φ_0) = (1/2π)∫ e^{−y²} e^{iωy} h(y) dy is the Fourier transform at −ω of a nonzero continuous
L^1 function, hence ≠ 0 for some ω.)

Put H_φ(t) := e^{−ct} F_φ(t). Then
  |H_φ(t)| ≤ K e^{−ρ|t|} ‖φ‖_{C^k} for all t ∈ R and all smooth φ,   (7.1)
because |e^{−ct}| = e^{−σt}. Moreover t ↦ Γ_tφ is C^1 into C^∞ with (d/dt)Γ_tφ = Γ_t(Pφ), so F_φ is
C^1 with F_φ' = F_{Pφ}, and therefore
  H_φ'(t) = e^{−ct}(F_{Pφ}(t) − c F_φ(t)) = H_{(P − c)φ}(t).   (7.2)

**Step 2 (moments and the Jordan relations).** For j ≥ 0 put m_j(φ) := ∫_R t^j H_φ(t) dt. By (7.1)
the integral converges absolutely and |m_j(φ)| ≤ K ‖φ‖_{C^k} ∫ |t|^j e^{−ρ|t|} dt, so each m_j is a
distribution density of order ≤ k. By (7.2), applied also to (P−c)φ (which satisfies (7.1) with
‖(P−c)φ‖_{C^k} in place of ‖φ‖_{C^k}), t^j H_φ(t) → 0 as |t| → ∞ and all integrals below converge
absolutely; integrating by parts on [−R,R] and letting R → ∞,
  m_0((P−c)φ) = ∫_R H_φ'(t) dt = 0,   m_j((P−c)φ) = −j m_{j−1}(φ)  (j ≥ 1).   (7.3)

**Step 3 (induction, using the hypothesis at c).** From (7.3) with j = 0,1:
m_0 ∘ (P−c) = 0 and (−m_1) ∘ (P−c) = m_0. If m_0 ≠ 0, then (A,B) = (−m_1, m_0) is an order-k Jordan
chain at c, contrary to the hypothesis. So m_0 = 0. Assume m_{j−1} = 0 for some j ≥ 1. Then by (7.3)
m_j ∘ (P−c) = 0 and (−m_{j+1}/(j+1)) ∘ (P−c) = m_j, so the same argument gives m_j = 0. By induction
m_j = 0 for every j ≥ 0.

**Step 4 (quasi-analyticity).** Fix φ. By (7.1), G(ξ) := ∫_R e^{−iξt} H_φ(t) dt converges and is
holomorphic on the strip |Im ξ| < ρ, with G^{(j)}(0) = (−i)^j m_j(φ) = 0 for all j. Hence G ≡ 0 on
the strip, in particular on R; H_φ ∈ L^1 ∩ C^0 with vanishing Fourier transform, so H_φ ≡ 0, and
S(φ) = H_φ(0) = 0. As φ was arbitrary, S = 0, contradicting Step 1. Therefore T ≡ 0. ∎

**Remarks.**
1. **c = 0 is Theorem J.** If 0 ∈ Ω one may take c = 0; under GH, 0 admits no Jordan chain: B∘P = 0
   gives B = cν by (F1) = (K0), and then A ∘ P = cν forces c = 0 by (F2) = (K1), i.e. B = 0. So
   Theorem A contains Lemma M / Theorem J (for strips through 0) and shows that the two facts
   (K0),(K1) are used *only at the single spectral point 0*.
2. **Strict improvement of [R8-b], Props. 3.1–3.2.** Those propositions require that the set of z
   admitting an order-k eigen-density (resp. an order-k Jordan chain) have empty interior in the
   half-plane. Theorem A requires only that *one* point of the given strip be free of Jordan chains.
   In particular Σ_k may be the whole strip minus one point and (EF) still holds there.
3. **c need not be real**, and need not be a zero of z ↦ T_z(φ_0).
4. The hypothesis can be weakened further to: "there is no *infinite geometric* chain at c", i.e. no
   sequence (A_j)_{j ≥ 0} of order-≤k densities with A_0 ≠ 0, A_0∘(P−c) = 0, A_j∘(P−c) = A_{j−1}
   and ‖A_j‖_{(C^k)'} ≤ C r^{−j} for some r > 0. Indeed Step 3 only needs the chain (m_j) to be
   killed, and ‖m_j‖ ≤ K j! ρ^{−j−1} … — more precisely, conversely, a nonzero family on the disc
   |z − c| < r *is the same thing* as such an infinite geometric chain: given (A_j), the series
   T_z := Σ_j (z−c)^j A_j converges for |z−c| < r and satisfies T_z ∘ (P − c) = (z−c)T_z, i.e.
   T_z ∘ P = z T_z; and conversely A_j := T^{(j)}_c/j! satisfies the chain relations with Cauchy
   bounds. So:
   **(EF) on Ω ⟺ no point c ∈ Ω carries a nonzero infinite geometric order-k Jordan chain**, and by
   Theorem A it is enough to kill the *first two* terms of the chain at one point.

**Corollary 7.1 (the problem reduced to a pointwise statement).** Assume GH, and suppose
  (JC) for every c ∈ C with Re c ≠ 0 lying in one of the strips produced by Theorem R, there are no
      distribution densities A, B of order ≤ 1 with B ≠ 0, X(B/ν) = −c(B/ν), X(A/ν) = −c(A/ν) − B/ν
      — it suffices to have *one* such c in each of those strips.
Then every ergodic flow-invariant probability has zero entropy and h_top(g_1) = 0.

*Proof.* If some ergodic μ has h_μ(g_1) > 0, Theorem R gives a nonzero family (T_z) of order ≤ 1 on
Ω = Σ(λ+δ, λ+θ−δ) satisfying (i)–(iii) of Theorem A with k = 1. If 0 ∈ Ω, Remark 1 above (i.e.
Theorem J) gives T ≡ 0; otherwise Ω ⊂ {Re z ≠ 0} and (JC) supplies a point c ∈ Ω with no order-1
Jordan chain, so Theorem A gives T ≡ 0. Either way we contradict the non-vanishing in Theorem R.
Hence h_μ(g_1) = 0 for every ergodic flow-invariant μ, and the variational step (step 1 of the
chain) gives h_top(g_1) = 0. ∎

**Corollary 7.2 (contrapositive; a strengthening of the known consequences of positive entropy).**
If X is any smooth field with an ergodic measure of positive entropy, then for the strip Ω of
Theorem R, **every** c ∈ Ω admits an order-1 Jordan chain (not merely every c off a discrete set is
in Σ_1). Indeed, apply Theorem A: if some c ∈ Ω had no chain, the family would vanish identically,
contradicting its non-vanishing.

**What is still missing after Theorem A (precisely).** One must exclude, for at least one point c of
a given strip with Re c ≠ 0, the pair of equations
  X b = −c b (b ≠ 0, order ≤ 1), X α = −c α − b (order ≤ 1).
GH does this at c = 0 by (K0) and (K1). At c ≠ 0 the obstruction identified in Remark 3.3 of [R8-b]
persists: the right-hand sides are not smooth, so GH cannot be applied directly, and the smooth
version of the statement (which *is* provable: at a maximum of |b|², X|b|² = −2 Re c |b|² forces
b = 0 when Re c ≠ 0) is unavailable for distributions. Two things that Theorem A newly makes
available, and that I could not exploit:
 (a) one is free to choose c anywhere in the strip, in particular at points where extra information
     might hold (e.g. c with Re c = max_m m(d), or c not of the form μ(d) for any ergodic μ, or c
     off the countable set of "tilted conformal" eigenvalues);
 (b) by Corollary 7.2 a counterexample must have Jordan chains at *every* point of a two-dimensional
     open set, with holomorphic dependence — an uncountable, analytically parametrized family of
     non-smooth eigen-distributions of order 1, all with wavefront sets inside the characteristic set
     {ξ : ξ(X) = 0} and invariant under the lifted flow (standard propagation of singularities for
     the first-order operator X + c, whose principal symbol does not depend on c). I record the
     wavefront remark as an observation only: it is the same for all c, so by itself it does not
     separate c = 0 from c ≠ 0.

### 7.1 A case where the Jordan chain *can* be excluded (proved; no GH)

Theorem A is not vacuous: here is a growth criterion that kills chains outright, and a genuine
consequence of it. Recall G_k(t) = ‖Γ_t‖_{C^k → C^k} and γ_k^± from Section 1.

**Proposition 7.3.** Let c ∈ C. If
  liminf_{t → +∞} G_k(t) e^{−(Re c)t} / t = 0  or  liminf_{t → +∞} G_k(−t) e^{(Re c)t} / t = 0,
then c admits no order-k Jordan chain. (In particular this holds whenever Re c ≥ γ_k^+ and
G_k(t) = o(t e^{γ_k^+ t}), or symmetrically on the backward side.)

*Proof.* Let (A,B) be a chain at c: B ≠ 0, B ∘ (P−c) = 0, A ∘ (P−c) = B. Fix φ with B(φ) ≠ 0. As in
Lemma 1, h_B(t) := B(Γ_tφ) satisfies h_B' = c h_B, so h_B(t) = e^{ct}B(φ); and
h_A(t) := A(Γ_tφ) satisfies h_A'(t) = A(P Γ_t φ) = c h_A(t) + B(Γ_t φ) = c h_A(t) + e^{ct}B(φ),
whence h_A(t) = e^{ct}(A(φ) + t B(φ)). Therefore
  |A(φ) + t B(φ)| e^{(Re c)t} = |A(Γ_tφ)| ≤ ‖A‖_{(C^k)'} G_k(t) ‖φ‖_{C^k},
so |t| |B(φ)| ≤ |A(φ)| + ‖A‖ ‖φ‖_{C^k} G_k(t) e^{−(Re c)t} for all real t. Dividing by |t| and using
either hypothesis along a sequence gives B(φ) = 0, a contradiction. ∎

**Corollary 7.4 (proved).** Suppose X preserves a smooth positive density ω and take ν = ω (so
d = 0, J ≡ 0, Γ_t φ = φ ∘ g_t, G_0(t) ≡ 1). Then no c ∈ C admits an order-0 Jordan chain, and
consequently (Theorem A) **there is no nonzero family (T_z) of complex measures on any open vertical
strip with T_z ∘ P = z T_z, holomorphic and locally bounded in total variation**. No GH is needed.
Combined with Lemma 1.1(iii) (Σ_0 ⊂ iR in the volume case) this completely settles the order-0 case
of (EF) for volume-preserving fields.

*Proof.* G_0(t) ≡ 1 = o(t), so Proposition 7.3 applies at every c with Re c ≥ 0 (forward hypothesis)
— and at every c (the forward hypothesis alone already covers all c, since e^{−(Re c)t}/t → 0 for
Re c > 0, while for Re c ≤ 0 one uses the backward hypothesis G_0(−t)e^{(Re c)t}/t = e^{(Re c)t}/t
→ 0). Then apply Theorem A with k = 0 on any strip. ∎

**Scope (honest).** Corollary 7.4 does not help with the problem, because the families produced by
Theorem R have genuine order 1 (the pair construction loses one derivative: the bound involves
‖φ‖_{C^1}), and for k = 1 the band is wide: γ_1^+ ≥ Λ_1 > 0 as soon as the flow has exponential
derivative growth, while the strips of Theorem R sit strictly inside the band (Corollary 1.2(b)).
Proposition 7.3 therefore never applies to them. It is recorded to show that the single-point
criterion of Theorem A is usable, and to isolate the exact quantity — the growth of
‖Γ_t‖_{C^1 → C^1} relative to e^{(Re c)t} — that would have to be controlled.

**Updated list of open questions.** Replace item 1 of Section 5 by the sharper
  1'. **(JC)**: under GH, exhibit in each strip of Theorem R one point c with Re c ≠ 0 carrying no
      order-1 Jordan chain of P^T (equivalently, by Remark 4 above, no infinite geometric chain).
      This is now the only missing input of the whole chain. By Theorem A it is a *pointwise*
      statement about the transposed operator at a single spectral point, and it is the exact
      analogue at c ≠ 0 of (K0) ∧ (K1) at c = 0.
Items 2–5 of Section 5 remain as stated; item 2 ((J1-0)) remains the natural target for the core
case μ(d) = 0, where one may also take c in the strip as close to 0 as one likes — note that
Theorem A allows c → 0, but the hypothesis "no Jordan chain at c" is *not* known to be stable as
c → 0, which is precisely the discontinuity that the Patterson blow-up of [R8-c] Cor. 2.3 embodies.

=== END OF ANSWER round9_q3 ===
