# Context Runtime
## An implementation plan for a branchable, persistent agent runtime

### Status

Architecture proposal, v0.1.

The system is designed around a simple proposition:

> An agent is not its prompt, its chat history, or its memory store.  
> At any moment, an agent continues from a complete state of being.  
> That state should be addressable, immutable, inspectable, branchable, replayable, and mergeable.

Git provides the persistent state-space.

The Context Runtime gives that state meaning.

Sessions provide interaction.

Surfaces provide presentation.

Models are computations over projections of state.

No individual AI framework owns the system.

---

# 1. North star

The architecture should remain understandable even if, five years from now:

- the dominant model providers are different;
- Assistant UI is replaced;
- ADK disappears;
- MCP is superseded;
- we move execution from Node to Rust;
- models gain ten-million-token contexts;
- agents run continuously for months;
- a single agent becomes thousands of collaborating agents;
- context compilation becomes learned rather than hand-designed;
- memory becomes substantially more sophisticated;
- agents begin modifying parts of their own runtime.

The durable abstractions therefore cannot be:

```text
chat messages
LLM provider APIs
framework sessions
vector databases
prompt templates
UI threads
```

They should instead be:

```text
state
transition
identity
provenance
branch
merge
capability
interaction
projection
```

Everything else is an implementation.

---

# 2. The six fundamental objects

The entire architecture can be understood through six objects.

```text
Context Universe
    └── Context Node
            └── Invocation

Session
    └── Surface
            └── Interaction
```

They belong to two separate worlds.

## Persistence

```text
Context Universe
Context Node
Invocation
```

describes what the agent is and how it changes.

## Interaction

```text
Session
Surface
Interaction
```

describes how humans, agents and software interact with that state.

Keeping these separate is one of the most important architectural decisions.

---

# 3. Context Universe

A **Context Universe** is the complete historical and counterfactual state-space of some persistent system.

It is implemented as a Git repository.

```text
                            ┌── C ── D
                            │
A ───── B ───── E ───── F ──┼────────────── M ── N
              ╲             │               ╱
               G ── H ──────┘───────────────
```

Every commit represents one Context Node.

Branches are names for particular continuations.

A merge is a node with several parents.

Historical nodes remain valid indefinitely.

The universe therefore simultaneously represents:

- actual history;
- experiments;
- alternatives;
- simulations;
- abandoned approaches;
- agent forks;
- runtime forks;
- recovered states;
- merged knowledge.

This is not merely an execution log.

It is the state-space from which continuation is possible.

---

# 4. Context Node

A **Context Node** is one complete continuation state.

Conceptually:

```ts
interface ContextNode {
  id: NodeId;
  parents: readonly NodeId[];

  state: WholeContextState;

  transition: TransitionRecord;

  schemaVersion: SchemaVersion;
  runtimeVersion: RuntimeVersion;

  provenance: Provenance;
}
```

Physically, it is a Git commit whose root tree contains the state.

```text
Git commit
│
├── parent(s)
│
└── root tree
    │
    ├── context/
    ├── agents/
    ├── memory/
    ├── runtime/
    ├── workspace/
    ├── artifacts/
    └── meta/
```

The Context Node should be considered immutable.

Once written:

> no mutation, ever.

Corrections create children.

Reversions create children.

Schema upgrades create children.

Memory corrections create children.

This gives us permanent provenance without requiring a second audit system.

---

# 5. Whole Context

The tree reachable from a Context Node is the **Whole Context**.

Example:

```text
/
├── context/
│   ├── manifest.json
│   ├── goals.json
│   ├── tasks.json
│   └── environment.json
│
├── agents/
│   ├── primary/
│   │   ├── identity.json
│   │   ├── state.json
│   │   └── policy.json
│   └── researcher/
│       └── ...
│
├── memory/
│   ├── working/
│   ├── episodic/
│   ├── semantic/
│   ├── procedural/
│   └── manifest.json
│
├── workspace/
│   └── ...
│
├── artifacts/
│   └── manifest.json
│
├── runtime/
│   ├── definition.json
│   ├── compiler.json
│   └── capabilities.json
│
└── meta/
    └── transition.json
```

Most of this tree will not change between commits.

Git therefore provides structural sharing automatically.

```text
Node A                        Node B

root A                        root B
├── agents X ─────────────────► agents X
├── workspace Y ───────────────► workspace Y
└── memory M                  └── memory M2
                                      │
                                      └── one new memory
```

Forking an enormous state is consequently almost free.

---

# 6. Git should be infrastructure, not domain API

No application code outside the Context Store should know about:

```text
git commit-tree
git mktree
git update-ref
git merge-tree
SHA-1
SHA-256
packfiles
object databases
```

Instead:

```ts
interface ContextStore {
  getNode(id: NodeId): Promise<ContextNode>;

  commit(command: CommitContext): Promise<NodeId>;

  createRef(
    ref: ContextRef,
    node: NodeId,
  ): Promise<void>;

  moveRef(
    ref: ContextRef,
    expected: NodeId,
    next: NodeId,
  ): Promise<RefUpdateResult>;

  diff(
    a: NodeId,
    b: NodeId,
  ): Promise<ContextDiff>;

  mergeBase(
    nodes: NodeId[],
  ): Promise<NodeId[]>;

  prepareMerge(
    request: MergeRequest,
  ): Promise<MergeProposal>;
}
```

`NodeId` remains opaque.

Do not expose Git hashes as semantic identifiers.

```ts
type NodeId = string & {
  readonly __brand: "NodeId";
};
```

That leaves us free to:

- change Git hash algorithms;
- migrate storage implementations;
- proxy repositories;
- introduce gitoxide/libgit2 later;
- remap IDs across replication boundaries.

### Initial implementation

Use native Git plumbing against bare repositories.

No working tree.

No:

```text
git checkout
git add
git status
```

Runtime operations should manipulate trees and commits directly.

That substantially reduces mutable state and race conditions.

---

# 7. Repository scope

Do not create one gigantic global Git repository.

Use:

> one Context Universe → one Git repository.

A universe could correspond to:

- a persistent personal agent;
- a project;
- an organization;
- a simulation;
- a long-running research process;
- a multi-agent society.

This gives natural boundaries for:

- authorization;
- garbage collection;
- replication;
- backups;
- retention;
- export;
- debugging.

Cross-universe relationships should be explicit references, not accidental shared filesystem state.

---

# 8. Large objects do not belong in Git

Git should hold:

- manifests;
- structured state;
- source files;
- small/medium artifacts;
- references;
- summaries;
- runtime definitions.

It should not become a dumping ground for:

- video;
- huge datasets;
- VM snapshots;
- model checkpoints;
- multi-gigabyte binary artifacts.

Large objects go into an object/blob store:

```text
S3
R2
GCS
MinIO
```

The Git tree contains:

```json
{
  "kind": "external-blob",
  "uri": "blob:01J...",
  "sha256": "...",
  "size": 841829138,
  "mediaType": "video/mp4"
}
```

This distinction should exist from day one.

---

# 9. Canonical, operational, derived, ephemeral

Every piece of data must belong to one of four classes.

## Canonical

Defines the persistent agent state.

Stored in the Context Universe.

Examples:

- goals;
- memories;
- agent state;
- workspace;
- policies;
- runtime definition;
- task state.

## Operational

Required to execute reliably but not part of the agent's semantic state.

Examples:

- job leases;
- worker status;
- session connections;
- Temporal execution history;
- retry counters.

Stored in PostgreSQL / Temporal.

## Derived

Can be rebuilt from canonical state.

Examples:

- vector indexes;
- full-text indexes;
- DAG query caches;
- materialized timelines;
- UI projections.

Stored in PostgreSQL/pgvector/cache.

## Ephemeral

May disappear without changing reality.

Examples:

- open tab;
- DAG zoom level;
- cursor position;
- partial streaming token buffer;
- hover state.

Stored in browser memory/local state.

This classification should be documented and enforced during reviews.

It prevents the architecture from gradually developing multiple sources of truth.

---

# 10. Session

A **Session is not a Context Universe**.

A session is an interactive environment in which humans and agents work.

```ts
interface Session {
  id: SessionId;

  participants: Participant[];

  bindings: ContextBinding[];

  surfaces: SurfaceDescriptor[];

  capabilities: SessionCapability[];

  metadata: Record<string, unknown>;
}
```

A session may:

- follow one Context branch;
- pin an old node;
- compare several nodes;
- interact with several universes;
- create a new universe;
- operate temporarily without any Context Universe.

This is what allows the frontend architecture to remain much broader than a DAG viewer.

---

# 11. Context bindings

The session does not own context.

It binds to context.

```ts
type ContextBinding =
  | {
      mode: "follow";
      universeId: UniverseId;
      ref: ContextRef;
    }
  | {
      mode: "pinned";
      universeId: UniverseId;
      node: NodeId;
    }
  | {
      mode: "compare";
      universeId: UniverseId;
      nodes: NodeId[];
    }
  | {
      mode: "none";
    };
```

This immediately enables interesting workflows.

### Follow

```text
Session → main
```

The session moves automatically as `main` advances.

### Time travel

```text
Session → node N42
```

The session observes a historical state.

### Compare

```text
Session
├── branch/research-A
├── branch/research-B
└── branch/research-C
```

### Detached exploration

A user can inspect an old state and later fork it.

---

# 12. Surface

A **Surface** is one interactive representation inside a session.

```ts
type SurfaceKind =
  | "thread"
  | "dag"
  | "artifact"
  | "document"
  | "diff"
  | "task"
  | "agent"
  | "terminal"
  | "browser"
  | "approval"
  | "timeline"
  | "form"
  | "dashboard"
  | "custom";
```

A session may contain arbitrary combinations.

```text
┌───────────────────────────────────────────────────────────┐
│ Session                                                   │
├─────────────────┬─────────────────────────────────────────┤
│                 │                                         │
│ Assistant UI    │              Artifact                   │
│ conversation    │              editor                     │
│                 │                                         │
├─────────────────┴─────────────────────────────────────────┤
│                                                           │
│                     Context DAG                           │
│                                                           │
│       ●──●──●──●                                          │
│             ╲                                             │
│              ●──●──●                                      │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

Assistant UI therefore becomes the implementation of one very important surface:

> `ThreadSurface`

not the application architecture itself.

---

# 13. Assistant UI

Use **Assistant UI with `ExternalStoreRuntime`**.

Our application owns:

- threads;
- messages;
- context bindings;
- tool state;
- execution;
- persistence.

Assistant UI owns:

- excellent conversational rendering;
- composition;
- streaming presentation;
- tool parts;
- approvals;
- attachments;
- reasoning parts;
- branch navigation;
- voice/interactions;
- custom message components.

The adapter boundary should be explicit:

```text
Session Projection
       │
       ▼
AssistantUIAdapter
       │
       ▼
ExternalStoreRuntime
       │
       ▼
Assistant UI components
```

Never make Assistant UI's internal thread representation canonical.

Its message branching is a UI affordance.

Context branching is a reality transition.

They may sometimes correspond, but they are not identical.

---

# 14. Universal interaction model

The backend should not fundamentally speak "chat".

It should speak:

```text
commands
events
projections
```

## Commands

A command expresses intent.

```ts
type RuntimeCommand =
  | SendMessage
  | InvokeAgent
  | CallTool
  | ApproveAction
  | EditArtifact
  | CommitMemory
  | ForkContext
  | CheckoutContext
  | MergeContexts
  | SpawnAgent
  | OpenSurface
  | UpdateSurface;
```

Commands may or may not modify Context state.

## Events

Events report what occurred.

```ts
type SessionEvent =
  | MessageStarted
  | MessageDelta
  | MessageCompleted
  | ToolRequested
  | ToolStarted
  | ToolCompleted
  | ContextCommitted
  | ContextForked
  | ContextMerged
  | AgentSpawned
  | ArtifactCreated
  | ApprovalRequested
  | SurfaceOpened
  | SurfaceUpdated
  | RuntimeFailed;
```

## Projections

A projection converts the underlying system into something useful for one consumer.

Examples:

```text
ThreadProjection
DagProjection
TimelineProjection
TaskProjection
AgentProjection
AssistantUIProjection
```

This gives us an extremely extensible frontend without changing the core.

---

# 15. Session events are not Context events

This distinction should remain explicit.

```text
User changes DAG zoom
→ session state only

User opens document
→ session state only

User sends message to agent
→ Context transition

Agent calls search tool
→ Context transition/provenance

User edits working memory
→ Context transition

Agent produces an artifact
→ Context transition

User switches active tab
→ session state only
```

A useful heuristic:

> Would this change what the agent can know, believe, access, or do on its next continuation?

If yes, Context.

If no, Session.

---

# 16. Context compiler

The LLM should never receive the Whole Context directly.

It receives a compiled projection.

```text
Whole Context Node
        │
        ▼
Context Compiler
        │
        ├── identity
        ├── current task
        ├── policies
        ├── recent history
        ├── selected memories
        ├── relevant artifacts
        ├── environment
        ├── tool capabilities
        └── budget constraints
        │
        ▼
Invocation Context
```

The compiler should eventually be one of the most important modules in the system.

```ts
interface ContextCompiler {
  compile(
    node: NodeId,
    request: CompilationRequest,
  ): Promise<CompiledContext>;
}
```

Every compiled element should retain provenance:

```ts
interface CompiledItem {
  content: unknown;

  source:
    | ContextPath
    | MemoryId
    | ArtifactId
    | NodeId;

  reason: string;

  priority: number;

  estimatedTokens: number;
}
```

This means we can later answer:

> Why did the model see this?

and:

> Why did the model not see that?

Context debugging becomes possible.

---

# 17. Model layer

Use **AI SDK Core** as the default provider abstraction.

But deliberately use its lower-level primitives.

```text
generateText
streamText
generateObject / structured output
tool definitions
embeddings
provider registry
```

Do not let the model SDK own:

- persistence;
- memory;
- tool authorization;
- the agent loop;
- branching;
- retries of external actions;
- context compilation.

The desired relationship is:

```text
Context Runtime
      │
      ▼
AI SDK
      │
 ┌────┼────┐
 ▼    ▼    ▼
OpenAI Anthropic Gemini ...
```

ADK remains an optional execution adapter for cases where its ecosystem or orchestration is useful.

---

# 18. Invocation

An **Invocation** is one model computation.

It should be fully reproducible as data, even though the model itself may be nondeterministic.

Record:

```ts
interface InvocationRecord {
  id: InvocationId;

  node: NodeId;

  agent: AgentId;
  model: ModelDescriptor;

  compilerVersion: string;

  compiledContext: ArtifactRef;

  toolDefinitions: ArtifactRef;

  request: ArtifactRef;
  response: ArtifactRef;

  usage: TokenUsage;

  startedAt: Timestamp;
  finishedAt: Timestamp;
}
```

Do not store hidden model reasoning.

Do store everything needed to explain the observable computation.

---

# 19. Transition engine

Models do not mutate state.

Humans do not mutate state.

Tools do not mutate state.

They propose transitions.

```text
proposal
   │
   ▼
validate
   │
   ▼
authorize
   │
   ▼
reduce
   │
   ▼
commit
```

```ts
interface TransitionEngine {
  propose(input: Proposal): Promise<ProposedTransition>;

  validate(
    node: NodeId,
    transition: ProposedTransition,
  ): Promise<ValidatedTransition>;

  apply(
    node: NodeId,
    transition: ValidatedTransition,
  ): Promise<NodeId>;
}
```

This is the security and correctness boundary.

---

# 20. Reducers

State changes should preferably be deterministic.

```ts
type Reducer<TTransition> = (
  current: WholeContextView,
  transition: TTransition,
) => Promise<StatePatch>;
```

Examples:

```text
MemoryWriteReducer
TaskUpdateReducer
ArtifactWriteReducer
AgentSpawnReducer
WorkspacePatchReducer
CapabilityChangeReducer
EnvironmentObservationReducer
```

The reducer produces a patch.

The Context Store creates the resulting Git tree and commit.

---

# 21. Commit granularity

Do not create a Git commit for every streamed token.

Do create Context commits at meaningful causal boundaries.

Recommended initial policy:

Commit when:

- external input enters persistent agent state;
- a model invocation completes and materially affects continuation;
- a tool with meaningful output completes;
- an external side effect occurs;
- memory changes;
- an artifact changes;
- an agent is spawned/merged;
- permissions change;
- runtime configuration changes;
- compaction occurs.

Do not commit:

- streamed token deltas;
- UI animation;
- speculative rendering;
- temporary parsing buffers.

A single agent "turn" may therefore produce multiple Context Nodes.

That is acceptable.

Commit policy itself should eventually be configurable and versioned.

---

# 22. Memory

Memory is part of Whole Context.

But retrieval indexes are not.

```text
Context Node
    │
    └── memory manifest
           │
           ├── working
           ├── episodic
           ├── semantic
           ├── procedural
           ├── relational
           └── identity
```

A memory object includes provenance.

```ts
interface MemoryRecord {
  id: MemoryId;

  kind: MemoryKind;

  content: ObjectRef;

  sources: SourceRef[];

  confidence?: number;

  status:
    | "candidate"
    | "active"
    | "contested"
    | "superseded";

  supersedes?: MemoryId[];
}
```

Never silently overwrite memory.

Correction means:

```text
M1 active
  ↓
M2 supersedes M1
```

History remains inspectable.

---

# 23. Retrieval

Start with:

```text
PostgreSQL
+ pgvector
+ PostgreSQL FTS
```

Use hybrid retrieval.

Later introduce more specialized infrastructure only when measurements justify it.

Retrieval should combine:

```text
semantic similarity
keyword relevance
recency
provenance
branch ancestry
memory status
agent access
task relevance
```

Retrieval returns references into canonical state.

It never becomes canonical state itself.

Indexes must always be rebuildable.

---

# 24. Compaction

Compaction is a state transition, not deletion.

```text
N1 → N2 → N3 → N4 → N5
                   │
                   └── compact → N6
```

N6 may use:

```text
summary(N1...N4)
+ unresolved obligations
+ important events
+ active memories
+ references to source nodes
```

But N1...N4 still exist.

A later compiler can choose to inspect them again.

Every compaction record should state:

- source range;
- compiler/compactor version;
- summary;
- retained facts;
- omitted information;
- provenance;
- confidence where meaningful.

This makes compaction reversible in principle.

---

# 25. Branches

Branches are cheap and should be used liberally.

Examples:

```text
main
experiment/context-compiler-v4
counterfactual/buy-vs-build
agent/researcher-17
simulation/market-crash
recovery/pre-bad-tool-call
```

Do not assume every branch will merge.

Branches may be:

```ts
type BranchDisposition =
  | "mainline"
  | "experiment"
  | "merge-likely"
  | "temporary"
  | "archive"
  | "simulation";
```

Branch metadata belongs in application state, not Git branch names alone.

---

# 26. Merge

Git gives us ancestry and structural three-way merging.

It does not give us semantic merging.

Merge therefore has two layers.

```text
Git-level merge
      +
Domain merge policies
```

Each state type declares one of:

```ts
type MergeStrategy =
  | "identical"
  | "union"
  | "three-way"
  | "crdt"
  | "semantic"
  | "manual"
  | "forbidden";
```

Examples:

```text
event sets             union
independent artifacts  union
source files           three-way
task graphs            domain three-way
beliefs                semantic
identity commitments   manual
permission expansion   forbidden automatically
secrets                 never merged through Context
```

Conflict is first-class.

Never hide unresolved disagreement behind an automatically generated summary.

---

# 27. Merge workflow

```text
               common ancestor
                     │
             ┌───────┴───────┐
             ▼               ▼
         branch A        branch B
             │               │
             └───────┬───────┘
                     ▼
             structural diff
                     │
                     ▼
           automatic resolution
                     │
                     ▼
           semantic resolution
                     │
                     ▼
              conflict set
                     │
            ┌────────┴─────────┐
            ▼                  ▼
       human/agent         clean merge
       reconciliation          │
            │                  │
            └────────┬─────────┘
                     ▼
                 merge node
```

Semantic merge agents may propose resolutions.

They do not bypass validation.

---

# 28. Agent model

An agent is not necessarily a process.

It is persistent state plus a way to compile that state into action.

```ts
interface AgentState {
  identity: ObjectRef;
  policy: ObjectRef;

  workingState: ObjectRef;

  memoryScope: MemoryScope;

  capabilityScope: CapabilityScope;

  compilerProfile: CompilerProfile;
}
```

The Whole Context can contain many agents.

```text
Context Node
├── Agent A
├── Agent B
├── Agent C
└── shared environment
```

Each agent sees a different compiled view of the same state.

---

# 29. Agent fork

Forking an agent should be cheap.

```text
Agent A
   │
   ├── A.1 explores design
   │
   └── A.2 explores implementation
```

Inheritance policy is explicit.

```ts
interface AgentForkPolicy {
  identity: "copy" | "derive" | "new";

  workingMemory:
    | "all"
    | "none"
    | "selected";

  semanticMemory:
    | "shared"
    | "copy"
    | "selected";

  episodicMemory:
    | "all"
    | "none"
    | "selected";

  capabilities: CapabilityId[];
}
```

Agent fork and Context branch can coincide, but need not.

---

# 30. Runtime itself is versioned

Most runtime semantics belong inside the Whole Context:

```text
context compiler
agent definitions
memory policy
tool policy
merge policy
planning policy
model routing policy
runtime configuration
```

The runtime may therefore fork itself.

```text
R1
├── compiler A
└── compiler B
```

This lets us evaluate runtime evolution from identical starting states.

The minimal execution kernel remains outside.

---

# 31. Minimal kernel

The external kernel should remain intentionally stupid.

It owns:

- Git repository access;
- object verification;
- schema bootstrapping;
- secret resolution;
- process/container isolation;
- authorization boundary;
- execution limits;
- runtime loading.

It does not own:

- goals;
- memory;
- reasoning;
- planning;
- context selection;
- identity;
- merge semantics.

This protects us from infinite self-reference and unsafe self-modification.

---

# 32. Capabilities, not credentials

Never commit secrets into Git.

Store:

```json
{
  "capability": "google-calendar.write",
  "grant": "cap_82h...",
  "scope": ["calendar:primary"]
}
```

The external kernel resolves:

```text
cap_82h...
      ↓
actual credential
```

This permits:

- revocation;
- audit;
- branch-specific permission;
- safe export of repositories;
- permission simulation.

Capabilities should themselves be versioned state.

Credentials should not.

---

# 33. Tool runtime

Tools should expose typed capabilities.

```ts
interface ToolDefinition<Input, Output> {
  id: ToolId;

  inputSchema: Schema<Input>;
  outputSchema: Schema<Output>;

  sideEffect:
    | "none"
    | "reversible"
    | "external";

  execute(
    input: Input,
    context: ToolExecutionContext,
  ): Promise<Output>;
}
```

A model produces:

```text
tool proposal
```

The runtime checks:

```text
schema
capability
policy
human approval
idempotency
```

before execution.

MCP tools are adapted into the same internal interface.

Native tools remain preferable for critical internal functionality.

---

# 34. Durable execution

Do not begin by building the entire system around Temporal.

Create an abstraction first:

```ts
interface ExecutionEngine {
  run(command: ExecutionCommand): Promise<ExecutionHandle>;
}
```

Initial implementation:

```text
Node process
+ PostgreSQL jobs
```

Later production implementation:

```text
Temporal
```

Temporal should provide:

- crash recovery;
- durable timers;
- human waits;
- reliable activity retry;
- long-running workflows.

Temporal history remains operational state.

Context history remains semantic state.

Never confuse the two.

---

# 35. Frontend architecture

Use a normal React application with a central Session Runtime.

```text
React App
   │
   ▼
Session Runtime
   │
   ├── session state
   ├── context bindings
   ├── server projections
   ├── event stream
   └── commands
   │
   ├────────► Assistant UI adapter
   │
   ├────────► DAG explorer
   │
   ├────────► artifact surfaces
   │
   ├────────► terminal
   │
   └────────► custom surfaces
```

Recommended:

```text
Next.js
React
Assistant UI
React Flow
TanStack Query
Zustand
```

Responsibilities:

### TanStack Query

Remote/query state.

### Zustand

Ephemeral session/UI state.

### Assistant UI

Thread interaction.

### React Flow

DAG visualization.

Avoid duplicating canonical backend state in Zustand.

---

# 36. Transport

Prefer simple protocols.

## Commands

HTTP JSON.

## Queries

HTTP JSON.

## Streaming events

Server-Sent Events initially.

SSE is simpler than WebSockets for:

- model streaming;
- tool events;
- Context commits;
- session event feeds.

Use WebSockets only where genuinely bidirectional realtime behavior is needed:

- shared terminals;
- collaborative cursors;
- multiplayer editing;
- low-latency presence.

Do not default everything to WebSockets.

---

# 37. Wire protocol

Keep the network contract framework-independent.

Avoid making tRPC types the enduring protocol.

Define stable schemas:

```ts
interface CommandEnvelope {
  commandId: string;
  sessionId: SessionId;

  type: string;
  payload: unknown;

  expectedNode?: NodeId;
}
```

and:

```ts
interface EventEnvelope {
  sequence: number;
  eventId: string;

  sessionId: SessionId;

  type: string;
  payload: unknown;

  timestamp: string;
}
```

Generate JSON Schema/OpenAPI where useful.

A Rust service should be able to implement the protocol later without importing the TypeScript application.

---

# 38. Optimistic concurrency

Every mutation against a followed Context ref should contain:

```text
expected head
```

Example:

```ts
commit({
  ref: "main",
  expected: nodeA,
  transition,
});
```

Git CAS ref update determines whether it succeeds.

If another transition already advanced `main`:

```text
expected A
actual B
```

the runtime must not silently overwrite it.

It can:

- retry on B;
- create a branch;
- ask for resolution;
- automatically merge if safe.

Concurrency therefore naturally creates explicit branches instead of hidden races.

---

# 39. PostgreSQL

PostgreSQL is the control plane and query accelerator.

Use it for:

```text
users
permissions
universes
sessions
session events
branch metadata
node indexes
node ancestry caches
search
memory retrieval indexes
artifact metadata
jobs
leases
invocations
observability metadata
```

Git remains canonical for Whole Context.

Postgres projections must be rebuildable wherever possible.

---

# 40. Git indexing

Do not repeatedly walk enormous Git histories for frontend queries.

Maintain a node index:

```text
node_id
universe_id
parent_ids
generation
timestamp
transition_type
actor
runtime_version
summary
```

This allows:

```text
find children
find ancestors
show graph
search transition types
filter agents
find merges
```

without expensive Git traversal.

Git answers truth.

Postgres answers questions quickly.

---

# 41. Observability

Use OpenTelemetry.

Every important span should carry:

```text
universe.id
node.id
node.parents
context.ref
session.id
agent.id
invocation.id
transition.id
tool.id
runtime.version
compiler.version
```

Operational traces can then be correlated with semantic state.

The DAG explorer should ultimately support:

```text
select node
  → inspect state
  → inspect diff
  → inspect compiled context
  → inspect model invocation
  → inspect tool calls
  → inspect telemetry
  → fork here
```

That becomes a genuinely new debugging environment for agents.

---

# 42. Evaluation becomes branching

Do not treat evaluation as only:

```text
prompt → answer → score
```

The runtime lets us test:

```text
same node
   │
   ├── model A
   ├── model B
   ├── compiler A
   ├── compiler B
   ├── memory strategy A
   └── memory strategy B
```

and compare resulting trajectories.

Metrics can include:

- correctness;
- cost;
- time;
- number of tool calls;
- state quality;
- memory quality;
- downstream success;
- reversibility;
- branch divergence.

This should eventually become one of the major advantages of the architecture.

---

# 43. Schema evolution

Never rewrite historical nodes merely because schemas changed.

A node declares:

```text
schemaVersion
runtimeVersion
```

Readers support historical schemas.

If an old state needs upgrading:

```text
Old Node
   │
   └── schema_upgrade
            │
            ▼
        New Node
```

The migration itself becomes provenance.

This is slower than destructive migration.

It is vastly more correct for a system whose defining property is historical continuity.

---

# 44. Modular monolith first

Do not begin with microservices.

Initial deployment:

```text
apps/
├── web
├── server
└── worker
```

with shared packages.

One PostgreSQL.

One Git storage service/module.

One object store.

This is enough for substantial scale.

Only split a component into a service when there is a concrete reason:

- different scaling characteristics;
- security isolation;
- different language/runtime;
- independent deployment requirement;
- operational bottleneck.

Architecture boundaries should exist in code before they become network boundaries.

---

# 45. Initial repository

Keep the package structure restrained.

```text
context-runtime/
├── apps/
│   ├── web/
│   ├── server/
│   └── worker/
│
├── packages/
│   ├── domain/
│   ├── context-store/
│   ├── runtime/
│   ├── compiler/
│   ├── memory/
│   ├── execution/
│   ├── session/
│   ├── projections/
│   ├── ai/
│   ├── tools/
│   ├── assistant-ui/
│   └── observability/
│
├── specs/
│   ├── ontology.md
│   ├── context-store.md
│   ├── transitions.md
│   ├── merging.md
│   ├── sessions.md
│   ├── wire-protocol.md
│   └── security.md
│
└── examples/
```

Avoid creating thirty tiny packages before the boundaries have earned their existence.

---

# 46. Implementation sequence

The implementation should proceed by proving one invariant at a time.

## Stage 0 — Specification

Before framework work, write and freeze:

```text
Context Node
Whole Context
Context Universe
Transition
Session
Context Binding
Surface
Invocation
Capability
```

Also document:

```text
canonical vs operational vs derived vs ephemeral
```

This prevents ontology drift.

---

## Stage 1 — Git Context Store

Implement only:

```text
create universe
commit node
read node
create ref
CAS move ref
fork
diff
ancestry
merge-base
```

No LLM.

No Assistant UI.

No memory retrieval.

Acceptance test:

```text
A → B → C
    ├→ D → E
    └→ F

merge(E, F) → M
```

and every node can be checked out and diffed.

---

## Stage 2 — Transition engine

Add:

```text
commands
validation
reducers
provenance
structured transitions
```

Create state transitions without models.

Acceptance tests:

- concurrent ref updates cannot overwrite;
- invalid transitions cannot commit;
- all state changes are attributable;
- unchanged tree portions structurally share.

---

## Stage 3 — Session runtime

Implement:

```text
Session
ContextBinding
Surface
CommandEnvelope
EventEnvelope
SSE
```

Build a tiny frontend showing:

```text
session
+ Context branch
+ DAG
+ node inspector
```

Acceptance test:

A session can:

- follow a branch;
- pin a historical node;
- fork it;
- switch back to main.

---

## Stage 4 — Assistant UI

Integrate Assistant UI through `ExternalStoreRuntime`.

Implement:

```text
ThreadProjection
message streaming
attachments
tool parts
approval parts
```

Messages remain session projections.

Acceptance test:

Two different Thread surfaces can present different projections over the same underlying Context Universe.

---

## Stage 5 — Model invocation

Add AI SDK Core.

Implement:

```text
ContextCompiler
InvocationRecord
model providers
structured tool proposals
stream events
```

Acceptance test:

```text
Context Node
→ compile
→ model
→ transition
→ new Context Node
```

with complete provenance.

---

## Stage 6 — Tool runtime

Add:

```text
typed internal tools
MCP adapter
capabilities
approval
idempotency
sandbox boundary
```

Acceptance test:

An external side effect can be traced from:

```text
node
→ invocation
→ proposal
→ authorization
→ tool execution
→ result
→ next node
```

---

## Stage 7 — Memory

Implement canonical memory plus:

```text
Postgres FTS
pgvector
hybrid retrieval
supersession
contradiction
provenance
```

Acceptance test:

The entire retrieval index can be deleted and reconstructed without loss of semantic memory.

---

## Stage 8 — Compaction

Implement:

```text
history summaries
obligation extraction
source provenance
reversible compaction
```

Acceptance test:

A compacted branch can still recover source history and be recompiled using a different compaction strategy.

---

## Stage 9 — Domain merge

Implement merge-policy registry:

```text
union
three-way
semantic
manual
forbidden
```

Build explicit conflict representation.

Acceptance test:

Two agent branches can diverge substantially and merge without silently discarding conflicting state.

---

## Stage 10 — Multi-agent

Add:

```text
AgentGraph
agent spawning
private/shared state
context scopes
agent fork
agent merge
```

At this point the architecture becomes substantially more than an agent SDK.

---

## Stage 11 — Durable execution

Introduce Temporal when execution semantics actually require it.

Do not change domain contracts.

Replace:

```text
LocalExecutionEngine
```

with:

```text
TemporalExecutionEngine
```

The Context Runtime should largely not care.

---

# 47. First complete demonstration

The first serious demo should exercise the ontology rather than merely generate an impressive chatbot answer.

Start:

```text
N0
```

User asks the agent to design something.

The agent works until:

```text
N5
```

Then the user selects:

> explore two approaches.

Runtime creates:

```text
N5
├── refs/approach-A
└── refs/approach-B
```

Two agents work independently.

```text
A1 → A2 → A3
B1 → B2 → B3 → B4
```

The UI simultaneously shows:

- Assistant UI conversations;
- artifacts;
- tool executions;
- DAG;
- live branch state.

The user selects both branches and requests comparison.

The runtime produces:

```text
Merge Proposal
```

with:

- agreements;
- conflicting assumptions;
- differing artifacts;
- memory changes;
- recommended reconciliations.

User accepts.

```text
A3 ───┐
      ├── M1 → continuation
B4 ───┘
```

Then the user time-travels to `N5`, creates approach C, and compares it with the previously merged state.

If this feels natural rather than hacked together, the architecture works.

---

# 48. Things we explicitly should not build yet

Do not initially build:

- a custom Git implementation;
- CRDT everything;
- a custom vector database;
- microservices;
- distributed consensus;
- complex A2A infrastructure;
- learned context compression;
- automatic semantic merging everywhere;
- runtime self-modification;
- arbitrary frontend plugins;
- custom workflow language;
- custom model-provider abstraction;
- global shared Git repository.

Create interfaces where those things may someday belong.

Do not implement them until the system asks for them.

---

# 49. Engineering laws

The following should effectively function as project laws.

### 1. One semantic source of truth

If it determines future agent continuation, it belongs in Context.

### 2. History is immutable

Never fix history. Add another transition.

### 3. Derived state is disposable

Indexes, embeddings and projections must be rebuildable.

### 4. Models propose; runtime commits

No model directly mutates reality.

### 5. Frameworks are adapters

Assistant UI, AI SDK, ADK, Temporal and MCP do not define our ontology.

### 6. Preserve provenance

A useful state whose origin cannot be explained is corrupted state.

### 7. Compaction does not destroy

Summaries optimize continuation, not history.

### 8. Conflict is information

Do not erase disagreement merely to make state look consistent.

### 9. Capabilities are explicit

Agents receive permissions, never ambient authority.

### 10. Prefer structural simplicity

A modular monolith with clear contracts is superior to premature distributed elegance.

### 11. Make concurrency visible

Conflicting continuations should create branches, not accidental overwrites.

### 12. Model context is a view

Whole Context is reality. Invocation Context is one projection.

---

# 50. Final architecture

```text
                              HUMAN / AGENTS
                                   │
                                   ▼
                        ┌───────────────────────┐
                        │       SESSION         │
                        │                       │
                        │ participants          │
                        │ bindings              │
                        │ surfaces              │
                        └──────────┬────────────┘
                                   │
             ┌─────────────────────┼──────────────────────┐
             │                     │                      │
             ▼                     ▼                      ▼
      Assistant UI             DAG UI               Other surfaces
        Thread                  React Flow           docs/tasks/etc.
             │                     │                      │
             └─────────────────────┼──────────────────────┘
                                   │
                         commands / projections
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       CONTEXT RUNTIME        │
                    │                              │
                    │ transitions                  │
                    │ reducers                     │
                    │ compiler                     │
                    │ memory                       │
                    │ merge                        │
                    │ capabilities                 │
                    └───────┬───────────┬──────────┘
                            │           │
                        inference    execution
                            │           │
                            ▼           ▼
                       AI SDK Core   ExecutionEngine
                            │           │
                      ┌─────┼─────┐   Temporal later
                      ▼     ▼     ▼
                   OpenAI Claude Gemini
                            │
                            │
                            ▼
                    ┌──────────────────────┐
                    │   CONTEXT STORE      │
                    │                      │
                    │ Git Context Universe │
                    │ commits / trees      │
                    │ refs / merges        │
                    └─────────┬────────────┘
                              │
              ┌───────────────┼─────────────────┐
              │               │                 │
              ▼               ▼                 ▼
           PostgreSQL       Blob Store       Secret Store
           indexes          large data       capabilities
           sessions
           projections
```

At the center of the entire system there is only one really unusual idea:

```text
A persistent intelligence is a trajectory through
a versioned space of possible whole states.
```

Git gives that trajectory durable structure.

The Context Runtime gives the states semantics.

The compiler turns a state into cognition.

Execution turns cognition into transitions.

Sessions let humans and agents inhabit and manipulate those trajectories.

Surfaces allow that interaction to take whatever form is appropriate.

That is the architecture I would build.