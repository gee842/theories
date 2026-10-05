# How discovery can preserve further discovery

Prepared 5 October 2026. Continuation of [How generative systems maintain the capacity to change](../ANSWER.md). This combines primary research, a project-precedence audit, constructed counterexamples, and an exact extension of the maintenance model. It is an AI-assisted research synthesis, not empirical validation of a universal theory.

Subsequent development: [How inherited means preserve or obstruct further generation](../succession/ANSWER.md) completes a bounded construction-and-succession study and a matched-material access comparison. Its contrary results qualify the proposal below: retained material can support later answers while impeding new construction when all of it is automatically active in search.

The important addition is that **when preserving access to future capabilities is an aim, current usefulness is not in general a sufficient criterion for deciding which differences to retain**. Structurally different arrangements can perform identically now while enabling different next steps. A presently inferior intermediate can also make a later useful capability reachable. Reproducing only the current best answer can remove the paths through which another answer would become possible.

The proposed generative relationship therefore includes the supported formation of new possibilities: differences are available to encounter, combine, and test; some acquire a function in a particular setting; workable constructions obtain support; and the resulting organization carries forward the means to form and test further possibilities. This is a causal hypothesis with identifiable parts, not a guarantee that protected variation will succeed.

## Present equivalence does not establish generative equivalence

Consider two arrangements A and B that supply exactly the same present service. Suppose an affordable construction step can turn B into C, which provides a required new capability, while no admissible path from A can provide it by the deadline. A description that retains only current service merges A and B. That description answers the current service question correctly but cannot answer the transformation question correctly.

This is a constructed counterexample, not a finding about every pair of arrangements. It establishes why the relation between forms matters alongside their present outputs. Which arrangement was retained changes what can be generated next, even before any observed service difference appears.

The earlier canonical representation result remains valid: a compression must preserve its declared intervention-response questions. The new implication concerns what those questions should cover. If the inquiry concerns generativity, tests of continued construction and revision cannot be replaced by current performance alone. A compression sufficient for today's questions need not be sufficient for a later question that was not included. No universal decoder can restore a distinction that the retained record erased.

The biological literature supplies a concrete analogue: in RNA folding models, different sequences can preserve a phenotype while placing a population near different possible phenotypes. The result depends on the level and measure of robustness; accessible variation does not automatically equal useful innovation. [Wagner 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2562401/).

## A useful path need not improve at every step

Digital-evolution experiments reconstructed pathways to complex functions that sometimes included immediately harmful mutations. Their contribution depended on the surrounding genetic configuration. This supplies an existence example of useful paths through inferior intermediates, not a general reason to preserve harmful variants. [Lenski and colleagues 2003](https://cse.msu.edu/~ofria/pubs/2003LenskiEtAl.pdf).

The synthesis is a distinction between **remaining available for investigation** and **being approved for operational use**. A conjecture can remain discussable without becoming official truth. A prototype can remain available for another construction without being installed. A practice can receive a bounded trial without acquiring permanent authority. These are proposed cross-domain interpretations of the distinction, not results directly established by the biological experiments.

There are costs on both sides. Removing all uncertain intermediates can eliminate future paths. Protecting every intermediate can exhaust the resources needed to investigate or install any of them. The generative requirement is consequently a maintained, accountable capacity to develop some uncertain possibilities while respecting ongoing obligations. It is neither unrestricted permissiveness nor a rule requiring every local step to improve the incumbent score.

March's organizational-learning model offers a related mechanism: rapid assimilation can extinguish differences from which the organizational code learns. Its reality-based comparison of individuals is supplied, however, so it does not explain how institutions reliably recognize better knowledge. [March 1991](https://doi.org/10.1287/orsc.2.1.71).

## What a new function means

Learning an unknown fact, creating a representational distinction, constructing a new effective action, and developing a new purpose are separate claims. The project's existing situated-discovery study already generates and validates policies within a supplied grammar. Its success should not be relabeled as the invention of a new action repertoire or purpose.

A function is realized through relations among a construction, its surroundings, and the relevant activity or purpose. A new artifact can make a response practically executable that was unavailable before, even if fixed physical rules describe both situations. Merely listing more programs or renaming existing actions does not establish this gain. The prior interface, resources, time, and permissions must be specified well enough for the difference to be checked.

Taylor's framework distinguishes search within a representation from changes requiring richer descriptions, and considers new uses of components and their combinations. It does not establish a sufficient mechanism for indefinitely expanding novelty. [Taylor 2019](https://arxiv.org/html/1806.01883v4).

The strongest proposed mechanism here is therefore construction and recombination whose consequences can change what subsequent construction makes available. A successful outcome may become a tool, a test, an environmental support, or an interpretable example for later inquiry. Whether this occurs has to be demonstrated, rather than inferred from increasing output or complexity.

## Discovery must share a budget with its own maintenance and implementation

The mathematical companion adds a different, narrower result. It charges discovery, noisy validation, and installation to the same effort that maintains both current operation and the inquiry apparatus. Candidate quality is supplied probabilistically. This calculation constrains the process; it does not explain the invention of candidates or useful intermediates.

Let support 1 maintain current service and support 2 maintain inquiry. For each, define a required maintenance fraction `p_i` and an inherited reserve duration `t_i` as in the previous establishment model. Assume `p_1+p_2 <= 1`. Then the exact maximum work available for discovery, validation, and installation by time T is

\[
B(T)=T-p_1(T-t_1)_+-p_2(T-t_2)_+.
\]

Both supports remain above their operating floors. The proof and all assumptions appear in [DISCOVERY-MATH.md](DISCOVERY-MATH.md).

If `p_1+p_2=1`, preserving the two supports uses all recurring effort. Inherited reserves can permit a finite amount of research, but the lifetime extra-work budget is only `p_1 t_1+p_2 t_2`. An inquiry apparatus can remain functional forever while there is eventually no effort available to use it. If the maintenance fractions sum to less than one, a continuing margin is available under the model's stable conditions.

Every candidate consumes generation work and fresh validation work. An accepting branch must still afford installation. Spending the whole allowance on finding and testing an idea does not make its implementation free. The comparison also keeps false installation distinct from failing to install anything by the deadline.

For one declared example, maintaining operation and inquiry leaves 12 work units; installation requires four, candidate generation one, and each validation observation one. Candidates are equally likely to be good or bad; positive observations occur with probability three quarters for a good candidate and one quarter for a bad one. All these probabilities are supplied, not learned or empirically estimated.

| Fixed protocol | Good installed | Bad installed | None installed |
|---|---:|---:|---:|
| One observation per candidate and up to four attempts | 70.31% | 23.44% | 6.25% |
| Three observations with three positives required and up to two attempts | 37.57% | 1.39% | 61.04% |
| Six observations with four positives required and one attempt | 41.53% | 1.88% | 56.59% |

The final row maximizes good installation subject to a two-percent bad-installation limit among the 37 enumerated deterministic fixed-batch protocols, including no inquiry and shorter stopping limits. This is the unconditional chance of a bad installation across all runs, including runs with no installation. Among runs that install something, the final row's bad fraction is instead `77/1778`, about 4.33 percent. It is not an optimum over adaptive tests, different generators, randomized policies, or other models. A two-percent limit is an illustrative supplied requirement, not a universal acceptable risk.

The checks independently reproduced 36 exact support-frontier comparisons and nine candidate outcome trees, including complete branchwise installation costs. See [VERIFICATION.json](VERIFICATION.json). The probability tradeoff cannot be eliminated by calling more proposals successful discoveries. For a fixed noisy rule that stops on first acceptance, more attempts also increase the chance of accepting a bad candidate. The companion gives a conservative confidence-and-work bound for a stricter finite procedure.

## What has to survive succession

The revised target is **continued discoverability**, not merely inheritance of a discovery. A successor may inherit an excellent instrument while lacking calibration skill, experimental access, records, time, or authority to question its interpretation. Performance on the old problem can continue while the ability to investigate another problem disappears.

This distinguishes the inheritance of a product from inheritance of means to construct and contest products. It also keeps the people involved visible. A research apparatus that serves only the incumbent can sustain invention while suppressing other participants' questions. Continued inquiry and shared health remain different claims, requiring separate accounts of access, burdens, and standing.

At this stage no completed succession experiment was claimed. The discriminating study proposed here would let a learner construct a new effective response, remove the predecessor, and present a different challenge. It would compare inheritance of the solution with inheritance of usable experimental means and authority, while charging maintenance, evidence, retention, and establishment to matched budgets. Some environments must reward retained intermediates, others make them useless, and others make their carrying costs decisive. Otherwise the result is built into the example. The subsequent study linked above implements paid construction and inheritance but leaves the base learner, authority and resource supply externally specified.

The existing project models already establish important pieces: paid candidate generation, fresh validation, distinct implementation gates, questions without anomalies, and limitations of inherited summaries. The [critical analysis](CRITICAL-ANALYSIS.md) identifies precisely what a new construction-and-succession study would add. The [research memo](RESEARCH.md) separates empirical, computational, and conceptual support.

## The refined core

The earlier account emphasized sustaining the conditions under which forms can change. This extension adds that current forms must also leave supported ways for differences to acquire new functions, and must carry those ways forward through succession. Selection based only on current performance can extinguish that process even while present functioning improves.

The proposed invariant remains a relationship: **activity renews the conditions through which further activity can become possible, intelligible, and executable, while allowing those conditions themselves to be revised**. The support, inquiry, and installation calculations provide conditional constraints on this relationship. The origins of particular inventions, the emergence of new purposes, and cross-domain universality remain substantive open questions.
