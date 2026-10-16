"""Finite belief MDP with exact rational posteriors and paid productive cash."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import numpy as np


METRICS=('cost','burden','tests','target_absent_repairs','repairs','standby','rebuilds',
         'expense','output','failure','terminal_stock','terminal_cash','treasury')
IDX={name:i for i,name in enumerate(METRICS)}


@dataclass(frozen=True)
class Params:
    horizon:int=5
    stock_cap:int=3
    cash_cap:int=8
    initial_stock:int=3
    initial_cash:int=8
    initial_ready:int=1
    initial_fault_probability:str='0'
    onset:str='0.1'
    clearance:str='0.05'
    damage_healthy:str='0.1'
    damage_fault:str='0.8'
    sensitivity:str='0.9'
    specificity:str='0.9'
    output_per_stock:int=2
    upkeep_cost:int=1
    rebuild_cost:int=3
    test_cost:int=2
    repair_cost:int=3
    terminal_stock_value:float=2
    failure_cost:float=12
    test_burden:float=.05


def diagnostic(p,cfg):
    """label, exact probability, exact posterior; no hidden truth is returned."""
    out=[]
    for label,like1,like0 in [('positive',F(cfg.sensitivity),1-F(cfg.specificity)),
                              ('negative',1-F(cfg.sensitivity),F(cfg.specificity))]:
        mass=p*like1+(1-p)*like0
        if mass:out.append((label,mass,p*like1/mass))
    return out


def production(p,x,repair,cfg):
    """Update once from joint visible stock/output, including clipping."""
    effective=F(0) if repair else p
    groups={}
    for theta,prior in ((0,1-effective),(1,effective)):
        q=F(cfg.damage_fault if theta else cfg.damage_healthy)
        for damage,prob in ((0,1-q),(1,q)):
            xp=max(0,min(cfg.stock_cap,x+1+repair-2*damage))
            masses=groups.setdefault(xp,[F(0),F(0)])
            masses[theta]+=prior*prob
    out=[]
    for xp,(m0,m1) in sorted(groups.items()):
        total=m0+m1
        if not total:continue
        posterior=m1/total
        next_p=F(cfg.onset)+(1-F(cfg.onset)-F(cfg.clearance))*posterior
        out.append((xp,total,next_p))
    return out


class BeliefMDP:
    def __init__(self,cfg=Params(),mode='adaptive'):
        if mode not in ('adaptive','no_test','continuous'):raise ValueError(mode)
        self.cfg=cfg;self.mode=mode
        self.nodes=[];self.index={};self.levels=[[] for _ in range(cfg.horizon+1)]
        self.root=self.node(cfg.horizon,cfg.initial_stock,cfg.initial_cash,cfg.initial_ready,F(cfg.initial_fault_probability))
        self.order=[i for level in self.levels for i in level]

    def node(self,t,x,b,ready,p):
        if x==0:t=0;ready=0;p=F(0)
        if t==0:ready=0;p=F(0)
        key=(t,x,b,ready,p)
        if key in self.index:return self.index[key]
        i=len(self.nodes);self.index[key]=i
        node={'state':key,'actions':[]}
        self.nodes.append(node);self.levels[t].append(i)
        cfg=self.cfg
        if t==0:
            terminal=np.zeros(len(METRICS))
            terminal[IDX['cost']]=-cfg.terminal_stock_value*x+cfg.failure_cost*(x==0)
            terminal[IDX['failure']]=float(x==0)
            terminal[IDX['terminal_stock']]=x
            terminal[IDX['terminal_cash']]=b
            node['terminal']=terminal
            return i
        infra=[('drop',0,0)]
        if ready and b>=cfg.upkeep_cost:infra.append(('keep',cfg.upkeep_cost,1))
        if not ready and b>=cfg.rebuild_cost:infra.append(('rebuild',cfg.rebuild_cost,1))
        if self.mode=='continuous':
            preferred='keep' if ready else 'rebuild'
            selected=[item for item in infra if item[0]==preferred]
            if selected:infra=selected
        for support,fee,next_ready in infra:
            test_options=[False]
            can_test=bool(ready and support=='keep' and b>=fee+cfg.test_cost)
            if can_test and self.mode!='no_test':test_options.append(True)
            if can_test and self.mode=='continuous':test_options=[True]
            for test in test_options:
                upfront=fee+cfg.test_cost*test
                observations=diagnostic(p,cfg) if test else [('none',F(1),p)]
                choices=(0,1) if b-upfront>=cfg.repair_cost else (0,)
                for prescription in product(choices,repeat=len(observations)):
                    stage=np.zeros(len(METRICS));branches=[]
                    stage[IDX['tests']]=test
                    stage[IDX['burden']]=cfg.test_burden*test
                    stage[IDX['standby']]=int(support=='keep' and not test)
                    stage[IDX['rebuilds']]=int(support=='rebuild')
                    for (label,po,posterior),repair in zip(observations,prescription):
                        spend=upfront+cfg.repair_cost*repair
                        if spend>b:raise AssertionError('prefix finance')
                        target_absent=float(po*(1-posterior))*repair
                        stage[IDX['burden']]+=target_absent
                        stage[IDX['target_absent_repairs']]+=target_absent
                        stage[IDX['repairs']]+=float(po)*repair
                        stage[IDX['expense']]+=float(po)*spend
                        for xp,pout,pnext in production(posterior,x,repair,cfg):
                            output=cfg.output_per_stock*xp
                            raw=b-spend+output
                            bp=min(cfg.cash_cap,raw)
                            treasury=raw-bp
                            probability=float(po*pout)
                            child=self.node(t-1,xp,bp,next_ready,pnext)
                            stage[IDX['output']]+=probability*output
                            stage[IDX['treasury']]+=probability*treasury
                            branches.append({'probability':probability,'next':child,'observation':label,
                                             'repair':repair,'next_stock':xp,'expense':spend,
                                             'output':output,'treasury':treasury})
                    stage[IDX['cost']]=stage[IDX['expense']]-stage[IDX['output']]
                    node['actions'].append({'support':support,'test':test,
                                            'repair_rule':dict(zip([o[0] for o in observations],prescription)),
                                            'stage':stage,'branches':branches})
        assert node['actions']
        return i

    def compile_levels(self):
        """Numerical arrays for the exact finite DAG, leaving original nodes auditable."""
        self.arrays=[]
        for level in self.levels[1:]:
            if not level:continue
            aa=max(len(self.nodes[i]['actions']) for i in level)
            bb=max(len(a['branches']) for i in level for a in self.nodes[i]['actions'])
            shape=(len(level),aa)
            c=np.full(shape,np.inf);h=np.full(shape,np.inf)
            child=np.zeros(shape+(bb,),dtype=int);pr=np.zeros(shape+(bb,))
            for row,i in enumerate(level):
                for col,a in enumerate(self.nodes[i]['actions']):
                    c[row,col]=a['stage'][IDX['cost']];h[row,col]=a['stage'][IDX['burden']]
                    for k,br in enumerate(a['branches']):
                        child[row,col,k]=br['next'];pr[row,col,k]=br['probability']
            self.arrays.append((np.array(level),c,h,child,pr))

    def solve(self,multiplier=0.,minimize_burden=False):
        if not hasattr(self,'arrays'):self.compile_levels()
        count=len(self.nodes)
        cost=np.zeros(count);harm=np.zeros(count);policy=np.full(count,-1,dtype=int)
        for i in self.levels[0]:cost[i]=self.nodes[i]['terminal'][IDX['cost']]
        for ids,stage_c,stage_h,child,pr in self.arrays:
            c=stage_c+np.sum(pr*cost[child],axis=2)
            h=stage_h+np.sum(pr*harm[child],axis=2)
            if minimize_burden:v=h
            elif multiplier==0:v=c
            else:v=c+multiplier*h
            # Primary v, then burden, then cost, then action index: original tie rule.
            indices=np.broadcast_to(np.arange(c.shape[1]),c.shape)
            order=np.lexsort((indices,c,h,v),axis=1)
            best=order[:,0];rows=np.arange(len(ids))
            cost[ids]=c[rows,best];harm[ids]=h[rows,best];policy[ids]=best
        value=harm[self.root] if minimize_burden else cost[self.root]+multiplier*harm[self.root]
        return {'multiplier':None if minimize_burden else multiplier,
                'cost':float(cost[self.root]),'burden':float(harm[self.root]),
                'lagrange_value':float(value),'policy':policy}

    def evaluate(self,solution,include_policy=False):
        values=np.zeros((len(self.nodes),len(METRICS)))
        policy=solution['policy']
        for i in self.order:
            node=self.nodes[i]
            if 'terminal' in node:values[i]=node['terminal'];continue
            action=node['actions'][policy[i]]
            values[i]=action['stage']
            for branch in action['branches']:values[i]+=branch['probability']*values[branch['next']]
        out=dict(zip(METRICS,map(float,values[self.root])))
        out['multiplier']=solution['multiplier']
        out['root_action']=self.action_description(self.root,policy)
        out['conservation_residual']=out['terminal_cash']-self.cfg.initial_cash+out['treasury']+out['expense']-out['output']
        if include_policy:
            reached={self.root:1.}
            records=[]
            for i in reversed(self.order):
                mass=reached.get(i,0.)
                if not mass or 'terminal' in self.nodes[i]:continue
                action=self.nodes[i]['actions'][policy[i]]
                records.append({'state':self.state_description(i),'reach_probability':mass,
                                'action':self.action_description(i,policy)})
                for br in action['branches']:reached[br['next']]=reached.get(br['next'],0.)+mass*br['probability']
            out['reachable_policy']=records
            out['witness']=self.witness(policy)
        return out

    def state_description(self,i):
        t,x,b,r,p=self.nodes[i]['state']
        return {'remaining':t,'stock':x,'cash':b,'ready':r,'fault_probability':str(p)}

    def action_description(self,i,policy):
        if policy[i]<0:return None
        a=self.nodes[i]['actions'][policy[i]]
        return {k:a[k] for k in ('support','test','repair_rule')}

    def witness(self,policy):
        """Most probable path with some paid diagnosis after an untested round."""
        found=[]
        def visit(i,mass,path,paused,reopened):
            node=self.nodes[i]
            if 'terminal' in node:
                if reopened:found.append((mass,path))
                return
            action=node['actions'][policy[i]]
            reopening=paused and action['test']
            for br in action['branches']:
                row={'state':self.state_description(i),'action':self.action_description(i,policy),
                     'observation':br['observation'],'repair':br['repair'],'next_stock':br['next_stock'],
                     'expense':br['expense'],'output':br['output'],'next_state':self.state_description(br['next'])}
                visit(br['next'],mass*br['probability'],path+[row],not action['test'],reopened or reopening)
        visit(self.root,1.,[],False,False)
        if not found:return None
        probability,path=max(found,key=lambda v:v[0])
        return {'probability':probability,'path':path,'selection':'most probable path with a test after an untested round, not a representative random run'}


def constrained(mdp,budget,tolerance=1e-8,max_iterations=45):
    """Primal mixture and valid Lagrange lower bound; report actual optimality gap."""
    if not hasattr(mdp,'minimum_burden_solution'):mdp.minimum_burden_solution=mdp.solve(minimize_burden=True)
    minimum=mdp.minimum_burden_solution['burden']
    if budget<minimum-1e-12:
        return {'feasible':False,'minimum_burden':minimum,'budget':budget,'components':[]}
    loose=mdp.solve(0.)
    if loose['burden']<=budget:
        return {'feasible':True,'minimum_burden':minimum,'components':[(1.,loose)],'cost':loose['cost'],'burden':loose['burden'],
                'dual_lower_bound':loose['cost'],'optimality_gap':0.,'supporting_multiplier':0.}
    low=0.;high=1.;tight=mdp.solve(high)
    while tight['burden']>budget:
        high*=2;tight=mdp.solve(high)
        if high>1e8:raise RuntimeError('no burden-feasible bracket')
    best_lower=max(loose['lagrange_value'],tight['lagrange_value']-high*budget)
    for _ in range(max_iterations):
        mid=(low+high)/2
        result=mdp.solve(mid)
        best_lower=max(best_lower,result['lagrange_value']-mid*budget)
        if result['burden']>budget:low=mid;loose=result
        else:high=mid;tight=result
        w=(budget-tight['burden'])/(loose['burden']-tight['burden'])
        upper=w*loose['cost']+(1-w)*tight['cost']
        if upper-best_lower<=tolerance:break
    return {'feasible':True,'minimum_burden':minimum,'components':[(float(w),loose),(float(1-w),tight)],'cost':float(upper),
            'burden':float(w*loose['burden']+(1-w)*tight['burden']),
            'dual_lower_bound':float(best_lower),'optimality_gap':float(max(0.,upper-best_lower)),
            'supporting_multiplier':(low+high)/2,'multiplier_bracket':[low,high]}


def summarize(mdp,result,include_policy=False):
    if not result.get('feasible',True):
        return {**{k:v for k,v in result.items() if k!='components'},'mode':mdp.mode,'state_count':len(mdp.nodes)}
    evaluations=[(w,mdp.evaluate(sol,include_policy)) for w,sol in result['components']]
    metrics={key:sum(w*ev[key] for w,ev in evaluations) for key in METRICS}
    return {**{k:v for k,v in result.items() if k!='components'},'metrics':metrics,
            'components':[{'probability':w,**ev} for w,ev in evaluations],
            'state_count':len(mdp.nodes),'action_count':sum(len(n['actions']) for n in mdp.nodes),
            'mode':mdp.mode}
