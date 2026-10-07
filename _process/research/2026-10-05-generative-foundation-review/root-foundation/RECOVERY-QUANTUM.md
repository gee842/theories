# The recovery rate is the dissipation of one failed conversion

7 October 2026. AI-assisted continuation of the [contact-formation track](CONTACT-FORMATION-LAW.md), which listed "the recovery rate of ten dissipated units per spare pair" as supplied. It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md): recovery is examined as one operation of the same activity whose failed conversions it recovers, not as an exchange with something outside it.

**Formal status:** [RecoveryQuantum.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/RecoveryQuantum.lean), 30 declarations, every axiom report empty. It is checked by [check_stock_derivation.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_stock_derivation.py) together with the formation-draw and starting-stock modules. No existing module is changed.

## Transition addressed

Recorded failed conversion → spare pair. The question is whether the rate at which dissipation becomes a pair is fixed by the native activity or chosen.

## What is derived

| Result | Lean statement |
|---|---|
| Every native conversion lowers the source coordinate by ten and raises exactly one of the arrived and dissipated records by ten. A failed conversion dissipates exactly ten | `conversion_settles_quantum`, `failed_conversion_dissipates_quantum` |
| Every completed native command raises the dissipated record by ten if it is a failed conversion, otherwise by zero | `native_dissipation_step`, `failure_record_step` |
| Along every closure history the dissipated record stays a whole number `k` of failed conversions, and recovered pairs never exceed `k` | `trace_failure_record` |
| Recovery stated at any rate `r`; the supplied recovery is `r = 10` | `recoverAt`, `recoverAt_ten`, `runAt_ten` |
| **One pair per failed conversion fixes the rate.** Each recovered pair is backed by a distinct recorded failed conversion, and each unrecovered failed conversion can be recovered, exactly when `r = 10` | `rate_determined` |
| Rate 11: the one failed conversion of the closure history cannot be recovered and the history stops | `coarser_rate_strands_failure` |
| Rate 9: nine failed conversions yield ten pairs | `finer_rate_overcounts` |

`rate_determined` holds for every natural rate. The two halves are separately necessary: a rate above ten leaves a recorded failure unrecoverable, a rate below ten lets some pair stand for no distinct failure.

## Status of the input

**Derived, relative to a stated claim.** The number ten is no longer a separate parameter of recovery. It is the dissipation quantum of the native conversion, and the requirement that one recovered pair corresponds to one recorded failed conversion forces it. Without that requirement the port is consistent with every rate; the two executed countercases show what the neighbouring rates change.

Still not derived here: why the native conversion moves ten units (inherited from the apparatus source, `diagnosis.py`, and bound by the checker), and why a pair should correspond to one failure rather than to a fixed number of failures. The latter is the claim under which the rate is determined; the theorem shows it is equivalent to `r = 10`, so it can be tested rather than assumed.

## What would change the account

A retained relation in which several failed conversions jointly form one pair. The theorem would then fix the rate at that multiple of ten instead, and the closure history's single failure would no longer open the contact.

## Reproduce

From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/` with Lean 4.29.1 on `PATH`: `python3 check_stock_derivation.py`.
