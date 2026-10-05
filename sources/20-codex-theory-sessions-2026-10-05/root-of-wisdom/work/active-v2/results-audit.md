# Active-inquiry pilot: independent results audit

Audited 2026-10-05 after all six planned participant contexts completed. No frozen input, raw response, feedback, state, or aggregate score was modified. This audit reviewed saved artifacts; it did not dispatch participants or add trials.

**Verdict: no material scoring, feedback, preservation, or stated-reason inconsistency found. The pilot reached a complete ceiling in all three conditions.**

## Preservation and replay

- All **25** file hashes in `run-freeze.json` match current bytes, including the six participant prompts. All **3** treatment hashes also match the earlier `treatment-freeze.json`.
- All **18** raw responses parse directly as JSON. No fence stripping, content repair, or fallback substitution is needed.
- Starting from the manifest's initial states, applying the raw responses through the frozen engine reproduces all **18** saved feedback files and all **6** final states exactly.
- Independently of stored optimality flags and aggregates, the audit reconstructed public posterior supports, query histories, cash spending, and elapsed time from the raw commands and private mechanical answers. Each choice was compared against freshly computed values from the separate verifier implementation. All **66** submitted commands were checked.
- Each round contains exactly the then-open required episode IDs in their prescribed order. All reasons are nonempty strings. No missing, duplicate, unknown, closed-episode, infeasible, repeated, or malformed command occurred.

## Verified outcomes

| Batch | Condition | Optimal initial choices | Optimal visited choices | Queries | Reason word range |
|---|---|---:|---:|---:|---:|
| r01 | Ordinary | 6/6 | 11/11 | 5 | 16–21 |
| r02 | Decision procedure | 6/6 | 11/11 | 5 | 15–29 |
| r03 | Six-question discipline | 6/6 | 11/11 | 5 | 16–24 |
| r04 | Ordinary | 6/6 | 11/11 | 5 | 14–24 |
| r05 | Decision procedure | 6/6 | 11/11 | 5 | 18–28 |
| r06 | Six-question discipline | 6/6 | 11/11 | 5 | 14–24 |

Each condition therefore has **12/12 optimal initial choices**, **22/22 optimal visited choices**, and **6/6 successful matched pairs**. Across the pilot: 36/36 initial, 66/66 visited, and 18/18 matched pairs. All initial Bellman gaps, visited-path gap sums, terminal conditional excess losses, and strict unnecessary-continuation counts are zero.

Every batch pays query fees **5** and terminal action fees **5**, with summed episode elapsed time **13** and realized total loss **26**. Thus each condition totals query fees 10, action fees 10, elapsed-time sum 26, and realized loss 52. Across all contexts the corresponding totals are 30, 30, 78, and 156. These reproduce `scores.json`.

Per-batch realized episode losses in A01–A06 order are **3, 1, 3, 8, 9, 2**. The initial Bayes-optimal value sum is **28**, whereas the selected-world realized total is **26**. The latter is a descriptive outcome under the fixed draws, not a replacement for the expected-choice criterion.

The 66 reasons contain **14–29 whitespace-delimited words** each, totaling **1,352 words**. No 35-word cap violations occurred. These visible word counts do not measure hidden reasoning effort or computation.

## Manual reason review

All 66 reasons were read and compared with the public cases and actually returned evidence. Their numerical comparisons, deadline claims, conditioning, and terminal choices are consistent with the stipulated models. No material contradiction between a reason and its chosen command was found.

All batches follow the same choices within each episode: acquire both inexpensive shares in A01; choose immediately in A02; open, diagnose, and repair in A03; use fallback in A04; choose the statewise-best action without inspecting in A05; inspect and choose the revealed state's best action in A06. They distinguish information that is jointly useful, information too costly to buy, information arriving too late to support repair, and information that cannot improve the action.

Phrases such as “with certainty” refer to exact deterministic observations in the given closed finite model. They do not, in these responses, assert certainty about the wider world or completeness of a philosophical framework. The absence of such broad claims is not itself a measured capacity to detect model inadequacy.

## Limits on interpretation

This is a successful execution and another nondiscriminating pilot. There is **no observed advantage** for the six-question discipline on the measured outcomes. Equal perfect performance does not establish general equivalence, inefficacy, superiority elsewhere, or a unique foundation of reasoning.

There are only two participant contexts per condition, with the same six synthetic episodes drawn from three closely related pairs. Reversed ordering did not change these observed answers, but does not establish absence of carryover or order effects generally. Full priors, response functions, losses, and action grammar were supplied. Cash caps do not bind in these cases; fees and the diagnostic deadline matter. The test therefore concerns selecting available information under stipulated objectives, not discovering omitted variables, revising values, or validating the purposes being optimized.

Only one realized world per episode was retained across conditions and repetitions. The audit checks the choices on those visited paths; it does not elicit full participant policies over every possible query answer. The separate oracle does evaluate public-model continuations, but attributing that complete policy to a participant would exceed the observations. Saved responses and dispatch metadata also do not independently expose hidden model computation or context implementation.

The appropriate next step is to revise the task's discriminating demand, not add repetitions of the same ceiling cases and treat larger item counts as new evidence. Any new design should preserve this result as a limitation of the current test and state in advance which missing capability it aims to exercise.
