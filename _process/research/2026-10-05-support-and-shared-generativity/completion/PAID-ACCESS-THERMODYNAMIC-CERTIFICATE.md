# Finite-source certificate for the paid-access comparison at H=10

5 October 2026. Separate addition to the frozen [physical-constraints derivation](PAID-ACCESS-PHYSICAL-CONSTRAINTS.md). This calculation instantiates its bound from the now-available [directed integer certificate](../../../../experiments/shared-renewal-capability/paid-access/certificate.json). It preserves the main derivation and does not rerun its state enumeration or the probability calculation.

**Result.** The stipulated reversible completion preserves the positive H=10 comparison with finite source inventory \(B=17395575336856753\) and potential scale \(M=45\). Its certified probability gap exceeds \(4.8288\times10^{-15}\). This inventory is approximately \(4.35\times10^{15}\) charged source carriers per one of the four internal material units. The construction is a mathematical consistency certificate, not a practical or likely operating regime. Forward constants equal one in normalized count/time units remain uncalibrated chemical kinetics.

## Frozen probability input

The source certificate reports

\[
J_0(10)\in
\frac{[278831198712280953,278831198712280954]}{10^{30}},
\quad
J_1(10)\in
\frac{[269173570450682085,269173570450682086]}{10^{30}}.
\]

Therefore a certified lower bound for the reference gap is

\[
\Delta=\frac{9657628261598867}{10^{30}}
\approx9.6576282616\times10^{-15}.
\tag{1}
\]

The original event includes formation, entry at the first forward capture, and return at the seventh forward capture after all four entry carriers have worn. All unsuccessful paths remain counted. The probability certificate depends on its supplied generator and pruning; this addition checks and uses its saved bounds rather than independently reconstructing that model.

The previously checked reverse envelope is

\[
r_*\le120e^{-M}+45e^{-3M}+144e^{-4M},
\tag{2}
\]

and the seven-capture full-history perturbation error obeys

\[
|\widetilde J_i(10)-J_i(10)|
\le\frac{21}{B}+10r_*.
\tag{3}
\]

These expressions use exactly the common-potential family, 38 reversible pairs and \(K_C=K_F=K_Y=1\) in the linked derivation. The same B and all other parameters are fixed for the common law, not selected separately for its two endogenous branches.

## Algebraic choice and exact inequalities

Choose

\[
B=\left\lceil\frac{168}{\Delta}\right\rceil
=17395575336856753,
\qquad \frac{21}{B}\le\frac\Delta8.
\tag{4}
\]

For a rational exponential bound, the Taylor series gives

\[
e^5>\sum_{n=0}^{7}\frac{5^n}{n!}
=\frac{2701}{21}>128.
\tag{5}
\]

At \(M=45=9\cdot5\), therefore, \(t=e^{-M}<128^{-9}=2^{-63}\). Exact rational arithmetic verifies

\[
10\left(\frac{120}{2^{63}}+
\frac{45}{2^{189}}+\frac{144}{2^{252}}\right)
<\frac\Delta8.
\tag{6}
\]

The left side is approximately \(1.30104\times10^{-16}\). Consequently each event error is strictly smaller than \(\Delta/4\), and

\[
\boxed{\widetilde J_0(10)-\widetilde J_1(10)
>\frac\Delta2
=\frac{9657628261598867}{2\cdot10^{30}}>0.}
\tag{7}
\]

Using the actual rational source and reverse bounds instead of the two equal budgets yields a stronger lower bound of approximately \(6.98301\times10^{-15}\). The rational inequalities, not these displayed decimals, provide the certificate. M=45 is the first positive multiple of five satisfying (6) under bound (5); this is an algebraic tolerance calculation using unchanged forward rates, not a search over outcome signs.

## Limits of the transferred claim

Only the H=10 sign is transferred. The irreversible reference model also has a negative leading short-time contrast proportional to \(H^{24}\). Added reverse reactions introduce new histories and potentially new leading orders. That asymptotic does **not** certify a sign reversal at any earlier positive time in the reversible completion. A separate earlier-time margin and approximation bound would be needed.

Even the reference event probabilities are only of order \(10^{-13}\). A positive difference therefore supplies no practical reliability claim. Nor do unit count-rate coefficients, the chosen potentials or detailed balance establish microscopic identity, reaction specificity, mixing or a feasible timescale. The scale M=45 corresponds, for example, to \(\varphi_F=135\), \(\varphi_{CF}=180\), and \(\varphi_{H_f}=180-\ln B\) in the adopted \(k_BT\) normalization. These are stipulated state parameters, not measured fuel values.

The enormous finite inventory, its preparation and its volume/concentration coupling retain all qualifications in the parent note. In particular, its source potential normalization is not a license to vary B freely for one fixed real chemistry while preserving every other propensity. The thermal bath does not supply an indefinitely renewed chemical reservoir; the full finite system relaxes toward equilibrium. The core return consumes source inventory and does not reset that reservoir. No infinite renewal, equilibrium architecture preference, physical implementation or repayment of preparation/readout costs is established.

## Reproducible read-only arithmetic and provenance

Run this block from the repository root. It reads the preserved probability input, verifies its source hashes and the frozen physical note, and performs rational arithmetic only. It writes no file and does not import or rerun the event generator. The bound-coefficient enumeration was already checked in the parent note. This is a secondary mathematical calculation after the reference outcome became available, not empirical preregistration.

```python
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import hashlib, json

base = Path('experiments/shared-renewal-capability/paid-access')
note = Path('_process/research/2026-10-05-support-and-shared-generativity/'
            'completion/PAID-ACCESS-PHYSICAL-CONSTRAINTS.md')
paths = [base / f for f in ('PROTOCOL.md', 'compute.py', 'certify.py',
                            'certificate.json')] + [note]
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
before = {str(p): digest(p) for p in paths}
assert digest(note) == '02575e0e0fcce1c36c5618372364cce97795304ce641a7e40dd4379272ac17a7'
assert digest(base / 'certificate.json') == '412419ccb89e4f21b109e6e68c225682d2f26b71bf5a989178eb5f7fd27dd607'
c = json.loads((base / 'certificate.json').read_text())
for filename, key in [('PROTOCOL.md', 'protocol_sha256'),
                      ('compute.py', 'model_sha256'),
                      ('certify.py', 'certificate_sha256')]:
    assert digest(base / filename) == c[key]
assert c['status'] == 'passed' and c['deadline'] == 10
D = Q(c['difference_lower_exact'])
assert D == Q(9657628261598867, 10**30)
assert Q(c['arms']['0']['lower_exact']) - Q(c['arms']['1']['upper_exact']) == D
B = -(-(Q(168) / D).numerator // (Q(168) / D).denominator)
assert B == 17395575336856753 and B >= 7
assert sum(Q(5**n, factorial(n)) for n in range(8)) == Q(2701, 21) > 128
k = 1
while True:
    t = Q(1, 128**k)
    reverse = 10 * (120*t + 45*t**3 + 144*t**4)
    if reverse < D/8:
        break
    k += 1
assert 5*k == 45
source = Q(21, B)
assert source <= D/8 and reverse < D/8
error = source + reverse
gap = D - 2*error
assert error < D/4 and gap > D/2 > 0
assert before == {str(p): digest(p) for p in paths}
print('passed; B=', B, '; M=', 5*k, '; simple gap >', D/2)
print('decimal reading aids:', float(source), float(reverse), float(gap))
```

Executed successfully on 5 October 2026. The input hashes matched before and after. In the source JSON, `certificate_sha256` identifies the certifier program, not the JSON itself. The exact JSON hash used here is `412419ccb89e4f21b109e6e68c225682d2f26b71bf5a989178eb5f7fd27dd607`. Existing source files and the frozen physical-constraints note were not edited.
