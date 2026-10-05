# Formed prediction-to-action coupling

6 October 2026. Exact finite construction for **acquired prediction → paid
formation and consequence-dependent revision of its action coupling**. The
[protocol](PROTOCOL.md) was saved before the results. The [mathematical
account](../../../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-COUPLING-MATH.md)
gives the conditional theorem, resource bound and premise ledger.

The parent's actual formation/repair/capture/adapter process reaches the
commissioned entrance with probability 2/9. This experiment uses the parent's
fixed-Fast predictor implementation and pays for every original component and
its renewal. A new paid normal/inverted output switch can be replaced while
the acquired register and its enclosing circuit remain. Actual capture pays
for switch maintenance; failures exhaust it. No performance score chooses the
switch. The switch recipe and extra functional capacity inside the composite
circuit are explicit additional local assumptions.

## Results

The primary case starts with thirty common fuel units and eighty-one source
units, before original formation. Eight post-commissioning opportunities
include a reversal after four. All figures below include unsuccessful
preparations and operational collapse.

| Mechanism | Expected captures | Strict same-memory coupling-revision probability |
|---|---:|---:|
| Variable paid switch | 37/36 | 1/18 |
| Conventional finite-state realization | 37/36 | 1/18 |
| Fixed normal, all hardware bills paid | 13/9 | 0 |
| Fixed inverted, all hardware bills paid | 1/9 | 0 |
| Outcome-blind switch maintenance | 7/9 | 0 |

The conventional realization agrees on the full recorded finite distribution.
Fixed normal performs better in this primary comparison. A zero revision
witness is not a failure to obtain support: the witness deliberately requires
an actual coupling change. Outcome-blind renewal keeps paying for unproductive
couplers and can prevent their replacement; its extra realized maintenance
expense is part of the intervention.

The strict witness requires prior acquired confident memory, an old failed
command with unchanged q, paid opposite-switch formation in the same circuit,
and a later different command obtaining a packet that pays the new switch's
renewal. One complete three-exposure prefix has unconditional probability 1/72.
It ends at fuel 8, q=4, last=1, circuit/updater/coupler lifetimes 6/2/2, and five
remaining ten-unit source packets. Its full account is

    111 = 4 preparation + 1 adapter + 28 operation + 20 lost source + 58 remaining.

Immediately before its third exposure, six inherited fuel units cannot pay
the next successful attempt; seven allow it with probability one half. The
updater replacement, coupler replacement, record retention and work cost
2+1+1+3 before the packet arrives.

Failures are retained in [all seven cases](results.json). With initial common
reserve twelve, every commissioned circuit spends its available reserve before
it can execute a trial. With circuit lifetime two, the strict witness is zero:
the enclosing record is replaced too soon for this same-memory switch revision.
With coupler lifetime one, the primary witness increases from 1/18 to 5/48,
while captures decrease from 37/36 to 41/48. More revision is not a general
performance improvement. Outages cause the inherited receipt decoder to make
actual errors; available support is never replaced with the hidden correct
answer.

## Reproduce and inspect

Run from this directory:

```sh
python3 model.py
python3 check.py
```

[model.py](model.py) computes 35 exact case/arm combinations.
[check.py](check.py) independently implements the operational successor by
enumerating exogenous draws and mutating a separate record. It agrees on all
**1,968 distinct reachable marked kernels and 2,566 marked branches**. A separate
forward enumeration directly writes the old positive reaction channels and
matches every preparation terminal state and probability. It also checks
**3,936** configurations of the stable-record recovery formula and the exact
complete witness. The checker uses the producer's forward moment summation
driver after verifying each marked kernel; it is not a separately written
aggregate dynamic program. [verification.json](verification.json) states this
scope and retains the full witness.

Both outputs include hashes of this implementation, the prespecified protocol
and every imported predecessor source. Runs fail if those sources change
during calculation. The independent record also hashes its checker. These are
internal exact model checks, not empirical evidence or a new Lean certificate.

For downstream composition, `prepare(law)` retains every preparation outcome;
`evolve(law, arm, reserve)` returns the complete terminal distribution keyed by
initial regime and `State`. Each mass has cumulative unnormalized ledger marks.
`terminal_records(...)` exports the complete state, final regime, probability
and **conditional mean** ledger marks. The export describes merged terminal
histories, so those means must not be presented as an individual history's
event count. Include unsuccessful preparation mass and source remainder when
joining a later process; do not restart from the original reserve. The primary
variable arm has active written memory with unconditional probability 1/6.

The model supplies a finite consequence-mediated sign of prediction use. It
does not derive intrinsic experience, all possible action couplings, concern,
ethical justification or an empirical chemistry. A later other-directed
extension must explicitly preserve the patient's distinct state, explain any
shared routing, and include every available omission or bypass.
