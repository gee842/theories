# Generality, prior art, and testable transfer

Independent review, 5 October 2026. Scope: the meta-attractor programme, situated correction, and the proposed general framework. This is a conceptual and targeted prior-art review, not a complete priority search or proof audit of the entire corpus.

## Verdict

The user is right to reject a financial boundary around the programme. Money was one implementation of support, incentives, and maintenance. The more general object is **a system whose activities transform the conditions of their own continuation and revision**. Those conditions can include material support, inherited environments, learning data, standards of assessment, organizational rules, and agents' available interpretations and actions. They need not include money, a conscious evaluator, a common objective, or gradient descent.

A useful proposed synthesis is therefore:

> Study how locally situated activities change the conditions that retain, support, assess, and revise those activities; identify when this coupling preserves possibilities for further response and when it erodes them.

This framing can have explanatory and practical value before it becomes a single predictive theory. It directs attention to omitted state variables and interventions. For example, a successful practice can be changing the selection process, exhausting its support, or suppressing the experience that would reveal its damage. However, writing an arbitrarily expressive state-transition model does not establish any of those mechanisms. The framework becomes explanatory when it restricts which couplings are present, their direction and timing, and the observations that could contradict those restrictions.

The financial results remain valid conditional constructions. They demonstrate that some coupled mechanisms can be integrated consistently and can yield exact persistence and loss results. They do not define the limits of the wider research question, and they do not prove that every domain follows their equations.

## The appropriate level of generality

Distinguish four claims:

1. **Framework:** identify relevant kinds of entities, relations, feedback, and change. Its value is organizing inquiry and exposing omissions.
2. **Mechanistic family:** specify a shared causal pattern, such as successful practices increasing control over subsequent assessment, or maintenance being depleted by the activity it supports.
3. **Conditional model and theorem:** specify dynamics, admissible disturbances, response mechanisms, and an exact conclusion.
4. **Empirical transfer:** independently identify those mechanisms in another setting and test the predicted response to interventions.

This hierarchy is not a retreat from generality. It is how a general framework supports different precise models without requiring all domains to be identical. Ostrom explicitly distinguishes frameworks, theories, and models, while connecting institutional outcomes back to rules, community attributes, and biophysical conditions. Her account also rejects reducing diverse motivations and institutional forms to one market-style model. [Ostrom, *Beyond Markets and States*, Nobel lecture, 2009, especially sections 2–3](https://www.canr.msu.edu/fsp/outreach/presentations/Ostrom_Nobel_Lecture_27_October_2016.pdf).

The proposed domain map should preserve different mechanisms:

| Setting | What continues or changes | How it changes its future conditions | A crucial distinction |
|---|---|---|---|
| Meritocracy and bureaucracy | People in roles, routines, promotion standards | Appointments, classifications, reporting channels, rule changes | Promotion is not biological reproduction; measured performance may differ from public purpose. |
| Democracy and politics | Coalitions, laws, mandates, public interpretations | Agenda setting, constitutional change, participation and contestation | Persistence or electoral victory does not establish legitimacy or justice. |
| Ecosystems and evolution | Organisms, traits, populations, ecological relationships | Resource modification, ecological inheritance, density dependence | No central evaluator or intentional rule designer is required. |
| AI development and deployment | Parameters, policies, datasets, evaluation and deployment practices | Behavior changes future observations, training distributions, and institutional decisions | Backpropagation may be one local update method; it is not the entire coupled system. |
| Living organization | Metabolic and regulatory processes, boundaries, repair capacities | Processes sustain or disrupt conditions required for their own operation | Material conservation, spatial organization, and timescales cannot be replaced by generic financial accounting. |

Some modules are optional. A cell population need not possess political authority; an ecosystem need not contain an agent with a representational frame. Conversely, human deliberation and changing commitments should not be compressed into a fixed biological fitness function.

## Closest established foundations

The general direction has substantial scientific grounding. It should be presented as a proposed integration and extension of established lines, not as the discovery that feedback exists everywhere.

| Primary source | Relevant established structure | Consequence for this programme |
|---|---|---|
| [W. Ross Ashby, *An Introduction to Cybernetics* (1956)](https://www.ashby.info/Ashby-Introduction-to-Cybernetics.pdf), especially chapters 1, 6, and 11 | Functional comparison across physical domains, coupled regulation, and constraints relating relevant disturbances, available responses, and possible outcomes | A common formal vocabulary is legitimate. Domain analogies still require appropriate variables and mechanisms. Requisite variety is not a command to maximize undifferentiated diversity. |
| [Laland, Odling-Smee and Feldman, *Evolutionary consequences of niche construction and their implications for ecology* (1999)](https://pmc.ncbi.nlm.nih.gov/articles/PMC17873/) | Organisms alter environmental resources and thereby change subsequent selection; the article develops a population-genetic model | Evolution already includes modification of selection conditions. This is a nonfinancial, nonintentional antecedent of the proposed reciprocal structure. |
| [Tilman, Plotkin and Akçay, *Evolutionary games with environmental feedbacks* (2020)](https://www.nature.com/articles/s41467-020-14531-6) | Strategy composition changes environmental conditions, which change payoffs and strategy dynamics; outcomes depend on incentives and timescales | This is particularly close mathematical prior art. Shared architecture does not entail a common attractor, or inevitable degradation. |
| [Perdomo, Zrnic, Mendler-Dünner and Hardt, *Performative Prediction* (2020)](https://proceedings.mlr.press/v119/perdomo20a.html) | A prediction used in decisions changes the distribution against which later prediction is assessed; retraining stability requires conditions | AI feedback is broader than parameter optimization against a fixed dataset. Conditions of evaluation can be endogenous without implying a universal objective. |
| [Ostrom, *Beyond Markets and States* (2009 lecture; revised AER article, 2010)](https://www.canr.msu.edu/fsp/outreach/presentations/Ostrom_Nobel_Lecture_27_October_2016.pdf) | Nested institutional analysis, rules in use, multiple decision centers, and context-dependent mechanisms of cooperation | Broader institutional interpretation is supported; a single fee-and-enforcement mechanism is not a universal prescription. |

The particular emphasis worth developing is the joint reproduction of **selection conditions, material support, and the capacity to revise the frame of selection**. The first two already have extensive foundations. The third adds a demanding research problem: distinguish acquiring evidence within a fixed representation from changing what can count as evidence, what actions are conceivable, and what purposes are endorsed. A general state variable for these changes is a starting point, not yet a mechanism explaining them.

Autopoiesis and enactive approaches are relevant conceptual neighbors for this last issue, but this review does not establish that their technical definitions transfer to every institution or ecosystem. They should not be used as a license to call every feedback network a living organization.

## Three falsifiable cross-domain hypotheses

These are proposed restricted hypotheses. Their contribution would be demonstrated transfer of a mechanism, not novelty of feedback itself.

### H1. Success that changes future selection produces additional persistence

**Claim:** When a retained practice can alter future selection conditions, and the resulting advantage returns to that practice soon enough to exceed its costs, access to this pathway increases its persistence after its original direct performance advantage disappears.

**Test:** At matched immediate success and available resources, enable or block the pathway from current success to future assessment or environment modification. Measure the proposed mediator separately: altered appointment rules, changed future training/evaluation data, or persistent environmental modification. Then remove the original advantage and compare persistence.

**Candidate settings:** Promotion systems with versus without incumbent influence over subsequent rubrics; AI development loops with versus without model influence on later evaluation data; microbial niche modification with environmental carryover versus reset.

**Failure and boundary conditions:** Shared spillovers can advantage noncontributors; delayed returns, independent rule revision, negative density dependence, or rapid environmental renewal can eliminate or reverse the effect. Persistence alone does not distinguish this mechanism from switching costs or direct resource advantages. Those alternatives require controls.

### H2. Local restoration can fail through cross-level coupling

**Claim:** In a specified operating range, systems with restoring dynamics at each isolated level can lose stability when positive cross-level feedback exceeds restoration. Current output alone then understates vulnerability to perturbation.

**Minimal exact case:** For deviations satisfying the actual linear equations

\[
\dot u=-\alpha u+\beta v,\qquad
\dot v=\gamma u-\delta v,
\]

with positive restoration rates and nonnegative couplings, the joint equilibrium is unstable when \(\beta\gamma>\alpha\delta\), despite stability of either isolated subsystem. This is established linear stability mathematics, not a new theorem.

**Test:** Estimate restoration rates and cross-responses from separate perturbations, before fitting the joint outcome. Manipulate or interrupt the coupling, then predict recovery rates or stability in held-out joint perturbations. Possible mappings include reporting pressure and institutional responsiveness, or production load and biological repair, provided each variable has an independent physical or behavioral measurement.

**Failure and boundary conditions:** A failed conservative upper-bound certificate is not observed instability. Delays, sign changes, saturation, hidden states, and extrapolation beyond the measured regime invalidate the two-variable criterion. “Correction capacity” cannot be defined retrospectively as whatever made recovery occur.

### H3. Usable information and executable response can be complementary

**Claim:** When observationally indistinguishable situations require incompatible timely actions, restoring only diagnostic access or only response capability cannot guarantee successful correction; restoring both can.

**Test:** Independently manipulate timely informative access and actual ability to act, using a factorial design with matched budgets and delays. Measure the context-dependent outcome independently of the intervention. Candidate mappings include staff testimony and revision rights, AI evaluation and authorized changes to deployment, or cellular sensing and downstream effectors.

**Failure and boundary conditions:** The interaction can disappear if existing observations already distinguish the situations, a single common action works, or the purported information is false or too late. Cells have effectors, not democratic standing; that difference must remain explicit. This hypothesis transfers an information-and-control obstruction, not the normative meaning of each intervention.

## Findings that do not transfer by relabeling

- **Excludable service finance:** A privately recoverable benefit and a fee-funded maintenance equilibrium do not imply that all correction should be privatized. Nonexcludable benefits, collective financing, reciprocity, coercion, and kin structure change the mechanism.
- **Scalar monetary copying:** Replication proportional to private receipts is not a universal model of decisions. Duty, learning, trust, rights, deliberation, mutation, and coercion require different operators.
- **Truth and majority:** The earlier governance model's constant truthful fraction follows from equal payoffs within a deterministic practice class. It is not a law of cultural or biological persistence. Its median guarantee also depends on authenticated weights, a common scalar quantity, and bounded errors; it is not a theorem about democratic legitimacy.
- **Cycles and attractors:** The earlier model's special monotonicity cannot rule out cycles elsewhere. Likewise, positive feedback can saturate, stabilize a beneficial regime, or be counteracted by other loops. It does not entail unbounded accumulation or domination.
- **Resources:** Energy, material, attention, status, money, and evidence differ in conservation, rivalry, transferability, and renewal. A vector of distinct resources is often necessary. A scalar exchange rate needs justification.
- **Normative judgments:** Persistence is not justice; organism-level viability is not the welfare of every component; lower measured error can reflect a weakened standard. Changing evaluative criteria must be tracked separately from changing material outcomes.

## Review of the proposed general mathematical core

The small-gain comparison route proposed by the math workstream is appropriate as a genuinely nonfinancial conditional result. For nonnegative measures \(V\), positive diagonal \(D\), nonnegative \(B\), and bounded forcing \(d\geq0\), a comparison inequality

\[
D^+V\leq(-D+B)V+d
\]

can yield invariant bounds when \(\rho(D^{-1}B)<1\). The inequality must hold throughout the region and times under discussion, and forward existence must be justified. The spectral condition certifies the original system only in the sufficient direction; its failure is not a converse instability theorem for an arbitrary nonlinear system. Standard positive-systems and small-gain mathematics must receive attribution.

The saturating example \(\dot x=-x+k\tanh r,\ \dot r=-r+k\tanh x\) usefully demonstrates that individually restoring components can produce multiple joint regimes. Its positive and negative branches carry no ethical meanings by themselves.

For a moving criterion \(b(s,\psi)\), including the contribution \(\nabla_\psi b\cdot\dot\psi\) in its derivative is essential. Otherwise changing goals can masquerade as recovery. This does not make all goal change suspect; it makes the distinct sources of change visible.

## Recommendation

Present the broader programme as a **situated theory of mutually changing practices and their conditions of continuation and revision**, with several conditional dynamical models underneath it. Its present strength is a coherent question, substantial established mathematical roots, and increasingly explicit constructive examples. Its potential contribution is showing that a small number of measured feedback mechanisms explain and predict interventions across otherwise different domains—including how the criteria and possibilities of correction themselves change. That contribution remains to be established empirically and against closer specialized prior art.

The strongest next evidence is not another claim of universality. It is one mechanism, independently operationalized in two contrasting domains, that predicts a held-out intervention and identifies in advance when the transfer should fail.
