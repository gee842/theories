"""Recompute descriptive counts using csv/Decimal, independently of pandas."""
import csv
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path
import statistics

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SOURCE = ROOT / 'sources/developmental-attention/yu-2021'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def near(a, b):
    assert abs(float(a) - float(b)) < 1e-12, (a, b)


def main():
    result = json.loads((HERE / 'results.json').read_text())
    assert result['analysis_sha256'] == sha(HERE / 'analyze.py')
    assert result['plan_sha256'] == sha(HERE / 'PLAN.md')
    assert result['source_manifest_sha256'] == sha(SOURCE / 'PROVENANCE.json')
    manifest = json.loads((SOURCE / 'PROVENANCE.json').read_text())
    for item in manifest['files']:
        assert sha(SOURCE / item['name']) == item['sha256'] == item['deposited_sha256']
    counts_by_window = []
    for w, audit in zip(result['windows'], result['schema_audit']):
        rows = list(csv.reader((SOURCE / audit['source']).open(newline='')))
        header = [x.strip().lstrip('#') for x in rows[1]]
        by_subject = defaultdict(list)
        for row in rows[2:]:
            values = dict(zip(header[:-2], map(D, row[:-2])))
            t, o = map(D, row[-2:])
            flags = dict(target_zero=t == 0, zero_target_other_positive=t == 0 and o > 0,
                         both_zero=t == 0 and o == 0, target_positive=t > 0,
                         target_majority=t > D('.5'), others_majority=o > D('.5'),
                         target_full=t == 1, others_full=o == 1)
            flags.update(target_mean=t, others_mean=o, unassigned_raw_mean=1-t-o)
            by_subject[int(values['subID'])].append(flags)
        n = sum(map(len, by_subject.values()))
        assert n == w['events'] == 1508 and len(by_subject) == w['participants'] == 36
        for metric in list(flags)[:8]:
            per_counts = [sum(r[metric] for r in subject) for subject in by_subject.values()]
            per_rates = [D(sum(r[metric] for r in subject))/len(subject)
                         for subject in by_subject.values()]
            count = sum(per_counts)
            expected = w[metric]
            assert count == expected['count']
            near(D(count)/n, expected['event_fraction'])
            near(statistics.mean(per_rates), expected['participant_mean'])
            near(statistics.stdev(per_rates), expected['participant_sd'])
            near(statistics.median(per_rates), expected['participant_median'])
            near(min(per_rates), expected['participant_min'])
            near(max(per_rates), expected['participant_max'])
            assert sum(x > 0 for x in per_counts) == expected['participants_with_any']
        for metric in ['target_mean', 'others_mean', 'unassigned_raw_mean']:
            near(sum(r[metric] for subject in by_subject.values() for r in subject)/n,
                 w[metric]['event_weighted'])
            near(statistics.mean(sum(r[metric] for r in subject)/len(subject)
                                 for subject in by_subject.values()),
                 w[metric]['participant_weighted'])
        assert w['target_zero']['count'] == w['zero_target_other_positive']['count'] + w['both_zero']['count']
        assert n == w['target_positive']['count'] + w['target_zero']['count']
        counts_by_window.append(dict(seconds=w['window_seconds'],
                                     other_gaze_without_target=w['zero_target_other_positive']['count'],
                                     no_coded_object_gaze=w['both_zero']['count']))
    files = [HERE / n for n in ['PLAN.md', 'analyze.py', 'check_analysis.py', 'results.json', 'participant-summaries.csv']]
    files += [SOURCE / n for n in ['PROVENANCE.json', 'node-api.json', 'files-api.json']]
    files += [SOURCE / x['name'] for x in manifest['files']]
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope='All eight descriptive counts and participant statistics in seven windows independently recomputed with Decimal; source hashes verified. Not an independent research review or exact reproduction of all published analyses.',
                  distinct_naming_events=1508, subjects=36, repeated_windows=7,
                  counts_by_window=counts_by_window,
                  source_sha256={str(p.relative_to(ROOT)): sha(p) for p in files},
                  new_lean_theorems=0, independent_agent_review=False, full_goal_complete=False)
    (HERE / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'source_sha256'}, indent=2))


if __name__ == '__main__':
    main()
