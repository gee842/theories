#!/usr/bin/env python3
"""R35: Markdown links inside record history notes to files R35's batches moved. The move tool rewrites path strings
and Markdown links in live files but not links inside the prose of a record's `history` (rendered on the record
page); this rewrites their targets to the history paths, by the move receipts, and changes nothing else in the note.

usage (from the checkout root): python3 -B history_links.py [--apply]
"""
import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RECORDS = ROOT / 'theories/becoming/results/records'
fmap = {}
for r in sorted(glob.glob(str(ROOT / '_process/architecture/moves/R35-*.json'))):
    for f in json.load(open(r)).get('files', []):
        fmap[f['old_path']] = f['new_path']
LINK = re.compile(r'\]\(([^)\s#]+)(#[^)\s]*)?\)')
n = 0
for f in sorted(RECORDS.glob('*.json')):
    d = json.loads(f.read_text())
    changed = False
    for h in d.get('history', []):
        for lang in ('en', 'zh'):
            text = h.get(lang)
            if not isinstance(text, str) or '](' not in text:
                continue

            def sub(m):
                target = m.group(1)
                path = os.path.normpath(os.path.join('theories/becoming/results/records', target))
                if path in fmap:
                    new = os.path.relpath(fmap[path], 'theories/becoming/results/records')
                    return f']({new}{m.group(2) or ""})'
                return m.group(0)
            new = LINK.sub(sub, text)
            if new != text:
                h[lang] = new
                changed = True
    if changed:
        n += 1
        print(d['id'])
        if '--apply' in sys.argv:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(n, 'records')
