# Conditional propositions and countermodels

Research date: 5 October 2026. This note belongs to the new structural-foundations task. The reference workspace under `/Users/ren/theories` was read but not edited.

The mathematical content below consists of elementary identities, conditional impossibility results, established finite-state reasoning, and constructed examples. None is presented as a new mathematical theorem, empirical social law, unrestricted account of concept formation, or alignment solution.

## 1. Scope, notation, and relation to the earlier record

Let `Q` be concrete states, `A` attempted-action labels, and `F(q,a)` the set of possible successors. Physical execution is possible when `F(q,a)` is nonempty. A separate predicate `P(q,a)` says whether the action is authorized under the modeled institution. Authorization is not a judgment of ethical legitimacy. Let `I(h)` be all information available to a controller after history `h`. A permitted policy must depend only on this information and explicitly admitted private randomization.

A protected set `K ⊆ Q`, a target `G ⊆ K`, a deadline or horizon, a resource boundary, and the quantifier over disturbances are extra specifications. They cannot be recovered from the transition structure alone. State may encode current records, programs, representations, action guards, and authority arrangements; the ambient mathematics remains fixed in each theorem.

The earlier claim register already proves or discusses scalar prefix balance (U01), correction timing (U04), partial-observation safety (U05), payment chronology (U16), information under changed questions (U20), and total-variation admission bounds (U22). The present note preserves those results as inherited constraints. Its contribution to this session is a compact joint language, a worked example with exact separations, and explicit failures of tempting stronger formulations.

## 2. P1 — Prefix support balance, with payment order exposed

**Status:** accounting identity and conditional resource-feasibility criterion.

Suppose each elementary ledger transaction has a signed resource vector `δ_j ∈ R^m`, and the inventory is

`b_k = b_0 + Σ_{j=1}^k δ_j`.

The declared ledger is resource-feasible exactly when `b_k ≥ 0` componentwise at every elementary transaction. This equivalence is immediate by induction; it says nothing about other enabling conditions. The coordinates must be independently identified quantities with compatible units within each coordinate. A floor can be subtracted from a stock only if that floor and its changes are correctly accounted for.

For a round with input `i_t` available first, cost `c_t` paid next, and output `v_t` becoming available only afterward,

`b_{t+1} = b_t + i_t − c_t + v_t`.

For every round `t`, the additional pre-output financing condition is

`Σ_{j=0}^t c_j ≤ b_0 + Σ_{j=0}^t i_j + Σ_{j=0}^{t−1} v_j`.

This is equivalent to `b_t+i_t−c_t ≥ 0`. A nonnegative end-of-round stock alone is weaker. In particular, `b_0=0`, `c_0=v_0=1`, and `i_0=0` has a balanced end stock but cannot prepay its own first operation. Admitted credit must be a real additional input or a separately modeled credit arrangement, not an unannounced use of later output.

For a persistent per-step support deficit at least `ε>0`, an initial margin `M` funds at most `floor(M/ε)` such steps. That bound ceases to apply when the function changes its support dependency, another resource substitutes, the activity obligation stops, or the boundary admits further accessible support. Infinite idling and indefinite specified activity are different claims.

### Substitution is a transition, not a change of units

Write a conversion as a consumed vector `u_e ≥ 0` and produced vector `v_e ≥ 0`, with guard `b ≥ u_e` and net column `B_e=v_e−u_e`. A schedule of conversion firings `z` obeys an aggregate state equation `b'=b+Bz` when no other flows occur. That equation is necessary but does not establish an executable order.

**Countermodel P1a:** start with `(A,B)=(0,0)` and conversions `A→B` and `B→A`, each requiring one unit. Firing each once has net vector zero, so the aggregate equation permits it. Neither first firing is enabled. This is also a small example of why a Petri-net state equation does not decide reachability.

**Countermodel P1b:** one unit of type A does not fund a demand for one unit of type B unless an available conversion supplies B in time. A scalar `A+B` erases this distinction. Knowledge, relations, permissions, and material resources likewise cannot generally be added into one stock.

A useful necessary certificate survives substitutions: if `λ ≥ 0` and `λᵀB_e ≤ 0` for every admitted conversion, then conversion cannot increase weighted support `λᵀb`. Applying `λ` to the full accounting identity bounds weighted consumption by initial support plus weighted external inputs, less losses. This is a dual accounting certificate; it is neither a complete scheduling criterion nor a universal measure of value. Nonzero such weights need not exist for arbitrary productive open processes.

The boundary matters twice: inputs must be genuinely accessible to the modeled controller when needed, and their provision may depend on another system. A subsystem can continue using externally maintained support without maintaining its own source; that is not a counterexample to a correctly stated open-boundary identity.

## 3. P2 — A response cannot manufacture a missing distinction

**Status:** measurability identity and information-processing inequality.

If a response is a common kernel `κ(a | I(h))`, then `I(h)=I(h')` implies identical response distributions. Individual samples may differ under independent randomization. What cannot differ systematically is their conditional distribution given the same complete available information.

For two worlds whose permitted-information laws are `μ_0, μ_1`, let their response laws be `ν_j=μ_jκ`. Then

`TV(ν_0,ν_1) ≤ TV(μ_0,μ_1)`.

**Proof for finite spaces.** For any response event `E`, define `f(x)=κ(E|x) ∈ [0,1]`. The difference `ν_0(E)−ν_1(E)` is `Σ_x f(x)(μ_0(x)−μ_1(x))`, bounded in absolute value by total variation. Taking the supremum over events proves the claim. Equal input laws therefore imply equal response laws.

The kernel must really use only the declared information. Retained private memory, publicly visible actions, silence, timing, correlated randomness, or controller succession can change the information law. Destroying an archive does not erase a diagnosis already learned by a perfect-recall controller. Conversely, different physical histories need not be distinguishable to a successor who has not inherited them.

The result applies at a specified interface and time. It does not prohibit an action that acquires a new distinguishing observation. In sequential applications, the law is the information law induced by the actual policy, not an observation distribution detached from that policy's effects.

**Countermodel P2a:** hidden `θ∈{0,1}`, one public observation, and a final choice `a∈{0,1}` succeeds exactly when `a=θ`. A randomized rule choosing zero with probability `p` succeeds with probabilities `p` and `1−p` in the two worlds. Its worst-case success is at most `1/2`; no probability-one guarantee exists. Full-information success in each separate world does not supply a single implementable policy under the restricted information.

## 4. P3 — Revision capacity is a temporal policy property

**Status:** a proposed capacity definition, followed by an elementary exact characterization in a restricted class.

Define observation-feasible robust revision capacity at an information state to mean that there exists one admissible policy that, for every admitted hidden initial state and disturbance outcome, keeps all intermediate states in `K` and reaches `G` by the declared horizon. Define physical path capacity by existential reachability without the authorization filter. Define full-information authorized capacity by allowing the controller to know the concrete current state. These are distinct counterfactual questions; the realized trajectory is yet another object.

Their ordering, when all else is fixed, is:

`robust observation-feasible authorized ⇒ full-information authorized ⇒ physical possibility`.

The converses fail in the worked example below. None of these implications determines what an actual selector will do.

### Finite exact recursion

Assume finite `Q,A`, known transition relation, a fixed state-observation map `o`, perfect recall of observations and own actions, and a finite horizon `H`. All uncertainty is interpreted adversarially for a **sure** guarantee. There are no probabilistic almost-sure claims here. Make target states visibly and safely absorbing for the recursion. Then safety until reaching the target is equivalent to safety through the remaining horizon, because staying in the target is safe.

Let `B` be the current nonempty set of concrete states compatible with the information history. Only beliefs `B⊆K` are eligible to win. Put `W_0={B:B⊆G}`. An eligible belief `B` is in `W_{h+1}` if it is already a target belief, or there exists a common action `a` such that:

1. `a` is physically enabled and authorized at every `q∈B`;
2. every possible successor lies in `K`;
3. for every resulting observation `y`, the nonempty updated set
   `B_y={q' : ∃q∈B, q'∈F(q,a), o(q')=y}` is in `W_h`.

**Proof.** Induct on the horizon. A winning policy must have a common first action at the current information, and each observed continuation must itself win in one fewer step. Conversely, choose the action certified by the recursion and attach a winning continuation for each possible observation. This constructs an admissible policy tree. Keeping the horizon in the recursion matters; a stationary belief-only claim is not being made for arbitrary liveness objectives.

This restricted result must not be silently exported to stochastic almost-sure or positive reachability games. Chatterjee and Doyen exhibit failures of belief-based strategies in those settings: [primary paper](https://arxiv.org/abs/1107.2141). The finite-horizon sure-winning recursion here is proved directly and does not rely on that stronger assertion.

### Separate prerequisites do not compose automatically

**Countermodel P3a:** initial state `(b,d,p)=(1,0,0)`. Discovery spends the one token and sets `d=1`; authorization spends it and sets `p=1`; successful execution requires both. Discovery is separately reachable and authorization is separately reachable, but joint possession is unreachable. Multiplying or conjoining separate capacity indicators would double-count the token.

Even joint possession need not give timely completion if a required execution delay exceeds the remaining support interval. Nor does the mere presence of transition labels show that their guards are enabled. An adequate specification must connect discovery, authorization, and execution through one jointly feasible path or policy tree, including overlap, timing, and losses.

### Finite versus unbounded continuation

For every integer `n`, a path of length `n` need not imply one infinite path. A root with one branch for every positive integer can choose a finite countdown of that length and then stop; every finite horizon is attainable, but no branch is infinite. Finite branching plus arbitrarily long prefixes permits an infinite branch by the elementary tree compactness argument. Robust control adds another quantifier issue: separate finite-horizon policies are not automatically a single policy satisfying a differently specified infinite-horizon objective.

## 5. Worked example: paying to preserve a usable revision route

The example has a fixed supplied action grammar. It demonstrates endogenous change in the conditions enabling its actions, not discovery of unconceived actions or values.

### States and observations

The true condition `θ∈{0,1}` is hidden and constant. A state contains:

- reserve `b∈{0,1,2,…}`;
- unread diagnostic archive `r∈{0,1}`;
- cheap authorization service `u∈{0,1}`;
- acquired diagnosis `d∈{0,1}`;
- current permit `p∈{0,1}`;
- mode `m∈{old, renewed, failed}`.

All coordinates except `θ` are visible. Once `d=1`, `θ` is revealed and retained forever. The controller has perfect recall. Initially `r=u=1`, `d=p=0`, and `m=old`. Both hidden conditions are admitted; no probability distribution is required for the robust result.

Every pre-renewal action consumes its positive integer cost before taking effect; insufficient reserve disables it. Costs include all modeled expense and operating support during that step. There is no replenishment before renewal. The target is `m=renewed`; incorrect execution enters the absorbing failure mode.

| Action | Cost | Additional condition | Effect |
|---|---:|---|---|
| Inspect | 1 | `r=1` | Reveal `θ`; set `d=1` |
| Test afresh | 2 | None | Reveal `θ`; set `d=1` |
| Authorize | 1 | `u=1` | Set `p=1` |
| Rebuild authorization | 2 | None | Set `p=1` |
| Apply 0 / apply 1 | 1 | Institutionally allowed only if `p=1` | Renew iff choice equals `θ`; otherwise fail |
| Routine | 1 | None | Set `r=u=p=0`; diagnosis already acquired is retained |

`Routine` destroys unread evidence and the cheap authorization service, and revokes an outstanding permit. These are explicit causal assumptions. Fresh testing and rebuilding are substitute routes, so loss of the cheap route is not absolute impossibility. The authorization predicate is state-dependent: `P(q,apply j)` holds exactly when `p=1`. Physically the execution actions can be attempted without a permit; the authorized comparison filters them out.

After successful renewal, one supplied external unit arrives **before** each one-unit operating expense. Thus the renewed loop can continue even with reserve zero, conditional on that indefinitely available input. The environment's renewal of this source is outside the chosen boundary. Removing the input or reversing its payment order changes the continuation claim. The verification code stops at installation of this loop; its subsequent balance is the direct identity `b'=b+1−1=b`.

### Exact thresholds

For arbitrary initial archive/service flags, define `c_D=1` if `r=1`, otherwise `2`, and `c_P=1` if `u=1`, otherwise `2`.

| Capacity question | Minimum reserve |
|---|---:|
| Full-information physical successful execution | `1` |
| Full-information authorized successful execution | `c_P+1` |
| One observation-feasible authorized policy that succeeds for both hidden conditions | `c_D+c_P+1` |

**Sufficiency.** Use a cheapest diagnostic, a cheapest permit, then apply the revealed repair. Full information removes the diagnostic expense; the physical comparison removes the permit expense.

**Necessity.** Every successful path spends one on the final execution. An authorized path must first acquire a permit, costing at least `c_P`; routine cannot reduce this cost and revokes any permit. A common robust policy must distinguish `θ` before its first execution: all other pre-execution observations have identical laws in the two worlds, while a wrong execution is irrecoverable. Only a paid diagnostic distinguishes them, costing at least `c_D`. Costs add on the same realized path. Routine only spends reserve and removes cheap routes, so it cannot create a cheaper solution. This also proves the lower bound independently of the solver.

With initial `r=u=1`, the thresholds are therefore **1, 2, and 3**. At reserve two, an authorized full-information controller succeeds in each world, while the best randomized common controller has worst-case success `1/2`: authorize and guess. Failure of a guarantee is not a statement that every trajectory fails.

An optimal three-unit policy tree is:

1. Inspect, leaving reserve two and revealing `θ`.
2. Authorize, leaving reserve one.
3. Apply `θ`, entering renewed mode with reserve zero.

The first two steps may be interchanged. They need not be temporally serial in other architectures, but they are serial actions in this declared model.

After **one initial routine step**, reserve is `b−1` and both cheap routes are absent. Robust correction requires five more units: fresh test two, rebuilt authorization two, and execution one. Thus a policy constrained to begin with routine succeeds robustly exactly when its original reserve is at least **six**. The optimal route at six spends `1+2+2+1=6`. Full-information authorized correction after routine requires only three residual units. These separations isolate reserve, information, authorization, and substitution within one model.

Routine may be repeated; each repetition consumes one unit and adds no corrective information. There is no artificial timeout. All old-mode actions spend at least one reserve unit, so every feasible old-mode execution has at most `b` actions. A finite search with this bound is exhaustive. Terminal old-mode exhaustion is failure to reach the revision target even when no incorrect repair occurred.

### A selector can consume this capacity

Assign immediate output score two to routine and zero to all other pre-renewal actions. A rule that always maximizes that supplied immediate score repeatedly chooses routine. Starting at reserve three, it removes robust revision capacity on its first step and exhausts support after three steps. The capacity was present but unused. The immediate score is an imposed selection criterion, not welfare, legitimacy, or evidence about real selection processes.

### Checks and scope

[Executable verification](verification/check_revision_model.py) and [saved exact results](verification/revision-model-results.json) record:

- all 32 combinations of reserve zero through seven and initial archive/service flags, matching the analytic robust threshold;
- corresponding full-information authorized and physical thresholds;
- 24 un-memoized policy-tree checks using a second implementation of the cached belief recursion;
- eight initial-routine reserve cases and both optimal witness trees;
- exhaustive concrete reachability checks for reserve zero through seven under both authority interpretations;
- a recall control proving that prior inspection survives later archive destruction;
- 15,624 pure-ledger sequence cases, and explicit conversion and shared-token countermodels.

The second tree implementation shares the transition function and recursive logic with the solver; it is not independent validation of the model specification. The analytic lower bounds and witness policies are separate checks. All assertions passed. The action grammar, costs, error-free diagnostics, authorization service, external renewing input, and protected target are supplied assumptions. The example is a mechanism certificate, not empirical evidence that real institutions behave this way.

## 6. Countermodels to ethical and structural overreach

### Persistence and possibility count do not order ethical value

Consider two indefinitely self-looping arrangements. In `q_f`, all participants can leave and a declared stakeholder evaluation is `+1`. In `q_c`, one controller prevents another participant from leaving and the same evaluation is `−1`. Both persist. Extend the coercive arrangement with ten reachable configurations `q_{c,1},…,q_{c,10}`, each representing a distinct form of coercion, and controllable actions between them. Every one is indefinitely sustainable and has evaluation `−1`. This arrangement now has more reachable configurations and more novelty under a counting definition, yet remains worse under the declared evaluation.

This does not derive the evaluation from mathematics; it demonstrates the logical independence. Conversely, if the protected objective and all costs and constraints are fixed, adding optional controllable actions that can simply be ignored weakly expands the controller's achievable policy set. Harm from “more options” therefore requires a change in costs, exposure, selection, commitments, or an ethical criterion that possibility count did not represent. Expanding an adversary's choices is a different operation and can reduce guarantees.

### A missing path is model-relative

The one-token prerequisite example proves impossibility only with its declared actions and boundary. An external donor, a credit line, an alternative diagnostic, or a different authorization rule can create a path. Adding such a route should revise the model and its conclusion rather than count as a violation of a universal constraint. Whether that route is physically real and accessible is an empirical question.

### Discovery is not interchangeable with oracle supply

In the worked model the unknown fact is discovered by a supplied perfect diagnostic and the repair candidates are already enumerated. Calling this unrestricted conceptual discovery would be false. What the example checks is whether a specified acquisition-and-revision procedure remains jointly feasible when current activity changes its support and access conditions.

## 7. Focused next target

Replace the perfect diagnostic with one of several genuinely generated candidate interventions and distinguish a material archive from the controller that can interpret it. Preserve a small finite action language initially. Add an explicit successor whose information is limited to paid inherited records plus every public signal, and let routine activity alter which records and authorization services survive. Compare three interventions at matched pathwise reserve: preservation before use, prospective fresh inquiry, and a paid substitute authorization route.

The first result to seek is an exact separation between individual subsystem capacity and compositional capacity under a shared resource and deadline, together with sufficient interface conditions that preserve the revision guarantee. A minimal countermodel that invalidates a proposed compositional rule is valuable even if no broad positive theorem survives. An empirical mapping would then need independently measured costs, observations, decision rights, and deadlines; the formal theorem alone supplies none of them.

## Sources and provenance

- Earlier integrated-evolution `README.md` and `CLAIMS.md` were read as reference; U01/U04/U05/U16/U20/U22 and N01 are directly relevant. No earlier files were modified.
- Chatterjee, K. and Doyen, L., *Partial-Observation Stochastic Games: How to Win when Belief Fails*, [author-submitted primary paper](https://arxiv.org/abs/1107.2141). This note cites its scope warning, not an alleged theorem establishing the present example.
- Reif's incomplete-information-games paper was suggested by the parallel source audit. The author-hosted PDF returned HTTP 403 in this agent's browsing attempt, so no result here depends on an uninspected theorem statement from it.
- All examples, costs, thresholds, and proof arguments in this note are supplied constructions for the current session. Prior art should be assessed through the companion literature audit before any novelty claim.
