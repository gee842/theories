# Model-family revision: retained evidence and the cost of reopening distinctions

6 October 2026. AI-authored comparator and identification note. Named connection: retained abstraction and qualified diagnosis → revision of the admitted model family → warranted use of retained or newly acquired evidence. This continues [experimental access](EXPERIMENTAL-ACCESS-COMPARATORS.md) and assesses the [revision protocol](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/PROTOCOL.md). The source comparison and elementary arguments below establish a claim boundary; they are not empirical observations or a new learning algorithm.

## Result and its exact scope

A representation sufficient for questions posed within an old family need not be sufficient after that family expands. This does not mean that every compression fails, that a full transcript is always necessary, or that fresh experiments cannot repair current prediction. It means that the preservation claim must name the family, questions, and admissible histories for which it holds.

For this continuation, the defensible positive claim is narrower than retrospective reconstruction: use a supplied candidate-generation rule to expand the current behavioral family; conservatively reopen unresolved current states; buy fresh evidence; retain only conclusions shared by the surviving candidates. The apparatus laws, action/read semantics, stationary epoch, finite candidate class, and generator remain supplied premises. The account advances by making their acquisition, retention, revision, and physical affordability explicit. It does not thereby derive unrestricted candidate invention or historical causal truth.

## Three primary comparators

**Predictive sufficiency is relative to the process and prediction target.** Shalizi and Crutchfield define causal states by grouping histories with identical conditional distributions over future observations. Their results concern discrete-valued, discrete-time stationary processes; the theoretical development assumes exact joint probabilities. The paper explicitly distinguishes predicting every future length from predicting a bounded horizon: a representation sufficient for the latter may merge distinctions needed for longer predictions. It also separates these mathematical results from statistical reconstruction from finite data. This is a strong existing antecedent for task-relative compression. It does not establish that a predictor sufficient for one process law preserves evidence for choosing a different law or reconstructing arbitrary historical causes. The term “causal state” should not be used to import that stronger causal interpretation. [Shalizi and Crutchfield, *Computational Mechanics: Pattern and Prediction, Structure and Simplicity* (2001), author-hosted full text, Definition 5, §V and §VII B](https://csc.ucdavis.edu/~cmg/papers/cmppss.pdf).

**Unknown parameters can be included in the belief state, provided their uncertainty was represented.** Ross, Chaib-draa and Pineau first give the ordinary POMDP belief update using the transition and observation laws. Their Bayes-adaptive construction then includes uncertainty about those laws: the augmented state contains the physical state and transition/observation count vectors, and the belief is a distribution over those augmented states. With hidden physical states, this is not a single observed count table. The construction assumes finite known state, action and observation sets, a specified prior family, and known reward in its stated formulation. This supplies an ordinary alternative to discarding model uncertainty: retain a larger joint posterior from the start. Its sufficiency does not automatically extend to newly invented latent variables, change mechanisms, or likelihood families absent from that construction. [Ross, Chaib-draa and Pineau, *Bayes-Adaptive POMDPs* (2007), official full text, §§2–3.1](https://papers.nips.cc/paper_files/paper/2007/file/3b3dbaf68507998acd6a5a5254ab2d76-Paper.pdf).

**Refining a hypothesis is distinct from changing the evidence semantics.** Angluin's L* retains a labeled observation table, extends it following counterexamples, and constructs successively revised automata for one unknown regular language over a fixed alphabet. The candidate can gain states while the retained membership answers still refer to the same target language. Thus growth of a candidate is already standard active learning; it does not by itself constitute revision of the admitted observation law or recovery of discarded historical evidence. If the target or reset/read interface changes, reusing earlier answers requires an additional validity argument. A retained final automaton is also a different object from the table that supported it. [Angluin, *Learning Regular Sets from Queries and Counterexamples* (1987), full text, §2 and Theorem 6](https://homepages.math.uic.edu/~lreyzin/papers/angluin87.pdf). The earlier [acquisition comparison](ABSTRACTION-ACQUISITION-COMPARATORS.md) records the teacher and finite-conformance assumptions.

These three comparisons were checked against the cited full texts, not just abstracts. They establish antecedents and premise boundaries. No human or field data are claimed here. No appeal to the Pitman–Koopman theorem is needed; in particular, there is no claim that every useful fixed-size summary requires an exponential family.

## A self-contained sufficiency test

Let \(\mathcal T\) be the admitted full histories and \(C:\mathcal T\to R\) the entire retained information available to the learner. For a deterministic historical query \(q:\mathcal T\to Y\), exact recovery from the retained record means that some \(g:R\to Y\) satisfies \(q=g\circ C\) on \(\mathcal T\).

Such a decoder exists exactly when

\[
C(\tau_1)=C(\tau_2)\ \Longrightarrow\ q(\tau_1)=q(\tau_2).
\]

Necessity follows by applying \(g\). For sufficiency, define \(g\) on each attained record to be the common query value on its fiber. Thus a summary preserves a family of queries precisely when every query is constant on every fiber. Adding a query that separates a previously merged pair defeats exact recovery from that record alone. This elementary deterministic factorization criterion is not an assertion of statistical sufficiency for a probability model.

For a finite deterministic model family \(H\), write \(V_H(\tau)\) for the models compatible with history \(\tau\). Consider two independent, equal-cost commands \(b,c\). An old model \(h_0\) predicts zero on either. Histories \((b,0)\) and \((c,0)\) both yield the old record \(V_{\{h_0\}}=\{h_0\}\). Introduce \(h_1\), which predicts zero on \(b\) and one on \(c\). The first history has expanded version space \(\{h_0,h_1\}\); the second has \(\{h_0\}\). Therefore the old version space alone cannot determine exact expanded historical compatibility. This is a counterexample to automatic transfer of sufficiency, not a claim that the repository's complete resource/controller state actually merges these two histories.

A statistical example reaches the same boundary by a different route. For two independent Bernoulli observations with common parameter \(p\in(0,1)\), their sum is sufficient: conditional on sum one, orders \(01\) and \(10\) each have probability one-half, independent of \(p\). Expand the family to independent observations with separate parameters \(p_1,p_2\). Their conditional probability ratio is now

\[
\frac{P(01)}{P(10)}=\frac{(1-p_1)p_2}{p_1(1-p_2)},
\]

which depends on the parameters. The sum no longer preserves all likelihood information for the expanded family. Both histories still have positive probability, so this example concerns lost likelihood evidence, not deterministic elimination.

If only record \(r\) survives, the conservative set of possible historical models is

\[
\{h\in H_{\rm new}:\exists\tau\in\mathcal T,\ C(\tau)=r
\ \text{and}\ h\text{ permits }\tau\}.
\]

This is generally larger than the exact version space from the unavailable actual transcript. It must incorporate any retained provenance, accounting information, timestamps, and controller state that the learner can really read. Intersecting newly admitted models with the old candidate list would instead reject them merely because they were not previously represented. An empty set flags inconsistency of the stated class and evidence assumptions; it is not a warranted diagnosis by vacuous unanimity.

## Fresh current tests versus historical diagnosis

Suppose two admissible pasts disagree about a historical cause but produce the same retained learner state and the same current physical state and future laws. Under any policy using only that state and subsequent accessible observations, the distribution of every future transcript is identical in the two cases. Induction proves this: the next action distribution is the same, its outcome law is the same, and the next retained states remain identically distributed. No such policy can establish which past occurred with certainty in both cases. Extra empty memory changes neither premise.

This obstruction disappears when an allowed intervention reaches a surviving historical trace, an independent archive supplies the lost distinction, or justified temporal constraints exclude one past. In particular, if the same unknown law is assumed to have governed the entire history, fresh tests identifying that law can also constrain historical explanations. Thus “new evidence cannot help with the past” would be false. The actual limit is absence of any accessible distinguishing consequence under the admitted temporal models.

The revision protocol correctly separates these cases. It reopens current phases in the expanded family and acquires new readings. It does not replay the auditor's old transcript into the learner or claim an exact reconstruction of all earlier compatibility. Its declared boundary-change branch must be interpreted as a new epoch; an old conclusion does not become a false old observation merely because a later law changes. Conversely, fresh agreement only supports current prediction within the supplied stationary family. It cannot certify untested sensor meaning, productive readiness, or reset behavior that the protocol excludes from its behavioral claim.

## Identification and comparator contract

The next comparison should distinguish these genuinely different conditions:

| Retention policy | Evidence available after expansion | Legitimate claim |
|---|---|---|
| Full accessible transcript | Old actions, observations and relevant provenance | Exact retrospective compatibility within a specified new family, if its interpretation applies to that epoch |
| Old-family summary only | The old conclusion and whatever other state actually survived | Only conclusions invariant across all compatible erased histories |
| Summary plus targeted witness | A retained distinction selected before deletion | Exact answers to the new questions proved to factor through that combined record |
| Larger joint model belief from the start | Uncertainty already represented over the proposed expanded family | Ordinary within-family updating, conditional on that prior and likelihood model |
| Conservative restart plus fresh tests | Newly acquired current behavior | Current-family identification, with historical ambiguity retained |

Storage and write costs must be charged when the distinctions are retained. Charge generation, translation, replay, and fresh sensing separately. Keep the auditor's complete log inaccessible to the learner in deletion branches. Equalize supplied recipes, sensor access, and current resources when comparing policies; also preserve genuine inherited resource differences when studying continuation. A supposed compression collision must equate all accessible retained state, including resource stocks and timing, not only a convenient displayed candidate list.

A synthetic result can demonstrate these semantic and resource conditions for the implemented finite class. An empirical result would additionally require independent evidence about the actual channels, model misspecification, temporal changes, and accessible historical records. Neither result identifies a uniquely generative learning algorithm: the ordinary comparators already maintain predictive states, joint beliefs, and revisable hypotheses. The unresolved foundational contribution is to derive when an organized system constructs and selects its candidate generators and retention policies under unknown future questions, with costs and operational significance arising within the system. Success at the present finite interface is progress toward that transition, not its completion.
