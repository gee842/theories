# Actor model state machines and transition hooks

created: 2026-04-28T11:12:16.943346Z  uuid: adab9a9f-196a-4ec4-bab8-b18a4bf32ce4  export: new
messages: 9  total_chars: 29935  human_chars: 581


---
**HUMAN** (2026-04-28T11:12):

I'll update

---
**HUMAN** (2026-04-28T11:13):

Uh, there, this, uh, kind of, uh, actor model where actor has internal state, like state machines, and they transition. And, uh, once transition happens before and after, there is a hook that can trigger. And are there those kind of designs of what kind of state a agent should have? Look into it.

---
**ASSISTANT** (2026-04-28T11:13):

Got it—you want me to search for agent state machine designs with hooks for state transitions. This is relevant to OpenClaw's agent architecture, right?
```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```



So yeah, solid design patterns exist here. The main patterns are Akka's actor framework with `OnTransition` handlers that fire between states—they're stacked so you can intersperse them—plus XState and the state design pattern. For agent-specific stuff, frameworks like Stately and LangGraph track state as a first-class concern with built-in hooks at pre-execution and post-execution points. Arize and other frameworks expose trace hooks for every state transition.

The hookable approach resonates with what you're building: before a transition fires, you can validate or modify, and after it completes, you trigger side effects. That lines up well with the SST loop structure for OpenClaw.

Want me to dig deeper into how this maps to your agent architecture, or should I focus on a specific framework like XState's approach?

---
**HUMAN** (2026-04-28T11:14):

Explain the state graph and cycles

---
**ASSISTANT** (2026-04-28T11:14):

  Now I'm thinking through how to explain state graphs and cycles for agent architectures—the core idea is that states are nodes and transitions are edges, and cycles represent loops where agents can return to previous states, which is essential for the agent loop itself. pattern
3. How this applies to agents specifically

Let me think about what's relevant to the SST (Sprite-Space-Token) architecture and OpenClaw context. The agent loop is fundamental: perceive → think → act → observe → think... This is itself a cycle.

I should think about:
- DAG vs cyclic state graphs (LangGraph started DAG, moved to support cycles)
- Self-loops
- The classic ReAct loop (reason-act)
- Hierarchical state machines (HSM)
- Parallel/concurrent states

Let me think about the format. This is a conceptual explanation, mobile interface, so I should be concise but substantive. The user asked to "explain" so this is a meaty topic. Let me aim for 2-3 paragraphs maybe with some light structure if it really helps.

Actually, given this is a meaty technical topic and the user seems to want depth (they've been asking probing questions), I think a slightly longer response with some structure makes sense. But not overly formatted - keep it conversational since it's mobile.

Now I'm getting into the core mechanics: in a state graph, nodes represent different states like planning or executing, and edges define how the system transitions between them. The real power for agents comes from cycles—paths that loop back, which is what makes iterative behavior possible. Without cycles you just have a one-shot pipeline, but with them you get the classic agent pattern of planning, executing, observing, and planning again. The trick is preventing infinite loops through guards and termination conditions like iteration limits or goal checks. LangGraph specifically added cycle support because agents fundamentally need that iterative structure to work.A **state graph** is just the topology of your state machine: nodes are states (Idle, Planning, Executing, Waiting, Reflecting, Done, Error...) and edges are transitions between them. Each edge can carry a guard (condition that must hold to fire), an event trigger, and actions. The hooks we discussed earlier attach at three natural points: on-exit of the source state, on-transition (the edge itself), and on-entry of the target state. The graph defines the *space of possible trajectories* your agent can take—everything not on the graph is impossible by construction, which is the safety property you get for free.

**Cycles** are paths that return to a state already visited. They're the difference between a *pipeline* (a DAG, one-shot) and an *agent* (iterative, goal-seeking). LangGraph explicitly forked away from a pure DAG model precisely because agentic behavior requires cycles—you can't ReAct without looping back. The canonical agent cycles look like:

- **ReAct loop**: Thought → Action → Observation → Thought...
- **Plan-Execute-Observe**: Plan → Execute → Observe → (Replan or Continue)
- **Perceive-Decide-Act**: classic control loop, runs forever
- **Self-loop**: a state transitions to itself, used for polling, retry, or accumulation

Each iteration of a cycle, the agent's *state graph topology stays fixed*, but its *internal memory/context evolves*—plan gets refined, observations accumulate, confidence updates. That's the key insight: the FSM is the skeleton, the memory is the muscle that changes shape inside it.

The hard problem with cycles is **termination**. Without exit guards you get runaway loops (the failure mode of every early agent demo). The standard mitigations are: max-iteration counters, goal-satisfaction predicates that check "are we done?", token/cost budgets, and stagnation detection (no progress for N steps → abort). In the SST framing, your Sprite is essentially the cycle controller, and the Token boundary is a natural place to evaluate whether to loop again or terminate.

Want me to sketch how this maps onto OpenClaw's SST loop specifically, or draw out a concrete state graph for a typical agent?

---
**HUMAN** (2026-04-28T11:15):

I mean for the existing implementations, how do people implement them? What kind of designs are there, in terms of state machine actor architecture

---
**ASSISTANT** (2026-04-28T11:16):

  I need to look at how real-world state machine and actor frameworks actually implement their architectures—XState, Akka, Erlang/OTP, LangGraph, and similar tools—to give the user concrete examples rather than abstract theory.
```
This block is not supported on your current device yet.
```

 I should look at how Akka, Erlang OTP's gen_statem, and LangGraph handle state machines to understand the canonical patterns for this kind of implementation.
```
This block is not supported on your current device yet.
```

 I've got enough material to provide a comprehensive overview. Let me organize this around the actual implementation patterns I've found—starting with Erlang's gen_statem as the foundational actor-FSM model, then moving into how Akka adapted that approach.

From there I can map out the design trade-offs: whether state lives as data (like Erlang's atoms) versus as objects (OO pattern), the distinction between Mealy and Moore machines, how different frameworks handle callbacks and hooks, and which ones support hierarchical states. I'll also touch on how actors handle event queues through selective receive, and how persistence strategies differ across these approaches.The canonical implementations cluster into a few distinct lineages, and the design choices they make are pretty illuminating.

**Erlang/OTP `gen_statem`** is the gold standard for actor+FSM and worth studying carefully because it's been battle-tested for decades in telecom. An actor process holds two things: a state name (atom) and a Data term. Events arrive via the mailbox and dispatch through a callback function. It offers two *callback modes*: `state_functions` (one function per state, function name = state name) or `handle_event_function` (single dispatcher that pattern-matches on state + event). The first scales better when you have many states with distinct behavior; the second is better when transitions are uniform. Critically, it supports **selective receive / event postponement**—if a message doesn't apply in the current state, you can postpone it back into the mailbox and it'll be re-delivered when you reach a state that handles it. This is huge for agent design because it means out-of-order tool results don't crash the agent—they just wait.

**Akka FSM** (Scala/JVM, descended from Erlang) is the reference for stacked transition hooks. You declare states and transitions, then register `OnTransition((from, to) => ...)` handlers that fire between states. Multiple handlers stack and can be interspersed with state-specific `when` blocks, so cross-cutting concerns (logging, persistence, metrics) attach orthogonally to business logic.

**XState / Stately** is the modern JS take, explicitly built on the SCXML spec which gives you hierarchical statecharts (states-within-states), parallel regions, history states, and guards. Actors are first-class: a machine becomes an actor when interpreted, and machines spawn child actor machines that communicate by message-passing. The actors-all-the-way-down pattern means your whole app is a tree of communicating FSMs. Restate extends this with durable execution—the state machine persists across crashes and restarts.

**LangGraph** is the agent-specific one. Nodes are functions, edges are transitions, and—unlike workflow DAGs—it explicitly supports cycles for ReAct-style loops. State is a single typed dict that flows through the graph; each node returns a partial update that gets merged. Hooks come via callbacks and interrupts (human-in-the-loop pauses).

**State design pattern (OO)** is the lowest-level building block: a Context holds a reference to a State object; events are delegated to the State, which returns the next State. Transitions live inside State methods. This is what you'd hand-roll without a framework.

The design axes that actually matter when you're choosing between them:

- *State representation*: atom + data blob (Erlang, lightweight, easy to serialize) vs. State-as-class (OO pattern, polymorphic dispatch but harder to persist) vs. config object (XState, declarative, visualizable)
- *Mealy vs Moore*: actions tied to transitions (Mealy, Akka's `OnTransition`) vs. actions tied to state entry/exit (Moore, gen_statem's `state_enter` calls). Most modern frameworks support both.
- *Hook placement*: `before-transition`, `on-transition`, `after-transition`, `on-entry`, `on-exit`. Stackable hooks (Akka) vs. single override (basic OO).
- *Event handling under state mismatch*: crash (pure FSM), drop, or postpone (gen_statem)—the postpone semantics are the killer feature for agents.
- *Hierarchy*: flat states vs. nested/parallel statecharts (XState). Hierarchy lets you factor common transitions to a parent state.
- *Persistence boundary*: in-memory only (Akka FSM) vs. snapshotted at every transition (Restate, durable execution frameworks).

For OpenClaw's SST loop, the gen_statem model is probably the closest fit conceptually—Sprite as the actor process, Space as the Data term, Token boundaries as the natural transition points where postpone/dispatch decisions get made. Want me to sketch how the postpone semantics specifically would handle out-of-order Tokens?

---
**HUMAN** (2026-04-28T11:21):

Explain the design of each in depth, I know the theory, I am looking for engineering answers

---
**ASSISTANT** (2026-04-28T11:23):

  I need to shift focus toward the implementation details rather than the conceptual overview—the user already understands the theory, so I should dig into the actual mechanics like Erlang's receive loop and mailbox handling, how Akka dispatches callbacks on the JVM, and XState's transition function signatures and actor spawning.

Before diving into the explanations, I should verify some specifics around LangGraph's Pregel-style execution and channel reducers, XState v5's persistence model, and the exact details of how gen_statem handles postponed messages and state entry callbacks, since those are the trickier implementation details to get right.
```
This block is not supported on your current device yet.
```

 Now let me verify the Akka FSM implementation details as well.
```
This block is not supported on your current device yet.
```

 Now I'm ready to dive into the implementation details—focusing on the actual data structures, how the runtime processes each cycle, which dispatch mechanism routes events to handlers, how state persists across restarts, and the threading architecture underneath it all. , what locks
6. **Hook insertion** - what's the mechanism, how does it compose

Let me structure this as 5 sections, one per implementation, going deep into engineering. The user said they know theory and want engineering answers. So I should drop the conceptual fluff and dive into mechanics.

Let me draft each section:

**1. Erlang gen_statem**
- The actor is a process (BEAM lightweight process, ~300 bytes overhead, own heap)
- State stored as `{StateName :: atom(), Data :: term()}`
- Driven by a receive loop in OTP behavior code (gen_statem.erl)
- Mailbox: process-private FIFO queue, message arrival appends, receive scans
- Dispatch: callback module exports either:
  - `state_functions` mode: one function per state name, exported with arity 3 `StateName(EventType, EventContent, Data)`
  - `handle_event_function` mode: single `handle_event/4` that pattern matches on (EventType, EventContent, StateName, Data)
- Return value from callback is a tuple like `{next_state, NewStateName, NewData, Actions}`
- Actions are a list of side effects: `{reply, From, Reply}`, `postpone`, `{state_timeout, Time, Msg}`, `{next_event, Type, Content}`, etc.
- **Postpone**: marked event goes back into a postpone queue inside the state machine; on next state transition, postponed events are re-prepended to the front of the mailbox
- **state_enter** mode: special callback called with EventType=enter on every state change, including S->S
- Lives inside a supervision tree; on crash, supervisor restarts the actor with init args (state is lost unless explicitly persisted)

**2. Akka FSM**
- Built on Actor trait; FSM[S, D] extends Actor
- Internal mutable fields track current state, next state, generation counter, and any active timeout futures
- Handler storage uses a map of state to partial functions, registered via when() for individual states, plus a fallback handler for any state
- Defining state handlers... ]]` - whenUnhandled, single (not stacked!)
  - `transitionEvent: List[PartialFunction[(S, S), Unit]]` - stacked, all tried on transition
  - `terminateEvent: PartialFunction[StopEvent, Unit]` - single
- Dispatch:
  - Override `receive` in FSM - it's a `PartialFunction[Any, Unit]` that matches on Akka actor messages
  - Wraps incoming msg into `Event(msg, stateData)`
  - Tries `stateFunctions(currentState.stateName)` first; if not defined, falls through to `handleEvent` (whenUnhandled)
  - State function returns `State[S, D]` describing next state
  - When the state changes, it triggers all registered transition handlers in sequence
  - All this runs single-threaded inside the actor's dispatcher thread
- Mailbox: standard Akka mailbox (default unbounded JVM ConcurrentLinkedQueue), one message processed at a time
- State data is immutable case classes you swap via `.using(newData)`
- No native postpone; you'd stash() with akka.actor.Stash trait

Now looking at XState v5, which takes a different approach—the core is an `ActorLogic` interface that handles transitions through a `transition` method, along with snapshot management for persistence and initialization.

The actor created from a machine exposes methods to send events, subscribe to changes, and manage lifecycle, while internally running a microtask loop that processes events sequentially, computes new snapshots including any spawned or invoked actors, and executes the exit actions from the source state.

Now looking at how actions can spawn child actors that live in the same event loop and communicate via send, and how persistence works by serializing snapshots including child actor state, with Restate integration adding durable journaling of every transition.

Shifting to LangGraph's Pregel model, which uses a different execution paradigm where nodes are functions that take state and return partial updates, with typed channels as the communication mechanism. , B)` adds edges between nodes; conditional edges use a function to route based on node output
- When a node returns a partial dict, it triggers writes to those channels, and the planner identifies which downstream nodes should run next
- The graph keeps executing supersteps until no nodes are triggered or we hit the recursion limit
- State gets checkpointed at every superstep boundary using a BaseCheckpointSaver (supporting Postgres, SQLite, in-memory, etc.), with each checkpoint identified by thread_id and checkpoint_id
- Subgraphs share the thread_id but get their own checkpoint_ns namespace
- Interrupts work by raising GraphInterrupt, which the loop catches and checkpoints the state; you can then resume by passing a Command with a resume value

For the State design pattern, the Context class holds a reference to the current State (defined as an interface or abstract class), and each concrete State implements that interface as its own class. Events become method calls on Context that delegate to the current State, which can either mutate state via context.setState(NewState) or return a new State directly. There's no event loop or mailbox—it's just synchronous method dispatch. Hooks typically live as entry/exit methods on State subclasses or wrap setState in Context with before/after logic. Memory-wise, you usually have one State instance per state (often singletons since they're stateless behavior containers) plus the Context holding the actual data.

Now I'm thinking through how to structure this response with real code examples and concrete mechanisms for each pattern, connecting back to how cycles can emerge in each approach. The user mentioned OpenClaw's SST architecture earlier, so I should probably tie that in briefly at the end, but the main focus should be engineering depth on the actual implementations.Engineering depth on each, focused on what's actually in memory, what runs on each tick, and how hooks attach to the runtime.

## Erlang `gen_statem`

The actor is a BEAM process — its own heap, its own mailbox (a FIFO linked list owned by the scheduler), no shared memory with anything else. State is literally `{StateName :: atom(), Data :: term()}` stored in the process dictionary slot the behavior owns. Your callback module exports one of two shapes:

- `state_functions` mode: you export one function per state, each with arity 3: `idle(EventType, EventContent, Data) -> Result`. Dispatch is just `apply(Module, StateName, [EventType, Event, Data])` — the BEAM does the lookup, no framework branching.
- `handle_event_function` mode: single `handle_event(EventType, Event, StateName, Data)` that you pattern-match inside.

Every callback returns a tagged tuple like `{next_state, NewState, NewData, Actions}`. `Actions` is a list of declarative side effects the runtime executes for you: `{reply, From, Msg}`, `{state_timeout, 5000, tick}`, `{next_event, internal, retry}`, `postpone`. The genius of the design is that side effects are *data*, not procedure calls — your callback stays pure-ish and the framework owns the imperative bits.

The receive loop lives in `gen_statem.erl`. On each cycle: pull next message from mailbox → wrap it as an event → call your callback → execute returned actions in order → if state changed and you opted into `state_enter` callback mode, invoke the same callback with `EventType=enter` so you can run on-entry logic. If your action list contains `postpone`, the runtime moves *that specific event* to a side queue; on the next state transition, postponed events get re-prepended to the mailbox front so they're retried in the new state. This is the killer engineering feature — out-of-order tool results in an agent context just wait until the agent reaches a state that handles them, no manual stash management.

Crash semantics: process dies → supervisor catches the EXIT signal → restarts via `init/1` with original args. State is lost unless you explicitly snapshot to ETS/Mnesia/disk. The supervision tree is the persistence boundary you design around.

## Akka FSM (JVM)

`FSM[S, D]` is a trait extending `Actor`, so under the hood you've got a JVM object with mutable fields:

```scala
private var currentState: State[S, D]
private var nextState: State[S, D]
private var generation: Long
private var timeoutFuture: Option[Cancellable]
private val stateFunctions = mutable.Map[S, StateFunction]()
private var handleEvent: StateFunction = NullFunction      // whenUnhandled — single
private var transitionEvent: List[TransitionHandler] = Nil // onTransition — STACKED
private var terminateEvent: PartialFunction[StopEvent, Unit] = NullFunction
```

`when(Idle)(pf)` calls `register(Idle, pf, timeout)` which inserts into `stateFunctions`. `onTransition(pf)` *prepends* to `transitionEvent` — that's the list semantic. `whenUnhandled` and `onTermination` are single-slot, each call replaces.

Dispatch: FSM overrides Actor's `receive` partial function. Per message:
1. Wrap message as `Event(msg, currentStateData)`
2. Look up `stateFunctions(currentState.stateName)` and try `pf.applyOrElse(event, fallback)`
3. If state function not defined for this event, fall through to `handleEvent`
4. Returned `State[S, D]` describes target — if `nextState.stateName != currentState.stateName`, call `handleTransition(prev, next)` which folds over the `transitionEvent` list, calling every partial function whose `isDefinedAt((prev, next))` returns true
5. Apply timer cancellations, set up new state timeout, swap `currentState`

This all runs on a single dispatcher thread per actor — Akka's mailbox (default `ConcurrentLinkedQueue`) is processed by exactly one thread at a time, so all that mutation is safe. The actor's mailbox sits in a JVM heap object, the dispatcher pulls one message, runs `receive`, returns the thread to the pool. No native postpone — you bolt on the `Stash` trait which gives you `stash()` / `unstashAll()` calls explicitly. Less elegant than Erlang's declarative postpone.

State data is conventionally immutable case classes; `.using(newData)` returns a new `State` object with `stateData = newData`. Heap pressure is real for high-throughput FSMs.

## XState v5

The interesting move in v5 was unifying everything under `ActorLogic`:

```typescript
interface ActorLogic<TSnapshot, TEvent, TInput> {
  transition(snapshot: TSnapshot, event: TEvent, scope: ActorScope): TSnapshot
  getInitialSnapshot(scope, input): TSnapshot
  getPersistedSnapshot(snapshot): unknown
  restoreSnapshot(persisted): TSnapshot
  start(snapshot, scope): void
}
```

A state machine is just one implementation. Promises, observables, callbacks, and other machines are others. So a "machine" and "an HTTP-fetching promise actor" speak the same protocol — both can be `invoke`d or `spawn`ed by a parent machine.

`transition()` is pure. Given `(snapshot, event)`, it computes a new snapshot — containing the new state value, updated context, queued actions, and references to any spawned children. The interpreter (`createActor(machine)`) wraps this with the imperative bits:

```typescript
class Actor {
  private _snapshot: Snapshot
  private _eventQueue: Event[]   // microtask-scheduled
  private _observers: Set<Observer>
  
  send(event) {
    this._eventQueue.push(event)
    this._processQueue()  // typically scheduled as microtask
  }
  
  _processQueue() {
    while (this._eventQueue.length) {
      const event = this._eventQueue.shift()
      const next = this.logic.transition(this._snapshot, event, scope)
      this._snapshot = next
      this._executeActions(next.actions)  // entry/exit/transition actions, spawn calls
      this._observers.forEach(o => o.next(next))
    }
  }
}
```

The snapshot is fully serializable — `getPersistedSnapshot()` walks the tree, recursively persisting child actor snapshots. Hierarchical statecharts (SCXML semantics) are encoded in `snapshot.value` as nested objects: `{ active: { editing: 'typing' } }` for parallel/compound states. The transition function does a tree walk to find which transitions are eligible at each level of nesting, computes the LCA between source and target, then runs exit actions bottom-up from the source and entry actions top-down to the target — this is straight from the SCXML algorithm.

Single-threaded JS so no locks. Restate's integration replaces the in-memory event queue with a durable journal — every `send` writes to log before being processed, and `transition()` results are persisted before being committed, so you get crash-safe replay for free without changing the machine.

## LangGraph (Pregel/BSP)

This one is *not* classical actor model — it's Pregel's bulk-synchronous-parallel model, which is a different beast. Worth understanding why: agent workflows often need parallel fanout with deterministic merge, and BSP gives you that natively where actors don't.

Nodes are pure-ish functions: `(state) -> dict_of_partial_updates`. They don't mutate state directly. Channels are typed slots that hold values between supersteps:

- `LastValue` channel: write replaces. Two writes in one superstep without a reducer = `InvalidUpdateError`.
- `BinaryOperator` channel: write is folded via `reducer(old, new)`. `operator.add` on a list channel = message accumulation, the standard pattern for chat history.
- `Topic` channel: multi-producer fanout, all writes preserved.

The execution loop is a `PregelLoop` (in `_loop.py`) that runs supersteps:

1. **Plan**: scan channel versions, find nodes whose subscribed channels updated last superstep — these are "triggered." Build `PregelExecutableTask` list.
2. **Execute**: run all triggered nodes in parallel (asyncio gather or threadpool). Each task accumulates its writes in `task.writes` — a list of `(channel_name, value)` tuples.
3. **Update**: `apply_writes()` iterates writes, groups by channel, calls `channel.update(values)`. For reducer channels this folds; for `LastValue` with multiple writes from one superstep it errors.
4. **Checkpoint**: if a checkpointer is configured, snapshot the channel state.
5. Loop until no node is triggered (quiescence) or recursion limit hit.

Cycles emerge from edges: `add_edge(A, B)` says A writes trigger B; `add_conditional_edges(A, router_fn, {...})` lets the router function pick which downstream to fire. A self-loop or back-edge creates the agent cycle. The recursion limit is your termination guard.

`BaseCheckpointSaver` interface: `put(config, checkpoint, metadata)`, `get_tuple(config)`, `put_writes(config, writes, task_id)` for in-flight writes. Implementations: `MemorySaver`, `SqliteSaver`, `PostgresSaver`, `RedisSaver`. Threads are identified by `thread_id`; subgraphs share the parent thread_id but get a `checkpoint_ns` namespace separator (`|` between levels). Interrupts work by raising `GraphInterrupt` from inside a node — the loop catches, persists the in-flight checkpoint with pending writes, and exits. Resume re-loads, re-injects the resume value via `Command(resume=value)`, and continues from the same superstep.

The trade-off vs. actors: BSP serializes everything into discrete supersteps, which makes parallelism deterministic and checkpointing trivial, but adds latency (you wait for all parallel nodes to finish before next superstep) and reduces flexibility (no async fire-and-forget; everything funnels through channels).

## State design pattern (OO baseline)

Worth covering because it's what you'd hand-roll without a framework, and what every framework above is essentially elaborating.

```python
class State(ABC):
    @abstractmethod
    def handle(self, ctx, event): ...
    def on_enter(self, ctx): pass
    def on_exit(self, ctx): pass

class Context:
    def __init__(self, initial: State):
        self._state = initial
        self._state.on_enter(self)
    
    def transition_to(self, new_state: State):
        self._state.on_exit(self)
        # hook insertion point: before/after observers fire here
        self._state = new_state
        self._state.on_enter(self)
    
    def send(self, event):
        self._state.handle(self, event)
```

That's it. No mailbox, no concurrency, no scheduler — synchronous method dispatch. Hooks are inserted by overriding `transition_to` or by Context maintaining a list of observers fired before/after. State objects are typically singletons (stateless behavior containers); the actual data lives on Context. To get an actor on top of this, you wrap Context in a thread or coroutine that pulls from a queue and calls `send()` in a loop. To get persistence, you serialize Context's data plus the current state's class name.

---

## The engineering axes that distinguish them

Putting them side by side: the things that actually differ at the implementation level are (1) **where the dispatch table lives** — symbol table lookup (Erlang), JVM map (Akka), config object walked at runtime (XState), graph adjacency with channel subscriptions (LangGraph); (2) **how side effects are expressed** — declarative action lists (Erlang/XState) vs. imperative callbacks (Akka) vs. pure return values folded by reducers (LangGraph); (3) **the unit of atomicity** — message (Erlang/Akka), microtask (XState), superstep (LangGraph); (4) **persistence integration point** — supervisor + ETS (Erlang), event sourcing on top (Akka Persistence), snapshot-after-transition (XState/Restate), built-in checkpointer at superstep boundary (LangGraph).

For OpenClaw specifically: the gen_statem model maps cleanest to your Sprite if you want sequential, message-driven agents with postpone semantics for out-of-order Tokens. The LangGraph BSP model maps cleanest if you want parallel agent fanout where Tokens from multiple subagents need deterministic merge into a Space. They're not exclusive — you can have gen_statem-style Sprites whose Spaces are merged via Pregel-style supersteps at coordination boundaries. Want me to sketch what that hybrid looks like concretely?
