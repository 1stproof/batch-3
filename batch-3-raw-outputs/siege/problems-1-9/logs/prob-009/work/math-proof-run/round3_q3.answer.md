# round3_q3 — answer (partial; no complete proof)

## Interpretation adopted
Closure of 𝒱 in M̄_g × Δ is analytic with fibre over t equal to closure(V_t); Δ_Γ ≅ ∏ M_{g_j,n_j} (no finite quotient); we work on a fine finite cover (level ≥ 3) so M̄_g may be treated as a smooth space with normal-crossing boundary.

## What is proved

**Lemma 1 (holomorphy).** t ↦ Y_t is holomorphic Δ → M_{g_i,n_i}.
Proof: closure(𝒱) ∩ (Δ_Γ × Δ) is analytic; its image under π_i × id is {(Y_t,t)}. The map is proper over relatively compact pieces of Δ: the closure of ∂V_t in M̄ meets deeper strata only where factor i stays in M_{g_i,n_i}, since π_i is constant along ∂V_t. So Remmert's proper mapping theorem (cited from memory) makes the image analytic. An analytic set that is the graph of a map from a disc is the graph of a holomorphic map. ∎
Consequence: the claim is equivalent to Y_t being locally constant near t=0 (identity theorem), or to {Y_t} being countable.

**Lemma 2 (conditional rigidity reduction).** Let S = closure(V_0) with boundary D, and N^log = T_{M̄_g}(−log ∂)|_S / T_S(−log D) (well defined where S is log-transverse to the strata; hypotheses (i),(ii) are what make the family a log/stratum-preserving deformation). If H^0(S, N^log) = 0, then the germ of the log-Douady space at [S] is a single (possibly non-reduced) point. Every reduced disc through it is then constant, so V_t = V_0 and Y_t = Y_0.
(Standard deformation theory, cited from memory. I have not verified it rigorously at non-transverse boundary points.)

**Lemma 3 (countability route).** If every V_t is totally geodesic, the claim holds. Reason: totally geodesic subvarieties are countable (Wright; Eskin–Mirzakhani–Mohammadi, cited from memory), and a continuous family taking countably many values is constant.

**Observation 4 (local arguments are insufficient).** Near ∂V_t, take coordinates (y, z, s) with y ∈ M_{g_i,n_i}, z on the other factors and s plumbing parameters. A germ y = Y_t + O(|s|) with Y_t any holomorphic arc meets every local condition imposed by (i) and (ii). Hypothesis (ii) is tautological along {Y_t} × closure(C_t). The local monodromy (Dehn twists about the pinched curves) does not see Y_t either. So any proof must use a global property of closure(V_t), such as Hodge-theoretic rigidity of the rank-4 sub-VHS W from Wright/Filip, or the vanishing in Lemma 2.

## Open (the single missing lemma)
Show that H^0(S, N^log) = 0 for totally geodesic surfaces S. A weaker sufficient statement: every log deformation of S keeps the constant factor fixed to all orders. Vanishing of the first-order component alone is not enough, since Y_t = Y_0 + t²v is possible.

I could not prove this lemma, and I found no counterexample. Possible routes:
- a negativity statement for N^log via the Hodge/Higgs decomposition of Q(X) along V_0;
- rigidity of the lower-level datum (Y_0 with its lower-level differential, which is Belyi-type in covering constructions) together with persistence of W over V_t.

Neither route is carried out here. The claim as posed therefore remains **unproved** in this answer.

=== END OF ANSWER round3_q3 ===
