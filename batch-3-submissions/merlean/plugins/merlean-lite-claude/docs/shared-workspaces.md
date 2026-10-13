# External projects and shared Lean dependencies

MerLean is a tool source tree, not a required home for research data. One checkout
can serve Lite, Heavy, Paper-writing and Referee for many external projects.
The Python runtime may also be external (`MERLEAN_RUNTIME`). Project sources,
plans, references, manuscripts and audit evidence belong in the project, not in
the tool checkout or its generated plugins.

## Opt-in setup for a new project

Prerequisites: macOS/Linux, Python 3.9+, Git, Lean/elan and an already installed,
trusted Lean/Mathlib dependency workspace. This helper does not clone, download,
update, migrate or repair dependencies. Prepare a provider once using ordinary
Lean tooling if one does not exist. Prefer a dedicated, stable dependency provider
for long-lived use; an existing research workspace can serve as a provider only
while its registered configuration and dependencies remain unchanged.

Run the tool by absolute path; it need not be copied into the project:

```bash
/path/to/MerLean/scripts/merlean-workspace register \
  --workspace /path/to/existing-lean-workspace --name mathlib-pinned
/path/to/MerLean/scripts/merlean-workspace init \
  --project /path/to/new-project --profile mathlib-pinned
/path/to/MerLean/scripts/merlean-workspace doctor --project /path/to/new-project
/path/to/MerLean/scripts/merlean-workspace build --project /path/to/new-project
/path/to/MerLean/scripts/merlean-workspace check \
  --project /path/to/new-project MerLeanExperiment.lean
```

`init` requires a nonexistent project directory and never overwrites an existing
workspace. It creates a starter `MerLeanExperiment` library. Add research modules
under that library and keep all project-specific files in this workspace.
The profile registry defaults to `~/.cache/merlean/shared-lean`; use
`MERLEAN_SHARED_HOME` or the same `--store DIR` for `register` and `init` to change it.
Profiles and the ignored `.merlean-workspace.json` contain machine-local paths:
do not publish them. They are local operational records, not portable audit evidence.

Optional Python/MCP setup and separate plan storage:

```bash
bash /path/to/MerLean/scripts/setup.sh --project /path/to/new-project \
  --runtime /path/to/python-runtime --skip-mathlib
MERLEAN_RUNTIME=/path/to/python-runtime PLAN_OFFLINE=1 \
  /path/to/MerLean/scripts/merlean --data /path/to/new-project/plan-data status
```

Setup refuses automatic cache retrieval/build for a marked shared workspace unless
`--skip-mathlib` is supplied. This is deliberate: the shared helper owns dependency
validation and compilation coordination. It does not launch an LLM; direct an active
host agent to the appropriate MerLean workflow and the external project path.

## What is shared, and what is pinned

| Location | Ownership |
|---|---|
| Tool checkout | Agent design and scripts; no research data or Mathlib required |
| Registered provider `.lake/packages` | One installed dependency closure, including Mathlib and compiled dependency artifacts |
| New project's `.lake/packages` | Directory symlink to that same dependency installation; no package copy |
| New project's `.lake/build` | Project-local compiled modules and build state |
| New project's sources, plan and evidence | Independent project data; never shared automatically |

The first version accepts Lake manifest `1.2.0`, standard `.lake/packages`, a pinned
released Lean toolchain (including release candidates), and HTTPS Git dependencies
at full 40-character revisions. Each package must be a clean checkout with matching
HEAD and origin; Mathlib must use its official repository and matching toolchain.
Path dependencies, floating toolchain aliases, Git subdirectories and custom package
layouts are rejected, not silently reinterpreted. Individual package directories may
not alias checkouts elsewhere: this prevents distinct provider locks from covering the
same aliased checkout. The entire `.lake/packages` directory may be a symlink and is
canonicalized before locking. All listed resolved dependencies are
registered, not just Mathlib. The generated project requires Mathlib at its full
commit and inherits the provider's resolved dependency manifest.

Before and after wrapped compilation, the helper checks the registered provider's
manifest, toolchain, Lake configuration and dependency identities, plus the project's
pinned configuration and symlink. Drift fails closed. Do not run `lake update`, cache
retrieval or dependency edits through a shared project. To change versions, prepare
a separate compatible provider/profile and new workspace deliberately. This initial
helper has no in-place migration/reconfiguration command: it also rejects manual
edits to a managed project's Lake configuration. Existing, independently managed
research projects can still use MerLean tools without adopting this helper.

Wrapped compilation uses explicit `elan run <pin>` without `--install`, checks the
reported Lean version and clears inherited Lean/Lake override variables. The pinned
toolchain must already be installed. Lake receives `--no-cache`, and hidden
`.lake/package-overrides.json` files are rejected. `doctor` checks listed dependency
identities, not semantic completeness of the closure; a real build is still necessary
to detect missing imports or unresolved transitive dependencies. Trusted package build
scripts are executable code and are not network-sandboxed by this helper.

## Concurrency, trust and portability limits

Wrapped `build` and `check` use a nonblocking, per-user POSIX advisory lock keyed by
the canonical dependency directory, independent of registry/profile name. A busy
provider is reported for retry. Different projects therefore cannot concurrently
write that provider **through this wrapper**. Direct Lake, Lean LSP/IDE commands,
other OS users and existing Gold-audit subprocesses do not take this lock. Schedule
those jobs separately; this is cooperative coordination, not filesystem isolation.
Builds can update ignored dependency build artifacts. Different build options may
trigger recompilation; sharing source does not guarantee zero rebuilds.

Only use a trusted provider: compiling Lake configurations can execute code. Source
identity checks do not establish immutable or cryptographically verified `.olean`
provenance. A symlink and a successful build do not certify mathematical correctness,
literature fidelity, Silver or Gold. Existing grade audits remain unchanged, still
inspect the project's manifest and installed Mathlib, and still require their full
proof/source/use-site evidence. Never transfer a grade merely because caches match.

The machine-local symlink, marker and profile are not a portable Git dependency
distribution. Preserve the pinned Lean configuration and manifest in project version
control. A fresh clone can provision those dependencies normally, or explicitly create
a new shared workspace on the other machine and bring its research sources across.
Do not commit `.lake`, machine-local registries, credentials or build caches.
