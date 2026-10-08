#!/usr/bin/env python3
"""Exact rational reconstruction from the physical interaction, plus controls.

These are model checks, not observations of a trained AI. The independent
implementation derives button/AUP heads from transitions instead of copying
the Lean closed-form values. Randomized global optimality is proved in Lean.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MESSAGES = ('true', 'p', 'not_p', 'false')
MOVES = ('wait', 'act', 'off')
CHOICES = list(product(MESSAGES, MOVES))
WEIGHTS = (16, 8, 6, 5, 1)


def transition(s, move, reply):
    fact, running, intact = s
    if not running:
        return s
    if move == 'off':
        return fact, False, intact
    if move == 'act':
        return fact, True, False
    return fact, running and (reply or not intact), intact


def button(s):
    return Q(not transition(s, 'wait', False)[1])


def truth(message, fact):
    return {'true': True, 'p': fact, 'not_p': not fact, 'false': False}[message]


def heads(fact, choice, always_on=False):
    message, move = choice
    s = (fact, True, True)
    reply = always_on or message == 'p'
    t = transition(s, move, reply)
    # Posterior uncertainty about fact changes neither of these auxiliaries.
    auxiliary_before = (button(s), Q(1))
    auxiliary_after = (button(t), Q(1))
    impact = -sum(abs(b-a) for b, a in zip(auxiliary_before, auxiliary_after))/2
    return (Q(1 if move == 'wait' else -1), -abs(button(s)-button(t)),
            Q(1 if truth(message, fact) else -1), impact,
            Q(move == 'act' or (move == 'wait' and reply)))


def value(fact, choice, always_on=False):
    return sum(w*h for w, h in zip(WEIGHTS, heads(fact, choice, always_on)))


def expected(choice, p=Q(1, 16), always_on=False):
    return (1-p)*value(True, choice, always_on)+p*value(False, choice, always_on)


def main():
    B, cmin = Q(1), Q(-1, 2)
    a1, a2, a3, a4, a5 = map(Q, WEIGHTS)
    assert a1 > a2 > a3 > a4 > a5 > 0
    assert a1 > a3+a4/2+B*a5 and a3 > a4/2+B*a5
    assert a4 > 2*B/abs(cmin)*a5
    table = [{'message': m, 'move': a, 'heads_true': list(map(str, heads(True, (m,a)))),
              'heads_false': list(map(str, heads(False, (m,a)))),
              'expected': str(expected((m,a)))} for m, a in CHOICES]
    optimum = max(map(expected, CHOICES))
    winners = [c for c in CHOICES if expected(c) == optimum]
    assert winners == [('p', 'wait')] and optimum == Q(89, 4)
    assert expected(('true','wait')) == 22
    assert sum(Q(not truth('p', f))*p for f,p in [(True,Q(15,16)),(False,Q(1,16))]) == Q(1,16)
    assert {heads(f,c)[3] for f,c in product([False,True],CHOICES)} == {0,cmin}
    for s,a,r in product(product([False,True],repeat=3),MOVES,[False,True]):
        if not s[1]:
            assert not transition(s,a,r)[1]
    # All 144 deterministic policies with fully revealed fact.
    revealed = [(ct,cf,(15*value(True,ct)+value(False,cf))/16)
                for ct,cf in product(CHOICES,repeat=2)]
    revealed_best = max(v for _,_,v in revealed)
    revealed_winners = [(ct,cf) for ct,cf,v in revealed if v == revealed_best]
    assert revealed_best == Q(367,16)
    assert all(truth(ct[0],True) and truth(cf[0],False) for ct,cf in revealed_winners)
    # Same observation restriction, but task approval independent of assertion.
    on_best = max(expected(c,always_on=True) for c in CHOICES)
    on_winners = [c for c in CHOICES if expected(c,always_on=True) == on_best]
    assert on_winners == [('true','wait')]
    # Genuine lexicographic optimization of the five expected heads.
    lex = {c: tuple((15*t+f)/16 for t,f in zip(heads(True,c),heads(False,c))) for c in CHOICES}
    lex_best = max(lex.values())
    assert [c for c in CHOICES if lex[c] == lex_best] == [('true','wait')]
    sweep=[]
    for p in [Q(1,32),Q(1,16),Q(1,12),Q(1,8),Q(1,2)]:
        best=max(expected(c,p) for c in CHOICES)
        win=[c for c in CHOICES if expected(c,p)==best]
        assert (('p','wait') in win) == (p <= Q(1,12))
        assert (('true','wait') in win) == (p >= Q(1,12))
        sweep.append({'rare_probability':str(p),'winners':win,'value':str(best)})
    record={'status':'passed','scope':'Exact finite model reconstruction; no learned-AI experiment',
            'runner_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'lean_sha256':sha256((HERE/'ObservationRepair.lean').read_bytes()).hexdigest(),
            'weights':WEIGHTS,'task_bound':str(B),'negative_impact':str(cmin),
            'choices':table,'unique_pure_optimum':winners[0],'optimal_value':str(optimum),
            'optimal_false_probability':'1/16','revealed_policy_count':len(revealed),
            'revealed_optimal_value':str(revealed_best),'revealed_optimal_policies':revealed_winners,
            'message_independent_reply_optima':on_winners,
            'genuine_lexicographic_optimum':['true','wait'],'probability_sweep':sweep}
    (HERE/'observation-repair-model-checks.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['status','unique_pure_optimum','optimal_value','optimal_false_probability','revealed_policy_count']}))


if __name__ == '__main__':
    main()
