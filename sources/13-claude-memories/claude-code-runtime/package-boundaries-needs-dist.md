---
name: package-boundaries-needs-dist
description: "package-boundaries.ts --write needs pnpm install + tsc -b (dist/) first in a fresh worktree, else it emits a ~26k-line bogus inventory diff"
metadata: 
  node_type: memory
  type: project
  originSessionId: aede50ed-cff4-415f-8ecb-3f087f5db5ab
  modified: 2026-08-15T11:28:11.366Z
---

`bench/scripts/history-core/package-boundaries.ts --write` resolves workspace imports through
each package's `exports` → `./dist/src/*.js`. In a fresh git worktree (no `node_modules`, no
`dist/`) it still "succeeds" but records `B00-export-target ... dist/src/index.js is missing`
under `activePhaseZeroViolations` for every package and the edge graph collapses — a ~26k-line
diff on `specs/history-core/package-boundaries.json`. Observed 2026-08-15 in worktree
`reverent-montalcini-099668`.

**Why:** the inventory is environment-dependent on the build output; the committed file was
written from a built main checkout.

**How to apply:** before `--write` in a worktree run `pnpm install --frozen-lockfile --prefer-offline`
then `pnpm typecheck` (`tsc -b`, ~40s, emits dist). A correct one-file edit then diffs as exactly
two hashes (`packageBoundarySha256`, `sourceSetSha256`). If the diff is huge, dist is missing —
don't commit it. Also: don't put scratch files under `packages/*` — the inventory sweeps
"all workspace source/test/tooling files" and will pick them up. See [[history-core-program]].
