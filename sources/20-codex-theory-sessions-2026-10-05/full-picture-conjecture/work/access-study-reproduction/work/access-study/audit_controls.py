"""Independent latent-event checks for frozen nonbaseline control kernels."""
import sys
sys.dont_write_bytecode=True
from collections import defaultdict
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
import time
import model as m

HERE=Path(__file__).resolve().parent
assert Path(m.__file__).resolve()==HERE/'model.py'

def norm(s,c):
    n,x,b,k,r,p,d=s
    if x==0 or n==0:return m.State(0,x,b,k,0,Q(0),d)
    if d==0:
        total=b+k;b=min(c.cap,total);k=total-b
    return m.State(n,x,b,k,r,p,d)

def legal(s,c):
    out=[]
    infrastructure=[('drop',0)]
    if s.ready and s.cash>=c.upkeep:infrastructure.append(('keep',c.upkeep))
    if not s.ready and s.cash>=c.rebuild:infrastructure.append(('rebuild',c.rebuild))
    for support,fee in infrastructure:
        tests=(False,True) if support=='keep' and s.cash>=fee+c.test else (False,)
        for test in tests:
            labels=('positive','negative') if test else ('none',)
            opts=(0,1) if s.cash-fee-test*c.test>=c.repair else (0,)
            for prescription in product(opts,repeat=len(labels)):
                out.append((support,test,tuple(zip(labels,prescription))))
    return out

def direct(s,action,c):
    support,test,rr=action;rr=dict(rr)
    fee={'drop':0,'keep':c.upkeep,'rebuild':c.rebuild}[support]
    stages=[Q(0)]*len(m.METRICS)
    grouped=defaultdict(lambda:[Q(0),Q(0)])
    for h,ph in ((0,1-s.belief),(1,s.belief)):
        if test:
            pos=c.sensitivity if h else 1-c.specificity
            signals=(('positive',pos),('negative',1-pos))
        else:signals=(('none',Q(1)),)
        for sig,ps in signals:
            repair=rr[sig];bill=fee+c.test*test+c.repair*repair
            assert bill<=s.cash
            effective=0 if repair else h
            risk=c.damage_fault if effective else c.damage_healthy
            for damage,pd in ((0,1-risk),(1,risk)):
                pr=ph*ps*pd
                if not pr:continue
                xp=max(0,min(c.stock_cap,s.stock+1+repair-2*damage))
                income=c.output_rate*xp
                free=s.cash-bill+income
                bp=min(c.cap,free);kp=s.treasury+free-bp
                assert bp+kp+bill==s.cash+s.treasury+income
                stages[m.INDEX['expense']]+=pr*bill
                stages[m.INDEX['burden']]+=pr*(c.test_burden*test+(1-h)*repair)
                stages[m.INDEX['tests']]+=pr*test
                stages[m.INDEX['repairs']]+=pr*repair
                stages[m.INDEX['rebuilds']]+=pr*(support=='rebuild')
                stages[m.INDEX['upkeep']]+=pr*(support=='keep')
                stages[m.INDEX['inquiry_expense']]+=pr*(fee+c.test*test)
                stages[m.INDEX['output']]+=pr*income
                dnext=max(0,s.unlock-1) if s.unlock>=0 else -1
                pub=(sig,xp,bp,kp,int(support!='drop'),dnext)
                pn=1-c.clearance if effective else c.onset
                grouped[pub][0]+=pr*(1-pn);grouped[pub][1]+=pr*pn
    branches=defaultdict(Q)
    for (sig,xp,bp,kp,rp,dn),(m0,m1) in grouped.items():
        pr=m0+m1
        child=norm(m.State(s.remaining-1,xp,bp,kp,rp,m1/pr,dn),c)
        branches[(sig,child)]+=pr
    assert sum(branches.values())==1
    return tuple(stages),branches

configs={
    'output_zero':replace(m.Config(),output_rate=0),
    'onset_and_healthy_damage_zero':replace(m.Config(),onset=Q(0),damage_healthy=Q(0)),
    'uninformative_test':replace(m.Config(),sensitivity=Q(1,2),specificity=Q(1,2)),
}
counts=defaultdict(int);started=time.perf_counter()
for name,cfg in configs.items():
    engine=m.Engine(cfg)
    states=set()
    for h,x,b,k,r,p,d in product((1,2),(1,2,3),range(9),(0,3),(0,1),(Q(0),Q(1,2),Q(1)),(-1,0,1)):
        s=norm(m.State(h,x,b,k,r,p,d),cfg)
        if s in states:continue
        states.add(s);counts['control_states']+=1
        actions=engine.actions(s)
        keys=[(a.support,a.test,a.repair_rule) for a in actions]
        assert keys==legal(s,cfg)
        direct_vectors=[]
        for a,key in zip(actions,keys):
            stage,expected=direct(s,key,cfg)
            assert a.stage==stage,(name,s,key,'stage')
            actual=defaultdict(Q)
            for br in a.branches:actual[(br.signal,br.child)]+=br.probability
            assert actual==expected,(name,s,key,'branches')
            counts['control_action_kernels']+=1
            counts['control_branch_masses']+=len(actual)
            if s.remaining==1:
                v=list(stage)
                for (_,child),pr in expected.items():
                    v[0]+=pr*(child.stock==0);v[3]+=pr*(child.stock<2)
                    v[10]+=pr*child.cash;v[11]+=pr*child.treasury
                direct_vectors.append(tuple(v))
        if s.remaining==1:
            for weight in m.WEIGHTS.values():
                expected=min(sum(w*v for w,v in zip(weight,vec[:4])) for vec in direct_vectors)
                values,_=engine.solve(s,weight)
                actual=sum(w*v for w,v in zip(weight,values[:4]))
                assert actual==expected
                counts['independent_control_H1_optima']+=1
out={'status':'passed','runtime_seconds':time.perf_counter()-started,
     'counts':dict(counts),'configurations':list(configs),
     'scope':'exact stage vectors and next-observation/posterior laws at H1/H2 states; independent H1 optimal values; not independent H4 control optima',
     'model_sha256':sha256((HERE/'model.py').read_bytes()).hexdigest()}
(HERE/'audit_control_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
