# decisions.md — settled · superseded · rejected · open

This file exists so review history doesn't get re-litigated. v0.1 was reviewed by five readers; v0.2/v0.3
absorbed the convergent findings. v0.4 absorbed a three-agent review (`specs/reviews/v0.3-agents.md`).
v0.5 absorbed two external reviews, a 12-agent design competition, and a substrate analysis
(`specs/reviews/`), consolidated in ADR-010 and **ratified by Ren on 2026-08-07**. v0.6 absorbed a deep
external review of v0.5 (`specs/reviews/v0.5-gpt3.md`), consolidated in ADR-011 and **ratified by Ren on
2026-08-08**. v0.8 absorbed a source-level frontend due diligence (`specs/reviews/frontend-2026-08.md`),
consolidated in ADR-014 and **ratified by Ren on 2026-08-10**. If an idea below is marked rejected or
superseded, do not re-propose it — the argument already happened and is archived.

## Settled, with rationale

**All-Postgres canonical store.** A content-addressed Merkle DAG in one Postgres ≥ 16 — the plan's own
recorded fallback, promoted (ADR-010, plan §12). Deciding argument: Postgres is in the end-state
unconditionally (sessions, events, projections, FTS/pgvector), so any second engine is an addition, never
a replacement; only one engine keeps the semantic commit one transaction at solo and hosted scale.
Fallback-of-record: **SQLite-per-universe** (same codec, same Store contract) if the Stage 1 probe fails,
and the future zero-server embedded dialect — with the recorded flip condition: if the hosted roadmap dies
and embedded adoption becomes the growth path, SQLite was the right primary. **Git is retired** to a
delayed `runtime export --git` format plus a differential integrity oracle when the exporter ships;
until then, integrity rests on the standing verify-by-hash walk and the codec golden-vector suite.

**Runtime-computed StateId** over the logical tree, domain-separated by encoding + schema version
(plan §8). Identity is store-independent; a store swap is a data move; Law 3 has no asterisk.
Convergence is *structural*, never called semantic. Rejected: StateId = storage OID (bound identity to
one engine's encoding).

**NodeId = ULID minted at commit**, in the transition record. Rejected: NodeId = commit/storage hash —
hash-chained ids can never be remapped, and storage identity would quietly become semantic identity.

**CR-CJSON/1 canonical encoding** (plan §10): NFC at admission → RFC 8785 → LF framing; Unicode version
pinned in the encoding version; explicit numeric domains (finite JSON numbers mean their represented
IEEE-754 binary64 value; typed decimal/bigint/money strings preserve lexical numeric semantics). Ships
in Stage 0 with golden vectors. Rejected: calling the profile
"RFC 8785" bare (JCS neither normalizes nor frames), and IEEE-754 doubles for money.

**Record-per-object; clean logical paths; internal balancing trie; manifests derived.** Public paths
carry no shard segments (`memory/claims/<ulid>`); the codec balances high-cardinality collections with a
fixed-fanout hash trie that is identity-bearing but encoding-internal — it never appears in a path, a
scope, or a merge pattern (ADR-011). Rejected: single-file JSON collections — O(N) rewrites, guaranteed
conflicts. Rejected: time-prefix sharding (one hot shard for days). Rejected: shard segments in public
paths (storage leaking into capability scopes and identity).

**Two blob tiers plus the ingest gate.** ≤ 64 KiB inline as canonical objects, otherwise CAS blob under
the universe's **erasure namespace** (dedup within a namespace only); tool output enters State only as
summary + reference; a `subject`-tagged record **is** blob-stored regardless of size — mandatory routing
(plan §9, §22; ADR-011). Rejected: a third
in-repo blob tier.

**Fine-grained nodes, grouped into turns; durable turn journal; live-effect fencing.** A turn is a chain
published by one fenced CAS; `canon.turns` makes in-flight turns findable; an unresolved live-effect turn
semantically occupies its ref across lease failover (plan §14). Rejected: one-node-per-turn (discards
intra-turn causality); per-token commits; turn anchoring on internal refs (superseded — the transactional
store made it a row).

**Effects as immutable facts through a transactional outbox** (plan §15): intent and observation records
in `canon.effects`, written in the commit transaction; dispatch attempts operational; no `dispatched`
semantic phase; deterministic idempotency keys (proposal id + action hash); orphaned outcomes surface for
reconciliation; `unknown`-and-escalate is the common recovery path. Guarantees are **executor-class-
specific** (idempotent / queryable / non-idempotent / reversible — ADR-011); **approvals precede
intents** (a pending approval never occupies a live ref); the seam is the `EffectDriver`/
`ExecutionDriver` ports. Rejected: Temporal from day one; a per-universe refs/effects journal; blanket
"touched once" guarantees the executor class cannot support.

**Serial-per-ref concurrency; observed footprints at first consumer** (plan §14): no declared footprints,
no commutation calculus; admission validates the **compilation dependency witness** — external
dependencies (authority, tools, retrieval, availability, realm) on every admission, state dependencies
against an advanced head (ADR-011; the v0.5 "frame digest unchanged" check was vacuous — the frame
contains StateId); `ScopedStateView` traces reads from Stage 2; OCC admission activates at the §33 demo
and generalizes at Stage 10. Authorization runs **after** reduce, against the actual patch. Rejected:
declared read/write footprints (unenforceable-by-construction; write-skew; served no v1 consumer);
authorize-before-reduce (cannot see the write set).

**Realm from the execution binding; promotion as three-way reconciliation** (plan §16): nodes carry no
realm — origin is record provenance; the kernel resolves realm from the binding; promotion routes through
a standard turn with a promotion report; approvals never transfer across realms. Rejected: `Node.realm`
(one node is reachable from many bindings); realm from branch metadata (advice, not enforcement);
promotion as net-state-diff adoption (imports simulation-derived state unexamined). *Re-scoped by
ADR-030 decision 13: what the rejection protected against was import history could not attribute —
`runtime.adopt` imports the same bytes with a cited cause, a `departure/1` envelope and a path-exact
debt, so the rejection stands for unlabeled import and the label is what changed.*

**Authority is attested, never authored — including model egress** (plan §17): capabilities in state are
references; the kernel attests at execution; fork attenuates, merge intersects, expansion needs a recorded
grant; model invocations dispatch only under attested model capabilities; authoritative budgets are
kernel-plane. In v1 the kernel is an in-process API boundary, stated plainly; extraction is Stage 10+
hardening. Rejected: capability JSON as authority (self-grant by tree edit); budget counters in State
(StateId churn) or only in disposable rollups.

**Compiler is a battery, not a gate; cognition operates on the Continuation Frame** (plan §19–20):
compile input is Frame(state, input, realm, authority, tools, retrieval, runtime); memoization keys on
the frame digest; retrieval snapshots carry index epochs (a rebuild is a new epoch). Adoption Levels 0–2
assemble their own prompts. Rejected: compiling from State alone (stale cognition on revocation; realm-
blind affordances); watermark-only retrieval pinning (identifies the index without identifying the
materialization).

**Memory = immutable claims + lifecycle transitions**; status is a projection of ancestry; authority
labels on provenance are derived, never author-supplied. Rejected: a mutable `status` field inside an
immutable record.

**Conflicts, redactions, and expiries are values** (plan §11, §24): `StateValue` is a discriminated union;
merge conflicts are contested values with per-path continuation policy; jj-style first-class conflicts.
Rejected: auto-synthesizing conflicting memories into summary prose; `CanonicalValue | null` reads that
let consumers treat one side as truth.

**Stage 6 domain merge and promotion.** Merge policy is statically composed per logical path, with
structural JSON three-way in the runtime, domain hooks after the structural pass, exact transition
causes on every contested alternative, and domain invariants re-run before commit. Multi-parent
reconciliation is a standard authorized transition; promotion reuses the same planner but keeps the
simulation tip out of live ancestry (*narrowed by ADR-030 to the anchor's primary line — secondary
parents may cite any lineage, each citation a departure*), refuses simulated effect plans, and re-proposes selected actions
through the live effect bracket. Its final report is a record-only transition whose proposal input is
the durable evidence. Observed-footprint OCC activates here only for pure, single-parent state
transitions; disjoint work linearizes and overlap preserves a branch. General multi-agent scheduling
remains Stage 10.

**Structured-claim equivalence v1.** Reference roles compare by exact canonical identity; the runtime
does not invent alias equivalence. The conservative comparator can emit a contradiction *candidate*
for matching predicate/subject/scope with unequal objects, and Stage 6 stores that disagreement as a
contest rather than judging truth. Richer reference equivalence and predicate-specific incompatibility
belong to the domain that first supplies evidence for them, not to a universal core table.

**Six-object core, two worlds** (plan §2): Encounter (Session/Surface/Interaction) is the reference
host's design, frozen when built (Stage 8), promotable into the core with evidence. The three-world story
survives as packaging.

**Adoption levels are coverage contracts** (plan §3): AdoptionManifest per level; Level 0 specified
against LangGraph's real BaseCheckpointSaver contract; superstep = turn (settled); partial-superstep
resume is a named drill. Rejected: per-level "laws hold" tables (overclaimed what adapters can see).

**Executable Stage 0; replay as the spine; resequenced build** (plan §29, §31–32): `packages/domain`
(zod schemas + golden vectors + property tests) is the spec — no parallel eleven-document markdown tree;
every source of nondeterminism enters through one injected seam, recorded from Stage 1, and every
acceptance run executes twice; memory and merge precede any web; sessions/thread surface/multi-user are
Stages 8–9 (when a second user exists); machinery is staged to its first consumer. Rejected: a spec-prose
Stage 0 for an audience of one (three normative layers); the tape harness as a Stage 5 feature.

**No rename op in `PatchOp`** — delete + put; content addressing makes rename free.

**Selector grammar v1** — an exact logical path, or a final `*` (one segment) / `**` (zero or more),
including root `*` and `**`. Other punctuation is literal path data. Rejected for v1: picomatch's richer
grammar; adding it later is a selector-version migration, never a silent authority widening.

**Precondition language v1** — `exists | absent | hashEquals`, each over one clean logical path; no
embedded query language.

**Dialog record v1** — `{ role, content, at, via }`, with `role = system | user | assistant | tool`,
canonical inline content or a `BlobRef`, UTC-ms time, and a canonical host/input-route label. It is a
State record consumed by Stage 3, not an Encounter object.

**Tooling:** pnpm not bun (Temporal TS SDK compatibility — revisit when Temporal lands) · plain SQL not
ORM (the control plane is small; SQL *is* its spec) · `pg` + node-pg-migrate. Rejected: isomorphic-git /
nodegit / fast-import pipelines (moot with Git's retirement; archived in ADR-006).

**Toolchain pins:** Node ≥ 22 · TypeScript strict, vitest, fast-check, biome · zod v4 (the domain
package's only runtime dependency — it is the schema language of the executable spec) · ulidx · the
`canonicalize` package or a hand-rolled JCS 40-liner (inside CR-CJSON/1) · Postgres ≥ 16 with
`synchronous_commit = on` for canon · blob CAS `data/blobs/sha256/ab/cd/…` behind `BlobStore` —
conventional defaults; challenge via a one-paragraph ADR, don't churn silently.

**TypeScript, no Rust migration.** The host ecosystem lives in TS. The wire protocol exists for Python
hosts as a sidecar — not as a rewrite path, and honestly re-priced: a later format-and-spec play, written
when the reference host needs it (Stage 8); no near-term sidecar deliverable.

## Settled in v0.6 — ADR-011 (ratified)

Redaction via the **availability ledger** — bytes never mutate under a hash; availability epoch in the
compilation witness; derived-evidence sweep; subject-tagged payloads blob-indirect from admission;
erasure namespaces decoupled from universes. (Supersedes v0.5's redact-in-place, which broke content
addressing, poisoned keys against future writes, and let compile caches serve erased bytes.) · The
frozen hash/value ABI: algorithm-tagged length-framed preimages, bytewise segment collation, `$`-key
reservation, the `contest` patch op, language-neutral fixtures + JSON Schema as Stage 0 exit criteria ·
The atomic reservation predicate (head = base ∧ fence = token ∧ no rival open turn, asserted in the
intent transaction, with schema-enforced uniqueness) and approval-parks-its-turn sequencing ·
Universe-scoped Store handles; turn as the agent profile of the durable publication batch;
`HostCheckpointCodec` (decomposition an optional lens); engine protocol decoupled from session
envelopes; static `DomainModule` composition; packages private by default · Per-ref leases; destructive-
GC inputs durable (never `proj`); retrieval basis `(ref, position)`; replay compares records, frames,
bytes, decisions, and traces; version axes split · Stage patches: egress attested from the first
invocation; promotion at Stage 6; the portability gate (LangGraph + contrasting micro-host); Stage 11
acceptance. Rejected: the full architectural-profile reframe and 8-stage resequence (ceremony beyond a
solo project's needs; defects patched in place).

## Settled in Stage 7 — retention and erasure

**Erasure removes leaf payloads, never structure.** Only `value` objects are physically deleted; interior
tree objects keep their bytes, so the path, its leaf hash, and the StateId survive a redaction and
`verify()` can check the chain from stored objects instead of re-materializing payloads that are gone
(plan §22). Consequence, enforced with a typed `policy` error rather than discovered: a state with erased
payloads can be read, diffed, and verified but **not re-materialized**, so it cannot father a child —
which is why a tombstone is a transition that excises the content from the continuing state first.
Rejected: erasing tree/record objects (destroys identity, not content); re-materializing with opaque
leaves (buys continuation from an erased state at the cost of a second materialization path).

**A tombstone is a transition; erasure follows it.** Same shape as the effect bracket (§15): the durable
fact commits, then the world (here, the bytes) changes, so a retried erasure is idempotent and a crash
between the two is recoverable from the tombstone record. The pre-confirmation **referent audit** is part
of the contract, and for blobs it resolves through the BlobRef leaves that cite them.

**Retention classes are enforced by the evidence catalogue.** `canon.evidence` records the class each
payload was written under and `canon.evidence_inputs` carries the derived-evidence edges; expiry selects
`standard` and can never select `permanent`. Both are canonical — destruction inputs are never in `proj`
(§23). Blob GC roots include catalogued evidence, not only what the state tree names.

**Subject routing is path policy, not a value tag.** §9's mandatory routing is enforced by the kernel at
admission (inline `put` refused; `link` must name the subject's erasure namespace). Rejected: a
`$subject` typed tag — that would be an encoding migration against the Stage 0 ABI freeze for something
policy expresses without touching the codec.

**Restore is gated by the append-only logical and physical ledgers.** Hash-level availability explains
typed absence; `canon.erasure_targets` preserves the exact `(namespace, hash)` CAS address. A stale base
backup cannot contain an erasure that happened later, so the retained ledger/WAL stream is applied
offline before application traffic. Import holds one universe lock across CAS reconciliation, canonical
row insertion, and inline ledger scrub. The isolated PostgreSQL 16 `pg_dump`/`pg_restore` drill proves the
negative control really resurrects bytes first, then proves reconciliation removes them without touching
the same hash in another subject namespace.

**Evidence redaction ruleset owned by the kernel** (`scrubCredentials`): eleven credential patterns plus a
field-name rule, applied before payloads become evidence, with `sanitized` recorded so scrubbed bytes are
never called exact. This closes the OPEN item that was mis-owned to the Stage 4 gate.

## Settled post-demo — ADR-012 (ratified 2026-08-09)

Composable context systems: mind-layer work arrives as modules on two axes (domain / pipeline) under
four rules — boundary IR over plugin interfaces; rule of two for any interface or registration surface;
composition as digestable data folded into `compilerDigest`; personality (psyche) as canonical data
inside the authority envelope, kernel floor non-droppable. GTC is a module catalog and one reference
composition, never a loadable monolith.

## Settled in v0.7 — ADR-013 (ratified 2026-08-09)

**The GTC confluence: one project, two layers.** The GTC research branch (archived in
`specs/reviews/gtc/`) is absorbed: GTC names this repo's mind layer — module catalog and eventual
named reference compositions — never a separate system. · **Σ, the Context System**: one named,
versioned composition+policy object with three binding sites (build default / agent psyche /
situation), all reaching the frame through `compilerDigest`; `COMPILER_POLICY_V1` is Σ v0; mechanics
extracted at the second real Σ (rule of two). · **Features into the record**: at the next compiler
touch, candidates write their named feature components (recency, retrieval score, pin, chronology)
into the compilation record beside the collapsed priority; rankers are Σ-owned weights — module-local
final scores rejected. · **The mind-layer eval program** as the track's acceptance discipline:
switching benchmark, ablation ladder, leave-one-module-out, ContextUtility, WritePrecision; offline on
recorded frames where modules are deterministic. · **Dissolutions**: proposition identity = statement
value hash (no proposition table); ContextDiff = derived tool over two compilation records, never
stored. · **Class B reference domains** named: external authoritative truth enters as refs +
provenance + rebuildable views (§9's workspace rule generalized). Rejected: polyglot mind-layer stack
(Kafka/Neo4j/Redis-class — the one-engine rule extends upward); a `context_runs` table (invocation
records + compilation evidence already carry it); a dynamic module planner before module plurality
(plan-as-evidence arrives with the planner); third-party module sandboxing now (§34, Stage 10+);
authored epistemic-status fields (an injected document must not self-upgrade to "observed" — origin
trust stays derived; `stance` is content and may be authored).

## Settled in v0.8 — ADR-014 (ratified 2026-08-10)

**The reference-host component layer: owned behavior over copied chrome.** Chrome is
AI-Elements-class copy-in over the shadcn substrate (thread · Workflow/React-Flow · Code/Artifact
groups); the thread behavior layer — branch state machine over fork topology, edit-as-fork,
status/tool/approval wiring, CAS attachment upload — belongs to the Session Runtime, priced at
≈4–6 days over any kit versus a recurring migration tax on a Beta-tier runtime. (Supersedes v0.5's
Assistant UI thread-frontend pin and its `AssistantTransport` spike — replaced by the §27
chrome-mapping spike.) Ecosystem adoption is layered: substrate and behaviors (Next.js · Tailwind ·
shadcn/ui · Streamdown · use-stick-to-bottom) taken; sovereignty layers (§26 wire, Session Runtime,
kernel egress) kept — `packages/ai` already speaks AI SDK core at the provider seam. Known
divergences are forks, not adaptations: `MessageBranch` → controlled pager; the registry's injected
`ai`/`@ai-sdk/react` deps pruned at install. **assistant-ui carries a recorded flip trigger** —
re-table before the Stage 8 thread build iff v1 ships with the Runtime API in the Stable tier,
`ExternalThread` documented, and the branch-adapter semantics frozen (its
`ExternalThreadBranchAdapter` shape is right; its stability tier and bus factor are not). Evidence
with a Stage-8-open re-verify list: `specs/reviews/frontend-2026-08.md`. Rejected: CopilotKit as
base (frontend-declared state/tools invert the authority direction; its runtime wants to own the
loop); legacy `ExternalStoreRuntime` (synchronous in-memory branch switch over fully materialized
siblings; `resetHead` destroys descendant bookkeeping — hostile to universe-fork rebinding);
`AssistantTransport` (snapshot-state wire, server-truncation branching, breaking migration
pre-announced); `useChat`/UIMessage as the wire (§26 is the protocol, session-free); forking a chat
application (surrenders the architecture).

## Settled in v0.9 — ADR-015 (ratified 2026-08-10)

**Stage 8 is the complete single-user Encounter product; Stage 9 is its multi-user trust boundary.**
ThreadProjection, streaming, tool/approval parts, controlled branch navigation, edit-as-fork,
attachments, the DAG, compare, and the node inspector all land with the Session Runtime and versioned
wire in Stage 8. Stage 9 adds authentication, server-derived principals, tenancy policy, limits, and
RLS without introducing another thread runtime. This makes the ADR-014 spike a real vertical slice and
prevents the wire from freezing before its primary consumer exists.

**Durable event fan-out is direct and transactional at the Stage 8 scale.** Ref-publication events go
to every active follow binding at the ref-CAS linearization point; turn events go to the originating
session; binding/surface events stay local. Ref locks precede ordered session locks; binding versions
make races explicit; per-session sequences and envelopes commit with their durable subjects. The engine
emits only session-free facts through a transaction-bound host sink. The recorded scale escape is an
atomic event + recipient snapshot with asynchronous envelope materialization, activated only if the
measured direct fan-out becomes a publication bottleneck.

## Superseded in v0.5 (arguments archived in ADRs and specs/reviews/)

- **Git as the first Store implementation** → export format only (ADR-006 → ADR-010).
- **SHA-256 universe repos, reftable, Git ≥ 2.45, fast-import/cat-file pipelines** → moot with Git's
  retirement.
- **Turn anchoring on `refs/internal/turns/`** (ADR-002) → a turn-journal row in the commit transaction.
- **Declared read/write footprints + commutation rule** (ADR-004 v1) → serial-per-ref now, observed OCC
  at first consumer.
- **Erasure rewrite ceremony** (ADR-003) → patch-values-by-hash makes inline erasure one audited object
  touch.
- **SQLite-per-universe as primary** (design-competition verdict) → fallback-of-record + future embedded
  dialect, with its flip condition recorded above.

## Settled by ADR-030 — implemented 2026-08-22, awaiting Ren's sign-off

Every package of the program landed green under `pnpm test` and is recorded in
`specs/acceptance/history-core/{w1,w2,w3,w4,d1,d2,d3,d4,integration}.md`; acceptance is Ren's act,
and these entries become *settled* when he signs. They are recorded now because the code already
behaves this way.

- **Everything is a plugin; Cordis composes a runtime.** Adopted on W0's GO, pinned published
  (`@deepseek-ai/cordis@4.0.1`, the DSH seam at `0.1.0-rc.7`). Hard lines: `packages/domain` stays
  zod-only; the engine libraries stay framework-free and are mounted by bridges that hold no logic;
  only `packages/dsh-host` names the framework; production profiles omit HMR; attestation is a
  continuous observer on the mounted set, never a boot digest, because Cordis has no seal.
- **The product is a separate repository over two pinned upstreams** — `~/repos/context-runtime-product`,
  consuming `@deepseek-ai/dsh` and `@context-runtime/*` alike as published artifacts (tarballs until
  the registry push). Supersedes ADR-011's "packages private by default": every `packages/*`
  publishes at `0.1.0`, lockstep. Re-aims ADR-015 (Encounter is the engine's reference host, not the
  product UI) and ADR-014 (the migration tax is answered by channels, the `dsh-compat` shim and a
  measured budget — the session seam was byte-stable across four upstream releases).
- **context-runtime is the truth layer**: a `PersistenceBackend` under DSH's own coordinator, canon
  the writer of record, one runtime per security boundary, one universe per boundary, a session a
  `session/*` ref. The two-plane encoding — `ops.session_log_staging` folded one canon node per DSH
  turn — exists because the effect bracket holds a turn open across a tool and chunk-grade durability
  cannot share that cadence. Fork is ref creation; departures surface only as a revision change of
  the whole log; erasure keeps the envelope and synthesizes two placeholder forms.
- **R0, the one-time reset**: one soft genesis, every family at `/1`, the realm re-carved to
  `anchored | world | detached`, the uniform `<class>/<name>` Ref grammar with the anchor a class,
  realm elision abolished, one `OperationKey`, `standing → channel` on the admission axis. Strictly
  representational; no correctness invariant moved.
- **Standing is a per-ref examination ledger, never a scalar** — accrual fixed by format
  (departures, shared-World effects, downgraded attestation under a declaring profile), discharge by
  selector-set subtraction, anti-laundering structural, the badge `intact | examined | unexamined(n)`
  format-fixed; policy decides only preconditions and discharge authority.
- **One primitive for history rewriting, forward**: `state := target tree` as adopt, supersede,
  transplant (contesting, never refusing whole), examine, archive and un-archive — every kind a
  departure with its envelope and its footprint; `refs_guard` unchanged; promotion gains the labeled
  door `resolution: "theirs"`.
- **Worlds**: a `world` binding acts reversibly on the World it holds — hold × grant × scope × the
  bracket, the kernel written once as three tiers; holds are operational, the shared-ness canonical.
- **The operation surface is TypeScript the carriers compile against**, never a checked artifact.
- **Decided, not open**: no forward-looking departure event in the session log until a consumer
  for one exists.

## Guard policy — settled by ADR-031 (2026-08-22)

- **A contract is frozen if and only if a published package exports it.** Supersedes the freeze
  registry, its four-way `freeze | frozen-legacy-read-only | experimental | private-versioned` enum,
  and the rule-of-two paperwork. Semver on a published artifact is enforcement we do not administer
  ourselves; a JSON file we grade ourselves is not. Nothing is published yet, so nothing is frozen —
  that is the intended state while the plugin adoption is experimental.
- **No version number before a second live version.** The rule of two, applied to versions. It stays
  where we do not control both sides — published packages, the DSH session seam, canon rows once
  genesis hardens — and means nothing elsewhere. The 143 existing `/1` tags stay as inert names: a
  mechanical version sweep is what inverted two guard polarities during R0, and that risk buys nothing.
- **No generated inventory of the source tree.** `package-boundaries`, `dependency-inventory`,
  `integration-profiles`, `production-boundary-inventory` and the mediation matrix all asserted that
  the tree we read is the tree that runs. Plugin composition ends that. Ask the question live —
  `bench/scripts/history-core/lib/closure.ts` — or record what actually mounted.
- **The gate is `pnpm test`.** Carried unchanged from R0 and narrowed further: no self-tests for
  harness code, no per-change generator obligation, and effort tradeoffs surfaced to Ren rather than
  answered with more verification.

## Rejected on the merits — do not re-propose

- **Compressing the Twenty Laws to sixteen.** The derivations were sound; the optimization target was
  wrong — §35 is a review-gating checklist, and checklist redundancy is a feature.
- **Unifying Invocation with Effect.** Opposite retry semantics (§15 vs §19) and opposite realm policy
  (§29: replay feeds invocations from tape while effects stay impossible).
- **SHA-1 object format; NodeId = commit OID; single-file collections; one-node-per-turn; per-token
  commits; realm from metadata; capability JSON as authority; mutable status fields; auto-synthesized
  conflict summaries; Temporal from day one; Rust rewrite** — all carried forward from earlier rounds.

## Deliberately deferred — do not build (plan §34)

Second store backend (SQLite/PGlite embedded dialect) until an embedded-only host demands it · the Git
exporter and differential oracle until someone wants the export · CRDTs · custom vector DB ·
microservices · cross-universe transactions · learned compression · agent fusion · runtime
self-modification with its signed-bundle/sandbox machinery (ADR-009/010) · adapters beyond LangGraph
until that one seam is proven · per-subject envelope encryption of evidence blobs (plan §22, §34).

## Open — owned by a stage, marked OPEN in code when reached

- ~~**`SimulationId` semantics** (§16)~~ — closed by ADR-030 decision 14: the identifier became
  `WorldId`; a World is a universe-scoped, held, reversible-only slice of the external world, and a
  binding's realm is derived from it.
- ~~**Evidence redaction ruleset** (§18)~~ — closed in Stage 7: `scrubCredentials` in the kernel, with
  `sanitized` recorded on every catalogued payload. (It had been mis-owned to the Stage 4 gate, which
  shipped without it.)
- **Omitted structured-claim scope semantics.** Claims lacking the comparator's roles remain `unknown`;
  deciding whether a domain may treat an omitted scope as a shared default is a genuine domain-policy
  fork, not a core default.
- **Per-domain object-incompatibility semantics** (beyond v1's exact-identity contradiction candidates):
  supplied by the domain that first brings evidence for them (per Structured-claim equivalence v1),
  registering through a comparator seam extracted on `DomainModule` at that first consumer (rule of two,
  ADR-012). Restores, as an owned item, the obligation narrowed in `6c4872c`. — first consumer,
  post-Stage-6.
- **Sidecar auth model** — defer until a Python host exists.
- **Claim `stance`** (ASSERTS / DENIES / HYPOTHESIZES / …): stance is claim content and may be
  authored — it records what the source did; origin trust stays provenance-derived. Lands with the
  world-model domain's first consumer. — ADR-013.
- **Causal-predicate admission policy**: typed causal vocabulary (observed_correlation / stated_cause
  / inferred_cause / …) with stricter validation than ordinary predicates, enforced in the world-model
  domain's `validate()`. — ADR-013, world-model domain.
- **WritePrecision refinement** (v1 landed 2026-08-09 with mind-01 — retained/asserted over the status
  projection, `packages/memory/src/precision.ts`, measured in `specs/acceptance/mind-01.md`): what
  counts as a *useful* durable write beyond mere retention is owned by the first module whose
  acceptance demands more. — ADR-013.
