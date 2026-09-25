---
name: review-architecture-sdk-2026-06-07
description: "Historical SDK review, rewritten with the verified current package status"
metadata:
  node_type: memory
  type: project
  originSessionId: 5f9191e1-29d5-452d-a422-f31fc58ce9e1
  modified: 2026-08-15T00:00:00.000Z
---

The 2026-06-07 maturity verdict and implementation log are obsolete. Do not
reuse their paths, line counts, test counts, priorities, or claims about
missing versioning, handler types, invariants, live queries, licensing, or
package publication without a fresh current-tree audit.

**Verified current package status:** `packages/core/package.json` and
`packages/sdk/package.json` both declare version `0.1.0`, the MIT license, and
public publish access. `packages/sdk/README.md` is the current public-surface
guide; it documents `BonfireClient`, `defineKind`, `defineHandler`, typed-client
helpers, agent entry points, product facades, and live query APIs. Repository
`README.md` says public repository metadata still waits on a public git remote.

Use the existing `check:release` script in `package.json` for the SDK release
workflow, and use the unit/integration split in repository `CLAUDE.md` for test
claims. The older review's verification and evidence framing is superseded by
[[verification-regime-2026-08-14]]. Current product intent lives in
[[project-sdk-redesign-objective]].
