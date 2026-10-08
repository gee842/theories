"""Read-only dated-assay transfer checks with explicit follow-up eligibility."""
from collections import Counter,defaultdict
from io import BytesIO
import json
import math
from zipfile import ZipFile

import openpyxl
import forecast_lineages as f

HERE=f.HERE
ARCHIVE=f.ROOT/'sources/evolutionary-selection/doulcier-2025/lce-genealogies-code-and-data.zip'
MEMBER='lce-genealogies-main/raw/24-04-03/Lifecycle fitness tests.xlsx'
STRAINS=('PE-2-WT-A5','PE-2-WT-A5 mutL')
DATES=('2018-05-22','2020-02-17','2020-06-02')


def raw_rows():
    with ZipFile(ARCHIVE) as z:
        book=openpyxl.load_workbook(BytesIO(z.read(MEMBER)),read_only=True,data_only=True)
    values=list(book['raw'].values)
    rows=[dict(zip(values[0],row),source_row=i) for i,row in enumerate(values[1:],2)]
    for r in rows:r['Date']=str(r['Date'])[:10]
    return rows


def key(r):return str(r['Rack']),str(r['Tube'])


def positive(v):return isinstance(v,(int,float)) and v>0


def batch(rows,date,strain):
    sub=[r for r in rows if r['Date']==date and r['Strain']==strain and str(r['Size']).lower()=='large']
    phases={p:{key(r):r for r in sub if r['Phase']==p} for p in (1,2)}
    assert sum(map(len,phases.values()))==len(sub)
    initial=phases[1];later=phases[2]
    survived={k for k,r in initial.items() if r['Extinct']==0}
    assert all((positive(r['Mat']) and positive(r['Count SM']))==(r['Extinct']==0) for r in initial.values())
    return dict(date=date,strain=strain,n1=len(initial),survived1=len(survived),n2=len(later),survived2=sum(r['Extinct']==0 for r in later.values()),
                followed_original_survivors=len(survived&later.keys()),
                missing_original_survivors=sorted(survived-later.keys()),
                later_nonoriginal_survivor_slots=sorted(later.keys()-survived),
                linked_final=sum(later[k]['Extinct']==0 for k in survived&later.keys()),
                joint_mat_sm=dict(Counter(f'{int(positive(r["Mat"]))}{int(positive(r["Count SM"]))}' for r in initial.values())),
                flags=dict(Counter(str(r['Condition']) for r in sub)),
                source_rows=[r['source_row'] for r in sub]),phases


def score(observations,p):
    assert 0<p<1 and observations
    return dict(n=len(observations),observed_success=sum(observations),probability=p,
                predicted_success=len(observations)*p,
                brier=sum((p-y)**2 for y in observations)/len(observations),
                log_loss=-sum(math.log(p if y else 1-p) for y in observations)/len(observations))


def main():
    rows=raw_rows();groups=defaultdict(list)
    for r in rows:groups[r['Date'],r['Strain'],str(r['Size']).lower(),r['Phase']].append(r)
    inventory=[]
    for (date,strain,size,phase),rs in sorted(groups.items()):
        inventory.append(dict(date=date,strain=strain,size=size,phase=phase,n=len(rs),survived=sum(r['Extinct']==0 for r in rs),
                              conditions=dict(Counter(str(r['Condition']) for r in rs)),
                              replacements=dict(Counter(str(r['Replaced by']) for r in rs)),source_rows=[r['source_row'] for r in rs]))
    selected=[r for r in rows if r['Date'] in DATES and r['Strain'] in STRAINS and str(r['Size']).lower()=='large']
    f.dump_csv(HERE/'assay-transfer-reading.csv',selected)
    batches=[];maps={}
    for date in DATES:
        for strain in STRAINS:
            summary,phases=batch(rows,date,strain)
            if summary['n1']:batches.append(summary);maps[date,strain]=phases
    feb={s:maps[DATES[1],s][1] for s in STRAINS}
    pooled=(1+sum(r['Extinct']==0 for b in feb.values() for r in b.values()))/(2+sum(map(len,feb.values())))
    predictions=[]
    for strain in STRAINS:
        earlier=feb[strain];p=(1+sum(r['Extinct']==0 for r in earlier.values()))/(2+len(earlier))
        target=maps[DATES[2],strain][1]
        y=[int(r['Extinct']==0) for r in target.values()]
        for model,prob in [('genotype_specific_february',p),('pooled_february',pooled),('uninformative',0.5)]:
            predictions.append(dict(training_date=DATES[1],test_date=DATES[2],strain=strain,phase='I',model=model,**score(y,prob)))
    early=maps[DATES[0],STRAINS[0]];test=maps[DATES[2],STRAINS[0]]
    survive={k for k,r in early[1].items() if r['Extinct']==0}
    assert survive<=early[2].keys()
    p1=(1+len(survive))/(2+len(early[1]))
    p2=(1+sum(early[2][k]['Extinct']==0 for k in survive))/(2+len(survive))
    direct=(1+sum(early[2][k]['Extinct']==0 for k in survive))/(2+len(early[1]))
    for clean in (False,True):
        y1=[int(r['Extinct']==0) for r in test[1].values() if not clean or r['Condition']==0]
        y2=[int(r['Extinct']==0) for r in test[2].values() if not clean or r['Condition']==0]
        yc=[int(k in test[2] and test[2][k]['Extinct']==0) for k,r in test[1].items()
            if not clean or (r['Condition']==0 and (k not in test[2] or test[2][k]['Condition']==0))]
        for phase,model,y,p in [('I','2018_stage',y1,p1),('II given I','2018_stage',y2,p2),
                              ('cycle','2018_stage_product',yc,p1*p2),('cycle','2018_direct_cycle',yc,direct)]:
            predictions.append(dict(training_date=DATES[0],test_date=DATES[2],strain=STRAINS[0],phase=phase,model=model,condition_zero_only=clean,**score(y,p)))
    output=dict(raw_rows=len(rows),cohorts=inventory,focal_batches=batches,predictions=predictions,
                missing_cycle_prediction=dict(training_date=DATES[1],test_date=DATES[2],status='not empirically calibrated',
                                              reason='Evolved phase-II follow-up covers 7/41 survivors; revertant covers 0/51. Neither missingness nor selective follow-up is treated as a complete conditional-stage sample.'),
                scope='Descriptive retrospective batch transfer under count-model priors. No culture-independent inference, microscopic switching rate, fresh intervention, or new theorem.',
                bindings={p.name:f.sha(p) for p in (HERE/'assay_transfer.py',HERE/'TRANSFER-PROTOCOL.md',HERE/'assay-transfer-reading.csv',ARCHIVE)})
    (HERE/'assay-transfer-results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(focal_batches=batches,predictions=predictions,raw_rows=len(rows),cohorts=len(inventory)),indent=2))


if __name__=='__main__':main()
