"""Material formation, contact and operative revision of activity scope.

The original plant and frozen criterion ancestor are preserved. Explicit added
reaction/contact laws create actual continuation relations, not ultimate value.
"""
from dataclasses import dataclass, asdict, replace
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('_scope_criterion',HERE/'criterion.py')
C=importlib.util.module_from_spec(spec);sys.modules[spec.name]=C;spec.loader.exec_module(C)


@dataclass(frozen=True)
class Config:
    contact_mode: int=0  # faithful0, missing1, stale2, false-absent3; refreshA only
    clamp: bool=False


@dataclass(frozen=True)
class State:
    core: C.State
    readers: int=0
    a: int=0  # absent0, formed1, primed2, product3, dissociated4
    b: int=0
    record_a: int=0  # phase+1, unknown0
    record_b: int=0
    snapshot_a: int=0
    snapshot_b: int=0
    last_target: int=0  # A1, B2
    last_payload: int=0
    selected: int=0
    pc: int=0
    common_spent: int=0
    total_spent: int=0


VECTOR_COLUMNS=C.VECTOR_COLUMNS+['scopeReaders','activityA','activityB','recordA','recordB',
    'snapshotA','snapshotB','lastTarget','lastPayload','scopeSelected','programCounter',
    'scopeCommonSpent','scopeTotalSpent']


def vector(s):
    return C.vector(s.core)+[s.readers,s.a,s.b,s.record_a,s.record_b,s.snapshot_a,s.snapshot_b,
        s.last_target,s.last_payload,s.selected,s.pc,s.common_spent,s.total_spent]


def held(phase):return int(phase in (1,2,3))
def occupied(s):return 2*(s.core.parts+s.readers+held(s.a)+held(s.b))
def native_options(s):
    return {e:tuple(t) for e,t,rate in C.native.channels(C.native.Law(material=78-occupied(s)),s.core.plant)}
def valid(s):
    return (C.valid(s.core) and 0<=s.readers<=3 and s.a in range(5) and s.b in range(5)
        and C.population(s.core.plant)+occupied(s)<=78
        and all(x in range(6) for x in (s.record_a,s.record_b,s.snapshot_a,s.snapshot_b)))
def plant_update(s,p):
    p=tuple(p)
    return replace(s,core=replace(s.core,plant=p),
        common_spent=s.common_spent+s.core.plant[5]-p[5],
        total_spent=s.total_spent+C.energy(s.core.plant)-C.energy(p))
def charge(s):
    p=list(s.core.plant);assert p[5]>0;p[5]-=1
    return plant_update(s,p)
def actual_pending(s):return [name for name,phase in [('A',s.a),('B',s.b)] if phase in (1,2)]
def acquired_pending(s,cfg):
    ra,rb=(s.snapshot_a,s.snapshot_b) if cfg.clamp else (s.record_a,s.record_b)
    return [name for name,record in [('A',ra),('B',rb)] if record in (2,3)]


PLANS={0:(),1:('native:repair','native:capture','finishA'),
       2:('native:capture','finishA'),3:('finishA',),4:('finishB',)}

def selection(s,cfg):
    ra,rb=(s.snapshot_a,s.snapshot_b) if cfg.clamp else (s.record_a,s.record_b)
    p=s.core.plant
    if ra==3 and s.core.candidates==1:
        if p[4]==1:return 3
        if p[6]>0:
            if p[3]==1:return 2
            if p[2]==1 and p[5]>0:return 1
    if rb==3 and p[5]>0:return 4
    return 0


def primitive_enabled(s,event):
    p=s.core.plant
    if event.startswith('native:'):return event[7:] in native_options(s)
    if event=='assemble':return s.readers<3 and p[0]>0 and p[1]>0 and p[5]>0 and s.a==0 and s.b==0
    if s.readers!=3:return False
    if event in ('formA','formB'):
        phase=s.a if event=='formA' else s.b
        return phase==0 and p[0]>0 and p[1]>0 and p[5]>0
    if event in ('primeA','finishA'):
        return s.a==(1 if event=='primeA' else 2) and p[4]==1
    if event in ('primeB','finishB'):
        return s.b==(1 if event=='primeB' else 2) and p[5]>0
    if event in ('dissociateA','dissociateB'):
        phase=s.a if event=='dissociateA' else s.b
        return phase in (1,2) and p[5]>0
    if event in ('contactA','contactB','refreshA','select'):return p[5]>0
    return False


def enabled(s,cfg,event):
    if not valid(s):return False
    if event=='act':
        word=PLANS.get(s.selected,())
        return s.pc<len(word) and primitive_enabled(s,word[s.pc])
    return primitive_enabled(s,event)


def primitive_step(s,cfg,event):
    assert primitive_enabled(s,event),(event,vector(s))
    if event.startswith('native:'):
        return plant_update(s,native_options(s)[event[7:]])
    if event in ('primeA','finishA'):
        p=list(s.core.plant);p[4]=0;p[3]=0
        return replace(plant_update(s,p),a=2 if event=='primeA' else 3)
    t=charge(s)
    if event in ('assemble','formA','formB'):
        p=list(t.core.plant);p[0]-=1;p[1]-=1;t=plant_update(t,p)
        if event=='assemble':t=replace(t,readers=t.readers+1)
        elif event=='formA':t=replace(t,a=1)
        else:t=replace(t,b=1)
    elif event in ('primeB','finishB'):
        t=replace(t,b=2 if event=='primeB' else 3)
    elif event in ('dissociateA','dissociateB'):
        p=list(t.core.plant);p[0]+=1;p[1]+=1;t=plant_update(t,p)
        t=replace(t,**({'a':4} if event=='dissociateA' else {'b':4}))
    elif event in ('contactA','refreshA','contactB'):
        is_a=event!='contactB';payload=(t.a if is_a else t.b)+1
        if event=='refreshA':
            if cfg.contact_mode==1:payload=0
            elif cfg.contact_mode==2:payload=t.snapshot_a
            elif cfg.contact_mode==3:payload=1
        t=replace(t,last_target=1 if is_a else 2,last_payload=payload)
        if payload:
            if is_a:t=replace(t,record_a=payload,snapshot_a=3 if payload==3 and t.snapshot_a==0 else t.snapshot_a)
            else:t=replace(t,record_b=payload,snapshot_b=3 if payload==3 and t.snapshot_b==0 else t.snapshot_b)
    elif event=='select':t=replace(t,selected=selection(t,cfg),pc=0)
    return t


def advance(s,cfg,event):
    assert enabled(s,cfg,event),(event,vector(s))
    if event=='act':t=replace(primitive_step(s,cfg,PLANS[s.selected][s.pc]),pc=s.pc+1)
    else:t=primitive_step(s,cfg,event)
    assert valid(t)
    assert C.energy(t.core.plant)+t.total_spent==C.energy(s.core.plant)+s.total_spent
    assert t.core.plant[5]+t.common_spent==s.core.plant[5]+s.common_spent
    assert t.readers>=s.readers and t.a>=s.a and t.b>=s.b
    assert (s.a!=3 or t.a==3) and (s.b!=3 or t.b==3)
    return t


class History:
    def __init__(self,cfg,initial):
        self.cfg=cfg;self.initial=initial;self.state=initial;self.steps=[];self.denied=[];self.milestones={}
    def do(self,event):
        before=self.state;effect=PLANS[before.selected][before.pc] if event=='act' else event
        self.state=advance(before,self.cfg,event)
        self.steps.append(dict(event=event,effect=effect,before=vector(before),after=vector(self.state)))
    def words(self,word):
        for event in word:self.do(event)
    def mark(self,name):self.milestones[name]=vector(self.state)
    def execute_selected(self):
        while self.state.pc<len(PLANS[self.state.selected]):
            if not enabled(self.state,self.cfg,'act'):
                self.denied.append(dict(event='act',effect=PLANS[self.state.selected][self.state.pc],state=vector(self.state)));break
            self.do('act')


PREFIX=['assemble']*3+['contactA','formA','primeA','contactA','formB','primeB','contactB']
CASES=[('completion_faithful',Config(),'complete'),('completion_stale',Config(contact_mode=2),'complete'),
    ('completion_missing',Config(contact_mode=1),'complete'),('completion_clamped',Config(clamp=True),'complete'),
    ('dissociation_faithful',Config(),'dissociate'),('dissociation_stale',Config(contact_mode=2),'dissociate'),
    ('unfinished_faithful',Config(),'unfinished'),('unfinished_false_absent',Config(contact_mode=3),'unfinished'),
    ('source_empty_faithful',Config(),'source_empty')]


def inherited_history():
    ancestor=C.ancestry();cfg=C.Config(later_repair=False)
    h=C.History(cfg,C.State(tuple(ancestor['final'])));h.words(C.TRAINING)
    assert h.state.plant==(29,30,1,1,1,274,215) and h.state.candidates==1 and not h.state.criterion_active
    return ancestor,dict(config=asdict(cfg),initial=C.vector(h.initial),events=C.TRAINING,
        steps=h.steps,final=C.vector(h.state)),h.state


def run_case(name,cfg,branch,initial):
    h=History(cfg,State(initial))
    for index,event in enumerate(PREFIX):
        h.do(event)
        if index==3:h.mark('empty_acquired')
        if index==6:h.mark('scope_A')
    h.mark('scope_AB');assert h.state.core.plant[5]==265
    if branch=='complete':h.words(['native:repair','native:capture','finishA'])
    elif branch=='dissociate':h.do('dissociateA')
    elif branch=='source_empty':
        h.do('native:repair')
        h.words(['native:capture','native:leak_local']*215)
        h.do('native:damage')
    h.mark('actual_branch')
    h.do('refreshA');h.mark('acquired_revision')
    h.words(['native:leak_common']*(262 if branch=='unfinished' else 261))
    h.mark('decision');assert h.state.core.plant[5]==2
    h.do('select');h.mark('selected');h.execute_selected();h.mark('final')
    return dict(name=name,config=asdict(cfg),branch=branch,initial=vector(h.initial),steps=h.steps,
        events=[r['event'] for r in h.steps],denied=h.denied,milestones=h.milestones,final=vector(h.state),
        actual_pending=actual_pending(h.state),acquired_pending=acquired_pending(h.state,cfg),
        product_A=h.state.a==3,product_B=h.state.b==3,selected=h.state.selected,
        damage_remaining=h.state.core.plant[3]==0)


def main():
    ancestor,training,initial=inherited_history()
    cases=[run_case(name,cfg,branch,initial) for name,cfg,branch in CASES];by={x['name']:x for x in cases}
    for name in ('completion_faithful','dissociation_faithful','source_empty_faithful'):
        assert by[name]['selected']==4 and by[name]['product_B']
    for name in ('completion_stale','completion_missing','completion_clamped','dissociation_stale'):
        assert by[name]['selected']==1 and not by[name]['product_B'] and len(by[name]['denied'])==1
    assert by['unfinished_faithful']['selected']==1 and by['unfinished_faithful']['product_A'] and not by['unfinished_faithful']['product_B']
    assert by['unfinished_false_absent']['product_B'] and not by['unfinished_false_absent']['product_A']
    assert 'A' in by['source_empty_faithful']['actual_pending'] and 'A' in by['source_empty_faithful']['acquired_pending']
    assert by['completion_faithful']['milestones']['decision']==by['completion_clamped']['milestones']['decision']
    paths=[Path(__file__),HERE/'SCOPE-PROTOCOL.md',HERE/'criterion.py',HERE/'CRITERION-PROTOCOL.md',
        HERE/'criterion-results.json',HERE/'study.py',HERE/'results.json',C.prior.FORMATION/'process.py',
        C.prior.FORMATION/'formal/FormedSelection.lean',Path(C.native.arithmetic.__file__)]+C.prior.preparation_sources()
    out=dict(status='passed',scope='Conditional material activity-scope formation, acquisition and operative revision',
        vector_columns=VECTOR_COLUMNS,ancestry=ancestor,criterion_training=training,cases=cases,
        source_hashes={str(p.relative_to(C.prior.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (HERE/'scope-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='passed',ancestral_events=len(ancestor['events']),training_events=len(training['events']),
        cases=[dict(name=x['name'],events=len(x['events']),selected=x['selected'],A=x['product_A'],B=x['product_B'],
                    pending=x['actual_pending'],acquired=x['acquired_pending']) for x in cases]),indent=2))


if __name__=='__main__':main()
