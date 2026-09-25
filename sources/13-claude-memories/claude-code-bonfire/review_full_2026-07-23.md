---
name: review-full-2026-07-23
description: "Historical full-review snapshot; retain only shared-checkout safety and the current-use caveat"
metadata: 
  node_type: memory
  type: project
  originSessionId: d6e6a613-daff-46e2-b10e-86c9a5a182b8
  modified: 2026-08-15T00:00:00.000Z
---

This is a point-in-time review of commit `94f0f305`, not a current repository
health report. Its scores, regression list, gate failures, phase percentages,
test counts, paths, and follow-up status are intentionally omitted: inspect the
current tree and run the current checks before acting. The Gates and Build/test
sections of repository `CLAUDE.md` supersede its verification framing; see
[[verification-regime-2026-08-14]].

**Durable shared-checkout safety:** never use `git reset`, `git stash`,
`git checkout --`, `git clean`, or `git add -A` in a shared checkout. Commit
early and stage explicit paths. To restore one tracked path, inspect it first,
then use `git show HEAD:<path> > <path>`; do not perform broad restores.
