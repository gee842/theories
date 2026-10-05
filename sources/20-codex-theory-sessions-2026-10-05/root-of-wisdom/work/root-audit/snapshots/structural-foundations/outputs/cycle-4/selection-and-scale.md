# Selection, transmission, and actual behavior across scale

Cycle 4 mathematical memo, 5 October 2026. This extends the [cycle-3 transport result](../cycle-3/constraint-transport.md) from available control to the controller actually implemented. It provides finite-state proofs, an exact counterexample, and executable checks. The mathematics specializes established simulation and Markov aggregation reasoning; no mathematical originality or empirical universality is claimed.

## 1. A capacity correspondence does not select its implementation

The previous result has the form

`an abstract winning controller π exists ⇒ a compiled concrete winning controller κπ exists`.

It does not say that the actual concrete selector is `κπ`, learns it, adopts it, or transmits it intact. Equal capacity profiles can coexist with different actual behavior. Conversely, two particular selectors can have the same outcome even when their systems possess different unused capacities. These are distinct comparison questions.

Write the actual augmented configuration as `z=(q,c)`, where `q` contains the plant, accessible resources, access relations, and clocks, while `c=(g,m)` contains the current rule/program `g` and its physically retained working memory `m`. The separation is bookkeeping: controller memory and program carriers are physical components, with whatever costs and access constraints the model supplies.

An implemented mechanism specifies:

1. an action rule using only its permitted information and memory;
2. a plant/environment transition with its event order and actual payments;
3. an update rule for the program, memory, or parameters;
4. any succession or transmission channel that constructs a later controller.

These stages can be represented as separate phase states. When a stage learns, searches, interprets, communicates, or installs a new program, its duration and expense belong to that mechanism. A declared optimizer is not automatically a physically available operation. An initial program, supplied model, or fixed interpreter can instead be an endowed component, but this must be stated. Representing an update rule as state does not explain its origin or require an infinite hierarchy of unexplained optimizers; a model may explicitly take a finite update mechanism as its starting assumption.

Once the actual mechanism is fixed, the resulting closed loop has no analyst-controlled choice of a better policy. Denote its possible labeled transitions by

`z —e→ z'`.

The label `e` can report action, output, payments, elapsed time, or a rule-transfer event. Hidden state and retained memory remain in `z`; labels need not reveal them. Failure is an explicit absorbing state. Environmental restrictions and persistent random seeds must be represented in the augmented state or admitted histories. A missing transition or forgotten random seed is not an unmodeled source of success.

## 2. Exact example: same financial capacity, different selectors

The plant has three mandatory one-tick phases per cycle and a carried-cash cap of two. A cycle begins with two units of cash.

| Phase | Available operation | Payment and result |
|---|---|---|
| Operation | `RESERVE` or `CONSUME` | `RESERVE` costs zero and produces visible output one. `CONSUME` spends one reserve unit and produces visible output two. Neither output is a cash receipt. |
| Service | Pay one | A one-unit service bill must be paid before proceeding. |
| Succession | Pay one | A one-unit transmission/renewal bill must be paid. Only afterward does an external two-unit receipt arrive; surplus above the cap is discarded. |

The external receipt is a supplied renewal input, conditional on completing the succession stage. It cannot finance that stage's earlier fee. The model does not claim to explain the source of the receipt or equate visible output with money. Program execution between these events is supplied infrastructure. Copying the rule costs the same one unit regardless of its payload, so bills do not secretly signal the program bit.

The general controller class may choose either operation from the observed plant state. For the test of indefinite payment and cycle completion, the plant has a winning controller: always choose `RESERVE`. Its cash path within each cycle is `2→2→1→0→2`, where the final arrow is the post-payment receipt. The same test fails under an actual selector that always chooses `CONSUME`: its path begins `2→1→0`, so the succession fee cannot be paid. It produces more visible output before failing.

The complete controlled safe set, with phase labels `O,S,T`, is

`{(O,2),(S,2),(T,1),(T,2)}`.

This is obtained by the greatest safety fixed point in the checker. Starting plant state, menus, financial capacity, available observations, and disturbance conditions are identical in the two comparisons. Only the implemented selection rule differs. The capacity statement is relative to the declared financial test and general controller class; it is not equality for every imaginable test about program identity.

### An initially correct selector can fail through transmission

Let the actual controller carry a rule bit `g∈{R,C}`. At the operation phase it uses `RESERVE` when `g=R` and `CONSUME` when `g=C`; at other phases it attempts the mandatory bill. Its action rule is fixed and uses the visible rule register. There is no hidden optimizer.

An identity transmission channel preserves `g=R`, so the actual system continues. Another channel has the same fee, receipt, initial rule, and first two actions, but changes `R` into `C` at the first handoff. The first cycle succeeds; the second fails at succession. A correspondence that matches the initial selector and plant transition while omitting the controller update is therefore insufficient.

More generally, let each successful handoff independently change `R→C` with probability `μ`, and let `C` remain `C`. From initial rule `R`, survival through `N≥1` complete cycles is

`P(survive N cycles)=(1−μ)^(N−1)`.

**Proof.** A cycle entered with `R` completes. A cycle entered with `C` fails. The first `N−1` handoffs must therefore retain `R`; the final handoff's outcome cannot cause a payment failure until the following cycle. Multiply the independent retention probabilities. ∎

For `μ>0`, infinite survival has probability zero; the expected failed-cycle index is `1+1/μ`. These are statements under the supplied independent channel law, not consequences of merely allowing a corruption transition. At any two rates strictly between zero and one, the supported finite paths are identical, but their probabilities differ. For example, survival through four cycles is `27/64` at `μ=1/4` and `1/8` at `μ=1/2`.

The controlled plant still admits an always-`RESERVE` controller independent of the mutable program bit. This compares controllers at the plant's input interface; it does not claim that the already installed bit-driven program can replace itself for free. That particular mechanism does not implement the winning input sequence after corruption. This is precisely the gap between an available strategy in the declared comparison class and an actual transmitted one.

## 3. S4.1 — Robust transfer of a fixed actual closed loop

Consider augmented closed loops `L` and `H` with finite state and event sets, and nonempty successor sets including explicit failure. Let `R⊆Z_L×Z_H` relate their boundary configurations and let `χ` translate event labels. Suppose:

- each admitted concrete initial state has a related admitted abstract initial state;
- for every related pair and every **actual** concrete transition `z_L —e_L→ z'_L`, there is an actual abstract transition `z_H —χ(e_L)→ z'_H` with `z'_L R z'_H`;
- the tested observations, protected states, and target conditions translate in the required direction.

Then every actual concrete path has a matching actual abstract path after label translation. Hence every all-path property of the abstract closed loop that is preserved by the stated translation holds for the concrete loop.

**Proof.** Extend the matching path one actual transition at a time. The successor clause supplies a matching abstract edge from the already selected abstract state and reestablishes the relation. Induction gives every finite prefix. For an infinite concrete path, the finite, finitely branching tree of matching abstract prefixes has an infinite branch, yielding a matching path. Property transfer follows from the hypothesis on the test and labels. ∎

This theorem checks the system that runs; it does not replace the implemented concrete action with a better action that merely exists. In particular, the concrete update and transmission outcomes must be covered by the abstract **actual** update and transmission process. An identity relation on plant states cannot conceal a future difference caused by an omitted rule register.

For different time resolutions, an actual abstract step may correspond to a concrete adaptive protocol. Then all the cycle-3 conditions remain necessary for this sufficient certificate: recognizable stopping, admitted information and memory, every-prefix affordability and safety, and bounded completion. The actual lower-level selector must execute the certified local protocol. Controller amendments during it are included. A matching endpoint does not certify internal solvency. Stuttering or compression does not preserve an arbitrary deadline or liveness test without the appropriate progress and clock conditions.

S4.1 is sufficient, not necessary for equality of one selected performance score. Programs may have different internal representations while producing the same relevant behavior. What must correspond is the behavior needed for the specified transfer, not literal source code.

## 4. S4.2 — Exact transfer of path probabilities

For stochastic claims, matching supports is weaker than matching laws. Consider Markov closed loops with finite augmented state and event sets, whose states contain all retained controller and environment memory. S4.2–S4.4 use this finite setting; continuous event labels would instead require kernel equality or approximation on measurable sets. Let

`K_s(z; e,z')`

be the joint probability of the next event and state. This kernel includes the actual selector's randomization, environmental law, controller update, and transmission channel in their declared order. It includes their correlations; separate one-variable marginals are insufficient.

Let `φ:Z_L→Z_H` be a state projection and `χ:E_L→E_H` an event translation. Assume corresponding initial distributions and, for every concrete state and every abstract event/next-state pair, the equality

`Σ_{χ(e_L)=e_H, φ(z'_L)=z'_H} K_L(z_L;e_L,z'_L)`

`= K_H(φ(z_L);e_H,z'_H).`  **(K)**

Then the translated concrete labeled-state process has exactly the abstract path law. In particular, corresponding measurable path tests have equal probabilities, and corresponding integrable path costs have equal expectations after their stated unit conversion.

**Proof.** The initial pushforward distributions agree. Conditional on any concrete past, the next projected event/state distribution is the right side of (K); it depends on that past only through the current projected state. Multiplication and summation therefore give equality of every finite cylinder probability by induction. On the finite-state infinite product space, the cylinder probabilities determine the path measure, giving the infinite-path statement as well. ∎

This is a labeled strong aggregation condition. It must hold for every concrete state in each relevant fiber, not just for a favorable hidden representative or one average distribution. An implementation-specific restriction to an invariant reachable subset is allowed when that subset and its initial coverage are established. Standard finite Markov aggregation and stochastic bisimulation provide the mathematical precedent. [Givan, Dean, and Greig (2003), *Equivalence notions and model minimization in Markov decision processes*](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf).

One practical way to establish (K) is phase-by-phase correspondence of the actual action kernel, plant/environment kernel, observation delivery, memory update, and transmission kernel, with paid operations included. These sufficient local equalities compose into the whole-step equality by summing over the internal phase states. Accidental cancellation can also produce the same overall kernel; literal equality of every internal procedure is not logically necessary for every observable equivalence.

A proof for one environmental law does not establish transfer under another law or under every adaptive adversary. For a robust family of laws, the appropriate correspondence must hold uniformly for that family. If the environment has history-dependent behavior, its required state or history must be included. A hidden persistent coin and a newly sampled coin at every tick both have fair one-time marginals, but the probability that two consecutive outputs agree is respectively one and one-half.

The theorem is about the declared observation process. It does not assert preservation of information deliberately omitted from `φ`, arbitrary future tests, or physical internal safety erased by temporal sampling.

### A positive implementation in the checker

The checker builds three descriptions of the same actual mechanism. Their currency units scale as `1,2,6`; their rule registers encode `R` as respectively `0,1,7`; and their irrelevant phase tags cycle modulo `1,2,6`. Action interpretation and transmission are adapted to each encoding. Cash fees, receipts, and caps scale consistently. The maps divide currency units, decode the rule, and project the phase tag.

For each `μ∈{0,1/4,1/2,1}`, condition (K) holds in all three comparisons `L→M`, `M→H`, and `L→H`. Their translated finite path laws agree. Leaving the transmission law at a different `μ` breaks (K), even though action menus and supported paths can remain unchanged. These are unit and representation transformations with redundant state, not a general proof about physically enlarging an organization.

## 5. S4.3 — Correspondences compose

For robust relations, if `L→M` and `M→H` satisfy S4.1 with compatible tests, their relational composition and composed event translation satisfy S4.1. A concrete edge first obtains its matching middle edge, and that edge obtains its matching abstract edge. The paired successors remain in the composed relation. Actual local protocols can be nested under the additional cycle-3 interface, timing, and memory obligations.

For exact kernels, if `(φ_LM,χ_LM)` and `(φ_MH,χ_MH)` satisfy (K), then

`φ_LH=φ_MH∘φ_LM`, `χ_LH=χ_MH∘χ_LM`

satisfy (K). **Proof.** Sum the lower-level kernel first over each middle event/state fiber, replacing that sum with `K_M` using the first equality; then sum over the middle fibers belonging to the abstract event/state pair and apply the second equality. Initial distributions push forward by the same composition. ∎

Thus an actual process can be transported through several descriptions. This does not follow from a sequence of capacity inequalities if each intermediate system implements an unrelated selector.

### S4.4 — A finite-horizon approximation bound

Suppose initial projected distributions differ by total variation at most `δ`, and the two sides of (K) differ by total variation at most `ε` uniformly over relevant concrete states. Then the translated path laws through `N` transitions differ by total variation at most

`min(1,δ+Nε)`.

**Proof.** Couple the initial projected states with mismatch probability at most `δ`. Whenever the projected states still agree, couple the next joint event/state pairs with mismatch probability at most `ε`; the uniform bound applies whatever concrete state and past remain. A union bound gives `δ+Nε` for any mismatch. Differences in any path-event probability are bounded by that coupling's mismatch probability. ∎

The approximation controls a finite horizon. It may become vacuous as `N` increases, and does not by itself preserve an infinite sure guarantee, a strict threshold, or a narrow quality margin. Additional contraction, recurrence, or stability structure is needed for a sharper long-run assertion. The checker verifies this bound for the two mutation rates; it does not establish its universal proof mechanically.

## 6. S4.5 — When a supplied planning selector itself transports

The preceding conditions apply to optimizers as well as fixed rule bits, provided an optimizer is the actual declared mechanism. A useful special case concerns a finite planning selector that examines a tree of feasible candidate schedules, chooses the schedule with best terminal value, and executes its first action.

Suppose a scale map supplies:

1. a depth-preserving bijection between the two feasible planning trees, including all internal payment and access guards;
2. corresponding first actions and future observations;
3. terminal values related by `J_L=a J_H+b`, with `a>0` and `b` independent of the candidate at the current root;
4. a deterministic tie order that is preserved by the mapping;
5. corresponding controller updates, memory, and replanning events after each executed step.

Then the actual selected first actions correspond. If the same conditions persist at later states, the rolling selectors remain in correspondence.

**Proof.** Positive affine transformation preserves every strict value comparison and equality. The tree bijection preserves feasibility and the tie order selects corresponding maximizers. The first actions therefore match. The update condition reestablishes the hypotheses at the next planning root, so induction gives the closed-loop correspondence. ∎

A fallback that first maximizes feasible planning depth and then terminal value also transports under the same depth-preserving bijection and tie rule. If a physical replication introduces extra intermediate designs, the tree is no longer bijective; one must restrict menus to the scaled image or separately prove those new alternatives cannot change the decision. Merely scaling the optimum value of one candidate is insufficient.

This explains the scope of the companion rolling-horizon model. A supplied finite-horizon planner can explain how infrastructure choice changes with the current reserve and horizon. It does not explain why that horizon, objective, model, or algorithm was adopted. Supplying an explicit update and transmission rule for those quantities advances that causal explanation. It is not supplied by an abstract existence proof or by calling the planner rational.

## 7. What the extension establishes

The theory now distinguishes three implications:

- **Capacity transfer:** a response implementable at one level has an implementable counterpart.
- **Actual robust transfer:** every admitted trajectory of the implemented concrete mechanism has a corresponding trajectory of the implemented abstract mechanism.
- **Actual probabilistic transfer:** corresponding joint kernels and initial laws give corresponding trajectory probabilities.

These results require progressively different evidence. Capacity is not realized selection; robust support is not a probability law; and an individual rule's initial match is not a certificate for its learning or succession dynamics. Feedback-refinement work likewise emphasizes implementation architecture rather than arbitrary state-informed controller matches. [Reissig, Weber, and Rungger (2017), *Feedback Refinement Relations for the Synthesis of Symbolic Controllers*](https://arxiv.org/abs/1503.03715).

None of these results chooses a legitimate objective, establishes that a real organization has the declared channels, or guarantees that future unmodeled concepts fit the same representation. Their contribution is a checkable route from a proposed mechanism to a prediction, and a clear location for failure when scale changes selection, memory, updates, or environmental dependence.

## Preserved verification

The [standard-library checker](verification/check_selection_scale.py) checks the physical safe set, the two supplied selectors, corrupted succession, 1,020 exact kernel rows, 436 composed state maps, 104 finite path-law equalities, 80 exact survival formulas, and 13 finite-horizon approximation bounds. It also checks the persistent-versus-fresh coin distinction. [All assertions passed](verification/selection-scale-results.json).

These are exhaustive finite checks for the listed states, laws, and horizons. The general proofs above, the infinite-survival limit, and any proposed empirical application are separate claims.
