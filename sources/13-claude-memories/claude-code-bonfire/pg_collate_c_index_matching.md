---
name: pg-collate-c-index-matching
description: "Bonfire's C-collated PG indexes match a query only when the comparison names COLLATE \"C\" — plain equality predicates plan as whole-domain scans"
metadata:
  node_type: memory
  type: project
---

`packages/server/migrations/001_init.sql` declares hot-path indexes with
per-column `COLLATE "C"` (e.g. `occasion_effects_target_position_idx
(domain_id COLLATE "C", target_ref COLLATE "C", sequence, ordinal)`).
PostgreSQL matches such an index only when the query's comparison carries the
same collation OID — and a plain `col = $1` carries the *default* collation
OID even when the database default is itself C. Verified 2026-08-29: without
naming the collation, the Occasion observation reads planned as whole-domain
scans (43 ms, 2,484 buffers); with `col COLLATE "C" = $1` the target index
drives (1.0 ms, 5 buffers).

**How to apply:** any query meant to hit a C-collated index must write
`column COLLATE "C" = …` explicitly. The fixed example is the
`commitTargetRef` selection in `packages/server/src/pg-occasion.ts`
(`observationSource`); the plain `targetRef` / `eventOwner` / `eventName`
predicates in the same reader still have the defect (a task chip was filed),
and `eventNamePrefix` needs a semantic decision because collation changes its
range ordering. The plan gate in
`pg-storage-hot-path-indexes.integration.test.ts` re-EXPLAINs the reader's
actual emitted SQL and pins that no effect-log scan is bounded by
`domain_id` alone.
