# round2_q4: attempt on GH => h_top = 0 by topological-dynamics routes

## Status: NOT settled. No route (R1)-(R3) is completed. Below: one rigorous small observation, plus the exact gaps.

### Observation P (proved). How a periodic orbit interacts with GH.
Let γ be a closed orbit of period T, and let ν be a smooth positive density with d = div_ν X. The invariant measure μ_γ = ∫_0^T δ_{γ(t)} dt is a distribution density with L_X μ_γ = 0. As a distribution *function* u = μ_γ/ν it satisfies Xu = −d·u. This is a distribution supported on γ, so it is never smooth when dim M ≥ 2. Replacing ν by e^{a}ν (or using the time change hX, which by (O4) keeps GH) changes d into d + Xa (resp. h d + Xh). Restricted to γ, the equation d + Xa = 0 is solvable iff ∫_0^T d(γ(t)) dt = 0. That integral is the log of the Jacobian of the Poincaré return map, so this holds only when the Poincaré map preserves volume.
**Conclusion (proved):** if GH holds and dim M ≥ 2, X has no periodic orbit along which the linearised return map has Jacobian determinant 1. (Proof: if ∫_γ d = 0, pick a with d + Xa = 0 on γ. Then for ν' = e^{a}ν, div_{ν'}X vanishes on γ, so u = μ_γ/ν' satisfies Xu = −d' u = 0 (d' vanishes on supp u, and d'u as a product of a smooth function with a measure is 0). Hence u is constant by L1, which is a contradiction.)
This does not exclude dissipative periodic orbits. Horseshoes, and so positive entropy, can occur where all periodic orbits are dissipative. So P does not reach the goal.

### Gaps per route
- (R1) Uniform rigidity: I have no argument that GH forces a sequence t_n with g_{t_n} → id. The only lever is the tame estimate plus the triviality of the kernel, and dead end (ii) shows that tame estimates alone are consistent with Anosov flows. The missing step is turning *surjectivity onto the annihilator of invariant densities* into recurrence.
- (R2) Asymptotic pairs: the distribution w = ∫_{−∞}^0 (δ_{g_t x} − δ_{g_t y}) dt has a right-hand side δ_x − δ_y. To make it smooth one has to average over a family of pairs that is smooth in a full-dimensional parameter (n parameters), with smooth dependence of the stable/unstable holonomy. Pesin theory gives only measurable families with absolutely continuous (Hölder) holonomies, not smooth ones. So the needed regularity is "C^∞ dependence of the pairing on a transversal family", and positive entropy does not supply it in general. Open.
- (R3) Volume growth: no estimate was obtained. The loss of derivatives in the tame estimate (dead end iii) defeats the naive pushforward argument.

### Final statement
Proved: Observation P only. Open: the claim GH ⇒ h_top(g_t) = 0 (this is closely tied to the Greenfield–Wallach/Katok conjectures; recalled from memory, it is not known in general).

=== END OF ANSWER round2_q4 ===
