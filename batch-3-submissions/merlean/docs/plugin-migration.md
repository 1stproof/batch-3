# Version 2 marketplace migration

The marketplace identifier remains `merlean` for both providers. Version 2 separates
four public agents into one standalone package each: Lite, Heavy, Paper-writing, and Referee.
All eight packages share the maintained runtime and trust policies.

| Previous package | Version 2 replacement |
| --- | --- |
| Claude `merlean` | `merlean-lite-claude` for new research, `merlean-heavy-claude` for full proof/formalization, `paper-writing-claude` for papers |
| Codex `lite-codex` | `merlean-lite-codex` for new research, `merlean-heavy-codex` for full proof/formalization |
| Codex `paper-writing-codex` | `paper-writing-codex` (same identifier, updated package) |

Update the repository marketplace in your host, install the desired replacement,
and disable the superseded package if its old entrypoints would conflict. Package
renaming is not an automatic migration of existing host installations. Keep research
projects and runtime data outside plugin directories. This repository does not modify
personal host configuration when building packages.

Lite remains the fresh research default and targets SILVER. Heavy requires explicit
selection or a full-formalization task and targets strictly audited GOLD. Internal
formalize/prove/translation/research procedures remain available through Heavy;
statement-only translation does not prove the statement or award a grade.

Maintainers edit `workflows/`, `ports/`, `roles/`, and `src/`, then regenerate all eight
packages with `python3 scripts/build_bundles.py --catalogs`. Commit the generated
packages and both catalogs with their source changes. Release archives are generated
from that committed Git tree and audited before distribution. Never hand-edit package
copies, include credentials/campaign data, or overwrite locally modified generated files.

## Referee integration

Referee now shares the maintained workflows/runtime and has `referee-codex` and
`referee-claude` packages. Its source entry is `workflows/referee.md`; it executes
manuscript-scoped MerLean Lite verification by default. Keep manuscript projects,
Lean workspaces, reports, and audit evidence in the user's review repository.
Replace any older standalone referee harness with a pointer to this source or
an installed Referee entry; do not maintain synchronized copies of its rules.
The report has no research grade. Explicit full formalization still follows Heavy.
