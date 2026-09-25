---
name: seed-scripts-unified-surface
description: "Current seed/demo entry points and their database requirements; all four seed scripts exist on the unified kind/port surface."
metadata: 
  node_type: memory
  type: project
  originSessionId: 2ff68d51-7945-4acc-95d2-03248ee08cd0
---

The former session-face claim and the statement that `seed-sdk-demo.ts` was
deleted are superseded. Sessions now persist `core:membered` and
`core:streamed` traits; see [[session-face-kinds-persisted]].

Verified entry points:

- `pnpm seed` runs `scripts/seed-sigil-demo.ts` in memory. It seeds the runtime,
  installs std, mints a sigil, sends it through an anchored session, and reads
  canonical content blocks back.
- `pnpm tsx scripts/seed-sdk-demo.ts` is an in-memory SDK authoring demo using
  `defineKind`, `defineKit`, typed handlers, gates, and kit deployment.
- `DATABASE_URL=postgres:///... pnpm tsx scripts/seed-mmorpg-demo.ts` targets an
  already migrated Postgres database and is idempotent by world address.
- `DATABASE_URL=postgres:///... pnpm tsx scripts/seed-hearth.ts <user-ref>`
  targets an already migrated database, accepts a uid or identity address, and
  is idempotent for an existing user's hearth container.

Seed code uses current `{ kind }`, Yi, session, port, kit, and product helpers;
do not revive face/class discriminators or removed per-face runtime namespaces.
The public RPC counterpart is summarized in [[rpc-write-surface-unified]].
