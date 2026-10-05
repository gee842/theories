# Formed slots and complete paid records

6 October 2026. This finite construction connects actual formed material to
the retained-record premise of the [paid teacher](../README.md) and its
[confidence interface](../transfer-evidence/README.md). It charges slot
construction and reserves writing capacity before each outcome. The positive
protocol preserves every admitted bit; an outcome-dropping control changes the
recorded observation law despite paying for every physical attempt.

The recipe, write mechanism, source access, receipt routing and finite retention
law remain supplied. This is not a construction of a confidence computer or an
infinite stream of reliable memory, and it does not duplicate the parallel
prediction-to-action or updater-formation mechanisms.

## Actual parts and fuel, without a reset

The preparation runs the existing [formation event table](../../process.py).
For `K` slots it starts with material capacity `2K+1`, no variants or resident,
a damaged site, common fuel `F0` and source `E0`. It forms `K` H particles and
one A, associates A, repairs, then executes `K` capture/local-copy pairs. Its
endpoint is:

`K free A, K free H, resident A, intact site, no local fuel, F0−K−3 common fuel, E0−K source`.

These are selected feasible histories of the existing law. No unconditional
stochastic probability of reaching them is assigned. Each new blank slot then
consumes one actual A, one actual H and one common unit. Its two parts remain
incorporated when the slot is blank, reserved or written. The local recipe is
available only while idle and with those parts and fuel; this experiment
assembles all slots before sampling and consumes every free A/H pair.

The two-slot fixture is exactly the earlier
[material-selector preparation](../../../../../../integrated-correction/general-framework/generative-basis/lean/learning/construction/README.md):
`F0=12,E0=18`, with no initial variants, becomes free A=2, free H=2, fuel 7 and
source 16. Assembly leaves fuel 5 and source 16. All original site, resident and
local-store fields remain accounted for. Handoff supplies no new resources.
The new receipt path into common fuel is an explicit interface mechanism; it
is not silently attributed to the old local-fuel capture rule.

The full construction bill is `3K+3`: formation spends `2K+3`, assembly `K`.
After construction, fuel is `F0−2K−3` and source `E0−K`. A full `N`-trial tree
can be supported by `2N` source units and `2N` common units before teaching,
in addition to the construction costs and enough constructed slots. These are
finite support requirements, not replenishment or memory renewal.

## Three events secure each admitted observation

1. **Reserve.** While idle, require a blank slot, common fuel at least two and
   source at least two. Reserve the slot, subtract two common units, spend one
   on operation and retain one in write escrow.
2. **Observe.** A zero converts two source units to common fuel; a one has no
   receipt. Latch the actual bit. No second admission can occur.
3. **Commit.** Spend the escrow unit and append the latched bit. The slot remains
   occupied by that record.

For the full recorder, each completed macro projects exactly to the existing
`prediction_step`, including fuel, source, paid count, one-target count and the
EWMA decoded from the word. This is a conditional projection for recorder-admitted
states. It is not equivalence with every old transition: at source zero the old
function can execute a realized loss branch, but a two-outcome trial is not
source-backed. The recorder therefore refuses admission there.

The checks include writing a one after reservation leaves common fuel zero.
Escrow still funds commitment. Writes before an outcome, repeated observations
or writes, and overlapping admissions are rejected. A supplied scheduler must
actually complete the admitted observation and commit; proving that commit is
enabled does not prove that every scheduler eventually executes it.

During all microstates, total stored energy includes escrow. Global accounting
includes preparation, slot assembly, every operation and every commitment. The
material ledger includes free particles, the resident, and two retained parts
per slot. Record length and popcount are mathematical readouts of the physical
bits, not additional uncharged counters whose construction has been proved.

All four two-bit words pass these checks. After `[0,1]`, the recorder has fuel 3
and source 14, so another old teacher trial is fuel-feasible. It has no blank
slot or free A/H pair, however, and cannot admit or construct a third record.
Actual part shortage remains an independent limit. The finite law has no
record damage, erasure or renewal mechanism; its proof obligation is a finite
retained prefix, not the growing `n→∞` record needed for eventual reliability.

## Dropping outcomes changes the evidence

The three controls share initial stocks, slot construction and a two-unit bill
for every actual trial. Their commitment policies differ:

| Policy | On a zero | On a one |
| --- | --- | --- |
| Full | Pay and retain it | Pay and retain it |
| Drop zero and resume | Pay, omit it, return slot to blank, continue | Pay and retain it |
| Halt on first zero | Pay, omit it, return slot to blank, stop permanently | Pay and retain it |

The halt control does **not** preserve the entire attempted word. Its record is
the genuine prefix ending before the terminal omitted zero. A false confidence
event is still an event on some actual prefix, so an anytime prefix guarantee
continues to cover it. Interior omission followed by resumed sampling instead
creates a different word. Equal retained values alone do not distinguish these
two situations; their relation to the complete physical history matters.

The stress case begins completely unformed with `K=8,F0=84,E0=72`. Formation and
assembly cost 27 out of initial energy 156, leaving common fuel 65 and source
64. Those stocks can fund every potential trial through 32 opportunities.
Targets have the supplied stationary Bernoulli parameter `beta=1/4`.

The slot-only decoder reuses the earlier dyadic lower certificate with
`alpha=1/10` and threshold one quarter:

| Policy | False certificate probability | Mean actual trials | Mean retained bits |
| --- | ---: | ---: | ---: |
| Full | `1/65536` | `8` | `8` |
| Drop zero and resume | `10469065127243216839/18446744073709551616` ≈ `0.567529` | ≈ `28.135` | ≈ `7.034` |
| Halt on first zero | `1/65536` | `21845/16384` ≈ `1.333313` | `21845/65536` ≈ `0.333328` |

The full recorder uses its eight slots and stops. Only eight consecutive ones
produce its false threshold certificate. The drop-zero recorder stores only
ones and can continue until eight are collected or 32 attempts finish. Its
false certificate probability is exactly `Pr(Binomial(32,1/4)>=8)`, exceeding
the nominal `1/10` allowance. The stationary Bernoulli premise no longer applies
to its decoded stored sequence. This does not contradict the earlier confidence
theorem.

The extra sampling has a real price. Full recording spends 16 operation/write
units; the drop-zero control spends approximately 56.270 on average; the halt
control spends `21845/8192`, approximately 2.667. Results retain every raw
attempt, zero/one count and bill through exact endpoint-history families. The
fault is never credited with cost-free missing observations. The arms have the
same price per attempt, not the same realized workload or stopping time.

The confidence decoder takes only retained bits. An observer with appropriate
initial references and current fuel/source measurements could instead recover
the raw counts from the resource ledger. This study therefore establishes a
failure of the specified record interface, not impossibility for every decoder.
No final recipient action is executed here. A false score certificate alone
does not identify a harmful action or settle an ethical question.

## Reproduce and scope

Run `python3 check.py` in this directory. [PROTOCOL.md](PROTOCOL.md) was fixed
before execution. [model.py](model.py) imports the existing formation, teacher
and certificate implementations; it does not modify them. [results.json](results.json)
contains the actual preparation paths, all two-slot microstates, guard failures,
the escrow witness, exact stress endpoint distributions and source hashes.
The stress computation uses exact rational dynamic programming, with a separate
binomial-tail reference for the displayed risk.

Independent checking is maintained by its separate owner. These Python checks
do not by themselves prove a quantified Lean theorem or construct the stored
word's decoder. They establish the specified finite mechanism and counterexamples
while retaining the supplied recipe, reliable writing, finite retention,
completion schedule, observation kernel and routing assumptions.

The separate [Lean package](formal/README.md) checks the general event-law,
record-word and completed-operation statements. The [independent checker](independent_check.py)
uses closed-form stopped-word families to compare the complete finite endpoint
distributions; its evidence is in [independent-check.json](independent-check.json).
The [integration and remaining derivation](../../../../../../../_process/research/2026-10-05-concern-theory/RECORDING-FIDELITY-INTEGRATION.md)
connect this finite result to the common roadmap, with the separate
[internal review](../../../../../../../_process/research/2026-10-05-concern-theory/RECORDING-FIDELITY-REVIEW.md)
retaining its acceptance scope.
