import json,collections,re
import os,subprocess
B=subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=os.path.dirname(os.path.abspath(__file__)),text=True).strip()+'/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'  # from the repository root
rc=json.load(open(B+'becoming-verification.json'))
g=json.load(open('graph.json'))['inherited']
x=json.load(open('classes.json'))
meta=json.load(open('tree/.build/bridge-meta.json')); mods=meta['modules']
# periphery modules referenced by the bridge ring
used=collections.defaultdict(set)   # periphery module -> bridge decls that mention it
for n,v in x.items():
    for c in v['trans_periphery']: used[mods.get(c,'?')].add(n)
names=[n for n in x]
rows=[]
for m in rc['modules']:
    mod=m['module']
    if mod not in g: continue
    thms=[d['name'] for d in m['declarations'] if d['kind']=='theorem']
    defs=[d['name'] for d in m['declarations'] if d['kind']!='theorem']
    restated=[];through=[];none_=[]
    for t in thms:
        last=t.split('.')[-1]
        # a bridge or join declaration whose name carries the periphery theorem's name, proved without it
        by_core=[n for n in names if (n.split('.')[-1].startswith(last) and n.split('.')[-1]!=last) or n.split('.')[-1]==last+'_by_core']
        by_core=[n for n in by_core if t not in x[n]['per_thm_used']]
        cites=[n for n in names if t in x[n]['per_thm_used']]
        if by_core: restated.append(t)
        elif cites: through.append(t)
        else: none_.append(t)
    dmention=[d for d in defs if any(d in x[n]['trans_periphery'] and x[n]['class'].startswith('1') for n in names)]
    rows.append({'module':mod,'path':g[mod]['path'],'theorems':len(thms),'restated_by_core':len(restated),
       'cited_by_join_or_instance':len(through),'untouched':len(none_),'defs':len(defs),
       'defs_identified_by_kind1':len(dmention),
       'bridge_decls':len(used.get(mod,())),
       'imported_by_periphery':g[mod]['imported_by_periphery'],'imported_by_spine':g[mod]['imported_by_bridge'],
       'restated':restated})
json.dump(rows,open('permods.json','w'),indent=1)
for r in sorted(rows,key=lambda r:-r['bridge_decls']):
    if r['bridge_decls']: print(f"{r['module']:34} thm={r['theorems']:3} byCore={r['restated_by_core']:3} cited={r['cited_by_join_or_instance']:3} untouched={r['untouched']:3} defs={r['defs']:3} idK1={r['defs_identified_by_kind1']:3} br={r['bridge_decls']:3} perDeps={len(r['imported_by_periphery'])}")
