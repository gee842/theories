#!/usr/bin/env python3
"""Source-ordered MPC timing domains and exact recorded-command exposure bounds.
No hardware, upstream execution, invented issue timestamp or future calibration.
Fractions preserve the finite decimal values in the archived files exactly.
"""
from pathlib import Path
from fractions import Fraction as F
import csv
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BASE = ROOT / 'sources/tclab-benchmark/extracted/3_TCLab'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    with path.open() as stream:
        return [{key: F(value) for key, value in row.items()} for row in csv.DictReader(stream)]


def encoded(value):
    return dict(exact=str(value), approximate=float(value))


def metrics(rows):
    error = sum(abs(r['T1']-r['T1SP'])+abs(r['T2']-r['T2SP']) for r in rows)
    movement = sum(abs(b['Q1']-a['Q1'])+abs(b['Q2']-a['Q2']) for a, b in zip(rows, rows[1:]))
    return dict(rows=len(rows), total_sample_error=encoded(error), mean_sample_error=encoded(error/len(rows)),
                total_movement=encoded(movement), movement_over_last_timestamp=encoded(movement/rows[-1]['Time']))


def source_contract(path, statements):
    lines = path.read_text().splitlines()
    found = []
    for statement in statements:
        matches = [i+1 for i, line in enumerate(lines) if statement in line]
        assert len(matches) == 1, (path, statement, matches)
        found.append(dict(statement=statement, line=matches[0]))
    return dict(path=str(path.relative_to(ROOT)), sha256=sha(path), statements=found)


def age_domains(rows, queued):
    result = []
    for i in range(2, len(rows)-1):
        stamp = rows[i-1]['Time'] if queued else rows[i]['Time']
        lower = rows[i]['Time']-stamp
        upper = rows[i+1]['Time']-stamp
        result.append(dict(index=i, input_record=i-1 if queued else i,
                           timestamp_age_lower=encoded(lower), age_upper=encoded(upper)))
    return dict(intervals=result, max_upper_seconds=float(max(F(r['age_upper']['exact']) for r in result)),
                deadline_classification={str(d): {
                    'certainly_within': sum(F(r['age_upper']['exact']) <= d for r in result),
                    'certainly_beyond_timestamp_deadline': sum(F(r['timestamp_age_lower']['exact']) > d for r in result),
                    'undetermined': sum(F(r['timestamp_age_lower']['exact']) <= d < F(r['age_upper']['exact']) for r in result)
                } for d in [1, 2, 3]},
                scope='Timestamp-age interval from source event order. Readout retrieval occurs after its timestamp, so the upper bound also bounds retrieval-to-request delay. The historical driver, firmware and hardware conversion timestamps are absent: interpreting this as hardware sample age additionally requires sampling within the retrieval bracket or an added internal-age bound. Recorded periods do not isolate solver duration or establish future bounds.')


def window_bounds(rows, start, end):
    channels = {}
    for key in ['Q1', 'Q2']:
        pieces = []
        for i in range(2, len(rows)-1):
            left = max(start, rows[i]['Time'])
            right = min(end, rows[i+1]['Time'])
            if right <= left:
                continue
            width = right-left
            old, new = rows[i-1][key], rows[i][key]
            lower, upper = width*min(old, new), width*max(old, new)
            center, radius = width*(old+new)/2, width*abs(old-new)/2
            assert center-radius == lower and center+radius == upper
            pieces.append(dict(index=i, start=str(left), end=str(right), old=str(old), new=str(new),
                               lower=str(lower), upper=str(upper), center=str(center), radius=str(radius)))
        assert sum(F(p['end'])-F(p['start']) for p in pieces) == end-start
        totals = {k: sum(F(p[k]) for p in pieces) for k in ['lower', 'upper', 'center', 'radius']}
        channels[key] = {k: encoded(v) for k, v in totals.items()}
        channels[key]['pieces'] = pieces
    combined = {k: sum(F(channels[q][k]['exact']) for q in channels) for k in ['lower', 'upper', 'center', 'radius']}
    # A descriptive time-weighted score for held sampled errors; this is not
    # a certified continuous-temperature integral or sensor calibration.
    held_error = F(0)
    for i in range(1, len(rows)-1):
        width = max(F(0), min(end, rows[i+1]['Time'])-max(start, rows[i]['Time']))
        held_error += width*(abs(rows[i]['T1']-rows[i]['T1SP'])+abs(rows[i]['T2']-rows[i]['T2SP']))
    return dict(start=encoded(start), end=encoded(end), duration=encoded(end-start), channels=channels,
                combined={k: encoded(v) for k, v in combined.items()},
                mean_held_sample_error=encoded(held_error/(end-start)),
                scope='Requested-command percent-seconds on the shared timestamp interval. Switch times are unknown within each source-ordered interval; each channel has a conservative enclosure. The held-sample error uses a declared reconstruction convention, not a proved thermal trajectory. No energy or ethical ordering is inferred.')


def main():
    provenance = ROOT / 'sources/tclab-benchmark/TIMING-PROVENANCE.json'
    manifest = json.loads(provenance.read_text())
    for item in manifest['extracted_members']:
        assert sha(ROOT/item['path']) == item['sha256']
    contracts = [source_contract(BASE/'ARX/tclab_farx.py', [
        'n = tf * 60 + 1', 'for i in range(1,n-1):', 'sleep_max = 1.0',
        'tm[i] = t - start_time', 'T1m[i] = a.T1', 'Q1s[i+1]  = Q1.NEWVAL',
        'a.Q1(Q1s[i])', 'tm[-1] = t - start_time', 'm.time=np.linspace(0,120,61)']),
        source_contract(BASE/'Physics/tclab_hybrid.py', [
        'loops = int(30.0*run_time)', 'for i in range(1,loops):', 'sleep_max = 2.0',
        'tm[i] = t - start_time', 'T1s[i] = a.T1', 'Q1s[i] = Q1.NEWVAL', 'a.Q1(Q1s[i])']),
        source_contract(BASE/'ANN/tclab_ann.py', [
        'loops = int(30.0*run_time)', 'for i in range(1,loops):', 'sleep_max = 2.0',
        'tm[i] = t - start_time', 'T1[i] = a.T1', 'Q1s[i] = Q1.NEWVAL', 'a.Q1(Q1s[i])']),
        source_contract(BASE/'Summary/results.py', ['sae[i] = sae[i] / len(data)', "qmv[i] = qmv[i] / data['Time'].values[-1]"])]
    specs = [('physics', 'Summary/results_hybrid.csv', False),
             ('arx_summary', 'Summary/results_farx.csv', True),
             ('ann', 'Summary/results_ann.csv', False),
             ('arx_figure', 'ARX/results_farx.csv', True)]
    valid = {}
    reports = []
    for label, name, queued in specs:
        path = BASE/name
        rows = load(path)
        assert len(rows) == (601 if queued else 300)
        assert all(b['Time'] > a['Time'] for a, b in zip(rows, rows[1:]))
        last = len(rows)-2 if queued else len(rows)-1
        if queued:
            assert all(rows[-1][q] == rows[0][q] for q in ['T1', 'T2'])
            assert rows[-1]['Time'] > rows[last]['Time']
        valid[label] = rows[:last+1]
        dt = [b['Time']-a['Time'] for a, b in zip(valid[label], valid[label][1:])]
        reports.append(dict(label=label, source=str(path.relative_to(ROOT)), source_sha256=sha(path),
                            queued_previous_plan=queued, last_acquired_index=last,
                            initialization_index=0, unacquired_terminal_indices=[600] if queued else [],
                            original_summary=metrics(rows), acquired_rows_only=metrics(rows[1:last+1]),
                            min_recorded_interval_seconds=float(min(dt)), max_recorded_interval_seconds=float(max(dt)),
                            timing=age_domains(valid[label], queued)))
    labels = ['physics', 'arx_summary', 'ann']
    start = max(valid[label][2]['Time'] for label in labels)
    end = min(valid[label][-1]['Time'] for label in labels)
    windows = {label: window_bounds(valid[label], start, end) for label in labels}
    comparisons = []
    for a in labels:
        for b in labels:
            if a == b:
                continue
            upper_a = F(windows[a]['combined']['upper']['exact'])
            lower_b = F(windows[b]['combined']['lower']['exact'])
            comparisons.append(dict(lower_exposure=a, higher_exposure=b,
                                    certified_by_disjoint_intervals=upper_a < lower_b,
                                    separating_margin=encoded(lower_b-upper_a),
                                    channel_separating_margins={q: encoded(
                                        F(windows[b]['channels'][q]['lower']['exact'])-
                                        F(windows[a]['channels'][q]['upper']['exact'])) for q in ['Q1', 'Q2']}))
    duplicate = {name: (BASE/(folder+'/'+name)).read_bytes() == (BASE/('Summary/'+name)).read_bytes()
                 for folder, name in [('Physics', 'results_hybrid.csv'), ('ANN', 'results_ann.csv'), ('ARX', 'results_farx.csv')]}
    output = dict(status='passed', producer_sha256=sha(Path(__file__)), provenance_sha256=sha(provenance),
                  source_contracts=contracts, duplicate_summary_members=duplicate, runs=reports,
                  primary_common_window=windows, exposure_comparisons=comparisons,
                  scope='Historical source/log correspondence and source-ordered timing/exposure domains. Three primary comparison records plus one distinct ARX illustration. Initialization and unacquired terminal rows remain preserved and are separately identified. Source fidelity, monotone clock and successful retained command writes are explicit; no prospective latency bound, thermal calibration, causal ranking of methods, or living-protection guarantee.')
    (HERE/'timing-results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(status='passed', runs=[{
        'label': r['label'], 'original_mean': r['original_summary']['mean_sample_error']['approximate'],
        'acquired_mean': r['acquired_rows_only']['mean_sample_error']['approximate'],
        'max_command_readout_age_upper': r['timing']['max_upper_seconds'],
        'deadline_counts': r['timing']['deadline_classification']} for r in reports],
        windows={k: {'exposure': {j: v['combined'][j]['approximate'] for j in ['lower', 'upper']},
                     'mean_held_error': v['mean_held_sample_error']['approximate']} for k, v in windows.items()},
        comparisons=[r for r in comparisons if r['certified_by_disjoint_intervals']]), indent=2))


if __name__ == '__main__':
    main()
