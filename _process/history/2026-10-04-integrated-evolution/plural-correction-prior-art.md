# Plural correction: prior art, implementation boundaries, and a sharper next question

5 October 2026. Focused primary-source audit for the proposed plural-correction experiment. This memo does not report new experimental results. The continuation-consent example below is an analytic construction, and its proposed extension to the existing model is **unrun**.

## What the present change can establish

The proposed model retains the recoverable-inquiry dynamics but asks whether one policy can satisfy upper bounds on three consequences: collapse probability F, expected target-absent intervention and diagnostic burden H, and expenditure minus actual output C. This is a useful change in the question: compatibility of requirements can be checked without declaring one scalar ordering across them.

The three coordinates are nevertheless **declared aggregate criteria, not three represented populations**. The model contains no individual identities, distribution of benefits and costs, preference reports, ownership, bargaining, or consent. The symbolic roles “service users,” “intervention subjects,” and “resource contributors” do not supply those missing structures. H also contains a declared internal exchange rate between its components. A target-absent repair can improve stock, so H is not literally a false-action or injury count.

The model still supplies the criteria, thresholds, prior, transition law, horizon, controller, observation access, and admissibility of randomization. Removing a scalar objective does not derive these commitments or establish that participants accept them. It does make their joint consequences more inspectable.

## Five close primary precedents

### 1. Attainable vectors, linear constraints, and separating certificates are established

[Etessami, Kwiatkowska, Vardi, and Yannakakis, *Multi-Objective Model Checking of Markov Decision Processes* (2008)](https://arxiv.org/pdf/0810.5728), published in *Logical Methods in Computer Science* 4(4:8), extends the TACAS 2007 paper. It asks whether one strategy simultaneously satisfies several probability requirements. Its linear characterization uses expected state–action visits; the proof relates attainable vectors to a projected polyhedron and uses nonnegative separating hyperplanes. General temporal properties can require memory and randomization.

This directly rules out claiming the attainable-set/dual-certificate machinery as new mathematics. Our finite-horizon, augmented-information-state, additive-expectation case is simpler than the paper’s general temporal-property setting. A valid separator certifies incompatibility of specified bounds; its coefficients are not discovered moral weights. A feasible vector need not be Pareto efficient, and an arbitrary feasible policy is not a bargaining solution. See particularly the linear system and strategy construction in Section 3 and the separation argument in its proof.

### 2. Cost-constrained partially observed maintenance is also an existing baseline

[Isom, Meyn, and Braatz, *Piecewise Linear Dynamic Programming for Constrained POMDPs* (AAAI 2008)](https://cdn.aaai.org/AAAI/2008/AAAI08-046.pdf) develops paired objective/constraint value representations and applies them to inspection, repair, and replacement of structures under hidden deterioration. It explicitly treats lifecycle cost subject to a failure-probability requirement.

This is close to our physical baseline, rather than merely a general optimization citation. Important differences remain: the paper’s defined policy class is deterministic and its formulations should not be treated as a proof of our randomized-policy convex hull. Its algorithm is not an independent verification of our finite belief-DAG occupancy program. The safe attribution is that partially observed maintenance with multiple performance requirements predates this project; the current model can contribute a transparent worked comparison of paid evidence, productive support, and specified permission rules.

### 3. Agreement need not begin with a common utility, but it needs more than feasibility

[Nash, *The Bargaining Problem* (1950)](https://www.haverford.edu/sites/default/files/Nash1950.pdf) formulates bargaining with separate expected-utility functions, a feasible utility set, and a disagreement outcome. Lotteries support convexity. Additional axioms select a solution; the treatment idealizes information and rationality.

The relevant precedent is neither a universal endorsement of Nash bargaining nor a recommendation to maximize a utility product here. It establishes that distinct preferences and a common feasible set are compatible with a formal theory of agreement. But a set of feasible consequences does not itself specify disagreement payoffs, participants’ preferences, bargaining procedure, or a reason they will accept one point. Those structures would have to be supplied and defended. A threshold box alone establishes none of them.

### 4. A central controller with several criteria is not a decentralized organization

[Bernstein, Givan, Immerman, and Zilberstein, *The Complexity of Decentralized Control of Markov Decision Processes* (2002)](https://cics.umass.edu/~immerman/pub/bgiz.pdf) defines local policies using each agent’s own observation history and studies the resulting joint-policy problem. Its hardness results already arise with a shared reward: disagreement about objectives is not required for decentralized information to matter.

Our current controller receives one specified information history and chooses the available actions. Calling its criteria plural does not give different participants separate information, communication constraints, or control. A policy depending on pooled evidence is not automatically implementable by agents who never receive that evidence. Nor does an information state sufficient for aggregate physical control necessarily preserve histories relevant to individual promises, participation decisions, or private information. Those additions can require a larger state or a different policy class. This is a structural distinction, not an assertion that our small finite centralized program inherits the general problem’s computational hardness.

### 5. Feasible gains need not be truthfully and voluntarily implementable

[Myerson and Satterthwaite, *Efficient Mechanisms for Bilateral Trading* (1983)](https://www.sciencedirect.com/science/article/abs/pii/0022053183900480) characterizes mechanisms with independent private valuations. Under the paper’s overlapping-support, positive-density assumptions, its impossibility result rules out combining ex post efficient trade, Bayesian incentive compatibility, individual rationality conditional on one’s valuation, and absence of outside subsidy. The [primary paper scan](https://www.cs.princeton.edu/courses/archive/spr07/cos444/reading/MS83/MS83.pdf) contains the precise statement in Corollary 1.

This is a narrow theorem with substantive assumptions, not a general impossibility of coordination. Its use here is to distinguish a physically feasible allocation from a mechanism that elicits information and secures participation. Our current model contains neither private preference reports nor incentives to misreport. Its feasibility result therefore cannot establish incentive compatibility; conversely, this trading theorem cannot establish that its policies would fail. That requires an actual institutional model.

## Boundaries the experiment should preserve

**Expectation versus individual protection.** A lottery can satisfy every declared expected bound while assigning an unacceptable realized burden to someone. Such convexification may be prohibited by the intended right. A per-person or pathwise restriction must be represented at the appropriate resolution; it does not follow from aggregate expectation constraints. Even expected constraints for named constituencies can conceal unequal treatment within each group.

**Permission versus legitimacy.** Pure removal of actions, holding dynamics, information, resources, and policy interpretation fixed, can only shrink the attainable set. This is set inclusion, not evidence that fewer rights are better. Actual changes in authority can change trust, reporting, cooperation, compliance, available resources, and future actions; that comparison is not a pure action-set restriction. A restriction that rules out one harmful action may be justified even when it eliminates some previously feasible aggregate vectors.

**Compatibility versus choice.** If bounds are feasible, there may be many witnesses. If they are infeasible, a separating certificate does not decide whose demand should change. Choosing a witness by minimizing C adds an explicit selection rule. Neither selection nor incompatibility determines legitimate authority over the decision.

**Current requirements versus revisable purposes.** These calculations answer a conditional question about specified purposes. They do not show that evolving human purposes can always be represented by fixed thresholds, or that all morally relevant considerations admit expected numerical loss functions.

The present contribution is consequently a controlled diagnostic: with one audited physical and observation model, which combinations of declared requirements remain attainable, and which specific permission changes remove their compatibility? That is more informative than a scalar optimum, without being a new general theory of agreement.

## A sharper next theorem: ex ante acceptability need not survive revelation

The next useful move is to make acceptance a continuing decision rather than merely the researcher’s threshold choice. This is an elementary continuation-participation result, not a claim of new bargaining mathematics. The five-source audit above is not an exhaustive priority search for dynamic participation contracts.

Consider a finite public-history decision tree with fixed participants, expected remaining losses, and a specified refusal outcome at each history h. Participant i can unilaterally trigger refusal there, giving them remaining expected loss d_i(h). Assume common knowledge of the relevant conditional distributions; no hidden reports, transfers, penalties, or binding commitment prevent refusal. Write V_i^π(h) for the remaining conditional expected loss under continuation policy π.

A necessary condition for voluntary continuation at every positive-probability decision history is

\[
V_i^\pi(h)\le d_i(h)\quad\text{for every participant entitled to refuse at }h.
\]

The proof is immediate: otherwise that participant strictly reduces their own expected loss by refusing. These inequalities are sufficient against **exit deviations only** if exit is the only alternative and the prescribed continuation is otherwise executed, with acceptance of indifference specified. They do not establish truthfulness, obedience to other actions, agreement about the model, or legitimacy.

The gap can be strict even with public information and no deception. Before a fair public coin is revealed, a corrective plan has losses

\[
\ell(A)=(0,2),\qquad \ell(B)=(2,0).
\]

The only alternative, either before or after revelation, has losses (1.1,1.1). The coin determines which participant unavoidably bears the corrective burden; there is no action that swaps these losses after revelation. Before revelation, both strictly prefer the plan’s expected losses (1,1), and bounds (1.05,1.05) are feasible under commitment. After either outcome, the person facing loss 2 prefers refusal, giving both losses (1.1,1.1). Thus the bounds cannot be voluntarily implemented under these continuation rights. Mixing correction with refusal after revelation does not help: every positive probability of correction makes the burdened person worse off than refusing immediately.

This establishes neither that veto rights are undesirable nor that binding commitment is desirable. It identifies a missing condition. Transfers, insurance, different corrective actions, altered refusal consequences, or commitment can change the example; each changes its assumptions. There is no unconditional inference that physical infeasibility caused the failure.

## A testable extension using the existing model

First reproduce the two-state construction independently. Then, rather than inventing another physical module, add explicit loss-bearing roles and refusal opportunities to the current finite public-history tree. Specify who observes what, when refusal is possible, what continuation refusal causes, and who actually bears each physical and financial consequence. Do not interpret F, H, and C as personal utilities merely by renaming them.

For a fixed history-dependent refusal loss d_i(h), let q_π(h) be the probability of reaching h, and let W_i^π(h) be the unconditional expected remaining loss contributed by descendants of h, including that reach probability. The conditional requirement can be written

\[
W_i^\pi(h)\le d_i(h)q_\pi(h).
\]

On a finite history-tree flow representation these are linear constraints when losses and refusal continuations are fixed. Zero-probability histories impose no conditional requirement because both sides vanish. The history must include information available when refusal is chosen, including any disclosed policy-lottery draw; otherwise the computation averages over distinctions participants can act on. A compressed physical belief state alone need not retain the necessary distinctions. Constraints protecting off-path behavior, private-information deviations, or renegotiated refusal outcomes require additional analysis.

Compare initial expected feasibility with feasibility under these continuation constraints, and retain a witness history for every demonstrated gap. If compensation restores participation, charge its funding, liquidity, incidence, and enforcement costs to an explicit ledger; do not treat transfers as free new social output. Compensation can redistribute losses without creating an aggregate physical loss, so both the financial constraint and the welfare interpretation must be stated separately.

The substantive research question would then be: **when can a system preserve attainable correction while also honoring specified continuing participation rights, using the same finite productive, informational, and financial resources?** A useful result could identify the precise reserve, information, or feasible-action change that restores both. Until implemented, this remains a proposed test. Its scientific value would lie in exposing and testing the coupling, rather than relabeling a standard multiobjective controller as a complete theory of human coordination or AI alignment.
