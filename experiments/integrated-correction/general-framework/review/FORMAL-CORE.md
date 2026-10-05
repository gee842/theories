# A nonfinancial formal core: systems that change their own conditions of continuation

5 October 2026. Mathematical proposal for the broader research programme. This extends the [situated-correction architecture](../../../evaluator-succession/SITUATED-CORRECTION.md) and the [multilevel framework](../../systems-dynamics/review/MULTILEVEL.md). It does not replace them with another financing model. The mathematical tools below are established; their proposed integration and cross-domain interpretation remain a research hypothesis requiring application-specific mechanisms and evidence.

The common object is a system in which activity changes the conditions that subsequently shape activity, continuation and change. Some such systems also form and revise interpretations, purposes and institutions. This formulation neither assigns intentions to all life nor assumes that every persistent pattern replicates, optimizes a scalar, competes, or receives a reward.

## 1. A shared architecture with typed differences

Use an augmented state

\[
s=(e,n,\mu,r,\{\phi_i,b_i,\succeq_i\}_{i\in\mathcal A}).
\tag{1}
\]

Here \(e\) contains environmental and material conditions; \(n\) contains typed relationships; \(\mu\) records retained configurations or activities; and \(r\) records currently implemented transition rules. The optional agent set \(\mathcal A\) carries frames \(\phi_i\), beliefs \(b_i\), and evaluative relations \(\succeq_i\). Those relations may be incomplete and need not be numerical. An ecological population model can omit this agent module entirely. The analyst should not assign a represented purpose to a cell, ecosystem or reaction network merely because a persistence condition can be measured.

The participant set may change through entry, death, succession, splitting or merger. Conditions can cross the model boundary as energy, matter, organisms, testimony or shocks. These events and fluxes must be stated; an augmented state is not a claim that the represented system is materially closed or contains its entire environment.

“Rule” means a causally effective regularity within the model: access, transition probabilities, reaction conditions, recurring evaluation procedures, feasible actions, or channels of evidence. An institutional rule and a biochemical regulation mechanism can occupy a similar mathematical position without being the same kind of thing. Relationships may transmit nutrients, force, infection, instruction, credibility or authority; their types and units remain distinct.

Retention is broader than replication. A useful optional representation is a nonnegative kernel

\[
\mu_{t+1}(B)=\int T_{s_t}(v,B)\,\mu_t(dv)+I_{s_t}(B).
\tag{2}
\]

The kernel must be specified for the application. It can represent physical durability, repeated enactment of a practice, use of a learned response, copying, organizational succession, or biological reproduction. A probability-preserving kernel can describe switching; a mass-changing kernel can describe production and loss. The innovation term \(I\) is not automatically useful or exogenous: its generating activity and limits require explanation. This is a bookkeeping form, not a law that everything undergoes Darwinian replication.

The general causal updates have the form

\[
\begin{aligned}
(e,n,\mu)_{t+1}&\sim P_{r_t}(\cdot\mid s_t,a_t),\\
r_{t+1}&\sim K(\cdot\mid r_t,e_t,n_t,\mu_t,a_t,o_t),\\
(\phi_i,b_i,\succeq_i)_{t+1}&\sim L_i(\cdot\mid s_t,a_t,o_t,\text{encounters}).
\end{aligned}
\tag{3}
\]

Agents, where present, act through a stated choice process under their available information, relationships and authority. Partial preferences alone do not determine their choices. Deliberation, habit, imitation, voting, negotiation, exploration and coercion require different mechanisms; none should be silently replaced by a common maximization operator.

The kernels in (3) are a schema until restricted. The empirical content lies in which influences exist, their signs, rates, delays and limits, and which interventions alter them. Reciprocal formation of networks and their constituent dynamics is established territory; [Gross and Blasius's adaptive-network review](https://arxiv.org/abs/0709.1858) provides one relevant mathematical lineage. The proposal is to retain the distinction between activity, its continuation conditions, and the routes by which those conditions can be revised.

| Application | What can be retained | Examples of conditions that activity changes |
|---|---|---|
| Meritocratic evaluation | Criteria, credentials, learned strategies, appointed people | Who can demonstrate competence; whose judgments set later criteria |
| Bureaucracy | Procedures, categories, records and patterns of discretion | What becomes administratively visible, admissible and actionable |
| Democracy and politics | Coalitions, precedents, participation and constitutional practices | Representation, agenda access, public understanding and amendment rights |
| Ecosystems and organisms | Traits, populations, ecological relationships and maintained structures | Nutrient cycles, habitat, interaction networks and developmental conditions |
| AI systems and their deployment | Parameters, policies, evaluation practices and deployed designs | Experience distribution, training signals, human practices and future deployment choices |
| Nonintentional living processes | Organization sustained through turnover | Reaction environments, membranes, transport and renewal conditions |

These are candidate mappings, not evidence that every row obeys one equation. In particular, biological fitness, political legitimacy, predictive accuracy and organizational persistence are different observables.

## 2. Reflexivity does not require an infinite tower of governors

A rule can be a state variable that affects both ordinary transitions and its own revision:

\[
x_{t+1}=F(x_t,r_t),\qquad
r_{t+1}=G(x_t,r_t).
\tag{4}
\]

Parts of \(r\) can encode appointment, amendment or learning procedures, and those parts can themselves change through the same recurrent transition. A finite self-modifying description therefore need not introduce an additional governor at every mathematical level. What remains fixed is the analyst's declared generative mechanism and physical boundary, not an imagined institution outside every institution.

This resolves a representational regress, not every causal or normative question. A model must still state what implements the encoded rule and what it cannot change. Open-ended novelty can invalidate the chosen state description. A useful finite model is a revisable account of a situation, not a claim that its variables exhaust possible future meanings or forms of life.

## 3. A cross-level proposition with quantitative content

The following elementary comparison result generalizes the two-variable loop already discussed in the multilevel memo. It supplies a measurable condition and a maintained region rather than treating the presence of feedback as an explanation by itself. It is a special case of established small-gain reasoning; [Jiang, Teel and Praly](https://web.ece.ucsb.edu/~teel/ECE236/jiang-teel-praly-1994) develop the broader nonlinear interconnection theory.

Choose separate nonnegative deviation or deficit functions \(V_i(s)\), \(i=1,\dots,k\). They might concern disturbance to a material renewal process, mismatch between a rule and its conditions, or loss of an information channel. Their meanings, reference conditions and units must be specified; they are not a social utility function. Suppose that along the actual **coupled** dynamics,

\[
D^+V\le(-D+B)V+d,
\tag{5}
\]

componentwise, where \(D=\operatorname{diag}(a_1,\dots,a_k)\) has \(a_i>0\), \(B\ge0\) has zero diagonal, and \(d\ge0\) bounds disturbances. The upper Dini derivative permits nonsmooth diagnostic functions. Each \(a_i\) bounds restoration within one component; \(B_{ij}\) bounds propagation from another. These inequalities must be derived or estimated on the region used in the claim, not chosen after observing the desired outcome.

Units need not be converted into a common value scale. Under a positive diagonal change of units \(\widetilde V=SV\), the gain matrix becomes \(S(D^{-1}B)S^{-1}\), which has the same spectral radius. The threshold below therefore does not depend on pricing the different components in one currency.

**Proposition.** If

\[
\boxed{\rho(D^{-1}B)<1,}
\tag{6}
\]

then \(H=D-B\) has a nonnegative inverse. Let

\[
v_* = H^{-1}d,\qquad w=H^{-1}\mathbf1>0.
\]

Every set

\[
\boxed{\mathcal R_\lambda=\{s:V(s)\le v_*+\lambda w\},\qquad\lambda\ge0,}
\tag{7}
\]

is forward invariant, provided (5) holds there and the ordinary existence conditions prevent escape through an unmonitored boundary. For example, it suffices that the relevant sublevel set is compact inside the model domain and the dynamics are locally well-posed. Along its trajectories,

\[
\boxed{\limsup_{t\to\infty}V(t)\le(D-B)^{-1}d.}
\tag{8}
\]

**Proof.** Since \(\rho(D^{-1}B)<1\), the nonnegative Neumann series gives

\[
(D-B)^{-1}=(I-D^{-1}B)^{-1}D^{-1}\ge0.
\]

At the \(i\)-th face of (7), the nonnegative off-diagonal terms imply

\[
D^+V_i\le[(-D+B)(v_*+\lambda w)+d]_i=-\lambda\le0.
\]

This proves invariance, with the zero-slack case obtained by comparison or a limit of positive-slack sets. The matrix \(M=-D+B\) is stable: \(Mw=-\mathbf1\), so its weighted maximum-norm decay rate is bounded above by \(-\min_i1/w_i<0\). Componentwise comparison with \(\dot v=Mv+d\) then yields (8). \(\square\)

For two components the condition is \(bc<ad\), and the disturbance limits are

\[
v_{1,*}=\frac{d\,d_1+b\,d_2}{ad-bc},\qquad
v_{2,*}=\frac{c\,d_1+a\,d_2}{ad-bc}.
\tag{9}
\]

Thus two systems with identical component restoration rates can have very different recovery margins because of their cross-level coupling. The denominator exposes amplification near the feedback boundary. In the exact positive comparison system, this is an exact stability boundary. In a nonlinear application using conservative bounds, failure of (6) only means that this certificate fails: it does not prove instability, collapse or a phase transition.

Neither (7) nor the weighted norm in the proof supplies a moral ranking. They establish bounded response relative to declared conditions. They do not imply convergence of every underlying state, absence of cycles inside the bounded region, or usefulness of the selected conditions. A viable ecosystem can lie outside this particular small-gain class.

### A bounded example: restoring parts, multiple joint regimes

Consider signed deviations of a practice and the condition selecting it:

\[
\dot x=-x+k\tanh r,\qquad
\dot r=-r+k\tanh x,\qquad k>0.
\tag{10}
\]

With either variable held fixed, the other converges exponentially to a unique response. The full system is bounded. Its equilibria satisfy \(x=r\), because subtracting the two equilibrium equations gives opposite signs unless the variables agree. For \(k<1\), the origin is globally attracting by the comparison bound applied to \((|x|,|r|)\).

For \(k>1\), the origin has eigenvalues \(-1\pm k\) and is a saddle. There are two further equilibria \(x=r=\pm z_*\), where \(z_*>0\) solves \(z_*=k\tanh z_*\). Both are locally asymptotically stable: their eigenvalues are \(-1\pm k\operatorname{sech}^2z_*\), and

\[
z_*\operatorname{sech}^2z_*<\tanh z_*
\]

implies \(k\operatorname{sech}^2z_*<1\). The positive solution is unique because \(\tanh z/z\) decreases from one to zero. This exact symmetric example has a pitchfork at \(k=1\); that bifurcation type is a property of this chosen symmetry, not a universal social transition.

The example contains no money, replication, common utility or conscious evaluator. It demonstrates a specific mechanism: individually restoring response laws can jointly create persistent alternative regimes. Whether either regime describes domination, cooperation, specialization or something else requires an actual domain mapping. Attractor structure alone does not supply that interpretation.

## 4. Goals and constraints can change inside the system

For situated agents, let \(\psi\) record their current concerns, representational categories or thresholds. Its change is part of the dynamics:

\[
\dot x=f(x,r,\psi,a),\qquad
\dot r=g(x,r,\psi,a),\qquad
\dot\psi=\ell(x,r,\psi,o,\text{relationships}).
\tag{11}
\]

This does not prescribe one universal preference-update law. Different components may change through encounter, development, deliberation, socialization or coercion. Distinguishing those mechanisms is part of the explanation. An update of a belief within a frame is different from changing which concerns can be represented or which actions can be conceived.

Suppose a stated concern is operationalized by \(b_j(x,r,\psi)\ge0\). Its derivative is

\[
\boxed{
\dot b_j=\nabla_x b_j\,f+\nabla_r b_j\,g+\nabla_\psi b_j\,\ell.
}
\tag{12}
\]

The last two terms cannot be dropped merely because the previous rule or goal was held fixed during a local evaluation. If implemented actions ensure \(\dot b_j\ge-\alpha_j b_j\) for every declared concern and every modeled uncertainty, comparison proves their joint preservation. At a discrete revision, the new state must likewise satisfy the declared jump condition; continuous-time reasoning does not protect an instantaneous rewrite. Time-varying constraint viability is established mathematics; see the [temporal viability analysis by Greiff, Sun, Robertsson and Johansson](https://arxiv.org/abs/1811.06350).

This provides a formal place for evolving goals without treating whichever goal survives as correct. Changing a standard and restoring a condition are distinct terms in (12). For example, let a physical condition decline as \(c(t)=e^{-t}\), while an internally accepted threshold follows \(a(t)=\tfrac12e^{-t}\). The declared margin \(c-a\) remains positive forever, although every fixed positive physical floor is eventually crossed. Conversely, a revised goal may legitimately recognize a previously excluded harm. The equations cannot decide between learning and accommodation to harm without additional empirical and normative judgments.

Consequently reports should retain independently measured consequences and identify whose criteria changed, how, and under what influence. “Alignment” cannot mean only persistence, viability or agreement with current institutional preferences. Cancer, coercion and self-confirming institutions can persist. Deciding which relationships and forms of life deserve protection remains a substantive question, not an eigenvalue calculation.

## 5. Three capacities that cannot be exchanged by renaming them

The architecture separates three causal questions:

1. **Informational distinction:** can available experience distinguish situations that require different responses before the relevant deadline?
2. **Effective response:** can some appropriate response actually be proposed and implemented through current relationships, authority and physical capabilities?
3. **Regeneration:** do the transitions maintain or restore the material and organizational conditions enabling future observation and response?

These are not three currencies. More stored energy cannot by itself distinguish observationally identical situations. More accurate belief cannot implement an unavailable action. One successful action does not show that its enabling conditions can be renewed. Their mechanisms differ across domains: metabolism, habitat formation, skill transmission, institutional standing, sensor calibration and public testimony do not share a universal production function.

The existing situated-correction note proves the informational distinction with an exact two-context example. Its lesson survives the financial special case: \(\forall\text{ context}\;\exists\text{ effective action}\) does not imply \(\exists\text{ available policy}\;\forall\text{ context}\). The policy must have both timely information and implementable choices. Conversely, a common safe response may make detailed observation unnecessary; every system need not maximize information.

Likewise, preserving a count of options is not a universal objective. If new options are optional, free, and leave the plant, information and constraints unchanged, they cannot reduce the mathematical set of states from which some successful policy exists. But actual choices may become worse, harmful options may impose unavoidable costs, and creating an option may alter those supposedly fixed conditions. Capacity, realized behavior and justification must remain separate.

## 6. What is proposed, what is proved, and what would test it

The architecture proposes a common family resemblance: activities are retained under conditions that those activities help reproduce or revise. In intentional systems, this includes the formation of evidence, interpretations and purposes. It does not propose a universal loss function or an inevitable direction toward competition, accumulation or domination.

The small-gain proposition and constraint-transport identity provide established mathematical restrictions on restricted members of that family. They are not new universal laws. Their scientific value here is to force a distinction between local performance and the coupled process that renews or closes off further response.

The programme's testable hypothesis is more specific than “everything has feedback”: some persistent failures are explained better by the feedback from retained practices into their own conditions of continuation than by fixed-rule individual adaptation alone. An application should therefore compare a fixed-rule account with an endogenous-rule account, measure the cross-level links, and test interventions that alter those links while holding immediate local performance as comparable as possible. A simpler account that predicts equally well is evidence against the need for the richer construction in that case.

Nothing here proves that all domains instantiate the same mechanism or that the research programme has the best model. The useful common question is whether a system's continued activity preserves, reconstructs or removes the conditions through which it and its participants can encounter, interpret and respond to consequential change. The answer is situated; the causal distinctions and conditional mathematics can nevertheless travel.
