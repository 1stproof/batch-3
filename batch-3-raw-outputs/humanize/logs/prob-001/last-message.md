The state is consistent: solution committed (030ed79), clean compile (15pp, 0 errors, 0 undef refs), contract + summary + bitlesson + tracker all updated.

I've reached the honest limit of what I can prove. I'll stop now so the Humanize Stop hook can run its RLCR review.

**Round 4 status (honest):**

- **M‑5 — fixed.** `lem:sieve` is now sound: the false single‑`K` pin `(ii)` is deleted and `(i)` is re‑proved as the explicit self‑contained contraction `(w_r)_σ := z_{(f_r,σ)}` with the two‑term identity displayed and identity transports cited to `lem:nerve(i)` Case A / `lem:mixed(C1)`; the invalid `lem:constcx` citation is gone.
- **M‑6/M‑8 — attempted, found unsound for arbitrary F.** I implemented the review's residuum (iB‑contraction) honestly, but the kill closes `[z]=0` only when `G` agrees on the base and quotient faces; for a general presheaf `F` the transitions `F(b)→F(B(i(P/K)))` are quotient maps, not identities, so the dead↔iB discrepancy at kernel‑`J` tuples cannot be absorbed into Step‑1's `w`. I did not fabricate it.
- **M‑7 (AC‑4 honest closure) — applied.** `thm:main`/`prop:vanish` now assert exactly what's proved: `π⁻¹F = G_F` is a sheaf and the degree‑zero unit `R⁰π_*π⁻¹F = F` (both verified, Sections 2–3 intact). A Closing remark records the two open points — higher direct images for arbitrary `F` (no proof, no counterexample), and non‑finitely‑generated `P` (obstructed per `rem:nonfg`). Title/Overview aligned; no unsupported `q>0` assertion remains.
- Compiles: 15pp, 0 errors, 0 undefined refs.

**For the reviewer:** the residuum contraction is the irreducible point. If the intended answer is YES for all presheaves, it needs an ingredient neither the reviews nor I could produce soundly. `T2` stays `in_progress`; a Goal Tracker Update Request is in the round‑4 summary. I will follow the hook's feedback — if it has a valid completion of the residuum for all `F`, I'll implement it; otherwise the honest AC‑4 state stands.