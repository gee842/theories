import json,sys
from collections import defaultdict,Counter
S=sys.argv[1]
meta=json.load(open(S+'/rr/.build/reroot-meta.json'))
rows=json.load(open(S+'/reach-rows.json'))
sim=json.load(open(S+'/sim.json'))
g=json.load(open(S+'/graph.json')); L=g['layers']; imp={k:list(v) for k,v in g['imports'].items()}
D={d['name']:d for d in meta['decls']}
ctors=defaultdict(list)
for n,d in D.items():
    if d['kind']=='ctor': ctors[n.rsplit('.',1)[0]].append(n)
def deps(n): return [c for c in D[n]['type']+D[n]['value']+ctors.get(n,[]) if c in D]
CHAIN=['Becoming.Renewal','Becoming.Dependence','Becoming.Return','Becoming.Generation','Becoming.Flow','Becoming.Change','Becoming.Population','Becoming.Dissipation','Becoming.Locality','Becoming.Roles','Becoming.Reserve','Becoming.Evolution','Becoming.Space']
lts_reg={r['name'] for r in rows if r['full_lts']}
# all constants (incl auto) that reach LTS, in chain modules
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
loc={n:d['module'] for n,d in D.items()}
for n in sim['base']: loc[n]='NEW.Base'
for n in sim['early_all']:
    if n not in sim['base']: loc[n]='NEW.ProcessReading'
moved_chain=[n for n,d in D.items() if d['module'] in CHAIN and isl(n)]
for n in moved_chain: loc[n]='NEW.ChainRuns'
print('chain LTS constants moved',len(moved_chain),'registry decls',len([n for n in moved_chain if n in {r["name"] for r in rows}]))
# new imports
new=dict(imp)
new['Becoming.Renewal']=['RelationalRenewal']
new['NEW.Base']=[]
new['Becoming.Dependence']=['Becoming.Renewal','NEW.Base']
new['NEW.ProcessReading']=['Becoming.Frame','NEW.Base'] # total moved to base anyway
new['Becoming.Unfolding']=imp['Becoming.Unfolding']+['NEW.ProcessReading']
new['NEW.ChainRuns']=['Becoming.Frame','Becoming.Space']
mods=set(L['FOUNDATION']+L['CORE'])|{'NEW.Base','NEW.ProcessReading','NEW.ChainRuns'}
def clos(m,G):
    s=set();st=[m]
    while st:
        x=st.pop()
        for y in G.get(x,[]):
            if y not in s: s.add(y);st.append(y)
    return s
need=defaultdict(set)
for n,d in D.items():
    m=loc[n]
    for c in deps(n):
        if loc[c]!=m: need[m].add(loc[c])
broken={}
for m in sorted(mods):
    if m not in new: continue
    c=clos(m,new)
    miss=need[m]-c-{m}
    if miss: broken[m]=sorted(miss)
print('modules missing an import after the cut:',len(broken))
for m,v in broken.items(): print('  ',m,'needs',v)
# depth of World now
from functools import lru_cache
@lru_cache(None)
def dep(m):
    ps=[p for p in new.get(m,[]) if p in mods]
    return 0 if not ps else 1+max(dep(p) for p in ps)
print('depths: Base',dep('NEW.Base'),'Frame',dep('Becoming.Frame'),'ProcessReading',dep('NEW.ProcessReading'),'Space',dep('Becoming.Space'),'Unfolding',dep('Becoming.Unfolding'))
fr=[m for m in L['CORE'] if 'Becoming.Frame' in clos(m,new)]
print('core modules with Frame in closure: before',sum('Becoming.Frame' in clos(m,imp) for m in L['CORE']),'after',len(fr))
mr=json.load(open(S+'/module-reach.json'))
allfree=[o['module'] for o in mr if o['stmt']==0 and o['proof_only']==0 and o['decls']>0 and o['module'].startswith('Becoming.')]
still=[m for m in allfree if 'Becoming.Frame' in clos(m,new)]
print('all-free core modules',len(allfree),'; with Frame in closure before',sum('Becoming.Frame' in clos(m,imp) for m in allfree),'after cut',len(still))
# compile steps whose key changes: modules (of the whole checked closure) whose closure contains an edited module
edited={'Becoming.Renewal','Becoming.Dependence','Becoming.Return','Becoming.Generation','Becoming.Flow','Becoming.Dissipation','Becoming.Roles','Becoming.Space','Becoming.Unfolding'}
allmods=list(imp)
aff=[m for m in allmods if m in edited or (clos(m,imp)&edited)]
print('compile steps in order',len(allmods),'; steps whose inputs change',len(aff))
regset={r['name'] for r in rows}
maxd=max(dep(m) for m in L['CORE'])
print('max core depth after cut',maxd)
json.dump({'moved_chain_declarations':sorted(n for n in moved_chain if n in regset),
  'early_readings':sorted(set(sim['early'])), 'late_readings':sorted(set(sim['late'])),
  'base_constants':sorted(sim['base']),
  'imports_to_add':broken,
  'core_modules_with_Frame_in_closure':{'before':sum('Becoming.Frame' in clos(m,imp) for m in L['CORE']),'after':len(fr)},
  'all_free_core_modules':{'count':len(allfree),'with_Frame_before':sum('Becoming.Frame' in clos(m,imp) for m in allfree),'with_Frame_after':len(still),'still_reaching_Frame':still},
  'compile_steps':{'in_order':len(allmods),'inputs_change':len(aff)},
  'depths_after':{'base':dep('NEW.Base'),'Frame':dep('Becoming.Frame'),'ProcessReading':dep('NEW.ProcessReading'),'Space':dep('Becoming.Space'),'Unfolding':dep('Becoming.Unfolding'),'max_core':maxd}},
  open(S+'/plan-sim.json','w'),indent=1)
