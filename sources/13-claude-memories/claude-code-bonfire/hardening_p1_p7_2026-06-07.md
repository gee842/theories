---
name: hardening-p1-p7-2026-06-07
description: "Verified runtime and Sigil hardening facts that remain current"
metadata:
  node_type: memory
  type: project
---

Current facts, verified 2026-08-15:

- Manifest, kind-membership, and dimension-patch state changes commit their
  corresponding `yi.*` events with the row write.
- `patchDimensions` is the shared body behind `rt.yi.patch` and handler
  `ctx.patch`. It validates partial dimension buckets, enforces the structural
  write floor, and is not a client RPC verb.
- `dispatchPort` validates arguments against a declared port schema before the
  handler runs.
- Sigil compilation defaults remain 2,097,152 source characters, an 8 MiB
  emitted bundle, and 30 seconds; `IdbCache` defaults to 500 entries with
  `writtenAt`-ordered eviction.

Use `pnpm typecheck`, `pnpm typecheck:tests`, and `pnpm test` for the unit loop.
Run integration suites separately with
`PG_URL=postgres:///bonfire_test pnpm test:integration`. Old pass counts,
known-red inventories, and verification anecdotes are superseded by
[[verification-regime-2026-08-14]].
