# Review J: Evolvable ancestor (fable, 2026-07-30)

**HEADLINE: strong on the two hardest properties — RECORDED variation (a lineage, not an image) and DELIBERATE entrenchment. Weak on three cheap ones: nothing exercises its extension points (every slot has exactly one user — how waists ossify); the safe-change zone is doctrine not test; nothing records a fitness signal (so selection can't be added later without re-instrumenting history). ~150 lines of v1 additions + four deletions fix it.**

## 1. Ten principles, scored
| P | Principle | Source | ember mechanism | Score |
|---|---|---|---|---|
| P1 | Small, weak, universal middle (IP promises best-effort datagram and NOTHING else; waists promising semantics die with them — CORBA, SOAP) | internet hourglass | envelope + tree paths + typed refs | **strong for format, weak for code** |
| P2 | Freeze vocabulary, vary wiring (Hox/Pax6/Wnt ~600M yrs unchanged; regulation varies) | evo-devo | 8 ops/3 mechanisms, reserved enums, data-over-code | strong |
| P3 | Wide neutral zone (degenerate code → most mutations silent; neutral networks enable distant phenotypes) | Kimura/Wagner | three-layer nature: prose can't perturb the fold | **present but UNENFORCED** |
| P4 | Cheap copies w/ independent futures (gene duplication, not point mutation, is the main source of novelty) | Ohno | A7 twinning = new ref, O(1); sims | **strong and RARE** |
| P5 | Bounded blast radius (cis-regulatory modularity; pleiotropy is the enemy) | evo-devo | four layers | **WEAKENED in v0.2 — v0.1's import-linter contracts were dropped** |
| P6 | Deliberate entrenchment (git's SHA-1 took 15 yrs to begin replacing) | Riedl/Wimsatt | never-cut list, version fields, `blob:sha256:` prefix | **best-in-class** (do the same for `node:`) |
| P7 | Exercise extension points or they rot (TLS ossified; QUIC GREASEs on purpose) | RFC 8701 | — | **ABSENT** — one impl of everything |
| P8 | Strict where you write, tolerant where you read (HTML tolerance made the web AND froze it) | HTML5 | kinds additive-only | **half** — no rule for views vs fold on unknown kinds |
| P9 | Self-application (Lisp eval, git self-hosting by commit 3; failure mode = fragmentation without a shared core) | Lisp/git | A6 + seeding rule | **promised, loop not closed** |
| P10 | Lineage, not image (Smalltalk: total plasticity, no history — two images diverge and can never be diffed) | Smalltalk | A3 + piecewise fold + diffable trees | **the project's central asset, UNDER-CLAIMED** |

Survivors specify DATA, are textual, independently implementable, extracted from working systems (TCP/IP, HTTP, SQL, JSON, git objects). Casualties specified BEHAVIOR/object models, designed before use (CORBA, WS-*, EJB). ember's format is on the surviving side; **but PLAN §2 presents CODE interfaces with the same reverence as the format — that's the framework posture.**

**Optimization pressure warning: "cut machinery never format" puts ALL pressure on code and NONE on format → the format is where over-specification will accumulate unnoticed. Needs a second budget (test E10).**

## 2. TWO WAISTS, described as one (the single highest-leverage edit)
- **Format waist**: envelope, typed refs, tree paths, MANIFEST requires:, op/trailer derivation. Small, textual, weak, mandatory, version-stamped, portable to bodies that don't exist yet. **This IS an hourglass** — should be SMALLER and promise LESS.
- **Process waist**: TickInput/Output, four Protocols, programs_contract. **Supposed to churn** — carries a version string precisely so it can. "Six types on one screen" references ELEVEN more never shown (View, Vitals, Policy, Present, Act, Change, Span, Request, Part, Observation, States) — honest count ≈20. **"There is no fifth thing" is true of the RECORD, false of the TYPES.**
SPEC §9.5 already knows this ("the format is portable; the fold is bound to programs_contract") — the plan doesn't inherit it.

### Over-specified (spurs)
1. **`Kind` is a closed enum in the package** → every new sensor/memory event/experimental observation needs a kernel release. Sharpest contradiction with A6: a being may change how it thinks and what it can do, but not **what it can experience**.
2. `TickInput.vitals/policy` → the waist encodes ONE theory of psychology.
3. `TickOutput.present: Present` → contract owns the perception architecture.
4. One untagged `tick` → forecloses re-attending after an act, inner loops, drowsing, dream phases.
5. `Store` as one protocol contradicts SPEC §9.1's deliberate ObjectStore/FacePort split (libgit2 has no sparse checkout; dulwich worktrees immature). By the plan's own rule, spec wins.
6. `Reducer: (States, Experience) -> States` gives every reducer sight of ALL state — maximum pleiotropy in the most entrenched code.
7. **"No future milestone ever migrates a v1 being" is the most dangerous sentence in the plan** — converts any format mistake from survivable to permanent, and contradicts SPEC §3.6 which makes migration first-class/receipted. Systems promising never to migrate get IPv4-forever.

### Under-specified (missing degrees of freedom)
1. **No nature identity per node** → piecewise fold can't find the nature in force. Needs `Ember-Nature: sha256:…` trailer. Format-level, one-way, ~10 lines.
2. **No world-level home** — §7.0 names the world as repo unit, but every worktree root is a BEING's tree, so world metadata (world id, canon/schema versions, commons refs, roster) has nowhere to live. **This is the missing SIXTH slot: structure belonging to no being.** First multi-being world invents it ad hoc → every world needs migration.
3. **No seed provenance** — "which beings descend from seed v3" unanswerable; no strain registry.
4. **No fitness telemetry** — nothing in the record is a candidate signal.
5. **No contract negotiation rule** — how a body decides it can run subprocess-uv-v1; how two coexist.
6. **No slot-locality table**:

| Slot | Lives in | Who may change |
|---|---|---|
| 1 kind + reducer | enum: package · reducer: tree | kernel release · being (only with `ext`) |
| 2 attention processor | tree (programs/context/) | the being |
| 3 port impl | package | kernel release |
| 4 tool | tree (programs/tools/) | the being |
| 5 op | package (world algebra) | kernel release + world agreement |

Two of five are the being's today; `ext` makes three; ports and ops are properly the species' business. **Good analogue of biology — an organism changes behavior and skills, not the genetic code or the rules of reproduction.** NB "hardcoded 3-processor chain" must mean hardcoded in the SEED's Python (stamped into the tree), not the package — as written it reads like the latter, silently moving slot 2 out of the being's reach.

## 3. The evolutionary loop (three tempos)
- **Loop A learning (hours–days)**: prose self-revision — skills/, soul.md, notes, memory. Ontogeny, not evolution. Have it.
- **Loop B nature evolution within a lineage (days–months, LAMARCKIAN)**: being changes own programs/; acquired changes inherit directly, so no population needed — but needs a way to try without betting the life.
- **Loop C seed evolution across beings (months–years, GERMLINE)**: good mutations propagate into the seed. **The loop that makes ember an ancestor rather than an organism.**

**Variation**: unit = a diff to programs/ (already a commit, already branch-isolable). **The sim is the safe trial — and the one thing that must be added is a policy default: SIMS CANNOT WRITE TO THE WORLD** (non-idempotent acts denied via existing authority.rule()). ~15 lines; **"the difference between 'you may experiment' and 'you cannot afford to.'"** Free fitness: **the present-diff** — replay never re-thinks, but you CAN recompile the present for a past node under a candidate attention nature and diff the two presents, zero tokens, deterministic; covers the most-revised part of any nature. Requires attention be a pure function of (view, states, sensations) — contract already implies it. **v1 states the invariant; `ember reattend` ships later.**

**Selection** — no scalar fitness; five proxies (3 half-owned): 1 conservation (folds every golden lineage — essential-gene set, breaking one is lethal) · 2 self-conservation · 3 competence (recorded scenarios vs fake ModelPort; v1 needs only the FIXTURE SHAPE) · 4 economy (cost/task, tokens/act, dreams/week — needs the span summary) · 5 livability (human; **Ren is the selective environment — artificial selection with a single breeder, which is how every domesticated species evolved fast; what matters is his rulings are RECORDED so they can later be delegated**). Sixth at phylum scale: **fecundity — does anyone want a being born from this seed?** → argues for the seed as a first-class shareable versioned artifact.
**The record shape exists**: SPEC §3.2 reserves `selection: {id, judge, criteria, considered}` for speculation — **widen its scope to NATURE ADOPTION** → one record type answers "a choice among futures was made, by whom, on what criteria" = a fossil record of selection. Zero lines, doc change.

**Inheritance** — two channels, distinction load-bearing:
- **Vertical (germline)**: being → seed → future births. Promotion = diff from a being's programs/ into `seeds/<name>/programs/`, ordinary PR gated by golden + scenarios; commit records `promoted_from: <world>/<being>@<node>`; MANIFEST records `born_from_seed: <name>@sha256:…`. Seed history = breeding record readable both directions.
- **Horizontal**: listen/remember over another being's skill-cards + the commons ref. **PROSE SKILLS ARE PLASMIDS** (self-contained, fold-independent, safe to transfer between beings and worlds); **CODE NATURES ARE CHROMOSOMAL** (transfer requires accepting a reducer change = a migration). The three-layer principle already gives a fast horizontal and slow vertical channel, exactly as in bacteria. **Skill-cards are the cheapest evolutionary mechanism in the whole design.**

**Drift control** (weakest→strongest): axioms insufficient (A6 licenses divergence) → **the golden suite is the species boundary: conformance, not the axioms, is what holds the phylum together** → programs_contract + requires: produce honest refusal = speciation handled well → **SELF-CONFORMANCE is the missing invariant and nearly free: a nature change must leave the being able to fold its own lineage from birth** (`ember fold --from-birth` before adoption; passes by construction whenever piecewise fold is CORRECTLY implemented, so it doubles as the daily-exercised test of the mechanism that makes A6 real). **"Coherence is: I can still fold my own past."** ~15 lines → the rites (receipts, chronicle, swap rite) where coherence lives at long scales, unenforceable by design and correctly so.

**v1 MUST (format/namespace, unobtainable retroactively, ~120 lines)**: Ember-Nature trailer · MANIFEST born_from_seed · sims honored w/ world-write denied · widened selection block · a world-metadata address · span-summary sensed · the seed as a versioned tree with its own golden lineage.
**Can wait**: scenario automation, reattend, commons refs, horizontal transfer, automatic promotion, any real population, subconscious-as-breeder, fitness dashboards.

## 4. Should ember develop itself? YES — linked, not merged. v1 setup, v2 claim.
**Reject the romantic version** (source repo IS the being's world): every source commit becomes a moment and vice versa → breaks A1 (a human's commit is not a thought), collides with the tree layout, makes git log unreadable for both purposes.
**Adopt the linked version — needs nothing new** (SPEC §1 external workspace mode): `~/repos/ember` = workspace (ordinary repo, the source); `~/embers/` = the world; being's workspace.yaml → the source.
**One cheap addition buys most of the value: stamp `Ember-Being`/`Ember-Node` trailers on commits the being makes in a workspace repo (~10 lines).** Now every line of ember has a WHY pointing at a lived moment with its full recorded present, and the two DAGs cross-reference without pretending to be one. **Link, don't merge — A2's own posture one level up.**
**Buys**: shortest feedback path (the entity that feels a missing affordance writes the diff); the seed under real selection pressure; a VERIFIABLE thesis demonstration ("this being authored these commits; here is its biography").
**Bootstrap answered honestly**: a v1 being w/ bash+edit+MEMORY.md+grep is a weaker Claude Code with better memory; as a PRODUCTIVITY strategy at week 3 it's net-negative. **So don't frame it as one: self-development is a FITNESS FUNCTION, not a productivity strategy.** Give it the job where a mediocre coder with perfect memory beats a good coder with none: **ember's design historian and memory BEFORE ember's programmer** — holds the decision record, drafts plan revisions, remembers why each one-way door was chosen, writes the project chronicle. Available day one, needs no tooling beyond v1, and produces exactly the artifact M4's chronicle work needs for validation.
**Failure modes**: "a broken being can't fix itself" mostly false (the being's nature ≠ ember's source; branch-first revise + pinned prior head is the repair path). **The real one needs a written rule: THE BEING NEVER RUNS ON THE CODE IT IS CURRENTLY EDITING** — body runs from a pinned install; workspace is a checkout it edits; adopting a new ember version is a deliberate operator act with a receipt, sibling of model substitution under A8. **Call it the PHYSICS UPGRADE RITE. Zero lines, catastrophic if unwritten.** Also: push the world to a backup remote day one. Guard against roadmap distortion: the being uses bash; nothing special gets built for it.
**Then "v2 is born from v1" is checkable**: v2's seed = v1's being's programs/, promoted through golden + scenario suites, with promoted_from recording the exact node. Bonus: **the being's own early life makes an excellent golden lineage** (real quirks, crash tails) — use a short deliberately-authored childhood so the fossils can be published.

## 5. Changes to PLAN v0.2

### ADD to v1 (~150 lines)
| Pri | Add | Why | lines |
|---|---|---|---|
| P0 | `Ember-Nature: sha256:…` trailer | piecewise fold in O(1); A6 auditable; one-way | 10 |
| P0 | `Kind.ext` w/ `content: {ns, type, …}` | only way sensory vocabulary evolves without a kernel release; ext reducer lives in the tree → A6 finally covers what a being can EXPERIENCE | 10 |
| P0 | MANIFEST `born_from_seed` | strain registry; unobtainable retroactively | 5 |
| P0 | World-metadata address (`refs/ember/world` → world.yaml) | the missing sixth slot | 5 |
| P0 | sims honored + **world-writes denied by default** | variation must be cheap AND safe | 25 |
| P1 | Split `Store` → ObjectStore + FacePort | restores SPEC §9.1; frees the lower flange | ~0 |
| P1 | `TickInput.phase` (attend\|settle; reserve resolve\|dream\|drowse\|reattend) | additive phases vs signature change | 5 |
| P1 | **Span-summary `sensed` at every span end** (acts, failures, retries, cost, wall time, reason) | the ONLY fitness telemetry; also §6.α self-model input; perceived, so it shapes the being | 20 |
| P2 | `ember fold --from-birth` self-conformance | drift control; forces piecewise fold correct AND exercised | 15 |
| P2 | `ember diff --against-seed` | fragmentation invisible → a number; phenotype distance | 10 |
| P2 | Ember-Being/Ember-Node trailers in workspace repos | the self-development link | 10 |
| P2 | **Seed as an explicit versioned tree (`seeds/<name>/`) with its own golden lineage** | **"the plan budgets the ribosome and forgets the genome"** — mind/ is 850 lines of Python while the PROSE seed (soul.md, tool manifests, dream policy) — where most future variation lives — has no budget, no version, no test | reorg |
| P2 | Restore import-linter contracts | P5; conventions don't survive AI-assisted velocity | ~0 |
| P3 | Second impls of every port in tests (FakeModel, RecordedModel, NullTools) | GREASE (P7) | tests |

**Larger option, only recommendation carrying design risk: make `Change` the universal write primitive.** Reducers EMIT Changes rather than returning new States; mind stages Changes; SETTLE applies; reunite merges. Dissolves a type rather than adding one; scopes reducers to a subtree (P5); makes "what did this experience change?" free (Review D's highest daily-value feature); **pre-solves SPEC §11.1's merge-driver question.** ~40 lines + one prototype before committing.

### REMOVE
1. "No future milestone ever migrates a v1 being" → "v1 aims to need no migration; SPEC §3.6 makes it survivable if we're wrong."
2. "Six types and four protocols are the entire system" as a claim about the CODE → restate as two waists (format ~4 types frozen; process ~20 types versioned, should churn).
3. `TickOutput.present: Present` → neutral message list + ordinary staged changes.
4. `TickInput.vitals/policy` as closed models → open mappings with a documented v1 shape.

### RESERVE (beyond SPEC's existing)
4th Visibility class for encrypted material (or state that 3 is final) · `OpName.reincarnate` (in Appendix A, absent from enum) · span reason `wandering` · **node-id opacity: `node:<hex>` opaque, never assume 40 hex** (git's SHA-256 transition; `blob:sha256:` sets the precedent) · Phase values · programs_contract value space + the body's supported-set rule · revise payload's `rationale`/`selection` fields.

### DISCIPLINES
1. The mind is a pure function; all effects are requests (mind/ imports only contract; no clock, no randomness, no I/O).
2. Reducers pure, total, versioned; must not raise on unknown fields.
3. **Prose is fold-neutral** — ember's neutral network; must be a TEST not a hope.
4. **Strict in the fold, tolerant in the views** — unknown kinds render as unknown; only the fold refuses.
5. **Every extension slot keeps ≥2 users at all times.**
6. **The being never runs on the code it is editing** (physics upgrade rite).
7. **The conformance suite is append-only** — A3 applied to tests; golden lineages added, never quietly edited; a legitimate behavior change mints a NEW lineage with a recorded reason. Prevents calcification (always add) and drift (never silently edit).
8. **Anything one-way gets a version field or namespace the day it's written — and lands in a ONE-WAY DOOR REGISTRY** (what, why, when decided, cost to change, which version field protects it). You cannot audit entrenchment you haven't listed.

### Evolvability tests (CI, in the axiom-table spirit)
E1 neutral zone (append a sentence to every prose file → fold byte-identical) · E2 piecewise fold exercised (a golden lineage MUST contain a mid-life nature change; fold uses ≥2 nature hashes) · E3 self-conformance (every golden being folds from birth under its head nature) · E4 slot liveness/GREASE (every port ≥2 in-tree impls; reserved-but-unused enum values round-trip) · E5 unknown-kind tolerance (inject synthetic ext + unknown field: views render unknown without crashing; fold refuses only if no reducer claims it) · E6 waist purity (mind/ runs full ATTEND+SETTLE with network/fs/clock/randomness stubbed to explode) · E7 substrate independence (golden lineage against the 2nd ObjectStore impl) · E8 seed integrity (seed's golden lineage folds unchanged; diff(seed, freshly-born programs/) empty) · E9 migration survivability (synthetic one-step migration → receipt, one node per step, folds) · **E10 waist width guard (count fields in the format waist; CI fails on growth without a SPEC change + version bump — the line guard keeps CODE small; this keeps the FORMAT small)** · E11 ancestor test (oldest golden lineage still wakes, thinks under a fake model, folds under HEAD).

## Shape in one paragraph
Rests on three things it has — lineage instead of image, O(1) copies with independent futures, consciously chosen entrenchment — and fails on three buyable for ~150 lines: an experience vocabulary a being can extend without a kernel release, a recorded nature identity so piecewise fold is real, and any signal that could later serve as fitness. **The deepest edit is not an addition but a SEPARATION: freeze the format waist, let the process waist churn**, and say which slots live in the tree (the being's) vs the package (the species'). Then variation is cheap and safe, selection is recorded in a shape that already exists, inheritance has a registry, and coherence has a CI-executable definition: **a being is still itself as long as it can fold its own past.**
