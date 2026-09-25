# Review M: Biology audit — PLAN-LIFE v0.1 vs SPEC v0.4, PLAN.md §8, and the code as shipped (fable, 2026-08-04)

**VERDICT: right organs, right order, wrong load-bearing claims.** Executable after a revision that
costs a day of writing and no code — but three central assertions are false as written:
self-revision is not "one tool, one rule" (it crosses the act/op mechanism boundary the kernel
deliberately built, and the crossing is unowned); the §4 benchmark's survival number is vacuous by
construction and its retrieval number measures inclusion arithmetic, not memory; and the
omission-ledger completeness claim is untrue at the kernel seam today. One law is missing entirely —
where a nature's "now" comes from — and its absence is the single defect in this plan that can
permanently poison committed history. The §0 gap table is accurate line for line; every cell was
verified. The diagnosis is right. The prescription needs surgery.

*(Findings 1–9 as delivered; the four load-bearing claims were independently re-verified against a
live world before folding: a tree program reading `time.time()` returns different values on
identical input; chronicle epochs are immutable in two enforcement sites; the being lease raises
`LeaseError` on nesting; the span trailer carries no cost field. All confirmed.)*

## 1. The invariant the plan relies on and never states

`derive_node` reconstructs every attend/settle input purely from (parent tree, node-local events) —
`derive.py:293-301`; `replay.py:245-261` re-executes attend at every verify and compares root OIDs.
Two corollaries the plan must carry as law:

1. **Attention is re-run by fold in this kernel.** PLAN.md §4.5 said "never re-run by fold"; the
   shipped code records `present/` *and* re-derives it. Every new attend behavior must be a
   deterministic function of the record and the parent tree, or verification of already-committed
   nodes fails forever.
2. **A new attend input cannot be passed; it must ride the stream or the tree.** The input dict is
   closed and built identically at live and verify. Anything else is a kernel change.

## 2. The tree-local claim, organ by organ

**Recollection — TRUE.** `entry.py:50` takes `state_root` and ignores it; `host.py:180-212` extracts
the parent states tree read-only; live and verify pass the same `states_oid`. Zero kernel change.

**Volition — prompt-side true; the loop-side mechanism is invented.** `self.sleep`/`self.decline`
are already durable as act + observation; the loop reads the committed record directly — no
settlement involvement, no state-path convention. What genuinely needs deciding is only the
*standing* petition: `wake_at` across moments (state file vs control file + a new tool — and that
tool is a `tools.py` change the organ table never counts).

**Self-revision — FALSE as stated. The headline finding.** The approval path resolves **acts** by
dispatching them mid-transaction (`runtime.py:796-806`). A nature change is a **restart op**:
`Runtime.revise` takes its own lease, pins a proposal, opens a new transaction with `mode=REVISE`.
An executor has no journal access (`tools.py:238-247`), cannot append an op, and a nested
`Runtime.revise` dies on the non-reentrant flock lease (`world.py:198-210`). The honest shape is
**two steps** — propose (act, `await`, ruled) then apply (`advance(mode="revise")`) — and the
act→op bridge is the actual design work, unowned. Unowned it produces a liveness state the plan
never names: **approved-but-unapplied**. The bridge also needs a recorded ruling↔op linkage or A8's
receipt cannot show the being that *its* proposal caused the change.

Adjacent defects organ 3 would copy: the shipped revise writes `consent="authorized"`
(`runtime.py:310`), **off SPEC §2.2's closed vocabulary `given | policy | imposed`**; and
"graduated autonomy expressed in a policy file" is impossible against a frozen dataclass
(`tools.py:186-197`) — moving policy into the tree is a third kernel change. Gate 2.3 is off by
two nodes: approve resolves at A, the revise op is R, the first thought under the new nature is R+1.

A cheaper organ 3 exists with direct spec support: the being writes proposals into
`states/intentions/` (SPEC §3.3 — denied proposals persist there as unfulfilled will) and the
operator applies them citing the proposal. The plan should choose *as a ruling*; it has chosen the
expensive design while pricing it as the cheap one.

**Ruling: 2.5 of 4 organs are tree-local, not 3 of 4** — and where the claim fails the kernel is not
wrong; the act/op split is the L-review's law working as designed.

## 3. Time has no law — the defect that can poison history

Commitments "when due", `wake_at`, and chronicle cadence all need a *now* inside `attend` — which
runs in a child process with a working clock and no stub (`host.py:126-141`). Replay-purity tests
explode *kernel* ports, not the child's syscalls. The first nature that reads the clock commits
nodes whose `present/` can never be re-derived, and unlike a fixture bug this is unrepairable: the
lineage is committed. **This is the biology phase's `Part.kind`.**

The missing law: **a nature's only clock is the record** — "now" is the `ts` of the newest event in
the window, or a `sensed` wake event the loop appends, never sampled. Corollary: the kernel stamps
wall-clock `ts` at append with no injection seam, so cadence must key on **moment count** or the
plan must own a clock seam it currently does not admit.

Recommended standing guard: after live derivation, re-run `derive_attention` from the journal before
commit and compare — a nondeterministic nature is caught before its node is committed.

## 4. The §5.1 collision, and a false ledger claim

§2.1 quotes §5.1's "notes always compiled, zero epoch latency" and then requires trimming by policy.
Both cannot hold once notes exceed budget, and nothing bounds notes. Missing ruling, governing the
**first** organ built.

"The omission ledger already works" is **false**: the kernel hands attend at most 80 recent events
(`lineage.py:171`); events beyond the window are silently absent and attend cannot ledger what it
never saw. The window is a kernel constant, not nature policy — a quiet limit on "attention policy
belongs to the being".

Also: `_extract` materializes the full states tree per moment, so per-moment cost is flat in
*lineage length* but linear in *state size*, and the chronicle grows monotonically.

## 5. The gate measures inclusion arithmetic and calls it memory

1. **Survival is vacuous.** Chronicle epochs and change reports are write-once, delete-never
   (`derive.py:209-215`, `tools.py:214-215`). A survival floor passes at 100% forever.
2. **Retrieval without recall is inclusion policy.** The plan defers hybrid recall but also silently
   omits **grep recall, which SPEC §0.4-M2 places inside "crude memory"**. A fact's only route to
   the prompt is unconditional inclusion or recency.
3. **The with/without-level-1 comparison is null as specified** — the index carries paths, not text;
   if only recent level-0 entries are included, level-1 is write-only and measures zero.
4. **Who distills is undecided**, and it decides what the number means: code distillation cannot
   exhibit the lossy-rewrite decay the hierarchy exists to bound; model distillation makes CI
   nondeterministic and paid.

Ruling 5's circularity is real: the gate needs the cadence and the cadence is ruling 5. The order
survives; the verification story needs rewriting.

## 6. The ordering: correct, partly for a reason the plan doesn't give

The counter-case fails: scripted iteration already exists (`benchmark_moments.py` lives 150
moments). The loop-as-organ is about *unattended* life, not the ability to iterate. Continuation-last
for spend safety is sound. "Without volition, self-revision has no motive" is rhetoric — the real
reason it can be third is that its gate needs only an operator in the loop.

## 7. What the four-organ frame re-drops from PLAN.md §8

PLAN.md §8 was variation **plus selection** plus inheritance. PLAN-LIFE builds variation and
Lamarckian inheritance with **no selection instrument** — no sims, no `rethink`, no present-diff, no
scenario suite — and none appears in §3's deferrals, so the drop is silent. The present-diff
(recompile a past node's present under a candidate nature; deterministic, zero token cost) is nearly
free against the shipped single-derivation kernel and is exactly the pre-adoption check an operator
ruling on a proposed `attend` change would need. "Scope grows with track record" presupposes
recorded proposal outcomes nobody collects.

Gap 4 cites "no fatigue" as evidence, then fatigue is neither built nor deferred.

## 8. Claims that are not true

1. "Three of four organs tree-local … self-revision: one tool, one rule" — it is a mechanism crossing.
2. "The ruling path already exists … no new ontology" — ruling→restart application does not exist.
3. "The omission ledger already works" — false above the 80-event window.
4. "Per-moment cost recorded in the span" — the span has no cost field.
5. "Fail on a survival floor" — vacuously satisfied.
6. "Graduated autonomy expressed in a policy file" — no policy file exists; policy is package code.
7. "The next moment runs under the new nature" — two nodes late.
8. §0's "none of them is an architectural question" — organ 3 is one.
9. §1's "does not give perception access to the durable part of moment" — the kernel gives it; the
   seed ignores it. §0's table states this correctly; §1 restates it wrongly. Gap 4's §3.4 citation
   is thin; §3.7's wake row and §5.2's preference order are the true support.

## 9. Disposition

**Must land before the first line of the biology**
1. The §1 invariant stated as law.
2. The time law — before any due-time or cadence code.
3. Omission legality and the corrected ledger claim — before organ 1.
4. The act→op bridge ruling — organ 3 redesigned as propose-then-apply (or intention-shaped), with
   linkage field and consent vocabulary corrected.
5. §4 rewritten to say what it measures, with the level-1 read path defined and grep recall added or
   its absence ruled.

**Fixable during the build**
Loop contract and `wake_at` mechanism · merge rulings 1+4 · reframe ruling 3 on moment ceilings plus
a named `sensed` span-summary · pre-commit attend-recompute guard · window-truncation marker ·
deferral list completed (sims, rethink, present-diff, seed promotion, fatigue) · state-size cost
slope stated beside the flat-cost gate · gate 2.3's node arithmetic · organ-table arithmetic.

**Forces a rewrite if discovered late** (ordered by pain)
**(1) A clock or any unrecorded input reaching `attend`** — committed nodes permanently
unverifiable; not fixable by any later patch. **(2) The benchmark built on ts-based cadence** —
retrofitting a clock seam after golden lineages exist touches recorded bytes. **(3) Self-revision
implemented the "obvious" way** — a special-cased apply-at-approve inside `_resolve` is a second
restart path parallel to `Runtime.revise`, the exact sin the derivation unification exists to
prevent. **(4) Notes-always implemented literally then reversed** — replay survives, but the phase
gate fails weeks in.

## 10. What is sound

The §0 gap table (every cell verified) · recollection as genuinely tree-local, the plan's central bet
honored by the kernel's single-derivation design · the broken-nature safety net (real, tested,
correctly predating the plan) · continuation's stop-condition posture and its refusal to paper over
pending-act halts · the byte-safety claim for §3's actual deferral list · keeping the standing kernel
gates.
