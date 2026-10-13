import re, sys, glob, os
def decls(path):
    ns=[]; out=[]
    for line in open(path, encoding='utf-8'):
        m=re.match(r'^namespace\s+(\S+)', line)
        if m: ns.append(m.group(1)); continue
        m=re.match(r'^end\s+(\S+)\s*$', line)
        if m and ns and ns[-1]==m.group(1): ns.pop(); continue
        m=re.match(r'^(?:private\s+|protected\s+|noncomputable\s+)*(theorem|def|structure|inductive|abbrev|instance)\s+([^\s:({\[]+)', line)
        if m:
            name=m.group(2)
            out.append('.'.join(ns+[name]))
    return out
mine=set(decls(sys.argv[1]))
others={}
for f in sys.argv[2:]:
    if os.path.abspath(f)==os.path.abspath(sys.argv[1]): continue
    for d in decls(f): others.setdefault(d,[]).append(f)
for d in sorted(mine):
    if d in others: print("COLLISION", d, others[d])
print(len(mine), "declarations checked")
