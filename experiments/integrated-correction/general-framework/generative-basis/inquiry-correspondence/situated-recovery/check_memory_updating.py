#!/usr/bin/env python3
"""Check deposit fragments, extraction, published targets and contrast arithmetic."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat
from scipy.stats import t as student_t
from analyze_memory_updating import table_from_workspace

P = Path(__file__).resolve().parent
ROOT = next(p for p in P.parents if (p / 'RESEARCH.md').exists())
S = ROOT / 'sources/situated-recovery/heald-2021'
def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()
def read(name):
    return json.loads((P / name).read_text())
def near(a, b):
    np.testing.assert_allclose(a, b, rtol=1e-10, atol=1e-12)

r = read('memory-updating-results.json')
rows = read('memory-updating-observations.json')
trips = read('memory-updating-triplets.json')
audit = read('memory-updating-extraction-audit.json')
retrieval = json.loads((S / 'memory-updating-retrieval.json').read_text())
metadata = {x['path']: x for x in json.loads((S / 'memory-updating-selected-files.json').read_text())}
assert len(metadata) == len(retrieval['files']) == len(audit) == r['n_participants'] == 24
for entry in retrieval['files']:
    meta = metadata[entry['original_path']]
    assert entry['original_size'] == meta['size'] and entry['deposited_full_sha256'] == meta['digest']
    assert entry['full_digest_verified'] is False
    for fragment in entry['fragments']:
        path = S / fragment['path']
        assert path.stat().st_size == fragment['bytes'] == fragment['end_inclusive'] - fragment['start_inclusive'] + 1
        assert sha(path) == fragment['sha256']
    assert entry['fragments'][-1]['end_inclusive'] == meta['size'] - 1
full = retrieval['full_original_crosscheck']
path = S / full['path']
assert path.stat().st_size == full['bytes'] and sha(path) == full['sha256']
assert full['sha256'] == metadata[path.name]['digest']
with path.open('rb') as stream:
    for fragment in retrieval['files'][-1]['fragments']:
        stream.seek(fragment['start_inclusive'])
        assert stream.read(fragment['bytes']) == (S / fragment['path']).read_bytes()
data = loadmat(path, simplify_cells=True)
assert data['None']['s0'][0] == b'TrialData'
full_table, _ = table_from_workspace(data['__function_workspace__'].tobytes())
full_rows = [x for x in rows if x['participant'] == 24]
near(full_table['TrialNumber'], [x['trial'] for x in full_rows])
near(full_table['Adaptation'], [np.nan if x['adaptation'] is None else x['adaptation'] for x in full_rows])
assert sha(S / 'originals/Fig3_data_figure.m') == retrieval['code']['sha256']
assert hashlib.md5((S / 'originals/Fig3_data_figure.m').read_bytes()).hexdigest() == '68bbd8f069eba774ddf08fea5878e435'
assert len(rows) == r['trial_rows'] == 51152
assert len(trips) == r['triplets'] == 2304
assert sum(x['adaptation'] is not None for x in rows) == r['finite_channel_measurements'] == 7008
indexed = {(x['participant'], x['trial']): x for x in rows}
assert len(indexed) == len(rows)
for trip in trips:
    pid, trial = trip['participant'], trip['exposure_trial']
    left, exposure, right = (indexed[pid, trial + i] for i in [-1, 0, 1])
    assert left['field_type'] == right['field_type'] == 2 and exposure['field_type'] == 1
    assert left['cue'] == right['cue']
    near(trip['first_channel'], left['adaptation']); near(trip['second_channel'], right['adaptation'])
    near(trip['update'], np.sign(exposure['field_gain']) * (right['adaptation'] - left['adaptation']))
for person in r['participant_means']:
    pid = person['participant']
    for i, condition in enumerate(r['conditions']):
        values = [t['update'] for t in trips if t['participant'] == pid and t['condition'] == condition]
        assert len(values) == [36, 12, 12, 36][i]
        near(person['pre'][i], np.mean(values[:4])); near(person['post'][i], np.mean(values[-8:]))
        near(person['post_first_half'][i], np.mean(values[-8:-4])); near(person['post_second_half'][i], np.mean(values[-4:]))
pre = np.array([p['pre'] for p in r['participant_means']]); post = np.array([p['post'] for p in r['participant_means']])
for name, w in r['contrast_weights'].items():
    for phase, matrix in [('pre', pre), ('post', post), ('change', post - pre)]:
        v = matrix @ w; out = r['contrasts'][name][phase]
        near(v.mean(), out['mean']); near(v.std(ddof=1) / np.sqrt(24), out['sem'])
        near(2 * student_t.sf(abs(v.mean() / out['sem']), 23), out['p_two_sided'])
        assert out['positive_participants'] == sum(v > 0)
    for phase, matrix in [('pre', pre), ('post', post), ('change', post - pre)]:
        near(np.delete(matrix, 12, axis=0).dot(w).mean(), r['omit_participant13_sensitivity'][name][phase])
primary = ['cue', 'perturbation', 'interaction']
order = sorted(primary, key=lambda k: r['contrasts'][k]['change']['p_two_sided'])
adjusted = np.maximum.accumulate([min(1, (3-i) * r['contrasts'][k]['change']['p_two_sided']) for i,k in enumerate(order)])
for k, value in zip(order, adjusted):
    near(value, r['contrasts'][k]['change']['holm_adjusted_p_three_primary'])
# Published rounded Fig3 statistics are an external target, not fitted values.
published = [('pre', 'cue', 2.40), ('pre', 'perturbation', .97),
             ('post', 'cue', 10.35), ('post', 'perturbation', 21.16), ('post', 'interaction', .64)]
for phase, name, expected in published:
    actual = r['contrasts'][name][phase]['t'] ** 2
    assert abs(actual - expected) < .0051, (phase, name, actual, expected)
assert [a['participant'] for a in audit if a['missing_trial_numbers']] == [13]
assert audit[12]['missing_trial_numbers'] == [1667, 1668]
assert all(a['author_sequence_exact_match'] and a['table_copies_agree'] >= 2 for a in audit)
files = ['MEMORY-UPDATING-PLAN.md', 'MEMORY-UPDATING.md', 'fetch_memory_updating.py',
         'analyze_memory_updating.py', 'check_memory_updating.py', 'plot_memory_updating.py',
         'memory-updating-results.json', 'memory-updating-observations.json', 'memory-updating-triplets.json',
         'memory-updating-extraction-audit.json', 'memory-updating-results.png', 'memory-updating-results.svg']
receipt = {'status': 'passed', 'date': '2026-10-09', 'participants': 24, 'trial_rows': len(rows),
           'channel_measurements': 7008, 'triplets': len(trips), 'original_fragments_checked': 48,
           'complete_updating_originals_hash_verified': 1, 'full_original_participant': 24,
           'full_original_table_extraction_matches': True, 'published_rounded_statistics_matched': len(published),
           'scope': 'Provenance, exact extraction, complete participant inclusion and numerical contrast checks; no new sample, latent-state identification or infinite convergence.',
           'new_theorems': 0, 'new_laboratory_experiments': 0, 'independent_review': False,
           'source_sha256': {f: sha(P/f) for f in files},
           'retrieval_sha256': sha(S/'memory-updating-retrieval.json')}
(P / 'memory-updating-verification.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({k:receipt[k] for k in ['status','participants','trial_rows','channel_measurements','triplets','published_rounded_statistics_matched']}))
