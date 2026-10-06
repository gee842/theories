# Paid contact formation changes the derived packet law

6 October 2026. AI-assisted Lean continuation of the [process-law derivation](PROCESS-LAW-DERIVATION.md), at Ren's direction to keep proving the generative core in Lean. This addresses the next derivation that note names: **formation of the contact organization → changed effective inquiry law**.

## The gap it addresses

The derived A/B/C transfer classes are a function of two native coordinates, inversion `tau` and contact `blocked` (`targetOf`). `execute_retains_parameters` in [NativePacketProcess.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/NativePacketProcess.lean) proves that no native command changes either. So the effective inquiry law was fixed for every native history: a blocked port is class C forever. The contact was a supplied, unchangeable coordinate.

## The construction

[ContactFormation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/ContactFormation.lean) adds one operation beside the unchanged port. Formation follows the port's own order:

1. Check capacity and pay the native interface bill.
2. Require one inherited spare component pair.
3. Consume that pair and clear `blocked`.

If no pair remains, the paid bill stays spent and the contact stays blocked. No material is created and no favorable configuration is substituted.

## What is proved

All 26 audited declarations have empty axiom reports.

| Theorem | Content |
|---|---|
| `form_complete_iff` | Formation completes exactly when the native interface is payable and a spare pair exists; the endpoint is fixed. |
| `form_capacity_stops`, `form_funding_stops`, `form_no_spare_spends_charge` | The three failure branches; a missing pair is discovered after payment and the charge is retained. |
| `formed_effects` | Formation changes only `blocked`, fuel, spent and the spare stock; phase, source, inversion, parity and receipt inversion are retained. |
| `failed_formation_retains_contact` | Every failed formation leaves contact, inversion and spare stock unchanged. |
| `native_trace_retains_contact`, `native_history_cannot_leave_C` | Over any native trace, contact and inversion are invariant; a blocked port stays class C. |
| `opening_requires_formation` | In the extended process, any history that opens a blocked contact contains a formation event. |
| `spare_accounting`, `formations_bounded_by_spares` | Final spares plus formations equal initial spares; formations are bounded by the inherited stock. |
| `formation_sets_open_class`, `formation_leaves_class_C`, `formation_changes_profile` | Formation moves the class from C to the open class fixed by `tau`; the response profile changes from (no, no) to exactly one arriving output. |
| `formation_changes_aligned_arrival` | Under the same alignment schedule from the same phase, aligning toward the output that differs from `tau` gives no arrival before formation and an actual arrival after it. |

## What remains supplied

- The spare-pair stock, charging formation at the native interface tariff, and the rule that a formed contact clears `blocked`. These follow the pattern of the [inquiry-revision contact](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/INQUIRY-REVISION.md#the-concrete-change) (one inherited spare pair, one paid operation). That mechanism belongs to a different apparatus, and its exact parts are not claimed to compose with this port.
- `tau`, sensor parity and receipt inversion remain fixed. Formation therefore opens the contact into whichever class `tau` dictates; it does not choose A over B, calibrate receipts, or acquire the phase knowledge alignment uses.
- Formation is not decided by anything inside the model; the theorems hold for any history that includes it. Why a formation event occurs (an acquired reason, selection or accident) is not derived here.
- Changing the effective law is not shown to be good. It changes what inquiry can reach.

## Next derivation

Derive one of the remaining fixed coordinates or the formation rule itself from earlier activity. Two candidates follow directly: the receipt-inversion flag through a paid calibration step, joining the existing acquired-calibration results where their interfaces match; or the spare-pair stock from the port's own retained material, so that formation draws on what earlier activity left rather than an inherited count.

## Reproduce

From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/` with Lean 4.29.1 on `PATH`:

```sh
python3 check_contact_formation.py
```

It checks that the 32 closure sources match the [process-law receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/process-law-verification.json), builds them and the new module fresh in a temporary directory, and requires empty audits, no warnings and no placeholders. The first run passed 33 modules and 625 audits, all empty ([receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/contact-formation-verification.json)). Unlike the earlier checkers, it does not pin a compiler binary path or hash, so it runs on any machine with the pinned version. No existing source, checker or receipt was changed.
