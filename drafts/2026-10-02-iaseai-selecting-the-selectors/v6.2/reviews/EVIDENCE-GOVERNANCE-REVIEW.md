# V6.2 independent review: evidence, alternatives, and governance judgment

Reviewed 4 October 2026. Reviewer: Codex evidence/governance subagent, independently assigned within the multi-agent review. This is a review artifact only; no manuscript files were changed and no commits were made. References below use the generated V6.2 files as read in this session. Stable identifiers accompany line numbers where available.

## Overall assessment

V6.2 has a substantially more defensible argument than a simple claim that competition inevitably causes catastrophe. Its most important improvements are substantive: C0 now identifies the empirical joining of mechanisms as a conjecture; the evidence table separates declarations from behavior; the proposed institutions are expressly untested; the coercive fallback is compared rather than endorsed; and the manuscript acknowledges that regulated competition can satisfy particular requirements without being renamed. These changes should be preserved.

The remaining weakness is the last mile from conditional mechanisms to decision rules. Several release and activation rules do not actually implement the conditions of the theorems they cite. The qualitative ranking also gains apparent support from a comparison that puts terminal losses on the continuation side and attempted repairs on the design side. Calling the ranking a judgment is appropriate, but does not eliminate the need to compare the same events and horizons.

My judgment is **major revision before presenting the recommendations as an operationally specified protection policy**. The manuscript can already support a serious research programme, explicit reasons to investigate institutional correction, and conditional arguments for preparation. It does not yet support a computed robust ranking, a validated custody activation mechanism, or a release rule based simply on falling residual risk. None of these criticisms requires rejecting the author's values or the basic selection mechanism.

### Findings at a glance

| ID | Priority | Confidence | Finding |
|---|---|---|---|
| EG1 | P1 | Very high | Falling residual risk is not enough to withdraw E3 or establish C1 favorable; the theorem turns on cumulative hazard/summability. |
| EG2 | P2 | High | Possibility of irreversible loss is treated as failure of a finite-horizon probability tolerance that has not been specified or bounded. |
| EG3 | P2 | High | The reversibility comparison omits matched terminal failure branches for the proposed design. |
| EG4 | P2 | High | Advance commitment removes a decision step, not physical response, installation, execution, or reneging; “only detecting” is unsupported. |
| EG5 | P2 | High | Tier 1(a)'s universal warrant exceeds the demonstrated option-value case, especially for institutional preparation plus binding activation commitment. |
| EG6 | P2 | Very high | E2 has two rationales but the C1 withdrawal rule and the C5/C7 activation rule do not say which takes precedence. |
| EG7 | P2 | Very high | The pacing comparison reverses one hazard inference and overlooks the cited paper's explicit monitoring-lag extension. |
| EG8 | P2 | High | Short public benchmark leads are turned into an unmeasured assertion that no breakout has put an actor beyond punishment. |
| EG9 | P3 | Very high | Several smaller source/operational statements remain stronger than their evidence: BEAD funds, UK remit, and readiness. |
| EG10 | P2 | Very high | Hash commitment does not establish held-out secrecy or prevent training on the committed metrics. |

P1 here means that the issue can change the warranted policy or the stated ranking; P2 changes scope or interpretation; P3 is a narrower correction. Confidence is confidence in the identified mismatch, not confidence in any prediction about future AI.

## EG1 — The C1 release rule substitutes declining risk for sufficiently low cumulative risk

**Location.** THEORY.md:516–520 (Theorem 5.13 / `coverage`, E3); THEORY.md:1166 (E3 trigger); THEORY.md:1200 (C1); TESTS.md:12,84,108,150. Related historical overstatement: DISCUSSION.md:501.

**Priority/confidence.** P1; very high. This is a logical mismatch, not an empirical dispute.

**Finding.** The theorem distinguishes a branch with persistent uncovered hazard from a branch with a summable upper bound. The practical register instead says that residual risk “falling under present incentives” causes E3 and the case for E2 to lapse for the class, with their triggers withdrawn. Declining hazard does not establish that distinction.

An example inside the theorem's own danger premises is U_t/Y_t = 1/(t+2), residual-floor coefficient h = 0.02, and actual conditional loss probability q_t = 0.02 + 0.01/(t+1), for t >= 0. Coverage lags, q_t exceeds h(1-U_t/Y_t), and q_t is strictly falling, yet survival tends to zero. Thus the current verbal withdrawal condition can be met while the theorem's failure premises continue to hold. Even requiring risk to tend to zero does not fix the issue: q_t = 1/[2(t+1)] decreases to zero but has a divergent sum, so log(1-q_t) <= -q_t still forces the survival product to zero. Conversely, an extremely low constant hazard may meet a specified five-year tolerance while failing an infinite-horizon summability criterion. Trend, finite-horizon acceptability, and asymptotic survival are three different propositions.

**Consequence.** The registered rule can withdraw precisely the protection meant to address cumulative exposure while the theorem's long-run failure mechanism remains. It also makes C1 easier to label favorable than the paper's own definition of E3 warrants. The converse activation rule, “residual risk not falling,” can activate on a safe low plateau unless the magnitude and exposure horizon are also specified.

**Repair.** Give C1 at least two separately scored parts:

1. A finite-horizon decision test: an independently estimated upper bound on the cumulative probability of O1/O2 over each protected horizon, including confidence, model uncertainty, and deployment scale, is below a registered tolerance.
2. If the asymptotic theorem is being invoked, a justified tail bound strong enough to establish summability, or an explicit assumption about the future trajectory. A finite sequence of declining observations is not a tail certificate.

“Residual risk falling” can remain an encouraging diagnostic, but should not by itself switch E2/E3 off. Apply the same repair to the claim that Cold War learning supplies a case of summable residual risk (DISCUSSION.md:501): a finite historical survival record and declining estimated hazards do not establish an infinite sum.

**Minimal acceptable revision.** Replace “falling” in the release condition with “bounded below the registered cumulative-risk tolerance at the relevant horizons, with the conditions for any invoked tail claim separately satisfied.” Keep the weaker trend claim as evidence that the case for slowing may weaken.

## EG2 — The protection standard is not instantiated, and its third step is not yet applied

**Location.** THEORY.md:796–812 (§8.1, Definition 8.1 / `kernel`); THEORY.md:1175–1179 (Tier 3); DISCUSSION.md:292,338; CLAIMS.md:21,36,39.

**Priority/confidence.** P2; high. This concerns consistency of the stated decision procedure. Final cross-review lowered the priority because the manuscript explicitly admits that the estimates are absent and labels its ranking a judgment; the defect is the unsupported move to the standard's third step, not concealment of an uncomputed ranking.

**Finding.** The standard compares upper bounds on probabilities of O1/O2 at common finite horizons over Θ, against a stated tolerance. The manuscript then concludes that every path fails that tolerance because every path's worst case includes an irreversible loss. No actual tolerance, bounded parameter set, finite-horizon risk bounds, or joint dependence assumptions are supplied.

The existence of an admissible irreversible event is not the same as a probability bound exceeding a tolerance. A path with a worst-case five-year loss probability of 0.001 contains irreversible-loss outcomes, as does one with probability 0.5. The standard distinguishes them; the verbal comparison does not.

There are two coherent readings, and the manuscript currently moves between them:

- **Probabilistic robust comparison:** Θ contains models with probabilities; use the supremum of the relevant cumulative probability. The bounds must be supplied or left unestimated.
- **Adversarial possibility comparison:** any named, uncontradicted catastrophic mechanism suffices to fail. This can be a normative rule, but if every path admits catastrophe, it often produces a tie. Qualitative preference for repairability is then an additional rule, not a calculation of the lowest probability bound.

The correctable kernel is an all-disturbance guarantee and is an appropriate separate concept. It should not silently turn a probability-based satisficing rule into zero-tolerance worst-outcome reasoning.

**Consequence.** Readers can mistakenly understand the Tier 3 preference as what the protection standard implies, when the text has not established that any path fails its finite-horizon tolerance, let alone identified the smallest upper bound. The manuscript does acknowledge missing estimates; the problem is retaining the preceding unconditional conclusion despite that acknowledgment.

**Repair.** State an explicit schematic decision rule, for example B_j(H) = sup over θ in Θ of Pr_j,θ(O1 or O2 by H), and specify how the multiple horizons and O1/O2 bounds are combined. Publish at least one transparent illustrative Θ and tolerance analysis, keeping it separate from an empirical estimate. Until calibrated bounds exist, say: “No candidate has yet been demonstrated to meet the tolerance; current evidence does not permit the standard to rank their bounds. We provisionally prefer X for the following qualitative, normative reasons.” If reversibility breaks an otherwise unranked tie, add it explicitly to the rule.

## EG3 — The proposed design receives remedies where continuation receives terminal outcomes

**Location.** THEORY.md:1176–1177; DISCUSSION.md:294–334 (failure-mode table), especially 298–304 versus 326–332; DISCUSSION.md:342,393,407–416.

**Priority/confidence.** P2; high. The problem is comparison structure; the paper already admits that the design is untested. Final cross-review lowered the priority to recognize that explicit qualification. Continuation's table also contains some remediable branches; the imbalance is the stage and timing of the compared failures, rather than a complete omission of its possible remedies.

**Finding.** Continuation's table includes capture before evidence, a floor crossed, an admitted masked divergence, and a lost capacity to overrule. The design's table mostly includes a captured function followed by recertification, collusion followed by rotation, service interruption followed by standby, and overreach followed by appeal. It then names only two irreversible design failures: coercive escalation and custody capture.

A shared disclosure registry could be captured or mistaken, causing a hazardous system to be admitted and an irreversible loss before recertification. A standby service could fail to restore essential provision before a catastrophic loss. A masked system could outrun oversight while the custodians remain formally independent. These are the same kinds of late-detection or failed-response branches already admitted for continuation; neither requires capture of decisive custody or a coercive strike. THEORY.md:520 explicitly says the growth hazard persists after racing stops.

Giving the design a planned response does not exclude these branches. Continuation also has planned responses—recall, courts, replacement of regulators, reciprocal limits—before a terminal threshold is crossed. Conversely, after a terminal threshold is crossed, the design's appeal or rotation is no more a reversal of the loss than continuation's is.

**Consequence.** The sentence that every other design failure has a reversal is too strong, even with the qualification that the reversals have not been tested. It supports the central qualitative ranking using a timing asymmetry. The issue is not that proposed designs must already have real-world outcome data; it is that they must face the same fault-to-loss chains.

**Repair.** Use a common event tree for both candidates:

fault -> detected before critical boundary? -> independent remedy available? -> remedy executes before the boundary? -> common-cause failure? -> protected loss avoided?

For each shared hazard, put the two pathways side by side. Separate “a remedy is specified” from “the failure is reversible with probability/bound X before O1/O2.” Add the design's uncovered-hazard, false-negative, covert internal-deployment, service-continuity, and delayed-repair branches to Θ. The defense may then be that the design plausibly lowers particular transition probabilities, not that the terminal branches are absent by design.

**What survives.** The preference for building explicit, independent remedies is a defensible value and engineering principle. It is stronger when described as a hypothesis about the probability of timely recovery rather than an exhaustive classification of irreversible failures.

## EG4 — A registered trigger is not yet a commitment technology, and does not leave only detection delay

**Location.** THEORY.md:749,1157,1165–1169; TESTS.md:142–150; DISCUSSION.md:357–359,393,411,441. The mathematical time-to-decisiveness indicator is TESTS.md:146, citing Remark S2.1 / `tdec`.

**Priority/confidence.** P2; high. Final cross-review treats this as a delay-accounting and implementation-interface defect. X10 explicitly acknowledges unresolved enforcement against the strongest participant; the review does not allege that this uncertainty is concealed.

**Finding.** It is sensible to prepare and agree a trigger before incentives deteriorate. The stronger statement that commitment leaves “only detecting” does not follow. Even a valid automatic decision has to be communicated, executed, and made effective. A plant needs to stop, keys need to be transferred or disabled, a violating actor may withhold access, and an executive or host jurisdiction may refuse. X10 expressly leaves execution against the strongest participant unresolved. A prior agreement cannot remove the enforcement failure merely by calling later activation mechanical.

The policy also mixes **prepared**, **installed**, and **in force**. The trigger subtracts the time to install and verify custody; the commitment paragraph treats building and deciding as already removed. Which physical and legal controls have actually been installed before the trigger fires is not specified.

Finally, the trigger's T_dec indicator is calculated using a constant local gap-growth factor and a finite decisive threshold. The manuscript correctly calls the decisive gap a quantity to measure, but does not show that the extrapolated hitting time is a conservative bound under saturation, strategic response, changing channels, or masking. A local growth estimate is useful for research without yet being an activation estimator.

**Consequence.** The recommendation can activate too late or claim incentive compatibility exactly where its actuator fails. The warning-time rationale for early preparation remains, but it is not a proof that precommitment solves the critical commitment problem.

**Repair.** Define the full response chain and its measured distribution: observation, classification, authorization if any, communication, execution, and time until the restraint actually binds. Mark completed preparation separately from remaining installation. Specify the precommitment instrument—escrow, already-installed controls, legal authority, custody of keys, or another concrete mechanism—and model revocation/bypass as a deviation rather than assuming it away. Use a conservative bound on T_dec across admitted models, including uncertainty in the decisive gap. Put response latency and the chance of failed execution into p_d. Then either prove the resulting enforcement inequality or call the mechanism a candidate to be tested under C4/C7.

**Minimal acceptable wording.** “Precommitment can remove the need for a new discretionary policy decision; detection and verified execution still take time and remain enforceability conditions.”

## EG5 — Tier 1(a) is an option-value argument, not established to pay on every reading

**Location.** THEORY.md:1153–1158; TESTS.md:44–65, especially 55,56,58,60; DISCUSSION.md:342,348,377,393.

**Priority/confidence.** P2; high.

**Finding.** The central issue is whether a binding activation commitment belongs in a tier whose warrant is independent of C4 while the design it would activate is still being compared under C4. Persistent reasons for information, research and preparation can survive every named crux without constituting a mathematical dominance theorem, and the tier is marked as a recommendation. TESTS also permits its contents to change with the evidence. The review therefore does not reject bounded research merely because it has costs. The stronger concern begins when preparation includes durable authority, financing, access rights and a binding commitment to an unresolved institutional design; describing that as forgoing nothing needs a separate argument.

This is clearest for item 4. If C5 establishes no route to a decisive advantage in the relevant range, or C4 indicates that common custody is more fragile than available verification arrangements, some continuing research option may remain sensible. It does not follow that the same level of institutional preparation and the same activation commitment remain warranted. Saying that the whole cost is the cost of preparation records the cost but does not show that it should be paid.

The asymmetry between item 4 and Tier 3 is also substantive: the latter compares whole custody configurations under uncertainty, while the former commits in advance to activating a custody mechanism whose implementation is still under comparison. This is not resolved merely by saying the tiers are simultaneous kinds of justification.

**Consequence.** The “on every reading” label should distinguish a continuing reason to investigate and prepare from an unconditional warrant to establish and bind a particular mechanism. Without that distinction, the recommendation can commit to the implementation before its own stated crux has been resolved.

**Repair.** Divide preparation into bounded research/design/pilot expenditure and the creation or irrevocable delegation of powers. Specify a budget, exit conditions, institutional option costs, and the counterfactual uses of resources. Treat the former as a provisionally justified option under named assumptions about possible warning times; require the latter to pass the same C4 comparison as the design it binds. Narrow the claim from “on every reading” to “robust across the presently plausible readings, within a stated budget and without activating the relevant restrictions.” Binding activation should be conditional on both the hazard trigger and a prior demonstration that the chosen mechanism can meet its own safeguards.

## EG6 — Clarify which E2 rationale survives a favorable C1

**Location.** THEORY.md:1165–1166,1195,1200,1205; TESTS.md:7,12,51,84,91,142–150.

**Priority/confidence.** P2; very high.

**Finding.** The theory gives E2 at least two intelligible rationales: dangerous capability outruns correction, and a decisive capability would defeat enforcement or permanently concentrate authority. Those need not coincide. Tier 2 activates custody and E2 from C5/C7 indicators of approach to decisiveness. C1 separately says that falling residual risk makes E3 and the case for E2 lapse, with their triggers withdrawn. The recommendation gives no precedence rule when these judgments differ.

Consider a class with a satisfactory hazard bound and good contestable control, but which gives one state a durable strategic advantage beyond external sanction. C1 can be favorable while C5/C7 support the strategic rationale for E2. The C1 row withdraws “their triggers”; Tier 2 still activates. Conversely, a hazardous class may warrant a pause or rollback even when strategic advantage is not decisive. The existing definition of E2 as decisive-class stopping does not cleanly name that case.

**Consequence.** Two readers implementing the same registered indicators can make opposite activation decisions. This is an operational ambiguity, not an objection to having multiple rationales.

**Repair.** Register separate hazard/control and strategic-domination triggers, say whether they combine by OR or AND, and specify which protection each favorable crux withdraws. A compact truth table should cover favorable/unfavorable C1, decisive/not-decisive C5, timely/untimely C7, and feasible/infeasible C4. Avoid making a favorable C1 erase a strategic-domination trigger unless that is the intended normative choice. Apply EG1's magnitude/cumulative-risk correction before filling the table.

## EG7 — Correct and deepen the comparison with spontaneous pacing

**Location.** DISCUSSION.md:180,186–191; EVIDENCE.md:197; THEORY.md §8.3(b). Source: [Fudenberg and Koh, *Cooperating against Catastrophe*, full text](https://arxiv.org/html/2609.28291v1), especially §§2.3 and 3.5.

**Priority/confidence.** P2; very high for the directional error and omission, high for the interface critique.

**Finding.** The sentence at DISCUSSION.md:187 has the direction backwards. Lower perceived hazard moves the calculation toward racing; it cannot explain participants computing pacing while true parameters put them in the racing region. A case with sufficiently high true hazard but understated perceived hazard gives the reverse discrepancy.

The full paper also explicitly includes private internal capability and a deployment/monitoring lag. Under its assumptions, sufficiently high effective hazard sustains pacing at every lag. Its effective hazard is a payoff-equivalent mathematical quantity; it is not defined simply as the fraction of harm an actor notices or morally counts. The manuscript transparently says it read the abstract, but then builds several paragraphs of substantive contrast that the full source qualifies. [Primary full text](https://arxiv.org/html/2609.28291v1)

**Consequence.** One of the strongest alternatives is made weaker by the comparison's source coverage, and a proposed cross-model mapping is described too close to a direct application. The conclusion that transparent incentives can produce endogenous restraint remains useful; the contrast should concern which specific assumptions fail, not the mere presence of internal deployment.

**Repair.** Reverse the sentence. Distinguish the source's defined effective hazard from this paper's conjectured transformation under relative accounting. Rework the comparison around the full source's relevant assumptions, including what determines risk, what becomes observable, and what is assumed about survival payoffs. Supply a translation between payoff functions or keep that translation expressly heuristic. Cite the lag extension and explain why a threat before deployment or an absorbing strategic breakout falls outside its scope. Do not claim that monitoring delay alone refutes spontaneous pacing.

## EG8 — The evidence on short leads does not establish the absence of decisive strategic capability

**Location.** THEORY.md:751; EVIDENCE.md:109–117; TESTS.md:17,146; DISCUSSION.md:462.

**Priority/confidence.** P2; high.

**Finding.** EV5's benchmark evidence is appropriately qualified and its limits are largely explicit. The core then says that short leads support enforcement because no breakout has yet put anyone beyond punishment. Public benchmark lag does not measure the existence of a position beyond sanction, let alone establish its absence. The relevant tests omit concealed internal systems, complementary assets, actual response capacity, deployment permissions, and whether even a short capability edge can cross an irreversible threshold. The manuscript itself treats internal deployment and masking as major limitations elsewhere.

The verified [Epoch ECI observation](https://epoch.ai/data-insights/open-closed-eci-gap) concerns public model-capability measurements and a historical average lag. The verified [METR page](https://metr.org/time-horizons/) measures success on specified task suites and warns about its upper-range reliability. Neither is a direct sanctionability measure.

**Consequence.** “Not established” in the evidence row becomes “has not happened” in the policy timing argument. This can give false assurance about the remaining preparation window even while the manuscript argues that observation lags are dangerous.

**Repair.** State that available public measures provide no affirmative demonstration of decisive breakout and are consistent with a remaining window, while its size is unbounded by those data. Add operational indicators of convertibility into strategic control and the time needed for effective balancing, rather than treating benchmark lead duration as a surrogate for T_dec. Keep unmeasured internal capability in the uncertainty range on the same basis as other unmeasured failure modes.

## EG9 — Narrow corrections and implementation caveats

These do not defeat the core argument. They matter because V6.2 otherwise takes care to distinguish what sources actually establish.

| Location | Issue | Concrete repair |
|---|---|---|
| EVIDENCE.md:77, EV3 | EO 14365 §5(a) concerns eligibility for remaining BEAD **non-deployment** funds; the register says “remaining broadband-deployment funds.” Section 5(b) separately orders assessment of discretionary grants. | Use the precise program/fund category and distinguish the directed policy notice from already completed withholding. [Primary order](https://www.govinfo.gov/content/pkg/FR-2025-12-16/html/2025-23092.htm) |
| EVIDENCE.md:76,82; THEORY.md:763 | The UK release establishes a rename, specified remit, a new misuse team, and a separate Sovereign AI partnership. It also expressly presents the work/security focus as continuous. The release alone does not establish a **narrowing** from the prior remit. | Record the new stated focus; compare archived prior remit and actual programme changes before concluding narrowing. Retain the excellent existing qualification that impairment of an entrusted purpose is not shown. [Primary release](https://www.gov.uk/government/news/tackling-ai-security-risks-to-unleash-growth-and-deliver-plan-for-change) |
| DISCUSSION.md:464; TESTS.md:154 | “No dimension is met” is stronger than “none is measured in the required form.” Some dimensions can be unsupported, others contradicted; these are different states. | Use “none has been demonstrated to meet the registered criterion,” then distinguish absence of measurement from affirmative failure for each Q dimension. |
| DISCUSSION.md:256, present-policy table | “No, unless custody follows” for reporting/evaluation conflicts with the explicit detection-and-response route in C7 and Remark 5.5. | State “only if detection and response prevent decisive breakout, or custody does”; do not make custody necessary where the theory presents an alternative. |
| TESTS.md:149; EVIDENCE.md:183–184 | The 2.8× annual cap adjustment is valid arithmetic for the cited benchmark trend, but is not a measured rate for every hazardous or decisive capability. EV9 says this; the operational indicator can read as a universal rule. | Keep it illustrative; estimate an efficiency envelope for each regulated capability and add post-training/inference and algorithmic uncertainty before using it as a binding cap schedule. [Primary paper abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6b066da6a23bc55f9b887e7298102884-Abstract.html) |
| DISCUSSION.md:490 | The historical record can illustrate difficulty of control after asymmetric advantage; it does not establish the necessity proposition “custody must precede decisiveness.” | Label that column as the theory's interpretation of the precedent, with alternate explanations and the source's historical limitations. |

## EG10 — A hash commits a metric without guaranteeing that it is held out

**Location.** DISCUSSION.md:353,373 (X10, held-out metrics).

**Priority/confidence.** P2; very high. This is a specific implementation error, not a general objection to preregistration.

**Finding.** The design concludes that publishing a hash before evaluation lets everyone verify prior choice and ensures that no one can train on the metric. The two guarantees are distinct. A deterministic hash over a small candidate set can be recovered by hashing every candidate. Even a properly randomized hiding commitment does not hide the material from whoever created or holds it, and publication at the first evaluation exposes it for later reuse. Standard commitment definitions distinguish binding from hiding; a hash-based hiding construction includes fresh random secret material. [Stanford CS355, lecture 3, §§1 and 3](https://crypto.stanford.edu/cs355/23sp/lec3.pdf)

**Consequence.** The same institutional capture channel the paper studies can expose the metric through the standards body's insiders while every published commitment still verifies. The design therefore cannot count this clause as ruling out assessment gaming.

**Repair.** Commit to a salted, high-entropy test package under a specified scheme; protect the nonce and test content until use; separate holders from assessed parties; record access and leaks; and rotate tests after revelation. State the guarantee as verifiable prior commitment plus a separately tested secrecy protocol. None of these mechanisms warrants the unrestricted phrase “no one can train on it.”

## Targeted primary-source audit

This was a substantive sample, not an exhaustive bibliography verification. “Verified” means that the specific recorded proposition was found in the retrieved primary text, not that the proposition proves the theory. “Limited” means that the text supports only a narrower claim, only an abstract was checked, or the source's own methodology was not independently reproduced. “Unverified” is a retrieval/coverage limitation, not a finding that the source is false. All accesses below occurred on 4 October 2026.

| Source / register use | Status and retrieval | Result for the manuscript |
|---|---|---|
| [Anthropic RSP v3.0](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0), EV2 | Verified; primary PDF text, introduction and policy sections read | The change from unilateral absolute-risk commitments to company plans and industry recommendations is directly supported. This verifies a policy declaration, not a causal estimate of actual racing. |
| [Anthropic RSP history/current page](https://www.anthropic.com/responsible-scaling-policy), EV2 | Verified; primary page | v3.4 dated 8 July 2026 is listed as current; retained discretion to pause and the intervening revisions are supported. The register appropriately distinguishes discretion from obligation. |
| [OpenAI Preparedness Framework v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), EV2 | Verified; primary PDF §4.3 | Competitor-contingent adjustment and all four stated safeguards are accurately represented. The source also includes safeguards during internal development. |
| [Zhu, Silent Revision](https://arxiv.org/abs/2609.08789), EV2 | Limited; primary abstract and metadata | The 710 commitment instances, twelve consecutive version pairs, 77% of traced changes, silence figures, and workshop-review status match. The manuscript now gives the correct denominator. No independent recoding performed. |
| [EvalDetectBench](https://arxiv.org/abs/2609.01611), EV6 | Limited; primary abstract and metadata | The 11.25% measurement-variance point and transfer failure of elicitation prompts match. Its unusual identifier/date combination is reproduced on the retrieved record; do not “correct” it solely from the identifier. |
| [METR time horizons](https://metr.org/time-horizons/), EV5 | Verified; primary methodology/updates page | The above-16-hour warning and task-suite limitation are supported. It is not an operational autonomy-duration or strategic-dominance measure. |
| [Epoch open–closed ECI gap](https://epoch.ai/data-insights/open-closed-eci-gap), EV5 | Verified; primary analysis | The four-month average and eight-point gap on 29 May 2026 match. Downstream inference to sanctionability remains unvalidated (EG8). |
| [Ho et al., Algorithmic progress](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6b066da6a23bc55f9b887e7298102884-Abstract.html), EV9 | Limited; official proceedings abstract | Eight-month halving, 90% interval of approximately 2–22 months, two pre-training benchmarks, 2012–2023, and 200+ evaluations match. Extrapolation to decisive agentic capabilities is not measured by it. |
| [Fudenberg–Koh full text](https://arxiv.org/html/2609.28291v1), EV11 / X8 | Verified relevant sections; not a proof replication | Supports the pacing alternative but requires the substantive comparison correction in EG7. |
| [Anthropic July Public First Action announcement](https://www.anthropic.com/news/donation-public-first-action), EV4 | Verified; primary page | Additional $20m, $40m total, restricted education/policy purpose, and non-election-use statement match. This is the donor's report, not audited recipient accounts. |
| [UK AISI rename announcement](https://www.gov.uk/government/news/tackling-ai-security-risks-to-unleash-growth-and-deliver-plan-for-change), EV3 | Verified facts / limited interpretation; primary page | Date, new name, security remit, and Sovereign AI partnership are supported. “Narrowed remit” requires a before/after comparison (EG9). |
| [EO 14365](https://www.govinfo.gov/content/pkg/FR-2025-12-16/html/2025-23092.htm), EV1/EV3 | Verified; primary legal text | Dominance objective, task force, funding instructions and legislative carve-outs match in substance; repair the non-deployment-funds wording (EG9). This audit does not establish later implementation or litigation outcomes. |
| [White House 25 September 2026 fact sheet](https://www.whitehouse.gov/fact-sheets/2026/09/fact-sheet-president-donald-j-trump-advances-a-fair-and-reciprocal-relationship-with-china-while-hosting-historic-state-visit/), EV8 | Verified; primary page | SI dialogue, next exchange by November, and agreement to establish an incident channel match. The register correctly marks absence of binding development limits as its interpretation. |
| [UN preliminary-report announcement](https://www.un.org/en/node/245172), EV7/EV8 | Unverified in this review; 403 retrieval failure | Do not treat this review as independent verification of the quoted July report, panel membership, or meeting details. Preserve the original register's precise coverage statement. |
| [Business Roundtable 2019 statement](https://www.businessroundtable.org/business-roundtable-redefines-the-purpose-of-a-corporation-to-promote-an-economy-that-serves-all-americans), EV15/X1 | Verified; primary statement | Date, 181 CEOs, stakeholder turn, and the organization's retrospective statement that versions since 1997 endorsed shareholder primacy match. This verifies declared purpose, not compliance. |
| [Truman policy memorandum to Baruch, 7 June 1946](https://history.state.gov/historicaldocuments/frus1946v01/d448), X11 | Verified relevant passages; primary historical record | International control, absence of stockpiles when fully operational, and distinction between dangerous and licensable activities are supported. Custody's success or universal necessity does not follow. |
| [OECD 5 January 2026 package announcement](https://www.oecd.org/en/about/news/press-releases/2025/12/international-community-agrees-way-forward-on-global-minimum-tax-package.html), EV18/X10 | Limited; primary announcement, not full implementing package | Confirms the side-by-side agreement and continued role of domestic minimum top-up taxation. The exemption's exact legal scope remains dependent here on the register's professional source. Interpretation as “coverage unravelling” should acknowledge this alternative-rule structure. |
| [Stanford CS355 commitment-scheme lecture](https://crypto.stanford.edu/cs355/23sp/lec3.pdf), X10 technical check | Verified; university's original lecture notes, definitions and hash construction | Binding and hiding are distinct; the hash construction uses message plus random secret string. This supports EG10's correction but cannot certify the design's operational security. |

### Sources not independently reverified in this pass

The Colorado litigation docket/order, original Wired memo, original July UN panel report, all military-AI endorsement lists, all author-corpus quotations, the complete AI 2040 plans, the Jones full paper, and most historical books were not independently re-read. The manuscript is often explicit about relying on reports or abstracts; retain those distinctions. No contradiction was inferred merely from an inaccessible source or lack of verification.

## What is strong and should remain

1. **C0 is now in the right logical place.** THEORY.md:693–707 and TESTS.md:11 openly separate within-model comparative statics, unproved interfaces, reduced numerical joint models, and real-world co-movement. That is a meaningful repair. No amount of passing numerical checks alone would have established C0, and the text now says so.
2. **The evidence register has a usable adversarial structure.** EV1 separates domestic and external declarations; EV2 preserves competitor-contingent safeguards and contrary commitments; EV3 says it has not established capture under Definition 4.1; EV4 records rule-making expenditures in both directions; EV5 distinguishes metrics; EV6 distinguishes constructed demonstrations from deployment prevalence.
3. **The author’s failed pilot is disclosed.** EV12 explicitly says there is no experimental support for the §4 mechanism yet and does not convert failed P1 into confirmation. This should not be weakened in the next draft.
4. **Whole designs are not presented as uniquely derived.** The polycentric alternative, regulated competition, verification-plus-provision, benign-winner argument, and the design's own D4/D5 failures are taken seriously. The coercive fallback's move to a compared tier is a significant improvement.
5. **The draft distinguishes normative disputes from algebra.** Protection of O2, the treatment of benefits forgone, and AI standing are declared cruxes. A reader may disagree with them without refuting the conditional mechanisms.
6. **Institutional details have become specific enough to criticize.** The chamber, formula funding, recusal, provider participation, fallback, escrow, and execution bodies expose real design choices. The next step is a feasibility model with timing and correlated failure, rather than more architectural labels.

## C0 and the empirical programme: assessment without overclaiming

C0 is not presently demonstrated; the manuscript admits this. That admission is not a defect. The weaker support actually available is that several recognizable observations are consistent with components of the proposed mechanisms and that the models can be coupled under specified assumptions. The evidence does not yet show a common causal driver, a measured Γ, an observed scissors crossing, or a stable empirical measure of success-to-corrector conversion.

Test E should be treated as a research design to operationalize, not a completed preregistration. It needs a fixed unit of analysis, a parameter intervention whose direct channels are identified, prespecified W/C/N outcomes, a justified observation/dwell window, effect-size and power criteria, and controls for changes that affect multiple outcomes without passing through the proposed common parameter. A disclosure intervention can itself change funding, access, reputation, enforcement and language; it is not automatically a single-signature negative control. The root review separately audits the tests' discriminating claims, so this report does not duplicate its findings.

The most useful near-term empirical sequence would be:

1. Operationalize one corrector-domain certificate on observed data, including unobserved-channel uncertainty, and check it against actual adverse findings against a leader.
2. Run a modest intervention or credible natural experiment whose incidence and timing are known, measuring the behavioral response and the proposed mediator separately.
3. Estimate a class-specific cumulative-risk or coverage model rather than substituting general capability trends for hazardous variety.
4. Conduct adversarial drills of the institutional response chain, with a deliberately noncompliant strongest participant and an injected correlated error.
5. Use those results to construct a bounded Θ and an illustrative, then empirical, comparison of a specific custody mechanism with a strong verification/regulation alternative.

This sequence would make both favorable and unfavorable findings actionable. It would also prevent the architecture from becoming insulated against evidence by moving every adverse result from a mechanism test into a design-revision exception.

## Normative disagreements that are not errors

The protection standard may deliberately give irreversible common catastrophe priority over diffuse deaths caused by benefits forgone. That is an explicit N1 choice, not a mathematical inconsistency. It would still help to define the boundary between O1 and forgone-benefit mortality so two equally large irreversible losses are not classified differently simply because one occurs by omission.

Likewise, excluding providers from formal votes is a contestable institutional tradeoff. X10 openly records the loss of local knowledge and participation incentives and acknowledges that influence can return through voice. That is a candidate policy choice, not something Proposition 4.3 alone proves necessary. The review's recommendation is to test the tradeoff under C4, not to insist on a different constitution.

Preference for broad distribution, non-domination, and human authority can support preparation even before probabilities are precisely estimated. The necessary correction is to call that a provisional practical judgment under stated uncertainty and cost limits, rather than claim that an uninstantiated robust calculation or a theorem has already selected it.

## Reading coverage and limits

Read closely: THEORY §§7 and 8, §12, the front-matter and claim-status passages, relevant §§5.3, 10.5 and 11 passages; DISCUSSION X1's literature/novelty structure and X8, X10, X11; the EVIDENCE register; TESTS' cruxes, tier matrix, tests and operational indicators; CLAIMS' definitions, support/status entries and normative summary. Line-numbered passages underpin every finding above. Supplement references were followed at the level needed for the policy checks, but this agent did not re-prove all mathematics, rerun the numerical suite, or certify the build. Those are separate streams of the multi-agent review.

The principal uncertainty is empirical, and the manuscript already states much of it correctly. The needed revision is concentrated: align C1's decision criteria with cumulative risk; distinguish unestimated from unsafe; compare matched fault-to-loss paths; specify the physical commitment and response chain; and repair the strongest-alternative comparison against the full source. These changes would make the practical argument much harder to dismiss without asking it to claim more evidence than exists.
