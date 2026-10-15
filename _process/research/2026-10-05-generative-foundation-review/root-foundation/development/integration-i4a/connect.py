"""I4a step 2: python3 -B connect.py DIR (DIR holds modules.json from inventory.py; writes DIR/connect.json).
Adds the snapshot rule, the run modules each module reaches through imports, importers and the first comment."""
import sys,json,collections,re
S=sys.argv[1].rstrip('/')+'/'
L='experiments/integrated-correction/general-framework/generative-basis/lean/'
m=json.load(open(S+'modules.json'))
# Snapshot rule: a path under a run, check, source-copy, verification or history folder, or under a folder named by a
# timestamp or a numeric run id, is a copy; a stem with no other path exists only as a snapshot.
SNAP=re.compile(r'^(\d{9,}|\d{8}T\d{6}.*|.*-runs?|runs?|.*-checks|checks|sources|.*-verification|verification|.*-history|history)$')
for o in m:
    o['live']=[p for p in o['paths'] if not any(SNAP.match(seg) for seg in p.split('/')[:-1])]
    # The canonical path: a module's own folder before a review, landing or development copy of it.
    o['live'].sort(key=lambda p: (p.startswith(('_process/', 'drafts/')) or '/development/' in p, p))
receipt=json.load(open(L+'becoming/becoming-verification.json'))
layer={mm['module']:mm.get('layer') for mm in receipt['modules']}
run_by_stem={mod.split('.')[-1]:mod for mod in receipt['source_paths']}
live={o['stem']:o for o in m if o['live']}
def first_comment(path):
    t=open(path,encoding='utf-8',errors='replace').read()
    mm=re.search(r'/-[!-]?(.*?)-/',t,re.S)
    c=mm.group(1).strip() if mm else ''
    if not c:
        lines=[l[2:].strip() for l in t.splitlines() if l.strip().startswith('--')]
        c=' '.join(lines[:6])
    return re.sub(r'\s+',' ',c)[:700]
def imps(o): return [i.split('.')[-1] for i in o['imports']]
memo={}
def to_run(stem,stack=()):
    if stem in memo: return memo[stem]
    o=live.get(stem); res=set()
    if o is None: return res
    for i,full in zip(imps(o),o['imports']):
        if full.startswith('Becoming'): res.add(full)
        elif i in run_by_stem: res.add(run_by_stem[i])
        elif i in live and i not in stack: res|=to_run(i,stack+(stem,))
    memo[stem]=res; return res
out=[]
for o in m:
    st=o['stem']
    row={'stem':st,'path':(o['live'] or o['paths'])[0],'snap':not o['live'],'theorems':o['theorems'],
         'others':[p for p in o['live'][1:]],
         'imports_outside':sorted({i for i in imps(o) if i in live and i!=st}),
         'direct_run':sorted({full if full.startswith('Becoming') else run_by_stem[i] for i,full in zip(imps(o),o['imports']) if full.startswith('Becoming') or i in run_by_stem}),
         'reach_run':sorted(to_run(st)) if o['live'] else [],
         'records':sorted({r for r,role in o['records']}),
         'mathlib':o['mathlib'],'sorry':o['sorry'],'axiom':o['axiom'],
         'doc':first_comment((o['live'] or o['paths'])[0]),'names':o['names'][:12]}
    out.append(row)
imp_by=collections.defaultdict(set)
for r in out:
    if not r['snap']:
        for i in r['imports_outside']: imp_by[i].add(r['stem'])
for r in out:
    r['importers']=sorted(imp_by.get(r['stem'],()))
    kinds={layer.get(x) for x in r['reach_run']}
    r['reach_kind']=('snapshot' if r['snap'] else 'core/bridge' if kinds & {'core','bridge'} else 'inherited' if 'inherited' in kinds
                     else 'foundation only' if kinds else 'none')
json.dump(out,open(S+'connect.json','w'),ensure_ascii=False,indent=1)
c=collections.Counter()
for r in out:
    if r['snap']: k='snapshot'
    elif r['reach_run']: k='reaches run'
    elif r['imports_outside'] or r['importers']: k='outside chain only'
    else: k='no imports either way'
    c[k]+=1
print(c)
