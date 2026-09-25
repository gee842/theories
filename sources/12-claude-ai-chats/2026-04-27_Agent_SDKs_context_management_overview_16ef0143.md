# Agent SDKs context management overview

created: 2026-04-27T14:07:43.656055Z  uuid: 16ef0143-c71a-47f5-9645-00928de70a7a  export: new
messages: 2  total_chars: 13730  human_chars: 77


---
**HUMAN** (2026-04-27T14:07):

how does agent sdks manage context? what is the whole picture in each of them

---
**ASSISTANT** (2026-04-27T14:09):

  I'm considering the major agent SDKs that handle context management—Claude's offering, OpenAI's approach, LangChain/LangGraph, Google's framework, and a few others—to give a comprehensive overview of how they each tackle this problem.

The core strategies vary: some use compaction or summarization, others delegate through sub-agents to isolate context, while many leverage external storage, sliding windows, or memory tools. Given Ren's background in harness engineering and the SST architecture work, I should dig into the actual mechanisms rather than surface-level explanations, and I need current information since these SDKs evolve quickly. Let me search for the latest implementations across these platforms.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I should also look into Google ADK since it's another key player in the agent SDK space.
```
This block is not supported on your current device yet.
```

 I've got solid coverage of the major frameworks now. Let me quickly verify my understanding of Pydantic AI and CrewAI/AutoGen to fill any gaps, then I can shape this into what Ren actually needs—someone who's already deep in Anthropic's context engineering and building with SST architecture, looking for a complete picture of how each framework approaches the problem.

Ren's after the architectural bones and design philosophy, not tutorials. They want to understand how each SDK's core mental model translates into its API, so they can make better decisions for OpenClaw. I'll organize around the primitives each framework exposes, the underlying philosophy, how the components interact, and the quirks that matter. Then I'll synthesize across all of them to show what design space they collectively cover and how they compare.

The philosophical landscape is becoming clearer—Anthropic's approach layers multiple memory and compaction strategies (server-side compression, tool-result clearing, persistent memory stores, subagents for isolation), while the others likely take different stances on where control and responsibility sit.

Now looking at how OpenAI structures this differently with sessions as the core abstraction, pluggable persistence backends, and server-side state management through the Responses API. LangGraph takes a fundamentally different angle—the state graph itself is the source of truth, with checkpointers handling thread-level snapshots and stores managing cross-thread memory, where context flows through the graph structure rather than as a message list. Google's approach appears to be more explicitly tiered...

I'm mapping out the key architectural dimensions across these systems: where state actually lives, how each one compresses context, what the persistence boundaries are, the mental model developers need to adopt, and who controls when context operations happen. For presenting this comparison, I'm thinking prose sections per SDK rather than heavy bullet points, since Ren values depth, but I'll need some structure to make the four approaches clear without overwhelming the reader.Four SDKs worth comparing here, since they span the design space pretty completely: Claude Agent SDK, OpenAI Agents SDK, LangGraph, and Google ADK. Each has a distinct mental model for what "context" even is, and that's where the interesting differences live.

## Claude Agent SDK

The mental model is **layered context engineering** — context is finite, has diminishing marginal returns, and you assemble strategies that operate on different parts of the window. Compaction compresses the whole window when it grows too large, clearing drops stale re-fetchable data inside the window, and memory moves information out of the window so it survives across sessions.

The four primitives:

**Compaction** distills the conversation into a high-fidelity summary when token usage approaches a threshold. Server-side compaction is recommended over SDK compaction — it handles context management automatically with less integration complexity, better token usage calculation, and no client-side limitations. Claude Code itself uses a more sophisticated trigger than naive "fill the window," making room for the response instead of pretending the whole context window is available for input — compaction needs space, recovery paths need space.

**Tool-result clearing** (`clear_tool_uses_20250919`) drops old tool outputs while keeping the record that the call happened — the assumption being those results are re-fetchable. Claude Code goes further and tracks compactable tool_result blocks and edits them in a cache-aware way instead of eagerly rewriting everything locally, because not all context pressure is token pressure — some is cache-lifecycle pressure.

**Memory tool** is structured note-taking via a `/memories` filesystem the model can read/write. Client-side, so the host controls storage. This is the key primitive for just-in-time context retrieval: rather than loading all relevant information upfront, agents store what they learn in memory and pull it back on demand.

**Subagents** isolate work in their own context window — the parent only sees the result. The new **Managed Agents** API also exposes `memory_stores` as first-class resources attached at session creation, with individual memories within the store capped at 100KB (~25K tokens) and the recommendation to structure as many small focused files.

Above the primitives sits a **harness pattern** for cross-window work: an initializer agent that sets up the environment on the first run, and a coding agent that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session — typically a `claude-progress.txt` plus git history. This is essentially "treat sessions like engineering shifts."

## OpenAI Agents SDK

The mental model is **Session-as-memory-object**. The Session abstraction unifies retrieval, storage, and trimming behind a single interface. The SDK supports several conversation management strategies: manual (calling result.to_input_list() and appending), session-based (get_items/add_items via the Session protocol), and server-managed (leveraging OpenAI's conversation state tracking to avoid resending full history).

The pluggable session implementations: `SQLiteSession` (default local), `SQLAlchemySession` (Postgres/MySQL for production), `OpenAIConversationsSession` (server-managed via Conversations API), `RedisSession`, `DaprSession`, plus the compaction wrapper.

For compaction specifically, **`OpenAIResponsesCompactionSession`** wraps an underlying session and calls the server-side `responses.compact` endpoint. It can run in `previous_response_id` mode (chains turn IDs) or `input` mode (rebuilds from current items). Compaction clears and rewrites the session history, so the SDK waits for compaction to finish before considering the run complete. In streaming mode, this means run.stream_events() can stay open for a few seconds after the last output token if compaction is heavy.

The **`session_input_callback`** is the elegant escape hatch — a hook that fires after history retrieval but before the model call, where you mutate the merged input list. This is where you implement custom trimming, dedup, or re-ordering without subclassing.

For long-term/typed state, **`RunContextWrapper`** is a separate axis — structured state objects that persist across runs, useful for the state-based long-term memory pattern: state object as your local-first memory store (structured profile + notes), distill memories during a run, consolidate session notes into global notes at the end, inject curated state at the start of each run with precedence rules.

The cookbook's two named techniques are **trimming** (last N turns, deterministic, zero summarizer cost) and **compression** (LLM-summarize older turns) — these are the two "default" patterns the SDK is shaped around.

## LangGraph

The mental model is fundamentally different: **context is graph state**, not a message list. The graph is the source of truth and the LLM call is one node in it.

**Checkpointers** persist state at every superstep. When you use a graph with a checkpointer, the checkpointer saves a checkpoint of the graph state at every superstep, enabling several powerful capabilities like human-in-the-loop, "memory" between interactions and more. Each checkpoint is keyed by `thread_id`, so threads = conversations. Backends: `InMemorySaver`, `SqliteSaver`, `PostgresSaver`, Redis, Couchbase, AgentCore on AWS, etc.

This gets you for free: time-travel debugging (replay from any checkpoint), fault tolerance (resume from last good state), HITL pause/resume (graph just stops at an interrupt and persists), and per-thread isolation.

**Store** is the cross-thread long-term layer — RedisStore and AsyncRedisStore enable cross-thread memory, letting agents access and store information that persists across different conversation threads, with vector search capabilities to retrieve semantically relevant information using embeddings. Stored as JSON documents, supports semantic search and metadata filtering.

The orthogonal short-term concern — keeping the messages list in the graph state from blowing up — is handled with **reducers** (the function that controls how new state merges with old) and **pre/post-model hooks**. You can write a reducer that summarizes when length exceeds N, or use the AgentCore-style pattern where a `pre_model_hook` runs before each LLM call to inject relevant memories from the Store.

So the picture: short-term memory = thread state via checkpointer; long-term memory = Store with semantic search; compression = your reducer's responsibility; everything is explicit graph nodes.

## Google ADK

The mental model is **three explicit tiers** with separate services for each.

**Session** is the conversation thread — holds events (chronological log of messages, tool calls, agent replies) and state. **State** is a key-value dict scoped to the session, with prefixes that signal scope: `app:` (shared across all users of the app), `user:` (across this user's sessions), `temp:` (this turn only). **Memory** is the long-term searchable archive across sessions.

Each tier has a Service interface with swappable backends:

- `SessionService`: `InMemorySessionService` (dev), `DatabaseSessionService` (Postgres/SQLite), `VertexAiSessionService` (managed)
- `MemoryService`: `InMemoryMemoryService` (keyword match), `VertexAiRagMemoryService` (RAG over embeddings), `VertexAiMemoryBankService` (the production option — Memory Bank uses the Gemini model to extract key information from session data, to store just the key memories for future use)

State updates are event-sourced — they go through `EventActions.state_delta` rather than direct mutation, so every change is captured in the event log. The retrieval pattern uses a `load_memory` tool that the agent calls explicitly when it needs cross-session context, rather than auto-injection.

Templating syntax (`{key}` in instructions) lets you inject state directly into the system prompt without callbacks — small but pleasant for context-aware instructions.

## How they compare

A few axes that map onto your SST thinking:

**Where context lives.** Claude SDK keeps it in the message stream and pushes overflow to a separate memory filesystem. OpenAI keeps it in a Session abstraction that's basically a database row. LangGraph keeps it in graph state with explicit reducers. ADK splits it into three named tiers.

**Who decides to compact.** Claude: the server (recommended) or SDK with thresholds. OpenAI: the SDK with a wrapper class, or you, via callbacks. LangGraph: you, in your reducers and hooks. ADK: you, via Memory Bank's automatic extraction or explicit tool calls.

**How cross-session continuity works.** Claude: explicit memory tool + handoff files (claude-progress.txt). OpenAI: pluggable Session backend persists, plus typed `RunContextWrapper`. LangGraph: Store with semantic search separate from the per-thread Checkpointer. ADK: MemoryService searched via `load_memory` tool.

**What "compression" means.** Claude: server-side LLM summarization of conversation. OpenAI: same, plus first-class trimming. LangGraph: emergent — your reducer compresses or you don't. ADK: Memory Bank extracts during ingest, not as a window operation.

**Isolation primitives.** Claude has explicit subagents (separate context windows). OpenAI has agent handoffs (also separate). LangGraph isolates naturally per-node. ADK has multi-agent orchestration with shared state across agents in the same session.

The convergent pattern across all four: **active window + external store**, with the model calling a tool to query the external store when needed. The divergence is in how aggressively the SDK handles the active window for you (Anthropic: a lot, server-side; OpenAI: a wrapper away; LangGraph: you write it; ADK: split by tier) and how opinionated the long-term layer is (ADK and Anthropic Managed Agents have first-class memory stores; LangGraph and OpenAI hand you a key-value/document store with optional vector search and let you build the policy).

For Sprite-Space-Token, the most directly relevant cross-cuts are probably (1) Anthropic's tool-result clearing as a model for what Space-level operations on stale tokens should look like, (2) LangGraph's reducers as a model for how Sprites compose into shared Space, and (3) ADK's `app:`/`user:`/`temp:` prefixes as a clean precedent for scoping in a multi-tenant Space.
