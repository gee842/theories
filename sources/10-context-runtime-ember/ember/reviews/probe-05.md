# Probe 05 — B1: shown its context filling, does a being compact?

**2026-08-04 · `openrouter/~deepseek/deepseek-v4-flash-latest` · budget 6,000 chars · unattended**

The bet named in plan v0.4 and untestable ever since, because `budget` was dead code: nothing
supplied it, so the trim could never fire and the being was never told anything.

**Preregistered:** if it compacts unprompted, the ledger-in-prompt bet holds and compaction is
something a being *does*. If it ignores the pressure across the run, the fallback is mechanical
pruning and the being's agency here is zero.

## Setup

Six topical exchanges to fill the window, then `ember live` with no further input. At the start of
the loop the being's context was **88% full**, and its prompt said so:

> Your context is 88% full (5,3xx of 6,000). Your oldest un-summarized moment is 0. You can
> `compact` a run of past moments into a summary — nothing is lost, `revisit` still reaches them —
> or `self.sleep` if there is nothing worth carrying.

## What it did

```
m1 ['self.status', 'history']          oriented, then looked at the shape of its own life
m2 []                                  answered
m3 ['compact']                         summarized its past, unprompted
m4 ['state.read' ×3]                   read back what it had written
m5 ['history']
m6 ['compact', 'state.read']           refined the summary
```

**B1 holds.** It read its own history before summarizing it, rather than compacting blind — which is
the behaviour the capability was designed to allow and not one the prompt asked for.

## The defect it found

It produced **two overlapping compactions**: `00000000-00000007` and `00000001-00000007`. With
overlapping ranges, which summary a moment gets depends on filename order — an accident, not a
decision. Fixed: the read path keeps the widest summary and skips what that already covers. The
narrower one stays in the record, because nothing here is ever deleted; it is simply not read.

This is what a probe is for. The overlap is obvious in hindsight and appears in no design document.

## Limits

n=1, one model, one budget. It compacted *twice* in six moments, which may be eagerness rather than
judgement — a longer run would show whether it settles. And "88% full" was reached with six turns of
deliberately wordy input, not by a life.
