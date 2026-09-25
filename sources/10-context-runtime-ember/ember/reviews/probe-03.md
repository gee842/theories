# Probe 03 — the substrate against a bare loop

**2026-08-04 · `openrouter/~deepseek/deepseek-v4-flash-latest` · same task, same sandbox, two arms**

## Criterion, stated before the run

Stated before the run.

- If **both arms** produce the correct `answer.txt`, in a similar number of moments,
  the substrate buys nothing measurable *for a task of this size*. That is the
  honest reading and it weakens the direction's case.
- If **A** succeeds where B fails, or needs materially fewer moments, the record is
  doing work.
- If **A** fails where B succeeds, the substrate is a tax.

This is one task, one model, n=1 per arm. It cannot settle the direction; it can
show whether the obvious comparator was ever going to separate the arms.

## Task

> Your workspace contains a directory `notes/` with several log entry files. Each contains a line `reading: <number>`. Find every reading, add them up, and write ONLY the total (digits, nothing else) to a file named `answer.txt` in the top level of your workspace. Then say DONE.

Correct answer: `2104`

## Result

**both correct — A in 3 moments, B in 5. The substrate is not measurably separating the arms on this task.**

| arm | correct | answer | moments |
|---|:--:|---|--:|
| A · ember | yes | `2104` | 3 |
| B · bare loop | yes | `2104` | 5 |

## Traces

### A-ember

```
m1:  ['shell']
m2:  ['shell']
m3: DONE []
(needed 0 operator approvals)
```

### B-bare

```
m1:  ['shell']
m2:  ['shell']
m3:  ['shell']
m4:  ['shell']
m5: DONE []
```


## What this shows, and what it does not

**The shell works, and the action-space ruling is confirmed operationally.** Three moments: list the
files, sum the readings, write the answer. Probes 01 and 02 spent their lives fighting a JSON schema
whose path convention was never sent to the model; here the being ran `ls`, `grep`, `python3` and
was done. That is the clearest evidence in the record for replacing the tool family with bash.

**The comparator did not separate the arms, and that is the honest headline.** A finished in 3
moments and B in 5, but n=1 per arm on a five-file task is well inside noise, and nothing here
depends on memory across a long run, on compaction, or on branching — which is what the substrate is
*for*. This task could not have shown a difference. Review O's design asked for a comparator; this is
one, and it says: **on a task of this size the record buys nothing measurable.**

**A defect the first attempt exposed.** Before this run, arm A halted: the being called
`workspace.write`, which is `approval: required`, and nothing was there to approve. Meanwhile `shell`
is `approval: automatic` and can write the same file — and strictly more. **An approval gate on a
weaker tool than the ungated one beside it is theatre**: it blocks the polite path and leaves the
powerful path open, and its only effect on an unattended being is to stop it. Either the shell is
gated too, or `workspace.write` is not. The kernel currently believes both things at once.

## What would actually separate the arms

A task that needs something the transcript cannot hold: work spanning more moments than fit in a
window, a fact planted early and needed late, a wrong turn that has to be abandoned and re-approached
from an earlier point. Those are compaction, navigation, and branching — the three claims v0.7 makes
and none of which this probe touched.
