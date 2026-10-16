# Checked rational market interface

AI-authored formal elaboration of Ren's market conjecture, 6 October 2026. This is a conditional contribution to [generative grounding](../../../theories/becoming/history/GENERATIVE-GROUNDING.md), addressing **consequences → paid correction of the mechanism selecting market practices**. It makes the supplied market mechanism and its viability conditions checkable. It does not derive that mechanism, faithful measurement, institutional authority or protected floors from the generative root.

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

<a id="checked-regime-boundary"></a>
## Checked regime boundary, 8 October 2026

[RegimeBoundary.lean](RegimeBoundary.lean) extends the actual imported market law in response to Ren's request for degeneration boundaries and transition conditions. It adds **19 checked theorems / 27 declaration audits**; **39 imported theorem audits** are separately rebuilt. Run the linked [check_boundary.py](check_boundary.py) with Python from the repository root. The [receipt](boundary-verification.json), [frozen sources and audit](boundary-verification/BoundaryAudit.lean) and logs preserve the checked dependency closure.

Write M = alpha*(1-theta) - beta*lambda*theta. For rational parameters with alpha>0, beta≥0, alpha+beta≤1, 0≤lambda≤1 and 0<theta<1:

| Theorem | Exact result |
|---|---|
| exact_floor_boundary | With correction executed and zero adverse error, every q in [theta,1] and w in [0,lambda] retains q'≥theta iff M≥0. |
| exact_robust_floor_boundary | For every error in [0,epsilon], epsilon≥0, the same uniform protection holds iff M≥epsilon. |
| exact_low_certificate_boundary | Positive-width certificate bounds 0<xd<1, 0≤qd<theta, 0≤wd≤1, wd≤lambda*(1-xd), alpha*(1-qd)≤beta*wd*qd exist iff M<0. This algebraic equivalence does not itself require alpha+beta≤1; actual closure does. |
| low_box_step, low_box_all_times | Under the declared rate/domain conditions, the paid, authorized operating projection keeps 0≤x≤xd, 0≤q≤qd, wd≤w≤lambda at every natural-number time. |
| strict_loss_of_renewing_share | For positive eta, fine and x in that region, x'<x. No limit theorem follows merely from this strict decrease. |
| gap_correspondence | The normalized gap fine*(q-theta) is exactly the existing profit gap when fine*theta=cost-lobby. |
| example_parameter_boundary | In the displayed one-parameter family, M≥0 iff beta≤5/12, and M=0 iff beta=5/12. |
| Three parameter witnesses | With alpha=1/4, lambda=1, theta=3/8, beta values 1/4, 5/12 and 1/2 give margins 1/16, 0 and -1/32. The last has the old low-box certificate (xd,qd,wd)=(1/10,9/25,9/10). |

Additional closure conditions are eta,fine≥0, eta*fine*theta≤1 and 0≤mu≤1. Strict selection and active feedback interpretations require positive rates, although the closure theorem allows zero rates. The original example simultaneously retains its favorable invariant rectangle: negative M does not imply every initial state degenerates.

The projection does not supply funds, permission or support. It applies to actual operating histories only while those execution conditions remain satisfied; it does not say an economy continues after essential support fails. Lambda bounds the influence target, and the theorem additionally requires current w≤lambda: inherited influence can violate that current-state premise. Error, initial states below theta, entry from zero, excluded-recipient harms and changed causal laws must retain their separate treatment.

This migrates and strengthens the old low-rectangle closure argument, not the old real-valued convergence or finite-support-failure arguments. The certificate is an invariant region, not a proved strict attractor or a complete basin boundary. No spectral bifurcation, critical exponent, hysteresis loop, universal rate threshold, ethical axiom or market calibration is proved. The [integrated interpretation and counterreview](../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MARKET-INTERNET-DEGENERATION.md#degeneration-boundary-and-transition) states empirical and normative correspondence separately.

<a id="checked-local-attraction"></a>
## Checked local attraction and coupled support, 8 October 2026

The later [RegimeAttraction.lean](RegimeAttraction.lean) completes a narrower, explicitly rational attraction result left open by the preceding boundary study. **38 new theorems / 52 declaration audits** pass; **58 inherited theorems / 66 audits** are rebuilt and separately recorded. Run [check_attraction.py](check_attraction.py) with Python; [the receipt](attraction-verification.json) and [frozen audit](attraction-verification/AttractionAudit.lean) bind all three actual source modules, compiler and logs. No previous real-valued theorem is silently upgraded.

| Checked result | Scope |
|---|---|
| fixed_iff_balances, fixed_classification | For the original numerical family with only beta varying over 0<beta≤3/4, every physical fixed state is H=(1,1,0), L=(0,1/(1+4 beta),1), or S=(1−5/(12 beta),3/8,5/(12 beta)). Clipping is shown inactive throughout this physical domain. |
| middle_physical_iff, middle_fixed, collision_at_boundary | S is physical iff beta≥5/12; it meets L at equality. At beta=1/2, S=(1/6,3/8,5/6). |
| low_selection_direction | The low fixed state's quality is below the selection threshold iff beta>5/12, and above iff beta<5/12. This is not a complete parameterized stability proof. |
| high_tube_step/history, high_approaches | At beta=1/2, H's weighted neighborhood contracts by 7/8 per step; every positive rational tolerance is eventually met permanently. The initial radius is at most 1/32. |
| low_tube_step/history, low_approaches | L's neighborhood contracts by 79/80 per step with the same quantified eventual property. Initial radius is at most 1/48. |
| upper_cone_step, middle_upper_escape, middle_unstable | Arbitrarily small physical perturbations near S eventually have x>1/4. While still in the stated neighborhood, the positive displacement lower bound grows by at least 81/80 per step. This does not classify every perturbation direction. |
| coupled_operating_step, coupled_histories | Exact lifting into the old full State includes budget=1, paid correction, zero additional shocks and the original support update, at every operating step. |
| low_stock_loss, low_guarded_history_fails | For x≤1/48 while C≥5, support loses at least 15/16 per step. Every finite rational initial support leads to finite failure of the original guarded history. |
| high_tube_supplies_old_safety, high_coupled_history_never_fails | The high neighborhood with C≥5 supplies the already checked safe rectangle, so the actual guarded history never fails. |
| zero_share_remains_zero | The supplied share law contains no entry route. Changing beta alone does not create renewers from x=0; this is a representation limitation, not real-world irreversibility. |

The two neighborhoods are relative to the physical state domain. With r≥0, H's tube is x∈[1−r,1], q∈[1−8r,1], w∈[0,2r]; L's is x∈[0,r], q∈[1/3−r,1/3+r], w∈[1−2r,1]. The proof scales are mathematical coordinate bounds, not ethical weights or empirical recovery rates. Natural-number bounds prove eventual approach rather than relying on numerical convergence.

The low projection's infinite limit is not an endlessly operating full economy: its essential support fails first. Failure is absorbing under the supplied guard; future replenishment, entry or changed laws would require their own representation. No complete basin surface, all-parameter stability, real-state extension, critical exponent, spectral bifurcation or empirical calibration is claimed.

[The stationary-branch figure](figures/regime-fixed-states.png) marks local behavior only at beta=1/2. [Its program](plot_regime_states.py) uses Matplotlib and creates PNG/SVG plus a [provenance record](figures/regime-fixed-states.json); no simulated history is used. For this run Matplotlib was installed in an isolated temporary environment outside the repository, with no global dependency change. The [theoretical integration and counterreview](../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MARKET-INTERNET-DEGENERATION.md#attraction-and-support-coupling) distinguishes the actual support relation, normative appraisal and next empirical correspondence.


<a id="checked-supported-transition"></a>
## Checked finite transition with support

[RegimeTransition.lean](RegimeTransition.lean) imports the original market, boundary and attraction modules. Run `python3 experiments/market-generativity/formal/check_transition.py` from the repository root. The [receipt](transition-verification.json) freezes four sources, the audit and five logs in [transition-verification](transition-verification). Lean 4.29.1 checks **27 new theorems / 35 named declarations** and separately rebuilds **96 inherited theorems / 118 declaration audits**. Only standard logical axioms are allowed; no unproved declarations, native decision shortcuts or warnings pass the checker.

All states and costs are rational. The supplied intervention changes only beta from 1/2 to 0 for a finite pulse, with an additional constant support consumption cost≥0 each step. It leaves the evolving x, q, w, monetary reserve and support stock intact. Its formation and actual institutional implementation are premises, not derived here.

| Declarations | Exact contribution |
|---|---|
| positive_seed_finite_landing | Every physical initial state with x>0 reaches x≥3/4, q≥1/2, w≤1/4 in finite pulse time. No initially favorable profit gap is required. |
| ready_after_three, growth_below_target, influence_relaxes | Actual quality recovery, positive-share growth and influence relaxation deliver the landing condition. |
| cover_formula, remaining_cover | K₀=5, Kₙ₊₁=(10/9)(Kₙ+1+cost). Initial stock≥K_N keeps each t≤N above K_(N−t)≥5. This is sufficient, not minimal. |
| pulse_coupling_history, pulse_prefix_executes | Exact correspondence with original full State and every guarded pulse step, including monetary payment and extra support use. |
| landing_supplies_safety, supported_finite_transition | The actual arrived state supplies the inherited Safe certificate. After withdrawing the pulse and extra burden, the original beta=1/2 guarded history continues forever. No resource reset occurs at handoff. |
| zero_seed_never_lands | This share law lacks an entry mechanism: x=0 cannot be restored by the pulse. |
| share_history_upper, no_uniform_pulse_duration | x_N≤(3/2)^N x₀; no fixed N guarantees landing for all positive seeds. |
| too_late_even_without_extra_cost | At (x,q,w,C)=(1/100,1/3,1,5), even immediate beta=0 with zero extra burden triggers first-step guarded failure; computed support is 353/100. |

The finite intervention horizon exists before the support cover is selected. The theorem does not claim that a given actual endowment is sufficient, that this is a least-cost policy, or that every positive state recovers under unchanged beta=1/2. The full recovery boundary, empirical calibration, partial interventions, discrete extinction/entry and formation of the correction remain separate questions. It proves protection after withdrawal, not a new all-state convergence result.

[Chinese/English integration and substantive counterreview](../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MARKET-INTERNET-DEGENERATION.md#supported-finite-transition) explain the link to degeneration, meta-attraction and generative alignment. The result reuses the established normative argument and does not derive an ethical verdict from stability.


<a id="checked-partial-transition"></a>
## Checked partial correction and the critical case

[PartialRegimeTransition.lean](PartialRegimeTransition.lean) extends the same model, importing the completed finite-transition module. `python3 experiments/market-generativity/formal/check_partial_transition.py` rebuilds five sources and an audit from frozen bytes. The [receipt](partial-transition-verification.json) and [frozen package](partial-transition-verification) bind **26 new theorems / 31 named-declaration audits** and **123 inherited theorems / 153 audits** to Lean 4.29.1. No new axioms or warnings are accepted; inherited work is not counted as new results.

| Declaration | Checked scope |
|---|---|
| exact_universal_landing_boundary | For 0≤beta≤3/4, every physical rational state with positive x reaches Landing in finite time iff beta≤5/12; zero additional error. |
| retained_positive_seed, uniform_seed_floor | Before selection turns favorable, transient losses still leave xₙ≥x₀/2 throughout the subcritical/critical history. This is derived, not assumed. |
| eventual_positive_gap, partial_finite_landing | The retained share changes influence; quality eventually exceeds 3/8 by x₀/32 and the original protection rectangle is reached. |
| supercritical_low_box_never_lands | The original low-certificate and all-time box theorems imply an entire nonarrival region above the threshold. This does not assert that all states fail. |
| critical_noise_fixed, arbitrarily_small_error_blocks_universal_landing | An arbitrarily small *constant adverse error*, not a sampled random process, yields a positive critical fixed state that never lands. No stability claim for that point. |
| partial_coupling_history, supported_partial_transition | Exact lifting of each partial-correction step to original full State, consumption of the declared extra support, then inherited guarded nonfailure after withdrawal without stock reset. |

The cover K_N, cover-step inequality, landing-to-Safe adapter and final protection theorem are reused. The new parameter condition is 0≤beta≤5/12; implementation and funding of that change remain supplied. The critical positive-seed bound and iff concern the operating projection; actual execution additionally requires the support cover. Zero-share entry, full basin boundaries, arbitrary time-varying beta, noisy recovery away from criticality, least costs and empirical calibration are not claimed.

[Theory, interpretation and counterreview](../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MARKET-INTERNET-DEGENERATION.md#partial-correction-boundary) preserve the distinction between a mathematical partial intervention and formed market effects.

<a id="checked-finite-support-obstruction"></a>
## Checked finite-support obstruction

[FiniteSupportObstruction.lean](FiniteSupportObstruction.lean) imports the original finite-transition module and uses the original full State, operatingStep and guardedStep with time-varying beta/error. Run `python3 -B experiments/market-generativity/formal/check_finite_support.py`. The [source-bound receipt](finite-support-verification.json) and [frozen proof package](finite-support-verification) record **17 new theorems / 22 declaration audits**, with **123 inherited theorems / 153 audits** separately rebuilt under Lean 4.29.1.

For each finite stock C₀≥5, take an integer N>C₀−5. Every seed 0<x₀≤(2/3)^N/6 fails by N for every beta/error sequence and nonnegative stock shock, with the share-growth and stock laws fixed. No support injection, direct entry or faster growth is admitted. This is a conservative obstruction interval, not the exact viability boundary. `support_required_for_small_prefix` derives C₀≥5+N as necessary for survival through a small-renewal prefix. `guarded_prefix_sound` connects the stock argument to the actual guarded history, and `guarded_failure_persists` retains termination. `projected_recovery_and_actual_failure` uses the old finite-arrival theorem for the same seed whose full history fails; `same_stock_can_support_high_seed` reuses old all-time protection for a different seed with the same stock.

中文：本轮将一个来不及恢复的示例推广为每个有限存量对应的正区间及全部时变纠正，且接回原实际守卫。生成、维持与组织终止在同一历史内解释；原规律和实际对应仍明示，未宣告无公理奠基。参见[论证、反审与下一接口](../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MARKET-INTERNET-DEGENERATION.md#finite-support-obstruction)。
