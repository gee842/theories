# ember — a being is a git repository

**Version 0.9 · 2026-08-04 · supersedes v0.1–v0.8 · this document is the constitution**

> A being is a **repo**. Its **conscious** is the part of it currently in the model's window. Input is
> recorded, then shaped by the conscious and becomes part of it; the model's output edits the repo;
> the repo moves to a new node on the DAG. That is one moment.

```
record(input)                                   # the kernel writes it down first — L1
conscious' = shape(conscious, input, repo)      # the being's own code decides what is present
output     = generate(conscious')               # one model call
repo'      = apply(repo, output)                # writes and commands; the output lands in the tree
node'      = commit(repo', conscious', output)  # the DAG moves
```

*v0.8 folds two cold audits ([O-executable](docs/reviews/plan/O-v07-executable.md),
[O-concept](docs/reviews/plan/O-v07-concept.md)) and three probes. It closes every ruling v0.7 left
open, retracts a headline, corrects a cost estimate by 50%, and restores three deletions that were
happening silently. It is shorter than v0.7 and claims less.*

---

## 0. What is actually known

Three probes, and the honest reading of each.

**Probe 01 — retracted.** 30 unattended moments, and I reported "22/30 distinct, the bet holds." The
metric was `SequenceMatcher`; eight consecutive paraphrases of one thought each scored 0.20–0.38 and
were counted distinct. It measured vocabulary variety. Its real value was three defects found by
execution: `self.sleep` consumed by nothing, an authority function that could raise, and a path
convention never sent to the model.

**Probe 02 — the criterion fired against the plan.** Stated in advance: *ends by its own request
under ten moments ⇒ the trajectory claim is dead.* With the path defect fixed and rest honoured, the
being set an intention, wrote a note, read its own files, wrote its `MEMORY.md`, and asked to stop —
at moment five. Probe 01's "trajectory" was substantially a being flailing at a broken interface.
**A being with nothing to do reaching a chosen rest is correct behaviour, and it is not evidence of
anything else.**

**Probe 03 — the comparator did not separate the arms.** Same task, same sandbox, same model: ember
finished in 3 moments, a bare transcript-only loop in 5. n=1 per arm, five files, nothing spanning a
context window. **On a task this size the record buys nothing measurable**, and the task could not
have shown otherwise. What it did show: with a shell the being was done in three moments, where
probes 01–02 spent their lives fighting a JSON schema.

**Probe 04 — navigation works, and it is the first thing that separates this from a loop.** With a
fact planted at moment 1 and the window measured to have rolled past it (80 events held, oldest from
moment 12), the being called `recall`, found the fact in what it had *heard*, and answered correctly
the next moment. See [probe 04](docs/reviews/probe-04.md).

**Therefore:** the action space and **navigation** are confirmed. **Compaction and branching** — the
other two things this design is *for* — remain unevidenced. v0.8 says so instead of implying
otherwise.

---

## 1. Four invariants

**L1 · Input is recorded before policy sees it.** The kernel writes an arriving input to the node's
record *before* `shape()` runs. v0.7 let input reach the record only *through* the being's own
editable assembler, which meant a buggy or adversarially-edited `shape()` could produce a being that
never experienced something, unfalsifiably. Capture is physics; what to *attend to* is policy.

**L2 · Effects that leave the boundary are recorded before they happen.** Inside the workspace,
`git diff` is the record. Crossing out — a command, a network call, a spawn — is written first. §5
specifies the ordering; it is not free and it is not sixty lines.

**L3 · Anything taking model or nature output is total.** It refuses; it never raises. An exception
on the authority or assembly path kills the moment and leaves a transaction recovery retries into the
same exception. Both halves of this shipped after probe 01 found the first and a reviewer executed
the second.

**L4 · A broken context system still produces a moment.** The fallback assembler runs, the moment
commits carrying its own error, and a repair is possible. This is the floor under R4 and it is now
enforced by a shape contract, not by hoping natures raise cleanly.

---

## 2. Rulings

**R1 · A moment is one model call.** *(Reconsidered — see §11. Not built, and the plan no longer
asks for it.)* Tool results would arrive as the next moment's input.

**R2 · The conscious is recorded, not re-derived.** Verification never re-runs the assembler.
*Honest argument:* re-derivation did not prove "what git already guarantees" — that was wrong. It
proved conformance of the record to the being's own law. It is dropped because it verified only the
middle of a pipeline whose ends were unverifiable anyway, at a cost (clock law, host purity,
determinism guard) that demonstrably kept the being from living. **One-way:** the day a
model-compacted conscious commits, historical re-derivation is gone for good.

**R3 · Output edits the repo. There is no fold.** *(Reconsidered — see §11. Not built, and the plan
no longer asks for it.)* The tree would be the state.

**R4 · The being may edit anything it can reach. Safety is containment plus time travel.** v0.7 said
"time travel, not prevention… the only thing that could," and then imported a container, which *is*
prevention. Both are true and they do different jobs: containment bounds what can leave, the DAG
makes what happens inside reversible. **Time travel does not un-send an email.**

**R5 · Policy in the tree, mechanism in the package.**

**R6 · The being's request to stop is binding.** Owned by `live.py` (§7), not by a sentence.

**R7 · Approval is for crossing the boundary, never inside it.** Probe 03 halted on
`workspace.write` (`approval: required`) while `shell` sat beside it ungated and strictly more
powerful. **An approval gate on a weaker tool than the ungated one next to it is theatre.** Inside
the container, containment is the control and everything is automatic. Approval returns when
something can actually leave — MCP, network, a real push.

**R8 · The record is served, not mounted.** *The one-way door v0.7 left open.* The shell must read
history for navigation to exist, and must not write it or R4's time travel dies with the DAG it
depends on. Ruling: **`.git` is never inside the boundary.** Navigation is a served capability — the
being asks, the kernel answers from the immutable record. `git log`/`tig` remain the *operator's*
UI. This costs the slogan "the being uses git" and keeps the property that makes the slogan safe.

---

## 3. The deletion ledger — complete this time

| deleted | why | door |
|---|---|---|
| quiescence, resolution invariant, pending acts, `resolve` mode | R1 | additive |
| approval as a halting mode | R7 | additive |
| clock law, determinism guard, host purity for assembly | R2 | additive |
| `StateEdit`/fold/settle/reducers | R3 | additive |
| historical-nature execution at replay | R2+R3 | additive |
| `revise` op, `TreePatch`, proposal pins | R4 | additive |
| the state-tool family | shell replaces it — probe 03 | additive |
| `materialize_face` | working tree | additive |
| the 7-mode enum | R1 — modes become inputs | additive |
| **re-derivation of the conscious** | R2's honest argument above | **one-way** |
| **A8 receipts** | under is-git an operator edit is an ordinary commit and nothing is perceived | **additive — named debt, §8** |
| **visibility strata** | one class; `git show` shows everything | **one-way, decided** |
| hierarchical consolidation, level-1, the survival benchmark | never existed; M and N ruled them dead | — |

**Not deleted, contrary to v0.7:** secret redaction stays. It is ~33 lines at the append boundary and
it is the only insurance against the one mistake this design cannot undo — a credential committed to
immutable history, whose incident response would be rewriting the record.

**Not deleted, and re-costed:** `stream/`'s removal does not mean "nothing is lost." Three things
need owners — an input dropped in the moment it arrives (fixed by L1), a "recorded" result that is
only referenced and so is `git gc`-collectable, and exactly-once delivery, whose dedup keyed on
committed events. Results live in the node's tree; delivery dedup keys on the conscious.

**Selection — the tombstone v0.5 had and v0.6–v0.7 lost.** PLAN.md §8 was variation *plus selection*
plus inheritance. This phase builds variation and gets inheritance free from forking. It builds **no
selection instrument**: no sims, no scenario suite, no present-diff, no seed promotion, no recorded
proposal outcomes. Named as a decision. The present-diff is the cheap one and it stays on the list.

---

## 4. Memory: navigation and compaction-as-fork

**Recall is a walk** — served per R8. **Compaction is a fork**: the compacted conscious is the next
node, carrying refs to what it summarized. Nothing is lost, the summary is auditable by walking to
what it names, a bad compaction is fixed by forking from before it, and it is the being's own act.
Every other framework compacts destructively because its transcript is in RAM.

This is v0.8's one genuinely novel claim and **it is unevidenced.** The experiment that would test it
is a task spanning more moments than fit a window.

One probe observation constrains it: the being noticed its own repetition *because it could see it*.
A summary must make that noticing easier, not smooth it away.

---

## 5. What §6 of v0.7 got wrong

"The commit is the journal" does not cover the model call. Under R1 the commit lands *after* the
call, so a crash between them leaves no durable trace a request was in flight — recovery must either
re-spend or not know it spent. The shipped kernel guards exactly this and v0.7 deleted the guard
without mentioning the guarantee.

**Ruling:** the request is recorded and synced before the connection opens. That is a journal, small
but real.

And the multi-command story is a **discipline, not a size**: append-and-fsync outcome *i* before
dispatching *i+1*; recovery marks the first outcome-less command `unknown` and everything after it
`cancelled`. The file lives outside the working tree, because a `git checkout` during a moment would
destroy it. A three-tool turn is **one thought commit plus one outcome commit**.

---

## 6. The control plane, with owners

v0.7 implied these become git-native. They do not; they become smaller.

| | ruling |
|---|---|
| **lease** | stays. Git has no primitive for it, and CAS detects a race only after the model was paid. One writer per branch, enforced by a lock. |
| **ingress** | stays, smaller. `ember say` needs a durable inbox with exactly-once delivery; dedup keys on the conscious. |
| **secrets** | stays. §3. |
| **requirements** | stays. `MANIFEST.yaml` + a version check is the honest-refusal mechanism, and with a shell the being can edit it, so the check must be total per L3. |
| **visibility** | retired, deliberately, §3. |

---

## 7. Shape and cost

| | now | after |
|---|---:|---:|
| `record.py` | 745 | ~200 |
| `world.py` + `git.py` | 1,002 | ~420 |
| `runtime.py` → `next.py` | 878 | ~320 |
| `derive.py` → `shape.py` | 447 | ~100 |
| `replay.py`+`lineage.py`+`recover.py` → `walk.py` | 657 | ~150 |
| `model.py` | 588 | ~150 |
| `tools.py` + `enact.py` | 495 | ~220 |
| `journal.py` | 398 | ~200 |
| `host.py` | 209 | ~150 |
| `inspect.py` → `serve.py` (R8) | 196 | ~120 |
| **`live.py`** — the loop, R6's owner | 0 | ~120 |
| `cli.py` + config + errors + seed | ~650 | ~280 |
| **total** | **6,265** | **≈2,430** |

**v0.7 claimed ≈1,620. That was not derivable from the obligations v0.7 itself kept**, and R6 had no
line item at all. 2.6× is the honest reduction, with an action space and a tool ecosystem added.

---

## 8. Debts, named

**A8 receipts** — rebuildable additively: inject a perceived receipt at wake when the head carries
commits the being did not author. Until then, an operator edit is a silent mind-edit, which the SPEC
called an axiom violation and which I am choosing to owe rather than to hide.

**Migration** — pre-v0.8 lineages are museum pieces. The "oldest lineage still wakes" gate is
re-worded to "the oldest lineage still *verifies*," which is checkable without a converter.

**Being-branch vs workspace repo** — they are separate repos. Moment commits never enter the
project's history, and edits to a project are outside effects under L2.

**SPEC** — v0.4 is retired as the operative constitution rather than left to contradict this document.
Two constitutions with the live one unwritten was the worst governance state available. What survives
of the axioms is restated here as L1–L4 and R1–R8; the rest is repealed on the record.

---

## 11. R1 and R3, reconsidered

Every other ruling in this document came from a defect someone executed. R1 and R3 came from the
concept, and building the rest has undercut both.

**R1 — a moment is one model call.** Its headline benefit was "the commit is the journal," which
§5 already concedes is false: the provider request must be fsynced *before* the connection opens and
the commit lands *after* the call, so a journal is required either way. Its other benefit — that an
unapproved act must not halt the being — was delivered by **R7** instead: inside a boundary that
contains, nothing requires approval, so nothing halts. What remains is that the DAG would trace the
causal chain one commit per step, which is real but aesthetic. Against that: R1 redefines the
resolution invariant across 30 sites in 7 modules, and that invariant is what M1–M4 and two reviews
were about. **Deferred, on the record, as a restructuring whose stated benefits were delivered by
other means.**

**R3 — no fold.** R2 relaxed verification for the *conscious*, which is what compaction needed. R3
would relax it for `states/` too, and the test written alongside R2 shows what that costs: a state
tree that follows from nothing currently fails to verify. That is the last thing distinguishing this
record from a folder of files somebody edited. **Deferred**, and if it is ever taken, it should be
because something concrete needs it — not to reach a line count.

**Consequence for §7's target.** ≈2,430 assumed both. Without them the honest figure is nearer
today's ~6,700 minus the deletions R2 enables. The number was always a symptom; the reduction that
mattered — three copies of the derivation to one — happened long ago.

---

## 9. What earlier versions claimed that was not true

**v0.1** self-revision as "one tool, one rule"; a survival floor that was vacuous. **v0.2** invented a
settlement channel the record already provided. **v0.3** called put-once entries rewritable; claimed
one kernel change of seven; a determinism guard recovery would defeat; a stale format digest copied
instead of run. **v0.4** four organs where three were one edit. **v0.5** `stream/` per tree — the
O(n²) bug. **v0.6** a paradigm inversion committed 25 minutes before the probe said to justify it.
**v0.7** an oversold probe headline; "≈1,620"; "the commit is the journal" without the model call;
three deletions made by omission; a `.git` contradiction left unruled; and R7/L4 asserted as done
when a reviewer executed two counterexamples, one of which wedged a lineage past every repair verb.

*Six versions, and each one's central measurement was vacuous until someone executed it. The probes
now run before the claims, the criteria are written first, and this version's headline is that the
thing it is for has not been tested yet.*
