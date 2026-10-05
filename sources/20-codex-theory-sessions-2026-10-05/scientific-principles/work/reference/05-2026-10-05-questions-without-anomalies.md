# Questions without anomalies: preserving a route to revision

5 October 2026. Seventh continuation of Ren's research into selection and the conditions for continued becoming. Immediate request: “continue the next frontier please.” This is AI-generated research assistance with three agents auditing mathematics, implementation, and primary literature. Exact conditional results, exploratory finite calculations, institutional hypotheses, and ethical commitments remain distinct.

The preceding cycle established that evidence can remain historically true while its relevance to present action changes. This cycle asks what an institution should preserve **before knowing which later question will matter**, and what permits a question to receive investigation.

The strongest finding is an information constraint: **a useful question need not announce itself as an anomaly in the records a system currently uses.** Requiring such an anomaly before financing investigation can exclude a useful change, even with truthful records, unlimited computation, and shared purposes. A new observation channel can remove this limitation; keeping more of the same information cannot.

## 1. The general constraint

Let D denote everything a gate may inspect, including public cues, retained records, and permitted past outcomes. Let g(D) in [0,1] be its probability of admitting an investigation; this includes randomized gates. For two worlds E and U,

\[
\left|\Pr_U(\mathrm{admit})-\Pr_E(\mathrm{admit})\right|
\le \operatorname{TV}(P_U^D,P_E^D).
\]

This is the standard total-variation bound on bounded tests. Integrating g against the two probability laws proves it; equivalently, write g as an integral of its level sets. If the entire available record has the same law in the two worlds, every gate based on that record has the same admission probability. A gate admitting at most alpha in E can admit at most alpha in U, however useful the proposed change is in U.

The constraint is independent of whether the implementation is human or computational. Its content depends on specifying the actual observation interface. It does not say that all further investigation is impossible. It says that a procedure cannot extract a distinction its available observations do not identify. Additional information in actions, silence, linked outcomes, or people’s testimony must be included rather than silently erased.

This is an application of established statistical identification, not a new mathematical discovery. The research contribution here is to connect that limit to the financing and admission of revision, with a paid counterexample that can be inspected and reproduced.

## 2. Four worlds expose four different questions

Each independent historical window has four binary switch indicators B, their total K, and a public fair endpoint Z. Every world has exactly K~Binomial(4,1/4), and every switch position has marginal probability 1/4. When K=2, the two clustered arrangements 0011 and 1100 together have probability q; the remaining four arrangements share 1-q. Other counts have uniformly arranged switches.

Let d be the number of switches in the latter half minus those in the first half. The supplied policy candidate uses this ordering to decide whether to add a response when Z=0. The response costs .3 and prevents a unit loss when need arises. Its effectiveness is assumed known. The usual policy responds only when Z=1.

| World | Historical order | Next-switch probability | Candidate useful after ongoing record cost? |
|---|---|---|---|
| E | Exchangeable, q=1/3 | .25 in every context | No |
| P | Clustered, q=1 | .45 for d>0, .05 for d<0, .25 otherwise | Yes |
| T | Clustered, q=1 | .25 in every context | No |
| U | Exchangeable, q=1/3 | .45 for d>0, .05 for d<0, .25 otherwise | Yes |

For Z=0, next need probability equals the next-switch probability; for Z=1 it equals one minus that probability. Every world gives the usual policy the same .275 expected operating loss. More strongly, every world has the same complete joint law of routine records (K,Z,Y), where Y is one subsequent need outcome per independent window. Symmetry between positive and negative d hides the interaction when order is discarded.

E and U have identical laws of the full four-switch window and endpoint. P and T also have identical historical laws. Therefore an archive of those windows can reveal clustering but cannot determine whether ordering matters for the later response. Even a perfect historical audit cannot separate E from U or P from T.

“Full historical window” has a precise boundary here. If the archive already linked each complete switch word to its subsequent Y, it would contain the validation evidence and these pairs would be distinguishable. Overlapping windows or repeated outcome labels could also change the observation experiment. The counterexample concerns the specified interface, not every imaginable history.

The four worlds distinguish preservation of a feature, detection of a historical pattern, evidence of its future relevance, and the value of acting on it. Neither detecting nor failing to detect clustering answers the policy question by itself.

## 3. Preservation is chosen before the later question

The institution prepays for m complete historical windows before observing their contents or learning which later question will be asked. Every procedure retains K and Z routinely. A later question Q asks either for a routine count-based answer or for the continuation decision above. Its probability of asking for continuation is lambda, independent of the world and records. Base lambda is .5; the calculation retains .01, .1, .25, .5, and 1.

When only the count question arrives, the extra ordering has no benefit, but its prepaid cost remains. This is genuine advance choice over two declared possible questions. It is not a model of inventing a question absent from the designer's language. The candidate response is likewise supplied; admission into active investigation is endogenous to the procedure, while unrestricted concept generation remains open.

Two procedures are compared. An **audit-first procedure** opens fresh validation only if its retained order rejects exchangeability. A **direct-validation procedure** can investigate the supplied candidate when the continuation question arrives without first requiring that historical rejection. Both require the same fresh test before adoption.

A more general rule investigates after a passed audit or, otherwise, an independent challenge with probability eta. If audit opening has probability A_w(m), its validation-opening probability is

\[
R_w(m,\eta)=A_w(m)+(1-A_w(m))\eta.
\]

This explicitly separates permission to investigate from permission to deploy.

## 4. Fresh validation and its price

The historical audit is a finite exact conditional test. Given J retained windows with K=2, the clustered count has Binomial(J,1/3) distribution under the null. Use its upper tail at level .05, with a fixed sample size and one evaluation. Under P/T, a rejection occurs exactly when at least three K=2 windows are present. Twenty-eight retained windows are the smallest quota giving at least .95 power against this specified alternative. Their opening probability in E/U is only .02897994.

When validation opens, it pays for all 1,024 fresh histories and their subsequent outcomes, including cases ineligible for the candidate response. Only Z=0,d>0 cases are eligible; eligibility is determined before their outcome. Every procedure follows the usual policy during the same reserved validation interval. This avoids granting immediate deployment to a procedure that merely skips the investigation. Because the usual policy leaves eligible cases untreated, their need outcomes are observable without treatment censoring.

The candidate's eligibility rate is

\[
\tau_q=\frac{120+54q}{1024}\ge\tau_{\min}=\frac{69}{512}.
\]

Using the candidate also costs f=.002 to collect and interpret ordering **per future decision**, including ineligible cases. Its net per-decision benefit is tau(p-.3)-f. Consequently the validation test uses the conservative threshold

\[
p_* = .3+f/\tau_{\min}=.3148405797\ldots.
\]

A nonbeneficial candidate satisfies p<=.3+f/tau<=p_*. A fixed binomial upper-tail test at .05 therefore controls false acceptance of nonpositive ongoing net benefit throughout the stated eligibility family. It does not establish that the investigation recovers its already incurred research costs, nor does it estimate an unknown treatment effect.

All acceptance probabilities are exact finite sums evaluated numerically. With 500 subsequent decisions, archive cost .02 per window, and validation cost .002 per screened window, the results are:

| World | Adoption: audit 28 first | Adoption: direct validation | Extra expected loss: audit 28 | Extra expected loss: direct |
|---|---:|---:|---:|---:|
| E | .00075% | .02577% | +.58969 | +1.02456 |
| P | 92.867% | 97.417% | −3.91704 | −4.69637 |
| T | .01133% | .01188% | +1.53648 | +1.02431 |
| U | **2.719%** | **93.838%** | **+.46584** | **−3.24909** |

Adoption is conditional on receiving the continuation question. Expected losses include lambda=.5, all inquiry expenses, future ordering costs, and the change in operating loss; negative means improvement over no inquiry. These figures describe the supplied artificial worlds, not estimated frequencies in institutions or AI deployments. The audit-28 example is a power-targeted illustration, not the optimal quota for every prior.

The two main counterexamples point in opposite directions. T passes the historical audit often but almost never passes the useful-action test. U rarely gets permission to take that test, even though the test would usually identify a beneficial action. Low historical anomaly and low future usefulness are different propositions.

## 5. Keeping records competes with financing new experience

Let V_w be fresh validation power, Delta_w=tau_w(p_w-.3) gross operating benefit, L the validation cohort, H the future decisions, c_a archive expense, and c_v validation expense. Exact incremental loss is

\[
C_w(m,\eta)=mc_a+\lambda R_w(m,\eta)
\left[Lc_v+V_wH(f-\Delta_w)\right].
\]

Every probability product is computed conditional on world before averaging over a designer's prior. Audit retention is prepaid even if the later question does not need it. Validation is paid whenever it opens, including when it fails. Ordering is paid throughout adopted deployment. Each feasible workflow also satisfies a conservative hard expense cap on every branch; equal caps do not imply equal spending.

For a fixed prior this expression is affine in eta, so an endpoint eta=0 or eta=1 minimizes expected loss. If eta=1, audit retention adds expense without affecting admission: m=0 direct validation dominates positive quotas. Interior challenge probabilities require a different constraint, a tie, or a robust criterion to be strictly preferred. The benchmark therefore compares no inquiry, every feasible audit-first quota from 1 to 128, and direct validation.

Across 286 explicitly enumerated priors with probabilities in tenths over the four worlds, at base prices and lambda=.5, direct validation wins in 233, no inquiry in 49, and audit-first in four. These counts summarize a chosen grid, not a probability distribution over real institutions. The four audit-favoring priors put zero probability on U. Cheaper storage and greater likelihood of needing the later question enlarge the audit-favoring region. With no possibility of that question, prepaid ordering has no benefit. Shorter deployment horizons and expensive inquiry also reduce its value.

Under finite-world minimax regret, an ex ante lottery over feasible workflows attains worst regret .841001, versus 1.024563 for the best deterministic workflow. The lottery is approximately 82.074% direct, 17.896% no inquiry, and .030% audit-16. The tiny audit weight reflects the exact artificial payoffs and has no general institutional significance. Each world's best **same-class workflow** supplies the regret comparator; low regret under a cap can mean that every workflow is prevented from investigating. It cannot be read as low absolute harm or robust alignment.

Preservation is one way to retain a route to learning. Fresh experience, affordable interpretation, and standing to request a test can matter more. A universal demand to retain all information does not follow.

## 6. What this contributes to the larger theory

The earlier principle concerned renewing the functions that continuing activity consumes. This cycle identifies an epistemic case: the capacity to change an institution's conclusions may depend on opportunities whose value its current records cannot establish. A current-score rule that retains only K chooses no paid ordering because ordering has no value for its admitted count task. If that institution also requires an order anomaly before buying fresh evidence, no inquiry is invariant under the stipulated rules. The example does not establish an attracting social dynamic or explain how those rules reproduce themselves.

For alignment, the resulting research requirement is precise and conditional: **an evaluation process intended to catch failures outside its present distinctions needs a feasible way to change those distinctions or collect different evidence.** Calibration and success within the old interface do not certify its adequacy. This applies to human and AI procedures through their information structure, without identifying markets, evolution, and backpropagation as literally one algorithm.

The mathematics cannot decide who has standing to raise a question, whose harms enter the loss, which inquiry risks are acceptable, or whether an intervention is legitimate. Here those are supplied common commitments. Protecting affected people's agency and the ability to contest evaluative rules remains an explicit normative commitment. Testing unfamiliar questions need not entail adopting their proposed interventions.

## 7. Prior art and verification

The building blocks have close precedents. The [information bottleneck method](https://arxiv.org/abs/physics/0004057) makes compression relative to a specified relevance variable explicit. [Information-directed sampling](https://arxiv.org/abs/1403.5556) studies acquisition for future decision value. [Posterior predictive model assessment](https://sites.stat.columbia.edu/gelman/research/published/A6n41.pdf) examines discrepancies a fitted model can miss. [Exact permutation testing](https://link.springer.com/article/10.1007/s11749-017-0571-1) supplies the relevant null-invariance foundation. [Selective inference](https://arxiv.org/abs/1410.2597) distinguishes valid testing of selected questions from naive reuse of the selecting data. The present computation uses fixed independent audit and validation cohorts; no optional-stopping or general selective-inference guarantee is silently assumed.

The central identification argument also has a close relative in Ben-David and colleagues' [Impossibility Theorems for Domain Adaptation](https://proceedings.mlr.press/v9/david10a.html): tasks indistinguishable from available training observations can respond differently to adaptation. Their source/target learning setting differs from this institutional admission procedure; the shared principle is the limit imposed by missing target-relevant information.

The [experiment](../../experiments/prospective-revision/README.md) preserves protocol, code, all priors and workflows, six boundary controls, thirteen one-parameter controls, all results, source hashes, and an inspected figure. Six tests pass. Independent elementary probability and branch enumeration agrees with reported calculations within 5.3e−14. The minimax primal and dual agree within 2.7e−15. These are verification of a conditional calculation, not empirical or human peer validation.

The [mathematical memo](../../_process/research/2026-10-04-integrated-evolution/prospective-revision-math.md), [implementation review](../../_process/research/2026-10-04-integrated-evolution/prospective-revision-design-review.md), and [prior-art audit](../../_process/research/2026-10-04-integrated-evolution/prospective-revision-prior-art.md) retain derivations and scope corrections. In particular, the discarded gross-benefit-only validation threshold is recorded: acceptance must account for the ongoing record expense. A generic baseline-reporting expression was also corrected to track a changed response cost; all saved baseline-world results remain unchanged.

## 8. Next frontier

The present institution receives its alternative question from a supplied grammar and its inquiry funds from an outside budget. Next, make **the production of questions and the renewal of their right to be investigated** part of the dynamics. Give differently situated participants different observations; let consequential experience generate proposals; and let the current evaluation rule determine replenishment of inquiry resources. Compare a protected route to fresh testing with one that must first earn justification under the incumbent representation. Include false proposals, cost, capture, and harm from investigation itself.

The target is a condition under which a system can sustain warranted revision without making the incumbent account the sole judge of whether another account deserves to be heard. Demonstrating that mechanism would connect this information constraint back to selection and paid renewal. Repeated succession, changing purposes, productive resource regeneration, and empirical cross-domain validation remain open.
