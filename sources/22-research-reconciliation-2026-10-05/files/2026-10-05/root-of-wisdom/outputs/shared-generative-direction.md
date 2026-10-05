# Formalizing a direction toward shared generativity

Research continuation for Ren, 5 October 2026. This advances the [renewal of access theory](renewing-access-to-support.md) and draws on the other sessions' work on [joint capabilities](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-FOUNDATION.md), [plural maintenance requirements](/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CAPACITY.md), and [conditional direction](/Users/ren/Documents/Codex/2026-10-05/fo/outputs/direction-of-regeneration/EXPLORATION.md). Those are earlier research contributions, not independent empirical confirmation.

**The proposed direction can be formalized as a dynamical bias toward forming and retaining relations that support a wider range of jointly realizable generative capacities.** This requires two distinct statements: what counts as wider capacity, and why actual dynamics favor it. We now have an operational definition of the first, a conditional theorem for the second, and a concrete shared-resource mechanism. Universality remains a hypothesis to establish.

The unit of explanation is the coupled situation. Its structures, resources, source access, waste, and other affected processes belong in the account. Different capacities can have incompatible demands. The success of one part does not settle the direction of the whole.

Let \(w\) describe the current situation. Fix a horizon \(H\), a family of productive functions, functional tests for the structures that perform them, and supports that must continue operating. Define

\[
\mathcal C_H(w)=\{q:\text{the joint capacity profile }q\text{ can be constructed and made functional from }w\}.
\]

The same physically implementable protocol must deliver all components together. It must pay maintenance, construction, energy, material, and timing costs. Calling a tested capacity regenerative additionally requires a specified test of renewing its enabling conditions, such as recovery after wear over a stated interval. A profile may concern replacement of an old carrier or formation of a new one. The definition does not assume that reality chooses an optimal protocol.

This gives a precise comparison:

\[
\boxed{w_+\succeq_H w_-
\quad\Longleftrightarrow\quad
\mathcal C_H(w_-)\subseteq\mathcal C_H(w_+).}
\]

Strict inclusion means an additional joint profile becomes feasible while all previously assessed profiles remain feasible. Some situations are incomparable. Inclusion is a partial order on assessed capacity regions. On physical situations it is a preorder: different situations can have the same region and therefore be equivalent for this comparison. It supplies no universal numerical score of goodness. Its meaning is relative to declared functions, protected supports, and time. Adding an omitted consequential function can overturn a comparison.

For a minimal example, suppose each of two new enabling structures needs one unit of material, while their work costs are one and two units. After upkeep and prior construction costs have been charged, let the available budgets be \((m,e)\). With sufficient production rates over the assay horizon,

\[
\mathcal C(m,e)=\{(q_1,q_2)\ge0:q_1+q_2\le m,\ q_1+2q_2\le e\}.
\]

Changing \((m,e)=(4,4)\) to \((3,6)\) makes three units of the second structure possible, but removes the possibility of four units of the first. More usable energy has not established wider joint capacity. If the material draw is also renewed, leaving \((4,6)\), every old profile remains feasible and a new one becomes feasible. The region strictly expands. The mechanism must actually produce these budgets; the definition does not provide them.

This concerns a matched-duration assay from each state. For a deadline fixed before the preceding transformation, its elapsed time must also be deducted. Giving the later state a fresh deadline would test a different claim. In linear resource models, the companion gives an exact certificate for inclusion even when resource costs and rates change.

**An order on capabilities does not yet explain a direction of motion.** For that, specify the actual transition law, starting conditions, and observation time. A strong statistical comparison says that a process assigns at least as much probability to every collection of regimes that is upward closed under the capability order. Here upward closed means that, whenever it includes a regime, it includes every assessed regime at least as capable. If this ordering fails, a particular average may still improve, but the stronger claim has failed.

A tractable special case uses certified levels \(n=0,\ldots,N\). Their assessed capacity regions must be strictly nested for a higher level to mean a strict gain in assessed capacity. A raw count of structures does not certify this. Suppose transitions add or lose one level:

\[
n\xrightarrow{\lambda_n}n+1,
\qquad n\xrightarrow{\mu_n}n-1.
\]

The rates describe the whole coupled situation after resource competition and maintenance effects. The level must be a sufficient Markov description for this calculation; otherwise retain the missing resource and structural coordinates.

With positive adjacent rates, the stationary probabilities satisfy

\[
\boxed{\frac{\pi_{n+1}}{\pi_n}=\frac{\lambda_n}{\mu_{n+1}}.}
\]

This gives a conditional direction theorem. Compare intact shared renewal, labeled \(F\), with a specified baseline, labeled \(0\). If

\[
\boxed{\frac{\lambda_n^F}{\mu_{n+1}^F}
\ge\frac{\lambda_n^0}{\mu_{n+1}^0}
\quad\text{for every adjacent pair},}
\]

then the renewal process has a stationary distribution that favors higher capability levels. Every increasing statistic of those certified levels has at least as large a stationary expectation. One strict ratio improvement makes the mean level strictly larger.

The result allows formation to become slower. For levels 0, 1, and 2, take baseline formation rates \((5/2,2)\) and loss rates \((1,2)\). Their stationary probabilities are \((1/6,5/12,5/12)\). Reduce the second formation rate to \(7/4\), but halve both loss rates. The stationary probabilities become \((4,20,35)/59\): the mean level rises from \(1.25\) to about \(1.53\). If formation slows by the same amount without lower losses, the mean falls to about \(1.21\).

These rates are stipulated effective rates, not a derived energetic implementation. They expose the needed balance. A causal explanation must show how physical renewal changes them after all relevant costs are counted. In particular, the comparison must not hide damage to other capacities by reporting only the repaired structure's lifetime.

![Capability tradeoffs and the effect of formation and loss rates](/Users/ren/Documents/Codex/2026-10-05/root-of-wisdom/outputs/shared-generative-direction.png)

The theorem describes long-run prevalence under stated support. It does not imply improvement at every moment. Indeed, starting from level 1 in this example, the renewal case initially has a smaller chance of reaching level 2 because its formation rate is lower. Loss of the assessed capacities is included in the stationary distribution. Restart from level 0 is an explicit premise; removing that route makes level 0 absorbing and changes the long-run conclusion.

**A concrete shared-material model supplies part of the physical mechanism.** Extend our capture machinery \(C\) with a second machinery \(Y\), which assembles from shared usable material \(R\), wears into degraded material \(D\), and can also help recycle \(D\). Capture still depends on \(C\); both processes draw on the same usable-energy reserve \(E\). All material remains in one conserved account.

At an active \(C\)-only state, the exact growth exponent of rare \(Y\) is \(\beta R_*-d\). Thus usable material maintained by the first renewal process can allow another process to grow, whereas it declines in the all-degraded situation. We constructed and proved local stability of a joint state with both forms continually replaced and contributing to shared recycling. The companion gives the equations, exact budget, and stability proof.

This mechanism has an instructive limit. The initial growth exponent of \(Y\) does not depend on whether \(Y\) helps recycle. Being enabled by a shared condition does not itself force a process to renew it. Also, the first machinery's abundance declines in the coexistence example. The result establishes compatible renewal of two functions, not preservation of every old throughput or inclusion of the full old capacity region. Nor have this differential-equation model's transition rates been derived into the reduced level model above. They are complementary results, not a completed multiscale derivation.

There is empirical evidence for a related causal sequence. In a long-term *E. coli* experiment, an evolved ability to use citrate changed the available metabolites; another lineage evolved to use those products. The resulting resource use and competition supported coexistence. The innovation also displaced earlier diversity. This is evidence of created ecological opportunities with tradeoffs, rather than universal expansion of every capacity. [Turner and colleagues, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10482366/).

The precise candidate for the proposed direction is therefore:

> Within a declared class of supported physical processes, endogenous renewal of shared enabling conditions biases the formation and retention of jointly regenerative capacities toward a broader capability distribution, compared with a physically matched disruption of those renewal pathways.

This is a falsifiable comparative hypothesis. Fix the process class, preparations, supplied inputs, assay family, resource accounting, and time horizon before testing. Include failed starts and collapsed runs. Compare the full capacity distribution, with incompatible gains and losses retained. A well-defined matched intervention may itself cost resources; those costs must be included. If only selected statistics improve, state that narrower result.

There are three distinct achievements here. Capability inclusion makes “wider possibilities” operational. The formation-to-loss theorem identifies a sufficient condition for a statistical direction. The shared-resource model shows a physical route by which one renewal process enables another. What remains to establish is when real shared-renewal mechanisms reliably improve the joint ratios or their richer-state counterpart across a specified class. Interconnectedness alone does not supply that sign.

This formalizes a descriptive candidate associated with the user's proposal of 善. It does not identify moral goodness with a capacity count or claim that the candidate already governs all of reality. The [mathematical companion](shared-generative-direction-mathematics.md) and [evidence record](shared-generative-direction-evidence.json) preserve the exact claims and their limits.
