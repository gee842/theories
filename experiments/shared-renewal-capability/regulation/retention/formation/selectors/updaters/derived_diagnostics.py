#!/usr/bin/env python3
"""Post-result diagnostics, explicitly separate from prespecified comparisons.

The frozen-initial-type mixture is a linear contrast of already reported arms.
The inheritance path investigates the zero inherited-credit readings in the
main matrix by combining noise and short updater lifetime; it is not a new
prespecified primary comparison.
"""
import hashlib
import json
from dataclasses import replace
from fractions import Fraction as Q
from pathlib import Path
from model import Law, State, MOMENTS, advance

ROOT = Path(__file__).resolve().parent


def main():
    result_path = ROOT/'results.json'
    j = json.loads(result_path.read_text())
    contrasts = {}
    for name, case in j['cases'].items():
        a = case['arms']
        val = lambda arm: Q(a[arm]['unconditional_exact']['captures'])
        frozen = (val('fixed_random')+val('fixed_directed'))/2
        contrasts[name] = {'variable': str(val('variable')),
                           'fair_frozen_type_mixture': str(frozen),
                           'difference': str(val('variable')-frozen)}
    assert Q(contrasts['primary']['difference']) == Q(5, 144)
    assert Q(contrasts['reserve_24']['difference']) == -Q(1, 48)

    law = replace(Law(), gate_lifetime=1, availability=Q(3, 4), horizon=3, reversals=())
    s = State(14)
    probability = Q(1)
    history = []
    # Same fixed regime throughout: no environment rescue or oracle switch.
    conditions = (
        lambda t, d: t.updater == 0 and t.selector == 0 and d[MOMENTS.index('captures')] == 1,
        lambda t, d: t.gate_lease == 0 and t.lease == 1 and d[MOMENTS.index('captures')] == 0,
        lambda t, d: t.updater == 1 and t.selector == 0 and not t.used
                     and d[MOMENTS.index('inherited_selector_renewals')] == 1,
    )
    for exposure, condition in enumerate(conditions):
        choices = [(t, p, d) for t, p, d in advance(law, s, 'variable', 0, exposure%2, False)
                   if condition(t, d)]
        assert len(choices) == 1
        t, p, d = choices[0]
        probability *= p
        history.append({'before': vars(s), 'after': vars(t), 'probability':str(p),
                        'increments':{k:str(v) for k,v in zip(MOMENTS,d)}})
        s = t
    assert probability == Q(9, 512) and s.fuel == 11 and not s.witness
    record = {'status':'passed', 'design':'post-result diagnostics; not prespecified primary arms',
              'source_sha256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest()
                               for n in ('model.py','results.json','derived_diagnostics.py')},
              'frozen_initial_type_contrast':contrasts,
              'inherited_credit_witness':{'law':law.record(),
                                         'conditional_start':'commissioned reserve14, hidden regime0',
                                         'probability':str(probability), 'history':history,
                                         'claim':'new updater receives maintenance before governing the inherited selector'}}
    (ROOT/'derived-diagnostics.json').write_text(json.dumps(record,indent=2)+'\n')
    print('Passed 12 derived contrasts and paid inherited-credit path, probability',probability)


if __name__ == '__main__': main()
