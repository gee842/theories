# Generativity through supporting conditions

Research continuation for Ren, 5 October 2026. The starting correction is that generativity requires conditions: our lives on Earth participate in a larger relation that includes the Sun. This develops the [endogenous renewal theory](endogenous-renewal-and-consequential-feedback.md) by making usable energy, its retention, and the timing of supply part of the dynamics.

**Dependence on conditions belongs in the foundation of the theory.** A process can be generative over a finite period, supported by other processes, without producing every condition of its own existence. The explanatory task is to show how its particular organization participates in, retains, and renews the conditions that make further activity possible.

There are two new mathematical results. A supplied-energy model has an exact constant-power threshold for a maintained active regime. The same model also admits an exact contrast: one average power supports a stable active equilibrium when supplied continuously, while sufficiently long interruptions at that same average power force activity to disappear. The arrangement across time matters as well as the amount.

## The supporting relation includes conversion and release

For Earth, the relevant physical account includes incoming sunlight and outgoing thermal radiation. Radiative balance describes their energy exchange; it does not mean that the incoming and outgoing radiation have the same capacity to drive transformations. [NASA on Earth's energy budget](https://science.nasa.gov/earth/earth-observatory/climate-and-earths-energy-budget/).

Usable work depends on disequilibrium and on mechanisms that can exploit it. Photosynthetic conversion can retain some solar photon energy in chemical form before it becomes ambient heat. Bounded steady dissipative operation also requires net entropy export. These dependencies connect local material cycling with a larger irreversible flow. [Kleidon's thermodynamic analysis](https://arxiv.org/html/1103.2014).

This does not require treating the organism and its surroundings as separate realities. A boundary specifies which exchanges we must track. Enlarging it brings the source and receiving surroundings into the same account. Local regeneration can be supported by a larger gradient that is itself changing or being depleted.

The different roles are consequential: some conditions are supplied by the wider situation; some are retained in reserves; some are regenerated through current activity; others are changed by that activity. Calling all of them simply “the environment” can hide these differences.

## Usable energy becomes a changing part of the model

Retain usable material \(R\), renewal machinery \(C\), and degraded material \(D\), with \(M=R+C+D\). Add a usable-energy reserve \(E\), supplied usable power \(P(t)\), reserve loss rate \(\ell E\), and work cost \(\varepsilon\) per unit recycled. Powered recycling has flux \(J=kECD\):

\[
\begin{aligned}
\dot R&=J-aR, & \dot C&=aR-bC,\\
\dot D&=bC-J, & \dot E&=P(t)-\ell E-\varepsilon J.
\end{aligned}
\]

Here \(P\) means usable power delivered to this reserve, after whatever capture and conversion are required. It is not all incident sunlight. The energy reserve is consumed by the same renewal activity that it enables. Machinery still assembles from available material and still wears out.

The model gives the exact joint balance

\[
\boxed{\frac{d}{dt}\big[E+\varepsilon(R+C)\big]
=P(t)-\ell E-\varepsilon bC.}
\]

The left side combines available work and active material in the model's work-equivalent accounting. Input must cover reserve loss and machinery wear if this combined capacity is to be maintained. Finite reserves can bridge a shortage; continued supply can sustain activity beyond the finite-stock limit. The equation is a reduced accounting model, not a complete molecular thermodynamic derivation.

## A constant supply has a precise threshold

For positive rates and fixed \(M>0\), define

\[
\boxed{P_c=\frac{\ell b}{kM}.}
\]

With constant \(P\le P_c\), all active material eventually vanishes: \(R,C\to0\), even if the initial energy reserve is arbitrarily large but finite. A reserve can delay this outcome without replacing adequate continuing support.

For constant \(P>P_c\), there is exactly one positive equilibrium, and it is locally asymptotically stable. More supplied usable power increases the equilibrium machinery amount, which approaches a finite material limit. Global convergence from every active starting state has not been proved for this extended model.

The threshold reveals several distinct conditions. More effective conversion \(k\), greater material availability \(M\), lower wear \(b\), and better reserve retention through lower \(\ell\) change which regimes are possible. Supporting a particular nonzero machinery level additionally depends on its work cost \(\varepsilon\). No one rate or resource describes the whole capacity to continue.

![Power threshold and equal-average supplies with different outcomes](/Users/ren/Documents/Codex/2026-10-05/root-of-wisdom/outputs/conditions-of-generativity.png)

The figure uses a constructed, dimensionless model with all rates and total material set to one. It is not a fit to terrestrial day and night or to an organism. The left curve gives equilibria; the right trajectories start from the same active equilibrium.

## Equal average support can permit different futures

In this same model, continuous supplied power \(P=1.2\) supports a stable active equilibrium. Now provide \(P=2.4\) for 30 time units, followed by zero for 30, and repeat. Each complete cycle supplies exactly the same usable energy as continuous \(P=1.2\).

Nevertheless, the intermittent case makes \(R,C\to0\) from every initial state with finite reserves. This conclusion is proved by bounding each cycle's effect on the remaining active material, not inferred only from the plotted trajectory.

The causal issue is that the machinery needed to use returning support also wears out during interruptions. The reserve loses availability; the material becomes degraded; later power encounters a different situation. In this example, repeated strong supply cannot offset that cumulative loss of active organization.

Energy continues arriving even as regenerative activity fades. The final material state is all degraded, while the energy reserve approaches a periodic pattern. Thus the failure is neither absence of average input nor literal disappearance of all energy. It is a failure of the particular supply, retention, conversion, and renewal arrangement to sustain activity across time.

Changing storage, wear, dormancy, or routes for renewed activation can alter the result. Their existence and costs must then enter the account. The counterexample establishes that average input alone is insufficient; it does not claim that intermittency always prevents regeneration.

## The present includes the state of supporting processes

This clarifies our earlier discussion of depending on the present. A present description that retains only average sunlight or average power has discarded a causally consequential distinction. The current reserves, remaining machinery, and position within the supporting cycle affect what can happen next.

For periodic forcing, one can include phase \(\theta\) in the state, with \(\dot\theta=1\) around the cycle and \(P=P(\theta)\). Then \(W=(R,C,D,E,\theta)\) describes the joint situation needed for these dynamics. In a fuller physical account, the phase belongs to the source and its relation to the supported process. This is consistent with the sufficiency of a suitably complete present; it shows why an impoverished present summary is insufficient.

It also sharpens the meaning of possible futures. A reaction can be chemically allowed yet unavailable at the required rate, time, or material state. A sufficient supply averaged over a month can fail to support a process through a particular interruption. Continuation depends on a realizable sequence of supporting conditions.

## The revised foundation

The current working statement is:

> Generativity is a capacity of a coupled situation: available differences can be converted into activity, some activity renews its enabling capacities, and the supporting conditions remain compatible with that renewal across time.

This statement proposes what the broader theory should explain. The equations establish particular instances and failure conditions. They do not yet define every kind of generativity, explain open-ended novelty, or derive which physical laws supply the available transformations.

The Sun example therefore leads to a stronger research direction: explain how local organizations maintain their participation in larger supporting processes, and how their activity changes those processes in turn. The next extension would make capture and storage themselves wear, form, and alter the supply they can use. That would bring another currently supplied condition into the same causal account.

The [mathematical companion](conditions-of-generativity-mathematics.md) contains the threshold proof, stability result, budget, and exact timing counterexample. The [evidence record](conditions-of-generativity-evidence.json) records checks, source scopes, and preservation of all prior outputs.
