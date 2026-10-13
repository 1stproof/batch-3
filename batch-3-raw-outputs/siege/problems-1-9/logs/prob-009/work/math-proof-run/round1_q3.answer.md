# round1_q3: partial answer. The claim is not proved.

## Interpretation
"Smoothly trivial" is read as follows: there is a diffeomorphism $\mathcal V\cong V_0\times\Delta$ that commutes with the projection to $\Delta$. Under hypothesis (i), the family $\partial\mathcal V:=\{(x,t): x\in\partial V_t\}$ is a smoothly trivial family of curves in $\Delta_\Gamma$.

## Proved
**Lemma 1.** The map $t\mapsto Y_t$ is holomorphic, from $\Delta$ to $\mathcal M_{g_i,n_i}$.

*Proof.* The closure $\overline{\mathcal V}\subset\overline{\mathcal M}_g\times\Delta$ is analytic, because $\mathcal V$ is the regular part of an analytic set; this is the hypothesis implicit in the phrase "closures of subvarieties". So $\partial\mathcal V=\overline{\mathcal V}\cap(\Delta_\Gamma\times\Delta)$ is analytic, and $\Pi:=(\pi_i\times\mathrm{id})(\partial\mathcal V)$ is the graph $\{(Y_t,t)\}$. We can choose a local holomorphic section $t\mapsto x_t\in\partial V_t$ through a smooth point of $\partial\mathcal V$ where $\partial\mathcal V\to\Delta$ is a submersion. Such points exist because the family is smoothly trivial and of relative dimension 1. Then $Y_t=\pi_i(x_t)$ is holomorphic near each $t$, hence holomorphic everywhere. ∎

So the claim is equivalent to $\frac{d}{dt}Y_t\equiv 0$.

## Where the suggested plumbing-coordinate route breaks
Near a generic point of $\partial V_t$, choose coordinates $(y,z,s)$:
- $y$ on $\mathcal M_{g_i,n_i}$,
- $z$ on the other factors,
- $s=(s_e)$ the plumbing parameters.

Then $\overline V_t$ is a 2-dimensional germ that contains $\{y=Y_t\}\times C_t\times\{0\}$.

For $t=0$, the theory of orbit closures says the plumbing parameters along $\overline V_0$ are related by $s_e=c_e\sigma^{m_e}$. These are cylinder/twist relations, recalled from memory: Mirzakhani–Wright, "The boundary of an orbit closure", and Chen–Wright. Moreover, $y$ restricted to $\overline V_0$ equals $Y_0+O(\sigma)$.

For $t\neq0$, $V_t$ is an arbitrary holomorphic deformation. Hypotheses (i) and (ii) constrain only:
- the topology of $\overline V_t\cap\Delta_G$ for each stratum,
- the incidence relations between these intersections across strata.

Neither of these involves the value of $y$. Concretely, the deformation $\overline V_t$ given by $y=Y_t+O(\sigma)$, with $Y_t$ any holomorphic curve through $Y_0$, satisfies every local constraint that (i) and (ii) impose near $\partial V_t$.

So any proof must use global information. The candidates are:
- **(a)** points of $\overline{\partial V_t}$ in deeper strata $\Delta_{G'}$. There, other boundary components of $\overline V_t$, on which factor $i$ might not be constant, pass through the same point. Hypothesis (ii) keeps these incidences, so if such a component's closure pins down the factor-$i$ coordinate, $Y_t$ is pinned down too.
- **(b)** a rigidity of the totally geodesic $V_0$ that propagates to its boundary.

Neither (a) nor (b) follows from the hypotheses as stated without further input. In (a), the other components also move with $t$.

## Missing lemma (precise)
**Missing Lemma.** Let $\overline V_t\subset\overline{\mathcal M}_g$ be a family satisfying (i) and (ii). Suppose $\pi_i(\partial V_t)=\{Y_t\}$, and let $Y_t$ be the corresponding point of $\overline{\mathcal M}_{g_i,n_i}$. Then the incidence structure of $\overline V_t$ in the boundary forces the point $Y_t$ to be one of finitely many points: for example, a point cut out by intersecting boundary curves of $\overline V_t$, whose number is fixed by (ii).

Lemma 1 together with the Missing Lemma gives the claim: a continuous map $t\mapsto Y_t$ into a finite set is constant on the connected disc $\Delta$.

I could not prove the Missing Lemma. I could not build a counterexample either, because a counterexample needs an actual analytic deformation of the closure of a totally geodesic surface that moves $Y_t$ while keeping (i) and (ii). Building one is the remaining open question.

## Status
- **Proved:** Lemma 1, and the reduction of the claim to the Missing Lemma.
- **Shown:** the local plumbing analysis alone cannot prove the claim.
- **Open:** the claim itself.

=== END OF ANSWER round1_q3 ===
