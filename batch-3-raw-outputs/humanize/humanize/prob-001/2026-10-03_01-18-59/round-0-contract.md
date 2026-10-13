# Round 0 Contract

## Mainline Objective

Produce a rigorous, self-contained, standalone LaTeX solution in
`solution.tex` resolving the exact question of `problem.tex`: whether, for the
inclusion $B_P^{\rm op}\subset A_P^{\rm op}$ (birhizomic topology on $A_P^{\rm
op}$, trivial topology on $B_P^{\rm op}$), the unit
$F \to \mathrm{R}\pi_*\pi^{-1}F$ is a quasi-isomorphism for every presheaf of
abelian groups $F$ on $B_P^{\rm op}$. The document must either prove the
affirmative answer in full, or give a completely rigorous counterexample.

## Target ACs

- AC-1 (answers the exact question, every claim proved)
- AC-3 (audited for logical direction, quantifiers, degeneracies, consistency
  with `problem.tex`)

## Capability Anchor

N/A (plan.md contains no Feature Map / Capability Map section)

## Blocking Side Issues in Scope

None.

## Queued Side Issues out of Scope

None.

## Round Success Criteria

1. All definitions (infinitesimal map, birhizomic-at, birhizomic cover, face
   $\Phi_T$, the Lan formula) normalized; conventions verified against
   `problem.tex`.
2. A complete proof or counterexample with no gap: injectivity+gluing of every
   relevant Čech complex for the sheafified left Kan extension, vanishing of
   higher $R^i\pi_*$ on the class $\pi^{-1}F$, and the conclusion.
3. `solution.tex` compiles with `pdflatex`, uses only standard packages, and
   is at most 16 typeset pages.
4. Round committed with a descriptive message; round-0-summary.md written.
