import json,re
from collections import Counter,defaultdict
D=json.load(open('decls.json'));ds=D['decls']
owners=set(d['full'] for d in ds if d['kind'] in('structure','inductive','class','def','abbrev'))
# witness namespaces: namespace segments (excluding Becoming) not equal to a declared type/def, which contain a def/inductive
wns=defaultdict(lambda: defaultdict(list))
for d in ds:
  if not d['ns'] or d['ns']=='Becoming': continue
  if d['ns'] in owners: continue
  wns[d['ns']][d['module']].append(d)
withdefs={ns:m for ns,m in wns.items() if any(x['kind'] in('def','inductive','structure','abbrev') for v in m.values() for x in v)}
print('namespaces not named after a declaration:',len(wns),' with their own definitions (witness/model namespaces):',len(withdefs))
print('theorems in them:',sum(1 for m in withdefs.values() for v in m.values() for x in v if x['kind']=='theorem'),' defs:',sum(1 for m in withdefs.values() for v in m.values() for x in v if x['kind']!='theorem'))
permod=Counter()
for ns,m in withdefs.items():
  for mod in m: permod[mod]+=1
print('modules with >=6 witness namespaces:',[(k[9:],v) for k,v in permod.most_common(25)])
# type signature classes of witness defs
sig=Counter()
ex=defaultdict(list)
for ns,m in withdefs.items():
  for mod,v in m.items():
    for x in v:
      if x['kind'] not in('def','abbrev'): continue
      st=' '.join(x['stmt'].split())
      mm=re.search(r':\s*((?:Process|Law|Web|Flow|World|Frame|ExchangeLaw|Run|Hexagram|Dependence|Formation)\b[^:=]*)$',st)
      if mm:
        t=re.sub(r'\s+',' ',mm.group(1)).strip()
        k=t.split()[0]; sig[t]+=1; ex[t].append((x['full'][9:],mod[9:]))
print('witness defs by type:'); 
for t,c in sig.most_common(25): print('  ',c,t,ex[t][:4])
json.dump({ns:{m:len(v) for m,v in mm.items()} for ns,mm in withdefs.items()},open('witness_ns.json','w'),indent=0)
