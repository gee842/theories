# Yi — The Ideal Architecture

> The end-state Yi: elegant, performant, robust. Derived from a grounded
> 10-agent exploration (6 per-tension deep-dives → 3 adversarial lenses →
> coherence synthesis), every claim checked against the real code. This doc is
> the **decision record** + the **build path**. It sits above the phase plan:
> 00–03 say what Yi *is*; 04 + the phases say how it was *built*; this says
> where the architecture *converges*.

## 0. The governing principle

**Unify the DECLARATION; split the EXECUTION by its real axis.**

The north-star hypothesis — *a Yi is made-of / contains / reacts-to other Yis
via one **tie**; MRO, lifecycle, materialization, and authority are **derived**
over that tie-DAG* — is **CONFIRMED at the level of the relation and the mental
frame, and REFUTED at the level of "collapse the mechanisms."** One relation
feeds many dispatch surfaces through **different reducers**, and those reducers
are load-bearing-distinct by a *real* axis: **timing, residency, failure-mode,
ctx-shape, cache-lifetime**. Every grounded attempt to fuse the reducers (fold
`kinds[]` into the MRO, lifecycle/claims into reactions, build a payload SPI,
fold `can_mint`/license into the gate ADT) is a behaviour change or a
hot-path / security regression.

This is the RR6 lesson promoted to a first principle: **elegance lives on the
declaration surface (one frame, one authoring vocabulary, one predicate, one
router, one engine SPI); the execution surface stays split where the split is
real.** A rigorous "this split is load-bearing, keep it" is as valuable as a
unification.

## 1. The model — one row, one relation (three faces), four derivations

A Yi is a row in the `yi` table: an unordered `kinds[]` marker set + `dimensions`.
The single structural relation is the **tie**; composition (made-of),
membership (in-container), and reaction (reacts-to) are its three faces.
Four derivations fall out, each *one relation read by a purpose-built reducer*:

1. **Composition → { `kinds[]` set, C3 MRO order }.** Two honest projections of
   one compose-DAG. `kinds[]` is the unordered made-of set (static mint-time
   closure, O(1), last-match-wins) answering is-a / has-feature / what-face /
   port-exists; the C3 MRO is the ordered resolution sequence (recomputed,
   LRU-cached, C3-throws-on-conflict) answering in-what-order-do-wrappers-nest,
   and it folds the **dynamic runtime grant-wrap** a static set cannot represent.
   *Two reducers, one relation* — framed as two derived views, never merged.

2. **Reaction → `sys/reaction` { on, invoke, lane }.** Reactivity is a
   first-class Yi: `{ on: eventKind, invoke: portRef, lane: 'inline'|'deferred'|'sync', priority? }`.
   The three event-matched authoring vocabularies (composed-type hooks map,
   per-holding `triggers[]`, implicit `on_message`) are the **same primitive**
   (they already share `gatherHandlers` verbatim, differing only by event-name
   and timing) — they become one normalized reaction list. The **lane** is the
   honest acknowledgement that timing is a real axis: `inline` = in-tx
   pre-commit veto/transform (throw rolls back row + event together),
   `deferred` = post-commit microtask with a fresh per-hop budget, `sync` =
   post-commit shared-frame cascade.

3. **Membership → one `isMemberOf` predicate.** One predicate consulted by the
   kit verb, the kernel floor, and the gate leaf (so they cannot diverge — a
   historical security-bug class). The **seam compiler** picks the
   *representation* per declared intent: `marker` (reads-hot, GIN-readable
   self-borne kind) vs `edge` (writes-churny, single-writer child with
   `referent === space` floor). A **container** is any Yi bearing `membered`
   (roster) and optionally `streamed` (payload).

4. **Authority → three firing-time layers.** Mint authority is not one surface
   but three layers separated by *when* they fire: caller-side **gate ADT**
   (the one rich decision surface) / deploy-time **license** (cross-cutting
   capability+holding lookup) / in-tx **`can_mint`** (storage-state floor that
   re-fires on the 23505 unique-edge race to hand the TOCTOU loser the exact
   domain deny). The ugliness is the *router* (a derived OR), not the layers —
   reify it into a **declared per-kind authority discriminator**.

**One materialization engine, many specs.** `ProjectionEngine` and the formerly
unwired `GateCacheEngine` are byte-siblings of one mechanism. They collapse into
one engine hosting a discriminated `ProjectionSpec` family
`{ roster | gate-decision | hot-trait }` — a projection *is* "materialize a
derivation over the tie-DAG." The engine unifies; `project()`/`affected()` stay
spec-specific; a decision/trait cell is always an **accelerator in front of the
live truth** (miss / stale ⇒ fail-safe fallthrough), never a replacement.

## 2. The keep-as-is discipline (load-bearing — proven, not assumed)

Each of these is a genuinely distinct concept; fusing it is a regression:

- `kinds[]` (static O(1) set, silent-override) **≠** C3 MRO (runtime LRU
  sequence, throws-on-conflict, folds the dynamic grant-wrap). Feature markers
  (`sys/sealed`, `sys/issuing`, `sys/signing-*`) belong **only** in `kinds[]`,
  never the MRO (they would corrupt `onInvoke` nesting — RR6 proved this).
- Item/spirit **lifecycle** (around-advice with prev/to ctx + `ctx.next`,
  single-parent) and **claims** (population-threshold scan, class-owner
  authority, scheduler-leader temporal) stay **out** of `sys/reaction`.
- The **three authority layers** stay separate by firing-time; `can_mint`'s
  in-tx 23505 re-fire is structurally impossible for a caller-side gate.
- `marker` **≠** `edge` membership *representations* (the seam picking is the
  unification; merging the representations reintroduces the GIN-cliff or
  lost-update). `membered` **≠** `streamed` traits.
- The **stream tier** is a named non-Yi dense table
  (`UNIQUE(session, seq)` + `parents[]` DAG + per-session advisory lock +
  same-tx signed dual-write) — message-scale invariants no tie expresses.
- The **residency split** inside the materialization engine (canonical same-tx
  cell for sanctions/permissions vs per-process accelerator for fan-out).
- Live `evaluate()` stays the gate **truth**; the `isGateCacheable` fence
  (time-window / caller-rate / within-n-hops / predicate stay LIVE) is
  **security**, not a knob (a cached rate-limit or expired mute is an exploit).
- The **inline pre-commit veto** lane ≠ the post-commit fan-out pump.
- Schema's three concerns: `payloadShape` (inner `payload`, left open by the
  seed) / `rowSchema` (whole bucket) / `PATCH_PROTECTED_KEYS` (a gate-bypass
  deny-list, **fail-closed** — never a kit-declarable schema attr).
- The typed-view `UnifiedKindRepo` face-filter **is** the `requireItem`
  correctness guard (collapsing to `where(kind)` relocates the guard, doesn't
  remove it). The two re-entrancy guards (item `inFlight` Set vs trigger ALS
  budget) guard different recursion topologies.

## 3. The build path

**Constraint (founder, standing): NOT deployed — no backward compatibility of
any kind. No alias layers, no deprecation cycles, no compat shims. Break
forward, always the long-term-elegant option.** Because of this, the staged
"compile-target then delete the old surface" two-step collapses: `sys/reaction`
becomes the *sole* authoring surface in one cut, old fields deleted, first-party
kits re-authored in the same change.

Each slice lands green independently with an adversarial differential verifier
(the RR6 slice discipline). Slices touching distinct subsystems run in parallel
worktrees; the reaction chain and the authority/membership mint area are
serialized where they share files.

| # | Slice | Kind | Status |
|---|-------|------|--------|
| S0 | Record this north star (this doc + 01-frame / 03-architecture framing) | docs | ✅ landed |
| S1 | Merge the Russian-doll middleware composers → one `composeMiddlewareChain` (`dispatch-compose.ts`) | pure DRY | ✅ landed |
| S2 | Reify `perFaceMintOwnsAuthority` → declared per-kind `authorityModel` discriminator | equivalence | ✅ landed |
| S3 | Collapse `GateCacheEngine` into a `ProjectionEngine` `ProjectionSpec` variant (SPI converge, no gate wiring) | equivalence | ✅ landed |
| S10 | One schema validator core + `fillMode`; add 3 missing invariant tests | refactor | ✅ landed |
| **S4+S5+S7** | `sys/reaction` + lane as the **sole** authoring surface (`hooks`/`triggers[]`/`on_message` desugar in; old fields deleted) | bifurcation | ✅ landed |
| **S6** | `anchorMembers` → real revocable cells; creator access via **ownership** | bifurcation (D2 changed) | ✅ landed (Option B) |
| S8 | `hot-trait` `ProjectionSpec` variant + migrate one **profiled** hot fold-read | additive | ⏸ evidence-gated |
| S9 | Gate-decision cache wired in front of `evaluate()` for `isGateCacheable` hot gates only | gated perf | ⏸ evidence-gated |

> **S6 was a D2 decision, not a refactor — the founder chose Option B (founders
> revocable).** Grounding (~40 call-sites) showed `anchorMembers` was the D2
> *immutable founding roster*, and that dissolving it changes D2 (founders become
> removable). The founder elected the elegant long-term model: **membership is
> uniform revocable cells; a creator's guaranteed control flows from OWNERSHIP,
> not from an unremovable array.** As built: every member (founder or joiner) is
> a real participant cell minted via the same `isMemberOf` edge path;
> `anchorMembers` + `isLiveAnchorMember` + `ANCHOR_ONLY_RELATION` +
> `getAnchorMembers` + the `chat.leave` immutability throw are **deleted**;
> `isMemberOf` collapses to one cell source. The owner is never locked out — the
> session/message write gate and members-only visibility now carry an
> **owner-ancestor arm** (`or(member, target, ancestor-of-target)`), and
> `createAnchoredSession` defaults `owner = caller`, so a founder removed from the
> roster keeps access *iff* they own the space. A non-owner co-founder removed
> from the roster correctly loses access (revocation now works). `isSessionMember`
> stays pure membership; ownership lives only in the gate/visibility layers. This
> separates **who-is-in** (ties) from **who-controls** (ownership/gates) — the
> elegant end-state. (Regressions D2 a–d pin all four properties.)

**Hard stop after each slice.** Never fold feature markers into the MRO,
lifecycle/claims into reactions, payload behind an SPI, or `can_mint`/license
into the gate ADT without a differential probe (RR6 / edge-bond-fold NO-GO).

S8 and S9 stay **evidence-gated**: the SPI convergence (S3) makes them clean
variants, but a `hot-trait` cell without a profiled consumer, or wiring a cache
into the security floor without a demonstrated bottleneck, is premature — the
elegant long-term position is to converge the SPI now and instantiate the
hot-path cells when a real read/bottleneck demands them.

## 4. Performance & robustness in one line each

**Performance:** project/cache a derivation only when it is cross-row + hot +
has a clean tie-key columnar shape; fold/read-live when single-row or cold;
cache per-request for within-invoke amortization. The unifications are on the
free surfaces; execution is touched only where profiling proves the win.
Scaling is more projection instances + Redis fan-out over the per-process
tailer — never a different truth (projections rebuild from canonical rows,
Law 8).

**Robustness:** one truth (the canonical row); events are best-effort prunable
audit, co-written same-tx so the audit cannot disagree; every projection
rebuildable (Law 8). Every guarantee is *re-expressed*, never erased — the
reaction lanes carry the in-tx veto / fresh-budget / shared-frame semantics; the
membership dissolution *closes* a founder-revocation hole; the authority layers
keep their scar-tissue boundaries; cache cells are accelerators in front of a
live floor that fails safe.
