# Open source messaging UI research

created: 2026-04-17T11:58:52.117519Z  uuid: 8d4ce1a4-d82e-4b41-a689-4360779f8c31  export: new
messages: 6  total_chars: 34242  human_chars: 289


---
**HUMAN** (2026-04-17T11:58):

i want to research on existing open source messaging ui, and solutions for messaging app

---
**ASSISTANT** (2026-04-17T11:59):

  The user is looking to integrate messaging capabilities into their Nomad OS project, which includes a chat component in its workflow. I should help them explore open source messaging UI libraries and backend solutions like Matrix or Rocket.Chat, plus consider end-to-end encryption options for their needs.

Before diving into broad research, I should clarify what matters most for their use case—whether they need just UI components or full backend solutions, if self-hosting is preferred, what platforms they're targeting, and how this integrates with their existing Nomad OS architecture. This will help me give them focused recommendations rather than generic options. I'll search across open source messaging UI libraries, chat backends like Matrix and Rocket.Chat, E2E encryption approaches, and embeddable SDK solutions to give them a comprehensive picture of what's available.Before I dive in — quick scoping so the research lands where you need it:
```
This block is not supported on your current device yet.
```



---
**HUMAN** (2026-04-17T12:01):

Q: What layer matters most for Nomad OS chat?
A: All of the above — comprehensive map

Q: Hard requirements? (Select all that apply)
A: Group chat / channels

---
**ASSISTANT** (2026-04-17T12:03):

  They're looking for a comprehensive landscape view across UI, backend, and full-stack solutions, with group chat and channels as the core requirement. I have flexibility to explore broadly. Let me map out the research approach: I'll cover UI libraries like React, React Native, Flutter, and Vue, then look at existing chat SDKs and UI kits from providers like Stream Chat, Sendbird, and open-source options.

For the backend, I'm examining self-hosted servers across different protocols — Matrix, XMPP, and modern alternatives like Rocket.Chat, Mattermost, Zulip, and some newer projects. Then I'll look at full-stack solutions that bundle everything together, plus embeddable SDKs for developers who want to integrate chat into existing apps. Let me start searching for the current state of these tools.Got it — comprehensive map, group chat is the must-have. Let me research the current landscape.
```
This block is not supported on your current device yet.
```

 Now I'm looking into embeddable chat SDKs and UI libraries that work with React and React Native.
```
This block is not supported on your current device yet.
```

 I should also look into what Flutter chat UI libraries are available, since Ren has been working with Flutter and might want to explore other options in that ecosystem.
```
This block is not supported on your current device yet.
```

 I'm looking into Matrix and Element as protocol options, then exploring more decentralized alternatives like SimpleX, Tinode, and Berty.
```
This block is not supported on your current device yet.
```

 I should look into some decentralized and peer-to-peer messaging platforms like SimpleX, Tinode, Berty, and Nostr, along with more recent options like Briar that might offer better privacy and autonomy.
```
This block is not supported on your current device yet.
```

 I'm organizing a comprehensive map based on Ren's context with Nomad OS and their focus on building a super-app for digital nomads, considering their work with Flutter and OpenClaw agents. The key areas I'm mapping out are the UI layer with drop-in components that work across different frontend frameworks, along with the other architectural pieces that would support their platform.

I'm thinking through how to present this research—it needs clear structure and depth without over-formatting, so I'll use inline prose with headers rather than heavy bulleting, since the breadth of options across multiple tiers calls for readable organization. me structure helps. I'll use level-2 headers for tiers and brief descriptions per option, with a comparison-oriented framing.

Let me draft the response:

---

# Open source messaging — landscape map (April 2026)

I'll group this by tier, give the live options in each, and end with the Nomad OS-specific call.

## 1. UI-only libraries (you bring the backend)

These are pure frontend kits. You wire them to whatever transport you want (Matrix, custom WebSocket, Firebase, whatever).

**Web / React**
- **stream-chat-react** — Stream's open-source React component library. Deep, polished, production-grade — channel list, message list, threads, reactions, typing, read receipts. The catch: optimized for Stream's hosted backend; if you go off-Stream you're rewriting a lot. But the code is MIT, so you can study or fork.
- **chatscope/chat-ui-kit-react** — Lightweight, BSD-licensed pure UI kit. No backend assumptions. ~3.7k stars, used widely as a starting shell. Comes with a hook for managing chat state.
- **assistant-ui** / **NLUX** — Built for AI chat and LLM-style streaming rather than traditional human messaging, worth considering if you're thinking about blending nomad chat with an AI agent interface.

**Flutter (most relevant given your current stack)**
- **flutter_chat_ui (Flyer Chat)** — The standout option here. Apache 2.0, backend-agnostic, modular packages for different message types, and works across iOS, Android, Web, and desktop. Still actively maintained through late 2025 with support for composer, threading, custom message types, and streaming markdown for AI agents. This is the natural choice if you're staying in Flutter.
- **flutter_firebase_chat_core** — Firebase-backed companion if you want a quick prototype without managing your own backend.

**React Native**
- **react-native-gifted-chat** — The long-standing default option, still maintained but showing its age.
- **flyer.chat for React Native** — Same team as the Flutter version, React Native flavor.
- **stream-chat-react-native** — Same tradeoffs as the web version.

## 2. Backend / protocol — self-hostable servers

You run the server, plug any client (custom or off-the-shelf).

**Matrix (Synapse / Dendrite / Conduit / Tuwunel)**
The federated, E2E-by-default protocol. Synapse is the reference Python server—heavy but feature-complete with all bridges. Dendrite is the Go rewrite, and Conduit/Tuwunel is the Rust performance fork now running in production at Swiss government scale. Massive ecosystem with matrix-react-sdk and matrix-js-sdk as the canonical web clients.

The matrix-rust-sdk has Swift, Kotlin, Wasm, and Go bindings, so you can embed Matrix client logic into basically any app. The honest tradeoff: Matrix is the most powerful option but also the heaviest—operationally non-trivial, room state can balloon, and federation adds complexity.

**XMPP (ejabberd / Prosody)**
The original protocol, battle-tested at WhatsApp scale back when WhatsApp ran on ejabberd. Lightweight and federated, but the spec is fragmented across XEPs and the developer experience feels dated. Still solid if you want lean and don't need modern polish.

**Tinode**
Go-based "modern XMPP replacement" with mobile-first design, gRPC and WebSocket support, and Swift/Java/JS clients built in.

Tinode has a smaller community but is cleanly engineered—a good middle ground if Matrix feels too heavy.

**SimpleX**
The novel one: no user IDs at all, relays are just dumb message-passers, and identity lives in pairwise queues. Self-hostable, recently added groups and calls, with a genuinely unique privacy model. The tradeoff is that groups are still maturing, the ecosystem is small, and the no-identity approach can confuse regular users.

**Full-stack solutions (UI + backend bundled)**
Drop-in or fork-and-customize options.

**Rocket.Chat** — Node/MongoDB-based, the most flexible option with customizable everything, an Apps Engine for plugins, native Matrix federation, and omnichannel support for SMS, email, and social integrations.  Used by Deutsche Bahn and several governments, though it has a heavier resource footprint and recently shifted toward dual-licensing, so worth checking the LICENSE file.

**Mattermost** — Go backend with React frontend, a polished Slack clone that's lighter than Rocket.Chat and strong for DevOps/ChatOps workflows. Community edition is MIT, but enterprise features like SSO and compliance tools are behind a license.

**Element** — The reference Matrix client, so if going with Matrix, Element Web or the newer Element X (Rust SDK rewrite for mobile) are the natural starting points, though you can also fork or use other clients.

**Zulip** — Threaded by default with topics-within-streams, making it best-in-class for async distributed teams, though less general-purpose for consumer messaging.

**Revolt** — A Discord-style open-source option with a Rust backend, channels, and voice support, though it's younger with a smaller community.

**Chatwoot** — Built for customer support on a Rails+Vue foundation, solid if that's the shape you need.

Now looking at the decentralized, protocol-first options that align more with sovereign and fork philosophies. Matrix stands out as the most production-ready federated chat system.

Beyond that, there's **Nostr**, which isn't really a chat protocol itself but rather a primitive for signed events broadcast over relays—several chat implementations exist on top of it (NIP-17 for private DMs, NIP-29 for relay-based groups), though the ecosystem remains fragmented. **SimpleX** offers the most novel privacy model. **Berty** uses P2P over libp2p and can work without internet via Bluetooth or local mesh, making it interesting for nomadic contexts with spotty connectivity. **Briar** takes an activist-grade approach with Tor, Bluetooth, and WiFi-direct—no servers required, though group functionality is limited. **Bitchat** operates as a pure Bluetooth mesh network.

For Nomad OS, the chat layer really needs to serve the coordination arc—group threads anchored to specific contexts like payment splits or trips, embedded directly in the app rather than as a separate client, self-hostable so you own the identity layer, and not necessarily end-to-end encrypted if the trust model is "we run the relay and the value-add is coordination." Three realistic approaches emerge: **Path A** involves running a Matrix backend like Synapse with a custom UI for maximum sovereignty. Path C makes sense if chat is really just a feature layered on top of your coordination model rather than the core product—you'd build a thin backend that treats messages as events within your existing Space/Token architecture, avoiding the overhead of rebuilding presence, sync, and multi-device support that Matrix handles for you. Given your SST thinking, this might actually align better than trying to force a general-purpose chat system into your domain.

I'm wondering whether to dig deeper into the Matrix embedding specifics, compare the operational complexity of Tinode versus Rocket.Chat, or sketch out what it'd actually look like to expose chat as a view over your event substrate. I'm thinking through whether citations are needed here. Most of what I'm covering is general knowledge about these projects, but specific recent claims like production deployments should be sourced. Let me add citations for the load-bearing facts and keep the rest as paraphrased context, then rewrite this as flowing prose rather than bullets.

For Flutter, **flutter_chat_ui** from Flyer Chat stands out as the strongest open-source option — it's Apache 2.0, backend-agnostic, modular, supports all six platforms, and has maintained active releases through late 2025, with **flutter_firebase_chat_core** available if you want Firebase integration for quick prototyping. On the React side, **stream-chat-react** is polished and feature-complete but tightly coupled to Stream's backend (though the MIT license lets you fork and rewire it), while **chatscope/chat-ui-kit-react** is lighter and fully backend-agnostic with built-in state management. For React Native, **react-native-gifted-chat** remains the standard but is fairly minimal in features.

If the chat interface needs to double as an AI agent surface, **assistant-ui** and **NLUX** are purpose-built for streaming LLM messages rather than peer-to-peer chat, though that distinction is increasingly blurred. On the backend side, **Matrix** is the federated, E2E-encrypted heavyweight with three main server implementations — Synapse (the Python reference, feature-rich but resource-heavy), Dendrite (Go rewrite), and Rust variants like Conduit and Tuwunel, which is already running in production for Switzerland's citizens.

The matrix-rust-sdk has bindings across Swift, Kotlin, Wasm, and Go, so embedding Matrix client logic into any platform is feasible, though the operational overhead is real — room state can balloon, federation adds complexity, and hiding the `@user:server` format from users takes work. **XMPP** remains the battle-tested, lightweight federated option used at WhatsApp scale, though the spec is fragmented across XEPs and the developer experience feels dated. **Tinode** offers a modern Go-based alternative with gRPC and WebSocket support, mobile-first design, and native Swift/Java/JS clients, but has a smaller ecosystem behind it.

**SimpleX** stands out for its novel approach — no user IDs, just per-pair message queues with dumb relays — giving it a strong privacy story and self-hosting capability, though groups are still maturing and the identity model requires more onboarding friction. **Rocket.Chat** is the most feature-rich full-stack option with Node/MongoDB, a plugin engine, native Matrix federation, and omnichannel bridges to SMS and social platforms, making it popular with enterprises like Deutsche Bahn, but it's heavier and you should verify the current licensing model before committing.

**Mattermost** offers a lighter, more polished Go/React alternative to Slack with excellent DevOps integrations, though compliance and SSO features are enterprise-only. **Element** and **Cinny** are the reference Matrix clients if you go that route. **Zulip** excels for async distributed teams with its threaded-by-default design, **Revolt** is a well-built Discord-style Rust alternative, and **Chatwoot** is purpose-built for customer support workflows.

For the decentralized tier, **Matrix** is the production-ready federated standard, while **Nostr** offers a lightweight censorship-resistant primitive through signed events (though the ecosystem is still fragmented), **SimpleX** provides a no-identity model, and **Berty** uses libp2p with mesh networking capabilities.

For Nomad OS specifically, I'm realizing chat isn't really a standalone product here—it's a coordination feature embedded in payments, trip planning, and trust attestations. That fundamentally shifts which platform makes sense. **Matrix** with a custom Flutter UI on the rust SDK seems like the most sovereign path, giving you federation and... Nomad OS instance in Da Nang can talk to one in Chiang Mai if you want), E2E, multi-device, history sync. You spend the budget hiding Matrix concepts from users. This is the path Beeper/Element X/Famedly take. Heaviest ops, highest ceiling.

**B — Tinode or Rocket.Chat as backend, your UI on top.** Pragmatic middle. Lighter than Matrix. Rocket.Chat gives you an Apps Engine for plugins; Tinode is leaner and more mobile-shaped. You give up federation. Good v1, can migrate later.

**C — flutter_chat_ui + a thin backend that maps to your existing event model (SST).** Fastest to ship, and probably the most coherent with your architecture: a chat thread becomes a Space, messages become Tokens, group membership is just Sprite presence in that Space. Chat stops being a separate system you bridge into and becomes a view over the substrate you're already building. The cost is you rebuild what Matrix gives free (history sync, push, multi-device sync). The benefit is everything in Nomad OS speaks the same protocol.

Path C aligns best with where you're heading—if chat is just one shape of Token-flow-in-a-Space, then a separate chat backend is architectural debt, and wiring a UI library to your own substrate is cleaner. You can always bridge the SST layer to Matrix later if federation becomes necessary.

I'm wondering whether to dig deeper into Matrix embedding specifics, compare Tinode and Rocket.Chat from an ops angle, or sketch out what chat-as-an-SST-view would actually look like in code.Here's the landscape map across all four tiers, ending with what I'd actually pick for Nomad OS.

## 1. UI-only libraries (bring your own backend)

For **Flutter**, **flutter_chat_ui (Flyer Chat)** is the strongest pick — Apache 2.0, backend-agnostic, modular sub-packages for text/streaming/image messages, all six platforms, and actively shipping releases through late 2025. Sibling **flutter_firebase_chat_core** gives you a Firebase BaaS pairing for prototyping, and the same project ships **react-native-chat-ui** for the RN side.

For **React**, two serious options. **stream-chat-react** is very polished (channels, threads, reactions, read receipts) but built around Stream's hosted backend — code is MIT so you can fork and rewire, but the cost of doing that is real. **chatscope/chat-ui-kit-react** is lighter, MIT, fully backend-agnostic, ships with a `use-chat` hook for state. For React Native, **react-native-gifted-chat** is the legacy default but feature-thin; the Flyer RN port is the better modern choice.

If chat is going to do double duty as an AI agent surface, look at **assistant-ui** and **NLUX** — built around streaming LLM messages rather than human-to-human, but the line keeps blurring.

## 2. Backend / protocol — self-hostable servers

**Matrix** is the heavyweight: federated, E2E by default, mature. Three server implementations matter — Synapse (Python reference, heavy but full-featured), Dendrite (Go rewrite), and the Rust forks Conduit / conduwuit / Tuwunel. Tuwunel is now deployed at scale serving the citizens of Switzerland in production, which is a useful proof point that Rust-Matrix is no longer a toy. The matrix-rust-sdk has bindings to Swift, Kotlin, Wasm, Go and more, so you can embed Matrix client logic in essentially any app. Honest cost: ops are non-trivial, room state can grow large over time, federation adds complexity, and you'll spend real effort hiding `@user:server` IDs from end users.

**XMPP** (ejabberd, Prosody) is battle-tested at WhatsApp-scale, lean, federated. Spec is fragmented across XEPs, DX feels like 2010, but it's still the lightest mature option.

**Tinode** is a Go-based, mobile-first "modern XMPP replacement" — gRPC + WebSocket, Swift/Java/JS clients. Smaller community but clean engineering. Good middle weight.

**SimpleX** is the conceptually novel one — no user IDs at all, identity lives in per-pair message queues, relays are dumb. Self-hostable, has groups and calls now, but groups are still maturing and the no-identity model takes onboarding work.

## 3. Full-stack (UI + backend bundled)

**Rocket.Chat** is the most flexible — Node/MongoDB, an Apps Engine for plugins, native Matrix federation built into the platform, omnichannel bridges (SMS/email/social). Used by Deutsche Bahn and pitched at defense/government for sovereign deployments. Heavier footprint. Check current LICENSE before committing — pieces have moved toward dual-licensing.

**Mattermost** is the Go/React Slack clone — lighter than Rocket.Chat, very polished, strong DevOps integrations. Mattermost runs primarily in Go on the server with React on the front end, optimized for performance, with official desktop and mobile apps and a wide plugin marketplace. Community edition is MIT; SSO/compliance features sit behind enterprise.

**Element** (Web, plus Element X for iOS/Android — the Rust SDK rewrite) is the reference Matrix client. If you go Matrix, this is your fork point. **Cinny** is a lighter alternative Matrix client.

**Zulip** is threaded-by-default (topics within streams), best-in-class for async distributed teams. Less natural for consumer chat.

**Revolt** is a Discord-style OSS take — Rust backend, channels/voice. Younger but well-built. **Chatwoot** is customer-support shaped (Rails + Vue) — worth knowing if your shape is closer to "user ↔ ops team" than peer ↔ peer.

## 4. Decentralized / sovereign-aligned

This tier maps most directly to the 共同体 / Fork orientation.

**Matrix** is the production-ready federated option. **Nostr** is more of a signed-events-over-relays primitive than a chat protocol, but NIP-17 (private DMs) and NIP-29 (relay-based groups) are pushing it that way; lightweight and censorship-resistant, ecosystem fragmented. **SimpleX** for the no-identity model. **Berty** runs on libp2p with Bluetooth/local-mesh fallback — interesting for nomad contexts with patchy connectivity. **Briar** is Tor + Bluetooth + WiFi-direct, activist-grade. **Bitchat** is pure Bluetooth mesh, cool but very limited range.

---

## What I'd actually pick for Nomad OS

The shape of what you're building suggests chat is a *feature of coordination*, not a standalone product. The unit isn't "channel" or "DM" — it's "this payment split needs comments," "this trip needs a planning thread," "this trust attestation needs a back-and-forth." That changes the calculus.

Three realistic paths:

**A — Matrix backend + custom Flutter UI on matrix-rust-sdk.** Most sovereign. You inherit federation (a Nomad OS instance in Da Nang can talk to one in Chiang Mai if you want), E2E, multi-device, history sync. You spend the budget hiding Matrix concepts from users. This is the path Beeper / Element X / Famedly take. Heaviest ops, highest ceiling.

**B — Tinode or Rocket.Chat as backend, your UI on top.** Pragmatic middle. Lighter than Matrix. Rocket.Chat gives you an Apps Engine for plugins; Tinode is leaner and more mobile-shaped. You give up federation. Good v1, can migrate later.

**C — flutter_chat_ui + a thin backend that maps to your existing event model (SST).** Fastest to ship, and probably most coherent with your architecture: a chat thread becomes a Space, messages become Tokens, group membership is Sprite presence in that Space. Chat stops being a separate system you bridge into and becomes a view over the substrate you're already building. Cost: you rebuild what Matrix gives free (history sync, push, multi-device sync). Benefit: everything in Nomad OS speaks the same protocol.

My honest read: **Path C aligns best with where you're heading.** If chat is just one shape of Token-flow-in-a-Space, then a separate chat backend is architectural debt, and a UI-only library you wire to your own substrate is the cleaner move. The day you need federation or E2E, you can bridge the SST layer to Matrix rather than rebuilding on top of it.

Want me to drill into any of: matrix-rust-sdk embedding specifics, a Tinode vs Rocket.Chat ops comparison, or sketching what chat-as-SST-view would actually look like in practice?

---
**HUMAN** (2026-04-17T12:22):

if i choose a, how do i extend server events

---
**ASSISTANT** (2026-04-17T12:23):

  They're asking how to add custom event types to a Matrix server if they go with Path A — essentially, how to extend Matrix beyond standard message events to support domain-specific events like payment splits and trust attestations that Nomad OS would need for coordination.

Matrix is fundamentally event-driven, so custom events are built in: you just namespace them with reverse-DNS (like `chat.nomad.payment_split`), then decide if they're state events that persist in room state or message events that live in the timeline. For server-side extensions, they'd have options like Synapse modules for Python plugins, Application Services for custom integrations and event routing, or custom auth providers — and on the client side, matrix-rust-sdk handles arbitrary event types natively.

Now I'm thinking through what they actually mean by "extend server events" — it could be custom event types themselves, server-side reactions to events via modules or Application Services, or new federation-level capabilities that would need a Matrix Spec Change. I should cover all three because the answer depends on what kind of extension they're after. Let me verify the current Synapse modules API and matrix-rust-sdk capabilities to make sure I'm giving them accurate details.
```
This block is not supported on your current device yet.
```

 I've got enough context to write a solid answer now. The user is asking how to extend server events in Matrix — essentially how to add custom event types and behaviors on the server side. I'm thinking through the layered approach: custom event types can be sent directly since Matrix is designed to be open, using reverse-DNS namespacing for custom types.

For server-side reactive logic, there are two main paths — Synapse modules written in Python that run in-process, or Application Services as separate HTTP services. For Nomad OS specifically, the practical approach would be defining custom event types for their payment split use case, then running an Application Service to handle the reactive logic when those events arrive — like calling the AEON Pay backend and posting confirmation events back. A Synapse module might be needed if they want to validate events at the homeserver level.

There's also a licensing consideration worth flagging: Synapse moved to AGPL in version 1.99 under Element's stewardship, while the matrix.org foundation version stayed on Apache 2.0 but is stuck on an older release. And I should mention that the Node.js libraries like matrix-appservice-bridge and matrix-bot-sdk make Application Service development much simpler than building raw HTTP handlers.

I'll structure the answer around these three extension layers and map each one to concrete Nomad OS use cases, keeping it focused with some code examples since they asked for a how-to.Matrix is unusually open here — events are first-class extension points, not just envelopes for `m.room.message`. There are three layers you can extend at, in order of increasing power and complexity.

## Layer 1 — Just send custom event types (no server changes)

This is the unsung superpower of Matrix: any client can send any event type as long as it uses a reverse-DNS namespace. The server stores it, federates it, syncs it to other clients in the room, and runs the same access control rules as any other event. You don't extend the server at all — you just use it as a typed event bus.

Two flavors matter:

**Message events** are timeline entries (no state semantics). Use these for anything append-only — comments on a payment split, a trip plan iteration, an attestation:

```json
{
  "type": "chat.nomad.payment_split.comment",
  "content": {
    "split_id": "split_01HXYZ...",
    "body": "I'll cover Sara's portion",
    "amount_minor": 12500,
    "currency": "VND"
  }
}
```

**State events** are keyed (by `state_key`) and represent the current state of something in the room — overwriteable, queryable as a set. Use these for "what is this room *about*":

```json
{
  "type": "chat.nomad.coordination_context",
  "state_key": "",
  "content": {
    "kind": "payment_split",
    "split_id": "split_01HXYZ...",
    "creator": "@ren:nomad.os",
    "total_minor": 250000,
    "currency": "VND"
  }
}
```

From matrix-rust-sdk (Rust, or any of its bindings — Swift/Kotlin/Wasm/Go), you call `room.send_raw(event_type, content)` for messages and `room.send_state_event_raw(event_type, state_key, content)` for state. On the receive side, the sync stream gives you every event regardless of type, so your Flutter UI just filters on `type` and renders the right widget. **At this layer the server is doing nothing custom — Synapse is just storage, ordering, federation, and access control for your typed events.** This is enough for a surprising amount of Nomad OS.

## Layer 2 — Application Services (reactive server-side logic)

When you need *the server* to do something — react to an event, mint events on behalf of users, gate room creation, hold state outside any single client — you use an Application Service. This is the same mechanism every Matrix bridge (WhatsApp, Telegram, Slack) is built on.

An AS is just an HTTP service registered with Synapse via a YAML file. You add a new configuration file for your AS to the list specified under the `app_service_config_files` config option in your Synapse config, with an `as_token` (your service authenticating to Synapse) and `hs_token` (Synapse authenticating to you), plus namespaces for users and room aliases the AS owns.

Once registered, two things flow:

Synapse pushes events to your AS via `PUT /transactions/{txn_id}` containing arrays of events the AS is interested in — based on namespace match (a user the AS owns, or a room with an aliased name in your namespace). Your handler is a few lines:

```python
@app.route("/transactions/<txn_id>", methods=["PUT"])
def on_events(txn_id):
    for event in request.json["events"]:
        if event["type"] == "chat.nomad.payment_split.confirm":
            # Trigger AEON Pay settlement
            settle_via_aeon(event["content"])
            # Post a confirmation back into the room as the bot user
            send_event(event["room_id"], "chat.nomad.payment_split.settled",
                       {"tx_hash": "0x...", "split_id": event["content"]["split_id"]})
    return jsonify({})
```

Going the other direction, your AS can puppet any user in its namespace (e.g., `@_nomad_aeon:nomad.os`) and call the normal client-server API to send events, create rooms, invite users, set state. So the typical Nomad OS pattern would be: a virtual user `@_nomad_settlement_bot:nomad.os` joins every payment-split room, watches for `confirm` events, hits AEON Pay, posts back `settled` or `failed` events. UI just listens for those event types and renders accordingly.

Two important limits. Application services can only function in a "passive" way — you cannot prevent an event from being sent, only react to it after the fact, because in federation the rest of the network has already seen it. So if your logic needs to *block* something (e.g., reject a malformed payment event), you need Layer 3. And Application Services can become a performance bottleneck because all events on the homeserver must be ordered and pushed to registered services — fine at Nomad OS scale, worth knowing.

For implementation, don't write the raw HTTP yourself. Use **matrix-bot-sdk** (TypeScript — probably the easiest given your stack) or **matrix-appservice-bridge** (Node.js) — they wrap the protocol and give you typed event handlers.

## Layer 3 — Synapse modules (in-process Python plugins)

When you need to gate events *before* they're accepted, hook into auth/registration flows, expose new HTTP endpoints under the homeserver itself, or modify behavior the spec doesn't cover, you write a Synapse module. Synapse supports extending its functionality by configuring external modules — you add them to the `modules` section of homeserver.yaml as a Python class path with a config block.

Modules run in-process and can register callbacks like:

- `check_event_for_spam` — called when receiving an event from a client or via federation; the module can return a bool to indicate whether the event must be rejected, or a string to give a rejection reason forwarded to clients
- `user_may_invite`, `user_may_create_room` — gate membership/creation
- `check_registration_for_spam` — gate signup
- Custom HTTP endpoints under `/_synapse/client/<your_module>/...` that share the homeserver's database and auth

For Nomad OS this is where you'd put things like: validate that a `chat.nomad.payment_split.confirm` event references an existing split, has a valid signature, and the sender is actually a participant — and reject it at the homeserver if not. This is the only layer that gives you that.

Practical caveat worth knowing now rather than later: Synapse 1.99 onward is maintained by Element under a new licence (AGPL) at github.com/element-hq/synapse, while the older Apache 2.0 fork at github.com/matrix-org/synapse is no longer being updated. If you write modules, you're targeting Element's AGPL Synapse. The AGPL is fine for self-hosting Nomad OS but matters if you ever ship a customer-hostable build.

If AGPL is a non-starter for licensing reasons, **Tuwunel** (the Rust fork) is permissively licensed and now production-grade — but its module/extension story is less mature than Synapse's, so you'd lean harder on Application Services and less on in-process plugins.

## How this maps to Nomad OS specifically

A reasonable architecture:

- **Custom event types** carry every Nomad OS primitive — payment splits, attestations, trust votes, trip plans, venue check-ins. Each is just a typed event in a room. Your Flutter UI dispatches on `type` and renders the right widget. This is Layer 1, no server work.

- **An Application Service** (`@_nomad:nomad.os` namespace) is your settlement and coordination bot. It bridges chat events to AEON Pay, watches for `confirm` events, posts `settled` events back, manages virtual rooms for things like "all splits between Ren and Sara." TypeScript with matrix-bot-sdk, runs as a separate Docker service next to Synapse.

- **A Synapse module** for the validation rules you can't enforce at the AS layer — schema validation on Nomad event types, sender authorization, anti-spam. Small Python module, ~few hundred lines.

- **Federation off by default** for v1. You don't need a Da Nang Nomad OS node talking to a Chiang Mai Nomad OS node yet, and turning it off removes a whole class of operational and abuse-surface concerns. The architecture stays federation-ready — the moment you want it, you flip the config.

The mental model that makes this click: in Path A, **Matrix isn't your chat backend, it's your event substrate**. Chat is just the easiest thing to render on top of it. Payment splits, trust attestations, trip plans are all rooms-with-typed-events too. That's actually pretty close to your SST model — `Space ≈ Room`, `Sprite ≈ user/AS`, `Token ≈ event` — which is why Path A and Path C are less far apart than they look.

Want me to sketch a concrete event schema for one of the Nomad OS primitives (payment_split would be the obvious one), or walk through what the AS code would look like end-to-end for the AEON Pay settlement loop?
