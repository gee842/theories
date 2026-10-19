import re,glob,os,collections,json,sys
root='/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
mods={}
for p in sorted(glob.glob(root+'/Becoming/*.lean')):
    name='Becoming.'+os.path.basename(p)[:-5]
    src=open(p).read()
    imps=re.findall(r'^import\s+(\S+)',src,re.M)
    mods[name]={'imports':imps,'lines':src.count('\n')}
print('modules',len(mods))
imported_by=collections.defaultdict(set)
for m,v in mods.items():
    for i in v['imports']: imported_by[i].add(m)
leaves=[m for m in mods if not imported_by[m]]
print('leaves (imported by no Becoming module):',len(leaves))
roots=[m for m in mods if not any(i.startswith('Becoming.') for i in mods[m]['imports'])]
print('roots (import no Becoming module):',[(m,mods[m]['imports']) for m in roots])
ext=collections.Counter(i for v in mods.values() for i in v['imports'] if not i.startswith('Becoming.'))
print('external imports',ext)
# longest chain
memo={}
def depth(m):
    if m in memo: return memo[m]
    best=(1,[m])
    for i in mods.get(m,{}).get('imports',[]):
        if i in mods:
            d,ch=depth(i)
            if d+1>best[0]: best=(d+1,[m]+ch)
    memo[m]=best; return best
sys.setrecursionlimit(10000)
L=max((depth(m) for m in mods),key=lambda x:x[0])
print('longest chain',L[0]); print(' <- '.join(L[1]))
print('most imported',sorted(((len(v),k) for k,v in imported_by.items()),reverse=True)[:25])
# transitive closure: how many modules reach World, Frame, GenerativeCore
closure={}
def clo(m):
    if m in closure: return closure[m]
    s=set()
    for i in mods.get(m,{}).get('imports',[]):
        s.add(i); s|=clo(i) if i in mods else set()
    closure[m]=s; return s
for m in mods: clo(m)
for b in ['Becoming.World','Becoming.Frame','GenerativeCore','RelationalRenewal','InquirySufficiency','Becoming.Labelled','Becoming.Unfolding','Becoming.Runs','Becoming.Naturals','Becoming.Integers','Becoming.IntegerOrder','Becoming.ListTests','Becoming.Dependence','Becoming.Flow','Becoming.Generation','Becoming.Recurrence']:
    print(b,'reached by',sum(1 for m in mods if b in closure[m]), 'direct',len(imported_by[b]))
noWorld=[m for m in mods if 'Becoming.World' not in closure[m] and m!='Becoming.World']
noFrame=[m for m in mods if 'GenerativeCore' not in closure[m]]
print('modules not reaching World:',len(noWorld),noWorld)
print('modules not reaching GenerativeCore:',len(noFrame))
json.dump({'mods':mods,'leaves':leaves},open(os.path.dirname(__file__)+'/imports.json','w'),indent=0)
leafl=sorted(leaves)
print('leaves list:',leafl)
