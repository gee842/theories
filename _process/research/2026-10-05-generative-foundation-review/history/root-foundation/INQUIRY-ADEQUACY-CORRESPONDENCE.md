# Checked inquiry adequacy / 求知适切性的实查对应

8 October 2026. Third-round mathematical component, supporting [projection and risk](KNOWLEDGE-PROJECTION-AND-RISK.md) and [inquiry priorities](INQUIRY-PRIORITIES-AND-G0.md). **Eight theorems and thirteen explicit declarations pass Lean 4.29.1 compilation and dependency audit.** [Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/InquiryAdequacy.lean) / [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/check_inquiry_adequacy.py) / [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/inquiry-adequacy-verification.json).

## Representation and exact claims

`H` represents whole local histories; `domain` selects admitted histories; `evidence` describes the available distinction; `policy` maps that distinction to a response. `admissible h a` is a supplied response requirement. It can encode a specified operational condition or an independently justified practical requirement, but the formal predicate does not establish either interpretation. These roles differentiate within the modeled activity; they are not independent ontological realms.

`Adequate` means the policy meets the supplied requirement for every admitted history. It is an exact guarantee, stronger than many defensible decisions under uncertainty. No predicate defines knowledge, ethical goodness or G0. No probability or welfare weight is hidden in the definition.

| Theorem | Checked content | Supplied premise or correspondence |
|---|---|---|
| `adequate_policy_iff_common_choice` | An adequate total policy exists exactly when each evidence value permits one response meeting the requirements of all admitted histories producing that evidence. | Evidence, domain and requirements are given. Values never produced still require an action to make the policy total; the forward and converse use the same total-policy convention. |
| `recoverable_evidence_preserves_adequacy` | An adequate policy lifts through a faithful recovery of its old evidence from new evidence. | The same domain and requirement relation remain in force. This does not show that obtaining new evidence leaves them unchanged. |
| `blind_target_not_identifiable` | A constant observation cannot identify both Boolean cases. | Both cases are admitted; the target is the specified Boolean. |
| `protection_without_identification` | A common stipulated protective response meets the requirement in both cases without identifying the case. | The common response actually fits either case and is taken at elapsed time zero. |
| `blind_targeted_response_impossible` | No constant-evidence policy guarantees the case-specific response across both cases. | This task permits only case-specific responses, not the common protective alternative. |
| `truthful_probe_adequate_iff_timely` | Given direct truthful evidence, a case-specific adequate policy exists exactly when elapsed inquiry time is within the deadline. | Probe truth, elapsed time and the deadline law are stipulated. |
| `late_probe_loses_even_common_protection` | After the deadline, even perfect case information cannot supply an adequate response under the protective requirement. | The inquiry has changed the elapsed-time condition; ignoring the report does not reverse that change. |
| `probe_enables_previously_unavailable_targeted_response` | A timely truthful probe makes a guaranteed case-specific response possible where blind evidence did not. | This is a conjunction of the preceding constructive and impossibility results, not a new empirical mechanism. |

## The finite example and its limits

The Boolean histories distinguish two stipulated cases. `Protective` permits either a common response (`none`) or the matching case-specific response (`some h`), provided the response occurs on time. `Targeted` permits only the matching Boolean response on time. Thus an unknown fact can be irrelevant to one task's guaranteed fulfillment and decisive for another's. A truthful probe supplies the case but consumes the specified elapsed time.

The adverse comparison does not refute the evidence-refinement theorem. It changes the response relation through elapsed time, violating that theorem's fixed-requirement premise. The whole inquiry is therefore different from adding a costless signal to an unchanged decision problem. This is a familiar information-and-feasibility distinction, not a priority or novelty claim over established decision theory.

The construction does not derive the probe, acquire its calibration, or compose a new physical history with the repository's existing paid apparatus. It formalizes the interface that an application must satisfy. Actual durations, deadlines, case coverage, access, cognitive uptake, permissions and costs require correspondence evidence. The common protective response is not a universal prescription to shut down, intervene or ignore uncertainty.

## Dependencies and checking

The module imports only `Std`. The checker freezes source, checker, compiler hash, toolchain, audit and logs, compiles in a fresh temporary directory and audits every explicit declaration. It rejects `sorry`, `admit`, added `axiom` declarations, unsafe code and native proof shortcuts. The abstract policy-existence converse uses classical choice; its named foundational dependencies are disclosed by the receipt. Other checked implications are not thereby independent of their stated mathematical hypotheses.

The successful snapshot is [20261007T220858.910861Z](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/inquiry-adequacy-checks/20261007T220858.910861Z/verification.json). UTC 7 October corresponds to local 8 October. The earlier twenty-theorem knowledge package remains unchanged and is not counted among these eight new theorems. Published results by Good or Pearl and Bareinboim are source comparisons, not proofs certified by this package.

## Philosophical and normative boundary

The criterion makes an actual distinction between identifying a fact and having a response that fits the remaining cases. It does not select the relevant domain, justify the response requirements or prove the rightness of caution. A robust guarantee can be unavailable even where a risky decision is justified. G0 and J1–J4 supply separately defended normative premises in the accompanying argument; encoding those premises would not establish their warrant.

The contribution is a checked correspondence component for situated inquiry. General induction, cognitive possession, empirical transportability, ethical weights, institutional authority and unique necessity of the theory are not proved.
