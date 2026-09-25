# ADR-017 — Temporal durable execution behind a serializable port

- **Status:** accepted
- **Date:** 2026-08-10

**Context.** Stage 4 deliberately put world contact behind `ExecutionDriver`, with
`LocalExecutionEngine` proving the effect bracket before adding a workflow system. The original
closure-valued `run(label, operation)` shape is sufficient inside one process but cannot cross a
Temporal boundary: closures, Store handles, and `EffectDriver` instances are not serializable. A
naive adapter would also introduce two correctness failures. An activity can wait in a queue until
after its lease fence expires, and committing a canonical intent before starting its workflow leaves
a crash gap. Temporal's default activity retries are unsafe for queryable and non-idempotent effects.
Stage 11 therefore needs a durable adapter without making Temporal history semantic, adding sessions
to the engine protocol, or weakening the Stage 4 executor-class contract.

**Decision.**

1. **The execution port carries versioned data, never closures.** `ExecutionDriver` accepts a
   serializable `ExecutionRequest` and returns a serializable driver observation. The request names
   its schema version, operation (`dispatch` or `reconcile`), stable execution id, universe, effect,
   turn, tool, executor class, fence, lease safety margin, and a semantic observation time. Before
   constructing the request, the caller asks the Store to bind one replay-seam time to the durable
   `(universe, effect, execution-id)` attempt. Exact retries reload that value without consuming the
   seam again. Multi-effect callers and the recovery outbox allocate once per effect in canonical
   intent order, never once per turn. The time is never taken from Temporal's operational clock. The
   request contains no Session id, Session
   binding, Store object, callback, or driver instance. A worker-side `ExecutionActivityRegistry`
   resolves the named tool to its `EffectDriver`. Local and Temporal drivers invoke the same registry.

   Recovery disposition is part of the immutable, versioned action evidence: `effect-action/v1`
   retains its original `absorb` meaning, while `effect-action/v2` carries an explicit
   `absorb | publish-or-branch` value. The canonical intent already binds that evidence by action
   digest, so the frozen `EffectFact` shape is unchanged. The execution request transports the
   derived value and the worker fails closed unless it matches the canonical action.

2. **Workflow granularity is one short workflow per canonical effect operation.** The execution id
   and Temporal workflow id are deterministic functions of
   `(protocol-version, universe-id, effect-id, operation, authorization-fence)`. The fence is the
   dispatch fence for first contact and the newly acquired recovery fence for reconciliation. This
   keeps retries within one authorization epoch while allowing a later, freshly fenced recovery to
   replace a terminally refused/failed workflow after its history is retained. Starts use
   reject-duplicate semantics. The complete validated request digest is stored in Temporal memo;
   “already started” is success only after that digest matches, otherwise execution fails closed.
   Canonical resolution is the
   permanent deduplication backstop after Temporal retention expires. Workflow ids never contain a
   Session, surface, user-interface event, or transport cursor.

3. **The canonical effect intent is the start outbox.** The transaction that records the intent does
   not also promise that a Temporal start succeeded. A scanner enumerates unresolved canonical intents
   and requests their deterministic workflows. It runs continuously and at worker startup. A crash
   after intent commit and before workflow start therefore leaves recoverable work, while concurrent
   scanners converge on one workflow. No Temporal-only queue row becomes the authority for whether an
   effect exists. The recurring scanner quarantines resolver, validation, and capacity failures by
   universe, so one poisoned route cannot stop healthy universes. Source-wide and Temporal-start
   failures produce credential-free degraded health and bounded jittered backoff; cancellation stops
   new starts and drains any start already in flight.

4. **The bracket maps to activities without moving semantic truth.** A workflow schedules worker
   activities to load the immutable intent/action evidence, execute the declared operation, and commit
   its observation. The world-contact activity records its operational attempt, then reloads the live
   ref lease and validates the exact fence and remaining safety margin immediately before calling the
   external driver. There is no intervening await after that validation and before world contact. A
   stale, missing, or near-expiry lease is a non-retryable refusal; queued work never touches the world
   on the strength of an old check. Completion atomically inserts or reuses the immutable observation
   and closes the matching attempt. Repeating an identical completion is success; a different
   observation for the same identity is a hard conflict. Fence loss after world contact can surface an
   orphaned semantic observation, as in Stage 4, but cannot authorize stale publication.

   The safety margin is the minimum ref-lease authorization that must remain at that adjacent check
   and the post-expiry buffer before recovery takeover; it is not a provider-call timeout. A recovery
   claim renews the ref lease for at least the configured margin plus acquisition headroom. After the
   check, an effect-wide worker claim is held and heartbeated through world contact and canonical
   observation, preventing a second worker from overlapping a long call even if the ref lease later
   expires. The live exclusion primitive is a dedicated, per-effect PostgreSQL session advisory lock;
   a worker-only operational row records its token, monotonically increasing generation, owning
   execution, backend pid, and heartbeat deadline. The deadline bounds frozen/crashed-session cleanup
   but is never used alone to authorize overlap. Claim acquisition fresh-reads canonical completion,
   and observation commit compares the current token and generation. Activity cancellation interrupts
   claim wait/heartbeat paths and stale claim owners cannot complete canonical work.
   Losing the database session cannot synchronously cancel an already-issued provider request, so
   crash takeover still follows the executor-class table below: only stable-key provider-idempotent
   dispatch is repeated, queryable/reversible effects reconcile first, and non-idempotent effects
   escalate rather than redispatch.

   Once every effect in the occupied turn has a canonical observation, recovery settles the whole
   turn under one homogeneous finalization policy derived from its immutable action evidence. `absorb`
   closes without publication; `publish-or-branch` either advances the original ref or creates the
   deterministic race branch. The ref change, exact recovery acknowledgement, attributed event, all
   matching Session envelopes, per-Session monotonic sequence allocations, and notifications commit
   in the same PostgreSQL transaction. The worker reaches that fan-out through a worker-only event
   sink; Session identity never enters `ExecutionRequest`, workflow ids, activities, or the engine
   protocol. The acknowledgement binds the recovery fence and exact published/branched result, so a
   lost reply returns the original result without publishing or fanning out twice.

5. **Retry policy is part of the executor class, not a Temporal default.** Workflow replay does not
   repeat activities already recorded complete. Activity retries are configured explicitly:

   | Executor class | Dispatch policy after an ambiguous attempt | Reconciliation policy |
   |---|---|---|
   | Provider-enforced idempotency | retry is allowed with the identical deterministic idempotency key, bounded by the valid lease | reconcile when available; duplicate provider receipts collapse at semantic completion |
   | Queryable | never blindly retry dispatch; the dispatch activity has one attempt | reconcile first; dispatch again only after a definitive “not applied” result and a fresh fence |
   | Non-idempotent, non-queryable | one dispatch attempt; record `unknown` and escalate | no automatic query or redispatch |
   | Reversible | never blindly retry ambiguous dispatch | reconcile first; if unknown, record escalation and the declared compensation guidance, never claim rollback or auto-compensate |

   Temporal timeouts, cancellation, worker death, and lost activity replies all count as ambiguity.
   Workflow or activity retry settings may be stricter than this table, never more permissive.

6. **Temporal history is operational; Context history is semantic.** Workflow starts, activity
   schedules, attempts, heartbeats, timers, backoff, worker build ids, and Temporal timestamps remain
   in Temporal and operational Store rows. They never enter `canon`, determine a Node/Effect id, or
   appear in a universe export. Context history continues to contain only the intent, immutable action
   and approval evidence, observation/outcome, and nodes that cite them. Temporal retention may delete
   operational history without deleting or changing Context history. Given the same tape and canonical
   inputs, Local and Temporal executions must produce byte-identical canonical exports, event rows,
   and semantic replay results; differing operational attempt histories are expected.

7. **Local remains explicit development/test infrastructure.** `LocalExecutionEngine` is retained for
   unit tests, deterministic tape tests, and local development. Production selects Temporal explicitly
   and fails closed if the client, namespace, or worker is unavailable; it never silently falls back to
   Local. The Temporal server and effect worker are separately supervised processes. The worker drains
   on shutdown, stops polling before its database connection closes, and resumes unresolved canonical
   intents on restart.

8. **The adapter targets one SDK line.** All `@temporalio/*` packages use the TypeScript SDK 1.22
   release line and resolve to one exact version in the lockfile. Client, workflow, activity, worker,
   and test packages do not drift independently. Workflow code imports only Temporal's deterministic
   workflow surface; Node, database, and provider APIs stay in activities.

**Alternatives considered.**

- **Keep the closure-valued port and wrap it in an activity.** Rejected because captured runtime state
  cannot be serialized or replayed and would make the “same driver” claim nominal rather than real.
- **One workflow per Session, thread, or turn.** Rejected because it leaks a reference-host concern into
  the session-free engine and couples independent effects to UI lifecycle and retention.
- **Start Temporal inside the intent transaction.** Rejected because PostgreSQL and Temporal do not
  share a transaction; either ordering leaves an unclosed crash gap. Deterministic starts from the
  canonical outbox make the gap recoverable.
- **Treat Temporal history as the effect ledger.** Rejected because retention and operational retries
  would then change Context meaning, break exports, and make Local and Temporal observably different.
- **Accept Temporal's default activity retries.** Rejected because at-least-once activity execution is
  stronger than most world APIs and would violate the Stage 4 recovery matrix.
- **Remove Local once Temporal lands.** Rejected because fast deterministic unit/tape testing remains
  valuable. The safe boundary is an explicit environment choice with no production fallback.

**Consequences.**

- The Stage 4 port changes once from a local closure seam to a serializable domain protocol, and its
  existing conformance suite must be extracted so Local and Temporal run the same assertions.
- Observation insertion and operational attempt completion need an atomic, retry-idempotent Store API.
- The canonical unresolved-intent scan remains necessary even when Temporal is healthy; it is the
  recovery mechanism for the post-commit workflow-start gap and for history retention.
- Production now operates a Temporal service/client and a separately supervised effect worker, with
  TLS/authentication, namespace, task queue, health, graceful shutdown, and retention to manage.
- Temporal can retry and reschedule only to the executor strength declared in immutable action
  evidence. It improves durability; it does not make a non-idempotent API idempotent.
- Migration 025 and claim-aware workers form one production cutover. Because a pre-claim worker cannot
  participate in the advisory-lock protocol, deployment order is: apply migrations, drain and prove
  absence of legacy execution workers, then start claim-aware workers. Mixed old/new workers are not
  claimed to provide single-flight behavior; worker readiness fails until the required schema is
  present.
- The engine, canonical schema, exports, tapes, Encounter sessions, and event protocol remain free of
  Temporal workflow concepts. Stage 11 is accepted only when the unchanged Stage 4 suite and explicit
  process-death/equivalence drills in `specs/acceptance/stage-11.md` pass.
