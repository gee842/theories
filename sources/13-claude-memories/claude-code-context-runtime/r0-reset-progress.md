---
name: r0-reset-progress
description: "R0, R1 and R2 are all complete — the resets, the gate retirement, and the inverted engine; what replaced them and the traps found on the way."
metadata:
  type: project
---

**R0** — ADR-030's pre-launch reset — completed on `main` 2026-08-22. Tag `pre-r0-baseline`
is the tree before it; `2e2997c` is its last commit.

**R1** — ADR-031, `specs/adr/031-composition-is-the-guard.md`, accepted and executed the same
day (`04af814`, `6021bc7`, `9ca3753`). Ren's directive: *"the old guard guards the old
architecture … these gates … maybe useful locally but negative globally"*, then *"prefer
cleaner removal and faster dev speed."* Net across both: ~143k lines deleted.

**The argument, in one line:** nine checked artifacts shared the premise *the code that runs
is the code in this tree*, and Cordis falsifies it (`ctx.plugin()` on every mounted plugin,
no seal, `disabled: !!js` re-evaluated per mount). They do not become annoying, they become
**false**. ADR-030 d.1 had already reached this for the mediation matrix; R1 applied it
uniformly.

**Retired:** `package-boundaries` (+ 3,798-edge snapshot, constructor inventory),
`freeze-registry` (+ 11-contract census), `dependency-inventory`, `integration-profiles`/
`integration-coverage` (+ 14 profiles), `production-boundary-inventory`, the product's
`mediation.ts`, `schema-inventory` (+ `schema-ownership.json`), the coverage generator, and
three adapters' collectors. **Arrived:** `bench/architecture.test.ts` — three live
module-closure invariants inside `pnpm test`, 168 ms — over
`bench/scripts/history-core/lib/closure.ts`.

**Two rules now govern.** *Freeze becomes publication*: a contract is frozen iff a published
package exports it — nothing is published, so **nothing is frozen**. *No version number
before a second live version* — the 143 existing `/1` tags stay as inert names, because a
mechanical version sweep is what inverted two guard polarities in R0.

**The finding worth keeping:** `schema-ownership.json` fed the two writer-exclusivity suites
(a real correctness rule) while attributing relations to `001_init.cjs`,
`032_history_perimeter.cjs` and 34 other migrations that R0 had deleted. The suites passed
anyway. **A stale corpus does not fail; it keeps answering.** They now walk the SQL live
(`packages/store/test/relation-writers.ts`) and catch *undeclared* writers, which the corpus
could not express.

**Traps.** Delete by *reference*, never by folder — `api-surface.ts` and `replay-evidence.ts`
sat inside the retired coverage module and are used by adapter manifests and the two-driver
kits. A sweep that rewrites `vN ? a : b` guards silently inverts them. When unsure whether a
branch is reachable, make it throw and run the whole suite.

**R2 (`672dae0`) — the inverted engine is retired**, no trace left. It had no production
wiring anywhere in its chain: `createTransitionEngine` was called only from tests, its
`MemoryTransitionPort` had no implementor, and `LangGraphStore` is never constructed in
production either. Careful: `packages/runtime/src/engine.ts` is a **different file** and is
load-bearing — `PlannedEffect` (24 production refs), `ExecutionBinding` (21), `RuntimeError`.
Two engines have now been retired out from under that vocabulary. `legacy-engine`/
`legacy-kernel` **stay**: they classify peer frameworks in the integration contract, not us.

Gate now: **168 files, 1,615 tests**. See [[freeze-liftable-pre-launch]] and
[[adr-030-assurance-model]].
