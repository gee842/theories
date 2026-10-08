#!/usr/bin/env python3
"""Exact comparison with the existing executable market model, not field data."""
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
MODEL = HERE.parent/'model.py'
spec = importlib.util.spec_from_file_location('meta_market_model', MODEL)
market = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = market
spec.loader.exec_module(market)


def main():
    p = market.Parameters()
    grid = []
    for qi in range(41):
        for wi in range(41):
            q, w = F(qi,40), F(wi,40)
            s = market.State(F(1,2), q, w, F(1), (F(10),))
            t, ledger = market.step(p, s)
            expected = (F(3,4)-w/2)*q+F(1,4)
            assert t.accountability == expected
            assert (4*t.accountability-F(3,2)>0) == ((6-4*w)*q>1)
            grid.append((qi,wi))
    cases=[]
    for w in [F(0), F(7,8), F(1)]:
        s=market.State(F(1,2),F(2,5),w,F(1),(F(10),))
        t,ledger=market.step(p,s)
        cases.append({'influence':str(w),'present_gap':str(ledger['profit_gap']),
                      'next_accountability':str(t.accountability),
                      'next_gap':str(4*t.accountability-F(3,2)),
                      'next_share':str(t.renewers), 'next_support':str(t.supports[0])})
    # Independent operational reconstruction of the minimal law: explicit wear,
    # activity return and overflow, compared with the simplified closed history.
    counts=0
    for q0 in range(9):
        q=q0
        for t in range(13):
            expected=min(8,q0+t) if q0>=3 else max(0,q0-t)
            assert q==expected
            for budget in range(9):
                can_leave=any(max(0,q-u)<3 for u in range(budget+1))
                assert can_leave == (q<3 or budget>=q-2)
                counts+=1
            worn=min(1,q)
            returned=2 if q>=3 else 0
            q=min(8,q-worn+returned)
    result={'scope':'Synthetic exact arithmetic, not empirical validation or a Lean/Python refinement theorem',
            'status':'passed','market_grid_cases':len(grid),'recurrence_budget_cases':counts,
            'market_examples':cases,
            'model_sha256':hashlib.sha256(MODEL.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'diagnosis.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
