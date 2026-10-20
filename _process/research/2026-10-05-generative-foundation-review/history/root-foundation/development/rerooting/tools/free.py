import json,sys
from collections import defaultdict,Counter
from functools import lru_cache
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
rows=json.load(open(S+'/reach-rows.json'))
g=json.load(open(S+'/graph.json')); L=g['layers']; imp=g['imports']
D={d['name']:d for d in meta['decls']}
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
CORESET=set(L['FOUNDATION']+L['CORE'])
LTS={'GenerativeCore','Becoming.Frame'}
# classify every Lean constant (incl. internal) as free or lts by full reach
memo={}
def isl(n):
    # iterative full reach to LTS
    if n in memo: return memo[n]
    stack=[n]; seen={n}; hit=False
    while stack:
        x=stack.pop()
        if x not in D: continue
        if D[x]['module'] in LTS: hit=True; break
        for c in D[x]['type']+D[x]['value']+ctors.get(x,[]):
            if c not in seen: seen.add(c); stack.append(c)
    memo[n]=hit; return hit
# module-level edges of the free part: free constants of M using constants of N
fe=defaultdict(set); le=defaultdict(set)
freecount=Counter(); ltscount=Counter()
for n,d in D.items():
    m=d['module']
    f=not isl(n)
    for c in d['type']+d['value']+ctors.get(n,[]):
        if c in D and D[c]['module']!=m:
            (fe if f else le)[m].add(D[c]['module'])
json.dump({k:sorted(v) for k,v in fe.items()},open(S+'/free-edges.json','w'),indent=0)
json.dump({k:sorted(v) for k,v in le.items()},open(S+'/lts-edges.json','w'),indent=0)
@lru_cache(None)
def fdepth(m):
    ps=fe.get(m,())
    return 0 if not ps else 1+max(fdepth(p) for p in ps)
@lru_cache(None)
def idepth(m):
    ps=[p for p in imp.get(m,[]) if p in CORESET]
    return 0 if not ps else 1+max(idepth(p) for p in ps)
def fchain(m):
    out=[m]
    while fe.get(m):
        m=max(fe[m],key=fdepth); out.append(m)
    return out
for m in ['Becoming.Web','Becoming.Dependence','Becoming.Flow','Becoming.Space','Becoming.Change','Becoming.Unfolding','Becoming.CouplingTraces','Becoming.SelectionPool','Becoming.Loops']:
    if m in D or m in imp:
        print(m,'import depth',idepth(m),'free-part depth',fdepth(m),' chain:',' <- '.join(x.replace('Becoming.','') for x in reversed(fchain(m))))
print('max import depth core', max(idepth(m) for m in L['CORE']), 'max free depth', max(fdepth(m) for m in L['CORE']))
# Which modules do free decls of the Space chain need
anc=set(); st=['Becoming.Space']
while st:
    x=st.pop()
    for y in fe.get(x,()):
        if y not in anc: anc.add(y); st.append(y)
print('free-part ancestors of Space:',sorted(anc))
# what free decls of Dependence reach from Renewal?
