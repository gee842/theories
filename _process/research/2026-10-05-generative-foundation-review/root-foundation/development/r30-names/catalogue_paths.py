"""R30: the reading catalogue's data (theories/becoming/results/data/arguments-*.json, not generated) names the Lean
files of the chapters it reads; the four renamed modules' paths follow the table's `paths`. Nothing else changes (the
reviewed source hashes are the review gate and are not refreshed). Run from the checkout root."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATHS = json.loads((HERE / 'RENAME-TABLE.json').read_text())['paths']
for f in sorted(Path('theories/becoming/results/data').glob('arguments-*.json')):
    s = f.read_text(encoding='utf-8')
    n = sum(s.count('"' + o + '"') for o in PATHS)
    for o, new in PATHS.items():
        s = s.replace('"' + o + '"', '"' + new + '"')
    if n:
        f.write_text(s, encoding='utf-8')
    print(f, n)
