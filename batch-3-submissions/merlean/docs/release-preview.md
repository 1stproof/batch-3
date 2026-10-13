# Release-preview policy

The private preview is a publication-ready staging repository, not a private-data archive.
Use the same root-level source organization, English documentation, public-compatible
manifests, attribution, tests and sanitized demonstration as the public repository.
Keep canonical sources in `src/`, `workflows/`, `ports/` and `roles/`; regenerate all eight
provider packages with `scripts/build_bundles.py`. Do not maintain a second nested design tree.

## Data and history

Before pushing, audit the complete outgoing tree and its reachable commit ancestry, not
only plugin archives. Exclude real personal paths or contact details, private research and
reference corpora, chat/session records, credentials, runtime databases and caches. Public
author attribution, licenses, cited public URLs and clearly synthetic test fixtures remain
subject to review; do not remove functional tests merely because they exercise unsafe input.
Only the sanitized demonstration belongs under `examples/`.

Preserve local historical work outside the release branch. Never push backup or research
branches incidentally, and never use `--all`, `--mirror` or `--follow-tags` for a preview release.

## Remote policy

The private preview remote is `origin` and is the default push target. Confirm the intended
repository and its private visibility before publication. The public repository is
`https://github.com/MerLeanProver/MerLean`, retained as `public-upstream` for comparison.
Its push URL is disabled by default in the maintained checkout.

A generic request to commit or push applies to the private preview, not the public repository.
A public release requires a current, explicit user instruction naming the public target,
an independent privacy/release audit of the exact tree and ancestry, and a deliberate
temporary reconfiguration of its push URL. Restore the disabled push URL after the authorized
release. Do not infer public-release permission from repository visibility or prior releases.

This remote configuration is local Git state, not a hosted access-control mechanism; fresh
clones must configure their remotes consistently. Do not change installed user-wide plugins
as part of repository synchronization unless separately requested.

## Release checks

Run the following after scoped changes:

```sh
python3 scripts/build_bundles.py --catalogs
python3 -m unittest discover -s tests
python3 scripts/audit_research_runtime_parity.py
python3 scripts/audit_codex_release.py
```

Review the exact staged paths and incoming/outgoing commit range, then push only the
authorized branch. A preview passing these checks is not automatically a public release,
nor does packaging change a mathematical result's verification grade.
