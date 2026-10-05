# Revision audit: changing a paid evaluator before renewal becomes impossible

Research audit, 5 October 2026. This cycle implements an actual observation-and-revision mechanism acting on a funded population process. Its target is narrower than the general idea of feedback-driven self-modification, adaptive control, or learning. Those ideas have substantial prior art. The useful question is whether the installed revision mechanism obtains usable evidence and completes a paid change while the successor population can still be financed.

## Three focused primary sources

**Feldbaum: probing, acting, and changing a controller.** The original paper distinguishes control actions that obtain information from actions that direct the plant, and discusses the tradeoff between acting prematurely and waiting too long. Its Figure 4(c) explicitly considers a higher controller changing the algorithm of a lower controller from observed consequences. Thus feedback-driven revision of a controller is already present. Part I formulates a finite-horizon Bayesian problem with supplied priors and loss, initially a memoryless plant; it does not establish treasury solvency or recovery after an unmodeled regime change. [A. A. Feldbaum, 1960, *Dual Control Theory I*](https://m.mathnet.ru/php/archive.phtml?jrnid=at&option_lang=eng&paperid=12624&wshow=paper), Avtomatika i Telemekhanika 21(9), 1240–1249. Access: full original Russian PDF retrieved and text inspected, especially pp.1244–1247; the archive also supplies an English abstract. The later parts' proofs were not inspected.

**Banerjee and Veeravalli: pay for observation and choose when to detect.** Their Bayesian change-detection formulation jointly chooses whether to observe and when to declare a change, balancing delay against false alarms and an expected pre-change observation count. The setting supplies pre/post observation densities and a geometric change-time prior. A posterior statistic determines observation and stopping choices. The two-threshold proposal is asymptotically optimal as false-alarm probability tends to zero; the paper explicitly exhibits finite-parameter cases where that form is not optimal. An expected sample-count constraint is not a pathwise cash constraint, and declaring a change does not pay for institutional repair. [Taposh Banerjee and Venugopal V. Veeravalli, 2012, *Data-Efficient Quickest Change Detection with On-Off Observation Control*](https://arxiv.org/pdf/1105.1361), Sequential Analysis 31(1), 40–77, DOI 10.1080/07474946.2012.651981. Access: full author preprint inspected for §II's formulation and posterior recursion, the finite-parameter qualification, and Theorem 7's asymptotic statement; asymptotic proofs not independently re-proved.

**Berkenkamp and colleagues: safe learning requires a supported safety certificate.** Their control method learns dynamics and updates policies while certifying a region of attraction. It starts from a locally safe policy and assumes Lipschitz regularity and uncertainty bounds that jointly cover the true dynamics with high probability. The exploration theorem adds Gaussian-process/RKHS and reachability conditions. These are meaningful guarantees under stated assumptions, not protection against an arbitrary change outside those bounds. A previously certified backup need not remain safe after such a change. The paper does not provide the current population treasury or revision-cost model. [Felix Berkenkamp, Matteo Turchetta, Angela P. Schoellig, and Andreas Krause, 2017, *Safe Model-based Reinforcement Learning with Stability Guarantees*](https://arxiv.org/pdf/1705.08551), NeurIPS 30. Access: full author preprint inspected, especially Assumptions 1–2, initial safe policy, Theorems 2–4, and the practical implementation caveats. No claim is imported that its guarantees survive miscalibration or model-class failure.

These three sources establish pertinent ingredients. The present work should make its own explicit transition and payment argument, without claiming that adding the word “revision” creates a new control architecture or solves safe adaptation in general.

## What exactly changes

The experiment should identify the object revised: a lookup table, posterior, ranking criterion, model parameter, program, or represented model class. Switching between two supplied decoders can be genuine revision of the installed evaluator. It is not, by itself, discovery of an unrepresented alternative or creation of a new explanatory vocabulary.

Represent the active process with its physical population, treasury, evaluator code, retained observation record, accessible program archive, clock, and relevant environmental state. The installed metarule must receive only its declared observations. The analyst's knowledge of the true environmental state must not enter the metarule through an unpriced argument.

Acquiring a signal, retaining it, authorizing an update, installing code, and producing a funded successor are separate transitions. Successful detection is not successful correction if the new code cannot be installed, the needed candidate program is gone, or the remaining cash cannot fund a successor. Conversely, a safe action can sometimes be chosen without identifying the environment. The target of the guarantee determines whether diagnosis is necessary.

## Independent calculation for the settlement-tariff experiment

The revised root design retains the previous S/L operating histories, with cash 100/136 and two/four diagnostic channels after two repair cycles. A settlement parameter changes from zero to 24 **after** those operating histories. The declared tariff pays a basic-plant credit of `(11/4)d` and charges `d` per auxiliary channel. Parent remittances become

\[
c_S(d)=100+(11/4)d-2d,\qquad c_L(d)=136+(11/4)d-4d.
\]

Thus post-change remittances are 118 for S and 106 for L. The changed environment reverses their remittance ranking without silently changing the already-executed operating programs. It is specifically a changed settlement contract with explicit outside credit and channel-charge flows. Those flows should not be renamed an unchanged physical plant law or hidden inside measured scores.

The supplied grant remains 150 per parent in both regimes; ordinary audit costs two per parent, the birth packet 260, site limit four, and treasury cap 259. Archive and evaluator-bit custody cost two per active epoch for the population as a whole. Before query or rewriting bills, the available pool is therefore

\[
F=R+148N+c_S(d)N_S+c_L(d)N_L-2.
\]

The custody fee is per population, unlike the grant and ordinary audit. That asymmetry is part of the scale mechanism and must remain visible.

For the bookkeeping potential `Φ=260N+R`, the replacement increments before spill and additional query/rewrite bills are:

| Environment | Pure S contribution | Pure L contribution |
|---|---:|---:|
| Tariff zero | `−12N−2` | `24N−2` |
| Tariff 24 | `6N−2` | `−6N−2` |

At the changed tariff, an initial two-L population with treasury zero becomes one L with treasury 246 after one stale epoch. Continuing without revision then loses eight treasury units per one-parent epoch. With the first changed epoch indexed by `j=1`, the treasury before epoch `j≥2` is

\[
R_j=262-8j
\]

as long as a stale L remains. At epoch 32, treasury six yields only 258 for a new packet, so this stale path ends.

The specified query costs 12, its retained report costs two, and rewriting costs 24. Query and report are paid before the late outcome; the report arrives after the parent closes. The corrected evaluator governs this epoch's newborn choice, not the already-completed parent behavior. In a one-L query-and-rewrite epoch the funds left for birth are

\[
R+254-2-14-24=R+214.
\]

One child can therefore be funded exactly when `R≥46`. Along the stale trajectory, this gives `j≤27`. Querying at epoch 27 funds one S with treasury zero; under the continuing grant and tariff, that S adds four per subsequent epoch after custody. At epoch 28, the same procedure learns the correct tariff but leaves only 252, below the newborn bill. This is a concrete case of accurate evidence arriving through a route that leaves insufficient resources to use it successfully.

These calculations independently audit the supplied design; the implementation audit below checks agreement. They do not certify every admissible metarule.

## Three distinctions essential to the interpretation

### A protocol deadline is not automatically the full recovery frontier

The epoch-27 cutoff belongs to the specified 14-unit observation plus 24-unit rewrite route. If a blind rewrite to the S-selecting decoder is permitted without that observation, it costs only 24. At epoch 28 it still leaves `38+252−24=266`, enough to fund S. Its cutoff along this path is epoch 28, since it requires treasury at least 32.

If the model forbids such a rewrite, that requires a real authority or execution precondition, not a restriction added only to make diagnosis necessary. Otherwise report the two frontiers separately. The state can lose the installed recovery route before it loses every possible recovery route.

### Neither fixed pure rule is a universal control for these regimes

Under the revised contract, pure S depletes before the change, while pure L depletes after it. This corrects the simpler design in which always selecting S would preserve the population in both regimes. It makes a no-change control against blind switching informative.

That does not prove that every possible successful policy needs diagnosis. Mixed cohorts, a supplied calendar allocator, a different initial reserve, or additional observable signals can change the answer. For example, under a supplied quota allocator with the same per-birth costs and custody bill, four carriers can alternate cohorts `(3S,1L)` and `(2S,2L)`. Pre-change potential increments alternate `−14,+22`; post-change they alternate `+10,−2`. Both complete two-epoch blocks gain eight. Starting in the first phase with treasury 16 also covers the worst single-change crossing, `−14−2`. This example requires a funded initial mixed cohort, an admitted clock/quota mechanism, and no additional unaccounted recurring switching bill. It is not a demonstrated route from the root's particular `(2L,R=0)` initial state. Its role is to show why the tariff pair alone does not prove information necessity across every population and policy class.

### One detected change is different from a permanently funded monitor

If the supplied environment admits only one irreversible zero-to-24 change, stopping queries after confirmation is legitimate and is part of the implemented mechanism. Repeated monitoring for future changes is a different task. A one-parent post-change S population produces only four treasury units per epoch after custody. A new 14-unit query every epoch would deplete it. For a simple periodic no-spill cycle, average spacing of at least four epochs is necessary to fund those continuing queries; prefix feasibility and rewriting expenses must also be checked.

The decision to gather information changes the resources available for later information and action. It is therefore insufficient to optimize expected detection delay and then assume the resulting monitor can keep running.

## Information and timing audit

The implemented interface gives the evaluator no direct access to treasury balances or late parent cash outside the paid query. That exclusion can define a legitimate institutional interface. It cannot be treated as universal: a treasurer with access to remittances could infer more, and an observed funded/refused action can itself reveal information. Include all such signals in the metarule's state before making an indistinguishability or information-necessity claim.

A publicly known deterministic change date also permits scheduled revision without change detection. When evaluating an unknown onset, specify what the metarule knows about its possible timing, which clock it can read, and whether the experiment's absolute date is visible. The realized change used for evaluation may be fixed by the analyst while remaining hidden from the controller, but those two roles must be kept separate.

The archive is necessary if earlier selection eliminated the program later preferred. Raising the score of an absent program does not recreate it. Its retained code, custody, read access, copy operation, and construction of a physical carrier require the declared support. Stored evaluator bits likewise need an update semantics: paying for a report does not by itself change the installed ranking.

The root's paid query reports the tariff regime perfectly after settlement. That is a supplied informative sensor, not a noisy sequential estimator of an unknown change law. The model therefore demonstrates paid detection and installation within a known two-contract family. The companion finite Bayesian example can study uncertain evidence separately; combining the two examples conceptually does not automatically produce an implemented noisy population monitor.

Average delay is insufficient for a pathwise survival claim. A detector may have excellent expected delay while occasionally requiring more observations than the treasury can support. The physical loss-of-recovery time also depends on monitoring costs; it is not a fixed deadline independent of the attempted diagnosis. Exact finite-state checking should include these shared dependencies.

## Discriminating tests

| Control | What it distinguishes |
|---|---|
| No environmental change, same paid monitor | False alarms, unnecessary rewriting, and monitoring expense |
| Always select S, and always select L, in both regimes | The changed contract's genuine reversal of the two pure-rule renewal margins |
| Blind or scheduled rewrite, if actually authorized | Paid diagnosis versus a cheaper supplied revision route |
| Query at epochs 27 and 28 | Correct evidence with a usable remaining budget versus correct evidence without a funded successor |
| Correct report but lost retained bit | Information obtained versus information physically available when copying occurs |
| Readable report but unavailable archive or rewrite authority | Epistemic success versus executable revision |
| Same full environment, give the evaluator treasury/remittance access | Restricted institutional observation versus a genuine impossibility for every observer |
| Stop after the single admissible change, then require recurring monitoring | A one-shot repair of calibration versus maintained adaptive capability |
| Change beyond the represented tariff family | Mode adaptation within a known model versus unsupported model revision |
| Safe finite closure or no remaining repair duty | Continued reproduction as a specified goal versus a permitted ending |

## Implementation audit

I inspected the [evaluator-revision implementation](verification/check_evaluator_revision.py) and its [saved results](verification/evaluator-revision-results.json). An independent reconstruction matched all 46,800 integer transition cases over population at most four, treasury from zero through 259, both regimes and installed model bits, and the three observation/retention choices. The reconstruction used the direct pool coefficients `248S+284L` before change and `266S+254L` afterward, subtracting custody, query, hold, and rewrite bills separately.

The implementation pays the channel charge before the 66-unit allowance. Both supplied parent profiles can pay that charge from their closing cash; the later credit is not silently borrowed. Query and report retention are prepaid from treasury, and a requested rewrite is paid before births. The global ledger includes external settlement credits, charges, plant operating receipts, and child cash transfers. Correct-but-too-late detection changes the installed model bit and still produces no child, as intended.

The missing-template control also has an explicit execution consequence: the revised decoder selects S, but without a retained S template or current S donor, it produces no child. The supplied rule has no fallback to L. This is failure of this installed mechanism, not a statement that every other controller has become physically impossible.

The periodic-monitor calculation uses more than a finite successful trajectory. Under every pre-change sequence of query/no-query choices, the initial population reaches the capped state `(4L,R=259,old model)` by epoch 25. Before this endpoint, the exact bound is `Φ′≥min(Φ+32,1299)`; the final increase into the cap can be less than 32. The finite reachable-set calculation checks 468 edges establishing the common endpoint. Subsequent onset times reduce to the monitor's clock-phase classes. Together with the earlier onset cases, this yields an all-onset guarantee for each supplied query period from one through 27. For any period at least 28, change in the first epoch is already a counterexample. Monitoring stops after the one admissible irreversible change is confirmed; post-change S nonemptiness then follows from its separate invariant.

The saved erased-report control fails with the old model still installed, while the no-change blind-switch control eventually depletes under S. These outcomes discriminate retained, executable evidence from merely paying an inspection bill or committing to an unverified new ranking.

The quota control has a closed four-part invariant. Before change, the three-S phase requires treasury at least 16 and the two-S phase at least two. After change, the corresponding guards are zero and two. Both unchanged and newly changed transitions preserve the next guard, and cap 259 preserves these lower bounds. The root's exhaustive certificate contains 1,020 invariant states and 1,522 edges. I independently reconstructed all 1,522 edges after the final correction and verified their next guards, ledger balance, and mixed successor labels. The quota assignment occurs inside the paid copying operation; it is not an additional free relabeling of completed newborns.

I inspected the completed [evaluator-revision memo](evaluator-revision.md) and [cycle synthesis](synthesis.md). The route-specific thresholds, all-onset periodic guarantee, archive limitation, changed initial conditions for the quota control, and perfect-inspector scope match the inspected model. The synthesis distinguishes the separate noisy-evidence experiment from the population's perfect inspection. No substantive mathematical issue was found. Both requested corrections are applied: capped potential growth is explicit, and quota records identify the actual paid mixed successor cohort.

## Scope

The three source statements above have been checked against primary texts. The revised tariff arithmetic and recovery-route thresholds are independently derived; code agreement checks the declared finite model rather than establishing empirical applicability.

The result sought is conditional and constructive: this actual, paid revision procedure can repair a supplied evaluator under a declared environmental change when enough time, retained information, authority, archived code, and finance remain. It does not imply that successful systems must discover the right evaluator, that every regime can be safely identified, or that persistence supplies an ethical objective.
