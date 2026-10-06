"""Acquired initiation conflict in a continuing material history.

Protection of a specified pending continuation is a declared local rule, not
an inferred universal priority. Existing products and ancestry remain real.
"""
from dataclasses import dataclass, asdict, replace
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('_initiation_scope',HERE/'scope.py')
S=importlib.util.module_from_spec(spec);sys.modules[spec.name]=S;spec.loader.exec_module(S)
C=S.C


@dataclass(frozen=True)
class Config:
    form_mode: int=0  # faithful0, missing1, false-source2
    finish_mode: int=0
    clamp: bool=False


@dataclass(frozen=True)
class State:
    parent: S.State
    parts: int=0
    trial_a: int=0
    new_b: int=0
    target_a: int=0
    phase: int=0  # unbound0, armed1, emitted2, observed3, committed4
    binding: int=0  # actual formTrialA1, actual finishOldB2
    pending: int=0
    observed: int=0
    form_family: int=7
    finish_family: int=7
    record_b: int=0
    selected: int=0
    pc: int=0
    common_spent: int=0
    total_spent: int=0


EXTRA=['initiationParts','trialA','newB','candidateA','contactPhase','binding','pendingCost',
    'observedCost','formFamily','finishFamily','newBRecord','initiationSelected','initiationPC',
    'initiationCommonSpent','initiationTotalSpent']
VECTOR_COLUMNS=S.VECTOR_COLUMNS+EXTRA
PLANS={0:(),1:('finishNewB',),2:('formTargetA','finishNewB'),3:('formTargetA',)}


def vector(s):
    return S.vector(s.parent)+[s.parts,s.trial_a,s.new_b,s.target_a,s.phase,s.binding,s.pending,
        s.observed,s.form_family,s.finish_family,s.record_b,s.selected,s.pc,s.common_spent,s.total_spent]
def plant(s):return s.parent.core.plant
def occupied(s):return S.occupied(s.parent)+2*(s.parts+S.held(s.trial_a)+S.held(s.new_b)+S.held(s.target_a))
def native_options(s):
    return {e:tuple(t) for e,t,rate in C.native.channels(C.native.Law(material=78-occupied(s)),plant(s))}
def valid(s):
    return (S.valid(s.parent) and 0<=s.parts<=3 and all(x in range(5) for x in (s.trial_a,s.new_b,s.target_a))
        and C.population(plant(s))+occupied(s)<=78 and s.phase in range(5) and s.binding in range(3)
        and all(x in range(8) for x in (s.pending,s.observed,s.form_family,s.finish_family)) and s.record_b in range(6))
def plant_update(s,p):
    p=tuple(p);old=plant(s)
    return replace(s,parent=replace(s.parent,core=replace(s.parent.core,plant=p)),
        common_spent=s.common_spent+old[5]-p[5],total_spent=s.total_spent+C.energy(old)-C.energy(p))
def charge(s):
    p=list(plant(s));assert p[5]>0;p[5]-=1;return plant_update(s,p)
def spend_channel(support,mask):
    if mask not in C.CHANNELS:return None
    index=C.CHANNELS.index(mask)
    if support[index]<1:return None
    out=list(support);out[index]-=1;return tuple(out)
def selection(s,cfg):
    if s.record_b!=3:return 3
    if cfg.clamp or s.form_family not in C.CHANNELS or s.finish_family not in C.CHANNELS:return 2
    support=C.support(plant(s));after_form=spend_channel(support,s.form_family)
    if after_form is not None and spend_channel(after_form,s.finish_family) is not None:return 2
    if spend_channel(support,s.finish_family) is not None:return 1
    return 0


def primitive_enabled(s,event):
    p=plant(s)
    if event.startswith('native:'):return event[7:] in native_options(s)
    if event=='assemble':return s.parts<3 and p[0]>0 and p[1]>0 and p[5]>0 and s.trial_a==0
    if s.parts!=3:return False
    if event in ('formTrialA','formNewB','formTargetA'):
        phase={'formTrialA':s.trial_a,'formNewB':s.new_b,'formTargetA':s.target_a}[event]
        return phase==0 and min(p[0],p[1],p[5])>0
    if event=='finishOldB':return s.parent.b==2 and p[5]>0
    if event in ('primeTrialA','finishTrialA','primeTargetA','finishTargetA'):
        phase=s.trial_a if 'Trial' in event else s.target_a
        return phase==(1 if event.startswith('prime') else 2) and p[4]==1
    if event in ('primeNewB','finishNewB'):return s.new_b==(1 if event=='primeNewB' else 2) and p[5]>0
    if event=='dissociateNewB':return s.new_b in (1,2) and p[5]>0
    if p[5]<1:return False
    if event=='armForm':return s.phase in (0,4) and s.trial_a==0
    if event=='armFinish':return s.phase in (0,4) and s.parent.b==2
    if event=='observe':return s.phase==2
    if event=='commit':return s.phase==3
    return event in ('contactNewB','select')

def enabled(s,cfg,event):
    if not valid(s):return False
    if event=='act':
        word=PLANS.get(s.selected,())
        return s.pc<len(word) and primitive_enabled(s,word[s.pc])
    return primitive_enabled(s,event)

def physical(event):
    return event.startswith('native:') or event in ('formTrialA','formNewB','formTargetA','finishOldB',
        'primeTrialA','finishTrialA','primeTargetA','finishTargetA','primeNewB','finishNewB','dissociateNewB')

def primitive_step(s,cfg,event):
    assert primitive_enabled(s,event),(event,vector(s))
    if event.startswith('native:'):t=plant_update(s,native_options(s)[event[7:]])
    elif event in ('primeTrialA','finishTrialA','primeTargetA','finishTargetA'):
        p=list(plant(s));p[3]=0;p[4]=0;t=plant_update(s,p)
        t=replace(t,**{('trial_a' if 'Trial' in event else 'target_a'):2 if event.startswith('prime') else 3})
    else:
        t=charge(s)
        if event in ('assemble','formTrialA','formNewB','formTargetA'):
            p=list(plant(t));p[0]-=1;p[1]-=1;t=plant_update(t,p)
            if event=='assemble':t=replace(t,parts=t.parts+1)
            else:t=replace(t,**{dict(formTrialA='trial_a',formNewB='new_b',formTargetA='target_a')[event]:1})
        elif event=='finishOldB':t=replace(t,parent=replace(t.parent,b=3))
        elif event in ('primeNewB','finishNewB'):t=replace(t,new_b=2 if event=='primeNewB' else 3)
        elif event=='dissociateNewB':
            p=list(plant(t));p[0]+=1;p[1]+=1;t=replace(plant_update(t,p),new_b=4)
        elif event in ('armForm','armFinish'):t=replace(t,phase=1,binding=1 if event=='armForm' else 2,pending=0,observed=0)
        elif event=='observe':
            mode=cfg.form_mode if t.binding==1 else cfg.finish_mode
            t=replace(t,phase=3,observed=t.pending if mode==0 else (0 if mode==1 else 4))
        elif event=='commit':
            key='form_family' if t.binding==1 else 'finish_family'
            family=getattr(t,key);t=replace(t,phase=4,**{key:family&t.observed if t.observed else family})
        elif event=='contactNewB':t=replace(t,record_b=t.new_b+1)
        elif event=='select':t=replace(t,selected=selection(t,cfg),pc=0)
    if s.phase==1 and physical(event):
        matching=event==('formTrialA' if s.binding==1 else 'finishOldB')
        t=replace(t,phase=2 if matching else 0,pending=C.emitted_channel(C.support(plant(s)),C.support(plant(t))) if matching else 0,
            binding=s.binding if matching else 0)
    return t

def advance(s,cfg,event):
    assert enabled(s,cfg,event),(event,vector(s))
    t=replace(primitive_step(s,cfg,PLANS[s.selected][s.pc]),pc=s.pc+1) if event=='act' else primitive_step(s,cfg,event)
    assert valid(t)
    assert C.energy(plant(t))+t.total_spent==C.energy(plant(s))+s.total_spent
    assert plant(t)[5]+t.common_spent==plant(s)[5]+s.common_spent
    assert plant(t)[5]<=plant(s)[5] and plant(t)[6]<=plant(s)[6]
    assert S.vector(t.parent)[7:25]==S.vector(s.parent)[7:25]
    assert S.vector(t.parent)[26:]==S.vector(s.parent)[26:]
    for before,after in ((s.trial_a,t.trial_a),(s.new_b,t.new_b),(s.target_a,t.target_a)):
        assert after>=before and (before!=3 or after==3)
    return t


class History:
    def __init__(self,cfg,initial):self.cfg=cfg;self.initial=initial;self.state=initial;self.steps=[];self.denied=[];self.milestones={}
    def do(self,event):
        before=self.state;effect=PLANS[before.selected][before.pc] if event=='act' else event
        self.state=advance(before,self.cfg,event)
        self.steps.append(dict(event=event,effect=effect,before=vector(before),after=vector(self.state)))
    def words(self,word):
        for event in word:self.do(event)
    def mark(self,key):self.milestones[key]=vector(self.state)
    def execute(self):
        while self.state.pc<len(PLANS[self.state.selected]):
            if not enabled(self.state,self.cfg,'act'):
                self.denied.append(dict(event='act',effect=PLANS[self.state.selected][self.state.pc],state=vector(self.state)));break
            self.do('act')


TRAINING=['assemble']*3+['armForm','formTrialA','observe','commit','armFinish','finishOldB','observe','commit',
    'native:repair','native:capture','primeTrialA','native:repair','native:capture','finishTrialA',
    'formNewB','primeNewB','contactNewB']
CASES=[('scarce_faithful',Config(),'scarce'),('scarce_clamped',Config(clamp=True),'scarce'),
    ('scarce_missing_form',Config(form_mode=1),'scarce'),('scarce_wrong_form',Config(form_mode=2),'scarce'),
    ('scarce_wrong_finish',Config(finish_mode=2),'scarce'),('ample_faithful',Config(),'ample'),
    ('ample_intervening_loss',Config(),'loss'),('B_completed',Config(),'complete'),('B_dissociated',Config(),'dissociate')]


def ancestry():
    saved=json.loads((HERE/'scope-results.json').read_text());row=next(c for c in saved['cases'] if c['name']=='completion_faithful')
    a,training,core=S.inherited_history()
    assert a==saved['ancestry'] and training==saved['criterion_training']
    s=S.State(core);steps=[]
    for index,event in enumerate(S.PREFIX+['native:repair','native:capture','finishA']):
        before=s;s=S.advance(s,S.Config(),event)
        step=dict(event=event,effect=event,before=S.vector(before),after=S.vector(s))
        assert step==row['steps'][index];steps.append(step)
    assert S.vector(s)==row['milestones']['actual_branch'] and plant(State(s))==(24,25,1,0,0,264,214)
    return dict(native=a,criterion_training=training,scope_prefix=dict(config=asdict(S.Config()),initial=row['initial'],
        events=[x['event'] for x in steps],steps=steps,final=S.vector(s))),s


def pending(s):
    return [name for name,phase in [('originalA',s.parent.a),('originalB',s.parent.b),('trialA',s.trial_a),
        ('newB',s.new_b),('targetA',s.target_a)] if phase in (1,2)]

def run_case(name,cfg,branch,parent):
    h=History(cfg,State(parent));h.words(TRAINING);h.mark('trained')
    assert plant(h.state)[5:]==(248,212)
    if branch in ('complete','dissociate'):
        h.do('finishNewB' if branch=='complete' else 'dissociateNewB');h.do('contactNewB')
    h.mark('scope_reached')
    leak_count=244 if branch in ('complete','dissociate') else (245 if branch in ('ample','loss') else 246)
    h.words(['native:leak_common']*leak_count);h.mark('decision');h.do('select');h.mark('selected')
    if branch=='loss':h.do('native:leak_common')
    h.mark('before_execution');h.execute();h.mark('final')
    s=h.state
    return dict(name=name,config=asdict(cfg),branch=branch,initial=vector(h.initial),steps=h.steps,
        events=[r['event'] for r in h.steps],denied=h.denied,milestones=h.milestones,final=vector(s),
        pending=pending(s),target_started=s.target_a>0,newB_product=s.new_b==3,newB_dissociated=s.new_b==4,
        retained_products=dict(originalA=s.parent.a==3,originalB=s.parent.b==3,trialA=s.trial_a==3),selected=s.selected)


def main():
    parent_history,parent=ancestry();cases=[run_case(n,c,b,parent) for n,c,b in CASES];by={c['name']:c for c in cases}
    assert by['scarce_faithful']['newB_product'] and not by['scarce_faithful']['target_started']
    for name in ('scarce_clamped','scarce_missing_form','scarce_wrong_form','scarce_wrong_finish','ample_intervening_loss'):
        assert by[name]['target_started'] and not by[name]['newB_product'] and len(by[name]['denied'])==1
    assert by['ample_faithful']['target_started'] and by['ample_faithful']['newB_product']
    assert by['B_completed']['target_started'] and by['B_completed']['newB_product']
    assert by['B_dissociated']['target_started'] and by['B_dissociated']['newB_dissociated']
    assert by['scarce_faithful']['milestones']['decision']==by['scarce_clamped']['milestones']['decision']
    saved=json.loads((HERE/'scope-results.json').read_text());paths=[C.prior.ROOT/p for p in saved['source_hashes']]
    paths += [HERE/'scope-results.json',Path(__file__),HERE/'INITIATION-PROTOCOL.md']
    out=dict(status='passed',scope='Acquired initiation conflict under a supplied bounded non-foreclosure rule',
        vector_columns=VECTOR_COLUMNS,ancestry=parent_history,cases=cases,
        source_hashes={str(p.relative_to(C.prior.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (HERE/'initiation-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='passed',ancestral_events=129,new_events=sum(len(c['events']) for c in cases),
        cases=[dict(name=c['name'],events=len(c['events']),selected=c['selected'],target_started=c['target_started'],
                    Bproduct=c['newB_product'],pending=c['pending']) for c in cases]),indent=2))


if __name__=='__main__':main()
