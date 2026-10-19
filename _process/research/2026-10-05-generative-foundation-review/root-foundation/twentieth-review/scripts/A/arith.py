import json,re,collections,os
D=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/decls.json'))
OK={'Nat','Int','List','Bool','Prop','Option','Type','True','False','Fin','Unit','Iff','Eq','Or','And','Not','Exists','Prod','Sum','Sort'}
def prelude_only(d):
    st=d['stmt']
    body=st.split(d['name'],1)[1] if d['name'] in st else st
    ids=re.findall(r'(?<![\w.])([A-Z][\w]*)',body)
    dotted=re.findall(r'\b([A-Za-z]\w*)\.(\w+)',body)
    return all(i in OK for i in ids) and all(a in OK or a[0].islower() for a,_ in dotted)
th=[d for d in D if d['kind']=='theorem' and prelude_only(d)]
print('prelude-only theorems',len(th))
bymod=collections.Counter(d['module'] for d in th)
print(bymod.most_common(40))
# group by last name
g=collections.defaultdict(list)
for d in th: g[d['name'].split('.')[-1]].append(d)
dup={k:v for k,v in g.items() if len(set(x['module'] for x in v))>1}
print('names repeated across modules',len(dup))
for k,v in sorted(dup.items(),key=lambda kv:-len(kv[1]))[:60]:
    print(k,len(v),sorted(set(x['module'].split('.')[1] for x in v)))
# normalized statement grouping
def norm(d):
    st=d['stmt']; st=st.split(d['name'],1)[1] if d['name'] in st else st
    st=re.sub(r'\s+',' ',st)
    # rename bound var names a..z single letters? keep
    return st.strip()
g2=collections.defaultdict(list)
for d in th: g2[norm(d)].append(d)
dd=[(k,v) for k,v in g2.items() if len(set(x['module'] for x in v))>1]
print('identical statements in >1 module',len(dd))
for k,v in sorted(dd,key=lambda kv:-len(kv[1]))[:40]:
    print(len(v),[x['q'] for x in v][:6],'|',k[:140])
