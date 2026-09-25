---
name: review-sdk-design-2026-06-11
description: "Current SDK review invariants: unified Yi authoring, wire/in-process port parity, and executable consumer checks"
metadata:
  node_type: memory
  type: project
  originSessionId: d6c0e299-2663-4052-bc8f-cf05fab7f8aa
---

The June 2026 score, agent tally, transcript references, and defect inventory are
historical; do not treat them as current SDK status. The current implementation
supersedes that review:

- `packages/sdk/README.md` and `packages/sdk/package.json` define the supported
  surface. New authoring uses `defineKind`, `definePort`, and `defineHandler`;
  application access uses `BonfireClient`, `client.yi(uid)`, product facades,
  and the typed helpers exported from `@bonfire/sdk/client/typed`.
- Wire `yi.invoke` in `packages/server/src/methods/handlers/yi.ts` delegates to
  `invokeYi` in `packages/core/src/runtime/invocation/runtime-invoke.ts`.
  Kind-declared ports resolve through the same runtime port path used by
  in-process invocation; built-in substrate verbs are the fallback. Coverage
  for wire invocation, discovery/explanation agreement, and argument-schema
  rejection lives in `packages/server/src/wire-port-invoke.test.ts`.
- `packages/sdk/src/public-surface.test.ts` and
  `packages/sdk/src/public-types-surface.test.ts` guard the supported exports.
  For an SDK-facing change, the change author runs `pnpm check:release`; its
  current root script covers type, SDK unit, browser, packed-consumer, and docs
  regressions, and the change author owns any failure.

Review the live exports and executable consumer paths, not old prose scores or
workflow artifacts. Verification ceremony from the original review is
superseded by [[verification-regime-2026-08-14]].
