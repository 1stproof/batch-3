# NL modifier for MerLean Lite

`-NL` (alias `--nl`) runs Lite without Lean execution or formalization. It uses the
same planning, discovery, independent review, original-scope checks, paper workflow,
and Silver acceptance rules. It is a capability switch, not another grade or agent.
The repository still builds four agents for two providers.

## Select and start

```bash
scripts/merlean-agent -NL --provider codex
scripts/merlean-agent -lite -NL --provider claude
bash scripts/setup.sh --project /path/to/new-project --runtime /path/to/runtime -NL
PLAN_OFFLINE=1 scripts/merlean --data /path/to/new-project/solution_data --nl list
```

The selector reports the existing `merlean-lite` entry; it does not launch a model.
In either provider, invoke the existing Lite skill with `-NL` in the request.
The Codex Lite manifest also supplies a second composer shortcut with that request.
There is no separate GUI application or ninth bundle.

NL setup persists `.merlean-capabilities.json`. It does not create Lean templates,
a toolchain, a Lake setup marker or Lean MCP configuration; it does not run Lake or
install the Lean MCP dependency section. Existing files are preserved. Online plan
storage still needs its ordinary Python dependencies and credentials; `PLAN_OFFLINE=1`
uses the existing deterministic local backend. The default setup and dependencies
remain unchanged. Re-running setup inherits an existing NL policy.

For the confined Codex pilot, add `--nl` to a **new** `--problems` launch. The frozen
host configuration records `nl_only: true`. Do not combine it with `--lean-executable`
or `--lean-library`. Continuations inherit the flag and reject changing it, including
turning an existing ordinary Lite campaign into NL. A selector using `--resume-mode`
reports capability as inherited/unknown; the actual persisted runtime is authoritative.
Use separate fresh projects for experiments comparing Lite and Lite NL.

## What remains required

A reviewer can decide that no local Lean certificates are necessary using the usual
substantive triage criteria. Silver remains possible when all existing gates pass,
including a genuinely independent complete review and the required original-scope
reviews. Disabling Lean does not automatically deselect any row, resolve any finding,
prove an uncertain claim, or award or downgrade a grade. A necessary unresolved
Lean obligation stays visible and can block completion in NL. Preserve `needs-lean`,
`needs-review`, failed evidence, counterexamples and other unknowns honestly.

Paper writing inherits the capability and existing grades. It cannot use writing as
a route into formalization or a new Gold claim. Existing mathematical history is not
rewritten. NL does not reset budgets, simplify the original problem, or replace
independent reviewers with self-review. Existing main/reviewer and worker model
preferences remain in force.

## Enforcement boundary

Maintained plan APIs, offline/online plan CLIs, direct proof seeding and Lean sync,
shared-workspace build/check, runtime Gold checking/recording, Lean probes, and the
confined pilot's Lean workers/local modules/inventory use one shared capability guard.
Persisted project/plan ancestors and frozen host configuration are checked, including
lexical and resolved paths; a descendant false/default value cannot enable Lean.
Changing a persisted capability requires a separate fresh project, not a resume flag.

Claude Code and ordinary Codex provider sessions also receive the same prohibition in
their instructions: do not call Lean MCP, `lean`, `lake`, `elan`, formalization workers,
or compiler inventory in NL. General-purpose native shell access is instruction-bound;
this modifier is not an operating-system ban on arbitrary commands outside maintained
interfaces. The confined pilot separately prevents research workers from executing
arbitrary shell tools. Its approved NL research workers and bounded Python probes
remain available under their existing safeguards.
