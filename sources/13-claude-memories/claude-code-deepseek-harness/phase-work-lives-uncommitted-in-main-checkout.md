---
name: phase-work-lives-uncommitted-in-main-checkout
description: "Desktop-phase work happens in the main checkout on branch worktree/agentic-web-desktop; finished phases are committed one commit per phase after review, the in-flight phase stays uncommitted"
metadata:
  node_type: memory
  type: project
  originSessionId: 1dede0ed-8778-456f-9c73-481c825aea16
  modified: 2026-08-30T14:32:01.073Z
---

The agentic-web-OS phases (see [[deepseek-harness-working-style]]) are built in the main checkout `/Users/ren/repos/deepseek-harness`, now on branch `worktree/agentic-web-desktop` (no longer uncommitted-on-master as in the phase-1 era). Completed phases land as one reviewed commit each (`feat(...): ... (phase N)` + implemented Agent Note); the phase currently under review sits as working-tree changes only. As of 2026-08-30 phases 1–5 and 7 are all committed and the tree is clean: phase 5 landed as `a01d84d5deaf` on Ren's explicit instruction, with the manifold split plan note committed just beneath it (`05eff9b7d2`). Post-phase-5 work continues in the separate manifold repo — see [[manifold-product-split-state]].

**Why:** Ren reviews each phase as a git diff before it becomes a commit; committing is their act (or explicitly delegated).

**How to apply:** never `git add`/`commit`/`stash` the in-flight phase; run gates with `export PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH"` per [[node-version-for-deepseek-harness]]. Gotcha learned in phase 7: a new `apps/web/tests/*.e2e.ts` host-face lane must be added BOTH to `tsconfig.host.json`'s include list AND to `apps/web/tsconfig.json`'s `exclude` array — missing the exclusion makes `tsc -b` pull host sources into the web project and emit stray `.js/.d.ts` artifacts INTO `src/` dirs across half the repo (delete the untracked twins; they broke lint with ~1130 errors).
