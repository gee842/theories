# Revision path for the AI trajectory paper

Prepared for Ren on 3 October 2026, after reading the five v5.2 reviews, their synthesis, the relevant manuscript sections, the claim register and the original authorial brief. This is a proposed revision path, not a revised manuscript. It preserves the situated case for cooperation and the full theory's scope.

The strongest next version should organize the argument around a concrete problem: **competitive success can purchase control over the institutions that determine whether further success is acceptable.** Faithful AI can intensify that process. A cooperative response must change harmful incentives and preserve the ability to correct them, including when the successful actors belong to the cooperative arrangement itself.

This changes what supports what. The institutional mechanism carries the argument. The account of Ψ explains a possible source of its persistence. The relational view supplies the scope of responsibility and the positive purpose. None has to masquerade as a proof of the others.

## The central revision

The present chain is approximately:

> Ψ is the one root → Ψ is false → growth requires an inclusive self → safeguards inside Ψ fail → a cooperative pivot is necessary.

Several arrows are unsupported, although many results around them are correct. Replace that chain with:

> Shared consequences exceed the interests represented in individual decisions → faithful assistance can amplify the resulting conflict → success can endogenously weaken its correction → institutions must address both the conflict and the durability of correction → compare feasible ways to do so, including their own capture and transition risks.

This keeps the nine layers connected: the host establishes shared exposure; selection explains rewarded behavior; the contest and delegation explain pressure; correctors and observation explain whether pressure is contained; failure identifies protected losses; verification and cooperation address incentives; transition addresses implementation. The full theory remains larger than a capture model.

A proposed replacement for the opening thesis:

> This paper examines AI development organized around decisive advantage, where competitive success can also reshape the institutions that evaluate and constrain it. Faithful assistance to each principal does not by itself resolve conflict among principals. Under specified conditions, success finances control over future selection, making some safety improvements vulnerable to reversal. We develop a cooperative response that reduces harmful stakes, protects independent correction, and preserves the standing of those affected to contest the technology's direction. Its institutional proposals are evaluated by the same standards as regulated competition, including participation, enforcement, capture and transition risks.

The positive organizing principle is: **everyone affected has standing; useful success earns rewards without purchasing exemption from shared constraints or control over its own assessment.** This gives the philosophical argument institutional content while allowing plural purposes and bounded competition.

## Resolve the conceptual decisions together

### Give Ψ a limited explanatory job

Treat Ψ as a hypothesized reinforcing configuration of objectives, beliefs and institutions. Do not make it a single scalar that silently contains every cause of racing. Keep three objects distinct:

- What an actor values, including its weight on relative advantage and others' welfare.
- What it believes about rivals, shared consequences and future enforcement.
- What institutions actually reward, permit and protect.

Rational concern about a future winner can arise from a real commitment problem. It is not automatically a false attribution. Conversely, a professed cooperative objective is not evidence that the institutional game has changed.

Replace “the race is a property of the self-model” with “objectives and institutions jointly determine whether a material conflict becomes a race.” Accurate self-interest can still generate a dilemma. Repetition, information and enforceable commitments can also support cooperation without universal identification with others.

Keep a testable Ψ hypothesis: independently measured objectives and rival beliefs help explain persistence and responses to institutional reform beyond material incentives alone. Predefine the observations that would weaken it. Successful durable correction with unchanged competitive motives is a counterexample to motive-change necessity. Failure of independently measured beliefs to add explanatory power weakens the proposed cognitive mechanism. Do not absorb either result by declaring an invisible Ψ still present.

“Slow variable” and “attractor” are substantive claims, not verbal repairs. The relevant timescale ordering and stability must be shown. Use the existing field model for the demonstrated dynamics. Keep an additional psychological model as an extension.

### Give “we are one” a precise positive role

Separate three claims:

1. **Empirical:** people and institutions share particular dependencies and hazards. Identify these pathways; interdependence alone does not make domination impossible.
2. **Normative:** people bearing consequential effects deserve consideration and meaningful standing to contest decisions, whether or not they compete in the race.
3. **Institutional:** incentives, shared provision and correction can make that wider responsibility effective without waiting for every actor's private identity to change.

The mathematics represents some implications of this view. It does not prove the ethical premise or establish identity expansion as the unique condition of survival.

In the current contest, θ = n−1 includes only the contestants. Call this contestant inclusion. It can describe a cartel. Do not call it planetary inclusion unless nonparticipants and their harms enter the model or the stated institutional constraints. Preserve different local purposes and reject the assumption that a single aggregate objective settles distribution, rights or representation.

This is a substantive role for “we are one”: it determines who counts and who retains a voice in correction. It is more useful than attaching the phrase to an invalid necessity claim.

### Make the institutional design answer the same problem

The Compact should separate economic returns, public authority and independent adjudication.

- Contributions can receive negotiated returns, contracts, access or compensation.
- Public rules require representation and contestability for affected people and participating jurisdictions.
- A party cannot purchase control over the evaluation of its own conduct.

Proposition 7.8 imposes a participation constraint on payoffs. It does not derive proportional voting rights or a great-power veto. Nor does “votes not proportional to compute” entail one participant, one vote. Specify the constitutional protections now; leave an exact voting formula as a design question unless a model supports it.

If no feasible allocation meets participation while keeping correction independent, say that the proposed Compact is infeasible in that region. Do not conceal the problem by giving the strongest participant an exemption.

V4 remains intact: capable authority supplies services, investment and coordination. V3 specifies how its exercise remains answerable. Apply Section 3 to the Compact's governing bodies and supply-chain enforcers as rigorously as to firms.

Cooperation over strategic permissions need not mean a single technical lineage. Preserve independent implementations, evaluators and replacement capacity. A common provider's failure or collusion belongs in the design's stress tests.

## Repair the formal bridges without expanding the paper

### Survival and the four interventions

Rename Proposition 1.4 to describe its actual result, for example “Cumulative harm under repeated stage equilibria.” State the maintained symmetric, myopic equilibrium selection. Its formula is not a forward-looking equilibrium theorem.

Use a hazard load rather than a probability that can exceed one:

$$
h_t=aL_t\mathcal E_t
=\frac{a r_t\Omega_t L_t(n-1-\theta_t)}{n[c_t+(1+\theta_t)L_t]},
\qquad q_t=1-e^{-h_t}.
$$

For the specified deterministic sequence of conditional hazard loads,

$$S_N=\exp\left(-\sum_{t\le N}h_t\right),$$

so positive limiting survival is equivalent to finite cumulative load. With history-dependent random loads, state the appropriate conditional/pathwise assumptions before importing this equivalence.

The actual contribution is the decomposition of contest-generated harm. It identifies four interventions: change the objective gap, reduce the contested stakes, reduce residual harm per unit, or raise the net marginal cost of harmful racing. The second-order question then becomes whether the institutions sustaining those changes survive competitive pressure. This is where Section 3 belongs in the argument.

Several details must travel with the repair:

- The exponential link is still a modeling premise, not empirical evidence that real hazards accumulate this way.
- Prize sharing scales intensity and hazard load h. It does not linearly scale q after the exponential change: qβ = 1 − (1 − q0)^(1−β).
- A levy enters through the actual net marginal incentive. If revenue is rebated equally among contestants, a levy τ contributes marginal objective cost τ(n−1−θ)/n, rather than τ. Specify revenue incidence before replacing c with c+τ.
- A rebated levy is a transfer, not an aggregate resource loss. Do not include it in dissipation as though it were an effort cost.
- This is a model of race-generated risk. Zero racing does not eliminate capability-related or background risk. For example, an explicitly assumed total load h(background) + h(race) retains background risk when θ = n−1.
- A constant factor reduction may produce a large finite-horizon benefit while leaving an infinite-horizon sum divergent. Keep the finite horizons used by standard D central.
- A hazard that saturates at a positive constant still gives zero limiting survival. The alternative relevant to Proposition 1.4 is summable residual hazard, not saturation alone.
- Do not infer that greater shared loss L implies a greater welfare-coupling coefficient κ. Those are different modeled mechanisms, and treating them interchangeably can double count dependence.

The theorem should support an intervention map. It should no longer announce that growth requires everyone to widen their self.

### Sharing and commitment

In the Tullock contest, sharing a fixed fraction of the modeled prize reduces equilibrium intensity. A reversal in a separate linear selection model does not establish elimination of racing in this contest. Correct the numerical example by placing the compared actors in the same field.

Separate divisible benefits from positional or governing power. An illustrative effective stake can be written as

$$\Omega_{\rm effective}=(1-\beta)\Omega_e+\Omega_s,$$

where the sharing arrangement covers only the divisible component. This extension needs its own assumptions. Lowering the contest exponent r is also not synonymous with removing domination: a lottery can still award its winner decisive power. Limit the winner's powers or reduce the positional stake explicitly.

The review's commitment calculation is useful in its stated transfer model:

$$G_{\rm renege}=\frac{\beta\Omega(n-1-\theta)}{n}.$$

Use it to expose an enforcement requirement. A wider objective reduces the temptation, holding the other factors fixed. Credible sanctions, escrow, contemporaneous distribution or shared control can also change the constraint. At θ = n−1, the toy model gives indifference, not strict compliance. If Ω grows, θ approaching n−1 does not even ensure that the temptation tends to zero.

Thus commitment supplies a second reason to care about inclusion, but not a second proof of its universal necessity. The constructive statement is that benefits should be distributed, and limits made effective, while the mechanisms supporting the agreement remain available.

### Be selective about new results from the reviews

Three tempting additions need narrower wording:

| Proposed addition | What can safely be retained | What to defer or reject |
|---|---|---|
| Pure relative objectives cannot cooperate | Common additive payoff improvements cancel at θ = −1; particular repeated games can prove stronger impossibility results | A universal claim that relative actors cannot cooperate or cannot care about any catastrophic outcome |
| The Ψ model is bistable iff B > 4s | This permits three fixed points for a range of intercepts; actual bistability also requires an intercept within that range | Treating the slope condition alone as sufficient at a fixed policy parameter |
| Sharing around 75% exits Ψ and falling below 65% restores it | An illustrative hysteresis example under chosen parameters | Estimated policy thresholds or a universal dwell-time rule |

The new repeated-game result is unnecessary for repairing the headline. A short counterexample showing that ordinary self-interested actors can cooperate is enough. If a positive proposition is wanted, prove it inside the existing binary faithful-AI game rather than presenting a theorem about all relative objectives.

Likewise, repair Definition 3.1 now: distinguish the recursive-selection mechanism from an attracting set demonstrated in a specified model, and distinguish both from long residence in a transient region. Positive feedback alone establishes neither attraction nor multistability. An attractor need not have a proper rather than global basin. The existing field results supply enough mathematical substance without a new Ψ proposition.

Targeted checks in this planning pass, using standard-library Python, found three equilibria for the reviewers' logistic parameters at β = 0.7, but only one at β = 0.5 or 0.9 despite B > 4s. The fold values are approximately 0.646716 and 0.753284. At n = 4, β = 0.75, Ω = 1, the reneging gain is 0.01875 for θ = 2.9 and zero for θ = 3. These checks concern the examples; they do not validate an empirical model of institutions. No full manuscript proof audit or full numerical-suite rerun is claimed here.

## Make the policy comparison capable of changing the answer

### Evaluate mechanisms before applying labels

Keep “pivot” as the name of the proposed direction. Remove the requirement that every policy be assigned to an exhaustive continuation/pivot binary. Delete the Class column in Section 6.9 and compare named, specified arrangements.

For each arrangement record what changes, who is covered, how it is enforced, whether a successful actor can undo it, and what happens when it fails. The existing durability tests provide most of this machinery. There is no need for another composite score.

For example, independent evaluation can be installed inside a competitive economy; benefit sharing may leave strategic stakes intact; incident notification can improve beliefs without changing payoffs. These are analytically different changes even when all appear in a cooperative program.

Do not define a real-world pivot as crossing an unmeasured separatrix. That language belongs in the model that contains the separatrix. In policy analysis, document the institutional change and test its durability.

R1–R6 should remain assessment dimensions until domain-specific thresholds, evidence requirements, responsible assessors and a decision rule exist. Where readiness is operationalized, protected requirements should be explicit gates; a weighted average should not allow excellent performance on one dimension to hide failure on another. Thresholds must come from the use domain and risk decision, not invented percentages.

### Repair the comparative conclusion as well as the introduction

There is a consequential gap beyond the synthesis's six headline fixes. Sections 6.9 and 9.2 infer preference for a cooperative arrangement because dangerous continuation has not been excluded. The cooperative arrangement's breakdown and capture risks are also unmeasured. A common uncertainty standard does not itself establish a ranking. The manuscript's own example allows well-corrected continuation to outperform both cooperative examples.

Keep the mechanism-based recommendation to build independent correction, reciprocal commitments and useful shared services. Distinguish this from an established superiority claim for the complete Compact. For stronger comparative language, define the uncertainty set, tolerances, transition costs and enforceability of each candidate, then show the result under the same horizons.

Proposed replacement for the decisive inference:

> The analysis supplies reasons to pursue reciprocal restraint, independent correction and changes to the rewards for harmful racing. It does not establish that every cooperative arrangement outperforms regulated competition. A particular arrangement is preferred only where its advantages survive a comparison that includes transition, enforcement, capture and breakdown. The Compact makes those requirements concrete; its comparative performance remains to be established.

Allow evidence to redirect the preferred policy. A feasible regulatory arrangement that performs better can change the recommendation; it must not automatically be renamed a pivot. A failed Compact may warrant a different design, a narrower agreement, or a different policy—not necessarily a larger version of the same program.

### Preserve effective human authority

Adopt bounded institutional mandates for AI. Human institutions authorize and revise purposes; systems implement delegated assignments and common admission constraints. “Legitimate principal” must refer to an institutional determination, not an AI's independent power to declare whose wishes count. Common constraints need verification and appeal; calling them hard does not prove their technical enforcement.

Purpose cannot literally be absent from a system's objectives: tasks themselves express purposes. The boundary concerns who has authority to set and revise the mandate.

Opacity alone is not O2. Humans need practical capacity to specify the mandate, obtain independent evidence, challenge consequential conduct, and enforce timely suspension, modification or replacement. A formal stop button with no usable information or fallback can fail this test; an opaque internal computation with effective assurance and recourse can pass it.

O2 should protect human authority through legitimate and contestable institutions. It should not protect each government's tenure or unrestricted unilateral action. Otherwise mutually authorized binding constraints would themselves count as the loss that the Compact is supposed to prevent.

Repair the unequal supervision comparison in Proposition 5.11, grant the strongest plausible AI-assisted oversight case, and count common causes and collusion against the cooperative design too. These are necessary repairs to an argument retained in the paper, even though the synthesis lists them under “should fix.” A new study can wait.

## Keep evidence and prior work proportionate

Correct the false quotation and semiconductor wording at their sources and propagate the corrections through both language versions and the registers. Keep descriptive claims separate from inferred mechanisms.

Two qualifications to the history review's own repair are needed. Replacing “Anglo-American” with “liberal market economies” does not establish historical priority; remove the unsupported “first.” A downstream disruption multiplier establishes dependence and propagation, not by itself an unpriced externality or an estimate of κ.

Keep a short account of corporate governance and interstate security competition as different precedents. A full causal genealogy is not needed to establish the mechanism. Describe traditions as internally diverse without expanding the submission into a comparative history of civilizations.

For present evidence, compare like documents by function and date, and record tensions within the same actor. A declared pursuit of leadership supports a claim about leadership; it does not alone establish an isolated self, winner entitlement or every tenet of Ψ. Balanced evidence means consistent standards, not equal counts of unfavorable quotations.

Include **Dario Amodei, CEO of Anthropic**, with ordinary attribution. His October 2024 [Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace), Section 4, proposes an alliance seeking AI advantage, military superiority and conditional benefit distribution, framed as protecting rights and improving governance. Treat it as a strategic essay and an instance of the benevolent-leadership proposal, not enacted corporate policy or proof of all three Ψ tenets. Preserve its strongest rationale when applying the paper's tests.

Position the contribution precisely:

| Prior work | Role in the revised argument |
|---|---|
| [Critch and Krueger, ARCHES](https://arxiv.org/html/2006.04948v1) | Acknowledge the existing distinction between single-principal success and multi-principal safety; Section 4's elementary game is an illustration |
| [Open Problems in Cooperative AI](https://arxiv.org/html/2012.08630v1) | Locate commitment, institutions and incentive design within an existing program; cooperation can also enable exclusion or collusion |
| [Kulveit and colleagues, ICML 2025](https://proceedings.mlr.press/v267/kulveit25a.html) | Address the close systemic argument about interacting mechanisms of disempowerment |
| Wendt and the security-community literature | Locate the claim that interests and identities can change; do not claim θ discovers this idea |
| [Sterman on learning and policy resistance](https://pmc.ncbi.nlm.nih.gov/articles/PMC1470513/), and Ashby | Credit established systems concepts; specify the paper's particular selection-and-correction mechanism |
| Endogenous-institution and regulatory-capture models already in the register | Compare actual assumptions and results before claiming originality for the selection gradient or field dynamics |

The best candidate contribution is the combination of conditional selection for control, its dependence on share and appropriability, correction-rate requirements, and the field results about reform and pauses. A general resemblance to prior work neither erases nor establishes that contribution. Preserve any relevant earlier use of the term meta-attractor in the provenance discussion.

## Execute a coherent revision before compression

Choose a strengthened version of option (a): **repair every retained claim that carries the argument, while deferring additions that create a new research program.** The synthesis's six-item boundary is too narrow; completing all eleven suggestions as expansions is too broad.

Keep the current section numbering and most valid derivations for the full theory. The largest prose changes belong in the Chinese overview, Sections 1 and 9, and the policy classification passages. This avoids renumbering the whole manuscript while changing its explanatory order.

| Pass | Concrete edits | Acceptance condition |
|---|---|---|
| 1. Repair the claims | Rewrite the opening and conclusion together; repair 1.4 and 1.5; distinguish objective, belief and institution; qualify Definition 3.1 | No necessity claim rests on a disjunction, no universal reabsorption claim survives a counterexample, and no hazard probability exceeds its range |
| 2. Repair the institutional comparison | Remove outcome-dependent labels; fix standard D's unsupported ranking, O2, AI mandates, supervision comparisons and payoff-versus-voting confusion | Regulation can win the comparison; the Compact faces the same capture and enforcement tests; human authority has observable content |
| 3. Repair evidence and positioning | Correct quotations and source strength; shorten genealogy; code actor statements consistently; add close prior work | Every retained empirical assertion has an appropriate source, and the specific contribution is visible |
| 4. Synchronize and verify | Update THEORY, Chinese overview, CLAIMS, EVIDENCE, CHANGELOG and relevant numerical checks together | No superseded headline remains in a summary, register, table, proof or output; changed results are independently checked |
| 5. Make the submission derivative | Select the strongest complete chain and retain a constructive institutional response | The shorter paper stands on its own and does not import unproved conclusions by reference to the longer theory |

Defer the new psychological bistability theorem, general repeated-game impossibility, calibrated hysteresis thresholds, expanded genealogy, new experiments, and a final global voting constitution. Preserve these as research questions with their caveats. Do not defer corrections to claims still printed.

For the submission, the narrative can be shorter than the full theory: faithful AI in a harmful game; selection for control over correction; conditions under which reform persists; implications for cooperation, participation and plural provision; evidence limits and discriminating tests. Historical and philosophical discussion can remain in the full theory without being a prerequisite for every formal result.

Use a quality gate rather than a commitment to submit at any cost: proceed only with a self-contained argument whose conclusions match its support. If that cannot be completed before the confirmed paper-track cutoff, preserve the repaired theory and do not submit claims known to be broken.

The supplied working deadline is 5 October 2026 AoE, which conventionally ends just before 19:00 Bangkok time on 6 October. However, the public [OpenReview submission configuration](https://api2.openreview.net/invitations?id=IASEAI.org%2F2027%2FConference%2F-%2FSubmission), checked directly in this planning pass, gives `duedate = 1791284340000`: **6 October 2026 at 17:59 Bangkok time** (10:59 UTC). Plan against that earlier due time; do not rely on the form's later technical expiration. The full venue guide, page limit and other submission requirements still need confirmation before preparing the derivative.

No manuscript, reviewer report or original reviewer script was edited in this planning pass. No commit, release or submission was made.
