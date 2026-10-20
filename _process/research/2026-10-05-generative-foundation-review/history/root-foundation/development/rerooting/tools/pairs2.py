import json,sys
from collections import defaultdict
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
D={d['name']:d for d in meta['decls']}
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
LTS={'GenerativeCore','Becoming.Frame'}
memo={}
def isl(n):
    if n in memo: return memo[n]
    stack=[n]; seen={n}; hit=False
    while stack:
        x=stack.pop()
        if x not in D: continue
        if D[x]['module'] in LTS: hit=True; break
        for c in D[x]['type']+D[x]['value']+ctors.get(x,[]):
            if c not in seen: seen.add(c); stack.append(c)
    memo[n]=hit; return hit
def clean(c): return not any(p.startswith(('_','match_','proof_','eq_')) for p in c.split('.')[1:])
for m,n in [('Becoming.Dependence','Becoming.Renewal'),('Becoming.Renewal','RelationalRenewal'),('Becoming.Flow','Becoming.Generation'),('Becoming.Generation','Becoming.Return'),('Becoming.Return','Becoming.Dependence')]:
    users=defaultdict(set)
    for x,d in D.items():
        if d['module']!=m or isl(x): continue
        for c in d['type']+d['value']:
            if c in D and D[c]['module']==n: users[c].add(x)
    print(f'{m} (free part) -> {n}:', sorted(c.replace('Becoming.','') for c in users if clean(c)))
    print('   used by', sorted({u.replace('Becoming.','') for v in users.values() for u in v if clean(u)})[:12])
