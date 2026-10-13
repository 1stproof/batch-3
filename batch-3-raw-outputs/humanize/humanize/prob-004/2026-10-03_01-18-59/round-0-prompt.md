Read and execute below with ultrathink

## Goal Tracker Setup (REQUIRED FIRST STEP)

Before starting implementation, you MUST initialize the Goal Tracker:

1. Read @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md
2. If the "Ultimate Goal" section says "[To be extracted...]", extract a clear goal statement from the plan
3. If the "Acceptance Criteria" section says "[To be defined...]", define 3-7 specific, testable criteria
4. Populate the "Active Tasks" table with MAINLINE tasks from the plan, mapping each to an AC and filling Tag/Owner/Capability
5. Record any already-known side issues in either "Blocking Side Issues" or "Queued Side Issues"
6. Write the updated goal-tracker.md

## Round Contract Setup (REQUIRED BEFORE CODING)

Before starting implementation, create @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/rlcr/2026-10-03_01-18-59/round-0-contract.md with:

1. **One mainline objective** for this round
2. **Target ACs** (1-2 ACs only)
3. **Capability Anchor**: the `Feature Map / Capability Map` node(s) or map section this round advances, or `N/A` when the plan has no capability map
4. **Blocking side issues in scope** for this round
5. **Queued side issues out of scope** for this round
6. **Round success criteria**

Use this contract to keep the round focused. Do NOT let non-blocking bugs or cleanup work replace the mainline objective.

**IMPORTANT**: The IMMUTABLE SECTION can only be modified in Round 0. After this round, it becomes read-only.

---

## Implementation Plan

For all tasks that need to be completed, please use the Task system (TaskCreate, TaskUpdate, TaskList).

Every task MUST start with exactly one lane tag:
- `[mainline]` for plan-derived work that directly advances the round objective
- `[blocking]` for issues that prevent the mainline objective from succeeding safely
- `[queued]` for non-blocking bugs, cleanup, or follow-up work

Rules:
- `[mainline]` tasks are the primary success condition for the round
- `[blocking]` tasks may be resolved in the round only if they truly block mainline progress
- `[queued]` tasks must NOT become the round objective and do NOT need to be cleared before moving on
- If a new issue is not blocking the current objective, tag it `[queued]` and keep moving on the mainline

## Task Tag Routing (MUST FOLLOW)

Each task must have one routing tag from the plan: `coding` or `analyze`.

- Tag `coding`: Claude executes the task directly.
- Tag `analyze`: Claude must execute via `/humanize:ask-codex`, then integrate Codex output.
- Keep Goal Tracker "Active Tasks" columns **Tag** and **Owner** aligned with execution (`coding -> claude`, `analyze -> codex`).
- If a task has no explicit tag, default to `coding` (Claude executes directly).

## Capability Anchor (MUST FOLLOW)

If the plan contains `## Feature Map / Capability Map`, every mainline task and round contract MUST stay anchored to it:
- Add the relevant Capability ID(s) or capability/feature name(s) to the round contract's **Capability Anchor** field.
- Fill the Goal Tracker Active Tasks `Capability` column for each mainline task.
- Before coding or analysis, restate how the task fits the selected capability's business, design, and implementation context.
- Do not let a task drift into another capability or future-scope node unless you record a Plan Evolution entry.

If the plan does not contain `## Feature Map / Capability Map`, set the round contract **Capability Anchor** and each Goal Tracker Active Tasks `Capability` value to `N/A`. Do not invent capability nodes for legacy or hand-written plans without a map.

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

---

## BitLesson Selection (REQUIRED FOR EACH TASK)

Before executing each task or sub-task, you MUST:

1. Read @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/bitlesson.md
2. Run `bitlesson-selector` for each task/sub-task to select relevant lesson IDs
3. Follow the selected lesson IDs (or `NONE`) during implementation

Include a `## BitLesson Delta` section in your summary with:
- Action: none|add|update
- Lesson ID(s): NONE or comma-separated IDs
- Notes: what changed and why (required if action is add or update)

Reference: @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/bitlesson.md

---

## Goal Tracker Rules

Throughout your work, you MUST maintain the Goal Tracker:

1. **Before starting a round**: Re-anchor on the original plan and current round contract
2. **Before starting a task**: Mark the relevant mainline task as "in_progress" in Active Tasks
   - Confirm Tag/Owner routing is correct before execution
   - Confirm the task's Capability matches the round contract's Capability Anchor
3. **Active Tasks** are MAINLINE tasks only - side issues do not belong there
4. **Blocking Side Issues** are reserved for issues that truly stop mainline progress
5. **Queued Side Issues** are non-blocking and must not take over the round
6. **After completing a mainline task**: Move it to "Completed and Verified" with evidence (but mark as "pending verification")
7. **If you discover the plan has errors**:
   - Do NOT silently change direction
   - Add entry to "Plan Evolution Log" with justification
   - Explain how the change still serves the Ultimate Goal
8. **If you need to defer a task**:
   - Move it to "Explicitly Deferred" section
   - Provide strong justification
   - Explain impact on Acceptance Criteria
9. **If you discover new issues**:
   - Add to "Blocking Side Issues" only if mainline progress is blocked
   - Otherwise add to "Queued Side Issues" or keep them as `[queued]` tasks/backlog

---

Note: You MUST NOT try to exit `start-rlcr-loop` loop by lying or edit loop state file or try to execute `cancel-rlcr-loop`

After completing the work, please:
0. If you have access to the `code-simplifier` agent, use it to review and optimize the code you just wrote
1. Finalize @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/rlcr/2026-10-03_01-18-59/goal-tracker.md (this is Round 0, so you are initializing it - see "Goal Tracker Setup" above)
2. Write your round contract into @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/rlcr/2026-10-03_01-18-59/round-0-contract.md
3. Commit your changes with a descriptive commit message
4. Write your work summary into @/work/first-proof-humanize-tdgou2bu/003-prob-004/.humanize/rlcr/2026-10-03_01-18-59/round-0-summary.md
