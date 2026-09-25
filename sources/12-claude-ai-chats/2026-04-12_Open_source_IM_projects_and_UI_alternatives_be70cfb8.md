# Open source IM projects and UI alternatives

created: 2026-04-12T18:32:37.912179Z  uuid: be70cfb8-59db-42b7-ad7b-f2914cbd237e  export: new
messages: 22  total_chars: 42305  human_chars: 682

summary: **Conversation Overview**

The person is building a coordination platform called Nomad OS, with a related project called OpenClaw and a concept called "706 network," featuring a "Pay → Split → Chat → Trust → Coordinate" flow likely targeting Southeast Asia's mobile-first market. The conversation was a deep technical exploration of open source messaging infrastructure, working through the full stack from protocols to frontends to backends, with the goal of identifying the right foundation to build upon.

The discussion began with Tinode alternatives and quickly converged on the Matrix protocol as the strongest candidate. Claude walked through the Matrix ecosystem comprehensively: frontend clients (Cinny recommended as the fork base due to React/TypeScript stack, Apache 2.0 license, and lightweight codebase; FluffyChat as runner-up for Flutter cross-platform needs), backend homeservers (Tuwunel recommended as the production pick — Rust, Apache 2.0, single binary, government-backed, deployed at national scale in Switzerland), and the Matrix protocol itself (a replicated DAG of JSON events with deterministic state resolution, cryptographic signing, and eventually-consistent federation). The person asked sharp clarifying questions at each layer, demonstrating strong architectural intuition — notably pushing on what the server-side API actually does when messages are encrypted, leading to a detailed explanation of metadata vs. content separation and how custom unencrypted event types (e.g., `com.nomados.payment.split`) can coexist with encrypted chat in the same room.

The person also asked about Signal as a comparison point. Claude explained that while Signal is technically open source (AGPL-3.0, GitHub-published clients and server), it's a closed platform with no federation support, no extensibility primitives, massive infrastructure requirements (Kubernetes cluster, Cassandra, Kafka, Twilio dependency), and almost no self-hosting documentation — making it significantly harder to build on than Matrix. When the person explicitly deprioritized federation and asked which is easier to build, Claude confirmed Matrix is the clear choice: a working instance can be running within an afternoon via Docker, custom event types require no server changes, and the Application Service sidecar pattern enables coordination logic without touching homeserver code. The conversation closed with Matrix's adoption landscape — France (600k government officials on Tchap), Germany's Bundeswehr, UN, NATO, European Commission, and 25+ countries deploying it for digital sovereignty reasons — establishing that Matrix has strong institutional backing and is unlikely to disappear.

The architectural pattern that emerged for Nomad OS: run Tuwunel as the homeserver, fork Cinny as the frontend, build coordination logic as an Application Service sidecar that observes the Matrix event firehose and injects `com.nomados.*` custom state events, keeping encrypted `m.room.message` for private chat while coordination primitives (payments, trust attestations, token grants) flow as plaintext custom events the server can read and act on. The 64KiB per-event limit was noted as non-constraining for metadata payloads, with large attachments handled via `mxc://` media repo URIs.


---
**HUMAN** (2026-04-12T18:32):

Are there other open source projects like tinode? Are there better ui implementations?

---
**ASSISTANT** (2026-04-12T18:33):

The user is asking about open source projects similar to Tinode (a chat/messaging server) and whether there are better UI implementations. Let me search for current information.
```
This block is not supported on your current device yet.
```

Let me search more specifically for the UI quality comparison and newer alternatives.
```
This block is not supported on your current device yet.
```

Let me also search for Cinny and other nice Matrix clients since the user is asking about better UIs.
```
This block is not supported on your current device yet.
```

Good, I have enough info now. Let me give Ren a structured answer about Tinode alternatives, focusing on what matters for their context — they're building coordination infrastructure (Nomad OS, OpenClaw) so the protocol/architecture decisions matter more than just "which Slack clone."Good question, and it depends on what you're actually optimizing for. Tinode occupies a specific niche — lightweight, WhatsApp-like open source IM with a Go backend, designed as a modern XMPP replacement. Here's how the landscape breaks down:

**Closest architectural peers to Tinode:**

**Matrix/Synapse** is the most direct philosophical competitor — also aiming at federated, decentralized messaging as an open standard. It's far more mature in terms of ecosystem, with dozens of clients and bridges to other platforms. Matrix defines simple HTTP APIs so devs can write their own clients, bots, bridges, or servers without lock-in. The tradeoff is that Synapse (the reference homeserver) is a Python resource hog. **Conduit** and **Dendrite** are lighter-weight Matrix homeserver implementations in Rust and Go respectively — worth evaluating if you want Matrix protocol without the weight.

**Rocket.Chat** — offers real-time messaging, video calls, file sharing, omnichannel communication, and deep customization via source code access. More enterprise-oriented than Tinode. Has native Matrix federation now. The downside: Rocket.Chat has moved a lot of features to the enterprise version, and the community edition may not be sufficient for some use cases.

**Mattermost** — Slack-replacement energy, strong DevOps integrations, React frontend. The community open source version of Mattermost has no permissions system, so anyone can change or delete anything about any channel. That's a dealbreaker for most serious deployments.

**Zulip** — unlike Slack, Matrix, or XMPP where conversations are separated into channels, Zulip built threading as an initial design feature rather than bolting it on. Excellent for async-heavy distributed teams. Not really a WhatsApp-style IM though.

**On the UI question — this is where it gets interesting:**

Tinode's React web client is functional but pretty bare. **Cinny** (a Matrix client) is fast with a sleek UI, and probably what most people are looking for when they want a Discord-like alternative. It separates DMs from channels, shows only necessary information, and provides a calm, visually appealing environment. It's the best-looking open source chat UI I'm aware of right now.

**Element X** is the next-gen Element client using sliding sync and native performance — much better than old Element. There's also a fork of Cinny in Material UI with customizable CSS, support for polls and captions.

**For your context specifically** — if this is related to Nomad OS or the coordination layer you're building, the Matrix protocol is probably more interesting than any single client. It gives you federation, bridges, and the ability to write custom clients against a well-specified API. You could run Conduit as a lightweight homeserver and build a custom UI (or fork Cinny) that fits the "Pay → Split → Chat → Trust → Coordinate" flow without being locked into someone else's UX decisions.

---
**HUMAN** (2026-04-12T18:47):

Matrix/Synapse is interesting, how’s the scalability? Can I have a server that changes the messages, run hooks on messages, and then sync

---
**ASSISTANT** (2026-04-12T18:48):

Ren is asking about Matrix/Synapse specifically for:
1. Scalability
2. Server-side message manipulation (changing messages)
3. Hooks on messages
4. Syncing

This is clearly related to building coordination infrastructure. Let me search for current info on Matrix scalability and the application service / hook capabilities.
```
This block is not supported on your current device yet.
```

Now let me search for Matrix application services, hooks, and message modification capabilities.
```
This block is not supported on your current device yet.
```

Now I have a good picture. Let me also quickly search for Synapse modules since those are the actual mechanism for intercepting/modifying messages server-side.
```
This block is not supported on your current device yet.
```

Good, I have solid info now. Let me give a clear answer about scalability and the hook/message modification architecture.Okay, here's the real picture — there are three layers to understand and one important constraint.

**Scalability**

Synapse scales horizontally across multiple Python processes (called "workers"). This eliminates the single-process bottleneck, and the matrix.org homeserver itself runs this way. The architecture shards event persisters, sync handlers, federation readers, etc. into separate workers you can spread across machines.

That said, Element has been explicit that nation-scale deployments (millions of users) need Synapse Pro, which rewrites worker processes in Rust so each can use multiple CPU cores. Synapse Pro's memory footprint is 5x smaller than community Synapse, and it features automatic elastic scaling. Community Synapse is fine for thousands to tens of thousands of users, but Python + GIL is a real ceiling.

Worth noting: the Conduit family of native Rust homeservers has continued to expand — Conduit, Continuwuity, Grapevine, and Tuwunel. Tuwunel is now deployed at scale serving the citizens of Switzerland in production, with markedly reduced CPU usage. These are lighter alternatives if you don't need Synapse's full feature set.

**Hooks and message interception — here's the constraint**

You have three mechanisms, each with tradeoffs:

**1. Synapse Modules** (deepest access) — A module is a Python class that registers callbacks Synapse will call on specific operations. If a callback returns a value that should cause the event to be denied, Synapse will fail the operation. Spam checker callbacks let you intercept incoming events and reject them. You can also register custom web resources. But modules can **deny** events, not **modify** them in-flight. You'd need to deny + re-emit a transformed version, which is a hack.

**2. Application Services** (AS API) — Application services are passive and can only observe events from the homeserver. They can inject events into rooms they are participating in. They cannot prevent events from being sent, nor can they modify the content of the event being sent. So an AS sees everything (firehose of events via webhooks), can create virtual users, can send new messages, but can't intercept-and-transform.

**3. Hookshot** — supports generic webhook support so services can send messages into Matrix rooms without being aware of the Matrix protocol, transforming HTTP payloads into Matrix messages. Good for inbound integration but not for intercepting internal message flow.

**The fundamental architectural issue for what you're describing:**

Matrix events are immutable by design — once persisted, an event's content doesn't change (you can only "redact" or send a new event that references the old one via relations/edits). This is core to how federation and state resolution work. There's no middleware-style "transform this message before it hits the room" pipeline in the spec.

**What you'd actually do for your use case:**

If you control the server and clients, the pragmatic pattern is: use a Synapse module to intercept events pre-persistence (deny the raw event), process it through your hooks, then re-emit the transformed version via the module API or a bot user. This is hacky but works if you're not federating. Alternatively, treat the AS as a sidecar — let messages flow through normally, have the AS observe them, then emit derived/enriched events into separate rooms or threads that your custom client knows to display.

For the "Pay → Split → Chat → Trust → Coordinate" flow, honestly this might argue for running Matrix as the transport/sync layer but building your coordination logic as an AS that maintains its own state, rather than trying to make the homeserver itself do the transformation. The sync infra is where Matrix shines; the business logic lives outside it.

---
**HUMAN** (2026-04-12T18:53):

Great, what are the open source frontends that I can use or build upon

---
**ASSISTANT** (2026-04-12T18:53):

Ren wants to know about open source Matrix frontends/clients they can build upon. Let me search for the current landscape of Matrix clients, especially web and mobile ones that could be forked or used as a base.
```
This block is not supported on your current device yet.
```

Good info. Let me search specifically for Element X and the matrix-rust-sdk since those are the most modern options.
```
This block is not supported on your current device yet.
```

Good, I have a comprehensive picture now. Let me organize this for Ren, focusing on what's actually forkable/buildable for someone in their position.Here's the landscape organized by what you'd actually build on top of, given your stack and context:

**Tier 1: Best candidates to fork or build upon**

**Cinny** (React/TypeScript, Apache 2.0) — Provides a clean, user-friendly interface with organized navigation separating DMs from channels, adaptive input, and calm visuals. Uses matrix-js-sdk underneath. Lightest codebase of the serious web clients, single-file deployable as static assets. Best option if you want a clean React base to rip apart and rebuild with your own coordination UI on top.

**Element Web** (React/TypeScript, AGPL-3.0) — The glossy Matrix collaboration client for the web, with 12,967 stars. Most feature-complete but also the heaviest — Element Web is built on matrix-js-sdk which is 10 years old, uses 782MiB of memory, and takes almost 10 seconds to load. You'd inherit a lot of tech debt. AGPL means any modifications you serve must be open-sourced.

**FluffyChat** (Flutter/Dart, AGPL-3.0) — An open source, nonprofit Matrix client written in Flutter, aiming to be accessible for everyone. Uses the Dart Matrix SDK. Cross-platform (Android, iOS, web, desktop) from a single codebase. If you're considering Flutter for Nomad OS's mobile targets this is the strongest starting point.

**Ditto Chat** (React Native, GPL-3.0) — An attractive Matrix client built in React Native targeting Android, iOS, and web. If React Native is in your stack this could be interesting.

**Tier 2: Next-gen architecture (newer, more complex)**

**Element X iOS** (SwiftUI + matrix-rust-sdk, AGPL-3.0) and **Element X Android** (Jetpack Compose + matrix-rust-sdk, AGPL-3.0) — Element rebuilt their mobile apps from scratch, moving to a common Rust SDK foundation to reduce maintenance overhead while delivering a platform-native experience. These are the most performant Matrix clients that exist. They're dual-licensed — free under AGPL, or available under a commercial license from Element. The architecture is excellent but forking means maintaining Rust SDK bindings + native UI code.

**Aurora** (experimental, AGPL) — Element prototyped Element X Web using matrix-rust-sdk compiled to WebAssembly via UniFFI. It loads in less than a second (10x faster than Element Web) and uses 115MiB of memory (6.8x less). Very early but this is where the web is heading — Rust SDK via WASM rather than the legacy JS SDK.

**Tier 3: SDKs to build from scratch**

The matrix-rust-sdk has bindings to Swift, Kotlin, WebAssembly, Go and more. It handles encryption, syncing, room state, event cache. There's also a Dart SDK, Python asyncio framework (mautrix), Go framework (mautrix-go), and Kotlin multiplatform SDK (Trixnity).

**My read for your use case:**

If the coordination layer is the product and chat is the transport, I'd start with **Cinny** as the fork base. It's React (you know it), Apache 2.0 (no AGPL copyleft constraints), clean architecture, and light enough to surgically replace the chat-centric UI with your payment/split/trust flows while keeping Matrix sync underneath. FluffyChat is the runner-up if you want Flutter's cross-platform story for the SE Asia mobile-first market.

The Element X / Rust SDK path is technically superior but the AGPL licensing and architecture complexity is a heavy lift for a solo dev — better suited once you've validated the product shape with a lighter fork.

---
**HUMAN** (2026-04-12T18:57):

How about backends?

---
**ASSISTANT** (2026-04-12T18:58):

Ren is asking about Matrix homeserver backends - the server-side implementations they could use or build upon. Let me search for the current state of Matrix homeserver implementations beyond Synapse.
```
This block is not supported on your current device yet.
```

Now let me also check for the TypeScript-based Transform homeserver, since that could be interesting for Ren.
```
This block is not supported on your current device yet.
```

Great, I have a comprehensive picture now. Let me organize this for Ren.Here's the backend landscape, from production-ready to experimental:

**The Big Four**

**Synapse** (Python/Twisted + Rust, AGPL-3.0) — 86.3% of all federated Matrix servers run Synapse. Most feature-complete, best tested, most ecosystem support. Horizontal scaling via workers. The downside you already know: Python + GIL, heavy memory footprint. Synapse is moving its build backend from poetry-core to maturin, allowing first-class Rust module interfacing. So the Python/Rust boundary is tightening. The module system we discussed earlier is Synapse-specific — it's the only backend with that deep hook architecture.

**Dendrite** (Go, AGPL-3.0) — Second-generation homeserver written in Go, with 100% server-server parity with Synapse and 93% client-server parity. Much lighter than Synapse. But: The Matrix.org Foundation is not able to resource maintenance of Dendrite and it continues to be developed by Element on a best-effort basis. Element maintains it, but it's no longer actively resourced by the Foundation. Good for small deployments (10s-100s of users), has a microservices-capable "polylith" mode, but you'd be building on a project with uncertain long-term investment.

**Tuwunel** (Rust, Apache-2.0) — This is the interesting one. A Matrix homeserver written entirely in Rust, designed as a high-performance enterprise-ready alternative to Synapse. Official successor to conduwuit, which was a fork of Conduit. Used by companies with full-time staff, primarily sponsored by the government of Switzerland where it's currently deployed for citizens. Single binary, low resource usage, already running on 2.7% of federated servers and growing. Apache-2.0 licensed — no copyleft. The codebase is modular with seven internal crates and clean dependency boundaries.

**Continuwuity** (Rust, Apache-2.0) — A community-driven second-degree fork of Conduit focusing on user experience and new features. Running on 2.5% of servers. Volunteer-maintained, so there's some community tension between this and Tuwunel about which fork to follow.

**The Experimental / Niche Ones**

**Cloudflare Workers homeserver** (TypeScript, open source) — This is wild. Someone ported the core Matrix protocol logic — event authorization, room state resolution, cryptographic verification — to TypeScript using the Hono framework, with D1 replacing PostgreSQL, KV replacing Redis, R2 replacing the filesystem, and Durable Objects handling real-time coordination. Usage-based costs mean low-traffic homeservers cost just pennies, and when a user in Tokyo sends a message, the Worker executes in Tokyo. Early proof-of-concept but architecturally fascinating for your SE Asia deployment context.

**hghs** (TypeScript, pure Node) — A zero-dependency Matrix homeserver written in pure TypeScript, intended for special use cases when Matrix protocol is used as a backbone for custom apps. Compiles as a single standalone JavaScript file with NodeJS as the only runtime dependency. Only implements a subset of the spec. Designed for serverless/embedded. This is closest to what you'd build if you wanted Matrix-as-transport without the full homeserver weight.

**Transform** (TypeScript/Redis) — Built with TypeScript and Redis, using Redis streams for room timelines and SQLite/Postgres for relational data. Abandoned since 2018, but architecturally interesting as a reference for how you'd build a minimal TS homeserver.

**My take for your situation:**

If you need production Matrix compatibility (federation, bridges, ecosystem clients), **Tuwunel** is the pick — Rust, Apache-2.0, single binary, low resources, government-backed development, and it'll run beautifully on a Singapore VPS or edge nodes. No module system like Synapse though, so your hooks would need to be Application Services or a sidecar pattern.

If you're thinking about Matrix-as-protocol-backbone rather than Matrix-as-full-chat-system — where the homeserver is just the sync/persistence layer and your coordination logic lives elsewhere — the **hghs** approach is worth studying. You could build a minimal TypeScript homeserver that implements just enough of the spec for your Cinny fork to connect, while your payment/trust/coordination layer runs alongside it with full control over message flow. That's more aligned with the SST architecture where you're defining your own primitives anyway.

The Cloudflare Workers approach is worth bookmarking for later — if Nomad OS scales across SE Asia, edge-deployed Matrix with zero ops overhead is compelling, but it's too early to bet on right now.

---
**HUMAN** (2026-04-12T19:03):

No module system like Synapse though, so your hooks would need to be Application Services or a sidecar pattern.
Explain

---
**ASSISTANT** (2026-04-12T19:03):

Ren wants me to explain what I mean by the sidecar pattern vs Application Services for hooks in the context of Tuwunel (or any non-Synapse homeserver). This is an architecture question, not a search question.Three patterns for running custom logic against Matrix events, from tightest coupling to loosest:

**1. Synapse Modules (Synapse only)**

Your Python code runs *inside* the homeserver process. The homeserver calls your callback before/during event processing — you can deny events, inspect them, trigger side effects, all in the same execution context. Like middleware in Express. This doesn't exist in Tuwunel/Dendrite/Conduit because it's a Synapse-specific plugin API, not part of the Matrix spec.

**2. Application Services (any homeserver)**

Part of the Matrix spec. The homeserver pushes events to your service via HTTP webhooks after they're persisted. Your AS registers interest in certain rooms/users/aliases, and the homeserver POSTs batches of events to your endpoint. You can then react — send new messages, create rooms, manage virtual users — but you're always *reacting after the fact*. You can't block or transform an event before it hits the room. It's the specced way to extend Matrix, so it works with any compliant homeserver including Tuwunel.

**3. Sidecar pattern**

This isn't a Matrix concept — it's an architecture pattern. Your coordination service sits alongside the homeserver as a separate process. It could work several ways:

- **Client-side interception**: Your custom frontend talks to your sidecar *first*, the sidecar processes the message (adds metadata, runs validation, triggers payment logic, whatever), then the sidecar forwards it to the homeserver via the client-server API as a bot user. The homeserver never sees the raw user input — it only sees what your sidecar decided to emit.

- **Reverse proxy interception**: You put a proxy (nginx, Caddy, your own code) in front of the homeserver's client-server API. Incoming requests hit your logic first. You can rewrite, reject, enrich, or reroute before passing through to the homeserver. Downside: you're now maintaining compatibility with the Matrix client-server API surface, which is large.

- **Event sourcing off the sync stream**: Your sidecar connects to the homeserver as a privileged client, consumes the /sync stream, and maintains its own derived state. It doesn't intercept — it shadows. When it needs to act, it sends events back through the normal API.

**For the coordination layer you're building**, the pragmatic setup on Tuwunel would be: AS for observing all events (firehose), sidecar for injecting your coordination logic (payment splits, trust scores, whatever), and your Cinny fork talks to both the homeserver (for sync/display) and your sidecar (for actions that need processing before they become Matrix events). The homeserver stays dumb transport; your sidecar is where the SST logic actually lives.

---
**HUMAN** (2026-04-12T19:05):

Explain matrix protocol itself

---
**ASSISTANT** (2026-04-12T19:06):

Ren wants to understand the Matrix protocol itself - the underlying spec, not the implementations. This is a foundational knowledge question that I can answer well from training data. No need to search.Matrix is a spec for decentralized, eventually-consistent replication of JSON event graphs over HTTP. That's the core of it. Everything else — chat, VoIP, E2EE — is built on top of that primitive.

**The fundamental data structure**

A room is a directed acyclic graph (DAG) of events. Each event is a JSON object with a type, content, sender, room ID, timestamp, and crucially — references to parent events (the `prev_events` field). This makes every room a Merkle-like DAG, not a linear log. Two servers can independently append events and later reconcile, just like Git branches.

Events come in two kinds: **state events** (key-value pairs that define the room's current configuration — name, topic, membership, power levels, join rules) and **message events** (ephemeral content — text messages, images, reactions, etc). State events have a `state_key` field that together with the event `type` forms a unique key. The "current state" of a room is the resolved set of the latest state events at any given point in the DAG.

**State resolution**

When the DAG forks (two servers emit events concurrently without seeing each other's), the room state diverges. When events reconnect the graph, the servers need to agree on what the room state actually is. This is **state resolution** — Matrix's consensus algorithm. It's deterministic: given the same set of events, all servers will compute the same resulting state. Version 2 (used in all modern rooms) resolves conflicts by power level, then by event timestamp, then lexicographically by event ID. It's not BFT consensus — it's a conflict resolution function over an eventually-consistent replicated data structure.

**Federation (server-server API)**

Every user belongs to a homeserver (`@user:server.example`). When a room has members from multiple servers, those servers federate — they push events to each other via the server-server API (also called the Federation API). This works like:

- Server A creates an event, signs it with its Ed25519 key, and sends it to all other servers that have users in the room
- Receiving servers verify the signature, check the event is authorized (by running it against the room's current power levels, join rules, etc.), and persist it into their local copy of the DAG
- If they missed events (gaps in `prev_events`), they backfill by requesting the missing events from the sending server

Every event is cryptographically signed by the originating server. Events reference their parents by hash. This means the DAG is tamper-evident — you can verify the integrity of any event chain. Federation is fire-and-forget with retries; servers queue events for unreachable peers and retry later.

**Authorization rules**

Each event type has authorization rules checked against the room state at the point of insertion. For example: can this user send messages? (Check their power level against the `events_default` or specific event type power level.) Can this user invite? Can they change the room name? These rules are evaluated locally by each server — there's no central authority. The rules are deterministic, so all servers reach the same conclusion about whether an event is allowed.

**Client-server API**

This is just REST/JSON over HTTP. Clients authenticate with access tokens, send events via `PUT /rooms/{roomId}/send/{eventType}/{txnId}`, and receive events via **sync**. The sync endpoint (`/sync`) is a long-poll (or sliding sync in Matrix 2.0) that returns all new events, state changes, and ephemeral data (typing notifications, read receipts) since the client's last sync token. The homeserver maintains per-device sync state.

**Rooms as the universal container**

Everything is a room. A DM is a room with two members. A group chat is a room. A "Space" is a room whose state events reference child rooms (like a folder). A VoIP call is signaled via events in a room. Even account data and presence are room-like constructs. This is the key architectural insight — rooms are the universal replicated container, and the protocol doesn't care what you put in them.

**End-to-end encryption (Megolm/Olm)**

E2EE is a layer on top. Message content is encrypted client-side using Megolm (a ratcheting group encryption protocol). Key exchange between devices uses Olm (Double Ratchet, like Signal). The homeserver stores and replicates ciphertext — it never sees plaintext. Device keys are published to the homeserver and cross-signed for verification. This is why the AS/module approach can't transform encrypted message *content* — the server literally doesn't have access to it.

**Identifiers**

Everything follows a `sigil:localpart:server` pattern: `@user:example.com`, `!roomid:example.com`, `#alias:example.com`. Room IDs are opaque and permanent; aliases are human-readable and mutable. Event IDs in modern room versions are the hash of the event content (`$base64hash`).

**What this means for what you're building**

The protocol is essentially a replicated event store with deterministic conflict resolution and cryptographic integrity. If you squint, rooms are very close to your SST Spaces — containers with membership, permissions, and an append-only event log. The Token concept maps loosely to power levels + event types (capability pointers). The Sprite concept maps to Matrix user IDs + device keys.

The main friction point for your use case: Matrix events are immutable and the DAG structure assumes append-only semantics. You can't retroactively modify the graph. Edits are new events that reference old ones. This is great for integrity and auditability but means your coordination logic has to work with event streams rather than mutable state — which is actually well-suited to an event-sourcing architecture where your sidecar maintains derived mutable state from the immutable Matrix event log.

---
**HUMAN** (2026-04-12T19:14):

If messages are encrypted, what does server aPi do

---
**ASSISTANT** (2026-04-12T19:14):

Ren is asking a sharp question - if E2EE means the server can't read message content, what's the point of the server-side APIs? What does the server actually do?Good question. The server handles everything *except* reading message content.

**What the server still does with encrypted messages**

The ciphertext is just the `content` field of the event. All the metadata is plaintext and the server operates on it:

- **Routing**: The server knows the room ID, sender, event type (`m.room.encrypted`), timestamps, and `prev_events` graph references. It knows *who* sent *something* to *which room* at *what time* — just not what they said.
- **DAG maintenance**: Ordering events, maintaining the `prev_events` graph, running state resolution, backfilling gaps over federation. The integrity of the DAG doesn't depend on reading content.
- **Authorization**: Power levels, membership, join rules, bans — these are all **state events that are NOT encrypted**. The server can still enforce "does this user have permission to send events in this room." It just can't inspect what they're sending.
- **Storage and delivery**: The server persists ciphertext blobs and delivers them via `/sync` to recipient devices. It's a dumb pipe for content, but a smart pipe for routing.
- **Device and key management**: Olm/Megolm key exchange happens via the server. Devices upload their identity keys and one-time keys to the homeserver (`/keys/upload`). Other devices query those keys (`/keys/query`). The server brokers the key exchange but doesn't have the private keys — it's like a key directory.
- **Notifications and push**: The server can't read the message, but it knows a new event arrived in a room. It pushes a notification to your device saying "new message in Room X from @alice." Your device then decrypts locally and shows the preview.
- **Read receipts, typing indicators, presence**: These are ephemeral events, sent in plaintext. The server knows you're typing, knows you read up to event X, knows you're online. This is metadata, not content.
- **Search**: This is where it breaks. Server-side search doesn't work on encrypted rooms — the server can't index what it can't read. Clients have to search locally. The matrix-rust-sdk is building client-side search for exactly this reason.

**What's encrypted vs. what's not**

Think of it as two layers in the same room:

- **Plaintext on the server**: Room membership, power levels, room name/topic (unless the room encrypts state events, which is experimental), join/leave/invite events, all event metadata (sender, timestamp, room, graph position), typing/receipts/presence, device keys
- **Encrypted (server sees ciphertext only)**: The `content` field of `m.room.encrypted` events — the actual message body, images, file attachments, reactions, edits

**The implication for your hooks**

Your AS or sidecar running server-side can still do a lot with encrypted rooms: observe membership changes, track which rooms are active, see who's talking to whom and when, enforce rate limits, manage invites, maintain room topology. You just can't inspect or transform message *content*.

This is actually fine for a coordination layer. Payment splits, trust graph updates, group membership changes — these can all be custom state events or unencrypted event types in their own rooms/spaces. Only the private chat content needs E2EE. You control the schema. You could define `com.nomados.payment.split` as an unencrypted event type that your sidecar processes, while `m.room.message` stays encrypted for private chat. The protocol doesn't force you to encrypt everything — it's per-room and per-event-type configurable.

---
**HUMAN** (2026-04-12T19:18):

So I can still attach unencrypted metadata? Any limit?

---
**ASSISTANT** (2026-04-12T19:19):

Ren is asking about attaching unencrypted metadata to events in Matrix, even in encrypted rooms. Let me search for specifics on this.
```
This block is not supported on your current device yet.
```

Good, I have comprehensive info. Let me give a clear answer.Yes, and this is where it gets powerful for your use case.

**Custom event types are first-class citizens**

Events are not limited to the types defined in the specification. New or custom event types can be created on a whim using the Java package naming convention. Server implementations must tolerate unknown event types and allow them to be passed between clients.

So you can send events like `com.nomados.payment.split`, `com.nomados.trust.attestation`, `com.nomados.token.grant` — whatever you want. The server will store them, replicate them over federation, include them in `/sync`, and your AS can observe them. The server doesn't care what's inside.

**Encryption is per-event-type, not per-room**

A room being "encrypted" means the client encrypts `m.room.message` events. Your custom event types don't have to follow that. You can send `com.nomados.payment.split` as plaintext in the same room where chat messages are encrypted. The server sees your coordination events in full, your sidecar/AS processes them, and private chat stays private. You control this in your client code — it's the client that decides what to encrypt before sending.

**The hard limit**

The complete event must not be larger than 65,536 bytes when formatted with the federation event format, including signatures, and encoded as Canonical JSON. The sender must not exceed 255 bytes. That's 64KiB per event total. Beyond the sender limit, additional keys have no limit other than that implied by the total 64KiB limit on events.

64KiB is generous for metadata. A payment split with participants, amounts, currency, memo, hash references — you'd struggle to fill that. If you need to attach larger payloads (receipts, documents), you'd upload to the media repo and reference the `mxc://` URI in the event.

**State events vs. message events — this matters**

You can make your custom types either:

- **State events** (with a `state_key`): These persist as the "current state" of the room. Only the latest event per `(type, state_key)` pair is the "active" one. Good for things like "current trust score for user X" or "active payment config for this group." Your sidecar can query current room state without scanning the full timeline.

- **Message events** (no `state_key`): These append to the timeline. Good for individual transactions, attestations, activity events. They accumulate in the DAG.

**No rate limits in the spec itself** — but homeserver implementations may impose their own. Synapse has configurable rate limits on event sending. Tuwunel has its own. For your own server you'd configure these to suit your throughput needs.

So the architecture for Nomad OS on Matrix looks like: encrypted `m.room.message` for private chat, plaintext custom state events for coordination primitives your server-side logic can read and act on, all in the same room, all replicated through the same DAG. Your Cinny fork renders both. Your AS/sidecar processes the coordination events. The homeserver is the dumb replicated event store, which is exactly what you want it to be.

---
**HUMAN** (2026-04-12T19:24):

How about signal? Is it also open source?

---
**ASSISTANT** (2026-04-12T19:24):

Ren is asking about Signal's open source status. Let me search for current info since things may have changed.
```
This block is not supported on your current device yet.
```

Good info. Let me summarize for Ren.Yes, but it's a very different kind of open source than Matrix. The distinction matters for what you're building.

**What's open source**

Everything is on GitHub under AGPL-3.0: the Android client (Kotlin), iOS client (Swift), Desktop client (Electron), and the server (Java/Spring Boot). The Signal Protocol itself is implemented in `libsignal`, a Rust library also open source.

**Why it doesn't help you**

Signal is a closed platform — users can't self-host a Signal server and expect to talk to other Signal users. Federation is not supported. Your self-hosted Signal server is an island. No one on the real Signal network can reach you, and you can't reach them.

Self-hosting the entire service is almost impossible due to the documentation's limited availability, the stack's complexity, and the options to customize. The infrastructure footprint is massive: Kubernetes 1.27+ with at least 6 worker nodes (8 vCPU / 32GB each), Cassandra in multi-DC, Redis cluster, Kafka, S3 storage, Twilio for SMS verification. This is enterprise cloud infra, not something you run on a Singapore VPS.

libsignal is published under AGPL-3.0, meaning every software that uses it must be published under the same license. The library is designed purely for the Signal ecosystem and types and structures seem suited only for it.

Signal has a history of going months without updating its public server repository, and there was a period where it stopped updating entirely. The code is technically open but the project doesn't prioritize third-party deployments.

**Signal vs Matrix — the philosophical divide**

Signal optimizes for *one thing*: private messaging between individuals, with minimal metadata. The server is deliberately dumb — it doesn't know who's talking to whom (sealed sender), stores almost nothing, and the protocol is designed so you don't need to trust the server at all.

Matrix optimizes for *extensibility*: federation, custom event types, bridging, Application Services, bots, Spaces, custom clients. The server is a rich replicated event store you can build on top of.

Signal is a product. Matrix is a protocol.

For Nomad OS, Signal gives you nothing useful — no federation, no custom events, no extensibility, no way to build coordination primitives on top of the transport, AGPL lock on libsignal, and a deployment stack that assumes AWS-scale infra. The Signal Protocol itself (Double Ratchet) is interesting cryptography and Matrix actually uses similar primitives (Olm is based on Double Ratchet), so you already get the good parts of Signal's crypto through the Matrix ecosystem without the platform lock-in.

---
**HUMAN** (2026-04-12T19:25):

Let’s not weight federation, which one is easier to build?

---
**ASSISTANT** (2026-04-12T19:26):

Ren is asking which is easier to build on top of if you ignore federation. This is a pragmatic question about developer experience and time-to-working-product.Matrix, and it's not close.

**Signal's build problem**

You need to stand up: a Java/Spring Boot server, Cassandra cluster, Redis cluster, Kafka, S3-compatible storage, Twilio or equivalent SMS provider for phone number verification (Signal requires phone numbers — no usernames-only auth), contact discovery service (originally ran in Intel SGX enclaves), push notification infrastructure for both APNs and FCM. Then you fork the Android (Kotlin) and iOS (Swift) clients separately, repoint them at your server, and rebuild. Two native codebases, no web client that works standalone, no shared SDK across platforms.

The server has almost no documentation for self-hosters. The API isn't designed to be extended — there are no custom event types, no hooks, no plugin system. It does one thing: relay encrypted message envelopes between phone numbers. Adding a payment split event type means forking the server and the clients and maintaining your own protocol divergence forever.

**Matrix's build path**

`docker run` a Tuwunel or Synapse container. Point Cinny at it. You have a working chat app. Add custom event types by just sending JSON with your own `com.nomados.*` types — no server changes needed. Build your coordination sidecar as an Application Service that registers with the homeserver in a YAML file. One web codebase (React) that works on mobile browsers too, or fork FluffyChat for native Flutter.

The protocol is documented exhaustively — the spec is public, versioned, with hundreds of pages of detail on every endpoint. Multiple SDKs in every language. Multiple server implementations to choose from. The entire system is designed for people to build custom things on top of it.

**Concretely, time to first custom feature**

Signal: weeks of infra setup before you can even send a message, then you're forking Java server code and two native clients to add anything beyond basic chat.

Matrix: afternoon to get chat working, then you're writing a small Node/Python AS or tweaking your Cinny fork's React components to render your custom event types. The server never needs to be touched.

If you're a solo dev with AI tooling building a coordination layer where chat is the transport, Matrix is the obvious choice. Signal is a fortress designed to keep everyone out, including you.

---
**HUMAN** (2026-04-13T05:13):

Who’s using matrix

---
**ASSISTANT** (2026-04-13T05:14):

The user wants to know who's using Matrix in production. Let me search for current notable deployments.
```
This block is not supported on your current device yet.
```

Good results. Let me synthesize the key deployments.The adoption is heavily government/public sector driven, and accelerating fast.

**Governments (nation-scale)**

France runs Tchap, used by more than 600,000 public officials for secure instant messaging. France's digital directorate (DINUM) became the first country to join the Matrix Foundation as a paying member.

Germany's Bundeswehr (armed forces) communicates and shares classified documents on a private Matrix network using BwMessenger. Germany's national healthcare system uses a Matrix-based system (TI-Messenger) for real-time communication among healthcare organizations and sharing sensitive patient data, developed by Gematik. Two German states run their own Matrix networks for schools — Rhineland-Palatinate's SchulchatRLP is sized for half a million pupils.

Luxembourg developed Luxchat4Gov for government officials. Sweden's Social Insurance Agency (Försäkringskassan) is building SAFOS, a Matrix-based service aimed at becoming a national standard for secure messaging across Swedish public sector.

The United Nations uses Matrix as the basis of its own air-gapped communications tool to remain independent of any country or hosting provider. The International Criminal Court is switching to it after losing access to Microsoft services due to US sanctions.

Over 25 countries are actively deploying Matrix for digital sovereignty. At the 2025 Matrix Conference, the European Commission, France, Germany, Luxembourg, NATO, Sweden, the United Nations, and the European Space Agency all presented on their deployments.

**Open source / tech community**

Mozilla replaced its IRC infrastructure with Matrix in 2020. FOSDEM has used Matrix since 2021. KDE, GNOME, and many open source projects use it as their primary chat. Thunderbird has had native Matrix support since version 102.

**The pattern**

The driver everywhere is digital sovereignty — organizations that can't afford to depend on US cloud providers for their communications. The Ukraine situation, Trump-era sanctions, and AWS outages taking down Signal/Slack/Zoom simultaneously all accelerated this. Matrix is currently talking to roughly 35 countries about FOSS communications infrastructure.

**What this means for you**

Matrix isn't a niche hobby project. It's becoming critical infrastructure for nation-states. That means the protocol will continue to be funded, the spec will keep evolving, and the ecosystem won't disappear. Building on it is a bet with strong institutional backing — which is unusual for open source protocols. The 706 network and Nomad OS would be riding a wave that governments are already validating at scale.
