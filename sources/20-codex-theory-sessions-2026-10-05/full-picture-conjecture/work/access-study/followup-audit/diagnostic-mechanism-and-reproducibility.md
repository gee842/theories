# Why no selected main policy bought diagnostics

Exploratory follow-up, 5 October 2026. The frozen access study is unchanged. This note interprets its negative diagnostic finding and supplies one independently checked counterexample to a universal dominance claim. It does not extend the registered grid, reclassify exploratory work as prospective evidence, or establish an empirical theory of inquiry.

## Exact answer

**The frozen result is nonuse in a particular grid under seven probes, not a theorem that paid diagnosis is dominated throughout this model.** The main 1,134 selected optima bought no tests. At the same physical parameters and costs, a different one-round state and evaluation criterion admit a strict diagnostic advantage. The full four-coordinate attainable set therefore cannot generally be replaced by the no-test set.

Several features explain the original nonuse without individually proving it:

- Direct repair needs no diagnosis or permission beyond the accessible cash bill. It costs three, clears the current fault, and also raises stock in the productive update. It can help even when the fault is absent.
- To test now, equipment must already be ready; upkeep plus testing costs `1+2=3` before any repair or new output. A positive-dependent repair requires a six-unit branch bill. Testing cannot pay that bill with the income it may help preserve.
- The main grid starts unready. Rebuilding costs three and introduces a one-round lag, within a four-round horizon. Many low-stock/liquidity histories need a direct response before that route becomes useful.
- Ordinary stock/output evidence is already observed and filtered. Paid tests add information before repair; they do not monopolize evidence about damage.
- The seven probes include pure failure/recovery, pure expense/burden, and three stipulated mixtures. Pure physical protection can favor repair without waiting for evidence; pure cost/burden can favor no intervention. The chosen mixed weights did not make the intervening diagnostic tradeoff optimal in the frozen grid.

The last statement is a computed conditional result. The first four mechanisms alone do not prove that tests can never pay: avoiding burden from a repair without its fault target can matter enough to justify information. The following exact example demonstrates that distinction.

## One-round local formulas

Take stock one, an already ready diagnostic, at least six accessible units, one round remaining, and fault probability `p`. Keep every physical and monetary parameter at its frozen value. Let `(F,E,B,U)` denote collapse probability, expected expense, the stipulated burden, and terminal stock below two.

The no-intervention damage probability is `d(p)=.1+.7p`. A positive test has probability `q(p)=.1+.8p`. Compare three complete prescriptions:

| Prescription | F | E | B | U |
|---|---:|---:|---:|---:|
| Drop readiness; no repair | `.1+.7p` | `0` | `0` | `.1+.7p` |
| Drop readiness; repair directly | `0` | `3` | `1−p` | `.1` |
| Keep, test, repair only a positive | `.09−.01p` | `3.3+2.4p` | `.15−.1p` | `.10+.07p` |

For the selective rule, failure is a negative report followed by damage without repair: `.1p·.8 + .9(1−p)·.1 = .09−.01p`. Expense is upkeep plus test plus positive-branch repair, `3+3q(p)`. Burden is `.05` for testing plus false-positive repair probability `.1(1−p)`. Unrecovered stock adds the `.1q(p)` probability of healthy damage after a positive-branch repair. These are expectations over the joint latent fault and diagnostic/damage events, not products that incorrectly assume those events independent marginally.

At `p=1/2`, the vectors become:

| Prescription | F | E | B | U |
|---|---:|---:|---:|---:|
| No intervention | `.45` | `0` | `0` | `.45` |
| Direct repair | `0` | `3` | `.5` | `.1` |
| Test; repair positive | `.085` | `4.5` | `.1` | `.135` |

Direct repair costs less and protects better than the selective test on this local comparison, but imposes greater **modeled burden**. The diagnostic avoids many repairs in healthy states, at the price of the test, false negatives, and some remaining failure. Because target-absent repair may physically improve stock, this burden is an explicit evaluation premise, not a demonstrated complete harm measure.

## Complete enumeration, not a cherry-picked pair

`diagnostic_mechanism.py` enumerates all eight legal prescriptions through the independent latent-event oracle. At the exploratory weight `(20,1,10,0)`:

| Prescription | Weighted score |
|---|---:|
| Drop; no repair | `9` |
| Drop; repair | `8` |
| Keep; no test; no repair | `10` |
| Keep; no test; repair | `9` |
| Keep; test; never repair | `12.5` |
| Keep; test; repair only negative | `16.8` |
| Keep; test; repair only positive | **`7.2`** |
| Keep; test; always repair | `11.5` |

Selective testing is the unique scalar optimum. The new weights are a mathematical witness to a tradeoff, not endorsed moral weights. The original seven probes, applied to this same new state, all still choose no testing. In particular `(12,1,4,0)` gives scores `5.4` for no action, `5` for direct repair, and `5.92` for selective testing. The changed criterion matters; merely making a test available does not make it desirable.

This witness changes the initial cash from the main total-five design to six, readiness from unready to ready, and horizon from four to one, and uses a previously untested objective. The physical transition, diagnostic quality, prices, and burden charges are unchanged. It disproves global dominance at those technology/cost parameters; it does not say diagnostics improve one of the originally registered four-round cases.

## A more interpretable common-constraint comparison

Hold the same new state fixed and require expected expense at most `4.5` and expected burden at most `.1`. Both policy classes have the same hard initial cash of six, so a six-unit diagnostic-plus-repair branch is feasible even though the **expected** expense limit is `4.5`.

Without testing, any randomized policy can do no better than randomize between direct repair and no repair. Terminal readiness has no benefit, and keeping it only adds expense. Let repair probability be `r`. Then burden is `.5r`, so the burden bound requires `r≤.2`. Failure is `.45(1−r)`, giving the exact no-test lower bound **`.36`**, attained by repairing with probability `.2`.

Selective testing attains **`.085`** failure, with expense `4.5` and burden `.1`. An exact rational linear-program vertex enumeration over mixtures of all eight prescriptions confirms that `.085` is also the constrained optimum of the full one-round policy class. The independent program enumerates supports of at most three prescriptions, sufficient for a probability normalization and two upper-bound constraints, and checks all relevant active-constraint vertices. The no-test mixture calculation independently agrees with the elementary formula.

This is a comparison under shared limits, **not equal actual spending**. The optimal no-test policy spends `.6`; selective testing spends `4.5`. Both satisfy the same allowance, but the no-test class cannot use additional expenditure to reduce failure without breaking the burden bound. There is no need to waste money to manufacture equal spending. The result demonstrates a genuine value of discriminating information under the supplied burden criterion and payment rules.

## What reproducibility establishes

There are distinct achievements, none of which implies the next automatically:

1. **A saved run can be reproduced.** The same frozen model, inputs, protocol and arithmetic give the same outputs. For an exact finite calculation, this checks the computational record and executable procedure; it is not a statistical replication on new worlds.
2. **A calculation survives independent implementation checks.** The previous audit independently enumerated latent histories and posteriors, checked cash ledgers, solved 4,536 one/two-round support values and 18 targeted four-round values, and verified the saved summary. This reduces the risk of a mistaken recurrence, omitted signal, timing error or wrong reported number. It does not remove shared modeling assumptions or prove every untested result.
3. **A conditional mathematical claim is demonstrated.** The identical-first-action access witness and this diagnostic witness establish exact possibilities within declared finite models. A proof may extend beyond numerically checked examples when its premises hold. Its connection to a real institution still needs a justified interpretation and independently measured mechanism.
4. **A mechanism transports to a substantive second implementation.** That would require new evidence about actual dependencies, interventions, measurement, access, and outcomes. Repeating the same simulator, even with a second code implementation, does not establish such transport.
5. **A normative conclusion is warranted.** A model can show consequences or incompatibility of thresholds. It does not determine whether its burden proxy, stakeholder choices, or acceptable risks are legitimate. Those premises remain explicit commitments open to challenge.

The practical accomplishment is therefore substantial but specific: the account-access failure and the limited normalization result are concretely inspectable, mathematically constrained, and supported by independent error checks. The absence of selected paid tests usefully narrows that study's claim. The exploratory witness shows how a changed evaluative requirement can make the same priced diagnostic useful; it does not turn the original absence into a hidden success.

## Durable evidence and limits

- `diagnostic_mechanism.py`: independent exact enumeration and constrained-mixture calculation.
- `diagnostic_mechanism_results.json`: all eight prescriptions, the new scalar comparison, both constrained optima, original-probe results at the new state, and hashes confirming frozen files were unchanged.

Every new file is within `work/access-study/followup-audit/`. The original main results, protocol, and model were checked unchanged before and after the calculation. No broad new parameter search, new field evidence, or universal value-of-inquiry result is claimed.
