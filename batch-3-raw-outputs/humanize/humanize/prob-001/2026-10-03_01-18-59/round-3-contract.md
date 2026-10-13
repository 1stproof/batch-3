# Round 3 Contract

## Mainline Objective

Close `prop:vanish` (H^{q>=1}(i(b),G_F)=0, H^0=F(b)) so that
`thm:main-end` is a proved theorem again, by executing the review's
Steps 3.1, 3.2, 3.3 exactly as written, using only the in-place and
reviewer-verified machinery (lem:constcx, lem:subquot, lem:depth,
rem:transfer, lem:filter, lem:nerve, lem:mixed, lem:dlemma, lem:dead,
lem:sieve(ii), lem:sandwich). The counterexample route is NOT
authorized; the AC-4 honest-restatement branch is a last resort only.

## Target ACs

- AC-1 (Section-4 endgame proved line by line; no floating
  parentheticals carrying the argument)
- AC-3 (audit of quantifiers, transport direction, degeneracies; every
  "after a pullback" cites rem:transfer; every
  chi^gp((K/J)^gp)=dZ,d>=1 cites lem:dlemma)

## Capability Anchor

N/A (plan.md has no Feature Map / Capability Map).

## Blocking Side Issues in Scope (all on the mainline)

- M-0/M-4: prop:vanish Steps 1-3 not yet named-reference deductions.
- M-1: lem:sieve(i)'s proof invokes the (f,iB)-vanishing hypothesis
  prop:vanish never establishes, and "at the remaining dead pieces by
  transport" is unsupported (dead sector not connected).
- M-2: lem:sieve(i)'s single-dead-pin conclusion is FALSE for
  rk(bar P)>=2 (incomparable dead pieces need not share a constant);
  prop:vanish Step 2 needs only equality of fold images, not the false
  single constant.

## Queued Side Issues (out of scope unless the chosen route re-enters)

- q-dead-sector: lem:filter (F2) single-anchor does not cover deep dead
  pieces (>=2 folds); the 3.1/3.2 route never needs the dead sector.
- q-skippedcases: rank-one (dim bar P<=1) and P={0} cases by named
  references (lem:const + lem:dead), two sentences.
- q-restriction-lemma / q-accounting: absorbed into M-4 (Step 3.3).
- Q-3 (rest) + final typography pass: final round (Round 4).

## Round Success Criteria

1. Step 3.1: prop:vanish Step 1 asserts ONLY that dead-sector values
   become coboundary values on the D-slice (constant sheaf F(b_P);
   lem:dead + lem:constcx H=D) after a common refinement (lem:sandwich);
   no false single-pin constancy. Step 2 keeps the two-fold displayed
   subtraction and concludes the equality
   F(iota_f)(z_f)=F(iota_{f'})(z_{f'}) in F(b_P) (dead coboundaries
   cancel via Step 1); dead sector left arbitrary.
2. Step 3.2: lem:sieve(i) re-proved by level-strands filter over the
   finitely many fold rays (per-ray strand contractible by lem:constcx
   with anchor H=f_rho; transport identity by lem:nerve(i) Case A /
   lem:mixed(C1)), via lem:subquot; the false "pinned to a single
   element" clause deleted. lem:sieve(ii) retained unchanged (verified
   sound).
3. Step 3.3: prop:vanish Step 3 rewritten: (a) lem:sieve(ii) pins
   z_K-hat; (b) two-fold comparison at (f,i(P/K)) gives
   F(pi_{K->P})(z_K-hat)=0 (keep the verified display); (c) z_K-hat
   killed by induction D(K) on the restricted cover (pullback along
   i(b)->i(P/K)), "after one more pullback" citing rem:transfer,
   "outward maps zero" citing (b); every floating parenthetical
   deleted; (d) rank-one / P={0} by named references (lem:const,
   lem:dead).
4. Recompile twice: 0 errors, 0 undefined refs, <=16 pages.
5. Goal tracker updated (B-8 -> resolved once M-2 closes; M-0/M-4
   cleared), commit referencing this review, round-3-summary.md.
