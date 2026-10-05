# The first reasoning pilot and what it changes

Continuation of Ren's root of wisdom inquiry, 5 October 2026, Asia/Bangkok. This report records a completed synthetic pilot, an elementary formal refinement, and the next research decision. It follows the [initial synthesis](root-of-wisdom-synthesis.md).

This document preserves the first pilot. The subsequent [active-inquiry comparison](active-inquiry-findings.md) has now been completed and also found no observed comparative advantage.

The pilot did not distinguish the proposed six-question discipline from ordinary reasoning or generic reflection. Every condition answered every case correctly. We therefore have no observed comparative advantage to report. This result does not establish equivalence across other tasks, nor does it refute every possible benefit of the discipline. It tells us that this test was insufficient to demonstrate its added value.

A substantive refinement emerged during design: incomplete information can still be enough for the decision at hand. A useful discipline must recognize both when a missing distinction matters and when demanding it would serve no present purpose. “Recognize your limits” should not become indiscriminate skepticism.

## What was tested

We compared three instruction sets: solve carefully; solve carefully and reflect before finalizing; and solve using the six questions from the initial synthesis. Those questions concern warrant and scope, evidence and alternatives, possible correction, purposes and affected people, executable response, and justified stopping.

Each condition received the same twelve newly authored cases, in six matched pairs. One member of each pair required retaining a specified initial conclusion; the other required revising it. The families concerned information sufficiency, model expansion, repair under constraints, the price of information, a stipulated equal-standing rule, and explicit conditions for releasing a commitment. The ethical cases tested application of supplied rules, not the moral truth of those rules.

Each item had four answer choices. Choices stated both a conclusion and a warrant, so correct choice meant selecting the whole valid statement. For example, retaining Cedar because neither release condition was met was correct; retaining Cedar because commitments can never be revised was incorrect, even though both selected Cedar.

The first order was generated with a recorded seed; the second was its reverse. Two fresh participant contexts per condition produced six batches and 72 item responses. The same order was used across conditions within each repetition. No model or reasoning-effort override was requested.

Participants were permitted one read to load their assigned prompt file, then instructed to use no further tools, files, browsing, or delegation. All received the same answer format and a 30-word maximum reason per item. This standardizes permitted input access and visible answer limits; it does not establish equal hidden computation. Inference token counts and sampling seeds were not available or controlled. The saved answer objects do not include full tool traces, so the independent result audit could not certify post-loading tool abstinence from those records alone.

Treatment wording was frozen before the case author’s instances were inspected. The root researcher and a separate reviewer checked the cases and keys before any participant was dispatched. Cases, keys, orders, scoring rules, and final prompts were then hashed. These are local prospective records, not an external preregistration. The evaluator set was deliberately constructed around the discipline's concerns and is not an independent validation set.

## Results

| Condition | Correct complete choices | Unsupported scope endorsements | False rejection of warranted scope | Correct matched pairs |
| --- | ---: | ---: | ---: | ---: |
| Ordinary reasoning | 24 of 24 | 0 of 8 | 0 of 8 | 12 of 12 |
| Generic reflection | 24 of 24 | 0 of 8 | 0 of 8 | 12 of 12 |
| Six-question discipline | 24 of 24 | 0 of 8 | 0 of 8 | 12 of 12 |

Scope denominators contain the four designated sufficiency and model-expansion cases, repeated twice. False rejection counts refer to explicitly keyed invalid rejections on those same eight responses; the denominator is not eight cases all requiring retention. Matched-pair totals contain six pairs in each of two batches.

Each individual batch scored 12 of 12. Within every condition, all twelve revision-required responses and all twelve retention-required responses were correct. There were no missing or invalid choices and no violations of the stated rationale word cap. All participants assigned confidence 100 to every selected option. With all choices correct, the exploratory binary correctness score is zero in every condition; this does not establish general calibration.

The primary endpoint was unsupported endorsement of a scoped claim, not mere action accuracy. In the four eligible cases, the options explicitly assessed whether a certificate or sufficiency claim held. This avoids interpreting a selected action as an unstated claim of completeness. A conservative error-or-missing score was fixed before collection so that silence could not look like success; it also remained zero.

Scoring used the frozen answer key, not an AI judge's rating of sophistication. Seven synthetic checks verified the scorer's handling of perfect, empty, erroneous, duplicated, invalid, missing-reason, and unknown-ID responses. A separate reviewer recounted every answer directly, checked all 72 rationales, and found no conflicts with the keyed reasoning. Rationales contained 17–26 words. Frozen input hashes remained unchanged. All six planned batches were retained. No extra runs were added after the ceiling appeared.

These are six context-level batches, not 72 independent participant replications. No significance test, confidence interval for a general treatment effect, or efficiency claim is warranted by this design. The [complete evidence bundle](reasoning-pilot-data.json) retains cases, keys, instructions, orders, raw answer objects, scores, and prospective records.

## A useful distinction exposed by the cases

The information-sufficiency pair is particularly instructive. Backup costs 5 and prevents loss 12 when two links fail together. Each link's marginal failure probability is one half. Those marginals alone do not determine the probability of simultaneous failure.

In one current model class, the only allowed joint-failure probabilities are 0 and 1/3. Omitting backup then costs either 0 or 4 in expectation. Both are below 5. The exact loss remains unidentified, but omitting backup is optimal in every model in this class.

In the paired class, the only allowed joint-failure probabilities are 0 and 1/2. Omitting backup then costs 0 or 6. Omitting is uniquely best in the first model and backup uniquely best in the second. The shared summary no longer supports a single action optimal in every model. Without an additional decision rule, assigning equal probability to the models would be an invented premise.

All three conditions recognized both cases correctly. The distinction therefore refines the theory but supplies no evidence of a special advantage from our instructions.

## A small formal refinement

Let M be a finite candidate-model class, r:M→Z the represented distinctions, A a finite common action set, and Lₘ(a) the specified expected loss under model m. A policy based only on r can attain each model's own minimum loss exactly when, for every represented value z,

\[
\bigcap_{m:r(m)=z}\operatorname{argmin}_{a\in A} L_m(a)\ne\varnothing.
\]

Necessity: a policy receives the same z for every model in that set, so its chosen action must be optimal for all of them. Sufficiency: choose one common optimum for each z. Randomization cannot repair an empty intersection when exact optimality under every model is required: every action receiving positive probability must itself be optimal under each model. This relies on a common action meaning and ordinary linear expected loss for the lottery.

This is an elementary decision result, not a claim of new mathematics. It says that preserving an optimal decision can require less information than identifying exact losses, answering all questions, or reconstructing the world. A minimax response can still be justified when the intersection is empty, but it answers a different question and need not attain every model-specific optimum.

For example, two indistinguishable models with losses (1,4) and (2,5) for actions a and b agree that a is best. Change the second pair to (5,2), and the shared optimum disappears. Incompleteness itself does not tell us whether current judgment is inadequate. Its relevance depends on the question and criterion.

This sharpens the proposed root: it should help locate the consequential boundary of an understanding, rather than treating every omitted detail as a reason to suspend judgment. That is an interpretation to test, not a definition that guarantees the method's success.

## What this pilot leaves untested

The cases supplied the important quantities, model changes, rights, deadlines, and alternative claims. Participants did not have to discover a new variable, design a measurement, acquire evidence at a real cost, or persuade an institution to implement a correction. The correct distinction was often named in an answer option. Perfect performance may therefore reflect recognition of a well-posed problem rather than the broader capacity we want to investigate.

The paired cases also shared a context and could teach one another. Reversing order balances position partly but does not eliminate that possibility. The cases were concise, synthetic, and selected for relevance to the discipline. Familiarity from training cannot be ruled out even though these particular instances were freshly authored.

Most importantly, a finite pass cannot certify an unrestricted capacity. If an admitted policy class contains two policies that agree on every tested history and differ on an untested one, this test record cannot distinguish their behavior there. A restricted policy class, an exhaustive domain, a structural proof, or justified sampling assumptions could support stronger conclusions. We have not supplied those conditions for a universal claim about wisdom.

That limitation applies to this report itself. Neither the procedure nor its evaluation can claim completeness by having successfully discussed completeness.

## The research decision

The practical-advantage hypothesis remains unsupported by this pilot. We should not count successful completion of cases as successful validation of the special discipline when ordinary reasoning succeeds equally. We also should not redescribe a saturated test as a demonstration that all methods are universally equivalent.

The next test should move from recognizing a supplied distinction to choosing whether and how to seek one. It should compare the discipline with both ordinary reasoning and an explicit established decision procedure, rather than relying only on a weak generic-reflection comparison. The next version must have new cases and a separately frozen protocol; results from this pilot should not be silently pooled with it.

A concrete next environment can use record-based decisions with a fixed inquiry budget. Initial records should omit some context. Available actions can include requesting a specified additional field, checking an observation's origin, running a priced test, acting provisionally, and stopping. Some episodes should make a new distinction valuable; others should make the same inquiry wasteful. The agent must formulate the relevant request without being shown the missing variable as the answer.

The author must specify what the agent can discover: hiding a decisive fact with no accessible route to it creates an information impossibility, not an agent failure. Tests that require the impossible should reward an appropriately scoped conclusion rather than pretend there was an attainable correct action.

Before running that next study, fix hidden worlds, query semantics, costs, deadlines, ethical constraints, termination rules, and scoring. Report useful questions, unnecessary inquiry costs, missed attainable corrections, unwarranted guarantees, and failures of stated constraints separately. Include cases where the right action remains unchanged despite new information. No such interactive comparison was run in this cycle.

The research has become more precise: the promising target is whether a method helps an agent identify when its present understanding is enough, when it needs another distinction, and how to obtain that distinction without losing the ability or opportunity to act.
