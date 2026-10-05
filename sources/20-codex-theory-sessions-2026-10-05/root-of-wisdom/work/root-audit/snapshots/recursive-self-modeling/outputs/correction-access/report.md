# Keeping correction possible when a model is wrong

Research continuation for Ren, 5 October 2026. This completes the next experiment proposed in [the previous report](../experiment/report.md), using fresh development and evaluation data.

**Protecting access to evidence works as a limited guarantee, but does not guarantee better decisions.** Periodic checks ensure that every tested hidden change is followed by a reference sample. They improve average full-horizon loss in episodes containing a change, yet slow initial calibration and worsen performance when the bias stays constant. Surprise-triggered checks are faster when they still have budget, but sometimes spend their entire allowance before the change. Combining both mechanisms does not produce a clearly better average result.

A separate result makes the limitation sharper. A richer estimator that learns the reference's own bias performs very well when its assumed dynamics are correct. Under unmodeled constant forcing, it instead learns a misleading interpretation of both sensors. Its nominal 90% forecast intervals then cover only about **2.5%** of outcomes, despite receiving all six scheduled references.

The resulting distinction is between **access to evidence, discrimination of a relevant error, and effective revision**. These are separate properties of the implemented process. Another reflective level does not establish any of them by its name.

## What was tested

The controlled system is

\[
x_{t+1}=.8x_t+u_t+g+w_t,\qquad
 y_t=x_t+b_t+\epsilon_t,\qquad z_t=x_t+d+\eta_t.
\]

There are 60 steps, initial x∼N(0,1), ordinary bias b initially ±1 with equal probability, and independent noise standard deviations .05, .25 and .05 for w, ε and η. Every controller uses u=clip(−.5 x_hat,−2,2). References are available at steps 0,5,…,55; each policy may buy at most six.

Eight worlds cross three factors: constant ordinary bias or one sign reversal; physical forcing g=0 or a hidden ±.15; and reference bias d=0 or ±.25. Nonzero forcing and reference bias are constant, with independent random signs. Change times are uniformly drawn integers from 8 through 47, hidden from the policies. A ninth, descriptive control has no bias or forcing at all.

All policies assume g=0. The four primary scalar policies additionally treat the reference as unbiased. Thus the forcing worlds test a specifically incorrect model assumption, not a model that represents uncertainty about g. The richer benchmark estimates d but also incorrectly fixes g=0 in those worlds.

The loss is

\[
L=\sum_{t=0}^{59}(x_{t+1}^{2}+.05u_t^{2})+.02N_{reference}.
\]

Computation has no price or physical delay in this continuation. The outcome measures control and sensing under free computation. It is not directly interchangeable with the earlier study's work-priced loss, and does not establish cognitive or energy efficiency. Monitoring counts and complete simulation timings are retained.

## Four access policies, one correction rule

The four scalar policies share the same estimate h, uncertainty calculation, residual audit, and controller. After a paid reference, they update h toward y−z. The gain is .2 unless the residual exceeds two modeled standard deviations, when it becomes 1. The state estimate is y−h. Thus h estimates **b−d**; calling it an estimate of absolute b assumes d=0.

| Policy | How it obtains references |
|---|---|
| Confidence gate | Buys when a heuristic immediate variance-reduction value exceeds the reference price, provided budget remains. |
| Surprise gate | Buys initially, then when an ordinary-observation mismatch exceeds its threshold. A mismatch between purchase opportunities remains latched until the next opportunity. |
| Periodic checks | Buys at 0,10,20,35,45,55, regardless of current confidence. |
| Protected + surprise | Reserves purchases at 0,25,55 and allows at most three additional surprise-triggered purchases. |

“Surprise” uses the mismatch

\[
r_t=y_t-.8y_{t-1}-u_{t-1}-.2h_{t^-}.
\]

It is computed before the current reference update, standardized by a declared approximate variance, and monitored at all 59 later steps. The rule clears its latch at every purchase opportunity, even when it declines. It never reads a reference before choosing to buy. This score can reveal model mismatch, but does not uniquely identify its cause: forcing also enters it.

The common correction gains come from the previous study; the initial uncertainty is adjusted to the new ±1 bias distribution. Development selects the surprise thresholds from 1.5,2,2.5,3,3.5. Both select 1.5, the lowest tested value. This is a finite candidate comparison, not an optimized solution over all possible gates or thresholds. Schedules are fixed examples, not optimal schedules for the chosen change-time distribution.

The descriptive benchmark jointly estimates x,b,d with a three-state Gaussian moment filter and the same six periodic purchases. Its assumed bias process variance, selected from 0,.0025,.04, is .04. It differs in inference as well as retained state, so its comparison with scalar correction does not isolate an access-policy effect. Its Gaussian priors and process model are approximations, including a supplied reference-bias prior variance .0625; they are not the exact generating distribution.

## Fresh evaluation and main comparisons

Development uses seeds 20000–20199, and evaluation uses 30000–31999. Shared exogenous draws pair policies and worlds; actions still change their actual observation values. Code, protocol and selected settings were hashed before evaluation. This is a local freeze, not an external preregistration. The earlier evaluation remains separate.

There are 90,000 evaluated episodes across nine worlds and five policies. The independent unit is one of **2,000 seeds**, not a time step or a world-policy episode. Six primary comparisons average the four change worlds within each seed, or separately average the four constant worlds, then compare each alternative with confidence. Normal-approximation intervals are adjusted together by Bonferroni for familywise 95% coverage. The practical margin is .02 loss units.

| Condition | Alternative minus confidence | Mean difference | Adjusted interval |
|---|---|---:|---:|
| Constant bias | Surprise gate | +2.718 | [+2.505, +2.931] |
| Constant bias | Periodic checks | +3.044 | [+2.902, +3.187] |
| Constant bias | Protected + surprise | +2.285 | [+2.100, +2.469] |
| Hidden change | Surprise gate | -3.209 | [-4.113, -2.306] |
| Hidden change | Periodic checks | -2.571 | [-3.533, -1.609] |
| Hidden change | Protected + surprise | -0.838 | [-1.802, +0.125] |


Surprise and periodic checking both improve the change mixture beyond the margin. The hybrid's change interval crosses zero, so its benefit remains unresolved. All three alternatives worsen the constant-bias mixture beyond the margin. These are average effects under the supplied, equal-weight mixture of forcing and reference-bias conditions.

| Policy | Mean loss, constant bias | Mean loss, hidden change | Changes followed by a sample | Capped mean sample delay |
|---|---:|---:|---:|---:|
| Confidence gate | 8.992 | 21.799 | 71.03% | 8.82 |
| Surprise gate | 11.710 | 18.590 | 83.61% | 4.90 |
| Periodic checks | 12.036 | 19.228 | 100.00% | 5.46 |
| Protected + surprise | 11.277 | 20.961 | 100.00% | 6.98 |


A sample arriving at the change step has delay zero. Missing samples are censored at the number of remaining steps; the sample fraction is reported separately. These delays measure **arrival**, not correct detection or successful correction.

![Loss and access to post-change evidence](gate-access-summary.png)

## Why surprise can be fast and still leave no route to correction

Whenever the surprise policy obtains a post-change reference in this evaluation, it arrives within four steps. The new ordinary-observation monitor and latch carry an off-grid discrepancy to the next purchase opportunity. But **16.39%** of change-world episodes receive no post-change reference at all. Every one of these misses occurs after the policy spends all six purchases before the change. A responsive trigger cannot spend an exhausted budget.

The confidence gate misses a later sample in **28.98%** of change-world episodes. Most of those misses also reflect early budget exhaustion; 60 of the 2,318 misses occur with budget still available. Some acquired samples arrive as late as 39 steps after the change. These are observed properties of the chosen heuristic, not necessary failures of probabilistic acquisition rules.

Periodic and hybrid checks reach every tested change because their reserved step-55 purchase remains available and all changes occur by step 47. Protection supplies a finite guarantee even when the trigger sees no reason to act. It does not establish perpetual vigilance: changes after the last available reference, cancelled opportunities, or an unlimited lifetime with a finite total budget require different provisions.

For this particular integer timing convention, periodic checks guarantee a first post-change sample within **14 steps**; the hybrid's protected schedule guarantees **29**. Both maxima occur in the evaluation. Additional discretionary checks can shorten a hybrid wait, but cannot remove the reserved terminal check. The schedules are not minimax over the restricted 8–47 change support.

## Why the same protection can hurt a stable world

The constant worlds start with an unknown ±1 sensor bias. They still require initial calibration. The confidence policy spends early: with no forcing or reference bias it averages about four purchases by step 15, versus 2.54 for surprise and hybrid and two for periodic. Since the common update initially learns slowly, moving purchases later prolongs the initial bias error.

This makes the cost of protection more specific than “extra checking is expensive.” Periodic and confidence use almost the same total number of references, yet their **timing** changes the time spent acting on a poorly calibrated estimate. The four constant worlds average 5.97 confidence purchases, 5.54 surprise purchases, six periodic purchases and 5.86 hybrid purchases. No-change acquisitions are not automatically wasteful or false alarms.

In the separate no-bias control, surprise generates 6.59 threshold-exceeding monitoring steps and buys 4.97 references on average; the hybrid produces 6.68 and buys 5.66. Those are no-change mismatch alarms, not tests with a declared statistical false-alarm rate. Their loss is about 1.59, compared with confidence's 1.63, so the constant-bias disadvantage does not extend uniformly to every no-change condition.

A post-evaluation reweighting illustrates why the expected frequency of change matters. For these frozen policies and the same within-condition world mix, the surprise policy's point estimate breaks even with confidence when the probability of a change is about .459; periodic breaks even near .542. These are descriptive crossings of two measured average costs, with no retuning. At a 50:50 mixture, both overall differences remain statistically unresolved by descriptive paired 95% intervals. Neither a protected schedule nor a reactive trigger is unconditionally best.

## A better estimator can be much worse under a wrong anchor

The full world results retain the important disagreements hidden by mixture averages:

| Bias behavior | Forcing | Reference bias | Confidence | Surprise | Periodic | Hybrid | Three-state |
|---|---|---|---:|---:|---:|---:|---:|
| Constant | Zero | Zero | 7.206 | 9.474 | 10.509 | 9.280 | 0.657 |
| Constant | Zero | ±.25 | 8.292 | 10.205 | 11.134 | 10.090 | 0.723 |
| Constant | Hidden ±.15 | Zero | 9.744 | 13.196 | 12.974 | 12.514 | 30.216 |
| Constant | Hidden ±.15 | ±.25 | 10.725 | 13.964 | 13.528 | 13.223 | 30.271 |
| Changes | Zero | Zero | 19.248 | 14.360 | 17.288 | 17.662 | 0.659 |
| Changes | Zero | ±.25 | 21.630 | 15.686 | 18.472 | 18.941 | 0.725 |
| Changes | Hidden ±.15 | Zero | 22.061 | 21.524 | 20.042 | 22.930 | 30.227 |
| Changes | Hidden ±.15 | ±.25 | 24.257 | 22.789 | 21.112 | 24.310 | 30.282 |
| None | Zero | Zero | 1.629 | 1.587 | 1.592 | 1.596 | 0.653 |


With correct g=0, the three-state estimator achieves loss around .66–.73 and learns enough about reference bias to retain roughly 90% coverage. With hidden nonzero forcing, its loss rises to about 30.2 and coverage collapses to 2.47–2.57%. The ordinary scalar estimator with the identical periodic acquisition schedule does substantially better in those forcing worlds. The reference packets are available; the failure is their interpretation under the fixed-zero-forcing assumption.

![The descriptive estimator benchmark depends on its dynamics anchor](anchor-benchmark-summary.png)

The earlier invariance proof explains a precise candidate mechanism. Define r=g/(1−a), and rewrite

\[
x'=x-r,\qquad b'=b+r,\qquad d'=d+r.
\]

Then the observation equations are unchanged and the transformed dynamics have g'=0. A model that allows both sensor biases to move while fixing g=0 can interpret observations in this displaced coordinate. If it tracks x' exactly, with no noise and inactive clipping, controlling toward x'=0 makes actual x tend toward r. For g=.15 and a=.8, r=.75. This is also the passive forcing equilibrium: the controller regulates deviations around a displaced zero, rather than necessarily creating the whole displacement.

This is an exact coordinate construction and a conditional equilibrium argument, not a theorem that the finite Gaussian filter always converges to that parameterization. The prespecified example, seed 30000, supports the mechanism: with true d=0 and g=.15, the final pre-action state is .683, the model estimates x=.012, and its estimated reference bias is .746. It has largely explained the discrepancy by moving its interpretation of the reference.

The sampled worlds have fixed generating priors and are not the unrestricted shift-closed class of the impossibility proof. The experiment shows misspecification in this chosen estimator; it does not prove every estimator must fail. A richer model that also represents forcing would be another experiment, with its own identification and prior-dependence questions.

## What the formal argument adds

The [formal note](formal-note.md) proves a small scheduling result. With N regularly spaced intervals to cover, B purchases after an initial boundary, and a required terminal sample, the maximum waiting gap is at least ceil(N/B). Balanced gaps attain the bound. A separately paid initial calibration consumes additional budget. The proof concerns a defined finite coverage problem, not an open-ended free guarantee.

It also constructs a confidently wrong model with an uninformative ordinary stream and an informative but unpurchased reference. Any computation using only that unchanged ordinary history inherits the same inability to distinguish the changed and unchanged worlds. An innovation gate cannot help when no innovation is observable. A clock or coverage constraint can preserve access without an alarm, but that still leaves two further conditions.

First, the evidence must discriminate the relevant alternatives. In the unanchored model allowing the common shift of x,b,d,g, even continuous reference access cannot identify absolute x. If two observationally identical states differ by c, at least one world's expected squared estimation error is at least c²/4. This lower bound comes from an exact squared-error identity. Known forcing, a justified reference, or a supplied initial prior can change the identification problem.

Second, the implementation must use the evidence effectively. A logged discrepancy can leave an estimate unchanged, and even perfect estimates can feed an unstable controller. The note states a conditional bounded-error control guarantee and its clipping limits. Access, discrimination and useful revision therefore cannot be collapsed into one “capacity to reflect.”

There is established work on choosing observations jointly with change detection. Banerjee and Veeravalli study the tradeoff among delay, false alarms and observations under declared change distributions. Their Bayesian rule can increase the probability of a change while sampling is off, because a change hazard remains active. A confidence-based policy therefore need not wait for a surprise before reopening access. Their model and guarantees are not those of our clipped controller, heuristic residual and six-purchase cap. [Banerjee and Veeravalli, 2012](https://vvv.ece.illinois.edu/papers/journal/bane-veer-sqa-2012.pdf)

## What this changes in the research argument

The original question concerned what constraints survive through recursive self-modeling. This continuation identifies a concrete one: **processing cannot recover distinctions that the permitted evidence never supplies**. Moving to another descriptive level does not bypass the acquisition budget, the observation symmetry, or the effect of a wrong dynamics assumption.

The constructive counterpart is conditional. A system can preserve opportunities for its current account to be challenged, including when that account presently feels no need for correction. But preserving those opportunities consumes resources and can delay other useful learning. Even when evidence arrives, the system may misattribute it to whichever parameters its model allows to change.

This suggests evaluating a self-modeling system by the actual routes through which an error can be encountered, distinguished and acted on, under stated costs and time horizons. It is a testable property of a process, not something secured by how many reflective levels its description contains. Turning that proposal into claims about lived introspection, consciousness, ethical legitimacy or changing purposes still needs additional arguments and evidence.

The next empirical frontier is to separate two improvements: **maintaining a reserve for evidence** and **representing uncertainty about the anchor itself**. A hazard-aware gate and a model that allows forcing as well as sensor bias would provide stronger comparisons. Their performance should be checked on new data and against alternative priors; this study has not run them.

## Verification and reproduction

All 18 filter and independent runner tests pass. The separate numerical audit independently replays all 72,000 scalar-policy episodes, verifies the reported intervals and all acquisition arrays, and checks noninterference from unpurchased reference values for all five policies on reserved test seed 40000, alongside code/dataflow review. It does not independently replay every three-state benchmark episode. Formal checks enumerate 4,095 finite schedules and verify the delay bounds and algebraic counterexamples. Neither these checks nor the simulation establish a claim about humans.

The [protocol](protocol.json), [results summary](results/summary.json), [post-evaluation diagnostics](results/diagnostics.json), [independent audit](independent-audit.txt), [formal checks](formal-checks.json), and [reproduction instructions](reproduction.md) preserve assumptions, failures and reproducibility. The readable [anchor mechanism note](anchor-mechanism.md) states the displaced-coordinate argument separately.
