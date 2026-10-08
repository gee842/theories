"""Separate source-XML, enumeration and arithmetic checks for the follow-up."""
from collections import Counter,defaultdict
import copy
import csv
from datetime import datetime,timedelta
from fractions import Fraction
from io import BytesIO
import itertools
import json
import math
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import numpy as np
import forecast_lineages as f
import forecast_blocks as b
from check_forecast import enumeration

HERE=f.HERE
ARCHIVE=f.ROOT/'sources/evolutionary-selection/doulcier-2025/lce-genealogies-code-and-data.zip'
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def xml_raw():
    with ZipFile(ARCHIVE) as outer:
        raw=outer.read('lce-genealogies-main/raw/24-04-03/Lifecycle fitness tests.xlsx')
    with ZipFile(BytesIO(raw)) as z:
        strings=[''.join(e.itertext()) for e in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',NS)]
        rels={e.get('Id'):e.get('Target') for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheets=ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',NS)
        sh=next(e for e in sheets if e.get('name')=='raw')
        rel=sh.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        path=rels[rel].lstrip('/');path=path if path.startswith('xl/') else 'xl/'+path
        cells={}
        for row in ET.fromstring(z.read(path)).findall('s:sheetData/s:row',NS):
            values={}
            for c in row.findall('s:c',NS):
                v=c.find('s:v',NS)
                if v is None:continue
                if c.get('t')=='s':value=strings[int(v.text)]
                else:
                    q=Fraction(v.text);value=int(q) if q.denominator==1 else float(q)
                values[''.join(a for a in c.get('r') if a.isalpha())]=value
            cells[int(row.get('r'))]=values
        header=cells.pop(1);rows=[]
        for number,r in cells.items():
            d={name:r.get(col) for col,name in header.items()}
            d['Date']=(datetime(1899,12,30)+timedelta(days=d['Date'])).strftime('%Y-%m-%d')
            d['source_row']=number;rows.append(d)
        return rows


def main():
    prior=json.loads((HERE/'forecast-verification.json').read_text())
    for name,digest in prior['bindings'].items():assert f.sha(HERE/name)==digest
    meta=json.loads((ARCHIVE.parent/'manifest.json').read_text())
    for item in meta['files']:assert f.sha(ARCHIVE.parent/item['file'])==item['sha256']
    # Exact finite-state summation independently exercises block grouping and roots.
    x,k=f.kernel(3,sigmas=(1,5,25));enum_checks=0;max_error=0.0
    for common in (False,True):
        for counts in ((0,8,4,4),(8,8,7,6),(2,6,5,1),(4,4,0,8)):
            prefix=[]
            for t,block,y in ((1,'A',counts[0]),(1,'B',counts[1]),(3,'A',counts[2]),(3,'B',counts[3])):
                prefix.extend(dict(time=t,tube=block+str(i+1),alive=int(i<y)) for i in range(8))
            actual,_=b.predict(prefix,5,['A1','B1'],x,k,common)
            parents=[-1,0 if common else -1,0 if common else -1,1,2]
            em=np.array([np.ones(3)]+[x**y*(1-x)**(8-y) for y in counts])
            ev,post=enumeration(parents,em,k);weights=f.normalize_weights(ev)
            for block,node in [('A',3),('B',4)]:
                expected=float(weights@np.sum(post[:,node]*(k@x),axis=1))
                err=abs(actual[block]-expected);assert err<1e-12;max_error=max(max_error,err);enum_checks+=1
    raw=f.load();x,k=f.kernel(100)
    rr=[r for r in raw if r['sheet']=='WT-L.csv'];tubes=sorted({r['tube'] for r in rr});isolation=0
    for time in (3,10,17):
        changed=copy.deepcopy(rr)
        for r in changed:
            if r['time']>=time:r.update(alive=1-r['alive'],condition='future-changed',parent='changed',replaced='changed')
        for common in (False,True):
            a,_=b.predict([r for r in rr if r['time']<time],time,tubes,x,k,common)
            c,_=b.predict([r for r in changed if r['time']<time],time,tubes,x,k,common)
            assert a==c;isolation+=1
    try:b.predict(rr,3,tubes,x,k,True)
    except AssertionError:pass
    else:raise AssertionError('Future rows accepted')
    tables={};row_checks=0;score_checks=0
    for grid in (50,100,200):
        j=json.loads((HERE/f'block-{grid}-results.json').read_text())
        for name,digest in j['bindings'].items():assert f.sha(HERE/name)==digest
        primary={(r['sheet'],r['node']):r for r in csv.DictReader((HERE/f'forecast-{grid}.csv').open())}
        table=list(csv.DictReader((HERE/f'block-{grid}.csv').open()));tables[grid]=table
        assert len(table)==3840
        for r in table:
            original=primary[r['sheet'],r['node']]
            assert all(r[key]==value for key,value in original.items())
            for model in b.BLOCK_MODELS:assert 0<float(r[model])<1
            row_checks+=1
        for batch in j['batches']:
            for obs in batch['observations']:
                sub=[r for r in raw if r['sheet']==batch['sheet'] and r['time']==obs['time'] and r['tube'].rstrip('0123456789')==obs['block']]
                assert obs['time']<batch['time'] and len(sub)==obs['n'] and sum(r['alive'] for r in sub)==obs['alive']
        for s in j['scores']:
            sub=[r for r in table if r['sheet']==s['sheet'] and int(r['cycle'])>=s['first_cycle'] and r['alive']!=''
                 and (not s['condition_zero_only'] or r['condition']=='0') and (not s['phase'] or int(r['phase'])==s['phase'])]
            assert len(sub)==s['n'];model=s['model']
            bs=math.fsum((float(r[model])-int(r['alive']))**2 for r in sub)/len(sub)
            ll=-math.fsum(math.log(float(r[model]) if r['alive']=='1' else 1-float(r[model])) for r in sub)/len(sub)
            assert abs(bs-s['brier'])<1e-13 and abs(ll-s['log_loss'])<1e-13;score_checks+=1
    sensitivity=[]
    for grid in (50,200):
        for model in b.BLOCK_MODELS:
            delta=max(abs(float(a[model])-float(c[model])) for a,c in zip(tables[grid],tables[100]))
            sensitivity.append(dict(grid=grid,model=model,max_probability_difference=delta))

    # Every selected cell and every inventory cohort is checked from raw XML.
    assays=xml_raw();idx={r['source_row']:r for r in assays}
    result=json.loads((HERE/'assay-transfer-results.json').read_text())
    for name,digest in result['bindings'].items():
        path=ARCHIVE if name==ARCHIVE.name else HERE/name;assert f.sha(path)==digest
    reading=list(csv.DictReader((HERE/'assay-transfer-reading.csv').open()))
    for row in reading:
        actual=idx[int(row['source_row'])]
        for key,v in actual.items():assert row[key]==('' if v is None else str(v)),(key,row,actual)
    assert len(reading)==485 and result['raw_rows']==len(assays)==3802
    cohorts=defaultdict(list)
    for r in assays:cohorts[r['Date'],r['Strain'],str(r['Size']).lower(),r['Phase']].append(r)
    assert len(result['cohorts'])==len(cohorts)==139
    for c in result['cohorts']:
        sub=cohorts[c['date'],c['strain'],c['size'],c['phase']]
        assert len(sub)==c['n'] and sum(r['Extinct']==0 for r in sub)==c['survived']
        assert c['conditions']==dict(Counter(str(r['Condition']) for r in sub))
        assert c['replacements']==dict(Counter(str(r['Replaced by']) for r in sub))
        assert c['source_rows']==[r['source_row'] for r in sub]
    phases={}
    for batch in result['focal_batches']:
        sub=[r for r in assays if r['Date']==batch['date'] and r['Strain']==batch['strain'] and str(r['Size']).lower()=='large']
        p={ph:{(str(r['Rack']),str(r['Tube'])):r for r in sub if r['Phase']==ph} for ph in (1,2)}
        phases[batch['date'],batch['strain']]=p
        survived={key for key,r in p[1].items() if r['Extinct']==0}
        assert len(p[1])==batch['n1'] and len(survived)==batch['survived1']
        assert len(p[2])==batch['n2'] and sum(r['Extinct']==0 for r in p[2].values())==batch['survived2']
        assert len(survived&p[2].keys())==batch['followed_original_survivors']
        assert [list(k) for k in sorted(survived-p[2].keys())]==batch['missing_original_survivors']
        assert [list(k) for k in sorted(p[2].keys()-survived)]==batch['later_nonoriginal_survivor_slots']
        assert sum(p[2][k]['Extinct']==0 for k in survived&p[2].keys())==batch['linked_final']
        joint=Counter(str(int(r['Mat']>0))+str(int(r['Count SM']>0)) for r in p[1].values())
        assert dict(joint)==batch['joint_mat_sm']
    # Confirm that the 2018 linked-original subset really was not replaced.
    early=phases['2018-05-22','PE-2-WT-A5']
    for key,r in early[1].items():
        if r['Extinct']==0:
            assert r['Replaced by']==0 and key in early[2]
        else:
            match=re.fullmatch(r'(.+?)([0-9]+)',str(r['Replaced by']))
            assert match is not None
            donor=match.group(1),match.group(2)
            assert early[1][donor]['Extinct']==0 and key in early[2]
    err=early[2]['V','6']
    assert early[1]['V','6']['Extinct']==0 and err['Condition']=='ERR' and err['Extinct']==1
    assert err['Count WS']=='NA' and err['Count SM']=='NA'
    for s in result['predictions']:
        assert s['training_date']<s['test_date']
        target=phases[s['test_date'],s['strain']]
        if s['phase']=='I':yy=[int(r['Extinct']==0) for r in target[1].values()]
        elif s['phase']=='II given I':yy=[int(r['Extinct']==0) for r in target[2].values()]
        else:yy=[int(k in target[2] and target[2][k]['Extinct']==0) for k in target[1]]
        assert all(r['Condition']==0 for ph in target.values() for r in ph.values())
        if s['training_date']=='2020-02-17':
            train=[r for r in assays if r['Date']==s['training_date'] and r['Phase']==1 and str(r['Size']).lower()=='large'
                   and r['Strain'] in ('PE-2-WT-A5','PE-2-WT-A5 mutL') and (s['model']=='pooled_february' or r['Strain']==s['strain'])]
            p=Fraction(1,2) if s['model']=='uninformative' else Fraction(1+sum(r['Extinct']==0 for r in train),2+len(train))
        else:
            train=phases[s['training_date'],s['strain']];alive={k for k,r in train[1].items() if r['Extinct']==0}
            ends=sum(train[2][k]['Extinct']==0 for k in alive)
            p1=Fraction(1+len(alive),2+len(train[1]));p2=Fraction(1+ends,2+len(alive))
            p={'I':p1,'II given I':p2,'cycle':p1*p2}[s['phase']]
            if s['model']=='2018_direct_cycle':p=Fraction(1+ends,2+len(train[1]))
        bs=sum((p-y)**2 for y in yy)/len(yy)
        assert abs(float(p)-s['probability'])<1e-14 and abs(float(bs)-s['brier'])<1e-13
        assert len(yy)==s['n'] and sum(yy)==s['observed_success']
        assert abs(float(p*len(yy))-s['predicted_success'])<1e-12
        ll=-math.fsum(math.log(float(p) if y else 1-float(p)) for y in yy)/len(yy)
        assert abs(ll-s['log_loss'])<1e-13
    assert result['missing_cycle_prediction']['status']=='not empirically calibrated'
    receipt=dict(status='passed',scope='Numerical block-model and source-bound assay checks, not a causal proof or independent research review.',
                 block_enumeration_comparisons=enum_checks,max_enumeration_error=max_error,future_isolation_cases=isolation,
                 forecast_rows_checked=row_checks,score_rows_checked=score_checks,block_grid_sensitivity=sensitivity,
                 original_assay_rows=3802,cohorts_checked=139,selected_reading_rows_checked=485,focal_batches_checked=len(result['focal_batches']),
                 original_and_replacement_transfer_slots_checked=48,
                 assay_predictions_checked=len(result['predictions']),
                 bindings={p.name:f.sha(p) for p in [HERE/'check_transfer.py',HERE/'TRANSFER-PROTOCOL.md',HERE/'assay_transfer.py',HERE/'forecast_blocks.py',HERE/'forecast_lineages.py',HERE/'check_forecast.py',HERE/'assay-transfer-results.json',HERE/'forecast-verification.json']+
                           [HERE/f'block-{g}-results.json' for g in (50,100,200)]})
    (HERE/'transfer-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
