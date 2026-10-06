"""Exact finite prediction/action law with an actual paid preparation producer."""
from collections import defaultdict
from dataclasses import dataclass, replace, asdict
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import sys

PARENT = Path(__file__).resolve().parents[1] / 'model.py'
spec = importlib.util.spec_from_file_location('_prediction_updater_parent', PARENT)
upstream = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = upstream
spec.loader.exec_module(upstream)

ARMS = ('variable', 'conventional', 'fixed_fast', 'fixed_slow', 'direct_record',
        'frozen_register', 'inverted_record', 'inverted_action')
MOMENTS = ('gate_forms', 'base_forms', 'retrofits', 'rents', 'trials', 'captures',
           'writes', 'updater_changes', 'post_captures', 'brier16',
           'decoder_errors', 'spent', 'waste', 'unpaid_writes',
           'slow_writes', 'fast_writes', 'acquired_uses')
ZERO = (Q(0),)*len(MOMENTS)


@dataclass(frozen=True)
class Law:
    initial_common: int = 24
    adapter: int = 1
    gate_assembly: int = 2
    base: int = 1
    retrofit: int = 3
    rent: int = 1
    trial: int = 3
    write: int = 1
    renewal: int = 1
    gate_renewal: int = 1
    packet: int = 10
    lifetime: int = 6
    gate_lifetime: int = 2
    horizon: int = 12
    reversals: tuple = (6,)
    availability: Q = Q(1)

    def __post_init__(self):
        assert self.initial_common >= 0
        assert min(self.adapter, self.gate_assembly, self.base, self.retrofit,
                   self.rent, self.trial, self.write, self.renewal,
                   self.gate_renewal, self.lifetime, self.gate_lifetime) > 0
        assert self.packet >= self.renewal+self.gate_renewal
        assert 0 <= self.availability <= 1
        assert self.horizon >= 0
        assert tuple(sorted(set(self.reversals))) == self.reversals
        assert all(0 <= t <= self.horizon for t in self.reversals)

    @property
    def initial_source(self):
        return 1+self.horizon*self.packet

    def record(self):
        d=asdict(self)
        d['availability']=str(self.availability)
        d['initial_source']=self.initial_source
        return d


def prepare(law):
    """Reuse the exact earlier assembly-free entrance and every failed history."""
    oldlaw = upstream.Law(initial_common=law.initial_common, adapter=law.adapter,
                          packet=law.packet, horizon=law.horizon)
    return upstream.prepare(oldlaw)


@dataclass(frozen=True)
class State:
    fuel: int
    gate: int = -1                 # 0 Slow (retrofitted R); 1 Fast (retrofitted D)
    gate_life: int = 0
    stage: int = 0                 # 0 absent, 1 paid legacy prototype, 2 predictor
    life: int = 0
    q: int = 2
    last: int = 0
    written: bool = False
    prelearn: bool = False
    stale: int = -1
    corrected: bool = False
    witness: bool = False          # historical completion, never erased


def choices(arm):
    if arm in ('fixed_fast', 'direct_record'):
        return ((1,Q(1)),)
    if arm == 'fixed_slow':
        return ((0,Q(1)),)
    if arm == 'conventional':
        return tuple((k,Q(1,2)) for k in range(2))
    return ((0,Q(1,2)),(1,Q(1,2)))


def command(q, last):
    return int(q>2) if q != 2 else last


def conventional_command(q, last):
    return (0,0,last,1,1)[q]


def issued(arm,q,last):
    action=conventional_command(q,last) if arm=='conventional' else command(q,last)
    return 1-action if arm=='inverted_action' else action


def learned(gate,q,label):
    return 4*label if gate else min(4,q+1) if label else max(0,q-1)


def conventional_learned(gate,q,label):
    if gate == 1:
        return (0,4)[label]
    return ((0,0,1,2,3),(1,2,3,4,4))[label][q]


def delta(**kw):
    return tuple(kw.get(k,0) for k in MOMENTS)


def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))


def advance(law, state, arm, regime, after):
    """Controller inputs: hardware, q, last and acquired receipt; no regime/clock."""
    assert arm in ARMS
    branches=[(state,Q(1),delta())]
    gate=[]
    for s,p,m in branches:
        if s.gate_life:
            gate.append((s,p,m))
        elif s.fuel < law.gate_assembly:
            gate.append((s,p,m))
        else:
            for kind,prob in choices(arm):
                t=replace(s,fuel=s.fuel-law.gate_assembly,gate=kind,
                          gate_life=law.gate_lifetime)
                inc=delta(gate_forms=1,spent=law.gate_assembly,
                          updater_changes=int(s.gate>=0 and s.gate!=kind))
                gate.append((t,p*prob,plus(m,inc)))
    base=[]
    for s,p,m in gate:
        if not s.gate_life or s.life or s.stage==1 or s.fuel < law.base:
            base.append((s,p,m));continue
        for prior in (0,1):
            t=replace(s,fuel=s.fuel-law.base,stage=1,life=0,q=2,last=prior,
                      written=False,prelearn=False,stale=-1,corrected=False)
            base.append((t,p/2,plus(m,delta(base_forms=1,spent=law.base))))
    assembled=[]
    retrofit_cost=1 if arm=='direct_record' else law.retrofit
    for s,p,m in base:
        if s.gate_life and s.stage==1 and s.fuel>=retrofit_cost:
            s=replace(s,fuel=s.fuel-retrofit_cost,stage=2,life=law.lifetime,q=2)
            m=plus(m,delta(retrofits=1,spent=retrofit_cost))
        assembled.append((s,p,m))
    out=[]
    for s,p,m in assembled:
        if not s.life or s.stage!=2:
            out.append((s,p,m));continue
        if s.fuel < law.rent:
            t=replace(s,stage=0,life=0,q=2,last=0,written=False,
                      prelearn=False,stale=-1,corrected=False)
            out.append((t,p,m));continue
        s=replace(s,fuel=s.fuel-law.rent)
        m=plus(m,delta(rents=1,spent=law.rent))
        if not s.gate_life or s.fuel < law.trial:
            out.append((s,p,m));continue
        a=issued(arm,s.q,s.last)
        forecast_numerator=s.q if a else 4-s.q
        success=law.availability if a==regime else Q(0)
        for capture,prob in ((False,1-success),(True,success)):
            if not prob:continue
            receipt_label=a if capture else 1-a
            fuel=s.fuel-law.trial+(law.packet-law.renewal-law.gate_renewal if capture else 0)
            has_write=fuel>=law.write
            q=s.q
            if has_write and arm!='frozen_register':
                label=1-receipt_label if arm=='inverted_record' else receipt_label
                q=(conventional_learned(s.gate,q,label) if arm=='conventional'
                   else learned(s.gate,q,label))
            prelearn=s.prelearn or bool(not after and capture and s.written and s.q!=2)
            stale=s.stale
            if after and not capture and s.prelearn and stale==-1:
                stale=a
            corrected=s.corrected or bool(after and has_write and q!=s.q and stale>=0
                                             and issued(arm,s.q,a)==stale
                                             and issued(arm,q,a)!=stale)
            # This trial precedes the current write; only prior correction can govern it.
            witness=s.witness or bool(after and capture and s.corrected
                                      and s.stale>=0 and a!=s.stale)
            t=replace(s,fuel=fuel-law.write*int(has_write),q=q,last=a,
                      gate_life=law.gate_lifetime if capture else s.gate_life-1,
                      life=law.lifetime if capture else s.life-1,
                      written=s.written or has_write,prelearn=prelearn,stale=stale,
                      corrected=corrected,witness=witness)
            inc=delta(trials=1,captures=int(capture),writes=int(has_write),
                      post_captures=int(after and capture),
                      brier16=(forecast_numerator-4*int(capture))**2,
                      decoder_errors=int(receipt_label!=regime),
                      spent=law.trial+(law.renewal+law.gate_renewal)*int(capture)
                                     +law.write*int(has_write),
                      unpaid_writes=int(not has_write),
                      slow_writes=int(has_write and s.gate==0),
                      fast_writes=int(has_write and s.gate==1),
                      acquired_uses=int(s.written and s.q!=2))
            out.append((t,p*prob,plus(m,inc)))
    complete=[]
    for s,p,m in out:
        captures=m[MOMENTS.index('captures')]
        m=plus(m,delta(waste=law.packet*(1-captures)))
        assert s.fuel+m[MOMENTS.index('spent')]+m[MOMENTS.index('waste')]==state.fuel+law.packet
        assert 0<=s.q<=4 and 0<=s.life<=law.lifetime and 0<=s.gate_life<=law.gate_lifetime
        assert s.last in (0,1) and s.fuel>=0
        complete.append((s,p,m))
    assert sum(p for _,p,_ in complete)==1
    return tuple(complete)


def evolve(law,arm,reserve):
    table={(z,State(reserve)):(Q(1,2),ZERO) for z in (0,1)}
    sizes=[len(table)]
    boundary=law.reversals[0] if law.reversals else law.horizon
    for t in range(law.horizon):
        nxt={}
        parity=sum(v<=t for v in law.reversals)%2
        for (z,s),(mass,moments) in table.items():
            for out,p,inc in advance(law,s,arm,z^parity,t>=boundary):
                key=(z,out)
                oldmass,oldmom=nxt.get(key,(Q(0),ZERO))
                nxt[key]=(oldmass+mass*p,tuple(a+p*(b+mass*c)
                                  for a,b,c in zip(oldmom,moments,inc)))
        table=nxt
        assert sum(p for p,_ in table.values())==1
        sizes.append(len(table))
    return table,sizes


def summaries(law,table,reserve):
    totals=tuple(sum((m[i] for _,m in table.values()),Q(0)) for i in range(len(MOMENTS)))
    d=dict(zip(MOMENTS,totals))
    def mean(fn):
        return sum((p*fn(s) for (_,s),(p,_) in table.items()),Q(0))
    d.update(reserve=mean(lambda s:s.fuel),p_correction=mean(lambda s:int(s.witness)),
             p_active_memory=mean(lambda s:int(s.stage==2 and s.life>0)),
             p_written_active_memory=mean(lambda s:int(s.stage==2 and s.life>0 and s.written)),
             final_q=mean(lambda s:s.q))
    d['brier_loss']=d.pop('brier16')/16
    assert d['reserve']+d['spent']+d['waste']==reserve+law.horizon*law.packet
    return d


def compare(law):
    preparations,visited=prepare(law)
    entrance=sum((Q(p['probability']) for p in preparations if p['commissioned']),Q(0))
    prep_cost=sum((Q(p['probability'])*p['preparation_spent'] for p in preparations),Q(0))
    retained_fail=sum((Q(p['probability'])*p['remaining_energy'] for p in preparations if not p['commissioned']),Q(0))
    cache={}
    rows={}
    for arm in ARMS:
        totals=defaultdict(Q)
        maxstates=0
        for p in preparations:
            if not p['commissioned']:continue
            key=(arm,p['reserve'])
            if key not in cache:
                table,sizes=evolve(law,arm,p['reserve'])
                cache[key]=(table,summaries(law,table,p['reserve']),sizes)
            table,values,sizes=cache[key]
            maxstates=max(maxstates,max(sizes))
            weight=Q(p['probability'])
            for metric,value in values.items():totals[metric]+=weight*value
            totals['source_remainder']+=weight*(p['remainder']+(p['packets']-law.horizon)*law.packet)
        totals['p_commissioned']=entrance
        totals['preparation_spent']=prep_cost
        totals['adapter_spent']=entrance*law.adapter
        totals['uncommissioned_energy']=retained_fail
        # Include typed predecessor failures, not zeroing their still-existing fuel.
        total=(totals['reserve']+totals['source_remainder']+retained_fail+
               totals['spent']+totals['waste']+prep_cost+entrance*law.adapter)
        assert total==law.initial_common+law.initial_source
        rows[arm]={'metrics':{k:str(v) for k,v in sorted(totals.items())},
                   'trial_weighted_brier':str(totals['brier_loss']/totals['trials']) if totals['trials'] else None,
                   'trial_coverage':str(totals['trials']/law.horizon) if law.horizon else None,
                   'maximum_distribution_states':maxstates}
    for p in preparations:
        if p['commissioned']:
            assert cache['variable',p['reserve']][0]==cache['conventional',p['reserve']][0]
    return {'law':law.record(),'preparations':preparations,'preparation_states':visited,
            'arms':rows,'exact_conventional_distribution':True}


def cases():
    base=Law()
    return {'primary':base,'no_change':replace(base,reversals=()),
            'two_changes':replace(base,reversals=(4,8)),
            'outages':replace(base,availability=Q(3,4)),
            'low_reserve':replace(base,initial_common=12),
            'high_write_cost':replace(base,write=2),
            'short_circuit':replace(base,lifetime=2),
            'low_yield':replace(base,packet=6)}
