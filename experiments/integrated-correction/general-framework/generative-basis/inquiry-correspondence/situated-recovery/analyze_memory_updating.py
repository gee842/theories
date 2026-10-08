#!/usr/bin/env python3
"""Reanalyse the complete participant set from preserved MAT5 table fragments."""
import hashlib
import io
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.io import loadmat
from scipy.io.matlab._mio5 import MatFile5Reader
from scipy.stats import ttest_1samp

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = ROOT / 'sources/situated-recovery/heald-2021'
CONDITIONS = ('P+cue1', 'P+cue2', 'P-cue1', 'P-cue2')
WEIGHTS = {'cue': [.5, -.5, .5, -.5],
           'perturbation': [.5, .5, -.5, -.5],
           'interaction': [1, -1, -1, 1],
           'cue_at_P+': [1, -1, 0, 0],
           'cue_at_P-': [0, 0, 1, -1]}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')

def table_from_workspace(workspace):
    assert workspace[:4] == b'\x00\x01IM'
    reader = MatFile5Reader(io.BytesIO(workspace), byte_order='<',
                           struct_as_record=False, squeeze_me=True)
    reader.initialize_read()
    reader.mat_stream.seek(8)
    header, _ = reader.read_var_header()
    cells = reader.read_var_array(header).MCOS['arr'][0]
    candidates = []
    for i in range(2, len(cells) - 5):
        names, values = cells[i + 5], cells[i]
        if not (isinstance(names, np.ndarray) and names.dtype == object
                and all(isinstance(x, str) for x in names) and 'Adaptation' in names):
            continue
        assert int(cells[i + 4]) == len(names) == len(values)
        table = dict(zip(names, values))
        assert all(len(v) == int(cells[i + 2]) for v in table.values())
        candidates.append(table)
    assert len(candidates) >= 2
    common = set.intersection(*(set(t) for t in candidates))
    required = {'BlockName', 'BlockTrial', 'TrialNumber', 'FieldConstants', 'ControlPoint',
                'FieldType', 'MissTrial', 'Adaptation'}
    assert required <= common
    for key in common:
        for candidate in candidates[1:]:
            np.testing.assert_equal(candidates[0][key], candidate[key])
    return {k: candidates[0][k] for k in required}, len(candidates)

def read_fragments(entry):
    fragments = entry['fragments']
    assert len(fragments) == 2
    for item in fragments:
        path = SOURCE / item['path']
        assert path.stat().st_size == item['bytes'] and sha(path) == item['sha256']
    # In-memory reading edition only: concatenate original header and subsystem.
    # The byte fragments on disk stay unchanged, and no new MAT is called original.
    data = b''.join((SOURCE / f['path']).read_bytes() for f in fragments)
    d = loadmat(io.BytesIO(data), simplify_cells=True)
    assert set(d) == {'__header__', '__version__', '__globals__', '__function_workspace__'}
    return table_from_workspace(d['__function_workspace__'].tobytes())

def author_sequence(table, cue1, plus):
    """Separately translate Fig3's chronological channel counter and reshape."""
    buckets = [[] for _ in range(6)]
    for i in np.flatnonzero(np.isfinite(table['Adaptation'])):
        if 'Triplet' in table['BlockName'][i]:
            exposure = i + 1 if sum(len(b) for b in buckets[:4]) % 2 == 0 else i - 1
            sign = np.sign(table['FieldConstants'][exposure, 0])
            cue = table['ControlPoint'][exposure]
            condition = 2 * int(sign != plus) + int(cue != cue1)
        else:
            assert table['BlockName'][i] == 'Double'
            condition = 4 + int(table['ControlPoint'][i] != cue1)
        buckets[condition].append(plus * table['Adaptation'][i])
    assert [len(x) for x in buckets] == [72, 24, 24, 72, 50, 50]
    return [(np.asarray(x).reshape(-1, 2)[:, 1] - np.asarray(x).reshape(-1, 2)[:, 0])
            * (1 if c < 2 else -1) for c, x in enumerate(buckets[:4])]

def extract():
    receipt = json.loads((SOURCE / 'memory-updating-retrieval.json').read_text())
    rows, trips, audits, participant = [], [], [], []
    assert len(receipt['files']) == 24
    for entry in receipt['files']:
        pid = int(entry['original_path'].split('participant')[1].split('.')[0])
        table, copies = read_fragments(entry)
        n = len(table['TrialNumber'])
        assert not np.any(table['MissTrial']), 'Reconcile any missed rows explicitly'
        trial_numbers = table['TrialNumber'].astype(int)
        assert trial_numbers[0] == 1 and np.all(np.diff(trial_numbers) > 0)
        gaps = sorted(set(range(1, int(trial_numbers[-1]) + 1)) - set(trial_numbers))
        assert gaps == ([1667, 1668] if pid == 13 else [])
        finite = np.isfinite(table['Adaptation'])
        assert np.array_equal(finite, table['FieldType'] == 2)
        assert sum(finite) == 292
        first = np.flatnonzero(table['BlockName'] == 'Triplet1')[0]
        cue1 = table['ControlPoint'][first]
        training = np.flatnonzero((table['BlockName'] == 'Exposure') & (table['ControlPoint'] == cue1))
        plus = np.sign(table['FieldConstants'][training[0], 0])
        assert cue1 in (-1, 1) and plus in (-1, 1)
        for i in range(n):
            rows.append({'participant': pid, 'trial': int(table['TrialNumber'][i]),
                         'block': str(table['BlockName'][i]), 'block_trial': int(table['BlockTrial'][i]),
                         'cue': int(table['ControlPoint'][i]), 'field_type': int(table['FieldType'][i]),
                         'field_gain': float(table['FieldConstants'][i, 0]),
                         'adaptation': float(table['Adaptation'][i]) if finite[i] else None})
        grouped = [[] for _ in range(4)]
        for i in range(1, n - 1):
            if 'Triplet' not in table['BlockName'][i] or table['FieldType'][i] != 1:
                continue
            assert trial_numbers[i - 1] + 1 == trial_numbers[i] == trial_numbers[i + 1] - 1
            assert table['FieldType'][i - 1] == table['FieldType'][i + 1] == 2
            assert table['BlockName'][i - 1] == table['BlockName'][i] == table['BlockName'][i + 1]
            assert table['ControlPoint'][i - 1] == table['ControlPoint'][i + 1] == cue1
            sign = np.sign(table['FieldConstants'][i, 0])
            assert abs(table['FieldConstants'][i, 0]) == .15
            cond = 2 * int(sign != plus) + int(table['ControlPoint'][i] != cue1)
            update = sign * (table['Adaptation'][i + 1] - table['Adaptation'][i - 1])
            grouped[cond].append(float(update))
            trips.append({'participant': pid, 'condition': CONDITIONS[cond], 'condition_index': cond,
                          'ordinal': len(grouped[cond]), 'exposure_trial': int(trial_numbers[i]),
                          'first_channel': float(table['Adaptation'][i - 1]),
                          'second_channel': float(table['Adaptation'][i + 1]),
                          'exposure_sign': int(sign), 'update': float(update)})
        assert [len(x) for x in grouped] == [36, 12, 12, 36]
        reference = author_sequence(table, cue1, plus)
        for a, b in zip(grouped, reference):
            np.testing.assert_allclose(a, b, rtol=0, atol=0)
        pre = [float(np.mean(x[:4])) for x in grouped]
        post = [float(np.mean(x[-8:])) for x in grouped]
        first_half = [float(np.mean(x[-8:-4])) for x in grouped]
        second_half = [float(np.mean(x[-4:])) for x in grouped]
        participant.append({'participant': pid, 'cue1': int(cue1), 'P_plus': int(plus),
                            'pre': pre, 'post': post, 'post_first_half': first_half,
                            'post_second_half': second_half})
        audits.append({'participant': pid, 'rows': n, 'finite_channels': int(sum(finite)),
                       'missed_trials': 0, 'missing_trial_numbers': gaps, 'table_copies_agree': copies,
                       'triplets_by_condition': [len(x) for x in grouped],
                       'author_sequence_exact_match': True})
    assert sorted(x['participant'] for x in participant) == list(range(1, 25))
    save('memory-updating-observations.json', rows)
    save('memory-updating-triplets.json', trips)
    save('memory-updating-extraction-audit.json', audits)
    return participant, rows, trips, audits

def summary(values, rng):
    values = np.asarray(values)
    assert values.shape == (24,) and np.all(np.isfinite(values))
    boot = values[rng.integers(0, 24, (20000, 24))].mean(axis=1)
    test = ttest_1samp(values, 0)
    loo = (values.sum() - values) / 23
    return {'mean': float(values.mean()), 'sem': float(values.std(ddof=1) / np.sqrt(24)),
            'bootstrap_ci95': np.quantile(boot, [.025, .975]).tolist(),
            'positive_participants': int(sum(values > 0)),
            'negative_participants': int(sum(values < 0)),
            't': float(test.statistic), 'df': 23, 'p_two_sided': float(test.pvalue),
            'leave_one_out_mean_range': [float(min(loo)), float(max(loo))]}

def main():
    participants, rows, trips, audits = extract()
    rng = np.random.default_rng(20261009)
    pre = np.array([x['pre'] for x in participants])
    post = np.array([x['post'] for x in participants])
    phase = {label: {cond: summary(matrix[:, i], rng) for i, cond in enumerate(CONDITIONS)}
             for label, matrix in [('pre', pre), ('post', post)]}
    contrasts = {}
    for name, w in WEIGHTS.items():
        contrasts[name] = {phase: summary(matrix @ w, rng)
                           for phase, matrix in [('pre', pre), ('post', post), ('change', post - pre)]}
    primary = list(WEIGHTS)[:3]
    order = sorted(primary, key=lambda k: contrasts[k]['change']['p_two_sided'])
    floor = 0
    for rank, key in enumerate(order):
        floor = max(floor, min(1., (3 - rank) * contrasts[key]['change']['p_two_sided']))
        contrasts[key]['change']['holm_adjusted_p_three_primary'] = floor
    a = np.array([x['post_first_half'] for x in participants])
    b = np.array([x['post_second_half'] for x in participants])
    halves = {name: {'first_half': summary(a @ w, rng), 'second_half': summary(b @ w, rng),
                     'second_minus_first': summary((b - a) @ w, rng)} for name, w in WEIGHTS.items()}
    out = {'analysis_date': '2026-10-09', 'kind': 'exploratory secondary reanalysis; no new experiment',
           'n_participants': 24, 'trial_rows': len(rows), 'finite_channel_measurements': sum(x['finite_channels'] for x in audits),
           'triplets': len(trips), 'pre_triplets_used': 24 * 4 * 4, 'post_triplets_used': 24 * 4 * 8,
           'conditions': list(CONDITIONS), 'contrast_weights': WEIGHTS,
           'bootstrap': {'replicates': 20000, 'seed': 20261009, 'unit': 'participant'},
           'phase_means': phase, 'contrasts': contrasts, 'post_half_sensitivity': halves,
           'participant_means': participants,
           'omit_participant13_sensitivity': {name: {'pre': float(np.delete(pre, 12, axis=0).dot(w).mean()), 'post': float(np.delete(post, 12, axis=0).dot(w).mean()), 'change': float(np.delete(post - pre, 12, axis=0).dot(w).mean())} for name, w in WEIGHTS.items()},
           'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}}
    save('memory-updating-results.json', out)
    print(json.dumps({k: out[k] for k in ['n_participants', 'trial_rows', 'finite_channel_measurements', 'triplets']}))
    print(json.dumps(contrasts, indent=2))

if __name__ == '__main__':
    main()
