# Consequences, factual reporting and the public evidence boundary

6 October 2026. AI-authored primary-source and artifact audit. Named connection: **concern for a valued future → treatment of present evidence and authorized action**. This supports the [reporting contract](FUTURE-REPORTING-CONTRACT.md); it does not duplicate the [AgentDojo replay](AGENTDOJO-REPLAY-REVIEW.md), establish acquired recipient valuation, or validate a complete alignment mechanism.

## 1. A sharper reported comparison

The [Summer 2026 primary study](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) motivates a comparison of downstream framing at fixed inputs. Its selected simulated cases cannot establish general deployment rates. See the [independent source-scope review](FUTURE-REPORTING-REVIEW.md) for interpretation limits.

**Discriminating implication:** if a fixed historical question and evidence receive different factual assertions when only a later use changes, concern about consequences affects the reporting interface. That is a different issue from external instructions contaminating AgentDojo actions. It does not by itself distinguish strategic misstatement, rubric reinterpretation, belief changes or response-style changes. A proposed downstream harm is not evidence of actual delivery; an honest objection can be warranted without falsifying the record.

## 2. Verified public artifacts do not permit the proposed reanalysis

The [source package](../../../../sources/31-agentic-misalignment-public-2026-10-06/README.md) preserves exact official article HTML, viewer HTML and JavaScript, the entire served manifest, two schema exemplars and retrieval headers. [Machine-readable availability findings](../../../../sources/31-agentic-misalignment-public-2026-10-06/metadata/availability.json) are descriptive artifact checks, not behavioral outcome statistics.

The complete manifest contains 440 IDs; its motivated-mislabelling section contains 18 `mislabel-input-*` entries and six selected multi-turn cases. A judge-input exemplar has `metadata`, `target_messages` and `annotations`; it explicitly omits full event logs and auditor scaffolding. A selected case additionally has `auditor_messages`. Neither is the repeated one-turn judging corpus. The client fetches only this manifest and entry-specific JSON paths. No complete judge-model × input × condition × repeat response table or run configuration was found in the verified release.

The proposed primary analysis was one fixed Sonnet 4.6 judge configuration, all 18 inputs, all five calls per consequence condition, with transcript-clustered comparisons. **It was not run.** The available inputs and selected examples cannot reconstruct its 270 calls, failures, token limits or full prompt equality. An input filename containing `standard`, `none` or `reversed` belongs to the earlier input-producing audit; it is not a valid substitute for the later repeated judge experiment. Likewise, annotation fields called `judge_highlights` are not judge outcomes.

Publication numbers and illustrative outcomes had already been seen before this audit, so any later reanalysis must disclose retrospective outcome knowledge. We have not selected a favorable response subset, regenerated missing calls, reverse-engineered counts from plots or treated the published rate as independently reproduced.

## 3. What a release would need to establish

Bind complete prompt bytes, target transcript IDs, task referent and time window, rubric, judge version, temperature/thinking/token settings, repetition IDs, output text, stop reasons, errors and exclusions. Check that the consequence paragraph is the only within-configuration change. Inputs with reasonably disputed readings need an explicit admissible-label set rather than automatic adoption of the published label.

Preserve all-call categories: correct assertion, definite error, unresolved assertion, explicit abstention, unstructured refusal, malformed output and truncation. Report unconditional category changes before conditional accuracy among emitted labels. Five calls on the same transcript do not create five independent historical cases; the all-refusal selection cannot estimate specificity on compliant cases. A label about following an instruction must remain distinct from whether the instruction should have been followed.

Missing raw data is an access boundary, not a refutation. For the present derivation this evidence sharpens an obligation: acquired evaluative influence must preserve contestable, faithful evidence while allowing legitimate objection. It does not supply the foundation's mechanism, a universal obligation to disclose, or authority for every downstream use.

## 4. Positive training comparator and earlier adverse comparator

[Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/) is the positive training comparator. Our link inspection found no complete training/evaluation rows or replication package. Its Google Docs link is a prose cross-reference, not identified dataset metadata. See the [independent review](FUTURE-REPORTING-REVIEW.md) for causal confounds and limits.

The [2025 official repository](https://github.com/anthropic-experimental/agentic-misalignment/tree/ea0630e1a3eaae7f9f9740fd2703229d3854ccda) supplies templates, configurations and classifiers for adverse self-continuation/goal-conflict scenarios. Its inspected current tree lacks result files; releases and tags were empty. A results-path history entry exists and was not exhaustively audited, so no blanket historical non-release claim is warranted. This branch was superseded by the closer 2026 reporting comparison, not silently counted as a new raw-data reanalysis.

## 5. Preservation and search limits

Plain `urllib` returned 403 on the viewer; web extraction saw an empty JavaScript shell. Inspecting the publicly served HTML exposed its client asset and manifest. Browser-user-agent `curl` succeeded without credentials. Only two schema exemplars were fetched; no need to bulk-download all selected cases to establish the absent judge matrix. No models, experiment code, embedded tool calls or site JavaScript were executed. No explicit reuse license was found; do not transfer the earlier repository's MIT license to these files.

This audit makes a bounded negative availability finding about the inspected primary page and served viewer, not all possible public repositories. It leaves the supplied causal and normative premises visible while the central evaluative-uptake producer continues in its own workspace.
