# Plan for writing v5

Prepared 3 October 2026. This is an assistant-authored proposal based on the current repository and the [supplied direction and reviews](../../sources/19-v5-handoff-2026-10-03/README.md). Ren requested a plan; this document does not start the v5 manuscript or treat instructions embedded in the attachments as new user commands.

The proposed task is to write a rigorous case for changing the present AI trajectory toward cooperation. The meta-attractor mechanism explains how a trajectory reproduces its own incentives and conditions of correction. v5 should connect that mechanism to the present situation, grant the strongest technical and institutional alternatives, and develop a cooperative path that people could actually establish and sustain. Its recommendation should be as strong as the combined reasoning and evidence support.

## Where the project stands

The current theory is [No Winning Position v4.5](v4/THEORY-clean.md), with the fuller working document and repair history in [THEORY.md](v4/THEORY.md). The manuscript in the handoff is an exact copy of the local reading version. Existing work was committed before import as `a6e63bd`.

The lineage matters. v1 and v2 developed selection over AI evaluation and cross-domain capture. The v3 plan strengthened the distinction between privately rewarded control and correction supplied as a public good; v3 and v3.1, *No Viable Race*, also widened the argument to the host, relative selection, and cooperation. v4 expanded into the nine-layer theory of shared conditions, selection, AI competition, correctors, observation, failure, trust, cooperation, and transition. v4.4 and v4.5 tried to derive stronger survival and exit conclusions, adding substantial mathematical material and further review findings.

The root [NOTES.md](NOTES.md) describes v2. [V3-PLAN.md](V3-PLAN.md) is a historical proposal. Their scope, experiment restrictions, numerical claims, and conference assumptions are not the current writing specification. The original scripts and logs are available in `build/`, `v3/`, and `v4/`; the package's reviewer checks are a separate suite. Neither numerical suite certifies all proofs or supplies empirical evidence about the world.

During this planning pass, the supplied reviewer script was rerun with Python 3.11.2, NumPy 2.4.6, and SciPy 1.17.1. Its assertions passed and output matched the archived log byte for byte. This reproduces selected numerical examples and counterexamples; it does not establish every printed analytical assertion or rerun the author's entire suite.

There is one documented 20-seed rubric-editing pilot. Its P1 prediction failed, while P2–P4 held; [PREDICTIONS-2.md](experiment/PREDICTIONS-2.md) records the result and a revised design. There is no saved run of design 2 in this project. Preserve that negative result. A proposed new experiment must not be described as completed or silently substituted for it.

The main bottleneck is the connection between the modules. A conditional selection result, a hazard model, and a model of trust do not together establish a current-world conclusion unless their quantities, assumptions, and decision criteria connect. The late v4 universal conclusions also exceed some of their premises. Changing the introduction alone would leave those problems intact.

## The argument to build

Use the brief's situated cooperative direction as the proposed organizing thesis. The argument should develop in this order:

1. Identify the actual decision: what purposes, incentives, dependencies, and correction arrangements govern consequential AI development and use, and what changing course would mean.
2. Explain recursive selection: success can finance or reproduce control over the processes that judge future success. Show when this weakens correction, when it does not, and what the existing mathematics establishes.
3. Grant perfect fidelity to human principals and continued human decision authority. Show why incompatible objectives and shared consequences can still produce a harmful game. Keep this human coordination problem central, alongside technical alignment.
4. Examine how AI changes the effectiveness, speed, reach, and reversibility of those choices, including its ability to improve independent correction. Connect each claimed gap to a specific hazard class.
5. Compare credible continuation policies with cooperative changes at common horizons and under common standards. Explain why the evidence supports the recommendation, and which disputed premises could change it.
6. Develop the positive purpose and machinery of cooperation: useful services, shared flourishing, human agency, capable authority, plural provision, correction, and a reachable transition.

The briefing's planetary purpose is a governing commitment to make explicit. Its empirical scope needs separate evidence about cross-border effects and dependencies. Shared purpose can coexist with diverse local purposes and bounded competition. Do not define every successful safeguard as a cooperative pivot after seeing its outcome.

The strongest defensible conclusion need not be a theorem of certain extinction. It must be more than a list of possible dangers. It needs a causal diagnosis, a stated decision standard, and a comparison showing why a feasible change of course addresses the consequential problems better.

## What to preserve and what to change

| Existing material | Treatment in v5 |
|---|---|
| Proposition 9 and its appendix derivation | Put selection for control near the center. Preserve appropriability, the square-of-share return, cost, horizon, variation, and transmission assumptions. A local gradient is not a full strategic equilibrium. |
| Propositions 10–11 | Retain correction as a public-good problem and the competition between control and correction rates. Preserve cases where AI-assisted correction succeeds. Repair the proposed link from human understanding to the rule-support decay rate. |
| Propositions 19–21 | Bring capture certificates, seeded cascades, reform re-absorption, and the two pause designs into the main explanatory sequence. Keep proofs and boundary conditions in the supplement. |
| Host, interdependence, masking, and delayed correction | Keep their distinct mechanisms and operational meanings. Separate loss of life, human agency, service continuity, and organizational persistence. |
| Contest, trust, and verification models | Retain valid conditional results, with timing and equilibrium concepts stated locally. Use them to identify burdens and interventions. |
| Theorems S and E and related global exclusions | Rebuild from repaired premises or replace with narrower statements. Remove unsupported universal claims where they appear, including abstracts, tables, diagrams, and conclusions. |
| Existing conditions and measurement tables | Turn Section 12 into a claim-evidence register with supporting evidence, contrary evidence, uncertainty, and causal alternatives. Indicators are not measurements. |
| Common infrastructure, public purpose, and exits | Give them comparable depth to the diagnosis. Treat authority as capable of delivering public goods and learning, with competence and failure both modeled. |

Maintain a contribution inventory for every retained formal result: statement, assumptions, proof location and status, closest predecessor, exact overlap, exact difference, and intended present-world use. Compare actual models before claiming either originality or redundancy. The reviews' thematic comparisons do not settle that question.

## The proposed manuscript structure

Write a complete theory before deciding what belongs in a conference-length derivative. A working title is *Changing the AI Trajectory: Meta-Attractors, Alignment, and Cooperation*; the final title should follow the achieved argument.

| Section | What the reader should understand by its end | Existing material and needed work |
|---|---|---|
| 1. The decision before us | The present trajectory, the proposed cooperative direction, the stakes, and the boundaries of the claim | Brief §§1–5; separate values from diagnosis and define continuation and pivot before comparison |
| 2. The system and the present trajectory | Who acts, what they share, what success allocates, and what the evidence does and does not establish | v4 §§1–2 and 12; disaggregate people, firms, states, providers, and evaluators |
| 3. How success changes future selection | Why control over evaluation can be selected and why local reforms may be absorbed | Propositions 9–11 and 19–21; contribution inventory and observed institutional channels |
| 4. Faithful AI in a harmful human game | Why perfect principal alignment and human final decisions leave a coordination problem | Brief §3A's elementary game, labeled as a standard conditional demonstration; connect it to reproduction of objectives and rules |
| 5. Capability, delegation, and effective correction | Which hazards, delays, dependencies, and irreversible losses change the practical stakes | Repaired contest, control, oversight, and survival modules; clear quantities and distinct outcomes |
| 6. The strongest case for continuing | What leadership, deterrence, technical alignment, verification, capped competition, and a finite sprint can achieve under credible conditions | Give each alternative its best case, installation path, residual risks, and evidence that could support it |
| 7. What cooperation makes possible | The useful collective purpose and the institutions that can deliver it | Financing, service obligations, access, public authority, distributed provision, evaluation, succession, and remedies |
| 8. A reachable transition and readiness to resume | The first feasible commitments, incentives, interim exposure, and what changes during a pause | A staged pathway, asymmetric participation, continuity, verification, and responses to breakdown |
| 9. The warranted decision and its cruxes | What follows now, what remains conditional, what would change the recommendation, and what to investigate next | Rewrite introduction and conclusion after the body is supported |

This preserves all nine existing layers. Trust and verification run through Sections 6–8; observation belongs with the reproduction of selection and with effective correction. Do not give every layer equal space merely to preserve the count. Keep the Chinese overview aligned with the final English argument; preserve useful Chinese conceptual material with accurate attribution.

## Repair the reasoning before carrying conclusions forward

Use the [detailed v4.5 review](../../sources/19-v5-handoff-2026-10-03/v5_0_handoff/02_theory_v4_5_deep_review_and_handoff.md) as a targeted issue list, checking each objection against the actual statement and proof. The table below records proposed work, not completed repairs.

| Issue | Required action and acceptance condition |
|---|---|
| V45-01 | Separate survival-first preferences from maxmin choice, certainty of domination, and perpetual growth. State each extra premise and apply the same preference rule to every policy compared. |
| V45-02 | Retain local risk compensation while distinguishing equilibrium branches and saturation. Do not infer a nonsummable residual hazard from it; identify independent support for any long-run hazard premise. |
| V45-03 | Specify serial, redundant, and common-cause oversight failures; compare net residual risk. A fallible corrector may still improve safety. Keep trajectory prediction distinct from invariant safety certification. Lemma D separately needs admissible variants, positive net advantage after enforcement and reliability benefits, cumulative selection, and a link to actual authority. |
| V45-04 | Use hazardous behavior Y instead of all behavior X where required. Supply regularity assumptions for local growth bounds; subexponential growth alone is insufficient. Summability does not require exact catch-up. A lower bound on risk cannot establish positive survival; that needs suitable upper control on actual residual risk. |
| V45-05 | Carry qL, speed, and horizon conditions through every delegation conclusion. Distinguish qL exactly equal to one from merely high qL; a speed cap cannot inherit an unbounded-speed conclusion. Someone losing agency does not imply each actor's survival tends to zero. Retain the valid finite-game result: at qL = 1, finite speed and positive shared survival, nondelegation strictly dominates. |
| V45-06 | Separate survival from permanent superiority. Analyze finite sprint, restraint, and preventive branches as dynamic choices unless their stronger exclusion is actually proved. |
| V45-07 | Rebuild S(3)–S(5) with one discrete or continuous risk convention, common finite horizons, and a consistent treatment of uncertainty. Two zero survival limits do not establish strict preference between them. |
| V45-08 | A proposed costly signal needs sender-type incentives, receiver beliefs, and response incentives. Near indifference by itself does not make a signal credible. |
| V45-09 | Repair interim versus ex-post incentive-compatibility claims, the multiplayer assurance threshold's interpretation, and sufficient conditions on deviation payoffs. Strict K7 requires strict participation; specify feasible shares, participation timing, and type-dependent survival. Keep verified timing and numerical results. |
| V45-10 | Convert the pseudo-solution labels into tests that also apply to the proposed cooperative institutions. Reassess source-dependent verdicts rather than inheriting them from review rhetoric. |
| V45-11 | Define a bridge between understanding coverage U and rule-support decay d, or keep them separate. Under the stated selected-control formula, check ∑pₖ^(1+2/η), the third moment for η = 1, rather than generic HHI. Fixed fragmentation can change a coefficient without changing a growth exponent. Recheck average-load claims and necessary versus sufficient control bounds. |

Maintain the review's already resolved findings as closed unless new evidence reopens them: finite-horizon mutual racing can remain a strict equilibrium; shared hazard does not remove cheap-talk bias; Proposition 24 now uses branch-specific decisive probabilities; Proposition 22 distinguishes membership-then-effort timing from deviations against fixed effort; and common-frontier existence has no general requirement that n ≥ 3 and r > 1. Preserve the history-conditional hazard premise and separate shared-failure assumption. These corrections do not close the new objections to the combined survival or policy conclusions.

Before rebuilding combined claims, use the review's counterexamples as acceptance cases. A hazardous set already covered by understanding must not generate positive guaranteed exposure merely because all behavior is larger; saturated delegation with summable residual hazards must remain possible; qL < 1 must not inherit the qL = 1 conclusion; bounded speed must not inherit an unbounded-speed limit; redundant oversight must be allowed to outperform a serial chain. Add decisive but saturating advantage and survival-first preferences without maxmin. Inspect the exact incentive and timing concepts instead of treating a reproduced number as proof of its interpretation.

At every interface, record the output quantity, units, population, timing, uncertainty, receiving premise, and whether the bridge is derived, measured, or conjectured. Prioritize capability → hazardous behavior; hazardous behavior → residual irreversible loss; understanding → executable correction; success → evaluator control; and observed danger → policy preference.

For the perfect-alignment example, grant faithful assistance without quietly weakening that grant. The stage game establishes possible collective inefficiency, not collapse. The simple cumulative-hazard proof requires a deterministic nonsummable sequence of lower bounds that holds uniformly conditional on surviving histories. A finite delay preserves that result only if the subsequent process and relevant hazards truly remain unchanged. A lasting cap, changed institutions, or a pause that reduces the hazard violates the mere-delay premise and must be evaluated on its own terms.

Any attempt to restore an all-paths or unique-exit theorem needs explicit coverage of saturation, safe freeze or rollback, bounded speed, durable correction, and prevention with permanent resolution or summable residual risk. This is a condition on retaining such a theorem, not a requirement to prove it in order to make the situated case.

## Build the evidence and comparison alongside the repairs

The attachments are a research handoff, not a new evidence base. This planning pass does not freshly verify their literature or current factual claims. The next writing pass should inspect primary sources, retain dates and scope, and search for contrary evidence as well as support.

| Priority | What to establish | What would weaken the diagnosis |
|---|---|---|
| Decisions under pressure | Resource allocation, deployment, or delegation actually changes when relative advantage conflicts with safety | Durable restraint despite competitive pressure; cooperative initiatives with demonstrated effects |
| Success and future evaluation | Appointment, funding, access, standards, procurement, or permission changes link success to later selection | Effects explained by expertise or resources; effective correction surviving unchanged dependence |
| Hazard-specific correction | Coverage, detection time, decision time, execution, human fallback, and residual risk for a defined class | Durable AI-assisted correction, robust controls, or saturation keeping the relevant danger bounded |
| Shared and irreversible consequences | Actual propagation pathways and affected groups, distinguishing provider loss from broader loss of agency or physical harm | Containment, recoverability, or exposure much narrower than claimed |
| Alternatives receiving serious support | Which proposals receive consideration, funding, and institutional sponsorship, with variation across actors | Substantial support for effective cooperative alternatives; an open policy process inconsistent with the proposed restriction |
| Alternatives and transition | Feasible participation, access, budgets, enforcement, continuity, and change under adaptation | A credible continuation policy that meets the same standards at lower cost or risk; a cooperative design that fails its own tests |

Each evidence row should include its premise, indicator, source and observation date, population, hazard class, supporting and contrary findings, confounds, uncertainty, and effect on the recommendation. Use justified ranges where possible; leave unmeasured parameters unmeasured. General capability benchmarks do not measure dangerous behavioral variety or residual catastrophe risk by themselves.

Use an independent criterion for capture: a change in selection or corrective authority that produces durable actor advantage while impairing an entrusted purpose or protected interest. A favorable rule change or concentration alone is insufficient. Expertise, legitimate revision, better standards, and resource scarcity are competing explanations to investigate. Distinguish selection during training, deployment allocation, and institutional replacement, including what is transmitted between rounds.

Define the comparison before choosing the winner: a common horizon, resources, exposure, welfare and agency measures, policy installation costs, residual risk, and a consistent decision criterion. Evaluate at least regulated competitive provision with strong correction, leadership and defense, a finite sprint followed by restraint, a temporary pause, and a cooperative infrastructure design. They may overlap; compare what each changes. Apply uncertainty or precaution symmetrically.

Match exposure first to isolate technical effects, then allow deployment to adapt and report both risk per useful output and aggregate harm. A reduction in one does not establish a reduction in the other.

Do not make a large new experiment a prerequisite for the whole v5 theory. The most useful optional study would test whether an initially better safety protocol loses its advantage when success changes evaluator rights. It needs fixed-selector, matched-drift, and endogenous-selector comparisons; independent safety measures; capture opportunities that are optional; costs for interference; and genuine room for correction to succeed. It would support a bounded mechanism claim, not prove a geopolitical diagnosis. Keep it distinct from the existing pilot and design 2.

## Give cooperation and transition equal analytical care

Develop one concrete candidate path far enough to expose its assumptions, then compare institutional variants. Public purpose should include useful provision, scientific progress, competent administration, long-term responsibility, and the capacity to hear unwelcome evidence. The brief presents a Chinese governing ideal of authority justified by improving people's lives and the historical trajectory. Preserve that positive conception as an attributed normative source; do not infer that every Chinese institution realizes it or that Western institutions share one motive. Model how officeholders and institutions reproduce public commitments. Neither inevitable corruption nor automatic benevolence is an acceptable premise.

Specify financing, ownership, service obligations, access, technical interfaces, evaluation, rule-making, operational authority, and enforcement separately. Common infrastructure need not have a single permanent operator. Explain what affected people can challenge, who can execute a justified correction, and how essential services continue during that correction.

Separate rewards for useful contribution from rights to appoint evaluators, exclude entrants, or amend governing rules. Protecting correction does not require removing every productive incentive.

The transition chapter should follow this candidate sequence, revising it if participation or risk analysis fails:

1. Establish a shared account of hazards and measurement, with explicit disagreement and uncertainty.
2. Agree narrow, testable commitments in a specified domain; identify who can authorize them and what happens on breach.
3. Fund effective correction and useful shared services, protecting access and continuity before dependencies become irreversible.
4. Change strategic delegation, access, and decision rights in stages, with fallback capacity and observable performance.
5. Broaden the arrangement only as its institutions demonstrate competence, fair participation, and correction under stress.

For every stage, state actors, benefits, concessions, budgets, deviation incentives, coalitions, interim vulnerability, and response to breakdown. Include smaller jurisdictions, users, and people unable to escape shared exposure. Stress-test a violation by the leading provider, a coalition of insiders, an unjustified restriction, leadership succession, and loss of essential service. These are mechanism-design cases, not assumed cultural incompatibilities.

Work through a contested adverse finding first against a weaker participant and then against the leading provider: who decides and acts pending appeal, what stays confidential, and how urgent protection and essential services continue. Nominally equal procedures need not have equal effects under unequal dependence.

A pause buys an opportunity. Readiness to resume should explain changes in objectives, strategic incentives, technical reliability, correction, deployment constraints, and retained human agency, with evidence for each. These are proposed assessment dimensions, not a proved sufficient checklist or a requirement that every person's private motives transform first.

Preserve E2, stopping before the decisive class, and E3, development paced by effective understanding and correction, as distinct choices. A temporary training pause is a third temporal arrangement whose value depends on what changes before resumption. Do not merge stopping, slowing, and delaying.

## The writing sequence and completion gates

| Pass | Concrete output | Gate before the next dependent step |
|---|---|---|
| 1. Fix the spine and preserve the contribution | A short thesis, operational definitions of continuation and pivot, a contribution inventory, and a claim-dependency map | Every old module has an explicit destination or recorded reason for exclusion; no universal impossibility claim hides in the framing |
| 2. Repair and gather evidence in parallel | A tracked V45 repair record, corrected proofs and targeted checks; a dated evidence register and primary-source comparisons | No essential inference rests on an unresolved mathematical objection; missing empirical premises remain visibly conditional |
| 3. Develop the hard comparisons and the transition | Strong continuation cases, one concrete cooperative design, and a staged path with participation and continuity analysis | Same horizons and standards for every path; a real counter-regime can change the recommendation |
| 4. Write the full theory | One coherent v5 manuscript and supplement, reorganized around the argument above | Claims are marked as definitions, values, theorems, assumptions, observations, conjectures, or recommendations; proofs support the exact prose |
| 5. Review and reconcile | Separate mathematical, empirical, and governance/argument reviews, followed by a focused revision; label AI-agent assessments as generated reviews | Objections are resolved, scoped, or openly retained; no lost contribution or silent strengthening; abstract and conclusion match the body; human review or external replication is claimed only if separately obtained |
| 6. Prepare a derivative for submission if wanted | A venue-specific paper drawn from the completed theory | Verify the actual current venue requirements first; compression does not decide the theory's intellectual scope |

Use a single lead editor for the argument. Parallel readers can handle formal repairs, primary-source evidence and novelty, and institutional comparisons. Agree the terms and interfaces before asking them to draft connected chapters; assemble their findings into one voice rather than concatenating separate essays.

When drafting begins, use `v5/THEORY.md` for the coherent text, `v5/CLAIMS.md` for contributions, dependencies and repair status, `v5/EVIDENCE.md` for the evidence register, and `v5/CHANGELOG.md` for decisions and preserved or relocated content. Add reproducible checks with the claims they test. Keep v4 and the imported sources intact. The working manuscript should already read cleanly; keep revision narration outside it.

v5 is ready for serious reading when its practical conclusion can be reconstructed from explicit mechanisms, dated evidence, stated values, fair alternatives, and a credible transition. Successful numerical checks, agreement among AI reviewers, or a stronger title are not substitutes for that chain.
