"""Independent XLSX XML extraction and backward ancestry/assay checks."""
from collections import Counter
import csv
from datetime import datetime, timedelta
from fractions import Fraction
from io import BytesIO
import hashlib
import itertools
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SOURCE=ROOT/'sources/evolutionary-selection/doulcier-2025'
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def workbook(raw):
    with ZipFile(BytesIO(raw)) as z:
        strings=[''.join(s.itertext()) for s in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',NS)]
        rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        output={}
        for sheet in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',NS):
            rid=sheet.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            target=rels[rid].lstrip('/');target=target if target.startswith('xl/') else 'xl/'+target
            rows={}
            for row in ET.fromstring(z.read(target)).findall('s:sheetData/s:row',NS):
                values={}
                for c in row.findall('s:c',NS):
                    v=c.find('s:v',NS)
                    if v is None:continue
                    value=strings[int(v.text)] if c.get('t')=='s' else Fraction(v.text)
                    if isinstance(value,Fraction):value=int(value) if value.denominator==1 else float(value)
                    values[''.join(x for x in c.get('r') if x.isalpha())]=value
                rows[int(row.get('r'))]=values
            output[sheet.get('name')]=rows
        return output


manifest=json.loads((SOURCE/'manifest.json').read_text())
for f in manifest['files']:
    b=(SOURCE/f['file']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256']
archive=SOURCE/'lce-genealogies-code-and-data.zip'
assert 'md5:'+hashlib.md5(archive.read_bytes()).hexdigest()==manifest['published_archive_md5']
with ZipFile(archive) as z:
    counts=workbook(z.read('lce-genealogies-main/raw/19-09-27/Counts_final.xlsx'))
    assays=workbook(z.read('lce-genealogies-main/raw/24-04-03/Lifecycle fitness tests.xlsx'))['raw']
result=json.loads((HERE/'lineage-results.json').read_text())
readings=list(csv.DictReader((HERE/'genealogy-reading.csv').open()))
assert len(readings)==3808
for e in readings:
    r=counts[e['sheet']][int(e['source_row'])]
    for k,col in [('mat','E'),('count_ws','F'),('count_sm','G'),('extinct','I'),('replaced','J'),('condition','K')]:
        assert e[k]==str(r[col]),(k,e,r)
    assert int(e['cycle'])==r['C']+1 and int(e['phase'])==r['D']
for sheet,rows in counts.items():
    index={(2*r['C']+r['D'],r['A']+str(r['B'])):r for i,r in rows.items() if i>1 and r['K']!='MISS'}
    terminal=[key for key,r in index.items() if key[0]==20 and r['I']==0]
    saved=result['treatments'][sheet]
    assert len(index)==saved['retained_nodes'] and len(terminal)==saved['terminal_viable_nodes']
    exported={e['node']:e for e in readings if e['sheet']==sheet}
    for (t,tube),r in index.items():
        expected=''
        if t>1 and (t-1,tube) in index:
            previous=index[t-1,tube];donor=tube if previous['J']==0 else previous['J']
            if (t-1,donor) in index:
                assert index[t-1,donor]['I']==0
                expected=f'{t-1}:{donor}'
        assert exported[f'{t}:{tube}']['parent']==expected
    paths=[];founders=Counter()
    for current in terminal:
        path=[]
        while True:
            t,tube=current;path.append(f'{t}:{tube}')
            if t==1:founders[path[-1]]+=1;break
            prior=index.get((t-1,tube))
            if prior is None:founders['unresolved']+=1;break
            donor=tube if prior['J']==0 else prior['J']
            if (t-1,donor) not in index:founders['unresolved']+=1;break
            current=t-1,donor
        paths.append(set(path))
    assert dict(founders)==saved['terminal_founder_counts']
    assert set.intersection(*paths)==set(saved['terminal_common_ancestors'])
    assert sum('4:A5' in p for p in paths)==saved['descendants_of_2_II_A5']
    for t in range(1,21):
        rr=[r for (time,_),r in index.items() if t==time]
        assert saved['phase_counts'][str(t)]==dict(observed=len(rr),survived=sum(r['I']==0 for r in rr),flagged=sum(r['K']!=0 for r in rr))
date_serial=(datetime(2020,6,2)-datetime(1899,12,30)).days
assay_reading=list(csv.DictReader((HERE/'linked-assay-reading.csv').open()))
assert len(assay_reading)==222
for entry in assay_reading:
    r=assays[int(entry['source_row'])]
    assert r['A']==date_serial and entry['Date']=='2020-06-02 00:00:00'
    for name,col in [('Strain','B'),('Size','C'),('Rack','D'),('Tube','E'),('Phase','F'),('Mat','G'),('Count WS','H'),('Count SM','I'),('Count FZ','J'),('Extinct','K'),('Replaced by','L'),('Condition','M')]:
        assert entry[name]==str(r[col])
focal={}
for strain in ('PE-2-WT-A5','PE-2-WT-A5 mutL'):
    rr=[r for i,r in assays.items() if i>1 and r.get('A')==date_serial and r.get('B')==strain and str(r.get('C')).lower()=='large']
    phase1={(r['D'],r['E']):r for r in rr if r['F']==1}
    phase2={(r['D'],r['E']):r for r in rr if r['F']==2}
    assert len(phase1)==72 and all(r['M']==0 and r['L']=='NA' for r in rr)
    assert set(phase2)=={k for k,r in phase1.items() if r['K']==0}
    finished=sum(r['K']==0 for r in phase2.values());saved=result['focal_assay'][strain]
    assert (72,len(phase2),finished)==(saved['initial'],saved['phase1_survived'],saved['phase2_survived'])
    rackcounts=[]
    for rack in range(1,10):
        d=dict(rack=rack,start=sum(k[0]==rack for k in phase1),phase1_survived=sum(k[0]==rack for k in phase2),cycle_completed=sum(k[0]==rack and r['K']==0 for k,r in phase2.items()))
        assert d==saved['racks'][rack-1];rackcounts.append(d['cycle_completed'])
    focal[strain]=rackcounts
ancestor=[r for i,r in assays.items() if i>1 and r.get('B')=='Line-17 mutS' and str(r.get('C')).lower()=='large' and r.get('F')==1]
table=Counter(f'{int(r["G"]>0)}{int(r["I"]>0)}' for r in ancestor if isinstance(r['I'],(int,float)))
assert dict(table)==result['ancestral_phase1']['known_table']=={'11':28,'10':22,'01':130,'00':3}
assert len(ancestor)==184
assert len([r for r in ancestor if r['I']=='NA' and r['G']==1 and r['M']=='CONT'])==1
def near(a,b):assert abs(a-float(b))<1e-12
near(result['matched_date_risk_difference'],Fraction(35,72));near(result['matched_date_ratio'],6)
deltas=[Fraction(42-a,64)-Fraction(7-b,64) for a,b in itertools.product(*focal.values())]
for a,b in zip(result['delete_one_rack_each_difference_range'],[min(deltas),max(deltas)]):near(a,b)
phase=result['ancestral_phase1'];near(phase['complete_joint_fraction'],Fraction(28,183));near(phase['complete_marginal_product'],Fraction(50*158,183**2))
for a,b in zip(phase['full_record_joint_range'],[Fraction(28,184),Fraction(29,184)]):near(a,b)
for a,b in zip(phase['full_record_marginal_product_range'],[Fraction(51*158,184**2),Fraction(51*159,184**2)]):near(a,b)
receipt=dict(status='passed',original_files_verified=3,publisher_archive_md5_verified=True,
             source_genealogy_nodes=3808,observed_parent_links_checked=sum(x['observed_parent_edges'] for x in result['treatments'].values()),
             backward_terminal_paths=sum(x['terminal_viable_nodes'] for x in result['treatments'].values()),
             linked_assay_initial_cultures=144,assay_rows=222,scope='Independent raw-XML extraction, all recorded parent links, backward terminal ancestry, and matched-date linked fates. No new biological experiment or genomic/Bayesian replication.',
             files_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE/'analyze_lineages.py',Path(__file__),HERE/'lineage-results.json',HERE/'genealogy-reading.csv',HERE/'linked-assay-reading.csv',HERE/'missing-reading.json',SOURCE/'manifest.json']})
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
