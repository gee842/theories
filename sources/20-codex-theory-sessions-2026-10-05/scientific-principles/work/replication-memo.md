# Replication, disclosure, criticism, and paid checking

Research memo, 5 October 2026 (Asia/Bangkok). Scope: conditional results for the scientific-principles investigation. The propositions below are elementary applications of information, probability, and decision theory; no novelty or empirical universality is claimed. Reference workspace was read only.

## Result in one paragraph

Situated causal reasoning does not by itself require every investigation to be repeated, every detail publicly disclosed, or every criticism pursued. Add an aim—such as detecting an error with controlled false alarms, improving decisions under a specified loss, or preserving future correction—and conditional requirements become available. A check must supply relevant information or a relevant stress on assumptions; dependence determines how much multiple checks add; the benefit must justify its resource and intervention costs under the declared criterion. Reproducibility, replication, transparent methods, and adversarial checking are useful implementations of these requirements. None is individually sufficient for truth, always necessary in its conventional form, or guaranteed to improve every investigation.

## 1. Distinguish the operations before deriving their value

Use the NASEM convention here: computational reproduction reruns an analysis using the original data and specified computational conditions; replication collects new data addressing the same question. Generalization asks about additional contexts. Terminology varies by field. Agreement must be interpreted with uncertainty, and reproduction can faithfully repeat an error. [NASEM 2019, Summary, pp. 1–6](https://www.nationalacademies.org/read/25303/chapter/3).

Three checks therefore target different failures:

* **Replay:** can the reported result actually be obtained from the archived input and procedure? This can expose missing steps, incompatible environments, transcription, and undocumented choices.
* **Independent implementation or measurement:** does another derivation, program, apparatus, or calibration give a compatible result? This probes some implementation and measurement assumptions.
* **New-data replication or contextual variation:** does the relevant pattern recur within the claimed scope, and which changes alter it? This probes sampling variation and transport assumptions.

These distinctions are operational, not a hierarchy in which the last check makes all earlier checks dispensable. An independently coded analysis of one biased dataset can preserve its bias; new data processed through the same wrong formula can preserve the formula's error. Conversely, a mathematical identity can be established without collecting a new physical dataset.

## 2. Proposition R1: additional independent detection opportunities reduce misses

Let \(E\) mean a particular asserted result is erroneous. Let \(M_i\) mean check \(i\) fails to detect that error. Assume the error remains fixed during the checks and, conditional on \(E\), the checks' misses are independent with probabilities \(r_i\). If any valid detection triggers investigation, then

\[
\Pr(M_1\cap\cdots\cap M_k\mid E)=\prod_{i=1}^k r_i.
\]

This is the product rule under conditional independence, not a deduction from the number of institutions or reviewers. Independence conditional on a relevant error class is stronger than different names, different computers, or fresh random seeds. Without independence the intersection still cannot exceed any individual miss probability, provided the old checks and decision rule remain available; a multiplicative reduction is unwarranted.

**Common-failure counterexample.** Conditional on an error, draw a common blind spot \(C\sim\mathrm{Bernoulli}(q)\). If \(C=1\), all checks miss. Otherwise, their residual misses are independent with probability \(r\). Then

\[
\Pr(\text{all miss}\mid E)=q+(1-q)r^k.
\]

With \(q=.1,r=.2\), one check misses .28; two miss .136; five miss .100288. Arbitrarily many such checks leave a .1 floor. The marginal gain from one more check is \((1-q)r^k(1-r)\). A check that changes the common failure mechanism may be more valuable than additional checks of the old kind. It need not be: its sensitivity, false alarms, scope, and cost still matter.

**Exact replay counterexample.** If a deterministic calculation is rerun with the same input and faulty code on a stipulated identical execution path, the second output is a known function of the first conditions. It supplies no new information about whether that code embodies the correct equation. Real replays can nevertheless test whether those conditions were actually recorded accurately, or whether hardware/runtime nondeterminism matters. The zero-information conclusion applies only when those uncertainties have already been excluded.

**Correlated measurement example.** Let \(Y_i=\theta+B+\varepsilon_i\), with zero-mean shared calibration error \(B\), variance \(\tau^2\), and independent zero-mean measurement errors of variance \(\sigma^2\), independent of \(B\). Then

\[
\mathbb E[(\overline Y-\theta)^2]=\tau^2+\sigma^2/n.
\]

Averaging suppresses sampling noise but leaves calibration uncertainty. If \(B=b\) is a fixed unknown offset, mean squared error instead contains \(b^2\). With no independent calibration or identifying restrictions, the data only identify \(\theta+b\). This illustrates why repeatable precision is not accuracy and why shared auxiliaries belong inside the error model.

The accompanying [exact checks](replication-checks.py) enumerate the common-failure model, rather than relying on Monte Carlo. [Results](replication-checks.json) preserve all declared cases.

## 3. Proposition R2: optional, costless information cannot worsen optimal decisions

Assume a supplied prior for state \(\Theta\), a fixed action set, integrable loss \(L(\Theta,a)\), a correctly specified information channel, and a decision maker able to ignore information. Let current information be \(\mathcal F\) and an added report enlarge it to \(\mathcal G\supseteq\mathcal F\). Define

\[
R(\mathcal F)=\inf_{a\ \mathcal F\text{-measurable}}\mathbb E L(\Theta,a).
\]

Then \(R(\mathcal G)\le R(\mathcal F)\): every old decision rule remains allowed. Strict improvement requires a report that changes a consequential choice for some possible evidence. This argument is about the option to use information, not a psychological claim that actual audiences cannot be confused.

For equal-prior binary states and zero-one classification loss, the current risk is .5. A symmetric diagnostic of accuracy .9 reduces risk to .1, a gross value .4. A monetary cost expressed in the same loss units must be below .4 for strict net benefit in this one-step problem. An uninformative diagnostic has zero gross value. If the best action stays the same after every result, decision value can be zero even though the posterior changes.

**Disclosure implication.** Methods, calibration records, exclusion decisions, analysis history, and code can enlarge an auditor's information and action options. Suppose two production histories lead to the identical public report, but one used a valid fixed test and the other selected the most favorable of many tests. An auditor restricted to that identical report cannot reliably distinguish the histories. Some distinguishing channel is necessary for that audit aim. Full public raw-data disclosure is not thereby necessary: sufficient provenance, authorized inspection, independent checks, or other informative summaries can sometimes provide the required distinction.

Disclosure itself can be costly, misleading, privacy-intrusive, or behavior-changing. The non-increase proof does not cover compulsory processing costs, bounded attention, a misspecified channel, changed incentives, or altered available actions. Ethical limits on disclosure require additional commitments. Epistemic usefulness alone does not decide whose private information may be released.

## 4. Adversarial checking changes search; opposition is not a reliability theorem

Represent the possible defects as a declared set \(\mathcal E\). Check \(i\) detects defects in \(D_i\subseteq\mathcal E\) in a noiseless model. Adding the check expands detectable defects from \(\bigcup_iD_i\) to its union with the new set. A challenger helps precisely when the challenger supplies previously missing detection coverage and reports it successfully. If every critic has the same blind spot, opposition adds no coverage. If the system suppresses every detected objection, detection does not produce correction.

For noisy checks, “investigate if any critic objects” increases false alarms. Under a correct result, twenty independent checks each issuing an unwarranted alarm with probability .05 produce at least one alarm with probability \(1-.95^{20}=.641514\). A union bound permits controlled allocation \(\sum_i\alpha_i\le\alpha\) without independence, provided each declared guarantee really holds for the actual protocol. Thus broader challenge and stricter acceptance are distinct design choices. A criticism can appropriately generate a question without itself validating a refutation.

Mellers, Hertwig, and Kahneman's original adversarial-collaboration study proposes jointly agreed empirical tests, recorded expectations, and an arbiter; participants retained theoretical disagreements after the studies. It is an instructive protocol and case, not an experiment establishing that adversarial collaboration always beats alternatives. [2001, pp. 269–270, especially Table 1](https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2001---do-frequency-representations-eliminate-conjunction-effects.pdf).

## 5. Reanalysis and independence must be assessed through the full transcript

Publishing a benchmark can improve inspectability while permitting future investigators to adapt to its examples. The fact that a final program never directly reads validation labels does not make its design independent of earlier feedback. Indirect dependence through published scores, prior choices, and rejected versions still belongs in the selection transcript.

Dwork and colleagues formalize adaptive statistical queries under independent samples from a fixed distribution and construct mechanisms preserving generalization under bounded interaction. Their results show both why naive reuse is problematic and why fresh data for every question is not universally necessary. The guarantees concern their specified mechanisms, sample assumptions, accuracy tolerances, and resource costs. They do not validate unrestricted reuse, arbitrary distribution drift, or every form of scientific inference. [STOC paper, §§1.1–1.2 and 5](https://arxiv.org/pdf/1411.2664); [holdout-reuse paper](https://proceedings.neurips.cc/paper/2015/hash/bad5f33780c42f2588878a9d07405083-Abstract.html).

The methodological consequence is conditional: if one invokes an independence-based validation guarantee, one must establish the required independence or replace the guarantee with a justified analysis of dependence. “Independent lab” is not a proof; “same dataset” is not an automatic disqualification. Disclosure of selection and access histories makes those claims more assessable.

## 6. A test is also an action with state and resource consequences

A minimally adequate sequential model is

\[
(S_{t+1},Y_{t+1})\sim K_\theta(\cdot\mid S_t,a_t),\qquad
b_{t+1}=b_t-c(S_t,a_t)+g_{t+1},
\]

where \(a_t\) includes observation, testing, repair, waiting, and disclosure. A feasible policy respects dated costs and access restrictions. The kernel includes measurement back-action, intervention effects, drift, and learning by observed people when relevant. Treating observations as passive iid samples is a special case requiring support.

**Destructive-test counterexample.** A unique specimen is either viable or nonviable with equal probabilities. Choosing to use a viable specimen yields one unit; using a nonviable one yields zero; abstaining yields zero. A perfect assay reveals its original type but destroys it, so the use option disappears. Without assay, expected value is .5; after assay it is zero. The test supplies perfect information and worsens this decision. Archival scientific knowledge could still justify it under an expanded objective; that value is absent from this explicitly narrow example.

**Moving-target counterexample.** If test exposure trains participants, depletes material, changes a population, or leads to strategic adaptation, a subsequent trial addresses a changed state. Divergent observations may refute assumed invariance, not the earlier historical observation. An identifying design might require unexposed units, randomized test exposure, measurement of carryover, or an explicit transition model. No design option is automatically available.

Perdomo and colleagues model prediction-induced distribution change through \(D(\theta)\), distinguish performance on the induced distribution from a retraining fixed point, and give conditional convergence results. Their “performative stability” is generally different from optimality. This is a precise precedent for one form of feedback, not a proof that all science is performative in that technical sense. [2020, Definitions 2.1/2.3, Example 2.2, Theorem 3.5](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf).

**Finite-resource constraint.** If available funds total \(B\), every check costs at least \(c>0\), and there are no later inputs or credit, feasible check count satisfies \(N\le\lfloor B/c\rfloor\). With dated inputs, each prefix expenditure must be financed at its payment time. These necessary accounting bounds do not identify the most informative allocation. If every duplicate has zero incremental information while an affordable alternative has positive net value, compulsory duplication is dominated under the declared loss.

## 7. Relationship to the existing framework and next test

The read-only README and CLAIMS distinguish information limits (U05/U22/U26), fresh validation (U15), financing (U16/U24/U25), and current testing versus preserved capacity (U17/U28). The recent snapshots on [renewal of inquiry](/Users/ren/theories/sources/15-codex-theory-conversations/2026-10-05-renewal-of-inquiry.md) and [recoverable inquiry](/Users/ren/theories/sources/15-codex-theory-conversations/2026-10-05-recoverable-inquiry.md) explicitly include controls where continued testing wastes resources. This memo strengthens the same distinction: preservation of a capacity can be useful even when using it now is not, and repetition need not create independent evidence.

NASEM likewise cautions that replication criteria differ, repeated significance is an unreliable criterion, and non-replication has multiple possible causes. These are consensus methodological judgments, not derivations from causal embeddedness. [2019, Chapter 5, pp. 73–75 and 85–90](https://www.nationalacademies.org/read/25303/chapter/8).

A concrete next synthetic test should compare, at equal total budget: repeated original-pipeline checks; fresh data with a shared calibration; one independent calibration plus fewer repeats; and a diversified pair of methods. Cross these with stationary versus test-altered systems and disclosed versus hidden selection history. Freeze the error-generation mechanisms and evaluation criterion before evaluating; report missed real defects, false alarms, decision loss, expense, and remaining correction capacity separately. Use separate evaluation seeds and retain no-error, common-error, and costly-test controls. The falsifiable model-specific prediction is that repeats reduce the idiosyncratic component but not the planted shared-error floor, while calibration diversification helps only when its cost and new errors do not outweigh that benefit.

Reject these stronger derivations: agreement proves truth; more critics always improve reliability; every scientific claim must permit exact physical repetition; public disclosure is always optimal or morally required; paid checking should continue forever; epistemic reliability determines legitimate interests. Whether real institutions satisfy the proposed error and resource models remains an empirical question.
