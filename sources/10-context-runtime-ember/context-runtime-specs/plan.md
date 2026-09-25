# Context Runtime
## An implementation plan for a branchable, persistent agent runtime

### Status

Architecture specification, **v0.9 — retained operational baseline**.

For History, continuation, authority and mediated-runtime boundaries, the implemented and accepted
Phase 9 architecture is now the current source: `history-kernel-mediated-runtime.md`, its execution
record, ADR-019/ADR-029, and the machine freeze register. This v0.9 plan remains authoritative for
product/Encounter material not superseded there and remains the historical source for the Twenty Laws.
The replacement is not a blanket public freeze: only evidence-complete register rows are
accepted/frozen. Ren signed off on 2026-08-20; the independent final
architecture/security/migration review verified the committed release and concluded with 0 P0 / 0 P1
on 2026-08-21 (`specs/reviews/2026-08-21-phase-9-final-review.md`). Experimental and unproven
dimensions remain unfrozen.

v0.1 was reviewed by five readers; v0.2 absorbed their convergent findings. v0.3 repositioned the runtime as an embeddable component. v0.4 absorbed a three-agent review (`specs/reviews/v0.3-agents.md`). v0.5 absorbed three further streams — two external reviews, a 12-agent design competition, and a focused substrate analysis — consolidated as ADR-010 and resolved by Ren: full package, all-Postgres substrate, Encounter demoted to the reference host. v0.6 absorbs a deep external review of v0.5 (`specs/reviews/v0.5-gpt3.md`, ADR-011): six contract-level corrections and the portability contracts, applied before anything froze. v0.7 merges the GTC research branch (`specs/reviews/gtc/`, ADR-012/ADR-013): the mind layer becomes this plan's parallel track — modules and named Context Systems over the same engine; no engine contract changed. v0.8 re-pins the reference host's component layer on source-level due diligence (`specs/reviews/frontend-2026-08.md`, ADR-014): copied AI-Elements-class chrome over an owned behavior layer; assistant-ui retired to a recorded flip trigger; no engine contract changed. v0.9 opens the hosted-product track and makes its boundary coherent (ADR-015): Stage 8 is the complete single-user Encounter product; Stage 9 is its multi-user trust boundary; durable events use transactionally attributed direct fan-out. The ontology is stable; the remaining uncertainty is implementation-level and belongs in measurements — with the honest caveat that every version has believed something like this, which is why the conformance suites, not this sentence, are the guarantee.

The system is designed around one proposition:

> An agent is not its prompt, its chat history, or its memory store.
> At any moment, an agent continues from a complete state of being.
> That state should be addressable, immutable, inspectable, branchable, replayable, and mergeable.

With one qualification and one consequence:

> The state is complete over what the runtime controls.
> The world is referenced, never contained.

> Because the world lives outside the state,
> touching the world is a protocol, not a write.

And one distinction v0.5 makes explicit:

> State describes being.
> The Continuation Frame describes the conditions under which this being is about to continue.

PostgreSQL provides the persistent state-space. The Context Runtime gives that state meaning. The kernel is the only source of authority. Hosts provide encounter. Models are computations over projections of continuation frames. No individual AI framework owns the system, and this system does not demand to own any framework.

### What changed since v0.8 (the v0.9 encounter opening — ADR-015)

1. **The thread moves into Stage 8.** Stage 8 now ships the complete single-user reference host:
   sessions, the versioned wire, transactional events, resumable SSE, the owned thread behavior layer,
   attachments, the DAG, compare, and the node inspector. Stage 9 becomes one clean concern: authn,
   server-derived principals, authorization, tenancy, and RLS over the already-working product.
2. **Durable-event attribution is explicit.** Publication events fan out, in the publication
   transaction, to every active `follow(universe, ref)` session at the ref-CAS linearization point;
   turn events go to the originating session; session events stay local. Per-session sequence
   allocation and event insertion are atomic. Binding changes and publications share the lock order
   `(canon refs, then sessions)` and carry binding versions, so their race has one observable answer.
3. **The chrome spike becomes the first product slice.** A thin real event log and resumable SSE fold
   land first; the controlled branch pager and Streamdown then run over one real thread with one fork.
   Successful spike code is the beginning of the product, not a disposable preview of a later stage.

### What changed since v0.7 (the v0.8 revision — ADR-014)

1. **The reference host's component layer is re-pinned** (§25, §27, originally staged for Stage 9): chrome is copied-in AI
   Elements components over the shadcn substrate (thread · Workflow/React-Flow · Code/Artifact
   groups); the thread behavior layer — branch state machine over fork topology, edit-as-fork,
   status/tool/approval wiring, CAS attachment upload — belongs to the Session Runtime. assistant-ui
   is retired to a recorded flip trigger (v1 · Stable-tier Runtime API · `ExternalThread` documented
   · branch-adapter semantics frozen): its legacy external-store path measured structurally hostile
   to universe-fork rebinding, and `AssistantTransport` is not this system's shape — that spike is
   replaced by the §27 chrome-mapping spike.
2. **Ecosystem adoption is layered; sovereignty layers unchanged**: substrate and behaviors
   (Next.js · Tailwind · shadcn/ui · Streamdown · use-stick-to-bottom) are taken; the §26 wire, the
   Session Runtime, and kernel egress are kept. `packages/ai` already speaks AI SDK core at the
   provider seam — the stack aligns without adopting `useChat`/UIMessage as a wire.
3. Evidence archived in `specs/reviews/frontend-2026-08.md` (with a Stage-8-open re-verify list);
   deltas in decisions.md. Nothing opens Stage 8 — the gate is untouched.

### What changed since v0.6 (the v0.7 confluence — ADR-012/ADR-013)

1. **One project, two layers.** The GTC research branch (v0.1 → two deep-research reports → v0.2, archived in `specs/reviews/gtc/`) converged, without sight of Stages 5–7, on this engine; it is absorbed, not adopted: **GTC names this repo's mind layer** — the module catalog and, eventually, named reference compositions — never a separate system and never a loadable monolith (ADR-012/013).
2. **Σ — the Context System** (§20): compilation policy becomes one named, versioned object with three binding sites — build default (`COMPILER_POLICY_V1` is Σ v0), agent (`agents/<id>/psyche/**`), situation (per-turn selection, reason recorded). All three reach the frame through `compilerDigest`; memoization, witness, and replay are untouched by construction. Mechanics land at the second real Σ (rule of two).
3. **Candidates record features, not only the collapsed priority** (§20): the compilation record gains the candidate's named feature components (recency, retrieval score, pin, chronology), making recorded evidence an offline experiment set — re-rank and ablate on tape, zero providers.
4. **The mind-layer track** (§32): parallel to Stages 8–11, module-by-module under ADR-012's rules, with its own acceptance discipline — the switching benchmark, the ablation ladder, leave-one-module-out, and two headline metrics: ContextUtility and WritePrecision.
5. **Two dissolutions**: proposition identity is the statement value's canonical hash — content addressing provides what a proposition table would (§21); ContextDiff is a derived inspector tool over two compilation records (§20, Stage 8's node inspector), never a stored object.
6. **Reference domains named** (§9's workspace rule generalized): domains whose truth lives outside the runtime enter as references + provenance + rebuildable derived views; coding/project-context modules are this class.
7. **Owned opens** (decisions.md): claim `stance` · causal-predicate admission policy · WritePrecision instrumentation — each waits for its first consumer.

### What changed since v0.5 (the v0.6 correction — ADR-011)

1. **Admission identities split** (§14, §19–20). The v0.5 "frame digest unchanged" fast path was vacuous — the frame contains StateId, so any ref advance changed it. Three identities now do three jobs: the frame digest (provenance), the **compilation dependency witness** (what admission validates — external dependencies on *every* admission, state dependencies against an advanced head), and the compiled-context digest (exact bytes).
2. **Authorization moved after reduce** (§13). Deleting declared footprints had left authorization running before the write set existed: now pre-authorize kind → reduce through scoped reads → **authorize the exact patch + effect plan** → verify → re-assert at commit.
3. **Redaction redesigned** (§12, §18, §22). Bytes are never mutated under a hash — an authenticated **availability ledger** is consulted at read; redaction bumps an availability epoch in the witness (no cache serves erased data); derived evidence sweeps; subject-tagged payloads are blob-indirect from admission; erasure namespaces are decoupled from universes; a restore drill guards against redaction resurrection.
4. **Effect guarantees are executor-class-specific** (§3, §15, §33), and `Proposal` gained its missing `id`.
5. **The reservation invariant is atomic and schema-enforced** (§5, §12), and **approvals precede intents** — a pending approval never occupies a live ref (§15).
6. **The hash/value ABI is pinned** (§8, §10, §13): algorithm-tagged, length-framed preimages; typed-tag (`$`-key) reservation; contested values materializable through the patch language; language-neutral fixtures.
7. **Portability contracts** (§3, §11, §14, §15, §26, §31): universe-scoped Store handles; the turn as an agent-shaped profile of the general **durable publication batch**; `EffectDriver`/`ExecutionDriver` ports; `HostCheckpointCodec` with semantic decomposition as an optional lens; the engine protocol decoupled from session envelopes; static `DomainModule` composition; packages private by default.
8. **Public paths lose their shard segment** (§8–9) — the codec balances collections with an internal fixed-fanout hash trie; scopes and merge patterns see clean paths.
9. **Contract hygiene**: per-ref leases (§12); destructive-GC inputs durable, never in `proj` (§23); retrieval basis as `(ref, position)` (§19); replay compares records, frames, bytes, decisions, and traces — not just StateIds (§29); version axes split (§30); universes decoupled from tenancy (§6).
10. **Stage patches** (§32): model egress attested from the first invocation via the Stage 2 grant table; promotion built at Stage 6 beside the merge machinery it reuses; the portability gate (LangGraph + a contrasting micro-host) is its own acceptance group; Stage 11 gained acceptance criteria.

### What changed since v0.4

1. **All-Postgres substrate.** The canonical store is a content-addressed Merkle DAG in PostgreSQL — the plan's own recorded fallback, promoted (§12, ADR-010). Git is retired to a delayed export format; SQLite is the fallback-of-record and future embedded dialect. The v1 stack is Node + one Postgres + a filesystem blob CAS. **Every durable step is one transaction in one engine** — the mid-turn step and the publication each span objects, outbox, events, projections, and ref CAS with zero cross-store seams — deleting turn anchoring (ADR-002), the checkpoint/fsync choreography (ADR-006), the projection barrier, the dual-write ordering gap, and the erasure rewrite ceremony (ADR-003).
2. **Six objects, two worlds.** Encounter (Session, Surface, Interaction) is demoted from the frozen core to the reference host's design (§2, §25–27). The core is Being and Becoming.
3. **The Continuation Frame** (§19–20). Cognition operates on `Frame(state, input, realm, authority, tools, retrieval, runtime)` — not on State alone. The compile cache is keyed by the frame digest; stale cognition on revocation is impossible by construction.
4. **Realm belongs to the execution binding, not the node** (§7, §16). Nodes record where they *arose* (provenance); the kernel resolves what a continuation may *touch* from the binding. `Node.realm` is gone.
5. **Live-effect fencing** (§14–15). An unresolved live-effect turn semantically occupies its ref: failover bumps the fence, and recovery must reconcile before the next live turn is admitted. The world may not change on behalf of a turn that can lose its place in history.
6. **Serial-per-ref concurrency** (§14). Declared footprints and the commutation calculus are deleted; frame staleness became the admission check (replaced in v0.6 by the dependency witness). Footprints return as *observed* read-traces with OCC validation — first activated at the §33 demo (end of Stage 6), generalized at Stage 10. Read-tracing lands at Stage 2 so the data exists.
7. **StateId is a runtime-computed Merkle hash** over the logical tree, domain-separated by encoding and schema version (§8). Law 3 loses its asterisk; the Store firewall now protects recorded identity; a store swap is a data move.
8. **Effects are immutable facts** (§15): intent and observation are records; dispatch attempts are operational; "current phase" is a projection. Promotion is a three-way reconciliation routed through a standard turn, with a promotion report (§16).
9. **Evidence availability is explicit** (§18): `full | replayable | audit-only | redacted | expired`, with the conservation law stated — permanent exact replay and guaranteed erasure cannot both hold. Blob references carry erasure namespaces.
10. **Adoption levels are coverage contracts** (§3): each level states what the runtime *actually captures* through the adapter, specified against LangGraph's real checkpointer contract.
11. **CR-CJSON/1** (§10): NFC at admission, then RFC 8785, then LF framing; Unicode version pinned; numeric domains explicit (typed decimal/bigint/money).
12. **The build is resequenced** (§31–32): Stage 0 is an executable spec (`packages/domain`: zod schemas, golden vectors, property tests); replay is the spine from Stage 1; memory and merge come before any web; sessions and the multi-user hosted product (Assistant UI) are the reference host stages, built when a second user exists.

---

# 1. North star

The architecture should remain understandable even if, five years from now: the dominant model providers are different; the surface chrome is replaced; MCP is superseded; the popular agent frameworks are different ones; models gain ten-million-token contexts; agents run continuously for months; a single agent becomes thousands of collaborating agents; context compilation becomes learned rather than hand-designed; memory becomes substantially more sophisticated; agents begin modifying parts of their own runtime.

The durable abstractions therefore cannot be:

```text
chat messages · LLM provider APIs · framework sessions
vector databases · prompt templates · UI threads
```

They should instead be:

```text
state · transition · effect · realm · identity · provenance
evidence · branch · merge · capability · frame · projection
```

Everything else is an implementation.

---

# 2. Six objects, two worlds

The core architecture is six objects in two worlds.

```text
BEING                 BECOMING
what is               how it changes

Universe              Transition
Node                  Invocation
State                 Effect
```

## Being

**Universe** — the materialized graph of explored continuations of one persistent system.

**Node** — one point on a trajectory: a State bound to the Record of how it arose.

**State** — one complete semantic continuation state. Content-addressed. Two nodes may share one State.

## Becoming

**Transition** — one causal step: a proposal that was validated, reduced, authorized, and committed.

**Invocation** — one model computation over a projection of a Continuation Frame. Invocations never create nodes; transitions do.

**Effect** — one contact with the external world: intent, dispatch, observation.

Keeping Being and Becoming separate — what persists versus how it becomes — is the most important architectural decision. It is also the packaging: these six objects ship as the embeddable core.

**Encounter** — Session, Surface, Interaction: how a trajectory is met by humans — is real, designed (§25–27), and deliberately *not* part of the frozen core. Every host owns its own session model (§3); a frozen cross-host Interaction type would be a fiction the first adapter contradicts. Encounter is the reference host's design, frozen when it is built (Stage 8), promotable into the core later with evidence. The three-world story survives as packaging truth: the core, and how hosts encounter it.

### Naming

"Context" was overloaded four ways in v0.1. Code uses the unambiguous names: Universe, Node, State, CompiledContext — and, since v0.5, **ContinuationFrame** for the full circumstance of an invocation (§19). The system keeps its name. The code keeps its clarity.

---

# 3. Hosts and adoption levels

Context Runtime is a component before it is an application.

The core ships as an embeddable TypeScript library: no server it owns, no UI, no opinion about your loop. Encounter is supplied by a **host**. Our reference application (§25–27) is one host — the one that grows into the multi-user product. LangGraph, Mastra, the OpenAI Agents SDK, and ADK are others. Your bespoke loop is another.

```text
the host owns                    the core owns
─────────────                    ─────────────
the loop                         Universe · Node · State
orchestration                    transitions · turns · sequencer
prompt assembly                  store · diff · merge
tool execution                   evidence · memory claims
its own session model            realms · capabilities †

                                 † at the levels that route through it
```

TypeScript, because the hosts live there. Non-TypeScript hosts embed the runtime as a sidecar speaking the wire protocol (§26) — a later format-and-spec play, honestly re-priced: the protocol is written when the reference host needs it (Stage 8), and no near-term sidecar is a deliverable. The store is Postgres (§12): production hosts point the adapter at a connection string — the incumbent norm; LangGraph's own production checkpointer is `PostgresSaver`. A zero-server embedded dialect (SQLite or PGlite behind the same Store contract) is the recorded future answer for the npm-and-try audience, built when an embedded-only host demands it (§34).

**Adoption levels are coverage contracts, not law lists.** The runtime can only guarantee properties of what flows through the adapter; each level states its coverage in an `AdoptionManifest` (what of semantic state, dialog, invocations, tool results, compilation, effects, and authority the adapter actually captures). Only Level 3 can claim complete continuation semantics.

## Level 0 — Checkpointer

*Versioned persistence for runtime-managed snapshots.* The host treats the runtime as a state backend and never learns it is holding a universe.

The LangGraph adapter is specified against the **real** `BaseCheckpointSaver` contract — `getTuple`, `list` (with filters), `put`, `put_writes`/pending writes, `channel_versions`, `versions_seen`, `get_next_version`, `delete_thread` — not a two-line sketch. Thread → ref; checkpoint → node; superstep → turn (settled); fork-from-checkpoint → branch. Scalar channels → one record per channel; accumulating list channels (`messages`) decompose to one record per item — a single growing file is exactly the merge bomb §9 forbids. Pending writes are the operational half of a turn; the adapter journals them in `ops` and folds them into the next committed node. Host writes become `host.snapshot` transitions; patches are computed by diff.

The base contract is a **HostCheckpointCodec**: opaque, byte-exact round-tripping of the host's checkpoint — what Level 0 *guarantees* for any host. Semantic decomposition (channels → records, which is what makes diff, edit, and merge meaningful) is an optional adapter lens layered on top; where the lens does not apply, the checkpoint still round-trips and history, forking, and provenance still hold.

The user gains immediately: durable history, time travel, fork-from-anywhere, structural diff (where the lens applies), provenance, rebuildable indexes. What is *not* guaranteed: completeness (the host may hold state the adapter never sees) or evidence for model calls made outside the runtime. The manifest says so.

Acceptance includes the drill third-party checkpointers actually fail: a **partially failed superstep resumes without re-running completed tasks**.

## Level 1 — Transactions

*Transactional semantics for runtime-managed mutations.* The host writes through `propose / commit`: typed transitions, preconditions, the no-op rule, verifiable patches, turns. Concurrent host workers stop overwriting each other.

## Level 2 — Effects and authority

*World and authority guarantees for runtime-routed effects.* The host routes tool execution through the bracket (§15) and attestation through the kernel (§17). For calls routed through the wrapper: simulations cannot email, approvals bind to what was seen, and double-charge is prevented to exactly the strength the executor's class supports (§15's matrix is the honest contract) — never silently exceeded. Routing is the host's adoption choice — the runtime cannot impose it, and the manifest records the boundary.

## Level 3 — Resident

*Complete continuation semantics.* The runtime's own loop, compiler, sessions, and surfaces — the reference host — for when nothing else owns the process.

**The compiler is a battery, not a gate.** At Levels 0–2 the host assembles its own prompts; the core offers `ScopedStateView`, retrieval, and `compile()` as services the host may take or leave.

**The first host is a forcing function.** The Level 0 LangGraph adapter is scheduled early (Stage 3): a real host is the cheapest possible stress test of the core API.

> Frameworks are adapters — in both directions.

---

# 4. Five classes of data

Every piece of data belongs to exactly one class. This is enforced in review.

**Canonical (semantic).** Defines continuation. If it can change what the agent knows, believes, may access, or may do next — it is here. Stored in the universe's canonical schema (`canon`, §12). Examples: goals, tasks, memory claims, agent state, workspace, policies, capability references, dialog.

**Evidential.** Recorded because it cannot be regenerated, kept as proof, never silently fed back into cognition. Payloads in the content-addressed blob store; records and hashes in `canon`. Examples: compiled contexts, model requests and responses, effect receipts, approvals, validation records, compaction records. Availability is retention-scoped (§18).

**Operational.** Required to execute reliably; not part of what the agent is. Stored in the `ops` schema. Examples: jobs, leases, dispatch attempts, session connections, retry counters.

**Derived.** Rebuildable from Canonical plus Evidential, always. Stored in the `proj` schema, plus caches. Examples: node index, ancestry, claim status, thread projections, FTS, vector indexes, DAG layouts.

**Ephemeral.** May disappear without changing reality. Browser memory. Examples: open tab, zoom level, cursor, partial token buffers.

The classes survive the substrate change intact; what changes is that all four server-side classes now live in one engine, separated by **schema discipline** — `canon` is truth, `proj` is disposable, `ops` is neither — enforced by a standing drop-`proj`-and-rebuild drill (§28).

---

# 5. The authority matrix

For every record, exactly one home answers "what is true."

```text
Record                                          Authority
──────────────────────────────────────────────────────────────────
State (the logical state tree)                  canon.objects
Node ancestry, ref heads, fences                canon.nodes / canon.refs
Transitions, patches, effect facts              canon (records; patch values by hash)
Invocation payloads, receipts, approvals        Blob store (hash in canon)
Declared capability references                  State
Effective grants, credentials, budgets          Kernel / secret store — never the tree
Authorization decisions taken                   Evidence (canon record + blob)
Sessions, connections, jobs, leases, attempts   ops
Session event log (sequences)                   ops — authoritative, appended transactionally (§26)
Indexes, projections, retrieval                 proj — rebuildable
UI state                                        Browser
```

The commit protocol distinguishes two events v0.4 conflated:

> **Durability is not publication.** A recorded fact is durable when its transaction commits.
> A continuation is published when the ref moves. Effects require durability *before dispatch*;
> observers see publication.

```text
mid-turn durable step:   BEGIN → assert head = turn.base ∧ fence = lease.token ∧ no rival open turn
                         → chain objects → turn journal tip → effect-outbox intent
                         → durable-event append (EffectIntended) → COMMIT
                         (dispatch follows only after a fresh fence-and-lease check — §14;
                          approval requests park their turn and occupy nothing — §15)

turn publication:        BEGIN → remaining objects → node record → transactional projections
                         → committed-event append → ref CAS (fence-equality) → close turn journal → COMMIT
```

Nothing before the publication transaction is *visible* on the ref. Everything in `proj` is a projection — the transactional tier (node index, claim status) joins the commit transaction, and the `ops` event log appends there too (§26); the genuinely expensive tier (embeddings, heavy FTS) is asynchronous behind a **basis watermark** (§28), and retrieval waits on basis or fails with a typed class. There is no cross-store seam anywhere in the semantic commit.

Blob uploads still precede their references (step 0, outside the transaction); the blob GC grace window exists for exactly this (§22).

---

# 6. Universe

A **Universe** is the materialized graph of historical and explored counterfactual continuations of one persistent system — the continuations actually materialized, not the implicit space of possible ones.

It is implemented as rows under one `universe_id` in the canonical schema (§12). One universe → one export unit and one GC scope; erasure namespaces (§18) and leases (§12) default 1:1 with universes but are their own identities — and a universe is not a tenant: ownership, export policy, and lease scope can split from it later without remodeling.

```text
                            ┌── C ── D
                            │
A ───── B ───── E ───── F ──┼────────────── M ── N
              ╲             │               ╱
               G ── H ──────┘───────────────
```

A universe could correspond to: a persistent personal agent, a project, an organization, a simulation, a long-running research process, a multi-agent society.

## Cross-universe references

There are **no atomic cross-universe transitions**. Ever.

Cross-universe relationships are explicit references (`universeId` + `NodeId`) and message passing. Delivery is an Effect (§15) on the sending side and a Transition on the receiving side. The guarantee is stated precisely: **at-least-once delivery, deduplicated by the receiver on the idempotency key** — effectively-once *application behavior* under the declared protocol, not a delivery-layer promise. A cross-universe NodeId reference is a claim about another universe; fetch and mirror behavior is policy.

This section stays short so it never becomes a distributed-transactions project.

---

# 7. Node and State

A trajectory position is not a state. Two different histories can arrive at byte-identical states:

```text
         transition X
       ┌──────────────► Node B    state = S₂
Node A
       └──────────────► Node C    state = S₂
         transition Y
```

B and C are different Nodes. They share one State.

```ts
interface Node {
  id: NodeId;                      // durable identity, minted at commit
  parents: readonly NodeId[];

  state: StateId;                  // what is (§8 — runtime-computed)
  record: RecordRef;               // how it came to be

  schema: SchemaVersion;
  encoding: EncodingVersion;       // §8, §30 — separate axes
  runtime: BundleDigest;
  kernel: KernelVersion;
}
```

**A node has no `realm` field.** Where a node *arose* is provenance — `executedIn` in its transition record. What a continuation *from* a node may touch is resolved by the kernel from the execution binding (§16). A single historical node can be reachable from the live ref, forked under a simulation, and pinned by a replay session simultaneously, without semantic weirdness.

The record side of a node carries: the transition (including the patch, with values referenced by hash — stored once, §12), invocation references, effect facts, approvals.

What the Node/State split buys:

- **No-op detection.** A transition that changes neither state nor record commits nothing; retries dedupe on proposal id. A transition with an unchanged state but evidence that must survive — an effect intent, a paid invocation — commits a **record-only node**: same StateId (memoization and convergence untouched), new record, durable in its own transaction, and **published like any other node** — the ref advances; only the state hash stands still.
- **Compile memoization.** The compiler cache is keyed by the frame digest (§20), whose largest component is StateId — identical states compile once, across branches.
- **Honest merges.** "Did this merge change anything?" is a hash comparison.
- **Structural convergence.** Two branches that arrive at the same State are detectably convergent.

The Node is immutable. Corrections, reversions, schema upgrades, memory corrections — all create children.

---

# 8. Identity

Three identifiers, three jobs:

```ts
type NodeId   = Brand<Ulid, "NodeId">;    // durable domain identity
type StateId  = Brand<Hash, "StateId">;   // runtime-computed content identity of the logical state tree
type StoreOid = Brand<string, "StoreOid">; // storage locator — never semantic, never leaves the store
```

**NodeId** is a ULID minted at commit time, written into the transition record. It is what sessions pin, branches reference, and other universes cite. It survives storage replacement because it never encodes storage.

**StateId is computed by the runtime, not borrowed from the store:**

```text
leaf     = H( "cr-state-leaf\0" ‖ LP(CR-CJSON bytes) )
interior = H( "cr-state-tree\0" ‖ sorted (LP(segment), LP(kind), LP(childHash)) entries )
StateId  = H( "cr-state\0" ‖ LP(encodingVersion) ‖ LP(schemaVersion) ‖ LP(rootHash) )
record   = H( "cr-record\0" ‖ LP(CR-CJSON bytes) )
```

computed incrementally during verify (§13) — O(changed paths × depth), the leaf bytes already in hand. Domain separation means identical bytes under different schema semantics never collide in a cache. The hash is over the **logical** tree; physical layout is a store concern excluded from identity. A store swap or layout change is a data move, not an identity migration — this is what makes the Store interface (§11) a real firewall.

The preimage discipline is part of the ABI, frozen at Stage 0: digests are algorithm-tagged (`sha256:`); every preimage field is length-prefixed — no ambiguous concatenation; path segments are NFC UTF-8 bytes, sorted bytewise, with declared limits; and the whole is fixed by language-neutral golden fixtures plus exported JSON Schema, so a second implementation can reproduce every hash from the spec alone.

Two more normative codec rules keep the hash total, because two conforming implementations must never disagree: **an interior node with zero entries is pruned from its parent** — deletes cascade upward, and a tree never contains empty children; and **the balancing trie's fan-out is fixed by the encoding version** (§9) — there is no dynamic re-balancing; changing it is an encoding migration. **Contested values (§24) have a canonical encoding from day one** — they are hashed state, and adding their encoding later would be an encoding migration. The Stage 0 golden vectors cover delete-to-empty, trie boundaries, contested values, and Unicode admission edges.

Precision about what this identity is: **equal canonical structural content under the same encoding profile yields equal StateId.** That is structural identity, and it is plenty. Two semantically equivalent states with different claim ULIDs or timestamps hash differently; call convergence *structural*, never semantic. Semantic equivalence can someday be a separate relation.

Every transition record embeds the parent and child StateIds and the NodeId, so history is hash-chained at the runtime level, independent of the store. Cross-implementation migration is an import with a recorded provenance link, never a silent remap.

---

# 9. The layout law

The unit of canonical data is the record, and the law from v0.1 survives every substrate:

> **One record, one object. Collections are logical prefixes. Manifests are derived, never canonical.**

```text
tasks/<ulid>                    not  a tasks.json
memory/claims/<ulid>            not  a memory manifest
dialog/<ulid>                   not  a conversation log file
```

Paths are **logical and clean** — consumers (capability scopes, merge-strategy dispatch, read traces) see `memory/claims/<ulid>`, never physical storage and never shard segments. Below the path layer, the codec balances high-cardinality collections with a **fixed-fanout hash trie** built from the ULID's entropy — bounding the incremental re-hash cost of an append (a flat 50k-child node would re-hash 50k entries every time) and spreading concurrent appends uniformly. The trie is identity-bearing (its fan-out is part of the encoding version — re-balancing is an encoding migration) but **encoding-internal**: it never appears in a path, a scope, or a merge pattern. Honestly bounded: trie buckets grow with total cardinality — "small" means N/fanout — and the Stage 1 probe measures interior-node cost at target cardinalities.

Why record-per-object matters as much as ever: one changed record is one changed leaf (semantic diffs); concurrent appends to one collection touch disjoint leaves (union merges stay automatic, §24); and a record is the unit of redaction (§22).

Two boundary rules complete the law:

**Size tiers.** A value ≤ 64 KiB lives inline as a canonical object. Anything larger lives in the blob store, referenced as:

```json
{ "kind": "blob", "ns": "u_01J9…", "hash": "sha256:…", "size": 841829138, "mediaType": "video/mp4" }
```

`ns` is the erasure namespace (§18, §22). A record tagged with an erasure `subject` **is** blob-stored regardless of size — mandatory routing (§22), the size tier's privacy dimension.

**The ingest gate.** Tool output never enters State raw. What enters State is an actionable summary plus a blob reference; the full payload is Evidence. This one rule is what prevents the canonical store from dying of bloat — a research agent produces gigabytes per month, and none of it belongs in State.

**Environment.** `env/config.json` holds stable configuration. Volatile observations ("weather = sunny") are memory claims or evidence, not shared mutable state.

**Workspace.** For an external product codebase, `workspace/` holds a *reference* — remote URI plus commit hash — together with the agent's working set. The product repository keeps its own lifecycle.

---

# 10. Canonical bytes — CR-CJSON/1

Because the store is content-addressed, representation is part of the contract:

> **Same canonical content, same identity.**

The profile is named — **CR-CJSON/1** — because it is *built on* RFC 8785, not identical to it (JCS neither normalizes Unicode nor frames output):

```text
CR-CJSON/1:
  1. admission:      strings NFC-normalized (Unicode version pinned in encodingVersion);
                     after admission, CanonicalValue strings are preserved byte-semantically —
                     serialization never re-normalizes
  2. serialization:  RFC 8785 (JCS): sorted keys, canonical number form, minimal escaping
  3. framing:        UTF-8, LF, single trailing newline
```

**Numeric domains are explicit**, because JCS numbers are IEEE-754 doubles and an agent runtime will meet money:

```text
JSON number     finite IEEE-754 binary64; its represented binary64 value is the meaning
decimal         { "$dec": "19.99" }        typed decimal string
bigint          { "$int": "18446744073709551616" }
money           { "$amt": "19.99", "cur": "USD" }
timestamps      RFC 3339, UTC, millisecond precision
```

A serializer that would change the represented binary64 value must reject at admission, never round.
Inputs that require integer or decimal lexical semantics use `$int`/`$dec` before conversion to a host
number; precision already discarded by an upstream parser cannot be recovered at admission. And keys
beginning `$` are **reserved for typed tags**: user JSON containing them is rejected at admission (or
escaped by declared policy), so ordinary data can never impersonate `$dec` or `$amt`.

Time discipline: **topological order is the logical clock.** Wall-clock timestamps are display metadata; no feature may depend on them for causality.

Everything rests on this page: the no-op rule, compile memoization, verifiable transitions, honest merges. The codec ships in Stage 0 with golden vectors and property tests — it *is* part of the executable spec.

---

# 11. The Store

No application code outside the Store knows about SQL, schemas, or connection pools. A `Store` handle is **scoped to one universe** at construction — storage identity is composite (`universe_id`, hash), and no method crosses universes; cross-universe work is message passing (§6), never a shared handle.

```ts
interface Store {
  node(id: NodeId): Promise<Node>;
  view(state: StateId, scope: ReadScope): ScopedStateView;   // principal + capability + realm

  open(parent: NodeId, ref: Ref | null): Promise<Turn>;      // durable turn journal, bound to its target ref;
                                                             //   refuses while the ref is occupied (§14)
  commit(turn: Turn, c: Commit): Promise<void>;              // one durable chain step (may carry outbox intents)
  publish(ref: Ref, turn: Turn, fence: Fence): Promise<Published | Raced | Fenced>;

  diff(a: StateId, b: StateId): Promise<Diff>;
  bases(nodes: readonly NodeId[]): Promise<readonly NodeId[]>;
  merge(r: MergeRequest): Promise<Clean | Conflicts | Rejected>;  // structural only — §24
}

interface ScopedStateView {
  read(path: Path): Promise<StateValue | null>;
  list(prefix: Path): AsyncIterable<Path>;
}

type StateValue =
  | { kind: "resolved"; value: CanonicalValue }
  | { kind: "contested"; conflict: ConflictRef }     // §24 — conflict is in the value domain
  | { kind: "redacted"; hash: Hash }                 // §22 — typed absence
  | { kind: "expired";  hash: Hash };                // §18 — typed absence
```

Load-bearing points:

- **`ScopedStateView` is the only read path** for reducers, the compiler, and ACL checks — path-scoped by the caller's capability and traced (§14). The unscoped raw view exists only inside the store and kernel. Read authority is in the API, not the prose.
- **Contested, redacted, and expired are values**, not exceptions — the type system forces every consumer to consciously handle uncertainty instead of accidentally treating one side as truth.
- **Durability is an interface obligation**: `commit` returns only after the transaction is durable; `publish` is the CAS with fencing. Any conforming store must honor both — the contract, not the engine, carries the guarantee.
- `Commit`, `MergeRequest`, `Diff`, and friends are finalized as zod schemas in `packages/domain` at Stage 0 — each carrying the encoding version, so auxiliary shapes migrate the same way state does.
- A `Commit` carries the complete `NodeRecord`, not a singular parent shortcut: its ordered `parents`
  represents ordinary and merge nodes uniformly; the envelope cross-checks node/transition ids, StateId,
  encoding, record digest, and every by-hash patch payload before the Store writes SQL.

`Store.merge` returns **structural** results only. Domain merge policy lives in the runtime (§24). The store does not know what a memory is.

---

# 12. PostgreSQL as the first implementation

The canonical store is a content-addressed Merkle DAG in PostgreSQL ≥ 16 — the plan's own recorded fallback, promoted by ADR-010 on the evidence that retired Git (four of eight v0.4 ADRs were storage-impedance repairs) and the constraint that decided between databases: **Postgres is in the end-state unconditionally** (sessions, events, projections, FTS, pgvector — and a lease on the write path under every design), so any second engine is an addition, never a replacement. One engine keeps the semantic commit transactional across the whole system at solo scale and at hosted scale.

The v1 stack: **Node + one Postgres + the filesystem blob CAS.** No Git binary. No SQLite.

## The canonical schema, sketched

```sql
-- canon: the truth. Append-only by trigger; audited exceptions: gc_sweep, redact.
canon.objects (
  universe_id  ulid    NOT NULL,
  hash         bytea   NOT NULL,           -- runtime hash (§8), the only identity
  kind         text    NOT NULL,           -- value | tree | record
  bytes        bytea   NOT NULL,           -- CR-CJSON (zstd for large values)
  PRIMARY KEY (universe_id, hash)
);
canon.nodes (
  universe_id  ulid  NOT NULL,
  node_id      ulid  NOT NULL,             -- NodeId
  state_hash   bytea NOT NULL,
  record_hash  bytea NOT NULL,
  parents      ulid[] NOT NULL,
  PRIMARY KEY (universe_id, node_id)
);
canon.refs (
  universe_id  ulid   NOT NULL,
  name         text   NOT NULL,            -- live | agents/<id>/… | exp/… | eval/… | sim/… | archive/…
  head         ulid   NOT NULL,            -- NodeId
  fence        bigint NOT NULL,            -- §14 — current lease's fencing token
  PRIMARY KEY (universe_id, name)
);
-- CAS in the publication transaction; $token is the publisher's lease token (§14):
--   UPDATE canon.refs SET head = $new
--    WHERE universe_id = $u AND name = $ref AND head = $expected AND fence = $token;
canon.turns (universe_id, turn_id ulid, ref text, base ulid, tip_hash bytea, opened_at, closed_at);
                                             -- ref: the publication target (NULL for unbound work) —
                                             --   what makes §14's occupation predicate queryable;
                                             --   partial UNIQUE (universe_id, ref) WHERE closed_at IS NULL
canon.effects (universe_id, effect_id ulid, turn_id ulid, fact text, payload_hash bytea, at);
                                             -- fact: intent | observation  (§15; attempts live in ops);
                                             -- UNIQUE (universe_id, effect_id, fact); observation requires
                                             --   a prior intent (enforced); proposal dedup is a unique
                                             --   (universe_id, proposal_id) journal in ops
canon.availability (universe_id, hash bytea, status text, subject text, at, epoch bigint);
                                             -- the redaction/expiry ledger (§22): reads consult it;
                                             -- object bytes are NEVER mutated under their hash;
                                             -- epoch feeds the compilation witness (§20)
```

`proj` (node index, ancestry, claim status, thread projections, FTS, embeddings, rollups) and `ops` (jobs, leases, dispatch attempts, sessions, the session event log — §26) complete the picture (§28). Patch values are stored once as objects and referenced by hash from transition records — an erased value is one audited object touch (§22).

## Implementation notes that are part of the plan

- **`synchronous_commit = on`** for canon transactions; durability is the engine's contract, not a config scavenger hunt.
- **Leases are per ref** (`ops.leases`), defaulting in v1 to one worker holding all of a universe's refs — a deployment choice, not a contract: the fence (§14) is already per-ref, and both serial-per-ref and the thousands-of-agents north star want ref granularity. The lease check and the ref CAS share a transaction, so fencing is atomic rather than choreographed.
- **Append-only where append-only means something**: `canon.objects` and `canon.nodes` are insert-only by trigger, with `gc_sweep` the only privileged, audited deleter; `redact` writes `canon.availability`, never object bytes (§22); `canon.refs` mutates only through the fenced CAS; `canon.turns` only transitions open → closed; `canon.effects` and `canon.availability` are insert-only facts.
- **Reads** are plain indexed lookups; a `ScopedStateView` path read walks root→leaf through `canon.objects`. No subprocess pools, no batch protocols.
- **Backup** is one story: nightly `pg_dump` plus WAL archiving when it matters, alongside the blob-store manifest. Per-universe export = `COPY` of the universe's rows + its blob manifest — a pair, not a triple.
- **Git is an export format** — `runtime export --git <dir>` streams a universe into a real Git repository with the same commit topology and NodeId/turn metadata, for inspection, sharing, and a differential integrity oracle. **Delayed by decision**: it ships when someone wants it, not in v1. Until then, integrity rests on the standing verify-by-hash walk (§13) — scheduled, not occasional — and the codec's golden-vector suite.
- **Fallback-of-record: SQLite-per-universe** (same codec, same Store contract) — activated if the Stage 1 probe fails, or as the embedded zero-server dialect when an embedded-only host demands it (the LangGraph sqlite-local/postgres-production pattern). The recorded dissent: if the hosted roadmap dies and embedded adoption becomes the growth path, SQLite was the right primary — the Store contract keeps that door open as a data move.

**The Stage 1 load probe.** Before anything is built on the store, a synthetic generator drives the production shape — full commit transactions, `synchronous_commit = on` — and records: p50/p99 commit-transaction latency; diff and merge latency at 100k nodes; interior-node hashing cost at target collection cardinalities; CAS contention across universes; GC sweep under open turns and the blob grace window; per-universe export size; drop-`proj` rebuild time at 10⁶ objects. Two crash drills are part of the probe, not deferred: `kill -9` mid-transaction (WAL recovery; nothing acknowledged is lost) and `kill -9` between intent durability and receipt (§15 reconciliation finds the outbox row). The probe also measures bracket overhead for observation-class (read-only) effects — the recorded spike question, settled here by measurement rather than by Temporal's authority. Targets are set, measured, and written into `specs/acceptance/stage-1.md`. If the numbers fail, the fallback replaces the implementation behind the unchanged Store interface — before anything is built on top.

The scale envelope, stated honestly: one universe sustains tens of commits per second through one writer. Ample for a person and a working set of agents; many universes, message passing (§6), and per-ref serialization are how the design scales out — which is already the design.

---

# 13. Transitions

Models do not mutate state. Humans do not mutate state. Tools do not mutate state.

They propose.

```ts
interface Proposal<K extends Kind = Kind> {
  id: ProposalId;                         // ULID — retries dedupe on it; effect idempotency keys derive from it
  kind: K;                                // "memory.assert" | "task.update" | …
  author: Principal;
  input: InputOf<K>;
  requires: readonly Precondition[];      // e.g. { path, cond: "exists" | "absent" | "hashEquals" }
}

type Reduce<K> = (view: ScopedStateView, p: Proposal<K>) => Promise<Patch>;

type Patch = readonly PatchOp[];
type PatchOp =
  | { op: "put";     path: Path; value: CanonicalValue }
  | { op: "delete";  path: Path }
  | { op: "link";    path: Path; blob: BlobRef }
  | { op: "contest"; path: Path; conflict: ConflictValue };  // merge/promotion transitions only —
                                                             //   how §24's contested values materialize;
                                                             //   patch authorization enforces the restriction
```

Proposals no longer declare read/write footprints — v1 is serial per ref (§14) and declared footprints were unenforceable. What replaces them is better: the `ScopedStateView` handed to a reducer **traces every read** (paths and prefix listings), and the observed trace is recorded in the transition record. From Stage 2 onward the data exists; its first consumer turns it into OCC admission — the §33 demo, then Stage 10 generally (§14).

The pipeline, each step recorded:

```text
propose → validate → pre-authorize → reduce → authorize patch → verify → commit
```

- **validate**: schema and domain invariants.
- **pre-authorize**: may *this author* submit *this kind* under *this binding* at all — against attestation, never against the proposal. Cheap rejection before any work. Self-grant is impossible by construction (§17).
- **reduce**: pure and deterministic over a `ScopedStateView` — reads are capability-scoped and traced. Reducers produce patches; only the Store produces objects.
- **authorize the patch**: the write set now exists, so the kernel checks it — every patch path, every blob namespace, and the effect plan, against the author's attested scope. Declared footprints are gone (§14); authorization judges what the reducer actually did, not what it promised. A reducer that writes outside its authorized prefix is refused here — a Stage 2 acceptance test, beside self-grant.
- **verify**: apply the patch to the parent State ⇒ recompute the child StateId incrementally (§8). Every commit is checkable by a third party from the transition record alone; the verify-by-hash walk runs as a standing scheduled test.
- **commit**: the fence, lease, and authority epoch are re-asserted inside the transaction (§14); then, if the transition changes neither state nor record, nothing commits — the no-op rule. An unchanged state with evidence that must survive commits a record-only node (§7).

The transition record embeds the patch (values by hash), the author, the observed read-trace, `executedIn` (the realm of the binding it ran under — provenance, §16), the frame digest (§19), validation results, and references to invocations and effect facts. A useful state whose origin cannot be explained is corrupted state — and the explanation is machine-checkable.

### The loop, in one page

```ts
async function step(ref: Ref, binding: ExecutionBinding): Promise<Node> {
  const head  = await heads.resolve(ref);
  const turn  = await store.open(head.id, ref);             // §12 — durable turn journal; refuses if occupied (§14)
  const obs   = await turn.accept(inbox.next());            // commits the dialog observation (§25) — before compile
  const frame = await frames.assemble(obs, binding);        // §19 — state + realm + authority + tools + retrieval
  const ctx   = await compiler.compile(frame);              // §20 — evidence; memoized on frame digest
  const prop  = await invoke(model, ctx);                   // §19 — via an attested model capability (§17)
  const admit = await engine.admit(turn, prop, frame);      // validate + pre-authorize + witness check (§14)
  const step  = await engine.settle(reduce(admit), admit);  // authorize the patch + effect plan; verify (§13)
  await store.commit(turn, step);                           // durable; effect intents enter the outbox here
  await kernel.effects(turn, admit.effects);                // §15 — dispatch after durability; observe; record
  return sequencer.publish(ref, turn, binding.fence);       // §14 — one fenced CAS, or branch
}
```

Every line is a section of this document. Nothing else is load-bearing.

---

# 14. Concurrency and turns

Three rules, simpler and stronger than v0.4's:

**One committer per ref — serial, really.** The sequencer applies proposals to a ref in arrival order. There is no commutation calculus and there are no declared footprints: with one human, a handful of agents, and a per-ref queue, linearization machinery served a consumer that does not exist yet. The design errs toward branching, never toward silent rebasing.

**Admission validates the compilation dependency witness.** A model-derived proposal is pinned to the frame it was compiled from, and three identities do three jobs (§19–20): the **frame digest** is provenance — which circumstance the proposal came from; the **compiled-context digest** is the exact bytes the model saw; and the **witness** — the selectors and prefix memberships the compiler consulted, the retrieval revision, the authority epoch, the availability epoch (§22), the realm, the tool set — is what admission checks. On *every* admission the witness's external dependencies are re-validated against the present: a revoked capability or a redaction invalidates an in-flight proposal even when the ref never moved. When the ref *did* advance, the witness's state dependencies are validated against the new head: untouched means the model would have seen the same projection and the proposal linearizes; touched means it lands as a child of its input node, on a branch — disagreement, preserved. (Note what the v0.5 draft got wrong: "frame digest unchanged" could never hold across a ref advance — the frame contains StateId. The witness, not the digest, is the admission object.) Reducer read traces remain a separate OCC concern (§13). Consequence stated: agents compiled from broad shared context invalidate often; agents whose compilation profile is scoped to their namespace run in parallel indefinitely.

**Parallelism arrives with its first consumer, as observation.** From Stage 2, every reducer's reads are traced through `ScopedStateView` (§13) and recorded. When real parallelism arrives — the §33 demo's two-agent drill is the first activation, Stage 10 the general case — admission becomes classic OCC: validate the *observed* read set (including prefix memberships) against the interleaved writes; disjoint linearizes, overlap branches. Observed, not declared: the trace is enforced by the read path itself and audited by replay (§29). Law 11 names the design intent; its enforcement is staged.

### Turns

A turn is the agent-shaped profile of the store's general primitive — the **durable publication batch**: open, accumulate durable steps, publish once. A LangGraph superstep is the same batch wearing different clothes (§3); nothing in the store knows about chat.

A single agent turn — user message, several invocations, tool calls, memory writes — produces multiple nodes, built as a chain and **published with one fenced CAS** to the tip:

```text
head H ──┐  (durable, unpublished)  c₁ → c₂ → c₃ → c₄
         └────────────────────────────────────────── publish(ref, H→c₄, fence)
```

Observers see turns, not keystrokes. Races happen once per turn. Every record in the chain carries the same turn ULID; the DAG surface collapses turns by default. Durability needs no ceremony: every `commit` is a transaction; the turn journal row (`canon.turns`) makes an in-flight turn findable after a crash. A crashed turn that touched nothing is closed and its unreferenced chain is swept. If it carried paid evidence — an invocation that returned before the crash — recovery **publishes a record-only node on the ref** folding that evidence in, then closes the turn: evidence worth keeping is kept by publishing it, never by exempting it from GC.

### The fence

> **A live effect reserves its causal position.** The world may not change on behalf of a turn
> that can subsequently lose its place in live history.

The failure this closes: worker A opens turn T1 from live head H, records an email intent, dispatches, and stalls. Worker B acquires the lease and advances the ref past H. T1's publication can now never succeed — but the email was sent. Under the fence this cannot happen: an open turn with a durable effect intent, bound to a live ref (`canon.turns.ref` makes the predicate queryable), **semantically occupies that ref**, and failover must resolve it — complete it, or reconcile its effects (§15) into an absorbing record — before any new live turn is admitted. (Two predicates, precisely: `open()` refuses while *any* open turn holds the ref — that is serial-per-ref, enforced by the partial unique index (§12); *occupation* is the stricter state — open **and** effectful — that additionally obliges failover to reconcile before advancing.)

The token discipline, precisely, because fencing that is vague is fencing that is absent:

- The token is **per lease**: acquiring or recovering a ref's lease increments `canon.refs.fence` and the new holder carries the returned value. Publication CAS and every mid-turn durable step assert `fence = $token` — a stale holder fails at its next write, and consecutive publications under one lease all carry the same token.
- **Absorbing an occupied turn bumps the fence first**, so the stalled worker's pending writes and publication are dead before reconciliation begins.
- **Dispatch is fenced too**, not just publication: the kernel dispatches only after a fresh fence-equality check *and* with remaining lease ≥ a safety margin Δ; failover waits lease expiry + Δ before absorbing. The irreducible residue — a dispatch in flight inside the Δ window while the fence is bumped — is bounded by Δ plus clock skew and handled where all effect uncertainty is handled: the absorbed turn's intent is reconciled as `unknown`-and-escalate (§15), with the deterministic idempotency key deduplicating on providers that support it. Stated as a limit, not hidden as an assumption.

This is a Stage 4 crash drill, not a paragraph.

---

# 15. Effects

The transition pipeline is excellent for state changes. It is insufficient for `send_email`, `charge_card`, `deploy` — because there is no transaction that spans the runtime and the rest of the world.

The failure that defines the design: the email sends, the process dies before the record. A retry sends it twice.

So the world is only ever touched **between two durable facts that say so**:

```text
fact 1  (canon.effects: intent, in the chain-step transaction)
   "I intend effect E, idempotency key K, under capability C, authorized by A, approved by R"
        │
        │   kernel dispatches E          (ops.attempts journals each try)
        ▼
   the world changes — or doesn't — or we cannot tell
        │
        ▼
fact 2  (canon.effects: observation)
   "E succeeded | failed | unknown; receipt ρ"
```

**Effects are immutable facts, not a mutable phase machine.** There is no `dispatched` record — before dispatch it would assert what a crash can falsify; after dispatch it is redundant with the observation. Current status is a projection over the facts. Dispatch attempts are operational (`ops`), not semantic.

Turn finalization is immutable action semantics, not a third field retrofitted onto the frozen effect-fact ABI. `effect-action/v1` means `absorb`; `effect-action/v2` records `absorb | publish-or-branch` explicitly. The intent's action digest binds those bytes (and therefore the policy), while the session-free execution request carries the derived value to recovery and must match the canonical action. This preserves historical EffectFact bytes and hashes without pretending an unversioned record change is backward-compatible.

The **idempotency key is minted deterministically** — from the proposal id and the action hash — so a re-run of a crashed turn reaches the same key and the outbox lookup returns the recorded outcome instead of re-dispatching. An orphaned outcome (an observation whose turn never published, because recovery proposed differently) is a first-class reconciliation item on the approval surface, never silently dropped.

**Approvals precede intents — and park their turn.** An effect that needs human approval publishes an **approval-request fact** and then **closes its turn without publishing an intent**: the chain stays reachable through the request, no intent means no occupation (§14), and the closed turn frees the ref's open-turn slot — a human deciding overnight blocks nothing. Requests expire or cancel. Approval spawns a fresh turn that revalidates — head, authority epoch, payload hash, projection hash — before the intent is recorded and dispatch proceeds; if the head moved overnight, ordinary admission (§14) decides linearize-versus-branch, and a stale approval produces a new request, never a silent re-bind.

What the bracket honestly guarantees is **executor-class-specific**, and acceptance tests say so:

```text
provider-enforced idempotency     the same key cannot cause a second effect
queryable outcome                 reconcile before any retry
non-idempotent, non-queryable     never retried automatically; unknown recorded and escalated
reversible                        compensation semantics recorded — not transactional rollback
```

The seam is a port, defined with the bracket at Stage 4 because a swap promised without an interface is a hope: an **EffectDriver** declares its reconciliation class, dispatches, and reconciles; an **ExecutionDriver** runs the bracket's activities — `LocalExecutionEngine` in v1, Temporal behind the same interface at Stage 11.

A crash between the facts leaves an explicitly representable truth: *the effect may or may not have occurred.* Recovery finds the intent in the outbox (durable by §5), the fence holds the ref (§14), and reconciliation queries the provider by key — or records `unknown` and escalates. Honestly: most real APIs, email first among them, offer no query-by-key, so `unknown`-and-escalate is the *common* path; every effect executor declares its reconciliation class up front, and the approval surface treats `unknown` as a first-class outcome. Non-idempotent APIs are **reconciled, never blindly retried**. Reversible effects declare compensations.

This protocol exists **before Stage 4's gate admits any external tool** — before the first tool, not after the first incident. It is exactly the shape Temporal activities want (Stage 11), which is why swapping the execution engine later does not disturb the domain.

> **Effects are not transactions.** Intend, act, observe — two facts, one world, and a fence
> holding the turn's place in history.

---

# 16. Realms

Branches materialize counterfactuals. Counterfactuals must not send email.

> **Only the universe's designated live binding is live.
> Every other binding — history, fork, experiment, evaluation — is a simulation by construction.**

Realm is a property of the **execution binding**, resolved by the kernel — never a property of a node:

```ts
interface ExecutionBinding {
  universe: UniverseId;
  at: Ref | PinnedNode;
  realm: { kind: "live" } | { kind: "simulation"; world?: SimulationId } | { kind: "replay" };
  principal: Principal;
  authority: AuthoritySnapshot;            // attested — §17
  fence: Fence;
}
```

Only the binding whose `at` is the universe's live ref resolves to `live`; a pinned historical node — even one that arose in live history — resolves to simulation or replay. Nodes record where they arose (`executedIn`, provenance); bindings decide what a continuation may touch. Consequences, all free: time-traveling to March and forking cannot touch today's calendar; evaluation branches are safe at any scale; an external effect requires a live binding **and** an attested capability **and** policy/approval — three independent gates.

**Promotion** — making a simulated continuation real — is a **three-way reconciliation routed through a standard turn** (built at Stage 6, beside the merge machinery it reuses), not an adoption and not a blind replay:

```text
base       = fork point          candidate = simulation tip          current = live head

promotion proposal = reconcile(base, candidate, current)     — §24 machinery, not bespoke
   state discoveries        reconciled; conflicts surface as conflicts (contested values)
   simulated effects        never imported; re-proposed through the full pipeline —
                            re-authorized, freshly approved (approvals never transfer, §17),
                            re-executed via the bracket with fresh receipts
   simulation-derived claims  cross over labeled `simulation` (§20) — hypotheses, not facts
   independent paths        commute
```

Because promotion is a standard turn on the live ref, a moved live head is handled by §14's ordinary rules rather than a bespoke race. The **promotion report** — what copied, what re-ran, what was refused, what stayed tainted — is evidence, and the honest replacement for any blanket taint promise. The simulated branch keeps its nodes and ids; session pins survive; live ancestry contains only what live execution produced.

> **Forking state does not fork the world.**

---

# 17. Authority and the kernel

The most dangerous idea in v0.1 was quiet: the runtime loads from the tree, and agents may someday edit the tree. Unconstrained, that is privilege escalation as a feature.

> **Authority flows from the kernel inward, never from the tree outward.
> The tree can only narrow its own power.**

**The kernel is the trusted computing base.** It owns: storage integrity, credential resolution, authorization, budgets, resource limits, runtime-bundle verification. It owns no goals, no memory, no reasoning, no identity. And honestly: in v1 the kernel is a library boundary inside one process — an API-level control that stops confused deputies and logic errors, not a privilege boundary against arbitrary in-process code. The interface is kept narrow — credential resolution, attestation, dispatch behind one seam — so extraction into its own process is mechanical, scheduled hardening (Stage 10+), not a rewrite.

**Capabilities are references; authority is attestation.**

```json
{ "capability": "google-calendar.write", "grant": "cap_82h…", "scope": ["calendar:primary"] }
```

That JSON in state is a *description of a wish*. At execution time the kernel attests `(principal × grant × universe × binding × realm × scope × expiry)` against stores outside the tree. Revocation is retroactive — a historical branch never resurrects a revoked grant.

**One egress law, no exceptions for inference:** a model invocation dispatches only under an **attested model capability**. Provider credentials and the dominant daily spend pass through the component that owns credentials and limits — closing v0.4's quiet hole where inference bypassed "the only source of authority." Budgets live here too: the authoritative consumption counter is kernel-plane, not State (writing usage into State would churn StateId and fight convergence) and not a disposable rollup; `proj` carries the queryable copies.

**The attenuation algebra.**

```text
fork:     child capabilities ⊆ parent's
merge:    capabilities = intersection of parents'
expand:   only by a recorded operator grant (an approval, held as evidence)
realm:    external effects additionally require a live binding (§16)
```

**Capability scopes are path-shaped** over logical paths (§9), and since v0.5 they gate model egress too:

```ts
interface CapScope {
  paths?: readonly Selector[];      // e.g. ["agents/researcher-17/**", "workspace/**"]
  tools?: readonly ToolId[];
  models?: readonly ModelRef[];     // the egress law's surface — no invocation without a match
  budget?: BudgetRef;               // kernel-plane counter this grant draws down
  effects: "none" | "reversible" | "external";
}
```

Read authority is enforced in the API: reducers and compilers receive `ScopedStateView`s (§11) — an agent's private memory is unreadable across scopes at the type level, not deprioritized in ranking. Authority labels on provenance are **derived by the runtime from authenticated origins**, never author-supplied — a claim cannot say "operator said so" unless an operator did.

**Runtime self-modification, bounded and deferred.** Runtime bundles are signed and referenced by digest, verified against a signer root outside the tree — but in v1 the kernel loads only its built-in runtime, so signature verification and compiler sandboxing activate when a second bundle can exist at all (Stage 10+, with self-modification itself). `runtime/**` merges are `forbidden` automatically. Every node records `kernel` and `runtime` versions.

**Approvals bind to what was seen.** An approval records the payload hash, the node, **and the projection hash** — produced by a **versioned, kernel-registered renderer** whose digest is recorded; an unregistered rendering cannot produce a bindable approval. The Stage 3 terminal renderer is the first registered projection. Checked at execution time against the executing node, closing approval-replay and TOCTOU. Approvals never transfer across realms (§16).

> **Authority is attested, never authored. Power only narrows.**

---

# 18. Evidence

Evidence is what you record because it cannot be regenerated: the model's actual response, the provider's receipt, the exact bytes a human approved, the exact context a model saw.

What is evidence: compiled contexts, invocation requests/responses, provider-opaque continuation state, effect receipts, approvals, validation records, compaction records.

Where it lives: records and hashes in `canon`; payloads in the content-addressed blob store, under an **erasure namespace** — its own identity, defaulting 1:1 with the universe but decoupled by design (a subject can be a namespace). Blob dedup happens within a namespace only, so one subject's blob erasure can never delete another's bytes (inline canonical values follow the per-universe rule of §22); indexed in `proj`, disposably.

**Availability is explicit and retention-scoped:**

```text
EvidenceAvailability = full | replayable | audit-only | redacted | expired
```

Retention classes: `permanent` (receipts, approvals, transition records — the audit trail) and `standard` (compiled contexts, requests, responses — expirable by policy age to cold storage or deletion). Expiry and redaction resolve reads to typed absences carrying the original hash — references never dangle silently. The conservation law is stated, not hidden:

> **You cannot simultaneously guarantee permanent exact replay and guaranteed physical erasure.**
> Evidence records are canonical; payload availability is a policy outcome, and every invocation
> can truthfully answer which epistemic guarantees still hold.

Properties:

- **Survives the loss of `proj`.** Indexes are projections of evidence, never its home.
- **Canonical, but not cognition.** Evidence is not compiler input by default; the compiler decides what enters awareness.
- **Sanitized at ingest, honestly.** Payloads are scrubbed for credentials before becoming evidence; scrubbed bytes are never called exact. Where exactness matters, the sanitized canonical representation may be paired with a sealed raw payload under a stricter retention and access class.
- **Priced, not discovered.** Evidence, not state, dominates storage. The invocation request record *references* the compiled context rather than embedding it; §28's rollups price evidence bytes alongside tokens.

> **Evidence is canonical, but it is not cognition.**

---

# 19. Invocation and the Continuation Frame

An **Invocation** is one request to one model endpoint yielding one observable response. A turn *contains* invocations; an SDK that collapses a multi-step loop into one opaque operation destroys the causality this architecture preserves. AI SDK Core is used as provider normalization; the loop is ours.

**State alone is not sufficient to define an invocation.** The state is complete over what the runtime controls — but at invocation time, cognition also depends on things deliberately outside State. v0.5 names the thing cognition actually operates on:

```ts
interface ContinuationFrame {
  state: StateId;
  input: InputRef;                       // the accepted observation (§13 — canonical before compile)
  realm: ExecutionRealm;                 // §16 — simulation compiles different affordances
  authority: AuthoritySnapshot;          // attested grants — revocation changes cognition, not just enforcement
  tools: ToolRegistryDigest;
  retrieval: RetrievalSnapshot;
  runtime: BundleDigest;  kernel: KernelVersion;
  modelProfile: ModelProfileDigest;
}
// frameDigest = H(all of the above) — the compile memoization key's foundation (§20)
```

```ts
interface InvocationRecord {
  id: InvocationId;
  frame: FrameDigest;                    // compiled from — the full circumstance
  inputNode: NodeId;
  capability: CapabilityRef;             // §17 — the attested model grant it dispatched under

  agent: AgentId;
  model: { requested: ModelRef; resolved: ModelRef; providerResponseId: string };
  sampling: SamplingConfig;

  compilerDigest: Digest;
  compiled: BlobRef;                     // the CompiledContext — evidence

  request: BlobRef;                      // references `compiled`; never embeds it
  response: BlobRef;
  providerState?: BlobRef;               // opaque continuation state (reasoning blocks) — stored, never compiled

  usage: TokenUsage;
  attempts: number;
  startedAt: Time; finishedAt: Time;
}
```

There is no `resultNodes` field — an immutable record cannot reference nodes created after it; transitions reference the InvocationId, and the reverse relation is a derived index.

**RetrievalSnapshot identifies a materialization, not a wish:**

```ts
interface RetrievalSnapshot {
  basis: { ref: Ref; position: number }; // publication position absorbed (§28) — a bare NodeId cannot order
  indexEpoch: Ulid;                      // a rebuild is a NEW epoch, same basis or not
  indexSchema: Digest; embeddingModel: Digest; rankingPolicy: Digest;
}
```

Recorded on every compile, live included. Same source history ≠ same retrieval materialization; the epoch keeps the cache honest.

**The reproducibility ladder, with availability honesty**: *reconstructable* (rebuild exactly what was supplied), *auditable* (explain what happened), *replayable* (recorded outputs drive the runtime deterministically) — claimed **while the referenced evidence is available** (§18); *re-executable*; *deterministically reproducible* (generally unavailable from hosted models). For A/B evaluation, the strongest method needs no retrieval at all: reuse the recorded `CompiledContext` (§29).

Streaming is the miniature of the effect problem: tokens a human has seen are provisional session output; the committed response is semantic output. If a stream dies at token 200, the session shows the wound honestly; the state never contains it.

---

# 20. The compiler

The compiler is the agent's attention. State is what exists in the agent's world; the compiler determines what is cognitively present *now*:

```text
Frame ─→ compile ─→ CompiledContext ─→ model ─→ proposal ─→ transition ─→ State ─→ Frame′
```

which makes compilation policy itself a branchable, evaluable cognitive architecture.

```ts
interface CompiledContext {
  items: readonly CompiledItem[];        // stored as a tree of blobs → structural sharing
  budget: Budget;
  witness: CompilationWitness;           // what could have influenced selection — the admission object
  record: BlobRef;                       // full selection process — evidence
}

interface CompilationWitness {           // the dependency witness — what admission validates (§14)
  stateReads: readonly Selector[];       // prefixes and queries consulted — not just winners
  selectedSources: readonly SourceRef[];
  retrieval: RetrievalSnapshot;
  authority: Digest;                    // digest of the attested snapshot — self-certifying
  availabilityEpoch: bigint;             // §22 — redaction invalidates dependent compilations
  realm: ExecutionRealm["kind"];
  toolSetDigest: Digest;
}

interface CompiledItem {
  content: BlobRef;
  source: Path | ClaimId | NodeId;       // provenance: where from
  authority: "kernel" | "policy" | "operator" | "agent" | "external" | "simulation";
  stability: "prefix" | "recent" | "volatile";
  reason: string;  priority: number;  tokens: number;
}
```

**Provenance includes authority.** A scraped webpage saying "ignore previous instructions" is `external` — data, not instruction; policy gates what each authority class may influence. `simulation` marks content whose provenance passes through a simulated receipt (§16): a hypothesis, weighted accordingly. These labels travel from ingest through memory into every future compilation — the defense against injection that persists across months.

**Stability is economics.** Providers price cached prefixes at a fraction of fresh tokens. `prefix` items (identity, standing policy) are byte-stable across turns; `recent` is append-mostly; `volatile` churns at the tail. The same stability gives structural sharing in storage.

**The v1 algorithm, written down** so it exists before it is learned:

```text
1. gather candidates per category with fixed budget shares:
   identity 2% · policy 5% · tasks 8% · dialog 30% · memory 35% · artifacts 12% · tools 8%
2. score: priority = f(category, recency, retrieval score, pin)
3. select greedily per category within share; spill unused share by fixed order
4. order: prefix (stable bytes) → recent (chronological) → volatile (priority)
5. redact at the boundary; label authority; emit witness and record
```

**Deterministic given the frame**: the memoization key is `(frameDigest, compilerDigest)` — nothing else. Because the frame carries authority, tools, realm, and the retrieval epoch — and the availability epoch reaches it through the witness — revoking a capability, rebuilding an index, or redacting a payload changes what compiles, and the cache cannot serve stale cognition. Three digests, three jobs: the frame digest keys this cache, the witness gates admission (§14), and the compiled-context digest names the exact bytes (§19).

**The record answers both questions** — why did the model see this, and why did it *not* see that: candidates, selected, rejected-with-reasons, budgets, digests. Context debugging is an inspectable runtime feature, not archaeology.

**The policy object is Σ — v0.7 (ADR-013).** The shipped pipeline is already the six-stage `/v2` form (gather → score → select → epistemic-complete → order → render, Law 12), and `COMPILER_POLICY_V1` is already a digested policy value — that value is the first **Context System**. The landing shape, written down before it is built: Σ becomes named, versioned canonical data with three binding sites — build default, agent (`agents/<id>/psyche/**`, ADR-012), and situation (per-turn selection or overlay; the choice and its reason enter the compilation record) — extracted when the second real Σ exists, not before. Two record obligations arrive with the next compiler touch: candidates write their named feature components (recency, retrieval score, pin, chronology) into the compilation record beside the collapsed priority — offline re-ranking and stage ablation then replay from evidence alone — and rankers stay Σ-owned weights over those features, never module-local scores. A **ContextDiff** between two records is a derived tool (Stage 8's node inspector; `context compare` in the terminal), never a stored object.

---

# 21. Memory

Memory is canonical; retrieval is derived.

**Memory is claims plus lifecycle transitions.**

```ts
interface Claim {
  id: ClaimId;
  content: BlobRef | CanonicalValue;
  sources: readonly SourceRef[];        // provenance; authority labels derived, never author-supplied (§17)
  observedAt: Time;                     // when it was true of the world
  confidence?: number;
}
```

Claims live at `memory/claims/<ulid>` and never change. Lifecycle is expressed as transitions — `memory.assert`, `memory.contest`, `memory.supersede`, `memory.retire` — and **current status is a projection of ancestry**, never mutated in place. M1 was correctly active in January and superseded in August without ever having been "wrong": observation time and validity time are distinct.

Retrieval starts as Postgres FTS beside the canonical tables, behind the basis watermark (§28). pgvector and hybrid ranking arrive when measurement — not aspiration — says retrieval quality is the bottleneck. Retrieval returns references into canonical state; indexes are deleted and rebuilt as a standing test, at corpus scale.

Access is enforced where reads happen: `ScopedStateView` and the compiler honor path scopes (§17). Private memory is private at the read path.

---

# 22. Compaction and retention

**Compaction is a state transition, not deletion.** N₆ continues from `summary(N₁…N₄) + unresolved obligations + active claims + references`, while N₁…N₄ remain. The compaction record carries: source frontier (not a "range" — ranges are ill-defined on a DAG), source digests, compactor version, retained facts, omitted information, retention class. Reversible while sources remain available — retention is part of compaction's contract.

> **Reachable is forever; unreachable is policy.**

- Ref classes: `live` and `archive` anchor history indefinitely; `exp/` and `eval/` carry TTLs; deleting a branch archives its head unless policy explicitly authorizes pruning.
- **Canonical GC** is mark-and-sweep over `canon.objects` from reachable roots — the `gc_sweep` role is one of two audited writers of deletions. Open turns (`canon.turns`) are roots. No grace window is needed for canonical objects: reference and object are created in one transaction.
- **Blob GC** keeps the grace window (uploads precede references, §5) plus roots for open turns and the `permanent` class. Policy expiry goes through the typed-absence path (§18), never the sweep.

And the companion law:

> **Logical history is immutable; physical storage is governed.**

A **tombstone** is a transition that marks content excluded-from-compile, excluded-from-retrieval, excluded-from-export — and physically erases the payload:

- **Blob payloads**: deleted within their erasure namespace; reads resolve to `{ kind: "redacted", hash }`.
- **Inline canonical values**: bytes are **never mutated under their hash** — a content-addressed store that lies about content is worse than one that cannot forget. Erasure is one audited row in the **availability ledger** (`canon.availability`, §12): reads consult it and resolve to `{ kind: "redacted", hash }`, and the object row is then physically scrubbed by `gc_sweep` under the ledger's authority. The hash chain survives; verify-by-hash treats ledger entries as first-class; and because the ledger, not the object table, carries redaction, a future legitimate write of identical bytes is not silently swallowed by a poisoned key. Two consequences are designed, not discovered: **redaction bumps the universe's availability epoch**, which sits in the compilation dependency witness (§14, §20) — no memoized compilation keeps serving erased bytes, and the blast radius is stated: the epoch is per-universe, so one redaction invalidates every in-flight compilation in that universe — a rare event bought with deliberately coarse, simple invalidation — and **derived evidence containing the subject (compiled contexts, requests) is swept through the same ledger**. Stated honestly: inline values dedup by content within a universe, so redaction is per `(universe, hash)` — every referent of those bytes in that universe reads `redacted` afterward; the audit lists referents before the operator confirms; and data whose subjects must be independently erasable is **blob-indirect from admission** — the §9 `subject`-tag rule is mandatory routing, not advice. One drill belongs beside the design: restoring from backup or WAL replay must not resurrect redacted payloads — the ledger restores with the data (Stage 7 acceptance).

  Was the previous design wrong? Twice, and the record should say how: v0.4's rewrite ceremony could not erase without destroying the universe's identity; v0.5's redact-in-place erased by making the store lie about content — leaving caches serving erased bytes and poisoning the key against future writes. The ledger is the design that survives both reviews.

For PII erasure, committed credentials, and legal requirements. Privileged, audited, rare — but designed, because "we can't delete it" is not an answer the world accepts, and an escape hatch that isn't designed becomes a crisis that is improvised. Per-subject envelope encryption of evidence blobs remains a compatible, deferred upgrade.

---

# 23. Branches and refs

Branches are rows, cheap, and used liberally — with a namespace, a disposition, and a lifecycle:

```text
live                       the one live ref (§16)
agents/<id>/…              agent work, private by scope
exp/…                      experiments — TTL'd
eval/…                     evaluation branches — aggressively TTL'd
sim/…                      simulations
archive/…                  anchored history
```

Disposition (`mainline | experiment | merge-likely | temporary | archive | simulation`) is display metadata and may live in `proj`. But **anything that drives destruction is durable**: TTLs, pins, and retention classes live in `ops` (or `canon`, where they are policy) — GC that reconstructs its inputs from a disposable projection cannot be audited and cannot survive the drop-`proj` drill. The realm rule depends on none of this — only on which binding resolves live (§16). Metadata advises; the kernel enforces.

Do not assume every branch merges. Most won't. That is the point.

---

# 24. Merge

The store contributes ancestry and structural three-way merging over the logical tree. Meaning is ours.

**Merge is transition-aware.** The inputs are not three states but three states *plus the transitions that produced each side* — "task removed as completed" and "task removed as cancelled" have identical trees and different meanings. Intent lives in the record, and the merge reads it.

**Strategy dispatch is per logical path-pattern**, with inheritance and a default:

```text
memory/claims/**        union          (automatic — record-per-object, disjoint leaves)
dialog/**               union
tasks/**                domain         (task-graph three-way)
workspace/**            three-way
agents/*/identity/**    manual
runtime/**              forbidden
env/config.json         manual
default                 three-way
```

`three-way` on canonical records means **structural JSON three-way** — a runtime merge driver over parsed canonical values (in `packages/runtime`); the store's merge is tree-structural only.

**The result is typed, and conflicts are data** — and they are *values* (§11):

```ts
type MergeResult = Clean | Conflicts | Rejected;

interface PathConflict {
  path: Path;
  base?: ValueRef;
  left: ValueRef;  leftCause: TransitionRef;
  right: ValueRef; rightCause: TransitionRef;
  strategy: MergeStrategy;
  resolution?: ValueRef | "left" | "right" | "both";
}
```

A merge node may carry unresolved conflicts as **contested values in state** (`StateValue.contested` — Jujutsu's first-class-conflicts model is the prior art), and each path policy declares whether continuation-while-contested is permitted:

```text
memory claims        continue        artifact prose      continue
task descriptions    policy          effective capability   never
runtime definition   never
```

Never hide disagreement behind a generated summary. Domain invariants run *after* reconciliation too.

**One semantic policy, fully worked — memory**: claims union automatically; lifecycle events union; the active set is a recomputed projection, never merged; contradictions (same subject, incompatible content by the domain comparator) become a contested pair via an auto-emitted `memory.contest` in the merge node — nothing synthesized, the disagreement stored; identity claims are manual, always.

**Agent-proposed resolutions are proposals** through the same validate → authorize pipeline — "models propose; the runtime commits" has no merge-shaped exception.

Three operations, named: **reconciliation** (two continuations of one agent — this section), **assimilation** (A learned X; B incorporates X with cross-branch provenance — cherry-picked claims), **fusion** (A and B become C — an explicit rite, out of scope until Stage 10+). Promotion (§16) is a constrained reconciliation. N-way merges decompose into ordered pairwise merges. Permission expansion through merge is forbidden by the algebra (§17).

---

# 25. The reference host: Session, Surface, Interaction

Everything from here through §27 is the **reference host** — the first consumer of the core, and the seed of the product on the roadmap: a Claude-web-like, multi-user application that just works, its surfaces skinned from copied-in chrome over the shadcn substrate (ADR-014). It is designed now and built at Stages 8–9, when a second user exists. It is not part of the frozen core (§2); it freezes when it ships.

A **Session is not a Universe.** It is an interactive environment in which humans and agents work.

```ts
interface Session {
  id: SessionId;
  participants: readonly Participant[];
  bindings: readonly ContextBinding[];     // resolve to ExecutionBindings (§16) at the kernel
  surfaces: readonly SurfaceDescriptor[];
  capabilities: readonly SessionCapability[];
}

type ContextBinding =
  | { mode: "follow";  universe: UniverseId; ref: Ref }
  | { mode: "pinned";  universe: UniverseId; node: NodeId }
  | { mode: "compare"; universe: UniverseId; nodes: readonly NodeId[] }
  | { mode: "none" };
```

Follow moves as the ref advances. Pin observes history — and continuations from a pin are simulations by construction (§16). Every surface shows the binding's **realm** — a human always knows whether they are looking at reality or a counterfactual.

A **Surface** is one representation inside a session: `thread | dag | artifact | document | diff | task | agent | terminal | approval | timeline | custom`. `ThreadSurface` is one very important surface, not the application architecture — copied chrome renders it; the Session Runtime owns its behavior (ADR-014).

An **Interaction** is one accepted exchange and what it became:

```ts
interface Interaction {
  id: InteractionId;
  session: SessionId;
  participant: Principal;
  surface: SurfaceId;
  command: CommandRef;
  outcome:
    | { kind: "transition"; node: NodeId }     // it changed reality
    | { kind: "session" }                      // it changed only the session
    | { kind: "rejected"; error: ErrorClass };
}
```

**Where messages live** — the load-bearing decision: the UI message is a surface rendering; the *accepted content* is canonical. A user message accepted by the runtime becomes an observation transition writing `dialog/<ulid>` (`role`, content or blob ref, `at`, `via`) — before compilation, so the model continues from a State containing what it is responding to (§13). `ThreadProjection` is a fold over dialog records and invocation evidence along the binding's ancestry — reconstructible from the universe alone. Edit-and-regenerate forks the universe; the only UI-local branch is an unsent draft.

The heuristic survives verbatim:

> Would this change what the agent can know, believe, access, or do on its next continuation?
> If yes — Context. If no — Session.

---

# 26. Commands, events, projections

The backend does not speak "chat." It speaks:

```ts
type Command =
  | SendMessage | InvokeAgent | ProposeTool | ApproveAction
  | EditState | EditArtifact | AssertClaim
  | ForkContext | CheckoutContext | MergeContexts | PromoteBranch
  | SpawnAgent | OpenSurface | UpdateSurface;

type Event =
  | MessageStarted | MessageDelta | MessageCompleted
  | ToolRequested | ToolStarted | ToolCompleted
  | EffectIntended | EffectResolved
  | ContextCommitted | ContextForked | ContextMerged
  | AgentSpawned | ApprovalRequested
  | SurfaceOpened | SurfaceUpdated | RuntimeFailed;
```

`EditState` is non-negotiable: a fully editable context was a founding requirement — fork-with-modification must feel like editing, not ceremony. `PromoteBranch` is §16's reconciliation. `EffectIntended`/`EffectResolved` surface the bracket so approval UIs see the world being touched.

**The engine protocol is session-free.** Beneath everything here sits the core protocol — commands and events keyed by `(universe, ref | turn)` — because Encounter is host-side (§2): a host with no sessions speaks it directly. The envelopes below are the **reference host's session wrappers** over that protocol; `sessionId` is their concern, never the engine's. Both layers stay framework-independent — a Python sidecar must be able to implement the wire without importing the TypeScript app:

```ts
interface CommandEnvelope { commandId: string; sessionId: SessionId; type: string; payload: unknown; expectedNode?: NodeId }
interface EventEnvelope   { sequence: number; eventId: string; sessionId: SessionId; type: string; payload: unknown; at: string }
```

`commandId` gives at-least-once delivery with dedupe. `sequence` is per-session monotonic and the event log lives in `ops` — it is *authoritative* for sequences (a client's `Last-Event-ID` must survive the drop-`proj` drill unrenumbered) and it carries events with no canonical source (`RuntimeFailed`, provisional deltas), so it was never a rebuildable projection; thread projections in `proj` remain one. **Events append in the transaction that makes their subject durable** (§5): mid-turn durable steps append `ApprovalRequested` and `EffectIntended` — both are durable facts *before* dispatch, which is what lets approval UIs see the world about to be touched — and publication appends `ContextCommitted` and its siblings; a client never sees an event for a fact that might not land. Streaming deltas are provisional session output (§19). **SSE reconnection resumes via `Last-Event-ID`** with server backfill; `LISTEN/NOTIFY` wakes the fan-out — notifications deliver post-commit and serialize around commit, so under write bursts the fan-out coalesces and falls back to polling; the escape is recorded here, not discovered in production. `RuntimeFailed` carries a structured class — `validation | authorization | race | transient | capacity | policy` — because retry behavior differs per class and clients should not parse prose.

**Attribution and fan-out (ADR-015).** Events have three audiences. Ref-publication events
(`ContextCommitted`, `ContextMerged`) fan out to every active session binding that follows the
published `(universe, ref)` at the ref-CAS linearization point. Turn-origin events
(`ApprovalRequested`, `EffectIntended`, `EffectResolved`, provisional message events,
`RuntimeFailed`) go to the session and command that originated the turn; other followers learn the
durable result from publication. Binding and surface events stay inside their session; a fork event
goes to the session that asked for the fork until another session explicitly follows its ref.

The reference-host adapter joins publication through a narrow transaction-bound sink carrying only
session-free facts `(universe, ref, node, position, turn, kind)`; the engine imports no Session type.
For each recipient, the sink locks the session row, allocates the next `sequence`, and inserts the
envelope before the publication commits. Durable `eventId`s derive from their fact identity; retries
therefore deduplicate on `(session, eventId)` without consuming a sequence. Provisional events mint ids
through the replay seam. `LISTEN/NOTIFY` is only a wake-up: every consumer backfills the authoritative
rows with `sequence > Last-Event-ID`.

Binding changes linearize against publication. Every transaction locks all affected `canon.refs` in
`(universe, ref)` order, then affected sessions in `sessionId` order. A binding change increments its
version and appends `BindingChanged` with the effective head and ref position. If publication wins the
ref lock, the old binding receives (or does not receive) the event before `BindingChanged`; if the
binding change wins, the new binding is the predicate publication sees. Event payloads carry the
matching binding ids and versions so the client fold is auditable rather than timing-dependent.

Transport: HTTP JSON for commands and queries; SSE for streams; WebSockets only where genuinely bidirectional.

---

# 27. Frontend

A normal React application with a central Session Runtime; no framework owns the core.

```text
React App
   └── Session Runtime
         ├── session state · bindings · realm badges
         ├── event stream (SSE, resumable)
         ├── commands
         ├──► ThreadSurface — copied AI Elements chrome + owned behavior layer
         ├──► DAG explorer (React Flow via the Workflow chrome — collapses turns by default)
         ├──► node inspector: state · diff · compiled context · invocation · effects · fork-here
         └──► artifact / terminal / approval surfaces
```

Stack (ADR-014 — chrome is copied and owned; behavior is the Session Runtime's): Next.js, React,
Tailwind + shadcn/ui as the substrate for every surface; AI Elements as copy-in chrome (thread ·
Workflow/React-Flow · Code/Artifact groups; Apache-2.0; the registry's force-injected
`ai`/`@ai-sdk/react` deps are pruned at install; `MessageBranch` — uncontrolled, all siblings
mounted — is forked into a controlled pager driven by fork topology); Streamdown (CJK-aware
streaming markdown) and use-stick-to-bottom as direct dependencies; TanStack Query keyed by
`(universe, ref | node)`; Zustand (ephemeral only). The thread behavior layer — branch state
machine, edit-as-fork, status/tool/approval wiring, attachment upload into the CAS — is written
against the Session Runtime: priced at ≈4–6 days over any component kit (ADR-014), bought once
instead of renting a Beta-tier runtime under quarterly breaking minors. assistant-ui re-tables only
on its recorded trigger (v1 · Stable-tier Runtime API · `ExternalThread` documented ·
branch-adapter semantics frozen). Stage 8 opens with a thin real event-log/SSE fold, immediately
followed by the forked pager plus Streamdown over one real thread with one fork. That vertical slice
becomes the first production thread code rather than a preview of Stage 9. Multi-user hardening follows
in Stage 9: authn, per-user principals through the kernel's
attestation, and row-level security on `universe_id` as defense in depth.

Before any of this exists, the walking skeleton's surface is a terminal plus a statically rendered DAG (Stage 3) — the ontology is felt long before the frontend is built.

---

# 28. Projections and the control plane

One Postgres, three schemas (§5, §12): `canon` is truth; this section is the other two.

```text
ops           users · leases · jobs · dispatch attempts · session connections · sequencer queues
              session event log (authoritative sequences — §26)
proj          node index (id, parents, generation, turn, kind, actor, summary)
              ancestry caches · branch display metadata · claim status · thread projections
              FTS · pgvector (measured-in) · cost rollups (evidence bytes + tokens)
              (TTLs, pins, retention classes — anything that drives destruction — are ops/canon, §23)
```

`canon` answers truth; `proj` answers questions quickly — and the line between them is schema discipline made testable: **the standing drill drops `proj` entirely and rebuilds it from `canon` plus evidence**, at corpus scale, forever. Implemented at Stage 2, run in every acceptance suite after.

Projections come in two tiers. The **transactional tier** (node index, claim status — plus the `ops` event log, which appends alongside them, §26) joins the publication transaction — read-your-writes is a property, not a barrier. The **asynchronous tier** (embeddings, expensive FTS) trails behind a **basis watermark**: basis is per-ref — the latest *published* node the index has absorbed, a monotone position along the ref's publication order (well-defined where DAG order is not); retrieval waits on `basis ≥ requested` with a bound, then fails with a typed `transient` class. A slow indexer degrades retrieval quality loudly — it never wedges the ref, and non-retrieval turns never wait.

`generation` is recomputed as `max(parents) + 1` on merge, so graph layouts are never subtly wrong. Per-invocation `TokenUsage` rolls up to branch and universe budgets — enforcement lives in the kernel plane (§17); `proj` holds the queryable copies.

---

# 29. Observability and evaluation

OpenTelemetry, with every span carrying: `universe.id`, `node.id`, `turn.id`, `ref`, `realm`, `session.id`, `agent.id`, `invocation.id`, `transition.kind`, `effect.id`, `frame.digest`, `kernel.version`.

The acceptance test that matters: **from any trace span, navigate to the exact node** — its state, diff, compiled context, invocation, effects. It lands with the first web surface (Stage 8).

**Replay is the spine, from Stage 1.** Every source of nondeterminism — time, ULIDs, randomness, model responses, tool results, and identities minted inside an adopted host — enters through one injected seam and is recorded from the first engine commit. Every acceptance run executes twice: live, then replayed from the tape — asserting identical record hashes, topology, frame digests, compiled bytes, authorization decisions, effect plans, and read traces, with exact tape consumption; StateId equality alone would let divergence hide in the records. Host protocols remain runtime-generic: an adapter captures and maps its host-minted identities at the boundary before they become canonical keys. This enforces "replayable" (the core proposition's least-tested leg) from day one, audits observed read-traces (§14), and makes the entire runtime testable with zero providers — the tape harness is not a late feature; it is how the project is built.

**Evaluation is branching.** From one node: model A vs B, compiler A vs B, memory strategy A vs B — compared as trajectories. Two rules keep comparisons honest: evaluation bindings are never live (§16), and the strongest comparison reuses the recorded `CompiledContext` — same bytes, different model — with retrieval never re-run (§19). Where retrieval must re-run, the frame pins the index epoch.

Metrics: correctness, cost, time, tool-call count, state quality, memory quality, downstream success, reversibility, branch divergence.

---

# 30. Schema evolution

Never rewrite historical nodes because schemas changed. A node declares `schema` and `encoding` (§7–8); readers support historical schemas **within a bounded horizon**: the kernel maintains a supported window, and touching a node older than the window first produces a `schema_upgrade` child (upgrade-on-touch). The migration is provenance; the compatibility burden is finite. Before an old parser is removed, its migration reader is retained — or the affected universes are proactively migrated; the horizon bounds *support*, never *readability*. Upgrade-on-touch ships with the first breaking schema change; the conformance window is defined in the Stage 0 domain package. And versions are **axes, not one number**: the encoding (§8/§10), the state schema, the record schema, the wire protocol (Stage 8), projector schemas (rebuild *is* their migration), and runtime bundles each move independently — upgrade-on-touch governs the state and record axes only.

---

# 31. Deployment and repository

A modular monolith. Boundaries exist in code before they become network boundaries.

```text
context-runtime/            (this repository)
├── packages/
│   ├── domain/         # the executable spec: six objects, proposals, patches, CR-CJSON codec,
│   │                   #   state hashing, golden vectors, property tests — zod and nothing else
│   ├── kernel/         # attestation, capabilities, budgets, secrets            (TCB)
│   ├── store/          # Postgres implementation of Store + migrations
│   ├── runtime/        # transition engine, sequencer, merge drivers
│   ├── compiler/
│   ├── memory/
│   ├── replay/         # the nondeterminism seam, recorder, replayer            (Stage 1)
│   ├── ai/             # provider adapters (AI SDK behind here)
│   ├── tools/          # typed tools, MCP adapter, effect executors
│   ├── adapters/
│   │   └── langgraph/  # BaseCheckpointSaver + BaseStore — the one host until the seam is proven (§34)
│   ├── session/        # reference host: sessions, envelopes, SSE               (Stage 8)
│   ├── product/        # authenticated application service, commands, traces    (Stage 8–9)
│   └── observability/
│
├── apps/               # reference host applications                            (Stage 8–9)
│   └── web/            # Next.js UI + API routes, thread/DAG/inspector           (Stage 8–9)
│
├── bench/              # Stage 1 load probe; measured numbers → acceptance records
│
└── specs/
    ├── plan.md         ├── decisions.md
    ├── adr/            ├── acceptance/          ├── reviews/
```

**The spec is executable.** There is no parallel tree of eleven markdown spec documents — `packages/domain` (schemas, codecs, golden vectors, property tests) *is* the ontology, encoding, layout, transition, and effect spec; this plan carries the prose; ADRs carry decisions. Three normative layers for an audience of one was one too many.

**Domains compose statically.** Task, memory, dialog, and future domains register through a `DomainModule` — namespaced schemas, reducers, migrations, merge policies, compiler sources — wired at build time from Stage 2 on. This is ordinary application composition; what §34 defers is *dynamic* loading, not composition.

`packages/domain`'s only runtime dependency is zod — it is the schema language of the executable spec. `kernel` stays auditable in one sitting. Everything under `packages/` is a **private workspace package**; publishing any of them is a separate, later decision — a solo project should not carry public compatibility obligations it never sold. `apps/` is only the reference host. Directories are created when their stage begins.

---

# 32. Implementation sequence

One invariant at a time — with the felt experience pulled forward, the risks measured first, failure drills as first-class acceptance tests, and machinery staged to its first consumer.

**The critical path to the §33 demo is Stages 0–6.** Stages 7–11 follow it. Under schedule pressure, cut along this line — deliberately, not in panic.

**The mind-layer track (v0.7)** runs beside Stages 8–11, not inside them: GTC-catalog modules and named Context Systems arrive one at a time under ADR-012's rules (boundary IR, rule of two, composition as digestable data, the authority envelope), each measured before it stays — the **switching benchmark** (state constant, Σ varies), the **ablation ladder** (vector → +recency → +temporal → +graph → +epistemics → full), **leave-one-module-out**, and two headline metrics: **ContextUtility** (useful evidence delivered / compile cost) and **WritePrecision** (useful durable writes / all durable writes). Deterministic modules evaluate offline on recorded frames with zero providers (§29). Neither track blocks the other; neither track's acceptance is the other's.

## Stage 0 — Executable domain spec

`packages/domain`: branded ids, the six objects, proposals, patches, preconditions, `Commit`/`MergeRequest`/`Diff`, the CR-CJSON/1 codec, logical-tree state hashing (§8), the schema-conformance window definition (§30), and the frozen hash/value ABI (§8, §10) with **language-neutral golden fixtures and exported JSON Schema**; property tests (encode/decode roundtrips; hash stability incl. delete-to-empty and trie boundaries; patch-apply ⇒ StateId equality on vectors). Workspace tooling (pnpm, TS strict, vitest, fast-check, biome) arrives here.

Acceptance: suites green; ADRs ratified; Ren signs off — recorded as `specs/acceptance/stage-0.md`.

## Stage 1 — Store, probe, replay seam

`packages/store` on Postgres 16 (install postgresql@16 now — flagged in-session): `canon` schema, turns, outbox rows, refs with fenced CAS, `ScopedStateView` reads, structural diff/bases/merge, GC with audited roles. `packages/replay`: the nondeterminism seam, recorder, replayer — **from the first commit, every acceptance run executes twice** (§29).

Acceptance: the graph test (fork, merge, checkout, diff every node) **plus the measured probe in the production shape** (§12) with its two crash drills; numbers in `specs/acceptance/stage-1.md`. The substrate bet becomes fact; the fallback is named (§12).

## Stage 2 — Transition engine

Proposals, validation, the authorization stub — **deny-by-default against a static grant table held outside the tree**; it never reads capability JSON from the proposal or the tree, which is what makes the self-grant test meaningful before Stage 4 replaces the table with attestation — reducers over traced `ScopedStateView`s, verify (incremental re-hash), no-op and record-only rules, turns, the serial-per-ref sequencer.

Acceptance: invalid transitions cannot commit; **a self-grant proposal fails**; **a reducer writing outside its authorized prefix is refused at patch authorization** (§13); every commit's patch re-applies to hash equality; a race branches (never silently rebases); read-traces recorded and replay-audited; unchanged subtrees structurally share; the **drop-`proj`-and-rebuild drill** passes and becomes standing. *Then the ontology is revised once, and held under the conformance suites.*

## Stage 3 — Walking skeleton and first host

The vertical slice, in a terminal:

```text
> chat "design a pergola"        (commits a turn; dialog records per §25 — a Stage 3 deliverable)
> fork exploration               > checkout N42
> log --turns                    > diff N42 N57
> why N57                        (compiled context: selected & rejected, from the witness)
> summarize-epoch                (manual compaction with a minimal record: frontier, digests,
                                  retained/omitted summary — Law 8 is not suspended while young)
> dag --render out.svg           (the static DAG the demo shows)
```

One honesty note: the read-only tool is read-only by review until Stage 4's capability enforcement, and any binding's invocation ships its compiled projection to a provider by design — "simulation" bounds effects, not inference. Tape recording is already on (Stage 1). Provider keys arrive here, and **the egress law holds from the first real invocation**: the Stage 2 grant table carries a static model capability, so no invocation ever dispatches unattested — Law 13 is never suspended, not even for one stage.

And the **portability gate**, its own acceptance group: the LangGraph adapter against the real checkpointer contract (§3), plus **one deliberately contrasting loop-shaped micro-host** — two hosts prove a seam where one proves an integration. The `HostCheckpointCodec` round-trip is the base assertion.

Skeleton acceptance: §33's core feels natural in text. Portability acceptance: an off-the-shelf LangGraph example runs unmodified; **a partially failed superstep resumes without re-running completed tasks**; a checkpoint round-trips byte-exact through the codec; the micro-host publishes batches with no session, no compiler, no chat; the adapter's index rebuilds from `canon` with nothing lost; each AdoptionManifest matches observed coverage.

## Stage 4 — The world gate: effects, capabilities, realms

The bracket over the outbox (§15) with deterministic idempotency keys, reconciliation classes, and the approval-before-intent sequence; the `EffectDriver` and `ExecutionDriver` ports (§15); **live-effect fencing** (§14); ExecutionBinding realms (§16); the egress law — model invocations through attested model capabilities with kernel-plane budgets (§17), replacing Stage 2's static model grant; path scopes enforced by `ScopedStateView`; attenuation; approvals binding payload + node + registered terminal projection. (Promotion moves to Stage 6 — it is a constrained reconciliation and needs the merge machinery built there.) Full attestation of *additional* principals activates with the first second principal; the stub's static table carries until then (revocation-retroactivity already works — the table is consulted at execution time).

Acceptance (crash drills, not happy paths): `kill -9` between intent and receipt → recovery reconciles **per executor class** (§15's matrix — idempotent keys cannot double-execute; non-queryable classes record `unknown` and escalate, never auto-retry); **the fencing drill** — worker A stalls mid-effect, worker B must reconcile before advancing live; a pending approval does not occupy the ref, and a stale approval requires a fresh request; a simulation binding attempting an external effect is refused by construction; a revoked grant fails on a historical branch; approval replay fails; an orphaned effect outcome surfaces for reconciliation. **No external tool exists before this stage passes review.** Level 2 tool-wrapper middleware ships here.

## Stage 5 — Memory

Claims, lifecycle transitions, status projections, FTS retrieval behind the basis watermark, ACLs at `ScopedStateView` and compiler. pgvector only when measured. The claim store doubles as a host memory backend (LangGraph `BaseStore`).

Acceptance: the retrieval index deleted and reconstructed at corpus scale without semantic loss; a rebuild mints a new epoch and the compile cache does not conflate epochs; private claims invisible across agent scopes.

## Stage 6 — Domain merge

Transition-aware merge, per-path dispatch, structural JSON three-way, `MergeResult`, contested values with per-path continuation policy (materialized via the `contest` patch op, §13), the worked memory policy, merge fuzzing. **Promotion is built here** (§16) — it is a constrained reconciliation and reuses this exact machinery — with the promotion report. The conflict surface is terminal-grade here; its research-grade UX iterates from Stage 8 on.

Acceptance: two substantially diverged branches merge without silently discarding conflicting state; contradictions land as contested pairs; a reducer meeting a contested value behaves per policy; **a promoted branch re-runs its effects through the full pipeline and its report matches what happened**; property tests hold. **The §33 demo runs at the end of this stage** — its two-agent drill is the first activation of observed-footprint OCC admission (§14).

## Stage 7 — Compaction and retention

Full compaction records, frontiers, retention classes and availability tiers, canonical GC + blob GC with namespaces, tombstones through the availability ledger (§22), per-universe export. (Stage 1's GC was store hygiene — sweep mechanics; this stage is *policy*: retention, tombstones, the ledger.)

Acceptance: a compacted branch recovers source history and recompiles under a different strategy; a tombstoned payload is physically gone, honest logically, absent from compile/retrieval/export — for both a blob and an inline value, with dependent compiled evidence swept; **a backup/WAL restore does not resurrect redacted payloads**; an export round-trips into a fresh universe with verify-by-hash green.

## Stage 8 — Encounter: the complete single-user product

**Completion audit reopened 2026-08-10; remaining evidence is tracked in `specs/acceptance/stage-8.md`.**

`packages/session` + `packages/product` + `apps/web`: Session, bindings, Interaction, versioned envelopes,
command dedupe, transactional event attribution/fan-out, and SSE with resume over the authoritative
event log. The first product surface is the owned thread behavior layer (ADR-014): ThreadProjection,
streaming, tool and approval parts, controlled fork navigation, edit-as-fork, attachments into the CAS,
and realm-visible follow/pin/fork/compare. The same application ships the turn-collapsed DAG explorer,
ContextDiff, and the node inspector (state, diff, compiled context, invocation, effects, fork-here).
Ren opened this stage with the hosted-product track on 2026-08-10. The wire protocol and Encounter
conventions freeze here.

Acceptance: a user message is canonical before compilation; a thread reconstructs from canonical
dialog and invocation evidence after its projection is destroyed; edit-and-regenerate forks the
universe; two surfaces hold different bindings over one universe; a continuation from a pin is forced
into simulation; tool, approval, and attachment flows fold correctly; kill the connection mid-stream
and resume loses or duplicates nothing; the tape harness drives the complete loop with zero providers;
from any trace span navigate to the exact node (§29). The UI is product-grade at desktop and mobile
sizes: keyboard-usable, accessible, responsive, and free of placeholder-only flows.

## Stage 9 — Multi-user trust boundary

**Completion audit reopened 2026-08-10; remaining evidence is tracked in `specs/acceptance/stage-9.md`.**

Harden the already-working Stage 8 product for multiple people: authentication, session ownership,
server-derived principals (never trusted from a command payload), per-user attestation, universe
ownership and sharing policy, rate/size limits, and RLS on `universe_id` across canonical, derived, and
relevant operational reads. Stage 9 adds no second thread runtime and no alternative wire.

Acceptance: the complete Stage 8 suite passes unchanged behind authentication; two users cannot read,
command, inspect, attach to, or subscribe to each other's universes or sessions; guessing a session id,
event id, or `Last-Event-ID` reveals nothing; authorized followers of a shared universe receive the
same publication fan-out while unauthorized users receive none; and isolation still holds when `proj`
is treated as compromised.

## Stage 10 — Multi-agent

AgentGraph, spawning, private/shared scopes, fork policies, assimilation; observed-footprint OCC admission generalized (§14); kernel process-extraction hardening begins; signed bundles activate if self-modification does. Fusion is named and deferred.

Acceptance: N agents with namespace-scoped compilation profiles produce zero accidental branches under OCC; private state never crosses scopes; a knowledge claim assimilates with cross-branch provenance.

## Stage 11 — Durable execution

Temporal replaces `LocalExecutionEngine` behind the `ExecutionDriver` port defined at Stage 4 (§15). The bracket maps onto activities; Temporal history stays operational; Context history stays semantic.

Acceptance: the ExecutionDriver conformance suite — every bracket drill and every Stage 4 acceptance — passes unchanged against Temporal; the domain does not notice, provably.

---

# 33. First complete demonstration

Runs at the end of Stage 6, in a terminal plus a rendered DAG. The demo exercises the ontology, then tries to break it.

```text
N0 … N5: the agent designs.
User: "explore two approaches."
    N5 ├── exp/approach-A   (simulation binding — cannot touch the world)
       └── exp/approach-B
A1 → A2 → A3        B1 → B2 → B3 → B4        (independent)
Surfaces: terminal thread · rendered DAG (turns collapsed) · realm shown on every prompt
User selects both → Merge Proposal: agreements · conflicting assumptions ·
    contested claims · recommended reconciliations
User reconciles → A3 ─┐
                      ├── M1 → continuation
                 B4 ─┘
User time-travels to N5 → approach C → compares against M1.
User promotes B4's booking → the promotion report shows what re-ran, what was refused,
    what crossed over labeled `simulation`.
```

Then the failure drills, live, in the same demo:

```text
kill -9 between an effect's intent and receipt   → reconciled per executor class (§15); never silently touched twice
worker stalls mid-effect; a second worker joins  → the fence holds; reconcile before advance
two agents commit disjoint paths concurrently    → linearized under observed-footprint OCC; no branch
drop the proj schema                             → rebuilt from canon; retrieval degrades loudly, never wrongly
fork a three-month-old node                      → simulation; its email is refused
ask "why did the model not see claim X?"         → the compile record answers
replay the whole demo from the tape              → records, frames, and traces identical (§29); zero providers
```

If both halves feel natural rather than hacked together, the architecture works.

---

# 34. Things we explicitly should not build yet

- a second store backend (SQLite embedded dialect, PGlite) — until an embedded-only host demands it;
- the Git exporter and differential oracle — until someone wants the export;
- CRDT everything;
- a custom vector database;
- a polyglot mind-layer stack — queue/graph/cache engines beside Postgres; the one-engine rule extends upward (ADR-013);
- a proposition table — content addressing already provides proposition identity (§21, ADR-013);
- microservices;
- distributed consensus, or any cross-universe transaction;
- agent fusion;
- learned context compression;
- automatic semantic merging everywhere;
- runtime self-modification — including the signed-bundle verification and compiler sandboxing that will bound it (§17; they activate together, Stage 10+);
- arbitrary frontend plugins;
- a custom workflow language;
- a custom model-provider abstraction;
- adapters for every framework at once — one host proves the seam;
- per-subject envelope encryption of evidence blobs (§22);
- a global shared universe store.

Create interfaces where these may someday belong. Do not implement them until the system asks.

---

# 35. Twenty laws

Five groups of four. These function as project law and gate every review.

### On being

1. **One semantic source of truth.** What determines continuation lives in State — or enters through the Continuation Frame and is recorded (§19) — to the coverage each adoption level honestly declares (§3).
2. **A node is not a state.** State is what is; a node is what is *and how it came to be*.
3. **Same canonical content, same identity.** CR-CJSON bytes, runtime-computed StateId over the logical tree; equal structural content shares a StateId; no-op transitions commit nothing.
4. **Compiled context is a view.** The model sees one projection of one continuation frame — never the whole of being.

### On becoming

5. **History is immutable.** Never fix history; add another transition.
6. **Preserve provenance.** State whose origin cannot be explained is corrupted state.
7. **Evidence is canonical, but it is not cognition.** The record survives everything; payload availability is retention-scoped and truthfully answerable; the compiler decides what enters awareness.
8. **Compaction does not destroy.** Summaries optimize continuation, not history. (Derivable from Laws 5 and 19 — kept; a review checklist earns its redundancy.)

### On the world

9. **Effects are not transactions.** Intend, act, observe — durable facts before and after, one world — and a live effect reserves its causal position (§14).
10. **Forking state does not fork the world.** Only the live binding touches reality; every other binding simulates.
11. **Parallelism is not branching.** Commuting work linearizes; disagreement branches. (Enforcement is staged to its first consumer — §14.)
12. **Conflict is information.** Store disagreement — as a value — and never synthesize it away.

### On authority

13. **Models propose; the runtime commits.** No computation mutates reality directly — and no invocation dispatches without an attested capability (§17).
14. **Authority is attested, never authored.** State may reference capabilities; only the kernel makes them real.
15. **Power only narrows.** Forks attenuate; merges intersect; expansion requires a recorded grant.
16. **Approvals bind to what was seen.** Payload hash, node, and registered projection hash — or it is not consent.

### On structure

17. **Frameworks are adapters — in both directions.** They do not define the ontology; the runtime does not demand to own their loop.
18. **Derived state is disposable.** `proj` rebuilds from `canon` and evidence — as a standing drill, not a promise. (Derivable from Law 1 plus the authority matrix — kept for the checklist.)
19. **Reachable is forever; unreachable is policy.** Logical history is immutable; physical storage is governed.
20. **Prefer structural simplicity.** A modular monolith with visible boundaries beats premature distribution — and machinery is built when its first consumer exists.

---

# 36. Final architecture

```text
                              HUMAN / AGENTS
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │  HOSTS (Encounter)        │
                      │  reference app · LangGraph│
                      │  sessions · surfaces      │
                      └────────────┬─────────────┘
                                   │
                        commands · events · projections
                                   │
                                   ▼
                    ┌──────────────────────────────────┐
                    │         CONTEXT RUNTIME          │
                    │  sequencer · transitions · turns │
                    │  compiler (frames) · memory      │
                    │  merge · replay seam             │
                    └────┬──────────────┬──────────────┘
                         │              │
                     inference       effects
                         │              │
                         ▼              ▼
                    AI SDK Core   ┌───────────────────┐
                   (providers)    │      KERNEL       │  ← the only source
                         │        │ attestation       │     of authority —
                         └───────►│ capabilities      │     including model
                       egress law │ budgets · secrets │     egress
                                  └────────┬──────────┘
                                           │  the bracket, fenced
                                           ▼
                                    external world
                                           │
                                       receipts
                                           ▼
                    ┌──────────────────────────────────┐
                    │        CONTEXT STORE             │
                    │  PostgreSQL — one engine         │
                    │  canon: objects · nodes · refs   │
                    │         turns · effect facts     │
                    │  proj:  indexes · events · FTS   │
                    │  ops:   jobs · leases · attempts │
                    └──────────────┬───────────────────┘
                                   ▼
                            Blob store (CAS, erasure-namespaced)
                            Secret store (never in the tree)
```

At the center there is only one really unusual idea — sharpened once more:

```text
A persistent intelligence is a causal trajectory
through immutable continuation states.

Cognition is computation over a projection of a continuation frame —
a state, situated in a realm, under attested authority.
Action proposes; the runtime decides what becomes real;
the world is touched only between durable facts that say so,
and a live effect holds its place in history.
Branching materializes alternatives. Merging reconciles them.
Authority is attested, never authored.
```

Stated this way, the architecture is nearly deductive. The store is content-addressed because immutable, structurally shared states with ancestry are what trajectories are made of — Postgres happens to be where those states durably live. The compiler exists because cognition cannot consume the whole of being. Memory is canonical because it changes continuation; retrieval is derived because it changes only salience. Sessions are host-side because observing a trajectory is not the trajectory. Models only propose because stochastic computation must not hold mutation authority. Capabilities are attested because describing power is not possessing it. Effects are bracketed and fenced because the world does not participate in our transactions. Compaction creates states because forgetting-for-attention differs from destroying history. And evaluation becomes branching because an agent is a policy for generating trajectories, not answers.

That is the runtime I will build.
