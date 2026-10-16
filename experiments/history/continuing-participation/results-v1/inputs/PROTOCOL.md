# Continuing participation and funded compensation

5 October 2026. AI-generated research under Ren's direction. Exploratory exact finite model, not a preregistration, empirical experiment, or complete bargaining mechanism. The preceding plural model supplied aggregate requirements. This model supplies two distinct personal loss functions, public exposure assignment, and a modeled unilateral veto over active cooperation.

## Inheritance and new assumptions

`upstream_model.py` is an unchanged snapshot of the recoverable-inquiry physical model. Its rational diagnostic and production kernels are reused: upkeep1, rebuilding3 with one-round lag, diagnostic2 (.9 sensitivity/specificity), repair3, stock0 absorbing, stock clipped at3, damage probability .1 healthy/.8 fault, repair clears fault, onset .1/clearance .05 after production, output2 per resulting stock, cash cap8 and inaccessible overflow. Opening funds must cover each expense before that round's output. The wrapper expands the complete finite public-history tree rather than merging equal physical beliefs.

There are two half-owners A and B. At each round a fair public assignment chooses which person bears any repair's fixed nonmonetary burden. The assignment adds no information about hidden fault. Default burden1 is **fixed per repair**, replacing the earlier target-absence index as the personal exposure measure; it therefore creates no unmodeled private diagnostic signal. Each owner incurs a terminal collapse loss of1, with a declared sensitivity control at6. A test has total nonmonetary burden .05 split equally. These quasilinear personal preferences, ownership shares, symmetric parameters, technology and horizon remain supplied.

They jointly own retained cash and overflow. A nonnegative payment k from the joint reserve to the exposed person is withdrawn privately and unavailable for future production funding. Only k in {0,1,2} on a repair is available in the transfer-enabled arm; the comparison restricts k to0. Both owners fund half the treasury debit. Personal incremental loss is

    (physical expense − output)/2 + k/2 − k*I(recipient)
    + repair_burden*I(exposed repair) + .025*I(test),

plus that person's terminal collapse penalty. The initial half-wealth is a common constant on continuation/refusal branches and is omitted. Do not also add terminal cash utility: flows already account for its ownership. The sum of personal losses cancels transfers, but payouts reduce the reserve and can change future physical opportunities. The expected cash identity is terminal cash−initial cash+physical expense+private payouts+overflow−output=0.

## Information and refusal chronology

1. Observe current stock, reserve, readiness, public sufficient fault belief and current exposed person. All earlier public actions, signals and randomizer outcomes are retained in the history.
2. Reveal the recommended upkeep/rebuilding/testing action. Both owners can veto **before** its expenditure. If accepted, pay and obtain any diagnostic result publicly. No test is available in the same round as rebuilding.
3. Reveal the recommended repair and its contingent payment. Both owners can veto. If both accept, repair/payment execute atomically; the recipient cannot take the payment and then invoke another veto before that repair.
4. Realize productive stock and income, update once from their joint likelihood, advance hidden fault, and assign the next round's exposed person publicly.

Either veto permanently ends active cooperation. Production continues passively without upkeep, tests, repairs or payments through the same remaining horizon. Ownership claims remain; there is no confiscation, exit penalty or controller-chosen deterioration of refusal. This is a **collective veto**, not individual withdrawal while another owner runs the plant. The passive outside process starts from the actual cash, stock and posterior at the gate. Sunk test/setup expense is not refunded; the earlier opening gate separately approved it. Refusal does not reset the hidden state or forget new evidence.

Atomic conditional payment is a supplied local commitment technology. There is no binding commitment to future participation, borrowing, funded private re-deposits, unsecured future compensation, altered refusal rights, private preference reports or other strategic deviations. Future ordinary shared production still enters each owner's continuation value and can motivate participation. Current payment requirements follow from this action/payment class, not from consent alone.

## Policies and objective

The ex-ante comparator imposes only each owner's initial expected loss <= passive refusal loss, before the first exposure assignment. It assumes the recommended plan is executed despite any later incentive to veto. Report it as a commitment benchmark, not a behavioral prediction.

The continuing-participation model additionally requires each person's expected remaining loss at every reached publicly disclosed recommendation to be no greater than their passive refusal loss there. Recommendations are not averaged across a lottery already visible to the owners. Indifference is accepted. Future recommendations remain history-dependent.

With action occupancies y, a row for recommendation a at history h sums its own and all uniquely descended occupied personal losses and subtracts outside_i(h)*y(h,a). Requiring this row <=0 is the linear, reach-weighted participation condition. Flow constraints enforce the tree probabilities. Initial inequalities are retained too. A passive retirement action ensures an admissible fallback. Positive-probability conditional violations are separately evaluated to prevent small reach weights from hiding them.

The reported frontier minimizes attainable collapse probability subject to the relevant participation constraints; it is a research comparison, not an agreed personal objective. Among equal minimum-collapse policies, minimize physical expense, then compensation payout. This reporting rule removes arbitrary wasted spending among tied LP solutions and is not a bargaining solution or fairness claim. The original failure-only development solutions remain preserved.

Replay each resulting policy under actual continuing veto: work backward, accounting for later vetoes; replace any recommendation making either owner strictly worse by the specified passive fallback. A 1e−8 tolerance accepts numerical indifference. Ex-ante promised and replayed consequences can differ. A continuing-compatible policy should replay unchanged to numerical tolerance. This verifies only refusal deviations under the fixed recommendation rule, not general equilibrium, truthful reporting or enforcement by an unmodeled planner.

## Declared comparisons and exploration

Development files retain 24 initial H1/H2 cases before the tie rule, twelve H3 cases after the tie rule but before the replay reporting extension, and sixteen high-collapse-loss H1/H2 cases. The initial wrapper snapshot is retained under `development-inputs`. Selected findings are exploratory.

Final base grid: horizon {1,2,3}, initial cash {2,3,4,5,8}, transfer grid {0} or {0,1,2}, and mode ex_ante/continuing: 60 results. All start at stock1, ready, fault belief1/2, burden1, terminal collapse loss1.

Controls: H1 burden {.5,1.5}, cash {4,8}, both transfer grids and modes:16 results. H2 collapse loss6, cash {3,4,5,8}, both transfer grids and modes:16 results. Total92 policy solves, not independent replications. Detailed reached policies and refusal witnesses are retained for the base H1 cash3/4 and high-loss H2 cash4/5 comparisons. Other cases retain metrics and numerical checks.

The exact H1 control has passive remaining loss−.65 each; uncompensated repair gives worker−.30 and donor−1.30. Before fair assignment each expects−.80. A pool payout k gives worker−.30−k/2, donor−1.30+k/2, so both accept iff .7<=k<=1.3. Divisible payouts require opening cash at least3.7; the implemented integer grid requires4. This terminal certificate does not determine optimal transfers with a future liquidity-dependent continuation.

At H2, collapse loss6, initial cash4/5 becomes cash3/4 on the .1-probability low-stock branch after the first repair. The next fault probability is .1. At that final gate both accept a payout between .68 and1.32; integer payment1 is affordable only with cash4 at that gate. Keep the default loss1 case in which later repair has negative aggregate surplus and compensation cannot help.

## Verification and scope

Independently enumerate short-horizon latent physical outcomes, personally allocated losses, response/refusal values, and transfer cancellation. Verify full history/action conditioning, sunk-cost timing, conditional payment and opening prefunding, the exact H1 interval, initial versus continuing constraints, veto replay, and a recurrent prefix case. Record LP primal/dual, flow, personal-loss decomposition, ledger, and conditional participation residuals. Preserve exact input snapshots and all output cases; refuse overwrite. Generate and visually inspect a scientific figure.

This model implements public symmetric information, two specified personal valuations, conditional local payments and collective veto only. It does not derive legitimate ownership, safe consent, truthful reports, new purposes, unrestricted private contracting or a universal preference for compensation. A worse refusal outcome can manufacture apparent willingness in another model; this comparison holds the refusal rule and property claims fixed. Numerical precision does not establish empirical validity or a universal alignment solution.
