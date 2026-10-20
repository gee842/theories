import json,sys
from collections import defaultdict,Counter
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
rows=json.load(open(S+'/reach-rows.json'))
g=json.load(open(S+'/graph.json')); L=g['layers']; imp={k:[i for i in v] for k,v in g['imports'].items()}
D={d['name']:d for d in meta['decls']}
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
def deps(n): return [c for c in D[n]['type']+D[n]['value']+ctors.get(n,[]) if c in D]
def owned(prefixes, mod):
    # constants of module mod named exactly prefix or prefix.<auto> (structure projections, ctors, recursors, eq lemmas)
    out=set()
    for n,d in D.items():
        if d['module']!=mod: continue
        for p in prefixes:
            if n==p or (n.startswith(p+'.') and n[len(p)+1:] in ('mk','rec','casesOn','recOn','noConfusion','noConfusionType','mk.injEq','mk.inj','mk.sizeOf_spec','sizeOf_spec','ctorIdx','mk.noConfusion') ) or (n.startswith(p+'.') and any(n==p+'.'+f for f in FIELDS.get(p,[]))) or n.startswith(p+'._') or n.startswith(p+'.mk.') :
                out.add(n)
    return out
FIELDS={'Becoming.Web':['level','active','requires','need','draws'],'Becoming.Flow':['present','take','give'],
        'Becoming.World':['Relatum','flow','web'],'Becoming.Exchange':['present','take','give']}
B=set()
B|=owned(['Becoming.Web'],'Becoming.Dependence')
B|=owned(['Becoming.Flow'],'Becoming.Flow')
B|=owned(['Becoming.World'],'Becoming.Space')
B|=owned(['Becoming.Exchange'],'Becoming.Unfolding')
for extra in ['Becoming.Exchange.taken','Becoming.Exchange.given','Becoming.World.move']: B.add(extra)
# close B under dependencies (pulling in what it needs: e.g. total)
st=list(B)
while st:
    x=st.pop()
    for c in deps(x):
        if D[c]['module'].startswith('Becoming.') or D[c]['module'] in ('GenerativeCore','RelationalRenewal','InquirySufficiency'):
            if c not in B: B.add(c); st.append(c)
print('base closure:',len(B),'constants; modules:',Counter(D[x]['module'] for x in B))
print(' non-auto:',sorted(x.replace('Becoming.','') for x in B if not any(p.startswith('_') or p in('rec','casesOn','recOn','noConfusion','noConfusionType','ctorIdx') or p.startswith(('match_','proof_','eq_')) for p in x.split('.')[1:])))
# early Unfolding: needs only B, GenerativeCore, Frame, prelude, and other early Unfolding constants
U=[n for n,d in D.items() if d['module']=='Becoming.Unfolding']
allowed=set(B)|{n for n,d in D.items() if d['module'] in ('GenerativeCore','Becoming.Frame')}
early=set()
changed=True
while changed:
    changed=False
    for n in U:
        if n in early: continue
        if all((c in allowed) or (c in early) or (c==n) for c in deps(n)):
            early.add(n); changed=True
reg={r['name'] for r in rows if r['module']=='Becoming.Unfolding'}
regth={r['name'] for r in rows if r['module']=='Becoming.Unfolding' and r['kind']=='theorem'}
print('Unfolding registry decls',len(reg),'theorems',len(regth),'; early decls',len(reg&early),'early theorems',len(regth&early))
print(' early:',sorted(x.replace('Becoming.','') for x in reg&early))
print(' late:',sorted(x.replace('Becoming.','') for x in reg-early))
# what blocks the late ones (first-level modules)
blk=Counter()
for n in reg-early:
    for c in deps(n):
        if c not in allowed and c not in early and D[c]['module']!='Becoming.Unfolding': blk[D[c]['module']]+=1
print(' late Unfolding decls use constants of:',blk.most_common())
json.dump({'early_all':sorted(early),'base':sorted(B),'early':sorted(reg&early),'late':sorted(reg-early)},open(S+'/sim.json','w'),indent=0)
blkc=defaultdict(set)
for n in reg-early:
    for c in deps(n):
        if c not in allowed and c not in early and D[c]['module']!='Becoming.Unfolding': blkc[c].add(n.replace('Becoming.',''))
for c,v in sorted(blkc.items(), key=lambda kv:D[kv[0]]['module']):
    print('  ',D[c]['module'].replace('Becoming.',''),c.replace('Becoming.',''),'<-',sorted(v)[:4])
