---
name: structural-arc-design-2026-07-12
description: Current Plan 49 pickup, status, and structural cautions
metadata:
  node_type: memory
  type: project
  modified: 2026-08-29
---

The structural owner is `docs/yi/49-structural-arc/`; start every session at
`HANDOFF.md`, not at an archived numbered plan or an old execution audit.

As of 2026-08-29 the arc is on the reset-forward protocol-162 baseline and
the handoff/constitution declare Plan 49 complete, with phases 6/7/8 (P-R,
P-X, S-F) marked certified. Read that status with
[[plan49-completion-review-2026-08-29]] beside it: ownership and structure
hold up, the event-time Yi read does not.

Cautions that still apply:

- An `active` structure-map claim proves ownership and boundaries, not a
  running capability. Verify a production caller before relying on execution.
- `packages/core/structure-map.json` is the sole ownership record;
  `pnpm check:core-structure` derives its counts from it. Do not duplicate
  those counts in a checker.
- Old gate inventories, byte pins, manual registers, proof fixtures, and the
  evidence-per-landing workflow are superseded by
  [[verification-regime-2026-08-14]]. Derive the live `check:*` namespace
  from `package.json`; there is no `check:architecture-shadow` any more.
- `docs/architecture/sdk-one-model-direction.md` is the forward-looking SDK
  north star written against this baseline. It is a direction sketch, not an
  implementation plan, and it lists real unconverged seams (World vs typed
  client vs raw handles, overloaded `Capability`, no general Activation
  model).
