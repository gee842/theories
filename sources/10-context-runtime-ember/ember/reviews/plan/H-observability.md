# Review H: Observability & DAG ergonomics for v1 (fable, 2026-07-30)

**Governing rule (A4 applied to the interface): observability adds ZERO new stored artifacts.** Two disjoint verb classes: **observe verbs never write anything** (not even caches); **move/edit verbs write only through the op/ref path the spec already defines**. No third class. This keeps the whole capability ~675–850 lines.

## 1. Eleven state questions → cost class
| # | State | Lives in | Cost |
|---|---|---|---|
| 1 | being status now (head, moment, span, epoch, brain, lease) | refs + trailers + .ember leases + MANIFEST | projection |
| 2 | what a moment perceived | `present/prompt.md`, `messages.json`, `request.json` committed per node | **free** (`git show`) |
| 3 | verbatim model return (parts, thinking, signatures, stop_reason, usage) | `thought` experience | free storage, projection to render |
| 4 | what tools did | act/observation experiences | projection (join by ref) |
| 5 | states/memory changes | `states/` committed per node | **free** (`git diff -- states/`) |
| 6 | attention: included AND omitted | `present/attention.json` | free storage, small renderer |
| 7 | token/cost economics | `usage` in each thought | projection (fold-and-sum) |
| 8 | lineage shape | commits + trailers + ref namespaces | **free** (`git log --graph`) |
| 9 | pending approvals | declared pending tail (A1 resolution invariant) | projection |
| 10 | WAL tail (uncommitted) | face's open segment past last committed seq | **free** (file read) |
| 11 | external-effect ledger | query over act/observation | projection |

**Punchline: rows 2, 5, 8, 10 — the expensive-looking ones — are FREE**, because "one thought = one commit with its exact perception inside" was the design. New code = renderers + one aggregator + three ops.

## 2. Verb set

### 2.0 Node selectors ("nodesh") — what makes it *quick*
- Being implicit if only one; else `-b/--being` or `EMBER_BEING`. World found by walking up from cwd (git-style).
- **`@` = head; every node arg defaults to `@`** → `ember show` with no args answers "what just happened" (the most common question).
- Any git revspec passes through (`alice~3`, `alice@{yesterday}`, shas) — free power.
- `m87` = moment 87 via `Ember-Moment` trailer walk. `sim:ID`, `pin:NAME`.
- **Visibility default in EVERY projection: experiential only**; `--vis forensic|marginalia|all` explicit override (§2.1 contract habit from the first renderer).
- `--json` on every observe verb = **the raw pydantic envelope** (schema stable by construction, pipes to jq).

### 2.1 `ember status` — dashboard
One screen: ref→head, moment, epoch, span state (AWAITING APPROVAL + the pending act + reason), brain + programs sha + last self-edit, lease holder + face path, WAL uncommitted count, today's thoughts/tokens/cost/stamina, refs (pins/sims/twins). `--json`; live = `watch -n2 ember status` (no bespoke loop). NB: approve/deny verbs (~+30 lines) belong to week-3 approval work, not this budget.

### 2.2 `ember show [node] [section]` — the moment inspector (core verb)
Default = moment card: node/moment/op/span/ts, parent, brain, cost, tokens; IN (heard) / THN (mused, spoke) / ACT (act → outcome) / STAT (states diff stat) / ATTN (n sources, n omissions + rules).
Sections: `--present` (git show prompt.md), `--messages`, `--request` (wire truth), `--attention` (table: source → tier → tokens → included/omitted → **rule**), `--thought` (verbatim parts in delivery order; thinking folded to `[thinking: 812 tok, signature ✓]` unless `--vis forensic`), `--acts` (paired w/ outcomes, refusal reasons, counteroffers), `--states [path]`, `--op` (+ authority block), `--stream` (raw envelope slice).

### 2.3 `ember log` — node/DAG view (distinct from `biography` = experience narrative)
`m214 9f3c2e1 live ⏸ awaiting "push branch" 09:12 $0.06` + ref badges (pins/sims). `--graph` delegates to git; `--all` (sims/twins/departed), `--cost`, `-n/--since`.

### 2.4 `ember tail [-f]` — live experience
One line per experience (ts kind gist), blob refs → byte counts. `-f` polls face segments (tail -F). **This is the watch-a-thought-happen view**: sensations → parts closing → acts dispatching → observations → BECOME sha. Filters `--kind`, `--vis`.

### 2.5 `ember diff <A> [B]` — B defaults to A's first parent
`--states`/`--programs` delegate to git; `--present` diffs the two renders (**key view for rethink-vs-original**); `--thought` gists side by side; `--stream` (ancestor pairs) = what happened between. Default `--stat` + thought gists.

### 2.6 `ember peek <node>` / `ember where` — move a VIEWPORT (observe)
`peek` = `git worktree add --detach` → prints path (`--rm`, `--ls`). The whole world-tree as it was, explorable with plain unix tools. `where` enables `cat $(ember peek m87)/states/notes/scratch.md`.

### 2.7 `ember goto <node>` — move the LIFE (op)
**Auto-pins the abandoned tail** (`refs/ember/pins/<being>/tail-<ts>`) so A3 holds by construction → CAS-moves the being ref → refuses if a lease is held (no teleporting a running body). At next wake, RESOLVE delivers a **displacement brief** (`sensed`: wall-clock gap, pinned tail ref, external-effect ledger of the abandoned tail) — +15 lines in cycle.py, charged here because goto makes old-node wakes routine. `twin <new> --at <node>` = non-destructive variant.

### 2.8 `ember revise <node>` — constitutional operator mind-edit (op)
`$EDITOR` on the file as it exists at `<node>` (or `--from <dir>`) → creates a **revise node** (parent=node, tree=node's tree + edits, op payload {author, reason, before/after, prior_head}, authority {requested_by: operator, consent: imposed|given}). **Branch-first by default** → `refs/ember/sims/<being>/rev-<id>`; `--mainline` legal only at head, marks `imposed`, **auto-pins prior head**. Receipt derived from op payload, injected as `sensed` at next RESOLVE. Revising a non-head node forks naturally; descendants untouched; the stream is never rewritten (A3).

### 2.9 `ember rethink <node>` — THE debug verb (op, sims-only)
**The symmetry that makes it safe: `fold` replays and never re-thinks; `rethink` does exactly ONE new think — and still never re-acts.** The world stays outside both (A5).
Modes: bare (stability probe) · `--edit-present` ($EDITOR on messages.json copy) · `--say "..."` (replace/add sensation, recompile) · `--programs <dir>` / `--edit programs/...` (patched nature, recompile) · `--brain gpt-5.2` (model what-if).
- **Copied: nothing materially** — temp detached face at parent (recompile) or node (verbatim); past held by reference (A2).
- **Two modes**: *verbatim* (use node's recorded present, bypass ATTEND — isolates the model) vs *recompile* (start from parent tree, apply mods, run ATTEND fresh, then THINK — tests attention + nature). Both = exactly one THINK (A1).
- **Forbidden mechanically**: ToolPort replaced by **RefusingToolPort** — every act resolves immediately `cancelled`, reason "rethink: acts are never dispatched" (satisfies resolution invariant; node commits clean and inert). No being ref moves. No EXPRESS to real channels. No writes outside `refs/ember/sims/`. Waking a sim later still triggers the displacement brief.
- **Recorded as the spec's speculation pattern verbatim** (§3.2): sim birth under `refs/ember/sims/<being>/rt-<id>`, op carries `speculation: {id, of_node, purpose: "rethink", modified: [...], k:1}` + operator authority. **Losers cited, not parented**; sims GC-eligible; pin to keep; promotion to being is a deliberate later `twin`. **The debug verb is the first user of a namespace the spec already reserved — zero new ontology.**
- **Compared**: prints re-ingest estimate for confirmation BEFORE running (§3.4), then Δ present / Δ thought / Δ acts.
`ember sims` lists/removes.

### 2.10 `fold --verify` (planned), `fsck` (25-line wrapper over standing axiom checks), `grep` (git grep in stream/ → moment/kind/gist)

## 3. Delegation map (where the budget is won)
Rule: **delegate when raw bytes are already the right view; write ember code only where meaning needs decoding or an invariant must be enforced.**
- File at node → `git show {sha}:present/prompt.md | $PAGER` (one subprocess line each)
- Diffs → `git diff {a} {b} -- states/ programs/`
- **DAG + trailers → `git log --graph --format='%h %(trailers:key=Ember-Moment,valueonly) ...'` — git decodes trailers NATIVELY**; ember adds a color map + ref badges (~20 lines), not a graph engine
- Faces/peeks → `git worktree add --detach`
- Search → `git grep -n {pat} {sha} -- stream/`; WAL tail via file read
- Editing → tempfile checkout → `$EDITOR` → diff → op
- Paging/watching → `$PAGER`, `watch -n2`
- Raw power → `cd $(ember where)`; gitk/`git log -p` just work

**Ember-native because raw view is wrong**: envelope→gist projection; ThoughtRecord rendering with forensic folding (raw parts leak signatures — a visibility violation, not just ugliness); act/observation pairing (a join); attention.json rendering; moment→sha resolution; cost folding; the three ops (shape recorded data, enforce pin/CAS/authority/receipt invariants no external tool knows).

## 4. TUI: NO for v1
1. **The quickness bottleneck is addressing, not interactivity** — `@`-defaults + `m87` make one-shot commands answer in one line; navigators only win in extended browsing (minority mode).
2. **The substrate already bought a TUI free: `tig --all` over the world repo IS a DAG navigator** (graph, node inspect, tree browse, diffs, trailers visible). Document it as blessed. Rebuilding in textual/urwid = 400–800 lines + a dep for a duplicate.
3. Spec already defers rendering to the M3 web inspector; a v1 TUI would be throwaway.
Quickness comes from: `@`/zero-arg defaults, `m87` addressing, `-f`, `watch` composability, `--json`+jq, `$PAGER`, `ember where`, 3 aliases (st/lg/sh), short-name sims/pins.

## 5. Budget
| Piece | Full | MVP |
|---|---|---|
| core/nodesh.py (selectors, moment lookup) | 55 | 50 |
| core/project.py (gist, thought render, act pairing, attention render, cost fold, effect ledger, vis filter) | 145 | 120 |
| status | 65 | 55 |
| show | 90 | 80 |
| log | 55 | 45 |
| tail -f | 50 | 45 |
| diff extension | 40 | 35 |
| peek + where | 35 | 30 |
| pin/pins UI | 20 | — (internal auto-pin only) |
| goto (+15 cycle displacement brief) | 45 | 45 |
| grep | 20 | — (document git grep) |
| fsck wrapper | 25 | — (CI-only) |
| revise | 80 | 65 |
| rethink + RefusingToolPort + sims | 125 | 105 |
| **Total** | **850** | **~675** |

MVP recommended → v1 lands ~4,505 vs 5,000 cap, preserving ~495 for predicted model_port/cycle overshoot. New files: `cli_obs.py`, `core/project.py`, `core/nodesh.py` (respects ≤450/file).

**One-way doors (must be v1)**: revise op payload + receipt content (A8 fields recorded into living streams from week 3) · rethink speculation payload + sim-namespace discipline · auto-pin-before-move in goto/--mainline · visibility-default filtering in every projection with explicit override · `--json` = the envelope itself (never a bespoke shape) · [restated] verbatim thoughts with usage + attention.json with omission ledger, without which rows 3/6/7 are unobservable forever.

**Safely additive later**: grep, fsck, pins UI, --cost aggregation, status --watch, rethink --programs recompile, sim promotion, any TUI, the web inspector.

## Scheduling note (IMPORTANT)
**Build nodesh + project + show + tail at the END OF WEEK 1**, not week 3 — they need only the substrate + golden lineage #1, and they are the debugging instrument for weeks 2–3, especially model_port where `show --thought --vis forensic` and `tail -f` are how part-demux bugs get seen at all. Observability is not only a product feature; it is how the rest of v1 ships on schedule.
