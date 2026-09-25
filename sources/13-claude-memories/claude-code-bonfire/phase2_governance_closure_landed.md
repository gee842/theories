---
name: phase2_governance_closure_landed
description: "The surviving Phase-2 fact: E2 final resolution and physical move/delete are a two-commit operation"
metadata:
  node_type: memory
  type: project
  originSessionId: a0a2cfa6-c6f0-40bf-9a36-0154f0f7736a
  modified: 2026-08-15T11:09:37.000Z
---

The old landing inventory, closure hashes, byte-drift blocker list, test-red
taxonomy, and reseal advice are superseded by
[[verification-regime-2026-08-14]].

The operational fact that survives is E2's two-commit law. The current
`check:kind-legacy-root-transition` implementation in
`scripts/yi49/kind-legacy-root-transition/lifecycle.mjs` requires a final
resolution to exist in a prior commit before the corresponding legacy source
can move or disappear.

`scripts/yi49/kind-legacy-root-transition/classification-archive.mjs` derives
`priorCommit` from git state: when the classification tree or guarded legacy
roots are dirty it uses `HEAD`; when they are clean it uses `HEAD^1`. Therefore
the first commit records the resolution and a later commit performs the
move/delete. Prior-commit consumer debt can self-heal after the next clean
commit advances that comparison window, while the separate baseline-plus-
authorized-consumers law can still report real debt. Diagnose the current gate
output; do not revive source-byte pins or archived blocker counts.

Related: [[e2_two_commit_law_mechanism]], [[verification-regime-2026-08-14]].
