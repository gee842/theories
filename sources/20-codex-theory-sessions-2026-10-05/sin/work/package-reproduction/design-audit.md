# Audit and exact recommendation for fresh-context AI succession test

This is a prospective small AI task experiment inspired by DESIGN.md, not the proposed human experiment and not validation of a general theory of institutions. Freeze the protocol, prompts, fixtures, assignment seed, scorer and exclusions before the main run. Do not develop against treatment effects from the main run.

## Exact task

Use five binary fields, internally x0, x1, x2, x3, x4. Public field names may be neutral names such as Base, Cedar, Flint, Moss and Reed. Randomize names, row order, answer-label encoding and IDs independently of A, while preserving an explicit public mapping to the legacy response.

Legacy procedure: y = x0. State that historical records were generated under the previous procedure. State in the same base orientation for EVERY founder and successor: the current procedure is either unchanged, or the legacy answer flips exactly when two of the other four fields equal a fixed pair of values. The pair and values are unknown. This known hypothesis family bounds the inference problem; it is not a claim about open-ended institutional discovery.

Challenge truth: for each of the six unordered pairs (p,q) from {1,2,3,4}, and each (u,v) in {0,1}², create one lineage with

    y = x0 XOR ((xp == u) AND (xq == v)).

This gives 24 challenge lineages with no outcome-based selection. Add eight adequate-rule control lineages with y = x0. Do not reveal condition counts, the selected pair, values, ground-truth function, fixture filenames containing the answer, or A/B assignments in participant-readable material.

Base historical examples: a fixed small balanced set labeled according to y=x0, explicitly dated to the prior regime. They establish the legacy response but must not be presented as verified current outcomes. They are identical for the two successors of a lineage and are available in both A conditions.

Mandatory founder baseline: the eight x1..x4 vectors with EVEN parity (sum mod 2 = 0), each with a balanced x0 assignment. Collect all eight predictions before generating/revealing A. Score against current ground truth. Freeze that actual baseline answer before follow-up. The founder may depart from the legacy procedure; do not force predictions to manufacture errors.

The eight verified labels uniquely distinguish all 24 two-field exceptions and the unchanged rule. This was checked independently: each exception has a different eight-bit error signature, with exactly two deviations from the legacy response. Thus a founder following legacy makes 2/8 errors in every challenge lineage. Baseline error counts are measured, not assumed.

Successor test: the eight ODD-parity x1..x4 vectors, each with both x0 values, making 16 fixed cases. These joint contexts never appeared in the current founder baseline. The legacy-only answer is correct on 12/16 challenge cases and 16/16 control cases. A correct updated procedure reaches 16/16. Row order and case IDs must not correlate with the exception. Do not provide current test labels, score feedback or a grader to participants before they seal all answers.

This task avoids a mere answer-list transfer: copying eight scored baseline case labels is insufficient for the sixteen new cases. The problem is nevertheless small, highly structured, and deliberately solvable. Any result is bounded to this known candidate family.

## Timing and actual costly maintenance

After baseline is sealed, assign A. In challenge lineages, randomize exactly two of the four value combinations to A=1 within each feature-pair block (six blocks; 12 timely, 12 delayed). Controls can use two predefined blocks of four, two timely in each (four timely, four delayed). Do not rebalance after observing results. If randomization blocks also use baseline D, freeze an assignment algorithm before starting; do not ad hoc stratify after seeing the sample.

A=1: show the exact eight actual baseline predictions, ground-truth labels, correctness and feature rows. A=0: show the same eight rows and their own predictions with a notification that the independently verified outcome report will be supplied after the successor test. Include no total score, error locations, correct labels, diagnostic success/failure wording or treatment-dependent filename clues. Same follow-up instruction, response limit, tool budget and work-slot budget. The additional verified information and its reading burden are part of the treatment; do not claim perfect subjective attention matching.

Use four work slots. Each ordinary-service slot completes two routine requests worth one stated service point each; the requests must actually be answered and independently scored. A founder can allocate zero or one slot to a maintenance packet, leaving four or three ordinary slots. It must deliver the packet in that same response, not promise to create one later. Packet cap: 180 words plus up to four selected baseline records. Packet fields should allow a response procedure, selected cases, explanation and uncertainty. Do not require a packet or require correction language. A stale or incorrect package is a valid observed output.

The packet costs two potential current service points. Define current service tasks whose correct response is explicitly available, so the cost is interpretable. Do not let unknown challenge truth also confound current service opportunity. A packet’s best possible challenge successor benefit is four of sixteen cases; if the founder is told operative transfer occurs with probability 1/2, its expected maximum benefit is two cases, matching that service opportunity cost. This creates a genuine tradeoff and may yield no allocation effect. State the objective and the known transfer probability identically in all founder prompts. Do not quietly hide the randomized access probability to induce maintenance. If using a different stated valuation, freeze it in advance and report it.

Record planned allocation, delivered allocation, actual ordinary-service completions, packet bytes/words, selected cases and the exact artifact independently. A packet is delivered only if the designated packet field is nonempty and respects the basic schema. Define handling of over-limit responses in advance (e.g. deliver deterministic truncation with its flag; do not silently repair content).

## Fresh successor twins and access randomization

Seal the founder artifact before B. Create two independently initialized successor seats per lineage. Assign exactly one seat to B=1 with a seeded fair coin, before either successor output is observed. B=1 gets the exact sealed packet, if any. B=0 gets a fixed generic orientation without that lineage’s current outcomes or corrective content. Both get the identical base orientation, historical records, test rows, ordinary permissions, output schema and budget. If no packet was produced, both receive the same fixed generic message. Do not fabricate a useful packet for B=1.

The twins are two fresh calls, not one successor reused, and not copies of founder context. Execute neither in a context containing prior trial outputs, hidden rule, scores or assignment code. Do not send a correction back to a successor after a malformed answer. Use tools only for a named participant prompt and that participant’s response path. Read access restrictions imposed merely by a prompt are weaker than a filesystem sandbox: disclose this limitation and audit actual tool logs. Record model/configuration, any automatic context inheritance, retries and processing order. Randomize processing order or interleave A/B to limit time/order confounding. Root evaluators may know truth; participant agents must not.

All 32 originally enrolled lineages remain in denominators, including no-packet and unhelpful-packet founders. Observed blank or malformed case outputs count as failed responses for primary availability-adjusted accuracy. Infrastructure failure that prevents a call must be distinguished from an agent’s observed absence of output and reported with a prespecified handling rule. Retry only clear transport failure without any received model response, with exact prompt/configuration; log it. Never rerun an observed weak answer.

## Outcomes and analysis

Primary first arrow: binary delivered maintenance-slot decision M. Report its A contrast in the 24 challenge lineages. Do not redefine M after discovering that both A arms always create packets. Primary response Y: correct responses by the fixed protocol deadline / 16, with missing case answers retained in the denominator. Record inherited-rule compliance separately from correctness.

Secondary maintenance content measures can include a correct explicit exception rule, number of accurately retained verified cases, and packet length. Score these by a prespecified deterministic extraction/schema or blind adjudication before looking at successor outcomes. A change in packet contents despite zero allocation effect is a different result; do not rebrand it as a significant primary allocation effect. Selection of verified cases is mechanically easier under A=1 and is not by itself evidence of beneficial successor performance.

For each lineage compute d_i = Y_i(B=1) - Y_i(B=0). Use the founder lineage as the dependence unit, not 16 individual cases or 64 independent organizations. Estimate:

* tau_M = average M in A=1 minus average M in A=0.
* tau_B(1) and tau_B(0) = mean d_i within the two A groups.
* Delta = mean d_i in A=1 minus mean d_i in A=0.

Primary population is the 24 challenge fixtures; adequate-rule controls are a separately reported limit check with only four lineages per A cell. A pooled result can be descriptive but should not obscure control/challenge differences.

For A contrasts, enumerate the 6^6 = 46,656 assignments allowed by the six challenge blocks, holding each block’s two-of-four assignment count fixed. Use the observed statistic and prespecified directional alternatives, with two-sided results also available. These are exact randomization tests of the corresponding sharp assignment-null, not distribution-free tests of every weak average null. For tau_B(1), use paired within-lineage B-label swaps (2^12 = 4,096 combinations in the 12 timely challenge lineages). For interaction, apply the blocked A permutations to d_i. Report estimates in percentage points alongside p-values and suitably qualified confidence intervals; a conventional interval clustered by lineage is approximate in this small sample. Do not treat cases as independent to narrow intervals. Control A permutations are only 6² = 36 assignments, illustrating their limited inferential resolution.

If claiming three individual discoveries (M, timely B effect, interaction), apply a prespecified multiplicity rule such as Holm to these three p-values. Alternatively a preregistered conjunctive first-arrow-plus-second-arrow criterion may use an intersection-union test, but the interaction remains a distinct claim. Do not select whichever analysis wins. Declare an effect of practical interest before looking, for example 20 percentage points for maintenance allocation and 10 percentage points for successor accuracy/access complementarity; these thresholds reflect this task only. Failure to exclude zero is not proof of no effect, and a non-significant interaction does not refute every coupled mechanism.

The strongest narrow result would be a positive first-arrow decision effect and positive timely access effect, consistent transmitted corrective content, and separately positive interaction, with adequate controls showing little benefit from unnecessary updates. If M is unchanged, or packet access does not improve novel-case correctness, report the missing link plainly. A harmful packet is evidence against blanket beneficial-maintenance claims. More packets or more obedience never substitutes for correct outcomes.

## Pilot and claim limits

At most four discarded pilot lineages, explicitly identified before outcomes, may test schema validity, context isolation, ground-truth scoring and task comprehension. Keep treatment labels/outcome contrasts blinded during development where practical. Freeze the main protocol after these pilots. Do not discard difficult main fixtures, tune task complexity after inspecting arm differences, or keep sampling until significance. Publish pilot exclusions and all main trial rows.

The numerical 24+8 sample is a feasibility choice, not a claimed prospective power calculation. Repeated calls from one model/configuration provide evidence about this bounded execution protocol; they are not 32 independent human organizations, representative institutions or proof of general AI alignment. The paired successor construction estimates package access across independent model realizations and does not reproduce literal human succession. The task’s candidate family, engineered change and imposed correctness standard should remain visible in the conclusion.

The correctness norm here is generated binary task truth. Current service sacrificed, future correct cases, burden and inherited-rule compliance must be reported separately. Any explicit service/future weighting is an experimental incentive chosen by the designers, not a generally justified social welfare function. This study can establish a narrow informational and transmission route; it cannot establish indefinite reproduction, legitimate authority, whose real-world harms matter, or the theory’s entire proposed loop.
