"""Retrospective descriptive check of a derived public browser preview.

No statistical significance, welfare, or energetic-cost inference is made.
The FNV receipt compares all ASCII cell strings to the observed DOM extraction;
it is a transcription check, not authentication of original CSV bytes.
"""
import csv
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data_path = HERE / 'experiment4-preview.tsv'
rows = list(csv.reader(data_path.read_text().splitlines(), delimiter='\t'))
assert len(rows) == 49 and all(len(row) == 10 for row in rows)
preview = [row.copy() for row in rows]
preview[0][0] = ''
canonical = json.dumps(preview, separators=(',', ':'), ensure_ascii=False)
fnv = 14695981039346656037
for b in canonical.encode('ascii'):
    fnv = ((fnv ^ b) * 1099511628211) % (2**64)
assert len(canonical) == 3119 and f'{fnv:x}' == 'df8ebe2256185e27'
records = list(csv.DictReader(data_path.read_text().splitlines(), delimiter='\t'))
assert [int(row['preview_row']) for row in records] == list(range(1, 49))
pairs = {}
for row in records:
    treatment = row['treatment']
    assert treatment in ('neutral', 'cooperating')
    pair = pairs.setdefault(row['ratID'], {})
    assert treatment not in pair
    pair[treatment] = int(row['pull_f'])
assert len(pairs) == 24 and all(len(pair) == 2 for pair in pairs.values())
totals = {t: sum(pair[t] for pair in pairs.values()) for t in ('neutral', 'cooperating')}
diff = [pair['cooperating']-pair['neutral'] for pair in pairs.values()]
signs = Counter('higher' if d > 0 else 'lower' if d < 0 else 'equal' for d in diff)
report = dict(
    scope='Retrospective descriptive browser-preview calculation; no inferential replication.',
    source='https://datadryad.org/dataset/doi:10.5061/dryad.h18931zjd',
    version=93077, experiment='experiment4.csv public HTML preview',
    row_count=len(records), paired_focal_ids=len(pairs),
    pull_totals=totals,
    mean_pulls={t: str(Fraction(n, 24)) for t, n in totals.items()},
    paired_pull_difference_mean=str(Fraction(sum(diff), 24)),
    paired_direction=dict(signs),
    missing_cells={k: sum(row[k] == 'NA' for row in records) for k in rows[0]
                   if any(row[k] == 'NA' for row in records)},
    transcription=dict(canonical_ascii_length=len(canonical), fnv1a64=f'{fnv:x}',
                       header_adaptation='Blank first header renamed preview_row'),
    file_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in (data_path, Path(__file__))},
    original_csv_downloaded=False,
    original_csv_bytes_verified=False,
)
(HERE / 'preview-check.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
