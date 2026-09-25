# Review I: Kernel critic on PLAN v0.2 (fable, 2026-07-30)

**VERDICT: 5,000 cap holds; 4,000 target does not — honest rewrite lands ~4,350 (~4,210 with the elegance removals). Restate target as 4,300. Architecture genuinely good, but two proudest claims overstated, and there is ONE REAL REPLAY-CORRECTNESS HOLE.**

## 1. Budget audit (module by module)

Honest as drawn: canon 60, kinds 120, tree 150, node 180, attention 300, dream 200, memory 150, next 200, tool_port 200(+10).

Underestimated:
- **experience 220→260**: `sensed` carries FOUR structurally different payloads (receipts w/ A8's six mandatory fields; origin sensations 5 fields; async-act completions; temporal displacement) → discriminated sub-union = 50–70 lines. Plus verbatim `thought` w/ signature blocks.
- **stream 250→290**: deterministic multi-writer interleave (even v1 gets >1 sid after a twin); torn-tail detection on final segment line; seq-recovery on reopen.
- **store 350→390**: 350 only achievable with naive full-tree rebuild (re-hashes growing stream/ every moment — perf cliff deferred to M4); incremental dirty-path TreeBuilder is +60–90 alone. **pygit2 has NO atomic ref CAS → shell to `git update-ref <ref> <new> <old>`** (extend the git-CLI blessing, say so). **Lease must be REPO-level, not face-level** (two bodies can check out two faces of the same ref) + staleness detection + takeover ≈ 50 lines. Git can't represent empty dirs → keep-file convention for `states/intentions/` etc.
- **fold 200→240**: piecewise-by-nature (A6) = detect programs/ tree-OID changes, map moment ranges to versions, **import each historical version's reducers in an ISOLATED module namespace** (importlib + sys.modules eviction = 50–70 lines). Tail recovery needs §4.5 reconciliation (synthesize cancelled/unknown). Write DAG-shaped NOW (+15) vs rewrite at M6/M7.
- **contract 80→100**: single `tick()` CANNOT implement the §5 trace, which invokes the host at step 4 (ATTEND) AND step 7 (SETTLE) → must be two calls or a generator; plus `Part` needs a typed home.
- **model_port 450→560 as drawn (most under-budgeted)**: request build + tool-schema conversion ~50; streaming demux w/ fragmented tool-call JSON accumulation + parallel-call indexing ~120; **verbatim capture, which LiteLLM's normalization ACTIVELY FIGHTS** (flattens content, separates reasoning_content/thinking_blocks from their in-message ORDER — and order is exactly what reordering exists to repair) ~50; echo assembly (thinking first, signatures intact, tool_use after, role-tool pairing hoist, cache_control ≤4 markers) ~120; usage/cost ~20. >550 before the "drift detector" adapter, uncounted.
- **cycle 400→490**: exits and edges, not the 8 steps — RESOLVE must FIND receipts (walk ops since last-lived node — mechanism unspecified), deliver rulings + async completions + displacement sensation; q2 exit (persist awaiting act, commit, terminate, resume); EXPRESS tap needs live deltas while WAL writes at part-close (two consumers of one raw stream); crash-recovery entry; vitals accounting; the span loop.
- **cli 220→300 (hard gap, not a quibble)**: THREE verbs the plan's own text requires are missing — **approve/deny** (week 3 promises approval flow; with no habitat the CLI is the only place a ruling can enter), **revise** (A8's axiom proof is "operator revise → receipt precedes next thought" — impossible without it; also needs store support for revise nodes w/ authority block + pinned prior head), **show** (used by §6's interim column). Plus `say` inbox plumbing.
- **errors/config/init 100→130**: §4.4 ladder w/ perceived stop-reasons is a real taxonomy (provider vs tool vs lease vs canon vs refusal → outcome + stop-reason).

**Revised total ~4,350 (or ~4,210 with removals). Warning: the plan's own "delete or defer" discipline will fire mid-week-2 exactly when pressure lands on model_port — and the corner cut will be verbatim echo, the one thing §0.4 calls non-negotiable.**

## 2. Elegant or merely small?

**Holds**: stream-as-only-bus, ports-out/folds-up, the waist, data-over-code, **the axiom-per-seam table is the best page in the plan**. Futures that DO fit the slots: chronicle levels, blocks/paging, hybrid recall, MCP/ACP, speculation, succession, veils/roster/self-model, migration receipts, federation.

**Three breaks:**
1. **Multi-parent fold is a SIXTH kind of move.** reunite/subconscious/chorus fold a node with TWO parents = stream union across writer ids + states merge. Not "a new reducer" — a change to the SHAPE of the fold, drawn linear. §10 files children/subconscious under slots 4,5 — true for the ops enum, false for the fold that replays them. **Fix now for ~15 lines: fold recursive over `parents: list[NodeId]` w/ memoization + deterministic interleave**, even though v1 is linear. Otherwise M7 rewrites the function the whole system's correctness rests on.
2. **The habitat is a WRITER, not a "new consumer" — and rule 1 quietly forbids it.** Durable approvals = habitat writes rulings a sleeping body must find; interrupts = signals a body mid-THINK; `say` over API = feeds an inbox. **Fix (cheap + elegant): name the three control-plane files NOW — `.ember/inbox.jsonl`, `.ember/rulings.jsonl`, `.ember/interrupt`** — CLI writes them in v1, habitat writes the same in M3, "zero core change" becomes true instead of aspirational.
3. **Wake/sleep are rites with hooks, landing in the cycle** (flesh regrowth, requires: check, arrival receipts, swap rite, displacement+ledger) — cycle-path edits, not port impls. **Give RESOLVE/BECOME an explicit ordered RITES LIST (data: functions run at wake, in order)** → converts recurring cycle surgery into slot-shaped extension for ~10 lines.

**Hidden complexity: four dicts + a missing type.** "Six types and four protocols" is marketing. Load-bearing untyped surfaces: `Experience.content: dict`, `Op.payload: dict`, `TickOutput.changes: list[Change]` (Change undefined), `refs: dict[str,str]`. Make the sketch honest:
```python
Content = Annotated[Heard|Sensed|Mused|Spoke|ActCall|Observation|ThoughtRequest|Thought|RefEdit|OpRecord|Error|Annotation, Field(discriminator="kind")]
# Sensed itself discriminates: Receipt | Origin | Displacement | AsyncDone | Words
# Op.payload: per-op models; refs: dict[EdgeName, Ref] w/ closed enum + parsed type
```
**Missing type: `Part`.** ModelPort returns `Iterator[Part]` and Part is never defined — yet the part grammar (text/thinking/signature/tool_call, open–delta–close, indexed) is the vocabulary shared by the WAL part-close rule, verbatim thought content, echo assembler, EXPRESS, and the record/replay cassettes §12 promises. **Arguably the most consequential type for replay honesty. Define it in core, in §2, with the other six.**

## 3. Month-two pain

**PAIN 1 — SETTLE CANNOT BE REPLAYED (the plan's one latent correctness bug).** §5 step 7 applies "mind's staged changes" to states/; replay never re-thinks; but NO experience kind carries them (no `settled` kind; `TickOutput.changes` never written to the stream). First being that takes a note via a staged change → `ember fold` diverges → A4 and A6 both fail → fix at that point is a migration.
**Resolution DELETES code: the ACTS-ONLY MUTATION LAW** — every durable state change the mind makes is a recorded act (memory tool, notes tool, intentions tool) with an observation; a kernel reducer replays observations into states/. Then `changes` is deleted from the contract, SETTLE shrinks to "record span disposition," and the fold has exactly ONE state-writing path.
**Corollary the plan must state**: `present/` is RECORDED, NEVER RE-DERIVED — fold verifies states/ + trailers only, so attention nondeterminism (token estimates) cannot break replay. Missing sentence; someone will "fix" replay by re-running ATTEND.

**PAIN 2 — the seeding rule fails SILENTLY on imports, and the plant has no gardener.** Template mind/*.py import each other; stamped into programs/, the tree's next.py says `from ember.mind.attention import ...` → Python imports the INSTALLED package, not the neighbor file. **The being's nature edits then change nothing, silently — the precise failure A6 exists to prevent, and it passes every test that doesn't hunt it.** Requires: seeded copies use package-relative imports; ProgramHost loads programs/ as a synthetic package with a unique per-version module namespace (also required by piecewise fold); **standing test: edit the tree's copy → assert behavior changed → assert the package copy is unreachable from the loaded namespace.** Second half: by month two, three beings' programs/ have drifted from a template with five bugfixes and no delivery path → **design (not build) `ember adopt` now**: a revise op applying the template diff through §3.7 with an A8 receipt. One paragraph; its absence is a month-two certainty.

**PAIN 3 — the mind will need a port mid-ATTEND; the host contract as drawn can never give it one.** v1 survives (recall is a THINK-time tool). But §5.1's reminiscence processor (M5) does ATTEND-time index queries, and M6's subprocess host rests on "same contract types over stdio" — a processor touching an IndexPort breaks both (you cannot serialize a live port over stdio). **Fix costs one reserved verb today: host protocol as a conversation — `attend | query* | settle` — host may issue typed READ-ONLY query requests (recall, block page-in) the body answers before the present returns.** v1 implements query trivially in-process; M5/M6 land in-slot instead of renegotiating the waist.
Runner-up: resuming a q2 awaiting node days later = cold cache + possibly new epoch → §3.4 requires re-ingest estimates ON APPROVAL PROMPTS → `ember approve` prints the cost line from day one.

## 4. Missing entirely
1. **World bootstrap**: no `ember init`; what does `ember birth` do in an empty dir (bare repo vs worktree-of-record, initial ref layout, orphan first commit, `born_from: null`), and what the seed contains beyond code (soul.md, permissions.yaml, vitality.yaml, body.yaml, tool manifests — data files someone must author in week 2).
2. **Receipt discovery**: RESOLVE injects receipts FROM WHERE? Rule: walk ancestors HEAD→last node this body lived, collecting restart-ops; needs a cheap "last-lived" marker (trailer suffices).
3. **Lease semantics + CAS mechanics**: repo-level location, staleness, takeover, renewal, `git update-ref` for CAS. "Lease" appears in one table cell and nowhere else.
4. **Mid-THINK crash policy**: WAL holds N closed parts, no message-close → wrap as truncated `thought` + `error`, commit at q3, never silently re-send; acts safe by construction only because dispatch is at message-close (say so); usage `unknown`; vitals must tolerate.
5. **Golden-fixture mechanics**: a golden lineage is a git repo — you cannot commit .git into git. **Answer: `git bundle`** (also the natural archive/migration format §8.4 wants). Dialect cassettes need a named format: Part-stream `*.parts.jsonl` (another reason Part must be a core type).
6. **Secret redaction at WAL write** (SPEC §9.4) — neither included nor listed as cut. v1 is daily-driven with a bash tool; the first `env` output writes plaintext keys into append-only immutable replicated history = **the exact one-way door the erasure taxonomy calls unrecoverable. ~20 lines belong in v1.**
7. **macOS durability**: fsync on Darwin doesn't flush to platter → `F_FULLFSYNC` (3 lines) or an honest dev-mode caveat. **The builder's machine is a Mac.**
8. **Float policy for money**: LiteLLM returns float costs; "no floats in states" → string-decimal or integer micro-dollars, decide now.
9. **Stream write-protection from the in-process mind**: no container in v1 → the edit tool can write `stream/` unless ToolPort path-guards it (~10 lines), else A3 is a convention.
10. **Fatigue's data source**: which tokenizer/estimator; where usage-from-response meets estimate-for-next.

## 5. Elegance moves
**Removals (lines out, fidelity kept):**
- **Acts-only mutation law** (Pain 1): −40 to −60 in cycle, collapses fold to one state-writing path, closes an axiom hole. **Best line-negative change available; makes the system MORE spec-faithful.**
- **Two adapters of unequal vows**: primary **direct Anthropic (~280)** where verbatim order/signatures/breakpoints are native passthrough (the non-negotiables become trivially true on the brain the being lives on, and §12's drift-detector risk disappears because the detector IS the primary) + **LiteLLM commodity (~180)** for breadth and dream_model with echo fidelity honestly stamped degraded in `brain_class`. Net ~−100 vs making LiteLLM alone meet the vows (~600+). SPEC §9.1 survives — LiteLLM remains a ModelPort implementation.
- **Defer `twin` from the v1 CLI, keep it in the store**: A7's test is a 5-line store fact; the CLI verb drags origin sensations + source notice + displacement (three obligations v1 would half-implement). −30 lines, deferred whole to M3 where the spec puts them.
- **One lineage verifier**: moment auditor + resolution invariant + trailer verification + fold compare = one walk, four checks, in fold.py; axiom tests and CLI both call it.
- **Kill §1 rhetoric that misprices futures**: "speculation ~0 lines" and "habitat: zero core change" are both false as shown.

**Additions despite budget**: DAG-shaped fold (+15); `query` verb reserved in host protocol (+5); three control-plane files named; redaction + F_FULLFSYNC + revise/approve/deny/show verbs; rites list (+10); one doc paragraph designing `ember adopt` (+0 code).

**Revised table**: canon 60 · kinds 120 · experience 260 · stream 290 · tree 150 · store 390 · node 180 · fold 240 · contract 100 · model_port 500 (280 direct + 180 litellm + 40 shared) · tool_port 210 · cycle 440 · attention 310 · dream 210 · memory 150 · next 200 · cli 270 · errors/config/init 130 = **~4,210; cap holds; headroom ~790.**

## Closing
Must change before execution: (1) the contract — split tick into attend/query/settle, delete `changes` under acts-only, define `Part`, type the four dicts; (2) the fold — DAG-shaped, isolation-imported, one verifier; (3) the claims — habitat is a writer (name the three files), wake is a rites list, slot table stops rounding hard futures to zero; (4) the gaps — revise/approve in CLI, receipt discovery, lease/CAS, mid-THINK crash rule, redaction, bundles-as-fixtures. **Every one is cheaper this week, at zero lines of existing code, than in month two at the cost of a migration the plan's own thesis has promised never to perform.**
