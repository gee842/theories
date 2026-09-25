---
name: event-time-yi-fold-coverage-gap
description: "Event-time Yi reads (yi.read with `at`) were broken at the Plan 49 completion HEAD; fixed by an uncommitted 2026-08-29 wave — durable laws and known limits of the repaired path"
metadata:
  node_type: memory
  type: project
  modified: 2026-08-29
---

At Plan 49's certified HEAD `644460d56`, `yi.read(uid, { at })` threw for any
Yi with a message or a patch (six-plus event names reached
`foldOccasionObservationsToYi`'s throwing `default`), session at-reads
returned `null` (`streams.session.create` folded as an observation), and
context effects never reached the fold at all. A three-wave uncommitted fix
(2026-08-29, this session) repaired it; if those changes are not in the tree,
re-derive from git around that date.

Durable laws the fix established (verified against live commit bytes):

- **Fold committed state, not command echoes.** `canonicalAfterState` is the
  contract-sanctioned exact replay source (observation.ts ~30). Mutating
  events decode it and fail closed when it is absent; command payloads often
  cannot describe the transition (e.g. `advanceLeafTo` is not in the
  active-leaf payload).
- **Every durable mutation co-commits a `yi:<uid>` root advance** — verified
  for identity, custody (transfer included, at
  yi-runtime-custody-transfer-occasion.ts ~170), containment, relations, and
  authority. So `commitTargetRef: yi:<uid>` selects every relevant commit;
  the event-time reader needs no multi-target selection.
- **Coordinates are exact, never prefix, for context owners.** The fold
  filter accepts `yi:<uid>`, `kinds:<uid>/…`, exact
  `identity|custody|containment|relations:<uid>`, and
  `authority:certificate/…` gated on `afterState.rootUid === uid` (one
  commit can carry certificate effects for two Yis). Journal coordinates
  (`custody:transfer/…`, `containment:move/…`, `authority:issuer/…`,
  `kinds:binding…`) never fold into a Yi image.
- **Reconcile producers to fold cases by `targetRef`,** not by grepping
  `eventName:` — producers use two literal shapes (`eventOwner`/`eventName`
  and `event: { owner, name }`) and either grep alone silently misses the
  other. The event-time e2e tests in
  `normalized-yi-read-source.test.ts` (session at-cursor, patch at-cursor,
  transfer pre/post cursor) are the standing guard.

Known, documented divergences of the repaired at-read (not silent — each
either fails loudly or is listed): composed binding closure under-reports
(non-primary `kinds.binding-manifest` bytes echo the selection's address —
producer fix in yi-runtime-manifest-effects.ts is an owner call, it changes
commit bytes); epoch-based authority revocation is invisible from the
revoked Yi's coordinates until a per-certificate effect commits; a
partial-split credited holding has no manifest-shaped effect so its at-read
is null before its first own commit; container `children` never fold; at-read
rows are not address-pathified (`pathifyAny` recommended in
views/service/yi-read.ts, unowned by the fix wave). Dead find for the owner:
`package-publish-support.ts:254` reads `identity.key-rotation.applied`,
which nothing writes.

Related: [[plan49-completion-review-2026-08-29]],
[[pg-collate-c-index-matching]], [[architecture-c-complete]].
