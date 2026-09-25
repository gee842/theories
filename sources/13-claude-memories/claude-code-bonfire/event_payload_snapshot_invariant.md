---
name: event-payload-snapshot-invariant
description: "Memory events snapshot payloads on append for PostgreSQL parity; memory event reads intentionally remain live"
metadata:
  node_type: memory
  type: project
  originSessionId: c2c2be40-ff06-4fc8-b94a-7f3d9d46ec5f
---

`packages/core/src/adapters/memory/storage.ts` uses
`structuredClone(ev.payload)` in both `events.append` and `appendVerbatim`.
The caller's object therefore cannot mutate the content-addressed and signed
event after the write. This matches PostgreSQL's JSONB serialization boundary.

Memory `readSince` and `readByYi` deliberately return live event references.
`packages/core/src/identity/service/signing/event-signing-no-seq-binding.test.ts`
mutates a returned payload to simulate stored corruption and verifies that the
next read rejects it. Do not add clone-on-read or deep-freeze without replacing
that corruption-test mechanism and its intended semantics.

Yi row reads are different: `packages/core/src/adapters/memory/yi-repo.ts`
returns clones, so row consumers must persist changes through the write
surface. Earlier paths, performance figures, and landing transcripts are
superseded by these current paths and [[verification-regime-2026-08-14]].
