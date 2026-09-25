# ADR-019 — History, Context, Authority, and mediated-runtime boundaries

- **Status:** constitution and public freeze accepted (2026-08-21), limited to the exact Phase 9
  machine-register scope. The Phase 0–8 artifacts and final Phase 9 candidate-bound pair are published.
  The independent Phase 0–2A architecture/security delta review
  (`specs/reviews/2026-08-15-phase-0-2a-delta-review.md`) found and closed 3 P0 / 9 P1. Ren signed off on
  2026-08-20; the authorized final architecture/security/migration review then verified the committed
  release and concluded with 0 P0 / 0 P1 on 2026-08-21
  (`specs/reviews/2026-08-21-phase-9-final-review.md`). The evidence registry, not this heading, defines
  the accepted/frozen surface; experimental and unproven dimensions remain explicitly unfrozen.
- **Date:** 2026-08-13

**Context.** The implemented v0.9 runtime has strong canonical identity, transaction, OCC, effect,
fencing, replay, erasure, and authority guarantees, but its public construction surfaces still couple
`PostgresStore`, the compiler, the Authority Kernel, Agent state, and host/framework adapters. The
independent v0.1 process-ontology proposal found a smaller vocabulary — immutable occurrence, lineage,
operator, and Ref — but made one LLM step the sole constructor, put a permission lattice into content,
made compile responsible for all contextual discovery, and reduced publication to object insertion plus
Ref CAS. Those choices cannot express the guarantees the implementation has since earned. We also need
two replaceability directions: History must work as a library in systems with no Agent model, and this
runtime must host decision loops from frameworks such as LangGraph, AI SDK, and ADK without giving those
frameworks Store, credentials, raw Authority, raw providers/executors, or canonical write handles.

This ADR originally recorded the proposed boundary before its completion. Phase 9 subsequently passed
the executable gates and completed governance for the exact registry-evidenced scope. The
[v0.9 plan](../plan.md) remains the operational baseline for material not superseded here, and accepted
ADRs plus frozen canonical bytes remain authoritative. The implemented target and execution record are
the reviewed [architecture plan](../history-kernel-mediated-runtime.md) and its
[execution companion](../history-core-execution-plan.md).

**Decision.** Adopt the following boundary within the exact scope supported by the Phase 9 evidence
registry. Any extension beyond that scope must pass its own staged evidence gates.

1. **History is an Agent-free protocol.** History Core owns schema-neutral content addresses/envelopes,
   immutable State, Transition evidence, causal Nodes, durable publication batches, Refs, Universe scope,
   traversal, availability, and retention mechanics. It may persist opaque upper-layer schemas but may
   not interpret them, authorize from them, or depend on their packages. `Invocation`, `Effect`,
   `CompilationRecord`, `AgentRecord`, and session/framework records remain extension-owned schemas.

2. **Store is an adapter, not the semantic contract.** The production Postgres implementation preserves
   the current transaction, fencing, OCC, lost-ack recovery, unresolved-effect guard, attribution,
   tenancy, erasure, and projection-rebuild semantics behind purpose-scoped History ports. A second
   implementation counts only if it passes the same protocol-faithful conformance suite. A bare
   `commit + CAS` facade is not a History implementation.

3. **Context is a continuation value, not the durable graph.** The target pipeline is
   `ContinuationRequest → ResolvedContinuation → MaterializedCandidates → ContextIR → RenderedInput`.
   Resolution and materialization may be effectful but must capture exact snapshot/result evidence.
   Candidate provenance and placement are assigned by runtime-owned admission, never self-attested by a
   source. Compiler and renderer are pure over exact, versioned inputs. Resolution ID, Materialization
   ID, Compilation Key, Render Key, and Conditioning ID cover distinct products and cannot substitute
   for one another.

4. **Authority and the external World are separate sovereigns.** Effective authority, credentials,
   grant/revocation state, and authoritative budget counters do not live in State, History, Context, or
   framework checkpoints. Context may cite a snapshot for explanation and planning, but every final
   model/effect/publication product is authorized again through a binding-scoped, attenuating Authority
   capability. Permits are exact-product, audience/realm/tenant/epoch bound and have explicit
   one-use/expiry/revocation/budget semantics.

5. **Decision actors are unprivileged by origin.** An internal Agent, third-party framework,
   deterministic workflow, or human-facing controller may own control flow and choose the next
   model/effect/proposal intent. It receives only scoped runtime capabilities. It never receives Store,
   credentials, raw Authority Kernel/provider, raw model provider, raw external-effect executor, or a
   canonical commit/publication handle. A common `DecisionDriver` is optional and remains provisional
   until distinct real consumers prove its shape.

6. **The runtime mediates all consequential boundaries.** External ingress becomes authenticated input
   evidence before it can cause continuation. Model and effect gateways bind exact final products,
   durably record attempts/intents before contact, distinguish partial/terminal/unknown outcomes, and
   retain refusal/paid-contact evidence even when no semantic State change follows. Canonical change
   starts as a proposal, passes exact admission, and publishes through the durable History batch
   protocol. Contact profiles share mediation laws but retain their distinct failure protocols.

7. **Integration coverage is generated from actual wiring.** Framework manifests declare independent
   control-flow, persistence, cognition, effect, authority, mediation, handoff, and isolation axes rather
   than one overloaded adoption level or `hosted | resident | peer` switch. Declared, observed, and
   enforced coverage remain distinct. API containment is not advertised as hostile-code containment;
   active bypass resistance requires address-space and, where claimed, egress isolation.

8. **Migration is additive and evidence-gated.** Existing canonical preimages and migration bytes never
   change. Legacy readers remain while reachable legacy evidence exists; new semantics use new
   families/versions. At most one canonical writer and one paid-contact path is active for a semantic
   fact. Shadow paths consume captured evidence and make no network/effect contact. Ports precede
   physical package splits; public interfaces and `ContextIR` obey the rule of two. Compatibility is
   allowed only to preserve released evidence, not to protect an unshipped abstraction from correction.

9. **Use unambiguous names.** `@context-runtime/kernel` remains the existing Authority Kernel package.
   New History work uses `HistoryCore`, `HistoryEngine`, and purpose-scoped History ports; it does not
   create another generic Kernel. Frozen fields such as `NodeRecord.kernel`,
   `ContinuationFrame.kernel`, and `InvocationRecord.agent` retain their bytes and legacy meaning until
   a new schema family exists. The normative vocabulary is [the Phase 0 terminology](../history-core/terminology.md).

10. **Seven constitutional laws.** These laws are accepted invariants within the exact registry-evidenced
    scope. Applying them to an unfrozen or experimental extension still requires that extension's own
    executable evidence:

    1. **Canonical becoming:** canonical History grows only by admitted occurrence; semantic State only
       by admitted transition; Ref only by authorized, fenced, recoverable publication.
    2. **Explanation closure:** within declared coverage, every canonical change, contact, observation,
       and refusal is navigable to its basis/root, inputs/proposal, implementation, and decision evidence.
    3. **Derived non-sovereignty:** Context, prompts, projections, indexes, caches, and operational state
       cannot become implicit semantic truth or an Authority source.
    4. **Accountable conditioning:** all observable/selected/fixable cognition inputs are frozen and
       referenceable; materialization may be effectful, while compilation/rendering are pure.
    5. **Authority non-amplification:** History content, placement, composition, fork, merge, delegation,
       and handoff cannot create power the Authority Provider did not grant.
    6. **Mediated contact:** ingress, model/effect egress, and canonical write/publication cross their
       boundaries only through exact authorization, protocol execution, and durable evidence.
    7. **Origin-independent mediation:** internal and external decision actors have no ambient bypass;
       replacing an actor does not change History, Authority, or Effect ontology.

   The current Twenty Laws are not silently repealed. Their claim-by-claim disposition is recorded in
   [the supersession map](../history-core/supersession.md). Encoding, concurrency, conflict, retention,
   and construction rules that do not remain constitutional still survive at their owning protocol or
   checklist layer.

**Alternatives considered.**

- **Adopt the v0.1 moment kernel literally.** Rejected as a target: “one LLM step = one moment” embeds an
  Agent/provider execution grain; a content-level authority integer can be forged; pure compile cannot
  honestly perform mutable retrieval; tombstone replacement and bare Ref CAS do not preserve current
  erasure, fencing, publication, and recovery guarantees. `MomentProfile` remains available as an
  extension protocol over History.
- **Keep `PostgresStore` as every subsystem's interface.** Rejected: persistence, authority, compilation,
  scheduling, and publication remain inseparable; History cannot be embedded safely and adapters obtain
  more capability than they need. The migration nevertheless reuses its correct transactions rather
  than rewriting SQL behind a weaker facade.
- **Put permissions and Agent states inside the History DAG.** Rejected: recorded descriptions cannot be
  live grants; revocation/budgets have their own time and linearization; Agent scheduling/control state is
  operational, while Agent semantic policy is ordinary versioned State within the authority envelope.
- **Make the runtime own every framework loop.** Rejected: it prevents resident frameworks and duplicates
  their control models. Runtime ownership is limited to contact, authority, admission, and publication;
  loop ownership is an explicit integration axis.
- **Let frameworks call providers/tools directly and observe them afterward.** Rejected: hooks and
  after-the-fact recording cannot stop post-authorization mutation, prove durability before contact,
  enforce revocation/budgets, or safely reconcile unknown outcomes.
- **Freeze a universal `DecisionDriver`, public `ContextIR`, and new package tree now.** Rejected under
  ADR-012's rule of two. First consumers may use private/versioned seams; the second real implementation
  supplies evidence for extraction and public freeze.
- **Big-bang rewrite or canonical dual-write.** Rejected: it risks frozen bytes and creates two sources
  of truth/contact. The staged plan uses dual readers, no-contact shadow computation, one active writer,
  and additive schema families.
- **Treat API containment as a security sandbox.** Rejected: imported hostile code can dynamically reach
  ambient services. Coverage must state whether it is API-contained, address-space-separated, or
  egress-contained and must prove the claimed tier adversarially.

**Consequences.**

- Phase 0 may establish vocabulary, provenance, address vectors, ownership ledgers, package-boundary
  manifests, and acceptance machinery without changing runtime output, SQL, canonical writers, or
  provider input.
- Phase 1 must prove a History-only supported surface with two protocol-faithful implementations before
  the abstraction counts. Phase 2A must prove exact Authority/permit/budget/attempt semantics before the
  proposed Laws or public write protocols can become constitutional candidates.
- No live provider input changes before the later compiler/contact activation phases; shadow resolution
  and compilation are no-contact and derived-only.
- Existing crash, race, replay, erasure, tenancy, Temporal/Postgres equivalence, and historical-reader
  gates remain cumulative. A new abstraction that weakens them is stopped, not merged with a promise to
  repair correctness later.
- A non-Agent adopter can eventually consume History contracts/adapter and supply its own admission
  semantics. A runtime adopter can eventually plug in a framework without changing History ontology or
  receiving ambient sovereign capabilities.
- More explicit identities and protocol records increase implementation surface. The cost buys precise
  replay, attribution, replacement, crash reconciliation, and honest coverage instead of implicit
  coupling.
- This ADR remains **proposed** at Phase 0 exit. Phase 0 completion and Ren sign-off permit Phase 1 to
  begin; they do not accept or freeze the Seven Laws.
