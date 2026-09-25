---
name: feedback-owner-manages-commits
description: "The owner commits this repo themselves; a general \"agree\" to a set of recommendations never authorizes a commit"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c62ec623-0222-46a3-86bd-9b9cbfb4d35b
  modified: 2026-08-15T17:39:47+07:00
---

Do not run `git commit` in this repo. On 2026-08-13 the owner interrupted a
commit mid-flight and said only "continue" — the work itself was wanted, the
commit was not.

**Why:** several sessions share this checkout, and the owner keeps control of
what enters history. Verified work sitting in the working tree is the normal
resting state here, not a problem to be tidied up.

**How to apply:** finish and verify the work, leave it in the tree, and say
plainly what is there. Ask about a commit at most once, then stop asking. Treat
a broad "agree", "sounds good", or "please proceed" as agreement with the
TECHNICAL recommendations only — it never extends to committing. Only an
explicit, unambiguous instruction to commit counts.

This is a shared checkout. Never use `git reset` (in any mode), `git stash`,
`git checkout --`, `git clean`, or `git add -A`. Stage only explicit paths;
avoid `git add -u`, which can collect another session's edits. Inspect
`git diff --cached --name-only` before any explicitly authorized commit. To
restore one tracked path to HEAD after confirming that the path is yours, use
`git show HEAD:<path> > <path>`; never use a broad tree restore. If an index
needs clearing after a mistaken add, `git restore --staged <explicit-paths>`
updates only the index.

Do not merge, rebase, or otherwise rewrite shared history without an explicit
owner instruction for that operation.

Related: [[shared_repo_concurrent_sessions]], [[feedback_no_clarifying_questions]].
