# round1_q2: partial answer. The claim is not settled.

## Proved (elementary)
1. **t -> Y_t is holomorphic.** The closure of the total space V in \overline M_g x Delta is analytic. Its intersection with Delta_Gamma x Delta is the family {∂V_t}. By (i) this family is smoothly trivial, and it is an analytic set. Composing with pi_i x id gives an analytic set {(Y_t, t)}. This set is the graph of a continuous map, so the map is holomorphic: an analytic set that is the graph of a continuous map over a disc is the graph of a holomorphic map (Riemann extension / graph theorem).
2. **∂V_t is a boundary curve of closure(V_t), not a limit of other boundary curves.** It has dimension 1, and the boundary of a 2-dimensional analytic set inside the boundary divisor has dimension at most 1. Hypothesis (ii) therefore only constrains the finitely many points of {Y_t} x (closure(C_t) \ C_t), and how these points lie on the closures of other boundary curves. Here C_t = projection of ∂V_t to the remaining factors.

## Where the soft hypotheses stop
Hypotheses (i) and (ii) are purely combinatorial and topological. They say that the incidence pattern of boundary pieces stays constant. A holomorphic motion of the point Y_t (via item 1) changes no incidence pattern. In every deeper stratum the point keeps its graph type, and the factor coming from Y_t either stays the same or degenerates in the same way for every t.

So (i), (ii), holomorphy and compactness cannot force dY_t/dt = 0 unless some rigidity property of Y_0 is added. I have **not** built a rigorous global counterexample: a surface in M_g whose deformations move Y_t while keeping (i) and (ii). This is open.

## Missing lemma (the input the totally geodesic hypothesis must supply)
**Lemma (needed).** If V_0 is totally geodesic and ∂V_0 is constant equal to Y_0 on the factor M_{g_i,n_i}, then Y_0 is determined by discrete data attached to the boundary incidence pattern that (i) and (ii) preserve.

Here is one possible route to this lemma, stated from memory and not checked:
- Totally geodesic subvarieties come from GL(2,R)-orbit closures. By Mirzakhani–Wright and Chen–Wright, the boundary of an orbit closure in a constant factor carries a zero differential, or lies in a smaller orbit closure. By Eskin–Mirzakhani–Mohammadi and Filip, orbit closures are defined over Q-bar.
- From this, Y_0 would be pinned down by the discrete data that (i) and (ii) preserve. For example, Y_0 could be cut out as an isolated point by the closures of other boundary curves through the deeper points.

But **this does not follow**. V_t is not totally geodesic for t ≠ 0, so Q-bar-rationality and isolation of Y_0 say nothing directly about Y_t. One would additionally need that, for every t, Y_t is cut out by the same intersection conditions, and that these conditions have isolated solutions. I could not establish this.

## Status
- Proved: items 1 and 2.
- Open: the main claim. It reduces to the missing lemma above, together with the claim that the conditions which isolate Y_0 persist for every t.
- Not attempted: a rigorous counterexample showing that the claim fails without the totally geodesic hypothesis.

=== END OF ANSWER round1_q2 ===
