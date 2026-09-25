# Frame/Pivot Claim Audit - 2026-06-19

> **Historical review artifact.** Names in quoted findings describe the
> June 19 working tree and are evidence, not current API guidance.

> Where this page and source-anchored docs disagree, `llms.txt` and the cited source files win.

Scope: current uncommitted `docs/concepts/the-frame.md` and `docs/design/the-pivot.md`, verified against the working tree.

This audit is intentionally narrow: it separates current facts from destination claims and flags claims likely to mislead implementation agents.

## Summary

Most important corrections:

1. `rt.yi.where` is not raw/ungated. Current type docs and implementation apply visibility filtering. `countWhere` is the read surface with explicit aggregate/no-row-gate caveats.
2. "One table" is already current physical storage for Postgres and memory. The remaining split is face-shaped write/index/API/lifecycle behavior.
3. The face guard is real and is currently the clearest code-level expression of the subject/object split.
4. The relation compiler/planner is destination-only. Existing indexed storage surfaces are manual and concrete.
5. "Every representation has a tested rebuild path" is too broad under retention and current test coverage.
6. Collective capability is destination-only.

## Claim Table

| Claim area | Status | Evidence | Implementation consequence |
|---|---:|---|---|
| Canonical Yi row shape | Verified | `packages/server/migrations/001_init.sql:40` describes `yi` as the unified substrate row table; `001_init.sql:48` creates `yi` with `uid`, `schema`, `kinds`, `origin_kind`, `path`, `parent_uid`, timestamps, `seq`, `head_event_uid`, and `dimensions`. | Safe to teach `Yi` as canonical row truth. |
| Postgres one table | Verified | `packages/server/migrations/001_init.sql:48` creates one `yi` table for spirits, holdings, sessions, kinds, etc. | Do not frame Phase 0 as creating the first physical `yi` table. |
| In-memory one map | Verified | `packages/core/src/storage/memory.ts:80` says every Spirit and Holding row lives in one map; `memory.ts:156` says there is no face partitioning at storage layer. | Same correction: the hard problem is not physical unification. |
| Storage APIs still face-shaped | Verified | `packages/core/src/storage/types.ts:827` exposes `spirits`, `items`, `relationships`, `messages`, `unifiedHoldings`, and `yi`; `packages/server/src/pg-storage.ts:996` says reads are unified but writes flow through per-face repos. | Reframe "two repos" as "face-shaped SPI/API and writer/index contracts." |
| Face guard | Verified | `packages/core/src/runtime-yi/kind-ops.ts:260` refuses adding `core:spirit`, `core:holding`, `sys/session`, or `core:kind` after manifest because face kinds decide storage face. | This is the actual code obstacle to agency-as-trait and item-carries-agent. |
| `face_class` stored column | False if read as DB fact | `packages/server/migrations/001_init.sql:48` has no `face_class` column. | Avoid saying "stored face_class" unless referring to type/API metadata. |
| `face` and `face_class` are gone | False | `packages/core/src/runtime-yi/types.ts:19` still has manifest `face`; `runtime-yi/types.ts:438` still has port `face_class`; `kind-ops.ts:260` still treats face kinds specially. | "No face" is destination-only. |
| Messages are special storage | Verified | `packages/server/migrations/001_init.sql:188` creates `yi_message`; `001_init.sql:190` says messages are not Yi rows and use purpose-built storage. | The frame should teach messages as the deliberate scale exception, not an embarrassment. |
| `rt.yi.where` raw / ungated | False | `packages/core/src/runtime-yi/types.ts:660` says results are filtered by caller visibility; `runtime-yi/create.ts:323`, `339`, `360`, `373`, `396`, `419`, and `423` apply read visibility helpers across branches. | Remove or rewrite the warning in both docs. The raw backdoor is `storage.*`, not `rt.yi.where`. |
| `rt.yi.countWhere` visibility | Verified caveat | `packages/core/src/runtime-yi/types.ts:682` says `countWhere` does not apply per-row visibility gates and is a system/container-owner aggregate. | If the docs need a footgun, point at `countWhere` aggregate semantics and direct storage reads, not `where`. |
| `caller-holds` full holding fallback scan | Verified | `packages/core/src/gates/gate.ts:1054` reads by holder/class; `gate.ts:1059` then iterates `storage.yi.byFace('holding')`. | Hot authorization path needs index/materialization work before compiler claims scale. |
| `caller-holds` cascade liveness gap | Verified | `packages/core/src/gates/gate.ts:631` `matchesCallerHolding` checks unburned/class/holder/issuer/active; it does not call `isHoldingLive`. | A burned upstream binding or cascade-dead holding can be mishandled unless another path gates it. |
| Trigger budget resets on message deferral | Partly true, intentional | `packages/core/src/runtime.ts:1055` snapshots cycle/depth; `runtime.ts:1062` says each deferred cascade gets its own budget allowance; `triggers.ts:247` installs a seeded fresh frame with `remaining: config.budget`. | Frame it as a deliberate isolation tradeoff, not simply a missing bound. Still needs load/fanout analysis. |
| Present dimensions cache invalidation | Mostly fixed for deploy paths checked | `packages/core/src/substrate/spirit.ts:1623` invalidates `PresentDimensionsCache` on spirit-kind deploy; `packages/core/src/holdings/holding-class.ts:853` invalidates for holding class deploy. | Do not keep stale "never invalidates on deployKind" claims without checking exact path. |
| Class read flags cache invalidation | Suspicious | `packages/core/src/runtime-yi/read.ts:99` comments that class read flags piggy-back on `PresentDimensionsCache.invalidate`, but grep found no direct invalidation of `classReadFlagsCache` outside its definition. | Needs a focused test/code pass before claiming fixed or broken. |
| Relation compiler/planner | Destination-only | No current relation declaration compiler was found. Existing storage exposes concrete repos and indexes. Gate SQL compiler files exist, but are not the general relation compiler described in the frame. | Do not let agents implement a broad compiler before a membership-only proof. |
| Gate SQL compiler | Partly implemented, production-unwired | `packages/core/src/gates/gate-sql-compiler.ts` and `gate-sql-partial.ts` exist; pivot itself says production is unwired. | Treat as a separate optimization path, not proof that relation planning exists. |
| Collective capability / `caller-via-group` | Destination-only | The docs describe it, but no current gate leaf matching `caller-via-group` was found in `packages/core/src/gates/gate.ts`. | Do not schedule product promises on this until policy/explain/revocation semantics are designed. |
| Membership unified today | Partly true | `packages/core/src/auth.ts:371` defines a unified session membership predicate over `anchorMembers` or live active relationship edge. Community membership still has separate product shapes and marker kinds. | Membership is the right first compiler proof, not already solved globally. |
| Rebuildability | Partly true | Representative rebuild tests exist, but `packages/core/src/runtime-yi/types.ts:695` says history is best-effort truncated when retention is enabled. | Rebuild generated projections from canonical rows where possible; do not assume complete event history. |
| Direct storage backdoors | Verified | Subagents found std/examples direct `rt.storage.*` usage. This is consistent with the frame's leak warning. | If `rt.yi` is the desired authoring surface, std/examples need a backdoor audit. |

## Claims That Should Be Reworded Before Implementation

### "Two repos today"

Safer wording:

> Current physical storage is already one `yi` table/map, but the storage SPI, write routes, public APIs, and lifecycle guards remain face-shaped. Phase 0 is about unifying the writer/index/lifecycle contract, not merging physical tables.

### "`rt.yi.where` is raw"

Safer wording:

> `rt.yi.where` applies visibility filtering. Direct `storage.*` reads are raw. `rt.yi.countWhere` is an aggregate surface with explicit no-per-row-visibility semantics.

### "No face"

Safer wording:

> No face as a birth-time storage partition is the destination. Today face markers and face-shaped APIs still drive manifest routing, add/remove-kind guards, display/discovery metadata, SDK/RPC inputs, and storage indexes.

### "Every projection rebuilds"

Safer wording:

> Derived projections must declare a rebuild source. Prefer canonical rows for durable projections. Event-based rebuild is only valid inside the retained event horizon unless the product explicitly requires complete event retention.

### "The compiler will choose representations"

Safer wording:

> A future relation compiler may choose marker, edge, message, list, map, DAG, or CRDT representations. Current code has manual indexed surfaces. The first proof should be one membership relation family.

## High-Risk Follow-Up Checks

1. Build a public API matrix for every face-shaped SDK/RPC method.
2. Inventory every `face`, `face_class`, `Kind.face`, and `holdingSubFaceFromKinds` dependency.
3. Verify whether `classReadFlagsCache` actually invalidates on compatible redeploy.
4. Add a focused test for cascade-dead holdings under `caller-holds`.
5. Add a performance test for `caller-holds` at high holding cardinality.
6. Define a row-based rebuild test for any generated membership marker/materialization.
7. Define a retention-enabled migration fixture.
8. Audit direct `rt.storage.*` usage in std/examples and classify it as admin-only, internal-only, or replacement-needed.
9. Design permission explain output before collective capability.
10. Decide whether presence is explicitly outside durable Yi semantics.

## Final Audit Position

The docs are much improved because they now label current fact, violation, destination, and future mechanism. They are still not safe as final implementation direction until the stale claims above are fixed.

The most dangerous stale claim is `rt.yi.where` visibility. The most dangerous structural overclaim is "Phase 0 equals one table." The most important missing engineering proof is membership as one compiled relation with no unbounded hot-path scans.
