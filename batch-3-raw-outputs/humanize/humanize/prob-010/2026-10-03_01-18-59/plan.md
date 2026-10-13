# Solve one First Proof Batch 3 problem

## Goal Description

Produce a rigorous, self-contained resolution of the exact mathematical
problem in `problem.tex`. Write the deliverable as a standalone compilable
LaTeX document in `solution.tex`, no longer than 16 typeset pages.

## Acceptance Criteria

- AC-1: `solution.tex` answers every part of the exact question and proves
  every claimed implication, construction, bound, or counterexample.
  - Positive test: a specialist can verify the argument line by line.
  - Negative test: the document only sketches an approach or leaves a
    substantive case or lemma unproved.
- AC-2: The solution is self-contained relative to standard graduate-level
  mathematics and precisely states any external theorem it invokes.
  - Positive test: notation, hypotheses, edge cases, and theorem applications
    are explicit.
  - Negative test: undefined notation or an unstated nonstandard result carries
    the argument.
- AC-3: The proof is audited for logical direction, quantifiers, degeneracies,
  constants, and consistency with `problem.tex`.
  - Positive test: the delicate steps and all requested cases are checked.
  - Negative test: confidence language or numerical evidence substitutes for
    proof.
- AC-4: If the proposed assertion is false or ill-posed, the response gives a
  rigorous disproof or precise diagnosis and never presents conjecture as fact.
- AC-5: `solution.tex` begins with `\documentclass`, ends with
  `\end{document}`, uses only the installed standard LaTeX package set,
  contains no Markdown or workflow commentary, and fits within 16 typeset
  pages.

## Path Boundaries

### Upper Bound (Maximum Scope)

A publication-quality resolution with supporting lemmas, explicit
computations or constructions, exceptional-case checks, and precise statements
of any genuinely external theorem.

### Lower Bound (Minimum Scope)

One complete and correct answer to the assigned problem with every essential
step justified and no known gap concealed.

### Allowed Choices

- Use `problem.tex` as the sole mathematical source.
- Local scratch calculations are allowed.
- Web search, browser tools, internet research, apps, plugins, subagents,
  canonical outputs, published solutions to the prompt, sibling jobs, and
  other model attempts are forbidden.
- Edit `solution.tex` for the deliverable. Humanize may maintain ignored state
  under `.humanize/`, and the worker must commit every completed round.
- Prefer the `article` class with `amsmath`, `amssymb`, `amsthm`, `mathtools`,
  `geometry`, `enumitem`, `hyperref`, `xcolor`, `graphicx`, `tikz`, or `tikz-cd`.
  These are installed; do not require external files, fonts, or shell commands.
- Do not modify `problem.tex`, `plan.md`, `AGENTS.md`, or hook configuration.

## Dependencies and Sequence

1. Read and normalize every definition and quantifier in the statement.
2. Develop a candidate proof, disproof, construction, or classification.
3. Stress-test the difficult lemmas, boundary cases, constants, and converses.
4. Write the complete argument in `solution.tex` and audit it against the
   original statement and the 16-page limit.
5. Resolve every Humanize reviewer finding and complete final review.

## Implementation Notes

This is a natural-language mathematics task. Do not substitute source code, a
research plan, or unsupported experimental evidence for the proof. Honest
identification of a genuine obstruction is preferable to an invented theorem
or concealed gap.
