---
name: merge_drop_audit_2026-06-11
description: "June 2026 merge-drop verdict plus a reusable merge-tree diagnostic; current auth coverage lives in integration suites"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4a4cc58d-b76d-49a6-b31b-50fcf96e8423
---

The 2026-06-11 audit found no dropped changes. The useful diagnostic is to
list the relevant merge commits, compute Git's merge tree for each merge's two
parents with `git merge-tree --write-tree M^1 M^2`, and diff that tree against
`M`. A non-empty diff identifies a recorded merge result that differs from
Git's computed merge and needs human inspection. Also inspect later reverts
before concluding that a merge lost content.

The apparent loss was stale integration coverage. The current files are
`packages/server/src/server-auth.integration.test.ts` and
`packages/server/src/server-wallet-auth.integration.test.ts`; they assert that
human-as-principal responses contain `token` and `subjectId`, carry no default
`agentId`, revoke old bearers, and mint fresh credentials on sign-in. Run them through
`PG_URL=postgres:///bonfire_test pnpm test:integration`.

The old suite count and default-suite explanation are superseded by the unit /
integration split in [[verification-regime-2026-08-14]]. See also
[[pg-test-suite-lock]] and [[shared_repo_concurrent_sessions]].
