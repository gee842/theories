# Paid evaluation, rule copying, and a usable successor

The same two supplied rules can produce opposite early and later rankings. A paid evaluator can therefore change which rule is copied, but correct identification alone does not guarantee that the successor can execute that rule. The evaluator may consume the reserve needed to bridge the successor's first repair. Copying a program also does not copy the channels that made its donor effective.

This is a finite evaluation-and-handoff experiment followed by an exact infinite-continuation check. It is separate from the common-calendar population model in this research cycle. There is one successor here, no endogenous evaluator financing, no population-growth theorem, and no claim that delayed evaluation is always better.

## 1. Physical process and supplied rules

The repair plant is the deterministic periodic plant used in the cycle-4 adoption study. Its basic eight-unit body is already present. An integer reserve has cap 240. An optional number of repair channels, \(k\in\{0,\ldots,8\}\), is a physical asset. Building an additional channel costs 30; discarding one is free and yields no sale proceeds. Dropping and later rebuilding pays again.

Each fault episode contains eight faults; the next episode begins eight slots later. Newly supplied diagnoses distinguish their hidden causes perfectly, and each diagnosis, authorization, and execution costs one unit per repaired item. The whole service stops earning during repair. Diagnosis can process \(k\) items per slot; authorization and execution add two pipeline slots. Thus, when \(k>0\),

\[
T(k)=\lceil8/k\rceil+2,\qquad
C(k)=24+(8+2k)T(k).
\]

A repair must finish within six slots. Every repaired healthy slot produces gross receipt 40, then pays basic operation 8 and channel upkeep \(2k\), leaving \(32-2k\). The carried reserve is capped after receipt and payment. There is no receipt during repair. Capital installation precedes repair. Since all repair payments are nonnegative and there is no intervening receipt, holding \(C(k)\) after installation is exactly the prefix-financing requirement for that episode. The cycle-4 checker separately expands this macrotransition into its diagnosis/authorization/execution slot ledger.

For current channels \(j\), choosing \(k\) costs \(30\max(k-j,0)\) before repair. The end reserve, before applying the cap at each healthy slot, is

\[
b'=b-30\max(k-j,0)-C(k)+(8-T(k))(32-2k).
\]

The actual rule **S** chooses the payable complete one-cycle plan with greatest terminal cash. Rule **L** chooses the payable complete two-cycle plan with greatest terminal cash. Both execute only the first choice and plan again next cycle. Ties use the lexicographically smallest channel sequence. If L cannot finance any two-cycle plan, it tries a one-cycle plan; either rule fails when no complete single cycle can be paid. Neither controller is supplied the infinite viability set as its objective.

The usable designs are:

| Channels | Repair duration | Repair expense | Healthy-cycle receipts after bills | Net cycle gain with existing channels |
|---:|---:|---:|---:|---:|
| 2 | 6 | 96 | 56 | −40 |
| 3 | 5 | 94 | 78 | −16 |
| 4 | 4 | 88 | 96 | +8 |
| 5 | 4 | 96 | 88 | −8 |
| 6 | 4 | 104 | 80 | −24 |
| 7 | 4 | 112 | 72 | −40 |
| 8 | 3 | 96 | 80 | −16 |

One channel misses the deadline; zero channels cannot repair. Each positive infinite claim below is conditional on the explicitly specified, indefinitely available healthy production input of gross 40 per slot and on the periodic fault/process contract. It is not a closed-system perpetual-growth claim.

### Capacity and actual continuation

**Plant-capacity proposition.** An infinite feasible sequence of repairs exists from \((b,j)\) exactly when

\[
b\ge 88+30\max(4-j,0).
\]

**Proof.** If the inequality holds, install four channels immediately and use them forever. Repair requires 88, and each complete cycle adds eight before the cap. Conversely, every feasible design except four has strictly negative net gain, even before any installation expense or cap loss. An infinite feasible path must therefore use four eventually. If \(j<4\), reaching four requires total positive channel purchases of at least \(30(4-j)\); all complete cycles before the first four-channel cycle have nonpositive net change. At least 88 must remain for that first repair. If \(j\ge4\), every feasible first repair itself costs at least 88. These observations give the same lower bound. ∎

For the actual supplied rules, the exact continuation regions needed here are:

| Initial auxiliary assets | S continues forever exactly when | L continues forever exactly when |
|---|---|---|
| No channels | Never, for \(0\le b\le240\) | \(b\ge208\) |
| Four channels | \(b\ge88\) | \(b\ge88\) |

These results also have short direct proofs. From a cold plant, every payable first choice available below cap 240 is among two, three, and four channels. Their one-cycle changes, including construction, are respectively −100, −106, and −112. S therefore builds two, keeps two, loses 40 per subsequent cycle, and eventually cannot pay 96. An existing two-channel plant likewise cannot be rescued by S's own one-cycle choices, regardless of its starting reserve up to 240.

When \(208\le b\le240\), L can build four and complete two cycles, ending with \(b-104\). Starting with two gives at most \(b-140\) after two cycles; starting with three gives at most \(b-122\), or \(b-128\) when switching to four. Thus L chooses four. From an existing four-channel plant, both rules keep four: it has the greatest feasible one-cycle gain, and alternative designs incur a loss and cannot improve a two-cycle result. The capacity proposition excludes all cold starting reserves below 208 and all four-channel reserves below 88. This proves the stated thresholds independently of a long simulated trace.

## 2. Trial profiles and observation

Two candidate addresses A and B contain one S program and one L program, in an unknown permutation. Both source trials start with an already-present basic plant, no auxiliary channels, and separately endowed cash 240. Their cash endowment totals 480. Their source program remains readable even if the trial plant later fails a repair. The evaluator cannot inspect the program identity before choosing a source.

| Completed checkpoint | S cash / auxiliary channels | L cash / auxiliary channels | Completed every duty through this checkpoint? |
|---:|---|---|---|
| 1 | 140 / 2 | 128 / 4 | Both yes |
| 2 | 100 / 2 | 136 / 4 | Both yes |
| 3 | 60 / 2 | 144 / 4 | Both yes |
| 4 | 60 / 2 | 152 / 4 | S no; L yes |

S's fourth entry is its retained cash when it cannot pay a complete repair; it is not a successfully completed fourth cycle. A trial with no payable complete repair shuts down, freezes its remaining cash, and ceases further operating receipts or bills. Its failed status and readable source program remain available at the checkpoint.

The evaluator chooses its checkpoint and interpretation rule before learning the address permutation. Three supplied interpretations are checked:

* **Cash ranking:** copy the address with greater audited cash; ties choose A.
* **Pass ranking:** observe only whether each trial completed every duty through the checkpoint, then copy a passing address; ties choose A.
* **Calibrated interpretation:** compare the observed cash/status pair with a supplied, correct L profile table; copy its uniquely matching address, otherwise A.

Cash ranking at checkpoint one chooses S. At checkpoint two it chooses L. But the early cash observations already distinguish the candidates: calibrated interpretation can choose L at checkpoint one by interpreting its *lower* early cash as the known investment signature. The reversal under raw cash ranking is therefore a property of that criterion and mechanism, not an informational impossibility theorem.

By contrast, the coarse pass observation is genuinely indistinguishable through checkpoint three. Swapping the two programs leaves the ordered observation \((\mathrm{pass},\mathrm{pass})\) unchanged. No observation-consistent deterministic evaluator can guarantee identifying L under both permutations. Under the explicitly uniform permutation distribution, any randomized evaluator based on that observation identifies L with probability at most \(1/2\). At checkpoint four, pass/fail separates the sources and pass ranking identifies L. The uniform distribution is used only for reported probabilities; all sure-continuation statements quantify over both assignments.

## 3. Paid evaluation, real address memory, and transfer

The evaluator and successor share an initial reserve \(R\), separate from the 480 of source-trial cash. There is no evaluator income. Source cash is inaccessible throughout and is not a successor endowment. The base plant body of the successor is separately endowed; this experiment prices its auxiliary channels, program transfer, and working reserve. A common construction bill \(E\), if introduced before launch with no intervening income, adds \(E\) to every threshold below. The population study in this cycle uses its own explicit construction and capital charges instead.

Payment order is:

1. Pay ten for evaluator support at the end of each trial cycle up to the predetermined checkpoint \(\tau\).
2. Pay two for the audit/comparison operation.
3. If retention is selected, pay one to carry the selected address through the handoff interval.
4. Pay two to copy the program from that address.
5. If transferring donor channels, pay three for the one-to-one physical handoff.
6. Launch the successor with the remainder, capped at 240; excess is explicitly recorded as spill.

All fees are actual cash bills. They are nonnegative, and there is no interim receipt. Total affordability is therefore equivalent to every payment prefix being affordable. A reserve of 19, for example, cannot finance two waiting bills; the second checkpoint is never reached by this evaluator.

The address register has states \(\{\bot,A,B\}\). At the end of audit, the audit controller retires. The copier receives only that physical register, the public preset protocol, and its cash; it has no audit transcript, remembered cash observations, hidden action history, or free payload-dependent timing channel. Paying retention preserves A or B. Without retention the register resets to \(\bot\), and the copier's supplied default is A. Fees and timing are independent of the selected address, so residual cash does not encode it. Program-copy cost includes its delivery; the address-retention fee covers the one intervening handoff interval. Trials retire at the checkpoint, and the channel-transfer fee covers the channels' custody and transport during this interval. Successor duties begin at launch; this model does not impose a common absolute service-start deadline across different checkpoints.

Three asset contracts are distinct:

* **Program only:** copy the rule; the successor starts with zero auxiliary channels. Source channels and source cash are not copied.
* **Donor bundle:** move the selected parent's existing auxiliary channels to this one successor. The selected donor ends with zero channels and retires. Hardware is conserved, not multiplied.
* **Existing four:** the successor already owns four endowed channels, independent of the selected parent. This is a different asset start state, used as a control.

The plant's internal repair observations remain under the supplied cycle-4 diagnostic contract. The newly priced finite memory here is specifically the evaluator-to-copier address. The study does not silently retrofit every internal computer register with this one fee.

## 4. Exact financing frontiers and reversals

Let \(\rho=1\) when the address is retained and zero otherwise, and let \(d=1\) for donor-channel transfer and zero otherwise. The total evaluator bill is

\[
A(\tau,\rho,d)=10\tau+4+\rho+3d.
\]

Once the chosen source and asset contract are fixed, the exact threshold is this bill plus the actual child's required reserve. When retained observation identifies L, program-only continuation requires \(R\ge A+208\); transferring its four channels requires \(R\ge A+88\). With an already-present four-channel plant, either copied rule continues exactly when \(R\ge A+88\).

| Evaluation and transfer | Least \(R\) guaranteeing actual continuation under both address assignments |
|---|---:|
| Calibrated checkpoint 1, program only | 223 |
| Cash ranking checkpoint 2, program only | 233 |
| Calibrated checkpoint 1, donor bundle | 106 |
| Cash ranking checkpoint 2, donor bundle | 116 |
| Cash ranking checkpoint 1, already-owned four channels | 103 |
| Cash ranking checkpoint 2, already-owned four channels | 113 |

Early cash ranking has **no** program-only guarantee at any reserve: it copies S, whose actual cold-start path fails for every reserve up to the plant's cap. More reserve beyond the cap cannot change that. Early donor transfer also cannot rescue S: its donor has only two channels, and S never selects the required investment from that state. These are failures of the supplied rule, even where an alternative allowed policy has feasible continuation.

The following are exact checked examples. All copy probabilities refer to the uniform address permutation, and continuation is actual infinite continuation under the copied rule.

| Case | \(R\) | Copied rule | Child cash / channels | Continuation |
|---|---:|---|---|---|
| Early cash ranking, program only | 240 | S | 225 / 0 | Fails |
| Delayed cash ranking at 2, program only | 240 | L | 215 / 0 | Succeeds |
| Calibrated early, program only | 230 | L | 215 / 0 | Succeeds |
| Delayed cash ranking at 2, program only | 230 | L | 205 / 0 | Fails |
| Delayed cash ranking at 2, program only | 120 | L | 95 / 0 | Fails |
| Same evaluation, donor bundle | 120 | L | 92 / 4 | Succeeds |
| Early cash ranking, existing four | 103 | S | 88 / 4 | Succeeds |
| Delayed cash ranking at 2, existing four | 103 | L | 78 / 4 | Fails |

The delay examples show that better-aimed selection can consume the bridge it needs. The donor example shows why identical copied code and more raw cash need not yield more usable capacity: 92 plus the transferred plant continues, while 95 without its channels does not. The warm-plant comparison shows that selecting L is unnecessary for continuation in some asset states and that paying extra evaluation cost can destroy a guarantee that S already had.

At reserve 240, delayed cash ranking with retained address always copies L and succeeds. Omitting address retention leaves 216 rather than 215 for the child, but the copier defaults to A. It copies L and succeeds with probability \(1/2\); under the other address assignment it copies S and fails. The observer's earlier correct decision is not available to the successor unless it crosses the specified physical handoff.

### No-hazard control

When the periodic fault is removed, both rules may choose zero auxiliary channels, receive eight healthy production receipts, and continue. The menu explicitly includes zero in this control. Receipts precede operating bills, so even a zero-reserve already-built plant can start healthy production. Both source rules reach cap 240 and their labels are indistinguishable by the tested observations. An early evaluator with \(R=15\) and a delayed evaluator with \(R=25\) each leaves zero child cash and succeeds. The second waits an extra cycle and pays ten more without improving continuation. This control changes the disturbance contract, not the rule into a welfare optimum.

## 5. Why the infinite conclusions are exact

For each of S and L under hazard/no-hazard, the checker constructs the actual deterministic successor of every state in

\[
Q=\{0,\ldots,240\}\times\{0,\ldots,8\}.
\]

There are 2,169 states per graph and 8,676 across the four graphs. It first marks states with no payable complete successor. It then repeatedly marks every state whose actual successor is marked. The remaining states form a closed invariant: every such state has a successor in the same set. Every losing state receives a positive rank that strictly decreases along its successor until a state with no payable successor is reached. Closure proves infinite continuation; the finite descending rank proves eventual failure. These are exhaustive graph certificates, not extrapolations from a selected trajectory, and concern the specified actual controller rather than an optimizer permitted to replace it.

For each evaluation protocol the checker enumerates both hidden source assignments, generates only the declared observations, executes the supplied interpretation, resets or retains the actual address register, and checks the launched state against that copied controller's invariant. The universal order is: **one preset protocol, then every hidden address assignment, then its observation-determined choice**. There is no source-identity-dependent pre-observation choice.

The 72 frontier entries cover four checkpoints, three interpretations, three asset contracts, and retention present/absent. Their reserve search through 300 is complete, not merely a finite lower-bound search: every protocol's total bill is at most 48, and reserve above \(48+240=288\) cannot change any child's capped state or selected source. Null entries therefore mean no reserve works under that protocol and cap. Fifteen selected examples additionally assert the reversals above.

The certificates are executable evidence for this finite declared model. The analytical financing, indistinguishability, and capacity arguments explain why its central numbers follow. The calculations do not establish that these fee sizes, horizons, or signal interpretations are empirically appropriate in any particular biological, social, or computational population.

## 6. Saved verification

* [Exact checker](verification/check_paid_evaluation.py)
* [Results and payment ledgers](verification/paid-evaluation-results.json)
* [All financing frontiers](verification/paid-evaluation-frontier.csv)
* [Closed winning sets and descending losing ranks](verification/paid-evaluation-controller-certificates.json)

Run `python3 outputs/cycle-5/verification/check_paid_evaluation.py` from the workspace. The saved run reports all assertions passed.

The demonstrated constraint is conditional and reusable: selection requires an observation-to-action path, a retained or reacquired address, an actual transfer contract, and enough reserve after paying for the selection process. Which evaluator succeeds can reverse with timing, information interpretation, asset inheritance, and the disturbance contract. Neither the most frequently copied rule nor the rule with the largest early or late cash is thereby an ethical good.
