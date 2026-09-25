---
name: principal-ticket-lifetime
description: "The engine mints a runtime's principal-context ticket once at boot with no renewal — stale runtimes lose the whole database and it looks like an RLS/provisioning bug"
metadata: 
  node_type: memory
  type: project
  originSessionId: 816f9b00-5217-42d0-8506-9fd34a8b91bf
  modified: 2026-08-24T11:56:56.145Z
---

In context-runtime-product, a boundary runtime's composition (`createCanonSessionHost` in the vendored engine) mints ONE principal-context ticket at boot and bakes the token into every pool's connection startup options — there is no renewal. When the ticket expires, `ops.context_runtime_principal()` resolves to `''` on every connection: reads answer empty (Lineage shows "0 sessions" over a universe that holds them) and the next turn's first write fails with `new row violates row-level security policy` (typically on `canon.blob_namespaces`). This presents as a fresh-boundary provisioning failure but provisioning is sound.

**Why:** the engine's default TTL (30 min, `issuePrincipalContextTicket`) is sized for per-connection tickets, not a mint-once-per-process composition; the engine caps `ttlMs` at 24h.

**How to apply:** if a turn fails with an RLS violation while `ops.universe_memberships` holds the right owner row, first compare the runtime process's age (`cp.audit` `boundary.runtime.started` / `ps`) against the ticket TTL. Fixed on 2026-08-24 (branch claude/beautiful-wozniak-1e5c0c): the control plane mints with `PRINCIPAL_CONTEXT_TICKET_TTL_MS` (24h, `apps/control-plane/src/provisioning.ts`) and the runtime manager retires every runtime at `RUNTIME_MAX_LIFETIME_MS` (23h, `apps/runtime-manager/src/manager.ts`); gates in `accounts.test.ts` and `runtime.test.ts`. A turn running past retirement is absorbed by the engine's turn-lease recovery.

Related: [[live-deployment-layout]].
