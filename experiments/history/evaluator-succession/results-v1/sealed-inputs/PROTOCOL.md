# Evaluator succession experiment protocol

Specified locally on 4 October 2026 before any benchmark outcome run. This is a prospective local protocol, not an externally registered study. The final code, configuration, and this protocol will be hashed before execution. Unit checks may precede that seal; aggregate treatment outcomes may not. No parameter search or outcome-dependent stopping is planned.

## Question and scope

Does allocating future evaluation authority by past performance change independent usefulness, compared with equally informed evaluators appointed independently of performance? Do protected correction procedures help while permitting useful rule revision?

This is a synthetic experiment with finite-choice, utility-driven strategic agents. It does not use trained language models, establish human behavior, or validate the separate continuous authority model. Both harmful and beneficial rule changes are available. The original 20-seed rubric pilot and its failed P1 remain separate and untouched; this experiment is not its previously proposed design 2.

## Environment and behavior

There are eight agents and 160 epochs of five production rounds, with 128 independent worlds per context. The last 40 epochs form the evaluation window. Four agents specialize in each of two useful production dimensions. Baseline skills are (1, 0.6) or (0.6, 1), multiplied by independent bounded jitter; identities are shuffled. Evaluators have identical information and computational abilities regardless of production skills.

Agents allocate one unit of effort to two useful outputs and presentation. The 15 actions form a simplex grid with increments of 0.25. Useful outputs equal skill times the square root of effort; presentation equals its effort. Public score is the dot product of the three outputs and rubric weights. Contract allocation is 10% equally distributed plus 90% softmax of score with inverse temperature 4. The guaranteed allocation floor prevents exclusion by construction; this experiment cannot establish persistence without that protection.

Independent usefulness per agent is alpha times output A plus (1-alpha) times output B. Presentation contributes no usefulness. System usefulness W is contract-share-weighted usefulness. Private utility is own contract share plus 0.25 W, minus a real private cost of 0.002 for an adopted amendment. An adopted amendment also consumes 0.002 units of system output per epoch; this is an explicit administrative-cost assumption. Protected review consumes an additional 0.001 per epoch. Gross and net usefulness are both reported.

At each production round, agents evaluate all actions against rivals' previous submissions and choose simultaneously via a logit response with inverse temperature 80. Governors compare possible rules using current frozen submissions and choose via a logit response with inverse temperature 200. These are myopic responses to stipulated utilities, not reinforcement learning, equilibrium computation, or evidence of discovering an unprogrammed objective. No capture bonus or hard-coded capture action appears in utility.

At the end of each nonterminal epoch, completed contract shares update an exponential moving average with weight 0.25. Appointment rights and contract allocation are separate functions. In the endogenous arm, the next governor is drawn with probabilities proportional to the square of that moving average. The governor selects no change or a feasible transfer of 0.05 rubric weight between two features. The resulting rubric applies next epoch. All weights remain nonnegative and sum to one. Initial weights are (0.675, 0.225, 0.10). There is no governance after the final production epoch, so an amendment or correction is counted only when its ensuing production epoch occurs.

## Contexts and interventions

The stable context has alpha=0.75 throughout. The shift context changes alpha from 0.75 to 0.25 halfway through. This represents a change in demand under the same predeclared purpose of useful production. It is not an authorized change in society's ultimate values.

Six treatment packages use the same production skills and keyed random draws within each world:

1. **Fixed:** the rubric never changes.
2. **Endogenous:** past success allocates governance rights as above.
3. **Independent:** draw the governor uniformly and independently at every opportunity, using the same appointment uniforms as the endogenous arm. Amendment opportunities, tenure, competence, information, and costs match. This is the primary causal contrast for performance-dependent appointment.
4. **Rotating:** each independently shuffled block of eight appointments gives every agent one turn. This adds a balancing constraint and changes appointment persistence; it is a secondary treatment package.
5. **Replay:** replay exact rubric paths from separately seeded endogenous donor worlds in the same context. Charge donor administrative amendment costs. Donors do not use the current world's skills or behavior. This also removes responsive adaptation, so it is a secondary comparison package, not an isolated test of capture.
6. **Protected:** endogenous appointments and ordinary proposals, with independent review. A proposal lowering usefulness on frozen submissions is vetoed without resampling. A valid externally supplied correction is implemented directly. Review has its stated cost. Protection and oracle access are maintained externally by assumption; this arm cannot establish self-sustaining independence.

Every 20 epochs except the terminal epoch, an independent source supplies the rubric (alpha, 1-alpha, 0), with an exact frozen-submission calculation. It qualifies as adverse evidence only when it improves W by more than 0.002. Endogenous, independent, and rotating governors may choose it alongside ordinary amendments. Protected governance implements a qualifying correction. The deadline is the start of the next epoch. Successful correction means the implemented rule recovers at least the reference proposal's frozen usefulness; another equally effective rule counts. Fixed and replay lack comparable amendment rights and are excluded from correction-response comparisons. The evidence is exact in this artificial environment and is not a realistic assumption about measuring human welfare.

## Endpoints and prospective predictions

The independent experimental unit is a world, not an agent, action, or epoch. All directional tests use seed-paired world summaries. Four confirmatory predictions are specified:

- **H1:** In the stable context, endogenous appointment lowers evaluation-window gross usefulness relative to independent appointment.
- **H2:** In the stable context, endogenous appointment increases the evaluation-window number of accepted amendments that raise the governor's frozen contract share and lower frozen usefulness, relative to independent appointment.
- **H3:** In the shifted context, independent appointment improves evaluation-window gross usefulness relative to fixed rules.
- **H4:** In the stable context, protected governance improves evaluation-window gross usefulness relative to endogenous governance.

Use a two-sided one-sample t-test on each paired difference and Holm adjustment across these four predictions. Label a prediction supported only if its direction matches and its adjusted p-value is below 0.05; label an adjusted significant reversal contradicted; otherwise label it inconclusive. Report mean paired differences with world-level bootstrap 95% intervals (10,000 resamples) and all p-values. Intervals are marginal descriptive intervals, not simultaneous intervals. Distributional limitations remain; this is a mechanism pilot.

Secondary results include net usefulness, endogenous versus replay/fixed, all shifted-context contrasts, presentation weights, allocation and authority concentration, beneficial amendments, correction opportunities and successes, and persistence of advantage. A purpose-impairing amendment is only an immediate mechanism measure: delta own share>1e-9 and delta W<−1e-9. It is not itself a complete capture diagnosis. For such events, report whether the governor's average contract share over the next five epochs exceeds its pre-amendment share by more than 1e-4. This descriptive persistence measure has no causal mediation interpretation and does not track entry or coalitions.

No universal ordering of the arms is assumed. Fixed rules may perform poorly when demand shifts. Self-benefit can accompany beneficial reform. Any absent effect, reversal, failed prediction, or costly safeguard will be reported. Results do not identify attractors from a finite trajectory or establish the prevalence of capture in existing institutions.

## Reproducibility and execution rules

Configuration is fixed in config.json. World seeds are 41000–41127; independent donors add 1,000,000. Use stable NumPy SeedSequence streams keyed separately to skills, production responses, appointments, amendment choices, and rotating schedules. Common exogenous draws are precomputed, so treatment-specific branches cannot shift later draws. The analysis uses its own fixed stream. Save per-world summaries, epoch traces, all governance receipts, donor paths, raw paired contrasts, the sealed input hashes, software versions, and timestamps. Run exactly the specified worlds; retain outcome failures and disclose implementation repairs. No human experiment is authorized or conducted by this protocol.

Before the first outcome run, independent code review identified that balanced rotation changes appointment variance as well as its connection to performance. The independent uniform arm was therefore added as the primary comparator, with rotation retained as secondary. Review also led to excluding terminal governance, richer frozen-submission receipts, and archived copies of sealed inputs. These changes preceded all benchmark outcomes; no parameters were selected using results.
