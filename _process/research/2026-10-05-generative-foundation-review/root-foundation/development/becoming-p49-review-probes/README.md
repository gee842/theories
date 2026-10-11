# Seventeenth review: probes

2026-10-11. Lean probes written by the independent reviewer (a Claude Opus 5.5 agent that did not write the work) for the [review of P49, registration and testing](../../BECOMING-P49-REVIEW.md), drafted and titled as P47. **These are review evidence, not registered results.** They are not in the Becoming package and have no checker receipt. The results that P49 moved into the core are cited from the package and its receipt, not from here (the study section on P49 and its handling of the review).

The reviewed module is the first draft of `Becoming.Testing`, SHA-256 `6ba242ddc8a927a97eca3ea38c071ae5a68b40da68e188b8e0ca3abe50f9646a`. Its bytes are kept in the first checker run, [`becoming-checks/20261010T210417.221419Z/Becoming.Testing.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/20261010T210417.221419Z/Becoming.Testing.lean), which passed on the branch then based on `c9c219e3`. The probes import that draft, so they compile against it and not against the module as landed. The review was written in the session scratchpad and is copied here byte for byte; its paths name that scratchpad.

| File | SHA-256 | Content |
|---|---|---|
| `Audit.lean` | `e163478c9d2a5921ba90a7722dc1da740c18bc20b72323254b89f5f198aabf3e` | the reviewer's axiom audit of the reviewed module (127 constants) |
| `ProbeThreshold.lean` | `b9e9b8c2ce2399e71262ceb577a15ca6cb33b1256b150148a31f601abd3bc6cf` | A0–A8: the threshold laws (`threshold_blind_no_webs`, `alike_keeps_difference`, `alike_iff_richer_only`, `alike_while_poorer_supported`, `changed_after_divergence`, `threshold_blind_of_general`), `JointFailure`, `Attracting`, `Exact` |
| `ProbeReach.lean` | `7f8da9f1b915e39986554ff36d06e81e175fd896a1c0ff1e6d084b74f69cadf4` | B1–B5: reach blindness where the members respond (`Balances.alike_within_closed`, `alike_within_registration`), its instances (`withheld_instance`, `ClearingResponsive`), and the closure growing with observation and exchange |
| `ProbeTesting.lean` | `2ad175f9b7faa3b10da43090cf8a520cae38e2684867dadd0b4fee730968ed2a` | C1–C8, D and E: refutation relative to a model, `Stationary`, `ClearingModel`, `ClearingPooled`, the bridge to `Becoming.Inquiry`, and what `finite_reading_credits_consumption` already gives |
| `ProbeStanding.lean` | `0a3ea312c715e501ecac5ba5b9c88d9339fff11ed0aca712d6e8f20a6b0a824a` | F1–F3: `Gauged_own`, `Prey_omits`, `SelfPrey` |
| `ProbeNames.lean` | `b0aa6640026484a13a8962d40d76b3257841c76b7a4f09fa85df3b7b282b4cac` | G: `nomatch` proofs of numeral disequalities bring in `propext`; `by decide` does not |
| `ProbeAudit.lean` | `721b75d96d5eaedb47ae34f937b72e72074bdd6ccc063aa17c79d16c61fe24f7` | the probes' axiom audit |

Each `.out.txt` holds the output of the file of the same name: none of the reviewed module's 127 constants, and none of the 192 probe constants, depends on any axiom.

## Where the probes went

- **A0:** `Flow.subthreshold_alike` no longer assumes that the two webs agree on what `g` requires and needs.
- **A1:** `Flow.difference_kept`.
- **A2:** `Flow.alike_while_supported`, with `Flow.levelsAtLeast_while_alike`.
- **A3:** `Web.registersAlike_iff_of_levelsAtLeast`.
- **A4:** `Flow.difference_changes_after_divergence`.
- **A5:** `Flow.subthreshold_alike`, now proved from A1 and A2.
- **A6, A7:** `JointFailure.difference_kept` and `Attracting.higher_breaks_first`; the probes' `poor`/`rich` became `lower`/`higher`.
- **A8:** `Web.alike_of_threshold` and `Web.observed_level_registers`.
- **B1–B4:** `Flow.alike_within_closed` and `Flow.alike_within_registration`, stated on `Flow.BalancesOn`; `Flow.unregistered_beyond_registration` and `Clearing.alike_for_clearer` are now proved as instances of B1.
- **B5:** `Flow.withinRegistration_mono_obs` and `Flow.withinRegistration_mono_flow`.
- **C1–C8:**
  - `Web.RefutesWithin`, `Web.refutes_iff_refutesWithin_all`, `RefutesWithin.narrow` and `RefutesWithin.not_meets`;
  - `Web.tail_unrefuted`;
  - `Flow.BalancedHistory` with `Flow.refutes_tail_within`;
  - `Stationary.model_error` and `model_refuted`;
  - `Web.RefutesBy` with `Clearing.pooled`;
  - `Web.refutesWithin_iff_conjunction`;
  - `Flow.beyond_needs_model`;
  - `Clearing.model_idles_registration`.
- **D:** `Web.Belief`, `Web.belief_refutes_iff`, `Web.belief_judge_iff`, `belief_judge_later`, `belief_judge_widen` and `Flow.belief_judge_beyond`.
- **E:** `Renewable.no_exact_finite_reading`, now the headline; `sound_not_complete` and `withholds_not_not` are kept here.
- **F1–F3:** `Gauged.own_is_stock`, `Prey.omits`, and `SelfPrey` with `threshold_on_oneself`.
- **G:** `by decide` replaces the root-level `one_ne_two` and `two_ne_three`.

Balance in the general theorems is now assumed only on the conditions registered (`Flow.BalancesOn`), where the probes assume global balance.
