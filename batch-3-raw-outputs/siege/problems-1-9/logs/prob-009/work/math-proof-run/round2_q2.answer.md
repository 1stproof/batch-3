# round2_q2: rigidity of 2-dim totally geodesic V_0. Partial answer; the main question is still open

## What is proved (reductions)
A. (Checked from context item 1.) t -> Y_t is holomorphic. Reason: closure(𝒱) ∩ (Δ_Γ × Δ) is analytic. Its image under π_i × id is analytic by Remmert's proper mapping theorem. That image is a graph over the disc, so it is the graph of a holomorphic map. So the claim is equivalent to: the set {Y_t} is countable, or dY_t/dt ≡ 0.

B. If V_t is totally geodesic for all t, the claim follows. Totally geodesic subvarieties of M_g form a countable set. This is cited from memory: Wright, "Totally geodesic submanifolds of Teichmüller space", identifies them with GL(2,R)-orbit closures of (quadratic) differentials; Eskin–Mirzakhani–Mohammadi show there are countably many orbit closures. A continuous family drawn from a countable set is constant. So V_t = V_0, and hence Y_t = Y_0.

C. If V_0 is rigid (every family as in the problem is constant), the claim follows trivially.

D. Hypotheses (i) and (ii) give no constraint on Y_t near ∂V_t (context items 2–4, which I re-checked and accept). So any proof must be global: it must use the whole compact surface closure(V_t).

## What is not proved
- R1 (an Arakelov-type characterization of total geodesicity for surfaces): I know no theorem from the literature, even from memory, that characterizes a 2-dimensional totally geodesic subvariety by a numerical equality of degrees on a compactification. Möller's argument for Teichmüller curves uses maximal Higgs field on a curve. For a surface, the analogue would be that the Higgs field of the rank-2 piece W is an isomorphism T_V ≅ Hom(W^{1,0}, W^{0,1}) on the whole surface. That is an open condition, not a closed numerical one. I could not show that it is preserved by the deformation. Gap: the missing lemma is "for the sub-VHS W over V_t, which persists because the monodromy is fixed, maximality of the Higgs field is characterized by an equality of Chern numbers of logarithmic bundles on closure(V_t)". I have not proved it, and I do not know it to be true.
- R2: I did not compute the normal-sheaf cohomology.
- R3: I did not find a counterexample. Covering-construction loci are images of Hurwitz spaces under fixed maps. That makes them rigid *as covering-construction loci*, but it does not rule out deformations as abstract subvarieties of M_g.

## Status
Open. The claim holds whenever V_t stays totally geodesic (B) or V_0 is rigid (C). In general the problem reduces exactly to the missing rigidity lemma stated above.

=== END OF ANSWER round2_q2 ===
