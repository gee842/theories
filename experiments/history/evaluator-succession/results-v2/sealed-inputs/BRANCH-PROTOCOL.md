# Matched state appointment experiment protocol

Specified locally on 4 October 2026 after observing results-v1 and before executing any new outcome worlds. This is a new, motivated test, not an untouched original hypothesis or an externally registered study. All input files will be archived and hashed before execution. Structural unit checks may precede the seal; treatment-outcome analysis may not. The prior contradicted predictions remain unchanged.

## Question and causal scope

From identical institutional states, does changing subsequent evaluator appointments alter adaptation when demand changes? Does that effect differ when demand remains stable?

The intervention replaces the future appointment policy, affecting all subsequent amendment decisions. It estimates that policy's total effect in the specified simulation. It does not isolate the effect of changing only who authorizes a particular correction while keeping ordinary governance fixed. A separate correction-gate experiment would be required for that narrower question.

## Design

Use 128 fresh world seeds, 51000–51127. Keep all behavioral, production, scoring, evidence, cost, and horizon parameters from config.json unchanged. There are 160 epochs of five rounds. For each world, generate two source histories over epochs 0–79: one with success-dependent appointment and one with independent uniform appointment. These histories need not resemble each other. They share initial skills and keyed randomness.

Fork each history immediately after epoch 79 governance and before epoch 80 production. In particular, retain epoch 79's amendment under the old demand and its updated authority memory. Do not shorten the configured horizon to generate the prefix, since doing so would change demand timing and suppress governance at the boundary.

The state contains the pending rubric, last production outputs, authority moving average, world identities and next absolute epoch. Immutable context includes skills, action features, parameter values, and keyed future production, appointment, and amendment uniforms. There is no accumulated wealth or learned policy state in this model. Copies must preserve every dynamic value without resetting authority or production.

From each source state, run eight continuations: two demand contexts crossed with four appointment/governance policies. Demand either stays at alpha=0.75 or changes to alpha=0.25 at epoch 80. Branch policies are:

- Endogenous appointments based on the current moving average of contract shares.
- Independent uniform appointments, with matching tenure, choices, costs, and information.
- Fixed inherited rubric, as a secondary comparison.
- Protected correction with the existing veto and mandatory valid-reference implementation, as a secondary feasibility package.

All continuations of a world use the same future keyed random draws. Branching changes no clock: the next correction offer is at epoch 99, followed by 119 and 139. The final epoch 159 has no governance. There is no extra intervention or privileged correction opportunity at the fork. Within a demand context, epoch 80 production and gross usefulness must be identical across branches; appointment differences first act afterward and can affect production from epoch 81 onward.

The appointment-policy change is implemented immediately and without transition costs or incumbent resistance. Thus this test concerns consequences if the change can be made; it does not prove political feasibility. The protected branch retains its externally maintained independence and exact usefulness information.

## Prospective predictions and analysis

Let Y(i,s,c,a) be world i's gross usefulness averaged over epochs 120–159, with source history s, demand context c, and branch policy a. Let D(i,s,c)=Y(i,s,c,independent)−Y(i,s,c,endogenous).

Three primary predictions are specified:

1. **B1:** D is positive under changed demand from an endogenous source history.
2. **B2:** D is positive under changed demand from an independent source history.
3. **B3:** The equal-source-weighted difference in D between changed and stable demand is positive: one half of the sum over source histories of D(shift)−D(stable).

B3 can be positive even if independent appointments are worse in both contexts. It cannot replace B1 or B2. Equal weighting of the two histories is a designed comparison, not an estimate of institutional prevalence.

Use world-paired two-sided t-tests with Holm adjustment across the three predictions. Supported requires the predicted sign and adjusted p<0.05; an adjusted significant reversal is contradicted; otherwise the result is inconclusive. Report paired mean effects and 95% bootstrap intervals using 10,000 resamples of whole world records. Intervals are marginal rather than simultaneous. The independent sample size remains 128: histories and branches are repeated potential outcomes, not extra independent observations.

Secondary analyses report each source/context/branch mean, net usefulness, usefulness over all 80 postfork epochs, source-specific stable contrasts, protected and fixed branch contrasts, and the difference in appointment effect between source histories. Mechanism summaries include rubric weights, contract shares, governor specialization, and correction opportunities and successes. Opportunity sets change with treatment; their conditional response rates are descriptive, not isolated causal estimates. No new threshold for declaring an attractor or permanent adaptation is introduced.

Keep every world. Do not tune parameters, select favorable histories, stop early, or rerun new seeds in response to verdicts. Any later exploratory analysis must be separately labeled. New findings do not replace results-v1 or validate a general social or AI alignment claim.

## Verification and preservation

Before the outcome run, verify that segmented execution under the original policy reproduces uninterrupted v1 execution exactly for each recorded field, including NaNs, shape and dtype. Check the boundary independently against archived v1 trajectories. Snapshot arrays must be copied, protected against mutation, and hashed. First-epoch branch outputs must agree within each context. Epoch 79 governance, absolute correction timing, and terminal exclusions must survive the refactor.

Archive config.json, benchmark.py, the new branch code/config/protocol/tests, and software versions. Save both source checkpoints, source histories, skills and keyed draws, every branch trace with its valid epoch range, per-world summaries, paired contrasts, and verification receipts. Unused prefix positions in branch trace arrays are storage placeholders and must not enter analyses. The output directory is results-v2; it must not overwrite results-v1.
