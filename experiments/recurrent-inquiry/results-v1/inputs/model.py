"""Exact finite-horizon inquiry allocation and one-step evidence transmission."""
from dataclasses import dataclass, asdict, replace
from functools import lru_cache
from itertools import product
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


@dataclass(frozen=True)
class Parameters:
    h: float = .1
    loss: float = 1.
    treatment: float = .4
    diagnostic: float = .08
    success: float = .8
    upkeep: float = .025
    rebuild: float = .3
    cap: float = .65


UNKNOWN = (-1, 0)


def probability(belief, h):
    state, age = belief
    return .5 if state == -1 else .5 + (state - .5) * (1 - 2*h)**age


def advance(belief):
    return UNKNOWN if belief[0] == -1 else (belief[0], belief[1]+1)


def observations(belief, test, params):
    if not test:
        return [(1., belief)]
    p = probability(belief, params.h)
    return [(w, b) for w,b in [(params.success*(1-p),(0,0)),
                               (params.success*p,(1,0)),
                               (1-params.success,belief)] if w > 0]


def operating(belief, params):
    p = probability(belief, params.h)
    # Tie break toward no treatment; no future information comes from this action.
    action = int(params.treatment < params.loss*p)
    return action, params.treatment*action + params.loss*p*(1-action)


class Planner:
    def __init__(self, params, calendar=None, inquiry_price=1.):
        self.p = params
        self.calendar = calendar
        self.price = inquiry_price
        self.choices = {}

    @lru_cache(None)
    def solve(self, n, belief, ready):
        if n == 0:
            return 0.
        p = self.p
        best = None
        for test in range(ready+1):
            fee = test*p.diagnostic
            if fee > p.cap+1e-12:
                continue
            total = self.price*fee
            following = {}
            for weight, post in observations(belief,test,p):
                _, op = operating(post,p)
                options = (0,) if n == 1 else (0,1)
                if self.calendar is not None:
                    options = (self.calendar[-n],)
                branches = []
                for nxt in options:
                    upkeep = nxt*(p.upkeep if ready else p.rebuild)
                    if fee+upkeep <= p.cap+1e-12:
                        branches.append((self.price*upkeep+
                                         self.solve(n-1,advance(post),nxt), nxt))
                if not branches:
                    total = float('inf')
                    break
                value,nxt = min(branches)
                following[post] = nxt
                total += weight*(op+value)
            choice = (total,test,following)
            if best is None or total < best[0]-1e-12:
                best = choice
        if best is None or not np.isfinite(best[0]):
            return float('inf')
        self.choices[(n,belief,ready)] = best[1:]
        return best[0]

    def decide(self,n,belief,ready):
        self.solve(n,belief,ready)
        return self.choices[(n,belief,ready)]


def evaluate(planner, horizon, initial=UNKNOWN, ready=1, world=None):
    """Forward distribution propagation; can evaluate a misspecified planner."""
    world = world or planner.p
    distribution = {(initial,ready):1.}
    totals = dict(untreated_loss=0.,treatment_cost=0.,diagnostic_cost=0.,
                  upkeep_cost=0.,rebuilding_cost=0.,tests=0.,
                  maintained_without_test=0.,ready_periods=0.)
    trace = []
    for t in range(horizon):
        nxtdist = {}
        n = horizon-t
        for (belief,available), mass in distribution.items():
            test,following = planner.decide(n,belief,available)
            totals['diagnostic_cost'] += mass*test*world.diagnostic
            totals['tests'] += mass*test
            totals['ready_periods'] += mass*available
            for weight,post in observations(belief,test,world):
                # The same support must exist in both the believed and true model.
                if post not in following:
                    # Resolve actions for off-believed-path observations explicitly.
                    proxy = replace(planner.p, success=world.success, h=world.h)
                    raise ValueError(f'unsupported observation {post}: {proxy}')
                nxt = following[post]
                action,_ = operating(post,planner.p)
                actualp = probability(post,world.h)
                w = mass*weight
                totals['untreated_loss'] += w*(1-action)*actualp*world.loss
                totals['treatment_cost'] += w*action*world.treatment
                fee = nxt*(world.upkeep if available else world.rebuild)
                totals['upkeep_cost' if available else 'rebuilding_cost'] += w*fee
                totals['maintained_without_test'] += w*(available and nxt and not test)
                assert test*world.diagnostic+fee <= world.cap+1e-9
                key = (advance(post),nxt)
                nxtdist[key] = nxtdist.get(key,0.)+w
                trace.append(dict(period=t,mass=w,belief=list(belief),
                                  probability=probability(belief,world.h),ready=available,
                                  test=test,post=list(post),treat=action,next_ready=nxt))
        assert abs(sum(nxtdist.values())-1) < 1e-10
        distribution = nxtdist
    totals['inquiry_cost'] = sum(totals[k] for k in ['diagnostic_cost','upkeep_cost','rebuilding_cost'])
    totals['operating_loss'] = totals['untreated_loss']+totals['treatment_cost']
    totals['total_loss'] = totals['operating_loss']+totals['inquiry_cost']
    return totals,trace


def calendars(horizon):
    return [tuple(bits)+(0,) for bits in product((0,1),repeat=horizon-1)]


def calendar_lp(params,horizon,budget=None,initial=UNKNOWN,ready=1,all_calendars=None):
    """Exact occupancy LP over ex ante calendars with adaptive randomized tests.

    One source variable per calendar chooses an ex ante lottery. Flow variables
    permit different test probabilities for each time/belief. The one expected
    inquiry budget is shared by the lottery. Capacity choices cannot depend on
    results. No Monte Carlo or sampled policy library is used.
    """
    schedules = all_calendars or calendars(horizon)
    entries=[]; op=[]; cost=[]; rows=[];cols=[];vals=[]; rhs=[]
    def var(entry,oper=0.,expense=0.):
        j=len(entries);entries.append(entry);op.append(oper);cost.append(expense);return j
    weights=[var(('calendar',i,cal)) for i,cal in enumerate(schedules)]
    rhs.append(1.)
    for j in weights: rows.append(0);cols.append(j);vals.append(1.)
    for idx,cal in enumerate(schedules):
        states=[{initial}]
        for t in range(horizon-1):
            available=ready if t==0 else cal[t-1]
            fee=cal[t]*(params.upkeep if available else params.rebuild)
            candidates=set()
            for belief in states[-1]:
                for test in range(available+1):
                    if fee+test*params.diagnostic<=params.cap+1e-12:
                        candidates.update(advance(post) for _,post in observations(belief,test,params))
            states.append(candidates)
        rowids={}
        for t,beliefs in enumerate(states):
            for belief in sorted(beliefs):
                rowids[(t,belief)] = len(rhs);rhs.append(0.)
        firstrow=rowids[(0,initial)]
        rows.append(firstrow);cols.append(weights[idx]);vals.append(-1.)
        for t,beliefs in enumerate(states):
            available=ready if t==0 else cal[t-1]
            fee=cal[t]*(params.upkeep if available else params.rebuild)
            for belief in sorted(beliefs):
                for test in range(available+1):
                    expense=fee+test*params.diagnostic
                    if expense>params.cap+1e-12:continue
                    obs=observations(belief,test,params)
                    oper=sum(w*operating(post,params)[1] for w,post in obs)
                    j=var((idx,t,belief,test),oper,expense)
                    rows.append(rowids[(t,belief)]);cols.append(j);vals.append(1.)
                    if t+1<horizon:
                        for w,post in obs:
                            rows.append(rowids[(t+1,advance(post))]);cols.append(j);vals.append(-w)
    A=coo_matrix((vals,(rows,cols)),shape=(len(rhs),len(entries))).tocsr()
    op=np.asarray(op); cost=np.asarray(cost)
    objective=op+cost if budget is None else op
    result=linprog(objective,A_eq=A,b_eq=rhs,
                   A_ub=None if budget is None else cost[None,:],
                   b_ub=None if budget is None else [budget],
                   bounds=(0,None),method='highs')
    if not result.success:raise RuntimeError(result.message)
    residual=float(np.max(np.abs(A@result.x-rhs)))
    actualcost=float(cost@result.x); actualloss=float(op@result.x)
    assert residual<1e-8
    assert budget is None or actualcost<=budget+1e-8
    mixture=[dict(calendar=list(schedules[i]),weight=float(result.x[j]))
             for i,j in enumerate(weights) if result.x[j]>1e-8]
    return dict(operating_loss=actualloss,inquiry_cost=actualcost,
                total_loss=actualloss+actualcost,budget=budget,
                flow_residual=residual,variables=len(entries),
                equality_constraints=len(rhs),mixture=mixture)


def handoff(prior=.5,cue_accuracy=.5,age=0,h=.1,loss=1.,treatment=.4,
            setup=.02,message=.1,delivery=1.):
    """Enumerate common disclosure rules; compute posterior including silence."""
    def risk(p):return min(treatment,loss*p)
    def aged(p):return .5+(p-.5)*(1-2*h)**age
    result=dict(total_loss=0.,operating_loss=0.,communication_cost=0.,
                sent_probability=0.,opened_probability=0.,contexts=[])
    for cue in (0,1):
        joint=np.array([(1-prior)*(cue_accuracy if cue==0 else 1-cue_accuracy),
                        prior*(cue_accuracy if cue==1 else 1-cue_accuracy)])
        mass=float(joint.sum())
        if not mass:continue
        q=float(joint[1]/mass)
        probs=[1-q,q]
        choices=[dict(rule='closed',operating_loss=risk(aged(q)),fee=0.,sent=0.,
                      opened=0,messages=[dict(symbol='none',probability=1.,posterior=q)])]
        for rule in product((0,1),repeat=2):
            groups={}
            for state in (0,1):
                for symbol,weight in ([(str(state),delivery),('silent',1-delivery)]
                                      if rule[state] else [('silent',1.)]):
                    groups.setdefault(symbol,np.zeros(2))[state]+=probs[state]*weight
            messages=[];oper=0.
            for symbol,weights in groups.items():
                w=float(weights.sum())
                if not w:continue
                post=float(weights[1]/w)
                oper+=w*risk(aged(post))
                messages.append(dict(symbol=symbol,probability=w,posterior=post))
            sent=sum(probs[state]*rule[state] for state in (0,1))
            choices.append(dict(rule=list(rule),operating_loss=oper,fee=setup+message*sent,
                                sent=sent,opened=1,messages=messages))
        chosen=min(choices,key=lambda x:(x['operating_loss']+x['fee'],x['fee']))
        result['operating_loss']+=mass*chosen['operating_loss']
        result['communication_cost']+=mass*chosen['fee']
        result['sent_probability']+=mass*chosen['sent']
        result['opened_probability']+=mass*chosen['opened']
        result['contexts'].append(dict(cue=cue,mass=mass,prior=q,chosen=chosen,alternatives=choices))
    result['total_loss']=result['operating_loss']+result['communication_cost']
    return result
