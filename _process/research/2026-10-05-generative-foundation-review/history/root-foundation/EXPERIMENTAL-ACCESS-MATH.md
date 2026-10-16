# Warranted experimental access under competing apparatus explanations

6 October 2026. AI-authored proof and mechanism contribution to **acquired abstraction → evidence-dependent diagnosis of its experimental access**. This continues [abstraction acquisition](ABSTRACTION-ACQUISITION-MATH.md). The aim is to diagnose failures of model, sensor or reset without presupposing that a reset is faithful, receiving the correct fault label, or declaring a finite candidate library exhaustive merely because a candidate survives.

**Result:** controlled transcript updates preserve every compatible candidate world. A positive diagnosis is warranted within the supplied class exactly when its label is constant across the nonempty surviving belief. Some apparatus explanations remain indistinguishable under every sensor-only policy. An additional action consequence can separate them only through explicit assumptions connecting that consequence to the target and to a calibrated observation channel.

The concrete continuation below uses the *actual retained learned machine* as its reference, admits hidden current phase and several sensor/reset/target variants, and spends the last available packet on a discriminating consequence probe. It does not import a correct partition, physical phase name or diagnosis. It also does not promise a second productive use after diagnosis: the probe consumes that packet.

These are hand proofs and a proposed finite interface, not a new diagnosis algorithm, a new Lean result or empirical apparatus calibration. Maintaining uncertainty about hidden state and using actions both to obtain information and alter the world are established ideas in partially observable control; the present proof uses sets of compatible configurations rather than probabilities or an optimized reward. [Kaelbling, Littman and Cassandra, 1998, §§1 and 3](https://cs.brown.edu/courses/csci2951-k/papers/kaelbling98.pdf).

## 1. Candidate worlds include the apparatus and its hidden current state

Let \(W\) be a finite set of candidate configurations. A configuration can include:

- a target-law template and the target's current hidden state;
- a reset-law and sensor-law template;
- an action-to-consequence law and access to its source;
- resource state needed to determine which actions can actually occur.

The supplied initial belief \(B_0\subseteq W\) lists all configurations initially admitted by the diagnostic model. It may contain different hidden initial states under the same law. There is no requirement that a reset sends all candidates to one state.

Let \(U\) be the finite control alphabet and \(Z\) the observation alphabet. Each control has a declared transition-and-observation relation

\[
\Delta_u\subseteq W\times Z\times W.
\tag{D1}
\]

The deterministic case assigns a unique observation and successor to each enabled configuration. A control with no informative readout can emit a common symbol \(\bot\) while still changing the hidden state. A reset is represented by its candidate transition law, not by deleting the preceding history or replacing the belief with one assumed initial state.

Costs and denials must be explicit. A command may have a modeled denial observation or be ruled infeasible before execution. An unmodeled failure is not silently treated as a normal target output. The actual diagnostic experiment also has a retained observation record; the relation above does not create that record without its paid read, computation and storage.

For an actual control-observation transcript

\[
h_t=(u_0,z_0,\ldots,u_{t-1},z_{t-1}),
\]

define the belief update

\[
B_{t+1}=\operatorname{Upd}(B_t,u_t,z_t)
=\{w':\exists w\in B_t,\ (w,z_t,w')\in\Delta_{u_t}\}.
\tag{D2}
\]

This is a belief about the **current** configuration. Simply discarding static candidates without evolving their hidden states would in general be wrong, especially when reset is uncertain.

## 2. Exact transcript compatibility and the diagnosis criterion

### Proposition D1 — The update retains exactly the compatible current configurations

\(B_t\) is precisely the set of endpoints of candidate runs starting in \(B_0\) that realize the retained transcript \(h_t\).

**Proof.** At \(t=0\), the compatible endpoints are exactly \(B_0\). Suppose the assertion holds at \(t\). A candidate run realizes the extended transcript if and only if it has an endpoint \(w\in B_t\) and a next transition \((w,z_t,w')\in\Delta_{u_t}\). Its possible new endpoints are exactly (D2). Induction proves the assertion. ∎

Consequently, if the actual initial configuration is in \(B_0\), its subsequent transitions are admitted by the stated \(\Delta_u\), and the retained observations are faithful, then the actual current configuration remains in \(B_t\) at every step. This is a conditional soundness invariant, not a proof that the initial candidate class covers the actual apparatus.

Several initial configurations can merge into one current configuration after an action. A smaller current belief can therefore reflect physical convergence as well as newly discriminating evidence. It does not necessarily identify the earlier hidden state. Immutable fault parameters remain part of the configuration when they are the objects of diagnosis.

Let \(\ell:W\to D\) be the diagnosis label of interest. It might be a reset mode, a sensor parameter, a target-law parameter, or their tuple. The intended label must be defined independently of which answer the procedure happens to prefer.

### Proposition D2 — Positive diagnosis iff the label is constant on a nonempty belief

For \(B_t\ne\varnothing\), a label \(d\) is guaranteed correct for every candidate run compatible with the transcript if and only if

\[
\{\ell(w):w\in B_t\}=\{d\}.
\tag{D3}
\]

**Proof.** If (D3) holds, D1 places every compatible run's endpoint among configurations labeled \(d\). Conversely, if (D3) fails, some compatible endpoint has another label, and D1 supplies a candidate run witnessing that endpoint. Reporting \(d\) as certain would be wrong on that admitted run. ∎

This is a necessary-and-sufficient criterion for **class-relative warrant**. The valid report is “the retained transcript determines this label within the specified candidate laws and observation assumptions.” A unique label in a restricted library is not by itself a unique physical explanation.

If \(B_t=\varnothing\), the result is **candidate-class inadequacy or failure of another declared interface premise**. No ordinary candidate run explains the transcript. It is not a vacuous diagnosis of every label, proof of a contradiction in reality, or evidence selecting a new unlisted fault by name. The failure could lie in target dynamics, sensor, reset, control delivery, source access, observation recording, or the candidate assumptions themselves.

### Corollary D2a — Diagnosis and warranted prediction are different questions

Even when \(\ell\) is not constant, an enabled next control \(u\) has a uniquely predicted observation if every admitted successor from every \(w\in B_t\) has the same observation \(z\). Such a prediction is warranted within the class without a unique fault diagnosis.

Conversely, a fault label may be constant while the current hidden state remains uncertain, leaving a next observation or useful action uncertain. A diagnosis does not automatically supply a complete state estimate.

### Proposition D3 — Enlarging the candidate class can restore ambiguity

Suppose a larger model embeds the old configurations and preserves their control laws, with initial belief \(B_0\subseteq B'_0\). For the same retained transcript, \(B_t\subseteq B'_t\). Thus a previous class-relative unique diagnosis can cease to be unique after the class is expanded.

**Proof.** The update operator is monotone in its belief argument. Apply that fact inductively. New explanations cannot invalidate the old transcript's status as evidence, but they can invalidate the inference that its former sole label is the only admitted explanation. ∎

This makes model revision accountable: preserve the evidence and explain which added possibilities changed its implications. Do not silently promote exclusion by a narrow model class into empirical elimination.

### Proposition D3a — Independent latent factors can remain exactly factored

Suppose configurations are pairs \((x,\lambda)\in X\times\Lambda\), and the current belief is \(C\times\Lambda\). For a set of controls, suppose the full transition law is exactly

\[
((x,\lambda),z,(x',\lambda'))\in\Delta_u
\quad\Longleftrightarrow\quad
\lambda'=\lambda\ \land\ (x,z,x')\in\Delta^X_u.
\tag{D3a}
\]

Then, for those controls,

\[
\operatorname{Upd}(C\times\Lambda,u,z)
=\operatorname{Upd}_X(C,u,z)\times\Lambda.
\tag{D3b}
\]

**Proof.** A pair \((x',\lambda)\) belongs to the left side exactly when some \((x,\lambda)\in C\times\Lambda\) has \((x,z,x')\in\Delta^X_u\). This is exactly membership in the right side. Induction gives the same identity for any transcript of such controls. ∎

Consequently, a controller can store \(C\) and one shared representation of \(\Lambda\), instead of copying every pair, without losing a compatible world or choosing a preferred explanation. Availability and any resource behavior that the guarantee uses must also satisfy the claimed independence or be separately tracked. This is an exact representational equivalence under the stated law, not a minimum-fault preference.

A later control whose observation depends jointly on \(x,\lambda\) need not preserve a Cartesian product posterior. The controller must then retain their correlation, for example by paying to expand the product before that control and filtering its pairs. Independent factors cannot be silently maintained after evidence has coupled them.

## 3. Exactly when a bounded active diagnosis policy exists

An adaptive policy chooses its next control from the retained transcript, not from the hidden actual configuration. A diagnostic policy achieves information-level diagnosis within \(H\) controls when every admitted run ends in a nonempty belief on which the requested label is constant, with every executed control and required update feasible. A final paid report or retained diagnosis is a further terminal requirement unless explicitly included in the stopping condition.

The following finite recursion describes the information and action-feasibility requirement. Any resource state used by the feasibility test must be included in the belief or in an explicitly tracked common ledger. For this proposition, regard that ledger and relevant controller state as part of the planning state denoted by \(B\), and carry their updates with the control; feasibility cannot depend on omitted history.

Let \(\mathcal W_0\) contain exactly the nonempty label-constant beliefs. Define

\[
B\in\mathcal W_{h+1}
\quad\Longleftrightarrow\quad
B\in\mathcal W_0
\ \ \text{or}\ \
\exists u\ \left[
\begin{array}{l}
u\text{ is feasible at }B,\\
\text{at least one admitted outcome is possible, and}\\
\operatorname{Upd}(B,u,z)\in\mathcal W_h
\text{ for every }z\text{ with nonempty update}
\end{array}\right].
\tag{D4}
\]

“Feasible” here means the command can be executed under every configuration that the guarantee covers; if denial is itself an admitted control outcome, its nonempty successor belief must also satisfy the recursion. A state where the apparatus can disappear or terminate without an admitted observation needs that possibility represented explicitly.

### Proposition D4 — The recursion exactly characterizes bounded guaranteed diagnosis

There is a policy that guarantees information-level class-relative diagnosis from \(B\) within at most \(h\) controls if and only if \(B\in\mathcal W_h\).

**Proof.** At horizon zero, success means the current belief already satisfies (D3). For horizon \(h+1\), a nonterminal successful policy first chooses a feasible control \(u\). After every possible observation, its continuation must succeed within \(h\) more controls; the induction hypothesis gives the condition in (D4). Conversely, choose a witness \(u\) in (D4), then follow the inductively supplied successful continuation for each observed nonempty successor belief. This gives a policy for all admitted branches. ∎

This establishes a finite planning criterion for a finite model. It does not supply free planning computation, a universal success guarantee for every class, or an empirically optimal choice of experiment. Constructing and retaining the policy or computing each next choice must be paid. A supplied finite protocol can instead be verified directly against the criterion.

If the intended guarantee includes a final report or retention, replace \(\mathcal W_0\) by the label-constant states where that terminal operation is feasible and include its transition in completion. The same induction then characterizes the stronger paid guarantee. Label constancy alone must not be reported as having paid that terminal bill.

In particular, being able to distinguish some pairs in isolation need not provide a feasible policy for all pairs and all branches. An informative destructive action can exhaust the only available experimental object or packet. Its effect on future feasibility belongs in the configuration and cannot be omitted from the diagnosis claim.

## 4. An exact limit: indistinguishable access channels

### Proposition D5 — Observational symmetry defeats every adaptive diagnosis policy

Suppose \(w\) and \(\widetilde w\) have different labels and belong to a relation \(\mathcal R\) satisfying, for every permitted control:

1. the control has the same availability and declared charge in both configurations;
2. its observed outcomes are identical;
3. their successor configurations are again related.

Assume deterministic candidate laws for this statement. Then no adaptive policy using only those controls and observations can guarantee the correct label for both configurations.

**Proof.** Start the two runs with the same policy and, if randomized, the same internal random choices. Identical past observations give the same next control. The relation gives the same availability, charge and new observation, and relates the successors. Induction yields identical transcripts and ledger observations for the whole policy. A final reported label is therefore the same in both runs, but their true labels differ. It cannot be correct for both. ∎

Randomization does not create a zero-error distinction: conditioning on each common sequence of random choices gives the same argument. With an equal prior on the two configurations and one reported label, the probability of correct identification cannot exceed one half. Choosing a preferred label from a prior is not new experimental evidence.

For nondeterministic apparatus, matching only one possible successor per action is insufficient for this strong conclusion. A corresponding relation must match all possible observations and related successors in both directions, or otherwise establish equality of the relevant transcript possibilities or distributions. The deterministic fixture below meets the simpler conditions exactly.

More repetitions, more memory, better optimization or more payment cannot break an exact observational symmetry if the newly available acts preserve that same symmetry. A genuinely new consequence channel can break it, but then its law and calibration are additional premises.

## 5. A finite continuation constructed from the retained learned machine

The preceding acquisition produced a retained Moore machine \(H\) with three states. Its learned initial state is called \(0\) here, and its successive learned action-\(a\) states \(1,2\). These are *learned abstract state indices*, not physical phase labels disclosed to the learner. Its retained table is

\[
a(q)=q+1\pmod3,\qquad
h(q)=\mathbf 1[q=2].
\tag{D5}
\]

The executable diagnostic library should be constructed from this retained table. Replacing it with a hardcoded hidden target table would break the acquisition-to-diagnosis join.

The diagnostic extension supplies a family of possible apparatus transformations, not their correct values:

\[
\theta=(\tau,\sigma,r)\in\{0,1\}^3,\qquad q\in\{0,1,2\}.
\tag{D6}
\]

Here \(\tau\) determines whether actual readiness is complemented relative to the retained output, \(\sigma\) determines sensor complementation relative to actual readiness, and \(r\) chooses reset-to-the-learned-initial-state versus a no-op reset:

\[
\begin{aligned}
\rho_\theta(q)&=h(q)\mathbin{\oplus}\tau,\\
y_\theta(q)&=\rho_\theta(q)\mathbin{\oplus}\sigma
             =h(q)\mathbin{\oplus}\tau\mathbin{\oplus}\sigma,\\
\operatorname{reset}_\theta(q)&=
\begin{cases}0,&r=1,\\q,&r=0.\end{cases}
\end{aligned}
\tag{D7}
\]

Action \(a\) retains the learned cycle in every template. A read does not change that phase. Initial current phase is unknown, so the starting belief has \(8\cdot3=24\) configurations. The actual phase remains private to the apparatus. No historical audit query or successful old action word is an extra diagnostic input.

These are supplied current apparatus configurations or perturbation scenarios at the diagnostic boundary. In particular, a changed inversion parity is not described as an unchanged law that also produced the earlier exact \(001\) acquisition history. If the whole physical history is asserted to use one apparatus, such a case requires an intervening configuration change. The model and resource ancestry can remain actual while the origin or onset of that access change remains a supplied local input.

This is a deliberately small hypothesis class: fixed three-cycle dynamics, uniform global sensor/target complements, and two particular reset laws. It does not include every actuator fault, phase-dependent sensor defect, delay, external disturbance or nonstationary change. Its adequacy is a supplied local hypothesis, not an inference from the number of templates.

The parameters also need a semantic bridge. “Actual readiness” refers to the target condition governing the declared productive port, not merely to whatever bit the current sensor displays. The target-complement option changes that readiness law; the sensor-complement option changes the readout without changing readiness. This difference is invisible on the sensor channel alone but can matter for action.

### Proposition D6 — Sensor-only access can identify parity but not the two complements

For every sensor-only adaptive policy built from \(a\), reset and read, configurations

\[
(\tau,\sigma,r,q)
\quad\text{and}\quad
(\tau\mathbin{\oplus}1,\sigma\mathbin{\oplus}1,r,q)
\tag{D8}
\]

give identical transcripts, including the supplied common action charges.

**Proof.** Toggling both bits preserves \(\tau\oplus\sigma\), hence every sensed output. Action and reset ignore both bits and keep the phases equal. Charges are the same by the stipulated resource law. The paired configurations satisfy D5's invariant relation. ∎

In particular, a sensor inversion with an unchanged target and a target-readiness inversion with an unchanged sensor cannot be uniquely distinguished this way. A normal-looking sensor trace likewise cannot exclude compensating target and sensor inversions.

### Proposition D7 — A bounded active test diagnoses reset without assuming it

The following sensor-only protocol determines current phase, the parity \(b=\tau\oplus\sigma\), and the reset parameter \(r\) within this class, leaving exactly the two complement possibilities in (D8).

1. Execute read, \(a\), read, \(a\), read without a preliminary trusted reset.
2. From the surviving current phases, issue at most two \(a\)-actions to move to the learned state \(1\).
3. Issue reset as an experimental control, then one \(a\)-action and one read.

**Proof.** The first triple is one of

\[
\begin{array}{c|ccc}
\text{starting }q&0&1&2\\ \hline
b=0&001&010&100\\
b=1&110&101&011
\end{array}.
\tag{D9}
\]

All six triples are different. Thus the transcript determines the starting phase and parity within the class, and the current phase is its second successor. Moving to state \(1\) uses the learned cycle and that unanimous phase.

A reset from state \(1\) yields state \(0\) if \(r=1\), and leaves state \(1\) if \(r=0\). The following \(a\)-action therefore reaches state \(1\) or state \(2\), respectively. The read returns \(b\) in the first case and \(1\oplus b\) in the second, since the retained outputs there are zero and one. Thus it determines \(r\) and current phase. Both complement pairs with that parity and the determined \(r\) still realize the entire transcript by D6. There are therefore exactly two surviving configurations, differing in \(\tau,\sigma\) but sharing current phase. ∎

A full second read/\(a\)/read/\(a\)/read triple after reset would also distinguish the two reset laws by (D9). The shorter reset/\(a\)/read witness is sufficient once parity and the pre-reset phase are known, and uses fewer paid apparatus operations. It is the adopted protocol here.

The reset test works because it is applied at a state where the two proposed reset laws have different effects. A reset tested only at state \(0\) would not discriminate these laws. This is an actual test of a candidate access condition; it does not infer reset fidelity by using reset fidelity in its interpretation.

An implementation need not decode the triple by a separate correct-phase oracle. Applying (D2) to the supplied candidate transitions and actual observations yields the same unanimous phase and parity. A command selection based on that unanimity is an ordinary paid belief computation.

## 6. One paid consequence can break the symmetry, under its own bridge

After D7, current phase is \(1\) or \(2\). Use at most one further \(a\)-action to reach the retained model's positive state \(2\), where \(h(2)=1\). The controller can do so from the unanimous current phase. There remains one accessible source packet of value \(v=10\) under the primary continuation's resource contract.

The consequence probe has the following explicitly supplied law:

- its execution and read are prepaid;
- the packet is consumed whether productive or wasted;
- it transfers \(v\) exactly when \(\rho_\theta(q)=1\);
- a calibrated transfer record yields \(z=1\) for an actual transfer and \(z=0\) for no transfer.

This record is an additional observation channel. It does not become infallible merely by being described as an action consequence. Its calibration and the asserted access to one real packet are the bridge premises.

### Proposition D8 — The paid receipt selects the complement parameters within this class

At state \(2\), with the declared available packet and consequence law,

\[
z=1\oplus\tau,\qquad
\tau=1\oplus z,\qquad
\sigma=b\oplus\tau.
\tag{D10}
\]

The consequence observation therefore leaves one diagnosis \((\tau,\sigma,r)\) in the primary class.

**Proof.** The transfer bit equals actual readiness by the consequence law. Substitute \(h(2)=1\) into (D7). The previously acquired parity and reset parameter then determine all three coordinates. Both possible receipts produce a determinate class-relative diagnosis, even though only one receipt supplies a productive return. ∎

The whole proposed protocol uses at most four sensor reads, six \(a\)-actions, one reset and one consequence probe. The six actions comprise two in the initial triple, at most two for alignment before the reset test, one in that test, and at most one for alignment before the consequence probe. This is at most twelve apparatus controls. The transfer-receipt read/record, enumeration, model evaluation, belief filtering, selection, memory and retention require their additional paid operations. This control bound is not a count of every payment event, a total resource bill or a proof of affordability under a particular tariff.

The sole packet has now been consumed. Even a correctly diagnosed and retained model does not imply a second available productive use. A productive diagnostic branch may have gained fuel while exhausting the source; the two resource accounts must remain separate. On a nonproductive branch, the lost packet is a real cost of obtaining information.

Nor does a single successful probe independently calibrate every phase. It selects global \(\tau,\sigma\) because the library assumes a uniform complement law at every phase. If phase-dependent sensor or productivity laws are admitted, the same observation may constrain only the tested phase. Unique physical diagnosis requires a stronger justification than this finite-library elimination.

### Proposition D9 — Unknown source access preserves nonreceipt ambiguity

Expand the templates with a bit \(\lambda\) denoting whether the nominal last packet is actually accessible to the consequence probe. There are now \(16\cdot3=48\) initial configurations. The sensor laws do not depend on \(\lambda\). At the final state \(2\), suppose the transfer law is

\[
z=\lambda(1\oplus\tau).
\tag{D11}
\]

Then \(z=1\) selects \(\lambda=1,\tau=0\), but \(z=0\) admits

\[
(\lambda,\tau)=(0,0),(0,1),(1,1).
\tag{D12}
\]

For the already fixed parity \(b\), these include different sensor and target diagnoses.

**Proof.** Evaluate the four Boolean possibilities in (D11); \(\sigma=b\oplus\tau\) follows in each. ∎

This is a different access contract from treating the inherited stock ledger as an infallible certificate of present accessibility. The enlarged class can describe a packet that became inaccessible or a weakened inference from nominal stock to usable source. It should not simultaneously assert known accessible supply and admit its negation.

The bit \(\lambda\) records **pre-probe accessibility**, not a renewable packet after the probe. A subsequent model must account for the attempted consumption and the resulting source state. Keeping a template label \(\lambda=1\) is not permission to extract a second time.

Unknown actuator delivery or an uncalibrated transfer reader creates analogous alternatives. A zero return can then be explained by another failed bridge. The right result is the surviving ambiguity, not an arbitrary choice of “sensor fault” or “model fault.”

### Corollary D9a — Broader access uncertainty can be retained without literal duplication

During the sensor-only part of this fixture, the access/transfer factor \(\lambda\) affects neither phase transitions, reset, sensed outputs nor their charges. The 48-world belief therefore factors exactly as the 24-world sensor/reset belief times \(\{0,1\}\), by D3a. A shared two-value factor is enough until the consequence probe. After the sensor protocol, two sensor/reset candidates remain, so paid expansion produces just four joint candidates for that probe.

For zero receipt, the surviving three pairs in (D12) are not a Cartesian product: taking their separate coordinate projections would reintroduce the disproved pair \((\lambda,\tau)=(1,0)\). Materializing and filtering the four candidates preserves this correlation exactly. The construction has kept both access modes and all simultaneous sensor/target possibilities throughout; no world was discarded to make the diagnosis fit the budget.

This gives a transparent response to a literal 48-entry implementation that exceeds workspace capacity: preserve that failed implementation as a control, then evaluate a newly specified factored representation with its own paid generation, updates and expansion. The mathematical equivalence establishes preservation of epistemic content; actual affordability depends on the declared cell/work law and measured execution. It is not an optimal-cost theorem or evidence that the controller autonomously invented factorization.

## 7. Empty belief, model revision and persistence of uncertainty

For example, a nondestructive read/\(a\)/read/\(a\)/read sequence returning \(000\) is impossible in the 24-world class, because it is absent from (D9). If the observations are faithfully retained, the belief becomes empty. The appropriate status is **model-class inadequate**. Calling it specifically a stuck sensor would import a new explanation; a changed constant-output target or a failed actuator could also produce repeated readings outside the original class.

Conversely, a model outside the library can agree with every observation in a bounded diagnostic transcript and differ afterward. A hidden counter or delayed change can preserve the finite evidence without following the admitted stationary template forever. The earlier finite-state certificate and the present diagnosis are therefore both relative to declared classes; neither finite assay establishes its own class's universal adequacy.

The correct continuation after an empty belief is to preserve the transcript, expand or revise the candidate laws with explicit reasons, and repeat the compatibility calculation with paid work. D3 states how adding alternatives can weaken a previous conclusion. The present finite protocol does not claim to synthesize every needed new apparatus law automatically.

The current belief is a sufficient summary for the updates of its fixed family, but not generally for reinterpreting discarded observations in an enlarged family. For example, an old one-state model predicting zero after either control \(u\) or \(v\) leaves the same singleton belief after observing \(u/0\) and after observing \(v/0\). A newly admitted model predicting zero for \(u\) and one for \(v\) survives the first transcript but not the second. The old singleton belief alone cannot determine this difference. If the full history exists only in external analyst logs, a controller cannot freely consult it for model-family revision. Such revision needs paid access to an adequate retained evidence representation, reconstruction justified by its retained state, or fresh experiments. The present controller's fixed-family updates do not implement that further bridge.

A nonempty ambiguous belief is also a completed informative result. It can prove that reset mode is determined while sensor/target inversion is not, identify a necessary additional consequence channel, or show that no permitted sensor-only experiment can supply the requested distinction. D5 turns the latter from an unsuccessful search into an exact no-guarantee theorem.

## 8. Resource and memory obligations for the actual continuation

The earlier primary acquisition/use trace supplies an actual retained \(H\), inherited fuel and one remaining source packet. The diagnostic stage must read the retained model and initialize its candidate templates through paid operations. Its controller and fault-transformation repertoire are newly supplied local machinery; their presence is not an inference from having learned \(H\).

The proposed implementation reuses the existing workspace cartridge. Compact template identifiers and current-state indices can represent the 24 candidates without copying a hidden target table. The lawful transformation rules, their evaluation, belief scans and selection work must still be charged. Logical-cell accounting is an explicit abstract implementation law, not measured Python memory or physical energy.

For any actual event sequence, let \(c_t\ge0\) be its charge and \(u_t\) a resource receipt genuinely available before that event. The exact payment requirement remains

\[
R_0+\sum_{j\le t}u_j-\sum_{j<t}c_j\ge c_t
\quad\text{at every paid prefix}.
\tag{D13}
\]

Each event also requires capacity for the live model, control state, current belief, retained evidence needed by the controller, and its declared temporary workspace. Candidate elimination is not free merely because it reduces the final belief size. A paid read followed by an unaffordable update does not authorize committing the uncomputed diagnosis.

A productive receipt may legitimately finance a later belief update or retention only after the packet has actually transferred. It cannot pay retrospectively for the actions and work needed to obtain the receipt. A policy claimed to guarantee diagnosis in every admitted case must fund the nonproductive branch as well, or report that branch's funding failure.

Failed payment and inadequate capacity are operational outcomes. They need not imply that a particular sensor or reset explanation is false. A completed informative transcript, a paid diagnosis calculation, a retained usable diagnosis, and renewed ability to act are separate milestones.

## 9. Scope of the closed connection

The positive bridge is now precise: **a learned model can generate competing access hypotheses; paid controlled observations can update their hidden states, expose an acquired mismatch, and establish a diagnosis exactly when the retained evidence forces its label within the candidate class.** Reset fidelity can be an object of testing instead of a prerequisite silently reused in every test.

The negative result is equally strong at its stated scope: sensor-only evidence cannot distinguish configurations related by the exact inversion symmetry. An action consequence breaks that symmetry only through the declared supply, actuator and calibrated receipt laws. If those laws are themselves broadened, the diagnosis broadens accordingly.

This is a conventional belief-state diagnostic mechanism operating on actually acquired model content. It does not establish the origin of the fault library, the correctness of every access premise, a universal learning guarantee, a uniquely privileged physical ontology, or an ethical reason to consume resources for information. Those remain distinct explanatory questions under the governing generative-grounding programme.

The executable continuation must independently verify its actual inheritance, candidate construction from retained \(H\), dynamic transcript compatibility, nonempty-label stopping rule, sensor-only ambiguity, consequence-dependent update, payment/capacity prefixes, packet consumption and failure cases. This note establishes the mathematical contract; it does not predeclare the numerical assay's acceptance.

## 10. Implementation review checkpoint

The [diagnostic implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/diagnosis.py) was inspected against the belief update, inversion symmetry and adopted shorter reset test. It builds candidate transformations from the passed retained model, receives native observations through a callback, and keeps physical phase and actual fault flags outside the controller's inputs. Its code uses a broken-reset bit equal to \(1-r\) and a blocked-transfer bit equal to \(1-\lambda\) in the notation above.

A read-only reproduction first ran the preceding acquisition/use fixture, then passed its actually learned model, resulting fuel \(1030367/65536\) and remaining source 10 into diagnosis. Across all 24 combinations of target complement, sensor complement, reset mode and hidden current phase, the diagnostic runs completed with the correct unique class-relative label, retained the two sensor-only inversion alternatives before the consequence probe, and consumed the final packet. These are alternative assay cases, not 24 uses of one physical stock.

The literal 48-entry representation stopped at the first read's workspace check. Its greatest accepted allocation was 215 cells; the proposed next workspace would exceed the capacity 256. In the inspected blocked-transfer case, the exact factored representation completed with peak 150 cells, retained three compatible explanations for zero receipt, received no return and exhausted the packet. This reproduces the qualitative distinction in D9/D9a without claiming cost optimality.

This checkpoint checks implementation correspondence and expected semantic outcomes. It does not independently replay the earlier Fast precursor or replace the package's separate event-by-event resource and capacity reconstruction. The acceptance record must preserve that broader audit and the literal representation's failure.
