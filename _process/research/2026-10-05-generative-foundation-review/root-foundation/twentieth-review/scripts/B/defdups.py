import json,re,sys
sys.argv=['x']
exec(open('dups.py').read().split("th = [d for d")[0])
from collections import defaultdict
res={}
for mode in ('exact','shape'):
  g=defaultdict(list)
  for d in ds:
    if d['kind'] not in ('def','abbrev','structure','inductive'): continue
    txt=d['stmt']+' := '+d['body'] if d['kind'] in('def','abbrev') else d['stmt']+d['body']
    k=norm(txt,d['name'],mode)
    if len(k.split())<12: continue
    g[k].append(d)
  cross={k:v for k,v in g.items() if len(set(x['module'] for x in v))>1}
  res[mode]=cross
  print('==',mode,'cross-module definition groups (>=12 tokens):',len(cross),'defs',sum(len(v) for v in cross.values()))
ex=set(tuple(sorted(x['full'] for x in v)) for v in res['exact'].values())
for mode in ('exact','shape'):
  print('#####',mode)
  for k,v in sorted(res[mode].items(),key=lambda kv:-len(kv[0].split())):
    if mode=='shape' and tuple(sorted(x['full'] for x in v)) in ex: continue
    print(len(v),[(x['full'][9:],x['kind'],x['module'][9:],x['line']) for x in v][:5]); print('     ',k[:150])
