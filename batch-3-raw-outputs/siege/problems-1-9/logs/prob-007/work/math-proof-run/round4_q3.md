kind: attempt
Open question attempted: the open gap "transport to every map f of the family, and rigorous statement/proof of the Teichmüller facts used" in the proof of ledger entry 16 ([GOAL]); the proof below is written for the single representative f = f_{1/4}.

Task. Below (verbatim) is a proof, for f = f_{1/4}(z) = 1 − 11/(12z) + 1/(6z²), that the twist about an explicit curve γ preserves D_f and has an infinite orbit on π_0(D_f). Produce complete, rigorous write-ups of the following, so that the final document can present the result for an arbitrary f as in the problem:

(A) Reduction to the model. Every quadratic rational map f with a critical point c_1 of exact period 4 and v = f(c_2) not on the cycle is Möbius-conjugate to exactly one f_t (normal form a_0 = 0, a_1 = ∞, a_2 = 1, a_3 = t, f_t = 1 + b/z + c/z², b = (t²+t−1)/(1−t), c = t(1−2t)/(1−t)) with t in W := C minus {0, 1, 1/2, roots of t²−3t+1, t²+t−1, 3t²−3t+1}; prove this (including why these 10 values are exactly the excluded ones, and that W is connected).

(B) Naturality/transport. Let t ∈ W and t_s (s ∈ [0,1]) a path in W from 1/4 to t. Prove: there is an isotopy h_s of S² with h_0 = id, h_s(B_{1/4}) = B_{t_s} pointwise-labelled, and a continuous lift h̃_s with f_{t_s}∘h̃_s = h_s∘f_{1/4}, h̃_0 = id, and h̃_s = h_s on A_{1/4}; then h_1^{-1}∘h̃_1 is isotopic to the identity rel A_{1/4}. Deduce that the map Teich(S², B_{1/4}) → Teich(S², B_t) induced by h_1 (change of marking) carries D_{f_{1/4}} onto D_{f_t}, hence components onto components, and conjugates the action of T_γ to that of T_{h_1(γ)}. Conclude that for f = f_t the curve h_1(γ) has the required property, and describe it explicitly at least for real t in a neighbourhood interval of 1/4 on which the real order v < 0 < t < 1 persists (same real-line crossing pattern). Also address: if f is given abstractly (not in normal form), the curve is the image of h_1(γ) under the conjugating Möbius map.

(C) The cited Teichmüller facts, stated precisely with proofs or precise standard references-free justifications: the definition of f^* as a well-defined map Teich(B) → Teich(A) (pulling back the complex structure by f and restricting the marking to A ⊂ f^{-1}(B)); the equivariance f^*(φ·τ) = φ~·f^*(τ) for the lift φ~ with f∘φ~ = φ∘f, and why φ~ fixes A pointwise up to isotopy when φ does B; the forgetful fibration i_*: Teich(B) → Teich(A) with fibre over p identified with the universal cover of S²∖A_p and the point-push subgroup acting as its deck group; contractibility of Teich(B); free action of PMod(S², A) on Teich(A) ≅ H; the modular λ-function facts used. Point out any place where the proof below uses one of these in a way that is not correct, and repair it.

## The proof (verbatim, from an earlier round)

# Answer: an explicit twist curve with an infinite orbit on π_0(D_f)

The proof below is written for the base map f = f_{1/4}. The planner's sketch was checked step by step. Every algebraic identity it uses was re-derived by hand. The numerical claim that the arc is simple is replaced by an exact combinatorial argument (§4), using the fact that V^{-1}(real line) is the union of the real line and two explicit circles.

## 0. Setup, notation, standard facts (cited from memory)

a_0 = c_1, a_{i+1} = f(a_i) (indices mod 4), A = {a_0,…,a_3}, B = A ∪ {v}. The critical values are a_1 = f(c_1) and v. Teich(A) is identified with H, and the modulus map π: Teich(A) → C∖{0,1} is the coordinate t of the normalisation (a_0,a_1,a_2,a_3) ↦ (0,∞,1,t). We take π = λ, the modular lambda function: a universal covering H → C∖{0,1} with deck group Γ(2)/±1. Its standard properties are λ(τ+2) = λ(τ), λ(−1/τ) = 1−λ(τ), and λ ≈ 16e^{iπτ} as τ → i∞. In particular, λ maps iR_{>0} decreasingly onto (0,1).

**Bers/Birman fibration (from memory).** i_*: Teich(B) → Teich(A) is a fibration. The fibre over p is the universal cover of S²∖A_p (A_p is the configuration with modulus π(p)), parametrised by the position v' of the fifth point. The point-push subgroup ker(PMod(S²,B) → PMod(S²,A)) ≅ π_1(S²∖A, v) acts on each fibre as its deck group. Teich(B) is contractible.

**Pullback.** f^*(τ) is the pullback of the marked structure, restricted to A ⊂ f^{-1}(B). For φ ∈ PMod(S²,B) there is a lift φ~ with f∘φ~ = φ∘f, and f^*(φτ) = φ~·f^*(τ). Similarly, i_*(φτ) = i(φ)·i_*(τ).

Put Ψ = (i_*, f^*): Teich(B) → H×H. Then D_f = Ψ^{-1}(Δ), where Δ is the diagonal.

## 1. Explicit model (verified by hand)

Normalise a_0 = 0, a_1 = ∞, a_2 = 1, a_3 = t, and put f_t(z) = 1 + b/z + c/z², with b = (t²+t−1)/(1−t) and c = t(1−2t)/(1−t). Then:
- 0 is a critical point mapping to ∞ (double pole), and f(∞) = 1.
- f(1) = 1+b+c = t, because b + c = −(1−t)²/(1−t) = t−1.
- f(t) = 0 ⇔ t² + bt + c = 0. The numerator is t²(1−t) + t(t²+t−1) + t(1−2t) = 0.

At t0 = 1/4 this gives b = −11/12, c = 1/6, c_2 = −2c/b = 4/11, and v = 1 − 121/48 + 121/96 = −25/96. On the real line the order is v < a_0 = 0 < a_3 = 1/4 < a_2 = 1 < a_1 = ∞.

## 2. The fibrewise formula (Step 1, verified)

Fix t and let v' ∉ {0,1,t,∞}. Up to Möbius maps, the pullback of (Ĉ; 0,∞,1,t,v') is given by F(z) = v' + z², whose critical points are ∞ ↦ ∞ = a_1 and 0 ↦ v'. The marked preimages are:
- a_0' = ∞;
- a_1' = s_2 with s_2² = 1−v' (a preimage of a_2);
- a_2' = s_3 with s_3² = t−v' (a preimage of a_3);
- a_3' = s_0 with s_0² = −v' (a preimage of a_0).

The Möbius map z ↦ (s_3−s_2)/(z−s_2) sends ∞, s_2, s_3 to 0, ∞, 1. So the pulled-back modulus is w = (s_3−s_2)/(s_0−s_2).

Put u = s_2 − s_0 and U = u². From s_2² − s_0² = 1 we get s_2 + s_0 = 1/u and s_2 = (u+1/u)/2. Also s_3 = s_2 − wu. Then s_3² − s_0² = t becomes 1 − w(U+1) + w²U = t, so U = (w+t−1)/(w(w−1)). Finally v' = −s_0² = −(1−U)²/(4U), which gives

  V_t(w) = −((w−1)² − t)² / (4w(w−1)(w+t−1)).

Check: V_t(t) = −(t²−3t+1)²/(4t(t−1)(2t−1)) = v(t).

**Key fact.** V_t^{-1}(∞) = {0, 1, ∞, 1−t}. At w = 1−t the numerator is (t²−t)² ≠ 0. Hence w = 1−t occurs only when v' = a_1, which is excluded. Therefore, for every τ' ∈ Teich(B):

  λ(f^*τ') ≠ 1 − λ(i_*τ').   (★)

**f^* on a fibre.** Restricted to the fibre Ũ over p0, the map τ' ↦ w(τ') := λ(f^*τ') is continuous, because the marked preimages move continuously with the marking. It satisfies V_{t0}∘w = (position of v'). So it is the lift, through the unbranched covering V_{t0}: Ŵ := Ĉ∖V^{-1}(A) → S²∖A, of the projection Ũ → S²∖A. The covering is unbranched because the branch values 0, 1, t lie in A, and over a_1 the preimages are simple. Since λ∘f^* = w, the map f^*|_Ũ is the lift of w through λ.

At τ ∈ D_f over p0 we have λ(f^*τ) = λ(p0) = t0, so τ sits at w = t0. Both lifts are pinned by w(τ) = t0 and f^*(τ) = p0.

## 3. Graphs and the linking argument (Steps 2–3, verified)

λ(q) = 1 − λ(p) = λ(−1/p) holds iff q = g(p) with g ∈ Γ(2)·S, where S(τ) = −1/τ. So by (★), Ψ(Teich(B)) avoids every graph Γ_g = {(p, g(p))}.

If g is not elliptic, then Γ_g ∩ Δ = ∅. Moreover X_g := H×H∖Γ_g ≅ H×(H∖{i}) via (p,q) ↦ (p, (q − Re g(p))/Im g(p)), so H_1(X_g) ≅ Z. The class of a loop in a fibre {p}×H is its winding number about g(p).

Let T ∈ PMod(S²,B) satisfy i(T) = 1 and Ψ∘T = Ψ. Then T preserves D_f. Let τ ∈ D_f, let D_0 be its component, and suppose T^m D_0 = D_0 with m ≠ 0.
- Choose σ ⊂ D_0 from τ to T^mτ, and σ' in the fibre over p0 with the same endpoints.
- Teich(B) is contractible, so σ ≃ σ' rel endpoints in Teich(B). Applying Ψ, the loop Ψσ is homotopic rel basepoint to Ψσ' inside Ψ(Teich(B)) ⊂ X_g. Both are loops at (p0,p0), because Ψ(T^mτ) = Ψ(τ).
- Ψσ lies in Δ ≅ H, which is contractible and contained in X_g, so Ψσ is null-homotopic in X_g.
- Hence the fibre loop f^*∘σ' has winding number 0 about g(p0).

This is a contradiction whenever that winding number is ±m.

## 4. The curve and the computation (Step 4, with an exact proof of simplicity)

### Definition of α

Work with f = f_{1/4}. Let α be an arc from v to a_1 = ∞, with interior in S²∖B, built as follows:
1. Leave v into the lower half-plane and cross R upward at a point x1 ∈ (1, ∞).
2. Run in the upper half-plane and cross downward at x2 ∈ (0, 1/4).
3. Run in the lower half-plane and cross upward at x3 ∈ (v, 0).
4. Stay in the upper half-plane until reaching ∞.

**α can be taken simple.** On the circle R∪{∞} the order is v < x3 < x2 < x1 < ∞.
- The lower chords [v, x1] and [x3, x2] are nested.
- The upper chords [x2, x1] and [x3, ∞] are nested.

So pairwise disjoint chords realise the pattern, and α is simple. Its isotopy class in (S²,B) is determined by this crossing pattern.

### Definition of γ

γ := ∂(thin regular neighbourhood of α). It is a simple closed curve enclosing exactly v and a_1 = f(c_1), and separating them from a_0 = c_1, a_3 = 1/4 and a_2 = 1.

T_γ^{±1} is the point push of v around the lasso of α. To see this, take an annulus around the lasso: its inner boundary bounds a disc containing only a_1, so that twist is trivial, and its outer boundary is γ. Forgetting v, γ bounds a disc with a single marked point, so i(T_γ) = 1.

### Exact lifting

At t = 1/4 the formula factorises: V(w) = −(w−½)²(w−3/2)² / (4w(w−1)(w−¾)). The deck group of V is {id, g_0, g_2, g_3}, with
- g_0(w) = (w−¾)/(w−1),
- g_3(w) = ¾(w−1)/(w−¾),
- g_2(w) = 3/(4w).

V(w) is real iff w̄ = h(w) for some deck transformation h. Solving each case:
- h = id gives R.
- h = g_0 gives |w|² − w − w̄ + ¾ = 0, i.e. the circle C1: |w−1| = ½.
- h = g_3 gives |w−¾|² = −3/16, which is empty.
- h = g_2 gives the circle C2: |w| = √3/2.

C1 and C2 meet at the critical points P, P̄ = ¾ ± (√3/4)i, which lie over t. These curves cut the sphere into 8 faces, each mapped homeomorphically onto a half-plane.

On R the images are: −√3/2 ↦ 1, 0 ↦ ∞, ¼ ↦ v, ½ ↦ 0, ⅔ ↦ v, ¾ ↦ ∞, √3/2 ↦ 1, 1 ↦ ∞, 9/8 ↦ v, 3/2 ↦ 0, 3 ↦ v. Since V′(¼) > 0 (V increases from −∞ to 0 on (0, ½)), the face U_2 = {Im w > 0, |w| < √3/2, |w−1| > ½} maps to the upper half-plane, and adjacent faces alternate.

Lifting α from w = ¼, piece by piece:
1. **Into L_2 (lower, inside C2 only).** On ∂L_2 the preimage of (1,∞) is (−√3/2, 0). So the lift crosses R at a point of (−√3/2, 0) and enters U_2.
2. **Inside U_2.** On ∂U_2 the preimage of (0, ¼) is the arc of C1 from ½ to P. The lift crosses it into U_12 (upper, inside both circles).
3. **Inside U_12.** On ∂U_12 the preimage of (v, 0) is the real segment (½, ⅔). The lift crosses it into L_12.
4. **Inside L_12.** On ∂L_12 the preimage of ∞ is ¾. The lift β therefore ends at w = ¾ = 1 − t0.

In C∖{0,1}, β goes from ¼ below 0 to the negative axis, over 0 to the right, and then to ¾. So β ≃ (clockwise loop about 0)·[¼, ¾].

Now lift β through λ from p0 = iy0, where λ(iy0) = ¼:
- The loop about 0 lifts to a path from p0 to p0 ∓ 2.
- The segment lifts along the vertical line to S(p0) ∓ 2, using λ(i/y0) = ¾.

So the endpoint is q* = g(p0) with g = T^{∓2}S, where T here is the translation τ ↦ τ+1. As a matrix g = [[∓2, −1], [1, 0]], with trace ∓2. So g is parabolic, not elliptic, and g ∈ Γ(2)S.

The lasso of α lifts to β·(small loop about ¾)·β^{-1}. Since ¾ ∉ {0, 1, ∞}, the small loop lifts through λ to a small closed loop about q*.

### Conclusions

**T_γ preserves D_f.** The lifted lasso is a closed loop in H. So f^*(T_γτ') = f^*(τ') on the fibre over p0. The lift T~ fixes a point of Teich(A), and PMod(S²,A) acts freely there, so T~ = 1. Hence Ψ∘T_γ = Ψ everywhere.

**The orbit is infinite.** For T_γ^m, the fibre loop f^*∘σ' is β̃·c̃^m·β̃^{-1}, which winds ±m about g(p0). By §3 this contradicts m ≠ 0.

## Final answer

For f = f_{1/4} (real points v = −25/96 < c_1 = 0 < f³(c_1) = 1/4 < f²(c_1) = 1, with f(c_1) = ∞), take γ to be the boundary of a thin neighbourhood of the simple arc α from v to f(c_1) = ∞ described in §4. In words:
- from v, go below the real axis and cross it in (1, ∞);
- pass above and come back down through (0, 1/4);
- pass below and come up through (v, 0);
- then go above everything to ∞.

γ encloses exactly v and f(c_1). The power k = 1 works: T_γ preserves D_f, and no nonzero power of T_γ fixes the component of the base point. So ⟨T_γ⟩ has an infinite orbit on π_0(D_f).

### Status

**Proved:** everything above for f_{1/4}, except the facts quoted from memory (the λ-function, the Bers/Birman fibration, and the lifting formalism for f^*).

**Only sketched:** the claim for other maps f in the family, obtained by transporting γ along a path in the image W of D_f in moduli space. This was not checked in detail.

