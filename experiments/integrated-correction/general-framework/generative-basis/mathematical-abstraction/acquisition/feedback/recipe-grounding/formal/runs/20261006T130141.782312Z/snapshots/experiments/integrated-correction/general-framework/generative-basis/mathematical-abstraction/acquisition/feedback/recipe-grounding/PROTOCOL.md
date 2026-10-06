# Forming the operative decoder used by the later reader

Prospective protocol, 6 October 2026. This is an additive **alternative
continuation before calibration-reader installation**, from the actual saved
remaining-dependency endpoint. It does not append a new budget to the depleted
calibration terminal state or modify either frozen ancestor.

## Named premise replaced and premises retained

The [calibration reader](../calibration_revision.py) supplied a reliable mapping
from contacted physical bits to acquired bits. Here its physical transducer is
initially unknown. A formed two-row decoder must translate actual raw contact
outputs into the bits used by the existing calibration consumer. Its rows begin
unbound, are constructed from acquired reference encounters, and are consulted
again during real stock/weak contacts. There is no preinstalled identity decoder,
desired-recipe flag, observer accuracy reward, or successful completed recipe
draw. The all-four decoder family follows from two independently assignable
Boolean output wires. The actual construction need not enumerate that family.

The addressed primitive transducer is a deterministic unary Boolean map `f`.
All four maps `00,01,10,11` are included. The same physical transducer acts on a
forced reference input and on the subsequent contacted stock/weak bit. Two
reference commands actually clamp a jig to 0 and then 1; the issued command is
retained and binds the acquired raw response. This action-grounded reference,
its contact binding, stable reuse of the same transducer, the stock-occupation
and weak-signal input coupling, finite register construction, and the comparator
and wiring primitives remain supplied physical laws. They are not derived by
calling a correct answer 'reliable'. Coherent wrong forcing and use-dependent
transduction are tested failures of those premises.

Faithful reference data `(raw=f(x), issued=x)` require output wire `g[raw]=x`.
The bind operation writes that row if empty or equal; a contrary previous
binding marks conflict and does not overwrite it. Two nonconflicting assigned
rows establish an operative decoder. Distinct outputs permit recovery for both
physical inputs; equal outputs are incompatible with recovering both. No raw
polarity is privileged: inverted transduction requires the correspondingly
inverted formed decoder. Missing or detectably misbound references stay unknown.

This explains local inverse-wiring formation and selection. It does not form
the native transducer itself, establish arbitrary sensors' reliability, derive
all physical laws, or replace the separate material carrier-formation law.

## Actual support and register encoding

The principal actual parents are `law_01_learned`, `calibration_break` and
`false_dependence` in [remaining-dependency-results.json](../remaining-dependency-results.json).
They retain H 110, old pair 01, selected 1, old completion, fuel `214009/32768`,
source 0, live 34 and stage peak 42. The entire saved history, including its actual
earlier peak 114, is reconstructed and preserved. Capacity stays 256.

Formation allocates 26 new bounded registers: the calibration interface's 16
candidate cells and 8 control/record cells, plus 2 decoder-output cells. These
are bounded finite registers, not a claimed bit-optimal hardware realization.
Initially the candidate bank is inactive/blank (`mask=None`). Its first 2 cells
temporarily hold the two bound reference records. The 8 control cells temporarily
hold issued-reference binding, physical jig setting, transient raw contact,
ready/conflict status, reference cursor, activation state, wire-address cursor,
and assembly/retention phase. Boolean flags and printed fields are finite
projections of these staged encodings, not extra freely supplied memory.

After both references and the readiness check, a separate charged activation
clears the temporary reference records and initializes all 16 candidate bits to
true, restoring the ordinary calibration control roles. The output wires stay
formed and are used thereafter. The old installation combined allocation and
mask initialization. This replacement allocates blank storage, performs actual
additional reference work, then initializes the bank; no old cost is refunded.
Past reference records remain in the external trace but are no longer actor
inputs after this overwrite. The completed wiring carries their consequence.

The original account tariff is unchanged. All events have zero workspace;
capacity precedes fuel guards and a denied charge changes nothing. An explicit
waiting control consumes support at this actual entrance, never sets fuel to a
fixture. There is no new source, full transfer or actor replenishment.

| New event | Work | Temporary | Extra | Rewrites / live change |
| --- | ---: | ---: | ---: | --- |
| `decoder_assembly` |26|8|1|live 34→60|
| `reference_force` |1|2|1/4|actual jig set by issued reference|
| `reference_contact` |0|2|1/4|actual raw response exposed|
| `reference_record` |1|2|0|2 rewrites|
| `bind_decoder_row` |1|2|0|1 rewrite|
| `reader_readiness` |2|2|0|1 rewrite|
| `activate_calibration` |16|2|0|16 rewrites; refs cleared, mask true|
| `formed_decoder_read` |1|1|0|consult actual addressed output row|
| `unbind_decoder_row` (intervention) |1|1|0|1 rewrite; no memory refund|

Both reference sequences occur even if one datum is missing; readiness then
fails unless both records are valid, both rows assigned and no conflict exists.
All real full/weak contacts subsequently use the [old calibration events and
prices](../CALIBRATION-REVISION-PROTOCOL.md) at live 60, with the additional formed
decoder read after the actual raw contact and before its existing record write.
A missing raw datum remains missing after this charged read. An absent addressed
row halts even when the previously retained ready flag was true. Retention of
the 60-cell interface is attempted after later failure if assembly succeeded.
The old immutable historical controller and all load/waste/source stocks remain.

The conventional consumer uses the same formed rows and inherited conventional
filter/selection implementation and must match the full trace. A raw-consumer
intervention incurs the same decoder-read charge but forwards raw rather than
the formed output. A formation intervention incurs identical row-bind charges
but forms no rows. An after-ready row-removal intervention consumes work and
leaves readiness true, testing operative wiring rather than a verdict flag.

## Fixed cases before execution

There are 33 cases:

1. The 3 principal parents × identity/inverting transducer × learned/conventional
   consumer:12 cases.
2. Each principal parent × constant 0/constant 1 transducer:6 cases.
3. Each principal parent with inverting transducer and raw-consumer clamp:3 cases.
4. Positive parent with inverting transducer and formation clamped:1 case.
5. Positive parent with inverting transducer and reference 0 or 1 missing, or
   reference 0 or 1 wrong-tagged:4 cases.
6. Positive parent with identity transducer and coherently inverted actual
   forcing (returned labels still match issued commands):1 case.
7. Positive parent with identity reference transducer changed to inversion after
   readiness, and a distinct case with reference identity/use inversion from
   the start:2 cases. The former has an explicit boundary-change event; the
   latter violates common-mode use. Neither is an actor diagnosis of that cause.
8. Positive parent with inverting transducer and output row 0 unbound after
   readiness:1 case.
9. Positive parent with inverting transducer after waiting consumption 1 or 2:2 cases.
10. The actual `source_exhausted` parent:1 entrance-denial case, not a negative
    full-load observation.

Reference faults change returned labels/data only, except coherent wrong forcing
which changes the actual jig. Stable primary maps and the two drift/use controls
are declared before execution. The inherited current-domain binding is context 1.
The reader never checks latent `f` to select a decoder or to reject corrupted
reference data. Common coherent faults can therefore create false confidence.

## Required conclusions and retained failures

Compare actual constructed rows for identity and inversion, constants and
partial evidence; preserve the exact real contact through those rows into the
existing application/filter/inquiry controller. Derive four candidate decoders
from the two row operations, rather than importing a favored decoder list.
Check all fixed conventional matches, old-coordinate conservation, no new source,
and the original 145-unit identity at every event. Raw-clamped histories must
match formation/reference expenditure and diverge only at actual decoder use.

No full diagnostic completion or retention is assumed affordable. The complete
old diagnostic history left less than one fuel unit; the new formation work can
prevent its completion or retention. A valid narrower positive result is formed
reliable decoding followed by an actual full-stock observation and retained
local application. Preserve all later failures and calculate the actual support
frontier rather than lowering prices after execution. Identifiability is still
limited to the supplied reference and same-transducer contract; ethical worth,
native carrier chemistry and all-premise grounding remain distinct questions.
