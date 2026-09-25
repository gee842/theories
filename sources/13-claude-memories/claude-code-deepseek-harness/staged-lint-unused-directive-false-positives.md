---
name: staged-lint-unused-directive-false-positives
description: "lefthook staged lint runs oxlint without type info; its \"Unused oxlint-disable directive\" warnings can be false positives for type-aware rules"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2821d33d-4056-4b0b-a667-30e526437804
  modified: 2026-08-27T16:47:22.681Z
---

The lefthook pre-commit `lint (staged)` step runs oxlint per staged file WITHOUT type information, while `pnpm run lint` (and `scripts/run-oxlint.ts`) run type-aware. A directive suppressing a type-aware rule (e.g. `typescript/no-misused-promises`) shows as "Unused oxlint-disable directive" in the staged hook but is load-bearing repo-wide.

**Why:** On 2026-08-27 I removed such a directive from `packages/automation/automation-domain/src/index.ts` because the staged hook called it unused; `pnpm run lint` then failed with `no-misused-promises` at that exact line, and it had to be restored.

**How to apply:** Never remove an oxlint-disable directive on the staged hook's word alone — first run `npx tsx scripts/run-oxlint.ts <package>` (with the nvm 22.22.2 PATH from [[node-version-for-deepseek-harness]]) and only remove it if the type-aware run is also clean. Staged-lint "unused directive" warnings are non-blocking; leaving them is fine.
