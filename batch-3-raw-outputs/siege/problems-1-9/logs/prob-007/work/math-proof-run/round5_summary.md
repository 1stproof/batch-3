# Running summary after round 4 results (written at round 5 plan)

## Notation
a_0=c_1, a_{i+1}=f(a_i), A={a_0..a_3}, B=A∪{v}; critical values a_1, v. i: PMod(S²,B)→PMod(S²,A) forgets v; kernel = point pushes π_1(S²∖A,v). W = parameter set (t-plane minus 9 finite points 0,1,1/2, roots of t²−3t+1, t²+t−1, 3t²−3t+1; "10" if ∞ counted). Ψ=(i_*,f^*): Teich(B)→H×H, D_f=Ψ^{-1}(Δ), λ = modular lambda (Teich(A)≅H with modulus = λ).

## Status: [GOAL] PROVED (entry 16, round3_q1) and certified by two independent verify queries (round4_q1, round4_q2), each with small repairs that the verifier itself proved in full; the same repairs were proved independently in round4_q3. Run concludes at round 5.

## The answer (for the proof document)
Model f = f_{1/4}(z) = 1 − 11/(12z) + 1/(6z²): cycle 0→∞→1→1/4→0, c_2=4/11, v=−25/96; real order v < c_1 < f³(c_1) < f²(c_1) < f(c_1)=∞.
α: simple arc from v to ∞: leave v into the lower half-plane, cross R upward in (1,∞), cross downward in (0,1/4), cross upward in (v,0), then upper half-plane to ∞. Explicit realisation (round4_q1): lower semicircle v→2, upper semicircle over [1/8,2], lower semicircle over [−1/8,1/8], vertical ray up from −1/8. γ = ∂N(α), enclosing exactly {v, f(c_1)}. Power k=1: T_γ preserves D_f, ⟨T_γ⟩ has infinite orbit on π_0(D_f).
Mapping-class form (round4_q4): γ = T_c^{-1}(γ_0^+), c = circle |z−1/2| = 3/5 (around c_1, f³c_1, f²c_1, not v), γ_0^+ = ∂N(α_0^+), α_0^+ : v → upper half-plane → down through (0,1/4) → lower half-plane to ∞. Note T_{γ_0^+} also preserves D_f but its g=S is elliptic (finite information), T_c does NOT preserve D_f (2/1 split).
General f: γ_f = M^{-1}h_1(γ) (M normalizing Möbius, h_1 transport isotopy along a path in W); for t ∈ (0,(3−√5)/2) same crossing description relative to the circle C=M^{-1}(R̂) through the five points (round4_q3 B6–B7).

## Standing results (never drop)
- #2 (round1_q2) normal form f_t=1+b/z+c/z², b=(t²+t−1)/(1−t), c=t(1−2t)/(1−t), v(t)=−(t²−3t+1)²/(4t(1−t)(1−2t)); uniqueness of (t,M) for the pair (f,c_1) proved in round4_q3 (A).
- #3 (round1_q2) H_1 obstruction fails (not on the current line).
- #4 (round1_q1) {v,a_j} curves: T_γ² preserves D_f (not on the current line).
- #5 (round1_q4) {a_1,v} curves: T_γ preserves D_f iff 3/0 split (not on current line; superseded by #17 framework).
- #6 (round1_q2) cusp t=1/2 twist in component stabilizer (not on the current line).
- #8, #9 (not on the current line).
- #13 (round3_q1) fibre formula V_t(w) = −((w−1)²−t)²/(4w(w−1)(w+t−1)), (★) λ(f^*τ')≠1−λ(i_*τ').
- #14 (round3_q1) linking criterion.
- #15 (round3_q1) explicit curve at t0=1/4, lift ending at 3/4, g = T^{−2}S parabolic (sign: "−", round4_q1/q2).
- #16 PROVED [GOAL] (round3_q1); [AUDIT] entries from round4_q1, round4_q2.
- NEW #17 (round4_q3; also q1 §3 R1, q2 §4) A-fixing lift T~=T_{γ1}T_{γ2} of T_γ; f^*∘T_γ=[T~]f^*; free action of PMod(S²,A) (elementary proof C3) ⇒ [T~]=1.
- NEW #18 (round4_q3 C6; q1 R2 implicit function; q2 analytic-set argument) D_f smooth curve, components = path components.
- NEW #19 (round4_q3 B1–B7; also q1 §4b, q2 §5b) transport lemma to every f.
- NEW #20 (round4_q4) mapping-class description and independent 3/0 parity check in coordinate s=1/z−11/4 (y = f−v = s²/6).

## Repairs the final proof must include (from the audits)
R1: round 3's general equivariance "every φ∈PMod(S²,B) lifts to PMod(S²,A)" is false in general (lift can swap a_i with its preimage-mate); use the explicit lift of T_γ (#17). R2: components are path components (#18). R3: transport (#19). Minor: g = T^{−2}S (not ∓); truncate β before 3/4 and use a small loop c~ around q*; homotope the fibre loop inside H∖λ^{-1}(1−t0) (legit by (★) and simple connectivity of the fibre); [1/4,3/4] passes through the critical point 1/2 so α_0 must be perturbed (round4_q4 §1). Facts cited from memory: λ properties, Teichmüller's theorem, Bers fibration/Birman exact sequence, push formula Push(δ)=T_{δ_L}T_{δ_R}^{-1}, isotopy classification of chord systems/Epstein, proper discontinuity, Hamstrom.

## Dead ends (precise)
None refuted. Set aside, not refuted (not needed): H_1 abelian route (#3 shows abelian test fails), finite quotients, Q-type quotients (#9).

## Open gaps
None for the goal. (Number of components of D_f infinite follows from the infinite orbit.)

## Target
Conclude: goal is the problem's posed claim, proved and certified twice. Proof assembly should build on round3_q1 + repairs from round4_q1/q2/q3 + description from round4_q4.
