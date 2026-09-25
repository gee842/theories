---
name: round2_sdk_review_fixes
description: "Current SDK/runtime invariants retained from the June review: typed port handlers, enforced row schemas, mutate-gated kind updates, liveness, and membership-gated DAG reads."
metadata: 
  node_type: memory
  type: project
  originSessionId: c56bcb1f-6f3d-4798-87eb-6d98983ca1ab
---

The old review transcript, commit list, suite counts, register-only-kind routing,
and in-progress notes are historical. Durable kind resolution in
`packages/core/src/engine/resolution/kinds.ts` and the current verification law
supersede those claims; see [[verification-regime-2026-08-14]].

Current verified invariants:

- `PortHandlerRow` and `PortHandlerContext` live in
  `packages/core/src/runtime/contracts/handler-context.ts`; core exports
  `PortHandlerCtx`, and `@bonfire/sdk` re-exports it. Typed `defineHandler`
  binds declared port arguments and row dimensions.
- `defineKind` compiles `t.*`, bare-map, and raw row schemas through
  `packages/sdk/src/authoring/class/normalization.ts`. The recursive validator
  in `packages/core/src/compiler/schema/validate.ts` is used by schema-bearing
  writes. Manifest and patch writes treat the outer bucket as incremental;
  complete writes such as `addKind` enforce top-level required fields.
- Re-adding an installed kind with a changed `init` replaces that dimension
  bucket under `gates.mutate` and emits `yi.kind-mutated`; re-adding without an
  `init` is idempotent. The live contract is exercised in
  `packages/core/src/engine/integration/runtime-yi-extensions.test.ts`.
- Holding liveness in `packages/core/src/engine/custody/cascade.ts` does not run
  an owner-orphan check for a kernel-owned kind whose owner is null.
- Session DAG reads (`currentPath`, `branches`, and `siblingsOf`) call
  `callerMaySeeSession`; a non-member receives an empty result, while an omitted
  caller is the internal/system read.
