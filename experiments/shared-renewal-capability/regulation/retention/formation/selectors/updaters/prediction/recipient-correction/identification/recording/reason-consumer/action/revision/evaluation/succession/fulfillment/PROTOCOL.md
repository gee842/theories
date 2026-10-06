# Fulfillment-sensitive withdrawal in the acquired evaluator: protocol

6 October 2026. AI-authored prospective protocol, written and hashed before any
implementation or run of this continuation. It is part of Ren's request to aim
for a complete alignment solution. It addresses one open item of the
[alignment completion contract](../../../../../../../../../../../../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-COMPLETION.md):
"Fulfillment-sensitive withdrawal in the acquired evaluator remains
unimplemented." The obligations come from the
[evaluative application account](../../../../../../../../../../../../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-APPLICATION.md),
which requires the following:

- an actual, accessible, episode-bound record;
- its justified interpretation and scope;
- the dependency connecting it to the affected recommendation;
- its use before the next enabled choice;
- distinct handling of pending, certified-fulfilled and unknown status;
- retention of still-correct efficacy knowledge and acquired influence.

It also warns that constant abstention, a fabricated pending flag, or
redefining the need after the outcome would supply no sensitivity contrast.

## Unchanged base

The accepted [succession model](../model.py) runs unchanged. It is loaded as a
module, and its source hash is checked before and after the run. This
continuation adds one component and one evaluator by wrapping that module's
functions inside a separate module instance; it edits no accepted file. All
29 frozen cases, three producers and the full donor mixtures are rerun.

## Added component: an episode receipt register

The accepted architecture retains the second query's receipt in its paid
four-cell frame. It does not retain the first probe's receipt. A count of
deliveries in the episode therefore cannot be certified from accessible
records. The continuation adds a **receipt register** for the first probe.
It mirrors the existing frame:

- **Provision.** 6 new isolated units, `register_provision`, are added to the
  conserved total, which becomes 596. They cannot fund any other component,
  and no other account can fund the register.
- **Binding (1 unit).** At the first probe's recipient sensing, the register
  binds to the bank epoch and the action read from the candidate, like
  `bank.prebind_query1`.
- **Latching and writing (4 units, one per bit).** At that probe's actual
  acquisition, the register latches (epoch, action, present, receipt).
  `present` is 0 when the feedback channel is missing. The four bits are
  written at the probe's completion. Only the actual acquisition supplies the
  contents.
- **Reading (1 unit).** The new evaluator reads the register during its paid
  evaluation, before writing its assessment.
- **Blocked operations.** If the probe does not reach sensing (outage,
  blocked guard, or exhausted support), the register stays unbound. Any of
  its steps that cannot proceed is recorded as blocked. Unused provision
  stays retained.

The second query's receipt is read from the reader's already paid, validated
factual cache entry 1. That entry is non-null exactly when the frame is
complete, bound to the current epoch, present and positive. Using it adds a
consumer route, not a sensor; this is a declared architectural premise. When
the cache entry is null there is no current command support, so the selected
opportunity cannot arise in the accepted guards.

## Claim premises (supplied, fixed before running)

**Episode.** The episode is this child's first-probe, second-query and
selected opportunities for the same retained recipient in the same bank
epoch. **Service meaning.** A qualifying delivery is an actual capture (the
recipient gains 10) in the episode. **Claim size.** The claim is for `k`
qualifying deliveries, with `k ∈ {1, 2, 3}`. These are independently
specified premises, not inferred from outcomes. Each is run on every history.

## Status rule

From accessible records only:

- `certified` counts the register record and the second-query frame where
  they are present, epoch-bound and positive;
- `unknown` counts records that are absent, unbound or have `present = 0`;
- **fulfilled** means `certified ≥ k`; **pending** means
  `certified + unknown < k`; anything else is **unknown**.

## Evaluator arms

All arms share the accepted paid evaluation read/write and guards.

| Arm | Decision at a valid assessment |
|---|---|
| `shared` | accepted rule: help iff `10·n > 64` |
| `fulfill_k1`, `fulfill_k3` | help iff the shared rule helps and status is pending |
| `fulfill_k2_deliver` | as above, and also help when status is unknown |
| `fulfill_k2_hold` | as above, but withhold when status is unknown |

For `k = 2`, the treatment of unknown status is a supplied priority, not
derived from the evidence. `deliver` gives an admitted claim precedence over
the actor's retained support when fulfillment cannot be certified. `hold`
gives precedence to retained support. Both are run. A withdrawal changes only
the assessment. Command support, retained `n`, the frame and the register are
left unchanged.

## Added cases

Each added case reuses the `changed` or `stable` configuration with one
change:

1. `first_feedback_missing_changed` and `first_feedback_missing_stable`: the
   first probe's feedback channel is `missing`.
2. `register_receipt_forged`: a configured provenance mutation. After a first
   probe that actually missed, the register's receipt bit is set to 1. This
   is labeled as a fault and tests the soundness premise.
3. `register_unprovisioned`: the register has 0 provision, so no record
   forms.

## Observer metrics (never policy inputs)

For each history the observer records:

- actual episode deliveries (probe captures plus a selected capture);
- `claim_met_end`, meaning episode deliveries ≥ `k`;
- `excess`, meaning a selected delivery made after `k` had already been
  reached;
- `withheld_while_unmet`, meaning a valid assessment withheld while actual
  deliveries were below `k`;
- retained units, `n`, current command support, and the register state.

Results are mixture-weighted as in the accepted study. No history is dropped.

## Predictions (frozen)

**P1 (regression).** For the 29 frozen cases, the `shared` arm's
outcome metrics (excluding the new register account) equal the accepted
`reporting.json` values for every case, arm and producer.

**P2 (k = 1).** In every history where `shared` attempts a selected delivery,
`fulfill_k1` withholds. The claim is actually met in each such history.
`n` and current command support are identical to `shared`. The actor retains
10 more source than in the corresponding `shared` history where the selected
service ran, apart from inherited miss and shortage paths, which are reported
separately.

**P3 (evidence sensitivity at k = 2).** With faithful channels, `fulfill_k2_*`
withholds exactly in the supported histories where both probes actually
captured. It delivers in the supported histories where the first probe
actually missed. `stable` contains the former and `changed` the latter. The
choice therefore varies with the recorded evidence under one fixed claim.
`excess` is 0 throughout.

**P4 (unknown).** In both `first_feedback_missing_*` cases, the status is
unknown in every supported history. `fulfill_k2_deliver` has positive
`excess` exactly where the first probe actually captured. `fulfill_k2_hold`
has positive `withheld_while_unmet` exactly where the first probe actually
missed. Evidence does not decide between them; the supplied priority does.

**P5 (forged record).** In `register_receipt_forged`, `fulfill_k2_*` withholds
in supported histories while the claim is actually unmet. This counterexample
is preserved: certification is only as sound as the record's faithfulness.

**P6 (k = 3).** `fulfill_k3` makes the same choice as `shared` in every
history.

**P7 (unprovisioned).** With no register, `fulfill_k2_deliver` matches
`shared`, and `fulfill_k2_hold` withholds in every supported history.

## Acceptance and failure

A prediction failure is reported as a failure and its history preserved. It
is not repaired by changing this protocol. Producer bugs found after the run
need a recorded rerun receipt that preserves the first run. An independent
reconstruction, written from this protocol and the accepted model's
interface without reading the producer, must reproduce the arm decisions and
observer metrics. A Lean module proves the status rule's soundness under
faithful records and relates the decisions to `ContinuationScope`.

## Scope

This continuation demonstrates evidence-sensitive withdrawal in a finite
architecture under supplied claim, episode and service meanings. It does not
derive patient good, standing, the claim size, or the priority used under
unknown status. It does not establish that withdrawal is right in a world
where the claim's meaning is contested.
