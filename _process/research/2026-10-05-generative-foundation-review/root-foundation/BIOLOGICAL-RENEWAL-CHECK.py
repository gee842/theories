#!/usr/bin/env python3
"""Owned-scope source/arithmetic/document checks, not an independent review."""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
from urllib.parse import unquote
import csv
import hashlib
import importlib.util
import io
import json
import math
import re
import statistics
import xml.etree.ElementTree as ET
import zipfile

P=Path(__file__).resolve().parent
R=P.parents[3]
E=R/'experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/renewal'
S=R/'sources/biological-scale-correspondence'
T=R/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
A=R/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def near(a,b,tol=1e-9):assert math.isclose(a,b,rel_tol=tol,abs_tol=tol),(a,b)

def worksheets(path):
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(path) as z:
        rels={e.attrib['Id']:e.attrib['Target'] for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            shared=[''.join(e.itertext()) for e in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        result={}
        for sheet in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns):
            target=rels[sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
            target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            cells={}
            for c in ET.fromstring(z.read(target)).findall('.//s:c',ns):
                v=c.find('s:v',ns)
                if v is not None and v.text:
                    cells[c.attrib['r']]=shared[int(v.text)] if c.attrib.get('t')=='s' else float(v.text)
                elif c.attrib.get('t')=='inlineStr':
                    cells[c.attrib['r']]=''.join(c.find('s:is',ns).itertext())
            result[sheet.attrib['name']]=cells
        return result

def check_summary(values,s):
    assert len(values)==s['n']
    near(statistics.mean(values),s['mean']);near(statistics.stdev(values),s['sd'])
    if 'median' in s:
        near(statistics.median(values),s['median'])
        ordered=sorted(values)
        for q,key in [(.25,'q25'),(.75,'q75')]:
            pos=(len(ordered)-1)*q;lo=int(pos)
            near(ordered[lo]+(ordered[min(lo+1,len(ordered)-1)]-ordered[lo])*(pos-lo),s[key])

for directory in ['pgen-1011178','boddu-2025','inheritance-replication']:
    for item in json.loads((S/directory/'manifest.json').read_text())['files']:
        p=S/directory/item['file']
        assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
results=json.loads((E/'results.json').read_text())
assert results['status']=='passed'
assert results['script_sha256']==sha(E/'analyze_renewal.py')
assert results['plan_sha256']==sha(E/'analysis-plan.json')
for name,h in results['inputs'].items():assert sha(R/name)==h
sheets=worksheets(S/'pgen-1011178/pgen.1011178.s005.xlsx')
assert sum(isinstance(v,float) for s in sheets.values() for v in s.values())==6503
for panel in results['memory']['panels'].values():
    for group in panel['groups'].values():
        values=[sheets[panel['sheet']][c] for c in group['cells']]
        assert values==group['values'];check_summary(values,group)
    g=panel['groups']
    if 'trained_to_control_ratio' in panel:
        near(panel['trained_to_control_ratio'],g['GRb0427']['mean']/g['OP50']['mean'])
        near(panel['trained_minus_control'],g['GRb0427']['mean']-g['OP50']['mean'])
    if 'Pv1_minus_empty' in panel:
        for strain,value in panel['Pv1_minus_empty'].items():near(value,g[strain+'_Pv1']['mean']-g[strain+'_empty']['mean'])
    if 'mean_minus_control' in panel:
        control=next(iter(g))
        for name,value in panel['mean_minus_control'].items():near(value,g[name]['mean']-g[control]['mean'])
for gen,value in results['memory']['panels']['choice_generations']['trained_minus_control'].items():
    g=results['memory']['panels']['choice_generations']['groups']
    near(value,g[gen+'_GRb0427']['mean']-g[gen+'_OP50']['mean'])
assert 'J299' in g['F4_GRb0427']['cells']

archive=S/'boddu-2025/varianceinwormgut-v1.0.0.zip'
with zipfile.ZipFile(archive) as z:
    csvs={}
    for name,meta in results['archive_members'].items():
        raw=z.read(name);assert len(raw)==meta['bytes'] and hashlib.sha256(raw).hexdigest()==meta['sha256']
        csvs[Path(name).name]=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
cal=results['calibration'];raw=csvs['CFU Mapping.csv']
assert len(raw)==169 and len(cal['training'])==70 and len(cal['test'])==96 and len(cal['zero_cfu_excluded'])==3
assert len({v['csv_line'] for v in cal['training']+cal['test']+cal['zero_cfu_excluded']})==169
abc=cal['inverse_tanh']['parameters_abc'];a,b,c=abc
assert a>cal['inverse_tanh']['lower_a'] and a<100 and c>0
for split in ['training','test']:
    rows=cal[split]
    assert all(v['time']==('T48' if split=='training' else 'T72') for v in rows)
    for row in rows:
        src=raw[row['csv_line']-2]
        assert row['green']==float(src['Green']) and row['cfu']==float(src['CFU/worm'])
        assert row['time']==src['Time'] and row['condition']==src['Condition']
        x=math.log10(row['green']);y=math.log10(row['cfu'])
        near(x,row['log10_green']);near(y,row['log10_cfu'])
        p=row['predictions'];near(p['constant'],cal['constant'])
        near(p['linear'],cal['linear_intercept_slope'][0]+cal['linear_intercept_slope'][1]*x)
        near(p['inverse_tanh'],b+c*math.atanh(x/a))
    sets={'training':rows} if split=='training' else {'all':rows,'common_conditions':[v for v in rows if v['condition']!='CM25'],'added_CM25':[v for v in rows if v['condition']=='CM25']}
    for model in cal['scores']:
        for name,sub in sets.items():
            s=cal['scores'][model]['training'] if split=='training' else cal['scores'][model]['test'][name]
            errors=[v['predictions'][model]-v['log10_cfu'] for v in sub]
            assert s['n']==len(sub) and s['domain_failures']==0
            near(s['rmse'],math.sqrt(statistics.mean(e*e for e in errors)))
            near(s['mae'],statistics.mean(abs(e) for e in errors));near(s['bias'],statistics.mean(errors))
for row in cal['zero_cfu_excluded']:assert float(raw[row['csv_line']-2]['CFU/worm'])==0 and row['log10_cfu'] is None
xs=[v['log10_green'] for v in cal['training']];ys=[v['log10_cfu'] for v in cal['training']]
near(cal['constant'],statistics.mean(ys))
cov=sum((x-statistics.mean(xs))*(y-statistics.mean(ys)) for x,y in zip(xs,ys))
var=sum((x-statistics.mean(xs))**2 for x in xs)
near(cal['linear_intercept_slope'][1],cov/var)
near(cal['linear_intercept_slope'][0],statistics.mean(ys)-cov/var*statistics.mean(xs))
assert all(v['success'] and v['gradient_max']<1e-3 for v in cal['inverse_tanh']['starts'])
assert max(v['training_sse'] for v in cal['inverse_tanh']['starts'])-min(v['training_sse'] for v in cal['inverse_tanh']['starts'])<1e-7
predictions=list(csv.DictReader((E/'calibration-predictions.csv').open()))
assert len(predictions)==166
for csvrow,row in zip(predictions,cal['training']+cal['test']):
    assert int(csvrow['csv_line'])==row['csv_line']
    for name,v in row['predictions'].items():near(float(csvrow[name]),v)

for run,name in zip(results['migration'],['Migration_Compiled.csv','Migration_run2_Compiled.csv']):
    raw=csvs[name];assert len(raw)==run['total_records']
    for group in run['groups']:
        lines=[i for i,row in enumerate(raw,2) if row['Time']==group['time'] and row['Condition']==group['condition']]
        assert lines==group['csv_lines']
        values=[float(raw[i-2]['Green']) for i in lines]
        check_summary(values,group['raw_green']);check_summary([math.log10(v) for v in values],group['log10_green'])
    for duplicate in run['duplicated_baselines']:
        group=lambda sign:[{k:v for k,v in row.items() if k!='Condition'} for row in raw if row['Time']=='T0' and row['Condition']==duplicate['initial']+' '+sign]
        assert group('+')==group('-') and len(group('+'))==duplicate['repeated_rows']
assert sum(v['repeated_rows'] for run in results['migration'] for v in run['duplicated_baselines'])==694

rep=json.loads((E/'replication-results.json').read_text())
assert rep['status']=='audit_completed_with_unresolved_source_discrepancies'
assert rep['script_sha256']==sha(E/'analyze_replication.py') and rep['plan_sha256']==sha(E/'replication-plan.json')
path=S/'inheritance-replication/elife-107034-supp1-v1.xlsx';assert rep['source_sha256']==sha(path)
cells=worksheets(path)['Table B'];assert sum(isinstance(v,float) for v in cells.values())==725
assert len(rep['rows'])==145
for row in rep['rows']:
    i=row['source_row'];assert row['pa14']==cells[f'D{i}'] and row['op50']==cells[f'E{i}']
    assert row['generation']==cells[f'A{i}'] and row['trial']==cells[f'B{i}']
    near(row['recomputed_index'],(row['op50']-row['pa14'])/(row['op50']+row['pa14']))
for gen,s in rep['summary'].items():check_summary([r['recomputed_index'] for r in rep['rows'] if r['generation']==gen],s)
for t,groups in rep['trials'].items():
    for gen,s in groups.items():check_summary([r['recomputed_index'] for r in rep['rows'] if r['generation']==gen and str(r['trial'])==t],s)
    for gen,v in rep['contrasts'][t].items():near(v,groups[gen]['mean']-groups['Naïve']['mean'])
for i,j in zip(range(32,42),range(64,74)):assert cells[f'D{i}']==cells[f'E{j}'] and cells[f'E{i}']==cells[f'D{j}']

# Rebind the old proof at its actual checked scope, without recompilation.
proof=json.loads((A/'organized-scale-verification.json').read_text());archive=A/proof['archive']
assert proof['status']=='passed' and proof['new_audits']==26 and proof['replayed_inherited_audits']==77
assert (archive/'receipt.json').read_bytes()==(A/'organized-scale-verification.json').read_bytes()
for module in proof['modules']:
    name=module['module'];source=A/(name+'.lean')
    if name=='SystemsOrganization':source=A.parent/(name+'.lean')
    if name=='GenerativeCore':source=A.parent.parent/(name+'.lean')
    assert sha(source)==sha(archive/'sources'/(name+'.lean'))==module['source_sha256']
    assert sha(archive/(name+'.txt'))==module['output_sha256'] and module['passed']

spec=importlib.util.spec_from_file_location('chain',P/'build_generative_chain.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
docs=[P/'BIOLOGICAL-RENEWAL-INTEGRATION.md',P/'BIOLOGICAL-JOINT-VALIDATION.md',P/'BIOLOGICAL-CONTINUATION-INTEGRATION.md',
      E/'README.md',T/'RELATIONS-ACROSS-SCALES.md',R/'sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md']
docs += [S/d/'README.md' for d in ['pgen-1011178','boddu-2025','inheritance-replication']]
links=[]
for p in docs:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if re.match('[a-z]+:',target):continue
        filename,_,anchor=unquote(target).partition('#');dest=(p.parent/filename).resolve() if filename else p
        assert dest.exists(),(p,target)
        assert not anchor or anchor in m.heading_ids(dest),(p,target)
        links.append(dict(source=str(p.relative_to(R)),target=target))
data=m.read_data();edits=json.loads((P/'BIOLOGICAL-RENEWAL-INDEX-EDITS.json').read_text())
entries={e['id']:e for s in data['sections'] for e in s['entries']};rendered=m.render(data);saved=m.OUTPUT.read_text()
for ident,entry in edits['after'].items():
    assert entries[ident]==entry
    row=next(line for line in rendered.splitlines() if line.startswith('| '+ident+' |'));assert row in saved
for p in docs[:3]:assert data['reviewed_sources'][str(p.relative_to(R))]==sha(p)
record=dict(status='passed',checked_at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(Path(__file__)),
    scope='Original bytes; separate stdlib/XML source and arithmetic checks; owned links and paired C29/F21; unchanged old Lean bindings. Not new proof compilation, independent review, biological replication, or whole-table certification.',
    source_issues_remain=True,full_biological_validation='incomplete',links=links,
    counts=dict(pv1_numeric_cells=6503,matched_calibration_records=169,positive_training=70,positive_test=96,
                migration_rows=3594,repeated_baseline_entries=694,replication_raw_assays=145,new_theorems=0),
    bindings={str(p.relative_to(R)):sha(p) for p in docs+list(E.glob('*.py'))+list(E.glob('*.json'))+list(E.glob('*.csv'))+list(E.glob('*.png'))+list(E.glob('*.svg'))+[A/'organized-scale-verification.json']},
    global_chain_pending=m.changes(data))
(P/'BIOLOGICAL-RENEWAL-CHECKS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='passed',links=len(links),counts=record['counts'],full_validation='incomplete',global_chain_pending=record['global_chain_pending']),ensure_ascii=False,indent=2))
