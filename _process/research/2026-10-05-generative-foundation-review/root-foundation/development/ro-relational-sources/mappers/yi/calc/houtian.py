import itertools
# bottom-up lines, 1 = unbroken
T = {'乾':(1,1,1),'兌':(1,1,0),'離':(1,0,1),'震':(1,0,0),'巽':(0,1,1),'坎':(0,1,0),'艮':(0,0,1),'坤':(0,0,0)}
cyc = ['震','巽','離','坤','兌','乾','坎','艮']   # 帝出乎震 ... 成言乎艮 (說卦 ch5)
seq = [T[n] for n in cyc]
def comp(s): return tuple(1-x for x in s)
# affine: permutation of places + xor mask
best=0; hits=[]
for p in itertools.permutations(range(3)):
    for m in itertools.product((0,1),repeat=3):
        f=lambda s:tuple(s[p[i]]^m[i] for i in range(3))
        k=sum(f(seq[i])==seq[(i+1)%8] for i in range(8))
        best=max(best,k)
        if k==8: hits.append((p,m))
print('affine hits', hits, 'best of 8', best)
# local rules (3-cell neighbourhood, cyclic and twisted)
def ca(rule,s,tw):
    n=3; out=[]
    for k in range(n):
        l=s[k-1] if k>0 else ((1-s[n-1]) if tw else s[n-1])
        r=s[k+1] if k<n-1 else ((1-s[0]) if tw else s[0])
        out.append((rule>>((l<<2)|(s[k]<<1)|r))&1)
    return tuple(out)
cab=0; cah=[]
for tw in (0,1):
    for rule in range(256):
        k=sum(ca(rule,seq[i],tw)==seq[(i+1)%8] for i in range(8))
        cab=max(cab,k)
        if k==8: cah.append((rule,tw))
print('local hits', cah, 'best of 8', cab)
# opposite positions on the circle
for i in range(4):
    a,b=cyc[i],cyc[i+4]
    print('opposite',a,b,'complement' if comp(T[a])==T[b] else '-')
# xian-tian (說卦 ch3 pairs) check
for a,b in [('乾','坤'),('艮','兌'),('震','巽'),('坎','離')]:
    print('ch3 pair',a,b,comp(T[a])==T[b])
# parity of yang count: 陽卦 乾震坎艮 odd, 陰卦 坤巽離兌 even
for n,s in T.items(): print(n, sum(s), 'odd' if sum(s)%2 else 'even', 'strokes', sum(s)+2*(3-sum(s)))
