---
name: yi45-implementation-progress
description: "Archived docs 45–47 implementation record; live source map, not a current remaining-work queue"
metadata:
  node_type: memory
  type: project
  originSessionId: 5011a948-1646-46fb-b8f1-2291432a578a
---

The July 2026 docs 45–47 progress diary is historical. Current archive locations are:

- `docs/yi/archive/45-full-yi-capability-runtime-upgrade-plan.md` and its sibling directory;
- `docs/yi/archive/46-occasion-execution-pillar.md` and its sibling directory;
- `docs/yi/archive/47-occasion-as-canonical-write.md`.

The implementation still has live descendants, but their present boundaries—not the old phase
labels—are authoritative: touch contracts are in
`packages/core/src/runtime/contracts/yi-runtime-touch.ts`; Occasion contracts are under
`packages/core/src/occasion/`; the settlement outbox port is
`packages/core/src/settlement/service/ports/outbox.ts`; and remote capability references are in
`packages/core/src/authority/service/certificates/remote.ts`. PG coverage now uses
`*.integration.test.ts`, including `packages/server/src/pg-outbox.integration.test.ts` and
`packages/server/src/occasion-commit-log-pg.integration.test.ts`.

Do not use this memory as a completion claim, owner-lane queue, baseline-red ledger, or source of
suite counts. Start at `docs/yi/49-structural-arc/HANDOFF.md` and apply
[[verification-regime-2026-08-14]].
