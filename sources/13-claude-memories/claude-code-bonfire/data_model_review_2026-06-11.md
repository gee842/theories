---
name: data_model_review_2026-06-11
description: "Current Yi row, structural-write, schema, and PostgreSQL event invariants"
metadata:
  node_type: memory
  type: project
  originSessionId: ac220a84-37fc-40ef-b925-e07036d8421d
  modified: 2026-08-15
---

Verified current invariants:

- `packages/core/src/model/yi/yi.ts` defines one physical Yi row shape. `kinds[]` is ordered, `kinds[0]` is the primary lineage, and face data lives in kind-keyed `dimensions`.
- `PATCH_PROTECTED_KEYS` and `patchDimensions` in `packages/core/src/engine/deployment/kind-operations.ts` keep structural fields off generic patch paths; custody, identity, membership, and lifecycle changes use dedicated verbs.
- `packages/core/src/compiler/schema/validate.ts` validates `rowSchema` writes and enforces a kind's `payloadShape` at mint.
- `parentUid` is the universal containment home; storage exposes indexed `childrenOf` reads. Lifecycle writers pair row changes with their events transactionally.
- In `packages/server/src/pg-storage/events.ts`, ambient kernel events may retain a witness with `witness_seq` null. Caller-supplied witnesses receive the allocated sequence; do not add a schema check that rejects the ambient form.

Run unit tests with `pnpm test`. Run PostgreSQL integration coverage with `PG_URL=postgres:///bonfire_test pnpm test:integration`; the runner must fail when `PG_URL` is absent.

The old branch/merge report, migration-number diary, suite counts, stale paths, and proof-language inventory are superseded by the live files and [[verification-regime-2026-08-14]].
