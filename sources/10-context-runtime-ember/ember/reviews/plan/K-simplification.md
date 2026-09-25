# Review K: Radical simplification of the kernel (Opus 5, 2026-07-30)

*Written in-session after Fable reviewers hit repeated server errors and agent spawning became unavailable. Same mandate: find the smaller idea underneath PLAN v0.3, holding SPEC v0.4 fixed.*

## 0. The finding

PLAN v0.3 describes the system as **eight types, five protocols, five extension slots, four layers, twenty-one modules**. That is an inventory, not an idea. Underneath it there is a three-verb algebra:

> **Append experience. Fold views. Commit at rest.**

Everything ember does is one of those three, and every extension extends exactly one of them. This is not a rename — adopting it *deletes an engine*, *deletes a trailer*, and *collapses five contract types into two*, because the inventory was hiding duplication.

| Verb | What it is | What extends it |
|---|---|---|
| **append** | writing an experience to the WAL — the only mutation in the system | a new **kind** (what can happen) · a new **port** (what can happen *from outside*) |
| **fold** | deriving anything from the stream: states, the present, the biography, the ledger, the index | a new **reducer** (what a happening means) · a new **processor** (how a view is shaped) |
| **commit** | the present becoming past at a quiescent point | a new **op** (a new kind of life-event) |

## 1. Attention *is* a fold — the plan is paying for two engines

PLAN §3 gives `fold` a reducer signature and then, separately, §6/§5 give attention a "projection → processors → renderers" pipeline with its own vocabulary. But SPEC §5.1's projection step is *literally a left fold over the stream* producing candidate messages. The two differ only in accumulator type and in whether a post-pass runs.

```python
# ONE engine (core/fold.py), two reducer families, an optional post-pass
def fold(xs: Iterable[Experience], reducers: Mapping[Kind, Reducer], init: A) -> A: ...

states   = fold(xs, STATE_REDUCERS,   States.empty())          # A = Change accumulator → states/
messages = chain(fold(xs, MESSAGE_REDUCERS, []), processors)    # A = list[Message] → present/
```

Consequences, all subtractive: `mind/attention.py` loses its engine and becomes reducers + processors + renderers; `core/project.py` (the observability renderer set) stops being a third thing and becomes *more views*; the effect ledger, the biography, the cost total, and the future SQLite index are all the same pipeline with different reducers. The mental model shrinks from "a fold engine, an attention pipeline, and a projection layer" to **"every derived artifact is a view: `render(process(fold(stream)))`."**

Slot count corrects downward too: what v0.3 calls five slots is really **three kinds of code** (reducer, port implementation, tool) plus **two kernel events** (a new kind, a new op). Say that instead; it is both truer and easier to hold.

## 2. `Ember-Nature` is redundant — delete it

The evolvability review asked for a trailer recording the nature that produced each node, so piecewise fold can find it in O(1). But git already stores it: the nature of a node **is** its `programs/` subtree, addressed by `<node>:programs`. One `git rev-parse` gives the exact same hash with no write path, no derivation, and no possibility of disagreeing with the tree it claims to describe.

Keep the *requirement* (piecewise fold groups spans by nature identity), delete the *mechanism*. This is the cleanest kind of simplification: the information was already in the substrate, and the plan was about to store it twice.

The remaining trailers (`Ember-Op`, `Ember-Moment`, `Ember-Span`, `Ember-Meta`) stay — not as a dual record with a consistency obligation, but as an **A4 cache** whose whole purpose is that `git log` is a biography on a machine with no ember installed. Verified by `fold`, exactly as v0.3 says.

## 3. The contract is five types too big

v0.3's waist is `TickInput(phase, sensations, view, vitals, policy)` → `TickOutput(messages, acts, queries, disposition)`, plus `View`, `Vitals`, `Policy`, `Span`, `Query`. But sensations are *already the newest experiences in the view*; vitals are *computed from the view* (the mind can count its own tokens); policy is *a file in the being's own tree*. Passing them separately encodes one theory of psychology into the one place that must outlive theories — precisely the over-specification the evolvability review flagged.

```python
class View(Protocol):                      # the mind's whole world, read-only
    def experiences(self, since: int | None = None) -> Iterator[Experience]: ...
    def state(self, path: str) -> bytes | None: ...
    def nature(self, path: str) -> bytes | None: ...     # its own programs/
    def now(self) -> str: ...                            # injected: no clock in the mind
    def ask(self, q: Query) -> Any: ...                  # reserved; in-process in v1

class Output(BaseModel):
    messages: list[Message] | None = None    # phase=attend
    acts: list[ActCall] = []
    disposition: Span | None = None          # phase=settle

def tick(phase: Phase, view: View) -> Output: ...
```

Three types where there were eight, and E6 (waist purity) becomes trivial to test: hand the mind a `View` whose `experiences()` is a fixture and whose `now()` is fixed, and stub everything else to explode.

## 4. `Change` survives, and it is process — not format

Tested the collapse: *make `Change` an experience kind, and reducers vanish* (the tool records what it changed; states = replay of change-experiences). It is genuinely smaller — but SPEC §2.4 chooses the other way on purpose: *"the fold is piecewise by the being's own nature… reducer changes are migration events."* State semantics are part of the nature (A6), so they must be **derived by code in the tree**, not frozen at write time. Recording changes would move that meaning out of the being's reach.

So: reducers stay, `Change` stays as their pure output, and the decisive answer to the question the coherence audit is chasing — **`Change` never appears in the stream, therefore it is process-waist, not format.** What reunite merges is `states/` trees (which git already merges) informed by Change lists; the Change type itself needs no version field.

`Op`, meanwhile, is not a core type at all — it is the content model of the `op` kind. Counting it separately is how "eight types" happened.

## 5. Concentric kernels — a build order that is always alive

The strongest test of whether a decomposition has the right centre: what survives at a third of the size?

**Ring 1 — a living being (~1,550 lines).** canon 40 · kinds 60 · experience 100 · stream 120 · store 180 · tree 60 · node 60 · fold 100 · view 80 · model 200 · tools 80 · cycle 180 · mind 200 (attention+dream+memory+next) · cli 150. It perceives, thinks, acts, sleeps, remembers, folds, branches, and you can read its biography with git. It is **not** safe (no approval), constitutional (no receipts), evolvable (no `ext`, no seed), or fully observable.

**Ring 2 — a safe, observable being (+~1,400 → ~2,950).** Durable awaiting node + approval with reasons · receipts + `authority.rule()` · visibility filtering + secret redaction · `status/show/log/tail/diff` · DAG-shaped fold · repo lease · sims + `rethink` · chronicle entries · span summary.

**Ring 3 — a constitutional, evolvable being (+~1,200 → ~4,150).** `goto`/`revise` · dream levels + change-reports · memory blocks and paging · `self.status`/decline · piecewise-fold isolation + `fold --from-birth` · `ext` kinds · world metadata · seeds as a versioned tree · async acts · golden fixtures with the full axiom and evolvability suites · error taxonomy.

Each ring ends with a being you could use. That is a better spine than "week 1 substrate, week 2 first light," because every ring is shippable and the line guard has three natural checkpoints instead of one cliff. It also exposes an honest schedule: three rings at this density is **closer to four weeks than three**, and Ring 1 alone is the two-week milestone.

## 6. The ugliness list

| # | Complicated | Simpler | Cost of simplifying |
|---|---|---|---|
| 1 | Two derivation engines (fold + attention projection) | one `fold`, two reducer families, one processor chain | slight awkwardness: state reducers accumulate, message processors transform |
| 2 | `Ember-Nature` trailer | `<node>:programs` tree OID | none — strictly better |
| 3 | Eight core types | five (Experience, Content, Part, Change, Manifest) — `Op` is a Content, `View`/`Output` are process | none |
| 4 | Contract of eight types | three (Phase, View, Output) | vitals/policy become the mind's business, which is where they belong |
| 5 | `nodesh.py` + `project.py` | one `view.py` (addressing *is* projection) | one 220-line file with two responsibilities — acceptable, they share every type |
| 6 | "Five extension slots" | three kinds of code + two kernel events | none — the story gets truer |
| 7 | `rites list` as a mechanism | in v1 there is exactly **one** rite (displacement on old-branch wake); call the function | abstraction returns at M3 with its second user, which is when it earns its name |
| 8 | 21 modules for 4.1k lines | 17 files, denser | fewer files read better in one context — which is the whole point |
| 9 | `StatesView` and `View` | one `View` | none |
| 10 | Budget arithmetic asserted, not checked | the line guard prints per-module actuals against the table | trivial, and it keeps the plan honest |

## 7. What I would *not* change

The parts of v0.3 that survive this pass unaltered, because they are already the smaller idea: the **acts-only law** (one state-writing path); **quiescence commits** with the resolution invariant; **verbatim thoughts** as the echo source with `Part` as the shared vocabulary; the **two-waist separation** (§1 — it is the plan's best page, and §4 above sharpens it rather than replacing it); **five protocols** (I tried merging ModelPort and ToolPort into one `perform` seam — the shapes are too different: one streams parts, one returns a resolution, and the union type is worse than the pair); **git plumbing for the store**; and **observability as views, adding zero stored artifacts**.

## 8. Recommendation

**Keep v0.3's architecture; adopt six edits.** In order of value:

1. **One fold, many views** (§1) — deletes an engine and a vocabulary; recast `mind/attention.py`, `core/project.py`, and `core/fold.py` accordingly.
2. **Delete `Ember-Nature`** (§2) — use `<node>:programs`.
3. **Shrink the contract to `Phase`/`View`/`Output`** (§3) — and state that `Change` is process-waist, never in the stream.
4. **Adopt concentric rings as the build order** (§5) — and revise the schedule to four weeks with three shippable checkpoints.
5. **Restate the extension story as three kinds of code plus two kernel events** (§6.6) — and drop the rites abstraction until its second user (§6.7).
6. **Merge `nodesh` + `project` into `view.py`; publish per-module actuals in the line guard** (§6.5, §6.10).

The organising sentence to put at the top of the plan, replacing the inventory:

> **The stream is the only truth. Everything else is a view of it. A moment is one thought, committed at rest.**

Append, fold, commit. If a proposed feature is not one of those three, it does not belong in the kernel.
