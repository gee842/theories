"""Four original carriers, all subsequent descendants, unchanged typed chemistry.

Skeleton=(four conserved material slots, directed G/Y bonds, permanent wear mask).
Only already-worn slots are permuted. Rates are affine polynomials a+b*free_F.
This implementation is independent of the count-law producer.
"""
from collections import defaultdict, deque
from functools import lru_cache
from itertools import permutations

R,C,Q,Y,D,A0,A1,G0,G1,B0,B1=range(11)
NAMES=('R','C','CF','Y','D','A0','A1','G0','G1','GF0','GF1')
FUNCTIONAL={C,Q,Y,A0,A1,G0,G1,B0,B1}

@lru_cache(None)
def canonical(roles,bonds,mask):
    lost=[i for i in range(4) if mask>>i&1]
    best=None
    for order in permutations(lost):
        mp=dict(zip(lost,order)); nr=list(roles)
        for a,b in mp.items():nr[b]=roles[a]
        nb=tuple(sorted((mp.get(g,g),mp.get(y,y)) for g,y in bonds))
        candidate=(tuple(nr),nb,mask)
        if best is None or candidate<best:best=candidate
    return best

def entry(i,j):return ((A0+i,Q,G0+j,Y),((2,3),),0)

def count(s,f):
    roles,bonds,mask=s; out={name:roles.count(i) for i,name in enumerate(NAMES)};out['F']=f
    for g,y in bonds:
        name='G'+str(roles[g]-G0);out[name]-=1;out['Y']-=1
        name='YG'+str(roles[g]-G0);out[name]=out.get(name,0)+1
    return out

def valid(s):
    roles,bonds,mask=s
    used=[]
    for g,y in bonds:
        assert roles[g] in (G0,G1) and roles[y]==Y and g!=y
        used.extend((g,y))
    assert len(used)==len(set(used))
    # A live original cannot change functional family before its wear.
    for i,allowed in enumerate(({A0,A1},{C,Q},{G0,G1,B0,B1},{Y})):
        if not mask>>i&1:assert roles[i] in allowed
    return True

def extinct(s):return Y not in s[0]
def empty_availability(s):return not any(k in s[0] for k in (R,C,Q,B0,B1))
def organization(s):
    roles,bonds,mask=s
    if len(bonds)==1 and roles.count(Q)==1 and sum(roles.count(a) for a in (A0,A1))==1:
        g,y=bonds[0];return (next(a-A0 for a in roles if a in (A0,A1)),roles[g]-G0)
    return None

def events(s):
    roles,bonds,mask=s;occupied={i for p in bonds for i in p};out=defaultdict(lambda:[0,0])
    ix=lambda choices:[i for i,r in enumerate(roles) if r in choices]
    rr=ix({R});dd=ix({D});cc=ix({C});qq=ix({Q});aa=ix({A0,A1})
    yy=[i for i in ix({Y}) if i not in occupied];gg=[i for i in ix({G0,G1}) if i not in occupied]
    def add(name,a=1,b=0,changes=(),df=0,wear=None,new_bonds=None):
        nr=list(roles)
        for i,r in changes:nr[i]=r
        nm=mask if wear is None else mask|(1<<wear)
        nb=bonds if new_bonds is None else tuple(sorted(new_bonds))
        target=canonical(tuple(nr),nb,nm);valid(target)
        k=(name,target,df);out[k][0]+=a;out[k][1]+=b
    # Unit constituent wear; a complex contributes separate G and Y wear clocks.
    for i,r in enumerate(roles):
        if r not in FUNCTIONAL:continue
        if i in occupied:
            g,y=next(p for p in bonds if i in p);name=f'YG{roles[g]-G0}_'+('G_wear' if i==g else 'Y_wear')
        else:name=NAMES[r]+'_wear'
        add(name,changes=((i,D),),df=int(r in (Q,B0,B1)),wear=i,new_bonds=[p for p in bonds if i not in p])
    add('free_leak',a=0,b=1,df=-1)
    for i,r in enumerate(roles):
        if r==Q:add('CF_leak',changes=((i,C),))
        if r in (B0,B1):add(f'GF{r-B0}_leak',changes=((i,G0+r-B0),))
    for c in cc:add('capture',changes=((c,Q),))
    for r in rr:
        add('assembly',changes=((r,C),))
        for y in yy:add('free_Y_reproduction',changes=((r,Y),))
        for g,y in bonds:
            if roles[g]==G1:add('bound_Y_reproduction',changes=((r,Y),))
        for i in (0,1):
            add(f'A{i}_formation',a=0,b=1,changes=((r,A0+i),),df=-1)
            for c in qq:add(f'A{i}_paid_formation',changes=((r,A0+i),(c,C)))
        for a in aa:
            i=roles[a]-A0
            add(f'A{i}_copying',a=0,b=1,changes=((r,A0+i),),df=-1)
            add(f'G{i}_fabrication',a=0,b=1,changes=((r,G0+i),),df=-1)
            for c in qq:add(f'G{i}_paid_fabrication',changes=((r,G0+i),(c,C)))
    for d in dd:
        for c in cc:add('C_recycling',a=0,b=1,changes=((d,R),),df=-1)
        for y in yy:add('Y_recycling',a=0,b=1,changes=((d,R),),df=-1)
        for c in qq:add('paid_recycling',changes=((d,R),(c,C)))
    for g in gg:
        i=roles[g]-G0
        add(f'G{i}_F_binding',a=0,b=1,changes=((g,B0+i),),df=-1)
        for y in yy:add(f'G{i}_Y_binding',new_bonds=bonds+((g,y),))
    for k,r in enumerate(roles):
        if r in (B0,B1):add(f'GF{r-B0}_dissociation',changes=((k,G0+r-B0),),df=1)
    for g,y in bonds:add(f'YG{roles[g]-G0}_dissociation',new_bonds=[p for p in bonds if p!=(g,y)])
    return [(name,target,df,a,b) for (name,target,df),(a,b) in out.items()]

def graph_skeletons():
    states=[entry(i,j) for i in (0,1) for j in (0,1)];index={x:i for i,x in enumerate(states)};queue=deque(states);rows=[]
    while queue:
        x=queue.popleft();edges=[]
        if x[2]==15 and organization(x) is not None:
            rows.append([]);continue
        for name,y,df,a,b in events(x):
            if extinct(y):d=-1
            else:
                if y not in index:index[y]=len(states);states.append(y);queue.append(y)
                d=index[y]
            edges.append((name,d,df,a,b))
        rows.append(edges)
    return states,rows

if __name__=='__main__':
    s,r=graph_skeletons();print({'skeletons':len(s),'edges':sum(map(len,r)),'mask_counts':{m:sum(x[2]==m for x in s) for m in range(16)},'cache':str(canonical.cache_info())})
