import json,sys,collections,subprocess
d=json.load(open('THEOREM-CONNECTIVITY.json'))
th=d['theorems']
print(type(th), list(th.items())[:2] if isinstance(th,dict) else th[:2])
new=[l.strip() for l in open(sys.argv[1])]
abbr={'statement on both families':'both','statement on Process/Frame/Run/Trace':'P','statement on World/Flow/Web':'W','proof through a base family':'prf','used by a theorem on the base':'used','apart: own vocabulary':'apart','apart: prelude-only statement':'prel'}
bym=collections.defaultdict(collections.Counter)
for t,c in th.items():
    c=c if isinstance(c,str) else c.get('class')
    # module guess: longest module prefix
    bym_key=None
    parts=t.split('.')
    for i in range(len(parts)-1,0,-1):
        m='.'.join(parts[:i])
        if m in modset: bym_key=m;break
    bym[bym_key][abbr.get(c,c)]+=1
