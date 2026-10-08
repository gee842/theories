# Selecting generators and evidence policies: a prospective mathematical interface

6 October 2026. AI-authored contribution to **consequence-sensitive selection of candidate-generation and evidence-retention policies**, following [model-family revision](MODEL-FAMILY-REVISION-MATH.md). This is a boundary proof and prospective design note. It adds no selector mechanism, paid return, autonomous generator origin or empirical outcome. Its accompanying checks may replay already installed operations and enumerate the finite logical countermodel; neither is a new meta-learning implementation.

The existing continuation uses an acquired model to construct and test a supplied larger candidate. That is substantive model revision. It does not yet explain why this generator or fresh-acquisition policy is installed. Replacing it with another supplied recipe must not be counted as deriving selection over recipes.

This note supplies three constraints and a minimal constructive interface. Future questions determine which historical distinctions need preserving; finite experiments cannot establish coverage against unrestricted continuations; and changing a selector requires an actual consequence-to-memory-to-enacted-policy causal path with payable operations. The current successful endpoints cannot fund the previous installation recipe. A new comparison from an earlier funded checkpoint would be an explicitly alternative history.

## 1. Exact scope and actual resource boundary

The [completed revision](../../../../theories/becoming/chapters/MODEL-FAMILY-REVISION.md) retains a model, observed-output parity and current cursor. Its new raw transcript remains external audit data. Its two successful primary continuations end as follows:

| Actual continuation | Fuel | Live cells | Remaining source |
|---|---:|---:|---:|
| Unchanged three-cycle | \(72475/65536\) | 33 | 0 |
| Declared four-cycle insertion | \(64123/65536\) | 35 | 0 |

These are checked fields in the [saved revision results](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/results.json). They are different branch endpoints, not additive resources. The generated fourth state and the environmental insertion also have different provenance: the learner constructs the candidate representation; the assay supplies the changed environment.

### Proposition M1 — The existing installation recipe is unavailable at both endpoints

Under the inherited tariffs, an installation with base charge 1 and eight work units costs at least

\[
1+\frac{8}{64}=\frac{73728}{65536}.
\]

Both displayed reserves are smaller. New cell writes, rent and temporary storage only add to this lower bound.

**Proof.** Compare numerators. The [existing account](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/diagnosis.py) rejects a charge before executing the charged operation if the reserve is insufficient. Neither endpoint has a remaining packet that can fund a prior installation. ∎

At the three-cycle endpoint, the previous eight-cell/eight-work installation pattern, with eight temporary cells and no other resident scratch, would cost \(82361/65536\): base 1, work \(8/64\), new writes \(8/64\), and rent \(49\cdot9/65536\). At the four-cycle endpoint its peak would be 51 and the bill \(82379/65536\). These are applications of the unchanged recipe, not bills for an implemented meta-selector.

The four-cycle endpoint cannot pay even base installation 1. The three-cycle endpoint can pay that base alone; M1 therefore does **not** establish that every imaginable cheaper retrofit or already installed operation is impossible there. In particular, the already installed forward-use procedure can be exercised without pretending to install it again. Its actual operations and any subsequent retention failure must be reported separately. The six other completed boundary configurations have their own remaining stocks; the two primary deficits are not a proof that all eight are blocked.

### Corollary M1a — Unfunded new income cannot support indefinite continuation

If no new income channel is added or physically exercised, and every native action/read costs at least \(1/4\), the four-cycle endpoint can execute at most three further native events and the three-cycle endpoint at most four. Other charges can reduce these counts.

**Proof.** \(k\) executed native events spend at least \(k/4\). The reserve must stay nonnegative at each prefix. Take the integer part of four times the initial reserve. ∎

This is a limit of the declared apparatus and tariffs, not a theorem that a sufficiently general physical system cannot obtain further support. Adding a new support channel would itself require an identified, funded interface. Moving to an earlier checkpoint means examining an alternative branch with its original stock and sunk costs, not rewinding the completed branch while keeping its later benefits.

## 2. Retention is relative to future questions

Let \(\mathcal H\) be the admitted complete histories, and let \(\mathcal F\) be a family of future questions. Question \(f\in\mathcal F\) has a specified answer \(f(h)\). Let \(m(h)\in M\) be **all retained information accessible at the later question**. Resource levels, clocks and persistent physical traces count if they carry accessible historical distinctions.

Define the future-answer profile

\[
\Phi_{\mathcal F}(h)=(f(h))_{f\in\mathcal F}.
\tag{M1}
\]

### Proposition M2 — Universal exact replay for a question family is profile sufficiency

A decoder \(D\) can satisfy

\[
D(m(h),f)=f(h)
\quad\text{for every }h\in\mathcal H,\ f\in\mathcal F
\tag{M2}
\]

if and only if

\[
m(h)=m(h')\ \Longrightarrow\
\Phi_{\mathcal F}(h)=\Phi_{\mathcal F}(h').
\tag{M3}
\]

**Proof.** A common decoder input \((m(h),f)\) has a common answer, giving necessity for each \(f\). Conversely, (M3) makes \(D(s,f)=f(h)\), for any \(h\) with \(m(h)=s\), well defined on attained memories. Values outside the attained image are immaterial. ∎

This extends the previous note's exact compatibility criterion from one proposed model family to all declared future questions. It remains an information theorem: effective decoding, reliable physical retention and affordable computation are additional obligations.

### Corollary M2a — Distinguishing future questions forbid lossless compression of history classes

If \(\mathcal F\) separates every pair of distinct admitted histories, (M3) requires \(m\) to be injective. More generally, let \(q\) be the number of distinct answer profiles on a finite admitted history set. Exact replay requires at least \(q\) memory states. A binary store of \(b\) bits, including every accessible source of historical information counted in the memory bound, requires

\[
2^b\ge q,
\qquad b\ge\lceil\log_2 q\rceil.
\tag{M4}
\]

**Proof.** Distinct profiles must have distinct memories by (M3). Count their images. Separation makes every history its own profile class. ∎

For example, all Boolean questions about a history separate the histories. A demand to answer every such later question exactly requires complete distinguishing information, even if some ingenious encoding makes particular answers cheap. This does not say all scientific inquiry needs raw event histories: restricted future questions may have a much smaller sufficient profile.

Neither the broad phrase “possibly useful later” nor a fixed finite memory supplies a uniquely correct compromise. Specifying which losses matter is part of specifying the future task or the actual organizational dependence.

## 3. A concrete obstruction to a universally best limited retention policy

Consider an admitted episode that acquires two independent bits \(x,y\). Before learning the future demand, a controller must retain only one binary memory state. All other later-accessible fields are independent of \((x,y)\), or are included in that one-bit bound. Future demand asks for either \(x\) or \(y\), identified when the question arrives.

Two available policies are \(P_x\), retain \(x\), and \(P_y\), retain \(y\). The future decoder may use both the retained bit and the named demand.

### Proposition M3 — No one-bit policy is everywhere at least as informative as both policies

There is no one-bit retention/decoding policy that is exact on every \(x\)-demand, as \(P_x\) is, and also exact on every \(y\)-demand, as \(P_y\) is.

**Proof.** Exact answers to both questions recover the pair \((x,y)\). There are four possible pairs and only two memory states, contradicting M2a. This covers every encoding, including adaptive encodings and parity, not just choosing one coordinate. Randomization cannot make both answers surely correct: a memory state used by two differing profiles would require incompatible certain decoded answers. ∎

The future demand changes the ranking of the two concrete policies. Under a supplied uniform distribution of independent bits and an always-\(x\) demand, \(P_x\) answers exactly while \(P_y\) can achieve probability at most \(1/2\). An always-\(y\) demand reverses those facts. These distributions are explicit counterexample contexts, not an inferred law of the current repository apparatus.

A physical version could make the correct demanded answer open an existing resource port, with identical costs and delivered resource otherwise. The same crossed comparison would then concern actual receipts. But that port, its calibration and the two future demand laws would be supplied environmental mechanisms. Calling their return “success” would not explain their origin.

The result rules out a policy that dominates all alternatives across these unrestricted demands. It does not rule out a best policy under a supplied probability law, a minimax or competitive guarantee under an explicit comparison criterion, a narrower question family, asymmetric costs or ethical priority. Those extra premises can make a choice well defined; they must not be attributed to the thin causal root merely because an optimization can use them.

There are \(2^4=16\) deterministic one-bit encoders on these four histories. Each future bit question has four one-bit-to-bit decoders, giving 16 decoder pairs and 256 encoder/decoder designs. Exhaustive enumeration can check the impossibility on this finite domain. It does not supply a future demand, wire a native reward or implement a retention selector.

The exact largest answer count is six of the eight history/question pairs. For any fixed decoder pair, each retained bit determines one reconstructed two-bit word, so there are at most two reconstructed words. At least two of the four true histories therefore differ from their reconstruction in at least one coordinate, forcing at least two incorrect answers. Retaining the first coordinate and always answering zero for the second attains six. This hand bound independently explains the enumeration's maximum; it does not assign probabilities or operational value to the questions.

## 4. Finite evidence does not choose a universally adequate generator

Candidate generation and candidate identification are different tasks. A finite program can enumerate every finite automaton given unbounded time and memory. The limitation here is finite paid generation and finite evidence, not the inability of a finite description to denote an infinite class.

For clarity take a unary deterministic binary-output process with a trusted starting boundary for this counterexample. Even this stronger access does not remove the following obstruction.

### Proposition M4 — Every finite observed prefix admits infinitely many distinct finite-state continuations

For every finite binary observation word \(v\), there are infinitely many pairwise behaviorally different deterministic finite-state processes whose reading stream begins with \(v\).

**Proof.** For each nonnegative \(k\), construct a finite chain emitting \(v\), then \(k\) zeros, then one, followed by an absorbing zero state. Different \(k\) place that later one at different positions. Each stream has a finite-state realization and the same observed prefix \(v\). ∎

### Corollary M4a — No finite generated family has evidence-certified unrestricted coverage

Given that prefix and a finite set of candidate output streams, at least one process from M4 remains observationally compatible but is absent from the candidate set.

**Proof.** A finite set cannot contain an infinite pairwise distinct set. ∎

The same delayed difference defeats any finite completed experiment whose observations inspect only a bounded continuation depth: choose the first disagreement beyond every inspected depth. For an adaptive experiment, construct the alternative to match the completed branch; the same observations induce the same choices along that branch.

The consequence is precise. No choice between a fixed finite collection of edit recipes can gain unrestricted model coverage from that finite evidence alone. A declared state bound, restricted grammar, temporal regularity, extra diagnostic channel or domain law can make finite coverage possible, as the earlier bounded learning proof illustrates. A generator that denotes all continuations avoids exclusion but does not thereby supply affordable distinguishing inference or a uniquely determined future prediction.

Likewise, choosing the cheapest recipe that fits the past does not prove it will fit the future. One can preserve the entire observed prefix and vary its continuation. Data-dependent generator selection requires justified restrictions connecting the observations to the later conditions where the chosen generator will be used.

## 5. The minimal causal interface for selection over policies

Let \(s\) be the complete accessible selector state, including the resources and memory needed by an installed architecture. A policy is an actually enacted recipe for candidate generation, evidence retention or both.

Suppose a completed operation produces an accessible consequence \(c\), such as an observed mismatch, a physically delivered resource or an executed/denied write. Let \(U(s,c)\) be the retained successor state after the consequence is sensed and its update is paid. Let \(E_w(s')\) be the future enacted control trace from successor state \(s'\), under a fixed admitted future context \(w\), including later payments and stops.

The symbols specify a proposed causal interface. They do not assert that its reader, writer, memory, program variation or support has already formed.

### Proposition M5 — Effective consequence-sensitive policy change requires a nonconstant composed route

At this interface, two feasible consequences \(c_0,c_1\) produce effective consequence-sensitive change of later policy if and only if

\[
E_w(U(s,c_0))\ne E_w(U(s,c_1))
\tag{M5}
\]

for some common admitted future context \(w\), with both consequence acquisition and relevant retained updates executed as stated.

**Proof.** The composed expression is the definition of the consequence's downstream causal effect at the specified boundary. If the traces coincide for every common context, the changed signal or stored label has no effect on enacted policy. If they differ, the two paid successor states cause a different later enactment under that context. ∎

This deliberately modest criterion prevents several substitutions:

- Changing an externally reported score is not changing a selector.
- Changing a stored policy label without changing later execution is not effective selection.
- An unpaid write cannot supply the successor memory assumed by the next operation.
- Receipt variation that only changes whether all work halts can demonstrate a resource dependence, but does not by itself demonstrate selection between generator or retention recipes.
- A direct signal-to-actuator response without a retained change may be regulation; the stronger history-dependent selection claim requires the retained route actually used later.

For a claim of selection **between recipes**, the differing traces in (M5) must instantiate the compared generation/retention operations while the compared execution opportunities are available. A complete collapse in one arm is a relevant failure, not a substitute positive witness of that stronger change.

The criterion establishes causal efficacy, not wisdom, statistical optimality or warrant. A misleading signal can satisfy (M5) and make later prediction worse. A truthful consequence can be incorrectly attributed to a policy when a changing environment or common cause produced it. Identifying that the route exists requires controlled or otherwise justified causal comparison; extrapolating usefulness requires additional stability and coverage evidence.

## 6. Minimal constructive comparison without an analyst reward channel

A prospective constructive test can use an earlier actual checkpoint only as an explicitly alternative continuation. Before implementation it must identify:

1. **Available variation:** at least two generation/retention recipes and how their executable differences are produced or already present.
2. **An operational dependence:** the native action, write, receipt or continuation affected by those differences, defined independently of the analyst's preferred recipe.
3. **Acquired feedback:** an actually sensed consequence and its calibration, attribution and cost. No oracle supplies “correct policy,” “good generator” or the intended winner.
4. **Retained influence:** a paid update that changes subsequent enacted recipe under M5, with the compared opportunities preserved where possible.
5. **Chronological funding:** construction, sensing, storage, replay, switching, later use and retention paid from that branch's actual stock and receipts.
6. **Failure comparisons:** severing feedback or the retained route, equalizing resource opportunities where feasible, misleading feedback, changed future demand and insufficient funding.

This test could explain how an installed architecture becomes consequence-sensitive about its own methods. It does not by itself explain the architecture's origin. The variation mechanism, consequence coupling and possible selector updates remain supplied until connected to an independently formed process. Reusing the repository's earlier formed sensing/revision mechanisms could supply some interfaces, but only a checked type, state and resource join would establish that composition. The present boundary round does not implement this test.

Two different kinds of result must remain distinct. **Differential persistence** occurs when a cheaper or better-supported recipe survives while another cannot be retained. **Acquired policy revision** occurs when one continuing system retains acquired information that changes which recipe it later enacts. Both can be consequence-sensitive; one is not automatically evidence of the other.

An operational constraint can select against expensive truth-preserving memory as readily as against wasteful error. With finite stock and no return, storing more accurate distinctions can prevent the next action from being executed. With later relevant demand, discarding those same distinctions can prevent recovery. M2–M3 show why neither “retain everything” nor “retain only the current model” is unconditionally favored.

More remaining fuel is not by itself a sufficient account of useful policy. In a model with no required operation or passive loss, doing nothing preserves the most fuel whenever all available operations have positive cost and no return. A native continuation obligation, deadline, dependency or receipt law is needed to make active inquiry serve an operational role. Such a law must be explicitly identified; adding an analyst's success condition does not derive it. Likewise, a record's proposed benefit must be exercised through an actual later demand and paid use before it is an operational result.

## 7. What this closes and what remains to be constructed

The information-level obligations are now precise:

- exact future replay requires the corresponding joint answer profile to survive in accessible memory;
- limited memory cannot dominate all retention alternatives over unrestricted future demands;
- finite observed agreement cannot certify unrestricted coverage by a finite generated family;
- effective selection over recipes requires a paid consequence-to-retained-state-to-enacted-policy path;
- the successful revision endpoints do not fund the previously used installation recipe, and no remaining source is silently available.

These results close several proposed unconditional routes. They do not show that consequence-sensitive policy revision is impossible. They define the premises a bounded positive construction must supply and the claims it may earn.

The next positive bridge is an explicit payable operational demand, its native feedback and the support for repeating the relevant work; renewable support is needed for a sustained claim. A finite comparison from an earlier funded checkpoint can test only a finite alternative history, without manufacturing renewable income. Only then can an actual consequence alter a retained selector and later generation/retention behavior under a connected paid process.

The right outcome is not fixed in advance: failure to fund it, loss under truthful but costly retention, or mislearning under a changed demand would change the account. A further supplied recipe with an externally stipulated winner would leave the explanatory bridge unresolved.
