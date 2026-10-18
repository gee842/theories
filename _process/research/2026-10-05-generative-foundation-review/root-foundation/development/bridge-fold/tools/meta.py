import json,re,collections
B='/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
src=open(B+'check_becoming.py').read()
def lst(name): return re.findall(r'"([A-Za-z.]+)"', re.search(r"^"+name+r" = \[(.*?)\]", src, re.S|re.M).group(1))
CORE=set(lst('CORE')); BRIDGE=lst('BRIDGE'); FOUND={'GenerativeCore','InquirySufficiency','RelationalRenewal'}
m=json.load(open('tree/.build/bridge-meta.json')); inv=json.load(open('inv.json'))
mods=m['modules']; info={d['name']:d for d in m['decls']}
def layer(mod):
    if mod.split('.')[0] in ('Init','Std','Lean'): return 'prelude'
    if mod in FOUND: return 'foundation'
    if mod in CORE: return 'core'
    if mod in BRIDGE: return 'bridge'
    return 'periphery'
def lay(c): return layer(mods.get(c, info[c]['module'] if c in info else '?'))
def aux(n): return any(p.startswith('_') or re.match(r'(match|proof|eq|eq_def|injEq|sizeOf_spec|rec|recOn|casesOn|brecOn|below|noConfusion|noConfusionType|ctorIdx|binductionOn|ibelow|mk)(_\d+)?$',p) for p in n.split('.')[1:]) and not n in parsed
parsed={d['name'] for d in inv['decls']}
memo={}
def closure(n, transitive, stack=()):
    """periphery constants reached from n's type and value, expanding bridge auxiliaries (and, if transitive, all bridge decls)"""
    key=(n,transitive)
    if key in memo: return memo[key]
    if n in stack: return set()
    memo[key]=set()
    out=set(); d=info.get(n)
    if d is None: return out
    for c in d['type']+d['value']:
        L=lay(c)
        if L=='periphery': out.add(c)
        elif L=='bridge' and c!=n and (transitive or c not in parsed):
            out|=closure(c,transitive,stack+(n,))
    memo[key]=out; return out
def typeper(n):
    d=info[n]; out=set()
    for c in d['type']:
        if lay(c)=='periphery': out.add(c)
        elif lay(c)=='bridge' and c!=n: out|=closure(c,True)  # type mentions a bridge def: count what that def reaches
    return out
missing=[d['name'] for d in inv['decls'] if d['name'] not in info]
print('unmatched',len(missing),missing[:20])
res={}
for d in inv['decls']:
    n=d['name']
    if n not in info: continue
    direct=closure(n,False); trans=closure(n,True); tp=typeper(n)
    core_used=sorted({c for c in info[n]['type']+info[n]['value'] if lay(c)=='core'})
    res[n]={'module':d['module'],'kind':d['kind'],'line':d['line'],'trivial':d['trivial'],'proof_len':d['proof_len'],
            'type_periphery':sorted(tp),'direct_periphery':sorted(direct),'trans_periphery':sorted(trans),
            'periphery_modules':sorted({mods.get(c,'?') for c in trans}),'core_used':core_used}
json.dump(res,open('meta-res.json','w'),indent=1)
c=collections.Counter()
for n,r in res.items():
    c[(r['kind'] in('theorem','lemma'), 'no-periphery' if not r['trans_periphery'] else ('type' if r['type_periphery'] else 'proof-only'))]+=1
print(c)
