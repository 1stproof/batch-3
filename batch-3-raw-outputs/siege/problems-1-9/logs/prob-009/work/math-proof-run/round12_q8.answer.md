kind: answer (round12_q8)

**Plan/status.** Status: PARTIAL. I do not exclude (γ°)/(IMOV_Q), and I do not construct a counterexample. What this file does:
- §2 makes the sketched part of round11_q7 §5 precise and proves it. It turns (γ°) into a configuration stated purely in terms of the (Rig) data (M_W, K_W) of one lifted family W: the "frozen twin" and "Y inside a fixed curve" (Lemmas 1–4).
- §3 proves an extra rigidity statement: α-symmetry holds on all of K_W except for mixed pairs (Lemma 5).
- §4 explains why these data contain no contradiction by themselves, and states the precise residual open statement (O-γ°′).

Readings: (R1), (R2) with H_0 = id, (Rig), and Y non-constant (for contradiction), as in the task file. Cited inputs are used as stated in the task file and were not re-proved:
- R8-2 Lemma U and corollary U3;
- R8-3 Theorem N;
- round10_q7 Lemma I0 (every sheet contains a lift-curve);
- round11_q3 Lemma 3.1 and Prop. 3.2;
- (K3): F_y(hp) ≅ F_{h^{-1}y}(p) for h ∈ Aut(Q);
- R7-3 Lemma 1 (values of constant vertices are holomorphic in t).

## 1. The configuration (γ°), restated

The data are as follows.
- X is the 3-fold component of Lemma D1, and D = X ∩ {N = 0}.
- T_1 ≠ T_2 = gT_1 are sheets of D, with g ∈ Aut(Q).
- C ⊂ T_1 ∩ T_2 is an irreducible curve germ at (0,0), finite over Δ_ε, with C ⊂ Fix(g).
- x ∈ Π(T_1), i.e. x is Y-persistent on T_1.
- P := P(T_1) = P(T_2) = gP.
- For t outside a countable set Z″ and r ∈ C_t, x is non-constant along the branch of T_{2,t} through r, and q(r) lies in the stratum Δ_{G_c} of the coarse piece of T_1.

Further notation.
- c̃ := T_1 ∩ {t = 0} is a lifted branch of a branch c of B_0 at Q.
- Q is a puncture of the piece of c (round11_q3 Lemma 3.1: Q ∉ Δ_{G_c}).
- G_c is G_Q with the edges outside P contracted. Since gP = P, g induces an automorphism α of G_c.
- Π: L_P → ∏_{w∈V(G_c)} M̄_w is the partial normalisation map (holomorphic into ∏M_w off the locus where extra edges are pinched).
- By round11_q3 §3.6 / Lemma U, (Π, t)(T_1) lies in a 2-dimensional component W of the lifted family of the piece of c. Every fibre component is K_W × {c_t}: the coordinates in M_W run over the fixed curve K_W, and the coordinates w ∉ M_W are constants c_t[w], holomorphic in t (R7-3 Lemma 1).
- Since x is persistent on T_1, the vertex {x} is constant on the fibres, so x ∉ M_W and c_t[x] ≅ Y_t.

## 2. Proved consequences of (γ°)

**Lemma 1 (the moving twin).** Put u := g^{-1}x. Then:
1. u is intact at every point of T_1, so {u} is a single vertex of G_c;
2. F_u(p) ≅ F_x(gp) on T_1;
3. u ≠ x, and u ∈ M_W, i.e. u is a moving vertex of the fibres of W.

*Proof.*
- The edges at x lie in P, because x is intact on T_1. Hence the edges at u = g^{-1}x lie in g^{-1}P = P. The pattern at every point of T_1 contains P (closed condition), so u is intact on T_1. This gives item 1.
- Item 2 is (K3).
- For generic t, x is non-constant along T_{2,t} = gT_{1,t}. By item 2, F_u is then non-constant along T_{1,t}. Since F_x is constant along T_{1,t}, we get u ≠ x. Since u is non-constant on the fibre components for uncountably many t, U1 of Lemma U gives u ∈ M_W. ∎

**Lemma 2 (the coarse branch has two distinct lifts at 0).** g c̃ ≠ c̃. Both are lifted branches of c through 0, contained in T_2 and T_1 respectively.

*Proof.* Along c̃, F_x is constant (≅ Y_0). Along g c̃, F_x(gp) ≅ F_u(p) for p ∈ c̃, and F_u is non-constant along c̃ because u ∈ M_W and U1 applies at t = 0 too. ∎

**Lemma 3 (frozen twin at the lift-curve).** Let λ ⊂ T_1 be a lift-curve (it exists by I0), so q(λ(t)) = Q_t. Then for all small t:
- F_u(λ(t)) ≅ Y_0;
- F_x(λ(t)) ≅ Y_t.

So Q_t has two distinct components (labels x ≠ u), isomorphic to Y_t and to Y_0. Moreover Y_0 = pr_u(κ_0) for a point κ_0 ∈ K_W ∩ ∂(∏_{w∈M_W} M̄_w) at which the u-coordinate is interior.

*Proof.*
- **Intactness.** By Lemma 1, u is intact at λ(t), and F_u is continuous on L_u ⊃ T_1.
- **Limit points are punctures.** Let p_n ∈ T_{1,t} ∖ λ tend to λ(t), and let k be a limit point of Π(p_n) in ∏M̄_w. The gluing map ξ̄ is continuous, so ξ̄(k) = Q_t. Since H_t preserves strata and Q ∉ Δ_{G_c}, we have Q_t ∉ Δ_{G_c} = ξ(∏M_w). Hence k ∉ ∏M_w.
- **The M_W-part lies in a finite set.** The constant coordinates of k are the c_t[w] ∈ M_w. So some coordinate in M_W is in the boundary, and pr_{M_W}(k) ∈ F_W := K_W ∩ ∂, which is a finite set independent of t (U3).
- **The u-coordinate.** It equals F_u(λ(t)), by continuity of F_u. So t ↦ F_u(λ(t)) is a continuous function on the connected punctured germ λ ∖ {(0,0)} with values in the finite set pr_u(F_W) ∩ M_u. Hence it is constant, equal to its value at λ(0) = 0, namely F_u(0) ≅ F_x(g·0) = F_x(0) ≅ Y_0.
- **The x-coordinate.** F_x(λ(t)) ≅ Y_t because x is persistent on T_1 ∋ λ(t). ∎

This is the "rigid twin" of round11_q1 §4, now derived inside (γ°) itself.

**Lemma 4 (Y inside a fixed curve; round11_q7 §5 made precise).** Let 𝒴 be the image of pr_u(K_W) ∩ M_u in 𝔐 = M_{g_i,n_i}/S_{n_i}. It is a closed analytic curve in 𝔐. Then:
- Y(Δ) ⊂ 𝒴;
- Y_0 ∈ 𝒴, as the u-value at a puncture point κ_0 ∈ F_W;
- more precisely, for small t, Y_t = pr_u(κ(s(t))), with κ(s(t)) ∈ K_W tending to the points of F_W with u-value Y_0.

*Proof.*
- **Closedness of 𝒴.** K_W is compact, so pr_u(K_W) is closed analytic in M̄_u by Remmert. Its intersection with M_u is closed analytic there, and the image in the quotient by S_{n_i} is closed analytic.
- **Crossing points.** Let t be generic and r ∈ C_t. Since g fixes r, F_u(r) ≅ F_x(gr) = F_x(r) ≅ Y_t. Also Π(r) ∈ K_W × {c_t}, so Y_t ∈ 𝒴.
- **All of Δ.** This holds for co-countably many small t. The set 𝒴 is closed, so it holds for all small t. Then Y^{-1}(𝒴) is an analytic subset of Δ containing an open set, so it is all of Δ.
- **Limit of the crossing points.** As t → 0, r → (0,0), so Π(r) accumulates only at points of closure(Ê_0) over Q. These lie in F_W × {c_0} by the argument of Lemma 3. ∎

## 3. Symmetry forced on K_W

The point k_t := Π(r) is fixed by α, because g ∈ Stab(r). That is, k_t[αw] ≅ α_* k_t[w] for every vertex w of G_c, with the special points relabelled by α. Classify the vertices w by whether w and αw lie in M_W.

**Lemma 5.**
- (a) For every w with w, αw ∈ M_W, the identity κ[αw] ≅ α_*κ[w] holds on all of K_W.
- (b) For every w with w, αw ∉ M_W, c_t[αw] ≅ α_*c_t[w] holds for all t.
- (c) The only conditions that depend jointly on (κ, t) come from the mixed pairs. Among them is (u, x): pr_u(κ) ≅ c_t[x] = Y_t.

*Proof.*
- (a) The set A ⊂ K_W where the identities hold is closed analytic. It contains the points κ(s(t)) for co-countably many t. These points are pairwise distinct for distinct values of Y_t, since their u-coordinates are the Y_t, which take infinitely many values (Y is non-constant). So A is infinite, and A = K_W because K_W is an irreducible curve.
- (b) Both sides are holomorphic in t (R7-3 Lemma 1) and agree for co-countably many t. Apply the identity theorem.
- (c) This is what remains after (a) and (b). ∎

## 4. Why §§2–3 give no contradiction, and the residual statement

**No contradiction from these data alone.** Take local coordinates (s, t) on W near (κ_0, 0), where s is a local parameter of a branch of K_W at κ_0. Then:
- λ maps to {s = 0};
- c̃ maps to {t = 0};
- C maps into {f(s) = Y_t}, where f := pr_u∘κ and f(0) = Y_0.

If 𝒴 is a curve, Y is non-constant with Y(Δ) contained in the branch f(s), and every mixed pair (w, αw) gives an equation κ(s)[w] = φ_{αw}(t) that shares the solution curve s = s(t), then every constraint proved so far is met. So no contradiction follows from the (Rig) data, Theorem N, or the chart and sheet structure.

**Total geodesy cannot be applied directly.**
- At t = 0 the crossing points collapse into the puncture Q, where g ∈ Aut(Q) already exists. Total geodesy at t = 0 sees only that c̃ and g c̃ are two lifts of c through 0 (Lemma 2), with x constant on one and moving on the other.
- Theorem X*_all does not apply, because both sheets are of puncture type.
- The extra automorphism g of R_t = q(r_t) is not a topological invariant under the coarse reading (R2). So Lemma S cannot transport it back to t = 0.

**Residual open statement (O-γ°′), to which (γ°) is now reduced (equivalent data, by §§2–3).** Exclude the following:
- a piece E of B_0 with puncture Q, and a component W of its lifted family with (Rig) data (M_W, K_W);
- a Y-vertex x ∉ M_W and a moving vertex u ∈ M_W, exchanged by the automorphism α of G_c induced by some g ∈ Aut(Q);
- a puncture point κ_0 ∈ K_W ∩ ∂ with pr_u(κ_0) ≅ Y_0;
- such that Y(Δ) ⊂ 𝒴 = pr_u(K_W), and for all small t there is κ(s(t)) → κ_0 with (κ(s(t)), c_t) α-fixed. In particular, (a) and (b) of Lemma 5 hold, and every mixed pair satisfies κ(s(t))[w] ≅ φ_{αw}(t).

**Partial exclusion.** If dim M_{g_i,n_i} ≥ 2 and 𝒴 is a Teichmüller curve (the case where u is a max-speed vertex, Lemma PA / Prop. C), then Y moves along a Teichmüller curve in M_{g_i,n_i}. I could not exclude this.

## 5. Proved / not proved / open

**Proved** (under (R1), (R2), (Rig), Y non-constant, with the cited lemmas as inputs):
- Lemma 1 (moving twin u = g^{-1}x ∈ M_W);
- Lemma 2 (g c̃ ≠ c̃);
- Lemma 3 (frozen twin: F_{g^{-1}x}(λ(t)) ≅ Y_0 and F_x(λ(t)) ≅ Y_t for all t; Y_0 is a puncture u-value of K_W);
- Lemma 4 (Y(Δ) ⊂ pr_u(K_W), a fixed closed curve; this proves the sketched step of round11_q7 §5);
- Lemma 5 (α-symmetry on all of K_W for pairs inside M_W, and in t for pairs outside M_W).

**Not proved:**
- that (γ°) cannot occur;
- that (γ°) never obstructs MS11♭;
- MS11♭ itself;
- any counterexample.

**Open:**
- (O-γ°′) as stated in §4, equivalently "Y moves inside the fixed curve pr_u(K_W) with a frozen twin at the puncture";
- the (β)-twist obstruction (O-Bpure), untouched;
- (Rig) (entry 82), untouched.

=== END OF ANSWER round12_q8 ===
