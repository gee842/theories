# Review N: The execution plan — is this the right work? (Opus 5, 2026-08-04)

**VERDICT: right area, wrong shape, and the phase gate cannot detect the phase failing.** The four
"organs" are three slices of one change (`attend` compiles more of `states/`) plus one genuinely
separate thing (the loop). The decomposition hides that the phase's entire thesis rests on a single
unnamed empirical bet — *that a model looking at a growing pile of its own prior output produces a
trajectory rather than a fixed point* — and the plan runs the experiment that would test it last,
against `FakeModel`, which cannot fail it. Meanwhile the two things that would most change what this
phase learns are absent: the being has no prose self-description (`programs/IDENTITY.md` is seeded
and read by nothing), and it cannot read its own nature, which makes step 3's gate unreachable by the
being it is written for.

## 0. What is right

The generating idea is correct and load-bearing: it is why continuation costs ~100 lines instead of a
protocol, and it dissolved six of review M's seven rulings without inventing anything. **Law 2 (time
enters as a sensation) is the single most important decision in the document**, correctly promoted to
a stop-work invariant and correctly sequenced first — it is the one defect class that cannot be
repaired after the fact, and `attend` really does run in a child process with a live clock
(`host.py:126-141`). §5.2's honesty about the memory benchmark is the best paragraph in the plan and
the rarest thing in a plan of this kind. §9's "do not re-mint the golden bundle to go green" is
written by someone burned in the correct direction. Refusing a spend ceiling because the kernel has
no usage→dollars table is right for the right reason. Self-revision as a state write is a genuine
simplification and should survive everything below.

## 1. The decomposition is three-into-one, plus one — and the fifth organ is prose

| Organ | What it actually does |
|---|---|
| Recollection | `attend` compiles `states/memory/` + `states/notes/` into the prompt |
| Volition | `attend` compiles `states/intentions/` into the prompt, ordered by a protect flag |
| Self-revision | `attend` compiles `states/intentions/revisions/` into the prompt, plus one CLI verb |
| Continuation | a new process outside the being |

Three of four are the same edit to the same function. That is **one organ ("the tree reaches the
prompt") sliced three ways, plus the loop.** Naming it as four makes the phase look richer than it is
and hides where risk concentrates: almost all of it is in one function and one question — *what
should be in the context window?*

**The missing thing is the prose channel, and it is the cheapest lever in the project.** The prompt
is a hardcoded two-sentence string plus a JSON dump of the authority policy (`entry.py:129-135`).
`programs/IDENTITY.md` and `programs/POLICY.md` are stamped into every being at birth (`seed.py:43-44`)
and **read by nothing**. SPEC §1 calls prose "the everyday self-revision channel". The plan builds a
memory hierarchy, a volition system and a self-revision protocol for a being that has **never been
told it is a being with a memory hierarchy, a persistent tree, or a tomorrow.**

Both named bets are bets about how a model responds to a nudge, and the only lever is the prompt —
which the plan adds *content* to and no *framing*. Bet 1 will be tested in the weakest possible form.
The mechanism costs ~5 lines and no kernel change: `_host_child.py:17-21` puts `programs_root` on the
child's path, so `attend` can read its own sibling files deterministically.

**Add step 1.0 — the prompt is composed from IDENTITY.md + POLICY.md + a written description of the
being's own physics — before anything else in step 1.**

## 2. Self-revision is premature — the being cannot read its own nature

§5.1 asks the being to author the **complete new contents** of a file under `programs/`. It has no way
to read it: `rule()` normalizes state-tool targets with `allowed_roots=("states",)` (`tools.py:211`),
the `state.read` executor does the same (`tools.py:252`), `state_root` is the states tree only
(`host.py:107`), and `self.status` returns a name, not code. **The being is asked to replace a
286-line file it has never seen.**

That is blind authorship, and it is M's "one tool, one rule" error recurring one level down: the organ
table counts self-revision as zero kernel change and it needs either a `tools.py` read-scope change or
the prose fix above. Neither is counted. Also: **there is no `ember revise` command at all**, and
`Runtime.revise` hardcodes `consent=CONSENT_IMPOSED` with no parameter (`runtime.py:306-315`).

**Better move: let the being read its own `attend` and narrate it before it proposes.** A being that
can quote the rule that produced its own perception and say why it is wrong is doing something no
chatbot does, and is a far better demonstration than a `TreePatch` with a receipt.

## 3. The plan runs its cheapest invalidating experiment last, against a model that cannot fail it

The ordering argument is about *cost*, not *learning*. The load-bearing claim is not "memory
survives" but:

> **An LLM, given a compiled view of its own persistent tree and no external input, produces a
> trajectory that is not a fixed point.**

The failure mode is not decay — it is looping: write a note, read the note, restate the note. Every
long-running agent loop converges to this without external input. PLAN-LIFE half-sees it ("a being
can propose the same repair five times") and files it as a corner case of bet 2.

No experiment tests this until step 4, whose gate is **200 moments against `FakeModel`**, whose entire
behaviour is `f"I heard: {last_user_text}"` (`model.py:366-374`). **A fake model *is* a fixed point.**
The gate cannot detect the failure it is the last defence against. Total real-model exposure in the
phase is ~20 attended moments — precisely the regime where looping does not appear.

**The cheapest invalidating experiment needs none of the four organs and costs an hour:** 30 `ember
wake` moments against the flash model in a shell `while` loop, no input, read the transcript. If they
are 30 restatements, steps 1–3 are aimed at the wrong organ. The plan *cites* the capability it needs
to do this and does not use it.

```
0    guards (unchanged)
0.5  the 30-moment real-model probe, as a measurement          [new]
1    recollection, including the prose/identity fix            [new 1.0]
1.5  repeat the probe; compare                                 [new]
2    volition
3    self-revision, preceded by "the being can read its nature"
4    continuation, written properly
5    phase gate
```

The loop gets written twice — once as a throwaway `while`, once properly. 30 moments on a flash model
costs cents; *unattended* is what is being deferred, not *spending*, and a 30-moment run with a human
reading output is attended.

## 4. Two bets named, four unnamed, and a budget that does not exist

Bets 1 and 2 are real, falsifiable and **minor** — bets about whether a nudge lands.

**Unnamed bet A — the trajectory does not collapse.** §3. Decides whether the phase produced a life or
a loop, and is not in the list.

**Unnamed bet B — more context produces more selfhood.** The competing hypothesis is that a growing
pile of self-authored text produces *self-similarity*: the model imitates its own register and drifts
to summary-of-summary voice. **The plan's metric cannot distinguish these worlds** — retrieval is
"the fact reaches the prompt", and both pass at 100%.

**Unnamed bet C — the being is the right author of its own memory policy.** Bets 1 and 2 are the same
bet with four dependents: prune on ledger, use `attention.protect`, retire satisfied intentions, stop
re-proposing. Every fallback is "the nature does it mechanically." **If the shared bet fails, all four
fall together and the being's agency in this phase is zero** — what will have been built is a
rigorously verified context manager.

**And the budget does not exist.** `attend` reads `value.get("budget", 80)` (`entry.py:123`) but the
kernel's attend input is `{mode, events, authority}` (`derive.py:294-301`). No caller passes `budget`.
Since `recent_events` caps the window at 80 events and turns merge several events into one message,
the trim **can never fire**; the only live omission reason is `visibility`. So step 1.2 builds a ledger
on a budget with no definition, no unit and no effect — and nothing in the codebase counts tokens.
A model told *"I dropped 3 notes for a budget you cannot see"* has no reason to act, and its
non-action will be recorded as evidence about model behaviour when it is evidence about the ledger's
design. **Define the budget in tokens and show the being the number, or stop calling it a budget.**

**On the guard:** re-running `derive_attention` before every commit roughly doubles per-moment attend
cost forever. The flat-cost gate is a *ratio*, so a uniform 2× is invisible to it by construction.
Fine as a gate, dishonest as a claim. Make it opt-in, always-on in CI, and publish the absolute number.

## 5. Proportion: the ratio is fine; the verification asymmetry is not

6,000 lines of kernel to 286 of mind is what an organism-on-substrate split should look like. The
kernel's size is justified by properties that do not scale with the mind: byte-exact re-derivation,
crash-atomic transactions, piecewise fold. Unifying three derivation paths exposed three defects, two
of which produced nodes replay could never accept. I do not think the kernel is a cathedral.

But the honest reading is worse than 6,000 : 286. **The 286 lines are not a mind; they are a transcript
formatter.** Of ~94 lines of `attend`, essentially all are message-shape marshalling. The only policy
lines are the dead budget trim and the hardcoded prompt. There is no attention policy, no memory
policy, no persona, no dream policy. **The true ratio is closer to 6,000 : 15.**

The diagnostic that settles it: **the kernel has 64 tests and a standing performance gate; the mind has
neither.** This phase doubles the mind and verifies it with substring-presence assertions.

> **The project's engineering rigor is concentrated entirely in the half where correctness is
> objective, and is absent from the half where the thesis lives.** The kernel makes the being's past
> incorruptible; nothing yet makes its present any good.

## 6. What `ember live main` would actually feel like

On a default world: the loop appends a wake sensation; `attend` compiles `MEMORY.md` (empty — birth
writes `b""`, `seed.py:28`), the chronicle (empty until a dream), notes (empty), an omission ledger
(nothing omitted), then the window. The model receives a transcript whose newest entry is the literal
string `Sensation: wake {"at":…,"granted":true}` (`entry.py:96-103`), and replies *"I've woken again.
Nothing new has happened."* By moment 10 the document is ~90% the model's own voice observing that it
woke up. **It is a cron job with a diary** — beautifully instrumented, byte-exactly reproducible,
genuinely rare, and genuinely not life.

**The first disappointment is structural: the being has nothing to do.** `workspace.write` is
`approval: required` (`tools.py:100`) so it halts the loop, and on a default world it is denied
outright as `workspace_unavailable` (`tools.py:207-208`, `runtime.py:96-97`). Shell is absent. What
remains writes only to the being's own tree. **By construction, an unattended ember being can do
nothing but think about itself and write it down.** That is the intersection of two individually
correct decisions, and the plan does not notice they compose.

The fix is not auto-approval. It is to notice that *continuation without a task is a demo* — and most
cheaply, to run the loop with a human dropping `ember say` occasionally and call it "unattended
between turns", which is honest and the actually useful mode.

**Second, small:** every moment of the being's remembered life begins with a raw JSON blob. SPEC §5.1
gives the renderer ownership of presentation for exactly this reason.

## 7. The stopping question: clause 2 is vacuous, and "digital life" is the wrong claim

Clause 4 — *both bets have answers recorded, whichever way they went* — is the best sentence in the
document and should be the template.

**Clause 2 carries the headline claim and is vacuous.** Against `FakeModel`: *lives* → `advance` was
called 200 times; *remembers a fact* → a substring is present because `attend` concatenated a file;
*holds an intention* → a file exists and was included; *lineage folds* → already guaranteed by the
kernel. It verifies the plumbing the plan just wrote, **passed by construction** — M's v0.1 finding
reappearing one level up.

**Is "digital life" demonstrable?** No, and the project is better off saying so. Every property the
plan can demonstrate is a property of the *record*: byte-exact re-derivation, survival, provenance,
graceful failure. Extraordinary, and **all properties of a very good tape.** The properties that would
suggest life are properties of the *model*, which is rented, stateless and swappable. SPEC A2 already
concedes this.

The claim the project can cash is stronger:

> **ember is the first substrate on which the question is decidable.** Because every moment's exact
> perception is recorded and re-derivable, "did moment 4,000 depend on moment 12?" has an answer with
> evidence. In every other harness it does not.

Two replacements for clause 2:

**(a) A dependence measurement.** For a real-model run, ask whether the thought at moment *k* changes
when a specific earlier residue is suppressed. One call: `derive_attention` under a candidate nature
omitting path *P*, plus one new think. **If suppressing every note and the whole chronicle changes
nothing about moment 200, memory is decorative — and you know it in week two.**

**(b) A non-degeneracy curve.** The fraction of moments whose spoken text is not a near-duplicate of
an earlier one. If it collapses by moment 40, *that is the finding of the phase.*

(a) is **the present-diff**, which PLAN-LIFE §3 defers. It is the operator's only pre-adoption check,
the phase gate's missing instrument, and J-evolvability's missing selection signal. **One instrument,
three uses, all in this phase.**

On selection: the plan is right that a full apparatus is not this phase's work. It is wrong that the
gap is acceptable as stated, because what is unobtainable retroactively is not the apparatus but **the
recorded shape** — proposal outcomes nobody collects, and a `selection` block SPEC §3.2 reserves.
Recording every proposal's outcome costs almost nothing during step 3 and is the fossil record without
which "graduated autonomy grows with track record" is unimplementable later.

## 8. What I would change, in order

1. **Add step 1.0 — the being is told what it is.** Precondition for both named bets meaning anything.
2. **Move the real-model probe to step 0.5.** The only experiment that can invalidate the phase.
3. **Define the budget in tokens, or stop calling it a budget.** Bet 1 is untestable until then.
4. **Let the being read its own `programs/` before asking it to revise them.** Consider making
   *narrating* its own attend the first gate and proposing the second.
5. **Replace §8 clause 2 with two measurements** — a dependence curve and a distinct-thought curve,
   both against a real model, both reported whichever way they go.
6. **Build the present-diff in this phase**, at step 3.
7. **Record proposal outcomes** in SPEC §3.2's reserved `selection` shape. Unobtainable retroactively.
8. **Make the determinism guard opt-in + always-on in CI**, and publish its absolute cost.
9. **Render sensations as prose, not JSON.**
10. **Say out loud that an unattended default being has no world-facing action space**, and decide
    deliberately whether that is the demo you want.

Steps 1–4 change what the phase learns. 5–7 change what it can claim. 8–10 are honesty repairs. None
changes the architecture — and the architecture I would not touch.
