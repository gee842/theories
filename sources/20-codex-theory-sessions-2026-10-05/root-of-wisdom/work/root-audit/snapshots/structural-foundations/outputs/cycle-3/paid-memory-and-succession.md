# Paid memory, changing validity, and succession

5 October 2026. This module addresses a specific limitation of the recurrent-repair model: its diagnostic bit and controller memory were free. Here information must cross an explicitly paid physical interface, a successor has no predecessor transcript, and a report can be erased before the eventual actuator uses it. The result is an exact finite model of paid succession, with a carefully scoped repeated-episode interpretation.

The distinction from cycle 2 is deliberate. Most results below concern exact conditional error probabilities and resource feasibility under a supplied stochastic model. They are **not** probability-one service guarantees. A deterministic constant-condition special case supplies a separate robust result.

## 1. What is being represented

There is a binary condition `X_t∈{0,1}`. Its stationary prior is uniform, and in each elementary time step it flips independently with supplied probability `η`, restricted to `0≤η≤1/2`. A response should match the condition at the time of action. A wrong response has a separately declared consequence; no ethical worth follows from correct prediction alone.

A predecessor observes `X_{−g}`. A successor begins at time zero. The predecessor's private controller is retired: the only payload channel to the successor is a physical archive register. The source and successor registers each have alphabet `{⊥,0,1}`, where `⊥` is empty. Programs, a public phase counter, and the stated timing parameters are free, but none contains the payload bit.

That initial source observation is an endowed input to this comparison, such as the result of earlier productive work or a separately funded audit. Its original acquisition cost is outside the compared budget, or can be added as a common fixed charge. The study does not claim that historical observations are produced without support. A repeated implementation also needs that source-producing process to remain available.

The institution chooses and funds its architecture **before** the hidden source bit is observed. It can preserve and hand off a record, acquire a new observation, or act without one. Public schedules, resource bills, access metadata, and program choices are fixed independently of the bit. That is a restricted but explicit policy class, not an assumption that all real institutions have only one communication channel.

Every possible deterministic payload encoder from two source values to the three register symbols is admitted (nine encoders), as is every final decoder from those symbols to two actions (eight decoders). The decoder receives the current physical register and public constants only. A solver cannot recover an erased report from an observation history that its actuator never receives.

## 2. Payments, delays, and physical memory

Let:

- `g` be the gap between source observation and successor arrival;
- `h` be handoff/read latency and `f` the new-test latency;
- `δ` be the delay between report delivery and action;
- `κ` be archive capacity cost per gap slot;
- `H` be the handoff/access fee and `F` the fresh-test fee;
- `μ` be successor-register retention cost per delay slot;
- `B_early` be funds available before writing the archive and `B_late` a later transfer at succession;
- `D` be the action deadline measured from succession.

The sequence is explicit:

1. Before the source bit is observed, an archive architecture prepays `κg` for capacity through the gap. The observation is then written by the chosen encoder. The payment reserves the slot regardless of whether its content is zero, one, or empty. A reacquisition architecture can omit this archive.
2. The condition evolves during the gap. At succession the old controller is discarded and the new controller's payload register is empty. The late allocation arrives now. Neither controller has an unpriced transcript available to the final actuator.
3. Handoff pays `H`, copies the record at succession, takes `h` slots, and delivers the old observation. This fee covers custody of the in-flight payload as well as access and transmission; prehandoff archive preservation has already cost `κg`. Alternatively, the new test pays `F`, samples `X_0`, and delivers that sample after `f` slots; its fee also covers its in-flight measurement buffer. The sample is historical by the time it arrives; “fresh” does not mean magically contemporaneous after a long measurement delay.
4. Keeping a delivered report across the following `δ` slots costs `μδ`, prepaid when the report is received. If that retention is not provided, the physical successor register is reset to `⊥` before action. With zero delay no intervening retention is needed.
5. The actuator applies the fixed decoder to the surviving register. No further inquiry or action-dependent timing channel is available at this point.

Thus the inherited observation has age `a_A=g+h+δ` at action and costs `C_A=κg+H+μδ`. The reacquired sample has age `a_F=f+δ` and costs `C_F=F+μδ`. The target is the actual condition at each route's action time. Main preserve-versus-reacquire comparisons use `h=f`, so they act at the same time. Where latencies differ, the objective treats time through the explicit deadline; it does not evaluate both against an unstated common terminal condition or secretly include a delay penalty.

The funding guards are:

`κg≤B_early`, `C_A≤B_early+B_late`, and `h+δ≤D` for inheritance;

`C_F≤B_early+B_late` and `f+δ≤D` for reacquisition.

Inheritance also requires the raw archive and authorized read access. A late transfer cannot retroactively purchase earlier preservation. There is no productive input between these costs, so these prefix guards completely describe finance for the declared workflow. They do not describe all possible institutions or credit arrangements.

### Actual finite-controller memory

The material information path is

`archive = encode(source_bit)`;

`successor_register = ⊥` at controller reset;

`successor_register = archive` only if the archive survives and handoff is accessible;

`successor_register = ⊥` if retention across the action delay is absent;

`action = decode(successor_register)`.

Both program branches after erasure have the same input symbol. Memory loss is therefore implemented in the controller, not merely charged in an external accounting variable while a perfect-recall solver retains the bit. Conversely, destroying the source archive **after** a paid copy reaches a retained successor register does not erase that copy. This distinction is explicitly checked.

## 3. Exact information and quality results

### M1. Historical truth and current usefulness separate

After age `a`, the probability that the condition differs from a correctly recorded old value is

`q_a(η) = [1−(1−2η)^a]/2`.

**Proof.** Let `r_a` be the probability of odd flip parity. Then `r_0=0` and `r_{a+1}=η+(1−2η)r_a`. Solving this scalar recurrence gives the formula. Under the uniform symmetric prior, an old zero and old one have the same conditional error. For `η≤1/2`, copying the observed bit is optimal. If rates above one-half were admitted, optimal decoding would sometimes flip the bit and the corresponding Bayes error would use `|(1−2η)^a|`; they are excluded here.

The archive still accurately records the past. Staleness changes the conditional relationship between that truth and the current task. This formula is established Markov-chain mathematics and already appears in substance in the earlier research's U18; no new theorem is claimed.

### M2. Erasing the only payload register removes the decision advantage

With readable retained memory, minimum expected error is `q_a`. With the only payload register empty, minimum expected error is `1/2`, irrespective of the discarded report's former quality.

**Proof.** A surviving bit has the posterior described in M1; an injective encoder and the appropriate decoder attain its Bayes error. A noninjective encoding cannot improve on observing the bit itself. After erasure, the decoder gets the same payload symbol in both underlying worlds. All other admitted inputs are bit-independent, so it must use the same action distribution. Under the uniform prior its error is one-half. The exhaustive nine-encoder/eight-decoder search verifies this result for all tested ages and interface controls.

Randomized encoders or decoders cannot improve this expected-error optimum: the expected loss is linear in a policy lottery, and deterministic encoder/decoder pairs already include its extreme choices. This statement is specific to the declared finite protocol and objective.

**Robust special case.** If `η=0`, a correct bit can remain valid indefinitely. A paid readable retained register permits zero error for both initial conditions. If the only register is lost, no response can guarantee correctness in both worlds. A randomized response choosing zero with probability `p` succeeds with probabilities `p` and `1−p`; its best worst-case success is `1/2`, attained by a fair coin. This is a sure-impossibility result, separate from average error under drift.

### M3. An error tolerance induces an age frontier

For a declared maximum conditional error `ε<1/2`, a readable retained report qualifies precisely when `q_a(η)≤ε`. If `0<η<1/2`, this is equivalent to

`a≤log(1−2ε)/log(1−2η)`.

For integer ages, use the greatest integer satisfying the original exact inequality. At `η=0.1` and `ε=0.2`, age two qualifies (`q_2=0.18`), while age three does not (`q_3=0.244`). A larger budget cannot turn an overly stale bit into a fresher one without an available information-producing operation.

This is a task-specific validity threshold. A different error tolerance, loss, future question, or transition model changes it. It is not a universal expiration date for evidence.

### M4. Paying for preservation versus reacquisition has a conditional frontier

The model reports the full pair `(cost,error)` and separately illustrates an explicitly supplied scalar criterion `J=cost+W·error`. If both routes are affordable, accessible, timely, and retained, preservation beats reacquisition under that criterion exactly when

`C_F−C_A ≥ W(q_{a_A}−q_{a_F})`.

Equivalently, its cost advantage must cover its excess expected error. No-information response has cost zero and error one-half, so either paid route must also beat `W/2`. Under a hard error requirement, first discard every route with error above `ε`; minimizing `J` without that restriction solves a different question.

This identity is a conditional comparison, not a normative argument for one error price or for the preservation of all information.

## 4. Qualitative reversals, checked exactly

Base values are `W=20`, `κ=0.1`, `H=0.5`, `F=4`, `μ=0.2`, `h=f=δ=1`, deadline five, and ten support units available early. The archive cost is `0.1g+0.7`; the fresh route costs `4.2`. All numbers are computed as exact rational quantities before decimal presentation.

| Condition | Least-criterion route | Minimum `J` | What changes |
|---|---|---:|---|
| `η=0.1`, gap 1 | Preserve/handoff | 5.68 | Cheap recent evidence pays despite some error |
| `η=0.1`, gap 8 | Reacquire | 7.8 | Stored evidence becomes too stale |
| `η=0.001`, gap 8 | Preserve/handoff | 1.6982095665 | The same gap is acceptable for a persistent condition |
| `η=0`, gap 50 | Reacquire | 4.2 | Historical relevance persists, but paid storage becomes more expensive |
| `η=0.5`, positive delivery/action lags | No information | 10 | Every delayed bit has lost its predictive advantage |
| `η=0`, gap 1, initial bit unknown | Preserve/handoff | 0.8 | Stable information can be reused once acquired |
| Delivered register erased before action | No information | 10 | Paying for a report does not preserve its usable contents |
| Early budget zero, ten units arrive later | Reacquire | 7.8 | Equal total finance does not pay an earlier retention bill |

The independent-next-bit control does not claim that a current observation is useless. Giving reacquisition zero delivery latency and zero action delay yields a contemporaneous bit, zero error, and criterion four even at `η=1/2`.

### The scalar favorite can violate the declared quality requirement

At the base short-gap case, inheritance costs `0.8` and has error `0.244`; reacquisition costs `4.2` and has error `0.18`. The former wins the illustrative scalar criterion, while only the latter meets an error bound of `0.2`. If the fresh test instead takes three slots and the deadline is two, neither route meets that quality requirement: a cheap reachable procedure is not automatically an adequate one.

### Equal raw records and cash, different effective access

Another control begins with the **same already-paid archive** and the same remaining cash in both worlds. There is no sunk-cost difference. Handoff takes one slot; a new test takes three; the deadline is two. With handoff access, paid read plus local retention costs `0.7`, yields error `0.244`, and gives criterion `5.58`. With handoff denied, the unchanged raw record cannot reach the successor and the fresh route misses the deadline. Best attainable error is `0.5` and criterion ten.

The intervention changes an institutional/physical interface, not the underlying record or total cash. It does not identify authorization with ethical legitimacy. An alternative channel would change the result and must be included if it actually exists.

### Erasing the archive and erasing the acquired memory differ

Loss of the raw archive before acquisition removes that route, but the fresh test can still produce a usable register. Loss of the final successor register after either acquisition destroys the advantage unless another remaining action can restore it. If the source archive is erased after a paid retained successor copy exists, the copy still supports the response. The model prices which physical carrier survives; it does not equate a vanished file with amnesia in every observer.

## 5. Across scales: an exact transformation and a failure of careless aggregation

Grouping `k` elementary steps into one block gives a coarse flip rate

`η^(k)=q_k(η)`.

For every integer number of blocks `n`,

`q_{kn}(η)=q_n(η^(k))`.

**Proof.** The block correlation is `1−2η^(k)=(1−2η)^k`; raising it to `n` reproduces the fine-scale expression. The code verifies the identity in 330 exact cases. For `0<η<1/2`, the exposure `−a·log(1−2η)` determines this model's error and is unchanged by such a consistent change of time unit.

This is a genuine cross-scale equality for the declared process, not a claim that all biological, institutional, or AI change follows a binary flip law. If a coarser representation also replaces per-step storage cost with `κ^(k)=kκ`, then matched durations preserve that total bill. Yet matching endpoint statistics and aggregate cost does **not** preserve the workflow's capacity unless internal payment, access, and deadline constraints also survive the translation.

The late-financing counterexample makes the missing condition concrete: an endpoint summary can show the same total ten units in both cases while hiding that one case had nothing available when the archive had to be preserved. Its posterior formula and total accounting can be correct while its claimed admissible procedure is wrong. The companion cross-scale formalization addresses the stronger interface and prefix obligations required for policy transfer.

## 6. The side-channel counterexample that bounds the claim

It is not enough to charge for a field named “memory.” Suppose a controller sees a bit, starts with one currency unit, spends zero if the bit is zero and one if it is one, and later observes its remaining balance. Even after the named report register is erased, `bit=1−balance` recovers it exactly. A public action, latency, readiness choice, or missing message can provide a similar channel.

The program checks this two-state balance example separately. It is **excluded by construction** from the main restricted protocol because allocation, timing, and bills are fixed before observation and independent of payload. This exclusion is an interface restriction, not evidence that real actors cannot signal through budgets. A wider theory must count all surviving distinguishable channels and their actual costs. Pricing an archive while leaving an unrestricted perfect-recall controller would not satisfy that requirement.

Likewise, the free program and public phase counter are not claimed to be physically costless in reality. Here they cannot encode the hidden payload and are treated as supplied operating infrastructure. Requiring paid renewal of that infrastructure is a different extension.

## 7. Repetition and its precise limits

The solved object is a finite succession episode. It can be repeated for successive independent work items, each with a new stationary source bit, the same declared transition law, an architecture chosen before its payload, and a reliable external allotment arriving in the stated early and late tranches. The transducer resets each epoch and reuses its finite program. Paying every episode's prefix costs makes the procedure executable indefinitely under that funding promise.

For a repeated route with per-episode error `q`, expected errors over `N` independent epochs equal `Nq`, and the probability all responses are correct is `(1−q)^N`. If `q>0`, this tends to zero. Continued financed inquiry therefore does not establish indefinite correct service. If `η=0`, usable retained memory can instead supply the deterministic zero-error special case—but neither external finance nor valid access is thereby guaranteed.

This repetition is not a solved optimal policy for a single continuously evolving plant that can reuse the same archive across arbitrary later inquiries. It also does not finance itself from response success. A joint recurrent reserve model would need to specify productive returns, correlated faults, record updates, and the actual finite controller before its safety or survival claims could be assessed.

## 8. Verification and preserved artifacts

- [Executable exact checker](verification/check_paid_memory.py)
- [Complete rational results and policy witnesses](verification/paid-memory-results.json)
- [Age–persistence frontier](verification/paid-memory-frontier.csv)

The checker compares the parity formula with direct two-state transition iteration in **306 cases**; checks **330 exact time-coarsening identities**; evaluates **176,256 deterministic finite-register encoder/decoder combinations** across ages, persistence rates, access, raw-record loss, and successor retention; and records **300 age–persistence frontier points** plus fourteen discriminating cases. A payload-independent random policy cannot lower the expected error below the deterministic optimum. The constant-condition erased-register maximin bound is proved analytically and checked on a rational probability grid.

No perfect-recall optimizer is used. The final decision function has no history argument. Conversely, this is exhaustive only for the declared finite transducer and public investment choices; it is not an optimizer over all social communication arrangements. All assertions passed.

The Markov-aging formula, information-processing limit, and prefix-financing constraint have established mathematical precedents and earlier entries in this research program (especially U16, U18–U20, and U22). The current extension is the explicit paid physical register, succession reset, access comparison, and checked interaction of those constraints. Mathematical novelty and empirical cross-domain validity are not claimed.
