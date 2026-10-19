import json,collections,re,os,sys
R='/Users/ren/theories/'
L=R+'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
C=json.load(open(R+'_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.json'))
th=C['theorems']; abm=C['apart_by_module']
new=[l.strip() for l in open(sys.argv[1])]
abbr={'statement on both families':'both','statement on Process/Frame/Run/Trace':'P','statement on World/Flow/Web':'W','proof through a base family':'prf','used by a theorem on the base':'used','apart: own vocabulary':'apart','apart: prelude-only statement':'prel'}
# parse decls per module
def decls(path):
    ns=[];out=[]
    for line in open(path):
        m=re.match(r'\s*namespace\s+(\S+)',line)
        if m: ns.append(m.group(1)); continue
        m=re.match(r'\s*end\s+(\S+)\s*$',line)
        if m and ns and ns[-1]==m.group(1): ns.pop(); continue
        m=re.match(r'\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(theorem|lemma)\s+(\S+)',line)
        if m:
            n=m.group(2)
            full='.'.join(ns+[n])
            out.append(full)
    return out
rows=[]
for m in new:
    p=L+m+'.lean'
    ds=decls(p)
    cnt=collections.Counter()
    miss=0
    for d in ds:
        c=th.get(d) or th.get('Becoming.'+d)
        if c is None: miss+=1; continue
        cnt[abbr[c]]+=1
    imps=[l.split()[1] for l in open(p) if l.startswith('import ')]
    lines=sum(1 for _ in open(p))
    a=abm.get('Becoming.'+m)
    rows.append((m,lines,len(ds),miss,dict(cnt),a,imps))
for r in sorted(rows,key=lambda r:-(r[5][0] if r[5] else 0)):
    m,lines,n,miss,cnt,a,imps=r
    print(f"{m:28s} L{lines:5d} thm{n:4d} miss{miss:3d} apart={a} {' '.join(f'{k}:{v}' for k,v in sorted(cnt.items()))} | imp {','.join(i.replace('Becoming.','') for i in imps)}")
