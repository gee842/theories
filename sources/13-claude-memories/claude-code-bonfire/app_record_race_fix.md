---
name: app-record-race-fix
description: "Current app-record concurrency model: immutable child rows and best-effort one-per-member dedupe"
metadata:
  node_type: memory
  type: project
  originSessionId: dc9b1bec-0f4c-46e7-9666-979dae28db1d
---

`packages/std/src/platform/app-record.ts` no longer uses a container record
array or `SpiritLockManager`. Each submission mints an independent
`core:holding` child whose `referent` is the app container; listing uses
`where({ referent, originKind, active: true })`. Concurrent submissions
therefore cannot clobber a shared collection cell.

The handler stamps `submittedBy` and `submittedAt`. `oncePerMember` is
deliberately best-effort: two truly concurrent submissions by one member may
both pass the child-row scan. Strict uniqueness needs a real shared
serialization/constraint domain.

The old lock + `ctx.atomic`/`FOR UPDATE` repair is superseded. Historical
verification transcripts are not instructions; use
[[verification-regime-2026-08-14]].
