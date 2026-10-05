"""Independent domain predictor: absolute FIFO departure-time recurrences, no target run calls."""
from itertools import product
import math

TIMES = (0,2,4,6,8)
BVALS = (0,1,3)
DVALS = (1,2,4)
LVALS = (2,4)

def predict_path(regime, backlog, bursts, duration, length, finance, authority,
                 mode='integrated', inject_time=None):
    # Jobs already queued reserve their worker's future departure times immediately.
    # A newly arriving job is appended to that absolute-time reservation calendar.
    tail_app = 0
    tail_maintenance = 0
    diag_finish = None
    deploy_finish = None
    proposal = None
    diag_submitted = False
    deployed = False
    horizon = 5 if mode == 'diag' else regime['horizon']
    for t in range(horizon + 1):
        if diag_finish == t and t <= 5:
            proposal = 5 if regime['batch'] else t
        arrivals = (backlog if t == 0 else 0) + (2 if t in TIMES and bursts[TIMES.index(t)] else 0)
        tail_app = max(t, tail_app) + arrivals
        if mode != 'enact' and not diag_submitted and t >= (0 if finance else 3):
            diag_submitted = True
            if regime['reserved']:
                diag_finish = max(t, tail_maintenance) + duration
                tail_maintenance = diag_finish
            else:
                diag_finish = max(t, tail_app) + duration
                tail_app = diag_finish
        if mode == 'enact' and t == inject_time:
            proposal = t
        if mode != 'diag' and proposal is not None and t >= proposal and t >= (0 if authority else regime['opening0']) and not deployed:
            deployed = True
            if regime['reserved']:
                deploy_finish = max(t, tail_maintenance) + length
                tail_maintenance = deploy_finish
            else:
                deploy_finish = max(t, tail_app) + length
                tail_app = deploy_finish
    return dict(gate=diag_finish is not None and diag_finish <= 5,
                proposal_time=(5 if regime['batch'] else diag_finish) if diag_finish is not None and diag_finish <= 5 else None,
                diag_finish=diag_finish,
                recovered=deploy_finish is not None and deploy_finish <= regime['horizon'],
                recovery_time=deploy_finish if deploy_finish is not None and deploy_finish <= regime['horizon'] else None)

def primitive_cases(params):
    for ib, backlog in enumerate(BVALS):
        for bursts in product((False,True), repeat=5):
            k = sum(bursts)
            weight = params['backlog'][ib] * params['arrival']**k * (1-params['arrival'])**(5-k)
            for id, duration in enumerate(DVALS):
                for il, length in enumerate(LVALS):
                    yield backlog, bursts, duration, length, weight*params['diag'][id]*params['deploy'][il]

def integrated_rates(regime, params):
    result = [0.,0.,0.,0.]
    for backlog, bursts, duration, length, weight in primitive_cases(params):
        for f in (0,1):
            for a in (0,1):
                if predict_path(regime, backlog, bursts, duration, length, f, a)['recovered']:
                    result[2*f+a] += weight
    return [x*params['correct']*params['effective'] for x in result]

def oracle_local(regime, params):
    histograms = [{},{}]
    p = [0.,0.]
    for backlog, bursts, duration, length, weight in primitive_cases(params):
        for f in (0,1):
            path = predict_path(regime, backlog, bursts, duration, length, f, 0, mode='diag')
            if path['gate']:
                probability = weight * params['correct']
                p[f] += probability
                t = path['proposal_time']
                histograms[f][t] = histograms[f].get(t,0.) + probability
    timing = {}
    for f in (0,1):
        for t,w in histograms[f].items(): timing[t] = timing.get(t,0.) + .5*w/p[f]
    q = [0.,0.]
    for backlog,bursts,duration,length,weight in primitive_cases(params):
        for t,pt in timing.items():
            for a in (0,1):
                path = predict_path(regime,backlog,bursts,duration,length,0,a,mode='enact',inject_time=t)
                if path['recovered']: q[a] += weight*pt*params['effective']
    return dict(p=p,q=q,timing=timing,predictions=[p[f]*q[a] for f in (0,1) for a in (0,1)])

TRUE_PARAMS = dict(backlog=[.25,.50,.25], diag=[.25,.50,.25], deploy=[.5,.5], correct=.85, effective=.95)
