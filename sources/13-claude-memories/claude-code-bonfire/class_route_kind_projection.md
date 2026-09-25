---
name: class_route_kind_projection
description: "Canonical spirit origin projection and ordered kind-port precedence"
metadata:
  node_type: memory
  type: reference
  originSessionId: 21bd1b1d-a2f7-42b1-bf97-ea52922b1a72
  modified: 2026-08-15
---

Current truth:

- `packages/core/src/identity/service/principals/spirit-create.ts` is the structural spirit builder. `createSpiritRow` writes `input.kind` at `kinds[0]`, then the `core:spirit`, `core:identity`, and `core:profile` traits, followed by inherited declared kinds from `resolveKindChain`. Origin and the ordered kind set therefore share one source.
- The `foundCommunity` declaration in `packages/std/src/platform/kinds.ts` gates on `bears('core:human')`. Use the structural human trait for human-only policy; do not recreate the deleted `sys/hero` constructor/marker split.
- `packages/core/src/runtime/invocation/port-resolution.ts` resolves borne ports last-match-wins over ordered `kinds[]`, so a more-derived marker can override a base kind. Spirit behavior is kind-port based; unmatched calls reach only explicit built-in verbs in `runtime-invoke.ts`.

The old `classId` divergence, `sys/hero`, class-method migration diary, commit handles, and suite counts are superseded by the current code and [[verification-regime-2026-08-14]].
