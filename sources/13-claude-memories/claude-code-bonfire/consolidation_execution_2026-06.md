---
name: consolidation-execution-2026-06
description: "Shared-checkout safety and current verification commands; the 2026 consolidation diary is obsolete"
metadata:
  node_type: memory
  type: project
  originSessionId: 9414f53c-cbf0-4c36-9d4f-11735a97c765
  modified: 2026-08-15
---

This repository is often shared by concurrent sessions. Treat unrelated dirty or untracked paths as another session's work.

- Never use `git reset`, `git stash`, `git checkout --`, `git clean`, or `git add -A` in the shared checkout.
- Stage only explicit paths you own. To restore one owned tracked path without disturbing the index or another session, use `git show HEAD:<path> > <path>`.
- If `.git/index.lock` exists, wait for its owner; never delete it.
- `pnpm typecheck` already runs `tsc --build --force`. Run `pnpm typecheck:tests` after renames, `pnpm test` for the database-free unit loop, and `PG_URL=postgres:///bonfire_test pnpm test:integration` for integration suites.

The old consolidation phases, owner gates, branch/commit handles, merge choreography, red-suite counts, and evidence language are historical and no longer operational. [[verification-regime-2026-08-14]] supersedes them.
