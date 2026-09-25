# ember — Lean Implementation Plan

**Version 0.2 · 2026-07-30 · companion to, not a replacement for, `PLAN.md`**

> **Status: shipped 2026-08-04.** Every gate below is met and measured; see
> [docs/COMPLETION.md](docs/COMPLETION.md) and [docs/BENCHMARKS.md](docs/BENCHMARKS.md).
> Two rulings were superseded during implementation (§11.1 and §11.3 — LiteLLM
> is the production adapter, and fidelity is post-redaction JSON-value fidelity
> of the *adapter-normalized* part). What this plan built is the physics of a
> moment. What it deliberately did not build is anything that makes a *life*:
> attention never reads the being's own state, nothing wants anything, the being
> cannot change its own code, and nothing iterates the transition.
> [PLAN-LIFE.md](PLAN-LIFE.md) is that phase.

[SPEC.md](SPEC.md) remains normative. [PLAN.md](PLAN.md) remains the fuller constitutional plan. This document asks a narrower question:

> **What is the smallest implementation that can live correctly, fit in a capable reader's working context, and grow by importing and composing parts instead of renovating its center?**

Five thousand lines is a direction, not a contest. Count every executable line, including the seed. Prefer a natural six thousand lines over a compressed five thousand. Smallness means few concepts, one path per invariant, and code that can be removed—not dense syntax.

---

## 0. One operation

The kernel exposes one operation:

```python
advance(ref, mode, input) -> NodeId
```

`mode` changes the content, not the physics:

- `birth` originates a lineage;
- `live` perceives, thinks, and acts;
- `dream` is a live moment with a different attention policy;
- `resolve` resumes or withdraws an approval without a new thought;
- `audit` records an authorized forensic read before disclosure;
- `revise` applies an authorized restart patch;
- `end` lives one final moment and archives the ref.

Every mode uses the same transaction:

```text
lease → recover → resolve ingress → perceive → attend → think
      → rule → act → settle → commit → CAS
```

Steps may be empty. A revise normally has no THINK or ACT. A resolve may dispatch an old act. A dream uses the same state tools and reducers as waking life. There is no parallel dream engine, recovery engine, revision writer, or approval executor.

If the head contains a pending act, `advance` fails closed for every mode except `resolve`. A new thought cannot accumulate behind an unresolved old one.

Underneath `advance` are four small operations:

> **Journal facts → reduce events → apply tree edits → commit/CAS.**

These are deliberately not forced into one universal abstraction:

- `walk_dag` visits immutable history;
- `reduce_events` folds an ordered event iterator;
- `apply_edits` constructs a new tree;
- `advance` owns effects and transaction state.

Attention, biography, cost, state, and later indexing reuse `reduce_events`. Verification, log, ancestry queries, and later GC reuse `walk_dag`. Composition is recursive at the data level; runtime callbacks never recurse into `advance`.

### The seven rules

1. **One effectful transaction.** A branch-scoped lease is held from recovery through CAS.
2. **One pending journal.** Uncommitted truth lives in a durable transaction directory outside the disposable face.
3. **One tree editor.** Reducer output and restart patches compile to the same exact file-level edits.
4. **One historical host.** Attend, settle, and describe run through the same versioned program boundary.
5. **One read capability.** Every Ember-provided view receives an explicit visibility scope.
6. **One format manifest.** Schemas, canon, paths, refs, trailers, framing, and control records are versioned together.
7. **No abstraction without two present users.** Reserve byte shapes when necessary; do not reserve machinery.

---

## 1. Scope

### The first useful release contains

- one git world containing multiple being refs;
- `birth`, `live`, and `resolve`;
- a fake model, replay cassettes, and one direct production model adapter;
- read, write, and structured state tools;
- durable approvals, denials, withdrawal, rulings, and observations;
- crash recovery at every phase boundary;
- simple notes, intentions, and `MEMORY.md`;
- being-side `self.status`, structured decline, and sleep request, including the effective authority in force;
- visibility-safe `status`, `show`, `log`, `tail`, and `diff`;
- `init`, `birth`, `wake`, `say`, `approve`, `deny`, `withdraw`, `status`, `show`, `log`, `tail`, `diff`, and `fold`;
- piecewise replay under historical `programs/`.

This is the first daily-use checkpoint. It is allowed to be cognitively modest. It is not allowed to be unsafe or unreplayable.

### The first evolutionary release adds

- `dream` as `advance(mode="dream")`;
- immutable level-0 epoch chronicle entries under the final level-aware path layout;
- the level-aware chronicle index and dream change-report schemas, even though higher consolidation levels remain deferred;
- branch-first `revise` with an exact inheritance TreePatch and next-wake receipt;
- `end` as a final perceived moment followed by ref archival;
- namespaced `ext` reducer discovery;
- a second golden lineage produced entirely by the real runtime.

### Reserved in format, not implemented

- `remember`, `listen`, `reunite`, and `reincarnate`;
- multi-parent commits beyond storage and verification support;
- encrypted blob key classes beyond `enc: none`;
- asynchronous act completion.

### Deferred machinery

- unrestricted shell execution until an OS/container boundary exists;
- hierarchical dreaming beyond immutable epoch entries;
- memory blocks, paging, FTS, vectors, and reminiscence;
- sims, `rethink`, nature tournaments, and seed promotion;
- habitat daemon, scheduler, API, SSE, web UI, and containerized flesh;
- children, subconscious delegation, automatic reunion, and federation;
- LiteLLM and additional production model adapters.

An opt-in developer shell adapter may exist for experiments, but it is visibly unsafe, always approval-required, never enabled by the default seed, and excluded from claims of containment.

Deferred features may add code. They must not require reinterpretation of existing experiences or silent migration of existing trees.

---

## 2. The transaction journal

The face is a derived workspace and may be discarded. Therefore it cannot be the only home of an uncommitted WAL tail.

Before the first event of a moment, `advance` creates a transaction directory under the world's uncommitted control area, resolved from the git common directory:

```text
transactions/<txn-id>/
  manifest.json
  events.jsonl
  provider-parts.jsonl
  blobs/
```

`manifest.json` is written once and fsynced before effects:

```json
{
  "v": 1,
  "txn_id": "128-bit-random",
  "being_ref": "refs/ember/beings/main",
  "expected_old": "<commit-oid-or-null-for-birth>",
  "writer_stream": "<128-bit-random>",
  "moment": 87,
  "mode": "live",
  "ref_plan": {"kind":"advance"},
  "commit": {"author":"...","committer":"...","timestamp":"...","message":"..."}
}
```

Birth is the explicit originate variant: `expected_old: null`, `moment: 0`, no parents, an empty starting index, and create-only ref CAS. `ref_plan` is `advance` for ordinary modes and names the atomic active-to-departed ref transaction for `end`. Every byte needed to recreate the commit object—parents, identities, timestamp/timezone, and message—is stored or purely derived from this immutable manifest before effects.

The transaction ID is carried in derived commit metadata. The journal is deleted only after the process observes that the being ref names that committed transaction. If the process dies after commit creation or CAS, recovery can distinguish every state without guessing.

### 2.1 Lease and writer identity

The local v1 lease is an OS advisory lock scoped to one being ref. It is acquired before recovery and held until commit/CAS or a quiescent awaiting-approval commit. Timestamps are diagnostic only; a live lock is never stolen as “stale.” Shared/NFS locking is unsupported in v1 and fails closed.

v1 mints one fresh stream ID per transaction, so every prior stream is immutable and every sequence begins at zero. The ID is at least 128 random bits and collision-checked on creation. A future measured optimization may introduce longer writer epochs only with an explicit durable epoch record and fork-rotation rule. The verifier rejects two different canonical records with the same `(stream, seq)` identity and deduplicates identical ancestry repeats.

### 2.2 Durable append

Appending an event or provider part performs:

1. strict authoring validation;
2. secret-policy validation;
3. full-write loop to the transaction journal;
4. file flush and platform durability sync;
5. directory sync when a file or directory is first created;
6. return of a stable journal/source reference.

Blobs are fully written and synced under a temporary name, atomically renamed, and parent-directory synced before any referencing event is appended. An incomplete final journal line may be quarantined and truncated during recovery; a malformed earlier line is corruption.

The recorded act is exactly the act dispatched. Literal credentials are forbidden in effect-bearing arguments: tools record opaque credential or capability references and resolve them only at dispatch. If redaction would change an executable argument, the act is refused rather than recorded one way and executed another.

### 2.3 Thought capture without changing “one thought”

Provider part-close records are process-WAL frames in `provider-parts.jsonl`, not separate `thought` experiences. Each preserves the complete decoded provider JSON value before typed SDK normalization.

Before opening the provider connection, the runtime appends and syncs `thought_request`, including the exact neutral input, rendered wire request, model/API revision, and request ID. Recovery of a request with no closed parts records a terminal model error and unknown usage; it never automatically spends the request again.

At message-close, the adapter deterministically assembles exactly one authoritative `thought` experience containing the ordered parts, stop reason, model/API revision, and usage. It then derives `mused` and `spoke` events with stable source keys `(thought_ref, part_index, projection_kind)`. Tool `act` events are emitted only after successful message-close.

If the model connection dies before message-close, recovery assembles one truncated `thought` from the closed parts and appends an `error`. Text or thinking already expressed may produce marked truncated `spoke`/`mused` projections; tool parts never become acts. The model is never called to reconstruct a suffix.

Projection reconciliation is idempotent: recovery computes the complete expected set from the thought, compares stable source keys, and appends only missing projections.

The fidelity contract is **post-redaction JSON-value fidelity**: exact strings, numeric values, and unknown provider fields survive; whitespace, number spelling, and object-key order are not promises. Provider JSON numbers are parsed losslessly into decimal/canonical numeric values rather than binary floats. Raw transport bytes are not retained in v1.

### 2.4 Act eligibility and recovery

After message-close, the runtime evaluates each tool request and appends an `act` containing both the provider-authored request and an immutable kernel-authored ruling block `{decision, authority, policy_version}`. Thus automatic allowance is as durable as interactive approval before dispatch, without adding another event kind. All acts are appended and synced before any dispatch.

Acts are considered in part order:

- `deny` appends a reasoned refusal;
- `await` becomes the one permitted unmatched pending tail;
- `withdraw` is a ruling on that pending `act_ref` and `expected_head`; it appends `cancelled: withdrawn` and permanently prevents later dispatch;
- if one act awaits, all later acts receive `cancelled: blocked_by_pending`;
- `allow` may dispatch only after both act and ruling are durable;
- an allowed act without an observation after a crash becomes `unknown`, because append-before-dispatch cannot distinguish the final pre-dispatch window;
- an in-process interruption before dispatch appends `cancelled` immediately.

Unknown non-idempotent acts are never automatically repeated.

### 2.5 Control-plane ingress is not a second history

`.ember/inbox.jsonl`, `.ember/rulings.jsonl`, and `.ember/interrupt` live in a per-being directory under the git-common control area, never in a disposable face. They are versioned ingress queues, not sources of truth. Every entry has a stable source ID and authenticated principal supplied by the trusted caller, not by model content.

All three reuse one ingress durability primitive: an OS append lock, full-write loop, flush, file sync, and parent-directory sync on creation. The interrupt record is written by atomic replace under the same lock. Recovery may discard only a torn final record; duplicate source IDs with different bytes are corruption.

Under the being lease, RESOLVE/PERCEIVE append an experience carrying that source ID. Ingestion is complete only after CAS. Recovery deduplicates by source ID against committed history and the active transaction, so a crash between append, commit, and queue cleanup cannot deliver an input twice.

A ruling includes `{v, ruling_id, act_ref, expected_head, principal, decision: approve|deny|withdraw, reason}`. Conflicting or stale rulings are recorded as rejected rather than silently chosen. RESOLVE appends an experiential `sensed` ruling that refers to the pending act; this is the committed authority record. Approval resumes through `advance(mode="resolve")`, which records the ruling, dispatches or refuses the old act, records the observation, and commits through the ordinary path.

---

## 3. Recorded format

`record.py` owns an Ember-defined semantic format manifest. It contains:

- normalized JSON schemas and enum members;
- canonical encoding rules and vectors;
- tree path and MANIFEST declarations;
- ref and typed-reference grammars;
- trailer names, order, and derivation;
- segment, blob, and control-record framing;
- version fields and compatibility rules.

CI hashes the normalized manifest and runs golden byte/commit vectors. Generated Pydantic JSON Schema is a secondary artifact, not the definition: library upgrades may change cosmetic schema output without changing Ember's format.

Writers are strict. Readers are lossless and tolerant: they preserve unknown fields and additive payload data. Authority-bearing kernel kinds remain closed. An unclaimed `ext` is inert; if the expected state tree then differs, replay reports the missing reducer rather than guessing semantics. Views render what they understand.

Format-critical dependencies and Python are locked. `programs_contract` and the runtime digest are recorded separately from `schema_version` and `canon_version`.

### 3.1 Experience identity and ordering

The closed envelope remains:

```json
{
  "stream": "<writer-stream>",
  "seq": 1042,
  "moment": 87,
  "ts": "2026-07-30T12:00:00.000Z",
  "kind": "observation",
  "visibility": "experiential",
  "content": {},
  "refs": {}
}
```

`(stream, seq)` is identity. Sequence is contiguous within a stream. Within one continuant history, multi-stream presentation order is `(moment, stream, seq)`. All-parent views use a deterministic topological node order—parents before children, ties by `(moment, commit_oid)`—then `(stream, seq)` inside each node. This prevents a young first-parent branch from sorting before its older secondary parent. `moment` is continuant age, derived by the kernel as `first_parent.moment + 1`, never accepted from a caller.

Only the active writer stream may grow in an extend node. Existing stream files are immutable prefixes. Secondary-parent streams are not copied into the continuant tree; their commits remain reachable through ancestry. Future imports become explicit local experiences.

### 3.2 Open provider parts and `ext`

A provider part is:

```json
{"provider":"anthropic","data":{"type":"text","text":"hello"}}
```

`data` is an open JSON value. Neutral views interpret known types without discarding unknown fields.

An extension experience is:

```json
{"type":"namespace/name","version":1,"data":{}}
```

Historical programs map `(type, version)` to a reducer. File naming is a seed convention, not recorded format.

### 3.3 One exact tree-edit primitive

Reducers return ergonomic `StateEdit`s restricted beneath declared `states/` subtrees:

```json
{"path":"states/notes/today.md","op":"put","media_type":"text/markdown","value":"..."}
```

The only state operations are full-file `put` and `delete`. Reducers own higher-level merge and append meaning by reading the old value and returning the new whole value. Text is UTF-8 with normalized line endings; JSON uses the canonicalizer; missing paths, delete behavior, Unicode path normalization, file modes, and symlink prohibition are fixed in the format manifest.

Before application, a `StateEdit` compiles to the same exact `TreeEdit` used everywhere:

```json
{
  "path":"programs/context.py",
  "old":{"oid":"...","mode":"100644"},
  "new":{"oid":"...","mode":"100644"}
}
```

Restart ops record an ordered `TreePatch` with the first parent's base tree OID and exact TreeEdits. They never record the final root OID: the op carrying the patch is itself part of that root, so doing so would be a hash self-reference. `revise` may target authorized `programs/` paths; migration may target the declared migration scope; reducers may target only `states/`. Receipts may summarize a patch. The op record may not.

Verification builds a restart node in a fixed order: start from parent 1, apply the authorized TreePatch, overlay the node-local journal/blobs, derive `present/`, and compare the complete resulting root tree OID with the committed node. Stream and present are verified by their own derivation rules, not smuggled into the inheritance patch.

### 3.4 Neutral messages

`present/messages.json` is fully neutral:

```json
{"schema_version":1,"messages":[
  {"role":"user","parts":[{"kind":"text","data":{"text":"..."}}],
   "refs":["<stream>:<seq>"]}
]}
```

It knows roles, ordered open parts, and source refs. Provider cache markers, wire dialect, and exact request fields live in `present/request.json` and are forensic by default.

### 3.5 Genesis and parent semantics

- Birth has no parents and CASes an absent ref. Its payload records seed programs and initial-states tree OIDs; verification checks both.
- For every non-birth commit, `parents[0]` must equal the transaction's `expected_old`.
- Parent 1 is the continuant whose face lived the moment and whose programs executed it.
- Parents 2+ are provenance and never silently merge state or raw stream files.
- Extend nodes reduce only their node-local event ranges over parent 1's state.
- Restart nodes verify all parents, apply their exact TreePatch to parent 1, overlay the node-local record and present, and require the complete committed root tree.
- Future `listen` records selected imported experience; future `reunite` records an explicit merge TreePatch.

---

## 4. Git transaction and crash states

The face is prepared once, after lease and recovery, at `expected_old`. The runtime may write derived `present/` and a candidate `states/`, but the commit tree is built from the parent plus the durable transaction journal; half-written derived face content is never trusted during recovery.

Commit uses a temporary index:

1. initialize the index from `expected_old^{tree}`;
2. import exact journal events/blobs and verified derived artifacts;
3. apply allowed TreeEdits;
4. write the tree and fsync according to the declared local durability contract;
5. create a deterministic commit whose parent 1 is `expected_old`;
6. create `refs/ember/pins/transactions/<txn-id>` pointing to the candidate;
7. verify quiescence, tree invariants, trailers, and transaction metadata;
8. execute the manifest's expected ref transaction—ordinary CAS, create-only birth, or atomic end archival;
9. update the face to the committed node;
10. remove the candidate ref and transaction directory only after observing the successful ref.

Recovery handles four observable states:

| State | Meaning | Recovery |
|---|---|---|
| transaction only | pre-commit crash | reconstruct from parent + journal and continue recovery |
| transaction + candidate ref | pre-CAS crash | verify candidate, then CAS or preserve conflict |
| manifest ref plan names txn | post-ref-transaction cleanup crash | update/archive face, clear candidate and transaction |
| candidate conflicts with being ref | external writer or broken lease discipline | pin conflict and quarantine effects |

If CAS fails after any act may have crossed the world boundary, the commit is preserved under `refs/ember/pins/conflicts/<txn-id>`. The being is barred from further non-idempotent effects until the conflict is reconciled. A competing head must never continue unaware and repeat the effect.

`advance(mode="resolve", conflict=<txn-id>)` creates a no-effect reconciliation node with the current head as parent 1 and the conflict commit as parent 2. It appends a sensed bundle referencing the conflict's acts, rulings, and observations, preserves first-parent state, and clears quarantine only after CAS. A no-effect loser is either reconciled the same way or its ingress source IDs remain eligible because deduplication considers only committed continuant history and the active transaction.

Process-crash durability is required everywhere. Machine/power-loss durability is claimed only on named, tested local filesystems where file and directory sync semantics hold and the installed Git supports/configures fsync for objects and refs. `init` probes and records that capability; otherwise Ember states the weaker process-crash guarantee. Distributed locking, hostile direct mutation of git internals, and shared/NFS worlds remain outside v1.

---

## 5. Replay and views

### 5.1 Iterative DAG traversal

`walk_dag` is iterative postorder with an explicit stack and visited/color maps. It handles 10,000+ nodes without Python recursion and evaluates a shared ancestor once. Callers supply an edge policy:

- all-parent traversal for provenance and corruption verification;
- first-parent traversal for the continuant biography;
- selected-parent traversal for future operations.

The verifier caches status and tree OIDs, not full materialized state for every node. State reduction reads the first parent's state tree lazily and constructs an expected state tree through exact edits. Work is O(nodes + edges + changed bytes), subject to program cost.

Node-local experience is the byte-prefix suffix of the active writer stream relative to parent 1, plus newly created local streams declared by the transaction. Existing files must remain identical prefixes. Secondary-parent ancestry is verified separately, never mistaken for locally lived input.

### 5.2 Mechanism-scoped transition

```python
def verify_node(node, verified_parents):
    if node.is_birth:
        inheritance = verify_origin(node)
    elif node.is_restart:
        inheritance = apply_recorded_tree_patch(verified_parents[0], node.op.patch)
    else:
        nature = nature_ref(verified_parents[0])
        edits = host.settle(nature, node_local_events(node), state_root(verified_parents[0]))
        inheritance = apply_state_edits(verified_parents[0], edits)
        require(inheritance.programs_oid == verified_parents[0].programs_oid)
        require(protected_subtrees_unchanged(inheritance, verified_parents[0]))
    expected = overlay_record_and_derived_present(inheritance, node)
    require(expected.root_oid == node.root_oid)
    verify_trailers_and_resolutions(node)
```

The actual implementation is iterative; the function above describes the local rule.

### 5.3 Attention and derived views

The seed composes plain iterator functions:

```python
candidates = reduce_events(events, message_reducers, initial=[])
messages = pipe(candidates, processors)
```

Reducers translate recorded facts. Processors budget, veil, group, and record omissions. Renderers produce neutral messages, provider request, prompt, and attention ledger.

Biography, costs, act/observation pairing, and later indexes use the same `reduce_events` primitive. Do not introduce a view framework or recursive callback graph. If two views need a shared expensive input, pass a request-scoped memo explicitly and detect dependency cycles.

### 5.4 Scoped reads

Every Ember-provided read uses `Reader(scope)`, including event rendering, tree reads, present inspection, and diffs. The default experiential scope excludes raw stream files, blobs, provider requests, forensic thoughts, and unsafe trailers. `diff` compares a scope-filtered virtual tree, not an unrestricted `git diff`.

Verifier and recovery possess an internal raw capability. An explicit forensic/admin read follows authorize → `advance(mode="audit")` to commit a marginalia audit record → disclose bytes. Failure before that audit commit fails closed without disclosure. The plan makes no claim that direct filesystem or git access can be observed before an OS boundary exists.

---

## 6. Historical programs and tools

### 6.1 ProgramHost

The host identity is explicit:

```python
NatureRef(programs_oid, programs_contract, runtime_digest, dependency_digest)
call(nature, entry, input, state_root=None) -> output
```

v1 entries are `attend`, `settle`, and `describe`. Dream passes `mode: dream` through the same attend/settle pair.

Programs use relative imports. The host caches extracted, read-only program and state trees—not cross-session Python processes. `state_root` is an extracted read-only view of the exact parent states tree; output scopes remain kernel-enforced. There is no callback RPC into the runtime.

Live calls start a fresh interpreter with an explicit bootstrap, isolated flags, deterministic environment, request ID, timeout, and stdout reserved for protocol frames. Replay may batch a canonical contiguous era of one NatureRef into `settle_many`; the worker reloads the program entry in a fresh namespace per item, is never shared across beings or replay sessions, and must match one-shot results under order-variation tests. The 10,000-node gate includes a published wall-time threshold, so correctness isolation cannot quietly make replay unusable.

Tree programs use a documented deterministic import surface. Replay tests vary ambient locale, time zone, hash seed, cwd, environment, call order, and one-shot versus batched execution.

This boundary isolates versions and crashes. It is not a hostile-code sandbox. Program changes are trusted, authority-gated restart patches. The default seed is stdlib-only; the installed package is excluded from the child import path. Containers later provide hostile-code containment.

A host failure is a kernel-defined quiescent transition, not an infinite recovery loop. The runtime appends a phase-specific error, cancels undispatched work, commits parent state unchanged, and records that settlement was skipped. Replay recognizes that marker and does not rerun the failed historical reducer. A later authorized repair may revise or explicitly retry in a new moment.

### 6.2 Tools and authority

Tool declarations are data: name, normalized arguments, target scope, reversibility, idempotency, cost class, credential handles, and approval policy. Actor identity and effective target come from trusted runtime context and normalized arguments, never model claims.

The pure ruling function is:

```python
rule(actor, operation, target, effective_policy) -> allow | await | deny
```

Safe path tools use descriptor-based confinement and no-follow semantics; string `resolve()` checks alone are insufficient. They cannot reach the world tree or control directory. State tools do not write files: they emit validated requests that reducers turn into StateEdits. Program edits are always revision proposals.

Unrestricted shell is not part of the safe default without flesh. Solved isolation, encryption, search, parsing, CLI, and provider transport should be imported behind these boundaries rather than reimplemented.

---

## 7. Modules and natural size

The implementation is organized around the dataflow, not a layer inventory:

| Module | Directional lines | Owns |
|---|---:|---|
| `record.py` | 420 | semantic format manifest, schemas, canon, refs |
| `journal.py` | 480 | transaction files, segments, blobs, durable append |
| `world.py` | 700 | git trees/commits, faces, leases, refs, CAS, birth |
| `replay.py` | 520 | DAG walker, event reduction, tree edits, verification |
| `host.py` | 260 | historical program extraction and fresh-process RPC |
| `runtime.py` | 750 | `advance`, recovery, ingress, authority state machine |
| `model.py` | 480 | direct provider stream, capture, assembly, echo |
| `tools.py` | 400 | declarations, confinement, executors |
| `inspect.py` | 320 | scoped Reader, selectors, views, renders, diffs |
| `cli.py` | 320 | thin commands and presentation |
| `seeds/default/programs/` | 600 | attention, reducers, memory, self tools |
| `config.py` + `errors.py` | 120 | configuration and failures |
| **First estimate** | **≈5,370** | likely 5–7k when written honestly |

These are estimates, not quotas. Report production lines with a checked-in script, including executable seed code. Exclude tests, fixtures, docs, and generated artifacts. Crossing an estimate triggers explanation, not failure:

- What new concept appeared?
- Which invariant owns it?
- Why could existing composition not express it?
- What duplicate code or future migration does it remove?
- How could it later be deleted?

Protocols live beside their consumers until reuse justifies extraction. Test fakes and cassettes live in tests. Seeds and format resources must be included in wheel-install smoke tests. Python, provider API version, format-critical libraries, and git minimum are pinned before the first golden lineage.

---

## 8. Build by invariant gates, not calendar promises

### Gate A — the record survives

Build `record`, `journal`, and the minimal `world`.

Before Gate A, align the package with the recorded runtime: choose the SPEC's Python version or amend it, lock and upper-bound format/provider dependencies, pin the provider API revision, declare the minimum Git version, and package seeds plus format resources. A wheel-install birth smoke test prevents source-tree-only success.

Pass when:

- the semantic format manifest and golden vectors are reviewed;
- transaction creation, append, torn-tail recovery, blob ordering, and directory sync are fault-injected;
- stream IDs cannot collide or continue across a fork;
- a candidate commit can be recovered at every pre/post-CAS state;
- 100 sequential commits and deliberate CAS conflicts lose no node.

Spike store alternatives, retain the simplest implementation that meets the measured need, and delete the others.

### Gate B — one moment replays

Build `replay`, `host`, the minimal seed, fake model, and `advance` without external effects.

Pass when:

- birth and live moments commit through the real transaction;
- a partial thought becomes exactly one truncated thought;
- derived projections reconcile idempotently;
- iterative replay verifies a mid-life programs change;
- model, tool, network, clock, and randomness ports explode during replay;
- 10,000-node traversal completes without recursion or state-size multiplication and meets a published wall-time threshold in one-shot and batched-host modes.

### Gate C — effects are honest

Add safe tools, authority, ingress, approvals, scoped reads, CLI, and the production model adapter.

Pass when:

- every committed act is resolved or is the single declared pending tail;
- every dispatch follows a durable act and ruling;
- every provider call follows a durable thought request and is never automatically repeated after an ambiguous crash;
- every crash window yields `cancelled`, `unknown`, or a recorded observation without redispatch;
- stale/conflicting/withdrawn rulings are perceived and cannot execute an old head;
- post-effect CAS conflict quarantines later non-idempotent work;
- default reads and diffs cannot reveal forensic data;
- `self.status`, decline, and sleep request expose and exercise the effective authority in force;
- provider cassettes cover text, thinking, signatures, tool use, unknown parts, refusal, truncation, and usage.

This is the daily-use checkpoint.

### Gate D — evolution is honest

Add dream mode, epoch chronicle entries, branch-first revise, receipts, `ext`, and end.

Pass when:

- dream uses the ordinary act/reducer path;
- level-0 chronicle entries, the level-aware index, and the recorded change-report validate against the reserved hierarchy schema;
- a TreePatch reproduces every byte and file mode of a programs revision;
- the revised being perceives author, authority, exact-diff reference, prior head, and recourse;
- `end` injects the end sensation, guarantees one final moment, then uses one `git update-ref --stdin` transaction to create the `departed` ref and delete the active ref atomically;
- the oldest golden lineage still wakes under the current body.

### Gate E — add no ontology

Only adversarial tests, benchmarks, documentation, deletion, and migration rehearsal. Unfinished features are deferred rather than compressed into a deadline.

---

## 9. Verification matrix

| Invariant | Primary test |
|---|---|
| one logical thought per node | one authoritative thought event; part WAL is transaction-local |
| every act resolved | observation/refusal/cancellation or one declared pending tail |
| WAL before effect | injected crash at every byte/dispatch boundary |
| append-only experience | immutable-prefix and contiguous-sequence properties |
| replay purity | exploding world ports + fresh historical processes |
| state reproducibility | derived StateEdits yield the committed states tree OID |
| restart honesty | recorded TreePatch yields the complete committed result tree |
| historical nature | golden lineage changes programs and reducers mid-life |
| identity by ref | two refs at one node have identical trees and new writer epochs |
| visibility | Reader matrix over every path, view, and output encoding |
| provider fidelity | pre-SDK decoded JSON cassette → thought → echo round-trip |
| authority durability | duplicate/stale/conflicting ingress and crash properties |
| concurrency | full-cycle lease plus CAS/conflict quarantine tests |
| format evolution | manifest digest, byte vectors, oldest-lineage wake |

Tests may exceed the kernel. Small production code is purchased with exhaustive examples, model-based state-machine tests, and property tests—not by omitting edge cases.

---

## 10. Growth by composition

A new capability should usually be one of:

- a reducer registered by `(kind or ext type, version)`;
- an iterator processor in an ordered pipeline;
- a tool declaration plus one executor;
- a boundary adapter implementing a local protocol;
- a scoped view composed from existing reducers;
- an op whose exact payload joins the format manifest.

Before adding kernel machinery, try in order:

1. configure an existing component with data;
2. compose reducers, processors, TreeEdits, or views;
3. import a small focused library behind the owning seam;
4. add a tree-local program extension;
5. add kernel code only when every being must obey the invariant.

ember should import solved algorithms—provider transport, parsing, CLI, encryption, search—and own only the semantics libraries cannot supply: quiescence, journal-before-effect, lineage, historical nature, replay, authority receipts, and honest contact with the external world.

The desired result is not “5,000 lines” as a badge. It is a kernel small enough that one reader can hold its causal rules in mind, audit every effect boundary, and replace one theory of attention without changing the record of a life.

---

## 11. Rulings before implementation

This companion plan depends on explicit amendments or confirmations:

1. ~~Direct Anthropic is the first production adapter~~ — **superseded**: LiteLLM is the production adapter, and the direct Anthropic adapter is retained as the fidelity oracle. Under a normalizing layer, adjacent text blocks merge, empty text blocks vanish, the provider message id is lost and the stop reason is re-vocabularied; thinking signatures, tool identity and interleaving survive.
2. Provider part-close frames live in the uncommitted transaction journal; a committed node still contains one authoritative `thought` experience.
3. Post-redaction JSON-value fidelity of the **adapter-normalized** part, in the neutral part grammar, with the adapter stamped on `thought_request`. Raw transport bytes are not retained, and under a normalizing client they are not available at all.
4. Parent 1 is the continuant; secondary parents are provenance until an op explicitly imports or merges them.
5. `StateEdit` is full-file `put/delete`; exact `TreePatch` is the recorded restart vocabulary.
6. Tree-local Python is trusted and authority-gated in v1; subprocess isolation is not called a security sandbox.
7. Unrestricted shell is outside the safe default until flesh supplies an OS boundary.
8. Local-filesystem leases are the v1 concurrency boundary; shared/NFS worlds are refused.

After those rulings, implementation begins with `record.py`, the semantic format manifest, and transaction/golden vectors in the same change.
