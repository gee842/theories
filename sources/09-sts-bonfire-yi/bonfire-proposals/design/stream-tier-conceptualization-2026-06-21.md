# The Stream tier (formerly `yi_message`) — is it right under the ideal Yi, and how to dissolve the friction

> Where this page and source-anchored docs disagree, `llms.txt` and the cited source files win.

---

## 0. TL;DR

> **⚠️ §0–§5 below are the original *pre-review* analysis (2026-06-21).** The **diagnosis** holds (the storage
> is sound; the friction is the *name* + the §3 self-contradiction). The proposed **cure** was **corrected by
> the five-lens review** — see the **Status** block above and **§Review outcome**. What shipped is the
> `yi_message → stream` rename + the **seam reconciliation** (stream = the canonical materialization the seam
> selects); the *"lead with the trait" / "one trait whose backing escapes the row"* mnemonic was **dropped as
> false** and did **not** ship, the §16b demotion did **not** ship, "strictly worse"/"2–3 orders of magnitude"
> were softened as unbacked, and the change was a cross-cutting **code** rename, not doc-only. Read §0–§5 as the
> route, not the destination.

A founder intuition — *"`yi_message` is a special case of the event; if the DAG and a list have their
own separate data, what is `yi_message` even for? I find it hard to conceptualize"* — turned out to rest
on two inverted premises. Correcting them is the whole answer:

1. **The event is the derived shadow of the message row, not its source.** Architecture C / Law 8: the
   `yi_message` row is canonical and prunable-never; the `yi.message` event is a same-transaction,
   *prunable*, best-effort audit dual-write. Truth runs row → event, not event → row.
2. **There is exactly one content store.** `yi_message` *is* the DAG (the `parents[]` column); the "DAG
   view" and the "list/timeline view" are pure read-functions over that one store. A separate
   `list`/`feed`/`crdt` store does not exist — it is a *destination* (the seam compiler), not code today.

Under the ideal Yi, `yi_message` is the **Stream tier**: one of exactly two *named, never hidden* non-Yi
centers (the other being the column-promoted relations `parentUid` / `originKindUid`). It earns the
exception by carrying three axes that no tie cheaply expresses: a **dense per-session `seq`**, the
**reply DAG**, and **volume**. Both alternative architectures (event-canonical; message-as-Yi) are
**worse** (the original "strictly worse" was softened post-review as unbacked — see §Review outcome). So:
**keep the storage.**

The friction is the **name** (`yi_message`'s `yi_` prefix asserts yi-ness against a tier defined by *not*
being a Yi) and a **live self-contradiction** in §3 (a reply is described as both *is* and *is not* a tie).
*(retired route — see the banner above: the original draft here proposed "lead with the trait" and taught
`yi_message` as "the one trait whose backing state spills out of the row," and called the change "doc-only."
The review showed that mnemonic is **false** — `membered`/`container`/`historied` also escape the row, and
`streamed` is an inert marker — so what shipped is the rename + the **seam reconciliation**, a cross-cutting
code change. See Status + §Review outcome.)*

---

## 1. The question

The founder asked, across two turns:

- Is `yi_message` a special case of the event?
- If the DAG and a list "have their own separate data," what is `yi_message` for in core?
- Some of these decisions predate the current (Yi-frame) direction — **is the current approach still
  the best under the ideal Yi?** How is performance at scale? Any limitations? Is it elegant?
- *"Somehow I found it a bit hard to conceptualize."*

For a frame whose explicit north star is **least cognitive resistance**, that last sentence is the
signal that matters most — it is a frame-smell to diagnose, not a reader's gap to apologize for.

---

## 2. What we discovered (grounded)

### 2.1 The two inversions

**Inversion A — direction of truth.** A message send performs two writes in **one transaction**
([`yi-message.ts:106`](../../packages/core/src/stream.ts:106) builds the event payload; both storage adapters
dual-write):

```
  WRITE 1 (canonical)            WRITE 2 (derived)
  ┌─────────────────┐            ┌──────────────────────┐
  │  yi_message row │ ─same tx─▶ │  yi.message event    │
  │  • mutable      │            │  • immutable          │
  │  • never pruned │            │  • PRUNABLE audit     │
  │  • read direct  │            │  • time-travel/wire   │
  └─────────────────┘            └──────────────────────┘
        TRUTH                          SHADOW
```

Live reads (`messageHistory`, `currentPath`, `branches`) read `yi_message` rows directly and **never
replay events** ([`runtime-messages.ts`](../../packages/core/src/runtime-messages.ts)). This is Architecture C
(row canonical; events = prunable best-effort audit) made concrete for messages, and it is exactly Law 8.
So "message = special case of event" is backwards: **the event is the special-cased shadow of the row.**

**Inversion B — one content store, two read-views.** Every DAG helper in
[`yi-message.ts:143-287`](../../packages/core/src/stream.ts:143) (`findChildren`, `findSiblings`, `findLeaves`,
`walkPathToRoot`, `getBranchInfo`) is a **pure function over a `readonly Message[]`** working set pulled
from the *same* `yi_message` store. "The DAG" = the `parents[]` column read one way; "the list/timeline"
= the same rows ordered by dense `seq` / walked first-parent. There is no `yi_dag`, `yi_list`, `yi_feed`,
or `yi_crdt` table (verified by grep). The plural-representation idea in §11 ("one stream is a DAG,
another a list, another a CRDT") is a **destination**, not present code.

### 2.2 What `yi_message` actually is — the Stream tier

From [`01-frame.md` §16b](../../yi/01-frame.md): *"a canonical store (Law 8) with a same-transaction audit
event — but **not a Yi** and **not a representation** the compiler picks. A canonical store is not a
representation *of* anything."* Law 1 counts the **named, never-hidden** non-Yi centers as the
column-promoted relations **and** the stream tier; D9 ([`02-pivot.md`](../../yi/archive/02-pivot.md)) ratifies this
explicitly and corrects the earlier over-claim that `parentUid` was the *only* exception.

Crucially, the frame's §1 thesis **already permits this**: *"Not 'everything is one table' — everything
is one kind of meaningful thing, while storage, indexes, fan-out, presence, **messages**, feeds, and
moderation specialize where scale demands."* The unification is of **meaning** (the authoring surface),
not of **storage**. Messages specializing in storage is *consistent with* the frame by its own top-line
claim — not a violation of it.

### 2.3 The three load-bearing axes

`yi_message` earns its separate existence because it carries three things a `yi` row + tie graph cannot
cheaply express ([`001_init.sql:194-237`](../../packages/server/migrations/001_init.sql:194),
[`yi-message.ts:8-15`](../../packages/core/src/stream.ts:8)):

| Axis | Mechanism | Why a Yi/tie can't carry it cheaply |
|---|---|---|
| **dense per-session `seq`** | `pg_advisory_xact_lock(session_uid)` → `COALESCE(MAX(seq),0)+1` ([`pg-storage.ts:2160`](../../packages/server/src/pg-storage.ts:2160)) | The Yi `seq` is a *global* `BIGSERIAL`; a tie has no per-container counter. Backs exact `beforeSeq` paging + O(1) unread counts. |
| **the reply DAG** | `parents TEXT[]` + GIN index | Branch/regenerate/edit at message scale; millions of edges can't each be a child Yi. |
| **volume** | a lean purpose-built row | The Yi shape (unique `path`, `kinds[]` GIN, `parentUid` cascade, `head_event_uid`, manifest lifecycle) is dead weight ×billions of rows. |

### 2.4 The three-tier decomposition of a chat (the clean model)

```
  session Yi (a real Yi: "membered + streamed")
    ├─ membered → roster: anchorMembers ∪ participant edges   ┐ container metadata
    └─ streamed → activeLeafUid (which branch tip is live)     ┘ (on the Yi row)
        │  FK
        ▼
  yi_message rows  ── Stream tier (canonical) ── content + parents[] DAG + dense seq
        │  same-tx dual write
        ▼
  yi.message events ── derived audit shadow (prunable) ── time-travel / wire / replay
```

The `membered` half lives **on the Yi**; the `streamed` half's *content* lives in **`yi_message`**; the
event log is the **shadow**. Nothing is redundant — each tier holds what the others structurally cannot.

### 2.5 Performance at scale

The scale story splits into two axes; only one touches `yi_message`.

- **Deliberate write ceiling (the `yi_message` one).** The per-session advisory lock **serializes all
  writes to a single session**. [`04-execution-plan.md` R8](../../yi/archive/04-execution-plan.md) classifies this as
  *deliberate*, not debt: *"single-writer-per-session is a correctness guarantee, not an accident,"* kept
  *"until a measured need overturns it,"* with G7's perf bar a *future* gate (*"Today's kernel is not
  Discord/MMORPG-scale"*).
  - **Excellent for the 99% case** — DMs, group chats, normal channels: fan-in per session is bounded,
    the lock is never hot, reads are O(1) by `(session, seq)` with no fold.
  - **A real ceiling for the megachannel-broadcast (firehose) shape** — one session, tens of thousands of
    concurrent posters. That workload is **explicitly deferred** (founder's 2026-06-19 call,
    [`02-pivot.md`](../../yi/archive/02-pivot.md) deferred set). So the ceiling is known and the workload that hits it
    is parked.
- **Read / fan-out / aggregate axis (NOT `yi_message`'s job).** Broadcast fan-out, cross-row reads,
  JSON-bag perf, unread-at-scale → the **projection pillar** (P2 / D14), the real engineering spine of
  the seam. Do not conflate these with the message-write lock.

### 2.6 Limitations (honest list)

- **Per-session write throughput** — the lock above. The binding one.
- **No cross-session DAG edges** (by design) — a reply can't cross sessions; "quote from another channel"
  is *content*, not structure; forking spawns a new session via `anchorForkOf`.
- **Not yet partitioned** — single table (stated pre-launch trade in `001_init.sql`); the RANGE-partition
  path keeps the advisory-lock allocator, only the `UNIQUE` backstop drops.
- **Unread-count couples to the lock** — cheap unread needs the gapless `seq`, which needs the lock; the
  feature and the ceiling are the *same* decision.
- **Deep-branch reads are windowed** — `currentPath` walks within `TURN_WINDOW_LIMIT`, not unbounded.

### 2.7 Two framings already in the docs — and a live contradiction

The same store is pitched at **two altitudes**, and the doc leads with the heavier one:

- **Heavy (leads today):** "the Stream tier, a *named non-Yi center*, an admitted exception" — Law 1,
  §16b, D9. Reads as *a rule you must memorize*.
- **Light (already exists, already built):** "`streamed` is a trait; composing it *provisions a moment
  stream* as backing state, like `identity` provisions a keypair" — §4
  ([`01-frame.md:250-253`](../../yi/01-frame.md)), §7's trait table, the
  [`03-architecture.md`](../../yi/archive/03-architecture.md) "Trait | Grants | **Backing state**" table
  (`streamed → a provisioned stream`), and **`streamed` is a seeded trait in code** (seq 15-19, landed
  178fcd97, [`phase-0.md` P0-AG0](../../yi/archive/phases/phase-0.md)). Reads as *something that falls out of a rule you
  already hold*.

And a **self-contradiction in the North Star itself**: §3's tie-table lists *"the message DAG
(`parents[]`) → a **relation**,"* then four lines later caveats *"the message reply-link is **not** a tie
at all."* The defining document says both.

---

## 3. The candidate architectures — and why the current one wins

Only three shapes are possible for messages. The current one is a local optimum; both alternatives are
**strictly worse**, not merely different.

| | Architecture | Why it loses |
|---|---|---|
| **A** | **Event-canonical** (messages *are* events; fold for views) — the founder's "special case of the event" intuition | You still need a queryable read-model for timeline/paging/branch (can't fold the log per read), so you rebuild a `yi_message`-shaped table anyway — *and* the event log becomes **un-prunable** (it's now canonical). Same two structures, minus Architecture-C prunability. |
| **B** | **Message-as-Yi** (a message is a `yi` row; a reply is a tie) — pure frame purity | Messages outnumber all other entities by 2–3 orders of magnitude; the Yi shape's `UNIQUE path` index, `kinds[]` GIN, `parentUid` cascade, `head_event_uid`, and manifest lifecycle become **dead weight ×billions of rows** — a large, multiplicative storage + write-amplification tax. |
| **C** | **Stream tier** (current — `yi_message` canonical, event = shadow) | Pays neither tax; event stays prunable, row stays lean. Cost: **one named exception** in the conceptual model — the exact thing that feels heavy. |

The decision *predates* the frame (S1/D3 message consolidation + Architecture C), but it has been
**re-ratified under the frame** (D9 names the tier; D14/R8 classify its scale; P0-AG0 already re-cast
`streamed` as a trait). It is not a stale pre-frame artifact — it survived scrutiny.

---

## 4. The diagnosis

**The storage is right (≈8.5/10). The conceptual *exposure today* is what feels wrong (≈6/10). The gap
between them is a framing problem, not a storage problem.**

- Storage layer: three tiers, each carrying exactly what the others can't, clean same-tx dual-write,
  row-canonical + prunable audit. Well-factored.
- Conceptual layer *today*: you author `session.send` and think in `seq` / `parents` / `leaves` /
  `activeLeafUid`; "messages aren't Yis" is memorized; the North Star contradicts itself (§3).
- Conceptual layer *at destination* (post-seam P3-SG1, `stream('messages',{volume:'high'})` hides the
  table): ≈8.5/10.

The founder's discomfort is precisely the 8.5→6 gap, and it is **doc-fixable now** — the lighter framing
is already in the code and partially in the docs; it just doesn't lead.

---

## 5. The best way to dissolve it  (ORIGINAL proposal — retired; see the §0 banner + §Review outcome)

> The trait-led cure below (§5.1's "one trait whose backing escapes the row" mnemonic; §5.3's scale-escape
> note) was **dropped** post-review; only **§5.2** (resolve the §3 contradiction) shipped, alongside the seam
> reconciliation. Kept here as the original reasoning, not as what landed.

**Keep the storage. Fix the framing. Resolve the contradiction.** Concretely, three moves, cheapest
first:

### 5.1 Lead with the trait, and name the one true asterisk (the core move)

Teach `yi_message` as *the backing state of the `streamed` trait*, not as a standalone tier. The mental
model to make canonical:

> A trait's backing state normally lives in `dimensions[trait]` — a JSONB bucket on the row. **`streamed`
> is the one trait whose backing state is too voluminous and too specially-ordered to fit in a bucket, so
> it *spills* to a purpose-built table.** That spillover store is the "Stream tier." You don't
> conceptualize a named non-Yi center; you conceptualize the `streamed` trait — whose bucket happens to be
> a table.

This is *least cognitive resistance*: `yi_message` stops being an exception to memorize and becomes a
consequence of a rule already held (*traits have backing state; backing state is usually `dimensions`,
occasionally a spillover store*). It is also **faithful to the prime principle** (reconcile code → docs,
never soften the ideal): the *code* already seeds `streamed` as a trait; the doc's emphasis is what lags.

The honest asterisk to state plainly (this is what actually dissolves the mystery): **`streamed` is the
single trait whose backing state escapes the row.** Every other trait's data — including `identity`'s
keypair — sits in `dimensions[trait]`. Naming "it's the trait whose state doesn't fit in the row" turns
the exception into a one-sentence rule.

### 5.2 Resolve the §3 contradiction — pick one reading

Make the North Star say one thing: **a reply *is* a relation by reading-lens, and *stream-internal* by
storage.** I.e. conceptually `msg —parent→ msg` is a relation (you may read it as one); its
*representation* is a slot inside the stream tier (`parents[]`), never a child Yi. This is the same
trait/role-vs-storage split the whole frame runs on, applied to the reply edge — so it dissolves the
contradiction without inventing anything.

### 5.3 Frame the seam as both the conceptual *and* the scale destination

[`phase-3.md` P3-SG1](../../yi/archive/phases/phase-3.md) already specifies `stream(name,{volume})` compiling
`volume:high → yi_message`. Two things worth making explicit in the frame:

- **Conceptual:** post-seam, the author writes `stream(...)` and never names `yi_message`; the Stream
  tier "leaves the mental frame, stays in storage" (the same move §10 makes for per-community member
  kinds). This is the destination that takes the exposure from 6 → 8.5.
- **Scale (net-new — not yet in the docs):** the seam is the natural escape valve for the per-session
  write ceiling. A future `stream(volume:'firehose')` could compile to a **lock-free append-only**
  representation (timestamp ordering, no dense `seq`, unread moved to a projection) behind the *same*
  `post`/`timeline` interface. This reframes §11's plurality as a **scale** feature, not only an elegance
  one — so the ceiling in §2.5 is escapable-by-design, not a wall. (Today firehose is *deferred*, so this
  is a forward-note, not a Phase-3 commitment.)

---

### 5.4 The name itself — `yi_message` is the wrong word

The founder flagged (2026-06-21) that `yi_message` is hard to understand. The diagnosis is the same as the
rest of this doc: **the name fights the concept.** The `yi_` prefix asserts the table is part of the Yi
family (a peer of `yi`) — i.e. that a message *is a Yi* — when the concept is defined by
being **the one canonical thing that is explicitly NOT a Yi** (§16b: "not a Yi — no
`kinds[]`/`dimensions`/`originKindUid`"). The prefix is the lie, and it is the specific source of the
"can't easily understand it" feeling.

The frame has *already* converged on the right word everywhere except this table: the trait is **`streamed`**,
the seam relation/verb is **`stream(name, {volume})`** / `post` / `timeline`, and the tier is named **"the
Stream tier."** The table is the lone holdout still called `yi_message`.

- **Recommended: `stream`** (table/tier), row type stays `Message` (an entry in a stream) — total vocabulary
  unity across `streamed` → `stream()` → the `stream` table, and it *reinforces* the "this is the Stream tier,
  not a Yi" reading. Robust to the §16b-vs-pivot fork (it's the Stream tier either way).
- **Conservative: `messages`** — drop the misleading prefix, keep the plain entity noun. Loses the vocabulary
  unity but kills the yi-ness lie.
- **Avoid `moment`/`moments`** — evocative (the frame's deep word for a port-firing) but it re-imports the
  event-sourced flavor D1 deliberately brackets as *rationale, not the daily model*, and over-claims (not
  every moment is a message).
- **Avoid keeping any `yi_` prefix.**

**Whichever noun wins, killing `yi_` is the fix.** The rename is a cross-cutting CODE change (schema, both
storage adapters, `runtime-messages`, `storage/types`, the SDK, migrations, tests) — so it is sequenced
*after* the framing fork is resolved (the name follows the settled concept) and after the storage layer is
quiescent (see Coordination below).

## Review outcome (five-lens, 2026-06-21)

Before implementing, a five-lens review (framing · ideal-Yi fidelity · elegance · adversarial · engineering)
stress-tested this doc. It confirmed the storage verdict (keep it; ~8.5/10) but **corrected the cure**:

- **The "one trait whose backing state escapes the row" mnemonic is false** — `membered` (roster = edges),
  `container` (children via `parentUid`), and `historied`/`versioned` (a durable history store) also escape the
  row. Dropped it.
- **"Lead with `streamed`, demote the named tier to an appendix" would *soften* Law 1** (which names its
  exceptions in the open by design) and overstates the code: `streamed` is still an **inert marker** (empty
  `rowSchema`, `dimensions['core:streamed']` unused). Dropped the demotion.
- **The right reconciliation is the seam, not a trait mnemonic:** the stream tier is the **canonical
  materialization the seam selects** (`representation: 'stream'`, already in `seam/compile.ts` / `seam/types.ts`).
  "Canonical" (Law 8) and "seam-chosen" (Law 7) are not opposites — §16b had overloaded "representation". This is
  what shipped in the §16 edits, and it resolves the §16b-vs-pivot fork in code-grounded terms.
- **Softened overstatements:** dropped "strictly worse" / "2–3 orders of magnitude" as unbacked; the
  per-session-lock ceiling is *deliberate* (R8), firehose *deferred*.

Net: the rename + the seam-reconciliation framing shipped; the trait-mnemonic framing did not.

## 6. Original proposed edits to `01-frame.md` (HISTORICAL — retired; see Status + Review outcome)

> **What actually shipped ≠ this list.** Only **edit 1 (resolve §3)** shipped as written. Edits **2–5 were
> replaced** by the seam reconciliation: the §16a/§16b edits frame the stream tier as *the canonical
> materialization the seam selects* while **keeping Law 1's named-center count** — so the proposed **demotion of
> §16b to an appendix did NOT ship**, the **"one trait whose backing escapes the row" mnemonic was dropped as
> false**, and no §11 scale-escape note was added. The items below are preserved as the original (pre-review)
> proposal, not a description of what landed.

All edits are to [`../yi/01-frame.md`](../../yi/01-frame.md) unless noted. **None changes storage or code.**

1. **§3 — resolve the reply-edge contradiction.** Replace the dual claim (table row "message DAG → a
   relation" + caveat "not a tie at all") with a single statement: *a reply is a relation by reading-lens,
   stream-internal by storage (`parents[]`, never a child Yi)*. Keep the stream-tier cross-reference;
   remove the "not a tie at all" flat denial that contradicts the table.

2. **§4 / §7 — promote the trait framing to primary.** Strengthen the existing §4 line ("adding
   `streamed` provisions a moment stream") and §7 trait-row into the *canonical teaching*, adding the
   spillover-bucket sentence (§5.1): backing state is normally `dimensions[trait]`; `streamed` is the one
   trait whose backing state spills to a purpose-built table.

3. **§16b — demote "named non-Yi center" to a storage appendix.** Keep the Stream-tier definition
   (canonical, dense `seq`, reply DAG, per-session) but reframe its *opening* as "the backing store of the
   `streamed` trait" rather than "the second named non-Yi center." The honest count stays in Law 1 /
   §16b for completeness, but it stops being the *first* thing a reader meets.

4. **Law 1 — keep the honest count, soften the lead.** Law 1 should still name the exceptions (truth in
   advertising), but the prose can note that the stream tier is *reached through the `streamed` trait*, so
   it is not a separate primitive the author holds.

5. **§11 — add the scale-escape note.** One sentence framing the plural-representation guarantee as the
   escape valve for the per-session write ceiling (the future `volume:'firehose'` → lock-free path),
   citing the deferred firehose decision.

> **Scope discipline:** these are emphasis/contradiction fixes, not new doctrine. They make the doc teach
> the framing the code already implements. The "ideal" is unchanged — no softening; if anything the
> trait-led framing is *closer* to the ideal (one rule, fewer named exceptions).

---

## 7. What NOT to do

- **Do not dissolve `yi_message` into the event log** (architecture A) — loses prunability, rebuilds the
  same read-model, demotes Architecture C.
- **Do not dissolve `yi_message` into Yi rows** (architecture B) — multiplicative storage + write-amp tax
  on the highest-cardinality entity.
- **Do not remove the per-session lock** to chase write throughput without first moving unread-count to a
  projection — the lock *is* the dense-seq guarantee that unread arithmetic depends on (R8: keep until a
  *measured* need overturns it).
- **Do not soften the frame** to accommodate the exception — the right move is the opposite: lead with the
  lighter framing that already exists.

---

## 8. Open questions for the founder

1. **Edit now, or wait for P3-SG1?** The trait reframing (§5.1/§5.2) buys most of the clarity with
   doc-only edits and no code. Worth doing now, independent of when the seam lands?
2. **Is "spillover bucket" the right teaching metaphor**, or do you prefer "provisioned backing store"
   (the language already in §4 / `03-architecture.md`)? The metaphor should be one you'd repeat.
3. **Should the firehose scale-escape (§5.3) be written into §11 now** as a forward-note, or kept out
   until federation/firehose is un-deferred? (Pro: shows the ceiling is escapable-by-design. Con: writes
   destination prose for a parked workload.)

---

## Coordination & sequencing (2026-06-21 git reality)

A concurrent session is actively advancing the canonical branch `docs/yi-direction` (RR3 running;
RR4∥RR7→RR6→RR2 queued). Verified git state from this worktree:

- This worktree (`claude/gracious-meninsky-ae6eff`) is **0 ahead / 23 commits (474 files) behind**
  `docs/yi-direction` (`2ff801a4`) — a stale base.
- The other session has **already edited `docs/yi/01-frame.md`** (Law 2 only — RR1; **not**
  §3/§4/§7/§16b/Law 1, so this doc's analysis stands) and **`03-architecture.md`** (seed count 19→23;
  **not** the trait backing-state table). It has also **heavily rewritten the storage/message layer**:
  `pg-storage.ts` (+220), `storage/types.ts` (+219), `runtime-messages.ts` (+98), `memory.ts`, plus new
  the projection schema now folded into `migrations/001_init.sql` — and is still going.
- `docs/design/` (this doc) is **completely uncontended**.

**Safe to land now:** this design doc only — additive, in an uncontended directory; cherry-picks onto current
`docs/yi-direction` with zero conflict.

**Deferred (not safe / not ready):**
- **The `01-frame.md` framing edits** — pending the founder's fork call, *and* must be redone on a fresh
  worktree cut from current `docs/yi-direction` (this base is 23 behind; they are actively in the same docs).
- **The `yi_message` → `stream` rename** — collides head-on with the in-flight storage rewrite (+220/+219).
  Sequence it after their RR run settles, as a dedicated atomic commit on a fresh branch off current
  `docs/yi-direction`.

> **Update (2026-06-21, fork decision):** per founder direction, this work moves to a **fresh worktree
> `claude/stream-tier` cut from the live `docs/yi-direction` tip (`7ed7cf4d` — RR3 landed *during* this
> exchange; the branch moved from `2ff801a4` while we talked, which is precisely why a fresh base +
> rebase-before-merge beats cherry-picking)** rather than the 23-behind base — so this doc lands on a current
> base and the framing edits will run against accurate line numbers. Forking from the tip already absorbs the
> bulk storage churn (`pg-storage`/`storage/types` rewrite is *in* the base). What
> still gates each step is unchanged: the framing edits wait on the founder's §16b-vs-pivot fork call; the
> `yi_message → stream` rename waits on branch quiescence (a many-file mechanical rename conflicts with any
> concurrent commit, so it wants a gap between the other session's RR fast-forwards).

## Appendix — citation index

- **Stream tier as canonical, named, not-a-Yi:** [`01-frame.md` §16b / Law 1](../../yi/01-frame.md);
  [`02-pivot.md` D9](../../yi/archive/02-pivot.md).
- **Direction of truth (row canonical, event derived):** Architecture C; Law 8
  ([`01-frame.md` §11](../../yi/01-frame.md)); dual-write [`yi-message.ts:106`](../../packages/core/src/stream.ts:106).
- **Event-sourced rationale rejected as the daily frame:** [`02-pivot.md` D1](../../yi/archive/02-pivot.md).
- **Three axes / schema:** [`001_init.sql:194-237`](../../packages/server/migrations/001_init.sql:194);
  advisory lock [`pg-storage.ts:2160`](../../packages/server/src/pg-storage.ts:2160); DAG helpers
  [`yi-message.ts:143-287`](../../packages/core/src/stream.ts:143).
- **`streamed` is a trait (light framing):** [`01-frame.md` §4:250-253 / §7](../../yi/01-frame.md);
  [`03-architecture.md`](../../yi/archive/03-architecture.md) trait backing-state table; seeded
  [`phase-0.md` P0-AG0](../../yi/archive/phases/phase-0.md).
- **Scale = deliberate, not debt:** [`04-execution-plan.md` R8](../../yi/archive/04-execution-plan.md); projection pillar
  D14; firehose deferred [`02-pivot.md`](../../yi/archive/02-pivot.md).
- **Seam destination:** [`phase-2.md` P2-SC1](../../yi/archive/phases/phase-2.md);
  [`phase-3.md` P3-SG1](../../yi/archive/phases/phase-3.md); [`01-frame.md` §10:569 / §11](../../yi/01-frame.md).
</content>
</invoke>
