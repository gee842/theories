---
name: worktree-dsh-submodule-init
description: Fresh manifold worktrees need the dsh submodule initialized with the file transport explicitly allowed
metadata: 
  node_type: memory
  type: project
  originSessionId: 2e444289-08b6-46f2-9edb-6b88bbe6d3f6
  modified: 2026-08-31T06:24:59.344Z
---

A fresh git worktree of manifold has an empty `dsh/` submodule, and every pnpm command fails with `ERR_PNPM_WORKSPACE_PKG_NOT_FOUND` (only ~95 of 285 workspace projects found) because pnpm's verify-deps-before-run triggers an implicit install without the dsh workspace members. The submodule URL is the local path `/Users/ren/repos/deepseek-harness`, which git's default `protocol.file` policy refuses to clone ("transport 'file' not allowed").

**Why:** Worktrees don't inherit the main checkout's submodule contents, and the CVE-mitigation default blocks local-path submodule clones.

**How to apply:** In the worktree run `git submodule update --init`, then `pnpm install`. Also select the pinned node first: `export PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH"`. Since 2026-08-31 the submodule URL is `../deepseek-harness.git` resolved through origin to `https://git.datong.to/ren/deepseek-harness.git`, so the fetch is HTTPS and the `protocol.file.allow` flag is only needed if the URL is ever pointed back at a local path.
