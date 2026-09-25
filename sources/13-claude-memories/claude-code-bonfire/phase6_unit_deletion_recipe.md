---
name: phase6-unit-deletion-recipe
description: "Current Phase-6 dead-unit rule: prove it unused, remove live scope claims atomically, then let the derived ledger drop it"
metadata:
  node_type: memory
  type: project
  originSessionId: 114ff51c-be53-430c-93b8-d39ed8b58265
  modified: 2026-08-15T11:09:37.000Z
---

The current Phase-6 ledger still admits only `single` and `split` dispositions;
it has no `delete` disposition. Its scope is derived from the legacy-destination
census, so dead code leaves the ledger only after its live census scope is
removed.

Before deleting a unit, search for all importers and runtime registration. A
passing proof test does not establish that the source is live because many
proofs exercise behavior without importing the adjudicated file.

Delete the source and every now-false live structural claim in one change. If
the current allowlist changes, append the transition described by
`packages/core/structure-map/convergence/allowlist-transitions/README.md`.
Update bridge, bounded-context, work-order, and census records only where they
name the removed source. Amend `packages/core/structure-moves.json` only when
one of its present claims becomes false; do not erase a historical move chain
merely because the current source is gone.

Once the regenerated census no longer includes the unit, remove its orphaned
judgment from the checker-consumed Phase-6 adjudication and use the current
`scripts/check-phase-6-migration-units.mjs` write workflow. Do not create a
separate deletion ledger, evidence quartet, or digest recipe. A structure-map
claim change also follows the journal rule: invoke
`scripts/architecture-shadow/write-architecture-change.mjs` with the change
descriptor and `--dry-run`, then run `pnpm check:architecture-shadow`.

Verify with
`node scripts/check-p-a-legacy-destination-census.mjs --write`,
`pnpm check:p-a:legacy-destination-census`,
`pnpm check:phase-6-migration-units`, `pnpm check:core-structure`, and
`pnpm check:phase-1-structure`, plus the affected bridge-retirement gate and
the relevant tests. Superseded ceremony: [[verification-regime-2026-08-14]].
