# Runtime source audit: the exposure is not the old paid-write block

6 October 2026. Read-only source inspection preceding the new numerical comparisons. The source program is `prediction/model.py:advance`; the predecessor proof is `PredictionAction.lean`, with completed blocks in `PredictionProtocolBridge.lean`. This note specifies correspondence obligations, not a new empirical experiment or a completed verification receipt.

## The actual state boundary

The runtime returns `(State, exact branch probability, MOMENTS increment)` for every scheduled exposure. The twelve state fields are `fuel, gate, gate_life, stage, life, q, last, written, prelearn, stale, corrected, witness`. Its first eight fields suffice for future physical/controller evolution. The remaining four only calculate historical witness readouts. Keeping only fuel or an average score is not a sufficient composition interface: gate/circuit lifetimes, prototype stage, previous action and acquired-write status determine later costs, operation and readouts.

The finite source schedule is external to `State`, but not absent from the account. Each call receives one opportunity and its packet is either captured or entirely wasted. Composition must carry the remaining opportunity count, original hidden orientation and actual reversal index. The plant state can change under the declared reversal schedule; the controller is not allowed to inspect that schedule. `after` is used only by the historical observer. The analyst must not resample hidden orientation or choose a favorable fresh entry on each call.

Input validity matters. Scores are in 0–4, stage in 0–2, lifetimes in their declared bounds, and a positive gate lifetime requires gate type 0 or 1. Gate −1 with positive lifetime is malformed: Python would treat −1 as truthy inside `learned`, while a formal absent-gate encoding need not do so. No equivalence for malformed states is proposed.

## Sequential branches that must survive abstraction

Gate assembly, old base assembly, and retrofit are sequential payments. If a later operation is unaffordable, its earlier costs remain spent. The type/prior draws occur only at their source guards; a fixed-size random tape can draw both in advance only if unused outcomes are marginalized and cannot affect subsequent choices.

An installed live circuit pays rent even if its gate has expired. If it cannot pay, `advance` clears the accessible circuit fields and unfinished correction flags. Its completed historical witness is retained. If rent is paid but the gate or work is unavailable, that rent stays spent and the scheduled packet still expires. The previously corrected implementation explicitly fixes this rent-before-gate-check order; the old development version must not be used as the reference.

For an actual trial after prelude, let \(F\) be its pre-rent fuel, \(a\) the issued action and \(c\in\{0,1\}\) actual capture. With maintenance \(m\),

\[
F_{\rm postwork}=F-r-d+c(G-m),\qquad
h=\mathbf1\{F_{\rm postwork}\ge w\},\qquad
F'=F_{\rm postwork}-hw.
\]

The write indicator uses the **actual branch's** return, so probability, output and affordability are correlated. Receipt label is \(a\) on capture and \(1-a\) on failure. Writing changes the score only when affordable and the arm's update path permits it. The frozen-register arm still pays and sets the historical `written` flag. After either paid or skipped writing, `last` becomes the executed action and both lifetimes renew on capture or wear on failure. A skipped write is an output boundary with retained state; it is not an absorbing failure state.

The no-return label can be false when the matching action encounters an outage. Nothing in a probability-preserving composition should quietly correct that label from hidden truth. Brier and decoder-error fields are analyst metrics, never rewards driving the update law.

## Exact probability interface

Under availability \(k/N\), a fixed tape of gate bit, prior bit and availability bit has weights \(k\) or \(N-k\), totaling \(4N\). The source uses fair type choice except fixed-type arms and a fair base orientation. Summing tapes that differ only in unused bits gives the guarded source probabilities. Outcome equality must preserve the **joint** distribution of state and expenditure, not only expected captures, average fuel or total success mass.

The computation checks every source-returned observer field and all seventeen `MOMENTS` components. The Lean operational kernel may project away historical flags and most moments if that projection and their noninterference are explicit. The compiled evaluator comparison then checks the remaining eight state fields jointly with expenditure, waste, work/capture/write and status. A projection theorem is narrower than a full Python semantics proof.

## Old formal overlap and counterexamples

The old Lean relation has ready/rented/observed/written phases. Its work receipt assumes availability true. Writing is enabled only when payable; finish requires a preceding written phase. It consumes a packet only at work. It does not contain the runtime's skipped-write completion, unpaid-rent destruction, inactive opportunity expiry or circuit rebuild.

Consequently:

- At a noiseless installed trial where rent/work/write are affordable, the projected four-phase endpoint and ledger can coincide. Updater reformation remains a separate ready-state event in the old relation.
- An unaffordable runtime write advances last/lifetimes and returns. The old relation remains at observed phase with its acquired receipt. These are different continuation laws.
- A scheduled no-work runtime exposure wastes its packet; the old formal no-work prefix retains unused source. Erasing that distinction can fabricate later opportunity or conceal waste.
- A funded prefix before work is not the same as a completed charged macro. Its live transient action/receipt and still-pending opportunity must remain represented if it is exposed or stopped.

The new layer must state exact correspondence to the runtime and the **restricted** old overlap separately. It cannot make the old law cover new outcomes simply by assigning its existing events probabilities.

## Source-bound independent strategy

[CHECK-PROTOCOL.md](CHECK-PROTOCOL.md) fixes the inherited case domain, guard grid and diagnostic examples before comparison. An independent microphase interpreter follows the sequential source contract, checks each prefix ledger, and aggregates exact rational tapes. It compares its full state/moment kernels with callable frozen `advance`, then propagates the actual successor distribution through the unchanged schedule. Failed preparation mass and stocks remain visible outside commissioned continuations.

A separately compiled Lean evaluator consumes the same declared tape fixtures and returns the operational projection. Passing finite comparisons would support that concrete bridge at those entries; generic Lean proofs concern their declared event/kernel law. Neither constitutes a universal compiler/Python refinement theorem, empirical identification, calibrated outage inference or an origin of the supplied circuit recipe.

## Subsequent verification record

The scoped new comparison has now passed on its first numerical run: [results and counts](RUNTIME-RESULTS.md), [receipt](runtime-verification.json). It includes direct compiled-evaluator comparison and the actual inherited endpoint/weighted-first-moment recursion. This updates the verification status without broadening the source-audit claim or identifying the supplied stochastic/physical laws empirically.
