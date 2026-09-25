---
name: review-full-2026-06-13
description: "Historical June 13 review; current durable handoff is storage-backed edge uniqueness and its limits"
metadata:
  node_type: memory
  type: project
  originSessionId: f486b9fc-8c69-47a1-9027-76951ac0859c
---

This was a review at commit `3c9a3d69`. Its suite totals, branch state,
source-line references, resolution checklist, and merge-process proposals are
historical rather than current operating facts.

**Durable follow-up, re-verified 2026-08-15:**

- The `core:unique-edge` backstop is live. Its marker is
  `CORE_KINDS.uniqueEdge` in `packages/core/src/model/kinds/ref.ts`.
  `packages/core/src/adapters/memory/storage-base.ts` rejects duplicate live
  marked edges in memory, and `packages/server/migrations/001_init.sql`
  defines the corresponding PostgreSQL partial unique indexes. Memory behavior
  is covered by `packages/core/src/model/tests/live-edge-unique.test.ts`; the
  PostgreSQL race is covered by
  `packages/server/src/write-path-atomicity.integration.test.ts`.
- The constraint applies only to relation kinds carrying the relevant
  uniqueness marker. It does not make arbitrary read-then-write deduplication
  race-safe. In particular, `oncePerMember` in
  `packages/std/src/platform/app-record.ts` is explicitly best-effort: two
  concurrent submits can both pass its pre-mint scan.
- Two former review items are closed in the current shape:
  `packages/core/src/engine/deployment/kind-removal.ts` explicitly refuses
  removal of a row's origin kind, and
  `packages/std/src/community/incubator/ritual.ts` represents occurrences and
  attendance as independent child rows rather than appending to shared arrays.
  The schema DSL also exposes `t.integer()` in
  `packages/sdk/src/authoring/schema.ts`.

Do not turn the old evil-merge lesson into a merge-content guard or other
meta-gate. Current gate law and the retirement of verification ceremony are in
[[verification-regime-2026-08-14]].
