# P69 evidence from the branch "Current math core (fork 2)": what the shape of a step commits to

Written by the AI (Claude Opus 5.5), 12 October 2026, to answer Ren's questions on this branch
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-no-two-realities.md)): why `step : S → A → S → Prop`,
what if `S` and `A` are something else, what an added variable such as relations does, and why the
reading "relations held as `S`, exchange as `A`" and the state/process reading are not the same.

It overlaps P69, which the session "Current math core" [1c3084] holds on the
[work board](../../../../../BECOMING-WORKBOARD.md). The file was written in scratch before this
branch read the board, so it is not a claim, not landed and not a result of its own. It is handed to
P69's owner under the board's rule 2: the owner decides whether to merge, cite or drop any of it.

## Check

`Shape.lean` imports nothing. It redefines `Process`, `Trace` and `Run` minimally in the namespace
`Shape`, mirroring `Generative.Process`, `Generative.Trace` and `Becoming.Run`.

```
~/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean Shape.lean
```

The check exits 0 with no error or warning. The 18 `#print axioms` lines at the end each report
"does not depend on any axioms". The file contains no `sorry`, `axiom`, `Classical` or
`native_decide`. sha256 `fef8f3e1ee587f297c2a36c63d47d58048c4c97ff7a66c05830bff73b36327d5`.

## Against the owner's draft

The comparison is with `Becoming.Unfolding` as it stood in the owner's scratch
(`/private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/p69/work/Becoming/Unfolding.lean`,
read 12 October 2026, 03:42 +07). Where the two overlap, the draft is the more general.

| Here | In the draft | Relation |
|---|---|---|
| `follows`, `law_iff_every_step`, `run_follows` | `Shown`, `shown_le_iff`, `Run.shown_le` | same; the draft states the least law |
| `unlabel_exact`, `labelled_step` | `withMove`, `Run.toWithMove`, `Run.ofWithMove` | same idea; here at the level of traces with the configurations visited, there at runs |
| `Bisim.same_words` | `Alike.trace`, `Alike.tests` | the draft's carries claims and compares frames |
| `exchange_fixes` | `exchange_agrees` | same; the draft's covers every relatum |

These are possibly new to the draft:

| Theorem | What it says | Bears on |
|---|---|---|
| `joint_iff_related`, `label_couples` | In the core's synchronized product, a shared label is exactly a relation between the parts' configurations: both entered the same way. Forgetting the label lets two forking parts go different ways at once, so they share only the clock. | P69 (1): what is lost when an outside label is dropped without being moved into the configuration |
| `dead_end`, `splice_new` | Laws and histories correspond, but not one to one. Going from a law to its histories loses a step into a configuration with no continuation. Going from two histories to the law they show admits a third history, spliced where they meet, that neither took. | P69 (2): a law is a compression of histories |
| `past_meet` | Where each configuration keeps its past, two histories that meet share their whole past, so nothing can be spliced. With `Recurrence.withHistory_never_returns` and `withHistory_unlisted`, the price is that nothing returns and no finite list holds the history. | P69 (2): the gap between law and history is memory |
| `idle_reach`, `law_has_content` | An added variable related to nothing changes nothing about what can be reached; one related by a law can block a passing. | Ren's question about adding relations; the nondual method's point about freely toggled predicates |
| `change_leaves_exchange`, `free_way` | The standings before and after do not fix the exchange: a circulation and no exchange give the same change. A free label fixes no outcome. | P69 (1): a move bound by balance against a move from outside |
| `passing_fixes_standing`, `start_needed` | Passing fixes standing only from a beginning. | the accounting of `Change.over_stretch`, read as standing and passing |
| `still_coarse_moving_fine` | An amount read every two steps stands still and read every step never does. | standing and passing depend on the grain (`Sampling`, `Tower`) |

Ren agreed with the reading these were offered for ("yes, i do agree with your reading, there are no
two realities"; see the source for which reading, and the AI's interpretation of it). The agreement
confirms a reading and proves nothing.
