---
name: multi-agent-dispatch-pin-working-dir-verify-before-commit
description: "When dispatching many parallel agents with Edit tool, some may write to wrong worktree if working dir isn't enforced; always git-status before commit; recovery via patch+3way"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 60cba10e-e303-4834-b561-ccbb9850a7f1
---

When dispatching ≥ 5 parallel agents over the same repo's docs/code, **at least one agent may edit files in the wrong worktree** even when the prompt says `Working dir: <path>`.

**Why**: The Agent tool sandbox honors absolute paths the agent uses with Edit/Write. If the agent picks an absolute path from a `find` / `ls` against the main repo (e.g., `/Users/ren/repos/<repo>/<file>` instead of `/Users/ren/repos/<repo>/.claude/worktrees/<x>/<file>`), the edit lands outside the worktree silently. The agent's report still claims success because Edit returned OK.

**How to apply**:
- Before committing, **always** `git status` *and* `git -C <main-repo> status` to see whether any agent edits leaked outside the worktree.
- If they did, recover via:
  ```
  git -C <main-repo> diff <scope-paths> > /tmp/patch
  git apply --3way /tmp/patch    # in worktree
  git -C <main-repo> restore <scope-paths>
  ```
- In future prompts, explicitly instruct agents to use **relative paths from the working dir** (e.g., `docs-next/00_start/foo.md` not `/Users/ren/.../docs-next/00_start/foo.md`) for Edit/Write. Or chdir into the worktree before file operations.

**Concrete instance (2026-05-21)**: Doc-sync Agent E wrote edits for 8 files under `docs-next/00_start/` to the main repo (on `codex/gut`) instead of the worktree branch `claude/quirky-wiles-2fc4ff`. Recovered via the 3-way patch above; merged into [[2026-05-21-doc-sync]] (commit `dbb0758` amended).
