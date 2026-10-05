# Actual recipient events → paid contextual evidence

6 October 2026. This closes a finite interface between the accepted
[recipient identification law](RECIPIENT-IDENTIFICATION-MATH.md) and an actual
partial factual reader. It extends the earlier
[recording fidelity account](RECORDING-FIDELITY-MATH.md), without reusing that
recorder's outcome-dependent actor-fuel transfer. The new
[protocol](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/PROTOCOL.md) is implemented in the existing
[identification recording package](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/README.md).

The derivation under test is **paid consequence → faithfully retained,
contextual evidence → paid usable factual input**. It does not derive the
sensing calibration, storage recipe, concern valuation, root of a reason
network, or an unlimited supply of records.

## 1. The producer is an event, not an observer's saved trace

Keep the entire recipient-identification state: working fuel, recipient fuel,
source packets, active controller, its packed action cells, phase and escrow.
A recipient query still costs eight working units and still transfers a
successful ten-unit packet to the recipient, never to the actor. Its actual
acquisition event supplies an `Option Bool`. A missing channel is `None`;
zero is a present but unsuccessful receipt. The archive cannot execute work,
produce a second receipt or inspect a hidden capture flag to fill a missing
acquisition.

Three addresses are bound to the three recipient queries in `R,A,R,A,R`.
A backed physical query pointer advances on recipient sensing even if no
archive admission follows. Each address owns four bit cells. A frame is

\[
  (c,a,p,r)=(\text{context},\text{issued action},
            \text{acquisition present},\text{acquired receipt}).
\]

Target and query address belong to the supplied finite address plan and
workspace; they are not additional hidden data stored inside four bits. The
four-bit encoding is injective. The formal generic recorder requires this
property; an arbitrary record type with a length-four encoder alone would
not justify physical storage of the record.

After paid recipient sensing and before work, admission checks the actual
query identity, current context, issued action, its own four unused backed
cells and five archive units. Binding spends one and escrows four. Only that
query's actual acquisition can latch the frame. A missing channel still
latches `(c,a,false,false)`. A different query cannot fill the binding. Four
writes consume the escrow, one per physical cell. No further source or
working-fuel transfer occurs. An interrupted frame retains its tags, latch,
written prefix, reserved cells and escrow; it is not a completed record.

The supplied context-change interlock quarantines new bindings, emissions
and unfinished writes. Completed historical bytes remain, but the current
reader cache is invalidated. Quarantine does not refund a payment, erase a
partial frame or silently refresh a context token.

## 2. Generic provenance and conservation

Let a producer give an actual transition relation, a binding predicate, an
emission function of the bound header and actual transition, a four-bit
injective encoding, a write-permission predicate and its energy account.
An archive trace may bind, execute a genuine producer transition, or write
the next latched bit. A write event carries no externally chosen outcome.

**A1 — provenance, persistence and account.** Starting with an empty archive,
every completed record has a preceding actual producer emission at the same
address. Completed addresses cannot be overwritten or rebound. A partial
write contains exactly a prefix of the emitted encoding. For every finite
valid trace,

\[
 E_{\rm producer,final}+B_{\rm final}+X_{\rm final}
 +\sum(\text{producer charge}+\text{binding charge}+\text{write charge})
 =E_{\rm producer,initial}+B_{\rm initial}+X_{\rm initial},
\]

where `B` is the unspent archive reserve and `X` is write escrow. If `m`
bindings occurred, then

\[
 \text{blank}_{\rm final}+4m=\text{blank}_{\rm initial}.
\]

In particular twelve cells permit at most three admissions, including
interrupted admissions. Producer events preserve archive funds, and archive
binding/writes preserve the entire producer world. Pooled capacity is only
the generic statement; the concrete admission additionally requires the
specific address's backing.

*Proof.* Induct on events. Binding transfers five reserve units to one spent
unit and four escrow units, and removes four blank cells. Core transitions
use the producer's own ledger. Each write spends one escrow unit, extends
the actual encoded prefix, and only the fourth write publishes the record.
At a new latched state, the emission function is its only source of payload.
At publication the previous latch supplies provenance. Empty initialization
removes the otherwise possible preexisting-record case. A completed address
is never enabled for another binding. These invariants and the telescoping
accounts are machine checked in `EmissionArchive.lean`.

Neither validity alone nor a fabricated latched state proves historical
provenance. The provenance theorem explicitly starts from an empty archive
and a valid history. The four-write endpoint calculation is separate from
an enabled four-write trace, which also needs a valid pending state and a
writable world. Completion remains conditional on executing the paid
writes; conservation and soundness do not supply a scheduler or fairness.

## 3. Actual acquisition → qualified partial truth

The existing physical law is

\[
 C=V\,\mathbf1[a=Z],
\]

with binary target orientation `Z`, availability `V`, and no false-positive
receipt. This identifies the action from a positive receipt, while zero
admits both mismatch and outage. The acquisition channel must faithfully
report the receipt when present. Target/context correspondence and stability
are supplied local premises.

For a predeclared proposition `Z=d`, define the decoder

\[
 D_c^d(F_i)=
 \begin{cases}
 \operatorname{Some}(a_i=d),&F_i\text{ is complete, correctly addressed,}\[-2pt]
 &c_i=c,\ p_i=r_i=1,\\
 \operatorname{None},&\text{otherwise}.
 \end{cases}
\]

**A2 — every emitted certificate is true at the declared target.** An empty
archive over a sound initial recipient world remains sound along genuine
archive transitions. Thus each `Some b` from a complete, currently matching
frame satisfies `b=(Z=d)`. This includes a sound `Some false` when a positive
receipt identifies the opposite binary action. A zero receipt itself never
licenses that negative conclusion.

*Proof.* The recipient work law establishes that positive receipt implies
issued action equals `Z`. Other valid core transitions preserve this
invariant where a receipt is pending. The concrete emission checks the
bound query id, action and context and reads only the actual acquisition;
therefore every positive payload has that action. A1 preserves the emitted
payload through the archive. The decoder returns a value only under the
positive, present, matching-context guard. The formal `ArchiveSound`
invariant and `completed_record_sound` make this connection explicit.

The formal law uses fixed `RecipientCorrection.Laws`; a varying-context
interpretation additionally needs a correct mapping from paid context token
to the applicable target law and stability during acquisition and use. It
does not prove unknown context sensors calibrated. The no-false-positive
law is operational calibration, not an ethical or phenomenological claim.

**Failure.** The two worlds `(a,Z,V)=(0,0,0)` and `(0,1,1)` both return zero.
Any total zero→orientation decoder is wrong in one. A paid but corrupted
action tag can similarly produce a wrong `Some` value: expenditure cannot
replace binding integrity. Missing records cannot be compacted into a list
without changing later query identities; fixed holes are therefore part of
the law, not presentation detail.

For the actual desired vector `(0,1,0)`, the complete truth vector is only
`101` when `Z=0` or `010` when `Z=1`. These are three correlated propositions
about one orientation, not three independently acquired reason edges.

## 4. A paid reader that consumes these records

Reader activation costs one and clears its bounded cache. A paid context
read costs one and acquires a token. Three prepaid, atomic four-cell reads
cost four each. Each read accesses its fixed address and stores the partial
decoder result, including unknown for an absent, partial or mismatched
record. A completed cache requires all three reads and a current matching
context token. A context change invalidates active/current use without
erasing old bytes or automatically acquiring a new token.

**A3 — paid cache soundness.** Starting with reader20, the declared
activation/context/three-read trace is feasible, spends14 and leaves6.
Every nonempty entry of its completed current cache equals the corresponding
`Z=d_i` truth value, provided its input is a reachable sound archive and the
fixed target premises of A2 hold. Reader steps preserve the entire supplied
world and archive. Incomplete or invalidated caches cannot claim a completed
current result.

*Proof.* A reader invariant states that every address below its read pointer
contains exactly the decoder result for the paid token and unchanged
archive. Each enabled read preserves the invariant and spends four; the
context interlock disables its use. The actual-archive handoff discharges
`Facts` using `ArchiveSound`; it does not assume a fresh independent assay.
`PaidArchiveReader.actual_archive_paid_certificate` proves this interface.
The finite five-event reader trace and exact14 charge are also checked. Its retained world is the entire archive state, including pending phase, reserve and escrow, not just a projection to the actor and source.

This is not an invocation of `ReasonReplay.paid_recorded_reason_sound`.
That theorem's original `Assayed` raw-Bool archive and old `decodeAt` have not
been instantiated. Its pure closure lemmas can consume arbitrary
`List (Option Bool)`, but an application still owes the relevant edges,
positive root, target interpretation, shared continuing account and paid
path checks. This package performs none of those checks. Its six remaining
reader units are an actual reserve for a possible next operation, not a
claim that that operation occurred.

## 5. Material witness and one original account

The unchanged `FormedSelection` process starts with material28, common91,
source144, no variants and no intact controller. Its named word is fourteen
H formations, A formation, association, repair, thirteen capture/local-copy
pairs, then capture. All44 events are enabled. The endpoint has free A13,
free H14, resident A1, local1, common74, source130. Formation spends30.

Twelve paid cell-pair assemblies and one paid reader-pair assembly bind26
constituents and spend13 common units. The remaining resident A and free H
back the old controller. Its old adapter spends one common unit and routes
the actual local unit into common. This leaves common61 and source130.
Protect archive15 and reader20 before any old outcomes: the unchanged old
prefix receives working26 and thirteen actual ten-unit packets. The
physical finite cell/reader wiring, address plan, protected routing,
quarantine and staged freeze of the formation pool are supplied recipes.
The proof does not infer their functionality merely from two constituent
counts. No bound part is reused as free precursor after handoff.

On the primary path the unchanged eight-exposure prefix reaches working28,
with five packets remaining; its actual five-query suffix ends with working4,
recipient20 and no packets. Archive recording spends15 and reading spends14,
leaving reader6. The complete account is

\[
 235=44_{\rm construction}+78_{\rm prefix}+54_{\rm suffix}
       +15_{\rm archive}+14_{\rm reader}+30_{\rm retained}.
\]

The formal package verifies the actual formation word, each guarded assembly
recipe, the exact endpoint and partition, and this arithmetic reconciliation.
The continuing stochastic prefix/suffix and whole runtime ledger are checked
by the separate exact executable and independent checker. The numerical
probabilities are conditional on the new controlled preparation; the old
small preparation probability is not inherited. A numerical endpoint account
is not labeled a machine-checked refinement of every Python microstate.

## 6. Scope of the advance and remaining transition

We have a finite, costed, material construction in which actual recipient
receipts become durable addressed records and then paid partial factual
certificates. It replaces an observer log or an arbitrary supplied Boolean
fact at this interface. It also rules out treating outage zeros as negative
orientation evidence or treating recording failure as core work failure.

Remaining supplied premises include the form/assembly repertoire, bounded
workspace capacity, address and context sensors, faithful channel, no-false-
positive outcome law, retention, stable local target, protected budgets and
completion schedule. The finite archive cannot establish infinitely many
samples, general calibration, or durable knowledge across unmodeled target
changes. The next concern interface needs an explicit relevant proposition
and root plus a physically compatible paid reason consumer; those are not
created by the correlation of these three target propositions.

Formal source and frozen verification: [formal README](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/formal/README.md).
