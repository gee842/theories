"""Declared participant-level secondary analysis. No raw-gaze pipeline claim."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import pandas as pd
import scipy
from scipy import stats

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'sources/developmental-attention/bazhydai-2026'
CONDITIONS = ['curiosity', 'yoked', 'random']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summarize(frame):
    groups, contrasts = {}, {}
    for name in CONDITIONS:
        values = frame.loc[frame.condition == name, 'mean'].to_numpy()
        n = len(values); mean = values.mean(); sd = values.std(ddof=1)
        se = sd / np.sqrt(n); radius = stats.t.ppf(.975, n-1) * se
        t = mean/se; p = 2 * stats.t.sf(abs(t), n-1)
        groups[name] = dict(n=n, mean=float(mean), sd=float(sd), se=float(se),
            ci95=[float(mean-radius), float(mean+radius)], one_sample_t=float(t),
            one_sample_df=n-1, p_unadjusted=float(p), p_bonferroni_3=float(min(1, p*3)))
    a = groups['curiosity']
    for other in ['yoked', 'random']:
        b = groups[other]; va=a['sd']**2/a['n']; vb=b['sd']**2/b['n']
        se = np.sqrt(va+vb); df=(va+vb)**2/(va**2/(a['n']-1)+vb**2/(b['n']-1))
        d=a['mean']-b['mean']; radius=stats.t.ppf(.975, df)*se
        contrasts['curiosity_minus_'+other] = dict(difference=d,se=float(se),df=float(df),
            ci95=[float(d-radius),float(d+radius)])
    f,p = stats.f_oneway(*[frame.loc[frame.condition == c, 'mean'] for c in CONDITIONS])
    return dict(groups=groups,contrasts=contrasts,anova=dict(f=float(f),df_between=2,
        df_within=len(frame)-3,p=float(p)))


def main():
    log = pd.read_csv(SRC / 'CuriGaze_log_Cleaned.csv')
    trials = pd.read_csv(SRC / 'hit_baselineCorr1-96.csv').rename(columns={'subject':'participant','label':'item'})
    summary = pd.read_csv(SRC / 'hit_baselineCorr_byPt1-96.csv').rename(columns={'subject':'participant'})
    wide = pd.read_csv(SRC / 'hit_summary_wide1-96.csv')
    keys = ['condition','participant']
    assert list(set(trials.columns) & set(log.columns)) and set(trials.columns) & set(log.columns) == set(keys)
    assert not log.duplicated(keys).any() and not trials.duplicated(keys+['testTrial']).any()
    assert not trials.isna().any().any()
    assert trials.groupby(keys).LearningTrialsN.nunique().eq(1).all()
    assert np.allclose(trials.PostLabel-trials.PreLabel,trials.BaselineCorrProp,rtol=0,atol=2e-14)
    ratios=wide.hit_1/(wide.hit_0+wide.hit_1)
    assert np.allclose(ratios,wide.propLooking,rtol=0,atol=2e-14)
    pivot=wide.pivot(index=['condition','subject','LearningTrialsN','testTrial','label'],columns='PrePostLabel',values='propLooking')
    complete=pivot.dropna(subset=['PreLabel','PostLabel']).reset_index().rename(columns={'subject':'participant','label':'item'})
    joined=trials.merge(complete,on=keys+['LearningTrialsN','testTrial','item'],validate='one_to_one',suffixes=('_saved','_rebuilt'))
    assert len(joined)==len(trials)==len(complete)
    for c in ['PreLabel','PostLabel']:
        assert np.allclose(joined[c+'_saved'],joined[c+'_rebuilt'],rtol=0,atol=2e-14)
    all_pt=trials.groupby(keys,as_index=False).agg(mean=('BaselineCorrProp','mean'),trials=('BaselineCorrProp','size'))
    compare=all_pt.merge(summary,on=keys,validate='one_to_one')
    assert len(compare)==len(all_pt)==len(summary)==77
    assert np.allclose(compare['mean'],compare.mean_BaselineCorr_Prop,rtol=0,atol=2e-14)
    assert (compare.trials==compare.trialsN).all()
    included=trials.merge(log[keys],on=keys,validate='many_to_one')
    assert len(included)==451
    pt=included.groupby(keys,as_index=False).agg(mean=('BaselineCorrProp','mean'),trials=('BaselineCorrProp','size'))
    assert len(pt)==75 and pt.groupby('condition').size().eq(25).all()
    excluded=all_pt.merge(log[keys],on=keys,how='left',indicator=True).query('_merge == "left_only"')
    pt.to_csv(HERE / 'participant-summaries.csv',index=False,float_format='%.17g')
    result=dict(created_at_utc=datetime.now(timezone.utc).isoformat(),
        scope='Exploratory participant-level summaries; conditional t/Welch intervals, no equivalence or causal-identification claim.',
        software=dict(python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__),
        units='proportion change (multiply by 100 for percentage points)',
        audit=dict(export_participants=77,primary_participants=75,export_trials=len(trials),primary_trials=len(included),
            primary_trials_by_condition={k:int(v) for k,v in included.groupby('condition').size().items()},
            log_omissions=excluded[keys+['trials']].to_dict('records'),
            omitted_reason='Cleaned-log membership only; individual omission reasons not established.',
            yoking_partner_ids_available=False,wide_rows=len(wide),complete_prepost_pairs=len(complete),
            incomplete_prepost_pairs=int(pivot[['PreLabel','PostLabel']].isna().any(axis=1).sum()),
            maximum_summary_reconstruction_difference=float(np.max(np.abs(compare['mean']-compare.mean_BaselineCorr_Prop)))),
        primary=summarize(pt),all_export_sensitivity=summarize(all_pt),
        source_sha256={str(p.relative_to(ROOT)):sha(p) for p in sorted(SRC.glob('*')) if p.is_file()},
        analysis_sha256=sha(Path(__file__)),plan_sha256=sha(HERE/'PLAN.md'))
    (HERE/'results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:result[k] for k in ['audit','primary','all_export_sensitivity']},indent=2))


if __name__ == '__main__':
    main()
