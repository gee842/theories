---
name: kit-index-race-fix
description: "Community kit collections avoid lost updates with single-writer referent children; locks remain only for true single-winner transitions"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e3985d0-de30-4998-863d-3ae6a1964644
---

The old shared-container-lock fix has been superseded by a stronger data model. Community collections no longer append uids into mutable container arrays such as `wishes[]`, `needs[]`, or `entries[]`. Each entry is its own `core:holding` child with `core:holding.referent` pointing at the container; list operations use the indexed referent query and active-state filter. Concurrent writers therefore mint independent rows and cannot clobber one shared cell.

This pattern covers the main community kits and incubator subcollections. Release removes an entry from the live collection by deactivation, not by filtering and rewriting a container array. The current regression coverage is in:

- `packages/std/src/community/kit-index-race.fix.test.ts`
- `packages/std/src/community/incubator/kit-index-race.fix.test.ts`
- `packages/server/src/kit-index-race.integration.test.ts`

True single-winner state still needs serialization. `need-wall` claim/fulfilment and `farewell.complete` use `ctx.atomicOn(writtenRowUid, ...)`, re-read the row inside that atomic unit, and admit one transition before enqueuing any second-domain effect. Lock by the row whose first-writer-wins field changes, not by its surrounding collection.

The memory-adapter payload-aliasing incident is also closed: current memory event append and row reads clone stored values. Callers should still treat returned data as immutable, but no lock or event-reseal ritual remains from the old design.
