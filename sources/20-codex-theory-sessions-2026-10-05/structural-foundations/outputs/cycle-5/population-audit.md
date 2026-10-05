# Population audit: funded reproduction of supplied decision rules

Research audit, 5 October 2026. This cycle can close a specific gap left by the [previous selection audit](../cycle-4/selection-audit.md): decision rules now have actual, resource-funded descendants whose numbers can differ. It does not explain the origin of the outer copying institution or establish that selection generally favors persistence. The proposed mechanism is organizational practice copying with renewal of physical organizations; biological terminology is an analogy unless a biological mapping is separately established.

## What constitutes the advance

Variation, inheritance, and differential contribution are explicit when two supplied rules operate, their observable outcomes affect a specified copying procedure, and the resulting funded newborn organizations carry different rules. A fixed copying procedure does not invalidate this selection model. It defines the conditional mechanism being studied.

The distinction from a normalized frequency update is substantive. A formula such as `p′ᵢ ∝ pᵢ wᵢ` can describe fixed-size replacement, but it neither pays for replacement nor specifies absolute population size. Here the treasury first determines an integer number of affordable births. The copying procedure then assigns rule labels to those actual newborns. When no newborn is affordable, there is no population whose shares can be normalized.

Three processes must remain distinguishable:

1. The **operating rule** chooses infrastructure and repairs inside an organization.
2. The **copying rule** uses observations to choose which operating rule newborns receive.
3. The **funding and retirement rules** determine whether and when physical organizations are replaced.

The current model selects among supplied operating rules. Selection or amendment of the copying, funding, or retirement rule remains outside it.

## The proposed common-calendar mechanism

Let `S` be the one-cycle rolling planner and `L` the two-cycle rolling planner from the previous adoption model. Each newborn starts with cash 240 and no installed diagnostic channels. Both parent types operate for **two complete fault cycles** before compulsory retirement. Early scoring reads cash after cycle one; late scoring reads cash after cycle two. Births occur at the same final boundary in both treatments.

| Quantity per parent | S | L |
|---|---:|---:|
| Cash used as early score | 140 | 128 |
| Cash used as late score and returned at retirement | 100 | 136 |
| Net operating cash change over the two cycles | −140 | −104 |

Old plant and channels are destroyed at retirement, with no salvage. A newborn receives only a copied rule label; its apparatus and cash are newly funded. The supplied birth bill is `E = 240 + 16 + 4 = 260`: working cash, basic plant, and copying. Audit and record retention cost two per parent. A grant of `G=150` per active parent enters the common treasury at the start of the epoch, before the audit fee. The record contract covers the longer retention needed by early scoring.

For counts `N_S,N_L`, total `N=N_S+N_L`, and starting treasury `R`, the end-of-operation pool is

\[
P=R+(G-2)N+100N_S+136N_L.
\]

With `K` physical sites, the funded birth count is

\[
M=\min\{K,\lfloor P/260\rfloor\}.
\]

Copying determines the composition of these `M` newborns, not their funding. Treasury remainder is `P−260M`; the implemented reserve cap of 259 discards overflow **after** births are paid. The base case has four sites. There is no grant when the population is empty and no immigration or spontaneous recreation of a missing rule in the faithful-copy version.

The initial founders have a declared origin: external founding finance of 520 pays their two 240-unit cash endowments, two 16-unit plants, and two four-unit copying fees. This initial provision is separate from later recurrent grants.

### Independent accounting check

The 240-unit newborn grant is a transfer from treasury to organizational cash, not destruction of 240 units of aggregate liquid wealth. At newborn boundaries let

\[
V=R+240N.
\]

If `s≥0` is actual treasury spill, the correct liquid ledger is

\[
V'-V=150N-2N-140N_S-104N_L-20M-s.
\]

The terms are the external grant, audit payment, the two types' net operating cash changes, and the newborn plant/copy expenses. Working cash cancels as an internal transfer. Plant and channel destruction have no extra cash receipt; their loss is already represented by zero salvage and the next purchase requirement. An audit must also retain the operating model's finer payment order; this aggregate equality cannot authorize temporary borrowing.

A useful, different quantity is the **renewal-capital potential**

\[
\Phi=R+260N.
\]

It is not literal cash. It assigns each active organization its replacement-funding amount. The same update gives

\[
\Phi'=\Phi-12N_S+24N_L-s.
\]

Thus, after faithful winner copying has produced a pure `S` population, every nonempty epoch reduces finite `Φ` by at least 12. Continued renewal cannot last forever. A pure `L` population can fund at least its existing population at each renewal, since `P=R+284N≥260N`, provided `N≤K` and the cap is applied after births. This is persistence **under the continuing declared grant**, not independence from external support.

The corresponding per-parent replacement thresholds are `G≥162` for `S` and `G≥126` for `L`. These thresholds concern this exact two-cycle retirement, newborn endowment, audit fee, and plant/copy bill. They are not the earlier operating viability frontier, and they need not survive a change to those institutions.

With one founder of each type and `R=0`, the first pool is 532, producing two newborns and treasury 12. Early winner copying makes both newborns `S`; the next pool is 508, producing one newborn and treasury 248. Thereafter one `S` reduces treasury by 12 per epoch until no newborn is affordable. With epoch zero denoting the founders, extinction occurs at epoch 23. Late winner copying makes both newborns `L` and supplies a nonnegative renewal margin.

The first full liquid ledger is also exact: 480 parental starting cash, 300 grant, and 480 operating receipts equal 724 operating/installation expenses, four audit units, 40 newborn plant/copy expenses, 480 child cash, and treasury 12. Parent operating receipts and expenses were imported from the preserved microstep repair ledger, rather than created by the score.

Positive margin does not by itself prove eventual growth to every available site. For example, a reserve cap of zero discards the surplus after each renewal and can keep the population at its present size. Starting from two `L` parents, a cap below 212 can prevent accumulation of the extra 260 needed for a third birth. Report the actual reserve cap and check growth separately from persistence.

## What causes the early–late difference

The common two-cycle calendar is essential: early scoring does not give `S` a shorter generation time, earlier births, or more grant payments per physical interval. The intervention changes which observation the fixed score-to-copy rule uses. Early cash ranks `S` above `L`; final returned cash reverses that order.

Early observation need not be intrinsically inadequate. If the supplied model makes the future return inferable from the early record, a predictor can transform the early observations into the correct two-cycle ranking. Comparing raw early cash with that prediction isolates a failure of the supplied interpretation rule from a lack of available information. Prediction must use the permitted physical record, and any charged computation or storage must be included consistently.

Nor does this result show that `L` intrinsically needs reproduction to continue. Its operating apparatus can already continue in the previous model, and a short-horizon rule can maintain an inherited four-channel apparatus. Compulsory retirement and destruction create a new renewal environment in which repeated founding costs matter. Keeping those assets, allowing sale, or making retirement optional is a discriminating intervention rather than a minor implementation detail.

## Population quantities that must be reported

Report absolute live counts, births, retirements, type counts, treasury, external inflows, copy/audit expenses, and spill, with type shares only when the total is positive. A rule's share can rise while every type declines: counts `(100,100)→(50,25)` raise the first share from one half to two thirds despite its losing half its carriers.

For stochastic copying, distinguish the distribution of the share from the ratio of expected counts. In general `E[N_S/N]` is not `E[N_S]/E[N]`, and the first expression requires a convention or conditioning when extinction has positive probability. Expected numbers, positive-probability persistence, almost-sure persistence, and a robust guarantee on every admitted path are different conclusions.

The copying mechanism needs a **joint** offspring law, not only each child's marginal probability of receiving a usable rule. Siblings can share a failed source record or copying apparatus. Equal expected valid births can coexist with different extinction probabilities. The accompanying population-kernel work studies this point directly; it should not be replaced by an independence assumption introduced only during analysis.

In the proposed finite-treasury, finite-site process, stochastic copying also changes the deterministic result. Without mutation, a batch containing only `S` gives a positive route to extinction, while a pure `L` state remains a persistent class. If recurring errors can recreate `S` from every state, a sufficiently long all-`S` sequence may make extinction reachable from every nonempty state. In a finite chain, if that accessibility is verified, eventual extinction has probability one even when short-run expected performance is favorable. Such a claim requires the actual transition graph, including funding and record failures; it cannot be inferred from a mean copying rate alone.

## Time and scale controls

Changing a time label or observing every second epoch does not change the underlying copying events. For an unchanged augmented Markov kernel `Q`, exact two-epoch observation uses `Q²`, retaining the internal births, bills, and failures. Replacing the underlying rule by one that scores only once every two epochs is a different mechanism. If intermediate safety is tested, preserve a failure flag or path event in the sampled state rather than inspecting endpoints alone.

Similarly, increasing site count from four to eight is a physical intervention. It can change saturation, stochastic extinction probabilities, and the reserve required for growth without changing per-organization operating bills. It is not a coordinate relabeling. Compare treatments on the same physical time interval and report how founding capital, treasury cap, grants, and copying capacity scale with sites.

The grant `150N` supplies more outside money when there are more active organizations. This is an explicit open-system assumption. The per-parent replacement margin can be the same at different sizes while total external support differs. Fixed-total grants, congestion in copying or auditing, and shared resource depletion are separate scale interventions whose effects should be tested, not presumed invariant.

## Discriminating controls

| Intervention | What it identifies |
|---|---|
| Neutral copying with the same funded births | Differential selection versus population financing alone |
| Predict two-cycle return from the same early record | Available information versus the supplied raw-score interpretation |
| Charge or erase the retained early record | A useful observation versus its later physical availability |
| Stop the external grant; provide only enough treasury to pay the first audit | Dependence on continuing outside support |
| Retain installed apparatus at succession | Inheritance of assets versus copying only a rule label |
| Remove compulsory retirement or allow priced salvage | The contribution of physical replacement to renewal cost |
| Vary site count with a fixed total grant, then with a fixed per-parent grant | Physical scale versus expanding outside support |
| Faithful copying, independent errors, then a common-mode error | Mean transmission fidelity versus the joint population law |
| A finite declared duty with safe closure | Population extinction as failure versus a permitted end of the task |
| No future faults or an equally affordable alternative repair | Whether maintaining this particular infrastructure remains useful |

With no grant, treasury four pays the two founders' first audit and their final cash totals 236, below one newborn's bill of 260. Both copying rules then fail to renew. This control demonstrates reliance on the declared funding boundary; it does not erase the contrast under a different, explicitly supplied grant.

## Focused prior art and evidence limits

**Selection dynamics need an implemented fitness link.** Taylor and Jonker derive frequency dynamics from stated type-count growth rates and then identify those rates with a particular payoff/fitness specification. They discuss inheritance and switching interpretations, and show that conclusions can depend on the dynamics, including differences between continuous and discrete formulations. This is direct precedent for supplying the score-to-reproduction mechanism rather than treating a payoff table as sufficient. Their simple growth law does not supply treasury finance, paid copying, or the present timing experiment. [Taylor and Jonker, 1978, *Evolutionarily Stable Strategies and Game Dynamics*](https://static1.squarespace.com/static/5dc9917c4cdb1467e1e54c4c/t/6526a5647942e33b89ab7af1/1697031525653/1978%2Bevolutionarily%2Bstable%2Bstrategies%2Band%2Bgame%2Bdynamics.pdf), §§2–3 and closing discussion. Access: full author-linked PDF inspected; Mathematical Biosciences 40, 145–156, DOI 10.1016/0025-5564(78)90077-9.

**Resource-funded population renewal is established prior art.** Bruss and Duerinckx specify offspring, resource production, claims, and an allocation policy; only fully funded claims remain in the next population. Definitions 2.1–2.2 explicitly couple available resources to the number retained. Their model aggregates inherited resources, production, and consumption, uses specified independent random arrays, and supplies the allocation policy. It is therefore a useful structural precedent, not a substitute for the present payment chronology or an explanation of why a copying institution arises. No broad political interpretation or theorem about all societies is imported. [Bruss and Duerinckx, 2015, *Resource Dependent Branching Processes and the Envelope of Societies*](https://arxiv.org/pdf/1212.0693), §§2.1–2.7. Access: full primary electronic reprint inspected for definitions and assumptions; theorem proofs not audited. Annals of Applied Probability 25, 324–372, DOI 10.1214/13-AAP998.

**Selection identities still require a mechanism.** The earlier [literature map](../literature-map.md) and [cycle-four audit](../cycle-4/selection-audit.md) already cover Price and the cultural-transmission treatment of El Mouden and colleagues. The current contribution weights can now be generated by a supplied paid copying process. An identity decomposing their consequences does not establish the empirical correctness or inevitable evolution of that process.

**Expected population and persistence are distinct classical quantities.** Lyons and Peres give the generating-function extinction criterion for independent Galton–Watson reproduction, including almost-sure extinction for nondegenerate mean-one offspring, alongside the identity `E[Zₙ]=mⁿ`. These results ground the companion example in which expected valid population stays one while extinction occurs almost surely. The exceptional exactly-one-child case and independence assumptions matter. [Lyons and Peres, *Probability on Trees and Networks*](https://rdlyons.pages.iu.edu/prbtree/book.pdf), §5.1, Corollary 5.3 and Propositions 5.4–5.5. Access: full author-hosted PDF retrieved, printed pages 134–136 inspected; the rest of the book was not audited. This is an author-hosted mathematical reference, not an original-priority claim.

The ingredients are established. The work under evaluation is their explicit coupling to the same paid repair process, with absolute population finance, timing, and transmission made testable. No priority claim or ethical conclusion follows from the example.

## Implementation audit and remaining scope

I inspected the [funded-selection implementation](verification/check_funded_selection.py) and its [saved results](verification/funded-selection-results.json). An independent reconstruction of the weighted pool-and-binomial transition equations matched all 7,800 early/late kernel rows on `N≤4,0≤R≤259`. The independent potential calculation agrees with the implementation; the earlier microstep plant ledger supplies the two parent profiles. No substantive accounting or transition issue was found.

The deterministic late-scoring population reaches four at epoch 11. For faithful weighted copying, exact propagation through epoch 24 brackets eventual survival between 0.4553133970 and 0.4553135483 under early scoring, and between 0.6490735099 and 0.6490735989 under late scoring. These are justified by the probability already in persistent pure-`L` states and the remaining probability in mixed states; nonempty pure-`S` states are excluded because their finite potential must run out. They are not probabilities of merely remaining alive through epoch 24.

The forecast-from-early-record control has the same copying probabilities and entire funded transition kernel as late scoring on every checked state. Its success does not establish that any real organization knows or can afford the correct predictive model; that model is supplied here. The agreement decisively rejects the claim that this example requires waiting for later observations.

For symmetric independent copying errors with `0<μ<1`, there is also an analytic eventual-extinction argument in this finite model. Every newborn batch is entirely `S` with probability at least `min(μ,1−μ)^K`. Once the next batch is pure `S`, retaining that outcome for enough epochs exhausts the bounded potential. For `K=4`, `Φ≤1299`, so a block of 110 epochs suffices for a uniformly positive extinction probability from any nonempty state. Repeated conditional block bounds imply almost-sure eventual extinction. This argument establishes an asymptotic property; a finite-epoch mutation trace alone does not prove it, nor does it estimate a practically relevant extinction time.

I also inspected the completed [funded-selection memo](funded-selection.md). It preserves the common calendar, grant boundary, compulsory retirement, fixed score interpretation, and distinction between rule and asset inheritance. Its asymptotic arguments are separate from its finite exact propagation. No substantive issue was found. The source access statements above refer only to material actually inspected.
