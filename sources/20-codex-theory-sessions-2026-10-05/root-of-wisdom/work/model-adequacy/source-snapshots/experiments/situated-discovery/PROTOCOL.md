# Situated discovery experiment protocol

5 October 2026. AI-generated implementation protocol under Ren's research direction. This file is written before the development run. Development seeds may diagnose implementation and power; any changes must be recorded before freezing separate evaluation seeds. This is a synthetic mechanism experiment, not evidence about actual people or deployed AI.

## Target and declared scope

Test whether a shared-purpose institution can generate a useful contextual explanation from its own records, verify the corresponding action using fresh randomized evidence, and act before a deadline. Separately intervene on inquiry funding, record retention, model expansion, evidence standing, and implementation rights. The experiment represents bounded model expansion within an analyst-supplied grammar, not unrestricted novelty, changing purposes, or a new action ontology.

The common objective in this local task is to reduce failures plus the declared costs of action and inquiry. Report these components separately as well as their sum. Both known actions and all generic attribute names are available. The currently active model initially has no contextual distinction.

## Environment and time

Each world contains six independent fair binary attributes. A seed chooses two distinct attributes and one value for each; their conjunction defines a latent context with probability 1/4. This planted rule is never passed to candidate search, confirmation, funding, or action choice. Unit outcomes are independent conditional on context and action; this is not a cumulative-damage environment.

Action A costs zero; action B costs .25 per case. Failure probability is .05 except that A fails with probability .80 in the latent context when the hazard is present. B removes this additional hazard. In the absent-hazard world both actions have failure probability .05. Failures have declared loss one.

Thus the latent conditional B policy has actual expected gain .125 per case over always A: 1/4 times (.75-.25). Always B loses .0625 per case in the hazard world, and .25 in the absent-hazard world. The scientist may calculate these quantities for assessment; the learner may not use them.

There are 64 blocks of 128 cases (8,192 cases). Outcomes arrive two blocks after the associated action. A first admitted/enacted response by block 24 counts as timely; report later responses separately. All arms use the same contexts and independent uniform outcome draws within each paired seed and hazard condition. The initial states and pre-intervention histories are identical.

## Candidate generation and confirmation

During discovery, A is used. Paid rich records contain case identifiers, pre-action attributes, and actions. Failure reports arrive later and can be linked only while those records remain available. Aggregate failure reports remain available even if the rich record has expired. No hidden cache may recover deleted attributes.

After at least 512 linked mature discovery records, generate a generic grammar of an all-cases predicate, 12 one-literal predicates, and 60 two-literal conjunctions (73 in total). Exclude conditional predicates with fewer than 64 observed cases on either side. Rank by the difference in failure rates inside versus outside the predicate. The constant predicate has score zero. This is exploratory association, not a causal certificate. The learner pays .01 per generated predicate and logs the entire ranked set. The frozen-model arm permits only the constant predicate.

Take the highest-ranked untested candidate and freeze it. The proposed policy uses B inside that predicate and A outside. Test on fresh qualifying cases, assigning 128 to each action in a random balanced order. Assignment order is fixed independently of outcomes. If funds are insufficient for the next trial slot, delay that slot; ordinary operation remains A. Test counts concern matured linked records, not merely initiated cases. Confirmation records never enter discovery ranking. A maximum of four candidates can be confirmed; candidates are frozen before their own future cases. No continuous significance checking or sample-size extension is allowed.

For attempt j use alpha_j=.05/4. Let delta_hat be the difference between A and B sample failure rates. For binary failures the one-sided Hoeffding radius is

\[
r_j=\sqrt{\tfrac12(1/n_A+1/n_B)\log(1/\alpha_j)}.
\]

Accept the conditional action effect only if delta_hat-r_j-.25>0. With a fixed candidate and fresh independent cases, this bounds false acceptance of a nonbeneficial conditional policy by alpha_j. The union bound gives at most .05 over four attempts under the stated sampling assumptions. Searching 73 candidates on discovery data does not consume the confirmation error budget. An unsuccessful attempt is logged and the next candidate receives fresh data. Failure to complete a test is not evidence against its hypothesis.

The null is actual expected policy gain at most zero, not failure to recover the exact planted predicate. Scientist-only enumeration of the 64 attribute combinations scores accepted policies and exact feature recovery separately.

## Costs and institutional funding

Rich record capture costs .01 per captured case; confirming an outcome costs .005 per initiated trial; generation costs .01 per predicate. A B trial also costs .25. These costs must be paid when initiated. The B cost is charged to the inquiry cash account during a trial and counted exactly once in the total action-cost outcome. Deployment B costs are paid from the common operating allocation, assumed sufficient up to .25 per case. Ordinary aggregate outcome recording and policy computation are unpriced assumptions.

Every arm has the same total possible inquiry allocation, 512 units. Allocation is a transfer into an inquiry cash account, not a cost; only expenditure counts as cost. Unspent money remains recorded. A protected institution allocates eight units per block while inquiry is unfinished. The return-funded institution's pre-validation rule is the calendar schedule max(.125, 8*rho^block), initially rho=.5. Since no validation has yet occurred during this acquisition stage, this represents repeated withdrawal in the absence of demonstrated returns. The code does not implement a general performance-responsive budget or its post-discovery maintenance. A first learner-validated proposal stops further inquiry even in the no-standing arm. These are explicit procedural assumptions, not consequences of rationality or common interests.

Unlinked metadata lifetime is eight blocks normally and one in the short-record arm; with a two-block outcome lag the latter loses the linking information before outcomes arrive. Capture costs are identical. After linkage, discovery records, candidate summaries, and completed evidence persist without an additional fee or expiry. This is a pre-outcome linking intervention, not a model of paid long-term archives or successor inheritance. Storage beyond capture is unpriced.

## Arms in each world

1. Protected: normal records, full candidate grammar, admission and implementation.
2. Return funded: only the allocation rule changes.
3. Short records: protected funding, record lifetime one block.
4. Frozen model: protected funding, constant predicate only.
5. No standing: the learner receives the same evidence and can validate a proposal, but it cannot enter the institutional decision record.
6. No authority: the proposal is validated and admitted, but cannot change operational actions.
7. No inquiry: no rich records, candidate generation, or trials; always A.
8. Temporary rescue: return-funded calendar rule, with protected allocations during blocks 12 through 27 inclusive, then return directly to the underlying calendar schedule (already at .125). The rescue does not restart a new halving sequence from eight. This tests a finite intervention, not an optimal timing claim.

Until the first validated proposal, the protected, no-standing, and no-authority arms must have identical actor-visible evidence, candidate selection, and trial actions. After that event the admission and enactment states differ. These are implementation controls, not surprising discoveries. Every arm shares potential available resources; actual spending differs and must be reported. This comparison does not by itself establish effects independent of the material resources the funding rule makes available.

## Predictions and failure criteria

P1. Protected inquiry will generate and confirm a positive-value conditional policy more often by the deadline than return-funded inquiry in the hazard world. Its improvement should be mediated by completed linked records and randomized trials. If both perform alike, the proposed funding bottleneck is unsupported at these settings.

**Pre-evaluation qualification from the development audit.** The severe .5-renewal arm receives only 23 units over the horizon. Even the minimum first-test bill is 512*.01 + 73*.01 + 256*.015 + 128*.25 = 41.69; actual delayed capture raises it to 42.97 in the normal discovery sequence. Its inability to complete confirmation is therefore a deterministic budget certificate, not an emergent discovery from the runs. Protected success remains contingent on generation, evidence, and timing. P1 is interpreted with that distinction.

P2. The richer model should sometimes be needed: the frozen constant policy should not pass confirmation often in the hazard world, because its actual gain is negative. If discovery relies on simulator truth or injected proposals, the target has not been met.

P3. No-standing and no-authority arms should preserve the protected arm's first learner validation event; only their downstream stage differs. These paths are checked exactly. Altered pre-gate evidence invalidates the claimed isolation.

P4. Short retention should prevent completed contextual search under this explicit lag. This is a deterministic interface check, not evidence that real institutions forget at this rate.

P5. Absent-hazard inquiry should incur positive costs and should rarely accept a nonbeneficial policy. A positive raw outcome difference caused by favorable noise is not evidence of gain; compare paired means with uncertainty. Protection need not dominate the no-inquiry control in this world.

P6. Temporary rescue should restore some otherwise incomplete discovery processes. Failure remains informative; a rescue that exceeds the deadline must not be called timely correction.

## Runs and reporting

Development seeds: 0 through 15. Evaluation seeds: 10000 through 10255, fixed before evaluation. With 256 independent paired worlds per condition, a proportion's worst-case standard error is .03125; provide Wilson intervals and paired standard errors for arm differences. This is enough to resolve large mechanistic effects, not rare-event calibration of a .05 bound or a precise social prediction.

Record first candidate, validation, admission and enactment times; initiated and completed trials; incomplete tests; generated and tested candidates; raw association scores; each confirmation bound; actual policy gain; exact predicate recovery; action counts; failures; inquiry overhead; B action costs; cash flows and reserves. Keep realized loss separate from scientist-computed expected policy gain. Save per-seed records and aggregate results. Archive the evaluation code, protocol, and hashes before using held-out seeds.

No extrapolation to a universal societal attractor is licensed by this finite experiment. A failure to discover by the horizon can be a deadline/resource failure without permanent closure. Fixed purpose, truthful attribute capture, independent cases, trusted randomization, available operating resources, and a finite representational grammar remain explicit assumptions.

## Development record and frozen evaluation extension

The first 16-seed development run and its exact inputs are retained in `results-development-v1/`. Protected and rescued inquiry found timely policies in all 16 hazard worlds, while the severe funding control could not complete a test. No false acceptance occurred. The audit identified the budget impossibility above; no numerical failure is hidden by the extension.

Before held-out evaluation, add six return-funded arms that multiply the next allocation by rho in {.80,.81,.815,.816,.82,.90}, with the same eight-unit start and .125 floor. No other acquisition, validation, or outcome parameter changes. This tests less severe withdrawal and deadline sensitivity. The rates bracket the analytically estimated first-test funding requirement before the two-block reporting lag, rather than being selected using evaluation outcomes. The original .5 arm remains as the explicit resource-impossibility control.

Prediction P7: within this frozen design, greater retention of the inquiry allocation should increase completed or timely validation, with an intermediate region of eventual but late evidence. A difference in achieved funding is part of this specified mechanism, not a claim of an effect at equal expenditure. Test every listed rate, report late and unfinished cases, and do not label this finite horizon an attracting permanent closure.

The same separate evaluation seeds 10000–10255 apply to all fourteen arms and both hazard conditions. The environment and learner parameters were inspected during development; held-out results estimate behavior of this selected synthetic benchmark and do not eliminate model-selection bias or establish external validity.

Before freezing, two AI-agent implementation audits found no truth leakage, confirmation invalidity under the stationary assumptions, double-charged B cost, or pre-gate mismatch. Their findings corrected the scope of the budget and archive claims above. A trace-only error was also repaired: the per-block allocation log now records actual credited cash even when inquiry terminates later in that block; cumulative accounting and actions were unaffected. Four mechanism tests passed, including all 60 possible planted conjunctions on an exact diagnostic training distribution, useful nonexact predicates, confidence/cost checks, and stage/ledger/retention checks. The evaluation freeze includes this protocol, the simulation code, and the test file.
