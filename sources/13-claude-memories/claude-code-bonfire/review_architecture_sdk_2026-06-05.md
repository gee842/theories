---
name: review_architecture_sdk_2026-06-05
description: "Historical architecture-review snapshot; retain only the subtractive-unification heuristic"
metadata:
  node_type: memory
  type: project
  originSessionId: d21d818f-5983-42e9-9ddf-6ef24c07da92
  modified: 2026-08-15T00:00:00.000Z
---

This is a point-in-time review from 2026-06-05, not a current architecture or
repository-health report. Its file inventory, symbol and API counts, risk
ranking, test claims, and follow-up status are intentionally omitted. The
current target is `docs/yi/README.md`; repository `README.md` distinguishes
that target from the implementation described by `docs/concepts/` and
`docs/sdk/`.

**Durable design heuristic:** a unifying surface should replace superseded
production surfaces instead of leaving parallel APIs indefinitely. Apply that
heuristic only after inspecting the current tree; repository `CLAUDE.md`
governs refactors and explicitly rejects compatibility aliases and deprecation
cycles in this pre-production codebase.

The Gates and Build/test sections of `CLAUDE.md` supersede the review's old
verification framing; see [[verification-regime-2026-08-14]]. The current SDK
product objective lives in [[project-sdk-redesign-objective]].
