---
name: ctx-atomic-real-transaction
description: "PortHandlerContext.atomic uses one real transaction; use the tx mirror and expect joined nesting"
metadata:
  node_type: memory
  type: project
  originSessionId: 10de148d-bdb4-4995-8368-d6de8a3e5b2d
  modified: 2026-08-15
---

`PortHandlerContext.atomic` is declared in `packages/core/src/runtime/contracts/handler-context.ts` and built by `makeUArcCtx` in `packages/core/src/runtime/invocation/port-handler-context.ts`. It rebuilds the handler surface over transaction-scoped storage, so a mid-body failure rolls back row writes and their events.

Operational rules:

- Use the callback's `tx` mirror for every verb; captured outer-`ctx` verbs do not join and can self-deadlock on PostgreSQL.
- Nested `atomic` joins the ambient transaction. There are no savepoints, so catching an inner failure does not create a partial rollback boundary.
- `tx.invoke` evaluates and runs the nested port in the same transaction but omits the ordinary touch-audit lifecycle.
- `deploy` is a terminal control transfer: earlier writes roll back and deployment runs under the root declaration lock rather than as one step in the handler transaction.

The current behavior tests are `packages/core/src/engine/integration/port-handler-ctx-atomic.test.ts` and `packages/server/src/write-path-atomicity.integration.test.ts`. Historical commit handles, suite counts, and the old pre-commit subscriber caveat are superseded by the code contract and [[verification-regime-2026-08-14]].
