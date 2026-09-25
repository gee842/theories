# Yi — The Unification Plan (the legacy-elimination era)

> **Status: canonical execution plan for the next era.** Born from the 2026-06-22 full multi-agent
> review (6 adversarial agents: fidelity+framing, fracture-hunt, SDK-shape, KindPolicy, storage,
> face-dissolution). The committed **direction does not change** — [`00-direction.md`](../00-direction.md)
> goals G1–G7, [`01-frame.md`](../01-frame.md) Laws + model, [`02-pivot.md`](02-pivot.md) decisions
> D1–D16 still stand. This plan exists to eliminate the **legacy shells** that survive around the now-
> unified spine, and to make the frame true at the level of *the vocabulary a developer holds*, not just
> the bytes on disk. It supersedes and absorbs the `04-execution-plan.md §9` residual register (RR1–RR7),
> re-scoped under one lens.
>
> Every track cites the concrete `file:line` it touches and the acceptance gate that proves it. Same
> green-bar as `04 §7` (typecheck 0 · typecheck:tests 0 · in-memory suite · PG integration · snapshot ·
> frame audit no-regress). Same discipline: **code rises to the docs ideal, never the reverse** (the ideal
> docs 00/01/02 stay pristine; revisions to them are *proposed* in §2 for founder ratification, not applied
> unilaterally). **No backwards-compat: break forward, atomically.**

---

> ## UNIFICATION — SPINE LANDED; NAMED RESIDUE OPEN (corrected 2026-06-23 after the grand review)
>
> **An earlier banner here read "UNIFICATION COMPLETE — all phases landed." That overstated.** An 8-lens
> adversarial review (synthesis score 66/100) found the representation spine is real and load-bearing, but
> (a) a CRITICAL read-authz regression had shipped, and (b) several phases the banner implied were done were
> not. This banner is the corrected, honest status.
>
> **Landed + verified (representation spine):** **U0** (dead fields: invokeAuth, KindPolicy 8→5, rt.events) ·
> **U1.1** (dead item-method surface) · **U1.4** (`*Shape` cluster) · **U1.3** (DEFER+documented — two
> genuinely-distinct lifecycle engines) · **U2.1–U2.3** (publicGrant→gate leaf, dead contracts deleted, G5
> `explain` wired) · **U3** (the row-shape face dissolution — `sys/session`→`membered`+`streamed`,
> `sys/spirit`→`identity`+`profile` in storage) · **U4.1/U4.2** (the 7 ROW-READ wire verbs + client read
> surface folded into `yi.*`, protocol 9) · **U5** (G8 cognitive-budget gate) · **U6** (22 examples migrated).
> **`cls*` 57→40**; `holdingSubFaceFromKinds`/`invokeItemMethod`/`sys/session` = 0 in source.
>
> **SECURITY — found by the review, FIXED (`9ee74e69`, `5a14a27b`):** the U4 fold deleted the gated
> `spirits.get` and re-pointed the read surface at the UNGATED `rt.yi.read`, leaking every hidden row + the
> per-spirit PRIVATE signing key to any authenticated caller (ROB-1/4); `history`/`subscribe` inherited it
> (ROB-3); `countWhere` referent+holder branches leaked cardinality (ROB-2/BUG-1); two divergent `isSession`
> guards mislabeled a holding (BUG-2). All closed with regression tests. in-memory 3911/0 · PG 122(+4)/0.
>
> **OPEN — named residue (NOT done; do not read the spine as the whole goal):**
> - **The keystone (Law 1 — the face-shaped writer/index/API contract collapse).** `01-frame §2` calls it "not
>   optional and not deferred," yet HEAD still ships THREE face-shaped repo APIs (`spirits`/`unifiedHoldings`/
>   `yi`), four write builders, two visibility engines, two lifecycle engines. The BYTES are one table; the
>   CONTRACT above them is not. This is the deepest fidelity gap (ARCH-1/FID-1) and the biggest remaining
>   decision.
> - **U4.3/U4.4/U4.5 — RESOLVED (see `07-grand-review.md`):** U4.3 ✅ `forum.ts` raw `messages.history`→gated
>   `rt.messages.list`. U4.4 🟡 the face-named SUBSCRIPTION cursors are genuinely specialized (per-face indexed
>   replay) — end-state reconciled honestly + the generic-`yi.subscribe(predicate)` fold scoped as a named
>   track. U4.5 ✅ the std `rt.storage` "leak" AUDITED = legitimate privileged reads (no writes / no `any`
>   backdoors / no user-authority bypass); `rt.storage` IS the documented ungated substrate for trusted kits.
> - **`face_class` (FID-2)** is still a required, stored discriminator in the event/audit tier. **Sub-face
>   vocabulary (ELEG-2):** `isToken`↔`sys/attestation`↔`'attestation'` — two names per concept. **Dimension
>   key drift (FID-4):** `sys/identity`'s bucket is keyed `'identity'`, breaking `Record<KindRef>`.
> - **Dead legacy (LEG-1):** an empty extinguish-alias subsystem still wired in. **LEG-4 (corrected
>   2026-06-25):** the pre-unification 事/间/机 face taxonomy is **comment doc-rot only (not wired)** — the
>   row-face is `kinds[]`-derived (`faceFromKinds`, no stored `face_class` per Law 2); the stale CJK-taxonomy
>   glosses have been stripped from the JSDoc. **doc-rot (LEG-2/3)** in the public RPC/holding JSDoc describing removed APIs as live.
> - U2.5 mint-authority = the D15 policy-engine program; gate-cache stays `[destination]`.
>
> **§2 framing revisions — RATIFIED + APPLIED 2026-06-24** (founder ratified): **G8** added to `00-direction`
> (the cognitive-budget goal); **D8** sharpened in `02-pivot` (one encoding per membership *relation*; the two
> relations named, not collapsed); **G5 `explain`** re-tagged WIRED in `03-architecture` (U2.3) and the
> **gate-cache** kept `[destination]`. The **`01-frame §2` keystone** was clarified to ACHIEVED+plumbing —
> grounded in G1 `item-as-agent` (an item that acts) + G8 enforcement: capability is a trait, the face is
> storage routing; the original "collapse the storage contract" prescription was superseded by the
> trait-based path (collapsing the load-bearing `@internal` typed views would break correctness).
>
> **The complete itemized residue checklist (every finding, file:line, status) lives in
> [`07-grand-review.md`](07-grand-review.md)** — the "remember all of it + fix completely" ledger.

---

## 0. The one-sentence verdict

**Representation is unified; meaning is not yet.** The Yi spine — one row, one write surface, one dispatch
resolver, one gate ADT, one membership *decision*, one kind-authoring verb — is real and load-bearing
(fidelity **≈81/100**, independently re-derived). But it is wrapped in legacy shells that a developer still
holds in their head: a 13-canonical + ~38-class-spec `Kind` read through **~57 `cls*` accessors**, **face-
named wire/client namespaces** (`spirits.*`/`tokens.*`/`items.*`) that contradict "no face" at the
vocabulary level, **two parallel lifecycle handler maps**, **two ways to ask "who can"** (gate ADT vs
imperative `if`-throw), and **two privileged seeds** (`sys/spirit`, `sys/session`) that keep "spirit" and
"session" first-class even though behavior is face-agnostic. The measured cognitive count is **~17 distinct
concepts vs the ≤12 target** the whole pivot is justified on. This plan closes that gap.

---

## Table of contents

1. [The review findings (condensed)](#1-the-review-findings-condensed)
2. [Framing & pivot revisions — proposed for ratification](#2-framing--pivot-revisions--proposed-for-ratification)
3. [The two unified lenses (the explicit ask)](#3-the-two-unified-lenses)
4. [The fracture register (ranked by cognitive-frame damage)](#4-the-fracture-register)
5. [The execution plan — phases U0–U5](#5-the-execution-plan--phases-u0u5)
6. [The end-state — "the ideal Yi is achieved when…"](#6-the-end-state)
7. [Sequencing, DAG, parallelism](#7-sequencing-dag-parallelism)
8. [What this plan deliberately does NOT do](#8-what-this-plan-deliberately-does-not-do)

---

## 1. The review findings (condensed)

### 1.1 Fidelity — 81/100, and *why* it isn't higher

The spine is genuinely past the "additive / two-of-everything" band. Laws **1, 2, 5, 6, 8, 9** are honored
and load-bearing; goals **G1–G7** all have green acceptance tests against real production code (no hollow
mocks). Agency-as-trait (G1/L6) is the **strongest** result and *exceeds* what the architecture doc claims.

The −19 is four things, in order of damage to the unified-mental-frame goal:

- **−8 closure not achieved (L3).** The cross-trait combination matrix is still **N=9** and has not shrunk to
  M; ~38 stored `Kind` class-spec fields + ~57 `cls*` accessors remain. Closure is the stated acceptance
  test (D6) and it has not passed.
- **−5 the face has not dissolved into the vocabulary (L6, the deepest gap).** Behavior is face-agnostic, but
  `sys/spirit` + `sys/session` remain privileged seeds, `membered`+`streamed` are **inert markers composed by
  nothing**, and `addKind('sys/identity')` does **not** mint a key (a live signing bug — see §3 / U3).
- **−3 the cognitive metric is unmeasured.** First actual count: **~17** vs ≤12. The thing the pivot is *for*
  is the one thing not on the scorecard.
- **−3 two Phase-3 mechanisms are BUILT BUT UNWIRED while marked CLOSED** (the one place the docs over-claim):
  the **G5 one-graph `explain`** wires only `explainPortGate` at runtime (`explainWriteAuthz` has zero non-test
  callers; the "six sources in one graph" is assembled in a *test fixture*, not the runtime), and the
  **compiled gate cache** (`GateCacheEngine`) is tested but consulted by no read path (the gate is still
  walked per-invoke, contradicting L5 "compiled, not walked").

### 1.2 The two unwired mechanisms (claim-vs-code gap to close)

| Mechanism | Claimed | Actual | Fix |
|---|---|---|---|
| G5 one-graph `explain` | "one trace spanning all six authority sources" | runtime walks only the port gate; `explainWriteAuthz` unwired | U2.3 wire it, or re-tag `[destination]` |
| Compiled gate cache | "compiled, not a predicate tree walked per invoke" (L5) | `GateCacheEngine` built + tested, consulted by no read path | U2.4 wire it, or re-tag |

### 1.3 SDK shape — strong spine, legacy multiplicity around it (~7/10)

A developer touches **far more than the four words** the frame promises: **~24 `rt.yi.*` verbs + ~38 verbs
across 11 sibling `rt.*` namespaces + ~18 free seam functions**, and the wire ships **72 RPC verbs across
face-named namespaces** (`spirits.*`(8) / `tokens.*`(3) / `sessions.*`(13) / `agents.*`(9) …) with a
19-namespace typed client. Per-surface maturity: **invoke 9/10** (the cleanest — one resolver, second
dispatch surface deleted), **authoring 7/10** (capped by the un-dissolved `Kind`), **query 7/10**, **kit
6/10** (~52 `rt.storage.*` convenience-read leaks + two handler-registration mechanisms), **wire/client
6/10** (the most legacy vocabulary). Estimated **~70% of the way** to "one obvious way."

---

## 2. Framing & pivot revisions — proposed for ratification

The direction holds. These are sharpenings the founder invited ("the framing can be revised"). They are
**proposed**, not applied — the ideal docs 00/01/02 stay pristine until the founder ratifies. Each is
KEEP or REVISE with the reason.

- **REVISE — add G8: a CI-enforced cognitive-concept budget.** *Why:* the north star is "fewest concepts a
  developer holds," yet no goal measures it; G1–G7 measure capabilities. Make the budget a scripted gate
  (kept-vocabulary ≤12 · `cls*` count ≤ target · `holdingSubFaceFromKinds`=0 · one dispatch surface ·
  zero `kinds.includes('sys/spirit'|'sys/session')` capability branches). This *operationalizes the thing the
  pivot exists for.* Highest-leverage framing change. → built in **U5**.
- **REVISE — D8 "membership ×3→×1" → "one encoding per membership *relation*", and name the two relations.**
  *Why:* the build proved membership is **two distinct relations** — session-participation (`anchorMembers` ∪
  `memberKindUid`) and community-standing (`bears('<c>/member')`) — not three encodings of one. The current
  wording invites a future engineer to wrongly collapse two different relations into one. Adopt the sharpened
  statement.
- **REVISE — re-tag G5 one-graph `explain` + the compiled gate cache from CLOSED to `[destination]`** in
  `03-architecture.md §7` and the G5 matrix row — *or* wire them (U2.3/U2.4). *Why:* they are built-but-unwired;
  "CLOSED" is the one place the docs slip from their otherwise-exemplary honesty.
- **KEEP — "the face dissolves into traits."** *Why:* it is the program's strongest, most load-bearing result;
  the objection "spirit/session should stay seeds" is answered by code (dispatch is already generic). Defend it
  — and finish it (U3).
- **KEEP — Law 4 "one connection," with its authoring-surface caveat kept prominent.** *Why:* the law is right
  *as written*; the danger is mis-reading it as "all ties behave alike." The D8 sharpening makes it concrete.
- **KEEP — Law 10 (subtract-first), un-softened, despite its disclosed inversion.** *Why:* the principle is
  correct as a target; the inversion was an execution-sequencing failure under goal-pressure, already disclosed.
  Do not edit the law to match what happened — that would violate the code→docs discipline. Add one line naming
  the inversion's *cost* (RR1–RR7 are *why* subtractions are still landing).
- **KEEP — D15 (resource-scoped policy engine) as the right boundary.** *Why:* verified — the `policy` node
  lives *inside* the Gate ADT (`gates/gate.ts`), precedence is a gate-node resolver (`policy-algebra.ts`), not a
  parallel algebra. `KindPolicy`-dissolution is structurally **disjoint** from D15 and ships independently.
- **KEEP — `mutual` as a stored boolean** (the blocked RR6 dissolution). *Why:* a relationship is mutual-by-
  default; a pure presence-marker is default-false and would invert the contract. The `sys/directed-edge`
  complement is real design out of scope; forcing it would *relocate* the zoo (the D6 trap). The boolean is the
  honest canonical signal.

---

## 3. The two unified lenses

The founder asked for "a more unified lens" on KindPolicy and storage, and for an ideal where there is no weird
"this thing is implemented a different way when there should be a unified approach." For both, the honest
answer is **not** "force everything through one mechanism" — it is "**name the genuine distinction crisply, fold
everything that is actually the same thing, and delete the dead.**"

### 3a. KindPolicy + Kind authz — TWO questions, cleanly partitioned

There are exactly **two** authorization questions in the kernel, and the fracture is that today they are each
asked **more than one way**. Unify *within* each, never *across* them (collapsing them is double-gating — the
exact trap the RR1/RR7 partition guards against):

| The question | Canonical mechanism | What must fold INTO it | What must NOT |
|---|---|---|---|
| **"May this caller invoke/transition this row?"** (caller-port-authz) | the **Gate ADT** (so `explain()` / G5 spans it) | `publicGrant` (imperative at `item.ts:263`); `contracts.{mint,transfer,burn}` (gate-shaped, unenforced today) | — |
| **"Is this operation structurally legal for this kind?"** (mint/transfer/burn invariants) | the **in-tx structural floor** (imperative, at the substrate chokepoint) | stays where it is — `transferable`/`revocableBy`/`maxPerHolder`/`bond`/`can_mint` are kind *invariants*, not caller permissions | do **not** fold these into the gate ADT — that re-homes structural floors as gate leaves = D15-scale, and re-introduces double-gating |

**Dead → delete (zero readers):** `invokeAuth` (its only decision-reader died with `invokeItemDirect` this
turn; `clsInvokeAuth` is now read only at `item.ts:472` as fork-copy) → delete field + accessor + `deploy.ts:175`
default + fork-copy + the `addressable→invokeAuth` translation at `holding-class.ts:1006`. The three dead
`KindPolicy` sub-fields `mutableBy`/`initialGrant`/`strictRequirements` (the KindPolicy session's work — see U0.3).

**The unifying statement for 02-pivot:** *every caller-authz question is a gate leaf the one `explain` graph
spans; every structural-legality invariant is an in-tx floor; there is no third way, and the two are never
merged.* This is "one approach per question," which is what the founder's principle actually requires here —
because `transferable` (a kind invariant) and `invokeAuth` (a caller permission) are **not the same thing**.

**The KindPolicy session's uncommitted work (8→5):** SOUND and equivalence-preserving (all three deleted
sub-fields verified zero-reader; `maxPerHolder` correctly KEPT). Applies cleanly onto HEAD **except** its two
edits to `item-addressable.test.ts` (HEAD deleted that whole file). → **U0.3: re-apply minus those two edits,
regen snapshot, verify.**

### 3b. Storage + runtime access — GATED VERBS vs UNGATED SUBSTRATE

The parallel storage session reached the right verdict (keep `rt.storage`) for the **wrong reason**. The
principled line is **not** "perspectival vs privileged" — it is **gated vs ungated**:

- **One gated verb surface per noun** — `rt.yi.*` (+ the named tiers). Every read runs visibility; every write
  runs port/authz gates.
- **One ungated substrate root** — `rt.storage` (mark `@internal`). Raw rows, `spiritByPath`, `withTx`,
  `projections`, `scheduler`, `childrenOf`, the global event-log tail. The **trust boundary is the wire**, and
  it is *empirically* the wire: the client has no `storage` member, there is no `storage` wire verb, and
  `rt.storage` is touched in exactly **one** non-test SDK file (the in-process agent runner). So untrusted code
  physically cannot reach it. **KEEP the root.**

The real fracture the founder dislikes is **not** that `rt.storage` exists — it is **duplicate *gated* verb
surfaces for the same noun**, plus the face-named wire/client:

- `rt.messages.list/currentPath` (gated) **and** `rt.storage.messages.history` (raw) both read the stream, and
  std mixes them (13 gated + 2 raw). → fold to one gated message-read surface (U4.3).
- face-named wire namespaces (`spirits.*`/`tokens.*`/`items.*`/`relationships.*`) and the 19-namespace client →
  fold into `yi.*` + a `client.at(uid)` read-lens (U4.1/U4.2). This is the single biggest SDK unification win.
- ~52 std `rt.storage.yi.*` convenience reads that bypass visibility for trusted bookkeeping → migrate
  to `rt.yi.read/where`, or expose **one** named privileged handle (not raw `rt.storage` + `rt.registry` +
  `rt.ports` reached ad hoc) (U4.5).

**Doc correction (supersedes the storage session's framing):** re-characterize `rt.storage` as "the ungated
substrate root," not "the privileged carve-out distinct from perspectival verbs," and drop "the §17 one-root
ideal is `rt.yi`" — there are already many gated verb roots (`rt.messages`/`rt.graph`/`rt.session`/…); the north
star is *one gated verb surface per noun* over *one ungated substrate*. Keep the proposed `@internal` tag on
`Runtime.storage` (it is correct and still uncommitted at HEAD).

The storage **contract** itself (RR2) is genuinely unified: zero per-face read sites in any kit; `storage.yi.*`
is one read+write contract; `messages`/`events`/`projections` are cleanly separated tiers with intentional
same-tx coupling (correct CQRS). Residual: per-face *write* repos survive as `@internal` delegation bodies
(one contract, two bodies — cosmetic, low value).

---

## 4. The fracture register

Ranked by cognitive-frame damage (how badly it makes a developer ask "why are there two/seven ways?"). The
lead is the worst.

| # | Fracture | The ≥2 implementations (file:line) | Unified target | Class | Track |
|---|---|---|---|---|---|
| **1** | **Kind class-spec grab-bag + ~57 `cls*` accessors** | `class.ts:378–494` stored block (methods/hooks/handlers/modifiers/slots/partySchema/contracts/claimTriggers/…); `class-accessors.ts` ~57 read-time reconcilers | `ports`+`lifecycle`+one `triggers` map; ~0 accessors | needs-design (gated on the dispatch fold, mostly done) | **U1** |
| **2** | **Two lifecycle handler maps** | `SpiritHooks` snake_case (`types.ts:746`, `fireTriggers`) vs `ClassLifecycle` camelCase (`item-lifecycle.ts`, `fireItemLifecycle`); `on_invoke`/`onInvoke` homonym; 5 distinct "when X→run Y" mechanisms | keep the 2 *engines* (deferred-cascade vs inline-chain are genuinely different); unify naming + the `ClassLifecycle` union field | naming foldable-now; engines keep | **U1.3** |
| **3** | **Two gated verb surfaces per noun + face-named wire/client** | `rt.messages.list` vs `rt.storage.messages.history`; wire `spirits.*`/`tokens.*`/`items.*` (72 verbs) + 19-namespace client vs `yi.*` | one gated verb surface per noun; wire mirrors `yi.*` 1:1 | needs-design → fold | **U4** |
| **4** | **Mint-authority multiplicity** | `create.ts:1126` `perFaceMintOwnsAuthority` routes to one of {gate, license, `can_mint`, subtree}; `add:deny`-as-marker overload | one `mintAuthority(kind)→Gate` compiling license/can_mint/subtree into gate leaves | needs-design | **U2.5** |
| **5** | **Authz spelling: gate ADT vs imperative `if`-throw** | gate ADT (~11 sites) vs ~95 `throw PermissionDenied`; `publicGrant` (item.ts:263), `contracts` (unenforced), `invokeAuth` (DEAD) | partition per §3a: caller-authz→gate; structural→floor; delete dead | mixed (see §3a) | **U0/U2** |
| **6** | **Schema field cluster** | `rowSchema` (canonical) + `payloadShape` (live) + `dataShape` (unvalidated) + `stateShape` (**DEAD**, accessor already deleted) | delete `stateShape`/`dataShape`; `payloadShape`→`rowSchema` (requiredMode) | foldable-now / contained | **U0.2 / U1.4** |
| **7** | **Two privileged seeds keep "spirit"/"session" first-class** | `sys/spirit` (`substrate-seed.ts:286`, identity+profile bundled), `sys/session` (`:671`, `add:DENY`); `membered`/`streamed` inert (only `gate.ts:757`) | session = `membered`+`streamed`; `sys/spirit`→`identity`+`profile`; kill face-field branches | needs-design (mostly plumbed) | **U3** |

**Cleared — NOT fractures (do not re-flag):** `grants` (trait-linearization splice) vs `confers` (live port
projection) — same concept, incompatible timing/cache, cannot fold without breaking Law 8; seam compiler vs
`manifest({referent})` — collaborate (seam emits manifest), not parallel; `Token`/`Relationship`/`Item` =
`Holding` aliases — cosmetic; `EVAL_VERB_ALIASES` — empty infra.

---

## 5. The execution plan — phases U0–U5

Each track: **target (file:line) · acceptance · risk**. Green-bar per `04 §7`. Risk: **S/M** full-auto,
**L** = adversarial-verify + design pass first.

### Phase U0 — pure subtraction (dead shapes, zero behavior change) · risk S · parallel-safe

> Do first. Each is dead-code removal verified by "no reader." Establishes momentum; shrinks the surface.
>
> **STATUS (2026-06-22): substantially LANDED.** U0.1 ✓ (`273627b2`), U0.3 ✓ (`480b0cb9`, via a worktree
> agent), U0.4 ✓ (`696a2539`). Two refinements found during execution: **U0.2 (`*Shape`) moved to U1.4** — it
> is NOT pure subtraction: `dataShape` is entangled (spirit deploy maps `input.dataShape → payloadShape`, the
> enforced field, at `spirit.ts:1582`), so the `*Shape` cluster must be unified coherently in U1.4, not split.
> **U0.5 (`contracts`) moved to U2.2** — `contracts` is an *intended* mint/transfer/burn-condition feature that
> is gate-shaped but unwired; the right move is to fold it into the gate ADT (U2.2), not delete designed surface.
> Each landed slice: typecheck 0 · typecheck:tests 0 · in-memory 3889/0 · PG 122 (+4)/0.

- **U0.1 — delete `invokeAuth`.** Field (`class.ts:469`), `clsInvokeAuth` (`class-accessors.ts:513`), deploy
  default (`deploy.ts:175`), fork-copy (`item.ts:472,490`), `addressable→invokeAuth` translation
  (`holding-class.ts:1006`), `HOLDING_PASSTHROUGH_FIELDS` entry (`holding-class.ts:306`), `index.ts:84` export.
  *Accept:* zero `invokeAuth` refs in core src; snapshot regen; suite green.
- **U0.2 — delete `stateShape` + `dataShape`.** Unenforced passthrough (`clsStateShape` already deleted as
  orphaned). Field + accessor + `ClassExtraFields` + `HOLDING_PASSTHROUGH_FIELDS` + deploy/fork promotions +
  inventory entries. *Accept:* inventory test passes with both removed; suite green.
- **U0.3 — KindPolicy 8→5.** Re-apply the KindPolicy session's uncommitted change from worktree
  `adoring-ardinghelli-c483cb` **minus** its two `item-addressable.test.ts` edits (HEAD deleted that file).
  Deletes `mutableBy`/`initialGrant`/`strictRequirements` + accessors + writer legs. *Accept:* `KindPolicy` has
  5 fields; `MutableStateConfig.mutableBy` (the live one) untouched; snapshot regen; suite + PG green.
- **U0.4 — delete vestigial aliases.** `rt.events` (zero live readers); assess `Token`/`Relationship`/`Item`
  aliases (cosmetic — keep or inline). *Accept:* suite green.
- **U0.5 — `contracts`: decide.** It is gate-shaped but has **no runtime evaluator**. Either delete now (field +
  `clsContracts` + fork-copy + validator presence-flag) or defer to U2.2 if the mint/transfer/burn conditions
  are a real intended feature. Recommend **delete now**; re-introduce as gate `when`-arms in U2 only if needed.

### Phase U1 — the Kind grab-bag dissolution + `cls*` collapse · risk M–L · the #1 cognitive tax

> The single highest-leverage cleanup: every `cls*` accessor deleted removes a "why are there two homes?"
> question. Mostly unblocked now that the item-method dispatch surface is gone (this session).
>
> **STATUS (2026-06-22): U1.1 LANDED (`b3aad417`, via a find→implement→adversarial-verify workflow).** It went
> beyond the original scope — the no-legacy decision removed the *entire* `getInterface` / `spirits.interface`
> introspection verb + `ItemMethodView` + `SpiritInterfaceView` across core/server/SDK/sigil/web (not just the
> empty branch), since the verb only ever returned empty item-method data. **−1022/+208 LOC, 43 files**, wire
> protocol 7→8, both snapshots regenerated; 3 adversarial lenses (equivalence/wire-safety/test-integrity) all
> refuted=false@high; typecheck 0 · typecheck:tests 0 · in-memory 3887/0 · PG 122 (+4)/0. The `cls*` count is
> down ~7 (invokeAuth, initialGrant, strictRequirements, methods, methodList, methodNamespace, addressable).
> One web note: the SpiritDetail *Interface panel* is gone with the verb (it displayed the dead item-method
> surface); if equip-`slots` display is wanted later, re-source it from the row's kind, not a verb.
>
> **REFINEMENT — U1.2 reprioritized.** Per D6 ("the win is *closure*, not relocation"), `forkable`→`policy.forkable`
> and `tags`/`icon`→dimension are *relocation* (the field + its `cls*` accessor survive, just in a different
> bucket) — they do NOT reduce the held-concept count. So U1.2 is **deprioritized** (do only if it enables an
> accessor deletion).
>
> **U1.4 LANDED (`66ac8c03`, via a find→implement→adversarial-verify workflow).** Delivered the conservative
> safe subset — deleted dead `stateShape` (zero readers; no state-shape validation exists) + collapsed the
> redundant stored `dataShape` into `payloadShape` (the spirit authoring input still flows to `payloadShape`;
> the duplicate stored field + `clsDataShape` + the `dataShape` DimensionRegistry seed/id-push are gone). It
> **correctly DEFERRED `payloadShape`→`rowSchema`**: they are distinct buckets (immutable `payload` at mint vs
> per-dimension at manifest/patch), a semantic merge not a field-collapse — out of scope for an equivalence-
> preserving pass (the requiredMode flag would be pure relocation). 15 files, +53/−55; typecheck 0 ·
> typecheck:tests 0 · in-memory 3887/0 · PG 122(+4)/0; a fresh adversarial equivalence lens (the 3 in-workflow
> lenses died on an API interruption) returned refuted=false@HIGH after 6 checks. `cls*` count now down ~9 from
> ~57.
>
> **Remaining U1:** U1.3 (collapse the two lifecycle handler maps' naming) is medium-value/medium-risk (broad
> rename, silent-break risk, modest closure since both *engines* stay). The next HIGH-value track is **U3 (face
> dissolution)** — real concept reduction + a live signing-bug fix — which is keystone/L-risk and gets a design
> pass first.

- **U1.1 — delete `methods`/`methodNamespace`/`addressable` + the `getInterface` item-view branch**
  (`spirit.ts:1412–1433`, always-empty in production). This is the wire-surface slice deferred from this
  session's dead-dispatch deletion. Removes `clsMethods`/`clsMethodList`/`clsMethodNamespace`/`clsAddressable`
  + `ItemMethodView` from the surface. *Risk M (touches wire/snapshot).* *Accept:* snapshot regen + wire
  version bump; suite green.
- **U1.2 — fold `forkable`→`policy.forkable`** (the proven KI4 pattern: `clsForkable` reads `policy.forkable`
  like `clsTransferable`); move `tags`/`icon` to a dimension or delete the registry id-push. *Risk S.*
- **U1.3 — unify the two lifecycle handler maps' naming + collapse the `ClassLifecycle` union field + the dual-
  shape `triggers`.** Keep both dispatch *engines*; fix the `on_invoke`/`onInvoke` homonym; one casing.
  *Risk M.* *Accept:* one authoring vocabulary for lifecycle; suite green.
- **U1.4 — `payloadShape`→`rowSchema`** via a `requiredMode:'full'|'incremental'` flag on the validator
  (`schema-validate.ts`), repoint the ~6 mint sites. *Risk M (live enforcement).*
- **U1.5 — collapse the `cls*` accessors** toward zero as their backing fields dissolve; shrink the
  `kind-field-inventory` map in lockstep (the no-phantom gate enforces it). *Risk L; gated on U1.1–U1.4.*
  *Accept:* `cls*` count drops from ~57 to a documented floor; the N=9 closure matrix tracked (and shrunk where
  feature-traits land).

### Phase U2 — authz unification + wiring the unwired (G5 made real) · risk L

> Fold the genuine caller-authz fields into the gate ADT; **wire the explain graph + the cache** so the L5/G5
> claims become code. Adversarial-verify each (these touch authorization).
>
> **STATUS (2026-06-23): U2.1–U2.3 LANDED (`5538afb3`, atomic workflow + 3 adversarial lenses + 1 orchestrator
> equivalence fix).** U2.1 — `publicGrant` folded into a new `caller-owns-or-public-grant` gate leaf (reads the
> FOREIGN granted kind-spec; `explain` spans it). The equivalence lens caught that the fold dropped the granted-
> owner **liveness guard** (a `publicGrant:true` class with a since-burned owner flipped deny→allow) — restored
> as an imperative validation guard (byte-equivalent; the gate keeps only the authz decision). U2.2 — the dead
> `contracts` Kind field (gate-shaped, zero runtime evaluator) deleted in 5-site lockstep. U2.3 — the one-graph
> `explain` WIRED as **sibling-dispatch** (write-action→`explainWriteAuthz`, port-invoke→`explainPortGate`), NOT
> an `and(floor,portGate)` node (which would fabricate a conjunction the runtime never computes — explain would
> lie). G5 is now real, not a fixture. typecheck 0 · typecheck:tests 0 · in-memory 3895/0 · PG 122(+4)/0.
>
> **U2.4 (gate cache) = NO-OP.** `03-architecture.md:463` already tags "compiled, not walked" as `[destination]`
> and `01-frame.md:383` states it as an aspiration ("*should* resolve into a cacheable artifact"), not an
> achievement — the ideal docs are already honest. The cache (PE3) is built but unwired; wiring it needs a
> `Gate→spec` compiler (a separate *perf* project, not a frame/no-legacy concern). No softening needed.
>
> **U2.5 (mint-authority) = DOCUMENTED D15-RESIDUE, not an equivalence-preserving slice.** Twice-confirmed (the
> prior `RR7-pt2` finding + the U2 design's adversarial pass): `perFaceMintOwnsAuthority` (`create.ts`) is a
> 3-disjunct *skip* predicate, NOT a 4-way fracture; the mint authorities (license / `can_mint` rule-hook /
> subtree / gate) are **genuinely separate layers, not duplicates**, and each kind already routes to *exactly
> one* — mint authority is already conceptually one-per-kind (no legacy fracture). `can_mint`'s per-site caller
> defaults make a naive fold a **caller-rebinding trap**, and `add:deny`-as-marker encodes owner-path semantics a
> gate leaf can't express. Collapsing the *mechanisms* into one gate ADT = re-homing the license subsystem +
> rule-hook as gate leaves with negative-rights/precedence = the **D15 policy-engine program** (partly built,
> PE1–4). Honest residue, not a forced fold.

- **U2.1 — fold `publicGrant` → a gate leaf** the deploy-grant path consults (e.g. `or(caller-owns-class,
  target-class-is-public-grant)`), so `explain` spans deploy-grant authority. *Accept:* explain trace includes it.
- **U2.2 — `contracts.{mint,transfer,burn}` → gate `when`-arms** *iff* kept (else done in U0.5).
- **U2.3 — WIRE the one-graph `explain`.** Fold `explainWriteAuthz` + the visibility guard into the runtime
  `rt.yi.explain` trace (today only `explainPortGate` is wired). Close the G5 claim-vs-code gap. *Accept:* the
  `explain-one-graph` assertion runs against the *runtime* path, not a test fixture.
- **U2.4 — WIRE the compiled gate cache** (`GateCacheEngine`) into the invoke/read path so the gate is consulted
  compiled, not walked per-invoke (L5). *Accept:* a perf/behavior test shows the cache is consulted; or, if
  deferred, re-tag L5/§7 honestly per §2.
- **U2.5 — one mint authority.** Compile license / `can_mint` / subtree into gate leaves → a single
  `mintAuthority(kind)→Gate`; delete the `perFaceMintOwnsAuthority` router and the `add:deny`-as-marker overload
  (`create.ts:1126`). *Risk L (the central mint path — design pass + equivalence test mandatory).*
- **PARTITION GUARD:** `transferable`/`revocableBy`/`maxPerHolder`/`bond` **stay imperative in-tx floors** —
  they are kind invariants, not caller permissions. Do **not** fold them (§3a).

### Phase U3 — the face dissolution (deepest gap, biggest fidelity win) · risk L

> Make "agency is a trait" true at the vocabulary level. Mostly plumbed by RR4 + the seam compiler.
>
> **DESIGN PASS DONE (2026-06-23, read-only workflow) — KEYSTONE, AWAITING FOUNDER DECISION.** Three parallel
> maps + an adversarial reviewer. Findings:
> - **U3.1 is NOT a live bug (red-test correction).** The design claimed `addKind('sys/identity')` mints no key;
>   red-testing showed it is **gate-unreachable for normal callers**: `sys/identity` is `add: ANCESTOR_OF_TARGET`,
>   spirits are always keyed (so it's a safe no-op — `getIdentity` also falls back to the spirit-home key), and
>   keyless holdings are uncontained (`mintHolding` sets no `parentUid`) so no ancestor caller exists → the gate
>   denies. The current code is **correct in practice**; NOT shipping U3.1. (Lesson: the design reasoned from the
>   static code path without checking gate-reachability; red-test-first caught it.)
> - **U3.2 is bigger than "drop a marker."** `sys/session` is the **bucket-key** for the entire session payload
>   (11 accessors, 3 writers incl. a missed one at `runtime-messages.ts:316`), a **PG unique index**
>   (`yi_dim_anchor_path`), the `yi.ts` dimensions type, `where()` index-routing, event-replay re-materialization,
>   AND an `add:DENY`/`frozen` **gate posture** (vs `membered`/`streamed`'s `add:ANCESTOR_OF_TARGET` — re-homing
>   makes a session-marker *addable*, a security change). Dissolving it re-homes the payload + needs a new
>   migration/index + orphans existing PG session rows.
> - **U3.3 cannot fully dissolve.** `createSpiritRow`/`writeShapeFromKind`/`storage.spirits` all key on
>   `sys/spirit`; keep a thin `sys/identity`+`sys/profile` composite carrying the NAME (the `sys/bot` status).
>
> **FOUNDER RULED (2026-06-23): FULL DISSOLUTION, NO COMPROMISE, greenfield reset authorized.**
>
> **U3.2 LANDED (`6d8e6ada`, atomic workflow + 4 adversarial lenses clean).** `sys/session` is GONE — the seed,
> the marker, the `SYS_KINDS.session` ref, the bucket-key, every discriminator. A session is now a `chat` row
> composing `sys/membered` + `sys/streamed` (both given real rowSchemas); `isSession()` = the membered∧streamed
> conjunction. Payload re-homed: membership (`anchorMembers`/`memberKindUid`/`joinPolicy`/`projectionId`/
> `anchorVisibility`) → `sys/membered`; thread + `anchorPath` → `sys/streamed`. PG unique index re-keyed off
> `dimensions->'sys/streamed'->>'anchorPath'` (migration `013`, greenfield no-backfill). 67 files, +632/−419;
> the workflow caught a 4th payload writer (`anchorSpiritAsSession`) I'd missed. typecheck 0 · typecheck:tests 0
> · in-memory 3888/0 · PG 122(+4)/0. Gate-posture note (not a floor break): `membered`/`streamed` are
> `add:ANCESTOR_OF_TARGET` (vs the old `sys/session` `add:DENY`) — correct in the dissolved world (no session
> face to protect; ancestor-managed composition is legitimate).
>
> **U3.3 LANDED (`5e73d737`, atomic workflow + 4 lenses; 1 caught + fixed an `agent-task-worker` regression).**
> `sys/spirit` split: the keypair → `dimensions['identity']` (the `sys/identity` trait home, so a row signs its
> own moments), displayName/avatar → a NEW `sys/profile` trait; `getIdentity` reassembles the `SpiritIdentity`
> from the two buckets (no spirit-home fallback). Every capability/meaning branch on `kinds.includes('sys/spirit')`
> is killed. **Chosen approach: routing-marker-composite** (NOT delete-entirely) — the spirit/holding physical
> index-routing over the one `yi` table is invisible plumbing, NOT a held concept; ripping it out is a low-frame-
> value mega-risk to the foundational layer, so `sys/spirit` survives ONLY as the `kindFaceOf` storage-routing
> marker (composing identity+profile), the way `sys/bot` survives as a named composite. The held *concept* of the
> spirit face is fully dissolved. 48 files; typecheck 0 · typecheck:tests 0 · in-memory 3888/0 · PG 122(+4)/0.
> The ergonomic `identity:{displayName,keypair,avatar}` authoring alias was KEPT (zero churn for ~23+251 sites) —
> the chokepoint decomposes it into the two trait buckets.
>
> **✅ U3 (THE FACE DISSOLUTION) IS COMPLETE.** Both privileged faces dissolved into composable traits; a session
> is `membered`+`streamed`, a spirit is `identity`+`profile` (+ the routing marker). The frame's deepest promise —
> "agency is a trait, the face dissolves" — is now true at the vocabulary level, not just behaviorally.
>
> **NEW TRACK SURFACED — U6 (docs/examples migration):** the `docs/examples/*` build was ALREADY red before this
> session on accumulated no-backwards-compat debt — the removed runtime kind-deploy method (RR5, gone), `SpawnKindInput.face` (RR1,
> gone), `token`→`HoldingKind`. The examples build is a `check:release` gate, NOT the per-slice `pnpm typecheck`
> bar prior phases held, so it was never caught. "No legacy / finish all phases" requires migrating them — a
> dedicated mechanical track (deploy→`yi.manifest`, face→`{kind}`, token→holdingKind, + the U3 identity/profile
> reshape). Tracked here; sequenced after the core folds.

- **U3.1 — compose-time key provisioning (fixes a LIVE bug).** Add a declarative `onCompose` trait-provisioner
  run once, in-tx, after the gate passes, at **both** mint (`holding-ops.ts:697`) and `addKind`
  (`kind-ops.ts:~357`). `sys/identity`'s provisioner mints the keypair. Today `addKind('sys/identity')` produces
  a row that claims identity but has **no key and silently cannot sign** — a correctness asymmetry against frame
  §4/§7. *Accept:* a test where `addKind('sys/identity')` then signs; one key-mint site reached by all three paths.
- **U3.2 — session = `membered`+`streamed`.** Compose the two traits on the session-origin (`chat`) kind; move
  the roster/anchor metadata into the `membered`/`streamed` buckets; re-point `isSessionMember`
  (`auth.ts:490`) at the `membered` *trait* instead of the `sys/session` bucket; **drop the `sys/session` seed**
  and its `add:DENY`. `isSession(yi)` becomes `kinds.includes('sys/membered') && kinds.includes('sys/streamed')`.
  *Accept:* a session is literally a composition; G4/G7 green; no `where({kind:'sys/session'})` capability check.
- **U3.3 — split `sys/spirit` → `sys/identity` + `sys/profile`.** Move displayName/avatar to a `sys/profile`
  trait; spirits get their key via the U3.1 provisioner (not the face slot). **Kill the face-field branches**
  at `resolve.ts:60` and `deploy.ts:668`. A thin `sys/spirit` *composite* (`composes:[sys/identity,sys/profile]`)
  may survive as bootstrap sugar (the status `sys/bot` enjoys) — but no code may branch on
  `kinds.includes('sys/spirit')` for *capability*. *Accept:* G1/G6 green; zero capability branches on the seed.
- **U3.4 — make `membered`/`streamed` load-bearing** (they are inert today, `gate.ts:757` only): the provisioner
  + the floor read them. *Accept:* grep shows real readers; the inert-marker finding is closed.

### Phase U4 — SDK surface unification ("one obvious way") · risk M–L

> **STATUS (2026-06-23): LANDED (`9411ed8c`, atomic workflow + 4 adversarial lenses + 1 orchestrator leak-fix).**
> The 7 pure ROW-READ face-named wire verbs folded into the generic vocabulary: `spirits.get`→`yi.read`;
> `spirits.list`→`yi.where({kind:'sys/spirit',originKind?})`; `spirits.inventory`≡`tokens.holdings`→
> `yi.where({kind:'sys/attestation',holder,…})`; `spirits.contains`→`yi.where({parent})`; `items.list`→
> `yi.where({kind:'sys/capability',holder})`; `relationships.queryEdges`→`yi.where({kind:'sys/edge',…})`. The 4
> "blocked" folds were unblocked by EXTENDING `YiPredicate` with `feature` + `includeBurned` + an edge-originKind
> index branch (so the predicate expresses what `HoldingsFilter`/`ItemsFilter`/`QueryEdgesInput` carried). Client
> face-namespaces `client.items`/`client.relationships` deleted → the `client.at(uid)` read-lens; `client.spirits`/
> `client.tokens` keep only their computed verbs. KEPT (computed/reduced/product): `spirits.context`/`items`/
> `resolve`, `tokens.balanceOf`/`ownerOf`, `messages.*`/`sessions.*`/`agents.*`/`communities.*`/`posts.*`.
> Protocol bumped 8→9; snapshots regenerated. **LEAK CAUGHT + FIXED:** the holder/parent folds dropped the
> up-front anchor-spirit visibility gate the old `listInventory`/`listContains` had (a hidden spirit's public
> holdings/children leaked to an outsider — empirically confirmed). Restored on `yi.where`'s holder+parent
> branches AND the anchored holder `countWhere` (also closing the same pre-existing gap in the SDK `YiHandle`);
> regression tests in `where-fold-parity.fix.test.ts`. typecheck 0 · typecheck:tests 0 · in-memory 3900/0 ·
> PG 122(+4)/0.

- **U4.1 — fold face-named wire namespaces** (`spirits.*`/`tokens.*`/`items.*`/`relationships.*`, ~25 verbs) into
  the generic `yi.*` verbs (`methods.ts:503`). *The biggest SDK win.* *Risk L (wire contract — version bump,
  5-layer surface CI).*
- **U4.2 — fold the client face namespaces** (`client.spirits`/`client.tokens`/`client.items`) into a
  `client.at(uid)` read-lens over `yi.*`. *Accept:* client speaks the frame's vocabulary.
- **U4.3 — fold the `rt.messages` vs `rt.storage.messages.history` duplication** → one gated message-read surface
  (std's 2 raw sites → `rt.messages.list`); reserve raw `messages.*` for the kernel's append/seq internals.
- **U4.4 — label the sibling `rt.*` namespaces** (`rt.graph`/`rt.sessions`/`rt.messages`) as the `@bonfire/std`
  product layer over `rt.yi`, not peers of it — or fold. Update `03-architecture.md` to stop tagging the seam
  `[future]` (it is `[partial]` — `compileRelation` is built and used).
- **U4.5 — close the kit→storage leak + unify handlers.** Migrate the ~52 std `rt.storage.yi.*` convenience
  reads → `rt.yi.read/where`; expose **one** named privileged handle for genuine privileged needs (rule-hooks)
  instead of raw `rt.storage`+`rt.registry`+`rt.ports` reached ad hoc; collapse the two handler-registration
  mechanisms (`defineHandler` vs `rt.registry.set`) into one.

### Phase U5 — the cognitive budget gate + Law-4 completion · risk M

- **U5.1 — build G8 (the cognitive-budget CI gate).** Script the measured count (§1, currently ~17) and gate it:
  kept-vocabulary ≤12 · `cls*` accessor count ≤ floor · `holdingSubFaceFromKinds`=0 · one dispatch surface ·
  zero `sys/spirit`/`sys/session` capability branches. Make the win *measured, not asserted* (the open §8
  end-state condition). *Accept:* CI fails if the count regresses.
- **U5.2 — seam generalization (Law 4 completion).** Route the remaining hand-authored relations (grants,
  social edges, the message DAG) through `compileRelation` so "declare every relation by intent" is realized
  beyond membership. *Larger; may remain the Phase-3 SG track.*

---

## 6. The end-state — "the ideal Yi is achieved when…"

- a developer holds **≤12 concepts**, *measured* by the G8 CI gate (not asserted);
- there is **one gated verb root** (`rt.yi.*` + named tiers) over **one ungated substrate** (`rt.storage`,
  `@internal`); the **wire mirrors `yi.*` 1:1 for row reads/writes** (U4.1/U4.2) **and for streaming**
  (U4.4 ✅ — the face-named `holdings.byHolder`/`relationships.byReferent` subscriptions folded into one
  generic `yi.where` subscription, predicate-routed to the existing per-face indexed replay paths). What
  stays *intentionally* specialized (documented, not face-leak accidents): the **computed verbs**
  (`spirits.context`/`items`/`resolve`, `tokens.balanceOf`/`ownerOf` — no row-read equivalent) and the
  **message-tier** verbs (`messages.list` / `messages.bySession` — the Stream tier, like `rt.messages.*`,
  not a face);
- a `Kind` is **~13 canonical fields with ~0 `cls*` accessors**; behavior is `ports`+`lifecycle`+`triggers`;
- **every caller-authz question is a gate leaf the one `explain` graph spans** (wired, not a fixture); **every
  structural invariant is an in-tx floor**; there is no third way and the two are never merged;
- **no code branches on `kinds.includes('sys/spirit'|'sys/session')` for capability**; a session *is*
  `membered`+`streamed`; composing `sys/identity` mints a key at mint *or* `addKind`;
- the closure matrix is **shrunk, not relocated** (N→M, D6);
- the frame is true for the **vocabulary**, not just the bytes.

---

## 7. Sequencing, DAG, parallelism

```
U0 (pure subtraction) ──┬─> U1 (Kind dissolution) ──> U1.5 (cls* collapse) ──┐
   [do first, parallel] │                                                    ├─> U5 (cognitive gate: measures the result, LAST)
                        ├─> U3 (face dissolution) ───────────────────────────┤
                        │      [largely independent of U1]                    │
                        └─> U2 (authz: needs U0.1/U0.5; U2.5 central mint) ───┤
                                                                              │
U4 (SDK surface) ── independent of U1–U3; U4.1 is the big wire fold ──────────┘
```

- **U0** first — pure subtraction, parallel-safe, low risk, momentum.
- **U1 (Kind)** and **U3 (face)** are largely independent → two parallel tracks (separate worktrees; `class.ts`
  vs `substrate-seed.ts`/`session-product.ts` have low overlap).
- **U2 (authz)** depends on U0.1 (invokeAuth gone) + U0.5 (contracts decided); **U2.5** (central mint path) is the
  highest-risk track — design pass + equivalence test mandatory; serialize it.
- **U4 (SDK)** independent-ish; **U4.1** (wire fold) is L-risk (public contract).
- **U5** last — it *measures* the result; the count only hits ≤12 after U1.5 + U3 land.
- **Concurrency:** gate.ts / create-path / storage / class.ts are hubs — never run two hub-touching tracks in the
  same worktree. Separate PG databases for any concurrent integration runs (the `bonfire_test` collision lesson).

---

## 8. What this plan deliberately does NOT do

- It does **not** fold `transferable`/`revocableBy`/`maxPerHolder`/`bond` into the gate ADT — they are
  structural kind invariants (in-tx floors), not caller permissions; folding them is D15-scale and re-introduces
  double-gating (§3a).
- It does **not** build the `sys/directed-edge` marker — `mutual` stays a stored boolean (§2).
- It does **not** soften the ideal docs (00/01/02). The §2 revisions are *proposed* for ratification; until then
  the ideal is pristine and code rises to it.
- It does **not** change the direction. The four words, the ten Laws, the seven goals, the unified mental frame —
  all unchanged. This plan removes the legacy *shells* so the direction becomes *visible* in the surface a
  developer holds.

---

*Authored 2026-06-22 from the full multi-agent review @ `c30b4e66`. Supersedes `04-execution-plan.md §9`
(RR1–RR7), re-scoped under §3–§5. The first slice (delete the dead uid-direct item-method dispatch surface)
already landed at `c30b4e66`.*
