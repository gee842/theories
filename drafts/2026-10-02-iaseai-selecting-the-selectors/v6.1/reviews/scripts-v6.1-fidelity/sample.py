import json, csv, random, re, collections, pathlib
S=pathlib.Path('/private/tmp/claude-501/-Users-ren-theories/125c36f5-6a17-4570-bcbc-ade65a8a973f/scratchpad/review61/fidelity')
D=pathlib.Path('/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1')
J=json.load(open(S/'units.json'))
text=dict((u,b) for u,b in J['units'])
low=collections.defaultdict(list)
for o in J['sents']:
    if o['cont']<0.25: low[o['unit']].append(o)
rows=list(csv.reader(open(D/'LEDGER-units.tsv'),delimiter='\t'))[1:]
status={r[0]:(r[5],r[2],r[6]) for r in rows}
assert set(status)==set(text), (len(set(status)^set(text)))
def top(u):
    m=re.match(r'L-60-§(\d+|A|Appendix [A-G]|[^-]+)',u); s=m.group(1)
    return s
random.seed(20261004)
bysec=collections.defaultdict(lambda: collections.defaultdict(list))
for u,(st,_,_) in status.items(): bysec[top(u)][st].append(u)
sample=[]
for sec in bysec:
    ch=bysec[sec]['check']; rw=bysec[sec]['rewritten']
    sample+=random.sample(ch,min(len(ch),2))
    sample+=random.sample(rw,min(len(rw),4 if len(rw)>12 else 2))
sample=sorted(set(sample))
print(len(sample), collections.Counter(status[u][0] for u in sample))
print(collections.Counter(top(u) for u in sample))
json.dump(sample,open(S/'sample.json','w'))
with open(S/'sample_dump.txt','w') as f:
    for u in sample:
        st,dest,disp=status[u]
        f.write(f'=== {u} [{st}] dest={dest} | {disp}\n{text[u]}\n--- low sentences:\n')
        for o in low[u]: f.write(f'  ({o["cont"]}) {o["sent"][:400]}\n')
        f.write('\n')
