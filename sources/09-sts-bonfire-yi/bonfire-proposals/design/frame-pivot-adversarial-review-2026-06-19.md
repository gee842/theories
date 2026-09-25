# Frame/Pivot Adversarial Review - 2026-06-19

> **Historical review artifact.** Names in quoted findings describe the
> June 19 working tree and are evidence, not current API guidance.

> Where this page and source-anchored docs disagree, `llms.txt` and the cited source files win.

Scope: current uncommitted `docs/concepts/the-frame.md` and `docs/design/the-pivot.md`, reviewed against the working tree and by five subagents with adversarial briefs.

This document does not replace the frame or pivot. It is a review artifact for deciding whether the updated direction should become the final architecture direction.

## Verdict

Not final as written.

The direction is strong as an ontology:

- one conceptual substrate object, `Yi`;
- traits/kinds instead of hard-coded spirit/token/item concepts;
- capabilities as things that can be held, attenuated, revoked, and invoked;
- ports and gates as the main behavior/authz surface;
- specialized storage and projections underneath a unified author-facing model.

But the current frame/pivot still overstates three things:

1. The keystone is not a physical "one table" merge. The code already has one physical `yi` table in Postgres and one canonical `yi` map in memory. The remaining hard problem is the face-shaped writer/index/lifecycle contract.
2. The relation compiler is not yet proven enough to be constitutional. It is currently a destination idea, not an engineering primitive with algebra, cost model, indexes, rebuild, and tests.
3. The product governance layer is under-specified. Discord-like channels, AT/Bluesky moderation/reach, MMORPG inventory/guild/zone systems, negative rights, audit, abuse control, and resource-scoped delegation cannot be hand-waved as "ties" without losing the very product semantics users need.

The recommended stance is: go forward with `Yi + trait + port + gate`, but do not freeze the pivot sequence until Phase 0 is reframed and proven by narrower implementation gates.

## What Should Stay

Keep the conceptual unification.

The user's original motivation is valid: items can carry capabilities, capabilities can grant permissions, agents can be held by things, and a thing can be both object and subject depending on role. The current spirit/token/item split makes this feel accidental. A single "thing" model with traits and held capabilities is the right conceptual spine.

Keep specialized implementations.

The right destination is not "everything has identical storage." It is "everything has the same conceptual interface, while storage implementations can be specialized and declared." Messages already prove the point: they are conceptually in the Yi world, but physically live in `yi_message` for DAG/history/stream access.

Keep ports and gates.

The port/gate split is still the best local expression of "what can this thing do?" and "who may cause it?" It is more concrete than generic actor messaging and more product-friendly than pure object-capability theory.

Keep "tie" as relation vocabulary, but not as metaphysical closure.

Tie is useful for relation thinking. It should not erase useful distinctions between type membership, possession, social membership, containment, delegation, message causality, and materialized feed membership.

## Main Findings

### P1 - Phase 0 Aims At The Wrong Hard Problem

The frame and pivot say the keystone is "one table, no face" and describe collapsing `storage.spirits` and `storage.unifiedHoldings`.

That is misleading if read literally. Current code already has a single canonical `yi` table in Postgres:

- `packages/server/migrations/001_init.sql:40` calls `yi` the unified substrate row table.
- `packages/server/migrations/001_init.sql:48` creates `CREATE TABLE yi`.

Current in-memory storage also has one canonical map:

- `packages/core/src/storage/memory.ts:80` says every Spirit and Holding row lives in one map.
- `packages/core/src/storage/memory.ts:156` says there is no face partitioning at the storage layer.

The real remaining split is not "two physical tables." It is:

- face-shaped public/internal repository APIs: `storage.spirits`, `storage.unifiedHoldings`, `storage.yi`;
- face-shaped writer routing: Postgres `yi` reads are unified, but writes still flow through per-face repos;
- face-kind lifecycle guards: `addKind` refuses adding `core:spirit`, `core:holding`, `sys/session`, or `core:kind` after manifest because the row would become index-malformed;
- API shape: SDK/RPC/product code still exposes `spirits`, `tokens`, `items`, `relationships`, `face: 'holding'`, and face-shaped mint/list calls.

Reframe Phase 0 as:

> Establish one writer/index/lifecycle contract for Yi rows, where face markers are ordinary traits only when their indexes, invariants, migration path, and public API semantics are proven.

Do not call it "merge two repos into one table." That will cause agents to delete useful abstractions instead of solving the actual coupling.

### P1 - The Compiler/Seam Is Not Yet A Scalability Contract

The frame says relation declarations can compile to marker, edge, `yi_message`, list, map, DAG, or CRDT representations. That is plausible as an end-state, but not yet a safe foundation.

Current storage exposes concrete indexed primitives:

- `unifiedHoldings.byHolder`, `byReferent`, `byClass`;
- `yi.byFace`, `yi.byClass`, `yi.byKind`;
- `messages.history`, `messages.children`, `messages.leaves`;
- event log readers and aggregate readers.

That is not yet a relation compiler. It is a set of carefully chosen storage surfaces.

The strongest warning sign is `caller-holds`:

- `packages/core/src/gates/gate.ts:1054` uses `unifiedHoldings.byHolder`.
- `packages/core/src/gates/gate.ts:1059` then falls back to `storage.yi.byFace('holding')`.
- `packages/core/src/gates/gate.ts:631` only checks unburned/class/holder/issuer/active, not full cascade liveness.

So the hot gate path is still partly a scan/materialize/filter path. A compiler that hides that cost would make the system less predictable.

Before generalizing, prove one relation family end to end: membership.

Minimum membership compiler proof:

- one declaration shape for session/community membership;
- one canonical row representation;
- one materialized hot read for `member(caller, container)`;
- rebuild from canonical rows, not from complete event history;
- explicit indexes for holder, referent/container, role label, active/live status;
- tests for send/list/fanout/join/leave/hostile mint/revocation;
- PG and memory parity;
- no full-table fallback in the hot path.

### P1 - Product Governance Is Under-Specified

The frame is elegant as ontology, but product authority needs more than gates over verbs.

Current delegation appears too coarse for real product authority: "may invoke verb X" is not enough. Real products need resource-scoped delegation:

- bot may moderate only one channel;
- agent may use one tool only inside one community;
- member may view a channel but not post;
- moderator may timeout but not ban;
- item may grant a combat ability only in a zone or encounter.

Discord's permission model is a useful stress test. Its documented permissions include channel-oriented actions such as `VIEW_CHANNEL`, `SEND_MESSAGES`, `MANAGE_MESSAGES`, `MANAGE_THREADS`, and `VIEW_AUDIT_LOG`, with administrator bypass and channel overwrite semantics in the same product model. See Discord's [permissions documentation](https://docs.discord.com/developers/topics/permissions).

Bonfire needs a first-class policy/capability layer with:

- resource scope;
- tenant/community scope;
- positive and negative rights;
- role hierarchy or precedence;
- explainability: why allow/deny?;
- audit trails;
- moderation sanctions;
- rate/abuse signals;
- revocation and cache invalidation semantics.

This can still be Yi-shaped. But it should not be reduced to "membership relation with a label" in the product model.

### P1 - Fanout Is Broadcast-Filtered, Not Interest-Indexed

The live event path is engineered carefully, but its current shape is not the final shape for Discord-scale or social-feed-scale systems.

Current facts:

- `packages/core/src/storage/delivery-pump.ts:31` says one chain delivers events sequentially.
- `packages/core/src/storage/delivery-pump.ts:44` warns backlog grows without bound if append-rate times fanout cost exceeds 1.
- `packages/server/src/ws.ts:881` has one live `events.subscribe` per attached server fanning each event out to every registered connection.
- `packages/server/src/ws.ts:1205` performs per-connection delivery with visibility checks.

That is a reasonable pre-scale design. It is not an interest-indexed delivery architecture.

Discord's gateway documentation explicitly treats state tracking, presence updates, and sharding as separate concerns; large apps shard gateway traffic by guild ID. See Discord's [Gateway sharding documentation](https://docs.discord.com/developers/events/gateway#sharding). ActivityPub makes inbox/outbox collections explicit and requires inbox de-duplication. See W3C [ActivityPub inbox/outbox](https://www.w3.org/TR/activitypub/#collections). AT Protocol separates PDS, Relay, App View, feed generators, and labelers for scale and reach. See AT Protocol's [overview](https://atproto.com/guides/overview).

Lesson: Bonfire needs recipient sets, feed/materialized views, subscription indexes, and presence channels as explicit outputs. They can be generated from Yi relations, but they cannot remain "generic event plus per-caller filter" forever.

### P1 - "Every Representation Is Rebuildable" Is Too Strong

The frame requires every derived representation to have canonical source, audit events, and tested rebuild paths. Good principle, too broad as current fact.

Current `YiRuntime.history` says the event log is best-effort and can be truncated under retention:

- `packages/core/src/runtime-yi/types.ts:695` says history is best-effort truncated.
- `packages/core/src/runtime-yi/types.ts:696` says the Yi row is canonical and the event log is an audit/replay feed.

Therefore migration/backfill must not depend on complete event replay unless the retention contract says it is complete. Derived indexes should rebuild from canonical rows where possible, and from retained events only where the product explicitly accepts loss of older audit detail.

This matters for federation too. AT Protocol makes signed user repositories, relays, App Views, and labelers first-class. ActivityPub makes inbox/outbox delivery and de-duplication first-class. Bonfire cannot hide signing, tombstones, deletes, labels, archive economics, and account recovery below the frame forever if federation is part of the product destination.

### P2 - Presence Must Be Explicitly Non-Durable

Presence, typing, voice state, zone/AOI, and online rosters should not be forced into durable Yi semantics.

The current server already treats presence as ephemeral Redis-backed state with TTL and capped snapshots. That is the right instinct. The frame should preserve a crisp category for volatile state:

- not canonical row truth;
- not audit-log truth by default;
- often tenant/channel/zone scoped;
- usually eventually consistent;
- often pushed over subscriptions/gateways;
- bounded by TTL and backpressure.

Discord and MMORPGs both keep this separate from durable identity and inventory. If Bonfire tries to express presence as ordinary ties without a volatile subsystem contract, it will make hot-path state expensive and semantically confused.

### P2 - Inventory/Items Need Transactional Aggregate Semantics

The user motivation includes items that carry agents/capabilities. That is the right conceptual target. But MMORPG-style items are not just graph edges.

They need:

- atomic transfer/trade;
- anti-duplication invariants;
- stack limits;
- unique/equipped slots;
- materialized counters;
- ownership and escrow;
- zone/encounter restrictions;
- server-authoritative action validation;
- fast capability lookup.

Bonfire can model items as Yi and capability as held Yi, but the storage/transaction layer must expose inventory aggregates as first-class hot paths. Otherwise "item as actor" will work in demos and fail in games or high-throughput communities.

### P2 - Object-Capability Claims Are Only Partly True

The model has object-capability flavor because capabilities are things that can be held. But current invocation is still globally addressable by uid and then gated. Some gates are marker/ACL-like, such as "caller bears kind."

If Bonfire wants object-capability properties, the invariants need to be explicit:

- unforgeable possession;
- attenuation by construction;
- no ambient authority surprises;
- delegation provenance;
- revocation semantics;
- capability discovery rules;
- capability invocation requiring possession, not merely uid knowledge.

Otherwise call it capability-oriented access control, not pure object-capability security.

### P2 - Moment/Tie Should Not Become Daily API

The frame's four-word vocabulary, `Yi`, `Tie`, `Port`, `Gate`, is usable. The deeper "Moment" collapse is not.

The current substrate is row-canonical, with purpose-built message tables, storage repos, events, handlers, and port dispatch. Treating everything as "tie seen in flow" is useful philosophy but bad API pressure. It increases conceptual load and risks overfitting the architecture around a metaphor rather than around implementation closure.

Keep "Moment" out of the daily model.

## External-System Lessons

### Discord

Discord teaches that permission systems must be product-shaped, not merely graph-shaped.

Important lessons:

- permissions are resource-specific, especially guild/channel/thread/voice/resource scope;
- role hierarchy and administrator override matter;
- audit logs and moderation verbs are product primitives;
- presence and gateway event state are cached, updated, and sharded separately;
- large-scale fanout is routed by shard/tenant, not by scanning all live clients.

Bonfire implication:

`Gate` needs a materialized permission engine with explainability, resource scopes, negative rights, channel overrides, and cache invalidation. `Tie` can represent the underlying facts, but cannot be the whole product model.

### AT Protocol / Bluesky

AT Protocol teaches separation of primitives and views.

Primary facts from the official overview:

- user data lives in signed repositories;
- the network has PDS, Relay, and App View roles;
- Lexicon is the schema/interoperation language;
- App Views support aggregate data, discovery, search, feeds, and metrics;
- feed generators and labelers are separate reach/moderation services.

See AT Protocol [overview](https://atproto.com/guides/overview) and [Lexicon specification](https://atproto.com/specs/lexicon).

Bonfire implication:

Do not collapse "speech", "reach", "moderation", and "view" into one substrate layer. A Bonfire version of App Views, labelers, feed indexes, and migration/recovery surfaces may still be Yi-aware, but they are real systems.

### ActivityPub

ActivityPub teaches explicit delivery collections.

The W3C spec defines outbox and inbox as ordered collections, says outbox reads are permission-filtered, says inboxes contain received activities, and requires de-duplication of inbox activities. See [ActivityPub Collections](https://www.w3.org/TR/activitypub/#collections).

Bonfire implication:

If federation or social delivery matters, recipient sets and inbox/outbox semantics must be first-class. Generic events plus visibility filters are not enough for delivery guarantees, de-duplication, retry, backfill, and moderation.

### MMORPG / ECS Systems

MMORPG and ECS systems teach a boundary:

- entities/components are good conceptual primitives;
- hot simulation state, inventory, buffs, zones, guilds, parties, chat, and presence need specialized systems;
- server authority and transactionality matter more than ontology purity;
- item instance vs item template must be crisp;
- effects/buffs/capabilities need deterministic conflict/stacking rules.

Bonfire implication:

Trait-based Yi is a good entity/component substrate. But game-like capability and inventory flows need specialized transaction and indexing semantics. Do not hide them behind a generic graph walker.

## Anti-Patterns To Avoid

### Metaphysical Compression

If every concept is declared "just a tie," the architecture may feel elegant while losing operational handles. Some distinctions are product facts:

- membership vs role vs ban;
- holding vs containment vs delegation;
- feed membership vs read permission;
- message causality vs storage parentage;
- presence vs durable state.

Collapse representation only after behavior is proven.

### Removing Useful Internal Boundaries

The author-facing model can be one Yi. The implementation should still keep:

- message storage;
- event log;
- presence;
- feed/index/materialized views;
- inventory aggregate indexes;
- federation archive/signing;
- moderation/audit stores.

The danger is not "too many internal systems." The danger is exposing those systems as unrelated concepts to authors. Internal specialization is allowed.

### Future Mechanism As Current Fact

The docs now label many future mechanisms better, but still occasionally talk as if the compiler, collective capability, and no-face lifecycle already constrain the code. They do not.

Make every claim say one of:

- current fact;
- current violation/debt;
- accepted destination;
- experiment hypothesis;
- rejected path.

### "Subtraction" That Hides Migration

Retiring faces, class-spec fields, and public SDK APIs is not simple deletion. It is a cross-package migration across core, server, SDK, tests, docs, snapshots, examples, and product assumptions.

Subtraction is good only if the new invariants are smaller and more testable.

## Critical Things The Current Direction Cannot Yet Do Elegantly

- Resource-scoped delegation: "agent can do X only in Y."
- Negative rights: ban, mute, block, timeout, deny-overrides-allow.
- Discord-style channel/thread permission overwrites.
- Collective capability: group-held authority exercised by members without joining the target.
- Policy explainability: why can/cannot caller invoke this port?
- Moderation: report, modlog, appeal, quarantine, sanctions, evidence preservation.
- Modern privacy: audience lists, per-channel read/write split, blocked DMs, label/age policy.
- Interest-indexed fanout: recipient sets, inboxes, feeds, backfill, de-duplication.
- Volatile presence: online/typing/voice/zone state outside durable audit truth.
- Inventory/transaction flows: atomic trades, unique/equipped slots, stack limits, escrow.
- Federation trust: signed rows/logs, tombstones, account migration, hostile host recovery.
- App View/feed/labeler separation: speech vs reach vs moderation.
- Migration under event retention: rebuild from canonical rows, not assumed complete history.
- Stable public API migration: SDK/RPC diff, snapshot update, migration guide.

## Recommended Phase Rewrite

### Phase A - Truth Pass

Before implementation, fix the frame/pivot claims:

- remove the false `rt.yi.where` raw/ungated claim;
- replace "two physical repos" with "face-shaped write/index/API contracts";
- mark relation compiler as future mechanism, not current architecture;
- mark collective capability as future mechanism;
- tighten "every representation rebuildable" to the actual retention/rebuild contract;
- clarify that messages are a deliberate specialized storage exception;
- clarify that presence is volatile and outside durable Yi truth.

### Phase B - Field And API Inventory

Produce a matrix before code changes:

- every public SDK/RPC face-shaped surface;
- every core/server call site using `storage.spirits` or `storage.unifiedHoldings`;
- every `face`, `face_class`, `holdingSubFaceFromKinds`, and `Kind.face` dependency;
- every stored `Kind` field, grouped into canonical, trait, migration-only, and dead;
- every direct `rt.storage.*` backdoor in std/examples.

This is the real map of coupling.

### Phase C - Correctness Debt Before Grand Refactor

Fix or explicitly defer independent debts:

- `caller-holds` full holding fallback scan;
- cascade liveness gap in `caller-holds`;
- production-unwired gate SQL compiler;
- public API snapshot plan;
- membership docs/code truth;
- direct storage backdoors in std/examples.

### Phase D - Membership Compiler Proof

Implement only membership as the first compiled relation family.

Success criteria:

- one declaration;
- one canonical row shape;
- one fast materialized read;
- rebuild from rows;
- revoke and cache invalidation;
- PG/memory parity;
- no unbounded scans;
- session/community behavior preserved.

### Phase E - Policy/Capability Layer

Design resource-scoped policy before collective capability ships.

It should include:

- scope tuple: tenant/container/channel/resource/port;
- positive and negative rights;
- attenuation;
- explain;
- audit;
- revocation;
- cache invalidation;
- migration/backfill.

### Phase F - Delivery, Presence, Feed, Federation

Treat these as first-class systems:

- recipient set and delivery index;
- presence/typing/voice/zone volatile state;
- feed/AppView/materialized view;
- federation log/signature/tombstone/archive;
- moderation labels and trust signals.

They can be declared from Yi/tie facts, but they need explicit operating semantics.

## Final Recommendation

Do not reject the frame.

Do reject the idea that this version is final.

The best direction is:

> One conceptual Yi interface, with traits/kinds, ports, gates, and capabilities; specialized internal systems for messages, presence, fanout, policy, inventory, feeds, moderation, and federation; a compiler only after one relation family proves the shape under performance and migration tests.

The system can become elegant and well engineered if it treats unification as an author-facing and conceptual invariant, not as a mandate to erase internal architecture.
