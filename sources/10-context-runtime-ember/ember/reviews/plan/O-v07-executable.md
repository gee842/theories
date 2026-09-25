# Review O: Executability audit — PLAN-LIFE v0.7 vs the shipped kernel (fable, 2026-08-04)

**VERDICT: the direction survives its own probe; the plan does not survive its own kernel.** The §3
deletion table is roughly half real: five rows delete cleanly under the rulings, three delete things
that were never built, and three — the journal, `stream/`, the faces sidecar — delete load-bearing
machinery whose obligations the plan's own kept verbs silently re-create. §6's central mechanism is
unsound at both ends. R7 is claimed as done and is not — two counterexamples executed against the
shipped tree, one of which **permanently wedges a lineage beyond every documented repair verb,
including the operator's own `revise`**, falsifying §6's "already built and tested" floor exactly
where R4 depends on it. §1's "it *is* git" contains a three-way contradiction — shell access,
append-only record, recall by `git log` — of which any two are achievable and the plan promises all
three. §10 diagnoses "every version's central measurement was vacuous until someone executed it";
v0.7's two central measurables — the §6 crash story and the §7 after column — were not executed.

*(Findings 1 and 2 were independently re-executed and both reproduced exactly; both are now fixed in
the tree, along with a third defect the second was masking. See the commit that follows this file.)*

## 1. R7 is not done — the executor raises on ordinary model output

`rule()` is total (`tools.py:200-215`). The next function that takes model output is not.
`ToolExecutor.dispatch` for `state.read` calls `World.read_file`, which raises `TreeError` for any
absent path. `TreeError` subclasses `EmberError`, not `ToolError`, and `_dispatch` caught only
`RefusedError, (ContractError, ToolError, OSError, UnicodeError)`.

Executed: `state.read {"path": "states/notes/tomorrow.md"}` — well-formed, allowed, absent — makes
`advance` raise. The moment dies, the journal is retained, and recovery commits the act as
`unknown / crash_after_authoritative_thought` — a false classification for a read that never
happened. Reading a file before writing it is the most natural act a being has; only F3's prefix bug
kept probe-01 from reaching this. `enact.py` must carry the same obligation to bash exit codes and
MCP client exceptions.

## 2. The R5 floor has a hole that wedges a lineage permanently

The built-and-tested floor covers exactly one class: natures that **raise**. A nature returning valid
JSON of the wrong shape is a different class and is fatal. Executed, with `attend` omitting `prompt`:

- the live moment dies at `neutral_to_wire(...)` with `KeyError`, journal retained;
- every subsequent `advance` runs recover → resume → `derive_attention` → same `KeyError`, forever;
- **the operator's repair `revise` also fails**, because `Runtime.revise` recovers first.

The only repair is hand-deleting `<world>/ember/transactions/<txn>` — an affordance no document
names. This is F4's shape one function downstream of F4's fix, and R4 makes it reachable by the being
on day one, where `shape()` *is* the being's code and the fallback is the entire safety story.

## 3. "The commit is the journal" does not cover the model call

§6's first sentence is violated by §6's own mechanism. Under R1 the commit lands *after* the model
call. A crash between call-start and commit leaves no durable trace a request was in flight:
recovery must re-call (double spend, possibly unreproducible response) or cannot know spend happened.
The shipped kernel guards exactly this — `THOUGHT_REQUEST` appended and fsynced before the connection
opens (`runtime.py:560-576`), recovery refuses to re-send (`recover.py:50-83`), PLAN-LEAN Gate C
names it. v0.7 deletes the journal carrying the guarantee and never mentions the guarantee.

## 4. The multi-command story is a discipline, not a size

`unknown`-never-repeat for the second and third command holds only under a discipline the plan never
states: append-and-fsync outcome *i* before dispatching *i+1*; recovery classifies the first
outcome-less command `unknown` and everything after `cancelled`. Three further holes: the append
cannot live in the working tree (a `git checkout` during a moment destroys it) so it lives under
`.git/` — "backed by git", the posture §1 abolishes; the post-effect conflict window moves rather
than dies, and quarantine is deleted with the journal; and "a three-tool turn is the right number of
commits" never says what the right number is.

## 5. "It *is* git" promises three things; any two are possible

- `.git` reachable in the container ⇒ the being can `update-ref`, rebase, gc, `rm -rf` its own past.
  Objects are immutable; **refs are not**. R4's time travel dies with the DAG it needs.
- `.git` excluded ⇒ `git log`/`git show`/`grep` of history — §5's whole recall story — do not work
  where the being lives.
- Mediated read-only surface ⇒ real machinery with no line item: the faces/Reader control plane
  reborn.

## 6. The control plane does not become git-native; it becomes unowned

**Lease** — git has no primitive; CAS detects the race after the model was paid, and nothing prevents
two `ember next` processes double-spending. **Ingress** — `IngressStore`'s exactly-once inbox is
deleted with journal.py, and conscious-as-record gives dedup nothing to key on. **Secrets** —
`SecretPolicy` refuses literal credentials and redacts every append; SPEC §9.4 calls this a one-way
door. v0.7 has no redaction point, with bash and provider credentials in reach and outcomes committed
verbatim into immutable history. **Visibility** — SPEC §2.1's strata are enforced by the Reader,
which shrinks to ~40 lines while `git show` shows everything to everyone. Three SPEC one-way doors
reversed by a line-count table.

## 7. The §3 deletion table, row by row

Clean under the rulings: quiescence/pending acts/`resolve` (provided the approval question lands
somewhere — R4's time travel cannot un-send what an MCP tool sent); approval-as-mode; clock
law/determinism guard/host purity; `StateEdit`/fold/settle *as a decided cost*; historical-nature
execution; the mode enum; the state-tool family (**the probe's best-supported row**, and understated:
`self.status`'s `describe` lists state paths *without* the `states/` prefix that `rule()` then
denies — the one discovery tool emits paths its own authority rejects).

Deletes things that were never built: the window-truncation marker, level-1 distillation, the
survival benchmark, self-revision approval. Honest housecleaning, but padding in a shrink table.

Not clean: `materialize_face` (finding 5), the journal (findings 3, 4, 6 — ~220 of the 398 lines are
primitives, ingress and secrets the plan's kept verbs require), and `stream/` (finding 8). The O(n²)
claim is **verified true**, but ceasing to inherit parent segments fixes it inside the current
design; sell the ontology on its merits, not on the bug.

Silent losses to name out loud: chronicle/receipt immutability loses its only enforcement and becomes
convention; **A8 receipts die** — an operator commit to the branch is a mind-edit with no receipt;
SPEC A3/A4 are repealed by implication.

## 8. `stream/` — three ways "nothing is lost" is false

1. **Same-moment loss.** An input `shape()` drops in the moment it arrives never reaches any commit.
   That is not forgetting, it is never-having-heard.
2. **Reachability.** A ref inside `conscious.json` does not make a blob reachable; `git gc` collects
   it. Recorded results must live in some node's tree — per-node record files reborn.
3. **Exactly-once delivery.** Dedup keys on committed events. No events, no dedup domain.

## 9. §7's "now" column is honest; "after" is not costed

`journal.py` 398 → ~60: surviving obligations total ≈200-250. `runtime.py` 876 → ~200: ≈300 before
error handling, and **R6 has no line item in any row** — the sleep-honouring loop is a new component
with no owner and no size. `world.py`+`git.py` → ~300: `git.py` alone is 371 lines of near-minimal
adapter, most of which survives, and worktree management is *added*. `record.py` and `model.py` are
plausible. A corrected total lands nearer **2,300–2,600 than 1,620** — still a large honest
reduction; the 4× headline is not.

## 10. What the plan does not say

Migration (v0.7 is a total format break; "the oldest lineage still wakes" is unsatisfiable without a
converter nobody budgets) · `MANIFEST.yaml` and `_check_requirements`, SPEC A2's honest-refusal
mechanism, unmentioned — and editable by bash, a second wedge class · being-branch vs workspace repo
(moment commits polluting project history, or edits leaving the diff-is-the-record story entirely) ·
`ember say` mid-moment · no verb creates a world or a being · approval vs MCP.

## 11. The probe document, verified

Arithmetic checks. F2 verified: `sleep_requested` produced at `tools.py:294`, consumed nowhere, no
loop exists. F3 verified at both cited sites and **understated** (finding 7). F4's fix verified. F5's
cache fix landed. Probe-01 is what the plan says it is — it tested §0's bet, and did not test §6 or
§7, which are v0.7's vacuous-until-executed candidates.

## Claims in the plan that are not true

1. R7 as an achieved property — the executor raises on ordinary allowed model output.
2. "A broken context system still produces a moment … already built and tested" — false for the
   wrong-shape class, which wedges past `advance`, `revise` and recovery.
3. "Effects that leave the repo are recorded before they happen" — the model call precedes its commit.
4. "~60-line append-and-fsync" — what remains includes primitives, an inbox, a pre-call record and a
   conflict story.
5. "the transaction journal (398 lines)" as a deletion — ≈220 are required by kept promises.
6. "append-only in git's sense … the whole integrity story" — refs are mutable; a shell can destroy
   the DAG.
7. "The CLI shrinks to `next`, `live`, `say`" — git cannot init a world, birth a being, hold a lease,
   deliver words mid-moment, or scope a read.
8. "Nothing is lost — the full history is the ancestry" — finding 8.
9. "≈1,620" — not derivable from the obligations the plan retains; R6 has no line item.
10. Four deletion rows delete things that do not exist.
11. "spawning … needs no new ontology" — concurrent writers need the lease conventions being deleted.

## Disposition

**Must land before the first line of code**
1. Close the two executed defects — totality at the executor; a shape contract on host output plus a
   non-looping terminal path in recovery. Neither is v0.7 work; both are prerequisites for R4.
2. Rule the record-protection architecture (finding 5). The plan's one true one-way door.
3. Specify §6 end to end: pre-call record (or an explicit re-spend acceptance revising Gate C),
   per-outcome append discipline with the recovery classification rule, the outcome file's location,
   the post-effect conflict story, and the right number of commits for a three-tool turn.
4. Name the control-plane survivors — lease, inbox, secret redaction, requirements check — with line
   items, or delete the verbs that need them. Give R6 an owner and a row.
5. Write the SPEC amendment batch for the axioms v0.7 repeals by implication (A1, A3, A4, A8,
   visibility, secrets, approval).
6. Rule migration, and re-word the "oldest lineage still wakes" gate accordingly.

**Fixable during the build**
Re-cost §7 (≈2,300–2,600) · birth/init verbs · workspace-repo separation · `say` mid-moment ·
gc/reachability for referenced results · dedup keying · chronicle immutability as convention · MCP
exception totality · the `describe` prefix bug.

**Forces a rewrite if discovered late**
**(1)** The `.git`-exposure choice deferred — a being that rewrites its own DAG is unrecoverable by
definition. **(2)** Outcomes in the working tree — the first `git checkout` during a moment destroys
results of effects that already happened. **(3)** The shape-contract hole shipped into R4 — with the
journal deleted the wedge has no hand-deletable artifact, only a branch whose every advance fails.
**(4)** Secrets committed to immutable history — incident response is history rewrite, contradicting
the one absolute. **(5)** Re-spend under a metered provider.

## What is sound

Probe-before-work, and a probe document whose every checkable claim survived verification — F3 is
stronger than stated. Commit-then-dispatch genuinely deletes today's dispatch-before-CAS quarantine
class, a real simplification the plan under-sells while over-selling everything else. The O(n²)
diagnosis is real and was verified by execution. R6's promotion is earned. The feedback-names-the-rule
principle is confirmed twice in the shipped tree, once where the probe missed it. The "now" column is
honestly measured. Deleting the never-built consolidation apparatus correctly executes M's and N's
rulings. And the core bet — R1's causal chain, R2's recorded conscious, the tree as state — is a
coherent, smaller physics. What this review disputes is not the destination but the claim that the
road is already paved and sixty lines long.
