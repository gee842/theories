import re, itertools, sys
src = open(sys.argv[1], encoding='utf-8').read()
i = src.index('def order : List Hexagram := [')
block = src[i:src.index(']', src.index('64 未濟', i))]
rows = re.findall(r'⟨(\w+), (\w+), (\w+), (\w+), (\w+), (\w+)⟩,?\s*--\s*(\d+) (\S+):', block)
order = [tuple(v == 'true' for v in r[:6]) for r in rows]
names = [r[7] for r in rows]
assert len(order) == 64
# elementary CA rules with cyclic / twisted boundary
def ca(rule, s, twist):
    n = len(s)
    out = []
    for k in range(n):
        l = s[k-1] if k > 0 else (not s[n-1] if twist else s[n-1])
        r = s[k+1] if k < n-1 else (not s[0] if twist else s[0])
        idx = (l << 2) | (s[k] << 1) | r
        out.append(bool((rule >> idx) & 1))
    return tuple(out)
hits = []
for twist in (False, True):
    for rule in range(256):
        if all(ca(rule, order[i], twist) == order[i+1] for i in range(63)):
            hits.append((rule, twist))
print('CA hits', hits)
# best CA: max number of consecutive steps matched
best = 0
for twist in (False, True):
    for rule in range(256):
        m = sum(ca(rule, order[i], twist) == order[i+1] for i in range(63))
        best = max(best, m)
print('best CA matches of 63 steps', best)
# affine maps: permutation + xor mask
best = (0, None)
cnt = 0
for perm in itertools.permutations(range(6)):
    for mask in range(64):
        m = 0
        for i in range(63):
            s = order[i]
            t = tuple(s[perm[k]] ^ bool((mask >> k) & 1) for k in range(6))
            m += (t == order[i+1])
        if m > best[0]:
            best = (m, (perm, mask))
print('best affine', best)
# within-pair vs between-pair steps
rev = lambda s: tuple(reversed(s))
comp = lambda s: tuple(not v for v in s)
within = sum(1 for i in range(0, 64, 2) if order[i+1] in (rev(order[i]), comp(order[i])))
print('within pairs paired', within)
# between-pair steps: relation of order[2j+1] -> order[2j+2]
def hamming(a, b): return sum(x != y for x, y in zip(a, b))
print('between-pair hamming distances', [hamming(order[i], order[i+1]) for i in range(1, 63, 2)])
print('within-pair hamming', [hamming(order[i], order[i+1]) for i in range(0, 64, 2)])
