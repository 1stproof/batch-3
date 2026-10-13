---
name: referee
description: >-
  Write or reassess a scientific referee report. Default to MerLean Lite for
  manuscript-scoped mathematical verification, inspect relevant Lean 4 proofs,
  and obtain independent review. Keep essential substantiated corrections and
  clear typos; omit taste or valid-method differences. Use for manuscript peer
  review, not internal proof-plan approval or generic proofreading.
---

Provider: `claude`. Resolve `<PLUGIN_ROOT>` as this installed file's third parent (`skills/<name>/SKILL.md` → package root). Read the following two files completely before acting: `<PLUGIN_ROOT>/ports/claude.md` and `<PLUGIN_ROOT>/workflows/common.md`. Internal references inherit that root.


# Referee

Apply default convergence from `workflows/common.md` to scoped, substantiated
findings and their verification. Preserve contrary evidence, independence and
read-only boundaries; do not launch unrelated proof-route exploration.

Read `<PLUGIN_ROOT>/ports/claude.md` and
`<PLUGIN_ROOT>/workflows/common.md`, then
`<PLUGIN_ROOT>/workflows/referee-standing-rules.md` and
`<PLUGIN_ROOT>/workflows/referee-protocol.md` in full. Resolve the plugin root
from the installed entrypoint, not the manuscript working directory. For direct
source use, the source directory containing `workflows/` is `<PLUGIN_ROOT>`;
choose the current host's provider adapter.

Referee is a public agent alongside Lite, Heavy, and Paper-writing. Substantive
review defaults to executing the bundled MerLean Lite workflow, not merely
selecting its name. Its mathematical verification has a SILVER ceiling and
never silently escalates to Heavy. Full formalization requires an explicit
user request and uses the unchanged Heavy trust gates. Editorial-only changes
reuse valid existing evidence and do not launch a new mathematics campaign.

Run in the user's `PROJECT_DIR`, outside the source and installed packages.
Keep new review evidence, verification workspaces, and the final report there.
Preserve existing manuscript and Lean project locations and inspect them in
place. Agent logic and helper scripts remain in `<PLUGIN_ROOT>`.

Use fresh independent `gpt-6-astra` reviewers for substantive mathematical and
proportionality checks when available; respect explicit model choices and host
concurrency. Main owns the final report and resolves disagreements from evidence.
Relevant existing Lean statements, hypotheses, definitions, proof dependencies,
and manuscript correspondence must be checked before retaining a mathematical
objection. Incomplete formalization is not itself a manuscript error.

For manuscript presentation, apply `workflows/paper/reader-facing-paper.md`: assess a
self-contained mathematical paper, not a process log. Do not demand failed exploration,
debugging histories, internal grades or acceptance records in the manuscript. Require real
mathematical gaps, necessary limitations and relevant negative results to remain explicit.

Follow the standing rules when selecting comments: important substantiated
corrections and useful clear typos, no quota, no objections based only on taste,
viewpoint, or a different valid method. The report is a review judgment, not a
research grade. Record verification limitations in its accompanying summary.

The optional `<PLUGIN_ROOT>/scripts/report_language_audit.py` flags wording
and em dashes; vocabulary differences are advisory unless the user explicitly
requests `--strict-vocabulary`. Compile a changed TeX report and visually
inspect every final PDF page before delivery.

Within existing substantive and exposition checks, locate undefined academic terms,
ambiguous invented labels, and missing key hypotheses or proof bridges. Ask for a
supported standard term, a clear descriptive expression, or a definition and role for
a genuinely useful new construction. Do not reject a term solely because it is new.
Require restoration of necessary argument, not arbitrary shortening or extra rounds;
use detailed source evidence only where the review's existing scope permits it.
