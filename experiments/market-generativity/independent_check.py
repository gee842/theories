#!/usr/bin/env python3
"""Independent equation/ledger reconstruction; imports no model or runner code.

Exact rational local verification and 120-digit replay of saved 80-digit paths.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from itertools import product
from pathlib import Path
import csv
import hashlib
import json

HERE = Path(__file__).resolve().parent
REPORT = HERE / 'results' / 'verification.json'
CSV = HERE / 'results' / 'trajectories.csv'
F = Fraction


def number(value, kind):
    rat = F(str(value))
    if kind is F:
        return rat
    return Decimal(rat.numerator) / Decimal(rat.denominator)


def decode(p, s, options, kind):
    pp = {key: number(value, kind) for key, value in p.items() if key != 'supports'}
    pp['supports'] = [{key: value if key == 'essential' else number(value, kind)
                       for key, value in support.items()} for support in p['supports']]
    ss = tuple(number(s[key], kind) for key in
               ('renewers', 'accountability', 'influence', 'fund'))
    ss += (tuple(number(value, kind) for value in s['supports']), s['operating'])
    opts = {'authorized': options.get('authorized', True),
            'freeze_rule': options.get('freeze_rule', False),
            'erosion': number(options.get('erosion', 0), kind),
            'losses': tuple(number(value, kind) for value in
                            options.get('losses', [0] * len(pp['supports'])))}
    return pp, ss, opts


def advance(p, state, opt):
    """Reconstruct from balances; state order is x, q, w, B, supports, active."""
    x, q, w, bank, stocks, active = state
    zero = bank * 0
    if not active:
        return state, {'paid': False, 'cash_residual': zero, 'fund_residual': zero}
    assert all(not support['essential'] or c >= support['floor']
               for c, support in zip(stocks, p['supports']))
    paid = opt['authorized'] and bank >= p['correction_cost']
    spent = p['correction_cost'] if paid else zero
    sanction = p['liability'] * q
    profit_r = p['price'] - p['levy'] - p['renewal_cost']
    profit_e = p['price'] - p['levy'] - p['political_cost'] - sanction
    gap = profit_r - profit_e
    xn = x + p['selection_rate'] * x * (1-x) * gap
    wn = w + p['influence_turnover'] * (p['influence_target'] * (1-x) - w)
    qn = q + (p['restoration'] * (1-q) if paid else zero)
    qn -= p['capture'] * w * q + opt['erosion']
    qn = min(1, max(0, qn))
    if opt['freeze_rule']:
        qn = q
    pre_cap = bank + p['levy'] - spent
    overflow = max(0, pre_cap - p['fund_cap'])
    bn = pre_cap - overflow
    cn = tuple(max(0, c - spec['depreciation'] * c
                       + spec['renewal'] * x - spec['depletion'] * (1-x)
                       - spec['background_harm'] - loss)
               for c, spec, loss in zip(stocks, p['supports'], opt['losses']))
    alive = all(not spec['essential'] or c >= spec['floor']
                for c, spec in zip(cn, p['supports']))
    distributed = x * profit_r + (1-x) * profit_e
    outlays = (p['levy'] + (1-x)*sanction + (1-x)*p['political_cost']
               + x*p['renewal_cost'] + distributed)
    ledger = {'paid': paid, 'gap': gap, 'cash_residual': p['price'] - outlays,
              'fund_residual': bank + p['levy'] - bn - spent - overflow}
    return (xn, qn, wn, bn, cn, alive), ledger


def in_high(s):
    x, q, w, bank, stocks, active = s
    return active and F(3,4) <= x <= 1 and F(1,2) <= q <= 1 \
        and 0 <= w <= F(1,4) and 1 <= bank <= 3 and stocks[0] >= 5


def exact_tests(saved):
    base = saved['scenarios']['renewal_basin']
    p, _, opt = decode(base['parameters'], base['initial'], {}, F)
    count = 0
    for x,q,w,bank,c,e,loss in product(
        (F(3,4),F(7,8),F(1)), (F(1,2),F(3,4),F(1)),
        (F(0),F(1,8),F(1,4)), (F(1),F(2),F(3)), (F(5),F(8),F(20)),
        (F(0),F(1,40),F(1,20)), (F(0),F(1,4),F(1,2))):
        state = (x,q,w,bank,(c,),True)
        new, ledger = advance(p, state, dict(opt, erosion=e, losses=(loss,)))
        assert in_high(new) and new[0] >= x
        assert ledger['cash_residual'] == ledger['fund_residual'] == 0
        count += 1
    assert count == saved['exact_checks']['rational_rectangle_points'] == 2187
    expected = {
        'high_worst': ((F(3,4),F(1,2),F(1,4),F(1),(F(5),),True),
                       dict(opt,erosion=F(1,20),losses=(F(1,2),)),
                       (F(123,160),F(41,80),F(1,4),F(1),(F(21,4),),True)),
        'outside_rectangle_recovery':
                      ((F(4,5),F(49,100),F(13,50),F(1),(F(5),),True),
                       dict(opt,erosion=F(1,20),losses=(F(1,2),)),
                       (F(2546,3125),F(2519,5000),F(49,200),F(1),(F(27,5),),True)),
        'negative_gap_recovery':
                      ((F(4,5),F(7,20),F(1,20),F(1),(F(5),),True),opt,
                       (F(498,625),F(403,800),F(7,80),F(1),(F(59,10),),True)),
    }
    for label,(initial,options,want) in expected.items():
        got, ledger = advance(p,initial,options)
        assert got == want, (label,got,want)
        assert ledger['cash_residual'] == ledger['fund_residual'] == 0
    broad_count = 0
    for x,q,w,bank,c,e,loss,authorized in product(
        (F(0),F(1,10),F(3,4),F(4,5),F(1)),
        (F(0),F(7,20),F(3,8),F(1,2),F(1)),
        (F(0),F(1,4),F(9,10),F(1)), (F(0),F(1,2),F(1),F(3)),
        (F(5),F(8),F(100)), (F(0),F(1,20),F(1,2)),
        (F(0),F(1,2),F(5)), (False,True)):
        state=(x,q,w,bank,(c,),True)
        got,ledger=advance(p,state,dict(opt,erosion=e,losses=(loss,),authorized=authorized))
        assert all(0 <= v <= 1 for v in got[:3])
        assert 0 <= got[3] <= 3 and got[4][0] >= 0
        assert ledger['cash_residual'] == ledger['fund_residual'] == 0
        if not got[-1]:
            terminal, post = advance(p,got,opt)
            assert terminal == got and not post['paid']
        broad_count += 1
    history_count=0
    for spec in saved['scenarios'].values():
        pp,ss,options=decode(spec['parameters'],spec['initial'],spec['options'],F)
        for _ in range(4):
            ss,ledger=advance(pp,ss,options)
            assert ledger['cash_residual'] == ledger['fund_residual'] == 0
            history_count += 1
    return {'primary_rectangle_points':count,'broader_domain_and_ledger_points':broad_count,
            'exact_short_history_steps':history_count,'exact_boundary_witnesses':list(expected)}


def replay(saved):
    by_name={name:[] for name in saved['scenarios']}
    with CSV.open(newline='') as stream:
        for row in csv.DictReader(stream):
            by_name[row['scenario']].append(row)
    outcomes={}
    maximum_error=Decimal(0)
    scalar_comparisons=0
    with localcontext() as ctx:
        ctx.prec=120
        tol=Decimal('1e-68')
        for name,spec in saved['scenarios'].items():
            p,state,opt=decode(spec['parameters'],spec['initial'],spec['options'],Decimal)
            failed=None
            violated=None
            paid=0
            minimum=list(state[4])
            rows=by_name[name]
            assert len(rows)==saved['horizon']+1
            for t,row in enumerate(rows):
                assert int(row['t'])==t
                assert state[-1]==(row['operating']=='True'),(name,t,'active')
                scalars=state[:4]+state[4]
                columns=('x','q','w','B','C')+ (('recipient',) if len(state[4])>1 else ())
                for value,column in zip(scalars,columns):
                    error=abs(value-Decimal(row[column]))
                    maximum_error=max(maximum_error,error)
                    assert error < tol,(name,t,column,str(error))
                    scalar_comparisons+=1
                if failed is None and not state[-1]: failed=t
                if violated is None and any(c < s['floor'] for c,s in zip(state[4],p['supports'])):
                    violated=t
                minimum=[min(a,b) for a,b in zip(minimum,state[4])]
                if t != saved['horizon']:
                    state,ledger=advance(p,state,opt)
                    assert abs(ledger['cash_residual'])<Decimal('1e-110')
                    assert abs(ledger['fund_residual'])<Decimal('1e-110')
                    paid+=int(ledger['paid'])
            assert failed==spec['first_economic_failure'],name
            assert violated==spec['first_any_support_violation'],name
            assert paid==spec['paid_rounds'],name
            assert all(abs(a-Decimal(b))<tol for a,b in zip(minimum,spec['minimum_supports']))
            outcomes[name]={'first_economic_failure':failed,
                            'first_any_support_violation':violated,'paid_rounds':paid}
    return {'precision':120,'saved_precision':saved['precision'],'horizon':saved['horizon'],
            'scalar_comparisons':scalar_comparisons,'comparison_tolerance':'1e-68',
            'maximum_absolute_error':str(maximum_error),'outcomes':outcomes}


def main():
    saved=json.loads(REPORT.read_text())
    result={'status':'passed','scope':'Independent equations; no imports from model.py or run.py.',
            'exact':exact_tests(saved),'trajectory_replay':replay(saved)}
    result['sha256']={str(path.relative_to(HERE)):hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in (HERE/'model.py',HERE/'run.py',REPORT,CSV,Path(__file__))}
    (HERE/'results'/'independent-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
