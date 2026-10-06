# Revising a model family with newly acquired evidence

6 October 2026. AI-authored continuation of [experimental access](EXPERIMENTAL-ACCESS.md), following [Ren's instruction](../../../sources/15-codex-theory-conversations/2026-10-06-model-family-revision-continuation.md). Named connection: **retained abstraction → broader candidate family → paid reacquisition → revised prediction**, supporting [generative grounding](GENERATIVE-GROUNDING.md).

A learned model can contribute to constructing and selecting a larger model. Our finite construction now performs that transition using actual retained content and resources. It also establishes a precise limitation: evidence compressed for one question need not preserve distinctions needed by a later question. Fresh experiments can repair current prediction without reconstructing the discarded past.

## What memory must preserve

Let \(h\) be a completed experimental history, \(m(h)\) everything the learner can still access, and \(K_C(h)\) the current configurations of a proposed family \(C\) compatible with that history. Exact retrospective revision from memory is possible precisely when

\[
m(h)=m(h')\quad\Longrightarrow\quad K_C(h)=K_C(h').
\]

If two histories leave the same accessible state but require different answers, a decoder receiving that state cannot guarantee both answers. Conversely, if the answer is constant for every set of histories sharing a memory state, a decoder is well defined. This information criterion does not guarantee an effective or affordable decoder. It must include accessible fuel, counters and other possible historical clues, not just the displayed model.

The [proof study](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MODEL-FAMILY-REVISION-MATH.md) gives a concrete failure of old-belief sufficiency. For a three-cycle `001`, readings `00` and `00100`, separated by actions, leave the same current belief. When a four-cycle `0001` is admitted, those histories permit different current configurations. The old belief alone cannot recover which exclusion was earned. The example has different lengths and costs, so it does not claim identical complete resource states in our actual implementation.

With insufficient retained information, the safe retrospective possibility set is the union over all histories consistent with what remains. Computing that union may itself be difficult. The implemented alternative conservatively starts a new current audit, without replaying the inaccessible old transcript. It retains the old diagnosis as a conclusion under its old assumptions, then retires it during paid compaction into the newly selected model. It does not silently certify that diagnosis under a broader family.

## A larger candidate generated from acquired structure

The actual retained model has a three-state cycle with outputs `001`. A supplied edit rule inserts a zero-output state before its learned positive state. It uses the retained transitions and outputs, preserving old state labels. The enlarged cycle reads `0001`; its stored output array is `0010` because the new state has the new label3. This distinction prevents a label change from being mistaken for a physical state change.

The audit admits both models, every current phase and both reading parities:14 behavioral possibilities. It acquires fresh reads separated by actions, updating all compatible configurations until one remains. No trusted reset, current-state label, old audit transcript or new transfer packet is provided.

Six readings separated by five actions suffice to distinguish all14 possibilities. Five can fail: the two cycle families can both produce `00100`. This is a sharp bound for the consecutive-reading protocol, not a claim about every possible experiment. Separate sensor and readiness causes remain unresolved because only their combined effect on readings is tested.

After selection, the learner pays to compact and retain the model, parity and current cursor. It then uses that representation to predict a fresh reading after an action, pays for the observation and comparison, and retains the updated cursor. The final model can support future conditional prediction; the raw new transcript remains external audit data. A paid reusable evidence archive is a further interface, not an implemented result here.

## The actual continuation and its failures

The successful earlier sensor-diagnosis branch leaves about11.470 fuel, no source packet and25 occupied cells. The new procedure inherits those values; it adds eight paid controller cells and stores the generated model and candidates in the existing cartridge.

| Continuation | Result | New cost | Remaining fuel |
|---|---|---:|---:|
| Actual prior apparatus unchanged | Reacquires three-cycle; correct paid forward prediction and retention |10.364|1.106|
| Declared insertion of a new phase | Selects four-cycle; correct paid forward prediction and retention |10.491|0.978|
| Prior sensor-only branch, last packet preserved | Cannot fund first prepared read after installation/generation |2.514|0.177|
| Actual earlier undetected four-cycle error | Cannot fund new installation |0|0.798|

The insertion is a supplied environmental change, preserving the actual old phase; its physical manufacture is not derived or priced by this learner model. What is charged is the learner's response to that change. The unchanged case is an actual continuation without that intervention. The low-fuel historical error is kept separate from the well-funded changed-apparatus case.

An especially informative alternative uses the already installed old diagnoser. The mistaken four-cycle branch can afford one additional reading that empties its old hypothesis set, leaving about0.450 fuel. It has acquired evidence that its former explanation fails, but still cannot install the new revision procedure. Recognizing error and possessing the means to revise it are different capabilities.

Across all14 declared current configurations with the successful branch's inherited reserve, eight complete acquisition, forward use and final retention. Four cannot fund the forward read; two verify that prediction but cannot fund final retention. All14 complete under a separately supplied ample reserve. These are exhaustive finite configurations, not empirical probabilities or new samples from the original history.

The [executable package](../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/revision/README.md) also preserves14 named fixtures, six learned-state renamings and every resource prefix. A two-state alternating process empties the candidate class. A five-state process can either fail during forward use or pass with a wrong accepted four-state model. A late change also defeats the new prediction. An unpaid cursor update can leave the retained cursor behind the physical state. Passing this finite audit never certifies the completeness or continued validity of its own premises.

## What this adds to the theory

The earlier abstraction now contributes to a new candidate structure, and fresh observations determine which candidate is retained and used. The transition does not require the analyst to supply the correct larger model as a verdict. However, the edit grammar, audit schedule, apparatus laws, current-family coverage, stationarity and tariffs remain supplied. The existing inference antecedents are reviewed in the [primary comparator note](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MODEL-FAMILY-REVISION-COMPARATORS.md).

This supports a more precise generative account of mathematical abstraction: a representation preserves distinctions adequate for a specified range of questions; a new range can require reopening distinctions, acquiring evidence and constructing a different representation. The necessity is conditional on the actual information loss and task. It is not a claim that all compression fails or that every new question requires retaining everything.

The next unresolved connection is **consequence-sensitive selection of candidate generators and evidence-retention policies**. Here we supplied the rule proposing an extra phase and the decision to reopen the family. A stronger account must explain how those choices form and are revised, including when preserving a potentially useful distinction competes with present operation. The present learner also discards its new raw observations; their future reusable retention remains unbuilt. Shared concern, wisdom, universal favorable direction and unique metaphysical constitution of mathematical truth are not established by this local result.

Read the [independent review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MODEL-FAMILY-REVISION-REVIEW.md) and [document and source checks](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MODEL-FAMILY-REVISION-CHECKS.json). The bounded current-family reacquisition interface is complete at the declared scope; the unified foundation remains ongoing.
