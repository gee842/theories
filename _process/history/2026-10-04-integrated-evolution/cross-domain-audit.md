# Cross-domain audit: selection and the conditions of continued generation

Prepared 4 October 2026 as an independent AI-agent research memorandum for Ren's requested integrated theory. This is a constructive adversarial assessment, not a completed systematic review or a claim of originality. Existing corpus claims remain distinct from new proposals. No experiment was run for this memorandum.

## Assessment

A useful common theory is possible at the level of **event accounting, coupled state dynamics, and conditions for persistence or recoverability**. A universal closed equation with the empirical standing of Navier–Stokes is not presently established. The strongest contribution would specify when changes that spread also maintain or enlarge the capacities needed for subsequent action, reproduction, learning, and legitimate revision—and identify interventions that reverse their erosion.

Do not make a universal optimizer the foundation. Frequency-dependent selection can cycle. Deliberation, habit, coercion, and imitation do not generally implement payoff-gradient ascent. Regeneration can coexist with competitive behavior; apparent cooperation can coexist with impending extinction. The theory should explain these cases rather than define them away.

## 1. A disciplined common architecture

Let \(n_i\) count carriers of a specified type, \(R\) record supporting stocks and capacities, and \(S\) record selection-relevant rules or interactions. A useful finite-type starting point is

\[
\dot n_i=n_i r_i(n,R,S)+\sum_j(q_{ji}n_j-q_{ij}n_i)+I_i,
\qquad \dot R=F(n,R,S,u),\qquad \dot S=H(n,R,S,u).
\]

The transition rates \(q_{ij}\ge0\) represent type change without reproduction; \(I_i\) represents external entry. Reproductive mutation belongs in a birth kernel when offspring production, rather than carrier conversion, is the mechanism. Learning, migration, imitation, birth, and organizational replacement must not silently become the same event. For finite populations, specify the corresponding stochastic process before taking deterministic limits.

This approach has direct mathematical precedent. [Champagnat, Ferrière, and Méléard](https://arxiv.org/abs/math/0510453) derive contrasting macroscopic limits from individual birth, death, mutation, and interaction processes. Different assumptions yield different deterministic or stochastic equations. That is a model for methodological rigor, not evidence that a single constitutive law transfers to every domain.

With no entry and conservative type transitions, \(N=\sum_i n_i\) obeys \(\dot N=N\bar r\). If transitions are absent too, \(p_i=n_i/N\) obeys \(\dot p_i=p_i(r_i-\bar r)\). A common additive loss in all \(r_i\) cancels from frequency dynamics but affects abundance. Consequently, selection data alone cannot identify collective flourishing.

Resource effects normally scale with exposure:

\[
\dot R_k=A_k(R,u)+N\sum_i p_i\,[P_{ik}(R,S)-C_{ik}(R,S)].
\]

Here production and consumption have stock-per-carrier-per-time units. Omitting \(N\) assumes a fixed population, normalized exposure, or an explicit compensating mechanism. A million identical carriers need not have the same material effect as ten. Stocks, flows, capacities, information, and legal rights need distinct units and production relations. An environmental variable that also changes selection can appear in both causal roles without duplicating it as two independent states.

## 2. Three operational cases

| Requirement | Biology: yeast public goods | Human institutions: repeated resource governance | AI: deployment and evaluator succession |
|---|---|---|---|
| Carrier and unit | Cells per culture volume, with producer/nonproducer genotypes | Users' practice choices; organizational lineages only if entry, exit, and inheritance are observed | Deployed policy instances or an explicitly measured allocation share |
| Transmission/change | Cell division with inherited genotype; mutation or experimental mixing | Adoption, imitation, deliberation, membership turnover, rule amendments | Replication, replacement, training, selection of descendants, changed allocations |
| Supporting conditions | Usable sugar, producer density, supplied medium, dilution regime | Resource stock, maintained infrastructure, monitoring competence, access and authority | Compute/energy budget, task environment, independent evidence, human correction competence and authority |
| Feedback to selection | Producer density changes the return to producing or using public goods | Actions change stocks; success can change rules, access, or enforcement | Deployed agents change data and task environment; successful lineages may influence subsequent evaluation |
| Independent outcomes | Absolute density, recovery following perturbation, extinction | Sustainable yield, infrastructure recovery, distribution of costs, successful legitimate appeals | Task utility on independent tests, repair success under adverse evidence, actual implementation of authorized correction |

**Biological anchor.** [Sanchez and Gore's 2013 yeast experiment](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001547) is unusually well matched. It follows population and allele trajectories across generations, rather than inferring attractors from snapshots. Small populations can collapse while producer frequency increases. Producer/nonproducer coexistence can retain similar equilibrium density while reducing resilience. This supplies two crucial counterexamples: increasing cooperation frequency does not guarantee regeneration, and nonproducers do not necessarily cause collapse. Use this as the first biological calibration; a cancer extension needs its own cell-state, tissue, treatment, and host measurements.

**Human anchor.** [Ostrom, Walker, and Gardner's experiments](https://www.wtf.tw/ref/ostrom_1992.pdf) manipulate communication and sanctioning in common-pool allocation. They provide primary precedent for testing institutional mechanisms rather than assuming externally enforced punishment is necessary. Their experiment is not itself a demonstration of every proposed stock-regeneration or evaluator-capture loop. A new longitudinal resource experiment should measure practice transitions directly and fit an adoption rule; a replicator equation requires evidence, not the label “competition.” People are rights-bearing participants, not morally ranked reproductive types.

**AI anchor.** [Performative prediction](https://proceedings.mlr.press/v119/perdomo20a.html) formalizes predictions changing the distribution on which future prediction is trained. It supplies one feedback mechanism, not a complete theory of institutional succession or regeneration. Distinguish weight updates inside one model from selection among deployed models. Compute shares obey allocation mechanisms, not biological birth laws. The proposed evaluator-succession benchmark is a new experiment, not an established empirical analogue of the yeast study.

## 3. What would constitute a cross-domain result?

There are three increasingly demanding claims:

1. **Shared vocabulary:** all systems have entities and environments. This has little predictive content.
2. **Conditional mathematical homology:** after explicit mapping of units, events, and timescales, systems satisfy the same restricted model family. A theorem then applies to every verified member.
3. **Transportable causal prediction:** an intervention on a mapped mechanism predicts out-of-sample changes across settings, with domain-specific parameters estimated independently.

The third is the valuable target. Similar sigmoid curves or phase portraits establish neither mechanism nor transportability. A defensible claim could be: lowering the appropriability of evaluator amendments reduces their selective benefit, under independently verified transmission and cost conditions. A false claim would be: all hierarchical institutions follow one capture law.

The existing [v6.2 section 4](../../../drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/40_s4.md) already specifies appropriability, persistence, cost, inheritance, and the two factors yielding a squared-share return. Preserve those restrictions. Its power-law cost and adaptation assumptions determine its correction-rate threshold; an integrated framework should expose that special case rather than promote its exponent to a universal constant.

## 4. Foundational failure modes and repairs

**Conservation versus reproduction.** Carrier number, institutional authority, and useful information are not conserved fluids. Conservation applies where physical accounting warrants it; birth/death and allocation require source terms. Reproduction consumes resources and dissipates energy. “Becoming” cannot be introduced as a conserved substance. Import/export terms are essential: local regeneration financed by degradation elsewhere is not net regeneration at the larger boundary.

**Closure under aggregation.** If \(X_a=\sum_{i\in a}n_i\), then \(\dot X_a=X_a\bar r_a\), but the group's average rate depends on its internal composition. Identical observed \((X,R,S)\) can have different futures. Either retain sufficient hidden states, justify fast equilibration, or include memory/noise with quantified prediction error. Test closure by asking whether history predicts changes after conditioning on the proposed state.

**Timescales and path dependence.** Ecological recovery, institutional skill acquisition, influence accumulation, and learning can occur at different rates. A quasi-static equilibrium approximation fails during rapid change. Estimate recovery delays and test interventions at several durations. Hysteresis requires different outcomes after matched parameter reversal; persistence after a short intervention alone could instead reflect slow relaxation. A local attractor need not be globally reachable, and an asymptotic safe state can be reached only after an unacceptable transient.

**No inevitable scalar gradient.** Coupled game–environment models already admit oscillatory and other regimes: [Weitz et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/) is a primary example. A Lyapunov function, when one exists, certifies behavior of the stated dynamics; it is not automatically welfare. A relative-fitness optimum can coexist with deterioration in shared support. Non-gradient dynamics are not a defect to remove from the theory.

**Regeneration is relational and boundary-dependent.** Predeclare what capacities are replenished, for whom, over what horizon, and against which disturbances. Abundance, diversity, persistence, recovery speed, and accessible future actions can disagree. A tumor can regenerate while its host degenerates. Institutional stability can preserve oppression. Do not conceal such conflicts inside a weighted score.

**Normative universalization.** Separate descriptive support conditions from ethically justified protected conditions. In human/AI applications, specify rights, standing, legitimate authority, contestability, and whose losses count. Their justification does not follow from biological reproduction. Continued correction must permit legitimate revision of purposes, not merely enforce a permanent evaluator's preferences. The seven-gauge corpus can supply proposed commitments, not a theorem that nature endorses them.

**Open-endedness.** A finite fixed type list cannot express indefinitely growing structural novelty. A fixed grammar of arbitrarily large programs, graphs, or genomes can, in principle, represent an unbounded space; novelty need not lie outside every predeclared mathematical state space. The scientific problem is how accessible forms and functions change, how their carriers remain interpretable, and how novelty is distinguished from noise. [Taylor 2018](https://arxiv.org/abs/1806.01883) provides a useful prior-art taxonomy. Do not equate mutation rate or diversity entropy with meaningful innovation.

## 5. Identification and falsification

The minimum dataset records absolute exposure, composition, support stocks, rule changes, observed transitions, and intervention timing. Separate latent states from measurements, for example \(y_t=h(R_t,S_t)+\epsilon_t\). A better reported score can arise from better conditions or altered reporting. Include independent channels and identical-item rescoring to identify the distinction.

For evaluator succession, retain four arms: fixed rules; endogenous amendment; exogenous replay of comparable amendments; and randomized or rotating amendment authority. Include amendments that legitimately improve evaluation, so every change is not defined as capture. Measure performance and access to correction independently of the contested rubric. Randomize authority separately from resources where feasible; otherwise talent, scale economies, or ordinary data shift can explain success-associated rule changes.

For regeneration, independently perturb support and composition. Vary initial total abundance at matched frequencies; vary support stock at matched population; withdraw maintenance; restore maintenance at different delays. Estimate the two causal directions separately before claiming a feedback loop. Predict withheld trajectories and intervention responses rather than merely fitting observed decline. Compare against models with exogenous deterioration, fixed rules, no feedback, and hidden-state memory. Spatial assortment, migration, and external subsidies are important alternatives to a well-mixed feedback account.

The local [pilot record](../../../drafts/2026-10-02-iaseai-selecting-the-selectors/experiment/PREDICTIONS-2.md) must remain visible: across 20 seeds, P1 failed because mean influence capacity did not fall in REPLAY or FAST; P2–P4 held. The record identifies drift and quality variation as possible explanations and specifies design 2. This audit neither reran the pilot nor verified a design-2 result. A redesign may diagnose the failure; it cannot retroactively count the first prediction as confirmed.

## 6. Contribution priorities and boundaries

Existing work occupies much of the broad synthesis. [Incomplete contracting and alignment](https://arxiv.org/abs/1804.04268) already joins economic misalignment with supporting institutions. [Harré 2025](https://arxiv.org/abs/2507.13616) explicitly combines institutional evolution, multilevel selection, and AI governance. Its advertised mathematical results require separate proof audit; proximity is enough to constrain broad novelty claims, not to establish their validity. The [earlier contribution assessment](../../../sources/15-codex-theory-conversations/2026-10-04-alignment-coordination-contribution-space.md) identifies further corrigibility and institutional-dynamics precedents.

Prioritize these questions:

1. **Minimum sufficient state:** what observations distinguish systems with equal competitive success but different recoverability? Prove an identifiability limit from frequencies alone; test the added value of abundance, support, authority, and memory.
2. **Persistence of regenerative and corrective capacity:** derive conditions when selection preserves a viable set while the mechanisms financing and authorizing repair themselves evolve. Supply both successful and failed regimes.
3. **Intervention transport:** which dimensionless mechanism ratios predict comparable treatment effects in microbial, human experimental, and AI systems? Transfer a restriction, not an unmeasured coefficient.
4. **Feasible transition:** can a system reach the protective regime before inherited damage or depleted authority makes it inaccessible? Include costs, delay, and distribution of burdens.
5. **Innovation without closure:** can protected revision and experimentation expand useful reachable capabilities while maintaining justified floors? Begin with an explicitly bounded structural-innovation model; defer universal claims.

The defensible foundational ambition is a theory of **selection coupled to the production, depletion, and revision of its enabling conditions**, with explicit domains of validity. Its contribution will be measured by restrictions and predictions that survive counterexamples—not by the number of domains to which its notation can be attached.
