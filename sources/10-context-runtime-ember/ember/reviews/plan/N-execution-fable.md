# Review N: Execution audit — EXECUTION.md vs PLAN-LIFE v0.3, SPEC v0.4, and the code as shipped (fable, 2026-08-04)

**VERDICT: the middle of this plan is real and the bookends are wrong.** Steps 1–4 largely survive
execution against the shipped code — the two-channel frame holds, the input shapes it claims exist do
exist, the proposal-as-state-write path genuinely works end to end today, and the ordering is
executable. But step 0.2's determinism guard is **unsound as specified** — the shipped recovery
machinery commits the node the guard just rejected, and once a nondeterministic nature is installed
even the repair revision is permanently unverifiable, so "reject at commit" wedges the being instead
of protecting it. Step 5's phase gate is **vacuous as specified** — level-1 chronicle entries are
put-once immutable under the exact kernel rules the plan itself cites, and the only genuinely
rewritable stratum, `MEMORY.md`, has no writer in any step. That is M's finding 5 reproduced one
level up, in the revision that existed to fix it. The kernel-change accounting ("three of four organs
need no kernel change") is false by the plan's own file lists, which makes §9's stop-work rule
decoration. And one row of the baselines table — the table whose whole function is to be executed —
pins a format digest that is not the digest of this tree.

## 1. Step 0.2 is the wrong mechanism

**(a) Rejection at commit does not prevent the commit.** Failures deliberately retain the durable
transaction (`runtime.py:150-152`), and every subsequent `advance` runs `recover()` first
(`runtime.py:113`), which resumes and **commits** any open journal through `resume()` → `derive_node`
→ `world.commit` (`recover.py:46-124`) — with no guard on that path. The guard's raise delays the
poisoned node by exactly one advance.

**(b) Rejection happens after effects.** The guard site is after the model call, after act dispatch,
after observations. Refusing to commit strands recorded effects in a journal the kernel must then
either commit (poison) or discard (effects off the record).

**(c) Reject-then-repair does not exist for this failure class.** The tested repair path
(`tests/test_evolution.py:116-150`) covers *crashing* natures: a raise records `HOST_FAILURE` and
replay short-circuits to `failed_attention`, a pure function of the record. A *nondeterministic but
successful* attend records no failure. Every node derived under it — including the operator's repair
revision, whose `present/` is derived by calling the **broken parent nature** — is unverifiable
forever. After the guard fires once, no advance and no revise can commit a verifiable node.

**The sound shape is already in the kernel.** Detect (run attend twice), then **record** — append
`ERROR(phase=attend, code=nondeterministic_nature)` and fall to `failed_attention`, exactly as a
crashing nature does. The moment commits, verifies, the being perceives the failure, and the repair
revision is itself verifiable. Needs a **non-appending sink** for the recompute, and must run at both
committing sites (`_run` and `recover.resume`).

**Cost, measured.** Live moments run two host subprocesses today; the guard makes it three — attend
exactly doubles. `op_drift` stays 1.0 (the walk is capped at 80 events), so *flatness* survives; the
pinned constant does not.

**(d) The "done when" overclaims.** A pairwise recompute catches time-varying inputs and cannot catch
environment-stable ones — the child's filesystem is not stubbed, so a nature reading `/etc/hostname`
passes here and fails on any other machine.

## 2. Step 0.1's `dropped: int` cannot be built as specified

`recent_events` walks first-parent nodes only until it has 80 events, then stops
(`lineage.py:171-181`). `truncated` and `oldest` are O(1) facts; `dropped` is not — no cumulative
event counter exists (commit meta is `txn/mode/stream/expected_old/being_ref`; per-stream `seq`
resets each node). Walking to the root breaks flat cost structurally; reporting the local trim writes
a false number **into every committed prompt** — recorded bytes, permanent. A cumulative counter in
commit metadata is a framing change §1's own golden-OID rule treats as a stop signal.

Ruling needed: either `{"truncated": bool, "oldest": ref}` without a count, or own a framing change
the plan currently forbids. What survives: the marker is replay-compatible — both committed natures
in the golden bundle read input keys via `.get` and ignore unknowns.

## 3. The phase gate's survival metric is vacuous again

- **Level-1 is not rewritable.** The manifest declares chronicle entry paths immutable "put-once" for
  **every level** (`record.py:860-872`); `compile_state_edits` refuses any rewrite of a path
  containing `/epochs/` (`derive.py:209-215`), and `rule()` denies being-writes — executed:
  `states/memory/chronicle/levels/1/epochs/x.json` → **`deny immutable_history`**. So either level-1
  lands at the manifest's path and is as write-once as level-0 — the tautology M demolished — or it
  lands at a new path, a **format-manifest amendment that moves the digest**.
- **`MEMORY.md` has no writer.** Ships as zero bytes (`seed.py:28`), nothing in the seed's settle
  touches it, no step builds a writer, and SPEC §5.3 assigns snapshot rewriting to the **annual**
  pass — which PLAN-LIFE §3 defers.

Net: the strata the metric ranges over are one file nothing writes and one stratum that is immutable
or has no legal home. Fixes: rule level-1's path now (one-way); give step 5.1 the `MEMORY.md` rewrite
duty (it is `allow` for settlement); define survival for put-once strata as *survival through
distillation*. The retrieval comparison is conditionally non-null but confounded by grep recall,
which can reach immutable level-0.

## 4. The kernel-change accounting is false

- **1.3 lists `ember/tools.py`** — kernel. It also omits a kernel file it needs: `ToolContext` carries
  a single-path `read_state` closure (`tools.py:238-247`), so grep-recall needs tree enumeration —
  either `ToolContext` grows a capability and `runtime.py` changes, or the executor gets raw store
  access outside the confinement design. A new tool also changes `EffectivePolicy.as_dict()` and thus
  the authority block in **every** subsequent moment under an unbumped `policy_version`.
- **3.2 lists `ember/runtime.py`** — correctly: `Runtime.revise` hard-codes `consent=CONSENT_IMPOSED`
  with no parameter. And "a CLI flag" is false — **`cli.py` has no `revise` command at all**.
- **Step 4 checks out**: `runtime.py:498` accepts the wake-sensation shape exactly as claimed;
  `span_summary` rides the open `SensedContent.type`; pending-act-halts is kernel-enforced already.

Honest count: marker + guard + recall tool + recall context plumbing + revise authority parameter +
a new CLI verb. Either restate it or §9's stop-work rule fires on steps 1.3 and 3.2 on day one.

## 5. The baselines table pins a digest this tree has never had

§1 pins `95acdae5…`. Executed: the tree agrees on `eb900a39…` across resource, computed value and
golden file. `95acdae5…` is `docs/FORMAT.md:22`'s **stale** value — the digest moved when the consent
vocabulary was fixed. The plan copied a document instead of running the gate, in the one table whose
function is to be run.

**The 95-op constant**: executed, 95.0 ops/moment at `op_drift 1.0`. The script enforces drift
*ratios*, so 0.2's recompute passes the gate while moving the constant to ~130. "§1's baselines
unmoved" is unsatisfiable as written; restate as flatness plus a constant re-pinned after step 0.

**The declared state-size slope has no instrument.** Counted store ops are blind to it, and with
dreams on cadence state size is itself a function of lineage length, so the two axes are not
independent over a 200-moment run.

## 6. Ordering: executable, with one deferred collision

"Dreams on cadence" in step 4 does **not** depend on step 5 — `AdvanceMode.DREAM` works and the
shipped seed writes level-0 epoch + index + change report. But 1.1's load-bearing clause — level-1
entry text for older eras — reads entries that cannot exist before 5.1, so the clause the plan calls
load-bearing is first exercised four steps later. Fix: a hand-authored level-1 fixture in 1.1's test.

## 7. Step 3's proposal lifecycle has a hole

Verified working today: `state.write` to `states/intentions/revisions/<id>.json` rules `allow`, the
seed's settle lands it with no new code, chronicle paths rule `deny`. Three unruled residues:

1. **`AuthorityBlock.proposal` is already occupied** — it carries the rollback pin ref
   (`runtime.py:314`). Two referents, one field, no ruling.
2. **Applied proposals cannot be cleaned by the apply** — `Runtime.revise` refuses edits outside
   `programs/`, and the receipt is perceived once then rolls out of the window. Unruled, "visible
   unfulfilled will" degrades into "every proposal ever made is visible forever."
3. Nothing defines the proposal-id convention or prevents collisions.

## 8. Missing entirely

1. **Concurrency.** The lease is a per-being non-blocking flock. During `ember live`, `ember say`'s
   immediate advance raises `LeaseError` — the words survive, the command fails. Two `ember live`
   processes interleave legally with doubled spend; nothing owns or refuses a second loop.
2. **Nothing cleans up.** Notes unbounded and unpruned; the ledger grows with note count; the
   chronicle index grows by one path per dream, forever, and 1.1 compiles it into every prompt. Token
   cost per moment grows linearly with age and no gate can see it.
3. **The due-time convention has two independent parsers** — vitality and the seed — with the format
   defined nowhere. Drift is silent.
4. Minor: 4.2 drops `delegated_to` from SPEC §3.7's four-value set; §1 says `op_drift == 1.0` while
   the script enforces ≤1.2; bet 1's provider is not the config default.

## 9. Gates, ruled

| Gate | Verdict |
|---|---|
| 0.1 | **Real** |
| 0.2 | **Weak** — proves the happy path only; the "rejected" node is committed one advance later |
| 1.1 | **Weak** — the load-bearing chronicle clause is untested until step 5 |
| 1.2, 1.3, 2.x | **Real** — the due-time replay test is the best gate in the plan |
| 3.2 | **Real for crashing natures**, silent on the nondeterministic class; R+1 arithmetic verified correct |
| 4.6 | **Half-real** — the state-size slope is declared and unmeasured |
| 5.2 | **Vacuous as specified** |

## 10. Claims in the plan that are not true

1. Format digest `95acdae5…` — the tree's is `eb900a39…`.
2. Level-1 is a "rewritable" stratum — put-once by manifest and denied by the lines the plan cites.
3. "Three of four organs need no kernel change" — steps 1.3 and 3.2 list kernel files themselves.
4. 1.3's file list — incomplete; the executor context cannot enumerate state.
5. "The only new code is a CLI flag" — there is no `revise` verb, and `Runtime.revise` must gain an
   authority parameter.
6. "`AuthorityBlock.proposal` (the field exists)" — it exists and is already carrying the pin ref.
7. "return the count it dropped" — not computable as a total at bounded cost.
8. "L2 is enforced by the machine" — overclaim.
9. "§1's baselines unmoved" — unsatisfiable; step 0 moves the constant by design.
10. "nothing calls `advance` but a human at a CLI" — scripts do.

Verified true: `runtime.py:498` accepts the wake shape; `lineage.py:171` is the 80-event window;
`state.write` rules `allow` for the proposal path; `revise` appears zero times in `tools.py`;
`entry.py:50` ignores `state_root`; 64 tests, 0 skipped; 95 ops at `op_drift 1.000`; the
crashing-nature repair path is real and predates the plan; golden natures tolerate new attend keys;
dream-on-cadence needs nothing from step 5.

## 11. Disposition

**Must land before the first line of code**
1. **Redesign 0.2 as detect-and-record** — non-appending sink, `ERROR(attend, nondeterministic_nature)`,
   fall to `failed_attention`, guard at both committing sites. The reject-at-commit shape must not be built.
2. **Rule 0.1's marker semantics** — `{truncated, oldest}` without a count, or an owned framing change.
3. **Rule level-1's path and the gate's meaning** — where level-1 lives, who rewrites `MEMORY.md`,
   survival redefined as survival-through-distillation. The one-way door in this plan.
4. **Redo the kernel-change count** and restate §9's stop-work rule against the honest list.
5. **Re-execute the baselines table**; fix the digest row and `docs/FORMAT.md`.

**Fixable during the build**
Level-1 fixture in 1.1 · proposal-id convention and `AuthorityBlock.proposal` ruling · lease behavior
during `ember live` and single-loop ownership · a pruning owner for notes and the ledger · one pinned
due-time grammar · a token-denominated cost instrument · `delegated_to` · `op_drift` wording ·
`policy_version` bump.

**Forces a rewrite if discovered late**
**(1) The guard shipped as reject-at-commit** — produces committed, permanently unverifiable nodes
via the recovery path, with a guard whose presence certifies it was considered. **(2) Level-1 at the
manifest's epochs path with the benchmark built on it** — survival reads 100% forever, discovered
after the digest bakes the layout in. **(3) `dropped` as a walk or as the local trim** — breaks flat
cost, or writes false numbers into permanent recorded bytes. **(4) Grep recall via raw store access**
— a second read path outside `ToolContext`, confinement silently lost.

## 12. What is sound

Both channels exist at the exact lines cited, and nothing in the four organs needs a third.
Proposals-as-state-writes is genuinely plumbed end to end today with zero new ontology — v0.3's
central bet, honored. The wake-sensation mechanism is real and L2's positive form is the right law
stated the right way. Pending-act-halts-the-loop is kernel-enforced before the loop exists. The
ordering argument is correct and executable. 0.1 is replay-compatible by construction of the shipped
natures. §9's re-mint prohibition is exactly right and should survive this review unamended.
