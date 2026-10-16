# Paid evidence at a later concern decision

6 October 2026. A finite exact composition of the [existing paid prediction
process](../README.md) with a separate, affordable next action. It supplies a
model-score reliability criterion toward the concern study's
[pathwise choice condition](../../../../../../../_process/research/2026-10-05-concern-theory/learning-formal.md),
under additional supplied counter, certificate and routing mechanisms.
Correspondence and efficacy are fixed at `g=z=1`; their formation and calibration
are not derived here. This is executable rational arithmetic, not a Lean proof
or an empirical observation.

The earlier [adaptive-evidence study](../../../../../../history/2026-10-05-general-framework/reproduction-test/adaptive-evidence/FORMAL.md)
already establishes the role of retained evidence, confidence budgets and
stationarity. This study does not count those methods as a new discovery. Its
new interface carries the actual paid teacher's resource state into a later
recipient decision and tests that decision on individual histories.

## Same paid observations, different retained evidence

Every acquired target uses the unchanged parent `prediction_step`: prepay two
common units, receive two from the counted source on a zero target and none on
a one target, and write the measured loss. Initial source is `2T`. The stored
count `s` equals `(initial common fuel − current common fuel)/2`; paid count `n`
equals half the decrease in total common-plus-source stock before the terminal
action. Actual acquired measurements, counters and writes are supplied apparatus;
the ledger identities alone do not construct a sensor.

The comparators use the same observations and price:

- The original gain-one-quarter EWMA retains the order of the acquired targets.
- A supplied count circuit stores `n,s` and uses `s/n`, or zero before observation.
- A supplied certificate circuit uses the exact binomial upper tail to produce
  a lower bound `L(n,s)` under the stationary Bernoulli model.

For `n>=1`, the grid denominator is the largest power of two no greater than
`n`. The certificate takes the largest grid candidate whose upper tail at `s`
is at most `alpha/[n(n+1)]`, defaulting to zero. The single stream receives
`alpha=1/10`; resource stopping never restarts that allowance. A model with
three unknown coordinates would need to split the budget. The controller uses
only the recorded counts and its supplied table, never the enumerator's hidden
`beta` parameter.

Both counters have predeclared capacity `0..T`, costing `ceil(log2(T+1))` bits
each. The common two-unit price includes one operation unit and one unit for
observation, writing and computation, assumed sufficient for either finite
circuit. A finite certificate table, confidence-budget bookkeeping and routing
records are also supplied. This price does not establish free memory, a
size-independent implementation, construction of the circuits, or indefinite
maintenance. No claim extends this finite capacity to an infinite run.

## A separate next action, with its own bill

After evidence acquisition ends, a new recipient state has adverse outcome
four. The supplied interface is `g=z=1, b=0, H=4, a=1`, making strict preference
`estimate>1/4`. Protect additionally requires one currently available common
unit, consumes it, and sets the recipient outcome to zero. Wait costs zero and
leaves outcome four. There is no terminal return to finance that action, and a
tie selects Wait. Earlier training shortfalls are retained; this later action
does not protect past outcomes retroactively.

Exact delivered-Protect probabilities over 16 opportunities are:

| Target parameter | Initial common fuel | EWMA | Raw count | Certificate |
| --- | ---: | ---: | ---: | ---: |
| `1/2` | 33 | `29271/32768` | `63019/65536` | `697/65536` |
| `1/2` | 16 | `20195/65536` | `2977/8192` | `0` |
| `1/2` | 17 | `29699/32768` | `63019/65536` | `1/256` |
| `1/4` | 33 | `989350265/2147483648` | `1588338283/4294967296` | `16249/4294967296` |
| `1/8` | 3 | `0` | `169/512` | `0` |

The 16- and 17-unit cases have identical acquired-history laws. At the eighth
loss both stop acquiring observations; only the latter retains an action unit.
Certificate preference occurs with probability `1/256` in both cases, while
delivery changes from zero to `1/256`. Thus evidence and usable action support
remain separate inputs.

With three initial units, acquisition stops after the first loss. Under
`beta=1/8`, raw-count preference occurs if that loss arrives among the first
three observations, with exact probability `1-(7/8)^3=169/512`. The original
EWMA reaches exactly one quarter after its sole loss and never passes the
strict threshold. This is an explicit selection effect from resource-dependent
stopping, not a valid substitution of a population mean into a pathwise theorem.

The certificate is very conservative in this short fixture. Even at `beta=1/2`
with every bill funded, it delivers protection only about **1.06%** of the time.
Its expected terminal recipient outcome is `64839/16384` (about **3.96**), versus
`2517/16384` (about **0.154**) for raw count. Every delivered repair physically
helps under the supplied efficacy of one. Confidence control concerns the
claim that the true model score exceeds the private-cost threshold; it is not
an optimal-protection rule, a certificate of ethical permissibility, or an
unqualified safety improvement. Withholding uncertified action still leaves
recipient outcome four.

At the true-score boundary `beta=1/4`, the certificate's final false-threshold
probability is `16249/4294967296`; its probability of any false lower certificate
along the paid history is `415/16777216`. Both are nonzero. An all-one sample
of length 16 alone has probability `1/4^16` under that boundary law and receives
lower bound `9/16`. Finite evidence therefore does not provide zero-error
identification when opposite models have overlapping finite histories.

## Paid counterexamples to durability and stale transfer

A fully paid history of 16 one targets followed by five zero targets starts
with fuel 43 and source 42. It ends with fuel 11 and source 32, before the
separate terminal bill. Five zeros reduce any preceding EWMA in `[0,1]` to at
most `243/1024<1/4`. The exact history has positive probability `2^-21` under
the stationary half-target law. A favorable stationary mean therefore cannot
guarantee strict preference on every paid history.

The same observed zeros can follow a change to `beta=0` after sample 16. The
retained certificate remains `5/16` after all five zeros, although the current
model score is now zero. This violates the certificate's stationarity premise;
it is not a counterexample to stationary coverage. Accumulated evidence needs
a justified response to model change, and old confidence must not be treated
as validation of a new regime.

These finite histories do not establish or refute an infinite funded-learning
theorem. An infinite claim separately needs continuing observations, valid
calibration, support for the growing record and affordable actions. The
[concern dynamics](../../../../../../../_process/research/2026-10-05-concern-theory/dynamics-formal.md)
also retain teaching interpretation, shared routing, efficacy, maintenance and
succession as substantive conditions. This package does not derive felt valence,
recognition of another center, or ethical standing from fuel losses.

## Reproduce and audit

Run `python3 check.py` in this directory. [PROTOCOL.md](PROTOCOL.md) fixes the
five cases and negative witnesses; [model.py](model.py) imports the parent
transition without editing it. A count/resource-state dynamic program computes
exact stopped probabilities. Exact weighted-subset counting reconstructs EWMA
threshold frequencies without listing all primary outcome words. The producer
also checks 45 small full-word count identities and 96 fixed-sample coverage
cases, plus stock, counter-capacity and terminal-action ledgers.

[results.json](results.json) preserves exact results and hashes of the producer,
checker, protocol and upstream transition source. Separate independent checking
and review are recorded by their owner; the producer's checks alone do not
constitute independent validation.
