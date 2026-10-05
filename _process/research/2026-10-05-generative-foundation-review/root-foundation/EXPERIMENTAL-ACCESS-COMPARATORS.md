# Warranted experimental access: diagnosis, active tests and identification

**6 October 2026. AI-authored supporting review.** Named connection: **acquired abstraction → paid tests of model, sensor and reset assumptions → warranted diagnosis or retained ambiguity**. This continues [abstraction acquisition](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ABSTRACTION-ACQUISITION.md) and its [comparator requirements](ABSTRACTION-ACQUISITION-COMPARATORS.md). The target is a small conditional mechanism, not a new empirical study or a derivation of every experimental primitive.

**Finding:** the proposed inference is an established form of model-based diagnosis and active experimental design. It can remove a supplied correct fault label by comparing complete candidate explanations against actually acquired consequences. Its warrant remains conditional on the candidate class and observation laws. A genuine ambiguity must survive when available experiments do not separate the remaining explanations. Paying for an experiment does not validate its interpretation.

## 1. Three primary comparisons

**Reiter: consistency-based diagnosis.** Reiter's 1987 framework supplies a system description, component vocabulary and observations, and diagnoses abnormalities that restore consistency. Its minimal diagnoses use set inclusion, not simply the smallest number of faults. The paper also studies measurements that discriminate competing diagnoses. A particularly relevant result is that new observations can produce new minimal diagnoses containing multiple faults; filtering only the old minimal diagnoses can lose them. These claims were checked in Definition 2.4, Theorem 4.4 and §5, especially Example 5.6 and Theorem 5.7. Our full-world candidate filter should not be confused with a filter restricted to currently preferred minimal fault labels. [Reiter, *A Theory of Diagnosis from First Principles*, primary full text](https://www.cs.ru.nl/~peterl/teaching/KeR/reiter.pdf).

**Sampath, Lafortune and Teneketzis: active diagnosis.** Their 1998 approach designs a controller that restricts a discrete-event system's behavior so faults become diagnosable. The supplied model includes normal and failed behavior, observed and unobserved events, and controllable and uncontrollable events. Diagnosis requires that sufficiently extended observations exclude traces without the relevant fault type. The initial development assumes a live language, no unobservable cycles, and that unobservable events cannot be disabled; the paper discusses related limits and illustrates a pump–valve model. This supports comparing experimental policies, while showing why a theorem for a supplied controller/plant model does not establish the origin or calibration of those models. Checked in §§I–II and the construction/discussion, not inferred from the abstract alone. [Primary author-hosted paper](https://web.eecs.umich.edu/~teneket/pubs/ActiveDiagnosisOfDES-1998.pdf).

**Haddad, Lefaucheux and Schwoon: costs already belong to active diagnosis.** Their 2026 paper studies weighted partially observed systems and bounds on accumulated costs or rewards before diagnosis. A belief contains the states compatible with the observed trace; it is conclusively faulty only when all those states are faulty. The model distinguishes controllable actions and imposes conditions allowing continued behavior. These are supplied transition and observation structures, not acquired physical architectures. Its weighted-run objectives are also different from paying installation, memory retention and each experimental operation from one inherited reserve. Checked in §§1–2, especially Definitions 1–10. Thus adding costs alone is not the novelty claim; the specific resource/history connection is what our construction must demonstrate. [*Active Diagnosis with Costs and Rewards*, primary proceedings paper, published 24 August 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol391-concur2026/LIPIcs.CONCUR.2026.37/LIPIcs.CONCUR.2026.37.pdf).

No new empirical results are taken from these comparisons. They establish relevant antecedents and assumption interfaces. The following exact examples and recommendations are our analysis of the repository's proposed continuation.

## 2. The warranted inference is conditional and property-specific

Let \(H\) be the supplied class of complete candidate worlds. A candidate must specify enough to predict each experiment: target transition law, reset behavior, sensor interpretation, relevant initial-state uncertainty, and any productive-consequence channel used for diagnosis. For a paid chronological transcript \(\tau\), define

\[
V(\tau)=\{h\in H:\tau\text{ is permitted by }h\}.
\]

For a diagnostic property \(D\), the exact positive rule is

\[
V(\tau)\neq\varnothing
\quad\text{and}\quad
\forall h\in V(\tau),\ D(h).
\]

If the actual world belongs to \(H\), and the recorded transcript faithfully represents the executed commands and observations under its interpretation, the actual world remains in \(V\). Therefore the conclusion is sound within that contract. The proof is immediate membership preservation; it does not show that \(H\) contains the actual world or that the record is calibrated.

Three different outcomes must remain separate:

- **Agreement on a diagnosis:** all surviving worlds share the stated property, even if other details differ.
- **Agreement on an action:** all surviving worlds warrant a particular action or predict its relevant consequence, although they disagree about the fault. Complete fault identification need not be necessary for that action.
- **An empty compatible set:** at least one candidate-class, observation, stationarity, record or implementation assumption has failed. It is not permission to infer every diagnosis by vacuous universal quantification.

A probabilistic ranking is a different claim. Choosing the most likely diagnosis requires stated likelihoods and priors; it cannot be presented as agreement of every surviving explanation. Likewise, exact elimination under a deterministic observation contract does not automatically extend to noisy measurements.

The underlying full-world set shrinks as valid observations accumulate. Its **minimal fault descriptions** need not simply shrink. For example, initially an observation may establish “sensor fault or reset fault,” leaving sensor-only, reset-only and combined faults. Selecting only the two single-fault explanations discards the combined world. Later evidence requiring both faults would then seem unexplained even though it was in the original model family. Retain all admitted combinations, or explicitly justify the restricted fault class and reconstruct alternatives when revising it.

## 3. Observability of a known system is not identification of its whole interface

An observation can distinguish internal states under a known output law while leaving the output law itself unidentified. More generally, different complete model/sensor pairs can produce the same input–output function. More accurate prediction then need not identify which factor was wrong.

A simple structural-identification example makes the distinction exact. If commanded input \(u\) produces physical response \(x=\alpha u\), and the sensor reports \(y=\beta x\), every possible input identifies only the product \(\alpha\beta\). For any nonzero \(k\), the candidate \((k\alpha,\beta/k)\) gives the identical report for every command. Exact and unlimited input–output data do not identify the two gains separately. A calibrated reference, an independently known gain, or an additional observation can remove this symmetry; the corresponding premise must be declared.

The three-phase apparatus has the same kind of boundary. Let \(x\in\{0,1,2\}\) advance cyclically, let reset set \(x=0\), and write \(c(x)=1\) exactly at phase 2. Compare:

| World | Reported contact | Productive readiness |
|---|---|---|
| Sensor inversion only | \(1-c(x)\) | \(c(x)\) |
| Sensor and productive-readiness inversion | \(1-c(x)\) | \(1-c(x)\) |

Every reset/action/read sequence has the same report in both worlds. This follows by induction: corresponding states start equal, each command preserves their equality, and the observation functions agree. Adaptive policies also receive identical transcripts and therefore cannot choose a separating read-only experiment. The failure is structural, not merely an insufficient finite sample.

A productive transfer probe can separate these worlds at a suitable phase, **if** the learner has an accessible, correctly interpreted receipt of the transfer or resource change. The physical success variable known to a simulator's auditor is not automatically such a receipt. If the receipt channel is also allowed to vary so that it conceals the difference, the augmented experiment can remain ambiguous. The procedure can test a suspect channel against another declared interface; it cannot certify every possible channel simultaneously without further structure.

## 4. Tests must replay the actual history and pay for what they reveal

Once reset is itself in question, a word is no longer automatically an independent membership query from the initial condition. Each candidate must replay the **actual chronological commands**, including attempted resets and accumulated state. Unknown current phase should be represented as uncertainty, not silently filled from the hidden simulator. Cached observations from the earlier faithful-reset regime are not new observations under a defective-reset hypothesis.

The previous acquisition stage retained a model and controller, not necessarily its original table, every query receipt or its present hidden cursor. The continuation must preserve that boundary. Reconstructing deleted evidence from the target's true transition table would provide the very information being diagnosed.

An experiment is useful for discrimination only when admitted candidates predict different accessible outcomes. It is operationally available only when its command, record, computation and retention steps can be funded. A test that would distinguish the worlds with unlimited funds may be unavailable on the inherited history. Conversely, successfully acquiring a diagnosis may consume the final source packet, leaving no further productive use. Report diagnosis, revision, retained capacity and subsequent action separately.

The full-world class should describe the consequences of the test itself. A destructive or resource-consuming probe cannot be analyzed as if every candidate world were restored afterward for free. If a test changes the plant, later compatibility must use the changed candidate states, not rerun the initial experiment counterfactually.

## 5. What would count as a dependency reduction

The meaningful reduction is from a supplied correct fault label to a conclusion constrained by acquired records, with unresolved cases retained. A conventional candidate-filtering implementation given identical hypotheses, observations, action choices and tariffs should reach the same conclusion. Agreement with that comparator is expected; it validates the connection without identifying a novel inference algorithm.

The next construction should make the following distinctions reviewable:

| Item | Acquired in this bridge | Still supplied unless separately established |
|---|---|---|
| Fault attribution | Property common to compatible worlds after paid tests | Initial fault vocabulary and admissible combinations |
| Experimental choice | Selection using disagreements among surviving predictions | Available actions and their execution mechanism |
| Reset assessment | Observed chronological consequences | Candidate reset laws and treatment of hidden initial state |
| Sensor assessment | Relation to separately observed consequences | Consequence receipt's calibration and meaning |
| Continued uncertainty | Recorded disagreement or infeasibility | The class beyond which the method cannot quantify |
| Retained correction | Paid update and subsequent use, if actually completed | Hardware recipe, storage law and update procedure |

Changing the representation of an assumption from one Boolean flag to a finite list of hypotheses makes its alternatives explicit. It does not derive the list's completeness. A misspecified class can leave one surviving but false diagnosis; an out-of-class control is therefore more informative than reporting only successful identification within a perfectly matched family.

## 6. An empirical identification contract, without claiming data

An eventual physical test could use an independently instrumented device with blinded, declared changes to sensor, reset and plant behavior. Record chronological commands, attempted and completed payments, raw sensor outputs and independently measured physical consequences. Give the learner only its declared channels; reserve hidden fault identity and external instrumentation for evaluation. Compare the conventional filter under the same information and prices. Include paired observationally equivalent cases, combined faults, missing candidate laws, exhausted budgets and suspect consequence receipts.

Relevant outcomes would be whether asserted diagnoses are true, whether ambiguities are preserved, which interventions discriminate them, and whether the resulting corrected policy remains affordable. A simulator can check these interfaces synthetically; it cannot establish that real sensors obey them. No such physical measurements or human-learning findings are reported by this note.

**Claim ceiling:** a paid model-comparison procedure can warrant particular diagnoses or actions within an explicit world class, while retaining real ambiguity. It can explain how an acquired abstraction participates in testing some of its own application assumptions. It does not validate the entire candidate class, derive the architecture that performs diagnosis, or turn an analyst's inaccessible success flag into a learned reason.

**Verification scope:** the Reiter and Sampath papers were read from their primary PDFs, including definitions and assumptions; the 2026 cost-diagnosis paper was checked in its primary proceedings text. The gain symmetry and phase-pair indistinguishability are self-contained arguments, not empirical findings. This owned note makes no changes to the shared theory, index or executable continuation.
