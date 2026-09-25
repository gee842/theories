---
name: doorway-welcome-migration
description: "Doorway and Sage use referent-indexed child rows for newcomers and introductions; there are no shared roster arrays"
metadata:
  node_type: memory
  originSessionId: fa811709-ac5d-4f74-be07-24034ee8057f
---

`packages/std/src/community/doorway.ts` stores both collections as
single-writer child rows. `welcome` mints an active newcomer whose
`core:holding.referent` is the doorway. `introduce` mints an active welcome
Token whose referent is the newcomer. Neither path mutates a shared
`newcomers[]` or `introductions[]` cell or needs a container lock.

`listNewcomers` queries newcomer children by referent and reconstructs each
introduction from welcome-Token children. Graduation is computed lazily from
`joinedAt + graduationDays`; the explicit `graduate` port also persists
`graduatedAt` and deactivates the newcomer.

`packages/std/src/community/sage.ts` derives each doorway family's kind ids and
uses system-view `rt.yi.where(..., undefined)` reads for newcomer and welcome
children. The old half-migrated claim that `introduce` still owned an array,
and its fixed test transcript, are superseded by this current child-row model
and [[verification-regime-2026-08-14]].
