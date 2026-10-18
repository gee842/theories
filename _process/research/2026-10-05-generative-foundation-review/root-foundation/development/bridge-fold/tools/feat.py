import json,re
B='/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
rc=json.load(open(B+'becoming-verification.json'))
kinds={}
for m in rc['modules']:
    for d in m['declarations']: kinds[d['name']]=d['kind']
meta=json.load(open('tree/.build/bridge-meta.json')); info={d['name']:d for d in meta['decls']}; mods=meta['modules']
r=json.load(open('meta-res.json'))
exec(open('meta.py').read().split("missing=")[0].split("m=json.load")[0])  # CORE, BRIDGE, FOUND
def layer(mod):
    if mod.split('.')[0] in ('Init','Std','Lean'): return 'prelude'
    if mod in FOUND: return 'foundation'
    if mod in CORE: return 'core'
    if mod in BRIDGE: return 'bridge'
    return 'periphery'
for n,x in r.items():
    v=info[n]['value']
    x['per_thm_used']=sorted({c for c in v if layer(mods.get(c,'?'))=='periphery' and kinds.get(c)=='theorem'})
    x['core_thm_used']=sorted({c for c in v if layer(mods.get(c,'?')) in('core','foundation') and kinds.get(c)=='theorem'})
    x['bridge_used']=sorted({c for c in v if layer(mods.get(c,'?'))=='bridge' and c in r and c!=n})
json.dump(r,open('meta-res.json','w'),indent=1)
