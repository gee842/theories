"""Attainable expected consequences on an unchanged finite belief graph."""
from dataclasses import dataclass
import numpy as np
from scipy.optimize import linprog, OptimizeResult
from scipy.sparse import coo_matrix, hstack, csr_matrix
from upstream_model import Params, BeliefMDP, IDX, diagnostic

NAMES=('failure','burden','net_expense')


@dataclass(frozen=True)
class Access:
    name:str='full'
    diagnostics:bool=True
    repairs:bool=True
    spending_cap:int|None=None
    repair_posterior_floor:float=0.
    response_posterior_floor:float=0.

    def permits(self,node,action,cfg):
        if action['test'] and not self.diagnostics:return False
        if not self.repairs and any(action['repair_rule'].values()):return False
        if self.spending_cap is not None and any(b['expense']>self.spending_cap for b in action['branches']):return False
        # This floor uses the publicly available pre-diagnostic opening belief.
        # It is an explicit rule denying contingent repair permissions in advance.
        if float(node['state'][4])<self.repair_posterior_floor and any(action['repair_rule'].values()):return False
        if self.response_posterior_floor>0:
            p=node['state'][4]
            posteriors={label:posterior for label,_,posterior in diagnostic(p,cfg)} if action['test'] else {'none':p}
            if any(repair and float(posteriors[label])<self.response_posterior_floor
                   for label,repair in action['repair_rule'].items()):return False
        return True


def terminal_vector(node):
    return np.array([node['terminal'][IDX['failure']],0.,0.])


def stage_vector(action):
    return np.array([0.,action['stage'][IDX['burden']],action['stage'][IDX['expense']]-action['stage'][IDX['output']]])


class ConsequenceGraph:
    def __init__(self,mdp,access=Access()):
        self.mdp=mdp;self.access=access
        self.living=[i for i in mdp.order if 'terminal' not in mdp.nodes[i]]
        self.row={i:r for r,i in enumerate(self.living)}
        self.variables=[];self.by_node={i:[] for i in self.living}
        rr=[];cc=[];vv=[];metrics=[]
        for i in self.living:
            for aidx,action in enumerate(mdp.nodes[i]['actions']):
                if not access.permits(mdp.nodes[i],action,mdp.cfg):continue
                j=len(self.variables);self.variables.append((i,aidx));self.by_node[i].append(j)
                rr.append(self.row[i]);cc.append(j);vv.append(1.)
                metric=stage_vector(action)
                for br in action['branches']:
                    child=br['next'];prob=br['probability']
                    if child in self.row:
                        rr.append(self.row[child]);cc.append(j);vv.append(-prob)
                    else:metric+=prob*terminal_vector(mdp.nodes[child])
                metrics.append(metric)
            assert self.by_node[i], 'At least one permitted action required'
        self.flow=coo_matrix((vv,(rr,cc)),shape=(len(self.living),len(self.variables))).tocsr()
        self.rhs=np.zeros(len(self.living))
        self.terminal_only=mdp.root not in self.row
        if not self.terminal_only:self.rhs[self.row[mdp.root]]=1.
        self.metrics=np.array(metrics).reshape((-1,3)).T
        self.options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9}

    def support(self,weights):
        """Independent backward recursion: min expected weighted consequence."""
        mdp=self.mdp;value=np.zeros(len(mdp.nodes));policy={}
        for i in mdp.order:
            node=mdp.nodes[i]
            if 'terminal' in node:value[i]=weights@terminal_vector(node);continue
            candidates=[]
            for j in self.by_node[i]:
                _,aidx=self.variables[j];a=node['actions'][aidx]
                v=weights@stage_vector(a)+sum(br['probability']*value[br['next']] for br in a['branches'])
                candidates.append((v,aidx))
            value[i],policy[i]=min(candidates)
        return float(value[mdp.root]),policy

    def linear_minimum(self,weights):
        if self.terminal_only:
            return OptimizeResult(success=True,status=0,fun=float(np.asarray(weights)@terminal_vector(self.mdp.nodes[self.mdp.root])),x=np.zeros(0))
        fit=linprog(np.asarray(weights)@self.metrics,A_eq=self.flow,b_eq=self.rhs,bounds=(0,None),method='highs',options=self.options)
        if not fit.success:raise RuntimeError(fit.message)
        return fit

    def feasibility(self,bounds,scales=(1.,1.,10.),details=False):
        bounds=np.asarray(bounds,float);scales=np.asarray(scales,float)
        if np.any(scales<=0):raise ValueError('Positive diagnostic scales required')
        if self.terminal_only:
            actual=terminal_vector(self.mdp.nodes[self.mdp.root]);violations=(actual-bounds)/scales
            k=int(np.argmax(violations));lambdas=np.eye(3)[k];weights=lambdas/scales
            value=float(violations[k])
            result={'status':'feasible' if value<=1e-8 else 'infeasible',
                'bounds':dict(zip(NAMES,map(float,bounds))),'scales':scales.tolist(),
                'consequences':dict(zip(NAMES,map(float,actual))),'phase_one_value':value,
                'maximum_normalized_violation':value,'certificate':{'normalized_weights':lambdas.tolist(),
                'raw_weights':weights.tolist(),'weighted_minimum':float(weights@actual),
                'weighted_bound':float(weights@bounds),'separation_margin':value,'primal_dual_gap':0.},
                'flow_residual':0.,'policy_evaluation_residual':0.,'minimum_occupancy':0.,
                'reachable_nodes':0,'randomized_nodes':0,'authority':self.access.name,'state_count':1,'action_count':0}
            if details:result['policy']=[]
            return result
        n=len(self.variables)
        flow=hstack([self.flow,csr_matrix((len(self.living),1))],format='csr')
        upper=csr_matrix(np.column_stack([self.metrics/scales[:,None],-np.ones(3)]))
        objective=np.zeros(n+1);objective[-1]=1.
        fit=linprog(objective,A_eq=flow,b_eq=self.rhs,A_ub=upper,b_ub=bounds/scales,
                    bounds=[(0,None)]*n+[(None,None)],method='highs',options=self.options)
        if not fit.success:raise RuntimeError(fit.message)
        occupancy=fit.x[:-1];actual=self.metrics@occupancy
        lambdas=np.maximum(0.,-fit.ineqlin.marginals);lambdas/=lambdas.sum()
        weights=lambdas/scales
        supported,_=self.support(weights)
        lower=supported-float(weights@bounds)
        violation=float(np.max((actual-bounds)/scales))
        if violation<=1e-8:status='feasible'
        elif lower>1e-8:status='infeasible'
        else:status='numerically_unresolved'
        evaluation=self.evaluate_occupancy(occupancy,details)
        result={'status':status,'bounds':dict(zip(NAMES,map(float,bounds))),'scales':scales.tolist(),
                'consequences':dict(zip(NAMES,map(float,actual))),
                'phase_one_value':float(fit.fun),'maximum_normalized_violation':violation,
                'certificate':{'normalized_weights':lambdas.tolist(),'raw_weights':weights.tolist(),
                    'weighted_minimum':supported,'weighted_bound':float(weights@bounds),
                    'separation_margin':lower,'primal_dual_gap':float(fit.fun-lower)},
                'flow_residual':float(np.max(np.abs(self.flow@occupancy-self.rhs))),
                'policy_evaluation_residual':float(np.max(np.abs(evaluation['vector']-actual))),
                'minimum_occupancy':float(np.min(occupancy)),
                'reachable_nodes':evaluation['reachable_nodes'],
                'randomized_nodes':evaluation['randomized_nodes'],
                'authority':self.access.name,'state_count':len(self.mdp.nodes),'action_count':n}
        if details:result['policy']=evaluation['policy']
        return result

    def evaluate_occupancy(self,occupancy,details=False):
        """Reconstruct randomized observation-based policy, evaluate independently."""
        mdp=self.mdp;values=np.zeros((len(mdp.nodes),3));records=[];count=randomized=0
        for i in mdp.order:
            node=mdp.nodes[i]
            if 'terminal' in node:values[i]=terminal_vector(node);continue
            indices=self.by_node[i];mass=float(np.sum(occupancy[indices]))
            if mass>0:
                probabilities=occupancy[indices]/mass
                if mass>1e-12:count+=1;randomized+=int(np.sum(probabilities>1e-10)>1)
            else:
                probabilities=np.zeros(len(indices));probabilities[0]=1.
            choices=[]
            for pr,j in zip(probabilities,indices):
                if pr==0:continue
                _,aidx=self.variables[j];action=node['actions'][aidx]
                total=stage_vector(action).copy()
                for br in action['branches']:total+=br['probability']*values[br['next']]
                values[i]+=pr*total
                if details and mass>1e-12:
                    choices.append({'probability':float(pr),'action_index':aidx,
                        **{k:action[k] for k in ('support','test','repair_rule')}})
            if details and mass>1e-12:records.append({'state':mdp.state_description(i),'occupancy':mass,'choices':choices})
        return {'vector':values[mdp.root],'reachable_nodes':count,'randomized_nodes':randomized,'policy':records}

    def least_burden(self,failure_cap):
        if self.terminal_only:
            v=terminal_vector(self.mdp.nodes[self.mdp.root])
            return {'feasible':True,**dict(zip(NAMES,map(float,v)))} if v[0]<=failure_cap else {'feasible':False,'solver_status':2}
        fit=linprog(self.metrics[1],A_eq=self.flow,b_eq=self.rhs,A_ub=self.metrics[[0]],b_ub=[failure_cap],bounds=(0,None),method='highs',options=self.options)
        if not fit.success:return {'feasible':False,'solver_status':fit.status}
        v=self.metrics@fit.x
        return {'feasible':True,**dict(zip(NAMES,map(float,v)))}
