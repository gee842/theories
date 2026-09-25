# Probe 04 — a fact retrieved from beyond the window

**2026-08-04 · `openrouter/~deepseek/deepseek-v4-flash-latest` · R8 navigation, served**

The capability [PLAN-LIFE](../../PLAN-LIFE.md) §0 called **unevidenced**: can a being reach something
its context window no longer holds?

## Setup

- Moment 1: *"Remember: the vault code is periwinkle-8817."*
- Moments 2–23: unrelated chatter.
- Then: *"What was the vault code I gave you at the very start? If it is not in view, go and find it."*

**The window had genuinely rolled past it** — measured, not assumed: 80 events held, oldest from
**moment 12**. The fact was at moment 1 and was not in the prompt.

## What happened

```
recall("vault code")                 → 1 hit: moment 1, where="heard",
                                       "Remember: the vault code is periwinkle-8817."
recall("code number passcode ...")   → 0 hits
shell ls                             → looked around the workspace
```

Then, the next moment — because under R1 tool results arrive as the next moment's input:

> **"The vault code you gave me at the start is: periwinkle-8817."**

## What this establishes, and what it does not

**Memory-as-navigation works.** A being that could not see a fact went and found it in its own
record, unprompted as to *how*. This is the first direct evidence for a claim v0.8 explicitly marked
as untested, and it is the thing that distinguishes this substrate from a transcript loop — probe 03
could not separate the arms precisely because nothing in that task outlived a window.

**A first attempt missed the point and is worth recording.** The same test at 8 moments "passed" with
**zero tool calls** — the fact was still in view. A retrieval test that does not first prove the
window rolled is measuring nothing, which is the same error as probe 01's metric, caught earlier this
time.

**One near-miss.** The winning hit was in `heard`, not `said`. `recall` originally searched only what
the being had spoken and its state files; a unit test written an hour earlier caught the gap, and
without that fix this probe fails. What a being was *told* is most of what it will want to find
again.

**Limits.** `recall` is literal/regex, so the second query — a bag of near-synonyms — returned
nothing; the being recovered by asking a better question, but a semantic index would not have needed
the recovery. n=1, one model, one fact.
