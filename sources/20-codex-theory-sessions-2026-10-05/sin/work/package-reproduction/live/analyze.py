from pathlib import Path
from collections import Counter
import itertools,json,sys,statistics,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
from run import ROOT,read,save,answers,truth

def count_correct(r,rows,t): return sum(a==truth(x,t) for a,x in zip(answers(r,len(rows)),rows))
def perm_a(vals,blocks,assignment):
    observed=sum((1 if assignment[i] else -1)*vals[i] for b in blocks for i in b)
    distribution=Counter({0:1})
    for b in blocks:
        total=sum(vals[i] for i in b)
        increments=Counter(2*sum(vals[b[j]] for j in chosen)-total for chosen in itertools.combinations(range(4),2))
        nxt=Counter()
        for x,n in distribution.items():
            for y,m in increments.items(): nxt[x+y]+=n*m
        distribution=nxt
    total=sum(distribution.values()); tail=sum(n for x,n in distribution.items() if abs(x)>=abs(observed))
    return {'numerator':observed,'p_two_sided':tail/total,'tail_count':tail,'permutations':total}
def perm_b(vals):
    obs=sum(vals); dist=Counter({0:1})
    for v in vals:
        nxt=Counter()
        for x,n in dist.items(): nxt[x+v]+=n; nxt[x-v]+=n
        dist=nxt
    total=sum(dist.values()); tail=sum(n for x,n in dist.items() if abs(x)>=abs(obs))
    return {'numerator':obs,'p_two_sided':tail/total,'tail_count':tail,'permutations':total}
def main():
    assignment=read(ROOT/'assignments.json'); blocks=read(ROOT/'assignment-blocks.json'); bmap={(x['id'],x['replica']):x['B'] for x in read(ROOT/'successor-assignments.json')}
    rows=[]
    for p in sorted((ROOT/'lineages').glob('*/private.json')):
        d=read(p); folder=p.parent; lid=d['id']; m=read(folder/'maintenance-response.json')
        packet=m.get('packet',''); slot=m.get('maintenance_slots'); valid=slot==1 and isinstance(packet,str) and 0<len(packet.split())<=120
        scores={}
        for replica in ('r0','r1'):
            scores[bmap[lid,replica]]=count_correct(read(folder/(replica+'-response.json')),d['test'],d['truth'])
        service_n=3 if slot==1 else 4
        service=count_correct(m,d['service'][:service_n],d['truth'])
        rows.append({'id':lid,'stratum':d['stratum'],'A':assignment[lid],'baseline_correct':count_correct(read(folder/'baseline-response.json'),d['baseline'],d['truth']),'M':int(valid),'slot_declared':slot,'packet_words':len(packet.split()) if isinstance(packet,str) else 0,'service_attempts':service_n,'service_correct':service,'Y0_count':scores[0],'Y1_count':scores[1],'gain_count':scores[1]-scores[0],'reason':m.get('reason','')})
    c=[r for r in rows if r['stratum']=='challenge']; cb=blocks[:6]
    pm=perm_a({r['id']:r['M'] for r in c},cb,assignment)
    pi=perm_a({r['id']:r['gain_count'] for r in c},cb,assignment)
    pb=perm_b([r['gain_count'] for r in c if r['A']==1])
    pm['effect']=pm['numerator']/12; pi['effect']=pi['numerator']/(12*16); pb['effect']=pb['numerator']/(12*16)
    alpha=.05/3
    for x in (pm,pi,pb): x['passes']=x['effect']>0 and x['p_two_sided']<alpha
    summary=[]
    for stratum in ('challenge','adequate'):
        for a in (0,1):
            group=[r for r in rows if r['stratum']==stratum and r['A']==a]
            summary.append({'stratum':stratum,'A':a,'n':len(group),'maintenance_rate':statistics.mean(r['M'] for r in group),'baseline_accuracy':statistics.mean(r['baseline_correct']/8 for r in group),'service_correct_mean':statistics.mean(r['service_correct'] for r in group),'service_attempts_mean':statistics.mean(r['service_attempts'] for r in group),'Y0':statistics.mean(r['Y0_count']/16 for r in group),'Y1':statistics.mean(r['Y1_count']/16 for r in group),'paired_access_gain':statistics.mean(r['gain_count']/16 for r in group),'team0_mean':statistics.mean(r['service_correct']+r['Y0_count'] for r in group),'team1_mean':statistics.mean(r['service_correct']+r['Y1_count'] for r in group)})
    hypotheses=[None]+[(p,q,u,v) for p,q in itertools.combinations(range(1,5),2) for u,v in itertools.product((0,1),repeat=2)]
    classical=[]
    for p in sorted((ROOT/'lineages').glob('*/private.json')):
        d=read(p); consistent=[h for h in hypotheses if all(truth(x,h)==truth(x,d['truth']) for x in d['baseline'])]
        assert len(consistent)==1
        classical.append({'id':d['id'],'report_learner_correct':sum(truth(x,consistent[0])==truth(x,d['truth']) for x in d['test']),'legacy_correct':sum(x[0]==truth(x,d['truth']) for x in d['test'])})
    result={'n_lineages':32,'n_successor_contexts':64,'alpha_per_primary_test':alpha,'primary':{'feedback_to_maintenance':pm,'access_after_feedback':pb,'factorial_interaction':pi},'all_three_pass':all(x['passes'] for x in (pm,pb,pi)),'arm_summary':summary,'lineages':rows,'classical_comparator':classical,'inference_scope':'Blocked finite-task randomization tests; model-family generalization and human inference are unsupported.'}
    save(ROOT/'results.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('lineages','classical_comparator')},indent=2))
if __name__=='__main__': main()
