# Joint organization and the emergence of parts

New research branch for Ren, 5 October 2026. The [current theory](root-of-wisdom-formalization.md) and all earlier deliverables are preserved unchanged. This branch investigates a question beneath the previous starting point: **what warrants treating the world as particular parts with particular degrees of independence?**

The strongest next candidate is:

> **Joint organization constrains which combinations are possible and which distinctions can function as relatively autonomous parts. The separation of parts must be justified at the scale where it is used.**

The earlier theory explains how interactions select effective laws and how responses reveal missing distinctions. This branch adds that a missing distinction can concern the organization of already known components. It also shows, in a specified model, how a connected process supports distinguishable units over a calculable range of times. These are substantive steps toward understanding unity and differentiation together. Whether one concrete whole ultimately grounds everything remains a further question.

## What makes this a new direction

Three questions precede treating local descriptions as a description of the whole:

| Question | What must be established |
|---|---|
| Can the descriptions coexist? | At least one joint realization satisfies them. |
| Do they determine the joint realization? | No consequential joint difference remains unresolved. |
| Can their subjects be treated independently? | The relevant possibilities, statistics, or dynamics factor in the required way, exactly or to a justified approximation. |

These are different questions. Agreement on overlaps need not establish coexistence. Coexistence need not establish determination. Neither establishes independence.

For a classical set of jointly possible configurations \(\Omega\), let \(\pi_i\Omega\) be the possibilities of component \(i\). Then

\[
\boxed{\Omega\subseteq\prod_i\pi_i\Omega.}
\tag{1}
\]

Equality says every combination of individually possible values is jointly possible. Strict inclusion means a description that assumes free recombination invents forbidden possibilities. This is relative to the specified physical regime: an intervention that changes the constraint can change \(\Omega\).

Even equality of these sets does not establish statistical independence. A distribution may give positive probability to every combination while assigning probabilities that cannot be recovered by multiplying the component distributions. Nor does statistical independence in one preparation establish dynamical independence under interventions. Each proposed separation needs the appropriate test.

## A consequential relation can be absent even when every variable is present

Here is the clearest new answer to the original missing-possibilities question.

Let \(n\ge2\), with \(x_i\in\{-1,+1\}\). For any \(-1\le\tau\le1\), define

\[
\boxed{P_\tau(x_1,\ldots,x_n)=2^{-n}\left(1+\tau\prod_{i=1}^n x_i\right).}
\tag{2}
\]

Every proper subset of these variables has exactly the same uniform distribution for every value of \(\tau\). Yet

\[
\boxed{\mathbb E_\tau\left[\prod_iX_i\right]=\tau.}
\tag{3}
\]

**Proof.** The probabilities are nonnegative and sum to one. When at least one variable is summed out, its two signs cancel the product term, leaving a uniform marginal. Multiplying by the product of all signs before summing instead cancels the constant term and leaves \(\tau\). □

For three variables, one distribution can permit only an even number of negative signs and another only an odd number. Each individual variable and every pair look statistically identical. A measurement of all three signs together distinguishes the distributions perfectly. For \(0<|\tau|<1\), the same failure of local determination persists even though every configuration is possible.

For nonzero \(\tau\), the law also fails to factor across every nontrivial partition of the supplied coordinates into two blocks: both block marginals are uniform, so multiplying them would give \(P_0\), not \(P_\tau\). This is a claim about these physically interpreted coordinates, not every conceivable change of representation.

The missing relation can change a decision. Suppose an action \(a\in\{-1,+1\}\), selected before a fresh sample, receives payoff \(a\prod_iX_i\). Its expected payoff is \(a\tau\). The laws \(P_{+\eta}\) and \(P_{-\eta}\), with \(0<\eta\le1\), therefore require opposite optimal actions despite identical proper-subset marginals. A rule using only those marginals has worst-case expected regret at least \(\eta\), even if randomized. If it chooses \(+1\) with probability \(q\), its two regrets are \(\eta[1-(2q-1)]\) and \(\eta[1+(2q-1)]\); their maximum is minimized at \(q=1/2\).

**No independent physical variable was missing from this example. What was missing was how the known variables fit together.** Adding parity as a derived feature would repair this particular description; it would not create an additional physical degree of freedom.

The information restriction matters. Knowing all proper-subset probability distributions differs from possessing aligned observations of every variable from the same trial. Such aligned observations recover full joint samples. Likewise, the payoff example establishes a decision consequence under a supplied distribution, not a causal effect of intervening on the variables.

## Local agreement can conceal global impossibility

Consider three binary quantities. Each pair is claimed to be perfectly anticorrelated, with both signs individually equally likely. All pair descriptions agree on their overlapping one-variable distributions. But no common classical joint distribution can satisfy them: the three requirements would give

\[
X_1X_2=X_2X_3=X_3X_1=-1,
\]

whose product is simultaneously \(+1\) and \(-1\).

A quantitative version survives imperfect correlations:

\[
\boxed{\mathbb E[X_1X_2]+\mathbb E[X_2X_3]+\mathbb E[X_3X_1]\ge-1.}
\tag{4}
\]

For every jointly defined sign triple, the sum is either \(3\) or \(-1\); averaging proves the inequality. If the three pair correlations all equal \(-\rho\), their joint realization requires \(\rho\le1/3\). This threshold is attainable by assigning equal probability to the six configurations that are not all equal. Mixing that distribution with independent uniform signs realizes every \(0\le\rho\le1/3\).

The general sign-constraint result is equally direct. Assign each edge of a finite undirected graph a required relation \(x_ix_j=s_{ij}\), with \(s_{ij}\in\{-1,+1\}\). A satisfying assignment exists exactly when

\[
\boxed{\prod_{e\in C}s_e=+1\quad\text{for every cycle }C.}
\tag{5}
\]

Multiplication around a cycle proves necessity. For sufficiency, choose one root sign per connected component and propagate along a spanning tree. The cycle condition makes every remaining edge consistent. A realizable graph with \(c\) components has exactly \(2^c\) assignments. The relations determine all signs up to one overall choice per component.

There is also a positive composition theorem. If finite-variable pair distributions are arranged on a tree and agree on their shared one-variable marginals, they always have a joint extension. Root the tree and set

\[
P(x_V)=p_r(x_r)\prod_{i\to j}p(x_j\mid x_i),
\tag{6}
\]

using the supplied edge-to-node ratios where the parent probability is positive and any normalized conditional row otherwise. Summing leaves proves normalization; induction from the root proves the required marginals. Zero-probability parent rows contribute nothing. This construction selects a particular conditional-independence extension; the local information need not uniquely require it. The parity family already supplies alternative extensions on a three-node path.

These are elementary instances of the established marginal-extension problem. The original mathematical literature studies which patterns of overlapping domains permit such extensions. [Vorob’ev, 1962](https://www.mathnet.ru/eng/tvp4710).

The practical gain is specific: when separately satisfactory accounts fail together, inspect their joint constraints, shared resources, and identification of supposedly common variables. Further detail inside each account alone may leave the contradiction intact.

## How a connected process supports relatively separate units

The negative results identify when separateness fails. A constructive result identifies when a useful form of separateness emerges.

Take four sites with nonnegative quantities. Exchange within the pairs \(\{1,2\}\) and \(\{3,4\}\) occurs at rate \(k\). Each of the four edges between pairs has rate \(\varepsilon/2\). Both rates have units of inverse time. For example,

\[
\dot x_1=k(x_2-x_1)+\varepsilon\left(\frac{x_3+x_4}{2}-x_1\right),
\tag{7}
\]

with the corresponding symmetric equations for the other sites. The generator preserves nonnegativity and total amount. For \(\varepsilon>0\), all four sites belong to one connected exchange process.

Define the pair means \(a=(x_1+x_2)/2\), \(b=(x_3+x_4)/2\). Addition and subtraction give

\[
\dot a=\varepsilon(b-a),\qquad\dot b=\varepsilon(a-b),
\]
\[
\boxed{
\begin{aligned}
x_1(t)-x_2(t)&=[x_1(0)-x_2(0)]e^{-(2k+\varepsilon)t},\\
a(t)-b(t)&=[a(0)-b(0)]e^{-2\varepsilon t}.
\end{aligned}}
\tag{8}
\]

The other within-pair difference follows the first equation. Internal differences can therefore disappear quickly while differences between the pairs remain.

The complete decay spectrum is \(0,2\varepsilon,2k+\varepsilon,2k+\varepsilon\). When \(\varepsilon>0\) and \(k>\varepsilon/2\), the slowest nonconstant mode is unique up to multiplication: its vector is \((1,1,-1,-1)\). Separating its positive and negative entries recovers the two pairs, up to exchange of their names. Thus an explicit spectral criterion selects the coarse partition from the generator. It does not uniquely select an ontology under every possible criterion.

For a relative tolerance \(0<\delta<1\), require internal contrasts to shrink to at most \(\delta\) of their initial magnitudes while the between-pair contrast retains at least \(1-\delta\). A uniform time window for these requirements is

\[
\boxed{
\frac{\log(1/\delta)}{2k+\varepsilon}
\le t\le
\frac{-\log(1-\delta)}{2\varepsilon}.
}
\tag{9}
\]

The window exists exactly when its lower endpoint does not exceed its upper endpoint. For \(\delta=0.05\), this requires approximately \(k/\varepsilon\ge57.904\). With \(k=100\), \(\varepsilon=1\), the window is approximately \(0.01490\le t\le0.02565\). Nonzero initial pair contrast, or a permitted preparation that excites it, is needed to observe that distinction.

An absolute error bound specifies what the coarse description omits. Reconstruct \(\widehat x=(a,a,b,b)\). Then

\[
\|x(t)-\widehat x(t)\|_\infty
=\frac12e^{-(2k+\varepsilon)t}
\max\{|x_1(0)-x_2(0)|,|x_3(0)-x_4(0)|\}.
\tag{10}
\]

The pair means have an exact closed joint law. Each pair remains coupled to the other, so neither has exact individual autonomy when \(\varepsilon>0\). Over the stated window, their internal coherence and slowly changing means justify treating them as two relatively autonomous coarse units for these quantity predictions.

The limiting cases explain the conditions of this result. At \(\varepsilon=0\), the pair dynamics decouple exactly, although initial statistical correlations can remain. At \(k=0<\varepsilon\), the proposed pair contrast disappears faster than their internal differences, defeating the intended separation. At \(k=\varepsilon/2>0\), all six edges are identical and all nonconstant decay rates coincide; the spectral criterion selects no preferred pair partition. Naming groups does not supply the missing rate separation.

The general importance of weak interactions between internally organized subsystems is established in Simon’s work on near decomposability. The four-site calculation here is a deliberately small, explicit realization with an error bound and degeneracy checks, not a claim to have originated that research tradition. [Simon, 1962](https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf).

This is emergence of effective units from specified microscopic dynamics. It does not derive microscopic sites or the historical formation of their couplings. Preparations or interventions that alter those couplings require a new analysis. That boundary identifies a meaningful next step: explaining how the structures that support separateness are formed and maintained.

## What physical theories add to the interpretation

The classical examples do not impose a classical ontology on every physical domain. In quantum theory, one must distinguish a joint physical description from a simultaneous assignment of context-independent values to every possible measurement. Abramsky and Brandenburger establish, under their formal assumptions, an equivalence between a factorizable hidden-variable realization and a global distribution over such assignments. Failure of that extension concerns that representation; it does not imply that actual experimental records cannot belong to a coherent account. The anticorrelated triangle above is a mathematical witness, not a claimed quantum experiment. [Abramsky and Brandenburger, 2011, theorem 8.1](https://arxiv.org/pdf/1102.0264).

A constructive quantum counterpart also exists. Zanardi, Lidar, and Lloyd show how suitable accessible observable algebras, satisfying independence and completeness conditions, induce a tensor-product subsystem structure. This supplies an established example of subsystem identification tied to operations and measurements. It does not mean that a person's belief creates physical parts or that every system has a uniquely preferred decomposition. [Zanardi, Lidar, and Lloyd, 2004, proposition 1](https://arxiv.org/pdf/quant-ph/0308043).

There is empirical reason to take restrictions on composition seriously. Hensen and colleagues reported a Bell test using electron spins separated by 1.3 kilometres, obtaining \(S=2.42\pm0.20\) and rejecting their specified local-realist null at reported \(P\le0.039\). This supports a particular failure of local hidden-variable explanations under the experiment's assumptions. It does not distinguish every monist and pluralist ontology. Only the primary report's abstract and stated result were reviewed here; no data reanalysis was performed. [Hensen et al., 2015](https://www.nature.com/articles/nature15759).

## What the other sessions contribute

The newest generative-foundation synthesis derives persistence and collapse from specified replacement, support, decay, and practice-copying mechanisms. Its composition theorem requires local operating conditions to hold together, including shared resources and permissions. Those results strengthen the physical implementation of the retained theory. They still supply their initial carriers, component boundaries, and mechanisms. The present branch asks how such a division becomes warranted.

An older strand of the user's corpus already explores operation and distinction monism through \(\Sigma(X)=X\times X\). Its valid conditional insight is that one operation determines a whole tower once the seed is fixed. For finite seeds,

\[
|T_j|=|X|^{2^j}.
\tag{11}
\]

Different seed sizes give different towers; a one-element seed remains a singleton and a two-element seed produces sizes \(2,4,16,256,\ldots\). The shared rule provides unity of formal construction. A physical interpretation additionally needs actual composition laws, observables, dynamics, and an account of their realization. The repository's claim ledger itself distinguishes carrier-level results from wider semantic claims. This branch preserves that construction and investigates the additional physical burden.

The new participation work also supplies a useful constraint on the philosophical interpretation: one jointly organized process can contain participants with different information, burdens, and reasons to continue or refuse. Dependence does not erase those differences. Source paths, hashes, review scopes, and the inherited-versus-new distinction are recorded in the [evidence file](next-root-evidence.json). Other sessions' experiments were not rerun here.

## The step toward monism

The supported advance is **differentiation without presumed independence**. Joint organization can contain information absent even from every proper-subset probability distribution, constrain what can coexist, and support particular relatively autonomous parts. Distinctness and unity can therefore coexist in a substantive model.

Several philosophical hypotheses can accommodate this. Priority monism holds that one concrete whole is fundamental while its many parts depend on it. Existence monism asserts only one concrete object exists. Substance monism concerns the uniqueness of substance under a particular account of substance. These are different theses. Schaffer explicitly separates the existence of parts from their fundamentality and supplies additional assumptions about metaphysical priority. [Schaffer, 2010, sections 1.1–1.3](https://www.jonathanschaffer.org/monism.pdf).

Spinoza's route likewise requires substantive premises about substance, attributes, and existence before reaching the uniqueness conclusion in *Ethics* I, proposition 14. It is a distinct argument rather than a consequence of statistical dependence. [Spinoza, *Ethics* I, definitions 3–6 and propositions 5, 11, 14–15](https://www.gutenberg.org/cache/epub/3800/pg3800-images.html#chap01).

Our current results are compatible with a differentiated common process. They are also compatible with **relational pluralism**: several real entities with real relations. A shared mathematical representation cannot settle that contest. Nor does needing joint information establish that the whole metaphysically grounds the existence of its parts. Formation, interaction, predictive dependence, and grounding are distinct explanatory relations.

The strongest positive position at this stage is therefore:

> **A unified process can support real differences and relatively autonomous parts. A satisfactory account must explain both their shared constraints and the conditions under which their separateness works.**

The unresolved comparison is precise: does treating the whole as fundamental explain the constitution and persistence of its parts better than treating entities and their relations as jointly fundamental? Future progress should identify an explanatory asymmetry or a warranted difference between those accounts. Repeating that everything is connected would not answer it.

## Consequences for wisdom and the next investigation

The retained theory asks what generates consequences, what evidence corrects our distinctions, and how action changes future conditions. This branch adds three concrete checks: whether the pieces can work together; whether their local descriptions omit a joint consequence; and whether their apparent independence survives the relevant time scale and intervention.

This provides a new search direction when no local anomaly is apparent. The missing possibility may be an untested combination, a relationship absent from the description, or a boundary that only works under old conditions. A joint experiment, a composition check, or a change of scale can reveal it. The parity example demonstrates why searching solely for additional components cannot guarantee finding such a gap.

The ethical connection remains reasoned rather than automatic. Shared dependence can reveal consequences imposed on others; it cannot alone rank their interests or turn a whole into a morally privileged beneficiary. A theory of unity must remain able to represent distinct experience, agency, refusal, and harm.

The next investigation is now well specified: allow the coupling structure itself to change through a supplied local formation or maintenance mechanism; derive when coherent boundaries emerge, survive perturbation, and dissolve; then ask whether that process gives a stronger account of the identity of its parts. This would advance from deriving effective units in a given organization to explaining the production of that organization. It is a next research burden, not a completed result of this branch.

## Verification and status

The general conclusions rest on the displayed proofs. Exact constructed checks additionally covered 59,808 signed graphs, 35 parity distributions and their 2,505 proper-subset marginals, 4,374 tree distributions including zero-probability cases, and 49 rational parameter pairs for the four-site generator. Its mode reconstruction was also checked on 81 rational states. Decimal time-window examples are numerical illustrations of analytic inequalities.

The [evidence record](next-root-evidence.json) includes the check programs and results, source provenance, review corrections, and hashes demonstrating preservation of all 19 pre-existing output files. No new physical or participant experiment was conducted. The established mathematics is used and rederived here without claiming historical novelty; the proposed next root and its connection to wisdom are the synthesis developed in this branch.
