"""Independent nine-state retention arithmetic review; no simulation or fitting."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

JUMPS = ((1, 2, 4), (0, 3, 5), (0, 3), (1, 2), (5,),
         (4, 6, 8), (5,), (2, 8), (3, 7))
KILL = (3, 3, 4, 4, 4, 4, 4, 3, 4)


def matrix(zeta):
    m = [[F(0) for _ in range(9)] for _ in range(9)]
    for i, successors in enumerate(JUMPS):
        m[i][i] = F(len(successors) + KILL[i] + (zeta if i == 7 else 0))
        for j in successors:
            m[i][j] -= 1
    return m


def solve(m, r):
    a = [row[:] + [F(r[i])] for i, row in enumerate(m)]
    for k in range(9):
        pivot = next(i for i in range(k, 9) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        scale = a[k][k]
        a[k] = [v / scale for v in a[k]]
        for i in range(9):
            if i != k:
                scale = a[i][k]
                a[i] = [v - scale*w for v, w in zip(a[i], a[k])]
    return [row[-1] for row in a]


def main():
    rewards = {
        'duration': [1]*9,
        'C_or_CF_occupation': [int(i < 4) for i in range(9)],
        'fresh_captures': [int(i in (2, 3)) for i in range(9)],
        'C_reassemblies': [int(i in (7, 8)) for i in range(9)],
    }
    expected = {
        'duration': (F(332837, 1101408), F(401591, 1329312)),
        'C_or_CF_occupation': (F(11497, 45892), F(13875, 55388)),
        'fresh_captures': (F(11593, 275352), F(13987, 332328)),
        'C_reassemblies': (F(24, 11473), F(28, 13847)),
    }
    m0, m1 = matrix(0), matrix(1)
    nz = solve(m0, [int(i == 7) for i in range(9)])
    assert nz[0] == F(4, 11473) and nz[7] == F(2374, 11473)
    results = {}
    for name, r in rewards.items():
        v0, v1 = solve(m0, r), solve(m1, r)
        assert (v0[0], v1[0]) == expected[name]
        for i in range(9):
            assert v0[i] >= v1[i] >= 0
            assert v0[i] - v1[i] == nz[i]*v0[7]/(1+nz[7])
            for m, v in ((m0, v0), (m1, v1)):
                assert sum(m[i][j]*v[j] for j in range(9)) == r[i]
        assert v0[0] > v1[0]
        results[name] = {'blocking': str(v0[0]), 'nonblocking': str(v1[0]),
                         'absolute_gain': str(v0[0]-v1[0])}
    assert solve(m0, rewards['duration'])[0] <= F(1, 3)
    assert solve(m0, rewards['C_reassemblies'])[0] <= F(1, 3)
    here = Path(__file__).resolve().parent
    source = here.parents[2]/'_process/research/2026-10-05-support-and-shared-generativity/completion/USEFUL-RETENTION-MECHANISM.md'
    result = {'status': 'passed', 'scope': 'Independent exact solution of the published nine-state table and rank-one formula; chemistry reviewed analytically, not empirically identified',
              'results': results, 'rank_one_identity_states_checked': 9,
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (here/'exact-check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
