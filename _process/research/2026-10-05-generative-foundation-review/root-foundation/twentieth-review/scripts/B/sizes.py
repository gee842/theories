import json,re,os,statistics
from collections import Counter,defaultdict
ROOT="/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"
D=json.load(open('decls.json'));ds=D['decls'];sizes=D['sizes']
th=Counter(d['module'] for d in ds if d['kind']=='theorem')
mods=sorted(sizes)
vals=[th[m] for m in mods]
print('modules',len(mods),'theorems',sum(vals),'median',statistics.median(vals),'mean %.1f'%statistics.mean(vals))
for lo,hi in [(0,4),(5,9),(10,14),(15,29),(30,59),(60,99),(100,199),(200,999)]:
  ms=[m for m in mods if lo<=th[m]<=hi]; print('  %d-%d theorems: %d modules, %d lines'%(lo,hi,len(ms),sum(sizes[m] for m in ms)))
small=[m for m in mods if th[m]<15]
print('under 15:',len(small),'lines',sum(sizes[m] for m in small),'theorems',sum(th[m] for m in small))
print(' '.join('%s(%d)'%(m[9:],th[m]) for m in sorted(small,key=lambda m:th[m])))
print('largest by theorems:',[(m[9:],th[m],sizes[m]) for m in sorted(mods,key=lambda m:-th[m])[:15]])
# cohesion of big modules: sections, witness namespaces, internal reference components
ID=re.compile(r"[A-Za-z_][\w'.]*")
for m in ['Becoming.Counting','Becoming.OneStep','Becoming.Order','Becoming.Resolution','Becoming.Likeness','Becoming.Entropy','Becoming.Identity','Becoming.Identification','Becoming.Regulation','Becoming.Feedback','Becoming.Population','Becoming.Loops']:
  f=os.path.join(ROOT,m[9:]+'.lean'); src=open(f).read()
  secs=re.findall(r'^/-! ##+ (.*)',src,re.M)
  md=[d for d in ds if d['module']==m]
  names={}
  for d in md:
    parts=d['full'].split('.')
    for i in range(1,len(parts)): names.setdefault('.'.join(parts[i:]),set()).add(d['full'])
  par={d['full']:d['full'] for d in md}
  def find(x):
    while par[x]!=x: par[x]=par[par[x]]; x=par[x]
    return x
  for d in md:
    for t in set(ID.findall(d['stmt']+' '+d['body'])):
      for k in (t, t.split('.')[-1]):
        for tgt in names.get(k,()):
          if tgt!=d['full']: par[find(d['full'])]=find(tgt)
  comps=Counter(find(x) for x in par)
  big=[c for c in comps.values() if c>=10]
  nsc=Counter(d['ns'] for d in md)
  print('%s: %d lines, %d theorems, %d defs, %d section headers, %d namespaces, internal-reference components %d (>=10 members: %s, largest %d)'%(m[9:],sizes[m],th[m],sum(1 for d in md if d['kind']!='theorem'),len(secs),len(nsc),len(comps),len(big),max(comps.values())))
  print('    sections:', ' | '.join(s[:40] for s in secs[:30]))
