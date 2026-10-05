# Conditional scientific principles: formal research memo

5 October 2026. Working contribution to Ren's investigation. Status: elementary conditional derivations and checked synthetic examples, using established probability and decision theory; no originality or empirical-validation claim. External source descriptions are deliberately brief. The proofs below are independently written, not quotations or close paraphrases of the linked papers.

## 1. Answer and dependency structure

Scientific principles can be derived **relative to declared epistemic aims, accessible experiments, reliability criteria, and costs**. Causal embeddedness motivates including investigators, records, tests, and resource transitions in the model. It does not choose the goal, supply accurate observation kernels, or uniquely select a scientific method.

| Added premises | Mathematical consequence | Methodological interpretation | What does not follow |
|---|---|---|---|
| Two rival claims, a common observable protocol, binary discrimination objective | Sum of two error probabilities is at least one minus transcript total variation | Obtain information that distinguishes the claims | Universal falsification, certainty, or a mandatory experiment |
| Distinct normalized probability laws | Some events favor each law relative to the other | Predictions must have possible adverse evidential consequences | Every model must prohibit a finite observation |
| Reliable error control throughout data-dependent stopping | Fixed-time control alone is insufficient; explicit sequential constructions work | Include continuation and selection in the protocol | Stop only at a fixed sample size |
| Repeated true-null tests and lifetime familywise error goal | Summable valid error allocations suffice | Budget error across attempts | FWER is always the right scientific or ethical criterion |
| Binary forecast evaluated by expected squared error | The true conditional probability uniquely minimizes risk | Honest probability reporting is useful under this score | Calibration alone gives informativeness or causal truth |
| Possible future need for a currently excluded action/model, with performance required in that case | A policy that never admits it cannot meet that requirement | Preserve a feasible route to correction | Revise after every anomaly, or maintain inquiry forever |

Related source-register results are U05 (observation and intervention), U15 (fresh validation), U20–U22 (model-relative summaries, admission and information), U24–U28 (resource renewal and lifetime constraints). This memo strengthens exposition around them; it does not relabel them new discoveries.

## 2. Minimal account: complete protocols, not isolated observations

Let the world belong to a declared class \(\Theta\). A hypothesis is a subset of that class, or, in the simple case, a particular world model \(\theta\). At time \(t\), the investigator has history \(H_t\), chooses an available action \(A_t\), receives \(Y_t\), and changes resources and the system being studied. A policy \(\pi\) includes experiment choices, internal randomization, stopping, and reported decisions. The law \(P_\theta^\pi\) is the distribution of the **complete accessible transcript** under that common policy.

All conditioning must include accessible side channels: inherited records, ordinary outcomes, timestamps, actions, selection and silence. The model may include latent states and action-dependent dynamics. This permits causal participation and moving targets; stationarity is an additional assumption, not part of the notation. Conditional distributions must remain well defined even when testing affects later observations. The resource-feasible policy set \(\Pi_{B,T}\) may require every expense to be paid before its result arrives, with deadline \(T\) and budget \(B\).

The structural signature \(S=(X,T,R,O)\) can describe which configurations, transformations, enabling conditions and distinctions the protocol admits. It does not, by itself, determine the probability laws, objectives, or losses used below.

Distinguish these terms:

- **Logical refutability:** a claim plus auxiliaries entails a restriction contradicted by an accepted observation. A contradiction refutes that conjunction; it does not identify the failing conjunct.
- **Statistical testability:** a specified protocol discriminates claims with declared errors or provides model-relative evidence. This does not require probability-zero outcomes.
- **Identifiability:** distinct target values imply distinct distributions over the specified observational or interventional family. This is a property of a model and access regime, not finite-sample certainty.
- **Practical testability:** a sufficiently informative protocol belongs to \(\Pi_{B,T}\). Identifiability may hold in an ideal experiment unavailable here.

For composite hypotheses, overlapping transcript distributions can defeat uniform discrimination even though many individual pairs are distinguishable. Pairwise identifiability also does not imply a uniform finite-sample accuracy bound over an arbitrarily close collection of models.

## 3. The discrimination necessity and a resource corollary

**F1 — transcript discrimination.** Take two simple hypotheses with laws \(P_0,P_1\) on the same transcript space. Let \(\varphi(H)\in[0,1]\) be the probability of reporting hypothesis 1. Set \(\alpha=E_0\varphi\) and \(\beta=E_1(1-\varphi)\). Then

\[
\alpha+\beta\ge 1-\operatorname{TV}(P_0,P_1).
\]

**Proof.** For any bounded test, \(E_1\varphi-E_0\varphi\le\operatorname{TV}(P_0,P_1)\), by expressing \(\varphi\) as the integral of indicators of its upper-level sets. Rearranging gives the result. In a finite space, choosing hypothesis 1 exactly where \(p_1>p_0\) achieves equality. Equal-prior, equal-cost minimum misclassification risk is therefore \((1-\mathrm{TV})/2\). Different losses or priors change the optimal test; they do not erase observational equivalence.

If every feasible policy gives \(P_0^\pi=P_1^\pi\), no investigator using those policies can have both errors below one-half. Extra recursive self-modeling is still a function of its accessible transcript and randomization. It cannot create the missing distinction. This is a limitation on an information interface, not proof that the claims are meaningless or forever indistinguishable.

**F2 — elementary finite resource bound.** Suppose initial transcripts agree in distribution, at most \(N\) observations are possible, and at every common history and common action the two next-observation kernels have TV at most \(\varepsilon\). In a finite model, couple the policies' randomization and maximally couple their next observations whenever the histories still agree. Their histories remain equal with probability at least \((1-\varepsilon)^N\). Hence

\[
\mathrm{TV}(P_0^\pi,P_1^\pi)\le1-(1-\varepsilon)^N,
\qquad \alpha+\beta\ge(1-\varepsilon)^N.
\]

If each observation requires at least \(c>0\) from a total nonreplenished budget \(B\), then \(N\le\lfloor B/c\rfloor\). The bound is usually loose but gives a necessary information-and-cost condition. It fails if supposedly free passive observations or inherited information were omitted, if the kernel bound fails after intervention, or if replenishment permits more observations. The existing U26 gives a sharper KL-based formulation with explicitly bounded conditional information.

**Checked instance.** The script enumerates 35 probability laws on four outcomes and all 16 deterministic tests for every ordered pair: 19,600 exact rational checks verify F1 and its optimum. Randomized tests are convex combinations of deterministic tests, so enumeration plus the proof covers them too. Computational agreement verifies these instances; the proof supplies the general statement.

## 4. Possible adverse evidence without logical falsification

**F3 — discrimination entails possible relative adversity.** If \(P\ne Q\), some event \(A\) satisfies \(Q(A)>P(A)\). Its complement satisfies \(Q(A^c)<P(A^c)\). Thus neither normalized law assigns at least as much probability to every event with a strict advantage somewhere. For finite positive mass functions, there are outcomes with \(q/p>1\) and outcomes with \(q/p<1\): observing either changes positive prior odds in opposite directions.

**Support qualification.** If supports differ, likelihood ratios can be zero or infinite; one cannot insist that both directions occur with positive probability under each hypothesis. Under \(Q\ll P\), \(E_P[dQ/dP]=1\); if the laws differ, the likelihood ratio has positive \(P\)-probability above and below one. Without absolute continuity that expectation argument must be revised. The event/complement statement remains valid. Probability zero in a continuous model is also not automatically logical impossibility: every exact point can have probability zero.

This supports a conditional methodological requirement: an investigator claiming evidence-based preference among distinguishable predictive accounts must specify what observations alter that preference and by which rule. It does not require every observation to discriminate, a uniquely privileged alternative, or a posterior decrease sufficient to reverse a decision. An unrestricted after-the-fact story that claims credit for every result has supplied no fixed predictive comparison.

**Worked stochastic example.** Let twenty independent flips have probability \(p=.5\) under \(H_0\) and \(p=.8\) under \(H_1\). Every finite binary sequence has positive probability under both. Rejecting \(H_0\) at fifteen or more heads has Type I error **.020694733** and power **.804207785**. The count likelihood ratio is \(1.6^k .4^{20-k}\). Both support and adverse evidence exist without any finite logical refuter. The transcript TV is **.855648337**, so optimal equal-prior classification error is **.072175831**. The level-.05 rule and equal-prior optimal classifier solve different objectives. Failure to reject is not proof of \(H_0\).

The likelihood-test tradition is represented by Neyman and Pearson (1933), *On the Problem of the Most Efficient Tests of Statistical Hypotheses*, DOI [10.1098/rsta.1933.0009](https://doi.org/10.1098/rsta.1933.0009). The original scan was located, but full-text retrieval failed in this pass; detailed historical interpretation is therefore deferred to the philosophy/literature contribution.

## 5. Optional stopping, repeated attempts, and adapting the test

**F4 — repeated opportunities change the error event.** If independent true-null attempts each falsely reject with probability exactly \(\alpha\), the probability of at least one false rejection among \(m\) attempts is \(1-(1-\alpha)^m\). At .05 and 100 attempts it is **.994079471**. Merely knowing errors are at most \(\alpha\) does not justify that equality, nor does arbitrary dependence.

For adaptively selected hypotheses, one sufficient lifetime FWER condition is conditional validity of each true-null test at a predictable allocation \(\alpha_j\), together with \(\sum_j\alpha_j\le\alpha\) almost surely. The tower property and union bound give probability at most \(\alpha\) of any false rejection. Independence is unnecessary under these stronger conditional assumptions. For fixed predeclared tests on prefixes of one stream, marginal validity and deterministic allocations suffice for the ordinary union bound. FWER, expected false discoveries, FDR and expected harm are different targets.

**F5 — one sequentially valid construction.** Under a declared null, let \(p_t(y\mid H_{t-1})>0\) be the conditional mass function. Choose a normalized alternative forecast \(q_t\) before observing \(Y_t\), possibly using past data. Then

\[
M_t=\prod_{s=1}^t \frac{q_s(Y_s\mid H_{s-1})}{p_s(Y_s\mid H_{s-1})},\qquad M_0=1
\]

is a nonnegative null martingale because each conditional ratio has expectation one. For first threshold crossing \(\tau=\inf\{t:M_t\ge1/\alpha\}\), bounded stopping yields

\[
1=E_0 M_{\tau\wedge n}\ge \alpha^{-1}P_0(\tau\le n).
\]

Taking \(n\to\infty\) gives \(P_0(\sup_t M_t\ge1/\alpha)\le\alpha\). A nonnegative supermartingale suffices. The investigator may stop early, continue, or adapt future forecasts; choosing today's forecast after today's outcome breaks the displayed proof. Composite nulls require validity for every null distribution; substituting a fitted null in the denominator is not automatically valid.

Howard et al. (2020), *Time-uniform Chernoff bounds via nonnegative supermartingales*, develops the wider machinery and its relation to classical sequential methods: [DOI](https://doi.org/10.1214/18-PS321), [2020 version inspected](https://arxiv.org/pdf/1808.03204v7). Ramdas et al. (2023), *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, gives modern e-process and confidence-sequence formulations: [DOI](https://doi.org/10.1214/23-STS894). These support adaptation with appropriate guarantees, not a general prohibition on flexible research.

**Exact peeking check.** For iid Bernoulli(.5), inspect the ordinary one-sided exact binomial p-value at every \(n=1,\ldots,200\) and stop on p≤.05. Absorbing-path rational recursion gives false rejection **.244627302**. Using thresholds \(\alpha_n=.05/[n(n+1)]\) gives **.000489253**. The likelihood martingale against .8, threshold 20, gives **.036712796**. At the .8 alternative, their detection probabilities by 200 are approximately 1, .999997372 and .999998402 respectively. This selected strong-effect example does not establish a uniform efficiency ranking; the spending rule is notably conservative here.

Fresh validation is a simple way to make a selected candidate's test conditionally valid. It is not the sole way. Dwork et al. (2015), *Generalization in Adaptive Data Analysis and Holdout Reuse*, explicitly studies controlled reuse rather than declaring every reused observation invalid: [primary paper](https://arxiv.org/abs/1506.02629). Uncontrolled holdout feedback can make the holdout part of training. Shared drift, dependence, or postselection exclusions can also defeat the assumed fresh-data law.

## 6. Uncertainty and revision: what is actually forced

**F6 — probability reporting under a declared score.** Let \(Y\in\{0,1\}\) and \(p=P(Y=1\mid H)\). For a forecast \(q\), expected Brier loss is

\[
E[(Y-q)^2\mid H]=p(1-p)+(q-p)^2.
\]

Reporting \(p\) uniquely minimizes this conditional loss. This is an exact derivation from a supplied loss and true conditional law; it does not make the law known. Strictly proper scoring rules generalize this incentive property: Gneiting and Raftery (2007), *Strictly Proper Scoring Rules, Prediction, and Estimation*, [author-hosted primary text](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf), DOI 10.1198/016214506000001437.

Calibration requires specifying conditioning groups and time horizon. With \(q_t=E[Y_t\mid H_{t-1}]\), the residuals are bounded martingale differences. For any predetermined/predictable binary selection \(I_t\), selected residuals still have zero conditional expectation, yielding concentration or asymptotic frequency results under their respective conditions. A finite record does not certify exact calibration. Unconditional calibration is weak: forecasts of .5 for alternating known zeros and ones match the overall frequency but have Brier loss .25; forecasts using the pattern have loss zero. Calibration is not sharpness, explanatory adequacy, causal validity, or subgroup protection.

**Revisability is a conditional capacity requirement, not compulsory churn.** If the class admits future histories at which a different available conclusion or action is necessary to meet the specified performance standard, a procedure permanently forbidding that alternative cannot meet that standard on those histories. This is set exclusion. It does not show that the alternative will be discovered, recognized, financed, or legitimate. In a finite Bayesian family, zero prior mass stays zero after finite positive-likelihood updating; admitting a previously excluded model is a separate operation. A zero-density point in a continuous prior is not the same phenomenon.

Preserving more information weakly improves attainable decision performance **when costs, actions and physical transitions are held fixed**, because the decision-maker can ignore it. This simple inclusion argument belongs to the established comparison-of-experiments tradition: Blackwell (1953), *Equivalent Comparisons of Experiments*, [DOI](https://doi.org/10.1214/aoms/1177729032). Only abstract and bibliographic metadata were accessible in this pass. Paid or system-changing observation invalidates the free-inclusion comparison: with fair binary state, 0–1 action loss and perfect-test cost .6, acting without a test costs .5 while testing costs .6. Testing is informative and undesirable under that objective.

Finite resources also make continued correction a feasibility question. Records, attention, model admission and authority can deteriorate. Their necessary renewal follows only when future correction is required and depends on them. A stationary question can be resolved sufficiently for its purpose; constant inquiry can waste resources. Current model success cannot by itself certify the accuracy of a claim about all future tests, but this limitation does not prove a mandatory rate of skepticism.

## 7. Rejected derivations and next discriminating test

Reject: embeddedness ⇒ falsifiability as a complete demarcation criterion; normalization ⇒ all observations can logically falsify; individual identifiability ⇒ affordable accurate discrimination; low p-value ⇒ the named mechanism rather than an auxiliary failed; Bayesian updating ⇒ automatic model admission; unlimited validation attempts at .05 ⇒ lifetime .05 control; calibration ⇒ truth; optional stopping ⇒ inevitably invalid inference; inquiry renewal ⇒ inquiry is always worth funding; reliability ⇒ legitimate interests or rights.

The next formal test should combine an unknown change point, ordinary informative outcomes, paid diagnostics, and affordable suspension/reopening. Compare terminal-only, repeatedly reused fixed-time, spending, and sequentially valid procedures at matched pathwise budgets and declared decision losses. Cross measurement drift with substantive mechanism drift so that an alarm need not identify its target. Freeze the protocol before test instances; report false alarms, missed changes, delay, expenditures and harm separately. Include no-change, uninformative-sensor, unreachable-budget and shared-calibration-error controls. This could test the value of **maintained access to warranted revision**. It would not yet explain novel concept formation or the legitimate choice of objectives.

## Local provenance and reproducibility

Read-only reference workspace: `/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/README.md` and `CLAIMS.md`; relevant snapshots under `/Users/ren/theories/sources/15-codex-theory-conversations/`: `2026-10-05-questions-without-anomalies.md`, `2026-10-05-renewal-of-inquiry.md`; and the research memo `recoverable-inquiry-math.md`. No source-workspace files were changed.

Verification: `work/formal/checks.py` and `work/formal/results.json` in this task. Script uses Python standard-library exact fractions for probability calculations and prints decimals only for reporting. Tested laws, stopping boundaries and selection horizon are explicit in code. These are synthetic calculations and analytical checks, not empirical replications.
