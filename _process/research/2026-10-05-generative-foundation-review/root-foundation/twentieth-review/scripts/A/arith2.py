import json,re,collections,os
H=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(H+'/decls.json'))
OK={'Nat','Int','List','Bool','Prop','Option','Type','True','False','Unit','Iff','Eq','Or','And','Not','Exists'}
LM={'map','length','sum','filter','all','any','append','reverse','foldl','foldr','head','tail','contains','succ','beq','ble','find?','bind','some','none','inl','inr','mem','zero','one','sub','add','mul'}
def body(d):
    st=d['stmt']; return st.split(d['name'],1)[1] if d['name'] in st else st
def strict(d):
    b=body(d)
    ids=re.findall(r'(?<![\w.])([A-Z]\w*)',b)
    if not all(i in OK for i in ids): return False
    for a,s in re.findall(r'\b([A-Za-z]\w*)\.([\w?]+)',b):
        if a in OK: continue
        if s not in LM: return False
    return True
TH=[d for d in D if d['kind']=='theorem' and strict(d)]
print('strict prelude-only theorems',len(TH),'of',sum(1 for d in D if d['kind']=='theorem'))
SH={'Becoming.Naturals','Becoming.Integers','Becoming.IntegerOrder','Becoming.ListTests'}
c=collections.Counter(d['module'] for d in TH)
print('in shared modules',sum(v for k,v in c.items() if k in SH),'outside',sum(v for k,v in c.items() if k not in SH),'modules with any',len(c))
print(c.most_common(30))
def norm(d):
    b=re.sub(r'\s+',' ',body(d)).strip()
    # alpha-rename lowercase identifiers not followed by '.' and not keywords
    kw={'fun','by','rfl','at','with','match','if','then','else','let','in','have','show','from','exact','intro'}
    names={}
    def rep(m):
        w=m.group(0)
        if w in kw or w in OK: return w
        if w not in names: names[w]='v%d'%len(names)
        return names[w]
    b=re.sub(r'(?<![\w.])[a-z]\w*(?![\w.])',rep,b)
    b=b.split(' | ')[0]
    return b
G=collections.defaultdict(list)
for d in TH: G[norm(d)].append(d)
rep=[(k,v) for k,v in G.items() if len(set(x['module'] for x in v))>1]
print('statement shapes proved in >1 module',len(rep),'theorems involved',sum(len(v) for k,v in rep))
for k,v in sorted(rep,key=lambda kv:-len(kv[1])):
    print(len(v),[x['q']+'@'+x['module'].split('.')[1]+':'+str(x['line']) for x in v],'|',k[:110])
