# Round 2 Recovery Contract (drift recovery)

## LATE CORRECTION (end-of-session; supersedes the "pinned convention" below)
The convention paragraph below ("evolved/antipode-dual pairing, S in the
FIRST Sweedler slot") describes an INTERMEDIATE round-2 world that was
itself discarded. The FINAL, axioms-verified world in solution.tex (and in
scratch/vrf.py: 333 PASS, derived from (PA),(P),(C),(S),(SK) only) is the
CLASSICAL Drinfeld-Tanisaki skew pairing with the standard recursion (PA)
(first line <u,yz>=<u1,y><u2,z>), the problem's symmetric values (P),
coproducts (C) on both Borels, and the skew product (SK) with S^{-1} on the
FIRST Sweedler slot: y x = sum <x_1, S^{-1}(y_1)> x_2 y_2 <x_3, y_3>.  This
world derives (vrf.py; no cross scalar hard-coded):
  (a) hK^{(-)}_i E_r = q^{-alpha_r(i)} E_r hK^{(-)}_i   (matches internal (H1));
  (b) hK^{(+)}_i F_s = q^{-alpha_s(i)} F_s hK^{(+)}_i    (matches internal (H1));
  (c) cross Cartans commute;
  (d) F_s E_r - E_r F_s = delta_rs th (cK_s^{(-)} - cK_r^{(+)-1}), so the
      diagonal quotient hK^{(+)}=hK^{(-)} reproduces printed (H1),(H2),(H3)
      and Omega_i = hK_i^{(+)} hK_i^{(-)-1} is central.
Two defects surfaced at session end (goal-tracker "Round 2, late"): (i) the
(PA) FIRST line in def:D is displayed with the (y,z) slots swapped relative
to the classical convention the engines/derivations use (display-order
repair; no mathematical content); (ii) a latent tuple-vs-index bug in
scratch/vfin.py's letter-grouplike crossing made every such crossing
evaluate to scalar 1, masking that the DERIVED arc relations are NOT
scalar-free.  The repair (the actual mainline work that follows) re-declares
def:A with the honest derived twisted relations (adjacent q-exchanges;
(M0)b with q^{alpha_j(i)}; (M1)p plain; recomputed (M2),(M3); minors
shifted by powers of q), proves well-definedness via the O_q(M_2)-block
presentation glued along the diagonal (Lê's O_q(M_n) triangular
identification, telescoping at every gap), and leaves Part 2 unchanged.

## Recovered mainline objective (exactly one)
Rebuild the target algebra of Part 1 as a presentation-explicit generalized
quantum double whose cross rules are derived from ONE machine-pinned sign
convention, so that (i) `D` is associative with the printed (P0)-pairing,
(ii) the diagonal quotient of `D` is exactly `H = U_q^{ext}(sl(n))` (printed
(H1),(H2),(H3)), and (iii) `S_n(B*) ≅ D` and `S_n(B*)/I ≅ H` hold with every
scalar re-derived from that convention.

## The pinned convention (decided by exhaustive exact enumeration, conv_enum/2/3.py)
UPDATE (final, after the full sweep over mirrorings x kernel antipodes x pairing
evolutions): no kernel convention over the PRINTED (input=B-, output=B+)
pairing gives an H-compatible diagonal quotient; the unique working
alternative forces the pairing to be used in its EVOLVED (antipode-dual) form
- still the standard Drinfel'd-Tanisaki skew pairing, descended to the
antipode-switched slots, which is precisely how the printed symmetric values
(both <E_i,F_j> and <F_j,E_i> equal delta theta) are realized. Concretely,
the document now prints: same coproducts (C) on both Borels; the pairing
recursion (PA) with the charged-letter minor in the S-twisted slot order;
and the skew product with S in the FIRST Sweedler slot:
  y x = sum <x_1, S(y_1)> x_2 y_2 <x_3, y_3>.
Derived rules (engine-verified, scratch/vhybrid.py: 430+ exact checks ALL PASS;
scratch/vfin.py rewrite-model cross-check):
  (a) hK^{(-)} E_r hK^{(-)-1} = q^{-alpha_r(i)} E_r
  (b) hK^{(+)} F_s hK^{(+)-1} = q^{-alpha_s(i)} F_s
  (c) cross Cartans commute
  (d) F_s E_r - E_r F_s = delta_rs th (cK_s^{(-)} - cK_r^{(+)-1})
  => diagonal quotient hK^{(+)}=hK^{(-)} reproduces printed (H1),(H2),(H3)
  => Omega_i = hK_i^{(+)} hK_i^{(-)-1} central (engine-verified).
Pairing-table consequences used by the paper proofs:
  <hK_i F_s hK_i^{-1}, E_r> = q^{+alpha_r(i)} <F_s,E_r>  (Cist1)
  <F_s, hK_i E_r hK_i^{-1}> = q^{-alpha_r(i)} <F_s,E_r>  (Cist2)
  <hK^u F_s, E_r> = delta th q^{+alpha_s(u)};  <F_s hK^u, E_r> = delta th
  <F_s, hK^v E_r> = delta th q^{-alpha_s(v)};  <F_s, E_r hK^v> = delta th.
NOTE the ORIGINAL demand list below (first enumeration) is SUPERSEDED by this
final convention; the demand structure (one sign convention, machine-derived)
is what survives.
Requirement set: (a) cross-Cartan conjugation `E K^{u(-)} = q^{+alpha_r(u)} K^{u(-)} E`,
(b) `K^{mu(+)} F = q^{-alpha_s(mu)} F K^{mu(+)}`, (c) cross Cartans commute,
(d) `E_r F_s = F_s E_r + delta_rs*theta*(cK_r^{(+)-1} - cK_s^{(-)})` so that the
diagonal quotient `hK^{(+)} = hK^{(-)}` gives printed (H1) and printed (H2).
Over the 4x3x3 grid (Borel mirrorings x antipode pair in the skew-product
kernel) x {input=F,output=E} x {input=E,output=F}, EXACTLY ONE combination
passes (a)-(d) at n=2,3 (engine-derived pairings):
  - cross product `y x = sum <x_1, S(y_1)> x_2 y_2 <x_3, y_3>` (S in the FIRST
    slot, bare pairing in the third),
  - standard coproducts (C) on both Borels, `Delta^2` as printed,
  - the pairing is USED "evolved": its nonzero root value is
    `<E_r, F_s> = delta_rs*theta` i.e. <input B+, output B-> (built with
    S(x), S^{-1}(y) on the two factors); the grouplike matrix (P0) is
    identical under the swap, so def:D states both conventions at once with
    the explicit pairing-evolution display.

Consequences (all to be re-derived in the document):
- lem:cross: (a) `hK^{(-)}E_r = q^{-alpha_r(i)} E_r hK^{(-)}`;
  (b) `F_s hK^{(+)} = q^{+alpha_s(i)} hK^{(+)} F_s`; (c) cross Cartans commute.
- prop:EF as in (d) above; diagonal quotient = H (printed signs); central
  loops are the DIAGONAL kind `Omega_i = hK_i^{(+)} hK_i^{(-)-1}`.
- def:phi now pins `s_{i+1,i} = hK_{i+1}^{(-)-1} F_i` and
  `t_{i,i+1} = E_i hK_{i+1}^{(+)}`: the mirror consistency computation then
  internally re-derives the S-first-slot kernel (this was the round-0/1
  ambiguity; now it is a theorem, not a choice).
- thm:mixed scalars: (a),(b) as before; (c) becomes `q^{+alpha_i(j)}`
  (inverse of round 1); (e) proof recomputed (net display of (M2) unchanged).

## Target acceptance criteria this round
- AC-1 (mainline): Part 1 and Part 2 proved against the rebuilt D with every
  cross-rule scalar channel-derived from (PA),(P),(C),(S),(SK) as now printed.
- AC-3 (verification): a rebuilt exact battery derived from the axioms only
  (pairing engine + rewrite engine parametrized by the printed rules),
  asserting engine-vs-engine differences; rem:verify states exactly what ran.
- Capability anchor: N/A (plan has no capability map).

## Root cause of the drift
Rounds 0-1 fixed the SK kernel by convention memory (S vs S^{-1} slot) instead
of deriving it; the two slots were then re-fixed mid-round, lem:cross's proof
developed two cancelling sign slips, and the 24 vtest FAILs that would have
caught the inconsistency (Omega-centrality) were dismissed as stale.

## Truly blocking issues
- B1: write def:D/(SK)/(S) in the pinned convention with the pairing-evolution
  paragraph; redo lem:T where orientation-sensitive (all values reproduced by
  engine), lem:compat, the DELTA2 display, lem:cross, prop:EF.
- B2: re-derive thm:mixed(a)-(e) + def:phi consistency proof under the new
  scalars (machine-assisted derivation, never hard-coded).
- B3: Part 2: lem:loops (diagonal Omega), lem:split, lem:diag (=H), thm:two.
- B4: rebuilt verification battery (vtest.py) in the same rule world as the
  paper: (M0)-(M3) exact/difference checks, Omega-centrality derived by the
  engine, minor images, diagonal commutator; rem:verify rewritten honestly.

## Queued (out of scope this round)
- Q1 scratch tidying; Q2 cosmetic LaTeX polish; Q3 any n=2-only extra checks.

## Success criteria that flip the verdict to ADVANCED
- solution.tex compiles, every cross-rule display is channel-derived in the
  pinned convention with no sign slip (the proof displays match the
  engine-derived values token-for-token);
- Omega-centrality and the diagonal quotient are proved and engine-verified;
- Part 1 (well-definedness incl. (M1') exponent +alpha_i(j)) and Part 2
  (D/J = H) are complete; vtest battery all-PASS with derived expectations;
- <= 16 pages.

## Task routing
- [mainline] B1-B3: execute directly (mathematical writing task; `coding`).
- [mainline] B4: execute directly (scratch battery rebuild).
- TaskCreate/TaskUpdate lane: tracked via goal-tracker Active Tasks table
  (this environment has no separate Task tool; statuses kept there).
