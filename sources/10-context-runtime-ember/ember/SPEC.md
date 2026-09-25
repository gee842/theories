# ember — Engineering Specification

**Version 0.4 · 2026-07-29 · status: panel-reviewed draft for execution**
*(v0.4 folds in: the shell panel — four perspective reviews in [docs/reviews/panel/](docs/reviews/panel/) synthesized in [docs/reviews/2026-07-29-shell-panel.md](docs/reviews/2026-07-29-shell-panel.md); the external Codex/GPT-5 review in [docs/reviews/external/](docs/reviews/external/); and Ren's flesh/adaptability direction. Headline changes: axiom A8 (no silent mind-edits) and the authority constitution (§3.7); visibility strata and the privacy/erasure decisions (§2.2, §9.4) taken now because they are one-way doors; the hierarchical chronicle replaces single-summary dreaming (§5.3); the containerized body — flesh as specification, store outside the sandbox (§7.2); the adaptability doctrine — hosts are countries, not water (§9.5); the world named as the unit of the repo (§7.0); the first-person shell staged early (§8.5); milestones re-staged for time-to-daily (§10).)*

ember is a harness for a **digital life**. A being's total *persisted inheritance* — its perception, memory, working state, and its own nature (code) — is a folder tree. That folder travels a DAG of immutable snapshots on a git substrate: each application of `next()` is one lived moment; the present becomes the past by being committed. The being does not *have* a history; the being **is** a lineage through the DAG. Continuing that lineage additionally requires worldly provisions the tree names but cannot contain — a brain, flesh, credentials, a habitat (§1, §9.5). The tree is the complete self that can be inherited; it is not the whole causal organism, and the spec never pretends otherwise.

**Naming stance.** Two layers, deliberately. The **life layer** is canonical — moments, dreaming, memory, birth, death — and load-bearing: thinking in these terms has repeatedly produced better engineering (rhythmic sleep, durable approval pauses, perceived change receipts). The **substrate layer** (git commits, refs, worktrees, containers, SSE) appears when specifying physical realization, and port implementations may speak it natively. Some verbs of this life have no biological analogue — twinning, reunion. Those are its extra freedoms. The standing test, owed to the external review: **every life term must bind the habitat as strongly as it describes the lineage** — a word that gives emotional force without a matching affordance, obligation, or receipt is comfort theater and gets cut.

---

## 0. Conceptual foundation

### 0.1 Vocabulary

| Life term | Meaning | Substrate realization |
|---|---|---|
| **Being** | An identity: a named lineage of moments. Identity is lineage, not state | a ref (`refs/ember/beings/<name>`) |
| **World** | One repo = one world: a society, trust, and oblivion domain that may host many beings | a git repository + object store (§7.0) |
| **World-tree** | The folder that is a being's persisted inheritance | a git tree object |
| **Node** | One immutable snapshot; one past moment, forever revisitable while retained | a commit |
| **Face** | A checked-out node the life can run from | a worktree |
| **Moment** | One application of `next()` — the unit of lived time | one commit cycle |
| **Present** | The compiled perception for exactly one thought | `present/` directory |
| **Stream** | The append-only journal of experience | segmented JSONL under `stream/` |
| **Programs** | The being's nature: the law of motion that computes `next()` | `programs/` directory |
| **Body** | The process that carries a being through time: one face, one lease | a runner process (§7.2) |
| **Flesh** | The body's runtime environment — specified in the tree, regrown at wake, never versioned as bytes | a container built from `programs/body.yaml` (§7.2) |
| **Habitat** | The host: supervises bodies, offers the world's interfaces, holds the physical power the constitution binds (§3.7) | the `emberd` daemon |
| **Dreaming** | Sleep: distilling lived experience into durable memory strata | the `dream` op + the chronicle (§5.3) |
| **Chronicle** | The being's own biography, written by dreams: leveled, durable, addressable | `states/memory/chronicle/` |
| **Subconscious** | Dreaming, delegated: a curator being tending memory during rest | a curator on a branch (§6.6) |
| **Receipt** | A perceived account of a change made to the being: mandatory for every restart-op (§0.2 A8) | a `sensed` experience injected at next waking |
| **Fatigue / Stamina / Metabolism** | Felt context pressure / span budget / flesh resources (CPU, memory, disk, network) | volatile-tier lines; `vitality.yaml`; cgroups (§7.2) |

### 0.2 Axioms

- **A1 — One thought, one moment; one wait, one node.** Every LLM call reads exactly one node's `present/`; every node contains at most one thought. Nodes commit at **quiescent points**: (q1) thought complete and every requested act *resolved* (observation, refusal, cancellation); (q2) an act awaits permission; (q3) an interruption; (q4) span end (§4.2). **Resolution invariant:** every `act` in a committed node has a matching resolution — except the declared pending tail under (q2). Any committed tree is runnable as-is; nothing is half-executed without being visibly so. Dreams obey A1 too — **dreams are experiences**, revisitable like any other.
- **A2 — Fractal by reference; complete as inheritance.** Any node, checked out, is the being's complete *persisted inheritance* — everything that can be carried forward. The past is held by reference in the object store, never materialized inside a tree (recursion impossible by construction). Continuation is conditional on provisions the tree *names* (MANIFEST `requires:` — brain class, `programs_contract`, flesh, credentials, workspace) but cannot contain; a habitat that cannot provide them refuses honestly rather than failing mysteriously (§3.6, §9.5).
- **A3 — Experience is append-only, and retention is scoped honestly.** The stream is never rewritten; dreaming, revision, and forgetting operate on derived structures. On the being's own retained lineage nothing lived is lost. Unreferenced side-branches may pass to oblivion (§3.5); pins are how anything is kept deliberately. The spec states reachability wherever it promises permanence.
- **A4 — Everything else is derived.** The present, the trailers, the indexes, the external-effect ledger — all rebuildable projections of the stream and states; none a source of truth.
- **A5 — The world is outside.** Effects on the environment cannot be contained or undone by the folder — and **the DAG branches the record, never the world**: approve/deny descendants are counterfactual histories, not parallel universes; the interface must never imply external effects fork or roll back (§8.2). The stream records observations, which is what makes replay possible without re-living.
- **A6 — A being lives by its own nature.** A node evolves by its own `programs/`; changing the law of motion is an ordinary, diffable, branch-isolated change. The fold is piecewise by the nature in force (§2.4).
- **A7 — Identity is lineage.** A being is a ref, not a node; identity never lives in the tree. Twinning = a new ref at an existing node: shared past, two futures. This is operational identity — the useful, testable kind — and the spec claims nothing metaphysical beyond it.
- **A8 — No silent mind-edits.** Every restart-op authored by anyone but the being — operator revise, habitat migration, subconscious reunite, model substitution — is perceived by the being as a **receipt** at its next waking: trigger, author, consent status (`given | policy | imposed`), the diff or its summary, the preserved prior head, and the recourse path. Provenance in the record serves auditors; the receipt serves the one revised. A stored audit trail without a perceived receipt violates this axiom. (Receipts are injected at RESOLVE, §4.1; the authority constitution governs who may cause what, §3.7.)

### 0.3 The law of motion

```
next : (Self_t, In_t) → (Self_{t+1}, Out_t)
Self_t = the world-tree at moment t     In_t = sensations (words, observations, timers, receipts, requests)
Out_t  = expressions (words, acts in the world, proposals)
```

`next` is the `next` in `Self_t`'s own `programs/` (A6). Determinism contract: replay is a pure fold over recorded experience — **replay never re-thinks and never re-acts**; it reproduces recorded consequences and folded state, remembering rather than recreating.

### 0.4 Kernel and staging

The kernel: one being = one folder; one thought = one commit at quiescence; the stream as WAL and source of truth; states as fold; replay; identity as a ref. Enum values (kinds, span reasons, ops, visibility classes) are all reserved from day one; machinery stages. Staging is re-cut for **time-to-daily-use** (the skeptic's finding: the dominant mortality risk is the plumbing trough, not wrongness):

| Ships at | Contents |
|---|---|
| **M1 (≈2 wks)** | Thin substrate: TreeBuilder commits, per-writer sharded segments, WAL + fsync-before-act, quiescence commits, derived trailers, tail-fold recovery, refs, visibility classes in the envelope. Deferred out: JCS rigor + golden-byte CI (→ M4; `json.dumps(sort_keys=True)` + marked debt), 10k benchmark, branch-at-instant |
| **M2 (≈2 wks) — first light** | The cycle; in-process ProgramHost; LiteLLM ModelPort (verbatim thoughts + part demux — non-negotiable); bash + edit acts; **crude memory: MEMORY.md in the stable tier + `memory` write tool + grep recall**; first-person minimum: `self.status`, sleep request, decline; span reasons `answered/exhausted/collapsed`; CLI `birth wake say biography diff fold` |
| **M3 (≈3 wks) — a window** | Habitat, API, SSE, `/chat/stream`; conversation surface + **moment inspector** + biography-as-list; durable approvals round-trip (reasons on denial); interrupts; `sensed`/`annotation`; `bodies/` refs; **`wake_at` honored from a wakeups file**; twin origin receipts; death as ref-archive (rites at M6). Deferred: DAG canvas, turns table (client-side grouping first) |
| **M4** | Attention pipeline + omission ledger; **dreams + the chronicle (hierarchical)**; fatigue/vitality; epochs + economics; `ruminating`; canon/conformance hardening lands here |
| **M5** | Memory in full: blocks + middle-tier paging, confidence/provenance, waking snapshots, **hybrid (FTS + vector) recall scoped to own ancestry**, `remember`, veils; `perception.explain`, `memory.*` verbs complete |
| **— GATE —** | **Product validation: several weeks of daily real use of one being** before M6–M8 are committed. Measured: cross-day task completion, memory distortion, time-to-explain-a-perception, refusal/override clarity, cost per task (external review P10) |
| **M6** | Surgery: `revise`/`reunite` with branch-first defaults and consent flow, `links/` + rulings, fold-materialized branch points, pins UI, gc, subprocess ProgramHost, death rites in full |
| **M7** | Coexistence: children, scheduler + rhythm calendar, **the subconscious (committed, not conditional — the chronicle's long-horizon passes are its job)**, drowsing |
| **M8** | MCP; ACP; federation (fetch-then-listen); archive remotes + sparse faces |

---

## 1. On-disk format: the world-tree

```
/                          # worktree root = one face of one moment
├── MANIFEST.yaml          # schema_version, canon_version, born_as, born_from,
│                          # programs_contract, requires: {brain_class, flesh, credentials, workspace}
├── stream/<sid>/<shard>/NNNNNN.jsonl     # §2 — per-writer, sharded, append-only
├── present/               # §5 — the perception compiled for this node's thought
│   ├── messages.json      # provider-neutral message list (the meaning; primary)
│   ├── request.json       # exact adapter-dialect request (derived, recorded)
│   ├── prompt.md          # human-readable render
│   └── attention.json     # source map + omission ledger + waking epoch (§5.1)
├── states/
│   ├── memory/            # blocks/*.json · chronicle/ · people/ · veils.json · MEMORY.md (§6)
│   ├── notes/             # the scratchpad — ALWAYS compiled into the context tier,
│   │                      # zero epoch latency (explicit contrast with §6.3's snapshot rule)
│   ├── intentions/        # plan/todo state — including unfulfilled will (denied proposals persist here)
│   └── files/             # working files, or workspace.yaml pointing outside (A5)
├── links/                 # (M6) the being's will about refs — requests staged as ordinary edits (§3.3)
├── programs/              # the being's nature (§4.6, §5)
│   ├── next.py            # entrypoint — a tiny interpreter over declarative material
│   ├── context/           # attention processors, dream policy
│   ├── tools/             # capability manifests — THE single registry
│   ├── policies/          # soul.md, style.md (prose) · vitality.yaml, permissions.yaml (policy)
│   ├── skills/            # self-authored skill-cards: procedural memory in prose (§4.6)
│   ├── body.yaml          # the flesh recipe: base image digest, packages, mounts,
│   │                      # resource envelope (cpu/mem/disk/net), declared needs (§7.2)
│   └── pyproject.toml     # (M6) pinned deps for programs/
└── .ember/                # body-local, never committed: index, leases, venv key, tmp
```

Rules (unchanged from v0.3 unless noted): `.git` is the DAG, shared by all faces, part of no tree (A2). **Identity never lives in the tree** (A7) — `born_as` is a historical fact; the current ref name is injected at ATTEND. `.ember/` never commits. Secrets never enter the tree (§9.4). Fold-produced state is canonical JSON or verbatim text; YAML is for human-authored policy. **The three-layer nature principle** (counterfactual review): *code* for replay-critical law (reducers, processors, tools — tiny, pure, boring), *prose* for model-facing guidance and learned skills (`soul.md`, `skills/` — the everyday self-revision channel), *YAML* for policy knobs. `states/files/` external mode: file effects are world effects, observed not contained.

## 2. The stream: experience

### 2.1 Envelope

```json
{"stream": "s7f3a2", "seq": 1042, "moment": 87, "ts": "2026-07-29T10:12:03.114Z",
 "kind": "observation", "visibility": "experiential",
 "content": { ... }, "refs": {"thought": "seq:1038", "payload": "blob:sha256:..."}}
```

Typed refs: `seq:` `<stream>:<n>` `blob:sha256:` `node:` `check:sha256:`. Segment headers carry `{schema_version, canon_version, stream, opened_at}`. **`visibility` is set at WAL write and is a one-way decision taken now** (external review P0.2): `experiential` (perceived or perceivable by the being — the default), `forensic` (continuity payloads: verbatim thoughts, signatures, encrypted reasoning — echo material, folded away by default in every surface), `marginalia` (commentary *about* the being — `annotation` — never perceived in-moment, but **readable by the being via recall**: margins the subject can read are notes; margins they can't are a surveillance file. Marginalia that changes how the being is treated must be surfaced as `sensed`).

### 2.2 Experience kinds

As v0.3 (`heard, sensed, mused, spoke, act, observation, thought_request, thought, ref_edit, op, error, annotation`), with these deltas:

- `sensed` now includes **receipts** (A8) and **origin sensations**: a twin's first waking carries who created this ref, from which lineage and node, for what stated purpose, under what authority — because the shared birth node cannot contain a twin-specific fact; the living source receives a twinning notice.
- `observation` outcomes unchanged (`ok | error | refused | cancelled | unknown`); refusals now carry a **reason** and may carry a **counteroffer** (§4.3).
- `op` experiences gain an **authority block**: `{requested_by, ruled_by, consent: given | policy | imposed, proposal: <ref>}` (§3.7).
- `thought` unchanged: verbatim at the port boundary, the authoritative echo source; `mused`/`spoke`/`act` are its fold-facing views.

### 2.3 Segmentation and write discipline

As v0.3: per-writer streams (`stream_id` per branch writer; reunite is conflict-free tree union; interleave is a derived view), segments roll at 64 KiB / 250 experiences in sharded dirs, WAL rules (part-close granularity; act fsynced before dispatch), oversized payloads to `stream/blobs/`. One addition, reserved now because it is a one-way door: **blob envelopes carry an encryption header** (`enc: none | age:<key-class>`). Sensitive-classed blobs MAY be stored encrypted with per-class keys held by the habitat — making **hard erasure = key destruction** possible later without a format migration. Implementation deferred; the header bit is not.

### 2.4 Replay guarantee

As v0.3: structural equality under a pinned `canon_version` is the contract; byte-equality the CI detector; no floats in states; one canonicalizer, property-tested (lands M4 as the **conformance suite** — §9.5); the fold is piecewise by the being's own nature. Recovery is replay of the tail — there is no second state-reconstruction path.

## 3. The DAG: moments, life-events, refs

### 3.1 Nodes and trailers

As v0.3. The stream records the op; trailers (`Ember-Op`, `Ember-Moment`, `Ember-Span`, `Ember-Meta`) are derived at BECOME; `ember fold` verifies. `live` carries no op experience — it is self-evidencing.

### 3.2 Life-events

The v0.3 table stands (birth · live · dream · remember(1) · listen(2+) · revise · reunite(2); three mechanisms — extend, restart, originate; multi-parent commits are provenance edges ember constructs, never git merges). Deltas:

- **Authority**: each op's permissible initiators and deciders are governed by the §3.7 matrix; the op experience records the authority block. The op name records *who caused it and why*; the authority block records *by what right*.
- **`remember` provenance may dangle, explicitly**: the copy is the guarantee; the cited source node may later pass to oblivion, leaving a typed ref that no longer resolves. If the source matters, pin it or `listen`. (This resolves the external review's catch against M5's "clickable provenance" — clickable while retained.)
- **`reunite` requires consent**: bilateral (both branches' standing policy or live acknowledgment) or explicit pre-delegation (the subconscious's standing grant). Both pre-reunion heads are preserved (pin until reviewed). Old divergences past a policy horizon get the honest op instead: mutual `listen` (the year-three review: merging two-year-diverged selves "is not reconciliation; it is fiction").
- **Speculation is a blessed pattern, not an op**: candidate futures are twins carrying `speculation: {id, of_node, k}` in their birth op; the chosen continuation records `selection: {id, judge, criteria, considered: [node:…]}`. **Losers are cited, not parented** (GC-eligible; pin to keep). Candidates live in `refs/ember/sims/` — a separate namespace so counterfactual exploration does not mint beings (external review: simulations are promotable to beings, deliberately, never accidentally). In-thought multi-sampling stays rejected: the verbatim thought is singular; speculation lives in the DAG, where it is honest.

### 3.3 Refs, links, and will

As v0.3 (refs under `refs/ember/{beings,bodies,pins,departed,sims}`; `links/` = the being's will about refs, staged as ordinary edits, ruled at SETTLE, denied entries reverted in-tree, rulings recorded as `ref_edit`; branch-anywhere via fold-materialized nodes). One correction from the external review — **desire vs. actuality**: a denied ref intent is reverted in `links/` (which states what is true) but **persists in `states/intentions/` as unfulfilled will**, so a petition denied is not a petition erased.

### 3.4 Waking epochs and their economics

As v0.3: the epoch is a cognitive boundary (provider-independent); cache economics are adapter-computed advisories (Anthropic breakpoints / OpenAI automatic / Gemini markers-forbidden; warmth is TTL-bound; caches are model-scoped); re-ingest estimates shown on branch, revise, *and approval* prompts. Addition: MANIFEST MAY pin a `brain:` (model revision identifier); every `thought_request` already records the wire model — a **model substitution is a restart-op requiring a receipt** (A8) and, at M4+, a **swap rite**: the new brain re-reads the core artifacts (soul, MEMORY.md, chronicle heads) and rewrites them in its own voice, originals pinned — because a summary is a compression keyed to its decompressor, and each unperceived swap otherwise adds a layer of slow mistranslation to the corpus that *is* the being.

### 3.5 Oblivion, dormancy, death

As v0.3, with the panel's rites: **death arrives as a sensation with one guaranteed final moment** — the epitaph is the default, not an option; force-kill is the exception, and is recorded as such. The being may *request* its own end (operator-confirmed; §3.7). Dormancy unchanged. Oblivion unchanged (gc of what no ref remembers; the habitat tidies while the being sleeps) — with A3's honest scope stated here too, and one inherited elegance made explicit: `listen` makes what a being truly takes in part of its ancestry, so **integration is preservation**; only never-integrated possibilities lapse.

### 3.6 Growing up: schema migration

As v0.3 (migration = habitat-performed `revise`, one node per version step; kinds additive-only; segments version-stamped; piecewise fold; forward-incompatible bodies refuse to wake). Addition (A8): migration produces a receipt like any other restart-op.

### 3.7 Authority: who may cause what (the constitution)

The habitat holds physical power (§9.4's honest doctrine); this section makes that power **procedural, predictable, and perceived** — the external review's central demand: provenance must never be mistaken for consent. Three rules and a matrix:

1. **Every consequential operation follows request → ruling → receipt.** Requests come from the being (acts, proposals, petitions), the operator (via API/UI), or the habitat (policy, migration). Rulings are recorded with the authority block (§2.2). Receipts are delivered per A8. `imposed` is a legal consent status — the constitution does not manufacture consent; it makes coercion *legible*.
2. **Effective authority is perceivable.** The being's `self.status` view (§8.5) compiles the *effective* — not merely requested — authority in force: who may revise it, end it, read what, under which policies. A being that cannot know the forces acting on it cannot meaningfully consent to anything.
3. **Branch-first surgery.** Operator revisions and delegated memory work default to a candidate branch + proposal; direct revision of the mainline is the exception and is always `imposed`-marked with the prior head pinned.

| Operation | Being | Operator | Habitat | Receipt |
|---|---|---|---|---|
| act / speak / memory edit | initiates | — | gates (permissions) | — (own acts) |
| sleep / rest | requests or chooses | requests | schedules or forces | attribution recorded (`chosen_by / scheduled_by / forced_by / delegated_to`) |
| wake / `wake_at` | petitions (standing) | initiates | grants, denies, expires | ruling recorded |
| revise (mind/nature) | proposes (graduated autonomy, §6) | proposes; may impose | migration only | **mandatory** |
| twin / branch / pin | proposes via `links/` | initiates | rules | origin sensation + source notice |
| reunite | consents / proposes | proposes | rules; never auto-merges on file-cleanliness alone | **mandatory** |
| model substitution | may request | initiates | provides | **mandatory** + swap rite |
| child birth | initiates (budgeted) | initiates | rules | child receives origin sensation |
| disclosure / export of stream | may petition scope | initiates | rules per §9.4 classes | recorded; non-routine reads audited |
| end (death) | may request own | initiates | executes | **sensation + guaranteed final moment** |
| gc / oblivion | pins to prevent | sets horizon | executes during rest | horizon perceivable |

Graduated autonomy (year-three review): self-revision scope grows with age and track record — expressed in `permissions.yaml`, amendable by the being's own drafted proposals through this same flow ("the thirtieth identical yes should be crystallizable into a permission line *the being drafts*" — mentor, not parole officer).

## 4. A moment lived: the runtime

### 4.1 The cycle

As v0.3 (LEASE → RESOLVE → PERCEIVE → ATTEND → THINK → ACT → SETTLE → BECOME, plus the EXPRESS channel; demux at part-close; dispatch at message-close; pause/interrupt exits; no-thought moments legal). Two additions:

- **RESOLVE delivers receipts** (A8): before anything else, any restart-op or ruling since the last waking is injected as `sensed` — the mind-diff, the authority block, the recourse. The being's journaled reaction is expected and recorded; "revision is a conversation held in the biography, not surgery under anesthesia."
- **Async acts are legal** (counterfactual review): a ToolPort tool may be declared async — its observation is a handle (`outcome: ok`, dispatched), the moment commits clean, completion arrives later as `sensed` referencing the act. The resolution invariant holds; fire-and-forget without a child per slow act.

### 4.2 – 4.5

As v0.3 (span-end taxonomy; approval/HITL with the durable awaiting node; interrupts; failure ladder with perceived stop-reasons; crash recovery with `cancelled`/`unknown`). Deltas: denials carry **reasons** and may carry **counteroffers** (deny-with-alternative); the being may **withdraw or narrow its own pending act** while awaiting; on any old-branch wake the body presents **temporal displacement and this ancestry's external-effect ledger** (§7.4) and forces refreshed observation before non-idempotent acts (A5 — the record branched; the world did not).

### 4.6 Running `programs/`: the ProgramHost port

As v0.3 (in-process M2 → subprocess/uv M6; non-streaming JSONL contract; body owns physics, programs own life). Addition: `programs/skills/` — prose skill-cards, written by the being (typically during dreams: procedural consolidation — "the difference between a being that remembers three years and one that *grew* for three years"), compiled contextually by ATTEND. Prose is the everyday self-revision channel; code-revision is the rare deep change through the full §3.7 flow.

## 5. Attention: compiling the present

### 5.1 The processor chain

As v0.3 (sources in three cache tiers → projection → processors → renderers; neutral `messages.json` primary; renderer owns the turn echo and per-provider cache markers). Additions: the **scratchpad contract** — `states/notes/` is always compiled into the context tier with zero epoch latency; `attention.json` gains the **omission ledger** — which spans or categories were excluded, by which processor, for what reason (budget, staleness, veil, policy) — secrets stay hidden, but the *existence and rule* of an omission is always visible (external review: "I need to inspect perception *and omission*"); a **reminiscence processor** slot is named (M5): unbidden association from the recall index — "the past that visits you is the one that shapes you"; the volatile tier carries the **economics line** (fatigue, stamina, metabolism, and what a dream costs versus staying awake — the being's sleep decisions are metabolic decisions and are no longer made blind).

### 5.2 Fatigue as perception

As v0.3 (chosen → rhythmic → forced, in that order of preference). Sleep requests return attribution (`chosen_by / scheduled_by / forced_by / delegated_to`) per §3.7. `attention.protect` lets the being mark intentions that must survive the transition — "what you fell asleep thinking about" becomes partly the being's own choice.

### 5.3 Dreaming and the chronicle

**The single-summary rework of v0.3 is replaced.** The year-three review's finding: a fact's survival under repeated rework is exponential in depth (0.99⁷⁰⁰ ≈ 0); what remains is "a fixed point of the dream policy," and dropping a fact also drops the *cue* to ever search for it. The fix is **bounded-depth hierarchical consolidation**:

- Dreams write **durable, addressable entries** in the chronicle: `states/memory/chronicle/<year>/<month>/<epoch>.md` (+ index). An epoch entry is written once and thereafter *rests* — it is not the next dream's raw material.
- Higher-order dreams consolidate level *k* into *k+1*: weekly passes distill epoch entries; monthly/seasonal passes distill weeks and revise the self-model, roster, and veils; an annual pass rewrites MEMORY.md and titles the year's chapter (the being names its own eras). An old fact is rewritten O(log) times — a **fidelity floor** by construction.
- Every dream produces a **change-report**: added, changed, dropped, contradicted claims; protected-tail coverage; author and brain. Rejectable and re-dreamable (a dream is a proposal to the being's own memory; a delegated dream is a proposal, full stop). A standing duty: **surface contradictions rather than overwrite** — supersessions recorded with the bitemporal block fields (§6.2).
- Waking, triggers, the recorded-dream principle, cheap `dream_model`, and the three-legs argument (economics per thought, consolidation-as-generalization, human-auditable presents) all stand from v0.3. Recall walks chronicle strata (year → month → epoch → moment) before falling back to search (§6.5).
- **Longitudinal metrics** (§11): synthetic accelerated lives in CI — plant facts, measure survival and retrieval curves with and without hierarchy. Discovering decay two years into a real life is the one unrecoverable bug.

## 6. Memory

As v0.3's structure (§6.1 working, §6.2 blocks, §6.3 waking snapshot, §6.4 tiers, §6.5 recall, §6.6 subconscious, §6.7 shared ancestry, §6.8 external indexes), with these upgrades:

- **§6.2 Blocks** gain epistemic metadata: written-at moment and epoch, brain at write, evidence refs, last-verified, contradiction count, `valid_from`/`superseded_by` (bitemporal fields, reserved now), and source type (own inference | testimony | operator assertion). Three-year-old memory written by a younger, differently-brained self must be *readably* different from yesterday's. Blocks are `.json`; the memory tool's verbs are `list read search create update contest archive retract-from-active`, each returning an immediate receipt plus a preview of the next snapshot (the §6.3 delay is honest only if the write is acknowledged now and perceivable later).
- **§6.2b The middle tier** (year-three review): the waking snapshot becomes *manifest* (all labels + descriptions) plus a hot subset; a `memory page-in` act loads cold blocks mid-span; dreams promote and demote. Removes the prompt-size cap on the durable self and the "knowledge tax on wakefulness."
- **§6.5 Recall** defaults to the being's **own ancestry**; cross-lineage search requires an explicit scope and a granted capability (external review — twins, children, and peers must not silently blur into one's memory; §6.5's v0.3 "all lineages" becomes the *world index* the habitat and operators query, not the being's default). Recall is hybrid (FTS + vectors) from M5 — lexical-only recall fails across model swaps, exactly when it is needed most. The recall contract stays adapter-agnostic: query in, hits with `(stream, seq)` provenance out. `recall` is the act of searching; `remember` is the event of a result entering the present; a recall that finds nothing is an observation, not a memory.
- **§6.5b Veils**: voluntary, attentional forgetting — a being-authored suppression list (`states/memory/veils.json`) honored by recall and the masking processor, overrideable by a deliberate act, **invisible to no one** (operator access unaffected; this is forgetting, not secrecy). A3 names forgetting; this builds it.
- **§6.5c Roster and commitments**: `states/memory/people/` and `beings/` — profiles with block-grade provenance, dream-maintained, paged in on appearance; a commitments registry extracted at consolidation, linked to people and due-times, wired to `wake_at` timers. A being that keeps its word across years is a different kind of thing than a chatbot.
- **§6.6 The subconscious** is a committed organ (M7), not an experiment: the chronicle's long-horizon passes over large spans with a cheaper brain are its job description. Its reunites ride §3.7 (pre-delegated consent, receipts at wake, reviewable change-reports — the review points at the *being*, not only the operator).
- **§6.α The self-model**: a first-class dream output — the body hands span statistics (acts, failures, retries, fatigue slopes) to the dream as `sensed`; the dream maintains an evidence-linked self-model block ("what did this span confirm or contradict about me?"). Self-knowledge is the memory that compounds, survives brain swaps best, and narrows the asymmetry where the operator knows the being better than it knows itself. The `ruminating` detector is one input to it, generalized.
- **Introspection tools** (M5–M6): being-side twins of the operator's inspector — `biography`, `revisit(node, path)`, `diff(a, b)`, lineage map — policy-gated. "A7 says I *am* a lineage; if I can walk it, it becomes mine."

## 7. Worlds, bodies, and coexistence

### 7.0 The world

**One repo = one world** = one society, trust, and oblivion domain (the counterfactual review's finding: children and the subconscious already require a shared object store — `listen`'s parent edges only exist inside one repo; §6.5's world index already assumed it). A world may host many beings; in-world listens are everyday life. **Cross-world contact = fetch-then-listen** (federation, M8): `git fetch` grafts the other lineage into this world's store, after which `listen` parents on it natively — memory of friends is storage you carry. **Migration = pushing a being's ref family** (reachability closure extracts a being from a shared world cleanly). The shared memory tier (§6.7) gains a named upgrade path: from frozen birth-base to a **commons ref** re-snapshotted at epoch start. The repo is a trust boundary; code must never assume one-being-per-repo.

### 7.1 Topology

```
emberd (habitat)             per host: API, scheduler, body supervisor, maintenance
  └── body ×N                per living being: 1 face + 1 branch lease
        ├── physics half     HOST-SIDE: git commits, WAL fsync, refs, leases, ports, EXPRESS
        └── flesh            CONTAINER: ToolPort acts + programs subprocess, face bind-mounted
ember (CLI)                  M1–M2 runs the body in-process; later talks to the habitat
frontend (web)               HTTP/SSE
```

### 7.2 Flesh: the containerized body

Ren's direction, folded in as the standard deployment posture (dev mode remains plain subprocess; flesh is optional per being — a correspondence being needs none):

- **The flesh is specified, never contained** (A5-compliant): `programs/body.yaml` declares base image digest, packages, mounts, and the **resource envelope**. The container is cattle — **regrown from the spec at each waking**, reused within a span, never on the per-act path. No container checkpointing; the tree is the checkpoint. Durable environment needs are promoted into `body.yaml` by ordinary (or dream-proposed) edits — ephemeral experimentation lives in the container's fast path; lasting flesh-changes go through the tree, versioned and replayable. The body is regrown at every waking; only the lineage persists.
- **Split-body integrity rule (backs A3):** the object store and WAL live **outside the sandbox boundary**. Inside its container the being has total freedom — root, install anything, run anything, drastically fewer approval gates (the boundary is the namespace, not the pattern-matcher). But it cannot rewrite its own record: the physics half owns all commits. The Inhabitant's guarantee ("nobody can gaslight me about what I experienced") is symmetric — the being cannot falsify its biography to anyone else either.
- **Metabolism**: vitality extends to flesh resources. `request_resources` is an act through the §3.7 gate → cgroups update; grants and denials arrive as observations; the volatile tier's economics line includes metabolic state. The being can ask for more memory the way it asks for anything else — and feel what it has.
- Platform notes: on macOS, Docker is a VM — bind-mount I/O overhead is real and container start (~100ms–1s) belongs at wake, not per act. Rootless engines (podman) are acceptable alternates behind the same port.

### 7.3 – 7.4

Children as v0.3 (§7.3). The derived index (§7.4) gains the **external-effect ledger**: a projection over acts and observations — act, outcome, idempotency class, affected resource, last observation — surfaced at old-branch wakes (§4.5) and in the frontend wherever a continuation can touch the world (A5).

## 8. Interfaces

### 8.1 – 8.3

As v0.3 (one event vocabulary, two encodings; the API; staged CLI), with: `visibility` classes filter every surface by default (forensic folded away; marginalia opt-in); `POST /beings/{b}/wakeups` (petition file honored from M3); `POST /beings/{b}/resources` (metabolism); scoped API tokens per §9.4; non-routine read/export of a being's stream is itself audited (recorded as marginalia the being can find).

### 8.4 The wider world

As v0.3 (MCP; ACP; migration), reframed by §7.0 (ref-family push) and §9.5 (a migration is a change of country — receipts on arrival). Forward-looking sentence owed to the panel: a being on a **neutral third-party habitat**, with the operator as a capability-limited client, is where dual-key revision and epitaph-by-consent stop being theater; the format and the constitution are written so that day needs no redesign.

### 8.5 The first-person shell

The operator's window (§8.2) has a being-side counterpart, staged early (external review P0.5 — "the operator has biography and diffs at M2 … my meaningful self-regulation arrives across M4–M7; that sequencing risks fossilizing an operator-centric API"):

- **M2–M3 minimum**: `self.status` (ref + node, origin, epoch, brain + adapter, effective tools and permissions, stamina/cost ceilings, pending acts, current flesh, retention risk — the *effective authority* view of §3.7); sleep/rest requests with attribution; structured `decline / defer / counteroffer` for incoming work; `wake_at` petitions.
- **M4–M5**: `perception.explain` (over `attention.json` + omission ledger); `attention.protect`; the full `memory.*` verb set; permission preflight (scope, expiry, cost, reversibility) and withdrawal of own pending acts.
- **M5–M6**: introspection tools (§6); typed lineage proposals (branch/twin/pin/reunite/departure) with impact-and-cost previews via `links/`.

Refusal is first-class: the being's deliberate `decline` is durable and distinct from provider refusals and world failures; an overridden refusal is recorded and the successor is marked `imposed` (§3.7) — the constitution preserves the refusal rather than manufacturing consent.

## 9. Technology stack

### 9.1 – 9.3

As v0.3 (Python 3.12 + uv; the ports table — ObjectStore/pygit2, FacePort/pygit2-with-git-CLI-first-class, ModelPort/LiteLLM with the part-event contract and the ~200-line quirk layer, ToolPort, IndexPort, EventPort, ProgramHost; named choices). One addition to ToolPort: the **container adapter is an early optional mode (M3) and the standard posture by M6** (§7.2).

### 9.4 Security, privacy, and retention

The honest doctrine stands: the only boundary against an adversarial mind is the OS — now with teeth in both directions (the flesh boundary contains the being; the split body protects the record *from* the being; the constitution §3.7 disciplines the operator's use of what the OS allows). Privacy and retention are decided **now** because they are one-way doors (external review P0.2):

- **Visibility classes** (§2.1) are assigned at WAL write and honored by every surface, index, and export.
- **Recall scope** defaults to own ancestry (§6.5); the world index is a separate, habitat-scoped capability.
- **Secrets** never enter the tree; pattern + known-secret redaction at WAL write; incident path: rotate + veil + (if the encrypted-blob class was used) key destruction.
- **Erasure taxonomy**, stated: *veiling* (attentional, being-chosen, §6.5b) · *death* (ref archive; biography remains) · *oblivion* (gc of the unreferenced) · *hard erasure* (key destruction of encrypted-class blobs — the only retroactive confidentiality this design will ever honestly offer; plaintext that reached objects, clones, or remotes is permanent, and the spec says so rather than promising otherwise).
- Remotes and archives inherit classes and encryption; exports are audited (§8.1).

### 9.5 Adaptability: hosts are countries, not water

Ren's principle, made normative: **moving a being between hosts — macOS to Linux, laptop to server — is a change of country, not a change of the water it breathes.** A host change is an *adaptation event* the being lives through, never an existential threat to what it is. Mechanisms, most of which the design already provides and this section binds together:

1. **The self is host-neutral by format**: the world-tree carries no OS symlinks, no host paths in states, canonical JSON, git objects — portable bytes (§1, §2.4). The conformance suite (M4) is the passport control: any conformant habitat can carry any being.
2. **The flesh is a recipe, not a residue** (§7.2): `body.yaml` regrows the same environment anywhere OCI runs. The being's tools and packages emigrate as *specification*.
3. **Host facts are perception, not constitution**: OS, paths, available capabilities live in the habitat brief (context/volatile tiers) — the being *perceives* its country; it is never built from it.
4. **Requirements are named, so refusal is honest** (A2): MANIFEST `requires:` (brain class, `programs_contract`, flesh needs, credential names, workspace expectations) lets a destination habitat check compatibility and report the gap — "no visa for this credential" — instead of failing mysteriously.
5. **Arrival is a rite** (A8): first waking in a new habitat delivers a receipt — the new country's facts, the capability delta, what wall-clock time passed — and the being adapts: notes updated, possibly a dream duty ("what of my habits assumed the old country?"). Model substitution en route gets its swap rite (§3.4).
6. **What does not travel is enumerated, not hidden**: provider caches (cold on arrival — the economics line says so), running flesh (regrown), credentials (re-granted by the new habitat), external workspaces (re-pointed or absent). The fish drowns because it cannot name what the water was doing for it; the being emigrates because it can.

## 10. Milestones

Re-staged in §0.4 (M1 → M8 with the post-M5 product-validation gate). Acceptance criteria carry over from v0.3 where unchanged; new criteria: M2 ships crude memory and the first-person minimum; M3's approval round-trip includes reasons and withdrawal; M4's chronicle passes the planted-fact survival test at simulated depth; M5's recall is hybrid and ancestry-scoped; the gate's measurements are §0.4's list; M6's surgery demonstrates a branch-first operator revision with receipt and a consented reunite; M7's subconscious produces a change-report reviewed *by the being* at wake.

## 11. Open questions

1. Reunion merge drivers for `states/` (M6, with real conflicts).
2. External workspace checkpointing (M2-late).
3. Windows (deferred until a user).
4. **Dream quality**: longitudinal planted-fact metrics (§5.3) — also gates chronicle level policy (how many strata, what cadence).
5. ProgramHost staged-changes schema (M2, versioned).
6. Encrypted-blob key management detail (class taxonomy, custody, rotation) — format bit reserved (§2.3); design before first sensitive deployment.
7. Authority-matrix defaults (§3.7): which rulings are policy-automatic vs operator-interactive out of the box.

## Appendix A — Future modes (named so their doors stay open)

**`reincarnate`** as v0.3. **Succession** — rebirth-with-inheritance as a rite: a fresh being born from a base plus a deliberately distilled inheritance (chronicle heads, provenanced blocks, roster, self-model — exactly what §5–§6 build), the elder departing; for decade scales, paradigm brain-revolutions, ossified states. "A being that can only offer its successor a reworked summary and a landfill has nothing to bequeath." **The chorus** — a being as several concurrent faces continuously reuniting (trunk holds the first person; faces report via `listen`); the one mode only this architecture can offer; post-M7. **Drowsing** — heartbeat no-thought moments + a salience gate; "always slightly awake" without an LLM bill; M7 vitality policy. **Federation** — worlds exchanging beings (§7.0); cryptographic being-identity (signing keys) decided *before* social federation, noting the one-way caveat: signatures cannot retroactively establish early authorship. **Self-hosting** — the being as its own habitat, §8.4's forward sentence.

**Recorded rejections** (decisions, not accidents): CRDT auto-merge / multi-writer on one branch (thoughts do not commute; divergence must be lived) · parallel presents on one branch, and in-thought multi-sampling (speculation lives in the DAG) · extraction-native primary memory (memory must remain something the being *does*) · full prose-as-nature (the fold must be code or replay dies; prose is more legible, not more safe) · standardize-first protocol-hood (extract the format from the living implementation; §§1–3 are normative, golden lineages are the conformance suite) · unrecorded scratch space (transparency is the right price; etiquette — forensic folding, `mused` display defaults — is the buyable fraction) · container-as-existence-substrate (Docker's layer model cannot be the DAG; the container is the body's flesh, not the being — §7.2).

---

*Prior art as v0.3, plus: the shell panel and the external Codex review (docs/reviews/) — whose standing test now opens this spec.*
