---
name: grab-bag-dissolution-finished
description: "Current handler and test-fixture boundaries after the grab-bag dissolution"
metadata:
  node_type: memory
  type: project
  originSessionId: 98d84781-4f72-4bc2-bdb2-ea557e4b574d
---

Current facts, verified 2026-08-15:

- `@bonfire/std/social` owns the friendship-request and calculator declarations
  and handlers; deployable kinds declare callable behavior through `ports`.
- `@bonfire/std/agent` owns agent equipment/persona helpers and
  `turn.inspect`/`turn.cancel`/`turn.replay` handlers.
- Server startup installs both kits. Core tests use
  `packages/core/src/test-utils/generic-fixture.ts` rather than duplicated
  product vocabulary.

Historical merge/test counts and process lore are superseded by
[[verification-regime-2026-08-14]] and the current `CLAUDE.md` commands.
