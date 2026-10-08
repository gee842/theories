# From an acquired consequence signal to paid predictive learning

6 October 2026. AI-authored mathematical interface for Ren's [accepted derivation](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#accepted-work-sequence), working backward from the [concern learner](../../2026-10-05-concern-theory/learning-formal.md) and [revisable-concern anchors](../../2026-10-05-revisable-concern/scope-math.md). This note concerns operational consequences and prediction, not phenomenal suffering, moral standing or their neural realization.

**Contribution.** A teaching target can be generated from an actually acquired record of a constitutive dependency instead of supplied as an unexplained positive number. Three distinct conditions govern the substitution: the target must be identifiable through available measurements; acquisition and use must remain materially feasible in the actual successor state; and sampling must justify the learning recurrence being claimed. An exact finite example satisfies the first condition but fails the second under insufficient resources. A second example satisfies conditional teacher calibration while resource-dependent sampling invalidates the usual unconditional recurrence.

The sensing, record decoding, memory update and decision-routing mechanisms remain declared architecture. This supplies a conditional operational teacher; it does not derive every role of the earlier primitive β or establish individual learning from chemical copying alone. It is separate from the concurrently developed selector-revision mechanism.

## 1. The downstream input to replace

The concern study starts from w₀=0 and supplies a positive self-teaching target β in

\[
w_{t+1}=(1-\delta-\eta u_t)w_t+\eta u_t\beta,
\qquad 0<\eta,\quad \delta\ge0,\quad \eta+\delta\le1.
\tag{1}
\]

Here u_t denotes an available, paid teaching event. The original account explicitly leaves β, the updater, shared evaluative routing and the interpretation of correspondence as premises. The revisable-concern graph subsequently treats established anchors as pinned values. Those separate premises must not disappear when a physically measured signal is introduced.

Replace β in an implemented update by an acquired target Y_t. The proposed narrower meaning is **predicted loss of a specified continuation capability**, or a directly measured shortfall in its actual enabling support. The continuation task and its material requirements are defined before choosing a learning rule. Less stored fuel is not automatically a task failure: a relation between the measurement and the declared activity must be established.

An accurate predictor of that loss does not, by itself, implement avoidance, concern, or an ethical reason. A controller still needs an effective route from prediction to action. Another controller can use the same prediction to conceal damage, or can exclude another center from evaluation. Substituting an operational teacher therefore preserves the earlier architectural counterexamples.

## 2. Exact acquisition and the stronger paid-tree condition

Let S be a finite class of possible physical histories under a declared model. Let b(s) be the target consequence for a fixed task and reference preparation, and h(s) the record actually accessible to the learner. A record-based exact decoder Y=φ(h) exists **if and only if**

\[
h(s)=h(s')\ \Longrightarrow\ b(s)=b(s').
\tag{2}
\]

Necessity follows because a decoder returns the same output on the same input. For sufficiency, assign to each attained record the common value on its fiber. This is an elementary identification criterion, not a new generalization theorem or proof that the decoder is physically installed. In particular, an analyst's access to b does not make it accessible to the process.

Paid adaptive probes require a stronger condition. A finite information state B contains the still-possible physical states, their resources and retained records, and the reference target label for each state. A probe q must be physically available in every member of B; its actual transitions spend resources and yield observation o. Let B[q,o] contain the corresponding **successor** states, not newly prepared copies. A target referring to the pre-probe task remains indexed to that reference; changing a target during probing cannot silently count as identifying the old one.

The policy class here is a **finite probe tree**: every internal node executes one declared probe q and branches on its acquired outcome; each leaf has already identified the target before executing its terminal plan. A probe may denote a declared finite physical macro that includes preparation or informative actions such as repair and capture, but every constituent event, cost, observation and intermediate state must be included in that macro's transition specification. Every acquisition used to identify the target must be represented in the tree. The bound k counts these declared probe-tree nodes along a path, not necessarily elementary physical events. Unrepresented preparatory or informative actions before or between probes are outside this policy class.

Let W₀(B) mean that the target labels already agree and a permitted terminal plan, containing no further probes or new target identification, can decode and write that value and meet the stated continuation obligation from those actual states. For example, the obligation can require preserving every continuation that was possible in the reference preparation; it need not demand success in worlds where the task was impossible to begin with. A common plan may use the agreed target and already acquired record, but not the hidden state identity. Define

\[
W_{k+1}(B)=W_0(B)\ \lor\
\exists q\ \forall o\text{ with }B[q,o]\ne\varnothing:\ W_k(B[q,o]).
\tag{3}
\]

The existential quantifier ranges only over jointly available probes. **Theorem:** W_k(B) holds exactly when a policy in this declared finite probe-tree class, of depth at most k, can guarantee identification, writing and the declared continuation obligation. Proof is induction on k: by definition a nonterminal policy in this class starts with an available probe and has a successful suffix at each possible observation; conversely those suffixes assemble such a tree. Resource and timing restrictions enter through the actual transitions and terminal obligation. This is a finite deterministic/worst-case criterion for the specified class, not a characterization of every physical controller or a universal minimum price of learning. Stochastic reliability requires a specified probability criterion instead.

Thus target constancy on observation fibers can hold even when no admissible paid identification-and-action policy exists. This differs from the earlier linear row-span theorem, which assumes supplied training features and targets rather than establishing affordable access to them.

## 3. Exact dependency and timing example

Consider one damaged support gate, c=0, a latent source packet E=θ∈{0,1}, and working reserve F=B. A receipt bit J starts at zero. The task is to deliver a fresh support packet through the gate. In this declared organization that delivery is the input to the next activity; it is not defined by whether a predictor receives a high score.

With source held fixed, an intact gate permits delivery exactly when θ=1, whereas the damaged gate does not. The operational dependency contrast is therefore derived from the event law:

\[
\beta_\theta=\mathbf1\{\text{delivery possible with intact gate}\}
-\mathbf1\{\text{delivery possible with damaged gate}\}=\theta.
\tag{4}
\]

This is a contrast between conditions, not a claim that repairing a gate costs nothing. Actual actions are:

| Action | Physical update |
|---|---|
| Paid probe | Spend one F; read the source/receipt record and emit Y=E+J=θ |
| Write prediction | Spend one F; apply w⁺=(1−η)w+ηY; η=1 in this exact one-write fixture |
| Repair | Spend one F; set c=1 |
| Capture | If c=1 and E=1, convert that E to one F and set J=1 |

The source/receipt ledger E+J=θ preserves the identity of the reference target after a delivery. The probe is a supplied clocked physical test: an absent packet produces a completed zero reading, not an unexplained inference from waiting forever. Probe and writer machinery, their accuracy, and the stated unit prices are assumptions. The decoder does not receive an externally assigned reward for repairing. Its output follows from an internally acquired record and the declared gate law.

The damage cue alone is identical in both worlds, although their targets differ. It violates (2). The paid source probe distinguishes them. If other unrepresented faults can prevent an intact gate from delivering, this probe may cease to identify (4); its adequacy is relative to the stated mechanism class and must be checked under expansion.

For a controller that must **probe → write calibrated memory → choose its first repair → capture**, B=3 suffices in the source-present world: its successive reserves are 3→2→1→0→1. For B=2, the probe and write leave zero reserve; capture cannot yet occur because the gate is still damaged. No learned first repair is possible under that required order. Logical identification after the first probe therefore does not establish deliverable learning or action.

The accompanying supplied controller reads only fuel, gate condition, the acquired record, written coefficient and receipt; it does not read hidden source directly. After probing and writing, it commands repair exactly when the written coefficient is positive, then commands capture through the repaired gate. Holding the plant and acquired record fixed while clamping that coefficient from one to zero changes the repair command to stopping. This intervention establishes use of the predictor in this particular route, beyond merely finding correct memory before a repair. The inverse actuator can instead repair when the coefficient is zero. The routing and its beneficial orientation remain supplied; acquiring an accurate predictor does not derive them.

This is an architectural and ordering boundary. B=2 can pay a blind repair, capture replenishes one unit, and later probe and write can both occur. Alternatively, probe → repair → capture → write works at B=2. Both achieve retrospective prediction, but their first repair did not use the newly written predictor. Direct action from a probe marker is another legitimate comparator. A stored learned coefficient is not a universal prerequisite for every successful response.

The target in (4) refers to the pre-repair task. Reading only current E after capture would return zero and misdescribe that earlier dependency; the retained receipt is needed. Conversely, applying the earlier positive target to a new attempt after the source has been consumed would be wrong without fresh support or a revised task. Source replenishment, reference indexing and stable cue meaning are composition obligations.

## 4. Exactly when the predictive recurrence follows

Let \(\mathcal F_t\) be acquired history before deciding whether to pay for teaching. Memory w_t and u_t∈{0,1} are measurable with respect to that history. A paid observation produces Y_t, and the installed updater obeys

\[
w_{t+1}=(1-\delta)w_t+\eta u_t(Y_t-w_t).
\tag{5}
\]

An unobserved target need not exist as an available input; all expressions involving it below are multiplied by u_t. The exact expectation identity is

\[
\boxed{\mathbb E w_{t+1}=(1-\delta)\mathbb E w_t
+\eta\mathbb E[u_tY_t]-\eta\mathbb E[u_tw_t].}
\tag{6}
\]

Suppose the actually acquired target is conditionally calibrated:
\(\mathbb E[Y_t\mid\mathcal F_t,u_t=1]=\beta\).
Because payment is decided before this target is observed,

\[
\mathbb E[u_tY_t]=\beta\mathbb E u_t.
\tag{7}
\]

That still does not generally make \(\mathbb E[u_tw_t]=(\mathbb E u_t)(\mathbb E w_t)\). Resource-dependent eligibility can correlate with learned memory. Selection of completed observations or surviving organizations after the outcome can also invalidate (7) itself.

**Funded finite-schedule theorem.** Suppose a deterministic teaching schedule is feasible on every history through T, all observations and writes complete, conditional calibration holds, and the updater is installed as (5). Then the mean follows (1) with that deterministic schedule. For u_t=1, t<T, w₀=0, put r=1−δ−η. It has

\[
\boxed{\mathbb E w_T=\frac{\eta\beta}{\delta+\eta}(1-r^T).}
\tag{8}
\]

Proof: measurability and calibration give (7), deterministic u permits factoring its multiplication with w, and the resulting affine recurrence has the displayed solution. No independence between successive targets is needed beyond conditional calibration.

For exact constant Y_t=β, the same equation holds pathwise and can supply the earlier deterministic coefficient theorem. For random Y_t it is only a mean statement. Substituting its mean into a nonlinear action threshold or a pinned graph anchor does not establish pathwise protection. Distributional reliability, retained evidence and the anchor's maintenance require separate conditions.

A nonzero finite budget cannot justify “sustained teaching” for indefinitely many dates merely because the first update is affordable. Actual inflows and every expenditure must stay in the successor ledger. If each round requires prepayment c, returns are nonnegative, and no other bills occur, B₀≥cT is sufficient for T paid rounds. Lower reserves may work on some histories, but need their own pathwise feasibility argument.

## 5. Exact support-loss teacher and a censoring counterexample

Here a round performs one support-seeking operation and reads/writes its outcome. Both have a price: operation one fuel unit, observation/update one fuel unit. The round requires B≥2 **before** it begins. One unit funds operation; one is committed to the measuring/writing apparatus, so an unsuccessful operation does not silently prevent its already-paid update.

The operation obtains a return of two fuel units if it succeeds and zero if it fails. At most three rounds are considered, with a finite external stock sufficient for at most three such returns; replenishment is not a reset of B. Let failure Y_t∈{0,1} have probability p=1/2, independently of previously acquired history. Then the balance after a paid round is

\[
B_{t+1}=B_t-2+2(1-Y_t)=B_t-2Y_t,
\qquad Y_t=(B_t-B_{t+1})/2.
\tag{9}
\]

The measured signal is an actual failure to replace the two units required for another operation-and-measurement round. Its relation to future activity is given by the prepayment guard, rather than declaring every expenditure harmful. The return law and a register that reads the balance are supplied mechanisms; the learner is not handed a separate success utility. The target mean β=p is fixed by that physical return law, not by the desired action.

Use η=1/4, δ=0, w₀=0 and three opportunities. With B₀=6, all three rounds can be paid even if every return fails. Equation (8) applies and gives

\[
\mathbb E w_3=\tfrac12[1-(3/4)^3]=37/128.
\tag{10}
\]

This mean exceeds 1/4, but it cannot be inserted into the concern learner's strict choice condition as a pathwise coefficient. The eight equiprobable three-outcome histories give coefficients

\[
0,\quad 9/64,\quad 3/16,\quad 1/4,\quad
21/64,\quad 25/64,\quad 7/16,\quad 37/64.
\]

Exactly four exceed 1/4, so \(\Pr(w_3>1/4)=1/2\). Funding every update and obtaining the claimed mean still leave half the histories outside that strict threshold. A probability or pathwise requirement must be checked at its own scope before substituting this random learner into the deterministic downstream result.

With B₀=2, the process stops paying after its first failure. Each prior successful round returns B to two and leaves w=0. The first failure writes w=1/4 and leaves B=0; subsequent unpaid opportunities do not update it. All histories remain in the accounting, including inactive ones. Hence

\[
\boxed{\mathbb E w_3=\tfrac14(1-2^{-3})=7/32,\qquad
\Pr(B_3\ge2)=1/8,\qquad
\mathbb E[w_3\mid B_3\ge2]=0.}
\tag{11}
\]

Here B₃≥2 means only that the **common operating reserve** can prepay another round. If the finite external return stock begins at six, the all-success history has consumed all of it by this time. Thus probability 1/8 does not establish full fourth-round feasibility under the same source-backed experiment. Completing all three paid rounds has probability 1/4: the first two returns must succeed, but the third may fail after its update has been prepaid. Those events must not be conflated.

The teacher is unbiased at each actually prepaid round, yet the unconditional mean differs from the fully funded recurrence because u depends on previous outcomes. Conditioning on B₃≥2 creates an additional distortion: these reserve-retaining processes have seen only successful returns. Their zero average signal is not evidence that support loss is absent or insignificant. Retained memory in inactive histories is itself distinct from an organization still able to use that memory; common reserve alone also does not establish future external support.

The general scarce-reserve version with failure probability p, no decay and gain η gives \(\mathbb E w_T=\eta[1-(1-p)^T]\), probability \((1-p)^T\) of retaining the common prepayment reserve, and conditional w=0 in that reserve-retaining group. This follows by the time of first failure, provided the return stock supports the declared T-round law. It should not be replaced with \(\beta[1-(1-\eta)^T]\) unless the required paid schedule actually occurs.

## 6. Exact scope of composition toward concern

This interface can replace the numerical target in the earlier learner **under an operational interpretation**: a paid internal measurement identifies a consequence of an actual dependency, and an implemented updater learns its prediction under stated sampling and resource conditions. For the source-present deterministic gate regime, β=1 is derived from the declared continuation law; for the support-return example, β=p is derived from the return distribution. Neither is a free reward for protecting another agent.

It does not yet supply the earlier teacher's entire motivational or experiential interpretation. The updater's formation, the response to its prediction, maintenance through succession, calibrated counterfactual models, correspondence evidence, and shared evaluation across identities remain explicit premises. In particular, a physically generated self predictor does not defeat the identity-gated alternative in the concern study. The revisable-concern reason graph still needs warranted transfer and actual paid routes; prediction of resource consequences cannot establish moral standing by itself.

The next useful integration must show that a continuing process constructs or retains this measurement-and-update architecture, can correct a once-useful cue when its dependency changes, and uses its physically learned predictor in an accountable action route. It must also identify which downstream target and threshold have actually been supplied. A successful first observation, a correctly computed mean and a sustained operative anchor are three different achievements.

Exact arithmetic:

```python
from fractions import Fraction as Q
eta, beta = Q(1, 4), Q(1, 2)
funded = beta * (1 - (1-eta)**3)
scarce = eta * (1 - (1-beta)**3)
assert funded == Q(37, 128)
assert scarce == Q(7, 32)
assert (1-beta)**3 == Q(1, 8)
```

This arithmetic verifies the displayed values only. The model, acquisition criterion, sampling conditions and costs require the arguments above and their separate implementation/review records.
