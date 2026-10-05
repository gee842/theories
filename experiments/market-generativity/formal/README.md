# Checked rational market interface

AI-authored formal elaboration of Ren's market conjecture, 6 October 2026. This is a conditional contribution to [generative grounding](../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md), addressing **consequences → paid correction of the mechanism selecting market practices**. It makes the supplied market mechanism and its viability conditions checkable. It does not derive that mechanism, faithful measurement, institutional authority or protected floors from the generative root.

[MarketGenerativity.lean](MarketGenerativity.lean) currently has **39 checked theorem declarations**. [verification.json](verification.json) records source, checker, compiler and log hashes. The [compiler output](verification/MarketGenerativity.txt) audits every theorem. All depend only on the standard Lean axioms `propext`, `Classical.choice` and `Quot.sound`; the source contains no unchecked proof placeholder, added axiom or native evaluation shortcut. Concrete rational calculations use `decide +kernel`.

## What is proved

| Result | Checked scope |
| --- | --- |
| `profits_difference` | The regenerative practice's private profit advantage is exactly `fine*q + lobby − cost`; no generativity score enters selection. |
| `market_uses_accounting`, `funded_total_accounting` | Revenue equals aggregate distributed private profits, renewal costs, fines, lobbying costs and the funded correction/reserve/overflow uses. These are accounting identities, not an endogenous production theory. |
| `payment_guard`, `no_unfunded_activation`, reserve results | Beginning funds determine whether correction can be bought. Later levy receipts do not retroactively authorize earlier spending; reserve overflow has a separate destination. |
| One-coordinate bound results | Share, influence, accountability, reserve and support inequalities follow from explicit endpoint inequalities and sign assumptions. |
| `rectangle_one_step` | A full state in the supplied rectangle remains in it for every admitted disturbance. Arbitrarily many finitely indexed supports are protected component by component. |
| `rectangle_all_times` | The rectangle is invariant at every natural-number time for every admitted disturbance sequence. This is an unbounded-history theorem, not a finite simulation. |
| `safe_history_never_fails` | A safe history never triggers the designated essential-support failure guard. Failure is absorbing in the guarded model. |
| `example_certificate`, `example_arbitrary_history` | The numerical rectangle below satisfies the generic theorem's premises. |
| `collar_recovers` | Every state in the specified external recovery collar reaches the protected rectangle in one step, for every admitted shock. This is an interval proof, not an endpoint-only sample or a claim that the collar contains the whole rectangle. |
| Failure witnesses | Positive private returns with depletion; capture reversing the private selection gradient; failure of pre-receipt liquidity; rising average supports with an individual shortfall; excluded recipient harm while the market keeps operating; absence of entry from zero renewers. |

The formalized operating map has rational states `x,q,w,B,C[j]`. Correction is an **already authorized** policy installed whenever beginning funds cover its fee. The rule is revised through funded restoration and paid adverse influence; this is not a model of learning which rule to install. `lambda` is the effective response to lobbying expenditure (the paper's supplied `a*lobby`). The model pays the lobby cost in private profit and accounting, but supplies the response coefficient; it does not derive influence technology.

The support guard has an explicit `essential : Fin n → Bool` designation. Safe states protect every represented support, including nonessential recipients. Operating failure depends only on supports designated essential. The checked exclusion example therefore permits market operation while a nonessential recipient's protected floor is breached. This distinguishes instrumental viability from concern; naming someone in the protected vector remains a substantive supplied choice.

The `Option State` guard collapses failed states to `none`; it checks essential floors at both beginning and endpoint. The Python simulator retains the final failed state's quantities and ledger before freezing. The safe-history claims agree on the operating trajectories, but no Python-to-Lean refinement theorem is claimed.

## Exact numerical certificate

The supplied parameters are `P=10`, `levy=fee=1`, `cap=3`, `cost=2`, `fine=4`, `lobby=1/2`, `eta=1/5`, `alpha=1/4`, `beta=1/2`, `mu=1/4`, `lambda=1`. The one represented essential stock has `depreciation=1/10`, `renewal=2`, `damage=1`, `baseline=0`, `floor=5`.

The invariant rectangle is

- `3/4 ≤ x ≤ 1`, `1/2 ≤ q ≤ 1`, `0 ≤ w ≤ 1/4`;
- `1 ≤ B ≤ 3`, `C ≥ 5`;
- adverse accountability error `e ≤ 1/20` and support shock `v ≤ 1/2` at every step.

The generic Lean disturbance condition only imposes upper bounds. Thus it covers the physically intended nonnegative adverse disturbances and also favorable signed inputs. The paper and simulator can impose the additional nonnegativity restriction without weakening the theorem.

At the rectangle's lower corner under maximal adverse disturbance, the exact successor is `x=123/160`, `q=41/80`, `w=1/4`, `B=1`, `C=21/4`. The selection gradient at the accountability floor is `1/2`; the exact positive-gradient threshold is `q>3/8`.

The one-step recovery collar has `x≥4/5`, `q≥49/100`, `w≤13/50` with the same upper/lower physical bounds, reserve and support floors. Every such state under every admitted shock enters the main rectangle. At its adverse accountability/influence corner the bounds are `q'≥2519/5000 > 1/2` and `w'≤49/200 < 1/4`.

The generic certificate uses only assumptions needed for these implications. Physical domain restrictions not required by a particular implication—for example nonnegative stock floors or nonnegative depreciation—remain additional model conditions in the paper. The standard numerical example satisfies them. The share proof uses nonnegative advantage in the safe rectangle and `eta*(fine+lobby-cost)≤1`. It does not formalize domain preservation for arbitrary negative-advantage states.

## Limits and next connection

The real-valued convergence arguments, low-regime attractor claims and eventual stock-failure theorem in the mathematical study are outside this Lean module. The finite harmful-regime witnesses are kernel checked, but they do not constitute a machine-checked low-basin convergence proof. The module also does not establish market calibration, endogenous institution formation, measurement truth, heterogeneous production, entry, participant exit, differentiated productive centers, supply renewal outside the operating guard, or universal favorable direction.

The next unresolved foundational connection is why a faithful, funded, revisable and uncaptured accountability mechanism forms and persists, including the standing of recipients whose harm does not disable exchange. Empirical failure of the supplied causal laws or shock bounds would invalidate application of this certificate to that market while leaving the conditional mathematics intact.

## Reproduce

From the repository root:

```sh
python3 experiments/market-generativity/formal/check.py
```

The checker uses the already installed Lean 4.29.1 binary in the normal elan toolchain location. `MARKET_LEAN` may point to that version elsewhere. It freezes the source bytes, compiles in a fresh temporary directory with `Std` as its only import, rejects warnings and missing/excess dependency audits, records hashes, and removes generated objects. It does not install a compiler or dependencies. Running plain `lean` from another repository directory may select a different toolchain; the checker avoids that ambiguity.

Environment provenance: an initial plain version probe during development caused elan to install the repository-selected Lean 4.34.1. It was not used for these checks; all saved verification pins 4.29.1. The additional global toolchain was left in place to avoid interfering with other concurrent work.
