---
name: ctx-transfer-verbs-shipped
description: "Current handler custody verbs and Kind authoring feature surface"
metadata:
  node_type: memory
  type: project
  originSessionId: 6868a65f-d851-417a-a867-51c960e1117a
  modified: 2026-08-15
---

`PortHandlerContext` in `packages/core/src/runtime/contracts/handler-context.ts` exposes `transfer`, `activate`, and `deactivate`. They route through the custody lifecycle machinery rather than generic patching, and emit the corresponding lifecycle events in the same transaction as the row write.

The default actor is `ctx.caller`; privileged kit-controlled moves must opt in explicitly with `ctx.systemCaller`. Structural fields such as holder and active state remain protected from `ctx.patch` by `PATCH_PROTECTED_KEYS` in `packages/core/src/engine/deployment/kind-operations.ts`.

Kind authoring's `features` field is declared in `packages/core/src/compiler/declaration-ingress/kind-authoring-v1/input.ts` and typed by `HoldingFeature` from `packages/core/src/model/custody/features.ts`. Plain runtime functions may use the runtime subject surface (`rt.as(caller).deactivate(...)`); port handlers should use their context verbs.

`packages/core/src/engine/tests/port-handler-ctx-verbs.test.ts` covers the live contract. The old duplicate-branch story, deleted test filename, loose task chip, commit handles, and counts are superseded by [[verification-regime-2026-08-14]].
