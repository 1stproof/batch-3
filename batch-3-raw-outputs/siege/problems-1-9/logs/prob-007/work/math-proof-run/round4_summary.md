# Running summary after round 3 results (written at round 4 plan)

## Notation
a_0=c_1, a_{i+1}=f(a_i), A={a_0..a_3}, B=A∪{v}; critical values a_1, v. i: PMod(S²,B)→PMod(S²,A) forgets v; kernel F=π_1(S²∖A,v) (point pushes). W = image of D_f in M_{0,5}. Ψ=(i_*,f^*): Teich(B)→H×H, D_f=Ψ^{-1}(Δ). λ = modular lambda function (Teich(A)≅H, moduli coordinate t=λ).

## Status: a complete written proof of the [GOAL] is in hand (round3_q1), independently corroborated by round3_q2 (exact simplicity + lift + 3/0 split check, taking Steps 1–3 as given) and round3_q4 (hostile referee: re-derived Steps 0–4, found no error, gave a second exact simplicity proof via deck images). round3_q3 re-proved the criterion (Steps 2–3) given Step 1. Not yet certified by verify queries; round 4 sends two verify queries on round3_q1.

## Standing results (never drop)
- #2 (round1_q2) model: a_0=0,a_1=∞,a_2=1,a_3=t, f_t=1+β/z+γ/z², β=(t²+t−1)/(1−t), γ=t(1−2t)/(1−t), v=−(t²−3t+1)²/D, D=4t(1−2t)(1−t); W = t-sphere minus 10 points. Base map t0=1/4: f=1−11/(12z)+1/(6z²), c_2=4/11, v=−25/96.
- #3 (round1_q2) H_1 obstruction fails (not on the current line).
- #4 (round1_q1) {v,a_j} curves: T_γ² preserves D_f (not on the current line).
- #5 (round1_q4) {a_1,v} curves: T_γ preserves D_f iff 3/0 split; no power if 2/1.
- #6 (round1_q2) cusp t=1/2: single twist about a 3/0 curve γ0, in the component stabilizer (finite orbit).
- #8 (round2_q3) forget-a_1 map u(t) (not on the current line).
- #9 (round2_q2) quotient tests useless for {v,a_j} (not on the current line).
- NEW #13 (round3_q1) fibre formula: over A=(0,∞,1,t), pulled-back modulus w satisfies v'=V_t(w)=−((w−1)²−t)²/(4w(w−1)(w+t−1)); V_t^{-1}(∞)={0,1,∞,1−t} simple, so λ(f^*τ')≠1−λ(i_*τ') for all τ' (★).
- NEW #14 (round3_q1) linking criterion: Ψ avoids all graphs Γ_g, g∈Γ(2)S; for non-elliptic g, H_1(H×H∖Γ_g)=Z, Δ contractible inside; if i(T)=1, Ψ∘T=Ψ and the fibre loop of T winds ±1 about g(p0), then ⟨T⟩ has infinite orbit on π_0(D_f).
- NEW #15 (round3_q1) explicit curve at t0=1/4: α from v: below R, up through (1,∞), down through (0,1/4), up through (v,0), above R to ∞ (simple: nested chords); exact lifting via V^{-1}(R)=R∪{|w−1|=1/2}∪{|w|=√3/2} gives lift β from 1/4 ending at 3/4 = 1−t0, β ≃ (clockwise loop about 0)·[1/4,3/4]; λ-lift endpoint g(p0), g=T^{∓2}S, trace ∓2, parabolic. Hence T_γ (k=1), γ=∂N(α), preserves D_f and has infinite orbit.
- NEW #16 PROVED [GOAL] (round3_q1).

## Proof outline (round3_q1, as it will be presented)
0. Standard facts cited: λ properties (λ(τ+2)=λ, λ(−1/τ)=1−λ, λ≈16e^{iπτ}); Bers/Birman fibration i_*: fibre over p = universal cover of S²∖A_p, point pushes = deck group; Teich(B) contractible; equivariance f^*(φτ)=φ~f^*(τ).
1. Step 1 fibre formula (#13), derived by F(z)=v'+z², Möbius normalization, u=s_2−s_0, U=u².
2. Steps 2–3 criterion (#14).
3. Step 4 (#15): point push around lasso of α = T_γ^{±1}; lasso lifts to closed loop (β·circle about 3/4·β^{-1}) ⇒ f^*∘T=f^* on fibre ⇒ lift T~ fixes a point of Teich(A) ⇒ trivial (PMod(S²,A) acts freely) ⇒ T preserves D_f; for T^m fibre loop winds ±m about g(p0) ⇒ contradiction for m≠0.
Caveat (honest): round3_q1 proves everything for the representative f=f_{1/4}; extending to an arbitrary f of the family by transporting γ along a path in W (naturality of D_f under a conjugating homeomorphism isotopic along the path) is only sketched there. Planner judges it a standard short naturality argument: along a path t_s in W, isotopy h_s of (S²,B) and its lift h̃_s with f_{t_s}∘h̃_s=h_s∘f_{1/4}, h̃_s|_A=h_s|_A, so h_1 is a combinatorial equivalence rel B carrying D_{f_{1/4}} to D_{f_t} and T_γ to T_{h_1(γ)}. Round 4 q3 writes it out.

## Dead ends (precise)
None refuted at the level of the main line. Earlier set-aside routes (not refuted, no longer needed): H_1 abelian obstruction (#3 shows it fails), finite quotients S_4/S_5 (planner computation: G_0-orbits = full orbits), Q-type quotients (#9), recollection of Hironaka–Koch.

## Open gaps
1. Certification of round3_q1 by two verify queries (round 4 q1, q2).
2. Full write-up of transport to arbitrary f in the family (round 4 q3).
3. Optional for the document: mapping-class description of γ (e.g. as image of the straight-segment cusp curve γ0 under an explicit point push / twist word) (round 4 q4).

## Next round target
Complete proof in hand → audit wave: q1, q2 = verify queries carrying round3_q1 verbatim (step-by-step check, explicit verdict, including whether the f_{1/4} representative + transport answers the problem as posed); q3 = rigorous transport to every f of the family plus careful statements/proofs of the cited Teichmüller facts (fibration, equivariance, free action); q4 = mapping-class description of γ. If both verifies certify: record [AUDIT] lines citing entry 16 and conclude at round 5 (after folding in q3's transport if it's sound). If a verifier finds a gap: RETRACT 16, re-open, aim the wave at the gap.
