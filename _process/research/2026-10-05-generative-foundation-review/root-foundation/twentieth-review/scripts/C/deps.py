import re,collections
p='/Users/ren/theories/theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
L=open(p,encoding='utf-8').read().split('\n')
heads=[(i,l) for i,l in enumerate(L,1) if l.startswith('## ')]
heads.append((len(L)+1,'END'))
def key(t):
    m=re.match(r'## (\d+)\.',t)
    if m: return 'S'+m.group(1)
    return {'## In one sentence':'One','## The theory stated in full':'Full','## The theory without axiom (sections 1–6)':'NoAx','## The theory stated whole':'Whole'}.get(t.strip(),t)
blocks={}
for (a,t),(b,_) in zip(heads,heads[1:]):
    blocks[key(t)]='\n'.join(L[a-1:b-1])
refre=re.compile(r'(?:§|sections? )(\d+)(?:\.(\d+))?')
print('== cross-references (target section counts) ==')
for k,txt in blocks.items():
    c=collections.Counter()
    for m in refre.finditer(txt):
        c['§'+m.group(1)+('.'+m.group(2) if m.group(2) else '')]+=1
    # also "sections 6.8, 6.15" lists
    for m in re.finditer(r'sections ([\d\.,– and]+)',txt):
        for n in re.findall(r'\d+(?:\.\d+)?',m.group(1))[1:]:
            c['§'+n]+=1
    top=sorted(c.items(),key=lambda x:-x[1])
    print(k, sum(c.values()), top[:25])
# backticked names per block
names={k:set(re.findall(r'`([^`]+)`',v)) for k,v in blocks.items()}
print('== name sets ==')
for k,v in names.items(): print(k,len(v))
body=set().union(*[names[k] for k in ['S1','S2','S3','S4','S5','S6','S7']])
for k in ['One','Full','S0','Whole','S8','S9','S10']:
    s=names[k]
    print(k,'names',len(s),'also in §1-§7:',len(s&body), round(100*len(s&body)/max(len(s),1)),'%')
# names repeated across many places
allc=collections.Counter()
for k,v in blocks.items():
    for n in set(re.findall(r'`([^`]+)`',v)): allc[n]+=1
tot=collections.Counter(re.findall(r'`([^`]+)`','\n'.join(L)))
print('== most cited names (total occurrences) ==')
for n,c in tot.most_common(40): print(c,allc[n],n)
print('distinct backticked', len(tot), 'occurring once', sum(1 for c in tot.values() if c==1))
