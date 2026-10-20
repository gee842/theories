"""Simulate the re-rooting batches on Lean's constant graph.
usage: sim3.py SCRATCH  (reads rr/.build/reroot-meta.json, reach-rows.json, graph.json, sim.json there)"""
import json,sys
from collections import defaultdict,Counter
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
rows=json.load(open(S+'/reach-rows.json'))
sim=json.load(open(S+'/sim.json'))
g=json.load(open(S+'/graph.json')); L=g['layers']; IMP={k:list(v) for k,v in g['imports'].items()}
D={d['name']:d for d in meta['decls']}
REG={r['name']:r for r in rows}
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
def deps(n): return [c for c in D[n]['type']+D[n]['value']+ctors.get(n,[]) if c in D]
LTSM={'GenerativeCore','Becoming.Frame'}
memo={}
def isl(n):
    if n in memo: return memo[n]
    st=[n]; seen={n}; hit=False
    while st:
        x=st.pop()
        if x not in D: continue
        if D[x]['module'] in LTSM: hit=True; break
        for c in D[x]['type']+D[x]['value']+ctors.get(x,[]):
            if c not in seen: seen.add(c); st.append(c)
    memo[n]=hit; return hit
mr={o['module']:o for o in json.load(open(S+'/module-reach.json'))}
for o in mr.values():
    o['class']='empty' if o['decls']==0 else ('all free' if o['stmt']+o['proof_only']==0 else 'mixed or lts')
CHAIN=['Becoming.Renewal','Becoming.Dependence','Becoming.Return','Becoming.Generation','Becoming.Dissipation','Becoming.Roles']
W2=['Becoming.Descent','Becoming.Significance','Becoming.Correspondence','Becoming.Metaethics','Becoming.Standpoints','Becoming.Recurrence','Becoming.Inquiry','Becoming.Testing','Becoming.Mechanism','Becoming.Counterfactual','Becoming.Capture','Becoming.Context','Becoming.Weighted','Becoming.Runs','Becoming.Description','Becoming.Learning','Becoming.Diagonal','Becoming.Identification','Becoming.Unfolding','Becoming.Likeness','Becoming.Histories','Becoming.Readings']
FOUND={'GenerativeCore','InquirySufficiency','RelationalRenewal'}
def clos(m,G):
    s=set();st=[m]
    while st:
        x=st.pop()
        for y in G.get(x,[]):
            if y not in s: s.add(y);st.append(y)
    return s
def acyclic(G):
    state={}
    def visit(x,stack):
        if state.get(x)==1: return False
        if state.get(x)==2: return True
        state[x]=1
        for y in G.get(x,[]):
            if not visit(y,stack): print('cycle at',x,'->',y); return False
        state[x]=2; return True
    sys.setrecursionlimit(100000)
    return all(visit(x,[]) for x in list(G))
EXIST=set(IMP); SUFFIX='Runs'
def run(split, strip, label, merge_existing=True):
    loc={n:d['module'] for n,d in D.items()}
    for n in sim['base']: loc[n]='Becoming.World'
    for n in sim['early_all']:
        if n not in sim['base']: loc[n]='Becoming.Labelled'
    target={}
    for X in split:
        short=X.split('.',1)[1]
        cand='Becoming.Labelled'+short
        target[X]=cand
        for n,d in D.items():
            if d['module']==X and loc[n]==X and isl(n): loc[n]=cand
    tmods=set(target.values())
    mods=set(loc.values())|set(IMP)
    need=defaultdict(set)
    for n,d in D.items():
        for c in deps(n):
            if loc[c]!=loc[n]: need[loc[n]].add(loc[c])
    lts_side={m for m in mods if m in LTSM or m in tmods or m=='Becoming.Labelled' or (m in mr and mr[m]['class']!='all free' and m not in split and m not in FOUND and m!='Becoming')}
    free_side={m for m in mods if m.startswith('Becoming.') and m not in lts_side}
    new={}
    for m in mods:
        cur=list(IMP.get(m,[]))
        if m=='Becoming.World': cur=[]
        if m=='Becoming.Labelled': cur=['Becoming.Frame','Becoming.World']
        for X,t in target.items():
            if m==t:
                cur=list(dict.fromkeys(cur+[X]+IMP[X]))
        if m in strip:
            cur=[i for i in cur if i in free_side or i in FOUND-{'GenerativeCore','InquirySufficiency'}]
        new[m]=cur
    new['Becoming.Dependence']=list(dict.fromkeys(new['Becoming.Dependence']+['Becoming.World']))
    if 'Becoming.Unfolding' not in split: new['Becoming.Unfolding']=new['Becoming.Unfolding']+['Becoming.Labelled']
    added=defaultdict(list)
    for it in range(6):
        for m in sorted(mods):
            c=clos(m,new)
            for x in sorted(need[m]-c-{m}):
                new[m].append(x); added[m].append(x)
    ok=acyclic(new)
    allfree=[m for m,o in mr.items() if o['class']=='all free' and m.startswith('Becoming.')]
    still=[m for m in allfree if 'Becoming.Frame' in clos(m,new)]
    splitfree=[X for X in split if 'Becoming.Frame' in clos(X,new)]
    changed=[m for m in IMP if set(new[m])!=set(IMP[m])]
    moved=Counter(loc[n] for n in REG if loc[n]!=D[n]['module'])
    src_edit=sorted({D[n]['module'] for n in REG if loc[n]!=D[n]['module']})
    merged=sorted(t for t in tmods if t in EXIST)
    import_only=sorted(m for m in changed if m not in src_edit and m not in merged)
    newmods=sorted(t for t in tmods if t not in EXIST)+['Becoming.World','Becoming.Labelled']
    core=set(L['CORE'])|set(newmods)
    print(f'== {label}: acyclic={ok}')
    print('  new modules',len(newmods),newmods)
    print('  existing modules receiving declarations',merged)
    print('  declarations moved by target:',dict(moved))
    print('  modules losing declarations',len(src_edit))
    print('  modules with import change only',len(import_only),import_only)
    print('  all-free modules reaching Frame',len(still),still[:12],'; split modules still reaching Frame',splitfree)
    print('  core modules with Frame in closure:',sum('Becoming.Frame' in clos(m,new) for m in core if m in new),'of',len(core))
    return dict(loc={n:loc[n] for n in REG if loc[n]!=D[n]['module']},imports=new,edited=src_edit,import_only=import_only,added=dict(added),still=still,new_modules=newmods,merged=merged,moved=dict(moved),acyclic=ok)
CHAINALL=CHAIN+['Becoming.Flow','Becoming.Change','Becoming.Population','Becoming.Locality','Becoming.Reserve','Becoming.Evolution','Becoming.Space']
n1=run(CHAIN,CHAINALL,'W1')
allfree=[m for m,o in mr.items() if o['class']=='all free' and m.startswith('Becoming.')]
n2=run(CHAIN+W2,CHAINALL+W2+allfree,'W1+W2')
json.dump({'W1':n1,'W12':n2},open(S+'/sim3.json','w'),indent=0)
# closed W2 set: every mixed module whose free constants are used by a free constant of a free-side module
mixed={m for m,o in mr.items() if o['class']!='all free' and o['class']!='empty' and m.startswith('Becoming.') and m not in ('Becoming.Frame',)}
allfree=[m for m,o in mr.items() if o['class']=='all free' and m.startswith('Becoming.')]
freeconst={n for n in D if not isl(n)}
use=defaultdict(set)   # module -> modules whose free constants its free constants use
for n in freeconst:
    for c in deps(n):
        if c in freeconst and D[c]['module']!=D[n]['module']: use[D[n]['module']].add(D[c]['module'])
side=set(allfree)|set(CHAINALL)
split=set(CHAIN)
changed=True
while changed:
    changed=False
    for m in list(side):
        for y in use[m]:
            if y in mixed and y not in split:
                split.add(y); side.add(y); changed=True
print('closed split set size',len(split),'LTS decls moved',sum(mr[m]['stmt']+mr[m]['proof_only'] for m in split))
W2c=sorted(split-set(CHAIN))
print('W2 modules',len(W2c),[m.replace('Becoming.','') for m in W2c])
EXIST=set()  # no merging into existing modules
_old=run
def run2(split,strip,label):
    return _old(split,strip,label)
# rename run modules to avoid collisions: patch target naming by suffix 'Process'
SUFFIX='Runs'
taken=[m for m in IMP if m.startswith('Becoming.')]
coll=[X for X in W2c if X+'Runs' in IMP]
print('name collisions with existing …Runs:',coll)
SUFFIX='Processes'
print('collisions …Processes:',[X for X in W2c if X+'Processes' in IMP])
n3=run(sorted(split),CHAINALL+W2c+allfree,'W1+W2 closed (run modules named …Processes for W2, …Runs for W1 chain)')
json.dump({'W1':n1,'W12':n3,'W2_modules':W2c},open(S+'/sim3.json','w'),indent=0)
# ---- per-batch spec ----
def descendants(G, roots):
    rev=defaultdict(set)
    for k,v in G.items():
        for i in v: rev[i].add(k)
    s=set(roots); st=list(roots)
    while st:
        x=st.pop()
        for y in rev.get(x,()):
            if y not in s: s.add(y); st.append(y)
    return s
def spec(prev_imp, prev_loc, cur, label):
    new=cur['imports']; loc=cur['loc']
    newmods=sorted(m for m in new if m not in prev_imp)
    moved={n:(prev_loc.get(n,D[n]['module']),t) for n,t in loc.items() if prev_loc.get(n,D[n]['module'])!=t}
    src=sorted({a for a,b in moved.values() if a in prev_imp})
    impch={m:{'before':sorted(prev_imp[m]),'after':sorted(new[m])} for m in prev_imp if m in new and set(prev_imp[m])!=set(new[m])}
    imp_only=sorted(m for m in impch if m not in src)
    touched=set(src)|set(impch)
    aff=descendants(new, touched|set(newmods))
    n_th=sum(1 for n in moved if REG[n]['kind']=='theorem')
    print(f'## {label}: new {len(newmods)}, declarations moved {len(moved)} ({n_th} theorems), sources edited {len(src)}, import-only {len(imp_only)}, compile steps whose inputs change {len(aff & set(new))} of {len(new)}')
    return dict(new_modules={m:sorted(new[m]) for m in newmods},
        moved={t:sorted(n for n,(a,b) in moved.items() if b==t) for t in sorted({b for a,b in moved.values()})},
        sources_edited=src, import_changes=impch, import_only=imp_only, affected_steps=len(aff&set(new)), steps=len(new),
        statements_changed=0)
P0=IMP; L0={}
W1=run(CHAIN,CHAINALL,'W1 final')
W12=run(sorted(split),CHAINALL+W2c+allfree,'W1+W2 final')
s1=spec(IMP,{},W1,'W1')
s2=spec(W1['imports'],W1['loc'],W12,'W2 (from the W1 tree)')
from functools import lru_cache
def depthmap(G):
    memo={}
    def d(m):
        if m in memo: return memo[m]
        ps=[p for p in G.get(m,[]) if p in G]
        memo[m]=0 if not ps else 1+max(d(p) for p in ps); return memo[m]
    return d
for lab,G in [('now',IMP),('after W1',W1['imports']),('after W2',W12['imports'])]:
    d=depthmap(G)
    print(lab,{m.replace('Becoming.',''):d(m) for m in ['Becoming.World','GenerativeCore','Becoming.Frame','Becoming.Labelled','Becoming.Space','Becoming.Unfolding'] if m in G}, 'max core', max(d(m) for m in G if m.startswith('Becoming.') and m in set(L['CORE'])|{'Becoming.World','Becoming.Labelled'}))
json.dump({'W1':s1,'W2':s2,'W2_set':W2c,'after_W1':{'all_free_reaching_Frame':W1['still']},'after_W2':{'all_free_reaching_Frame':W12['still']}},open(S+'/plan-batches.json','w'),indent=1)
CORE0=[m for m in L['CORE'] if m!='Becoming']
for lab,G in [('now',IMP),('after W1',W1['imports']),('after W2',W12['imports'])]:
    print(lab,'old core modules with Frame in closure',sum('Becoming.Frame' in clos(m,G) for m in CORE0),'of',len(CORE0),
          '; all-free reaching Frame',sum('Becoming.Frame' in clos(m,G) for m in allfree),'of',len(allfree))
