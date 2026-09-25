---
name: single-writer-children-shipped
description: Container collections use single-writer child rows aggregated at read
metadata:
  node_type: memory
  type: project
  originSessionId: fa811709-ac5d-4f74-be07-24034ee8057f
---

The current container-collection rule is documented and exercised at
`docs/cookbook/13-container-collection.md`: a collection is a set of child Yi
rows carrying `core:holding.referent = container`, never a mutable uid array on
the container. Add with `manifest`, list/count through the appropriate
subject-first `ctx.as(...)` view using `{ referent, kind, active: true }`, and
remove with `deactivate`. Independent rows remove the lost-update race and need
no collection lock.

Load-bearing details:

- Query by `kind`, not `originKind`; register-only kinds may have no
  `originKindUid`.
- Choose the read subject from the collection's visibility contract. Current
  public kit aggregates commonly use `ctx.as(ctx.systemCaller)`; private
  collections use `ctx.as()`.
- Query order is newest-first by `seq`; sort explicitly when a product needs
  chronological display.
- Sub-row collections use the same shape with `referent` set to the parent
  item. Genuine first-writer-wins transitions use `ctx.atomicOn` and re-read
  inside the unit; the old `kitCasLocks`/`community/locks.ts` mechanism is gone.
- `activeOnSpawn` is a real `ManifestInput` option and defaults to active.

The cookbook retains the invariant, but current source wins where its older
reader and lock examples disagree. Historical suite counts are superseded by
[[verification-regime-2026-08-14]].
