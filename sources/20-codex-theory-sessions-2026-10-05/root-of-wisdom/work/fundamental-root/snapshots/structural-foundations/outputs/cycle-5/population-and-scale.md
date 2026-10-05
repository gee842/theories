# Populations, funded succession, and scale

Cycle 5 mathematical memo, 5 October 2026. This extends [actual selection and transmission](../cycle-4/selection-and-scale.md) to finite populations of physically endowed carriers. It separates differential contribution, absolute continuation, offspring dependence, and cross-scale correspondence. The results are conditional accounting and stochastic-process arguments; no new general law of evolution or mathematical priority is claimed.

## 1. The population state must include carriers and their support

At a census, write the state as

`P=( {z_i}_{i=1}^{N}, r, e )`,

where `N` is the actual carrier count, `z_i` records a carrier's plant, program, retained memory, accessible stock, age, and execution rights, `r` records any accessible shared reserve, and `e` contains the relevant common environment. A multiset suffices when identities have no further effect. When kinship, parent identity, locality, or credit relationships matter, retain those relations too.

A population transition must specify at least:

1. how carriers operate and generate observable consequences during a declared evaluation window;
2. what is measured, retained, and paid for;
3. how contribution scores affect funded allocations to successors;
4. how actual successor carriers are built, endowed, and given access;
5. the joint transmission law for their programs and records;
6. which parents retire and which assets or balances remain accessible.

A contribution weight is an input to an allocation rule. It is not itself money, physical offspring, or an endowed working process. If an observation arrives after allocation, it cannot have caused that allocation. If a parent is copied before its later failure, the earlier rule may spread despite that failure. These are temporal features of the mechanism, not implications of a generic preference for successful behavior.

After these mechanisms are supplied, a generation has an actual joint kernel

`K(P; event,P')`.

The event can include measurements, choices, fees, births, deaths, grants, and discarded balances. The state must retain any common random cause or memory needed to make this kernel a valid description. For the general statements below, state and event sets are finite or countable, every generation has a finite realized population, and the transition probabilities sum to one. An empty population is absorbing only when the declared mechanism cannot construct a new carrier from its remaining assets or external inputs.

## 2. Relative contribution is a different quantity from absolute continuation

Let `N_j` be the current number of carriers of type `j`, and `x_j=N_j/N` when `N>0`. At extinction the frequencies are undefined; assigning a surviving frequency to an empty population conceals the event of interest.

In a deterministic model with exact offspring counts

`N'_j=Σ_i N_i f_i M_ij`,

normalizing gives the familiar frequency update

`x'_j=Σ_i x_i f_i M_ij / Σ_i x_i f_i`,

provided the denominator is positive. This identity requires that its right-side count expression actually describes the mechanism. Integer rounding, inaccessible endowments, shared bottlenecks, or random offspring totals can prevent that interpretation. A deterministic fractional-mass model is another declared model, not automatically an exact finite population.

With random counts, a mean-offspring matrix can correctly describe `E[N'_j|P]` under its stated conditional transmission assumptions. That does not generally describe the expected normalized share. For example, let offspring counts be `(A,B)=(1,0)` or `(0,9)`, each with probability one-half. Then

`E[A/(A+B)]=1/2`, while `E[A]/E[A+B]=1/10`.

Neither outcome is empty. The two expressions weight differently sized realized populations differently. These outcomes can be financed by a fixed reserve sufficient for nine children; the one-child branch simply leaves unused funds. The probability distinction does not require unsupported offspring.

If the number of successor slots is fixed and positive, and each slot has type marginal `p_j`, then expected share does equal `p_j` by linearity. Independence is unnecessary for that particular mean, but it still matters for the distribution. A subsequent viability filter can make the surviving total random again.

## 3. P5.1 — Favored share can rise while all carriers disappear

Consider a deliberately small process with two types, A and B. Each live parent carries three cash units. Evaluation lasts one generation and costs one cash unit per parent. The evaluator assigns supplied contribution scores two to A and one to B. These are visible performance scores, not cash income.

After paying evaluation, parents pool their remaining cash. A child requires one unit for construction and copying plus three units of inherited operating cash. All parents retire after this allocation; no resale or outside receipt occurs. Any unallocated remainder is removed from the accessible system. Copying is faithful and every child has the same endowment and construction cost, regardless of its type.

With `N` parents, the number of funded child slots is therefore

`M=floor[2N/(1+3)]=floor(N/2)`.

Allocate these slots by largest-remainder quotas proportional to `(2N_A,N_B)`, resolving exact remainder ties in favor of A. This is the supplied finite allocation rule; contribution weights change the type distribution but do not change the available money.

Starting with 64 carriers of each type gives:

| Generation | A carriers | B carriers | A share among living carriers |
|---:|---:|---:|---:|
| 0 | 64 | 64 | 1/2 |
| 1 | 43 | 21 | 43/64 |
| 2 | 26 | 6 | 13/16 |
| 3 | 14 | 2 | 7/8 |
| 4 | 7 | 1 | 7/8 |
| 5 | 4 | 0 | 1 |
| 6 | 2 | 0 | 1 |
| 7 | 1 | 0 | 1 |
| 8 | 0 | 0 | Undefined: extinction |

The favored type takes over, but no carrier continues indefinitely. Every transition satisfies the exact ledger

`3N = evaluation fee N + construction/copy fee M + inherited cash 3M + discarded remainder`.

The initial 384 units are completely accounted for across the run. No measured score is substituted for a replenishment flow. A frequency-only account would miss the central outcome.

### General depletion lemma

Suppose a generational process has finite initial accessible stock `S₀`, no external inflow or net stock-creating conversion, nonnegative remaining stocks, and an irreversible cost of at least `c>0` per newborn. All current carriers retire by the next census; a nonempty next census therefore requires at least one new carrier. Transfers between parents, pools, and children do not create stock.

Then an empty census occurs no later than `floor(S₀/c)+1`. If the empty state is absorbing, this is permanent extinction by that bound. If retained assets can later reconstruct a carrier, the bound concerns the first interruption of active-carrier continuity; it does not locate the last possible reconstruction.

**Proof.** If the first `t` transitions all lead to nonempty censuses, at least `t` births have been funded. Their irreversible expense is at least `tc`, so `tc≤S₀`. Taking `t=floor(S₀/c)+1` contradicts this inequality. Discarded stock or additional operating costs only strengthen the obstruction. ∎

The bound is intentionally loose; the example dies in eight generations. The assumptions matter. Costless copying, arbitrarily long-lived parents, productive external inputs, or an accessible outside balance change the model. In particular, differential selection does not itself supply the omitted replenishment.

## 4. P5.2 — A constructive succession reserve condition

Consider a specified handoff with no incoming funds during construction. Suppose child `j` needs a setup/copy payment `k_j` and usable continuation reserve `r_j`. Any retained parent needs reserve `r_parent`, and a common setup stage costs `k₀`. Assume the actual assembly and transmission protocol can create the required child configurations, respects its information and authority interfaces, finishes before the parents' permitted retirement, and has no additional unpriced contention or obligation.

Then sufficient funding from an accessible common pool is

`b ≥ k₀ + Σ_j(k_j+r_j) + r_parent`.

With nonnegative payments and no intervening income, this total pays every spending prefix of a sequential implementation and leaves the specified reserves. If the listed fees and reserves are mandatory in this same handoff model, the inequality is also necessary by conservation. It is not a theorem that money alone can construct any desired carrier. Physical access, materials, duration, and the implemented program remain independent conditions; typed stocks require their own componentwise accounts or explicit conversion routes.

The reserves must refer to the actual continuation test. A child's reserve sufficient for one repair is not automatically sufficient for producing its next successor. The actual allocation must leave the reserve accessible to the child, rather than count cash simultaneously in several recipients or divert it according to an unrelated score.

### A repeated homogeneous construction

For a concrete sufficient indefinite condition, suppose each new carrier begins with reserve `R` and an actual certified operating protocol maps it to handoff cash `min(B,R+G)`, where `B` is its carried-cash cap. The certificate separately verifies every operating payment prefix from reserve `R`. Here `G` parameterizes the certified endpoint transition; merely summing receipts minus expenses does not establish that transition when intermediate spills can precede later bills. Its payment order and capping effects must be checked.

Each new child requires setup/copy expense `K` and fresh reserve `R`. If the parent produces `m≥1` children, the exact handoff funding condition is

`min(B,R+G) ≥ m(R+K)`,

equivalently

`B ≥ m(R+K)`, and `G ≥ (m−1)R+mK`.

If the actual protocol completes within the reproduction window and **every admitted joint transmission outcome contains at least one child in the same certified operating-and-reproduction class**, these conditions can be applied recursively. Starting with such a carrier, every census has a certified successor. Induction gives nonextinction and continuation along at least one certified lineage. A duty requiring several concurrent functions or a minimum population needs the corresponding stronger invariant. Producing `m` children all in that class is a stronger sufficient condition, not required for the existence of one continuing lineage.

This induction presumes the environment supplies the promised input to each continuing carrier and that simultaneous lineages do not exhaust a shared resource that the certificate treated as independent. If the promise is conditional on a population-level capacity limit, that limit belongs in the joint invariant. Parent retirement occurs only after the successor is ready. A per-copy success probability below one is not the all-outcome transmission condition.

For one child, the conditions reduce to `B≥R+K` and `G≥K`, alongside the operating and handoff certificates. For multiple children, the extra inherited endowments are real transfers that must also be funded. Multiplying contribution weights cannot replace them.

## 5. P5.3 — Offspring dependence changes extinction despite equal marginals

Give a valid parent reserve three. It prepays one operating unit, receives an explicitly external six units, and reaches handoff with eight. That funds two children, each with construction/copy expense one and reserve three. The same money and chronology apply to both mechanisms below. Invalid copies consume their funded construction and endowment and fail before the next census; they cannot donate those funds back. Valid copies can repeat the specified operating protocol.

Compare two joint transmission mechanisms, independently repeated for different valid parents and generations:

- **One protected copy:** exactly one of the two children is valid, with its position chosen fairly.
- **Independent copies:** each child is valid independently with probability one-half.

Every labeled child has marginal validity probability one-half in both mechanisms. Both produce one valid child per parent **in expectation**, and both pay for two physical births. The first mechanism has exactly one continuing carrier at every census when started from one. The second has viable count `Z_{t+1}|Z_t=n ~ Binomial(2n,1/2)`.

For independent copies,

`E[Z_t]=1` for every finite `t`, but `P(eventual extinction)=1`.

**Proof.** The conditional mean is `E[Z_{t+1}|Z_t]=Z_t`, giving mean one by induction. Let `q_t` be the probability that the lineage from one parent has no valid carrier at generation `t`. Independent sublineages give

`q₀=0`, `q_{t+1}=((1+q_t)/2)^2`.

The sequence increases and is bounded by one, so its limit `q` exists and satisfies `q=((1+q)/2)^2`. The only solution in `[0,1]` is one. Since zero is absorbing, the increasing union of finite-time extinction events is eventual extinction, with probability one. ∎

No infinite enumeration is used in this proof. The finite checker independently propagates the full viable-count distribution through seven generations, verifies the recurrence, mean one, and variance `t/2`. This is a classical critical branching-process result; the deterministic-one-child case is the essential degenerate exception, not a contradiction. See [Lyons and Peres, *Probability on Trees and Networks*, §5.1](https://rdlyons.pages.iu.edu/prbtree/). The author-hosted reference establishes classical context; the argument needed here is given in full.

The external six-unit receipt is a reliable per-valid-parent promise in this example. With a fixed shared feedstock pool, the assumed independent branching law can fail. These results do not claim that every real population with mean reproduction one goes extinct, or that marginal error rates alone identify the relevant population process. Dependence across siblings, across parents, and across generations must all be specified.

## 6. P5.4 — A full population process can transfer across scale

Let `L` and `H` be actual population processes, with state map `φ` and event map `χ`. Their states contain absolute counts, endowed configurations, common funds, clocks, controller memory, and common environmental state to the extent those affect the future. For all relevant concrete states and abstract event/next-state pairs, require

`Σ_{χ(e_L)=e_H, φ(P'_L)=P'_H} K_L(P_L;e_L,P'_L)`

`= K_H(φ(P_L);e_H,P'_H)`. **(PK)**

Assume corresponding initial distributions and corresponding tests. Then translated concrete population trajectories have the abstract joint path law. If `φ(P_L)` is empty exactly when `P_L` is empty, extinction probabilities agree; matching only normalized frequencies does not supply this condition. Cash units and test thresholds must also be translated explicitly when financial quantities are compared.

**Proof.** Conditional on every concrete past, (PK) gives the same projected next-event/state distribution as the abstract kernel. Induction gives equality of all finite cylinder probabilities. For countable state and event spaces these cylinder probabilities determine the path law. No finite population truncation is needed for this argument, but each declared kernel must be normalized and the state must contain the requisite memory. ∎

This is the previous closed-loop kernel theorem applied to population states, with its countable extension justified by the same nonnegative sums. It is not a new branching or evolutionary theorem. The extra substantive work lies in exhibiting a population-level correspondence.

A phase-by-phase sufficient certificate matches:

- evaluation windows, observations and their actual timing;
- measurement, record, construction, and transfer expenses;
- the actual funding/allocation mechanism, including rounding and caps;
- the joint program-and-endowment transmission mechanism;
- common shocks, parent retirement, and retained reserves;
- the child's subsequent interpretation of the transmitted rule and its usable information.

Every-prefix safety and bounded construction time remain necessary obligations of this sufficient implementation certificate when one generation hides multiple physical steps. An exact census kernel cannot by itself prove that no unsafe or insolvent internal state was visited. For adversarial rather than stochastic populations, use the cycle-4 actual transition relation condition uniformly over admitted environmental choices, with the same prefix and progress qualifications.

### Composition

Two population correspondences `L→M→H` satisfying (PK) compose by `φ_LH=φ_MH∘φ_LM` and `χ_LH=χ_MH∘χ_LM`. Sum the lower-level probabilities first over middle fibers and then over abstract fibers. Since all terms are nonnegative, rearranging the countable sums is valid. Initial distributions compose in the same direction. The result preserves the actual population mechanism, not merely the availability of a better reproduction policy.

## 7. Independent replication is not exact stochastic packet scaling

An exact constructive population map can group `a` corresponding carriers into a packet. Every operation, expense, reserve and contribution is replicated; corresponding packet members share the same evaluation and transmission outcome. Separate packets may still act independently. If allocation respects these packets, the detailed counts stay divisible by `a`, and dividing by `a` recovers the original joint process.

The checker verifies this kind of map for two-type populations with up to four source packets, nontrivial mortality and mutation, and packet factors two and six. It checks every one-step count kernel and the composed projection. This is a useful exact certificate, but its common-outcome assumption is substantive.

For contrast, one carrier surviving with probability one-half has extinction probability one-half after the transition. Two synchronized corresponding carriers have the same extinction probability, and their normalized count is either zero or one. Two independent carriers instead have survivor counts `0,1,2` with probabilities `1/4,1/2,1/4`; extinction probability is one-quarter. Both pairs have expected survivor count one. Independent replication improves this particular survival probability while failing the proposed exact normalized-count law.

Pooling can break a deterministic scaling claim too. In general,

`floor(aF/E) ≠ a floor(F/E)`.

Newly pooled remainders may fund additional children. To assert exact correspondence, restrict allocation to the scaled image, retain packet rules, or prove that the extra possibilities leave the actual selector unchanged. The same issue arises when a larger system gains intermediate designs, shared equipment, new communication routes, or different evaluation windows.

Changing the number of carriers is therefore neither automatically a unit conversion nor automatically a harmful or beneficial change. One must identify which budgets, dependencies, and selectors change with it. A correspondence can preserve some first moments while changing extinction, tail risk, or the probability that a protected lineage survives.

## 8. Integration and scope

The [companion population experiment](funded-selection.md) links contribution scores to the earlier short- and longer-horizon repair selectors. This memo supplies complementary constraints and counterexamples: absolute stock must fund endowed successors; rising share can coexist with depletion; actual offspring dependence controls continuation; and a cross-scale prediction needs the full selection-and-transmission law.

None of these results identifies reproductive contribution with ethical merit. A mechanism may favor traits that impose costs on other carriers or outside the model boundary. Continued existence, a large share, and protection of the declared functions are different tests. Their evaluation requires an explicit account of affected parties and external inputs.

The mathematical core is closed once the state, environment, costs, allocation, transmission, and test are fixed. Empirically identifying those mechanisms, explaining the origin of the evaluation rule, or extending the representation to new practices remains open work. The examples do not solve every level of selection or establish a universal empirical scaling law.

## Preserved verification

The [exact standard-library checker](verification/check_population_scale.py) verifies the eight-generation depletion ledger; 21,600 reserve-guard identities; full independent-branching distributions through seven generations; the random-denominator counterexample; 405 population-kernel projection rows; and 135 composed projections. It also compares independent and synchronized physical replication. [All assertions passed](verification/population-scale-results.json).

The unbounded extinction and continuation claims rely on the proofs and assumptions above, not extrapolation from those finite checks.
