# Checked recipient correction interface

6 October 2026. [RecipientCorrection.lean](RecipientCorrection.lean) contains **36 checked declarations** under pinned Lean 4.29.1. It imports only `Std`, so it does not depend on the concurrently changing prediction, coupling or concern implementations. The [mathematical note](../../../../../../../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/RECIPIENT-CORRECTION-MATH.md) states the derivation, assumptions and protocol-specific calculations.

The package proves:

- Exact zero-new-probe actions for every pair of independently varying binary target laws require an injective encoding into the controller's complete accessible state. Different pairs have distinguishable target-query behavior; four distinct states are necessary. One complete Boolean state cannot suffice.
- A two-cell table packed as `actorBit + 2*recipientBit` uses four of the five already available abstract register values. Recipient writes preserve the actor cell; actor writes preserve the recipient cell; distinct-cell writes commute.
- Opposite stable laws defeat a single shared overwritten bit. Consistent target relabeling preserves behavior, while aliasing recipient evidence into the actor cell can damage actor behavior.
- A genuine action-tagged recipient receipt identifies its noiseless complementary binary law. Zero private credit cannot distinguish recipient success from failure. Using private zero as a fabricated receipt happens to identify the correct law exactly on failure; source outages also produce observation aliases.
- Observation followed by writing requires their summed price in the actor's remaining reserve. Completed updates have an exact payment ledger and preserve the actor cell. An affordable observation remains charged when writing subsequently fails.
- Explicit finite witnesses demonstrate packed correction and shared-record interference under opposite laws.

The lower bound applies to **all** state the action rule can consult and assumes no new outcome probe after the target query. It does not say the inherited organization lacks physical capacity: its five-valued register already contains enough codes, and its other fields must not be silently excluded if a different controller uses them. The paid recoding recipe and actual material realization remain supplied.

It also requires independently variable laws. A supplied invariant that recipient law is always the opposite of actor law permits one stored bit plus target-dependent inversion. The concrete shared arm lacks that rule and instead uses and overwrites one common estimate. Its opposite-laws failure alone is not the four-state lower-bound proof.

The formal payment interface begins after prior routing and work expenses. `paidFeedback = none` denotes the absence of a completed observation/write pair; it does not refund an observation. A separate theorem retains that intermediate expense. This partial interface does not represent full installation, missing-channel handling, unpaid rent destruction, all four exposure stages, the stochastic predecessor or its inherited ledger.

The [protocol](../PROTOCOL.md), producer and independent computational checks cover those larger claims. In particular, the inherited 20-unit boundary for the four-phase witness and its unconditional probability are not Lean theorems here. No source-to-Lean refinement, physiological implementation, normative value or private-retention advantage for recipient evidence is claimed.

Run `python3 check.py` in this directory. The checker freezes the source, compiles it in a fresh temporary directory, audits every theorem and records hashes in [verification.json](verification.json), with full output in [verification/RecipientCorrection.txt](verification/RecipientCorrection.txt). It rejects placeholders, custom unproved declarations, native proof shortcuts, unsafe declarations, compiler warnings and unexpected dependencies. The checked dependency union is `propext` and `Quot.sound`; several theorems have empty dependency lists. No project object cache or predecessor source is used.
