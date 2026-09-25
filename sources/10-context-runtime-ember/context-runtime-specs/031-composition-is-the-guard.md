# ADR-031 — Composition is the guard: retiring the closed-tree scanners

- **Status:** accepted (Ren, 2026-08-22); G1, G2 and G3 executed the same day. Scoped by Ren's
  directive: *"the old guard guards the old architecture, but we need architecture upgrade … many
  places compromised design due to gate, and we are still experimenting, so v1/v2 won't even make
  sense, and these gates won't either, they maybe useful locally but negative globally"* — and the
  execution directive that followed: *"prefer cleaner removal and faster dev speed, and significantly
  reduced constrains and allow more experiment range."* This ADR is the guard-policy half of ADR-030; ADR-030
  keeps the adoption itself. It does not touch a single correctness invariant — see **Untouched**.
- **Date:** 2026-08-22

## The finding: one premise under nine guards

Nine of this repo's checked artifacts assert different things, but every one of them rests on the same
premise:

> **The set of code that runs is the set of code in this tree, and I can enumerate it by reading the tree.**

That premise licensed a *scan* to stand in for a *runtime property*. It was true while the runtime was a
monolith we compiled whole, and the scanners were the honest way to keep §10.5's seventh step — *a path
that has not been migrated must be listed*.

Cordis falsifies the premise, and ADR-030 decision 1 already says so in detail: `ctx.plugin()` is a core
`Context` method available to every mounted plugin, there is no seal, `disabled: !!js` re-evaluates at
every mount decision, and waterfall listeners may `prepend` and short-circuit. After adoption a scan of
*our* tree says nothing about the *mounted* tree, and the mounted tree is data that changes post-boot.

So these guards do not become annoying. They become **false** — green while the property they name is
gone. ADR-030 worked the substitution for exactly one of them, calling the attestation observer *"the
mediation matrix's honest successor."* The finding here is that this is not a special case for the
mediation matrix. It is the general answer, and applying it once, uniformly, is what makes the adoption
smooth instead of a fight with our own tooling.

## Decision 1 — the substitution

> **Static scan of a closed tree → declared composition · observed composition · a recorded regime that
> downgrades on divergence.**

Three artifacts replace nine scanners:

1. **The declared tree** — the Cordis profile, dumped as data (`--dump-config`). This is what
   `dependency-inventory`, `package-boundaries`, `constructor-inventory` and `integration-profiles` were
   each approximating by reading source.
2. **The observed tree** — the attestation observer of ADR-030 decision 5, watching post-boot mounts and
   listener registration on the mediated seams.
3. **The regime record** — what a session's claim cites, downgraded the moment observed ≠ declared.

This is strictly stronger than the scanners, because it survives an open tree. The scanners cannot be
repaired to do that; the property they check stops existing.

## Decision 2 — freeze becomes publication

**A contract is frozen if and only if it is exported from a published package.** Nothing else is frozen.

The freeze registry asked "which contracts are stable enough to depend on" and answered it by
self-grading: a four-way decision enum, a rule-of-two checklist, and a census we maintain by hand. W1
makes the question real in the only place it has ever mattered — the published surface — where semver
and `exports` are enforcement we do not administer ourselves. ADR-030 decision 2 already committed to
the symmetry: *our product trusts our engine exactly the way it trusts DSH, through published, pinned,
semver-disciplined artifacts.*

`freeze-registry.json`, its 1,606-line checker, and the `freeze | frozen-legacy-read-only | experimental
| private-versioned` enum retire. This also removes the recurring defect of the R0 work, where deleting a
dead migration-era reader silently "unfroze" a family, because the rule of two had been counting a
corpse as the second consumer.

## Decision 3 — a version number is a boundary artifact, and stays where one exists

There are **143 distinct format tags in `packages/*/src`, and every one of them is `/1`.** A version
suffix is a promise that a reader may one day meet a different number. Pre-launch, with no legacy and one
active writer per semantic, no internal reader ever will. The suffix costs a decision at every new format
whose answer is always the same, cost R0 a whole-tree renumber, and advertises a compatibility discipline
we have explicitly declined.

The rule of two, applied to versions themselves: **a version number appears when a second live version
exists, and not before.** It therefore stays exactly where we do not control both sides —

- published packages (W1), where semver on the package *is* the version;
- the DSH session seam, which carries upstream's own `sessionFormatVersionRefusal`;
- canon rows, once genesis hardens at the first uncontrolled consumer.

— and it means nothing anywhere else.

**We are not re-sweeping the 143 tags.** The literal string is inert; the *rule about* the string is what
costs. Deleting the rule costs one file. Deleting the suffix costs a second 560-file sweep, and R0 proved
what that sweep does: a mechanical version-string rewrite hit two ternaries whose left operand was the
version test, inverted their polarity, typechecked cleanly, and shipped a live effect refusal that only a
behavioural test caught. Trading a real regression risk for the removal of an inert suffix is a bad trade.
The tags stay as opaque names until a boundary gives one of them a second version.

## Decision 4 — the adoption shape

```text
  Framework-free libraries        domain · store · kernel · compiler · runtime services · replay
        ▲                         (zod, no Cordis, no schemastery — ADR-030 d.1 hard line)
        │ constructed by
  Bridge plugins                  history · authority · admission · effect · publication
        ▲                         one per existing port in packages/runtime/src/ports
        │ composed by
  Profiles (data)                 dev · test · production — the mounted set, dumpable
```

The five ports already in `packages/runtime/src/ports` are the five service keys. Three rules keep the
shape honest:

1. **A bridge plugin has no logic.** It constructs a library object and registers it under a service key.
   If a bridge grows a branch, the branch belongs in the library.
2. **One service key is one active writer.** Cordis enforces this natively; it replaces our hand-rolled
   statement of the same rule for *services*. Which component is the writer of record for a *canonical
   fact* remains ADR-030 decision 4's separate and stricter statement.
3. **Framework types appear only in bridges.** `Context`, `Service` and schemastery config vocabulary stop
   at the bridge layer.

What makes adoption *smooth* is rule 1 plus rule 3: because the libraries stay framework-free, every
conformance kit, crash drill and replay assertion keeps constructing libraries directly and does not
change at all. No test is rewritten to adopt a framework. Verified today — no file under any
`packages/*/src` imports `@deepseek-ai/*`.

## Disposition

| Guard | Lines | Disposition | Why |
|---|---|---|---|
| PG triggers, OCC, fencing, effect bracket, erasure, replay, RLS, tenancy | — | **keep** | ADR-030: *no plugin tree repeals a trigger* |
| Two-driver conformance kits · `kill -9` drills · `liveThenReplay` · adversarial titles | — | **keep** | CLAUDE.md already names these as the verification |
| `vector-coherence` | 916 | **keep** | proves the corpus does not contradict itself; still true, still cheap |
| `schema-inventory` + `schema-ownership.json` | 606 | **replace** | a census in exactly the retired vocabulary — families, versions, classifications, owners; its one surviving claim (`packages/domain` stays zod-only) is now a live invariant |
| `package-boundaries` + `package-boundaries.json` (3,798 edges) + `constructor-inventory.json` | 2,533 | **replace** | rules are named `phase9-*`; carries a self-test CLAUDE.md forbids; `tsc -b` and `exports` enforce layering already |
| `freeze-registry` + registry JSON | 1,606 | **replace** (decision 2) | self-graded; publication is real enforcement |
| `integration-profiles` + `integration-coverage` + 15-file profile corpus | 1,990 | **replace** (decision 1) | profiles encode phase-era classifications; the declared profile supersedes them |
| `dependency-inventory` | 1,303 | **replace** (decision 1) | composition is data now |
| `production-boundary-inventory` + `packages/product/src/mediation.ts` | 1,051 | **replace** (decision 1) | a closed-tree scan is false under an open tree |
| frozen-migration byte pin · `trustedManifestSha256` | — | **disarmed while genesis is soft** | already soft; re-pinning on every genesis edit is pure friction |
| `/1` on 143 internal tags | — | **left inert; the rule deleted** (decision 3) | re-sweeping risks the R0 polarity bug for no gain |

Net: roughly **8,500 lines of scanner and three JSON corpora retire**; two small rules and one observer
arrive. `atomicWrite`, `canonicalJson`, `checkFile` and `ROOT` move out of `package-boundaries.ts` into a
shared helper first — `w0-probe.ts`, the DSH probe we are keeping, imports them, which is itself a small
instance of the gate standing in the adoption's way.

## Untouched

Nothing here weakens a correctness semantic, and none was ever in conflict: canonical bytes (CR-CJSON/1),
OCC read-trace witnesses, per-lease fencing, the effect intent/observation bracket, erasure, replay
determinism, tenancy and RLS, append-only canon, one-open-turn-per-ref, `refs_guard`,
`effect_observation_requires_intent`, the role split. The enforcement that matters was never in the
composition layer, which is precisely why moving composition to a framework costs us nothing.

## Sequencing

- **G1 — extract the shared helpers**, then delete what is already false or inert: the phase-scoped
  boundary engine, the freeze registry, the dependency inventory, the integration profile corpus.
  No window opens: each asserts a property that either holds structurally or is proven by a suite.
- **G2 — land the two replacements**: framework-freeness as a narrow check, and the published surface as
  the frozen surface via `exports` + semver.
- **G3 — the mediation matrix.** Its checked artifact and scanner go with G1, because every bridge plugin
  would otherwise owe it a row; the claim it carried survives as prose here until the attestation observer
  lands in W2/W3. This is the one place a stale claim leaves before its successor arrives, and it is
  recorded rather than glossed: the matrix's own rows were already wrong — they classified the inverted
  engine's two entry points as awaiting adopter reducers that had since landed. That engine was itself
  retired on 2026-08-22 (addendum below), so the rows now describe nothing at all.

## What execution turned up

Two things the disposition table did not anticipate, both recorded because they sharpen the argument
rather than soften it:

- **A retired corpus was feeding live correctness tests.** `schema-ownership.json` was read by the two
  writer-exclusivity suites — one active writer per semantic, which is not a representational rule.
  Deleting it broke them, which is how it came to light that the corpus had attributed every relation to
  migrations R0 deleted (`001_init.cjs`, `032_history_perimeter.cjs`, thirty-four more), and the suites
  had been passing against names for nothing since. They now walk the SQL live and assert something the
  corpus could not: not merely that declared writers are right, but that **no undeclared writer exists**.
  A stale corpus does not fail; it keeps answering.
- **Not everything in a retired module was retired.** `api-surface.ts` and `replay-evidence.ts` sat
  inside the coverage module and are used by the adapter manifests and the two-driver conformance kits.
  Deleting by folder would have taken them; the reference sweep found them first. Same for three ADK
  conformance helpers inside a dead collector.

The general lesson for the remaining W-packages: **delete by reference, never by folder**, and expect at
least one live consumer inside anything this old.

## Addendum — the inverted engine (2026-08-22)

Ren directed the retirement after the disposition above landed. `packages/runtime/src/transition-engine.ts`
and its four test files are gone: 492 lines of engine, 1,173 of test. The decisive facts —

- **No production wiring anywhere in the chain.** `createTransitionEngine` was called only in tests; its
  `MemoryTransitionPort` had no implementor; and `LangGraphStore`, the would-be consumer of that port, is
  never constructed in production either.
- **A clean cut.** `packages/runtime/src/engine.ts` survives whole and is load-bearing — `PlannedEffect`
  (24 production references), `ExecutionBinding` (21), `TransitionRequest` (9), `TransitionResult` (6),
  plus `RuntimeError` and its class. Two engines have now been retired out from under that vocabulary;
  the vocabulary was never the engine.
- **The coverage was duplicated at the layer that owns it.** Eight of the kit's twelve behaviours map onto
  History-conformance titles running against the *same two adapters*, including the two that looked
  unique: prefix-read invalidation (`history-conformance/index.ts:727`) and disjoint-write admission
  (`:742`), plus lost-acknowledgement recovery, adjunct durability, the deterministic race branch and
  stale publication.

What is genuinely gone: the non-committing `observe()` path and the moved-compilation-read refusal. Those
tested an engine-level API, so they retire with their subject rather than leaving a hole — but if an
adopter reducer later wants a dry run, it will be designed against the perimeter, not recovered from here.

Resolved with it: the `transition-engine` direct-path counter surface, six `purpose-port` denylists, three
runtime import denylists, the product's allowed-constructions regex, 27 prose references, and 212 lines of
commented-out Phase-9 fixture in `continuation-resolver.test.ts`. The `legacy-engine`/`legacy-kernel` enum
members **stay** — they classify peer frameworks in the integration contract, not our code.

Two corpora that G1 should have taken went with it, found by this sweep: `dependency-ledger.json` (594 KB)
and `production-boundaries.json` (60 KB), both orphaned when their generators were deleted and read by
nothing. `specs/history-core/` now holds four files.

## Addendum — where the artifacts came from (2026-08-22)

Retiring the scanners raised the question of why there were nine. The answer is uncomfortable and is
recorded because the fix depends on it: **the execution plan asked for them.**

§2 of `history-core-execution-plan.md` is a program-control system that requires, per phase, a
candidate-bound JSON artifact, an acceptance document, a `--check` command, and — §2.3 step 3 — an
*acceptance self-test*, meaning the harness verifying itself. §0.1 made "candidate-bound result
artifact published atomically" part of the definition of completion. Nine phases against that template
produce nine artifacts. The 441-line mediation matrix satisfies §10.5's *coverage matrix 诚实列出其余
路径* exactly as written. **That is compliance, not defection**, which is why the correction had to
land in the plan and not only in the code. §0.0 now retracts the machinery; §5–§14 stay as history.

Two observations worth keeping:

- **Volume was never the signal.** Test-and-bench is 0.67× production lines after R1, and was ~0.77×
  before. The two-driver conformance kits are large and are the real verification. The retired
  boundary snapshot was comparatively small and worthless. Any budget expressed in lines would have
  cut the wrong half.
- **The discriminator is the oracle.** Every surviving gate has a source of truth outside the tree
  under test — a second implementation, the tape, the OS, Postgres, a hand-derived vector. Every
  retired one graded itself: regenerate, then compare against what was just regenerated. The
  mechanical test is *can this go red without a human first editing the expectation?*

A soft rule had already been tried. CLAUDE.md carried *"Keep gates narrow"* from 2026-08-14, after
Phase 0 overbuilt its harness, and the harness kept growing for a week. That is the evidence for
making the admission rules normative in the plan rather than advisory in the instructions.

## Consequences

The engine keeps the guards that catch real defects — the suites — and stops maintaining a second,
hand-written implementation of properties `tsc -b`, `exports`, and Postgres already enforce. Adoption
stops fighting the tooling: a new bridge plugin is a new file, not a new row in four corpora. The claim we
make about mediation gets weaker on paper and stronger in fact, because a recorded regime that downgrades
on divergence beats a source scan that cannot see a dynamic mount.

The cost is real and worth naming: we lose the ability to answer *"what is the whole import graph, as of
this commit?"* from a checked artifact. That question stops being answerable under an open tree anyway,
which is the argument, but the loss is a loss.

## OPEN

- Whether the attestation observer records at mount granularity or seam granularity — W2/W3's call.

**Resolved on execution.** *"Whether `schema-inventory` keeps anything beyond the zod-only claim"* — it
does not. The inventory is a census in precisely the vocabulary decision 3 retires (family, versions,
classification, semantic owner), nothing in the suites calls it, and the zod-only claim now runs live in
`bench/architecture.test.ts`. It retires with `schema-ownership.json`, which had no other reader. ADR-030
decision D1's requirement that new families enter *"with schema-ownership rows"* is superseded: a new
family enters by being written, and is frozen only if a published package exports it.
