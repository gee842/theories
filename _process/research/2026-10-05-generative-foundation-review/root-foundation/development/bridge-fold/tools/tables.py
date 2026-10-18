import json,collections
x=json.load(open('classes.json'))
a=json.load(open('/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'))['roots']
BR=['Bridge','CompositionBridge','JoiningBridge','GranularityBridge','RepairComparison','Instances','RenewalBridge','CoursesBridge']
order=[]
for v in x.values():
    if v['module'] not in order: order.append(v['module'])
K=['1 R-def','1 R-enc','2 C','3 A-inst','3 A-hand','3 A-join','3 A-read','3 A-sup']
print('| Module | thms | 1 def | 1 enc | 2 | 3 inst | 3 hand | 3 join | 3 sup | defs (1/2/3) | movable thms/defs |')
print('|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|')
tot=collections.Counter()
for m in order:
    T=[v for v in x.values() if v['module']==m and v['kind']=='theorem']
    D=[v for v in x.values() if v['module']==m and v['kind']!='theorem']
    c=collections.Counter(v['class'] for v in T); d=collections.Counter(v['class'][0] for v in D)
    mt=sum(v['movable'] for v in T); md=sum(v['movable'] for v in D)
    row=[len(T)]+[c[k] for k in K if k not in('3 A-read',)]
    tot.update({'thms':len(T),**{k:c[k] for k in K},'d1':d['1'],'d2':d['2'],'d3':d['3'],'mt':mt,'md':md,'defs':len(D)})
    print(f"| `{m.replace('Becoming.','')}` | {len(T)} | {c['1 R-def']} | {c['1 R-enc']} | {c['2 C']} | {c['3 A-inst']} | {c['3 A-hand']} | {c['3 A-join']} | {c['3 A-sup']} | {len(D)} ({d['1']}/{d['2']}/{d['3']}) | {mt}/{md} |")
print(f"| **Total** | {tot['thms']} | {tot['1 R-def']} | {tot['1 R-enc']} | {tot['2 C']} | {tot['3 A-inst']} | {tot['3 A-hand']} | {tot['3 A-join']} | {tot['3 A-sup']} | {tot['defs']} ({tot['d1']}/{tot['d2']}/{tot['d3']}) | {tot['mt']}/{tot['md']} |")
# per kind citations
print()
for grp,pred in (('eight bridges',lambda v:v['module'].split('.')[-1] in BR),('31 joins',lambda v:v['module'].split('.')[-1] not in BR)):
  for k in ('1','2','3'):
    T=[v for v in x.values() if pred(v) and v['kind']=='theorem' and v['class'][0]==k]
    cited=[v for v in T if v['records']]; recs=collections.Counter(r for v in T for r in v['records'])
    ch=sorted({s for v in T for s in v['chapter']})
    print(grp,k,len(T),'cited',len(cited),'records',len(recs), recs.most_common(60)); print('   chapter',ch)
# roots
print()
bi=[(n,v) for n,v in a.items() if v['category']=='bridge-interface']
c=collections.Counter()
for n,v in bi:
    k=x[n]['class'] if n in x else 'outside the 39 modules'
    c[k]+=1; print(n,'|',v['module'],'|',k)
print(c)
mw=[(n,v['category'],x[n]['class']) for n,v in a.items() if n in x and v['category']!='bridge-interface']
print(mw)
