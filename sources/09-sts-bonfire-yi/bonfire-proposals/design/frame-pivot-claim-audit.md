# Claim Audit for `the-frame.md` and `the-pivot.md`

> Where this page and source-anchored docs disagree, `llms.txt` and the cited source files win.

Status: source-verified audit. This file is a companion to
`docs/design/frame-pivot-evaluation.md`.

No tests were run. Verification used targeted file reads and searches.

## Legend

- **Verified**: supported by current source.
- **Partly true**: directionally right, but incomplete, stale, or overstated.
- **Destination**: valid as desired end-state, not true today.
- **Risk**: conceptually plausible but needs proof before becoming doctrine.

## Claims

| Claim | Status | Notes / Evidence |
|---|---|---|
| `Yi` is one canonical row shape with additive `kinds[]` and `dimensions`. | Verified | `packages/core/src/yi.ts` defines one row shape and says every persisted thing is a Yi; `kinds[]` is ordered/additive and face fields live in dimension buckets. |
| A row can carry both `core:spirit` and `core:holding`. | Verified | `packages/core/src/yi.ts` explicitly names NFT-character, bot-as-membership-token, and delegation-actor as examples. |
| Ports dispatch by walking `kinds[]`, not by a spirit-only method table. | Verified | `packages/core/src/runtime-yi/port-dispatch.ts` resolves ports from row kinds. This is one of the strongest existing substrate features. |
| Meaning should live in `kinds[]`, not field presence. | Verified as direction; not current truth everywhere | Storage routing is already marker-based in important paths, but `yi-guards` and runtime type projections still infer token/item/relationship shape from fields such as `issuer` and `referent`. |
| Holding subface is currently a top-level discriminator. | Mostly stale | Current storage comments and `holdingSubFaceFromKinds` derive subface from `sys/token`, `sys/item`, `sys/relationship` markers. The remaining problem is repeated re-derivation and public/type-level field-presence semantics. |
| `holdingSubFaceFromKinds` is a measurable leak. | Verified | It appears broadly across core/server/std. The count depends on whether dist/test/comments are included, but this is a real repeated dispatch/re-derivation surface. |
| `Kind` carries old class-spec fields. | Verified | `packages/core/src/kinds/class.ts` still includes stored fields such as `face`, `policy`, `features`, `methods`, `hooks`, `partySchema`, `slots`, `issuer`, `referent`, `mutual`, `transferable`, `revocable`, etc. |
| `Kind` should shrink to exactly eight fields. | Destination, needs review | The eight-field target is coherent, but current canonical fields also include `invariants`, `evolutionPolicy`, `transientVia`, `examples`, and `frozen`. These need explicit classification before deletion. |
| The word `face` is overloaded. | Verified | `face`/`face_class` appears as manifest input, stored kind metadata, port/discovery register, event payload label, docs vocabulary, and SDK projection/wire naming. |
| `ports-and-faces.md` contradicts `yi.md`. | Partly true | `yi.md` says no row `kind` discriminator. `ports-and-faces.md` says `face_class` is only a register label, but also says the Yi row carries a `kind` partition discriminator. The stale part is narrower than the rhetoric, but real. |
| Membership is split across multiple representations. | Verified | Session membership uses `anchorMembers` plus live participant edges. Community/platform code also uses marker-style member kinds and `bears(...)` gates. |
| The gate SQL compiler is production-dead. | Verified | `gate-sql-compiler.ts` is consumed by `gate-sql-partial.ts`; excluding tests, neither is imported by runtime/storage paths. |
| The gate SQL compiler should become an invisible read prefilter. | Risk / future mechanism | Plausible, but not proven. It needs a concrete query path and performance tests before becoming part of the compiler story. |
| Messages are a special representation, not Yis. | Verified | Messages live in `yi_message`, have dense per-session `seq`, parent DAGs, and dual-write `yi.message` events. |
| `stream(...)` relation/compiler API exists. | Destination only | The docs show `stream('messages', { volume: 'high' })`, but no production relation compiler API exists today. |
| Every representation is already a rebuildable projection of one canonical Yi. | Overstated | Strong as a law. Too broad as current fact. For messages, the event dual-write helps, but future feeds/CRDT/list/map representations are not implemented or proven rebuildable. Retention can also limit history fidelity. |
| A deploy-time compiler is better than a runtime planner. | Verified as sound engineering judgment | The planner would be a query optimizer plus online migration engine. A deploy-time compiler is the right ceiling until real workloads justify more. |
| Phase 1 is router-independent. | Mostly true | Shrinking old faces, field-presence identity, and port model cleanup do not require a compiler. Membership and streams do. |
| Phase 1 is pure deletion and needs no new machinery. | Overstated | `DimensionRegistry.contributesToFace`, stored `Kind` fields, SDK wire terms, face/class manifest inputs, and subface dispatch are live surfaces. This is migration work, not simple deletion. |
| No backwards compatibility is the right project law. | Plausible, with condition | Fine because this is pre-production and compatibility scaffolding is part of the pain. But each breaking phase must be atomic across core/server/SDK/docs/tests/snapshots. |
| Tie/Moment should be the taught daily model. | Doubtful | Useful as rationale. Too broad as the model developers must hold. It risks making `kinds[]`, membership, message parentage, port invocation, and audit all one overloaded word. |
| Trait/role should be the taught model. | Verified as best fit | It is closer to the current substrate: traits map to kinds, roles map to relation positions, ports/gates map to existing runtime behavior. |
| Agency is a trait. | Verified as doctrine to keep | This avoids making every Yi an actor. However, "can hold capabilities" should probably be separate from agency. |
| `the-frame.md` uses `rt.yi.get`. | Incorrect detail | Current public runtime verb is `rt.yi.read`, not `rt.yi.get`. This should be fixed before the doc becomes acceptance criteria. |

## High-Confidence Corrections

1. Replace "Tie is the irreducible second concept" with "Tie/Relation explains
   why the unification works; daily authoring uses Yi, Trait, Role, Port, Gate."

2. Mark the compiler sections as planned substrate work until a membership
   compiler exists.

3. Replace "every representation is a pure rebuildable function" with a testable
   law: every materialization must declare its canonical source, audit event,
   and rebuild path.

4. Treat `Kind` shrink as an inventory-and-migration project, not pure deletion.

5. Split agency from capability-bearing:
   - `agent`: can initiate actions;
   - `messageable/callable`: can receive ports;
   - `capability`: can be held and used as authority evidence;
   - `container`: can contain or carry.

6. Do not touch stream generalization until membership compiler parity is proven.

## Suggested Acceptance Tests

For field-presence identity removal:

- A holding with both `issuer` and `referent` routes by declared marker, not by
  field precedence.
- Public guards and SDK projections use declared traits/markers.
- Ambiguous multi-subface rows are impossible or rejected.

For `Kind` shrink:

- Every removed field has a replacement home.
- Deployed stored kinds migrate or are regenerated.
- Public API snapshots intentionally change.
- SDK authoring examples compile.

For membership compiler:

- Marker and edge representations produce identical `join`, `leave`,
  `isMember`, and `members` behavior.
- Negative auth cases match current `isSessionMember` semantics.
- PG EXPLAIN tests prove the expected marker and referent/holder indexes are
  used.
- Kit code does not call `holdingSubFaceFromKinds`, manually mint member marker
  kinds, or reach into per-face storage repos.

For stream compiler:

- It still uses `storage.messages.append` or an equivalent contract.
- Dense per-session sequence allocation is preserved.
- `yi.message` event dual-write remains same-transaction.
- Subscriber ordering is unchanged or explicitly redesigned and tested.

## Bottom Line

The docs are strongest as a north-star diagnosis and weakest as a direct route
to implementation. The right move is not to reject them, but to downgrade some
assertions from "truth" to "target", perform a doc-truth pass, and then start
with concrete, testable subtractions.
