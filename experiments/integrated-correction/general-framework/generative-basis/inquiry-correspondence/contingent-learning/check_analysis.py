"""Rebuild the analysis with csv/Decimal, independently of pandas aggregation.

Distribution functions use SciPy in both implementations; this is not an
independent validation of SciPy or independent-agent scientific acceptance.
"""
from collections import defaultdict
import csv
from datetime import datetime, timezone
from decimal import Decimal, getcontext
import hashlib
import json
from pathlib import Path
from scipy import stats

getcontext().prec = 50
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT / 'sources/developmental-attention/bazhydai-2026'
D = Decimal


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rows(name):
    # The cleaned log has a UTF-8 BOM; decode it without changing source bytes.
    with (SRC/name).open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def near(actual, expected, tolerance=2e-12):
    assert abs(float(actual)-float(expected)) < tolerance, (actual, expected)


def check(values, saved):
    groups = {}
    for name, xs in values.items():
        n = len(xs); mean = sum(xs)/n; ss = sum((x-mean)**2 for x in xs)
        var=ss/(n-1); sd=var.sqrt(); se=(var/n).sqrt()
        g=saved['groups'][name]; assert g['n']==n
        for k,v in [('mean',mean),('sd',sd),('se',se),('one_sample_t',mean/se)]: near(v,g[k])
        radius=stats.t.ppf(.975,n-1)*float(se)
        near(float(mean)-radius,g['ci95'][0]);near(float(mean)+radius,g['ci95'][1])
        p=2*stats.t.sf(abs(float(mean/se)),n-1)
        near(p,g['p_unadjusted']);near(min(1,p*3),g['p_bonferroni_3'])
        groups[name]=(n,mean,var,ss)
    for other in ['yoked','random']:
        na,ma,va,_=groups['curiosity'];nb,mb,vb,_=groups[other]
        a,b=va/na,vb/nb;se=(a+b).sqrt();df=(a+b)**2/(a*a/(na-1)+b*b/(nb-1))
        out=saved['contrasts']['curiosity_minus_'+other]
        for k,v in [('difference',ma-mb),('se',se),('df',df)]:near(v,out[k])
        radius=stats.t.ppf(.975,float(df))*float(se)
        near(float(ma-mb)-radius,out['ci95'][0]);near(float(ma-mb)+radius,out['ci95'][1])
    n=sum(g[0] for g in groups.values());total=sum(g[0]*g[1] for g in groups.values())/n
    between=sum(g[0]*(g[1]-total)**2 for g in groups.values());within=sum(g[3] for g in groups.values())
    f=(between/2)/(within/(n-3));near(f,saved['anova']['f']);near(stats.f.sf(float(f),2,n-3),saved['anova']['p'])
    return dict(participants=n,between_ss=str(between),within_ss=str(within),f=str(f))


def main():
    result=json.loads((HERE/'results.json').read_text())
    assert result['analysis_sha256']==sha(HERE/'analyze.py')
    assert result['plan_sha256']==sha(HERE/'PLAN.md')
    for p,h in result['source_sha256'].items(): assert sha(ROOT/p)==h,p
    manifest=json.loads((SRC/'PROVENANCE.json').read_text())
    for item in manifest['files']:
        p=SRC/item['name'];assert sha(p)==item['sha256']==item['deposited_sha256']
        assert p.stat().st_size==item['bytes']
    log={(r['condition'],r['participant']) for r in rows('CuriGaze_log_Cleaned.csv')}
    wide={}
    for r in rows('hit_summary_wide1-96.csv'):
        k=(r['condition'],r['subject'],r['testTrial'],r['PrePostLabel'])
        assert k not in wide
        p=D(r['hit_1'])/(D(r['hit_1'])+D(r['hit_0']))
        near(p,D(r['propLooking']),2e-14);wide[k]=p
    participant=defaultdict(list)
    for r in rows('hit_baselineCorr1-96.csv'):
        k=(r['condition'],r['subject']);trial=k+(r['testTrial'],)
        reconstructed=wide[trial+('PostLabel',)]-wide[trial+('PreLabel',)]
        near(reconstructed,D(r['BaselineCorrProp']),2e-14)
        participant[k].append(D(r['BaselineCorrProp']))
    summary={(r['condition'],r['subject']):r for r in rows('hit_baselineCorr_byPt1-96.csv')}
    assert set(participant)==set(summary)
    primary,all_export=defaultdict(list),defaultdict(list)
    for k,xs in participant.items():
        mean=sum(xs)/len(xs);near(mean,D(summary[k]['mean_BaselineCorr_Prop']),2e-14)
        assert len(xs)==int(summary[k]['trialsN'])
        all_export[k[0]].append(mean)
        if k in log: primary[k[0]].append(mean)
    assert len(log)==75 and log.issubset(participant)
    assert sum(len(xs) for k,xs in participant.items() if k in log)==451
    assert set(participant)-log=={('curiosity','18'),('yoked','53')}
    elementary={name:check(values,result[name]) for name,values in [('primary',primary),('all_export_sensitivity',all_export)]}
    report=dict(status='passed',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        scope='Original hashes; gaze-count ratios; trial differences; participant means; cleaned-log inclusion; Decimal variances, ANOVA and Welch arithmetic; shared SciPy distribution functions.',
        independent_agent_review=False,raw_gaze_pipeline_reproduced=False,full_goal_complete=False,
        elementary_checks=elementary,source_sha256=result['source_sha256'],
        artifact_sha256={str(p.relative_to(ROOT)):sha(p) for p in [HERE/'analyze.py',HERE/'check_analysis.py',HERE/'PLAN.md',HERE/'results.json',HERE/'participant-summaries.csv']})
    (HERE/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['source_sha256','artifact_sha256']},indent=2))


if __name__=='__main__':main()
