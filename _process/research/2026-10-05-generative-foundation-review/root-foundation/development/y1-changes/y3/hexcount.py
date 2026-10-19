import itertools, re, json
ORDER_SRC = open('/Users/ren/theories/.claude/worktrees/reverent-tu-7f9353/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Hexagrams.lean').read()
order=[]; names=[]
for m in re.finditer(r'⟨(true|false), (true|false), (true|false), (true|false), (true|false), (true|false)⟩,?\s+-- (\d+) (\S+):', ORDER_SRC):
    order.append(tuple(x=='true' for x in m.groups()[:6])); names.append(m.group(8))
assert len(order)==64
name={s:n for s,n in zip(order,names)}
num={s:i+1 for i,s in enumerate(order)}
T,F=True,False
def nuc(s): a,b,c,d,e,f=s; return (b,c,d,c,d,e)
def wax(s): a,b,c,d,e,f=s; return (not f,a,b,c,d,e)
def comp(s): return tuple(not x for x in s)
def rev(s): return tuple(reversed(s))
allh=list(itertools.product([F,T],repeat=6))
core=[s for s in allh if nuc(nuc(s))==s or nuc(s)==s]
print('core', [name[s] for s in core])
# returns under nuc
def orbit(f,s,n):
    for _ in range(n): s=f(s)
    return s
ret=[s for s in allh if any(orbit(nuc,s,p)==s for p in range(1,65))]
print('returns', [name[s] for s in ret])
entry={0:0,1:0,2:0}
for s in allh:
    k=min(k for k in range(3) if orbit(nuc,s,k) in ret); entry[k]+=1
print('entry', entry)
basin={}
for s in allh:
    t=orbit(nuc,s,2); key=name[t] if t in [(T,)*6,(F,)*6] else 'cycle'; basin[key]=basin.get(key,0)+1
print('basins', basin)
print('nuc image size', len(set(map(nuc,allh))), 'nuc2 image', len(set(orbit(nuc,s,2) for s in allh)))
print('commute comp', all(nuc(comp(s))==comp(nuc(s)) for s in allh), 'rev', all(nuc(rev(s))==rev(nuc(s)) for s in allh))
# middle pair lumping
mid=lambda s:(s[2],s[3])
print('mid lumped', all(mid(nuc(s))==mid(nuc(t)) for s in allh for t in allh if mid(s)==mid(t)))
yang=lambda s:sum(s)
bad=[(name[s],name[t]) for s in allh for t in allh if yang(s)==yang(t) and yang(nuc(s))!=yang(nuc(t))]
print('yang not lumped e.g.', bad[:3])
# merge witness
for s in allh:
    for t in allh:
        if s<t and nuc(s)==nuc(t): print('merge', name[s],name[t],'->',name[nuc(s)]); break
    else: continue
    break
print('--- H2')
seen=set(); orbs=[]
for s in order:
    if s in seen: continue
    o=[s]; t=wax(s)
    while t!=s: o.append(t); t=wax(t)
    seen|=set(o); orbs.append(o)
def alt(s): return sum(1 for i in range(5) if s[i]!=s[i+1])
def rises(s): return sum(1 for i in range(5) if (not s[i]) and s[i+1])
def falls(s): return sum(1 for i in range(5) if s[i] and not s[i+1])
def kept(s): return rises(s)+falls(s)+(1 if s[0]==s[5] else 0)
for o in orbs: print(len(o), name[o[0]], [name[x] for x in o], 'kept', {kept(x) for x in o})
print('kept conserved', all(kept(wax(s))==kept(s) for s in allh))
from collections import Counter
print('values', Counter(kept(s) for s in allh))
print('--- H4')
def cls(s): return frozenset([s,comp(s),rev(s),comp(rev(s))])
classes=set(cls(s) for s in allh)
print('classes', len(classes), Counter(len(c) for c in classes))
fixrev=[s for s in allh if rev(s)==s]; fixcr=[s for s in allh if comp(rev(s))==s]
print('fixed by rev', [name[s] for s in fixrev]); print('fixed by comp rev', [name[s] for s in fixcr])
# order pairs by complement
pairs=[(order[2*i],order[2*i+1]) for i in range(32)]
bycomp=[p for p in pairs if p[1]==comp(p[0]) and rev(p[0])==p[0]]
print('pairs by comp', [(name[a],name[b]) for a,b in bycomp])
both=[(name[a],name[b]) for a,b in pairs if b==comp(a) and b==rev(a)]
print('pairs where both rev and comp', both)
# waxWane on classes lumped?
def canon(s): return min(cls(s))
print('classes lumped for wax?', all(canon(wax(s))==canon(wax(t)) for s in allh for t in allh if canon(s)==canon(t)))
print('classes lumped for nuc?', all(canon(nuc(s))==canon(nuc(t)) for s in allh for t in allh if canon(s)==canon(t)))
ex=[(name[s],name[t]) for s in allh for t in allh if canon(s)==canon(t) and canon(wax(s))!=canon(wax(t))][:3]; print('wax counterex', ex)
print('--- H5')
def val(s): return sum((1<<i) for i in range(6) if s[i])
def ofval(n): return tuple(bool((n>>i)&1) for i in range(6))
def cnt(s): return ofval((val(s)+1)%64)
o=[(F,)*6]; t=cnt(o[0])
while t!=o[0]: o.append(t); t=cnt(t)
print('counter orbit', len(o))
