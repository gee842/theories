# Generative capacities: a rigorous component of the integrated theory

Research memo, 2026-10-04. AI-generated working analysis, not canonical doctrine. **Status:** definitions and synthesis proposed below; the toy-model statements are derived; cross-domain transfer and originality remain unverified. No empirical results were generated for this memo.

## 1. What the formalization must preserve

The [glossary](../../../GLOSSARY.md:422) explicitly distinguishes 生生 from preservation of a particular form, increasing complexity, and maximizing options. Its requirement concerns the sources, pathways, and successor conditions of generation. The [seven gauges](../../../GLOSSARY.md:717) are a partial order with floors, not a summable objective. The canonical chapter also distinguishes responsive simplicity from option-rich rigidity. Those distinctions rule out identifying 生生 with population growth, entropy production, novelty counts, diversity, or survival probability alone.

The weakest defensible formal bridge is: **entities and practices change their prevalence while changing the resources, relations, and effective capacities through which subsequent entities and practices can arise, respond, and repair.** Whether those subsequent possibilities deserve protection requires a declared normative specification. Evolutionary dynamics do not supply it.

There are therefore three different objects: (i) actual transition dynamics; (ii) counterfactual capacities under specified perturbations and interventions; (iii) judgments about whose capacities, over which horizons, deserve protection. Combining them in one scalar would conceal disagreements instead of resolving them.

## 2. Stocks, flows, and maintained generators

Use state \(z=(n,b,c,s,\xi)\): absolute abundances \(n\), material stocks \(b\), functional capacities \(c\), selection/institutional conditions \(s\), and other state or memory \(\xi\). A useful material submodel is

\[
\dot b=Sv(b,n,c,s)+I(t)-\ell(b,n,c,s).
\]

Here \(S\) is a stoichiometric matrix, \(v\) the reaction/process fluxes, \(I\) boundary inputs, and \(\ell\) losses not already represented in \(Sv\). Accounting must avoid counting the same flow twice. Physical materials and energy require compatible balances. Trust, authority, and knowledge should not be assigned fictitious conservation laws merely because they share a diagram with material stocks.

For a maintained capability, a schematic constitutive equation is

\[
\dot c_j=P_j(n,b,c,s)-L_j(n,b,c,s).
\]

Its empirical content lies in measurable production and loss mechanisms. Capacity can remain constant while costly production continuously replaces losses. Conversely, a large accumulated stock can mask the disappearance of its renewal process. Static state indicators alone cannot distinguish a maintained library from one whose remaining copies are never repaired, taught, or reproduced.

**Biological precedents.** RAF theory identifies reaction subsets whose reactants are generated from a food set and whose reactions are catalyzed within the resulting system; see [Steel and Hordijk](https://arxiv.org/abs/1801.03953). Such structural eligibility does not by itself prove adequate rates, concentrations, energy supply, or dynamical persistence. [Montévil and Mossio](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/) formalize mutually maintained constraints acting on material processes. Their term *organizational closure* denotes productive interdependence, and can enable the responsiveness called openness in Ren's terminology. It is not equivalent to normative 闭.

The cross-domain question becomes: which functioning activities regenerate the components and constraints that make those activities possible, and where do the required inputs originate? An AI ecosystem cannot be judged regenerative by software reproduction alone while its energy, maintenance labor, human expertise, or effective oversight are treated as inexhaustible external inputs.

## 3. A relational capacity profile instead of a universal score

Fix an explicit evaluation specification

\[
\mathcal E=(A,\mathcal D,\mathcal T,K,B,T,\varepsilon),
\]

where \(A\) specifies affected parties or biological reference systems, \(\mathcal D\) disturbances, \(\mathcal T\) target functions, \(K\) protected constraints, \(B\) resource and intervention budgets, \(T\) deadlines, and \(\varepsilon\) tolerated failure probabilities.

Define \(\mathcal C_{\mathcal E}(z)\) as the set of tests in this specification that can be accomplished from \(z\): preserve or recover the relevant function by its deadline, within budget, without violating protected constraints, at the stated reliability. A test records its beneficiary, perturbation, target, budget, and horizon. This is a set of **effective, situated capabilities**, not a count of imaginable futures.

An inclusion \(\mathcal C_{\mathcal E}(z')\supseteq\mathcal C_{\mathcal E}(z)\) means improvement relative to the same tests, model, and intervention class. It is invariant to merely duplicating labels, unlike a raw option count. Many transitions will be incomparable. Beneficial transformation can remove a harmful capability; the protected test set should not include unrestricted powers of coercion simply because they are abilities. Choices about inclusion remain visible political or ethical choices.

A practical profile keeps separate entries for material renewal, functional renewal, response to disturbances, recovery from errors, legitimate revisability, and successor transmission. Human and AI applications additionally need person-indexed agency and standing. These components overlap and are not claimed to be a uniquely complete taxonomy; Ren's four, six, and seven existing criteria still require explicit reconciliation.

**Potential versus actual capacity.** A standard viability calculation asks whether some admissible policy preserves \(K\):

\[
V_T^{\rm possible}(z)=\sup_{\pi\in\Pi(z)}\inf_{w\in\mathcal W}
\Pr_z^{\pi,w}\{Z_t\in K\text{ for all }0\leq t\leq T\}.
\]

This is conditional on the policy class, information, uncertainty, and feasibility definitions. It does not establish that an institution will adopt the policy, or that its operators survive selection. A second calculation must use the actual evolving policy-generation and authority dynamics. Their difference is a deliverability gap.

[Martin's 2004 viability analysis](https://ecologyandsociety.org/vol9/iss2/art8/print.pdf) already makes resilience conditional on objectives, disturbance classes, available controls, recovery costs, and timescales. Importantly for this project, its particular lake model assumes the controlling institution can bear control costs and treats those costs as external. Endogenizing authority, resources, succession, and policy selection removes a substantive assumption. State-dependent admissible controls are already standard viability machinery; their mere introduction is not novel.

## 4. Regeneration, degeneration, and continuing generations

**Proposed operational definitions.** A regenerative episode restores or establishes specified renewal mechanisms and a protected capacity profile over a declared horizon, while respecting non-negotiable constraints. A degenerative episode weakens those mechanisms or shrinks protected effective capacities relative to a declared comparator. Neither definition requires every state variable to improve monotonically.

Temporary destruction can enable regeneration. Model it using an admissible transition region, deadlines for recovery, and separate constraints that may never be breached. Burning stored fuel to rebuild essential infrastructure can be regenerative; moving the liabilities beyond the measurement horizon cannot establish that it is.

For successors, introduce a transmission kernel \(H(dz'\mid z,\pi)\) covering replacement, reproduction, inheritance, training, or organizational succession. Track whether successors receive functioning generators and can themselves transmit them. Finite-generation recursion is operational:

\[
q_0(z)=\mathbf1_K(z),\qquad
q_{k+1}(z)=\mathbf1_K(z)\int q_k(z')H(dz'\mid z,\pi(z)).
\]

This probability describes remaining within the specified successor constraints for \(k+1\) steps under the modeled actual policy. It does not itself certify meaningful regeneration: the kernel must record renewal events or maintained fluxes, and \(K\) must include the protected capacities. Otherwise a frozen or oppressive state qualifies. A supremum over policies again measures possibility, not endogenous delivery. An infinite-horizon guarantee can be inappropriate when unavoidable extinction hazards accumulate; finite horizons, renewal cycles, and explicit hazard budgets are often more honest.

Successors need not resemble their predecessors. A neuron replacement, a succession of scientific paradigms, and a new AI architecture require different transmission descriptions. Functional persistence can coexist with identity change. Conversely, copying the current ruler, model, or genotype indefinitely is neither necessary nor sufficient for the preservation of protected generative conditions.

## 5. An exact toy model with no external maintainer

Let \(C\) be maintainers of a shared enabling stock \(E\), \(D\) users who do not pay maintenance cost \(c>0\), and \(N=C+D\). Consider positive parameters:

\[
\dot C=C(\alpha E-m-c-kN),\qquad
\dot D=D(\alpha E-m-kN),\qquad
\dot E=qC-\delta E-hNE.
\]

The population produces its enabling condition through maintainers, uses it, and experiences shared crowding. There is no guaranteed external corrector or inexhaustible supply of \(E\). This is an illustrative ecological public-good model, not a claimed novel model or a universal social law.

For \(C,D>0\), the non-maintainer share \(x=D/N\) satisfies exactly

\[
\dot x=cx(1-x),\qquad
\dot N=N[\alpha E-m-kN-c(1-x)].
\]

**Derived proposition.** Any initial \(D>0\) leads to \(N\to0\) and \(E\to0\) in this deterministic model. Proof: \(E\leq M=\max(E_0,q/h)\), because \(\dot E\leq N(q-hE)-\delta E\). Logistic comparison therefore bounds \(N\). Since \(x\to1\), \(C=(1-x)N\to0\). The equation for \(E\) then implies \(E\to0\). Eventually \(\dot N/N\leq-m/2\), yielding extinction. If \(C_0=0\), the same conclusion follows directly. The relative share remains meaningful at finite positive \(N\); its limiting value is not a surviving population.

Regeneration is possible on the invariant all-maintainer subspace. For \(\alpha=4\), \(q=\delta=h=m=1\), and \(c=k=1/2\), positive equilibria are \((N,E)=(1,1/2)\) and \((3,3/4)\). The first is a saddle; the second is locally asymptotically stable within that subspace: its Jacobian has trace \(-5.5\), determinant \(3\). Nevertheless a rare non-maintainer grows at rate \(c=1/2\) there. Thus a regenerative state can be internally maintained yet evolutionarily vulnerable.

The assumptions doing the work are costly maintenance, a constant advantage from evading it, indispensable shared support, and absence of alternative supply or selective counterpressure. Preferential benefits to maintainers, spatial assortment, or other interaction changes can overturn extinction. One must model the production and evolution of these counterpressures rather than install them as unexplained permanent virtues.

## 6. Counterexamples the integrated theory must survive

* **Stable prison:** ample resources, low mortality, effective reproduction, but no meaningful exit or challenge. Passes biological persistence; fails expressly included agency and standing constraints. Dynamics cannot derive the latter by themselves.
* **Innovative exploitation:** rapid invention makes extraction and repression more effective. Novelty increases while protected capacities decline. Novelty is not a moral gradient.
* **Creative destruction:** a form disappears while other forms inherit and enlarge protected generative functions. An identity-preservation metric wrongly diagnoses degeneration.
* **Late cooperation:** maintainers gain frequency after absolute maintenance stocks have crossed an unrecoverable threshold. A favorable selection gradient arrives too late.
* **Hidden maintenance loss:** output remains constant while training, repair, measurement competence, or ecosystem redundancy erodes. State stability conceals loss of future response.
* **Cross-scale conflict:** a cancer lineage can renew itself while damaging host functions. Specify the reference system and protected patient interests; do not turn this analogy into a classification of persons or social groups.

The late-cooperation case is empirical, not merely imaginable. [Sanchez and Gore's yeast experiments](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001547) found small populations collapsing while cooperative alleles increased, and larger populations approaching coexistence. Cheaters reduced resilience even without a substantial change in equilibrium density. These observations show why abundance, composition, and recoverability must be distinguished; they do not validate the particular equations above.

## 7. Novelty and tests that could change our minds

Novelty is relative to a representation and observer. [Taylor's analysis](https://arxiv.org/abs/1806.01883) distinguishes exploration within an existing space from changes to accessible possibilities and representations. A graph or program space can accommodate many new structures, but an enormous fixed encoding does not automatically explain their functional significance. Track experimentally demonstrated new functions, altered dependencies, and changed admissible interventions. Do not require a novelty rate to rise forever; maintenance, rest, and reversible specialization can be generative.

Three discriminating research hypotheses follow:

1. At matched present output, measured loss of maintenance flux or intervention capacity predicts poorer recovery after controlled shocks. Failure would undermine the proposed capacity indicators.
2. At matched selection incentives, changing appropriability of maintenance benefits changes whether maintainers persist and whether total support regenerates. This tests a constitutive mechanism rather than an analogy.
3. At matched nominal oversight budgets, interventions preserving transmission of expertise and independent authority improve correction after institutional or AI succession. If capacity disappears only because of a missing external subsidy, claims of self-sustaining correction fail.

The potential contribution is a coupled theory that explains both selection and the production, transmission, and destruction of its enabling capacities. The irreducible qualification is that the protected capacity profile is public, contestable, and situated. Neither a fixed universal score nor a theorem that survival is goodness follows from this construction.
