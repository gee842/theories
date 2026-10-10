# Continuation-grounding review probes (W8 evidence)

2026-10-10. Lean probes written by the independent reviewer (a Claude Opus 5.5 agent that did not write the work) for the [review of W1–W5](../../CONTINUATION-GROUNDING-REVIEW.md), commit `1f6f375f`. **These are review evidence, not registered results.** They are not in the Becoming package and have no checker receipt. The results that W8 moved into the core are cited from the package and its receipt, not from here (study §47.1–47.4).

| File | SHA-256 | Content |
|---|---|---|
| `Probe.lean` | `0be5ffcf571d01dbd0593f6cd531324821a7c34471b4bb37e4530bb4ef639da6` | probes R1–R9: 17 declarations |
| `ProbeAudit.lean` | `b293e30ebc882ed353f37d8ac53a8d31ef1f1b91419245e9cc6f3a589b12e7d2` | the same probes followed by `#print axioms` for 11 theorems |
| `Probe2.lean` | `7ac25367f9c609bd43f0db4639e902d7418de6df848e8ca3b9d4f4a0d128f6da` | probe R10 (`keeper_active_not_living`) and its `#print axioms` |

`probe-audit.log` (SHA-256 `5c41c6db4f5cdbb54fa389c206a9b17430b51dd278f31d8bde3250fb4b189123`) holds the rerun output. All three files compile with exit code 0, and all 12 printed declarations report no axioms. `lean-version.log` records the toolchain (Lean 4.29.1).

The rerun compiled `Becoming.Continuation` and `Becoming.Standpoints` from the bytes of commit `1f6f375f`, together with the rest of the core built from commit `7f69f455`; the reviewed modules import only from that build. The probes refer to declarations that W8 later changed (`Totalizer.valuation`, `Apart.standpoint_neutrality_is_needed`), so they compile against `1f6f375f` and not against the W8 package.

## What the probes show, and where W8 took them

- **R1 `own_transmission_of_selfGood`:** S0 at every position gives transmission into each own region. In the core this is `Valuation.own_transmission` (finding C1).
- **R2 `significant_of_selfGood_transmits`, `apart_fails_transmission`:** a second completion, and `Apart` failing N_rel. In the core these are `Valuation.significant_of_transmits` and a conjunct of `Apart.not_enough` (C2).
- **R3 `significant_iff_held_own`:** on held lives, sharing restricted to each position's own region already suffices. This is kept here as evidence and was not moved.
- **R4 `Tot.out_of_own_fails`, R5 `Tot.stronger`:** transmission out of own regions along formed relations fails, and a witness closed along dependence exists. In the core these are the strengthened `Totalizer.center_not_derived` with `Flow.FedBy` and `Totalizer.fedBy_sun`; the core's `FedBy` also requires the feeding formation to take part (C1).
- **R6 `Tot.supply_not_cut_living_on`:** in the core this is `Totalizer.supply_not_cut_living_on` (C8).
- **R7 `lone_only_sun`, R8 `mortal_joint_excess`, R9 `exceeding_by_definition`:** evidence for C3, C6 and C7, handled by rewording.
- **R10 `keeper_active_not_living`:** in the core this is `Totalizer.keeper_not_living` (C13).

## Reproduction

Build the core at `7f69f455` with `../continuation-grounding-sketch/build_core.py`, then compile the two reviewed modules from `1f6f375f` and the probes:

```sh
python3 -I ../continuation-grounding-sketch/build_core.py <work>   # set CORE_COMMIT to 7f69f455
git show 1f6f375f:experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Continuation.lean > <work>/Becoming/Continuation.lean
git show 1f6f375f:experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Standpoints.lean > <work>/Becoming/Standpoints.lean
cd <work> && export LEAN_PATH=$PWD && L=~/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean
$L -o Becoming/Continuation.olean Becoming/Continuation.lean && $L -o Becoming/Standpoints.olean Becoming/Standpoints.lean
$L <this dir>/Probe.lean && $L <this dir>/ProbeAudit.lean && $L <this dir>/Probe2.lean
```
