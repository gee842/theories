"""Frozen-seed evaluation of the bounded inquiry model; Python standard library.

Run only after sources and protocol have been frozen. This script never tunes
parameters. Its comparisons use fixed requested denominators and paired seeds.
"""
import argparse
import csv
import gzip
import hashlib
import json
import statistics
from pathlib import Path

import integrated_model as model

SEEDS = tuple(800001 + 7919 * i for i in range(64))


def distribution(values):
    return {'mean': statistics.mean(values), 'minimum': min(values),
            'maximum': max(values), 'sd': statistics.stdev(values) if len(values) > 1 else 0}


def metrics(record):
    out = {key: record[key] for key in
           ('final_cash', 'receipts', 'reviews', 'rule_changes', 'mandate_changes',
            'checker_losses', 'checker_rebuilds')}
    for group in model.GROUPS:
        c = record['counts'][group]
        assert c['requested'] == c['served'] + c['unserved']
        assert c['served'] == c['correct'] + c['errors']
        assert c['requested'] == record['config']['rounds']
        for key, value in c.items():
            out[group + '_' + key] = value
        out[group + '_failures'] = c['errors'] + c['unserved']
    out['expense_total'] = sum(record['expenses'].values())
    assert record['cash_identity']
    assert out['final_cash'] == record['initial_cash'] + out['receipts'] - out['expense_total']
    assert out['final_cash'] >= 0
    ledger = record['chronological_ledger']
    balance, credits, paid, transactions = record['initial_cash'], 0, 0, 0
    for row in ledger['rounds']:
        assert row['cash_before'] == balance
        assert row['cash_after'] == balance + row['credited'] - row['paid']
        assert row['minimum_interim_cash'] >= 0
        assert row['minimum_interim_cash'] <= min(row['cash_before'], row['cash_after'])
        balance = row['cash_after']
        credits += row['credited']
        paid += row['paid']
        transactions += row['transactions']
    assert balance == out['final_cash']
    assert credits == out['receipts'] and paid == out['expense_total']
    assert transactions == ledger['transaction_count']
    kinds = [event['kind'] for event in record['events']]
    for kind in ('review_blocked', 'review_failed_pilot', 'review_unfunded_check',
                 'fresh_check_planned', 'review_finished', 'purpose_hearing'):
        out[kind] = kinds.count(kind)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    summaries, comparisons, first_seed = [], [], []
    total = 0
    # mtime=0 makes identical reproductions byte-for-byte comparable.
    with (args.output / 'integration-all-runs.jsonl.gz').open('wb') as raw:
        with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as packed:
            for scenario in model.SCENARIOS:
                by_arm = {arm: [] for arm in model.ARMS}
                for seed in SEEDS:
                    for arm in model.ARMS:
                        record = model.run(seed, scenario, arm,
                                           trace_ledger=(seed == SEEDS[0] and arm == 'full'))
                        m = metrics(record)
                        by_arm[arm].append(m)
                        total += 1
                        packed.write((json.dumps(record, sort_keys=True, separators=(',', ':')) + '\n').encode())
                        if seed == SEEDS[0]:
                            first_seed.append(record)
                for arm, rows in by_arm.items():
                    summaries.append({'scenario': scenario, 'arm': arm, 'runs': len(rows),
                        'metrics': {key: distribution([r[key] for r in rows]) for key in rows[0]},
                        'runs_with_mandate_change': sum(r['mandate_changes'] > 0 for r in rows),
                        'runs_with_rule_change': sum(r['rule_changes'] > 0 for r in rows),
                        'runs_with_checker_loss': sum(r['checker_losses'] > 0 for r in rows),
                        'runs_with_checker_rebuild': sum(r['checker_rebuilds'] > 0 for r in rows),
                        'runs_with_unserved': sum(r['B_unserved'] > 0 for r in rows)})
                for arm in model.ARMS:
                    if arm == 'full':
                        continue
                    differences = {
                        key: distribution([a[key] - b[key] for a, b in zip(by_arm['full'], by_arm[arm])])
                        for key in ('A_failures', 'B_failures', 'B_errors', 'B_unserved',
                                    'final_cash', 'expense_total', 'reviews')}
                    comparisons.append({'scenario': scenario, 'comparison': 'full minus ' + arm,
                                        'paired_seed_clusters': len(SEEDS), 'differences': differences})
                print('Completed', scenario, flush=True)
    result = {
        'seed_rule': '800001 + 7919*i, i=0,...,63', 'seeds': SEEDS,
        'seed_clusters': len(SEEDS), 'scenarios': model.SCENARIOS, 'arms': model.ARMS,
        'runs': total, 'money_unit': 'integer thousandths of one contract currency unit',
        'failure_definition': 'wrong completed service plus unserved requests; denominator is all requested service',
        'scope': 'Descriptive simulation variation in six constructed environments; no estimate of effects in human science.',
        'summaries': summaries, 'paired_comparisons': comparisons,
        'all_runs_sha256': hashlib.sha256((args.output / 'integration-all-runs.jsonl.gz').read_bytes()).hexdigest(),
    }
    (args.output / 'integration-validation-results.json').write_text(json.dumps(result, indent=2) + '\n')
    (args.output / 'integration-first-seed-traces.json').write_text(json.dumps(first_seed, indent=2) + '\n')
    with (args.output / 'integration-summary.csv').open('w', newline='') as f:
        fields = ['scenario', 'arm', 'runs', 'mean_B_errors', 'mean_B_unserved', 'mean_B_failures',
                  'mean_final_cash', 'mean_reviews', 'mandate_change_runs', 'rule_change_runs',
                  'checker_loss_runs', 'checker_rebuild_runs']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in summaries:
            m = row['metrics']
            writer.writerow(dict(zip(fields, [row['scenario'], row['arm'], row['runs'],
                m['B_errors']['mean'], m['B_unserved']['mean'], m['B_failures']['mean'],
                m['final_cash']['mean'] / 1000, m['reviews']['mean'],
                row['runs_with_mandate_change'], row['runs_with_rule_change'],
                row['runs_with_checker_loss'], row['runs_with_checker_rebuild']])))
    print('Completed all', total, 'runs.', flush=True)


if __name__ == '__main__':
    main()
