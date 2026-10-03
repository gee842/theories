# v5 evidence register

Companion to [THEORY.md](THEORY.md) and [CLAIMS.md](CLAIMS.md). Each row ties a premise of the situated diagnosis to dated sources. The premises are that the winning model Ψ governs (THEORY Definition 1.1), that it is false, the components of its three signatures W, C and N, and the hazard premises of THEORY §5.4. Each row gives supporting and contrary findings, competing explanations, uncertainty, what the row does to the recommendation, and the next measurement.

**How the sources were checked.** Rows marked *checked 2026-10-03* were retrieved during this pass, from the primary source where it was reachable, and otherwise from a secondary report that quotes it. Rows marked *carried* come from the v4.5 reviews, which checked them on the same date, and were not re-fetched. Rows marked *from prior knowledge* were not re-fetched and must be checked before public use. Declared positions establish what an actor says, not what it does. Nothing here is a measurement of a model parameter unless it says so.

**What the register cannot yet support.** No row measures the variety of hazardous behaviour, the residual probability of an irreversible loss after correction, or the conversion of success into control over evaluators. Those are the central cruxes, and THEORY §9 treats them as such.

---

## E1. Declared strategic objectives (W; Ψ governs)

- **Premise.** Strategic success is defined substantially by relative or decisive advantage.
- **Indicator.** The objectives leading states and developers state in their own plans.
- **Sources.**
  - America's AI Action Plan, White House, 23 July 2025. It frames policy as "winning the AI race" and ensuring "U.S. dominance in artificial intelligence". Its three pillars are accelerating innovation, building infrastructure, and international diplomacy and security. *Checked 2026-10-03* ([White House](https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan/)).
  - Executive Order "Ensuring a National Policy Framework for Artificial Intelligence", 11 December 2025. It states a policy to sustain and enhance the country's global AI dominance through a minimally burdensome national framework. *Checked 2026-10-03* through law-firm summaries quoting the order ([Sidley](https://www.sidley.com/en/insights/newsupdates/2025/12/unpacking-the-december-11-2025-executive-order); [DLA Piper](https://www.dlapiper.com/en-us/insights/publications/2025/12/new-executive-order-aims-to-preempt-state-ai-regulation)).
- **Contrary.** China's Global AI Governance Action Plan of 26 July 2025 stresses international cooperation and capacity building for developing countries. It proposes a scientific panel and a global dialogue under the UN, with "向善为民" as a principle. *Checked 2026-10-03* ([MFA](https://www.mfa.gov.cn/wjb_673085/zzjg_673183/xws_674681/xgxw_674683/202507/t20250726_11677803.shtml)). Declared cooperative aims coexist with national development and security goals, and neither document shows behaviour.
- **Competing explanations.** Race language can be rhetoric for domestic audiences. It can also be a response to a rival's perceived race, which is the same objective by reflection, not a separate cause.
- **Uncertainty.** These are declared positions of particular governments at particular dates. They do not cover every state or firm.
- **Effect on the recommendation.** Supports the objective of W, and the claim that Ψ governs, for at least one leading state's declared objective. The vocabulary of winning and dominance is Ψ applied to AI (THEORY §1.5). It does not establish that resources move by that objective (E2 bears on that).
- **Next measurement.** Allocations and decisions when rank and safety conflict: budgets, export and compute policy, release decisions.

## E2. Safety commitments contingent on rivals (the tempo of W; N)

- **Premise.** Developers accelerate, or relax safeguards, when rivals advance; unilateral restraint is treated as unrealistic.
- **Indicator.** Clauses in frontier safety frameworks that condition requirements on competitors' conduct; how the frameworks change between versions.
- **Sources.**
  - OpenAI Preparedness Framework, version 2, 15 April 2025. It states that if another frontier developer releases a high-risk system without comparable safeguards, the company "may adjust our requirements". It conditions this on first rigorously confirming that the risk landscape has changed and publicly acknowledging the adjustment. *Checked 2026-10-03* through the framework's announcement as quoted in search results; the PDF itself could not be parsed ([framework PDF](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)).
  - Anthropic Responsible Scaling Policy, version 3.0, effective 24 February 2026, revised through version 3.4 during 2026. An independent analysis reports four changes:
    - earlier language implying a pause when risks were unacceptably high was removed;
    - commitments were split into modest unilateral ones and conditional "industry-wide recommendations";
    - demanding security levels now appear only among the recommendations;
    - risk reports and a safety roadmap were added, largely self-assessed.

    The policy's "in the lead" scenario commits to delay "until and unless we no longer believe we have a significant lead". *Checked 2026-10-03* ([policy v3.0](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0); [GovAI analysis](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections)).
  - Zhu, "Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers", arXiv:2609.08789, 8 September 2026. It covers every public version of the frameworks of the twelve developers that have published one: 710 commitment instances across twelve consecutive version pairs. Of the traced changes, 77% weakened or removed commitments. Of material changes, 67% were undisclosed under strict criteria (53% under lenient ones), and weakened commitments were more often silent than strengthened ones in seven of eight version pairs. *Checked 2026-10-03* (abstract) ([arXiv](https://arxiv.org/abs/2609.08789)). It is a single-author preprint and has not been peer reviewed.
- **Contrary.** The frameworks exist, are published, and include some strengthening. Their authors argue that a unilateral pause while others proceed would not reduce risk. That argument is itself an instance of the coordination failure the theory describes, but it is also a sincere and partly correct claim about unilateral restraint (THEORY Prop 7.3).
- **Competing explanations.** Better risk assessment can legitimately relax a requirement. A weakening is evidence of competitive pressure only where the stated reason is rivals' conduct or time to market.
- **Uncertainty.** The study's classification of "weakened" is the author's coding. The framework clauses state permissions, not exercised decisions.
- **Effect on the recommendation.** Strong support for the tempo of W, and for the treatment of restraint as unrealistic (N), at the level of written commitments. It is the most direct current evidence that safety terms are set relative to rivals.
- **Next measurement.** Whether the competitor clauses have been invoked; release timing against rivals' releases; changes in evaluation windows before deployment.

## E3. Oversight institutions' mandates and dependence (C)

- **Premise.** Oversight depends on the resources, access or priorities of those it oversees, and its mandate moves with the field's success.
- **Indicator.** Mandates, names, funding and access arrangements of public evaluation bodies; arrangements that pre-empt or restrict other rule-makers.
- **Sources.**
  - The US AI Safety Institute was replaced by the Center for AI Standards and Innovation, announced 3–6 June 2025. It is described as "industry's primary point of contact" within government for testing and collaborative research, under voluntary agreements with developers. *Checked 2026-10-03* through reports ([FedScoop](https://fedscoop.com/trump-administration-rebrands-ai-safety-institute-aisi-caisi/); [SSTI](https://ssti.org/blog/us-ai-safety-institute-has-been-renamed-center-ai-standards-and-innovation)).
  - The UK AI Safety Institute was renamed the AI Security Institute in February 2025. *From prior knowledge*.
  - The December 2025 executive order set up a litigation task force to challenge state AI laws and conditioned some federal funding on states' AI laws, with carve-outs. *Checked 2026-10-03* (as E1).
  - A proposed ten-year moratorium on state AI laws was removed from a federal bill by a 99–1 Senate vote in July 2025. *From prior knowledge*.
- **Contrary.** Pre-deployment testing by public institutes continues under voluntary agreements. A national framework can be argued for on grounds of coherence rather than capture. Removing the moratorium is evidence that rule-makers can resist pre-emption.
- **Competing explanations.** Changes of administration and of security priorities; legitimate federal uniformity; scarce expertise outside the developers.
- **Uncertainty.** None of this meets the capture criterion of THEORY Definition 3.3, which needs an entrusted purpose shown to be impaired. It shows mandates and pre-emption moving in the direction the field prefers.
- **Effect on the recommendation.** Partial support for the dependence of oversight in C. It is consistent with the mechanism of §3 but does not identify it.
- **Next measurement.** Access terms (who sets evaluation windows), funding sources of evaluators, staff flows between developers and evaluators, outcomes of pre-emption litigation.

## E4. Reinvestment of success in influence over rules (C)

- **Premise.** Success is reinvested in influence over evaluation and rules.
- **Indicator.** Lobbying and policy spending by frontier developers; participation in standards; developer-authored benchmarks and evaluation tooling.
- **Sources.** No source was retrieved in this pass. v4.5 cited developer-owned benchmarks and evaluation tooling (Perez et al. 2023, model-written evaluations) and fixed-cost lobbying (Bombardini 2008). *Carried*.
- **Effect on the recommendation.** This part of C is the most important link to the mechanism of §3 and the least evidenced in this register. It is a central gap.
- **Next measurement.** Lobbying disclosures by year and firm; authorship of standards drafts; the share of evaluation compute and benchmarks funded or built by evaluated developers (THEORY §3.8).

## E5. Capability growth (context for (X))

- **Premise.** Capability compounds.
- **Indicator.** Task-length horizons; training compute.
- **Sources.**
  - METR, "Measuring AI Ability to Complete Long Tasks", arXiv:2503.14499, March 2025: the frontier time horizon doubled about every seven months over 2019–2025. METR's Time Horizon 1.1, 29 January 2026, estimates a post-2023 doubling time of 131 days, against 165 days under the earlier suite. *Checked 2026-10-03* ([METR](https://metr.org/blog/2026-1-29-time-horizon-1-1/)).
  - Epoch AI: training compute of frontier models grew 4–5× a year from 2010 to May 2024, and about 5× a year for frontier language models since 2020. *Checked 2026-10-03* ([Epoch](https://epoch.ai/publications/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year)).
- **Contrary.** Capabilities are "jagged" (E7). Horizons are measured at a fixed success rate on specified task suites.
- **Effect on the recommendation.** Supports compounding capability (X1). It does **not** measure the variety of hazardous behaviour $Y$ or the growth of residual risk. The step from capability to $Y$ is premise (X2), which remains a conjecture.
- **Next measurement.** Predefined hazard modes per class, and how many of them each model generation exhibits.

## E6. Evaluation awareness and masking (Section 3.4)

- **Premise.** Evaluated systems can distinguish evaluation from deployment, which lets evaluation results mask behaviour.
- **Sources.** Needham, Edkins, Pimpale, Bartsch and Hobbhahn, "Large Language Models Often Know When They Are Being Evaluated", arXiv:2505.23836, May 2025. On 1,000 transcripts from 61 datasets, frontier models classified evaluation against deployment above chance (best AUC 0.83 against a human baseline of 0.92), better in agentic settings. *Checked 2026-10-03* ([arXiv](https://arxiv.org/abs/2505.23836)). Later work on evaluation awareness exists, for example EvalDetectBench, arXiv:2609.01611 (title seen, not read).
- **Contrary.** Awareness is not yet above human level in that study. Awareness does not imply strategic behaviour, its frequency, or its consequences.
- **Effect on the recommendation.** Supports the existence of the channel $\beta_{\text{model}}$ of THEORY §3.5. It does not support a permanent lower bound on residual risk.
- **Next measurement.** Behaviour differences between detected-evaluation and deployment conditions; success rates of probes that suppress awareness.

## E7. The state of the science on risk and safeguards (Section 5.4)

- **Premise.** Correction is incomplete for at least some hazard classes.
- **Source.** International AI Safety Report 2026, published 3 February 2026. It was led by Yoshua Bengio with an expert advisory panel nominated by more than 30 countries. Capabilities continued to improve, especially in mathematics, coding and autonomous operation, and remain jagged. Risks fall into malicious use, malfunction and systemic risks. Technical safeguards alone have significant limits, and the report recommends defence in depth. *Checked 2026-10-03* through summaries ([report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)).
- **Effect on the recommendation.** Supports the claim that correction is incomplete, which is a premise of urgency. It does not quantify residual risk (φ).
- **Next measurement.** Hazard-specific coverage, detection time, decision time, execution and residual risk, per class.

## E8. Cooperative initiatives and their limits (N, and the transition)

- **Premise under test.** Collective restraint and shared provision are treated as unrealistic (N). Contrary evidence weakens the uniform description of the trajectory and identifies seeds of the transition.
- **Sources.**
  - The UN General Assembly adopted A/RES/79/325 by consensus on 26 August 2025. It established an Independent International Scientific Panel on AI (40 experts, an annual summary report) and a Global Dialogue on AI Governance among 193 member states. *Checked 2026-10-03* ([Simon Institute](https://simoninstitute.ch/blog/post/adoption-of-the-independent-international-scientific-panel-on-ai-and-the-global-dialogue-on-ai-governance); [Wikipedia](https://en.wikipedia.org/wiki/Independent_International_Scientific_Panel_on_AI)).
  - Two leading states affirmed "the need to maintain human control over the decision to use nuclear weapons" at their leaders' meeting in Lima on 16 November 2024. *Checked 2026-10-03* ([NPR](https://www.npr.org/2024/11/16/nx-s1-5193893/xi-trump-biden-ai-export-controls-tariffs); [CNBC](https://www.cnbc.com/2024/11/17/biden-xi-agree-that-humans-not-ai-should-control-nuclear-arms.html)).
  - On 24–25 September 2026 the same two states agreed a "Super Intelligence Dialogue" on risks and benefits, with a next meeting by November 2026, and a bilateral channel for AI incidents. The agreement creates no binding obligation, standard or limit on development. A senior official stated that international dialogue "cannot be allowed to drift toward global governance". *Checked 2026-10-03* through reports ([The Next Web](https://thenextweb.com/news/us-china-super-intelligence-dialogue-ai-incident-channel); [UPI](https://www.upi.com/Top_News/US/2026/09/26/White-House-Trump-Xi-agree-super-intelligence-dialogue/1951790465468/)).
  - At the Paris AI Action Summit, February 2025, about 60 states signed a statement on inclusive and sustainable AI; two leading Western states did not sign. *Checked 2026-10-03* ([CNBC](https://www.cnbc.com/2025/02/11/us-and-britain-snub-international-ai-accord-in-paris.html)).
- **Reading.** The evidence cuts both ways.
  - It contradicts a uniform arms-race description. Shared assessment (the UN panel), a narrow strategic commitment (human control of nuclear use) and an incident channel exist, and the leading rivals are in direct dialogue on superintelligence risk.
  - It also shows binding constraints explicitly rejected at the same moment, which is N in its sharpest form.
- **Effect on the recommendation.** These are the first stages of the transition of THEORY §8 (shared diagnosis, narrow verifiable commitments, incident channels). The recommendation is not that cooperation must start from nothing; it is that these seeds be made binding, verifiable and broader before lock-in.
- **Next measurement.** Whether the dialogue produces shared measurement, joint evaluations or commitments with verification; whether the incident channel is used.

## E9. Algorithmic efficiency and compute thresholds (Section 8.3)

- **Source.** Ho et al. 2024, "Algorithmic progress in language models": compute efficiency in pre-training doubles roughly every eight months. *Carried* (from the AI-safety review of v4.4).
- **Effect on the recommendation.** Thresholds stated in compute erode; a nominal cap must tighten by roughly 2.5–3× a year to hold a capability line. That is a rate condition on verification, not a refutation of it.

## E10. Plan A of AI 2040: figures used in the symmetric stress tests (Section 6.8)

- **Sources.** *AI 2040: Plan A* and its supplements, AI Futures Project, 2026. The handoff review checked the following on 2026-10-03 ([Deal Decline](https://ai-2040.com/supplements/deal-decline); [Comparing Possible Plans](https://ai-2040.com/supplements/comparing-possible-plans); [Capability Scaling Strategy](https://ai-2040.com/supplements/capability-scaling-strategy)). *Carried.*
  - The source distinguishes decline, dissolution and impairment. In one author's scenario judgment, decline in years five to ten runs at about 4% a year, of which about 2% is dissolution and 2% impairment. Cumulative decline over ten years is about 48%, not near certainty.
  - Handoff decisions weigh the marginal value of further alignment research against other risks, and the plan keeps an option of a longer pause.
  - On the authors' median estimates, a leader spending its lead (Plan C) buys a reduction in takeover risk of about $(0.40-0.25)/(0.72-0.25)\approx0.32$ of what a coordinated slowdown (Plan A) buys, both relative to racing (Plan D).
- **Effect on the recommendation.** The figures are scenario judgments, not observed frequencies. v5 uses them only to show how the durability tests apply, and applies the same tests to its own design.

## E11. Experimental and theoretical evidence on racing behaviour

- Fernández Domingos and Han, arXiv:2607.26034, 2026. In an idealized laboratory race, falling behind drove unsafe choices, while the stated level of shared risk (10% to 90%) changed them little. *Carried.* This is a caution for THEORY §8: changing the prediction may not be enough.
- Fudenberg and Koh, "Cooperating against Catastrophe", arXiv:2609.28291, 2026. In a capability race with a linearly advancing safety frontier, the regions are racing only, coexistence, and pacing only; with high effective hazard, pacing can be the unique Markov perfect equilibrium without agreement. *Carried.* This is a counter-regime: bounded competition that paces itself. THEORY §6.2 asks whether its conditions hold on the present path.
- Bueno de Mesquita, Dziuda and Polborn, NBER Working Paper 35276, 2026: fragmentation raises speed and conditional risk, and committing to slow can pay because rivals slow too. *Carried*; the number was checked by the handoff review.

## E12. The author's own experiment

- One 20-seed pilot of the rubric-editing experiment ran on 2 October 2026 ([PREDICTIONS-2.md](../experiment/PREDICTIONS-2.md)).
- P2–P4 held. P1 failed: mean control capacity rose in the closed arm (0.500 to 0.675), but did not fall in two of the comparison arms; every arm's 95% interval was about ±0.14.
- The failure is attributed to winner-take-all among too few lineages, decided mostly by quality differences and drift. That is a diagnosis of the design, not a vindication of P1.
- Design 2 is pre-specified and has not been run.
- **Effect on the recommendation.** No experimental support for the mechanism of §3 yet. The mechanism rests on the proof of Prop 3.4 and on institutional evidence (E3, E4).

## E13. Interdependence in the supply chain of the raced technology (Ψ is false: material)

- **Premise.** No one wins the supply chain of the raced technology alone, so Ψ3's alternative of winning or being dominated misdescribes the situation: the winner still depends on those it would dominate.
- **Indicator.** Whether any actor can complete the supply chain of advanced semiconductors alone, and at what cost.
- **Source.** Semiconductor Industry Association and Boston Consulting Group, "Strengthening the Global Semiconductor Supply Chain in an Uncertain Era", 1 April 2021. No company or country can achieve self-sufficiency in semiconductors. Fully self-sufficient local supply chains in each region would need at least $1 trillion of incremental up-front investment and raise semiconductor prices by 35% to 65% overall. *Checked 2026-10-03* through the study's summary and its press release ([SIA summary](https://www.semiconductors.org/wp-content/uploads/2021/03/SIA-BCG_Global-Value-Chain_2-pager.pdf); [SIA release](https://www.semiconductors.org/study-identifies-benefits-and-vulnerabilities-of-global-semiconductor-supply-chain-recommends-government-actions-to-strengthen-it/)).
- **Contrary.** Since 2021 several states have subsidized domestic fabrication, and the degree of interdependence is a policy target. An industry association has an interest in open supply chains.
- **Competing explanations.** Interdependence can be read as vulnerability to be reduced rather than as a fact to be counted. Both readings agree that it exists now.
- **Uncertainty.** A 2021 estimate; the figures are scenario estimates by the industry and a consultancy.
- **Effect on the recommendation.** Supports the claim against Ψ3. Interdependence through trade is settled by prices and is compatible with selfish actors. It does not by itself establish $\kappa>0$ in the sense of THEORY §2.5, which counts coupling that prices do not settle: shared hazards, propagation of failures through concentrated nodes, and systemic risk (E7).
- **Next measurement.** Concentration of each stage of the AI supply chain (equipment, fabrication, materials, chips, compute, data, talent), the cost of duplicating each, and how disruptions at one node propagate to others. The last of these measures unpriced coupling.

## E14. Behaviour against the self-interest model, and performativity (Ψ is false: behavioural; Ψ governs: performativity)

- **Premise.** Human beings are not Ψ1 actors, and models of behaviour can make themselves true.
- **Sources.**
  - Henrich, Boyd, Bowles, Camerer, Fehr, Gintis and McElreath, "In Search of Homo Economicus: Behavioral Experiments in 15 Small-Scale Societies", *American Economic Review* 91(2), 2001. The canonical self-interest model was not supported in any society studied. Group differences in market integration and in the payoffs to cooperation explained much of the variation: the more integrated and the higher the payoffs, the more cooperation. *Checked 2026-10-03* ([AEA](https://www.aeaweb.org/articles?id=10.1257%2Faer.91.2.73)).
  - Fischbacher, Gächter and Fehr, "Are People Conditionally Cooperative? Evidence from a Public Goods Experiment", *Economics Letters* 71(3), 2001. About a third of subjects were free riders and 50% conditional cooperators. *Checked 2026-10-03* ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0165176501003949)).
  - Frank, Gilovich and Regan, "Does Studying Economics Inhibit Cooperation?", *Journal of Economic Perspectives* 7(2), 1993. Economics students defected more often in a prisoner's dilemma, with evidence that training contributes. *Checked 2026-10-03* (abstract and summaries) ([AEA](https://www.aeaweb.org/articles?id=10.1257%2Fjep.7.2.159)).
  - Ferraro, Pfeffer and Sutton, "Economics Language and Assumptions: How Theories Can Become Self-Fulfilling", *Academy of Management Review* 30(1), 2005. Theories become self-fulfilling through institutional design, social norms and language. *Checked 2026-10-03* ([PDF](https://jeffreypfeffer.com/wp-content/uploads/2019/10/AMR-Jan2005-econ-lang-23.pdf)).
- **Contrary.** Free riders exist in every population studied, and cooperation decays in repeated public-goods games without punishment. Part of the gap between economics students and others may be self-selection, and a later study, "Does Studying Economics Discourage Cooperation? Watch What We Do, Not What We Say or How We Play" (*Journal of Economic Perspectives* 10(1), 1996), disputes the inference from laboratory play (title seen, not read).
- **Competing explanations.** Cooperation in experiments may reflect norms imported from daily life, which is consistent with the claim that institutions shape behaviour.
- **Uncertainty.** Laboratory and field-experiment evidence; the actors in AI development are organizations as well as persons.
- **Effect on the recommendation.** Supports the claims that Ψ1 is not a law of human nature. Henrich et al.'s association of market integration with more cooperation means the target is Ψ's reading of markets, not markets (THEORY §1.4). It also supports the claim that the share of conditional cooperators makes cooperation reachable when others are seen to cooperate (THEORY §8). It supports performativity as a mechanism by which Ψ maintains itself.
- **Next measurement.** Conduct of AI organizations under institutional changes that make others' cooperation visible.

## E15. The history of the governing vocabulary (Ψ governs: history)

- **Premise.** Over half a century, institutional criteria moved toward Ψ, and the present vocabulary of AI policy applies Ψ to a new technology.
- **Sources.**
  - Friedman, "The Social Responsibility of Business Is to Increase Its Profits", *New York Times Magazine*, 13 September 1970. *Checked 2026-10-03* ([text](https://public.websites.umich.edu/~thecore/doc/Friedman.pdf)).
  - Jensen and Meckling, "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure", *Journal of Financial Economics* 3(4), 1976. *Checked 2026-10-03* ([RePEc](https://ideas.repec.org/a/eee/jfinec/v3y1976i4p305-360.html)).
  - Business Roundtable. Each version of its statement on corporate governance from 1997 endorsed shareholder primacy, stating that "the principal objective of a business enterprise is to generate economic returns to its owners". On 19 August 2019 it issued a Statement on the Purpose of a Corporation, signed by 181 chief executives, committing to all stakeholders. *Checked 2026-10-03* ([Business Roundtable](https://www.businessroundtable.org/business-roundtable-redefines-the-purpose-of-a-corporation-to-promote-an-economy-that-serves-all-americans); [Harvard Law School Forum](https://corpgov.law.harvard.edu/2019/08/22/so-long-to-shareholder-primacy)).
  - Harvey, *A Brief History of Neoliberalism*, Oxford University Press, 2005: where neoliberalization came from and how it spread globally. *Checked 2026-10-03* (bibliographic record and reviews).
  - E1 for the vocabulary of winning and dominance in AI policy.
- **Contrary.** Friedman's essay bounds profit-seeking by "the rules of the game". THEORY §1.5 treats that qualification as the doctrine's strongest form and locates its failure in signature C: when success buys influence over the rules, the bound no longer binds. The 2019 revision, and assessments of whether it changed practice, show contestation within the same institutions. Neoliberalism is a contested term, and the policy turn varied across countries. Darwin, Smith, Kropotkin, Polanyi and Ostrom belong to the same intellectual history and criticize the model (THEORY §1.5).
- **Competing explanations.** Shareholder primacy can be defended as a solution to agency problems rather than as an endorsement of greed. Read that way, it is still a choice of objective that counts only one party's payoff, which is Ψ1 at the level of the firm.
- **Uncertainty.** A history of ideas and declared criteria, not a measurement of conduct. It concerns firms in general. For AI organizations specifically, the direct evidence is the declarations of E1 and the framework clauses of E2.
- **Effect on the recommendation.** Supports the claim that Ψ governs through institutional criteria and narratives, and that it has a history, which means it can change. It does not single out any state or firm; Ψ is held, in some measure, by actors of every origin.
- **Next measurement.** Objectives written into the charters, incentive contracts and evaluation criteria of AI organizations and agencies.

## E16. The status drive and its two routes (Ψ governs: the status drive)

- **Premise.** The desire for status is a fundamental motive, and status can be gained by dominance or by prestige.
- **Sources.**
  - Anderson, Hildreth and Howland, "Is the Desire for Status a Fundamental Human Motive? A Review of the Empirical Literature", *Psychological Bulletin*, 2015. The importance of status was observed across cultures, genders, ages and personalities. Status is respect, admiration and voluntary deference, distinct from power, financial success and belonging. *Checked 2026-10-03* (summaries) ([Semantic Scholar](https://www.semanticscholar.org/paper/Is-the-desire-for-status-a-fundamental-human-motive-Anderson-Hildreth/48cd8f785a2ea53b3e537dbc7268cbfbe62b6042)).
  - Henrich and Gil-White, "The Evolution of Prestige: Freely Conferred Deference as a Mechanism for Enhancing the Benefits of Cultural Transmission", *Evolution and Human Behavior* 22(3), 2001. Prestige is an alternative route to dominance for attaining high rank. *Checked 2026-10-03* ([Harvard](https://henrich.fas.harvard.edu/publications/evolution-prestige-freely-conferred-deference-mechanism-enhancing-benefits)).
- **Contrary.** The relative weight of the two routes varies across settings, and dominance remains effective in some.
- **Effect on the recommendation.** Supports the design principle that winners be rewarded with recognition for contribution rather than with control (THEORY V5, §7). It explains why Ψ feels natural without making it true.
- **Next measurement.** How recognition is awarded in AI organizations and research: for contribution to shared provision and correction, or for rank.

---

## Gaps, in order of their effect on the recommendation

1. **Residual irreversible risk after correction, per hazard class** (φ). Nothing in this register measures it. It is the central crux of THEORY §9.
2. **Success converted into control over evaluators** (C, $b_{ij}$, $\chi$). Channels are plausible and partly visible (E3); their size is unmeasured.
3. **Coverage against hazardous variety** ($U$ against $Y$). Capability growth is measured (E5); hazardous variety and coverage are not.
4. **Allocation under conflict between rank and safety** (W in behaviour, not declaration).
5. **Performance of cooperative institutions under stress** (THEORY §7.8). Precedents exist (THEORY §8.6); no AI-specific test exists.
6. **Whether institutions widen the effective self or shrink what is contested** (THEORY Prop 1.5, crux C6). Conditional cooperation is common (E14). The conduct of AI organizations under pooling and under sharing of the contested prize is unmeasured.
