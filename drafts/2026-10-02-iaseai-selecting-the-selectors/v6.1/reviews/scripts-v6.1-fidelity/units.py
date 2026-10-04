"""Independent loss scan: segment v6.0 THEORY.md into the ledger's units (same segmentation),
split each into sentences, and measure each sentence's best trigram containment against the
whole of V6.1 (all .md files, pooled), and against each V6.1 paragraph individually."""
import re, json, pathlib, collections, sys
D=pathlib.Path('/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors')
S=pathlib.Path('/private/tmp/claude-501/-Users-ren-theories/125c36f5-6a17-4570-bcbc-ade65a8a973f/scratchpad/review61/fidelity')
old=(D/'v6/THEORY.md').read_text().split('\n## References')[0]
def norm(s):
    s=re.sub(r'\$\$.*?\$\$',' ',s,flags=re.S); s=re.sub(r'\$[^$]*\$',' ',s)
    s=re.sub(r'\[[^\]]*\]\([^)]*\)',' ',s)
    return re.findall(r"[a-z][a-z'\-]+",s.lower())
def grams(ws,n=3): return {tuple(ws[i:i+n]) for i in range(len(ws)-n+1)}
units=[]; sec='front'; pi=0
for block in re.split(r'\n\s*\n',old):
    b=block.strip()
    if not b: continue
    h=re.match(r'^(#{1,3}) (.*)',b)
    if h:
        m=re.match(r'(\d+(?:\.\d+)?|Appendix [A-G](?:\.\d)?|A\.\d)',h.group(2))
        sec=(m.group(1) if m else h.group(2)[:20]); pi=0
        rest=b.split('\n',1)
        if len(rest)<2: continue
        b=rest[1]
    pi+=1
    ws=norm(b)
    if len(ws)<8: continue
    units.append((f'L-60-§{sec}-p{pi:02d}',b))
# V6.1 pooled grams
pool=set(); paras=[]
for f in sorted((D/'v6.1').glob('*.md')):
    t=f.read_text()
    for p in re.split(r'\n\s*\n',t):
        ws=norm(p); g=grams(ws)
        pool|=g
        if g: paras.append((f.name,p[:80].replace('\n',' '),g))
def sents(b):
    b=re.sub(r'\$\$.*?\$\$',' [EQ] ',b,flags=re.S)
    return [s.strip() for s in re.split(r'(?<=[.;:!?])\s+(?=[A-Z*(\[])',b) if len(norm(s))>=7]
out=[]
for uid,b in units:
    for s in sents(b):
        g=grams(norm(s))
        if not g: continue
        c=len(g&pool)/len(g)
        out.append(dict(unit=uid,cont=round(c,2),sent=s))
json.dump(dict(units=[(u,b) for u,b in units],sents=out),open(S/'units.json','w'),ensure_ascii=False)
print(len(units),'units',len(out),'sentences')
cnt=collections.Counter()
for o in out:
    cnt['<0.2' if o['cont']<0.2 else '<0.4' if o['cont']<0.4 else '>=0.4']+=1
print(cnt)
