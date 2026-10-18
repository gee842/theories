import json,re,pathlib,collections
here=pathlib.Path('.').resolve(); root=here.parent
d=json.load(open('becoming-verification.json'))
mods={m['module']:m for m in d['modules']}
paths=d['source_paths']
imports={}
for m,p in paths.items():
    f=(root/p) if not (here/p).exists() else here/p
    if not f.exists(): f=root/p
    txt=f.read_text() if f.exists() else ''
    imports[m]=re.findall(r'^import (\S+)',txt,re.M)
rev=collections.defaultdict(list)
for m,ims in imports.items():
    for i in ims: rev[i].append(m)
spine=set(d['spine_modules']); pj=set(d['periphery_join_modules']); found=set(d['foundation_modules'])
inh=[m for m in d['compile_order'] if m not in spine and m not in pj and m not in found]
print(len(inh),'inherited (non-foundation)')
out={}
for m in inh:
    deps=rev[m]
    out[m]={'path':paths[m],'theorems':mods[m]['theorems'],'decls':len(mods[m]['declarations']),
      'imported_by_bridge':[x for x in deps if x in spine],'imported_by_join':[x for x in deps if x in pj],
      'imported_by_periphery':[x for x in deps if x not in spine and x not in pj]}
json.dump({'imports':imports,'inherited':out},open('/private/tmp/claude-501/-Users-ren-theories/3aea53b8-c6fe-4816-90c7-b6c209d7001d/scratchpad/graph.json','w'),indent=1)
for m,v in out.items():
    print(f"{m:40} thm={v['theorems']:3} br={','.join(x.replace('Becoming.','') for x in v['imported_by_bridge'])} | pj={len(v['imported_by_join'])} | per={','.join(v['imported_by_periphery'])[:120]}")
