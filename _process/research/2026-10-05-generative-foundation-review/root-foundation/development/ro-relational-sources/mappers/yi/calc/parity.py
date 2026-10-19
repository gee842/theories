import itertools, re, sys
src = open(sys.argv[1], encoding='utf-8').read()
i = src.index('def order : List Hexagram := [')
block = src[i:src.index(']', src.index('64 未濟', i))]
rows = re.findall(r'⟨(\w+), (\w+), (\w+), (\w+), (\w+), (\w+)⟩,?\s*--\s*(\d+) (\S+):', block)
order = [tuple(v == 'true' for v in r[:6]) for r in rows]; names=[r[7] for r in rows]
H = list(itertools.product((False,True), repeat=6))
ww = lambda s: (not s[5],)+s[:5]
yang = lambda s: sum(s)
odd = lambda k: k % 2 == 0   # places p1..p6 indexed 0..5; p1 odd
phase = lambda s: sum(1 for k in range(6) if s[k] == odd(k))
assert all((yang(ww(s))+yang(s))%2==1 for s in H)
assert all((yang(s[:k]+(not s[k],)+s[k+1:])+yang(s))%2==1 for s in H for k in range(6))
assert all(phase(s)%2==(yang(s)+1)%2 for s in H)
# parity is a lumping waxWane goes alike across
assert all((yang(ww(s))%2==yang(ww(t))%2) for s in H for t in H if yang(s)%2==yang(t)%2)
# within each received pair, same parity
pairs=[(order[2*i],order[2*i+1]) for i in range(32)]
print('pairs same parity', sum(yang(a)%2==yang(b)%2 for a,b in pairs), 'of 32')
print('order steps changing parity', sum(yang(order[i])%2!=yang(order[i+1])%2 for i in range(63)), 'of 63')
opp_all=[names[j] for j,s in enumerate(order) if all(s[h]!=s[h+3] for h in range(3))]
print('opposed at all heights', opp_all)
# swap: 損 from 泰 (p3<->p6), 益 from 否 (p1<->p4)
def swap(s,i,j):
    l=list(s); l[i],l[j]=l[j],l[i]; return tuple(l)
N=dict(zip(names,order))
print('swap(泰,p3,p6)==損', swap(N['泰'],2,5)==N['損'], ' swap(否,p1,p4)==益', swap(N['否'],0,3)==N['益'])
# which hexagrams are one in-place swap (lower k <-> upper k', values differ) from 泰 / 否
for base in ('泰','否'):
    out=[]
    for i in range(3):
        for j in range(3,6):
            t=swap(N[base],i,j)
            if t!=N[base]: out.append((i+1,j+1,names[order.index(t)]))
    print(base,'one swap ->',out)
print('waxWane fixed points', [names[order.index(s)] for s in H if ww(s)==s])
