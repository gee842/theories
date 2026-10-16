"""Exploratory matched-package access intervention after the main grid.

Every arm receives exactly the same bytes and bank. Dormant extras remain
available for exact retrieval; only their automatic entry into combinatorial
search changes. Current-step construction outcomes are compared; the successor
package can subsequently differ. This is not a learned selection mechanism.
"""
from itertools import product
from pathlib import Path
import hashlib
import json
import shutil

from model import episode, primitive_state

HERE = Path(__file__).resolve().parent


def main():
    out = HERE / 'results-access'
    out.mkdir(exist_ok=False)
    snap = out / 'inputs'
    snap.mkdir()
    hashes = {}
    for name in ('model.py', 'check_access.py', 'test_model.py', 'PROTOCOL.md'):
        shutil.copyfile(HERE/name, snap/name)
        hashes[name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
    records = []
    groups = []
    for policy, flow, reserve in product(('closest', 'diverse', 'recent'),
                                        (300, 1200), (0, 1)):
        predecessor, _ = episode(primitive_state(), 102, 0, policy, 2)
        cells = []
        for target in range(256):
            pair = []
            for active in (True, False):
                _, r = episode(predecessor, target, flow, policy, 2, reserve, active)
                pair.append(r)
            assert pair[0]['opening_bank'] == pair[1]['opening_bank']
            assert pair[0]['inherited_target'] == pair[1]['inherited_target']
            cells.append(pair)
            records.append({'policy': policy, 'flow': flow, 'reserve': reserve,
                            'target': target, 'all_active': pair[0], 'extras_dormant': pair[1]})
        groups.append({'policy': policy, 'flow': flow, 'reserve_quarters': reserve,
                       'targets': 256,
                       'inherited_exact_targets': sum(p[0]['inherited_target'] for p in cells),
                       'all_active_successes': sum(p[0]['solved'] for p in cells),
                       'dormant_successes': sum(p[1]['solved'] for p in cells),
                       'all_active_new_compositions': sum(p[0]['new_composition'] for p in cells),
                       'dormant_new_compositions': sum(p[1]['new_composition'] for p in cells),
                       'active_only_successes': [i for i,p in enumerate(cells) if p[0]['solved'] and not p[1]['solved']],
                       'dormant_only_successes': [i for i,p in enumerate(cells) if p[1]['solved'] and not p[0]['solved']]})
    (out/'runs.json').write_text(json.dumps(records,indent=2)+'\n')
    (out/'summary.json').write_text(json.dumps({'scope':'exploratory matched-package one-step access intervention',
        'source_sha256':hashes,'pairs':len(records),'groups':groups},indent=2)+'\n')
    print(json.dumps(groups,indent=2))


if __name__ == '__main__':
    main()
