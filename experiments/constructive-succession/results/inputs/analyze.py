"""Run the declared exploratory grid and retain auditable records."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import hashlib
import json
import platform
import shutil
import statistics
import time

from model import run

HERE = Path(__file__).resolve().parent
OUT = HERE / 'results'
POLICIES = ('solution', 'closest', 'diverse', 'recent', 'diverse_recompute')


def main():
    OUT.mkdir(exist_ok=False)
    snapshots = OUT / 'inputs'
    snapshots.mkdir()
    hashes = {}
    for name in ('model.py', 'test_model.py', 'analyze.py', 'PROTOCOL.md'):
        shutil.copyfile(HERE / name, snapshots / name)
        hashes[name] = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
    groups = defaultdict(list)
    start = time.monotonic()
    runs = 0
    with (OUT / 'runs.jsonl').open('w') as stream:
        for regime, policy, price, flow, reserve in product(
                ('repeat', 'local', 'independent'), POLICIES, (0, 2, 16), (300, 1200), (0, 1)):
            seeds = range(1 if regime == 'repeat' else 64)
            for seed in seeds:
                r = run(seed, regime, policy, price, flow, reserve_quarters=reserve)
                r.pop('final_package')
                stream.write(json.dumps(r, separators=(',', ':')) + '\n')
                groups[(regime, policy, price, flow, reserve)].append(r)
                runs += 1
            if runs % 500 < 64:
                print(f'{runs} paired runs completed', flush=True)
    summary = []
    for key, records in groups.items():
        regime, policy, price, flow, reserve = key
        eps = [e for r in records for e in r['episodes']]
        counts = [sum(e['solved'] for e in r['episodes']) for r in records]
        recovery = sum(any(not r['episodes'][j]['solved'] and
                           any(e['solved'] for e in r['episodes'][j+1:])
                           for j in range(3)) for r in records)
        base = groups[(regime, 'solution', price, flow, reserve)]
        differences = [c - sum(e['solved'] for e in b['episodes']) for c, b in zip(counts, base)]
        summary.append({
            'regime': regime, 'policy': policy, 'archive_price': price,
            'flow': flow, 'reserve_quarters': reserve, 'seed_clusters': len(records),
            'successes': sum(counts), 'episodes': len(eps),
            'success_rate': sum(counts)/len(eps),
            'all_four': sum(c == 4 for c in counts),
            'new_compositions': sum(e['new_composition'] for e in eps),
            'direct_reuses': sum(e['solved'] and not e['new_composition'] for e in eps),
            'inherited_exact_matches': sum(e['inherited_target'] for e in eps),
            'successes_when_not_inherited': sum(e['solved'] and not e['inherited_target'] for e in eps),
            'episodes_without_inherited_match': sum(not e['inherited_target'] for e in eps),
            'lineages_recovering_after_failure': recovery,
            'mean_final_bank': statistics.mean(r['final_bank'] for r in records),
            'mean_paid_work': statistics.mean(1000 + 4*flow - r['final_bank'] for r in records),
            'mean_delivered_extra_nodes': statistics.mean(e['extra_nodes'] for e in eps),
            'paired_success_difference_per_lineage': statistics.mean(differences),
            'paired_difference_standard_error': (statistics.stdev(differences)/len(differences)**0.5
                                                if len(differences) > 1 else None),
        })
    result = {'status': 'complete', 'scope': 'exploratory finite computational model',
              'runs': runs, 'successor_episodes': runs*4, 'groups': summary,
              'source_sha256': hashes, 'python': platform.python_version(),
              'seconds': time.monotonic()-start}
    (OUT / 'summary.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'groups'}, indent=2))


if __name__ == '__main__':
    main()
