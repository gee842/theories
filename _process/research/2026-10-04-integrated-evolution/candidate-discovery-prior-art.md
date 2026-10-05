# Candidate discovery, validation, and institutional use: a focused audit

5 October 2026. AI-generated research memo for the implemented discovery-and-validation cycle. This audit reads the [formation and revision account](../../../sources/15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md) and [experiment design](situated-frame-experiment-audit.md). It audits that design and supplies conditional checks; it does not claim to have reviewed the subsequent implementation or its results. Five primary research contributions are used below, with manuscript versions identified.

The main risk is conflating a useful search procedure with trustworthy discovery, then conflating discovery with an effective institutional response. Common purposes remove one source of disagreement; they do not remove selection bias, missing counterfactuals, finite evidence budgets, or implementation constraints. The experiment should preserve distinct states for a proposed explanation, validated prediction, estimated intervention effect, admitted reason, and enacted response.

## Closest precedents and what they actually establish

### 1. Searching for new expressions is established; the supplied grammar still matters

[Schmidt and Lipson, *Distilling Free-Form Natural Laws from Experimental Data* (2009)](https://pdodds.w3.uvm.edu/files/papers/others/2009/schmidt2009a.pdf) search both equation structure and parameters by recombining mathematical operators, functions, constants, and measured variables. They assess prediction on withheld data and reuse parts of previously found equations to accelerate later searches. The experimental observations include different approximations emerging from different dynamical regimes and altered expressions when building blocks are removed. Final equation selection also includes human inspection.

**Implication for this design:** generating lag/context expressions that were absent from the active predictor is meaningful bounded discovery, but neither grammar-based generation, held-out comparison, nor reuse of earlier discoveries is new by itself. The analyst still supplies the language, sensors, comparison criterion, and accessible experience. Report discovery within that language; do not equate it with unrestricted conceptual invention or the emergence of purposes. A predictive expression need not identify an intervention's effect.

### 2. Automated hypothesis–experiment cycles and detailed records already exist

[King et al., *The Automation of Science* (2009; author preprint before final corrections)](https://www.aber.ac.uk/~dcswww/Research/bio/robotsci/publications/science18.pdf) describe Adam generating functional-genomics hypotheses, designing and physically conducting experiments, interpreting results, and preserving linked experimental records. The system uses supplied biological models, databases, and software for hypothesis formation and experimental planning. Additional manual experiments examined its conclusions. Consumable replenishment and technical maintenance remain necessary.

**Implication:** the complete generate–test–record loop has a strong practical predecessor. A new contribution cannot rest on adding a proposal generator to a simulation. The sharper target is a causal comparison of institutional rules that maintain, discard, admit, or disable parts of this loop, including the resources and authority needed to use its results. Material maintenance and detailed provenance are themselves established requirements, rather than newly discovered principles.

### 3. Selecting and testing on the same evidence can manufacture discovery

[Dwork et al., *Generalization in Adaptive Data Analysis and Holdout Reuse* (NeurIPS 2015)](https://proceedings.neurips.cc/paper_files/paper/2015/file/bad5f33780c42f2588878a9d07405083-Paper.pdf) formalize how adaptively chosen analyses can overfit reused data. Their Thresholdout result (Theorem 9) permits controlled reuse through a restricted, randomized interface with a budget and sample-size conditions. It assumes an i.i.d. holdout from a fixed distribution; arbitrary access to a supposedly held-out archive does not inherit the guarantee.

**Implication:** candidate ranking, parameter fitting, threshold tuning, and reported validation cannot all inspect the same records without accounting for that selection. Splitting once is insufficient if later proposals are repeatedly adjusted in response to the same validation scores. A fresh batch for each frozen proposal is a simpler first benchmark than implementing reusable-holdout machinery. The institution's validation records and the researcher's final evaluation seeds also serve different purposes and should remain separate.

### 4. Repeated inspection requires a sequential guarantee

[Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences* (2021; linked revised 2022 manuscript, v9)](https://arxiv.org/pdf/1810.08240v9) construct intervals with simultaneous coverage over observation times. Their treatment-effect example permits adaptive treatment probabilities and predictable outcome estimates under bounded outcomes and probabilities bounded away from zero and one. These assumptions support the relevant martingale arguments.

**Implication:** repeatedly applying a fixed-sample confidence interval until a candidate passes does not provide the advertised error rate. Confidence sequences can address optional stopping under their assumptions, but do not by themselves correct adaptive hypothesis generation, confounding, or missing records. Validity over time for one fixed claim also does not automatically supply validity across many claims. For a small initial experiment, fixed candidate-specific sample sizes and a declared total error budget are easier to audit.

### 5. Action-generated evidence requires an evaluation design

[Li, Chu, Langford, and Wang, *Unbiased Offline Evaluation of Contextual-bandit-based News Article Recommendation Algorithms* (2011)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/published-3.pdf) prove that replay under uniform random logging and i.i.d. context/payoff events reproduces the target algorithm's history distribution (Theorem 1). Collecting a target history of length \(T\) takes \(KT\) logged events in expectation for \(K\) actions.

**Implication:** data gathered by the institution's current action policy are not automatically valid evidence about another policy. Record allocation probabilities and the sampling rule. More fundamentally, the proposed accumulation of damage makes future states depend on past actions, violating this contextual-bandit theorem's i.i.d. premise. Independent episodes or units, or a separately justified sequential causal method, are needed. Replaying isolated rows from a cumulative-damage trajectory cannot establish how the alternative institution would have evolved. The simulator may measure that counterfactual externally; it must not silently deliver it to the institution.

## A minimal validation guarantee suitable for the first implementation

The following is an elementary concentration-and-union-bound construction, not a new theorem of discovery. It makes the distinction between selection and validation concrete without requiring the more elaborate methods above.

Let \(\mathcal F_j\) contain everything known before validation of proposal \(j\). The candidate, fitted parameters, baseline predictor, loss, sample size \(n_j\), and significance allowance \(\alpha_j\) are fixed using that history. Obtain a genuinely fresh validation batch. Conditional on \(\mathcal F_j\), assume its paired loss improvements \(D_{j1},\ldots,D_{jn_j}\in[-1,1]\) are i.i.d., with common mean \(\Delta_j\). Positive improvement means that the candidate predicts better than the frozen baseline on the declared validation distribution.

Accept the prediction claim only if

\[
\overline D_j>\sqrt{\frac{2\log(1/\alpha_j)}{n_j}}.
\tag{1}
\]

Hoeffding's inequality gives, on histories where \(\Delta_j\le0\), conditional false-acceptance probability at most \(\alpha_j\). Candidate generation may depend on all earlier batches; it must not inspect its own fresh batch before the candidate is frozen. If deterministic allowances obey \(\sum_{j\ge1}\alpha_j\le\alpha\), then

\[
\Pr(\text{at least one accepted proposal has }\Delta_j\le0)\le\alpha.
\tag{2}
\]

One choice is \(\alpha_j=\alpha/[j(j+1)]\). The proof conditions on each pre-validation history, applies the one-sided bound, then takes a union bound over proposals. Aborting a fixed-size test without acceptance does not inflate this bound; accepting early requires a different rule. An equivalent argument can test improvement beyond a declared margin by shifting the null and threshold. Allocation across prediction tests and subsequent causal tests must be included in any claimed joint guarantee.

This guarantee establishes predictive improvement on a specified distribution, not causal explanation, policy benefit, or discovery of the simulator's true feature. Distinct features may be observationally equivalent or useful proxies. Track semantic recovery of the planted feature only as an external diagnostic, not the definition of every valid discovery.

A parallel causal stage can freeze a proposed operational change and use fresh randomized units or independent reset episodes. The analyst must define its net consequence and sampling assumptions separately. The learner observes the outcome actually generated for each assigned unit; it cannot construct a paired difference by reading both simulator potential outcomes. New proposals require renewed evidence expenditure. Data with cumulative carryover, outcome-dependent censoring, or adaptive subpopulation changes do not automatically satisfy the simple i.i.d. assumptions in (1).

For comparison, if \(M\) independent null tests each reject with probability \(0.05\), the probability that at least one rejects is \(1-0.95^M\). At \(M=20\), that is approximately \(0.642\). This exact illustration assumes independent tests; real candidate tests often share data. Its lesson is that positive-interest selection can produce false discoveries without dishonesty or conflicting goals.

## The strongest implementation pitfalls

**Time and information leakage.** A lag feature must use variables available at the prediction or decision time. A candidate fitted after an incident may use historical variables only if the necessary links were retained. Random row splits may place overlapping windows of the same event in discovery and validation; a later row is not automatically independent of an earlier one. Waiting for an outcome must count toward the correction deadline. Unresolved outcomes are neither successes nor failures.

**Retention that is only cosmetic.** If candidate construction can still access a global raw-history array, deleting records from the displayed archive does not remove information. Audit all inherited summaries, caches, fitted coefficients, pending experiment records, and feature-generation inputs. Conversely, retaining every raw row does not create a missing interpretation automatically. Distinguish raw evidence, a fitted explanatory model, and the procedure needed to regenerate or interpret it.

**Giving the candidate its own answer.** A generator may rank correlations or forecast improvement. It must not receive a hidden hazard flag, the scientist's correct lag, or a callback saying which repair is beneficial. A predictive candidate can select an experiment, but the intervention effect must still be learned. Include a case with a predictive marker that does not identify a useful intervention, and one with a useful coarse policy whose exact causal feature remains unresolved.

**Admission confused with exposure.** To isolate standing, an actor should receive the same interpretable candidate and validation result in both arms and reach the same personal judgment. The institutional acceptance rule alone changes. If records disappear before the actor sees them, the treatment concerns exposure or retention. If the validation standard changes, it concerns epistemic screening as well as institutional standing; label that joint change.

**Authority confused with belief.** An authority ablation holds the accepted proposal fixed and varies whether it can be executed, including execution funding. If accepted beliefs differ, it is not a clean enactment comparison. The existence of an externally imposed veto tests a constraint; it does not explain why the institution reproduces that veto. Endogenous authority formation would require another mechanism.

**Feedback encoded as a desired conclusion.** Budget revision should use the institution's observable records and a stated rule, not hidden truth or an instruction to punish inquiry. Compare a clamped budget and at least one alternative renewal rule. If inquiry loses support solely because the programmer awards it zero recognized value forever, exclusion is stipulated. Delays, inconclusive trials, and false positives should be able to produce either recovery or loss under the same rule.

## Staged ablations and negative controls

| Comparison | Hold fixed | Change | Diagnostic interpretation |
|---|---|---|---|
| Record retention | Physical trajectory and recording opportunity | Which raw links/summaries survive | Tests availability of interpretable experience |
| Active-model expansion | Same accessible records and validation opportunities | Whether grammar search can add a fitted distinction | Tests bounded representation change |
| Evidence standing | Actor-visible candidate, evidence, and judgment | Whether that reason enters institutional decision | Tests admission rather than exposure |
| Enactment | Accepted belief, proposal, and its estimated effect | Effective authority/funding for implementation | Tests the gap between judgment and action |
| Inquiry renewal | Search/validation algorithm and initial capacities | Observable-input budget update versus clamping | Tests reproduction of inquiry capacity |
| Validation discipline | Generator and null environment | Fresh fixed tests versus deliberate evidence reuse | Detects statistical manufacture of discovery |

The first four comparisons can use matched checkpoints before trajectories diverge. They are mechanism tests, not estimators of an entire institution's total effect. The last two require full trajectories. Common random numbers can improve precision, but keep environmental, search, validation, and turnover streams separate; a branch consuming an extra random number must not accidentally change every later shock. Coupling must preserve each arm's marginal distribution.

Run a no-hazard control with positive inquiry and unnecessary-change costs; a hazard too weak to justify the proposed repair; an unavailable-feature control; and an oracle proposal control that bypasses discovery but still pays implementation costs. If the grammar omits the needed feature, failure does not show poor evidence admission. If an archive intervention changes sample counts as well as retention, identify that as a compound treatment or add an equal-information comparison. Equal-budget arms are useful, but need not discard relevant resource benefits: report both the resource-mediated total effect and the comparison at matched expenditure.

Primary measurements should include proposal count, fresh validation count, rejected candidates, false acceptances, model changes, first causal support, admission and enactment times, actual consequences, and each cost. Hazard absence does not make every predictive improvement false: a candidate may fix an unrelated baseline error. Classify false acceptance against the stated statistical claim, and unnecessary repair against its actual consequences. The no-hazard false-acceptance frequency needs uncertainty bounds across independent runs. A nominal test level is an upper bound under assumptions, not a prediction that the empirical frequency must equal that level.

## A simpler benchmark if cumulative dynamics obscure the mechanism

Use independent units with a recorded pre-action context, two already known procedures, and a delayed outcome linked by unit ID. The active model initially omits a context interaction, while the generator can construct it from a small supplied grammar. Use early units for discovery and new units for validation and randomized repair trials. Charge the delay, records, searches, and interventions. Let institutional memory and budgets evolve between cohorts; reserve the cumulative-damage physical dynamics for a second stage.

This preserves bounded discovery, costly record retention, admission, succession, and enactment while making the evidence assumptions auditable. It sacrifices the first design's cumulative physical hazard. Report that scope change explicitly. Add back carryover only after the simpler system distinguishes false discovery, missing representation, rejected evidence, and blocked implementation.

## Claim boundary

The implemented loop can establish that particular institutional choices preserve or destroy a statistically disciplined route from experience to effective correction in a specified common-interest environment. Automated discovery, experimental validation, detailed records, action-dependent sampling, and shared-purpose epistemic failure each have substantial predecessors.

The prospective contribution is their identified coupling to the renewal of institutional capacities, with distinct evidence and authority interventions and costly false alternatives. This audit does not establish mathematical priority for that coupling. A finite grammar remains a supplied space of possible distinctions; a simulator remains an analyst's representation. The useful orienting question survives those limits: which part of the route from consequential experience to justified, executable revision fails, and what maintains that part over time?
