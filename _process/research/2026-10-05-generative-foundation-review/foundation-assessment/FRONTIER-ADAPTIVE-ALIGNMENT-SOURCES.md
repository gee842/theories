# Adaptive alignment: learning, revision and warranted use

6 October 2026. AI-authored targeted primary-source comparison for **formed evaluative influence → warranted revision → effective action**. This deepens selected entries in [the earlier literature assessment](ALIGNMENT-LITERATURE.md); it is not an exhaustive frontier survey, experiment, replication or priority determination. The accepted conditional foundation and its completion conditions remain unchanged.

The important comparison is between what changes, why it changes, and what makes the changed response appropriate. An altered preference estimate, an altered decision rule and a justified correction are different achievements. None becomes unimportant because the other two require separate support.

## Primary evidence and precise reading scope

### COCOA: implemented constitutional adaptation

[Governance in Motion, final EMNLP 2025 paper](https://aclanthology.org/2025.emnlp-main.869.pdf), §§3–4, pp. 17189–17195; Appendix A, pp. 17199–17201; evaluation definitions in Appendix B.

Stage 1 updates an initially empty constitution, fine-tunes the Actor and contrastively trains the Guider. Stage 2 holds the constitution fixed during GRPO. Empty rules do not mean absent normative inputs: the pretrained judge receives helpfulness/harmlessness criteria and normative examples. The evaluation concerns generated responses and benchmark choices. Table 4 separates SFT, RL and prompted rules; §4.7 additionally compares a baseline using the same Qwen judge as reward model. These do not isolate constitutional evolution against a fixed constitution with identical teaching data and update budgets. Results include transfer, mixed subscale effects and worse XSTest performance under the complete system. There is an unresolved implementation discrepancy: §3.3 names GPT-4o-mini as RL judge, whereas Appendix A.3 names Qwen2.5-7B-Instruct for stage 2, consistent with §4.7. No independent reproduction resolves it here.

Reading scope: main methods/results/limitations, Algorithm 1, judge/update/reward prompts and benchmark definitions; no training logs or weights inspected. This is evidence of implemented rule/behavior adaptation, not independent ethical validation of every learned rule.

### CIRL: learning within an already shared objective

[Cooperative Inverse Reinforcement Learning](https://arxiv.org/pdf/1606.03137v4), 2016 work in the expanded 17 February 2024 version; §§3–4, PDF pp. 4–8; Appendix §§6.1–6.3, pp. 9–11.

The definition supplies identical human/robot payoffs, a static reward parameter known to the human, a known reward family and prior, and observation/transition structure. The robot learns about that parameter. Teaching and information-seeking can emerge instrumentally without separate rewards for those activities. The optimal-policy reduction assumes coordinated policies; the paper distinguishes this from solving actual coordination. Navigation experiments compare algorithmically generated expert/instructive demonstrations with MaxEnt IRL over sampled reward functions. They are computational comparisons, not observations of humans acquiring ethical concern.

Reading scope: formal definition, reduction and apprenticeship results, experimental design/results and corresponding appendix definitions/proofs. The revised reward estimate changes action selection, while the commitment to shared reward is supplied. Calling this merely factual learning understates its decision relevance; calling it acquisition of the reason to serve the human overstates its derivation.

### Off-Switch: a conditional incentive, including its adverse regime

[The Off-Switch Game, version 3, 16 June 2017](https://arxiv.org/pdf/1611.08219v3), §§2–5, PDF pp. 2–7.

The robot is designed to maximize human utility but is uncertain about it. Theorem 1 gives nonnegative deference value for the stipulated rational human; strictness requires positive probability on both utility signs. Section 4 already models suboptimal human decisions and regions where bypassing oversight is preferred. Section 5 examines the cost of inflating uncertainty. These are formal and illustrative numerical results, not a learned-agent deployment evaluation.

Reading scope: game, utility/information premises, both theorems, noisy-human analysis and designer tradeoff. This source must not be represented as proving unconditional deference from uncertainty alone, or as overlooking imperfect human behavior.

### Neth: learning and binding deference can diverge

[Off-Switching Not Guaranteed, version 1, 13 February 2025](https://arxiv.org/html/2502.08864v1), §§2–7; the inspected manuscript labels itself forthcoming in *Philosophical Studies*.

Neth examines decision/update assumptions behind information value and the effect of misleading preference signals. With a noisy channel, a Bayesian agent can benefit from retaining access to information yet prefer not to bind its action to the signal. Section 5 explicitly distinguishes automatic implementation of the human response from learning followed by another choice. The paper offers arguments and examples, not an estimate of failure prevalence in deployed AI. Its broad characterization of the original guarantee needs the qualification established immediately above: original §4 already permits noisy-human nondeference.

Reading scope: complete main argument §§1–8, including the information/deference distinction and practical discussion; cited supporting papers and linked notebook were not independently audited. The useful addition here concerns the assumptions connecting receptivity to actual obedience, rather than a refutation of the original conditional theorem.

### Collective Constitutional AI: public input with a controlled training comparison

[Collective Constitutional AI, FAccT 2024, version 1](https://arxiv.org/html/2406.07814v1), §§3–5 and 7; [conference PDF](https://facctconference.org/static/papers24/facct24-94.pdf).

The Public/Standard comparison changes the constitution while retaining training data, hyperparameters, steps, seeds and prompt mixes (§3.4). Public input comes from 1,002 screened U.S. adults; researchers supply seeds, moderation, aggregation, selection and translation. Reported outcomes include lower BBQ bias, broadly similar capabilities and some poorer OpinionQA representativeness. The paper does not directly measure complete constitutional adherence. Conflicting-principle tradeoffs remain with the model; ongoing participant deliberation and wider governance are not implemented by this study.

Reading scope: full main methods, results, limitations and ethics discussion. The conference PDF opened through early methods; a later reader request timed out, so the remaining reading used versioned primary HTML. This deepens the earlier abstract-only entry. It establishes actual public-input/model-output influence, not universal representation, a validated ethical ordering or continuing public control.

## What the local studies actually add

The following are our comparisons and assessments of the local artifacts, not extra findings attributed to those papers.

[Evaluative plasticity](../../../../theories/becoming/chapters/EVALUATIVE-PLASTICITY.md) supplies a particularly explicit finite causal decomposition. Conducting links begin absent; paid paired consequences form their signs; those links later influence recipient choice. Controls preserve factual means knowledge, native learning and costs while removing formation or blocking transmission. Further matched learning can replace a positive link and suppress an affordable, effective service. An ordinary implementation matches exactly. This isolates a contribution of acquired evaluative influence in the specified process; it does not isolate acquisition of an ethical reason, outperform conventional learning, or explain every supplied socket, code, gain and local update law.

[Evaluative grounding](../../../../theories/becoming/chapters/EVALUATIVE-GROUNDING.md) adds an independently argued application: an accountable actor's uncompensated deprivation can supply a repair reason under justified patient, responsibility, remedy, authority and comparison premises. The same acquired connection can mediate that warranted response. The argument also identifies an adverse revision: if those grounds still apply, changing an association does not defeat them. It does not follow that every actual helpful action has been justified, that moral validity was learned, or that the learner recognizes responsibility as responsibility.

That combination is worth retaining as a precise explanatory result. It is not a new general discovery that objectives can be learned, rules can evolve, public input can influence trained behavior, or correction depends on information. Nor does the comparison establish that this particular causal decomposition is absent everywhere else. Its potential contribution is an inspectable connection among formation history, retained factual competence, operational mediation, resource costs and independently assessed application, including the same mechanism's failure regime.

The relevant distinctions are therefore:

| Test | What the present local account can distinguish | What remains unestablished |
|---|---|---|
| Changed means knowledge | Whether an available command is currently supported and effective | General empirical calibration in arbitrary environments |
| Changed evaluative influence | Different choice despite matched acquired facts, native learning and bills | Reliable general acquisition of justified priorities |
| Changed application grounds | Fulfillment, authority, competing claims or a defeated premise can alter the appropriate act | An implemented unified learner that acquires, interprets and enforces all these changes |
| Effective justified response | Conditional agreement of defended application and paid delivered action in the selected history | General social legitimacy or deployed learned-AI reliability |

A self-revision mechanism requires a criterion for accepting revisions, but a fixed judge is not thereby illegitimate, and public agreement is not thereby infallible. The criterion can remain an explicit, defensible normative input. The empirical question is whether its representation and use survive disagreement, changed facts, power incentives and succession. The philosophical question is whether the particular criterion and authority are justified. Treating either question as answered by successful optimization would erase the distinction being investigated.

For a stronger learned-AI claim, the material missing evidence is a joined case: acquired influence, subsequently warranted selective revision, and verified effects under independently justified application conditions. Evaluate preservation of still-valid grounds as well as withdrawal of defeated ones. A process that blindly strengthens a helpful disposition, obeys every signal, or improves only a judge score would not establish this joint claim. This identifies the current empirical ceiling; it adds no new gate to the accepted conditional foundation and prescribes no experiment in this round.

## Provenance and local comparison bindings

All external material above was read on 6 October 2026 through primary publisher/arXiv readers. Versions and pinpoint scopes are recorded above. No original-byte preservation, code execution, independent model training, raw-output reanalysis or complete literature coverage is claimed. Section references identify the inspected primary material; bibliographic references inside those papers are not automatically verified evidence.

Local SHA-256 snapshots used for this comparison:

| File | SHA-256 |
|---|---|
| `EVALUATIVE-PLASTICITY.md` | `f6e4033286f0e23238f0ac38c3893575e6ed728bf5c12d0230c19ad35e07a523` |
| `EVALUATIVE-GROUNDING.md` | `b8d89086044825cfca9ea64edc296fb12d4bce25344af5aede6a24bc41df9d3b` |

These bind the local reading, not future edits. See the companion [goal/authority comparison](FRONTIER-GOAL-AUTHORITY-COMPARISON.md) for fulfillment and effect-boundary distinctions. No canonical document or shared index was edited in this source-review task.
