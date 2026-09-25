---
name: worktree-node-modules-trap
description: Worktrees under .claude/worktrees/ have no node_modules, so bare @context-runtime/* imports silently resolve to the MAIN checkout's live sources.
metadata:
  type: project
---

Git worktrees under `.claude/worktrees/` are created without their own `node_modules`.
Node/vite resolution therefore walks up past the worktree root to
`/Users/ren/repos/context-runtime/node_modules`, whose pnpm workspace links point at the
**main checkout's** `packages/*` — not the worktree's.

Consequences, both hit on 2026-08-21:
- Any script run in a worktree that imports a bare `@context-runtime/*` specifier reads main's
  working tree. Regenerating a committed artifact this way produces a diff against a source the
  worktree does not contain.
- `vitest` in a worktree fails to resolve package-level devDependencies (e.g. `ajv`, a
  `packages/session` devDep installed at `packages/session/node_modules/ajv`) because only the
  ROOT `node_modules` is reachable. Pre-existing tests fail to even load.

Before doing anything in a worktree: compare `git rev-parse HEAD` against the main checkout's.
If they differ, fast-forward the worktree first — resolution is only safe while both trees are at
the same clean commit. A `ln -s <main>/packages/<pkg>/node_modules packages/<pkg>/node_modules`
makes a suite runnable, but remove it afterwards: it silently reads main once the trees diverge.

Related: [[session-schema-artifacts-are-generated]]
