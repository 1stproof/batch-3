# Round 1 Contract

## IMMUTABLE SECTION (locked at Round 0; reproduced for reference)

### Mainline Objective (Round 1)

Produce a complete, axiom-level proof of the theorem in problem.tex:
for every hyperfield H and all x,y,z ∈ H, 0 ∈ x ⊞ y ⊞ z implies
0 ∈ x³ ⊞ y³ ⊞ z³ ⊞ (−xyz) ⊞ (−xyz) ⊞ (−xyz). Concretely this round must
CLOSE the free case (Round 0 left it conditional on an unproved exchange
lemma) with a proof using only (H1)–(H4) and lemmas proved in the
document; no enumeration and no external structural theorems may be used
as proof steps. If — and only if — every provable route fails after
genuine effort, the verdict must instead be downgraded to a precisely
stated conditional theorem (Option B of the Round-0 review), never an
asserted "Yes" resting on unproved claims.

### Target ACs

- AC-1 (complete, line-checkable proof of the claimed assertion)
- AC-3 (no numerical evidence or confidence language substituting for a
  proof step)

### Capability Anchor

N/A (plan.md has no Feature Map / Capability Map section)

### Blocking side issues in scope (from Round-0 review)

- B1/MS: free case unproved — the mainline objective itself.
- B2: Round-0 document asserted a false general claim
  (|H×/⟨g³⟩| ∈ {1,3}) and relied on enumeration (Prop 4.6) and on
  external structure theory (Sec. 5); all such content must be removed.
- B3: garbled step in lem:basic(iv); typo "Since −" in prop:degen.

### Queued side issues out of scope

- bitlesson-selector binary absent (informational; bitlesson.md read
  directly).
- Git history containing the old draft (no action).

### Round success criteria

1. solution.tex contains a full proof of Theorem 2.1 for all cases, or
   an explicitly downgraded verdict with exact open statement.
2. solution.tex contains no proof-step usage of: enumeration/computer
   verification (words "verified", "enumeration", instance counts,
   "99.6%"), external structure theory ("Massouros", "Baker–Bowler",
   "cube subgroup/cubic class" as proof inputs), or any lemma stated
   without proof.
3. Compiles standalone with pdflatex (two passes, no errors), ≤ 16
   pages, article class with the allowed standard packages only.
4. Round committed; goal tracker mutable section updated; round-1
   summary written.
