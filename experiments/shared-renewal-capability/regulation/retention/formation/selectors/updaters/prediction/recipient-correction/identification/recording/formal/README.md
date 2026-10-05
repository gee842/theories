# Formal actual-emission recording interface

This package formalizes the deterministic interface in the
[parent protocol](../PROTOCOL.md): a recipient's real acquisition supplies an
addressed, prepaid four-bit archive, which a paid partial reader can consume.
It does not execute rooted reason replay or derive normative relevance.

Run `python3 check.py`. The saved [verification.json](verification.json)
records a fresh frozen-source Lean **4.29.1** build, compiler/source/checker/
toolchain/log hashes and declaration dependency audits. There are **67 new
audited theorems**, distributed over four modules. The unchanged dependencies
contribute 142 inherited audits: GenerativeCore 18, FormedSelection 43,
RecipientCorrection 36 and RecipientIdentification 45. Each new theorem has a
matching `#print axioms`; the checker rejects proof holes, custom axioms,
`native_decide`, unsafe declarations, compilation warnings and dependencies
outside `propext`, `Quot.sound`, `Classical.choice`. No downloaded dependency,
object cache or compiler binary is included.

## What is proved

| Module | New audits | Exact scope |
|---|---:|---|
| [EmissionArchive.lean](EmissionArchive.lean) | 19 | Generic actual-emission provenance from empty traces; injective four-bit encoding; valid partial written prefixes; no completed-address overwrite; archive/world noninterference; prepaid reserve/escrow account; cell account and twelve-cell admission bound. |
| [RecipientArchive.lean](RecipientArchive.lean) | 22 | Instantiation by actual recipient acquisition; prebound query/context/action checks; missing-channel payload; three-query pointer guard; per-address backing; quarantine; physical positive-receipt invariant and archive preservation; partial certificate soundness and correlated truth vectors. |
| [ArchivePreparation.lean](ArchivePreparation.lean) | 12 | The enabled 44-event word through unchanged FormedSelection; endpoint and 30 energy cost; guarded pair assembly, material/energy conservation; twelve cells plus reader; original common/source partition; arithmetic whole-account reconciliation. |
| [PaidArchiveReader.lean](PaidArchiveReader.lean) | 14 | Paid activation, context read and three four-cell reads; preservation of the whole archive state and world; reader charge 14 / remaining 6; invalidation; sound partial cache; an explicit handoff from an empty ready archive and an actual archive history. |

The main composition is `reachable_archive_paid_certificate`. It starts with
an empty archive over a ready recipient world, follows an actual archive
trace, then the paid reader trace. Every `Some b` cache entry at address `i<3`
equals `b=(Z==designated i)` under the declared fixed recipient law. Its proof
uses `empty_archive_sound`, `archive_trace_sound` and
`actual_archive_paid_certificate`; no new supplied `Facts` assay replaces the
producer history. The reader retains the **entire archive state** as its world,
including producer accounts, archive reserve, write escrow, blanks, pending
phase and completed records. Its record field is a read-only view of those
same records, not another paid storage allocation.

The desired vector is `(0,1,0)`, so complete truth vectors are only `101` and
`010`. These are correlated propositions about one orientation. There is no
claim of three independent reason edges or the old six-record/two-context
reason archive.

## State and boundary qualifications

The generic archive carries actual producer successors justified by the
producer step relation. Its writer never accepts a user-supplied receipt
bit. A four-bit injective encoder is required; record identity is not inferred
from encoding length alone. The header/workspace capacity and address plan
are explicit hardware premises. Generic blank accounting is pooled; concrete
binding also checks `backing i=true` and `i<3`. A record at address `i` cannot
shift to another address after omission.

The concrete world increments its pointer on recipient sensing regardless of
archive admission. Its step relation restricts a new recipient sense to
`next<3`, matching this finite client; `step_pointer_bounded` preserves the
bound from a bounded initial state. This is a client restriction, not a
refinement of every arbitrary continuation of the predecessor process.
A supplied context interlock disables emission and writing after quarantine;
it preserves pending physical contents and escrow. The paid reader separately
invalidates its context token/current-use flag while retaining cache bytes.

The formal target law is fixed `RecipientCorrection.Laws`, even through tag
changes. Arbitrary changing-context plants, sensor calibration and renewal
of access are not proved. Interpreting tags as a changing law additionally
requires the appropriate correspondence and stability premises. The current
reader guard checks its paid context token; it cannot manufacture calibration.

`four_writes_endpoint` is the deterministic advance calculation for a
latched frame with four escrow units. A valid four-write execution additionally
requires a valid pending state, writable world and the supplied completion
schedule. The generic trace invariants and guarded executable witness cover
those respective claims; the endpoint calculation is not a scheduler theorem.
Arbitrary valid fabricated states do not have provenance: the provenance and
reachable-certificate theorems explicitly require the empty initial state and
actual history.

The preparation theorem proves the new controlled material word and paid
assembly recipe. Their wiring, storage function, protected compartments and
freeze of the bound material pool remain supplied. It does not inherit the
old small preparation probability. `primary_whole_ledger` is an arithmetic
identity, **not** a Lean derivation of the whole stochastic prefix/suffix.
The exact Python and independent-check packages establish those finite
histories separately. There is no machine-checked full Python refinement:
for example, old source bookkeeping exposes an in-flight packet earlier than
the corresponding formal completed work boundary. After a context-change interruption, Python can retain an acquired payload in an invalid pending frame, while the formal quarantine suppresses that emission. Both block writing/current certification; this is a further representation difference, not an asserted microstate equivalence.

## Remaining consumer boundary

The output is a paid `Option Bool` factual cache with six reader units still
present. Pure closure lemmas accepting that type can be reused only after an
explicit relevance/root/target mapping. This package does not invoke the old
`ReasonReplay.paid_recorded_reason_sound`, does not discharge its raw-Bool
`Assayed`/`decodeAt` interface, does not perform its path checks and does not
create ethical significance. Finite three-frame capacity supplies no
unbounded evidence accumulation or general learning theorem.

See the [mathematical account](../../../../../../../../../../../../_process/research/2026-10-05-concern-theory/RECIPIENT-RECORDING-MATH.md)
and [parent executable README](../README.md) for the positive construction,
controls, failure regimes and separate numerical evidence.
