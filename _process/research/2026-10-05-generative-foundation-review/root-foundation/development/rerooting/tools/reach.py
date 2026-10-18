import json,sys,re
from collections import Counter,defaultdict
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
reg=json.load(open(S+'/registry.json'))
g=json.load(open(S+'/graph.json'))
D={d['name']:d for d in meta['decls']}
MOD=meta['modules']
for n,d in D.items(): MOD[n]=d['module']
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
LTSMODS={'GenerativeCore','Becoming.Frame'}
sys.setrecursionlimit(100000)
# full reach: set of modules (core/foundation) reached through type+value
memo_full={}
def full(n):
    # returns frozenset of core/foundation modules reached transitively (iterative)
    if n in memo_full: return memo_full[n]
    stack=[n]; seen={n}; mods=set()
    while stack:
        x=stack.pop()
        if x not in D: continue
        mods.add(D[x]['module'])
        for c in D[x]['type']+D[x]['value']+ctors.get(x,[]):
            if c not in seen: seen.add(c); stack.append(c)
    memo_full[n]=mods; return mods
def stmt(n):
    # statement reach: type of n; through defs/structures follow type+value+ctors; through theorems only type
    stack=list(D[n]['type'])+ctors.get(n,[]); seen=set(stack); mods=set()
    while stack:
        x=stack.pop()
        if x not in D: continue
        mods.add(D[x]['module'])
        nxt=D[x]['type']+ctors.get(x,[])
        if D[x]['kind']!='theorem': nxt=nxt+D[x]['value']
        for c in nxt:
            if c not in seen: seen.add(c); stack.append(c)
    return mods
def direct_type_mods(n):
    return {MOD.get(c,'?') for c in D[n]['type']}
# map registry names to Lean names
def lean_name(mod,name):
    if name in D: return name
    # private
    cands=[k for k in D if k.endswith('.'+name.split('.')[-1]) and D[k]['module']==mod and name.split('.',1)[-1] in k]
    return cands[0] if cands else None
rows=[]; missing=0
for mod,items in reg.items():
    for it in items:
        ln=lean_name(mod,it['name'])
        if ln is None: missing+=1; continue
        f=full(ln); s=stmt(ln)
        rows.append(dict(module=mod,name=it['name'],kind=it['kind'],
            full_lts=bool(f&LTSMODS), full_gc='GenerativeCore' in f, stmt_lts=bool(s&LTSMODS),
            stmt_gc='GenerativeCore' in s, full_mods=sorted(f), stmt_mods=sorted(s)))
print('missing',missing,'rows',len(rows))
json.dump(rows,open(S+'/reach-rows.json','w'))
