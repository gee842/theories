"""Only declared development seeds; never invokes the held-out seed rule."""
from pathlib import Path
import hashlib
import json
import integrated_model as m

def main():
    rows = []
    for seed in m.DEVELOPMENT_SEEDS:
        for scenario in m.SCENARIOS:
            for arm in m.ARMS:
                r = m.run(seed, scenario, arm)
                rows.append({k: r[k] for k in ('scenario', 'seed', 'arm', 'final_cash',
                    'receipts', 'expenses', 'cash_identity', 'counts', 'reviews', 'rule_changes',
                    'mandate_changes', 'checker_losses', 'checker_rebuilds', 'events',
                    'paid_observations_by_stage', 'final_mandate', 'final_prefix')})
        print('completed development seed', seed)
    root = Path(__file__).parent
    result = {'seeds': m.DEVELOPMENT_SEEDS, 'scenarios': m.SCENARIOS, 'arms': m.ARMS,
              'source_sha256': hashlib.sha256(root.joinpath('integrated_model.py').read_bytes()).hexdigest(),
              'purpose_source_sha256': hashlib.sha256(root.joinpath('purpose_policy.py').read_bytes()).hexdigest(),
              'records': rows}
    root.joinpath('development-v3-all-seeds.json').write_text(json.dumps(result, indent=2) + '\n')
    for scenario in m.SCENARIOS:
        for arm in m.ARMS:
            found = [r for r in rows if r['scenario'] == scenario and r['arm'] == arm]
            print(scenario, arm, 'Berrors', [r['counts']['B']['errors'] for r in found],
                  'served', [r['counts']['B']['served'] for r in found],
                  'rules', [r['rule_changes'] for r in found],
                  'mandates', [r['mandate_changes'] for r in found],
                  'rebuilds', [r['checker_rebuilds'] for r in found])

if __name__ == '__main__':
    main()
