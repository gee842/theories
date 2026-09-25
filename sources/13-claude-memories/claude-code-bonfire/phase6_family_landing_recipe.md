---
name: phase6-family-landing-recipe
description: "Current Phase-6 family landing mechanics: checker-consumed unit records, destination roots, bridge debt, and exact structural claims"
metadata:
  node_type: memory
  type: project
  originSessionId: c62ec623-0222-46a3-86bd-9b9cbfb4d35b
  modified: 2026-08-15T11:09:37.000Z
---

The landing diary, family counts, byte-pin/reseal explanations, and proof-gate
registration history are superseded by [[verification-regime-2026-08-14]].
The Phase-6 unit, census, and bridge records remain temporary operational data
only because the surviving Phase-5/6 checkers read them;
`docs/yi/49-structural-arc/governance.md` says they die with those phases.

For a Phase-6 representation family:

1. Read its current unit in
   `docs/yi/49-evidence/phase-6-migration-unit-ledger-v1/` and the source
   adjudication it derives from. Follow the declared owner, milestone, bridge,
   proof, successors, and `residual` decision. Do not mint a parallel evidence
   quartet.
2. Land enduring code under the owner's `representationRoots` from
   `packages/core/structure-map/destination/bounded-contexts/`. Repoint every
   reader, searching both full legacy paths and sibling-relative imports. A
   residual successor keeps the old source; a non-residual successor does not.
3. Keep live structural claims exact. In
   `packages/core/structure-moves.json`, use `moves` only when the old source is
   gone, `liveSourceExtractions` when an old-path forwarding source remains,
   and `directoryMoves` only when historical directory resolution needs it.
   Update the owning bridge's sorted `supportPaths` and exact
   `legacyConsumerCensus`; when a legacy root retires, update the bridge,
   bounded-context `legacyByMilestone`, work-order record, and current
   allowlist claim together. Use the current record READMEs and generators;
   do not copy hashes or counts into memory.
4. Change a milestone only with the cutover that earns the state. `active`
   establishes ownership and boundaries; it does not prove a running
   capability.
5. Write an architecture-shadow journal entry only when the landing changes a
   structure-map claim. Invoke
   `scripts/architecture-shadow/write-architecture-change.mjs` with the change
   descriptor and `--dry-run` first, then run
   `pnpm check:architecture-shadow`. A code-only landing with no claim change
   writes no entry.

Baseline the full output before editing. Verify `pnpm typecheck`,
`pnpm typecheck:tests`, `pnpm test`, `pnpm check:core-structure`,
`pnpm check:phase-1-structure`, and `pnpm check:phase-6-migration-units`, plus
the touched census/bridge gate and the unit's current `check:p-r:*` retirement
leaf. Run `pnpm test:integration` with `PG_URL=postgres:///bonfire_test` when
persistence or server behavior is involved. Phase-exit and retirement gates
are intake/debt lists while the phase is open: read all output and verify the
expected delta instead of demanding an invented green baseline.

In the shared checkout, never let two lanes edit the same compatibility-bridge
record or `structure-moves.json`, and never overwrite another session's dirty
paths. Related: [[shared_repo_concurrent_sessions]],
[[verification-regime-2026-08-14]].
