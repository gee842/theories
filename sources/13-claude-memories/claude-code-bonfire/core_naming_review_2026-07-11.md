---
name: core-naming-review-2026-07-11
description: "Current Core vocabulary authority and the surviving route-name invariants"
metadata:
  node_type: memory
  type: project
  originSessionId: 0fdaaa78-7462-4463-ac52-288903154687
  modified: 2026-08-15
---

`CLAUDE.md` and `docs/VOCABULARY.md` are authoritative. New identifiers use one current word per concept; `token`, `item`, `relationship`, `class`, `cls`, `type` as a synonym for kind, and `spawn` are banned. Storage-level uid prefixes, persisted dimension fields, marker ids, and durable event kinds remain frozen data.

Current useful landmarks:

- `packages/core/src/model/yi/yi.ts` defines the one Yi row shape.
- `packages/core/src/model/kinds/ref.ts` contains the single `CORE_KINDS` bag.
- `packages/core/src/model/kinds/holding-route.ts` is the shared holding-route authority; its order is capability, edge, then attestation.

The old file/word counts, three-strata census, dictionary proposal, byte-pin explanation, and phase plan are stale. Current vocabulary law and [[verification-regime-2026-08-14]] supersede them.
