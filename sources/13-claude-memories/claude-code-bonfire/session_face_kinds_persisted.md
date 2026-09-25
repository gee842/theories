---
name: session-face-kinds-persisted
description: "Session identity is persisted as core:spirit + core:membered + core:streamed; there is no session face discriminator, and Yi projection remains faithful to stored kinds."
metadata: 
  node_type: memory
  type: project
  originSessionId: 51a01b16-42b4-4401-b1ab-5444c2cea61e
---

The old `{ face: 'session' }` / `sys/session` description is superseded by the
trait-based session model.

- `CreateSpiritInput` in
  `packages/core/src/identity/service/principals/spirit-create.ts` has a required
  `kind` and no `face`. `createSpiritRow` creates ordinary spirit-shaped rows;
  anchored sessions are created through `createAnchoredSession`.
- A product session normally has origin kind `core:chat` and persistently
  composes `core:spirit`, `core:membered`, and `core:streamed`. `isSession`
  checks the stored presence of those three kinds; it does not inspect a
  projection-only marker.
- `spiritToYi` in
  `packages/core/src/runtime/composition/current-yi-read-source.ts` copies the
  stored kind list and dimensions. Do not synthesize session traits during
  projection: storage queries and `isSession` must observe the same row shape.
- `packages/server/src/pg-storage-session-kinds.integration.test.ts` exercises
  the Postgres round trip, `byKind('core:streamed')`, public
  `where({ kind: 'core:streamed' })`, anchored-path uniqueness, and DM pair
  re-resolution.

See [[session-architecture]] for creation and product behavior.
