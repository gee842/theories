"""Replay frozen arithmetic checks without live repositories.

Default replay reads bundled provenance; it does not verify live sources or Lean.
Use --inspect-live-sources to refresh source hashes/excerpts by read-only inspection.
Neither mode imports or builds SSBX.
"""
import argparse
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
REPO = Path('/Users/ren/repos/生生不息')
THEORY = Path('/Users/ren/theories/theories/shengsheng-buxi-generative-existence/README.md')
FILES = {
    'canonical_synthesis': THEORY,
    'kernel': REPO / 'formal/SSBX/Foundation/Wen/Kernel.lean',
    'r7': REPO / 'formal/SSBX/Foundation/Atlas/Yi/Classical/Cells/R7.lean',
    'yi': REPO / 'formal/SSBX/Foundation/Atlas/Yi/Classical/Core/Yi.lean',
    'root': REPO / 'formal/SSBX/Foundation/Core/MonadRoot.lean',
    'full_gut': REPO / 'formal/SSBX/Foundation/Doctrine/FullGUT.lean',
    'root_plan': REPO / 'formal/SSBX/notes/monad-root-plan.md',
    'claim_ledger': REPO / 'docs-next/10_formal_形式/claim-status-ledger.md',
    'jian': REPO / '史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/03_一、间.md',
    'openness': REPO / '史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/06_四、开闭.md',
    'global_assertion': REPO / '史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/15_十三、行仁要善_alignment_之真义.md',
}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--inspect-live-sources', action='store_true',
                    help='Refresh provenance/excerpts from the original source paths, read-only.')
args = parser.parse_args()
if args.inspect_live_sources:
    manifest = {
        name: {'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        for name, path in FILES.items()
    }
else:
    manifest = json.loads((HERE / 'source-manifest.json').read_text())

# Kernel.lean:152–157, R7.lean componentwise XOR, Yi.lean:65–69.
# Coordinates: (hexagram y1,...,y6, past-trace bit); yin=1, yang=0.
mask = (1, 0, 0, 0, 0, 0, 0)
def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))
def motion(a):
    return xor(a, mask)
states = list(product((0, 1), repeat=7))
orbits = []
for state in states:
    assert motion(state) != state
    assert motion(motion(state)) == state
    orbit = [state]
    for _ in range(16):
        orbit.append(motion(orbit[-1]))
    assert len(set(orbit)) == 2
    assert all(orbit[n + 2] == orbit[n] for n in range(15))
    orbits.append(orbit)

# General involution check, independent integer encoding of all 7-bit cells.
for c in range(1, 128):
    for s in range(128):
        assert (s ^ c) != s
        assert ((s ^ c) ^ c) == s

# Logical separating examples for the bare distinction/transition interface.
# Same observed eventful prefix, terminal versus indefinitely extending model.
prefix_pairs = []
for horizon in range(1, 51):
    continuing_prefix = list(range(horizon + 1))
    stopping_prefix = list(range(horizon + 1))
    assert continuing_prefix == stopping_prefix
    continuing_successors = [horizon + 1]
    stopping_successors = []
    assert continuing_successors and not stopping_successors
    prefix_pairs.append({'horizon': horizon, 'same_observed_prefix': True,
                         'continuing_next': continuing_successors,
                         'stopping_next': stopping_successors})

result = {
    'scope': 'Independent arithmetic check of inspected definitions; not a Lean rebuild or empirical test.',
    'source_mask_coordinate_order': '(y1,y2,y3,y4,y5,y6,past_trace)',
    'source_mask': mask,
    'source_states_checked': len(states),
    'source_orbit_distinct_states': 2,
    'source_orbit_exact_period': 2,
    'source_orbit_pairs': len({frozenset(orbit) for orbit in orbits}),
    'all_nonzero_masks_checked': 127,
    'state_mask_pairs_checked': 127 * 128,
    'origin_first_nine_states': orbits[0][:9],
    'prefix_pairs_checked': len(prefix_pairs),
    'prefix_example': prefix_pairs[-1],
    'all_checks_passed': True,
    'sources': manifest,
}
(HERE / 'root-scope-checks.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
if args.inspect_live_sources:
    (HERE / 'source-manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')

EXCERPTS = {
    'kernel': [(143, 175), (206, 242), (264, 335)],
    'r7': [(258, 306)],
    'yi': [(61, 69)],
    'root': [(1119, 1136), (1259, 1292)],
    'full_gut': [(53, 88), (1082, 1087), (1560, 1578), (1631, 1639), (2481, 2505)],
    'root_plan': [(34, 38)],
    'jian': [(1, 25)],
    'openness': [(3, 11), (19, 26), (34, 38)],
    'global_assertion': [(28, 46)],
    'canonical_synthesis': [(303, 315)],
}
if args.inspect_live_sources:
    parts = ['# Source excerpts for the root scope audit\n',
             'Read-only inspection on 2026-10-05. Full-file SHA-256 values are in source-manifest.json.\n']
    for name, ranges in EXCERPTS.items():
        path = FILES[name]
        lines = path.read_text().splitlines()
        parts += [f'\n## {name}\n\n`{path}`\n']
        for start, end in ranges:
            parts += [f'\nLines {start}–{end}:\n\n```text\n']
            parts += [f'{n}: {lines[n - 1]}\n' for n in range(start, min(end, len(lines)) + 1)]
            parts += ['```\n']
    (HERE / 'axiom-source-excerpts.md').write_text(''.join(parts))
print(json.dumps({k: v for k, v in result.items() if k not in ('sources', 'origin_first_nine_states')}, indent=2))
