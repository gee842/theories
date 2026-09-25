---
name: pg-test-suite-lock
description: "Unit/integration split and the machine-wide advisory lock for PG-backed test invocations"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4a4cc58d-b76d-49a6-b31b-50fcf96e8423
---

`pnpm test` is the database-free unit loop and excludes
`*.integration.test.ts`, whether or not `PG_URL` is set. Run the PG suites with:

`PG_URL=postgres:///bonfire_test pnpm test:integration`

`vitest.integration.config.ts` selects only integration files, runs files
serially, and uses `packages/server/scripts/pg-integration-setup.ts` to fail
loudly when `PG_URL` is absent.

PG-backed invocations acquire the session advisory lock implemented by
`packages/server/scripts/pg-test-suite-lock.ts`. Many suites use fixed schema
names and drop/recreate them, so concurrent sessions against the shared test
database would otherwise destroy one another's schemas. If the runner prints
`[pg-suite-lock] ... waiting`, leave it queued; disconnecting releases the
session lock. A custom Vitest config that bypasses the shared setup also
bypasses this protection.

This split supersedes the former PG-gated default suite and any red-suite
inventory. See [[verification-regime-2026-08-14]].
