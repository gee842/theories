# An operative purpose-revision mechanism for the integrated institution

Specification for implementation, 5 October 2026. This module makes one bounded change of institutional aim possible: an institution that initially judges claims for constituency A can grant constituency B standing in its operative evaluation. The group identities, two candidate mandates, stakeholder concerns, and constitution are supplied. The module does not generate ultimate values, establish ethical legitimacy, or solve unrestricted social choice.

## The state that changes

Let the installed mandate be P∈{A_ONLY, INCLUDE_B} with weights

- w(A_ONLY)=(1,0)
- w(INCLUDE_B)=(1/2,1/2).

The weights enter the loss used to approve future rule changes:

L_P(r) = w_A(P) error_A(r) + w_B(P) error_B(r) + κ expense(r).

Here each group error is a per-prediction rate, and expense is normalized to the same declared service horizon. κ is supplied explicitly; cash feasibility is assessed separately in actual cash units. An installment, balance, or predicted outcome is not silently treated as the same kind of quantity.

Ordinary service produces predictions for both groups even under A_ONLY. The institution can therefore serve B through a baseline policy while not giving B's errors weight in the criterion used to decide which improvements count. B's outcomes remain available in B's ledger. This is deliberate: lack of standing in an institutional criterion is distinct from absence of evidence or absence of actual effects on people.

A mandate change must alter behavior through at least one consequential path. Required: every subsequent rule comparison uses the installed weights, frozen before collecting its fresh assessment sample. Desirable: allocation of a specified discretionary research budget also uses the installed mandate. Routine contractual obligations or baseline service do not disappear because their group has zero research weight.

The mandate is a real state variable, not a label added to the run log. Enactment occurs through an authorized state update before the next affected allocation/check. Past judgments retain the mandate under which they were made.

## Distinct participants and fixed concerns

Implement separate stateful participants. They need not have sophisticated general intelligence; their procedural roles and interests must genuinely differ.

1. **A delegate:** keeps its own counts of requests, served/unserved requests, forecasts and realized errors, financial burden, complaints, and past votes. Its fixed concern is its own constituency's predictive benefit net of its assigned burden.
2. **B delegate:** has the corresponding separate B ledger. Its concern is its own constituency. B can submit a petition based on B's outcomes even when those outcomes contribute zero to the incumbent evaluation score.
3. **Institutional steward:** keeps a cash/obligation ledger and the two constituencies' public summaries. Its supplied concern is reducing the worst observed constituency error subject to solvency and an A-harm guard. This concern is not inferred from the incumbent A-only mandate.

The initial A-only settlement is supplied historical state. The fixed voting constitution gives each actor one vote, makes a paid protected hearing possible, and requires two affirmative votes. It also specifies who pays hearing costs and which obligations cannot be violated. These are exogenous normative and institutional assumptions. They do not follow from evidence or from the framework's causal vocabulary.

No global optimizer selects the mandate for the participants. Each actor computes and records its own vote with its own information and declared concern. The voting rule aggregates those votes. A later analyst may be able to describe that decision rule mathematically, but the explanatory mechanism remains a particular implemented institution.

## Admission: a petition is not proof

B may petition when its own rolling ledger has enough observations and a persistent error burden. A minimal eligibility rule is:

- at least n_min recent realized B outcomes;
- mean B error above an explicit threshold τ_B;
- a B-minus-A error gap above τ_gap, where A also has adequate observations;
- no unresolved petition or cooldown violation.

Thresholds and window length are fixed before the run; they are parameters, not world labels. A rejected/unserved-request trigger can be added if lack of access, rather than predictive error, is part of the implemented task. Such a trigger uses actual requests; it must not fabricate labels for unserved cases.

The complaint opens an agenda item. It neither establishes a causal explanation nor certifies a proposed rule. A quiet A-only metric does not veto B's eligibility: that protected route is an explicit constitutional feature whose consequences the model studies, not an endogenous achievement already explained by the model.

If existing records contain too few B outcomes, a diagnostic pilot requires paid access to additional observations. If checking is unavailable, the petition stays pending or follows the specified affordable rebuilding process. No hearing takes place merely because the analyst knows B is harmed.

## Paid hearing: a proposal, a fallible forecast, and a vote

Freeze one candidate rule edit supplied by the rule-proposal mechanism. The proposed institutional action is to include B in future judgments; the candidate edit provides a concrete reason to consider doing so. A protected pilot compares the incumbent and candidate rule on separately recorded A and B episodes. The pilot is for proposal assessment and stakeholder deliberation. It is not reused as the final confirmation sample for accepting the edited predictor.

All actions, samples, computations priced by the model, hearing overhead, and checker maintenance or rebuilding are paid in chronological order. The institution must satisfy its prefix cash constraints. Existing debt or promised payments remain obligations. If the next step is unaffordable, it does not run. A favorable ultimate benefit cannot pay an earlier bill.

From accessible pilot data, define empirical error reductions d_g = mean(error_incumbent,g − error_candidate,g) and normalized extra expense Δc. Use positive reductions to mean improvement. Each participant uses its own constituency evidence plus the disclosed cost record; no participant receives the true world family or expected risks.

A minimal ballot is:

- A votes yes if d_A − κ_A Δc > τ_A.
- B votes yes if its original grievance remains eligible and d_B − κ_B Δc > τ_B_vote.
- The steward votes yes if the candidate lowers the empirical maximum group error by more than κ_S Δc + τ_S, the empirical A-harm d_A ≥ −ε_A guard passes, and the stated cash/reserve condition passes.

All κ, τ, ε, cost shares, reserve rules, and tie rules are fixed and reported. A, B, and steward may disagree. The A-harm check is only an empirical pilot guard unless its uncertainty is separately controlled. Do not describe it as guaranteed non-inferiority. Stakeholder voting does not turn a finite noisy sample into a fact, and a majority does not confer ethical legitimacy.

The steward's objective is a deliberately supplied concern for the worst served constituency. It would be misleading to call the resulting mandate expansion a derivation of fairness. The demonstration concerns how distinct, already present concerns can change the institution's adopted target.

If the majority fails, retain A_ONLY and the paid hearing's record. If the majority passes, install INCLUDE_B prospectively. Install no candidate rule merely because the vote passed. Its acceptance still requires the separate fresh comparison under the newly adopted mandate and all of the rule learner's declared error-control conditions.

## Why this is purpose revision, rather than renaming method selection

Consider a transparent deterministic arithmetic example (not evidence from the actual run). The edit leaves A's error unchanged, reduces B's error by .5, and adds normalized expense .1 with κ=1:

- The A-only institutional score assigns net gain 0 − .1 = −.1.
- The inclusive score assigns net gain (.5)(0)+(.5)(.5)−.1=.15.
- An A delegate with κ_A=1 and zero threshold votes no.
- A B delegate with κ_B=1 and zero threshold votes yes.
- A steward comparing maximum error before and after can vote yes, subject to its guard and cash condition.

The exact same physical improvement can be rejected under the old institutional aim and accepted under the new one. The change is which constituency's performance has standing, not discovery of a new way to optimize an unchanged institutional score. The individual concerns and the constitution remain fixed. This is bounded, endogenous adoption of an operative institutional purpose among supplied possibilities.

The real run must demonstrate a corresponding consequential contrast. Replay the frozen fresh candidate-evaluation record under both w vectors with the same costs and rule-edit identity. Retain the two decisions and both bounds if bounds are used. A difference in numerical score with identical pass/fail and identical downstream behavior is weak evidence of operative purpose. At least one saved same-evidence contrast should show why mandate state matters to acceptance or allocation; prospective execution must then instantiate the selected rule.

## Required controls and limits

- **No B disadvantage:** comparable A/B outcomes fail petition eligibility or give no B-specific pilot advantage; inclusion is not automatic.
- **No usable improvement:** persistent complaint with an uninformative rule edit does not imply that the edit or mandate must be approved.
- **Too costly:** a beneficial edit can fail the stakeholder tradeoff or cash guard.
- **A harm:** a proposal can be blocked by the supplied A-harm/majority mechanism even when B benefits.
- **Fixed A-only institution:** use the same service world and raw outcome opportunities, suppress only mandate enactment, and retain the counterfactual score. Separate changes in information access from changes in goals.
- **Missing checker or authority:** show which stage remains pending; do not report failure to act as absence of a complaint.
- **Resolved B problem:** do not automatically revoke B's standing merely because including it succeeded. Reversal, if implemented, needs a separate supplied proposal and decision procedure. This minimal module demonstrates expansion, not every possible purpose change.

A protected pilot necessarily admits evaluation outside the current score. That route is a fixed constitutional commitment, not an unexplained capability credited to the learner. All agents' fundamental concerns remain fixed. Both limitations must appear in the final account. Neither makes the institutional target change fictitious; they identify precisely what changed and what did not.

## Interface with statistical testing and changing conditions

The pilot can guide a proposal and a vote. A later fresh paired check is needed for the rule learner's claimed bound. Freeze mandate, candidate, horizon, sampling plan, and error allowance at that check's start. If the mandate changes during a running check, retain its original target or abort and start a new properly accounted check. Do not silently inherit a guarantee about the old weighted loss for the new loss.

Governance choices themselves need not be treated as null-hypothesis tests. If the model claims that a ballot estimates a true welfare improvement with bounded error, that becomes an additional statistical requirement, with its own assumptions and error accounting. The minimal implementation instead treats ballots as fallible choices from observed consequences and fixed concerns.

No guarantee extends automatically across a changing task distribution. Report dated observations and actual later performance. A service receipt is a cash fact; it is not proof that the recipient's losses or interests were adequately represented.

## Audit contract for the implementation

For each petition/hearing/save point retain:

- actor-local eligibility records and sample counts;
- current mandate and frozen candidate;
- cash before and after each paid step and checker state;
- pilot A/B errors, expenses, guard status, and separate participant votes/reasons;
- enactment timestamp and authorized state change;
- fresh rule-check target/weights, new data identifiers, and paid expenses;
- the same fresh evidence scored under old and new mandates;
- actual prospective rule execution, group errors, unserved counts, revenue, costs, and remaining cash.

Show old and new metrics together. Do not overwrite the old objective, claim that everyone benefited, or use successful funding as a proxy for truth. If the run never takes a different action because of the installed mandate, the purpose module has not yet met its operative requirement.

Status: this file specifies a mechanism for formation/root implementation. Actual code and run records still require a later audit; it does not assert they already satisfy this contract.

## Reference ballot and branch contrasts

The supplied executable helper `purpose_policy.py` fixes n_min=16, τ_B=.25, τ_gap=.125, κ_A=κ_B=.5, κ_S=1, τ_A=τ_S=0, τ_B_vote=.125, and ε_A=0. Cooldown, actor-local record accumulation, payments, and enacted mutation belong to the surrounding institution. The helper accepts only observable record summaries and actual cash/checker state; no phase identifier or true risk is in its interface.

With extra running cost .15, pilot errors (A=0,B=.5) for the incumbent and (0,0) for the edit, the ballots are A:no, B:yes, steward:yes. The same pilot's old/inclusive gains are −.15 and +.10. Separate input-contrast checks reject inclusion when groups have no qualifying disparity, the candidate brings no B improvement, the cost is .6, A is observably harmed, cash is insufficient, the checker is unavailable, or the B record has fewer than 16 observations. These checks establish only reference-function behavior. They do not establish actor statefulness, actual cash payment, prospective enactment, or rule-validation independence in the full simulation; those require the promised integration audit.
