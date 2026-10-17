# Worktree salvage, 18 October 2026

Ren asked to clean up merged worktrees for disk. Before removal, everything these two worktrees held
that main lacks was copied here byte for byte, with paths kept relative to the repository root.

- `jolly-pike-140c94` (.claude/worktrees, HEAD 52ff83a49, merged into main): the untracked check run
  `20261011T170859.998618Z` with its full logs (main's copy of that run keeps only what main lacked);
  `uncommitted.diff` records its only other change, a deleted `.claude/launch.json` (still in git).
- `review-wt` (/private/tmp scratchpad of session e4915bb3, HEAD 1a78f978b, merged into main): its modified
  `becoming-verification.json` (and `uncommitted.diff` against its HEAD) and its untracked check run
  `20261016T112106.917817Z` (main's copy lacks `version.log`; main's has `RUN-INDEX.json`).

Copies verified with `diff -rq` and `cmp` before the worktrees were removed.
