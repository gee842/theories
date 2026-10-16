# Sources and claim status for causal foundations

This record accompanies the [synthesis](causal-foundations.md) and [formal appendix](formal-results.md). Research date: 5 October 2026. Ren supplied the question and conceptual direction; the formal examples, source comparison, verification, and synthesis were produced with AI research assistance. Three internal research agents divided the formal, causal-modeling, and conceptual audits. Their agreement is not independent empirical evidence or human peer review.

## Claim register

| Claim | Status and basis | Boundary or failure condition |
|---|---|---|
| Observer and revision processes should have explicit realizations or declared support assumptions | Proposed explanatory discipline | Does not require microscopic completeness or a cost model for every process |
| Effective mechanism revision can be a state change under a larger fixed rule | Exact representation construction | Explains neither why that rule holds nor how an unforeseen mechanism is discovered |
| The signature S needs a closure test to evolve autonomously | Conditional mathematical requirement | Same signature with different next-signature laws defeats the proposed closure |
| Intervention-relative quotient preserves specified macro path laws | Proposition A, established controlled lumpability ideas | Requires common admissible protocols, initial law, appropriate observations and chronology, and macro-defined outcomes |
| Uniform one-step total-variation error bounds finite-horizon error | Proposition A extension, coupling proof | For observation-first control, bound must hold conditionally on each supported observation, or observation must be in the state |
| Identical observation laws can have different intervention laws | Proposition B1, exact two-model counterexample | Additional experiments or justified structural restrictions can distinguish them |
| Matching all nine perfect-intervention distributions on a binary observed pair need not fix individual counterfactuals | Proposition B2 and extended enumeration | Interventions on latent context are not included; cross-world coupling is additional structure |
| Exact memory requirements depend on the future query family | Proposition C, pigeonhole and construction proof | No claim about optimal lossy compression, privacy, or net value after storage costs |
| Universally correct announced-bit prediction can be defeated | Proposition D, diagonal construction | Requires a responder able to see and negate that bit in time |
| Arbitrary finite traces fit some augmented dynamics | Proposition E, timestamped trace construction | Fit is not identification of causal mechanisms or prediction under new interventions |
| Descriptive dynamics alone do not select an evaluative ordering | Proposition F, underdetermination without added normative premises | Not a theorem against moral realism or the relevance of facts to ethics |
| Information, recognition, enactment, resources, and goals have distinct causal roles | Constructed finite institutional example | Supplied probe, candidate grammar, initial budget, rules, and short support horizon |
| A rule can be revised through a paid internal amendment procedure | Exact staged example, success 1 versus 1/2 without its amendment channel | Amendment channel remains supplied; success does not establish legitimacy |
| Modeling support renewal improves prediction beyond simpler models | Research hypothesis, not tested here | Must improve held-out intervention prediction or explain a preregistered difference |
| Causality is the final foundational vocabulary | Open philosophical conjecture | No result in this investigation establishes it |

## Decisions retained from the investigation

We retain a finite classical model as a useful formal laboratory, while declining to treat it as universal physics. Functional distinctions among model, policy, goal, and institutional arrangement can share their realization. The actor's accessible information remains smaller than the analyst's state description.

We use intervention-relative equivalence rather than treating graph shape or every microscopic difference as the effective causal structure. Abstract action labels must correspond to feasible protocols, or be explicitly hypothetical comparisons. If different hidden states require different implementations, merely proving that an implementation exists in each state is insufficient: an actor must have an information-admissible way to select it.

We distinguish actual goal change from justified improvement, and operational access from legitimate authority. The reference research's normative commitment to shared agency is retained as an explicit commitment. It is not deduced from persistence, complexity, novelty, or causal influence.

Review corrected the general update to depend on the current observation, so it can store what was sensed. It also sharpened the approximate abstraction condition for adaptive interventions and corrected an unrelated bibliographic link before delivery. These were corrections to exposition and assumptions, not failed empirical predictions.

## Core primary sources

These are scoped precedents, not a claim that the proposal is novel or that the literature review is exhaustive. Links lead to original papers, author copies, or original texts. Claims in the report go no further than the stated uses below. Exact examples and proofs in the appendix are our own elementary reconstructions.

**Pearl 2009 — Causal inference in statistics An overview.** Structural assignments and equation replacement distinguish interventions from observational conditioning; section 3.4 defines unit counterfactuals using a fixed background context. This is semantics conditional on a causal model, not recovery of causal meaning from arbitrary covariance. Checked locators: sections 3.2–3.2.1 and 3.4, especially Definition 4 and equation 27. [Author PDF](https://web.cs.ucla.edu/~kaoru/SS-2009-57-Sup.pdf); [published article](https://doi.org/10.1214/09-SS057).

**Bongers, Forré, Peters and Mooij 2021 — Foundations of Structural Causal Models with Cycles and Latent Variables.** Cycles may destroy existence, uniqueness, marginalization, and familiar graphical properties; stronger solvability assumptions restore specified results. The extended author version's sections 3, 4 and 8 distinguish these issues. Definition 8.1 and Proposition 8.2 concern simple SCMs. Numbering is for the extended 75-page version, not the journal layout. [Primary paper](https://arxiv.org/abs/1611.06221); [journal DOI](https://doi.org/10.1214/21-AOS2064).

**Rubenstein and colleagues 2017 — Causal Consistency of Structural Equation Models.** Definition 3 uses state and intervention maps to require agreement of corresponding intervention distributions; Theorem 6 develops the causal consistency interpretation. Allowed interventions and solvability are declared. The result does not endorse arbitrary aggregation. [Primary paper](https://arxiv.org/abs/1707.00819).

**Beckers and Halpern 2019 — Abstracting Causal Models.** Example 3.4 and Definitions 3.5 onward examine overly permissive transformation notions and stronger requirements linking context, state, and intervention maps. These distinctions motivate explicit scope for invariance. They are stronger and more varied than the appendix's simple kernel quotient. [Author PDF](https://www.cs.cornell.edu/home/halpern/papers/abstraction.pdf); [primary preprint](https://arxiv.org/abs/1812.03789).

**Beckers, Eberhardt and Halpern 2019 conference and 2020 proceedings — Approximate Causal Abstractions.** Section 3 extends exact causal abstraction using specified discrepancy metrics. This supports testing approximate correspondence while making errors and interventions explicit. Our elementary finite-horizon coupling bound is not presented as the paper's theorem. [Proceedings and paper](https://proceedings.mlr.press/v115/beckers20a.html).

**Givan, Dean and Greig 2003 — Equivalence notions and model minimization in Markov decision processes.** Section 3.2 and Theorems 5–7 develop stochastic bisimulation and preservation of suitable rewards and control properties. This is close precedent for the finite controlled quotient. The report restricts itself to a common preserved-information policy and does not transfer optimality between differently informed controllers. [Author-hosted primary PDF](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf).

**Wolpert 2008 — Physical limits of inference.** Setup and conclusion functions represent inference devices within possible world histories. Proposition 1(ii) and Theorem 1 establish limits under the paper's definitions; the latter requires setup-distinguishability. The appendix's exposed-bit negation argument is a separate elementary result. Neither warrants claiming that all prediction or self-modeling is impossible. [Primary text](https://arxiv.org/html/0708.1362v2).

**Montévil and Mossio 2015 — Biological organisation as closure of constraints.** The article distinguishes constraints conserved at relevant operating scales from the processes they constrain, and develops reciprocal maintenance. Its organizational closure is neither thermodynamic isolation nor universal physical causal closure. The author's site and direct PDF did not load in this session; the author-uploaded article text was inspected instead. [Author-uploaded primary article](https://www.researchgate.net/publication/262486802_Biological_organisation_as_closure_of_constraints); [DOI](https://doi.org/10.1016/j.jtbi.2015.02.029).

## Adjacent precedents and alternatives

**Mooij, Janzing and Schölkopf 2013 — From Ordinary Differential Equations to Structural Causal Models the deterministic case.** Section 2.2 interprets ideal clamping through feedback and an infinite-gain limit; Theorem 2 requires stability conditions for correspondence between intervened dynamics and equilibrium SCMs. An equilibrium alone does not preserve transient behavior. [Primary paper](https://arxiv.org/abs/1304.7920).

**Sokol and Hansen 2014 — Causal interpretation of stochastic differential equations.** Definition 2.4 gives a substitution-based intervention semantics, while section 4 relates it to discretized structural models. Theorem 5.3 identifies postintervention distributions from a generator under specific regularity and noise conditions. This is not identification from arbitrary finite data. [Primary paper](https://arxiv.org/abs/1304.0217).

**Dawid 2021 — Decision-theoretic foundations for statistical causality.** Regime indicators distinguish observation from intervention, and stability assumptions justify transfer between them. This provides a causal decision framework without making a joint distribution of all individual counterfactuals primitive. [Primary paper](https://arxiv.org/abs/2004.12493).

**Conant and Ashby 1970 — Every good regulator of a system must be a model of that system.** The original model relation depends on its regulation, success, and simplicity assumptions. The title should not be read as proving that every effective organism or institution learns a rich explicit world model. [Original PDF](https://theisticscience.com/papers/tree/BioRegulation/Conant-IJSS1970.pdf); [DOI](https://doi.org/10.1080/00207727008920220).

**Virgo, Biehl, Baltieri and Capucci 2025 — A good regulator theorem for embodied agents.** Definitions 3.1–3.3 and Theorem 3.4 relate regulation to consistent belief interpretations and a normative map in deterministic discrete time. Section 3.2 admits trivial examples such as a doorstop. An interpretive model relation does not demonstrate learned rich representation. This is a preprint, not a claim of settled consensus. [Primary text](https://arxiv.org/html/2508.06326v1).

**Kolchinsky and Wolpert 2018 — Semantic information autonomous agency and nonequilibrium statistical physics.** Sections I.2 and IV–VI define a technical kind of semantic information through interventions and a viability function. Boundaries, timescales, distributions, and evaluation choices matter. This does not equate all linguistic meaning, truth, or ethical legitimacy with self-maintenance. [Primary text](https://arxiv.org/html/1806.08053).

**Oreshkov, Costa and Brukner 2012 — Quantum correlations with no causal order.** The process-matrix construction explores correlations without assuming a predefined global order, under local quantum assumptions. It cautions against declaring one classical graph language universal; it does not show that ordinary institutional feedback lacks temporal order or that the universe as a whole violates every definite-order account. [Primary publication](https://www.nature.com/articles/ncomms2076).

**Hume 1740 — A Treatise of Human Nature.** Passage 3.1.1.27 asks for an explanation of the transition from descriptive propositions to an ought. It is a historical precedent for keeping normative premises explicit, not an endorsement of every part of Hume's metaethics. [Original text](https://davidhume.org/texts/t/3/1/1).

## Relationship to the reference workspace

The integrated-evolution README and CLAIMS register were read as reference, especially U01, U05, U12–U13, U20–U25, H01–H05, P01 and N01. Recent source snapshots on frame formation, inherited evidence, selection and renewal, and inquiry renewal supplied context. The new formal results overlap established ideas already acknowledged there; none is presented as a discovery replacing that record.

This task's contributions are the disciplined minimal embedding, the distinction between effective mechanism change and a larger fixed dynamics, the explicitly scoped representation-invariance criterion, and a synthesis of what causal participation does and does not establish. Their usefulness as an integration remains to be demonstrated through applications.

## Unresolved assumptions and next discriminating work

1. **State and boundary selection.** Does the proposed state retain what matters under new interventions, or only under the training policy? What environmental supports remain outside the boundary?
2. **Intervention realization.** Which protocol actually implements each theoretical intervention, with what side effects, access requirements, delays, and failure modes?
3. **Semantic interpretation.** What makes an internal variable a representation used by the system, rather than merely a convenient description imposed by the analyst?
4. **Acquisition and novelty.** How are distinctions and candidate programs acquired? Which possibilities are supplied in advance, and which are generated by a demonstrated process?
5. **Maintenance of revision.** Can the amendment or evaluation process survive turnover, loss, and resource shortages? Can it restart or be replaced when its own implementation fails?
6. **Multiple purposes and authority.** How are disagreement, affected parties, protected constraints, and legitimate revision represented without assuming that current control confers justification?
7. **Empirical discrimination.** Does the richer model improve predictions under held-out interventions enough to warrant its extra structure? What observed result would count against it?

The immediate research target is one bounded system in which a previously supplied support for revision becomes endogenous, with explicit alternatives and a held-out intervention test. Continuing to add unrestricted variables without such a test would enlarge the description without establishing a stronger foundation.
