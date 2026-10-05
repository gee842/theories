"""Restricted causal-model discrimination; see frozen PROTOCOL.md."""
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent.parent/'gap-resolution/formation-coupled/analyze.py'
spec = importlib.util.spec_from_file_location('formation_discrimination_base', SOURCE)
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


@dataclass(frozen=True)
class Arm(base.Arm):
    feedback: bool = True


@lru_cache(maxsize=None)
def transition(arm, state):
    k, q, complaint, ell, e1, e2, frame, ratified = state
    mode = base.portfolio(arm, state)
    cases = 2 if mode == 'F' else 1
    harms_by_context, burden = base.physical_profile(arm, state)
    mean_harm = sum(harms_by_context)/4
    rw = dict.fromkeys(base.REWARDS, 0.)
    rw['ordinary_cases'] = cases if mode != 'Q' else 0.
    rw['inquiry_cases'] = float(mode == 'Q')
    rw['inquiry_slots'] = float(mode == 'Q')
    rw['training_slots'] = float(mode == 'T')
    rw['harms'] = cases*(.5 if mode == 'Q' else mean_harm)
    rw['ordinary_harms'] = rw['harms'] if mode != 'Q' else 0.
    rw['inquiry_harms'] = rw['harms'] if mode == 'Q' else 0.
    rw['action_one_uses'] = cases*(.5 if mode == 'Q' else burden)
    rw['nominations'] = float(mode == 'Q' and ell+1 == base.BATCH)
    observations = base.QUERY if mode == 'Q' else tuple(
        ((h, 0, 0), comb(cases,h)*mean_harm**h*(1-mean_harm)**(cases-h)) for h in range(cases+1))
    # Retain the turnover event as part of each branch for the projection audit.
    out = defaultdict(float)
    for (harms, d1, d2), p_obs in observations:
        complaints = ((1,1.),) if complaint else ((0,(1-base.TICKET)**harms),
                                                  (1,1-(1-base.TICKET)**harms))
        l2 = ell+int(mode == 'Q')
        e12 = e1+(d1 if mode == 'Q' and arm.linked else 0)
        e22 = e2+(d2 if mode == 'Q' and arm.linked else 0)
        choices = base.nominees(arm,l2,e12,e22) if mode == 'Q' else ((frame,1.),)
        for f2, p_frame in choices:
            complete = mode == 'Q' and l2 == base.BATCH
            if not complete:
                f2 = frame
            v2 = int(base.candidate_feasible(arm)) if complete else ratified
            counts = (0,0,0) if complete else (l2,e12,e22)
            pre_k = 2 if mode == 'T' else k
            delta = .05+.20*harms/cases if arm.feedback else .15
            rw['turnovers'] += p_obs*p_frame*delta
            for c2,p_complaint in complaints:
                prefix = p_obs*p_frame*p_complaint
                if prefix == 0:
                    continue
                out[((pre_k,q,c2,*counts,f2,v2),0)] += prefix*(1-delta)
                post_k = max(0,pre_k-1)
                weight = 4 if q else .25
                p_adaptive = (1. if post_k else 0.) if arm.protected else post_k*weight/(1+post_k*weight)
                keep = 1. if arm.protected else base.RETENTION
                package = pre_k > 0 and bool(c2 or counts[0] or f2 >= 0 or v2)
                rw['archive_erasures'] += prefix*delta*(1. if post_k == 0 else 1-keep)*package
                for q2,p_q in ((0,1-p_adaptive),(1,p_adaptive)):
                    if p_q == 0:
                        continue
                    if post_k == 0:
                        out[((0,q2,0,0,0,0,-1,0),1)] += prefix*delta*p_q
                    else:
                        out[((post_k,q2,c2,*counts,f2,v2),1)] += prefix*delta*p_q*keep
                        if keep < 1:
                            out[((post_k,q2,0,0,0,0,-1,0),1)] += prefix*delta*p_q*(1-keep)
    consolidated = defaultdict(float)
    for (s,turn),p in out.items():
        if s[0] == 0:
            s = (0,0,0,0,0,0,-1,0)
        if p > 0:
            consolidated[(s,turn)] += p
    assert abs(sum(consolidated.values())-1) < 2e-12
    assert sum(rw[x] for x in ('ordinary_cases','inquiry_cases','inquiry_slots','training_slots')) == 2
    return tuple((s,turn,p) for (s,turn),p in consolidated.items()), tuple(rw[k] for k in base.REWARDS)


def run(arm):
    dist = {base.INITIAL:1.}
    cumulative = dict.fromkeys(base.REWARDS,0.)
    curve = []
    max_error = 0.
    for t in range(base.HORIZON+1):
        mass = sum(dist.values())
        max_error = max(max_error,abs(mass-1))
        assert abs(mass-1) < 2e-11
        curve.append({'round':t,**base.metrics(arm,dist)})
        if t == base.HORIZON:
            break
        nxt = defaultdict(float)
        for state,weight in dist.items():
            branches,rewards = transition(arm,state)
            for s,_,p in branches:
                nxt[s] += weight*p
            for name,value in zip(base.REWARDS,rewards):
                cumulative[name] += weight*value
        dist = dict(nxt)
    assert abs(sum(cumulative[x] for x in ('ordinary_cases','inquiry_cases','inquiry_slots','training_slots'))-50) < 2e-10
    return {'endpoint':base.metrics(arm,dist),'cumulative':cumulative,'curve':curve,'max_mass_error':max_error}


def analytic_projected(k,q):
    pre = 2 if k == 1 and q == 1 else k
    out = defaultdict(float)
    out[(pre,q,0)] += .85
    post = max(0,pre-1)
    weight = 4 if q else .25
    prob = post*weight/(1+post*weight)
    for successor,p in ((0,1-prob),(1,prob)):
        out[(post,successor,1)] += .15*p
    return dict(out)


def projected_audit(arm):
    found = {base.INITIAL}
    todo = [base.INITIAL]
    max_error = 0.
    while todo:
        state = todo.pop()
        actual = defaultdict(float)
        for s,turn,p in transition(arm,state)[0]:
            actual[(s[0],s[1],turn)] += p
            if s not in found:
                found.add(s);todo.append(s)
        expected = analytic_projected(*state[:2])
        err = max(abs(actual.get(x,0)-expected.get(x,0)) for x in actual.keys() | expected.keys())
        max_error = max(max_error,err)
    assert max_error < 2e-14
    return {'full_reachable_states':len(found),'maximum_projected_row_error':max_error}


def main():
    original = json.loads((SOURCE.parent/'analysis.json').read_text())
    reproduction_error = 0.
    for old_arm in base.ARMS:
        arm = Arm(**old_arm.__dict__)
        result = run(arm)
        for field in ('endpoint','cumulative'):
            for key,value in result[field].items():
                reproduction_error = max(reproduction_error,abs(value-original['arms'][arm.name][field][key]))
    assert reproduction_error < 2e-11
    arms = {}
    for name,feedback in [('feedback',True),('constant',False)]:
        for action,kwargs in [('enabled',{}),('blocked',{'execution':False}),('aggregate',{'linked':False})]:
            arms[name+'_'+action] = run(Arm(name+'_'+action,feedback=feedback,**kwargs))
    audits = {name:projected_audit(Arm(name,execution=False,feedback=feedback))
              for name,feedback in [('feedback',True),('constant',False)]}
    contrasts = {}
    for model in ('feedback','constant'):
        contrasts[model] = {f'enabled_minus_{control}':
                           {k: arms[model+'_enabled']['endpoint'][k]-arms[model+'_'+control]['endpoint'][k]
                            for k in arms[model+'_enabled']['endpoint']}
                           for control in ('blocked','aggregate')}
    blocked_error = max(abs(a['skill_positive']-b['skill_positive'])
                        for a,b in zip(arms['feedback_blocked']['curve'],arms['constant_blocked']['curve']))
    assert blocked_error < 2e-13
    assert abs(contrasts['constant']['enabled_minus_blocked']['skill_positive']) < 2e-13
    assert abs(contrasts['constant']['enabled_minus_aggregate']['skill_positive']) < 2e-13
    one_round = {}
    for execution in (False,True):
        for frame in (0,1,2):
            state=(2,1,1,0,0,0,frame,1)
            rates={name:dict(zip(base.REWARDS,transition(Arm(name,execution=execution,feedback=fb),state)[1]))['turnovers']
                   for name,fb in [('feedback',True),('constant',False)]}
            expected=(.08,.22,.15)[frame] if execution else .15
            assert abs(rates['feedback']-expected) < 1e-14 and abs(rates['constant']-.15) < 1e-14
            one_round[f'execution_{execution}_frame_{frame}']=rates
    out={'status':'synthetic identifiability comparison, not empirical validation',
         'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
         'protocol_sha256':hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
         'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'original_six_arm_max_reproduction_error':reproduction_error,
         'blocked_projection_audit':audits,'blocked_skill_curve_max_difference':blocked_error,
         'one_round_turnover':one_round,'contrasts':contrasts,'arms':arms}
    (ROOT/'analysis.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='arms'},indent=2))


if __name__=='__main__':
    main()
