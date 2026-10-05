# Standards, institutions, and the changing conditions of inquiry

Research memo, 5 October 2026. Prepared for the continuation of Ren's theory-of-science investigation. Scope: explicit mechanisms, primary-source comparison, and failure tests. This is conceptual model development, not an empirical validation or a novelty claim.

## Provisional answer

The proposed framework can support a theory of scientific development if it explains changes in the machinery of inquiry, rather than only imposing requirements on a fixed testing procedure. The promising object is a coupled process: available observations influence accepted questions; questions direct investments in methods; methods create evidence; evaluative standards determine which evidence and people receive attention; those allocations alter the questions, methods, and standards available next. Causal embeddedness makes such feedback admissible, but does not specify its direction or establish that it is reliable.

A useful theory must distinguish at least four outcome variables: epistemic performance on a declared target, institutional reward, the continued availability of inquiry, and ethical legitimacy. These can move separately. A method can yield accurate answers to an unimportant or harmful question; an institution can prosper while its methods deteriorate; an unpopular approach can be accurate but unmaintainable. A theory that uses “success” for all four cannot explain their divergence.

## Primary sources and genuine differences

**Kuhn, “Objectivity, Value Judgment, and Theory Choice” (1977).** The accessible primary excerpt lists accuracy, consistency, scope, simplicity, and fruitfulness, then discusses ambiguity in their application and conflict among them. Shared criteria therefore need not yield a unique individual choice. This matters for our framework because disagreement cannot automatically be coded as epistemic malfunction: differences in interpretation and weighting need representation. Kuhn is analyzing theory choice and the character of scientific judgment, not proving an optimal policy under a known loss function. Replacing his plural values with one fixed utility function would change the problem. Verified locator: opening discussion from “What, I ask to begin with” through “Individually the criteria are imprecise,” and subsequent paragraphs. [Primary excerpt at UCSD](https://cseweb.ucsd.edu/~goguen/courses/268D/kuhn.html). The linked CMU scan has 12 pages, but local extraction was uninformative; the excerpt, rather than the whole essay, was read.

**Longino, “Cognitive and Non-Cognitive Values in Science: Rethinking the Dichotomy” (1996), pp. 39–58.** Longino treats evidential relevance as dependent on background assumptions and disputes context-independent epistemic authority for familiar theoretical virtues. Her ending allows local communities provisional standards, revisable through engagement with other communities and the world. The opening explicitly places Laudan's theories–methods–aims reticulation in the existing literature. This is substantial prior art for our proposed revisable standards. Our separation of epistemic reliability from ethical legitimacy should be understood as an analytical distinction, not a claim that actual standards are socially neutral. Longino's position goes beyond optimizing accuracy within an already fixed target. Verified locators: introduction and contextual empiricism, pp. 39–40; criteria discussion, pp. 42–45; conclusion, pp. 54–55. [Primary chapter scan](https://joelvelasco.net/teaching/5330/longino1996.pdf). Indexed primary text and PDF parsing exposed these passages, but repeated direct fetching was intermittent. No claim to have audited the entire book or her later four-condition formulation is made.

**Smaldino and McElreath, “The natural selection of bad science” (2016).** Their population model makes research methods culturally transmissible and ties laboratory reproduction to publication success. Effort, false positives, and publication opportunities can consequently evolve in directions that impair reliability without requiring deliberate deception. Replication did not arrest deterioration under their modeled conditions; that result is not an impossibility theorem for every incentive system. This supplies an explicit explanatory mechanism for method persistence, unlike a purely normative prescription to be careful. Verified locators: preprint §4, especially §4.1–4.2, and §5.1–5.3; PDF pp. 14–27. [Primary preprint](https://arxiv.org/pdf/1605.09511). Reproducing this qualitative mechanism in our vocabulary would be synthesis, not a new discovery.

**Kohrt, Smaldino, McElreath, and Schönbrodt, “Replication of the natural selection of bad science” (2023).** Their reimplementation found a coding problem that changed the transient evolution of replication frequency while preserving the main deterioration result. This is both a qualification on the original implementation and an example of independent scrutiny exposing a discrepancy between description and execution. The companion correction also identifies implementation-order and parameter-description issues. Verified locators: abstract, replication results, and conclusion. [Primary replication](https://pmc.ncbi.nlm.nih.gov/articles/PMC9943874/) and [authors' correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC10480692/). The replication is evidence about this model's implementation and robustness, not confirmation that every scientific institution follows its dynamics.

**Weisberg and Muldoon, “Epistemic Landscapes and the Division of Cognitive Labor” (2009), pp. 225–252.** Their agents explore an unknown landscape using different social search rules. The model compares independent exploration, following, and avoidance of already investigated approaches. Its limitation is especially useful here: an approach's objective significance is supplied, a visit yields the corresponding truth, and exploration costs are idealized. They explicitly warn against quantitative application before robustness testing. We should not equate their “maverick” strategy with universal endorsement of dissent. Verified locators: §2.1–2.2, particularly pp. 232–234 and footnotes 6–7; discussion pp. 249–251. [Author-uploaded full text](https://www.researchgate.net/publication/257943182_Epistemic_Landscapes_and_the_Division_of_Cognitive_Labor); [institutional manuscript](https://repository.upenn.edu/bitstreams/020cfba0-9660-434c-8c33-44b1264e9d82/download). Repository access failed, so the author-uploaded primary text was used. The 2009 publication date should not be replaced by the hosting platform's later upload date.

These sources address different questions: judgment, evidential relevance and values, selection among practices, implementation correction, and collective search. They are not equivalent expressions of a single established law.

## Minimal model that makes the mechanism inspectable

Let the community state contain a candidate-question set Q, represented model families H, feasible methods M, retained records D, operative standards V, agents and communication links N, and resources R. The observer's structural signature S=(X,T,R,O) can contain these, but merely listing them is not yet an explanation. A model must specify transitions, who observes which variables, and how a rule is implemented.

One deliberately restricted episode is:

1. A proposal mechanism generates a question and candidate explanatory package.
2. An admission rule allocates time or funds, using current standards and accessible records.
3. A selected method acts on the world and returns a fallible observation while incurring costs.
4. A reporting rule determines what survives into the communal record.
5. Evaluation distributes credit, training opportunities, and later research resources.
6. A revision mechanism can change any of the preceding rules using specified evidence and authority.

This model separates **generation**, **admission**, **validation**, and **propagation**. It permits a promising question to be admitted without treating its conjectured answer as established. It also permits a published result to propagate because of its reward while being poorly warranted. None of these transitions should secretly receive access to the experimenter's true world state.

The revision mechanism is itself an implemented process with costs, limited observations, and power relations. Encoding a transition V→V′ is sufficient to represent a standard change, but not sufficient to explain it. Its selection rule, enabling resources, and evidence must be specified. A schema that permits every transition equally explains none of them.

## Four modelable mechanisms

### 1. Methods reproduce under institutional rewards

For method j, let sensitivity be s_j, false-positive probability f_j, true-claim prevalence π, per-opportunity cost c_j, reward per positive result u, probability of detecting a published false claim d, and penalty λ. A simple expected institutional score is

R_j = u[πs_j+(1−π)f_j] − c_j − λd(1−π)f_j.

For equal sensitivity, let careful research have additional cost Δc>0 and reduce f by Δf>0. Then

R_careful − R_quick = (1−π)Δf(λd−u) − Δc.

Thus careful research wins in expected score exactly when λd>u+Δc/[(1−π)Δf]. A propagation rule increasing with score is an additional premise; negative scores cannot directly serve as probabilities. The calculation assumes common exogenous detection, collectible penalties, no erroneous penalties on true results, equal opportunity timing, and no other effects. If time or throughput differs, compare returns per limiting resource or use a full dynamic budget. This is a restricted reconstruction of an established selection mechanism, not an argument that harsh penalties are ethically justified or always effective.

### 2. An admission rule can prevent its own correction

Suppose an incumbent method maps two relevant world states to the same observation distribution. A new calibration would distinguish them, but funding is permitted only after an anomaly appears in the incumbent observations. Then no observation-based anomaly rule can selectively trigger calibration in the problematic state. Repetition and higher internal confidence do not supply the missing distinction. This is the earlier information bound applied to institutional admission.

Correction can become possible through an external signal, a scheduled audit, a separately justified exploratory allocation, or a new observation channel. Which one is affordable remains a decision problem. The prediction is selective: opening an informative route can improve diagnosis; admitting arbitrary alternative stories without new information cannot. “Criticism welcomed” is insufficient if criticism cannot reach a relevant test or alter allocation.

### 3. Current output can consume future revision capacity

Let calibration capability r_t decline by δ per period without maintenance; paying maintenance k preserves it. Suppose current publication score gives maintenance zero credit and a budget allocation rule directs all funding to currently rewarded output. Then, under those assumptions, capability eventually disappears even while publication score remains high. After an instrument change, the institution may be unable to distinguish physical change from sensor failure.

This is not an unconditional claim that science must preserve every capability. In stable worlds, maintenance may be wasted; substitute infrastructure can make local loss harmless; a completed project may reasonably close. The modelable hypothesis is that the value of maintenance depends on future diagnostic need, replacement time, and access to substitutes. Record these separately from organization survival.

### 4. Revised standards can improve scores without improving answers

Let old and new standards score different targets or populations. A change in reported performance is not interpretable until targets, populations, and scoring rules are tracked. One can improve an internal score by changing what counts as a question, excluding difficult cases, or selecting a favorable evaluator, even when the underlying conditional predictions stay fixed.

This mechanism need not involve dishonesty: a defensible change of scientific purpose also changes the evaluation problem. Where targets are comparable, retain a common prospective evaluation panel and report old and new scores. Where they are not comparable, report the change of purpose rather than asserting global improvement. A procedure's decision to include a neglected population may be ethically warranted even if a chosen average accuracy score declines. The data inform consequences; they do not settle standing.

## Concrete next test and failure conditions

Extend the existing sensor laboratory into a small research community. Every agent initially has the same vocabulary, observations, and resource allowance. Give the institution an admission rule, publication score, and renewal rule. Randomize independently: whether calibration is informative, its cost, whether physical or sensor drift later occurs, delay to external feedback, and whether maintenance produces immediate credit. Keep a fixed resource-matched schedule as a comparator.

Compare four declared mechanisms: incumbent-anomaly admission; scheduled exploratory calibration; calibration conditional on externally validated diagnostic value; and the same policy with resource renewal unavailable. Do not give the adaptive arm the correct diagnosis or future drift time. Measure correct diagnosis, false revision, missed change, time to correction, costs, and preserved future testing capability. Institutional credit must be a separate outcome. Evaluate on withheld worlds and new fault mechanisms; fitting the community model to its own favorable outcomes does not assess generalization.

Expected interactions matter more than a universal winner. Maintenance should help when relevant drift precedes replacement and hurt when expensive and unnecessary. Opening admission should help only where a usable informative test exists. A credit change should influence method prevalence only through the modeled propagation mechanism. These predictions make explanatory components independently vulnerable.

The proposed implementation loses support if its advantage disappears after fair resource matching, if diagnosis improves without the allegedly mediating information channel, or if measured institutional behavior does not follow the proposed allocation and propagation rules. Stable-world false revisions can defeat a claimed overall advantage. A simulation can check consequences of stipulated mechanisms; historical data or intervention studies would still be needed to show that a real institution instantiates them.

## Decisions and open work

Accepted: a theory of science should explain the production and revision of inquiry's conditions as well as belief updates. Rejected: persistence proves truth; consensus proves independence; every standard revision is progress; the framework derives an ethical objective; broad causal vocabulary is explanatory evidence.

The strongest unresolved task is concept and standard generation beyond a supplied menu. A finite model can explain why an available variant spreads without explaining how investigators invent it. Do not rename a programmer-supplied action “emergent discovery.” Further primary reading should include Laudan's actual reticulation argument and work on concept formation; the present memo verifies Longino's engagement with that argument, not Laudan's book itself. Novelty remains unestablished. The defensible contribution to pursue is a testable account of interactions among changing distinctions, admission, resource renewal, and revisable evaluation.
