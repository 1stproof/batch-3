# Standing rules for scientific referee reports

Apply this policy to manuscript reviews and revisions of referee reports.
It supersedes older harness requirements that forced every small concern
into the report, restricted every report word to the target vocabulary, or
made incomplete formalization an automatic objection. It does not relax
proof correctness or authorize weakening a theorem being formalized.

## Which comments belong in the report

- Keep the most important, well-supported corrections that affect a central
  result, a stated comparison, a consequential interpretation, or the ability
  to substantiate a principal computational claim. State the precise problem
  and the smallest adequate repair.
- Include a few clear typos or localized factual/notation corrections when
  useful. There is no quota or required minor-comments section. A true but
  low-value observation may stay in internal notes.
- Omit differences in taste, exposition, viewpoint, proof method, code
  organization, or experimental approach when the authors' approach is valid
  for what they actually claim. Do not turn an alternative research program
  or a stronger desired theorem into a revision requirement.
- Before retaining a criticism, reread its surrounding definitions, global
  assumptions, appendices, stated scope, and cited results. Consider the
  strongest reasonable response the authors could make from that material.
  Withdraw the criticism if it is already answered there.
- Old reports and audit notes are leads, not primary evidence. Recheck their
  concerns against the current version. Keep a short rationale for important
  withdrawn comments; do not restore a comment merely because an old ledger
  called it unresolved.

## Mathematical comments and Lean 4

For each proposed mathematical objection, inspect the corresponding Lean
code when it exists: the exact statement, all hypotheses and typeclass
assumptions, definitions/representations, imported results, proof, and the
connection to the manuscript. Distinguish:

1. A contradiction or counterexample satisfying the paper's actual hypotheses.
2. A consequential gap that remains after checking the full context.
3. A limit of our formalization or computation: an unproved adapter, an explicit
   premise implementing an inherited assumption, a cited theorem boundary,
   missing library support, or a check we have not run.

Only the first two ordinarily justify mathematical correction requests.
The third belongs in the verification summary unless separate evidence shows
an actual manuscript problem. A counterexample outside the theorem's
hypotheses does not refute it. A compiled conditional theorem does not prove
its premises; a clean axiom audit does not establish source fidelity by itself.

Do feasible direct checks before requesting more material. Separate a wrong
result from an unverified result. Source-derived inputs may suffice for
independent recomputation even when the authors' original run is unavailable.
Request only material needed to resolve the identified issue, allowing a
short argument, implementation, or checkable output as appropriate. Do not
routinely demand every minor, proof certificate, seed, hardware trajectory,
or optimization run. Preserve honest scope: source inspection is not a new
Lean build, and checking ranks is not certifying code distance.

## Independent review and final judgment

Use fresh independent Astra (`gpt-6-astra`) reviewers for substantive reviews
when available in the current host, respecting explicit model choices and
host concurrency. Supply the actual manuscript, the proposed report, and
relevant Lean and primary-source evidence. Ask reviewers to assess both the
validity and proportionality of each retained objection; do not instruct them
to invent criticisms or reach a desired recommendation.

The main reviewer evaluates disagreements against evidence and owns the final
wording. A vote or unanimous PASS is not a substitute for judgment. Rerun the
affected review after a substantive change; a punctuation or layout edit does
not require restarting all mathematics, computation, and literature audits.
Record what was actually reviewed and any changed scope.

## Writing

Lead with a short assessment, followed by the essential actionable points.
Use the paper's established technical terminology where accurate, and natural
English elsewhere. Words or phrases absent from the paper are not errors by
themselves. Never delete a valid scientific criticism merely to satisfy a
vocabulary list. Exact vocabulary matching is optional only when the user
explicitly requests that constraint. Keep the existing preference against
em dashes. Avoid duplicated conclusions and process-heavy prose.
