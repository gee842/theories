"""Finite candidate discovery with paid records, fresh trials, and separate gates.

Run `--phase development`, freeze inputs, then run `--phase evaluation`.
Learner code sees neutral attributes and delayed observed outcomes, never truth.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import math
import shutil
import time
import numpy as np

HERE = Path(__file__).resolve().parent
BLOCK_SIZE, BLOCKS, DELAY = 128, 64, 2
DISCOVERY_N, PER_ARM, MAX_ATTEMPTS = 512, 128, 4
ACTION_COST, CAPTURE_COST, TEST_COST, FEATURE_COST = .25, .01, .005, .01
ALPHA, DEADLINE, TOTAL_ALLOCATION = .05, 24, 512.

@dataclass(frozen=True)
class Predicate:
    terms: tuple[tuple[int, int], ...]

    def matches(self, x):
        return all(int(x[i]) == value for i, value in self.terms)

    def mask(self, x):
        out = np.ones(len(x), dtype=bool)
        for i, value in self.terms:
            out &= x[:, i] == value
        return out

    def key(self):
        return 'all' if not self.terms else '&'.join(f'x{i}={v}' for i,v in self.terms)

def grammar(full=True):
    predicates = [Predicate(())]
    if full:
        predicates += [Predicate(((i,v),)) for i in range(6) for v in (0,1)]
        predicates += [Predicate(((i,a),(j,b)))
                       for i,j in combinations(range(6),2) for a,b in product((0,1),repeat=2)]
    return predicates

def nominate(records, full=True):
    """Uses only linked discovery records; no environment truth argument."""
    x=np.asarray([row[0] for row in records], dtype=np.int8)
    y=np.asarray([row[1] for row in records], dtype=float)
    ranked=[]
    for predicate in grammar(full):
        mask=predicate.mask(x)
        n1,n0=int(mask.sum()),int((~mask).sum())
        if predicate.terms and min(n1,n0)<64:
            continue
        score=float(y[mask].mean()-y[~mask].mean()) if predicate.terms else 0.
        ranked.append((predicate,score,n1,n0))
    ranked.sort(key=lambda row:(-row[1],row[0].key()))
    return ranked

def confirmation(ys_a, ys_b, alpha=ALPHA/MAX_ATTEMPTS):
    """Fresh fixed-candidate, fixed-size bounded-outcome one-sided test."""
    assert len(ys_a)==len(ys_b)==PER_ARM
    delta=float(np.mean(ys_a)-np.mean(ys_b))
    radius=math.sqrt(.5*(1/len(ys_a)+1/len(ys_b))*math.log(1/alpha))
    lower=delta-radius-ACTION_COST
    return {'delta_hat':delta,'radius':radius,'net_lower_bound':lower,
            'accepted':bool(lower>0),'alpha':alpha}

@dataclass(frozen=True)
class Arm:
    name: str
    funding: str = 'protected'
    retention: int = 8
    full_grammar: bool = True
    standing: bool = True
    authority: bool = True

ARMS = [Arm('protected'),Arm('return_funded',funding='returns'),
        Arm('short_records',retention=1),Arm('frozen_model',full_grammar=False),
        Arm('no_standing',standing=False),Arm('no_authority',authority=False),
        Arm('no_inquiry',funding='none',retention=0),
        Arm('temporary_rescue',funding='rescue')]

class World:
    """Scientist/environment boundary. Truth is used for outcomes and scoring only."""
    def __init__(self,seed,hazard):
        self.seed,self.hazard=seed,hazard
        rng=np.random.default_rng(np.random.SeedSequence([seed,2718]))
        indices=sorted(rng.choice(6,2,replace=False).tolist())
        values=rng.integers(0,2,2).tolist()
        self.truth=Predicate(tuple(zip(indices,values)))
        self.x=rng.integers(0,2,(BLOCKS*BLOCK_SIZE,6),dtype=np.int8)
        self.noise=rng.random(BLOCKS*BLOCK_SIZE)
        self.special=self.truth.mask(self.x)

    def outcome(self,case,action):
        prob=.05 + .75*(self.hazard and self.special[case] and action==0)
        return int(self.noise[case]<prob)

    def policy_gain(self,predicate):
        if predicate is None: return 0.
        contexts=np.array(list(product((0,1),repeat=6)),dtype=np.int8)
        selected=predicate.mask(contexts)
        gain=selected*(.75*self.hazard*self.truth.mask(contexts)-ACTION_COST)
        return float(gain.mean())

def allocation(arm,block):
    if arm.funding=='none': return 0.
    if arm.funding=='protected' or (arm.funding=='rescue' and 12<=block<=27): return 8.
    return max(.125,8.*2.**(-block))

def simulate(world,arm,detail=False):
    cash=allocated=overhead=trial_b_charge=0.
    capture_spend=feature_spend=test_spend=0.
    discovery=[]
    metadata={}
    pending=[[] for _ in range(BLOCKS+DELAY)]
    ranked=None
    generated_log=[]
    tests=[]
    active=None
    tested_index=0
    finished=arm.funding=='none'
    validated=admitted=authorized=enacted=None
    selected=operational=None
    first_candidate=None
    initiated=completed=captures=expired=0
    failures=b_actions=trial_b_actions=0
    record_ids_discovery=set()
    record_ids_confirmation=set()
    trace=[]
    actor_digest=hashlib.sha256()
    digest_at_validation=None
    accepted_report=None
    ordinary_count=ordinary_failures=0

    def start_test(block):
        nonlocal active,tested_index,finished
        if ranked is None or active is not None or finished: return
        if tested_index>=min(MAX_ATTEMPTS,len(ranked)):
            finished=True
            return
        p,score,n1,n0=ranked[tested_index]
        order=np.array([0]*PER_ARM+[1]*PER_ARM,dtype=np.int8)
        rng=np.random.default_rng(np.random.SeedSequence([world.seed,31415,tested_index]))
        rng.shuffle(order)
        active={'predicate':p,'search_score':score,'order':order,'initiated':0,
                'ys':[[],[]],'ids':[],'attempt':tested_index+1,'start_block':block}
        tested_index+=1

    for block in range(BLOCKS+DELAY):
        # Delete linking metadata before reports at this time become visible.
        stale=[case for case,row in metadata.items() if block-row['block']>=arm.retention]
        for case in stale:
            del metadata[case]
            expired+=1
        for case,y in pending[block]:
            ordinary_count+=1
            ordinary_failures+=y
            row=metadata.pop(case,None)
            if row is None: continue
            if row['kind']=='discovery':
                discovery.append((row['x'],y))
                record_ids_discovery.add(case)
            elif active is not None and row['attempt']==active['attempt']:
                active['ys'][row['action']].append(y)
                active['ids'].append(case)
                record_ids_confirmation.add(case)
                completed+=1
                actor_digest.update(f'{case}:{row["action"]}:{y};'.encode())

        if active is not None and all(len(v)==PER_ARM for v in active['ys']):
            test=confirmation(*active['ys'])
            test.update({'attempt':active['attempt'],'predicate':active['predicate'].key(),
                         'terms':active['predicate'].terms,'start_block':active['start_block'],
                         'complete_block':block,'search_score':active['search_score'],
                         'n_a':PER_ARM,'n_b':PER_ARM,
                         'confirmation_id_hash':hashlib.sha256(json.dumps(active['ids']).encode()).hexdigest()})
            tests.append(test)
            if test['accepted']:
                validated=block
                selected=active['predicate']
                accepted_report=dict(test)
                digest_at_validation=actor_digest.hexdigest()
                if arm.standing:
                    admitted=block
                    if arm.authority:
                        authorized=block
                        operational=selected
                finished=True
            active=None

        if block>=BLOCKS: continue
        if not finished:
            credit=min(allocation(arm,block),TOTAL_ALLOCATION-allocated)
            cash+=credit
            allocated+=credit
        if not finished and ranked is None and len(discovery)>=DISCOVERY_N:
            fee=FEATURE_COST*len(grammar(arm.full_grammar))
            if cash+1e-12>=fee:
                cash-=fee;overhead+=fee;feature_spend+=fee
                ranked=nominate(discovery,arm.full_grammar)
                first_candidate=block
                generated_log=[{'predicate':p.key(),'terms':p.terms,'score':score,
                                'n_inside':n1,'n_outside':n0} for p,score,n1,n0 in ranked]
                actor_digest.update(json.dumps(generated_log,sort_keys=True).encode())
        start_test(block)

        for case in range(block*BLOCK_SIZE,(block+1)*BLOCK_SIZE):
            x=world.x[case]
            action=int(operational is not None and operational.matches(x))
            kind=None
            trial=False
            attempt=None
            if active is not None and active['initiated']<2*PER_ARM and active['predicate'].matches(x):
                proposed_action=int(active['order'][active['initiated']])
                fee=CAPTURE_COST+TEST_COST+ACTION_COST*proposed_action
                if cash+1e-12>=fee:
                    cash-=fee
                    overhead+=CAPTURE_COST+TEST_COST
                    capture_spend+=CAPTURE_COST;test_spend+=TEST_COST
                    trial_b_charge+=ACTION_COST*proposed_action
                    action=proposed_action
                    trial=True
                    kind='confirmation'
                    attempt=active['attempt']
                    active['initiated']+=1
                    initiated+=1
            elif not finished and ranked is None and cash+1e-12>=CAPTURE_COST:
                cash-=CAPTURE_COST
                overhead+=CAPTURE_COST
                capture_spend+=CAPTURE_COST
                kind='discovery'
            if kind is not None:
                metadata[case]={'block':block,'x':x.copy(),'action':action,
                                'kind':kind,'attempt':attempt}
                captures+=1
            if action and not trial and operational is not None and enacted is None:
                enacted=block
            y=world.outcome(case,action)
            failures+=y
            b_actions+=action
            trial_b_actions+=int(trial and action)
            pending[block+DELAY].append((case,y))
        trace.append({'block':block,'allocation':0. if finished else allocation(arm,block),
                      'cash':cash,'cumulative_allocated':allocated,'overhead':overhead,
                      'trial_b_charge':trial_b_charge,'discovery_records':len(discovery),
                      'initiated_trials':initiated,'completed_trials':completed,
                      'active_attempt':None if active is None else active['attempt'],
                      'active_initiated':0 if active is None else active['initiated']})

    assert not (record_ids_discovery & record_ids_confirmation)
    assert abs(allocated-cash-overhead-trial_b_charge)<1e-7
    assert abs(trial_b_charge-ACTION_COST*trial_b_actions)<1e-7
    assert abs(overhead-capture_spend-feature_spend-test_spend)<1e-7
    assert cash>=-1e-8
    assert ordinary_count==BLOCKS*BLOCK_SIZE
    gain=world.policy_gain(selected)
    result={'seed':world.seed,'hazard':world.hazard,'arm':arm.name,
            'first_candidate_block':first_candidate,'validated_block':validated,
            'admitted_block':admitted,'authorized_block':authorized,'enacted_block':enacted,
            'timely_validation':validated is not None and validated<=DEADLINE,
            'timely_enactment':enacted is not None and enacted<=DEADLINE,
            'selected_predicate':None if selected is None else selected.key(),
            'true_predicate_for_scientist':world.truth.key(),
            'true_selected_policy_gain':gain,
            'false_acceptance':validated is not None and gain<=0.,
            'exact_predicate_recovered':selected==world.truth if selected is not None else False,
            'failures':failures,'b_actions':b_actions,'trial_b_actions':trial_b_actions,
            'action_cost':ACTION_COST*b_actions,'inquiry_overhead':overhead,
            'capture_cost':capture_spend,'generation_cost':feature_spend,'measurement_cost':test_spend,
            'total_realized_loss':failures+ACTION_COST*b_actions+overhead,
            'allocated':allocated,'cash_remaining':cash,
            'unallocated_potential_budget':TOTAL_ALLOCATION-allocated,
            'captures':captures,'expired_unlinked':expired,'mature_discovery_records':len(discovery),
            'initiated_trials':initiated,'completed_trials':completed,
            'completed_attempts':len(tests),
            'pending_test':None if active is None else {'attempt':active['attempt'],
                'initiated':active['initiated'],'n_a':len(active['ys'][0]),'n_b':len(active['ys'][1])},
            'first_validation_evidence_hash':digest_at_validation,
            'accepted_report':accepted_report,'generated_candidates':generated_log,'tests':tests,
            'discovery_confirmation_overlap':False}
    if detail: result['trace']=trace
    return result

def wilson(success,total,z=1.959963984540054):
    p=success/total
    den=1+z*z/total
    mid=(p+z*z/(2*total))/den
    spread=z*math.sqrt(p*(1-p)/total+z*z/(4*total*total))/den
    return [mid-spread,mid+spread]

def summarize(records):
    summary=[]
    for hazard in [True,False]:
        baseline={r['seed']:r for r in records if r['hazard']==hazard and r['arm']=='no_inquiry'}
        protected={r['seed']:r for r in records if r['hazard']==hazard and r['arm']=='protected'}
        for arm in ARMS:
            rows=[r for r in records if r['hazard']==hazard and r['arm']==arm.name]
            item={'hazard':hazard,'arm':arm.name,'n':len(rows)}
            for field in ['timely_validation','timely_enactment','false_acceptance','exact_predicate_recovered']:
                count=sum(bool(r[field]) for r in rows)
                item[field]={'count':count,'rate':count/len(rows),'wilson95':wilson(count,len(rows))}
            for field in ['failures','action_cost','inquiry_overhead','total_realized_loss',
                          'true_selected_policy_gain','initiated_trials','completed_trials',
                          'completed_attempts','mature_discovery_records']:
                arr=np.array([r[field] for r in rows],dtype=float)
                item[field]={'mean':float(arr.mean()),'se':float(arr.std(ddof=1)/np.sqrt(len(rows)))}
            times=[r['validated_block'] for r in rows if r['validated_block'] is not None]
            item['ever_validated']=len(times)
            item['validation_block_mean_if_any']=None if not times else float(np.mean(times))
            diff=np.array([baseline[r['seed']]['total_realized_loss']-r['total_realized_loss'] for r in rows])
            item['loss_reduction_vs_no_inquiry']={'mean':float(diff.mean()),'se':float(diff.std(ddof=1)/np.sqrt(len(rows)))}
            paired=np.array([int(protected[r['seed']]['timely_validation'])-int(r['timely_validation']) for r in rows])
            item['protected_minus_arm_timely_validation']={'mean':float(paired.mean()),'se':float(paired.std(ddof=1)/np.sqrt(len(rows)))}
            summary.append(item)
    return summary

def check_gate_pairing(rows):
    for hazard in [True,False]:
        arms={r['arm']:r for r in rows if r['hazard']==hazard}
        a=arms['protected']
        for name in ['no_standing','no_authority']:
            b=arms[name]
            for key in ['validated_block','first_validation_evidence_hash','selected_predicate',
                        'generated_candidates','tests','initiated_trials','completed_trials','inquiry_overhead']:
                assert a[key]==b[key],(name,key)
        assert arms['no_standing']['admitted_block'] is None
        assert arms['no_standing']['enacted_block'] is None
        assert arms['no_authority']['admitted_block']==a['admitted_block']
        assert arms['no_authority']['enacted_block'] is None
        assert arms['short_records']['mature_discovery_records']==0
        assert arms['no_inquiry']['inquiry_overhead']==0

def freeze():
    dest=HERE/'evaluation-inputs'
    if dest.exists(): raise RuntimeError('Evaluation inputs already frozen; do not overwrite.')
    dest.mkdir()
    manifest={}
    for name in ['experiment.py','PROTOCOL.md']:
        data=(HERE/name).read_bytes()
        (dest/name).write_bytes(data)
        manifest[name]=hashlib.sha256(data).hexdigest()
    (dest/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(manifest,indent=2))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--phase',choices=['development','evaluation','freeze'],required=True)
    args=parser.parse_args()
    if args.phase=='freeze':
        freeze();return
    if args.phase=='evaluation':
        manifest=json.loads((HERE/'evaluation-inputs/manifest.json').read_text())
        for name,digest in manifest.items():
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest, 'Inputs changed after freeze'
    seeds=range(16) if args.phase=='development' else range(10000,10256)
    out=HERE/f'results-{args.phase}'
    out.mkdir(exist_ok=True)
    if (out/'runs.jsonl').exists(): raise RuntimeError('Run output already exists; preserve previous runs.')
    results=[]
    started=time.monotonic()
    with (out/'runs.jsonl').open('w') as file:
        for index,seed in enumerate(seeds):
            paired=[]
            for hazard in [True,False]:
                world=World(seed,hazard)
                for arm in ARMS:
                    result=simulate(world,arm,detail=index==0)
                    paired.append(result)
                    results.append(result)
                    file.write(json.dumps(result,separators=(',',':'))+'\n')
            check_gate_pairing(paired)
            if (index+1)%16==0:
                print(f'{args.phase}: {index+1}/{len(seeds)} paired seeds; {time.monotonic()-started:.1f}s',flush=True)
    report={'phase':args.phase,'n_seeds':len(seeds),'rows':len(results),
            'inputs_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in ['experiment.py','PROTOCOL.md']},
            'checks':'cash balance, no confirmation reuse, no truth in nomination, paired pre-gate evidence, stage gates, retention',
            'summary':summarize(results)}
    (out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps([{'hazard':r['hazard'],'arm':r['arm'],
                     'timely_validated':r['timely_validation']['count'],
                     'ever_validated':r['ever_validated'],
                     'timely_enacted':r['timely_enactment']['count'],
                     'false_accepts':r['false_acceptance']['count'],
                     'loss_reduction':r['loss_reduction_vs_no_inquiry']}
                    for r in report['summary']],indent=2))

if __name__=='__main__': main()
