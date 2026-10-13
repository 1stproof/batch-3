# Shared-workspace smoke validation

Manual integration run: 2026-09-15, macOS arm64, Lean 4.32.2 / Lake 5.0.0.
This records tool behavior, not a research grade or a portable proof certificate.
No existing research source, project configuration or manifest was edited by the test.

- Registered an existing installed provider with nine Git dependencies and official
  Mathlib revision `905b95818eb32af7874a58b427f50c1711a5e96c`.
- Created two fresh temporary projects outside both the provider and the tool tree.
  Their `.lake/packages` symlinks resolve to the same provider directory. Their
  `.lake/build` directories are independent; each project occupies approximately 1.5 MB.
- Both default library builds completed successfully (121 Lake jobs each).
- Both projects checked an extra file importing their own built library and using its
  `0 + n = n` theorem. The second also checked an integer polynomial identity by `ring`.
- A separate `example : False := by trivial` failed with compiler exit code 1, as required.
- The existing unmodified `_installed_mathlib_identity` grade prerequisite returned
  the expected Mathlib revision and project manifest hash for both shared workspaces.
  This check alone is explicitly not a Gold audit.
- Provider profile validation still passed after compilation. The sampled compiled
  `Mathlib/Data/Nat/Basic.olean` retained its original modification time and size;
  this is a sample, not a claim that every ignored cache byte is immutable.

Reproduce with the commands in `docs/shared-workspaces.md`, using a trusted installed
provider and new temporary project directories. Do not publish machine-local profiles
or the generated `.merlean-workspace.json` marker. The offline unit tests in
`tests/test_shared_workspace.py` exercise drift rejection, dependency identity, isolation,
override rejection, lock contention, command restrictions and launcher behavior using
temporary Git fixtures; they do not replace this real Lean integration check.
