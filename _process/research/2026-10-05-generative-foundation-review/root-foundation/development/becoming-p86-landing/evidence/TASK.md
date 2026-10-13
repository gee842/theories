# P86: feeding across steps — delayed conveyance and redundant feeders

Read `/private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/AGENT-COMMON.md` first and follow it. Your scratch directory is `/private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/p86/`.

Open items named in the chapter's section 8 (continuation) and in the next deltas of the records `feeding-closure` and `consumption-ends-with-feeders` (`theories/becoming/results/records/*.json`):
- "whether delayed conveyance through conditions counts as feeding (P40's feeding closure counts giving at a common step only)";
- "return under redundant feeders and reserves".

Relevant core: `Becoming/Interdependence.lean` (`Flow.FedBy`, `Flow.FedClosed`, `Flow.WithinFeeding`, the feeding closure and its theorems, `unfed_consumption_ends_at`, `consumption_ends_with_feeders_at`); `Becoming/Continuation.lean` (`Flow.Conveys`, `FedFromBeyond`); `Becoming/Reserve.lean` (reserves defer ending); `Becoming/Flow.lean` (`BalancesOn`, `GiversSupported`).

Task, in this order, stopping where the honest answer is a boundary:
1. **Delayed feeding.** Define feeding through a condition across steps: a formation giving to a condition at step `s` feeds the continuation of a formation requiring that condition at a later step `t`, where what was given can still stand there (state exactly what carrying from `s` to `t` needs; balance on the condition over the stretch is the natural candidate). Define the delayed feeding closure in the style of `WithinFeeding`. Prove that it contains the same-step closure, give a witness where it is strictly larger (a formation fed only through a held reserve), and prove the analogue of the closure theorem: nothing outside the delayed closure gives, at any step, to a condition carried to a requirement of a member. Say whether same-step feeding is the delayed form at delay zero, as an equivalence.
2. **Redundant feeders.** `consumption_ends_with_feeders_at` says that where every feeder of a condition is unsupported, a formation taking from it ends within its level. State and prove the converse direction's exact condition under balance: consumption can continue exactly where, at each step, supported givers give at least what is drawn beyond what stands (or the precise local form you find), so losing one of several feeders does not end it while another suffices; give a witness with two feeders where removing either keeps the consumer active and removing both ends it. Connect with reserves: a reserve defers the end by at most its level (reuse `Reserve` where it already says this; do not reprove it).

New core module (suggested name `Becoming.Feeding`, or a better precise name); no change to existing modules unless necessary. Report as AGENT-COMMON.md says.
