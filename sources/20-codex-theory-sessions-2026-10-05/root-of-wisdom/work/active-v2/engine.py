"""Exact public-belief oracle and mechanical private-world reply service.

The oracle never uses selected_world. Only query and terminal realization do.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json

ROOT = Path(__file__).resolve().parent

def encode(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'))

class Oracle:
    def __init__(self, case):
        self.c = case
        self.queries = {q['id']:q for q in case['queries']}
        self.actions = {a['id']:a for a in case['actions']}
        self.priors = {w['id']:F(w['prior']) for w in case['worlds']}
        assert sum(self.priors.values()) == 1
        assert all(p>0 for p in self.priors.values())
        self.budget=F(case['constraints']['cash_budget'])
        self.deadline=case['constraints']['deadline']
        self.max_queries=case['constraints']['max_queries']

    def posterior(self,h):
        remaining={w:p for w,p in self.priors.items() if all(
            encode(self.queries[q]['response_by_world'][w])==r for q,r in h)}
        total=sum(remaining.values())
        assert total>0, ('impossible public transcript',h)
        return {w:p/total for w,p in remaining.items()}

    def consumed(self,h):
        return (sum((F(self.queries[q]['fee']) for q,r in h),F(0)),
                sum(self.queries[q]['duration'] for q,r in h))

    def feasible(self,h,kind,target):
        items=self.queries if kind=='query' else self.actions if kind=='act' else {}
        if target not in items: return False
        obj=items[target];cash,time=self.consumed(h)
        if cash+F(obj['fee'])>self.budget or time+obj['duration']>self.deadline:
            return False
        if kind=='query':
            used={q for q,r in h}
            if len(h)>=self.max_queries or target in used: return False
            if not set(obj.get('prerequisites',[])).issubset(used): return False
        return True

    @lru_cache(None)
    def qvalues(self,h):
        belief=self.posterior(h);values={}
        for a,obj in self.actions.items():
            if self.feasible(h,'act',a):
                values[('act',a)]=F(obj['fee'])+sum(
                    p*F(obj['residual_loss_by_world'][w]) for w,p in belief.items())
        for q,obj in self.queries.items():
            if not self.feasible(h,'query',q): continue
            groups={}
            for w,p in belief.items():
                response=encode(obj['response_by_world'][w])
                groups[response]=groups.get(response,F(0))+p
            values[('query',q)]=F(obj['fee'])+sum(
                p*self.value(h+((q,r),)) for r,p in groups.items())
        assert ('act','fallback') in values
        return values

    def value(self,h): return min(self.qvalues(h).values())

    def optimal(self,h):
        values=self.qvalues(h);v=min(values.values())
        return {command for command,value in values.items() if value==v}

    def best_terminal(self,h):
        return min(v for (k,t),v in self.qvalues(h).items() if k=='act')

def load_cases():
    env=json.loads((ROOT/'environment.json').read_text())
    return {c['case_id']:c for c in env['cases']}

def initialize(batch,condition,replicate,order):
    return {'batch':batch,'condition':condition,'replicate':replicate,'round':0,
            'order':order,'episodes':{i:{'history':[],'events':[],'closed':False} for i in order}}

def step(state,response,cases):
    """Apply a round unchanged; invalid commands force the public fallback."""
    commands=response.get('decisions',[]) if isinstance(response,dict) else []
    if not isinstance(commands,list): commands=[]
    valid_dicts=[c for c in commands if isinstance(c,dict)]
    counts=Counter(encode(c.get('id')) for c in valid_dicts)
    mapping={c.get('id'):c for c in valid_dicts if isinstance(c.get('id'),str) and counts[encode(c.get('id'))]==1}
    open_ids=[i for i in state['order'] if not state['episodes'][i]['closed']]
    state.setdefault('format_events',[]).append({'round':state['round'],
        'extra_ids':[c.get('id') for c in valid_dicts if c.get('id') not in open_ids],
        'duplicate_ids':[json.loads(i) for i,n in counts.items() if n>1]})
    replies=[]
    for identifier in open_ids:
        case=cases[identifier];oracle=Oracle(case);ep=state['episodes'][identifier]
        h=tuple(tuple(x) for x in ep['history'])
        c=mapping.get(identifier,{})
        kind=c.get('kind');target=c.get('target');reason=c.get('reason')
        format_ok=(kind in ('query','act') and isinstance(target,str) and isinstance(reason,str) and bool(reason.strip()))
        word_count=len(reason.split()) if isinstance(reason,str) else None
        feasible=format_ok and oracle.feasible(h,kind,target)
        command=(kind,target) if feasible else ('act','fallback')
        q=oracle.qvalues(h)[command];v=oracle.value(h);terminal=oracle.best_terminal(h)
        event={'round':state['round'],'submitted':c,'invalid':not feasible,
               'effective_kind':command[0],'effective_target':command[1],
               'public_posterior':{w:str(p) for w,p in oracle.posterior(h).items()},
               'remaining_optimum':str(v),'chosen_Q':str(q),'bellman_gap':str(q-v),
               'optimal_command':feasible and command in oracle.optimal(h),
               'best_immediate_terminal_loss':str(terminal),
               'strict_unnecessary_continuation':feasible and kind=='query' and q>terminal,
               'reason_words':word_count,'word_cap_compliant':word_count is not None and word_count<=35}
        private_world=case['private']['selected_world']
        if command[0]=='query':
            query=oracle.queries[target]
            result=query['response_by_world'][private_world]
            ep['history'].append([target,encode(result)])
            cash,time=oracle.consumed(tuple(tuple(x) for x in ep['history']))
            event['query_result']=result
            replies.append({'id':identifier,'query':target,'result':result,
                            'fee_charged':query['fee'],'cash_remaining':str(oracle.budget-cash),
                            'elapsed_time':time,'deadline':oracle.deadline,
                            'queries_remaining':oracle.max_queries-len(ep['history'])})
        else:
            action=oracle.actions[command[1]]
            query_spending,elapsed=oracle.consumed(h)
            event['terminal_conditional_excess']=str(q-terminal)
            event['terminal_expected_remaining_loss']=str(q)
            event['realized_residual_loss']=action['residual_loss_by_world'][private_world]
            ep['closed']=True
            ep['terminal_action']=command[1]
            ep['query_spending']=str(query_spending)
            ep['action_fee']=action['fee']
            ep['realized_total_loss']=str(query_spending+F(action['fee'])+F(action['residual_loss_by_world'][private_world]))
            ep['final_elapsed']=elapsed+action['duration']
        ep['events'].append(event)
    state['round']+=1
    remaining=[i for i in state['order'] if not state['episodes'][i]['closed']]
    assert state['round']<=3
    if state['round']==3: assert not remaining
    feedback={'query_results':replies,'open_episode_ids':remaining,
              'instruction':'Choose one next command for each open episode in the listed order. Use only the original public model and returned evidence. Return the same JSON format; no tools.'}
    return state,feedback

def apply_saved_round(batch,round_number):
    state_path=ROOT/'runs'/batch/'state.json'
    state=json.loads(state_path.read_text())
    assert state['round']==round_number
    raw=(state_path.parent/f'response-{round_number}.txt').read_text()
    try:
        response=json.loads(raw)
    except json.JSONDecodeError as error:
        response={}
        state.setdefault('parse_failures',[]).append({'round':round_number,'error':str(error)})
    state,feedback=step(state,response,load_cases())
    state_path.write_text(json.dumps(state,indent=2)+'\n')
    (state_path.parent/f'feedback-{round_number}.json').write_text(json.dumps(feedback,indent=2)+'\n')
    return feedback

if __name__=='__main__':
    import sys
    print(json.dumps(apply_saved_round(sys.argv[1],int(sys.argv[2])),indent=2))
