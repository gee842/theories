# Splitting modules into smaller executables

created: 2026-04-12T17:45:38.213228Z  uuid: d1456341-f839-47f0-bce2-bcc96110900e  export: new
messages: 6  total_chars: 7325  human_chars: 300

summary: **Conversation Overview**

The person explored a software architecture question about splitting applications into many smaller executables versus fewer larger ones, with a focus on the tradeoffs in co-located, same-machine deployments where executables call each other via IPC. The conversation covered technical dimensions including IPC mechanisms (Unix domain sockets, named pipes, shared memory, gRPC over localhost), serialization overhead, crash isolation, and deployment flexibility. Claude outlined when process-per-module architectures are worth the IPC cost versus when in-process message-passing (actor models, Tokio tasks, Erlang-style) is preferable.

The conversation culminated in the person revealing the primary motivation behind the architecture question: designing systems where each executable is scoped to fit within a single AI agent context window, enabling agent teams to each own and fully comprehend one self-contained component. This reframed the IPC overhead as a deliberate tradeoff — the serialization boundary doubles as the interface contract that makes the code agent-legible and supports parallel development by multiple agent teams. The person is working on a project called OpenClaw, targeting edge deployment on Snapdragon devices, and is thinking through agent-driven development workflows. Claude flagged interface churn as the key risk in this model and suggested stable, versioned, schema-defined contracts as mitigation, connecting to the person's existing thinking around capability-based interfaces.


---
**HUMAN** (2026-04-12T17:45):

Can I put many modules into smaller executables? What’s the pro and cons?

---
**ASSISTANT** (2026-04-12T17:45):

The user is asking about putting many modules into smaller executables - this seems like a general software architecture/design question about monolithic vs. modular executable design. No search needed, this is well-established software engineering knowledge.

Given Ren's context as a systems thinker working on agent infrastructure (OpenClaw), this likely relates to deployment architecture decisions - whether to bundle modules into fewer larger binaries or split them into many smaller ones.Great question — this touches on a classic architecture tradeoff. Here's how it breaks down:

**Yes, you can.** Common approaches include statically linking modules into a single binary, using plugin/dynamic loading (`.so`/`.dll`), compiling multiple crate/package targets, or using subcommand-style multi-call binaries (like BusyBox).

**Pros of many-modules-in-fewer-executables:**

Reduced overhead per process — shared memory, single runtime initialization, no IPC serialization cost. Simpler deployment (one binary to ship). Easier shared state and direct function calls between modules. Smaller total disk footprint from deduplication of dependencies. Faster cold-start since you're not spawning N processes.

**Pros of splitting into many smaller executables:**

Process isolation — one module crashing doesn't take down others. Independent scaling and resource limits (critical for edge/daemon workloads). Easier to update, patch, or hot-swap a single component. Cleaner dependency graphs — each binary only links what it needs. Better fault attribution and monitoring. Composes naturally with Unix philosophy and container orchestration.

**The key tradeoffs to weigh:**

The monolithic approach wins on latency and simplicity but loses on resilience and independent deployability. The split approach wins on fault isolation and operational flexibility but adds IPC complexity and coordination overhead.

For something like an agent orchestration system running on edge devices, a hybrid is common — a thin supervisor binary that manages lifecycle for smaller worker executables, or a multi-call binary pattern where one binary dispatches based on `argv[0]`. Erlang/BEAM's approach (single VM, many isolated lightweight processes) is the idealized middle ground if your runtime supports it.

What's the specific context — are you thinking about this for OpenClaw's edge deployment on Snapdragon devices, or something else?

---
**HUMAN** (2026-04-12T17:49):

Let’s say every part is running on the same machine, all executables, that calls each other

---
**ASSISTANT** (2026-04-12T17:50):

Ren is asking about multiple executables on the same machine that call each other - this is about IPC architecture for co-located processes. Let me think about the tradeoffs clearly.Got it — co-located executables communicating via IPC. This is the "microservices on localhost" pattern. Here's the honest breakdown:

**How they'd call each other:**

Unix domain sockets, named pipes, shared memory, stdin/stdout piping, gRPC over localhost, or even just subprocess spawning with JSON on stdio. Each has different latency/complexity profiles.

**The real cost you're paying:**

Serialization/deserialization on every call boundary. Even with Unix domain sockets and MessagePack, you're looking at microseconds per hop that would be nanoseconds as direct function calls. If module A calls B calls C in a hot path, that overhead compounds. You also inherit coordination complexity — startup ordering, health checks, process supervision, and the "what if B dies mid-call from A" problem.

**When it's still worth it despite the overhead:**

If modules have genuinely different failure modes (a vision module segfaulting shouldn't kill the scheduler). If you want to restart or update one piece without bouncing everything. If modules are written in different languages. If you need hard memory/CPU isolation between components. If the call frequency is low enough that IPC cost is noise (e.g., agent tasks measured in seconds, not microsecond-level inner loops).

**When it's not worth it:**

If all modules are the same language and trust level, a single process with in-process module boundaries (trait objects, interfaces, message channels) gives you the same logical separation without the serialization tax. Tokio tasks or goroutines or Erlang processes give you concurrency isolation without process isolation.

**The honest take:** on a single machine, the main thing multiple executables buy you is crash isolation and independent deployment. If you don't need those — and especially if your call graph is chatty — you're paying real overhead for architectural purity. A single binary with internal message-passing (like an actor model) is almost always faster and simpler for same-machine, same-language, same-trust-level workloads.

Does this map to a specific part of the stack you're designing?

---
**HUMAN** (2026-04-12T17:53):

Well… if each can be written and tested in one context length, it will be very easy for agent teams to each only take care of their part

---
**ASSISTANT** (2026-04-12T17:54):

Ah, now the real reason emerges — this isn't about runtime architecture, it's about AI-assisted development ergonomics. Each executable is scoped to fit within a single context window, so an agent (or agent team) can fully comprehend and work on it without context overflow. That's a genuinely strong reason to split things up.

Let me think about this tradeoff from that angle.That's the real reason, and it's a strong one. You're optimizing the architecture for **agent-writability**, not just runtime efficiency.

The logic is sound: if each executable fits in one context window, an agent can hold the entire thing in mind — all the code, tests, and interfaces. No "scroll up and forget" problem. No hallucinating about code it can't see. Each agent team owns a complete, self-contained unit they can reason about end-to-end.

**What this buys you:**

Parallel development — N agent teams working simultaneously on N executables with zero merge conflicts. Clear interface contracts (the IPC boundary *is* the API spec). Each piece is independently testable with mock inputs/outputs. When something breaks, you hand the whole executable to an agent and it can actually understand everything. Refactoring stays local.

**The IPC overhead reframes:**

The serialization cost you pay at runtime is actually *the same* boundary that makes the code agent-legible. The interface contract that feels like "overhead" is actually the spec document the agents work against. So you're not paying a tax for nothing — you're paying for a development model that scales with AI tooling.

**The real risk to watch:**

Interface churn. If module A's protocol to module B keeps changing, you now need cross-agent coordination to update both sides. Keep the contracts stable and versioned, or you lose the independence benefit. This is where your SST/UCAN thinking probably maps well — capability-based interfaces that are self-describing.

**Practical shape:** define each executable's interface as a schema (JSON Schema, protobuf, whatever), put that in a shared contract repo, and let each agent team treat it as their only external dependency. The rest is their world.

This is basically the "Conway's Law for AI agents" insight — structure the code so it matches the cognitive boundaries of who's writing it.
