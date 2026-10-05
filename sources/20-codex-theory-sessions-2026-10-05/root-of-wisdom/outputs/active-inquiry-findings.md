# Active inquiry: what to investigate, when to act, and what remains untested

Continuation of Ren's root of wisdom inquiry, 5 October 2026, Asia/Bangkok. This report follows the [initial synthesis](root-of-wisdom-synthesis.md) and [first reasoning pilot](reasoning-pilot-findings.md). The [evidence bundle](active-inquiry-data.json) preserves the complete finite models, instructions, participant responses, mechanical feedback, scoring, and audit records.

This report preserves that comparison. The subsequent [answer drawing on other sessions](noticing-missing-possibilities.md) identifies an already implemented route to bounded candidate discovery and tests a further limit in the candidate language.

The active-inquiry comparison is complete. Ordinary careful reasoning, explicit sequential decision analysis, and the six-question discipline each made **12 of 12 optimal initial choices and 22 of 22 optimal choices across the states actually visited**. None made an unnecessary paid inquiry under the prespecified definition. This is another ceiling result: these cases show no comparative advantage for the proposed discipline. They do not establish general equivalence or prove that the discipline has no use.

The substantive refinement concerns what finite understanding must accomplish. Understanding can be sufficient for a present decision while leaving the outcome uncertain. It can also require a sequence of inquiries whose first step has no immediate decision benefit. Whether inquiry is worthwhile depends on its possible continuation and whether an effective response will still be available. These are established decision principles illustrated here, not newly discovered mathematics or a demonstrated definition of wisdom.

## A stronger test than selecting an answer

The first pilot supplied complete answer options. This one required participants to select an inquiry, pay its fee, receive only the selected result, and then choose their next inquiry or terminal action. Every episode allowed at most two queries and three decision rounds. Query and action fees counted toward both the loss objective and the cash budget; residual losses counted toward the objective only. Query and action durations both counted toward the deadline. Finishing exactly at the deadline was permitted.

There were three conditions:

| Condition | Additional instruction |
| --- | --- |
| Ordinary reasoning | Choose carefully to minimize expected total loss under the stated constraints. |
| Explicit decision procedure | Condition probabilities on evidence; enumerate feasible actions and queries; compare immediate action with query fees plus optimal possible continuations. |
| Six-question discipline | Examine warrant, evidence and alternatives, possible correction, purposes and affected people, executable response, and justified stopping. |

The explicit procedure is a stronger comparator than the first pilot's generic reflection instruction. It directly describes the established technique suitable for these fully specified problems.

Two fresh participant contexts per condition received the same six episodes. The second presentation order reversed the first, with common orders across conditions. The six episodes formed three matched pairs. Their worlds, priors, query response functions, actions, losses, and constraints were fully disclosed; only the realized world was hidden. Thus this tests **active selection of evidence within a supplied model**, not discovery of previously unimagined variables, causes, or experiments.

The following table gives the exact initial optimum, including query and action fees. Values are expected loss units under the public prior; lower is better.

| Episode | Controlled feature | Optimal initial command or commands | Optimal value |
| --- | --- | --- | ---: |
| A01 | Two complementary queries, each costing 1 | Query either share | 3 |
| A02 | Same model, each share now costs 4 | Immediately choose either state-directed action | 7 |
| A03 | Diagnosis and repair fit a deadline of 6 | Open the panel, enabling diagnosis | 3 |
| A04 | Same model, deadline reduced to 5 | Take fallback immediately | 8 |
| A05 | The same action is best in both possible states | Choose option A immediately | 5 |
| A06 | One loss entry changes, making different actions best in the two states | Inspect the state | 2 |

The cash limits were enforced, but do not bind in the six actual cases. This comparison therefore tests sensitivity to query fees and a binding deadline, not demonstrated sensitivity to a binding cash cap. Separate software fixtures checked cash-boundary handling.

## How scoring avoided rewarding luck

At a public information state, a feasible terminal action was valued by its action fee plus posterior expected residual loss. A query was valued by its fee plus the probability-weighted optimal continuation after each possible answer. The evaluator considered every answer with positive probability under the public model, not just the answer produced in the run. This finite recursive decision method belongs to established dynamic programming; Bellman's early account explicitly treats sequences of operations, costs, and the best first operation. We examined pages 716–717 of [Bellman's 1952 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063639/).

Writing the current public state as s, the calculation is:

    Q(s, action) = action fee + expected residual loss given s
    Q(s, query)  = query fee + sum over answers y of P(y | s, query) V(next(s, query, y))
    V(s)         = minimum Q(s, command) over feasible commands

The next state includes the answer, remaining resources, time, completed prerequisites, and remaining queries. At the query limit, only terminal actions remain. Backward evaluation therefore terminates. Exact fractions retain all true ties. The private world is used only to generate requested answers and realized losses; it is excluded from the expected-choice calculation.

The primary outcome was membership in the optimal initial-command set. Later choices were checked against the optimum at their actual information state. A strictly unnecessary continuation meant a selected query whose value was worse than the best immediately available terminal action. An answer that happened to leave the preferred action unchanged did not make its query an error.

We also recorded each visited choice's excess over its state's optimum. The sum is a diagnostic along the observed trajectory. It does not measure the participant's complete policy across unobserved branches: those branches were not elicited. Realized fees and losses are reported separately and are not substituted for expected decision quality.

Treatment instructions were frozen before case inspection. Cases, independent private draws, orders, interface conventions, oracle, and scorer were fixed and hashed before participant dispatch. These are local prospective records, not an external preregistration. Independent checks agreed on every feasible choice value and optimal tie across all 74 reachable ordered public histories. Pre-run review also resolved a malformed-JSON boundary and clarified invalid-command handling. The original protocol and its explicit pre-run amendments are retained.

## Complete results

| Condition | Optimal initial choices | Correct matched pairs | Optimal visited choices | Queries strictly worse than immediate action | Invalid commands |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ordinary reasoning | 12/12 | 6/6 | 22/22 | 0 | 0 |
| Explicit decision procedure | 12/12 | 6/6 | 22/22 | 0 | 0 |
| Six-question discipline | 12/12 | 6/6 | 22/22 | 0 | 0 |

Each of the six individual contexts scored 6/6 initial choices, 3/3 matched pairs, and 11/11 visited choices. Every context followed the same path in each episode:

| Episode | Observed sequence in every context | Query fees | Action fee | Realized residual loss |
| --- | --- | ---: | ---: | ---: |
| A01 | share_a → share_b → choose_0 | 2 | 1 | 0 |
| A02 | choose_0 | 0 | 1 | 0 |
| A03 | open_panel → diagnose → repair_0 | 2 | 1 | 0 |
| A04 | fallback | 0 | 0 | 8 |
| A05 | option_a | 0 | 1 | 8 |
| A06 | inspect → option_b | 1 | 1 | 0 |

Each condition made ten queries across its two contexts, paid ten query-fee units and ten action-fee units, and incurred total realized loss 52. Every initial excess-loss sum, visited-state excess-loss sum, and conditional terminal excess-loss sum was zero. No missing answers, malformed responses, duplicate or extra IDs, invalid requests, or violations of the 35-word reason cap occurred. All planned runs were retained; no additional runs were added after the ceiling appeared.

Post-run independent review replayed all 18 response-and-feedback rounds and all six final states, recounted every choice, and confirmed that all 25 frozen input hashes and the three earlier treatment hashes remained unchanged. The 66 reasons ranged from 14 to 29 whitespace-delimited words; review found no material arithmetic or decision contradiction. This is internal research review, not external scientific replication.

The sum of initial optimal expected losses was 28 per context, while realized loss was 26. This difference reflects the particular hidden worlds. For example, the uninformed choice in A02 happened to avoid residual loss, while the rationally uninformed action in A05 incurred residual loss 8. Neither observation changes the quality of the decision at the time it was made.

The hidden worlds were six independent seeded draws from the stated priors, then reused across conditions and repetitions. A superseded pre-run draft shared draws within pairs; it was replaced before dispatch and is preserved in the design history. The final draws coincidentally agree within each pair, but the sampling rule does not impose such agreement. Repetition across conditions helps compare the same realized branches; it does not provide six new independent world samples for each episode.

## What the three pairs clarify

**A question can be useful because of another question.** In A01 either share alone leaves the decision-relevant alternatives equally likely. Acting without inquiry has expected loss 7. Buying one share and then immediately acting costs 8. A one-step calculation would therefore reject either share. But buying both identifies the right action, for total loss 1 + 1 + 1 = 3. In A02 the identical information costs 4 + 4 + 1 = 9, making immediate action at expected loss 7 preferable. The value belongs to an attainable sequence, with its costs, rather than to information considered in isolation.

**Information is useful only through responses still available.** Opening, diagnosing, and repairing requires 1 + 2 + 3 = 6 time units. At deadline 6, this yields loss 3 rather than fallback loss 8. At deadline 5, the diagnosis can arrive, but the repair cannot finish. Opening and then falling back costs 9; completing diagnosis and then falling back costs 10. Immediate fallback costs 8. Learning the fault is insufficient to repair it within the available opportunity.

**Knowing what to do need not settle what will happen.** In A05 option A is best in both states, although its residual loss is either 0 or 8. Expected total loss is 5. Inspection resolves the state but leaves the justified action unchanged, raising expected total loss to 6. In A06 a single changed consequence makes different actions best in the two states; inspection then reduces expected total loss from 4 to 2.

The realized A06 answer is especially instructive. Without inspection, option B is the best immediate action. The returned state also favors option B, so the actual action is unchanged. Inspection was nevertheless worthwhile before its answer: the other possible state would have warranted option A. Judging inquiry only by whether it changed the observed action would misclassify a good decision.

## What this changes in the root proposal

We can sharpen the provisional formulation: a finite discipline of understanding must distinguish uncertainty that matters for a current judgment, inquiry sequences capable of resolving it, and the point at which enough has been learned to act. “Enough” is relative to a question, a considered model, feasible responses, and defensible purposes. It is not a certificate of completeness about the world.

These examples support that distinction. They do not show that the six-question prompt contributes a special capacity beyond ordinary reasoning or the explicit decision procedure. Both completed pilots reached the ceiling on their selected tasks. Continuing to add similarly transparent cases until a difference appears would not provide a sound basis for a stronger claim.

Nor does minimizing a stipulated scalar loss establish ethical wisdom. These models hand participants the purposes, burdens, and permissible actions. They do not test whether those terms deserve acceptance, whose interests were omitted, or whether an apparent improvement violates an obligation. The fourth question of the proposed discipline—about consequences and defensible purposes—therefore receives no substantive ethical validation here.

The next consequential question is **how to allocate limited inquiry between improving a decision within the current model and checking whether the model omits something that would change the decision**. A controlled next study could disclose the possibility of omissions and offer limited opportunities to inspect a premise. Both warranted model revision and warranted retention would need examples. The fuller reference models, omission frequencies, costs, and outcomes would have to be fixed before collection. Such a study would test bounded model revision; an experimenter-supplied larger menu must not be relabeled unrestricted discovery.

This question returns directly to Ren's original intuition. A finite account may be sufficient for a situated judgment while remaining open to consequential distinctions it does not yet contain. The unresolved task is explaining how those distinctions become thinkable and assessable, without turning revisability into permanent indecision. The present experiment clarifies where that task begins; it does not solve it.

## Limits of the evidence

There are six context-level batches, three closely related case pairs, 36 episodes, and 66 recorded choices. The episodes and choices are not independent replications of a general reasoning ability. All participants used the inherited model configuration; sampling seeds and hidden computation were uncontrolled. Prompt lengths differ because the treatments differ. Matching permitted tools and visible word limits does not establish equal effort or efficiency.

Participants were instructed to load only their assigned prompt and then use no tools, external information, or delegation. The evidence bundle preserves their final response texts and all mechanical feedback, not a complete independent tool-trace audit. Fresh contexts and public-only prompts limit direct contamination from the research history, but the cases were intentionally authored around the framework's concerns and are not an independent validation set. The evaluator knew the condition; fixed mechanical scoring limits, but does not erase, this design limitation.

The evidence therefore supports a precise, limited result: all three instruction conditions handled these fully specified active-inquiry problems correctly. It does not establish a unique root of wisdom, general reasoning superiority, conceptual discovery, ethical authority, consciousness, or alignment.
