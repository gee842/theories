# Independent implementation review

Internal AI review of [analyze.py](analyze.py), the frozen [protocol](PROTOCOL.md), and [recorded results](results/analysis.json). No implementation file was changed. The review includes an independently written rational transition enumerator and an independent graph calculation, rather than only rerunning the implementation's checks.

## Verdict

No blocking event-order, accounting, policy-information or graph-analysis error was found in the declared comparison arms. The implemented model contains the reciprocal loop promised by the revised protocol. Its strong finite and infinite-horizon conclusions are about this specified synthetic institution, not empirical validation or a new universal theorem.

The most important reporting distinctions are retained capacity versus current output, finite reliability versus indefinite safety, and recurrence of beneficial responses versus a guarantee to address every particular discrepancy. The final interpretation must also retain the limited criterion repertoire and the externally fixed admission and execution settings.

## Event order and information access

The enumerated transition follows the frozen order:

1. The context changes.
2. An outside entrant can arrive only if skilled capacity is absent.
3. The installed criterion and skill count determine F, Q or T.
4. A qualified inquiry produces a noisy report; admission updates the retained record; permitted adaptive execution uses that record.
5. Adequacy is evaluated against the actual context, separately from completed-case count.
6. Delivered apprenticeship adds a carrier.
7. At most one carrier is lost through adequacy-dependent attrition.
8. Actual succession uses the post-loss carrier count and the prior criterion's weight; records can then be forgotten.

The independent event sampler implements the same order without calling the transition enumerator. A training event can occur only when the adaptive criterion encounters k=1, so it never creates a mentor or qualified apprentice spontaneously at k=0. An external entrant is a separately logged source, not disguised internal renewal.

The policy function receives r, q, k, the retained record, an available report and the declared settings. It does not receive hidden e. The environment uses e to generate a report and to determine adequacy and its attrition consequence. This is a physical consequence in the transition law, not hidden-state access by the decision-maker. The model does assume that current criterion, routine and carrier count are available to the institutional procedure.

The causal loop is present: q affects inquiry and apprenticeship; records can alter r; adequacy affects attrition; attrition changes k and triggers succession; successor q changes later work and record use. Without failure-induced attrition, the information/action module no longer feeds back into the skill/criterion marginal. This is explicitly checked below.

The loop should not be overstated. q denotes one of two inherited criterion/work policies. It is not a model of discovering an unanticipated goal. Admission and execution are fixed experimental settings, while q determines whether inquiry is performed and whether the stored record is used. Their constitutional evolution is not separately modeled. Experience changes succession through withdrawal/overload, not through a modeled deliberative argument about which criterion is legitimate.

## Independent rational transition reconstruction

A separate enumerator was written for all 72 states using rational arithmetic. It independently branches over context switching, entry, report error, attrition, appointment and forgetting; it does not call `branches`, `decision`, `coin` or `care_probability` from the implementation. The declared decimal parameters were converted to their exact rational values.

The enumerator and independent graph check are preserved in [verify_independent.py](verify_independent.py). Its [machine-readable report](results/independent_verification.json) records the checked production source hash, checker hash, exact survival fractions, safe-core states and reachable bottom classes. Running the checker rebuilds those results and verifies that the production source still matches its recorded analysis.

Seven arms were checked this way: endogenous, protected, no admission, no execution, no training, rare adverse succession and re-entry.

- All 72 rows in each arm sum **exactly** to one in rational arithmetic.
- Every positive-probability edge agrees with the implementation.
- The maximum difference between the rational matrix converted to doubles and the implementation's matrix is 1.11×10⁻¹⁶.

A second calculation obtains transitive reachability directly and groups mutually reachable states. It reproduces the bottom strongly connected components returned by the implementation. Computing the safe core as the states from which no unsafe state is reachable reproduces the iterative greatest-closed-subset calculation in every checked arm.

Exact rational propagation of the surviving distribution for 200 transitions gives:

| Arm | Probability of never losing capacity through period 200 |
|---|---:|
| Endogenous | 0.09436917425904917 |
| Rare adverse succession, adaptive weight 10000 | 0.9988099634015596 |

These decimals are rounded presentations of exact rational calculations. The implementation's floating-point results agree at the displayed practical precision. The ordinary implementation uses floating-point transition probabilities and linear solves; it should not describe every recorded probability or mean as an exact rational result merely because the finite event space is exhaustively enumerated.

## Safety and recurrence checks

The safe set in this study is specifically k≥1. The greatest-safe-core algorithm repeatedly removes a state if it has any positive-probability transition outside the retained set. It uses no probability cutoff that could erase the rare adverse-succession path.

The endogenous, no-admission, no-execution, no-training, rare-adverse and re-entry arms have empty almost-sure safe cores. Re-entry can restore capacity after loss; it does not turn the property “never lost capacity” into a true statement. The protected arm has 36 safe-core states.

The protected core is not the entire 48-state positive-capacity set. A volume incumbent with k=1 can lose its final carrier before the protected succession mechanism has an opportunity to install an adaptive successor. The supplied initial state is correctly inside the core. The theorem and report should therefore retain their initial-state condition.

The bottom-class event analysis correctly asks whether a positive-probability event-producing transition exists inside each reachable closed irreducible class. In a finite irreducible class such an event recurs almost surely under the specified Markov event process. Thus the protected case genuinely includes recurrent inquiry, delivered teaching and beneficial revisions, rather than inferring them from the label “adaptive.”

This event recurrence does not establish that every individual discrepancy is addressed, that it is addressed before a deadline, or that every succession transmits a particular record. Those stronger properties need the pending-obligation monitors discussed in [FORMAL.md](FORMAL.md). They are not implemented here and should not be implied by the recurrence result.

## Stronger checks of the gate and feedback controls

The implementation compares distributions over the first 200 periods. An additional independent calculation checks the relevant one-step projected kernels.

For no admission and no execution, project onto `(e,r,q,k)` over reachable states. Within each arm, the projected transition distribution does not depend on the omitted record. The two arms' projected kernels agree, with maximum numerical difference 2.78×10⁻¹⁷. This establishes the mechanism behind their matching path distributions, beyond merely comparing separate time marginals. Their record distributions are allowed to differ.

With failure-induced attrition removed, project onto `(q,k)` over all 72 states. The projected kernel is independent of e, r and b and agrees across ordinary, no-admission and no-execution settings to 1.11×10⁻¹⁶. The outcome-dependent attrition term is therefore the explicit feedback route that reconnects experience and response to institutional continuation. Removing it has the advertised structural effect.

There is no need to call an admission failure and an execution failure identical mechanisms. They produce the same operating path law in this particular setup because both preserve the initial routine while the remaining physical processes depend on that routine. Raw inquiry, record admission and execution remain different event quantities.

## Interpretation of the recorded outcomes

The recorded endogenous expected first-loss time is approximately 91.0924 periods. Removing admission or execution lowers it to approximately 49.4410, and both arms have survival probability approximately .00672182 at period 200. Perfect inquiry does not repair a succession mechanism that retains a path to terminal skill loss.

Rare adverse succession has expected first loss approximately 159,002 periods and survival probability .99880996 through period 200. Its empty safe core and the positive uniform depletion path still imply eventual loss with probability one. These results are compatible; a long expected lifetime is not an indefinite guarantee.

Re-entry leaves the first-loss distribution unchanged, because it acts only after capacity reaches zero. It changes later recovery and recurrence, giving limiting positive-capacity occupancy approximately .468494 under the stated arrival rate. That fraction is a model result under an explicit outside source, not evidence of self-sufficient regeneration.

The outcome profile exposes a substantive tradeoff. Protected succession has long-run adequacy approximately .935484 but completes one case per period, giving approximately .935484 adequate cases per period. After skill depletion, the volume regime completes two cases per period, each adequate with probability .5 under the symmetric switching context, giving one adequate case per period. The protected regime retains skill, information and responsiveness and has much higher adequacy per case; it does not dominate the depleted regime on every aggregate output measure. This is a reason to preserve the plural outcome table, not to rename one quantity universal welfare.

Finally, k=0 is loss of the specified skill and revision mechanism. Basic case production continues. “Capacity depletion” or “loss of this corrective function” is more accurate than extinction of the organization or loss of all activity.

## Boundaries of this validation

The code is a verifier for the stated finite construction and comparisons, not a generic proof that all adaptive institutions meet these properties. Initial-distribution summaries use the declared `START`; the safe core is calculated globally, while recurrent-class summaries retain only classes reachable from that start. The reported mean first-loss solve is used for the current empty-core cases. Generalizing the helper to arbitrary initial states with unreachable safe recurrent classes would require a reachability-specific first-passage treatment.

The exact finite-state mathematics is standard. The model's substantive test is the joint inclusion of selected succession, inquiry, record admission, execution and skill renewal, with nonfinancial work allocation and explicit outside restoration. Its parameters, candidate weights, binary context and attrition mechanism remain synthetic assumptions. This review validates implementation consistency and the stated finite-model properties; it does not establish scientific priority, empirical realism, political legitimacy or universal transfer.

## Addendum: external microbial prediction analysis

The [external protocol](external-test/PROTOCOL.md), [analysis implementation](external-test/analyze.py), original matched data and saved predictions were independently inspected. This addendum concerns the actual secondary analysis and the identified preprocessing repair; it does not turn the synthetic institution model into an empirically fitted ecological model.

### Outcome and split correctness

The target is independently measured, background-corrected next-cycle OD600. It is not a growth rate computed from the same composition predictors. Current cycles 1, 3 and 5 are correctly joined to cycles 2, 4 and 6. Independently recomputing blank subtraction and the condition means reproduced all 72 current/next OD pairs exactly.

The absence of replicate identifiers in the biomass table is handled honestly: all three biological replicates are averaged within each source, salt, temperature and cycle. No fictitious one-to-one pairing to sequencing samples is introduced. This changes the prediction unit to a condition mean; it cannot support individual-replicate claims.

All three cycle pairs of a condition remain together in the condition-held-out split. The source-held-out split excludes every condition from that source during regression fitting. Feature standardization uses the training fold only. The source indicator vocabulary is determined by treatment labels, without using outcomes; columns constant in training are dropped. I found no downstream outcome leakage in the join, scaling or ridge fit.

An independent implementation of the same primary regression solved ridge through an augmented least-squares design, rather than the production normal-equation solve. The baseline and augmented predictions under both split schemes agree with the saved predictions within 5.0×10⁻¹⁵. This independently reproduces the reported primary errors.

### Preprocessing and temporal boundaries

The supplied `norare` feature files use a global prevalence screen over the complete experimental sample set. Held-out conditions and later cycles therefore influence which taxa enter the deposited feature summaries. This is unsupervised preprocessing, not direct use of future biomass labels, but it prevents a claim that the complete measurement-to-prediction pipeline is isolated by fold.

The [repair protocol](external-test/PROTOCOL-REPAIR.md) appropriately preserves the original results and fixes a single repair before computing revised outcomes: use sample-local composition summaries without the global prevalence filter, retaining the original target, predictors, folds, penalties and comparisons. It also requires reproducing the original summaries as an implementation check. That check passed across all 368 samples: maximum absolute errors were 2.49×10⁻¹⁴ for MCN and 1.60×10⁻¹⁴ for Shannon, against a frozen tolerance of 10⁻⁷.

The repaired reconstruction was independently inspected. Its taxonomic eligibility is fixed, copy-number lookup uses the fixed external rrnDB hierarchy, and each corrected summary depends only on the eligible counts of that sample. The global prevalence mask is used exclusively to reproduce the original summaries. Directly evaluating a row alone or within a multirow array produces exactly the same corrected summaries. This checks sample locality at the declared count-table stage; it makes no claim about redoing upstream sequencing and taxonomy inference.

The repair wrapper only substitutes the two feature files and sends output to a separate results directory; the original analysis is preserved. Comparing all 72 repaired matched rows to the original confirms that source, salt, temperature, cycle, current OD and next OD are identical. Only MCN and Shannon change. No regression setting, target, fold or primary criterion is changed by the repair.

Even after that repair, deposited read-count and taxonomy tables remain upstream sequencing products, and the regression folds train on other trajectories' later cycles. These are cross-condition or cross-source generalization tests of a next-cycle target. They are not a chronological forecast trained only on observations available at an earlier calendar date, nor a fully prospective sequencing-to-prediction validation.

### The original primary result is mixed

The original primary condition-holdout comparison gives RMSE .0936919 → .0868784, an absolute reduction of .0068135 OD units or approximately 7.3%. MAE changes .0686791 → .0689487, a small worsening. Fourteen of 24 condition groups improve in squared error. The descriptive four-source bootstrap interval for RMSE gain crosses zero.

The frozen protocol specified improvement in both RMSE and MAE as the primary positive signal. That signal was not obtained. Favorable source holdout, alpha=10 and the MCN-only ablation are legitimate prespecified secondary results; none should replace the original primary result after inspection.

The source-block bootstrap has only four source units and reweights already produced out-of-fold errors; it is not a full repeated-data analysis that refits the learning procedure in each resample. Its interval is descriptive, not a reliable population-level significance claim. Likewise, one of 100 random-feature controls beating the augmented primary result does not supply a permutation-test p-value. The nuisance features do not reproduce the ecological correlation structure of the measured traits.

### The repaired primary result remains mixed

With the repaired summaries, the unchanged primary baseline has RMSE .0936919 and MAE .0686791. Adding both traits gives RMSE .0868653, a reduction of .0068266 OD units or approximately 7.3%, but MAE .0690178 is worse. Fourteen of 24 condition groups improve in squared error. The descriptive four-source interval for RMSE gain is approximately [−.0057943, .0160762], again crossing zero. The frozen requirement that both errors improve is still not met.

The source-holdout secondary comparison improves RMSE .0934974 → .0771899 and MAE .0683288 → .0595960, with 16 of 24 condition groups improving in squared error. This remains a useful secondary observation under a four-source design; it does not replace the failed primary positive criterion. The preprocessing repair removes the identified global prevalence dependence without changing the study's mixed interpretation.

### Baseline and generalization

The baseline is not an obvious strawman: it includes current OD, environmental context, cycle curvature and source-specific environmental terms, and it improves substantially over persistence. It is still one fixed regularized feature family. The composition summaries could supply information about omitted nonlinear environmental responses or source structure, without identifying a causal composition-to-renewal mechanism. The observed gain is conditional on this baseline and these folds.

Seventy-two prediction rows and 24 condition trajectories do not constitute 72 or 24 independently sampled ecosystems. Sources, passages and experimental processing are shared; replicate averaging further removes within-condition variation. Holding out one of four sources is useful but does not establish transfer across independently replicated ecological populations, much less institutions or AI systems.

This external analysis tests a narrow state-description question: whether two contemporaneous composition summaries add predictive information beyond the declared current-state and context features. It does not yet test reciprocal feedback, selected succession, maintenance of correction, a new shock/recovery outcome, changing purposes or the full general theory. Retaining the mixed result and the preprocessing limitation is necessary for that distinction to remain credible.
