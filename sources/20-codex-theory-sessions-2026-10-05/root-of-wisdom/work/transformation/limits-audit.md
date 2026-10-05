# Independent audit: transformation, information, and continued viability

5 October 2026. This note reviews the proposed next branch against `outputs/differentiation-and-viewpoints.md`. It supplies original finite-model proofs and counterexamples. It does not revise earlier outputs or claim a new result in the general mathematical literature. No external claim is needed for the proofs below.

## Verdict

There is a substantive advance if one integrated mechanism pays the costs of changing its sensing, accessible inputs, and conversion machinery, then survives an environmental sequence that every permanently fitted configuration fails. The comparison must name that restricted fixed-configuration class. A finite controller that changes its hardware is itself a fixed larger dynamical system once hardware configuration is included in the state.

The most useful generalization is: **adequacy is a property of available information, feasible action, and the transitions through which those capabilities can be maintained or changed.** It is not a property of an observation partition considered alone. A distinguishing experiment can exist while every way to perform it destroys the system before it can use the result.

## 1. A finite multi-step extension of the information–action criterion

Let \(X\) be a finite set of world-and-organization states, \(A\) a finite action set, and \(g:X\to O\) the observation available before each action. The state includes any hardware configuration, stored resources, environmental phase, and relevant physical memory. Let

\[
F:X\times A\to 2^X\setminus\{\varnothing\}
\]

give the possible successors. Nondeterminism represents all disturbances allowed by the stated contract. An unavailable action leads to a distinguished absorbing failure state, rather than silently removing its incompatible worlds from consideration. Let \(K\subseteq X\) be the explicitly stated set of acceptable continuing states; failure is outside \(K\).

A belief \(B\) is the nonempty set of states still compatible with the complete available history. At a decision instant, \(B\) lies in one observation class of \(g\). Let \(\mathcal B_K\) be the finite set of all such nonempty beliefs contained in \(K\).

For an action \(a\), define

\[
P(B,a)=\bigcup_{x\in B}F(x,a),\qquad
U(B,a,o)=P(B,a)\cap g^{-1}(o).
\]

The belief update retains exactly the successor states compatible with the next observation. Define

\[
\Phi(W)=\{B\in\mathcal B_K:\exists a\in A,
\ P(B,a)\subseteq K\ \text{and}
\ \forall o,\ U(B,a,o)\ne\varnothing\Rightarrow U(B,a,o)\in W\}.
\tag{1}
\]

Starting with \(W_0=\mathcal B_K\), set \(W_{n+1}=\Phi(W_n)\). These sets descend, and stabilize after at most \(|\mathcal B_K|\) strict eliminations. Write \(W_\infty\) for the fixed point.

**Theorem.** A history-dependent policy can keep the system in \(K\) forever, against every allowed disturbance sequence from initial belief \(B_0\), if and only if \(B_0\in W_\infty\).

**Proof.** Inductively, \(W_n\) consists exactly of beliefs from which some policy guarantees safety for the next \(n\) transitions. To extend a guarantee by one step, one action must be safe for every currently possible state, and the resulting belief after every possible observation must have an \(n\)-step continuation. This is exactly (1). At a fixed-point belief choose one witnessing action. The next belief stays in the fixed point, so repeating the choice guarantees safety indefinitely. Conversely, any indefinite policy guarantees every finite horizon and therefore its initial belief belongs to every \(W_n\), hence to their stabilized intersection. □

For this safety objective a policy depending only on the current belief suffices; this does not mean that the current raw sensor value suffices. The belief already summarizes the relevant history under the supplied transition model. Randomization cannot create a sure safety guarantee when every available action has an allowed failing continuation.

If a requirement is terminal success at a finite horizon rather than safety at every step, use backward recursion from the specified acceptable terminal beliefs. Do not identify finite-horizon success, indefinite safety, eventual success, or repeated attainment: their objectives and recursions differ.

### Relation to the one-step intersection criterion

For one transition, define \(A_K(x)=\{a:F(x,a)\subseteq K\}\). Then

\[
B\in W_1\quad\Longleftrightarrow\quad
\bigcap_{x\in B}A_K(x)\ne\varnothing.
\]

For multiple steps, the action must also preserve a successor belief with a viable continuation. **An immediately acceptable common action is necessary but need not be sufficient for continued viability.**

Reconfiguring a sensor or a boundary does not invalidate the theorem. Include configuration in \(X\), let observations and transitions depend on it, and include the reconfiguration's intermediate states and costs. Changing the represented state variables without supplying their transition mechanism would instead change the model from outside.

## 2. Four exact failure cases

### A. Every actual state is individually controllable, but the viewpoint is inadequate

Two states \(x,y\) give the same observation. In \(x\), action 0 returns to \(x\) while action 1 fails. In \(y\), action 1 returns to \(y\) while action 0 fails. Each singleton is viable with full information; the belief \(\{x,y\}\) is not. Combining statewise viability kernels without preserving the common-action constraint makes a false guarantee.

### B. A safe first step can be a dead end

Both available actions take safe state \(x\) to safe state \(y\); both actions at \(y\) lead to failure. At \(x\) the immediate common-action intersection is nonempty, but there is no indefinitely safe policy. The fixed-point recursion removes \(y\), then \(x\).

### C. Acquiring a distinction can repair the problem

Before a probe, worlds 0 and 1 have the same observation and require opposite terminal actions. A probe preserves safety and produces distinguishable records of the two worlds. The probe followed by the corresponding response succeeds. A criterion that examines only current terminal responses would miss this viable history policy.

### D. The same distinction can be unreachable while alive

Change only the probe so it destroys the organization in world 1. Now neither immediate response works in both worlds, and probing cannot guarantee continuation. Perfect information in a hypothetical successor state is irrelevant if reaching it violates the requirement. No amount of describing the distinction replaces a feasible path to it.

The check program verifies these cases and independently compares (1) to exhaustive stationary belief-policy enumeration for all 81 deterministic transition tables with two safe states, two actions, and one failure state, under both observation partitions. Across 162 systems and 972 policies the winning beliefs agree exactly. These checks detect implementation mistakes; the theorem rests on the proof.

## 3. Audit of the proposed joint receptor–transporter–converter construction

The shared construction has one fitted type \(q\in\{A,B\}\), a resource reserve \(r\le K\), and a receptor, selective transporter, and converter fitted to that type. Availability is \(E_t\in\{\{A\},\{B\},\{A,B\}\}\). The processing bit \(h_q\) is revealed by the fitted receptor when its resource is present. Correct processing yields 2 reserve units before maintenance costs 1; the stored reserve is capped at \(K\). A two-tick reconstruction changes the fitted triplet, supplies no harvest, and costs 1 on each tick. A state is alive only if \(r\ge1\) after every tick; depletion prevents further reconstruction and operation.

For the proposed controller, absent fitted input triggers reconstruction immediately. With \(K=3\), a reconstruction followed by two successful processing ticks gives the reserve path

\[
3\longrightarrow2\longrightarrow1\longrightarrow2\longrightarrow3.
\]

If every constant-availability phase lasts at least four ticks, the process starts at the beginning of such a phase with reserve 3, and the initial fitted type is arbitrary, the first four ticks either retain a present type or complete that path. Once restored, continued availability holds it at reserve 3. At each subsequent phase boundary the reserve is therefore full. Induction gives indefinite operation for every allowed availability sequence and every processing-bit sequence, using only local receptor signals and reconstruction stage.

**Timing matters.** With arbitrary initial phase position and an initially absent fitted type, the remaining availability interval might end during reconstruction. Four-tick full phases do not imply four remaining ticks. The theorem must retain its initial phase-start contract, or replace it with a separately proved initialization condition. Initial matching with full reserve is another sufficient entry condition because the first mismatch is then detected at a later phase boundary.

**The reserve threshold is sharp for this mechanism.** Completing any reconstruction consumes two reserve units without replenishment. Maintaining \(r\ge1\) therefore requires a reserve of at least 3 at its start. With \(K\le2\), reconstruction is impossible while alive, even with perfect knowledge of future availability. An opposite-only phase of unbounded duration defeats every permanently fitted type. Thus \(K\ge3\) is necessary for a universal survival guarantee over the specified environmental class.

**At capacity 3, the four-tick minimum phase length is also sharp for a universal guarantee.** Consider the permitted counterexample consisting of alternating A-only and B-only phases, each of length 3. Any surviving full phase must contain at least one successful harvest: three ticks without a successful harvest exhaust a reserve capped at 3. Across \(n\) phases the harvested resource therefore alternates, requiring at least \(n-1\) completed reconstructions between representative successful harvests in consecutive phases. Each reconstruction occupies two ticks without harvesting. The number \(H\) of successful harvests in the \(3n\) ticks consequently satisfies

\[
H\le3n-2(n-1)=n+2.
\]

Every successful harvest increases reserve by at most 1; each other tick decreases it by 1. Even granting perfect processing and knowledge of the entire future, the final reserve satisfies

\[
r_{3n}\le3+H-(3n-H)\le7-n.
\]

At \(n=7\), survival would require both \(r_{21}\ge1\) and \(r_{21}\le0\), a contradiction. This defeats every allowed control history, including anticipatory reconstruction; it is not merely a failure of the reactive controller. Exhaustive reachable-state propagation over all harvest, wait, and reconstruction histories gives an even earlier failure: no history survives the 14th tick. The analytical 21-tick bound is deliberately not claimed sharp. The necessity statement is for capacity 3 and the universal phase contract; larger capacities can change the result. In particular, capacity 4 can survive this particular repeating three-tick schedule with one permanently fitted type by bridging each three-tick absence.

**Why all three changes matter.** Permanent transport or conversion of only one resource defeats operation during an indefinitely sustained opposite-only phase. If transport and conversion can change but the receptor remains fixed to the original type, the arbitrary processing bits of the opposite resource remain unobserved. No policy can guarantee correct processing on every allowed bit sequence. The information limitation is distinct from the resource-access limitation. This claim requires the stated restriction that no other observation reveals those bits; an implicit global controller would invalidate the comparison.

The construction integrates sensing, access, conversion, and the reserve that funds their replacement in one transition mechanism. It remains a deliberately supplied two-type mechanism, with external resources and a designed reconstruction capability. It does not explain the physical origin of that machinery, how an unforeseen third type is discovered, or unrestricted transformation.

## 4. The fixed-controller issue

An adaptive implementation is described by a constant overall rule whose state includes its current configuration. It therefore cannot establish that adaptation defeats every fixed algorithm, every fixed architecture, or every fixed global law. The fair comparator here is **a permanently fitted single configuration under the same interface-slot and reserve constraints**. A larger permanent device with two receptors, transporters, and converters might succeed without reconstructing; its extra resource and interface costs must be counted before comparison.

Similarly, an infinitely long run of reversible switches demonstrates continuing successful use of a finite repertoire. It does not show an ability to generate indefinitely many new capabilities, learn an unknown chemistry, revise the laws that govern reconstruction, or survive every possible world.

## 5. Physical stakes and chosen purposes

Making depletion disable future sensing and reconstruction gives a causal explanation for why reserve differences affect the continuation of this organization. This is stronger than attaching a reward number to otherwise unchanged transitions. But the investigator still specifies the model, the organization whose continuation is being considered, and the property \(K\) that the guarantee protects. The causal implication is objective within the mechanism; its moral importance is not derived by that fact alone.

A different organization can have different dependencies. Transforming the organization can change which distinctions are consequential for its continuation. It does not follow that any such transformation is good, that continued operation is always preferable, or that protecting one organization's kernel accounts for everyone it affects.

Changing \(K\) after a failure must be reported as changing the task. A stronger theory of wise transformation would make the reasons for such revision explicit and preserve facts about who loses capacities or bears costs. Physical self-maintenance, learning, justified revision of aims, and ethical concern are distinct achievements.

## 6. The impossibility that remains

If two permitted worlds generate the same complete available history under every safe inquiry policy, but eventual continuation requires disjoint action sets, no controller restricted to those histories can guarantee continuation in both. Changing the language used for unity, intelligence, or wisdom does not remove that indistinguishability. A genuine repair must supply a new feasible discriminating interaction, a common response, or a justified change in the protected requirement.

This result is relative to the permitted worlds and actions. It does not provide a complete method for discovering omissions from an unrestricted world model. A violated guarantee could expose an omitted state, an incorrect transition, an uncounted cost, an observation failure, or a requirement that was never actually satisfied. The investigation must identify which premise failed.

## 7. Recommended claim

> A system can preserve an ongoing capacity by changing the organization through which that capacity is exercised. Such change is possible only when its current information and resources support a viable transition to the new arrangement.

For the philosophical inquiry, this is a precise refinement of maintained differentiation: **a continuing individual need not preserve one arrangement of its interface, but continuity of operation depends on the realizable path between arrangements.** It explains one mechanism of transformation within common dynamics. It does not yet equate functional transformation with wisdom or settle metaphysical monism.

## Files

- `work/transformation/check_limits.py`: executable independent finite checks.
- `work/transformation/limits-checks.json`: exact results.
- This note: proof, comparison scope, counterexamples, and model audit.
