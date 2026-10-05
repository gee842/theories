# Financing recurrent inquiry: closest precedents and limits

Research memo, 5 October 2026. AI-generated research assistance under Ren's research direction. Primary sources were browsed for this memo; versions and corrections are identified below. This is a literature and design audit, not empirical evidence about institutions. It complements [the mathematical memo](inquiry-renewal-math.md).

The proposed experiment can join three established mechanisms that must remain distinguishable: financial interruption of a valuable activity, incentives that discourage uncertain exploration, and selection that reproduces methods rewarded by imperfect evaluation. A grant rule based on successful revisions can participate in all three, but none follows automatically from the others. Preserving an inquiry service can be necessary for future correction while being insufficient for good inquiry or desirable coordination.

## Six close primary sources

### 1. Bounded reserves and eventual ruin

David C. M. Dickson and Howard R. Waters, **Some Optimal Dividends Problems**, *ASTIN Bulletin* 34(1), 49–74 (2004). [Publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0515036100013878).

Their introduction and classical-risk-model discussion explicitly identify certain eventual ruin under a constant upper dividend barrier. They also study injections of capital after ruin. This is a close mathematical predecessor: surplus cannot accumulate indefinitely because the institution distributes amounts above a ceiling, and unfavorable sequences can exhaust what remains. The insurance process differs from a research service, so its particular formulas should not be transplanted without matching assumptions.

**Use here:** cite established ruin theory for the finite-buffer mechanism. A reserve ceiling may represent payout, appropriation, or limited access to a larger balance sheet. Restart finance changes permanent extinction into an outage/recovery problem. Neither the eventual-ruin statement nor the idea of financing restart is new.

### 2. Exploration incentives and tolerance of unsuccessful attempts

Gustavo Manso, **Motivating Innovation**, *Journal of Finance* 66(5), 1823–1860 (2011). [Journal record](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2011.01688.x); [author manuscript inspected, 26 November 2010](https://faculty.haas.berkeley.edu/manso/mi.pdf).

In a principal–agent model with exploration, exploitation, and shirking, contracts implementing exploration tolerate early failure and reward later success. The inspected manuscript's propositions 2 and 4 distinguish exploration incentives and the value of commitment; short-term contracts cannot generally reproduce the optimal long-term exploration contract. These are conditional optimal-contract results, not a theorem favoring unconditional funding in every environment.

**Use here:** the inadequacy of immediate performance rewards for uncertain inquiry is established. Our separate question is whether a service with aligned intentions and fixed behavior can physically remain available under outcome-contingent funding. Financial survival and incentive compatibility are different constraints. If the new model has no strategic choice or hidden effort, it does not reproduce Manso's mechanism.

### 3. Learning can cease because actions determine evidence

Monica Brezzi and Tze Leung Lai, **Optimal Learning and Experimentation in Bandit Problems**, *Journal of Economic Dynamics and Control* 27(1), 87–108 (2002). [Publisher article and section excerpts](https://www.sciencedirect.com/science/article/pii/S0165188901000288); [Stanford's September 2000 report record](https://statistics.stanford.edu/technical-reports/optimal-learning-and-experimentation-bandit-problems).

The publisher's section on the value of experimentation describes incomplete learning under discounted Bayesian bandit allocation: with positive probability an optimal policy uses the truly optimal action only finitely often. This is an existence result within their bandit assumptions, not a characterization of all optimal learning policies. Their earlier theorem is attributed to Brezzi and Lai (2000), extending earlier incomplete-learning work including Rothschild (1974).

**Use here:** endogenous absence of corrective evidence is established even without financial ruin or bad intentions. A research service losing the ability to test because it cannot pay is an additional mechanism. Conversely, paying its expenses does not make it choose sufficiently informative experiments. An imposed exploration quota must be identified as a policy assumption, not a consequence of adequate funding.

### 4. Selection of methods without deliberate manipulation

Paul E. Smaldino and Richard McElreath, **The Natural Selection of Bad Science**, *Royal Society Open Science* 3, 160384 (2016). [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC5043322/); [2023 correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC10480692/).

The model connects publication-based reproductive success of laboratories to cultural transmission of research methods. Under its specified relationships between output and rigor, selection can degrade methods without conscious cheating. This supplies a direct predecessor to the distinction between what spreads and what supports reliable inquiry.

**Version caution:** the correction fixes a coding error that used the initial replication probability instead of each laboratory's evolving value, along with reproduction-order and textual issues. The authors report that the main conclusions remain; the original replication-rate dynamics should not be presented as a correctly implemented test of the stated model.

**Use here:** a single service under a fixed funding rule is not yet a model of selection among institutional practices. To claim reproduction or evolution of a rule, specify competing variants, their transmission, and their differential persistence.

### 5. Funding rules, negative results, and cultural selection in one model

Paul E. Smaldino, Matthew A. Turner, and Pablo A. Contreras Kallens, **Open Science and Modified Funding Lotteries Can Impede the Natural Selection of Bad Science** (2019). Read and cite the [corrected full article, *Royal Society Open Science* 6, 191249](https://pmc.ncbi.nlm.nih.gov/articles/PMC6731693/), which replaces editorial changes to the original 190194 article.

Labs pay for studies, obtain additional grants, publish results, and transmit methods through publication-weighted succession. Funding can follow publication history, methodological quality, randomness, or a quality-screened lottery; negative-result publication and peer review also vary. The simulation finds benefits from quality-directed funding, particularly with improved publication and review practices. Its methodological-integrity benchmark accesses a lab's intrinsic false-positive rate; hypotheses arrive at a fixed truth base rate. Grant seeking remains available without a positive research balance.

**Use here:** this is the nearest combined institutional predecessor. Our useful distinction would be local evidence generating proposals, fresh observable validation rather than direct access to intrinsic quality, and financing charged against real productive alternatives. Its grant mechanism also shows why a zero research balance need not mean permanent institutional death. Random funding or protected funding alone does not establish research quality.

### 6. A relevant empirical comparison, with limited identification

Pierre Azoulay, Joshua S. Graff Zivin, and Gustavo Manso, **Incentives and Creativity: Evidence from the Academic Life Sciences**, *RAND Journal of Economics* 42(3), 527–554 (2011). [Author manuscript inspected](https://www.mit.edu/~manso/hhmi.pdf); [journal DOI](https://doi.org/10.1111/j.1756-2171.2011.00140.x).

The paper compares HHMI investigators with selected comparison researchers and studies changes in research output and direction. The findings are consistent with longer horizons and tolerance of unsuccessful exploration encouraging more exploratory work. The manuscript explicitly discusses nonrandom program selection, matching and weighting on observables, and the possibility that selection identifies researchers already likely to explore.

**Use here:** motivation for later empirical work, not validation of our proposed reserve theorem or evidence that a protected grant is universally superior. Funding regimes differ along several dimensions; this comparison does not isolate a finite-buffer mechanism. No numerical estimate from this study should become a parameter calibration without an explicit transport argument.

## What the elementary survival result actually adds

Let an active inquiry service have accessible reserves bounded by a finite ceiling, a positive unavoidable service cost, and no replenishment route after shutdown. Suppose some finite block length \(L\) has a uniform conditional probability \(\epsilon>0\) of forcing shutdown from every surviving history. For shutdown time \(T\),

\[
\Pr(T>nL)\le(1-\epsilon)^n,
\qquad \Pr(T<\infty)=1.
\]

This follows by conditioning on successive surviving blocks; independent periods are unnecessary. A uniformly possible sufficiently long block without credited rewards is one sufficient mechanism. The accompanying math memo states payment timing, gives the expectation bound and finite-chain formulas, and supplies the positive-mean example. This argument is an elementary application of established probability, not a new universal survival law.

The useful conceptual separation is **expected productive return versus accessibility of resources during a sequence of attempts**. Positive mean income before applying the reserve cap does not imply positive drift of the capped reserve in every state. Overflow may benefit other people rather than disappear; it remains unavailable to rescue inquiry unless the allocation rule allows it to return. Charging this opportunity cost is essential to a fair comparison.

An almost-sure infinite-horizon statement is also not a prediction of imminent failure. A larger finite buffer can make failure exceedingly unlikely over a relevant operating horizon. Report the exact finite-horizon outage probability and expected time to interruption, not only eventual absorption.

The survival premise fails or changes meaning with free dormancy, funded rebuilding, a growing reserve ceiling, an accessible parent balance sheet, only finitely many required investigations, a protected revenue floor sufficient for expenses, or shortfall probabilities that diminish sufficiently fast. A positive *unconditional* frequency of unsuccessful rounds does not establish the required conditional chance of arbitrarily long damaging sequences.

## Design choices that decide the interpretation

**Define the service, not just an account.** A policy that never spends again can preserve cash while eliminating inquiry. Specify whether the obligation is continuous monitoring, a minimum chance of investigating each locally reported problem, or timely response when problems recur. A funding rule can satisfy one and violate another.

**Generate proposals from permitted observations.** A local signal may affect which candidate is nominated, whether anything is reported, or the proposal's content. Those public traces can themselves carry information. An authority that sees a proposal but ignores its signaling content is a stipulated limited policy, not automatically a rational Bayesian decision maker. Discovery within a finite supplied grammar should not be described as generation of arbitrary unanticipated concepts.

**Separate no credit from no epistemic value.** Correct rejection of a harmful proposal, an informative negative result, no actionable candidate, a missed beneficial candidate, and an erroneous positive result have different meanings. If the credit rule rewards only deployment, a valid negative result can be financially unrewarded while still improving decisions. Count and cost these events separately. Do not call all of them failed research.

**Separate statistical error from capture.** A poor candidate or a false acceptance from an honest noisy test is not by itself institutional capture. Capture requires a specified process that changes access, evidence admission, evaluation, or allocation to serve an actor or group. Exogenously increasing a false-proposal rate is a stress test, not an explanation of how capture emerges.

**Fresh validation is not perpetual error control.** Candidate nomination based on past observations can be followed by a conditionally valid fresh test. But fixed per-round error control does not provide a fixed lifetime probability of avoiding all false deployments. State whether the target is per-test error, expected cumulative harm, false discovery rate, or lifetime familywise error. The last target can be bounded with summable conditional error levels, potentially at a substantial power and resource cost. The survival theorem itself requires no particular testing criterion.

**Fixed rules are not evolving rules.** If grants depend on observed outcomes, funding paths are endogenous. The evaluation standard, base-allocation commitment, and participant rights may still be externally supplied. Likewise, an institutionally protected service can remain alive while revising the wrong things. Survival, validation quality, realized welfare, and the evolution of authority are separate outcomes.

**Finance must be consolidated.** A protected allocation reallocates productive resources; it does not create them. Record other output forgone, expenses, reserves, and overflow under the same timing convention. If support itself comes from a finite endowment or risky external sponsor, include that constraint before claiming indefinite continuity. Preserving the inquiry function through replacement providers may be enough; permanent survival of one incumbent is not intrinsically required.

## Informative comparisons and possible contribution

Compare outcome-contingent finance with a paid baseline allocation under the same productive resource process, evaluation rule, local observations, and initial reserves. Then remove mechanisms one at a time: permit rebuilding, remove the reserve cap, make dormant readiness costless, credit warranted negative evidence, or change the statistical protocol. Include a stable, already-understood environment where continual protected inquiry has negative net value. Otherwise the protected institution may win because the experiment assumed an endless supply of sufficiently valuable corrections.

A meaningful next result would identify where **a common-purpose institution's own successful-revision credit rule eliminates future opportunities to discover a needed correction**, despite adequate total production, and how much useful output different continuity arrangements cost. Local observations and fresh validation would make the information-to-finance feedback explicit. The finite-buffer ruin argument explains only the interruption; it does not already explain whose questions disappear, which missed correction matters, or the welfare cost of protecting access.

The contribution claim should therefore be a transparent synthesis and a specific mechanism comparison. None of the sources supports a universal optimal research budget, permanent protection of every research organization, or a deduction of human purposes from survival mathematics. Choosing whose harms count, who may pose a question, and what authorities may block requires an explicit normative specification. The formal model can reveal consequences and feasibility constraints once those commitments are stated.
