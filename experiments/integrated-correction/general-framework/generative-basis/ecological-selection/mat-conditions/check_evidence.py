#!/usr/bin/env python3
"""Separate extraction and source-binding checks, not a biological replication."""
import csv
import hashlib
from html import unescape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / 'sources/evolutionary-selection/koza-2011/article.html'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    html = SOURCE.read_text()
    manifest = json.loads((SOURCE.parent / 'manifest.json').read_text())
    assert sha(SOURCE) == manifest['files'][0]['sha256']
    assert SOURCE.stat().st_size == manifest['files'][0]['bytes']
    table = re.search(r'id="tbl1".*?<tbody[^>]*>(.*?)</tbody>', html, re.S).group(1)
    source_rows = re.findall(r'<tr>(.*?)</tr>', table, re.S)
    observed = list(csv.DictReader((HERE / 'growth-summary.csv').open()))
    expected = [('0.047','0.004','c'), ('0.005','0.001','d'),
                ('0.119','0.002','a'), ('0.011','0.000','d'),
                ('0.044','0.000','c'), ('0.006','0.001','d'),
                ('0.100','0.001','b'), ('0.010','0.001','d')]
    independent = []
    for row in source_rows:
        cells = re.findall(r'<td\b[^>]*>(.*?)</td>', row, re.S)
        cells = [''.join(unescape(re.sub('<[^>]+>', '', c)).split()) for c in cells]
        for value in cells[1:]:
            independent.append(re.fullmatch(r'([0-9.]+)±([0-9.]+)([a-z])', value).groups())
    assert independent == expected
    assert [(x['mean'], x['se'], x['group']) for x in observed] == expected
    assert [x['strain'] for x in observed] == ['SBW25']*4 + ['WS']*4
    assert [(x['mixing'],x['oxygen']) for x in observed] == [('static','high'),('static','low'),('shaken','high'),('shaken','low')]*2
    summary = json.loads((HERE / 'oxygen-summary.json').read_text())
    assert summary['source_sha256'] == sha(SOURCE)
    assert [(x['mean'],x['se'],x['n'],x['comparator']) for x in summary['competition']] == [('1.23','0.15',8,'SM-13'),('0.12','0.07',8,'SM-13')]
    text = unescape(re.sub('<[^>]+>', '', html))
    assert 'W=1.23±0.15' in text and 'W=0.12±0.07' in text
    assert 'n=8 for each condition' in text
    assert not summary['raw_replicates_retrieved'] and not summary['fitted_mat_viability_model']
    receipt = dict(status='pass', growth_summary_values_checked=8,
                   competition_summary_values_checked=2,
                   validation='Two extraction methods plus manually read source values; no author statistics rerun.',
                   new_lean_theorems=0, biological_replication=False,
                   source_sha256=sha(SOURCE),
                   bindings={p.name:sha(p) for p in [HERE/'read_evidence.py', HERE/'check_evidence.py', HERE/'growth-summary.csv', HERE/'oxygen-summary.json']})
    (HERE / 'verification.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
