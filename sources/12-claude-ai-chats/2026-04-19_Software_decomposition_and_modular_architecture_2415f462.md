# Software decomposition and modular architecture

created: 2026-04-19T17:24:58.259887Z  uuid: 2415f462-cd7d-4500-8e5e-b178b10ac8ef  export: new
messages: 14  total_chars: 71638  human_chars: 1953


---
**HUMAN** (2026-04-19T17:24):

exploring compositional design, when i want to create a software, what are the best ways to compartmentalize different parts? what are the abstracts/concept(module, object, class, process, interface etc) that should be considered in decomposition?
for example, if I create a structure where everything can be divided into sub parts and independently executed without the contexts of other parts?

---
**ASSISTANT** (2026-04-19T17:26):

  The user is asking about compositional design principles—how to break systems into independently executable parts. This connects to architectural thinking and systems decomposition, so I should explore the conceptual foundations: what primitives enable decomposition (modules, objects, processes, interfaces), how to effectively compartmentalize, and what makes these approaches work across different domains.

The real question is about composability at a fundamental level. I'm recognizing that decomposition strategies vary dramatically depending on which axis you cut along—whether you're organizing around data structures, behavioral operations, independent execution units, protocols, capabilities, temporal events, or domain boundaries. Each approach creates different constraints and possibilities for independent execution. Beyond the strategic choices, there are also distinct levels of granularity to consider, from individual functions up through objects and modules, each with different tradeoffs for composability.

Now I'm drilling into what actually enables independent execution without needing surrounding context. This comes down to referential transparency and keeping reasoning localized—pure functions that depend only on their inputs, immutable data that eliminates temporal coupling, explicit dependencies with no hidden globals, capability-based systems where you can only affect what you have references to, content-addressable identities, and hermetic build systems that declare everything upfront. These properties work together to create the isolation needed for true composability.

The thinkers and frameworks that matter here span from Alan Kay's vision of objects as biological cells communicating through messages, to the Actor Model, to functional programming's emphasis on values and immutability, to Unix's philosophy of doing one thing well through pipes, to capability security and content-addressed systems like Git and Nix. All of these are pointing at the same underlying principle—you need to eliminate hidden dependencies and make everything explicit and composable.

For Ren's specific context, this maps cleanly onto pure functional approaches, serverless architectures, immutable containers, the Actor Model, hermetic builds, and Unix-style composition through streams.

Given his background with SST, OpenClaw, and UCAN, he's already thinking deeply about these boundaries. I should avoid being patronizing, connect to frameworks he likely knows, offer a clean conceptual lens, and highlight some less-obvious angles. The question itself lists specific decomposition units—module, object, class, process, interface—so some structure makes sense, but I should keep it mostly prose rather than heavy lists.

The key move is showing that these primitives aren't interchangeable; they're actually cutting along different axes. Once you see what axis you're optimizing for, the right decomposition becomes clearer. I want to walk through the main axes—state ownership, namespace boundaries, execution context, interface contracts—and specifically address his point about independent execution without context, since that's pointing at a particular set of properties. Then I can reference some useful frameworks and thinkers to pull on. **Self-describing data** (schemas, content hashes)

The architectures/paradigms that nail this:
- **Pure functional programming**: function as the unit, immutable data
- **Actor model**: actors own all their state, communicate via messages
- **Nix-style hermetic builds**: derivations declare all inputs
- **Container/unikernel**: full stack isolation
- **Unix pipes**: programs as functions from stdin → stdout
- **Capability-based security**: you can only act on what you have a reference to
- **Content-addressed systems**: identity = hash of content (IPFS, Git, Merkle DAGs)

I think the frame to give is: **what invariant are you trying to preserve?** Different decomposition primitives preserve different invariants.

Each decomposition strategy protects something different—modules guard namespacing and cohesion, classes maintain state encapsulation, processes isolate faults, interfaces enable substitutability, services decouple deployment, actors keep state local, pure functions guarantee referential transparency, and content-addressable blobs ensure immutability and verifiability. So really, the question of how to compartmentalize comes down to which invariants matter most for your particular system.

For AI agent systems like what Ren is building, the critical invariants are likely around state...

For AI agent systems like what Ren is building, the critical invariants are likely around state locality with each agent owning its own state, capability-based addressing so agents can only access what they have references to, content-addressable artifacts that are versioned and verifiable, hermetic execution that can rerun deterministically, and protocol-level interfaces that make agents substitutable through schemas. This maps directly onto his SST framework where Sprites function as actors, Spaces define bounded contexts, and Tokens represent capabilities. I should structure the response around this connection and keep it concise. I'm ready to start writing the response now.Compositional design is really a question of *what axis are you cutting along*, because the primitives you listed — module, object, class, process, interface — aren't alternatives to each other; they're addressing different invariants. Once that's clear, you stop asking "which one?" and start asking "which invariants matter most for this system?"

**The axes of decomposition**

- **Module** preserves *namespacing* and *code cohesion*. It's a compile-time/source-level grouping. No runtime identity.
- **Class/object** preserves *state encapsulation* and *behavior locality*. State and the operations that touch it live together.
- **Interface/protocol/trait** preserves *substitutability*. The contract is separate from the implementation, so you can swap implementations without cascading changes.
- **Process** preserves *fault isolation* and *resource ownership*. If one crashes, the rest survive. OS enforces the boundary.
- **Actor** preserves *state locality* + *asynchronous message passing*. Each actor owns all its state; no shared memory, only messages.
- **Service** preserves *deployment independence* and *network-boundary isolation*. Different release cycles, different runtimes.
- **Pure function** preserves *referential transparency*. Same inputs → same outputs, no side effects, no hidden state.
- **Content-addressed blob** (Merkle-style) preserves *immutability* and *verifiability*. Identity = hash of content.
- **Capability** (OCAP / UCAN-style) preserves *authority locality*. You can only act on what you hold a reference to; no ambient authority.

Most real systems layer several of these. A service contains modules, which contain classes; actors communicate via messages but their payloads are content-addressed blobs; capabilities gate what functions can do. You pick primitives per layer based on what property you need at that layer.

**The "independently executable without context" property**

This is the interesting part of your question, because it's pointing at a specific cluster of properties — what the hermetic-builds and pure-FP people call *locality of reasoning*. To get it, you need:

1. **Explicit dependencies** — no globals, no ambient authority, nothing "in scope" that isn't passed in. Everything the unit needs is declared.
2. **Referential transparency** — given the same inputs, same outputs. No hidden state, no wall-clock, no network calls unless explicitly modeled.
3. **Bounded state** — either none (pure function), or fully owned by the unit (actor).
4. **Self-describing inputs/outputs** — schemas, types, content hashes. The unit can be run with any caller that produces valid inputs.
5. **Stable contract** — the interface is versioned separately from the implementation.

The paradigms that genuinely deliver this:

- **Pure functional programming** (Haskell, Elm) — function is the unit, data is immutable.
- **Actor model** (Erlang, Akka) — state is local to the actor, communication is explicit messages; Armstrong's "let it crash" works because the isolation is real.
- **Nix / Bazel hermetic builds** — derivations declare every input (source, compiler, env vars); same inputs always produce the same output, cacheable by hash.
- **Unix pipes** — every program is a function from stdin to stdout; the shared interface is bytes, the universal composer is `|`.
- **Capability-based security** — authority is bounded by reference; you can statically reason about what a component *could* do.
- **Content-addressed data** (Git, IPFS, AT Protocol's records) — identity is the content; history is a Merkle DAG; independent verification is free.

**The deeper pattern**

The common thread across all of these is: **make dependencies explicit, and make the unit closed under its declared inputs.** Coupling isn't eliminated — it's *moved into the type/schema/protocol* where it can be inspected and versioned. That's what distinguishes composition from mere juxtaposition: composed pieces expose their seams, so the system around them can reason about the seams.

If I had to give you a single design heuristic: **the unit of decomposition should be the unit of independent understanding.** If you can't reason about a piece without pulling in three other pieces' implementations, your boundaries are wrong — not necessarily too small or too large, but cut along the wrong axis. Ousterhout's *Philosophy of Software Design* calls this "deep modules": a small, stable interface hiding substantial implementation. That's the shape you want at every layer, whether it's a function, a class, an actor, or a service.

Given what you're building with SST, this probably already resonates — Sprites are the state-local actors, Spaces are the bounded contexts, Tokens are the capabilities. That's a coherent stack because each layer picks one invariant and commits to it. The places where compositional systems usually fail aren't in the primitives — they're in the seams between layers, when a capability leaks ambient authority, or an actor quietly shares memory, or a content hash depends on a non-deterministic input. The discipline is keeping the invariants honest.

---
**HUMAN** (2026-04-19T17:36):

good answer, this is what i am thinking about, like we have frontend and back end, then frontend each has modules, ui, and there are shared things can be implemented. what if we follow a particular order, first design data structure, then design a local sdk, then add a server to expose the sdk, then develop the frontend, i think to build such sop is quite possible

---
**ASSISTANT** (2026-04-19T17:38):

  The user is proposing a structured development methodology—building from data structures up through a local SDK, then a server that exposes that SDK, and finally the frontend—and wants to know if this approach is actually practical and valuable. They're clearly thinking deeply about systems architecture, so this deserves a thoughtful exploration of the tradeoffs and real-world viability of this kind of disciplined ordering. order:**
1. Design data structures first
2. Build a local SDK (pure logic, in-process)
3. Add a server that exposes the SDK (network boundary)
4. Build the frontend (consumer)

This methodology has real precedent. Data structures are foundational—they outlast code, and getting them right means everything else can adapt. The SDK comes next as pure business logic, completely separate from transport concerns. Then the server becomes just a thin adapter layer that exposes the SDK over HTTP or gRPC, meaning the same core can work in-process, as a CLI, or anywhere else. The frontend comes last because it's just a consumer of the API.

This approach shows up everywhere: protobuf-first design at Google, OpenAPI contracts, AT Protocol's lexicon-first approach, hexagonal architecture, domain-driven design, and Rich Hickey's philosophy of separating data from functions and effects. The pattern is consistent across different domains and scales.

But there are real pitfalls to watch for. You can't finalize data structures in isolation—the UI will reveal what you actually need, so you have to prototype interfaces in parallel to validate the model. Building an SDK before understanding what consumers actually need leads to over-engineering. And local SDKs don't map cleanly to network SDKs; network layers need batching, caching, retries, pagination, and auth that local code doesn't. Once you commit to a data schema, evolving it becomes the hardest problem.

This order is actually well-validated as a software development pattern—it's contract-first development with a functional core and library-oriented design, which is how SQLite, Redis, Lucene, and libgit2 all started. Data structures need to be designed for evolution from the beginning, using approaches like AT Protocol's versioning or protobuf's field numbering. Given that Ren is building systems-oriented projects like OpenClaw and Nomad OS, this library-first approach probably resonates with their thinking. I'm recognizing this as a real, well-validated pattern — contract-first, functional-core, library-before-service development — where the ordering reflects actual dependency relationships: each layer depends on what's below it, but lower layers remain independent of what sits above. The power isn't in the sequence itself but in ensuring each layer is self-contained and complete, so dependencies flow only downward. independently testable artifact. You should be able to test data structures with property-based tests and fixtures, use the SDK from a REPL or CLI without a server running, hit the server with curl without a frontend, and mock the server to develop the frontend independently.

The key is doing a vertical slice first to validate the data model, then building out layer-by-layer — treating this as strictly sequential waterfall will lead you astray. This approach aligns with "Parse, don't validate" and making illegal states unrepresentable, so once the data structures are solid, a whole class of bugs just disappears.

I'm also noticing how this connects to Ren's SST protocol work — Tokens, Spaces, and Sprites are the foundational data primitives with systems built on top, and OpenClaw as an agent framework would benefit from this same discipline. This pattern shows up across different communities under various names: contract-first or schema-first development, hexagonal architecture, functional core with imperative shell, and the library-before-service approach that spawned ecosystems around SQLite, libgit2, and Lucene. by being libraries first)

The pattern works because each layer you're describing corresponds to an independently testable artifact with a stable contract to the layer above it. That's the key discipline — not the order per se, but that each layer is *complete on its own terms* before the next is built.

Let me unpack why your specific order is good:

**Data structures first** — Linus's "bad programmers worry about code, good programmers worry about data structures" and Rich Hickey's "data, function, macro" point at the same truth: data outlives code. If your schema is right, you can rewrite everything above it. If it's wrong, every layer above has to paper over the mistake. AT Protocol's lexicons, Git's object model, the Linux kernel's struct definitions — these all exemplify freezing the data model and iterating everything else.

**Local SDK second** — this is where the functional core lives, in-process without network or UI concerns. It should be usable from a REPL, CLI, test harness, or another process entirely. The real test is whether you can drive the whole product from the command line; if you can, your core is clean.

**Server as a thin wrapper** — the server becomes just a transport adapter, deserializing requests and serializing responses while the SDK handles all the interesting logic. This lets you swap transports without touching business logic and run the same code path in-process for tests or local-first deployments.

**Frontend last** — because it's the presentation layer, furthest from the data and most likely to change based on user feedback.

Now the caveats, because this breaks in predictable ways: building order isn't the same as thinking order — if you design data structures in isolation, you'll get them wrong because the UI reveals what data you actually need. The discipline is to prototype a crude end-to-end slice first to pressure-test the model, then build out layer by layer. And a local SDK is fundamentally different from a network SDK since one is a library while the other has to handle...

Still writing about network concerns...

The schema evolution piece is critical—once you lock in data structures, every change becomes a migration, which is why systems like AT Protocol and protobuf obsess over versioning and field rules. Building for evolution from the start means designing for additive changes, versioned envelopes, and content-addressed records where possible.

There's a real cost to this ordering though: nothing visible ships until you've built all four layers, which starves product and design feedback on teams. The vertical slice approach solves this by getting a rough end-to-end flow working fast—even if it's crude—so each layer can deepen with real feedback rather than assumptions.

The reason this dependency-ordered approach works is that it mirrors the actual dependency graph: data has no dependencies, the SDK depends only on data, the server depends on the SDK, and the frontend depends on the server. Building in that order means you're always standing on solid ground. Reversing it creates fragility because you're building on assumptions that haven't been validated yet.

For what you're working on—SST, OpenClaw, Nomad OS—this matters even more because you're designing protocols, not just products. Protocols *are* their data structures; everything else is implementation detail. Starting with lexicons, tokens, and schemas is already the right instinct.

I'm thinking through what to keep here. The person engaged deeply and has the context to follow nuance, so I should preserve the substance but tighten the delivery. The real value isn't explaining why this works—they probably sense that already—it's the caveats, the places where this approach breaks down. Let me restructure around that and avoid over-formatting.Yes, this SOP is real and well-validated — it goes by several names depending on which community you ask: **contract-first / schema-first development** (protobuf, OpenAPI, AT Protocol lexicons), **hexagonal architecture** or ports-and-adapters (Cockburn), **functional core, imperative shell** (Bernhardt), and **library-before-service** (SQLite, libgit2, Lucene — each spawned ecosystems by being libraries first, and getting wrapped in servers later).

What makes it work isn't the order itself, but that each layer is a complete, independently testable artifact with a stable contract to the layer above. Let me unpack why your specific sequence is good:

**Data structures first.** Linus's "bad programmers worry about code, good programmers worry about data structures" and Rich Hickey's "data, function, macro" are pointing at the same truth — data outlives code. If the schema is right, you can rewrite everything above it. If it's wrong, every layer above has to paper over the mistake. AT Protocol lexicons, Git's object model, kernel struct definitions — all "freeze the data model, iterate everything else."

**Local SDK second.** This is the functional core. Business logic lives here, in-process, no network, no UI. It should be drivable from a REPL, a CLI, a test harness, another process. The test: can you exercise the whole product from the command line? If yes, your core is clean.

**Server as a thin wrapper.** The server becomes a transport adapter — deserialize request, call SDK, serialize response. All interesting logic is in the SDK; the server is plumbing. This means you can swap the transport (HTTP → gRPC → WebSocket → in-process) without rewriting logic, and run the same code path locally for tests or for local-first deployments.

**Frontend last.** Because it's a consumer. The frontend should be "dumb" in the sense that it has no business rules the SDK doesn't already enforce. Ideally the same client library works whether it talks to an in-process SDK or a remote server.

Now, the caveats — because this breaks in predictable ways.

The first and biggest: **building order is not thinking order.** If you design data structures in isolation and only then think about UI, you'll design the wrong data. The UI reveals what fields, what indices, what queries, what events you actually need. The discipline is to prototype a crude end-to-end vertical slice first — maybe three fields and one screen — to pressure-test the data model, and *then* build out layer by layer for real. Waterfall-izing this SOP is the trap.

Second: **a local SDK and a network SDK are not the same thing.** A library handles success and failure synchronously in one address space. A network SDK has to handle batching, pagination, retries, caching, auth, partial failure, optimistic updates, offline queues. You can't just "add a server wrapper" — the network boundary introduces real concerns that don't exist in-process. The honest version is to design the local SDK to be *compatible* with becoming networked (async by default, explicit error types, no assumed locality, no hidden shared state), then expect to add a genuine layer of adapters at the network seam rather than pretending the seam is transparent.

Third: **schema evolution is the hardest part, and you pay for it at the beginning.** Once you commit to data structures, every change is a migration. This is the thing AT Protocol obsesses over with lexicon versioning, protobuf with field-number rules, event sourcing with upcasting. If you put data first, design it for evolution from day one — additive changes only, versioned envelopes, content-addressed records if you can get away with it. Otherwise you've locked in your mistakes at the foundation.

Fourth: **this order has a cost in feedback velocity.** You ship nothing visible until step 4. For a solo builder that's fine because you hold the whole model in your head; for teams it can starve product/design feedback for weeks. The vertical-slice fix addresses this — get to "crappy UI talking to real server talking to real SDK talking to real schema" as fast as possible, then deepen each layer in order.

The deeper reason the SOP works is that it matches the dependency DAG: data doesn't depend on SDK, SDK doesn't depend on server, server doesn't depend on frontend. Building in dependency order means you're always building on a stable base. Building in the reverse order — frontend-first, mocking everything below — is how you get business logic scattered across React components and schemas retrofitted to whatever the UI happened to need that week.

For what you're building, this discipline is especially well-suited because SST and OpenClaw are protocols, not just products. Protocols *are* their data structures; everything else is implementation. The Token-Space-Sprite primitives as the foundation, then a local library that operates on them, then a server that exposes that library, then any number of frontends and agents as consumers — that's the same pattern, and it's probably why the architecture is holding together.

---
**HUMAN** (2026-04-19T17:43):

I think to think about what the software do - and what states are involved, what outcomes and the information that will be represented, to generate that interface. i think the thinking should start with what i want to do - then naturally think interface

---
**ASSISTANT** (2026-04-19T17:44):

 Exactly — you've arrived at the real starting point, which is *intent* before *structure*. The SOP I described (data → SDK → server → UI) is the *building* order, but the *thinking* order is the opposite: start from what the system is for, let that produce the interface, and let the interface dictate what data structures must exist to support it.

This is a known distinction and worth naming because it has real consequences. A few framings from different traditions, all circling the same truth:

**"Design the interface first, implementation second."** Parnas's 1972 "On the Criteria To Be Used in Decomposing Systems into Modules" argued that modules should hide design decisions, and the way to find the right decomposition is to ask what the system *does*, then work out what could change, and hide each changeable decision behind an interface. You can't do this by starting from data structures — you have to start from purpose.

**"What does the user/caller want to say?"** API-first and DSL-design people phrase it this way. Before you design the tables, design the sentences someone would write against the system. If your system is a todo app, the sentences are `addTask`, `completeTask`, `listTasksDueThisWeek`. Those verbs, plus their arguments and return shapes, *are* the interface. The data structures are whatever it takes to make those sentences efficient to execute.

**"Sketch the README first."** Readme-driven development (Tom Preston-Werner). Write the README as if the system already existed. If the README is confusing, the system will be confusing. If the README is clean, you now have a spec.

**"What are the nouns and verbs?"** Domain-driven design. The nouns become entities and value objects; the verbs become commands and queries; the invariants become aggregates. But you can only find these by talking about the domain in its own language, not by starting from tables.

**"States and transitions."** What you mentioned — states, outcomes, information — is exactly the vocabulary of state machines and process calculi. Every non-trivial system is a state machine at some level of abstraction; making that explicit up front often reveals the interface. "The document is in states `draft`, `submitted`, `approved`, `rejected`; these are the transitions between them; these are the events each transition emits." Now you know your API surface and your data model fell out as a consequence.

So the full loop is:

1. **Intent.** What is this system *for*? What does it let someone do that they couldn't do before?
2. **Interface.** What are the sentences its users (human or machine) want to say to it? What states does it expose, what transitions, what queries, what outcomes?
3. **Data.** What structures must exist to make those sentences executable, those states representable, those queries efficient?
4. **Implementation.** Modules, SDK, server, UI — in that dependency order, once the above is stable.

The reason this matters — and why I think you're pointing at something important — is that **data-first without intent-first produces well-structured irrelevance.** You can design a beautiful schema that no one needs. Whereas intent-first forces you to answer "why does this exist?" before "how is it shaped?" — and the "why" is what ultimately makes the shape right.

The Unix tradition has a saying for this: *"Write down what the thing does on an index card before you write any code."* If it doesn't fit on the card, you don't yet understand what you're building. That's the same discipline — intent precedes interface precedes implementation.

There's also a useful second-order point here for your work specifically: when you're designing protocols (SST, OpenClaw, Nomad OS), the interface *is* the product. The data structures are implementation details of the protocol, but the verbs and the states are what other people build against forever. Getting the intent crisp, then the interface crisp, then letting data fall out — that's exactly the right order for protocol design, and it's also why AT Protocol spent so long on lexicons before shipping, and why Git's plumbing commands were designed before its porcelain.

So your instinct is right: thinking should start with "what do I want to do," then "what does saying that look like," and only then "what does that require underneath." The building order is bottom-up; the thinking order is top-down; and the skill is holding both simultaneously without collapsing one into the other.

---
**HUMAN** (2026-04-19T17:46):

well, there is another way thinking about it: we are building a system, and what sub systems that composes the system, what are the interface between them? like human and organs - metaphorically speaking, and each organ has cells, which are systems themselves and have interface

---
**ASSISTANT** (2026-04-19T17:47):

 Yes — and this is actually a *different* decomposition principle from the intent-first one, not just a restatement. You've moved from "what does the system do" to "what are the natural seams along which the system is already composed." These are complementary, and mature designers use both.

The biological metaphor is load-bearing, not just evocative. Herbert Simon's "The Architecture of Complexity" (1962) made the argument formally: complex systems that survive are almost always **hierarchical** and **nearly decomposable** — meaning interactions *within* a subsystem are dense and fast, interactions *between* subsystems are sparse and slow, and each level is a complete system in its own right. This isn't a design choice; it's a property of systems that evolution, biological or otherwise, converges on because it's the only way complexity scales. His parable of the watchmakers Tempus and Hora makes the point: the one who builds in stable sub-assemblies finishes; the one who builds monolithically never does.

So when you say "organ → cell → organelle," you're describing exactly Simon's near-decomposability. Each level has:

- **Internal coherence** — dense interaction, shared state, tight coupling *inside*.
- **Thin interface** — a small, stable surface to the level above and below.
- **Level-appropriate vocabulary** — cells don't think about organs; organs don't think about organelles. Each level reasons in its own terms.

This maps directly onto software and gives you a third decomposition axis beyond the two we've discussed:

1. **By intent** (what does it do) — top-down, starts from purpose.
2. **By data/build order** (what depends on what) — bottom-up, dependency DAG.
3. **By natural seams** (what are the organs) — *sideways*, finds the coherent subsystems that exist because the domain itself is structured.

The sideways view is what you're pointing at. It asks: *where are the dense-interaction clusters, and where are the thin interfaces between them?* Conway's Law is the social version of this — systems mirror the communication structure of the organizations that build them — and microservices, bounded contexts (DDD), and actor systems are all attempts to engineer this deliberately.

Some practical consequences:

**Interfaces at each level should be narrow and level-appropriate.** Blood carries oxygen between organs; the lungs don't know what the brain does with it. Similarly, a payment subsystem shouldn't expose its internal ledger representation; it exposes `charge`, `refund`, `balance`. The interface is in the vocabulary of the *caller*, not the implementer. A cell communicates via hormones, neurotransmitters, ion gradients — all tiny, stable, domain-appropriate signals. Not by exposing its mitochondria.

**Recursive self-similarity is a feature.** A cell is a system with inputs, outputs, state, metabolism, defense, reproduction. So is an organ. So is an organism. So is a colony. Good software has this too: a function is a tiny system (inputs → outputs, maybe local state); a module is a system; a service is a system; a product is a system. The primitives I listed earlier — pure function, actor, service — each implement the system-ness at a different scale with different isolation guarantees. This is why the "is it a module or a service?" question is often malformed: the answer is *both, at different levels*.

**The interfaces between levels are where the real design happens.** Evolution is parsimonious about interfaces — the number of signaling molecules, the number of neurotransmitters, the number of standard protocols between organs is small and highly conserved. The same is true of good software architecture: the count of *types of interfaces* should be small (HTTP+JSON, message queue, function call, content-addressed blob) even if the *number of components* is large. Proliferation of interface *types* is usually a symptom of missing abstraction, not of necessary variety.

**Nearly decomposable ≠ fully decomposable.** This is the subtle point Simon insisted on. Organs *do* interact — just slowly, through well-defined channels (hormones, blood, nerves). Software subsystems interact too. The goal isn't zero coupling; it's *bounded, legible, slow* coupling at the seams, and dense-fast coupling only within. When a design fails, it's almost always because fast coupling leaked across a seam that was supposed to be slow — a service reaching into another service's database, a UI component directly mutating store state owned by another feature, a capability being used as ambient authority.

Now — the crucial synthesis. The three decomposition views aren't alternatives; they're checks on each other:

- **Intent-first** tells you *what the system must do.*
- **Seams-first** tells you *what the system naturally is.*
- **Data/build-first** tells you *in what order to construct it.*

When these three agree, the design is probably right. When they disagree, the disagreement is the signal. If intent says "users want X" but no natural seam supports X, you're either missing a subsystem or X isn't really coherent. If seams say "these two things are separate organs" but intent keeps requiring them to share deep state, one of the two views is wrong — usually the seam was drawn in the wrong place. If the build order forces you to construct a subsystem before you understand its interface, you're going to get the interface wrong.

There's a name for designers who hold all three views simultaneously: **architects**, in the genuine sense of the word — not the job title, but the discipline of seeing a system from the outside (intent), from the inside (seams), and over time (construction and evolution) at once. Christopher Alexander's pattern language came from architecture-architecture and was explicitly about this: a pattern is a resolution of forces at a particular scale, and systems are composed of patterns at many scales, each internally coherent, each thinly connected to the scales above and below.

For your work — OpenClaw, SST, Nomad OS — this triple view is especially relevant because protocols are organisms. They have organs (the core primitives), cells (individual records, tokens, sprites), tissues (subsystems like auth, storage, coordination), and they communicate with other organisms (interop with other protocols). The hardest protocol-design mistake is drawing the organ boundaries wrong, because unlike code, protocol boundaries are almost impossible to move once deployed. The biological metaphor is the right one to hold in your head while making those cuts.

The short version: you're not picking between "top-down from intent" and "sideways from seams." You're learning to triangulate. The system is what it does, what it's made of, and how it comes into being — all three, always, at once.

---
**HUMAN** (2026-04-19T17:49):

i mean the intent is to construct this system, but it is recurrent, at each level, agent understand what the system given to them to construct, it decompose them into smaller systems, manage the interface design, and spawn new agent to deal with the sub system as if they are the system, to each level, and every system should be completed within 1 full context

---
**ASSISTANT** (2026-04-19T17:50):

 Now you're describing something quite specific and interesting — you've jumped from *how humans decompose systems* to *how an agent swarm recursively decomposes and builds systems*, with the context window as the fundamental physical constraint. This is a real architecture, and it has precedents worth naming before we examine where it breaks.

**What you're describing**

Stated precisely: a recursive agent that receives a system specification, decomposes it into subsystems with defined interfaces, spawns child agents for each subsystem (each receiving only its own spec + interface contracts), and recurses until the leaves are small enough to implement in one context. Each level has complete local knowledge; no level has global knowledge. The context window becomes the unit of decomposition — if a subsystem doesn't fit, it wasn't decomposed enough.

This is genuinely novel as an agent architecture, but the underlying pattern has three strong ancestors:

**Hierarchical Task Networks (HTN)** from classical AI planning. A task is either primitive (directly executable) or compound (decomposes into subtasks via methods). Planning proceeds by recursive decomposition until everything is primitive. Your architecture is HTN with LLM agents as the decomposers, and "fits in one context" as the primitive-ness criterion.

**Structured analysis / stepwise refinement** (Wirth, 1971; Yourdon-DeMarco, 1970s). "Program development by stepwise refinement" is exactly this pattern for humans: start with the whole problem, decompose, specify interfaces between parts, recurse on each part. The discipline that fell out of favor with OOP but whose bones are still in every good top-down design.

**The Mythical Man-Month's "surgical team"** and later Fred Brooks's conceptual integrity argument. The idea that a system's integrity comes from a single mind holding the whole — and when that doesn't scale, from hierarchical decomposition where each level has its own integrity. Your "one full context" is the AI-era version of "one mind."

**Why the constraint is load-bearing, not incidental**

The "complete within one context" rule is doing more work than it looks. It's not just a memory limit — it's enforcing Simon's near-decomposability *physically*. If a subsystem can be fully specified, implemented, and verified in one context, then by construction it has bounded internal complexity and a thin enough interface to be describable as input. The context window becomes a complexity budget that forces correct decomposition.

This is genuinely elegant. Most decomposition disciplines fail because there's no forcing function — humans can always "just add one more thing" to a module. A context limit is incorruptible. When a subsystem doesn't fit, you *have to* decompose further; you can't cheat.

**Where this architecture succeeds and where it fails**

It works beautifully for problems that are *genuinely hierarchical*: compilers (lexer → parser → typechecker → codegen, each independently specifiable), build systems, many kinds of data pipelines, CRUD systems where domain boundaries are clean. Anywhere the dependency DAG is close to a tree, recursive decomposition with local context is extremely powerful.

It struggles in several predictable ways, and these are worth being explicit about because they're the design problems you'll actually hit:

*Interface design is global, not local.* A parent agent defines the interface between two children. But whether that interface is *right* depends on what each child actually needs — which the parent doesn't know until the children try to implement. Interface mistakes at level N surface as contradictions at level N+2, and the child at N+2 can't fix them; only the ancestor at N can. You need a mechanism for *upward escalation* — a child saying "this interface you gave me is unbuildable, here's why, please redesign" — and the parent must be able to actually redesign, which means the parent's context can't be finalized when it spawns children. This breaks the "each level completes in one context" purity.

*Cross-cutting concerns don't decompose.* Security, observability, error handling, performance, naming conventions, shared types — these appear at every level and must be *consistent across siblings who never see each other*. The classic failure mode of recursive decomposition (in humans and presumably in agents) is that sibling subsystems invent incompatible vocabularies, duplicate types, choose conflicting conventions, because no one sees both. You need either (a) a shared spine of conventions passed to every child as part of their spec, or (b) a later integration pass that reconciles sibling outputs — and (b) is often where the real work turns out to live.

*Decomposition itself requires context the decomposer may not have.* To decompose well, the parent needs to understand the domain, the constraints, the likely evolution, the failure modes. Sometimes decomposition is the hard part and implementation is trivial; sometimes it's the reverse. If your parent agent decomposes naively and your leaves are perfectly implemented against bad interfaces, you've built a clean skeleton of the wrong animal.

*Leaf-level completeness ≠ system-level correctness.* Each subsystem can be individually correct against its spec while the assembled whole fails, because emergent properties (latency under load, consistency across a distributed transaction, end-to-end UX coherence) are not properties of any single subsystem. You need *vertical slice tests* that cross all levels, which means somewhere there must be an agent or process whose context spans the whole depth — violating the one-context rule.

*The specification of a subsystem is often longer than the subsystem.* Counter-intuitively, handing down a complete enough spec for a child to work in isolation may take more tokens than just building the subsystem. This is the old "writing the spec is harder than writing the code" problem. In practice the specs want to be terse and reference shared artifacts (types, protocols, example inputs) rather than restate them — which means children need access to a shared context artifact, which means "one full context" per agent is augmented by "plus a shared substrate they can query."

**The version of this that actually works**

Given those failure modes, the architecture that falls out looks something like:

1. **A shared substrate** — the data structures, the type system, the interface definitions, the naming conventions — authored at the root and accessible (read-only) to every descendant. Not duplicated into every context; referenced. This is analogous to how cells share DNA: each cell has the whole genome but only expresses what it needs.

2. **Decomposition agents separate from implementation agents.** The decomposer's job is to produce a spec + interface contracts. The implementer's job is to fulfill the spec. They are different skills and probably different prompts. Decomposers look at the whole; implementers look at the leaf.

3. **Bidirectional communication.** Children can raise contradictions upward; parents can revise and respawn. This is expensive but essential. Without it, you get cascading mistakes.

4. **Integration / conformance agents at each level** whose job is specifically to check that sibling outputs compose correctly against the interfaces their parent defined. This is the "immune system" of the architecture.

5. **End-to-end testing agents** with the context to trace a request through all levels and verify system-level properties. These violate the one-context rule locally, but that's fine — they exist specifically to catch what local contexts can't see.

6. **The leaves should be chosen to be as boring as possible.** The recursion terminates not when something fits in context, but when something is *so standard* that implementation is mechanical. A CRUD endpoint, a data transformation, a UI component following an established pattern. If your leaves are creative, your decomposition didn't go deep enough.

**The deeper observation**

What you're actually designing is *an organization*. Everything I just described — shared conventions, decomposers vs. doers, escalation paths, integration roles, end-to-end testing — these are exactly what every well-functioning engineering organization develops. Conway's Law running in reverse: you're designing the organization first, and the software is its output. This is why the biological metaphor keeps recurring — organisms are organizations of cells, organizations of organs, etc., and they've solved this problem at every scale.

There's a specific bet implicit in your design: that one agent + one context + one spec is the right *unit* of organizational attention. This is a bet worth making — it's roughly analogous to the two-pizza team, or the single-maintainer module, or the one-person-week task. But like those, it's a heuristic that works until the work doesn't fit the heuristic, and then you need the surrounding structure (the shared substrate, the escalation, the integration) to handle the misfits.

For OpenClaw specifically, this maps cleanly: a parent Sprite decomposes a Space into child Spaces with Token-gated interfaces; each child is itself a Space that can recurse; the context window is the natural size of a Sprite's working memory. The SST vocabulary already has the right primitives. The hard parts are exactly the ones above: shared substrate (how do child Spaces see common types?), escalation (how does a child Sprite signal interface problems upward?), integration (who verifies sibling Spaces compose?), end-to-end (who holds the whole trace?).

So: yes, the recursive one-context decomposition is a real and powerful architecture. The elegance is genuine. The discipline will be in the *non-recursive machinery* that keeps the recursion honest — and that machinery is where most of the design effort will end up going.

---
**HUMAN** (2026-04-19T18:01):

great, let's design the system that can spawn such "organization", that can self organize by spawning more sub systems that spawns subsystems on demand

---
**ASSISTANT** (2026-04-19T18:02):

 Good — this is the right move. You're now designing the *meta-system*: not the thing being built, but the thing that builds things. Let me work through this carefully, because the design decisions at this level determine whether the whole architecture holds together or collapses into either chaos or rigid hierarchy.

I'll structure this as: the core abstraction, the protocols that make it work, the shared substrate, the failure modes it must handle by design, and the minimum viable implementation.

**The core abstraction: the Builder**

Every node in this organization is the same kind of thing. Call it a Builder. A Builder receives:

- a **Charter** — what it is responsible for producing (intent + acceptance criteria)
- an **Interface Contract** — what it must expose upward (its promise to its parent)
- a **Substrate Handle** — read access to shared artifacts (types, conventions, protocols, sibling interfaces published so far)
- a **Budget** — context tokens, wall-clock, spawn depth, money

A Builder has exactly four capabilities:

1. **Implement** — produce the artifact directly (terminal case)
2. **Decompose** — produce a set of child Charters + Interface Contracts + a composition plan
3. **Escalate** — return to parent with "this charter is unbuildable as specified, here's why, here's what I'd need"
4. **Publish** — write artifacts to the substrate at well-known addresses so siblings and descendants can reference them

That's it. Same interface at every level. A Builder doesn't know if it's the root or a leaf; it just receives a Charter and decides which of the four moves to make. This is the self-similarity that makes recursion possible.

The recursion terminates on Implement. The recursion escapes upward on Escalate. The recursion expands on Decompose. Publish is the side-channel that keeps the tree coherent.

**The five protocols that make this work**

*1. The Charter protocol — how work is specified*

A Charter must be self-contained enough that a Builder with no other context can act on it. Structure:

- **Goal**: one sentence, what this subsystem is for
- **Acceptance**: observable criteria — tests, examples, invariants — not implementation requirements
- **Interface promised upward**: the shape the parent expects back
- **Interfaces available downward**: what the substrate already provides (types, siblings' outputs, shared protocols)
- **Constraints**: budgets, conventions to follow, things explicitly out of scope
- **References**: pointers into the substrate for anything non-trivial — never inlined, always by address

The discipline: a Charter says *what* and *against what contract*, never *how*. If you find yourself specifying the how, you're either micromanaging or the decomposition was wrong.

*2. The Interface Contract protocol — how promises are made*

Between every parent and child there's a contract. Contracts must be:

- **Total** — every input case has a defined output or error
- **Versioned** — contracts evolve; consumers declare which version they speak
- **Machine-checkable** — types, schemas, or examples the integration agent can validate against
- **Stable under implementation changes** — the whole point of the contract is that the implementation behind it is swappable

Contracts live in the substrate, not in any single Builder's context. When a parent decomposes, it *publishes* the contracts to the substrate and passes *handles* to children. Children read the contracts from the substrate. This way sibling A and sibling B both see the same contract; neither has a private copy that could drift.

*3. The Escalation protocol — how the recursion stays honest*

This is the single most important protocol and the one most meta-systems get wrong. A child must be able to push back. The escalation message contains:

- **What's unbuildable**: the specific contradiction, missing input, or impossible constraint
- **Minimal diff**: what change to the Charter or Contract would make it buildable
- **Downstream impact**: which sibling contracts would be affected by the change

The parent receiving an escalation has three responses: revise the Charter and respawn the child, revise the Contracts (which may require re-decomposing other siblings too), or escalate further upward if the problem originates above.

Without a working escalation protocol, recursive decomposition produces fractally wrong systems where no level can fix the mistake. With it, the system is self-correcting.

*4. The Publication protocol — how siblings coordinate without seeing each other*

Every artifact a Builder produces — interfaces, types, test suites, implementations, documentation — gets published to a shared address space at a predictable path. Something like `/{project}/{subsystem-path}/{artifact-type}/{name}`. 

This is the circulatory system. A child Builder writing a module doesn't need to know what its cousin is doing; it just reads the published interfaces it depends on. Content-addressing helps: if artifacts are identified by hash, a child can declare "I built against hash X of contract Y" and any later mismatch is detectable.

Critically, the substrate is *append-mostly* with *explicit revisions*. You don't overwrite; you publish v2 and mark v1 superseded. This lets a long-running child discover its dependency changed and decide to rebuild or escalate.

*5. The Composition protocol — how to verify the whole from the parts*

Every parent, upon receiving all its children's artifacts, must run a composition check: do the published artifacts actually satisfy the parent's own Charter? This is not just "did each child succeed individually" — it's "does the assembly satisfy the parent's interface promise upward?"

This is where integration tests, end-to-end traces, and conformance checks live. The parent is responsible for this because only the parent sees all its children at once. If composition fails, the parent either re-decomposes, re-issues Charters, or escalates.

**The shared substrate**

I've mentioned it repeatedly — let's make it concrete. The substrate is:

- A **content-addressed store** for immutable artifacts (types, schemas, test suites, code modules)
- A **namespace** for mutable references (pointers to the current version of each contract)
- A **conventions document** at a well-known address — naming, error handling, logging, telemetry — that every Builder reads as part of its Charter
- A **registry of open Charters and their status** — what's been decomposed, what's being built, what's been published, what's escalated
- An **event log** — every Builder action is recorded so the whole construction history is auditable

This is essentially Git + a type registry + a work queue + a convention book. None of these are novel individually; the point is that together they form the *physical substrate* that makes the recursive decomposition possible.

Why content-addressing matters specifically: it makes "did this change?" a cheap hash comparison, it makes cycles detectable, it makes reproducibility automatic, and it lets you cache — if a Charter has been built before with the same hash of inputs, you can reuse the prior output. For an agent swarm paying for tokens, cache is survival.

**The failure modes the design must handle**

Any self-organizing system has characteristic failure modes. A minimum viable design addresses each:

*Runaway decomposition.* A Builder keeps decomposing without ever implementing. Mitigation: budgets at every level. Depth budget, token budget, time budget, dollar budget. When budget is exhausted, a Builder must Implement or Escalate; it cannot Decompose further. This forces recursion to terminate.

*Interface drift.* Siblings evolve incompatible interfaces. Mitigation: contracts in the substrate are the source of truth; implementations reference them by version; a conformance agent checks every published artifact against its declared contract version.

*Convention drift.* Siblings use inconsistent naming, error handling, style. Mitigation: the conventions document is *part of every Charter*, not assumed. A linter/style agent can run on every published artifact.

*Silent failure.* A child produces something that passes its local tests but fails to satisfy its actual purpose. Mitigation: acceptance criteria in the Charter include behavior, not just shape. Examples and properties, not just types.

*Deadlock.* Child A waits for child B's output; child B waits for A's. Mitigation: the parent's decomposition must produce a DAG, not a graph. If children need mutual visibility, they weren't properly decomposed — they should be one child, or their shared concern should be lifted to a third sibling that both depend on.

*Loss of global coherence.* The assembled system does things no Charter specified. Mitigation: the root Builder (or a dedicated integration Builder at each level) runs end-to-end tests whose context spans multiple children.

*Cost explosion.* Agents spawn agents without bound. Mitigation: budgets are *consumed*, not *inherited*. A parent with budget N gives children budgets summing to ≤ N minus its own overhead. Every decomposition strictly reduces available budget downstream. This makes runaway costs structurally impossible.

**The minimum viable implementation**

If I were building this — and for OpenClaw, you essentially are — I'd start with the smallest possible version that demonstrates the loop:

1. A single Builder type with the four capabilities, implemented as an agent harness with a very specific prompt and tool set.
2. A content-addressed file store for the substrate (Git works; IPFS works; a flat directory with hashes works).
3. A work queue where open Charters are posted and Builders pick them up.
4. A conventions document at a known path, loaded into every Builder's context.
5. A simple escalation channel — a specific file path or queue where children write escalation messages and parents poll.
6. A logging system that captures every Builder invocation for replay and debugging.

The first thing to build with it should be small — something like "build a CLI tool that does X" with two or three levels of decomposition. The goal of v0 is not to build impressive software; it's to discover where the loops actually break. They will break. The escalation protocol will be wrong; the substrate schema will be wrong; the budget accounting will leak. That's fine — the system is designed to tell you where it's wrong because every Builder's actions are logged and every escalation is explicit.

**Where this sits relative to what exists**

Worth naming so you know what to learn from and what not to reinvent:

Systems like AutoGPT, BabyAGI, and their descendants were early tries at this — they failed primarily because they had no substrate, no contracts, no escalation, and no budgets. They were recursive but not organized. 

Claude Code's subagents and the Agent Teams pattern are closer — they have explicit delegation and structured outputs, but don't yet have a first-class substrate or escalation protocol in the way I've described.

Research systems like Voyager (Minecraft) and MetaGPT have pieces — Voyager has a skill library (substrate), MetaGPT has role-based decomposition. None has the full loop.

The closest mature analogue is actually *Bazel* — a build system where every rule has declared inputs, declared outputs, is content-addressed, caches aggressively, and composes hierarchically. You're designing Bazel for agent-generated software, where the "rules" are LLM-driven Builders rather than fixed compilers.

**The meta-principle**

A self-organizing system is not one with no structure. It's one whose structure is in the *protocols* rather than the *participants*. Any Builder can be replaced; the protocols are what persist. That's why I've spent most of this answer on protocols rather than on Builders. Get the Charter, Contract, Escalation, Publication, and Composition protocols right, and the system can be populated by any agent capable of following them — which means it survives model upgrades, mixed agent types, and even humans acting as Builders at some levels. That portability is the real test that the design is right.

For SST specifically, you already have the right primitive vocabulary — Sprite is Builder, Space is the substrate-region a Builder operates on, Token is the capability that gates what it can publish and consume. The design above is essentially "SST with a decomposition lifecycle bolted on." That's not coincidence; it's because you've been converging on this shape from multiple angles, and the shape is the one that works.

---
**HUMAN** (2026-04-19T18:09):

but i think there is a more general approach and intuition, like what a tech lead skill tool box that can have, to deal with different decompositions

---
**ASSISTANT** (2026-04-19T18:10):

 Yes — you're reaching for the right level of abstraction. What I described before was *one particular* decomposition architecture. What you're asking about now is the **meta-skill**: the toolbox a tech lead reaches into, matches to the situation, and applies. That's a more important thing to articulate because it transfers across problems; any single architecture is just one tool in the box.

Let me try to lay out what's actually in that toolbox. This is the thing senior engineers have internalized as "taste" but which can be made explicit.

**The toolbox, organized by what kind of cut you're making**

*Cuts by responsibility* — "who owns what"

- **Layered decomposition.** Stack of tiers where each only talks to the one below. Classic three-tier (presentation/business/data), OSI network layers, compiler passes. Works when the problem has a clear flow direction and abstraction gradient. Fails when concerns cut across layers.
- **Hexagonal / ports-and-adapters.** A functional core with pluggable adapters for every external concern (DB, network, UI, time). Works when you want the core independently testable and want to preserve optionality on infrastructure. The move when you don't yet know what the outside world looks like.
- **Onion / clean architecture.** Concentric rings of dependency — domain at center, infrastructure at edge, dependencies only point inward. Same idea as hexagonal, different metaphor; useful when you want to be very strict about the dependency direction.
- **MVC / MVVM / MVP.** Separation specifically for UI-bearing systems: the model doesn't know about the view. Works for interactive UIs; overkill elsewhere.

*Cuts by data flow* — "where does information move"

- **Pipeline / pipe-and-filter.** Each stage transforms and passes along. Unix pipes, ETL, stream processors, compiler pipelines. The move when the problem is fundamentally a transformation of data.
- **Event-driven / publish-subscribe.** Producers emit events, consumers subscribe, no direct coupling. Works when many downstream systems need to react to the same thing and you want extensibility without modifying producers.
- **Dataflow / reactive.** Explicit graph of dependencies, changes propagate automatically. Spreadsheets, React, RxJS. The move when you want derived state to always be consistent with sources.
- **Request/response.** The boring default. Worth naming because it's often the right answer and people over-engineer away from it.

*Cuts by domain* — "what are the natural seams"

- **Domain-driven design / bounded contexts.** Cut along the vocabulary of the business. Each context has its own language and its own model, even for "the same" entity. The move when the organization has multiple overlapping mental models of the domain.
- **Feature verticals.** One team/module owns a user-visible capability end-to-end, including its slice of UI, API, data. The move when you want fast independent iteration per feature and are willing to accept duplication across verticals.
- **Aggregate roots.** Group entities by transactional consistency boundary. Each aggregate is internally consistent; between aggregates, eventual consistency. The move when you have complex state with different consistency needs.

*Cuts by runtime isolation* — "what can fail independently"

- **Process / service decomposition.** OS-enforced isolation, independent failure, independent deployment. The move when fault isolation or independent scaling matters more than call efficiency.
- **Actor model.** State-owning concurrent units communicating by message. The move when you have many independent stateful things (connections, sessions, devices, games).
- **Sandbox / capability-confined.** Isolation by what each unit is *permitted* to do, not by where it runs. The move when trust is asymmetric — plugins, user code, third-party integrations.

*Cuts by time* — "what changes at different rates"

- **Stable core, volatile shell.** Identify the slow-changing heart of the system and the fast-changing surface; invest in the core's quality, let the shell be cheap to rewrite. Meyer's Open/Closed in spirit.
- **Plug-in architecture.** A host that doesn't change much + extensions that change often. VSCode, browsers, Figma. The move when you want an ecosystem.
- **Versioned contracts.** Separate the lifecycle of the interface from the lifecycle of the implementation. Every long-lived system eventually needs this.

*Cuts by cognitive load* — "what fits in a head"

- **Deep modules.** Ousterhout's rule: small interface, substantial implementation behind it. The module is valuable because it hides a lot.
- **Small units of change.** Each commit, PR, or task is reviewable in one sitting. Social/cognitive, not technical, but shapes the architecture.
- **Bounded context window.** The agent-era version of the above — each unit fits in one context.

**The meta-skill: knowing which cut to reach for**

The toolbox isn't the skill. The skill is diagnosis. A tech lead is doing something like this, often without articulating it:

*What kind of change will hurt most?* If the most likely painful change is "we need to swap the database," cut with hexagonal so the core doesn't know about the DB. If it's "we need to add a new kind of user," cut by domain so each user type is a clean extension. If it's "we need to add a third team," cut so their work doesn't contend with existing teams.

*What's the dominant complexity?* Data complexity → cut by data model and aggregates. Interaction complexity → cut by event flows. Domain complexity → cut by bounded contexts. Scale complexity → cut by runtime isolation. Cut along the axis where the complexity actually lives; any other cut will leave the hard part tangled.

*Where's the entropy coming from?* Some systems are complicated because the world is complicated (genuine domain complexity — you can't design it away, only organize it). Some are complicated because they evolved without decomposition (accidental complexity — the right cut will dissolve most of it). These get different treatments; the second gets refactored, the first gets partitioned.

*What does the organization look like?* Conway's Law is predictive, not just descriptive. If you have three teams that don't talk to each other, you will have three subsystems with awkward interfaces whether you planned it or not. Design the decomposition to match the communication structure, or change the communication structure, but don't fight it.

*What's reversible vs irreversible?* Internal module boundaries are reversible; data schemas mostly aren't; public APIs aren't; protocol wire formats really aren't. Spend design effort proportional to reversibility cost. For the irreversible things, over-design is cheap insurance. For the reversible things, under-design is fine — you'll learn what's right by building.

*What's the blast radius of being wrong?* A wrong internal abstraction means refactoring. A wrong service boundary means a painful migration. A wrong data model means years of compatibility code. A wrong protocol means a broken ecosystem. Cut conservatively where the blast radius is large; cut aggressively where it's small and you'll get feedback.

**The diagnostic questions I'd actually ask, in order**

When facing a new system, the questions roughly in priority:

1. What is this system *for*? (Without this, no cut is right.)
2. What are the nouns and verbs in its domain? (Reveals bounded contexts.)
3. What states does it have, and what transitions? (Reveals interfaces.)
4. What does information flow *through*? (Reveals pipeline vs. event vs. request/response.)
5. What's allowed to fail independently? (Reveals process/service boundaries.)
6. What's likely to change, and at what rate? (Reveals stable core vs. volatile shell.)
7. What must be transactionally consistent? (Reveals aggregates.)
8. Who will work on this, and how do they communicate? (Reveals Conway-appropriate structure.)
9. What's reversible and what isn't? (Reveals where to spend design effort.)
10. What's the smallest end-to-end slice that would prove the design? (Reveals where to start.)

A tech lead doesn't do this explicitly every time; it becomes pattern-matching. But when a design is contested, walking through these questions explicitly tends to resolve the argument — because disagreements about architecture are usually disagreements about which of these questions is most important to answer first.

**The signs a decomposition is wrong**

Equally important: how to diagnose that an existing decomposition is failing. The symptoms:

- **Shotgun change** — a simple feature touches many modules. Decomposition is cut across the grain of how changes actually arrive.
- **Feature envy** — module A constantly reaches into module B. The boundary is in the wrong place.
- **Leaky abstraction** — callers must know implementation details to use the interface. The interface is too shallow.
- **Chatty interface** — many small calls where a few domain-level calls would do. The abstraction is at the wrong level.
- **God object / god service** — one unit knows about everything. Missed decomposition opportunities.
- **Duplicated domain logic** — the same rule lives in multiple places. A bounded context is being split where it shouldn't be.
- **Circular dependencies** — A needs B needs A. The dependency structure isn't a DAG; something wants to be extracted into a third module.
- **Tests that are hard to write** — always a sign the abstraction is wrong; good decomposition makes tests easy.
- **New team members take forever to ramp on one module** — that module is too deep for the interface it exposes, or its boundaries are arbitrary.

These are the diagnostics. Each points to a specific cut in the toolbox as the remedy.

**The underlying principle that unifies the toolbox**

All of these techniques are doing one of two things: **making a coupling explicit, or moving a coupling to where it can be managed.** You never eliminate coupling — the system has to work as a whole. You relocate it from implicit to explicit, from scattered to localized, from ad-hoc to protocol-mediated, from fast-changing to slow-changing. That's the whole game.

A tech lead's toolbox is really a set of *patterns for relocating coupling*. Hexagonal moves coupling from "core depends on DB" to "core depends on an interface the DB implements." Events move coupling from "A calls B" to "A and B both agree on event shape." Bounded contexts move coupling from "everyone uses the same model" to "translations happen at context boundaries." Versioned contracts move coupling from "change breaks consumers" to "consumers declare which version they accept." Every item in the toolbox is a specific technique for taking a painful coupling and moving it somewhere it hurts less.

This is why the skill is learnable but not reducible to rules. You're pattern-matching: *where does the coupling hurt, and which technique relocates it to somewhere it hurts less?* Senior engineers have seen enough coupling-pain in enough shapes to recognize the patterns. That recognition is the whole thing.

**For your work specifically**

The reason this framing matters for OpenClaw and SST is that you're building systems where the *agents* need to carry a version of this toolbox. A Builder that can only decompose one way will produce the same shape of output for every problem — which is exactly the failure mode of early agent systems. A Builder that can reach into a toolbox, diagnose which cut fits, and apply it is doing what a human tech lead does. The toolbox isn't an implementation detail; it's likely the core content of what distinguishes a competent Builder from a useless one.

Which suggests a concrete design: the system prompt or skill library for a decomposing Builder should contain this toolbox *explicitly*, plus the diagnostic questions, plus examples of each technique being applied well. Not as trivia — as the actual working vocabulary the agent reasons in when it decides how to decompose. The ability to *name* the cut ("this is a pipeline / this is an aggregate boundary / this is a port-adapter seam") is what lets the decomposition be deliberate rather than arbitrary.

The meta-point: the toolbox is not something a tech lead *has*. It's something they *are*. They've internalized the patterns until recognition is automatic. The goal of making it explicit is to bootstrap that same recognition in a system — whether the system is a junior engineer you're teaching, a document you're writing, or an agent you're prompting.
