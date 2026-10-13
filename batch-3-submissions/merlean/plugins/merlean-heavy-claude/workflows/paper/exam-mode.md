# Exam writing profile

For the automatic research-to-writing transition, see `docs/exam-mode.md`: the
executable Codex Lite host's fresh `--exam` run shares one whole-exam clock and
enters writing at hour 22.75 by default. Saved clocks remain unchanged. The standalone paper profile below starts no timer.
The official Batch 3 system-output limit is 16 pages per solution, within 24 hours
for all ten problems; the 12-page human problem-selection limit is a different rule.

For an exam/benchmark answer, use `--profile exam` with `paperctl init-compose` or
`init-refine`. For an existing run use `paperctl set-profile --state WORK/00-run-state.json
--profile exam`. This preserves old policy/state in `profile-history/` and reopens affected
gates without restarting the manuscript or repeating completed reader cycles automatically.
Use the current manuscript and the original accepted result; never create a duplicate run.

## Batch 3 page budget

The [official call](https://1stproof.org/assets/docs/batch3-call-for-submissions.pdf) limits
each of the ten LaTeX solutions to 16 pages. Our conservative counting policy includes the
entire delivered PDF, including appendices and references; do not assume an exclusion that the
call does not state. Use the proof-first allocation and compiled-count checks in
`mathematical-writing.md`. When feasible, aim for a complete draft of at most 14 pages to leave
room for reader repairs and final matter. This is our optional working reserve, not an official
cap, a minimum length, or a reason to remove essential explanation from a 15- or 16-page answer.
A draft above 14 pages is an early warning to review the remaining allocation, not a failed gate.
Use an ordinary legible template; our class and margin guidance is not an official Batch 3 rule.
The final measured PDF must still fit 16 pages after both reader cycles and all edits.

## Narrow scope of the exam settings

Both profiles preserve the FULL paper-writing and polishing workflow. Exam mode only removes
novelty as a requirement and human literature authorization/download waits:

| Setting | Default | Behavior |
| --- | --- | --- |
| `assess_novelty` in `literature-policy.json` | false | Skip novelty searches and originality requirements; use audited `NOT_REQUESTED`. An exam answer may be correct even if the result is known. |
| `request_human_authorization` | false | Do not wait for human literature authorization; use available permitted tools, respecting offline/access restrictions. |
| `request_human_download` | false | Obtain and verify sources autonomously, or omit unavailable optional citations with a recorded reason. Never hide a needed proof dependency or known credit. |

A requested novelty assessment may explicitly set `assess_novelty: true`; insufficient evidence
then yields audited `NOT_ASSESSED`, not fabricated CLEAR. Selecting exam mode resets novelty
and both human-wait settings to false. Selecting standard preserves explicit literature choices;
it does not silently enable novelty. The reference contract in `references.md` governs evidence.

## Full writing quality remains required

`writing-profile.json` fixes `readability_required: true`, `compression_required: true`, and
`polishing: full` in both presets. These are invariants, not switches for skipping quality work.
No exam profile may disable or excuse:

- coherent proof structure, definitions before use, consistent notation and explicit key inferences;
- explanatory prose, local hypothesis clarity, and a standalone argument a reader can reconstruct;
- substantive editorial revision, wording improvements and removal of repetition;
- the full compression/shrink pass, with preservation ledgers and audit of every actual edit;
- compliance with any supplied page limit or exam format (record the actual limit; never invent one);
- layout refinement, visual inspection, legibility and clean compilation;
- the two distinct sequential fresh-reader/revision cycles and verification of the second revision;
- original-question coverage, correctness, raw fidelity, premises, proof and known-credit preservation;
- source verification for all used citations, manuscript audits and all ordered release gates.

Do not use an exam/no-novelty setting as justification for skipping compression or treating an
unrevised readable draft as polished. A no-op shrink is allowed only under the existing evidence
and independent review rules, not because this profile was selected. Page limits must be met
without deleting essential hypotheses or proof bridges, tiny fonts, or unreadable layout. If a
limit conflicts with a complete readable answer, report the actual unresolved constraint rather
than declaring compliance.

This profile changes no research acceptance standard, account/model, network or file permission,
or publication authorization. It creates no new proof, grade or novelty certificate.
