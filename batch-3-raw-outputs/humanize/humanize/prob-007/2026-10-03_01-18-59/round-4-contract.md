# Round 4 Contract

## Mainline Objective

Repair the rigor defects in the newly added `lem:allpairs` (round-3 review
Finding 1), a self-contained AC-2/AC-3 issue that does NOT touch the headline
results:

(a) State explicitly how Ψ extends to words in E_f — via the
    anti-homomorphic (reversal) composition rule Ψ(σ1σ2)=Ψ(σ2)Ψ(σ1) already
    proved in sec:content — and JUSTIFY the image equality Ψ(E_f) =
    ⟨Ψ(a_0),Ψ(a_2)⟩ = PMCG(A) via the reversal-coincidence on the
    generators a_0,a_2 (Ψ(x_i²)=e reversal-invariant; reversal of a word in
    a_0,a_2 maps to the reversed word in u_0,u_2, and ⟨u_0,u_2⟩ is closed
    under reversal), so the set-equality of image groups is proved, not
    asserted.

(b) Replace the undefined-quantifier `Ψ(x_i)=e` by the proved
    `Ψ(x_i^{∘2}) = e` throughout (lem:allpairs, prop:contenttable), or define
    Ψ for a non-liftable twist only via its square's lift; remove `x_i`
    (i≠1) from the E_f generator set, keeping only the liftable powers
    (x_1, x_i^{∘2}, a_j).

(c) Define `\Ef` ONCE, early (start of §sec:content), with a single
    consistent generator set used everywhere; explicitly reconcile the
    adjacent `a_j = T_{{p_j,p_{j+1}}}` with the non-adjacent census twists
    `u_i = T_{{p_i,p_3}}`, stating that both maps (under descent) to the same
    generators of PMCG(A) on A.

## Target ACs

- AC-2 (no undefined quantifier: Ψ(x_i) never written for a non-liftable
  twist; Ψ's extension rule stated)
- AC-3 (the image-equality Ψ(E_f)=PMCG(A) is proved via the stated
  reversal-coincidence, not asserted; notation consistent, \Ef defined once)

## Capability Anchor

N/A (the plan contains no `## Feature Map / Capability Map` section).

## Blocking side issues in scope

- Only round-3 review Finding 1 (lem:allpairs (a),(b),(c)) — it is the single
  blocking side issue; it gates AC-2/AC-3 sign-off.
- Finding 2 (cheap confirmation): re-read prop:contenttable(b) to confirm no
  semantic remnant of the deleted "conjugates of H" clause survives and the
  load is carried by the essential-twist / free-action argument. Fold into
  the same edit.

## Queued side issues explicitly out of scope

- Exact `#pi_0(D_f) ∈ {2,4}` (unused; leave unpursued).
- Do NOT touch the component count `{2,4}` or the orbit verdict — they are
  correct (round-3 review confirmed).
- Do NOT chase the all-sheets equality `D_f = π^{-1}(M_f)` — correctly
  abandoned and unused.

## Round success criteria

1. `lem:allpairs` states the anti-hom extension and proves Ψ(E_f)=PMCG(A)
   via the reversal-coincidence; uses only `Ψ(x_i^{∘2})=e` (never `Ψ(x_i)`)
   and a consistent E_f generator set (x_1, x_i^{∘2}, a_j).
2. `\Ef` is defined exactly once, early in §sec:content; `u_i` vs `a_j`
   reconciled explicitly; no use of `\Ef` before its definition.
3. `prop:contenttable` uses `Ψ(x_i^{∘2})=e` and a consistent generator set;
   its (b) is carried by the essential-twist / free-action argument with no
   conjugacy remnant.
4. `pdflatex` ×2: 0 errors, 0 undefined refs, ≤ 16 pages.
5. Committed; round-4 summary + goal-tracker mutable section updated.
