"""Descriptive secondary analysis; no data cleaning, fitting or learning verdicts."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SOURCE = ROOT / 'sources/developmental-attention/yu-2021'
WINDOWS = (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0)
METRICS = ('target_zero', 'zero_target_other_positive', 'both_zero',
           'target_positive', 'target_majority', 'others_majority',
           'target_full', 'others_full')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((SOURCE / 'PROVENANCE.json').read_text())
    for item in manifest['files']:
        assert sha(SOURCE / item['name']) == item['sha256'] == item['deposited_sha256']
    frames, summaries, participants, diagnostics = {}, [], [], []
    identity = None
    for seconds in WINDOWS:
        path = SOURCE / f'naming_onset-{seconds:.2f}_target_exp12.csv'
        raw = pd.read_csv(path, header=1)
        headers = [x.strip().lstrip('#') for x in raw.columns]
        d = raw.copy()
        d.columns = headers
        assert len(headers) == (9 if seconds == 4 else 7)
        if seconds == 4:
            assert set(d.expID) == {12}
        d = d.rename(columns={headers[-2]: 'target', headers[-1]: 'others'})
        assert not d.isna().any().any()
        assert np.isfinite(d.to_numpy()).all()
        assert not d[['subID', 'instanceID']].duplicated().any()
        d = d.sort_values(['subID', 'instanceID']).reset_index(drop=True)
        keys = d[['subID', 'instanceID', 'onset', 'category']]
        if identity is None:
            identity = keys.copy()
        else:
            pd.testing.assert_frame_equal(keys, identity)
        assert len(d) == 1508 and d.subID.nunique() == 36
        for col in ['target', 'others']:
            assert d[col].between(0, 1).all()
        gaze_sum = d.target + d.others
        assert gaze_sum.max() <= 1.00001  # exported decimal rounding; do not alter values
        span = d.offset - d.onset
        assert (span > 0).all() and (span <= seconds + .005).all()
        d['target_zero'] = d.target == 0
        d['zero_target_other_positive'] = (d.target == 0) & (d.others > 0)
        d['both_zero'] = (d.target == 0) & (d.others == 0)
        d['target_positive'] = d.target > 0
        d['target_majority'] = d.target > .5
        d['others_majority'] = d.others > .5
        d['target_full'] = d.target == 1
        d['others_full'] = d.others == 1
        # An arithmetic remainder, not a label for incorrect attention or missing tracking.
        d['unassigned_raw'] = 1 - gaze_sum
        per = d.groupby('subID').agg(naming_events=('instanceID', 'size'))
        for metric in METRICS:
            per[metric + '_count'] = d.groupby('subID')[metric].sum()
            per[metric + '_fraction'] = d.groupby('subID')[metric].mean()
        for col in ['target', 'others', 'unassigned_raw']:
            per[col + '_mean'] = d.groupby('subID')[col].mean()
        for row in per.reset_index().to_dict(orient='records'):
            participants.append(dict(window_seconds=seconds, **row))
        summary = dict(window_seconds=seconds, events=len(d), participants=len(per))
        for metric in METRICS:
            values = per[metric + '_fraction']
            summary[metric] = dict(count=int(d[metric].sum()), event_fraction=float(d[metric].mean()),
                                   participant_mean=float(values.mean()),
                                   participant_sd=float(values.std(ddof=1)),
                                   participant_min=float(values.min()),
                                   participant_median=float(values.median()),
                                   participant_max=float(values.max()),
                                   participants_with_any=int((per[metric + '_count'] > 0).sum()))
        for col in ['target', 'others', 'unassigned_raw']:
            summary[col + '_mean'] = dict(event_weighted=float(d[col].mean()),
                                          participant_weighted=float(per[col + '_mean'].mean()))
        summaries.append(summary)
        diagnostics.append(dict(window_seconds=seconds, source=path.name, headers=headers,
                                row_count=len(d), subject_count=len(per), source_sha256=sha(path),
                                sum_above_one_count=int((gaze_sum > 1).sum()),
                                max_gaze_sum=float(gaze_sum.max()),
                                span_min=float(span.min()), span_max=float(span.max()),
                                shorter_than_nominal_by_over_5ms=int((span < seconds-.005).sum()),
                                event_count_per_subject_min=int(per.naming_events.min()),
                                event_count_per_subject_max=int(per.naming_events.max())))
        frames[seconds] = d
    paired = []
    for earlier, later in zip(WINDOWS, WINDOWS[1:]):
        a, b = frames[earlier], frames[later]
        assert (b.offset >= a.offset).all()
        # Presence monotonicity requires no assumed conversion from proportions to durations.
        paired.append(dict(earlier=earlier, later=later,
                           target_present_then_zero=int(((a.target > 0) & (b.target == 0)).sum()),
                           others_present_then_zero=int(((a.others > 0) & (b.others == 0)).sum()),
                           both_zero_then_object_gaze=int(((a.both_zero) & (~b.both_zero)).sum())))
    result = dict(status='descriptive-analysis-completed',
                  generated_at_utc=datetime.now(timezone.utc).isoformat(),
                  interpretation='Recorded gaze proportions, not learning outcomes or optical visibility.',
                  units='stored fractions of each exported window, despite percentage header',
                  source_manifest_sha256=sha(SOURCE / 'PROVENANCE.json'),
                  plan_sha256=sha(HERE / 'PLAN.md'), analysis_sha256=sha(Path(__file__)),
                  runtime=dict(python=sys.version, numpy=np.__version__, pandas=pd.__version__),
                  primary_window_seconds=3.0, windows=summaries, schema_audit=diagnostics,
                  paired_presence_checks=paired)
    (HERE / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    pd.DataFrame(participants).to_csv(HERE / 'participant-summaries.csv', index=False)
    primary = next(x for x in summaries if x['window_seconds'] == 3)
    print(json.dumps({'primary': primary, 'schema_audit': diagnostics,
                      'paired_presence_checks': paired}, indent=2))


if __name__ == '__main__':
    main()
