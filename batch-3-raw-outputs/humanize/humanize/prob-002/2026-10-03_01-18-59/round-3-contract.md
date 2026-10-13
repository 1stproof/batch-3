# Round 3 Contract (post review-phase audit #5)

## One mainline objective
Close the three blocking upper-bound defects in Prop. 5.1 so the minimax
upper bound is a complete proof, while keeping the (already-sound) lower
bound and answer `n^{-2α/(2α+d+2)}` (log-free) intact:

- **P1 (rδ^α discrepancy, lines 1460–1474, 1490–1494).** The crude
  `‖e∇u_m‖_{H^{-1}} ≤ ‖e∇u_m‖₂ ≤ r‖∇u_m‖_∞` boundary-collar estimate
  injects a non-absorbable `rδ^α`, breaking the δ∗ balance. Fix by the
  interior/boundary split actually available for the Darcy Green's
  function: decompose the collar `{|x|>1−δ}` (using smallness of `e` in
  `L^p`, `p>d`, against `1/dist(x,∂D)`) from the interior (gain `δ`);
  split off the PDE error `w_2=u_{f_0}−u_{T_δf_0}` from the wavelet
  smoothing `u_{T_δf_0}−u_{f_{≤δ}}`. Target `‖Z‖₂ ≲ δ^{α+1} +
  δ^{α+d/2−1} ≤ δ^{α+1/2}` (and ideally `~δ^{α+1}` up to a log, absorbed
  into "up to logarithmic factors"), eliminating every `δ^{α−k}`, `k≤1`,
  boundary term with an explicit mechanism.

- **Origin-mode gap (eq:infsup / eq:infsupapp).** The current sieve spans
  *all* packets of scale `≥δ`, so `h` can live at the origin where the
  gain is only `≳δ²` — triangle subtraction against the `δ` terms fails.
  Fix by **bulk-projected sieve**: `F_δ` built from packets of scale
  `≥δ` supported in `dist(x,∂D) ≥ c₀` only, then set
  `Π_δf = 1 + (T_δf − 1)φ₀` (`φ₀` a fixed `{|x|≤1−c₀}` patch) so `m`
  keeps the C^α-regularity/low-frequency properties of `Π_δf` while `h =
  f̂−m` is bulk-supported by construction. Then `lem:invert`'s lower bound
  applies to the whole `h` (no origin modes remain), and the origin
  content is absorbed into the bias, whose `u`-image (after the P1
  interior/boundary/mollifier treatment) is `≪δ·δ^α` so it does not
  convert back to an `‖h‖` expression via `/δ`. Rewire
  `lem:invert`/`rem:modewise`/`eq:infsupapp` and the bias bookkeeping.

- **P2 (line-1518 accounting).** Recompute the final risk from the
  repaired `eq:basic`, carrying every bias/discrepancy term; show all are
  `≲δ^{2α}` at `δ∗` (no dropped `r²δ^{2α−2}`/`r²`).

## Target ACs
- AC-1 (upper-bound risk analysis is a complete proof: no unabsorbable
  boundary/bias term, no un-inverted mode class; no invented mechanism)
- AC-3 (quantifiers/thresholds/constants: r₀, δ₀, C_W, s/r₀ explicit;
  bias image demonstrated `≪δ⁻¹`-inversion threshold)

## Capability Anchor
N/A (plan has no capability map).

## Blocking side issues in scope
- P1 discrepancy/collar (above).
- Origin-mode sieve redefinition + `Π_δ`, `eq:infsupapp`, bias split.
- Sign-checks inside the collar integration-by-parts and the
  multipole/second-moment mechanism for general packets.

## Queued side issues (out of scope)
- Q-1 exact minimax log power (if a log labors the bias term).
- F-5 expository compression (cross-scale AO, `lem:invert`(i)).
- Q-2/Q-4/Q-5 page-economy/constant polish.

## Round success criteria
1. `F_δ`, `Π_δ` redefined so every `h = f̂−m` is supported in
   `dist(x,∂D) ≥ c₀`; `lem:invert`'s lower bound then yields `eq:infsupapp`
   uniformly on the sieve (the "handled identically / never inverted"
   sentence either removed or made true); `m` retains the C^α/apriori
   bounds used by `lem:quad` and `eq:opdiff`.
2. `eq:basic`'s right side no longer contains `rδ^α`; `‖P_δ(u_{f_0}−u_m)‖₂`
   bounded by the interior Poisson/mean-zero gain plus collar terms
   `≤δ^{α+½}` (and shown `≪δ^{α+1}` pre-inversion), with the collar
   `rδ^α` → `δ^{α+d/2−1}` replacement demonstrated using an `L^p`, `p>d`
   smallness of `e` and the radial Green profile.
3. Final risk display recomputed: all terms `≲δ∗^{2α}` at
   `δ∗=n^{−1/(2α+d+2)}` (or `δ∗^{2α}` × a log factor, recorded honestly);
   the "two terms of equal order" sentence made consistent.
4. Lower bound (Prop. 4.1) unchanged and still consistent with the new
   sieve/`Π_δ`; sign conventions (source `=1`) preserved throughout.
5. Two `pdflatex` passes clean, ≤16 pages, 0 undefined refs; tracker and
   round-3-summary updated; commits made.
