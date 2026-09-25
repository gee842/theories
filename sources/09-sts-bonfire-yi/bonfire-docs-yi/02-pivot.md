# The Pivot — Integrated Findings & Decisions

> **Implementation-status warning, 2026-06-26:** this is a decision/provenance
> record, not the current work ledger. Some route and status claims below have
> since landed or changed. Implementers should use
> `docs/yi/13-final-yi-sdk-closure-plan.md`,
> `docs/yi/14-privileged-authority-inventory.md`, and code/tests as
> authority.

> **Status:** committed decision record. This file integrates (a) a full read of the kernel as it
> stands today, (b) the diagnosis of why it generates constant friction, (c) the founder's original
> intent restated, (d) an assessment of the two prior inputs — `docs/design/unified-mental-frame.md`
> (the multi-round exploration) and a peer-agent design critique — and (e) the decisions we have now
> frozen. Its output and successor is the canonical concept doc, [`the-frame.md`](../01-frame.md),
> which is the North Star the codebase is to be refactored *toward*.
>
> **One-line thesis:** Bonfire unified the layer it should have left plural (*representation* — one row,
> one table, one message DAG) and left plural the layer it meant to unify (*meaning* — subject/object as
> a stored type, the relationship primitive split ~8 ways) — and, the case analysis later proved, it never
> even *finished* the unification it did attempt: the bytes are already one `yi` table (PG migration `001`),
> but a Yi's subject/object nature is still frozen at birth behind a **face guard** and routed through
> **face-shaped repo APIs** (writer · index · fold · SDK/RPC), so the keystone of the whole refactor is
> collapsing that *face-shaped contract* — **not** merging tables (D11). The pivot is to invert the
> meaning/representation split: unify the
> **meaning** (one entity, one relation, meaning in the open) and let the **representation** stay plural
> *below a seam the author never crosses*.

---

## Table of contents

1. [The kernel as it stands today](#1-the-kernel-as-it-stands-today)
2. [The diagnosis — what generates the friction](#2-the-diagnosis--what-generates-the-friction)
3. [The original intent, restated](#3-the-original-intent-restated)
4. [Assessment of the two inputs](#4-assessment-of-the-two-inputs)
5. [The decisions (frozen)](#5-the-decisions-frozen)
6. [What stays below the seam (kept, not deleted)](#6-what-stays-below-the-seam-kept-not-deleted)
7. [Open forks — still the founder's call](#7-open-forks--still-the-founders-call)
8. [The sequence of moves](#8-the-sequence-of-moves)
9. [Appendix — evidence index & corrections](#9-appendix--evidence-index--corrections)

---

## 1. The kernel as it stands today

The core is a **layer cake**: storage at the floor, the `Yi` row + faces above it, the kind/dimension
type-system, the capability/authz layer, the `rt.yi.*` runtime spine that assembles all of it into verbs,
then reactivity and product surfaces on top. Dependencies point downward. (A read of all ~60 core modules
backs this; the per-cluster detail lives in the design exploration, this is the integrated shape.)

| Layer | Files | Responsibility |
|---|---|---|
| Product & messaging | `sessions`, `session-product`, `runtime-messages`, `content-blocks`, `plugins`, `graph`, `attachments` | sessions, the message DAG, kit install, graph traversal |
| Reactivity & lifecycle | `triggers`, `scheduler`, `lifecycle`, `item-lifecycle`, `context`, `recovery/`, `migration/` | event-driven handlers, ticks, stat/requirement engine, key-recovery, host migration |
| Verb · gate · dispatch | `invoke`, `invoke-frame`, `runtime-yi/port-dispatch`, `gates/`, `predicate`, `predicate-ast`, `discovery` | port resolution, gate evaluation (the authz ADT), cycle/depth guard |
| **rt.yi.\* spine** | `runtime`, `runtime-invoke`, `runtime-yi/*`, `request-cache` | `manifest · touch · invoke · read · where · addKind · patch · extinguish · discover · explain` |
| Capability & authz | `auth`, `holdings/`, `grants`, `grant-events`, `authority`, `builtins` | `assertCan` (the one write-authz seam), holdings, grants, licensing, built-in classes |
| Kinds & dimensions | `kinds/`, `dimensions/`, `schema-validate`, `schema-evolution`, `dsl`, `features` | kinds-as-rows, the open dimension registry, schema validation/evolution |
| Substrate — one Yi row | `yi`, `yi-accessors`, `yi-guards`, `substrate/{spirit,item,token,edge,write}`, `substrate-seed` | the universal row, the faces, the single write path, the 19 seed kinds (incl. the 5 agency traits) |
| Storage (canonical) | `storage/{types,memory,delivery-pump}`, `event-fold`, `event-signing`, `signing`, `cascade` | the adapter SPI, in-memory reference adapter, event log + fold, signing, liveness |

**The coupling is hub-and-spoke, not a mesh.** A small set of files are imported by 30–47 others and
everything else passes through them: `yi-accessors`, `ids`/`paths`, `substrate/types`, `holding-ops`,
`kinds/resolve`, `kinds/class-accessors`, `storage/types`, `auth`, and `handlers/{registry,helpers}`. Three
**enforcement seams** funnel all writes: `assertCan` (write authz), the `holding-ops` dispatchers (mutation
+ events + lifecycle), and `gate.evaluate` (invoke authz). The layering is acyclic; the few would-be cycles
are broken deliberately with lazy imports.

**What the original vision already got right in this shape:**

- **Type-is-a-thing.** Kinds are themselves `Yi` rows carrying `sys/kind` (`substrate-seed.ts:218`). The
  model describes itself in its own primitive — the property that makes Lisp and RDF low-resistance.
- **Anything can carry gated methods.** `port-dispatch` resolves ports by walking `row.kinds[]`
  face-agnostically (`runtime-yi/port-dispatch.ts:35`) — a holding can have ports just as a spirit can.
- **Capabilities as held things.** Holdings/grants exist and are reference-shaped.
- **One canonical row, audit events beside it.** Architecture C: the row is truth, the event log is a
  rebuildable audit projection written in the same transaction.

These are the strong spine. The friction is **not** here.

---

## 2. The diagnosis — what generates the friction

### 2.1 The headline: representation unified, meaning not

The substrate unified the *representation* (one row, one `kinds[]`, one `dimensions`) but never unified the
*meaning*. **Identity is still carried by hidden discriminators that sit beside `kinds[]` instead of in
it.** The worst single instance: a holding's nature — capability vs attestation vs edge — is inferred from
**which optional field happens to be present at construction**, not declared on its kind
(`yi-guards.ts:48-60`: `Token = Holding & {issuer: string}`, `Relationship = Holding & {referent: string}`;
`glossary.md:99` states it as doctrine). The kind — the thing meant to carry the contract — carries none of
it. You can declare a `FollowKind` with nothing edge-like about it and it becomes an edge only because a
caller passed `referent`.

The same disease recurs: `Kind` is a ~13-field canonical ideal plus ~45 leftover class-spec fields (the entire
pre-unification class taxonomy preserved as optional fields, `class.ts:377-454`); the word **"face" names
six unrelated things** and two foundational docs *contradict* on whether the row discriminator even exists
(`yi.md:26` "there is no `kind` column" vs `ports-and-faces.md:5` "the row carries a `kind` partition
discriminator"); **membership is encoded three ways at once** (`anchorMembers` array, `memberKindUid` edges,
`bears('<c>/member')` marker).

The cost is **measurable, not impressionistic**: `holdingSubFaceFromKinds(...)` is re-derived at ~84
occurrences across `core`/`server`/`std` — frequently *after* a query that already filtered by sub-face — each one a closure leak where the
type lost a fact the call site recomputes. Kit authors bypass the "one root" `rt.yi` to reach the per-face
storage repo at ~20 sites. The advertised frame is ~6 concepts; the one a developer must actually hold is
~24, roughly half of them pure carving artifacts. Scored against the rubric for low-resistance systems,
Bonfire lands ~**42/100** — strong where models are usually weak (a real generative spine, self-description)
and weak exactly where it *claims* to be strong (closure, uniform access, hidden seam). **A beautiful spine
with leaky joints.**

### 2.2 The deeper structure: one relationship primitive, split three ways

Three mechanisms that *feel* separate are the same idea in three costumes:

1. **`kinds[]`-membership** — "this row is-a X / bears marker M."
2. **Holding edges** — `holder → referent` in the `sys/holding` bucket.
3. **The message DAG** — `parents[]` reply/branch structure.

All three are *a typed, directed link between two addressable things* — **a tie**. They were split for three
real performance reasons (the kinds GIN; holding indexes; per-row overhead at message scale). The split is
implementation-justified, but **it leaked out of the implementation and into the concept**, and that leak is
the source of the recurring marker-vs-edge confusion, the "messages aren't Yis" special case, and the uid
sprawl (a membership relation materialized as a per-member marker, with per-community kinds as the visible
cost).

### 2.3 The inversion (why it feels wrong even though the spine is good)

The founder's stated intent was a **unified interface over plural representations** — minimal concepts, "one
session is a DAG, another a list, another a map," used easily without thinking. The code delivered the dual:
**uniform representation under a still-forked interface.** It forced one row, one table, one hardcoded
message DAG — so the *representational plurality that was explicitly wanted is absent* (any diversity gets
jammed into the `dimensions` JSON bag), while the *subject/object distinction that was meant to dissolve is
load-bearing* in storage (`face_class`, two face-shaped repo APIs, `holder`/`issuer`/`referent` columns). You are paying the
full cost of representational uniformity and getting none of the interface uniformity you wanted. **That
inversion is the constant tension.**

### 2.4 Why it feels unchangeable

Core is ~30k LOC; you cannot hold it whole. But the real reason it resists change is that **there is no
frozen target to refactor toward.** The two-concept model lives as an intuition, not a written spec the code
can be measured against, so every local cleanup is ambiguous (collapse `holder` and `referent` into *what*?),
subtraction feels risky, accretion wins, the thing grows, it feels more unchangeable. Producing the yardstick
([`the-frame.md`](../01-frame.md)) is the move that breaks the loop.

---

## 3. The original intent, restated

In the founder's words, sharpened into the actor model he reached for:

> A thing can be a **subject** or an **object**, a **bearer** or a **capability**, a **container**, a
> **type**, an **agent**, a **message target**, or a **resource** — *depending on its traits and relations,
> not on a permanent category.* Having something and being something are the same substance seen from two
> ends of a relation. Even the **type** of a thing is a thing. The unification's purpose is a single
> **mental** frame — minimal concepts a developer holds whole — over representations that need not share a
> data structure.

Two corollaries (both already constitutional law in `encoded-implementation.md`):

- **(a) The concept need not mirror the implementation 1:1** — the substrate may diverge for performance
  *provided the divergence is hidden below the conceptual surface and reconstructable from the canonical
  `Yi`.* A leak is a defect; a hidden divergence is not.
- **(b) The conceptual framework itself may be flawed** — we are permitted to question the concepts, not
  just the engineering.

The operative definition of success is cognitive: **mental resistance = the number of independent things you
must hold in working memory to predict the system's behavior at a point.** This is *not* "number of
primitives" — a frame with three primitives that interact through a dozen special cases has higher resistance
than five primitives that compose with zero special cases. The levers are **closure, no-special-cases, and
uniform access** — never noun-count. Collapsing into an *overloaded* primitive makes resistance worse, not
better.

---

## 4. Assessment of the two inputs

### 4.1 `unified-mental-frame.md` (the exploration) — the stronger artifact

Verified against code, deep, and self-reconciling. We **adopt its diagnosis wholesale** (§2 above is its
diagnosis) and its **central principle**: the author declares relations *by intent*; the substrate owns
representation; every representation is a rebuildable projection of one `Yi`. Its single best argument is
that this seam is **already constitutional law and already implemented correctly three times** (CQRS
row/event; single-writer children + aggregate-at-read; faces-as-projections-over-one-row) — which is what
makes the pivot a *finish*, not a rewrite. Most of the win is **subtraction** (~24 concepts → ~12).

We **refine it on three points** (carried into the decisions below):

- It calls the **router** "small." It is not — a representation planner that *re-materializes as data grows
  with zero author changes*, under the seq lock and the auth floor, is a query optimizer. → Build a
  **deploy-time compiler**, not a runtime planner. (Decision D3.)
- It presents Thread 1 (subtraction) and Thread 2 (the router) as parallel and **leads its PoC with the
  router**. → **Sequence the router-independent subtractions first**; they need no new
  machinery and shrink the codebase fastest — though they are net-subtractive *migration* (many call sites
  + snapshots, landed atomically with tests), not literal deletion. (Decision D4.)
- It nominates the **Tie-duality** frame (ENTITY + TIE⇄MOMENT + PORT + GATE⇄TRIGGER) as the *taught* North
  Star. That frame is subtly **event-sourced** ("a tie is the fold of its moments") while the substrate is
  **row-canonical** — so it is the wrong thing to put in a developer's hands daily (maximal concept↔substrate
  distance at the moment they cross the seam). → **Teach the trait/role frame** (closer to the substrate);
  keep Tie-duality as the *rationale* that explains why the unification holds. (Decision D1.)

### 4.2 The peer-agent critique — one keeper, one reject

**Keep — "everything *can* be active, not everything *is* active."** Its best contribution, and the
exploration doc does not state it as doctrine. Make **addressability universal, agency a trait.** If every
`Yi` is an actor with a mailbox by default, cognitive load *increases* (every read might be behavioral,
every gate surface expands) and the "minimal understanding" goal is undercut. Passivity is the default;
activeness is composed. (Decision D2.) Its North-Star sentence is also the better daily one-liner: *"`Yi` is
not a superclass for old entities; it is the one addressable bearer of traits, relations, capabilities, and
behavior."*

**Reject — the compatibility-migration strategy.** It advises "migrate behind compatibility," "keep `face`
internally for compatibility," "delete compatibility vocabulary only after public-surface tests, SDK docs,
and server RPC all agree." That is correct for a shipped system with external users; it is **wrong here** and
**contradicts a standing project law**: no alias layers, no deprecation cycles, no migration cushions — each
phase lands clean and breaks forward (Bonfire is pre-production; elegance over legacy). Following it would
build the exact accreted compat scaffolding that *created* the tension. We subtract and break forward.
(Decision D5.)

### 4.3 The trap both inputs share

Renaming `face → trait` is **not** the win. Moving the ~45 `Kind` fields into ~45 traits relocates the zoo,
it does not dissolve it. The win materializes only if **traits compose with zero special cases.** The
acceptance test for the subtraction is therefore not "did faces become traits" but **"do `capability` +
`container` + `agent` compose on one row with no special-case branch?"** That closure discipline is Decision
D6.

---

## 5. The decisions (frozen)

| # | Decision | Rationale |
|---|---|---|
| **D1** | **The taught frame is the trait/role model**; Tie-duality is the *rationale*, not the daily model. | Trait/role sits closest to the substrate (kinds = traits, ports = messageable, holdings = held ties), so the model does not change shape when an author drops down the escape ladder. Lowest seam-crossing cost. |
| **D2** | **Addressability is universal; agency is a trait.** Every `Yi` is addressable; *some* receive ports, *some* initiate, *some* hold capabilities. Not "everything is active." | Universal agency increases what must be reasoned about and expands every gate surface. Passive-by-default is lower-resistance and safer. |
| **D3** | **The seam is law; realize it as a deploy-time *compiler*, not a runtime *planner*.** The author declares a relation + access hint; the substrate compiles it to a *fixed* representation at deploy time. Pinning is the default; the live cost-based re-materializer is deferred indefinitely (YAGNI until a real hot, churny relation exists). | Gets the entire mental-frame win — kit code never names marker-vs-edge — without betting on an online migration engine under live data + seq lock + auth floor. De-risks "the one additive bet." |
| **D4** | **Sequence: keystone, then subtraction, then seam.** Phase 0 = the face-shaped-contract collapse (D11, the keystone — writer/index/API/lifecycle + the agency-generic work, *not* a table merge). Phase 1 = the router-independent cuts (dissolve `Kind`'s ~45 stored class-spec fields into feature-traits, keeping its ~13 canonical fields; fix the field-presence mint surface; declare holding sub-faces as composed kinds; retire the six meanings of `face`; demote `Grant` to a recipe; unify port dispatch per D12; pick one port model). Phase 2 = the membership/stream seam (the compiler). | Phase 1 is net-subtractive (drops most of ~24 → ~12) and needs no new machinery — but it is **migration, not literal deletion**: it touches many call sites across core/server/SDK + public-surface snapshots and must land atomically with tests. It still shrinks the codebase that feels "too big." Only membership (and streams) is coupled to the seam, because collapsing membership to one edge kind *without* the compiler would cost the cheap `bears(marker)` read on hot paths. |
| **D5** | **No backwards-compat — but each phase atomic.** No alias layers, no deprecation cycles, no "keep `face` for compatibility." Each phase lands clean and breaks forward **atomically across core/server/SDK/docs/tests/public-surface snapshots** — break-forward is one coherent world per phase, never old+new names coexisting or half a bridge left to guess. | Standing project law; pre-production; the compat scaffolding is itself the tension. Overrides the peer-agent's "migrate behind compatibility" advice, but adopts its atomicity condition. |
| **D6** | **Closure is the acceptance test.** Traits must be orthogonal and compose with as few special cases as possible. The first metric is the ~84 `holdingSubFaceFromKinds` re-derivations (across `core`/`server`/`std`) collapsing to `kinds.includes()`. **Honest caveat (from the cases):** traits carrying *combination invariants* (e.g. `fungible`+`unique` forbidden) become a *trait-with-validator*, not zero-special-case — so the real metric is **the cross-trait combination matrix shrinking from N rules to M**, stated when you cut. | Guards against relocating the zoo into a feature-combination matrix. Closure is the property that lowers resistance; not every field reaches perfect closure, and the doc should not pretend otherwise. |
| **D7** | **Meaning lives in markers, in the open.** What a `Yi` *is* = the traits (kinds) it composes — never which optional field was set at construction, never a parallel `face`/`face_class`/`Kind.face` discriminator. `issuer`/`referent` presence becomes *validated against the declaration*, not *the definition of identity* — at the **write** surface (the `manifest` overloads), not only the read guards. | Restores closure and kills the field-presence disease at its root. The cases showed the root is the mint API, not just `yi-guards`. |
| **D8** | **One encoding per membership *relation* the auth floor consults.** **[SHARPENED — ratified 2026-06-24.]** The earlier wording ("membership is encoded three ways at once" — `anchorMembers` array ∪ `memberKindUid` edges ∪ a `bears('<c>/member')` marker — "make it **one**") was imprecise: the build proved these are **two genuinely distinct relations**, not three encodings of one — **session-participation** (`anchorMembers` ∪ `memberKindUid` — the roster of who is *in* a thread) and **community-standing** (`bears('<c>/member')` — who is *a member of* a community). The decision is therefore **one encoding per membership relation**; the auth floor consults *that* representation (marker for hot reads, edge for churny writes), never a parallel kit convention — but the **two relations are NOT collapsed into one** (a future engineer must not fuse who-is-in-a-thread with who-is-a-community-member). The closed leak is a kernel floor (`auth.ts`) and a kit marker convention disagreeing *within one relation*. | The Phase-2 spine, and the reason the seam is sequenced before policy. Per-relation encoding is what makes communities composable (G4). This is the decision `03-architecture.md §9` refers to as "D8". The sharpening prevents a wrong future collapse of two distinct relations (Law 4's "one connection" caveat made concrete). |
| **D9** | **The stream tier is a named canonical center — not a Yi, not a representation.** Messages live in their own dense-ordered, per-session-partitioned `stream` table — a *canonical* store with a same-transaction audit event (Law 8) — carrying a `session` FK + a dense `seq` that **no tie expresses**. Admit it as a **named first-class tier** (beside Signals/Projections, `01-frame.md §16b`), *not* as "an invisible `stream` representation the compiler picks" (a canonical store is not a representation *of* anything). | Resolves the Law-8-vs-§16 contradiction and the over-claim that `parentUid` is the *only* exception to "no hidden center." Honest count: the **named** (never hidden) non-Yi centers are the column-promoted relations (`parentUid`, `originKindUid`) **and** the stream tier. "No *hidden* center" stays true; "one exception" undercounted. |
| **D10** | **The agency/composition vocabulary is a defined seed-trait set, created before it is consumed.** `identity`, `agent`, `messageable`, `streamed`, `membered` are **first-class seed traits** (`sys/*` kinds), each with a one-line contract (backing state + what it enables); `container` already exists as a holding feature. G1 and the de-spirit work compose these, so they must be **seeded in Phase 0 before** the tasks that consume them (`P0-AG0`, ahead of AG3/AG5/AG6 and FC1's `membered`+`streamed` test). | Closes the same gap class as the `sys/edge` inversion: the plan consumed `agent`/`messageable`/`streamed`/`membered` that no task created. "Agency is a trait" (D2) needs the traits to exist *with contracts*, not just names. |
| **D11** | **The keystone is the *face-shaped contract*, not a table merge.** Storage is **already** one `yi` table (PG migration 001; one aliased in-memory map; `Spirit = Holding = Yi`) — **both** review sessions verified this independently. So Phase 0 is **not** a live-data migration. The real keystone: establish **one writer / index / lifecycle / public-API contract** — retire the face guard (`runtime-yi/kind-ops.ts:270`), dissolve the per-face write routing + field-presence mint, key replay/fold off `kinds[]` (the fold reads `kinds[]` as the source of truth for the replayed face), retire the face-shaped SDK/RPC surface — so `sys/spirit`/`sys/holding`/`sys/session` become ordinary traits *once their indexes, invariants, migration path, and API semantics are proven*. Identity-class traits are **irremovable** (a keypair that signed events can't be orphaned). _Status: the code went further than this decision required — `face_class` is FULLY REMOVED from the durable fold (`FoldedYi` has no `face_class` field; face is reconstructed from `kinds[]` via `faceFromKinds`, `event-fold.ts:86`), not retained even as a fallback._ | "Merge two repos" mis-locates the work (risks deleting useful abstractions / planning a nonexistent migration). The coupling is in writer/index/API/lifecycle, not the bytes. **And the motivating case is real, not retreated:** "item carries an agent" = the item itself bears `identity`+`agent`+ports and signs its *own* actions while the holder writes its data — two authorities the substrate **already** separates (custody in `auth.ts`; signing-witness in `event-signing.ts` — a message already self-witnesses via `msg.sender`). There was never one custody scalar to fuse (a prior re-spec to "a tie to a separate agent-Yi" was a conflation, reverted). Phase 0's real agency work is to **de-spirit reactivity** (`triggers`/`lifecycle` dispatch off `storage.spirits.get`) so a held `messageable` row can receive/emit moments. |
| **D12** | **Ports flow through ties — both readings valid.** A Yi's invokable ports = those projected by its *is-a* ties (borne traits, always) ∪ its *holds*-ties to capabilities that declare `confers` (opt-in). One dispatch, one `discoverPorts`. | "Address the item" and "the holder transparently gains the item's ports" are the **same** primitive (a tie projecting ports), differing only in tie-type. Supporting both collapses today's two dispatch surfaces (kind-ports + `<ns>:<name>` item-methods) instead of choosing between them. |
| **D13** | **Admit collective capability.** A capability tie may be held by a *group*; its members exercise it transitively via a `caller-via-group` gate leaf — attenuated by scope, eagerly revocable, **without** joining the target. Sequenced **last** (after the gate cliffs are fixed), implemented as an **index intersection** (`byReferent(A) ∩ byHolder(M)`), with **both legs liveness-checked** (not just `burnedAt`). | "Community B lends its members restricted access to community A" is a real, intended shape. It is the one *second-order* gate, bounded to one hop. The naive "for each of M's groups…" reading is a fan-out cliff; the index-intersection is O(caps-on-A + M's-memberships). |
| **D14** | **The projection pillar (keep — agreed).** The seam's most important representation is one *tie-indexed, rebuildable, columnar projection* — simultaneously the author's declared relation/aggregate, storage's ECS-*archetype* fast path, delivery's interest/recipient set (area-of-interest fan-out), and the cross-row read engine (counts / feeds / inboxes / search / inventory aggregates). | Four criticisms — JSON-bag storage perf, broadcast fan-out, the single-anchor read doctrine, missing aggregation — are **one** missing *projection family* — one mechanism (a tie-indexed, rebuildable, columnar projection), instantiated once per declared relation/aggregate, **not** one global object. Build the mechanism once. This, not a table merge, is the engineering spine of the seam. |
| **D15** | **Reactivity is a triad + the gate is a policy engine (keep — agreed).** Add a **pre-commit inline-trigger** lane (moderation / anti-abuse veto before a moment is visible) beside the post-commit trigger; make the gate **resource-scoped** with **negative rights + precedence** (deny-overrides-allow, channel overrides), explainable, and **compiled-and-cached** (Discord-style materialized permission), not a predicate tree walked per invoke. | "Authz is Port + Gate" is right, but the gate is too coarse for real product governance ("a membership relation with a label"); **both** review sessions flagged resource-scope + negative rights + precedence as P1. Stays Yi-shaped (roles/bans/overrides are ties with policy). |
| **D16** | **Mint authority lives in the open — retire `RuntimeWriteOpts.enforce` (founder's call, 2026-06-21).** **[LANDED — full closure: `enforce`+`shouldEnforce` DELETED; named `SYSTEM_CALLER`/`provides[]` for boot/re-entrancy/handler mints. The trait-derived gate described next is now REACHED (RR7): agency-as-trait is complete — `sys/agent` is a seeded trait stamped on every agent-birth path (`sys/bot`.composes; `digital`/`hero`.kinds), so the agent-part kinds carry `add: all(any(self, ancestor()), targetHas('sys/agent'))` — the structural self-equip arm keeps the G6 closure AND the trait arm requires the HOLDER to bear `sys/agent`. Authority flows from the borne trait, in the open. Residual (MA §7 part 2 "unify the mint surfaces") RESOLVED as a category error — no build: the `face:'holding'` premise is stale (face gone, RR1) and `resolveAuthorityModel` (`runtime-yi/gates.ts:118`) already routes each kind to exactly one authority (license / `can_mint` / add gate partition by kind class); the non-gate layers are separate authorities, not duplicates. See `04-execution-plan.md §9 RR7`.]** The FC2 Option-1 `enforce:false` flag (commit `306f5e54`) lets an in-process caller *assert* its own privilege to skip the mint license + `assertCan('holding.mint')` gate. Replace it with two **readable** layers, both already in the substrate: (1) the imperative license layer (`assertLicenseOrBuiltin` — held `sys/license` token or a readable bypass: builtin-kind, sys-root, sys-admin, class-owner-ancestor, `SYSTEM_CALLER`); (2) the declarative `can_mint` rule hook fired in `mintHolding` (`holding-ops.ts:701`, flag-independent, already a floor for membership kinds). Agent self-equip becomes a `can_mint` recipe: **allow iff `isAncestorOrSelf(caller, holder)` AND the HOLDER bears `sys/agent`** (read off the holder via `target-has-kind`, never the caller — that would be privilege-escalation). `enforce:false` survives only as a renamed substrate-private `internalContinuation` for the two non-retirable classes (license/sys-admin **bootstrap** — circular root; already-authorized **re-entrancy** — transfer recipient-mint, fork inner deploy, auto-title). **Tracked, not built now (Phase-3 Track MA);** Option 1 stays until then. | G2/G5/Law 5 — authority you can `explain()` beats authority you *assert*. Verified economy: for `sys/mind|context|persona` (∈ `BUILTIN_KIND_PATHS`) the flag is **already redundant** with the builtin bypass, so the equip retirement is a *strict reduction* on existing machinery (no new primitive — a `can_mint` handler + readable callers). Honest accounting: net-**more** mechanism, but G5-legible and strictly **tighter** than the flag (blast radius: "any in-process caller, any holder, any kind" → "an ancestor of the agent, that agent, those three kinds"). The `sys/agent` acquisition gate is already `add: ANCESTOR_OF_TARGET` (`substrate-seed.ts:727`), so the recipe's floor holds. Bounded Option-1 debt, **not** a frame violation. |
| **— deferred** | **GDPR-delete / E2E and federation/firehose: parked (founder's call, 2026-06-19).** Not now. Recorded only so a future effort knows they are unsolved — erasure-vs-signed-log and the cross-host tie graph are **not** bolt-on-able after the signing substrate solidifies, and are **not** "solved below the seam." | Out of scope for the current pivot; revisit if/when federation becomes a goal. |

---

### Engineering principles (the discipline for the refactor)

These govern *how* every phase is executed — the rules that keep the unification from becoming a rewrite or
a regression:

1. **Break forward, atomically.** No alias layers, no deprecation cycles, no compat cushions. Each phase
   lands as **one coherent world** across core/server/SDK/docs/tests/public-surface snapshots — never
   old+new names coexisting, never half a bridge left to guess (Law 9).
2. **Subtract before you add; keystone before polish.** Prefer deletion. The only genuinely new machinery in
   the whole pivot is the compiler, built last; the keystone collapse and the Kind dissolution come first
   (Law 10).
3. **Migration, not `rm`.** "Net-subtractive" still touches many call sites and deployed data. Inventory and
   classify every field/site, write the migration + backfill test, *then* delete. Nothing disappears by
   assertion.
4. **Canonical, or rebuildable with a tested path.** No performance representation becomes the sole home of
   truth; every derived structure declares its source, its audit event, and a rebuild test (Law 8).
5. **Storage stays free to optimize below the seam.** One ontology ≠ generic slow storage. Preserve the
   index-backed hot paths (kinds GIN, holder/referent, child-aggregate, per-session stream); the compiler's
   job is to keep the author on a fast path without naming it. A representation choice that regresses a hot
   path is a bug, not a simplification.
6. **Verify against authoritative `tsc`/test, not stale IDE diagnostics.** (A recurring trap in this repo.)
7. **Correctness debt is fixed on its own, not folded into the pivot.** The bugs the cases surfaced (§9) are
   landed as independent, tested fixes — several are *subsumed* by the frame's single-tie model, but they
   are not blocked on it.

---

## 5b. Build status — frame claim vs. code today

The frame describes the *model*; this table is the one place that tracks how far the code has walked toward
it. Inline `(Destination)` notes in `the-frame.md` defer here, so the frame itself reads as the model.

- **Current fact (true in code today):** one `yi` table (spirit/holding/item/… are one row, `kinds[]`-typed);
  `kinds[]` carries meaning; ports/gates resolve live-by-reference at dispatch; gated dispatch with no
  backdoor; CQRS row + same-transaction audit event; single-writer children + aggregate-at-read; presence as
  a Redis *signal* tier; the index-backed hot paths.
- **Violation (code contradicts the frame — remaining Phase-1 targets):** the per-face **WRITE repos**
  (`storage.spirits` / `storage.unifiedHoldings` survive as the write path; `rt.storage.yi.*` kit-reachability
  ≈79 non-test sites — RR2 honest tail); lifecycle dispatch (`lifecycle.ts:41,151`, `AG4`) + the trigger
  ctx-target re-load (`triggers.ts:507`, `AG5`) still spirit-shaped; the ~40 stored Kind class-spec fields
  (RR6 increment — gated on KI3 homes + fork-propagation); membership encoded 3 ways (the G4 residual, deferred
  to the seam compiler). **RESOLVED by the residual-register program (no longer violations):** the face guard
  (`FC1` — the `FACE_KINDS` refusal is DELETED from `kind-ops.ts`) + per-face **write routing** (`FC2`/RR1 —
  `SpawnInput.face` + `switch(input.face)` gone; `{ kind }` is the sole authoring form, write shape derived
  from `composes`); field-presence mint (RR1/MD3 — the holding sub-face is a declared `kinds[]` marker, read via
  `holdingSubFaceLabel`, no longer re-derived from `issuer`/`referent` presence); the two port-dispatch surfaces
  (RR-PD/D12 — the item-method/`grants`-splice second surface is GONE; `invokeItemMethod` has zero source hits;
  one `resolvePortOnRow` tie-walk projects is-a ∪ spec ∪ live-holds `confers`); `rt.kinds.*` separate namespace
  (RR5 — folded to `rt.yi.manifest({ kind: 'sys/kind' })`; reads `@internal`); the auth write-authz switch
  (RR3 — folded into one gate ADT); session-participation membership (RR4 — seam-compiled via `mintFloor`).
  Also generic since Phase 0: witness resolution (`AG2`) + the trigger *entry* (`AG3`) → `storage.yi.get`; the
  fold reads `kinds[]` as the source of truth for the replayed face (`FC4`). **Went further than logged:**
  `face_class` is FULLY REMOVED from the durable fold — `FoldedYi` has no `face_class` field, and face is
  reconstructed from `kinds[]` via `faceFromKinds` (`event-fold.ts:86`). Law 9 is honored more fully than
  originally recorded: the field is not retained even as a fallback. The fold reads `kinds[]` only, which new
  events carry; no backfill/replay fixtures (they would violate the no-backwards-compat law).
- **Destination (designed, partly built):** agency generic (any Yi bearing `identity` witnesses/reacts/acts)
  — **LANDED** (AG2/AG3 + AG3-residual + AG4 lifecycle + AG5 dispatch; G1 closed, Phase 0 complete). `confers`
  ports-through-ties — **LANDED** (RR-PD/D12: `resolvePortOnRow` walks is-a ∪ spec ∪ live-holds `confers`; the
  legacy second surface deleted). Still pending: resource-scoped policy + negative rights + precedence; inline
  pre-commit trigger lane; collective capability (`caller-via-group`); `historied`/`versioned` trait; edge
  expiry/audit; one membership notion the auth floor consults.
- **D16 LANDED — `RuntimeWriteOpts.enforce` is DELETED (full closure, retired early not parked):** the flag and
  `shouldEnforce` are gone; the hard cases (boot, op re-entrancy, handler mints) use the named `SYSTEM_CALLER`
  sentinel / `provides[]`. **The agent-part gate is now TRAIT-DERIVED (RR7 MET — the original D16 design
  reached):** the agent-part kinds (`sys/mind`/`turn`/`context`/`persona`) declare `add: all(any(self,
  ancestor()), targetHas('sys/agent'))` — the structural arm keeps the G6 closure (a non-ancestor peer still
  denied), the trait arm requires the holder to bear `sys/agent`. Agent-ness is no longer fragmented: `sys/agent`
  is a seeded trait stamped on every agent-birth path (`sys/bot`.composes; `digital`/`hero`.kinds), so the gate
  authority flows from the borne trait, in the open. **MA §7 *part 2* ("unify ALL holding-mint authority into
  one gate") is RESOLVED as a category error — no code to build (`c-deep`, RR7 residual).** Its premise (a
  `face:'holding'` equip path with its own license-only authority redundant with `gates.add`) is stale: the face
  is gone (RR1), and the `resolveAuthorityModel` switch (`runtime-yi/gates.ts:118`) already routes each kind
  to **exactly one** authority — license, `can_mint`, or the add gate **partition by kind class**, they never
  coexist on one kind. The three non-gate layers (deploy-time license, the per-relation `can_mint` tx floor that
  re-fires on the 23505 unique-edge race, the `assertCan` subtree floor) are **separate authority layers, not
  duplicates of `gates.add`**; folding them in = re-homing the license subsystem into the gate ADT = D15
  policy-engine work, not a discrete MA slice. See D16 below + `04-execution-plan.md §9 RR7`.
- **Future mechanism (the new machinery — last, after subtraction):** the deploy-time seam compiler
  (marker/edge/table/stream); the projection pillar (tie-indexed columnar projection = storage fast path + AoI
  fan-out + cross-row reads).
- **Deliberately deferred (not now):** GDPR-delete / E2E; federation / firehose / labelers / app-views.

---

## 6. What stays below the seam (kept, not deleted)

The pivot is **not** a flattening of the substrate. The following stay — they simply leave the *mental frame*
and live below the seam, invisible to the author for the 90% case:

- **The marker / edge / special-table representation split.** Real performance; the seam *hides* it, the
  router/compiler *picks* it. The mental frame has one relation; the substrate keeps three materializations.
- **The per-community member kinds (the uid sprawl).** Generated *internally* by the compiler as the marker
  materialization of a membership relation. They leave the authoring surface, stay in storage.
- **The `stream` table and its dense per-session seq + DAG.** The high-volume materialization of a
  `stream` relation, chosen by declared volume. The "messages aren't Yis" exception becomes a representation
  the substrate picks, not a rule the author memorizes.
- **The stranded SQL gate-prefilter** (`gate-sql-compiler.ts`, deleted in Phase 0 as wired-to-nothing —
  see §9, P0-CD3). It was the right idea at the wrong layer; the compiler reintroduces it as an invisible
  read-projection it switches on.
- **Specialized SQL indexes.** Unified ontology ≠ generic slow storage. Public concepts stay unified;
  storage stays free to optimize common traits.
- **CQRS row/event.** Row canonical, events derived audit. Kept; framed in docs as *derived audit*, not a
  second source of truth.

The deepest guarantee comes free: 间理's "no bypass for performance" law (`encoded-implementation.md:11,
83-85`) *already requires* every materialization to be a rebuildable projection that records its audit event
in the same transaction. The seam is not a new risk surface — it is the enforcement mechanism for a rule the
codebase already lives by.

---

## 7. Open forks — still the founder's call

1. **The taught frame.** D1 commits to trait/role as the daily model with Tie-duality as rationale. If you
   want the *radical* Tie-duality framing to be the literal taught model instead, that is a conscious
   trade (more explanatory power, higher seam-crossing cost). *Recommendation already encoded as D1.*
2. **The compiler's ceiling.** D3 caps the seam at a deploy-time compiler. The open question is whether the
   runtime cost-based **planner** (auto re-materialize as data grows) is ever built, or whether the compiler
   + manual `represent:` pin is the permanent ceiling. *Recommendation: cap at compiler until a real
   workload proves the planner's value.*

Neither fork blocks Phase 1. Both can be decided after the subtraction lands.

---

## 8. The sequence of moves

1. **Freeze the frame.** [`the-frame.md`](../01-frame.md) is the canonical concept doc and the
   yardstick. It supersedes the contradictory `yi.md` / `ports-and-faces.md` pair. *(This pivot's first
   deliverable — done alongside this file.)*
2. **Correctness debt first (before the grand refactor).** Bounded `gate.ts` caller-holds (was a full-table
   holdings scan per gated invoke; fixed by P0-CD1) + closed the `caller-holds` liveness gap (P0-CD2),
   retired the dead SQL prefilter (P0-CD3), and gate `rt.yi.where` or rename it to scream "unfiltered."
   These are independent, tested fixes (engineering principle 7) **and prerequisites for D12/D13**, which
   route the hottest paths through exactly these primitives. (Full list: §9 correctness debt.)
3. **Phase 0 — the keystone: one writer/index/API/lifecycle contract + agency made generic (Decision D11).**
   *Not* a table merge — storage is already one `yi` table (verified both sessions). Two halves:

   **(A) The contract work.** Retire the face guard (`runtime-yi/kind-ops.ts:270`), dissolve the per-face
   **write routing** + field-presence mint, key **replay/fold** off `kinds[]` (landed: the fold reads `kinds[]`
   as the source of truth for the replayed face; `face_class` is FULLY REMOVED from the durable fold — `FoldedYi`
   has no `face_class` field and face is reconstructed from `kinds[]` via `faceFromKinds` (`event-fold.ts:86`)),
   retire the
   face-shaped **SDK/RPC** surface — so `sys/spirit`/`sys/holding`/`sys/session` become ordinary traits *once
   their indexes, invariants, migration path, and API semantics are proven*.

   **(B) The agency work — the sharper half.** "The item itself acts" must become *literally* true, not just
   stated. The substrate already proves the custody/signing *separation*. Witness resolution and the trigger
   entry-point are now generic (landed); lifecycle dispatch and the trigger ctx-target re-load still
   short-circuit on the spirit repo. Finish making it generic:
   1. **`identity` becomes a trait any Yi can bear** — irremovable once it has witnessed events (landed: `sys/identity` seed).
   2. **Witness resolution goes generic** (landed) — `resolveWitness` (`event-signing.ts:197`) resolves via
      `storage.yi.get` (`:204`); the only `spiritByPath` calls left are the sanctioned `sys/ROOT` resolution.
   3. **Trigger/lifecycle dispatch targets any Yi** with the reactive trait — the trigger *entry* already
      resolves via `storage.yi.get` (`triggers.ts:402`); the remaining work is `lifecycle.ts:41,151`
      (`storage.spirits.has`) and the trigger ctx-target re-load (`triggers.ts:507`).
   4. **Message/port dispatch is trait-based**, not spirit/session-face based.
   5. **Custody, signing, gate-authorization, and holder-transfer stay four separate axes** — none fused.
   6. **"Item tied to a separate agent" stays a delegation pattern**, never the definition of an active item.

   **Acceptance milestone (no rhetorical victory):** a held item bearing `identity`+`agent`+ports *signs its
   own action-event, receives a trigger, and fires a gated port — with tests* — while its stats are still
   written under the holder's custody. *(A type-system + write-path + projection refactor, landed atomically,
   suite green — not a live-data migration; budget it there.)*
4. **Phase 1 — the subtractions**, in leverage order (each an atomic, tested migration — not `rm`):
   - **Dissolve `Kind`'s class-spec layer.** Keep the ~13 canonical fields (`id, rowSchema, gates, ports,
     composes, defaults, lifecycle, triggers, invariants, evolutionPolicy, transientVia, examples, frozen`);
     move the ~45 stored class-spec fields to composable feature-traits. **Inventory & classify every field
     with a migration test before deleting any.**
   - **Fix the mint surface (Law 2 at the write side).** Mint becomes `manifest({ kind, init })` only; delete
     the field-presence `manifest` overloads (`runtime-yi/types.ts:778`) and the `yi-guards` field-presence
     projections. Without this, deleting the read-guards just relocates the inference one layer down.
   - **Declare holding sub-faces** as composed kinds (`sys/capability` / `sys/attestation` / `sys/edge`);
     `holdingSubFaceFromKinds` collapses to `kinds.includes()`.
   - **Retire "face"**: derive from `kinds[]`; rename the `事面/间面/机面` registers to "register"; fix the
     stale `ports-and-faces.md`.
   - **Demote `Grant`** to a recipe (a Token kind + the `hasGrant` gate leaf).
   - **Unify port dispatch (Decision D12).** One tie-walk — borne traits *and* held capabilities that declare
     `confers` — collapsing the `<ns>:<name>` item-method surface + the `grants` splice into the kind-ports
     surface, reported through one `discoverPorts`.
   - **Pick one port model**: re-home the ~8 live `DimensionRegistry.contributesToFace` contributions (called
     by `discoverPorts`) onto `Kind.ports`, then remove it.
   - **Fix discover/present-dimension cache invalidation** on the unified `deployKind` path (a redeploy
     leaves them stale today — Law 8 bounded-staleness).
   - **Make "a kind is a Yi" true ergonomically (types-as-governed-Yi).** Fold `rt.kinds.*` into
     `rt.yi.manifest({ kind: 'sys/kind' })` (one authoring namespace), make `defineKind` produce a manifest
     rather than a config object, and address kinds like any Yi (uid, not a bespoke path-ref resolver). The
     face-guard's refusal of `addKind('sys/kind')` lifts with the keystone. *(The one clean remaining
     contradiction of the frame's "a kind is a Yi" — storage-true today, ergonomically false.)*
5. **Phase 2 — the membership PoC through the compiler** (the projection pillar, D14, is its spine). Declare `membership(...)` with access hints; route
   community-standing to a marker and channels to an edge, **compiling to the representation the auth floor
   (`isSessionMember`) itself consults** so there is one membership notion, not a kernel edge-check racing a
   kit marker convention. **Success criterion:** a kit author writes `join` / `isMember` / `members` with no
   knowledge of marker vs edge, performance matches today, the `referent === session.uid` floor (`auth.ts:381`)
   is intact, and `grep` finds zero `holdingSubFaceFromKinds` / `addKind('<c>/member')` / `rt.storage.spirits.get`
   in the kit.
6. **Then** build the **projection pillar (D14)** — the tie-indexed rebuildable columnar projection that
   serves membership reads, interest-managed (AoI) delivery, and cross-row aggregates from one projection family (one mechanism, one instance per relation) — add
   the **policy layer + inline-trigger triad (D15)**, admit **collective capability (D13)** as an
   index-intersection with liveness-checked legs, generalize the compiler to the `stream` relation and
   collections, recut the `community.md` / `session.md` docs onto the frame, and only *then* re-open Fork 2
   (planner vs compiler-ceiling).

Each move lands clean (full suite + typecheck green) and breaks forward — no compat layer between phases.

---

## 9. Appendix — evidence index & corrections

**Verified this round:**

- **The gate SQL compiler WAS dead code in production — now deleted (Phase 0, P0-CD3).** `gate-sql-compiler.ts`
  was consumed only by `gate-sql-partial.ts`, which was imported by nothing but its own tests; both files and
  their tests are gone (`grep -rl gate-sql packages/core/src` → none). The exploration doc's "stranded
  read-optimization" claim was accurate. *Correction to an earlier kernel synthesis that asserted `where()`
  prefilters through it — that was unverified and wrong.*
- **`contributesToFace` is LIVE, not "mostly dead."** Called by `rt.yi.discoverPorts`
  (`dimensions/registry.ts:120`), populated by ~8 seed dimensions (`dimensions/seed.ts`). Removing it is
  *migration* (re-home onto `Kind.ports`), not deletion. *Corrects the exploration doc's Flaw F and an earlier
  claim here.*
- **`Kind`'s canonical authored set is ~13 fields, not 8.** It also carries `invariants`, `evolutionPolicy`,
  `transientVia`, `examples`, `frozen` (`kinds/class.ts:270-358`). The pivot dissolves the ~45 *stored
  class-spec* fields, not these. *Corrects an "8-field" overstatement in both docs.*
- **The runtime read verb is `rt.yi.read`, not `rt.yi.get`** (`runtime-yi/types.ts:653`); `.yi.get` is the
  storage repo only. *Fixed in `the-frame.md`.*
- *Source of these four corrections: the peer review in `frame-pivot-evaluation.md` +
  `frame-pivot-claim-audit.md` (2026-06-18), verified against code before applying.*

**Correctness debt found during case analysis (2026-06-18) — fix independent of the pivot.** Seven agents
probing ten real scenarios surfaced these; several are *subsumed* by the frame's single-tie model but should
not wait on it (engineering principle 7):

- **`gate.ts` full-table holdings scan per gated invoke — FIXED (P0-CD1, as of 178fcd97).** The `caller-holds`
  leaf used to fetch the caller's holdings via the indexed `byHolder` then *unconditionally* `byFace('holding')`
  scan every holding row in the instance. Was the worst perf cliff; bounded to `unifiedHoldings.byHolder(ctx.caller)`
  with no full `byFace('holding')` scan (`gate.ts:1049-1050`), still catching `kinds[]`-riding classes.
- **`caller-holds` skipped `isHoldingLive` — FIXED (P0-CD2, as of 178fcd97).** A cascade-dead membership (bound
  to a burned item, orphaned holder) used to pass the authority gate — "dead for reads, live for authz."
  Survivors are now filtered through `isHoldingLive` (`gate.ts:1057-1063`). (The single-tie model with one
  read path closes this by construction.)
- **`anchorMembers` un-revocable static roster — ✅ RESOLVED (S6 / D2 Option B).** The debt was: a
  burned/suspended founder kept thread access because the array was never reconciled against cascade liveness
  (unlike `caller-holds`, `isHoldingLive`-checked via P0-CD2). **As built:** `anchorMembers` is DELETED entirely
  ([`08-ideal-architecture.md`](08-ideal-architecture.md) S6). Membership is now uniform **revocable cells** minted
  via the one `isMemberOf` edge path (`anchorMembers` + `isLiveAnchorMember` + `ANCHOR_ONLY_RELATION` +
  `getAnchorMembers` + the `chat.leave` immutability throw all gone). A non-owner member removed from the roster
  correctly loses access (revocation works); a founder removed from the roster keeps access **iff** they own the
  space — guaranteed control now flows from **OWNERSHIP** (the session/message write gate + members-only
  visibility carry an owner-ancestor arm; `createAnchoredSession` defaults `owner = caller`), separating
  who-is-in (ties) from who-controls (ownership/gates). This was a **D2 decision** (founders become removable —
  the founder elected the elegant long-term model), not just a fix; the formerly-scheduled **P2-MEM-AR** is
  subsumed. (Regressions D2 a–d pin all four properties.)
- **`rt.yi.where` gating — doc correction, not a hole.** `rt.yi.where` *does* apply per-row visibility at the
  runtime root (`create.ts` `canSeeHoldingForRead`/`canSeeSpiritForRead` on every branch); the earlier
  "ungated" claim was stale (it read only the internal raw `matchesPredicate`, `where.ts:10`). Residual =
  per-row gate-eval *perf* (the projection pillar's job) + a regression test pinning the floor. No over-share.
- **Trigger budget resets to a fresh 1024 on every `on_message` hop**, so a bot-to-bot reply cascade is
  bounded by cycle-detection, not the 1024 budget; the docstring (`triggers.ts:158-160`) claims the opposite.
  Scheduled as **P0-CD5** — a docstring reconcile only (the per-hop-reset vs. shared-budget tradeoff is the
  founder's call, no semantics change).
- **Discover / present-dimension caches not invalidated on the unified `deployKind` path** → stale port
  disclosure after a redeploy. (Folded into Phase 1.)
- **Single process-global delivery chain** serializes all fan-out (throughput ≈ 1/(sockets × per-offer
  cost)); **`caller-within-n-hops` is an uncapped, unmemoized BFS.** Both are scale cliffs, not pivot work.
- **The sigil install-scope-guard is built and tested but wired to nothing** — the "members change shared
  data via miniapps" path is currently read-only in the shipped shell. Wire the guard *with* any mutating
  mount.
- **Doc rot — addressed for this pivot's named pages, not globally.** `community.md` / `session.md` taught the
  deprecated `face_class` / `anchorMembers`-bundle / per-community-member-kind model the frame retired; the recut
  landed with the Phase-2 seam (SG track) and the S6 `anchorMembers` deletion. Broader docs truth remains an active
  completion gate in [`13-final-yi-sdk-closure-plan.md`](13-final-yi-sdk-closure-plan.md).

**Diagnosis anchors (from the exploration, verified there):**

- Spine: `yi.ts:180-245`; `substrate-seed.ts:91-122,218`.
- Holding-by-field-presence: `yi-guards.ts:48-60`; `runtime-yi/types.ts:57`; `glossary.md:99`.
- `holdingSubFaceFromKinds` re-derivation (~84 occurrences across `core`/`server`/`std`; the definition + ~80 call sites): `holdings/holding-ops.ts:102`.
- `Kind` 13-field canonical set vs ~45 stored fields: `kinds/class.ts:259-358`, `:377-454`.
- `manifest` overloads + dynamic-input degradation: `runtime-yi/types.ts:769-805`.
- "face" × 6 + doc contradiction: `class.ts:384`; `runtime-yi/types.ts:29,438`; `ports-and-faces.md:5` vs
  `yi.md:26`.
- Membership × 3: `auth.ts:299,406`; `std/.../family.ts:183,337`.
- Grant-is-a-Token: `grants.ts:11,55,294`.
- Dead port model: `dimensions/registry.ts:127`.

**The seam's three working precedents (why it is a finish):**

- CQRS row/event: `encoded-implementation.md:43-45`.
- Single-writer children + aggregate-at-read: `std/.../wishing-pool.ts:58-63,255`;
  `runtime-yi/create.ts:458`.
- Faces-as-projections over one row: `yi.ts:180`; `runtime-yi/create.ts:5-7`.
- Constitutional law (the seam is already required): `encoded-implementation.md:11,83-85`.
- Already-present trait vocabulary (a trait = a composed kind): `docs/concepts/traits.md`.

**Provenance:** integrates the multi-round exploration `docs/design/unified-mental-frame.md` (2026-06-16→18; **its diagnosis is folded into §2/§4 here — the original exploration file is not retained in this package**),
a full kernel read (all core clusters), a peer-agent design critique, and this conversation's decisions
(2026-06-18).
