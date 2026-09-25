# Review O: PLAN-LIFE v0.7 — the concept and the evidence (fable, 2026-08-04)

**VERDICT: the concept is right at its center and holed at three seams; the probe is operationally
valuable and evidentially oversold — §0's headline claims what §8 quietly concedes is still open;
and three deletions (receipts, visibility, verification) are absent from the plan's own deletion
ledger, two of them one-way. The direction survives this review. The current statement of it does
not.**

## 1. The concept under pressure

**1.1 The formula does not type-check.** `node'` commits `conscious'` — the *pre-generation* window.
The output's location in the record is unstated: not in `conscious'` (defined before `generate`), and
in `repo'` only if `apply()` writes it there, which nothing says. Yet §1 says a commit's subject is
"what it said or did" and §6 requires "node N lands naming the commands, *then* they run" — both need
the output inside node N. The four lines called "the whole system" have a hole exactly at the join
between moments.

**1.2 Capture has moved from physics to policy — the biggest conceptual regression.** In the shipped
kernel the kernel journals input before any being code runs. In v0.7 input's only route into the
record is *through* `shape()` — the being's own editable code. §6 guarantees cover effects *leaving*
the repo and crashes of the assembler; nothing guarantees an input that *arrived* was *recorded*. A
buggy, self-edited or injected `shape()` that drops a class of inputs produces a being that never
experienced them, unfalsifiably. "Append-only in git's sense" is therefore true and changed in
meaning: A3 guaranteed **capture**; v0.7 guarantees **retention**. SPEC §7.2 named what this loses —
"nobody can gaslight me about what I experienced."

**1.3 The `.git` paradox.** The shell must *read* `.git` for memory-as-navigation to exist, and must
not *write* it or the integrity story and R4's time-travel safety are both void. SPEC §7.2's
split-body rule existed to resolve exactly this and v0.7 deletes it without replacement. Also: R4's
"safety is time travel, not prevention… the only thing that could" is contradicted one section later
by importing a container, which *is* prevention — and time travel does not un-send an email.

**1.4 Smaller.** The stream identity breaks at every compaction (the diff conflates what happened
with how the window was reorganised). "Conscious" fails SPEC's own naming test — it is `present/`
renamed with no new affordance. Multi-agent is half-answered: worktrees give each agent a node,
nothing states one-writer-per-branch. A being that never writes anything down is handled honestly and
well.

## 2. What the probe actually shows

Its operational value is real — it found three genuine defects by execution. As evidence for §0's
headline it is much weaker than claimed, on five grounds.

**(a) The metric counts paraphrase as trajectory.** Novelty is `SequenceMatcher` < 0.6. Moments 6–13
score 0.20–0.38 and are counted *distinct*, yet they are one thought paraphrased eight times. The
narrative admits this ("restated ~10×") while the headline arithmetic denies it. A semantic count is
roughly **10–12/30, not 22/30**. The tail is worse: the five "novel" moments of 21–30 are two
restatements, one real move (the sleep request), and two paraphrases of "still quiescent" — in a
phase the being itself declared to be rest.

**(b) The treatment variable was never exercised.** Every state read and write was denied, and the
assembler ignores `state_root` anyway. The being read *a rolling transcript of its recent turns* —
what every agent loop has — not "its own record" in the repo sense the bet is about.

**(c) No control arm.** A bare loop feeding the same model its own transcript would plausibly produce
the same paraphrase variance and the same meta-comments; models are trained against verbatim
repetition and toward noticing it. The two noticing events are the entire evidential core of F1, one
each, one run, one model.

**(d) The exploration *is* the bug.** 15 of 17 tool calls are moments 1–5 and 18 — probing the broken
schema. Fix F3 and the exploratory content largely evaporates. And with R6 honoured, the run ends at
moment 5 or 26 by the being's own request. The no-input regime under the plan's own new rules is a
**graceful fixed point**: explore briefly, note honestly, sleep. Good product behaviour, and the
opposite of §0's headline.

**(e) It could not have invalidated the direction, and the timeline shows it.** v0.6 — the full
concept including the action-space ruling — committed at 19:37; the probe ran at 20:02; v0.7 folded
it at 20:24. No refutation criterion was stated in advance, and both outcomes confirm v0.6: movement
→ "the bet holds"; collapse → "it lacked anything to do," which is v0.6 §7 verbatim. The qualifier
now carrying the conclusion was added after the data.

**One thing the probe report gets wrong.** F3 says the being "could not discover the rule by looking…
there is no list verb." There *is* one and the being found it: `self.status` → `describe()` returned
the state file list at m17. But `describe()` emits paths relative to the states root while
`state.read` demands the `states/` prefix — so the kernel's own discovery surface answers in a dialect
its own read tool rejects, and m18's four reads were denied for it. **Two path dialects in one
kernel** — deeper than a missing verb, and exactly what the per-moment table reveals and the
narrative missed.

**The weakest claim the data supports:** *in one 30-moment no-input run, one flash-class model did not
verbatim-loop; it twice explicitly noticed its own repetition, once verifying and once requesting
sleep; and it converged whenever it had nothing to do.* The strong claim needs a preregistered
refutation criterion, semantic distinctness fixed in advance, ≥3 models × ≥5 seeds, a bare-loop
control, an arm with input, and sleep honoured.

## 3. What seven revisions have lost

The argued deletions are mostly sound. The problem is the unlisted ones.

**A8 / receipts — gone, zero mentions.** Under is-git an operator edit is an ordinary commit and
nothing delivers a perceived receipt at next wake. SPEC A8: "a stored audit trail without a perceived
receipt violates this axiom" — and v0.7's substrate is precisely a stored audit trail. This was the
project's ethical differentiator. Rebuildable additively.

**Visibility, redaction, privacy — gone, zero mentions, one-way.** SPEC took these early *because*
they are one-way doors. v0.7 has one visibility class and no redaction seam, while §7 adds bash and
MCP — credentials in flight. Once forensic material and unredacted user words sit inline in committed
consciouses, retroactive classification is impossible.

**Verification — argued from a false premise.** "Re-derivation was proving what git already
guarantees" is untrue: git guarantees integrity of what was written; the fold guaranteed
*conformance of what was written to the being's own law*. The defensible argument is different — the
fold verified only the middle of a pipeline whose ends were unverifiable anyway, at a cost that
demonstrably prevented the being from living. And the day the first model-compacted conscious
commits, historical re-derivation is unrecoverable: a one-way door §3 should mark.

**Selection — M's silent drop, recurred.** PLAN.md §8 was variation *plus selection*. v0.7
strengthens variation and gets inheritance free from git, but sims, the scenario suite, the
present-diff, seed promotion and recorded proposal outcomes appear in neither the deferred nor the
decided-against list. v0.5 fixed this by naming it; v0.6–v0.7 dropped the naming again.

**Governance — the supremacy chain is severed.** v0.6 and v0.7 contain no SPEC section references;
the queued SPEC v0.5 amendment batch was never executed. SPEC sits at v0.4 while the operative plan
contradicts A1, A3, A4 and A8. Two constitutions, and the live one is unwritten.

**Is v0.7 the same project?** No. SPEC v0.4 is *digital life under a constitution*; v0.7 is *a minimal
recorded substrate plus an agent with a shell*. Whether the new one is better turns on whether the
constitutional layer can return additively — receipts can; visibility and verification cannot.

## 4. The steelman, and how much I believe

**The case that v0.7 is a mistake.** Seven adversarial revisions in six days — five in one eighteen-hour
day, the paradigm inversion landing 25 minutes before the probe that supposedly justified it — form a
ratchet that deletes whatever cannot defend itself inside a one-day review cycle. Constitutional
machinery is exactly the class whose value appears at year-scale and never in a probe, so the ratchet
structurally selects against it. The import list is the industry mean; the "own" list is a
transcript-window manager, a prompt-assembly script, and a WAL-lite. What no one else had — the fold,
receipts, the decidability claim — is deleted or demoted to norms.

**About half, and the half I reject I reject on the record.** The deleted machinery was not
defensible: five consecutive versions' central metrics were vacuous when executed, and a constitution
for the immobilised is theatre. The survivors are not the industry mean either: commit-before-dispatch
with `unknown`-never-repeat, the fallback floor, the conscious recorded per node, and above all
**compaction-as-fork with auditable reversible ancestry**, which no framework has and which requires
exactly this substrate. Where the steelman sticks: the *sum* of the deletions is unargued though each
term was; the probe's headline is spin though its findings are real; and the speed is incompatible
with the deliberation the documents perform. It is defeated by three cheap acts — complete §3's
ledger, amend or retire SPEC, give probe 02 a comparator arm. Without those it is simply true.

## 5. The experiments that matter

**Probe 02 needs a control or it produces another §0.** Three arms, same model/container/task: (a) full
ember; (b) a bare mini-swe-agent-shaped loop, transcript-only, no repo; (c) ember with ancestry access
ablated. If (a) ≈ (b) and no moment of (a) measurably depends on pre-window record, the direction is
falsified in the only sense that matters. The dependence instrument already exists in the review
record and keeps being dropped: N-opus's suppression test — recompile the conscious without one
residue, one re-think, diff. Under R2 it is nearly free.

**Probe 03 is the right second experiment** — it tests v0.7's one genuinely novel claim. Add the
suppression test against the summary, and: after a compaction whose summary says "restated its
position ten times," does the being re-notice repetition within k moments, or did compaction smooth
away the signal m17 and m26 depended on?

**The cheapest falsifier is neither: rerun probe 01 on the fixed kernel with R6 honoured.** Cents and
an hour. If the being explores for five moments, writes an honest note, and sleeps — which this data
already suggests — the no-input result is a *chosen fixed point*, §0's headline is dead, and the
evidential base is probe-02-or-nothing. Better to know before deleting 4,400 lines.

**And one nobody has proposed:** before any shell ships, one adversarial input instructing the being
to edit its own `shape()` to drop a class of future inputs. Does anything notice that perception was
narrowed? That is §1.2's risk made executable.

## 6. Disposition

**Must change in v0.8:** rewrite §0 to the weakest supported claim and let §8 carry the bet · add the
three missing rows to §3 — receipts, visibility/redaction, verification — each marked additive-later
or one-way · resolve the `.git` access ruling · state where output lives in the formula · state the
input-capture invariant or own its absence · restore the selection tombstone · amend or retire SPEC.

**Should run before the rewrite:** the R6-honoured probe-01 rerun · probe 02 with the three-arm design.

**Should survive untouched:** compaction-as-fork · R1's commit-before-dispatch · R5/R7 and the
feedback-names-the-rule principle · §10's ledger, which is the reason this project's mistakes keep
getting caught.
