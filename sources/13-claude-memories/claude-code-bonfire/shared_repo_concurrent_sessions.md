---
name: shared-repo-concurrent-sessions
description: "OWNER RULE: multiple sessions share this checkout; never reset, stash, checkout --, clean, or stage broadly. Stage explicit owned paths only."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 006a7a79-5a05-4eb6-93b6-149e4d3dfd03
  modified: 2026-07-26T10:48:52.627Z
---

Multiple agent sessions work in `/Users/ren/repos/bonfire` on the same working
tree and checked-out branch. Treat every unrelated modification, untracked file,
index entry, and newly appearing commit as another session's work.

Operational rules:

- Never run `git reset` (including `--hard` or `--soft`), `git stash`,
  `git checkout --`, `git clean`, or any other tree-wide restore/rewrite.
- Never run `git add -A`, `git add -u`, or stage a directory. Stage only the
  explicit files owned by the current task.
- Before committing, inspect `git diff --cached --name-only` and the staged
  diff; every staged path and hunk must belong to the current task.
- To restore one owned tracked file to `HEAD`, use the path-targeted form
  `git show HEAD:<path> > <path>` after verifying the exact path. Never apply it
  to a file another session may be editing.
- Do not rewrite shared history or switch branches merely to isolate work.
  Another session may commit while the task is running, so re-read status and
  the recent log before any commit.
- Tell delegated agents the same rules and forbid them from touching git state
  unless their task explicitly owns that operation.

These safety rules are independent of verification-gate cleanup; stale gate
ceremony never authorizes destructive git operations.
