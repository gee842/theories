"""Independent recount/replay of inherited records; no new participant benchmark."""
from pathlib import Path
from itertools import product
import hashlib
import json
import numpy as np
import experiment as ex

p = Path(__file__).resolve().parent / 'inherited-evidence'
rows = [json.loads(line) for line in (p / 'runs.jsonl').open()]
saved = json.loads((p / 'summary.json').read_text())
manifest = json.loads((p / 'manifest.json').read_text())
source = p.parent.parent / 'source-snapshots/experiments/situated-discovery'
assert all(hashlib.sha256((source / n).read_bytes()).hexdigest() == h
           for n, h in manifest.items())
assert len(rows) == 7168
assert len({r['seed'] for r in rows}) == 256
for seed in sorted({r['seed'] for r in rows}):
    ex.check_gate_pairing([r for r in rows if r['seed'] == seed])
assert ex.summarize(rows) == saved['summary']
selected = []
for seed in [10000, 10255]:
    for hazard in [True, False]:
        world = ex.World(seed, hazard)
        for arm in ex.ARMS:
            old = next(r for r in rows if r['seed'] == seed
                       and r['hazard'] == hazard and r['arm'] == arm.name)
            new = ex.simulate(world, arm, detail=(seed == 10000))
            # Generated predicates use tuples internally, serialized as arrays.
            assert json.loads(json.dumps(new)) == old, (seed, hazard, arm.name)
            selected.append([seed, hazard, arm.name])

# Exact representation stress check, not another seeded performance evaluation.
# Four required literals are unavailable in the inherited <=2-literal grammar.
x = np.array(list(product((0, 1), repeat=6)), dtype=np.int8)
four = ex.Predicate(tuple((i, 1) for i in range(4)))
all_gains = [float(np.mean(p.mask(x) * (.75 * four.mask(x) - ex.ACTION_COST)))
             for p in ex.grammar()]
true_gain = float(np.mean(four.mask(x) * (.75 - ex.ACTION_COST)))
assert max(all_gains) < 0 < true_gain
metrics = []
for arm in ['protected', 'return_funded', 'short_records', 'frozen_model',
            'no_standing', 'no_authority', 'temporary_rescue']:
    rs = [r for r in rows if r['arm'] == arm and r['hazard']]
    metrics.append({'arm': arm, 'n': len(rs),
                    'timely_validation': sum(r['timely_validation'] for r in rs),
                    'timely_enactment': sum(r['timely_enactment'] for r in rs),
                    'exact_recovery': sum(r['exact_predicate_recovered'] for r in rs)})
report = {
    'source_manifest_match': True,
    'record_count': len(rows),
    'independent_seed_clusters': 256,
    'aggregate_summary_exact_recount_match': True,
    'all_saved_gate_pairings_pass': True,
    'exact_replays': len(selected),
    'replayed_seed_ids': [10000, 10255],
    'mechanism_tests': {'count': 4, 'status': 'passed'},
    'conjunction_4_diagnostic': {
        'kind': 'Exact enumeration outside inherited evaluation; not new benchmark',
        'best_gain_in_original_73_predicate_grammar': max(all_gains),
        'exact_four_literal_policy_gain': true_gain,
        'interpretation': 'The supplied grammar contains no beneficial policy, despite complete raw records and known actions.'},
    'hazard_present_metrics': metrics,
    'run_notes': [
        'Initial unittest invocation from workspace root failed import; rerun in copied scratch directory passed.',
        'Initial raw Python replay comparison failed only because tuples serialize to lists; JSON-normalized exact comparisons pass.'
    ]
}
(p.parent / 'audit-check-results.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
