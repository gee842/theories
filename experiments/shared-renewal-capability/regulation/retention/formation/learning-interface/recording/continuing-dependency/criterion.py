"""Declared material-backed acquisition of a completion criterion.

Native plant events use the unchanged FormedSelection implementation. Added
contacts derive receipt payloads from actual admitted native effects. The native
law, finite consumption family, task scope, recipes and schedule remain supplied.
"""
from dataclasses import dataclass, asdict, replace
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_criterion_existing', HERE/'study.py')
prior = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = prior
spec.loader.exec_module(prior)
native = prior.native
MATERIAL = 78
MODULES = 9
CHANNELS = (1, 2, 4)  # common, local, source


@dataclass(frozen=True)
class Config:
    receipt_mode: int = 0  # faithful0, missing1, wrong-source2
    clamp: bool = False
    later_repair: bool = True
    force_bulk: bool = False


@dataclass(frozen=True)
class State:
    plant: tuple
    parts: int = 0
    target_a: int = 0
    episode: int = 0
    historical: int = 0  # bit1 first count completed, bit2 second count completed
    closed: bool = False
    finished: bool = False
    blocked_seen: bool = False
    restored_seen: bool = False
    phase: int = 0  # unbound0, armed1, emitted2, observed3, committed4, compiled5
    pending: int = 0  # mask from native effect; zero means no receipt
    observed: int = 0
    candidates: int = 7
    criterion_active: bool = False
    selected: int = 0  # none0, bulk1, local2
    common_spent: int = 0
    total_spent: int = 0


def support(p):
    return p[5], p[4], p[6]


def count_a(p):
    return p[0] + (p[2] == 1)


def population(p):
    return p[0]+p[1]+int(p[2] != 0)


def energy(p):
    return p[5]+p[4]+p[6]


def vector(s):
    """Stable full finite state projection; no hidden runtime receipt omitted."""
    return list(s.plant)+[s.parts,s.target_a,s.episode,s.historical,int(s.closed),
        int(s.finished),int(s.blocked_seen),int(s.restored_seen),s.phase,s.pending,
        s.observed,s.candidates,int(s.criterion_active),s.selected,s.common_spent,s.total_spent]


VECTOR_COLUMNS = ['freeA','freeH','resident','intact','local','common','source',
    'parts','targetA','episode','historical','closed','finished','blockedSeen','restoredSeen',
    'phase','pending','observed','candidates','criterionActive','selected','commonSpent','totalSpent']


def native_options(s):
    return {e: tuple(t) for e,t,rate in native.channels(
        native.Law(material=MATERIAL-2*s.parts),s.plant)}


def valid(s):
    return (0 <= s.parts <= MODULES and population(s.plant)+2*s.parts <= MATERIAL
        and all(x>=0 for x in s.plant) and s.plant[2] in (0,1,2)
        and s.plant[3] in (0,1) and s.plant[4] in (0,1))


def emitted_channel(before, after):
    result=0
    for i,c in enumerate(CHANNELS):
        if before[i] == after[i]+1 and all(before[j] == after[j] for j in range(3) if j!=i):
            result |= c
    return result


def charge(s):
    assert s.plant[5]>0
    p=list(s.plant);p[5]-=1
    return replace(s,plant=tuple(p),common_spent=s.common_spent+1,total_spent=s.total_spent+1)


def native_step(s, event):
    options=native_options(s)
    assert event in options,(event,vector(s))
    p=options[event]
    t=replace(s,plant=p,common_spent=s.common_spent+s.plant[5]-p[5],
        total_spent=s.total_spent+energy(s.plant)-energy(p))
    if s.phase==1:
        if event=='repair':
            t=replace(t,phase=2,pending=emitted_channel(support(s.plant),support(p)))
        else:
            # Bound contact cannot be replayed across an intervening native event.
            t=replace(t,phase=0,pending=0)
    return t


def operative(s, cfg):
    return s.criterion_active and not cfg.clamp


def channel_met(s, cfg, p=None):
    p=s.plant if p is None else p
    if not operative(s,cfg):
        return True
    return any(s.candidates==c and support(p)[i]>=1 for i,c in enumerate(CHANNELS))


def complete(s,cfg):
    # Closure enables a real one-common-unit handoff; preserve its support too.
    if s.plant[5]<1:return False
    p=list(s.plant);p[5]-=1
    return count_a(s.plant)>=s.target_a and channel_met(s,cfg,tuple(p))


def simulate_plan(s, plan):
    t=s
    for e in plan:
        if e not in native_options(t):
            return None
        t=native_step(t,e)
    return t


def candidate_plans(s,cfg):
    out=[]
    for code,word in ((1,('bulk_a',)),(2,('capture','copy_a'))):
        t=simulate_plan(s,word)
        # The forthcoming judgment has an actual cost, deducted before its criterion.
        if t is None or t.plant[5]<1:
            continue
        judged=charge(t)
        out.append((code,word,complete(judged,cfg)))
    return out


def enabled(s,cfg,event):
    if not valid(s):return False
    if event.startswith('native:'):
        return event[7:] in native_options(s)
    if event=='finish':return s.closed and not s.finished and s.plant[5]>0
    if s.plant[5]<1:return False
    if event=='assemble':return s.parts<MODULES and s.plant[0]>0 and s.plant[1]>0 and s.episode==0
    if s.parts!=MODULES:return False
    if event=='admit':return s.episode==0
    if event=='openEpisode':return s.episode==1 and s.phase==5 and not s.finished
    if event=='judge':return s.episode==1 and not s.finished
    if event=='probeCapture':return s.episode==1 and not s.finished
    if event=='armRepair':return s.blocked_seen and s.phase==0 and not s.finished
    if event=='observe':return s.phase==2
    if event=='commit':return s.phase==3
    if event=='compileCriterion':return s.phase==4 and s.restored_seen
    if event=='select':return s.episode==2 and not s.closed and not s.finished
    if event=='judgeAfter':return s.episode==2 and not s.finished
    return False


def advance(s,cfg,event):
    assert enabled(s,cfg,event),(event,vector(s))
    if event.startswith('native:'):
        t=native_step(s,event[7:])
    elif event=='finish':
        t=replace(charge(s),finished=True)
    else:
        t=charge(s)
        if event=='assemble':
            p=list(t.plant);p[0]-=1;p[1]-=1
            t=replace(t,plant=tuple(p),parts=t.parts+1)
        elif event=='admit':
            t=replace(t,target_a=count_a(t.plant),episode=1,closed=False)
        elif event=='openEpisode':
            t=replace(t,episode=2,closed=False,selected=0)
        elif event in ('judge','judgeAfter'):
            hist=t.historical | (1 if t.episode==1 else 2) if count_a(t.plant)>=t.target_a else t.historical
            t=replace(t,historical=hist,closed=complete(t,cfg))
        elif event=='probeCapture':
            if 'capture' in native_options(t):
                t=native_step(t,'capture')
                t=replace(t,restored_seen=t.restored_seen or t.blocked_seen)
            else:
                t=replace(t,blocked_seen=True,closed=False)
        elif event=='armRepair':
            t=replace(t,phase=1,pending=0)
        elif event=='observe':
            mask=t.pending if cfg.receipt_mode==0 else (0 if cfg.receipt_mode==1 else 4)
            t=replace(t,phase=3,observed=mask)
        elif event=='commit':
            cs=t.candidates & t.observed if t.observed else t.candidates
            t=replace(t,phase=4,candidates=cs)
        elif event=='compileCriterion':
            active=cfg.later_repair and t.blocked_seen and t.restored_seen and t.candidates in CHANNELS
            t=replace(t,phase=5,criterion_active=active)
        elif event=='select':
            plans=candidate_plans(t,cfg)
            selected=next((code for code,word,ok in plans if (cfg.force_bulk and code==1) or (not cfg.force_bulk and ok)),0)
            t=replace(t,selected=selected)
    assert valid(t)
    assert energy(t.plant)+t.total_spent==energy(s.plant)+s.total_spent
    assert t.plant[5]+t.common_spent==s.plant[5]+s.common_spent
    assert t.parts>=s.parts
    return t


class History:
    def __init__(self,cfg,initial):
        self.cfg=cfg;self.initial=initial;self.state=initial;self.steps=[];self.denied=[];self.milestones={}
    def do(self,event):
        old=self.state;self.state=advance(old,self.cfg,event)
        self.steps.append(dict(event=event,before=vector(old),after=vector(self.state)))
        return self.state
    def words(self,events):
        for e in events:self.do(e)
    def mark(self,name):self.milestones[name]=vector(self.state)
    def maybe(self,event):
        if enabled(self.state,self.cfg,event):self.do(event);return True
        self.denied.append(dict(event=event,state=vector(self.state)));return False


TRAINING = ['assemble']*MODULES+['native:leak_local','admit','native:wear_a','native:bulk_a',
    'judge','native:damage','probeCapture','armRepair','native:repair','observe','commit',
    'probeCapture','compileCriterion']


def run_case(name,cfg,ancestor,*,exhaust_source=False):
    h=History(cfg,State(tuple(ancestor)))
    for event in TRAINING:
        h.do(event)
        if event=='judge':h.mark('first_count_complete')
        if event=='native:repair':h.mark('actual_repair_receipt')
        if event=='commit':h.mark('acquired_record')
    h.mark('trained')
    assert h.state.plant==(29,30,1,1,1,274,215)
    if exhaust_source:
        h.do('native:leak_local')
        for _ in range(215):h.words(['native:capture','native:leak_local'])
    else:h.do('native:leak_local')
    h.words(['native:leak_common']*269)
    h.do('native:wear_a')
    h.do('openEpisode')
    h.mark('decision_before_read')
    assert h.state.plant[5]==4
    h.do('select');h.mark('selected')
    if h.state.selected==1:h.do('native:bulk_a')
    elif h.state.selected==2:h.words(['native:capture','native:copy_a'])
    h.mark('reconstruction')
    h.do('judgeAfter');h.mark('judged')
    finished=h.maybe('finish');h.mark('returned_or_open')
    h.do('native:damage');h.mark('later_damage')
    repaired=h.maybe('native:repair');h.mark('final')
    # This is an external endpoint audit, not a further runtime observation.
    result=dict(name=name,config=asdict(cfg),initial=vector(h.initial),events=[s['event'] for s in h.steps],
        steps=h.steps,denied=h.denied,milestones=h.milestones,final=vector(h.state),
        count_completed=bool(h.state.historical&2),criterion_active=h.state.criterion_active,
        selected=h.milestones['selected'][20],returned=finished,later_repair=repaired,
        source_exhaustion_history=exhaust_source)
    return result


def ancestry():
    saved=json.loads((HERE/'results.json').read_text())['histories']['ancestor']
    p=tuple(saved['initial']);rows=[]
    for e in saved['word']:
        options={event:tuple(t) for event,t,rate in native.channels(native.Law(material=78),p)}
        t=options[e];rows.append(dict(event=e,before=list(p),after=list(t)));p=t
    assert p==(38,39,1,1,1,293,216)
    return dict(initial=saved['initial'],events=saved['word'],steps=rows,final=list(p))


def main():
    parent=ancestry()
    cases=[run_case(name,cfg,parent['final'],exhaust_source=empty) for name,cfg,empty in [
        ('faithful',Config(),False),('clamped',Config(clamp=True),False),
        ('missing',Config(receipt_mode=1),False),('wrong_source',Config(receipt_mode=2),False),
        ('count_only_scope',Config(later_repair=False),False),
        ('source_exhausted',Config(),True),('forced_bulk_faithful_judge',Config(force_bulk=True),False)]]
    by={x['name']:x for x in cases}
    assert by['faithful']['later_repair'] and by['faithful']['selected']==2 and by['faithful']['returned']
    for name in ('clamped','missing','wrong_source','count_only_scope'):
        assert by[name]['selected']==1 and by[name]['count_completed'] and by[name]['returned'] and not by[name]['later_repair']
    assert by['forced_bulk_faithful_judge']['selected']==1 and by['forced_bulk_faithful_judge']['count_completed']
    assert not by['forced_bulk_faithful_judge']['returned'] and by['forced_bulk_faithful_judge']['later_repair']
    assert by['source_exhausted']['selected']==0 and not by['source_exhausted']['count_completed'] and not by['source_exhausted']['returned']
    assert by['faithful']['milestones']['decision_before_read']==by['clamped']['milestones']['decision_before_read']
    assert by['clamped']['milestones']['reconstruction']==by['forced_bulk_faithful_judge']['milestones']['reconstruction']
    training=by['faithful']['milestones']['actual_repair_receipt']
    bulk=by['clamped']['milestones']['later_damage']
    counter=dict(scope='Separate outside-family law diagnostic, not an original native history',
        description='Original repair if common>0; otherwise source-funded repair if source>0.',
        original_training_channel=1,alternative_training_channel=1,
        common_at_bulk_endpoint=bulk[5],source_at_bulk_endpoint=bulk[6],
        original_later_repair=False,alternative_later_repair=(bulk[5]>0 or bulk[6]>0))
    paths=[Path(__file__),HERE/'CRITERION-PROTOCOL.md',HERE/'study.py',HERE/'results.json',prior.FORMATION/'process.py',
        prior.FORMATION/'formal/FormedSelection.lean',Path(native.arithmetic.__file__)]+prior.preparation_sources()
    out=dict(status='passed',scope='Conditional acquired completion criterion under supplied maintenance scope and contact family',
        vector_columns=VECTOR_COLUMNS,ancestry=parent,cases=cases,hidden_fallback_countermodel=counter,
        source_hashes={str(p.relative_to(prior.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (HERE/'criterion-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='passed',ancestral_events=len(parent['events']),
        cases=[dict(name=x['name'],selected=x['selected'],count_completed=x['count_completed'],
                    returned=x['returned'],later_repair=x['later_repair'],events=len(x['events'])) for x in cases]),indent=2))


if __name__=='__main__':main()
