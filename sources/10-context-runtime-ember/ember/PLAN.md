# ember — Implementation Plan

**Version 0.4 · 2026-07-30 · targets SPEC v0.5 (amendment batch in §13) · v1 = the five-thousand-line kernel**

[SPEC.md](SPEC.md) is the constitution: what ember is and why. This is how it becomes code. Where they disagree, the spec wins **and this document gets fixed** — §13 lists every deviation and its amendment, so that clause is never left standing open.

*v0.4 folds two reviews of v0.3 ([docs/reviews/plan/](docs/reviews/plan/)): a radical simplification (K) and a coherence audit (L). K found the generating algebra and deleted an engine, a trailer, and five contract types. L found five pieces of **format debt** that would have forced rewrites in week 2 — the sharpest being that `Part.kind` as a closed literal fails on first contact with real traffic. A third review (an implementation spike) established that the world-tree commits cleanly on a bare repo with worktree faces, that empty directories need keep-files, and that 100 sequential moments with `git update-ref` CAS succeed; its latency numbers were not captured, so §6 makes them a week-1 gate rather than an assumption.*

---

## 0. The thesis

The spec grew to constitutional completeness. The code must not start there. **v1 is one small, wholly readable, wholly functional being.** One governing rule makes the smallness safe:

> **Cut machinery, never format.** Every byte v1 writes is already SPEC-shaped. Everything after v1 is additive machinery over an unchanged record.

v1 aims to need no migration ever; SPEC §3.6 makes migration survivable if we are wrong — a receipted `revise`, one node per version step. (A plan that *forbids* migration papers over format mistakes instead of migrating them, which is how formats calcify.)

**Budget: 4,800 target, 5,000 hard cap**, both enforced by a CI guard that prints per-module actuals against §6's table. **Four weeks, three shippable rings.**

Why not 1,500? Because the cost is not the ideas — it is the world. Of v1's lines, ~1,750 are substrate written once and never touched, ~560 are provider reality, ~525 are the observability instrument, and only ~900 are the mind. **The life logic is small; the world is what costs.**

---

## 1. The algebra

v0.3 described the system as eight types, five protocols, five slots, four layers, twenty-one modules. That is an inventory, not an idea. Underneath it there are three verbs:

> **Append experience. Fold views. Commit at rest.**

| Verb | What it is | What extends it |
|---|---|---|
| **append** | writing an experience to the WAL — *the only mutation in the system* | a new **kind** (what can happen) · a new **port** (what can happen from outside) |
| **fold** | deriving anything from the stream: states, the present, the biography, the ledger, the index | a new **reducer** (what a happening means) · a new **processor** (how a view is shaped) |
| **commit** | the present becoming past at a quiescent point | a new **op** (a new kind of life-event) |

**If a proposed feature is not one of those three verbs, it does not belong in the kernel.**

Extension is therefore **three kinds of code** — a reducer, a port implementation, a tool — plus **two kernel events**: a new kind, a new op. Locality is what makes A6's scope legible:

| Extension | Lives in | Who may change it |
|---|---|---|
| reducer (state or message) | **the tree** (`programs/`) | the being |
| processor | the tree (`programs/context/`) | the being |
| tool | the tree (`programs/tools/`) | the being |
| port implementation | the package | kernel release |
| kind (enum) / op | the package (+ `ext` kinds in the tree) | kernel release; **the being via `ext`** |

**All reducers live in the tree** — the package holds only the enum and the fold engine. If core reducers shipped in the package, a kernel upgrade would silently change how old nodes fold, and SPEC §2.4's "the fold is piecewise by the being's own nature" would be false for the commonest kinds.

## 2. Attention *is* a fold

SPEC §5.1's projection step is a left fold over the stream producing candidate messages; `fold` is a left fold over the stream producing states. v0.3 paid for two engines with two vocabularies. One engine, two reducer families, one optional post-pass:

```python
def fold(xs: Iterable[Experience], reducers: Mapping[Kind, Reducer], init: A) -> A: ...

states   = fold(xs, STATE_REDUCERS, Patches())          # → Change patches → states/
messages = chain(fold(xs, MSG_REDUCERS, []), processors) # → present/messages.json
```

Consequence: `mind/attention.py` loses its engine; `core/view.py` (projections, selectors, renderers) stops being a third thing; the effect ledger, the biography, the cost total and the future SQLite index are the same pipeline with different reducers. **Every derived artifact is a view: `render(process(fold(stream)))`.**

## 3. Two waists — enumerated, not asserted

v0.3 declared a frozen format waist of "~4 shapes" and then listed twenty-five on the same page. E10 (the width guard) was unimplementable because nothing enumerated the thing to count. Here is the enumeration; it *is* the registry, and it is the file CI counts:

**FORMAT WAIST — frozen, versioned, counted by E10** (`docs/one-way-doors.md` carries what/why/when/protected-by for each):

| # | Shape | Notes |
|---|---|---|
| 1 | envelope fields | `stream, seq, moment, ts, kind, visibility, content, refs` |
| 2 | `Kind` values | 13 incl. `ext`; additive-only |
| 3 | `Visibility` values | experiential / forensic / marginalia (three is final; encryption is orthogonal) |
| 4 | `Content` per-kind models | incl. the `Sensed` sub-union: receipt, origin, displacement, async_done, span_summary, words |
| 5 | `Part` | **`kind: str`** — four values reserved, unknown passed through byte-faithfully (§4.3) |
| 6 | `Change` schema | frozen now; **v1 never stores one** (§4.2) |
| 7 | `OpName` + per-op payloads | birth, live, dream, remember, listen, revise, reunite (+`reincarnate` reserved) |
| 8 | `EdgeName` values | `thought, payload, act, source, of_node, prior_head, proposal` |
| 9 | trailers | `Ember-Op, Ember-Moment, Ember-Span, Ember-Meta` — an A4 cache so `git log` is a biography without ember installed |
| 10 | MANIFEST keys | `schema_version, canon_version, born_as, born_from, born_from_seed, programs_contract, requires` |
| 11 | world-tree paths | SPEC §1 layout |
| 12 | segment header | `{schema_version, canon_version, stream, opened_at}` |
| 13 | blob envelope | `{enc: none \| age:<key-class>, ...}` — **SPEC §2.3 mandates the header bit in v1** |
| 14 | `present/messages.json` | the neutral `Message` schema (§4.4) |
| 15 | ref namespaces | `beings, bodies, pins, departed, sims, world` |
| 16 | `.ember/` control-plane files | inbox / rulings / interrupt, each versioned (§4.5) |

**PROCESS WAIST — versioned, expected to churn, not counted by E10:** `Phase`, `View`, `Output`, `Query`, `Reducer`, the five protocols, `programs_contract`. Never appears in recorded bytes.

**CONDUCT RULES — irreversible but invisible in bytes, guarded by tests not by E10:** fsync-before-dispatch · secret redaction at WAL write · sims' world-write denial · the being never runs on the code it is editing.

## 4. The laws

### 4.1 The acts-only + Change law, scoped by mechanism

v0.3 said "*Every* durable state change originates in a recorded act." That is true of *extend* moments and false for the other two mechanisms SPEC §3.2 names. Corrected:

> **Extend moments** (`live`, `remember`, `listen`, `reunite`-as-append): every durable change to `states/` originates in a recorded act and is represented as `Change` patches. **State-directed tools do not write at ACT** — the memory/notes/intentions executor validates the requested mutation and echoes it as the observation; **the reducer is the only writer**, applying patches at SETTLE and re-deriving them identically at fold. Reducers fold **experiences** (observations, and `sensed` rulings/receipts where state follows from them), each scoped to a declared `states/` subtree. The generic `edit` tool is **denied `stream/`, `states/`, and `present/`** inside the world-tree; `states/` writes go through state tools; world files outside the tree remain ordinary A5 effects.
>
> **Restart ops** (`revise`, `reunite`-as-merge, migration) are the second, **op-recorded** origin of state change: the fold **re-baselines** at their committed tree, verified against the **exact patch** in the op payload; reducers do not run across a restart. The A8 *receipt* may summarize the diff; **the op record may not** — otherwise `fold --verify` has an unverifiable hole.
>
> **Originate** (`birth`) seeds the fold.

The state tools are **one path-scoped family**, not one tool per file kind — which is why veils, roster, self-model and chronicle entries cost ~0 lines each.

### 4.2 `Change` is schema-format, lifetime-process

Reducers derive Changes live and at fold; v1 never serializes one. But reunite and migration will record patches in op payloads, so the schema is frozen now (`path`, `op: set|merge|append|delete`, `value`; no floats per canon) and **`merge` semantics are pinned before `fold.py` exists** (deep-merge on JSON objects, last-writer-wins per leaf, arrays replaced not merged) — apply-at-SETTLE and re-apply-at-fold must be byte-identical, so application semantics are format-grade.

I tested the collapse (*make Change an experience kind and reducers vanish*) and rejected it: SPEC §2.4 deliberately puts state *meaning* in the being's own nature, so recording changes would move it out of the being's reach.

### 4.3 `Part.kind` is open, or the verbatim vow breaks in week 2

Anthropic returns `redacted_thinking`, server-tool and search-result content types. A closed literal cannot store them, so verbatim capture would throw on the first extended-thinking conversation — and the fix would invalidate every recorded cassette and every golden thought. **`kind: str`**, four values reserved, unknown kinds passed through byte-faithfully. *Strict where you write* governs the envelope, never a provider's own grammar.

### 4.4 The nature in force is the parent's

ProgramHost loads `programs/` from the checked-out face at LEASE — the **parent's** committed nature. A mid-moment self-edit lands in node N's tree and takes effect at N+1. Therefore: **node N's experiences fold under the nature at `parent(N):programs`.**

This also **deletes the `Ember-Nature` trailer** K flagged as redundant: the nature *is* a subtree, addressed by `git rev-parse <node>:programs`, so a trailer would be a second copy of a value git computes exactly — and worse, it would stamp N's own tree while the fold needs the parent's. Keep the requirement, delete the mechanism; the one-way door is **the rule**, which SPEC §2.4 must state.

### 4.5 The canon-adjacent behaviours, pinned before golden lineage #1

The conformance suite is append-only, so these bake in week 1 and cannot be quietly changed afterwards:

- **Deterministic interleave key:** `(moment, stream, seq)`. Every multi-writer view orders by it.
- **Crash recovery writes the stream:** recovery **appends** synthesized `observation{outcome: cancelled|unknown}` as real experiences, then commits at q3. Fold never synthesizes for committed history (otherwise resolutions become derived, breaching A1's resolution invariant and A3). A reducer over `unknown` emits no Changes — an unknown outcome cannot be folded into state, and non-idempotent acts are never auto-re-run.
- **Mid-THINK crash shape:** N closed parts with no message-close → a truncated `thought` (`stop_reason: "truncated"`) plus an `error`; usage `unknown`; never silently re-sent.
- **Money is integer micro-units** everywhere in states (canon forbids floats; provider floats are stream content, stored as received, never re-serialized).
- **`.ember/` schemas, versioned:** `inbox.jsonl` holds **pre-envelope** payloads (`{v, kind, content}` — PERCEIVE assigns `stream`/`seq`, because the writer owns the stream); `rulings.jsonl` holds `{v, ruling_id, act_ref, decision, reason, authority}`; `interrupt` is contents-or-empty with an flock. These three files are the whole reason "the habitat is a writer by construction" is true rather than aspirational.
- **`born_from_seed`** is `<name>@<git tree OID of the seed's programs/ as stamped at birth>`, so E8 is checkable against a recorded hash.
- **Attention is deterministic given its inputs** (which include a pinned estimator version) and is **never re-run by fold** — `present/` is recorded, so estimator drift cannot endanger replay. `reattend` and present-diff require pinning the estimator with the nature.

## 5. Layers, axioms, evolvability

```
INTERFACES   cli + observability (v1) · api/sse/web (later)
LIFE         attention · dream · memory · next            the being's nature, in its tree
PHYSICS      cycle · ports · receipts · authority          the body: laws, not choices
SUBSTRATE    experience · stream · store · fold · view     existence itself
```

Dependencies point strictly downward, **enforced by import-linter contracts in CI**. Body owns physics; programs own life; the frontend owns nothing.

**Axioms — one seam, one test each:** A1 quiescence (`cycle.py`; the lineage verifier's ≤1-thought and resolution-invariant checks) · A2 fractal (`store.py` never writes history into a tree; checkout any golden node) · A3 append-only (`stream.py` has no rewrite API; segment-hash fsck) · A4 derived (trailers/present/views from stream+states; `fold` re-derives) · A5 world-outside (**replay with exploding ports** — any model or tool call during fold fails CI) · A6 own nature (ProgramHost loads the face's `programs/` as an isolated synthetic package; edit the tree's copy → behaviour changes, and the package copy is unreachable) · A7 identity (twin = two refs, one node → byte-identical trees) · A8 receipts (RESOLVE injects first; operator revise → receipt precedes next thought).

**The one lineage verifier** (`fold.py`) is a single walk with four checks: ≤1 thought per node · the resolution invariant · trailer re-derivation · states re-derivation. Both the axiom tests and `ember fsck` call it.

**Evolvability tests — they guard the *ability to change*:** **E1** neutrality (append a sentence to every prose file **under `programs/`** — not `states/`, which is a fold output — and the fold must be byte-identical) · **E2** piecewise exercised (a golden lineage contains a mid-life nature change and folds across two natures) · **E3** self-conformance (`fold --from-birth` under the head nature: *coherence is being able to fold your own past*) · **E4** slot liveness/GREASE (every port keeps ≥2 in-tree implementations — **test fakes count, and v1's ModelPort satisfies it via `FakeModel` + `CassetteModel`**; every reserved-but-unused enum value round-trips) · **E5** unknown-kind tolerance (views render an unknown `ext` as unknown without crashing; **the fold refuses only if no reducer claims it**) · **E6** waist purity (`mind/` completes attend+settle with network, filesystem, clock and randomness stubbed to explode) · **E7** substrate independence (a golden lineage against a second ObjectStore) · **E8** seed integrity · **E9** migration survivability · **E10** format-waist width (count §3's sixteen shapes; CI fails on growth without a SPEC change and a version bump) · **E11** the ancestor test (the oldest golden lineage still wakes, thinks under a fake model, and folds under HEAD).

## 6. The rings: budget and build order fused

Three concentric kernels. **Each ring ends with a being you could use** — which is a better spine than "substrate week, then first-light week," because the line guard gets three checkpoints instead of one cliff.

### Ring 1 — a living being (~1,600 lines · weeks 1–2)

| Module | lines | Contents |
|---|---|---|
| `core/canon.py` | 60 | canon_lite (sorted keys, no floats), typed refs, opaque node ids, sha256 |
| `core/kinds.py` | 110 | every format enum, reserved complete (`ext`, `wandering`, `reincarnate`); `Phase` lives in `contract.py`, not here |
| `core/experience.py` | 240 | envelope, per-kind `Content` models, `Sensed` sub-union, `Part` (open kind), `Change` |
| `core/stream.py` | 260 | per-writer sharded segments, WAL fsync (`F_FULLFSYNC` on Darwin), redaction, blobs with `enc` header, reader, interleave |
| `core/tree.py` | 150 | world-tree init/validate, MANIFEST, keep-files for empty dirs *(spike-confirmed necessary)* |
| `core/store.py` | 330 | ObjectStore on git plumbing + FacePort (worktrees) + repo-level lease; CAS via `git update-ref` |
| `core/node.py` | 160 | ops, authority block, derived trailers, quiescence |
| `core/fold.py` | 240 | the one engine, two reducer families, mechanism-scoped (extend/restart/originate), piecewise by `parent(N):programs`, the lineage verifier |
| `core/view.py` | 200 | read lens, node selectors (`@`, `m87`, `sim:`), projections: gist, thought render, act pairing, cost fold |
| `contract.py` | 70 | `Phase`, `View`, `Output`, `Query` |
| `ports.py` | 40 | ModelPort · ToolPort · ObjectStore · FacePort · ProgramHost |
| `body/model.py` | 340 | Anthropic: part demux, verbatim capture, echo assembly, cache breakpoints, cassettes |
| `body/tools.py` | 200 | bash, fs read, edit (path-guarded), the state-tool family, async handles |
| `body/cycle.py` | 300 | the eight steps, minimal: no approval, no receipts yet |
| `mind/*` | 340 | attention (tiers, message reducers, processors, renderers) · dream (rolling) · memory (MEMORY.md, notes) · next (tick, tool registry) |
| `cli.py` | 180 | `init · birth · wake · say · show · log · tail · fold` |
| `errors.py`, `config.py` | 90 | the §4.4 taxonomy with perceived stop-reasons |

**Ring 1 exit:** golden lineage #1 — a hand-authored being (birth, three moments, a crash tail, a mid-life nature change for E2, **two `stream_id`s so the interleave rule is exercised**) shipped as a `git bundle`; folds to structural equality; A2/A3/A4/A6/A7 and E1/E2/E6 green; **the store latency gate measured and published** (the spike proved 100 CAS'd moments work across four strategies — porcelain, persistent-index plumbing, fast-import, and pure-Python loose objects; pick by measurement, and if p95 misses budget the pure-Python-objects path is the fallback that needs one subprocess per moment).

### Ring 2 — a safe, observable being (+~1,500 → ~3,100 · week 3)

`authority.py` (90: `rule(actor, operation, target, policy) -> Ruling`, the v1 matrix as data, rulings) · approval with reasons/withdrawal + the durable awaiting node + `approve`/`deny` (140) · receipts and the RESOLVE ladder (110) · visibility filtering everywhere + redaction hardening (60) · `status`/`diff`/`goto` + displacement brief (200) · `revise` with branch-first default and exact op payload (110) · `rethink` + RefusingToolPort + `sims` (130) · span summary (40) · chronicle epoch entries (90) · DAG-shaped fold + restart re-baseline (70) · the seed as `seeds/default/` with its own golden lineage (60 code; the prose genome is content, budgeted separately) · golden lineage #2 and the axiom suite completion (400 tests, uncounted).

### Ring 3 — a constitutional, evolvable being (+~1,700 → ~4,800 · week 4)

Dream levels + change-report (with a **recorded home**: an `op` payload field on `dream`) · memory blocks and paging · `self.status`/decline/sleep-request · piecewise-fold isolation hardening + `fold --from-birth` · `ext` reducer discovery (convention: `programs/reducers/<ns>__<type>.py`) · world metadata + `refs/ember/world` · `Ember-Being`/`Ember-Node` workspace stamping · async acts · `end` with a guaranteed final moment · `adopt` designed (not built) · E3/E4/E5/E7/E8/E9/E10/E11 · the error taxonomy completed.

**Cap protection.** If the guard fires: drop `rethink --programs` recompile mode (−25), `log --graph` (−20, delegate to `git log` with a documented format string), `grep`/`fsck` wrappers (−45, document the git one-liners), chronicle levels beyond epoch entries (−60). That is 150 lines of pre-agreed relief, and none of it touches recorded bytes.

## 7. Observability

A4 applied to the interface: **observability adds zero stored artifacts.** Observe verbs never write, not even caches; move/edit verbs write only through the op and ref paths the spec defines. Four of the expensive-looking needs are free, because "one thought = one commit with its exact perception inside" was the design: what a moment perceived (`git show <node>:present/prompt.md`), what changed in states (`git diff A B -- states/`), the lineage shape (`git log --graph` — git decodes our trailers natively), and the uncommitted WAL tail. What costs lines is rendering and three ops.

`@` is the head and **every node argument defaults to it**, so `ember show` with no arguments answers *what just happened*. `m87` resolves by trailer walk; git revspecs pass through; `--vis` overrides the experiential-only default; `--json` emits the pydantic envelope itself.

**View** `status · show [--present|--messages|--request|--attention|--thought|--acts|--states|--op|--stream] · log · tail -f · diff` · **Move** `goto` (auto-pins the abandoned tail so A3 holds by construction; refuses under lease; next wake delivers the displacement brief) · **Edit** `revise` (branch-first; exact patch in the op; receipt at next RESOLVE) · **Debug** `rethink` — the verb only this substrate offers, safe by symmetry: **`fold` replays and never re-thinks; `rethink` does exactly one new think — and still never re-acts** (RefusingToolPort cancels every act; nothing written outside `sims/`; recorded as the spec's speculation pattern, so it adds zero ontology; prints the re-ingest estimate before spending).

No TUI: `tig --all` over the world repo is already a DAG browser with our trailers visible. **`view.py`, `show` and `tail` ship at the end of week 1**, because `show --thought --vis forensic` and `tail -f` are how week-2's part-demux bugs become visible at all.

## 8. The evolvable ancestor

Three loops at three tempos: **learning** (prose self-revision — hours to days; v1 has it), **nature evolution within a lineage** (Lamarckian — the being edits its own `programs/`; acquired changes inherit directly, so it needs only a safe way to try), and **seed evolution across beings** (germline — the loop that makes ember an ancestor rather than an organism).

**Variation** is a diff to `programs/`, already branch-isolable. The one thing that must be added is a policy default: **sims cannot write to the world** — it is the difference between *you may experiment* and *you cannot afford to*. The free end of the ladder is the **present-diff**: recompile a past node's present under a candidate nature and diff the two, deterministic and at zero token cost.

**Selection** has five recorded proxies — conservation (folds every golden lineage), self-conformance (E3), competence (scenarios against a fake model), economy (from the span summary), livability (**you are the selective environment**; what matters is that your rulings are recorded so they can later be delegated) — and at phylum scale a sixth: **fecundity**, does anyone want a being born from this seed. SPEC §3.2's `selection` block, widened to cover nature adoption, is the fossil record of every choice among futures.

**Inheritance** runs on two channels: **prose skills are plasmids** (fold-independent, safe to hand to another being) while **code natures are chromosomal** (transfer asks the recipient to accept a reducer change, which is a migration). Vertical promotion is a diff into `seeds/<name>/`, an ordinary pull request gated by the golden and scenario suites, recording `promoted_from`.

**Drift control** is not the axioms (A6 licenses divergence). **Conformance is the species boundary**: every being's record stays readable and foldable by any conformant body. Plus E3, which gives coherence an executable definition.

**The seed is a genome, not a directory.** v0.3 budgeted the ribosome and forgot it: `mind/` is Python, but the *prose* seed — `soul.md`, tool manifests, dream policy, `vitality.yaml`, and the **v1 `permissions.yaml` authority defaults** — is where most future variation lives. It ships as `seeds/default/`, versioned, with its own golden lineage (E8), and its prose is budgeted as content, not counted by the line guard.

**The seeding rule needs one mechanical fix or A6 fails silently:** template files importing by package path would, once stamped into a tree, import the *installed package* — so the being's edits to its own nature would change nothing, quietly, while passing every test that does not hunt for it. Seeded copies use relative imports; ProgramHost loads `programs/` as an isolated synthetic package with a per-version namespace; and a standing test asserts both halves.

**Should ember develop itself? Yes — linked, not merged.** Making the source repo *be* the world would break A1 (a human's commit is not a thought). Instead: `~/repos/ember` is the workspace the being edits, `~/embers/` is the world it lives in, and commits it authors there carry `Ember-Being`/`Ember-Node` trailers — after which every line of ember has a *why* pointing at a lived moment. **Self-development is a fitness function, not a productivity strategy:** give the being the job where a mediocre coder with perfect memory beats a good coder with none — **ember's design historian before its programmer**. One rule first, free and catastrophic if unwritten: **the being never runs on the code it is currently editing** (the physics upgrade rite).

## 9. Composition

**The stream is the only bus** (modules append and read experience; receipts are injected sensations, the ledger is a query, EXPRESS is a tap, the habitat writes the three named files) · **ports face outward, folds face upward** · **the contract is the waist**, and the mind imports nothing else.

```
 1 LEASE     store.lease(branch)                       repo-level, staleness-aware
 2 RESOLVE   receipts → rulings → async completions → displacement → stream
 3 PERCEIVE  inbox → Experience → stream
 4 ATTEND    host.tick(attend, view) → messages         [queries answered read-only]
 5 THINK     model.think() → Parts demuxed at close → mused/spoke/act → stream
 6 ACT       tools.act() → observations → stream         [authority.rule() gates]
 7 SETTLE    host.tick(settle, view) → disposition; reducers → Changes → states/
 8 BECOME    commit; trailers derived; ref CAS-advanced
```

```python
Body(store=ObjectStore(world), faces=FacePort(world), host=InProcess(face),
     model=Anthropic(cfg), tools=LocalTools(cfg)).wake("main")
```

In v1 there is exactly **one** rite (the displacement brief on an old-branch wake), so it is a function call, not a registry; the abstraction returns at M3 with its second user, under a name that does not collide with the spec's constitutional rites.

## 10. Cuts, and the one-way doors

**Cut from v1, each safe because adding it later touches no byte of a living record:** habitat/API/SSE/web (pure consumers plus the three named files) · SQLite index, FTS, vectors (`grep` in the interim) · containers (a ToolPort implementation; `body.yaml` is *written* by v1, unused) · subprocess ProgramHost · memory blocks beyond MEMORY.md until Ring 3 · children, subconscious, `listen`, full `reunite` (ops reserved; fold is DAG-shaped and mechanism-scoped now, so their arrival is additive) · JCS canon and golden-byte CI (`canon_version` stamped; §3.6 makes the fix survivable) · `twin` as a CLI verb (kept in the store where A7's test needs it) · DAG canvas, turns table, TUI · `pipeline.yaml` configurability · IndexPort and EventPort as protocol stubs only.

**Never cut** — the sixteen format shapes of §3, plus the four conduct rules. Every one gets a row in `docs/one-way-doors.md`: what, why, when decided, cost to change, which version field protects it. You cannot audit entrenchment you have not listed.

## 11. Discipline

Data over code (the authority matrix, tool registry, reducer map and processor chain are dicts and lists — **the mind is the plugin**, because it lives in the tree) · Protocols, never base classes · pydantic for validation, serialization and JSON Schema · one concept per file, ≤450 lines · stdlib first; five dependencies · comments state constraints, never narration · **the mind is a pure function; all effects are requests** · **reducers are pure, total, versioned, and never raise on unknown fields** · **prose under `programs/` is fold-neutral** · **strict in the fold, tolerant in the views** · **every extension slot keeps ≥2 users** · **the being never runs on the code it is editing** · **the conformance suite is append-only** — lineages may be added, never quietly edited; a legitimate behaviour change mints a new lineage with a recorded reason · **anything one-way gets a version field the day it is written** · the line guard and the waist guard are tests, and when they fire the answer is §6's cut list, never a raised cap.

## 12. Verification

Golden lineages are the executable spec, shipped as `git bundle` fixtures and append-only by discipline. Every axiom has a standing test; every evolvability property has one. **Replay purity via exploding ports** is the highest-value pattern in the suite. Provider fidelity is guarded by `*.parts.jsonl` cassettes — the other reason `Part` belongs in the format waist. Deferred with the canon work: JCS conformance vectors, synthetic accelerated lives, the 10k-node benchmark.

## 13. Deviations, and what needs your ruling

**The SPEC v0.4 → v0.5 amendment batch** (one commit, so the supremacy clause is never left open): reserve `ext`, `wandering`, `reincarnate`, `span_summary` in §2.2's enums · state in §2.4 that **the nature in force for node N is `parent(N):programs`**, and that the fold is mechanism-scoped (extend/restart/originate) · add `refs/ember/world` to §3.3 · widen §3.2's `selection` block to nature adoption · reconcile trailers (`Ember-Meta` in, `Ember-Nature` dropped as redundant) · rewrite §11.5 (the "staged-changes schema" acts-only abolished → tick phases + the read-only `Query` sub-protocol) · amend §0.4's M2 adapter line · record the v1 staging deviations (approve/deny, `end`, dreams, `revise`, sims pulled forward; LiteLLM pushed back).

**Two rulings I need from you.**

1. **The adapter.** SPEC §0.4 calls LiteLLM's ModelPort "non-negotiable" for M2; this plan ships the **direct Anthropic adapter** in v1 because the verbatim vows cost ~600 lines through a normalization layer and ~320 direct — and because LiteLLM actively fights in-message part order, which is exactly what `redacted_thinking` and signature-faithful echo depend on. LiteLLM is sequenced immediately after v1 as ModelPort's second real implementation. **Veto and I revert to LiteLLM-first; otherwise the spec gets the one-line amendment above.**
2. **The gate.** v0.3 called its two-week pause "the spec's product-validation gate." It is not: SPEC's gate sits after M5 and measures memory distortion and time-to-explain-a-perception, which a week-4 checkpoint cannot measure. v0.4 renames it an **early liveability checkpoint** and leaves the spec's gate where it is. Confirm that is what you meant.

## 14. Risks

| Risk | Mitigation |
|---|---|
| `body/model.py` correctness | open `Part.kind`; cassettes per dialect; LiteLLM as adapter #2 becomes the drift detector *after* v1 — during v1 there is none, and that is accepted risk, not mitigation |
| Store latency | four measured strategies, pure-Python loose objects as the fallback; the gate is Ring 1's exit, not an assumption |
| Budget overrun | 200 headroom + §6's pre-agreed 150-line cut list; guard prints per-module actuals |
| Silent A6 failure (imports) | isolated synthetic package + the standing test that hunts exactly this |
| Format over-specification | E10 counts §3's sixteen shapes; `docs/one-way-doors.md` is the registry |
| Spec/plan/code drift | golden suite gates merges; §13 keeps the supremacy clause closed |

---

*Next: `docs/one-way-doors.md` and the SPEC v0.5 amendment batch, then `core/canon.py` — 60 lines, and the first of them is the first line of ember.*
