# How organizations regulate the conditions of their continuation

Research continuation for Ren, 5 October 2026. This develops the proposal that generative organizations can regulate themselves and their surroundings, preserving the possibility of future organization through change, mutation, and selection. It connects the [previous account of generative becoming](generative-becoming.md) to allostasis, environmental construction, cognition, and social persistence. The universal ambition is retained; the cross-domain synthesis remains a hypothesis requiring specific mechanisms in each application.

**Some interactions produce organizations that regulate the conditions of their own regeneration. Variation and differential continuation can then change those organizations and their surroundings together.** What is carried forward can be a productive relation with the surroundings whose material implementation and behavior change over time.

This is stronger than the observation that everything has consequences. It calls for mechanisms that detect or otherwise respond to consequential conditions, alter internal processes or surroundings, and thereby affect the continuation of the organization. A causal test disables or changes a proposed regulatory link and checks the independently specified consequences.

## Regeneration can become regulated

The earlier models explain mutual production: one component helps replace another, which helps replace the first. Regulation adds state-dependent adjustment. For example, a mechanism can increase repair when wear accumulates, change resource use as supply falls, or alter the surroundings in a way that changes subsequent losses. The regulator itself requires physical support; it is part of the organization being explained.

Allostasis supplies a more specific biological connection. In Sterling's formulation, regulation anticipates needs and adjusts coordinated activity before those needs produce large errors. Changes in operating conditions are compatible with continued functioning. This is a published theoretical account of predictive regulation, not a warrant to call every feedback loop allostatic. [Sterling, 2012](https://pubmed.ncbi.nlm.nih.gov/21684297/).

The proposed foundation can distinguish reactive repair, anticipatory adjustment, learning, and inherited change without requiring each to be present in every persistent system. A feedback controller need not predict; a prediction need not be conscious; and a stable physical structure need not regulate anything.

There is a close established agency proposal: an autonomous organization adaptively regulates its interaction with its surroundings and thereby contributes to its own continuation. Its authors distinguish individuality, an active contribution to the interaction, and norms of functioning. This is a predecessor for the present interpretation, rather than an independently discovered universal theorem. [Barandiaran, Di Paolo, and Rohde, 2009](https://journals.sagepub.com/doi/10.1177/1059712309343819).

## The surroundings enter the explanatory unit

Let \(s\) be an organization's current material state, \(e\) its relevant surroundings, and \(\theta\) its maintained structure, including any controller, memory, or inherited disposition. A schematic joint dynamics is

\[
\begin{aligned}
s_{t+1}&=F(s_t,e_t,\theta_t),\\
e_{t+1}&=H(e_t,s_t,\theta_t),\\
\theta_{t+1}&=G(\theta_t,s_t,e_t).
\end{aligned}
\tag{1}
\]

The organization responds to its surroundings, changes them, and can change the mechanisms of that response. These effects can occur at different rates; the equation does not assert a common biological timescale. Stochastic counterparts require a specified joint transition law. The functions still need physical justification.

The environment is therefore part of the causal account. It need not be entirely controlled by the organization, and broadening the account does not erase meaningful boundaries inside it. A system–environment relation is a useful explanatory unit. Calling that relation a unit of evolutionary selection additionally requires identifying how its relevant features are inherited or reconstructed across the counted continuations.

Niche-construction research explicitly separates environmental modification from subsequent evolutionary responses to the modified conditions, and includes environmental legacies across generations. It provides an established route for investigating this feedback. [Odling-Smee and colleagues, 2013](https://pubmed.ncbi.nlm.nih.gov/23653966/).

## Changing form without making failure disappear

The user's future form can mean a viable successor organization rather than a copy of today's shape. A precise account needs two independently assessed relations:

1. **Continuation:** the later organization has the relevant history of production, inheritance, or maintained organization connecting it to the earlier one.
2. **Capacity:** the later organization can still perform specified productive or regulatory functions under stated conditions, possibly through a different implementation.

Resemblance alone does not establish the first. Causal descent of material into inert debris does not establish the second. The criteria, or a justified procedure for revising them, must be stated before an outcome is declared successful. Otherwise every collapse could be redescribed as a successful transformation.

An individual, its descendants, and its collective can have different continuations. Mutation may sustain a lineage while ending a particular inherited form. A collective may persist while replacing its members. These can fit one causal account without being treated as the same identity relation.

This extends the [history investigation](identity-through-change.md): a future-capacity description and a causal history answer complementary questions. Depending on the present for prediction remains compatible with using history to establish which organization continued.

## What selection by generativity can mean

Selection is not an additional agent that recognizes valuable futures. For a population account, specify variants, how they differ, how continuations are counted, what is inherited, and the mechanisms affecting their numbers. Then ask whether independently measured generative capacities explain differential continuation.

A simple deterministic census model is

\[
\boxed{
n_j(t+1)=\sum_i n_i(t)\,W_i(e_t,n_t)\,M_{ij}(e_t,n_t),
\qquad e_{t+1}=H(e_t,n_t).
}
\tag{2}
\]

Here \(n_i\) is a nonnegative abundance of variant \(i\); \(W_i\ge0\) is its specified per-capita contribution to the next census; and \(M_{ij}\ge0\), with \(\sum_j M_{ij}=1\), describes the distribution of successor types. Retained parents and offspring must be counted consistently rather than counted twice. The functions can depend on current population composition as well as environmental conditions. Fractional abundances make this a deterministic population model; a model of random finite counts requires its own stochastic law.

The explanatory work lies in deriving or measuring \(W\), \(M\), and \(H\) through independently specified mechanisms. Defining generativity as observed success and then explaining success by generativity would explain nothing. A fixed catalogue of variants also does not account for unlimited invention of new kinds; equation (2) describes variation within a supplied type space.

There is a useful exact check on the proposed direction of selection. Suppose successors retain their parent's type, so \(M_{ij}=\delta_{ij}\), each type retains a fixed capacity score \(g_i\), and both current and next total abundances are positive. With current frequencies \(p_i=n_i/\sum_j n_j\),

\[
p_i'=\frac{p_iW_i}{\bar W},
\qquad
\bar W=\sum_i p_iW_i>0.
\]

Consequently,

\[
\boxed{\bar g'-\bar g
=\frac{\operatorname{Cov}_{p}(g,W)}{\bar W}.}
\tag{3}
\]

**Proof.** The new mean is \(\sum_i p_iW_i g_i/\bar W\). Subtract \(\bar g\), put the terms over the common denominator, and use \(\operatorname{Cov}_{p}(g,W)=\sum_i p_i g_iW_i-\bar g\bar W\). The identity follows. It is an accounting consequence of the supplied reproduction rule, not a mechanism that determines \(W\).

For two initially equally common variants with scores \(g=(2,1)\) and contributions \(W=(1,2)\), the mean score falls from \(3/2\) to \(4/3\) even though total abundance increases by a factor \(3/2\). Reversing the contributions gives a mean of \(5/3\). These constructed examples show that differential continuation alone does not force a selected capacity measure to increase. The score must be specified independently; it is not a universal unit of generativity.

When mutation, learning, or environmental change alters the scores, those changes add to the frequency-change effect. Short-term spread can also deplete resources needed for later continuation. Thus the universal account must explain both regenerative success and forms of success that undermine their own support.

## A bridge to functional cognition

An analyst can describe a distribution of possible futures without the system representing that distribution. The future distribution does not itself steer the present. A physical prediction mechanism can make anticipated consequences causally effective through its current state.

One possible extension of (1) adds a physically maintained record or predictive model \(m_t\):

\[
u_t=\pi(m_t,s_t),\qquad
m_{t+1}=U(m_t,o_{t+1},u_t),
\tag{4}
\]

where \(o\) is an observation generated through a specified sensor and \(u\) changes the system–environment interaction. If \(m\) encodes estimates of action-dependent consequences and those estimates influence \(\pi\), anticipated futures enter regulation through present mechanisms. Intervening on the record, prediction, or action channel can test the proposed contribution.

This gives a route from regulation to prediction, learning, and planning. It does not show that all cognition needs an explicit world model, nor establish why such activity has felt experience. Friston's free-energy framework is an established related proposal connecting action, perception, and learning through a particular formal construction. It remains a theory to compare and test, rather than permission to equate every adaptive process with a mind. [Friston, 2010](https://www.nature.com/articles/nrn2787).

The difficult next derivation is how the sensing, representation, and execution machinery itself arises and is renewed within the broader process. Installing an ideal predictor would leave that part of the universal explanation supplied from outside the construction.

## Culture and conflicting continuations

The same questions can be asked of a practice, belief, organization, or cult: what physically carries it, how is it transmitted, which conditions support participation, and how does its activity alter those conditions? The mechanisms are communication, learning, incentives, resources, rules, and people acting; a group label is not an extra causal agent.

As a hypothetical example, a group may preserve a doctrine by affecting which evidence its members encounter and which disagreements receive a hearing. That could sustain the doctrine while weakening members' independent correction. Another organization may depend on criticism to improve its predictions and practices. A useful theory should identify the mechanisms and conditions producing each pattern, rather than equating persistence with accurate belief.

There is empirical work connecting institutional requirements with persistence: Sosis and Bressler analyzed historical records of 83 nineteenth-century United States communes to test a costly-signaling account of cooperation and longevity. The study's abstract reports support for aspects of that account. This does not establish that every restrictive group persists longer, that restriction causes longevity in all settings, or that a long-lived doctrine is true. [Sosis and Bressler, 2003](https://journals.sagepub.com/doi/abs/10.1177/1069397103037002003).

The user's earlier work already distinguishes a process reproducing itself through growing control from a process renewing shared capacities for agency, criticism, and repair. That distinction becomes central here: **continuation of a pattern, continuation of its participants, and continuation of their wider conditions can diverge.** A universal descriptive theory should explain that divergence. Choosing which continuations deserve protection requires reasons that mere persistence cannot supply.

## The revised universal candidate

The strongest present formulation is:

> **Transformations can produce organizations that regulate and renew the conditions of further transformation. Their interactions alter the environments and inherited structures through which later continuation becomes possible. Some develop mechanisms that represent possible consequences and use those representations to change what they do.**

This connects physical organization, regeneration, environmental modification, selection, and functional cognition without assuming that every process exhibits the entire sequence. Universal scope means explaining their relations and limits within one account, including inert persistence, failure, exploitation, and collapse. Demonstrating a common vocabulary across domains is an initial step; deriving and testing the relevant mechanisms would supply the stronger explanation.

The next integrated test should let a changing organization produce its own regulatory machinery, alter the conditions of its renewal, and undergo inherited variation. It should compare immediate persistence with longer-term productive capacity and retain the consequences for other organizations. That would make the claim about generatively selected system–environment relations concrete and capable of failing.

## Review and evidence

The [evidence record](regulating-generative-conditions-evidence.json) records source scope, the exact arithmetic examples, the independent conceptual review, and preservation hashes. The new mathematics is an elementary consequence of an explicitly supplied population rule. No biological, psychological, or social experiment was performed, and no empirical universality claim was verified. This report is a new branch; earlier reports were not edited by this work.
