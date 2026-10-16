"""Paragraph-level preservation check: map every v6.0 paragraph to its best-matching V6.1 section by trigram
containment and content-word coverage. Writes src/preserve.json (LEDGER-units.tsv is built from it)."""
import re, json, pathlib, collections
D=pathlib.Path('/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors')
old=(D/'v6/THEORY.md').read_text().split('\n## References')[0]
def norm(s):
    s=re.sub(r'\$\$.*?\$\$',' ',s,flags=re.S); s=re.sub(r'\$[^$]*\$',' ',s)
    s=re.sub(r'\[[^\]]*\]\([^)]*\)',' ',s)
    return re.findall(r"[a-z][a-z'\-]+",s.lower())
STOP=set("the a an of and or to in on at by for with from as is are was were be been that this these those it its their there which who whom what when where than then not no but if so such each every any all can may must would could should does do did has have had more most less least into over under between among within without about also only own same other others one two three".split())
def grams(ws,n=3): return {tuple(ws[i:i+n]) for i in range(len(ws)-n+1)}
def content(ws): return {w for w in ws if w not in STOP and len(w)>5}
# old units
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
    units.append((f'L-60-§{sec}-p{pi:02d}',b[:90].replace('\n',' '),ws))
# new sections
new=[]
for doc in ['THEORY','SUPPLEMENT','DISCUSSION','TESTS','EVIDENCE','CLAIMS']:
    t=(D/'v6.1'/f'{doc}.md').read_text().split('\n## References')[0]
    for part in re.split(r'(?m)^(?=#{2,3} )',t):
        head=part.splitlines()[0][:50] if part.strip() else ''
        ws=norm(part)
        new.append((doc,head,grams(ws),content(ws)))
out=[]
for uid,start,ws in units:
    g=grams(ws); c=content(ws)
    best=max(new,key=lambda s: len(g&s[2])/max(len(g),1)+0.5*len(c&s[3])/max(len(c),1))
    cont=len(g&best[2])/max(len(g),1); cov=len(c&best[3])/max(len(c),1)
    status='kept' if cont>=0.4 else ('rewritten' if (cont>=0.12 or cov>=0.6) else 'check')
    out.append(dict(unit=uid,start=start,dest=f'{best[0]} {best[1]}',trigram=round(cont,2),terms=round(cov,2),status=status))
json.dump(out,open(D/'v6.1'/'src'/'preserve.json','w'),indent=0,ensure_ascii=False)
print(collections.Counter(o['status'] for o in out), len(out))
for o in out:
    if o['status']=='check': print(o['unit'],'|',o['trigram'],o['terms'],'|',o['start'][:80],'→',o['dest'][:40])
