#!/usr/bin/env python3
"""Independent reconstruction from the original XLSX XML; no producer imports.

Read-only workbook analysis. Participant, not bin, is the statistical unit.
Intervals are Student-t/Welch sampling-model intervals, not causal certificates.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import statistics
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import scipy
from scipy.stats import t

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'sources/29-motor-learning-cost-2026-10-06/cost_of_error_data.xlsx'
SOURCE_SHA = '0cd6ae5b0f159531f2442f49a474c5ecfda23a1fcf0965598da99df5d84891cc'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
# Literal published block labels, not reconstructed physical-side tags.
BLOCKS = {'EXP1': {'LARGE COST': 3, 'SMALL COST': 27},
          'EXP2': {'LARGE COST': 51, 'SMALL COST': 75}}
WINDOWS = {'pre': (52, 59, 801., 931.),
           'early': (62, 69, 971., 1100.),
           'late': (70, 78, 1101., 1250.)}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def col(number: int) -> str:
    result = ''
    while number:
        number, rem = divmod(number - 1, 26)
        result = chr(65 + rem) + result
    return result


def summary(values: list[float]) -> dict:
    n = len(values)
    mean = math.fsum(values) / n
    sd = statistics.stdev(values)
    se = sd / math.sqrt(n)
    width = float(t.ppf(.975, n - 1)) * se
    return {'n': n, 'mean': mean, 'sd': sd, 'se': se,
            'df': n - 1, 'ci95': [mean - width, mean + width]}


def welch(a: list[float], b: list[float]) -> dict:
    va, vb = statistics.variance(a)/len(a), statistics.variance(b)/len(b)
    effect = statistics.mean(a) - statistics.mean(b)
    se = math.sqrt(va + vb)
    df = (va + vb)**2 / (va**2/(len(a)-1) + vb**2/(len(b)-1))
    width = float(t.ppf(.975, df)) * se
    return {'n_exp2': len(a), 'n_exp1': len(b), 'mean': effect,
            'se': se, 'df': df, 'ci95': [effect-width, effect+width]}


def main() -> None:
    source = SOURCE.read_bytes()
    assert digest(source) == SOURCE_SHA, 'Source workbook bytes changed'
    with ZipFile(SOURCE) as archive:
        strings = [''.join(si.itertext()) for si in
                   ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        book = ET.fromstring(archive.read('xl/workbook.xml'))
        sheet_names = [n.attrib['name'] for n in book.findall('s:sheets/s:sheet', NS)]
        assert sheet_names == ['ADAPTATION', 'DECISION'], sheet_names
        tree = ET.fromstring(archive.read('xl/worksheets/sheet1.xml'))
        cells = {}
        formula_cells = set()
        for node in tree.findall('s:sheetData/s:row/s:c', NS):
            address = node.attrib['r']
            if node.find('s:f', NS) is not None:
                formula_cells.add(address)
            value = node.find('s:v', NS)
            if value is None:
                continue
            cells[address] = strings[int(value.text)] if node.attrib.get('t') == 's' else float(value.text)
    source_cells = {}
    window_means = {}
    coords = {}
    metadata = {}
    for cohort, blocks in BLOCKS.items():
        window_means[cohort] = {}
        for condition, head in blocks.items():
            assert cells[f'A{head}'] == cohort
            assert cells[f'C{head}'] == condition
            assert cells[f'D{head}'] == 'ADAPTATION'
            assert cells[f'B{head+2}'] == 'ID'
            assert cells[f'C{head+2}'] == 'TRIAL NUM'
            label = f'{cohort}/{condition}'
            coords[label] = {}
            metadata[label] = {'header_row': head, 'participants': []}
            dest = window_means[cohort][condition] = {}
            for row in range(head+3, head+23):
                participant = cells[f'B{row}']
                assert participant.is_integer() and 1 <= participant <= 20
                participant = int(participant)
                assert participant not in dest, (label, participant)
                assert cells[f'A{row}'] == (1 if condition == 'LARGE COST' else 2)
                dest[participant] = {}
                metadata[label]['participants'].append(participant)
                for window, (first, last, lower, upper) in WINDOWS.items():
                    addresses = [f'{col(c)}{row}' for c in range(first, last+1)]
                    values = [cells.get(a) for a in addresses]
                    assert all(isinstance(v, float) and math.isfinite(v) for v in values), (label, participant, window)
                    assert not formula_cells.intersection(addresses)
                    times = [cells[f'{col(c)}{head+2}'] for c in range(first,last+1)]
                    assert all(lower <= x <= upper for x in times), (label, window, times)
                    coords[label][window] = times
                    source_cells.update(zip(addresses, values))
                    dest[participant][window] = math.fsum(values)/len(values)
            assert set(dest) == set(range(1,21)), (label, set(dest))
    participants, aggregates, contrasts = {}, {}, {}
    for cohort in BLOCKS:
        participants[cohort] = []
        aggregates[cohort] = {}
        contrasts[cohort] = {}
        for participant in range(1,21):
            means = {c: window_means[cohort][c][participant] for c in BLOCKS[cohort]}
            deltas = {c: {w: means[c][w]-means[c]['pre'] for w in ('early','late')}
                      for c in BLOCKS[cohort]}
            opposed = {w: deltas['SMALL COST'][w]-deltas['LARGE COST'][w]
                       for w in ('early','late')}
            participants[cohort].append({'id': participant, 'window_means': means,
                                        'deltas': deltas, 'opposed_contrasts': opposed})
        for window in ('early','late'):
            contrasts[cohort][window] = [x['opposed_contrasts'][window] for x in participants[cohort]]
            aggregates[cohort][window] = {
                'opposed': summary(contrasts[cohort][window]),
                'initial_small_change': summary([x['deltas']['SMALL COST'][window] for x in participants[cohort]]),
                'initial_large_change': summary([x['deltas']['LARGE COST'][window] for x in participants[cohort]])}
    between = {w: welch(contrasts['EXP2'][w], contrasts['EXP1'][w]) for w in ('early','late')}
    result = {'status':'computed independently; producer comparison pending',
              'scope':'Secondary paired binned-amplitude analysis, literal source labels; no raw-trial, latent-gain or physical-updater identification.',
              'producer_imported':False, 'producer_code_inspected':False,
              'source_sha256':SOURCE_SHA,
              'protocol_sha256':digest((HERE/'PROTOCOL.md').read_bytes()),
              'checker_sha256':digest(Path(__file__).read_bytes()),
              'versions':{'python':sys.version.split()[0], 'scipy':scipy.__version__},
              'counts':{'cohorts':2,'participants_per_cohort':20,'condition_rows':80,
                        'source_amplitude_cells':len(source_cells),'participant_window_means':240,
                        'opposed_participant_contrasts':80,'between_cohort_contrasts':2},
              'metadata':metadata, 'mean_trial_coordinates':coords,
              'source_amplitude_cells':source_cells,
              'participants':participants,'aggregate':aggregates,'between_cohort':between}
    assert len(source_cells) == 2000
    (HERE/'independent-results.json').write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print(json.dumps({'counts':result['counts'],'primary':aggregates['EXP2']['early']['opposed'],
                      'secondary_between':between},indent=2))


if __name__ == '__main__':
    main()
