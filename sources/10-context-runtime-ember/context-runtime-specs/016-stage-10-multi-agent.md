# ADR-016 — Stage 10 multi-agent contract

- **Status:** proposed — implementation contract for Stage 10
- **Date:** 2026-08-10

**Context.** Stage 6 proved a narrow, in-process observed-footprint OCC path for two pure
transitions. Stage 10 is the first stage that needs that mechanism generally: durable agents spawn
from other agents, operate over one canonical universe with disjoint private context, exchange selected
knowledge, and may submit concurrently through more than one worker. The plan names AgentGraph,
private/shared scopes, fork policy, assimilation, generalized OCC, and the beginning of kernel process
extraction, but does not yet say what the durable facts are or where each security boundary lies. Without
those decisions, an agent id can become caller-supplied attribution, branch ancestry can accidentally
grant private reads, assimilation can become an unauthenticated copy, and a process-local queue can be
mistaken for cross-worker concurrency control.

**Decision.** Stage 10 adopts the following contract.

## 1. AgentGraph is canonical and append-only

`AgentRecord`, `SpawnEdge`, and `AuthorityAttenuation` are versioned domain schemas and canonical
evidence. `proj` may index parent/child closure, labels, status, and runnable agents, but deleting `proj`
and rebuilding it from canonical rows must recover the same graph. Agent ids are
runtime-minted ULIDs. An execution principal is derived as `agent:<AgentId>` and never accepted as a
command's assertion of identity.

The Stage 10 record is `agent-record/1`:

```ts
interface AgentRecord {
  format: "agent-record/1";
  id: AgentId;
  principal: Principal;       // exactly `agent:<id>`
  owner: Principal;           // attribution and administration, not execution authority
  label: string;
  status: "active" | "paused" | "completed" | "failed";
  ref: Ref;                   // `agents/<id>/work`
  initialNode: NodeId;
  privateScope: Selector;     // exactly `agents/<id>/**`
  sharedScopes: readonly Selector[];
  grantIds: readonly AuthorityGrantId[];
  authority: Digest;          // root authority, or the child's attenuation-record digest
  createdAt: Time;
}
```

Universe identity is the composite key in the canonical table and the universe-scoped `AgentStore`
handle, not a byte inside the portable record. Exporting the same canonical agent into a fresh universe
therefore preserves its record digest.

The creation record, including its Stage 10 status, is immutable; Stage 10 adds no status-mutation
protocol. Only records whose status is `active` are schedulable. Root-agent creation records the same
fields but has no synthetic parent edge.

The Stage 10 spawn edge is `agent-spawn-edge/1`:

```ts
interface SpawnEdge {
  format: "agent-spawn-edge/1";
  parent: AgentId;
  child: AgentId;
  sourceRef: Ref;
  sourceNode: NodeId;
  childRef: Ref;
  policy: ForkPolicy;
  parentGrantIds: readonly AuthorityGrantId[];
  childGrantIds: readonly AuthorityGrantId[];
  attenuation: Digest;        // canonical `authority-attenuation/1`
  requestedBy: Principal;
  createdAt: Time;
}
```

The edge records provenance, not authority. Every later command resolves the agent record in the target
universe, derives its principal, checks current status, and asks the kernel for current attestation.
Owning a human session or knowing an `AgentId` is not enough to act as that agent.

## 2. Private and shared paths are different namespaces

The path layout is fixed for Stage 10:

```text
agents/<id>/memory/claims/<claim-id>       private immutable claims
agents/<id>/assimilations/<proposal-id>    private assimilation provenance
agents/<id>/psyche/**                      private canonical Context System/profile data
agents/<id>/<other>/**                     other private agent work
<AgentRecord.sharedScopes>                 explicitly shared non-agent paths
```

The entire `agents/<id>/**` selector is private. A matching agent principal may read and write within
the narrower scope granted to it; another agent may not receive that private selector through spawn.
The owner/operator has a separate, audited administrative path, not implicit access through ownership.
`psyche/**` is readable by its agent's compiler but remains privileged-write state as required by
ADR-012: ordinary agent proposals and assimilation cannot change it. A path named
`agents/<id>/shared/**` is still private.

Shared is a capability designation, not one mandatory physical root. `AgentRecord.sharedScopes` contains
explicit selectors outside every `agents/<other>/**` private envelope (for example,
`workspace/research/**`, `memory/shared/**`, or `shared/**`). It is an upper bound, and both reducer and
compiler views are further intersected with current attested read/write selectors. Existing top-level
domain roots remain host-owned for backward compatibility; they become visible to an agent only when an
exact selector appears in both its shared scopes and current attestation.

An agent compilation profile is namespace-scoped by construction. Its effective state selectors are
its own `privateScope` plus an explicit subset of `sharedScopes`, intersected with current attested read
authority and the non-droppable kernel policy floor. Profile data may narrow this set but cannot widen
it. Candidate gathering receives only that `ScopedStateView`; a caller-supplied `admitted` flag is not an
authorization mechanism. The compilation record stores the agent, profile/Context-System digest,
effective selectors, selected sources, and the resulting `CompilationWitness.stateReads`. Consequently,
private-only agents have disjoint compiler dependencies, while agents that consult the same shared path
correctly invalidate one another when that path changes.

## 3. Spawn is one atomic attenuation transition

The only Stage 10 fork policy is the versioned `agent-fork-policy/1` value:

```ts
interface ForkPolicy {
  format: "agent-fork-policy/1";
  source: "parent-ref-head" | "pinned-node";
  privateState: "isolated";
  sharedState: "explicit-subset";
  authority: "attenuate";
}
```

`parent-ref-head` locks the named parent ref and selects its actual head. `pinned-node` requires a node
in the same universe that is reachable from the named parent ref; it does not turn a historical node
into a live binding. In both modes the child's home ref is
`agents/<child>/work`, initially points to `sourceNode`, and therefore resolves to simulation under §16.
`privateState: isolated` creates a new private selector; it does not copy or grant the parent's private
namespace even though the source state structurally contains it. `sharedState: explicit-subset` means
every child shared selector is contained by a parent shared selector. `authority: attenuate` means child
grant ids and every capability they resolve to — paths, blobs, tools, models, budget, effect grade,
expiry, and spawn permission — are no broader than the parent's current attestation.

Spawn persists three additional authority objects. `authority-attenuation/1` binds the exact parent and
child grant-id sets, private/shared envelopes, the caller's normalized read/write/tool/model/effect
request, the child materialization digest, the exact parent spawn-authorization digest, and the
self-certifying child attestation digest. The referenced
`agent-authority-materialization/1` stores sorted, principal-substituted grant descriptors including
proposal kinds, realms, expiry, read/write selectors, blob namespaces, tools, models, budget limits,
effect grade, and mandatory subject-routing selectors. The referenced attested authorization-decision
record proves the parent principal, universe, realm, `agent.spawn` kind, current authority epoch, exact
grant set, and effective selectors that admitted this spawn. The service derives that child materialization
from the parent's current `authority.attested-snapshot/v2`; a host resolver reconstructs a child kernel
from those canonical bytes after restart. Reusing a grant id with a wider descriptor or another
principal therefore changes the snapshot/materialization and fails closed.

Consumable model-budget counters are not copied into independently reconstructed child kernels. A child
request that selects a budgeted model bundle fails closed until a shared durable reservation allocator
can preserve one counter across parent and children; unbudgeted model bundles may be attenuated normally.
This is budget attenuation by refusal, not a reset of spent capacity.

The parent must separately preauthorize the `agent.spawn` operation. Because every child home ref is
non-live, derived child grants remove the `live` realm even when the parent can act on `live`; later
scheduling accepts only the child's home ref or the edge's recorded non-live source ref. Shared claim
writes are narrowed to `shared/claims/<child>/**`, and ordinary private writes are limited to work,
memory, and assimilation roots, never `psyche/**`.

The store exposes one interactive `spawnAuthorized` operation that, in one PostgreSQL transaction,
reads the immutable parent, locks the parent ref, then invokes the authority-preparation callback and
creates the child ref plus immutable `AgentRecord`, `SpawnEdge`, content-addressed
`AuthorityAttenuation`, referenced authority materialization, and exact authorization record. It also
emits a session-free `agent.spawned` durable fact through the generic transaction-bound Store event sink;
the fact binds the agent-record and edge digests and carries only an opaque host-global origin cause.
The host allocates recipients and its per-session sequence while that same transaction is open. A late
sink failure exposes the ref, every canonical object/index row, event, and host interaction, or none.
After those writes and the sink append, the Store invokes a service-only final revalidation as its last
pre-commit action. It must reassert the parent's exact v2 snapshot digest and the authorization epoch;
revocation or drift throws and rolls the whole transaction back. The callback is not a command or replay
field and cannot be supplied through the wire.
Raw spawn is internal replay/import only and may omit the host fact.

The service's nondeterminism seam mints the child id; a separate replay/test-only method admits an
explicit identity, and no product command may assert either the id or derived principal. A symbolic
`ownClaims` request is resolved only after minting to `shared/claims/<child>/**`, then the normalized
exact selector enters the attenuation record. Child runtime resolution consumes the stored
materialization only after the canonical spawn has committed, so there is no runnable pre-commit
authority window. Reload verifies the materialization, child attestation, exact parent spawn decision,
and full attenuation against the parent's canonical runtime before the child can schedule.

## 4. Assimilation is authenticated claim cherry-pick, not merge

Assimilation is a dedicated same-universe operation over one immutable claim. Its canonical record is
`agent-assimilation/1`:

```ts
interface AssimilationRecord {
  format: "agent-assimilation/1";
  id: ProposalId;
  source: {
    agent: AgentId; node: NodeId; path: Path; claim: ClaimId;
    claimDigest: Digest; contentDigest: Digest;
  };
  target: {
    agent: AgentId; ref: Ref; base: NodeId; path: Path; claim: ClaimId;
    claimDigest: Digest; contentDigest: Digest;
  };
  requestedBy: Principal;
  sourceAuthority: Digest;
  targetAuthority: Digest;
  at: Time;
}
```

The result transition references this record; the record cannot name a node created after its own
content digest, for the same reason an invocation has no `resultNodes` field (§19).

Before reducing the target transition, the runtime preauthorizes `agent.assimilate` under the target
agent, loads the exact source node through a view scoped by that target decision, proves that the source
agent authored the introducing transition and wrote the exact claim value at that node, parses it, and
binds the record to both its claim-value and content digests. Cross-agent transfer uses the attributed
`shared/claims/<source-agent>/<claim-id>` source path; a private source remains unreadable to the target.
It independently authorizes the target write to
`agents/<target>/memory/claims/<new-id>` and the provenance write to
`agents/<target>/assimilations/<proposal-id>`. The target claim reuses the immutable content but receives
target-local claim identity. Its source provenance is constructed by the runtime from the verified
source node; the request cannot author that hop or upgrade its authority label.

Assimilation does not add the source node as a parent, import claim lifecycle facts or contested status,
copy private bytes into compiler candidates, transfer approvals/capabilities/effects, merge arbitrary
state, or expand target authority. It cannot target `psyche/**`. Cross-universe assimilation remains
message passing and is not part of Stage 10.

The target authority snapshot and universe availability epoch are captured before source verification
and reasserted at engine admission and immediately before commit; the availability epoch is additionally
fenced inside the Store commit transaction. Every direct or nested `BlobRef` in the claim is checked
against the exact namespace/hash retention ledger and its physical CAS bytes between the epoch reads.
Revocation, redaction, expiry, missing bytes, or authority/availability movement is a typed refusal/race
rather than an assimilation of stale evidence.

## 5. General OCC validates both cognition and reduction

The Stage 6 in-process queue is replaced for the generalized path by store-backed admission on the ref
row. A transition is OCC-eligible only when it is deterministic, effect-free, single-parent, targeted at
one ref, all state access occurred through traced views, and its reducer explicitly declares
`generalizedOcc: true`. Merge reducers and the promotion, spawn, assimilation, approval-bearing,
effect-bearing, and multi-parent doors are ineligible and keep their stricter serialized paths. A
model-derived proposal may be eligible: its recorded invocation is immutable evidence and the provider
is never called again during re-admission.

Eligibility is not sufficient for linearization. Admission locks the target ref and validates:

1. the base is on the current head's first-parent history;
2. the host validator authenticates the witness against the compiled-context evidence and validates its
   current retrieval materialization and tool set, while the runtime validates authority, availability,
   and realm;
3. every compiler state selector/prefix membership in `CompilationWitness.stateReads`, every reducer
   exact read and prefix listing, and every precondition has the same observable result at the current
   head; and
4. the proposed writes do not overlap writes between the base and current head.

Intervening writes are the recorded `TransitionRecord.patch` facts along the first-parent path, not a
net state diff. A path written and then restored still conflicts with reducer reads, reducer writes, and
compiler selectors; missing or malformed history fails closed rather than proving disjointness.

If all checks pass, the runtime validates, pre-authorizes, reduces, authorizes the resulting patch, and
verifies again at the locked current head, then performs the fenced publication CAS. The new transition's
parent is the current head; its invocation still records the original `inputNode` and frame, and the
linearization record names the original base. A patch is never replayed blindly. If a state or witness
dependency overlaps, the original-base candidate is retained under deterministic
`exp/race/<ProposalId>` and the result is `branched`; stale external authority/availability or malformed
evidence is a typed refusal, not a branch. A CAS loss retries validation against the new head within a
bounded policy. Exhausting that policy preserves the original proposal as the same deterministic detached
race branch against the latest observed head; it does not leak a transient error or repeat provider work.
This transaction, rather than a JavaScript map or one worker's queue, is the authority across processes.

## 6. Kernel extraction begins with a fail-closed port

`AuthorityKernel` gains an asynchronous, versioned, fully serializable counterpart named
`AsyncAuthorityPort`. An in-process adapter preserves the current host, and a local child-process adapter
carries strict JSON-round-trippable `authority-port/v2` IPC messages with request id, request digest, method, parameters,
and a typed result; the caller enforces a bounded request timeout. The port covers the complete existing
`AuthorityKernel` surface (preauthorization, patch/model/effect authorization, model-budget
settlement/release, authority snapshot/digest, and grant-id attenuation for spawn). The child returns
decisions and digests, never credentials.

The two adapters run one conformance suite and must produce byte-identical decisions for the same
attestation state. Timeout, EOF/process death, malformed bytes, unknown operation/version, mismatched
or duplicate request id, or invalid response schema fails closed; the child-process adapter never falls
back to the in-process kernel. The server marks request ids seen before dispatch and quarantines its
connection on an in-flight duplicate or delayed replay, so a mutating call cannot execute twice. A death
after a request but before its response cannot authorize caller progress.
This is the beginning of extraction, not a completed hostile-code sandbox: provider/effect drivers and
the host can still share an address space in Stage 10. Moving credential-bearing dispatch into the
kernel process remains later hardening behind the same port.

`TransitionEngine` accepts either the legacy synchronous kernel or this port through the same injected
authority seam and awaits every preauthorization, patch/effect reassertion, witness snapshot, and
observation-time authorization call. Agent scheduling supplies the port, so process death cannot be
bypassed by a synchronous in-process engine path. The synchronous type remains only a source-compatible
adapter for older callers.

## 7. Conditional and deferred work stays deferred

Stage 10 introduces no second runtime bundle and no runtime self-modification. Therefore signed-bundle
verification and compiler sandboxing do not activate; ADR-009's trigger remains “when a second runtime
bundle can exist.” If implementation adds that capability, signing, signer-root verification outside
State, digest pinning, and sandbox acceptance become same-change gates rather than follow-up work.

Fusion remains named as “A and B become C” and is not implemented. Full-state copying as assimilation,
implicit private sharing through ancestry, authority union, autonomous semantic merging, a workflow
language, a kernel network service, microservices, distributed consensus, and cross-universe
transactions are also outside this stage.

**Alternatives considered.**

- Store agents only in session/product tables — rejected because scheduling, authority, replay, and
  provenance must survive loss of a host projection and cannot make the engine session-aware.
- Treat every agent branch as a private copy — rejected because ancestry is storage identity, not read
  authority; copying also destroys structural sharing without closing the leak.
- Put “shared” below each private agent root — rejected because a selector cannot then express the
  privacy boundary honestly. Shared selectors remain outside every agent-private envelope.
- Assimilate by merge or accept a caller-supplied `SourceRef` — rejected because both import more than
  one fact, and neither proves that the source node contained the named claim.
- Validate reducer reads but not compiler reads — rejected because a model can depend on shared state
  the reducer never reads; linearizing that proposal would silently rebase cognition.
- Retain only the in-process OCC queue — rejected because two app/worker processes can each believe
  they are first. The ref-row transaction is the cross-process serialization point.
- Extract the whole runtime into services — rejected as §34-premature. One local authority port makes
  the boundary executable without adding service discovery or distributed failure modes.

**Consequences.** Agent work stays private by construction, while deliberate collaboration remains
possible through explicit shared selectors and claim assimilation. Spawn and authority become one
auditable fact rather than adjacent best-effort writes. General OCC can keep namespace-disjoint agents
on one ref without accidental branches, but agents that compile from broad shared context will branch
more often by design. Model-derived re-admission requires separating invocation input provenance from
the eventual transition parent. Kernel APIs become asynchronous at their callers, and the child-process
adapter adds a hard fail-closed mode before it provides a complete OS privilege boundary.
