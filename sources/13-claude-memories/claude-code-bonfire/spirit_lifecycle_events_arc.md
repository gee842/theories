---
name: spirit-lifecycle-events-arc
description: Current web lifecycle invalidation and invoke dispatch distinction
metadata:
  node_type: memory
  type: project
  originSessionId: 08921de6-c513-49b2-9a42-1e6d743529ed
---

Web lifecycle invalidation lives in `packages/web/src/data/invalidate.ts`.
`SPIRIT_LIFECYCLE_KINDS` covers `yi.manifested`, `yi.identity_updated`,
`yi.renamed`, `yi.reparented`, and `yi.extinguished`.
`isSpiritLifecycleFrame` distinguishes birth/death with the payload's public
`kinds` array (`core:holding` means holding-shaped); the deleted
`payload.face_class` rule is not current.

`renameSession` and `deleteSession` live in
`packages/core/src/runtime/composition/sessions.ts`: rename delegates to
`setIdentity`, while delete uses `burnSpirit`, leaving a tombstone, emitting
`yi.extinguished`, and cascading held rows.

Dispatch still has two entry semantics worth remembering. Wire-facing
`invokeYi` in `packages/core/src/runtime/invocation/runtime-invoke.ts` handles
substrate verbs such as `setIdentity` and holding lifecycle operations, then
delegates declared ports. Direct `rt.yi.invoke` or
`rt.yi.touch({ kind: 'invoke' })` dispatches declared ports through
`dispatchPort`; adding a built-in case to `invokeYi` does not create a declared
port.
