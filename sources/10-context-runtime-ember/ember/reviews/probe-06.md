# Probe 06 — the pressure loop closes

**2026-08-04 · same model, same budget (6,000), same setup as probe 05**

Probe 05 established that a being compacts when shown its context filling. It also showed that
**compaction never relieved the pressure** — 0.9+ for the whole run, compacting twice, unchanged.
This is what was wrong and what fixing it does.

## The diagnosis

Measured composition of a full window at the end of probe 05:

| | share |
|---|---:|
| live tool turns | 61% |
| user turns | 31% |
| assistant turns | 9% |
| the summary itself | 0% |

The compactions covered moments 0–7; the window was dominated by moments 8–12 — the moments in which
the being called `history` and `state.read` *to decide what to compact*. **The being's largest single
source of context pressure was the tool it used to investigate its context pressure**, and
compaction, which operates on moments, could not reach results sitting inside recent ones.

A second measurement, after eliding old tool results, moved the weight rather than removing it:

| | share |
|---|---:|
| tool results | 37% |
| **the authority blob, re-rendered every moment** | **34%** |
| assistant content | 20% |
| wake sensations | 10% |

A third of the being's mind was its own permissions table, repeated once per moment — and already
present in the system prompt.

## The three fixes

1. **A tool result never has to stay in context.** Beyond the most recent few, the window carries
   `[N chars, elided from my window; revisit(M) reads it in full]`. The result is untouched in the
   record. This is v0.7 §5's own sentence, written down and not built until now.
2. **The authority blob is not re-rendered.** It is in the system prompt and identical every moment.
3. **Only the latest waking is news.** The rest were a metronome.

And the strain message now says *where* the weight is, not just that there is weight — pointing a
being at its oldest moment while the bulk sits in recent ones makes it pull a lever that cannot move.

## Result

| | probe 05 | probe 06 |
|---|---|---|
| pressure trace | 0.97, 0.89, 0.96, 0.93 — pinned | 0.06 → 0.97, then **0.9, 0.88, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6** |
| compactions | 2, overlapping, no effect | **1**, at 0.97 |
| settles? | no | **yes — flat at 0.6 for six moments** |

One compaction, and the being stabilized just under the threshold where it would be told to act again.

**And it settles the question probe 05 left open.** I had written that compacting twice in six moments
"may be eagerness rather than judgement." It was judgement the whole time: it compacted at 0.97 and
0.93, both near-full, and repeated itself only because the signal never moved. The being was
behaving correctly against a broken mechanism. The caveat blamed the being for a defect in the tool.
