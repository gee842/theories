# Paid positive-witness identification

This supporting experiment supplies qualified recipient-response input to the
[recipient correction interface](../PROTOCOL.md). It addresses the
[prediction decoder's outage ambiguity](../../PROTOCOL.md): a missing receipt
alone cannot distinguish wrong action from missing opportunity. The new rule
leaves that observation unqualified and pays to explore. It is not a general
availability detector, a source renewal mechanism, or a derivation of concern.

## Actual predecessor and source

Use the unchanged [coupling model](../../coupling/model.py) preparation and its
first eight exposures, including failed preparations, finite fuel, all endpoint
masses and conditional ledger marks. Declare **13 ten-unit packets before
preparation**, with initial common fuel 30 and the existing one-unit source
adapter input. Run the old eight-exposure prefix; the remaining five packets
fund the external opportunities `recipient, actor, recipient, actor, recipient`.
Nothing is refilled at the interface. The prefix is noiseless with reversal
after four exposures; suffix recipient availability is 3/4 in the primary case.
Actual suffix entrance fuel is 11, 21 or 28 in eligible variable-coupler paths.

Admission uses exactly the parent eligibility predicate: active formed
predictor, updater and normal coupler; an acquired confident register q=0 or4.
It does not assume that register is correct about the actor in every history.
The complete inherited state remains in the saved fixture and setup trace.

## Supplied finite recoding and query law

One newly supplied **atomic four-unit recipe** installs target observation and
recodes the existing register. This intentionally differs from the parent's
partial two-plus-two setup billing. With inherited bit b, set q=b+2b and
repurpose the old binary `last` field as recipient qualification flag 0. The
old last-action role ends. Actor bit, recipient candidate and qualification
need eight distinguishable states, within the old five-by-two state capacity;
the code does not silently use an observer flag as controller memory. The
finite recipe/wiring and a five-exposure stabilized hold are supplied; parent
wear, renewal and replacement are suspended during this declared interface.

Before each query, require the **whole eight-unit actor bill**, then charge
rent1, target observation1, work3, acquisition1 and two register writes2.
Acquisition plus writes are escrowed before work. The sequential microstates
are saved, but the guard is atomic: if the total is unavailable, no query is
admitted, no partial bill is charged, and stabilized access ends. The payload
may remain but is no longer operational. Every admitted query pays acquisition
and both writes even if missing evidence or unchanged memory requires a sham
write. An actor return cannot finance its own admission. The expensive-write
control changes write2 to write4, hence total10, with the same rule.

Every scheduled exposure consumes one source packet. A correct available
actor action transfers10 to actor fuel; a correct available recipient action
transfers10 to a separate recipient reserve. All other packets are lost,
including those at unaffordable/inactive exposures. Recipient receipts never
pay actor rent, sensing, work or memory. Source stock being present and a
physical opportunity being available are distinct premises.

The controller reads only installed q/flag and the paid target report. A
recipient action is its candidate; an actor action is its inherited actor bit.
Actor queries leave both cells and qualification unchanged, with paid sham
writes. Recipient updates from acquired action-tagged target receipts are:

| Previous status | Receipt | Next candidate | Next status |
|---|---|---|---|
| unknown | zero | opposite action, for the next paid exploration | unknown |
| unknown | positive | action just executed | qualified |
| qualified | either | unchanged | qualified |
| either | missing channel | unchanged | unchanged |

Under a stable binary target and no false-positive capture, a qualified
recipient candidate is correct. Zero is never itself assigned a truth label.
There is no hidden change clock or final-use phase in this policy: the third
recipient call executes the same rule as the first. The observer's raw trace,
truth, error counters and witness marks never enter the controller.

## Prespecified comparisons and failures

`positive` is the rule above. `conventional` is an explicit finite-state table
with exactly the same prices and behavior. `failure_label` writes action on
every positive and its complement on **every zero**, always qualifying the
result, including after previous qualification. `no_exploration` qualifies a
positive but retains its candidate on an unknown zero. Actor queries are
unchanged for all four arms.

Cases: primary opposite target with recipient availability3/4; noiseless;
same target with3/4; no opportunity (availability0, stock still paid); missing
recipient channel; target flips immediately before the third recipient query;
initial common12; initial common36; write4. Prefix producers are variable,
its conventional realization and fixed-normal. No claim of superiority over
the conventional realization is permitted. Target change is an adverse case:
an old positive no longer licenses a persistent truth assertion.

On the correct-actor, opposite-target path with successful second and third
recipient calls, inherited fuel28 gives
`28 -> setup24 -> R16 -> A18 -> R10 -> A12 -> R4`.
The exact entrance threshold for all five admitted calls on this path is26;
at25 the second actor call cannot prepay and no later recipient use occurs.
These are conditional path witnesses, not unconditional preparation claims.

Qualification cannot be guaranteed from a finite all-zero history. Under a
conditional opportunity floor lambda for each completed matching trial,
failure through k such trials is at most `(1-lambda)^k`; independence is not
needed. Payment and completion of those k matching trials are separate
conditions. A stable target throughout diagnosis is required to attribute an
earlier zero to mismatch rather than outage; otherwise a later positive only
identifies the later target. No infinite continuation follows from finite
stocks or the supplied finite hold.

## Outputs and acceptance

`fixtures.json` preserves original preparation branches, original/prefix laws,
actual predecessor endpoint masses/states and prefix ledger marks.
`results.json` preserves all unconditional endpoints and suffix traces,
qualification errors, acquired qualified later use, costs and final reserves.
`model.py` uses exact rational branch probabilities; `check.py` replays those
results and targeted boundary/ambiguity cases. A separate checker must use an
independent transition implementation. Source hashes bind all results to the
actual imported preparation/prefix code and this protocol. The formal package
is independently maintained and verifies its stated deterministic scope.
