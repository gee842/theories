---
name: ideal-yi-architecture
description: "Current Yi architecture rule: unify declaration, keep execution split by timing, residency, failure, authority, and storage shape"
metadata:
  node_type: memory
  type: project
  originSessionId: c875e246-03f2-42b8-95e3-0dc7cfd560e4
---

The durable verdict is: **unify the declaration and mental model; keep execution split where the runtime contract differs.** The current SDK authoring surface exposes `defineKind`, `defineTrait`, `defineRelation`, `defineProjection`, and `defineReaction`; it does not justify collapsing their execution mechanisms into one reducer.

Current load-bearing splits:

- A Kind's durable `kinds[]` markers and its C3/effective linearization are different views. The latter also folds active grant-bearing holdings and can reject an inconsistent order.
- Session membership lives in `core:membered`; stream state lives in `core:streamed`. Founders are ordinary membership edges plus ownership/authority, not a separate `anchorMembers` roster.
- `ProjectionEngine` currently hosts `roster`, `hot-trait`, and `fold` specs. There is no `gate-decision` projection variant; gate evaluation remains the authority truth.
- Pre-commit veto/transform work, post-commit reactions, and scheduled Automation work have different rollback, retry, and authority contracts and remain separate execution paths.
- Marker, edge, and stream representations are chosen for different cardinality and write/read shapes; they are not interchangeable storage encodings.

The old `sys/reaction` row, S0-S10 build sequence, commit hashes, test totals, and evidence-gated follow-up instructions are historical. Production code has no generic `sys/reaction` kind; current durable reaction authoring is `bonfire.automation/reaction/v1`, while installed legacy Kind reactions remain a compatibility/runtime path. The old design document is now at `docs/yi/archive/08-ideal-architecture.md`.

Verification ceremony in the original memory is superseded by [[verification-regime-2026-08-14]].
