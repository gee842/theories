---
name: sdk-separability-review-2026-06-16
description: "Current package boundary retained from the June SDK review; point-in-time product-readiness scores and gap inventories are superseded."
metadata: 
  node_type: memory
  type: project
  originSessionId: 98d84781-4f72-4bc2-bdb2-ea557e4b574d
---

Bonfire's live package direction is still **domain-agnostic kernel plus
composition layers**:

- `@bonfire/core` owns Yi, kinds, authority, storage/runtime ports, streams,
  sessions, and other substrate domains. Its package dependencies are the
  Noble crypto libraries only.
- `@bonfire/sdk` depends on core and exposes client, authoring, agent,
  terminal-custody, and testing entry points. AI-provider packages are optional
  peer dependencies behind the agent entry points.
- `@bonfire/std` depends on core and SDK and composes product/community
  behavior with authored kinds, ports, relations, projections, and handlers.
  It is a private, in-process package, and it still installs some rule hooks
  directly with `rt.registry.set` (for example platform membership and install
  floors). Do not treat std as proof that every behavior is available to an
  unprivileged external SDK package.

The June product-readiness percentages, blocker lists, file-line citations,
and recommended build order are superseded. Ranking materializers, product
write facades, presence/typing signal subscriptions, and the agent surfaces
have all changed since then. Re-audit Discord/Slack/Reddit readiness from the
current product proofs and server implementations rather than reusing those
scores. The durable session model is summarized in [[session-architecture]].
