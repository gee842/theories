import json,sys
from collections import defaultdict,Counter
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
rows=json.load(open(S+'/reach-rows.json'))
D={d['name']:d for d in meta['decls']}
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
TARGETS={'Becoming.Web':'web','Becoming.Flow':'flow','Becoming.World':'world','Becoming.Exchange':'exchange',
 'Becoming.Dependence':'state-observables','Becoming.Conditions':'state-observables','RelationalRenewal.Unfolding':'relational-renewal'}
def stmt_hits(n):
    stack=list(D[n]['type'])+ctors.get(n,[]); seen=set(stack); hits=set()
    while stack:
        x=stack.pop()
        if x in TARGETS: hits.add(TARGETS[x])
        if x not in D: continue
        nxt=D[x]['type']+ctors.get(x,[])
        if D[x]['kind']!='theorem': nxt=nxt+D[x]['value']
        for c in nxt:
            if c not in seen: seen.add(c); stack.append(c)
    return hits
c=Counter(); ex=defaultdict(list)
for r in rows:
    if r['kind']!='theorem' or r['full_lts']: continue
    h=stmt_hits(r['name'])
    if h & {'web','flow','world','exchange','relational-renewal'}: k='about Web/Flow/World'
    elif 'state-observables' in h: k='state-indexed observables, no process'
    else: k='other'
    c[k]+=1; ex[k].append(r['module'])
print(c)
print('other by module:',Counter(ex['other']).most_common(25))
