---
name: rpc-write-surface-unified
description: "Current RPC registry: typed schema + exhaustive method tuple, yi substrate writes, product write facades, kit deployment, and unified Yi persistence."
metadata: 
  node_type: memory
  type: project
  originSessionId: 3188f256-d113-4f31-99e2-c70ddfd71597
---

The former `yi.manifest` + `kinds.deploy`-only description is superseded.
The public substrate create method is now `yi.create`, kind declarations deploy
through `kits.deploy`, and product-level write methods are intentionally present.

Current verified shape:

- `RpcSchema` is declared in `packages/sdk/src/client/rpc-schema.ts`; the
  exhaustive runtime tuple is `packages/sdk/src/client/rpc-schema/methods.ts`.
  Adding or removing a schema key requires changing `RPC_METHODS` in the same
  code change.
- Public substrate writes include `yi.create`, `yi.invoke`, `yi.extinguish`,
  `yi.addKind`, and `yi.removeKind`, plus explicit relation lifecycle methods.
  Product facades include capability, currency, membership, group, and envelope
  writes. Kind authoring is `kits.plan` / `kits.inspect` / `kits.deploy`; the
  public `kinds.*` methods are reads.
- Server method-form dispatch is the typed `METHODS` registry in
  `packages/server/src/methods/registry.ts`. `packages/server/src/rpc.ts` and
  `packages/server/src/eval.ts` share that registry for dotted methods; eval's
  compact forms additionally use the core wire-verb table.
- The Postgres adapter is decomposed under `packages/server/src/pg-storage/`
  and persists unified Yi rows with stored `kinds` and kind-keyed `dimensions`.
  Database suites belong to `pnpm test:integration` with
  `PG_URL=postgres:///bonfire_test`; see [[verification-regime-2026-08-14]].
