---
name: structure-remediation-2026-06-11
description: Durable module-separation facts after later structural work
metadata:
  node_type: memory
  type: project
  originSessionId: 4512a8a8-9e98-4175-a7e1-54f3ac1fc0e6
---

The durable result of the old remediation is the single typed server method
registry: `packages/server/src/methods/registry.ts` defines
`METHODS: { [M in MethodName]: MethodEntry<M> }`, assembled from bounded
handler tables. RPC and dotted eval dispatch share it.

The SDK/runtime parity surface remains under `packages/sdk/src/testing/`, with
`substrate-parity.test.ts` covering the in-memory test substrate against the
runtime. In std, the named raw Yi read boundary is
`packages/std/src/raw-yi.ts`; `packages/std/src/raw-storage-read-ceiling.fix.test.ts`
guards that exception. Do not reintroduce ad-hoc `(rt as any).storage` writes.

The old directory map, suite counts, and one-time audit claims are stale. For
moves and renames, run both `pnpm typecheck` and `pnpm typecheck:tests`; use
`PG_URL=postgres:///bonfire_test pnpm test:integration` for database coverage.
Gate policy is [[verification-regime-2026-08-14]].
