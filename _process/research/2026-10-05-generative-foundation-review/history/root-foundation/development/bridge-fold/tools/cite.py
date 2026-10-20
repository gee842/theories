import json,re,glob,os,collections
import subprocess
T=subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=os.path.dirname(os.path.abspath(__file__)),text=True).strip()+'/'  # the repository root, from this script's location
r=json.load(open('meta-res.json'))
recs={}
for f in glob.glob(T+'theories/becoming/results/records/*.json'):
    rid=os.path.basename(f)[:-5]
    d=json.load(open(f)); d.pop('history',None)
    txt=json.dumps(d,ensure_ascii=False)
    recs[rid]=txt
chap=open(T+'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md').read().split('\n')
heads=[];cur='(top)'
for line in chap:
    m=re.match(r'^(#{2,4}) (.*)',line)
    if m: cur=m.group(2)[:70]
    heads.append(cur)
def suffixes(text):
    out=set()
    for tok in re.findall(r"[A-Za-z_][\w'.]*[\w']", text):
        parts=tok.split('.')
        for i in range(len(parts)): out.add('.'.join(parts[i:]))
    return out
def keys(n,mod):
    short=n[len('Becoming.'):] if n.startswith('Becoming.') else n
    parts=short.split('.'); last=parts[-1]; ks=[]
    if len(parts)>1: ks.append('.'.join(parts[-2:]))
    if len(parts)==1 or parts[0]==mod.split('.')[-1]:
        if last.count('_')>=2 or len(last)>=16: ks.append(last)
    return ks
recset={rid:suffixes(t) for rid,t in recs.items()}
lineset=[suffixes(l) for l in chap]
for n,x in r.items():
    K=keys(n,x['module'])
    x['records']=sorted(rid for rid,S in recset.items() if any(k in S for k in K))
    x['chapter']=sorted({heads[i] for i,S in enumerate(lineset) if any(k in S for k in K)})
modfile={m:m.split(".")[-1]+".lean" for m in {x["module"] for x in r.values()}}
for m in modfile:
    pass
bind=collections.defaultdict(list)
for rid,txt in recs.items():
    for m,fn in modfile.items():
        if '/Becoming/'+fn in txt: bind[m].append(rid)
json.dump(r,open('meta-res.json','w'),indent=1)
json.dump(bind,open('module-bindings.json','w'),indent=1)
print(sum(1 for x in r.values() if x['records']), 'decls cited by a record;', sum(1 for x in r.values() if x['chapter']),'in chapter')
for m,l in bind.items(): print(m, len(l))
