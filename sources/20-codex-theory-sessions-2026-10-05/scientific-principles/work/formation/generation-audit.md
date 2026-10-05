# Independent audit of the finite concept-generation example

Audit date: 5 October 2026. Read `check_generation.py` and `generation-results.json`; did not alter them. Independently reconstructed selection and enumerated training and validation outcomes with integer probability weights in `audit_generation.py`. Exact audit results are in `generation-audit-results.json`.

## Verdict

The implementation supports **experience-dependent construction and selection of predictive representations within a supplied finite grammar**. It does not establish unrestricted discovery of new primitives, a causal explanation of the generated predictor, or an information impossibility facing the greedy policy. No numerical implementation error was found. All five reported numeric metrics, for each of the eight noise/procedure rows, matched independent enumeration exactly.

## What is actually generated?

The learner receives the three binary feature identities, full-grid observations, and a grammar allowing a constant partition, any singleton partition, and any pair partition. `fit` estimates each cell's label by training-sample majority. It is not passed the world identity, the true error probability, or the XOR formula. XOR occurs only in the external evaluator and verification checks. The selected `(0,1)` table is therefore data-derived; it is not an oracle candidate inserted specifically for the signal world.

However, all reachable partition structures are specified in advance. The procedure constructs tables from experience and selects among representations allowed by that grammar. This is a meaningful finite illustration of a concept-generating operation, if "concept" is explicitly defined as a learned predictive distinction. It is also entirely describable as feature interaction search and classifier fitting. It neither learns a new sensing primitive nor independently establishes that the chosen relation is causal, explanatory, or transportable beyond the assumed future distribution.

The compositional method searches all three pairs. The greedy method first requires a singleton to strictly improve the penalized training score, then considers only pairs containing the best singleton. The initial failure in noiseless XOR comes from this search gate. Both methods already possess the same feature-rich observations. Computationally exposing a relation can make existing information usable; deterministic recombination does not add Shannon information to the full transcript.

## Fixed-grid design and marginal IID claims

Training is one noisy observation at each of the eight three-bit contexts, not eight IID contexts. Validation repeats that fixed design with fresh independent outcome noise. Deployment risk alone averages uniformly over contexts.

For uniform IID deployment, each individual bit has zero mutual information with noiseless XOR of the first two bits, and each singleton predictor has risk 1/2. This fact does **not** imply that full fixed-grid training transcripts have the same distribution in XOR and fair-independent-label worlds. A simple counterexample is the total number of positive labels: noiseless XOR always supplies exactly four; fair independent labels do so with probability C(8,4)/2^8 = 35/128. The learner can in principle notice such a discrepancy even without fitting a pair predictor. Any phrase such as "there can be no anomaly in the available observations" would overstate this experiment.

The valid statement is narrower: the declared singleton-improvement gate does not open on the noiseless balanced grid, while a broader pair search finds the signal. Any separate observational-equivalence proof must specify its own IID observation interface and must not be imported into this grid example.

## Training selection and fresh validation

Only one candidate, selected entirely from training, is evaluated on fresh validation outcomes. The accept-at-least-seven-of-eight rule is fixed. There is no selection among candidates using validation and no reuse of validation for fitting. Conditional on any selected fixed predictor in the independent fair-label world, the number correct has law Binomial(8,1/2); conditional acceptance probability is 9/256. Thus unconditional adoption equals proposal probability times 9/256, exactly as reported.

This is a one-episode calculation for the declared independent fair-label null. It is not lifetime error control and is not automatically a guarantee over every concept-free or misspecified world, dependent noise model, changing environment, or altered selection/stopping protocol. Acceptance also does not prove XOR or a particular causal theory.

For other noise rates, the code correctly uses a Poisson-binomial tail because contexts on which the predictor matches underlying truth have success probability 1-eps, and other contexts have success probability eps. Our audit directly summed all validation outcome vectors, independently checking this tail usage.

"Adoption probability" should not be labeled "successful discovery probability": it includes inaccurate or unprofitable adopted representations. The independent audit additionally records adoption probabilities for candidates with nonpositive expected deployment gain after feature costs. For example, at eps=1/4 the compositional procedure's total adoption probability is about .110775, while about .007208 of episodes adopt a predictor whose deployment gain is nonpositive. These bad-adoption rates use the evaluator's true risk and are unavailable to the learner.

## Prices, baseline, and decision horizon

The cost calculation consistently charges eight training outcomes, 1/4 for each searched singleton or pair, and eight fresh validation outcomes only when a candidate is proposed. The constant baseline fit is uncharged, as are choosing/arranging all feature contexts, obtaining their values during training, storing them, and performing validation comparisons. This is a declared stylized cost model; "all inquiry costs" would be too broad unless those free operations are explicitly made assumptions. The parameter description "cost per candidate fit" should be understood as cost per nonconstant searched fit.

Future gain equals the baseline risk 1/2 minus the candidate's true noisy risk and a deployment cost of 1/50 per retained feature, multiplied by its adoption probability. If no candidate is adopted, the system returns to the baseline and receives no future incremental gain. All modeled worlds have balanced deployment labels, so either constant prediction has baseline risk 1/2. This accounting is coherent.

The acceptance gate is not an economic optimizer: it does not take the future horizon, true gain, or total inquiry expense into account. The reported `cost - N*gain` correctly evaluates the resulting strategy against zero-cost baseline deployment in expected common loss units. Break-even horizon is an expectation ratio, not a guarantee that any individual run pays back its investment. Inquiry itself worsens expected performance in some conditions; this is visible in the reported results. Comparison with a more capable preexisting predictor, a different cost schedule, or a price-aware adoption rule could change conclusions.

## Safe conclusions and excluded ones

Supported: a locally attractive search restriction can block a useful interaction; a generic broader grammar can construct a predictive rule from data; selection can be tested on independent outcomes; and search/validation/deployment prices can make the same capability worthwhile or wasteful depending on noise and horizon.

Not established: that the old observations contain no informative discrepancy, that the learner discovers unrestricted new concepts, that pair searching is generally best, that the true model is identified, that adoption proves a causal explanation, or that the experiment explains historical scientific change.

The example is therefore suitable as one conditional mechanism within the proposed theory. It illustrates how an implemented rule for admitting representational changes affects what gets discovered. It does not by itself constitute a general theory of the origins of scientific questions, concepts, or standards.
