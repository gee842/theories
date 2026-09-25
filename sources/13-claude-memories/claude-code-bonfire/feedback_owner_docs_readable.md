---
name: feedback-owner-docs-readable
description: Owner-facing docs must be plain-language decision narratives; implementation detail belongs only where an executor needs it
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3839d657-7523-4b60-9f9a-90f1a0d1216b
---

On 2026-06-12 the owner called the platform proposal "very hard to read and
understand." The proposal had been written like an execution spec: dense
citations, cross-spec ids, and substrate jargon. Right content, wrong
audience. The revised historical proposal now lives at
`docs/archive/proposals/platform.md`.

**Why:** proposals exist for the owner to make decisions. If the owner can't read it, it fails regardless of correctness. Spec-grade density is for cold executing agents, not for [[user_role]] (founder/designer who reviews design narratives and answers open questions).

**How to apply:** owner-facing proposals and decision docs use a plain-language
narrative, a running example, explicit decisions, and open questions with
shippable defaults. Avoid file:line citation walls and internal phase codes.
Put implementation detail in the active execution note only when an executor
actually needs it, and state that the owner-facing proposal owns decisions.
The archived split between `docs/archive/proposals/platform.md` and
`docs/archive/plans/consolidation/P3-implementation-notes.md` is a historical
example, not a mandate to create duplicate companion documents.

Do not create an evidence-style companion merely to prove diligence; see
[[verification-regime-2026-08-14]].
