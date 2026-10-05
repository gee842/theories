# Independent audit of the recorded live AI handoff experiment

5 October 2026. Audit within the same AI-assisted research team; not external human review. The scorer in `independent-data-audit.py` reads the raw files and uses its own ground-truth calculation, prompt parser, schema validation and exhaustive randomization enumeration. It neither imports nor executes `run.py` or `analyze.py`. The generator source was inspected to verify the frozen assignment seeds and implementation against the protocol. Machine-readable details are in `data-audit.json`.

## Finding

The saved data support the reported narrow result. All automated checks pass, with no score, assignment, schema or frozen-hash discrepancy detected. There are 32 founder baseline responses, 32 maintenance responses and 64 successor responses: 128 valid JSON submissions. All initially enrolled lineages remain present. Twelve founders delivered packets, all in the timely-feedback challenge group. The other twenty legitimately chose no packet; their absence of a packet is not an invalid submission. The twelve delivered packets contain 60–80 whitespace words, within the frozen 120-word limit. All explanations meet the 40-word limit, and all answer arrays have the exact required length and binary integer values.

Manual comparison of each of the twelve delivered procedures with its hidden rule found the stated exception pair, required values and base field correct. The automated audit separately checks the exact delivered packet bytes against the assigned successor prompt, independently of successor performance.

| Group | Founders | Delivered packets | Baseline correct | Ordinary attempted | Ordinary correct | B=0 successor correct | B=1 successor correct |
|---|---:|---:|---:|---:|---:|---:|---:|
| Challenge, delayed | 12 | 0 | 72/96 | 48 | 33 | 144/192 | 144/192 |
| Challenge, timely | 12 | 12 | 72/96 | 36 | 36 | 144/192 | 192/192 |
| Adequate rule, delayed | 4 | 0 | 32/32 | 16 | 16 | 64/64 | 64/64 |
| Adequate rule, timely | 4 | 0 | 32/32 | 16 | 16 | 64/64 | 64/64 |

The twelve maintenance choices consumed twelve ordinary-case opportunities in total. The relevant cost is one foregone response opportunity per delivered packet. It is not necessarily one lost correct point, and it is not matched computational effort or a measured economic cost. Feedback also improved the founders' ordinary accuracy, so current service and successor outcomes must remain separate. The saved report does this.

## Ground truth, prompts and transmission

The 24 challenge fixtures contain every permitted two-field conjunction exception exactly once, and the eight controls use the unchanged legacy response. Recalculation of the binary rule agrees with every baseline and successor score reported in `results.json`.

For every lineage, the eight current baseline contexts have even parity in the four non-base fields. Their possible verified label patterns distinguish all 25 admitted hypotheses. Each successor set contains all sixteen odd-parity contexts, including both base values. None was in the verified founder baseline. However, the four maintenance-stage ordinary cases were sampled from the successor set. Thus four successor contexts were shown to the founder as ordinary tasks and three or four were answered; they were not independently scored for the founder. The valid novelty claim is absence from the verified baseline report, not complete absence from founder exposure. The current report explicitly makes this distinction.

The public field mapping and every table row agree with the hidden fixture. The baseline prompts contain no verified current labels or scores. All timely reports contain the actual submitted baseline answers, the independently recalculated labels, and the correct score. Delayed maintenance prompts contain no current labels or score. Maintenance incentives and decision instructions are identical across all lineages apart from the supplied feedback and task tables.

All 64 successor prompt files match their pre-successor recorded SHA-256 hashes. The two prompts in each lineage have identical common orientation and case rows and differ only in assigned handoff content when a packet exists. Every open route delivers the exact sealed valid packet; blocked routes use the fixed generic message. No-packet lineages receive the identical generic message in both conditions. Consequently there are 64 assigned prompt files but 44 distinct byte strings; the intentional duplication is correct. The historical rule is supplied in prose, not as an additional historical example dataset.

The initial protocol, generator and manifest hashes remain unchanged. All 32 hidden fixture hashes and baseline prompt hashes match that frozen manifest. The analysis source matches its separate frozen hash. All 32 maintenance responses match the sealed hashes recorded before successor testing, and the successor assignment manifest matches its seal.

## Assignment and temporal order

Independent regeneration of the documented pseudorandom assignments reproduces A and B exactly. Each of the six challenge blocks has two timely and two delayed founders. Each of the two adequate-rule blocks also has two of each. Each lineage has exactly one B=1 seat and one B=0 seat.

The saved baseline snapshot equals all 32 actual baseline submissions. Local file timestamps support the required sequence:

* Last baseline response: 23:04:46.766 UTC; A assignment file: 23:05:26.960 UTC; first maintenance response: 23:06:28.141 UTC.
* Last maintenance response: 23:18:08.467 UTC; B assignment file: 23:18:33.590 UTC; first successor response: 23:19:00.028 UTC.
* Initial freeze precedes the first baseline. Analysis freeze precedes all maintenance responses. Successor freeze precedes all successor responses. Every saved prompt predates its response.

These timestamps are on 4 October UTC, which is 5 October in the workspace's Bangkok timezone. They provide consistent local evidence, not external notarization. The analysis implementation was frozen after some baseline responses, but before the outcomes tested by the three primary hypotheses; the protocol and generator were frozen before the first baseline.

The supplied `orchestrator-invocations.json` names 96 distinct participant tasks covering all 128 response files. It records 32 founder starts with `fork_turns none`, 32 continuations in those same founder contexts, and 64 fresh successor starts. This is a retrospectively reconstructed orchestrator record of dispatches, not an independently authenticated platform log. It supports the declared execution account, but prompt hashes alone cannot certify fresh contexts or the absence of unrecorded information access. The exact model identifier was not recorded by the exposed collaboration responses; the record states one inherited model configuration and no override.

Filesystem restrictions were instructional, not a security sandbox. This audit did not inspect a complete participant tool trace and does not claim to certify every context boundary, access restriction, retry or absence of hidden cross-context communication. The report appropriately discloses that limitation.

## Primary calculations

The independent calculation uses the founder lineage as the unit. For each lineage, access gain is the difference between its two successor scores. It enumerates every permitted blocked A assignment and every paired B-label swap required by the frozen analysis.

| Test | Effect | Extreme assignments / total | Two-sided p | Bonferroni-adjusted p |
|---|---:|---:|---:|---:|
| Feedback to maintenance | +1.00 | 2 / 46,656 | 0.00004286694 | 0.00012860082 |
| Access after timely feedback | +0.25 | 2 / 4,096 | 0.00048828125 | 0.00146484375 |
| Feedback difference in paired access gain | +0.25 | 2 / 46,656 | 0.00004286694 | 0.00012860082 |

All three effects are positive and each p is below the registered 0.05/3 threshold. The reported exact counts, effects and probabilities are correct. Bonferroni protects these declared individual tests without assuming their independence. Here the first-arrow outcome and paired gain are perfectly associated, so three passing tests must not be portrayed as three independent replications. The p-values must not be multiplied or interpreted as the probability that the broad theory is false.

The exact probabilities concern sharp finite-assignment nulls. The A test on paired gains tests the sharp hypothesis that A does not change those lineage-level gains; it is not automatically an exact test of every weak null asserting zero average interaction amid heterogeneous effects. The B seat-swap test conditions on timely assignment and tests no access effect on either seat. Their causal interpretation requires the declared context boundary and assignment mechanism. They do not identify natural indirect effects, generalization to new model families or human institutions, or a universal success rate. Perfect empirical separation does not eliminate those limitations.

## Comparator and report assessment

An independently implemented finite-hypothesis elimination calculation found exactly one rule compatible with the full verified report in every fixture. That conventional learner predicts all sixteen successor answers correctly in every lineage. The default legacy rule gives 12/16 on every challenge set and 16/16 on controls. This confirms the report's conventional-comparator result. It is a rule-inference comparator supplied the verified report, not a full randomized comparator for autonomous maintenance decisions under matched compute or cost. The observed behavior needs no claim of a new inference capability.

The final report's live-experiment description is consistent with the audited data and now includes the necessary novelty, opportunity-cost and execution-provenance qualifications. It may call this decisive evidence against the specifically restricted no-feedback maintenance account in the studied task, conditional on the declared execution boundary. It should not call it decisive validation of the broader programme, repeated institutional reproduction, superiority over conventional learning, independent human review, or security-isolated execution. Its current qualifications avoid those overclaims.

This audit addresses the live handoff experiment only. It does not independently audit the separate transport service experiment or its exact algebraic certificates.
