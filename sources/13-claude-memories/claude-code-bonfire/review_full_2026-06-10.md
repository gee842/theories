---
name: review-full-2026-06-10
description: "Historical June 10 review; current durable handoff is typed authoring, runtime schema enforcement, and click-gated/read-only sigils"
metadata:
  node_type: memory
  type: project
  originSessionId: 1c69fca0-08a8-4d45-8b30-5a08b12a8dac
---

This was a product/architecture review at commit `c1369ac`. Its commit totals,
suite totals, package counts, branch instructions, and source-layout inventory
are historical and must not be used as current operating facts.

**Durable follow-up, re-verified 2026-08-15:**

- Typed authoring is live and first-party exercised. `definePort` and
  `defineKind` are implemented in
  `packages/sdk/src/authoring/class/definitions.ts`; `defineBonfireApp` and
  `createTypedClient` are implemented in
  `packages/sdk/src/client/typed-client.ts`. Standard product kits under
  `packages/std/src/platform/product-kits/` define typed apps, and
  `docs/examples/typed-wishing-pool/index.ts` invokes through a typed client.
  The old finding that this surface had zero first-party users is false.
- A port's declared schema is enforced before handler execution in
  `packages/core/src/runtime/invocation/port-execution.ts`.
  `SchemaInvalid` and `SchemaIncompatible` remain public core error codes in
  `packages/core/src/kernel/errors.ts`.
- Message-rendered sigils do not execute merely because a message is viewed.
  `packages/chat-bonfire/src/renderers/sigil.tsx` click-gates both inline and
  panel execution, while
  `packages/sigil-bonfire/src/sigil-bonfire-sdk.ts` exposes a read-only method
  set by default and requires explicit host opt-in for the full surface.
- Use the current commands in `CLAUDE.md`: `pnpm typecheck`,
  `pnpm typecheck:tests`, and database-free `pnpm test`; run
  `PG_URL=postgres:///bonfire_test pnpm test:integration` for integration
  suites. Do not reuse this review's historical green counts as a baseline.

The former gate/evidence assumptions and landing-by-landing verification
ceremony are superseded by [[verification-regime-2026-08-14]].
