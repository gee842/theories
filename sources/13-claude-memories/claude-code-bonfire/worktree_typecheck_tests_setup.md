---
name: worktree-typecheck-tests-setup
description: "Run verification in the checkout containing the edits; current source mappings remove the old stale-dist workaround"
metadata: 
  node_type: memory
  type: reference
  originSessionId: d7359b57-2903-435e-b4b8-6a918d51040b
---

# Worktree verification and shared-checkout safety

Run every build, test, and git command in the checkout that contains the edits.
Before verification or branch operations, confirm both `pwd` and
`git rev-parse --show-toplevel`; testing the primary checkout while editing a
worktree produces a false green.

In a fresh worktree, install dependencies when absent with `pnpm install`.
`tsconfig.base.json` now maps `@bonfire/*` imports to workspace source and
`vitest.config.ts` aliases tests to source, so the former instruction to build
`packages/core/dist` to avoid the primary checkout's stale declarations is
obsolete.

Use the current loops from `CLAUDE.md`: `pnpm typecheck`,
`pnpm typecheck:tests`, and database-free `pnpm test`. Run PostgreSQL suites
separately with
`PG_URL=postgres:///bonfire_test pnpm test:integration`; they are the
`*.integration.test.ts` suites. See [[verification-regime-2026-08-14]].

In a shared checkout, never use `git reset`, `git stash`, `git checkout --`,
`git clean`, or `git add -A`. Restore only a path you own with
`git show HEAD:<path> > <path>` after checking the target. Preserve all unrelated
tracked and untracked work.
