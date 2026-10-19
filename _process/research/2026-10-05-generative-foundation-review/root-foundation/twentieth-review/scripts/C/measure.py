import re,sys,collections,json
p='/Users/ren/theories/theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
L=open(p,encoding='utf-8').read().split('\n')
# sections: top-level ## and ### for section 6/7/8
secs=[]
for i,l in enumerate(L,1):
    if l.startswith('## ') or l.startswith('### '):
        secs.append((i,l.strip('# ').strip()))
secs.append((len(L)+1,'END'))
def rng(a,b): return L[a-1:b-1]
rows=[]
tot=collections.Counter()
hashre=re.compile(r'\b[0-9a-f]{8,12}\b')
rcpt=re.compile(r'\b2026\d{4}T\d{6}(?:\.\d+Z)?')
datere=re.compile(r'\b\d{1,2} October 2026|\b2026-10-\d\d|\b1\d October\b|\b[0-9] October\b')
board=re.compile(r'\b(?:P\d{2,3}[a-z]?|R\d{1,2}[a-z]?|U[2-5]|F[1-3][A-Z]?|G[1-5]|M[1-4]|K[1-3]|Y[1-5]|V2?|S[1-3]|L[12]|C[12]|E1|O[12]|SC|RG|RC|RH|RO|HS|MD1|LL1|PT1|Z1|SG|A4-L|W[1-3]|N[1-7]|I[1-5])\b')
procw=re.compile(r'\b(landed|landing|receipt|board item|study section|study §|rerun|checker|sweep|commit)\b',re.I)
renre=re.compile(r'\bRen\b')
dref=re.compile(r'\bD\d{1,2}\b')
for (a,t),(b,_) in zip(secs,secs[1:]):
    body=rng(a,b)
    txt='\n'.join(body)
    words=len(re.findall(r'\S+',txt))
    bt=re.findall(r'`[^`]+`',txt)
    lines_nonempty=[x for x in body if x.strip()]
    lines_bt=[x for x in lines_nonempty if '`' in x]
    r=dict(start=a,title=t[:60],lines=b-a,bytes=len(txt.encode()),words=words,
           backticks=len(bt),bt_per_100w=round(100*len(bt)/max(words,1),1),
           hashes=len(hashre.findall(txt)),receipts=len(rcpt.findall(txt)),
           dates=len(datere.findall(txt)),proc=len(procw.findall(txt)),ren=len(renre.findall(txt)),
           drefs=len(dref.findall(txt)),links=txt.count(']('))
    rows.append(r)
    for k in ['bytes','words','backticks','hashes','receipts','dates','proc','ren','drefs','links']:
        tot[k]+=r[k]
for r in rows:
    print('{start:5} {lines:4} {bytes:7} {words:6} bt={backticks:4} ({bt_per_100w:5}/100w) hash={hashes:3} rcpt={receipts:3} date={dates:3} proc={proc:3} Ren={ren:3} D={drefs:3} links={links:3}  {title}'.format(**r))
print(dict(tot))
nonempty=[x for x in L if x.strip()]
print('nonempty lines',len(nonempty),'with backticks',sum('`' in x for x in nonempty))
json.dump(rows,open('/private/tmp/claude-501/-Users-ren--claude-spares-spare-RPrOpt/640236e0-5942-4f65-ba76-5e779f26edff/scratchpad/review/c-work/sections.json','w'),indent=1,ensure_ascii=False)
