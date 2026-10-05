# A minimal mechanism for the formation of scientific questions and concepts

Research contribution for the current continuation, 5 October 2026. This memo reads the existing investigation, research record, and supplied questions-without-anomalies snapshot. It proposes a bounded mechanism and checks one finite example. It does not establish a complete theory of science or unrestricted conceptual creativity.

## Main finding

The framework can go beyond evaluating supplied claims if it models the **construction and installation of new distinctions and inquiry procedures** as activities with observable inputs, executable operations, costs, and consequences. A useful minimal loop is:

**experience → candidate construction → question admission → method choice → fresh assessment → representation/method installation → changed experience and resources.**

Every arrow needs a transition rule. Writing this loop does not explain it. Below, the construction rule is generic table fitting on accessible fields; selection is penalized empirical performance; validation uses fresh observations; deployment pays ongoing measurement costs. These are supplied mechanisms whose consequences can be checked.

An especially useful result is that discovery need not correct a false old assertion. In the worked example, the old statement `P(Y=1)=1/2` remains exactly true. Discovery reveals a previously unrepresented conditional relationship. A theory of science needs to explain both **correction of errors and production of more discriminating knowledge**.

## Explicit premises and state

Let the investigator's state be `Z_t=(D_t, phi_t, Q_t, M_t, G_t, b_t, L_t)`. These terms denote retained records, installed representation, active questions, available methods, construction procedures, resources, and the presently used loss/evaluation rules. A surrounding causal environment supplies observations when specified acquisition actions are actually performed.

Necessary added premises are:

1. An epistemic or practical task: here, prediction under specified loss. Science has other tasks; this choice is not a derivation of their insignificance.
2. Raw measurement interfaces and their limitations. Physical accessibility differs from actual recording and from permission to compute on records.
3. A finite executable construction grammar. Examples are joining two fields, splitting a class by a measured predicate, fitting a conditional table, and composing existing measurement operations.
4. Search, storage, measurement, and deployment costs, with payment deadlines.
5. A procedure for selecting generated candidates; its estimates can be wrong.
6. An assessment protocol accounting for data reuse. The example uses a fresh fixed validation batch.
7. A resource-replenishment rule if inquiry is to continue. The finite calculation supplies a budget rather than deriving its renewal.
8. An external evaluation criterion for the researcher's model of the investigator. The investigator does not receive that evaluator's true world identity, optimal concept, or true risks.

These premises make the account non-oracular. They also establish its limits. A prior or grammar is inductive structure, not a neutral consequence of causal embeddedness.

## What is formed endogenously?

A candidate question is a constructed record `q=(target, proposed distinction, comparison, feasible assessment, possible downstream use)`. For example, a generic join operation creates the question whether predictions improve when two measured fields are considered jointly. Experience supplies the entries in a fitted table. The field combination, fitted map, and question's priority need not be installed or actively considered before that computation.

There are three distinct senses of novelty:

| Sense | What this model explains |
|---|---|
| Newly active question | A candidate is constructed and admitted to a resource-bearing inquiry queue |
| Newly installed concept/method | A computed mapping or composed procedure becomes available for routine prediction, measurement, or future search |
| A primitive beyond every available construction and acquisition operation | Not explained by this finite model |

The full closure of a grammar is not the same as an investigator's current representation. An astronomically large program space may contain a useful function that no available researcher has constructed, interpreted, or financed. At the mathematical level this remains search in a supplied space. At the process level it can be a real change in what the agent can ask and do. We should preserve both descriptions instead of calling bounded construction either unrestricted invention or mere selection from already active concepts.

Methods can be formed in the same bounded sense: compose an acquisition, calibration, intervention, recording, and analysis routine, check that each step is feasible, and assess the procedure's performance. No grammar guarantees that the needed instrument or intervention can be built. If the only admissible operations cannot reach a discriminating channel, successful computation alone will not solve that information problem.

## Questions, value, and the danger of circular agenda setting

For a supplied task, a candidate protocol's prospective value can be written

`V_t(q,m) = R_t(current policy) - E_t[R_t(policy after m's evidence)] - expected acquisition/search/implementation cost`.

Here expectations use the investigator's stated beliefs, and `R_t` concerns the actual downstream task and horizon. This is an agenda rule, not a guarantee that the computed value is correct. A valid implementation pays for estimating it. A question can gain priority from prediction difficulties, disagreement, a new practical use, a newly available instrument, an analogy, or a deliberately scheduled exploration step. An anomaly in the incumbent representation is only one possible trigger.

If the investigator assigns probability zero to every alternative involving a missing distinction, its subjective information value for investigating that distinction can be zero. Calling a positive value into existence is an oracle. Alternatives include an explicitly supplied uncertainty class, randomized exploration in the available grammar, or a protected budget for generating and checking proposals. Each has cost and can be inferior in some environments. None is universally justified from embeddedness.

For square prediction loss, if the true joint law is supplied to an ideal evaluator, refinement from installed features `W` to `(W,Z)` has value

`R(W)-R(W,Z) = E[(E[Y|W,Z]-E[Y|W])^2] >= 0`.

This follows by conditional expectation orthogonality. It characterizes what a useful distinction accomplishes: it changes warranted conditional predictions. It does not teach the investigator the conditional expectations, pay for `Z`, overcome finite-sample estimation error, or establish a causal explanation.

## Two different restrictions exposed by XOR

Let `C,D,E` be mutually independent fair bits, with `E` a distractor. Let

`Y=C XOR D XOR N`, where `N` is independent Bernoulli(epsilon), `0<=epsilon<=1/2`.

Under ordinary independent draws, `Y` alone and every single-field pair `(C,Y)`, `(D,Y)`, and `(E,Y)` have the same fair independent law as a null world in which `Y` is an unrelated fair bit. The joint triple `(C,D,Y)` differs when `epsilon<1/2`. The ideal Brier gain of joint conditioning is `(1/2-epsilon)^2`; the ideal classification gain is `1/2-epsilon`.

Two distinct barriers must not be conflated:

* **Information barrier:** if the routine interface supplies only `Y`, or disjoint independently sampled single-field records with no shared row identifiers, the available records do not distinguish these worlds. Paid linked acquisition changes the channel. Recording all fields on the same cases destroys this observational-equivalence premise.
* **Search barrier:** if the full joint records already exist but the installed search rule only admits a joint candidate after a single-field improvement, XOR can sit on an exact single-field plateau. Information is present but the method fails to use it. This is an algorithmic restriction, not an information impossibility.

The computation below isolates the second barrier. Both investigators receive the full training rows. It must not be described as evidence that their joint information was erased. The preceding IID interface argument separately identifies what happens if linked acquisition itself is unavailable.

## An exact, non-oracular construction and validation calculation

Saved implementation: `work/formation/check_generation.py`. Exact results: `work/formation/generation-results.json`. All calculations use rational arithmetic.

### Protocol fixed before running

Training consists of one observation at each of the eight binary contexts `(C,D,E)`. This is a balanced controlled design, not an IID realization of routine contexts. The label at each row follows the stipulated noisy-XOR law independently; the evaluator exhaustively enumerates all 256 possible training label vectors.

The generator receives only the eight context/label records. It receives no world identity, XOR primitive, useful-field label, correct mapping, or true risk. For each candidate singleton or pair partition, it fits a majority-label table. Ties predict zero. Candidates are ranked by empirical 0–1 error plus `1/32` per extra table cell, with fixed lexicographic ties. The baseline fitted constant is included.

Two construction policies are compared:

* **Singleton-gated:** fit the three singleton partitions. If no singleton improves the penalized score over the constant, stop. Otherwise fit only the two pair partitions containing the chosen singleton and select the best improvement.
* **Bounded pair construction:** fit all three singleton and all three pair partitions, then select the best improvement over the constant.

One selected candidate, if any, is frozen before validation. Validation collects a new independent label at each of the eight contexts, using the same stable environment. Adoption requires at least seven correct predictions. Under the independent fair-label null, conditional on any fixed selected prediction table, the number correct is `Binomial(8,1/2)`; hence conditional false adoption is exactly `9/256`. Averaging over whether a candidate was proposed gives a smaller unconditional rate. This is a point-null, one-episode guarantee, not continuing error control or a test of every possible nonbeneficial model.

Acquisition costs one unit per label. Each fitted singleton/pair candidate costs `1/4` unit. Constant fitting is the common baseline and is uncharged. Deployment costs `1/50` unit per retained field per prediction. Future contexts are uniform on the eight rows, and the reference policy has error `1/2`. The label cost includes the training context record; field acquisition is not charged separately during inquiry. These artificial costs are declared accounting choices, not empirical estimates. All losses below include acquisition, search, validation, prediction error changes, and ongoing field costs.

### Results

| Noise | Construction policy | Probability of proposing | Probability of adopting | Expected inquiry cost | Extra expected loss over 100 later decisions |
|---:|---|---:|---:|---:|---:|
| 0 | Singleton-gated | 0 | 0 | 8.7500 | +8.7500 |
| 0 | Bounded pairs | 1 | 1 | 17.5000 | -28.5000 |
| .10 | Singleton-gated | .101359 | .000249 | 9.6115 | +9.6120 |
| .10 | Bounded pairs | .946602 | .528071 | 17.0728 | -1.4828 |
| .25 | Singleton-gated | .316132 | .005600 | 11.4371 | +11.4483 |
| .25 | Bounded pairs | .819275 | .110775 | 16.0542 | +14.1197 |
| .50 (fair null) | Singleton-gated | .429688 | .015106 | 12.4023 | +12.4326 |
| .50 (fair null) | Bounded pairs | .734375 | .025818 | 15.3750 | +15.4481 |

On deterministic XOR, each singleton's fitted predictive error is exactly `.5`; the fitted `(C,D)` table has zero error and constructs the binary classification `C differs from D`. The useful relation is inferred through a general table-fitting operation rather than supplied as the candidate to validate. The initial aggregate assertion `P(Y=1)=.5` remains true.

For deterministic XOR, bounded pair construction yields `.5-.04=.46` net gain per later prediction, so its 17.5 upfront cost breaks even at a horizon of about 38.04 decisions. At noise `.25`, selected adopted rules improve expected prediction, but the expected benefit is too small to repay inquiry at the 100-decision horizon. Under the fair null, needless field collection and inquiry produce losses despite valid false-adoption control. More capable construction is therefore neither universally advantageous nor free.

With a deliberately restricted evaluator prior placing probability `r` on deterministic XOR and `1-r` on the fair null, the bounded-pair study beats no inquiry at horizon 100 exactly when `r > 84367/240015`, about `.351507`. This is a conditional decision comparison under that two-world prior, not a prior the generator knows and not a universal exploration threshold.

Checks include independent direct enumeration of all 256 validation label vectors for each of nine numbers of underlying correct predictions, compared against the dynamic count calculation. The generator's deterministic XOR table and singleton plateau are checked explicitly. No external empirical data were collected.

## Resource and method feedback

If methods must finance their successors, use `b_(t+1)=b_t-c(a_t)+r_t`, with the receipt rule `r_t` separately declared. A positive eventual return does not establish a feasible path: before every payment, available balance plus permitted receipts/credit must cover cumulative costs. If a multi-step experiment yields its first measurable benefit only after it has finished, an immediate-performance gate can prevent it from ever running.

This suggests an explanation of path dependence: the installed representation controls measured benefit; measured benefit controls resources; resources constrain the construction and acquisition paths by which the representation could change. A protected route can break that dependence in specified worlds. It can also finance fruitless search. The exact example supplies the ingredients but does not run a reproducing institutional model, derive an attracting equilibrium, or establish empirical prevalence.

Changing a scientific standard can be treated as changing a policy for scoring evidence or admitting claims, then assessing consequences under a declared higher-level objective. That higher objective does not become true or ethically legitimate because it is implemented. Recursive evaluation can continue as a causal process, but no finite model removes all supplied evaluative commitments. Distinguish describing why a standard spreads from demonstrating its epistemic reliability and defending its moral legitimacy.

## Predictions and discriminating follow-up tests

1. **Representation depth:** on environments whose informative relation requires two fields and has zero one-field gain, a positive-singleton-gain gate should systematically miss useful questions that a bounded pair generator constructs. On one-field environments the advantage should shrink, while extra search cost remains.
2. **Information versus computation:** if joint records already exist, allowing pair computation can remove the barrier without new observations. If row linkage was never acquired, additional computation cannot substitute for linked acquisition. Factorially manipulating these two restrictions distinguishes the mechanisms.
3. **Horizon and price:** beneficial deeper inquiry can become uneconomical as deployment horizon shortens or measurement/search costs rise. The calculation gives explicit boundaries instead of a claim that openness always wins.
4. **Financing timing:** holding lifetime funds fixed, moving funds to before the decisive acquisition/search steps can change whether discovery occurs. A model sensitive only to total funds predicts no such timing effect and can be tested against this one.
5. **Correct aggregate, incomplete resolution:** relation discovery can improve conditional performance while the old aggregate forecast remains calibrated and true. Measuring only aggregate error or anomalous outcomes will miss this form of epistemic progress.

These discriminate specified mechanisms and baselines; they are not established unique signatures of the whole situated framework. Existing learning and discovery theories may predict them too. A next study should randomize generic variable names and which field combination is informative, include one-field and independent-null worlds, vary cost/horizon/linkage/search depth, and keep hidden evaluation data separate from the agent's discovery and validation records.

## Closest primary precedents and reading limits

[Klahr and Dunbar, 1988, Dual Space Search During Scientific Reasoning](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1201_1) treats discovery as interacting search over hypotheses and experiments. The primary abstract reports both memory-based hypothesis generation and generation from experimental results, including participants who reached a rule only after experimentation. We read the publisher abstract and metadata, not the full 48-page article in this contribution. This supports the relevance of experience-dependent hypothesis production; it does not validate the present toy model.

[Schunn and Klahr, 1995, A 4-Space Model of Scientific Discovery](https://cdn.aaai.org/Symposia/Spring/1995/SS-95-03/SS95-03-009.pdf) explicitly adds data representations and experimental paradigms. The primary report, especially printed pp. 40–43, already includes interactions among these spaces, new experimental routines, practical costs, risk, information tradeoffs, and feedback on expected costs and success. Its representation section acknowledges the absence of a general generator and offers search within an existing repertoire. The accessible six-page AAAI version was inspected through the full text of the model sections; the closely related proceedings record was also located. Our finite construction grammar faces a comparable limit. Neither multi-space discovery nor resource-sensitive search can be presented here as newly invented.

The possible contribution is a more explicit account of **which feasible, financed pathways permit distinctions and methods to be constructed, and which current evaluation rules block those pathways despite correct existing results**. Establishing that contribution requires comparison with these precedents, broader computational discovery work, and empirical cases. The present calculation is a mechanism demonstration and boundary test, not proof of historical novelty or of a comprehensive theory of science.
