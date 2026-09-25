---
name: platform-design-converged
description: Owner-approved community-OS direction, with current address and implementation pointers
metadata:
  node_type: memory
  type: project
  originSessionId: 3839d657-7523-4b60-9f9a-90f1a0d1216b
  modified: 2026-08-15T00:00:00.000Z
---

The owner-approved product direction remains in
`docs/archive/proposals/platform.md`: a community has its own rulebook,
surface, belongings, and one consent door for installs. Views compose into
layouts and tabs; presets and marketplace bundles share the install model;
agents use the same gated ports as people. Its old "one group primitive"
framing is superseded: `docs/concepts/community.md` and `docs/yi/01-frame.md`
define a community as a Yi composing `membered` + `streamed`; a membered
container is not a substrate primitive.

Treat that document as product direction, not current API spelling. The live
implementation is `packages/std/src/platform/`. Communities now use canonical
world addresses `@<slug>` (via `communityAddressOfSlug` in
`packages/std/src/platform/address.ts`), not the proposal's old `c/<slug>`
form. `core:community`, `foundCommunity`, the consent door, presets, subgroup
creation, and graduation are all represented in that package.

`docs/archive/plans/consolidation/P3-implementation-notes.md` is explicitly
superseded for membership mechanics; do not implement its per-community member
kind plan. Use current `docs/yi/` plans and live code for execution details.
See [[session_architecture]] for the matching trait-composition model.
