#!/usr/bin/env python3
"""Audit the published replication table without applying unreported exclusions."""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import statistics
import xml.etree.ElementTree as ET
import zipfile
import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SOURCE = ROOT/'sources/biological-scale-correspondence/inheritance-replication'
PATH = SOURCE/'elife-107034-supp1-v1.xlsx'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def stats(a): return dict(n=len(a),mean=statistics.mean(a),sd=statistics.stdev(a))

for item in json.loads((SOURCE/'manifest.json').read_text())['files']:
    p=SOURCE/item['file'];assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
wb=openpyxl.load_workbook(PATH,data_only=True,read_only=True)
sheet=wb['Table B']
numeric={c.coordinate:float(c.value) for row in sheet for c in row if isinstance(c.value,(int,float))}
with zipfile.ZipFile(PATH) as z:
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    sheets=ET.fromstring(z.read('xl/workbook.xml'))
    rels={e.attrib['Id']:e.attrib['Target'] for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    node=next(e for e in sheets.findall('s:sheets/s:sheet',ns) if e.attrib['name']=='Table B')
    target=rels[node.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
    member=target.lstrip('/') if target.startswith('/') else 'xl/'+target
    xml={c.attrib['r']:float(c.find('s:v',ns).text) for c in ET.fromstring(z.read(member)).findall('.//s:c',ns)
         if c.attrib.get('t','n')=='n' and c.find('s:v',ns) is not None}
    assert xml==numeric
rows=[];groups=defaultdict(list)
for i,values in enumerate(sheet.iter_rows(min_row=2,values_only=True),2):
    generation,trial,assay,pa14,op50,supplied=values
    assert all(isinstance(v,int) and v>=0 for v in [pa14,op50]) and pa14+op50>0
    index=(op50-pa14)/(op50+pa14)
    tolerance=.05 if generation=='F1' else .005
    assert abs(index-supplied)<=tolerance+1e-12
    row=dict(source_row=i,generation=generation,trial=trial,assay=assay,pa14=pa14,op50=op50,
             supplied_index=supplied,recomputed_index=index,rounding_difference=index-supplied)
    rows.append(row);groups[(generation,trial)].append(row)
generations=['Naïve','Trained','F1','F2']
summary={g:stats([r['recomputed_index'] for r in rows if r['generation']==g]) for g in generations}
trials={str(t):{g:stats([r['recomputed_index'] for r in groups[g,t]]) for g in generations}
        for t in range(1,5)}
contrasts={str(t):{g:trials[str(t)][g]['mean']-trials[str(t)]['Naïve']['mean']
                  for g in generations if g!='Naïve'} for t in range(1,5)}
sequence_a=groups['Naïve',4];sequence_b=groups['Trained',3]
assert len(sequence_a)==len(sequence_b)==10
assert [(r['pa14'],r['op50']) for r in sequence_a]==[(r['op50'],r['pa14']) for r in sequence_b]
record=dict(status='audit_completed_with_unresolved_source_discrepancies',
    generated_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(Path(__file__)),
    plan_sha256=sha(HERE/'replication-plan.json'),source_sha256=sha(PATH),
    numeric_cells_cross_checked=len(numeric),raw_n=len(rows),summary=summary,trials=trials,contrasts=contrasts,
    equal_trial_mean_contrasts={g:statistics.mean(contrasts[str(t)][g] for t in range(1,5))
                               for g in ['Trained','F1','F2']},
    published_counts=dict(figure_after_exclusions={'Naïve':38,'Trained':38,'F1':19,'F2':43},
                          methods_before_exclusions=143,methods_excluded=5),
    source_issues=[dict(issue='Table B has 145 assay rows, versus 143 before exclusion stated in methods and 138 after exclusion in Figure 1. No exclusion mask is supplied; no rows discarded here.'),
                   dict(issue='An entire ten-assay count sequence reappears with PA14/OP50 columns exchanged between Naïve trial 4 and Trained trial 3.',
                        first_rows=[r['source_row'] for r in sequence_a],second_rows=[r['source_row'] for r in sequence_b],
                        inference='The source alone does not identify why. Preserve and flag; do not allege intent or treat the two sequences as established independent measurements.')],
    rows=rows,scope='Recalculation of supplied table, not an experimental replication, resolved source correction, new inferential significance test, or verification of Pv1 and F4 inheritance.')
(HERE/'replication-results.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
wb.close()
print(json.dumps({k:record[k] for k in ['status','raw_n','summary','contrasts','source_issues']},indent=2,ensure_ascii=False))
