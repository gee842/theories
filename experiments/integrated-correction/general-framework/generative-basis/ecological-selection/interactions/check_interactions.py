"""Independent stdlib XLSX/XML and rational-arithmetic check, not a second experiment."""
from collections import defaultdict
import csv
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = ROOT / 'sources/evolutionary-selection/driscoll-2017'
BOOK = SOURCE / '41467_2017_BFncomms15707_MOESM80_ESM.xlsx'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
result = json.loads((HERE / 'interaction-results.json').read_text())
errors = []


def near(actual, expected):
    error = abs(float(actual)-float(expected))
    errors.append(error)
    assert error < 1e-10, (actual, expected, error)


def average(xs):
    return sum(xs, F(0))/len(xs)


manifest = json.loads((SOURCE / 'manifest.json').read_text())
for entry in manifest['files']:
    b = (SOURCE / entry['file']).read_bytes()
    assert len(b) == entry['bytes']
    assert hashlib.sha256(b).hexdigest() == entry['sha256']
assert hashlib.sha256(BOOK.read_bytes()).hexdigest() == result['source_sha256']
with ZipFile(BOOK) as z:
    strings = [''.join(el.itertext()) for el in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si', NS)]
    workbook = ET.fromstring(z.read('xl/workbook.xml'))
    sheet = next(el for el in workbook.findall('s:sheets/s:sheet', NS) if el.get('name') == 'Mean cluster velocity')
    rid = sheet.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
    relation = next(el for el in ET.fromstring(z.read('xl/_rels/workbook.xml.rels')) if el.get('Id') == rid)
    path = relation.get('Target').lstrip('/')
    if not path.startswith('xl/'):
        path = 'xl/' + path
    cells = {}
    for cell in ET.fromstring(z.read(path)).findall('.//s:c', NS):
        value = cell.find('s:v', NS)
        if value is not None:
            cells[cell.get('r')] = strings[int(value.text)] if cell.get('t') == 's' else F(value.text)

records = list(csv.DictReader((HERE / 'video-means.csv').open()))
assert len(records) == 54
raw = defaultdict(lambda: defaultdict(list))
for row, exported in zip(range(2, 56), records):
    species, medium = cells[f'A{row}'], cells[f'B{row}']
    density, replicate, video = [int(cells[f'{col}{row}']) for col in 'CDE']
    speed = cells[f'F{row}']
    assert int(exported['source_row']) == row
    assert (exported['species'], exported['medium']) == (species, medium)
    assert [int(exported[k]) for k in ('density_percent','technical_replicate','video')] == [density,replicate,video]
    near(exported['mean_velocity_mm_min'],speed)
    raw[f'{species}|{medium}|{density}'][replicate].append(speed)

means, omitted = {}, {}
for key, reps in raw.items():
    assert set(reps) == {1,2,3} and all(len(v) == 3 for v in reps.values())
    repmeans = [average(reps[i]) for i in (1,2,3)]
    means[key] = average(repmeans)
    omitted[key] = [(sum(repmeans)-x)/2 for x in repmeans]
    saved = result['groups'][key]
    assert saved['video_count'] == 9 and saved['technical_replicate_count'] == 3
    near(saved['mean_mm_min'],means[key])
    near(saved['replicate_mean_sd_mm_min'],math.sqrt(float(sum((x-means[key])**2 for x in repmeans)/2)))
    for a,b in zip(saved['replicate_means_mm_min'],repmeans):near(a,b)
    for a,b in zip(saved['replicate_mean_range_mm_min'],[min(repmeans),max(repmeans)]):near(a,b)
    for a,b in zip(saved['leave_one_replicate_out_means_mm_min'],omitted[key]):near(a,b)
assert set(raw) == set(result['groups']) and len(raw) == 6
for c in result['contrasts'].values():
    high, low = c['high'], c['low']
    near(c['mean_difference_mm_min'],means[high]-means[low])
    near(c['ratio_of_means'],means[high]/means[low])
    gap=min(average(v) for v in raw[high].values())-max(average(v) for v in raw[low].values())
    near(c['min_high_rep_minus_max_low_rep_mm_min'],gap)
    differences = [a-b for a,b in itertools.product(omitted[high],omitted[low])]
    for a,b in zip(c['delete_one_each_condition_difference_range_mm_min'],[min(differences),max(differences)]):near(a,b)
khi,klo,shi,slo = 'K. lactis|YPD|100','K. lactis|YPD|5','S. cerevisiae|YPD|100','S. cerevisiae|YPD|5'
near(result['species_by_density_difference_mm_min'],means[khi]-means[klo]-means[shi]+means[slo])
differences = [a-b-c+d for a,b,c,d in itertools.product(omitted[khi],omitted[klo],omitted[shi],omitted[slo])]
assert len(differences) == 81
for a,b in zip(result['delete_one_each_condition_interaction_range_mm_min'],[min(differences),max(differences)]):near(a,b)
receipt = dict(status='passed',original_files_verified=len(manifest['files']),
               videos=54,technical_replicates=18,conditions=6,checked_numeric_values=len(errors),
               max_absolute_difference=max(errors),interaction_deletions=81,
               scope='Independent XML extraction and exact-decimal rational arithmetic; no independent biological replication, statistical population inference or mathematical theorem.',
               files_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                             [HERE/'analyze_interactions.py',Path(__file__),HERE/'interaction-results.json',HERE/'video-means.csv',SOURCE/'manifest.json']})
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
