---
name: SDK is a kit, not a values enforcer
description: Don't bake anti-pattern preventions into the Bonfire SDK kernel — build what we want, leave the rest open
type: feedback
originSessionId: b6dea1de-b7e9-44df-ac08-48c803826c9d
---
When designing Bonfire SDK primitives, do NOT propose mechanisms that prevent users from building things we disapprove of. No kernel-level leaderboard refusals, no mandatory consent checks for generators, no friction-as-deterrent, no required sunset clauses on metrics. The kit is descriptive of possibility space, not prescriptive of values within it.

**Why:** Ren repeatedly corrected the pattern of dressing up
Western-democratic or individualist defaults as "neutral SDK design." Those
are values impositions disguised as kernel decisions. Communities choose
governance shapes the SDK cannot anticipate; pre-emptive structural
prohibition is itself paternalism. Bonfire's "build for the world we want,
don't engineer against the worlds we don't" stance is load-bearing.

**How to apply:** Build strong opinionated defaults in the *standard
distribution* (curated generators, worldview-bearing spirits, healthy default
compositions, leaderboards-not-as-primitives). Do not add friction,
prohibitions, required checks, or measurement refusals at the kernel/primitive
layer. If something becomes harmful in practice, respond contextually rather
than pre-emptively. Measurement is a tool; do not turn refusal to measure into
dogma.

The live rare exception is the human automation boundary. The
`CORE_API_KEYABLE` definition in
`packages/core/src/runtime/bootstrap/seed-principals.ts` has an add gate that
refuses a target carrying `core:human`, and the human Kind is frozen. That
protects human agency; it does not authorize general values enforcement in the
kernel. The current explanation is `docs/concepts/unified-class.md`.
