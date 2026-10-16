# Retained evidence and warranted revision of a model family

6 October 2026. AI-authored proof and mechanism contribution to **retained evidence → warranted revision of the apparatus/model family**, continuing [experimental access](EXPERIMENTAL-ACCESS-MATH.md). This note separates exact reinterpretation of earlier observations, conservative reasoning when those observations were compressed, and fresh experiments about a possibly changed current apparatus.

**Result:** a retained state supports exact retrospective revision precisely when it preserves every distinction needed by the expanded compatibility calculation. An old-family belief need not do so. Fresh controlled observations can nevertheless identify a current model within a declared expanded family, while leaving the past explanation unresolved. For the retained three-cycle and a generated four-cycle extension, six consecutive readings, with five intervening actions and no reset, identify the current cycle, phase and observed-output parity within the stated class.

The proofs are elementary deterministic compatibility and information arguments. They are not a new general learning algorithm, new Lean verification or evidence that a finite hypothesis family covers all physical possibilities. The preceding [access result](../../../../theories/becoming/history/EXPERIMENTAL-ACCESS.md) supplies the actual ancestry and resource boundary; its sensor/target ambiguity, source consumption, calibration assumptions and out-of-family failures remain in force.

## 1. The retrospective question requires a specified evidence domain

Fix a set \(\mathcal H\) of possible completed control-observation histories. A history includes the commands and observations needed by the declared interface. Any relevant recipe version, initial-context constraint, clock, interruption or omitted-command distinction must either be part of this history or an explicit common premise.

For a proposed model family \(\mathcal C\), with its admitted initial configurations and transition/observation laws, let

\[
K_{\mathcal C}(h)
=\{\text{current configurations of }\mathcal C
\text{ reached by a run compatible with }h\}.
\tag{R1}
\]

This is the dynamic compatibility set proved correct in [D1 of the access note](EXPERIMENTAL-ACCESS-MATH.md#proposition-d1--the-update-retains-exactly-the-compatible-current-configurations). It evolves hidden states through the actual command sequence. It does not assume that resets work or that a final configuration is a label for the entire past.

Let

\[
m:\mathcal H\to M
\tag{R2}
\]

be the retained state available to the revising controller. For an impossibility claim, \(m\) must include **all accessible retained information**: not just the old belief, but any model, controller state, evidence record, accessible resource ledger, elapsed-count information or other field that can distinguish histories. A precise fuel balance can carry historical information. It cannot be silently omitted from a proof that the whole handoff has lost a distinction.

These definitions describe an information question. Physically reading \(m\), decoding it, creating new hypotheses and computing their compatibility remain paid operations.

## 2. The exact sufficient-memory criterion

### Proposition R1 — Exact retrospective revision iff compatibility is constant on memory fibers

There exists a decoder \(D:M\to\mathcal P(W_{\mathcal C})\) satisfying

\[
D(m(h))=K_{\mathcal C}(h)
\quad\text{for every }h\in\mathcal H
\tag{R3}
\]

if and only if

\[
m(h)=m(h')
\ \Longrightarrow\
K_{\mathcal C}(h)=K_{\mathcal C}(h')
\quad(h,h'\in\mathcal H).
\tag{R4}
\]

The decoder is uniquely determined on the attained memory states \(m(\mathcal H)\).

**Proof.** If \(D\) exists, equal inputs give equal decoded sets, proving necessity. Conversely, for an attained state \(s=m(h)\), define \(D(s)=K_{\mathcal C}(h)\). Condition (R4) makes this independent of the chosen history. These forced values are unique. Values outside the attained image can be assigned arbitrarily. ∎

The theorem is exact but does not assert effective or affordable decoding. The memory may encode its information in a form requiring more computation than the remaining apparatus can perform.

It also distinguishes targets of reconstruction. Recovering which model labels remain possible can require less memory than recovering every compatible current hidden state. Recovering a particular historical cause can require more. Replace \(K_{\mathcal C}(h)\) by the precise answer map being claimed; the same proof gives its necessary-and-sufficient memory condition.

### Corollary R1a — The compatibility profile is the coarsest sufficient summary

Define \(h\equiv_{\mathcal C}h'\) exactly when \(K_{\mathcal C}(h)=K_{\mathcal C}(h')\). The quotient by this relation is a coarsest exact summary for the retrospective question. Any sufficient memory has a unique map from its used states onto this quotient, taking \(m(h)\) to \([h]\).

**Proof.** Condition (R4) makes that map well defined; every class has a representing history, so the map is onto. Its values are prescribed on every used memory state. ∎

This is minimality in the information-partition sense, not minimal implementation cost or bit count. Defining a summary by the whole desired compatibility profile does not explain how the controller acquires or computes that profile.

For several anticipated future families, use the joint profile \((K_{\mathcal C}(h))_{\mathcal C}\). Sufficiency for the old family alone does not entail sufficiency for this richer question.

### Corollary R1b — Lossless evidence is sufficient for computable finite replay

If the retained evidence has a decoder recovering the relevant complete history \(h\), then it satisfies (R4) for every family interpreted on that same evidence interface. If that history decoder is computable, then for an effectively specified family with finitely many candidate configurations and computable transition/observation relations, exact compatibility can be computed by replaying each recorded command and observation through those relations.

**Proof.** Equal memories decode to the same history and hence the same compatibility set. For effective replay, first compute the decoded history. Dynamic update on that history then computes (R1), by the access-note induction. Finite histories and finite computable candidate relations make each update finite and effective. ∎

This does not mean a record is sufficient for every imaginable future physical hypothesis. A record of abstract actions and endpoint readings may omit real timing, interventions or context needed by a newly time-sensitive model. Sufficiency is relative to a declared observation/control interface and its context.

## 3. A concrete old-belief collision for the three- and four-cycles

Let the old family have a unary three-cycle with output sequence \(001\), unknown current phase and unknown uniform output parity \(b\in\{0,1\}\). A read leaves phase unchanged; action \(a\) advances one phase. Consider two transcripts, with an \(a\)-action between successive readings:

\[
h:\ 00,\qquad h':\ 00100.
\tag{R5}
\]

In the old three-cycle, both require starting phase \(0\) and parity \(0\). After the last reading, both are at phase \(1\): \(h\) has made one action, and \(h'\) four. Thus their old current beliefs are exactly the same singleton

\[
K_3(h)=K_3(h')=\{(3,1,0)\}.
\tag{R6}
\]

Now admit a four-cycle with sequence \(0001\). Use triples \((n,q,b)\) to label current cycle length, phase and observed-output parity. Here and in the reading-word proof below, phase means position along the cycle from its initial state. It is not necessarily the stored state identifier: the implemented insertion preserves old identifiers and walks through \(0,1,3,2\). For the expanded family,

\[
\begin{aligned}
K_{3,4}(h)
&=\{(3,1,0),(4,1,0),(4,2,0)\},\\
K_{3,4}(h')
&=\{(3,1,0),(4,1,0)\}.
\end{aligned}
\tag{R7}
\]

**Verification.** In the four-cycle, two zero readings can start at phase \(0\) or \(1\), ending at \(1\) or \(2\). The five-reading word \(00100\) can start only at phase \(1\), ending at phase \(1\) after four actions. No complemented version produces either word: every consecutive pair in the complemented three-cycle \(110\) contains a one, and the complemented four-cycle \(1110\) has no pair \(00\). The old-cycle claims follow directly from \(001\)'s rotations. ∎

Therefore the old belief alone fails criterion (R4) for the expanded family. It cannot tell whether the extra current possibility \((4,2,0)\) was excluded by the discarded observations.

This example deliberately proves insufficiency of **belief-only compression**. The transcript lengths and costs differ. It does not prove that two executions with those histories have identical full controller state or identical fuel. If the actual handoff retains such additional distinctions, their evidential value must be assessed and their decoding paid.

### Proposition R2 — Identical complete retained states cannot reconstruct a lost distinction

Suppose two histories have the same complete accessible retained state \(m(h)=m(h')\) but different answers to the retrospective question. No procedure using only that state, its own computation and random choices can guarantee the correct answer for both histories.

**Proof.** A deterministic procedure has the same input and makes the same state transitions, so returns the same answer. That answer cannot equal two different required answers. For a randomized procedure, couple the same random choices in both runs; the resulting output distributions are identical. They cannot each be concentrated with certainty on a different correct answer. ∎

More computation, payment or a new name for the old memory does not create the missing distinction. A new external observation might do so; it is then an additional information source with its own access and calibration conditions.

The current continuation takes a conservative operational route. It does not claim to have proved a collision of complete accessible handoffs in the earlier assay. It makes no uncharged retrospective query to the external audit and does not treat the old belief as exact new-family evidence. It acquires fresh current evidence instead.

## 4. What can honestly be inferred from insufficient memory

For a retained state \(s\), let

\[
\mathcal H_s=\{h\in\mathcal H:m(h)=s\}.
\]

If contextual information is also retained, include it when defining this set. When \(\mathcal H_s\ne\varnothing\), define

\[
K^+(s)=\bigcup_{h\in\mathcal H_s}K_{\mathcal C}(h),
\qquad
K^-(s)=\bigcap_{h\in\mathcal H_s}K_{\mathcal C}(h).
\tag{R8}
\]

### Proposition R3 — Union is the least conservative retrospective possibility set

For every possible actual history \(h\in\mathcal H_s\),

\[
K^-(s)\subseteq K_{\mathcal C}(h)\subseteq K^+(s).
\tag{R9}
\]

Moreover, \(K^+(s)\) is the least set that contains the exact compatibility set for every history consistent with the retained state.

**Proof.** The inclusions follow from intersection and union. Any set containing every \(K_{\mathcal C}(h)\) must contain their union. ∎

Using the intersection as the current possibility set would wrongly discard a world that fits the actual history but not another history that merely could have occurred. If a property holds in every configuration of the nonempty upper set, it is warranted for every covered actual history whose expanded class contains the actual configuration. An empty upper set is model inadequacy, not a vacuous positive diagnosis.

The upper set can be difficult or unaffordable to compute. Starting a fresh audit from all current configurations of a declared family is a still more conservative alternative when they include the actual current configuration. It abandons exact retrospective exclusion; it does not erase or refute the earlier evidence.

Dynamic updates distribute over unions:

\[
\operatorname{Upd}\left(\bigcup_i B_i,u,z\right)
=\bigcup_i\operatorname{Upd}(B_i,u,z).
\tag{R10}
\]

**Proof.** The existential predecessor in the definition belongs to a union exactly when it belongs to one member. ∎

Thus fresh evidence can refine a conservative possibility set soundly. It need not recover which earlier history supplied the actual member.

## 5. The expanded candidate is generated from acquired content

Let \(H\) be the actual retained three-state machine, with initial state \(q_0\), action \(a\), and cycle outputs \(001\). Its state labels need not be \(0,1,2\). Identify its unique positive-output state \(p\) by the retained output table, and its unique predecessor \(z\) on the learned cycle. That predecessor has output zero.

Construct \(\operatorname{Stut}(H)\) by creating one fresh state \(s\), assigning it output zero, and changing only the two relevant edges:

\[
z\xrightarrow{a}s\xrightarrow{a}p.
\tag{R11}
\]

All old labels, outputs and other transitions are preserved, as is the initial state. The cycle's output word from that initial state is now \(0001\). This is a supplied generative edit of the acquired table, not a hidden target table or a label saying the edit is correct.

The edit is equivariant under renaming learned states: apply the same construction after an isomorphism of \(H\), map the new state to the new state, and the resulting four-state machines are isomorphic. The chosen numeric name of the fresh state carries no physical phase information.

The current audit admits \(H\) and \(\operatorname{Stut}(H)\), all phases of each, and observed-output parity \(b=0,1\). This gives

\[
2\cdot3+2\cdot4=14
\tag{R12}
\]

observable configurations. It does not assume that the old family's diagnosis transfers unchanged into the enlarged current family. The old belief remains a historical conclusion under its earlier hypotheses.

Readiness reversal and sensor reversal are represented only through their parity in these readings. Their individual values remain ambiguous as in the access proof. Reset is not used, so reset fidelity is not newly established. No consequence probe is used, so the exhausted packet is not restored or implicitly borrowed.

The generator itself, the possible parities, the current-family coverage and stability during the assay remain supplied. Other transition changes, longer cycles, irregular delays or nonstationarity are not thereby excluded. The edit becomes a warranted selected current model only through its predictions and the new observations.

## 6. Six readings identify the current observational configuration

For \(n\in\{3,4\}\), write the corresponding reference cycle as \(p_3=001\), \(p_4=0001\). The reading sequence from phase \(q\) and parity \(b\) is

\[
y_k=p_n((q+k)\bmod n)\oplus b.
\tag{R13}
\]

Execute read, \(a\), read, \(a\), and so on, recording each actual output and advancing the candidates through each paid command. Stop if one observational configuration remains, or after six readings and five actions. No reset or physical phase label is needed.

### Proposition R4 — Six consecutive readings suffice, and five can fail

The length-six reading words for the 14 admitted initial configurations are all distinct. Consequently a completed matching six-reading transcript determines cycle family, initial audit phase, parity and current phase within this class.

**Proof across cycle families.** An uncomplemented three-cycle produces exactly two ones in six readings, separated by three positions; its complement produces exactly two zeros separated by three positions. An uncomplemented four-cycle produces one or two ones; when there are two, they are separated by four positions. Its complement has the analogous one or two zeros. Opposite parities cannot match across families, because an uncomplemented word has at most two ones and a complemented word has at least four. With the same parity, either the minority-bit counts differ, or their separation is three versus four. Thus no three-cycle word equals a four-cycle word.

**Proof within each family.** Reading a full period distinguishes all its cyclic phases because the reference word has exactly one positive position. Its complement has a different count of positive positions over that period, distinguishing parity as well. Six readings include a full period in both families, so the phase/parity words are distinct.

**Failure with five.** The three-cycle from phase \(0\), parity \(0\), and four-cycle from phase \(1\), parity \(0\), both produce \(00100\). Their complements both produce \(11011\). Thus five consecutive readings do not guarantee identification from unknown phase/parity. ∎

This is a sharp worst-case bound for this consecutive-reading protocol. It is not a lower bound on every adaptive experiment design with other permitted controls.

After \(k+1\) readings, the current phase has advanced by \(k\) actions. The controller must retain the current compatible states, not confuse the identified starting phase with the current one. Once a singleton remains, the selected cycle and parity give an output-preserving recursive prediction of every subsequent \(a\)-continuation under the family and stationarity premises.

This conclusion concerns current sensed behavior. A finite exact match to the family does not certify its own calibration, coverage or stability, and it does not uniquely diagnose the cause of a difference from the earlier apparatus.

## 7. Fresh observations need not identify the past cause

Current-family selection and historical explanation answer different questions. A four-cycle selected now could have been omitted earlier, could have arisen through an intervening change, or could still be only one representative of another currently indistinguishable law. Distinguishing those possibilities requires relevant evidence about the past or stronger justified persistence assumptions.

### Proposition R5 — A common present state can make different pasts permanently indistinguishable

Suppose two histories end with the same complete accessible controller state and the same current causal apparatus state for all permitted future controls, but have different historical-cause labels. Suppose their future laws are the same. No future adaptive experiment restricted to those controls can guarantee the correct past-cause label for both histories.

**Proof.** Couple the same future control choices and any random outcomes in the two cases. Their identical current states and future laws yield identical next observations and states. Induction yields the same complete future transcript, so the procedure's eventual historical answer is also the same. It cannot correctly name two different past causes. ∎

The qualifier “complete” matters. If an accessible log, persistent physical mark or witness distinguishes the histories, it belongs to the accessible state or adds a new permitted observation channel. The theorem does not prohibit historical knowledge; it states why current predictive success alone does not entail recovery of a discarded cause.

No such identical-state pair is being asserted without proof for the precise resource handoffs in this repository. In particular, the earlier undetected four-cycle branch has a different remaining reserve from the primary successful branch. Its funding failure cannot be turned into a successful continuation by substituting the primary branch's fuel.

## 8. Separate retention alternative: a paid evidence record would permit later replay

The implemented continuation chooses fresh reacquisition. It retains the selected model, parity and current cursor; its observation history remains an external auditor record unavailable to the learner. It does **not** implement raw-evidence retention or earn exact retrospective replay for a future expanded family.

A separate future design could retain the new observations in addition to a selected model. For the fixed consecutive-reading recipe, a lossless record of the assayed interface could consist of:

- the recipe/version and audit boundary/context it refers to;
- the number of completed readings and their ordered bits;
- enough interruption information to distinguish a completed prefix from a commanded but unrecorded action or read;
- the model reference or generator specification needed by the intended later interpretation.

The intervening command sequence is reconstructible from the declared recipe and completed-prefix information; it need not be copied verbatim if this reconstruction is exact. This is lossless coding for that interface, not the assumption that every raw physical event was observed.

If the record is retained and readable, R1b permits a later newly generated family to be tested against these actual observations by paid replay. The procedure must not substitute the selected model's predictions for the recorded bits: doing so would discard exactly the unexpected evidence that future revision may need.

If an action physically occurs but the next read or record cannot be paid, the evidence record and the current-state belief can be at different stages. Mark the interruption and either represent the unobserved transition uncertainty or stop with the last completed evidence prefix. Do not present a stale belief as a current certified state.

This proposed retention alternative would preserve distinctions for later paid reinterpretation under R1b. Its storage, recording, interruption handling and retention require their own implementation and comparison. The current experiment establishes revision by fresh evidence without claiming that additional result. Neither route automatically generates an adequate repertoire of future transformations or eliminates every relevant omitted variable.

## 9. Resource and ancestry obligations

The actual access-study handoff supplies its retained learned table, historical old-family belief, remaining fuel, live storage and any remaining source. Only those declared readable fields can influence the reviser. External analyst histories and hidden physical phase are not free learner inputs.

The successful sensor-reversal/probe branch and the earlier undetected four-cycle branch have different resource stocks. Current-family assays must retain their own actual ancestry. Alternative current phases or a newly inserted stutter are declared boundary configurations, not additional successful histories from the same stock or unexplained retrospective changes to the old target.

The implemented recipe needs paid installation or reprogramming, model copying/reference reads, stutter construction, candidate generation, live memory, prediction/filtering, updates from observations, compaction and final retention. The separate raw-record alternative in section 8 would additionally need paid observation records. The existing cartridge is a capacity bound, not free computation. The information bound of six reads and five actions excludes these additional costs.

For initial reserve \(R_0\), actual receipts \(u_t\) and charges \(c_t\), every executed prefix must satisfy

\[
R_0+\sum_{j\le t}u_j-\sum_{j<t}c_j\ge c_t.
\tag{R14}
\]

Storage must accommodate the old scoped archive while it is still held, newly generated candidates and the current temporary workspace. A retained evidence prefix would also count if the section 8 alternative were implemented; it is not part of the present learner's payload. A later compact model does not excuse an earlier allocation beyond capacity.

The present fresh sensor audit has no productive extraction and creates no new packet return. If it cannot run on the actual inherited fuel, the correct result is an interrupted or unavailable revision. An explicitly provisioned comparison can explore the information mechanism, but its extra resources must not be credited to the actual branch.

A completed observation sequence, a computed compatible set, a selected current model and an affordable later prediction are separate milestones. The implementation and checker must report which were actually paid. A retained raw evidence record is a further milestone not achieved here.

## 10. Scope and required verification

The mathematical bridge is closed at the declared scope: **exact retrospective revision requires a sufficient retained state; a conservative current-family audit can instead acquire new distinctions and retain a revised current predictive model.** The generated \(0001\) alternative supplies a concrete case in which a learned structure contributes to its own revision without receiving the correct larger model as an oracle. The implementation takes this fresh-evidence route without deciding whether the exact old handoff could support a different, paid retrospective decoder.

The supplied generator and finite family do not prove that this is the actual cause of earlier error, that no longer or different model is possible, or that a retained diagnosis justifies all its former empirical premises. Fresh conditional prediction improves warranted revision without promising complete self-calibration. Choosing which future distinctions to preserve remains unresolved; section 8 states an evidence-retention option, not a completed result.

Executable acceptance requires independent checks of actual ancestry, absence of audit/phase inputs, generated-state construction and renaming invariance, dynamic compatibility, the six-reading separation and five-reading collision, every resource/capacity prefix, retained result and inadequate-funding cases. Evidence-record replay is not an acceptance claim for this implementation.

### Executed continuation checkpoint

Read-only inspection of the [implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/revision.py), [protocol](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/PROTOCOL.md) and [saved results](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/results.json) confirms the intended information interfaces: candidates derive from the retained learned machine, the old scoped archive is not treated as new-family evidence, native observations filter current configurations, and compaction retains the selected machine/parity/cursor. The old archive and generated candidates are then discarded. The externally recorded new history never becomes a learner input.

The actual successful sensor-reversal/probe handoff has \(187921/16384\) fuel, 25 live cells and no remaining source packet. Its unchanged-apparatus continuation costs \(679209/65536\); the declared phase-insertion continuation costs \(687561/65536\). Both retain the selected model, execute one subsequent predicted action/read and retain the resulting state, with peak storage 118 cells. The inserted apparatus keeps the old positive state identifier; the new zero state is not an unannounced reinterpretation of that old state.

Across the 14 declared current-family boundary configurations at that inherited reserve, eight complete, four fail at a native-read payment and two fail final retention. A separately supplied reserve of 100 permits all 14 to complete, with maximum cost \(805831/65536\). This establishes finite-class semantic capability under supplied funding, not universal affordability on the actual history. The actual earlier undetected four-cycle branch keeps its own \(52327/65536\) reserve and cannot fund the new installation; the rich branch does not repair that failed continuation.

The saved checks also preserve a five-reading unresolved case, empty and undetected outside-family cases, a subsequent mismatch after a declared change, and a cursor commit denied after its physical action. Historical model acquisition, current predictive agreement and a currently usable retained cursor remain separate statuses. These checks concern a declared logical-cell and macro-work accounting model; they do not measure all physical computation costs or prove that the supplied candidate generator arose autonomously.
