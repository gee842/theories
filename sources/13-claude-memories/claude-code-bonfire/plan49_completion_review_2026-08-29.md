---
name: plan49-completion-review-2026-08-29
description: "Review verdict on the Plan 49 completion claim: structure/gates green, but the public event-time Yi read (yi.read with `at`) was broken at the certified HEAD and is only half-fixed in the working tree"
metadata:
  node_type: memory
  type: project
---

Reviewed on 2026-08-29: commit `644460d56` ("complete normalized Plan 49
closure") plus an uncommitted ~380-line working tree that flips
`HANDOFF.md`, `README.md`, `current-truth-and-verdict.md`, and phases 6/7/8
from "recertification pending" to "complete / certified".

## What holds up

Every structural claim I could measure is true: `check:core-structure`
reports 934 Core production modules, fifteen contexts, eight shells;
protocol is `162` (`packages/sdk/src/client/rpc-schema/system.ts`); Core and
SDK are `0.2.0`; retired route markers survive only as the compiler's
`RETIRED_ROUTE_MARKERS` rejection set; there is no broad
`@bonfire/core/internal` export and no process-global handler registry;
`dispose()` is async. `typecheck`, `typecheck:tests`, and all eight fast
`check:*` gates pass — including the two the previous review left red
(`check:kernel-internal-caller-admission`, `check:kinds-compiler-foundation`).

## What does not

The public event-time read `yi.read(uid, { at })` (wire-exposed as
`at?: ObservationCursor`) folds Occasion observations through
`foldOccasionObservationsToYi`, whose `default` branch **throws** on any
unrecognised event name. See [[event-time-yi-fold-coverage-gap]] for the
mechanism and the exact uncovered events. At `644460d56` that read threw for
any Yi that had ever been patched or had a binding attached. The working tree
fixes the Kinds-root family and leaves six production event names throwing —
including `streams.active-leaf.advance`, which every `rt.messages.send`
emits on `yi:<uid>`, so the read is broken for any session that has ever
carried a message, before and after the change. A green `check:release` did
not catch a broken public read because nothing exercises `read(uid, {at})`
end-to-end except the two tests the uncommitted diff itself adds.

Two smaller things: `docs/architecture/sdk-one-model-direction.md` (untracked,
same tree) still calls Plan 49 "provisional" and links the handoff as
"still-provisional" — it contradicts the completion docs beside it;
`scripts/domain-census.known.txt` is a tracked evidence file with no
surviving reader, which the CLAUDE.md gate law says to delete.


## Fix status (later the same day)

A three-wave agent effort in this session repaired the read (uncommitted;
owner commits): fold cases decided per event against live commit bytes,
committed-state (`canonicalAfterState`) folding with fail-closed decoding,
the client filter widened to exact context coordinates, the PG
`commitTargetRef` selection made index-driven (43 ms → 1.0 ms), and e2e
at-cursor tests added. Full unit suite green; integration 372 tests green
(3 WS timing tests flaked only under my concurrent-suite load and passed
serially — the documented starvation mode).

Two of this review's claims were corrected by the fix waves: the old
`targetRef` query was NOT narrow (C-collation kept it off the index too —
see [[pg-collate-c-index-matching]]), and custody transfer DOES co-commit a
root advance (my "selection gap" claim was wrong; the defect was filter+fold
only).

**How to apply:** treat "Plan 49 complete" as true for structure and
ownership, not yet for the event-time read surface. Do not re-run the
completion certification as proof until `read(uid, {at})` has real coverage.
Related: [[verification-regime-2026-08-14]], [[pin-ossification-audit]],
[[structural-arc-design-2026-07-12]], [[feedback-owner-manages-commits]].
