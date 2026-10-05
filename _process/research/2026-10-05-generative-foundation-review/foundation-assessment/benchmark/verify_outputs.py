"""Independent standard-library recalculation from saved prediction tables."""
from pathlib import Path
import csv
import hashlib
import itertools
import json
import math

ROOT = Path(__file__).resolve().parent


def require(condition, name, checks):
    checks.append(dict(name=name, passed=bool(condition)))
    if not condition:
        raise AssertionError(name)


def main():
    result = json.loads((ROOT/'analysis.json').read_text())
    rows = list(csv.DictReader((ROOT/'predictions.csv').open()))
    source_rows = list(csv.DictReader((ROOT/'paired_source_errors.csv').open()))
    checks = []
    require(len(rows) == 24, '24 held-out predictions', checks)
    require(len({r['row_index'] for r in rows}) == 24, 'unique held-out row indices', checks)
    require({float(r['cycle']) for r in rows} == {5.}, 'all predictions use current cycle 5', checks)
    require(len({r['source'] for r in rows}) == 4, 'four source blocks', checks)
    for source in {r['source'] for r in rows}:
        require(sum(r['source'] == source for r in rows) == 6, f'six conditions: {source}', checks)
    for name, expected in result['metrics'].items():
        errors = [float(r['next_od'])-float(r[name]) for r in rows]
        calculated = dict(rmse=math.sqrt(sum(e*e for e in errors)/len(errors)),
                          mae=sum(abs(e) for e in errors)/len(errors))
        require(all(abs(calculated[k]-expected[k]) < 1e-12 for k in calculated), f'CSV-derived metrics: {name}', checks)
    for fold in result['folds']:
        source = fold['held_out_source']
        require(len(fold['train_indices']) == 36 and len(fold['test_indices']) == 6, f'outer fold counts: {source}', checks)
        require(not set(fold['train_indices']) & set(fold['test_indices']), f'outer index disjointness: {source}', checks)
        for label, lib in fold['libraries'].items():
            require(len(lib['validation']) == 18, f'equal 18-candidate budget: {source}/{label}', checks)
            for choice, index in lib['selected_indices'].items():
                family = None if choice == 'selected' else choice.split('_')[0]
                eligible = [v['mse'] for v in lib['validation'] if family is None or v['candidate']['family'] == family]
                require(lib['validation'][index]['mse'] <= min(eligible)+1e-12, f'inner-only optimum: {source}/{label}/{choice}', checks)
            require(lib['selected_candidates']['selected']['family'] == 'persistence', f'selected persistence: {source}/{label}', checks)
    require(all(float(r['baseline_selected']) == float(r['augmented_selected']) == float(r['current_od']) for r in rows),
            'identical selected predictors equal current biomass', checks)
    require(not result['primary_expectation_met'], 'primary improvement expectation not met', checks)
    require(all(float(r['mse_gain']) == float(r['mae_gain']) == 0 for r in source_rows), 'all paired source gains zero', checks)
    require(result['bootstrap_replicates'] == len(list(itertools.product(range(4), repeat=4))), '256 source-block resamples', checks)
    for field, path in [('protocol_sha256', ROOT/'PROTOCOL.md'), ('code_sha256', ROOT/'analyze.py'),
                        ('source_sha256', Path(result['source_path']))]:
        require(hashlib.sha256(path.read_bytes()).hexdigest() == result[field], f'hash: {field}', checks)
    summary = dict(all_passed=True, n_checks=len(checks), scope='Independent saved-output arithmetic and selection bookkeeping; not independent model implementation or empirical replication.', checks=checks)
    (ROOT/'VERIFICATION.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps({k: v for k, v in summary.items() if k != 'checks'}, indent=2))


if __name__ == '__main__':
    main()
