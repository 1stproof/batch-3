# Running summary after round 2 results (written at round 3 plan)

## Notation
a_0=c_1, a_{i+1}=f(a_i), A={a_0..a_3}, B=A∪{v}; critical values a_1, v. i: PMod(S²,B)→PMod(S²,A) forgets v; kernel F=π_1(S²∖A,v)≅F_3 (point pushes), ℓ_j = loop around a_j. G = mapping classes whose lift fixing A equals i(φ) rel A (they preserve D_f). W = image of D_f in M_{0,5}; G_0 = stabilizer of a component D_0 = monodromy image of π_1(W). Orbit of D_0 under ⟨φ⟩ infinite iff no nonzero power of φ lies in G_0. H = G∩F, K = G_0∩F.

## Established in earlier rounds (ledger #2–#6)
- Model (round1_q2, sympy-checked): a_0=0,a_1=∞,a_2=1,a_3=t, f_t=1+β/z+γ/z², β=(t²+t−1)/(1−t), γ=t(1−2t)/(1−t), v=−(t²−3t+1)²/D, v−1=−(t²+t−1)²/D, v−t=−(3t²−3t+1)²/D, D=4t(1−2t)(1−t). W = t-sphere minus 10 points (0,1,∞,1/2, roots of t²−3t+1 [v→a_0], t²+t−1 [v→a_2], 3t²−3t+1 [v→a_3]). Base example t0=1/4: f=1−11/(12z)+1/(6z²), c_2=4/11, v=−25/96.
- H_1 obstruction fails (round1_q2, #3). {v,a_j} curves: T_γ² ∈ G for every arc (round1_q1, #4). {a_1,v} curves: T_γ ∈ G iff 3/0 split, no power if 2/1 (#5). t=1/2 cusp: single twist about a 3/0 curve γ0, in G_0 (#6).

## Round 2 results (all four screened OK, none settled the goal)
- round2_q3: forget-a_1 map u(t)=(1−t)P²/R², u−1=−tQ²/R² (sympy-rechecked by planner; ledger). Its conclusion: F/⟨⟨ℓ_1⟩⟩ cannot decide the {v,a_j} family (modulo a sketched surjectivity lemma).
- round2_q2: Q and F/⟨⟨ℓ_1⟩⟩ quotient tests cannot separate T_γ² from K for {v,a_j} curves (ledger). Candidate answers in round2_q1/q3/q4 (e.g. T_β²(γ0) with β around {v,a_0}) are unproved; NOTE the planner's computation shows the twist-square about the short real segment [v,a_0] at t0=0.3 IS the cusp monodromy of the root (3−√5)/2, so round2_q3's candidate with that β is in G_0 (useless).
- round2_q1/q4: only recollections of Hironaka–Koch ("A disconnected deformation space of rational maps", J. Mod. Dyn. 2017); nothing reconstructed.

## Planner's own work this step (machine checks, recorded honestly)
1. Numerical braid monodromy (t0=0.3, scripts in /tmp/mono, not part of any proof): computed the 9 generators of G_0 as automorphisms of F_4=π_1(C∖{v,0,t,1}); all pure; root loops come out as squares of twists about short segments (e.g. root (3−√5)/2: σ⁴ on [v,0]). Finite-quotient test: G_0-orbits on Hom(F_4,S_m)/conj (m=4,5) almost always coincide with full pure-braid orbits, and every candidate tested lay in the G_0-orbit — so FINITE QUOTIENTS ARE USELESS here (dead end).
2. KEY NEW IDEA (linking-number proof; full sketch in round3_q1..q4): 
   - Fibrewise formula: fixing the A-configuration (0,∞,1,t) and moving v', the pulled-back A-modulus w (cross-ratio of c_1 and the marked preimages of a_2,a_3,a_0 for z↦v'+z²) satisfies v' = V_t(w) = −((w−1)²−t)²/(4w(w−1)(w+t−1)). V_t is a degree-4 Galois cover P¹_w→P¹_v, deck maps g_0(w)=(w+t−1)/(w−1), g_3(w)=(1−t)(w−1)/(w+t−1); V_t(t)=v(t) (sympy). Points over a_1: w∈{0,1,∞,1−t}; over a_0: 1±√t; over a_2: ±√(1−t); over a_3: roots of w²+2(t−1)w+1−t. So f^* on a fibre of i_* is (the lift of) the coordinate w itself, and f^*τ never lies over 1−t.
   - Ψ=(i_*,f^*): Teich(B)→H×H, D_f=Ψ^{-1}(diagonal). Lifts of {q=1−t} are graphs q=g(p), g∈Γ(2)S Möbius (λ(−1/τ)=1−λ(τ)); Ψ avoids them all; a graph meets the diagonal iff g elliptic. For g non-elliptic, H_1(H×H∖Γ_g)=Z; a path in D_0 from τ to T^mτ maps into the contractible diagonal, a fibre path maps to a loop winding ±m around g(p0): contradiction unless m=0.
   - Curve: arcs α from v to a_1 ↔ lifts β in the w-sphere from w=t0; T_{∂N(α)} ∈ G iff β ends at 1−t0 (consistent with 3/0); g determined by the class of β in C∖{0,1}. Straight segment [t0,1−t0] ↦ g=S elliptic (cusp curve γ0). Loop around 0 then segment ↦ g=T^{±2}S parabolic ⇒ infinite orbit.
   - Explicit at t0=1/4: β = lower half of |w|=1/4 (1/4→−1/4), upper half of |w−5/32|=13/32 (−1/4→9/16), lower half of |w−21/32|=3/32 (9/16→3/4). Numerically α=V∘β is simple (β disjoint from g_i(β)); α leaves v=−25/96 into the lower half plane, crosses R upward in (1,∞) at ≈1.378, downward in (0,1/4) at ≈0.088, upward in (v,0) at ≈−0.019, then stays in the UHP to ∞. Numerically f^{-1}(α) does not separate a_1,a_2,a_3 (3/0 ✓); the real arc [−∞,v] is 2/1 ✓; the straight-segment arc is 3/0 ✓.
   Status: all OPEN (ledger, round3_plan) until a worker writes and checks the proof. Possible weak points to watch: marking conventions making both coordinates of Ψ the same Teich(A); λ-normalization; rigorous simplicity of α.

## Dead ends
- H_1(M_{0,5}) abelian obstruction (full rank). Finite quotients S_4,S_5 (G_0 orbits = full orbits). Pillowcase/Heisenberg/Q-type quotients (K contains a conjugate of ℓ_1 and conjugates of ℓ_j², so any quotient that collapses conjugacy classes kills the test). Forget-one-point maps to M_{0,4}: images have finite index. "Twist monodromy ⇒ peripheral loop" lemma: false in general (local branched examples). Recollection of Hironaka–Koch.

## Open gaps
1. Rigorous write-up of the linking-number proof (Steps 1–4 of the sketch), especially the Teichmüller identifications.
2. Rigorous proof that α is simple with the stated real-line pattern (or a cleaner equivalent arc); mapping-class description as a check.
3. Optional: {v,a_j} variant with k=2 (fits the problem's "power"), and the covering-space formulation π_0(D_f)≅π_1(U)/K as an "other routes" item.

## Next round
Round 3 wave (4 attempt queries, all carrying the sketch): q1 full rigorous write-up; q2 explicit-curve verification (simplicity, λ-lift sign, 3/0 check, mapping-class description); q3 structural covering formulation + general criterion + {v,a_j} k=2 family; q4 hostile referee of the sketch. When a complete written proof returns, write PROVED [GOAL] and send two verify queries spliced verbatim from the best answer file.
