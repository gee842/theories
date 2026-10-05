# Constructed records before outcome-dependent evidence

6 October 2026. AI-authored specification written before executing results.
This study supplies a finite physical-record interface to the existing paid
teacher and [confidence calculation](../transfer-evidence/README.md). It does
not implement the parallel prediction-to-action or updater-formation work.

## Actual formation and paid slot construction

Use the existing `FormedSelection` preparation under its unchanged event law.
For `K` desired slots, start with no variants or resident, a damaged site,
material capacity `2K+1`, common fuel `F0`, and source `E0`. Execute `K` H
formations, one A formation, A association and repair, followed by `K`
capture/local-copy pairs. The actual endpoint has `K` free A, `K` free H,
one A resident, common fuel `F0-K-3`, source `E0-K`, and no local fuel.
Formation spends `2K+3` total fuel units, including the local-copy fuel.

A supplied blank-slot recipe consumes one free A, one free H and one common
fuel unit. Both material units remain incorporated in the blank, reserved or
written slot. No overwritten or spent material is silently made reusable.
Assembly occurs before recording; its costs remain in the global ledger and
are not treated as invisible steps of the old teacher. The primary preparation
is exactly the previously checked `K=2,F0=12,E0=18` witness, producing common
fuel 7 and source 16 before slot assembly and 5 and 16 afterward.

The bit-record recipe, its wiring, phase separation, access to source receipts
and their routing to common fuel are supplied local mechanisms. The old
formation repertoire is suspended after handoff. Inherited site, resident and
local-store fields remain accounted for. This does not derive chemistry for
memory or prove that the old capture site alone implements the new routing.

## Reserve, observe, commit

The recorder is initially idle with no acquired bits. Admission requires a
blank slot, at least two common units and at least two source units. Before
the outcome is realized, reserve that slot, subtract two common units, burn one
for operation and hold one in write escrow. No second trial can be admitted
while this one is incomplete.

Outcome zero converts two actual source units to common fuel and latches zero;
outcome one produces no receipt and latches one. Commitment consumes the
reserved write unit and appends that actual bit. A supplied completion schedule
executes every admitted outcome and commitment before another admission; an
enabled commit alone is not a theorem of eventual scheduling. Record retention
has no damage or erasure event within this finite experiment. No claim of free
or perpetual retention follows.

A completed three-event macro exactly projects to the unchanged
`prediction_step`, including fuel, source, paid/loss counts and the EWMA decoded
from the retained word. In the full recorder, the stored word equals the entire
attempted outcome word. The stored word's length and popcount are decoded
quantities, not separately constructed free counters or a constructed confidence
computer. Further decoding, certificate or action machinery remains supplied.

Every completed trial spends two units. During a partial trial, write escrow
is included in available stored energy. At all phases, free and bound parts,
slots and the resident are included in material accounting. The possible
receipt must be backed before admission: without enough source, the same full
Bernoulli kernel is not licensed merely because a failure branch can execute.

## Controls on record completeness

All arms use the same initial stocks, slot recipe and two-unit price for every
attempt. Their commitment rules differ:

- **Full:** append every actual outcome; halt acquisition when no slot remains.
- **Drop zero and resume:** consume write escrow but omit a zero and return its
  slot to blank, then permit another trial. Ones are retained normally. This
  is a declared faulty commitment rule, not the positive protocol.
- **Halt on first zero:** append the actual zero, then stop. All retained records
  form an actual prefix, so outcome-dependent stopping does not remove evidence
  from the prefix or spend a fresh confidence budget.

The audit retains raw attempt counts, both outcome counts, exact history-family
probabilities and all operation/write costs, including omitted observations.
The slot-only certificate decoder reads the retained bits; it does not invert
global fuel/source ledgers. An alternative observer with suitable stock readings
and initial references could recover the raw counts. Thus this is a failure of
the specified record interface, not an impossibility of every possible decoder.

## Prespecified checks

First check every two-bit word from the actual two-slot preparation, including
every reserve/outcome/commit state, exact parent-teacher projection and global
ledgers. After the word `[0,1]`, fuel 3 and source 14 can support another old
teacher trial, but the constructed recorder has no blank slot. Abundant fuel
cannot replace missing parts or a consumed record slot.

For the stress comparison use `K=8,T=32,F0=84,E0=72`, giving actual post-assembly
fuel 65 and source 64. Targets are stationary independent Bernoulli with
`beta=1/4`. All potential attempts through the horizon can be funded before
their outcomes; the different record rules determine which are admitted.
Use the earlier single-stream dyadic certificate with `alpha=1/10` and strict
threshold one quarter. No new final recipient action is performed here.

The full recorder retains its first eight outcomes and stops. Its final false
threshold certificate occurs only on eight ones, with probability `1/65536`.
The drop-zero recorder can keep trying until eight ones are retained or 32
attempts finish. Its false certificate probability is exactly
`Pr(Binomial(32,1/4)>=8)`, about `0.567529`. It has changed the stored observation
law despite paying the same price per actual trial. The halt-on-zero control
retains a genuine prefix and should preserve the confidence guarantee.

Use exact rational dynamic programming for all stress histories and an
independent reference implementation. Check parts, slot capacity, escrow,
prepayment, complete record equality under the positive protocol, and all raw
attempts and costs under the fault. The finite handoff supplies a complete
observation record under these laws, not stationary calibration after arbitrary
physical change, memory renewal, ethical valuation or the unified foundation.
