# Fulfillment-sensitive withdrawal in the acquired evaluator

AI-authored continuation, 6 October 2026. The [protocol](PROTOCOL.md) was
written and [frozen](protocol-freeze.json) before implementation. It was
committed before the producer existed. The [producer](model.py) loads the
accepted [succession model](../model.py) as a separate module instance and
wraps it; no accepted file is edited. Both hashes are checked before and after
the run.

Before the full run, one smoke test exercised four cases on the single donor
path `signals_111/shared/variable/11`. It wrote no output files. The
[first full run](first-run-receipt.json) covered 33 cases (29 frozen, 4
added), 5 arms, 3 producers, 6,270 histories and 147,792 checked snapshots,
with no producer change after outcomes.
[`check.py`](check.py) tests the frozen predictions; its output is
[`check.json`](check.json). [`formal/FulfillmentStatus.lean`](formal/FulfillmentStatus.lean)
proves the status rule exact. An independent reconstruction, written from the protocol without reading the
producer, matched all 136,389 compared values. It is recorded in
[`independent-check.json`](independent-check.json), and its notes are in the
[integration](../../../../../../../../../../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/FULFILLMENT-WITHDRAWAL-INTEGRATION.md#5-independent-reconstruction).

## What was added

The episode receipt register retains the first probe's
(epoch, action, present, receipt), mirroring the accepted second-query frame.
It is paid from 6 new isolated units: bind 1, write 4, read 1. The total
conserved quantity becomes 596. The fulfillment evaluator keeps the accepted
paid read and write and the acquired rule (`10·n > 64`). It adds a status
computed only from accessible records: the register, and the reader's already
paid cache entry for the second query. The status gates the help decision.
Withdrawal changes only the assessment; `n`, command support, the frame and
the register are unchanged.

## Results against the frozen predictions

| Prediction | Result |
|---|---|
| P1 shared-arm regression on 29 frozen cases | **passed**: every reported metric except `retained` and total `new_spent` (which include the new register) equals the accepted `reporting.json` |
| P2 `k = 1` withdraws wherever the shared arm attempts | **passed**: the claim was met in every such history; `n` and command support were identical; retained source was 10 higher where the shared service completed |
| P3 evidence sensitivity at `k = 2` | **passed**: 36 withholdings where both probes actually captured, 216 deliveries where the first probe missed, no excess |
| P4 unknown status, first channel missing | **failed in part**: status was unknown in all 36 supported histories, and `deliver` exceeded the claim in all 18 of its histories. The predicted positive count for `hold` leaving the claim unmet was **0**, not positive |
| P5 forged record | **passed**: 36 histories withheld while the claim was actually unmet |
| P6 `k = 3` matches shared | **passed** |
| P7 unprovisioned register | **passed** |

**Why P4 failed.** When the first feedback channel is missing, the
candidate is not updated, so both probes use the same action. A supported
command then requires the second probe to have captured under the same law.
This was confirmed by replaying all 76 donor paths of both cases: every
supported history has actions (0,0) or (1,1) and receipts (true,true). Given
stationarity of the law between probes, support therefore implies that the
first probe also captured. The counting rule correctly reports what the
receipts alone certify. But the architecture's own update dynamics settle
what the receipts leave open. In every actual unknown-status history here,
withholding was correct and delivering exceeded the claim. An evaluator that
also used its own update law and the stationarity premise could have certified
fulfillment. The prediction's assumption that both worlds occur among
supported histories was wrong for this architecture. The failure is
preserved, and the protocol is unchanged.

## Scope

This establishes evidence-sensitive, paid, episode-bound withdrawal under
supplied claim, episode and service meanings. Efficacy knowledge and acquired
influence are retained. The decision changes with recorded fulfillment under
a fixed claim (P3), and that contrast is absent from constant abstention. A
forged record misleads it (P5). The `k = 2` treatment of unknown status is a
supplied priority. Patient good, standing, the claim size and authority remain
supplied, as in the accepted application account.
