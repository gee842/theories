# Pre-dispatch scorer and interface audit

Audited 2026-10-05 before participant dispatch. Inspected final `score.py`, the updated `apply_saved_round` raw-response boundary, pre-run amendments, prompt preparation, run manifest, all six prepared prompts, and their initial states. No runner, scorer, cases, prompts, or run states were modified. All fixtures ran in memory; the parsing-boundary test mocked filesystem reads and writes.

**Verdict: no substantive blocker found in the inspected snapshot.** The malformed full-response JSON issue from the preceding engine audit is resolved. The scorer preserves the intended distinction between submitted-command validity and the effective fallback's decision cost.

## Fixtures passed

| Fixture | Independently expected and observed result |
|---|---|
| All-optimal six-episode batch | 6/6 initial choices, 3/3 matched pairs, 11/11 visited choices; 5 queries; query fees 5; action fees 5; summed terminal elapsed times 13; realized total loss 26; all initial/local/terminal excess sums 0. |
| A04 blank reason despite optimal fallback | Initial success falls to 5/6; invalid and empty-reason counts each 1; matched pairs 2/3; cost gaps remain 0 because the forced fallback is itself optimal. |
| A05 unnecessary status query followed by inferior option_b | Initial gap 1/2; terminal excess 7/2; local gap sum 4; one strict unnecessary continuation; query fees 11/2; realized total 55/2. |
| A01 repeated query after paying for its first query | Invalid repetition forces fallback; the first fee remains charged; total query fees 4, action fees 4, realized total 32, and local gap sum 6 across the batch. |
| A04 reason over 35 words | Command executes and remains optimal; cap violation count 1, invalid count 0. |
| Malformed full raw JSON response | Exact raw fenced text fails parsing; one parse error recorded; all six open episodes receive invalid fallback; no queries or query feedback; realized loss 52. Raw response is not rewritten or repaired. |

The ideal realized loss of 26 is specific to the selected private worlds. It is not the initial Bayes value sum, which is 28, and should not replace the expected-choice score. The scoring fields correctly keep those quantities separate.

## Prompt and amendment checks

Each of the six prompts exactly equals its condition's treatment text, the identical interface clarification, shared public rules, and public case statements in the manifest's order. No private-world selection, private seed, oracle answer, or audit result is introduced by preparation. Initial states exactly match `initialize` and contain no participant outcomes. The three conditions share each repetition's order; repetition two reverses repetition one.

The pre-run amendment accurately records implemented policies: exact raw-response parsing without fence stripping or retry; blank/missing/non-string reasons invalidate; over-limit reasons execute with a violation count; extra unknown/closed IDs are logged and ignored; missing or duplicate required IDs force that episode's fallback. Invalid commands fail the primary endpoint even when their forced action is optimal. Independent case draws and shared realized worlds across conditions are recorded before execution.

## Interpretation requirements retained

The aggregate scorer does not claim independent episode-level replications or inferential significance. Report per-case and per-batch outcomes from retained states alongside condition totals. Initial gaps are common-initial-state comparisons; summed visited gaps remain trajectory-local diagnostics. Summed elapsed times are descriptive episode-resource totals, not wall-clock model runtime. Strict unnecessary continuation is evaluated before the query's answer using the public-belief continuation value.

## Audited hashes

```text
score.py                a01297689f54ae49ac5c6fd7ccd1de676e125a364bb1585d922410f660187395
engine.py               6733cc3b374dc1e9e74879db420824e9dd46d0feee81d50b50ed5a6b19bc9fe7
pre-run-amendments.json  7423c915ba96412ee75fc76b45bcd7acd49cf583913f3c888d29597f4296c3c3
prepare.py              c4b585580c90d054be7b7a10f314186beb571a31a41f616eb6a94468daf11f71
run-manifest.json       38a3a605bb19973cbe45aad74eda79ec028ec50a03d3fc0b0ebb9c21f08d969a
```
