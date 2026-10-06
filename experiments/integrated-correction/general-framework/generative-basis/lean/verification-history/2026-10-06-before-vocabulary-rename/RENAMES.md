# Vocabulary renames, 6 October 2026

At [Ren's direction](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md), market and exchange names were replaced with names for what the activity does. Only names changed: every audited declaration reports the same axioms as before ([check.py](check.py), [receipt.json](receipt.json): 48 modules, 963 audits, 48 renamed declarations, no mismatch).

## Core vocabulary

| Old | New | Meaning |
|---|---|---|
| `fuel`, `reserve` | `held` | what remains available to become further activity (存) |
| `spent`, `demand` | `enacted` | what has become, or an event makes into, activity (化) |
| `income`, `credit` | `arrived` | what comes in through actual contact (来) |
| `wasted` | `dissipated` | what left activity without becoming it |
| `AccountLaw` | `SustainLaw` | U1: `held t + enacted s a t ≤ held s + arrived s a t` |

## Conditional package (`conditional/ResourceContinuation.lean`, `RenewalExamples.lean`)

| Old | New |
|---|---|
| `SupportTrace.spent` / `.received` | `enactedTotal` / `arrivedTotal` |
| `credited` | `arrivalEvent` |
| `account_law_pullback` | `sustain_law_pullback` |
| `trace_has_support_account` | `trace_has_support_totals` |
| `repeat_accounted_cycle` | `repeat_supported_cycle` |
| `support_trace_balance` | `support_trace_bound` (U2) |
| `support_cycle_covers_demand` | `support_cycle_arrival_covers_enactment` |
| `support_trace_unit_demand` | `support_trace_unit_enactment` |
| `amount_le_cap_times_credited` | `amount_le_cap_times_arrival_events` |
| `support_trace_credit_cap` | `support_trace_arrival_cap` |
| `execution_interval_balance` | `execution_interval_bound` |
| `componentwise_execution_balance` | `componentwise_execution_bound` |
| `unbounded_demand_requires_unbounded_credit` | `unbounded_enactment_requires_unbounded_arrival` |
| `infinite_unit_execution_credit_window` | `infinite_unit_execution_arrival_window` |
| `infinite_unit_execution_unbounded_credit` | `infinite_unit_execution_unbounded_arrival` |
| `renewal_account_law`, `insufficient_account_law`, `free_account_law`, `bulk_account_law` | `renewal_sustain_law`, `insufficient_sustain_law`, `free_sustain_law`, `bulk_sustain_law` |
| `renewal_unit_demand` / `renewal_credit_cap` | `renewal_unit_enactment` / `renewal_arrival_cap` |
| `insufficientDemand` / `insufficientCredit` | `insufficientEnacted` / `insufficientArrived` |
| `insufficient_credit_is_always_positive` | `insufficient_arrival_is_always_positive` |
| `free_process_has_no_unit_demand` | `free_process_has_no_unit_enactment` |
| `bulk_has_no_uniform_credit_cap` | `bulk_has_no_uniform_arrival_cap` |
| `bulk_consumes_reserve` | `bulk_consumes_held` |
| phase `.spent` (RenewalExamples) | `.depleted` |
| local `budget` (SupportNecessity) | `withinLife` |

## Native packet port (`inquiry-root/sufficiency/NativePacketProcess.lean`, `PacketLawDerivation.lean`)

| Old | New |
|---|---|
| fields `fuel`, `spent`, `income`, `wasted` | `held`, `enacted`, `arrived`, `dissipated` |
| `bill` (amount a stage needs) | `draw` |
| `Payable` | `Supportable` |
| `debit` | `enact` (moves `draw` from held to enacted) |
| `charge` | `support` |
| `Payment` = `.paid s` / `.capacity` / `.funding` | `Support` = `.sustained s` / `.capacity` / `.insufficient` |
| `gain` | `arrivalAmount` |
| failures `interfaceFunding` / `receiptFunding` | `interfaceInsufficient` / `receiptInsufficient` |
| `charge_paid`, `charge_capacity`, `charge_funding`, `charge_paid_iff` | `support_sustained`, `support_capacity`, `support_insufficient`, `support_sustained_iff` |
| `interface_funding_stops` | `interface_insufficient_stops` |
| `probe_receipt_funding_stops` | `probe_receipt_insufficient_stops` |
| `rotation_fuel` | `rotation_held` |
| `rotations_ready_implies_budget` / `rotations_ready_from_budget` | `rotations_ready_implies_held_bound` / `rotations_ready_from_held_bound` |
| hypotheses `funding` (enough / not enough), `payable`, `payment` | `covered` / `short`, `supportable`, `outcome` |

## NativePortContinuation

| Old | New |
|---|---|
| `debit_continues`, `debit_lowers_potential` | `enact_continues`, `enact_lowers_potential` |
| `bill_positive` | `draw_positive` |
| `paid_continues` | `supported_continues` |
| `step_balance_exact` | `step_sustained_exact` |
| `port_account_law` | `port_sustain_law` |

## Contact-formation, phase-cycle and valuation modules (renamed when merged with main)

`ContactFormation`, `FormationClosure`, `AcquiredContact`, `PhaseCycleDerivation` and `PortValuation` reached main while the rename was under way. On merge they take the native-port names above, plus:

| Old | New |
|---|---|
| `form_reserve_stops` | `form_insufficient_stops` |
| `FormFailure.interfaceReserve` | `FormFailure.interfaceInsufficient` |
| `spare_accounting` | `spare_count` |
| `completed_native_wasted_monotone` | `completed_native_dissipated_monotone` |
| `pair_ledger` | `pair_record` |
| hypothesis `noWaste` | `noDissipation` |

## Kept on purpose

- The Python originals (`diagnosis.py` and its port) keep `fuel`, `spent`, `income`; the correspondence checker maps them (`LEAN_FIELD`).
- `receipt` names an observation of the completed conversion, not a payment.
- `spent` in `OnePacketQuestions` is the macro packet state, not a quantity.
- Downstream studies that only import these laws (`PatientConcern`, `ControllerRevision`, `FormationSupport`, `SupportedRevision`) had the imported names updated; their own local vocabulary is unchanged.
- The 32-module core closure (for example `Depletion.reserve`, `BoundaryModels.FuelState`, `CompletionApplicability.queryCredit`) and the renewal package's own `reserve`/`demand` (`conditional/renewal/RenewalAccounting.lean`) are not renamed in this round.
