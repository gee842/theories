"""I4a step 3: python3 -B similar.py DIR: the three core modules whose headers and declaration names share the most
weighted words with each module's (a suggestion to check by reading, never a classification)."""
import sys,json,re,math,collections,glob
S=sys.argv[1].rstrip('/')+'/'
B='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
rows=json.load(open(S+'connect.json'))
def words(t):
    t=re.sub(r'([a-z])([A-Z])',r'\1 \2',t)
    return [w.lower() for w in re.findall(r'[A-Za-z]{4,}',t)]
core={}
for p in sorted(glob.glob(B+'*.lean')):
    t=open(p).read()
    mm=re.search(r'/-!(.*?)-/',t,re.S)
    names=re.findall(r'^\s*(?:theorem|def|structure|inductive|abbrev)\s+(\S+)',t,re.M)
    core[p.split('/')[-1][:-5]]=words((mm.group(1) if mm else '')+' '+' '.join(names))
df=collections.Counter()
docs={k:collections.Counter(v) for k,v in core.items()}
for v in docs.values(): df.update(set(v))
N=len(docs)
idf={w:math.log(N/(1+c)) for w,c in df.items()}
def vec(c): 
    v={w:n*idf.get(w,math.log(N)) for w,n in c.items() if w in idf}
    s=math.sqrt(sum(x*x for x in v.values())) or 1
    return {w:x/s for w,x in v.items()}
cv={k:vec(c) for k,c in docs.items()}
for r in rows:
    c=collections.Counter(words(r['doc']+' '+' '.join(r['names'])+' '+r['stem']))
    v=vec(c)
    sims=sorted(((sum(x*cv[k].get(w,0) for w,x in v.items()),k) for k in cv),reverse=True)[:3]
    r['similar']=[(k,round(s,2)) for s,k in sims]
json.dump(rows,open(S+'connect.json','w'),ensure_ascii=False,indent=1)
print(len(core),'core modules')
