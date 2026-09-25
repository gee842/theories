---
name: grab-bag-dissolution-shipped
description: "Current package boundary for agent/social vocabulary and core boot kinds"
metadata:
  node_type: memory
  type: project
  originSessionId: 98d84781-4f72-4bc2-bdb2-ea557e4b574d
---

Current facts, verified 2026-08-15:

- Agent vocabulary is installed by `installAgentKit` from `@bonfire/std/agent`;
  social/demo vocabulary is installed by `installSocialKit` from
  `@bonfire/std/social`.
- Core boot owns authority kinds through `seedAuthorityKinds` and session
  workflow kinds through `ensureSessionKinds`.
- `system.kinds(refs)` is the generic kind directory. The web maps it to its
  local convenience shape in `packages/web/src/data/useWellKnown.ts`.

The earlier intermediate deviations, follow-up list, suite counts, and
worktree-verification narrative are superseded by the finished boundary above
and [[verification-regime-2026-08-14]].
