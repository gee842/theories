"""Independent pre-freeze implementation audit; development seeds only."""
from dataclasses import replace
from pathlib import Path
import hashlib,json,subprocess,sys
import integrated_model as m
import audit_recorded_integration as saved_audit

root=Path(__file__).parent
class AuditInstitution(m.Institution):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,trace_ledger=True,**kwargs)
        self.fitting_credits=0
    def pay(self,amount,category,t):
        success=super().pay(amount,category,t)
        if success and category=='model_fitting':
            assert amount%self.cfg.fit_price==0
            self.fitting_credits+=amount//self.cfg.fit_price
        return success

class AuditWorld(m.World):
    def __init__(self,scenario,seed,owner):
        super().__init__(scenario,seed);self.owner=owner;self.sample_calls=0;self.contexts=set();self.paid_samples=0
    def context(self,t,g,stage,j,k):
        self.contexts.add((t,g,stage,j,k))
        return super().context(t,g,stage,j,k)
    def sample(self,t,g,stage,j,k,forced_row=None):
        self.sample_calls+=1
        if stage=='ordinary':
            assert (t,g,stage,j,k) in self.contexts
            assert any(tr['round']==t and tr['category']=='ordinary_operation' and tr['direction']=='pay' for tr in self.owner.ledger_transactions[-8:])
        else:
            assert self.owner.checker
            tr=self.owner.ledger_transactions[-1]
            assert tr['direction']=='pay' and tr['category']=='evidence_'+stage
            assert tr['round']==t and tr['before']>=tr['amount']
            self.paid_samples+=1
        return super().sample(t,g,stage,j,k,forced_row)

def audit_runs():
    real_fit=m.fit;current=None
    def prepaid_fit(fields,labels):
        assert current.fitting_credits>0,'A fitted table ran before its computation was paid.'
        current.fitting_credits-=1
        return real_fit(fields,labels)
    m.fit=prepaid_fit
    records=[];details=[]
    try:
        for scenario in m.SCENARIOS:
            for arm in m.ARMS:
                current=AuditInstitution(m.Config(),arm)
                world=AuditWorld(scenario,1103,current)
                record=current.run(world)
                assert current.fitting_credits==0
                accepted,checks=saved_audit.audit_record(record)
                assert world.paid_samples==sum(record['paid_observations_by_stage'].values())
                details.append({'scenario':scenario,'arm':arm,'accepted':len(accepted),
                                'nonpositive_accepted':sum(x['nonpositive'] for x in accepted),
                                'paid_observations':world.paid_samples,'cash':record['final_cash']})
                # Compact record sufficient to compare standard and -O execution.
                records.append({k:record[k] for k in ('scenario','seed','arm','final_cash','receipts','expenses','counts','reviews','rule_changes','mandate_changes','checker_losses','checker_rebuilds','final_mandate','final_prefix')})
    finally:m.fit=real_fit
    return records,details

def boundaries():
    cfg=replace(m.Config(),initial_cash=0)
    owner=AuditInstitution(cfg,'full');world=AuditWorld('emerging',1103,owner)
    try:owner.take(world,100,'B','boundary',0)
    except RuntimeError:pass
    else:raise AssertionError('Unfunded observation proceeded')
    assert world.sample_calls==0 and owner.cash==0
    owner.checker=False
    try:owner.take(world,100,'B','boundary',1)
    except RuntimeError:pass
    else:raise AssertionError('Observation proceeded without declared capability')
    assert world.sample_calls==0
    model=m.Model((),(0,)*8,0)
    owner.package=m.Package(True,(model,model))
    owner.serve(world,world.quotes(100,cfg),100)
    assert world.sample_calls==0 and all(v['unserved']==1 for v in owner.counts.values())
    owner.review(world,100,['B_grievance'])
    assert world.sample_calls==0 and owner.review_index==0
    return {'unfunded_observation_calls':0,'missing_capability_observation_calls':0,'unfunded_service_observation_calls':0,'blocked_review_spent_alpha':False}

if __name__=='__main__':
    records,detail=audit_runs();boundary=boundaries()
    digest=hashlib.sha256(json.dumps(records,sort_keys=True).encode()).hexdigest()
    if '--compact' in sys.argv:print(digest)
    else:
        optimized=subprocess.check_output([sys.executable,'-O',str(Path(__file__)),'--compact'],text=True).strip()
        # Under -O this auditor's assert checks are disabled, but the production
        # record digest still proves debits/decisions did not disappear with them.
        assert optimized==digest
        result={'source_sha256':hashlib.sha256((root/'integrated_model.py').read_bytes()).hexdigest(),
                'development_seed':1103,'runs':len(records),'all_acquisitions_and_fits_prepaid':True,
                'ledger_and_fresh_check_math_independently_verified':True,
                'optimized_python_behavior_digest_identical':True,'behavior_sha256':digest,
                'boundary_checks':boundary,'run_details':detail,
                'scope':'No held-out seed run. Fixed source domain and root-approved synchronous settlement/centrally represented interests.'}
        (root/'implementation-audit-results.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k!='run_details'},indent=2))
