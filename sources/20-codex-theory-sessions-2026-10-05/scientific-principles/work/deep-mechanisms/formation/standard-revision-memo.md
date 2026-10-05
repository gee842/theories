# Learning to revise an admission standard

Continuation mechanism study, 5 October 2026. This is an executed finite model with exact controls, reproducible synthetic runs, fresh transfer executions, and separate exact evaluator calculations. It extends the earlier concept-construction example. It does not establish a complete theory of science or unrestricted self-revision.

## What is new

Previously, the researcher compared two supplied search policies. Now a learner syntactically edits its own admission rule, pays to try the edit, evaluates observed outcomes, checks it on separate fresh tasks, installs the edit, and actually uses the changed rule on subsequent tasks. It receives neither a hidden world label nor an oracle declaration that the edit is better.

The editable standard is specific: **must a single-variable improvement be found before trying a two-variable model?** It is an admission/search standard. The prediction goal, loss weights, measurement interface, hypothesis grammar, final local validation criterion, and meta-level assessment procedure remain supplied and fixed. Removing one eligible precondition is the entire edit grammar. Choosing this editable clause and supplying a protected probe route are design commitments, not discoveries made by the learner.

The stronger result is not simply that a rule can change. The same learner changes it in a favorable task distribution, rejects it under several controls, can remain locked out despite abundant funds, and is harmed by keeping its learned rule after a task-distribution shift.

## Mechanism and information boundary

Each task has three binary fields with arbitrary field identity. Interaction tasks choose one of the three field pairs and one of two output complements uniformly: six equally weighted deterministic rules. Single-field tasks similarly randomize the useful field and output complement. The independent-null task produces fresh fair labels. Noisy interaction tasks flip each label independently with probability one quarter. The mixed profile chooses a deterministic interaction task or an independent-null task with probability one half.

A base procedure obtains one training observation at each of the eight binary contexts. Generic majority-table fitting constructs candidate models from every single field and permitted pair. The search score is empirical classification error plus `1/32` for each extra table cell. Baseline constant fitting is free. Ties are fixed in advance.

The incumbent first fits all three singleton models. It permits pair construction only if a singleton improves the penalized training score; if permitted, it examines the two pairs containing the selected field. The generated edit deletes that prefix-gain requirement, making all three pairs available. The final training-improvement requirement and fresh local validation are preserved.

For either procedure, one selected candidate must predict at least seven of eight fresh validation outcomes correctly before being used. Otherwise the fitted constant remains installed. The procedure then makes 64 predictions on a balanced sequence of fresh cases. Their outcomes are revealed after prediction and constitute observed feedback. These 64 routine outcome revelations carry no additional acquisition charge; that is an explicit environment assumption. Field collection during those predictions is charged.

The meta-learner runs both procedures on the same sampled task type, but each receives its own independent training, local validation, and routine outcome streams. Both streams' expenses are paid. It first screens the edit on 32 paired tasks, using observed expense plus prediction errors. If mean improvement is positive, it checks the frozen edit on 256 entirely fresh paired tasks. The rule is installed only if a conservative lower confidence bound for expected improvement is positive.

Only observed reports enter edit screening and checking. The environment's truth table and noise law remain in its sampling functions. A separate exact evaluator uses those quantities after the run; its output is never fed to the learner.

## Declared costs and supplied commitments

| Item | Value or rule |
|---|---|
| Acquired training/local-validation label, including its context record | 1 unit |
| Fitting a singleton or pair candidate | 1/4 unit |
| Retained field per routine prediction | 1/50 unit |
| Wrong routine prediction | 1 loss unit |
| Routine outcome feedback after prediction | No added acquisition charge |
| Baseline fitting, rule editing, and meta-level arithmetic | No separately priced charge in this toy model |
| Primary task horizon | 64 predictions per procedure episode |
| Meta-study | 32 discovery pairs, then at most 256 fresh checking pairs |
| One-check significance level | .05 |
| Available funds in the principal run | 12,000 units |

These prices and the conversion of prediction errors and expenditures into one loss are supplied. They do not follow from causal embeddedness. Every expense that this model prices is included. Real engineering, institution-building, opportunity, and computation costs absent from the price list have not been estimated.

For default prices, any procedure episode costs between 8.75 and 20.06 in acquisition, fitting, and field expenses. A pair therefore costs at most 40.12. Reserving all possible payments before the study requires `2(32+256)20.06 = 11,554.56`. This is a conservative sufficient pre-funding policy. It is not a theorem that every feasible financing arrangement needs that initial balance; sequential credit or replenishment could change feasibility.

## Conditional reliability of the rule change

Let `D_i = observed loss of incumbent - observed loss of edited procedure` on fresh checking pair `i`. This is a within-task comparison; outcomes may be dependent across the two arms through their shared task type. The argument requires the *pairs* to be independent and identically distributed under an unchanged task law. Independence between the arms is not needed for the range bound, although the implementation supplies separate outcome streams.

At default prices, total loss lies in `[8.75, 84.06]`: 0–64 prediction errors plus the expense range. Thus `D_i` lies in `[-75.31,75.31]`. For `n` fresh pairs the lower bound is

`lower = mean(D) - 150.62 sqrt(log(1/alpha)/(2n))`.

The bounded-independent-sum inequality gives probability at most `alpha` that this bound exceeds the true mean. In particular, accepting only when it is positive controls the chance of installing this nonpositive-mean-gain edit at `.05` for one fixed check. Screening on different earlier tasks preserves that conditional guarantee. This uses the established [Hoeffding bounded-sum result](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830); we verified the primary publication record/abstract and apply the standard inequality. No new concentration theorem is claimed.

The guarantee does not survive arbitrary task drift, unaccounted dependence, incorrect bounds, repeated checking until success, or hidden changes to loss. It is not a statement that every future episode improves, and not a lifetime false-adoption guarantee across repeated meta-studies.

## Executed results

The first nine rows below use seed `20261005`. Counts, costs, and outcomes are reproducible synthetic results. Deterministic interaction/simple/constant results also have exact structural checks; stochastic rows are particular finite runs rather than exact frequencies of outcomes over all possible studies.

| Task profile or intervention | Result | Priced study expense | Fresh checking mean gain | Lower confidence bound |
|---|---|---:|---:|---:|
| Randomized deterministic interactions; protected probe | Admission rule changed | 8,297.28 | 20.6900 | 9.1688 |
| Same interactions; incumbent rule controls probe admission | Probe blocked; rule unchanged | 8.75 | — | — |
| Same interactions; only 100 funding units | Study cannot meet its chosen reserve policy | 0 | — | — |
| Single-field tasks | Edit rejected during discovery | 1,193.92 | — | — |
| Constant tasks | Edit rejected during discovery | 584.00 | — | — |
| Independent fair labels | Edit rejected during discovery | 837.78 | — | — |
| Interaction labels with .25 independent noise | Passed discovery; failed fresh checking | 8,059.18 | -3.2216 | -14.7428 |
| Half interactions, half independent-null tasks | Passed discovery; failed fresh checking | 8,174.48 | 8.2925 | -3.2287 |
| Interactions, but field price raised from .02 to .30 | Edit rejected during discovery | 2,068.80 | — | — |
| Mixed tasks, fresh follow-up with 1,024 checking pairs | Admission rule changed | 29,730.70 | 8.7633 | 3.0027 |

The 1,024-pair follow-up was designed after seeing the initial mixed-profile result. It uses fresh seed `912867` and does not extend or reuse the failed checking prefix. Its sample size was fixed before the new run. It is an externally designed follow-up, not an autonomous sample-size revision by the learner. Each check has the stated one-study guarantee under its conditions; no combined `.05` lifetime guarantee is claimed for the two studies.

The mixed-profile result illustrates insufficient power, not evidence that the edit is useless. Separate exact evaluation finds positive mean benefit 8.8449609375 per future task. More checking can establish that benefit, but requires more financing. The noisy-profile edit really has negative mean benefit at the declared horizon and costs, despite appearing favorable in its discovery sample.

## Exact lockout and actual standard change

For every one of the six deterministic interaction orientations, each singleton table has prediction error one half on the balanced training grid. No singleton earns its complexity penalty. The incumbent gate consequently constructs no pair candidate. Under the edited rule, the relevant pair table is constructed and fits all eight outcomes. It then passes the independent local validation and predicts the later cases perfectly.

This is an exact lockout for the declared noiseless family and gate. If permission to test a revised admission rule itself requires the same singleton improvement, the meta-probe cannot open. Repeating this gate on other tasks from this same family changes nothing. Funds alone do not alter that predicate. Noise, other task types, altered opening rules, or outside exploration can remove the premise, so this is not a claim about every institution.

With the protected route, observations establish that the edited procedure produces lower priced predictive loss. The learner changes `require_improving_prefix` from `True` to `False`. The final rule is then reconstructed and used in genuinely fresh future executions. This is an operational change in the mechanism selecting which models can be investigated, not merely a flag announcing that revision would be desirable.

The old unconditional description `P(Y=1)=1/2` stays correct. The change enables production of more resolved knowledge. Correcting false aggregate beliefs is not its only role.

## Transfer after change: the learned standard can become wrong for its context

After the interaction study, the learned rule is frozen and actually executed on 512 new task pairs in each specified future profile, using a new seed and future data. The learner receives no advance signal naming the shift. Separately, `exact_transfer.py` enumerates all training label vectors, integrates local validation, and averages all relevant task orientations to compute the true mean for each fixed profile. These exact values are evaluator diagnostics only.

| Future task distribution | Observed gain in 512 fresh executions | Exact expected gain of learned rule |
|---|---:|---:|
| Same randomized deterministic interactions | +20.6900 | +20.6900 |
| Single-field relations | -0.2500 | -0.2500 |
| Constant labels | -0.7500 | -0.7500 |
| Independent fair labels | -2.8927 | -3.000078125 |
| Interactions with .25 independent label noise | -4.3751 | -3.371819006 |

The guarantee concerned the study distribution and cost/horizon regime. It does not justify permanent universal use of the learned standard. This implementation does not yet detect drift or reopen its meta-level rule after the shift. The transfer losses are a deliberately retained failure case, not a repaired-away limitation.

A separately specified follow-up now demonstrates repeated revisions under externally scheduled, newly financed studies; see `repeated-revision-memo.md`. It preserves this frozen-rule transfer failure and does not claim endogenous drift detection.

## Meta-study expense, amortization, and financing are different questions

The primary study pays all 8,297.28 units of priced acquisition/search/field expense. The checked 20.69 per-task gain compares the full edited procedure with the full incumbent procedure; future method-execution costs are already subtracted. Recharging those future costs would double count them.

If one requires future improvements alone to match **every priced study payment**, deliberately ignoring useful services produced during the study, the exact unchanged-law gain requires `8297.28/20.69 = 401.0285` future episodes: 402 whole episodes. Using the 95% lower bound yields about 904.951, hence 905 episodes. This is a conservative total-outlay hurdle under stationarity, not a theorem that the entire study has negative value before that point or that reduced loss creates spendable cash. Converting value gains into inquiry revenue is a further financing rule, absent here.

A second accounting question compares the complete study to an incumbent supplying the same required prediction services. The study delivers 576 blocks of 64 predictions, half through each procedure. In noiseless interaction tasks its total observed loss, already including every priced expense, is 17,513.28. Delivering the same 576 blocks through the incumbent costs 23,472 in the same loss units. The study therefore has **-5,958.72 incremental loss** against that matched service counterfactual. Its additional cash expense relative to the incumbent's 5,040 cash units is 3,257.28; its reduced prediction losses are 9,216. These sum to the same incremental result.

That matched-service calculation assumes those prediction services were needed anyway. If study predictions have no service value, an outside alternative supplies them differently, or inquiry harms are omitted, the counterfactual changes. On stochastic tasks, duplicating one observed incumbent stream is only an estimator of a second stream's loss, and selection can bias reuse of these reports; no confidence claim is attached to that descriptive accounting. The deterministic principal case has identical incumbent losses on every orientation, making its comparison exact.

The learner's adoption criterion validates better future per-episode procedure performance. It does not itself choose the optimal number of studies, determine the value of the service schedule, or optimize the total economic return of conducting meta-research.

## What this supports, and what remains outside it

This is a constructive conditional example of methodological learning: an implemented investigator can revise a rule for admitting representations using consequences observable in its own world. The rule's continuation depends on a financed, informative evaluation route. A more capable route can be blocked by the rule it would challenge. A justified change can later become costly after the task distribution changes.

The most discriminating prediction is a three-way interaction: **task structure × permission for meta-probes × available financing**. For deterministic interactions, admission lockout persists even with adequate money; protected probing works only if the inquiry is feasible; the same structural change loses value in simple/noisy contexts or after a shift. A theory explaining only which individual model best fits a fixed dataset does not by itself specify these institutional/procedural transitions. Existing computational discovery and meta-learning theories may already predict them; no historical novelty is inferred from the example.

The following remain supplied or missing: the editable rule grammar, the external probe trigger and budget, the higher-level loss, the error threshold, the reliability of measured outcomes, the finite representation language, endogenous new instruments, endogenous goals, social authority over standards, resource regeneration, harmful experimentation, and drift-triggered meta-revision. These boundaries are substantial. They locate a workable next layer of a theory of science, rather than converting one successful simulation into the full theory.

## Files and verification

* `revise_standard.py`: learner, environment, rule-change protocol, conservative ledger, and prospective transfer executions.
* `standard-revision-results.json`: every reported main-study record, configurations, event summaries, source hash, and service accounting.
* `standard-transfer-results.json`: actual use of the installed rule on future tasks.
* `exact_transfer.py` and `exact-transfer-results.json`: evaluator-only exact expected losses and total-outlay calculations.
* `audit_rule_revision.py` and its results: independent audit supplied by the adversarial agent.

Exact controls check all six interaction orientations/complements and the 9/256 local-validation tail under independent fair labels. The independent audit checked report replay, concentration arithmetic, expense/reserve arithmetic, observation calls, and hidden-world separation. It found an underfunded-pilot chronology bug: observations were drawn before the funding check. The code now checks and charges the pilot before observing. A follow-up design audit also caught reuse of the 256-check prefix in an initial 1,024-case sensitivity run; the final saved follow-up uses a fresh stream and records its design history.
