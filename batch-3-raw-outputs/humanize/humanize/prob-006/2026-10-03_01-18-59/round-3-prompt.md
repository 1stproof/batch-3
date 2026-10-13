# Code Review Findings

You are in the **Review Phase**. Codex has performed a code review and found issues that need to be addressed.

## Required Re-anchor

Before touching code:
- Re-read the original plan at @plan.md
- Re-read the goal tracker at @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
- Refresh the current round contract at @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md

The round contract must preserve a single mainline objective. Code review findings do NOT automatically become the new round objective.
If the original plan contains `## Feature Map / Capability Map`, the refreshed contract must also preserve or update the current Capability Anchor intentionally.

## Review Results

## Codex Review Issues

- [P1] False claim that Gordon--Luecke proved the cabling conjecture — /work/first-proof-humanize-tdgou2bu/005-prob-006/solution.tex:499-503
  Remark \ref{rem:glcabling} asserts that Gordon--Luecke proved 'the cabling conjecture for knots in S^3', i.e. that every knot in S^3 with a reducible surgery is cabled. This is incorrect: the cabling conjecture (Gonzalez-Acuna--Short) remains open in general; Gordon--Luecke proved that reducing slopes are integral (correctly cited as Theorem \ref{thm:gl} above) and, with Boyle, that the conjecture holds when the surgery has only two summands — but the full statement attributed to them here is a famous open problem. The falsity is significant, not cosmetic: stated as known, this 'remark' would trivialize the entire content of the paper, since the main theorem for arbitrary (hence a fortiori L-space) knots would follow from just Theorem \ref{thm:gl}-style reasoning plus Lemma \ref{lem:cablesplit}, bypassing Ni--Wu's deep L-space-specific theorem. This should be deleted or corrected (e.g. by instead stating Gordon--Luecke's actual result [Invent. Math. 89 (1987)] that a reducible surgery has exactly two summands and, combined with Theorem \ref{thm:gl}, the slope is integral — which already gives the 'at most two prime summands' count for any knot, though not the primality of the summands handled here).
The main proof (Sections 1-4) is mathematically correct, compiles cleanly as standalone LaTeX within the 16-page limit, and answers the problem; but the document contains a major false historical statement in Remark \ref{rem:glcabling} attributing to Gordon--Luecke a proof of the (still open) cabling conjecture, which as stated would trivialize the result. Since the deliverable is a mathematics proof and accuracy of theorems is the core requirement, this finding must be fixed before the patch is considered correct.

Review comment:

- [P1] False claim that Gordon--Luecke proved the cabling conjecture — /work/first-proof-humanize-tdgou2bu/005-prob-006/solution.tex:499-503
  Remark \ref{rem:glcabling} asserts that Gordon--Luecke proved 'the cabling conjecture for knots in S^3', i.e. that every knot in S^3 with a reducible surgery is cabled. This is incorrect: the cabling conjecture (Gonzalez-Acuna--Short) remains open in general; Gordon--Luecke proved that reducing slopes are integral (correctly cited as Theorem \ref{thm:gl} above) and, with Boyle, that the conjecture holds when the surgery has only two summands — but the full statement attributed to them here is a famous open problem. The falsity is significant, not cosmetic: stated as known, this 'remark' would trivialize the entire content of the paper, since the main theorem for arbitrary (hence a fortiori L-space) knots would follow from just Theorem \ref{thm:gl}-style reasoning plus Lemma \ref{lem:cablesplit}, bypassing Ni--Wu's deep L-space-specific theorem. This should be deleted or corrected (e.g. by instead stating Gordon--Luecke's actual result [Invent. Math. 89 (1987)] that a reducible surgery has exactly two summands and, combined with Theorem \ref{thm:gl}, the slope is integral — which already gives the 'at most two prime summands' count for any knot, though not the primality of the summands handled here).

## Issue Classification

Classify each review finding before acting on it:
- **blocking side issue**: prevents the current mainline objective from succeeding safely or prevents review acceptance
- **queued side issue**: valid follow-up, but does not block the current round objective

Queued issues may be documented, but they must NOT take over the round.

## Task Rules

Every task must use one lane tag:
- `[blocking]` for review findings that must be fixed now
- `[queued]` for non-blocking follow-up work

Do not create new `[mainline]` tasks in review phase unless the review proves the previous mainline objective was incomplete.

## Instructions

1. **Refresh the round contract** at `/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/round-3-contract.md`
2. **Address blocking issues first** and keep the mainline objective stable
3. **Keep fixes inside the Capability Anchor** unless the review proves the anchor was wrong
4. **Focus on fixes only** - do not add new features or make unrelated changes
5. **Commit your changes** after fixing the issues
6. **Write your summary** to: `/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/rlcr/2026-10-03_01-18-59/round-3-summary.md`

## Summary Template

Your summary should include:
- The mainline objective for this round
- Which blocking issues were fixed
- Which issues were reclassified as queued follow-up
- How each fixed issue was resolved
- Any issues that could not be resolved (with explanation)
- Confirmation that `goal-tracker.md` was updated if the blocking/queued issue lists changed
- A Goal Tracker Update Request only if tracker reconciliation still needs Codex help

## Important Notes

- The COMPLETE signal has no effect during the review phase
- You must address the code review findings to proceed
- After you commit and write your summary, Codex will perform another code review
- The loop continues until no `[P0-9]` issues are found

## BitLesson Selection (REQUIRED FOR EACH FIX TASK)

Before implementing each fix task, you MUST:

1. Read @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each fix task/sub-task to select relevant lesson IDs
3. Follow the selected lesson IDs (or `NONE`) during implementation

Reference: @/work/first-proof-humanize-tdgou2bu/005-prob-006/.humanize/bitlesson.md

## Task Tag Routing Reminder

Follow the plan's per-task routing tags strictly:
- `coding` task -> Claude executes directly
- `analyze` task -> execute via `/humanize:ask-codex`, then integrate the result
- Keep Goal Tracker Active Tasks columns `Tag` and `Owner` aligned with execution

## Capability Anchor Reminder

If the plan contains `## Feature Map / Capability Map`:
- The round contract must name the relevant Capability ID(s) or capability/feature name(s)
- Goal Tracker Active Tasks must keep their `Capability` column aligned with the round contract
- Mainline work must preserve the selected capability's business, design, and implementation context
- Do not let queued or future-scope capability work take over the current round
