"""Full public-history flow with two half-owners and contingent compensation."""
from dataclasses import dataclass,asdict
from fractions import Fraction as Q
from functools import lru_cache
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix,vstack
from scipy.optimize import linprog
from upstream_model import Params, diagnostic, production

METRICS=('loss_a','loss_b','failure','expense','output','compensation','repairs','tests','terminal_cash','treasury')
IX={k:i for i,k in enumerate(METRICS)}

@dataclass(frozen=True)
class ParticipationParams:
    horizon:int=2
    initial_stock:int=1
    initial_cash:int=4
    initial_ready:int=1
    initial_fault_probability:str='1/2'
    compensation_grid:tuple=(0,1,2)
    repair_burden:float=1.
    collapse_loss:float=1.
    total_test_burden:float=.05


class PublicTree:
    def __init__(self,cfg=ParticipationParams()):
        self.cfg=cfg
        self.physical=Params(horizon=cfg.horizon,initial_stock=cfg.initial_stock,
            initial_cash=cfg.initial_cash,initial_ready=cfg.initial_ready,
            initial_fault_probability=cfg.initial_fault_probability)
        self.nodes=[];self.actions=[];self.roots=[]
        self._passive=lru_cache(None)(self._passive_calculation)
        if cfg.horizon<1 or cfg.initial_stock<1:raise ValueError('Study requires a living initial stock and positive horizon')
        for worker in (0,1):
            self.roots.append(self.node(cfg.horizon,cfg.initial_stock,cfg.initial_cash,cfg.initial_ready,Q(cfg.initial_fault_probability),worker,'opening',None,[]))
        self.build_matrices()

    def terminal(self,x,b):
        v=np.zeros(len(METRICS));v[IX['failure']]=float(x==0)
        v[:2]=self.cfg.collapse_loss*(x==0);v[IX['terminal_cash']]=b
        return v

    def _passive_calculation(self,t,x,b,p):
        if t==0 or x==0:return tuple(self.terminal(x,b))
        result=np.zeros(len(METRICS))
        for xp,prob,pp in production(p,x,0,self.physical):
            output=self.physical.output_per_stock*xp;bp=min(self.physical.cash_cap,b+output)
            treasury=b+output-bp
            local=np.zeros(len(METRICS));local[:2]=-output/2
            local[IX['output']]=output;local[IX['treasury']]=treasury
            result+=float(prob)*(local+np.asarray(self._passive(t-1,xp,bp,pp)))
        return tuple(result)

    def passive(self,t,x,b,p):return np.asarray(self._passive(t,x,b,p))

    def node(self,t,x,b,ready,p,worker,phase,parent,ancestors):
        i=len(self.nodes)
        n={'id':i,'t':t,'stock':x,'cash':b,'ready':ready,'p':p,'worker':worker,'phase':phase,
           'parent_action':parent,'ancestors':tuple(ancestors),'actions':[],
           'outside':self.passive(t,x,b,p)[:2].copy()}
        self.nodes.append(n)
        self.action(n,{'kind':'retire'},self.passive(t,x,b,p).copy(),[])
        if phase=='opening':
            supports=[('drop',0,0)]
            if ready and b>=1:supports.append(('keep',1,1))
            if not ready and b>=3:supports.append(('rebuild',3,1))
            for support,fee,next_ready in supports:
                for test in (False,True):
                    if test and not (ready and support=='keep' and b>=fee+2):continue
                    if fee+2*test>b:continue
                    obs=diagnostic(p,self.physical) if test else [('none',Q(1),p)]
                    v=np.zeros(len(METRICS));spend=fee+2*test
                    v[:2]=spend/2+self.cfg.total_test_burden*test/2
                    v[IX['expense']]=spend;v[IX['tests']]=test
                    j=self.action(n,{'kind':'inquiry','support':support,'test':test,'expense':spend},v,[])
                    for label,mass,post in obs:
                        child=self.node(t,x,b-spend,next_ready,post,worker,'response',j,ancestors+[j])
                        self.actions[j]['branches'].append({'probability':float(mass),'child':child,'label':label})
        else:
            for repair in (0,1):
                for payment in (self.cfg.compensation_grid if repair else (0,)):
                    spend=3*repair+payment
                    if spend>b:continue
                    v=np.zeros(len(METRICS));v[:2]=3*repair/2+payment/2
                    v[worker]+=self.cfg.repair_burden*repair-payment
                    v[IX['expense']]=3*repair;v[IX['compensation']]=payment;v[IX['repairs']]=repair
                    j=self.action(n,{'kind':'response','repair':repair,'compensation':payment,'recipient':worker,'expense':3*repair},v,[])
                    for xp,mass,pp in production(p,x,repair,self.physical):
                        output=self.physical.output_per_stock*xp;bp=min(self.physical.cash_cap,b-spend+output)
                        treasury=b-spend+output-bp;prob=float(mass)
                        self.actions[j]['stage'][:2]-=prob*output/2
                        self.actions[j]['stage'][IX['output']]+=prob*output
                        self.actions[j]['stage'][IX['treasury']]+=prob*treasury
                        if t==1 or xp==0:
                            self.actions[j]['stage']+=prob*self.terminal(xp,bp)
                            self.actions[j]['branches'].append({'probability':prob,'child':None,'next_stock':xp,'next_cash':bp,'output':output,'treasury':treasury})
                        else:
                            for next_worker in (0,1):
                                child=self.node(t-1,xp,bp,ready,pp,next_worker,'opening',j,ancestors+[j])
                                self.actions[j]['branches'].append({'probability':prob/2,'child':child,'next_stock':xp,'next_cash':bp,'output':output,'treasury':treasury,'next_worker':next_worker})
        return i

    def action(self,node,description,stage,branches):
        j=len(self.actions);self.actions.append({'id':j,'node':node['id'],'description':description,'stage':stage,'branches':branches})
        node['actions'].append(j);return j

    def build_matrices(self):
        nn=len(self.nodes);na=len(self.actions);rr=[];cc=[];vv=[]
        for a in self.actions:
            j=a['id'];rr.append(a['node']);cc.append(j);vv.append(1.)
            for branch in a['branches']:
                if branch['child'] is not None:rr.append(branch['child']);cc.append(j);vv.append(-branch['probability'])
        self.flow=coo_matrix((vv,(rr,cc)),shape=(nn,na)).tocsr();self.rhs=np.zeros(nn)
        for i in self.roots:self.rhs[i]=.5
        self.metrics=np.stack([a['stage'] for a in self.actions],axis=1)
        # At each public recommendation, descendant occupied costs are its reach-weighted continuation loss.
        rr=[];cc=[];vv=[]
        for a in self.actions:
            j=a['id'];node=self.nodes[a['node']]
            for ancestor in list(node['ancestors'])+[j]:
                for party in (0,1):
                    value=a['stage'][party]
                    if value:rr.append(2*ancestor+party);cc.append(j);vv.append(value)
            for party in (0,1):
                value=-node['outside'][party]
                if value:rr.append(2*j+party);cc.append(j);vv.append(value)
        self.participation=coo_matrix((vv,(rr,cc)),shape=(2*na,na)).tocsr()
        self.initial_outside=self.passive(self.cfg.horizon,self.cfg.initial_stock,self.cfg.initial_cash,Q(self.cfg.initial_fault_probability))[:2]
        self.options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9}

    def solve(self,mode='continuing',details=False):
        if mode not in ('ex_ante','continuing'):raise ValueError(mode)
        A=csr_matrix(self.metrics[:2]);b=self.initial_outside.copy()
        if mode=='continuing':A=vstack([A,self.participation],format='csr');b=np.r_[b,np.zeros(self.participation.shape[0])]
        fit=linprog(self.metrics[IX['failure']],A_eq=self.flow,b_eq=self.rhs,A_ub=A,b_ub=b,bounds=(0,None),method='highs',options=self.options)
        if not fit.success:raise RuntimeError(fit.message)
        primary=fit
        # Reporting tie rule: retain best failure, then minimize physical expense,
        # then current transfers. This is not either owner's personal objective.
        eq=vstack([self.flow,csr_matrix(self.metrics[[IX['failure']]])],format='csr')
        rhs=np.r_[self.rhs,primary.fun]
        second=linprog(self.metrics[IX['expense']],A_eq=eq,b_eq=rhs,A_ub=A,b_ub=b,bounds=(0,None),method='highs',options=self.options)
        if not second.success:raise RuntimeError(second.message)
        eq=vstack([eq,csr_matrix(self.metrics[[IX['expense']]])],format='csr');rhs=np.r_[rhs,second.fun]
        third=linprog(self.metrics[IX['compensation']],A_eq=eq,b_eq=rhs,A_ub=A,b_ub=b,bounds=(0,None),method='highs',options=self.options)
        if not third.success:raise RuntimeError(third.message)
        occupancy=third.x
        ev=self.evaluate(occupancy,details)
        replay=self.evaluate(occupancy,False,True)
        measured=self.metrics@occupancy
        residual=float(np.max(np.abs(self.flow@occupancy-self.rhs)))
        report={'mode':mode,'config':asdict(self.cfg),'metrics':dict(zip(METRICS,map(float,measured))),
                'initial_outside_loss':self.initial_outside.tolist(),
                'veto_replay_metrics':dict(zip(METRICS,map(float,replay['vector']))),
                'maximum_conditional_refusal_gain':ev['max_gain'],
                'maximum_reach_weighted_violation':float(max(0.,np.max(self.participation@occupancy))),
                'flow_residual':residual,'policy_evaluation_residual':float(np.max(np.abs(ev['vector']-measured))),
                'duality_gap':float(fit.fun-(self.rhs@fit.eqlin.marginals+b@fit.ineqlin.marginals)),
                'minimum_failure':float(primary.fun),'minimum_expense_at_best_failure':float(second.fun),
                'node_count':len(self.nodes),'action_count':len(self.actions),
                'cash_conservation_residual':float(measured[IX['terminal_cash']]-self.cfg.initial_cash+measured[IX['expense']]+measured[IX['compensation']]+measured[IX['treasury']]-measured[IX['output']]),
                'loss_sum_residual':float(measured[0]+measured[1]-(measured[IX['expense']]-measured[IX['output']]+self.cfg.repair_burden*measured[IX['repairs']]+self.cfg.total_test_burden*measured[IX['tests']]+2*self.cfg.collapse_loss*measured[IX['failure']]))}
        if details:report['policy']=ev['policy'];report['largest_refusal_witness']=ev['witness']
        return report

    def evaluate(self,occupancy,details=False,veto=False):
        values=np.zeros((len(self.nodes),len(METRICS)));action_values={};records=[];max_gain=0.;witness=None
        for n in reversed(self.nodes):
            ids=n['actions'];mass=float(np.sum(occupancy[ids]));probs=occupancy[ids]/mass if mass>0 else np.eye(1,len(ids),0)[0]
            for pr,j in zip(probs,ids):
                a=self.actions[j];v=a['stage'].copy()
                for br in a['branches']:
                    if br['child'] is not None:v+=br['probability']*values[br['child']]
                if veto and np.any(v[:2]>n['outside']+1e-8):
                    v=self.passive(n['t'],n['stock'],n['cash'],n['p']).copy()
                values[n['id']]+=pr*v;action_values[j]=v
                if occupancy[j]>0:
                    gains=v[:2]-n['outside'];g=float(np.max(gains))
                    if g>max_gain:
                        max_gain=g;witness={'node':self.describe(n),'action':a['description'],'action_occupancy':float(occupancy[j]),'continuation_losses':v[:2].tolist(),'refusal_losses':n['outside'].tolist(),'refusal_gains':gains.tolist()}
                    if details:records.append({'node':self.describe(n),'action_index':j,'action':a['description'],'action_probability':float(pr),'action_occupancy':float(occupancy[j]),'continuation_losses':v[:2].tolist(),'refusal_losses':n['outside'].tolist()})
        return {'vector':sum(.5*values[i] for i in self.roots),'max_gain':max_gain,'witness':witness,'policy':records}

    def describe(self,n):
        return {'id':n['id'],'remaining':n['t'],'phase':n['phase'],'stock':n['stock'],'cash':n['cash'],'ready':n['ready'],'fault_probability':str(n['p']),'worker':n['worker'],'parent_action':n['parent_action']}
