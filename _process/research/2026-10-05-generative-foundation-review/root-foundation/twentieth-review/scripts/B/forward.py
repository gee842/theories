import json,re
from collections import Counter,defaultdict
D=json.load(open('decls.json'));ds={d['full']:d for d in D['decls']}
r=json.load(open('wrappers.json'))
ID=re.compile(r"[A-Za-z_α-ω][A-Za-z0-9_'!?₀-₉.]*")
fw=[]
for x in r:
  if x['kind'] not in('alias-other-module','alias-same-module'): continue
  d=ds[x['full']]; body=' '.join(d['body'].split())
  body=re.sub(r'^by\s+(exact|simpa\s+using)\s+','',body)
  toks=ID.findall(body)[1:]
  stoks=set(ID.findall(d['stmt']))
  rest=[t for t in toks if t not in stoks and t not in ('mp','mpr','symm','_') and not re.fullmatch(r'\d+',t)]
  if not rest: fw.append(x)
print('pure forwarding (args only the theorem\'s own binders):',len(fw), Counter(x['kind'] for x in fw))
per=Counter(x['module'] for x in fw)
print(per.most_common(30))
json.dump(fw,open('forwarding.json','w'),indent=0,ensure_ascii=False)
import random;random.seed(1)
for x in random.sample(fw,15): print('  ',x['full'][9:],x['module'][9:],'|',x['body'][:100])
