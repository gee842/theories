# Matched states, different future appointments

**The follow-up supports a conditional adaptation mechanism.** In this simulation, appointing rule makers through their contract success improved performance while demand stayed stable. Independent appointments improved adaptation after demand changed, even when both policies began with identical inherited rules, production, and authority memory. Different starting institutions alone therefore cannot explain the earlier result.

This is AI-generated research, reviewed by other AI agents, not independent human peer review. It establishes a policy effect within the specified synthetic model. The [first report](REPORT.md), including its two contradicted predictions, remains unchanged.

## What was held fixed

Each of 128 fresh worlds generated two histories: success-based appointments and independent uniform appointments. After epoch 79 governance, each history was copied into eight continuations: four governance policies crossed with unchanged or changed demand. This produced 256 source histories and 2,048 continuation trajectories. The statistical sample size is **128 worlds**; branches and histories are paired outcomes, not additional independent samples.

Success-based appointment uses the squared moving average of each agent's contract share. Independent appointment selects uniformly among the same agents. Both retain the same information, tenure, decision options, amendment costs, and behavioral rules. Demand initially favors specialization A and, in the changed context, favors B from epoch 80 onward. The model's usefulness measure evaluates production against that demand independently of the public scoring rubric.

Within each source history, every continuation received exactly the same pending rubric, last production outputs, authority memory, skills, and future keyed random draws. Epoch 80 production, allocations, and gross usefulness were identical across policies within each context. Only subsequent governance could cause divergence. No extra correction opportunity was introduced at the fork; the next scheduled opportunity remained epoch 99.

The [protocol](BRANCH-PROTOCOL.md) was written after seeing v1 but before running these new worlds. Seven input files were archived and hashed at **2026-10-04 16:29:46 UTC**. This is local prospective specification, not external preregistration. Parameters were inherited unchanged from v1 apart from the fresh seeds and the branching design. No outcome-dependent tuning or seed replacement occurred.

## Results

The primary outcome was mean gross usefulness over the final 40 epochs. Higher values mean more useful production under the model's specified demand.

| Source history | Demand | Future success-based appointments | Future independent appointments | Independent minus success-based |
|---|---|---:|---:|---:|
| Success-based | Unchanged | 0.70020 | 0.66785 | −0.03235 |
| Success-based | Changed | 0.31999 | 0.63641 | +0.31642 |
| Independent | Unchanged | 0.69766 | 0.66684 | −0.03082 |
| Independent | Changed | 0.33768 | 0.63987 | +0.30219 |

All three prospective primary predictions were supported:

| Prediction | Paired effect | 95% bootstrap interval | Holm-adjusted p |
|---|---:|---:|---:|
| B1: independent appointment helps after changed demand, from success-based history | +0.31642 | [0.29098, 0.34002] | 2.20 × 10⁻⁵⁰ |
| B2: the same effect, from independent history | +0.30219 | [0.27192, 0.33103] | 4.24 × 10⁻⁴¹ |
| B3: that appointment effect is larger after changed demand than under unchanged demand, averaging the two histories equally | +0.34089 | [0.31379, 0.36699] | 3.02 × 10⁻⁵⁰ |

Tests were paired across worlds, with Holm adjustment across these three predictions. Bootstrap intervals use 10,000 whole-world resamples and are marginal, not simultaneous. Independent appointment helped in 115/128 changed-demand worlds from success-based history and 109/128 from independent history; improvement was not universal. Statistical precision here concerns random worlds under one model configuration, not uncertainty about whether the model describes society.

![Matched-state appointment results](results-v2/matched-state-results.png)

The stable-context effects were negative from both histories: −0.03235 [−0.03867, −0.02662] and −0.03082 [−0.03914, −0.02106]. The changed-demand difference between the two history-specific policy effects was +0.01423 [−0.00531, +0.03481]. That comparison did not resolve a history interaction; it does not establish equivalence.

## What the trajectories show

After demand changed, success-based appointment continued to favor A specialists. They held 90.1% of postfork appointments after success-based history and 85.2% after independent history. Independent appointment gave them 49.4%. Final-period rubric weight on A remained 0.824 and 0.794 under success-based appointment, versus 0.206 and 0.194 under independent appointment.

This pattern also arose when success-based appointment was introduced only at the fork. In the model, the ongoing allocation of authority helps preserve the previously favored specialization.

Correction records are consistent with this account. After success-based history, the success-based branch implemented 17 of 349 qualifying reference corrections; the independent branch implemented 132 of 278. After independent history, the corresponding counts were 16/328 and 130/260. These are descriptive comparisons: the branches develop different states and therefore different correction opportunities. They do not isolate the causal effect of who approves one identical correction.

Protected governance reached approximately 0.705 usefulness after changed demand from either history, but it bundles externally maintained authority, a harm veto, and mandatory implementation of qualifying corrections. Fixed branches freeze each inherited rubric; they are not the original v1 fixed-initial-rubric condition.

## Implication and boundary

The supported claim is that **authority allocated through success under current rules can favor stable performance while impeding adaptation when what is useful changes**. Holding inherited state fixed strengthens this claim beyond the original comparison of separately evolving institutions. It does not rescue the original prediction that success-based authority is uniformly harmful.

The intervention changes all subsequent appointments and their ordinary amendments and correction decisions. A correction-only intervention would be needed to separate those pathways. Replacement of appointment policy is immediate, costless, and unopposed by assumption; political feasibility is not modeled. Agents remain myopic, the usefulness signal is exact, and minimum allocations preserve participation. The finite horizon does not demonstrate permanent lock-in, an attractor, a general alignment solution, or an empirical effect in human institutions or deployed AI.

Five structural branching tests passed before execution, including exact agreement with uninterrupted and archived v1 trajectories. The subsequent [audit](results-v2/audit.json) passed all 36 recorded checks, verified all 2,048 summary rows, reconstructed authority memory, and reproduced the three primary contrasts from saved traces. Independent agent review reproduced their bootstrap intervals and checked boundary timing. Frozen-submission rescoring agreed to numerical precision. Both experiments' sealed inputs remained intact.

Full records: [input manifest](results-v2/input_manifest.json), [analysis](results-v2/analysis.json), [per-world summaries](results-v2/world_summaries.csv), [branch checks](results-v2/branch_checks.json), and [pre-run state audit](BRANCH-STATE-AUDIT.md). Checkpoints and complete branch traces are preserved in `results-v2/`.
