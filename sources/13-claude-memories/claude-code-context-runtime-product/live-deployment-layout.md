---
name: live-deployment-layout
description: "Where the user's live context-runtime-product deployment keeps its database, runtime homes, and logs on this machine"
metadata: 
  node_type: memory
  type: project
  originSessionId: 816f9b00-5217-42d0-8506-9fd34a8b91bf
  modified: 2026-08-24T11:56:32.338Z
---

The user's live (non-test) product deployment on this Mac, as of 2026-08-24:

- Postgres 16 runs at `localhost:55432` (postmaster `-D /Users/ren/repos/runtime/data/postgres-16`); its stderr log file `/Users/ren/repos/runtime/data/postgres-16.log` is stale — the live postmaster's stderr goes elsewhere, so don't rely on it for error forensics.
- The live product database is `context_runtime_product`; the disposable test database is `context_runtime_product_test` (same server). Many other `context_runtime_*` databases on that server are old engine-migration probes.
- Runtime homes (DSH_HOME per boundary) live under `/Users/ren/repos/context-runtime-product/data/runtimes/<boundary-id>/`; `storages/workspace.json` and `storages/session_projcache.json` there are useful forensics (session ids, timestamps).
- product-web runs on port 4000; boundary runtime processes are `dsh --profile <boundary-id>` children, port discoverable via `lsof -p <pid> -a -iTCP -sTCP:LISTEN`, env via `ps eww <pid>`.
- Superuser forensics on engine tables need `SET context_runtime.internal=on` (RLS-forced tables), e.g. `ops.universe_memberships`, `canon.turns`, `ops.principal_context_tickets`; `cp.audit` reconstructs boundary/runtime/ticket timelines.

Related: [[principal-ticket-lifetime]].
