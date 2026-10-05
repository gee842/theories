"""Exact rational checks of the five-cycle conditional law-selection theorem."""
from fractions import Fraction as F
from pathlib import Path
import json

N = 5
V = N * N

def row(terms):
    out = [F(0)] * V
    for i, j, value in terms:
        out[(i % N) * N + j % N] += F(value)
    return out

constraints = {
    "locality": [row([(i, j, 1)]) for i in range(N) for j in range(N)
                 if (j-i) % N not in (0, 1, N-1)],
    "translation": [row([(i, j, 1), (i+1, j+1, -1)])
                    for i in range(N) for j in range(N)],
    "reflection": [row([(i, j, 1), (-i, -j, -1)])
                   for i in range(N) for j in range(N)],
    "conservation": [row([(i, j, 1) for i in range(N)]) for j in range(N)],
}

def rref(rows):
    a = [list(r) for r in rows]
    pivot_cols = []
    r = 0
    for col in range(V):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][col]
        a[r] = [v / divisor for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                factor = a[i][col]
                a[i] = [x-factor*y for x,y in zip(a[i], a[r])]
        pivot_cols.append(col)
        r += 1
        if r == len(a):
            break
    free = [c for c in range(V) if c not in pivot_cols]
    basis = []
    for c in free:
        v = [F(0)] * V
        v[c] = F(1)
        for i,p in enumerate(pivot_cols):
            v[p] = -a[i][c]
        basis.append(v)
    return pivot_cols, basis

L = [[F(-2 if i == j else 1 if (j-i) % N in (1,N-1) else 0)
      for j in range(N)] for i in range(N)]
flatL = sum(L, [])
allrows = sum(constraints.values(), [])
pivots, basis = rref(allrows)
assert len(basis) == 1
scale = basis[0][1]
assert scale != 0 and [v / scale for v in basis[0]] == flatL


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]

def transpose(a):
    return [list(r) for r in zip(*a)]

I = [[F(i == j) for j in range(N)] for i in range(N)]
B = [row([(i,i,-1),(i,i+1,1)])[i*N:(i+1)*N] for i in range(N)]
BtB = mm(transpose(B), B)
assert all(L[i][j] == -BtB[i][j] for i in range(N) for j in range(N))
# Faddeev-LeVerrier computes characteristic coefficients exactly.
C = I
char = [F(1)]
for k in range(1,N+1):
    LC = mm(L, C)
    c = -sum(LC[i][i] for i in range(N))/k
    char.append(c)
    C = [[LC[i][j]+c*I[i][j] for j in range(N)] for i in range(N)]
assert char == [1,10,35,50,25,0]  # lambda*(lambda^2+5lambda+5)^2
assert all(v == 0 for r in C for v in r)


def shift(step):
    return [[F(j == (i-step)%N) for j in range(N)] for i in range(N)]

def add(*terms):
    return [[sum(scale*m[i][j] for scale,m in terms) for j in range(N)]
            for i in range(N)]

def check(m):
    v = sum(m, [])
    flags = {name: all(sum(x*y for x,y in zip(c,v)) == 0 for c in rows)
             for name,rows in constraints.items()}
    flags["positivity_generator"] = all(m[i][j] >= 0 for i in range(N)
                                          for j in range(N) if i != j)
    return flags

weighted = [[F(0)]*N for _ in range(N)]
for i,w in enumerate([1,2,3,2,1]):
    j=(i+1)%N
    weighted[i][j]+=w; weighted[j][i]+=w
    weighted[i][i]-=w; weighted[j][j]-=w

witnesses = {
    "reflection": add((1,shift(1)),(-1,I)),
    "locality": add((1,shift(2)),(1,shift(-2)),(-2,I)),
    "conservation": add((1,L),(-1,I)),
    "positivity_generator": add((-1,L)),
    "translation": weighted,
}
witness_results = {}
for removed,mat in witnesses.items():
    flags=check(mat)
    assert not flags[removed]
    assert all(value for key,value in flags.items() if key != removed)
    witness_results[removed] = {"matrix":mat,"properties":flags}

# A negative D immediately makes a neighbor component negative from delta data.
negative = [[-v for v in r] for r in L]
assert negative[1][0] < 0

result = {
    "status":"all exact assertions passed",
    "arithmetic":"Python fractions.Fraction; no floating point",
    "sites":N,
    "matrix_unknowns":V,
    "constraint_rows":{k:len(v) for k,v in constraints.items()},
    "linear_constraint_rank":len(pivots),
    "linear_solution_dimension":len(basis),
    "normalized_generator":L,
    "positivity":"D>=0 iff exp(t*D*L) preserves nonnegativity for t>=0; necessity verified by delta-state derivative, sufficiency proved by nonnegative exponential series",
    "energy_identity":"L = -B^T B exactly; d(1/2 sum_i(p_i-mean)^2)/dt = -D sum_i(p_{i+1}-p_i)^2",
    "characteristic_coefficients_descending":char,
    "factorization":"lambda*(lambda^2+5*lambda+5)^2",
    "eigenvalues":"0 (multiplicity 1); (-5+sqrt(5))/2 and (-5-sqrt(5))/2 (each multiplicity 2), multiplied by D",
    "consequence":"For D>0 every conserved-density trajectory converges exponentially to its uniform density; D=0 stays fixed",
    "one_requirement_removed_witnesses":witness_results,
    "linear_dimensions_on_removal":{name:len(rref(sum([v for k,v in constraints.items() if k != name],[]))[1]) for name in constraints},
    "scope":"Finite five-cycle verification supports this implementation. The general N>=5 statement rests on the proof in critical-audit.md; no empirical or universal-physics validation is claimed."
}

def encode(o):
    if isinstance(o,F):
        return int(o) if o.denominator == 1 else str(o)
    raise TypeError(type(o).__name__)
output=Path(__file__).with_name("diffusion-checks.json")
output.write_text(json.dumps(result,default=encode,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["status","linear_constraint_rank","linear_solution_dimension","linear_dimensions_on_removal"]}))
