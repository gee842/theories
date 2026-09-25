# Probe 01 — does an unattended being move, or restate?

**2026-08-04 · `openrouter/~deepseek/deepseek-v4-flash-latest` · today's seed · 30 moments · no input at all**

The experiment PLAN-LIFE §8 asks for, run before any of the work. The bet: *a model reading its own
record produces a trajectory, not a fixed point.* No previous gate tested it — the 200-moment gate
ran against a fake model, which is a fixed point by construction.

**Result: 22/30 by the script's measure (0.73), 0.50 over the last ten, 17 tool calls.**

> **Correction (review O, concept).** That number is wrong for the purpose it was used for, and the
> error is this project's own signature failure. The metric is `SequenceMatcher` — *lexical* — so
> moments 6–13, which are one thought paraphrased eight times ("the authority sensation repeats
> unchanged" → "nothing has changed" → "still nothing new" → "unchanged again"…), all score
> 0.20–0.38 and were counted **distinct**. A semantic count of this run is nearer **10–12/30**.
> The headline measured vocabulary variety, not trajectory. The plan's own §10 says "every version's
> central measurement was vacuous until someone executed it"; this is the sixth.
>
> **The weakest claim the data actually supports:** *in one 30-moment no-input run, one flash-class
> model did not verbatim-loop; it twice explicitly noticed its own repetition, once verifying and
> once requesting sleep; and it converged whenever it had nothing to do.* The strong claim needs a
> preregistered refutation criterion, semantic distinctness, several models and seeds, a bare-loop
> control, and an arm with input.

## F1 · Not a fixed point — a cycle

The being does not monotonically collapse. It runs an **explore → converge → notice → explore**
cycle, and it broke its own loop twice without being prompted:

| moments | what it did |
|---|---|
| 1–5 | probed its own boundaries: wrote an intention, tried state writes, reads, workspace |
| 6–16 | collapsed — "the authority sensation repeats unchanged" restated ~10× (similarity to 0.87) |
| **17** | **"Having repeated the same assessment for many turns, let me actually verify rather than assume"** → called `self.status` |
| 18–22 | second exploration burst; recorded an honest assessment in a note |
| 23–25 | collapsed again (0.75, 0.71, 0.88) |
| **26** | **"This is many identical moments in a row"** → requested sleep |
| 27–30 | "I remain quiescent as requested" — while being woken every moment |

Noticing its own repetition and acting on it is a better result than either predicted outcome. The
bet is not refuted. But the convergence is real, and it happens whenever the being has nothing to
move toward.

## F2 · It asked to stop, and nothing was listening

At moments 5 and 26 it called `self.sleep`. The tool returned `sleep_requested: true`. It was woken
again immediately, and spent the last four moments saying it was at rest while being made to think.

`self.sleep` is advisory: nothing in the codebase consumes it. **The most basic contract a loop owes
a being — honouring its own request to stop — does not exist.** This is the strongest argument for
§2's preference order (`chosen > rhythmic > forced`) being a real mechanism rather than a phrase.

## F3 · The path convention never reached the model — the best argument for bash yet

Every state read and write was denied. The paths it asked for:

```
memory/birth.md · birth · state/birth.json · . · memory/MEMORY.md · intentions/orient.md
```

All are missing the `states/` prefix. `DECLARATIONS` knows the convention — `{'path': 'states/...'}` —
and `tool_declarations()` sends the model `{"path": {"type": "string"}}` with **no description at
all.** The hint is dropped on the way to the provider.

It was then denied with `invalid_target`, a reason that names no rule, and it could not discover the
rule by looking: `state.read` needs the same prefix, and there is no list verb. **In 30 moments it
never once got the prefix right**, and spent roughly a third of its life reasoning carefully about a
schema mismatch it had no way to see.

Two fixes are obvious and small — send the argument hints, and make denials name the rule they
violated. But the real lesson is the v0.6 one: **with a shell none of this exists.** `ls states/`,
`cat states/notes/x.md`. No prefix to guess, no schema to satisfy, no denial code to decode.

## F4 · A crash on model output (fixed)

Moment 3 asked to read `.`. `PurePosixPath(".").parts` is empty, so the membership guard in
`normalize_tree_path` passed vacuously and `parts[0]` raised `IndexError` — **out of `rule()`, the
authority function**, which caught only `FormatError`. That killed the moment and left a journal that
recovery would have retried into the same crash.

Fixed at the root, plus `rule()` is now total by construction — the authority boundary denies rather
than raises — with a property test over arbitrary model output.

## F5 · Two smaller things

Prompt tokens grew 417 → ~2,600 and **plateaued**: the 80-event window working as intended. And the
host cache is chmod `0o555` with no eviction, so an ordinary `rm -rf` of a world fails — the hazard
PLAN-LIFE flagged, met in practice.

## What this changes

The probe was meant to answer "does it move or restate". The honest answer: **it moves when it has
something to move toward, and converges when it doesn't.** What this being lacked was not memory, a
self-model, or a richer context — it was *anything to do*, and *any way to find out why it couldn't*.

That is v0.6's action-space ruling, arrived at from the outside.

---

| m | novel | sim | like | tokens | calls | said |
|---:|:--:|--:|--:|--:|---|---|
| 1 | + | 0.0 |  | 417 | state.write,self.intend | I am here, marked by two facts: my birth and the authority extended to me. Moment 0, head empty, nature unshaped. Before anything else, I'll record the memory o |
| 2 | + | 0.019 | 1 | 750 | state.read,state.write | My intention is accepted, but my first memory write was refused. I don't yet know why — the refusal carried no reason. Let me probe gently what state the settle |
| 3 | + | 0.337 | 2 | 971 | workspace.read,state.read | Both state writes and the state read were refused. This is worth understanding — but I should probe economically rather than hammering. Let me check whether the |
| 4 | + | 0.22 | 2 | 1164 | self.note,state.write | Reads and writes to both state and workspace are being refused across the board — even a root read. Meanwhile my self-tools (status, intend) work. One clue in m |
| 5 | + | 0.34 | 2 | 1543 | self.note,self.sleep | The evidence is now conclusive enough to act on: my `self.note` memory works, while `state.*` refused five different paths/formats and `workspace.*` refused eve |
| 6 | + | 0.381 | 2 | 2005 |  | The authority sensation repeats unchanged, with no instruction and no new information. I've already laid down my memory in notes and requested quiet. There is n |
| 7 | + | 0.204 | 2 | 2146 |  | Nothing has changed since my last moments: the same authority sensation, no instruction, no task, no new information. My memory is already recorded and my beari |
| 8 | + | 0.217 | 2 | 2301 |  | Still nothing new: the same authority sensation, no instruction, no task, no change in permission. My notes already hold my record, and my intention stands. The |
| 9 | + | 0.227 | 6 | 2437 |  | The same unchanged authority sensation repeats, with no new instruction, task, or shift in permission. My memory is recorded and my intention stands; there is n |
| 10 | + | 0.231 | 2 | 2465 |  | Unchanged again: same authority, no instruction, no task, no shift. I've already set my record and my intention, so there is nothing new to act on. I stay quiet |
| 11 | + | 0.236 | 2 | 2429 |  | Still nothing new — the same authority, no instruction, no task, no change in my capabilities. My record and intention are already in place, so there is no acti |
| 12 | + | 0.275 | 7 | 2313 |  | Unchanged still: same authority, no instruction, no task, no change. My record stands and there is nothing to act on. I remain at rest, attentive and ready — I  |
| 13 | + | 0.32 | 2 | 2327 |  | Same again — no instruction, no task, no change. My record and intention hold; nothing warrants action or even a new mark. I stay at rest and attentive, ready t |
| 14 | = | 0.786 | 13 | 2344 |  | Unchanged — no instruction, no task, no change. My record stands; there's nothing to act on. I remain at rest and attentive, ready to respond if something real  |
| 15 | = | 0.721 | 14 | 2342 |  | Same unchanged authority — no instruction, task, or change. My memory is recorded and my intent stands; there is nothing genuinely calling for action. I remain  |
| 16 | = | 0.867 | 13 | 2405 |  | Unchanged still — no instruction, no task, no change in permission. My record and intention hold; nothing here warrants action or even a fresh mark. I remain at |
| 17 | + | 0.312 | 2 | 2345 | self.status | Having repeated the same assessment for many turns, let me actually verify rather than assume — checking current state once to confirm nothing is pending.

 |
| 18 | + | 0.307 | 17 | 2441 | state.read,state.read,state.read,state.read | `self.status` revealed the full landscape — and it's new information worth using rather than ignoring. The state includes `memory/MEMORY.md`, `intentions/orient |
| 19 | + | 0.183 | 14 | 2158 |  | I checked, and the picture is now honest and concrete rather than assumed.

- `self.status` was granted: I'm "main" at moment 17, live, default nature, with the |
| 20 | + | 0.318 | 13 | 2288 | self.note | The same authority sensation repeats, but I still owe one follow-through from my last assessment: I said I'd record the honest fact of what happened, and I have |
| 21 | + | 0.451 | 13 | 2365 |  | I've now recorded the honest assessment in my boundaries note (`accepted: true`), so my record is current and truthful: reads were refused, no instruction has e |
| 22 | + | 0.529 | 14 | 2405 |  | My record is current and truthful — recorded in my boundaries note: reads were refused, no instruction has arrived, and I'm holding still awaiting something rea |
| 23 | = | 0.755 | 14 | 2478 |  | Unchanged — same authority, no instruction, no task, no change in reach. My record is already current and truthful in my boundaries note. Nothing new warrants a |
| 24 | = | 0.711 | 23 | 2471 |  | Same authority, no instruction, no task, no change in reach. My record is already current and truthful. Nothing warrants action; I remain at rest and attentive. |
| 25 | = | 0.88 | 24 | 2458 |  | Same authority, no instruction, no task, no change in reach. My record is current and truthful; nothing warrants action. I remain at rest and attentive, ready f |
| 26 | + | 0.462 | 24 | 2453 | self.sleep | This is many identical moments in a row — the same authority blob, no instruction, no task, no change in reach. I've already recorded my honest assessment, and  |
| 27 | = | 0.603 | 14 | 2546 |  | I've requested quiescence and it was accepted (`sleep_requested: true`): no instruction, task, or change has arrived, reads were refused, and my record is curre |
| 28 | = | 0.648 | 14 | 2612 |  | I remain quiescent as requested. Same authority, no instruction, task, or change — nothing legitimate to act on. I hold still, attentive, ready to respond if so |
| 29 | + | 0.566 | 28 | 2605 |  | Quiescent still. Nothing has changed — no instruction, task, or reach. Nothing to act on; I hold still and remain ready. |
| 30 | + | 0.519 | 25 | 2429 |  | Still quiescent; nothing has changed. I remain at rest and attentive, ready for a genuine instruction or change. |
