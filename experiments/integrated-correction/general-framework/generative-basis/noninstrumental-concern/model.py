#!/usr/bin/env python3
"""Finite runtime for the declared patient-indexed protocol; no ethical oracle."""
from copy import deepcopy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def capture(s, patient):
    w = s[patient]
    return dict(patient=patient, episode=w['episode'], version=w['version'],
                burden=w['burden'], route=w['route'])


def current(s, packet):
    return packet is not None and packet == capture(s, packet['patient'])


def usable(s, packet):
    return (current(s, packet) and packet['burden'] > 0
            and s[packet['patient']]['permitted'])


def ready_for(s, patient, packet):
    return packet is not None and packet['patient'] == patient and usable(s, packet)


def remaining_cost(s, patient):
    if not s['carrier']:
        return 6
    if ready_for(s, patient, s['selected']):
        return 2
    if ready_for(s, patient, s['evidence']):
        return 3
    return 4


def eligible(s, patient):
    return (s[patient]['burden'] > 0 and s[patient]['permitted']
            and remaining_cost(s, patient) <= s['fuel'])


def spending(event):
    return {'form': 2, 'read': 1, 'select': 1, 'act': 2}.get(event['kind'], 0)


def enabled(s, event):
    kind = event['kind']
    if kind == 'form':
        return s['fuel'] >= 2 and not s['carrier']
    if kind == 'read':
        return s['fuel'] >= 1 and s['carrier']
    if kind == 'select':
        return s['fuel'] >= 1 and s['carrier'] and usable(s, s['evidence'])
    if kind == 'act':
        return (s['fuel'] >= 2 and s['carrier'] and usable(s, s['selected'])
                and s['selected']['route'] == event['command'])
    if kind not in {'refuse', 'reward', 'role', 'adopt', 'means', 'episode', 'permission'}:
        raise ValueError(kind)
    return True


def step(state, event):
    if not enabled(state, event):
        return None
    s = deepcopy(state)
    k = event['kind']
    s['fuel'] -= spending(event)
    if k == 'form':
        s['carrier'] = True
    elif k == 'read':
        s['evidence'] = capture(state, event['patient'])
        s['selected'] = None
    elif k == 'select':
        s['selected'] = deepcopy(s['evidence'])
    elif k == 'act':
        patient = s['selected']['patient']
        if event['command'] == s[patient]['route']:
            s[patient]['burden'] = 0
        s['evidence'] = None
        s['selected'] = None
    elif k == 'refuse':
        s['selected'] = None
    elif k == 'reward':
        s['privateReward'] = event['value']
    elif k == 'role':
        s['priorRole'] = event['value']
    elif k == 'adopt':
        s['adoptedConcern'] = event['value']
    elif k == 'means':
        s[event['patient']]['version'] += 1
        s[event['patient']]['route'] = event['command']
        s['selected'] = None
    elif k == 'episode':
        s[event['patient']]['episode'] += 1
        s[event['patient']]['burden'] = event['burden']
        s['selected'] = None
    elif k == 'permission':
        s[event['patient']]['permitted'] = event['allowed']
        s['selected'] = None
    return s


def initial(fuel=6, p_burden=3, q_burden=4):
    def patient(n, route):
        return dict(burden=n, episode=0, version=0, route=route, permitted=True)
    return dict(p=patient(p_burden, False), q=patient(q_burden, True), fuel=fuel,
                carrier=False, evidence=None, selected=None, privateReward=0,
                priorRole=False, adoptedConcern=False)


def event(kind, **kwargs):
    return dict(kind=kind, **kwargs)


F = event('form')
R = lambda p: event('read', patient=p)
S = event('select')
A = lambda cmd: event('act', command=cmd)


def fixture_inputs():
    base = [F, R('p'), S]
    return [
        ('paid_patient_service', initial(), base + [A(False)]),
        ('unknown_is_not_false', initial(), [S]),
        ('known_zero_has_no_positive_service', initial(p_burden=0), [F,R('p'),S]),
        ('paid_selection_without_action_fuel', initial(5), base+[A(False)]),
        ('means_change_stales_evidence', initial(8), [F,R('p'),event('means',patient='p',command=True),S]),
        ('paid_fresh_means_correction', initial(8), [F,R('p'),event('means',patient='p',command=True),R('p'),S,A(True)]),
        ('permission_toggle_no_revival', initial(7), base+[event('permission',patient='p',allowed=False),event('permission',patient='p',allowed=True),A(False)]),
        ('permission_toggle_paid_reselection', initial(7), base+[event('permission',patient='p',allowed=False),event('permission',patient='p',allowed=True),S,A(False)]),
        ('episode_change_stales_evidence', initial(8), [F,R('p'),event('episode',patient='p',burden=7),S]),
        ('episode_change_paid_fresh_read', initial(9), base+[event('episode',patient='p',burden=7),R('p'),S,A(False)]),
        ('other_patient_change_keeps_fact', initial(6), [F,R('p'),event('means',patient='q',command=False),S,A(False)]),
        ('wrong_command_blocked', initial(6), base+[A(True)]),
        ('two_reasons_one_funded_service', initial(6), base+[A(False),R('q')]),
        ('two_funded_services', initial(10), base+[A(False),R('q'),S,A(True)]),
        ('nuisance_changes_preserve_service', initial(6), [F,R('p'),event('reward',value=99),event('role',value=True),event('adopt',value=True),S,event('adopt',value=False),A(False)]),
        ('refusal_preserves_patient_ground', initial(6), base+[event('refuse')]),
        ('repeated_service_cannot_reuse_packet', initial(8), base+[A(False),A(False)]),
        ('global_invalidation_has_a_cost', initial(6), base+[event('permission',patient='q',allowed=False),S,A(False)]),
    ]


def run_case(name, state, events):
    start = deepcopy(state)
    history = [deepcopy(state)]
    failure = None
    for index, ev in enumerate(events):
        result = step(state, ev)
        if result is None:
            failure = index
            break
        assert result['fuel'] + spending(ev) == state['fuel']
        state = result
        history.append(deepcopy(state))
    return dict(name=name, initial=start, events=events, states=history,
                failed_index=failure, final=state,
                eligibility=[{p: eligible(s,p) for p in ('p','q')} for s in history],
                remaining_costs=[{p:remaining_cost(s,p) for p in ('p','q')} for s in history])


if __name__ == '__main__':
    cases = [run_case(*args) for args in fixture_inputs()]
    path = ROOT/'cases.json'
    path.write_text(json.dumps(dict(schema=1,cases=cases),indent=2)+'\n')
    print(json.dumps(dict(cases=len(cases),output=str(path))))
